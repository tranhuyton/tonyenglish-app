import React, { useState, useEffect, useCallback, useMemo, useRef } from 'react';
import { supabase } from './supabase';

// =========================================================================================
// 🚀 COMPONENT RENDER BÀI GIẢNG TRONG IFRAME
// =========================================================================================
const StaticLectureContent = React.memo(({ html, onOpenPopup, onOpenDict, onCloseDict }: any) => {
   const iframeRef = useRef<HTMLIFrameElement>(null);
   const [iframeHeight, setIframeHeight] = useState(100);

   useEffect(() => { setIframeHeight(10); }, [html]);

   useEffect(() => {
     const handleMessage = (e: MessageEvent) => {
       if (e.data?.type === 'LECTURE_LINK_CLICK') {
         const href = e.data.href;
         if (href.includes('tonyenglish.vn/uploads') || href.includes('youtube.com') || href.includes('youtu.be')) {
           onOpenPopup(href);
         } else { window.open(href, '_blank', 'noopener,noreferrer'); }
       } else if (e.data?.type === 'LECTURE_RESIZE') {
         const h = e.data.height;
         if (h) setIframeHeight(Math.max(100, h + 20)); 
       } else if (e.data?.type === 'LECTURE_OPEN_DICT') {
         if (iframeRef.current) {
            const rect = iframeRef.current.getBoundingClientRect();
            onOpenDict(e.data.word, rect.left + e.data.x, rect.top + e.data.y, rect.top + e.data.rectTop);
         }
       } else if (e.data?.type === 'LECTURE_CLOSE_DICT') {
         onCloseDict();
       } else if (e.data?.type === 'OPEN_IELTS_AI') {
         // Kích hoạt Radar Bẻ Lái AI
         const fakeBtn = document.createElement('button');
         fakeBtn.className = 'btn-ai-trigger hidden'; 
         if (e.data.topic) fakeBtn.setAttribute('data-topic', e.data.topic);
         if (e.data.image) fakeBtn.setAttribute('data-image', e.data.image);
         if (e.data.task) fakeBtn.setAttribute('data-task', e.data.task);
         document.body.appendChild(fakeBtn);
         fakeBtn.click(); 
         setTimeout(() => { fakeBtn.remove(); }, 100); 
       } 
       // 🚀 ĐÓN TÍN HIỆU MỞ PHÒNG LIVE TỪ IFRAME
       else if (e.data?.type === 'OPEN_LIVE_SPEAKING') {
         const fakeLiveBtn = document.createElement('button');
         fakeLiveBtn.className = 'btn-live-trigger hidden';
         if (e.data.topic) fakeLiveBtn.setAttribute('data-topic', e.data.topic);
         document.body.appendChild(fakeLiveBtn);
         fakeLiveBtn.click(); // Đánh lừa App.tsx để nó mở phòng
         setTimeout(() => { fakeLiveBtn.remove(); }, 100);
       }
     };
     window.addEventListener('message', handleMessage);
     return () => window.removeEventListener('message', handleMessage);
   }, [onOpenPopup, onOpenDict, onCloseDict]);

   const iframeContent = `
     <!DOCTYPE html>
     <html lang="vi">
     <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
       <style>
         html, body { 
             height: max-content !important; min-height: 0 !important;
             margin: 0; padding: 0; 
             font-family: 'Segoe UI', Arial, sans-serif; color: #334155; 
             background: transparent; overflow: hidden; line-height: 1.8;
             -webkit-font-smoothing: antialiased;
         }
         * { box-sizing: border-box; }
         img, video, iframe { max-width: 100%; height: auto; display: block; border-radius: 8px; margin: 10px 0; }
         svg { max-width: 100%; height: auto; pointer-events: all !important; }
         a { cursor: pointer; color: #0ea5e9; text-decoration: none; font-weight: 600; transition: opacity 0.2s; }
         a:hover { opacity: 0.8; text-decoration: underline; }
         ::selection { background: #bae6fd; color: #0369a1; }
         #content-wrapper { display: flow-root; width: 100%; padding-bottom: 20px; font-size: 16px; }
         p { margin-top: 0; margin-bottom: 1rem; }
         table { border-collapse: collapse; width: 100%; margin-bottom: 1rem; }
         table th, table td { border: 1px solid #cbd5e1; padding: 0.75rem; vertical-align: top; }
         table th { background-color: #f1f5f9; font-weight: 700; text-align: left; }
       </style>
     </head>
     <body>
       <div id="content-wrapper">${html ? html.replace(/viewbox=/gi, 'viewBox=') : ''}</div>
       <script>
         document.addEventListener('click', function(e) {
           var target = e.target;
           
           var anchor = target.closest('a');
           if (anchor && anchor.href && !anchor.outerHTML.includes('openIELTSAssessor') && !anchor.classList.contains('btn-ielts-trigger') && !anchor.classList.contains('btn-ai-trigger') && !anchor.classList.contains('btn-live-trigger')) {
               e.preventDefault(); 
               window.parent.postMessage({ type: 'LECTURE_LINK_CLICK', href: anchor.href }, '*'); 
               return; 
           }

           // 1. TÌM NÚT BẺ LÁI AI (CŨ)
           var aiBtn = target.closest('.btn-ai-trigger, .btn-ielts-trigger');
           if (aiBtn) {
               e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
               var topic = aiBtn.getAttribute('data-topic') || '';
               var image = aiBtn.getAttribute('data-image') || '';
               var task = aiBtn.getAttribute('data-task') || 'task2';
               
               var originalText = aiBtn.innerHTML;
               aiBtn.innerHTML = "✨ Đang mở Giám Khảo...";
               aiBtn.style.opacity = "0.7";
               setTimeout(function() { aiBtn.innerHTML = originalText; aiBtn.style.opacity = "1"; }, 1500);

               window.parent.postMessage({ type: 'OPEN_IELTS_AI', topic: topic, image: image, task: task }, '*');
               return false;
           }

           // 2. 🚀 TÌM NÚT GỌI LIVE SPEAKING (MỚI)
           var liveBtn = target.closest('.btn-live-trigger');
           if (liveBtn) {
               e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
               var topic = liveBtn.getAttribute('data-topic') || '';
               
               var originalText = liveBtn.innerHTML;
               liveBtn.innerHTML = "📞 Đang kết nối...";
               liveBtn.style.opacity = "0.7";
               setTimeout(function() { liveBtn.innerHTML = originalText; liveBtn.style.opacity = "1"; }, 1500);

               // Bắn tín hiệu ra ngoài
               window.parent.postMessage({ type: 'OPEN_LIVE_SPEAKING', topic: topic }, '*');
               return false;
           }

         }, true);
         
         var selectionTimer = null;
         document.addEventListener('mouseup', function(e) {
           clearTimeout(selectionTimer);
           selectionTimer = setTimeout(function() {
               var sel = window.getSelection();
               var text = sel.toString().trim();
               if (text && text.length > 0 && text.length < 40 && text.split(' ').length <= 4) {
                 var range = sel.getRangeAt(0);
                 var rect = range.getBoundingClientRect();
                 window.parent.postMessage({ type: 'LECTURE_OPEN_DICT', word: text, x: rect.left + (rect.width/2), y: rect.bottom, rectTop: rect.top }, '*');
               }
           }, 150);
         });

         document.addEventListener('mousedown', function(e) {
           var sel = window.getSelection();
           if (!sel.toString().trim()) { window.parent.postMessage({ type: 'LECTURE_CLOSE_DICT' }, '*'); }
         });

         function reportHeight() {
            var wrapper = document.getElementById('content-wrapper');
            if (wrapper) {
                var h = wrapper.getBoundingClientRect().height;
                if (h > 0) window.parent.postMessage({ type: 'LECTURE_RESIZE', height: h }, '*');
            }
         }
         window.addEventListener('load', reportHeight);
         if (window.ResizeObserver) {
            var ro = new ResizeObserver(reportHeight);
            ro.observe(document.body);
            ro.observe(document.getElementById('content-wrapper'));
         } else { setInterval(reportHeight, 500); }
       </script>
     </body>
     </html>
   `;

   return (
     <div className="w-full animate-in fade-in duration-500 relative">
       <iframe
         ref={iframeRef}
         srcDoc={iframeContent}
         style={{ width: '100%', height: `${iframeHeight}px`, border: 'none', overflow: 'hidden' }}
         sandbox="allow-scripts allow-same-origin allow-popups"
         scrolling="no"
       />
     </div>
   );
 }, (prevProps, nextProps) => prevProps.html === nextProps.html);


