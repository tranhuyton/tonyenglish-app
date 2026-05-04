import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';
import JoditEditor from 'jodit-react';

export default function LectureEditorModal({ lectureData, courses, onClose, onRefresh }: any) {
  const [title, setTitle] = useState(lectureData?.title || '');
  const [courseId, setCourseId] = useState(lectureData?.course_id || '');
  const [moduleId, setModuleId] = useState(lectureData?.module_id || '');
  
  const [pages, setPages] = useState<any[]>([]);
  const [activePageIndex, setActivePageIndex] = useState(0);
  const [isSaving, setIsSaving] = useState(false);

  const editorRef = useRef(null);

  // Cấu hình Jodit Editor: Giữ nguyên HTML, thêm Toolbar đầy đủ
  const editorConfig = useMemo(() => ({
    readonly: false,
    height: 550,
    allowResizeY: false,
    statusbar: false,
    toolbarAdaptive: false,
    defaultActionOnPaste: 'insert_as_html', // Quan trọng: Báo cho Editor giữ nguyên HTML khi paste
    askBeforePasteHTML: false,
    askBeforePasteFromWord: false,
    uploader: { insertImageAsBase64URI: true } // Cho phép copy paste ảnh trực tiếp
  }), []);

  useEffect(() => {
    if (lectureData.id !== 'new') fetchPages();
    else setPages([{ id: 'temp_1', page_number: 1, content_html: '' }]);
  }, [lectureData]);

  const fetchPages = async () => {
    const { data } = await supabase.from('lecture_pages').select('*').eq('lecture_id', lectureData.id).order('page_number', { ascending: true });
    if (data && data.length > 0) setPages(data);
    else setPages([{ id: 'temp_1', page_number: 1, content_html: '' }]);
  };

  const activePage = pages[activePageIndex] || null;

  const handleHtmlChange = (newHtml: string) => {
    const updatedPages = [...pages];
    updatedPages[activePageIndex].content_html = newHtml;
    setPages(updatedPages);
  };

  const handleAddPage = () => {
    setPages([...pages, { id: `temp_${Date.now()}`, page_number: pages.length + 1, content_html: '' }]);
    setActivePageIndex(pages.length);
  };

  const handleRemovePage = (indexToRemove: number) => {
    if (pages.length <= 1) return alert('Bài giảng phải có ít nhất 1 trang!');
    if (!window.confirm('Xóa trang này?')) return;
    const newPages = pages.filter((_, idx) => idx !== indexToRemove).map((p, idx) => ({ ...p, page_number: idx + 1 }));
    setPages(newPages);
    setActivePageIndex(Math.max(0, indexToRemove - 1));
  };

  const handleSave = async () => {
    if (!title.trim() || !courseId) return alert('Vui lòng nhập tên và chọn khóa học!');
    setIsSaving(true);

    try {
      let currentLectureId = lectureData.id;
      const lecPayload = { title, course_id: courseId, module_id: moduleId || null, is_published: true };
      
      if (currentLectureId === 'new') {
        const { data: newLec, error: err1 } = await supabase.from('lectures').insert([lecPayload]).select().single();
        if (err1) throw err1;
        currentLectureId = newLec.id;
      } else {
        const { error: err2 } = await supabase.from('lectures').update(lecPayload).eq('id', currentLectureId);
        if (err2) throw err2;
      }

      await supabase.from('lecture_pages').delete().eq('lecture_id', currentLectureId);

      const pagesToInsert = pages.map((p, idx) => ({
        lecture_id: currentLectureId,
        page_number: idx + 1,
        content_html: p.content_html || ''
      }));
      
      const { error: err3 } = await supabase.from('lecture_pages').insert(pagesToInsert);
      if (err3) throw err3;

      alert('Lưu bài giảng thành công!');
      onRefresh();
      onClose();
    } catch (error: any) {
      alert('Lỗi lưu bài giảng: ' + error.message);
    } finally {
      setIsSaving(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-slate-900/80 z-[100] flex justify-center items-center p-4">
      <div className="bg-[#f4f6f9] w-full max-w-7xl h-[95vh] rounded-2xl shadow-2xl flex flex-col overflow-hidden animate-in zoom-in-95">
        
        <div className="h-16 bg-white border-b border-slate-200 px-6 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-4">
             <div className="w-10 h-10 rounded-xl bg-blue-100 flex items-center justify-center text-xl">📝</div>
             <h2 className="text-lg font-black text-[#0a5482] uppercase tracking-wide">
               {lectureData.id === 'new' ? 'Tạo Bài Giảng Mới' : 'Cập Nhật Bài Giảng'}
             </h2>
          </div>
          <div className="flex items-center gap-3">
            <button onClick={onClose} className="px-5 py-2 rounded-xl text-slate-500 font-bold hover:bg-slate-100 transition">Hủy bỏ ✖</button>
            <button onClick={handleSave} disabled={isSaving} className="bg-[#2bd6eb] hover:bg-[#1bc1d6] text-white px-8 py-2 rounded-xl font-black shadow-lg flex items-center gap-2 transition disabled:opacity-50">
              {isSaving ? '⏳ ĐANG LƯU...' : '💾 LƯU LẠI'}
            </button>
          </div>
        </div>

        <div className="p-4 bg-white border-b border-slate-200 flex gap-4 shrink-0">
          <div className="flex-1">
             <label className="text-[11px] font-black text-slate-400 uppercase tracking-widest mb-1 block">Tên bài giảng <span className="text-red-500">*</span></label>
             <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Nhập tên bài giảng..." className="w-full bg-slate-50 border border-slate-200 rounded-lg px-4 py-2 font-bold text-slate-700 outline-none focus:border-[#2bd6eb]" />
          </div>
          <div className="w-64">
             <label className="text-[11px] font-black text-slate-400 uppercase tracking-widest mb-1 block">Khóa học <span className="text-red-500">*</span></label>
             <select value={courseId} onChange={(e) => setCourseId(e.target.value)} className="w-full bg-slate-50 border border-slate-200 rounded-lg px-4 py-2 font-bold text-slate-700 outline-none focus:border-[#2bd6eb]">
                <option value="" disabled>Chọn khóa học...</option>
                {courses.map((c: any) => <option key={c.id} value={c.id}>{c.title}</option>)}
             </select>
          </div>
        </div>

        <div className="flex-1 flex overflow-hidden">
          
          <div className="flex-1 flex flex-col bg-white border-r border-slate-200 overflow-hidden relative">
             <div className="flex items-center justify-between p-3 border-b border-slate-200 bg-slate-50 shrink-0">
                <div className="text-sm font-bold text-[#0a5482] flex items-center gap-2">
                   <span className="animate-pulse text-emerald-500">🟢</span> Đang xử lý: Trang {activePageIndex + 1}
                </div>
                <div className="text-[12px] font-medium text-slate-500">
                   💡 Bấm vào nút <b>&lt;/&gt;</b> trên thanh công cụ để dán mã HTML gốc.
                </div>
             </div>

             <div className="flex-1 overflow-auto bg-[#f8fafc] p-2">
                 <JoditEditor
                    ref={editorRef}
                    value={activePage?.content_html || ''}
                    config={editorConfig}
                    onBlur={(newContent) => handleHtmlChange(newContent)}
                 />
             </div>
          </div>

          <div className="w-80 bg-slate-50 flex flex-col shrink-0">
             <div className="p-4 border-b border-slate-200 bg-white">
                <button onClick={handleAddPage} className="w-full border-2 border-dashed border-[#2bd6eb] text-[#0a5482] bg-blue-50 hover:bg-[#2bd6eb] hover:text-white transition px-4 py-3 rounded-xl font-black text-sm flex items-center justify-center gap-2">
                   ➕ THÊM TRANG NỘI DUNG
                </button>
             </div>
             <div className="flex-1 overflow-y-auto p-4 space-y-3 custom-scrollbar">
                {pages.map((p, idx) => (
                   <div 
                      key={p.id}
                      onClick={() => setActivePageIndex(idx)}
                      className={`flex justify-between items-center p-3 rounded-xl cursor-pointer transition-all border-2 ${activePageIndex === idx ? 'bg-white border-[#2bd6eb] shadow-md' : 'bg-white border-slate-100 hover:border-slate-300'}`}
                   >
                      <div className="flex items-center gap-3">
                         <div className={`w-7 h-7 rounded-lg flex items-center justify-center text-xs font-black ${activePageIndex === idx ? 'bg-[#2bd6eb] text-white' : 'bg-slate-200 text-slate-500'}`}>
                            {idx + 1}
                         </div>
                         <span className="font-bold text-[13px] text-slate-700">Trang nội dung</span>
                      </div>
                      <button onClick={(e) => { e.stopPropagation(); handleRemovePage(idx); }} className="text-red-400 hover:text-red-600 font-bold p-1 bg-red-50 rounded">✖</button>
                   </div>
                ))}
             </div>
          </div>

        </div>
      </div>
    </div>
  );
}