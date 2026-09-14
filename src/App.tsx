import React, { useState, useEffect, useRef, Suspense } from 'react';
import { supabase } from './supabase';
import Home from './Home';
import StudentPortal from './StudentPortal';
import { lazyWithRetry, AppErrorBoundary } from './chunkReload';

// 🚀 CODE SPLITTING: Lazy load các component nặng có cơ chế tự động phục hồi khi có bản cập nhật mới
const ComputerTest = lazyWithRetry(() => import('./ComputerTest'));
const PaperTest = lazyWithRetry(() => import('./PaperTest'));
const StandardMCQTest = lazyWithRetry(() => import('./StandardMCQTest'));
const StandardSplitScreenTest = lazyWithRetry(() => import('./StandardSplitScreenTest'));
const AdminPanel = lazyWithRetry(() => import('./AdminPanel'));
const AdminLogin = lazyWithRetry(() => import('./AdminLogin'));
const IeltsWriting = lazyWithRetry(() => import('./IeltsWriting'));
const IeltsSpeaking = lazyWithRetry(() => import('./IeltsSpeaking'));
const SplitScreenTest = lazyWithRetry(() => import('./SplitScreenTest'));
const LectureViewer = lazyWithRetry(() => import('./LectureViewer'));
const SiegeGame = lazyWithRetry(() => import('./SiegeGame'));
const NinjaSurvival = lazyWithRetry(() => import('./NinjaSurvival'));
const VocabRacing = lazyWithRetry(() => import('./VocabRacing'));
const IgcsePaperTest = lazyWithRetry(() => import('./IgcsePaperTest'));
const IgcseDirectPaperTest = lazyWithRetry(() => import('./IgcseDirectPaperTest'));
const AITutorSidebar = lazyWithRetry(() => import('./AITutorSidebar'));
const LiveSpeakingTest = lazyWithRetry(() => import('./LiveSpeakingTest'));
const MixedPaperTest = lazyWithRetry(() => import('./MixedPaperTest'));

// Loading fallback khi đang tải component
const LoadingFallback = () => (
  <div className="h-screen bg-[#f8fafc] flex flex-col items-center justify-center gap-4">
    <div className="w-12 h-12 border-4 border-slate-200 border-t-[#2bd6eb] rounded-full animate-spin" />
    <p className="text-slate-500 font-bold text-sm animate-pulse">Đang tải...</p>
  </div>
);

