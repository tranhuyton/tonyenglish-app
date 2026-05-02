import React, { useState, useRef, useEffect } from 'react';
import { supabase } from './supabase';

export default function SplitScreenTest({ onBack }: { onBack?: () => void }) {
  // LẤY ĐÚNG ĐỀ THI TỪ THƯ VIỆN TRUYỀN VÀO (Không tải lung tung từ bảng cũ nữa)
  const [testData, setTestData] = useState<any>(() => {
     const saved = sessionStorage.getItem('lms_current_test');
     return saved ? JSON.parse(saved) : null;
  });
  const [isLoading, setIsLoading] = useState(!testData);

  // KHÔI PHỤC BẢN NHÁP TỪ TRƯỚC (NẾU CÓ) ĐỂ CHỐNG F5 MẤT CHỮ
  const [answers, setAnswers] = useState<Record<string, string>>(() => {
     if (!testData?.id) return {};
     try {
        const saved = localStorage.getItem(`case_study_ans_${testData.id}`);
        return saved ? JSON.parse(saved) : {};
     } catch(e) { return {}; }
  });
  
  // Dùng Ref để đồng hồ khi hết giờ không bị nộp bài trắng
  const answersRef = useRef(answers);
  useEffect(() => { answersRef.current = answers; }, [answers]);

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [gradeResult, setGradeResult] = useState<any>(null);

  const [leftWidth, setLeftWidth] = useState(50); 
  const [isDragging, setIsDragging] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  // --- THUẬT TOÁN ĐỒNG HỒ ĐẾM NGƯỢC ---
  const [timeLeft, setTimeLeft] = useState(5400); 
  const isFinishingRef = useRef(false);

  const getSavedEndTime = (testId: string) => {
    if (!testId) return null;
    const saved = localStorage.getItem(`case_study_endtime_${testId}`);
    return saved ? parseInt(saved, 10) : null;
  };

  // TỰ ĐỘNG LƯU NHÁP TỪNG CHỮ VÀO BỘ NHỚ TRÌNH DUYỆT
  useEffect(() => {
    if (testData?.id && !isFinishingRef.current && !gradeResult) {
      localStorage.setItem(`case_study_ans_${testData.id}`, JSON.stringify(answers));
    }
  }, [answers, testData?.id, gradeResult]);

  // Khởi tạo thời gian thực cho bài thi
  useEffect(() => {
    if (testData) {
       const rawTime = testData.content_json?.basicInfo?.timeLimit || testData.timeLimit;
       const configuredTime = parseInt(rawTime) || 90;
       const initialSeconds = configuredTime * 60;

       let currentEndTime = getSavedEndTime(testData.id);
       if (!currentEndTime) {
           currentEndTime = Date.now() + initialSeconds * 1000;
           localStorage.setItem(`case_study_endtime_${testData.id}`, currentEndTime.toString());
           setTimeLeft(initialSeconds);
       } else {
           const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
           setTimeLeft(remaining);
       }
       setIsLoading(false);
    }
  }, [testData]);

  const formatTime = (totalSeconds: number) => {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    const pad = (num: number) => num.toString().padStart(2, '0');
    if (hours > 0) return `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
    return `${pad(minutes)}:${pad(seconds)}`;
  };

  const handleAnswerChange = (inputId: string, value: string) => {
    setAnswers(prev => ({ ...prev, [inputId]: value }));
  };

  const handleSubmit = async () => {
    const currentAnswers = answersRef.current; // Lấy đáp án mới nhất kể cả khi bị timer ép nộp
    if (Object.keys(currentAnswers).length === 0 && timeLeft > 0) {
      alert("⚠️ Bạn chưa điền câu trả lời nào cả!");
      return;
    }

    if (timeLeft > 0 && !window.confirm("Bạn có chắc chắn muốn nộp bài thi?")) {
      return; 
    }

    setIsSubmitting(true);
    isFinishingRef.current = true;
    
    // BỔ SUNG: Xóa sạch bộ nhớ nháp khi nộp bài
    if (testData?.id) {
       localStorage.removeItem(`case_study_endtime_${testData.id}`);
       localStorage.removeItem(`case_study_ans_${testData.id}`);
    }

    try {
      const prompt = `
        Bạn là một giám khảo chấm thi Cambridge IGCSE vô cùng nghiêm khắc và chính xác.
        Nhiệm vụ của bạn là chấm điểm bài làm của học sinh dựa trên Marking Scheme chính thức.

        THÔNG TIN ĐỀ THI VÀ MARKING SCHEME:
        ${JSON.stringify(testData.json_config?.questions || [])}

        BÀI LÀM CỦA HỌC SINH:
        ${JSON.stringify(currentAnswers)}

        YÊU CẦU:
        - So sánh từng câu trả lời của học sinh với Marking Scheme.
        - Chấm điểm từng phần cực kỳ chặt chẽ (đúng từ khóa/ý mới cho điểm).
        - Đưa ra nhận xét ngắn gọn vì sao được điểm và vì sao mất điểm.
        - TÍNH TỔNG ĐIỂM.

        BẠN BẮT BUỘC PHẢI TRẢ VỀ KẾT QUẢ DƯỚI ĐỊNH DẠNG JSON SAU (không chứa markdown hay text thừa):
        {
          "total_student_score": 0,
          "total_max_score": 0,
          "general_feedback": "Nhận xét tổng quan...",
          "details": [
            {
              "question_number": "1(a)",
              "student_score": 0,
              "max_score": 8,
              "examiner_comment": "Giải thích chi tiết tại sao..."
            }
          ]
        }
      `;

      // GỌI QUA SUPABASE EDGE FUNCTION
      const { data, error } = await supabase.functions.invoke('ai-grader', {
        body: { 
          prompt: prompt,
          // Đề xuất dùng model Pro cho dạng Case Study IGCSE để chấm chuẩn Marking Scheme hơn
          model: 'gemini-2.5-flash' 
        }
      });

      if (error) throw new Error("Lỗi gọi Server: " + error.message);
      if (data?.error) throw new Error("Lỗi chấm điểm AI: " + data.error);

      // Xử lý làm sạch JSON đề phòng AI trả về markdown backticks
      const aiResponseText = data.result.replace(/\u0060{3}(json)?/gi, "").trim();
      const gradedData = JSON.parse(aiResponseText);

      setGradeResult(gradedData);

      // Lưu kết quả vào Database
      try {
        const { data: { user } } = await supabase.auth.getUser();
        if (user) {
          const rawTime = testData.content_json?.basicInfo?.timeLimit || testData.timeLimit;
          const initialSeconds = (parseInt(rawTime) || 90) * 60;
          const timeSpentSecs = initialSeconds - timeLeft;
          
          await supabase.from('test_results').insert([{
            user_id: user.id,
            course_id: testData.course_id,
            test_title: testData.title || "Case Study Test",
            test_type: testData.test_type || 'Case-Study',
            score: gradedData.total_student_score,
            total_score: gradedData.total_max_score,
            time_spent: timeSpentSecs > 0 ? timeSpentSecs : 0,
            details: { test_id: testData.id, userAnswers: currentAnswers, aiFeedback: gradedData }
          }]);
        }
      } catch (dbError) {
        console.error("Lỗi lưu DB:", dbError);
      }

    } catch (err: any) {
      console.error("Lỗi khi chấm bài:", err);
      alert("❌ Đã có lỗi xảy ra: " + err.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  // Đồng hồ chạy liên tục
  useEffect(() => {
    if (isLoading || !testData || gradeResult || isFinishingRef.current) return;
    
    const timer = setInterval(() => {
        const currentEndTime = getSavedEndTime(testData.id);
        if (currentEndTime) {
            const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
            setTimeLeft(remaining);
            if (remaining <= 0) {
                clearInterval(timer);
                alert("⏰ Hết giờ làm bài! Hệ thống tự động nộp bài.");
                handleSubmit();
            }
        } else {
            setTimeLeft(prev => prev - 1);
        }
    }, 1000);
    
    return () => clearInterval(timer);
  }, [isLoading, testData, gradeResult]);

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!isDragging || !containerRef.current) return;
      const containerWidth = containerRef.current.getBoundingClientRect().width;
      const newLeftWidth = (e.clientX / containerWidth) * 100;
      if (newLeftWidth > 20 && newLeftWidth < 80) setLeftWidth(newLeftWidth);
    };
    const handleMouseUp = () => setIsDragging(false);
    if (isDragging) {
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('mouseup', handleMouseUp);
    }
    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, [isDragging]);

  if (isLoading) {
    return (
      <div className="h-screen w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold">
        <div className="animate-spin text-4xl mb-4">⏳</div>
        <p>Đang tải đề thi và tài liệu...</p>
      </div>
    );
  }

  if (!testData || !testData.json_config || !testData.json_config.questions) {
    return (
      <div className="h-screen w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold gap-4">
        <p>⚠️ Chưa có đề thi nào trong hệ thống hoặc dữ liệu bị lỗi.</p>
        <button onClick={onBack} className="bg-[#1e88e5] text-white px-6 py-2 rounded-none">Quay lại</button>
      </div>
    );
  }

  return (
    <div className="h-screen w-screen flex flex-col bg-white font-sans text-slate-900 overflow-hidden">
      
      {/* HEADER TỔNG */}
      <header className="h-14 w-full bg-white border-b border-slate-300 flex items-center justify-between px-4 sm:px-6 shrink-0 z-20 box-border">
        <div className="flex items-center gap-3 sm:gap-4 overflow-hidden">
          <button onClick={onBack} className="text-slate-600 hover:text-black font-bold text-sm transition-colors whitespace-nowrap">← Quay lại</button>
          <div className="h-5 w-px bg-slate-300 hidden sm:block"></div>
          <div className="truncate flex items-baseline gap-2">
            <h1 className="font-bold text-black text-[15px] leading-tight truncate">{testData.title || 'Bài thi Case Study'}</h1>
            <p className="text-[11px] font-semibold text-slate-500 uppercase tracking-wider hidden md:block">Phân loại: {testData.test_type || 'Case-Study'}</p>
          </div>
        </div>
        {!gradeResult && (
          <div className="flex items-center gap-2 sm:gap-4 shrink-0">
             <div className={`font-bold flex items-center gap-2 px-3 py-1 rounded ${timeLeft <= 300 ? 'text-red-600 bg-red-50 animate-pulse' : 'text-slate-600'}`}>
               <span>⏱️</span> <span className="hidden sm:inline font-mono tracking-widest">{formatTime(timeLeft)}</span>
             </div>
             <button 
               onClick={handleSubmit} 
               disabled={isSubmitting}
               className="bg-[#1e88e5] hover:bg-blue-700 text-white font-bold text-sm px-6 py-1.5 rounded-none transition-colors active:scale-95 disabled:opacity-50 whitespace-nowrap"
             >
               {isSubmitting ? 'Đang nộp...' : 'Nộp Bài'}
             </button>
          </div>
        )}
      </header>

      {/* WORKSPACE - SPLIT SCREEN */}
      <div ref={containerRef} className="flex-1 flex overflow-hidden w-full select-none bg-[#525659]">
        
        {/* NỬA TRÁI: PDF */}
        <div style={{ width: `${leftWidth}%` }} className="h-full flex flex-col shrink-0 bg-[#525659]">
          <div className="bg-[#323639] border-b border-[#202224] px-4 flex justify-between items-center h-10 shrink-0 shadow-sm">
            <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest">Tài liệu tham khảo</span>
          </div>
          <div className={`flex-1 w-full h-full ${isDragging ? 'pointer-events-none' : ''}`}>
             {testData.insert_pdf_url ? (
               <iframe src={`${testData.insert_pdf_url}#toolbar=0&navpanes=0&scrollbar=0&view=FitH`} className="w-full h-full border-none bg-transparent" title="PDF Insert" />
             ) : (
               <div className="flex flex-col items-center justify-center h-full text-slate-400 p-8 text-center bg-[#525659]">📄<p className="font-bold">Không có tài liệu PDF đính kèm.</p></div>
             )}
          </div>
        </div>

        {/* THANH KÉO (RESIZER) */}
        <div onMouseDown={() => setIsDragging(true)} className={`w-[6px] h-full bg-[#202224] hover:bg-[#1e88e5] cursor-col-resize flex items-center justify-center shrink-0 z-10 transition-colors ${isDragging ? 'bg-[#1e88e5]' : ''}`}>
          <div className="flex flex-col gap-1">
            <div className="w-[2px] h-[2px] bg-slate-500"></div><div className="w-[2px] h-[2px] bg-slate-500"></div><div className="w-[2px] h-[2px] bg-slate-500"></div>
          </div>
        </div>

        {/* NỬA PHẢI: KHU VỰC LÀM BÀI / KẾT QUẢ CHẤM */}
        <div style={{ width: `calc(${100 - leftWidth}% - 6px)` }} className="h-full flex flex-col shrink-0 bg-[#525659]">
          
          <div className="bg-[#323639] border-b border-[#202224] px-6 flex justify-between items-center h-10 shrink-0 shadow-sm">
            <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest flex items-center gap-2">
              {gradeResult ? (
                <><span>✅</span> Kết quả chấm điểm AI</>
              ) : (
                <><span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> Khu vực làm bài</>
              )}
            </span>
          </div>

          <div className={`flex-1 overflow-y-auto p-4 sm:p-5 ${isDragging ? 'pointer-events-none' : ''}`}>
            
            {/* 1. NẾU ĐÃ CHẤM XONG -> HIỂN THỊ KẾT QUẢ */}
            {gradeResult ? (
              <div className="w-full bg-white shadow-xl mb-5 px-6 py-12 sm:px-16 sm:py-16 min-h-[85vh]">
                <div className="border-b-4 border-black pb-8 mb-10 text-center">
                  <h2 className="text-3xl font-black text-black mb-3">Kết Quả Chấm Điểm (Gemini)</h2>
                  <div className="text-6xl font-black text-[#1e88e5] mb-6">
                    {gradeResult.total_student_score} <span className="text-3xl text-slate-400">/ {gradeResult.total_max_score}</span>
                  </div>
                  <p className="text-[16px] text-slate-700 italic bg-slate-100 p-6 border-l-4 border-[#1e88e5] text-left">
                    <span className="font-bold not-italic block mb-2 text-black uppercase text-sm">Nhận xét tổng quan:</span>
                    {gradeResult.general_feedback}
                  </p>
                </div>

                <div className="space-y-10">
                  {gradeResult.details.map((item: any, idx: number) => (
                    <div key={idx} className="border border-slate-300 p-8 shadow-sm relative">
                      <div className="flex justify-between items-center mb-6 border-b border-slate-200 pb-4">
                        <h4 className="font-black text-xl text-black">Câu {item.question_number}</h4>
                        <span className={`font-black px-4 py-2 text-[15px] ${item.student_score === item.max_score ? 'bg-emerald-100 text-emerald-700 border border-emerald-300' : item.student_score === 0 ? 'bg-red-100 text-red-700 border border-red-300' : 'bg-orange-100 text-orange-700 border border-orange-300'}`}>
                          Đạt: {item.student_score} / {item.max_score}
                        </span>
                      </div>
                      
                      <div className="mb-4">
                         <span className="font-bold text-slate-500 uppercase text-[11px] tracking-widest block mb-2">Bài làm của bạn:</span>
                         <div className="bg-slate-50 p-4 border border-slate-200 text-[14px] text-slate-600 italic">
                            {answers[`${item.question_number}_input_0`] || "Không có câu trả lời..."}
                         </div>
                      </div>

                      <div>
                        <span className="font-bold text-[#0a5482] uppercase text-[11px] tracking-widest block mb-2">Examiner Feedback:</span>
                        <p className="text-[15px] text-black leading-relaxed whitespace-pre-wrap font-medium">
                          {item.examiner_comment}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>
                
                <div className="mt-12 flex justify-center">
                  <button onClick={() => {
                      setGradeResult(null);
                      if (testData?.id) {
                         localStorage.removeItem(`case_study_ans_${testData.id}`);
                         const rawTime = testData.content_json?.basicInfo?.timeLimit || testData.timeLimit;
                         const initialSeconds = (parseInt(rawTime) || 90) * 60;
                         const newEndTime = Date.now() + initialSeconds * 1000;
                         localStorage.setItem(`case_study_endtime_${testData.id}`, newEndTime.toString());
                         setTimeLeft(initialSeconds);
                      }
                      setAnswers({});
                      isFinishingRef.current = false; // Reset lại cờ nộp bài
                  }} className="border-2 border-black hover:bg-slate-100 text-black font-bold px-10 py-3 transition-colors">
                    Làm lại bài thi
                  </button>
                </div>
              </div>
            ) : (
              /* 2. NẾU CHƯA CHẤM -> HIỂN THỊ KHUNG LÀM BÀI */
              <>
                {testData.json_config.questions.map((q: any, index: number) => (
                  <div key={index} className="w-full bg-white shadow-xl mb-5 px-6 py-12 sm:px-16 sm:py-20 min-h-[85vh]">
                    <div className="flex gap-3 mb-8 items-baseline">
                      <div className="font-bold text-black text-[16px] sm:text-[18px] min-w-[30px]">{q.question_number}</div>
                      <div className="flex-1">
                        <h3 className="font-medium text-black text-[15px] sm:text-[16px] leading-relaxed inline">{q.question_text}</h3>
                        <span className="inline-block text-slate-500 text-[12px] font-bold ml-2 uppercase tracking-wider">[{q.total_marks} marks]</span>
                      </div>
                    </div>
                    <div className="space-y-8 pl-0 sm:pl-[42px]">
                      {q.inputs.map((input: any, i: number) => {
                        const inputId = `${q.question_number}_input_${i}`;
                        return (
                          <div key={inputId} className="space-y-2">
                            <label className="block text-[14px] font-semibold text-black">{input.label}</label>
                            <textarea
                              value={answers[inputId] || ''}
                              onChange={(e) => handleAnswerChange(inputId, e.target.value)}
                              className="w-full border border-slate-400 rounded-none p-4 min-h-[120px] text-[15px] text-black leading-relaxed outline-none focus:border-[#1e88e5] focus:ring-1 focus:ring-[#1e88e5] transition-all resize-y bg-transparent"
                            />
                          </div>
                        )
                      })}
                    </div>
                  </div>
                ))}
                
                <div className="w-full bg-white shadow-xl px-8 py-8 sm:px-16 flex justify-end mb-12 border-t border-slate-100">
                   <button 
                     onClick={handleSubmit} 
                     disabled={isSubmitting}
                     className="bg-[#1e88e5] hover:bg-blue-700 text-white font-bold px-10 py-3 rounded-none transition-transform active:scale-95 flex items-center gap-2 shadow-md disabled:opacity-50"
                   >
                     {isSubmitting ? 'AI đang chấm bài...' : 'Hoàn tất & Nộp bài thi'}
                   </button>
                </div>
              </>
            )}

          </div>
        </div>

      </div>
    </div>
  );
}