import React, { useState } from 'react';
import { supabase } from './supabase';

export default function AdminLogin({ onLoginSuccess }: { onLoginSuccess: () => void }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      const { data, error } = await supabase.auth.signInWithPassword({
        email: email,
        password: password,
      });

      if (error) {
        alert("Đăng nhập thất bại! Vui lòng kiểm tra lại Email hoặc Mật khẩu.");
      } else if (data.user) {
        // Có thể thêm bước check xem email có chữ admin không nếu muốn bảo mật thêm
        if (email.toLowerCase().includes('admin')) {
          onLoginSuccess();
        } else {
          alert("Tài khoản này không có quyền truy cập trang Quản trị!");
          await supabase.auth.signOut();
        }
      }
    } catch (err) {
      alert("Đã có lỗi xảy ra khi kết nối máy chủ.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 flex items-center justify-center p-4 font-sans relative overflow-hidden">
      {/* Background pattern */}
      <div className="absolute inset-0 bg-[url('https://placehold.co/1920x1080/0f172a/1e293b?text=+')] opacity-20 bg-cover bg-center"></div>
      
      <div className="bg-white rounded-[2rem] w-full max-w-md shadow-2xl overflow-hidden relative z-10 animate-in fade-in zoom-in-95 duration-500">
        <div className="bg-[#0a5482] px-8 py-10 text-center relative overflow-hidden">
          <div className="absolute top-0 right-0 w-32 h-32 bg-blue-400 opacity-20 rounded-full blur-3xl -mr-10 -mt-10"></div>
          <div className="w-16 h-16 bg-white rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg">
            <span className="text-3xl">🛡️</span>
          </div>
          <h2 className="text-2xl font-black text-white tracking-tight">HỆ THỐNG QUẢN TRỊ</h2>
          <p className="text-blue-100/80 font-medium text-[13px] mt-1">Dành riêng cho Giáo viên TonyEnglish</p>
        </div>

        <form onSubmit={handleLogin} className="p-8 space-y-6">
          <div className="space-y-2">
            <label className="text-[12px] font-black text-slate-500 uppercase tracking-widest">Email Quản trị</label>
            <input 
              type="email" 
              required
              placeholder="admin@tonyenglish.vn" 
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full border-2 border-slate-200 rounded-xl px-4 py-3.5 outline-none focus:border-[#0a5482] focus:ring-4 focus:ring-blue-900/10 text-[15px] font-bold text-slate-700 transition-all bg-slate-50 focus:bg-white" 
            />
          </div>

          <div className="space-y-2">
            <label className="text-[12px] font-black text-slate-500 uppercase tracking-widest">Mật mã truy cập</label>
            <input 
              type="password" 
              required
              placeholder="••••••••" 
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full border-2 border-slate-200 rounded-xl px-4 py-3.5 outline-none focus:border-[#0a5482] focus:ring-4 focus:ring-blue-900/10 text-[15px] font-bold text-slate-700 transition-all bg-slate-50 focus:bg-white" 
            />
          </div>

          <button 
            type="submit" 
            disabled={isLoading}
            className="w-full bg-[#0a5482] hover:bg-[#084266] disabled:bg-slate-400 text-white font-black py-4 rounded-xl shadow-xl shadow-[#0a5482]/20 transition-all active:scale-95 flex justify-center items-center gap-2 mt-4"
          >
            {isLoading ? '⏳ ĐANG XÁC THỰC...' : 'TRUY CẬP HỆ THỐNG ➜'}
          </button>
        </form>
      </div>
    </div>
  );
}