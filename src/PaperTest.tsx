import React, { useState, useRef, useEffect } from 'react';
import { supabase } from './supabase';
import './tailwind.css';

export default function PaperTest({ onBack, testData, onFinish }: { onBack: () => void, testData?: any, onFinish?: (res: any) => void }) {
  let safeTestData = testData;
  if (typeof safeTestData === 'string') { try { safeTestData = JSON.parse(safeTestData); } catch (e) { } }

  const contentJSON = safeTestData?.content_json || safeTestData || {};
  const basicInfo = contentJSON.basicInfo || { title: "IELTS Paper-based", timeLimit: "60", skill: "" };
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
        const saved = localStorage.getItem(`ielts_paper_ans_${safeTestData?.id}`); 
        return saved ? JSON.parse(saved) : {};
    } catch(e) { return {}; }
  });

  useEffect(() => { 
    if (!isReviewMode && !isFinishingRef.current && safeTestData?.id) {
      localStorage.setItem(`ielts_paper_ans_${safeTestData.id}`, JSON.stringify(answers)); 
    }
  }, [answers, safeTestData?.id, isReviewMode]);

  const handleAnswer = (qNum: string, value: string) => { if (!isReviewMode) setAnswers(prev => ({ ...prev, [qNum]: value })); };
  
  const getSavedEndTime = () => {
    if (!safeTestData?.id) return null;
    const saved = localStorage.getItem(`ielts_paper_endtime_${safeTestData.id}`);
    return saved ? parseInt(saved, 10) : null;
  };

  const parseInitialTime = (timeStr: string) => {
    if (!timeStr) return 3600; const timeParts = String(timeStr).replace(/[^0-9:]/g, '').split(':');
    return timeParts.length === 2 ? parseInt(timeParts[0]) * 60 + parseInt(timeParts[1]) : (parseInt(timeParts[0]) || 60) * 60;
  };

  const [timeLeft, setTimeLeft] = useState(() => parseInitialTime(basicInfo.timeLimit));

  const clearDraft = () => { 
    if (window.confirm('Xóa toàn bộ bản nháp và làm lại từ đầu?')) { 
      if (safeTestData?.id) {
         localStorage.removeItem(`ielts_paper_ans_${safeTestData.id}`); 
         localStorage.removeItem(`ielts_paper_endtime_${safeTestData.id}`);
      }
      setAnswers({}); 
      const initialSeconds = parseInitialTime(basicInfo.timeLimit);
      const newEndTime = Date.now() + initialSeconds * 1000;
      if (safeTestData?.id) localStorage.setItem(`ielts_paper_endtime_${safeTestData.id}`, newEndTime.toString());
      setTimeLeft(initialSeconds);
    } 
  };

  const handleFinish = async () => {
    if (!isReviewMode) {
      if (!window.confirm("Bạn có chắc chắn muốn nộp bài thi?")) return;
      
      isFinishingRef.current = true;
      if (safeTestData?.id) {
         localStorage.removeItem(`ielts_paper_ans_${safeTestData.id}`);
         localStorage.removeItem(`ielts_paper_endtime_${safeTestData.id}`);
      }

      let score = 0; let total = 0;
      let questionTypeStats: Record<string, { correct: number, total: number }> = {};

      parts.forEach((p: any) => p.sections?.forEach((s: any) => {
        const qType = s.questionType || 'Khác';
        if (!questionTypeStats[qType]) questionTypeStats[qType] = { correct: 0, total: 0 };

        // 🚀 THUẬT TOÁN CHẤM ĐIỂM CHÉO COMBO CHECKBOX
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
            user_id: user.id,
            course_id: safeTestData?.course_id || safeTestData?.content_json?.basicInfo?.courseId || null,
            test_title: basicInfo.title || safeTestData?.title || "IELTS Test",
            test_type: safeTestData?.test_type || 'IELTS Paper',
            score: score,
            total_score: total,
            time_spent: timeSpentSecs > 0 ? timeSpentSecs : 0,
            details: { 
              test_id: safeTestData?.id,
              bandScore: band, 
              userAnswers: answers,
              questionTypeStats: questionTypeStats 
            }
          }]);
        }
      } catch (error) {
        console.error("Lỗi lưu kết quả thi:", error);
      }

    } else {
      if (onFinish) onFinish({ score: scoreResult.score, total: scoreResult.total, testTitle: basicInfo.title, bandScore: scoreResult.band }); else onBack();
    }
  };

  const resetTest = () => { 
    if (window.confirm("Làm lại từ đầu? Mọi đáp án sẽ bị xóa.")) { 
      if (safeTestData?.id) localStorage.removeItem(`ielts_paper_endtime_${safeTestData.id}`);
      setAnswers({}); setIsReviewMode(false); setTestStarted(false); setTimeLeft(parseInitialTime(basicInfo.timeLimit)); 
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

  const scrollToQuestion = (qNum: number | string) => {
    const element = document.getElementById(`q-${qNum}`);
    if (element) { element.scrollIntoView({ behavior: 'smooth', block: 'center' }); element.classList.add('bg-blue-100', 'transition-colors', 'duration-500'); setTimeout(() => element.classList.remove('bg-blue-100'), 1500); }
  };

  const [highlightMenu, setHighlightMenu] = useState({ x: 0, y: 0, show: false });
  const [currentRange, setCurrentRange] = useState<Range | null>(null);
  const [stickyNote, setStickyNote] = useState({ show: false, id: '', text: '', x: 0, y: 0 });

  const handleMouseUp = () => {
    if (isReviewMode) return;
    const selection = window.getSelection();
    if (selection && selection.toString().trim().length > 0) {
      const range = selection.getRangeAt(0); const rect = range.getBoundingClientRect(); setHighlightMenu({ x: rect.left + rect.width / 2, y: rect.top - 10, show: true }); setCurrentRange(range);
    } else { setHighlightMenu({ ...highlightMenu, show: false }); setCurrentRange(null); }
  };

  const handleCopy = async () => { if (currentRange) { await navigator.clipboard.writeText(currentRange.toString()); setHighlightMenu({ ...highlightMenu, show: false }); window.getSelection()?.removeAllRanges(); } };
  const applyHighlight = () => { if (currentRange) { const span = document.createElement('span'); span.className = 'bg-yellow-300 cursor-pointer rounded-sm'; try { currentRange.surroundContents(span); } catch (e) {} setHighlightMenu({ ...highlightMenu, show: false }); window.getSelection()?.removeAllRanges(); } };
  const initNote = () => {
    if (currentRange) {
      const noteId = 'note_' + new Date().getTime(); const span = document.createElement('span'); span.className = 'bg-yellow-300 cursor-pointer rounded-sm border-b-2 border-red-500'; span.dataset.noteId = noteId; span.dataset.noteText = '';
      try { currentRange.surroundContents(span); const rect = span.getBoundingClientRect(); setStickyNote({ show: true, id: noteId, text: '', x: rect.left, y: rect.bottom + 10 }); } catch (e) { alert("Lưu ý: Chỉ bôi đen gọn trong 1 đoạn văn nhé!"); }
      setHighlightMenu({ ...highlightMenu, show: false }); window.getSelection()?.removeAllRanges();
    }
  };

  const handleContentClick = (e: React.MouseEvent) => {
    const target = e.target as HTMLElement;
    if (target.tagName === 'SPAN' && target.dataset.noteId) { const rect = target.getBoundingClientRect(); setStickyNote({ show: true, id: target.dataset.noteId, text: target.dataset.noteText || '', x: rect.left, y: rect.bottom + 10 }); }
  };

  // 🚀 LẤY TOÀN BỘ ID CÂU HỎI VÀ ĐẢM BẢO SORT CHUẨN ĐỂ FIX SỐ LỘN XỘN
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

  const questionIndexMap = allQuestionIds.reduce((acc: any, id: string, idx: number) => { 
    acc[id] = idx + 1; 
    return acc; 
  }, {});

  // 🚀 HÀM DỌN RÁC HTML THỪA VÀ SỐ ĐẾM ĐẦU CÂU HỎI
  const getCleanQuestionText = (htmlContent: string) => {
    let txt = String(htmlContent || '').trim();
    txt = txt.replace(/^<p[^>]*>/i, '').replace(/<\/p>$/i, '').trim();
    // Xóa số thứ tự đầu câu (VD: "14.", "Câu 14:") bất chấp việc bị bọc trong thẻ b/strong
    txt = txt.replace(/^(<[^>]+>)*(Câu\s*\d+|\d+[\-\d]*)\s*[\.\):]?\s*(<\/[^>]+>)*\s*/i, '').trim();
    return txt;
  };

  // 🚀 HÀM DỌN RÁC OPTIONS ĐÁP ÁN (Tránh lặp lại A. A. Đáp án)
  const getCleanOptionText = (opt: string, index: number) => {
    let cleanOpt = String(opt || '').replace(/^<p[^>]*>/i, '').replace(/<\/p>$/i, '').trim();
    const expectedLetter = String.fromCharCode(65 + index);
    const match = cleanOpt.match(/^(<[^>]+>)*([a-zA-Z])([\.\):]?)\s*(<\/[^>]+>)*\s*([\s\S]*)/i);
    // Xóa tiền tố "A." hoặc "B)" nếu nó trùng khớp với thứ tự chuẩn của Option
    if (match && match[2].toUpperCase() === expectedLetter) {
        if (match[3] !== '' || match[5] === '') return match[5].trim();
    }
    return cleanOpt;
  };

  const renderInlineQuestion = (text: string) => {
    if (!text) return null;
    const partsText = text.split(/(\[\d+\])/g);
    return partsText.map((part, index) => {
      const match = part.match(/\[(\d+)\]/);
      if (match) {
        const qNum = match[1];
        const userAns = answers[qNum] || '';
        const displayIndex = questionIndexMap[qNum] || qNum;
        
        if (isReviewMode) {
          const qData = parts.flatMap((p: any) => p.sections?.flatMap((s: any) => s.questions) || []).find((q: any) => String(q.id) === String(qNum));
          const correctAns = qData?.correctAnswer || '';
          const isCorrect = userAns.trim().toUpperCase() === correctAns.trim().toUpperCase();
          
          return (
            <span key={index} className="relative inline-flex flex-col items-center mx-1 align-baseline">
              <span className={`px-2.5 py-0.5 text-[14px] font-bold text-white rounded shadow-sm border ${isCorrect ? 'bg-emerald-500 border-emerald-600' : 'bg-red-500 border-red-600'}`}>
                {displayIndex}. {userAns || '(trống)'}
              </span>
              {!isCorrect && (
                <span className="absolute top-full left-1/2 -translate-x-1/2 mt-1 text-[11px] text-emerald-800 font-bold bg-emerald-100 px-2 py-0.5 border border-emerald-300 rounded text-center whitespace-nowrap z-10 shadow-md">
                  ĐA: {correctAns}
                </span>
              )}
            </span>
          );
        }

        return (
          <span key={index} id={`q-${qNum}`} className="inline-flex items-baseline mx-1">
            <span className="font-bold text-[15px] mr-1 text-slate-700">{displayIndex}.</span>
            <input 
              type="text" 
              className="w-32 border-b-2 border-slate-400 focus:outline-none focus:border-blue-600 bg-transparent text-center text-blue-800 font-bold px-1 text-[15px] leading-tight pb-0.5 uppercase" 
              value={userAns} 
              onChange={(e) => handleAnswer(qNum, e.target.value)} 
              autoComplete="off" 
              spellCheck="false"
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
    if (globalAudioRef.current && isListening) { globalAudioRef.current.play().catch(e => { console.error("Autoplay blocked:", e); alert("Trình duyệt chặn phát âm thanh. Vui lòng bấm Bắt Đầu lại."); }); }
  };

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
              <span className="font-bold">⚠️ LƯU Ý THI LISTENING:</span> File âm thanh sẽ <span className="font-bold underline">tự động phát</span> ngay khi bạn bấm nút Bắt Đầu bên dưới. <br/><br/>Bạn chỉ có thể chỉnh âm lượng (Volume), KHÔNG THỂ tạm dừng hay tua lại.
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

  return (
    <div className="flex flex-col h-screen bg-[#f3f4f6] font-serif text-gray-900 relative">
      
      {isListening && globalAudio && !isReviewMode && ( <audio ref={globalAudioRef} src={globalAudio} preload="auto" className="hidden" /> )}

      {highlightMenu.show && !isReviewMode && (
        <div style={{ left: highlightMenu.x, top: highlightMenu.y, transform: 'translate(-50%, -100%)' }} className="fixed z-50 bg-white font-sans text-gray-800 rounded shadow-[0_4px_15px_rgba(0,0,0,0.15)] border border-gray-200 text-sm flex flex-col py-1 min-w-[130px]" onMouseDown={(e) => e.preventDefault()}>
          <button onClick={handleCopy} className="flex items-center gap-3 px-4 py-2 hover:bg-gray-100 text-left w-full"><span className="font-medium">Copy</span></button>
          <button onClick={applyHighlight} className="flex items-center gap-3 px-4 py-2 hover:bg-gray-100 text-left w-full"><span className="font-medium text-yellow-600">Highlight</span></button>
          <button onClick={initNote} className="flex items-center gap-3 px-4 py-2 hover:bg-gray-100 text-left w-full"><span className="font-medium text-blue-600">Note</span></button>
        </div>
      )}

      {stickyNote.show && (
        <div style={{ left: Math.min(stickyNote.x, window.innerWidth - 300), top: stickyNote.y }} className="fixed z-50 flex flex-col shadow-2xl rounded border border-gray-300 w-72 font-sans">
          <div className="bg-[#4aa0e6] h-6 flex justify-between items-center px-2 cursor-move"><button onClick={() => setStickyNote({...stickyNote, show: false})} className="text-white text-xs">✕</button></div>
          <div className="bg-[#f8f5dc] p-3 relative">
            <textarea autoFocus value={stickyNote.text} onChange={(e) => setStickyNote({ ...stickyNote, text: e.target.value })} className="w-full h-32 bg-transparent outline-none resize-none text-sm" placeholder="Nhập ghi chú..." disabled={isReviewMode} />
            {!isReviewMode && (
              <div className="flex justify-between items-center mt-2 border-t border-gray-300/50 pt-2"><button onClick={() => { const span = document.querySelector(`span[data-note-id="${stickyNote.id}"]`) as HTMLElement; if (span && span.parentNode) span.parentNode.replaceChild(document.createTextNode(span.textContent || ''), span); setStickyNote({ ...stickyNote, show: false }); }} className="text-red-500 text-xs font-bold underline">Xóa Note</button><button onClick={() => { const span = document.querySelector(`span[data-note-id="${stickyNote.id}"]`) as HTMLElement; if (span) span.dataset.noteText = stickyNote.text; setStickyNote({ ...stickyNote, show: false }); }} className="bg-[#3b82f6] text-white text-xs font-bold px-4 py-1.5 rounded">Lưu</button></div>
            )}
          </div>
        </div>
      )}

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
          <div className={`font-mono text-xl px-4 py-1 rounded-md shadow-inner tracking-wider font-bold ${isReviewMode ? 'bg-emerald-600 text-white' : 'bg-gray-800 text-white'}`}>{isReviewMode ? `Band ${scoreResult.band}` : formatTime(timeLeft)}</div>
        </div>
      </header>

      <main className="flex-1 overflow-y-auto p-8 relative" onMouseUp={handleMouseUp}>
        <div className="max-w-7xl mx-auto space-y-12" onClick={handleContentClick}>
          
          {parts.map((part: any, pIndex: number) => {
            const hasPassage = part.content && part.content.trim().length > 0;
            const showTwoColumns = hasPassage || (isListening && isReviewMode && part.content); 

            return (
              <div key={pIndex} className="bg-white p-8 md:p-12 shadow-sm border border-gray-200">
                
                <div className="text-center mb-8 border-b-2 border-gray-800 pb-4">
                  <h2 className="font-bold text-2xl uppercase tracking-widest text-gray-800 font-sans">{part.title}</h2>
                </div>

                <div className={`grid ${showTwoColumns ? 'lg:grid-cols-2 gap-12' : 'grid-cols-1 max-w-3xl mx-auto'}`}>
                  
                  {showTwoColumns && (
                    <div className="text-justify leading-loose text-[15px] border-r border-gray-200 pr-8">
                      {isReviewMode && isListening && <div className="bg-amber-100 text-amber-800 p-2 rounded font-bold text-xs mb-4 border border-amber-300 inline-block font-sans shadow-sm">🎙️ TAPESCRIPT</div>}
                      <div dangerouslySetInnerHTML={{ __html: part.content }} className="space-y-4" />
                    </div>
                  )}

                  <div className={`${showTwoColumns ? 'pl-4' : ''}`}>
                    {part.sections?.map((sec: any, sIndex: number) => {
                      // 🚀 ĐỒNG BỘ TIÊU ĐỀ SECTION: Tự động đổi "Questions X-Y" theo index thực tế
                      let displaySecTitle = sec.title;
                      let firstIdx = null, lastIdx = null;
                      if (sec.questionType === "Điền từ" || sec.questionType === "Kéo thả vào Part") {
                          const matches = Array.from(String(sec.content || sec.questions?.[0]?.content || '').matchAll(/\[(\d+)\]/g));
                          if (matches.length > 0) {
                              firstIdx = questionIndexMap[matches[0][1]];
                              lastIdx = questionIndexMap[matches[matches.length - 1][1]];
                          }
                      } else if (sec.questions?.length > 0) {
                          firstIdx = questionIndexMap[sec.questions[0].id];
                          lastIdx = questionIndexMap[sec.questions[sec.questions.length - 1].id];
                      }
                      
                      if (firstIdx && lastIdx && /Questions?\s+\d+/i.test(sec.title)) {
                          displaySecTitle = sec.title.replace(/Questions?\s+\d+(-\d+)?/i, firstIdx === lastIdx ? `Question ${firstIdx}` : `Questions ${firstIdx}-${lastIdx}`);
                      }

                      return (
                        <div key={sIndex} className="mb-10 font-sans">
                          
                          {sec.title && (
                            <div className="bg-gray-100 border border-gray-300 px-4 py-2 mb-4">
                              <h4 className="font-bold text-gray-800">{displaySecTitle}</h4>
                            </div>
                          )}

                          {(sec.questionType === "Điền từ" || sec.questionType === "Kéo thả vào Part") && (
                            <div className={`border p-8 rounded-xl shadow-sm ${isReviewMode ? 'border-slate-300' : 'border-gray-200'}`}>
                              <div className="space-y-6 leading-[2.5] text-[15px] font-serif text-slate-800">
                                {renderInlineQuestion(sec.content)}
                              </div>
                            </div>
                          )}

                          {(sec.questionType === "Trắc nghiệm" || sec.questionType === "TFNG") && (
                            <div className="space-y-6">
                              {sec.questions?.map((q: any) => {
                                const cleanQText = getCleanQuestionText(q.content);
                                const correctAns = String(q.correctAnswer || '').trim().toUpperCase(); 
                                const userAns = String(answers[String(q.id)] || '').trim().toUpperCase(); 
                                const isCorrect = userAns === correctAns;
                                const displayIndex = questionIndexMap[q.id] || q.id;
                                
                                const isTFNG = sec.questionType === "TFNG" || q.options?.some((opt: string) => ['TRUE', 'FALSE', 'NOT GIVEN', 'YES', 'NO'].includes(opt?.trim()?.toUpperCase()));

                                // Dàn hàng ngang cho TFNG
                                if (isTFNG) {
                                   return (
                                      <div key={q.id} id={`q-${q.id}`} className={`p-6 rounded-xl border shadow-sm ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-200' : 'bg-red-50/50 border-red-200') : 'border-gray-200'}`}>
                                        <div className="flex gap-4 mb-2">
                                          <span className="font-bold text-gray-800 shrink-0 w-6 text-right pt-[2px]">{displayIndex}.</span>
                                          <div className="flex-1">
                                            {isReviewMode && (<div className="mb-3">{isCorrect ? <span className="text-[11px] font-bold bg-emerald-100 text-emerald-700 px-3 py-1 rounded">✅ ĐÚNG</span> : <span className="text-[11px] font-bold bg-red-100 text-red-700 px-3 py-1 rounded">❌ SAI</span>}</div>)}
                                            {cleanQText && <div className="text-[16px] mb-4 font-serif leading-relaxed" dangerouslySetInnerHTML={{ __html: cleanQText }} />}
                                            <div className={`flex flex-row flex-wrap gap-4`}>
                                              {q.options?.map((opt: string, i: number) => {
                                                const safeOpt = String(opt || '').replace(/^<p[^>]*>/i, '').replace(/<\/p>$/i, '').trim();
                                                const optionValue = safeOpt.replace(/<[^>]*>/g, '').toUpperCase(); 
                                                const isSelected = userAns === optionValue; 
                                                const isCorrectOpt = correctAns === optionValue;
                                                let labelClass = "flex items-center gap-2 p-1.5 transition";
                                                
                                                if (isReviewMode) { 
                                                  if (isCorrectOpt) labelClass += " font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 rounded"; 
                                                  else if (isSelected) labelClass += " text-red-500 line-through opacity-70 bg-red-50 rounded"; 
                                                  else labelClass += " opacity-50"; 
                                                } else { labelClass += " cursor-pointer group hover:text-blue-600"; }
                                                return (
                                                  <label key={i} className={labelClass}>
                                                    <input type="radio" name={`q${q.id}`} value={optionValue} checked={isSelected} onChange={(e) => handleAnswer(String(q.id), e.target.value)} className="w-4 h-4 accent-blue-600 cursor-pointer" disabled={isReviewMode} />
                                                    <span className="text-[15px] font-serif leading-relaxed font-semibold" dangerouslySetInnerHTML={{ __html: safeOpt }} />
                                                  </label>
                                                );
                                              })}
                                            </div>
                                            {isReviewMode && (<div className="mt-6 pt-4 border-t border-slate-200"><p className="text-[12px] font-black text-amber-600 uppercase mb-2">💡 Giải thích đáp án:</p><div className="text-[14px] text-slate-700 italic" dangerouslySetInnerHTML={{ __html: q.explanation || "Không có lời giải thích." }} /></div>)}
                                          </div>
                                        </div>
                                      </div>
                                   );
                                }

                                // Layout dọc thông thường cho Multiple Choice
                                return (
                                  <div key={q.id} id={`q-${q.id}`} className={`p-6 rounded-xl border shadow-sm ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-200' : 'bg-red-50/50 border-red-200') : 'border-gray-200'}`}>
                                    <div className="flex gap-4 mb-4">
                                      <span className="font-bold text-gray-800 shrink-0 w-6 text-right pt-[2px]">{displayIndex}.</span>
                                      <div className="flex-1">
                                        {isReviewMode && (<div className="mb-3">{isCorrect ? <span className="text-[11px] font-bold bg-emerald-100 text-emerald-700 px-3 py-1 rounded">✅ ĐÚNG</span> : <span className="text-[11px] font-bold bg-red-100 text-red-700 px-3 py-1 rounded">❌ SAI</span>}</div>)}
                                        {cleanQText && <div className="text-[16px] mb-4 font-serif leading-relaxed" dangerouslySetInnerHTML={{ __html: cleanQText }} />}
                                        <div className={`flex flex-col gap-2`}>
                                          {q.options?.map((opt: string, i: number) => {
                                            const cleanOpt = getCleanOptionText(opt, i);
                                            const optionValue = String.fromCharCode(65+i); 
                                            const isSelected = userAns === optionValue; 
                                            const isCorrectOpt = correctAns === optionValue;
                                            let labelClass = "flex items-start gap-3 p-1.5 transition";
                                            
                                            if (isReviewMode) { 
                                              if (isCorrectOpt) labelClass += " font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 rounded"; 
                                              else if (isSelected) labelClass += " text-red-500 line-through opacity-70 bg-red-50 rounded"; 
                                              else labelClass += " opacity-50"; 
                                            } else { labelClass += " cursor-pointer group hover:text-blue-600"; }
                                            return (
                                              <label key={i} className={labelClass}>
                                                <input type="radio" name={`q${q.id}`} value={optionValue} checked={isSelected} onChange={(e) => handleAnswer(String(q.id), e.target.value)} className="mt-1 accent-blue-600 cursor-pointer shrink-0" disabled={isReviewMode} />
                                                <span className="text-[15px] font-serif leading-relaxed"><span className="font-bold mr-1">{optionValue}.</span> <span dangerouslySetInnerHTML={{ __html: cleanOpt }} /></span>
                                              </label>
                                            );
                                          })}
                                        </div>
                                        {isReviewMode && (<div className="mt-6 pt-4 border-t border-slate-200"><p className="text-[12px] font-black text-amber-600 uppercase mb-2">💡 Giải thích đáp án:</p><div className="text-[14px] text-slate-700 italic" dangerouslySetInnerHTML={{ __html: q.explanation || "Không có lời giải thích." }} /></div>)}
                                      </div>
                                    </div>
                                  </div>
                                );
                              })}
                            </div>
                          )}

                          {sec.questionType === "Droplist" && (
                            <div className="space-y-4">
                              {sec.questions?.map((q: any) => {
                                const cleanQText = getCleanQuestionText(q.content);
                                const correctAns = String(q.correctAnswer || '').trim().toUpperCase(); 
                                const userAns = String(answers[String(q.id)] || '').trim().toUpperCase(); 
                                const isCorrect = userAns === correctAns;
                                const displayIndex = questionIndexMap[q.id] || q.id;
                                
                                const otherSelectedAnswers = sec.questions
                                    .filter((otherQ: any) => otherQ.id !== q.id)
                                    .map((otherQ: any) => String(answers[String(otherQ.id)] || '').trim().toUpperCase())
                                    .filter((ans: string) => ans !== '');

                                return (
                                  <div key={q.id} id={`q-${q.id}`} className={`p-5 rounded-xl border flex flex-col sm:flex-row sm:items-center gap-4 shadow-sm ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-200' : 'bg-red-50/50 border-red-200') : 'border-gray-200 bg-white'}`}>
                                    <div className="flex items-center gap-3 flex-1">
                                      <span className="font-bold text-gray-800 shrink-0">{displayIndex}.</span>
                                      <div className="text-[15px] font-serif text-slate-800 line-clamp-2" dangerouslySetInnerHTML={{ __html: cleanQText }} />
                                    </div>
                                    <div className="shrink-0 flex items-center justify-end">
                                        {isReviewMode ? (
                                           <div className="flex items-center gap-2">
                                               <div className={`px-4 py-1.5 rounded font-bold text-[14px] border ${isCorrect ? 'bg-emerald-100 text-emerald-800 border-emerald-300' : 'bg-red-100 text-red-800 border-red-300'}`}>
                                                  {userAns || '(chưa chọn)'}
                                               </div>
                                               {!isCorrect && <div className="text-[12px] font-bold text-emerald-700">Đúng: {correctAns}</div>}
                                           </div>
                                        ) : (
                                           <select 
                                              className="border-b-2 border-slate-400 bg-transparent focus:border-blue-600 rounded-none px-3 py-1 outline-none text-blue-800 font-serif font-medium text-[15px] min-w-[150px] cursor-pointer text-center"
                                              style={{ textAlignLast: 'center' }}
                                              value={userAns}
                                              onChange={(e) => handleAnswer(String(q.id), e.target.value)}
                                           >
                                              <option value="" disabled className="text-gray-500 font-sans">-- Chọn --</option>
                                              {q.options?.map((opt: any, i: number) => {
                                                 const optionValue = String(opt || '').replace(/<[^>]*>/g, '').trim().toUpperCase();
                                                 const isDisabled = otherSelectedAnswers.includes(optionValue);
                                                 return (
                                                     <option key={i} value={optionValue} disabled={isDisabled} className="text-gray-800 font-sans">
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

                          {/* 🚀 ĐÃ BỔ SUNG: ÁP DỤNG THUẬT TOÁN COMBO CHECKBOX VÀO PAPER TEST */}
                          {sec.questionType === "Checkbox" && (
                            <div className="space-y-6">
                              {(() => {
                                  const combos: any[][] = [];
                                  sec.questions?.forEach((q: any) => {
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
                                      
                                      const userAnsArr = Array.from(new Set(comboIds.map(id => answers[id]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase()))));
                                      const correctAnsComboSet = new Set(combo.flatMap((q:any) => String(q.correctAnswer).split(',').map((x:string)=>x.trim().toUpperCase()).filter(Boolean)));
                                      const validOptions = combo[0]?.options?.filter((opt: any) => String(opt || '').trim() !== '') || [];
                                      
                                      let comboPoints = 0;
                                      userAnsArr.forEach((ans:string) => { if (correctAnsComboSet.has(ans)) comboPoints++; });
                                      const isPerfect = comboPoints === maxAllowed;
                                      const isPartial = comboPoints > 0 && comboPoints < maxAllowed;

                                      let containerClass = "p-6 rounded-xl border shadow-sm transition-all ";
                                      if (isReviewMode) {
                                          if (isPerfect) containerClass += "bg-emerald-50/50 border-emerald-200";
                                          else if (isPartial) containerClass += "bg-amber-50/50 border-amber-200";
                                          else containerClass += "bg-red-50/50 border-red-200";
                                      } else {
                                          containerClass += "bg-white border-gray-200 hover:border-blue-300";
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
                                      };

                                      const qText = getCleanQuestionText(combo[0]?.content);
                                      const firstQIdx = questionIndexMap[comboIds[0]] || comboIds[0];
                                      const lastQIdx = questionIndexMap[comboIds[comboIds.length - 1]] || comboIds[comboIds.length - 1];
                                      const displayIndexText = comboIds.length > 1 ? `${firstQIdx}-${lastQIdx}` : firstQIdx;

                                      return (
                                         <div key={`combo-${comboIndex}`} id={`q-${combo[0].id}`} className={containerClass}>
                                           <div className="flex gap-4 mb-4">
                                             <div className="flex flex-col gap-1 shrink-0 w-8 md:w-10 text-right pt-[2px]">
                                                <span className="font-bold text-gray-800">{displayIndexText}.</span>
                                             </div>
                                             <div className="flex-1 w-full">
                                               {isReviewMode && (
                                                 <div className="mb-3">
                                                     {isPerfect ? <span className="text-[11px] font-bold bg-emerald-100 text-emerald-700 px-3 py-1 rounded">✅ ĐÚNG (ĐỦ ĐIỂM)</span> 
                                                     : isPartial ? <span className="text-[11px] font-bold bg-amber-100 text-amber-700 px-3 py-1 rounded">⚠️ ĐÚNG 1 PHẦN</span>
                                                     : <span className="text-[11px] font-bold bg-red-100 text-red-700 px-3 py-1 rounded">❌ SAI TOÀN BỘ</span>}
                                                 </div>
                                               )}

                                               {qText && <div className="text-[16px] mb-4 font-serif leading-relaxed text-slate-800" dangerouslySetInnerHTML={{ __html: qText }} />}

                                               <div className={`flex flex-col gap-2`}>
                                                 {validOptions.map((opt: any, i: number) => {
                                                   const cleanOpt = getCleanOptionText(opt, i);
                                                   const optionValue = String.fromCharCode(65+i); 
                                                   const isSelected = userAnsArr.includes(optionValue); 
                                                   const isCorrectOpt = correctAnsComboSet.has(optionValue);
                                                   
                                                   let labelClass = "flex items-start gap-3 p-1.5 rounded transition";
                                                   if (isReviewMode) { 
                                                       if (isCorrectOpt && isSelected) labelClass += " font-bold text-emerald-700 bg-emerald-50 border border-emerald-200"; 
                                                       else if (isCorrectOpt && !isSelected) labelClass += " font-bold text-amber-700 bg-amber-50 border border-amber-200"; 
                                                       else if (isSelected && !isCorrectOpt) labelClass += " text-red-500 line-through opacity-70 bg-red-50";
                                                       else labelClass += " opacity-50"; 
                                                   } else { 
                                                       labelClass += " cursor-pointer hover:bg-gray-50 hover:text-blue-600"; 
                                                   }
                                                   return (
                                                     <label key={i} className={labelClass}>
                                                       <input type="checkbox" checked={isSelected} onChange={(e) => handleComboChange(optionValue, e.target.checked)} className="mt-1 w-4 h-4 accent-blue-600 rounded-sm shrink-0 cursor-pointer" disabled={isReviewMode} />
                                                       <span className="text-[15px] font-serif leading-relaxed text-slate-800"><span className="font-bold mr-1">{optionValue}.</span> <span dangerouslySetInnerHTML={{ __html: cleanOpt }} /></span>
                                                     </label>
                                                   )
                                                 })}
                                               </div>

                                               {isReviewMode && (
                                                 <div className="mt-6 pt-4 border-t border-slate-200">
                                                    <p className="text-[12px] font-black text-amber-600 uppercase mb-3">💡 Giải thích đáp án:</p>
                                                    {combo.map((q:any) => {
                                                        if (!q.explanation || String(q.explanation).trim() === '') return null;
                                                        return (
                                                            <div key={q.id} className="text-[14px] text-slate-700 font-serif leading-relaxed mb-3 last:mb-0 italic border-l-2 border-gray-300 pl-3">
                                                                <span className="font-bold text-slate-900 px-2 py-0.5 bg-slate-200 rounded text-[13px] mr-2 font-sans not-italic">Câu {questionIndexMap[String(q.id)] || q.id}</span>
                                                                <span dangerouslySetInnerHTML={{ __html: q.explanation }} />
                                                            </div>
                                                        )
                                                    })}
                                                 </div>
                                               )}
                                             </div>
                                           </div>
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

      <footer className="bg-white border-t border-gray-300 px-4 py-3 flex items-center shadow-[0_-2px_10px_rgba(0,0,0,0.05)] z-20 shrink-0 font-sans">
        <div className="flex-1 flex gap-2 overflow-x-auto pb-1 custom-scrollbar justify-center">
          {allQuestionIds.map(id => {
            let isAnswered = answers[id] && answers[id].trim() !== '';
            let btnClass = `w-9 h-9 shrink-0 flex items-center justify-center font-bold text-[14px] rounded transition-all `;
            
            const section = parts.flatMap((p: any) => p.sections || []).find((s:any) => s.questions?.some((sq:any)=>String(sq.id)===id));
            const qType = section?.questionType;

            // Xử lý báo trạng thái Footer cho Combo Checkbox
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
              let isCorrect = false;
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
                     isCorrect = idxInCombo < pts;
                 }
              } else {
                 const q = section?.questions.find((q:any) => String(q.id) === id);
                 isCorrect = q && answers[id]?.trim().toUpperCase() === q.correctAnswer?.trim().toUpperCase();
              }
              
              btnClass += isCorrect ? 'bg-emerald-100 text-emerald-700 border border-emerald-300' : 'bg-red-100 text-red-700 border border-red-300';
            } else { 
              btnClass += isAnswered ? 'bg-blue-600 text-white border-none' : 'bg-gray-100 text-gray-600 hover:bg-gray-200 border border-gray-300 cursor-pointer'; 
            }
            return (<button key={id} onClick={() => scrollToQuestion(id)} className={btnClass}>{questionIndexMap[id]}</button>)
          })}
        </div>
        <div className="ml-4 shrink-0">
          <button onClick={handleFinish} className={`font-bold text-sm px-8 py-3 rounded shadow-md transition ${isReviewMode ? 'bg-emerald-600 hover:bg-emerald-500 text-white' : 'bg-blue-600 hover:bg-blue-500 text-white'}`}>
            {isReviewMode ? 'Hoàn thành' : 'Nộp Bài Thi'}
          </button>
        </div>
      </footer>
    </div>
  );
}