export default function App() {
  const getInitialView = () => {
    const path = window.location.pathname;
    if (path === '/admin' || path === '/admin/') return 'admin-login'; 
    try { return sessionStorage.getItem('lms_current_view') || 'home'; } catch(e) { return 'home'; }
  };

  const [currentView, setCurrentView] = useState(getInitialView()); 
  const timerRef = useRef<any>(null); 
  
  // --- 🤖 AI SIDEBAR STATE ---
  const [isAISidebarOpen, setIsAISidebarOpen] = useState(false);
  const [aiMode, setAiMode] = useState<'tutor' | 'ielts'>('tutor');
  const [ieltsTopic, setIeltsTopic] = useState("");
  const [ieltsImage, setIeltsImage] = useState("");
  const [ieltsTaskType, setIeltsTaskType] = useState("task2");
  const [currentLectureTitle, setCurrentLectureTitle] = useState("");
  const [currentHtmlContent, setCurrentHtmlContent] = useState("");

  // 🚀 LIVE TUTOR WIDGET STATE
  const [liveTutorState, setLiveTutorState] = useState<'CLOSED' | 'FULLSCREEN' | 'MINIMIZED'>('CLOSED');

  useEffect(() => {
    const handleGlobalClick = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      
      const triggerBtn = target.closest('.btn-ai-trigger, .btn-ielts-trigger'); 
      if (triggerBtn) {
        const topicText = triggerBtn.getAttribute('data-topic');
        const topicImg = triggerBtn.getAttribute('data-image'); 
        const taskLabel = triggerBtn.getAttribute('data-task') || 'task2';
        
        if (topicText || topicImg) {
          setIeltsTopic(topicText || "");
          setIeltsImage(topicImg || ""); 
          setIeltsTaskType(taskLabel); 
          setAiMode('ielts');       
          setIsAISidebarOpen(true); 
        }
        return; 
      }

      // 🚀 BẮT NÚT GỌI TỪ BÀI GIẢNG VÀ MỞ FULLSCREEN WIDGET
      const liveBtn = target.closest('.btn-live-trigger');
      if (liveBtn) {
          const topicText = liveBtn.getAttribute('data-topic');
          if (topicText) {
              sessionStorage.setItem('tony_live_topic', topicText);
              sessionStorage.removeItem('tony_live_mode'); 
              sessionStorage.removeItem('tony_tutor_data'); 
              setLiveTutorState('FULLSCREEN'); 
          }
      }
    };

    const handleUpdateContext = (e: any) => {
      setCurrentLectureTitle(e.detail.title || "");
      setCurrentHtmlContent(e.detail.html || "");
    };

    document.addEventListener('click', handleGlobalClick);
    window.addEventListener('tony-update-lecture-context', handleUpdateContext);
    return () => {
      document.removeEventListener('click', handleGlobalClick);
      window.removeEventListener('tony-update-lecture-context', handleUpdateContext);
    };
  }, []);

  // 🚀 INTERCEPT ĐIỀU HƯỚNG: NẾU LÀ 'live-test', KHÔNG CHUYỂN TRANG MÀ MỞ WIDGET
  useEffect(() => {
    const handleCustomNavigate = (e: any) => {
      const view = e.detail;
      if (view === 'live-test') {
         if (liveTutorState === 'FULLSCREEN') {
           // Đã đang ở bảng → không làm gì (tránh restart conversation)
           return;
         } else {
           setLiveTutorState('FULLSCREEN');
         }
      } else if (view) {
         setCurrentView(view);
         try { sessionStorage.setItem('lms_current_view', view); } catch(err) {}
      }
    };
    const handleChangeCourse = (e: any) => {
      const newCourseId = e.detail;
      if (newCourseId) {
        setActiveCourseId(newCourseId);
        try { sessionStorage.setItem('lms_active_course_id', newCourseId); } catch(err) {}
      }
    };
    window.addEventListener('tony-navigate', handleCustomNavigate);
    window.addEventListener('tony-change-course', handleChangeCourse);
    return () => {
      window.removeEventListener('tony-navigate', handleCustomNavigate);
      window.removeEventListener('tony-change-course', handleChangeCourse);
    };
  }, [liveTutorState]);

  const [currentTestData, setCurrentTestData] = useState<any>(() => {
    try {
      const savedTest = sessionStorage.getItem('lms_current_test');
      return savedTest ? JSON.parse(savedTest) : null;
    } catch (e) { return null; }
  });

  const [activeCourseId, setActiveCourseId] = useState<string | null>(() => {
    try { 
      return sessionStorage.getItem('lms_active_course_id') || sessionStorage.getItem('portal_selected_course_id') || null; 
    } catch(e) { return null; }
  });

  const [activeCourseTitle, setActiveCourseTitle] = useState<string>("");

  useEffect(() => {
    if (!activeCourseId) {
      setActiveCourseTitle("");
      return;
    }
    supabase.from('courses')
      .select('title')
      .eq('id', activeCourseId)
      .single()
      .then(({ data }) => {
        if (data) {
          setActiveCourseTitle(data.title);
        }
      });
  }, [activeCourseId]);

  const [returnView, setReturnView] = useState<string>(() => {
    try { return sessionStorage.getItem('lms_return_view') || 'portal'; } catch(e) { return 'portal'; }
  });

  useEffect(() => {
    // 🚀 Xóa lựa chọn giọng khi chuyển trang → hỏi lại khi vào trang mới
    try { sessionStorage.removeItem('tony_voice_examiner'); } catch(e) {}
    if (currentView === 'admin' || currentView === 'admin-login') window.history.pushState(null, '', '/admin');
    else if (currentView === 'home') window.history.pushState(null, '', '/');
  }, [currentView]);

  useEffect(() => {
    const startGlobalTimer = () => {
      if (!timerRef.current) {
        timerRef.current = setInterval(() => {
          // Tạm dừng hoàn toàn khi tab bị ẩn (tiết kiệm tài nguyên Supabase)
          if (document.hidden) return;
          try {
            const currentSecs = parseInt(localStorage.getItem('tony_global_time') || '0');
            const newSecs = currentSecs + 60;
            localStorage.setItem('tony_global_time', newSecs.toString());
            // Chỉ gọi Supabase mỗi 15 phút thay vì 5 phút
            if (newSecs > 0 && newSecs % 900 === 0) {
              supabase.auth.getSession().then(({ data: { session } }) => {
                const user = session?.user;
                if (user) supabase.from('profiles').update({ study_time_seconds: newSecs }).eq('id', user.id).then().catch(console.error);
              }).catch(console.warn);
            }
          } catch(e) {}
        }, 60000); // Chạy mỗi 60 giây thay vì mỗi giây
      }
    };
    const stopGlobalTimer = () => { if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; } };

    // Tự động dừng/chạy timer khi tab bị ẩn/hiện
    const handleVisibility = () => {
      if (document.hidden) {
        stopGlobalTimer();
      } else {
        supabase.auth.getSession().then(({ data: { session } }) => {
          if (session) startGlobalTimer();
        }).catch(console.warn);
      }
    };
    document.addEventListener('visibilitychange', handleVisibility);

    supabase.auth.getSession().then(({ data: { session } }) => { if (session) { setCurrentView(prev => prev === 'home' ? 'portal' : prev); startGlobalTimer(); } }).catch(console.warn);
    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      if (event === 'SIGNED_IN') { setCurrentView(prev => prev === 'home' ? 'portal' : prev); startGlobalTimer(); }
      else if (event === 'SIGNED_OUT') {
        setCurrentView(prev => (prev !== 'admin' && prev !== 'admin-login') ? 'home' : prev); 
        try { sessionStorage.removeItem('lms_current_view'); sessionStorage.removeItem('lms_current_test'); sessionStorage.removeItem('lms_active_course_id'); sessionStorage.removeItem('lms_return_view'); } catch(e) {}
        stopGlobalTimer(); 
      }
    });
    return () => { subscription.unsubscribe(); stopGlobalTimer(); document.removeEventListener('visibilitychange', handleVisibility); };
  }, []); 

  const handleNavigate = (view: string) => { setCurrentView(view); try { sessionStorage.setItem('lms_current_view', view); } catch(e) {} };
  const handleStartTest = (type: string, data: any) => {
    try {
      setCurrentTestData(data); setReturnView(currentView); sessionStorage.setItem('lms_return_view', currentView);
      let targetView = type.toLowerCase();
      if (data?.title?.includes('Volume 4') || data?.title?.includes('Volume 3') || data?.title?.includes('Volume 2') || data?.title?.includes('Volume 1')) targetView = 'standard-splitscreen';
      else if (targetView.includes('igcse-direct')) targetView = 'igcse-direct';
      else if (targetView.includes('igcse')) targetView = 'igcse';
      else if (targetView.includes('standard-reading') || (targetView.includes('splitscreen') && targetView.includes('standard'))) targetView = 'standard-splitscreen';
      else if (targetView.includes('split-standard')) targetView = 'case-study';
      else if (targetView.includes('standard')) targetView = 'standard';
      else if (targetView.includes('case-study') || targetView.includes('business') || targetView.includes('splitscreen')) targetView = 'case-study';
      else if (targetView.includes('mixed-paper')) targetView = 'mixed-paper';
      handleNavigate(targetView); sessionStorage.setItem('lms_current_test', JSON.stringify(data));
    } catch (error) {}
  };
  const handleOpenLecture = (courseId: string, lectureId?: string) => { 
    setActiveCourseId(courseId); 
    try { 
      sessionStorage.setItem('lms_active_course_id', courseId); 
      if (lectureId) {
        sessionStorage.setItem('tony_target_lecture_id', lectureId);
        window.dispatchEvent(new CustomEvent('tony-open-target-lecture', { detail: lectureId }));
      }
    } catch(e) {} 
    handleNavigate('lecture'); 
  };
  const handleReturnFromTest = () => {
    handleNavigate(returnView);
    setTimeout(() => {
      window.dispatchEvent(new CustomEvent('tony-refresh-lecture-progress'));
    }, 150);
  };

  const validViews = ['admin-login', 'home', 'portal', 'admin', 'ielts-writing', 'ielts-speaking', 'computer', 'paper', 'mixed-paper', 'standard', 'standard-splitscreen', 'case-study', 'igcse', 'igcse-direct', 'siege-game', 'ninja-survival', 'vocab-racing', 'lecture'];

  return (
    <React.Fragment>
      {/* Eager-loaded components (luôn cần) */}
      {currentView === 'home' && <Home onNavigate={handleNavigate} onStartTest={handleStartTest} />}
      {currentView === 'portal' && <StudentPortal onNavigate={handleNavigate} onStartTest={handleStartTest} onOpenLecture={handleOpenLecture} />}
      
      {/* Lazy-loaded components (chỉ tải khi cần) bọc trong AppErrorBoundary chống sập màn hình trắng */}
      <AppErrorBoundary>
        <Suspense fallback={<LoadingFallback />}>
          {currentView === 'admin-login' && <AdminLogin onLoginSuccess={() => handleNavigate('admin')} />}
          
          {/* 🚀 ĐÃ NỐI CẦU ONSTARTTEST VÀO ADMIN PANEL */}
          {currentView === 'admin' && <AdminPanel onNavigate={handleNavigate} onStartTest={handleStartTest} />}
          
          {currentView === 'ielts-writing' && <IeltsWriting onBack={handleReturnFromTest} />}
          {currentView === 'ielts-speaking' && <IeltsSpeaking onBack={handleReturnFromTest} />}
          
          {currentView === 'computer' && <ComputerTest onBack={handleReturnFromTest} testData={currentTestData} />}
          {currentView === 'paper' && <PaperTest onBack={handleReturnFromTest} testData={currentTestData} />}
          {currentView === 'mixed-paper' && <MixedPaperTest onBack={handleReturnFromTest} testData={currentTestData} />}
          {currentView === 'standard' && <StandardMCQTest onBack={handleReturnFromTest} testData={currentTestData} onFinish={handleReturnFromTest} />}
          {currentView === 'standard-splitscreen' && <StandardSplitScreenTest onBack={handleReturnFromTest} testData={currentTestData} onFinish={handleReturnFromTest} />}
          {currentView === 'case-study' && <SplitScreenTest key={`split-${currentTestData?.id || ''}`} onBack={handleReturnFromTest} testData={currentTestData} />}
          {currentView === 'igcse' && <IgcsePaperTest onBack={handleReturnFromTest} testData={currentTestData} onStartTest={handleStartTest} />}
          {currentView === 'igcse-direct' && <IgcseDirectPaperTest onBack={handleReturnFromTest} testData={currentTestData} onStartTest={handleStartTest} />}
          {currentView === 'siege-game' && <SiegeGame onBack={handleReturnFromTest} testData={currentTestData} />}
          {currentView === 'ninja-survival' && <NinjaSurvival onBack={handleReturnFromTest} testData={currentTestData} />}
          {currentView === 'vocab-racing' && <VocabRacing onBack={handleReturnFromTest} testData={currentTestData} />}
          
          {currentView === 'lecture' && (
            <LectureViewer 
              courseId={activeCourseId || (typeof window !== 'undefined' ? (sessionStorage.getItem('lms_active_course_id') || sessionStorage.getItem('portal_selected_course_id') || '') : '')} 
              onBack={() => handleNavigate('portal')} 
              onCourseChange={(newId: string) => {
                setActiveCourseId(newId);
                try { sessionStorage.setItem('lms_active_course_id', newId); } catch(e) {}
              }}
              onStartTest={handleStartTest}
              onOpenAI={(passedMode?: string, topic?: string, image?: string, task?: string) => { 
                if (passedMode === 'ielts' || topic) {
                   setAiMode('ielts');
                   if (topic) setIeltsTopic(topic);
                   if (image) setIeltsImage(image);
                   if (task) setIeltsTaskType(task);
                } else {
                   setAiMode('tutor'); 
                }
                setIsAISidebarOpen(true); 
              }}
            />
          )}

          <AITutorSidebar 
            isOpen={isAISidebarOpen}
            onClose={() => setIsAISidebarOpen(false)}
            mode={aiMode}
            topicTitle={ieltsTopic}
            topicImage={ieltsImage} 
            taskType={ieltsTaskType}
            lectureTitle={currentLectureTitle}
            htmlContent={currentHtmlContent}
            courseTitle={activeCourseTitle}
            isCallActive={liveTutorState !== 'CLOSED'}
          />

          {/* 🚀 GLOBAL WIDGET: HIỂN THỊ ĐÈ LÊN TRÊN BÀI THI/BÀI GIẢNG */}
          {liveTutorState !== 'CLOSED' && (
            <LiveSpeakingTest 
               viewState={liveTutorState}
               onMinimize={() => setLiveTutorState('MINIMIZED')}
               onMaximize={() => setLiveTutorState('FULLSCREEN')}
               onClose={() => setLiveTutorState('CLOSED')}
               courseTitle={activeCourseTitle}
               onOpenAI={() => {
                  const topic = sessionStorage.getItem('tony_live_topic') || '';
                  if (topic) {
                     setAiMode('ielts');
                     setIeltsTopic(topic);
                  }
                  setIsAISidebarOpen(true);
               }}
            />
          )}
        </Suspense>
      </AppErrorBoundary>

      {!validViews.includes(currentView) && (
        <div className="h-screen bg-red-50 flex flex-col items-center justify-center p-8 text-center font-sans">
          <h1 className="text-4xl font-black text-red-600 mb-4">⚠️ LỖI ĐỊNH TUYẾN</h1>
          <button onClick={() => { sessionStorage.clear(); window.location.reload(); }} className="bg-red-600 text-white font-bold px-8 py-3 rounded-xl shadow-lg">Khôi phục hệ thống</button>
        </div>
      )}
    </React.Fragment>
  );
}
