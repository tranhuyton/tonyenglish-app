import React, { useState, useRef, useEffect } from 'react';
import { supabase } from './supabase';
import './tailwind.css';

// --- BỘ ICON CHUẨN IDP ---
const UserIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path fillRule="evenodd" d="M7.5 6a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM3.751 20.105a8.25 8.25 0 0116.498 0 .75.75 0 01-.437.695A18.683 18.683 0 0112 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 01-.437-.695z" clipRule="evenodd" /></svg>;
const SettingsIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path fillRule="evenodd" d="M11.078 2.25c-.917 0-1.699.663-1.85 1.567L9.05 4.889c-.02.12-.115.26-.297.348a7.493 7.493 0 00-.986.57c-.166.115-.334.126-.45.083L6.3 5.508a1.875 1.875 0 00-2.282.819l-.922 1.597a1.875 1.875 0 00.432 2.385l.84.692c.097.078.15.222.15.399v.111c0 .177-.053.321-.15.399l-.84.692a1.875 1.875 0 00-.432 2.385l.922 1.597a1.875 1.875 0 002.282.818l1.019-.382c.115-.043.283-.031.45.082.312.214.641.405.985.57.182.088.277.228.297.35l.178 1.071c.151.904.933 1.567 1.85 1.567h1.844c.916 0 1.699-.663 1.85-1.567l.178-1.072c.02-.12.114-.26.297-.349.344-.165.673-.356.985-.57.167-.114.335-.125.45-.082l1.02.382a1.875 1.875 0 002.28-.819l.923-1.597a1.875 1.875 0 00-.432-2.385l-.84-.692c-.098-.078-.15-.222-.15-.399v-.111c0-.177.052-.321.15-.399l.84-.692a1.875 1.875 0 00.432-2.385l-.923-1.597a1.875 1.875 0 00-2.28-.818l-1.02.382c-.114.043-.282.031-.449-.083a7.49 7.49 0 00-.985-.57c-.183-.087-.277-.227-.297-.348l-.179-1.072a1.875 1.875 0 00-1.85-1.567h-1.843zM12 15.75a3.75 3.75 0 110-7.5 3.75 3.75 0 010 7.5z" clipRule="evenodd" /></svg>;
const NoteIcon = () => <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L6.832 19.82a4.5 4.5 0 01-1.89.11l-3.125-3.125a4.5 4.5 0 011.11-1.89l12.45-12.45c.414-.415 1.086-.415 1.498 0z" /></svg>;
const MicIcon = () => <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" d="M12 18.75a6 6 0 006-6v-1.5m-6 7.5a6 6 0 01-6-6v-1.5m6 7.5v3.75m-3.75 0h7.5M12 15.75a3 3 0 01-3-3V4.5a3 3 0 116 0v8.25a3 3 0 01-3 3z" /></svg>;
const StopIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-6 h-6"><path fillRule="evenodd" d="M4.5 7.5a3 3 0 013-3h9a3 3 0 013 3v9a3 3 0 01-3 3h-9a3 3 0 01-3-3v-9z" clipRule="evenodd" /></svg>;
const PlayIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path fillRule="evenodd" d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z" clipRule="evenodd" /></svg>;
const TrashIcon = () => <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" /></svg>;

