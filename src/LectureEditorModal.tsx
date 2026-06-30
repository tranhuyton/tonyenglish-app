import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import { supabase } from './supabase';
import JoditEditor from 'jodit-react';
import ReactPlayer from 'react-player';
import { fixJoditIndentAndOutdent } from './utils/joditFix';

// =========================================================================
// COMPONENT CHỌN BÀI TẬP VỚI BỘ GIẢM XÓC (DEBOUNCE) TÌM KIẾM
// =========================================================================
const ExerciseSelectionModal = React.memo(({ availableExercises, onClose, onAddExercise }: any) => {
  const [searchInput, setSearchInput] = useState(''); 
  const [exSearch, setExSearch] = useState('');       
  const [exFilter, setExFilter] = useState('all');

  useEffect(() => {
    const timer = setTimeout(() => setExSearch(searchInput), 250);
    return () => clearTimeout(timer);
  }, [searchInput]);

  const filteredExercises = useMemo(() => {
      return availableExercises.filter((ex: any) => {
          const matchesSearch = ex.title.toLowerCase().includes(exSearch.toLowerCase());
          const cat = ex.content_json?.basicInfo?.category || 'test';
          const matchesFilter = exFilter === 'all' || cat === exFilter;
          return matchesSearch && matchesFilter;
      });
  }, [availableExercises, exSearch, exFilter]);

  return (
    <div className="fixed inset-0 z-[200] bg-slate-900/80 flex items-center justify-center p-4 animate-in fade-in">
        <div className="bg-white rounded-3xl shadow-2xl w-full max-w-3xl max-h-[85vh] flex flex-col overflow-hidden animate-in zoom-in-95">
            <div className="px-6 py-5 border-b border-slate-100 flex justify-between items-center bg-slate-50 shrink-0">
                <h3 className="font-black text-[#0a5482] text-lg uppercase tracking-tight">Thêm Bài Tập / Đề Thi Vào Bài Giảng</h3>
                <button 
                    onClick={onClose} 
                    className="w-8 h-8 rounded-full bg-white border border-slate-200 hover:bg-slate-200 hover:text-red-500 flex items-center justify-center text-xl font-bold text-slate-400"
                >
                    &times;
                </button>
            </div>
            
            <div className="p-5 border-b border-slate-100 flex flex-col sm:flex-row gap-3 bg-white shrink-0">
                <div className="relative flex-1">
                    <input 
                        type="text" 
                        placeholder="Nhập tên bài tập để tìm kiếm..." 
                        value={searchInput} 
                        onChange={e => setSearchInput(e.target.value)} 
                        className="w-full bg-slate-50 border border-slate-200 rounded-xl pl-10 pr-4 py-3 text-sm outline-none focus:border-[#0a5482]" 
                        autoFocus 
                    />
                    <span className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400">🔍</span>
                </div>
                <select 
                    value={exFilter} 
                    onChange={e => setExFilter(e.target.value)} 
                    className="w-full sm:w-48 bg-slate-50 border border-slate-200 rounded-xl px-4 py-3 text-sm outline-none focus:border-[#0a5482] font-bold text-slate-600 cursor-pointer"
                >
                    <option value="all">Tất cả thể loại</option>
                    <option value="exercise">Chỉ Bài tập</option>
                    <option value="test">Chỉ Đề thi</option>
                </select>
            </div>
            
            <div className="flex-1 overflow-y-auto p-4 bg-[#f8fafc] custom-scrollbar">
                {filteredExercises.length === 0 ? (
                    <div className="p-10 text-center flex flex-col items-center justify-center border-2 border-dashed border-slate-200 rounded-2xl m-4 bg-white">
                       <span className="text-4xl mb-3 opacity-50">📭</span>
                       <span className="text-slate-400 font-bold text-[15px]">Không tìm thấy bài tập/đề thi nào.</span>
                       <span className="text-slate-400 text-[13px] mt-1">Anh hãy kiểm tra lại bộ lọc hoặc tên tìm kiếm nhé!</span>
                    </div>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                        {filteredExercises.map((ex: any) => (
                            <div key={ex.id} className="flex justify-between items-center bg-white border border-slate-200 p-4 rounded-xl hover:border-emerald-400 hover:shadow-md group">
                                <div className="flex flex-col flex-1 min-w-0 pr-3">
                                    <span className="font-bold text-slate-700 text-[14px] truncate group-hover:text-emerald-700">
                                        {ex.title}
                                    </span>
                                    <span className={`w-fit mt-1.5 text-[9px] px-2 py-0.5 rounded uppercase font-black tracking-wider ${ex.content_json?.basicInfo?.category === 'exercise' ? 'bg-emerald-100 text-emerald-700' : 'bg-rose-100 text-rose-700'}`}>
                                        {ex.content_json?.basicInfo?.category === 'exercise' ? 'BÀI TẬP' : 'ĐỀ THI'}
                                    </span>
                                </div>
                                <button 
                                    onClick={() => onAddExercise(ex)} 
                                    className="bg-emerald-50 border border-emerald-200 text-emerald-600 hover:bg-emerald-500 hover:text-white px-4 py-2 rounded-lg text-xs font-black active:scale-95 shrink-0"
                                >
                                    THÊM ➕
                                </button>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    </div>
  );
});


// =========================================================================
// CÁCH LY EDITOR: BỎ THANH CUỘN NGANG, CHO NÚT TỰ ĐỘNG XUỐNG DÒNG GỌN GÀNG
// =========================================================================
const MemoizedEditor = React.memo(({ initialValue, config, onHtmlChange }: any) => {
  const editorRef = useRef(null);
  return (
     <div className="w-full bg-white relative rounded-b-xl overflow-hidden shadow-sm border border-slate-200">
         <style>{`
            .jodit-toolbar__box {
                flex-wrap: wrap !important;
            }
            
            /* --- CĂN CHỈNH LẠI BULLET POINT CHUẨN BRUTALIST IDP/BC --- */
            .jodit-wysiwyg ul {
                padding-left: 1.5rem !important;
                margin: 0.5rem 0 !important;
                list-style-type: disc; /* Level 1: Chấm đen */
            }
            .jodit-wysiwyg ol {
                padding-left: 1.5rem !important;
                margin: 0.5rem 0 !important;
                list-style-type: decimal outside;
            }
            
            .jodit-wysiwyg ul ul {
                list-style-type: circle; /* Level 2: Vòng tròn trắng */
            }
            .jodit-wysiwyg ul ul ul {
                list-style-type: square; /* Level 3: Hình vuông đen */
            }

            /* Ép thẳng vào thẻ LI để trị dứt điểm inline-style của Jodit */
            .jodit-wysiwyg ul > li, .jodit-wysiwyg ol > li {
                margin-bottom: 0.25rem !important;
            }

            /* FIX LỖI RỚT DÒNG: Ép thẻ p bên trong li nằm trên cùng 1 hàng */
            .jodit-wysiwyg li > p, 
            .jodit-wysiwyg li > div {
                display: inline !important; 
                margin: 0 !important;
            }

            /* --- FIX HIỂN THỊ BẢNG EXCEL TRONG EDITOR --- */
            .jodit-wysiwyg table {
                width: 100% !important;
                border-collapse: collapse !important;
                margin: 1.5rem auto !important;
            }
            .jodit-wysiwyg th, .jodit-wysiwyg td {
                border: 1px solid #cbd5e1 !important;
                padding: 12px 16px !important;
                white-space: normal !important;
                word-break: break-word !important;
            }
            /* Trả lại quyền Vertical Align cho Editor */
            .jodit-wysiwyg td { vertical-align: top; }
            .jodit-wysiwyg [style*="vertical-align: middle"], .jodit-wysiwyg [valign="middle"] { vertical-align: middle !important; }
            .jodit-wysiwyg [style*="vertical-align: bottom"], .jodit-wysiwyg [valign="bottom"] { vertical-align: bottom !important; }
            .jodit-wysiwyg [style*="vertical-align: top"], .jodit-wysiwyg [valign="top"] { vertical-align: top !important; }

            /* --- BÀN TAY SẮT: ĐỒNG BỘ FONT CHỮ & GIÃN DÒNG MẶC ĐỊNH --- */
            .jodit-wysiwyg {
                font-family: inherit !important; 
                line-height: 1.7 !important;     
                color: #334155;                  
                font-size: 15px;                 
            }
            
            /* Ép các thẻ con kế thừa Font và Giãn dòng, KHÔNG ép chết Size và Màu */
            .jodit-wysiwyg p,
            .jodit-wysiwyg div,
            .jodit-wysiwyg span,
            .jodit-wysiwyg li,
            .jodit-wysiwyg td,
            .jodit-wysiwyg th,
            .jodit-wysiwyg b,
            .jodit-wysiwyg strong,
            .jodit-wysiwyg i,
            .jodit-wysiwyg em {
                font-family: inherit !important;
                line-height: inherit !important;
            }
            
            /* Giữ lại màu cho thẻ link */
            .jodit-wysiwyg a {
                color: #00a651 !important;
                text-decoration: underline !important;
                font-family: inherit !important;
            }
            
            /* --- FIX LỖI KHOẢNG TRẮNG DƯỚI ẢNH TRONG BẢNG --- */
            .jodit-wysiwyg table p {
                margin: 0 !important;
            }
            .jodit-wysiwyg td img {
                display: block !important; 
                max-width: 100% !important;
                height: auto !important;
                margin: 0 auto !important; 
            }
            /* Ép ẩn hoàn toàn các thẻ P rỗng hoặc chỉ chứa thẻ BR do Editor sinh ra trong bảng */
            .jodit-wysiwyg td > p:empty,
            .jodit-wysiwyg td > p:has(> br:only-child) {
                display: none !important;
                margin: 0 !important;
                padding: 0 !important;
                height: 0 !important;
            }

            /* --- FIX NÚT UPDATE/SAVE TRONG BẢNG CHỈNH ẢNH --- */
            html body div.jodit-dialog__footer {
                display: flex !important;
                justify-content: flex-end !important;
                gap: 8px !important;
                padding: 12px !important;
                border-top: 1px solid #eee !important;
                background: #f9f9f9 !important;
                visibility: visible !important;
                opacity: 1 !important;
            }
            html body div.jodit-dialog__footer button.jodit-button_primary, 
            html body div.jodit-dialog__footer button.jodit-ui-button_primary,
            html body div.jodit-dialog__footer button[type="submit"] {
                background-color: #00a651 !important; 
                color: #ffffff !important;
                padding: 6px 20px !important;
                border-radius: 4px !important;
                font-weight: bold !important;
                border: none !important;
                opacity: 1 !important;
                visibility: visible !important;
                display: inline-flex !important;
                text-shadow: none !important;
                box-shadow: none !important;
            }
            html body div.jodit-dialog__box {
                max-height: 85vh !important;
                overflow-y: auto !important;
            }
         `}</style>
         <JoditEditor
            ref={editorRef}
            value={initialValue}
            config={config}
            onBlur={onHtmlChange}
         />
     </div>
  );
}, () => true);


// =========================================================================
// MÀN HÌNH CHÍNH LECTURE EDITOR
// =========================================================================
export default function LectureEditorModal({ lectureData, courses, onClose, onRefresh }: any) {
  const [title, setTitle] = useState(lectureData?.title || '');
  const [courseId, setCourseId] = useState(lectureData?.course_id || '');
  const [moduleId, setModuleId] = useState(lectureData?.module_id || '');
  
  // 🚀 State quản lý BÍ KÍP AI (Long Context Text)
  const [tutorContext, setTutorContext] = useState(lectureData?.tutor_context || '');
  
  // 🚀 State Upload Ảnh Bí Kíp
  const [isUploadingAnswerImg, setIsUploadingAnswerImg] = useState(false);
  const answerImgInputRef = useRef<HTMLInputElement>(null);

  const [pages, setPages] = useState<any[]>([]);
  const [activePageIndex, setActivePageIndex] = useState(0);
  const [isSaving, setIsSaving] = useState(false);

  const [taskList, setTaskList] = useState<any[]>(lectureData?.task_list || []);
  
  // Đã thêm tab 'context' vào đây
  const [rightTab, setRightTab] = useState<'pages' | 'tasks' | 'context'>('pages');
  
  const [availableExercises, setAvailableExercises] = useState<any[]>([]);
  const [showExerciseModal, setShowExerciseModal] = useState(false);

  // Giữ nguyên cấu hình chuẩn của anh
  const editorConfig = useMemo(() => ({
    readonly: false,
    height: 600, 
    allowResizeY: true, 
    statusbar: true, 
    toolbarSticky: true, 
    toolbarAdaptive: false,
    
    // FIX PHÍM TAB: Ép thực hiện lệnh thụt lề (indent) thay vì chuyển focus sang ô khác
    tabAction: 'indent',
    tabIndex: -1,
    
    // NÚT "SOURCE" ĐƯỢC ĐẶT Ở CUỐI CÙNG (CẠNH PRINT)
    buttons: [
      'bold', 'italic', 'underline', 'strikethrough', '|',
      'superscript', 'subscript', '|',
      'ul', 'ol', 'outdent', 'indent', '|',
      'font', 'fontsize', 'brush', 'paragraph', '|',
      'image', 'video', 'file', 'table', 'link', '|',
      'align', 'undo', 'redo', '|',
      'hr', 'eraser', 'copyformat', 'symbol', 'fullsize', 'print', 'source'
    ],
    
    // --- FIX PASTE: insert_as_html để giữ nguyên cấu trúc bảng từ Excel/Word ---
    defaultActionOnPaste: 'insert_as_html', 
    askBeforePasteHTML: false,
    askBeforePasteFromWord: false,
    uploader: { insertImageAsBase64URI: true }, 
    safeMode: false, 
    htmlParseBrowser: false,
    cleanHTML: { 
        fillEmptyParagraph: false, 
        cleanOnPaste: false, // Tắt clean mặc định của Jodit để dùng bộ lọc Custom bên dưới
        replaceNBSP: true,
        removeOnError: false 
    },
    
    // --- BỘ LỌC DOM PARSER BÀN TAY SẮT: Lột sạch style rác, giữ nguyên Bảng/Đậm/Nghiêng ---
    events: {
      processPaste: (event: any, html: any) => {
        if (!html || typeof html !== 'string') return html;
        try {
          // Bắt trình duyệt giả lập đọc đoạn HTML vừa paste
          const parser = new DOMParser();
          const doc = parser.parseFromString(html, 'text/html');
          
          // 1. Tiêu diệt các thẻ CSS, Script, Meta ẩn dính từ web khác
          doc.querySelectorAll('style, meta, script, link, title').forEach(n => n.remove());
          
          // 2. Quét TẤT CẢ các thẻ còn lại
          doc.querySelectorAll('*').forEach((el: any) => {
            // Xóa tận gốc các định dạng nội tuyến (inline styles) gây lệch giao diện
            if (el.style) {
              el.style.removeProperty('font-family');
              el.style.removeProperty('font-size');
              el.style.removeProperty('line-height');
              el.style.removeProperty('background-color');
              el.style.removeProperty('background');
              el.style.removeProperty('margin');
              el.style.removeProperty('margin-top');
              el.style.removeProperty('margin-bottom');
              el.style.removeProperty('padding');
              
              // Giữ lại màu cho thẻ Link, còn lại xóa màu chữ rác
              if (el.tagName !== 'A') {
                el.style.removeProperty('color');
              }
              
              // Nếu style rỗng thì xóa luôn thuộc tính style cho sạch code
              if (el.getAttribute('style') === '') {
                el.removeAttribute('style');
              }
            }
            
            // Xóa các class và ID lạ do web khác tự gen ra
            el.removeAttribute('class');
            el.removeAttribute('id');
            
            // Lột bỏ định dạng của các thẻ <font> cổ lỗ sĩ
            if (el.tagName === 'FONT') {
              el.removeAttribute('face');
              el.removeAttribute('size');
              el.removeAttribute('color');
            }
          });
          
          // Trả lại HTML sạch sẽ, chỉ còn cấu trúc nguyên thủy
          return doc.body.innerHTML;
        } catch(err) {
          console.error("Lỗi parse HTML:", err);
          return html; // Fallback nếu có lỗi
        }
      },
      beforeCommand: (command: string, _1: any, _2: any, _3: any, editor: any) => {
        const outdentResult = fixJoditIndentAndOutdent(command, _1, _2, _3, editor);
        if (outdentResult === false) return false;
      },
      beforeInsertNode: (node: any) => {
        if (node && node.tagName === 'IMG') {
          node.style.width = '80%';
          node.style.display = 'block';
          node.style.marginLeft = 'auto';
          node.style.marginRight = 'auto';
        }
      }
    }
  }), []);

  useEffect(() => {
    if (lectureData.id !== 'new') {
        fetchPages();
    } else {
        setPages([{ id: 'temp_1', page_number: 1, content_html: '' }]);
    }
  }, [lectureData]);

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
      
    if (data && data.length > 0) {
        const parsedPages = data.map((p: any) => {
            const isHidden = String(p.content_html || '').startsWith('<!-- hidden -->');
            return {
                ...p,
                is_hidden: isHidden,
                content_html: isHidden ? p.content_html.substring('<!-- hidden -->'.length) : p.content_html
            };
        });
        setPages(parsedPages);
    } else {
        setPages([{ id: 'temp_1', page_number: 1, content_html: '', is_hidden: false }]);
    }
  };

  const activePage = pages[activePageIndex] || null;

  const handleHtmlChange = useCallback((newHtml: string) => {
    setPages(prevPages => {
        const updated = [...prevPages];
        if (updated[activePageIndex]) {
            updated[activePageIndex].content_html = newHtml;
        }
        return updated;
    });
  }, [activePageIndex]);

  const handleAddPage = () => {
    setPages([
        ...pages, 
        { id: `temp_${Date.now()}`, page_number: pages.length + 1, content_html: '', is_hidden: false }
    ]);
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
    if (pages.length <= 1) {
        return alert('Bài giảng phải có ít nhất 1 trang!');
    }
    if (!window.confirm('Xóa trang này?')) return;
    const newPages = pages
        .filter((_, idx) => idx !== indexToRemove)
        .map((p, idx) => ({ ...p, page_number: idx + 1 }));
    setPages(newPages);
    setActivePageIndex(Math.max(0, indexToRemove - 1));
  };

  const toggleHidePage = (index: number) => {
    setPages(prevPages => {
        const updated = [...prevPages];
        if (updated[index]) {
            updated[index] = {
                ...updated[index],
                is_hidden: !updated[index].is_hidden
            };
        }
        return updated;
    });
  };

  const handleAddExerciseTask = useCallback((ex: any) => {
      const isExercise = ex.content_json?.basicInfo?.category === 'exercise';
      const newTask = {
          id: `task_${Date.now()}`,
          text: `${isExercise ? 'Làm bài tập' : 'Làm bài kiểm tra'}: ${ex.title}`,
          test_id: ex.id,
          type: 'exercise'
      };
      setTaskList(prev => [...prev, newTask]);
      setShowExerciseModal(false); 
  }, []);

  const handleAddManualTask = () => {
      const text = window.prompt("Nhập nội dung ghi chú / nhiệm vụ:");
      if (text && text.trim()) {
          setTaskList([
              ...taskList, 
              { id: `task_${Date.now()}`, text: text.trim(), type: 'manual' }
          ]);
      }
  }

  const handleEditTask = (task: any) => {
      const newText = window.prompt("Sửa đổi tên hiển thị của nhiệm vụ:", task.text);
      if (newText && newText.trim() !== "") {
          setTaskList(taskList.map(t => t.id === task.id ? { ...t, text: newText.trim() } : t));
      }
  }

  const handleMoveTaskUp = (index: number) => {
      if (index === 0) return;
      const newTasks = [...taskList];
      [newTasks[index - 1], newTasks[index]] = [newTasks[index], newTasks[index - 1]];
      setTaskList(newTasks);
  }

  const handleMoveTaskDown = (index: number) => {
      if (index === taskList.length - 1) return;
      const newTasks = [...taskList];
      [newTasks[index + 1], newTasks[index]] = [newTasks[index], newTasks[index + 1]];
      setTaskList(newTasks);
  }

  // =========================================================================
  // 🚀 CỐT LÕI XỬ LÝ UPLOAD ẢNH CHUNG (DÙNG CHO CẢ NÚT BẤM VÀ CTRL+V)
  // =========================================================================
  const processImageUpload = async (file: File) => {
    if (file.size > 10 * 1024 * 1024) {
        alert('Dung lượng ảnh tối đa 10MB.');
        return;
    }
    
    setIsUploadingAnswerImg(true);
    try {
        const fileExt = file.name.split('.').pop() || 'png';
        const fileName = `answer_${Date.now()}.${fileExt}`;
        
        // Tải lên Supabase Storage bucket 'documents'
        const { error } = await supabase.storage.from('documents').upload(fileName, file);
        if (error) throw error;
        
        // Lấy URL công khai
        const { data } = supabase.storage.from('documents').getPublicUrl(fileName);
        
        // Chèn Tag Ảnh vào ô Text Bí Kíp
        const newImageTag = `\n[IMAGE_ANSWER: ${data.publicUrl}]\n`;
        setTutorContext(prev => prev + newImageTag);
        
    } catch (err: any) {
        alert('Lỗi tải ảnh: ' + err.message);
    } finally {
        setIsUploadingAnswerImg(false);
    }
  };

  // Xử lý khi bấm nút Upload thủ công
  const handleUploadAnswerImage = async (event: React.ChangeEvent<HTMLInputElement>) => {
      const file = event.target.files?.[0];
      if (file) {
          await processImageUpload(file);
      }
      if (answerImgInputRef.current) answerImgInputRef.current.value = '';
  };

  // Xử lý khi ấn Ctrl+V (Paste) vào thẳng Textarea
  const handlePasteImage = async (e: React.ClipboardEvent<HTMLTextAreaElement>) => {
      const items = e.clipboardData?.items;
      if (!items) return;

      for (let i = 0; i < items.length; i++) {
          // Bắt các item có type là image
          if (items[i].type.indexOf('image') !== -1) {
              e.preventDefault(); // Chặn hành vi paste chuỗi Base64 dài dằng dặc
              const file = items[i].getAsFile();
              if (file) {
                  await processImageUpload(file);
              }
              break; // Chỉ xử lý ảnh đầu tiên nếu copy nhiều thứ
          }
      }
  };

  const handleSave = async () => {
    if (!title.trim() || !courseId) return alert('Vui lòng nhập tên và chọn khóa học!');
    setIsSaving(true);

    try {
      let currentLectureId = lectureData.id;
      
      // Khởi tạo Payload, bao gồm cả biến tutor_context
      const lecPayload: any = { 
         title, 
         course_id: courseId, 
         module_id: moduleId || null, 
         is_published: true, 
         task_list: taskList,
         tutor_context: tutorContext.trim() || null
      };
      
      if (currentLectureId === 'new') {
        // Thuật toán đánh số thứ tự
        let maxOrder = 0;
        
        if (moduleId) {
            const { data: existingLecs } = await supabase.from('lectures').select('order_index').eq('module_id', moduleId);
            if (existingLecs && existingLecs.length > 0) {
                maxOrder = Math.max(...existingLecs.map(l => l.order_index || 0));
            }
        } else {
            const { data: existingLecs } = await supabase.from('lectures').select('order_index').eq('course_id', courseId).is('module_id', null);
            if (existingLecs && existingLecs.length > 0) {
                maxOrder = Math.max(...existingLecs.map(l => l.order_index || 0));
            }
        }
        
        lecPayload.order_index = maxOrder + 1;

        // Lưu mới vào DB
        const { data: newLec, error: err1 } = await supabase.from('lectures').insert([lecPayload]).select().single();
        if (err1) throw err1;
        currentLectureId = newLec.id;
      } else {
        // Cập nhật bài cũ
        const { error: err2 } = await supabase.from('lectures').update(lecPayload).eq('id', currentLectureId);
        if (err2) throw err2;
      }

      // Cập nhật Pages
      await supabase.from('lecture_pages').delete().eq('lecture_id', currentLectureId);

      const pagesToInsert = pages.map((p, idx) => ({
        lecture_id: currentLectureId,
        page_number: idx + 1,
        content_html: p.is_hidden ? `<!-- hidden -->${p.content_html || ''}` : (p.content_html || '')
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
      <div className="bg-[#f4f6f9] w-full max-w-7xl h-[95vh] rounded-2xl shadow-2xl flex flex-col overflow-hidden animate-in zoom-in-95 relative z-10">
        
        <div className="h-16 bg-white border-b border-slate-200 px-6 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-4">
             <div className="w-10 h-10 rounded-xl bg-blue-100 flex items-center justify-center text-xl">📝</div>
             <h2 className="text-lg font-black text-[#0a5482] uppercase tracking-wide">
               {lectureData.id === 'new' ? 'Tạo Bài Giảng Mới' : 'Cập Nhật Bài Giảng'}
             </h2>
          </div>
          <div className="flex items-center gap-3">
            <button 
                onClick={onClose} 
                className="px-5 py-2 rounded-xl text-slate-500 font-bold hover:bg-slate-100 transition"
            >
                Hủy bỏ ✖
            </button>
            <button 
                onClick={handleSave} 
                disabled={isSaving} 
                className="bg-[#2bd6eb] hover:bg-[#1bc1d6] text-white px-8 py-2 rounded-xl font-black shadow-lg flex items-center gap-2 transition disabled:opacity-50"
            >
              {isSaving ? '⏳ ĐANG LƯU...' : '💾 LƯU LẠI'}
            </button>
          </div>
        </div>

        <div className="p-4 bg-white border-b border-slate-200 flex gap-4 shrink-0">
          <div className="flex-1">
             <label className="text-[11px] font-black text-slate-400 uppercase tracking-widest mb-1 block">Tên bài giảng <span className="text-red-500">*</span></label>
             <input 
                 value={title} 
                 onChange={(e) => setTitle(e.target.value)} 
                 placeholder="Nhập tên bài giảng..." 
                 className="w-full bg-slate-50 border border-slate-200 rounded-lg px-4 py-2 font-bold text-slate-700 outline-none focus:border-[#2bd6eb]" 
             />
          </div>
          <div className="w-64">
             <label className="text-[11px] font-black text-slate-400 uppercase tracking-widest mb-1 block">Khóa học <span className="text-red-500">*</span></label>
             <select 
                 value={courseId} 
                 onChange={(e) => setCourseId(e.target.value)} 
                 className="w-full bg-slate-50 border border-slate-200 rounded-lg px-4 py-2 font-bold text-slate-700 outline-none focus:border-[#2bd6eb]"
             >
                <option value="" disabled>Chọn khóa học...</option>
                {courses.map((c: any) => (
                    <option key={c.id} value={c.id}>{c.title}</option>
                ))}
             </select>
          </div>
        </div>

        <div className="flex-1 flex overflow-hidden">
          
          <div className="flex-1 flex flex-col bg-white border-r border-slate-200 overflow-hidden relative">
             <div className="flex items-center justify-between p-3 border-b border-slate-200 bg-slate-50 shrink-0">
                <div className="text-sm font-bold text-[#0a5482] flex items-center gap-2">
                   <span className="animate-pulse text-emerald-500">🟢</span> Đang xử lý: Trang {activePageIndex + 1}
                </div>
             </div>

             <div className="flex-1 overflow-y-auto bg-[#f8fafc] p-4 custom-scrollbar">
                 <MemoizedEditor 
                    key={activePage?.id || `empty_${activePageIndex}`} 
                    initialValue={activePage?.content_html || ''}
                    config={editorConfig}
                    onHtmlChange={handleHtmlChange}
                 />
             </div>
          </div>

          <div className="w-[340px] md:w-[380px] bg-slate-50 flex flex-col shrink-0">
             
             <div className="flex bg-slate-200/50 p-1 m-3 rounded-xl border border-slate-200">
                <button 
                    onClick={() => setRightTab('pages')} 
                    className={`flex-1 py-2 text-[10px] sm:text-[11px] font-black uppercase rounded-lg transition-colors ${rightTab === 'pages' ? 'bg-white shadow-sm text-[#0a5482]' : 'text-slate-500 hover:text-slate-700'}`}
                >
                    📑 Nội dung
                </button>
                <button 
                    onClick={() => setRightTab('tasks')} 
                    className={`flex-1 py-2 text-[10px] sm:text-[11px] font-black uppercase rounded-lg transition-colors ${rightTab === 'tasks' ? 'bg-white shadow-sm text-[#0a5482]' : 'text-slate-500 hover:text-slate-700'}`}
                >
                    📌 Nhiệm vụ
                </button>
                <button 
                    onClick={() => setRightTab('context')} 
                    className={`flex-1 py-2 text-[10px] sm:text-[11px] font-black uppercase rounded-lg transition-colors flex items-center justify-center gap-1 ${rightTab === 'context' ? 'bg-amber-100 shadow-sm text-amber-700 border border-amber-200' : 'text-slate-500 hover:text-amber-600'}`}
                >
                    🧠 Bí Kíp AI
                </button>
             </div>

             {/* TAB NỘI DUNG */}
             {rightTab === 'pages' && (
                <>
                   <div className="px-4 pb-4 border-b border-slate-200">
                      <button 
                          onClick={handleAddPage} 
                          className="w-full border-2 border-dashed border-[#2bd6eb] text-[#0a5482] bg-blue-50 hover:bg-[#2bd6eb] hover:text-white transition px-4 py-3 rounded-xl font-black text-sm flex items-center justify-center gap-2"
                      >
                         ➕ THÊM TRANG MỚI
                      </button>
                   </div>
                   <div className="flex-1 overflow-y-auto p-4 space-y-3 custom-scrollbar">
                      {pages.map((p, idx) => (
                         <div key={p.id} onClick={() => setActivePageIndex(idx)} className={`flex justify-between items-center p-3 rounded-xl cursor-pointer transition-all border-2 ${activePageIndex === idx ? 'bg-white border-[#2bd6eb] shadow-md' : 'bg-white border-slate-100 hover:border-slate-300'} ${p.is_hidden ? 'bg-slate-100/50 opacity-75' : ''}`}>
                            <div className="flex items-center gap-2 min-w-0 flex-1">
                               <div className={`w-7 h-7 rounded-lg flex items-center justify-center text-xs font-black shrink-0 ${activePageIndex === idx ? 'bg-[#2bd6eb] text-white' : 'bg-slate-200 text-slate-500'}`}>
                                   {idx + 1}
                               </div>
                               <span className={`font-bold text-[13px] truncate flex-1 ${p.is_hidden ? 'text-slate-400 line-through' : 'text-slate-700'}`}>
                                  Trang {idx + 1} {p.is_hidden && <span className="text-[10px] text-red-500 font-normal no-underline ml-1">(Ẩn)</span>}
                               </span>
                            </div>
                            <div className="flex items-center gap-1 shrink-0">
                               <button 
                                   onClick={(e) => { e.stopPropagation(); toggleHidePage(idx); }} 
                                   className={`w-6 h-6 flex items-center justify-center rounded transition text-xs hover:bg-slate-100`}
                                   title={p.is_hidden ? "Hiện trang" : "Ẩn trang"}
                               >
                                   {p.is_hidden ? '🙈' : '👁️'}
                               </button>
                               <button onClick={(e) => { e.stopPropagation(); handleMoveUp(idx); }} disabled={idx === 0} className="w-6 h-6 flex items-center justify-center bg-slate-100 hover:bg-slate-200 rounded disabled:opacity-30 disabled:hover:bg-slate-100 transition" title="Lên trên">⬆️</button>
                               <button onClick={(e) => { e.stopPropagation(); handleMoveDown(idx); }} disabled={idx === pages.length - 1} className="w-6 h-6 flex items-center justify-center bg-slate-100 hover:bg-slate-200 rounded disabled:opacity-30 disabled:hover:bg-slate-100 transition" title="Xuống dưới">⬇️</button>
                               <button onClick={(e) => { e.stopPropagation(); handleRemovePage(idx); }} className="w-6 h-6 flex items-center justify-center text-red-500 hover:text-red-700 bg-red-50 hover:bg-red-100 rounded ml-1 transition" title="Xóa trang">✖</button>
                            </div>
                         </div>
                      ))}
                   </div>
                </>
             )}

             {/* TAB NHIỆM VỤ */}
             {rightTab === 'tasks' && (
                <>
                   <div className="px-4 pb-4 border-b border-slate-200 flex flex-col gap-2 relative">
                      <button 
                          onClick={() => setShowExerciseModal(true)} 
                          className="w-full border-2 border-dashed border-emerald-400 text-emerald-700 bg-emerald-50 hover:bg-emerald-500 hover:text-white transition px-2 py-3 rounded-xl font-black text-[12px] flex items-center justify-center"
                      >
                         ➕ CHỌN BÀI TẬP TỪ KHO
                      </button>
                      <button 
                          onClick={handleAddManualTask} 
                          className="w-full bg-white border border-slate-200 text-slate-500 hover:border-slate-400 hover:bg-slate-100 transition px-2 py-2 rounded-lg font-bold text-[12px] flex items-center justify-center shadow-sm"
                      >
                         📝 Thêm ghi chú văn bản
                      </button>
                   </div>
                   <div className="flex-1 overflow-y-auto p-4 space-y-3 custom-scrollbar bg-white">
                      {taskList.map((task, idx) => (
                         <div key={task.id} className="bg-slate-50 border border-slate-200 p-3 rounded-xl shadow-sm flex items-start justify-between group hover:border-[#0a5482] transition-colors">
                            <div className="flex-1 min-w-0 pr-2">
                               <div className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1.5">
                                 {task.type === 'exercise' ? '🔗 BÀI TẬP ĐÍNH KÈM' : '📝 NHIỆM VỤ ĐỌC'}
                               </div>
                               <div className="font-bold text-[#0a5482] text-[13px] leading-snug break-words">
                                   {task.text}
                               </div>
                            </div>
                            
                            <div className="flex flex-col items-center gap-1 shrink-0">
                               <div className="flex items-center gap-1">
                                   <button onClick={() => handleMoveTaskUp(idx)} disabled={idx === 0} className="w-6 h-6 flex items-center justify-center bg-white border border-slate-200 hover:bg-slate-100 rounded text-[10px] disabled:opacity-30 transition-colors" title="Chuyển lên">▲</button>
                                   <button onClick={() => handleMoveTaskDown(idx)} disabled={idx === taskList.length - 1} className="w-6 h-6 flex items-center justify-center bg-white border border-slate-200 hover:bg-slate-100 rounded text-[10px] disabled:opacity-30 transition-colors" title="Chuyển xuống">▼</button>
                               </div>
                               <div className="flex items-center gap-1 mt-1">
                                   <button onClick={() => handleEditTask(task)} className="w-6 h-6 flex items-center justify-center bg-blue-50 text-blue-600 hover:bg-blue-100 rounded text-[12px] transition-colors" title="Sửa tên nhiệm vụ">✏️</button>
                                   <button onClick={() => setTaskList(taskList.filter(t => t.id !== task.id))} className="w-6 h-6 flex items-center justify-center bg-red-50 text-red-500 hover:bg-red-100 rounded text-[12px] transition-colors" title="Xóa">✖</button>
                               </div>
                            </div>
                         </div>
                      ))}
                      {taskList.length === 0 && (
                          <div className="text-center text-xs text-slate-400 italic mt-8 border-2 border-dashed border-slate-200 p-6 rounded-2xl mx-2">
                              Chưa có nhiệm vụ nào được giao.<br/>Học sinh sẽ chỉ cần đọc nội dung.
                          </div>
                      )}
                   </div>
                </>
             )}

             {/* TAB BÍ KÍP AI (LONG CONTEXT) - NÂNG CẤP HỖ TRỢ CTRL+V */}
             {rightTab === 'context' && (
                <div className="flex-1 flex flex-col bg-white">
                   <div className="p-4 border-b border-slate-100 bg-amber-50 shrink-0">
                       <div className="flex justify-between items-start mb-2">
                           <h4 className="font-black text-amber-800 text-[13px] uppercase tracking-tight flex items-center gap-2">
                               <span className="text-lg">🧠</span> CẤP BÍ KÍP CHO AI
                           </h4>
                           
                           {/* NÚT UPLOAD ẢNH ĐÁP ÁN (DÙNG KHI CHỌN FILE TỪ MÁY) */}
                           <input 
                               type="file" 
                               accept="image/*" 
                               className="hidden" 
                               ref={answerImgInputRef} 
                               onChange={handleUploadAnswerImage} 
                           />
                           <button 
                               onClick={() => answerImgInputRef.current?.click()}
                               disabled={isUploadingAnswerImg}
                               className="bg-amber-500 hover:bg-amber-600 text-white font-bold text-[10px] px-3 py-1.5 rounded-lg shadow-sm transition-colors flex items-center gap-1 disabled:opacity-50"
                           >
                               {isUploadingAnswerImg ? '⏳ ĐANG TẢI...' : '📸 CHỌN ẢNH'}
                           </button>
                       </div>
                       <p className="text-[11px] text-amber-700/80 leading-relaxed font-medium">
                           Nhập Text, hoặc <strong>Paste (Ctrl+V)</strong> ảnh đáp án trực tiếp vào ô bên dưới. AI sẽ dùng thông tin này để giải đáp cho học sinh.
                       </p>
                   </div>
                   <div className="flex-1 p-3 relative">
                       {isUploadingAnswerImg && (
                           <div className="absolute inset-0 z-10 bg-white/80 flex flex-col items-center justify-center rounded-xl">
                               <div className="w-8 h-8 border-4 border-amber-200 border-t-amber-500 rounded-full animate-spin"></div>
                               <span className="mt-2 text-xs font-bold text-amber-600">Đang lưu ảnh lên Cloud...</span>
                           </div>
                       )}
                       <textarea 
                           value={tutorContext}
                           onChange={e => setTutorContext(e.target.value)}
                           onPaste={handlePasteImage} // BẮT SỰ KIỆN PASTE
                           placeholder="Dán nội dung, hoặc ấn Ctrl+V để dán trực tiếp ảnh đáp án vào đây..."
                           className="w-full h-full resize-none border border-slate-200 bg-slate-50 rounded-xl p-4 text-[13px] text-slate-700 outline-none focus:border-amber-400 focus:bg-white transition-colors custom-scrollbar font-mono"
                       ></textarea>
                   </div>
                   {tutorContext && (
                       <div className="px-4 py-2 border-t border-slate-100 bg-slate-50 flex justify-end shrink-0">
                           <button 
                               onClick={() => setTutorContext('')} 
                               className="text-[11px] text-red-500 font-bold hover:underline transition"
                           >
                               Xóa trắng bí kíp
                           </button>
                       </div>
                   )}
                </div>
             )}

          </div>
        </div>
      </div>

      {showExerciseModal && (
        <ExerciseSelectionModal 
            availableExercises={availableExercises} 
            onClose={() => setShowExerciseModal(false)} 
            onAddExercise={handleAddExerciseTask} 
        />
      )}

    </div>
  );
}