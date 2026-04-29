import React from 'react';
import { supabase } from './supabase';

export default function StudentPortal({ onNavigate, onStartTest }: { onNavigate: (view: string) => void, onStartTest: (type: string, data: any) => void }) {
  
  const handleLogout = async () => {
    await supabase.auth.signOut();
    onNavigate('home');
  };

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-800">
      
      {/* HEADER */}
      <header className="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-sm">
        <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-3">
             <div className="w-8 h-8 bg-blue-100 text-[#0a5482] rounded-lg flex items-center justify-center font-black">🎓</div>
             <h1 className="font-black text-[#0a5482] text-xl">Góc Học Viên</h1>
          </div>
          <button 
            onClick={handleLogout}
            className="text-sm font-bold text-slate-500 hover:text-red-500 transition-colors"
          >
            Đăng xuất ➜
          </button>
        </div>
      </header>

      {/* NỘI DUNG CHÍNH */}
      <main className="max-w-7xl mx-auto px-6 py-12">
        <div className="mb-10">
          <h2 className="text-3xl font-black text-slate-800 mb-2">Chào mừng bạn quay lại! 👋</h2>
          <p className="text-slate-500 font-medium">Hãy chọn một bài thi bên dưới để bắt đầu ôn luyện nhé.</p>
        </div>

        {/* DANH SÁCH BÀI THI */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          
          {/* Card 1: IELTS Computer */}
          <div className="bg-white border border-slate-200 rounded-2xl p-6 hover:shadow-lg transition-shadow group flex flex-col">
            <div className="w-12 h-12 bg-blue-50 text-blue-600 rounded-xl flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition-transform">🎧</div>
            <h3 className="text-lg font-black text-slate-800 mb-2">IELTS Computer</h3>
            <p className="text-sm text-slate-500 font-medium mb-6 flex-1">Thi thử IELTS Listening & Reading với giao diện máy tính chuẩn IDP/BC.</p>
            <button 
              onClick={() => onStartTest('computer', {})}
              className="w-full bg-slate-100 hover:bg-[#1e88e5] text-slate-700 hover:text-white font-bold py-3 rounded-xl transition-colors"
            >
              Vào phòng thi
            </button>
          </div>

          {/* Card 2: Standard Test (IGCSE Science / Math) */}
          <div className="bg-white border border-slate-200 rounded-2xl p-6 hover:shadow-lg transition-shadow group flex flex-col">
            <div className="w-12 h-12 bg-emerald-50 text-emerald-600 rounded-xl flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition-transform">🧬</div>
            <h3 className="text-lg font-black text-slate-800 mb-2">IGCSE Khoa Học</h3>
            <p className="text-sm text-slate-500 font-medium mb-6 flex-1">Luyện đề các môn Khoa học, Toán học chuẩn Cambridge (Dạng bài thường).</p>
            <button 
              onClick={() => onStartTest('standard', {})}
              className="w-full bg-slate-100 hover:bg-[#1e88e5] text-slate-700 hover:text-white font-bold py-3 rounded-xl transition-colors"
            >
              Vào phòng thi
            </button>
          </div>

          {/* Card 3: NÚT MỚI - CASE STUDY (SPLIT SCREEN) */}
          <div className="bg-white border-2 border-[#1e88e5]/20 rounded-2xl p-6 shadow-sm hover:shadow-xl hover:border-[#1e88e5] transition-all group flex flex-col relative overflow-hidden">
            <div className="absolute top-0 right-0 bg-orange-500 text-white text-[10px] font-black px-3 py-1 rounded-bl-lg uppercase tracking-wider">Mới</div>
            <div className="w-12 h-12 bg-orange-50 text-orange-600 rounded-xl flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition-transform">💼</div>
            <h3 className="text-lg font-black text-slate-800 mb-2">IGCSE Business / Econ</h3>
            <p className="text-sm text-slate-500 font-medium mb-6 flex-1">Làm bài luận và phân tích Case Study với giao diện chia đôi màn hình siêu việt.</p>
            <button 
              onClick={() => onNavigate('split-screen')}
              className="w-full bg-[#0a5482] hover:bg-[#084266] text-white font-bold py-3 rounded-xl transition-colors shadow-md active:scale-95"
            >
              Vào phòng thi ➜
            </button>
          </div>

        </div>
      </main>
    </div>
  );
}