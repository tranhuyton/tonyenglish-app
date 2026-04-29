import React, { useState, useRef, useEffect } from 'react';
import { supabase } from './supabase'; // Bắt buộc phải import supabase để lấy dữ liệu

export default function SplitScreenTest({ onBack }: { onBack?: () => void }) {
  // --- TRẠNG THÁI LƯU TRỮ DỮ LIỆU THẬT TỪ SUPABASE ---
  const [testData, setTestData] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(true);

  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Trạng thái cho thanh kéo (Resizer)
  const [leftWidth, setLeftWidth] = useState(50); 
  const [isDragging, setIsDragging] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  // --- GỌI API LẤY ĐỀ MỚI NHẤT TỪ SUPABASE KHI MỞ PHÒNG THI ---
  useEffect(() => {
    const fetchLatestTest = async () => {
      setIsLoading(true);
      try {
        // Lấy 1 đề thi mới nhất từ bảng case_study_tests
        const { data, error } = await supabase
          .from('case_study_tests')
          .select('*')
          .order('id', { ascending: false }) // Sắp xếp giảm dần để lấy cái mới nhất
          .limit(1)
          .single();

        if (error) throw error;
        setTestData(data);
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

  const handleSubmit = () => {
    setIsSubmitting(true);
    setTimeout(() => {
      console.log("Dữ liệu nộp cho AI chấm:", answers);
      alert("🎉 Nộp bài thành công! Hệ thống AI đang xử lý chấm điểm...");
      setIsSubmitting(false);
      if(onBack) onBack();
    }, 1500);
  };

  // Logic xử lý kéo thả
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!isDragging || !containerRef.current) return;
      const containerWidth = containerRef.current.getBoundingClientRect().width;
      const newLeftWidth = (e.clientX / containerWidth) * 100;
      if (newLeftWidth > 20 && newLeftWidth < 80) {
        setLeftWidth(newLeftWidth);
      }
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

  // MÀN HÌNH CHỜ (LOADING)
  if (isLoading) {
    return (
      <div className="h-screen w-screen flex flex-col items-center justify-center bg-slate-50 text-slate-500 font-bold">
        <div className="animate-spin text-4xl mb-4">⏳</div>
        <p>Đang tải đề thi từ hệ thống...</p>
      </div>
    );
  }

  // MÀN HÌNH LỖI (NẾU CHƯA CÓ ĐỀ NÀO TRONG KHO)
  if (!testData || !testData.json_config || !testData.json_config.questions) {
    return (
      <div className="h-screen w-screen flex flex-col items-center justify-center bg-slate-50 text-slate-500 font-bold gap-4">
        <p>⚠️ Chưa có đề thi nào trong hệ thống hoặc dữ liệu bị lỗi.</p>
        <button onClick={onBack} className="bg-[#1e88e5] text-white px-6 py-2 rounded-lg">Quay lại</button>
      </div>
    );
  }

  // --- GIAO DIỆN CHÍNH ---
  return (
    <div className="h-screen w-screen flex flex-col bg-slate-50 font-sans text-slate-800 overflow-hidden">
      
      {/* HEADER */}
      <header className="h-16 w-full bg-white border-b border-slate-200 flex items-center justify-between px-4 sm:px-6 shrink-0 z-20 shadow-sm box-border">
        <div className="flex items-center gap-3 sm:gap-4 overflow-hidden">
          <button onClick={onBack} className="text-slate-500 hover:text-[#0a5482] font-bold transition-colors whitespace-nowrap">
            ← Quay lại
          </button>
          <div className="h-6 w-px bg-slate-300 hidden sm:block"></div>
          <div className="truncate">
            <h1 className="font-black text-[#0a5482] text-[15px] sm:text-lg leading-tight truncate">{testData.title}</h1>
            <p className="text-[10px] sm:text-[12px] font-bold text-slate-500 uppercase tracking-wider">Mã đề: {testData.exam_code} / Paper {testData.paper}</p>
          </div>
        </div>
        <div className="flex items-center gap-2 sm:gap-4 shrink-0">
           <div className="bg-orange-100 text-orange-600 px-3 py-1.5 rounded-full font-bold text-[12px] sm:text-[13px] flex items-center gap-2 border border-orange-200">
             <span>⏱️</span> <span className="hidden sm:inline">01:30:00</span>
           </div>
           <button 
             onClick={handleSubmit} 
             disabled={isSubmitting}
             className="bg-[#1e88e5] hover:bg-[#1565c0] text-white font-bold px-4 sm:px-6 py-2 rounded-lg transition-all shadow-md active:scale-95 disabled:opacity-50 whitespace-nowrap"
           >
             {isSubmitting ? 'Đang nộp...' : 'Nộp Bài'}
           </button>
        </div>
      </header>

      {/* WORKSPACE (SPLIT SCREEN) */}
      <div ref={containerRef} className="flex-1 flex overflow-hidden w-full select-none">
        
        {/* NỬA TRÁI: HIỂN THỊ FILE PDF (Tạm thời là Text giữ chỗ) */}
        <div style={{ width: `${leftWidth}%` }} className="h-full bg-slate-200/50 flex flex-col relative shrink-0">
          <div className="absolute top-0 left-0 right-0 bg-white/80 backdrop-blur-sm border-b border-slate-200 px-4 py-2 flex justify-between items-center z-10">
            <span className="font-black text-slate-700 text-xs sm:text-sm uppercase tracking-wider">📄 Tài liệu tham khảo</span>
          </div>
          
          <div className={`flex-1 overflow-y-auto p-4 sm:p-6 pt-14 ${isDragging ? 'pointer-events-none' : ''}`}>
             <div className="bg-white p-6 sm:p-8 rounded-xl shadow-sm border border-slate-200 min-h-[800px]">
               <h2 className="text-2xl font-black text-center mb-6">Tài liệu Case Study</h2>
               <p className="text-slate-600 leading-relaxed mb-4 text-justify">
                 Tính năng hiển thị file PDF Insert chuẩn bị được kích hoạt. Bạn đang làm bài: <strong>{testData.title}</strong>
               </p>
             </div>
          </div>
        </div>

        {/* THANH KÉO (RESIZER) */}
        <div 
          onMouseDown={() => setIsDragging(true)}
          className={`w-2 h-full bg-slate-300 hover:bg-[#1e88e5] cursor-col-resize flex items-center justify-center shrink-0 z-10 transition-colors ${isDragging ? 'bg-[#1e88e5]' : ''}`}
        >
          <div className="flex flex-col gap-1">
            <div className="w-1 h-1 bg-white rounded-full"></div>
            <div className="w-1 h-1 bg-white rounded-full"></div>
            <div className="w-1 h-1 bg-white rounded-full"></div>
          </div>
        </div>

        {/* NỬA PHẢI: KHU VỰC LÀM BÀI GỌI TỪ JSON TRONG SUPABASE */}
        <div style={{ width: `calc(${100 - leftWidth}% - 8px)` }} className="h-full bg-white relative flex flex-col shrink-0">
          <div className="absolute top-0 left-0 right-0 bg-white/90 backdrop-blur-sm border-b border-slate-200 px-6 py-2 z-10 shadow-sm flex justify-between items-center">
            <span className="font-black text-emerald-600 text-xs sm:text-sm uppercase tracking-wider flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> Khu vực làm bài
            </span>
          </div>

          <div className={`flex-1 overflow-y-auto p-4 sm:p-8 pt-16 ${isDragging ? 'pointer-events-none' : ''}`}>
            <div className="max-w-3xl mx-auto space-y-8">
              {/* LẶP QUA CẤU TRÚC JSON ĐỂ VẼ CÂU HỎI */}
              {testData.json_config.questions.map((q: any, index: number) => (
                <div key={index} className="bg-white border-2 border-slate-100 rounded-2xl p-5 sm:p-6 shadow-sm hover:border-blue-100 transition-colors">
                  
                  <div className="flex gap-4 mb-6">
                    <div className="w-10 h-10 shrink-0 bg-[#0a5482] text-white rounded-xl flex items-center justify-center font-black text-lg shadow-inner">
                      {q.question_number.replace(/[^0-9]/g, '')}
                    </div>
                    <div>
                      <h3 className="font-bold text-slate-800 text-[15px] sm:text-[16px] leading-relaxed mb-2">
                        <span className="text-[#1e88e5] mr-1">{q.question_number}</span> {q.question_text}
                      </h3>
                      <span className="inline-block bg-slate-100 text-slate-500 text-[11px] font-black px-2 py-1 rounded uppercase tracking-wider">
                        [{q.total_marks} marks]
                      </span>
                    </div>
                  </div>

                  <div className="space-y-5 pl-2 sm:pl-14">
                    {q.inputs.map((input: any, i: number) => {
                      // Tạo ID độc nhất cho mỗi input để lưu bài
                      const inputId = `${q.question_number}_input_${i}`;
                      return (
                        <div key={inputId} className="space-y-2">
                          <label className="block text-[13px] sm:text-[14px] font-bold text-slate-700">
                            {input.label}
                          </label>
                          <textarea
                            value={answers[inputId] || ''}
                            onChange={(e) => handleAnswerChange(inputId, e.target.value)}
                            placeholder="Nhập câu trả lời..."
                            className="w-full border border-slate-300 rounded-xl p-3 sm:p-4 min-h-[100px] text-[14px] sm:text-[15px] text-slate-800 leading-relaxed outline-none focus:border-[#1e88e5] focus:ring-4 focus:ring-blue-50 transition-all resize-y bg-slate-50 focus:bg-white"
                          />
                        </div>
                      )
                    })}
                  </div>

                </div>
              ))}

              <div className="pt-6 pb-12 flex justify-end">
                 <button 
                   onClick={handleSubmit} 
                   className="bg-emerald-500 hover:bg-emerald-600 text-white font-black px-6 sm:px-8 py-3 rounded-xl shadow-lg shadow-emerald-500/30 transition-transform active:scale-95 flex items-center gap-2"
                 >
                   Hoàn tất & Nộp bài ➜
                 </button>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}