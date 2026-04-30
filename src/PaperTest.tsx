import React, { useState, useEffect, useRef } from 'react';
import './tailwind.css';

export default function PaperTest({ onBack, testData, onFinish }: { onBack: () => void, testData?: any, onFinish?: (res: any) => void }) {
  let safeTestData = testData;
  if (typeof safeTestData === 'string') { try { safeTestData = JSON.parse(safeTestData); } catch (e) { } }

  // ĐỒNG BỘ CẤU TRÚC DỮ LIỆU MỚI TỪ ADMIN
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
    const saved = localStorage.getItem(`ielts_paper_ans_${safeTestData?.id}`); return saved ? JSON.parse(saved) : {};
  });

  useEffect(() => { 
    if (!isReviewMode && !isFinishingRef.current && safeTestData?.id) {
      localStorage.setItem(`ielts_paper_ans_${safeTestData.id}`, JSON.stringify(answers)); 
    }
  }, [answers, safeTestData?.id, isReviewMode]);

  const handleAnswer = (qNum: string, value: string) => { if (!isReviewMode) setAnswers(prev => ({ ...prev, [qNum]: value })); };
  const clearDraft = () => { if (window.confirm('Xóa toàn bộ bản nháp?')) { if (safeTestData?.id) localStorage.removeItem(`ielts_paper_ans_${safeTestData.id}`); setAnswers({}); } };

  const handleFinish = () => {
    if (!isReviewMode) {
      if (!window.confirm("Bạn có chắc chắn muốn nộp bài thi?")) return;
      
      isFinishingRef.current = true;
      if (safeTestData?.id) localStorage.removeItem(`ielts_paper_ans_${safeTestData.id}`);

      let score = 0; let total = 0;
      parts.forEach((p: any) => p.sections?.forEach((s: any) => s.questions?.forEach((q: any) => {
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
      if (onFinish) onFinish({ score: scoreResult.score, total: scoreResult.total, testTitle: basicInfo.title, bandScore: scoreResult.band }); else onBack();
    }
  };

  const resetTest = () => { if (window.confirm("Làm lại từ đầu?")) { setAnswers({}); setIsReviewMode(false); setTestStarted(false); setTimeLeft(parseInitialTime(basicInfo.timeLimit)); } };

  const parseInitialTime = (timeStr: string) => {
    if (!timeStr) return 3600; const timeParts = String(timeStr).replace(/[^0-9:]/g, '').split(':');
    return timeParts.length === 2 ? parseInt(timeParts[0]) * 60 + parseInt(timeParts[1]) : (parseInt(timeParts[0]) || 60) * 60;
  };

  const [timeLeft, setTimeLeft] = useState(() => parseInitialTime(basicInfo.timeLimit));
  useEffect(() => {
    if (!testStarted || timeLeft <= 0 || isReviewMode) return;
    const timer = setInterval(() => { setTimeLeft(prev => { if (prev <= 1) { clearInterval(timer); alert("⏰ Hết giờ!"); handleFinish(); return 0; } return prev - 1; }); }, 1000);
    return () => clearInterval(timer);
  }, [testStarted, timeLeft, isReviewMode]);

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

  // --- THUẬT TOÁN ĐỒNG BỘ ID VÀ SỐ THỨ TỰ ---
  const allQuestionIds: string[] = [];
  parts.forEach((p: any) => p.sections?.forEach((s: any) => {
    if (s.questionType === "Điền từ" || s.questionType === "Kéo thả vào Part") {
      const matches = s.content?.match(/\[(\d+)\]/g);
      if (matches) {
        matches.forEach((m: string) => {
          const num = m.replace(/\D/g, '');
          if (!allQuestionIds.includes(num)) allQuestionIds.push(num);
        });
      }
    } else {
      s.questions?.forEach((q: any) => {
        if (!allQuestionIds.includes(String(q.id))) allQuestionIds.push(String(q.id));
      });
    }
  }));

  const questionIndexMap = allQuestionIds.reduce((acc: any, id: string, idx: number) => { 
    acc[id] = idx + 1; 
    return acc; 
  }, {});
  // ------------------------------------------

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
              className="w-32 border-b-2 border-slate-400 focus:outline-none focus:border-blue-600 bg-transparent text-center text-blue-800 font-bold px-1 text-[15px] leading-tight pb-0.5" 
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
            <button onClick={handleStartTest} className="bg-blue-600 hover:bg-blue-700 text-white font-bold px-8 py-3 rounded-lg shadow-lg transition">Bắt Đầu Làm Bài</button>
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
                    {part.sections?.map((sec: any, sIndex: number) => (
                      <div key={sIndex} className="mb-10 font-sans">
                        
                        <div className="bg-gray-100 border border-gray-300 px-4 py-2 mb-4">
                          <h4 className="font-bold text-gray-800">{sec.title}</h4>
                        </div>

                        {(sec.questionType === "Điền từ" || sec.questionType === "Kéo thả vào Part") && (
                          <div className={`border p-8 rounded-xl shadow-sm ${isReviewMode ? 'border-slate-300' : 'border-gray-200'}`}>
                            <div className="space-y-6 leading-[2.5] text-[15px] font-serif text-slate-800">
                              {renderInlineQuestion(sec.content)}
                            </div>
                          </div>
                        )}

                        {sec.questionType === "Trắc nghiệm" && (
                          <div className="space-y-6">
                            {sec.questions?.map((q: any) => {
                              const correctAns = q.correctAnswer?.trim().toUpperCase(); 
                              const userAns = answers[String(q.id)]?.trim().toUpperCase(); 
                              const isCorrect = userAns === correctAns;
                              const displayIndex = questionIndexMap[q.id] || q.id;

                              return (
                                <div key={q.id} id={`q-${q.id}`} className={`p-6 rounded-xl border shadow-sm ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-200' : 'bg-red-50/50 border-red-200') : 'border-gray-200'}`}>
                                  <div className="flex gap-4 mb-4">
                                    <span className="font-bold text-gray-800 shrink-0 w-6 text-right pt-1">{displayIndex}.</span>
                                    <div className="flex-1">
                                      {isReviewMode && (<div className="mb-3">{isCorrect ? <span className="text-[11px] font-bold bg-emerald-100 text-emerald-700 px-3 py-1 rounded">✅ ĐÚNG</span> : <span className="text-[11px] font-bold bg-red-100 text-red-700 px-3 py-1 rounded">❌ SAI</span>}</div>)}
                                      {q.content && <p className="text-[16px] mb-4 font-serif leading-relaxed">{q.content}</p>}
                                      
                                      <div className={`flex flex-col gap-2`}>
                                        {q.options?.map((opt: string, i: number) => {
                                          const optionValue = opt.split('.')[0]?.trim().toUpperCase() || String.fromCharCode(65+i); 
                                          const isSelected = userAns === optionValue; 
                                          const isCorrectOpt = correctAns === optionValue;
                                          let labelClass = "flex items-start gap-3 p-1.5 transition";
                                          
                                          if (isReviewMode) { 
                                            if (isCorrectOpt) labelClass += " font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 rounded"; 
                                            else if (isSelected) labelClass += " text-red-500 line-through opacity-70 bg-red-50 rounded"; 
                                            else labelClass += " opacity-50"; 
                                          } else { 
                                            labelClass += " cursor-pointer group hover:text-blue-600"; 
                                          }
                                          return (
                                            <label key={i} className={labelClass}>
                                              <input type="radio" name={`q${q.id}`} value={optionValue} checked={isSelected} onChange={(e) => handleAnswer(String(q.id), e.target.value)} className="mt-1 accent-blue-600 cursor-pointer" disabled={isReviewMode} />
                                              <span className="text-[15px] font-serif leading-relaxed">{opt}</span>
                                            </label>
                                          );
                                        })}
                                      </div>
                                      {isReviewMode && (<div className="mt-6 pt-4 border-t border-slate-200"><p className="text-[12px] font-black text-amber-600 uppercase mb-2">💡 Giải thích đáp án:</p><p className="text-[14px] text-slate-700 italic">{q.explanation || "Không có lời giải thích."}</p></div>)}
                                    </div>
                                  </div>
                                </div>
                              );
                            })}
                          </div>
                        )}
                      </div>
                    ))}
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
            const isAnswered = answers[id] && answers[id].trim() !== '';
            let btnClass = `w-9 h-9 shrink-0 flex items-center justify-center font-bold text-[14px] rounded transition-all `;
            if (isReviewMode) {
              const q = parts.flatMap((p: any) => p.sections?.flatMap((s: any) => s.questions) || []).find((q: any) => String(q.id) === id);
              const isCorrect = q && answers[id]?.trim().toUpperCase() === q.correctAnswer?.trim().toUpperCase();
              btnClass += isCorrect ? 'bg-emerald-100 text-emerald-700 border border-emerald-300' : 'bg-red-100 text-red-700 border border-red-300';
            } else { btnClass += isAnswered ? 'bg-blue-600 text-white border-none' : 'bg-gray-100 text-gray-600 hover:bg-gray-200 border border-gray-300 cursor-pointer'; }
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