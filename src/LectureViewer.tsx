import React, { useState, useEffect, useCallback, useMemo, useRef } from 'react';
import { supabase } from './supabase';
import 'react-quill/dist/quill.snow.css';

// =========================================================================================
// 🚀 COMPONENT RENDER HTML "CHẾT" (STATIC RENDER) CHỐNG LAG 100%
// =========================================================================================
const StaticLectureContent = React.memo(({ html }: { html: string }) => {
   // Đảm bảo chữ viewBox của SVG viết đúng chuẩn CamelCase để đồ thị co giãn tốt
   const safeHtml = html ? html.replace(/viewbox=/gi, 'viewBox=') : '';
 
   return (
     <div className="animate-in fade-in duration-500 w-full overflow-hidden">
       <style>{`
         .html-content-isolate { 
            font-family: 'Segoe UI', Arial, sans-serif !important; 
            display: block; 
            width: 100%;
         }
         
         /* 1. Ép các thẻ dùng border-box để Padding không làm phình khung ngang */
         .html-content-isolate * { 
            box-sizing: border-box !important; 
            max-width: 100% !important; 
         }
 
         /* 2. CỨU CÁI IFRAME: Trả lại content-box cho thẻ bọc Iframe để không bị vỡ tỷ lệ */
         .html-content-isolate div[style*="padding-bottom"] {
            box-sizing: content-box !important;
         }
         
         /* Giải phóng Iframe khỏi các giới hạn */
         .html-content-isolate iframe {
            max-width: none !important;
            width: 100% !important;
            height: 100% !important;
            display: block;
         }
         
         /* 3. ĐẶC TRỊ ĐỒ THỊ SVG: Ép co giãn theo khung */
         .html-content-isolate svg { 
            width: 100% !important;
            max-width: 100% !important; 
            height: auto !important; 
            display: block; 
         }
 
         .html-content-isolate img { 
            max-width: 100% !important; 
            height: auto !important; 
         }
         
         .html-content-isolate a { cursor: pointer; color: #0284c7; text-decoration: none; font-weight: 600; }
         .html-content-isolate a:hover { text-decoration: underline; }
       `}</style>
       <div className="html-content-isolate" dangerouslySetInnerHTML={{ __html: safeHtml }} />
     </div>
   );
 }, (prevProps, nextProps) => prevProps.html === nextProps.html);


