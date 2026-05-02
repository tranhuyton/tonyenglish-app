import React, { useState, useEffect } from 'react';
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
                allQuestions.push({ ...q, partTitle: p.title, partContent: p.content, secTitle: s.title, secContent: s.content });
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
        ${JSON.stringify(allQuestions.map((q, i) => `Task ${i+1} (${q.partTitle}): ${q.content}`))}

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

      // GỌI QUA SUPABASE EDGE FUNCTION VỚI THAM SỐ MODEL
      const { data, error } = await supabase.functions.invoke('ai-grader', {
        body: { 
           prompt: prompt,
           model: 'gemini-2.5-flash' // Anh có thể đổi thành 'gemini-2.5-pro' tại đây
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
    return <div className="h-screen w-full flex items-center justify-center bg-[#f4f5f7] font-bold text-slate-500">Loading test data...</div>;
  }

  return (
    <div className="h-screen flex flex-col bg-[#f0f2f5] font-sans text-slate-800 overflow-hidden">
      
      <header className="h-[46px] bg-[#323639] text-white flex justify-between items-center px-4 shrink-0 select-none z-20 shadow-sm relative">
        <div className="flex items-center gap-2">
          <UserIcon />
          <span className="font-bold text-[14px] truncate max-w-[200px] md:max-w-xs text-slate-200">{basicInfo.title}</span>
        </div>
        
        <div className={`absolute left-1/2 -translate-x-1/2 font-bold text-[14px] tracking-wide ${timeLeft <= 300 ? 'text-red-400 animate-pulse' : 'text-white'}`}>
           {isSubmitted ? 'TEST FINISHED' : formatTime(timeLeft)}
        </div>

        <div className="flex items-center gap-4">
           {isSubmitted ? (
              <button onClick={onBack} className="text-[13px] font-bold border border-white/40 px-3 py-1.5 rounded hover:bg-white/10 transition text-white">Return to Home</button>
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
             <svg className="absolute inset-0 w-full h-full animate-spin text-[#323639]" viewBox="0 0 100 100">
               <circle cx="50" cy="50" r="45" fill="none" stroke="currentColor" strokeWidth="8" strokeDasharray="200" strokeLinecap="round" />
             </svg>
             <span className="font-bold text-xl text-slate-800">AI</span>
          </div>
          <h2 className="text-xl font-bold text-slate-800 mb-2">Grading in Progress</h2>
          <p className="text-slate-500 text-sm">Please wait while the AI examiner analyzes your essay...</p>
        </div>
      )}

      {!isSubmitted && !isGrading && currentTask && (
        <div className="flex-1 flex flex-col overflow-hidden bg-[#f4f5f7]">
          
          <div className="h-[54px] bg-white border-b border-slate-300 flex items-center px-8 shrink-0 shadow-sm z-10">
            <h2 className="font-bold text-[18px] text-slate-900">{currentTask.partTitle}:</h2>
          </div>

          <main className="flex-1 flex flex-col md:flex-row overflow-hidden relative">
            
            <section className="w-full md:w-1/2 p-8 md:p-10 overflow-y-auto custom-scrollbar border-r border-slate-300 flex flex-col">
              <div className="max-w-2xl text-[16px] leading-[1.8] text-slate-800">
                {currentTask.partContent && (
                  <div className="mb-6 text-[15px] font-normal" dangerouslySetInnerHTML={{__html: currentTask.partContent}} />
                )}
                {currentTask.content && (
                  <div className="font-bold mb-6 whitespace-pre-wrap text-black text-[16px] tracking-tight leading-[1.8]">{currentTask.content}</div>
                )}
                {currentTask.secContent && (
                  <div className="mb-6 text-[15px] font-normal whitespace-pre-wrap" dangerouslySetInnerHTML={{__html: currentTask.secContent}} />
                )}
                {currentTask.imageUrl && (
                  <img src={currentTask.imageUrl} alt="Diagram" className="max-w-full rounded border border-slate-300 mt-4 shadow-sm" />
                )}
              </div>
            </section>

            <section className="w-full md:w-1/2 p-8 md:p-10 flex flex-col overflow-hidden relative">
              
              <div className="flex-1 bg-white border border-slate-300 rounded shadow-sm flex flex-col overflow-hidden">
                <div className="h-12 border-b border-slate-200 flex items-center px-4 gap-6 shrink-0 bg-[#fbfbfb]">
                   <div className="flex gap-4 border-r border-slate-300 pr-6 text-slate-400">
                      <button className="hover:text-slate-700 transition" title="Undo"><UndoIcon /></button>
                      <button className="hover:text-slate-700 transition" title="Redo"><RedoIcon /></button>
                   </div>
                   <div className="flex items-center gap-4 text-slate-600">
                      <span className="font-serif font-bold text-[14px] cursor-pointer hover:text-black">A <span className="text-[10px] text-slate-400">▼</span></span>
                      <button className="w-7 h-7 hover:bg-slate-200 flex items-center justify-center rounded transition"><BoldIcon /></button>
                      <button className="w-7 h-7 hover:bg-slate-200 flex items-center justify-center rounded transition"><ItalicIcon /></button>
                      <button className="w-7 h-7 hover:bg-slate-200 flex items-center justify-center rounded transition"><UnderlineIcon /></button>
                   </div>
                </div>
                
                <textarea 
                  className="flex-1 w-full p-8 outline-none resize-none text-[16px] text-black font-sans custom-scrollbar leading-[1.8]"
                  placeholder=""
                  value={answers[currentTask.id] || ''}
                  onChange={(e) => handleAnswerChange(currentTask.id, e.target.value)}
                  spellCheck="false"
                />
              </div>
              
              <div className="mt-3 text-[14px] text-slate-600 font-medium">
                Word Count: {getWordCount(answers[currentTask.id])}
              </div>

            </section>
          </main>

          <footer className="h-[60px] bg-[#f8f9fa] border-t border-slate-200 flex justify-between items-center px-8 shrink-0 select-none">
             
             <div className="flex items-center h-full">
                <label className="flex items-center gap-2 cursor-pointer h-full pr-8 border-r border-[#e0e6ed]">
                   <input 
                     type="checkbox" 
                     className="w-4 h-4 cursor-pointer accent-[#323639]" 
                     checked={!!reviewFlags[currentTaskIndex]}
                     onChange={handleReviewToggle}
                   />
                   <span className="text-[15px] font-bold text-[#2c3e50] mt-0.5">Review</span>
                </label>
                
                <div className="flex items-center gap-6 h-full pl-8">
                   {allQuestions.map((q, idx) => {
                      const isActive = idx === currentTaskIndex;
                      const isReview = reviewFlags[idx];
                      
                      const shapeClass = isReview ? 'rounded-full' : 'rounded-sm';
                      const bgClass = isActive ? 'bg-[#323639] text-white border-[#323639]' : 'bg-white text-[#2c3e50] border-[#d2dce5] hover:bg-slate-50';

                      return (
                        <div key={q.id} className="flex items-center gap-3 h-full">
                           <span className="text-[14px] font-medium text-[#2c3e50] hidden sm:block">Part {idx + 1}:</span>
                           <button 
                             onClick={() => setCurrentTaskIndex(idx)}
                             className={`w-9 h-10 flex items-center justify-center font-bold text-[14px] border transition-all ${shapeClass} ${bgClass}`}
                           >
                             {idx + 1}
                           </button>
                        </div>
                      )
                   })}
                </div>
             </div>

             <div className="flex items-center gap-6">
                <button className="text-slate-400 hover:text-black transition text-lg px-2 hidden md:block" title="Minimize/Maximize">↙</button>
                
                <div className="flex items-center gap-3 ml-2">
                   <button onClick={() => setCurrentTaskIndex(prev => Math.max(0, prev - 1))} disabled={currentTaskIndex === 0} className="w-10 h-10 flex items-center justify-center text-slate-400 hover:text-[#2c3e50] border border-[#d2dce5] bg-white rounded-sm transition disabled:opacity-30">←</button>
                   <button onClick={() => setCurrentTaskIndex(prev => Math.min(allQuestions.length - 1, prev + 1))} disabled={currentTaskIndex === allQuestions.length - 1} className="w-10 h-10 flex items-center justify-center text-slate-400 hover:text-[#2c3e50] border border-[#d2dce5] bg-white rounded-sm transition disabled:opacity-30">→</button>
                </div>
                
                <button 
                  onClick={handleSubmit}
                  className="bg-[#323639] hover:bg-[#1a1c1e] text-white px-10 py-2.5 rounded-sm text-[15px] font-bold shadow-sm transition active:scale-95 ml-4"
                >
                  Nộp bài
                </button>
             </div>

          </footer>

        </div>
      )}

      {isSubmitted && aiResult && (
        <main className="flex-1 overflow-y-auto p-4 md:p-8 custom-scrollbar bg-[#f8f9fa]">
          <div className="max-w-6xl mx-auto space-y-8">
            
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 flex flex-col md:flex-row gap-8 items-center justify-center">
              <div className="text-center">
                <span className="text-sm font-bold text-slate-500 uppercase tracking-widest block mb-2">Overall Band Score</span>
                <span className="text-6xl font-black text-[#1ea1db] bg-blue-50 px-8 py-4 rounded-3xl border-4 border-blue-100 shadow-inner block">{aiResult.overall}</span>
              </div>
            </div>

            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
                <h3 className="font-black text-xl text-slate-800 mb-4 flex items-center gap-2">💡 Nhận xét tổng quan</h3>
                <div className="p-5 bg-slate-50 border border-slate-200 rounded-xl text-[15px] leading-[1.8] font-medium text-slate-800">
                  {aiResult.generalFeedback}
                </div>
            </div>

            {Array.isArray(aiResult.tasks) && aiResult.tasks.map((task: any, idx: number) => (
              <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200" key={idx}>
                <div className="flex justify-between items-center mb-6 pb-4 border-b border-slate-100">
                  <h3 className="font-black text-2xl text-slate-800">{task.task_name}</h3>
                  <span className="font-black text-xl text-white bg-[#1ea1db] px-4 py-1.5 rounded-xl shadow-sm">Band {task.score}</span>
                </div>
                
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
                  {Array.isArray(task.criteria) && task.criteria.map((c: any, i: number) => (
                    <div key={i} className="bg-slate-50 p-4 rounded-xl border border-slate-200">
                      <div className="flex justify-between items-center mb-2">
                        <span className="font-bold text-slate-700">{c.name}</span>
                        <span className="font-black text-[#1ea1db] text-lg">{c.score}</span>
                      </div>
                      <p className="text-sm text-slate-600 font-medium leading-relaxed">{c.comment}</p>
                    </div>
                  ))}
                </div>

                <div>
                  <h4 className="font-black text-lg text-slate-700 mb-4">✍️ Bài làm & Gợi ý sửa lỗi</h4>
                  <div className="p-6 bg-[#f4f5f7] border border-slate-200 rounded-xl text-[16px] leading-[1.8] font-serif text-slate-800" dangerouslySetInnerHTML={{__html: task.feedback}} />
                </div>
              </div>
            ))}
          </div>
        </main>
      )}
    </div>
  );
}