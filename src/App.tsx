import React, { useState, useEffect } from 'react';
import ComputerTest from './ComputerTest';
import PaperTest from './PaperTest';
import StandardTest from './StandardTest';
import AdminPanel from './AdminPanel';
import AuthModal from './AuthModal';
import { supabase } from './supabase';
import { testData as localTestData } from './testData';
import './tailwind.css';

export default function App() {
  const [currentView, setCurrentView] = useState<'menu' | 'computer' | 'paper' | 'admin' | 'standard'>('menu');
  const [cloudTests, setCloudTests] = useState<any[]>([]);
  const [selectedTest, setSelectedTest] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(false);
  
  // State lựa chọn định dạng cho IELTS
  const [showFormatPicker, setShowFormatPicker] = useState<{show: boolean, data: any} | null>(null);

  const [user, setUser] = useState<any>(null);
  const [showAuthModal, setShowAuthModal] = useState(false);
  const [history, setHistory] = useState<any[]>([]);

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => setUser(session?.user || null));
    const { data: authListener } = supabase.auth.onAuthStateChange((_event, session) => setUser(session?.user || null));
    return () => authListener.subscription.unsubscribe();
  }, []);

  useEffect(() => {
    if (currentView === 'menu') {
      fetchTestsFromCloud();
      if (user) fetchUserHistory(user.email);
    }
  }, [currentView, user]);

  const fetchTestsFromCloud = async () => {
    setIsLoading(true);
    const { data } = await supabase.from('mock_tests').select('*').order('created_at', { ascending: false });
    if (data) setCloudTests(data);
    setIsLoading(false);
  };

  const fetchUserHistory = async (email: string) => {
    const { data } = await supabase.from('test_results').select('*').eq('user_email', email).order('created_at', { ascending: false });
    if (data) setHistory(data);
  };

  // HÀM LƯU KẾT QUẢ THI VÀO DATABASE
  const handleFinishTest = async (results: { score: number, total: number, testTitle: string }) => {
    if (user) {
      const accuracy = Math.round((results.score / results.total) * 100);
      await supabase.from('test_results').insert([{
        user_email: user.email,
        test_title: results.testTitle,
        score: results.score,
        total_questions: results.total,
        accuracy: accuracy
      }]);
      alert(`🎉 Bạn đã hoàn thành! Điểm số: ${results.score}/${results.total} (${accuracy}%)`);
    }
    setCurrentView('menu');
    setSelectedTest(null);
  };

  const handleStartTest = (type: string, testData: any = null) => {
    if (!user) {
      alert("⚠️ Vui lòng Đăng Nhập để lưu kết quả!");
      setShowAuthModal(true);
      return;
    }
    
    // Bóc tách data
    let parsedData = testData;
    if (typeof testData === 'string') try { parsedData = JSON.parse(testData); } catch (e) {}

    const category = parsedData?.examCategory || 'ielts';
    
    if (category === 'standard') {
      setSelectedTest(parsedData);
      setCurrentView('standard');
    } else {
      // Nếu là IELTS, hiện bảng chọn định dạng
      setShowFormatPicker({ show: true, data: parsedData });
    }
  };

  if (currentView === 'computer') return <ComputerTest onBack={() => setCurrentView('menu')} testData={selectedTest} onFinish={handleFinishTest} />;
  if (currentView === 'paper') return <PaperTest onBack={() => setCurrentView('menu')} testData={selectedTest} onFinish={handleFinishTest} />;
  if (currentView === 'standard') return <StandardTest onBack={() => setCurrentView('menu')} testData={selectedTest} onFinish={handleFinishTest} />;
  if (currentView === 'admin') return <AdminPanel onBack={() => setCurrentView('menu')} />;

  return (
    <div className="min-h-screen bg-[#f1f5f9] flex flex-col items-center py-8 px-4 font-sans relative">
      {showAuthModal && <AuthModal onClose={() => setShowAuthModal(false)} />}
      
      {/* MODAL CHỌN ĐỊNH DẠNG IELTS */}
      {showFormatPicker?.show && (
        <div className="fixed inset-0 bg-black/60 z-[100] flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl shadow-2xl p-8 max-w-md w-full text-center">
            <h2 className="text-xl font-black text-slate-800 mb-2">Chọn hình thức làm bài</h2>
            <p className="text-sm text-slate-500 mb-8 italic">Đề thi: {showFormatPicker.data?.title}</p>
            <div className="grid grid-cols-2 gap-4">
              <button 
                onClick={() => { setSelectedTest(showFormatPicker.data); setCurrentView('computer'); setShowFormatPicker(null); }}
                className="flex flex-col items-center p-6 border-2 border-blue-100 rounded-xl hover:border-blue-500 hover:bg-blue-50 transition group"
              >
                <span className="text-4xl mb-2 group-hover:scale-110 transition">💻</span>
                <span className="font-bold text-blue-700">Thi Máy</span>
                <span className="text-[10px] text-slate-400 mt-1">Giao diện IDP/BC</span>
              </button>
              <button 
                onClick={() => { setSelectedTest(showFormatPicker.data); setCurrentView('paper'); setShowFormatPicker(null); }}
                className="flex flex-col items-center p-6 border-2 border-emerald-100 rounded-xl hover:border-emerald-500 hover:bg-emerald-50 transition group"
              >
                <span className="text-4xl mb-2 group-hover:scale-110 transition">📝</span>
                <span className="font-bold text-emerald-700">Thi Giấy</span>
                <span className="text-[10px] text-slate-400 mt-1">Dàn trang cuộn dọc</span>
              </button>
            </div>
            <button onClick={() => setShowFormatPicker(null)} className="mt-6 text-slate-400 text-sm font-bold hover:text-slate-600 underline">Hủy bỏ</button>
          </div>
        </div>
      )}

      <div className="max-w-6xl w-full">
        {/* HEADER TÀI KHOẢN (giữ nguyên) */}
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
            <button onClick={() => setCurrentView('admin')} className="bg-gray-100 hover:bg-gray-200 text-gray-700 text-sm px-4 py-2 rounded-lg font-bold transition">⚙️ Quản Trị</button>
            {user ? (
              <button onClick={async () => { if (window.confirm("Đăng xuất?")) await supabase.auth.signOut(); }} className="bg-red-50 hover:bg-red-100 text-red-600 text-sm px-4 py-2 rounded-lg font-bold transition">Đăng xuất</button>
            ) : (
              <button onClick={() => setShowAuthModal(true)} className="bg-[#2b88c9] hover:bg-[#1a6ea6] text-white text-sm px-5 py-2 rounded-lg font-bold transition">Đăng Nhập</button>
            )}
          </div>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2 bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden h-fit">
            <div className="bg-[#1f2937] px-8 py-10 text-center">
              <h1 className="text-3xl font-bold text-white mb-3">Hệ Thống Luyện Thi Mock Test</h1>
              <p className="text-gray-300 text-sm italic">Lưu ý: Các bài thi mẫu sẽ mặc định mở giao diện thi thực tế nhất.</p>
            </div>
            <div className="p-8">
              <h3 className="font-bold text-lg text-gray-800 mb-4 flex items-center gap-2"><span className="w-1.5 h-5 bg-blue-500 rounded"></span> Bài Thi Mẫu (Demo)</h3>
              <div className="grid md:grid-cols-2 gap-6 mb-10">
                <button onClick={() => handleStartTest('computer', localTestData)} className="flex flex-col items-center text-center p-8 border-2 border-gray-200 rounded-xl hover:border-blue-500 hover:bg-blue-50 transition-all group">
                  <div className="text-6xl mb-4 group-hover:scale-110 transition">💻</div>
                  <h2 className="text-xl font-bold text-gray-800 mb-2">IELTS Simulation</h2>
                  <p className="text-sm text-gray-500 italic">Highlight, Copy, Sticky Note chuẩn IDP/BC</p>
                </button>
                <button onClick={() => handleStartTest('standard', { examCategory: 'standard', skill: 'reading', parts: [] })} className="flex flex-col items-center text-center p-8 border-2 border-gray-200 rounded-xl hover:border-purple-500 hover:bg-purple-50 transition-all group">
                  <div className="text-6xl mb-4 group-hover:scale-110 transition">📙</div>
                  <h2 className="text-xl font-bold text-gray-800 mb-2">Standard (TOEIC)</h2>
                  <p className="text-sm text-gray-500 italic">Dạng Card, Sidebar Navigation thông minh</p>
                </button>
              </div>

              <h3 className="font-bold text-lg text-gray-800 mb-4 flex items-center gap-2 pt-6 border-t border-gray-100">
                <span className="w-1.5 h-5 bg-purple-500 rounded"></span> Kho Đề Từ Đám Mây (Live)
              </h3>
              {isLoading ? <div className="text-center py-6 text-gray-500 animate-pulse">Đang tải đề...</div> : (
                <div className="grid sm:grid-cols-2 gap-6">
                  {cloudTests.map((test) => {
                    let parsedData = test.test_data;
                    if (typeof parsedData === 'string') try { parsedData = JSON.parse(parsedData); } catch (e) {}
                    const cat = parsedData?.examCategory || 'ielts';
                    const sk = parsedData?.skill || 'reading';
                    return (
                      <div key={test.id} className="border border-purple-200 bg-purple-50/30 rounded-xl p-5 hover:shadow-md transition flex flex-col">
                        <div className="flex justify-between items-start mb-2">
                          <span className="bg-purple-100 text-purple-700 text-[10px] font-bold px-2 py-1 rounded">LIVE</span>
                          <span className={`text-[10px] px-2 py-0.5 rounded uppercase font-bold border ${cat === 'standard' ? 'bg-purple-200 text-purple-800' : 'bg-blue-100 text-blue-700'}`}>{cat} - {sk}</span>
                        </div>
                        <h2 className="text-base font-bold text-gray-800 mb-4 line-clamp-2 min-h-[48px]">{test.title}</h2>
                        <button onClick={() => handleStartTest('computer', parsedData)} className="w-full mt-auto bg-purple-600 hover:bg-purple-700 text-white text-sm font-bold py-2.5 rounded-lg shadow-sm">Bắt đầu làm bài ➔</button>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          </div>

          {/* DASHBOARD LỊCH SỬ (giữ nguyên) */}
          <div className="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden h-fit max-h-[700px] flex flex-col">
            <div className="bg-gray-50 border-b border-gray-200 px-6 py-4"><h2 className="font-bold text-gray-800 flex items-center gap-2">📈 Lịch Sử</h2></div>
            <div className="p-6 overflow-y-auto flex-1">
              {history.map((record, i) => (
                <div key={i} className="bg-gray-50 border border-gray-200 p-4 rounded-xl mb-4 relative overflow-hidden">
                  <div className={`absolute left-0 top-0 bottom-0 w-1 ${record.accuracy >= 70 ? 'bg-green-500' : 'bg-yellow-400'}`}></div>
                  <h3 className="font-bold text-sm text-gray-800 truncate mb-1">{record.test_title}</h3>
                  <div className="flex justify-between items-end">
                    <p className="text-lg font-black">{record.score}/{record.total_questions}</p>
                    <p className="text-[10px] font-bold text-gray-400">{record.accuracy}%</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}