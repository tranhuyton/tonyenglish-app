import React, { useState } from 'react';
import Home from './Home';
import StudentPortal from './StudentPortal';
import ComputerTest from './ComputerTest';
import PaperTest from './PaperTest';
import StandardTest from './StandardTest';
import AdminPanel from './AdminPanel';
import IeltsWriting from './IeltsWriting';
import IeltsSpeaking from './IeltsSpeaking';

export default function App() {
  // ĐÃ SỬA: Trả mặc định về 'home' (Trang đăng nhập) thay vì 'portal'
  const [currentView, setCurrentView] = useState('home'); 
  const [currentTestData, setCurrentTestData] = useState<any>(null);

  // Hàm xử lý khi học sinh bấm "Làm bài"
  const handleStartTest = (type: string, data: any) => {
    setCurrentTestData(data);
    setCurrentView(type);
  };

  // Hàm xử lý điều hướng chung
  const handleNavigate = (view: string) => {
    setCurrentView(view);
  };

  return (
    <React.Fragment>
      {/* 1. TRANG CHỦ (HOME - LOGIN) */}
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
      
      {/* 3. TRANG QUẢN TRỊ (ADMIN) */}
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
    </React.Fragment>
  );
}