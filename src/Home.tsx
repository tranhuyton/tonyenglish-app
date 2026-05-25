import React, { useState, useEffect } from 'react';
import { supabase } from './supabase';

export default function Home({ 
    onNavigate, 
    onStartTest 
}: { 
    onNavigate: (view: string) => void, 
    onStartTest: (type: string, data: any) => void 
}) {
  const [showLoginModal, setShowLoginModal] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  
  const [currentUserRole, setCurrentUserRole] = useState<string | null>(null);

  const dummyIELTS = { title: "IELTS Simulation Demo", timeLimit: "60:00", parts: [] };
  const dummyStandard = { title: "IGCSE / TOEIC Standard Demo", timeLimit: "45:00", parts: [] };

  useEffect(() => {
    checkActiveSession();
  }, []);

  const checkActiveSession = async () => {
    const { data: { user } } = await supabase.auth.getUser();
    if (user) {
      const { data: profile } = await supabase.from('profiles').select('role').eq('id', user.id).single();
      if (profile) setCurrentUserRole(profile.role);
    }
  };

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      const { data, error } = await supabase.auth.signInWithPassword({ email, password });
      
      if (error) {
        alert("Đăng nhập thất bại! Vui lòng kiểm tra lại Email hoặc Mật khẩu.");
      } else if (data.user) {
        const { data: profile } = await supabase.from('profiles').select('role').eq('id', data.user.id).single();
        
        setShowLoginModal(false);
        if (profile?.role === 'admin') {
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
    <div className="min-h-[100dvh] bg-slate-50 font-sans text-slate-800 flex flex-col relative selection:bg-[#0ea5e9]/30">
      
      {/* 🚀 NAVBAR TRANG CHỦ (Glassmorphism) */}
      <nav className="fixed top-0 w-full bg-white/80 backdrop-blur-md border-b border-slate-200/80 z-50 transition-all duration-300">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 h-16 md:h-20 flex items-center justify-between">
          
          <div 
            className="flex items-center gap-2 sm:gap-3 cursor-pointer hover:opacity-80 transition-opacity"
            onClick={() => window.open('https://tonyenglish.vn/vi', '_blank')}
            title="Về trang chủ TonyEnglish"
          >
            <div className="w-9 h-9 md:w-11 md:h-11 flex items-center justify-center overflow-hidden shrink-0">
                <img src="/logo-shield.png" alt="TonyEnglish Logo" className="w-auto h-full object-contain" />
            </div>
            <div className="flex flex-col items-start leading-none mt-1">
              <div className="font-black text-[18px] md:text-[22px] tracking-tight">
                <span className="text-[#0ea5e9]">TONY</span><span className="text-slate-800">ENGLISH</span>
              </div>
            </div>
          </div>

          <div className="flex items-center gap-2 md:gap-4 shrink-0">
            {!currentUserRole ? (
              <button 
                onClick={() => setShowLoginModal(true)} 
                className="bg-slate-900 hover:bg-black text-white text-[13px] md:text-[14px] font-bold px-5 py-2 md:px-6 md:py-2.5 rounded-full transition-all shadow-md active:scale-95 whitespace-nowrap"
              >
                Đăng nhập
              </button>
            ) : (
              <>
                {currentUserRole === 'admin' && (
                  <button 
                    onClick={() => onNavigate('portal')} 
                    className="bg-emerald-50 hover:bg-emerald-100 text-emerald-600 text-[12px] md:text-[13px] font-bold uppercase tracking-widest px-4 py-2 md:px-5 md:py-2.5 rounded-full transition-all border border-emerald-200 shadow-sm active:scale-95 whitespace-nowrap"
                  >
                    <span className="md:hidden">Thi thử</span>
                    <span className="hidden md:inline">Góc Học Viên</span>
                  </button>
                )}
                
                <button 
                  onClick={() => currentUserRole === 'admin' ? onNavigate('admin') : onNavigate('portal')} 
                  className="bg-[#0ea5e9] hover:bg-[#0284c7] text-white text-[13px] md:text-[14px] font-bold px-5 py-2 md:px-6 md:py-2.5 rounded-full transition-all shadow-[0_4px_14px_rgba(14,165,233,0.4)] active:scale-95 whitespace-nowrap flex items-center gap-2"
                >
                  {currentUserRole === 'admin' ? 'Quản Trị' : 'Vào Lớp Học'} 
                  <span className="hidden sm:inline">➜</span>
                </button>
              </>
            )}
          </div>
        </div>
      </nav>

      <main className="flex-1 flex flex-col pt-16 md:pt-20">
        
        {/* 🚀 HERO SECTION (Modern EdTech / AI Theme) */}
        <section className="relative overflow-hidden bg-white pt-20 pb-28 md:pt-32 md:pb-40 border-b border-slate-100">
          
          {/* Background Elements */}
          <div className="absolute inset-0 bg-[url('/chat-pattern.png')] bg-repeat bg-[length:300px] opacity-[0.03]"></div>
          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-[#0ea5e9]/20 blur-[120px] rounded-full pointer-events-none"></div>
          
          <div className="max-w-7xl mx-auto px-6 relative z-10 text-center flex flex-col items-center">
            
            <div className="inline-flex items-center gap-2 bg-sky-50 text-[#0ea5e9] font-bold text-[11px] md:text-[12px] px-4 py-1.5 rounded-full uppercase tracking-widest mb-8 shadow-sm border border-sky-100 animate-in slide-in-from-bottom-4 duration-500">
              <span className="w-2 h-2 rounded-full bg-[#0ea5e9] animate-pulse"></span>
              The future begins here
            </div>
            
            <h1 className="text-4xl md:text-6xl lg:text-7xl font-black text-slate-800 tracking-tight leading-[1.25] md:leading-[1.3] pb-2 mb-6 max-w-4xl mx-auto animate-in slide-in-from-bottom-6 duration-700">
              Nền tảng luyện thi <br className="hidden md:block" />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#0ea5e9] to-indigo-600">thông minh thế hệ mới</span>
            </h1>
            
            <p className="text-[16px] md:text-xl text-slate-500 font-medium max-w-2xl mx-auto mb-10 leading-relaxed animate-in slide-in-from-bottom-8 duration-700 delay-100">
              Trải nghiệm môi trường thi sát thực tế 100%. Tích hợp AI phân tích điểm mạnh yếu, chấm chữa chuyên sâu. Lộ trình cá nhân hóa từ IELTS đến các môn IGCSE quốc tế.
            </p>
            
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4 w-full sm:w-auto animate-in slide-in-from-bottom-10 duration-700 delay-200">
              {currentUserRole === 'admin' ? (
                <>
                  <button 
                      onClick={() => onNavigate('admin')} 
                      className="bg-slate-900 hover:bg-black text-white text-[15px] font-bold px-8 py-4 rounded-full transition-all shadow-[0_8px_20px_rgba(0,0,0,0.2)] w-full sm:w-auto active:scale-95 flex items-center justify-center gap-2"
                  >
                    Vào Trang Quản Trị ➜
                  </button>
                  <button 
                      onClick={() => onNavigate('portal')} 
                      className="bg-white hover:bg-slate-50 text-slate-700 text-[15px] font-bold px-8 py-4 rounded-full transition-all shadow-sm border border-slate-200 w-full sm:w-auto active:scale-95 flex items-center justify-center gap-2"
                  >
                    Vào Góc Học Viên ➜
                  </button>
                </>
              ) : currentUserRole === 'student' ? (
                <>
                  <button 
                      onClick={() => document.getElementById('demo-section')?.scrollIntoView({ behavior: 'smooth' })} 
                      className="bg-slate-900 hover:bg-black text-white text-[15px] font-bold px-8 py-4 rounded-full transition-all shadow-[0_8px_20px_rgba(0,0,0,0.2)] w-full sm:w-auto active:scale-95 flex items-center justify-center gap-2"
                  >
                    Làm bài test năng lực ➜
                  </button>
                  <button 
                      onClick={() => onNavigate('portal')} 
                      className="bg-white hover:bg-slate-50 text-slate-700 text-[15px] font-bold px-8 py-4 rounded-full transition-all shadow-sm border border-slate-200 w-full sm:w-auto active:scale-95 flex items-center justify-center gap-2"
                  >
                    Vào Lớp Học ➜
                  </button>
                </>
              ) : (
                <>
                  <button 
                      onClick={() => document.getElementById('demo-section')?.scrollIntoView({ behavior: 'smooth' })} 
                      className="bg-[#0ea5e9] hover:bg-[#0284c7] text-white text-[15px] font-bold px-8 py-4 rounded-full transition-all shadow-[0_8px_20px_rgba(14,165,233,0.3)] w-full sm:w-auto active:scale-95 flex items-center justify-center gap-2"
                  >
                    Trải nghiệm thi thử miễn phí
                  </button>
                  <button 
                      onClick={() => setShowLoginModal(true)} 
                      className="bg-white hover:bg-slate-50 text-slate-700 text-[15px] font-bold px-8 py-4 rounded-full transition-all shadow-sm border border-slate-200 w-full sm:w-auto active:scale-95 flex items-center justify-center gap-2"
                  >
                    Tìm hiểu khóa học
                  </button>
                </>
              )}
            </div>
          </div>
        </section>

        {/* 🚀 TÍNH NĂNG NỔI BẬT */}
        <section className="py-24 bg-slate-50">
          <div className="max-w-7xl mx-auto px-6">
            <div className="text-center mb-16">
              <h2 className="text-3xl md:text-4xl font-black text-slate-800 mb-4 tracking-tight">Tại sao chọn hệ thống của chúng tôi?</h2>
              <div className="w-20 h-1.5 bg-[#0ea5e9] mx-auto rounded-full"></div>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-10">
              
              {/* Feature 1 */}
              <div className="bg-white rounded-[2rem] p-8 border border-slate-200 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 cursor-default group">
                <div className="w-16 h-16 rounded-2xl bg-blue-50 text-blue-500 flex items-center justify-center text-3xl mb-6 shadow-sm border border-blue-100 group-hover:scale-110 transition-transform">💻</div>
                <h3 className="text-xl font-black text-slate-800 mb-3 leading-snug">Giao diện thi chuẩn quốc tế</h3>
                <p className="text-slate-500 leading-relaxed font-medium">Hệ thống mô phỏng bài thi trên máy tính chân thực nhất. Hỗ trợ đầy đủ công cụ Highlight, Take Notes, Copy/Paste giúp bạn không bỡ ngỡ khi bước vào phòng thi thật.</p>
              </div>
              
              {/* Feature 2 */}
              <div className="bg-white rounded-[2rem] p-8 border border-slate-200 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 cursor-default group">
                <div className="w-16 h-16 rounded-2xl bg-purple-50 text-purple-500 flex items-center justify-center text-3xl mb-6 shadow-sm border border-purple-100 group-hover:scale-110 transition-transform">🤖</div>
                <h3 className="text-xl font-black text-slate-800 mb-3 leading-snug">AI chấm chữa chuyên sâu</h3>
                <p className="text-slate-500 leading-relaxed font-medium">Tự động chấm điểm và phân tích biểu đồ năng lực qua từng dạng bài. Đưa ra gợi ý cải thiện kỹ năng ngay lập tức giúp tối ưu hóa thời gian ôn luyện.</p>
              </div>
              
              {/* Feature 3 */}
              <div className="bg-white rounded-[2rem] p-8 border border-slate-200 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 cursor-default group">
                <div className="w-16 h-16 rounded-2xl bg-emerald-50 text-emerald-500 flex items-center justify-center text-3xl mb-6 shadow-sm border border-emerald-100 group-hover:scale-110 transition-transform">📚</div>
                <h3 className="text-xl font-black text-slate-800 mb-3 leading-snug">Hệ sinh thái đa môn học</h3>
                <p className="text-slate-500 leading-relaxed font-medium">Không chỉ IELTS, hệ thống hỗ trợ ôn luyện đa dạng các chứng chỉ và môn học chuẩn IGCSE, đáp ứng mọi nhu cầu củng cố kiến thức khoa học và ngoại ngữ.</p>
              </div>

            </div>
          </div>
        </section>

        {/* 🚀 DEMO THI THỬ (Dark Mode) */}
        <section id="demo-section" className="py-24 bg-slate-900 text-white relative overflow-hidden">
          
          <div className="absolute top-0 left-0 w-full h-full bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-indigo-900/40 via-slate-900 to-slate-900 pointer-events-none"></div>

          <div className="max-w-5xl mx-auto px-6 text-center relative z-10">
            <h2 className="text-3xl md:text-5xl font-black mb-6 tracking-tight">Trải nghiệm không gian thi mô phỏng</h2>
            <p className="text-slate-400 font-medium mb-12 text-[16px] md:text-lg max-w-2xl mx-auto">Bạn không cần tài khoản để thử sức. Hãy chọn một giao diện bài thi mẫu bên dưới để xem hệ thống hoạt động mượt mà như thế nào.</p>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 text-left">
              
              {/* Card Demo 1 */}
              <div 
                onClick={() => onStartTest('computer', dummyIELTS)}
                className="bg-white/5 backdrop-blur-md border border-white/10 rounded-[2rem] p-8 md:p-10 cursor-pointer hover:bg-white/10 hover:border-white/20 transition-all duration-300 group hover:-translate-y-1"
              >
                <div className="flex justify-between items-start mb-8">
                  <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-[#0ea5e9] to-indigo-500 flex items-center justify-center text-3xl shadow-lg border border-white/20 group-hover:scale-110 transition-transform">🎧</div>
                  <span className="bg-white/10 text-white font-bold text-[10px] px-3 py-1 rounded-full uppercase tracking-widest border border-white/5">Free Demo</span>
                </div>
                <h3 className="text-2xl font-black mb-3 text-white group-hover:text-[#0ea5e9] transition-colors leading-tight">IELTS Computer-Delivered</h3>
                <p className="text-slate-400 font-medium mb-8 leading-relaxed">Trải nghiệm giao diện chia đôi màn hình, tự động chạy Audio và công cụ ghi chú y hệt IDP/BC.</p>
                <div className="font-bold text-[#0ea5e9] flex items-center gap-2 group-hover:gap-4 transition-all text-sm uppercase tracking-wider">
                  Vào làm thử ngay <span>➜</span>
                </div>
              </div>

              {/* Card Demo 2 */}
              <div 
                onClick={() => onStartTest('standard', dummyStandard)}
                className="bg-white/5 backdrop-blur-md border border-white/10 rounded-[2rem] p-8 md:p-10 cursor-pointer hover:bg-white/10 hover:border-white/20 transition-all duration-300 group hover:-translate-y-1"
              >
                <div className="flex justify-between items-start mb-8">
                  <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-emerald-500 to-teal-500 flex items-center justify-center text-3xl shadow-lg border border-white/20 group-hover:scale-110 transition-transform">🧬</div>
                  <span className="bg-white/10 text-white font-bold text-[10px] px-3 py-1 rounded-full uppercase tracking-widest border border-white/5">Free Demo</span>
                </div>
                <h3 className="text-2xl font-black mb-3 text-white group-hover:text-emerald-400 transition-colors leading-tight">Standard Interface</h3>
                <p className="text-slate-400 font-medium mb-8 leading-relaxed">Giao diện dạng thẻ (card) trực quan, bảng điều hướng thông minh. Phù hợp luyện đề TOEIC, IGCSE.</p>
                <div className="font-bold text-emerald-400 flex items-center gap-2 group-hover:gap-4 transition-all text-sm uppercase tracking-wider">
                  Vào làm thử ngay <span>➜</span>
                </div>
              </div>

            </div>
          </div>
        </section>

      </main>

      {/* 🚀 FOOTER */}
      <footer className="bg-slate-950 text-slate-400 py-12 border-t border-slate-800">
        <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-6">
          <div className="flex items-center gap-3 opacity-60 hover:opacity-100 transition-all cursor-pointer" onClick={() => window.open('https://tonyenglish.vn/vi', '_blank')}>
             <img src="/logo-shield.png" alt="TonyEnglish" className="h-8 w-auto object-contain grayscale" />
             <div className="font-black text-xl tracking-tight text-white">TONY<span className="text-[#0ea5e9]">ENGLISH</span></div>
          </div>
          <div className="text-sm font-medium text-center md:text-right text-slate-500">
            <p>© 2026 TonyEnglish.vn - The future begins here.</p>
            <p className="mt-1">Nền tảng luyện thi và giáo dục trực tuyến thế hệ mới.</p>
          </div>
        </div>
      </footer>

      {/* 🚀 MODAL ĐĂNG NHẬP (Glassmorphism & Smooth Animation) */}
      {showLoginModal && (
        <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-md z-[100] flex items-center justify-center p-4 animate-in fade-in duration-200">
          <div className="bg-white rounded-[2rem] w-full max-w-md shadow-2xl overflow-hidden animate-in zoom-in-95 duration-300 border border-slate-200">
            
            <div className="bg-white px-8 py-6 border-b border-slate-100 flex justify-between items-center">
              <div className="flex items-center gap-2">
                 <div className="w-8 h-8 bg-sky-50 rounded-full flex items-center justify-center text-lg">👋</div>
                 <h2 className="text-xl font-black text-slate-800 tracking-tight">Đăng Nhập</h2>
              </div>
              <button 
                  onClick={() => setShowLoginModal(false)} 
                  className="text-slate-400 hover:text-rose-500 w-8 h-8 rounded-full hover:bg-rose-50 flex items-center justify-center transition-colors"
              >
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
              </button>
            </div>

            <form onSubmit={handleLogin} className="p-8 space-y-6">
              <div className="space-y-2">
                <label className="text-[11px] font-bold text-slate-500 uppercase tracking-widest ml-1">Email của bạn</label>
                <input 
                  type="email" 
                  required
                  placeholder="name@example.com" 
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-5 py-4 outline-none focus:border-[#0ea5e9] focus:bg-white focus:ring-4 focus:ring-[#0ea5e9]/10 text-[15px] font-semibold text-slate-800 transition-all shadow-sm placeholder:text-slate-400 placeholder:font-medium" 
                />
              </div>

              <div className="space-y-2">
                <div className="flex justify-between items-center ml-1 pr-1">
                  <label className="text-[11px] font-bold text-slate-500 uppercase tracking-widest">Mật khẩu</label>
                  <a href="#" className="text-[11px] font-bold text-[#0ea5e9] hover:underline">Quên mật khẩu?</a>
                </div>
                <input 
                  type="password" 
                  required
                  placeholder="••••••••" 
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-5 py-4 outline-none focus:border-[#0ea5e9] focus:bg-white focus:ring-4 focus:ring-[#0ea5e9]/10 text-[15px] font-semibold text-slate-800 transition-all shadow-sm placeholder:text-slate-400 placeholder:font-medium" 
                />
              </div>

              <button 
                type="submit" 
                disabled={isLoading}
                className="w-full bg-[#0ea5e9] hover:bg-[#0284c7] disabled:bg-slate-300 text-white font-black py-4 rounded-xl shadow-[0_8px_20px_rgba(14,165,233,0.3)] disabled:shadow-none transition-all active:scale-95 flex justify-center items-center gap-2 mt-2 uppercase tracking-widest text-[13px]"
              >
                {isLoading ? (
                    <><span className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></span> Đang xử lý...</>
                ) : (
                    'Đăng Nhập Hệ Thống'
                )}
              </button>
            </form>
          </div>
        </div>
      )}

    </div>
  );
}