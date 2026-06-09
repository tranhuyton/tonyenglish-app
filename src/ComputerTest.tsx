import React, { useState, useRef, useEffect, useMemo } from 'react';
import { supabase } from './supabase';
import './tailwind.css';

const UserIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
    <path fillRule="evenodd" d="M7.5 6a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM3.751 20.105a8.25 8.25 0 0116.498 0 .75.75 0 01-.437.695A18.683 18.683 0 0112 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 01-.437-.695z" clipRule="evenodd" />
  </svg>
);

const SettingsIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
    <path fillRule="evenodd" d="M11.078 2.25c-.917 0-1.699.663-1.85 1.567L9.05 4.889c-.02.12-.115.26-.297.348a7.493 7.493 0 00-.986.57c-.166.115-.334.126-.45.083L6.3 5.508a1.875 1.875 0 00-2.282.819l-.922 1.597a1.875 1.875 0 00.432 2.385l.84.692c.097.078.15.222.15.399v.111c0 .177-.053.321-.15.399l-.84.692a1.875 1.875 0 00-.432 2.385l.922 1.597a1.875 1.875 0 002.282.818l1.019-.382c.115-.043.283-.031.45.082.312.214.641.405.985.57.182.088.277.228.297.35l.178 1.071c.151.904.933 1.567 1.85 1.567h1.844c.916 0 1.699-.663 1.85-1.567l.178-1.072c.02-.12.114-.26.297-.349.344-.165.673-.356.985-.57.167-.114.335-.125.45-.082l1.02.382a1.875 1.875 0 002.28-.819l.923-1.597a1.875 1.875 0 00-.432-2.385l-.84-.692c-.098-.078-.15-.222-.15-.399v-.111c0-.177.052-.321.15-.399l.84-.692a1.875 1.875 0 00.432-2.385l-.923-1.597a1.875 1.875 0 00-2.28-.818l-1.02.382c-.114.043-.282.031-.449-.083a7.49 7.49 0 00-.985-.57c-.183-.087-.277-.227-.297-.348l-.179-1.072a1.875 1.875 0 00-1.85-1.567h-1.843zM12 15.75a3.75 3.75 0 110-7.5 3.75 3.75 0 010 7.5z" clipRule="evenodd" />
  </svg>
);

const FullscreenIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5">
    <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" />
  </svg>
);

const ExitFullscreenIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5">
    <path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" />
  </svg>
);

const stripHtmlRegex = /[<][^>]*[>]/g;

// TỰ ĐỘNG XÓA BỎ CÁC THUỘC TÍNH HEIGHT/OVERFLOW GÂY LỖI THANH CUỘN
const cleanHtmlContent = (html: any) => {
  if (!html) return '';
  return String(html).replace(/style\s*=\s*(['"])(.*?)\1/gi, (match, quote, styleContent) => {
      let newStyle = styleContent
          .replace(/(?:^|;)\s*(max-height|min-height|height|overflow|overflow-y|overflow-x)\s*:[^;]+/gi, '')
          .replace(/^;+|;+$/g, '')
          .trim();
      return newStyle ? `style=${quote}${newStyle}${quote}` : '';
  });
};

const isRealContent = (htmlContent: any) => {
  const str = String(htmlContent || '');
  const rawText = str.replace(stripHtmlRegex, '').replace(/&nbsp;/gi, '').replace(/\s+/g, '');
  return rawText !== '' || str.includes('<img') || str.includes('<audio');
};

const buildCheckboxCombos = (questions: any[]) => {
  const combos: any[][] = [];
  (Array.isArray(questions) ? questions : []).forEach((q: any) => {
    if (combos.length === 0) {
      combos.push([q]); 
      return;
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

    if (contentEmpty || hasSameOptions || hasNoOptions || hasSameContent) {
        combos[combos.length - 1].push(q);
    } else {
        combos.push([q]); 
    }
  });
  return combos;
};

// NÂNG CẤP HÀM CHẤM ĐIỂM HOÀN HẢO CHO MỌI BIẾN THỂ KÉO THẢ
const isAnswerCorrect = (userAns: string, correctAns: string) => {
  if (!userAns || !correctAns) return false;
  
  // Chuẩn hóa khoảng trắng
  const u = String(userAns).trim().toUpperCase().replace(/\s+/g, ' ');
  const cArr = String(correctAns).split('/').map(x => x.trim().toUpperCase().replace(/\s+/g, ' '));
  
  for (const c of cArr) {
    if (u === c) return true;
    
    const uMatch = u.match(/^([A-Z])[\.\):]\s*(.*)$/);
    if (uMatch) {
      if (uMatch[1] === c) return true;
      if (uMatch[2] === c) return true;
    }
    
    const cMatch = c.match(/^([A-Z])[\.\):]\s*(.*)$/);
    if (cMatch) {
      if (u === cMatch[1]) return true;
      if (u === cMatch[2]) return true;
    }

    if (c.includes('(') && c.includes(')')) {
      const withoutParens = c.replace(/\(.*?\)/g, '').replace(/\s+/g, ' ').trim();
      const withParensContent = c.replace(/[\(\)]/g, '').replace(/\s+/g, ' ').trim();
      
      if (u === withoutParens || u === withParensContent) return true;
      if (uMatch && (uMatch[2] === withoutParens || uMatch[2] === withParensContent)) return true;
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
      const lowerKey = key.toLowerCase();
      // Ngăn chặn parse các thuộc tính gây lỗi scrollbar từ inline HTML
      if (['height', 'max-height', 'min-height', 'overflow', 'overflow-y', 'overflow-x'].includes(lowerKey)) {
          return;
      }
      const camelKey = key.replace(/-([a-z])/g, g => g[1].toUpperCase());
      style[camelKey] = val;
    }
  });
  return style;
};

