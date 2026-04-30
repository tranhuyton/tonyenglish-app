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

export default function App() {
  const getInitialView = () => {
    const path = window.location.pathname;
    if (path === '/admin' || path === '/admin/') {
      return 'admin-login'; 
    }
    return 'home'; 
  };

  const [currentView, setCurrentView] = useState(getInitialView()); 
  const [currentTestData, setCurrentTestData] = useState<any>(null);

  useEffect(() => {
    if (currentView === 'admin' || currentView === 'admin-login') {
      window.history.pushState(null, '', '/admin');
    } else if (currentView === 'home') {
      window.history.pushState(null, '', '/');
    }
  }, [currentView]);

  // ĐÃ FIX: CHỈ CHẠY 1 LẦN DUY NHẤT, KHÔNG BỊ VÒNG LẶP GIẬT NGƯỢC VỀ PORTAL NỮA
  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      if (session) {
        setCurrentView(prev => prev === 'home' ? 'portal' : prev);
      }
    });

    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      if (event === 'SIGNED_IN') {
        setCurrentView('portal'); 
      } else if (event === 'SIGNED_OUT') {
        setCurrentView(prev => (prev !== 'admin' && prev !== 'admin-login') ? 'home' : prev); 
      }
    });

    return () => subscription.unsubscribe();
  }, []); // <== Mấu chốt ở đây: bỏ mảng dependency đi để nó không chạy lại liên tục

  const handleStartTest = (type: string, data: any) => {
    setCurrentTestData(data);
    setCurrentView(type);
  };

  const handleNavigate = (view: string) => {
    setCurrentView(view);
  };

  return (
    <React.Fragment>
      {currentView === 'admin-login' && (
        <AdminLogin onLoginSuccess={() => setCurrentView('admin')} />
      )}

      {currentView === 'home' && (
        <Home onNavigate={handleNavigate} onStartTest={handleStartTest} />
      )}
      
      {currentView === 'portal' && (
        <StudentPortal 
          onNavigate={handleNavigate} 
          onStartTest={handleStartTest} 
        />
      )}
      
      {currentView === 'admin' && (
        <AdminPanel onNavigate={handleNavigate} />
      )}
      
      {currentView === 'ielts-writing' && (
        <IeltsWriting onBack={() => setCurrentView('portal')} />
      )}
      
      {currentView === 'ielts-speaking' && (
        <IeltsSpeaking onBack={() => setCurrentView('portal')} />
      )}

      {currentView === 'computer' && (
        <ComputerTest 
          onBack={() => setCurrentView('portal')} 
          testData={currentTestData} 
        />
      )}

      {currentView === 'paper' && (
        <PaperTest 
          onBack={() => setCurrentView('portal')} 
          testData={currentTestData} 
        />
      )}

      {currentView === 'standard' && (
        <StandardTest 
          onBack={() => setCurrentView('portal')} 
          testData={currentTestData} 
          onFinish={(res: any) => {
            console.log("Kết quả bài thi:", res);
            setCurrentView('portal');
          }} 
        />
      )}

      {currentView === 'case-study' && (
        <SplitScreenTest onBack={() => setCurrentView('portal')} />
      )}
    </React.Fragment>
  );
}