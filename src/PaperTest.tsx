import React, { useState, useRef, useEffect, useMemo } from 'react';
import { supabase } from './supabase';
import './tailwind.css';

// --- CÁC HÀM LOGIC DÙNG CHUNG TỪ COMPUTER TEST ---
const stripHtmlRegex = /[<][^>]*[>]/g;

const isRealContent = (htmlContent: any) => {
  const str = String(htmlContent || '');
  const rawText = str.replace(stripHtmlRegex, '').replace(/&nbsp;/gi, '').replace(/\s+/g, '');
  return rawText !== '' || str.includes('<img') || str.includes('<audio');
};

const buildCheckboxCombos = (questions: any[]) => {
  const combos: any[][] = [];
  (Array.isArray(questions) ? questions : []).forEach((q: any) => {
    if (combos.length === 0) {
      combos.push([q]); return;
    }
    const prevQ = combos[combos.length - 1][0];
    const contentEmpty = !isRealContent(q.content);
    const getOptStr = (qq: any) => JSON.stringify((qq.options || []).map((o:any) => String(o).replace(stripHtmlRegex, '').trim()).filter(Boolean));
    const currOpts = getOptStr(q);
    const prevOpts = getOptStr(prevQ);
    const hasSameOptions = currOpts === prevOpts && currOpts !== '[]';
    const hasNoOptions = currOpts === '[]';
    const normalizeText = (text: string) => String(text || '').replace(stripHtmlRegex, '').replace(/\(\d+\)|\[\d+\]|\d+\./g, '').trim().toLowerCase();
    const currText = normalizeText(q.content);
    const prevText = normalizeText(prevQ.content);
    const hasSameContent = currText === prevText && currText !== '';

    if (contentEmpty || hasSameOptions || hasNoOptions || hasSameContent) combos[combos.length - 1].push(q);
    else combos.push([q]); 
  });
  return combos;
};

// LOGIC CHẤM ĐIỂM (HỖ TRỢ NGOẶC ĐƠN)
const isAnswerCorrect = (userAns: string, correctAns: string) => {
  if (!userAns || !correctAns) return false;
  const u = String(userAns).trim().toUpperCase().replace(/\s+/g, ' ');
  const cArr = String(correctAns).split('/').map(x => x.trim().toUpperCase().replace(/\s+/g, ' '));
  
  for (const c of cArr) {
    if (u === c) return true;
    const uMatch = u.match(/^([A-Z])[\.\):]/);
    if (uMatch && uMatch[1] === c) return true;
    const cMatch = c.match(/^([A-Z])[\.\):]/);
    if (cMatch && u === cMatch[1]) return true;

    if (c.includes('(') && c.includes(')')) {
      const withoutParens = c.replace(/\(.*?\)/g, '').replace(/\s+/g, ' ').trim();
      const withParensContent = c.replace(/[\(\)]/g, '').replace(/\s+/g, ' ').trim();
      if (u === withoutParens || u === withParensContent) return true;
    }
  }
  return false;
};

const parseStyle = (styleStr: string) => {
  const style: any = {};
  if (!styleStr) return style;
  styleStr.split(';').forEach(s => {
    const match = s.match(/^\s*([\w-]+)\s*:\s*(.+)\s*$/);
    if (match) {
      const [, key, val] = match;
      const camelKey = key.replace(/-([a-z])/g, g => g[1].toUpperCase());
      style[camelKey] = val;
    }
  });
  return style;
};

