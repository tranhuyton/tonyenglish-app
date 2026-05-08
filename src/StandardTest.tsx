import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';
import './tailwind.css';

export default function StandardTest({ onBack, testData, onFinish }: { onBack: () => void, testData: any, onFinish: (res: any) => void }) {
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
  
  const isListening = String(basicInfo.skill || safeData?.test_type || '').toLowerCase().includes('listening');
  const globalAudio = basicInfo.audioUrl || parts[0]?.audioUrl;

  // 🚀 TỐI ƯU: Quét Audio 1 lần duy nhất
  const hasAnyAudio = useMemo(() => {
    let flag = !!globalAudio;
    if (!flag) {
      parts?.forEach((p: any) => {
        if (p?.audioUrl) flag = true;
        p?.sections?.forEach((s: any) => {
          if (s?.audioUrl) flag = true;
          s?.questions?.forEach((q: any) => { if (q?.audioUrl) flag = true; });
        });
      });
    }
    return flag;
  }, [parts, globalAudio]);

  const [testStarted, setTestStarted] = useState(false);
  const [isReviewMode, setIsReviewMode] = useState(false);
  const [scoreResult, setScoreResult] = useState({ score: 0, total: 0 });
  const [showPalette, setShowPalette] = useState(false); 
  
  const globalAudioRef = useRef<HTMLAudioElement>(null);
  const isFinishingRef = useRef(false);

  const [leftWidth, setLeftWidth] = useState(50); 
  const containerRef = useRef<HTMLDivElement>(null);
  const leftPaneRef = useRef<HTMLDivElement>(null);
  const rightPaneRef = useRef<HTMLDivElement>(null);

  // 🚀 TỐI ƯU KÉO THẢ: Can thiệp DOM trực tiếp, không làm lag React State (60 FPS)
  const handleMouseDown = (e: React.MouseEvent) => {
    e.preventDefault();
    document.body.style.cursor = 'col-resize';
    document.body.style.userSelect = 'none'; 
    
    const handleMouseMove = (moveEvent: MouseEvent) => {
      if (!containerRef.current || !leftPaneRef.current || !rightPaneRef.current) return;
      const containerRect = containerRef.current.getBoundingClientRect();
      const newWidth = ((moveEvent.clientX - containerRect.left) / containerRect.width) * 100;
      if (newWidth >= 25 && newWidth <= 75) {
        leftPaneRef.current.style.width = `${newWidth}%`;
        rightPaneRef.current.style.width = `${100 - newWidth}%`;
      }
    };

    const handleMouseUp = (upEvent: MouseEvent) => {
      document.body.style.cursor = 'default';
      document.body.style.userSelect = 'auto';
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);

      if (!containerRef.current) return;
      const containerRect = containerRef.current.getBoundingClientRect();
      let finalWidth = ((upEvent.clientX - containerRect.left) / containerRect.width) * 100;
      if (finalWidth < 25) finalWidth = 25;
      if (finalWidth > 75) finalWidth = 75;
      setLeftWidth(finalWidth); // Chỉ lưu lại 1 lần khi nhả chuột
    };

    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);
  };

  const [answers, setAnswers] = useState<Record<string, string>>(() => {
    try {
      const saved = localStorage.getItem(`std_ans_${safeData?.id}`);
      return saved ? JSON.parse(saved) : {};
    } catch (e) { return {}; }
  });

  const [marked, setMarked] = useState<Record<string, boolean>>(() => {
    try {
      const saved = localStorage.getItem(`standard_mark_${safeData?.id}`);
      return saved ? JSON.parse(saved) : {};
    } catch (e) { return {}; }
  });

  useEffect(() => {
    if (!isReviewMode && !isFinishingRef.current && safeData?.id) {
      localStorage.setItem(`std_ans_${safeData.id}`, JSON.stringify(answers));
      localStorage.setItem(`standard_mark_${safeData.id}`, JSON.stringify(marked));
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
        localStorage.removeItem(`standard_mark_${safeData.id}`);
        localStorage.removeItem(`standard_endtime_${safeData.id}`);
      }

      let score = 0; let total = 0;
      let questionTypeStats: Record<string, { correct: number, total: number }> = {};

      parts?.forEach((p: any) => {
        p?.sections?.forEach((s: any) => {
          const qType = s.questionType || 'Khác';
          if (!questionTypeStats[qType]) questionTypeStats[qType] = { correct: 0, total: 0 };

          // 🚀 CHẤM ĐIỂM CHÉO COMBO CHECKBOX
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
                 userAnsComboSet.forEach(ans => { if (correctAnsComboSet.has(ans)) comboPoints++; });
                 comboPoints = Math.min(comboPoints, combo.length); 
                 
                 score += comboPoints;
                 total += combo.length;
                 questionTypeStats[qType].correct += comboPoints;
                 questionTypeStats[qType].total += combo.length;
             });

          } else {
             s?.questions?.forEach((q: any) => {
               if (!q?.id) return;
               total++; questionTypeStats[qType].total++;
               const uAns = String(answers[String(q.id)] || '').trim().toUpperCase();
               const cAns = String(q.correctAnswer || '').trim().toUpperCase();
               if (uAns === cAns && cAns !== '') { score++; questionTypeStats[qType].correct++; }
             });
          }
        });
      });

      setScoreResult({ score, total });
      setIsReviewMode(true);
      setShowPalette(false);
      window.scrollTo({ top: 0, behavior: 'smooth' });

      try {
        const { data: { user } } = await supabase.auth.getUser();
        if (user) {
          const timeSpentSecs = parseInitialTime(basicInfo.timeLimit) - timeLeft;
          await supabase.from('test_results').insert([{
            user_id: user.id,
            course_id: safeData?.course_id || safeData?.content_json?.basicInfo?.courseId || null,
            test_title: basicInfo.title || safeData?.title || "Standard Test",
            test_type: safeData?.test_type || 'Standard',
            score: score, total_score: total,
            time_spent: timeSpentSecs > 0 ? timeSpentSecs : 0,
            details: { test_id: safeData?.id, userAnswers: answers, questionTypeStats: questionTypeStats }
          }]);
        }
      } catch (error) { console.error("Lỗi lưu kết quả thi:", error); }

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

  const getSavedEndTime = () => {
    if (!safeData?.id) return null;
    const saved = localStorage.getItem(`standard_endtime_${safeData.id}`);
    return saved ? parseInt(saved, 10) : null;
  };

  const [timeLeft, setTimeLeft] = useState(() => parseInitialTime(basicInfo.timeLimit));
  
  useEffect(() => {
    if (!testStarted || isReviewMode) return;
    const timer = setInterval(() => { 
        const currentEndTime = getSavedEndTime();
        if (currentEndTime) {
            const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
            setTimeLeft(remaining);
            if (remaining <= 0) {
                clearInterval(timer);
                alert("⏰ Hết giờ làm bài!");
                handleFinish();
            }
        } else { setTimeLeft(prev => prev - 1); }
    }, 1000);
    return () => clearInterval(timer);
  }, [testStarted, isReviewMode]);

  const formatTime = (sec: number) => {
    const m = Math.floor(sec / 60).toString().padStart(2, '0');
    const s = (sec % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  };

  const scrollToQuestion = (id: string) => {
    const el = document.getElementById(`q-${id}`);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      el.classList.add('ring-4', 'ring-[#0ea5e9]/40', 'rounded-xl');
      setTimeout(() => el.classList.remove('ring-4', 'ring-[#0ea5e9]/40', 'rounded-xl'), 1500);
    }
    setShowPalette(false);
  };

  // 🚀 TỐI ƯU HIỆU SUẤT: Gom các việc đếm câu hỏi vào useMemo để không bị re-render mỗi 1s
  const { allQuestionIds, questionIndexMap } = useMemo(() => {
    const ids: string[] = [];
    parts?.forEach((p: any) => {
      p?.sections?.forEach((s: any) => {
        if (s?.questionType === "Điền từ" || s?.questionType === "Kéo thả vào Part") {
          const matches = String(s?.content || s?.questions?.[0]?.content || '').match(/\[(\d+)\]/g);
          if (matches) {
            matches.forEach((m: string) => {
              const num = m.replace(/\D/g, '');
              if (!ids.includes(num)) ids.push(num);
            });
          }
        } else {
          s?.questions?.forEach((q: any) => {
            if (q?.id && !ids.includes(String(q.id))) ids.push(String(q.id));
          });
        }
      });
    });
    ids.sort((a, b) => parseInt(a) - parseInt(b));
    const map = ids.reduce((acc: any, id: string, idx: number) => { acc[id] = idx + 1; return acc; }, {});
    return { allQuestionIds: ids, questionIndexMap: map };
  }, [parts]);

  const { answeredCount, markedCount, totalCount } = useMemo(() => {
    return {
      answeredCount: Object.keys(answers).filter(k => answers[k] && answers[k].trim() !== '').length,
      markedCount: Object.values(marked).filter(Boolean).length,
      totalCount: allQuestionIds.length
    }
  }, [answers, marked, allQuestionIds]);

  // 🚀 HÀM DỌN RÁC HTML THỪA VÀ SỐ ĐẾM ĐẦU CÂU HỎI
  const getCleanQuestionText = (htmlContent: string) => {
    let txt = String(htmlContent || '').trim();
    txt = txt.replace(/^<p[^>]*>/i, '').replace(/<\/p>$/i, '').trim();
    txt = txt.replace(/^(<[^>]+>)*(Câu\s*\d+|\d+[\-\d]*)\s*[\.\):]?\s*(<\/[^>]+>)*\s*/i, '').trim();
    return txt;
  };

  // 🚀 HÀM DỌN RÁC OPTIONS ĐÁP ÁN (VD: Xóa chữ A. A. Đáp án)
  const getCleanOptionText = (opt: string, index: number) => {
    let cleanOpt = String(opt || '').replace(/^<p[^>]*>/i, '').replace(/<\/p>$/i, '').trim();
    const expectedLetter = String.fromCharCode(65 + index);
    const match = cleanOpt.match(/^(<[^>]+>)*([a-zA-Z])([\.\):]?)\s*(<\/[^>]+>)*\s*([\s\S]*)/i);
    if (match && match[2].toUpperCase() === expectedLetter) {
        if (match[3] !== '' || match[5] === '') return match[5].trim();
    }
    return cleanOpt;
  };

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
            <span key={index} className="relative inline-flex flex-col items-center align-top mx-1.5 mt-1 group">
              <span className={`px-2.5 py-0.5 text-[14px] font-bold text-white rounded-md shadow-sm border ${isCorrect ? 'bg-emerald-600 border-emerald-700' : 'bg-red-500 border-red-600'}`}>
                {displayIndex}. {userAns || '(trống)'}
              </span>
              {!isCorrect && (
                <span className="absolute top-full left-1/2 -translate-x-1/2 mt-1.5 text-[11px] text-emerald-800 font-bold bg-emerald-100 px-2 py-0.5 border border-emerald-300 rounded text-center whitespace-nowrap z-10 shadow-sm opacity-0 group-hover:opacity-100 transition-opacity">
                  ĐA: {correctAns}
                </span>
              )}
            </span>
          );
        }

        return (
          <span key={index} id={`q-${qNum}`} className="inline-flex items-center align-middle mx-1.5 scroll-mt-24">
            <span className="font-bold text-[14px] mr-1.5 text-slate-500">{displayIndex}.</span>
            <input 
              type="text" 
              className="w-28 border-b-[2px] border-slate-300 focus:outline-none focus:border-[#0ea5e9] bg-transparent text-center text-[#0ea5e9] font-bold px-1 text-[15px] pb-[1px] transition-colors" 
              value={userAns} 
              onChange={(e) => handleAnswer(qNum, e.target.value)} 
              autoComplete="off" 
              spellCheck="false"
            />
          </span>
        );
      }
      return <span key={index} dangerouslySetInnerHTML={{ __html: partText || '' }} />;
    });
  };

  const handleStartTest = () => {
    setTestStarted(true);
    let currentEndTime = getSavedEndTime();
    if (!currentEndTime) {
        const initialSeconds = parseInitialTime(basicInfo.timeLimit);
        currentEndTime = Date.now() + initialSeconds * 1000;
        if (safeData?.id) localStorage.setItem(`standard_endtime_${safeData.id}`, currentEndTime.toString());
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
        alert("Trình duyệt chặn phát âm thanh tự động. Vui lòng bấm Bắt Đầu lại.");
      });
    }
  };

  // ==========================================
  // GIAO DIỆN READING (SPLIT-SCREEN NGANG)
  // ==========================================
  const renderReadingLayout = () => (
    <div className="flex flex-col h-[100dvh] font-sans bg-[#f1f5f9] overflow-hidden text-slate-800">
      
      <header className={`h-[60px] border-b border-slate-200 flex justify-between items-center px-6 shrink-0 shadow-sm z-20 ${isReviewMode ? 'bg-emerald-700 text-white border-none' : 'bg-white text-slate-800'}`}>
        <div className="font-black text-[16px] flex items-center gap-3 uppercase tracking-tight">
          <span className={`text-xl ${isReviewMode ? 'opacity-100' : 'opacity-70'}`}>📖</span>
          <span className="truncate max-w-[200px] md:max-w-xl">{isReviewMode ? `[CHỮA BÀI] ${basicInfo?.title}` : basicInfo?.title}</span>
        </div>
        <div className="flex items-center gap-4">
          <button onClick={onBack} className={`text-[13px] font-bold px-4 py-2 rounded-lg transition-colors flex items-center gap-2 shadow-sm border ${isReviewMode ? 'bg-emerald-600 text-white border-emerald-500 hover:bg-emerald-800' : 'bg-white hover:bg-slate-50 text-slate-600 border-slate-200'}`}>
            Thoát
          </button>
        </div>
      </header>

      <div className="flex-1 flex overflow-hidden relative flex-col md:flex-row" ref={containerRef}>
        
        {/* PANEL TRÁI (BÀI ĐỌC) */}
        <div className="bg-white overflow-y-auto custom-scrollbar w-full md:w-auto" ref={leftPaneRef} style={{ width: window.innerWidth > 768 ? `${leftWidth}%` : '100%' }}>
          <div className="p-6 md:p-10">
            {isReviewMode && (
              <div className="bg-emerald-50 rounded-2xl shadow-sm border border-emerald-100 p-6 mb-8 text-center">
                 <h3 className="text-emerald-700 font-bold uppercase tracking-widest text-xs mb-2">Kết quả bài làm</h3>
                 <div className="text-5xl font-black text-emerald-600">{scoreResult.score} <span className="text-2xl text-emerald-400">/ {scoreResult.total}</span></div>
              </div>
            )}

            {parts?.map((part: any, pIdx: number) => (
              <div key={part?.id || pIdx} className="mb-12">
                {part?.title && <h3 className="font-black text-xl text-slate-800 mb-6 uppercase tracking-tight border-b-2 border-slate-800 pb-3">{part.title}</h3>}
                {part?.imageUrl && <img src={part.imageUrl} className="max-w-full mb-6 rounded-xl shadow-sm border border-slate-200" alt="Part Image" />}
                {part?.content && (
                  <div className="prose prose-slate max-w-none text-slate-800 text-[16px] leading-[1.9] whitespace-pre-wrap mb-8 text-justify bg-slate-50 p-6 md:p-8 rounded-2xl border border-slate-200 shadow-sm" dangerouslySetInnerHTML={{ __html: part.content || '' }} />
                )}
                
                {part?.sections?.map((sec: any, sIdx: number) => {
                  let displaySecTitle = sec.title;
                  if (displaySecTitle && /Questions?\s+\d+/i.test(displaySecTitle)) {
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
                      if (firstIdx && lastIdx) displaySecTitle = displaySecTitle.replace(/Questions?\s+\d+(-\d+)?/i, firstIdx === lastIdx ? `Question ${firstIdx}` : `Questions ${firstIdx}-${lastIdx}`);
                  }

                  return (
                    <div key={sec?.id || sIdx} className="mb-8">
                      {displaySecTitle && <h4 className="font-bold text-[15px] text-slate-800 bg-slate-100 border border-slate-200 inline-block px-4 py-1.5 rounded-lg mb-4">{displaySecTitle}</h4>}
                      {sec?.imageUrl && <img src={sec.imageUrl} className="max-w-full mb-4 rounded-xl shadow-sm border border-slate-200" alt="Section Image" />}
                      {sec?.content && sec?.questionType !== "Điền từ" && sec?.questionType !== "Kéo thả vào Part" && (
                        <div className="prose prose-sm max-w-none text-slate-700 whitespace-pre-wrap leading-relaxed bg-white p-5 rounded-xl border border-slate-200 shadow-sm" dangerouslySetInnerHTML={{ __html: sec.content || '' }} />
                      )}
                    </div>
                  )
                })}
              </div>
            ))}
          </div>
        </div>

        {/* THANH KÉO THẢ RESIZER (Ẩn trên Mobile) */}
        <div 
          onMouseDown={handleMouseDown}
          className="hidden md:flex w-2.5 bg-slate-100 hover:bg-[#0ea5e9] cursor-col-resize flex-col justify-center items-center transition-colors shrink-0 z-10 border-x border-slate-200 group shadow-sm active:bg-blue-600"
          title="Kéo để điều chỉnh độ rộng"
        >
          <div className="flex flex-col gap-1.5 opacity-40 group-hover:opacity-100 transition-opacity">
            <div className="w-1 h-1 rounded-full bg-slate-600 group-hover:bg-white"></div>
            <div className="w-1 h-1 rounded-full bg-slate-600 group-hover:bg-white"></div>
            <div className="w-1 h-1 rounded-full bg-slate-600 group-hover:bg-white"></div>
          </div>
        </div>

        {/* PANEL PHẢI (CÂU HỎI) */}
        <div className="bg-[#f8fafc] overflow-y-auto custom-scrollbar scroll-smooth w-full md:w-auto" id="questions-container" ref={rightPaneRef} style={{ width: window.innerWidth > 768 ? `${100 - leftWidth}%` : '100%' }}>
           <div className="p-6 md:p-10 max-w-3xl mx-auto">
             {parts?.map((part: any, pIdx: number) => (
                <div key={`qpane-${part?.id || pIdx}`}>
                   {part?.sections?.map((sec: any, sIdx: number) => {
                      
                      let displaySecTitle = sec.title;
                      if (displaySecTitle && /Questions?\s+\d+/i.test(displaySecTitle)) {
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
                          if (firstIdx && lastIdx) displaySecTitle = displaySecTitle.replace(/Questions?\s+\d+(-\d+)?/i, firstIdx === lastIdx ? `Question ${firstIdx}` : `Questions ${firstIdx}-${lastIdx}`);
                      }

                      return (
                      <div key={`qsec-${sec?.id || sIdx}`} className="mb-12">
                         {displaySecTitle && <div className="bg-slate-200/60 border border-slate-300 px-4 py-2 mb-4 rounded-lg inline-block"><h4 className="font-bold text-[14px] text-slate-800">{displaySecTitle}</h4></div>}
                         
                         {(sec?.questionType === "Điền từ" || sec?.questionType === "Kéo thả vào Part") && (
                           <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 mb-6">
                             {sec?.imageUrl && <img src={sec.imageUrl} className="max-w-full mb-6 rounded-lg border border-slate-200" alt="Fill Image" />}
                             <div className="space-y-5 leading-[2.5] text-[16px] text-slate-800 text-justify">
                               {renderInlineQuestion(sec?.content || '')}
                             </div>
                           </div>
                         )}

                         {(sec?.questionType === "Trắc nghiệm" || sec?.questionType === "TFNG") && sec?.questions?.map((q: any) => {
                            if (!q?.id) return null;
                            const cleanQText = getCleanQuestionText(q.content);
                            const correctAns = String(q.correctAnswer || '').trim().toUpperCase();
                            const userAns = String(answers[String(q.id)] || '').trim().toUpperCase();
                            const isQuestionCorrect = userAns === correctAns;
                            const displayIdx = questionIndexMap[String(q.id)] || q.id;
                            
                            const isTFNG = sec?.questionType === "TFNG" || q.options?.some((opt: string) => ['TRUE', 'FALSE', 'NOT GIVEN', 'YES', 'NO'].includes(opt?.trim()?.toUpperCase()));

                            if (isTFNG) {
                               return (
                                 <div key={q.id} id={`q-${q.id}`} className={`bg-white p-6 rounded-2xl shadow-sm border transition-all mb-4 scroll-mt-20 relative group ${isReviewMode ? (isQuestionCorrect ? 'border-emerald-300 bg-emerald-50/20' : 'border-red-300 bg-red-50/20') : 'border-slate-200 hover:border-[#0ea5e9]/50'}`}>
                                   {!isReviewMode && (
                                     <button onClick={() => toggleMark(String(q.id))} className={`absolute top-5 right-5 transition-colors ${marked[String(q.id)] ? 'text-amber-500' : 'text-slate-200 hover:text-slate-400'}`}>
                                        <svg className="w-6 h-6" fill={marked[String(q.id)] ? "currentColor" : "none"} stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={marked[String(q.id)] ? 2 : 1.5} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" /></svg>
                                     </button>
                                   )}
                                   {isReviewMode && (<div className="absolute top-5 right-5 font-bold text-[12px]">{isQuestionCorrect ? <span className="text-emerald-700 bg-emerald-100 px-3 py-1 rounded-md">✅ Đúng</span> : <span className="text-red-700 bg-red-100 px-3 py-1 rounded-md">❌ Sai</span>}</div>)}

                                   <div className="flex gap-4 mb-2">
                                     <span className="font-bold text-slate-800 shrink-0 w-6 text-right pt-[2px]">{displayIdx}.</span>
                                     <div className="flex-1">
                                       {q.imageUrl && <img src={q.imageUrl} className="max-w-[80%] mb-4 rounded border border-slate-200" alt="Question" />}
                                       {cleanQText && <div className="text-[16px] text-slate-800 font-medium leading-relaxed whitespace-pre-wrap mb-4" dangerouslySetInnerHTML={{ __html: cleanQText }} />}
                                       
                                       <div className="flex flex-row flex-wrap gap-4">
                                         {q.options?.map((opt: string, i: number) => {
                                            const safeOpt = String(opt || '');
                                            const val = safeOpt.trim().toUpperCase();
                                            const isSelected = userAns === val;
                                            const isCorrectOpt = correctAns === val;

                                            let labelStyle = "flex items-center gap-2 p-1.5 transition rounded-lg border border-transparent";
                                            if (isReviewMode) {
                                               if (isCorrectOpt) labelStyle += " font-bold text-emerald-800 bg-emerald-100 border-emerald-300";
                                               else if (isSelected) labelStyle += " text-red-600 line-through opacity-70 bg-red-50 border-red-200";
                                               else labelStyle += " opacity-50";
                                            } else {
                                               labelStyle += " cursor-pointer hover:bg-slate-50 hover:border-slate-200";
                                            }

                                            return (
                                               <label key={i} className={labelStyle}>
                                                  <input type="radio" name={`q-${q.id}`} value={val} checked={isSelected} onChange={() => handleAnswer(String(q.id), val)} disabled={isReviewMode} className="w-4 h-4 accent-[#0ea5e9] cursor-pointer" />
                                                  <span className="text-[15px] font-semibold" dangerouslySetInnerHTML={{ __html: safeOpt }} />
                                               </label>
                                            );
                                         })}
                                       </div>
                                       {isReviewMode && q.explanation && (
                                         <div className="mt-6 pt-4 border-t border-slate-100"><p className="text-[12px] font-black text-amber-600 uppercase mb-2">💡 Giải thích:</p><div className="text-[14px] text-slate-700 italic leading-relaxed" dangerouslySetInnerHTML={{ __html: String(q.explanation) }} /></div>
                                       )}
                                     </div>
                                   </div>
                                 </div>
                               );
                            }

                            return (
                              <div key={q.id} id={`q-${q.id}`} className={`bg-white p-6 md:p-8 rounded-2xl shadow-sm border transition-all mb-4 scroll-mt-20 relative group ${isReviewMode ? (isQuestionCorrect ? 'bg-emerald-50/20 border-emerald-200' : 'bg-red-50/20 border-red-200') : 'hover:border-[#0ea5e9]/50 border-slate-200'}`}>
                                 {!isReviewMode && (
                                    <button onClick={() => toggleMark(String(q.id))} className={`absolute top-6 right-6 transition-colors ${marked[String(q.id)] ? 'text-amber-500' : 'text-slate-200 hover:text-slate-400'}`}>
                                       <svg className="w-7 h-7" fill={marked[String(q.id)] ? "currentColor" : "none"} stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={marked[String(q.id)] ? 2 : 1.5} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" /></svg>
                                    </button>
                                 )}
                                 {isReviewMode && (
                                    <div className="absolute top-6 right-6 font-bold text-[12px]">
                                       {isQuestionCorrect ? <span className="text-emerald-700 bg-emerald-100 px-3 py-1 rounded-md">✅ Đúng</span> : <span className="text-red-700 bg-red-100 px-3 py-1 rounded-md">❌ Sai</span>}
                                    </div>
                                 )}

                                 <div className="flex gap-4 mb-5 pr-10 items-start">
                                    <span className="font-bold text-white bg-slate-800 px-2 py-0.5 rounded text-[13px] mt-0.5">{displayIdx}</span>
                                    <div className="flex-1 w-full">
                                       {q.imageUrl && <img src={q.imageUrl} className="max-w-[80%] mb-4 rounded-xl border border-slate-200" alt="Question Image" />}
                                       {cleanQText && <div className="text-[16px] text-slate-800 leading-relaxed font-medium mb-3" dangerouslySetInnerHTML={{ __html: cleanQText }} />}
                                    </div>
                                 </div>
                                 
                                 <div className="flex flex-col gap-2 pl-10">
                                    {q.options?.map((opt: any, i: number) => {
                                       const cleanOpt = getCleanOptionText(opt, i);
                                       const val = String.fromCharCode(65+i);
                                       const isSelected = userAns === val;
                                       const isCorrectOpt = correctAns === val;

                                       let labelStyle = "flex items-start gap-4 p-3 rounded-xl transition-colors border border-transparent";
                                       let circleStyle = "border-slate-300 bg-white";
                                       let textStyle = "text-slate-800";
                                       
                                       if (isReviewMode) {
                                          if (isCorrectOpt) { labelStyle += " bg-emerald-50 border-emerald-200"; circleStyle = "border-emerald-500 bg-emerald-500 text-white"; textStyle = "font-bold text-emerald-900"; }
                                          else if (isSelected) { labelStyle += " bg-red-50 border-red-200"; circleStyle = "border-red-500 bg-red-500 text-white"; textStyle = "line-through text-red-700 opacity-70"; }
                                       } else {
                                          labelStyle += " cursor-pointer hover:bg-slate-50";
                                          if (isSelected) { labelStyle += " bg-blue-50/50 border-blue-200"; circleStyle = "border-[#0ea5e9] bg-[#0ea5e9] text-white shadow-inner"; textStyle = "font-bold text-[#0ea5e9]"; }
                                       }

                                       return (
                                          <label key={i} className={labelStyle}>
                                             <input type="radio" name={`q-${q.id}`} value={val} checked={isSelected} onChange={() => handleAnswer(String(q.id), val)} disabled={isReviewMode} className="hidden" />
                                             <div className="pt-0.5">
                                                <div className={`w-[22px] h-[22px] rounded-full border-2 flex items-center justify-center shrink-0 transition-colors shadow-sm ${circleStyle}`}>
                                                   {(isSelected || isCorrectOpt) && <div className="w-2 h-2 rounded-full bg-white"></div>}
                                                </div>
                                             </div>
                                             <span className={`text-[16px] leading-relaxed ${textStyle}`}><span className="font-bold mr-2">{val}.</span> <span dangerouslySetInnerHTML={{ __html: cleanOpt }} /></span>
                                          </label>
                                       );
                                    })}
                                 </div>

                                 {isReviewMode && q.explanation && (
                                    <div className="mt-8 pt-5 border-t border-slate-200 ml-10">
                                       <p className="text-[12px] font-black text-amber-600 uppercase mb-2">💡 Giải thích:</p>
                                       <div className="text-[14px] text-slate-700 font-medium whitespace-pre-wrap italic" dangerouslySetInnerHTML={{ __html: String(q.explanation) }} />
                                    </div>
                                 )}
                              </div>
                            );
                         })}

                         {sec?.questionType === "Droplist" && (
                           <div className="space-y-4">
                             {sec?.questions?.map((q: any) => {
                               if (!q?.id) return null;
                               const cleanQText = getCleanQuestionText(q.content);
                               const correctAns = String(q.correctAnswer || '').trim().toUpperCase();
                               const userAns = String(answers[String(q.id)] || '').trim().toUpperCase();
                               const isQuestionCorrect = userAns === correctAns;
                               const displayIdx = questionIndexMap[String(q.id)] || q.id;
                               
                               const otherSelectedAnswers = sec.questions
                                   .filter((otherQ: any) => otherQ.id !== q.id)
                                   .map((otherQ: any) => String(answers[String(otherQ.id)] || '').trim().toUpperCase())
                                   .filter((ans: string) => ans !== '');

                               return (
                                  <div key={q.id} id={`q-${q.id}`} className={`bg-white p-5 rounded-2xl shadow-sm border flex flex-col sm:flex-row gap-4 items-center mb-4 transition-all scroll-mt-20 ${isReviewMode ? (isQuestionCorrect ? 'border-emerald-300 bg-emerald-50/30' : 'border-red-300 bg-red-50/30') : 'border-slate-200 hover:border-[#0ea5e9]/40'}`}>
                                     <div className="font-bold text-white bg-slate-800 px-2 py-0.5 rounded text-[13px] shrink-0">{displayIdx}</div>
                                     <div className="flex-1 text-[15px] text-slate-800 line-clamp-2" dangerouslySetInnerHTML={{ __html: cleanQText }} />
                                     <div className="shrink-0">
                                        {isReviewMode ? (
                                           <div className="flex flex-col items-end gap-1">
                                              <div className={`px-4 py-1.5 rounded-lg font-bold text-[14px] border ${isQuestionCorrect ? 'bg-emerald-100 text-emerald-800 border-emerald-300' : 'bg-red-100 text-red-800 border-red-300'}`}>
                                                 {userAns || '(chưa chọn)'}
                                              </div>
                                              {!isQuestionCorrect && <div className="text-[11px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 shadow-sm">ĐA: {correctAns}</div>}
                                           </div>
                                        ) : (
                                           <select 
                                              className="border-2 border-slate-300 bg-white hover:bg-slate-50 focus:border-[#0ea5e9] rounded-xl px-4 py-2.5 outline-none font-bold text-slate-700 min-w-[150px] cursor-pointer text-[14px] text-center shadow-sm transition-colors"
                                              style={{ textAlignLast: 'center' }}
                                              value={userAns}
                                              onChange={(e) => handleAnswer(String(q.id), e.target.value)}
                                           >
                                              <option value="" disabled className="text-slate-400 font-normal">-- Chọn đáp án --</option>
                                              {q.options?.map((opt: any, i: number) => {
                                                 const val = String(opt || '').trim().toUpperCase();
                                                 const isDisabled = otherSelectedAnswers.includes(val);
                                                 return <option key={i} value={val} disabled={isDisabled} className="text-slate-800">{val} {isDisabled ? '(Đã chọn)' : ''}</option>
                                              })}
                                           </select>
                                        )}
                                     </div>
                                  </div>
                               )
                             })}
                           </div>
                         )}

                         {/* 🚀 THUẬT TOÁN COMBO CHECKBOX ĐỘC LẬP TỰ ĐỘNG GOM NHÓM */}
                         {sec?.questionType === "Checkbox" && (
                            <div className="space-y-6">
                              {(() => {
                                  const combos: any[][] = [];
                                  sec.questions?.forEach((q: any) => {
                                      const rawText = String(q.content || '').replace(/<[^>]*>/g, '').trim();
                                      const hasRealContent = rawText !== '' || String(q.content || '').includes('<img') || String(q.content || '').includes('<audio');
                                      if (combos.length === 0 || hasRealContent) combos.push([q]);
                                      else combos[combos.length - 1].push(q);
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

                                      let containerClass = "bg-white p-6 md:p-8 rounded-2xl shadow-sm border transition-colors relative group scroll-mt-20 mb-4 ";
                                      if (isReviewMode) {
                                          if (isPerfect) containerClass += "border-emerald-300 bg-emerald-50/30";
                                          else if (isPartial) containerClass += "border-amber-300 bg-amber-50/30";
                                          else containerClass += "border-red-300 bg-red-50/30";
                                      } else {
                                          containerClass += "border-slate-200 hover:border-[#0ea5e9]/40";
                                      }

                                      const handleComboChange = (optionValue: string, isChecked: boolean) => {
                                          setAnswers(prev => {
                                              let currentSelected = Array.from(new Set(comboIds.map(id => prev[id]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase()))));
                                              
                                              if (isChecked) {
                                                  if (currentSelected.length >= maxAllowed) {
                                                      alert(`Đề bài yêu cầu chọn tối đa ${maxAllowed} đáp án. Vui lòng bỏ chọn bớt trước khi tick cái mới.`);
                                                      return prev;
                                                  }
                                                  if (!currentSelected.includes(optionValue)) currentSelected.push(optionValue);
                                              } else {
                                                  currentSelected = currentSelected.filter((v:string) => v !== optionValue);
                                              }
                                              
                                              const next = { ...prev };
                                              comboIds.forEach((id, idx) => { next[id] = currentSelected[idx] || ''; }); 
                                              return next;
                                          });
                                      };

                                      const qText = getCleanQuestionText(combo[0]?.content);
                                      const firstQIdx = questionIndexMap[comboIds[0]] || comboIds[0];
                                      const lastQIdx = questionIndexMap[comboIds[comboIds.length - 1]] || comboIds[comboIds.length - 1];
                                      const displayIndexText = comboIds.length > 1 ? `Câu ${firstQIdx}-${lastQIdx}` : `Câu ${firstQIdx}`;

                                      return (
                                         <div key={`combo-${comboIndex}`} id={`q-${combo[0].id}`} className={containerClass}>
                                           
                                           {!isReviewMode && (
                                              <button onClick={() => toggleMark(String(combo[0].id))} className={`absolute top-6 right-6 transition-colors ${marked[String(combo[0].id)] ? 'text-amber-500' : 'text-slate-300 hover:text-slate-400'}`}>
                                                 <svg className="w-6 h-6" fill={marked[String(combo[0].id)] ? "currentColor" : "none"} stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={marked[String(combo[0].id)] ? 2 : 1.5} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" /></svg>
                                              </button>
                                           )}
                                           {isReviewMode && (
                                              <div className="absolute top-6 right-6 font-bold text-[12px]">
                                                 {isPerfect ? <span className="text-emerald-700 bg-emerald-100 px-3 py-1.5 rounded-lg">✅ Đúng hết</span> 
                                                 : isPartial ? <span className="text-amber-700 bg-amber-100 px-3 py-1.5 rounded-lg">⚠️ 1 phần</span>
                                                 : <span className="text-red-700 bg-red-100 px-3 py-1.5 rounded-lg">❌ Sai hết</span>}
                                              </div>
                                           )}

                                           <div className="flex flex-col mb-4 pr-16">
                                             <div className="font-bold text-white bg-slate-800 inline-block px-3 py-1 rounded w-fit text-[14px] mb-4">{displayIndexText}</div>
                                             
                                             {qText && <div className="text-[16px] font-medium leading-relaxed text-slate-800 mb-2 whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: qText }} />}
                                             
                                             <div className={`flex flex-col gap-2.5 mt-2`}>
                                               {validOptions.map((opt: any, i: number) => {
                                                 const cleanOpt = getCleanOptionText(opt, i);
                                                 const optionValue = String.fromCharCode(65+i); 
                                                 const isSelected = userAnsArr.includes(optionValue); 
                                                 const isCorrectOpt = correctAnsComboSet.has(optionValue);
                                                 
                                                 let labelClass = "flex items-start gap-4 p-3 rounded-xl transition-colors border border-transparent ";
                                                 if (isReviewMode) { 
                                                     if (isCorrectOpt && isSelected) labelClass += " bg-emerald-50 border-emerald-400 font-bold text-emerald-900"; 
                                                     else if (isCorrectOpt && !isSelected) labelClass += " bg-amber-50 border-amber-300 font-bold text-amber-800"; 
                                                     else if (isSelected && !isCorrectOpt) labelClass += " bg-red-50 border-red-300 text-red-700 line-through opacity-70";
                                                     else labelClass += " opacity-50"; 
                                                 } else { 
                                                     labelClass += " cursor-pointer hover:bg-slate-50"; 
                                                     if (isSelected) labelClass += " bg-blue-50/50 border-[#0ea5e9]/40";
                                                 }
                                                 return (
                                                   <label key={i} className={labelClass}>
                                                     <input type="checkbox" checked={isSelected} onChange={(e) => handleComboChange(optionValue, e.target.checked)} className="mt-1 w-5 h-5 accent-[#0ea5e9] rounded cursor-pointer shrink-0" disabled={isReviewMode} />
                                                     <span className="text-[16px] leading-relaxed text-slate-800"><span className="font-bold mr-2">{optionValue}.</span> <span dangerouslySetInnerHTML={{ __html: cleanOpt }} /></span>
                                                   </label>
                                                 )
                                               })}
                                             </div>
                                           </div>

                                           {isReviewMode && (
                                             <div className="mt-8 pt-5 border-t border-slate-200">
                                                <p className="text-[13px] font-black text-amber-600 uppercase mb-3">💡 Giải thích đáp án:</p>
                                                {combo.map((q:any) => {
                                                    if (!q.explanation || String(q.explanation).trim() === '') return null;
                                                    return (
                                                        <div key={q.id} className="text-[14px] text-slate-700 font-medium leading-relaxed mb-3 last:mb-0 border-l-[3px] border-slate-300 pl-4 bg-slate-50 py-3 pr-3 rounded-r-xl italic">
                                                            <span className="font-bold text-white px-2 py-0.5 bg-slate-800 rounded text-[12px] mr-2 font-sans not-italic">Câu {questionIndexMap[String(q.id)] || q.id}</span>
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
                   );})}
                </div>
             ))}
             {(!parts || parts.length === 0) && (
               <div className="text-center py-20 text-slate-400 font-medium text-lg">Đề thi này chưa có nội dung.</div>
             )}
           </div>
        </div>

        {/* BẢNG PALETTE ĐIỀU HƯỚNG CÂU HỎI (MOBILE) */}
        {showPalette && (
           <div className="absolute bottom-20 right-4 md:right-auto md:left-6 w-[340px] bg-white rounded-2xl shadow-2xl border border-slate-200 flex flex-col max-h-[60vh] z-40 animate-in slide-in-from-bottom-4">
              <div className="p-5 border-b border-slate-100 flex justify-between items-center bg-slate-50 rounded-t-2xl">
                 <h4 className="font-black text-slate-800 text-[14px] uppercase tracking-wide">Danh sách câu hỏi</h4>
                 <button onClick={() => setShowPalette(false)} className="w-8 h-8 flex items-center justify-center rounded-full bg-slate-200 text-slate-500 hover:bg-slate-300 transition-colors">✖</button>
              </div>
              <div className="flex gap-4 p-4 text-[11px] font-bold text-slate-500 border-b border-slate-100 justify-center bg-white">
                 <span className="flex items-center gap-1.5"><div className="w-3.5 h-3.5 rounded bg-slate-100 border border-slate-300"></div> Chưa làm</span>
                 <span className="flex items-center gap-1.5"><div className="w-3.5 h-3.5 rounded bg-[#0ea5e9]"></div> Đã làm</span>
                 <span className="flex items-center gap-1.5"><div className="w-3.5 h-3.5 rounded border-2 border-amber-400"></div> Note</span>
              </div>
              <div className="p-5 overflow-y-auto custom-scrollbar flex-1 bg-slate-50/50">
                 <div className="grid grid-cols-5 gap-3">
                    {allQuestionIds.map(id => {
                       let isAns = answers[id] && answers[id].trim() !== '';
                       const isMark = marked[id];
                       let btnClass = 'bg-white border-slate-200 text-slate-600 hover:border-[#0ea5e9] hover:text-[#0ea5e9] shadow-sm';
                       
                       const section = parts.flatMap((p: any) => p.sections || []).find((s:any) => s.questions?.some((sq:any)=>String(sq.id)===id));
                       const qType = section?.questionType;

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
                               isAns = comboIds.indexOf(id) < userAnsArr.length;
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
                                 let pts = 0; userAnsSet.forEach((v:string) => { if(correctAnsSet.has(v)) pts++; });
                                 isCorrect = comboIds.indexOf(id) < pts;
                             }
                          } else {
                             const q = section?.questions.find((q:any) => String(q.id) === id);
                             isCorrect = q && answers[id]?.trim().toUpperCase() === String(q.correctAnswer || '').trim().toUpperCase();
                          }
                          btnClass = isCorrect ? 'bg-emerald-100 border-emerald-400 text-emerald-800' : 'bg-red-100 border-red-400 text-red-800';
                       } else if (isAns) {
                          btnClass = 'bg-[#0ea5e9] border-[#0ea5e9] text-white shadow-inner';
                       }

                       return (
                          <button key={id} onClick={() => scrollToQuestion(id)} className={`h-11 w-full rounded-xl border text-[14px] font-bold flex items-center justify-center transition-all ${btnClass} ${!isReviewMode && isMark ? 'ring-[3px] ring-amber-400 ring-offset-1' : ''}`}>
                             {questionIndexMap[id]}
                          </button>
                       )
                    })}
                 </div>
              </div>
           </div>
        )}
      </div>

      <footer className="h-[75px] bg-white border-t border-slate-200 flex justify-between items-center px-4 md:px-8 shrink-0 z-30 relative font-sans shadow-[0_-4px_20px_rgba(0,0,0,0.03)]">
        <div className="flex-1">
           <button onClick={() => setShowPalette(!showPalette)} className={`font-bold px-6 py-3 rounded-xl transition-colors shadow-sm text-[13px] flex items-center gap-2 border ${showPalette ? 'bg-slate-800 text-white border-slate-800' : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50'}`}>
             <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6A2.25 2.25 0 016 3.75h2.25A2.25 2.25 0 0110.5 6v2.25a2.25 2.25 0 01-2.25 2.25H6a2.25 2.25 0 01-2.25-2.25V6zM3.75 15.75A2.25 2.25 0 016 13.5h2.25a2.25 2.25 0 012.25 2.25V18a2.25 2.25 0 01-2.25 2.25H6A2.25 2.25 0 013.75 18v-2.25zM13.5 6a2.25 2.25 0 012.25-2.25H18A2.25 2.25 0 0120.25 6v2.25A2.25 2.25 0 0118 10.5h-2.25a2.25 2.25 0 01-2.25-2.25V6zM13.5 15.75a2.25 2.25 0 012.25-2.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-2.25A2.25 2.25 0 0113.5 18v-2.25z" /></svg>
             <span className="hidden sm:block">Thống kê</span>
           </button>
        </div>
        <div className={`flex-1 flex justify-center items-center gap-2 font-black text-xl md:text-2xl tracking-wider ${timeLeft <= 300 && !isReviewMode ? 'text-red-500 animate-pulse' : 'text-slate-800'}`}>
           ⏱ {formatTime(timeLeft)}
        </div>
        <div className="flex-1 flex justify-end">
           {isReviewMode ? (
              <button onClick={onFinish} className="bg-emerald-600 hover:bg-emerald-700 text-white px-8 md:px-12 py-3.5 rounded-xl font-black text-[14px] transition-colors shadow-md uppercase tracking-wider">Thoát</button>
           ) : (
              <button onClick={handleFinish} className="bg-[#0ea5e9] hover:bg-[#0284c7] text-white px-8 md:px-12 py-3.5 rounded-xl font-black text-[14px] transition-colors shadow-md uppercase tracking-wider">Nộp Bài</button>
           )}
        </div>
      </footer>
    </div>
  );

  // ==========================================
  // GIAO DIỆN LISTENING (CUỘN DỌC TỪ TRÊN XUỐNG DƯỚI)
  // ==========================================
  const renderListeningLayout = () => (
    <div className="flex flex-col h-[100dvh] bg-[#f8fafc] font-sans text-slate-800 overflow-hidden">
      <header className={`h-[65px] px-6 flex justify-between items-center shrink-0 shadow-sm z-30 border-b ${isReviewMode ? 'bg-emerald-700 border-emerald-800' : 'bg-white border-slate-200'}`}>
        <div className="flex items-center gap-4">
          <h1 className={`font-black text-[18px] tracking-tight truncate max-w-xs md:max-w-xl ${isReviewMode ? 'text-white' : 'text-slate-800'}`}>
            {isReviewMode ? `[CHỮA BÀI] ${basicInfo?.title}` : basicInfo?.title}
          </h1>
        </div>

        {globalAudio && (
          <div className="flex-1 max-w-lg mx-8 flex items-center justify-center">
            {isReviewMode ? (
              <audio controls src={globalAudio} className="h-10 w-full rounded outline-none shadow-sm" />
            ) : (
              <div className="flex items-center gap-3 bg-slate-50 px-5 py-2 rounded-full border border-slate-200 shadow-inner w-full">
                <span className="text-xl opacity-70" title="Chỉnh âm lượng">🔊</span>
                <input type="range" min="0" max="1" step="0.05" defaultValue="1" onChange={(e) => { if(globalAudioRef.current) globalAudioRef.current.volume = parseFloat(e.target.value) }} className="w-full accent-[#0ea5e9] cursor-pointer" />
              </div>
            )}
          </div>
        )}

        <button onClick={onBack} className={`font-bold text-[13px] flex items-center gap-2 border px-4 py-2 rounded-lg transition-colors shadow-sm ${isReviewMode ? 'text-emerald-700 border-white bg-white hover:bg-emerald-50' : 'text-slate-600 border-slate-300 hover:bg-slate-50 bg-white'}`}>
          Thoát
        </button>
      </header>

      <div className="flex-1 overflow-y-auto custom-scrollbar w-full scroll-smooth relative">
        <div className="max-w-[1400px] mx-auto w-full flex flex-col lg:flex-row items-start gap-8 p-4 md:p-8">
          
          <div className="flex-1 w-full space-y-10 pb-24">
            {parts?.map((part: any, pIdx: number) => {
              const hasPassage = part?.content && part.content.trim().length > 0;
              return (
                <div key={pIdx} className="w-full bg-white p-8 md:p-10 rounded-3xl border border-slate-200 shadow-sm">
                  {!hasPassage && (
                    <div className="mb-8 border-b-2 border-slate-800 pb-4 text-center max-w-3xl mx-auto">
                      {part?.title && <h2 className="font-black text-[22px] uppercase tracking-widest text-slate-800">{part.title}</h2>}
                      {part?.imageUrl && <img src={part.imageUrl} className="max-w-full mt-6 mx-auto rounded-xl shadow-sm border border-slate-200" alt="Part" />}
                    </div>
                  )}

                  <div className={`flex items-start gap-10 ${hasPassage ? 'flex-col xl:flex-row' : 'flex-col max-w-3xl mx-auto'}`}>
                    {hasPassage && (
                      <div className="w-full xl:w-[45%] xl:sticky top-4 xl:h-[calc(100vh-140px)] overflow-y-auto custom-scrollbar pr-4 mb-8 xl:mb-0 border-r border-slate-200">
                        <div className="border-b-2 border-slate-800 pb-3 mb-6 text-center">
                           <h2 className="font-black text-[20px] uppercase tracking-widest text-slate-800">{part.title}</h2>
                        </div>
                        {part?.imageUrl && <img src={part.imageUrl} className="max-w-full mb-6 rounded-xl shadow-sm border border-slate-200" alt="Part" />}
                        <div className="prose prose-slate max-w-none text-justify leading-[1.9] text-[16px] text-slate-700">
                          {isReviewMode && isListening && <div className="bg-amber-50 text-amber-800 px-4 py-2 rounded-lg font-bold text-[13px] mb-6 border border-amber-200 inline-block shadow-sm">🎙️ TAPESCRIPT CHỮA BÀI NẰM Ở ĐÂY</div>}
                          <div dangerouslySetInnerHTML={{ __html: part.content || '' }} />
                        </div>
                      </div>
                    )}

                    <div className={`${hasPassage ? 'w-full xl:w-[55%] py-2 pl-4' : 'w-full'}`}>
                      {part?.audioUrl && (!isListening || isReviewMode) && (
                        <div className="bg-slate-50 p-4 rounded-xl shadow-sm border border-slate-200 mb-8 flex items-center">
                          <audio src={part.audioUrl} controls className="w-full h-10 outline-none" controlsList="nodownload" />
                        </div>
                      )}

                      <div className="space-y-8">
                        {part?.sections?.map((sec: any, sIdx: number) => {
                          let displaySecTitle = sec.title;
                          if (displaySecTitle && /Questions?\s+\d+/i.test(displaySecTitle)) {
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
                              if (firstIdx && lastIdx) displaySecTitle = displaySecTitle.replace(/Questions?\s+\d+(-\d+)?/i, firstIdx === lastIdx ? `Question ${firstIdx}` : `Questions ${firstIdx}-${lastIdx}`);
                          }

                          return (
                          <div key={sIdx} className="space-y-6">
                            
                            {displaySecTitle && (
                               <div className="bg-slate-100 border border-slate-200 px-4 py-2.5 rounded-lg mb-6 inline-block">
                                  <h4 className="font-bold text-slate-800 text-[15px] uppercase tracking-wide">{displaySecTitle}</h4>
                               </div>
                            )}

                            {sec?.imageUrl && <img src={sec.imageUrl} className="max-w-full rounded-xl shadow-sm border border-slate-200" alt="Section" />}
                            
                            {(sec?.questionType === "Điền từ" || sec?.questionType === "Kéo thả vào Part") && (
                              <div className={`border p-8 md:p-10 rounded-2xl shadow-sm ${isReviewMode ? 'bg-white border-slate-300' : 'bg-slate-50/50 border-slate-200'}`}>
                                <div className="space-y-5 leading-[3] text-[16px] text-slate-800 text-justify">
                                  {renderInlineQuestion(sec.content || '')}
                                </div>
                              </div>
                            )}

                            {(sec?.questionType === "Trắc nghiệm" || sec?.questionType === "TFNG") && sec?.questions?.map((q: any) => {
                              if (!q?.id) return null;
                              const cleanQText = getCleanQuestionText(q.content);
                              const correctAns = String(q.correctAnswer || '').trim().toUpperCase();
                              const userAns = String(answers[String(q.id)] || '').trim().toUpperCase();
                              const isQuestionCorrect = userAns === correctAns;
                              const displayIdx = questionIndexMap[String(q.id)] || q.id;

                              const isTFNG = sec?.questionType === "TFNG" || q.options?.some((opt: string) => ['TRUE', 'FALSE', 'NOT GIVEN', 'YES', 'NO'].includes(opt?.trim()?.toUpperCase()));

                              if (isTFNG) {
                                 return (
                                    <div key={q.id} id={`q-${q.id}`} className={`bg-white p-6 md:p-8 rounded-2xl shadow-sm border transition-all mb-4 scroll-mt-20 relative group ${isReviewMode ? (isQuestionCorrect ? 'border-emerald-300 bg-emerald-50/20' : 'border-red-300 bg-red-50/20') : 'border-slate-200 hover:border-[#0ea5e9]/40'}`}>
                                      {!isReviewMode && (
                                        <button onClick={() => toggleMark(String(q.id))} className={`absolute top-6 right-6 transition-colors ${marked[String(q.id)] ? 'text-amber-500' : 'text-slate-200 hover:text-slate-400'}`}>
                                           <svg className="w-7 h-7" fill={marked[String(q.id)] ? "currentColor" : "none"} stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={marked[String(q.id)] ? 2 : 1.5} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" /></svg>
                                        </button>
                                      )}
                                      {isReviewMode && (<div className="absolute top-6 right-6 font-bold text-[12px]">{isQuestionCorrect ? <span className="text-emerald-700 bg-emerald-100 px-3 py-1.5 rounded-lg">✅ Đúng</span> : <span className="text-red-700 bg-red-100 px-3 py-1.5 rounded-lg">❌ Sai</span>}</div>)}

                                      <div className="flex gap-4 mb-4 pr-12">
                                        <span className="font-bold text-white bg-slate-800 shrink-0 px-2 py-0.5 rounded text-[13px] mt-[1px]">{displayIdx}</span>
                                        <div className="flex-1 w-full">
                                           {q.imageUrl && <img src={q.imageUrl} className="max-w-[80%] mb-4 rounded-lg border border-slate-200" alt="Question Image" />}
                                           {cleanQText && <div className="text-[16px] text-slate-800 leading-relaxed font-medium whitespace-pre-wrap mb-4" dangerouslySetInnerHTML={{ __html: cleanQText }} />}
                                           
                                           <div className="flex flex-row flex-wrap gap-4">
                                             {q.options?.map((opt: string, i: number) => {
                                                const safeOpt = String(opt || '');
                                                const val = safeOpt.replace(/<[^>]*>/g, '').trim().toUpperCase();
                                                const isSelected = userAns === val;
                                                const isCorrectOpt = correctAns === val;

                                                let labelStyle = "flex items-center gap-2 p-2 transition-colors rounded-lg border border-transparent";
                                                if (isReviewMode) {
                                                   if (isCorrectOpt) labelStyle += " font-bold text-emerald-800 bg-emerald-100 border-emerald-300";
                                                   else if (isSelected) labelStyle += " text-red-600 line-through opacity-70 bg-red-50 border-red-200";
                                                } else {
                                                   labelStyle += " cursor-pointer hover:bg-slate-50 hover:text-[#0ea5e9] border-slate-100";
                                                }

                                                return (
                                                   <label key={i} className={labelStyle}>
                                                      <input type="radio" name={`q-${q.id}`} value={val} checked={isSelected} onChange={() => handleAnswer(String(q.id), val)} disabled={isReviewMode} className="w-4 h-4 accent-[#0ea5e9] cursor-pointer" />
                                                      <span className="text-[15px] font-bold" dangerouslySetInnerHTML={{ __html: safeOpt }} />
                                                   </label>
                                                );
                                             })}
                                           </div>
                                        </div>
                                      </div>
                                      {isReviewMode && q.explanation && (
                                        <div className="mt-8 pt-5 border-t border-slate-200 ml-10"><p className="text-[12px] font-black text-amber-600 uppercase mb-2">💡 Giải thích:</p><div className="text-[14px] text-slate-700 italic leading-relaxed border-l-[3px] border-amber-300 pl-3 whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: String(q.explanation) }} /></div>
                                      )}
                                    </div>
                                 );
                              }

                              return (
                                <div key={q.id} id={`q-${q.id}`} className={`bg-white p-6 md:p-8 rounded-2xl border shadow-sm relative group scroll-mt-20 transition-colors ${isReviewMode ? (isQuestionCorrect ? 'bg-emerald-50/30 border-emerald-200' : 'bg-red-50/30 border-red-200') : 'border-slate-200 hover:border-[#0ea5e9]/40'}`}>
                                  {!isReviewMode && (
                                    <button onClick={() => toggleMark(String(q.id))} className={`absolute top-6 right-6 transition-colors ${marked[String(q.id)] ? 'text-amber-500' : 'text-slate-300 hover:text-slate-400'}`}>
                                      <svg className="w-7 h-7" fill={marked[String(q.id)] ? "currentColor" : "none"} stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={marked[String(q.id)] ? 2 : 1.5} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" /></svg>
                                    </button>
                                  )}
                                  {isReviewMode && (
                                    <div className="absolute top-6 right-6 font-bold text-[14px]">
                                      {isQuestionCorrect ? <span className="text-emerald-700 bg-emerald-100 px-3 py-1.5 rounded-lg">✅ Đúng</span> : <span className="text-red-700 bg-red-100 px-3 py-1.5 rounded-lg">❌ Sai</span>}
                                    </div>
                                  )}

                                  <div className="flex gap-4 mb-5 pr-10 items-start">
                                    <span className="font-bold text-white bg-slate-800 px-2 py-0.5 rounded text-[13px] mt-0.5">{displayIdx}</span>
                                    <div className="flex-1 w-full">
                                       {q.imageUrl && <img src={q.imageUrl} className="max-w-[80%] mb-4 rounded-xl border border-slate-200 shadow-sm" alt="Question Image" />}
                                       {cleanQText && <div className="text-[16px] text-slate-800 leading-relaxed font-medium mb-3 whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: cleanQText }} />}
                                    </div>
                                  </div>
                                  
                                  <div className="flex flex-col gap-2 pl-10">
                                    {q.options?.map((opt: any, i: number) => {
                                      const cleanOpt = getCleanOptionText(opt, i);
                                      const val = String.fromCharCode(65+i);
                                      const isSelected = userAns === val;
                                      const isCorrectOpt = correctAns === val;

                                      let optStyle = 'text-slate-700 border-transparent hover:bg-slate-50';
                                      let ringStyle = 'bg-white border-slate-300 text-transparent';

                                      if (isReviewMode) {
                                        if (isCorrectOpt) { optStyle = 'bg-emerald-50/50 border-emerald-200 text-emerald-900 font-bold'; ringStyle = 'border-emerald-500 bg-emerald-500 text-white'; } 
                                        else if (isSelected && !isCorrectOpt) { optStyle = 'bg-red-50/50 border-red-200 text-red-700 line-through opacity-70'; ringStyle = 'border-red-500 bg-red-500 text-white'; } 
                                        else { optStyle = 'opacity-50 text-slate-400 border-transparent'; }
                                      } else {
                                        if (isSelected) { optStyle = 'bg-blue-50/40 border-[#0ea5e9]/30 text-blue-900 font-bold'; ringStyle = 'border-[#0ea5e9] bg-[#0ea5e9] text-white shadow-inner'; }
                                      }

                                      return (
                                        <label key={i} className={`flex items-start gap-4 p-3 rounded-xl transition-colors border ${optStyle} ${!isReviewMode ? 'cursor-pointer' : 'cursor-default'}`}>
                                          <input type="radio" name={`q-${q.id}`} value={val} checked={isSelected} onChange={() => handleAnswer(String(q.id), val)} className="hidden" disabled={isReviewMode} />
                                          <div className="pt-0.5">
                                            <div className={`w-[22px] h-[22px] rounded-full border-2 flex items-center justify-center shrink-0 transition-colors shadow-sm ${ringStyle}`}>
                                              {(isSelected || isCorrectOpt) && <div className="w-2 h-2 rounded-full bg-white"></div>}
                                            </div>
                                          </div>
                                          <span className={`text-[16px] leading-relaxed px-1`}><span className="font-bold mr-2">{val}.</span> <span dangerouslySetInnerHTML={{ __html: cleanOpt }} /></span>
                                        </label>
                                      );
                                    })}
                                  </div>

                                  {isReviewMode && q.explanation && (
                                    <div className="mt-8 pt-5 border-t border-slate-200 ml-10">
                                      <p className="text-[13px] font-black text-amber-600 uppercase tracking-widest mb-2">💡 Giải thích đáp án:</p>
                                      <div className="text-[14px] font-serif italic text-slate-700 leading-relaxed whitespace-pre-wrap border-l-[3px] border-slate-300 pl-3" dangerouslySetInnerHTML={{ __html: String(q.explanation) }} />
                                    </div>
                                  )}
                                </div>
                              );
                            })}

                            {sec?.questionType === "Droplist" && (
                               <div className="space-y-4 mb-8">
                                 {sec?.questions?.map((q: any) => {
                                   if (!q?.id) return null;
                                   const cleanQText = getCleanQuestionText(q.content);
                                   const correctAns = String(q.correctAnswer || '').trim().toUpperCase();
                                   const userAns = String(answers[String(q.id)] || '').trim().toUpperCase();
                                   const isQuestionCorrect = userAns === correctAns;
                                   const displayIdx = questionIndexMap[String(q.id)] || q.id;
                                   
                                   const otherSelectedAnswers = sec.questions
                                       .filter((otherQ: any) => otherQ.id !== q.id)
                                       .map((otherQ: any) => String(answers[String(otherQ.id)] || '').trim().toUpperCase())
                                       .filter((ans: string) => ans !== '');

                                   return (
                                      <div key={q.id} id={`q-${q.id}`} className={`bg-white p-5 rounded-2xl shadow-sm border flex flex-col sm:flex-row gap-4 items-start sm:items-center transition-all scroll-mt-20 ${isReviewMode ? (isQuestionCorrect ? 'border-emerald-300 bg-emerald-50/20' : 'border-red-300 bg-red-50/20') : 'border-slate-200 hover:border-[#0ea5e9]/40'}`}>
                                         <div className="font-bold text-white bg-slate-800 px-2 py-0.5 rounded text-[13px] shrink-0">{displayIdx}</div>
                                         <div className="flex-1 text-[15px] text-slate-800 line-clamp-2" dangerouslySetInnerHTML={{ __html: cleanQText }} />
                                         <div className="shrink-0 w-full sm:w-auto text-right">
                                            {isReviewMode ? (
                                               <div className="flex flex-col items-end gap-1">
                                                  <div className={`px-4 py-1.5 rounded-lg font-bold text-[14px] border inline-block ${isQuestionCorrect ? 'bg-emerald-100 text-emerald-800 border-emerald-300' : 'bg-red-100 text-red-800 border-red-300'}`}>
                                                     {userAns || '(chưa chọn)'}
                                                  </div>
                                                  {!isQuestionCorrect && <div className="text-[11px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">ĐA: {correctAns}</div>}
                                               </div>
                                            ) : (
                                               <select 
                                                  className="border border-slate-300 bg-slate-50 hover:bg-white focus:border-[#0ea5e9] rounded-xl px-4 py-2.5 outline-none font-bold text-slate-700 min-w-[150px] cursor-pointer text-[14px] transition-colors shadow-sm text-center"
                                                  style={{ textAlignLast: 'center' }}
                                                  value={userAns}
                                                  onChange={(e) => handleAnswer(String(q.id), e.target.value)}
                                               >
                                                  <option value="" disabled className="text-slate-400 font-normal">-- Chọn --</option>
                                                  {q.options?.map((opt: any, i: number) => {
                                                     const val = String(opt || '').trim().toUpperCase();
                                                     const isDisabled = otherSelectedAnswers.includes(val);
                                                     return <option key={i} value={val} disabled={isDisabled} className="text-slate-800 font-bold">{val} {isDisabled ? '(Đã chọn)' : ''}</option>
                                                  })}
                                               </select>
                                            )}
                                         </div>
                                      </div>
                                   )
                                 })}
                               </div>
                            )}

                            {/* 🚀 THUẬT TOÁN COMBO CHECKBOX TỰ ĐỘNG GOM NHÓM LẠI CHO LISTENING */}
                            {sec?.questionType === "Checkbox" && (
                               <div className="space-y-6">
                                 {(() => {
                                     const combos: any[][] = [];
                                     sec.questions?.forEach((q: any) => {
                                         const rawText = String(q.content || '').replace(/<[^>]*>/g, '').trim();
                                         const hasRealContent = rawText !== '' || String(q.content || '').includes('<img') || String(q.content || '').includes('<audio');
                                         if (combos.length === 0 || hasRealContent) combos.push([q]);
                                         else combos[combos.length - 1].push(q);
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

                                         let containerClass = "bg-white p-6 md:p-8 rounded-2xl shadow-sm border transition-colors relative group scroll-mt-20 mb-4 ";
                                         if (isReviewMode) {
                                             if (isPerfect) containerClass += "border-emerald-300 bg-emerald-50/30";
                                             else if (isPartial) containerClass += "border-amber-300 bg-amber-50/30";
                                             else containerClass += "border-red-300 bg-red-50/30";
                                         } else {
                                             containerClass += "border-slate-200 hover:border-[#0ea5e9]/40";
                                         }

                                         const handleComboChange = (optionValue: string, isChecked: boolean) => {
                                             setAnswers(prev => {
                                                 let currentSelected = Array.from(new Set(comboIds.map(id => prev[id]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase()))));
                                                 
                                                 if (isChecked) {
                                                     if (currentSelected.length >= maxAllowed) {
                                                         alert(`Lưu ý: Chỉ yêu cầu chọn tối đa ${maxAllowed} đáp án.`);
                                                         return prev;
                                                     }
                                                     if (!currentSelected.includes(optionValue)) currentSelected.push(optionValue);
                                                 } else {
                                                     currentSelected = currentSelected.filter((v:string) => v !== optionValue);
                                                 }
                                                 
                                                 const next = { ...prev };
                                                 comboIds.forEach((id, idx) => { next[id] = currentSelected[idx] || ''; }); 
                                                 return next;
                                             });
                                         };

                                         const qText = getCleanQuestionText(combo[0]?.content);
                                         const firstQIdx = questionIndexMap[comboIds[0]] || comboIds[0];
                                         const lastQIdx = questionIndexMap[comboIds[comboIds.length - 1]] || comboIds[comboIds.length - 1];
                                         const displayIndexText = comboIds.length > 1 ? `Câu ${firstQIdx}-${lastQIdx}` : `Câu ${firstQIdx}`;

                                         return (
                                            <div key={`combo-${comboIndex}`} id={`q-${combo[0].id}`} className={containerClass}>
                                              
                                              {!isReviewMode && (
                                                 <button onClick={() => toggleMark(String(combo[0].id))} className={`absolute top-6 right-6 transition-colors ${marked[String(combo[0].id)] ? 'text-amber-500' : 'text-slate-300 hover:text-slate-400'}`}>
                                                    <svg className="w-7 h-7" fill={marked[String(combo[0].id)] ? "currentColor" : "none"} stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={marked[String(combo[0].id)] ? 2 : 1.5} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" /></svg>
                                                 </button>
                                              )}
                                              {isReviewMode && (
                                                 <div className="absolute top-6 right-6 font-bold text-[12px]">
                                                    {isPerfect ? <span className="text-emerald-700 bg-emerald-100 px-3 py-1.5 rounded-lg">✅ Đúng</span> 
                                                    : isPartial ? <span className="text-amber-700 bg-amber-100 px-3 py-1.5 rounded-lg">⚠️ Đúng 1 phần</span>
                                                    : <span className="text-red-700 bg-red-100 px-3 py-1.5 rounded-lg">❌ Sai</span>}
                                                 </div>
                                              )}

                                              <div className="flex gap-4 mb-4 pr-16">
                                                <div className="flex flex-col gap-1 shrink-0 w-8 md:w-10 text-right pt-[2px]">
                                                   <span className="font-bold text-white bg-slate-800 inline-block px-2 py-0.5 rounded w-fit text-[14px]">{displayIndexText}</span>
                                                </div>
                                                <div className="flex-1 w-full mt-0.5">
                                                   {qText && <div className="text-[16px] mb-4 text-slate-800 leading-relaxed font-medium whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: qText }} />}

                                                   <div className={`flex flex-col gap-2.5`}>
                                                     {validOptions.map((opt: any, i: number) => {
                                                       const cleanOpt = getCleanOptionText(opt, i);
                                                       const optionValue = String.fromCharCode(65+i); 
                                                       const isSelected = userAnsArr.includes(optionValue); 
                                                       const isCorrectOpt = correctAnsComboSet.has(optionValue);
                                                       
                                                       let labelClass = "flex items-start gap-4 p-3 rounded-xl transition-colors border border-transparent -ml-3";
                                                       if (isReviewMode) { 
                                                           if (isCorrectOpt && isSelected) labelClass += " bg-emerald-50 border-emerald-400 font-bold text-emerald-900"; 
                                                           else if (isCorrectOpt && !isSelected) labelClass += " bg-amber-50 border-amber-300 font-bold text-amber-800"; 
                                                           else if (isSelected && !isCorrectOpt) labelClass += " bg-red-50 border-red-300 text-red-700 line-through opacity-70";
                                                           else labelClass += " opacity-50 border-transparent bg-transparent"; 
                                                       } else { 
                                                           labelClass += " cursor-pointer hover:bg-slate-50 border-transparent bg-transparent"; 
                                                           if (isSelected) labelClass += " bg-blue-50/50 border-[#0ea5e9]/30 font-bold text-[#0ea5e9]";
                                                       }
                                                       return (
                                                         <label key={i} className={labelClass}>
                                                           <input type="checkbox" checked={isSelected} onChange={(e) => handleComboChange(optionValue, e.target.checked)} className="mt-1 w-5 h-5 accent-[#0ea5e9] rounded cursor-pointer shrink-0" disabled={isReviewMode} />
                                                           <span className="text-[16px] leading-relaxed text-slate-800"><span className="font-bold font-sans mr-2">{optionValue}.</span> <span dangerouslySetInnerHTML={{ __html: cleanOpt }} /></span>
                                                         </label>
                                                       )
                                                     })}
                                                   </div>
                                                </div>
                                              </div>

                                              {isReviewMode && (
                                                <div className="mt-8 ml-[3.5rem] pt-5 border-t border-slate-200">
                                                   <p className="text-[13px] font-black text-amber-600 uppercase tracking-widest mb-3">💡 Giải thích:</p>
                                                   {combo.map((q:any) => {
                                                       if (!q.explanation || String(q.explanation).trim() === '') return null;
                                                       return (
                                                           <div key={q.id} className="text-[14px] text-slate-700 font-serif leading-relaxed mb-3 last:mb-0 border-l-[3px] border-slate-300 pl-3 italic">
                                                               <span className="font-bold text-slate-900 px-2 py-0.5 bg-slate-200 rounded text-[13px] mr-2 font-sans not-italic">Câu {questionIndexMap[String(q.id)] || q.id}</span>
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
                        );})}
                      </div>
                    </div>
                  </div>
                </div>
              );
            })}
            {(!parts || parts.length === 0) && (
              <div className="text-center py-20 text-slate-400 font-medium text-lg">Đề thi này chưa có nội dung.</div>
            )}
          </div>

          {/* ASIDE BÊN PHẢI (BẢNG ĐIỀU HƯỚNG LISTENING) */}
          <aside className="w-full lg:w-[320px] shrink-0 lg:sticky top-4 h-auto lg:h-[calc(100vh-140px)] flex flex-col bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden z-20">
            <div className="p-6 border-b border-slate-200 flex flex-col items-center bg-slate-50/50">
              {isReviewMode ? (
                <div className="bg-emerald-50 text-emerald-700 p-6 rounded-2xl border border-emerald-100 w-full text-center shadow-sm">
                  <p className="text-[12px] font-bold uppercase tracking-widest mb-2">Kết quả của bạn</p>
                  <p className="text-5xl font-black">{scoreResult.score} <span className="text-2xl text-emerald-400">/ {scoreResult.total}</span></p>
                </div>
              ) : (
                <div className="bg-white text-slate-800 px-6 py-4 rounded-xl font-black text-[22px] mb-6 border border-slate-200 flex items-center justify-center gap-3 w-full shadow-sm tracking-wider">
                  <span className="text-[#0ea5e9]">⏱</span> {formatTime(timeLeft)}
                </div>
              )}
              
              <div className="w-full text-[14px] font-bold text-slate-800 mb-5 mt-2 uppercase tracking-wide">Trạng thái câu hỏi</div>
              
              <div className="w-full flex flex-col gap-3 text-[13px] font-medium text-slate-600 mb-2">
                <div className="flex items-center justify-between bg-white p-2.5 rounded-lg border border-slate-200">
                   <div className="flex items-center gap-2.5"><div className="w-4 h-4 rounded-md bg-white border border-slate-300 shadow-sm"></div> Chưa làm</div>
                   <span className="font-bold">{totalCount - answeredCount}</span>
                </div>
                <div className="flex items-center justify-between bg-white p-2.5 rounded-lg border border-slate-200">
                   <div className="flex items-center gap-2.5"><div className="w-4 h-4 rounded-md bg-[#0ea5e9] shadow-sm"></div> Đã làm</div>
                   <span className="font-bold text-[#0ea5e9]">{answeredCount}</span>
                </div>
                {!isReviewMode && (
                  <div className="flex items-center justify-between bg-white p-2.5 rounded-lg border border-slate-200">
                     <div className="flex items-center gap-2.5"><div className="w-4 h-4 rounded-md border-[3px] border-amber-500 bg-transparent"></div> Đánh dấu</div>
                     <span className="font-bold text-amber-600">{markedCount}</span>
                  </div>
                )}
              </div>
            </div>
            
            <div className="flex-1 overflow-y-auto p-6 custom-scrollbar bg-slate-50/50">
              <div className="grid grid-cols-5 lg:grid-cols-4 sm:grid-cols-6 gap-2.5">
                {allQuestionIds.map(id => {
                  let isAns = answers[id] && answers[id].trim() !== '';
                  const isMarked = marked[id];
                  let btnStyle = 'bg-white border-slate-200 text-slate-600 hover:border-[#0ea5e9] hover:text-[#0ea5e9] shadow-sm'; 
                  
                  const section = parts.flatMap((p: any) => p.sections || []).find((s:any) => s.questions?.some((sq:any)=>String(sq.id)===id));
                  const qType = section?.questionType;

                  // ĐỒNG BỘ ĐỔ MÀU BẢNG ĐIỀU HƯỚNG COMBO CHECKBOX
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
                          isAns = idxInCombo < userAnsArr.length;
                      }
                  }

                  if (isReviewMode) {
                    let isCorrect = false;
                    if (qType === 'Checkbox') {
                        const combos: any[][] = [];
                        parts.flatMap((p:any) => p.sections || []).forEach(sec => {
                            if (sec.questionType === 'Checkbox') {
                               const c: any[][] = [];
                               sec.questions?.forEach((q: any) => {
                                   const rawText = String(q.content || '').replace(/<[^>]*>/g, '').trim();
                                   const hasRealContent = rawText !== '' || String(q.content || '').includes('<img') || String(q.content || '').includes('<audio');
                                   if (c.length === 0 || hasRealContent) c.push([q]); else c[c.length - 1].push(q);
                               });
                               combos.push(...c);
                            }
                        });
                        const myCombo = combos.find(c => c.some((q:any) => String(q.id) === id)) || [];
                        if (myCombo.length > 0) {
                            const comboIds = myCombo.map((q:any) => String(q.id));
                            const userAnsSet = new Set(comboIds.map(cid => answers[cid]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase())));
                            const correctAnsSet = new Set(myCombo.flatMap((q:any)=>String(q.correctAnswer).split(',').map((x:string)=>x.trim().toUpperCase()).filter(Boolean)));
                            let pts = 0; userAnsSet.forEach((v:string) => { if(correctAnsSet.has(v)) pts++; });
                            const idxInCombo = comboIds.indexOf(id);
                            isCorrect = idxInCombo < pts;
                        }
                    } else {
                        const q = section?.questions.find((q:any) => String(q.id) === id);
                        isCorrect = q && answers[id]?.trim().toUpperCase() === String(q.correctAnswer || '').trim().toUpperCase();
                    }
                    btnStyle = isCorrect ? 'bg-emerald-100 border-emerald-400 text-emerald-800' : 'bg-red-100 border-red-400 text-red-800';
                  } else if (isAns) { 
                    btnStyle = 'bg-[#0ea5e9] border-[#0ea5e9] text-white'; 
                  }
                  
                  return (
                    <button key={id} onClick={() => scrollToQuestion(id)} className={`relative h-11 flex items-center justify-center rounded-xl text-[14px] font-bold transition-all border ${btnStyle} ${!isReviewMode && isMarked ? 'ring-2 ring-amber-400 ring-offset-1' : ''}`}>
                      {questionIndexMap[id]}
                    </button>
                  )
                })}
              </div>
            </div>

            <div className="p-6 border-t border-slate-200 bg-white shrink-0">
              <button onClick={handleFinish} className={`w-full text-white font-black py-4 rounded-xl transition-colors shadow-md text-[15px] uppercase tracking-wider ${isReviewMode ? 'bg-emerald-600 hover:bg-emerald-700' : 'bg-[#0ea5e9] hover:bg-[#0284c7]'}`}>
                {isReviewMode ? 'Thoát Xem Lại' : 'Nộp Bài Thi'}
              </button>
            </div>
          </aside>

        </div>
      </div>
    </div>
  );

  return (
    <React.Fragment>
      {isListening && globalAudio && !isReviewMode && (
        <audio ref={globalAudioRef} src={globalAudio} preload="auto" className="hidden" />
      )}

      {!testStarted ? (
        <div className="flex flex-col h-[100dvh] items-center justify-center bg-[#f8fafc] font-sans p-4">
          <div className="bg-white p-10 md:p-12 rounded-3xl shadow-2xl border border-slate-200 w-full max-w-xl text-center animate-in zoom-in-95 duration-300">
            <div className="w-24 h-24 bg-blue-50 border border-blue-100 rounded-full flex items-center justify-center mx-auto mb-6 shadow-inner text-[#0ea5e9]">
               <span className="text-5xl">{(isListening && hasAnyAudio) ? '🎧' : '📖'}</span>
            </div>
            <h1 className="text-[24px] md:text-[28px] font-black text-slate-800 mb-3 leading-tight">{basicInfo?.title}</h1>
            <div className="flex items-center justify-center gap-2 text-slate-500 mb-8 font-medium bg-slate-50 inline-flex px-5 py-2.5 rounded-xl border border-slate-100 mx-auto">
               <span className="text-lg">⏱</span> Thời gian làm bài: <span className="font-bold text-slate-800">{formatTime(parseInitialTime(basicInfo?.timeLimit))}</span>
            </div>
            
            {(isListening && hasAnyAudio) && (
              <div className="bg-amber-50 border border-amber-200 p-5 rounded-xl text-amber-800 text-[14px] font-medium mb-8 text-left leading-relaxed shadow-sm flex items-start gap-4">
                <span className="text-2xl mt-1">⚠️</span>
                <div>
                   <span className="font-black block mb-1">LƯU Ý BÀI THI LISTENING</span> 
                   File âm thanh sẽ được <span className="font-bold underline">tự động phát</span> ngay khi bạn bấm nút Bắt Đầu bên dưới. Vui lòng đeo tai nghe và kiểm tra lại âm lượng thiết bị.
                </div>
              </div>
            )}

            <div className="flex flex-col sm:flex-row gap-3 justify-center mt-2">
              <button onClick={onBack} className="w-full sm:w-auto flex-1 bg-white px-8 py-4 rounded-xl font-bold text-slate-600 hover:text-slate-800 hover:bg-slate-50 border border-slate-200 transition-colors uppercase tracking-widest text-[13px] shadow-sm">Quay lại</button>
              <button onClick={handleStartTest} className="w-full sm:w-auto flex-[2] bg-[#0ea5e9] hover:bg-[#0284c7] text-white font-black px-10 py-4 rounded-xl shadow-lg transition-colors uppercase tracking-widest text-[13px] active:scale-95">Bắt Đầu Làm Bài</button>
            </div>
          </div>
        </div>
      ) : (
        isListening ? renderListeningLayout() : renderReadingLayout()
      )}
    </React.Fragment>
  );
}