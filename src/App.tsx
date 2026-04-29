import React, { useState, useEffect } from 'react';
import Home from './Home';
import StudentPortal from './StudentPortal';
import ComputerTest from './ComputerTest';
import PaperTest from './PaperTest';
import StandardTest from './StandardTest';
import AdminPanel from './AdminPanel';
import AdminLogin from './AdminLogin';
import IeltsWriting from './IeltsWriting';
import IeltsSpeaking from './IeltsSpeaking';
// BƯỚC 1: IMPORT GIAO DIỆN CHIA ĐÔI MÀN HÌNH MỚI LÀM
import SplitScreenTest from './SplitScreenTest';

export default function App() {
  // KIỂM TRA URL NGAY KHI WEB VỪA KHỞI ĐỘNG
  const getInitialView = () => {
    const path = window.location.pathname;
    if (path === '/admin' || path === '/admin/') {
      return 'admin-login'; 
    }
    return 'home'; 
  };

  const [currentView, setCurrentView] = useState(getInitialView()); 
  const [currentTestData, setCurrentTestData] = useState<any>(null);

  // ĐỒNG BỘ URL TRÊN THANH TRÌNH DUYỆT
  useEffect(() => {
    if (currentView === 'admin' || currentView === 'admin-login') {
      window.history.pushState(null, '', '/admin');
    } else if (currentView === 'home') {
      window.history.pushState(null, '', '/');
    }
  }, [currentView]);

  const handleStartTest = (type: string, data: any) => {
    setCurrentTestData(data);
    setCurrentView(type);
  };

  const handleNavigate = (view: string) => {
    setCurrentView(view);
  };

  return (
    <React.Fragment>
      {/* 0. TRANG ĐĂNG NHẬP DÀNH CHO ADMIN */}
      {currentView === 'admin-login' && (
        <AdminLogin onLoginSuccess={() => setCurrentView('admin')} />
      )}

      {/* 1. TRANG CHỦ (HOME - LOGIN CHO HỌC VIÊN) */}
      {currentView === 'home' && (
        <Home onNavigate={handleNavigate} onStartTest={handleStartTest} />
      )}
      
      {/* 2. CỔNG THÔNG TIN HỌC VIÊN (PORTAL) */}
      {currentView === 'portal' && (
        <StudentPortal 
          onNavigate={handleNavigate} 
          onStartTest={handleStartTest} 
        />
      )}
      
      {/* 3. TRANG QUẢN TRỊ (ADMIN PANEL) */}
      {currentView === 'admin' && (
        <AdminPanel onNavigate={handleNavigate} />
      )}
      
      {/* 4. PHÒNG THI IELTS WRITING */}
      {currentView === 'ielts-writing' && (
        <IeltsWriting onBack={() => setCurrentView('portal')} />
      )}
      
      {/* 5. PHÒNG THI IELTS SPEAKING */}
      {currentView === 'ielts-speaking' && (
        <IeltsSpeaking onBack={() => setCurrentView('portal')} />
      )}

      {/* 6. PHÒNG THI COMPUTER (LISTENING/READING) */}
      {currentView === 'computer' && (
        <ComputerTest 
          onBack={() => setCurrentView('portal')} 
          testData={currentTestData} 
        />
      )}

      {/* 7. PHÒNG THI PAPER (GIAO DIỆN GIẤY) */}
      {currentView === 'paper' && (
        <PaperTest 
          onBack={() => setCurrentView('portal')} 
          testData={currentTestData} 
        />
      )}

      {/* 8. PHÒNG THI TIÊU CHUẨN (STANDARD TEST - BAO GỒM IGCSE/TOEIC) */}
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

      {/* BƯỚC 2: KHAI BÁO PHÒNG THI CASE STUDY (BUSINESS/ECON) */}
      {currentView === 'case-study' && (
        <SplitScreenTest onBack={() => setCurrentView('portal')} />
      )}
    </React.Fragment>
  );
}