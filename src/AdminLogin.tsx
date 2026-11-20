import React, { useState } from 'react';
import { supabase } from './supabase';

export default function AdminLogin({ onLoginSuccess }: { onLoginSuccess: () => void }) {
  const [isLoading, setIsLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [showPassword, setShowPassword] = useState(false);

  const handleLogin = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setErrorMsg(null);
    setIsLoading(true);

    const formData = new FormData(e.currentTarget);
    const email = (formData.get('email') as string || '').trim();
    const password = formData.get('password') as string;

    try {
      const { data, error } = await supabase.auth.signInWithPassword({
        email: email,
        password: password,
      });

      if (error) {
        setErrorMsg("Đăng nhập thất bại! Vui lòng kiểm tra lại Email hoặc Mật khẩu.");
      } else if (data.user) {
        if (email.toLowerCase().includes('admin')) {
          onLoginSuccess();
        } else {
          setErrorMsg("Tài khoản này không có quyền truy cập trang Quản trị!");
          await supabase.auth.signOut();
        }
      }
    } catch (err) {
      setErrorMsg("Đã có lỗi xảy ra khi kết nối máy chủ. Vui lòng thử lại.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#071f33] via-[#0f172a] to-[#0a3d5c] flex items-center justify-center p-4 font-sans relative overflow-hidden">
      <div className="absolute -top-32 -right-32 w-96 h-96 bg-[#2ab4e8]/20 blur-3xl rounded-full pointer-events-none" />
      <div className="absolute -bottom-32 -left-32 w-96 h-96 bg-[#0a5482]/35 blur-3xl rounded-full pointer-events-none" />
      
      <div className="bg-white rounded-3xl w-full max-w-md shadow-2xl border border-white/10 overflow-hidden relative z-10 animate-in fade-in zoom-in-95 duration-500 transform-gpu">
        <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-8 py-9 text-center relative overflow-hidden">
          <div className="absolute top-0 right-0 w-40 h-40 bg-gradient-to-bl from-[#2ab4e8]/30 to-transparent rounded-full -mr-12 -mt-12 pointer-events-none"></div>
          <div className="w-16 h-16 bg-white/95 rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg relative z-10 p-2.5">
            <img src="/logo-shield.png" alt="TonyEnglish Admin" className="w-full h-full object-contain" />
          </div>
          <h2 className="text-2xl font-black text-white tracking-tight relative z-10">HỆ THỐNG QUẢN TRỊ</h2>
          <p className="text-sky-200/90 font-medium text-[13px] mt-1 relative z-10">Dành riêng cho Giáo viên TonyEnglish</p>
        </div>

        <form onSubmit={handleLogin} className="p-7 sm:p-8 space-y-5">
          {errorMsg && (
            <div className="p-3.5 rounded-xl bg-rose-50 border border-rose-200 text-rose-700 text-xs font-bold leading-relaxed flex items-start gap-2">
              <span className="shrink-0">⚠️</span>
              <span>{errorMsg}</span>
            </div>
          )}

          <div className="space-y-1.5">
            <label className="text-[11.5px] font-black text-slate-500 uppercase tracking-widest">Email Quản trị</label>
            <input 
              name="email"
              type="email" 
              required
              autoComplete="email"
              defaultValue=""
              placeholder="admin@tonyenglish.vn" 
              className="w-full border-2 border-slate-200 rounded-xl px-4 py-3 outline-none focus:border-[#0a5482] focus:ring-4 focus:ring-[#2ab4e8]/15 text-[15px] font-bold text-slate-700 transition-all bg-slate-50 focus:bg-white" 
            />
          </div>

          <div className="space-y-1.5">
            <label className="text-[11.5px] font-black text-slate-500 uppercase tracking-widest">Mật mã truy cập</label>
            <div className="relative">
              <input 
                name="password"
                type={showPassword ? 'text' : 'password'} 
                required
                autoComplete="current-password"
                defaultValue=""
                placeholder="••••••••" 
                className="w-full border-2 border-slate-200 rounded-xl pl-4 pr-16 py-3 outline-none focus:border-[#0a5482] focus:ring-4 focus:ring-[#2ab4e8]/15 text-[15px] font-bold text-slate-700 transition-all bg-slate-50 focus:bg-white" 
              />
              <button
                type="button"
                onClick={() => setShowPassword((prev) => !prev)}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-xs font-extrabold text-slate-500 hover:text-[#0a5482] px-2 py-1 rounded-lg hover:bg-slate-100 transition cursor-pointer"
              >
                {showPassword ? 'Ẩn' : 'Hiện'}
              </button>
            </div>
          </div>

          <button 
            type="submit" 
            disabled={isLoading}
            className="w-full bg-[#0a5482] hover:bg-[#084266] disabled:bg-slate-400 text-white font-black py-3.5 rounded-xl shadow-xl shadow-[#0a5482]/20 transition-all active:scale-95 flex justify-center items-center gap-2 mt-2 cursor-pointer"
          >
            {isLoading ? '⏳ ĐANG XÁC THỰC...' : 'TRUY CẬP HỆ THỐNG ➜'}
          </button>

          <div className="pt-2 text-center border-t border-slate-100">
            <a
              href="/"
              className="inline-flex items-center gap-1.5 text-xs font-bold text-slate-500 hover:text-[#0a5482] transition-colors py-1"
            >
              <span>← Quay về trang chủ TonyEnglish.vn</span>
            </a>
          </div>
        </form>
      </div>
    </div>
  );
}