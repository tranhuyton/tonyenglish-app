import React, { useState } from 'react';
import { supabase } from './supabase';

export default function AuthModal({ onClose, onNavigate }: { onClose?: () => void, onNavigate?: (view: string) => void }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const { error } = await supabase.auth.signInWithPassword({ email, password });
      if (error) throw error;
      
      if (typeof onClose === 'function') onClose(); 
      if (typeof onNavigate === 'function') {
        onNavigate('student'); 
      } else {
        window.location.href = '/';
      }
    } catch (error: any) {
      alert(error.message === 'Invalid login credentials' ? 'Sai email hoặc mật khẩu!' : 'Lỗi: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[100] flex items-center justify-center p-4 animate-in fade-in">
      <div className="bg-white rounded-3xl w-full max-w-md shadow-2xl overflow-hidden animate-in zoom-in-95">
        <div className="p-8">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-black text-[#0a5482] uppercase tracking-tight">
              Đăng nhập hệ thống
            </h2>
            {typeof onClose === 'function' && (
              <button onClick={onClose} className="text-slate-400 hover:text-red-500 text-2xl transition">&times;</button>
            )}
          </div>

          <p className="text-slate-500 text-[13px] font-medium mb-6">
            Hệ thống chỉ dành cho học viên nội bộ. Nếu chưa có tài khoản, vui lòng liên hệ Admin để được cấp phát.
          </p>

          <form onSubmit={handleSubmit} className="space-y-5">
            <div>
              <label className="text-[13px] font-bold text-slate-600 block mb-1">Email</label>
              <input 
                type="email" 
                required
                value={email} 
                onChange={(e) => setEmail(e.target.value)}
                className="w-full bg-slate-50 border border-slate-200 rounded-xl p-3.5 text-[14px] outline-none focus:border-[#2bd6eb] focus:ring-1 focus:ring-[#2bd6eb] transition"
                placeholder="Ví dụ: hocvien@tonyenglish.vn"
              />
            </div>
            
            <div>
              <label className="text-[13px] font-bold text-slate-600 block mb-1">Mật khẩu</label>
              <input 
                type="password" 
                required
                value={password} 
                onChange={(e) => setPassword(e.target.value)}
                className="w-full bg-slate-50 border border-slate-200 rounded-xl p-3.5 text-[14px] outline-none focus:border-[#2bd6eb] focus:ring-1 focus:ring-[#2bd6eb] transition"
                placeholder="••••••••"
              />
            </div>

            <button 
              type="submit" 
              disabled={loading}
              className="w-full bg-[#0a5482] hover:bg-[#084266] text-white font-black py-4 rounded-xl shadow-lg transition active:scale-95 disabled:opacity-50 mt-2"
            >
              {loading ? '⏳ ĐANG XỬ LÝ...' : 'ĐĂNG NHẬP ➔'}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}