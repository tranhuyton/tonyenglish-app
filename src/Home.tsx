import React, { useState } from 'react';
import AuthModal from './AuthModal'; // Khôi phục file AuthModal

export default function Home({ onNavigate }: { onNavigate?: (view: string) => void }) {
  const [showAuthModal, setShowAuthModal] = useState(false); // State quản lý bật/tắt popup đăng nhập

  return (
    <div className="min-h-screen bg-[#f8fafc] font-sans text-slate-800 relative">
      {/* HEADER */}
      <header className="flex justify-between items-center px-8 py-5 bg-white shadow-sm sticky top-0 z-50">
        <div className="flex items-center gap-2 font-black text-xl tracking-tight text-[#0a5482] uppercase cursor-pointer">
          <span className="text-2xl">🛡️</span> TONY<span className="text-[#2bd6eb]">ENGLISH</span>
        </div>
        <div className="flex gap-4">
          {/* NÚT CHUYỂN TRANG ADMIN DÀNH CHO TESTER */}
          <button 
            onClick={() => onNavigate?.('admin')} 
            className="bg-red-500 hover:bg-red-600 text-white font-bold px-5 py-2.5 rounded-xl transition shadow-md flex items-center gap-2"
          >
            ⚙️ Admin Portal (Test)
          </button>
          
          {/* NÚT ĐĂNG NHẬP (Đã gắn lại lệnh bật Modal) */}
          <button 
            onClick={() => setShowAuthModal(true)}
            className="bg-[#0a5482] hover:bg-[#084266] text-white font-bold px-6 py-2.5 rounded-xl transition shadow-md"
          >
            Đăng nhập
          </button>
        </div>
      </header>

      {/* HERO SECTION */}
      <main className="flex flex-col items-center justify-center text-center px-4 pt-24 pb-10">
        <div className="bg-blue-50 text-[#0a5482] font-black text-[10px] uppercase tracking-widest px-4 py-1.5 rounded-full mb-8 border border-blue-100">
          THE FUTURE BEGINS HERE
        </div>
        
        <h1 className="text-5xl md:text-6xl font-black text-slate-800 mb-6 tracking-tight max-w-4xl leading-tight">
          Nền tảng luyện thi <span className="text-[#2bd6eb]">thông minh</span> thế hệ mới
        </h1>
        
        <p className="text-slate-500 text-lg max-w-2xl mb-10 font-medium leading-relaxed">
          Trải nghiệm môi trường thi sát thực tế 100%. Tích hợp AI phân tích điểm mạnh yếu, chấm chữa chuyên sâu. Lộ trình cá nhân hóa từ IELTS đến các môn khoa học chuẩn quốc tế.
        </p>
        
        <div className="flex flex-col sm:flex-row gap-4">
          <button 
            onClick={() => setShowAuthModal(true)}
            className="bg-[#2bd6eb] hover:bg-[#1bc1d6] text-white font-black px-8 py-3.5 rounded-xl transition shadow-lg flex items-center justify-center gap-2"
          >
            Làm bài test năng lực ➔
          </button>
          <button className="bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 font-bold px-8 py-3.5 rounded-xl transition shadow-sm">
            Tìm hiểu khóa học
          </button>
        </div>
      </main>
      
      {/* SECTION TẠI SAO CHỌN CHÚNG TÔI */}
      <section className="mt-20 text-center pb-20">
         <h2 className="text-2xl font-black text-slate-800">Tại sao chọn hệ thống của chúng tôi?</h2>
         <div className="w-16 h-1.5 bg-[#2bd6eb] mx-auto mt-4 rounded-full"></div>
      </section>

      {/* MODAL ĐĂNG NHẬP */}
      {showAuthModal && (
        <AuthModal onClose={() => setShowAuthModal(false)} onNavigate={onNavigate} />
      )}
    </div>
  );
}