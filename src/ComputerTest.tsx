import React, { useState, useRef, useEffect } from 'react';
import { supabase } from './supabase';
import './tailwind.css';

const UserIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path fillRule="evenodd" d="M7.5 6a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM3.751 20.105a8.25 8.25 0 0116.498 0 .75.75 0 01-.437.695A18.683 18.683 0 0112 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 01-.437-.695z" clipRule="evenodd" /></svg>;
const SettingsIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path fillRule="evenodd" d="M11.078 2.25c-.917 0-1.699.663-1.85 1.567L9.05 4.889c-.02.12-.115.26-.297.348a7.493 7.493 0 00-.986.57c-.166.115-.334.126-.45.083L6.3 5.508a1.875 1.875 0 00-2.282.819l-.922 1.597a1.875 1.875 0 00.432 2.385l.84.692c.097.078.15.222.15.399v.111c0 .177-.053.321-.15.399l-.84.692a1.875 1.875 0 00-.432 2.385l.922 1.597a1.875 1.875 0 002.282.818l1.019-.382c.115-.043.283-.031.45.082.312.214.641.405.985.57.182.088.277.228.297.35l.178 1.071c.151.904.933 1.567 1.85 1.567h1.844c.916 0 1.699-.663 1.85-1.567l.178-1.072c.02-.12.114-.26.297-.349.344-.165.673-.356.985-.57.167-.114.335-.125.45-.082l1.02.382a1.875 1.875 0 002.28-.819l.923-1.597a1.875 1.875 0 00-.432-2.385l-.84-.692c-.098-.078-.15-.222-.15-.399v-.111c0-.177.052-.321.15-.399l.84-.692a1.875 1.875 0 00.432-2.385l-.923-1.597a1.875 1.875 0 00-2.28-.818l-1.02.382c-.114.043-.282.031-.449-.083a7.49 7.49 0 00-.985-.57c-.183-.087-.277-.227-.297-.348l-.179-1.072a1.875 1.875 0 00-1.85-1.567h-1.843zM12 15.75a3.75 3.75 0 110-7.5 3.75 3.75 0 010 7.5z" clipRule="evenodd" /></svg>;

