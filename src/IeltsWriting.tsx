import React, { useState, useEffect, useRef } from 'react';
import { supabase } from './supabase';
import './tailwind.css';

// --- BỘ ICON CHUẨN IDP ---
const UserIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path fillRule="evenodd" d="M7.5 6a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM3.751 20.105a8.25 8.25 0 0116.498 0 .75.75 0 01-.437.695A18.683 18.683 0 0112 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 01-.437-.695z" clipRule="evenodd" /></svg>;
const SettingsIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path fillRule="evenodd" d="M11.078 2.25c-.917 0-1.699.663-1.85 1.567L9.05 4.889c-.02.12-.115.26-.297.348a7.493 7.493 0 00-.986.57c-.166.115-.334.126-.45.083L6.3 5.508a1.875 1.875 0 00-2.282.819l-.922 1.597a1.875 1.875 0 00.432 2.385l.84.692c.097.078.15.222.15.399v.111c0 .177-.053.321-.15.399l-.84.692a1.875 1.875 0 00-.432 2.385l.922 1.597a1.875 1.875 0 002.282.818l1.019-.382c.115-.043.283-.031.45.082.312.214.641.405.985.57.182.088.277.228.297.35l.178 1.071c.151.904.933 1.567 1.85 1.567h1.844c.916 0 1.699-.663 1.85-1.567l.178-1.072c.02-.12.114-.26.297-.349.344-.165.673-.356.985-.57.167-.114.335-.125.45-.082l1.02.382a1.875 1.875 0 002.28-.819l.923-1.597a1.875 1.875 0 00-.432-2.385l-.84-.692c-.098-.078-.15-.222-.15-.399v-.111c0-.177.052-.321.15-.399l.84-.692a1.875 1.875 0 00.432-2.385l-.923-1.597a1.875 1.875 0 00-2.28-.818l-1.02.382c-.114.043-.282.031-.449-.083a7.49 7.49 0 00-.985-.57c-.183-.087-.277-.227-.297-.348l-.179-1.072a1.875 1.875 0 00-1.85-1.567h-1.843zM12 15.75a3.75 3.75 0 110-7.5 3.75 3.75 0 010 7.5z" clipRule="evenodd" /></svg>;
const UndoIcon = () => <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M9 15L3 9m0 0l6-6M3 9h12a6 6 0 010 12h-3" /></svg>;
const RedoIcon = () => <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M15 15l6-6m0 0l-6-6m6 6H9a6 6 0 000 12h3" /></svg>;
const BoldIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-4 h-4"><path fillRule="evenodd" d="M8.25 4.5A.75.75 0 007.5 5.25v13.5a.75.75 0 00.75.75h5.25a4.5 4.5 0 003.568-7.254 4.5 4.5 0 00-2.818-7.746H8.25zM9 10.5h4.125a2.25 2.25 0 000-4.5H9v4.5zm0 2.25v4.5h4.875a2.25 2.25 0 000-4.5H9z" clipRule="evenodd" /></svg>;
const ItalicIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-4 h-4"><path fillRule="evenodd" d="M12.984 4.15A.75.75 0 0113.5 4.5h4.5a.75.75 0 010 1.5h-2.316l-3.375 12h2.441a.75.75 0 010 1.5H10.5a.75.75 0 010-1.5h2.316l3.375-12H13.5a.75.75 0 01-.516-1.35z" clipRule="evenodd" /></svg>;
const UnderlineIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-4 h-4"><path fillRule="evenodd" d="M6 3.75a.75.75 0 01.75.75v8.25a5.25 5.25 0 0010.5 0V4.5a.75.75 0 011.5 0v8.25a6.75 6.75 0 01-13.5 0V4.5a.75.75 0 01.75-.75zM3.75 20.25a.75.75 0 01.75-.75h15a.75.75 0 010 1.5h-15a.75.75 0 01-.75-.75z" clipRule="evenodd" /></svg>;

