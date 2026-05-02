import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';
// @ts-ignore
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';

const uploadToSupabase = async (file: File) => {
  const fileExt = file.name ? file.name.split('.').pop() : 'png';
  const fileName = `media_${Date.now()}_${Math.random().toString(36).substring(7)}.${fileExt}`;
  const { error } = await supabase.storage.from('test_assets').upload(`uploads/${fileName}`, file, { cacheControl: '3600', upsert: false });
  if (error) throw error;
  return supabase.storage.from('test_assets').getPublicUrl(`uploads/${fileName}`).data.publicUrl;
};

export default function LectureEditorModal({ lectureData, courses, defaultModuleId, onClose, onRefresh }: any) {
  const [title, setTitle] = useState(lectureData?.title || '');
  const [courseId, setCourseId] = useState(lectureData?.course_id || '');
  
  const [pages, setPages] = useState<any[]>([]);
  const [activePageId, setActivePageId] = useState<string | null>(null);
  const [isSaving, setIsSaving] = useState(false);
  const [isUploading, setIsUploading] = useState(false);
  const quillRef = useRef<any>(null);

  useEffect(() => {
    if (lectureData?.id && lectureData.id !== 'new') {
      fetchPages(lectureData.id);
    } else {
      const initPage = { id: 'temp_' + Date.now(), page_number: 1, content_html: '' };
      setPages([initPage]);
      setActivePageId(initPage.id);
    }
  }, [lectureData]);

  const fetchPages = async (lectureId: string) => {
    const { data } = await supabase.from('lecture_pages').select('*').eq('lecture_id', lectureId).order('page_number');
    if (data && data.length > 0) {
      setPages(data);
      setActivePageId(data[0].id);
    } else {
      const initPage = { id: 'temp_' + Date.now(), page_number: 1, content_html: '' };
      setPages([initPage]);
      setActivePageId(initPage.id);
    }
  };

  const handleAddPage = () => {
    const newPage = { id: 'temp_' + Date.now(), page_number: pages.length + 1, content_html: '' };
    setPages([...pages, newPage]);
    setActivePageId(newPage.id);
  };

  const handleDeletePage = (pageId: string) => {
    if (pages.length <= 1) return alert("Phải có ít nhất 1 trang nội dung!");
    if (!window.confirm("Xác nhận xóa trang nội dung này?")) return;
    const newPages = pages.filter(p => p.id !== pageId);
    setPages(newPages);
    if (activePageId === pageId) setActivePageId(newPages[0].id);
  };

  const updateActivePageContent = (html: string) => {
    setPages(pages.map(p => p.id === activePageId ? { ...p, content_html: html } : p));
  };

  const handleSave = async () => {
    if (!title.trim()) return alert("Vui lòng nhập tên bài giảng!");
    if (!courseId) return alert("Vui lòng chọn Khóa học để lưu trữ!");
    setIsSaving(true);

    try {
      let finalLectureId = lectureData?.id;
      let alertMessage = "✅ Đã lưu bài giảng thành công!";

      if (finalLectureId === 'new') {
        const { data, error } = await supabase.from('lectures').insert([{ 
           title, 
           course_id: courseId,
           module_id: defaultModuleId || null 
        }]).select().single();
        if (error) throw error;
        finalLectureId = data.id;
      } else {
        let updatePayload: any = { title, course_id: courseId };
        if (lectureData.course_id && courseId !== lectureData.course_id) {
            updatePayload.module_id = null;
            alertMessage = "✅ Đã lưu! Vì bạn đổi Khóa học, bài giảng đã tự động được gỡ khỏi Học phần cũ và chuyển về Kho chờ.";
        }
        const { error } = await supabase.from('lectures').update(updatePayload).eq('id', finalLectureId);
        if (error) throw error;
      }

      await supabase.from('lecture_pages').delete().eq('lecture_id', finalLectureId);
      
      const pagesToInsert = pages.map((p, index) => ({
        lecture_id: finalLectureId,
        page_number: index + 1,
        content_html: p.content_html
      }));

      const { error: pagesErr } = await supabase.from('lecture_pages').insert(pagesToInsert);
      if (pagesErr) throw pagesErr;

      alert(alertMessage);
      onRefresh();
      onClose();
    } catch (error: any) {
      alert("❌ Lỗi khi lưu: " + error.message);
    } finally {
      setIsSaving(false);
    }
  };

  const activePageContent = pages.find(p => p.id === activePageId)?.content_html || '';

  const imageHandler = () => {
    const input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.setAttribute('accept', 'image/*');
    input.click();
    input.onchange = async () => {
      const file = input.files ? input.files[0] : null;
      if (file) {
        setIsUploading(true);
        try {
          const url = await uploadToSupabase(file);
          const quill = quillRef.current?.getEditor();
          if (quill) {
            const range = quill.getSelection(true);
            quill.insertEmbed(range?.index || 0, 'image', url);
          }
        } catch (err) {
          alert("Lỗi tải ảnh!");
        } finally {
          setIsUploading(false);
        }
      }
    };
  };

  const modules = useMemo(() => ({
    toolbar: {
      container: [
        [{ 'header': [1, 2, 3, false] }],
        ['bold', 'italic', 'underline', 'strike'],
        [{ 'color': [] }, { 'background': [] }],
        [{ 'align': [] }],
        [{ 'list': 'ordered'}, { 'list': 'bullet' }],
        ['link', 'image', 'video'],
        ['clean']
      ],
      handlers: { image: imageHandler }
    }
  }), []);

  return (
    <div className="fixed inset-0 bg-[#e0e6ed] z-50 flex flex-col font-sans text-slate-800">
      <div className="h-14 bg-white border-b border-slate-300 px-6 flex justify-between items-center shadow-sm shrink-0">
         <h1 className="font-black text-[#0a5482] text-lg uppercase flex items-center gap-2">
            <span className="text-2xl">📝</span> Cập nhật Bài giảng
         </h1>
         <div className="flex gap-2">
            <button onClick={onClose} className="bg-white border border-slate-300 text-slate-600 hover:bg-slate-50 font-bold px-4 py-1.5 text-[13px] rounded shadow-sm transition">✖ Hủy bỏ</button>
            <button onClick={handleSave} disabled={isSaving} className="bg-[#1e88e5] hover:bg-[#1565c0] text-white font-bold px-5 py-1.5 text-[13px] rounded shadow-md transition disabled:opacity-50 flex items-center gap-1.5">
               {isSaving ? '⏳ Đang lưu...' : '💾 Lưu lại'}
            </button>
         </div>
      </div>

      <div className="flex-1 flex overflow-hidden">
         {/* KHU VỰC SOẠN THẢO BÊN TRÁI */}
         <div className="flex-1 flex flex-col border-r border-slate-300 bg-white shadow-xl z-10 min-w-0">
            <div className="px-6 pt-5 pb-4 bg-slate-50 border-b border-slate-200 flex flex-col md:flex-row justify-between items-start md:items-end gap-4 shrink-0">
               <div className="flex-1 w-full space-y-3">
                  <div className="flex items-center">
                     <label className="w-28 font-bold text-sm text-slate-600 shrink-0">Khóa học <span className="text-red-500">*</span></label>
                     <select value={courseId} onChange={(e) => setCourseId(e.target.value)} className="flex-1 max-w-md border border-slate-300 rounded px-3 py-1.5 text-sm outline-none bg-white focus:border-[#0a5482] transition-colors">
                        <option value="" disabled>-- Chọn Khóa học --</option>
                        {courses?.map((c: any) => <option key={c.id} value={c.id}>Khóa: {c.title}</option>)}
                     </select>
                  </div>
                  <div className="flex items-center">
                     <label className="w-28 font-bold text-sm text-slate-600 shrink-0">Tên bài giảng <span className="text-red-500">*</span></label>
                     <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Nhập tên bài giảng..." className="flex-1 max-w-md border border-slate-300 rounded px-3 py-1.5 text-sm outline-none focus:border-[#0a5482] transition-colors" />
                  </div>
               </div>
               
               <div className="shrink-0 flex flex-col items-end gap-3">
                  <div className="flex items-center gap-2">
                     <label className="font-bold text-[12px] text-slate-500">Hệ thống:</label>
                     {isUploading ? (
                        <span className="text-[11px] font-bold text-amber-600 bg-amber-50 border border-amber-200 px-2 py-1 rounded shadow-sm">⏳ Đang tải ảnh...</span>
                     ) : (
                        <span className="text-[11px] font-bold text-emerald-600 bg-emerald-50 border border-emerald-200 px-2 py-1 rounded shadow-sm">✅ Sẵn sàng</span>
                     )}
                  </div>
                  
                  <div className="bg-blue-50/80 px-4 py-1.5 rounded border border-blue-200 shadow-sm flex items-center justify-center">
                     <span className="font-black text-[13px] text-[#0a5482]">Đang soạn thảo: Trang {pages.findIndex(p => p.id === activePageId) + 1}</span>
                  </div>
               </div>
            </div>

            {/* ĐÃ FIX: Cho wrapper cuộn (overflow-y-auto) để nếu kéo Editor to quá thì khung bên ngoài tự sinh scrollbar */}
            <div className="flex-1 flex flex-col px-6 pt-4 pb-8 bg-slate-50 overflow-y-auto custom-scrollbar">
               {/* Khôi phục resize-y, set chiều cao mặc định h-[65vh] (khoảng 65% màn hình) để mép dưới hiện rõ */}
               <div className="border border-slate-300 rounded-lg flex flex-col bg-white shadow-sm resize-y overflow-hidden h-[65vh] min-h-[300px]">
                  <ReactQuill 
                     ref={quillRef}
                     theme="snow" 
                     value={activePageContent} 
                     onChange={updateActivePageContent} 
                     modules={modules} 
                     placeholder="Bắt đầu soạn thảo nội dung bài giảng..." 
                     className="flex-1 flex flex-col min-h-0 [&_.ql-container]:flex-1 [&_.ql-container]:!overflow-y-auto [&_.ql-editor]:text-[15px] [&_.ql-editor]:min-h-full [&_.ql-editor]:font-sans [&_.ql-editor]:leading-relaxed [&_.ql-toolbar]:bg-slate-50 [&_.ql-toolbar]:border-b-slate-300"
                  />
               </div>
            </div>
         </div>

         {/* KHU VỰC DANH SÁCH TRANG BÊN PHẢI */}
         <div className="w-[300px] shrink-0 h-full bg-[#f8fafc] flex flex-col">
            <div className="h-14 border-b border-slate-200 px-4 flex items-center justify-between shrink-0 bg-white">
               <h2 className="font-bold text-[#0a5482] text-[13px] uppercase tracking-wide">Danh sách trang</h2>
            </div>
            <div className="p-3 shrink-0">
               <button onClick={handleAddPage} className="bg-white border border-slate-300 text-slate-700 hover:text-blue-600 font-bold px-3 py-2 text-[13px] rounded shadow-sm w-full transition border-dashed hover:border-blue-400">➕ Thêm trang mới</button>
            </div>
            <div className="flex-1 overflow-y-auto px-3 pb-6 space-y-2 custom-scrollbar">
               {pages.map((page, index) => {
                  const isActive = page.id === activePageId;
                  const textSnippet = page.content_html.replace(/<[^>]*>?/gm, '').substring(0, 30) || '(Trống...)';
                  return (
                     <div key={page.id} onClick={() => setActivePageId(page.id)} className={`p-2.5 rounded-lg border flex items-center gap-2 cursor-pointer shadow-sm transition-colors ${isActive ? 'bg-blue-50 border-blue-400' : 'bg-white border-slate-200 hover:border-slate-300'}`}>
                        <div className="w-6 h-6 shrink-0 bg-slate-100 rounded border border-slate-300 flex items-center justify-center text-[11px] font-black text-slate-500">{index + 1}</div>
                        <div className="flex-1 min-w-0"><p className={`text-[13px] truncate ${isActive ? 'font-bold text-blue-800' : 'text-slate-600'}`}>{textSnippet}</p></div>
                        <div className="shrink-0 flex gap-0.5">
                           <button onClick={(e) => { e.stopPropagation(); setActivePageId(page.id); }} className="p-1 text-blue-500 hover:bg-blue-100 rounded transition text-xs">✏️</button>
                           <button onClick={(e) => { e.stopPropagation(); handleDeletePage(page.id); }} className="p-1 text-red-500 hover:bg-red-100 rounded transition text-xs">✖</button>
                        </div>
                     </div>
                  );
               })}
            </div>
         </div>
      </div>
    </div>
  );
}