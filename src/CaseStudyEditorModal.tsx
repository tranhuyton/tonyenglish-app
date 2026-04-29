import React, { useState } from 'react';
import { supabase } from './supabase';

export default function CaseStudyEditorModal({ testData: testRecord, courses, onClose, onSave }: any) {
  const getInitialData = () => {
    // NẾU LÀ ĐỀ SỬA LẠI
    if (testRecord.content_json) {
      const data = {...testRecord.content_json};
      if (testRecord.insert_pdf_url) {
        if (!data.basicInfo) data.basicInfo = {};
        data.basicInfo.insert_pdf_url = testRecord.insert_pdf_url;
      }
      data.json_config_string = testRecord.json_config ? JSON.stringify(testRecord.json_config, null, 2) : '';
      return data;
    }

    // NẾU LÀ ĐỀ TẠO MỚI
    return {
      basicInfo: {
        title: testRecord.title || '',
        courseId: 'all', 
        skill: 'Case-Study',
        mode: 'Đề thi',
        timeLimit: '90',
        scoreType: 'IGCSE Grading', // Điểm IGCSE mặc định
        insert_pdf_url: '' 
      },
      json_config_string: ''
    };
  };

  const [testData, setTestData] = useState<any>(getInitialData());
  const [isSaving, setIsSaving] = useState(false);
  const [uploading, setUploading] = useState(false);

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setUploading(true);
    try {
      const fileExt = file.name.split('.').pop();
      const fileName = `pdf_${Date.now()}_${Math.random().toString(36).substring(7)}.${fileExt}`;
      const { error } = await supabase.storage.from('test_assets').upload(`uploads/${fileName}`, file);
      if (error) throw error;
      const url = supabase.storage.from('test_assets').getPublicUrl(`uploads/${fileName}`).data.publicUrl;
      setTestData({...testData, basicInfo: {...testData.basicInfo, insert_pdf_url: url}});
    } catch (error: any) { alert("Lỗi upload: " + error.message); } 
    finally { setUploading(false); }
  };

  const handleSave = () => {
    setIsSaving(true);
    onSave(testData); 
  };

  return (
    <div className="fixed inset-0 bg-[#f4f7f6] z-[60] flex flex-col animate-in fade-in">
      {/* HEADER */}
      <div className="bg-white px-8 py-4 flex justify-between items-center shrink-0 border-b border-slate-200 shadow-sm">
        <div className="flex items-center gap-4">
          <button onClick={onClose} className="text-slate-400 hover:text-red-500 font-bold text-2xl transition">&times;</button>
          <h2 className="font-black text-lg text-[#0a5482] uppercase tracking-tight">📄 {testRecord.id === 'new' ? 'Tạo Đề Case Study' : 'Chỉnh Sửa Đề Case Study'}</h2>
        </div>
      </div>

      {/* CONTENT: 2 CỘT TỐI GIẢN */}
      <div className="flex-1 overflow-y-auto p-8">
        <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-8">
          
          {/* CỘT TRÁI: THÔNG TIN & UPLOAD */}
          <div className="space-y-6">
            <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 space-y-4">
              <h3 className="font-black text-slate-800 border-b border-slate-100 pb-3 mb-4 uppercase text-sm">1. Cài đặt hệ thống</h3>
              
              <div>
                <label className="text-[13px] font-bold text-slate-600 block mb-1">Tên đề thi <span className="text-red-500">*</span></label>
                <input value={testData.basicInfo.title} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, title: e.target.value}})} placeholder="Ví dụ: Business mock T4/2026" className="w-full p-3 bg-slate-50 border border-slate-200 rounded-xl outline-none focus:ring-2 focus:ring-[#0a5482] text-[14px]" />
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="text-[13px] font-bold text-slate-600 block mb-1">Thuộc Khóa học</label>
                  <select value={testData.basicInfo.courseId} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, courseId: e.target.value}})} className="w-full p-3 bg-slate-50 border border-slate-200 rounded-xl outline-none text-[14px]">
                    <option value="all">Dùng chung</option>
                    {courses?.map((c: any) => <option key={c.id} value={c.id}>{c.title}</option>)}
                  </select>
                </div>
                <div>
                  <label className="text-[13px] font-bold text-slate-600 block mb-1">Thời gian làm (phút)</label>
                  <input type="number" value={testData.basicInfo.timeLimit} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, timeLimit: e.target.value}})} className="w-full p-3 bg-slate-50 border border-slate-200 rounded-xl outline-none text-[14px]" />
                </div>
              </div>

              <div>
                <label className="text-[13px] font-bold text-slate-600 block mb-1">Cách tính điểm (AI)</label>
                <select value={testData.basicInfo.scoreType} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, scoreType: e.target.value}})} className="w-full p-3 bg-slate-50 border border-slate-200 rounded-xl outline-none text-[14px]">
                  <option value="IGCSE Grading">Điểm gốc ➔ Thang điểm IGCSE (A*, A, B...)</option>
                  <option value="1 điểm/ câu đúng">1 điểm/ câu đúng</option>
                </select>
              </div>
            </div>

            <div className="bg-blue-50 p-6 rounded-2xl shadow-sm border border-blue-200">
              <h3 className="font-black text-[#0a5482] border-b border-blue-200/50 pb-3 mb-4 uppercase text-sm">2. Tài liệu đính kèm</h3>
              <label className="text-[13px] font-bold text-slate-600 block mb-2">File PDF Case Study (Hiển thị nửa trái màn hình)</label>
              
              <div className="flex items-center gap-3 w-full">
                <label className="bg-white border border-slate-300 text-slate-700 px-5 py-3 rounded-xl text-[13px] font-bold cursor-pointer hover:bg-slate-100 transition shadow-sm shrink-0">
                  <input type="file" className="hidden" accept=".pdf" onChange={handleFileUpload} /> 
                  {uploading ? '⏳ Đang tải...' : '📁 Chọn tệp PDF'}
                </label>
                <span className="text-[13px] font-medium text-slate-500 truncate">
                  {testData.basicInfo.insert_pdf_url ? '✅ Đã tải lên thành công' : 'Chưa có file nào'}
                </span>
              </div>
            </div>
          </div>

          {/* CỘT PHẢI: MÃ JSON */}
          <div className="bg-slate-800 p-6 rounded-2xl shadow-lg border border-slate-700 flex flex-col h-[600px]">
            <div className="flex justify-between items-center mb-4">
              <h3 className="font-black text-emerald-400 uppercase text-sm flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> 3. Dán mã cấu trúc đề (JSON)</h3>
            </div>
            <textarea
              value={testData.json_config_string || ''}
              onChange={e => setTestData({...testData, json_config_string: e.target.value})}
              className="flex-1 w-full font-mono text-[13px] bg-slate-900/50 text-slate-300 border border-slate-600 p-4 rounded-xl outline-none focus:border-emerald-400 focus:ring-1 focus:ring-emerald-400 custom-scrollbar resize-none"
              spellCheck={false}
              placeholder={`{\n  "questions": [\n    {\n      "question_number": "1(a)",\n      "question_text": "Giải thích...",\n      "total_marks": 8,\n      "inputs": [{ "label": "Nhập đáp án:" }]\n    }\n  ]\n}`}
            />
          </div>

        </div>
      </div>

      <button onClick={handleSave} disabled={isSaving || uploading} className="fixed bottom-10 right-10 w-40 bg-[#00a651] hover:bg-[#008f45] text-white font-black py-4 rounded-2xl shadow-xl transition-transform active:scale-95 disabled:opacity-50 flex items-center justify-center gap-2">
        {isSaving ? '⏳ ĐANG LƯU...' : '💾 LƯU ĐỀ THI'}
      </button>

    </div>
  );
}