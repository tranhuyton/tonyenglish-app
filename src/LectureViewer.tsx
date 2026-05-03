import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';
// @ts-ignore
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';

const uploadToSupabase = async (file: File) => {
  const fileExt = file.name ? file.name.split('.').pop() : 'png';
  const fileName = `media_${Date.now()}_${Math.random().toString(36).substring(7)}.${fileExt}`;
  const { error } = await supabase.storage.from('test_assets').upload(`uploads/${fileName}`, file, { cacheControl: '3600', upsert: false });
  if (error) throw error;
  return supabase.storage.from('test_assets').getPublicUrl(`uploads/${fileName}`).data.publicUrl;
};

export default function LectureViewer({ courseId, onBack }: { courseId: string, onBack: () => void }) {
  // --- STATES DATA ---
  const [course, setCourse] = useState<any>(null);
  const [modules, setModules] = useState<any[]>([]);
  const [lectures, setLectures] = useState<any[]>([]);
  const [pages, setPages] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  // --- STATES UI & NAVIGATION ---
  const [expandedModules, setExpandedModules] = useState<string[]>([]);
  const [activeLectureId, setActiveLectureId] = useState<string | null>(null);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  // --- STATE TỪ ĐIỂN: THÊM rectTop ĐỂ TÍNH TOÁN LẬT POPUP ---
  const [dictPopup, setDictPopup] = useState<{show: boolean, word: string, x: number, y: number, rectTop: number, data: any, isLoading: boolean} | null>(null);

  useEffect(() => {
    if (courseId && courseId !== '') {
      fetchCourseData();
    } else {
      setErrorMessage("Không tìm thấy mã Khóa học. Vui lòng quay lại và thử lại.");
      setIsLoading(false);
    }
  }, [courseId]);

  // Xóa popup từ điển khi click ra chỗ khác
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
       const popup = document.getElementById('dict-popup');
       if (popup && !popup.contains(e.target as Node)) {
          setDictPopup(null);
       }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const fetchCourseData = async () => {
    setIsLoading(true);
    setErrorMessage(null);
    try {
      const { data: courseData, error: courseErr } = await supabase.from('courses').select('*').eq('id', courseId).single();
      if (courseErr || !courseData) throw new Error("Không tìm thấy dữ liệu Khóa học trên hệ thống.");
      setCourse(courseData);

      const { data: modData } = await supabase.from('lecture_modules').select('*').eq('course_id', courseId).order('order_index');
      setModules(modData || []);
      if (modData && modData.length > 0) setExpandedModules([modData[0].id]);

      const { data: lecData } = await supabase.from('lectures').select('*').eq('course_id', courseId).eq('is_published', true).order('order_index');
      setLectures(lecData || []);

      if (lecData && lecData.length > 0) handleSelectLecture(lecData[0].id);
    } catch (error: any) {
      setErrorMessage(error.message || "Đã xảy ra lỗi khi tải dữ liệu bài giảng.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleSelectLecture = async (lectureId: string) => {
    setActiveLectureId(lectureId);
    setCurrentPage(1);
    setPages([]); 
    
    const { data: pageData } = await supabase.from('lecture_pages').select('*').eq('lecture_id', lectureId).order('page_number');
    setPages(pageData || []);
  };

  const toggleModule = (modId: string) => {
    setExpandedModules(prev => prev.includes(modId) ? prev.filter(id => id !== modId) : [...prev, modId]);
  };

  const activeLecture = lectures.find(l => l.id === activeLectureId);
  const activePageData = pages.find(p => p.page_number === currentPage);
  const totalPages = pages.length;

  const handleNextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(prev => prev + 1);
    } else {
      const currentIndex = lectures.findIndex(l => l.id === activeLectureId);
      if (currentIndex !== -1 && currentIndex < lectures.length - 1) {
         const nextLecture = lectures[currentIndex + 1];
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
       const currentIndex = lectures.findIndex(l => l.id === activeLectureId);
       if (currentIndex > 0) {
          const prevLecture = lectures[currentIndex - 1];
          if (prevLecture.module_id && !expandedModules.includes(prevLecture.module_id)) {
             setExpandedModules(prev => [...prev, prevLecture.module_id]);
          }
          handleSelectLecture(prevLecture.id);
       }
    }
  };

  // ========================================================
  // XỬ LÝ SỰ KIỆN CLICK ĐÚP HOẶC BÔI ĐEN ĐỂ DỊCH TỪ
  // ========================================================
  const handleTextSelection = async (e: React.MouseEvent) => {
     setTimeout(async () => {
        const selection = window.getSelection();
        if (!selection || selection.rangeCount === 0) return;
        
        const text = selection.toString().trim();
        
        if (text && text.length > 0 && text.length < 40 && text.split(' ').length <= 4) {
           const range = selection.getRangeAt(0);
           const rect = range.getBoundingClientRect();

           // Lưu tọa độ Y bên dưới (rect.bottom) và Y bên trên (rect.top) của từ
           setDictPopup({
              show: true,
              word: text,
              x: rect.left,
              y: rect.bottom,
              rectTop: rect.top,
              data: null,
              isLoading: true
           });

           try {
              let phonetics = '';
              let audio = '';
              let translation = '';

              try {
                 const enRes = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(text)}`);
                 if (enRes.ok) {
                    const enData = await enRes.json();
                    const firstEntry = enData[0];
                    phonetics = firstEntry.phonetics?.find((p:any) => p.text)?.text || '';
                    audio = firstEntry.phonetics?.find((p:any) => p.audio)?.audio || '';
                 }
              } catch(err) { /* Bỏ qua nếu không lấy được phiên âm */ }

              try {
                 const viRes = await fetch(`https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=en|vi`);
                 const viData = await viRes.json();
                 translation = viData.responseData.translatedText;
              } catch(err) {
                 translation = "Không thể tải bản dịch lúc này.";
              }

              setDictPopup(prev => prev ? {
                 ...prev, 
                 data: { phonetics, audio, translation },
                 isLoading: false
              } : null);

           } catch (error) {
              setDictPopup(prev => prev ? { ...prev, data: { translation: "Lỗi kết nối từ điển." }, isLoading: false } : null);
           }
        }
     }, 100);
  };

  const playAudio = (url: string) => {
     if (!url) return;
     const audio = new Audio(url);
     audio.play();
  };

  const isLastLectureAndPage = currentPage === totalPages && lectures.findIndex(l => l.id === activeLectureId) === lectures.length - 1;

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
    <div className="flex h-screen bg-[#f8fafc] font-sans text-slate-800 overflow-hidden relative">
      
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
        
        <header className="h-[65px] bg-white border-b border-slate-200 flex items-center px-6 shrink-0 shadow-sm z-10 justify-between">
          <div className="flex items-center gap-4">
             <button 
                onClick={() => setIsSidebarOpen(!isSidebarOpen)} 
                className="w-10 h-10 flex items-center justify-center rounded-xl bg-slate-100 text-slate-600 hover:bg-[#1e88e5] hover:text-white transition-colors"
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

        {/* NỘI DUNG HTML CÓ GẮN SỰ KIỆN CHỌN TỪ */}
        <div className="flex-1 overflow-y-auto scroll-smooth flex justify-center bg-[#f4f6f9] relative">
          <div className="max-w-[850px] w-full bg-white shadow-md min-h-full pb-32">
            <div className="h-2 w-full bg-gradient-to-r from-[#1e88e5] to-[#2bd6eb]"></div>
            
            <div 
               className="p-10 sm:p-14"
               onMouseUp={handleTextSelection} 
            >
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

        {/* POPUP TỪ ĐIỂN - ĐÃ THÊM LOGIC LẬT LÊN/XUỐNG VÀ GIỚI HẠN CHIỀU CAO */}
        {dictPopup && dictPopup.show && (
           <div 
             id="dict-popup"
             className="fixed z-[100] bg-white rounded-2xl shadow-[0_10px_40px_rgba(0,0,0,0.15)] border border-slate-200 w-80 flex flex-col animate-in fade-in zoom-in-95 duration-200 overflow-hidden"
             style={{
               left: Math.min(dictPopup.x, window.innerWidth - 330),
               // Lập trình giới hạn mép: 
               // Nếu mép dưới cùng của màn hình cách từ được bôi < 300px -> lật popup nổi lên trên
               ...(window.innerHeight - dictPopup.y < 300 
                   ? { bottom: window.innerHeight - dictPopup.rectTop + 10 } 
                   : { top: dictPopup.y + 10 }),
               maxHeight: '320px' // Đảm bảo không bao giờ quá dài
             }}
           >
              <div className="bg-slate-50 border-b border-slate-100 p-4 flex justify-between items-start shrink-0">
                 <div className="max-w-[200px]">
                    <h4 className="text-[18px] font-black text-[#e53935] truncate">{dictPopup.word}</h4>
                    {dictPopup.data?.phonetics && (
                       <span className="text-[13px] font-medium text-slate-500">{dictPopup.data.phonetics}</span>
                    )}
                 </div>
                 {dictPopup.data?.audio && (
                    <button onClick={() => playAudio(dictPopup.data.audio)} className="w-8 h-8 rounded-full bg-blue-100 text-[#1e88e5] flex items-center justify-center hover:bg-[#1e88e5] hover:text-white transition-colors shadow-sm active:scale-95 shrink-0">🔊</button>
                 )}
              </div>
              
              {/* Vùng nội dung có scroll riêng */}
              <div className="p-4 bg-white overflow-y-auto custom-scrollbar">
                {dictPopup.isLoading ? (
                   <div className="flex flex-col items-center justify-center py-6">
                      <div className="animate-spin text-2xl text-slate-300 mb-2">⏳</div>
                      <span className="text-[11px] font-bold text-slate-400 uppercase tracking-widest">Đang dịch...</span>
                   </div>
                ) : (
                   <div>
                     <div className="flex items-center gap-2 mb-2">
                        <span className="text-[10px] bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded font-black uppercase tracking-wider">Nghĩa tiếng Việt</span>
                     </div>
                     <p className="text-[14px] text-slate-800 font-medium leading-relaxed">
                        {dictPopup.data?.translation}
                     </p>
                   </div>
                )}
              </div>
           </div>
        )}

        {/* FOOTER ĐIỀU HƯỚNG */}
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