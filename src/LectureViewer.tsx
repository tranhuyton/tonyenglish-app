import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';

interface LectureViewerProps {
  courseId: string;
  onBack: () => void;
}

export default function LectureViewer({ courseId, onBack }: LectureViewerProps) {
  // --- STATES DATA ---
  const [course, setCourse] = useState<any>(null);
  const [modules, setModules] = useState<any[]>([]);
  const [lectures, setLectures] = useState<any[]>([]);
  const [pages, setPages] = useState<any[]>([]);
  
  // ĐÃ FIX: Thêm state lỗi để xử lý khi không có dữ liệu
  const [isLoading, setIsLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  // --- STATES UI & NAVIGATION ---
  const [expandedModules, setExpandedModules] = useState<string[]>([]);
  const [activeLectureId, setActiveLectureId] = useState<string | null>(null);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  useEffect(() => {
    // ĐÃ FIX: Chỉ gọi API nếu có courseId hợp lệ. Nếu không thì báo lỗi luôn.
    if (courseId && courseId !== '') {
      fetchCourseData();
    } else {
      setErrorMessage("Không tìm thấy mã Khóa học. Vui lòng quay lại và thử lại.");
      setIsLoading(false);
    }
  }, [courseId]);

  const fetchCourseData = async () => {
    setIsLoading(true);
    setErrorMessage(null);
    try {
      // 1. Lấy thông tin khóa học
      const { data: courseData, error: courseErr } = await supabase.from('courses').select('*').eq('id', courseId).single();
      if (courseErr || !courseData) throw new Error("Không tìm thấy dữ liệu Khóa học trên hệ thống.");
      setCourse(courseData);

      // 2. Lấy danh sách Học phần (Modules)
      const { data: modData } = await supabase.from('lecture_modules').select('*').eq('course_id', courseId).order('order_index');
      setModules(modData || []);
      
      if (modData && modData.length > 0) {
        setExpandedModules([modData[0].id]); // Mở sẵn module đầu tiên
      }

      // 3. Lấy danh sách Bài giảng (Lectures) - Chỉ lấy những bài đã publish
      const { data: lecData } = await supabase.from('lectures').select('*').eq('course_id', courseId).eq('is_published', true).order('order_index');
      setLectures(lecData || []);

      if (lecData && lecData.length > 0) {
        // Tự động chọn bài giảng đầu tiên
        handleSelectLecture(lecData[0].id);
      }
    } catch (error: any) {
      console.error("Lỗi tải bài giảng:", error);
      setErrorMessage(error.message || "Đã xảy ra lỗi khi tải dữ liệu bài giảng.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleSelectLecture = async (lectureId: string) => {
    setActiveLectureId(lectureId);
    setCurrentPage(1);
    setPages([]); // Xóa trang cũ trong lúc chờ tải trang mới
    
    // Tải nội dung trang của bài giảng này
    const { data: pageData } = await supabase.from('lecture_pages').select('*').eq('lecture_id', lectureId).order('page_number');
    setPages(pageData || []);
  };

  const toggleModule = (modId: string) => {
    setExpandedModules(prev => 
      prev.includes(modId) ? prev.filter(id => id !== modId) : [...prev, modId]
    );
  };

  // Tính toán điều hướng
  const activeLecture = lectures.find(l => l.id === activeLectureId);
  const activePageData = pages.find(p => p.page_number === currentPage);
  const totalPages = pages.length;

  const handleNextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(prev => prev + 1);
    } else {
      // Nếu đã ở trang cuối, tìm bài giảng tiếp theo
      const currentIndex = lectures.findIndex(l => l.id === activeLectureId);
      if (currentIndex !== -1 && currentIndex < lectures.length - 1) {
         const nextLecture = lectures[currentIndex + 1];
         // Mở khóa module chứa bài giảng tiếp theo nếu nó đang đóng
         if (nextLecture.module_id && !expandedModules.includes(nextLecture.module_id)) {
            setExpandedModules(prev => [...prev, nextLecture.module_id]);
         }
         handleSelectLecture(nextLecture.id);
      }
    }
  };

  const handlePrevPage = () => {
    if (currentPage > 1) {
      setCurrentPage(prev => prev - 1);
    } else {
       // Trở về bài giảng trước đó
       const currentIndex = lectures.findIndex(l => l.id === activeLectureId);
       if (currentIndex > 0) {
          const prevLecture = lectures[currentIndex - 1];
          if (prevLecture.module_id && !expandedModules.includes(prevLecture.module_id)) {
             setExpandedModules(prev => [...prev, prevLecture.module_id]);
          }
          handleSelectLecture(prevLecture.id);
          // Lưu ý: Không biết trang cuối của bài trước là bao nhiêu nên tạm set về trang 1
       }
    }
  };

  const isLastLectureAndPage = 
     currentPage === totalPages && 
     lectures.findIndex(l => l.id === activeLectureId) === lectures.length - 1;

  // MÀN HÌNH CHỜ & BÁO LỖI NẾU CÓ
  if (isLoading) {
    return <div className="min-h-screen flex items-center justify-center bg-[#f8fafc]"><div className="animate-spin text-4xl text-[#1e88e5]">⏳</div></div>;
  }

  if (errorMessage) {
     return (
        <div className="min-h-screen flex flex-col items-center justify-center bg-[#f8fafc]">
           <div className="text-5xl mb-4">⚠️</div>
           <h2 className="text-xl font-black text-slate-800 mb-2">Không thể tải bài giảng</h2>
           <p className="text-slate-500 mb-6">{errorMessage}</p>
           <button onClick={onBack} className="bg-[#1e88e5] text-white px-6 py-2.5 rounded-xl font-bold shadow-md hover:bg-[#1565c0] transition-colors">Quay lại trang chủ</button>
        </div>
     );
  }

  return (
    <div className="flex h-screen bg-[#f8fafc] font-sans text-slate-800 overflow-hidden">
      
      {/* SIDEBAR TRÁI */}
      <aside className={`${isSidebarOpen ? 'w-[320px]' : 'w-0 opacity-0'} transition-all duration-300 ease-in-out bg-white border-r border-slate-200 flex flex-col h-full shrink-0 shadow-[4px_0_24px_rgba(0,0,0,0.02)] relative z-20`}>
        <div className="p-5 border-b border-slate-200 bg-slate-50 flex items-center gap-3">
           <button onClick={onBack} className="w-8 h-8 flex items-center justify-center rounded-full bg-white border border-slate-200 text-slate-600 hover:bg-slate-100 transition shadow-sm font-bold shrink-0">←</button>
           <h2 className="font-black text-slate-800 text-[15px] uppercase tracking-wide truncate" title={course?.title}>{course?.title || 'Khóa học'}</h2>
        </div>
        
        <div className="flex-1 overflow-y-auto custom-scrollbar bg-slate-50/30">
          {modules.length === 0 ? (
             <div className="p-6 text-center text-slate-400 text-sm border-2 border-dashed border-slate-200 m-4 rounded-xl">Khóa học này chưa được cập nhật cấu trúc bài giảng.</div>
          ) : (
             modules.map((mod, index) => {
               const moduleLectures = lectures.filter(l => l.module_id === mod.id);
               const isExpanded = expandedModules.includes(mod.id);
               
               return (
                 <div key={mod.id} className="border-b border-slate-200 last:border-0 bg-white">
                   <button 
                     onClick={() => toggleModule(mod.id)}
                     className={`w-full text-left p-5 transition-colors flex justify-between items-center hover:bg-slate-50 ${isExpanded ? 'bg-slate-50/50' : ''}`}
                   >
                     <div>
                        <div className="text-[10px] font-black text-[#1e88e5] uppercase tracking-widest mb-1">Học phần {index + 1}</div>
                        <h3 className={`font-bold text-[14px] leading-snug pr-4 ${isExpanded ? 'text-slate-800' : 'text-slate-600'}`}>{mod.title}</h3>
                     </div>
                     <span className={`text-slate-400 text-[10px] transition-transform duration-200 ${isExpanded ? 'rotate-180' : ''}`}>▼</span>
                   </button>
                   
                   {/* Khối bài giảng của học phần */}
                   <div className={`overflow-hidden transition-all duration-300 ease-in-out ${isExpanded ? 'max-h-[1000px] opacity-100' : 'max-h-0 opacity-0'}`}>
                     <div className="py-2 bg-slate-50/80 border-t border-slate-100">
                       {moduleLectures.length === 0 ? (
                          <div className="pl-6 pr-4 py-2 text-xs text-slate-400 italic">Chưa có bài giảng</div>
                       ) : (
                          moduleLectures.map((lec, lIdx) => {
                            const isActive = activeLectureId === lec.id;
                            return (
                              <button
                                key={lec.id}
                                onClick={() => handleSelectLecture(lec.id)}
                                className={`w-full text-left pl-6 pr-4 py-3 text-[13px] transition-colors flex items-start gap-3 relative before:absolute before:left-0 before:top-0 before:bottom-0 before:w-1 before:transition-colors ${isActive ? 'text-[#0a5482] font-black bg-blue-100/50 before:bg-[#1e88e5]' : 'text-slate-600 font-medium hover:text-slate-800 hover:bg-slate-100 before:bg-transparent'}`}
                              >
                                <span className={`w-5 h-5 shrink-0 rounded-full flex items-center justify-center text-[10px] mt-0.5 border ${isActive ? 'bg-[#1e88e5] text-white border-[#1e88e5]' : 'bg-white text-slate-400 border-slate-300'}`}>{lIdx + 1}</span> 
                                <span className="leading-relaxed">{lec.title}</span>
                              </button>
                            )
                          })
                       )}
                     </div>
                   </div>
                 </div>
               )
             })
          )}
        </div>
      </aside>

      {/* VÙNG CHÍNH: NỘI DUNG BÀI GIẢNG */}
      <main className="flex-1 flex flex-col h-full overflow-hidden relative transition-all duration-300">
        
        {/* HEADER BÀI GIẢNG */}
        <header className="h-[65px] bg-white border-b border-slate-200 flex items-center px-6 shrink-0 shadow-sm z-10 justify-between">
          <div className="flex items-center gap-4">
             <button 
                onClick={() => setIsSidebarOpen(!isSidebarOpen)} 
                className="w-10 h-10 flex items-center justify-center rounded-xl bg-slate-100 text-slate-600 hover:bg-[#1e88e5] hover:text-white transition-colors"
                title={isSidebarOpen ? "Thu gọn danh mục" : "Mở danh mục"}
             >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h7" /></svg>
             </button>
             {activeLecture ? (
                <div>
                   <h1 className="text-[16px] font-black text-slate-800 leading-none">{activeLecture.title}</h1>
                   <div className="text-[12px] font-bold text-[#1e88e5] mt-1 tracking-wider uppercase">Bài giảng đang học</div>
                </div>
             ) : (
                <div>
                   <h1 className="text-[16px] font-black text-slate-400 leading-none">Chưa chọn bài</h1>
                </div>
             )}
          </div>
          
          {/* Thanh Tiến Độ Mini */}
          {lectures.length > 0 && activeLectureId && (
             <div className="hidden sm:flex items-center gap-3 bg-slate-50 px-4 py-1.5 rounded-full border border-slate-200">
                <span className="text-[11px] font-bold text-slate-500 uppercase tracking-widest">Tiến độ</span>
                <div className="w-24 h-1.5 bg-slate-200 rounded-full overflow-hidden">
                   <div className="h-full bg-emerald-500 rounded-full transition-all duration-500" style={{ width: `${((lectures.findIndex(l => l.id === activeLectureId) + 1) / lectures.length) * 100}%` }}></div>
                </div>
                <span className="text-[12px] font-black text-emerald-600">{lectures.findIndex(l => l.id === activeLectureId) + 1} / {lectures.length}</span>
             </div>
          )}
        </header>

        {/* NỘI DUNG HTML */}
        <div className="flex-1 overflow-y-auto scroll-smooth flex justify-center bg-[#f4f6f9] relative">
          <div className="max-w-[850px] w-full bg-white shadow-md min-h-full pb-32">
            {/* Thanh màu trang trí mép trên */}
            <div className="h-2 w-full bg-gradient-to-r from-[#1e88e5] to-[#2bd6eb]"></div>
            
            <div className="p-10 sm:p-14">
               {!activeLectureId ? (
                 <div className="text-center py-20 text-slate-400 font-medium border-2 border-dashed border-slate-200 rounded-2xl">
                    <span className="text-4xl block mb-2 opacity-50">👈</span>
                    Vui lòng chọn một bài giảng ở menu bên trái.
                 </div>
               ) : !activePageData ? (
                 <div className="text-center py-20">
                    <span className="text-4xl block mb-4 opacity-50">📖</span>
                    <p className="text-slate-400 font-medium">Nội dung trang này đang được cập nhật...</p>
                 </div>
               ) : (
                 <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
                    <div 
                      className="prose prose-slate max-w-none prose-headings:font-black prose-headings:text-[#0a5482] prose-h1:text-3xl prose-h2:text-2xl prose-p:text-[16px] prose-p:leading-loose prose-p:text-slate-700 prose-a:text-[#1e88e5] prose-a:no-underline hover:prose-a:underline prose-img:rounded-xl prose-img:shadow-md prose-strong:text-slate-800 prose-li:text-[16px]"
                      dangerouslySetInnerHTML={{ __html: activePageData.content_html }} 
                    />
                 </div>
               )}
            </div>
          </div>
        </div>

        {/* FOOTER: THANH ĐIỀU HƯỚNG CỐ ĐỊNH DƯỚI ĐÁY */}
        {activeLectureId && (
           <footer className="absolute bottom-0 left-0 right-0 h-20 bg-white/90 backdrop-blur-md border-t border-slate-200 flex items-center justify-between px-6 sm:px-10 shadow-[0_-4px_20px_rgba(0,0,0,0.03)] z-20">
               <button 
                 onClick={handlePrevPage}
                 disabled={currentPage === 1 && lectures.findIndex(l => l.id === activeLectureId) === 0}
                 className="flex items-center gap-2 text-slate-500 font-bold text-[14px] uppercase tracking-wider hover:text-[#1e88e5] disabled:opacity-30 disabled:hover:text-slate-500 transition-colors py-3"
               >
                 <span className="text-xl">←</span> Bài Trước
               </button>

               {totalPages > 0 && (
                  <div className="flex items-center gap-1.5 bg-slate-100 p-1.5 rounded-xl border border-slate-200">
                    {Array.from({ length: totalPages }).map((_, i) => {
                      const pageNum = i + 1;
                      const isActive = currentPage === pageNum;
                      return (
                        <button
                          key={pageNum}
                          onClick={() => setCurrentPage(pageNum)}
                          className={`w-10 h-10 rounded-lg flex items-center justify-center text-[14px] font-black transition-all ${isActive ? 'bg-white text-[#1e88e5] shadow-sm ring-1 ring-slate-200' : 'text-slate-500 hover:bg-white hover:text-slate-700'}`}
                        >
                          {pageNum}
                        </button>
                      );
                    })}
                  </div>
               )}

               <button 
                 onClick={handleNextPage}
                 disabled={isLastLectureAndPage}
                 className={`flex items-center gap-2 font-bold text-[14px] uppercase tracking-wider transition-colors py-3 px-6 rounded-xl ${currentPage === totalPages ? 'bg-[#1e88e5] text-white shadow-md hover:bg-[#1565c0]' : 'text-[#1e88e5] hover:bg-blue-50'} disabled:opacity-30 disabled:bg-transparent disabled:text-slate-500 disabled:shadow-none`}
               >
                 {currentPage === totalPages ? 'Bài Tiếp Theo' : 'Trang Sau'} <span className="text-xl">→</span>
               </button>
           </footer>
        )}
        
      </main>
    </div>
  );
}