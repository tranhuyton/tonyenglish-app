import React, { useState, useRef, useEffect } from 'react';
import { supabase } from './supabase';

export default function SplitScreenTest({ onBack }: { onBack?: () => void }) {
  const [testData, setTestData] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(true);

  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  
  // STATE MỚI: Lưu trữ kết quả chấm điểm từ Gemini
  const [gradeResult, setGradeResult] = useState<any>(null);

  const [leftWidth, setLeftWidth] = useState(50); 
  const [isDragging, setIsDragging] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const fetchLatestTest = async () => {
      setIsLoading(true);
      try {
        const { data, error } = await supabase
          .from('case_study_tests')
          .select('*')
          .order('id', { ascending: false })
          .limit(1);

        if (error) throw error;
        if (data && data.length > 0) {
          setTestData(data[0]);
        } else {
          setTestData(null);
        }
      } catch (err: any) {
        console.error("Lỗi khi tải đề thi:", err);
        alert("Không thể tải đề thi từ máy chủ!");
      } finally {
        setIsLoading(false);
      }
    };
    fetchLatestTest();
  }, []);

  const handleAnswerChange = (inputId: string, value: string) => {
    setAnswers(prev => ({ ...prev, [inputId]: value }));
  };

  // =========================================================================
  // TRÙM CUỐI: HÀM NỘP BÀI VÀ GỌI GEMINI API CHẤM ĐIỂM
  // =========================================================================
  const handleSubmit = async () => {
    // Kiểm tra xem học sinh đã làm câu nào chưa
    if (Object.keys(answers).length === 0) {
      alert("⚠️ Bạn chưa điền câu trả lời nào cả!");
      return;
    }

    setIsSubmitting(true);

    try {
      // 1. Chuẩn bị dữ liệu Prompt cho Gemini
      const prompt = `
        Bạn là một giám khảo chấm thi Cambridge IGCSE vô cùng nghiêm khắc và chính xác.
        Nhiệm vụ của bạn là chấm điểm bài làm của học sinh dựa trên Marking Scheme chính thức.

        THÔNG TIN ĐỀ THI VÀ MARKING SCHEME:
        ${JSON.stringify(testData.json_config.questions)}

        BÀI LÀM CỦA HỌC SINH:
        ${JSON.stringify(answers)}

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

      // 2. Gọi thẳng API Gemini (Dùng model 1.5 Flash cho tốc độ siêu nhanh)
      const apiKey = import.meta.env.VITE_GEMINI_API_KEY;
      const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{ parts: [{ text: prompt }] }],
          generationConfig: { 
            response_mime_type: "application/json" // Ép Gemini trả về chuẩn JSON
          }
        })
      });

      if (!response.ok) throw new Error("Lỗi kết nối đến máy chủ AI.");

      const resultData = await response.json();
      
      // 3. Bóc tách dữ liệu JSON AI trả về
      const aiResponseText = resultData.candidates[0].content.parts[0].text;
      const gradedData = JSON.parse(aiResponseText);

      // 4. Cập nhật state để hiển thị kết quả
      setGradeResult(gradedData);

    } catch (err: any) {
      console.error("Lỗi khi chấm bài:", err);
      alert("❌ Có lỗi xảy ra trong quá trình AI chấm điểm: " + err.message);
    } finally {
      setIsSubmitting(false);
    }
  };
  // =========================================================================

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
      
      {/* HEADER */}
      <header className="h-14 w-full bg-white border-b border-slate-300 flex items-center justify-between px-4 sm:px-6 shrink-0 z-20 box-border">
        <div className="flex items-center gap-3 sm:gap-4 overflow-hidden">
          <button onClick={onBack} className="text-slate-600 hover:text-black font-bold text-sm transition-colors whitespace-nowrap">← Quay lại</button>
          <div className="h-5 w-px bg-slate-300 hidden sm:block"></div>
          <div className="truncate flex items-baseline gap-2">
            <h1 className="font-bold text-black text-[15px] leading-tight truncate">{testData.title}</h1>
            <p className="text-[11px] font-semibold text-slate-500 uppercase tracking-wider hidden md:block">Mã đề: {testData.exam_code}</p>
          </div>
        </div>
      </header>

      {/* WORKSPACE */}
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

        {/* THANH KÉO */}
        <div onMouseDown={() => setIsDragging(true)} className={`w-[6px] h-full bg-[#202224] hover:bg-[#1e88e5] cursor-col-resize flex items-center justify-center shrink-0 z-10 transition-colors ${isDragging ? 'bg-[#1e88e5]' : ''}`}>
          <div className="flex flex-col gap-1">
            <div className="w-[2px] h-[2px] bg-slate-500"></div><div className="w-[2px] h-[2px] bg-slate-500"></div><div className="w-[2px] h-[2px] bg-slate-500"></div>
          </div>
        </div>

        {/* NỬA PHẢI: KHU VỰC LÀM BÀI / KẾT QUẢ CHẤM */}
        <div style={{ width: `calc(${100 - leftWidth}% - 6px)` }} className="h-full flex flex-col shrink-0 bg-[#525659]">
          
          <div className="bg-[#323639] border-b border-[#202224] px-6 flex justify-between items-center h-10 shrink-0 shadow-sm">
            <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest flex items-center gap-2">
              {gradeResult ? 'Bảng điểm AI (Gemini)' : 'Khu vực làm bài'}
            </span>
          </div>

          <div className={`flex-1 overflow-y-auto p-4 sm:p-5 ${isDragging ? 'pointer-events-none' : ''}`}>
            
            {/* NẾU ĐÃ CHẤM XONG -> HIỂN THỊ KẾT QUẢ */}
            {gradeResult ? (
              <div className="w-full bg-white shadow-xl mb-5 px-6 py-10 sm:px-16 sm:py-12 min-h-[85vh]">
                <div className="border-b-4 border-black pb-6 mb-8 text-center">
                  <h2 className="text-3xl font-black text-black mb-2">Kết Quả Chấm Điểm</h2>
                  <div className="text-5xl font-black text-[#1e88e5] mb-4">
                    {gradeResult.total_student_score} <span className="text-2xl text-slate-400">/ {gradeResult.total_max_score}</span>
                  </div>
                  <p className="text-[15px] text-slate-700 italic bg-slate-100 p-4 border-l-4 border-[#1e88e5]">
                    "{gradeResult.general_feedback}"
                  </p>
                </div>

                <div className="space-y-8">
                  {gradeResult.details.map((item: any, idx: number) => (
                    <div key={idx} className="border border-slate-300 p-6">
                      <div className="flex justify-between items-center mb-4 border-b border-slate-200 pb-2">
                        <h4 className="font-bold text-lg">Câu {item.question_number}</h4>
                        <span className={`font-black px-3 py-1 text-sm ${item.student_score === item.max_score ? 'bg-emerald-100 text-emerald-700' : 'bg-orange-100 text-orange-700'}`}>
                          Điểm: {item.student_score} / {item.max_score}
                        </span>
                      </div>
                      <p className="text-[14px] text-slate-800 leading-relaxed whitespace-pre-wrap">
                        <span className="font-bold text-slate-500 uppercase text-xs">Nhận xét của Examiner:</span><br/>
                        {item.examiner_comment}
                      </p>
                    </div>
                  ))}
                </div>
                
                <div className="mt-10 flex justify-center">
                  <button onClick={() => setGradeResult(null)} className="border-2 border-black hover:bg-slate-100 text-black font-bold px-8 py-2">
                    Làm lại bài thi
                  </button>
                </div>
              </div>
            ) : (
              /* NẾU CHƯA CHẤM -> HIỂN THỊ ĐỀ THI BÌNH THƯỜNG */
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
                              className="w-full border border-slate-400 rounded-none p-4 min-h-[120px] text-[15px] text-black leading-relaxed outline-none focus:border-black focus:ring-1 focus:ring-black transition-all resize-y bg-transparent"
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
                     className="bg-black hover:bg-slate-800 text-white font-bold px-10 py-3 rounded-none transition-transform active:scale-95 flex items-center gap-2 shadow-md disabled:opacity-50"
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