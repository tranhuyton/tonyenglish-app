import React, { useState, useRef, useEffect, useMemo } from 'react';
import { supabase } from './supabase';

export default function IgcsePaperTest({ onBack, onStartTest, testData: propTestData }: { onBack?: () => void, onStartTest?: any, testData?: any }) {
  const [testData, setTestData] = useState<any>(() => {
      let raw = propTestData;
      if (!raw) {
          const saved = sessionStorage.getItem('lms_current_test');
          raw = saved ? JSON.parse(saved) : null;
      }
      if (!raw) return null;
      // Normalize: ensure json_config.questions exists from either json_config or content_json
      if (!raw.json_config?.questions && raw.content_json?.questions) {
          raw.json_config = { ...(raw.json_config || {}), questions: raw.content_json.questions, timeLimit: raw.content_json?.basicInfo?.timeLimit || raw.json_config?.timeLimit || 120 };
      }
      return raw;
  });
  
  const [isLoading, setIsLoading] = useState(!testData);
  const initIsReview = !!testData?.isReview;
  const [isReviewMode, setIsReviewMode] = useState(initIsReview);

  const [answers, setAnswers] = useState<Record<string, string>>(() => {
      if (initIsReview && testData?.past_answers) return testData.past_answers;
      if (!testData?.id) return {};
      try {
         const saved = localStorage.getItem(`igcse_ans_${testData.id}`);
         return saved ? JSON.parse(saved) : {};
      } catch(e) { return {}; }
  });
  
  const answersRef = useRef(answers);
  useEffect(() => { answersRef.current = answers; }, [answers]);

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [gradeResult, setGradeResult] = useState<any>(() => {
      if (initIsReview && testData?.aiFeedback) return testData.aiFeedback;
      return null;
  });

  const [leftWidth, setLeftWidth] = useState(50); 
  const [isDragging, setIsDragging] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  const [timeLeft, setTimeLeft] = useState(7200); 
  const isFinishingRef = useRef(false);

  const getSavedEndTime = (testId: string) => {
    if (!testId) return null;
    const saved = localStorage.getItem(`igcse_endtime_${testId}`);
    return saved ? parseInt(saved, 10) : null;
  };

  // Auto-save answers to localStorage
  useEffect(() => {
    if (testData?.id && !isFinishingRef.current && !gradeResult && !isReviewMode) {
      localStorage.setItem(`igcse_ans_${testData.id}`, JSON.stringify(answers));
    }
  }, [answers, testData?.id, gradeResult, isReviewMode]);

  // Initialize timer
  useEffect(() => {
    if (testData && !isReviewMode) {
       const rawTime = testData.json_config?.timeLimit || testData.timeLimit || testData.time_limit || 120;
       const initialSeconds = parseInt(rawTime) * 60;
       let currentEndTime = getSavedEndTime(testData.id);
       if (!currentEndTime) {
           currentEndTime = Date.now() + initialSeconds * 1000;
           localStorage.setItem(`igcse_endtime_${testData.id}`, currentEndTime.toString());
           setTimeLeft(initialSeconds);
       } else {
           const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
           setTimeLeft(remaining);
       }
       setIsLoading(false);
    } else if (isReviewMode) {
       setIsLoading(false);
    }
  }, [testData, isReviewMode]);

  const formatTime = (totalSeconds: number) => {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    const pad = (num: number) => num.toString().padStart(2, '0');
    if (hours > 0) return `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
    return `${pad(minutes)}:${pad(seconds)}`;
  };

  const handleAnswerChange = (inputId: string, value: string) => {
    if (isReviewMode) return;
    setAnswers(prev => ({ ...prev, [inputId]: value }));
  };

  // Image compression at browser - resize to max 1000px and compress JPEG 60%
  const handleImageUpload = (questionId: string, file: File) => {
      const reader = new FileReader();
      reader.onload = (e) => {
          const img = new Image();
          img.onload = () => {
              const canvas = document.createElement('canvas');
              const MAX_WIDTH = 1000; 
              const MAX_HEIGHT = 1000;
              let width = img.width;
              let height = img.height;

              if (width > height) {
                  if (width > MAX_WIDTH) { height *= MAX_WIDTH / width; width = MAX_WIDTH; }
              } else {
                  if (height > MAX_HEIGHT) { width *= MAX_HEIGHT / height; height = MAX_HEIGHT; }
              }
              
              canvas.width = width;
              canvas.height = height;
              const ctx = canvas.getContext('2d');
              if (ctx) {
                  ctx.fillStyle = '#ffffff'; 
                  ctx.fillRect(0, 0, canvas.width, canvas.height);
                  ctx.drawImage(img, 0, 0, width, height);
                  const resizedBase64 = canvas.toDataURL('image/jpeg', 0.6);
                  handleAnswerChange(questionId, resizedBase64);
              }
          };
          img.src = e.target?.result as string;
      };
      reader.readAsDataURL(file);
  };

  // Unicode character palette for formula insertion
  const [showPalette, setShowPalette] = useState<Record<string, boolean>>({});
  const inputRefs = useRef<Record<string, HTMLInputElement | HTMLTextAreaElement | null>>({});
  
  const scienceChars = [
    { label: 'Chỉ số dưới', chars: ['₀','₁','₂','₃','₄','₅','₆','₇','₈','₉'] },
    { label: 'Chỉ số trên', chars: ['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹','⁺','⁻','ⁿ'] },
    { label: 'Ký hiệu', chars: ['→','⇌','Δ','°','±','×','÷','≈','≠','≤','≥','∞','√','π','θ','α','β','γ','λ','μ','Ω'] },
  ];

  const insertChar = (subId: string, char: string) => {
    const el = inputRefs.current[subId];
    if (!el) {
      handleAnswerChange(subId, (answers[subId] || '') + char);
      return;
    }
    const start = el.selectionStart ?? el.value.length;
    const end = el.selectionEnd ?? start;
    const val = el.value;
    const newVal = val.slice(0, start) + char + val.slice(end);
    handleAnswerChange(subId, newVal);
    requestAnimationFrame(() => {
      el.focus();
      el.setSelectionRange(start + char.length, start + char.length);
    });
  };

  // Submit and grade via edge function
  const handleSubmit = async () => {
    const currentAnswers = answersRef.current;
    if (Object.keys(currentAnswers).length === 0 && timeLeft > 0) {
      alert("⚠️ Bạn chưa điền câu trả lời nào cả!"); return;
    }
    if (timeLeft > 0 && !window.confirm("Bạn có chắc chắn muốn nộp bài thi?")) { return; }

    setIsSubmitting(true);
    isFinishingRef.current = true;
    
    if (testData?.id) {
       localStorage.removeItem(`igcse_endtime_${testData.id}`);
       localStorage.removeItem(`igcse_ans_${testData.id}`);
    }

    try {
      // Separate image answers from text answers
      const imageAnswers: { questionId: string, base64: string }[] = [];
      const textAnswers: Record<string, string> = {};

      for (const [key, val] of Object.entries(currentAnswers)) {
          if (val.startsWith('data:image')) {
              imageAnswers.push({ questionId: key, base64: val });
              textAnswers[key] = "[HỌC SINH ĐÃ CHỤP ẢNH BẢN VẼ - HÃY XEM TRONG PHẦN ĐÍNH KÈM]";
          } else {
              textAnswers[key] = val;
          }
      }

      // Call IGCSE grading edge function
      const { data, error } = await supabase.functions.invoke('igcse-grader', {
        body: { 
            testConfig: testData.json_config?.questions || [],
            textAnswers: textAnswers,
            imageAnswers: imageAnswers
        }
      });

      if (error) throw new Error("Lỗi gọi Server: " + error.message);
      if (data?.error) throw new Error("Lỗi chấm điểm: " + data.error);
      
      const cleanJson = (data.result || "").replace(/```json/gi, "").replace(/```/gi, "").trim();
      const gradedData = JSON.parse(cleanJson);

      setGradeResult(gradedData);
      setIsReviewMode(true);

      // Save to database
      try {
        const { data: { user } } = await supabase.auth.getUser();
        if (user) {
          const rawTime = testData.json_config?.timeLimit || testData.timeLimit || testData.time_limit || 120;
          const initialSeconds = parseInt(rawTime) * 60;
          const timeSpentSecs = initialSeconds - timeLeft;
          
          await supabase.from('test_results').insert([{
            user_id: user.id, course_id: testData.course_id, test_title: testData.title || "IGCSE Paper",
            test_type: 'IGCSE-Science', score: gradedData.total_student_score, total_score: gradedData.total_max_score,
            time_spent: timeSpentSecs > 0 ? timeSpentSecs : 0,
            details: { test_id: testData.id, userAnswers: currentAnswers, aiFeedback: gradedData }
          }]);
        }
      } catch (dbError) { console.error("DB save error:", dbError); }

    } catch (err: any) {
      alert("❌ Có lỗi trong lúc chấm: " + err.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  // Timer countdown
  useEffect(() => {
    if (isLoading || !testData || gradeResult || isFinishingRef.current || isReviewMode) return;
    const timer = setInterval(() => {
        const currentEndTime = getSavedEndTime(testData.id);
        if (currentEndTime) {
            const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
            setTimeLeft(remaining);
            if (remaining <= 0) { clearInterval(timer); alert("⏰ Hết giờ làm bài!"); handleSubmit(); }
        } else { setTimeLeft(prev => Math.max(0, prev - 1)); }
    }, 1000);
    return () => clearInterval(timer);
  }, [isLoading, testData, gradeResult, isReviewMode]);

  // Drag resize handler
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!isDragging || !containerRef.current) return;
      const containerWidth = containerRef.current.getBoundingClientRect().width;
      const newLeftWidth = (e.clientX / containerWidth) * 100;
      if (newLeftWidth > 20 && newLeftWidth < 80) setLeftWidth(newLeftWidth);
    };
    const handleMouseUp = () => setIsDragging(false);
    if (isDragging) { document.addEventListener('mousemove', handleMouseMove); document.addEventListener('mouseup', handleMouseUp); }
    return () => { document.removeEventListener('mousemove', handleMouseMove); document.removeEventListener('mouseup', handleMouseUp); };
  }, [isDragging]);

  // Call AI Tutor for wrong answers
  const callAiTutor = (questionText: string, studentAns: string, correctAnswer: string) => {
      let query = '';
      if (studentAns.startsWith('data:image')) {
          window.dispatchEvent(new CustomEvent('tony-open-image-board', { detail: studentAns }));
          (window as any).tonyPendingImage = studentAns;
          query = `Thầy ơi, đây là bài vẽ của em cho câu hỏi: "${questionText}". \nĐáp án đúng của Cambridge là: "${correctAnswer}". \nThầy xem ảnh em vẽ sai ở đâu và hướng dẫn lại giúp em với ạ!`;
      } else {
          query = `Thầy ơi, câu hỏi là: "${questionText}". \nEm điền đáp án là: "${studentAns}". \nĐáp án chuẩn là: "${correctAnswer}". \nThầy giải thích chi tiết giúp em tại sao em sai ạ!`;
      }

      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
      setTimeout(() => {
          window.dispatchEvent(new CustomEvent('tony-force-start', { 
              detail: { 
                  mode: studentAns.startsWith('data:image') ? 'vision_mode' : 'text_mode',
                  image: studentAns.startsWith('data:image') ? studentAns : null,
                  query: query,
                  courseTitle: testData?.title || 'IGCSE Science'
              } 
          }));
      }, 500);
  };

  // Answered count for progress
  const allSubQuestions = useMemo(() => {
    if (!testData?.json_config?.questions) return [];
    return testData.json_config.questions.flatMap((q: any) => q.sub_questions || []);
  }, [testData]);

  const answeredCount = useMemo(() => {
    return allSubQuestions.filter((sq: any) => answers[sq.id]?.trim()).length;
  }, [allSubQuestions, answers]);

  // Loading state
  if (isLoading) return (
    <div className="h-screen w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold">
      <div className="animate-spin text-4xl mb-4">⏳</div>
      <p>Đang tải đề thi IGCSE...</p>
    </div>
  );

  // No test data
  if (!testData || (!isReviewMode && (!testData.json_config || !testData.json_config.questions))) return (
    <div className="h-screen w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold gap-4">
      <p>⚠️ Chưa có cấu hình đề thi trong hệ thống.</p>
      <button onClick={onBack} className="bg-[#1e88e5] px-6 py-2 rounded hover:bg-blue-700 transition-colors">Quay lại</button>
    </div>
  );

  const questions = testData.json_config.questions || [];

  return (
    <div className="h-screen w-screen flex flex-col bg-white font-sans text-slate-900 overflow-hidden">
      {/* Header */}
      <header className="h-14 w-full bg-white border-b border-slate-300 flex items-center justify-between px-4 sm:px-6 shrink-0 z-20 box-border">
        <div className="flex items-center gap-3 sm:gap-4 overflow-hidden">
          <button onClick={onBack} className="text-slate-600 hover:text-black font-bold text-sm transition-colors whitespace-nowrap">← Quay lại</button>
          <div className="h-5 w-px bg-slate-300 hidden sm:block"></div>
          <div className="truncate flex items-baseline gap-2">
            <h1 className="font-bold text-black text-[15px] leading-tight truncate">{isReviewMode ? `[REVIEW] ${testData.title}` : testData.title}</h1>
            {!isReviewMode && (
              <span className="text-xs text-slate-400 whitespace-nowrap">({answeredCount}/{allSubQuestions.length} câu)</span>
            )}
          </div>
        </div>
        {!gradeResult && !isReviewMode && (
          <div className="flex items-center gap-2 sm:gap-4 shrink-0">
             <div className={`font-bold flex items-center gap-2 px-3 py-1 rounded ${timeLeft <= 300 ? 'text-red-600 bg-red-50 animate-pulse' : 'text-slate-600'}`}>
               <span>⏱️</span> <span className="hidden sm:inline font-mono tracking-widest">{formatTime(timeLeft)}</span>
             </div>
             <button onClick={() => { if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(()=>{}); else document.exitFullscreen(); }} className="text-slate-500 hover:text-black transition-colors text-lg px-1" title="Toàn màn hình">
               {document.fullscreenElement ? '🔲' : '⛶'}
             </button>
             <button onClick={handleSubmit} disabled={isSubmitting} className="bg-[#1e88e5] hover:bg-blue-700 text-white font-bold text-sm px-6 py-1.5 rounded transition-colors active:scale-95 disabled:opacity-50 whitespace-nowrap">
               {isSubmitting ? 'Đang chấm...' : 'Nộp Bài'}
             </button>
          </div>
        )}
      </header>

      {/* Submitting overlay */}
      {isSubmitting && (
        <div className="fixed inset-0 z-50 bg-slate-900/70 backdrop-blur-sm flex flex-col items-center justify-center text-white">
          <div className="w-16 h-16 border-4 border-white/30 border-t-white rounded-full animate-spin mb-6"></div>
          <p className="text-xl font-bold mb-2">🧠 AI đang chấm bài...</p>
          <p className="text-sm text-slate-300">Gemini Vision đang phân tích bài làm và hình vẽ của bạn</p>
        </div>
      )}

      {/* Split Screen */}
      <div ref={containerRef} className="flex-1 flex overflow-hidden w-full select-none bg-[#525659]">
        {/* Left: PDF Viewer */}
        <div style={{ width: `${leftWidth}%` }} className="h-full flex flex-col shrink-0 bg-[#525659]">
          <div className="bg-[#323639] border-b border-[#202224] px-4 flex justify-between items-center h-10 shrink-0 shadow-sm">
            <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest">📄 Đề thi Cambridge</span>
          </div>
          <div className={`flex-1 w-full h-full ${isDragging ? 'pointer-events-none' : ''}`}>
             {testData.insert_pdf_url ? (
               <iframe src={`${testData.insert_pdf_url}#toolbar=0&navpanes=0&scrollbar=0&view=FitH`} className="w-full h-full border-none bg-transparent" title="PDF Paper" />
             ) : (
               <div className="flex flex-col items-center justify-center h-full text-slate-400 p-8 text-center bg-[#525659]">
                 <span className="text-5xl mb-4">📄</span>
                 <p className="font-bold">Không có file PDF đề thi.</p>
                 <p className="text-sm mt-2">Admin chưa upload PDF cho đề này.</p>
               </div>
             )}
          </div>
        </div>

        {/* Drag Handle */}
        <div onMouseDown={() => setIsDragging(true)} className={`w-[6px] h-full bg-[#202224] hover:bg-[#1e88e5] cursor-col-resize flex items-center justify-center shrink-0 z-10 transition-colors ${isDragging ? 'bg-[#1e88e5]' : ''}`}>
          <div className="flex flex-col gap-1"><div className="w-[2px] h-[2px] bg-slate-500"></div><div className="w-[2px] h-[2px] bg-slate-500"></div><div className="w-[2px] h-[2px] bg-slate-500"></div></div>
        </div>

        {/* Right: Answer Sheet */}
        <div style={{ width: `calc(${100 - leftWidth}% - 6px)` }} className="h-full flex flex-col shrink-0 bg-[#f8fafc]">
          <div className="bg-[#323639] border-b border-[#202224] px-6 flex justify-between items-center h-10 shrink-0 shadow-sm">
            <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest flex items-center gap-2">
              {gradeResult ? <><span>✅</span> Kết quả chấm điểm IGCSE</> : <><span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> Answer Sheet (Phiếu trả lời)</>}
            </span>
          </div>

          <div className={`flex-1 overflow-y-auto p-4 sm:p-8 ${isDragging ? 'pointer-events-none' : ''} custom-scrollbar`}>
            {/* Score Summary */}
            {gradeResult && (
                <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 mb-8 text-center">
                    <h2 className="text-2xl font-black text-slate-800 mb-2">Total Score</h2>
                    <div className="text-5xl font-black text-[#1e88e5] mb-4">
                        {gradeResult.total_student_score} <span className="text-2xl text-slate-400">/ {gradeResult.total_max_score}</span>
                    </div>
                    <div className="w-full bg-slate-200 rounded-full h-3 mb-4">
                      <div className="bg-gradient-to-r from-[#1e88e5] to-emerald-400 h-3 rounded-full transition-all" style={{ width: `${Math.min(100, (gradeResult.total_student_score / gradeResult.total_max_score) * 100)}%` }}></div>
                    </div>
                    <p className="text-[14px] text-slate-600 bg-slate-50 p-4 rounded-lg italic text-left">{gradeResult.general_feedback}</p>
                </div>
            )}

            {/* Questions */}
            <div className="space-y-8">
                {questions.map((q: any, qIdx: number) => (
                    <div key={qIdx} className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
                        <div className="flex gap-3 mb-6 items-baseline border-b border-slate-100 pb-4">
                            <h3 className="font-black text-slate-800 text-[18px]">Question {q.question_number}</h3>
                        </div>
                        
                        <div className="space-y-6">
                            {(q.sub_questions || []).map((sub: any) => {
                                const feedbackData = gradeResult?.details?.find((d:any) => d.id === sub.id);
                                const isCorrect = feedbackData?.student_score === sub.max_marks;
                                const isWrong = feedbackData && feedbackData?.student_score === 0;

                                return (
                                    <div key={sub.id} className={`p-4 rounded-lg border ${isReviewMode ? (isCorrect ? 'bg-emerald-50 border-emerald-200' : isWrong ? 'bg-red-50 border-red-200' : 'bg-orange-50 border-orange-200') : 'bg-slate-50 border-slate-200'}`}>
                                        <div className="flex justify-between items-start mb-3">
                                            <label className="font-semibold text-slate-800 text-[14px] leading-relaxed pr-4 whitespace-pre-wrap">{sub.label}</label>
                                            <span className="font-bold text-slate-400 text-[12px] whitespace-nowrap">[{sub.max_marks} marks]</span>
                                        </div>

                                        {/* Render input by question type */}
                                        {sub.type === 'short_answer' ? (
                                            <div className="relative">
                                                <div className="flex items-center gap-2">
                                                    <input ref={(el) => { inputRefs.current[sub.id] = el; }} type="text" value={answers[sub.id] || ''} onChange={(e) => handleAnswerChange(sub.id, e.target.value)} disabled={isReviewMode} placeholder="Điền đáp án ngắn..." className={`w-full max-w-sm px-4 py-2 border rounded-md text-[14px] outline-none transition-all ${isReviewMode ? 'bg-white border-slate-300' : 'focus:border-[#1e88e5] focus:ring-1 focus:ring-[#1e88e5]'}`}/>
                                                    {!isReviewMode && (
                                                        <button type="button" onClick={() => setShowPalette(prev => ({...prev, [sub.id]: !prev[sub.id]}))} className={`shrink-0 px-2.5 py-1.5 rounded-md text-[12px] font-bold border transition-all ${showPalette[sub.id] ? 'bg-[#1e88e5] text-white border-[#1e88e5]' : 'bg-white text-slate-500 border-slate-300 hover:border-[#1e88e5] hover:text-[#1e88e5]'}`} title="Bảng ký tự công thức">
                                                            f<sub>x</sub>
                                                        </button>
                                                    )}
                                                </div>
                                                {showPalette[sub.id] && !isReviewMode && (
                                                    <div className="absolute z-30 top-full mt-1 left-0 bg-white border border-slate-200 rounded-lg shadow-lg p-3 w-[340px]">
                                                        {scienceChars.map((group, gi) => (
                                                            <div key={gi} className="mb-2 last:mb-0">
                                                                <div className="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">{group.label}</div>
                                                                <div className="flex flex-wrap gap-1">
                                                                    {group.chars.map(c => (
                                                                        <button key={c} type="button" onClick={() => insertChar(sub.id, c)} className="w-8 h-8 flex items-center justify-center rounded border border-slate-200 bg-slate-50 hover:bg-[#1e88e5] hover:text-white hover:border-[#1e88e5] text-[14px] font-medium transition-all active:scale-90">{c}</button>
                                                                    ))}
                                                                </div>
                                                            </div>
                                                        ))}
                                                    </div>
                                                )}
                                            </div>
                                        ) : sub.type === 'long_answer' ? (
                                            <div className="relative">
                                                <div className="flex items-start gap-2">
                                                    <textarea ref={(el) => { inputRefs.current[sub.id] = el; }} value={answers[sub.id] || ''} onChange={(e) => handleAnswerChange(sub.id, e.target.value)} disabled={isReviewMode} placeholder="Viết câu trả lời tự luận..." className={`w-full px-4 py-3 border rounded-md min-h-[80px] text-[14px] outline-none transition-all resize-y ${isReviewMode ? 'bg-white border-slate-300' : 'focus:border-[#1e88e5] focus:ring-1 focus:ring-[#1e88e5]'}`}/>
                                                    {!isReviewMode && (
                                                        <button type="button" onClick={() => setShowPalette(prev => ({...prev, [sub.id]: !prev[sub.id]}))} className={`shrink-0 mt-1 px-2.5 py-1.5 rounded-md text-[12px] font-bold border transition-all ${showPalette[sub.id] ? 'bg-[#1e88e5] text-white border-[#1e88e5]' : 'bg-white text-slate-500 border-slate-300 hover:border-[#1e88e5] hover:text-[#1e88e5]'}`} title="Bảng ký tự công thức">
                                                            f<sub>x</sub>
                                                        </button>
                                                    )}
                                                </div>
                                                {showPalette[sub.id] && !isReviewMode && (
                                                    <div className="absolute z-30 top-full mt-1 left-0 bg-white border border-slate-200 rounded-lg shadow-lg p-3 w-[340px]">
                                                        {scienceChars.map((group, gi) => (
                                                            <div key={gi} className="mb-2 last:mb-0">
                                                                <div className="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">{group.label}</div>
                                                                <div className="flex flex-wrap gap-1">
                                                                    {group.chars.map(c => (
                                                                        <button key={c} type="button" onClick={() => insertChar(sub.id, c)} className="w-8 h-8 flex items-center justify-center rounded border border-slate-200 bg-slate-50 hover:bg-[#1e88e5] hover:text-white hover:border-[#1e88e5] text-[14px] font-medium transition-all active:scale-90">{c}</button>
                                                                    ))}
                                                                </div>
                                                            </div>
                                                        ))}
                                                    </div>
                                                )}
                                            </div>
                                        ) : (
                                            /* Image Upload type */
                                            <div className="w-full mt-2" tabIndex={0} onPaste={(e) => {
                                                if (isReviewMode) return;
                                                const items = e.clipboardData?.items;
                                                if (!items) return;
                                                for (let i = 0; i < items.length; i++) {
                                                    if (items[i].type.startsWith('image/')) {
                                                        e.preventDefault();
                                                        const file = items[i].getAsFile();
                                                        if (file) handleImageUpload(sub.id, file);
                                                        return;
                                                    }
                                                }
                                            }}>
                                                {answers[sub.id] ? (
                                                    <div className="relative inline-block border-2 border-slate-300 rounded-lg p-2 bg-white shadow-sm">
                                                        <img src={answers[sub.id]} alt="Bài làm" className="max-h-[250px] object-contain rounded" />
                                                        {!isReviewMode && (
                                                            <button onClick={() => handleAnswerChange(sub.id, '')} className="absolute -top-3 -right-3 bg-red-500 text-white w-7 h-7 rounded-full shadow-md font-bold hover:scale-110 transition-transform">✕</button>
                                                        )}
                                                    </div>
                                                ) : (
                                                    <label className={`flex flex-col items-center justify-center w-full h-32 border-2 border-dashed border-slate-300 rounded-lg bg-white transition-colors ${!isReviewMode ? 'cursor-pointer hover:bg-sky-50 hover:border-sky-400' : 'opacity-50'}`}>
                                                        <div className="flex flex-col items-center justify-center pt-5 pb-6">
                                                            <span className="text-3xl mb-2">📸</span>
                                                            <p className="text-sm text-slate-500 font-semibold">Nhấn để chọn ảnh hoặc Ctrl+V để dán từ clipboard</p>
                                                            <p className="text-xs text-slate-400 mt-1">Ảnh sẽ tự động nén nhỏ {"<"} 1MB</p>
                                                        </div>
                                                        <input type="file" className="hidden" accept="image/*" capture="environment" onChange={(e) => {
                                                            if(e.target.files && e.target.files[0]) handleImageUpload(sub.id, e.target.files[0]);
                                                        }} disabled={isReviewMode}/>
                                                    </label>
                                                )}
                                            </div>
                                        )}

                                        {/* Review feedback */}
                                        {isReviewMode && feedbackData && (
                                            <div className="mt-4 pt-4 border-t border-slate-200/60">
                                                <div className="flex justify-between items-center mb-2">
                                                    <span className={`font-bold text-[12px] uppercase tracking-wider px-2 py-1 rounded ${isCorrect ? 'bg-emerald-200 text-emerald-800' : isWrong ? 'bg-red-200 text-red-800' : 'bg-orange-200 text-orange-800'}`}>
                                                      Điểm đạt: {feedbackData.student_score} / {sub.max_marks}
                                                    </span>
                                                </div>
                                                <p className="text-[13px] text-slate-700 mt-2 mb-3"><span className="font-bold text-slate-900">Nhận xét: </span> {feedbackData.examiner_comment}</p>
                                                <div className="bg-white p-3 rounded border border-slate-200 text-[13px]">
                                                    <span className="font-bold text-slate-500 uppercase text-[10px] tracking-widest block mb-1">Đáp án đúng (Cambridge MS):</span>
                                                    <span className="font-medium text-emerald-600">{feedbackData.correct_answer}</span>
                                                </div>

                                                {!isCorrect && (
                                                    <button onClick={() => callAiTutor(sub.label, answers[sub.id] || "Bỏ trống", feedbackData.correct_answer)} className="mt-4 flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-amber-400 to-orange-400 text-white font-bold text-[12px] rounded-lg shadow-md hover:shadow-lg transition-all active:scale-95">
                                                        ✨ Gọi Thầy AI ra bảng đen giảng lại câu này
                                                    </button>
                                                )}
                                            </div>
                                        )}
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