export default function ComputerTest({ onBack, testData, onFinish }: { onBack: () => void, testData?: any, onFinish?: (res: any) => void }) {
  let safeTestData = testData;
  if (typeof safeTestData === 'string') {
    try { 
        safeTestData = JSON.parse(safeTestData);
    } catch (e) { 
        console.error("Error parsing testData", e);
    }
  }

  const contentJSON = safeTestData?.content_json || safeTestData || {};
  const basicInfo = contentJSON.basicInfo || { title: "IELTS Test", timeLimit: "40", skill: "" };
  const parts = Array.isArray(contentJSON.parts) ? contentJSON.parts : []; 
  
  const isListening = basicInfo.skill?.toLowerCase().includes('listening') || String(safeTestData?.test_type || '').toLowerCase().includes('listening');
  
  const audioPlaylist = useMemo(() => {
      if (basicInfo.audioUrl) return [basicInfo.audioUrl];
      return parts.map((p: any) => p.audioUrl).filter(Boolean);
  }, [basicInfo.audioUrl, parts]);
  
  const [currentAudioIndex, setCurrentAudioIndex] = useState(0);
  const globalAudio = audioPlaylist[currentAudioIndex] || '';
  const [isFullscreen, setIsFullscreen] = useState(false);

  useEffect(() => {
    const handleFullscreenChange = () => setIsFullscreen(!!document.fullscreenElement);
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', handleFullscreenChange);
  }, []);

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => console.error(err));
    } else {
        if (document.exitFullscreen) document.exitFullscreen();
    }
  };

  const handleExit = () => {
    if (document.fullscreenElement) document.exitFullscreen().catch(() => {});
    onBack();
  };

  // 🚀 TỰ ĐỘNG KÍCH HOẠT REVIEW MODE NẾU NHẬN ĐƯỢC TÍN HIỆU TỪ STUDENT PORTAL
  const initIsReview = !!safeTestData?.isReview;
  const [testStarted, setTestStarted] = useState(initIsReview);
  const [isReviewMode, setIsReviewMode] = useState(initIsReview);
  const [scoreResult, setScoreResult] = useState({ 
      score: parseInt(safeTestData?.past_score || 0), 
      total: parseInt(safeTestData?.past_total || 0), 
      band: safeTestData?.past_band || "0.0" 
  });
  
  const globalAudioRef = useRef<HTMLAudioElement>(null);
  const isFinishingRef = useRef(false);

  // 🚀 NẾU LÀ REVIEW, ĐỔ BÊ TÔNG ĐÁP ÁN CŨ VÀO LUÔN
  const [answers, setAnswers] = useState<Record<string, string>>(() => {
    if (initIsReview && safeTestData?.past_answers) {
        return safeTestData.past_answers;
    }
    try {
      const saved = localStorage.getItem(`ielts_ans_${safeTestData?.id}`);
      return saved ? JSON.parse(saved) : {};
    } catch (error) { 
      return {}; 
    }
  });
  
  const [reviewFlags, setReviewFlags] = useState<Record<string, boolean>>({});
  const [activeQuestionId, setActiveQuestionId] = useState<string>('');
  const [draggedOption, setDraggedOption] = useState<string | null>(null);

  useEffect(() => {
      if (testStarted && !isReviewMode && isListening && globalAudioRef.current && audioPlaylist[currentAudioIndex]) {
          setTimeout(() => {
              globalAudioRef.current?.play().catch(e => console.log("Auto-play next track blocked", e));
          }, 100);
      }
  }, [currentAudioIndex, testStarted, isReviewMode, isListening, audioPlaylist]);

  useEffect(() => {
    if (!isReviewMode && !isFinishingRef.current && safeTestData?.id) {
      localStorage.setItem(`ielts_ans_${safeTestData.id}`, JSON.stringify(answers));
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
    const saved = localStorage.getItem(`ielts_endtime_${safeTestData.id}`);
    return saved ? parseInt(saved, 10) : null;
  };

  const parseInitialTime = (timeStr: string) => {
    if (!timeStr) return 3600; 
    const timeParts = String(timeStr).replace(/[^0-9:]/g, '').split(':');
    if (timeParts.length === 2) {
        return parseInt(timeParts[0]) * 60 + parseInt(timeParts[1]);
    } else {
        return (parseInt(timeParts[0]) || 60) * 60;
    }
  };

  const [timeLeft, setTimeLeft] = useState(() => parseInitialTime(basicInfo.timeLimit));

  const clearDraft = () => {
    if(window.confirm('Xóa bản nháp và làm lại từ đầu?')) { 
      if (safeTestData?.id) {
        localStorage.removeItem(`ielts_ans_${safeTestData.id}`);
        localStorage.removeItem(`ielts_endtime_${safeTestData.id}`);
      }
      setAnswers({}); 
      setReviewFlags({});
      
      const initialSeconds = parseInitialTime(basicInfo.timeLimit);
      const newEndTime = Date.now() + initialSeconds * 1000;
      
      if (safeTestData?.id) {
          localStorage.setItem(`ielts_endtime_${safeTestData.id}`, newEndTime.toString());
      }
      setTimeLeft(initialSeconds);
    }
  };

  const handleFinish = async () => {
    if (!isReviewMode) {
      if (!window.confirm("Bạn có chắc chắn muốn nộp bài thi?")) return;
      isFinishingRef.current = true;
      
      if (safeTestData?.id) {
        localStorage.removeItem(`ielts_ans_${safeTestData.id}`);
        localStorage.removeItem(`ielts_endtime_${safeTestData.id}`);
      }

      let score = 0; 
      let total = 0;
      let questionTypeStats: Record<string, { correct: number, total: number }> = {};

      parts.forEach((p: any) => {
        if (!Array.isArray(p.sections)) return;
        
        p.sections.forEach((s: any) => {
          const qType = s.questionType || 'Khác';
          if (!questionTypeStats[qType]) {
              questionTypeStats[qType] = { correct: 0, total: 0 };
          }
          if (!Array.isArray(s.questions)) return;

          if (qType === 'Checkbox') {
            const combos = buildCheckboxCombos(s.questions);
            combos.forEach(combo => {
              const comboIds = combo.map((q: any) => String(q.id));
              
              const userAnsComboSet = new Set(
                  comboIds.map(id => answers[id])
                          .filter(v => v && v.trim() !== '')
                          .flatMap(x => x.split(',').map(v => v.trim().toUpperCase()))
              );
              
              const correctAnsComboSet = new Set(
                  combo.flatMap((q:any) => String(q.correctAnswer || '')
                       .split(',')
                       .map((x:string) => x.trim().toUpperCase())
                       .filter(Boolean))
              );
              
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
                 score++; 
                 questionTypeStats[qType].correct++;
              }
            });
          }
        });
      });

      let band = "0.0";
      if (score >= 39) band = "9.0"; 
      else if (score >= 37) band = "8.5";
      else if (score >= 35) band = "8.0"; 
      else if (score >= 33) band = "7.5";
      else if (score >= 30) band = "7.0"; 
      else if (score >= 27) band = "6.5";
      else if (score >= 23) band = "6.0"; 
      else if (score >= 19) band = "5.5";
      else if (score >= 15) band = "5.0"; 
      else if (score >= 13) band = "4.5";
      else if (score >= 10) band = "4.0"; 
      else if (score >= 8) band = "3.5";
      else if (score >= 6) band = "3.0"; 
      else if (score >= 4) band = "2.5";
      else if (score >= 2) band = "2.0"; 
      else if (score >= 1) band = "1.0";

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
            test_type: safeTestData?.test_type || 'IELTS Computer',
            score: score, 
            total_score: total, 
            time_spent: timeSpentSecs > 0 ? timeSpentSecs : 0,
            // 🚀 ĐÃ SỬA: ĐẨY TOÀN BỘ questionTypeStats VÀO DETAILS ĐỂ SUPABASE GHI NHẬN LẠI DẠNG BÀI
            details: { test_id: safeTestData?.id, bandScore: band, userAnswers: answers, type_stats: questionTypeStats }
          }]);
        // 🚀 ANH DÁN ĐOẠN CODE BẮN PHÁO HIỆU VÀO ĐÂY NHÉ:
        await supabase.from('activity_logs').insert([{
          user_id: user.id, 
          action_type: 'finish_test',
          details: { 
              test_title: basicInfo.title || "Bài kiểm tra", 
              score: score,
              total: total
          }
        }]);
        }
      } catch (error) { 
          console.error("Lỗi lưu kết quả thi:", error); 
      }
      
    } else {
      if (document.fullscreenElement) {
          document.exitFullscreen().catch(() => {});
      }
      if (onFinish) {
          onFinish({ score: scoreResult.score, total: scoreResult.total, testTitle: basicInfo.title, bandScore: scoreResult.band });
      } else {
          onBack();
      }
    }
  };

  const resetTest = () => {
    if (window.confirm("Làm lại từ đầu? Mọi đáp án sẽ bị xóa.")) { 
      if (safeTestData?.id) localStorage.removeItem(`ielts_endtime_${safeTestData.id}`);
      setAnswers({}); 
      setReviewFlags({}); 
      setIsReviewMode(false); 
      setTestStarted(false); 
      setTimeLeft(parseInitialTime(basicInfo.timeLimit)); 
    }
  };

  const [currentPartIndex, setCurrentPartIndex] = useState(0);
  const currentPart = parts[currentPartIndex] || {};

  const { allQuestionIds, questionIndexMap, questionToPartMap, questionDataMap } = useMemo(() => {
    const ids: string[] = [];
    const partMap: Record<string, number> = {};
    const dataMap: Record<string, { qType: string, options: string[] }> = {};
    
    parts.forEach((p: any, pIndex: number) => {
      if (Array.isArray(p?.sections)) {
        p.sections.forEach((s: any) => {
          if (Array.isArray(s?.questions)) {
             s.questions.forEach((q: any) => {
                const qIdStr = String(q.id);
                if (q?.id && !ids.includes(qIdStr)) {
                  ids.push(qIdStr);
                  partMap[qIdStr] = pIndex;
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
                    partMap[num] = pIndex;
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
    return { allQuestionIds: ids, questionIndexMap: idxMap, questionToPartMap: partMap, questionDataMap: dataMap };
  }, [parts]);

  const scrollToQuestion = (qNum: number | string) => {
    const targetPartIndex = questionToPartMap[String(qNum)];
    setActiveQuestionId(String(qNum));
    
    if (targetPartIndex !== undefined && targetPartIndex !== currentPartIndex) {
      setCurrentPartIndex(targetPartIndex);
      setTimeout(() => {
        const el = document.getElementById(`q-${qNum}`);
        if (el) { 
            el.scrollIntoView({ behavior: 'smooth', block: 'center' }); 
            el.classList.add('bg-slate-200', 'transition-colors', 'duration-500'); 
            setTimeout(() => el.classList.remove('bg-slate-200'), 1500); 
        }
      }, 150);
    } else {
      const el = document.getElementById(`q-${qNum}`);
      if (el) { 
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
          el.classList.add('bg-slate-200', 'transition-colors', 'duration-500'); 
          setTimeout(() => el.classList.remove('bg-slate-200'), 1500); 
      }
    }
  };

  useEffect(() => {
     if (allQuestionIds.length > 0 && !activeQuestionId) {
         setActiveQuestionId(allQuestionIds[0]);
     }
  }, [allQuestionIds]);

  useEffect(() => {
    if (!testStarted || isReviewMode) return;
    if (basicInfo?.category === 'exercise') return;
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
      const m = Math.floor(seconds / 60).toString().padStart(2, '0');
      const s = (seconds % 60).toString().padStart(2, '0');
      return `${m}:${s}`;
  };

  const [highlightMenu, setHighlightMenu] = useState<{ x: number, y: number, show: boolean, isClear?: boolean, targetNode?: HTMLElement | null }>({ x: 0, y: 0, show: false, isClear: false, targetNode: null });
  const [currentRange, setCurrentRange] = useState<Range | null>(null);
  const [stickyNote, setStickyNote] = useState({ show: false, id: '', text: '', x: 0, y: 0 });

  const leftPaneRef = useRef<HTMLElement>(null);

  const handleMouseUp = () => {
    if (isReviewMode) return;
    
    const selection = window.getSelection();
    if (selection && selection.toString().trim().length > 0) {
      if (leftPaneRef.current && leftPaneRef.current.contains(selection.anchorNode)) {
          const range = selection.getRangeAt(0);
          const rect = range.getBoundingClientRect();
          setHighlightMenu({ x: rect.left + rect.width / 2, y: rect.top - 10, show: true, isClear: false, targetNode: null });
          setCurrentRange(range);
          return;
      }
    } 
    setHighlightMenu(prev => ({ ...prev, show: false })); 
    setCurrentRange(null);
  };

  const handleContentClick = (e: React.MouseEvent) => {
    const target = e.target as HTMLElement;
    if (target.tagName === 'SPAN' && target.dataset.noteId) { 
        const rect = target.getBoundingClientRect();
        setStickyNote({ show: true, id: target.dataset.noteId, text: target.dataset.noteText || '', x: rect.left, y: rect.bottom + 10 });
        setHighlightMenu(prev => ({ ...prev, show: false }));
    }
    else if (target.tagName === 'SPAN' && target.classList.contains('bg-yellow-300') && !target.dataset.noteId) {
        const rect = target.getBoundingClientRect();
        setHighlightMenu({ x: rect.left + rect.width / 2, y: rect.top - 10, show: true, isClear: true, targetNode: target });
        setStickyNote(prev => ({ ...prev, show: false }));
    }
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
          span.className = 'bg-yellow-300 cursor-pointer rounded-none'; 
          try { 
              currentRange.surroundContents(span); 
          } catch (e) {
              console.error("Lỗi highlight", e);
          } 
          setHighlightMenu({ ...highlightMenu, show: false });
          window.getSelection()?.removeAllRanges(); 
      } 
  };

  const clearHighlight = () => {
      if (highlightMenu.targetNode && highlightMenu.targetNode.parentNode) {
          const parent = highlightMenu.targetNode.parentNode;
          while (highlightMenu.targetNode.firstChild) {
              parent.insertBefore(highlightMenu.targetNode.firstChild, highlightMenu.targetNode);
          }
          parent.removeChild(highlightMenu.targetNode);
          parent.normalize();
      }
      setHighlightMenu({ ...highlightMenu, show: false, isClear: false, targetNode: null });
  };

  const initNote = () => {
    if (currentRange) {
      const noteId = 'note_' + new Date().getTime();
      const span = document.createElement('span'); 
      span.className = 'bg-yellow-300 cursor-pointer rounded-none border-b-2 border-slate-800'; 
      span.dataset.noteId = noteId; 
      span.dataset.noteText = '';
      try { 
          currentRange.surroundContents(span); 
          const rect = span.getBoundingClientRect();
          setStickyNote({ show: true, id: noteId, text: '', x: rect.left, y: rect.bottom + 10 });
      } catch (e) { 
          alert("Chỉ bôi đen gọn trong 1 đoạn văn!"); 
      }
      setHighlightMenu({ ...highlightMenu, show: false }); 
      window.getSelection()?.removeAllRanges();
    }
  };

  const showLeftColumn = !(isListening && !isReviewMode);

  const [leftWidth, setLeftWidth] = useState(50);
  const [listeningWidth, setListeningWidth] = useState(768); 
  
  const containerRef = useRef<HTMLElement>(null);
  const isDragging = useRef(false);
  const listeningDragRef = useRef(false);

  const startDrag = () => { 
      isDragging.current = true; 
      document.body.style.cursor = 'col-resize';
      document.body.style.userSelect = 'none'; 
  };

  const startListeningDrag = (e: React.MouseEvent | React.TouchEvent) => {
      // Don't prevent default on touch start immediately to avoid breaking scrolling globally, 
      // but we do want to drag.
      listeningDragRef.current = true;
      document.body.style.cursor = 'col-resize';
      document.body.style.userSelect = 'none';
  };
  
  const stopDrag = () => { 
      isDragging.current = false;
      listeningDragRef.current = false;
      document.body.style.cursor = 'default'; 
      document.body.style.userSelect = 'auto'; 
  };
  
  const onDrag = (e: MouseEvent | TouchEvent) => {
    const clientX = 'touches' in e ? e.touches[0]?.clientX : e.clientX;
    if (clientX === undefined) return;
    
    if (isDragging.current && containerRef.current && showLeftColumn) {
        const containerRect = containerRef.current.getBoundingClientRect(); 
        const newLeftWidth = ((clientX - containerRect.left) / containerRect.width) * 100;
        if (newLeftWidth > 20 && newLeftWidth < 80) {
            setLeftWidth(newLeftWidth);
        }
    } else if (listeningDragRef.current) {
        const newWidth = (clientX - window.innerWidth / 2) * 2;
        if (newWidth >= 600 && newWidth <= window.innerWidth - 32) {
            setListeningWidth(newWidth);
        }
    }
  };

  useEffect(() => { 
      window.addEventListener('mousemove', onDrag); 
      window.addEventListener('mouseup', stopDrag); 
      window.addEventListener('touchmove', onDrag, { passive: false }); 
      window.addEventListener('touchend', stopDrag); 
      return () => { 
          window.removeEventListener('mousemove', onDrag); 
          window.removeEventListener('mouseup', stopDrag); 
          window.removeEventListener('touchmove', onDrag); 
          window.removeEventListener('touchend', stopDrag);
      }; 
  }, [showLeftColumn]);

  const rightPaneRef = useRef<HTMLElement>(null);
  const scrollRafRef = useRef<number | null>(null);
  const autoScrollSpeed = useRef<number>(0);

  const startAutoScroll = () => {
    if (scrollRafRef.current) return;
    const scrollStep = () => {
      if (rightPaneRef.current && autoScrollSpeed.current !== 0) {
        rightPaneRef.current.scrollTop += autoScrollSpeed.current;
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
      if (!draggedOption || !rightPaneRef.current) return;
      const container = rightPaneRef.current;
      const rect = container.getBoundingClientRect();
      const threshold = 120; 
      const y = e.clientY;
      const x = e.clientX;

      if (x < rect.left || x > rect.right || y < rect.top || y > rect.bottom) {
        stopAutoScroll(); 
        return;
      }

      if (y >= rect.top && y < rect.top + threshold) {
        autoScrollSpeed.current = -25 * (1 - (y - rect.top) / threshold) - 2;
        startAutoScroll();
      } 
      else if (y <= rect.bottom && y > rect.bottom - threshold) {
        autoScrollSpeed.current = 25 * (1 - (rect.bottom - y) / threshold) + 2;
        startAutoScroll();
      } 
      else {
        stopAutoScroll();
      }
    };

    if (draggedOption) {
        window.addEventListener('dragover', handleGlobalDragOver);
    } else {
        stopAutoScroll();
    }

    return () => {
      window.removeEventListener('dragover', handleGlobalDragOver);
      stopAutoScroll();
    }
  }, [draggedOption]);

  const onDragStart = (e: React.DragEvent<HTMLDivElement>, option: string) => {
    if (isReviewMode) return;
    e.stopPropagation(); 
    setDraggedOption(option);
  };

  const onDrop = (qId: string) => {
    stopAutoScroll();
    if (isReviewMode || !draggedOption) return;
    const match = draggedOption.match(/^([A-Z])[\.\):]\s/);
    const valueToSave = match ? match[1].toUpperCase() : draggedOption;
    handleAnswer(qId, valueToSave);
    setDraggedOption(null);
  };

  const clearDragAnswer = (qId: string) => {
    if (isReviewMode) return;
    handleAnswer(qId, '');
  };

  const handleSoundCheck = () => {
    if (globalAudioRef.current) {
      globalAudioRef.current.currentTime = 0;
      const playPromise = globalAudioRef.current.play();
      if (playPromise !== undefined) {
        playPromise.then(() => {
          setTimeout(() => { 
              globalAudioRef.current?.pause(); 
          }, 3000);
        }).catch(error => console.log("Trình duyệt tạm thời chặn autoplay âm thanh", error));
      }
    }
  };

  // 🚀 TÍNH NĂNG CHAT VỚI AI ĐỂ GIẢI THÍCH (BẰNG TEXT)
  const askAIToExplain = (questionId: string, qContent: string, qExplanation: string) => {
     const passageContent = currentPart?.content ? currentPart.content.replace(stripHtmlRegex, '') : "";
     window.dispatchEvent(new CustomEvent('tony-update-lecture-context', {
       detail: { title: basicInfo.title, html: passageContent }
     }));
     
     const displayPrompt = `**Câu hỏi số ${questionIndexMap[questionId] || questionId}:**\n${qContent.replace(stripHtmlRegex, '')}\n\n**Đáp án & Giải thích gốc:**\n${qExplanation.replace(stripHtmlRegex, '')}`;
     
     const fakeBtn = document.createElement('button');
     fakeBtn.className = 'btn-ai-trigger hidden';
     fakeBtn.setAttribute('data-task', 'reading');
     fakeBtn.setAttribute('data-topic', displayPrompt);
     document.body.appendChild(fakeBtn);
     fakeBtn.click();
     setTimeout(() => { fakeBtn.remove(); }, 100);
  };

  // 🚀 TÍNH NĂNG GỌI GIA SƯ (VOICE) CHO TỪNG CÂU HỎI KÈM LỆNH AUTO_START
  const callTutorForQuestion = (q: any) => {
      const plainContent = String(q.content || '').replace(stripHtmlRegex, '').trim();
      const plainExplanation = String(q.explanation || 'Không có lời giải thích.').replace(stripHtmlRegex, '').trim();
      const correctAns = String(q.correctAnswer || '');
      const userAns = String(answers[String(q.id)] || '(trống)');
      
      const tutorContext = {
          overall: scoreResult.band,
          transcript: `Câu hỏi: "${plainContent}". \nĐáp án của học sinh: ${userAns}. \nĐáp án đúng: ${correctAns}. \nGiải thích gốc: "${plainExplanation}".`,
          feedback: "Bạn là gia sư IELTS. Học sinh đang xem lại câu hỏi này trong phần Review. Hãy chủ động chào và giải thích chi tiết tại sao đáp án lại như vậy, phân tích từ vựng/ngữ pháp liên quan. Dùng giọng điệu tự nhiên, ân cần như đang dạy kèm 1-1."
      };
      
      sessionStorage.setItem('tony_live_mode', 'TUTOR');
      sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
      sessionStorage.setItem('tony_auto_start', 'true'); // ÉP AI TỰ ĐỘNG BỐC MÁY
      
      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
  };

  const renderHtmlWithHoles = (htmlStr: any, sec: any) => {
    if (!htmlStr) return null;
    const safeText = String(htmlStr);

    if (typeof window === 'undefined') {
        return <span className="html-content-renderer" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(safeText) }} />;
    }

    const processedHtml = safeText.replace(/\[\s*(\d+)\s*\]/g, '<hole data-id="$1"></hole>');
    const cleanProcessedHtml = cleanHtmlContent(processedHtml);
    const parser = new DOMParser();
    const doc = parser.parseFromString(cleanProcessedHtml, 'text/html');
    
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
            
            if (isReviewMode) {
              const qData = parts.flatMap((p: any) => Array.isArray(p?.sections) ? p.sections.flatMap((s: any) => s?.questions) : []).find((q: any) => String(q?.id) === String(qNum));
              const correctAns = String(qData?.correctAnswer || '');
              const isCorrect = isAnswerCorrect(userAns, correctAns);

              let displayUserAnsForReview = userAns;
              if (["Kéo thả", "Kéo thả vào Part", "Matching"].includes(sec.questionType)) {
                  let allOpts: string[] = [];
                  (sec?.questions || []).forEach((q: any) => {
                      (q.options || []).forEach((o: any) => {
                          const cOpt = String(o).replace(stripHtmlRegex, '').trim();
                          if (cOpt && !allOpts.includes(cOpt)) allOpts.push(cOpt);
                      });
                  });
                  if (userAns && /^[A-Z]$/i.test(userAns)) {
                      const oIdx = userAns.toUpperCase().charCodeAt(0) - 65;
                      if (allOpts[oIdx]) {
                          displayUserAnsForReview = allOpts[oIdx].replace(/^[A-Z][\.\):]\s*/i, '');
                      }
                  } else if (userAns) {
                      displayUserAnsForReview = userAns.replace(/^[A-Z][\.\):]\s*/i, '');
                  }
              }

              return (
                <span key={pathKey} id={`q-${qNum}`} className="relative inline-flex items-center align-middle mx-1 -translate-y-[2px] whitespace-nowrap" style={{ textIndent: 0 }}>
                  <span className={`shrink-0 inline-flex items-center justify-center leading-none px-3 py-1 text-[14px] font-bold font-sans text-white rounded-none border border-black ${isCorrect ? 'bg-emerald-600' : 'bg-red-600'}`} style={{ color: '#ffffff', textIndent: 0 }}>
                    {displayIndex}. {displayUserAnsForReview || '(trống)'}
                  </span>
                  {!isCorrect && (
                    <span className="absolute top-full left-0 mt-1 text-[12px] font-sans text-white font-bold bg-slate-800 px-2 py-1 rounded-none whitespace-nowrap z-10" style={{ color: '#ffffff', textIndent: 0 }}>
                      ĐA: {correctAns}
                    </span>
                  )}
                </span>
              );
            }

            if (["Kéo thả", "Kéo thả vào Part", "Matching"].includes(sec.questionType)) {
                let allOpts: string[] = [];
                (sec?.questions || []).forEach((q: any) => {
                    (q.options || []).forEach((o: any) => {
                        const cOpt = String(o).replace(stripHtmlRegex, '').trim();
                        if (cOpt && !allOpts.includes(cOpt)) allOpts.push(cOpt);
                    });
                });
                
                let displayUserAns = userAns;
                if (userAns && /^[A-Z]$/i.test(userAns)) {
                    const oIdx = userAns.toUpperCase().charCodeAt(0) - 65;
                    if (allOpts[oIdx]) {
                        displayUserAns = allOpts[oIdx].replace(/^[A-Z][\.\):]\s*/i, '');
                    }
                } else if (userAns) {
                    displayUserAns = userAns.replace(/^[A-Z][\.\):]\s*/i, '');
                }

                return (
                    <span 
                      key={pathKey} 
                      id={`q-${qNum}`} 
                      onDragOver={(e) => e.preventDefault()} 
                      onDrop={() => onDrop(qNum)} 
                      onClick={(e) => { e.stopPropagation(); setActiveQuestionId(String(qNum)); }} 
                      className={`inline-flex items-center justify-center align-middle mx-1 my-1 min-w-[120px] h-[30px] border rounded-none transition-all px-2 cursor-pointer ${activeQuestionId === String(qNum) ? 'border-slate-800 bg-slate-100' : 'border-slate-500 bg-white hover:bg-slate-100'}`}
                      style={{ textIndent: 0 }}
                    >
                        <span className="shrink-0 inline-flex items-center justify-center leading-none font-bold text-white bg-slate-800 px-1.5 min-w-[24px] h-[24px] text-[12px] mr-2 rounded-none" style={{ color: '#ffffff', textIndent: 0 }}>
                            {displayIndex}
                        </span>
                        {userAns ? (
                            <div className="flex items-center justify-between w-full text-slate-800 font-sans text-[14px] font-bold" style={{ textIndent: 0 }}>
                                <span className="truncate">{displayUserAns}</span>
                                <button onClick={(e) => { e.stopPropagation(); clearDragAnswer(qNum); }} className="ml-2 hover:text-red-500 text-[14px] font-black font-sans">✕</button>
                            </div>
                        ) : ( 
                            <span className="text-slate-400 text-[13px] italic font-sans w-full text-center" style={{ textIndent: 0 }}>Thả vào đây</span> 
                        )}
                    </span>
                );
            }

            if (qInfo.qType === 'Droplist' || sec.questionType === "Droplist") {
               const rawOptions = (qInfo.options && qInfo.options.length > 0) ? qInfo.options : (sec.questions?.[0]?.options || []);
               const validOptions = rawOptions.filter(Boolean);
               
               return (
                 <span key={pathKey} id={`q-${qNum}`} className="inline-flex items-center align-middle mx-1 my-1 whitespace-nowrap" style={{ textIndent: 0 }}>
                    <span className={`shrink-0 inline-flex items-center justify-center leading-none text-white font-bold px-2 min-w-[30px] h-[30px] text-[14px] rounded-none border border-slate-800 border-r-0 ${activeQuestionId === qNum ? 'bg-slate-900' : 'bg-slate-800'}`} style={{ color: '#ffffff', textIndent: 0 }}>
                      {displayIndex}
                    </span>
                    <select 
                      value={userAns}
                      onFocus={() => setActiveQuestionId(qNum)}
                      onChange={(e) => handleAnswer(qNum, e.target.value)}
                      className="shrink-0 bg-white border border-slate-800 text-slate-800 font-bold font-sans text-[14px] h-[30px] px-1 rounded-none outline-none focus:border-black cursor-pointer min-w-[100px] max-w-[200px] truncate"
                      style={{ textIndent: 0 }}
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

            return (
              <span key={pathKey} id={`q-${qNum}`} onClick={(e) => { e.stopPropagation(); setActiveQuestionId(String(qNum)); }} className="inline-flex items-center align-middle mx-1 my-1 whitespace-nowrap shadow-sm" style={{ textIndent: 0 }}>
                <span className={`shrink-0 inline-flex items-center justify-center leading-none text-white font-bold px-2 min-w-[30px] h-[30px] text-[14px] rounded-none border border-slate-800 border-r-0 ${activeQuestionId === String(qNum) ? 'bg-slate-900' : 'bg-slate-800'}`} style={{ color: '#ffffff', textIndent: 0 }}>
                  {displayIndex}
                </span>
                <input 
                  type="text" 
                  className="shrink-0 inline-block w-24 sm:w-32 border border-slate-800 bg-white text-center font-sans text-slate-800 font-bold px-2 text-[14px] h-[30px] rounded-none m-0 focus:outline-none focus:ring-1 focus:ring-slate-800" 
                  value={userAns} 
                  onFocus={() => setActiveQuestionId(String(qNum))}
                  onChange={(e) => handleAnswer(qNum, e.target.value)} 
                  autoComplete="off"
                  spellCheck="false"
                  style={{ textIndent: 0 }}
                />
              </span>
            );
        }

        const props: any = { key: pathKey };
        Array.from(el.attributes).forEach(attr => {
          if (attr.name === 'class') {
              props.className = attr.value;
          } else if (attr.name === 'style') {
              props.style = parseStyle(attr.value);
          } else if (attr.name === 'for') {
              props.htmlFor = attr.value;
          } else if (attr.name.startsWith('data-') || attr.name.startsWith('aria-')) {
              props[attr.name] = attr.value;
          } else {
            const camelCaseAttr = attr.name.replace(/-([a-z])/g, g => g[1].toUpperCase());
            const reactProp = attr.name === 'colspan' ? 'colSpan' : attr.name === 'rowspan' ? 'rowSpan' : attr.name === 'cellpadding' ? 'cellPadding' : attr.name === 'cellspacing' ? 'cellSpacing' : attr.name === 'tabindex' ? 'tabIndex' : camelCaseAttr;
            props[reactProp] = attr.value;
          }
        });

        const children = Array.from(el.childNodes).map((child, i) => renderNode(child, `${pathKey}-${i}`));
        const voidElements = ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'];
        
        if (voidElements.includes(tagName)) {
            return React.createElement(tagName, props);
        }
        
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
        if (safeTestData?.id) {
            localStorage.setItem(`ielts_endtime_${safeTestData.id}`, currentEndTime.toString());
        }
        setTimeLeft(initialSeconds);
    } else {
        const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
        setTimeLeft(remaining);
        if (remaining <= 0 && basicInfo?.category !== 'exercise') {
            alert("⏰ Bài thi này đã hết thời gian làm bài!");
            handleFinish();
            return;
        }
    }
    if (globalAudioRef.current && isListening) { 
        globalAudioRef.current.play().catch(e => { 
            console.error("Autoplay blocked:", e); 
        });
    }
  };

  return (
    <React.Fragment>
      <style>{`
          .format-passage { overflow: visible !important; }
          .format-passage table { display: block; overflow-x: auto; overflow-y: hidden !important; width: 100% !important; min-width: 600px; border-collapse: collapse !important; margin-top: 1.5rem !important; margin-bottom: 1.5rem !important; }
          .html-content-renderer table { display: block; overflow-x: auto; overflow-y: hidden !important; width: 100% !important; min-width: 600px; border-collapse: collapse !important; margin-top: 1.5rem !important; margin-bottom: 1.5rem !important; }
          .format-passage table::-webkit-scrollbar:vertical, .html-content-renderer table::-webkit-scrollbar:vertical { display: none !important; width: 0px !important; }
          .format-passage input::-webkit-scrollbar, .format-passage span::-webkit-scrollbar, .html-content-renderer input::-webkit-scrollbar, .html-content-renderer span::-webkit-scrollbar { display: none !important; }
          .format-passage input, .format-passage span { scrollbar-width: none !important; }
          .format-passage::-webkit-scrollbar { height: 8px; }
          .format-passage::-webkit-scrollbar-thumb { background-color: #cbd5e1; border-radius: 4px; }
          .format-passage p { margin-bottom: 1.25rem !important; }
          .format-passage p:last-child { margin-bottom: 0 !important; }
          .format-passage p:empty, .html-content-renderer p:empty { display: none !important; }
          .format-passage p > br:only-child, .html-content-renderer p > br:only-child { display: none !important; }
          .format-passage br, .html-content-renderer br { display: inline !important; content: normal !important; margin: 0 !important; }
          .format-passage ul { list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1.25rem; }
          .format-passage ul ul { list-style-type: circle; margin-top: 0.5rem; margin-bottom: 0; padding-left: 1.5rem; }
          .format-passage ul ul ul { list-style-type: square; }
          .format-passage ol { list-style-type: decimal; padding-left: 1.5rem; margin-bottom: 1.25rem; }
          .format-passage li { margin-bottom: 0.5rem; }
          .format-passage li > p { margin-bottom: 0 !important; display: inline; }
          .format-passage p:has(+ ul), .html-content-renderer p:has(+ ul) { margin-bottom: 0.25rem !important; }
          .format-passage p + ul, .html-content-renderer p + ul { margin-top: 0 !important; }
          @supports not selector(:has(+ ul)) { .format-passage p + ul, .html-content-renderer p + ul { margin-top: -1rem !important; } }
          .format-passage th, .format-passage td, .html-content-renderer th, .html-content-renderer td { border: 1px solid #444 !important; padding: 12px 16px !important; vertical-align: top !important; white-space: normal !important; word-break: break-word !important; }
          .format-passage th, .html-content-renderer th { background-color: #e5e5e5 !important; font-weight: 900 !important; color: #000 !important; }
          .format-passage table *, .html-content-renderer table * { font-family: inherit !important; line-height: 1.6 !important; }
          .format-passage table p, .html-content-renderer table p { margin: 0 !important; display: inline-block !important; }
          .format-passage td span, .html-content-renderer td span { text-indent: 0 !important; }
          .format-passage td input, .format-passage td select, .html-content-renderer td input, .html-content-renderer td select { max-width: 100%; }
          .html-content-renderer ul { list-style: disc outside !important; padding-left: 1.5rem !important; margin: 0.5rem 0 !important; }
          .html-content-renderer ul ul { list-style-type: circle !important; padding-left: 1.5rem !important; }
          .html-content-renderer ol { list-style: decimal outside !important; padding-left: 1.5rem !important; margin: 0.5rem 0 !important; }
          .html-content-renderer li { margin-bottom: 0.25rem !important; }
          .html-content-renderer li > p, .html-content-renderer li > div { display: inline !important; margin: 0 !important; }
          .html-content-renderer img { max-width: 100% !important; width: 80% !important; height: auto !important; display: block !important; margin-left: auto !important; margin-right: auto !important; margin-top: 1.5rem !important; margin-bottom: 1.5rem !important; }
      `}</style>

      {isListening && globalAudio && !isReviewMode && ( 
          <audio 
              ref={globalAudioRef} 
              src={globalAudio} 
              preload="auto" 
              className="hidden" 
              onEnded={() => { 
                  if (currentAudioIndex < audioPlaylist.length - 1) {
                      setCurrentAudioIndex(prev => prev + 1); 
                  }
              }} 
          /> 
      )}

      {!testStarted ? (
        <div className="flex flex-col h-screen items-center justify-center bg-[#eeeeee] font-sans">
          <div className="bg-white p-10 rounded-none border border-slate-300 shadow-sm text-center max-w-lg w-full">
            <div className="text-6xl mb-6">{isListening ? '🎧' : '💻'}</div>
            <h1 className="text-2xl font-black text-slate-900 mb-2">{basicInfo.title || "IELTS Test"}</h1>
            {basicInfo?.category === 'exercise' ? (
                <p className="text-emerald-600 font-black tracking-widest uppercase mb-8">BÀI TẬP</p>
            ) : (
                <p className="text-slate-600 mb-8 font-medium">Thời gian: {formatTime(parseInitialTime(basicInfo.timeLimit))}</p>
            )}
            
            {isListening && (
              <div className="bg-slate-100 border border-slate-300 p-5 text-slate-800 text-[13px] font-bold mb-8 text-left leading-[1.8] rounded-none font-sans">
                <p className="mb-3">LƯU Ý THI LISTENING: Hệ thống sẽ tự động phát âm thanh ngay khi bắt đầu. Bạn hãy kiểm tra và chỉnh âm lượng trước tại đây nhé.</p>
                <div className="flex flex-col sm:flex-row items-start sm:items-center gap-4 bg-white p-3 border border-slate-400">
                  <button onClick={handleSoundCheck} className="bg-slate-800 hover:bg-black text-white px-4 py-1.5 rounded-none font-bold transition text-[13px]">Test Loa 🔊</button>
                   <div className="flex items-center gap-2 w-full flex-1">
                     <span className="text-sm">🔈</span>
                     <input 
                         type="range" 
                         min="0" max="1" step="0.05" defaultValue="1" 
                         onChange={(e) => { 
                             if(globalAudioRef.current) {
                                 globalAudioRef.current.volume = parseFloat(e.target.value);
                             } 
                         }} 
                         className="w-full accent-black cursor-pointer" 
                     />
                   </div>
                </div>
              </div>
            )}
            <div className="flex gap-4 justify-center">
              <button onClick={handleExit} className="px-6 py-2.5 rounded-none font-bold text-slate-700 hover:bg-slate-200 border border-slate-400 transition text-[14px]">Quay lại</button>
              <button onClick={handleStartTest} className="bg-slate-800 hover:bg-black text-white font-bold px-8 py-2.5 rounded-none transition text-[14px]">Bắt Đầu Làm Bài</button>
            </div>
          </div>
        </div>
      ) : (
        <div className="flex flex-col h-screen bg-[#eeeeee] font-sans text-slate-900 relative">
          
          {highlightMenu.show && !isReviewMode && (
            <div style={{ left: highlightMenu.x, top: highlightMenu.y, transform: 'translate(-50%, -100%)' }} className="fixed z-50 bg-white text-slate-900 rounded-none shadow-md border border-slate-400 text-[13px] flex flex-col py-1 min-w-[130px]" onMouseDown={(e) => e.preventDefault()}>
              {highlightMenu.isClear ? (
                 <button onClick={clearHighlight} className="flex items-center gap-3 px-4 py-2 hover:bg-red-50 text-left w-full text-red-600 border-b border-transparent font-sans">
                     <span className="font-bold">Clear Highlight</span>
                 </button>
              ) : (
                 <React.Fragment>
                   <button onClick={handleCopy} className="flex items-center gap-3 px-4 py-2 hover:bg-slate-200 text-left w-full font-sans">
                       <span className="font-bold">Copy</span>
                   </button>
                   <button onClick={applyHighlight} className="flex items-center gap-3 px-4 py-2 hover:bg-slate-200 text-left w-full font-sans">
                       <span className="font-bold">Highlight</span>
                   </button>
                   <button onClick={initNote} className="flex items-center gap-3 px-4 py-2 hover:bg-slate-200 text-left w-full font-sans">
                       <span className="font-bold">Note</span>
                   </button>
                 </React.Fragment>
              )}
            </div>
          )}

          {stickyNote.show && (
            <div style={{ left: Math.min(stickyNote.x, window.innerWidth - 300), top: stickyNote.y }} className="fixed z-50 flex flex-col shadow-md rounded-none border border-slate-500 w-72">
              <div className="bg-amber-100 h-8 flex justify-between items-center px-3 cursor-move border-b border-amber-300 font-sans">
                 <span className="text-[11px] font-bold text-slate-800 uppercase tracking-widest">Note</span>
                 <button onClick={() => setStickyNote({...stickyNote, show: false})} className="text-slate-800 font-bold text-sm">✕</button>
              </div>
              <div className="bg-amber-50 p-3 relative rounded-none font-sans">
                <textarea 
                    autoFocus 
                    value={stickyNote.text} 
                    onChange={(e) => setStickyNote({ ...stickyNote, text: e.target.value })} 
                    className="w-full h-32 bg-transparent outline-none resize-none text-[14px] text-slate-900 font-medium custom-scrollbar" 
                    placeholder="Nhập ghi chú..." 
                    disabled={isReviewMode} 
                />
                {!isReviewMode && (
                  <div className="flex justify-between items-center mt-2 border-t border-amber-200 pt-2 font-sans">
                    <button 
                        onClick={() => { 
                            const span = document.querySelector(`span[data-note-id="${stickyNote.id}"]`) as HTMLElement;
                            if (span && span.parentNode) {
                                span.parentNode.replaceChild(document.createTextNode(span.textContent || ''), span); 
                            }
                            setStickyNote({ ...stickyNote, show: false });
                        }} 
                        className="text-red-600 text-[12px] font-bold hover:underline"
                    >
                        Xóa Note
                    </button>
                    <button 
                        onClick={() => { 
                            const span = document.querySelector(`span[data-note-id="${stickyNote.id}"]`) as HTMLElement;
                            if (span) {
                                span.dataset.noteText = stickyNote.text; 
                            }
                            setStickyNote({ ...stickyNote, show: false });
                        }} 
                        className="bg-slate-800 hover:bg-black text-white text-[12px] font-bold px-4 py-1.5 rounded-none transition"
                    >
                        Lưu lại
                    </button>
                  </div>
                )}
              </div>
            </div>
          )}

          <header className={`h-[46px] ${isReviewMode ? 'bg-[#064e3b]' : 'bg-[#222222]'} text-white flex justify-between items-center px-4 z-20 shrink-0 border-b border-slate-700 relative font-sans`}>
            <div className="flex items-center gap-2">
              <UserIcon />
              <span className="font-bold text-[14px] truncate max-w-[200px] md:max-w-xs text-white">
                 {isReviewMode ? `[REVIEW] ${basicInfo.title || "IELTS"}` : (basicInfo.title || "IELTS Test")}
              </span>
            </div>
            
            {isReviewMode ? (
               <div className="absolute left-1/2 -translate-x-1/2 flex items-center gap-3">
                  <div className="font-bold text-[14px] tracking-wide text-white bg-black px-4 py-1 border border-[#10b981] rounded-none">
                     Điểm: {scoreResult.score}/{scoreResult.total} (Band {scoreResult.band})
                  </div>
               </div>
            ) : (
               <div className={`absolute left-1/2 -translate-x-1/2 font-bold text-[15px] tracking-widest ${basicInfo?.category === 'exercise' ? 'text-[#0ea5e9]' : (timeLeft <= 300 ? 'text-red-500 animate-pulse' : 'text-white')}`}>
                  {basicInfo?.category === 'exercise' ? 'BÀI TẬP' : formatTime(timeLeft)}
               </div>
            )}

            <div className="flex items-center gap-4 shrink-0">
               {!isReviewMode && (
                   <button onClick={clearDraft} className="text-[12px] text-slate-300 hover:text-white font-bold transition mr-2 hidden sm:block">
                       Clear Draft
                   </button>
               )}
               
               {isReviewMode ? (
                  <div className="flex items-center gap-4">
                     <button onClick={toggleFullscreen} className="hover:text-white text-slate-300 transition" title="Toàn màn hình">
                        {isFullscreen ? <ExitFullscreenIcon /> : <FullscreenIcon />}
                     </button>
                     <button onClick={resetTest} className="text-[12px] font-bold border border-white px-3 py-1 rounded-none hover:bg-white/10 transition text-white">
                         Retake Test
                     </button>
                  </div>
               ) : (
                  <div className="flex items-center gap-4">
                     {isListening && globalAudio && (
                        <div className="flex items-center gap-2 mr-2 bg-black/40 px-2 py-1 rounded-none border border-slate-500 hidden sm:flex" title="Chỉnh âm lượng">
                         <span className="text-sm">🔈</span>
                         <input 
                             type="range" min="0" max="1" step="0.05" defaultValue="1" 
                             onChange={(e) => { 
                                 if(globalAudioRef.current) {
                                     globalAudioRef.current.volume = parseFloat(e.target.value);
                                 } 
                             }} 
                             className="w-20 h-1 accent-white cursor-pointer" 
                         />
                       </div>
                     )}
                     <button onClick={toggleFullscreen} className="hover:text-white text-slate-300 transition" title="Toàn màn hình">
                        {isFullscreen ? <ExitFullscreenIcon /> : <FullscreenIcon />}
                     </button>
                     <button onClick={handleExit} className="hover:text-white text-slate-300 transition text-[13px] font-bold tracking-wide">Exit</button>
                     <button className="hover:text-white text-slate-300 transition" title="Settings">
                        <SettingsIcon />
                     </button>
                  </div>
               )}
            </div>
          </header>

          <div className={`border-b border-slate-400 px-6 pt-2 pb-0 flex gap-4 overflow-x-auto font-sans ${isReviewMode ? 'bg-[#f4f4f4]' : 'bg-white'}`}>
            {(Array.isArray(parts) ? parts : []).map((p: any, index: number) => {
              const isActive = currentPartIndex === index;
              return (
                <button 
                  key={index} 
                  onClick={() => setCurrentPartIndex(index)} 
                  className={`px-3 py-2 text-[14px] font-bold transition-all whitespace-nowrap border-b-[3px] rounded-none ${isActive ? (isReviewMode ? 'text-[#064e3b] border-[#064e3b]' : 'text-black border-black') : 'text-slate-500 border-transparent hover:text-black'}`}
                >
                  {p.title || `Part ${index + 1}`}
                </button>
              )
            })}
          </div>

          <main className="flex flex-1 overflow-hidden relative bg-[#eeeeee]" ref={containerRef} onMouseUp={handleMouseUp} onClick={handleContentClick}>
            
            {showLeftColumn && (
              <React.Fragment>
                <div className="flex flex-col h-full bg-white relative" style={{ width: window.innerWidth > 768 ? `${leftWidth}%` : '100%', flex: 'none' }}>
                    
                    {isReviewMode && isListening && currentPart?.audioUrl && (
                      <div className="bg-[#f4f4f4] p-4 border-b border-slate-400 flex items-center gap-4 shrink-0 shadow-sm z-10 font-sans">
                        <p className="text-[12px] font-black text-slate-800 uppercase tracking-widest shrink-0">Audio Part:</p>
                        <audio controls controlsList="nodownload" className="h-10 flex-1 outline-none w-full">
                          <source src={currentPart.audioUrl} type="audio/mpeg" />
                        </audio>
                      </div>
                    )}
                    
                    <section className="p-8 md:p-10 overflow-y-auto custom-scrollbar flex-1 relative" ref={leftPaneRef as any}>
                      {currentPart?.content ? (
                        <div className={`format-passage html-content-renderer max-w-none text-[16px] text-black break-words font-sans selection:bg-yellow-200 ${isReviewMode ? 'leading-[2.8]' : 'leading-[1.8]'}`}>
                          {isReviewMode && isListening && (
                              <div className="bg-slate-200 text-black p-4 rounded-none font-bold font-sans text-[14px] mb-6 border border-slate-400">
                                  🎙️ TRANSCRIPT CHỮA BÀI
                              </div>
                          )}
                          <div dangerouslySetInnerHTML={{ __html: cleanHtmlContent(currentPart?.content || "") }} />
                        </div>
                      ) : (
                        <div className="flex flex-col items-center justify-center h-full text-slate-400 opacity-70 font-sans">
                           <span className="text-6xl mb-4">📄</span>
                           <p className="font-bold text-[15px]">Blank Passage</p>
                        </div>
                      )}
                      <div className="h-[200px]" />
                    </section>
                </div>
                
                <div 
                    className="w-4 bg-[#e8e8e8] border-x border-[#c0c0c0] hover:bg-[#d4d4d4] cursor-col-resize flex flex-col justify-center items-center z-10 shrink-0 transition-colors shadow-sm" 
                    onMouseDown={startDrag}
                    onTouchStart={startDrag}
                >
                   <div className="flex flex-col gap-1.5 opacity-40">
                      <div className="w-1 h-1 bg-black"></div>
                      <div className="w-1 h-1 bg-black"></div>
                      <div className="w-1 h-1 bg-black"></div>
                      <div className="w-1 h-1 bg-black"></div>
                   </div>
                </div>
              </React.Fragment>
            )}

            <section 
              ref={rightPaneRef as any}
              className={`p-8 md:p-10 overflow-y-auto custom-scrollbar html-content-renderer ${isReviewMode ? 'bg-[#f4f4f4]' : 'bg-[#f4f4f4]'}`} 
              style={{ width: showLeftColumn ? `${100 - leftWidth}%` : '100%', flex: 'none' }}
            >
              <div 
                 className={`mx-auto relative ${!showLeftColumn ? 'pr-8' : ''}`}
                 style={{ width: showLeftColumn ? '100%' : `${listeningWidth}px`, maxWidth: '100%' }}
              >
                <div className="w-full">
                  
                  {currentPart?.audioUrl && (!isListening) && (
                    <div className="mb-8 bg-white p-4 rounded-none border border-slate-400 flex items-center gap-4 font-sans">
                       <p className="text-[12px] font-bold text-slate-800 uppercase tracking-widest shrink-0">Audio Part:</p>
                       <audio controls controlsList="nodownload" className="h-10 flex-1 outline-none">
                          <source src={currentPart.audioUrl} type="audio/mpeg" />
                       </audio>
                    </div>
                  )}
                  
                  {(Array.isArray(currentPart?.sections) ? currentPart.sections : []).map((sec: any, index: number) => {
                    
                    let rawContentText = '';
                    if (String(sec.content || '').match(/\[\s*\d+\s*\]/)) {
                        rawContentText = sec.content;
                        if (Array.isArray(sec.questions)) {
                            sec.questions.forEach((q: any) => {
                                if (q.content && q.content !== sec.content && String(q.content).match(/\[\s*\d+\s*\]/)) {
                                    rawContentText += '<br><br>' + q.content;
                                }
                            });
                        }
                    } else {
                        if (Array.isArray(sec.questions)) {
                            sec.questions.forEach((q: any) => {
                                let qContent = String(q.content || '').trim();
                                if (qContent) {
                                    if (sec.questionType === "Điền từ" && !/\[\s*\d+\s*\]/.test(qContent)) {
                                        qContent += ` [${q.id}]`;
                                    }
                                    rawContentText += (rawContentText ? '<br><br>' : '') + qContent;
                                }
                            });
                        }
                    }

                    const hasInlineBrackets = /\[\s*\d+\s*\]/.test(rawContentText);
                    const isInlineDroplist = sec.questionType === "Droplist" && hasInlineBrackets;
                    const isBlockDroplist = sec.questionType === "Droplist" && !hasInlineBrackets;
                    const isInlineDragDrop = ["Kéo thả", "Matching", "Kéo thả vào Part"].includes(sec.questionType) && hasInlineBrackets;
                    const isBlockDragDrop = ["Kéo thả", "Matching", "Kéo thả vào Part"].includes(sec.questionType) && !hasInlineBrackets;
                    
                    const secContentHasHoles = /\[\s*\d+\s*\]/.test(String(sec.content || ''));
                    const shouldRenderGlobalSecContent = sec.content && !secContentHasHoles;

                    return (
                      <div key={index} className="mb-12">
                        
                        {sec.title && <h3 className="font-bold font-sans text-[17px] mb-3 text-black">{sec.title}</h3>}
                        
                        {shouldRenderGlobalSecContent && (
                            <div className="mb-6 text-[15px] font-bold font-sans text-black bg-white p-4 rounded-none border border-slate-400 html-content-renderer" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(sec.content) }} />
                        )}
                        
                        {(sec.questionType === "Điền từ" || isInlineDroplist) && (
                          <div className={`p-8 bg-white border border-slate-400 rounded-none`}>
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
                                    <React.Fragment>
                                        <div className={`format-passage text-[16px] text-black break-words font-sans html-content-renderer ${isReviewMode ? 'leading-[3.0] pb-6' : 'leading-[2.0]'}`}>
                                            {renderHtmlWithHoles(cleanHtmlContent(mainContent), sec)}
                                        </div>
                                        {wordBankItems.length > 0 && (
                                            <div className="mt-8 p-5 bg-[#f4f4f4] border border-slate-400 rounded-none font-sans">
                                                <p className="text-[13px] font-black text-black uppercase tracking-widest mb-4">Danh sách từ (Word Bank)</p>
                                                <div className="flex flex-wrap gap-3">
                                                    {wordBankItems.map((item, idx) => {
                                                        const text = item.replace(stripHtmlRegex, '').trim();
                                                        return text ? (
                                                            <div key={idx} className="px-4 py-2 bg-white border border-slate-400 rounded-none font-bold text-black min-w-[100px] flex items-center html-content-renderer" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(text) }} />
                                                        ) : null;
                                                    })}
                                                </div>
                                            </div>
                                        )}

                                        {/* 🚀 THÊM BLOCK REVIEW & GỌI GIA SƯ CHO CÂU ĐIỀN TỪ Ở ĐÂY */}
                                        {isReviewMode && (
                                           <div className="w-full mt-8 border-t border-slate-300 pt-6 font-sans">
                                              <p className="text-[14px] font-black text-black uppercase mb-4 tracking-widest">💡 Giải thích chi tiết & Gia sư AI:</p>
                                              <div className="space-y-4">
                                                 {(Array.isArray(sec.questions) ? sec.questions : []).map((q: any) => {
                                                     if (!q?.id) return null;
                                                     const qIdx = questionIndexMap[String(q.id)] || q.id;
                                                     const explanationText = q.explanation || 'Không có lời giải thích.';
                                                     const qContentForAI = q.content || sec.content || 'Điền từ vào chỗ trống trong đoạn văn.';
                                                     
                                                     return (
                                                         <div key={`expl-${q.id}`} className="bg-[#f4f4f4] p-5 border border-slate-300 rounded-none">
                                                             <div className="flex items-center gap-2 mb-2">
                                                                 <span className="bg-slate-800 text-white font-bold px-2 py-0.5 text-[13px] rounded-none">Câu {qIdx}</span>
                                                             </div>
                                                             <div className="text-[15px] text-slate-800 font-medium leading-relaxed font-sans html-content-renderer" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(explanationText) }} />
                                                             
                                                             <div className="flex items-center gap-2 mt-4 pt-4 border-t border-slate-300">
                                                                 <button onClick={(e) => { e.stopPropagation(); askAIToExplain(String(q.id), qContentForAI, explanationText); }} className="px-4 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded-none text-[13px] transition shadow-sm border border-[#064e3b]">
                                                                    💬 Chat với AI
                                                                 </button>
                                                                 <button onClick={(e) => { e.stopPropagation(); callTutorForQuestion({ ...q, content: qContentForAI }); }} className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-none text-[13px] transition shadow-sm border border-emerald-600 flex items-center gap-1">
                                                                    📞 Gọi Gia sư (Voice)
                                                                 </button>
                                                             </div>
                                                         </div>
                                                     );
                                                 })}
                                              </div>
                                           </div>
                                        )}
                                    </React.Fragment>
                                );
                             })()}
                          </div>
                        )}
                        
                        {(sec.questionType === "Trắc nghiệm" || sec.questionType === "TFNG") && (
                           <div className="space-y-6">
                             {(Array.isArray(sec.questions) ? sec.questions : []).map((q: any) => {
                                if (!q?.id) return null;
                                const correctAns = String(q.correctAnswer || '').trim().toUpperCase(); 
                                const userAns = String(answers[String(q.id)] || '').trim().toUpperCase(); 
                                const isCorrect = isAnswerCorrect(userAns, correctAns);
                                const displayIdx = questionIndexMap[String(q.id)] || q.id;
                                
                                const validOptions = (Array.isArray(q.options) ? q.options : []).filter((opt: any) => String(opt || '').trim() !== '');
                                const isTFNG = sec.questionType === "TFNG" || validOptions.some((opt: string) => ['TRUE', 'FALSE', 'NOT GIVEN', 'YES', 'NO'].includes(opt?.trim()?.toUpperCase()));
                                
                                if (isTFNG) {
                                    return (
                                     <div key={q.id} id={`q-${q.id}`} onClick={() => setActiveQuestionId(String(q.id))} className={`p-6 bg-white border rounded-none relative group transition-all flex flex-col gap-4 ${isReviewMode ? (isCorrect ? 'border-emerald-600 bg-emerald-50' : 'border-red-600 bg-red-50') : (activeQuestionId === String(q.id) ? 'border-black' : 'border-slate-400 hover:border-slate-600')}`}>
                                       
                                       <div className="flex items-start gap-4 font-sans w-full">
                                         <span className={`shrink-0 inline-flex items-center justify-center leading-none font-bold min-w-[30px] h-[30px] text-[14px] rounded-none border ${isReviewMode ? (isCorrect ? 'bg-emerald-600 text-white border-emerald-600' : 'bg-red-600 text-white border-red-600') : (activeQuestionId === String(q.id) ? 'bg-slate-900 text-white border-black' : 'bg-white text-black border-slate-800')}`} style={{ textIndent: 0 }}>
                                           {displayIdx}
                                         </span>
                                         <div className="text-[16px] leading-relaxed font-bold text-black cursor-pointer flex-1 min-w-0 font-sans html-content-renderer [&>p]:!m-0 [&>p]:!inline" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.content) }} />
                                       </div>
                                       
                                       <div className={`flex flex-row flex-wrap items-center gap-4 sm:gap-6 font-sans ml-[46px]`}>
                                         {validOptions.map((opt: any, i: number) => {
                                           const safeOpt = String(opt || '');
                                           const optionValue = safeOpt.replace(stripHtmlRegex, '').trim().toUpperCase(); 
                                           const isSelected = userAns === optionValue; 
                                           const isCorrectOpt = isAnswerCorrect(optionValue, correctAns);
                                           let labelClass = "flex items-center gap-2 py-1.5 px-2 rounded-none transition border border-transparent";
                                           
                                           if (isReviewMode) { 
                                              if (isCorrectOpt) labelClass += " bg-emerald-200 border-emerald-600 font-bold text-emerald-900";
                                              else if (isSelected) labelClass += " bg-red-200 border-red-600 text-red-900 line-through opacity-70"; 
                                              else labelClass += " opacity-50";
                                           } else labelClass += " cursor-pointer hover:bg-slate-100";
                                           
                                           return (
                                             <label key={i} className={labelClass}>
                                               <input type="radio" name={`q${q.id}`} value={optionValue} checked={isSelected} onChange={(e) => handleAnswer(String(q.id), e.target.value)} className="w-[18px] h-[18px] accent-black cursor-pointer" disabled={isReviewMode} />
                                               <span className="text-[15px] font-bold text-black html-content-renderer font-sans [&>p]:!m-0 [&>p]:!inline" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(safeOpt) }} />
                                             </label>
                                           );
                                         })}
                                       </div>
                                       
                                       {isReviewMode && (
                                          <div className="w-full mt-2 pt-4 border-t border-slate-300 ml-[46px] font-sans">
                                             <p className="text-[13px] font-black text-black uppercase mb-1">💡 Giải thích đáp án:</p>
                                             <div className="text-[15px] text-slate-800 font-medium leading-relaxed font-sans html-content-renderer" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.explanation || 'Không có lời giải thích.') }} />
                                             <div className="flex items-center gap-2 mt-3">
                                                 <button onClick={() => askAIToExplain(String(q.id), q.content, q.explanation || 'Không có lời giải thích.')} className="px-4 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded-none text-[13px] transition shadow-sm border border-[#064e3b]">
                                                    💬 Chat với AI
                                                 </button>
                                                 <button onClick={() => callTutorForQuestion(q)} className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-none text-[13px] transition shadow-sm border border-emerald-600 flex items-center gap-1">
                                                    📞 Gọi Gia sư (Voice)
                                                 </button>
                                             </div>
                                          </div>
                                       )}
                                     </div>
                                    );
                                }
                                
                                return (
                                 <div key={q.id} id={`q-${q.id}`} onClick={() => setActiveQuestionId(String(q.id))} className={`p-6 bg-white border rounded-none relative group transition-all flex flex-col gap-4 ${isReviewMode ? (isCorrect ? 'border-emerald-600 bg-emerald-50' : 'border-red-600 bg-red-50') : (activeQuestionId === String(q.id) ? 'border-black' : 'border-slate-400 hover:border-slate-600')}`}>
                                   
                                   <div className="flex items-start gap-4 font-sans w-full">
                                     <span className={`shrink-0 inline-flex items-center justify-center leading-none font-bold min-w-[30px] h-[30px] text-[14px] rounded-none border ${isReviewMode ? (isCorrect ? 'bg-emerald-600 text-white border-emerald-600' : 'bg-red-600 text-white border-red-600') : (activeQuestionId === String(q.id) ? 'bg-slate-900 text-white border-black' : 'bg-white text-black border-slate-800')}`} style={{ textIndent: 0 }}>
                                       {displayIdx}
                                     </span>
                                     <div className="text-[16px] leading-relaxed font-bold text-black cursor-pointer flex-1 min-w-0 font-sans html-content-renderer [&>p]:!m-0 [&>p]:!inline" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.content) }} />
                                   </div>
                                   
                                   <div className={`flex flex-col gap-4 font-sans ml-[46px]`}>
                                     {validOptions.map((opt: any, i: number) => {
                                       const safeOpt = String(opt || '');
                                       const optionValue = String.fromCharCode(65+i); 
                                       const isSelected = userAns === optionValue; 
                                       const isCorrectOpt = isAnswerCorrect(optionValue, correctAns);
                                       let labelClass = "flex items-start gap-3 py-1.5 px-2 rounded-none transition border border-transparent";
                                       
                                       if (isReviewMode) { 
                                          if (isCorrectOpt) labelClass += " bg-emerald-200 border-emerald-600 font-bold text-emerald-900";
                                          else if (isSelected) labelClass += " bg-red-200 border-red-600 text-red-900 line-through opacity-70"; 
                                          else labelClass += " opacity-50";
                                       } else labelClass += " cursor-pointer hover:bg-slate-100 hover:border-slate-400";
                                       
                                       return (
                                         <label key={i} className={labelClass}>
                                           <input type="radio" name={`q${q.id}`} value={optionValue} checked={isSelected} onChange={(e) => handleAnswer(String(q.id), e.target.value)} className="mt-1 w-[18px] h-[18px] accent-black shrink-0 cursor-pointer" disabled={isReviewMode} />
                                           <span className="text-[15px] leading-[1.8] text-black font-sans html-content-renderer [&>p]:!m-0 [&>p]:!inline">
                                               <span className="font-bold mr-1 font-sans">{optionValue}.</span> 
                                               <span dangerouslySetInnerHTML={{ __html: cleanHtmlContent(safeOpt) }} />
                                           </span>
                                         </label>
                                       );
                                     })}
                                   </div>

                                   {isReviewMode && (
                                      <div className="w-full mt-2 pt-4 border-t border-slate-300 ml-[46px] font-sans">
                                         <p className="text-[13px] font-black text-black uppercase mb-1">💡 Giải thích đáp án:</p>
                                         <div className="text-[15px] text-slate-800 font-medium leading-relaxed font-sans html-content-renderer" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.explanation || 'Không có lời giải thích.') }} />
                                         <div className="flex items-center gap-2 mt-3">
                                             <button onClick={() => askAIToExplain(String(q.id), q.content, q.explanation || 'Không có lời giải thích.')} className="px-4 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded-none text-[13px] transition shadow-sm border border-[#064e3b]">
                                                💬 Chat với AI
                                             </button>
                                             <button onClick={() => callTutorForQuestion(q)} className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-none text-[13px] transition shadow-sm border border-emerald-600 flex items-center gap-1">
                                                📞 Gọi Gia sư (Voice)
                                             </button>
                                         </div>
                                      </div>
                                   )}
                                 </div>
                                );
                             })}
                           </div>
                        )}

                        {/* 🚀 DẠNG BÀI DROPLIST BLOCK */}
                        {isBlockDroplist && (
                           <div className="space-y-3 bg-white p-6 sm:p-8 border border-slate-400 rounded-none font-sans">
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
                                      <div
                                          key={q.id}
                                          id={`q-${q.id}`}
                                          onClick={() => setActiveQuestionId(String(q.id))}
                                          className={`py-4 px-5 rounded-none border flex flex-col gap-4 cursor-pointer transition-all ${isReviewMode ? (isCorrect ? 'bg-emerald-50 border-emerald-600' : 'bg-red-50 border-red-600') : (activeQuestionId === String(q.id) ? 'bg-slate-50 border-black' : 'bg-white border-transparent hover:border-slate-300')}`}
                                      >
                                        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 w-full">
                                          <div className="flex items-center gap-4 flex-1 min-w-0">
                                            <span
                                                className={`shrink-0 inline-flex items-center justify-center leading-none font-bold min-w-[30px] h-[30px] text-[14px] rounded-none border font-sans ${isReviewMode ? (isCorrect ? 'bg-emerald-600 text-white border-emerald-600' : 'bg-red-600 text-white border-red-600') : (activeQuestionId === String(q.id) ? 'bg-slate-900 text-white border-black' : 'bg-white text-black border-slate-800')}`}
                                                style={{ textIndent: 0 }}
                                            >
                                                {displayIdx}
                                            </span>
                                            <div
                                                className="text-[16px] font-bold text-black leading-relaxed font-sans html-content-renderer flex-1 min-w-0 break-words [&>p]:!m-0 [&>p]:!inline"
                                                dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.content) }}
                                            />
                                          </div>

                                          <div className="shrink-0 flex items-center justify-start md:justify-end font-sans">
                                              {isReviewMode ? (
                                                 <div className="flex items-center gap-2 justify-start md:justify-end w-full">
                                                     <div className={`px-4 py-1.5 rounded-none font-bold text-[14px] border min-w-[140px] text-center ${isCorrect ? 'bg-emerald-200 text-emerald-900 border-emerald-600' : 'bg-red-200 text-red-900 border-red-600'}`}>
                                                        {userAns || '(trống)'}
                                                     </div>
                                                     {!isCorrect && (
                                                         <div className="text-[12px] font-bold text-white bg-slate-800 px-2 py-0.5 rounded-none whitespace-nowrap font-sans">
                                                             ĐA: {correctAns}
                                                         </div>
                                                     )}
                                                 </div>
                                              ) : (
                                                 <select
                                                   value={userAns}
                                                   onChange={(e) => handleAnswer(String(q.id), e.target.value)}
                                                   className="bg-transparent border-0 border-b-2 border-slate-400 text-black font-bold font-sans text-center text-[15px] h-[36px] px-2 outline-none focus:border-black cursor-pointer min-w-[140px] max-w-[250px]"
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

                                        {isReviewMode && (
                                           <div className="w-full mt-2 border-t border-slate-300 pt-3 flex-none basis-full font-sans">
                                              <p className="text-[13px] font-black text-black uppercase mb-1">💡 Giải thích đáp án:</p>
                                              <div className="text-[15px] text-slate-800 font-medium leading-relaxed font-sans html-content-renderer" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.explanation || 'Không có lời giải thích.') }} />
                                              <div className="flex items-center gap-2 mt-3">
                                                  <button onClick={() => askAIToExplain(String(q.id), q.content, q.explanation || 'Không có lời giải thích.')} className="px-4 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded-none text-[13px] transition shadow-sm border border-[#064e3b]">
                                                     💬 Chat với AI
                                                  </button>
                                                  <button onClick={() => callTutorForQuestion(q)} className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-none text-[13px] transition shadow-sm border border-emerald-600 flex items-center gap-1">
                                                     📞 Gọi Gia sư (Voice)
                                                  </button>
                                              </div>
                                           </div>
                                        )}
                                      </div>
                                    );
                                  });
                                })()}
                             </div>
                        )}

                        {/* 🚀 DẠNG BÀI DRAG AND DROP BLOCK */}
                        {(isInlineDragDrop || isBlockDragDrop) && (
                          <div className="bg-white p-8 rounded-none border border-slate-400">
                            {isInlineDragDrop ? (
                              <React.Fragment>
                                <div className={`format-passage text-[16px] text-black font-sans html-content-renderer ${isReviewMode ? 'leading-[3.0] pb-6' : 'leading-[2.0]'}`}>
                                  {renderHtmlWithHoles(cleanHtmlContent(rawContentText), sec)}
                                </div>
                                
                                {/* 🚀 THÊM BLOCK REVIEW & GỌI GIA SƯ CHO CÂU KÉO THẢ INLINE Ở ĐÂY */}
                                {isReviewMode && (
                                   <div className="w-full mt-8 border-t border-slate-300 pt-6 font-sans">
                                      <p className="text-[14px] font-black text-black uppercase mb-4 tracking-widest">💡 Giải thích chi tiết & Gia sư AI:</p>
                                      <div className="space-y-4">
                                         {(Array.isArray(sec.questions) ? sec.questions : []).map((q: any) => {
                                             if (!q?.id) return null;
                                             const qIdx = questionIndexMap[String(q.id)] || q.id;
                                             const explanationText = q.explanation || 'Không có lời giải thích.';
                                             const qContentForAI = q.content || sec.content || 'Điền từ vào chỗ trống trong đoạn văn.';
                                             
                                             return (
                                                 <div key={`expl-${q.id}`} className="bg-[#f4f4f4] p-5 border border-slate-300 rounded-none">
                                                     <div className="flex items-center gap-2 mb-2">
                                                         <span className="bg-slate-800 text-white font-bold px-2 py-0.5 text-[13px] rounded-none">Câu {qIdx}</span>
                                                     </div>
                                                     <div className="text-[15px] text-slate-800 font-medium leading-relaxed font-sans html-content-renderer" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(explanationText) }} />
                                                     
                                                     <div className="flex items-center gap-2 mt-4 pt-4 border-t border-slate-300">
                                                         <button onClick={(e) => { e.stopPropagation(); askAIToExplain(String(q.id), qContentForAI, explanationText); }} className="px-4 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded-none text-[13px] transition shadow-sm border border-[#064e3b]">
                                                            💬 Chat với AI
                                                         </button>
                                                         <button onClick={(e) => { e.stopPropagation(); callTutorForQuestion({ ...q, content: qContentForAI }); }} className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-none text-[13px] transition shadow-sm border border-emerald-600 flex items-center gap-1">
                                                            📞 Gọi Gia sư (Voice)
                                                         </button>
                                                     </div>
                                                 </div>
                                             );
                                         })}
                                      </div>
                                   </div>
                                )}
                              </React.Fragment>
                            ) : (
                              <div className="space-y-4">
                                {(() => {
                                  let allOpts: string[] = [];
                                  (sec?.questions || []).forEach((q: any) => {
                                      (q.options || []).forEach((o: any) => {
                                          const cOpt = String(o).replace(stripHtmlRegex, '').trim();
                                          if (cOpt && !allOpts.includes(cOpt)) allOpts.push(cOpt);
                                      });
                                  });

                                  return (Array.isArray(sec.questions) ? sec.questions : []).map((q: any) => {
                                    if (!q?.id) return null;
                                    const userAns = String(answers[String(q.id)] || '');
                                    const correctAns = String(q.correctAnswer || '').trim().toUpperCase();
                                    const isCorrect = isAnswerCorrect(userAns, correctAns);
                                    const displayIdx = questionIndexMap[String(q.id)] || q.id;
                                    
                                    let displayUserAns = userAns;
                                    if (userAns && /^[A-Z]$/i.test(userAns)) {
                                        const oIdx = userAns.toUpperCase().charCodeAt(0) - 65;
                                        if (allOpts[oIdx]) displayUserAns = allOpts[oIdx].replace(/^[A-Z][\.\):]\s*/i, '');
                                    } else if (userAns) {
                                        displayUserAns = userAns.replace(/^[A-Z][\.\):]\s*/i, '');
                                    }

                                    return (
                                      <div
                                          key={q.id}
                                          id={`q-${q.id}`}
                                          onClick={() => setActiveQuestionId(String(q.id))}
                                          className={`py-4 px-5 rounded-none border flex flex-col gap-4 cursor-pointer transition-all ${isReviewMode ? (isCorrect ? 'bg-emerald-50 border-emerald-600' : 'bg-red-50 border-red-600') : (activeQuestionId === String(q.id) ? 'bg-slate-50 border-black' : 'bg-white border-transparent hover:border-slate-300')}`}
                                      >
                                        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 w-full">
                                          <div className="flex items-center gap-4 flex-1 min-w-0">
                                            <span className={`shrink-0 inline-flex items-center justify-center leading-none font-bold font-sans min-w-[30px] h-[30px] text-[14px] rounded-none border ${isReviewMode ? (isCorrect ? 'bg-emerald-600 text-white border-emerald-600' : 'bg-red-600 text-white border-red-600') : (activeQuestionId === String(q.id) ? 'bg-slate-900 text-white border-black' : 'bg-white text-black border-slate-800')}`} style={{ textIndent: 0 }}>
                                              {displayIdx}
                                            </span>
                                            <div className="text-[16px] font-bold text-black leading-relaxed font-sans html-content-renderer flex-1 min-w-0 break-words [&>p]:!mb-0 [&>p]:!inline" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.content) }} />
                                          </div>

                                          <div className="shrink-0 flex items-center justify-start md:justify-end font-sans">
                                              {isReviewMode ? (
                                                 <div className="flex items-center gap-2 justify-start md:justify-end w-full">
                                                     <div className={`px-4 py-1.5 rounded-none font-bold text-[14px] font-sans border min-w-[140px] text-center ${isCorrect ? 'bg-emerald-200 text-emerald-900 border-emerald-600' : 'bg-red-200 text-red-900 border-red-600'}`}>
                                                        {displayUserAns || '(trống)'}
                                                     </div>
                                                     {!isCorrect && <div className="text-[12px] font-bold text-white bg-slate-800 px-2 py-0.5 rounded-none whitespace-nowrap font-sans">ĐA: {correctAns}</div>}
                                                 </div>
                                              ) : (
                                                <span
                                                  onDragOver={(e) => e.preventDefault()}
                                                  onDrop={() => onDrop(String(q.id))}
                                                  className={`inline-flex items-center justify-between align-middle min-w-[140px] max-w-[250px] h-[36px] border border-black rounded-none transition-all px-2 ${activeQuestionId === String(q.id) ? 'bg-slate-200' : 'bg-white'}`}
                                                >
                                                  {userAns ? (
                                                    <div className="flex items-center justify-between w-full text-black font-sans text-[14px] font-bold py-1">
                                                        <span className="truncate">{displayUserAns}</span>
                                                        <button onClick={(e) => { e.stopPropagation(); clearDragAnswer(String(q.id)); }} className="ml-2 hover:text-red-600 text-[12px] font-black font-sans">✕</button>
                                                    </div>
                                                  ) : (
                                                    <span className="text-slate-400 text-[13px] italic font-sans w-full text-center">Thả vào đây</span>
                                                  )}
                                                </span>
                                              )}
                                          </div>
                                        </div>

                                        {isReviewMode && (
                                           <div className="w-full mt-2 border-t border-slate-300 pt-3 flex-none basis-full font-sans">
                                              <p className="text-[13px] font-black text-black uppercase mb-1">💡 Giải thích đáp án:</p>
                                              <div className="text-[15px] text-slate-800 font-medium leading-relaxed font-sans html-content-renderer" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.explanation || 'Không có lời giải thích.') }} />
                                              <div className="flex items-center gap-2 mt-3">
                                                  <button onClick={() => askAIToExplain(String(q.id), q.content, q.explanation || 'Không có lời giải thích.')} className="px-4 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded-none text-[13px] transition shadow-sm border border-[#064e3b]">
                                                     💬 Chat với AI
                                                  </button>
                                                  <button onClick={() => callTutorForQuestion(q)} className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-none text-[13px] transition shadow-sm border border-emerald-600 flex items-center gap-1">
                                                     📞 Gọi Gia sư (Voice)
                                                  </button>
                                              </div>
                                           </div>
                                        )}
                                      </div>
                                    );
                                  });
                                })()}
                              </div>
                            )}

                            {!isReviewMode && (
                              <div className="mt-10 p-6 bg-[#f4f4f4] border border-slate-400 rounded-none font-sans">
                                 <p className="text-[13px] font-black text-black uppercase tracking-widest mb-4">Danh sách lựa chọn (Kéo từ đây):</p>
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
                                      
                                      const optLetter = String.fromCharCode(65 + oIdx);
                                      const isUsed = selectedInSec.includes(optLetter) || selectedInSec.includes(displayOpt.toUpperCase()) || selectedInSec.includes(opt.trim().toUpperCase());
                                      
                                      return (
                                        <div
                                          key={oIdx}
                                          draggable={!isUsed}
                                          onDragStart={(e) => onDragStart(e, displayOpt)}
                                          onDragEnd={() => {
                                            setDraggedOption(null);
                                            stopAutoScroll(); 
                                          }}
                                          className={`px-4 py-2 font-bold font-sans text-[14px] border border-black rounded-none transition-all select-none
                                            ${isUsed 
                                              ? 'bg-slate-200 text-slate-400 opacity-50 cursor-not-allowed' 
                                              : 'bg-white text-black cursor-grab hover:bg-slate-200 active:cursor-grabbing'
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
                                    
                                    let containerClass = "p-6 bg-white border rounded-none relative group transition-all flex flex-col ";
                                    if (isReviewMode) {
                                        if (isPerfect) containerClass += " border-emerald-600 bg-emerald-50";
                                        else if (isPartial) containerClass += " border-amber-600 bg-amber-50";
                                        else containerClass += " border-red-600 bg-red-50";
                                    } else {
                                        if (comboIds.includes(activeQuestionId)) containerClass += " border-black";
                                        else containerClass += " border-slate-400 hover:border-slate-600";
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
                                          <div className="flex items-start gap-4 mb-5 flex-col w-full">
                                            <div className="flex gap-2 flex-wrap shrink-0 mt-0.5">
                                               {combo.map((q: any, qIdxInCombo: number) => {
                                                   const displayIdx = questionIndexMap[String(q.id)] || q.id;
                                                   
                                                   let boxClass = "";
                                                   if (isReviewMode) {
                                                       if (isPerfect) boxClass = 'bg-emerald-600 text-white border-emerald-600';
                                                       else if (isPartial) boxClass = 'bg-amber-600 text-white border-amber-600';
                                                       else boxClass = 'bg-red-600 text-white border-red-600';
                                                   } else {
                                                       const isFilled = qIdxInCombo < userAnsArr.length;
                                                       if (activeQuestionId === String(q.id)) {
                                                           boxClass = 'bg-slate-900 text-white border-black ring-2 ring-slate-400 ring-offset-1';
                                                       } else if (isFilled) {
                                                           boxClass = 'bg-slate-800 text-white border-black';
                                                       } else {
                                                           boxClass = 'bg-white text-black border-slate-800';
                                                       }
                                                   }

                                                   return (
                                                       <span 
                                                         key={q.id} 
                                                         id={`q-${q.id}`} 
                                                         onClick={() => setActiveQuestionId(String(q.id))} 
                                                         className={`cursor-pointer shrink-0 inline-flex items-center justify-center leading-none font-bold font-sans px-2 min-w-[30px] h-[30px] text-[14px] rounded-none border transition-all ${boxClass}`}
                                                         style={{ textIndent: 0 }}
                                                       >
                                                         {displayIdx}
                                                       </span>
                                                   );
                                               })}
                                            </div>
                                            <div className="text-[16px] leading-relaxed font-bold text-black cursor-pointer w-full flex-1 min-w-0 break-words font-sans html-content-renderer [&>p]:!m-0 [&>p]:!inline" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(qText) }} />
                                          </div>

                                          <div className={`flex flex-col gap-4 ml-0 font-sans`}>
                                            {validOptions.map((opt: any, i: number) => {
                                              const safeOpt = String(opt || '').replace(/^<p>|<\/p>$/gi, '');
                                              const optionValue = String.fromCharCode(65+i); 
                                              const isSelected = userAnsArr.includes(optionValue); 
                                              let isCorrectOpt = false;
                                              correctAnsComboSet.forEach(c => {
                                                  if (isAnswerCorrect(optionValue, c)) isCorrectOpt = true;
                                              });
                                              
                                              let labelClass = "flex items-start gap-3 py-1.5 px-2 rounded-none transition border border-transparent";
                                              if (isReviewMode) { 
                                                 if (isCorrectOpt && isSelected) labelClass += " bg-emerald-200 border-emerald-600 font-bold text-emerald-900";
                                                 else if (isCorrectOpt && !isSelected) labelClass += " bg-amber-200 border-amber-600 font-bold text-amber-900";
                                                 else if (isSelected && !isCorrectOpt) labelClass += " bg-red-200 border-red-600 text-red-900 line-through opacity-70";
                                                 else labelClass += " opacity-50";
                                              } else labelClass += " cursor-pointer hover:bg-slate-100 hover:border-slate-400";
                                              
                                              return (
                                                <label key={i} className={labelClass}>
                                                  <input type="checkbox" checked={isSelected} onChange={(e) => handleComboChange(optionValue, e.target.checked)} className="mt-1 w-[18px] h-[18px] accent-black cursor-pointer rounded-none" disabled={isReviewMode} />
                                                  <span className="text-[15px] leading-[1.8] text-black font-sans html-content-renderer [&>p]:!m-0 [&>p]:!inline"><span className="font-bold mr-1 font-sans">{optionValue}.</span> <span dangerouslySetInnerHTML={{ __html: cleanHtmlContent(safeOpt) }} /></span>
                                                </label>
                                              );
                                            })}
                                          </div>

                                          {isReviewMode && (
                                            <div className="mt-6 ml-0 pt-4 border-t border-slate-300 font-sans w-full">
                                               <p className="text-[13px] font-black text-black uppercase mb-3">💡 Giải thích đáp án:</p>
                                               {combo.map((q:any) => {
                                                   if (!q.explanation || String(q.explanation).trim() === '') return null;
                                                   return (
                                                       <div key={q.id} className="text-[15px] text-slate-800 font-medium leading-relaxed mb-3 last:mb-0 font-sans html-content-renderer">
                                                           <span className="font-bold font-sans text-white px-2 py-0.5 bg-slate-800 rounded-none text-[13px] mr-2">Câu {questionIndexMap[String(q.id)] || q.id}</span>
                                                           <span dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.explanation) }} />
                                                           <div className="flex items-center gap-2 mt-3">
                                                               <button onClick={(e) => { e.stopPropagation(); askAIToExplain(String(q.id), q.content, q.explanation); }} className="px-4 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded-none text-[12px] transition shadow-sm border border-[#064e3b]">
                                                                  💬 Chat với AI
                                                               </button>
                                                               <button onClick={(e) => { e.stopPropagation(); callTutorForQuestion(q); }} className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-none text-[12px] transition shadow-sm border border-emerald-600 flex items-center gap-1">
                                                                  📞 Gọi Gia sư (Voice)
                                                               </button>
                                                           </div>
                                                       </div>
                                                   );
                                               })}
                                            </div>
                                          )}
                                        </div>
                                    );
                                });
                             })()}
                           </div>
                        )}

                      </div>
                    );
                  })}
                </div>
                
                {!showLeftColumn && (
                  <div 
                      className="w-4 absolute right-0 top-0 bottom-0 bg-[#e8e8e8] border-x border-[#c0c0c0] hover:bg-[#d4d4d4] cursor-col-resize flex flex-col justify-start items-center z-10 transition-colors shadow-sm"
                      onMouseDown={startListeningDrag}
                      onTouchStart={startListeningDrag}
                  >
                     <div className="flex flex-col gap-1.5 opacity-40 sticky top-[50vh] -mt-6">
                        <div className="w-1 h-1 bg-black"></div>
                        <div className="w-1 h-1 bg-black"></div>
                        <div className="w-1 h-1 bg-black"></div>
                        <div className="w-1 h-1 bg-black"></div>
                     </div>
                  </div>
                )}
                
              </div>
              <div className="h-[200px]" />
            </section>

          </main>

          <footer className="h-[60px] bg-white border-t border-slate-400 flex justify-between items-center px-6 shrink-0 select-none font-sans">
            
            <div className="flex items-center gap-2 h-full pr-6 border-r border-slate-400 shrink-0 min-w-max">
              <input 
                type="checkbox" 
                id="review" 
                className="w-4 h-4 cursor-pointer accent-black" 
                disabled={isReviewMode} 
                checked={!!reviewFlags[activeQuestionId]}
                onChange={() => setReviewFlags(prev => ({...prev, [activeQuestionId]: !prev[activeQuestionId]}))}
              />
              <label htmlFor="review" className="text-[14px] font-bold text-black cursor-pointer mt-0.5 whitespace-nowrap">Review</label>
            </div>
            
            <div className="flex-1 flex justify-start sm:justify-center items-center gap-1.5 overflow-x-auto px-6 py-1 custom-scrollbar min-w-0">
              {allQuestionIds.map(id => {
                let isAnswered = answers[id] && answers[id].trim() !== '';
                const isReview = reviewFlags[id];
                const isActive = activeQuestionId === id;
                
                const shapeClass = isReview ? 'rounded-full' : 'rounded-none';
                let btnClass = `w-8 h-8 flex items-center justify-center font-bold text-[13px] transition-all box-border shrink-0 ${shapeClass} `;
                
                const section = parts.reduce((acc: any[], p: any) => acc.concat(Array.isArray(p?.sections) ? p.sections : []), []).find((s:any) => {
                    if ((Array.isArray(s?.questions) ? s.questions : []).some((sq:any)=>String(sq?.id)===id)) return true;
                    if (s?.questionType === "Điền từ" || s?.questionType === "Kéo thả vào Part" || s?.questionType === "Kéo thả" || s?.questionType === "Matching" || s?.questionType === "Droplist") {
                        let combinedContent = String(s?.content || '');
                        if (Array.isArray(s?.questions)) {
                            s.questions.forEach((q: any) => combinedContent += ' ' + String(q.content || ''));
                        }
                        const matches = combinedContent.match(/\[\s*\d+\s*\]/g);
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
                             if (sec?.questionType === 'Checkbox') {
                                const c = buildCheckboxCombos(sec.questions);
                                combos.push(...c);
                             }
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
                             correctAnsSet.forEach(c => {
                                 if (isAnswerCorrect(v, c)) isMatched = true;
                             });
                             if (isMatched) pts++; 
                         });
                         
                         const idxInCombo = comboIds.indexOf(id);
                         if (idxInCombo < pts) {
                             btnClass += 'bg-emerald-200 border border-emerald-600 text-emerald-900';
                         } else {
                             btnClass += 'bg-red-200 border border-red-600 text-red-900';
                         }
                     } else {
                         btnClass += 'bg-red-200 border border-red-600 text-red-900';
                     }
                  } else {
                     let qCorrectAns = '';
                     parts.forEach((p: any) => {
                        (Array.isArray(p?.sections) ? p.sections : []).forEach((s: any) => {
                           const q = (Array.isArray(s?.questions) ? s.questions : []).find((sq: any) => String(sq?.id) === String(id));
                           if (q) {
                               qCorrectAns = String(q.correctAnswer || '');
                           }
                        });
                     });
                     
                     const isCorrect = isAnswerCorrect(answers[id], qCorrectAns) && qCorrectAns !== '';
                     btnClass += isCorrect ? 'bg-emerald-200 border border-emerald-600 text-emerald-900' : 'bg-red-200 border border-red-600 text-red-900';
                  }
                } else { 
                  if (isActive) {
                     btnClass += 'bg-slate-900 text-white border border-black shadow-inner';
                  } else if (isAnswered) {
                     btnClass += 'bg-slate-800 text-white border border-black cursor-pointer'; 
                  } else {
                     btnClass += 'bg-white border border-slate-400 text-black cursor-pointer hover:bg-slate-200'; 
                  }
                }
                
                return (
                    <button key={id} id={`nav-${id}`} onClick={() => scrollToQuestion(id)} className={btnClass}>
                        {questionIndexMap[id]}
                    </button>
                );
              })}
            </div>

            <div className="flex items-center gap-4 shrink-0 pl-6 border-l border-slate-400">
               <div className="flex items-center gap-2 hidden sm:flex">
                  <button 
                      onClick={() => {
                         const currIdx = allQuestionIds.indexOf(activeQuestionId);
                         if (currIdx > 0) scrollToQuestion(allQuestionIds[currIdx - 1]);
                      }} 
                      className="w-8 h-8 flex items-center justify-center text-black hover:bg-slate-200 border border-slate-400 bg-white rounded-none transition"
                  >
                      ←
                  </button>
                  <button 
                      onClick={() => {
                         const currIdx = allQuestionIds.indexOf(activeQuestionId);
                         if (currIdx < allQuestionIds.length - 1) scrollToQuestion(allQuestionIds[currIdx + 1]);
                      }} 
                      className="w-8 h-8 flex items-center justify-center text-black hover:bg-slate-200 border border-slate-400 bg-white rounded-none transition"
                  >
                      →
                  </button>
               </div>
               
               {isReviewMode ? (
                 <div className="flex items-center gap-2">
                     <button 
                        onClick={() => {
                          const tutorContext = {
                            overall: scoreResult.band,
                            transcript: `Bài test: ${basicInfo.title}. Điểm số: ${scoreResult.score}/${scoreResult.total} (Band ${scoreResult.band}).`,
                            feedback: "Bạn là gia sư IELTS. Học sinh vừa hoàn thành bài kiểm tra Reading/Listening và đang xem lại điểm. Hãy gửi lời chào chúc mừng/động viên dựa trên điểm số, sau đó gợi ý học sinh đọc câu hỏi mà họ không hiểu để bạn phân tích chi tiết và đưa ra lời giải thích chuyên sâu."
                          };
                          sessionStorage.setItem('tony_live_mode', 'TUTOR');
                          sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
                          sessionStorage.setItem('tony_auto_start', 'true');
                          window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
                        }}
                        className="bg-emerald-600 hover:bg-emerald-500 text-white px-4 sm:px-6 py-2 rounded-none text-[13px] sm:text-[14px] font-bold transition uppercase tracking-wide shadow-sm flex items-center gap-2"
                     >
                         📞 Gọi Gia Sư
                     </button>
                     <button onClick={handleExit} className="bg-[#064e3b] hover:bg-[#047857] text-white px-4 sm:px-6 py-2 rounded-none text-[13px] sm:text-[14px] font-bold transition uppercase tracking-wide">
                         Thoát
                     </button>
                 </div>
               ) : (
                 <button onClick={handleFinish} className="bg-slate-900 hover:bg-black text-white px-6 py-2 rounded-none text-[14px] font-bold transition ml-2 uppercase tracking-wide">
                     Nộp bài
                 </button>
               )}
            </div>

          </footer>
        </div>
      )}
    </React.Fragment>
  );
}