// =========================================================================================
// MAIN COMPONENT: LECTURE VIEWER
// =========================================================================================
export default function LectureViewer({ courseId, onBack }: { courseId: string, onBack: () => void }) {
  const [course, setCourse] = useState<any>(null);
  const [modules, setModules] = useState<any[]>([]);
  const [lectures, setLectures] = useState<any[]>([]);
  const [currentUser, setCurrentUser] = useState<any>(null);
  
  const [pages, setPages] = useState<any[]>([]);
  const [activeLectureId, setActiveLectureId] = useState<string | null>(null);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [completedTasks, setCompletedTasks] = useState<string[]>([]);

  const [expandedModules, setExpandedModules] = useState<string[]>([]);
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [isTaskSidebarOpen, setIsTaskSidebarOpen] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const [dictPopup, setDictPopup] = useState<{show: boolean, word: string, x: number, y: number, rectTop: number, data: any, isLoading: boolean} | null>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (courseId && courseId !== '') fetchCourseData();
    else { setErrorMessage("Không tìm thấy mã Khóa học."); setIsLoading(false); }
  }, [courseId]);

  useEffect(() => {
    const handleFullscreenChange = () => setIsFullscreen(!!document.fullscreenElement);
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', handleFullscreenChange);
  }, []);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
       const popup = document.getElementById('dict-popup');
       if (popup && !popup.contains(e.target as Node)) setDictPopup(null);
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // ---------------------------------------------------------------------------
  // 🚀 EVENT DELEGATION: Tự động mở TẤT CẢ các link ra Tab mới cực sạch sẽ
  // ---------------------------------------------------------------------------
  const handleContainerClick = useCallback((e: React.MouseEvent) => {
      const target = e.target as HTMLElement;
      const link = target.closest('a');
      
      if (link) {
          const href = link.getAttribute('href');
          if (!href) return;

          e.preventDefault(); 
          // Mở link ra Tab mới bằng trình duyệt native (Không iframe, không lag)
          window.open(href, '_blank', 'noopener,noreferrer');
      }
  }, []);

  const fetchCourseData = async () => {
    setIsLoading(true); setErrorMessage(null);
    try {
      const { data: { user } } = await supabase.auth.getUser();
      setCurrentUser(user);
      const { data: courseData, error: courseErr } = await supabase.from('courses').select('*').eq('id', courseId).single();
      if (courseErr || !courseData) throw new Error("Không tìm thấy dữ liệu Khóa học trên hệ thống.");
      setCourse(courseData);
      const { data: modData } = await supabase.from('lecture_modules').select('*').eq('course_id', courseId).order('order_index');
      setModules(modData || []);
      if (modData && modData.length > 0) setExpandedModules([modData[0].id]);
      const { data: lecData } = await supabase.from('lectures').select('*').eq('course_id', courseId).eq('is_published', true).order('order_index');
      setLectures(lecData || []);
      if (lecData && lecData.length > 0) handleSelectLecture(lecData[0].id, user?.id);
    } catch (error: any) { setErrorMessage(error.message); } 
    finally { setIsLoading(false); }
  };

  const handleSelectLecture = async (lectureId: string, userIdOverride?: string) => {
    try {
        setActiveLectureId(lectureId); setCurrentPage(1); setPages([]); setCompletedTasks([]);
        const { data: pageData } = await supabase.from('lecture_pages').select('*').eq('lecture_id', lectureId).order('page_number');
        setPages(pageData || []);
        const targetUserId = userIdOverride || currentUser?.id;
        if (targetUserId) {
           const { data: progressDataArray } = await supabase.from('lecture_progress').select('*').eq('lecture_id', lectureId).eq('user_id', targetUserId);
           if (progressDataArray && progressDataArray.length > 0) {
               const pData = progressDataArray[0];
               if (pData && Array.isArray(pData.completed_tasks)) setCompletedTasks(pData.completed_tasks);
           }
        }
    } catch (err) { console.error(err); }
  };

  const toggleModule = (modId: string) => {
    setExpandedModules(prev => prev.includes(modId) ? prev.filter(id => id !== modId) : [...prev, modId]);
  };

  const activeLecture = lectures.find(l => l.id === activeLectureId);
  const totalPages = useMemo(() => pages.length, [pages]);
  const safeLectureTasks = useMemo(() => Array.isArray(activeLecture?.task_list) ? activeLecture.task_list : [], [activeLecture]);
  const safeCompletedTasks = Array.isArray(completedTasks) ? completedTasks : [];

  const handleToggleTask = useCallback(async (taskId: string) => {
      if (!currentUser || !activeLectureId) return;
      setCompletedTasks(prev => {
         const newCompleted = prev.includes(taskId) ? prev.filter(id => id !== taskId) : [...prev, taskId];
         const isCompleted = safeLectureTasks.length > 0 && newCompleted.length === safeLectureTasks.length;
         supabase.from('lecture_progress').select('id').eq('user_id', currentUser.id).eq('lecture_id', activeLectureId)
         .then(({ data: existingArray }) => {
             if (existingArray && existingArray.length > 0) {
                 supabase.from('lecture_progress').update({ completed_tasks: newCompleted, is_completed: isCompleted }).eq('id', existingArray[0].id).then();
             } else {
                 supabase.from('lecture_progress').insert({ user_id: currentUser.id, lecture_id: activeLectureId, completed_tasks: newCompleted, is_completed: isCompleted }).then();
             }
         }).catch();
         return newCompleted;
      });
  }, [currentUser, activeLectureId, safeLectureTasks]);

  const handleNextPage = () => {
    if (currentPage < totalPages) setCurrentPage(prev => prev + 1);
    else {
      const currentIndex = lectures.findIndex(l => l.id === activeLectureId);
      if (currentIndex !== -1 && currentIndex < lectures.length - 1) {
         const nextLecture = lectures[currentIndex + 1];
         if (nextLecture.module_id && !expandedModules.includes(nextLecture.module_id)) setExpandedModules(prev => [...prev, nextLecture.module_id]);
         handleSelectLecture(nextLecture.id);
      }
    }
  };

  const handlePrevPage = () => {
    if (currentPage > 1) setCurrentPage(prev => prev - 1);
    else {
       const currentIndex = lectures.findIndex(l => l.id === activeLectureId);
       if (currentIndex > 0) {
          const prevLecture = lectures[currentIndex - 1];
          if (prevLecture.module_id && !expandedModules.includes(prevLecture.module_id)) setExpandedModules(prev => [...prev, prevLecture.module_id]);
          handleSelectLecture(prevLecture.id);
       }
    }
  };

  const handleTextSelection = useCallback(() => {
     setTimeout(async () => {
        const selection = window.getSelection();
        if (!selection || selection.rangeCount === 0) return;
        const text = selection.toString().trim();
        if (!text) return;
        
        if (text.length > 0 && text.length < 40 && text.split(' ').length <= 4) {
           const range = selection.getRangeAt(0);
           const rect = range.getBoundingClientRect();
           setDictPopup({ show: true, word: text, x: rect.left + (rect.width/2), y: rect.bottom, rectTop: rect.top, data: null, isLoading: true });

           try {
              let phonetics = '', audio = '', translation = '';
              try {
                 const enRes = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(text)}`);
                 if (enRes.ok) {
                    const enData = await enRes.json();
                    phonetics = enData[0]?.phonetics?.find((p:any) => p.text)?.text || '';
                    audio = enData[0]?.phonetics?.find((p:any) => p.audio)?.audio || '';
                 }
              } catch(err) {}
              try {
                 const viRes = await fetch(`https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=en|vi`);
                 const viData = await viRes.json();
                 translation = viData.responseData.translatedText;
              } catch(err) { translation = "Không thể tải bản dịch lúc này."; }
              setDictPopup(prev => prev ? { ...prev, data: { phonetics, audio, translation }, isLoading: false } : null);
           } catch (error) { setDictPopup(prev => prev ? { ...prev, data: { translation: "Lỗi kết nối." }, isLoading: false } : null); }
        }
     }, 100);
  }, []);

  const playAudio = (url: string) => { if (!url) return; new Audio(url).play(); };
  
  const toggleFullScreen = () => {
    if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(e => console.log(e));
    else if (document.exitFullscreen) document.exitFullscreen();
  };

  const isLastLectureAndPage = currentPage === totalPages && lectures.findIndex(l => l.id === activeLectureId) === lectures.length - 1;
  const currentHtmlContent = useMemo(() => { const page = pages.find(p => p.page_number === currentPage); return page ? page.content_html : ''; }, [pages, currentPage]);


  if (isLoading) return <div className="min-h-screen flex items-center justify-center bg-[#e6e9ee]"><div className="animate-spin text-4xl text-[#3ea6e6]">⏳</div></div>;
  if (errorMessage) return (
      <div className="min-h-screen flex flex-col items-center justify-center bg-[#e6e9ee]"><div className="text-5xl mb-4">⚠️</div><h2 className="text-xl font-black text-slate-800 mb-2">Lỗi tải bài giảng</h2><p className="text-slate-500 mb-6">{errorMessage}</p><button onClick={onBack} className="bg-[#3ea6e6] text-white px-6 py-2.5 rounded-xl font-bold shadow-md hover:bg-[#0284c7]">Quay lại trang chủ</button></div>
  );

  return (
    <div className="flex flex-col h-screen bg-[#e6e9ee] font-sans text-slate-800 overflow-hidden relative">
      
      {/* THANH TOP BAR */}
      <header className="h-[60px] bg-[#3ea6e6] text-white flex items-center px-4 md:px-8 shrink-0 z-30 shadow-sm justify-between">
         <div className="flex items-center gap-2 md:gap-3 min-w-0">
            <button onClick={onBack} className="w-10 h-10 flex items-center justify-center rounded text-white hover:bg-white/20 transition-colors shrink-0" title="Quay lại danh sách">
               <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M9 15L3 9m0 0l6-6M3 9h12a6 6 0 010 12h-3" /></svg>
            </button>
            <div className="w-px h-5 bg-white/30 mx-0.5 hidden sm:block"></div>
            <button onClick={() => setIsSidebarOpen(!isSidebarOpen)} className="w-10 h-10 flex items-center justify-center rounded text-white hover:bg-white/20 transition-colors shrink-0" title="Ẩn/Hiện Sidebar">
               <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h7" /></svg>
            </button>
            <h1 className="text-[20px] md:text-[24px] font-medium leading-none truncate tracking-wide ml-1">{course?.title || 'Đang tải khóa học...'}</h1>
         </div>
         <div className="flex items-center gap-3 shrink-0 ml-4">
             {safeLectureTasks.length > 0 && (
                <button onClick={() => setIsTaskSidebarOpen(!isTaskSidebarOpen)} className="flex items-center gap-2 px-3 py-1.5 md:px-4 md:h-10 rounded text-[14px] font-medium transition-all bg-white/10 hover:bg-white/20 border border-white/20 text-white shadow-sm" title="Danh sách nhiệm vụ">
                   <span>📋</span> <span className="hidden sm:inline">Nhiệm vụ ({safeCompletedTasks.length}/{safeLectureTasks.length})</span>
                </button>
             )}
             <button onClick={toggleFullScreen} className="w-10 h-10 rounded flex items-center justify-center bg-white/10 hover:bg-white/20 border border-white/20 text-white transition-colors shadow-sm" title={isFullscreen ? "Thu nhỏ" : "Toàn màn hình"}>
                {isFullscreen ? <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" /></svg> : <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" /></svg>}
             </button>
          </div>
      </header>

      <div className="flex flex-1 overflow-hidden">
         {/* SIDEBAR TRÁI */}
         <aside className={`${isSidebarOpen ? 'w-[300px]' : 'w-0 opacity-0 border-r-0'} transition-all duration-300 ease-in-out bg-[#f8f9fa] border-r border-slate-200 flex flex-col h-full shrink-0 shadow-[2px_0_10px_rgba(0,0,0,0.02)] relative z-20 overflow-hidden`}>
           <div className="p-5 border-b border-slate-200 shrink-0 min-w-[300px]">
              <div className="text-[14px] text-slate-700 mb-4">Khóa học của bạn</div>
              <h3 className="font-medium text-slate-800 text-[15px] mb-6">{course?.title || '...'}</h3>
           </div>
           
           <div className="flex-1 overflow-y-auto custom-scrollbar bg-[#f8f9fa]">
             {modules.length === 0 ? (
                <div className="p-6 text-center text-slate-400 text-sm italic">Chưa có bài giảng nào được xuất bản.</div>
             ) : (
                modules.map((mod) => {
                  const moduleLectures = lectures.filter(l => l.module_id === mod.id);
                  const isExpanded = expandedModules.includes(mod.id);
                  return (
                    <div key={mod.id} className="border-b border-slate-200 last:border-0">
                      <button onClick={(e) => { e.preventDefault(); e.stopPropagation(); toggleModule(mod.id); }} className="w-full text-left px-5 py-4 transition-colors flex justify-between items-center hover:bg-slate-100">
                        <h4 className="text-[14px] text-slate-700 font-normal pr-4 flex items-center gap-2"><span className={`text-[10px] text-slate-400 transition-transform duration-200 ${isExpanded ? 'rotate-90' : ''}`}>▶</span>{mod.title}</h4>
                      </button>
                      <div className={`overflow-hidden transition-all duration-300 ease-in-out ${isExpanded ? 'max-h-[1000px] opacity-100' : 'max-h-0 opacity-0'}`}>
                        <div className="py-1">
                          {moduleLectures.length === 0 ? (
                             <div className="pl-10 pr-4 py-2 text-sm text-slate-400 italic">Chưa có bài giảng</div>
                          ) : (
                             moduleLectures.map((lec) => {
                               const isActive = activeLectureId === lec.id;
                               return (
                                 <button key={lec.id} onClick={() => handleSelectLecture(lec.id)} className={`w-full text-left pl-10 pr-5 py-2.5 text-[14px] transition-colors flex items-start gap-2 relative ${isActive ? 'bg-[#e0f2fe] text-[#0284c7] font-medium' : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'}`}>
                                   <span className="leading-snug truncate">{lec.title}</span>
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

         {/* VÙNG GIỮA CHỨA NỘI DUNG VÀ SCROLLBAR */}
         <main 
            className="flex-1 overflow-y-auto bg-[#e6e9ee] custom-scrollbar relative"
            ref={containerRef}
            onClick={handleContainerClick} 
            onMouseUp={handleTextSelection}
         >
             <div className="min-h-full flex flex-col items-center py-10 px-4 md:px-8">
               <div className="max-w-[1000px] w-full bg-white shadow-md flex-none rounded-none p-10 md:p-14 mb-8">
                  {!activeLectureId ? (
                    <div className="text-center py-20 text-slate-400 font-medium">Vui lòng chọn bài giảng.</div>
                  ) : !currentHtmlContent ? (
                    <div className="text-center py-20 text-slate-400 font-medium">Nội dung đang được cập nhật...</div>
                  ) : (
                    <div>
                       <h2 className="text-[26px] md:text-[32px] text-slate-800 font-normal mb-12 pb-6 border-b border-slate-100">{activeLecture?.title}</h2>
                       <StaticLectureContent html={currentHtmlContent} />
                    </div>
                  )}
               </div>
               
               {/* THANH PHÂN TRANG */}
               {activeLectureId && (
                  <div className="max-w-[1000px] w-full flex justify-between items-center px-4 pb-10">
                      <button onClick={handlePrevPage} disabled={currentPage === 1 && lectures.findIndex(l => l.id === activeLectureId) === 0} className="text-[#3ea6e6] font-bold text-[14px] hover:text-[#0284c7] disabled:opacity-30 transition-colors uppercase">&lt; TRƯỚC</button>
                      {totalPages > 0 && (
                         <div className="flex gap-4">
                           {Array.from({ length: totalPages }).map((_, i) => (
                                 <button key={i+1} onClick={() => setCurrentPage(i+1)} className={`w-10 h-10 rounded-full flex items-center justify-center text-[15px] font-bold transition-all ${currentPage === i+1 ? 'bg-[#3ea6e6] text-white shadow-md' : 'text-[#3ea6e6] hover:bg-white hover:shadow-sm'}`}>{i+1}</button>
                           ))}
                         </div>
                      )}
                      <button onClick={handleNextPage} disabled={isLastLectureAndPage} className="text-[#3ea6e6] font-bold text-[14px] hover:text-[#0284c7] disabled:opacity-30 transition-colors uppercase">SAU &gt;</button>
                  </div>
               )}
             </div>
         </main>

         {/* SIDEBAR PHẢI: TASK LIST */}
         {safeLectureTasks.length > 0 && (
           <aside className={`${isTaskSidebarOpen ? 'w-[320px]' : 'w-0 opacity-0 border-l-0'} hidden md:flex transition-all duration-300 ease-in-out bg-[#fdfdfd] border-l border-slate-200 flex-col h-full shrink-0 shadow-[-2px_0_10px_rgba(0,0,0,0.02)] relative z-20 overflow-hidden`}>
              <div className="p-6 border-b border-slate-200 bg-white flex flex-col justify-center shrink-0 min-w-[320px]">
                  <div className="flex justify-between items-center mb-3">
                     <h2 className="font-bold text-[#d97706] text-[15px] uppercase tracking-wide">Danh sách nhiệm vụ</h2>
                     <span className="text-[#d97706] text-[14px] font-bold">{safeCompletedTasks.length}/{safeLectureTasks.length}</span>
                  </div>
                  <div className="w-full h-1.5 bg-[#fef3c7] rounded-full overflow-hidden">
                     <div className="h-full bg-[#f59e0b] rounded-full transition-all duration-500" style={{ width: `${safeLectureTasks.length > 0 ? (safeCompletedTasks.length / safeLectureTasks.length) * 100 : 0}%` }}></div>
                  </div>
              </div>

              <div className="flex-1 overflow-y-auto p-5 space-y-3 custom-scrollbar bg-[#f8fafc]">
                  {safeLectureTasks.map((task: any) => {
                      const isCompleted = safeCompletedTasks.includes(task.id);
                      return (
                          <label key={task.id} className={`flex items-start gap-3 p-4 rounded border cursor-pointer transition-all ${isCompleted ? 'bg-[#ecfdf5] border-[#bbf7d0]' : 'bg-white border-slate-200 hover:border-slate-300'}`}>
                              <div className="relative flex items-center justify-center shrink-0 mt-0.5">
                                  <input type="checkbox" className="peer sr-only" checked={isCompleted} onChange={() => handleToggleTask(task.id)} />
                                  <div className={`w-5 h-5 rounded flex items-center justify-center transition-colors border-2 ${isCompleted ? 'bg-[#10b981] border-[#10b981]' : 'bg-white border-slate-300 peer-hover:border-slate-400'}`}>
                                      {isCompleted && <span className="text-white text-xs font-black">✓</span>}
                                  </div>
                              </div>
                              <span className={`text-[14px] leading-relaxed transition-colors ${isCompleted ? 'text-[#047857] font-medium line-through opacity-70' : 'text-slate-700'}`}>{task.text}</span>
                          </label>
                      )
                  })}
              </div>
           </aside>
         )}
      </div>

      {/* TỪ ĐIỂN POPUP VỚI LOGO TONYENGLISH LỆCH TRÁI */}
      {dictPopup && dictPopup.show && (
         <div id="dict-popup" className="fixed z-[100] bg-white rounded-[1.5rem] shadow-[0_20px_60px_rgba(0,0,0,0.25)] border-2 border-slate-100 w-80 flex flex-col animate-in fade-in zoom-in-95 duration-200 overflow-hidden"
           style={{ left: Math.min(dictPopup.x, window.innerWidth - 330), ...(window.innerHeight - dictPopup.y < 300 ? { bottom: window.innerHeight - dictPopup.rectTop + 10 } : { top: dictPopup.y + 10 }), maxHeight: '380px' }}>
            
            <div className="bg-[#f0f9ff] border-b border-[#e0f2fe] py-2.5 px-5 flex items-center justify-start shrink-0">
               <img src="/logo-shield.png" alt="TonyEnglish" className="h-4 w-auto object-contain mr-1.5" />
               <span className="font-black text-[12px] text-[#0a5482] tracking-wider">TONY<span className="text-[#3ea6e6]">ENGLISH</span></span>
            </div>

            <div className="bg-white border-b border-slate-100 p-5 flex justify-between items-start shrink-0">
               <div className="max-w-[200px]"><h4 className="text-[17px] font-bold text-[#e53935] truncate">{dictPopup.word}</h4>{dictPopup.data?.phonetics && (<span className="text-[13px] text-slate-500">{dictPopup.data.phonetics}</span>)}</div>
               {dictPopup.data?.audio && (<button onClick={() => playAudio(dictPopup.data.audio)} className="w-8 h-8 rounded-full bg-blue-50 text-[#0ea5e9] flex items-center justify-center hover:bg-[#0ea5e9] hover:text-white transition-colors shrink-0">🔊</button>)}
            </div>
            
            <div className="p-5 bg-white overflow-y-auto custom-scrollbar">
              {dictPopup.isLoading ? (
                 <div className="flex flex-col items-center justify-center py-6"><div className="animate-spin text-xl text-slate-300 mb-2">⏳</div><span className="text-[12px] font-medium text-slate-500">Đang tra cứu...</span></div>
              ) : (
                 <div><p className="text-[14px] text-slate-800 leading-relaxed">{dictPopup.data?.translation}</p></div>
              )}
            </div>
         </div>
      )}

    </div>
  );
}