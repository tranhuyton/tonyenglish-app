import React, { useState } from 'react';
import { supabase } from './supabase';

export default function Home({ onNavigate, onStartTest }: { onNavigate: (view: string) => void, onStartTest: (type: string, data: any) => void }) {
  // STATE CHO FORM ĐĂNG NHẬP THẬT
  const [showLoginModal, setShowLoginModal] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Dữ liệu giả lập để test giao diện khi bấm vào thẻ bài thi mẫu
  const dummyIELTS = { title: "IELTS Simulation Demo", timeLimit: "60:00", parts: [] };
  const dummyStandard = { title: "IGCSE / TOEIC Standard Demo", timeLimit: "45:00", parts: [] };

  // --- HÀM XỬ LÝ ĐĂNG NHẬP THẬT BẰNG SUPABASE ---
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
        // Phân luồng thông minh
        if (email.toLowerCase().includes('admin')) {
          onNavigate('admin');
        } else {
          onNavigate('portal');
        }
      }
    } catch (err) {
      alert("Đã có lỗi xảy ra khi kết nối máy chủ.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-white font-sans text-slate-800 flex flex-col relative">
      
      {/* NAVBAR TRANG CHỦ */}
      <nav className="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
          {/* CẬP NHẬT: GẮN LINK TRANG CHỦ CHÍNH THỨC VÀO LOGO */}
          <div 
            className="flex items-center gap-3 cursor-pointer hover:opacity-80 transition-opacity"
            onClick={() => window.location.href = 'https://tonyenglish.vn/vi'}
            title="Về trang chủ TonyEnglish"
          >
            <img src="/logo-shield.png" alt="TonyEnglish" className="h-10 w-auto object-contain" />
            <div className="flex flex-col items-start leading-none">
              <div className="font-black text-[24px] tracking-tight mb-1">
                <span className="text-[#2ab4e8]">TONY</span><span className="text-[#0a5482]">ENGLISH</span>
              </div>
            </div>
          </div>

          <div className="flex items-center gap-4">
            <button className="text-[14px] font-bold text-slate-500 hover:text-[#0a5482] transition hidden sm:block">
              Dành cho Giáo viên
            </button>
            <button className="bg-slate-100 hover:bg-slate-200 text-slate-700 text-[14px] font-bold px-5 py-2.5 rounded-xl transition shadow-sm border border-slate-200">
              Góc Học Viên
            </button>
            <button 
              onClick={() => setShowLoginModal(true)} 
              className="bg-[#0a5482] hover:bg-[#084266] text-white text-[14px] font-bold px-6 py-2.5 rounded-xl transition shadow-lg shadow-blue-900/20 active:scale-95"
            >
              Đăng Nhập
            </button>
          </div>
        </div>
      </nav>

      <main className="flex-1">
        {/* HERO SECTION */}
        <section className="relative overflow-hidden bg-slate-50 pt-20 pb-28">
          <div className="absolute inset-0 bg-[url('https://placehold.co/1920x1080/f8fafc/e2e8f0?text=Pattern')] opacity-50 bg-cover bg-center"></div>
          <div className="max-w-7xl mx-auto px-6 relative z-10 text-center">
            <div className="inline-block bg-blue-100 text-[#0a5482] font-black text-[13px] px-4 py-1.5 rounded-full uppercase tracking-wider mb-6 shadow-sm border border-blue-200">
              The future begins here
            </div>
            <h1 className="text-5xl md:text-7xl font-black text-slate-800 tracking-tight leading-tight mb-8 max-w-4xl mx-auto">
              Nền tảng luyện thi <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#2ab4e8] to-[#0a5482]">thông minh</span> thế hệ mới
            </h1>
            <p className="text-lg md:text-xl text-slate-600 font-medium max-w-2xl mx-auto mb-10 leading-relaxed">
              Trải nghiệm môi trường thi sát thực tế 100%. Tích hợp AI phân tích điểm mạnh yếu, chấm chữa chuyên sâu. Lộ trình cá nhân hóa từ IELTS đến các môn khoa học chuẩn quốc tế.
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <button onClick={() => document.getElementById('demo-section')?.scrollIntoView({ behavior: 'smooth' })} className="bg-[#2ab4e8] hover:bg-[#1d9ad1] text-white text-[16px] font-bold px-8 py-4 rounded-xl transition shadow-xl shadow-cyan-500/30 w-full sm:w-auto active:scale-95">
                Làm bài test năng lực ➜
              </button>
              <button onClick={() => setShowLoginModal(true)} className="bg-white hover:bg-slate-50 text-slate-700 text-[16px] font-bold px-8 py-4 rounded-xl transition shadow-md border border-slate-200 w-full sm:w-auto active:scale-95">
                Tìm hiểu khóa học
              </button>
            </div>
          </div>
        </section>

        {/* TÍNH NĂNG NỔI BẬT */}
        <section className="py-24 bg-white">
          <div className="max-w-7xl mx-auto px-6">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-black text-slate-800 mb-4">Tại sao chọn hệ thống của chúng tôi?</h2>
              <div className="w-20 h-1.5 bg-[#2ab4e8] mx-auto rounded-full"></div>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
              <div className="bg-slate-50 rounded-3xl p-8 border border-slate-100 hover:shadow-xl transition-shadow duration-300 cursor-default">
                <div className="w-16 h-16 rounded-2xl bg-blue-100 flex items-center justify-center text-3xl mb-6 shadow-inner">💻</div>
                <h3 className="text-xl font-black text-slate-800 mb-3">Giao diện thi chuẩn IDP/BC</h3>
                <p className="text-slate-600 leading-relaxed font-medium">Hệ thống mô phỏng bài thi trên máy tính chân thực nhất. Hỗ trợ đầy đủ công cụ Highlight, Take Notes, Copy/Paste giúp bạn không bỡ ngỡ khi bước vào phòng thi thật.</p>
              </div>
              <div className="bg-slate-50 rounded-3xl p-8 border border-slate-100 hover:shadow-xl transition-shadow duration-300 cursor-default">
                <div className="w-16 h-16 rounded-2xl bg-purple-100 flex items-center justify-center text-3xl mb-6 shadow-inner">🤖</div>
                <h3 className="text-xl font-black text-slate-800 mb-3">AI Chấm chữa chuyên sâu</h3>
                <p className="text-slate-600 leading-relaxed font-medium">Tự động chấm điểm và phân tích biểu đồ năng lực qua từng dạng bài. Đưa ra gợi ý cải thiện kỹ năng ngay lập tức giúp tối ưu hóa thời gian ôn luyện.</p>
              </div>
              <div className="bg-slate-50 rounded-3xl p-8 border border-slate-100 hover:shadow-xl transition-shadow duration-300 cursor-default">
                <div className="w-16 h-16 rounded-2xl bg-emerald-100 flex items-center justify-center text-3xl mb-6 shadow-inner">📚</div>
                <h3 className="text-xl font-black text-slate-800 mb-3">Hệ sinh thái đa môn học</h3>
                <p className="text-slate-600 leading-relaxed font-medium">Không chỉ IELTS, hệ thống hỗ trợ ôn luyện đa dạng các chứng chỉ và môn học chuẩn quốc tế, đáp ứng mọi nhu cầu củng cố kiến thức khoa học và ngoại ngữ.</p>
              </div>
            </div>
          </div>
        </section>

        {/* DEMO THI THỬ */}
        <section id="demo-section" className="py-24 bg-[#0a5482] text-white">
          <div className="max-w-5xl mx-auto px-6 text-center">
            <h2 className="text-3xl md:text-4xl font-black mb-6">Trải nghiệm không gian thi mô phỏng</h2>
            <p className="text-blue-100 font-medium mb-12 text-lg max-w-2xl mx-auto">Bạn không cần tài khoản để thử sức. Hãy chọn một giao diện bài thi mẫu bên dưới để xem hệ thống hoạt động mượt mà như thế nào.</p>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 text-left">
              {/* Card Demo 1 */}
              <div 
                onClick={() => onStartTest('computer', dummyIELTS)}
                className="bg-white/10 backdrop-blur-sm border border-white/20 rounded-3xl p-8 cursor-pointer hover:bg-white/20 transition-all group"
              >
                <div className="flex justify-between items-start mb-6">
                  <div className="w-14 h-14 rounded-full bg-[#2ab4e8] flex items-center justify-center text-2xl shadow-lg">🎧</div>
                  <span className="bg-white text-[#0a5482] font-black text-xs px-3 py-1 rounded-full uppercase">Demo Free</span>
                </div>
                <h3 className="text-2xl font-black mb-2 group-hover:text-[#2ab4e8] transition-colors">IELTS Computer-Delivered</h3>
                <p className="text-blue-100/80 font-medium mb-6">Trải nghiệm giao diện chia đôi màn hình, tự động chạy Audio và công cụ ghi chú y hệt IDP/BC.</p>
                <div className="font-bold text-[#2ab4e8] flex items-center gap-2 group-hover:gap-4 transition-all">Làm thử ngay <span>➜</span></div>
              </div>

              {/* Card Demo 2 */}
              <div 
                onClick={() => onStartTest('standard', dummyStandard)}
                className="bg-white/10 backdrop-blur-sm border border-white/20 rounded-3xl p-8 cursor-pointer hover:bg-white/20 transition-all group"
              >
                <div className="flex justify-between items-start mb-6">
                  <div className="w-14 h-14 rounded-full bg-emerald-500 flex items-center justify-center text-2xl shadow-lg">🧬</div>
                  <span className="bg-white text-[#0a5482] font-black text-xs px-3 py-1 rounded-full uppercase">Demo Free</span>
                </div>
                <h3 className="text-2xl font-black mb-2 group-hover:text-emerald-400 transition-colors">Standard Interface</h3>
                <p className="text-blue-100/80 font-medium mb-6">Giao diện dạng thẻ (card) trực quan, bảng điều hướng thông minh. Phù hợp luyện đề TOEIC, IGCSE.</p>
                <div className="font-bold text-emerald-400 flex items-center gap-2 group-hover:gap-4 transition-all">Làm thử ngay <span>➜</span></div>
              </div>
            </div>
          </div>
        </section>

      </main>

      {/* FOOTER */}
      <footer className="bg-slate-900 text-slate-400 py-12 border-t border-slate-800">
        <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-6">
          <div className="flex items-center gap-3 opacity-50 grayscale hover:grayscale-0 transition-all cursor-pointer" onClick={() => window.location.href = 'https://tonyenglish.vn/vi'}>
             <img src="/logo-shield.png" alt="TonyEnglish" className="h-8 w-auto object-contain" />
             <div className="font-black text-xl tracking-tight text-white">TONYENGLISH</div>
          </div>
          <div className="text-sm font-medium text-center md:text-right">
            <p>© 2026 TonyEnglish.vn - The future begins here.</p>
            <p className="mt-1">Nền tảng luyện thi và giáo dục trực tuyến.</p>
          </div>
        </div>
      </footer>

      {/* MODAL ĐĂNG NHẬP */}
      {showLoginModal && (
        <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl w-full max-w-md shadow-2xl overflow-hidden animate-in zoom-in-95">
            
            <div className="bg-[#f8fafc] px-8 py-6 border-b border-slate-200 flex justify-between items-center">
              <h2 className="text-2xl font-black text-slate-800">Đăng Nhập</h2>
              <button onClick={() => setShowLoginModal(false)} className="text-slate-400 hover:text-red-500 text-2xl font-bold transition-colors">&times;</button>
            </div>

            <form onSubmit={handleLogin} className="p-8 space-y-6">
              <div className="space-y-2">
                <label className="text-[13px] font-bold text-slate-500 uppercase tracking-widest">Email</label>
                <input 
                  type="email" 
                  required
                  placeholder="Nhập email của bạn..." 
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#1e88e5] text-[15px] font-medium transition-shadow bg-white" 
                />
              </div>

              <div className="space-y-2">
                <div className="flex justify-between items-center">
                  <label className="text-[13px] font-bold text-slate-500 uppercase tracking-widest">Mật khẩu</label>
                  <a href="#" className="text-[12px] font-bold text-[#1e88e5] hover:underline">Quên mật khẩu?</a>
                </div>
                <input 
                  type="password" 
                  required
                  placeholder="••••••••" 
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#1e88e5] text-[15px] font-medium transition-shadow bg-white" 
                />
              </div>

              <button 
                type="submit" 
                disabled={isLoading}
                className="w-full bg-[#0a5482] hover:bg-[#084266] disabled:bg-slate-400 text-white font-black py-4 rounded-xl shadow-lg transition-transform active:scale-95 flex justify-center items-center gap-2 mt-4"
              >
                {isLoading ? '⏳ ĐANG XỬ LÝ...' : 'ĐĂNG NHẬP HỆ THỐNG ➜'}
              </button>

              <div className="text-center mt-6 pt-6 border-t border-slate-100">
                <p className="text-[12px] text-slate-400 font-medium">Bạn chưa có tài khoản? <a href="#" className="text-[#1e88e5] font-bold hover:underline">Đăng ký ngay</a></p>
              </div>
            </form>
          </div>
        </div>
      )}

    </div>
  );
}