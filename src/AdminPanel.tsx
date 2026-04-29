import React, { useState } from 'react';
import { supabase } from './supabase';

export default function AdminPanel({ onNavigate }: { onNavigate: (view: string) => void }) {
  // Trạng thái quản lý Tab
  const [activeTab, setActiveTab] = useState('create-case-study');

  // Trạng thái cho Form Tạo đề Case Study
  const [title, setTitle] = useState('');
  const [examCode, setExamCode] = useState('');
  const [paper, setPaper] = useState('');
  const [duration, setDuration] = useState('');
  const [jsonConfig, setJsonConfig] = useState('');
  const [isSaving, setIsSaving] = useState(false);

  // Hàm xử lý Đăng xuất
  const handleLogout = async () => {
    await supabase.auth.signOut();
    onNavigate('admin-login');
  };

  // Hàm lưu đề Case Study (Tạm thời in ra log, bài sau mình sẽ đấu nối Supabase)
  const handleSaveCaseStudy = () => {
    setIsSaving(true);
    setTimeout(() => {
      console.log("Đã lưu đề mới:", { title, examCode, paper, duration, jsonConfig });
      alert("✅ Đã lưu đề Case Study lên hệ thống thành công!");
      setIsSaving(false);
      // Reset form sau khi lưu
      setTitle(''); setExamCode(''); setPaper(''); setDuration(''); setJsonConfig('');
    }, 1000);
  };

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-800 flex">
      
      {/* SIDEBAR TÙY CHỈNH */}
      <aside className="w-64 bg-[#0a5482] text-white flex flex-col shrink-0">
        <div className="h-16 flex items-center justify-center border-b border-blue-900/50">
          <h1 className="font-black text-xl tracking-widest">ADMIN PANEL</h1>
        </div>
        <nav className="flex-1 py-6 px-4 space-y-2">
          <button 
            onClick={() => setActiveTab('manage')}
            className={`w-full text-left px-4 py-3 rounded-xl font-bold transition-colors ${activeTab === 'manage' ? 'bg-[#1e88e5] text-white' : 'text-blue-100 hover:bg-blue-900/30'}`}
          >
            📊 Tổng quan & Quản lý
          </button>
          <button 
            onClick={() => setActiveTab('create-standard')}
            className={`w-full text-left px-4 py-3 rounded-xl font-bold transition-colors ${activeTab === 'create-standard' ? 'bg-[#1e88e5] text-white' : 'text-blue-100 hover:bg-blue-900/30'}`}
          >
            📝 Tạo đề Tiêu chuẩn
          </button>
          <button 
            onClick={() => setActiveTab('create-case-study')}
            className={`w-full text-left px-4 py-3 rounded-xl font-bold transition-colors relative overflow-hidden ${activeTab === 'create-case-study' ? 'bg-[#1e88e5] text-white' : 'text-blue-100 hover:bg-blue-900/30'}`}
          >
            <span className="absolute top-1 right-2 text-[9px] bg-orange-500 px-1.5 rounded text-white uppercase tracking-wider">AI</span>
            💼 Tạo đề Case Study
          </button>
        </nav>
        <div className="p-4 border-t border-blue-900/50">
          <button onClick={handleLogout} className="w-full bg-blue-900/50 hover:bg-red-500 text-white font-bold py-3 rounded-xl transition-colors">
            Đăng xuất
          </button>
        </div>
      </aside>

      {/* NỘI DUNG CHÍNH CỦA TAB */}
      <main className="flex-1 flex flex-col h-screen overflow-hidden">
        <header className="h-16 bg-white border-b border-slate-200 flex items-center px-8 shrink-0 shadow-sm">
          <h2 className="text-xl font-black text-slate-700">
            {activeTab === 'create-case-study' ? 'Xưởng tạo đề Case Study (Split-screen)' : 'Quản trị hệ thống'}
          </h2>
        </header>

        <div className="flex-1 overflow-y-auto p-8">
          
          {/* GIAO DIỆN TẠO ĐỀ CASE STUDY */}
          {activeTab === 'create-case-study' && (
            <div className="max-w-4xl mx-auto space-y-8 pb-12">
              <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
                <h3 className="text-lg font-black text-slate-800 mb-6 border-b border-slate-100 pb-4">1. Thông tin cơ bản</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div className="space-y-2 md:col-span-2">
                    <label className="text-[13px] font-bold text-slate-500 uppercase tracking-wider">Tên bài thi</label>
                    <input 
                      type="text" value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Ví dụ: Business Studies Mock Test 2026..."
                      className="w-full border border-slate-300 rounded-xl px-4 py-3 font-medium focus:border-[#1e88e5] focus:ring-2 focus:ring-blue-50 outline-none" 
                    />
                  </div>
                  <div className="space-y-2">
                    <label className="text-[13px] font-bold text-slate-500 uppercase tracking-wider">Mã môn (Exam Code)</label>
                    <input 
                      type="text" value={examCode} onChange={(e) => setExamCode(e.target.value)} placeholder="Ví dụ: 0450, 0455..."
                      className="w-full border border-slate-300 rounded-xl px-4 py-3 font-medium focus:border-[#1e88e5] focus:ring-2 focus:ring-blue-50 outline-none" 
                    />
                  </div>
                  <div className="space-y-2">
                    <label className="text-[13px] font-bold text-slate-500 uppercase tracking-wider">Paper / Variant</label>
                    <input 
                      type="text" value={paper} onChange={(e) => setPaper(e.target.value)} placeholder="Ví dụ: 22"
                      className="w-full border border-slate-300 rounded-xl px-4 py-3 font-medium focus:border-[#1e88e5] focus:ring-2 focus:ring-blue-50 outline-none" 
                    />
                  </div>
                </div>
              </div>

              <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
                <h3 className="text-lg font-black text-slate-800 mb-6 border-b border-slate-100 pb-4 flex justify-between items-center">
                  <span>2. Tài liệu đính kèm (Insert / Case Study)</span>
                </h3>
                <div className="border-2 border-dashed border-slate-300 rounded-xl p-8 text-center hover:bg-slate-50 transition-colors cursor-pointer">
                  <div className="text-4xl mb-3">📄</div>
                  <p className="font-bold text-slate-700">Kéo thả file PDF vào đây hoặc <span className="text-[#1e88e5]">Bấm để chọn file</span></p>
                  <p className="text-sm text-slate-400 mt-2">Dung lượng tối đa 10MB.</p>
                </div>
              </div>

              <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
                <h3 className="text-lg font-black text-slate-800 mb-6 border-b border-slate-100 pb-4 flex justify-between items-center">
                  <span>3. Cấu trúc câu hỏi (JSON)</span>
                  <button className="text-[13px] text-[#1e88e5] font-bold hover:underline">Copy Prompt cho AI</button>
                </h3>
                <p className="text-sm text-slate-500 mb-4">Dán đoạn mã JSON do AI bóc tách từ file đề thi và Marking Scheme vào đây.</p>
                <textarea 
                  value={jsonConfig}
                  onChange={(e) => setJsonConfig(e.target.value)}
                  placeholder="{\n  'questions': [...]\n}"
                  className="w-full border border-slate-300 rounded-xl p-4 font-mono text-[13px] h-64 focus:border-[#1e88e5] focus:ring-2 focus:ring-blue-50 outline-none bg-slate-50"
                ></textarea>
              </div>

              <div className="flex justify-end gap-4">
                <button className="bg-slate-200 hover:bg-slate-300 text-slate-700 font-bold px-8 py-3 rounded-xl transition-colors">
                  👁️ Xem trước (Preview)
                </button>
                <button 
                  onClick={handleSaveCaseStudy}
                  disabled={isSaving}
                  className="bg-emerald-500 hover:bg-emerald-600 text-white font-black px-10 py-3 rounded-xl shadow-lg transition-transform active:scale-95 disabled:opacity-50"
                >
                  {isSaving ? 'ĐANG LƯU...' : '💾 LƯU BÀI THI'}
                </button>
              </div>
            </div>
          )}

          {/* CÁC TAB KHÁC (Để trống chờ phát triển sau) */}
          {activeTab !== 'create-case-study' && (
            <div className="flex items-center justify-center h-full text-slate-400 font-medium">
              Khu vực này đang được xây dựng...
            </div>
          )}

        </div>
      </main>
    </div>
  );
}