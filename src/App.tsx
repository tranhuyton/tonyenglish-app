import React, { useState, useEffect } from 'react';
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

export default function App() {
  const getInitialView = () => {
    const path = window.location.pathname;
    if (path === '/admin' || path === '/admin/') return 'admin-login'; 
    return sessionStorage.getItem('lms_current_view') || 'home'; 
  };

  const [currentView, setCurrentView] = useState(getInitialView()); 
  const [currentTestData, setCurrentTestData] = useState<any>(() => {
    const savedTest = sessionStorage.getItem('lms_current_test');
    return savedTest ? JSON.parse(savedTest) : null;
  });

  const [activeCourseId, setActiveCourseId] = useState<string | null>(() => {
    return sessionStorage.getItem('lms_active_course_id') || null;
  });

  const [returnView, setReturnView] = useState<string>(() => {
    return sessionStorage.getItem('lms_return_view') || 'portal';
  });

  useEffect(() => {
    if (currentView === 'admin' || currentView === 'admin-login') window.history.pushState(null, '', '/admin');
    else if (currentView === 'home') window.history.pushState(null, '', '/');
  }, [currentView]);

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      if (session) setCurrentView(prev => prev === 'home' ? 'portal' : prev);
    });

    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      if (event === 'SIGNED_IN') {
        setCurrentView(prev => prev === 'home' ? 'portal' : prev); 
      } else if (event === 'SIGNED_OUT') {
        setCurrentView(prev => (prev !== 'admin' && prev !== 'admin-login') ? 'home' : prev); 
        sessionStorage.removeItem('lms_current_view');
        sessionStorage.removeItem('lms_current_test');
        sessionStorage.removeItem('lms_active_course_id');
        sessionStorage.removeItem('lms_return_view'); 
      }
    });
    return () => subscription.unsubscribe();
  }, []); 

  const handleNavigate = (view: string) => {
    setCurrentView(view);
    sessionStorage.setItem('lms_current_view', view);
  };

  const handleStartTest = (type: string, data: any) => {
    setCurrentTestData(data);
    setReturnView(currentView);
    sessionStorage.setItem('lms_return_view', currentView);

    let targetView = type.toLowerCase();
    if (targetView.includes('standard')) targetView = 'standard';
    else if (targetView.includes('case-study') || targetView.includes('business')) targetView = 'case-study';

    handleNavigate(targetView);
    sessionStorage.setItem('lms_current_test', JSON.stringify(data));
  };

  const handleOpenLecture = (courseId: string) => {
    setActiveCourseId(courseId);
    sessionStorage.setItem('lms_active_course_id', courseId);
    handleNavigate('lecture');
  };

  const handleReturnFromTest = () => handleNavigate(returnView);

  return (
    <React.Fragment>
      {currentView === 'admin-login' && <AdminLogin onLoginSuccess={() => handleNavigate('admin')} />}
      {currentView === 'home' && <Home onNavigate={handleNavigate} onStartTest={handleStartTest} />}
      {currentView === 'portal' && <StudentPortal onNavigate={handleNavigate} onStartTest={handleStartTest} onOpenLecture={handleOpenLecture}/>}
      {currentView === 'admin' && <AdminPanel onNavigate={handleNavigate} />}
      {currentView === 'ielts-writing' && <IeltsWriting onBack={handleReturnFromTest} />}
      {currentView === 'ielts-speaking' && <IeltsSpeaking onBack={handleReturnFromTest} />}
      {currentView === 'computer' && <ComputerTest onBack={handleReturnFromTest} testData={currentTestData} />}
      {currentView === 'paper' && <PaperTest onBack={handleReturnFromTest} testData={currentTestData} />}
      {currentView === 'standard' && <StandardTest onBack={handleReturnFromTest} testData={currentTestData} onFinish={handleReturnFromTest} />}
      {currentView === 'case-study' && <SplitScreenTest onBack={handleReturnFromTest} testData={currentTestData} />}
      {currentView === 'siege-game' && <SiegeGame onBack={handleReturnFromTest} />}
      
      {currentView === 'lecture' && activeCourseId && (
        <LectureViewer 
          courseId={activeCourseId}
          onBack={() => handleNavigate('portal')} 
          onStartTest={handleStartTest}
        />
      )}
    </React.Fragment>
  );
}