// =========================================================================================
// MAIN COMPONENT: LECTURE VIEWER
// =========================================================================================
export default function LectureViewer({ courseId, onBack, onStartTest, onOpenAI }: { courseId: string, onBack: () => void, onStartTest?: (type: string, data: any) => void, onOpenAI?: (passedMode?: string, topic?: string, image?: string, task?: string) => void }) {
  const [course, setCourse] = useState<any>(null);
  const [modules, setModules] = useState<any[]>([]);
  const [lectures, setLectures] = useState<any[]>([]);
  const [currentUser, setCurrentUser] = useState<any>(null);
  
  const [pages, setPages] = useState<any[]>([]);
  const [activeLectureId, setActiveLectureId] = useState<string | null>(null);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [completedTasks, setCompletedTasks] = useState<string[]>([]);
  const [allLectureProgress, setAllLectureProgress] = useState<Record<string, string[]>>({});

  const [expandedModules, setExpandedModules] = useState<string[]>([]);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false); 
  const [isTaskMenuOpen, setIsTaskMenuOpen] = useState(false);
  const taskMenuRef = useRef<HTMLDivElement>(null);
  
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const [popupUrl, setPopupUrl] = useState<string | null>(null);
  const [dictPopup, setDictPopup] = useState<{show: boolean, word: string, x: number, y: number, rectTop: number, data: any, isLoading: boolean} | null>(null);
  
  const containerRef = useRef<HTMLDivElement>(null);

  const activeLecture = useMemo(() => lectures.find(l => l.id === activeLectureId), [lectures, activeLectureId]);
  const totalPages = pages.length;
  const currentHtmlContent = useMemo(() => { const page = pages.find(p => p.page_number === currentPage); return page ? page.content_html : ''; }, [pages, currentPage]);

  useEffect(() => {
    if (activeLecture && currentHtmlContent) {
      window.dispatchEvent(new CustomEvent('tony-update-lecture-context', {
        detail: {
          title: activeLecture.title, 
          html: currentHtmlContent 
        }
      }));
    }
  }, [activeLecture, currentHtmlContent]);

  useEffect(() => {
    if (containerRef.current) containerRef.current.scrollTo({ top: 0, behavior: 'smooth' });
  }, [activeLectureId, currentPage]);

  useEffect(() => {
    if (courseId && courseId !== '') fetchCourseData();
    else { setErrorMessage("Không tìm thấy mã Khóa học."); setIsLoading(false); }
  }, [courseId]);

  useEffect(() => {
    const handleFullscreenChange = () => setIsFullscreen(!!document.fullscreenElement);
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    if (window.innerWidth >= 768) setIsSidebarOpen(true);
    return () => document.removeEventListener('fullscreenchange', handleFullscreenChange);
  }, []);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
       const dictPop = document.getElementById('dict-popup');
       if (dictPop && !dictPop.contains(e.target as Node)) setDictPopup(null);
       if (taskMenuRef.current && !taskMenuRef.current.contains(e.target as Node)) setIsTaskMenuOpen(false);
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
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
      const safeModData = modData || [];
      setModules(safeModData);

      const { data: lecData } = await supabase.from('lectures').select('*').eq('course_id', courseId).eq('is_published', true);
      
      let validLectures = (lecData || []).filter(lec => lec.module_id && safeModData.some(mod => mod.id === lec.module_id));
      validLectures.sort((a, b) => {
          const modA = safeModData.find(m => m.id === a.module_id);
          const modB = safeModData.find(m => m.id === b.module_id);
          const modOrderDiff = (modA?.order_index || 0) - (modB?.order_index || 0);
          if (modOrderDiff !== 0) return modOrderDiff;
          return (a.order_index || 0) - (b.order_index || 0);
      });
      
      setLectures(validLectures);

      if (user && validLectures.length > 0) {
         const lectureIds = validLectures.map(l => l.id);
         const { data: allProg } = await supabase.from('lecture_progress').select('lecture_id, completed_tasks').eq('user_id', user.id).in('lecture_id', lectureIds);
         const pMap: Record<string, string[]> = {};
         if (allProg) { allProg.forEach(p => { pMap[p.lecture_id] = p.completed_tasks || []; }); }
         setAllLectureProgress(pMap);
      }

      if (validLectures && validLectures.length > 0) {
         const savedLectureId = localStorage.getItem(`tony_last_lec_${user?.id}_${courseId}`);
         const targetLecture = validLectures.find(l => l.id === savedLectureId) || validLectures[0];
         if (targetLecture.module_id) setExpandedModules([targetLecture.module_id]);
         handleSelectLecture(targetLecture.id, user?.id);
      } else {
         if (safeModData.length > 0) setExpandedModules([safeModData[0].id]);
      }
    } catch (error: any) { setErrorMessage(error.message); } finally { setIsLoading(false); }
  };

  const handleSelectLecture = async (lectureId: string, userIdOverride?: string) => {
    try {
        setActiveLectureId(lectureId); setCurrentPage(1); setPages([]); setCompletedTasks([]);
        if (window.innerWidth < 768) setIsSidebarOpen(false);
        const targetUserId = userIdOverride || currentUser?.id;
        if (targetUserId) localStorage.setItem(`tony_last_lec_${targetUserId}_${courseId}`, lectureId);

        const { data: pageData } = await supabase.from('lecture_pages').select('*').eq('lecture_id', lectureId).order('page_number');
        setPages(pageData || []);
        
        if (targetUserId) {
           const { data: progressDataArray } = await supabase.from('lecture_progress').select('*').eq('lecture_id', lectureId).eq('user_id', targetUserId);
           if (progressDataArray && progressDataArray.length > 0) {
               const pData = progressDataArray[0];
               if (pData && Array.isArray(pData.completed_tasks)) {
                   setCompletedTasks(pData.completed_tasks);
                   setAllLectureProgress(prev => ({...prev, [lectureId]: pData.completed_tasks}));
               }
           } else { setCompletedTasks([]); }
        }
    } catch (err) {}
  };

  const toggleModule = (modId: string) => {
    setExpandedModules(prev => prev.includes(modId) ? prev.filter(id => id !== modId) : [...prev, modId]);
  };

  const handleToggleTask = useCallback(async (taskId: string) => {
      if (!currentUser || !activeLectureId) return;
      const safeLectureTasks = Array.isArray(activeLecture?.task_list) ? activeLecture.task_list : [];
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

         setAllLectureProgress(allPrev => ({ ...allPrev, [activeLectureId]: newCompleted }));
         return newCompleted;
      });
  }, [currentUser, activeLectureId, lectures, activeLecture]);

  const handleStartTaskExercise = async (task: any) => {
      if (!onStartTest || !task.test_id) return;
      try {
         const { data: testData, error } = await supabase.from('tests').select('*').eq('id', task.test_id).single();
         if (error || !testData) { alert("Bài tập này hiện không khả dụng. Vui lòng liên hệ Admin."); return; }
         if (!completedTasks.includes(task.id)) handleToggleTask(task.id);
         const type = String(testData.test_type || '').toLowerCase();
         if (type.includes('standard')) onStartTest('standard', testData);
         else if (type.includes('case-study') || type.includes('business')) onStartTest('case-study', testData);
         else if (type === 'ielts-writing') onStartTest('ielts-writing', testData);
         else if (type === 'ielts-speaking') onStartTest('ielts-speaking', testData);
         else if (type.includes('ielts')) onStartTest('computer', testData); 
         else onStartTest('standard', testData);
      } catch (err) {}
  };

  const handleNextPage = () => {
    if (currentPage < pages.length) setCurrentPage(prev => prev + 1);
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

  const triggerDictionary = useCallback((word: string, x: number, y: number, rectTop: number) => {
    setDictPopup({ show: true, word, x, y, rectTop, data: null, isLoading: true });
    
    Promise.allSettled([
        fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(word)}`).then(r => r.ok ? r.json() : Promise.reject()),
        fetch(`https://api.mymemory.translated.net/get?q=${encodeURIComponent(word)}&langpair=en|vi`).then(r => r.json())
    ]).then(([enRes, viRes]) => {
        let phonetics = '', audio = '', translation = 'Không tìm thấy bản dịch.';
        if (enRes.status === 'fulfilled' && enRes.value[0]) {
            phonetics = enRes.value[0].phonetics?.find((p:any) => p.text)?.text || '';
            audio = enRes.value[0].phonetics?.find((p:any) => p.audio)?.audio || '';
        }
        if (viRes.status === 'fulfilled' && viRes.value?.responseData?.translatedText) {
            translation = viRes.value.responseData.translatedText;
        }
        setDictPopup(prev => prev ? { ...prev, data: { phonetics, audio, translation }, isLoading: false } : null);
    });
  }, []);

  const handleTextSelection = useCallback(() => {
     setTimeout(() => {
        const selection = window.getSelection();
        if (!selection || selection.rangeCount === 0) return;
        const text = selection.toString().trim();
        if (!text) return;
        if (text.length > 0 && text.length < 40 && text.split(' ').length <= 4) {
           const range = selection.getRangeAt(0);
           const rect = range.getBoundingClientRect();
           triggerDictionary(text, rect.left + (rect.width/2), rect.bottom, rect.top);
        }
     }, 100);
  }, [triggerDictionary]);

  const playAudio = (url: string) => { if (!url) return; new Audio(url).play(); };
  
  const toggleFullScreen = () => {
    if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(e => console.log(e));
    else if (document.exitFullscreen) document.exitFullscreen();
  };

  const getEmbedUrl = (url: string) => {
    if (url.includes('youtube.com/playlist?list=')) return url.replace('playlist?list=', 'embed/videoseries?list=');
    if (url.includes('youtube.com/watch?v=')) return url.replace('watch?v=', 'embed/');
    if (url.includes('youtu.be/')) return url.replace('youtu.be/', 'youtube.com/embed/');
    return url;
  };

  const safeLectureTasks = Array.isArray(activeLecture?.task_list) ? activeLecture.task_list : [];
  const safeCompletedTasks = Array.isArray(completedTasks) ? completedTasks : [];
  const isLastLectureAndPage = currentPage === totalPages && lectures.findIndex(l => l.id === activeLectureId) === lectures.length - 1;

  if (isLoading) return <div className="min-h-[100dvh] flex items-center justify-center bg-[#f1f5f9]"><div className="animate-spin text-4xl text-[#0ea5e9]">⏳</div></div>;
  if (errorMessage) return (
      <div className="min-h-[100dvh] flex flex-col items-center justify-center bg-[#f1f5f9]"><div className="text-5xl mb-4">⚠️</div><h2 className="text-xl font-black text-slate-800 mb-2">Lỗi tải bài giảng</h2><p className="text-slate-500 mb-6">{errorMessage}</p><button onClick={onBack} className="bg-[#0ea5e9] text-white px-6 py-2.5 rounded-xl font-bold shadow-md hover:bg-[#0284c7]">Quay lại trang chủ</button></div>
  );

  return (
    <div className="flex flex-col h-[100dvh] w-full bg-[#f1f5f9] font-sans text-slate-800 overflow-hidden relative overscroll-none">
      
      <header className="h-[65px] bg-[#0ea5e9] text-white flex items-center px-4 md:px-6 shrink-0 z-30 shadow-md justify-between">
         <div className="flex items-center gap-2 md:gap-3 min-w-0 flex-1">
            <button onClick={onBack} className="w-10 h-10 flex items-center justify-center rounded-lg text-white hover:bg-white/20 transition-colors shrink-0" title="Quay lại danh sách">
               <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M9 15L3 9m0 0l6-6M3 9h12a6 6 0 010 12h-3" /></svg>
            </button>
            <div className="w-px h-6 bg-white/30 mx-1 hidden sm:block"></div>
            <button onClick={() => setIsSidebarOpen(!isSidebarOpen)} className="w-10 h-10 flex items-center justify-center rounded-lg text-white hover:bg-white/20 transition-colors shrink-0" title="Ẩn/Hiện Sidebar">
               <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h7" /></svg>
            </button>
            <h1 className="text-[17px] md:text-[20px] leading-none truncate tracking-wide ml-1">{course?.title || 'Đang tải khóa học...'}</h1>
            
            {safeLectureTasks.length > 0 && (
               <div className="relative ml-2 shrink-0" ref={taskMenuRef}>
                 <button 
                   onClick={() => setIsTaskMenuOpen(!isTaskMenuOpen)} 
                   className={`flex items-center gap-2 px-3 py-2 rounded-lg text-[13px] font-bold transition-all border ${safeCompletedTasks.length === safeLectureTasks.length ? 'bg-emerald-500/30 text-emerald-50 border-emerald-400/50' : 'bg-white/10 hover:bg-white/20 text-white border-white/20 shadow-sm'}`}
                 >
                   <span>📋</span> 
                   <span className="hidden sm:inline">Nhiệm vụ</span>
                   <span>({safeCompletedTasks.length}/{safeLectureTasks.length})</span>
                   <span className={`text-[10px] ml-1 transition-transform duration-200 hidden sm:inline ${isTaskMenuOpen ? 'rotate-180' : ''}`}>▼</span>
                 </button>

                 {isTaskMenuOpen && (
                    <div className="fixed top-[75px] left-1/2 -translate-x-1/2 w-[92vw] max-w-[380px] md:absolute md:top-full md:left-auto md:right-0 md:translate-x-0 md:mt-3 bg-white rounded-2xl shadow-[0_20px_60px_rgba(0,0,0,0.15)] border border-slate-200 overflow-hidden z-[100] animate-in zoom-in-95 duration-200">
                       <div className="bg-slate-50 px-5 py-4 border-b border-slate-100 flex justify-between items-center">
                          <h4 className="font-black text-slate-700 text-[13px] uppercase tracking-widest">Nhiệm vụ bài học</h4>
                          <span className="text-[#0ea5e9] font-bold text-[14px] bg-blue-50 px-2 py-0.5 rounded-md">{Math.round((safeCompletedTasks.length / safeLectureTasks.length) * 100)}%</span>
                       </div>
                       
                       <div className="max-h-[60vh] overflow-y-auto p-3 custom-scrollbar space-y-2">
                          {safeLectureTasks.map((task: any) => {
                             const isCompleted = safeCompletedTasks.includes(task.id);
                             return (
                                <div key={task.id} className={`flex items-start gap-3 p-3.5 rounded-xl transition-all border ${isCompleted ? 'bg-emerald-50/50 border-emerald-100' : 'bg-white border-slate-100 hover:border-[#0ea5e9]/50 shadow-sm'}`}>
                                   <div className="relative flex items-center justify-center shrink-0 mt-0.5 cursor-pointer" onClick={() => handleToggleTask(task.id)}>
                                       <div className={`w-5 h-5 rounded flex items-center justify-center transition-colors border-2 ${isCompleted ? 'bg-[#10b981] border-[#10b981]' : 'bg-white border-slate-300 hover:border-[#0ea5e9]'}`}>
                                           {isCompleted && <span className="text-white text-xs font-black">✓</span>}
                                       </div>
                                   </div>
                                   <div className="flex-1 min-w-0 flex flex-col items-start gap-2">
                                      <span className={`text-[14px] font-medium leading-snug transition-colors ${isCompleted ? 'text-emerald-700 opacity-70 line-through' : 'text-slate-700'}`}>{task.text}</span>
                                      {task.type === 'exercise' && (
                                         <button 
                                           onClick={() => handleStartTaskExercise(task)} 
                                           className={`text-[12px] font-bold px-4 py-2 rounded-lg shadow-sm transition-all ${isCompleted ? 'bg-slate-100 text-slate-500 hover:bg-slate-200' : 'bg-slate-800 text-white hover:bg-black active:scale-95'}`}
                                         >
                                           {isCompleted ? 'Làm lại bài' : 'Làm bài ngay ➜'}
                                         </button>
                                      )}
                                   </div>
                                </div>
                             )
                          })}
                       </div>
                    </div>
                 )}
               </div>
            )}
         </div>

         <div className="flex items-center gap-2 sm:gap-3 shrink-0 ml-2 sm:ml-4">
             {!(course?.title || '').toLowerCase().includes('ielts') && (
                 <button 
                    onClick={() => { if(onOpenAI) onOpenAI('tutor'); }} 
                    className="flex items-center gap-2 px-3 py-2 md:px-4 md:h-10 rounded-lg text-[13px] md:text-[14px] font-bold transition-all bg-amber-400 hover:bg-amber-500 text-amber-950 shadow-md border border-amber-300" 
                    title="Hỏi AI"
                 >
                    <span className="animate-pulse">✨</span> <span className="hidden sm:inline">Hỏi AI</span>
                 </button>
             )}

             <button onClick={toggleFullScreen} className="hidden md:flex w-10 h-10 rounded-lg items-center justify-center bg-white/10 hover:bg-white/20 border border-white/20 text-white transition-colors shadow-sm" title={isFullscreen ? "Thu nhỏ" : "Toàn màn hình"}>
                {isFullscreen ? <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" /></svg> : <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" /></svg>}
             </button>
          </div>
      </header>

      <div className="flex flex-1 overflow-hidden relative w-full">
         
         {isSidebarOpen && (
            <div className="fixed inset-0 bg-slate-900/40 z-40 md:hidden transition-opacity" onClick={() => setIsSidebarOpen(false)} />
         )}

         {/* CỘT MỤC LỤC TRÁI */}
         <aside className={`fixed md:relative inset-y-0 left-0 z-50 md:z-20 h-[100dvh] md:h-full bg-white border-r border-slate-200 flex flex-col shrink-0 transition-transform duration-300 ease-in-out shadow-2xl md:shadow-none
            ${isSidebarOpen ? 'translate-x-0 w-[280px] md:w-[320px]' : '-translate-x-full w-[280px] md:w-0 md:opacity-0 md:border-r-0 md:translate-x-0'}`}>
           
           <div className="p-6 border-b border-slate-200 shrink-0 bg-slate-50 min-w-[280px] md:min-w-[320px]">
              <div className="text-[12px] text-slate-500 uppercase tracking-widest mb-2">Khóa học của bạn</div>
              <h3 className="text-slate-800 text-[16px] leading-snug">{course?.title || 'Đang tải...'}</h3>
           </div>
           
           <div className="flex-1 overflow-y-auto custom-scrollbar bg-white" style={{ WebkitOverflowScrolling: 'touch' }}>
             {modules.length === 0 ? (
                <div className="p-8 text-center text-slate-400 text-sm font-medium">Chưa có bài giảng nào.</div>
             ) : (
                modules.map((mod) => {
                  const moduleLectures = lectures.filter(l => l.module_id === mod.id);
                  const isExpanded = expandedModules.includes(mod.id);
                  return (
                    <div key={mod.id} className="border-b border-slate-100 last:border-0">
                      <button onClick={(e) => { e.preventDefault(); e.stopPropagation(); toggleModule(mod.id); }} className={`w-full text-left px-5 py-4 transition-colors flex justify-between items-center ${isExpanded ? 'bg-slate-50' : 'hover:bg-slate-50'}`}>
                        <h4 className="text-[14px] text-slate-800 pr-4 flex items-center gap-3">
                           <span className={`text-[10px] text-slate-400 transition-transform duration-200 ${isExpanded ? 'rotate-90 text-[#0ea5e9]' : ''}`}>▶</span>
                           {mod.title}
                        </h4>
                      </button>
                      <div className={`overflow-hidden transition-all duration-300 ease-in-out ${isExpanded ? 'max-h-[1500px] opacity-100' : 'max-h-0 opacity-0'}`}>
                        <div className="py-2 bg-white">
                          {moduleLectures.length === 0 ? (
                             <div className="pl-12 pr-4 py-2 text-[13px] text-slate-400 italic">Chưa có bài giảng</div>
                          ) : (
                             moduleLectures.map((lec) => {
                               const isActive = activeLectureId === lec.id;
                               const totalTasks = Array.isArray(lec.task_list) ? lec.task_list.length : 0;
                               const completedCount = allLectureProgress[lec.id]?.length || 0;

                               return (
                                 <button key={lec.id} onClick={() => handleSelectLecture(lec.id)} className={`w-full text-left pl-12 pr-5 py-3 text-[14px] transition-colors flex items-center justify-between gap-3 relative border-l-4 ${isActive ? 'bg-[#f0f9ff] text-[#0ea5e9] border-[#0ea5e9]' : 'border-transparent text-slate-600 hover:text-slate-900 hover:bg-slate-100'}`}>
                                   <span className="leading-snug truncate flex-1">{lec.title}</span>
                                   <span className="shrink-0 ml-1 flex items-center">
                                       {totalTasks > 0 ? (
                                           completedCount === totalTasks ? (
                                               <span className="bg-emerald-100 text-emerald-700 text-[10px] font-black px-2 py-0.5 rounded shadow-sm">✓ {completedCount}/{totalTasks}</span>
                                           ) : completedCount > 0 ? (
                                               <span className="bg-blue-100 text-[#0ea5e9] text-[10px] font-bold px-2 py-0.5 rounded shadow-sm">{completedCount}/{totalTasks}</span>
                                           ) : (
                                               <span className="bg-white text-slate-500 text-[10px] font-bold px-2 py-0.5 rounded border border-slate-200">0/{totalTasks}</span>
                                           )
                                       ) : (
                                           <span className="bg-slate-100 text-slate-500 text-[9px] uppercase tracking-wider font-bold px-2 py-0.5 rounded border border-slate-200">Lý thuyết</span>
                                       )}
                                   </span>
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

         {/* CỘT NỘI DUNG CHÍNH */}
         <main 
            className="flex-1 overflow-y-auto bg-[#f1f5f9] custom-scrollbar relative lecture-content"
            style={{ WebkitOverflowScrolling: 'touch' }}
            ref={containerRef}
            onMouseUp={handleTextSelection}
         >
             <div className="min-h-full flex flex-col items-center py-6 md:py-10 px-0 sm:px-4 md:px-8">
               <div className="max-w-[1000px] w-full bg-white shadow-sm border border-slate-200 flex-none rounded-none sm:rounded-2xl p-8 md:p-14 mb-8 min-h-[50vh]">
                  {!activeLectureId ? (
                    <div className="text-center py-24 text-slate-400 font-medium text-lg">Vui lòng chọn bài giảng ở danh mục bên trái.</div>
                  ) : !currentHtmlContent ? (
                    <div className="text-center py-24 text-slate-400 font-medium flex flex-col items-center gap-3">
                       <span className="w-8 h-8 border-4 border-[#0ea5e9] border-t-transparent rounded-full animate-spin"></span>
                       Đang tải nội dung bài học...
                    </div>
                  ) : (
                    <div>
                       <h2 className="text-[24px] md:text-[34px] text-[#0a5482] font-black mb-8 md:mb-12 pb-4 border-b-2 border-slate-100 leading-snug">{activeLecture?.title}</h2>
                       <StaticLectureContent 
                          html={currentHtmlContent} 
                          onOpenPopup={setPopupUrl} 
                          onOpenDict={triggerDictionary}
                          onCloseDict={() => setDictPopup(null)}
                       />
                    </div>
                  )}
               </div>
               
               {/* THANH ĐIỀU HƯỚNG TRANG */}
               {activeLectureId && (
                  <div className="max-w-[1000px] w-full flex justify-between items-center px-6 pb-12">
                      <button onClick={handlePrevPage} disabled={currentPage === 1 && lectures.findIndex(l => l.id === activeLectureId) === 0} className="text-[#0ea5e9] font-bold text-[13px] md:text-[14px] hover:text-[#0284c7] disabled:opacity-30 transition-colors uppercase tracking-widest bg-white px-5 py-2.5 rounded-lg border border-slate-200 shadow-sm disabled:shadow-none">&lt; Trang trước</button>
                      {totalPages > 0 && (
                         <div className="flex gap-2 md:gap-3 flex-wrap justify-center px-4">
                           {Array.from({ length: totalPages }).map((_, i) => (
                                 <button key={i+1} onClick={() => setCurrentPage(i+1)} className={`w-10 h-10 md:w-11 md:h-11 rounded-xl flex items-center justify-center text-[14px] md:text-[15px] font-bold transition-all shadow-sm border ${currentPage === i+1 ? 'bg-[#0ea5e9] text-white shadow-md border-transparent' : 'text-slate-600 bg-white border border-slate-200 hover:border-[#0ea5e9] hover:text-[#0ea5e9]'}`}>{i+1}</button>
                           ))}
                         </div>
                      )}
                      <button onClick={handleNextPage} disabled={isLastLectureAndPage} className="text-[#0ea5e9] font-bold text-[13px] md:text-[14px] hover:text-[#0284c7] disabled:opacity-30 transition-colors uppercase tracking-widest bg-white px-5 py-2.5 rounded-lg border border-slate-200 shadow-sm disabled:shadow-none">Trang sau &gt;</button>
                  </div>
               )}
             </div>
         </main>
      </div>

      {dictPopup && dictPopup.show && (
         <div id="dict-popup" className="fixed bg-white rounded-2xl shadow-[0_20px_50px_rgba(0,0,0,0.2)] border border-slate-200 w-[90vw] max-w-[320px] flex flex-col overflow-hidden animate-in fade-in zoom-in-95 duration-200"
           style={{ 
             zIndex: 99999, 
             left: Math.max(10, Math.min(dictPopup.x - 160, window.innerWidth - 330)), 
             ...(window.innerHeight - dictPopup.y < 300 ? { bottom: window.innerHeight - dictPopup.rectTop + 10 } : { top: dictPopup.y + 10 }), 
             maxHeight: '380px' 
           }}>
            
            <div className="bg-slate-50 border-b border-slate-100 py-2.5 px-5 flex items-center justify-start shrink-0">
               <img src="/logo-shield.png" alt="TonyEnglish" className="h-4 w-auto object-contain mr-1.5" />
               <span className="font-black text-[12px] text-slate-700 tracking-wider">TONY<span className="text-[#0ea5e9]">ENGLISH</span> Diction</span>
            </div>

            <div className="bg-white border-b border-slate-100 p-5 flex justify-between items-start shrink-0">
               <div className="max-w-[200px]">
                  <h4 className="text-[18px] font-black text-[#e53935] truncate mb-1">{dictPopup.word}</h4>
                  {dictPopup.data?.phonetics && (<span className="text-[14px] text-slate-500 font-serif italic">{dictPopup.data.phonetics}</span>)}
               </div>
               {dictPopup.data?.audio && (<button onClick={() => playAudio(dictPopup.data.audio)} className="w-9 h-9 rounded-full bg-blue-50 text-[#0ea5e9] flex items-center justify-center hover:bg-[#0ea5e9] hover:text-white transition-colors shrink-0 shadow-sm border border-blue-100">🔊</button>)}
            </div>
            
            <div className="p-5 bg-[#f8fafc] overflow-y-auto custom-scrollbar flex-1" style={{ WebkitOverflowScrolling: 'touch' }}>
              {dictPopup.isLoading ? (
                 <div className="flex flex-col items-center justify-center py-6"><div className="w-6 h-6 border-2 border-blue-200 border-t-blue-500 rounded-full animate-spin mb-3"></div><span className="text-[13px] font-medium text-slate-500">Đang tra từ...</span></div>
              ) : (
                 <div><p className="text-[15px] font-medium text-slate-800 leading-relaxed">{dictPopup.data?.translation}</p></div>
              )}
            </div>
         </div>
      )}

      {popupUrl && (
        <div className="fixed inset-0 bg-slate-900/90 backdrop-blur-sm flex flex-col items-center justify-center p-4 md:p-8 animate-in fade-in duration-200" style={{ zIndex: 99999 }}>
          <div className="w-full max-w-6xl flex justify-end mb-4">
             <button 
                onClick={() => setPopupUrl(null)} 
                className="w-12 h-12 rounded-full bg-white/10 border border-white/20 hover:bg-red-500 flex items-center justify-center text-white text-2xl font-black transition-colors"
             >✕</button>
          </div>
          <div className="w-full max-w-6xl h-[85vh] bg-black rounded-2xl overflow-hidden shadow-2xl relative border border-slate-700">
             <div className="absolute inset-0 flex items-center justify-center bg-slate-900 z-0">
                <div className="flex flex-col items-center gap-4">
                   <div className="w-10 h-10 border-4 border-[#0ea5e9] border-t-transparent rounded-full animate-spin"></div>
                   <span className="font-bold text-slate-400 uppercase tracking-widest text-sm">Đang tải tài liệu...</span>
                </div>
             </div>
             <iframe src={getEmbedUrl(popupUrl)} className="absolute inset-0 w-full h-full border-0 z-10 bg-white" allowFullScreen></iframe>
          </div>
        </div>
      )}
    </div>
  );
}