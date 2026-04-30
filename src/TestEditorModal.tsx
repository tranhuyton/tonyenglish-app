import React, { useState, useRef } from 'react';
import { supabase } from './supabase';
import * as XLSX from 'xlsx';

export default function TestEditorModal({ testData: testRecord, courses, onClose, onSave }: any) {
  const isImportMode = testRecord.mode === 'import'; 
  const [activeTab, setActiveTab] = useState(isImportMode ? 'content' : 'basic'); 
  
  const [isDraggingExcel, setIsDraggingExcel] = useState(false);
  const [uploadingId, setUploadingId] = useState<string | null>(null);

  const getInitialData = () => {
    if (testRecord.content_json) return {...testRecord.content_json};
    return {
      basicInfo: {
        title: testRecord.title || (isImportMode ? 'Đề thi Import từ Excel/CSV' : ''),
        courseId: 'all', 
        skill: testRecord.test_type || 'Standard-Test',
        mode: 'Đề thi',
        timeLimit: '40',
        scoreType: '1 điểm/ câu đúng',
      },
      parts: [] 
    };
  };

  const [testData, setTestData] = useState<any>(getInitialData());
  const [isSaving, setIsSaving] = useState(false);

  // ==========================================
  // 1. HÀM UPLOAD FILE CHUNG
  // ==========================================
  const uploadToSupabase = async (file: File) => {
    const fileExt = file.name ? file.name.split('.').pop() : 'png';
    const fileName = `media_${Date.now()}_${Math.random().toString(36).substring(7)}.${fileExt}`;
    const { error } = await supabase.storage.from('test_assets').upload(`uploads/${fileName}`, file, { cacheControl: '3600', upsert: false });
    if (error) throw error;
    return supabase.storage.from('test_assets').getPublicUrl(`uploads/${fileName}`).data.publicUrl;
  };

  // ==========================================
  // 2. THUẬT TOÁN ĐỌC EXCEL/CSV (SIÊU NHẠY)
  // ==========================================
  const processExcelFile = async (file: File) => {
    setUploadingId('excel');
    const reader = new FileReader();
    
    reader.onload = (e) => {
      try {
        // Dùng ArrayBuffer để chống lỗi font chữ tiếng Việt của file CSV
        const data = new Uint8Array(e.target?.result as ArrayBuffer);
        const workbook = XLSX.read(data, { type: 'array' });
        const firstSheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[firstSheetName];
        const jsonData = XLSX.utils.sheet_to_json(worksheet, { defval: "" });

        if (jsonData.length === 0) {
          alert("⚠️ File trống hoặc không đúng định dạng.");
          setUploadingId(null);
          return;
        }

        let newParts: any[] = [];
        let currentPart: any = null;
        let currentSection: any = null;
        let importCount = 0;

        // Hàm dò tìm tên cột thông minh (Bỏ qua viết hoa, viết thường, dấu cách)
        const getCol = (row: any, keywords: string[]) => {
          const keys = Object.keys(row);
          for (let key of keys) {
            const cleanKey = key.toLowerCase().replace(/[^a-z0-9]/g, '');
            if (keywords.some(k => cleanKey.includes(k))) return row[key];
          }
          return "";
        };

        jsonData.forEach((row: any) => {
          const partTitle = getCol(row, ['part']) || 'Part 1';
          const secTitle = getCol(row, ['section', 'nhóm', 'đoạn']) || 'Section 1';
          const qContent = getCol(row, ['question', 'câu', 'nộidung']);
          const optA = getCol(row, ['optiona', 'đápána', 'lựachọna']);
          const optB = getCol(row, ['optionb', 'đápánb', 'lựachọnb']);
          const optC = getCol(row, ['optionc', 'đápánc', 'lựachọnc']);
          const optD = getCol(row, ['optiond', 'đápánd', 'lựachọnd']);
          const answer = getCol(row, ['correct', 'answer', 'đápánđúng']);
          const exp = getCol(row, ['explanation', 'giảithích']);

          if (!qContent && !optA && !partTitle) return; // Bỏ qua dòng trống

          // 1. Tạo Part
          if (!currentPart || currentPart.title !== partTitle) {
            currentPart = { id: Date.now().toString() + Math.random(), title: partTitle, content: '', tags: '', audioUrl: '', explanation: '', sections: [] };
            newParts.push(currentPart);
            currentSection = null; 
          }

          // 2. Tạo Section
          if (!currentSection || currentSection.title !== secTitle) {
            currentSection = { id: Date.now().toString() + Math.random(), title: secTitle, content: '', tags: '', questionType: 'Trắc nghiệm', audioUrl: '', explanation: '', questions: [] };
            currentPart.sections.push(currentSection);
          }

          // 3. Tạo Question
          if (qContent || optA) {
            const options = [];
            if (optA) options.push(optA.toString());
            if (optB) options.push(optB.toString());
            if (optC) options.push(optC.toString());
            if (optD) options.push(optD.toString());

            currentSection.questions.push({
              id: Date.now().toString() + Math.random(),
              content: qContent.toString(),
              tags: '',
              audioUrl: '',
              explanation: exp.toString(),
              options: options.length > 0 ? options : ['A', 'B', 'C', 'D'],
              correctAnswer: answer.toString()
            });
            importCount++;
          }
        });

        if (newParts.length > 0) {
          setTestData((prev: any) => ({ ...prev, parts: [...prev.parts, ...newParts] }));
          alert(`🎉 Bóc tách thành công ${importCount} câu hỏi! Anh cuộn xuống dưới để xem nhé.`);
        } else {
          alert("⚠️ Không tìm thấy câu hỏi nào hợp lệ. Anh kiểm tra lại tên các cột trong file.");
        }
      } catch (err) {
        alert("❌ Lỗi hệ thống khi đọc file. Hãy chắc chắn file không bị lỗi định dạng.");
      } finally {
        setUploadingId(null);
      }
    };
    reader.readAsArrayBuffer(file);
  };

  const handleExcelDrop = (e: React.DragEvent) => {
    e.preventDefault(); setIsDraggingExcel(false);
    if (e.dataTransfer.files?.[0]) processExcelFile(e.dataTransfer.files[0]);
  };

  const handleExcelUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files?.[0]) {
      processExcelFile(e.target.files[0]);
      e.target.value = ''; // Reset để chọn lại file cũ nếu cần
    }
  };

  // ==========================================
  // 3. GIAO DIỆN HỖ TRỢ CHÈN ẢNH VÀ AUDIO TRỰC TIẾP
  // ==========================================
  
  // Nút chèn ảnh và ô Text hỗ trợ Paste
  const RichFieldRow = ({ label, value, onChange, placeholder = "" }: any) => {
    const fileInputRef = useRef<HTMLInputElement>(null);
    const [isUploading, setIsUploading] = useState(false);

    const appendImageToText = async (file: File) => {
      setIsUploading(true);
      try {
        const url = await uploadToSupabase(file);
        const newText = (value || '') + `\n<img src="${url}" alt="image" style="max-width:100%; border-radius:8px; margin: 10px 0;"/>\n`;
        onChange({ target: { value: newText } });
      } catch (err) {
        alert("Lỗi tải ảnh!");
      } finally {
        setIsUploading(false);
      }
    };

    const handlePaste = (e: React.ClipboardEvent<HTMLTextAreaElement>) => {
      const items = e.clipboardData.items;
      for (let i = 0; i < items.length; i++) {
        if (items[i].type.indexOf('image') !== -1) {
          e.preventDefault();
          const file = items[i].getAsFile();
          if (file) appendImageToText(file);
        }
      }
    };

    return (
      <div className="flex flex-col py-3 border-b border-slate-100 last:border-0 gap-2">
        <div className="flex justify-between items-center">
          <label className="text-[13px] font-bold text-slate-600">{label}</label>
          <button 
            onClick={() => fileInputRef.current?.click()} 
            className="text-[12px] bg-slate-100 hover:bg-slate-200 text-slate-700 px-3 py-1.5 rounded-lg border border-slate-300 transition flex items-center gap-1.5 font-bold shadow-sm active:scale-95"
          >
            {isUploading ? '⏳ Đang tải...' : '📷 Chèn ảnh/Hình'}
          </button>
          <input type="file" accept="image/*" className="hidden" ref={fileInputRef} onChange={(e) => { if(e.target.files?.[0]) appendImageToText(e.target.files[0]); }} />
        </div>
        <textarea 
          value={value || ''} 
          onChange={onChange} 
          onPaste={handlePaste}
          placeholder={placeholder + " (Anh có thể ấn Ctrl+V để dán trực tiếp ảnh vào đây)"} 
          className="w-full bg-slate-50 hover:bg-white focus:bg-white border border-slate-200 rounded-lg p-3 text-[14px] focus:border-[#00a651] outline-none transition min-h-[100px] custom-scrollbar" 
        />
      </div>
    );
  };

  // Nút Audio đính kèm
  const MediaRow = ({ label, value, onUpload, id, accept = "audio/*, image/*" }: any) => {
    const [isDrag, setIsDrag] = useState(false);
    const handleFile = async (file: File) => {
      setUploadingId(id);
      try {
        const url = await uploadToSupabase(file);
        onUpload(url);
      } catch (err) { alert("Lỗi tải file!"); }
      finally { setUploadingId(null); }
    };

    return (
      <div className="flex flex-col py-3 border-b border-slate-100 last:border-0 gap-2">
        <label className="text-[13px] font-bold text-slate-600">{label}</label>
        <div 
          className={`w-full border-2 border-dashed rounded-lg p-4 flex items-center justify-between transition ${isDrag ? 'border-[#00a651] bg-[#e6f4ea]' : 'border-slate-300 bg-slate-50'}`}
          onDragOver={(e) => { e.preventDefault(); setIsDrag(true); }}
          onDragLeave={(e) => { e.preventDefault(); setIsDrag(false); }}
          onDrop={(e) => { e.preventDefault(); setIsDrag(false); if(e.dataTransfer.files?.[0]) handleFile(e.dataTransfer.files[0]); }}
        >
          <div className="flex items-center gap-3">
            <span className="text-2xl">{value ? '✅' : '🎵'}</span>
            <div className="text-[13px] text-slate-500">
              {uploadingId === id ? <span className="text-amber-500 font-bold">⏳ Đang tải lên...</span> : 
               value ? <span className="text-emerald-600 font-bold truncate block max-w-[200px]">Đã có file đính kèm</span> : 
               <span>Kéo thả file Âm thanh vào đây</span>}
            </div>
          </div>
          <label className="bg-white border border-slate-300 text-slate-700 px-4 py-2 rounded-lg text-[12px] font-bold cursor-pointer hover:bg-slate-100 transition shadow-sm">
            <input type="file" className="hidden" accept={accept} onChange={(e) => { if(e.target.files?.[0]) handleFile(e.target.files[0]); }} /> 
            Tải lên
          </label>
        </div>
      </div>
    );
  };

  // Các thẻ input Text bình thường (Tiêu đề, Tags...)
  const FieldRow = ({ label, value, onChange, placeholder = "" }: any) => (
    <div className="flex flex-col md:flex-row items-start md:items-center py-3 border-b border-slate-100 last:border-0 gap-2">
      <label className="w-32 shrink-0 text-[13px] font-bold text-slate-600">{label}</label>
      <input type="text" value={value || ''} onChange={onChange} placeholder={placeholder} className="flex-1 w-full bg-slate-50 hover:bg-white focus:bg-white border border-slate-200 rounded-lg p-2.5 text-[14px] focus:border-[#00a651] outline-none transition" />
    </div>
  );

  // ==========================================
  // 4. HÀM QUẢN LÝ THÊM SỬA XÓA MẢNG
  // ==========================================
  const addPart = () => {
    const newData = { ...testData };
    if (!newData.parts) newData.parts = [];
    newData.parts.push({ id: Date.now().toString(), title: `Part ${newData.parts.length + 1}`, content: '', tags: '', audioUrl: '', explanation: '', sections: [] });
    setTestData(newData);
  };
  const removePart = (pIdx: number) => {
    const newData = { ...testData }; newData.parts.splice(pIdx, 1); setTestData(newData);
  };

  const addSection = (pIdx: number) => {
    const newData = { ...testData };
    if (!newData.parts[pIdx].sections) newData.parts[pIdx].sections = [];
    newData.parts[pIdx].sections.push({ id: Date.now().toString(), title: `Section ${newData.parts[pIdx].sections.length + 1}`, content: '', tags: '', questionType: 'Kéo thả vào Part', audioUrl: '', explanation: '', questions: [] });
    setTestData(newData);
  };
  const removeSection = (pIdx: number, sIdx: number) => {
    const newData = { ...testData }; newData.parts[pIdx].sections.splice(sIdx, 1); setTestData(newData);
  };

  const addQuestion = (pIdx: number, sIdx: number) => {
    const newData = { ...testData };
    if (!newData.parts[pIdx].sections[sIdx].questions) newData.parts[pIdx].sections[sIdx].questions = [];
    newData.parts[pIdx].sections[sIdx].questions.push({ id: Date.now().toString(), content: '', tags: '', audioUrl: '', explanation: '', options: ['A', 'B', 'C', 'D'], correctAnswer: '' });
    setTestData(newData);
  };
  const removeQuestion = (pIdx: number, sIdx: number, qIdx: number) => {
    const newData = { ...testData }; newData.parts[pIdx].sections[sIdx].questions.splice(qIdx, 1); setTestData(newData);
  };

  const addOption = (pIdx: number, sIdx: number, qIdx: number) => {
    const newData = { ...testData }; 
    if (!newData.parts[pIdx].sections[sIdx].questions[qIdx].options) newData.parts[pIdx].sections[sIdx].questions[qIdx].options = [];
    newData.parts[pIdx].sections[sIdx].questions[qIdx].options.push(''); 
    setTestData(newData);
  };
  const removeOption = (pIdx: number, sIdx: number, qIdx: number, oIdx: number) => {
    const newData = { ...testData }; newData.parts[pIdx].sections[sIdx].questions[qIdx].options.splice(oIdx, 1); setTestData(newData);
  };

  const updateField = (path: number[], field: string, value: any) => {
    const newData = { ...testData };
    if (path.length === 1) newData.parts[path[0]][field] = value;
    else if (path.length === 2) newData.parts[path[0]].sections[path[1]][field] = value;
    else if (path.length === 3) newData.parts[path[0]].sections[path[1]].questions[path[2]][field] = value;
    setTestData(newData);
  };

  const updateOption = (pIdx: number, sIdx: number, qIdx: number, oIdx: number, value: string) => {
    const newData = { ...testData }; newData.parts[pIdx].sections[sIdx].questions[qIdx].options[oIdx] = value; setTestData(newData);
  };

  const handleSave = () => { setIsSaving(true); onSave(testData); };

  return (
    <div className="fixed inset-0 bg-[#f0f2f5] z-[60] flex flex-col animate-in fade-in">
      <div className="bg-white px-6 py-3 flex justify-between items-center shrink-0 border-b border-slate-200 shadow-sm relative z-20">
        <div className="flex items-center gap-3">
          <button onClick={onClose} className="text-slate-500 hover:text-slate-800 font-bold text-xl transition">←</button>
          <h2 className="font-black text-[15px] text-slate-800 uppercase tracking-tight">{isImportMode ? 'Import Đề Thi Bằng Excel/CSV' : 'Soạn Thảo Đề Thi'}</h2>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto relative custom-scrollbar">
        <div className="max-w-[1200px] mx-auto w-full p-4 md:p-8 space-y-8 pb-20"> 
          <div className="flex flex-col md:flex-row gap-4 mb-6">
            <button onClick={() => setActiveTab('basic')} className={`w-full md:w-1/2 py-3 rounded-t-xl font-black text-sm uppercase tracking-widest transition-all border-b-4 ${activeTab === 'basic' ? 'bg-white border-[#00a651] text-[#00a651] shadow-sm' : 'bg-slate-200/50 border-transparent text-slate-400 hover:bg-slate-200'}`}>Thông tin chính</button>
            <button onClick={() => setActiveTab('content')} className={`w-full md:w-1/2 py-3 rounded-t-xl font-black text-sm uppercase tracking-widest transition-all border-b-4 ${activeTab === 'content' ? 'bg-white border-[#00a651] text-[#00a651] shadow-sm' : 'bg-slate-200/50 border-transparent text-slate-400 hover:bg-slate-200'}`}>Cài đặt & Nội dung đề</button>
          </div>

          {activeTab === 'basic' && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-start animate-in slide-in-from-left-4">
              <div className="bg-white rounded-xl overflow-hidden border border-slate-200 shadow-sm p-6 space-y-5">
                <h3 className="font-black text-[#00a651] border-b border-slate-100 pb-2 mb-4 uppercase text-[13px]">Thông tin chính</h3>
                <div>
                  <label className="text-[12px] font-bold text-slate-600 block mb-1">Tên đề <span className="text-red-500">*</span></label>
                  <input value={testData.basicInfo.title} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, title: e.target.value}})} placeholder="Ví dụ: Đề thi tiếng Anh 10" className="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none focus:border-[#00a651] text-[14px] transition" />
                </div>
              </div>

              <div className="bg-white rounded-xl overflow-hidden border border-slate-200 shadow-sm p-6 space-y-5">
                <h3 className="font-black text-[#00a651] border-b border-slate-100 pb-2 mb-4 uppercase text-[13px]">Cài đặt hệ thống</h3>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="text-[12px] font-bold text-slate-600 block mb-1">Thuộc Khóa học</label>
                    <select value={testData.basicInfo.courseId} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, courseId: e.target.value}})} className="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] transition">
                      <option value="all">Dùng chung</option>
                      {courses?.map((c: any) => <option key={c.id} value={c.id}>{c.title}</option>)}
                    </select>
                  </div>
                  <div>
                    <label className="text-[12px] font-bold text-slate-600 block mb-1">Kỹ năng / Dạng đề</label>
                    <select value={testData.basicInfo.skill} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, skill: e.target.value}})} className="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] transition">
                      <option value="IELTS-Listening">Listening (IELTS)</option>
                      <option value="IELTS-Reading">Reading (IELTS)</option>
                      <option value="Standard-Listening">Listening (Standard)</option>
                      <option value="Standard-Reading">Reading (Standard)</option>
                    </select>
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="text-[12px] font-bold text-slate-600 block mb-1">Thời gian làm (phút)</label>
                    <input type="number" value={testData.basicInfo.timeLimit} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, timeLimit: e.target.value}})} className="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] transition" />
                  </div>
                  <div>
                    <label className="text-[12px] font-bold text-slate-600 block mb-1">Cách tính điểm</label>
                    <select value={testData.basicInfo.scoreType} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, scoreType: e.target.value}})} className="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] transition">
                      <option value="1 điểm/ câu đúng">1 điểm/ câu đúng</option>
                      <option value="IELTS Band Score">IELTS Band Score</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'content' && (
            <div className="animate-in slide-in-from-right-4 space-y-6">
              
              {/* --- KHU VỰC KÉO THẢ EXCEL CHUẨN --- */}
              {isImportMode && (
                <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                  <div className="flex justify-between items-center border-b border-slate-100 pb-3 mb-4">
                     <h3 className="font-black text-[#0a5482] uppercase text-sm">📥 Nhập dữ liệu từ Excel/CSV</h3>
                  </div>

                  <div 
                    className={`w-full mt-2 border-2 border-dashed rounded-xl p-8 flex flex-col items-center justify-center transition-colors ${isDraggingExcel ? 'border-[#0a5482] bg-blue-50' : 'border-slate-300 bg-slate-50 hover:bg-slate-100'}`}
                    onDragOver={handleDragOverExcel}
                    onDragLeave={handleDragLeaveExcel}
                    onDrop={handleExcelDrop}
                  >
                    <span className="text-5xl mb-3 opacity-50">📊</span>
                    <p className="text-[15px] font-bold text-slate-700 mb-1">Kéo thả file Excel/CSV vào đây</p>
                    <p className="text-[13px] font-medium text-slate-400 mb-4">hoặc</p>
                    
                    <label className="bg-[#00a651] hover:bg-[#008f45] text-white px-8 py-3 rounded-xl text-[14px] font-bold cursor-pointer shadow-md transition active:scale-95">
                      <input type="file" className="hidden" accept=".xlsx, .xls, .csv" onChange={handleExcelUpload} /> 
                      {uploadingId === 'excel' ? '⏳ Đang phân tích...' : 'Duyệt tệp trong máy'}
                    </label>
                  </div>
                </div>
              )}

              {/* VÒNG LẶP RENDER CẤU TRÚC ĐỀ */}
              {testData.parts?.map((part: any, pIdx: number) => (
                <div key={part.id} className="border-2 border-[#00a651] rounded-2xl bg-white overflow-hidden shadow-sm">
                    <div className="bg-[#e6f4ea] px-6 py-4 border-b border-[#00a651]/20 flex justify-between items-center group">
                      <input value={part.title} onChange={(e) => updateField([pIdx], 'title', e.target.value)} className="font-black text-[#00a651] text-xl bg-transparent outline-none border-b border-dashed border-[#00a651]/50 focus:border-[#00a651] w-64" placeholder="Part Title..." />
                      <button onClick={() => removePart(pIdx)} className="text-red-500 font-bold px-3 py-1 bg-red-50 rounded-lg opacity-0 group-hover:opacity-100 transition hover:bg-red-500 hover:text-white">Xóa Part ✖</button>
                    </div>
                    
                    <div className="p-6 md:p-8 space-y-4 bg-slate-50 border-b border-slate-200">
                      <RichFieldRow label="Nội dung Part (Bài đọc/Giới thiệu)" value={part.content} onChange={(e:any) => updateField([pIdx], 'content', e.target.value)} />
                      <MediaRow label="File Âm thanh Part" value={part.audioUrl} id={`part-${part.id}`} onUpload={(url: string) => updateField([pIdx], 'audioUrl', url)} />
                    </div>

                    <div className="p-6 md:p-8 space-y-8">
                      {part.sections?.map((sec: any, sIdx: number) => (
                        <div key={sec.id} className="border-2 border-[#3b82f6] rounded-xl bg-white overflow-hidden shadow-sm">
                          <div className="bg-[#3b82f6] px-6 py-3 flex justify-between items-center group">
                            <input value={sec.title} onChange={(e) => updateField([pIdx, sIdx], 'title', e.target.value)} className="font-black text-white text-base bg-transparent outline-none border-b border-dashed border-white/50 focus:border-white w-64 placeholder:text-white/60" placeholder="Section Title..." />
                            <button onClick={() => removeSection(pIdx, sIdx)} className="text-white hover:text-red-200 font-bold opacity-0 group-hover:opacity-100 transition">✖</button>
                          </div>
                          
                          <div className="p-6 bg-blue-50/30 border-b border-blue-100 space-y-4">
                            <RichFieldRow label="Nội dung Section (Đoạn văn/Hướng dẫn)" value={sec.content} onChange={(e:any) => updateField([pIdx, sIdx], 'content', e.target.value)} />
                            <div className="flex flex-col md:flex-row items-start md:items-center py-3 border-b border-slate-100 gap-2">
                              <label className="w-32 shrink-0 text-[13px] font-bold text-slate-600">Kiểu làm</label>
                              <select value={sec.questionType} onChange={(e) => updateField([pIdx, sIdx], 'questionType', e.target.value)} className="flex-1 w-full bg-white border border-slate-200 rounded-lg p-2.5 text-[14px] text-slate-700 outline-none focus:border-[#3b82f6] transition">
                                <option value="Kéo thả vào Part">Kéo thả vào Part</option>
                                <option value="Trắc nghiệm">Trắc nghiệm</option>
                                <option value="Điền từ">Điền từ</option>
                              </select>
                            </div>
                            <MediaRow label="File Âm thanh Section" value={sec.audioUrl} id={`sec-${sec.id}`} onUpload={(url: string) => updateField([pIdx, sIdx], 'audioUrl', url)} />
                          </div>

                          <div className="p-6 space-y-6">
                            {sec.questions?.map((q: any, qIdx: number) => (
                              <div key={q.id} className="border border-slate-200 rounded-xl bg-white shadow-sm hover:border-amber-300 transition group relative">
                                <button onClick={() => removeQuestion(pIdx, sIdx, qIdx)} className="absolute -top-3 -right-3 bg-red-500 text-white w-7 h-7 rounded-full opacity-0 group-hover:opacity-100 transition shadow-lg z-10">✖</button>
                                
                                <div className="p-5">
                                    <div className="flex gap-4 items-start">
                                      <div className="w-10 h-10 shrink-0 bg-amber-100 text-amber-700 font-black rounded-full flex items-center justify-center border border-amber-200">
                                        {qIdx + 1}
                                      </div>
                                      <div className="flex-1 space-y-4">
                                        <RichFieldRow label="Nội dung câu hỏi" value={q.content} onChange={(e:any) => updateField([pIdx, sIdx, qIdx], 'content', e.target.value)} />
                                        
                                        <div className="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-3">
                                          <label className="text-[12px] font-bold text-slate-600 block border-b border-slate-200 pb-2">Các lựa chọn đáp án</label>
                                          {q.options?.map((opt: string, oIdx: number) => (
                                            <div key={oIdx} className="flex items-center gap-3">
                                              <div className="w-8 h-8 rounded-full bg-white border border-slate-300 text-slate-600 font-black text-[12px] flex items-center justify-center shrink-0 shadow-sm">{String.fromCharCode(65+oIdx)}</div>
                                              <input value={opt || ''} onChange={(e) => updateOption(pIdx, sIdx, qIdx, oIdx, e.target.value)} placeholder="Nhập đáp án..." className="flex-1 bg-white border border-slate-200 rounded-lg p-2.5 text-[14px] outline-none focus:border-[#0a5482] transition" />
                                              <button onClick={() => removeOption(pIdx, sIdx, qIdx, oIdx)} className="text-slate-300 hover:text-red-500 font-bold px-2 py-1 text-lg">×</button>
                                            </div>
                                          ))}
                                          <button onClick={() => addOption(pIdx, sIdx, qIdx)} className="text-[#0a5482] text-[12px] font-bold mt-2 hover:underline">+ Thêm lựa chọn (A, B, C, D...)</button>
                                        </div>

                                        <div className="flex gap-4">
                                          <div className="flex-1">
                                            <FieldRow label="Lời giải thích" value={q.explanation} onChange={(e:any) => updateField([pIdx, sIdx, qIdx], 'explanation', e.target.value)} placeholder="Giải thích vì sao đúng..." />
                                          </div>
                                          <div className="shrink-0 w-32">
                                            <label className="text-[12px] font-bold text-slate-600 block mb-1">Đáp án đúng (VD: A)</label>
                                            <input value={q.correctAnswer || ''} onChange={(e) => updateField([pIdx, sIdx, qIdx], 'correctAnswer', e.target.value)} className="w-full bg-emerald-50 border border-emerald-200 text-emerald-700 font-black text-center rounded-lg p-2.5 outline-none focus:ring-2 focus:ring-emerald-400" />
                                          </div>
                                        </div>
                                      </div>
                                    </div>
                                </div>
                              </div>
                            ))}
                            <button onClick={() => addQuestion(pIdx, sIdx)} className="w-full border-2 border-dashed border-slate-300 text-slate-500 hover:border-[#00a651] hover:text-[#00a651] hover:bg-[#e6f4ea] py-4 rounded-xl font-bold transition flex justify-center items-center gap-2">
                              <span className="text-xl">+</span> Thêm Câu Hỏi Mới
                            </button>
                          </div>
                        </div>
                      ))}
                      <button onClick={() => addSection(pIdx)} className="bg-[#3b82f6] hover:bg-[#2563eb] text-white px-6 py-2.5 rounded-full text-[13px] font-bold shadow-md">+ Thêm Section Mới</button>
                    </div>
                </div>
              ))}
              
              {(!isImportMode || testData.parts?.length > 0) && (
                <div className="flex justify-center pt-8 border-t-2 border-dashed border-slate-200 pb-10">
                    <button onClick={addPart} className="bg-[#00a651] hover:bg-[#008f45] text-white px-10 py-4 rounded-full text-[15px] font-black shadow-lg hover:scale-105 transition-transform">+ THÊM PART MỚI</button>
                </div>
              )}
            </div>
          )}
        </div>
      </div>

      <button onClick={handleSave} disabled={isSaving} className="fixed bottom-10 right-10 w-20 h-20 bg-[#2bd6eb] hover:bg-[#1bc1d6] text-white rounded-full shadow-[0_10px_25px_rgba(43,214,235,0.4)] flex flex-col items-center justify-center z-[100] transition-all hover:scale-110 active:scale-95 disabled:opacity-50 disabled:hover:scale-100">
        <span className="text-[26px] mb-0.5">{isSaving ? '⏳' : '💾'}</span>
        <span className="text-[10px] font-black uppercase tracking-wider">{isSaving ? 'Đang lưu' : 'Lưu Đề'}</span>
      </button>
    </div>
  );
}