export default function IeltsWriting({ onBack, testData: propTestData, onFinish }: { onBack?: () => void, testData?: any, onFinish?: (res: any) => void }) {
  
  const [testData, setTestData] = useState<any>(() => {
     if (propTestData) return propTestData;
     try {
       const saved = sessionStorage.getItem('lms_current_test');
       return saved ? JSON.parse(saved) : null;
     } catch (e) { return null; }
  });

  let safeData = testData || {};
  if (typeof safeData === 'string') {
    try { safeData = JSON.parse(safeData); } catch (e) { safeData = {}; }
  }
  let contentJSON = safeData?.content_json || safeData || {};
  if (typeof contentJSON === 'string') {
    try { contentJSON = JSON.parse(contentJSON); } catch (e) { contentJSON = {}; }
  }
  const basicInfo = contentJSON?.basicInfo || { title: "IELTS Writing", timeLimit: "60" };
  const parts = Array.isArray(contentJSON?.parts) ? contentJSON.parts : [];

  const allQuestions: any[] = [];
  if (Array.isArray(parts)) {
    parts.forEach((p: any) => {
      if (p && Array.isArray(p.sections)) {
        p.sections.forEach((s: any) => {
          if (s && Array.isArray(s.questions)) {
            s.questions.forEach((q: any) => {
              if (q) {
                // Thu gom dữ liệu mỏng nhẹ, loại bỏ partTitle, partContent
                allQuestions.push({ ...q, secTitle: s.title, secContent: s.content });
              }
            });
          }
        });
      }
    });
  }

  const [answers, setAnswers] = useState<Record<string, string>>(() => {
     if (!safeData?.id) return {};
     try {
        const saved = localStorage.getItem(`ielts_writing_ans_${safeData.id}`);
        const parsed = saved ? JSON.parse(saved) : {};
        return (typeof parsed === 'object' && parsed !== null) ? parsed : {};
     } catch(e) { return {}; }
  });

  const [currentTaskIndex, setCurrentTaskIndex] = useState(0);
  const currentTask = allQuestions[currentTaskIndex];
  
  const [reviewFlags, setReviewFlags] = useState<Record<number, boolean>>({});

  const [isSubmitted, setIsSubmitted] = useState(false);
  const [isGrading, setIsGrading] = useState(false);
  const [aiResult, setAiResult] = useState<any>(null);

  const parseTime = (t: any) => parseInt(t) || 60;
  const [timeLeft, setTimeLeft] = useState(() => parseTime(basicInfo.timeLimit) * 60);

  // Resize Left/Right Column logic
  const [leftWidth, setLeftWidth] = useState(50);
  const containerRef = useRef<HTMLElement>(null);
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

  useEffect(() => {
    if (isSubmitted || isGrading) return;
    const timer = setInterval(() => setTimeLeft(prev => {
        if (prev <= 1) { clearInterval(timer); handleSubmit(); return 0; }
        return prev - 1;
    }), 1000);
    return () => clearInterval(timer);
  }, [isSubmitted, isGrading]);

  const formatTime = (secs: number) => {
    if (isNaN(secs)) return '60 minutes left';
    const m = Math.floor(secs / 60);
    return `${m} minutes left`;
  };

  useEffect(() => {
    if (safeData?.id && !isSubmitted && !isGrading) {
      localStorage.setItem(`ielts_writing_ans_${safeData.id}`, JSON.stringify(answers));
    }
  }, [answers, safeData?.id, isSubmitted, isGrading]);

  const handleAnswerChange = (qId: string, value: string) => {
    setAnswers(prev => ({ ...prev, [qId]: value }));
  };

  const handleReviewToggle = () => {
    setReviewFlags(prev => ({ ...prev, [currentTaskIndex]: !prev[currentTaskIndex] }));
  };

  const getWordCount = (text: any) => {
    if (!text || typeof text !== 'string') return 0;
    const str = text.trim();
    return str === '' ? 0 : str.split(/\s+/).length;
  };

  const handleSubmit = async () => {
    let totalWords = 0;
    Object.values(answers).forEach(ans => totalWords += getWordCount(ans));

    if (totalWords < 50) {
      alert("Bạn chưa viết đủ bài. Vui lòng hoàn thiện tối thiểu 50 từ trước khi nộp.");
      return;
    }
    if (!window.confirm("Bạn có chắc chắn muốn nộp bài thi? Hệ thống sẽ gửi bài cho Giám khảo AI chấm điểm.")) return;

    setIsGrading(true);

    if (safeData?.id) localStorage.removeItem(`ielts_writing_ans_${safeData.id}`);

    try {
      const prompt = `
        Bạn là một Giám khảo IELTS vô cùng khắt khe. Hãy chấm bài IELTS Writing sau đây.
        
        THÔNG TIN ĐỀ BÀI (Chứa các yêu cầu của Task 1 và Task 2):
        ${JSON.stringify(allQuestions.map((q, i) => `Task ${i+1} (${q.secTitle}): ${q.secContent} ${q.content}`))}

        BÀI LÀM CỦA HỌC SINH (Map theo ID câu hỏi):
        ${JSON.stringify(answers)}

        Hãy phân tích tất cả các Task học sinh đã làm và trả về ĐÚNG định dạng JSON sau (không dùng markdown block):
        {
          "overall": 6.5,
          "tasks": [
            {
              "task_name": "Task 1",
              "score": 6.0,
              "criteria": [
                { "name": "Task Achievement", "score": 6.0, "comment": "Nhận xét..." },
                { "name": "Coherence & Cohesion", "score": 6.0, "comment": "Nhận xét..." },
                { "name": "Lexical Resource", "score": 6.0, "comment": "Nhận xét..." },
                { "name": "Grammatical Range", "score": 6.0, "comment": "Nhận xét..." }
              ],
              "feedback": "Văn bản bài làm kèm thẻ <span class='bg-red-200 text-red-800 line-through px-1'>từ sai</span> và <span class='bg-emerald-200 text-emerald-800 font-bold px-1'>từ đúng</span>..."
            }
          ],
          "generalFeedback": "Nhận xét tổng quan điểm mạnh điểm yếu..."
        }
      `;

      const { data, error } = await supabase.functions.invoke('ai-grader', {
        body: { 
           prompt: prompt,
           model: 'gemini-2.5-flash'
        }
      });

      if (error) throw new Error("Lỗi gọi Server: " + error.message);
      if (data?.error) throw new Error("Lỗi chấm điểm AI: " + data.error);

      const textResponse = data.result.replace(/\u0060{3}(json)?/gi, "").trim();
      const parsedResult = JSON.parse(textResponse);
      
      setAiResult(parsedResult);
      setIsSubmitted(true);

      const { data: { user } } = await supabase.auth.getUser();
      if (user) {
        await supabase.from('test_results').insert([{
          user_id: user.id,
          course_id: safeData?.course_id || null,
          test_title: basicInfo.title,
          test_type: 'IELTS-Writing',
          score: parsedResult.overall,
          total_score: 9,
          time_spent: (parseTime(basicInfo.timeLimit) * 60) - timeLeft,
          details: { test_id: safeData?.id, userAnswers: answers, aiFeedback: parsedResult, bandScore: parsedResult.overall }
        }]);
      }

    } catch (error: any) {
      console.error("LỖI CHI TIẾT:", error);
      alert("Hệ thống chấm điểm AI bị lỗi. Vui lòng thử lại: " + error.message);
    } finally {
      setIsGrading(false);
    }
  };

  if (!testData || allQuestions.length === 0) {
    return <div className="h-screen w-full flex items-center justify-center bg-[#eeeeee] font-bold text-slate-900">Loading test data...</div>;
  }

  return (
    <div className="h-screen flex flex-col bg-[#eeeeee] font-sans text-slate-900 overflow-hidden">
      
      {/* Đã tinh chỉnh khoảng cách dòng (leading) và margin dưới của thẻ P */}
      <style>{`
          .format-passage p { margin-bottom: 0.75rem !important; }
          .format-passage p:last-child { margin-bottom: 0 !important; }
          .format-passage br { display: block; content: ""; margin-bottom: 0.25rem; }
      `}</style>

      {/* HEADER MÀU ĐEN BRUTALIST */}
      <header className="h-[46px] bg-[#222222] text-white flex justify-between items-center px-4 shrink-0 select-none z-20 border-b border-slate-700 relative">
        <div className="flex items-center gap-2">
          <UserIcon />
          <span className="font-bold text-[14px] truncate max-w-[200px] md:max-w-xs text-white">{basicInfo.title}</span>
        </div>
        
        <div className={`absolute left-1/2 -translate-x-1/2 font-bold text-[15px] tracking-widest ${timeLeft <= 300 ? 'text-red-500' : 'text-white'}`}>
           {isSubmitted ? 'TEST FINISHED' : formatTime(timeLeft)}
        </div>

        <div className="flex items-center gap-4">
           {isSubmitted ? (
              <button onClick={onBack} className="text-[13px] font-bold border border-white px-3 py-1 rounded-none hover:bg-white/10 transition text-white">Return to Home</button>
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

      {isGrading && (
        <div className="flex-1 flex flex-col items-center justify-center bg-white/95 z-50 absolute inset-0 pt-10">
          <div className="relative flex items-center justify-center w-32 h-32 mb-6">
             <svg className="absolute inset-0 w-full h-full animate-spin text-black" viewBox="0 0 100 100">
               <circle cx="50" cy="50" r="45" fill="none" stroke="currentColor" strokeWidth="8" strokeDasharray="200" strokeLinecap="round" />
             </svg>
             <span className="font-bold text-xl text-black">AI</span>
          </div>
          <h2 className="text-xl font-bold text-black mb-2">Grading in Progress</h2>
          <p className="text-slate-600 text-sm font-medium">Please wait while the AI examiner analyzes your essay...</p>
        </div>
      )}

      {!isSubmitted && !isGrading && currentTask && (
        <div className="flex-1 flex flex-col overflow-hidden bg-[#eeeeee]">

          <main className="flex-1 flex flex-col md:flex-row overflow-hidden relative" ref={containerRef as any}>
            
            {/* CỘT TRÁI - ĐỀ BÀI (CHUẨN UI IDP/BC) */}
            <section className="p-8 md:p-12 overflow-y-auto custom-scrollbar border-r border-slate-400 flex flex-col bg-white" style={{ width: window.innerWidth > 768 ? `${leftWidth}%` : '100%', flex: 'none' }}>
              <div className="format-passage max-w-none text-[15px] leading-[1.6] text-black font-serif break-words">
                
                {/* Chỉ giữ lại Tên Section (Task) và Nội Dung */}
                {currentTask.secTitle && (
                    <p className="font-bold text-[16px] text-black mb-4">[{currentTask.secTitle}]</p>
                )}

                {currentTask.secContent && (
                  <div className="mb-4 whitespace-pre-wrap" dangerouslySetInnerHTML={{__html: currentTask.secContent}} />
                )}
                
                {currentTask.content && (
                  <div className="mb-4 whitespace-pre-wrap" dangerouslySetInnerHTML={{__html: currentTask.content}} />
                )}

                {currentTask.imageUrl && (
                  <img src={currentTask.imageUrl} alt="Diagram" className="w-full max-w-[700px] h-auto mt-6 block" />
                )}

              </div>
              <div className="h-[100px]" />
            </section>

            {/* THANH KÉO DÃN Ở GIỮA */}
            <div className="w-4 bg-[#e8e8e8] hover:bg-[#d4d4d4] cursor-col-resize flex flex-col justify-center items-center z-10 border-x border-slate-400 transition-colors shrink-0" onMouseDown={startDrag}>
               <div className="flex flex-col gap-1.5 opacity-40">
                  <div className="w-1 h-1 bg-black"></div>
                  <div className="w-1 h-1 bg-black"></div>
                  <div className="w-1 h-1 bg-black"></div>
                  <div className="w-1 h-1 bg-black"></div>
               </div>
            </div>

            {/* CỘT PHẢI - BÀI VIẾT CỦA HỌC SINH */}
            <section className="p-8 md:p-10 flex flex-col overflow-hidden relative bg-[#f4f4f4]" style={{ width: `${100 - leftWidth}%`, flex: 'none' }}>
              
              <div className="flex-1 bg-white border border-slate-400 rounded-none flex flex-col overflow-hidden">
                {/* THANH TOOLBAR CỦA TEXTAREA */}
                <div className="h-12 border-b border-slate-300 flex items-center px-4 gap-6 shrink-0 bg-[#e0e0e0]">
                   <div className="flex gap-4 border-r border-slate-400 pr-6 text-slate-700">
                      <button className="hover:text-black transition" title="Undo"><UndoIcon /></button>
                      <button className="hover:text-black transition" title="Redo"><RedoIcon /></button>
                   </div>
                   <div className="flex items-center gap-4 text-slate-700">
                      <span className="font-serif font-bold text-[14px] cursor-pointer hover:text-black">A <span className="text-[10px] text-slate-500">▼</span></span>
                      <button className="w-7 h-7 hover:bg-slate-300 flex items-center justify-center rounded-none transition"><BoldIcon /></button>
                      <button className="w-7 h-7 hover:bg-slate-300 flex items-center justify-center rounded-none transition"><ItalicIcon /></button>
                      <button className="w-7 h-7 hover:bg-slate-300 flex items-center justify-center rounded-none transition"><UnderlineIcon /></button>
                   </div>
                </div>
                
                {/* Giảm line-height xuống 1.6 cho cân bằng */}
                <textarea 
                  className="flex-1 w-full p-8 outline-none resize-none text-[15px] text-black font-serif custom-scrollbar leading-[1.6] bg-white"
                  placeholder=""
                  value={answers[currentTask.id] || ''}
                  onChange={(e) => handleAnswerChange(currentTask.id, e.target.value)}
                  spellCheck="false"
                />
              </div>
              
              <div className="mt-3 text-[14px] text-slate-700 font-bold tracking-wide">
                Word Count: {getWordCount(answers[currentTask.id])}
              </div>

            </section>
          </main>

          {/* THANH FOOTER BRUTALIST */}
          <footer className="h-[60px] bg-white border-t border-slate-400 flex justify-between items-center px-6 shrink-0 select-none">
             
             <div className="flex items-center h-full">
                <div className="flex items-center gap-2 h-full pr-6 border-r border-slate-400 shrink-0 min-w-max">
                  <input 
                    type="checkbox" 
                    id="review" 
                    className="w-4 h-4 cursor-pointer accent-black" 
                    checked={!!reviewFlags[currentTaskIndex]}
                    onChange={handleReviewToggle}
                  />
                  <label htmlFor="review" className="text-[14px] font-bold text-black cursor-pointer mt-0.5 whitespace-nowrap">Review</label>
                </div>
                
                <div className="flex-1 flex justify-start sm:justify-center items-center gap-1.5 overflow-x-auto px-6 py-1 custom-scrollbar min-w-0">
                   {allQuestions.map((q, idx) => {
                      const isActive = idx === currentTaskIndex;
                      const isReview = reviewFlags[idx];
                      
                      const shapeClass = isReview ? 'rounded-full' : 'rounded-none';
                      const bgClass = isActive ? 'bg-slate-900 text-white border-black shadow-inner' : 'bg-white text-black border-slate-400 hover:bg-slate-200 cursor-pointer';

                      return (
                        <div key={q.id} className="flex items-center gap-3 h-full">
                           <span className="text-[14px] font-bold text-black hidden sm:block">Part {idx + 1}:</span>
                           <button 
                             onClick={() => setCurrentTaskIndex(idx)}
                             className={`w-9 h-9 flex items-center justify-center font-bold text-[14px] border transition-all ${shapeClass} ${bgClass}`}
                           >
                             {idx + 1}
                           </button>
                        </div>
                      )
                   })}
                </div>
             </div>

             <div className="flex items-center gap-4 shrink-0 pl-6 border-l border-slate-400">
                <button className="text-slate-500 hover:text-black transition text-lg px-2 hidden md:block" title="Minimize/Maximize">↙</button>
                
                <div className="flex items-center gap-2 hidden sm:flex ml-2">
                   <button onClick={() => setCurrentTaskIndex(prev => Math.max(0, prev - 1))} disabled={currentTaskIndex === 0} className="w-8 h-8 flex items-center justify-center text-black hover:bg-slate-200 border border-slate-400 bg-white rounded-none transition disabled:opacity-30">←</button>
                   <button onClick={() => setCurrentTaskIndex(prev => Math.min(allQuestions.length - 1, prev + 1))} disabled={currentTaskIndex === allQuestions.length - 1} className="w-8 h-8 flex items-center justify-center text-black hover:bg-slate-200 border border-slate-400 bg-white rounded-none transition disabled:opacity-30">→</button>
                </div>
                
                <button 
                  onClick={handleSubmit}
                  className="bg-slate-900 hover:bg-black text-white px-6 py-2 rounded-none text-[14px] font-bold transition ml-2 uppercase tracking-wide"
                >
                  Nộp bài
                </button>
             </div>

          </footer>

        </div>
      )}

      {isSubmitted && aiResult && (
        <main className="flex-1 overflow-y-auto p-4 md:p-8 custom-scrollbar bg-[#f4f4f4]">
          <div className="max-w-6xl mx-auto space-y-8">
            
            <div className="bg-white p-8 rounded-none border border-slate-400 flex flex-col md:flex-row gap-8 items-center justify-center">
              <div className="text-center">
                <span className="text-sm font-bold text-slate-600 uppercase tracking-widest block mb-2">Overall Band Score</span>
                <span className="text-6xl font-black text-black border-4 border-black px-8 py-4 rounded-none block">{aiResult.overall}</span>
              </div>
            </div>

            <div className="bg-white p-8 rounded-none border border-slate-400">
                <h3 className="font-black text-xl text-black mb-4 flex items-center gap-2">💡 Nhận xét tổng quan</h3>
                <div className="p-5 bg-[#e0e0e0] border border-slate-400 rounded-none text-[15px] leading-[1.8] font-bold text-black font-serif">
                  {aiResult.generalFeedback}
                </div>
            </div>

            {Array.isArray(aiResult.tasks) && aiResult.tasks.map((task: any, idx: number) => (
              <div className="bg-white p-8 rounded-none border border-slate-400" key={idx}>
                <div className="flex justify-between items-center mb-6 pb-4 border-b border-slate-400">
                  <h3 className="font-black text-2xl text-black">{task.task_name}</h3>
                  <span className="font-black text-xl text-white bg-black px-4 py-1.5 rounded-none">Band {task.score}</span>
                </div>
                
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
                  {Array.isArray(task.criteria) && task.criteria.map((c: any, i: number) => (
                    <div key={i} className="bg-[#f4f4f4] p-4 rounded-none border border-slate-400">
                      <div className="flex justify-between items-center mb-2">
                        <span className="font-bold text-black">{c.name}</span>
                        <span className="font-black text-black text-lg">{c.score}</span>
                      </div>
                      <p className="text-sm text-slate-800 font-medium leading-relaxed font-serif">{c.comment}</p>
                    </div>
                  ))}
                </div>

                <div>
                  <h4 className="font-black text-lg text-black mb-4">✍️ Bài làm & Gợi ý sửa lỗi</h4>
                  <div className="p-6 bg-[#e0e0e0] border border-slate-400 rounded-none text-[16px] leading-[1.8] font-serif text-black" dangerouslySetInnerHTML={{__html: task.feedback}} />
                </div>
              </div>
            ))}
          </div>
        </main>
      )}
    </div>
  );
}