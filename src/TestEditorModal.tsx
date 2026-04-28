import React, { useState } from 'react';
import { supabase } from './supabase';
import * as XLSX from 'xlsx';

export default function TestEditorModal({ testData: testRecord, courses, folders, onClose, onSave }: any) {
  const isImportMode = testRecord.mode === 'import'; 
  const [activeTab, setActiveTab] = useState<'basic' | 'content'>('basic'); 
  
  const getInitialData = () => {
    const baseData = testRecord.content_json || {
      basicInfo: {
        title: testRecord.title || '',
        thumbnail: '',
        skill: testRecord.test_type || 'IELTS-Reading',
        mode: 'Đề thi',
        timeLimit: '40',
        scoreType: '1 điểm/ câu đúng',
        limit: ''
      },
      parts: isImportMode ? [] : [
        {
          id: Date.now().toString(), title: 'Part 1', content: '', tags: '', audioUrl: '', imageUrl: '', explanation: '',
          sections: [
            {
              id: (Date.now()+1).toString(), title: 'Section 1', content: '', tags: '', questionType: 'Trắc nghiệm', audioUrl: '', imageUrl: '', explanation: '',
              questions: [
                { id: (Date.now()+2).toString(), content: '', tags: '', audioUrl: '', imageUrl: '', explanation: '', options: ['A', 'B', 'C', 'D'], correctAnswer: '' }
              ]
            }
          ]
        }
      ]
    };
    return { ...baseData, folder_id: testRecord.folder_id || '' };
  };

  const [testData, setTestData] = useState<any>(getInitialData());
  const [isSaving, setIsSaving] = useState(false);
  const [uploadingId, setUploadingId] = useState<string | null>(null);

  // --- HÀM IMPORT EXCEL ---
  const handleImportExcel = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (evt) => {
      try {
        const bstr = evt.target?.result;
        const wb = XLSX.read(bstr, { type: 'binary' });
        const wsname = wb.SheetNames[0];
        const ws = wb.Sheets[wsname];
        const rows = XLSX.utils.sheet_to_json(ws) as any[];

        if (rows.length === 0) {
          alert("File Excel trống hoặc không đúng định dạng!");
          return;
        }

        const importedPartId = Date.now().toString();
        const importedSecId = (Date.now() + 1).toString();

        const importedQuestions = rows.map((row, index) => {
          const content = row['Question'] || row['Câu hỏi'] || row['Nội dung'] || `Câu hỏi ${index + 1}`;
          const optA = row['Option A'] || row['A'] || row['Đáp án A'] || '';
          const optB = row['Option B'] || row['B'] || row['Đáp án B'] || '';
          const optC = row['Option C'] || row['C'] || row['Đáp án C'] || '';
          const optD = row['Option D'] || row['D'] || row['Đáp án D'] || '';
          const correctAns = row['Answer'] || row['Đáp án'] || row['Correct Answer'] || '';
          const explain = row['Explanation'] || row['Giải thích'] || '';

          const options = [optA, optB, optC, optD].filter(o => o !== '');

          return {
            id: (Date.now() + index + 2).toString(),
            content: content,
            tags: 'Imported',
            audioUrl: '',
            imageUrl: '',
            explanation: explain,
            options: options.length > 0 ? options : ['A', 'B', 'C', 'D'],
            correctAnswer: correctAns ? correctAns.toString().trim().toUpperCase() : ''
          };
        });

        const newPart = {
          id: importedPartId,
          title: 'Part 1 (Imported từ Excel)',
          content: '',
          tags: '',
          audioUrl: '',
          imageUrl: '',
          explanation: '',
          sections: [
            {
              id: importedSecId,
              title: 'Section 1',
              content: 'Danh sách câu hỏi được hệ thống tự động bóc tách từ file của bạn.',
              tags: '',
              questionType: 'Trắc nghiệm',
              audioUrl: '',
              imageUrl: '',
              explanation: '',
              questions: importedQuestions
            }
          ]
        };

        setTestData({ ...testData, parts: [newPart] });
        alert(`🎉 Import thành công ${importedQuestions.length} câu hỏi! Vui lòng cuộn xuống để kiểm tra lại.`);
        
      } catch (error) {
        console.error(error);
        alert("Lỗi khi đọc file. Vui lòng đảm bảo file Excel/CSV không bị lỗi.");
      }
    };
    reader.readAsBinaryString(file);
    e.target.value = '';
  };

  const uploadToSupabase = async (file: File) => {
    const fileExt = file.name ? file.name.split('.').pop() : 'png';
    const fileName = `media_${Date.now()}_${Math.random().toString(36).substring(7)}.${fileExt}`;
    const { error } = await supabase.storage.from('test_assets').upload(`uploads/${fileName}`, file, { cacheControl: '3600', upsert: false });
    if (error) throw error;
    return supabase.storage.from('test_assets').getPublicUrl(`uploads/${fileName}`).data.publicUrl;
  };

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>, updateCallback: (url: string) => void, id: string) => {
    const file = e.target.files?.[0];
    if (file) {
      setUploadingId(id);
      try {
        const url = await uploadToSupabase(file);
        updateCallback(url);
      } catch (error: any) { alert("Lỗi upload: " + error.message); } 
      finally { setUploadingId(null); }
    }
  };

  const handlePasteImage = async (e: React.ClipboardEvent<HTMLDivElement>, updateCallback: (url: string) => void, id: string) => {
    const items = e.clipboardData?.items;
    if (!items) return;
    for (let i = 0; i < items.length; i++) {
      if (items[i].type.indexOf('image') !== -1) {
        const file = items[i].getAsFile();
        if (file) {
          e.preventDefault();
          setUploadingId(id);
          try {
            const url = await uploadToSupabase(file);
            updateCallback(url);
          } catch (err: any) { alert("Lỗi tải ảnh: " + err.message); }
          finally { setUploadingId(null); }
        }
      }
    }
  };

  const addPart = () => { setTestData({ ...testData, parts: [...testData.parts, { id: Date.now().toString(), title: `Part ${testData.parts.length + 1}`, content: '', tags: '', audioUrl: '', imageUrl: '', explanation: '', sections: [] }] }); };
  const removePart = (pIdx: number) => { const newData = { ...testData }; newData.parts.splice(pIdx, 1); setTestData(newData); };
  const addSection = (pIdx: number) => { const newData = { ...testData }; newData.parts[pIdx].sections.push({ id: Date.now().toString(), title: `Section ${newData.parts[pIdx].sections.length + 1}`, content: '', tags: '', questionType: 'Trắc nghiệm', audioUrl: '', imageUrl: '', explanation: '', questions: [] }); setTestData(newData); };
  const removeSection = (pIdx: number, sIdx: number) => { const newData = { ...testData }; newData.parts[pIdx].sections.splice(sIdx, 1); setTestData(newData); };
  const addQuestion = (pIdx: number, sIdx: number) => { const newData = { ...testData }; newData.parts[pIdx].sections[sIdx].questions.push({ id: Date.now().toString(), content: '', tags: '', audioUrl: '', imageUrl: '', explanation: '', options: ['A', 'B', 'C', 'D'], correctAnswer: '' }); setTestData(newData); };
  const removeQuestion = (pIdx: number, sIdx: number, qIdx: number) => { const newData = { ...testData }; newData.parts[pIdx].sections[sIdx].questions.splice(qIdx, 1); setTestData(newData); };
  const addOption = (pIdx: number, sIdx: number, qIdx: number) => { const newData = { ...testData }; newData.parts[pIdx].sections[sIdx].questions[qIdx].options.push(''); setTestData(newData); };
  const removeOption = (pIdx: number, sIdx: number, qIdx: number, oIdx: number) => { const newData = { ...testData }; newData.parts[pIdx].sections[sIdx].questions[qIdx].options.splice(oIdx, 1); setTestData(newData); };
  
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

  const handleSave = () => {
    if (!testData.folder_id) {
      alert("⚠️ LỖI: Vui lòng chọn [Thuộc Danh mục] trước khi lưu đề thi! Đề thi bắt buộc phải nằm trong một thư mục của khóa học.");
      setActiveTab('basic'); 
      return;
    }
    setIsSaving(true);
    onSave(testData); 
  };

  const FieldRow = ({ label, value, onChange, placeholder = "", isTextArea = false }: any) => (
    <div className="flex flex-col lg:flex-row items-start lg:items-center py-3 border-b border-slate-100 last:border-0 gap-2">
      <label className="w-32 shrink-0 text-[13px] font-medium text-slate-500">{label}</label>
      {isTextArea ? (
        <textarea value={value} onChange={onChange} placeholder={placeholder} rows={3} className="flex-1 w-full bg-slate-50 border border-slate-200 rounded-lg p-2.5 text-[14px] focus:border-[#00a651] focus:bg-white outline-none transition custom-scrollbar" />
      ) : (
        <input type="text" value={value} onChange={onChange} placeholder={placeholder} className="flex-1 w-full bg-slate-50 border border-slate-200 rounded-lg p-2.5 text-[14px] focus:border-[#00a651] focus:bg-white outline-none transition" />
      )}
    </div>
  );

  const FileRow = ({ label, value, onUpload, id, accept }: any) => (
    <div className="flex flex-col lg:flex-row items-start lg:items-center py-3 border-b border-slate-100 last:border-0 gap-2">
      <label className="w-32 shrink-0 text-[13px] font-medium text-slate-500">{label}</label>
      <div className="flex items-center gap-3 flex-1 w-full">
        <label className="bg-slate-50 border border-slate-200 text-slate-600 px-4 py-2 rounded-lg text-[13px] cursor-pointer hover:bg-slate-100 transition shadow-sm">
          <input type="file" className="hidden" accept={accept} onChange={(e) => handleFileUpload(e, onUpload, id)} /> 
          {uploadingId === id ? '⏳ Đang tải...' : 'Chọn tệp'}
        </label>
        <span className="text-[12px] text-slate-400 truncate flex-1">{value ? '✅ Đã tải lên' : 'Không có tệp... được chọn'}</span>
      </div>
    </div>
  );

  const ImagePasteRow = ({ label, value, onUpload, id }: any) => (
    <div className="flex flex-col lg:flex-row items-start py-3 border-b border-slate-100 gap-2">
      <label className="w-32 shrink-0 text-[13px] font-medium text-slate-500 pt-2">{label}</label>
      <div className="flex-1 w-full">
        {value ? (
          <div className="relative inline-block group">
            <img src={value} className="max-h-40 rounded-lg border border-slate-200 shadow-sm" alt="Uploaded" />
            <button onClick={() => onUpload('')} className="absolute -top-2 -right-2 bg-red-500 hover:bg-red-600 text-white rounded-full w-6 h-6 flex items-center justify-center text-xs opacity-0 group-hover:opacity-100 transition-opacity shadow-md">✕</button>
          </div>
        ) : (
          <div 
            onPaste={(e) => handlePasteImage(e, onUpload, id)}
            className="w-full border-2 border-dashed border-slate-300 rounded-xl p-6 text-center hover:bg-slate-50 hover:border-blue-400 transition-all flex flex-col items-center justify-center min-h-[100px] outline-none"
            tabIndex={0}
            title="Click vào khung này rồi ấn Ctrl+V để dán ảnh"
          >
            <input type="file" id={`file-${id}`} accept="image/*" className="hidden" onChange={(e) => handleFileUpload(e, onUpload, id)} />
            {uploadingId === id ? (
              <span className="text-blue-500 font-bold text-sm animate-pulse">⏳ Đang tải ảnh lên...</span>
            ) : (
              <label htmlFor={`file-${id}`} className="cursor-pointer text-slate-500 text-[14px] font-medium flex flex-col items-center gap-2">
                <span className="text-3xl opacity-50">🖼️</span>
                <span><span className="text-[#00a651] hover:underline">Tải ảnh lên</span> hoặc click vào đây và <span className="font-bold text-slate-700">Ctrl+V</span> để dán ảnh</span>
              </label>
            )}
          </div>
        )}
      </div>
    </div>
  );

  return (
    <div className="fixed inset-0 bg-[#f0f2f5] z-[60] flex flex-col animate-in fade-in">
      
      <div className="bg-white px-8 py-4 flex justify-between items-center shrink-0 border-b border-slate-200 shadow-sm relative z-20">
        <div className="flex items-center gap-3">
          <button onClick={onClose} className="text-slate-400 hover:text-slate-800 font-black text-xl transition">←</button>
          <h2 className="font-black text-[16px] text-slate-800 uppercase tracking-tight">{isImportMode ? 'IMPORT ĐỀ THI' : 'SOẠN THẢO ĐỀ THI'}</h2>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto relative custom-scrollbar">
        <div className="w-full px-8 lg:px-16 py-8 space-y-8 pb-32"> 
          
          <div className="flex justify-center mb-8">
            <div className="flex w-full max-w-4xl border-b-2 border-slate-200 gap-8">
              <button 
                onClick={() => setActiveTab('basic')} 
                className={`flex-1 pb-4 text-center font-black text-sm uppercase tracking-widest transition-all ${activeTab === 'basic' ? 'text-[#00a651] border-b-[3px] border-[#00a651]' : 'text-slate-400 hover:text-slate-600'}`}
              >
                THÔNG TIN CHÍNH
              </button>
              <button 
                onClick={() => setActiveTab('content')} 
                className={`flex-1 pb-4 text-center font-black text-sm uppercase tracking-widest transition-all ${activeTab === 'content' ? 'text-[#00a651] border-b-[3px] border-[#00a651]' : 'text-slate-400 hover:text-slate-600'}`}
              >
                CÀI ĐẶT & NỘI DUNG ĐỀ
              </button>
            </div>
          </div>

          {activeTab === 'basic' && (
            <div className="grid grid-cols-1 xl:grid-cols-2 gap-8 items-start animate-in slide-in-from-left-4">
              <div className="bg-white rounded-xl overflow-hidden border border-[#00a651] shadow-sm">
                <div className="bg-[#00a651] text-white text-center py-3 font-bold text-[14px] uppercase tracking-widest">THÔNG TIN CHÍNH</div>
                <div className="p-8 space-y-6">
                    <div>
                      <label className="text-[13px] font-bold text-slate-700">Tên đề <span className="text-red-500">*</span></label>
                      <input value={testData.basicInfo.title} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, title: e.target.value}})} className="w-full mt-2 p-3.5 bg-slate-50 border border-slate-200 rounded-lg outline-none focus:border-[#00a651] focus:bg-white text-[15px] transition" />
                    </div>
                    <div>
                      <label className="text-[13px] font-bold text-slate-700 mb-2 block">Ảnh đại diện</label>
                      <div className="w-full aspect-video bg-slate-50 border-2 border-dashed border-slate-300 rounded-xl flex flex-col items-center justify-center text-slate-400 hover:bg-slate-100 transition cursor-pointer">
                        <span className="text-6xl opacity-30 mb-4">🖼️</span>
                        <p className="text-[14px] font-medium">Kéo thả hoặc tải lên...</p>
                      </div>
                    </div>
                </div>
              </div>

              <div className="bg-white rounded-xl overflow-hidden border border-slate-200 shadow-sm">
                <div className="bg-[#f8fafc] text-slate-600 text-center py-3 font-bold text-[14px] uppercase tracking-widest border-b border-slate-200">CÀI ĐẶT HỆ THỐNG</div>
                <div className="p-8 space-y-6 bg-white">
                    <div>
                      <label className="text-[13px] font-bold text-slate-700">Thuộc Danh mục (Bắt buộc) <span className="text-red-500">*</span></label>
                      <select 
                        value={testData.folder_id || ''} 
                        onChange={e => setTestData({...testData, folder_id: e.target.value})} 
                        className={`w-full mt-2 p-3.5 bg-slate-50 border rounded-lg outline-none focus:ring-2 focus:ring-[#00a651] text-[14px] text-slate-800 transition cursor-pointer ${!testData.folder_id ? 'border-red-400 bg-red-50' : 'border-slate-200'}`}
                      >
                        <option value="" disabled>-- Vui lòng chọn danh mục lưu đề --</option>
                        {courses?.map((c: any) => {
                          const courseFolders = folders?.filter((f: any) => String(f.course_id) === String(c.id)) || [];
                          const rootFolders = courseFolders.filter((f: any) => !f.parent_id || f.parent_id === 'null' || f.parent_id === '');
                          
                          return (
                            <React.Fragment key={c.id}>
                              <option value={`course-${c.id}`} disabled className="font-black text-slate-800 bg-slate-100">📚 {c.title}</option>
                              {rootFolders.length === 0 && <option disabled className="text-slate-400 italic">&nbsp;&nbsp;&nbsp;&nbsp;⚠ Chưa có thư mục nào trong khóa này</option>}
                              
                              {rootFolders.map((f1: any) => {
                                // KIỂM TRA XEM THƯ MỤC CẤP 1 NÀY CÓ THƯ MỤC CON HAY KHÔNG
                                const children = courseFolders.filter((f2: any) => String(f2.parent_id) === String(f1.id));
                                const isLeaf = children.length === 0;

                                return (
                                  <React.Fragment key={f1.id}>
                                    <option 
                                      value={f1.id} 
                                      disabled={!isLeaf} 
                                      className={`font-bold ${!isLeaf ? 'text-slate-400 bg-slate-50' : 'text-[#00a651]'}`}
                                    >
                                      &nbsp;&nbsp;&nbsp;&nbsp;📁 {f1.title} {!isLeaf ? '(Chứa mục con - Không thể chọn)' : ''}
                                    </option>
                                    
                                    {children.map((f2: any) => (
                                      <option key={f2.id} value={f2.id} className="text-slate-600 font-medium">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ 📂 {f2.title}
                                      </option>
                                    ))}
                                  </React.Fragment>
                                );
                              })}
                            </React.Fragment>
                          );
                        })}
                      </select>
                      {!testData.folder_id && <p className="text-[11px] text-red-500 mt-1.5 italic">* Bạn phải chọn thư mục cấp thấp nhất để lưu đề thi</p>}
                    </div>

                    <div>
                      <label className="text-[13px] font-bold text-slate-700">Kỹ năng / Dạng đề <span className="text-red-500">*</span></label>
                      <select value={testData.basicInfo.skill} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, skill: e.target.value}})} className="w-full mt-2 p-3.5 bg-slate-50 border border-slate-200 rounded-lg outline-none focus:border-[#00a651] focus:bg-white text-[14px] text-slate-800 transition">
                        <option value="IELTS-Listening">Listening (IELTS)</option>
                        <option value="IELTS-Reading">Reading (IELTS)</option>
                        <option value="IELTS-Writing">Writing (IELTS - Chấm AI)</option>
                        <option value="IELTS-Speaking">Speaking (IELTS - Chấm AI)</option>
                        <option value="Standard-Listening">Listening (Standard - TOEIC/IGCSE)</option>
                        <option value="Standard-Reading">Reading (Standard - TOEIC/IGCSE)</option>
                      </select>
                    </div>
                    <div className="grid grid-cols-2 gap-6">
                      <div>
                        <label className="text-[13px] font-bold text-slate-700">Loại bài làm</label>
                        <select value={testData.basicInfo.mode} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, mode: e.target.value}})} className="w-full mt-2 p-3.5 bg-slate-50 border border-slate-200 rounded-lg outline-none focus:border-[#00a651] focus:bg-white text-[14px] text-slate-800 transition">
                          <option value="Đề thi">Đề thi</option>
                          <option value="Bài tập">Bài tập</option>
                        </select>
                      </div>
                      <div>
                        <label className="text-[13px] font-bold text-slate-700">Thời gian làm (phút)</label>
                        <input type="number" value={testData.basicInfo.timeLimit} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, timeLimit: e.target.value}})} className="w-full mt-2 p-3.5 bg-slate-50 border border-slate-200 rounded-lg outline-none focus:border-[#00a651] focus:bg-white text-[14px] text-slate-800 transition" />
                      </div>
                    </div>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'content' && (
            <div className="animate-in slide-in-from-right-4">
              <h3 className="text-center font-black text-slate-700 uppercase tracking-widest text-[16px] mb-8">NỘI DUNG ĐỀ</h3>
              
              <div className="bg-[#f8f9fa] border border-[#d1e9f6] rounded-2xl p-6 lg:p-10 shadow-sm max-w-6xl mx-auto">
                
                {isImportMode && (
                  <div className="bg-white p-8 rounded-xl border border-slate-200 mb-10 flex flex-col md:flex-row items-start md:items-center gap-6 shadow-sm">
                    <label className="text-[15px] font-bold text-slate-700 shrink-0 w-32">File upload</label>
                    <div className="flex-1 flex flex-col sm:flex-row items-start sm:items-center gap-4 w-full">
                      <label className="bg-white border border-slate-300 text-slate-700 px-6 py-3 rounded-lg text-[14px] font-bold cursor-pointer hover:bg-slate-50 shadow-sm transition shrink-0 flex items-center gap-2">
                        <input type="file" accept=".xlsx, .xls, .csv" onChange={handleImportExcel} className="hidden" /> 
                        <svg className="w-5 h-5 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                        Chọn tệp Excel/CSV
                      </label>
                    </div>
                  </div>
                )}

                {testData.parts.map((part: any, pIdx: number) => (
                  <div key={part.id} className="border-2 border-[#10b981] rounded-2xl bg-white overflow-hidden mb-10 relative shadow-sm">
                      <div className="bg-[#ecfdf5] px-8 py-4 border-b border-[#10b981]/20 flex justify-between items-center group">
                        <input value={part.title} onChange={(e) => updateField([pIdx], 'title', e.target.value)} className="font-black text-[#10b981] text-xl bg-transparent outline-none border-b border-dashed border-[#10b981]/50 focus:border-[#10b981] w-64" placeholder="Part Title..." />
                        <button onClick={() => removePart(pIdx)} className="text-red-400 hover:text-red-600 font-bold px-3 py-1 opacity-0 group-hover:opacity-100 transition">✖</button>
                      </div>
                      
                      <div className="p-8">
                        <FieldRow label="Nội dung" value={part.content} onChange={(e:any) => updateField([pIdx], 'content', e.target.value)} isTextArea={true} />
                        <FieldRow label="Tags" value={part.tags} onChange={(e:any) => updateField([pIdx], 'tags', e.target.value)} />
                        <ImagePasteRow label="Hình ảnh" value={part.imageUrl} onUpload={(url: string) => updateField([pIdx], 'imageUrl', url)} id={`img-p-${part.id}`} />
                        <FileRow label="Âm thanh" accept="audio/*" value={part.audioUrl} onUpload={(url: string) => updateField([pIdx], 'audioUrl', url)} id={`aud-p-${part.id}`} />
                        <FieldRow label="Giải thích" value={part.explanation} onChange={(e:any) => updateField([pIdx], 'explanation', e.target.value)} isTextArea={true} />
                      </div>

                      <div className="px-8 pb-8 space-y-8">
                        {part.sections.map((sec: any, sIdx: number) => (
                          <div key={sec.id} className="border-2 border-[#3b82f6] rounded-2xl bg-white overflow-hidden shadow-sm">
                            <div className="bg-[#eff6ff] px-8 py-4 border-b border-[#3b82f6]/20 flex justify-between items-center group">
                              <input value={sec.title} onChange={(e) => updateField([pIdx, sIdx], 'title', e.target.value)} className="font-black text-[#3b82f6] text-lg bg-transparent outline-none border-b border-dashed border-[#3b82f6]/50 focus:border-[#3b82f6] w-64" placeholder="Section Title..." />
                              <button onClick={() => removeSection(pIdx, sIdx)} className="text-red-400 hover:text-red-600 font-bold px-3 py-1 opacity-0 group-hover:opacity-100 transition">✖</button>
                            </div>
                            
                            <div className="p-8">
                              <FieldRow label="Nội dung" value={sec.content} onChange={(e:any) => updateField([pIdx, sIdx], 'content', e.target.value)} isTextArea={true} />
                              <FieldRow label="Tags" value={sec.tags} onChange={(e:any) => updateField([pIdx, sIdx], 'tags', e.target.value)} />
                              <div className="flex flex-col lg:flex-row items-start lg:items-center py-3 border-b border-slate-100 gap-2">
                                <label className="w-32 shrink-0 text-[13px] font-medium text-slate-500">Kiểu làm</label>
                                <select value={sec.questionType} onChange={(e) => updateField([pIdx, sIdx], 'questionType', e.target.value)} className="flex-1 w-full bg-slate-50 border border-slate-200 rounded-lg p-2.5 text-[14px] text-slate-700 outline-none focus:border-[#3b82f6] focus:bg-white transition">
                                  <option value="Kéo thả vào Part">Kéo thả vào Part</option>
                                  <option value="Trắc nghiệm">Trắc nghiệm</option>
                                  <option value="Điền từ">Điền từ</option>
                                </select>
                              </div>
                              <ImagePasteRow label="Hình ảnh" value={sec.imageUrl} onUpload={(url: string) => updateField([pIdx, sIdx], 'imageUrl', url)} id={`img-s-${sec.id}`} />
                              <FileRow label="Âm thanh" accept="audio/*" value={sec.audioUrl} onUpload={(url: string) => updateField([pIdx, sIdx], 'audioUrl', url)} id={`aud-s-${sec.id}`} />
                            </div>

                            <div className="px-8 pb-8 space-y-6">
                              {sec.questions.map((q: any, qIdx: number) => (
                                <div key={q.id} className="border-2 border-[#fbbf24] rounded-2xl bg-white overflow-hidden relative shadow-sm">
                                  <div className="bg-[#fffbeb] px-6 py-3 flex justify-between items-center group border-b border-[#fbbf24]/30">
                                    <span className="font-black text-[#d97706] text-[15px]">⬍ Question {qIdx + 1}</span>
                                    <button onClick={() => removeQuestion(pIdx, sIdx, qIdx)} className="text-red-400 hover:text-red-600 font-bold px-3 py-1 opacity-0 group-hover:opacity-100 transition">✖</button>
                                  </div>
                                  
                                  <div className="p-6">
                                      <FieldRow label="Nội dung" value={q.content} onChange={(e:any) => updateField([pIdx, sIdx, qIdx], 'content', e.target.value)} isTextArea={true} />
                                      <ImagePasteRow label="Hình ảnh" value={q.imageUrl} onUpload={(url: string) => updateField([pIdx, sIdx, qIdx], 'imageUrl', url)} id={`img-q-${q.id}`} />
                                      
                                      <div className="pt-5 lg:pl-[136px] space-y-3">
                                        {q.options.map((opt: string, oIdx: number) => (
                                          <div key={oIdx} className="flex items-center gap-3">
                                            <div className="w-9 h-9 rounded-full bg-slate-100 border border-slate-200 text-slate-600 font-black text-[13px] flex items-center justify-center shrink-0 shadow-sm">{String.fromCharCode(65+oIdx)}</div>
                                            <input value={opt} onChange={(e) => updateOption(pIdx, sIdx, qIdx, oIdx, e.target.value)} className="flex-1 bg-white border border-slate-200 rounded-lg p-2.5 text-[14px] outline-none focus:border-[#10b981] focus:ring-1 focus:ring-[#10b981] transition" />
                                            <button onClick={() => removeOption(pIdx, sIdx, qIdx, oIdx)} className="text-slate-300 hover:text-red-500 font-bold px-2 py-1 text-lg">×</button>
                                          </div>
                                        ))}
                                        <div className="pt-3">
                                          <button onClick={() => addOption(pIdx, sIdx, qIdx)} className="bg-[#10b981] hover:bg-[#059669] text-white px-5 py-2 rounded-full text-[12px] font-bold shadow-sm transition flex items-center gap-1"><span className="text-lg leading-none">+</span> Thêm đáp án</button>
                                        </div>
                                      </div>

                                      <div className="pt-4 border-t border-slate-100 mt-6">
                                        <FieldRow label="Lời giải" value={q.explanation} onChange={(e:any) => updateField([pIdx, sIdx, qIdx], 'explanation', e.target.value)} isTextArea={true} />
                                      </div>
                                  </div>
                                </div>
                              ))}

                              <div className="flex justify-center pt-2">
                                <button onClick={() => addQuestion(pIdx, sIdx)} className="bg-[#10b981] hover:bg-[#059669] text-white px-6 py-2.5 rounded-full text-[13px] font-bold shadow-md flex items-center gap-1.5 transition-transform active:scale-95"><span className="text-lg leading-none">+</span> Thêm câu</button>
                              </div>
                            </div>

                          </div>
                        ))}
                        
                        <div className="flex justify-center pt-2">
                          <button onClick={() => addSection(pIdx)} className="bg-[#10b981] hover:bg-[#059669] text-white px-6 py-2.5 rounded-full text-[13px] font-bold shadow-md flex items-center gap-1.5 transition-transform active:scale-95"><span className="text-lg leading-none">+</span> Thêm nhóm</button>
                        </div>

                      </div>
                  </div>
                ))}

                <div className="flex justify-center mt-8">
                    <button onClick={addPart} className="bg-[#10b981] hover:bg-[#059669] text-white px-8 py-3 rounded-full text-[15px] font-bold shadow-lg flex items-center gap-2 transition-transform active:scale-95 hover:scale-105"><span className="text-xl leading-none">+</span> Thêm phần</button>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>

      <button 
        onClick={handleSave} 
        disabled={isSaving} 
        className="fixed bottom-10 right-10 w-20 h-20 bg-[#2bd6eb] hover:bg-[#1bc1d6] text-white rounded-full shadow-[0_10px_25px_rgba(43,214,235,0.4)] flex flex-col items-center justify-center z-[100] transition-all hover:scale-110 active:scale-95 disabled:opacity-50 disabled:hover:scale-100"
        title="Lưu Đề Thi"
      >
        <span className="text-[26px] mb-0.5">{isSaving ? '⏳' : '💾'}</span>
        <span className="text-[10px] font-black uppercase tracking-wider">{isSaving ? 'Đang lưu' : 'Lưu Đề'}</span>
      </button>

    </div>
  );
}