import React, { useState } from 'react';
import { supabase } from './supabase';

export default function AuthModal({ onClose, onNavigate }: { onClose?: () => void, onNavigate?: (view: string) => void }) {
  const [mode, setMode] = useState<'login' | 'forgot'>('login');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  // 🔐 Forgot password state
  const [resetEmail, setResetEmail] = useState('');
  const [isResetting, setIsResetting] = useState(false);
  const [resetSentSuccess, setResetSentSuccess] = useState(false);
  const [resetError, setResetError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      // Timeout 10 giây — nếu Supabase chậm thì báo lỗi thay vì treo vô hạn
      const loginPromise = supabase.auth.signInWithPassword({ email, password });
      const timeoutPromise = new Promise((_, reject) => 
        setTimeout(() => reject(new Error('TIMEOUT')), 10000)
      );
      
      const { data, error } = await Promise.race([loginPromise, timeoutPromise]) as any;
      if (error) throw error;
      
      if (data?.user) {
        const { data: profile } = await supabase.from('profiles').select('role, status').eq('id', data.user.id).single();
        if (profile?.role !== 'admin' && profile?.status === 'inactive') {
          await supabase.auth.signOut();
          alert("⛔ Tài khoản học của bạn hiện đang ở trạng thái TẠM DỪNG.\nVui lòng liên hệ trung tâm / quản trị viên để được hỗ trợ kích hoạt lại nhé!");
          return;
        }

        // 🚀 GHI LOG ĐĂNG NHẬP (fire-and-forget, không block login flow)
        supabase.from('activity_logs').insert([{
            user_id: data.user.id,
            action_type: 'login',
            details: { message: 'Đăng nhập vào hệ thống LMS' }
        }]).then(() => {});
      }
      
      if (typeof onClose === 'function') onClose();
      if (typeof onNavigate === 'function') {
        onNavigate('portal');
      } else {
        window.location.href = '/';
      }
    } catch (error: any) {
      if (error.message === 'TIMEOUT') {
        alert('⏳ Máy chủ đang phản hồi chậm. Vui lòng thử lại!');
      } else {
        alert(error.message === 'Invalid login credentials' ? 'Sai email hoặc mật khẩu!' : 'Lỗi: ' + error.message);
      }
    } finally {
      setLoading(false);
    }
  };

  const handleForgotPassword = async (e: React.FormEvent) => {
    e.preventDefault();
    const cleanEmail = resetEmail.trim().toLowerCase();
    if (!cleanEmail) return;
    setIsResetting(true);
    setResetError('');
    try {
      // 1. Kiểm tra email có thuộc danh sách tài khoản học viên / giáo viên TonyEnglish không
      const { data: profile } = await supabase
        .from('profiles')
        .select('id, email')
        .ilike('email', cleanEmail)
        .maybeSingle();

      if (!profile) {
        setResetError('Email này không tồn tại trong danh sách học viên của hệ thống TonyEnglish.');
        return;
      }

      // 2. Nếu có, tiến hành gửi email khôi phục mật khẩu
      const { error } = await supabase.auth.resetPasswordForEmail(cleanEmail, {
        redirectTo: `${window.location.origin}/`,
      });
      if (error) throw error;
      setResetSentSuccess(true);
    } catch (err: any) {
      setResetError(err.message || 'Không thể gửi email đặt lại mật khẩu. Vui lòng kiểm tra lại địa chỉ email.');
    } finally {
      setIsResetting(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[100] flex items-center justify-center p-4 animate-in fade-in">
      <div className="bg-white rounded-3xl w-full max-w-md shadow-2xl overflow-hidden animate-in zoom-in-95">
        <div className="p-8">
          <div className="flex justify-between items-center mb-6">
            <div className="flex items-center gap-3">
              {mode === 'forgot' && (
                <button
                  type="button"
                  onClick={() => { setMode('login'); setResetSentSuccess(false); setResetError(''); }}
                  className="w-8 h-8 rounded-full hover:bg-slate-100 text-slate-500 flex items-center justify-center transition-colors font-bold text-sm"
                  title="Quay lại đăng nhập"
                >
                  ←
                </button>
              )}
              <h2 className="text-2xl font-black text-[#0a5482] uppercase tracking-tight">
                {mode === 'login' ? 'Đăng nhập hệ thống' : 'Quên mật khẩu'}
              </h2>
            </div>
            {typeof onClose === 'function' && (
              <button onClick={onClose} className="text-slate-400 hover:text-red-500 text-2xl transition">&times;</button>
            )}
          </div>

          {mode === 'login' ? (
            <>
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
                  <div className="flex justify-between items-center mb-1">
                    <label className="text-[13px] font-bold text-slate-600 block">Mật khẩu</label>
                    <button
                      type="button"
                      onClick={() => {
                        setMode('forgot');
                        setResetEmail(email);
                        setResetSentSuccess(false);
                        setResetError('');
                      }}
                      className="text-[12px] font-bold text-[#0ea5e9] hover:underline"
                    >
                      Quên mật khẩu?
                    </button>
                  </div>
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
            </>
          ) : (
            <div>
              {resetSentSuccess ? (
                <div className="text-center py-4 space-y-4 animate-in fade-in">
                  <div className="w-16 h-16 bg-sky-100 text-[#0a5482] rounded-full flex items-center justify-center mx-auto text-3xl shadow-sm">
                    📧
                  </div>
                  <h3 className="text-xl font-black text-slate-800">Đã Gửi Email Khôi Phục!</h3>
                  <p className="text-slate-600 text-[14px] leading-relaxed">
                    Hệ thống đã gửi liên kết đặt lại mật khẩu đến: <br/>
                    <strong className="text-slate-800 font-bold">{resetEmail}</strong>
                  </p>
                  <p className="text-[12px] text-slate-500 bg-slate-50 p-3 rounded-xl border border-slate-200">
                    💡 Vui lòng mở hòm thư (kiểm tra cả mục <strong>Spam / Thư rác</strong>) và nhấn vào liên kết để tạo mật khẩu mới.
                  </p>
                  <button
                    type="button"
                    onClick={() => { setMode('login'); setResetSentSuccess(false); setResetError(''); }}
                    className="w-full bg-[#0a5482] hover:bg-[#084266] text-white font-black py-3.5 rounded-xl shadow-lg transition-all active:scale-95 text-[14px]"
                  >
                    ← Quay lại Đăng nhập
                  </button>
                </div>
              ) : (
                <form onSubmit={handleForgotPassword} className="space-y-5">
                  <p className="text-slate-600 text-[14px] leading-relaxed">
                    Nhập email đã đăng ký của bạn. Chúng tôi sẽ gửi một liên kết an toàn qua email để bạn đặt lại mật khẩu mới.
                  </p>

                  {resetError && (
                    <div className="p-3.5 bg-rose-50 border border-rose-200 rounded-xl text-rose-700 text-[13px] font-bold flex items-center gap-2">
                      <span>⚠️</span>
                      <span>{resetError}</span>
                    </div>
                  )}

                  <div>
                    <label className="text-[13px] font-bold text-slate-600 block mb-1">Email tài khoản</label>
                    <input 
                      type="email" 
                      required
                      placeholder="Ví dụ: hocvien@tonyenglish.vn" 
                      value={resetEmail}
                      onChange={(e) => setResetEmail(e.target.value)}
                      className="w-full bg-slate-50 border border-slate-200 rounded-xl p-3.5 text-[14px] outline-none focus:border-[#2bd6eb] focus:ring-1 focus:ring-[#2bd6eb] transition" 
                    />
                  </div>

                  <button 
                    type="submit" 
                    disabled={isResetting}
                    className="w-full bg-[#0a5482] hover:bg-[#084266] disabled:bg-slate-400 text-white font-black py-4 rounded-xl shadow-lg transition-transform active:scale-95 flex justify-center items-center gap-2 mt-4"
                  >
                    {isResetting ? (
                      <>
                        <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                        <span>ĐANG GỬI EMAIL...</span>
                      </>
                    ) : (
                      'GỬI LIÊN KẾT ĐẶT LẠI MẬT KHẨU ➔'
                    )}
                  </button>

                  <div className="text-center pt-2">
                    <button
                      type="button"
                      onClick={() => { setMode('login'); setResetError(''); }}
                      className="text-[13px] font-bold text-slate-500 hover:text-[#0a5482] transition-colors"
                    >
                      ← Quay lại Đăng nhập
                    </button>
                  </div>
                </form>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}