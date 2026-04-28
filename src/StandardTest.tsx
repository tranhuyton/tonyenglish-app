import React, { useState, useEffect, useRef } from 'react';
import './tailwind.css';

export default function StandardTest({ onBack, testData, onFinish }: { onBack: () => void, testData: any, onFinish: (res: any) => void }) {
  let safeData = testData;
  if (typeof testData === 'string') {
    try { safeData = JSON.parse(testData); } catch (e) { }
  }

  const data = safeData || { title: "Standard Test", parts: [], timeLimit: "60:00" };
  const isListening = data.skill === 'listening';
  const globalAudio = data.audioUrl || data.parts?.[0]?.audioUrl;

  const [testStarted, setTestStarted] = useState(false);
  const [isReviewMode, setIsReviewMode] = useState(false);
  const [scoreResult, setScoreResult] = useState({ score: 0, total: 0 });
  
  const globalAudioRef = useRef<HTMLAudioElement>(null);
  const isFinishingRef = useRef(false); // CÔNG TẮC KHÓA LƯU NHÁP KHI ĐÃ NỘP BÀI

  const [answers, setAnswers] = useState<Record<string, string>>(() => {
    const saved = localStorage.getItem(`std_ans_${data.testId}`);
    return saved ? JSON.parse(saved) : {};
  });

  const [marked, setMarked] = useState<Record<string, boolean>>(() => {
    const saved = localStorage.getItem(`std_mark_${data.testId}`);
    return saved ? JSON.parse(saved) : {};
  });

  // Tự động lưu nháp nếu chưa nộp bài
  useEffect(() => {
    if (!isReviewMode && !isFinishingRef.current) {
      localStorage.setItem(`std_ans_${data.testId}`, JSON.stringify(answers));
      localStorage.setItem(`std_mark_${data.testId}`, JSON.stringify(marked));
    }
  }, [answers, marked, data.testId, isReviewMode]);

  const handleAnswer = (qId: string, val: string) => { 
    if(!isReviewMode) setAnswers(prev => ({ ...prev, [qId]: val })); 
  };
  
  const toggleMark = (qId: string) => { 
    if(!isReviewMode) setMarked(prev => ({ ...prev, [qId]: !prev[qId] })); 
  };

  const handleFinish = () => {
    if (!isReviewMode) {
      if (!window.confirm("Bạn có chắc chắn muốn nộp bài?")) return;
      
      // BẬT CÔNG TẮC VÀ TIÊU HỦY NGAY LẬP TỨC BỘ NHỚ TẠM
      isFinishingRef.current = true;
      localStorage.removeItem(`std_ans_${data.testId}`);
      localStorage.removeItem(`std_mark_${data.testId}`);

      let score = 0;
      let total = 0;
      data.parts.forEach((p: any) => p.questionGroups?.forEach((g: any) => g.questions?.forEach((q: any) => {
        total++;
        if (answers[q.id]?.trim().toUpperCase() === q.correctAnswer?.trim().toUpperCase()) score++;
      })));
      setScoreResult({ score, total });
      setIsReviewMode(true);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      if (onFinish) onFinish({ score: scoreResult.score, total: scoreResult.total, testTitle: data.title });
      else onBack();
    }
  };

  const parseInitialTime = (str: string) => {
    if (!str) return 3600;
    const parts = String(str).replace(/[^0-9:]/g, '').split(':');
    return parts.length === 2 ? parseInt(parts[0]) * 60 + parseInt(parts[1]) : (parseInt(parts[0]) || 60) * 60;
  };

  const [timeLeft, setTimeLeft] = useState(() => parseInitialTime(data.timeLimit));
  
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
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
  };

  const allQuestionIds = data.parts.flatMap((p: any) => p.questionGroups?.flatMap((g: any) => g.questions?.map((q: any) => q.id) || []) || []);
  const answeredCount = Object.keys(answers).length;
  const markedCount = Object.values(marked).filter(Boolean).length;
  const totalCount = allQuestionIds.length;

  // --- CẬP NHẬT: GẠCH CHÂN DÍNH SÁT CHỮ CHO GAP FILL ---
  const renderInlineQuestion = (text: string) => {
    if (!text) return null;
    const parts = text.split(/(\[\d+\])/g);
    return parts.map((part, index) => {
      const match = part.match(/\[(\d+)\]/);
      if (match) {
        const qNum = match[1];
        const userAns = answers[qNum] || '';
        
        if (isReviewMode) {
          const qData = data.parts.flatMap((p: any) => p.questionGroups?.flatMap((g: any) => g.questions) || []).find((q: any) => q.id === qNum);
          const correctAns = qData?.correctAnswer || '';
          const isCorrect = userAns.trim().toUpperCase() === correctAns.trim().toUpperCase();
          
          return (
            <span key={index} className="relative inline-flex flex-col items-center align-top mx-1 mt-1">
              <span className={`px-2.5 py-0.5 text-[14px] font-bold text-white rounded shadow-sm border ${isCorrect ? 'bg-emerald-500 border-emerald-600' : 'bg-red-500 border-red-600'}`}>
                {qNum}. {userAns || '(trống)'}
              </span>
              {!isCorrect && (
                <span className="absolute top-full left-1/2 -translate-x-1/2 mt-1 text-[11px] text-emerald-800 font-bold bg-emerald-100 px-2 py-0.5 border border-emerald-300 rounded text-center whitespace-nowrap z-10 shadow-md">
                  ĐA: {correctAns}
                </span>
              )}
            </span>
          );
        }

        // Căn chỉnh baseline và ép lineHeight để vạch sát chữ
        return (
          <span key={index} id={`q-${qNum}`} className="inline-flex items-baseline mx-1">
            <span className="font-bold text-[15px] mr-1 text-slate-700">{qNum}.</span>
            <input 
              type="text" 
              className="w-28 border-b-[1.5px] border-slate-500 focus:outline-none focus:border-blue-600 bg-transparent text-center text-blue-700 font-bold px-1 text-[16px] pb-[1px]" 
              style={{ lineHeight: '1.2' }}
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
    if (globalAudioRef.current && isListening) {
      globalAudioRef.current.play().catch(e => {
        console.error("Autoplay blocked:", e);
        alert("Trình duyệt chặn phát âm thanh. Vui lòng bấm Bắt Đầu lại.");
      });
    }
  };

  return (
    <React.Fragment>
      {/* Ẩn Audio tải trước để sẵn sàng play không bị chặn */}
      {isListening && globalAudio && !isReviewMode && (
        <audio ref={globalAudioRef} src={globalAudio} preload="auto" className="hidden" />
      )}

      {!testStarted ? (
        <div className="flex flex-col h-screen items-center justify-center bg-[#f4f6f8] font-sans">
          <div className="bg-white p-10 rounded-2xl shadow-lg text-center max-w-xl border border-slate-200 w-full">
            <div className="text-6xl mb-6">{isListening ? '🎧' : '📖'}</div>
            <h1 className="text-2xl font-black text-slate-800 mb-2">{data.title}</h1>
            <p className="text-slate-500 mb-8 font-medium text-lg">Thời gian: {formatTime(parseInitialTime(data.timeLimit))}</p>
            
            {isListening && (
              <div className="bg-amber-50 border border-amber-200 p-5 rounded-lg text-amber-700 text-[14px] font-medium mb-8 text-left leading-relaxed shadow-inner">
                <span className="font-bold">⚠️ LƯU Ý THI LISTENING:</span> File âm thanh sẽ <span className="font-bold underline">tự động phát</span> ngay khi bạn bấm nút Bắt Đầu bên dưới. <br/><br/>Bạn chỉ có thể chỉnh âm lượng (Volume), KHÔNG THỂ tạm dừng hay tua lại.
              </div>
            )}

            <div className="flex gap-4 justify-center mt-4">
              <button onClick={onBack} className="px-8 py-3.5 rounded-lg font-bold text-slate-500 hover:bg-slate-100 border border-slate-300 transition text-lg">Quay lại</button>
              <button onClick={handleStartTest} className="bg-[#3b82f6] hover:bg-blue-700 text-white font-bold px-10 py-3.5 rounded-lg shadow-lg transition text-lg">Bắt Đầu Làm Bài</button>
            </div>
          </div>
        </div>
      ) : (

        <div className="flex flex-col h-screen bg-[#f4f6f8] font-sans text-slate-800 overflow-hidden">
          
          {/* HEADER CHÍNH */}
          <header className={`px-6 py-3.5 flex justify-between items-center shrink-0 shadow-sm z-30 ${isReviewMode ? 'bg-emerald-600' : 'bg-white border-b border-slate-200'}`}>
            <div className="flex items-center gap-6">
              <h1 className={`font-bold text-[18px] tracking-wide truncate max-w-xs md:max-w-xl ${isReviewMode ? 'text-white' : 'text-slate-800'}`}>
                {isReviewMode ? `[REVIEW] ${data.title}` : data.title}
              </h1>
            </div>

            {isListening && globalAudio && (
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
              ⚙ Cài đặt / Thoát
            </button>
          </header>

          {/* VÙNG LÀM BÀI CUỘN FULL MÀN HÌNH - SCROLLBAR NẰM SÁT LỀ PHẢI */}
          <div className="flex-1 overflow-y-auto custom-scrollbar w-full">
            
            {/* KHỐI TRUNG TÂM GOM SÁT 2 CỘT */}
            <div className="max-w-[1400px] mx-auto w-full flex items-start gap-8 p-6 md:p-8">
              
              {/* VÙNG BÀI LÀM (TRÁI/GIỮA) */}
              <div className="flex-1 w-full space-y-12">
                {data.parts.map((part: any, pIdx: number) => {
                  const hasPassage = part.passageContent && part.passageContent.trim().length > 0;

                  return (
                    <div key={pIdx} className="w-full">
                      
                      {/* Tiêu đề Part (nếu không có Passage) */}
                      {!hasPassage && (
                        <div className="mb-6 max-w-3xl mx-auto">
                          <h2 className="font-bold text-[20px] text-slate-800">{part.title}</h2>
                          {part.instructions && <p className="text-[16px] text-slate-600 mt-2">{part.instructions}</p>}
                        </div>
                      )}

                      {/* Flex chia 2 cột Passage & Questions */}
                      <div className={`flex items-start gap-8 ${hasPassage ? 'flex-row' : 'flex-col max-w-3xl mx-auto'}`}>
                        
                        {/* CỘT PASSAGE (CHỈ HIỆN KHI CÓ PASSAGE) */}
                        {hasPassage && (
                          <div className="w-[45%] sticky top-2 h-[calc(100vh-120px)] overflow-y-auto custom-scrollbar pr-3">
                            <h2 className="font-bold text-[18px] text-slate-800 mb-3">{part.title}</h2>
                            {part.instructions && <p className="text-[15px] text-slate-600 mb-5">{part.instructions}</p>}
                            <div className="prose prose-slate max-w-none text-justify leading-loose text-[16px] bg-white p-8 border border-slate-200 rounded-2xl shadow-sm">
                              {part.passageTitle && <h3 className="font-bold text-[20px] mb-6 text-slate-800">{part.passageTitle}</h3>}
                              <div dangerouslySetInnerHTML={{ __html: part.passageContent }} />
                            </div>
                          </div>
                        )}

                        {/* CỘT QUESTIONS */}
                        <div className={`${hasPassage ? 'w-[55%] py-2' : 'w-full'}`}>
                          
                          {/* Audio phụ cho Part nếu có */}
                          {part.audioUrl && (!isListening || isReviewMode) && (
                            <div className="bg-white p-3 rounded-lg shadow-sm border border-slate-200 mb-8 flex items-center">
                              <audio src={part.audioUrl} controls className="w-full h-10 outline-none" controlsList="nodownload" />
                            </div>
                          )}

                          {/* Render Nhóm câu hỏi */}
                          <div className="space-y-8">
                            {part.questionGroups?.map((group: any, gIdx: number) => (
                              <div key={gIdx} className="space-y-6">
                                
                                {group.type === "GAP_FILL" && (
                                  <div className={`border p-8 rounded-2xl shadow-sm ${isReviewMode ? 'bg-white border-slate-300' : 'bg-white border-slate-200'}`}>
                                    {group.boxTitle && <h4 className="font-bold text-[18px] mb-6">{group.boxTitle}</h4>}
                                    <div className="space-y-5 leading-[3] text-[16px] font-serif text-slate-800">
                                      {renderInlineQuestion(group.content)}
                                    </div>
                                  </div>
                                )}

                                {(group.type === "TFNG" || group.type === "MCQ") && group.questions?.map((q: any) => {
                                  const correctAns = q.correctAnswer?.trim().toUpperCase();
                                  const userAns = answers[q.id]?.trim().toUpperCase();
                                  const isQuestionCorrect = userAns === correctAns;

                                  return (
                                    <div key={q.id} id={`q-${q.id}`} className={`p-8 rounded-2xl border shadow-sm relative group ${isReviewMode ? (isQuestionCorrect ? 'bg-emerald-50/30 border-emerald-200' : 'bg-red-50/30 border-red-200') : 'bg-white border-slate-200 hover:border-slate-300'}`}>
                                      
                                      {!isReviewMode && (
                                        <button 
                                          onClick={() => toggleMark(q.id)}
                                          className={`absolute top-6 right-6 transition-colors ${marked[q.id] ? 'text-amber-500' : 'text-slate-300 hover:text-slate-500'}`}
                                        >
                                          <svg className="w-7 h-7" fill={marked[q.id] ? "currentColor" : "none"} stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={marked[q.id] ? 1 : 2} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" /></svg>
                                        </button>
                                      )}

                                      {isReviewMode && (
                                        <div className="absolute top-6 right-6 font-bold text-[14px]">
                                          {isQuestionCorrect ? <span className="text-emerald-700 bg-emerald-100 px-3 py-1.5 rounded">✅ Đúng</span> : <span className="text-red-700 bg-red-100 px-3 py-1.5 rounded">❌ Sai</span>}
                                        </div>
                                      )}

                                      {/* FORMAT CÂU HỎI CHUẨN MỚI */}
                                      <div className="mb-6 pr-16">
                                        <div className="font-bold text-slate-800 text-[16px] mb-2">Question {q.id}:</div>
                                        {q.text && <div className="text-[16px] text-slate-800 leading-relaxed font-normal">{q.text}</div>}
                                      </div>
                                      
                                      {q.imageUrl && (
                                        <img src={q.imageUrl} className="max-w-full rounded mb-6 max-h-[350px] object-contain border border-slate-200" />
                                      )}
                                      
                                      <div className="space-y-4 ml-1">
                                        {q.options?.map((opt: string, i: number) => {
                                          const val = opt.split('.')[0]?.trim().toUpperCase();
                                          const isSelected = userAns === val;
                                          const isCorrectOpt = correctAns === val;

                                          let optStyle = 'text-slate-700 hover:bg-slate-50';
                                          let ringStyle = 'bg-slate-50 border-slate-300';
                                          let showTick = false;

                                          if (isReviewMode) {
                                            if (isCorrectOpt) {
                                              optStyle = 'bg-emerald-100 border-emerald-500 text-emerald-900 font-bold';
                                              ringStyle = 'bg-emerald-500 border-emerald-500 text-white';
                                              showTick = true;
                                            } else if (isSelected && !isCorrectOpt) {
                                              optStyle = 'bg-red-50 border-red-300 text-red-700 line-through opacity-70';
                                              ringStyle = 'bg-red-500 border-red-500 text-white';
                                              showTick = true; 
                                            } else {
                                              optStyle = 'opacity-50 text-slate-400';
                                            }
                                          } else {
                                            if (isSelected) {
                                              optStyle = 'bg-blue-50 border-blue-500 text-blue-800 font-medium';
                                              ringStyle = 'bg-[#3b82f6] border-[#3b82f6] text-white';
                                              showTick = true;
                                            }
                                          }

                                          return (
                                            <label key={i} className={`flex items-start gap-4 p-3 -ml-3 rounded-lg transition border border-transparent ${optStyle} ${!isReviewMode ? 'cursor-pointer' : 'cursor-default'}`}>
                                              <input 
                                                type="radio" 
                                                name={`q-${q.id}`} 
                                                value={val}
                                                checked={isSelected}
                                                onChange={() => handleAnswer(q.id, val)}
                                                className="hidden"
                                                disabled={isReviewMode}
                                              />
                                              <div className="pt-0.5">
                                                <div className={`w-[22px] h-[22px] rounded-full border flex items-center justify-center shrink-0 transition-colors shadow-sm ${ringStyle}`}>
                                                  {showTick && (
                                                    <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                                                      <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                                                    </svg>
                                                  )}
                                                </div>
                                              </div>
                                              <span className={`text-[16px] leading-relaxed`}>{opt}</span>
                                            </label>
                                          );
                                        })}
                                      </div>

                                      {isReviewMode && (
                                        <div className="mt-8 pt-5 border-t border-slate-200">
                                          <p className="text-[14px] font-black text-amber-600 uppercase mb-2">💡 Giải thích đáp án:</p>
                                          <p className="text-[15px] text-slate-700 font-medium leading-relaxed whitespace-pre-wrap">
                                            {q.explanation || "Không có lời giải thích cho câu hỏi này."}
                                          </p>
                                        </div>
                                      )}

                                    </div>
                                  );
                                })}

                                {group.type === "MATCHING" && (
                                  <div className="p-8 rounded-2xl border border-slate-200 shadow-sm bg-white">
                                    {group.questions?.[0]?.options?.length > 0 && (
                                      <div className="mb-8">
                                        <p className="font-bold text-[16px] text-slate-800 mb-4 border-b pb-2">Danh sách đáp án:</p>
                                        <div className="space-y-2">
                                          {group.questions[0].options.map((opt: string, i: number) => (
                                            <p key={i} className="text-[15px] font-medium text-slate-700">{opt}</p>
                                          ))}
                                        </div>
                                      </div>
                                    )}
                                    
                                    <div className="space-y-6">
                                      {group.questions?.map((q: any) => {
                                        const correctAns = q.correctAnswer?.trim().toUpperCase();
                                        const userAns = answers[String(q.id)]?.trim().toUpperCase() || '';
                                        const isCorrect = userAns === correctAns;

                                        return (
                                          <div key={q.id} id={`q-${q.id}`} className={`p-5 rounded-xl border ${isReviewMode ? (isCorrect ? 'bg-emerald-50/50 border-emerald-200' : 'bg-red-50/50 border-red-200') : 'bg-slate-50 border-slate-200'}`}>
                                            <div className="mb-4">
                                              <div className="font-bold text-slate-800 text-[16px] mb-2">Question {q.id}:</div>
                                              {q.text && <div className="text-[16px] font-normal text-slate-800 leading-relaxed">{q.text}</div>}
                                            </div>
                                            
                                            <div className="relative max-w-sm">
                                              <select
                                                className={`w-full p-3 rounded-lg border appearance-none font-medium text-[15px] outline-none focus:ring-2 focus:ring-blue-400 ${isReviewMode ? (isCorrect ? 'bg-emerald-100 border-emerald-400 text-emerald-800' : 'bg-red-100 border-red-400 text-red-800') : 'bg-white border-slate-300 text-slate-700 cursor-pointer'}`}
                                                value={userAns}
                                                onChange={(e) => handleAnswer(String(q.id), e.target.value.toUpperCase())}
                                                disabled={isReviewMode}
                                              >
                                                <option value="" disabled>-- Chọn câu trả lời --</option>
                                                {group.questions[0].options?.map((opt:string, i:number) => {
                                                  const letter = opt.split('.')[0]?.trim().toUpperCase();
                                                  return <option key={i} value={letter}>{opt}</option>
                                                })}
                                              </select>
                                              
                                              {!isReviewMode && (
                                                <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-4 text-slate-500">
                                                  <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
                                                </div>
                                              )}
                                            </div>
                                            
                                            {isReviewMode && !isCorrect && (
                                              <p className="mt-3 text-[13px] font-bold text-emerald-700">✅ Đáp án đúng: {correctAns}</p>
                                            )}
                                          </div>
                                        );
                                      })}
                                    </div>
                                  </div>
                                )}

                              </div>
                            ))}
                          </div>
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* KHỐI SIDEBAR STICKY BÊN PHẢI */}
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
                        const q = data.parts.flatMap((p: any) => p.questionGroups?.flatMap((g: any) => g.questions) || []).find((q: any) => q.id === id);
                        const isCorrect = q && answers[id]?.trim().toUpperCase() === q.correctAnswer?.trim().toUpperCase();
                        btnStyle = isCorrect ? 'bg-emerald-100 border-emerald-400 text-emerald-700' : 'bg-red-100 border-red-400 text-red-700';
                      } else if (isAns) {
                        btnStyle = 'bg-[#bfdbfe] border-[#93c5fd] text-blue-800'; 
                      }
                      
                      return (
                        <button
                          key={id}
                          onClick={() => scrollToQuestion(id)}
                          className={`relative h-10 flex items-center justify-center rounded-full text-[14px] font-bold transition-all border shadow-sm ${btnStyle} ${!isReviewMode && isMarked ? 'ring-2 ring-amber-400 ring-offset-1' : ''}`}
                        >
                          {id}
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
      )}
    </React.Fragment>
  );
}