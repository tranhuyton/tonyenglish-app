import React, { useState } from 'react';
import { supabase } from './supabase';

interface ResetPasswordModalProps {
  isOpen: boolean;
  onClose: () => void;
  onNavigate?: (view: string) => void;
}

export default function ResetPasswordModal({ isOpen, onClose, onNavigate }: ResetPasswordModalProps) {
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');
  const [isSuccess, setIsSuccess] = useState(false);

  if (!isOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMsg('');

    if (password.length < 6) {
      setErrorMsg('Mật khẩu mới phải có tối thiểu 6 ký tự!');
      return;
    }

    if (password !== confirmPassword) {
      setErrorMsg('Mật khẩu xác nhận không khớp với mật khẩu mới!');
      return;
    }

    setLoading(true);
    try {
      const { error } = await supabase.auth.updateUser({ password });
      if (error) throw error;

      setIsSuccess(true);
      // Xóa URL hash/params chứa token recovery để URL sạch sẽ
      try {
        window.history.replaceState(null, '', window.location.pathname);
      } catch (err) {}
    } catch (err: any) {
      setErrorMsg(err.message || 'Đã có lỗi xảy ra khi cập nhật mật khẩu.');
    } finally {
      setLoading(false);
    }
  };

  const handleFinish = () => {
    onClose();
    if (onNavigate) {
      onNavigate('portal');
    }
  };

  return (
    <div className="fixed inset-0 bg-slate-900/70 backdrop-blur-md z-[120] flex items-center justify-center p-4 animate-in fade-in duration-300">
      <div className="bg-white rounded-[2rem] w-full max-w-md shadow-2xl overflow-hidden border border-slate-100 animate-in zoom-in-95 duration-200">
        
        {/* Header */}
        <div className="bg-gradient-to-r from-[#0a5482] to-[#0ea5e9] p-7 text-white text-center relative">
          <div className="w-14 h-14 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center mx-auto mb-3 shadow-inner text-2xl border border-white/20">
            🔐
          </div>
          <h2 className="text-2xl font-black tracking-tight">Đặt Lại Mật Khẩu Mới</h2>
          <p className="text-sky-100 text-[13px] font-medium mt-1">
            Thiết lập mật khẩu an toàn cho tài khoản của bạn
          </p>
        </div>

        {/* Body */}
        <div className="p-7">
          {isSuccess ? (
            <div className="text-center py-4 space-y-4 animate-in fade-in">
              <div className="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto text-3xl shadow-sm">
                ✓
              </div>
              <h3 className="text-xl font-black text-slate-800">Thành Công!</h3>
              <p className="text-slate-600 text-[14px] leading-relaxed">
                Mật khẩu của bạn đã được cập nhật thành công. Bạn có thể sử dụng mật khẩu này cho các lần đăng nhập tiếp theo.
              </p>
              <button
                type="button"
                onClick={handleFinish}
                className="w-full bg-[#0a5482] hover:bg-[#084266] text-white font-black py-4 rounded-xl shadow-lg shadow-sky-900/20 transition-all active:scale-95 text-[15px] mt-2"
              >
                Vào Lớp Học Ngay ➜
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-5">
              {errorMsg && (
                <div className="p-3.5 bg-rose-50 border border-rose-200 rounded-xl text-rose-700 text-[13px] font-bold flex items-center gap-2 animate-in shake">
                  <span>⚠️</span>
                  <span>{errorMsg}</span>
                </div>
              )}

              {/* Mật khẩu mới */}
              <div className="space-y-1.5">
                <label className="text-[12px] font-bold text-slate-600 uppercase tracking-wider block">
                  Mật khẩu mới
                </label>
                <div className="relative">
                  <input
                    type={showPassword ? 'text' : 'password'}
                    required
                    minLength={6}
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Tối thiểu 6 ký tự..."
                    className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-3.5 pr-12 text-[14px] font-medium outline-none focus:border-[#0ea5e9] focus:bg-white focus:ring-4 focus:ring-sky-100 transition-all"
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 p-1"
                  >
                    {showPassword ? (
                      <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l18 18" />
                      </svg>
                    ) : (
                      <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                      </svg>
                    )}
                  </button>
                </div>
              </div>

              {/* Xác nhận mật khẩu mới */}
              <div className="space-y-1.5">
                <label className="text-[12px] font-bold text-slate-600 uppercase tracking-wider block">
                  Xác nhận mật khẩu mới
                </label>
                <div className="relative">
                  <input
                    type={showConfirm ? 'text' : 'password'}
                    required
                    minLength={6}
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    placeholder="Nhập lại mật khẩu..."
                    className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-3.5 pr-12 text-[14px] font-medium outline-none focus:border-[#0ea5e9] focus:bg-white focus:ring-4 focus:ring-sky-100 transition-all"
                  />
                  <button
                    type="button"
                    onClick={() => setShowConfirm(!showConfirm)}
                    className="absolute right-3.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 p-1"
                  >
                    {showConfirm ? (
                      <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l18 18" />
                      </svg>
                    ) : (
                      <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                      </svg>
                    )}
                  </button>
                </div>
              </div>

              {/* Password strength tips */}
              <div className="text-[12px] text-slate-500 bg-slate-50 p-3 rounded-xl border border-slate-100 flex items-center gap-2">
                <span className="text-base">💡</span>
                <span>Mật khẩu nên kết hợp chữ hoa, chữ thường và số để tăng độ an toàn.</span>
              </div>

              <button
                type="submit"
                disabled={loading}
                className="w-full bg-[#0a5482] hover:bg-[#084266] disabled:bg-slate-300 text-white font-black py-4 rounded-xl shadow-lg shadow-sky-900/20 transition-all active:scale-95 text-[15px] mt-2 flex items-center justify-center gap-2"
              >
                {loading ? (
                  <>
                    <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                    <span>ĐANG CẬP NHẬT...</span>
                  </>
                ) : (
                  'CẬP NHẬT MẬT KHẨU MỚI ➔'
                )}
              </button>
            </form>
          )}
        </div>
      </div>
    </div>
  );
}
