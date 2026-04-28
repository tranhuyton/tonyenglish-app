import React, { useState } from 'react';
import { supabase } from './supabase';

interface TestEditorProps {
  testRecord: any;
  onClose: () => void;
  onRefresh: () => void;
}

export default function TestEditorModal({ testRecord, onClose, onRefresh }: TestEditorProps) {
  const [testData, setTestData] = useState<any>(JSON.parse(JSON.stringify(testRecord.test_data)));
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

  const handlePasteImage = async (e: React.ClipboardEvent, updateCallback: (url: string) => void, id: string) => {
    const items = e.clipboardData.items;
    for (let i = 0; i < items.length; i++) {
      if (items[i].type.indexOf('image') !== -1) {
        const file = items[i].getAsFile();
        if (file) {
          setUploadingId(id);
          try {
            const url = await uploadToSupabase(file);
            updateCallback(url);
          } catch (error: any) { alert("Lỗi upload ảnh: " + error.message); } 
          finally { setUploadingId(null); }
        }
      }
    }
  };

  const handleSave = async () => {
    setIsSaving(true);
    const { error } = await supabase.from('mock_tests').update({ test_data: testData }).eq('id', testRecord.id);
    setIsSaving(false);
    if (error) { alert("Lỗi khi lưu: " + error.message); } 
    else { alert("✅ Đã lưu thành công!"); onRefresh(); onClose(); }
  };

  return (
    <div className="fixed inset-0 bg-slate-900/95 z-[60] flex flex-col p-4 md:p-8">
      <div className="bg-white rounded-xl shadow-2xl w-full max-w-6xl mx-auto flex flex-col h-full overflow-hidden border border-slate-300">
        
        <div className="bg-[#1e293b] px-6 py-4 flex justify-between items-center shrink-0">
          <div>
            <h2 className="font-bold text-lg text-white flex items-center gap-2">✏️ Trình Soạn Thảo Đề Thi</h2>
            <p className="text-slate-300 text-xs mt-1">Đề: {testData.title}</p>
          </div>
          <div className="flex gap-3">
            <button onClick={onClose} className="px-6 py-2 text-white hover:bg-slate-700 rounded font-medium transition">Hủy</button>
            <button onClick={handleSave} disabled={isSaving} className="bg-[#3b82f6] hover:bg-blue-500 text-white px-8 py-2 rounded font-bold transition shadow-lg">{isSaving ? '⏳ Đang lưu...' : '💾 Lưu Thay Đổi'}</button>
          </div>
        </div>

        <div className="p-6 overflow-y-auto flex-1 bg-[#f8fafc] custom-scrollbar space-y-6">
          {testData.parts.map((part: any, pIndex: number) => (
            <div key={pIndex} className="bg-white border border-slate-200 rounded-xl shadow-sm overflow-hidden mb-8">
              <div className="bg-slate-100 px-6 py-4 border-b border-slate-200 flex gap-4 items-center">
                <input 
                  value={part.title} 
                  onChange={(e) => { const newData = {...testData}; newData.parts[pIndex].title = e.target.value; setTestData(newData); }}
                  className="font-black text-slate-800 uppercase text-base bg-transparent border-b border-dashed border-slate-400 focus:border-blue-500 outline-none w-64"
                  placeholder="TÊN SECTION/PART"
                />
              </div>
              
              {/* KHU VỰC NHẬP NỘI DUNG PASSAGE / TAPESCRIPT (MỚI) */}
              <div className="p-6 border-b border-slate-200 bg-white grid md:grid-cols-2 gap-8">
                <div className="space-y-4">
                  <div>
                    <label className="text-[11px] font-bold text-slate-500 uppercase">Tiêu đề bài đọc / Hội thoại</label>
                    <input 
                      value={part.passageTitle || ''} 
                      onChange={(e) => { const newData = {...testData}; newData.parts[pIndex].passageTitle = e.target.value; setTestData(newData); }}
                      className="w-full mt-1 p-2 border border-slate-300 rounded text-sm font-bold text-slate-800 focus:border-blue-500 outline-none"
                      placeholder="VD: The History of Bicycles"
                    />
                  </div>
                  <div>
                    <label className="text-[11px] font-bold text-slate-500 uppercase">Câu lệnh hướng dẫn (Instruction)</label>
                    <input 
                      value={part.instructions || ''} 
                      onChange={(e) => { const newData = {...testData}; newData.parts[pIndex].instructions = e.target.value; setTestData(newData); }}
                      className="w-full mt-1 p-2 border border-slate-300 rounded text-sm text-slate-800 focus:border-blue-500 outline-none italic"
                      placeholder="VD: Read the text below and answer questions 1-5"
                    />
                  </div>
                  <div>
                    <label className="text-[11px] font-bold text-slate-500 uppercase">🎵 AUDIO CỦA PART NÀY</label>
                    <div className="flex items-center gap-4 mt-1">
                      {part.audioUrl ? (
                        <div className="flex-1 flex items-center gap-4 bg-white p-2 border border-slate-200 rounded">
                          <audio controls src={part.audioUrl} className="h-8 flex-1 outline-none" />
                          <button onClick={() => { const newData = {...testData}; newData.parts[pIndex].audioUrl = ''; setTestData(newData); }} className="text-red-500 text-xs font-bold px-3">Xóa</button>
                        </div>
                      ) : (
                        <label className="bg-white border border-slate-300 text-slate-700 px-4 py-2 rounded text-sm font-medium cursor-pointer hover:bg-slate-50 transition w-full text-center">
                          <input type="file" accept="audio/*" className="hidden" onChange={(e) => handleFileUpload(e, (url) => { const newData = {...testData}; newData.parts[pIndex].audioUrl = url; setTestData(newData); }, `audio-${pIndex}`)} />
                          {uploadingId === `audio-${pIndex}` ? '⏳ Đang tải...' : '📎 Tải file MP3'}
                        </label>
                      )}
                    </div>
                  </div>
                </div>

                <div>
                  <label className="text-[11px] font-bold text-blue-600 uppercase">📝 NỘI DUNG BÀI ĐỌC (HOẶC TAPESCRIPT CHO LISTENING)</label>
                  <textarea 
                    value={part.passageContent || ''} 
                    onChange={(e) => { const newData = {...testData}; newData.parts[pIndex].passageContent = e.target.value; setTestData(newData); }}
                    className="w-full mt-1 p-3 border-2 border-blue-200 bg-blue-50/30 rounded-md text-[14px] leading-relaxed text-slate-800 focus:border-blue-500 outline-none resize-y min-h-[220px] custom-scrollbar"
                    placeholder="Dán nội dung bài đọc hoặc Tapescript vào đây (Hỗ trợ thẻ HTML như <br>, <p>, <b>...)"
                  />
                </div>
              </div>

              {/* KHU VỰC CÂU HỎI */}
              <div className="p-6 bg-slate-50">
                {part.questionGroups.map((group: any, gIndex: number) => (
                  <div key={gIndex} className="mb-10">
                    <div className="flex gap-4 mb-5 items-center">
                      <span className="w-1 h-6 bg-blue-500 rounded"></span>
                      <input 
                        value={group.title}
                        onChange={(e) => { const newData = {...testData}; newData.parts[pIndex].questionGroups[gIndex].title = e.target.value; setTestData(newData); }}
                        className="font-bold text-slate-800 text-lg bg-transparent border-b border-dashed border-slate-400 focus:border-blue-500 outline-none flex-1"
                        placeholder="Group Title (VD: Questions 1-5)"
                      />
                    </div>
                    
                    <div className="space-y-6">
                      {group.questions.map((q: any, qIndex: number) => (
                        <div key={qIndex} className="p-5 border border-slate-200 rounded-lg bg-white flex gap-5 shadow-sm hover:border-blue-300 transition">
                          <div className="font-black text-slate-600 bg-slate-200 w-8 h-8 flex items-center justify-center rounded-full text-sm shrink-0">{q.id}</div>
                          
                          <div className="flex-1 space-y-4">
                            <div>
                              <label className="text-[11px] font-bold text-slate-500 uppercase tracking-wide">Nội dung câu hỏi</label>
                              <textarea 
                                value={q.text}
                                onChange={(e) => { const newData = {...testData}; newData.parts[pIndex].questionGroups[gIndex].questions[qIndex].text = e.target.value; setTestData(newData); }}
                                className="w-full mt-1 p-3 border border-slate-300 rounded-md text-[15px] font-bold text-slate-900 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none resize-y min-h-[60px] bg-slate-50 shadow-inner"
                                placeholder="Nhập nội dung câu hỏi..."
                              />
                            </div>

                            <div className="bg-white p-3 border border-slate-200 rounded-md">
                              <label className="text-[11px] font-bold text-slate-500 uppercase mb-2 block">Hình ảnh minh họa</label>
                              {q.imageUrl ? (
                                <div className="relative inline-block border border-slate-200 rounded p-1 bg-slate-50">
                                  <img src={q.imageUrl} className="max-h-40 object-contain rounded" />
                                  <button onClick={() => { const newData = {...testData}; newData.parts[pIndex].questionGroups[gIndex].questions[qIndex].imageUrl = ''; setTestData(newData); }} className="absolute top-2 right-2 bg-red-500 text-white text-[10px] px-2 py-1 rounded shadow hover:bg-red-600">Xóa</button>
                                </div>
                              ) : (
                                <div className="flex gap-2">
                                  <label className="bg-slate-100 border border-slate-300 text-slate-700 px-4 py-2 rounded text-xs font-bold cursor-pointer hover:bg-slate-200 transition shrink-0">
                                    <input type="file" accept="image/*" className="hidden" onChange={(e) => handleFileUpload(e, (url) => { const newData = {...testData}; newData.parts[pIndex].questionGroups[gIndex].questions[qIndex].imageUrl = url; setTestData(newData); }, `img-q-${q.id}`)} />
                                    {uploadingId === `img-q-${q.id}` ? '⏳ Đang tải...' : '📎 Chọn ảnh'}
                                  </label>
                                  <input type="text" readOnly placeholder="Hoặc Click vào đây và nhấn Ctrl+V để dán ảnh chụp màn hình..." onPaste={(e) => handlePasteImage(e, (url) => { const newData = {...testData}; newData.parts[pIndex].questionGroups[gIndex].questions[qIndex].imageUrl = url; setTestData(newData); }, `img-q-${q.id}`)} className="flex-1 border border-dashed border-slate-300 rounded px-3 text-sm font-medium text-slate-600 bg-slate-50 focus:border-blue-500 focus:bg-white outline-none cursor-text" />
                                </div>
                              )}
                            </div>

                            {q.options && q.options.length > 0 && (
                              <div className="bg-white p-4 border border-slate-200 rounded-md">
                                <label className="text-[11px] font-bold text-slate-500 uppercase mb-3 block">Các đáp án</label>
                                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                                  {q.options.map((opt: string, optIndex: number) => (
                                    <div key={optIndex} className="flex items-center gap-3">
                                      <span className="font-black text-slate-400">{String.fromCharCode(65 + optIndex)}</span>
                                      <input value={opt} onChange={(e) => { const newData = {...testData}; newData.parts[pIndex].questionGroups[gIndex].questions[qIndex].options[optIndex] = e.target.value; setTestData(newData); }} className="flex-1 border border-slate-300 rounded p-2 text-sm font-semibold text-slate-800 focus:border-blue-500 outline-none" />
                                    </div>
                                  ))}
                                </div>
                              </div>
                            )}

                            <div className="grid md:grid-cols-3 gap-4">
                              <div className="md:col-span-1">
                                <label className="text-[11px] font-bold text-emerald-600 uppercase">Đáp án đúng</label>
                                <input value={q.correctAnswer || ''} onChange={(e) => { const newData = {...testData}; newData.parts[pIndex].questionGroups[gIndex].questions[qIndex].correctAnswer = e.target.value; setTestData(newData); }} className="w-full mt-1 p-2 border-2 border-emerald-400 bg-emerald-50 rounded-md text-base font-black text-emerald-700 outline-none focus:border-emerald-600 text-center uppercase" placeholder="VD: A" />
                              </div>
                              <div className="md:col-span-2">
                                <label className="text-[11px] font-bold text-amber-600 uppercase">Lời giải / Giải thích</label>
                                <textarea value={q.explanation || ''} onChange={(e) => { const newData = {...testData}; newData.parts[pIndex].questionGroups[gIndex].questions[qIndex].explanation = e.target.value; setTestData(newData); }} className="w-full mt-1 p-2 border border-amber-300 bg-amber-50 rounded-md text-sm font-medium text-slate-800 outline-none focus:border-amber-500 resize-y min-h-[60px]" placeholder="Nhập giải thích cho học sinh..." />
                              </div>
                            </div>

                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}