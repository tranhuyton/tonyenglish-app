import React, { useState } from 'react';
import { supabase } from './supabase';

export default function AdminPanel({ onNavigate }: { onNavigate: (view: string) => void }) {
  const [activeTab, setActiveTab] = useState('create-case-study');

  const [title, setTitle] = useState('');
  const [examCode, setExamCode] = useState('');
  const [paper, setPaper] = useState('');
  const [jsonConfig, setJsonConfig] = useState('');
  // STATE MỚI: Dùng để lưu trữ file PDF khi người dùng chọn
  const [pdfFile, setPdfFile] = useState<File | null>(null); 
  const [isSaving, setIsSaving] = useState(false);

  const handleLogout = async () => {
    await supabase.auth.signOut();
    onNavigate('admin-login');
  };

  // HÀM XỬ LÝ KHI NGƯỜI DÙNG CHỌN FILE
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      const file = e.target.files[0];
      if (file.type === 'application/pdf') {
        setPdfFile(file);
      } else {
        alert('⚠️ Vui lòng chỉ chọn định dạng file PDF anh nhé!');
      }
    }
  };

  const handleSaveCaseStudy = async () => {
    if (!title || !examCode || !paper || !jsonConfig) {
      alert("⚠️ Anh vui lòng điền đầy đủ thông tin và dán cấu trúc JSON nhé!");
      return;
    }

    let parsedJson;
    try {
      parsedJson = JSON.parse(jsonConfig);
    } catch (error) {
      alert("❌ Lỗi cú pháp JSON! Anh kiểm tra lại xem copy từ AI đã chuẩn chưa nhé.");
      return;
    }

    setIsSaving(true);

    try {
      let pdfUrl = '';

      // BƯỚC 1: NẾU CÓ CHỌN FILE PDF THÌ UPLOAD LÊN STORAGE TRƯỚC
      if (pdfFile) {
        // Tạo tên file độc nhất để không bị trùng lặp (dùng timestamp)
        const fileName = `${Date.now()}_${pdfFile.name.replace(/\s+/g, '_')}`;
        
        const { error: uploadError } = await supabase.storage
          .from('case_study_pdfs')
          .upload(fileName, pdfFile);

        if (uploadError) {
          throw new Error("Lỗi khi tải file PDF lên kho: " + uploadError.message);
        }

        // Lấy đường link công khai của file vừa upload
        const { data: publicUrlData } = supabase.storage
          .from('case_study_pdfs')
          .getPublicUrl(fileName);

        pdfUrl = publicUrlData.publicUrl;
      }

      // BƯỚC 2: BẮN TOÀN BỘ DỮ LIỆU (KÈM LINK PDF) VÀO BẢNG DATABASE
      const { error: dbError } = await supabase
        .from('case_study_tests')
        .insert([
          {
            title: title,
            exam_code: examCode,
            paper: paper,
            json_config: parsedJson,
            insert_pdf_url: pdfUrl // Lưu link PDF vào đây
          }
        ]);

      if (dbError) throw dbError;

      alert("✅ Đã lưu đề Case Study và tải file PDF lên hệ thống thành công!");
      
      // Xóa trắng form để tiện tạo đề tiếp theo
      setTitle(''); 
      setExamCode(''); 
      setPaper(''); 
      setJsonConfig('');
      setPdfFile(null);

    } catch (err: any) {
      console.error("Lỗi khi lưu lên Supabase:", err);
      alert("Đã có lỗi xảy ra từ máy chủ: " + err.message);
    } finally {
      setIsSaving(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-800 flex">
      
      {/* SIDEBAR */}
      <aside className="w-64 bg-[#0a5482] text-white flex flex-col shrink-0">
        <div className="h-16 flex items-center justify-center border-b border-blue-900/50">
          <h1 className="font-black text-xl tracking-widest">ADMIN PANEL</h1>
        </div>
        <nav className="flex-1 py-6 px-4 space-y-2">
          <button onClick={() => setActiveTab('manage')} className={`w-full text-left px-4 py-3 rounded-xl font-bold transition-colors ${activeTab === 'manage' ? 'bg-[#1e88e5] text-white' : 'text-blue-100 hover:bg-blue-900/30'}`}>📊 Tổng quan & Quản lý</button>
          <button onClick={() => setActiveTab('create-standard')} className={`w-full text-left px-4 py-3 rounded-xl font-bold transition-colors ${activeTab === 'create-standard' ? 'bg-[#1e88e5] text-white' : 'text-blue-100 hover:bg-blue-900/30'}`}>📝 Tạo đề Tiêu chuẩn</button>
          <button onClick={() => setActiveTab('create-case-study')} className={`w-full text-left px-4 py-3 rounded-xl font-bold transition-colors relative overflow-hidden ${activeTab === 'create-case-study' ? 'bg-[#1e88e5] text-white' : 'text-blue-100 hover:bg-blue-900/30'}`}>
            <span className="absolute top-1 right-2 text-[9px] bg-orange-500 px-1.5 rounded text-white uppercase tracking-wider">AI</span>
            💼 Tạo đề Case Study
          </button>
        </nav>
        <div className="p-4 border-t border-blue-900/50">
          <button onClick={handleLogout} className="w-full bg-blue-900/50 hover:bg-red-500 text-white font-bold py-3 rounded-xl transition-colors">Đăng xuất</button>
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
          
          {activeTab === 'create-case-study' && (
            <div className="max-w-4xl mx-auto space-y-8 pb-12">
              <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
                <h3 className="text-lg font-black text-slate-800 mb-6 border-b border-slate-100 pb-4">1. Thông tin cơ bản</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div className="space-y-2 md:col-span-2">
                    <label className="text-[13px] font-bold text-slate-500 uppercase tracking-wider">Tên bài thi</label>
                    <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Ví dụ: Business Studies Mock Test 2026..." className="w-full border border-slate-300 rounded-xl px-4 py-3 font-medium focus:border-[#1e88e5] focus:ring-2 focus:ring-blue-50 outline-none bg-white" />
                  </div>
                  <div className="space-y-2">
                    <label className="text-[13px] font-bold text-slate-500 uppercase tracking-wider">Mã môn (Exam Code)</label>
                    <input type="text" value={examCode} onChange={(e) => setExamCode(e.target.value)} placeholder="Ví dụ: 0450, 0455..." className="w-full border border-slate-300 rounded-xl px-4 py-3 font-medium focus:border-[#1e88e5] focus:ring-2 focus:ring-blue-50 outline-none bg-white" />
                  </div>
                  <div className="space-y-2">
                    <label className="text-[13px] font-bold text-slate-500 uppercase tracking-wider">Paper / Variant</label>
                    <input type="text" value={paper} onChange={(e) => setPaper(e.target.value)} placeholder="Ví dụ: 22" className="w-full border border-slate-300 rounded-xl px-4 py-3 font-medium focus:border-[#1e88e5] focus:ring-2 focus:ring-blue-50 outline-none bg-white" />
                  </div>
                </div>
              </div>

              {/* Ô UPLOAD FILE PDF (ĐÃ NÂNG CẤP) */}
              <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
                <h3 className="text-lg font-black text-slate-800 mb-6 border-b border-slate-100 pb-4 flex justify-between items-center">
                  <span>2. Tài liệu đính kèm (Insert / Case Study)</span>
                </h3>
                <div className="border-2 border-dashed border-slate-300 rounded-xl p-8 text-center hover:bg-slate-50 transition-colors relative cursor-pointer group">
                  <input 
                    type="file" 
                    accept="application/pdf"
                    onChange={handleFileChange}
                    className="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-10"
                  />
                  <div className="text-4xl mb-3 transition-transform group-hover:scale-110">
                    {pdfFile ? '✅' : '📄'}
                  </div>
                  <p className="font-bold text-slate-700">
                    {pdfFile ? `Đã chọn: ${pdfFile.name}` : <>Kéo thả file PDF vào đây hoặc <span className="text-[#1e88e5]">Bấm để chọn file</span></>}
                  </p>
                  <p className="text-sm text-slate-400 mt-2">Dung lượng tối đa 10MB. Chỉ nhận định dạng .pdf</p>
                </div>
              </div>

              <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
                <h3 className="text-lg font-black text-slate-800 mb-6 border-b border-slate-100 pb-4 flex justify-between items-center">
                  <span>3. Cấu trúc câu hỏi (JSON)</span>
                  <button className="text-[13px] text-[#1e88e5] font-bold hover:underline" onClick={() => alert("Đã copy Prompt!")}>Copy Prompt cho AI</button>
                </h3>
                <p className="text-sm text-slate-500 mb-4">Dán đoạn mã JSON do AI bóc tách từ file đề thi và Marking Scheme vào đây.</p>
                <textarea value={jsonConfig} onChange={(e) => setJsonConfig(e.target.value)} placeholder={'{\n  "questions": [...]\n}'} className="w-full border border-slate-300 rounded-xl p-4 font-mono text-[13px] h-64 focus:border-[#1e88e5] focus:ring-2 focus:ring-blue-50 outline-none bg-slate-50"></textarea>
              </div>

              <div className="flex justify-end gap-4">
                <button className="bg-slate-200 hover:bg-slate-300 text-slate-700 font-bold px-8 py-3 rounded-xl transition-colors">👁️ Xem trước (Preview)</button>
                <button onClick={handleSaveCaseStudy} disabled={isSaving} className="bg-emerald-500 hover:bg-emerald-600 text-white font-black px-10 py-3 rounded-xl shadow-lg transition-transform active:scale-95 disabled:opacity-50">
                  {isSaving ? 'ĐANG LƯU...' : '💾 LƯU BÀI THI'}
                </button>
              </div>
            </div>
          )}

          {activeTab !== 'create-case-study' && (
            <div className="flex items-center justify-center h-full text-slate-400 font-medium">Khu vực này đang được tích hợp...</div>
          )}

        </div>
      </main>
    </div>
  );
}