export default function IeltsSpeaking({ onBack, testData: propTestData, onFinish }: { onBack?: () => void, testData?: any, onFinish?: (res: any) => void }) {
  
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
  const basicInfo = contentJSON?.basicInfo || { title: "IELTS Speaking", timeLimit: "15" };
  const parts = Array.isArray(contentJSON?.parts) ? contentJSON.parts : [];

  const allQuestions: any[] = [];
  if (Array.isArray(parts)) {
    parts.forEach((p: any, pIdx: number) => {
      if (p && Array.isArray(p.sections)) {
        p.sections.forEach((s: any, sIdx: number) => {
          if (s && Array.isArray(s.questions)) {
            s.questions.forEach((q: any, qIdx: number) => {
              if (q) {
                let maxTime = 30;
                const partNameLower = (p.title || '').toLowerCase();
                if (partNameLower.includes('part 2') || partNameLower.includes('cue card')) maxTime = 120;
                else if (partNameLower.includes('part 3') || partNameLower.includes('discussion')) maxTime = 60;

                allQuestions.push({
                  ...q,
                  globalIndex: allQuestions.length,
                  partTitle: p.title,
                  partContent: p.content,
                  partIndex: pIdx,
                  secTitle: s.title,
                  secIndex: sIdx,
                  maxTime: maxTime,
                  isPart2: maxTime === 120 
                });
              }
            });
          }
        });
      }
    });
  }

  const [currentQIndex, setCurrentQIndex] = useState(0);
  const currentQ = allQuestions[currentQIndex];
  const totalQuestions = allQuestions.length;

  const [notes, setNotes] = useState<Record<string, string>>({}); 
  const [recordedBlobs, setRecordedBlobs] = useState<Record<string, Blob[]>>({}); 
  const [audioUrls, setAudioUrls] = useState<Record<string, string>>({}); 
  const [reviewFlags, setReviewFlags] = useState<Record<number, boolean>>({});

  const [isRecording, setIsRecording] = useState(false);
  const [recordingTime, setRecordingTime] = useState(0);
  
  const [isGrading, setIsGrading] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [aiResult, setAiResult] = useState<any>(null);

  const parseTime = (t: any) => parseInt(t) || 15; 
  const [timeLeft, setTimeLeft] = useState(() => parseTime(basicInfo.timeLimit) * 60);

  useEffect(() => {
    if (isSubmitted || isGrading) return;
    const timer = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) { clearInterval(timer); handleFinalSubmit(); return 0; }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timer);
  }, [isSubmitted, isGrading]);

  const formatTime = (secs: number) => {
    if (isNaN(secs)) return '00:00';
    const m = Math.floor(secs / 60).toString().padStart(2, '0');
    const s = (secs % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  };

  const formatTotalTime = (secs: number) => {
    if (isNaN(secs)) return '15 minutes left';
    const m = Math.floor(secs / 60);
    return `${m} minutes left`;
  };

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const timerRef = useRef<any>(null);

  const startRecording = async () => {
    if (!currentQ?.id) return;
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;
      audioChunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) audioChunksRef.current.push(event.data);
      };

      mediaRecorder.onstop = () => {
        stream.getTracks().forEach(track => track.stop());
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
        const audioUrl = URL.createObjectURL(audioBlob);
        
        setRecordedBlobs(prev => ({ ...prev, [currentQ.id]: [...audioChunksRef.current] }));
        setAudioUrls(prev => ({ ...prev, [currentQ.id]: audioUrl }));
      };

      mediaRecorder.start();
      setIsRecording(true);
      setRecordingTime(0);

      timerRef.current = setInterval(() => {
        setRecordingTime(prev => {
           if (prev >= currentQ.maxTime - 1) {
              stopRecording();
              return currentQ.maxTime;
           }
           return prev + 1;
        });
      }, 1000);
    } catch (err) {
      alert("System Error: Unable to access microphone. Please check your browser permissions.");
      console.error(err);
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
      clearInterval(timerRef.current);
    }
  };

  const deleteRecording = () => {
    if (!window.confirm("Bạn có chắc chắn muốn xóa file ghi âm này để thu lại từ đầu?")) return;
    const newBlobs = { ...recordedBlobs }; delete newBlobs[currentQ.id];
    const newUrls = { ...audioUrls }; delete newUrls[currentQ.id];
    setRecordedBlobs(newBlobs);
    setAudioUrls(newUrls);
    setRecordingTime(0);
  };

  const handleReviewToggle = () => {
    setReviewFlags(prev => ({ ...prev, [currentQIndex]: !prev[currentQIndex] }));
  };

  const goToNext = () => {
    if (isRecording) stopRecording(); 
    if (currentQIndex < totalQuestions - 1) setCurrentQIndex(prev => prev + 1);
  };
  const goToPrev = () => {
    if (isRecording) stopRecording();
    if (currentQIndex > 0) setCurrentQIndex(prev => prev - 1);
  };
  const goToQuestion = (idx: number) => {
    if (isRecording) stopRecording();
    setCurrentQIndex(idx);
  };

  const blobToBase64 = (blob: Blob): Promise<string> => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onloadend = () => resolve((reader.result as string).split(',')[1]);
      reader.onerror = reject;
      reader.readAsDataURL(blob);
    });
  };

  const handleFinalSubmit = async () => {
    if (isRecording) stopRecording();
    
    const answeredQuestions = Object.keys(recordedBlobs).length;
    if (answeredQuestions === 0) {
      alert("Bạn chưa ghi âm câu nào cả! Vui lòng thu âm ít nhất 1 câu trước khi nộp bài.");
      return;
    }

    if (!window.confirm(`Bạn đã hoàn thành ${answeredQuestions}/${totalQuestions} câu. Bạn đã sẵn sàng nộp bài cho Giám khảo AI?`)) return;

    setIsGrading(true);

    try {
      const allChunks: Blob[] = [];
      allQuestions.forEach(q => { if (recordedBlobs[q.id]) allChunks.push(...recordedBlobs[q.id]); });
      const combinedBlob = new Blob(allChunks, { type: 'audio/webm' });
      const base64Audio = await blobToBase64(combinedBlob);

      const prompt = `
        Bạn là Giám khảo IELTS. Hãy nghe đoạn ghi âm tổng hợp các câu trả lời sau:
        ${JSON.stringify(allQuestions.map((q, i) => `Câu ${i+1} (${q.partTitle}): ${q.content}`))}
        
        Nhiệm vụ:
        1. Chấm điểm Overall và 4 tiêu chí.
        2. Cung cấp Lời giải chi tiết (Transcript).
        3. Đưa ra các gợi ý cải thiện Phát âm, Từ vựng, Trôi chảy.
        
        LƯU Ý ĐỊNH DẠNG:
        - KHÔNG dùng dấu ngoặc kép (") bên trong nội dung string. Dùng dấu (').
        - Trả về ĐÚNG CẤU TRÚC JSON sau:
        {
          "overall": 6.5,
          "criteria": {
            "pronunciation": 6.0,
            "grammar": 6.5,
            "lexicalResource": 7.0,
            "fluency": 6.5
          },
          "transcript": "Văn bản bóc băng...",
          "feedback": {
            "general": "Nhận xét tổng quan...",
            "pronunciation": "Các lỗi phát âm cần sửa...",
            "vocabulary": "Từ vựng có thể nâng cấp...",
            "fluency": "Cách nói trôi chảy hơn...",
            "modelAnswer": "Gợi ý câu trả lời mẫu..."
          }
        }
      `;

      // GỌI QUA SUPABASE EDGE FUNCTION KÈM THAM SỐ MODEL
      const { data, error } = await supabase.functions.invoke('ai-grader', {
        body: { 
          prompt: prompt,
          base64Audio: base64Audio,
          model: 'gemini-2.5-flash' // Chỉnh sửa model tùy thích tại đây
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
          test_type: 'IELTS-Speaking',
          score: parsedResult.overall,
          total_score: 9,
          time_spent: (parseTime(basicInfo.timeLimit) * 60) - timeLeft,
          details: { test_id: safeData?.id, aiFeedback: parsedResult, bandScore: parsedResult.overall }
        }]);
      }
    } catch (error: any) {
      console.error("LỖI CHI TIẾT:", error);
      alert("System Error during AI grading. Please try again: " + error.message);
    } finally {
      setIsGrading(false);
    }
  };

  if (!testData || allQuestions.length === 0) return <div className="h-screen flex items-center justify-center bg-[#f4f5f7] font-bold text-slate-500">Loading test data...</div>;

  return (
    <div className="h-screen flex flex-col bg-[#f0f2f5] font-sans text-slate-800 overflow-hidden">
      
      <header className="h-[46px] bg-[#323639] text-white flex justify-between items-center px-4 shrink-0 select-none z-20 shadow-sm relative">
        <div className="flex items-center gap-2">
          <UserIcon />
          <span className="font-bold text-[14px] truncate max-w-[200px] md:max-w-xs text-slate-200">{basicInfo.title}</span>
        </div>
        
        <div className={`absolute left-1/2 -translate-x-1/2 font-bold text-[14px] tracking-wide ${timeLeft <= 300 ? 'text-red-400 animate-pulse' : 'text-white'}`}>
           {isSubmitted ? 'TEST FINISHED' : formatTotalTime(timeLeft)}
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
          <p className="text-slate-500 text-sm">Please wait while the AI examiner analyzes your responses...</p>
        </div>
      )}

      {!isSubmitted && !isGrading && currentQ && (
        <div className="flex-1 flex flex-col overflow-hidden bg-[#f4f5f7]">
          
          <div className="h-[54px] bg-white border-b border-slate-300 flex items-center px-8 shrink-0 shadow-sm z-10">
            <h2 className="font-bold text-[18px] text-slate-900">{currentQ.partTitle}:</h2>
          </div>

          <main className="flex-1 flex flex-col md:flex-row overflow-hidden relative">
            
            <section className="w-full md:w-1/2 p-8 md:p-10 overflow-y-auto custom-scrollbar border-r border-slate-300 flex flex-col">
              <div className="max-w-2xl text-[16px] leading-[1.8] text-slate-800">
                {currentQ.partContent && (
                  <div className="mb-6 text-[15px] font-normal" dangerouslySetInnerHTML={{__html: currentQ.partContent}} />
                )}
                {currentQ.content && (
                  <div className={`font-bold mb-6 whitespace-pre-wrap text-black text-[16px] tracking-tight leading-[1.8] ${currentQ.isPart2 ? 'bg-[#fffae6] p-6 border border-amber-200 rounded shadow-sm' : ''}`}>
                    {currentQ.secTitle && currentQ.secTitle.toLowerCase() !== 'section 1' && <div className="font-bold mb-3">{currentQ.secTitle}</div>}
                    {currentQ.content}
                  </div>
                )}
              </div>
            </section>

            <section className="w-full md:w-1/2 bg-[#f4f5f7] flex flex-col overflow-hidden relative">
              
              <div className="flex-1 p-8 md:p-10 pb-0 flex flex-col overflow-hidden">
                  <div className="flex-1 bg-white border border-slate-300 rounded shadow-sm flex flex-col overflow-hidden">
                    <div className="h-12 border-b border-slate-200 flex items-center px-4 gap-2 shrink-0 bg-[#fbfbfb]">
                       <NoteIcon />
                       <span className="text-[13px] font-bold text-slate-700">Notes</span>
                    </div>
                    <textarea 
                      className="flex-1 w-full p-6 outline-none resize-none text-[15px] text-black font-sans custom-scrollbar leading-[1.8]"
                      placeholder="You can make some notes here..."
                      value={notes[currentQ.id] || ''}
                      onChange={(e) => setNotes(prev => ({...prev, [currentQ.id]: e.target.value}))}
                      spellCheck="false"
                    />
                  </div>
              </div>

              <div className="p-8 md:p-10 shrink-0">
                  <div className="h-[90px] bg-white border border-slate-300 rounded shadow-sm flex items-center justify-between px-6">
                      
                      {audioUrls[currentQ.id] ? (
                         <div className="flex items-center gap-4 w-full">
                            <button onClick={() => { const audio = new Audio(audioUrls[currentQ.id]); audio.play(); }} className="w-10 h-10 bg-slate-100 border border-slate-300 rounded flex items-center justify-center hover:bg-slate-200 text-[#323639] transition">
                               <PlayIcon />
                            </button>
                            <div className="flex-1 h-2 bg-slate-200 rounded-full overflow-hidden">
                               <div className="h-full bg-[#323639] w-full rounded-full"></div>
                            </div>
                            <span className="text-[13px] font-bold text-slate-500 hidden sm:block">Recorded</span>
                            <button onClick={deleteRecording} className="w-10 h-10 rounded text-slate-500 hover:text-red-500 hover:bg-red-50 transition flex items-center justify-center ml-2 border border-slate-200" title="Delete & Retake">
                               <TrashIcon />
                            </button>
                         </div>
                      ) : (
                         <div className="flex items-center gap-6 w-full">
                            {isRecording ? (
                               <button onClick={stopRecording} className="px-6 py-2.5 bg-red-600 hover:bg-red-700 text-white font-bold rounded flex items-center gap-2 transition shadow-sm active:scale-95 text-[14px]">
                                 <StopIcon /> Stop
                               </button>
                            ) : (
                               <button onClick={startRecording} className="px-6 py-2.5 bg-[#323639] hover:bg-[#1a1c1e] text-white font-bold rounded flex items-center gap-2 transition shadow-sm active:scale-95 text-[14px]">
                                 <MicIcon /> Record
                               </button>
                            )}
                            
                            {isRecording ? (
                               <div className="font-mono text-[16px] text-red-600 font-bold tracking-widest tabular-nums flex items-center gap-2">
                                 <span className="w-2.5 h-2.5 bg-red-600 rounded-full animate-pulse"></span>
                                 {formatTime(recordingTime)} <span className="text-slate-400">/ {formatTime(currentQ.maxTime)}</span>
                               </div>
                            ) : (
                               <div className="text-[13px] text-slate-500 font-medium">Max time: {formatTime(currentQ.maxTime)}</div>
                            )}
                         </div>
                      )}

                  </div>
              </div>

            </section>
          </main>

          <footer className="h-[60px] bg-[#f8f9fa] border-t border-slate-300 flex justify-between items-center px-6 shrink-0 select-none overflow-x-auto custom-scrollbar">
             
             <div className="flex items-center h-full shrink-0">
                <label className="flex items-center gap-2 cursor-pointer h-full pr-6 border-r border-[#e0e6ed]">
                   <input 
                     type="checkbox" 
                     className="w-4 h-4 cursor-pointer accent-[#323639]" 
                     checked={!!reviewFlags[currentQIndex]}
                     onChange={handleReviewToggle}
                   />
                   <span className="text-[15px] font-bold text-[#2c3e50] mt-0.5">Review</span>
                </label>
                
                <div className="flex items-center gap-3 h-full pl-6">
                   {allQuestions.map((q, idx) => {
                      const isActive = idx === currentQIndex;
                      const isReview = reviewFlags[idx];
                      const isAnswered = !!recordedBlobs[q.id];
                      
                      const shapeClass = isReview ? 'rounded-full' : 'rounded-sm';
                      
                      let bgClass = 'bg-white text-[#2c3e50] border-slate-300 hover:bg-slate-100';
                      if (isActive) bgClass = 'bg-[#323639] text-white border-[#323639]';
                      else if (isAnswered) bgClass = 'bg-[#e0e6ed] text-slate-700 border-[#d2dce5] underline decoration-2 underline-offset-2';

                      return (
                        <button 
                          key={q.id} 
                          onClick={() => goToQuestion(idx)}
                          className={`w-8 h-9 flex items-center justify-center font-bold text-[13px] border transition-all ${shapeClass} ${bgClass}`}
                          title={`Part ${q.partIndex + 1} - Question ${idx + 1}`}
                        >
                          {idx + 1}
                        </button>
                      )
                   })}
                </div>
             </div>

             <div className="flex items-center gap-6 shrink-0 pl-6">
                <div className="flex items-center gap-3">
                   <button onClick={goToPrev} disabled={currentQIndex === 0} className="w-9 h-9 flex items-center justify-center text-slate-500 hover:text-[#2c3e50] border border-slate-300 bg-white rounded-sm transition disabled:opacity-30">←</button>
                   <button onClick={goToNext} disabled={currentQIndex === totalQuestions - 1} className="w-9 h-9 flex items-center justify-center text-slate-500 hover:text-[#2c3e50] border border-slate-300 bg-white rounded-sm transition disabled:opacity-30">→</button>
                </div>
                
                <button 
                  onClick={handleFinalSubmit}
                  className="bg-[#323639] hover:bg-[#1a1c1e] text-white px-8 py-2.5 rounded-sm text-[14px] font-bold shadow-sm transition active:scale-95"
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
                <span className="text-6xl font-black text-[#323639] bg-slate-100 px-8 py-4 rounded-3xl border-4 border-slate-200 shadow-inner block">{aiResult.overall}</span>
              </div>
            </div>

            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
                <h3 className="font-black text-xl text-slate-800 mb-4 flex items-center gap-2">💡 Nhận xét tổng quan</h3>
                <div className="p-5 bg-slate-50 border border-slate-200 rounded-xl text-[15px] leading-[1.8] font-medium text-slate-800">
                  {aiResult.generalFeedback || 'Hệ thống đã ghi nhận bài thi Speaking của bạn.'}
                </div>
            </div>

            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
                <div className="flex justify-between items-center mb-6 pb-4 border-b border-slate-100">
                  <h3 className="font-black text-2xl text-slate-800">Chi tiết các tiêu chí</h3>
                </div>
                
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
                   <div className="bg-slate-50 p-5 rounded-xl border border-slate-200 text-center">
                      <div className="text-[12px] text-slate-500 font-bold uppercase mb-2">Pronunciation</div>
                      <div className="text-3xl font-black text-[#323639]">{aiResult.criteria?.pronunciation || 0.0}</div>
                   </div>
                   <div className="bg-slate-50 p-5 rounded-xl border border-slate-200 text-center">
                      <div className="text-[12px] text-slate-500 font-bold uppercase mb-2">Grammar</div>
                      <div className="text-3xl font-black text-[#323639]">{aiResult.criteria?.grammar || 0.0}</div>
                   </div>
                   <div className="bg-slate-50 p-5 rounded-xl border border-slate-200 text-center">
                      <div className="text-[12px] text-slate-500 font-bold uppercase mb-2">Lexical Resource</div>
                      <div className="text-3xl font-black text-[#323639]">{aiResult.criteria?.lexicalResource || 0.0}</div>
                   </div>
                   <div className="bg-slate-50 p-5 rounded-xl border border-slate-200 text-center">
                      <div className="text-[12px] text-slate-500 font-bold uppercase mb-2">Fluency</div>
                      <div className="text-3xl font-black text-[#323639]">{aiResult.criteria?.fluency || 0.0}</div>
                   </div>
                </div>

                <div className="space-y-6 mt-8">
                   <div>
                      <h4 className="font-bold text-slate-700 mb-3 uppercase tracking-widest text-[13px]">🎧 Bóc băng (Transcript)</h4>
                      <div className="p-5 bg-[#f4f5f7] border border-slate-200 rounded-lg text-[15px] leading-[1.8] font-serif text-slate-600 italic whitespace-pre-wrap">
                         "{aiResult.transcript}"
                      </div>
                   </div>
                   
                   {aiResult.detailedFeedback && (
                   <div>
                      <h4 className="font-bold text-slate-700 mb-3 uppercase tracking-widest text-[13px]">💡 Gợi ý sửa lỗi</h4>
                      <div className="p-5 bg-blue-50 border border-blue-100 rounded-lg text-[15px] leading-[1.8] font-medium text-blue-900 whitespace-pre-wrap">
                         {aiResult.detailedFeedback}
                      </div>
                   </div>
                   )}
                </div>
            </div>

          </div>
        </main>
      )}
    </div>
  );
}