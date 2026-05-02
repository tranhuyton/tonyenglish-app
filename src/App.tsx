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
import LectureViewer from './LectureViewer'; // BỔ SUNG IMPORT BÀI GIẢNG

export default function App() {
  const getInitialView = () => {
    const path = window.location.pathname;
    if (path === '/admin' || path === '/admin/') {
      return 'admin-login'; 
    }
    // Khôi phục trạng thái màn hình cũ nếu có (Chống F5 Reload & Tiết kiệm RAM)
    const savedView = sessionStorage.getItem('lms_current_view');
    return savedView || 'home'; 
  };

  const [currentView, setCurrentView] = useState(getInitialView()); 
  
  // Khôi phục đề thi cũ đang làm dở nếu bị Reload
  const [currentTestData, setCurrentTestData] = useState<any>(() => {
    const savedTest = sessionStorage.getItem('lms_current_test');
    return savedTest ? JSON.parse(savedTest) : null;
  });

  useEffect(() => {
    if (currentView === 'admin' || currentView === 'admin-login') {
      window.history.pushState(null, '', '/admin');
    } else if (currentView === 'home') {
      window.history.pushState(null, '', '/');
    }
  }, [currentView]);

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      if (session) {
        setCurrentView(prev => prev === 'home' ? 'portal' : prev);
      }
    });

    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      // ĐÃ FIX: Chỉ đẩy về Portal nếu người dùng đang đứng ở ngoài Home.
      // Nếu đang trong phòng thi (computer/paper), kệ cho họ thi tiếp!
      if (event === 'SIGNED_IN') {
        setCurrentView(prev => prev === 'home' ? 'portal' : prev); 
      } else if (event === 'SIGNED_OUT') {
        setCurrentView(prev => (prev !== 'admin' && prev !== 'admin-login') ? 'home' : prev); 
        // Xóa sạch bộ nhớ đệm khi đăng xuất
        sessionStorage.removeItem('lms_current_view');
        sessionStorage.removeItem('lms_current_test');
      }
    });

    return () => subscription.unsubscribe();
  }, []); 

  // Hàm chuyển trang kèm lưu bộ nhớ đệm
  const handleNavigate = (view: string) => {
    setCurrentView(view);
    sessionStorage.setItem('lms_current_view', view);
  };

  // Hàm vào phòng thi kèm lưu đề thi vào bộ nhớ đệm
  const handleStartTest = (type: string, data: any) => {
    setCurrentTestData(data);
    setCurrentView(type);
    sessionStorage.setItem('lms_current_view', type);
    sessionStorage.setItem('lms_current_test', JSON.stringify(data));
  };

  return (
    <React.Fragment>
      
      {/* NÚT TEST TẠM THỜI (Góc dưới bên phải) CHO BÀI GIẢNG */}
      {(currentView === 'home' || currentView === 'portal') && (
        <button
          onClick={() => handleNavigate('lecture')}
          className="fixed bottom-8 right-8 bg-amber-500 hover:bg-amber-600 text-white font-bold py-4 px-8 rounded-full shadow-2xl z-50 transition-transform active:scale-95"
        >
          🚀 Test Giao diện Bài Giảng
        </button>
      )}

      {currentView === 'admin-login' && (
        <AdminLogin onLoginSuccess={() => handleNavigate('admin')} />
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
        <IeltsWriting onBack={() => handleNavigate('portal')} />
      )}
      
      {currentView === 'ielts-speaking' && (
        <IeltsSpeaking onBack={() => handleNavigate('portal')} />
      )}

      {currentView === 'computer' && (
        <ComputerTest 
          onBack={() => handleNavigate('portal')} 
          testData={currentTestData} 
        />
      )}

      {currentView === 'paper' && (
        <PaperTest 
          onBack={() => handleNavigate('portal')} 
          testData={currentTestData} 
        />
      )}

      {currentView === 'standard' && (
        <StandardTest 
          onBack={() => handleNavigate('portal')} 
          testData={currentTestData} 
          onFinish={(res: any) => {
            console.log("Kết quả bài thi:", res);
            handleNavigate('portal');
          }} 
        />
      )}

      {currentView === 'case-study' && (
        <SplitScreenTest onBack={() => handleNavigate('portal')} />
      )}

      {/* MÀN HÌNH BÀI GIẢNG (LECTURE) */}
      {currentView === 'lecture' && (
        <LectureViewer onBack={() => handleNavigate('portal')} />
      )}

    </React.Fragment>
  );
}