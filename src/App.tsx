import React, { useState, useEffect, useRef, Suspense } from 'react';
import { supabase } from './supabase';
import Home from './Home';
import StudentPortal from './StudentPortal';

// 🚀 CODE SPLITTING: Lazy load các component nặng — chỉ tải khi cần
const ComputerTest = React.lazy(() => import('./ComputerTest'));
const PaperTest = React.lazy(() => import('./PaperTest'));
const StandardTest = React.lazy(() => import('./StandardTest'));
const AdminPanel = React.lazy(() => import('./AdminPanel'));
const AdminLogin = React.lazy(() => import('./AdminLogin'));
const IeltsWriting = React.lazy(() => import('./IeltsWriting'));
const IeltsSpeaking = React.lazy(() => import('./IeltsSpeaking'));
const SplitScreenTest = React.lazy(() => import('./SplitScreenTest'));
const LectureViewer = React.lazy(() => import('./LectureViewer'));
const SiegeGame = React.lazy(() => import('./SiegeGame'));
const NinjaSurvival = React.lazy(() => import('./NinjaSurvival'));
const VocabRacing = React.lazy(() => import('./VocabRacing'));
const IgcsePaperTest = React.lazy(() => import('./IgcsePaperTest'));
const IgcseDirectPaperTest = React.lazy(() => import('./IgcseDirectPaperTest'));
const AITutorSidebar = React.lazy(() => import('./AITutorSidebar'));
const LiveSpeakingTest = React.lazy(() => import('./LiveSpeakingTest'));
const MixedPaperTest = React.lazy(() => import('./MixedPaperTest'));

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
    window.addEventListener('tony-navigate', handleCustomNavigate);
    return () => window.removeEventListener('tony-navigate', handleCustomNavigate);
  }, [liveTutorState]);

  const [currentTestData, setCurrentTestData] = useState<any>(() => {
    try {
      const savedTest = sessionStorage.getItem('lms_current_test');
      return savedTest ? JSON.parse(savedTest) : null;
    } catch (e) { return null; }
  });

  const [activeCourseId, setActiveCourseId] = useState<string | null>(() => {
    try { return sessionStorage.getItem('lms_active_course_id') || null; } catch(e) { return null; }
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
          try {
            const currentSecs = parseInt(localStorage.getItem('tony_global_time') || '0');
            const newSecs = currentSecs + 1;
            localStorage.setItem('tony_global_time', newSecs.toString());
            if (newSecs > 0 && newSecs % 300 === 0) {
              supabase.auth.getUser().then(({ data: { user } }) => {
                if (user) supabase.from('profiles').update({ study_time_seconds: newSecs }).eq('id', user.id).then();
              });
            }
          } catch(e) {}
        }, 1000);
      }
    };
    const stopGlobalTimer = () => { if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; } };
    supabase.auth.getSession().then(({ data: { session } }) => { if (session) { setCurrentView(prev => prev === 'home' ? 'portal' : prev); startGlobalTimer(); } });
    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      if (event === 'SIGNED_IN') { setCurrentView(prev => prev === 'home' ? 'portal' : prev); startGlobalTimer(); }
      else if (event === 'SIGNED_OUT') {
        setCurrentView(prev => (prev !== 'admin' && prev !== 'admin-login') ? 'home' : prev); 
        try { sessionStorage.removeItem('lms_current_view'); sessionStorage.removeItem('lms_current_test'); sessionStorage.removeItem('lms_active_course_id'); sessionStorage.removeItem('lms_return_view'); } catch(e) {}
        stopGlobalTimer(); 
      }
    });
    return () => { subscription.unsubscribe(); stopGlobalTimer(); };
  }, []); 

  const handleNavigate = (view: string) => { setCurrentView(view); try { sessionStorage.setItem('lms_current_view', view); } catch(e) {} };
  const handleStartTest = (type: string, data: any) => {
    try {
      setCurrentTestData(data); setReturnView(currentView); sessionStorage.setItem('lms_return_view', currentView);
      let targetView = type.toLowerCase();
      if (targetView.includes('igcse-direct')) targetView = 'igcse-direct'; else if (targetView.includes('igcse')) targetView = 'igcse'; else if (targetView.includes('standard')) targetView = 'standard'; else if (targetView.includes('case-study') || targetView.includes('business')) targetView = 'case-study'; else if (targetView.includes('mixed-paper')) targetView = 'mixed-paper';
      handleNavigate(targetView); sessionStorage.setItem('lms_current_test', JSON.stringify(data));
    } catch (error) {}
  };
  const handleOpenLecture = (courseId: string) => { setActiveCourseId(courseId); try { sessionStorage.setItem('lms_active_course_id', courseId); } catch(e) {} handleNavigate('lecture'); };
  const handleReturnFromTest = () => handleNavigate(returnView);

  const validViews = ['admin-login', 'home', 'portal', 'admin', 'ielts-writing', 'ielts-speaking', 'computer', 'paper', 'mixed-paper', 'standard', 'case-study', 'igcse', 'igcse-direct', 'siege-game', 'ninja-survival', 'vocab-racing', 'lecture'];

  return (
    <React.Fragment>
      {/* Eager-loaded components (luôn cần) */}
      {currentView === 'home' && <Home onNavigate={handleNavigate} onStartTest={handleStartTest} />}
      {currentView === 'portal' && <StudentPortal onNavigate={handleNavigate} onStartTest={handleStartTest} onOpenLecture={handleOpenLecture} />}
      
      {/* Lazy-loaded components (chỉ tải khi cần) */}
      <Suspense fallback={<LoadingFallback />}>
        {currentView === 'admin-login' && <AdminLogin onLoginSuccess={() => handleNavigate('admin')} />}
        
        {/* 🚀 ĐÃ NỐI CẦU ONSTARTTEST VÀO ADMIN PANEL */}
        {currentView === 'admin' && <AdminPanel onNavigate={handleNavigate} onStartTest={handleStartTest} />}
        
        {currentView === 'ielts-writing' && <IeltsWriting onBack={handleReturnFromTest} />}
        {currentView === 'ielts-speaking' && <IeltsSpeaking onBack={handleReturnFromTest} />}
        
        {currentView === 'computer' && <ComputerTest onBack={handleReturnFromTest} testData={currentTestData} />}
        {currentView === 'paper' && <PaperTest onBack={handleReturnFromTest} testData={currentTestData} />}
        {currentView === 'mixed-paper' && <MixedPaperTest onBack={handleReturnFromTest} testData={currentTestData} />}
        {currentView === 'standard' && <StandardTest onBack={handleReturnFromTest} testData={currentTestData} onFinish={handleReturnFromTest} />}
        {currentView === 'case-study' && <SplitScreenTest onBack={handleReturnFromTest} testData={currentTestData} />}
        {currentView === 'igcse' && <IgcsePaperTest onBack={handleReturnFromTest} testData={currentTestData} onStartTest={handleStartTest} />}
        {currentView === 'igcse-direct' && <IgcseDirectPaperTest onBack={handleReturnFromTest} testData={currentTestData} onStartTest={handleStartTest} />}
        {currentView === 'siege-game' && <SiegeGame onBack={handleReturnFromTest} testData={currentTestData} />}
        {currentView === 'ninja-survival' && <NinjaSurvival onBack={handleReturnFromTest} testData={currentTestData} />}
        {currentView === 'vocab-racing' && <VocabRacing onBack={handleReturnFromTest} testData={currentTestData} />}
        
        {currentView === 'lecture' && activeCourseId && (
          <LectureViewer 
            courseId={activeCourseId} 
            onBack={() => handleNavigate('portal')} 
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

      {!validViews.includes(currentView) && (
        <div className="h-screen bg-red-50 flex flex-col items-center justify-center p-8 text-center font-sans">
          <h1 className="text-4xl font-black text-red-600 mb-4">⚠️ LỖI ĐỊNH TUYẾN</h1>
          <button onClick={() => { sessionStorage.clear(); window.location.reload(); }} className="bg-red-600 text-white font-bold px-8 py-3 rounded-xl shadow-lg">Khôi phục hệ thống</button>
        </div>
      )}
    </React.Fragment>
  );
}
