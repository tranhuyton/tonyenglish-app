import React, { useState, useEffect, useRef } from 'react';
import { supabase } from './supabase';
import './tailwind.css';

export default function StandardTest({ onBack, testData, onFinish }: { onBack: () => void, testData: any, onFinish: (res: any) => void }) {
  // 1. KIỂM TRA VÀ PARSE DỮ LIỆU SIÊU AN TOÀN
  let safeData = testData || {};
  if (typeof safeData === 'string') {
    try { safeData = JSON.parse(safeData); } catch (e) { safeData = {}; }
  }

  let contentJSON = safeData?.content_json || safeData || {};
  if (typeof contentJSON === 'string') {
    try { contentJSON = JSON.parse(contentJSON); } catch (e) { contentJSON = {}; }
  }

  const basicInfo = contentJSON?.basicInfo || { title: "Standard Test", timeLimit: "60", skill: "" };
  const parts = Array.isArray(contentJSON?.parts) ? contentJSON.parts : [];
  
  const isListening = String(basicInfo.skill || '').toLowerCase().includes('listening');
  const globalAudio = basicInfo.audioUrl || parts[0]?.audioUrl;

  const [testStarted, setTestStarted] = useState(false);
  const [isReviewMode, setIsReviewMode] = useState(false);
  const [scoreResult, setScoreResult] = useState({ score: 0, total: 0 });
  const [showPalette, setShowPalette] = useState(false); 
  
  const globalAudioRef = useRef<HTMLAudioElement>(null);
  const isFinishingRef = useRef(false);

  // --- LOGIC KÉO THẢ THANH NGĂN CÁCH (SPLIT PANE CHO READING) ---
  const [leftWidth, setLeftWidth] = useState(45); 
  const containerRef = useRef<HTMLDivElement>(null);

  const handleMouseDown = (e: React.MouseEvent) => {
    e.preventDefault();
    document.body.style.cursor = 'col-resize';
    document.body.style.userSelect = 'none'; 
    
    const handleMouseMove = (moveEvent: MouseEvent) => {
      if (!containerRef.current) return;
      const containerRect = containerRef.current.getBoundingClientRect();
      const newWidth = ((moveEvent.clientX - containerRect.left) / containerRect.width) * 100;
      if (newWidth >= 20 && newWidth <= 80) setLeftWidth(newWidth);
    };

    const handleMouseUp = () => {
      document.body.style.cursor = 'default';
      document.body.style.userSelect = 'auto';
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };

    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);
  };

  // --- QUẢN LÝ LOCAL STORAGE AN TOÀN ---
  const [answers, setAnswers] = useState<Record<string, string>>(() => {
    try {
      const saved = localStorage.getItem(`std_ans_${safeData?.id}`);
      return saved ? JSON.parse(saved) : {};
    } catch (e) { return {}; }
  });

  const [marked, setMarked] = useState<Record<string, boolean>>(() => {
    try {
      const saved = localStorage.getItem(`std_mark_${safeData?.id}`);
      return saved ? JSON.parse(saved) : {};
    } catch (e) { return {}; }
  });

  useEffect(() => {
    if (!isReviewMode && !isFinishingRef.current && safeData?.id) {
      localStorage.setItem(`std_ans_${safeData.id}`, JSON.stringify(answers));
      localStorage.setItem(`std_mark_${safeData.id}`, JSON.stringify(marked));
    }
  }, [answers, marked, safeData?.id, isReviewMode]);

  const handleAnswer = (qId: string, val: string) => { 
    if(!isReviewMode) setAnswers(prev => ({ ...prev, [qId]: String(val) })); 
  };
  
  const toggleMark = (qId: string) => { 
    if(!isReviewMode) setMarked(prev => ({ ...prev, [qId]: !prev[qId] })); 
  };

  const handleFinish = async () => {
    if (!isReviewMode) {
      if (!window.confirm("Bạn có chắc chắn muốn nộp bài?")) return;
      
      isFinishingRef.current = true;
      if (safeData?.id) {
        localStorage.removeItem(`std_ans_${safeData.id}`);
        localStorage.removeItem(`std_mark_${safeData.id}`);
      }

      let score = 0;
      let total = 0;
      parts?.forEach((p: any) => {
        p?.sections?.forEach((s: any) => {
          s?.questions?.forEach((q: any) => {
            if (!q?.id) return;
            total++;
            // BỌC STRING() ĐỂ CHỐNG CRASH KHI ĐÁP ÁN LÀ SỐ
            const uAns = String(answers[String(q.id)] || '').trim().toUpperCase();
            const cAns = String(q.correctAnswer || '').trim().toUpperCase();
            if (uAns === cAns && cAns !== '') score++;
          });
        });
      });

      setScoreResult({ score, total });
      setIsReviewMode(true);
      setShowPalette(false);
      window.scrollTo({ top: 0, behavior: 'smooth' });

      // LƯU KẾT QUẢ VÀO SUPABASE
      try {
        const { data: { user } } = await supabase.auth.getUser();
        if (user) {
          const timeSpentSecs = parseInitialTime(basicInfo.timeLimit) - timeLeft;
          await supabase.from('test_results').insert([{
            user_id: user.id,
            course_id: safeData?.course_id || safeData?.content_json?.basicInfo?.courseId || null,
            test_title: basicInfo.title || safeData?.title || "Standard Test",
            test_type: safeData?.test_type || 'Standard',
            score: score,
            total_score: total,
            time_spent: timeSpentSecs > 0 ? timeSpentSecs : 0,
            details: { userAnswers: answers }
          }]);
        }
      } catch (error) {
        console.error("Lỗi lưu kết quả thi:", error);
      }

    } else {
      if (onFinish) onFinish({ score: scoreResult.score, total: scoreResult.total, testTitle: basicInfo.title });
      else onBack();
    }
  };

  const parseInitialTime = (val: any) => {
    if (!val) return 3600;
    if (typeof val === 'number') return val * 60;
    const num = parseInt(val);
    return isNaN(num) ? 3600 : num * 60;
  };

  const [timeLeft, setTimeLeft] = useState(() => parseInitialTime(basicInfo.timeLimit));
  
  useEffect(() => {
    if (!testStarted || timeLeft <= 0 || isReviewMode) return;
    const timer = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) { clearInterval(timer); alert("⏰ Hết giờ làm bài!"); handleFinish(); return 0; }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timer);
  }, [testStarted, timeLeft, isReviewMode]);

  const formatTime = (sec: number) => {
    const m = Math.floor(sec / 60).toString().padStart(2, '0');
    const s = (sec % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  };

  const scrollToQuestion = (id: string) => {
    const el = document.getElementById(`q-${id}`);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      el.classList.add('ring-4', 'ring-[#3ba1e2]/50');
      setTimeout(() => el.classList.remove('ring-4', 'ring-[#3ba1e2]/50'), 1500);
    }
    setShowPalette(false);
  };

  // --- THUẬT TOÁN ĐỒNG BỘ ID CÂU HỎI AN TOÀN ---
  const allQuestionIds: string[] = [];
  parts?.forEach((p: any) => {
    p?.sections?.forEach((s: any) => {
      if (s?.questionType === "Điền từ" || s?.questionType === "Kéo thả vào Part") {
        const matches = String(s?.content || '').match(/\[(\d+)\]/g);
        if (matches) {
          matches.forEach((m: string) => {
            const num = m.replace(/\D/g, '');
            if (!allQuestionIds.includes(num)) allQuestionIds.push(num);
          });
        }
      } else {
        s?.questions?.forEach((q: any) => {
          if (q?.id && !allQuestionIds.includes(String(q.id))) {
            allQuestionIds.push(String(q.id));
          }
        });
      }
    });
  });

  const questionIndexMap = allQuestionIds.reduce((acc: any, id: string, idx: number) => { 
    acc[id] = idx + 1; 
    return acc; 
  }, {});

  const answeredCount = Object.keys(answers).length;
  const markedCount = Object.values(marked).filter(Boolean).length;
  const totalCount = allQuestionIds.length;

  // --- RENDER DẠNG ĐIỀN TỪ (CÓ LIÊN KẾT ĐÚNG ID) ---
  const renderInlineQuestion = (text: any) => {
    if (!text) return null;
    const safeText = String(text);
    const textParts = safeText.split(/(\[\d+\])/g);
    return textParts.map((partText, index) => {
      const match = partText.match(/\[(\d+)\]/);
      if (match) {
        const qNum = match[1]; 
        const userAns = String(answers[qNum] || '');
        const displayIndex = questionIndexMap[qNum] || qNum;
        
        if (isReviewMode) {
          const qData = parts.flatMap((p: any) => p?.sections?.flatMap((s: any) => s?.questions) || []).find((q: any) => String(q?.id) === String(qNum));
          const correctAns = String(qData?.correctAnswer || '');
          const isCorrect = userAns.trim().toUpperCase() === correctAns.trim().toUpperCase();
          
          return (
            <span key={index} className="relative inline-flex flex-col items-center align-top mx-1 mt-1">
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
          <span key={index} id={`q-${qNum}`} className="inline-flex items-baseline mx-1 scroll-mt-24">
            <span className="font-bold text-[15px] mr-1 text-slate-700">{displayIndex}.</span>
            <input 
              type="text" 
              className="w-28 border-b-[1.5px] border-slate-500 focus:outline-none focus:border-[#3ba1e2] bg-transparent text-center text-[#3ba1e2] font-bold px-1 text-[16px] pb-[1px]" 
              style={{ lineHeight: '1.2' }}
              value={userAns} 
              onChange={(e) => handleAnswer(qNum, e.target.value)} 
              autoComplete="off" 
            />
          </span>
        );
      }
      return <span key={index} dangerouslySetInnerHTML={{ __html: partText || '' }} />;
    });
  };

  const handleStartTest = () => {
    setTestStarted(true);
    if (globalAudioRef.current && isListening) {
      globalAudioRef.current.play().catch(e => {
        console.error("Autoplay blocked:", e);
        alert("Trình duyệt chặn phát âm thanh. Vui lòng bấm Bắt Đầu lại.");
      });
    }
  };

  // ==========================================
  // VIEW 1: GIAO DIỆN READING (SPLIT-PANE) CÓ THANH KÉO
  // ==========================================
  const renderReadingLayout = () => (
    <div className="flex flex-col h-screen font-sans bg-[#f4f6f8] overflow-hidden">
      <header className="h-14 bg-[#3498db] text-white flex justify-between items-center px-6 shrink-0 shadow-md z-20">
        <div className="font-bold text-[16px] flex items-center gap-3">
          <span className="text-xl">📖</span>
          {isReviewMode ? `[REVIEW] ${basicInfo?.title}` : basicInfo?.title}
        </div>
        <button onClick={onBack} className="text-sm font-bold border border-white/40 px-4 py-1.5 rounded hover:bg-white/10 transition flex items-center gap-2">
          ⚙ Thoát
        </button>
      </header>

      <div className="flex-1 flex overflow-hidden relative" ref={containerRef}>
        
        {/* CỘT TRÁI: PASSAGE */}
        <div className="bg-[#f1f5f8] overflow-y-auto custom-scrollbar" style={{ width: `${leftWidth}%` }}>
          <div className="p-8">
            {isReviewMode && (
              <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 mb-8 text-center">
                 <h3 className="text-slate-500 font-bold uppercase tracking-widest text-xs mb-2">Kết quả bài làm</h3>
                 <div className="text-4xl font-black text-[#3498db]">{scoreResult.score} <span className="text-2xl text-slate-400">/ {scoreResult.total}</span></div>
              </div>
            )}

            {parts?.map((part: any, pIdx: number) => (
              <div key={part?.id || pIdx} className="mb-12">
                {part?.title && <h3 className="font-black text-lg text-slate-800 mb-4">{part.title}</h3>}
                {part?.imageUrl && <img src={part.imageUrl} className="max-w-full mb-6 rounded-lg shadow-sm border border-slate-200" alt="Part Image" />}
                {part?.content && <div className="prose prose-slate max-w-none text-slate-700 whitespace-pre-wrap leading-relaxed mb-8 bg-white p-6 rounded-xl border border-slate-200 shadow-sm" dangerouslySetInnerHTML={{ __html: part.content || '' }} />}
                
                {part?.sections?.map((sec: any, sIdx: number) => (
                  <div key={sec?.id || sIdx} className="mb-8">
                    {sec?.title && <h4 className="font-bold text-[16px] text-slate-700 mb-3">{sec.title}</h4>}
                    {sec?.imageUrl && <img src={sec.imageUrl} className="max-w-full mb-4 rounded-lg shadow-sm border border-slate-200" alt="Section Image" />}
                    {sec?.content && sec?.questionType !== "Điền từ" && sec?.questionType !== "Kéo thả vào Part" && (
                      <div className="prose prose-sm max-w-none text-slate-600 whitespace-pre-wrap leading-relaxed bg-white p-5 rounded-xl border border-slate-200 shadow-sm" dangerouslySetInnerHTML={{ __html: sec.content || '' }} />
                    )}
                  </div>
                ))}
              </div>
            ))}
          </div>
        </div>

        {/* THANH KÉO (SPLITTER) */}
        <div 
          onMouseDown={handleMouseDown}
          className="w-2 bg-slate-200 hover:bg-[#3498db] cursor-col-resize flex flex-col justify-center items-center transition-colors shrink-0 z-10 active:bg-[#2980b9]"
          title="Kéo để điều chỉnh độ rộng 2 bên"
        >
          <div className="flex flex-col gap-1">
            <div className="w-1 h-1 rounded-full bg-slate-400"></div>
            <div className="w-1 h-1 rounded-full bg-slate-400"></div>
            <div className="w-1 h-1 rounded-full bg-slate-400"></div>
          </div>
        </div>

        {/* CỘT PHẢI: QUESTIONS */}
        <div className="bg-[#eef2f6] overflow-y-auto custom-scrollbar scroll-smooth" id="questions-container" style={{ width: `${100 - leftWidth}%` }}>
           <div className="p-8">
             {parts?.map((part: any, pIdx: number) => (
                <div key={`qpane-${part?.id || pIdx}`}>
                   {part?.sections?.map((sec: any, sIdx: number) => (
                      <div key={`qsec-${sec?.id || sIdx}`} className="mb-10">
                         
                         {(sec?.questionType === "Điền từ" || sec?.questionType === "Kéo thả vào Part") && (
                           <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 mb-6">
                             {sec?.title && <h4 className="font-bold text-[16px] text-slate-800 mb-6">{sec.title}</h4>}
                             {sec?.imageUrl && <img src={sec.imageUrl} className="max-w-full mb-6 rounded-lg border border-slate-200" alt="Fill Image" />}
                             <div className="space-y-5 leading-[3] text-[16px] font-serif text-slate-800">
                               {renderInlineQuestion(sec?.content || '')}
                             </div>
                           </div>
                         )}

                         {sec?.questionType === "Trắc nghiệm" && sec?.questions?.map((q: any) => {
                            if (!q?.id) return null;
                            const correctAns = String(q.correctAnswer || '').trim().toUpperCase();
                            const userAns = String(answers[String(q.id)] || '').trim().toUpperCase();
                            const isQuestionCorrect = userAns === correctAns;
                            const displayIdx = questionIndexMap[String(q.id)] || q.id;

                            return (
                              <div key={q.id} id={`q-${q.id}`} className={`bg-white p-6 rounded-xl shadow-sm border transition-all mb-4 scroll-mt-20 relative group ${isReviewMode ? (isQuestionCorrect ? 'border-emerald-300 bg-emerald-50/20' : 'border-red-300 bg-red-50/20') : 'border-slate-200 hover:border-[#3ba1e2]/50'}`}>
                                 
                                 {!isReviewMode && (
                                    <button onClick={() => toggleMark(String(q.id))} className={`absolute top-5 right-5 transition-colors ${marked[String(q.id)] ? 'text-amber-400' : 'text-slate-200 hover:text-slate-400'}`}>
                                       <svg className="w-6 h-6" fill={marked[String(q.id)] ? "currentColor" : "none"} stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={marked[String(q.id)] ? 1 : 2} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" /></svg>
                                    </button>
                                 )}

                                 {isReviewMode && (
                                    <div className="absolute top-5 right-5 font-bold text-[12px]">
                                       {isQuestionCorrect ? <span className="text-emerald-700">✅ Đúng</span> : <span className="text-red-600">❌ Sai</span>}
                                    </div>
                                 )}

                                 <div className="font-bold text-slate-800 text-[15px] mb-3 pr-10">Question {displayIdx}:</div>
                                 {q.imageUrl && <img src={q.imageUrl} className="max-w-[80%] mb-4 rounded border border-slate-200" alt="Question Image" />}
                                 {q.content && <div className="text-[14px] text-slate-700 leading-relaxed whitespace-pre-wrap mb-5">{String(q.content)}</div>}
                                 
                                 <div className="space-y-3 pl-2">
                                    {q.options?.map((opt: any, i: number) => {
                                       const safeOpt = String(opt || '');
                                       const val = safeOpt.split('.')[0]?.trim().toUpperCase() || String.fromCharCode(65+i);
                                       const isSelected = userAns === val;
                                       const isCorrectOpt = correctAns === val;

                                       let circleStyle = 'border-slate-300 bg-white text-transparent';
                                       let textStyle = 'text-slate-600';

                                       if (isReviewMode) {
                                          if (isCorrectOpt) { circleStyle = 'border-emerald-500 bg-emerald-500 text-white'; textStyle = 'font-bold text-emerald-800'; }
                                          else if (isSelected) { circleStyle = 'border-red-500 bg-red-500 text-white'; textStyle = 'line-through text-red-600 opacity-70'; }
                                       } else {
                                          if (isSelected) { circleStyle = 'border-[#3ba1e2] bg-[#3ba1e2] text-white shadow-inner'; textStyle = 'font-bold text-[#3ba1e2]'; }
                                       }

                                       return (
                                          <label key={i} className={`flex items-start gap-3 transition-colors ${!isReviewMode ? 'cursor-pointer hover:bg-slate-50 p-1.5 -ml-1.5 rounded' : ''}`}>
                                             <input type="radio" name={`q-${q.id}`} value={val} checked={isSelected} onChange={() => handleAnswer(String(q.id), val)} disabled={isReviewMode} className="hidden" />
                                             <div className={`w-[20px] h-[20px] rounded-full border-2 flex items-center justify-center shrink-0 mt-0.5 transition-all ${circleStyle}`}>
                                                <div className={`w-2 h-2 rounded-full ${isSelected || isCorrectOpt ? 'bg-white' : 'bg-transparent'}`}></div>
                                             </div>
                                             <span className={`text-[14px] ${textStyle}`}>{safeOpt}</span>
                                          </label>
                                       );
                                    })}
                                 </div>

                                 {isReviewMode && q.explanation && (
                                    <div className="mt-6 pt-4 border-t border-slate-100 bg-amber-50/50 p-4 rounded-lg">
                                       <p className="text-[12px] font-black text-amber-600 uppercase mb-1">💡 Giải thích:</p>
                                       <p className="text-[13px] text-slate-700 font-medium whitespace-pre-wrap">{String(q.explanation)}</p>
                                    </div>
                                 )}
                              </div>
                            );
                         })}
                      </div>
                   ))}
                </div>
             ))}
             {(!parts || parts.length === 0) && (
               <div className="text-center py-20 text-slate-400 font-medium">Đề thi này chưa có nội dung.</div>
             )}
           </div>
        </div>

        {/* Modal Palette */}
        {showPalette && (
           <div className="absolute bottom-16 left-6 w-[360px] bg-white rounded-t-xl shadow-[0_-10px_40px_rgba(0,0,0,0.15)] border border-slate-200 flex flex-col max-h-[60vh] z-40 animate-in slide-in-from-bottom-4">
              <div className="p-4 border-b border-slate-100 flex justify-between items-center bg-slate-50 rounded-t-xl">
                 <h4 className="font-bold text-slate-700 text-sm">Danh sách câu hỏi</h4>
                 <button onClick={() => setShowPalette(false)} className="text-slate-400 hover:text-slate-700">✖</button>
              </div>
              <div className="flex gap-4 p-4 text-[11px] font-bold text-slate-500 border-b border-slate-100 justify-center">
                 <span className="flex items-center gap-1.5"><div className="w-3 h-3 rounded-full border border-slate-300"></div> Chưa làm</span>
                 <span className="flex items-center gap-1.5"><div className="w-3 h-3 rounded-full bg-[#3ba1e2]"></div> Đã làm</span>
                 <span className="flex items-center gap-1.5"><div className="w-3 h-3 rounded-full border-2 border-amber-400"></div> Đánh dấu</span>
              </div>
              <div className="p-5 overflow-y-auto custom-scrollbar flex-1">
                 <div className="grid grid-cols-5 gap-3">
                    {allQuestionIds.map(id => {
                       const isAns = answers[id] && answers[id].trim() !== '';
                       const isMark = marked[id];
                       let btnClass = 'bg-white border-slate-200 text-slate-600 hover:bg-slate-50';
                       
                       if (isReviewMode) {
                          const q = parts.flatMap((p: any) => p?.sections?.flatMap((s: any) => s?.questions) || []).find((q: any) => String(q?.id) === String(id));
                          const isCorrect = q && answers[id]?.trim().toUpperCase() === String(q.correctAnswer || '').trim().toUpperCase();
                          btnClass = isCorrect ? 'bg-emerald-50 border-emerald-400 text-emerald-600' : 'bg-red-50 border-red-400 text-red-600';
                       } else if (isAns) {
                          btnClass = 'bg-[#3ba1e2] border-[#3ba1e2] text-white';
                       }

                       return (
                          <button key={id} onClick={() => scrollToQuestion(id)} className={`h-10 w-full rounded-full border text-[13px] font-bold flex items-center justify-center transition-all ${btnClass} ${!isReviewMode && isMark ? 'ring-2 ring-amber-400 ring-offset-2' : ''}`}>
                             {questionIndexMap[id]}
                          </button>
                       )
                    })}
                 </div>
              </div>
           </div>
        )}
      </div>

      <footer className="h-16 bg-[#3498db] text-white flex justify-between items-center px-6 shrink-0 shadow-[0_-4px_10px_rgba(0,0,0,0.1)] z-30 relative">
        <div className="flex-1">
           <button onClick={() => setShowPalette(!showPalette)} className="bg-white text-[#3498db] font-bold px-5 py-2.5 rounded hover:bg-slate-50 transition shadow text-[13px] flex items-center gap-2">
             Bảng thống kê <span className="text-lg leading-none">☷</span>
           </button>
        </div>
        <div className="flex-1 flex justify-center items-center gap-2 font-black text-xl tracking-wider">
           ⏱ {formatTime(timeLeft)}
        </div>
        <div className="flex-1 flex justify-end">
           {isReviewMode ? (
              <button onClick={onFinish} className="bg-white text-slate-800 px-10 py-2.5 rounded font-black text-[14px] hover:bg-slate-100 transition shadow">THOÁT</button>
           ) : (
              <button onClick={handleFinish} className="bg-[#f1c40f] hover:bg-[#f39c12] text-slate-900 px-10 py-2.5 rounded font-black text-[14px] transition shadow">NỘP BÀI</button>
           )}
        </div>
      </footer>
    </div>
  );

  // ==========================================
  // VIEW 2: GIAO DIỆN LISTENING (CUỘN DỌC - SIDEBAR PHẢI)
  // ==========================================
  const renderListeningLayout = () => (
    <div className="flex flex-col h-screen bg-[#f4f6f8] font-sans text-slate-800 overflow-hidden">
      <header className={`px-6 py-3.5 flex justify-between items-center shrink-0 shadow-sm z-30 ${isReviewMode ? 'bg-emerald-600' : 'bg-white border-b border-slate-200'}`}>
        <div className="flex items-center gap-6">
          <h1 className={`font-bold text-[18px] tracking-wide truncate max-w-xs md:max-w-xl ${isReviewMode ? 'text-white' : 'text-slate-800'}`}>
            {isReviewMode ? `[REVIEW] ${basicInfo?.title}` : basicInfo?.title}
          </h1>
        </div>

        {globalAudio && (
          <div className="flex-1 max-w-lg mx-8 flex items-center justify-center">
            {isReviewMode ? (
              <audio controls src={globalAudio} className="h-10 w-full rounded outline-none" />
            ) : (
              <div className="flex items-center gap-3 bg-slate-100 px-5 py-2 rounded-full border border-slate-300">
                <span className="text-xl" title="Chỉnh âm lượng">🔊</span>
                <input type="range" min="0" max="1" step="0.05" defaultValue="1" onChange={(e) => { if(globalAudioRef.current) globalAudioRef.current.volume = parseFloat(e.target.value) }} className="w-40 accent-blue-500 cursor-pointer" />
              </div>
            )}
          </div>
        )}

        <button onClick={onBack} className={`font-bold text-[14px] flex items-center gap-2 border px-5 py-2 rounded transition shadow-sm ${isReviewMode ? 'text-white border-emerald-400 hover:bg-emerald-700' : 'text-slate-600 border-slate-300 hover:bg-slate-50 bg-white'}`}>
          ⚙ Thoát
        </button>
      </header>

      <div className="flex-1 overflow-y-auto custom-scrollbar w-full">
        <div className="max-w-[1400px] mx-auto w-full flex items-start gap-8 p-6 md:p-8">
          
          <div className="flex-1 w-full space-y-12">
            {parts?.map((part: any, pIdx: number) => {
              const hasPassage = part?.content && part.content.trim().length > 0;
              return (
                <div key={pIdx} className="w-full">
                  {!hasPassage && (
                    <div className="mb-6 max-w-3xl mx-auto">
                      {part?.title && <h2 className="font-bold text-[20px] text-slate-800">{part.title}</h2>}
                      {part?.imageUrl && <img src={part.imageUrl} className="max-w-full mt-4 rounded-lg shadow-sm border border-slate-200" alt="Part" />}
                    </div>
                  )}

                  <div className={`flex items-start gap-8 ${hasPassage ? 'flex-row' : 'flex-col max-w-3xl mx-auto'}`}>
                    {hasPassage && (
                      <div className="w-[45%] sticky top-2 h-[calc(100vh-120px)] overflow-y-auto custom-scrollbar pr-3">
                        <h2 className="font-bold text-[18px] text-slate-800 mb-3">{part.title}</h2>
                        {part?.imageUrl && <img src={part.imageUrl} className="max-w-full mb-4 rounded-lg shadow-sm" alt="Part" />}
                        <div className="prose prose-slate max-w-none text-justify leading-loose text-[16px] bg-white p-8 border border-slate-200 rounded-2xl shadow-sm">
                          <div dangerouslySetInnerHTML={{ __html: part.content || '' }} />
                        </div>
                      </div>
                    )}

                    <div className={`${hasPassage ? 'w-[55%] py-2' : 'w-full'}`}>
                      {part?.audioUrl && (!isListening || isReviewMode) && (
                        <div className="bg-white p-3 rounded-lg shadow-sm border border-slate-200 mb-8 flex items-center">
                          <audio src={part.audioUrl} controls className="w-full h-10 outline-none" controlsList="nodownload" />
                        </div>
                      )}

                      <div className="space-y-8">
                        {part?.sections?.map((sec: any, sIdx: number) => (
                          <div key={sIdx} className="space-y-6">
                            
                            {sec?.imageUrl && <img src={sec.imageUrl} className="max-w-full rounded-xl shadow-sm border border-slate-200" alt="Section" />}
                            
                            {(sec?.questionType === "Điền từ" || sec?.questionType === "Kéo thả vào Part") && (
                              <div className={`border p-8 rounded-2xl shadow-sm ${isReviewMode ? 'bg-white border-slate-300' : 'bg-white border-slate-200'}`}>
                                {sec?.title && <h4 className="font-bold text-[18px] mb-6">{sec.title}</h4>}
                                <div className="space-y-5 leading-[3] text-[16px] font-serif text-slate-800">
                                  {renderInlineQuestion(sec.content || '')}
                                </div>
                              </div>
                            )}

                            {sec?.questionType === "Trắc nghiệm" && sec?.questions?.map((q: any) => {
                              if (!q?.id) return null;
                              const correctAns = String(q.correctAnswer || '').trim().toUpperCase();
                              const userAns = String(answers[String(q.id)] || '').trim().toUpperCase();
                              const isQuestionCorrect = userAns === correctAns;
                              const displayIdx = questionIndexMap[String(q.id)] || q.id;

                              return (
                                <div key={q.id} id={`q-${q.id}`} className={`p-8 rounded-2xl border shadow-sm relative group scroll-mt-20 ${isReviewMode ? (isQuestionCorrect ? 'bg-emerald-50/30 border-emerald-200' : 'bg-red-50/30 border-red-200') : 'bg-white border-slate-200 hover:border-slate-300'}`}>
                                  {!isReviewMode && (
                                    <button onClick={() => toggleMark(String(q.id))} className={`absolute top-6 right-6 transition-colors ${marked[String(q.id)] ? 'text-amber-500' : 'text-slate-300 hover:text-slate-500'}`}>
                                      <svg className="w-7 h-7" fill={marked[String(q.id)] ? "currentColor" : "none"} stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={marked[String(q.id)] ? 1 : 2} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" /></svg>
                                    </button>
                                  )}
                                  {isReviewMode && (
                                    <div className="absolute top-6 right-6 font-bold text-[14px]">
                                      {isQuestionCorrect ? <span className="text-emerald-700 bg-emerald-100 px-3 py-1.5 rounded">✅ Đúng</span> : <span className="text-red-700 bg-red-100 px-3 py-1.5 rounded">❌ Sai</span>}
                                    </div>
                                  )}

                                  <div className="mb-6 pr-16">
                                    <div className="font-bold text-slate-800 text-[16px] mb-2">Question {displayIdx}:</div>
                                    {q.imageUrl && <img src={q.imageUrl} className="max-w-full mt-3 mb-4 rounded-lg shadow-sm border border-slate-200" alt="Question" />}
                                    {q.content && <div className="text-[16px] text-slate-800 leading-relaxed font-normal whitespace-pre-wrap">{String(q.content)}</div>}
                                  </div>
                                  
                                  {q.audioUrl && <audio src={q.audioUrl} controls className="w-full h-10 mb-6" />}
                                  
                                  <div className="space-y-4 ml-1">
                                    {q.options?.map((opt: any, i: number) => {
                                      const safeOpt = String(opt || '');
                                      const val = safeOpt.split('.')[0]?.trim().toUpperCase() || String.fromCharCode(65+i);
                                      const isSelected = userAns === val;
                                      const isCorrectOpt = correctAns === val;

                                      let optStyle = 'text-slate-700 hover:bg-slate-50';
                                      let ringStyle = 'bg-slate-50 border-slate-300';
                                      let showTick = false;

                                      if (isReviewMode) {
                                        if (isCorrectOpt) { optStyle = 'bg-emerald-100 border-emerald-500 text-emerald-900 font-bold'; ringStyle = 'bg-emerald-500 border-emerald-500 text-white'; showTick = true; } 
                                        else if (isSelected && !isCorrectOpt) { optStyle = 'bg-red-50 border-red-300 text-red-700 line-through opacity-70'; ringStyle = 'bg-red-500 border-red-500 text-white'; showTick = true; } 
                                        else { optStyle = 'opacity-50 text-slate-400'; }
                                      } else {
                                        if (isSelected) { optStyle = 'bg-blue-50 border-blue-500 text-blue-800 font-medium'; ringStyle = 'bg-[#3b82f6] border-[#3b82f6] text-white'; showTick = true; }
                                      }

                                      return (
                                        <label key={i} className={`flex items-start gap-4 p-3 -ml-3 rounded-lg transition border border-transparent ${optStyle} ${!isReviewMode ? 'cursor-pointer' : 'cursor-default'}`}>
                                          <input type="radio" name={`q-${q.id}`} value={val} checked={isSelected} onChange={() => handleAnswer(String(q.id), val)} className="hidden" disabled={isReviewMode} />
                                          <div className="pt-0.5">
                                            <div className={`w-[22px] h-[22px] rounded-full border flex items-center justify-center shrink-0 transition-colors shadow-sm ${ringStyle}`}>
                                              {showTick && <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20"><path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" /></svg>}
                                            </div>
                                          </div>
                                          <span className={`text-[16px] leading-relaxed`}>{safeOpt}</span>
                                        </label>
                                      );
                                    })}
                                  </div>

                                  {isReviewMode && q.explanation && (
                                    <div className="mt-8 pt-5 border-t border-slate-200">
                                      <p className="text-[14px] font-black text-amber-600 uppercase mb-2">💡 Giải thích đáp án:</p>
                                      <p className="text-[15px] text-slate-700 font-medium leading-relaxed whitespace-pre-wrap">{String(q.explanation)}</p>
                                    </div>
                                  )}
                                </div>
                              );
                            })}
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              );
            })}
            {(!parts || parts.length === 0) && (
              <div className="text-center py-20 text-slate-400 font-medium">Đề thi này chưa có nội dung.</div>
            )}
          </div>

          <aside className="w-[320px] shrink-0 sticky top-2 h-[calc(100vh-120px)] flex flex-col bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
            <div className="p-6 border-b border-slate-200 flex flex-col items-center">
              {isReviewMode ? (
                <div className="bg-emerald-50 text-emerald-700 p-5 rounded-xl border border-emerald-200 w-full text-center shadow-sm">
                  <p className="text-[13px] font-bold uppercase tracking-widest mb-2">Kết quả của bạn</p>
                  <p className="text-4xl font-black">{scoreResult.score} <span className="text-xl text-emerald-500">/ {scoreResult.total}</span></p>
                </div>
              ) : (
                <div className="bg-[#fee2e2] text-[#ef4444] px-6 py-3.5 rounded-lg font-bold text-[18px] mb-6 border border-[#fecaca] flex items-center justify-center gap-2 w-full shadow-sm">
                  ⏱ {formatTime(timeLeft)} phút
                </div>
              )}
              
              <div className="w-full text-[15px] font-bold text-slate-800 mb-4 mt-4">Danh sách câu hỏi</div>
              
              <div className="w-full grid grid-cols-2 gap-3 text-[13px] text-slate-600 mb-3">
                <div className="flex items-center gap-2"><div className="w-3.5 h-3.5 rounded-full bg-[#f1f5f9] border border-slate-300"></div> Chưa trả lời ({totalCount - answeredCount})</div>
                <div className="flex items-center gap-2"><div className="w-3.5 h-3.5 rounded-full bg-[#93c5fd]"></div> Đã trả lời ({answeredCount})</div>
              </div>
              {!isReviewMode && (
                <div className="w-full flex items-center gap-2 text-[13px] text-slate-600">
                  <div className="w-3.5 h-3.5 rounded-full border-2 border-amber-500 bg-transparent"></div> Đánh dấu ({markedCount})
                </div>
              )}
            </div>
            
            <div className="flex-1 overflow-y-auto p-6 custom-scrollbar bg-slate-50/50">
              <p className="text-[12px] text-slate-400 mb-4 italic text-center">Bấm vào ô để đến câu hỏi</p>
              <div className="grid grid-cols-4 gap-x-2 gap-y-3">
                {allQuestionIds.map(id => {
                  const isAns = answers[id] && answers[id].trim() !== '';
                  const isMarked = marked[id];
                  let btnStyle = 'bg-white border-slate-200 text-slate-500 hover:bg-slate-50'; 
                  if (isReviewMode) {
                    const q = parts.flatMap((p: any) => p?.sections?.flatMap((s: any) => s?.questions) || []).find((q: any) => String(q?.id) === String(id));
                    const isCorrect = q && answers[id]?.trim().toUpperCase() === String(q.correctAnswer || '').trim().toUpperCase();
                    btnStyle = isCorrect ? 'bg-emerald-100 border-emerald-400 text-emerald-700' : 'bg-red-100 border-red-400 text-red-700';
                  } else if (isAns) { btnStyle = 'bg-[#bfdbfe] border-[#93c5fd] text-blue-800'; }
                  return (
                    <button key={id} onClick={() => scrollToQuestion(id)} className={`relative h-10 flex items-center justify-center rounded-full text-[14px] font-bold transition-all border shadow-sm ${btnStyle} ${!isReviewMode && isMarked ? 'ring-2 ring-amber-400 ring-offset-1' : ''}`}>
                      {questionIndexMap[id]}
                    </button>
                  )
                })}
              </div>
            </div>

            <div className="p-6 border-t border-slate-200 bg-white">
              <button onClick={handleFinish} className={`w-full text-white font-bold py-4 rounded-xl transition shadow-md text-lg ${isReviewMode ? 'bg-emerald-600 hover:bg-emerald-700' : 'bg-[#3b82f6] hover:bg-[#2563eb]'}`}>
                {isReviewMode ? 'Thoát' : 'Nộp Bài'}
              </button>
            </div>
          </aside>

        </div>
      </div>
    </div>
  );

  return (
    <React.Fragment>
      {/* Ẩn Audio tải trước */}
      {isListening && globalAudio && !isReviewMode && (
        <audio ref={globalAudioRef} src={globalAudio} preload="auto" className="hidden" />
      )}

      {!testStarted ? (
        <div className="flex flex-col h-screen items-center justify-center bg-[#f4f6f8] font-sans">
          <div className="bg-white p-10 rounded-2xl shadow-lg text-center max-w-xl border border-slate-200 w-full">
            <div className="text-6xl mb-6">{isListening ? '🎧' : '📖'}</div>
            <h1 className="text-2xl font-black text-slate-800 mb-2">{basicInfo?.title}</h1>
            <p className="text-slate-500 mb-8 font-medium text-lg">Thời gian: {formatTime(parseInitialTime(basicInfo?.timeLimit))}</p>
            
            {isListening && (
              <div className="bg-amber-50 border border-amber-200 p-5 rounded-lg text-amber-700 text-[14px] font-medium mb-8 text-left leading-relaxed shadow-inner">
                <span className="font-bold">⚠️ LƯU Ý THI LISTENING:</span> File âm thanh sẽ <span className="font-bold underline">tự động phát</span> ngay khi bạn bấm nút Bắt Đầu.
              </div>
            )}

            <div className="flex gap-4 justify-center mt-4">
              <button onClick={onBack} className="px-8 py-3.5 rounded-lg font-bold text-slate-500 hover:bg-slate-100 border border-slate-300 transition text-lg">Quay lại</button>
              <button onClick={handleStartTest} className="bg-[#3ba1e2] hover:bg-blue-600 text-white font-bold px-10 py-3.5 rounded-lg shadow-lg transition text-lg">Bắt Đầu Làm Bài</button>
            </div>
          </div>
        </div>
      ) : (
        isListening ? renderListeningLayout() : renderReadingLayout()
      )}
    </React.Fragment>
  );
}