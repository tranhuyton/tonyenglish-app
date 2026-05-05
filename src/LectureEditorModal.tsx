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

  // 🚀 STATE MỚI CHO BÀI TẬP ĐÍNH KÈM
  const [taskList, setTaskList] = useState<any[]>(lectureData?.task_list || []);
  const [rightTab, setRightTab] = useState<'pages' | 'tasks'>('pages');
  const [availableExercises, setAvailableExercises] = useState<any[]>([]);
  const [showExerciseDropdown, setShowExerciseDropdown] = useState(false);

  const editorRef = useRef(null);

  const editorConfig = useMemo(() => ({
    readonly: false,
    height: 550,
    allowResizeY: false,
    statusbar: false,
    toolbarAdaptive: false,
    defaultActionOnPaste: 'insert_as_html', 
    askBeforePasteHTML: false,
    askBeforePasteFromWord: false,
    uploader: { insertImageAsBase64URI: true },
    safeMode: false, 
    htmlParseBrowser: false,
    disablePlugins: ['clean-html', 'sanitize'], 
    cleanHTML: { fillEmptyParagraph: false, cleanOnPaste: false }
  }), []);

  useEffect(() => {
    if (lectureData.id !== 'new') fetchPages();
    else setPages([{ id: 'temp_1', page_number: 1, content_html: '' }]);
  }, [lectureData]);

  // 🚀 TỰ ĐỘNG LẤY ĐỀ THI / BÀI TẬP CỦA KHÓA HỌC HIỆN TẠI
  useEffect(() => {
    if (!courseId) {
       setAvailableExercises([]);
       return;
    }
    const fetchEx = async () => {
       const { data } = await supabase.from('tests')
          .select('id, title, content_json, test_type')
          .eq('course_id', courseId)
          .order('created_at', { ascending: false });
       if (data) setAvailableExercises(data);
    };
    fetchEx();
  }, [courseId]);

  const fetchPages = async () => {
    const { data } = await supabase.from('lecture_pages')
      .select('*')
      .eq('lecture_id', lectureData.id)
      .order('page_number', { ascending: true });
      
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

  const handleMoveUp = (index: number) => {
    if (index === 0) return;
    const newPages = [...pages];
    [newPages[index - 1], newPages[index]] = [newPages[index], newPages[index - 1]];
    newPages.forEach((p, i) => p.page_number = i + 1); 
    setPages(newPages);
    setActivePageIndex(index - 1);
  };

  const handleMoveDown = (index: number) => {
    if (index === pages.length - 1) return;
    const newPages = [...pages];
    [newPages[index + 1], newPages[index]] = [newPages[index], newPages[index + 1]];
    newPages.forEach((p, i) => p.page_number = i + 1); 
    setPages(newPages);
    setActivePageIndex(index + 1);
  };

  const handleRemovePage = (indexToRemove: number) => {
    if (pages.length <= 1) return alert('Bài giảng phải có ít nhất 1 trang!');
    if (!window.confirm('Xóa trang này?')) return;
    const newPages = pages.filter((_, idx) => idx !== indexToRemove).map((p, idx) => ({ ...p, page_number: idx + 1 }));
    setPages(newPages);
    setActivePageIndex(Math.max(0, indexToRemove - 1));
  };

  // 🚀 CHỨC NĂNG THÊM TASK VÀO BÀI GIẢNG
  const handleAddExerciseTask = (ex: any) => {
      const isExercise = ex.content_json?.basicInfo?.category === 'exercise';
      const newTask = {
          id: `task_${Date.now()}`,
          text: `${isExercise ? 'Làm bài tập' : 'Làm bài kiểm tra'}: ${ex.title}`,
          test_id: ex.id,
          type: 'exercise'
      };
      setTaskList([...taskList, newTask]);
      setShowExerciseDropdown(false);
  }

  const handleAddManualTask = () => {
      const text = window.prompt("Nhập nội dung ghi chú / nhiệm vụ:");
      if (text && text.trim()) {
          setTaskList([...taskList, { id: `task_${Date.now()}`, text: text.trim(), type: 'manual' }]);
      }
  }

  const handleSave = async () => {
    if (!title.trim() || !courseId) return alert('Vui lòng nhập tên và chọn khóa học!');
    setIsSaving(true);

    try {
      let currentLectureId = lectureData.id;
      // 🚀 ĐƯA THÊM TASK_LIST VÀO DỮ LIỆU LƯU TRỮ
      const lecPayload = { title, course_id: courseId, module_id: moduleId || null, is_published: true, task_list: taskList };
      
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
          
          {/* KHUNG SOẠN THẢO TRÁI */}
          <div className="flex-1 flex flex-col bg-white border-r border-slate-200 overflow-hidden relative">
             <div className="flex items-center justify-between p-3 border-b border-slate-200 bg-slate-50 shrink-0">
                <div className="text-sm font-bold text-[#0a5482] flex items-center gap-2">
                   <span className="animate-pulse text-emerald-500">🟢</span> Đang xử lý: Trang {activePageIndex + 1}
                </div>
                <div className="text-[12px] font-medium text-slate-500 bg-amber-100 text-amber-800 px-3 py-1 rounded">
                   ⚠️ Nhớ gõ nhẹ nhàng khi sửa text trong vùng biểu đồ anh nhé!
                </div>
             </div>

             <div className="flex-1 overflow-auto bg-[#f8fafc] p-2 relative">
                 <JoditEditor
                    ref={editorRef}
                    key={activePage?.id || activePageIndex}
                    value={activePage?.content_html || ''}
                    config={editorConfig}
                    onBlur={(newContent) => handleHtmlChange(newContent)}
                 />
             </div>
          </div>

          {/* KHUNG ĐIỀU KHIỂN PHẢI (TRANG & NHIỆM VỤ) */}
          <div className="w-[340px] bg-slate-50 flex flex-col shrink-0">
             
             {/* THANH TAB ĐIỀU KHIỂN */}
             <div className="flex bg-slate-200/50 p-1 m-3 rounded-xl border border-slate-200">
                <button onClick={() => setRightTab('pages')} className={`flex-1 py-2 text-[11px] font-black uppercase rounded-lg transition-colors ${rightTab === 'pages' ? 'bg-white shadow-sm text-[#0a5482]' : 'text-slate-500 hover:text-slate-700'}`}>Trang nội dung</button>
                <button onClick={() => setRightTab('tasks')} className={`flex-1 py-2 text-[11px] font-black uppercase rounded-lg transition-colors ${rightTab === 'tasks' ? 'bg-white shadow-sm text-[#0a5482]' : 'text-slate-500 hover:text-slate-700'}`}>Nhiệm vụ đính kèm</button>
             </div>

             {/* TAB 1: QUẢN LÝ SỐ TRANG */}
             {rightTab === 'pages' && (
                <>
                   <div className="px-4 pb-4 border-b border-slate-200">
                      <button onClick={handleAddPage} className="w-full border-2 border-dashed border-[#2bd6eb] text-[#0a5482] bg-blue-50 hover:bg-[#2bd6eb] hover:text-white transition px-4 py-3 rounded-xl font-black text-sm flex items-center justify-center gap-2">
                         ➕ THÊM TRANG MỚI
                      </button>
                   </div>
                   <div className="flex-1 overflow-y-auto p-4 space-y-3 custom-scrollbar">
                      {pages.map((p, idx) => (
                         <div key={p.id} onClick={() => setActivePageIndex(idx)} className={`flex justify-between items-center p-3 rounded-xl cursor-pointer transition-all border-2 ${activePageIndex === idx ? 'bg-white border-[#2bd6eb] shadow-md' : 'bg-white border-slate-100 hover:border-slate-300'}`}>
                            <div className="flex items-center gap-2">
                               <div className={`w-7 h-7 rounded-lg flex items-center justify-center text-xs font-black shrink-0 ${activePageIndex === idx ? 'bg-[#2bd6eb] text-white' : 'bg-slate-200 text-slate-500'}`}>{idx + 1}</div>
                               <span className="font-bold text-[13px] text-slate-700 truncate w-16">Trang {idx + 1}</span>
                            </div>
                            <div className="flex items-center gap-1 shrink-0">
                               <button onClick={(e) => { e.stopPropagation(); handleMoveUp(idx); }} disabled={idx === 0} className="w-6 h-6 flex items-center justify-center bg-slate-100 hover:bg-slate-200 rounded disabled:opacity-30 disabled:hover:bg-slate-100 transition" title="Lên trên">⬆️</button>
                               <button onClick={(e) => { e.stopPropagation(); handleMoveDown(idx); }} disabled={idx === pages.length - 1} className="w-6 h-6 flex items-center justify-center bg-slate-100 hover:bg-slate-200 rounded disabled:opacity-30 disabled:hover:bg-slate-100 transition" title="Xuống dưới">⬇️</button>
                               <button onClick={(e) => { e.stopPropagation(); handleRemovePage(idx); }} className="w-6 h-6 flex items-center justify-center text-red-500 hover:text-red-700 bg-red-50 hover:bg-red-100 rounded ml-1 transition" title="Xóa trang">✖</button>
                            </div>
                         </div>
                      ))}
                   </div>
                </>
             )}

             {/* TAB 2: QUẢN LÝ BÀI TẬP & NHIỆM VỤ */}
             {rightTab === 'tasks' && (
                <>
                   <div className="px-4 pb-4 border-b border-slate-200 flex flex-col gap-2 relative">
                      {/* NÚT CHỌN BÀI TẬP TỪ KHO */}
                      <button onClick={() => setShowExerciseDropdown(!showExerciseDropdown)} className="w-full border-2 border-dashed border-emerald-400 text-emerald-700 bg-emerald-50 hover:bg-emerald-500 hover:text-white transition px-2 py-3 rounded-xl font-black text-[12px] flex items-center justify-center">
                         ➕ CHỌN BÀI TẬP TỪ KHO
                      </button>
                      
                      {/* DROPDOWN DANH SÁCH BÀI TẬP */}
                      {showExerciseDropdown && (
                         <div className="absolute top-[60px] left-4 right-4 bg-white border border-slate-200 shadow-2xl rounded-xl max-h-64 overflow-y-auto z-50 animate-in fade-in zoom-in-95">
                            {availableExercises.length === 0 ? <div className="p-4 text-xs text-slate-400 text-center italic border-2 border-dashed m-2 rounded-lg">Khóa học chưa có bài tập/đề thi nào trong kho.</div> : (
                               availableExercises.map(ex => (
                                  <button key={ex.id} onClick={() => handleAddExerciseTask(ex)} className="w-full text-left px-4 py-3 text-xs font-bold hover:bg-emerald-50 hover:text-emerald-700 border-b border-slate-100 last:border-0 flex justify-between items-center transition-colors">
                                     <span className="truncate pr-2">{ex.title}</span>
                                     <span className={`shrink-0 text-[9px] px-1.5 py-0.5 rounded uppercase tracking-wider ${ex.content_json?.basicInfo?.category === 'exercise' ? 'bg-emerald-100 text-emerald-700' : 'bg-rose-100 text-rose-700'}`}>
                                        {ex.content_json?.basicInfo?.category === 'exercise' ? 'Bài tập' : 'Đề thi'}
                                     </span>
                                  </button>
                               ))
                            )}
                         </div>
                      )}

                      <button onClick={handleAddManualTask} className="w-full bg-white border border-slate-200 text-slate-500 hover:border-slate-400 hover:bg-slate-100 transition px-2 py-2 rounded-lg font-bold text-[12px] flex items-center justify-center shadow-sm">
                         📝 Thêm ghi chú văn bản
                      </button>
                   </div>
                   <div className="flex-1 overflow-y-auto p-4 space-y-3 custom-scrollbar bg-white">
                      {taskList.map((task, idx) => (
                         <div key={task.id} className="bg-slate-50 border border-slate-200 p-3 rounded-xl shadow-sm flex items-start justify-between group">
                            <div>
                               <div className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1.5">
                                 {task.type === 'exercise' ? '🔗 BÀI TẬP ĐÍNH KÈM' : '📝 NHIỆM VỤ ĐỌC'}
                               </div>
                               <div className="font-bold text-[#0a5482] text-[13px] leading-snug">{task.text}</div>
                            </div>
                            <button onClick={() => setTaskList(taskList.filter(t => t.id !== task.id))} className="text-red-400 hover:text-red-600 bg-white border border-red-100 hover:bg-red-50 w-6 h-6 rounded flex items-center justify-center transition-all ml-2 shrink-0">✖</button>
                         </div>
                      ))}
                      {taskList.length === 0 && <div className="text-center text-xs text-slate-400 italic mt-8 border-2 border-dashed border-slate-200 p-6 rounded-2xl mx-2">Chưa có nhiệm vụ nào được giao.<br/>Học sinh sẽ chỉ cần đọc nội dung.</div>}
                   </div>
                </>
             )}
          </div>

        </div>
      </div>
    </div>
  );
}