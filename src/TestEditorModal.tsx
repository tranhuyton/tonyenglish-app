import React, { useState } from 'react';
import { supabase } from './supabase';

// ĐƯA CÁC COMPONENT NÀY RA NGOÀI ĐỂ KHÔNG BỊ VĂNG CON TRỎ CHUỘT KHI GÕ
const FieldRow = ({ label, value, onChange, placeholder = "" }: any) => (
  <div className="flex flex-col md:flex-row items-start md:items-center py-3 border-b border-slate-100 last:border-0 gap-2">
    <label className="w-32 shrink-0 text-[13px] font-medium text-slate-500">{label}</label>
    <input type="text" value={value || ''} onChange={onChange} placeholder={placeholder} className="flex-1 w-full bg-white border border-slate-200 rounded-lg p-2.5 text-[14px] focus:border-[#00a651] outline-none transition" />
  </div>
);

const FileRow = ({ label, value, onUpload, id, accept = "audio/*, image/*", uploadingId, handleFileUpload }: any) => (
  <div className="flex flex-col md:flex-row items-start md:items-center py-3 border-b border-slate-100 last:border-0 gap-2">
    <label className="w-32 shrink-0 text-[13px] font-medium text-slate-500">{label}</label>
    <div className="flex items-center gap-3 flex-1 w-full">
      <label className="bg-slate-50 border border-slate-300 text-slate-700 px-4 py-2 rounded-lg text-[13px] cursor-pointer hover:bg-slate-100 transition shadow-sm">
        <input type="file" className="hidden" accept={accept} onChange={(e) => handleFileUpload(e, onUpload, id)} /> 
        {uploadingId === id ? '⏳ Đang tải...' : 'Chọn tệp'}
      </label>
      <span className="text-[12px] text-slate-400 truncate flex-1">{value ? '✅ Đã tải lên thành công' : 'Không có tệp... được chọn'}</span>
    </div>
  </div>
);