// --- COMPONENT CHÍNH ---
export default function PaperTest({ onBack, testData, onFinish }: { onBack: () => void, testData?: any, onFinish?: (res: any) => void }) {
  let safeTestData = testData;
  if (typeof safeTestData === 'string') {
    try { safeTestData = JSON.parse(safeTestData); } catch (e) { }
  }

  const contentJSON = safeTestData?.content_json || safeTestData || {};
  const basicInfo = contentJSON.basicInfo || { title: "IELTS Paper-based", timeLimit: "60", skill: "" };
  const parts = Array.isArray(contentJSON.parts) ? contentJSON.parts : [];
  
  const isListening = basicInfo.skill?.toLowerCase().includes('listening') || String(safeTestData?.test_type || '').toLowerCase().includes('listening');
  const globalAudio = basicInfo.audioUrl || parts?.[0]?.audioUrl;

  const [testStarted, setTestStarted] = useState(false);
  const [isReviewMode, setIsReviewMode] = useState(false);
  const [scoreResult, setScoreResult] = useState({ score: 0, total: 0, band: "0.0" });
  
  const globalAudioRef = useRef<HTMLAudioElement>(null);
  const isFinishingRef = useRef(false);

  // States cơ bản
  const [answers, setAnswers] = useState<Record<string, string>>(() => {
    try {
      const saved = localStorage.getItem(`ielts_paper_ans_${safeTestData?.id}`);
      return saved ? JSON.parse(saved) : {};
    } catch (error) { return {}; }
  });
  
  const [reviewFlags, setReviewFlags] = useState<Record<string, boolean>>({});
  const [activeQuestionId, setActiveQuestionId] = useState<string>('');
  const [draggedOption, setDraggedOption] = useState<string | null>(null);

  // Resize Cột Trái/Phải (Thanh Kéo)
  const [leftWidth, setLeftWidth] = useState(50);
  const containerRef = useRef<HTMLDivElement>(null);
  const leftPaneRef = useRef<HTMLDivElement>(null);
  const isDragging = useRef(false);

  const startDrag = () => { 
      isDragging.current = true; 
      document.body.style.cursor = 'col-resize'; 
      document.body.style.userSelect = 'none'; 
  };
  
  const stopDrag = () => { 
      isDragging.current = false; 
      document.body.style.cursor = 'default'; 
      document.body.style.userSelect = 'auto'; 
  };
  
  const onDrag = (e: MouseEvent) => {
    if (!isDragging.current || !containerRef.current) return;
    const containerRect = containerRef.current.getBoundingClientRect(); 
    const newLeftWidth = ((e.clientX - containerRect.left) / containerRect.width) * 100;
    if (newLeftWidth > 20 && newLeftWidth < 80) setLeftWidth(newLeftWidth);
  };

  useEffect(() => { 
      window.addEventListener('mousemove', onDrag); 
      window.addEventListener('mouseup', stopDrag); 
      return () => { 
          window.removeEventListener('mousemove', onDrag); 
          window.removeEventListener('mouseup', stopDrag); 
      }; 
  }, []);

  // Lưu bản nháp
  useEffect(() => {
    if (!isReviewMode && !isFinishingRef.current && safeTestData?.id) {
      localStorage.setItem(`ielts_paper_ans_${safeTestData.id}`, JSON.stringify(answers));
    }
  }, [answers, safeTestData?.id, isReviewMode]);

  const handleAnswer = (qNum: string, value: string) => { 
    if (!isReviewMode) {
      setAnswers(prev => ({ ...prev, [String(qNum)]: String(value) }));
      setActiveQuestionId(String(qNum)); 
    }
  };

  const getSavedEndTime = () => {
    if (!safeTestData?.id) return null;
    const saved = localStorage.getItem(`ielts_paper_endtime_${safeTestData.id}`);
    return saved ? parseInt(saved, 10) : null;
  };

  const parseInitialTime = (timeStr: string) => {
    if (!timeStr) return 3600; 
    const timeParts = String(timeStr).replace(/[^0-9:]/g, '').split(':');
    return timeParts.length === 2 ? parseInt(timeParts[0]) * 60 + parseInt(timeParts[1]) : (parseInt(timeParts[0]) || 60) * 60;
  };

  const [timeLeft, setTimeLeft] = useState(() => parseInitialTime(basicInfo.timeLimit));

  const clearDraft = () => {
    if(window.confirm('Xóa bản nháp và làm lại từ đầu?')) { 
      if (safeTestData?.id) {
        localStorage.removeItem(`ielts_paper_ans_${safeTestData.id}`);
        localStorage.removeItem(`ielts_paper_endtime_${safeTestData.id}`);
      }
      setAnswers({}); 
      setReviewFlags({});
      const initialSeconds = parseInitialTime(basicInfo.timeLimit);
      const newEndTime = Date.now() + initialSeconds * 1000;
      if (safeTestData?.id) localStorage.setItem(`ielts_paper_endtime_${safeTestData.id}`, newEndTime.toString());
      setTimeLeft(initialSeconds);
    }
  };

  // NỘP BÀI VÀ TÍNH ĐIỂM
  const handleFinish = async () => {
    if (!isReviewMode) {
      if (!window.confirm("Bạn có chắc chắn muốn nộp bài thi?")) return;
      isFinishingRef.current = true;
      if (safeTestData?.id) {
        localStorage.removeItem(`ielts_paper_ans_${safeTestData.id}`);
        localStorage.removeItem(`ielts_paper_endtime_${safeTestData.id}`);
      }

      let score = 0; 
      let total = 0;
      let questionTypeStats: Record<string, { correct: number, total: number }> = {};

      parts.forEach((p: any) => {
        if (!Array.isArray(p.sections)) return;
        p.sections.forEach((s: any) => {
          const qType = s.questionType || 'Khác';
          if (!questionTypeStats[qType]) questionTypeStats[qType] = { correct: 0, total: 0 };
          if (!Array.isArray(s.questions)) return;

          if (qType === 'Checkbox') {
            const combos = buildCheckboxCombos(s.questions);
            combos.forEach(combo => {
              const comboIds = combo.map((q: any) => String(q.id));
              const userAnsComboSet = new Set(comboIds.map(id => answers[id]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase())));
              const correctAnsComboSet = new Set(combo.flatMap((q:any) => String(q.correctAnswer || '').split(',').map((x:string)=>x.trim().toUpperCase()).filter(Boolean)));
              
              let comboPoints = 0;
              userAnsComboSet.forEach(ans => {
                let isMatched = false;
                correctAnsComboSet.forEach(c => {
                  if (isAnswerCorrect(ans, c)) isMatched = true;
                });
                if (isMatched) comboPoints++;
              });
              comboPoints = Math.min(comboPoints, combo.length); 
              
              score += comboPoints;
              total += combo.length;
              questionTypeStats[qType].correct += comboPoints;
              questionTypeStats[qType].total += combo.length;
            });
          } else {
            s.questions.forEach((q: any) => {
              if (!q?.id) return;
              total++;
              questionTypeStats[qType].total++;
              const userAns = String(answers[String(q.id)] || "");
              const correctAns = String(q.correctAnswer || "");
              
              if (isAnswerCorrect(userAns, correctAns) && correctAns.trim() !== "") {
                 score++; questionTypeStats[qType].correct++;
              }
            });
          }
        });
      });

      let band = "0.0";
      if (score >= 39) band = "9.0"; else if (score >= 37) band = "8.5";
      else if (score >= 35) band = "8.0"; else if (score >= 33) band = "7.5";
      else if (score >= 30) band = "7.0"; else if (score >= 27) band = "6.5";
      else if (score >= 23) band = "6.0"; else if (score >= 19) band = "5.5";
      else if (score >= 15) band = "5.0"; else if (score >= 13) band = "4.5";
      else if (score >= 10) band = "4.0"; else if (score >= 8) band = "3.5";
      else if (score >= 6) band = "3.0"; else if (score >= 4) band = "2.5";
      else if (score >= 2) band = "2.0"; else if (score >= 1) band = "1.0";
      
      setScoreResult({ score, total, band }); 
      setIsReviewMode(true); 
      window.scrollTo({ top: 0, behavior: 'smooth' });

      try {
        const { data: { user } } = await supabase.auth.getUser();
        if (user) {
          const timeSpentSecs = parseInitialTime(basicInfo.timeLimit) - timeLeft;
          await supabase.from('test_results').insert([{
            user_id: user.id, 
            course_id: safeTestData?.course_id || safeTestData?.content_json?.basicInfo?.courseId || null,
            test_title: basicInfo.title || safeTestData?.title || "IELTS Test", 
            test_type: safeTestData?.test_type || 'IELTS Paper',
            score: score, 
            total_score: total, 
            time_spent: timeSpentSecs > 0 ? timeSpentSecs : 0,
            details: { test_id: safeTestData?.id, bandScore: band, userAnswers: answers, questionTypeStats: questionTypeStats }
          }]);
        }
      } catch (error) { 
        console.error("Lỗi lưu kết quả thi:", error);
      }
    } else {
      if (onFinish) {
        onFinish({ score: scoreResult.score, total: scoreResult.total, testTitle: basicInfo.title, bandScore: scoreResult.band });
      } else {
        onBack();
      }
    }
  };

  const resetTest = () => {
    if (window.confirm("Làm lại từ đầu? Mọi đáp án sẽ bị xóa.")) { 
      if (safeTestData?.id) localStorage.removeItem(`ielts_paper_endtime_${safeTestData.id}`);
      setAnswers({}); 
      setReviewFlags({});
      setIsReviewMode(false); 
      setTestStarted(false); 
      setTimeLeft(parseInitialTime(basicInfo.timeLimit)); 
    }
  };

  // MAP DỮ LIỆU CÂU HỎI
  const { allQuestionIds, questionIndexMap, questionDataMap } = useMemo(() => {
    const ids: string[] = [];
    const dataMap: Record<string, { qType: string, options: string[] }> = {};
    
    parts.forEach((p: any) => {
      if (Array.isArray(p?.sections)) {
        p.sections.forEach((s: any) => {
          if (Array.isArray(s?.questions)) {
             s.questions.forEach((q: any) => {
                const qIdStr = String(q.id);
                if (q?.id && !ids.includes(qIdStr)) {
                  ids.push(qIdStr);
                  dataMap[qIdStr] = { qType: s.questionType, options: q.options || [] };
                }
             });
          }
          if (["Điền từ", "Kéo thả vào Part", "Kéo thả", "Matching", "Droplist"].includes(s?.questionType)) {
            const combinedContent = String(s?.content || '') + ' ' + String(s?.questions?.[0]?.content || '');
            const matches = combinedContent.match(/\[\s*\d+\s*\]/g);
            if (matches) {
              matches.forEach((m: string) => { 
                 const num = m.replace(/\D/g, '').trim(); 
                 if (!ids.includes(num)) {
                    ids.push(num); 
                    const qInSec = (s.questions || []).find((qq:any) => String(qq.id) === num);
                    dataMap[num] = { qType: s.questionType, options: qInSec?.options || s.questions?.[0]?.options || [] };
                 }
              });
            }
          }
        });
      }
    });
    
    ids.sort((a, b) => parseInt(a) - parseInt(b));
    const idxMap = ids.reduce((acc: any, id: string, idx: number) => { acc[id] = idx + 1; return acc; }, {});
    return { allQuestionIds: ids, questionIndexMap: idxMap, questionDataMap: dataMap };
  }, [parts]);

  const scrollToQuestion = (qNum: number | string) => {
    setActiveQuestionId(String(qNum));
    const el = document.getElementById(`q-${qNum}`);
    if (el) { 
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        el.classList.add('bg-blue-100', 'transition-colors', 'duration-500'); 
        setTimeout(() => el.classList.remove('bg-blue-100'), 1500); 
    }
  };

  // Timer
  useEffect(() => {
    if (!testStarted || isReviewMode) return;
    const timer = setInterval(() => { 
        const currentEndTime = getSavedEndTime();
        if (currentEndTime) {
            const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
            setTimeLeft(remaining);
            if (remaining <= 0) {
                clearInterval(timer);
                alert("⏰ Hết giờ!");
                handleFinish();
            }
        } else { 
            setTimeLeft(prev => prev - 1); 
        }
    }, 1000);
    return () => clearInterval(timer);
  }, [testStarted, isReviewMode]);

  const formatTime = (seconds: number) => { 
      return `${Math.floor(seconds / 60).toString().padStart(2, '0')}:${(seconds % 60).toString().padStart(2, '0')}`;
  };

  // Tools: Copy, Highlight, Notes
  const [highlightMenu, setHighlightMenu] = useState({ x: 0, y: 0, show: false });
  const [currentRange, setCurrentRange] = useState<Range | null>(null);
  const [stickyNote, setStickyNote] = useState({ show: false, id: '', text: '', x: 0, y: 0 });

  const handleMouseUp = () => {
    if (isReviewMode) return;
    const selection = window.getSelection();
    if (selection && selection.toString().trim().length > 0) {
      // FIX LỖI: Chỉ hiện highlight khi bôi đen nội dung trong Cột Trái (Bài đọc)
      if (leftPaneRef.current && leftPaneRef.current.contains(selection.anchorNode)) {
          const range = selection.getRangeAt(0);
          const rect = range.getBoundingClientRect();
          setHighlightMenu({ x: rect.left + rect.width / 2, y: rect.top - 10, show: true }); 
          setCurrentRange(range);
          return;
      }
    }
    setHighlightMenu({ ...highlightMenu, show: false }); 
    setCurrentRange(null);
  };

  const handleCopy = async () => { 
      if (currentRange) { 
          await navigator.clipboard.writeText(currentRange.toString());
          setHighlightMenu({ ...highlightMenu, show: false }); 
          window.getSelection()?.removeAllRanges(); 
      } 
  };

  const applyHighlight = () => { 
      if (currentRange) { 
          const span = document.createElement('span');
          span.className = 'bg-yellow-300 cursor-pointer rounded-sm'; 
          try { currentRange.surroundContents(span); } catch (e) {} 
          setHighlightMenu({ ...highlightMenu, show: false });
          window.getSelection()?.removeAllRanges(); 
      } 
  };

  const initNote = () => {
    if (currentRange) {
      const noteId = 'note_' + new Date().getTime();
      const span = document.createElement('span'); 
      span.className = 'bg-yellow-300 cursor-pointer rounded-sm border-b-2 border-red-500'; 
      span.dataset.noteId = noteId; 
      span.dataset.noteText = '';
      try { 
          currentRange.surroundContents(span); 
          const rect = span.getBoundingClientRect();
          setStickyNote({ show: true, id: noteId, text: '', x: rect.left, y: rect.bottom + 10 });
      } catch (e) { alert("Chỉ bôi đen gọn trong 1 đoạn văn!"); }
      setHighlightMenu({ ...highlightMenu, show: false }); 
      window.getSelection()?.removeAllRanges();
    }
  };

  const handleContentClick = (e: React.MouseEvent) => {
    const target = e.target as HTMLElement;
    if (target.tagName === 'SPAN' && target.dataset.noteId) { 
        const rect = target.getBoundingClientRect();
        setStickyNote({ show: true, id: target.dataset.noteId, text: target.dataset.noteText || '', x: rect.left, y: rect.bottom + 10 }); 
    }
  };

  // Drag and Drop & Auto Scroll Logic
  const mainScrollRef = useRef<HTMLElement>(null);
  const scrollRafRef = useRef<number | null>(null);
  const autoScrollSpeed = useRef<number>(0);

  const startAutoScroll = () => {
    if (scrollRafRef.current) return; 
    const scrollStep = () => {
      if (mainScrollRef.current && autoScrollSpeed.current !== 0) {
        mainScrollRef.current.scrollTop += autoScrollSpeed.current;
        scrollRafRef.current = requestAnimationFrame(scrollStep);
      } else {
        scrollRafRef.current = null;
      }
    };
    scrollRafRef.current = requestAnimationFrame(scrollStep);
  };

  const stopAutoScroll = () => {
    autoScrollSpeed.current = 0;
    if (scrollRafRef.current) {
      cancelAnimationFrame(scrollRafRef.current);
      scrollRafRef.current = null;
    }
  };

  useEffect(() => {
    const handleGlobalDragOver = (e: DragEvent) => {
      if (!draggedOption || !mainScrollRef.current) return;
      const container = mainScrollRef.current;
      const rect = container.getBoundingClientRect();
      const threshold = 120;
      
      const y = e.clientY;
      const x = e.clientX;

      if (x < rect.left || x > rect.right || y < rect.top || y > rect.bottom) {
        stopAutoScroll(); return;
      }

      if (y >= rect.top && y < rect.top + threshold) {
        autoScrollSpeed.current = -25 * (1 - (y - rect.top) / threshold) - 2;
        startAutoScroll();
      } else if (y <= rect.bottom && y > rect.bottom - threshold) {
        autoScrollSpeed.current = 25 * (1 - (rect.bottom - y) / threshold) + 2;
        startAutoScroll();
      } else { stopAutoScroll(); }
    };

    if (draggedOption) window.addEventListener('dragover', handleGlobalDragOver);
    else stopAutoScroll();

    return () => {
      window.removeEventListener('dragover', handleGlobalDragOver);
      stopAutoScroll();
    }
  }, [draggedOption]);

  const onDragStart = (option: string) => {
    if (isReviewMode) return;
    setDraggedOption(option);
  };

  const onDrop = (qId: string) => {
    stopAutoScroll();
    if (isReviewMode || !draggedOption) return;
    handleAnswer(qId, draggedOption);
    setDraggedOption(null);
  };

  const clearDragAnswer = (qId: string) => {
    if (isReviewMode) return;
    handleAnswer(qId, '');
  };

  // RENDER HTML CHỨA ĐỤC LỖ - STYLE CỦA PAPER TEST
  const renderHtmlWithHoles = (htmlStr: any, sec: any) => {
    if (!htmlStr) return null;
    const safeText = String(htmlStr);

    if (typeof window === 'undefined') {
        return <span dangerouslySetInnerHTML={{ __html: safeText }} />;
    }

    const processedHtml = safeText.replace(/\[\s*(\d+)\s*\]/g, '<hole data-id="$1"></hole>');
    const parser = new DOMParser();
    const doc = parser.parseFromString(processedHtml, 'text/html');
    
    const sectionQIds = (sec?.questions || []).map((q:any) => String(q.id));
    const selectedInSec = sectionQIds.map((id:string) => answers[id]?.trim().toUpperCase()).filter(Boolean);

    const renderNode = (node: ChildNode, pathKey: string): React.ReactNode => {
      if (node.nodeType === Node.TEXT_NODE) return node.textContent;
      if (node.nodeType === Node.ELEMENT_NODE) {
        const el = node as HTMLElement;
        const tagName = el.tagName.toLowerCase();
        
        if (tagName === 'hole') {
            const qNum = el.getAttribute('data-id');
            if (!qNum) return null;

            const userAns = String(answers[qNum] || '');
            const displayIndex = questionIndexMap[qNum] || qNum;
            const qInfo = questionDataMap[qNum] || { qType: sec?.questionType || 'Điền từ', options: [] };

            // REVIEW MODE
            if (isReviewMode) {
              const qData = parts.flatMap((p: any) => Array.isArray(p?.sections) ? p.sections.flatMap((s: any) => s?.questions) : []).find((q: any) => String(q?.id) === String(qNum));
              const correctAns = String(qData?.correctAnswer || '');
              const isCorrect = isAnswerCorrect(userAns, correctAns);

              return (
                <span key={pathKey} className="relative inline-flex flex-col items-center mx-1 align-baseline -translate-y-1">
                  <span className={`px-2.5 py-0.5 text-[14px] font-bold text-slate-800 rounded shadow-sm border ${isCorrect ? 'bg-emerald-100 border-emerald-300' : 'bg-red-100 border-red-300'}`}>
                    {displayIndex}. {userAns || '(trống)'}
                  </span>
                  {!isCorrect && (
                    <span className="absolute top-full mt-1 text-[11px] text-emerald-800 font-bold bg-emerald-100 px-2 py-0.5 border border-emerald-300 rounded text-center whitespace-nowrap z-10 shadow-md">
                      ĐA: {correctAns}
                    </span>
                  )}
                </span>
              );
            }

            // KÉO THẢ INLINE (Paper Style)
            if (["Kéo thả", "Kéo thả vào Part", "Matching"].includes(sec.questionType)) {
                const displayUserAns = userAns ? userAns.replace(/^[A-Z][\.\):]\s*/i, '') : '';
                return (
                    <span 
                      key={pathKey} 
                      id={`q-${qNum}`} 
                      onDragOver={(e) => e.preventDefault()} 
                      onDrop={() => onDrop(qNum)} 
                      onClick={(e) => { e.stopPropagation(); setActiveQuestionId(String(qNum)); }} 
                      className={`inline-flex items-center justify-center align-middle mx-1 min-w-[120px] h-[30px] border rounded transition-all px-2 cursor-pointer ${activeQuestionId === String(qNum) ? 'border-blue-600 bg-blue-50' : 'border-gray-400 bg-gray-50 hover:bg-gray-100'}`}
                    >
                        <span className="font-bold text-gray-700 text-[13px] mr-2">{displayIndex}.</span>
                        {userAns ? (
                            <div className="flex items-center justify-between w-full text-blue-800 text-[14px] font-bold">
                                <span className="truncate">{displayUserAns}</span>
                                <button onClick={(e) => { e.stopPropagation(); clearDragAnswer(qNum); }} className="ml-2 hover:text-red-500 text-[14px] font-black">✕</button>
                            </div>
                        ) : ( <span className="text-gray-400 text-[13px] italic w-full text-center">Thả vào đây</span> )}
                    </span>
                );
            }

            // DROPLIST INLINE
            if (qInfo.qType === 'Droplist' || sec.questionType === "Droplist") {
               const rawOptions = (qInfo.options && qInfo.options.length > 0) ? qInfo.options : (sec.questions?.[0]?.options || []);
               const validOptions = rawOptions.filter(Boolean);
               
               return (
                 <span key={pathKey} id={`q-${qNum}`} className="inline-flex items-center align-baseline mx-1">
                    <span className="font-bold text-[15px] mr-1 text-slate-700">{displayIndex}.</span>
                    <select 
                      value={userAns}
                      onFocus={() => setActiveQuestionId(qNum)}
                      onChange={(e) => handleAnswer(qNum, e.target.value)}
                      className="border-b-2 border-slate-400 bg-transparent focus:border-blue-600 rounded-none px-1 py-0.5 outline-none text-blue-800 font-bold text-[14px] min-w-[100px] max-w-[200px] cursor-pointer"
                    >
                      <option value="">-- Chọn --</option>
                      {validOptions.map((opt:string, oIdx:number) => {
                         const val = opt.replace(stripHtmlRegex, '').trim();
                         const isSelectedElsewhere = selectedInSec.includes(val.toUpperCase()) && userAns.trim().toUpperCase() !== val.toUpperCase();
                         return (
                           <option key={oIdx} value={val}>
                             {val} {isSelectedElsewhere ? '(Đã chọn)' : ''}
                           </option>
                         );
                      })}
                    </select>
                 </span>
               );
            }

            // ĐIỀN TỪ INLINE
            return (
              <span key={pathKey} id={`q-${qNum}`} onClick={(e) => { e.stopPropagation(); setActiveQuestionId(String(qNum)); }} className="inline-flex items-baseline mx-1">
                <span className="font-bold text-[15px] mr-1 text-slate-700">{displayIndex}.</span>
                <input 
                  type="text" 
                  className="w-32 border-b-2 border-slate-400 focus:outline-none focus:border-blue-600 bg-transparent text-center text-blue-800 font-bold px-1 text-[15px] leading-tight pb-0.5" 
                  value={userAns} 
                  onFocus={() => setActiveQuestionId(String(qNum))}
                  onChange={(e) => handleAnswer(qNum, e.target.value)} 
                  autoComplete="off"
                  spellCheck="false"
                />
              </span>
            );
        }

        const props: any = { key: pathKey };
        Array.from(el.attributes).forEach(attr => {
          if (attr.name === 'class') props.className = attr.value;
          else if (attr.name === 'style') props.style = parseStyle(attr.value);
          else if (attr.name === 'for') props.htmlFor = attr.value;
          else if (attr.name.startsWith('data-') || attr.name.startsWith('aria-')) props[attr.name] = attr.value;
          else {
            const camelCaseAttr = attr.name.replace(/-([a-z])/g, g => g[1].toUpperCase());
            const reactProp = attr.name === 'colspan' ? 'colSpan' : attr.name === 'rowspan' ? 'rowSpan' : attr.name === 'cellpadding' ? 'cellPadding' : attr.name === 'cellspacing' ? 'cellSpacing' : attr.name === 'tabindex' ? 'tabIndex' : camelCaseAttr;
            props[reactProp] = attr.value;
          }
        });

        const children = Array.from(el.childNodes).map((child, i) => renderNode(child, `${pathKey}-${i}`));
        const voidElements = ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'];
        if (voidElements.includes(tagName)) return React.createElement(tagName, props);
        return React.createElement(tagName, props, children.length > 0 ? children : null);
      }
      return null;
    };

    return Array.from(doc.body.childNodes).map((node, i) => renderNode(node, `root-${i}`));
  };

  const handleStartTest = () => {
    setTestStarted(true);
    let currentEndTime = getSavedEndTime();
    if (!currentEndTime) {
        const initialSeconds = parseInitialTime(basicInfo.timeLimit);
        currentEndTime = Date.now() + initialSeconds * 1000;
        if (safeTestData?.id) localStorage.setItem(`ielts_paper_endtime_${safeTestData.id}`, currentEndTime.toString());
        setTimeLeft(initialSeconds);
    } else {
        const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
        setTimeLeft(remaining);
        if (remaining <= 0) {
            alert("⏰ Bài thi này đã hết thời gian làm bài!");
            handleFinish();
            return;
        }
    }
    if (globalAudioRef.current && isListening) { 
        globalAudioRef.current.play().catch(e => { 
            console.error("Autoplay blocked:", e); 
            alert("Trình duyệt chặn phát âm thanh. Vui lòng bấm Bắt Đầu lại."); 
        });
    }
  };

  // MÀN HÌNH CHƯA BẮT ĐẦU THI
  if (!testStarted) {
    return (
      <div className="flex flex-col h-screen items-center justify-center bg-[#f3f4f6] font-serif">
        {isListening && globalAudio && <audio ref={globalAudioRef} src={globalAudio} preload="auto" className="hidden" />}
        <div className="bg-white p-10 rounded-2xl shadow-xl text-center max-w-lg border border-gray-200 w-full font-sans">
          <div className="text-6xl mb-6">{isListening ? '🎧' : '📝'}</div>
          <h1 className="text-2xl font-black text-slate-800 mb-2">{basicInfo.title}</h1>
          <p className="text-slate-500 mb-8 font-medium">Thời gian: {formatTime(parseInitialTime(basicInfo.timeLimit))}</p>
          {isListening && (
            <div className="bg-amber-50 border border-amber-200 p-4 rounded-lg text-amber-700 text-[13px] font-medium mb-8 text-left leading-relaxed shadow-inner">
              <span className="font-bold">⚠️ LƯU Ý THI LISTENING:</span> File âm thanh sẽ <span className="font-bold underline">tự động phát</span> ngay khi bạn bấm nút Bắt Đầu bên dưới.
              <br/><br/>Bạn chỉ có thể chỉnh âm lượng (Volume), KHÔNG THỂ tạm dừng hay tua lại.
            </div>
          )}
          <div className="flex gap-4 justify-center">
            <button onClick={onBack} className="px-6 py-3 rounded-lg font-bold text-slate-500 hover:bg-slate-100 border border-slate-300 transition">Quay lại</button>
            <button onClick={handleStartTest} className="bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-8 py-3 rounded-lg shadow-lg transition">Bắt Đầu Làm Bài</button>
          </div>
        </div>
      </div>
    );
  }

  // MÀN HÌNH LÀM BÀI CHÍNH THỨC
  return (
    <div className="flex flex-col h-screen bg-[#f3f4f6] font-serif text-gray-900 relative">
      
      {/* CSS fix giao diện vỡ bảng & Padding */}
      <style>{`
          .format-passage p { margin-bottom: 1.25rem !important; }
          .format-passage p:last-child { margin-bottom: 0 !important; }
          .format-passage br { display: block; content: ""; margin-bottom: 0.5rem; }
          
          .format-passage { overflow-x: auto; }
          .format-passage table { 
              width: 100% !important; 
              border-collapse: collapse !important; 
              margin: 1.5rem 0 !important; 
          }
          .format-passage th, .format-passage td { 
              border: 1px solid #cbd5e1 !important; 
              padding: 20px 16px !important; /* Mở rộng biên trên dưới */
              vertical-align: top !important; 
          }
          .format-passage th { 
              background-color: #f1f5f9; 
              font-weight: 900; 
              color: #1e293b; 
          }
          .format-passage td span { text-indent: 0 !important; }
          .format-passage td input, .format-passage td select { max-width: 100%; }
          
          /* Lùi bullet point sang trái tiết kiệm diện tích */
          .format-passage td ul, .format-passage td ol {
              padding-left: 16px !important;
              margin-top: 0 !important;
              margin-bottom: 0 !important;
          }
          .format-passage td li {
              margin-bottom: 8px !important;
          }
          .format-passage td li:last-child {
              margin-bottom: 0 !important;
          }
      `}</style>

      {isListening && globalAudio && !isReviewMode && ( <audio ref={globalAudioRef} src={globalAudio} preload="auto" className="hidden" /> )}

      {/* Menu Highlight */}
      {highlightMenu.show && !isReviewMode && (
        <div style={{ left: highlightMenu.x, top: highlightMenu.y, transform: 'translate(-50%, -100%)' }} className="fixed z-50 bg-white font-sans text-gray-800 rounded shadow-[0_4px_15px_rgba(0,0,0,0.15)] border border-gray-200 text-sm flex flex-col py-1 min-w-[130px]" onMouseDown={(e) => e.preventDefault()}>
          <button onClick={handleCopy} className="flex items-center gap-3 px-4 py-2 hover:bg-gray-100 text-left w-full"><span className="font-medium">Copy</span></button>
          <button onClick={applyHighlight} className="flex items-center gap-3 px-4 py-2 hover:bg-gray-100 text-left w-full"><span className="font-medium text-yellow-600">Highlight</span></button>
          <button onClick={initNote} className="flex items-center gap-3 px-4 py-2 hover:bg-gray-100 text-left w-full"><span className="font-medium text-blue-600">Note</span></button>
        </div>
      )}

      {/* Sticky Note */}
      {stickyNote.show && (
        <div style={{ left: Math.min(stickyNote.x, window.innerWidth - 300), top: stickyNote.y }} className="fixed z-50 flex flex-col shadow-2xl rounded border border-gray-300 w-72 font-sans">
          <div className="bg-[#4aa0e6] h-6 flex justify-between items-center px-2 cursor-move">
              <button onClick={() => setStickyNote({...stickyNote, show: false})} className="text-white text-xs">✕</button>
          </div>
          <div className="bg-[#f8f5dc] p-3 relative">
            <textarea autoFocus value={stickyNote.text} onChange={(e) => setStickyNote({ ...stickyNote, text: e.target.value })} className="w-full h-32 bg-transparent outline-none resize-none text-sm" placeholder="Nhập ghi chú..." disabled={isReviewMode} />
            {!isReviewMode && (
              <div className="flex justify-between items-center mt-2 border-t border-gray-300/50 pt-2">
                  <button onClick={() => { const span = document.querySelector(`span[data-note-id="${stickyNote.id}"]`) as HTMLElement; if (span && span.parentNode) span.parentNode.replaceChild(document.createTextNode(span.textContent || ''), span); setStickyNote({ ...stickyNote, show: false }); }} className="text-red-500 text-xs font-bold underline">Xóa Note</button>
                  <button onClick={() => { const span = document.querySelector(`span[data-note-id="${stickyNote.id}"]`) as HTMLElement; if (span) span.dataset.noteText = stickyNote.text; setStickyNote({ ...stickyNote, show: false }); }} className="bg-[#3b82f6] text-white text-xs font-bold px-4 py-1.5 rounded">Lưu</button>
              </div>
            )}
          </div>
        </div>
      )}

      {/* HEADER PAPER */}
      <header className="bg-white border-b border-gray-300 px-6 py-3 flex justify-between items-center shadow-sm z-20 shrink-0 font-sans">
        <div className="flex items-center gap-4">
          <button onClick={onBack} className="text-gray-600 hover:bg-gray-100 text-sm px-3 py-1.5 rounded-lg font-bold border border-gray-300 transition shrink-0">⬅ Thoát</button>
          <div className="font-bold text-lg text-gray-800 border-l border-gray-300 pl-4 truncate max-w-[200px] md:max-w-md">{isReviewMode ? `[CHỮA BÀI] ${basicInfo.title}` : basicInfo.title}</div>
        </div>

        {isListening && globalAudio && (
          <div className="flex-1 max-w-lg mx-8 flex items-center justify-center">
            {isReviewMode ? (
              <audio controls src={globalAudio} className="h-10 w-full outline-none" />
            ) : (
              <div className="flex items-center gap-3 bg-gray-100 px-4 py-1.5 rounded-full border border-gray-200">
                <span className="text-lg" title="Chỉnh âm lượng">🔊</span>
                <input type="range" min="0" max="1" step="0.05" defaultValue="1" onChange={(e) => { if(globalAudioRef.current) globalAudioRef.current.volume = parseFloat(e.target.value) }} className="w-32 accent-blue-500 cursor-pointer" />
              </div>
            )}
          </div>
        )}

        <div className="flex items-center gap-4 shrink-0">
          {!isReviewMode && <button onClick={clearDraft} className="text-sm text-gray-500 hover:text-red-500 font-medium">Xóa nháp</button>}
          {isReviewMode && <button onClick={resetTest} className="text-sm bg-gray-100 hover:bg-gray-200 px-3 py-1.5 rounded font-bold transition border border-gray-300">🔄 Làm Lại</button>}
          <div className={`font-mono text-xl px-4 py-1 rounded-md shadow-inner tracking-wider font-bold ${isReviewMode ? 'bg-emerald-600 text-white' : 'bg-gray-800 text-white'}`}>
              {isReviewMode ? `Band ${scoreResult.band}` : formatTime(timeLeft)}
          </div>
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="flex-1 overflow-y-auto p-8 relative" onMouseUp={handleMouseUp} ref={mainScrollRef as any}>
        <div className="max-w-7xl mx-auto space-y-12" onClick={handleContentClick} ref={containerRef as any}>
          
          {parts.map((part: any, pIndex: number) => {
            const hasPassage = part.content && part.content.trim().length > 0;
            const showTwoColumns = hasPassage || (isListening && isReviewMode && part.content); 

            return (
              <div key={pIndex} className="bg-white p-8 md:p-12 shadow-sm border border-gray-200 rounded-xl">
                
                <div className="text-center mb-8 border-b-2 border-gray-800 pb-4">
                  <h2 className="font-bold text-2xl uppercase tracking-widest text-gray-800 font-sans">{part.title}</h2>
                </div>

                <div className={`flex flex-col lg:flex-row items-stretch gap-0`}>
                  
                  {showTwoColumns && (
                    <>
                      <div className="format-passage text-justify leading-[1.8] text-[16px] pr-8" style={{ width: window.innerWidth > 1024 ? `${leftWidth}%` : '100%', flex: 'none' }} ref={leftPaneRef as any}>
                        {isReviewMode && isListening && <div className="bg-amber-100 text-amber-800 p-2 rounded font-bold text-xs mb-4 border border-amber-300 inline-block font-sans shadow-sm">🎙️ TAPESCRIPT</div>}
                        <div dangerouslySetInnerHTML={{ __html: part.content }} className="space-y-4" />
                      </div>
                      
                      {/* Thanh kéo Split-pane */}
                      {window.innerWidth > 1024 && (
                        <div className="w-4 bg-gray-50 border-x border-gray-200 hover:bg-gray-200 cursor-col-resize flex flex-col justify-center items-center shrink-0 transition-colors mx-4 rounded-full" onMouseDown={startDrag}>
                           <div className="flex flex-col gap-1.5 opacity-30">
                              <div className="w-1 h-1 bg-slate-600 rounded-full"></div>
                              <div className="w-1 h-1 bg-slate-600 rounded-full"></div>
                              <div className="w-1 h-1 bg-slate-600 rounded-full"></div>
                              <div className="w-1 h-1 bg-slate-600 rounded-full"></div>
                           </div>
                        </div>
                      )}
                    </>
                  )}

                  <div className={`${showTwoColumns ? 'pl-4' : ''}`} style={{ width: showTwoColumns && window.innerWidth > 1024 ? `calc(${100 - leftWidth}% - 2rem)` : '100%', flex: 'none' }}>
                    {part.sections?.map((sec: any, sIndex: number) => {
                      
                      let rawContentText = '';
                      if (String(sec.content || '').match(/\[\s*\d+\s*\]/)) {
                          rawContentText = sec.content;
                      } else if (String(sec.questions?.[0]?.content || '').match(/\[\s*\d+\s*\]/)) {
                          rawContentText = sec.questions[0].content;
                      } else {
                          rawContentText = sec.questions?.[0]?.content || '';
                      }

                      const hasInlineBrackets = /\[\s*\d+\s*\]/.test(rawContentText);
                      const isInlineDroplist = sec.questionType === "Droplist" && hasInlineBrackets;
                      const isBlockDroplist = sec.questionType === "Droplist" && !hasInlineBrackets;
                      const isInlineDragDrop = ["Kéo thả", "Matching", "Kéo thả vào Part"].includes(sec.questionType) && hasInlineBrackets;
                      const isBlockDragDrop = ["Kéo thả", "Matching", "Kéo thả vào Part"].includes(sec.questionType) && !hasInlineBrackets;
                      const secContentHasHoles = /\[\s*\d+\s*\]/.test(String(sec.content || ''));
                      const shouldRenderGlobalSecContent = sec.content && !secContentHasHoles;

                      return (
                        <div key={sIndex} className="mb-10 font-sans">
                          
                          {sec.title && (
                            <div className="bg-gray-100 border border-gray-300 px-4 py-2 mb-4 rounded">
                              <h4 className="font-bold text-gray-800">{sec.title}</h4>
                            </div>
                          )}

                          {shouldRenderGlobalSecContent && (
                             <div className="mb-6 text-[15px] font-bold text-slate-800 bg-gray-50 p-4 rounded-lg border border-gray-200" dangerouslySetInnerHTML={{ __html: sec.content }} />
                          )}

                          {/* DẠNG ĐIỀN TỪ & DROPLIST INLINE */}
                          {(sec.questionType === "Điền từ" || isInlineDroplist) && (
                            <div className={`border p-8 rounded-xl shadow-sm ${isReviewMode ? 'border-slate-300' : 'border-gray-200 bg-white'}`}>
                              {(() => {
                                let mainContent = rawContentText;
                                let wordBankItems: string[] = [];
                                const splitKeywords = ['<br><br>Options:<br>', '<br>Options:<br>', 'Options:<br>', 'Options:'];
                                for (const keyword of splitKeywords) {
                                    if (mainContent.includes(keyword)) {
                                        const partsArr = mainContent.split(keyword);
                                        mainContent = partsArr[0];
                                        wordBankItems = partsArr[1].split(/(?:<br\s*\/?>\s*)+/).filter((x:string) => x.replace(stripHtmlRegex, '').trim() !== '');
                                        break;
                                    }
                                }

                                return (
                                  <>
                                    <div className="format-passage space-y-6 leading-[2.5] text-[16px] font-serif text-slate-800">
                                      {renderHtmlWithHoles(mainContent, sec)}
                                    </div>
                                    {wordBankItems.length > 0 && (
                                        <div className="mt-8 p-5 bg-gray-50 border border-gray-200 rounded-lg">
                                            <p className="text-[13px] font-black text-gray-600 uppercase tracking-widest mb-4">Danh sách từ (Word Bank)</p>
                                            <div className="flex flex-wrap gap-3">
                                                {wordBankItems.map((item, idx) => {
                                                    const text = item.replace(stripHtmlRegex, '').trim();
                                                    return text ? (
                                                        <div key={idx} className="px-4 py-2 bg-white border border-gray-300 rounded font-bold text-gray-800 min-w-[100px] flex items-center shadow-sm" dangerouslySetInnerHTML={{ __html: text }} />
                                                    ) : null;
                                                })}
                                            </div>
                                        </div>
                                    )}
                                  </>
                                );
                              })()}
                            </div>
                          )}

                          {/* DẠNG TRẮC NGHIỆM & TFNG */}
                          {(sec.questionType === "Trắc nghiệm" || sec.questionType === "TFNG") && (
                            <div className="space-y-6">
                              {sec.questions?.map((q: any) => {
                                if (!q?.id) return null;
                                const correctAns = String(q.correctAnswer || '').trim().toUpperCase(); 
                                const userAns = String(answers[String(q.id)] || '').trim().toUpperCase(); 
                                const isCorrect = isAnswerCorrect(userAns, correctAns);
                                const displayIndex = questionIndexMap[q.id] || q.id;
                                
                                const validOptions = (Array.isArray(q.options) ? q.options : []).filter((opt: any) => String(opt || '').trim() !== '');
                                const isTFNG = sec.questionType === "TFNG" || validOptions.some((opt: string) => ['TRUE', 'FALSE', 'NOT GIVEN', 'YES', 'NO'].includes(opt?.trim()?.toUpperCase()));

                                // TFNG (Dàn hàng ngang)
                                if (isTFNG) {
                                   return (
                                      <div key={q.id} id={`q-${q.id}`} onClick={() => setActiveQuestionId(String(q.id))} className={`p-6 rounded-xl border shadow-sm transition-all ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-200' : 'bg-red-50/50 border-red-200') : (activeQuestionId === String(q.id) ? 'border-blue-400 bg-blue-50/30' : 'border-gray-200 bg-white hover:border-gray-300')}`}>
                                        <div className="flex gap-4 mb-2">
                                          <span className="font-bold text-gray-800 shrink-0 w-6 text-right pt-[2px]">{displayIndex}.</span>
                                          <div className="flex-1">
                                            {isReviewMode && (<div className="mb-3">{isCorrect ? <span className="text-[11px] font-bold bg-emerald-100 text-emerald-700 px-3 py-1 rounded">✅ ĐÚNG</span> : <span className="text-[11px] font-bold bg-red-100 text-red-700 px-3 py-1 rounded">❌ SAI</span>}</div>)}
                                            {q.content && <p className="text-[16px] mb-4 font-serif leading-relaxed" dangerouslySetInnerHTML={{ __html: q.content }}></p>}
                                            <div className={`flex flex-row flex-wrap gap-4`}>
                                              {validOptions.map((opt: any, i: number) => {
                                                const safeOpt = String(opt || '');
                                                const optionValue = safeOpt.replace(stripHtmlRegex, '').trim().toUpperCase(); 
                                                const isSelected = userAns === optionValue; 
                                                const isCorrectOpt = isAnswerCorrect(optionValue, correctAns);
                                                
                                                let labelClass = "flex items-center gap-2 p-1.5 transition ";
                                                let boxClass = "w-full h-full border flex items-center justify-center rounded-[3px] transition-colors ";
                                                
                                                if (isReviewMode) { 
                                                  if (isCorrectOpt) {
                                                     labelClass += "font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 rounded ";
                                                     boxClass += "border-emerald-500 bg-emerald-100";
                                                  }
                                                  else if (isSelected) {
                                                     labelClass += "text-red-500 line-through opacity-70 bg-red-50 rounded ";
                                                     boxClass += "border-red-500 bg-red-100";
                                                  }
                                                  else {
                                                     labelClass += "opacity-50 ";
                                                     boxClass += "border-gray-300 bg-white";
                                                  }
                                                } else { 
                                                  labelClass += "cursor-pointer group hover:text-blue-600 ";
                                                  boxClass += isSelected ? "border-blue-600 bg-blue-50" : "border-gray-400 bg-white group-hover:border-blue-400";
                                                }
                                                
                                                return (
                                                  <label key={i} className={labelClass}>
                                                    <div className="relative inline-flex items-center justify-center w-[18px] h-[18px] shrink-0 mt-0.5">
                                                      <input type="radio" name={`q${q.id}`} value={optionValue} checked={isSelected} onChange={(e) => handleAnswer(String(q.id), e.target.value)} className="opacity-0 absolute inset-0 z-10 cursor-pointer w-full h-full m-0" disabled={isReviewMode} />
                                                      <div className={boxClass}>
                                                        {isSelected && (
                                                          // Đã cập nhật nét bút chữ V mềm mại và thon dài hơn
                                                          <svg viewBox="0 0 24 24" overflow="visible" className={`w-[22px] h-[22px] absolute pointer-events-none ${isReviewMode ? (isCorrectOpt ? 'text-emerald-600' : 'text-red-600') : 'text-blue-600'}`} style={{ filter: 'drop-shadow(0px 1px 1px rgba(0,0,0,0.2))', transform: 'translate(1px, -3px)' }}>
                                                            <path d="M5 14 C7 14, 9 17, 10 19 C13 11, 17 5, 23 3" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                                                          </svg>
                                                        )}
                                                      </div>
                                                    </div>
                                                    <span className="text-[15px] font-serif leading-relaxed font-semibold" dangerouslySetInnerHTML={{ __html: safeOpt }} />
                                                  </label>
                                                );
                                              })}
                                            </div>
                                            {isReviewMode && (<div className="mt-6 pt-4 border-t border-slate-200"><p className="text-[12px] font-black text-amber-600 uppercase mb-2">💡 Giải thích đáp án:</p><div className="text-[14px] text-slate-700 italic font-serif" dangerouslySetInnerHTML={{ __html: q.explanation || "Không có lời giải thích." }} /></div>)}
                                          </div>
                                        </div>
                                      </div>
                                   );
                                }

                                // Trắc nghiệm (Layout dọc)
                                return (
                                  <div key={q.id} id={`q-${q.id}`} onClick={() => setActiveQuestionId(String(q.id))} className={`p-6 rounded-xl border shadow-sm transition-all ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-200' : 'bg-red-50/50 border-red-200') : (activeQuestionId === String(q.id) ? 'border-blue-400 bg-blue-50/30' : 'border-gray-200 bg-white hover:border-gray-300')}`}>
                                    <div className="flex gap-4 mb-4">
                                      <span className="font-bold text-gray-800 shrink-0 w-6 text-right pt-[2px]">{displayIndex}.</span>
                                      <div className="flex-1">
                                        {isReviewMode && (<div className="mb-3">{isCorrect ? <span className="text-[11px] font-bold bg-emerald-100 text-emerald-700 px-3 py-1 rounded">✅ ĐÚNG</span> : <span className="text-[11px] font-bold bg-red-100 text-red-700 px-3 py-1 rounded">❌ SAI</span>}</div>)}
                                        {q.content && <p className="text-[16px] mb-4 font-serif leading-relaxed" dangerouslySetInnerHTML={{ __html: q.content }}></p>}
                                        <div className={`flex flex-col gap-2`}>
                                          {validOptions.map((opt: any, i: number) => {
                                            const safeOpt = String(opt || '');
                                            const optionValue = String.fromCharCode(65+i); 
                                            const isSelected = userAns === optionValue; 
                                            const isCorrectOpt = isAnswerCorrect(optionValue, correctAns);
                                            
                                            let labelClass = "flex items-start gap-3 p-1.5 transition ";
                                            let boxClass = "w-full h-full border flex items-center justify-center rounded-[3px] transition-colors ";
                                            
                                            if (isReviewMode) { 
                                              if (isCorrectOpt) {
                                                 labelClass += "font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 rounded ";
                                                 boxClass += "border-emerald-500 bg-emerald-100";
                                              }
                                              else if (isSelected) {
                                                 labelClass += "text-red-500 line-through opacity-70 bg-red-50 rounded ";
                                                 boxClass += "border-red-500 bg-red-100";
                                              }
                                              else {
                                                 labelClass += "opacity-50 ";
                                                 boxClass += "border-gray-300 bg-white";
                                              }
                                            } else { 
                                              labelClass += "cursor-pointer group hover:text-blue-600 ";
                                              boxClass += isSelected ? "border-blue-600 bg-blue-50" : "border-gray-400 bg-white group-hover:border-blue-400";
                                            }

                                            return (
                                              <label key={i} className={labelClass}>
                                                <div className="relative inline-flex items-center justify-center w-[18px] h-[18px] shrink-0 mt-0.5">
                                                  <input type="radio" name={`q${q.id}`} value={optionValue} checked={isSelected} onChange={(e) => handleAnswer(String(q.id), e.target.value)} className="opacity-0 absolute inset-0 z-10 cursor-pointer w-full h-full m-0" disabled={isReviewMode} />
                                                  <div className={boxClass}>
                                                    {isSelected && (
                                                      <svg viewBox="0 0 24 24" overflow="visible" className={`w-[22px] h-[22px] absolute pointer-events-none ${isReviewMode ? (isCorrectOpt ? 'text-emerald-600' : 'text-red-600') : 'text-blue-600'}`} style={{ filter: 'drop-shadow(0px 1px 1px rgba(0,0,0,0.2))', transform: 'translate(1px, -3px)' }}>
                                                        <path d="M5 14 C7 14, 9 17, 10 19 C13 11, 17 5, 23 3" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                                                      </svg>
                                                    )}
                                                  </div>
                                                </div>
                                                <span className="text-[15px] font-serif leading-relaxed"><span className="font-bold mr-1">{optionValue}.</span> <span dangerouslySetInnerHTML={{ __html: safeOpt }} /></span>
                                              </label>
                                            );
                                          })}
                                        </div>
                                        {isReviewMode && (<div className="mt-6 pt-4 border-t border-slate-200"><p className="text-[12px] font-black text-amber-600 uppercase mb-2">💡 Giải thích đáp án:</p><div className="text-[14px] text-slate-700 italic font-serif" dangerouslySetInnerHTML={{ __html: q.explanation || "Không có lời giải thích." }} /></div>)}
                                      </div>
                                    </div>
                                  </div>
                                );
                              })}
                            </div>
                          )}

                          {/* DẠNG DROPLIST BLOCK CÓ EXCLUSION LOGIC */}
                          {isBlockDroplist && (
                             <div className="space-y-4 bg-white p-8 border border-gray-200 rounded-xl shadow-sm">
                               {(() => {
                                  const sectionQIds = (sec.questions || []).map((q:any) => String(q.id));
                                  const selectedInSec = sectionQIds.map((id:string) => answers[id]?.trim().toUpperCase()).filter(Boolean);
                                  
                                  return (Array.isArray(sec.questions) ? sec.questions : []).map((q: any) => {
                                      if (!q?.id) return null;
                                      const correctAns = String(q.correctAnswer || '').trim().toUpperCase(); 
                                      const userAns = String(answers[String(q.id)] || '').trim(); 
                                      const isCorrect = isAnswerCorrect(userAns, correctAns);
                                      const displayIdx = questionIndexMap[String(q.id)] || q.id;
                                      
                                      let rawOptions = (q.options && q.options.length > 0) ? q.options : (sec.questions[0]?.options || []);
                                      const validOptions = rawOptions.filter(Boolean);
                                      
                                      return (
                                       <div key={q.id} id={`q-${q.id}`} onClick={() => setActiveQuestionId(String(q.id))} className={`p-4 rounded-lg border flex flex-col sm:flex-row sm:items-center gap-4 cursor-pointer transition-all ${isReviewMode ? (isCorrect ? 'bg-emerald-50 border-emerald-200' : 'bg-red-50 border-red-200') : (activeQuestionId === String(q.id) ? 'bg-blue-50/30 border-blue-300' : 'bg-white border-gray-200 hover:border-gray-300')}`}>
                                         <div className="flex items-center gap-4 flex-1">
                                           <span className="font-bold text-gray-800 w-6 text-right">{displayIdx}.</span>
                                           <div className="text-[15px] text-gray-800 leading-relaxed font-serif" dangerouslySetInnerHTML={{ __html: q.content }} />
                                         </div>
                                         <div className="shrink-0 flex items-center justify-end mt-1 sm:mt-0">
                                            {isReviewMode ? (
                                                <div className="flex items-center gap-2">
                                                    <div className={`px-4 py-1.5 rounded font-bold text-[14px] border ${isCorrect ? 'bg-emerald-100 text-emerald-800 border-emerald-300' : 'bg-red-100 text-red-800 border-red-300'}`}>
                                                       {userAns || '(trống)'}
                                                    </div>
                                                    {!isCorrect && <div className="text-[12px] font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded whitespace-nowrap">Đúng: {correctAns}</div>}
                                                </div>
                                             ) : (
                                                <select 
                                                  value={userAns}
                                                  onChange={(e) => handleAnswer(String(q.id), e.target.value)}
                                                  className="bg-transparent border-0 border-b-2 border-gray-400 text-blue-800 font-bold text-center text-[15px] h-[36px] px-2 outline-none focus:border-blue-600 cursor-pointer w-auto min-w-[100px] max-w-[200px]"
                                                >
                                                  <option value="">---</option>
                                                  {validOptions.map((opt: string, oIdx: number) => {
                                                     const val = opt.replace(stripHtmlRegex, '').trim();
                                                     const isSelectedElsewhere = selectedInSec.includes(val.toUpperCase()) && userAns.trim().toUpperCase() !== val.toUpperCase();
                                                     return (
                                                       <option key={oIdx} value={val}>
                                                         {val} {isSelectedElsewhere ? '(Đã chọn)' : ''}
                                                       </option>
                                                     );
                                                  })}
                                                </select>
                                             )}
                                         </div>
                                       </div>
                                      )
                                   })
                               })()}
                             </div>
                          )}

                          {/* DẠNG KÉO THẢ & MATCHING */}
                          {(isInlineDragDrop || isBlockDragDrop) && (
                            <div className="bg-white p-8 rounded-xl border border-gray-200 shadow-sm">
                              {isInlineDragDrop ? (
                                <div className="format-passage leading-[2.8] text-[16px] text-slate-800 font-serif">
                                  {renderHtmlWithHoles(rawContentText, sec)}
                                </div>
                              ) : (
                                <div className="space-y-4">
                                  {(Array.isArray(sec.questions) ? sec.questions : []).map((q: any) => {
                                    if (!q?.id) return null;
                                    const userAns = String(answers[String(q.id)] || '');
                                    const correctAns = String(q.correctAnswer || '').trim().toUpperCase();
                                    const isCorrect = isAnswerCorrect(userAns, correctAns);
                                    const displayIdx = questionIndexMap[String(q.id)] || q.id;
                                    
                                    const displayUserAns = userAns ? userAns.replace(/^[A-Z][\.\):]\s*/i, '') : '';
                                    return (
                                      <div key={q.id} id={`q-${q.id}`} onClick={() => setActiveQuestionId(String(q.id))} className={`p-5 rounded-lg border flex flex-col sm:flex-row sm:items-center gap-4 cursor-pointer transition-all ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-200' : 'bg-red-50/50 border-red-200') : (activeQuestionId === String(q.id) ? 'bg-blue-50/30 border-blue-300' : 'bg-white border-gray-200 hover:border-gray-300')}`}>
                                        <div className="flex items-center gap-4 flex-1">
                                          <span className="font-bold text-gray-800 w-6 text-right">{displayIdx}.</span>
                                          <div className="text-[15px] text-gray-800 leading-relaxed font-serif" dangerouslySetInnerHTML={{ __html: q.content }} />
                                        </div>
                                        <div className="shrink-0 flex items-center justify-end mt-1 sm:mt-0 sm:ml-4">
                                          {isReviewMode ? (
                                            <div className="flex items-center gap-2">
                                                <div className={`px-4 py-1.5 rounded font-bold text-[14px] border ${isCorrect ? 'bg-emerald-100 text-emerald-800 border-emerald-300' : 'bg-red-100 text-red-800 border-red-300'}`}>
                                                   {displayUserAns || '(trống)'}
                                                </div>
                                                {!isCorrect && <div className="text-[12px] font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded whitespace-nowrap">Đúng: {correctAns}</div>}
                                            </div>
                                          ) : (
                                            <span 
                                              onDragOver={(e) => e.preventDefault()}
                                              onDrop={() => onDrop(String(q.id))}
                                              className={`inline-flex items-center align-middle min-w-[150px] h-[36px] border border-gray-400 rounded transition-all px-2 ${activeQuestionId === String(q.id) ? 'bg-blue-50/50' : 'bg-gray-50'}`}
                                            >
                                              {userAns ? (
                                                <div className="flex items-center justify-between w-full text-blue-800 text-[14px] font-bold py-1">
                                                  <span className="truncate">{displayUserAns}</span>
                                                  <button onClick={(e) => { e.stopPropagation(); clearDragAnswer(String(q.id)); }} className="ml-2 hover:text-red-600 text-[12px] font-black">✕</button>
                                                </div>
                                              ) : (
                                                <span className="text-gray-400 text-[13px] italic w-full text-center">Thả vào đây</span>
                                              )}
                                            </span>
                                          )}
                                        </div>
                                      </div>
                                    )
                                  })}
                                </div>
                              )}

                              {/* KHO TỪ KÉO THẢ */}
                              {!isReviewMode && (
                                <div className="mt-10 p-6 bg-gray-50 border border-gray-200 rounded-lg shadow-inner">
                                  <p className="text-[13px] font-black text-gray-600 uppercase tracking-widest mb-4">Danh sách lựa chọn (Kéo từ đây):</p>
                                  <div className="flex flex-wrap gap-3">
                                    {(() => {
                                      let allOptions: string[] = [];
                                      (sec.questions || []).forEach((q: any) => {
                                          if (Array.isArray(q.options)) {
                                              q.options.forEach((o: any) => {
                                                  const cleanOpt = String(o).replace(stripHtmlRegex, '').trim();
                                                  if (cleanOpt && !allOptions.includes(cleanOpt)) {
                                                      allOptions.push(cleanOpt);
                                                  }
                                              });
                                          }
                                      });
                                      
                                      const sectionQIds = (sec?.questions || []).map((q:any) => String(q.id));
                                      const selectedInSec = sectionQIds.map((id:string) => answers[id]?.trim().toUpperCase()).filter(Boolean);
                                      
                                      return allOptions.map((opt: string, oIdx: number) => {
                                        const prefix = `${String.fromCharCode(65 + oIdx)}. `;
                                        const displayOpt = /^[A-Z][\.\):]\s/.test(opt) ? opt : prefix + opt;
                                        const isUsed = selectedInSec.includes(displayOpt.toUpperCase()) || selectedInSec.includes(opt.trim().toUpperCase());
                                        
                                        return (
                                          <div
                                            key={oIdx}
                                            draggable={!isUsed}
                                            onDragStart={() => onDragStart(displayOpt)}
                                            onDragEnd={() => {
                                              setDraggedOption(null);
                                              stopAutoScroll(); 
                                            }}
                                            className={`px-4 py-2 font-bold text-[14px] border rounded transition-all select-none shadow-sm
                                              ${isUsed 
                                                ? 'bg-gray-200 border-gray-300 text-gray-400 opacity-60 cursor-not-allowed' 
                                                : 'bg-white border-gray-300 text-gray-800 cursor-grab hover:bg-gray-100 hover:border-gray-400 active:cursor-grabbing'
                                              }`}
                                          >
                                            {displayOpt}
                                          </div>
                                        );
                                      });
                                    })()}
                                  </div>
                                </div>
                              )}
                            </div>
                          )}

                          {/* DẠNG CHECKBOX GROUP */}
                          {sec.questionType === "Checkbox" && (
                            <div className="space-y-6">
                               {(() => {
                                  const combos = buildCheckboxCombos(sec.questions);

                                  return combos.map((combo, comboIndex) => {
                                      const comboIds = combo.map((q: any) => String(q.id));
                                      const maxAllowed = combo.length;
                                      
                                      const userAnsArr = Array.from(new Set(comboIds.map(id => answers[id]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase()))));
                                      const correctAnsComboSet = new Set(combo.flatMap((q:any) => String(q.correctAnswer).split(',').map((x:string)=>x.trim().toUpperCase()).filter(Boolean)));
                                      const validOptions = (Array.isArray(combo[0]?.options) ? combo[0].options : []).filter((opt: any) => String(opt || '').trim() !== '');
                                      
                                      let comboPoints = 0;
                                      userAnsArr.forEach((ans:string) => {
                                          let isMatched = false;
                                          correctAnsComboSet.forEach(c => {
                                              if (isAnswerCorrect(ans, c)) isMatched = true;
                                          });
                                          if (isMatched) comboPoints++;
                                      });
                                      
                                      const isPerfect = comboPoints === maxAllowed;
                                      const isPartial = comboPoints > 0 && comboPoints < maxAllowed;
                                      
                                      let containerClass = "p-6 bg-white border rounded-xl shadow-sm relative group transition-all ";
                                      if (isReviewMode) {
                                          if (isPerfect) containerClass += "border-emerald-200 bg-emerald-50/50";
                                          else if (isPartial) containerClass += "border-amber-200 bg-amber-50/50";
                                          else containerClass += "border-red-200 bg-red-50/50";
                                      } else {
                                          if (comboIds.includes(activeQuestionId)) containerClass += "border-blue-400 bg-blue-50/30";
                                          else containerClass += "border-gray-200 hover:border-gray-300";
                                      }

                                      const handleComboChange = (optionValue: string, isChecked: boolean) => {
                                          setAnswers(prev => {
                                              let currentSelected = Array.from(new Set(comboIds.map(id => prev[id]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase()))));
                                              
                                              if (isChecked) {
                                                  if (currentSelected.length >= maxAllowed) {
                                                      alert(`Lưu ý: Nhóm câu hỏi này chỉ yêu cầu chọn tối đa ${maxAllowed} đáp án.`);
                                                      return prev;
                                                  }
                                                  if (!currentSelected.includes(optionValue)) currentSelected.push(optionValue);
                                              } else {
                                                  currentSelected = currentSelected.filter((v:string) => v !== optionValue);
                                              }
                                              
                                              const next = { ...prev };
                                              comboIds.forEach((id, idx) => {
                                                  next[id] = currentSelected[idx] || ''; 
                                              });
                                              return next;
                                          });
                                          setActiveQuestionId(comboIds[0]);
                                      };

                                      const qText = combo[0]?.content.replace(/^<p>|<\/p>$/gi, '').replace(/^\d+[\.\)]\s*/, '') || '';
                                      
                                      return (
                                         <div key={`combo-${comboIndex}`} className={containerClass}>
                                           <div className="flex items-start gap-4 mb-5">
                                             <div className="flex gap-2 flex-wrap shrink-0 mt-0.5">
                                                {combo.map((q: any) => {
                                                    const displayIdx = questionIndexMap[String(q.id)] || q.id;
                                                    const boxClass = isReviewMode 
                                                        ? (isPerfect ? 'bg-emerald-600 text-white border-emerald-600' : isPartial ? 'bg-amber-500 text-white border-amber-500' : 'bg-red-500 text-white border-red-500')
                                                        : (activeQuestionId === String(q.id) ? 'bg-blue-600 text-white border-blue-600 shadow-md' : 'bg-gray-100 text-gray-700 border-gray-300');
                                                    return (
                                                        <span key={q.id} id={`q-${q.id}`} onClick={() => setActiveQuestionId(String(q.id))} className={`cursor-pointer inline-flex items-center justify-center font-bold px-2 min-w-[28px] h-[28px] text-[13px] rounded shadow-sm border ${boxClass}`}>
                                                          {displayIdx}
                                                        </span>
                                                    );
                                                })}
                                             </div>
                                             <div className="text-[16px] leading-relaxed text-gray-800 cursor-pointer w-full font-serif" dangerouslySetInnerHTML={{ __html: qText }} />
                                           </div>

                                           <div className={`flex flex-col gap-3 ml-[3.5rem]`}>
                                             {validOptions.map((opt: any, i: number) => {
                                               const safeOpt = String(opt || '').replace(/^<p>|<\/p>$/gi, '');
                                               const optionValue = String.fromCharCode(65+i); 
                                               const isSelected = userAnsArr.includes(optionValue); 
                                               
                                               let isCorrectOpt = false;
                                               correctAnsComboSet.forEach(c => {
                                                  if (isAnswerCorrect(optionValue, c)) isCorrectOpt = true;
                                               });
                                               
                                               let labelClass = "flex items-start gap-3 p-1.5 transition ";
                                               let boxClass = "w-full h-full border flex items-center justify-center rounded-[3px] transition-colors ";
                                               
                                               if (isReviewMode) { 
                                                 if (isCorrectOpt && isSelected) {
                                                    labelClass += "font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 rounded ";
                                                    boxClass += "border-emerald-500 bg-emerald-100";
                                                 }
                                                 else if (isCorrectOpt && !isSelected) {
                                                    labelClass += "font-bold text-amber-600 bg-amber-50 border border-amber-200 rounded ";
                                                    boxClass += "border-amber-500 bg-amber-100";
                                                 }
                                                 else if (isSelected && !isCorrectOpt) {
                                                    labelClass += "text-red-500 line-through opacity-70 bg-red-50 rounded ";
                                                    boxClass += "border-red-500 bg-red-100";
                                                 }
                                                 else {
                                                    labelClass += "opacity-50 ";
                                                    boxClass += "border-gray-300 bg-white";
                                                 }
                                               } else { 
                                                 labelClass += "cursor-pointer group hover:text-blue-600 ";
                                                 boxClass += isSelected ? "border-blue-600 bg-blue-50" : "border-gray-400 bg-white group-hover:border-blue-400";
                                               }

                                               return (
                                                 <label key={i} className={labelClass}>
                                                   <div className="relative inline-flex items-center justify-center w-[18px] h-[18px] shrink-0 mt-0.5">
                                                     <input type="checkbox" checked={isSelected} onChange={(e) => handleComboChange(optionValue, e.target.checked)} className="opacity-0 absolute inset-0 z-10 cursor-pointer w-full h-full m-0" disabled={isReviewMode} />
                                                     <div className={boxClass}>
                                                       {isSelected && (
                                                         <svg viewBox="0 0 24 24" overflow="visible" className={`w-[22px] h-[22px] absolute pointer-events-none ${isReviewMode ? (isCorrectOpt ? 'text-emerald-600' : 'text-red-600') : 'text-blue-600'}`} style={{ filter: 'drop-shadow(0px 1px 1px rgba(0,0,0,0.2))', transform: 'translate(1px, -3px)' }}>
                                                           <path d="M5 14 C7 14, 9 17, 10 19 C13 11, 17 5, 23 3" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                                                         </svg>
                                                       )}
                                                     </div>
                                                   </div>
                                                   <span className="text-[15px] leading-[1.8] font-serif"><span className="font-bold mr-1">{optionValue}.</span> <span dangerouslySetInnerHTML={{ __html: safeOpt }} /></span>
                                                 </label>
                                               )
                                             })}
                                           </div>

                                           {isReviewMode && (
                                             <div className="mt-6 ml-[3.5rem] pt-4 border-t border-gray-200">
                                                <p className="text-[12px] font-black text-amber-600 uppercase mb-3">💡 Giải thích đáp án:</p>
                                                {combo.map((q:any) => {
                                                    if (!q.explanation || String(q.explanation).trim() === '') return null;
                                                    return (
                                                        <div key={q.id} className="text-[14px] text-gray-600 italic leading-relaxed mb-3 last:mb-0 font-serif">
                                                            <span className="font-bold text-white px-2 py-0.5 bg-gray-600 rounded text-[11px] mr-2">Câu {questionIndexMap[String(q.id)] || q.id}</span>
                                                            <span dangerouslySetInnerHTML={{ __html: q.explanation }} />
                                                        </div>
                                                    )
                                                })}
                                             </div>
                                           )}
                                         </div>
                                      )
                                  });
                               })()}
                            </div>
                          )}

                        </div>
                      )
                    })}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </main>

      {/* FOOTER (Câu hỏi) */}
      <footer className="bg-white border-t border-gray-300 px-4 py-3 flex items-center shadow-[0_-2px_10px_rgba(0,0,0,0.05)] z-20 shrink-0 font-sans">
        
        {/* Review Toggle */}
        <div className="flex items-center gap-2 h-full pr-6 border-r border-gray-300 shrink-0 min-w-max">
          <input 
            type="checkbox" 
            id="review" 
            className="w-4 h-4 cursor-pointer accent-blue-600 rounded-sm" 
            disabled={isReviewMode} 
            checked={!!reviewFlags[activeQuestionId]}
            onChange={() => setReviewFlags(prev => ({...prev, [activeQuestionId]: !prev[activeQuestionId]}))}
          />
          <label htmlFor="review" className="text-[14px] font-bold text-gray-700 cursor-pointer mt-0.5 whitespace-nowrap">Đánh dấu</label>
        </div>

        <div className="flex-1 flex gap-2 overflow-x-auto px-4 py-1 custom-scrollbar justify-start items-center min-h-[44px]">
          {allQuestionIds.map(id => {
            let isAnswered = answers[id] && answers[id].trim() !== '';
            const isReview = reviewFlags[id];
            const isActive = activeQuestionId === id;
            
            const shapeClass = isReview ? 'rounded-full' : 'rounded'; 
            let btnClass = `w-9 h-9 shrink-0 flex items-center justify-center font-bold text-[14px] transition-all ${shapeClass} `;
            
            const section = parts.reduce((acc: any[], p: any) => acc.concat(Array.isArray(p?.sections) ? p.sections : []), []).find((s:any) => {
                if ((Array.isArray(s?.questions) ? s.questions : []).some((sq:any)=>String(sq?.id)===id)) return true;
                if (s?.questionType === "Điền từ" || s?.questionType === "Kéo thả vào Part" || s?.questionType === "Kéo thả" || s?.questionType === "Matching" || s?.questionType === "Droplist") {
                    const combined = String(s?.content || '') + ' ' + String((Array.isArray(s?.questions) ? s.questions : [])[0]?.content || '');
                    const matches = combined.match(/\[\s*\d+\s*\]/g);
                    if (matches && matches.some((m:string) => m.replace(/\D/g, '') === id)) return true;
                }
                return false;
            });
            
            const qType = section?.questionType;

            if (!isReviewMode && qType === 'Checkbox') {
                const combos = buildCheckboxCombos(section?.questions);
                const myCombo = combos.find((c: any[]) => c.some((q:any) => String(q.id) === id));
                if (myCombo) {
                    const comboIds = myCombo.map((q:any) => String(q.id));
                    const userAnsArr = Array.from(new Set(comboIds.map(cid => answers[cid]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim()))));
                    const idxInCombo = comboIds.indexOf(id);
                    isAnswered = idxInCombo < userAnsArr.length;
                }
            }

            if (isReviewMode) {
              if (qType === 'Checkbox') {
                 const combos: any[][] = [];
                 parts.forEach((p:any) => {
                     (Array.isArray(p?.sections) ? p.sections : []).forEach((sec: any) => {
                         if (sec?.questionType === 'Checkbox') combos.push(...buildCheckboxCombos(sec.questions));
                     });
                 });
                 const myCombo = combos.find((c: any[]) => c.some((q:any) => String(q.id) === id)) || [];
                 if (myCombo.length > 0) {
                     const comboIds = myCombo.map((q:any) => String(q.id));
                     const userAnsSet = new Set(comboIds.map(cid => answers[cid]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase())));
                     const correctAnsSet = new Set(myCombo.flatMap((q:any)=>String(q.correctAnswer || '').split(',').map((x:string)=>x.trim().toUpperCase()).filter(Boolean)));
                     let pts = 0;
                     userAnsSet.forEach((v:string) => { 
                         let isMatched = false;
                         correctAnsSet.forEach(c => { if (isAnswerCorrect(v, c)) isMatched = true; });
                         if (isMatched) pts++; 
                     });
                     const idxInCombo = comboIds.indexOf(id);
                     if (idxInCombo < pts) {
                         btnClass += 'bg-emerald-100 border border-emerald-400 text-emerald-800';
                     } else {
                         btnClass += 'bg-red-100 border border-red-400 text-red-800';
                     }
                 } else {
                     btnClass += 'bg-red-100 border border-red-400 text-red-800';
                 }
              } else {
                 let qCorrectAns = '';
                 parts.forEach((p: any) => {
                    (Array.isArray(p?.sections) ? p.sections : []).forEach((s: any) => {
                       const q = (Array.isArray(s?.questions) ? s.questions : []).find((sq: any) => String(sq?.id) === String(id));
                       if (q) qCorrectAns = String(q.correctAnswer || '');
                    });
                 });
                 const isCorrect = isAnswerCorrect(answers[id], qCorrectAns) && qCorrectAns !== '';
                 btnClass += isCorrect ? 'bg-emerald-100 border border-emerald-400 text-emerald-800' : 'bg-red-100 border border-red-400 text-red-800';
              }
            } else { 
              if (isActive) {
                 btnClass += 'bg-blue-600 text-white shadow-md transform scale-110';
              } else if (isAnswered) {
                 btnClass += 'bg-blue-100 text-blue-800 border-b-4 border-blue-600 cursor-pointer';
              } else {
                 btnClass += 'bg-gray-100 border border-gray-300 text-gray-600 cursor-pointer hover:bg-gray-200';
              }
            }
            
            return (<button key={id} onClick={() => scrollToQuestion(id)} className={btnClass}>{questionIndexMap[id]}</button>)
          })}
        </div>
        <div className="ml-4 shrink-0 flex items-center gap-3 border-l border-gray-300 pl-4">
          <button onClick={handleFinish} className={`font-bold text-sm px-8 py-2.5 rounded shadow-md transition ${isReviewMode ? 'bg-emerald-600 hover:bg-emerald-500 text-white' : 'bg-blue-600 hover:bg-blue-500 text-white'}`}>
            {isReviewMode ? 'Thoát' : 'Nộp Bài Thi'}
          </button>
        </div>
      </footer>
    </div>
  );
}