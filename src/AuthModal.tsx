import React, { useState } from 'react';
import { supabase } from './supabase';

export default function AuthModal({ onClose }: { onClose: () => void }) {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');

  const handleAuth = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setErrorMsg('');
    
    if (isLogin) {
      // Đăng nhập
      const { error } = await supabase.auth.signInWithPassword({ email, password });
      if (error) setErrorMsg("Đăng nhập thất bại: " + error.message);
      else onClose(); // Thành công thì đóng cửa sổ
    } else {
      // Đăng ký
      const { error } = await supabase.auth.signUp({ email, password });
      if (error) {
        setErrorMsg("Đăng ký thất bại: " + error.message);
      } else {
        alert("🎉 Đăng ký thành công! Hệ thống đang tự động đăng nhập...");
        await supabase.auth.signInWithPassword({ email, password });
        onClose();
      }
    }
    setLoading(false);
  };

  return (
    <div className="fixed inset-0 bg-gray-900/60 backdrop-blur-sm flex justify-center items-center z-50 p-4">
      <div className="bg-white rounded-2xl shadow-2xl max-w-md w-full p-8 relative overflow-hidden">
        <button onClick={onClose} className="absolute top-4 right-4 text-gray-400 hover:text-gray-700 text-2xl font-bold">&times;</button>
        <div className="text-center mb-8">
          <div className="w-16 h-16 bg-[#2b88c9] text-white rounded-2xl flex items-center justify-center text-3xl font-bold mx-auto mb-4 shadow-lg">🎓</div>
          <h2 className="text-2xl font-bold text-gray-800">{isLogin ? 'Đăng Nhập' : 'Tạo Tài Khoản'}</h2>
          <p className="text-gray-500 text-sm mt-2">Hệ thống Luyện thi EdTech</p>
        </div>

        {errorMsg && <div className="mb-4 p-3 bg-red-50 text-red-600 border border-red-200 rounded text-sm font-bold">{errorMsg}</div>}

        <form onSubmit={handleAuth} className="space-y-5">
          <div>
            <label className="block text-sm font-bold text-gray-700 mb-1">Email</label>
            <input type="email" required value={email} onChange={e => setEmail(e.target.value)} className="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#2b88c9] outline-none transition" placeholder="hocsinh@gmail.com" />
          </div>
          <div>
            <label className="block text-sm font-bold text-gray-700 mb-1">Mật khẩu</label>
            <input type="password" required minLength={6} value={password} onChange={e => setPassword(e.target.value)} className="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#2b88c9] outline-none transition" placeholder="Ít nhất 6 ký tự" />
          </div>
          <button disabled={loading} type="submit" className="w-full bg-[#2b88c9] hover:bg-[#1a6ea6] text-white font-bold py-3.5 rounded-lg transition shadow-md disabled:bg-gray-400">
            {loading ? 'Đang xử lý...' : (isLogin ? 'Đăng Nhập' : 'Đăng Ký')}
          </button>
        </form>

        <div className="mt-6 text-center text-sm text-gray-600 border-t border-gray-100 pt-6">
          {isLogin ? "Chưa có tài khoản? " : "Đã có tài khoản? "}
          <button type="button" onClick={() => { setIsLogin(!isLogin); setErrorMsg(''); }} className="text-[#2b88c9] font-bold hover:underline">
            {isLogin ? "Đăng ký tại đây" : "Đăng nhập ngay"}
          </button>
        </div>
      </div>
    </div>
  );
}