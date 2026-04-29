import React, { useState, useRef, useEffect } from 'react';
import { supabase } from './supabase';

export default function SplitScreenTest({ onBack }: { onBack?: () => void }) {
  const [testData, setTestData] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(true);

  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [isSubmitting, setIsSubmitting] = useState(false);

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

  const handleSubmit = () => {
    setIsSubmitting(true);
    setTimeout(() => {
      console.log("Dữ liệu nộp cho AI chấm:", answers);
      alert("🎉 Nộp bài thành công! Hệ thống AI đang xử lý chấm điểm...");
      setIsSubmitting(false);
      if(onBack) onBack();
    }, 1500);
  };

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
      
      {/* HEADER CHÍNH CỦA ỨNG DỤNG (GIỮ NGUYÊN) */}
      <header className="h-14 w-full bg-white border-b border-slate-300 flex items-center justify-between px-4 sm:px-6 shrink-0 z-20 box-border">
        <div className="flex items-center gap-3 sm:gap-4 overflow-hidden">
          <button onClick={onBack} className="text-slate-600 hover:text-black font-bold text-sm transition-colors whitespace-nowrap">
            ← Quay lại
          </button>
          <div className="h-5 w-px bg-slate-300 hidden sm:block"></div>
          <div className="truncate flex items-baseline gap-2">
            <h1 className="font-bold text-black text-[15px] leading-tight truncate">{testData.title}</h1>
            <p className="text-[11px] font-semibold text-slate-500 uppercase tracking-wider hidden md:block">Mã đề: {testData.exam_code} / Paper {testData.paper}</p>
          </div>
        </div>
        <div className="flex items-center gap-2 sm:gap-4 shrink-0">
           <div className="text-slate-600 font-bold text-[13px] flex items-center gap-2">
             <span>⏱️</span> <span className="hidden sm:inline">01:30:00</span>
           </div>
           <button 
             onClick={handleSubmit} 
             disabled={isSubmitting}
             className="bg-[#1e88e5] hover:bg-blue-700 text-white font-bold text-sm px-6 py-1.5 rounded-none transition-colors active:scale-95 disabled:opacity-50 whitespace-nowrap"
           >
             {isSubmitting ? 'Đang nộp...' : 'Nộp Bài'}
           </button>
        </div>
      </header>

      {/* WORKSPACE (SPLIT SCREEN) */}
      <div ref={containerRef} className="flex-1 flex overflow-hidden w-full select-none bg-[#525659]">
        
        {/* ========================================================= */}
        {/* NỬA TRÁI: PDF */}
        {/* ========================================================= */}
        <div style={{ width: `${leftWidth}%` }} className="h-full flex flex-col shrink-0 bg-[#525659]">
          
          {/* THANH TIÊU ĐỀ TRÁI (Màu xám đen đồng bộ trình duyệt PDF) */}
          <div className="bg-[#323639] border-b border-[#202224] px-4 flex justify-between items-center h-10 shrink-0 shadow-sm">
            <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest">Tài liệu tham khảo</span>
          </div>
          
          <div className={`flex-1 w-full h-full ${isDragging ? 'pointer-events-none' : ''}`}>
             {testData.insert_pdf_url ? (
               <iframe 
                 src={`${testData.insert_pdf_url}#toolbar=0&navpanes=0&scrollbar=0&view=FitH`} 
                 className="w-full h-full border-none bg-transparent"
                 title="PDF Insert"
               />
             ) : (
               <div className="flex flex-col items-center justify-center h-full text-slate-400 p-8 text-center bg-[#525659]">
                 <span className="text-4xl mb-4">📄</span>
                 <p className="font-bold">Không có tài liệu PDF đính kèm cho bài thi này.</p>
               </div>
             )}
          </div>
        </div>

        {/* ========================================================= */}
        {/* THANH KÉO (RESIZER) - Màu tối */}
        {/* ========================================================= */}
        <div 
          onMouseDown={() => setIsDragging(true)}
          className={`w-[6px] h-full bg-[#202224] hover:bg-[#1e88e5] cursor-col-resize flex items-center justify-center shrink-0 z-10 transition-colors ${isDragging ? 'bg-[#1e88e5]' : ''}`}
        >
          <div className="flex flex-col gap-1">
            <div className="w-[2px] h-[2px] bg-slate-500"></div>
            <div className="w-[2px] h-[2px] bg-slate-500"></div>
            <div className="w-[2px] h-[2px] bg-slate-500"></div>
          </div>
        </div>

        {/* ========================================================= */}
        {/* NỬA PHẢI: KHU VỰC LÀM BÀI (COPY Y ĐÚC PDF) */}
        {/* ========================================================= */}
        <div style={{ width: `calc(${100 - leftWidth}% - 6px)` }} className="h-full flex flex-col shrink-0 bg-[#525659]">
          
          {/* THANH TIÊU ĐỀ PHẢI (Copy y hệt bên trái) */}
          <div className="bg-[#323639] border-b border-[#202224] px-6 flex justify-between items-center h-10 shrink-0 shadow-sm">
            <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest flex items-center gap-2">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> Khu vực làm bài
            </span>
          </div>

          {/* VÙNG CUỘN CHỨA CÁC "TỜ GIẤY" */}
          <div className={`flex-1 overflow-y-auto p-4 sm:p-6 ${isDragging ? 'pointer-events-none' : ''}`}>
            
            {testData.json_config.questions.map((q: any, index: number) => (
              /* MỖI CÂU HỎI LÀ 1 TỜ GIẤY A4 */
              <div key={index} className="w-full max-w-[850px] mx-auto bg-white shadow-xl mb-6 px-8 py-12 sm:px-14 sm:py-16">
                
                {/* CÂU HỎI */}
                <div className="flex gap-3 mb-8 items-baseline">
                  <div className="font-bold text-black text-[16px] sm:text-[18px] min-w-[30px]">
                    {q.question_number}
                  </div>
                  <div className="flex-1">
                    <h3 className="font-medium text-black text-[15px] sm:text-[16px] leading-relaxed inline">
                      {q.question_text}
                    </h3>
                    <span className="inline-block text-slate-500 text-[12px] font-bold ml-2 uppercase tracking-wider">
                      [{q.total_marks} marks]
                    </span>
                  </div>
                </div>

                {/* CÁC Ô NHẬP LIỆU */}
                <div className="space-y-8 pl-0 sm:pl-[42px]">
                  {q.inputs.map((input: any, i: number) => {
                    const inputId = `${q.question_number}_input_${i}`;
                    return (
                      <div key={inputId} className="space-y-2">
                        <label className="block text-[14px] font-semibold text-black">
                          {input.label}
                        </label>
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

            {/* NÚT NỘP BÀI (Nằm trong 1 mẩu giấy nhỏ ở cuối cùng) */}
            <div className="w-full max-w-[850px] mx-auto bg-white shadow-xl px-8 py-6 sm:px-14 flex justify-end mb-12">
               <button 
                 onClick={handleSubmit} 
                 className="bg-[#1e88e5] hover:bg-blue-700 text-white font-bold px-10 py-3 rounded-none transition-transform active:scale-95 flex items-center gap-2 shadow-md"
               >
                 Hoàn tất & Nộp bài thi
               </button>
            </div>

          </div>
        </div>

      </div>
    </div>
  );
}