export default function ComputerTest({ onBack, testData, onFinish }: { onBack: () => void, testData?: any, onFinish?: (res: any) => void }) {
  let safeTestData = testData;
  if (typeof safeTestData === 'string') { try { safeTestData = JSON.parse(safeTestData); } catch (e) { } }

  const contentJSON = safeTestData?.content_json || safeTestData || {};
  const basicInfo = contentJSON.basicInfo || { title: "IELTS Test", timeLimit: "40", skill: "" };
  const parts = contentJSON.parts || []; 
  
  const isListening = basicInfo.skill?.toLowerCase().includes('listening');
  const globalAudio = basicInfo.audioUrl || parts?.[0]?.audioUrl;

  const [testStarted, setTestStarted] = useState(false);
  const [isReviewMode, setIsReviewMode] = useState(false);
  const [scoreResult, setScoreResult] = useState({ score: 0, total: 0, band: "0.0" });
  
  const globalAudioRef = useRef<HTMLAudioElement>(null);
  const isFinishingRef = useRef(false);

  const [answers, setAnswers] = useState<Record<string, string>>(() => {
    try {
      const saved = localStorage.getItem(`ielts_ans_${safeTestData?.id}`);
      return saved ? JSON.parse(saved) : {};
    } catch (error) { return {}; }
  });

  const [reviewFlags, setReviewFlags] = useState<Record<string, boolean>>({});
  const [activeQuestionId, setActiveQuestionId] = useState<string>('');

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
    if (!timeStr) return 3600; const timeParts = String(timeStr).replace(/[^0-9:]/g, '').split(':');
    return timeParts.length === 2 ? parseInt(timeParts[0]) * 60 + parseInt(timeParts[1]) : (parseInt(timeParts[0]) || 60) * 60;
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
      if (safeTestData?.id) localStorage.setItem(`ielts_endtime_${safeTestData.id}`, newEndTime.toString());
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

      let score = 0; let total = 0;
      let questionTypeStats: Record<string, { correct: number, total: number }> = {};

      parts.forEach((p: any) => p.sections?.forEach((s: any) => {
        const qType = s.questionType || 'Khác';
        if (!questionTypeStats[qType]) questionTypeStats[qType] = { correct: 0, total: 0 };

        // 🚀 THUẬT TOÁN CHẤM ĐIỂM COMBO CHECKBOX ĐỘC LẬP
        if (qType === 'Checkbox') {
            const combos: any[][] = [];
            s.questions?.forEach((q: any) => {
                const rawText = String(q.content || '').replace(/<[^>]*>/g, '').trim();
                const hasRealContent = rawText !== '' || String(q.content || '').includes('<img') || String(q.content || '').includes('<audio');
                if (combos.length === 0 || hasRealContent) combos.push([q]);
                else combos[combos.length - 1].push(q);
            });

            combos.forEach(combo => {
                const comboIds = combo.map((q: any) => String(q.id));
                const userAnsComboSet = new Set(comboIds.map(id => answers[id]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase())));
                const correctAnsComboSet = new Set(combo.flatMap((q:any) => String(q.correctAnswer).split(',').map((x:string)=>x.trim().toUpperCase()).filter(Boolean)));
                
                let comboPoints = 0;
                userAnsComboSet.forEach(ans => {
                    if (correctAnsComboSet.has(ans)) comboPoints++;
                });
                comboPoints = Math.min(comboPoints, combo.length); 
                
                score += comboPoints;
                total += combo.length;
                questionTypeStats[qType].correct += comboPoints;
                questionTypeStats[qType].total += combo.length;
            });

        } else {
            s.questions?.forEach((q: any) => {
                total++;
                questionTypeStats[qType].total++;
                const userAns = String(answers[String(q.id)] || "").trim().toUpperCase();
                const correctAns = String(q.correctAnswer || "").trim().toUpperCase();
                if (userAns === correctAns && correctAns !== "") {
                   score++; questionTypeStats[qType].correct++;
                }
            });
        }
      }));

      let band = "0.0";
      if (score >= 39) band = "9.0"; else if (score >= 37) band = "8.5"; else if (score >= 35) band = "8.0"; else if (score >= 33) band = "7.5";
      else if (score >= 30) band = "7.0"; else if (score >= 27) band = "6.5"; else if (score >= 23) band = "6.0"; else if (score >= 19) band = "5.5";
      else if (score >= 15) band = "5.0"; else if (score >= 13) band = "4.5"; else if (score >= 10) band = "4.0"; else if (score >= 8) band = "3.5";
      else if (score >= 6) band = "3.0"; else if (score >= 4) band = "2.5"; else if (score >= 2) band = "2.0"; else if (score >= 1) band = "1.0";

      setScoreResult({ score, total, band }); setIsReviewMode(true); window.scrollTo({ top: 0, behavior: 'smooth' });

      try {
        const { data: { user } } = await supabase.auth.getUser();
        if (user) {
          const timeSpentSecs = parseInitialTime(basicInfo.timeLimit) - timeLeft;
          await supabase.from('test_results').insert([{
            user_id: user.id, course_id: safeTestData?.course_id || safeTestData?.content_json?.basicInfo?.courseId || null,
            test_title: basicInfo.title || safeTestData?.title || "IELTS Test", test_type: safeTestData?.test_type || 'IELTS Computer',
            score: score, total_score: total, time_spent: timeSpentSecs > 0 ? timeSpentSecs : 0,
            details: { test_id: safeTestData?.id, bandScore: band, userAnswers: answers, questionTypeStats: questionTypeStats }
          }]);
        }
      } catch (error) { console.error("Lỗi lưu kết quả thi:", error); }

    } else {
      if (onFinish) onFinish({ score: scoreResult.score, total: scoreResult.total, testTitle: basicInfo.title, bandScore: scoreResult.band }); 
      else onBack();
    }
  };

  const resetTest = () => {
    if (window.confirm("Làm lại từ đầu? Mọi đáp án sẽ bị xóa.")) { 
        if (safeTestData?.id) localStorage.removeItem(`ielts_endtime_${safeTestData.id}`);
        setAnswers({}); setReviewFlags({}); setIsReviewMode(false); setTestStarted(false); setTimeLeft(parseInitialTime(basicInfo.timeLimit)); 
    }
  };

  const [currentPartIndex, setCurrentPartIndex] = useState(0);
  const currentPart = parts[currentPartIndex];
  
  const questionToPartMap: Record<string, number> = {};
  parts.forEach((p: any, pIndex: number) => { p.sections?.forEach((s: any) => s.questions?.forEach((q: any) => { questionToPartMap[String(q.id)] = pIndex; })); });

  const scrollToQuestion = (qNum: number | string) => {
    const targetPartIndex = questionToPartMap[String(qNum)];
    setActiveQuestionId(String(qNum)); 

    if (targetPartIndex !== undefined && targetPartIndex !== currentPartIndex) {
      setCurrentPartIndex(targetPartIndex);
      setTimeout(() => {
        const el = document.getElementById(`q-${qNum}`);
        if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'center' }); el.classList.add('bg-yellow-200', 'transition-colors', 'duration-500'); setTimeout(() => el.classList.remove('bg-yellow-200'), 1500); }
      }, 150);
    } else {
      const el = document.getElementById(`q-${qNum}`);
      if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'center' }); el.classList.add('bg-yellow-200', 'transition-colors', 'duration-500'); setTimeout(() => el.classList.remove('bg-yellow-200'), 1500); }
    }
  };

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
        } else { setTimeLeft(prev => prev - 1); }
    }, 1000);
    return () => clearInterval(timer);
  }, [testStarted, isReviewMode]);

  const formatTime = (seconds: number) => { return `${Math.floor(seconds / 60).toString().padStart(2, '0')}:${(seconds % 60).toString().padStart(2, '0')}`; };

  const [highlightMenu, setHighlightMenu] = useState({ x: 0, y: 0, show: false });
  const [currentRange, setCurrentRange] = useState<Range | null>(null);
  const [stickyNote, setStickyNote] = useState({ show: false, id: '', text: '', x: 0, y: 0 });

  const handleMouseUp = () => {
    if (isReviewMode) return;
    const selection = window.getSelection();
    if (selection && selection.toString().trim().length > 0) {
      const range = selection.getRangeAt(0); const rect = range.getBoundingClientRect();
      setHighlightMenu({ x: rect.left + rect.width / 2, y: rect.top - 10, show: true }); setCurrentRange(range);
    } else { setHighlightMenu({ ...highlightMenu, show: false }); setCurrentRange(null); }
  };

  const handleCopy = async () => { if (currentRange) { await navigator.clipboard.writeText(currentRange.toString()); setHighlightMenu({ ...highlightMenu, show: false }); window.getSelection()?.removeAllRanges(); } };
  const applyHighlight = () => { if (currentRange) { const span = document.createElement('span'); span.className = 'bg-yellow-300 cursor-pointer rounded-sm'; try { currentRange.surroundContents(span); } catch (e) {} setHighlightMenu({ ...highlightMenu, show: false }); window.getSelection()?.removeAllRanges(); } };
  const initNote = () => {
    if (currentRange) {
      const noteId = 'note_' + new Date().getTime(); const span = document.createElement('span'); span.className = 'bg-yellow-300 cursor-pointer rounded-sm border-b-2 border-red-500'; span.dataset.noteId = noteId; span.dataset.noteText = '';
      try { currentRange.surroundContents(span); const rect = span.getBoundingClientRect(); setStickyNote({ show: true, id: noteId, text: '', x: rect.left, y: rect.bottom + 10 }); } catch (e) { alert("Chỉ bôi đen gọn trong 1 đoạn văn!"); }
      setHighlightMenu({ ...highlightMenu, show: false }); window.getSelection()?.removeAllRanges();
    }
  };

  const handleContentClick = (e: React.MouseEvent) => {
    const target = e.target as HTMLElement;
    if (target.tagName === 'SPAN' && target.dataset.noteId) { const rect = target.getBoundingClientRect(); setStickyNote({ show: true, id: target.dataset.noteId, text: target.dataset.noteText || '', x: rect.left, y: rect.bottom + 10 }); }
  };

  const [leftWidth, setLeftWidth] = useState(50);
  const containerRef = useRef<HTMLElement>(null);
  const isDragging = useRef(false);
  const startDrag = () => { isDragging.current = true; document.body.style.cursor = 'col-resize'; document.body.style.userSelect = 'none'; };
  const stopDrag = () => { isDragging.current = false; document.body.style.cursor = 'default'; document.body.style.userSelect = 'auto'; };
  const onDrag = (e: MouseEvent) => {
    if (!isDragging.current || !containerRef.current) return;
    const containerRect = containerRef.current.getBoundingClientRect(); const newLeftWidth = ((e.clientX - containerRect.left) / containerRect.width) * 100;
    if (newLeftWidth > 20 && newLeftWidth < 80) setLeftWidth(newLeftWidth);
  };
  useEffect(() => { window.addEventListener('mousemove', onDrag); window.addEventListener('mouseup', stopDrag); return () => { window.removeEventListener('mousemove', onDrag); window.removeEventListener('mouseup', stopDrag); }; }, []);

  const allQuestionIds: string[] = [];
  parts?.forEach((p: any) => {
    p?.sections?.forEach((s: any) => {
      s?.questions?.forEach((q: any) => {
        if (q?.id && !allQuestionIds.includes(String(q.id))) {
          allQuestionIds.push(String(q.id));
        }
      });
      if (s?.questionType === "Điền từ" || s?.questionType === "Kéo thả vào Part") {
        const matches = String(s?.content || s?.questions?.[0]?.content || '').match(/\[(\d+)\]/g);
        if (matches) {
          matches.forEach((m: string) => { 
             const num = m.replace(/\D/g, ''); 
             if (!allQuestionIds.includes(num)) allQuestionIds.push(num); 
          });
        }
      }
    });
  });
  allQuestionIds.sort((a, b) => parseInt(a) - parseInt(b));

  useEffect(() => {
     if (allQuestionIds.length > 0 && !activeQuestionId) {
         setActiveQuestionId(allQuestionIds[0]);
     }
  }, [allQuestionIds]);

  const questionIndexMap = allQuestionIds.reduce((acc: any, id: string, idx: number) => { acc[id] = idx + 1; return acc; }, {});

  // 🚀 Hàm dọn dẹp số câu hỏi lặp lại đầu dòng (VD: "20. Which TWO" -> "Which TWO")
  const getCleanQuestionText = (htmlContent: string) => {
    let txt = String(htmlContent || '').trim();
    txt = txt.replace(/^<p[^>]*>/i, '').replace(/<\/p>$/i, '').trim();
    txt = txt.replace(/^(Câu\s*\d+|\d+[\-\d]*)\s*[\.\):]?\s*/i, '').trim();
    return txt;
  };

  const renderInlineQuestion = (text: any) => {
    if (!text) return null; 
    const safeText = String(text);
    const textParts = safeText.split(/(\[\d+\])/g);
    return textParts.map((part, index) => {
      const match = part.match(/\[(\d+)\]/);
      if (match) {
        const qNum = match[1];
        const userAns = String(answers[qNum] || '');
        const displayIndex = questionIndexMap[qNum] || qNum;
        
        if (isReviewMode) {
          const qData = parts.flatMap((p: any) => p?.sections?.flatMap((s: any) => s?.questions) || []).find((q: any) => String(q?.id) === String(qNum));
          const correctAns = String(qData?.correctAnswer || '');
          const isCorrect = userAns.trim().toUpperCase() === correctAns.trim().toUpperCase();
          
          return (
            <span key={index} className="relative inline-flex items-center align-middle mx-1 -translate-y-[4px] whitespace-nowrap">
              <span className={`inline-flex items-center justify-center px-3 py-0.5 text-[14px] font-bold text-white rounded-sm shadow-sm border h-[28px] ${isCorrect ? 'bg-emerald-500 border-emerald-600' : 'bg-red-500 border-red-600'}`}>
                {displayIndex}. {userAns || '(trống)'}
              </span>
              {!isCorrect && (
                <span className="absolute top-full left-1/2 -translate-x-1/2 mt-1 text-[12px] text-emerald-800 font-bold bg-emerald-100 px-2 py-0.5 border border-emerald-300 rounded-sm shadow-sm whitespace-nowrap z-10">
                  ĐA: {correctAns}
                </span>
              )}
            </span>
          );
        }

        return (
          <span key={index} id={`q-${qNum}`} onClick={() => setActiveQuestionId(String(qNum))} className="inline-flex items-center align-middle mx-1 -translate-y-[4px] whitespace-nowrap">
            <span className={`inline-flex items-center justify-center text-white font-bold px-2 min-w-[28px] h-[28px] text-[13px] rounded-sm shadow-sm ${activeQuestionId === String(qNum) ? 'bg-[#1ea1db]' : 'bg-[#323639]'}`}>
              {displayIndex}
            </span>
            <input 
              type="text" 
              className="inline-block w-32 ml-1 border border-slate-400 focus:outline-none focus:border-[#323639] focus:ring-1 focus:ring-[#323639] bg-white text-center text-slate-800 font-bold px-2 text-[14px] h-[28px] rounded-sm shadow-inner m-0 uppercase" 
              value={userAns} 
              onFocus={() => setActiveQuestionId(String(qNum))}
              onChange={(e) => handleAnswer(qNum, e.target.value)} 
              autoComplete="new-password"
              spellCheck="false"
              autoCorrect="off"
            />
          </span>
        );
      }
      return <span key={index} dangerouslySetInnerHTML={{ __html: part }} />;
    });
  };

  const handleStartTest = () => {
    setTestStarted(true);
    let currentEndTime = getSavedEndTime();
    if (!currentEndTime) {
        const initialSeconds = parseInitialTime(basicInfo.timeLimit);
        currentEndTime = Date.now() + initialSeconds * 1000;
        if (safeTestData?.id) localStorage.setItem(`ielts_endtime_${safeTestData.id}`, currentEndTime.toString());
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
    if (globalAudioRef.current && isListening) { globalAudioRef.current.play().catch(e => { console.error("Autoplay blocked:", e); alert("Trình duyệt không cho phép tự động phát âm thanh. Vui lòng ấn nút Bắt Đầu lại."); }); }
  };
  
  const showLeftColumn = !(isListening && !isReviewMode);

  return (
    <React.Fragment>
      <style>{`
          .format-passage p { margin-bottom: 1.25rem !important; }
          .format-passage p:last-child { margin-bottom: 0 !important; }
          .format-passage br { display: block; content: ""; margin-bottom: 0.5rem; }
      `}</style>

      {isListening && globalAudio && !isReviewMode && ( <audio ref={globalAudioRef} src={globalAudio} preload="auto" className="hidden" /> )}

      {!testStarted ? (
        <div className="flex flex-col h-screen items-center justify-center bg-[#f4f5f7] font-sans">
          <div className="bg-white p-10 rounded-2xl shadow-sm text-center max-w-lg border border-slate-200 w-full">
            <div className="text-6xl mb-6">{isListening ? '🎧' : '💻'}</div>
            <h1 className="text-2xl font-black text-[#323639] mb-2">{basicInfo.title || "IELTS Test"}</h1>
            <p className="text-slate-500 mb-8 font-medium">Thời gian: {formatTime(parseInitialTime(basicInfo.timeLimit))}</p>
            {isListening && (
              <div className="bg-amber-50 border border-amber-200 p-4 rounded-lg text-amber-700 text-[13px] font-medium mb-8 text-left leading-[1.8] shadow-sm">
                <span className="font-bold">⚠️ LƯU Ý THI LISTENING:</span> File âm thanh đã được tải ngầm và sẽ <span className="font-bold underline">tự động phát ngay lập tức</span> khi bạn bấm Bắt Đầu. Bạn chỉ có thể chỉnh âm lượng, KHÔNG THỂ tạm dừng hay tua lại.
              </div>
            )}
            <div className="flex gap-4 justify-center">
              <button onClick={onBack} className="px-6 py-2.5 rounded font-bold text-slate-600 hover:bg-slate-100 border border-slate-300 transition text-[14px]">Quay lại</button>
              <button onClick={handleStartTest} className="bg-[#323639] hover:bg-[#1a1c1e] text-white font-bold px-8 py-2.5 rounded shadow-sm transition text-[14px]">Bắt Đầu Làm Bài</button>
            </div>
          </div>
        </div>
      ) : (
        <div className="flex flex-col h-screen bg-[#f4f5f7] font-sans text-slate-800 relative">
          
          {highlightMenu.show && !isReviewMode && (
            <div style={{ left: highlightMenu.x, top: highlightMenu.y, transform: 'translate(-50%, -100%)' }} className="fixed z-50 bg-white text-slate-800 rounded shadow-[0_4px_15px_rgba(0,0,0,0.15)] border border-slate-200 text-[13px] flex flex-col py-1 min-w-[130px]" onMouseDown={(e) => e.preventDefault()}>
              <button onClick={handleCopy} className="flex items-center gap-3 px-4 py-2 hover:bg-slate-100 text-left w-full"><span className="font-bold">Copy</span></button>
              <button onClick={applyHighlight} className="flex items-center gap-3 px-4 py-2 hover:bg-slate-100 text-left w-full"><span className="font-bold text-amber-600">Highlight</span></button>
              <button onClick={initNote} className="flex items-center gap-3 px-4 py-2 hover:bg-slate-100 text-left w-full"><span className="font-bold text-[#1ea1db]">Note</span></button>
            </div>
          )}

          {stickyNote.show && (
            <div style={{ left: Math.min(stickyNote.x, window.innerWidth - 300), top: stickyNote.y }} className="fixed z-50 flex flex-col shadow-xl rounded border border-slate-300 w-72">
              <div className="bg-[#fbdb65] h-7 flex justify-between items-center px-3 cursor-move border-b border-amber-200">
                 <span className="text-[11px] font-bold text-amber-800 uppercase tracking-widest">Note</span>
                 <button onClick={() => setStickyNote({...stickyNote, show: false})} className="text-amber-800 font-bold text-sm hover:scale-110 transition">✕</button>
              </div>
              <div className="bg-[#fff9dc] p-3 relative rounded-b">
                <textarea autoFocus value={stickyNote.text} onChange={(e) => setStickyNote({ ...stickyNote, text: e.target.value })} className="w-full h-32 bg-transparent outline-none resize-none text-[13px] text-slate-800 leading-relaxed custom-scrollbar" placeholder="Nhập ghi chú..." disabled={isReviewMode} />
                {!isReviewMode && (
                  <div className="flex justify-between items-center mt-2 border-t border-amber-200/50 pt-2">
                    <button onClick={() => { const span = document.querySelector(`span[data-note-id="${stickyNote.id}"]`) as HTMLElement; if (span && span.parentNode) span.parentNode.replaceChild(document.createTextNode(span.textContent || ''), span); setStickyNote({ ...stickyNote, show: false }); }} className="text-red-500 text-[12px] font-bold hover:underline">Xóa Note</button>
                    <button onClick={() => { const span = document.querySelector(`span[data-note-id="${stickyNote.id}"]`) as HTMLElement; if (span) span.dataset.noteText = stickyNote.text; setStickyNote({ ...stickyNote, show: false }); }} className="bg-amber-400 hover:bg-amber-500 text-amber-900 text-[12px] font-bold px-4 py-1.5 rounded transition">Lưu lại</button>
                  </div>
                )}
              </div>
            </div>
          )}

          <header className={`h-[46px] ${isReviewMode ? 'bg-emerald-700' : 'bg-[#323639]'} text-white flex justify-between items-center px-4 z-20 shrink-0 shadow-sm relative`}>
            <div className="flex items-center gap-2">
              <UserIcon />
              <span className="font-bold text-[14px] truncate max-w-[200px] md:max-w-xs text-slate-200">
                 {isReviewMode ? `[REVIEW] ${basicInfo.title || "IELTS"}` : (basicInfo.title || "IELTS Test")}
              </span>
            </div>
            
            {isReviewMode ? (
               <div className="absolute left-1/2 -translate-x-1/2 font-bold text-[14px] tracking-wide text-white bg-emerald-800 px-4 py-1 rounded-sm shadow-inner">
                  Điểm: {scoreResult.score}/{scoreResult.total} (Band {scoreResult.band})
               </div>
            ) : (
               <div className={`absolute left-1/2 -translate-x-1/2 font-bold text-[14px] tracking-wide ${timeLeft <= 300 ? 'text-red-400 animate-pulse' : 'text-white'}`}>
                  {formatTime(timeLeft)}
               </div>
            )}

            <div className="flex items-center gap-4 shrink-0">
               {!isReviewMode && <button onClick={clearDraft} className="text-[12px] text-slate-400 hover:text-red-300 font-bold transition mr-2">Clear Draft</button>}
               
               {isReviewMode ? (
                  <button onClick={resetTest} className="text-[12px] font-bold border border-white/40 px-3 py-1.5 rounded hover:bg-white/10 transition text-white">Retake Test</button>
               ) : (
                  <div className="flex items-center gap-5">
                     <button onClick={onBack} className="hover:text-white text-slate-300 transition text-[13px] font-bold tracking-wide">Exit</button>
                     <button className="hover:text-white text-slate-300 transition" title="Settings">
                       <SettingsIcon />
                     </button>
                  </div>
               )}
            </div>
          </header>

          {isListening && globalAudio && !isReviewMode && (
             <div className="bg-[#f0f2f5] border-b border-slate-300 px-6 py-2 flex items-center justify-center shrink-0">
               <div className="flex items-center gap-4 bg-white px-4 py-1.5 rounded-full border border-slate-300 shadow-sm" title="Chỉnh âm lượng"> 
                  <span className="text-lg text-slate-600">🔊</span> 
                  <input type="range" min="0" max="1" step="0.05" defaultValue="1" onChange={(e) => { if(globalAudioRef.current) globalAudioRef.current.volume = parseFloat(e.target.value) }} className="w-40 accent-[#323639] cursor-pointer" /> 
               </div>
             </div>
          )}

          <div className={`border-b border-slate-300 px-6 pt-2 pb-0 flex gap-4 overflow-x-auto ${isReviewMode ? 'bg-emerald-50' : 'bg-white'}`}>
            {parts.map((p: any, index: number) => {
              const isActive = currentPartIndex === index;
              return (
                <button 
                  key={index} 
                  onClick={() => setCurrentPartIndex(index)} 
                  className={`px-2 py-2 text-[14px] font-bold transition-all whitespace-nowrap border-b-[3px] ${isActive ? (isReviewMode ? 'text-emerald-700 border-emerald-600' : 'text-[#323639] border-[#323639]') : 'text-slate-500 border-transparent hover:text-slate-800'}`}
                >
                  {p.title || `Part ${index + 1}`}
                </button>
              )
            })}
          </div>

          <main className="flex flex-1 overflow-hidden relative" ref={containerRef} onMouseUp={handleMouseUp}>
            
            {showLeftColumn && (
              <>
                <section className="p-8 md:p-10 overflow-y-auto custom-scrollbar relative bg-white" style={{ width: `${leftWidth}%`, flex: 'none' }} onClick={handleContentClick}>
                  {currentPart?.content ? (
                    <div className="format-passage max-w-3xl text-[16px] leading-[1.8] text-slate-800">
                      {isReviewMode && isListening && <div className="bg-amber-50 text-amber-800 p-4 rounded-lg font-bold text-[14px] mb-6 border border-amber-200 shadow-sm">🎙️ TAPESCRIPT CHỮA BÀI NẰM Ở ĐÂY ➔</div>}
                      <div dangerouslySetInnerHTML={{ __html: currentPart?.content || "" }} />
                    </div>
                  ) : (
                    <div className="flex flex-col items-center justify-center h-full text-slate-400 opacity-70">
                       <span className="text-6xl mb-4">📄</span>
                       <p className="font-bold text-[15px]">Blank Passage</p>
                    </div>
                  )}
                  <div className="h-[200px]" />
                </section>
                
                <div className="w-3 bg-slate-100 hover:bg-slate-200 cursor-col-resize flex flex-col justify-center items-center z-10 border-x border-slate-300 transition-colors" onMouseDown={startDrag}>
                   <div className="w-[2px] h-8 bg-slate-400 rounded-full"></div>
                </div>
              </>
            )}

            <section className={`p-8 md:p-10 overflow-y-auto custom-scrollbar ${isReviewMode ? 'bg-slate-50' : 'bg-[#f4f5f7]'}`} style={{ width: showLeftColumn ? `${100 - leftWidth}%` : '100%', flex: 'none' }}>
              <div className={`${!showLeftColumn ? 'max-w-3xl mx-auto' : 'max-w-3xl'}`}>
                
                {currentPart?.audioUrl && (!isListening || isReviewMode) && (
                  <div className="mb-8 bg-white p-4 rounded border border-slate-300 shadow-sm flex items-center gap-4">
                     <p className="text-[12px] font-bold text-slate-500 uppercase tracking-widest shrink-0">Audio Part:</p>
                     <audio controls controlsList="nodownload" className="h-10 flex-1 outline-none"><source src={currentPart.audioUrl} type="audio/mpeg" /></audio>
                  </div>
                )}
                
                {currentPart?.sections?.map((sec: any, index: number) => (
                  <div key={index} className="mb-12">
                    
                    {sec.title && <h3 className="font-bold text-[17px] mb-3 text-slate-900">{sec.title}</h3>}
                    
                    {(sec.questionType === "Điền từ" || sec.questionType === "Kéo thả vào Part") && (
                      <div className={`p-8 shadow-sm rounded-sm ${isReviewMode ? 'bg-white border border-slate-300' : 'bg-white border border-slate-300'}`}>
                        {sec.content && (
                           <div className="mb-6 text-[15px] font-semibold text-slate-700 leading-relaxed bg-slate-100/50 p-4 rounded-lg border border-slate-200" dangerouslySetInnerHTML={{ __html: sec.content }} />
                        )}
                        {(() => {
                            const rawContent = sec.questions?.[0]?.content || '';
                            let mainContent = rawContent;
                            let wordBankItems: string[] = [];
                            
                            const splitKeywords = ['<br><br>Options:<br>', '<br>Options:<br>', 'Options:<br>', 'Options:'];
                            for (const keyword of splitKeywords) {
                                if (mainContent.includes(keyword)) {
                                    const parts = mainContent.split(keyword);
                                    mainContent = parts[0];
                                    wordBankItems = parts[1].split(/<br\s*\/?>/).filter((x:string) => x.trim() !== '');
                                    break;
                                }
                            }

                            return (
                                <>
                                    <div className="format-passage leading-[2.2] text-[16px] text-slate-800">
                                        {renderInlineQuestion(mainContent)}
                                    </div>
                                    {wordBankItems.length > 0 && (
                                        <div className="mt-8 p-5 bg-[#f8f9fa] border-2 border-dashed border-slate-300 rounded-xl">
                                            <p className="text-[13px] font-black text-slate-500 uppercase tracking-widest mb-4">Danh sách từ (Word Bank)</p>
                                            <div className="flex flex-wrap gap-3">
                                                {wordBankItems.map((item, idx) => {
                                                    const text = item.replace(/^<p>|<\/p>$/gi, '').trim();
                                                    return text ? (
                                                        <div key={idx} className="px-4 py-2 bg-white border border-slate-300 rounded-lg shadow-sm text-[15px] font-medium text-slate-800 min-w-[100px] flex items-center" dangerouslySetInnerHTML={{ __html: text }} />
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
                    
                    {(sec.questionType === "Trắc nghiệm" || sec.questionType === "TFNG") && (
                       <div className="space-y-6">
                         {sec.questions?.map((q: any) => {
                            if (!q?.id) return null;
                            const cleanQText = getCleanQuestionText(q.content);
                            const correctAns = String(q.correctAnswer || '').trim().toUpperCase(); 
                            const userAns = String(answers[String(q.id)] || '').trim().toUpperCase(); 
                            const isCorrect = userAns === correctAns;
                            const displayIdx = questionIndexMap[String(q.id)] || q.id;
                            
                            const validOptions = q.options?.filter((opt: any) => String(opt || '').trim() !== '') || [];
                            const isTFNG = sec.questionType === "TFNG" || validOptions.some((opt: string) => ['TRUE', 'FALSE', 'NOT GIVEN', 'YES', 'NO'].includes(opt?.trim()?.toUpperCase()));

                            if (isTFNG) {
                                return (
                                 <div key={q.id} id={`q-${q.id}`} onClick={() => setActiveQuestionId(String(q.id))} className={`p-6 rounded-sm border relative group ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-300' : 'bg-red-50/50 border-red-300') : (activeQuestionId === String(q.id) ? 'bg-white border-[#323639] shadow-md' : 'bg-white border-slate-300 shadow-sm hover:border-slate-400')} transition-all`}>
                                   <div className="flex items-start gap-4 mb-5">
                                     <span className={`inline-flex items-center justify-center font-bold min-w-[30px] h-[30px] text-[14px] rounded-sm shrink-0 mt-0.5 ${isReviewMode ? (isCorrect ? 'bg-emerald-600 text-white' : 'bg-red-600 text-white') : (activeQuestionId === String(q.id) ? 'bg-[#1ea1db] text-white' : 'bg-[#323639] text-white')}`}>
                                       {displayIdx}
                                     </span>
                                     <div className="text-[16px] leading-relaxed font-medium text-slate-800 cursor-pointer w-full" dangerouslySetInnerHTML={{ __html: cleanQText }} />
                                   </div>
                                   <div className={`flex flex-row flex-wrap gap-4 sm:gap-6 ml-11`}>
                                     {validOptions.map((opt: any, i: number) => {
                                       const safeOpt = String(opt || '');
                                       const optionValue = safeOpt.trim().toUpperCase(); 
                                       const isSelected = userAns === optionValue; 
                                       const isCorrectOpt = correctAns === optionValue;
                                       
                                       let labelClass = "flex items-center gap-2 p-2 rounded transition border border-transparent";
                                       if (isReviewMode) { 
                                          if (isCorrectOpt) labelClass += " bg-emerald-100 border-emerald-400 font-bold text-emerald-900"; 
                                          else if (isSelected) labelClass += " bg-red-100 border-red-300 text-red-700 line-through opacity-70"; 
                                          else labelClass += " opacity-50"; 
                                       } else { 
                                          labelClass += " cursor-pointer hover:bg-slate-100 hover:border-slate-300"; 
                                       }
                                       return (
                                         <label key={i} className={labelClass}>
                                           <input type="radio" name={`q${q.id}`} value={optionValue} checked={isSelected} onChange={(e) => handleAnswer(String(q.id), e.target.value)} className="w-[18px] h-[18px] accent-[#323639]" disabled={isReviewMode} />
                                           <span className="text-[15px] font-semibold text-slate-800" dangerouslySetInnerHTML={{ __html: safeOpt }} />
                                         </label>
                                       )
                                     })}
                                   </div>
                                   {isReviewMode && (<div className="mt-6 ml-11 pt-4 border-t border-slate-200"><p className="text-[13px] font-black text-amber-600 uppercase mb-1">💡 Giải thích đáp án:</p><div className="text-[15px] text-slate-700 font-medium leading-relaxed" dangerouslySetInnerHTML={{ __html: q.explanation || 'Không có lời giải thích.' }} /></div>)}
                                 </div>
                                )
                            }
                            
                            return (
                             <div key={q.id} id={`q-${q.id}`} onClick={() => setActiveQuestionId(String(q.id))} className={`p-6 rounded-sm border relative group ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-300' : 'bg-red-50/50 border-red-300') : (activeQuestionId === String(q.id) ? 'bg-white border-[#323639] shadow-md' : 'bg-white border-slate-300 shadow-sm hover:border-slate-400')} transition-all`}>
                               <div className="flex items-start gap-4 mb-5">
                                 <span className={`inline-flex items-center justify-center font-bold min-w-[30px] h-[30px] text-[14px] rounded-sm shrink-0 mt-0.5 ${isReviewMode ? (isCorrect ? 'bg-emerald-600 text-white' : 'bg-red-600 text-white') : (activeQuestionId === String(q.id) ? 'bg-[#1ea1db] text-white' : 'bg-[#323639] text-white')}`}>
                                   {displayIdx}
                                 </span>
                                 <div className="text-[16px] leading-relaxed font-medium text-slate-800 cursor-pointer w-full" dangerouslySetInnerHTML={{ __html: cleanQText }} />
                               </div>
                               <div className={`flex flex-col gap-3 ml-11`}>
                                 {validOptions.map((opt: any, i: number) => {
                                   const safeOpt = String(opt || '');
                                   const optionValue = String.fromCharCode(65+i); 
                                   const isSelected = userAns === optionValue; 
                                   const isCorrectOpt = correctAns === optionValue;
                                   
                                   let labelClass = "flex items-start gap-3 p-2.5 rounded transition border border-transparent";
                                   if (isReviewMode) { 
                                      if (isCorrectOpt) labelClass += " bg-emerald-100 border-emerald-400 font-bold text-emerald-900"; 
                                      else if (isSelected) labelClass += " bg-red-100 border-red-300 text-red-700 line-through opacity-70"; 
                                      else labelClass += " opacity-50"; 
                                   } else { 
                                      labelClass += " cursor-pointer hover:bg-slate-100 hover:border-slate-300"; 
                                   }
                                   return (
                                     <label key={i} className={labelClass}>
                                       <input type="radio" name={`q${q.id}`} value={optionValue} checked={isSelected} onChange={(e) => handleAnswer(String(q.id), e.target.value)} className="mt-1 w-[18px] h-[18px] accent-[#323639] shrink-0" disabled={isReviewMode} />
                                       <span className="text-[15px] leading-[1.8] text-slate-800"><span className="font-bold mr-1">{optionValue}.</span> <span dangerouslySetInnerHTML={{ __html: safeOpt }} /></span>
                                     </label>
                                   )
                                 })}
                               </div>
                               {isReviewMode && (<div className="mt-6 ml-11 pt-4 border-t border-slate-200"><p className="text-[13px] font-black text-amber-600 uppercase mb-1">💡 Giải thích đáp án:</p><div className="text-[15px] text-slate-700 font-medium leading-relaxed" dangerouslySetInnerHTML={{ __html: q.explanation || 'Không có lời giải thích.' }} /></div>)}
                             </div>
                            )
                         })}
                       </div>
                    )}
                    
                    {sec.questionType === "Droplist" && (
                       <div className="space-y-4">
                         {sec.questions?.map((q: any) => {
                            if (!q?.id) return null;
                            const cleanQText = getCleanQuestionText(q.content);
                            const correctAns = String(q.correctAnswer || '').trim().toUpperCase(); 
                            const userAns = String(answers[String(q.id)] || '').trim().toUpperCase(); 
                            const isCorrect = userAns === correctAns;
                            const displayIdx = questionIndexMap[String(q.id)] || q.id;
                            
                            const validOptions = q.options?.filter((opt: any) => String(opt || '').trim() !== '') || [];
                            
                            let dropOptions = validOptions.map((opt:any) => String(opt || '').trim().toUpperCase());
                            if (dropOptions.length === 0 || (dropOptions.length === 4 && dropOptions[0] === 'A' && dropOptions[1] === 'B')) {
                                dropOptions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'];
                            }

                            const otherSelectedAnswers = sec.questions
                                .filter((otherQ: any) => otherQ.id !== q.id)
                                .map((otherQ: any) => String(answers[String(otherQ.id)] || '').trim().toUpperCase())
                                .filter((ans: string) => ans !== '');

                            return (
                             <div key={q.id} id={`q-${q.id}`} onClick={() => setActiveQuestionId(String(q.id))} className={`p-5 rounded-sm border flex flex-col sm:flex-row sm:items-start gap-4 cursor-pointer ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-300' : 'bg-red-50/50 border-red-300') : (activeQuestionId === String(q.id) ? 'bg-white border-[#323639] shadow-md' : 'bg-white border-slate-300 shadow-sm hover:border-slate-400')} transition-all`}>
                               <div className="flex items-start gap-4 flex-1">
                                 <span className={`inline-flex items-center justify-center font-bold min-w-[30px] h-[30px] text-[14px] rounded-sm shrink-0 mt-0.5 ${isReviewMode ? (isCorrect ? 'bg-emerald-600 text-white' : 'bg-red-600 text-white') : (activeQuestionId === String(q.id) ? 'bg-[#1ea1db] text-white' : 'bg-[#323639] text-white')}`}>
                                   {displayIdx}
                                 </span>
                                 <div className="text-[15px] font-medium text-slate-800 leading-relaxed" dangerouslySetInnerHTML={{ __html: cleanQText }} />
                               </div>
                               <div className="shrink-0 flex items-center justify-end mt-1 sm:mt-0">
                                   {isReviewMode ? (
                                      <div className="flex items-center gap-2">
                                          <div className={`px-4 py-1.5 rounded-sm font-bold text-[14px] border ${isCorrect ? 'bg-emerald-100 text-emerald-800 border-emerald-400' : 'bg-red-100 text-red-800 border-red-300'}`}>
                                             {userAns || '(chưa chọn)'}
                                          </div>
                                          {!isCorrect && <div className="text-[12px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 border border-emerald-200 rounded-sm shadow-sm">ĐA: {correctAns}</div>}
                                      </div>
                                   ) : (
                                      <select 
                                         className="border-b-[2px] border-slate-400 bg-transparent focus:border-[#323639] rounded-none px-2 py-0.5 outline-none text-[#323639] font-bold text-[16px] min-w-[120px] max-w-[160px] cursor-pointer text-center appearance-none"
                                         style={{ textAlignLast: 'center' }}
                                         value={userAns}
                                         onChange={(e) => handleAnswer(String(q.id), e.target.value)}
                                      >
                                         <option value="" disabled className="text-gray-500 font-sans font-normal">-- Chọn --</option>
                                         {dropOptions.map((optionValue: string, i: number) => {
                                            const isDisabled = otherSelectedAnswers.includes(optionValue);
                                            return (
                                                <option key={i} value={optionValue} disabled={isDisabled} className="text-gray-800 font-sans font-bold">
                                                   {optionValue} {isDisabled ? '(Đã chọn)' : ''}
                                                </option>
                                            )
                                         })}
                                      </select>
                                   )}
                               </div>
                             </div>
                            )
                         })}
                       </div>
                    )}
                    
                    {/* 🚀 BẢN CẬP NHẬT MỚI: TỰ ĐỘNG CHIA COMBO ĐỘC LẬP TỪNG NHÓM TRONG 1 SECTION */}
                    {sec.questionType === "Checkbox" && (
                       <div className="space-y-6">
                         {(() => {
                            const combos: any[][] = [];
                            
                            sec.questions?.forEach((q: any) => {
                                // Câu có nội dung tạo Combo mới. Câu rỗng nội dung thì tự động "bám" vào Combo liền trước.
                                const rawText = String(q.content || '').replace(/<[^>]*>/g, '').trim();
                                const hasRealContent = rawText !== '' || String(q.content || '').includes('<img') || String(q.content || '').includes('<audio');
                                if (combos.length === 0 || hasRealContent) {
                                    combos.push([q]);
                                } else {
                                    combos[combos.length - 1].push(q);
                                }
                            });

                            return combos.map((combo, comboIndex) => {
                                const comboIds = combo.map((q: any) => String(q.id));
                                const maxAllowed = combo.length;
                                
                                // Thuật toán lưu đáp án phân bổ xuống từng ID để tính toán chính xác
                                const userAnsArr = Array.from(new Set(comboIds.map(id => answers[id]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase()))));
                                const correctAnsComboSet = new Set(combo.flatMap((q:any) => String(q.correctAnswer).split(',').map((x:string)=>x.trim().toUpperCase()).filter(Boolean)));
                                const validOptions = combo[0]?.options?.filter((opt: any) => String(opt || '').trim() !== '') || [];
                                
                                let comboPoints = 0;
                                userAnsArr.forEach((ans:string) => { if (correctAnsComboSet.has(ans)) comboPoints++; });
                                const isPerfect = comboPoints === maxAllowed;
                                const isPartial = comboPoints > 0 && comboPoints < maxAllowed;

                                let containerClass = "p-6 rounded-sm border relative group transition-all ";
                                if (isReviewMode) {
                                    if (isPerfect) containerClass += "bg-emerald-50/50 border-emerald-300";
                                    else if (isPartial) containerClass += "bg-amber-50/50 border-amber-300";
                                    else containerClass += "bg-red-50/50 border-red-300";
                                } else {
                                    if (comboIds.includes(activeQuestionId)) containerClass += "bg-white border-[#323639] shadow-md";
                                    else containerClass += "bg-white border-slate-300 shadow-sm hover:border-slate-400";
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
                                        // 🚀 Rải đáp án phân bổ xuống từng ID (Ví dụ: ID 20 lưu 'B', ID 21 lưu 'D')
                                        comboIds.forEach((id, idx) => {
                                            next[id] = currentSelected[idx] || ''; 
                                        }); 
                                        return next;
                                    });
                                    setActiveQuestionId(comboIds[0]);
                                };

                                const qText = getCleanQuestionText(combo[0]?.content);

                                return (
                                   <div key={`combo-${comboIndex}`} className={containerClass}>
                                     <div className="flex items-start gap-4 mb-5">
                                       <div className="flex gap-2 flex-wrap shrink-0 mt-0.5">
                                          {combo.map((q: any) => {
                                              const displayIdx = questionIndexMap[String(q.id)] || q.id;
                                              const boxClass = isReviewMode 
                                                  ? (isPerfect ? 'bg-emerald-600 text-white' : isPartial ? 'bg-amber-500 text-white' : 'bg-red-600 text-white')
                                                  : (activeQuestionId === String(q.id) ? 'bg-[#1ea1db] text-white' : 'bg-[#323639] text-white');
                                              return (
                                                  <span id={`q-${q.id}`} key={q.id} onClick={() => setActiveQuestionId(String(q.id))} className={`cursor-pointer inline-flex items-center justify-center font-bold px-2 min-w-[30px] h-[30px] text-[14px] rounded-sm shadow-sm ${boxClass}`}>
                                                    {displayIdx}
                                                  </span>
                                              );
                                          })}
                                       </div>
                                       <div className="text-[16px] leading-relaxed font-medium text-slate-800 cursor-pointer w-full" dangerouslySetInnerHTML={{ __html: qText }} />
                                     </div>

                                     <div className={`flex flex-col gap-3 ml-[3.5rem]`}>
                                       {validOptions.map((opt: any, i: number) => {
                                         const safeOpt = String(opt || '').replace(/^<p>|<\/p>$/gi, '');
                                         const optionValue = String.fromCharCode(65+i); 
                                         const isSelected = userAnsArr.includes(optionValue); 
                                         const isCorrectOpt = correctAnsComboSet.has(optionValue);
                                         
                                         let labelClass = "flex items-start gap-3 p-2.5 rounded transition border border-transparent";
                                         if (isReviewMode) { 
                                             if (isCorrectOpt && isSelected) labelClass += " bg-emerald-100 border-emerald-400 font-bold text-emerald-900"; 
                                             else if (isCorrectOpt && !isSelected) labelClass += " bg-amber-50 border-amber-300 font-bold text-amber-800"; 
                                             else if (isSelected && !isCorrectOpt) labelClass += " bg-red-100 border-red-300 text-red-700 line-through opacity-70";
                                             else labelClass += " opacity-50"; 
                                         } else { 
                                             labelClass += " cursor-pointer hover:bg-slate-100 hover:border-slate-300"; 
                                         }
                                         return (
                                           <label key={i} className={labelClass}>
                                             <input type="checkbox" checked={isSelected} onChange={(e) => handleComboChange(optionValue, e.target.checked)} className="mt-1 w-[18px] h-[18px] accent-[#323639] rounded-sm shrink-0" disabled={isReviewMode} />
                                             <span className="text-[15px] leading-[1.8] text-slate-800"><span className="font-bold mr-1">{optionValue}.</span> <span dangerouslySetInnerHTML={{ __html: safeOpt }} /></span>
                                           </label>
                                         )
                                       })}
                                     </div>

                                     {isReviewMode && (
                                       <div className="mt-6 ml-[3.5rem] pt-4 border-t border-slate-200">
                                          <p className="text-[13px] font-black text-amber-600 uppercase mb-3">💡 Giải thích đáp án:</p>
                                          {combo.map((q:any) => {
                                              if (!q.explanation || String(q.explanation).trim() === '') return null;
                                              return (
                                                  <div key={q.id} className="text-[15px] text-slate-700 font-medium leading-relaxed mb-3 last:mb-0">
                                                      <span className="font-bold text-slate-900 px-2 py-0.5 bg-slate-200 rounded text-[13px] mr-2">Câu {questionIndexMap[String(q.id)] || q.id}</span>
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
                ))}
              </div>
              <div className="h-[200px]" />
            </section>
          </main>

          <footer className="h-[60px] bg-[#f8f9fa] border-t border-slate-300 flex justify-between items-center px-6 shrink-0 select-none">
            
            <div className="flex items-center gap-2 h-full pr-6 border-r border-[#e0e6ed]">
              <input 
                type="checkbox" 
                id="review" 
                className="w-4 h-4 cursor-pointer accent-[#323639]" 
                disabled={isReviewMode} 
                checked={!!reviewFlags[activeQuestionId]}
                onChange={() => setReviewFlags(prev => ({...prev, [activeQuestionId]: !prev[activeQuestionId]}))}
              />
              <label htmlFor="review" className="text-[14px] font-bold text-slate-700 cursor-pointer mt-0.5">Review</label>
            </div>
            
            <div className="flex-1 flex justify-center items-center gap-1.5 overflow-x-auto px-6 py-1 custom-scrollbar">
              {allQuestionIds.map(id => {
                let isAnswered = answers[id] && answers[id].trim() !== '';
                const isReview = reviewFlags[id];
                const isActive = activeQuestionId === id;
                
                const shapeClass = isReview ? 'rounded-full' : 'rounded-sm';
                let btnClass = `w-8 h-8 flex items-center justify-center font-bold text-[13px] transition-all box-border shrink-0 ${shapeClass} `;
                
                const section = parts.flatMap((p: any) => p.sections || []).find((s:any) => s.questions?.some((sq:any)=>String(sq.id)===id));
                const qType = section?.questionType;

                // 🚀 CẬP NHẬT ĐIỀU HƯỚNG BÁO THIẾU ĐÁP ÁN: Học sinh tick 1 ô thì chỉ sáng 1 ô ở Footer
                if (!isReviewMode && qType === 'Checkbox') {
                    const combos: any[][] = [];
                    section.questions?.forEach((q: any) => {
                        const rawText = String(q.content || '').replace(/<[^>]*>/g, '').trim();
                        const hasRealContent = rawText !== '' || String(q.content || '').includes('<img') || String(q.content || '').includes('<audio');
                        if (combos.length === 0 || hasRealContent) combos.push([q]);
                        else combos[combos.length - 1].push(q);
                    });
                    
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
                     section.questions?.forEach((q: any) => {
                         const rawText = String(q.content || '').replace(/<[^>]*>/g, '').trim();
                         const hasRealContent = rawText !== '' || String(q.content || '').includes('<img') || String(q.content || '').includes('<audio');
                         if (combos.length === 0 || hasRealContent) combos.push([q]);
                         else combos[combos.length - 1].push(q);
                     });
                     
                     const myCombo = combos.find((c: any[]) => c.some((q:any) => String(q.id) === id)) || [];
                     if (myCombo.length > 0) {
                         const comboIds = myCombo.map((q:any) => String(q.id));
                         const userAnsSet = new Set(comboIds.map(cid => answers[cid]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase())));
                         const correctAnsSet = new Set(myCombo.flatMap((q:any)=>String(q.correctAnswer).split(',').map((x:string)=>x.trim().toUpperCase()).filter(Boolean)));
                         let pts = 0;
                         userAnsSet.forEach((v:string) => { if(correctAnsSet.has(v)) pts++; });
                         
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
                     const q = section?.questions.find((q:any) => String(q.id) === id);
                     const isCorrect = q && answers[id]?.trim().toUpperCase() === String(q.correctAnswer || '').trim().toUpperCase();
                     btnClass += isCorrect ? 'bg-emerald-100 border border-emerald-400 text-emerald-800' : 'bg-red-100 border border-red-400 text-red-800';
                  }
                } else { 
                  if (isActive) {
                     btnClass += 'bg-[#323639] text-white border border-[#323639]';
                  } else if (isAnswered) {
                     btnClass += 'bg-white border-b-[4px] border-b-[#323639] border-t border-x border-slate-300 text-slate-800 hover:bg-slate-50 cursor-pointer'; 
                  } else {
                     btnClass += 'bg-white border border-slate-300 text-slate-600 hover:bg-slate-50 cursor-pointer';
                  }
                }
                
                return (<button key={id} onClick={() => scrollToQuestion(id)} className={btnClass}>{questionIndexMap[id]}</button>)
              })}
            </div>

            <div className="flex items-center gap-4 shrink-0 pl-6 border-l border-[#e0e6ed]">
               <div className="flex items-center gap-2 hidden sm:flex">
                  <button onClick={() => {
                     const currIdx = allQuestionIds.indexOf(activeQuestionId);
                     if (currIdx > 0) scrollToQuestion(allQuestionIds[currIdx - 1]);
                  }} className="w-8 h-8 flex items-center justify-center text-slate-400 hover:text-[#323639] border border-slate-300 bg-white rounded-sm transition">←</button>
                  <button onClick={() => {
                     const currIdx = allQuestionIds.indexOf(activeQuestionId);
                     if (currIdx < allQuestionIds.length - 1) scrollToQuestion(allQuestionIds[currIdx + 1]);
                  }} className="w-8 h-8 flex items-center justify-center text-slate-400 hover:text-[#323639] border border-slate-300 bg-white rounded-sm transition">→</button>
               </div>
               {isReviewMode ? (
                 <button onClick={handleFinish} className="bg-emerald-600 hover:bg-emerald-700 text-white px-6 py-2 rounded-sm text-[14px] font-bold shadow-sm transition active:scale-95 ml-2">Thoát</button>
               ) : (
                 <button onClick={handleFinish} className="bg-[#323639] hover:bg-[#1a1c1e] text-white px-6 py-2 rounded-sm text-[14px] font-bold shadow-sm transition active:scale-95 ml-2">Nộp bài</button>
               )}
            </div>

          </footer>
        </div>
      )}
    </React.Fragment>
  );
}