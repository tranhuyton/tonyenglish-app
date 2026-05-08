import React, { useState, useEffect, useRef } from 'react';
import { supabase } from './supabase';
import Home from './Home';
import StudentPortal from './StudentPortal';
import ComputerTest from './ComputerTest';
import PaperTest from './PaperTest';
import StandardTest from './StandardTest';
import AdminPanel from './AdminPanel';
import AdminLogin from './AdminLogin';
import IeltsWriting from './IeltsWriting';
import IeltsSpeaking from './IeltsSpeaking';
import SplitScreenTest from './SplitScreenTest';
import LectureViewer from './LectureViewer'; 
import SiegeGame from './SiegeGame'; 
import NinjaSurvival from './NinjaSurvival';
import VocabRacing from './VocabRacing';

export default function App() {
  const getInitialView = () => {
    const path = window.location.pathname;
    if (path === '/admin' || path === '/admin/') return 'admin-login'; 
    try { return sessionStorage.getItem('lms_current_view') || 'home'; } 
    catch(e) { return 'home'; }
  };

  const [currentView, setCurrentView] = useState(getInitialView()); 
  const timerRef = useRef<any>(null); 
  
  // 🚀 LÁ CHẮN BẢO VỆ KHI ĐỌC BỘ NHỚ TẠM
  const [currentTestData, setCurrentTestData] = useState<any>(() => {
    try {
      const savedTest = sessionStorage.getItem('lms_current_test');
      return savedTest ? JSON.parse(savedTest) : null;
    } catch (e) {
      console.error("Lỗi đọc Session Storage:", e);
      return null;
    }
  });

  const [activeCourseId, setActiveCourseId] = useState<string | null>(() => {
    try { return sessionStorage.getItem('lms_active_course_id') || null; } catch(e) { return null; }
  });

  const [returnView, setReturnView] = useState<string>(() => {
    try { return sessionStorage.getItem('lms_return_view') || 'portal'; } catch(e) { return 'portal'; }
  });

  useEffect(() => {
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
                if (user) {
                  supabase.from('profiles').update({ study_time_seconds: newSecs }).eq('id', user.id).then();
                }
              });
            }
          } catch(e) {}
        }, 1000);
      }
    };

    const stopGlobalTimer = () => {
      if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    };

    supabase.auth.getSession().then(({ data: { session } }) => {
      if (session) {
        setCurrentView(prev => prev === 'home' ? 'portal' : prev);
        startGlobalTimer(); 
      }
    });

    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      if (event === 'SIGNED_IN') {
        setCurrentView(prev => prev === 'home' ? 'portal' : prev); 
        startGlobalTimer(); 
      } else if (event === 'SIGNED_OUT') {
        setCurrentView(prev => (prev !== 'admin' && prev !== 'admin-login') ? 'home' : prev); 
        try {
          sessionStorage.removeItem('lms_current_view');
          sessionStorage.removeItem('lms_current_test');
          sessionStorage.removeItem('lms_active_course_id');
          sessionStorage.removeItem('lms_return_view'); 
        } catch(e) {}
        stopGlobalTimer(); 
      }
    });

    return () => { subscription.unsubscribe(); stopGlobalTimer(); };
  }, []); 

  const handleNavigate = (view: string) => {
    setCurrentView(view);
    try { sessionStorage.setItem('lms_current_view', view); } catch(e) {}
  };

  const handleStartTest = (type: string, data: any) => {
    try {
      setCurrentTestData(data);
      setReturnView(currentView);
      sessionStorage.setItem('lms_return_view', currentView);

      let targetView = type.toLowerCase();
      if (targetView.includes('standard')) targetView = 'standard';
      else if (targetView.includes('case-study') || targetView.includes('business')) targetView = 'case-study';

      handleNavigate(targetView);
      sessionStorage.setItem('lms_current_test', JSON.stringify(data));
    } catch (error) {
      console.error("Lỗi khi chuyển trang game:", error);
      alert("Dữ liệu đề thi quá lớn hoặc bị lỗi cấu trúc, không thể lưu vào bộ nhớ!");
    }
  };

  const handleOpenLecture = (courseId: string) => {
    setActiveCourseId(courseId);
    try { sessionStorage.setItem('lms_active_course_id', courseId); } catch(e) {}
    handleNavigate('lecture');
  };

  const handleReturnFromTest = () => { handleNavigate(returnView); };

  // Danh sách các View hợp lệ
  const validViews = ['admin-login', 'home', 'portal', 'admin', 'ielts-writing', 'ielts-speaking', 'computer', 'paper', 'standard', 'case-study', 'siege-game', 'ninja-survival', 'vocab-racing', 'lecture'];

  return (
    <React.Fragment>

      {currentView === 'admin-login' && <AdminLogin onLoginSuccess={() => handleNavigate('admin')} />}
      {currentView === 'home' && <Home onNavigate={handleNavigate} onStartTest={handleStartTest} />}
      {currentView === 'portal' && <StudentPortal onNavigate={handleNavigate} onStartTest={handleStartTest} onOpenLecture={handleOpenLecture} />}
      {currentView === 'admin' && <AdminPanel onNavigate={handleNavigate} />}
      {currentView === 'ielts-writing' && <IeltsWriting onBack={handleReturnFromTest} />}
      {currentView === 'ielts-speaking' && <IeltsSpeaking onBack={handleReturnFromTest} />}
      {currentView === 'computer' && <ComputerTest onBack={handleReturnFromTest} testData={currentTestData} />}
      {currentView === 'paper' && <PaperTest onBack={handleReturnFromTest} testData={currentTestData} />}
      
      {currentView === 'standard' && (
        <StandardTest onBack={handleReturnFromTest} testData={currentTestData} onFinish={() => handleReturnFromTest()} />
      )}

      {currentView === 'case-study' && <SplitScreenTest onBack={handleReturnFromTest} testData={currentTestData} />}
      {currentView === 'siege-game' && <SiegeGame onBack={handleReturnFromTest} testData={currentTestData} />}
      {currentView === 'ninja-survival' && <NinjaSurvival onBack={handleReturnFromTest} testData={currentTestData} />}
      {currentView === 'vocab-racing' && <VocabRacing onBack={handleReturnFromTest} testData={currentTestData} />}
      
      {currentView === 'lecture' && activeCourseId && (
        <LectureViewer courseId={activeCourseId} onBack={() => handleNavigate('portal')} onStartTest={handleStartTest} />
      )}

      {/* 🚀 RADAR CẢNH BÁO LỖI: NẾU ĐỊNH TUYẾN BỊ LỆCH, SẼ HIỆN MÀN HÌNH ĐỎ THAY VÌ TRẮNG XÓA */}
      {!validViews.includes(currentView) && (
        <div className="h-screen bg-red-50 flex flex-col items-center justify-center p-8 text-center font-sans">
          <h1 className="text-4xl font-black text-red-600 mb-4">⚠️ LỖI ĐỊNH TUYẾN (ROUTE)</h1>
          <p className="text-slate-700 text-lg mb-8 font-medium">
            Hệ thống đang cố truy cập vào một giao diện không tồn tại: <strong className="text-red-600 bg-red-100 px-2 py-1 rounded">{currentView}</strong>
          </p>
          <button 
            onClick={() => { sessionStorage.clear(); window.location.reload(); }} 
            className="bg-red-600 hover:bg-red-700 text-white font-bold px-8 py-3 rounded-xl shadow-lg transition"
          >
            Khôi phục hệ thống (Xóa Cache)
          </button>
        </div>
      )}

    </React.Fragment>
  );
}