// HÀM CHÍNH
export default function TestEditorModal({ testData: testRecord, courses, onClose, onSave }: any) {
  const isImportMode = testRecord.mode === 'import'; 
  const [activeTab, setActiveTab] = useState('basic'); 
  
  const getInitialData = () => {
    if (testRecord.content_json) return {...testRecord.content_json};
    return {
      basicInfo: {
        title: testRecord.title || '',
        courseId: 'all', 
        thumbnail: '',
        skill: testRecord.test_type || 'IELTS-Listening',
        mode: 'Đề thi',
        timeLimit: '40',
        scoreType: '1 điểm/ câu đúng',
        limit: ''
      },
      parts: isImportMode ? [] : [
        {
          id: Date.now().toString(), title: 'Part 1', content: '', tags: '', audioUrl: '', explanation: '',
          sections: [
            {
              id: (Date.now()+1).toString(), title: 'Section 1', content: '', tags: '', questionType: 'Kéo thả vào Part', audioUrl: '', explanation: '',
              questions: [
                { id: (Date.now()+2).toString(), content: '', tags: '', audioUrl: '', explanation: '', options: ['A', 'B', 'C', 'D'], correctAnswer: '' }
              ]
            }
          ]
        }
      ]
    };
  };

  const [testData, setTestData] = useState<any>(getInitialData());
  const [isSaving, setIsSaving] = useState(false);
  const [uploadingId, setUploadingId] = useState<string | null>(null);

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

  const handleSave = () => {
    setIsSaving(true);
    onSave(testData); 
  };

  return (
    <div className="fixed inset-0 bg-[#f0f2f5] z-[60] flex flex-col animate-in fade-in">
      <div className="bg-white px-6 py-3 flex justify-between items-center shrink-0 border-b border-slate-200 shadow-sm relative z-20">
        <div className="flex items-center gap-3">
          <button onClick={onClose} className="text-slate-500 hover:text-slate-800 font-bold text-xl transition">←</button>
          <h2 className="font-black text-[15px] text-slate-800 uppercase tracking-tight">{isImportMode ? 'Import Đề Thi' : 'Soạn Thảo Đề Thi'}</h2>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto relative custom-scrollbar">
        <div className="max-w-[1400px] mx-auto w-full p-4 md:p-8 space-y-8 pb-20"> 
          <div className="flex flex-col md:flex-row gap-4 mb-6">
            <button onClick={() => setActiveTab('basic')} className={`w-full md:w-1/2 py-3 rounded-t-xl font-black text-sm uppercase tracking-widest transition-all border-b-4 ${activeTab === 'basic' ? 'bg-white border-[#00a651] text-[#00a651] shadow-sm' : 'bg-slate-200/50 border-transparent text-slate-400 hover:bg-slate-200'}`}>Thông tin chính</button>
            <button onClick={() => setActiveTab('content')} className={`w-full md:w-1/2 py-3 rounded-t-xl font-black text-sm uppercase tracking-widest transition-all border-b-4 ${activeTab === 'content' ? 'bg-white border-[#00a651] text-[#00a651] shadow-sm' : 'bg-slate-200/50 border-transparent text-slate-400 hover:bg-slate-200'}`}>Cài đặt & Nội dung đề</button>
          </div>

          {activeTab === 'basic' && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-start animate-in slide-in-from-left-4">
              <div className="bg-white rounded-xl overflow-hidden border border-slate-200 shadow-sm">
                <div className="bg-[#00a651] text-white text-center py-2.5 font-bold text-[13px] uppercase tracking-widest">Thông tin chính</div>
                <div className="p-6 space-y-5">
                    <div>
                      <label className="text-[12px] font-bold text-slate-600">Tên đề <span className="text-red-500">*</span></label>
                      <input value={testData.basicInfo.title} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, title: e.target.value}})} placeholder="Ví dụ: Đề thi tiếng Anh 10" className="w-full mt-1.5 p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none focus:border-[#00a651] text-[14px] transition" />
                    </div>
                </div>
              </div>

              <div className="bg-white rounded-xl overflow-hidden border border-slate-200 shadow-sm">
                <div className="bg-slate-100 text-slate-600 text-center py-2.5 font-bold text-[13px] uppercase tracking-widest border-b border-slate-200">Cài đặt hệ thống</div>
                <div className="p-6 space-y-5">
                    <div>
                      <label className="text-[12px] font-bold text-slate-600">Thuộc Khóa học <span className="text-red-500">*</span></label>
                      <select value={testData.basicInfo.courseId} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, courseId: e.target.value}})} className="w-full mt-1.5 p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] text-slate-800 transition">
                        <option value="all">Dùng chung (Không thuộc khóa nào)</option>
                        {courses?.map((c: any) => <option key={c.id} value={c.id}>{c.title}</option>)}
                      </select>
                    </div>
                    <div>
                      <label className="text-[12px] font-bold text-slate-600">Kỹ năng / Dạng đề <span className="text-red-500">*</span></label>
                      <select value={testData.basicInfo.skill} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, skill: e.target.value}})} className="w-full mt-1.5 p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] text-slate-800 transition">
                        <option value="IELTS-Listening">Listening (IELTS)</option>
                        <option value="IELTS-Reading">Reading (IELTS)</option>
                        <option value="Standard-Listening">Listening (Standard)</option>
                        <option value="Standard-Reading">Reading (Standard)</option>
                        <option value="IELTS-Writing">Writing (IELTS - Chấm AI)</option>
                        <option value="IELTS-Speaking">Speaking (IELTS - Chấm AI)</option>
                        <option value="Standard-Test">Standard (TOEIC/IGCSE)</option>
                      </select>
                    </div>
                    <div className="grid grid-cols-2 gap-4">
                      <div>
                        <label className="text-[12px] font-bold text-slate-600">Loại bài làm</label>
                        <select value={testData.basicInfo.mode} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, mode: e.target.value}})} className="w-full mt-1.5 p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] text-slate-800 transition">
                          <option value="Đề thi">Đề thi</option><option value="Bài tập">Bài tập</option>
                        </select>
                      </div>
                      <div>
                        <label className="text-[12px] font-bold text-slate-600">Thời gian làm (phút)</label>
                        <input type="number" value={testData.basicInfo.timeLimit} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, timeLimit: e.target.value}})} className="w-full mt-1.5 p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] text-slate-800 transition" />
                      </div>
                    </div>
                    <div>
                      <label className="text-[12px] font-bold text-slate-600">Cách tính điểm</label>
                      <select value={testData.basicInfo.scoreType} onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, scoreType: e.target.value}})} className="w-full mt-1.5 p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] text-slate-800 transition">
                        <option value="1 điểm/ câu đúng">1 điểm/ câu đúng</option>
                        <option value="IELTS Band Score">IELTS Band Score</option>
                        <option value="IGCSE Grading">Điểm gốc ➔ Thang điểm IGCSE (A*, A, B...)</option>
                      </select>
                    </div>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'content' && (
            <div className="animate-in slide-in-from-right-4">
              <h3 className="text-center font-black text-slate-700 uppercase tracking-widest text-[14px] mb-6">NỘI DUNG ĐỀ / MARKING SCHEME</h3>
              
              <div className="bg-[#f4f9fd] border border-[#bae0f5] rounded-2xl overflow-hidden p-4 md:p-8 shadow-sm">
                {testData.parts?.map((part: any, pIdx: number) => (
                  <div key={part.id} className="border-2 border-[#00a651] rounded-xl bg-[#f8fcf9] overflow-hidden mb-8 relative shadow-sm">
                      <div className="bg-[#e6f4ea] px-6 py-3.5 border-b border-[#00a651]/20 flex justify-between items-center group">
                        <input value={part.title} onChange={(e) => updateField([pIdx], 'title', e.target.value)} className="font-black text-[#00a651] text-lg bg-transparent outline-none border-b border-dashed border-[#00a651]/50 focus:border-[#00a651] w-64" placeholder="Part Title..." />
                        <button onClick={() => removePart(pIdx)} className="text-red-500 font-bold px-3 py-1 opacity-0 group-hover:opacity-100 transition">✖</button>
                      </div>
                      
                      <div className="p-6 md:p-8">
                        <FieldRow label="Tiêu đề" value={part.title} onChange={(e:any) => updateField([pIdx], 'title', e.target.value)} />
                        <FieldRow label="Nội dung" value={part.content} onChange={(e:any) => updateField([pIdx], 'content', e.target.value)} />
                        <FieldRow label="Tags" value={part.tags} onChange={(e:any) => updateField([pIdx], 'tags', e.target.value)} />
                        <FileRow label="Âm thanh" value={part.audioUrl} handleFileUpload={handleFileUpload} uploadingId={uploadingId} onUpload={(url: string) => updateField([pIdx], 'audioUrl', url)} id={`part-${part.id}`} />
                      </div>

                      <div className="px-6 md:px-8 pb-8 space-y-8">
                        {part.sections?.map((sec: any, sIdx: number) => (
                          <div key={sec.id} className="border-2 border-[#3b82f6] rounded-xl bg-[#f4f8ff] overflow-hidden shadow-sm">
                            <div className="bg-[#3b82f6] px-6 py-3 flex justify-between items-center group">
                              <input value={sec.title} onChange={(e) => updateField([pIdx, sIdx], 'title', e.target.value)} className="font-black text-white text-base bg-transparent outline-none border-b border-dashed border-white/50 focus:border-white w-64 placeholder:text-white/60" placeholder="Section Title..." />
                              <button onClick={() => removeSection(pIdx, sIdx)} className="text-white hover:text-red-200 font-bold px-3 py-1 opacity-0 group-hover:opacity-100 transition">✖</button>
                            </div>
                            
                            <div className="p-6 md:p-8">
                              <FieldRow label="Nội dung" value={sec.content} onChange={(e:any) => updateField([pIdx, sIdx], 'content', e.target.value)} />
                              <div className="flex flex-col md:flex-row items-start md:items-center py-3 border-b border-slate-100 gap-2">
                                <label className="w-32 shrink-0 text-[13px] font-medium text-slate-500">Kiểu làm</label>
                                <select value={sec.questionType} onChange={(e) => updateField([pIdx, sIdx], 'questionType', e.target.value)} className="flex-1 w-full bg-white border border-slate-200 rounded-lg p-2.5 text-[14px] text-slate-700 outline-none focus:border-[#3b82f6] transition">
                                  <option value="Kéo thả vào Part">Kéo thả vào Part</option>
                                  <option value="Trắc nghiệm">Trắc nghiệm</option>
                                  <option value="Điền từ">Điền từ</option>
                                </select>
                              </div>
                              <FileRow label="Âm thanh" value={sec.audioUrl} handleFileUpload={handleFileUpload} uploadingId={uploadingId} onUpload={(url: string) => updateField([pIdx, sIdx], 'audioUrl', url)} id={`sec-${sec.id}`} />
                            </div>

                            <div className="px-6 md:px-8 pb-8 space-y-6">
                              {sec.questions?.map((q: any, qIdx: number) => (
                                <div key={q.id} className="border-2 border-amber-300 rounded-xl bg-white overflow-hidden relative shadow-sm">
                                  <div className="bg-[#fef3c7] px-6 py-3 flex justify-between items-center group border-b border-amber-200">
                                    <span className="font-black text-amber-600 text-[15px]">⬍ Question {qIdx + 1}</span>
                                    <button onClick={() => removeQuestion(pIdx, sIdx, qIdx)} className="text-red-500 hover:text-red-700 font-bold px-3 py-1 opacity-0 group-hover:opacity-100 transition">✖</button>
                                  </div>
                                  
                                  <div className="p-6">
                                      <FieldRow label="Câu hỏi" value={q.content} onChange={(e:any) => updateField([pIdx, sIdx, qIdx], 'content', e.target.value)} />
                                      
                                      <div className="pt-5 md:pl-[136px] space-y-3">
                                        {q.options?.map((opt: string, oIdx: number) => (
                                          <div key={oIdx} className="flex items-center gap-3">
                                            <div className="w-9 h-9 rounded-full bg-slate-100 border border-slate-200 text-slate-600 font-black text-[13px] flex items-center justify-center shrink-0 shadow-sm">{String.fromCharCode(65+oIdx)}</div>
                                            <input value={opt || ''} onChange={(e) => updateOption(pIdx, sIdx, qIdx, oIdx, e.target.value)} placeholder="Nhập đáp án..." className="flex-1 bg-white border border-slate-200 rounded-lg p-2.5 text-[14px] outline-none focus:border-[#00a651] focus:ring-1 focus:ring-[#00a651] transition" />
                                            <button onClick={() => removeOption(pIdx, sIdx, qIdx, oIdx)} className="text-slate-300 hover:text-red-500 font-bold px-2 py-1 text-lg">×</button>
                                          </div>
                                        ))}
                                        <div className="pt-3">
                                          <button onClick={() => addOption(pIdx, sIdx, qIdx)} className="bg-[#00a651] hover:bg-[#008f45] text-white px-5 py-2 rounded-full text-[12px] font-bold shadow-sm transition">+ Thêm lựa chọn</button>
                                        </div>
                                      </div>
                                  </div>
                                </div>
                              ))}
                              <div className="flex justify-center pt-2">
                                <button onClick={() => addQuestion(pIdx, sIdx)} className="bg-[#00a651] hover:bg-[#008f45] text-white px-6 py-2.5 rounded-full text-[13px] font-bold shadow-md">+ Thêm câu hỏi</button>
                              </div>
                            </div>
                          </div>
                        ))}
                        <div className="flex justify-center pt-2">
                          <button onClick={() => addSection(pIdx)} className="bg-[#00a651] hover:bg-[#008f45] text-white px-6 py-2.5 rounded-full text-[13px] font-bold shadow-md">+ Thêm nhóm (Section)</button>
                        </div>
                      </div>
                  </div>
                ))}
                <div className="flex justify-center pt-6 border-t border-[#b6dff5]">
                    <button onClick={addPart} className="bg-[#00a651] hover:bg-[#008f45] text-white px-8 py-3 rounded-full text-[14px] font-bold shadow-lg">+ Thêm Part</button>
                </div>
              </div>
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