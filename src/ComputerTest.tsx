import React, { useState, useRef, useEffect } from 'react';
import './tailwind.css';

export default function ComputerTest({ onBack, testData, onFinish }: { onBack: () => void, testData?: any, onFinish?: (res: any) => void }) {
  let safeTestData = testData;
  if (typeof safeTestData === 'string') { try { safeTestData = JSON.parse(safeTestData); } catch (e) { } }
  if (typeof safeTestData === 'string') { try { safeTestData = JSON.parse(safeTestData); } catch (e) { } }

  const data = safeTestData || {};
  const parts = data.parts || []; 
  
  const isListening = data.skill === 'listening';
  const globalAudio = data.audioUrl || parts?.[0]?.audioUrl;

  const [testStarted, setTestStarted] = useState(false);
  const [isReviewMode, setIsReviewMode] = useState(false);
  const [scoreResult, setScoreResult] = useState({ score: 0, total: 0, band: "0.0" });
  
  const globalAudioRef = useRef<HTMLAudioElement>(null);
  const isFinishingRef = useRef(false);

  const [answers, setAnswers] = useState<Record<string, string>>(() => {
    try {
      const saved = localStorage.getItem(`ielts_ans_${data.testId}`);
      return saved ? JSON.parse(saved) : {};
    } catch (error) {
      return {};
    }
  });

  useEffect(() => {
    if (!isReviewMode && !isFinishingRef.current && data.testId) {
      localStorage.setItem(`ielts_ans_${data.testId}`, JSON.stringify(answers));
    }
  }, [answers, data.testId, isReviewMode]);

  const handleAnswer = (qNum: string, value: string) => { if (!isReviewMode) setAnswers(prev => ({ ...prev, [String(qNum)]: value })); };

  const clearDraft = () => {
    if(window.confirm('Xóa bản nháp và làm lại từ đầu?')) { 
      if (data.testId) localStorage.removeItem(`ielts_ans_${data.testId}`); 
      setAnswers({}); 
    }
  };

  const handleFinish = () => {
    if (!isReviewMode) {
      if (!window.confirm("Bạn có chắc chắn muốn nộp bài thi?")) return;
      
      isFinishingRef.current = true;
      if (data.testId) localStorage.removeItem(`ielts_ans_${data.testId}`);

      let score = 0; let total = 0;
      parts.forEach((p: any) => p.questionGroups?.forEach((g: any) => g.questions?.forEach((q: any) => {
        total++;
        const userAns = answers[String(q.id)]?.trim().toUpperCase() || "";
        const correctAns = String(q.correctAnswer || "").trim().toUpperCase();
        if (userAns === correctAns && correctAns !== "") score++;
      })));
      let band = "0.0";
      if (score >= 39) band = "9.0"; else if (score >= 37) band = "8.5"; else if (score >= 35) band = "8.0"; else if (score >= 33) band = "7.5";
      else if (score >= 30) band = "7.0"; else if (score >= 27) band = "6.5"; else if (score >= 23) band = "6.0"; else if (score >= 19) band = "5.5";
      else if (score >= 15) band = "5.0"; else if (score >= 13) band = "4.5"; else if (score >= 10) band = "4.0"; else if (score >= 8) band = "3.5";
      else if (score >= 6) band = "3.0"; else if (score >= 4) band = "2.5"; else if (score >= 2) band = "2.0"; else if (score >= 1) band = "1.0";

      setScoreResult({ score, total, band }); setIsReviewMode(true); window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      if (onFinish) onFinish({ score: scoreResult.score, total: scoreResult.total, testTitle: data.title || "IELTS Test", bandScore: scoreResult.band }); 
      else onBack();
    }
  };

  const resetTest = () => {
    if (window.confirm("Làm lại từ đầu? Mọi đáp án sẽ bị xóa.")) { setAnswers({}); setIsReviewMode(false); setTestStarted(false); setTimeLeft(parseInitialTime(data.timeLimit)); }
  };

  const [currentPartIndex, setCurrentPartIndex] = useState(0);
  const currentPart = parts[currentPartIndex];
  
  const questionToPartMap: Record<string, number> = {};
  parts.forEach((p: any, pIndex: number) => { p.questionGroups?.forEach((g: any) => g.questions?.forEach((q: any) => { questionToPartMap[String(q.id)] = pIndex; })); });

  const scrollToQuestion = (qNum: number | string) => {
    const targetPartIndex = questionToPartMap[String(qNum)];
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

  const parseInitialTime = (timeStr: string) => {
    if (!timeStr) return 3600; const timeParts = String(timeStr).replace(/[^0-9:]/g, '').split(':');
    return timeParts.length === 2 ? parseInt(timeParts[0]) * 60 + parseInt(timeParts[1]) : (parseInt(timeParts[0]) || 60) * 60;
  };

  const [timeLeft, setTimeLeft] = useState(() => parseInitialTime(data.timeLimit));

  useEffect(() => {
    if (!testStarted || timeLeft <= 0 || isReviewMode) return;
    const timer = setInterval(() => { setTimeLeft(prev => { if (prev <= 1) { clearInterval(timer); alert("⏰ Hết giờ!"); handleFinish(); return 0; } return prev - 1; }); }, 1000);
    return () => clearInterval(timer);
  }, [testStarted, timeLeft, isReviewMode]);

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

  const renderInlineQuestion = (text: string) => {
    if (!text) return null; 
    const textParts = text.split(/(\[\d+\])/g);
    return textParts.map((part, index) => {
      const match = part.match(/\[(\d+)\]/);
      if (match) {
        const qNum = match[1];
        const userAns = answers[String(qNum)] || '';
        
        if (isReviewMode) {
          const qData = parts.flatMap((p: any) => p.questionGroups?.flatMap((g: any) => g.questions) || []).find((q: any) => String(q.id) === String(qNum));
          const correctAns = qData?.correctAnswer || '';
          const isCorrect = String(userAns).trim().toUpperCase() === String(correctAns).trim().toUpperCase();
          
          return (
            <span key={index} className="relative inline-flex items-center align-middle mx-1 -translate-y-[14px] whitespace-nowrap">
              <span className={`inline-flex items-center justify-center px-3 py-1 text-[14px] font-bold text-white rounded-md shadow-sm border h-[30px] ${isCorrect ? 'bg-emerald-500 border-emerald-600' : 'bg-red-500 border-red-600'}`}>
                {qNum}. {userAns || '(trống)'}
              </span>
              {!isCorrect && (
                <span className="absolute top-full left-1/2 -translate-x-1/2 mt-1 text-[12px] text-emerald-800 font-bold bg-emerald-100 px-2 py-0.5 border border-emerald-300 rounded-md shadow-sm whitespace-nowrap z-10">
                  ĐA: {correctAns}
                </span>
              )}
            </span>
          );
        }

        return (
          <span key={index} id={`q-${qNum}`} className="inline-flex items-center align-middle mx-1 -translate-y-[14px] whitespace-nowrap">
            <span className="inline-flex items-center justify-center bg-[#1f2937] text-white font-bold px-2 min-w-[30px] h-[30px] text-[14px] rounded-sm shadow-sm">
              {qNum}
            </span>
            <input 
              type="text" 
              className="inline-block w-32 ml-1 border border-slate-400 focus:outline-none focus:border-blue-600 focus:ring-1 focus:ring-blue-600 bg-white text-center text-blue-800 font-bold px-2 text-[15px] h-[30px] rounded-sm shadow-inner m-0" 
              value={userAns} 
              onChange={(e) => handleAnswer(qNum, e.target.value)} 
              autoComplete="off" 
            />
          </span>
        );
      }
      return <span key={index} dangerouslySetInnerHTML={{ __html: part }} />;
    });
  };

  const handleStartTest = () => {
    setTestStarted(true);
    if (globalAudioRef.current && isListening) { globalAudioRef.current.play().catch(e => { console.error("Autoplay blocked:", e); alert("Trình duyệt không cho phép tự động phát âm thanh. Vui lòng ấn nút Bắt Đầu lại."); }); }
  };

  const totalQuestions = data.totalQuestions || parts.reduce((acc: number, p: any) => acc + (p.questionGroups?.reduce((gAcc: number, g: any) => gAcc + (g.questions?.length || 0), 0) || 0), 0) || 40;
  const footerQuestions = Array.from({ length: totalQuestions }, (_, i) => i + 1);
  
  const showLeftColumn = !(isListening && !isReviewMode);

  return (
    <React.Fragment>
      {isListening && globalAudio && !isReviewMode && ( <audio ref={globalAudioRef} src={globalAudio} preload="auto" className="hidden" /> )}

      {!testStarted ? (
        <div className="flex flex-col h-screen items-center justify-center bg-[#f0f2f5] font-sans">
          <div className="bg-white p-10 rounded-2xl shadow-xl text-center max-w-lg border border-slate-200 w-full">
            <div className="text-6xl mb-6">{isListening ? '🎧' : '📖'}</div>
            <h1 className="text-2xl font-black text-slate-800 mb-2">{data.title || "IELTS Test"}</h1>
            <p className="text-slate-500 mb-8 font-medium">Thời gian: {formatTime(parseInitialTime(data.timeLimit))}</p>
            {isListening && (
              <div className="bg-amber-50 border border-amber-200 p-4 rounded-lg text-amber-700 text-[13px] font-medium mb-8 text-left leading-relaxed shadow-inner">
                <span className="font-bold">⚠️ LƯU Ý THI LISTENING:</span> File âm thanh đã được tải ngầm và sẽ <span className="font-bold underline">tự động phát ngay lập tức</span> khi bạn bấm Bắt Đầu. Bạn chỉ có thể chỉnh âm lượng, KHÔNG THỂ tạm dừng hay tua lại.
              </div>
            )}
            <div className="flex gap-4 justify-center">
              <button onClick={onBack} className="px-6 py-3 rounded-lg font-bold text-slate-500 hover:bg-slate-100 border border-slate-300 transition">Quay lại</button>
              <button onClick={handleStartTest} className="bg-blue-600 hover:bg-blue-700 text-white font-bold px-8 py-3 rounded-lg shadow-lg transition">Bắt Đầu Làm Bài</button>
            </div>
          </div>
        </div>
      ) : (
        <div className="flex flex-col h-screen bg-white font-sans text-gray-900 relative">
          
          {highlightMenu.show && !isReviewMode && (
            <div style={{ left: highlightMenu.x, top: highlightMenu.y, transform: 'translate(-50%, -100%)' }} className="fixed z-50 bg-white text-gray-800 rounded shadow-[0_4px_15px_rgba(0,0,0,0.15)] border border-gray-200 text-sm flex flex-col py-1 min-w-[130px]" onMouseDown={(e) => e.preventDefault()}>
              <button onClick={handleCopy} className="flex items-center gap-3 px-4 py-2 hover:bg-gray-100 text-left w-full"><span className="font-medium">Copy</span></button>
              <button onClick={applyHighlight} className="flex items-center gap-3 px-4 py-2 hover:bg-gray-100 text-left w-full"><span className="font-medium text-yellow-600">Highlight</span></button>
              <button onClick={initNote} className="flex items-center gap-3 px-4 py-2 hover:bg-gray-100 text-left w-full"><span className="font-medium text-blue-600">Note</span></button>
            </div>
          )}

          {stickyNote.show && (
            <div style={{ left: Math.min(stickyNote.x, window.innerWidth - 300), top: stickyNote.y }} className="fixed z-50 flex flex-col shadow-2xl rounded border border-gray-300 w-72">
              <div className="bg-[#4aa0e6] h-6 flex justify-between items-center px-2 cursor-move"><button onClick={() => setStickyNote({...stickyNote, show: false})} className="text-white text-xs">✕</button></div>
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

          <header className={`px-6 py-3 flex justify-between items-center z-10 shrink-0 shadow ${isReviewMode ? 'bg-emerald-700' : 'bg-[#1f2937]'} text-white`}>
            <div className="flex items-center gap-4">
              <button onClick={onBack} className="bg-black/20 hover:bg-black/40 border border-white/20 text-sm px-3 py-1.5 rounded font-bold transition shrink-0">⬅ Thoát</button>
              <div className="font-bold text-lg tracking-wide border-l border-white/30 pl-4 truncate max-w-[200px] md:max-w-md">{isReviewMode ? `[CHỮA BÀI] ${data.title || "IELTS"}` : (data.title || "IELTS Test")}</div>
            </div>
            {isListening && globalAudio && (
              <div className="flex-1 max-w-lg mx-8 flex items-center justify-center">
                {isReviewMode ? (<audio controls src={globalAudio} className="h-9 w-full rounded outline-none" style={{ filter: 'invert(0.9) hue-rotate(180deg)' }} />) : (<div className="flex items-center gap-3 bg-black/30 px-4 py-1.5 rounded-full border border-white/10" title="Chỉnh âm lượng"> <span className="text-lg">🔊</span> <input type="range" min="0" max="1" step="0.05" defaultValue="1" onChange={(e) => { if(globalAudioRef.current) globalAudioRef.current.volume = parseFloat(e.target.value) }} className="w-32 accent-blue-400 cursor-pointer" /> </div>)}
              </div>
            )}
            <div className="flex items-center gap-4 shrink-0">
              {!isReviewMode && <button onClick={clearDraft} className="text-sm text-gray-300 hover:text-red-300 underline font-medium">Xóa nháp</button>}
              {isReviewMode && <button onClick={resetTest} className="text-sm bg-white/20 hover:bg-white/30 px-3 py-1.5 rounded font-bold transition">🔄 Làm Lại</button>}
              <div className={`font-bold text-lg flex items-center gap-2 px-3 border-l border-white/30 ${timeLeft <= 300 && !isReviewMode ? 'text-red-400 animate-pulse' : 'text-white'}`}>{isReviewMode ? `Điểm: ${scoreResult.score}/${scoreResult.total} (Band ${scoreResult.band})` : formatTime(timeLeft)}</div>
              <button onClick={handleFinish} className={`font-bold text-sm px-5 py-1.5 rounded transition shadow-sm border ${isReviewMode ? 'bg-emerald-500 hover:bg-emerald-600 border-emerald-400 text-white' : 'bg-blue-600 hover:bg-blue-500 border-blue-500 text-white'}`}>{isReviewMode ? 'Lưu & Thoát' : 'Nộp bài'}</button>
            </div>
          </header>

          <div className={`border-b border-gray-300 px-6 py-2 flex gap-2 ${isReviewMode ? 'bg-emerald-50' : 'bg-gray-100'}`}>
            {parts.map((p: any, index: number) => (
              <button key={index} onClick={() => setCurrentPartIndex(index)} className={`px-4 py-1.5 text-sm font-bold rounded shadow-sm transition-colors ${currentPartIndex === index ? (isReviewMode ? 'bg-emerald-600 text-white border-emerald-600' : 'bg-white text-blue-600 border border-gray-300 border-b-transparent') : 'bg-gray-200 text-gray-600 hover:bg-gray-300 border border-transparent'}`}>{p.title || `Part ${index + 1}`}</button>
            ))}
          </div>

          <main className="flex flex-1 overflow-hidden relative" ref={containerRef} onMouseUp={handleMouseUp}>
            {showLeftColumn && (
              <>
                <section className="p-8 overflow-y-auto leading-relaxed custom-scrollbar relative" style={{ width: `${leftWidth}%`, flex: 'none' }} onClick={handleContentClick}>
                  {currentPart?.passageContent ? (
                    <div><h2 className="font-bold text-xl mb-4 text-slate-800">{currentPart?.title}</h2>{isReviewMode && isListening && <div className="bg-amber-100 text-amber-800 p-3 rounded font-bold text-[13px] mb-6 border border-amber-300 inline-block shadow-sm">🎙️ TAPESCRIPT CHỮA BÀI NẰM Ở ĐÂY ➔</div>}<p className="font-bold mb-6 text-gray-700">{currentPart?.instructions}</p><h3 className="font-bold text-center mb-6 text-2xl text-slate-900">{currentPart?.passageTitle}</h3><div className="text-justify space-y-4 text-[15px]" dangerouslySetInnerHTML={{ __html: currentPart?.passageContent || "" }} /></div>
                  ) : (<div className="flex flex-col items-center justify-center h-full text-gray-400 opacity-70"><span className="text-6xl mb-4">📄</span><p className="font-bold text-lg">Không có dữ liệu văn bản</p></div>)}
                  <div className="h-[200px]" />
                </section>
                <div className="w-2 bg-gray-200 hover:bg-gray-300 cursor-col-resize flex flex-col justify-center items-center z-10 border-x border-gray-300" onMouseDown={startDrag}><div className="w-0.5 h-10 bg-gray-500"></div></div>
              </>
            )}

            <section className={`p-8 overflow-y-auto leading-relaxed custom-scrollbar ${isReviewMode ? 'bg-slate-50' : 'bg-[#f9fafb]'}`} style={{ width: showLeftColumn ? `${100 - leftWidth}%` : '100%', flex: 'none' }}>
              <div className={`${!showLeftColumn ? 'max-w-3xl mx-auto' : ''}`}>
                {currentPart?.audioUrl && (!isListening || isReviewMode) && (<div className="mb-8 bg-white p-4 rounded-xl border border-gray-300 shadow-sm flex items-center gap-4"><p className="text-xs font-bold text-gray-500 uppercase tracking-widest shrink-0">Audio Part:</p><audio controls controlsList="nodownload" className="h-10 flex-1 outline-none"><source src={currentPart.audioUrl} type="audio/mpeg" /></audio></div>)}
                {currentPart?.questionGroups?.map((group: any, index: number) => (
                  <div key={index} className="mb-12">
                    <h3 className="font-bold text-lg mb-2 text-slate-800">{group.title}</h3><p className="italic mb-4 text-gray-600">{group.instruction}</p>
                    
                    {group.type === "GAP_FILL" && (
                      <div className={`border p-8 shadow-sm rounded-xl ${isReviewMode ? 'bg-white border-slate-300' : 'bg-white border-gray-200'}`}>
                        {group.boxTitle && <h4 className="font-bold mb-4">{group.boxTitle}</h4>}
                        <div className="space-y-6 leading-loose text-[16px] font-serif text-slate-800">{renderInlineQuestion(group.content)}</div>
                      </div>
                    )}
                    
                    {(group.type === "TFNG" || group.type === "MCQ") && (
                       <div className="space-y-6">
                         {group.questions?.map((q: any) => {
                            const correctAns = q.correctAnswer?.trim().toUpperCase(); const userAns = answers[q.id]?.trim().toUpperCase(); const isCorrect = userAns === correctAns;
                            const optionsList = group.type === "TFNG" ? ['TRUE', 'FALSE', 'NOT GIVEN', 'YES', 'NO'] : q.options;
                            return (
                             <div key={q.id} id={`q-${q.id}`} className={`p-6 rounded-xl border relative group ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-200' : 'bg-red-50/50 border-red-200') : 'bg-white border-slate-200 shadow-sm hover:border-slate-300'}`}>
                               
                               {/* ĐÃ FIX: ĐỒNG BỘ BOX ĐEN CHUẨN IDP CHO TFNG/MCQ */}
                               <div className="flex items-start gap-3 mb-4">
                                 <span className={`inline-flex items-center justify-center font-bold min-w-[30px] h-[30px] text-[14px] rounded-sm shadow-sm shrink-0 ${isReviewMode ? (isCorrect ? 'bg-emerald-500 text-white' : 'bg-red-500 text-white') : 'bg-[#1f2937] text-white'}`}>
                                   {q.id}
                                 </span>
                                 <p className="text-[15px] font-medium text-slate-800 pt-[4px]">{q.text}</p>
                               </div>

                               <div className={`flex ${group.type === "TFNG" ? 'gap-8' : 'flex-col gap-3'} ml-10 mt-4`}>
                                 {optionsList?.map((opt: string, i: number) => {
                                   const optionValue = group.type === "TFNG" ? opt : opt.split('.')[0]?.trim().toUpperCase(); const isSelected = userAns === optionValue; const isCorrectOpt = correctAns === optionValue;
                                   let labelClass = "flex items-start gap-3 p-2 rounded transition border border-transparent";
                                   if (isReviewMode) { if (isCorrectOpt) labelClass += " bg-emerald-100 border-emerald-400 font-bold text-emerald-800"; else if (isSelected) labelClass += " bg-red-100 border-red-300 text-red-700 line-through opacity-60"; else labelClass += " opacity-50"; } else { labelClass += " cursor-pointer hover:bg-gray-100 hover:border-gray-300"; }
                                   return (
                                     <label key={i} className={labelClass}>
                                       <input type="radio" name={`q${q.id}`} value={optionValue} checked={isSelected} onChange={(e) => handleAnswer(String(q.id), e.target.value)} className="mt-1 w-4 h-4 accent-blue-600" disabled={isReviewMode} />
                                       <span className="text-[14px] leading-relaxed">{opt}</span>
                                     </label>
                                   )
                                 })}
                               </div>
                               {isReviewMode && (<div className="mt-5 ml-10 pt-4 border-t border-slate-200"><p className="text-[13px] font-black text-amber-600 uppercase mb-1">💡 Giải thích đáp án:</p><p className="text-[14px] text-slate-700 font-medium">{q.explanation || "Không có lời giải thích."}</p></div>)}
                             </div>
                            )
                         })}
                       </div>
                    )}

                    {(group.type === "MATCHING") && (
                      <div className="space-y-6">
                        {group.questions?.[0]?.options?.length > 0 && (
                          <div className="border border-gray-300 p-4 mb-6 bg-gray-50 rounded-lg">
                            <div className="space-y-2">
                              {group.questions[0].options.map((opt: string, i: number) => (<p key={i} className="text-[15px] font-medium font-sans text-slate-700">{opt}</p>))}
                            </div>
                          </div>
                        )}
                        <div className="space-y-4">
                          {group.questions?.map((q: any) => {
                            const correctAns = q.correctAnswer?.trim().toUpperCase(); const userAns = answers[String(q.id)]?.trim().toUpperCase() || ''; const isCorrect = userAns === correctAns;
                            return (
                              <div key={q.id} id={`q-${q.id}`} className={`p-5 rounded-xl border ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-200' : 'bg-red-50/50 border-red-200') : 'bg-slate-50 border-slate-200'}`}>
                                
                                {/* ĐÃ FIX: ĐỒNG BỘ BOX ĐEN CHUẨN IDP CHO MATCHING */}
                                <div className="flex items-start gap-3 mb-4">
                                  <span className={`inline-flex items-center justify-center font-bold min-w-[30px] h-[30px] text-[14px] rounded-sm shadow-sm shrink-0 ${isReviewMode ? (isCorrect ? 'bg-emerald-500 text-white' : 'bg-red-500 text-white') : 'bg-[#1f2937] text-white'}`}>
                                    {q.id}
                                  </span>
                                  <p className="text-[16px] font-normal text-slate-800 leading-relaxed pt-[3px]">{q.text}</p>
                                </div>
                                
                                <div className="relative max-w-sm">
                                  <select className={`w-full p-3 rounded-lg border appearance-none font-medium text-[15px] outline-none focus:ring-2 focus:ring-blue-400 ${isReviewMode ? (isCorrect ? 'bg-emerald-100 border-emerald-400 text-emerald-800' : 'bg-red-100 border-red-400 text-red-800') : 'bg-white border-slate-300 text-slate-700 cursor-pointer'}`} value={userAns} onChange={(e) => handleAnswer(String(q.id), e.target.value.toUpperCase())} disabled={isReviewMode}>
                                    <option value="" disabled>-- Chọn câu trả lời --</option>
                                    {group.questions[0].options?.map((opt:string, i:number) => { const letter = opt.split('.')[0]?.trim().toUpperCase(); return <option key={i} value={letter}>{opt}</option> })}
                                  </select>
                                  {!isReviewMode && (<div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-4 text-slate-500"><svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg></div>)}
                                </div>
                                {isReviewMode && !isCorrect && (<p className="mt-3 text-[13px] font-bold text-emerald-700">✅ Đáp án đúng: {correctAns}</p>)}
                              </div>
                            );
                          })}
                        </div>
                      </div>
                    )}

                  </div>
                ))}
              </div>
              <div className="h-[200px]" />
            </section>
          </main>

          <footer className="bg-[#f0f0f0] border-t border-gray-300 p-2 flex justify-between items-center shrink-0 z-20">
            <div className="flex items-center gap-2 ml-4">
              <input type="checkbox" id="review" className="w-4 h-4 cursor-pointer accent-black" disabled={isReviewMode} />
              <label htmlFor="review" className="text-sm font-bold cursor-pointer">Review</label>
            </div>
            <div className="flex-1 flex justify-center items-center gap-1.5 overflow-x-auto px-4 py-1 custom-scrollbar">
              {footerQuestions.map(num => {
                const isAnswered = answers[String(num)] && answers[String(num)].trim() !== '';
                let btnClass = `w-8 h-8 flex items-center justify-center font-bold text-sm bg-white transition-all box-border shrink-0 `;
                if (isReviewMode) {
                  const q = parts.flatMap((p: any) => p.questionGroups?.flatMap((g: any) => g.questions) || []).find((q: any) => String(q.id) === String(num));
                  const isCorrect = q && answers[String(num)]?.trim().toUpperCase() === q.correctAnswer?.trim().toUpperCase();
                  btnClass += isCorrect ? 'bg-emerald-200 border border-emerald-400 text-emerald-800' : 'bg-red-200 border border-red-400 text-red-800';
                } else { btnClass += isAnswered ? 'border-b-[4px] border-b-black border-t border-x border-gray-400 text-black' : 'border border-gray-400 text-black hover:bg-gray-100 cursor-pointer'; }
                return (<button key={num} onClick={() => scrollToQuestion(num)} className={btnClass}>{num}</button>)
              })}
            </div>
          </footer>
        </div>
      )}
    </React.Fragment>
  );
}