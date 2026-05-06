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
import SiegeGame from './SiegeGame'; // 🚀 KHAI BÁO THÊM MINI-GAME VÀO HỆ THỐNG

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

  // State lưu mã khóa học khi bấm vào học bài giảng
  const [activeCourseId, setActiveCourseId] = useState<string | null>(() => {
    return sessionStorage.getItem('lms_active_course_id') || null;
  });

  // State lưu lại NƠI XUẤT PHÁT (để thi xong biết đường quay về)
  const [returnView, setReturnView] = useState<string>(() => {
    return sessionStorage.getItem('lms_return_view') || 'portal';
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
      if (event === 'SIGNED_IN') {
        setCurrentView(prev => prev === 'home' ? 'portal' : prev); 
      } else if (event === 'SIGNED_OUT') {
        setCurrentView(prev => (prev !== 'admin' && prev !== 'admin-login') ? 'home' : prev); 
        // Xóa sạch bộ nhớ đệm khi đăng xuất
        sessionStorage.removeItem('lms_current_view');
        sessionStorage.removeItem('lms_current_test');
        sessionStorage.removeItem('lms_active_course_id');
        sessionStorage.removeItem('lms_return_view'); // Xóa trí nhớ đường về
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
    
    // BÍ KÍP: Lưu lại màn hình hiện tại vào "returnView" trước khi nhảy sang bài thi/game
    setReturnView(currentView);
    sessionStorage.setItem('lms_return_view', currentView);

    handleNavigate(type);
    sessionStorage.setItem('lms_current_test', JSON.stringify(data));
  };

  // Hàm mở bài giảng kèm lưu lại Khóa học đang học
  const handleOpenLecture = (courseId: string) => {
    setActiveCourseId(courseId);
    sessionStorage.setItem('lms_active_course_id', courseId);
    handleNavigate('lecture');
  };

  // HÀM ĐIỀU HƯỚNG QUAY VỀ ĐÚNG NƠI XUẤT PHÁT
  const handleReturnFromTest = () => {
    handleNavigate(returnView);
  };

  return (
    <React.Fragment>

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
          onOpenLecture={handleOpenLecture}
        />
      )}
      
      {currentView === 'admin' && (
        <AdminPanel onNavigate={handleNavigate} />
      )}
      
      {currentView === 'ielts-writing' && (
        <IeltsWriting onBack={handleReturnFromTest} />
      )}
      
      {currentView === 'ielts-speaking' && (
        <IeltsSpeaking onBack={handleReturnFromTest} />
      )}

      {currentView === 'computer' && (
        <ComputerTest 
          onBack={handleReturnFromTest} 
          testData={currentTestData} 
        />
      )}

      {currentView === 'paper' && (
        <PaperTest 
          onBack={handleReturnFromTest} 
          testData={currentTestData} 
        />
      )}

      {currentView === 'standard' && (
        <StandardTest 
          onBack={handleReturnFromTest} 
          testData={currentTestData} 
          onFinish={(res: any) => {
            console.log("Kết quả bài thi:", res);
            handleReturnFromTest(); // Chạy về nơi xuất phát khi nộp bài
          }} 
        />
      )}

      {currentView === 'case-study' && (
        <SplitScreenTest onBack={handleReturnFromTest} />
      )}

      {/* 🚀 LUỒNG RẼ NHÁNH CHO MINI-GAME CÔNG THÀNH CHIẾN */}
      {currentView === 'siege-game' && (
        <SiegeGame onBack={handleReturnFromTest} />
      )}

      {/* MÀN HÌNH BÀI GIẢNG (LECTURE) */}
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