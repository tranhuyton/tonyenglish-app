import React, { useState, useEffect } from 'react';
import ComputerTest from './ComputerTest';
import PaperTest from './PaperTest';
import AdminPanel from './AdminPanel';
import AuthModal from './AuthModal'; // Kéo Popup Đăng nhập vào
import { supabase } from './supabase';
import { testData as localTestData } from './testData';
import './tailwind.css';

export default function App() {
  const [currentView, setCurrentView] = useState<'menu' | 'computer' | 'paper' | 'admin'>('menu');
  const [cloudTests, setCloudTests] = useState<any[]>([]);
  const [selectedTest, setSelectedTest] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(false);
  
  // TÀI KHOẢN VÀ LỊCH SỬ HỌC TẬP
  const [user, setUser] = useState<any>(null);
  const [showAuthModal, setShowAuthModal] = useState(false);
  const [history, setHistory] = useState<any[]>([]);

  useEffect(() => {
    // Check xem có ai đang đăng nhập không
    supabase.auth.getSession().then(({ data: { session } }) => setUser(session?.user || null));
    // Tự động thay đổi Trạng thái trên giao diện khi Đăng nhập/Đăng xuất
    const { data: authListener } = supabase.auth.onAuthStateChange((_event, session) => setUser(session?.user || null));
    return () => authListener.subscription.unsubscribe();
  }, []);

  useEffect(() => {
    if (currentView === 'menu') {
      fetchTestsFromCloud();
      if (user) fetchUserHistory(user.email);
      else setHistory([]); // Nếu chưa đăng nhập thì xóa trắng bảng lịch sử
    }
  }, [currentView, user]);

  const fetchTestsFromCloud = async () => {
    setIsLoading(true);
    const { data } = await supabase.from('mock_tests').select('*').order('created_at', { ascending: false });
    if (data) setCloudTests(data);
    setIsLoading(false);
  };

  const fetchUserHistory = async (email: string) => {
    // CHỈ LẤY ĐIỂM CỦA ĐÚNG HỌC SINH ĐÓ
    const { data } = await supabase.from('test_results').select('*').eq('user_email', email).order('created_at', { ascending: false });
    if (data) setHistory(data);
  };

  const handleLogout = async () => {
    if (window.confirm("Bạn có chắc muốn đăng xuất?")) await supabase.auth.signOut();
  };

  const handleBackToMenu = () => { setCurrentView('menu'); setSelectedTest(null); };

  // HÀM CHẶN CỬA: Nếu chưa đăng nhập thì hiện Popup bắt Đăng nhập
  const handleStartTest = (type: 'computer' | 'paper', testData: any = null) => {
    if (!user) {
      alert("⚠️ Vui lòng Đăng Nhập để hệ thống lưu trữ điểm số của bạn!");
      setShowAuthModal(true);
      return;
    }
    setSelectedTest(testData);
    setCurrentView(type);
  };

  if (currentView === 'computer') return <ComputerTest onBack={handleBackToMenu} />;
  if (currentView === 'paper') return <PaperTest onBack={handleBackToMenu} testData={selectedTest || localTestData} />;
  if (currentView === 'admin') return <AdminPanel onBack={handleBackToMenu} />;

  return (
    <div className="min-h-screen bg-[#f1f5f9] flex flex-col items-center py-8 px-4 font-sans relative">
      
      {/* NẾU showAuthModal = true THÌ BẬT POPUP LÊN */}
      {showAuthModal && <AuthModal onClose={() => setShowAuthModal(false)} />}
      
      <div className="max-w-6xl w-full">
        {/* THANH ĐIỀU HƯỚNG TÀI KHOẢN TRÊN CÙNG */}
        <div className="flex justify-between items-center bg-white p-4 rounded-xl shadow-sm mb-6 border border-gray-200">
          <div className="flex items-center gap-3">
            <div className={`w-10 h-10 rounded-full flex items-center justify-center font-bold text-xl uppercase ${user ? 'bg-blue-100 text-blue-600' : 'bg-gray-100 text-gray-400'}`}>
              {user ? user.email.charAt(0) : 'G'}
            </div>
            <div>
              <p className="text-xs text-gray-500">{user ? 'Xin chào học viên,' : 'Khách truy cập'}</p>
              <p className="font-bold text-gray-800">{user ? user.email : 'Chưa đăng nhập'}</p>
            </div>
          </div>
          <div className="flex items-center gap-3">
            <button onClick={() => setCurrentView('admin')} className="bg-gray-100 hover:bg-gray-200 text-gray-700 text-sm px-4 py-2 rounded-lg font-bold transition">
              ⚙️ Quản Trị
            </button>
            {user ? (
              <button onClick={handleLogout} className="bg-red-50 hover:bg-red-100 text-red-600 text-sm px-4 py-2 rounded-lg font-bold transition border border-red-100">
                Đăng xuất
              </button>
            ) : (
              <button onClick={() => setShowAuthModal(true)} className="bg-[#2b88c9] hover:bg-[#1a6ea6] text-white text-sm px-5 py-2 rounded-lg font-bold transition shadow-sm">
                Đăng Nhập
              </button>
            )}
          </div>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          
          {/* ================ CỘT TRÁI: DANH SÁCH ĐỀ THI ================ */}
          <div className="lg:col-span-2 bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden h-fit">
            
            {/* CẬP NHẬT HEADER GIỐNG BẢN CŨ (To, rõ ràng và sang trọng hơn) */}
            <div className="bg-[#1f2937] px-8 py-10 text-center relative overflow-hidden">
              <h1 className="text-3xl font-bold text-white mb-3">Hệ Thống Luyện Thi Mock Test</h1>
              <p className="text-gray-300 text-sm">Vui lòng chọn định dạng bài thi bạn muốn trải nghiệm.</p>
              <p className="text-emerald-400 text-sm font-bold mt-2">Dữ liệu làm bài được tự động lưu & đồng bộ Máy chủ.</p>
            </div>
            
            <div className="p-8">
              
              {/* PHẦN 1: BÀI THI MẪU - ĐƯỢC THAY BẰNG GIAO DIỆN NÚT TO CỦA BẢN CŨ */}
              <h3 className="font-bold text-lg text-gray-800 mb-4 flex items-center gap-2">
                <span className="w-1.5 h-5 bg-blue-500 rounded"></span> Bài Thi Mẫu (Demo Offline)
              </h3>
              
              <div className="grid md:grid-cols-2 gap-6 mb-10">
                {/* NÚT THI MÁY */}
                <button 
                  onClick={() => handleStartTest('computer')}
                  className="flex flex-col items-center text-center p-8 border-2 border-gray-200 rounded-xl hover:border-[#3b82f6] hover:bg-blue-50 transition-all group cursor-pointer"
                >
                  <div className="text-6xl mb-4 group-hover:scale-110 transition-transform">💻</div>
                  <h2 className="text-xl font-bold text-gray-800 mb-2 group-hover:text-blue-600">Computer-Delivered</h2>
                  <p className="text-sm text-gray-500">Giao diện chia đôi màn hình kéo thả, ô điền từ nội tuyến. Chuẩn format thi máy IDP/BC.</p>
                </button>

                {/* NÚT THI GIẤY / NGHE */}
                <button 
                  onClick={() => handleStartTest('paper')}
                  className="flex flex-col items-center text-center p-8 border-2 border-gray-200 rounded-xl hover:border-[#2b88c9] hover:bg-blue-50 transition-all group cursor-pointer"
                >
                  <div className="text-6xl mb-4 group-hover:scale-110 transition-transform">📝</div>
                  <h2 className="text-xl font-bold text-gray-800 mb-2 group-hover:text-[#2b88c9]">Paper-based / Listening</h2>
                  <p className="text-sm text-gray-500">Giao diện chia cột cố định, có Audio nghe, ghim Navigation trượt theo mắt, đánh dấu câu.</p>
                </button>
              </div>

              {/* PHẦN 2: KHO ĐỀ TỪ ĐÁM MÂY */}
              <h3 className="font-bold text-lg text-gray-800 mb-4 flex items-center gap-2 pt-6 border-t border-gray-100">
                <span className="w-1.5 h-5 bg-purple-500 rounded"></span> Kho Đề Từ Đám Mây (Live Database)
              </h3>
              
              {isLoading ? (
                 <div className="text-center py-6 text-gray-500 animate-pulse">Đang tải đề...</div>
              ) : cloudTests.length === 0 ? (
                 <p className="text-gray-500 italic text-sm py-4">Chưa có đề thi nào trên Server.</p>
              ) : (
                <div className="grid sm:grid-cols-2 gap-6">
                  {cloudTests.map((test) => {
                    // Tự động nhận diện loại đề từ Database hoặc JSON data
                    const testType = test.type || (test.test_data && test.test_data.type) || 'paper';
                    
                    return (
                      <div key={test.id} className="border border-purple-200 bg-purple-50/30 rounded-xl p-5 hover:shadow-md transition group">
                        <div className="flex justify-between items-start mb-2">
                          <span className="bg-purple-100 text-purple-700 text-[10px] font-bold px-2 py-1 rounded uppercase inline-block">LIVE CLOUD</span>
                          {/* Hiển thị Badge cho phù hợp nền sáng */}
                          {testType === 'computer' ? (
                            <span className="bg-purple-100 text-purple-700 text-[10px] px-2 py-0.5 rounded uppercase font-bold border border-purple-200">
                              💻 Thi Máy
                            </span>
                          ) : (
                            <span className="bg-blue-100 text-blue-700 text-[10px] px-2 py-0.5 rounded uppercase font-bold border border-blue-200">
                              📝 Thi Giấy
                            </span>
                          )}
                        </div>
                        <h2 className="text-base font-bold text-gray-800 mb-1 truncate" title={test.title}>{test.title}</h2>
                        <p className="text-xs text-gray-500 mb-4 font-mono">ID: {test.test_id}</p>
                        <button 
                          onClick={() => handleStartTest(testType, test.test_data)} 
                          className="w-full bg-purple-600 hover:bg-purple-700 text-white text-sm font-bold py-2.5 rounded-lg transition shadow-sm"
                        >
                          Làm bài thi này ➔
                        </button>
                      </div>
                    );
                  })}
                </div>
              )}

            </div>
          </div>

          {/* ================ CỘT PHẢI: BẢNG LỊCH SỬ DASHBOARD ================ */}
          <div className="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden h-fit max-h-[700px] flex flex-col">
            <div className="bg-gray-50 border-b border-gray-200 px-6 py-4 shrink-0">
              <h2 className="font-bold text-gray-800 flex items-center gap-2"><span>📈</span> Lịch Sử Học Tập</h2>
            </div>
            
            <div className="p-6 overflow-y-auto custom-scrollbar flex-1">
              {!user ? (
                <div className="text-center py-10">
                  <div className="text-4xl mb-3">🔒</div>
                  <p className="text-gray-500 text-sm">Đăng nhập để xem lịch sử làm bài của bạn.</p>
                  <button onClick={() => setShowAuthModal(true)} className="mt-4 text-sm font-bold text-[#2b88c9] underline">Đăng nhập ngay</button>
                </div>
              ) : history.length === 0 ? (
                <div className="text-center py-10">
                  <div className="text-4xl mb-3">📭</div>
                  <p className="text-gray-500 text-sm">Bạn chưa nộp bài thi nào.</p>
                </div>
              ) : (
                <div className="space-y-4">
                  {history.map((record, index) => (
                    <div key={index} className="bg-gray-50 border border-gray-200 p-4 rounded-xl relative overflow-hidden hover:shadow-md transition">
                      <div className={`absolute left-0 top-0 bottom-0 w-1 ${record.accuracy >= 70 ? 'bg-green-500' : record.accuracy >= 50 ? 'bg-yellow-400' : 'bg-red-500'}`}></div>
                      
                      <h3 className="font-bold text-sm text-gray-800 truncate mb-1 pr-2" title={record.test_title}>{record.test_title}</h3>
                      <p className="text-[11px] text-gray-400 mb-3">{new Date(record.created_at).toLocaleString('vi-VN')}</p>
                      
                      <div className="flex justify-between items-end">
                        <div>
                          <p className="text-[10px] text-gray-500 uppercase font-bold tracking-wider mb-1">Điểm số</p>
                          <p className="text-lg font-black text-gray-800">{record.score} <span className="text-sm font-medium text-gray-400">/ {record.total_questions}</span></p>
                        </div>
                        <div className="text-right">
                          <p className="text-[10px] text-gray-500 uppercase font-bold tracking-wider mb-1">Chính xác</p>
                          <p className={`font-bold ${record.accuracy >= 70 ? 'text-green-600' : record.accuracy >= 50 ? 'text-yellow-600' : 'text-red-600'}`}>{record.accuracy}%</p>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}