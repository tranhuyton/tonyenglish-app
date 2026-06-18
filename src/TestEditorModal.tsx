import React, { useState, useRef, useMemo, useEffect } from 'react';
import { supabase } from './supabase';
import * as XLSX from 'xlsx';
import JoditEditor from 'jodit-react';

// ==========================================
// 1. CÁC HÀM VÀ COMPONENT CON
// ==========================================

const uploadToSupabase = async (file: File) => {
  const fileExt = file.name ? file.name.split('.').pop() : 'png';
  const fileName = `media_${Date.now()}_${Math.random().toString(36).substring(7)}.${fileExt}`;
  
  const { error } = await supabase.storage.from('test_assets').upload(`uploads/${fileName}`, file, { cacheControl: '3600', upsert: false });
  if (error) throw error;
  
  return supabase.storage.from('test_assets').getPublicUrl(`uploads/${fileName}`).data.publicUrl;
};

// COMPONENT EDITOR DÀNH CHO CÁC Ô NHẬP NỘI DUNG
const JoditEditorRow = ({ label, value, onChange, placeholder = "" }: any) => {
  const editorRef = useRef(null);

  const editorConfig = useMemo(() => ({
    readonly: false,
    height: 250, 
    allowResizeY: true, 
    statusbar: false, 
    toolbarSticky: false, 
    placeholder: placeholder || "Nhập nội dung vào đây...",
    
    // FIX PHÍM TAB: Ép thực hiện lệnh thụt lề (indent) thay vì chuyển focus sang ô khác
    tabAction: 'indent',
    tabIndex: -1,

    buttons: [
      'source', 'fullsize', '|', 
      'bold', 'italic', 'underline', 'strikethrough', '|',
      'superscript', 'subscript', '|',
      'ul', 'ol', 'outdent', 'indent', '|',
      'font', 'fontsize', 'brush', '|',
      'image', 'table', 'link', '|',
      'align', 'valign', 'undo', 'redo', '|',
      'eraser'
    ],
    extraButtons: ['source', 'fullsize'],
    
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
      beforeInsertNode: (node: any) => {
        if (node && node.tagName === 'IMG') {
          node.style.width = '80%';
          node.style.display = 'block';
          node.style.marginLeft = 'auto';
          node.style.marginRight = 'auto';
        }
      }
    }
  }), [placeholder]);

  return (
    <div className="flex flex-col py-3 border-b border-slate-100 last:border-0 gap-2">
      <div className="flex justify-between items-center">
        <label className="text-[13px] font-bold text-slate-600">{label}</label>
      </div>
      <div className="bg-white rounded-lg border border-slate-200 shadow-sm relative z-0">
         <style>{`
            .jodit-toolbar__box { flex-wrap: wrap !important; }
            .jodit-workplace { min-height: 150px !important; }
            
            /* --- CĂN CHỈNH LẠI BULLET POINT CHUẨN BRUTALIST IDP/BC --- */
            .jodit-wysiwyg ul {
                padding-left: 1.5rem !important;
                margin: 0.5rem 0 !important;
            }
            .jodit-wysiwyg ol {
                list-style: decimal outside !important;
                padding-left: 1.5rem !important;
                margin: 0.5rem 0 !important;
            }
            
            /* Ép thẳng vào thẻ LI để trị dứt điểm inline-style của Jodit */
            .jodit-wysiwyg ul > li {
                list-style-type: disc !important; /* Level 1: Chấm đen */
                margin-bottom: 0.25rem !important;
            }
            .jodit-wysiwyg ul ul > li {
                list-style-type: circle !important; /* Level 2: Vòng tròn trắng */
            }
            .jodit-wysiwyg ul ul ul > li {
                list-style-type: square !important; /* Level 3: Hình vuông đen */
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
            value={value || ''}
            config={editorConfig}
            onBlur={(newContent) => onChange({ target: { value: newContent } })}
         />
      </div>
    </div>
  );
};

// --- COMPONENT MEDIA ROW ---
const MediaRow = ({ label, value, onUpload, id, accept = "audio/*, image/*", uploadingId, setUploadingId }: any) => {
  const [isDrag, setIsDrag] = useState(false);
  const [showLink, setShowLink] = useState(false);
  const [linkVal, setLinkVal] = useState('');
  const [isDeleting, setIsDeleting] = useState(false);

  const handleFile = async (file: File) => {
    setUploadingId(id);
    try {
      const url = await uploadToSupabase(file);
      onUpload(url);
    } catch (err) { 
      alert("Lỗi tải file!"); 
    } finally { 
      setUploadingId(null); 
    }
  };

  const handleSaveLink = () => {
    if (linkVal.trim()) {
      onUpload(linkVal.trim());
    }
    setShowLink(false);
    setLinkVal('');
  };

  const handleRemoveFile = async () => {
    if (!window.confirm("Anh có chắc muốn xóa file đính kèm này không?")) return;
    
    setIsDeleting(true);
    try {
      if (value && value.includes('supabase.co/storage/v1/object/public/test_assets/')) {
        const urlParts = value.split('/test_assets/');
        if (urlParts.length === 2) {
          const filePath = urlParts[1];
          await supabase.storage.from('test_assets').remove([filePath]);
        }
      }
      onUpload('');
    } catch (error) {
      console.error("Lỗi khi xóa file:", error);
      alert("Có lỗi khi xóa file trên server, nhưng hệ thống đã gỡ link khỏi đề thi.");
      onUpload('');
    } finally {
      setIsDeleting(false);
    }
  };

  return (
    <div className="flex flex-col py-3 border-b border-slate-100 last:border-0 gap-2">
      <label className="text-[13px] font-bold text-slate-600">{label}</label>
      <div 
        className={`w-full border-2 border-dashed rounded-lg p-4 flex flex-col md:flex-row items-start md:items-center justify-between gap-4 transition ${isDrag ? 'border-[#00a651] bg-[#e6f4ea]' : 'border-slate-300 bg-slate-50'}`}
        onDragOver={(e) => { 
          e.preventDefault(); 
          setIsDrag(true); 
        }}
        onDragLeave={(e) => { 
          e.preventDefault(); 
          setIsDrag(false); 
        }}
        onDrop={(e) => { 
          e.preventDefault(); 
          setIsDrag(false); 
          if(e.dataTransfer.files?.[0]) {
            handleFile(e.dataTransfer.files[0]); 
          }
        }}
      >
        <div className="flex items-center gap-3 w-full md:w-auto">
          <span className="text-2xl shrink-0">{value ? '✅' : '🎵'}</span>
          <div className="text-[13px] text-slate-500 w-full min-w-0">
            {uploadingId === id ? (
               <span className="text-amber-500 font-bold">⏳ Đang tải lên...</span> 
            ) : isDeleting ? (
               <span className="text-red-500 font-bold">🗑️ Đang xóa file...</span> 
            ) : value ? (
                <div className="flex flex-col sm:flex-row sm:items-center gap-2 w-full min-w-0">
                   <span className="text-emerald-600 font-bold truncate block w-full sm:max-w-[200px] md:max-w-[250px] lg:max-w-[350px]" title={value}>
                      {value.startsWith('http') ? value : 'Đã có file đính kèm'}
                   </span>
                   <button 
                      onClick={handleRemoveFile} 
                      className="bg-red-50 hover:bg-red-500 text-red-500 hover:text-white border border-red-200 hover:border-red-500 px-2.5 py-1 rounded text-[11px] font-bold transition flex items-center justify-center gap-1 shrink-0 w-fit mt-2 sm:mt-0"
                   >
                      ✖ Xóa
                   </button>
                </div>
             ) : (
                <span>Kéo thả file Âm thanh vào đây</span>
             )}
          </div>
        </div>
        
        <div className="flex items-center gap-2 w-full md:w-auto mt-2 md:mt-0">
           {showLink && !value ? (
              <div className="flex items-center gap-1 bg-white border border-slate-300 rounded-lg p-1 shadow-sm w-full md:w-[280px]">
                <input
                  type="text"
                  autoFocus
                  placeholder="Dán link audio (R2, host ngoài)..."
                  value={linkVal}
                  onChange={e => setLinkVal(e.target.value)}
                  className="flex-1 text-[12px] font-medium text-slate-700 outline-none px-2 py-1 bg-transparent min-w-0"
                />
                <button 
                  onClick={handleSaveLink} 
                  className="bg-[#00a651] hover:bg-[#008f45] text-white px-3 py-1.5 rounded text-[11px] font-bold transition shrink-0"
                >
                  OK
                </button>
                <button 
                  onClick={() => setShowLink(false)} 
                  className="bg-slate-200 hover:bg-slate-300 text-slate-600 px-2 py-1.5 rounded text-[11px] font-bold transition shrink-0"
                >
                  ✖
                </button>
              </div>
           ) : !value ? (
              <>
                 <button 
                    onClick={() => setShowLink(true)} 
                    className="bg-white border border-slate-300 text-slate-700 px-3 py-2 rounded-lg text-[12px] font-bold cursor-pointer hover:bg-slate-100 transition shadow-sm flex items-center justify-center gap-1.5 shrink-0 flex-1 md:flex-none"
                    title="Dùng link audio từ host ngoài (Cloudflare R2, AWS...)"
                 >
                    <span className="text-blue-500 text-sm leading-none">🔗</span> Thêm Link
                 </button>
                 <label className="bg-white border border-slate-300 text-slate-700 px-4 py-2 rounded-lg text-[12px] font-bold cursor-pointer hover:bg-slate-100 transition shadow-sm shrink-0 flex-1 md:flex-none text-center">
                   <input 
                      type="file" 
                      className="hidden" 
                      accept={accept} 
                      onChange={(e) => { 
                        if(e.target.files?.[0]) {
                          handleFile(e.target.files[0]); 
                        }
                      }} 
                    /> 
                   Tải lên
                 </label>
              </>
           ) : null}
        </div>
      </div>
    </div>
  );
};

// ==========================================
// 2. COMPONENT CHÍNH TEST EDITOR
// ==========================================
export default function TestEditorModal({ testData: testRecord, courses, folders, onClose, onSave }: any) {
  const isImportMode = testRecord.mode === 'import'; 
  const [activeTab, setActiveTab] = useState(isImportMode ? 'content' : 'basic'); 
  
  const [isDraggingExcel, setIsDraggingExcel] = useState(false);
  const [uploadingId, setUploadingId] = useState<string | null>(null);

  const getInitialData = () => {
    if (testRecord.content_json) {
      const data = {...testRecord.content_json};
      // Always use the actual course_id from the test record (not the stale one in content_json)
      if (data.basicInfo) {
        data.basicInfo = { ...data.basicInfo, courseId: testRecord.course_id || 'all' };
      }
      return data;
    }
    
    return {
      basicInfo: {
        title: testRecord.title || (isImportMode ? 'Đề thi Import từ Excel/CSV' : ''),
        courseId: testRecord.course_id || 'all', 
        folderId: testRecord.folder_id || '', 
        skill: testRecord.test_type || 'SplitScreen (Standard)',
        category: testRecord.content_json?.basicInfo?.category || 'exercise', 
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
  // THUẬT TOÁN ĐỌC EXCEL 
  // ==========================================
  const processExcelFile = async (file: File) => {
    setUploadingId('excel');
    const reader = new FileReader();
    
    reader.onload = (e) => {
      try {
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

        let isReplace = true;
        if (testData.parts && testData.parts.length > 0) {
           isReplace = window.confirm("CẢNH BÁO: Đề này đang có sẵn câu hỏi.\n\nAnh muốn XÓA SẠCH câu hỏi cũ để thay bằng file mới (Bấm OK)?\nHay muốn NỐI THÊM câu hỏi vào dưới cùng (Bấm Cancel)?");
        }

        let newParts: any[] = [];
        let currentPart: any = null;
        let currentSection: any = null;
        let importCount = 0;

        const getCol = (row: any, exactKeywords: string[], partialKeywords: string[] = []) => {
          const keys = Object.keys(row);
          for (let key of keys) {
            const cleanKey = key.toLowerCase().replace(/[\s_.,|()[\]-]/g, '');
            if (exactKeywords.includes(cleanKey)) return row[key];
          }
          for (let key of keys) {
            const cleanKey = key.toLowerCase().replace(/[\s_.,|()[\]-]/g, '');
            if (partialKeywords.some(k => cleanKey.includes(k))) return row[key];
          }
          return "";
        };

        const cleanText = (val: any) => {
          if (val === undefined || val === null) return "";
          let str = String(val).trim();
          str = str.replace(/[\u200B-\u200D\uFEFF\u2028\u2029]/g, '');
          str = str.replace(/<\/?p[^>]*>/gi, '<br><br>'); 
          str = str.replace(/<(?!\/?(br|img|audio)(?=>|\s.*>))\/?.*?>/gi, '');
          str = str.replace(/\n/g, '<br>');
          str = str.replace(/(<br\s*\/?>\s*){3,}/gi, '<br><br>'); 
          str = str.replace(/^(<br\s*\/?>\s*)+|(<br\s*\/?>\s*)+$/gi, ''); 
          return str.trim();
        };

        jsonData.forEach((row: any) => {
          if (Object.values(row).some(val => String(val).includes('---'))) return;

          const rawPartTitle = getCol(row, ['parttitle'], ['part']);
          const partTitle = rawPartTitle !== undefined && rawPartTitle !== null ? String(rawPartTitle).trim() : '';
          
          const rawPartContent = getCol(row, ['partcontent'], ['bàiđọc', 'content']);
          const partContent = cleanText(rawPartContent);
          
          const rawSecTitle = getCol(row, ['sectiontitle'], ['section', 'nhóm']);
          const secTitle = rawSecTitle !== undefined && rawSecTitle !== null ? String(rawSecTitle).trim() : '';
          
          const rawSecContent = getCol(row, ['sectioncontent'], ['hướngdẫn', 'instruction']);
          const secContent = cleanText(rawSecContent);
          
          const qTypeRaw = String(getCol(row, ['questiontype'], ['dạng', 'loạicâu'])).trim();
          let qType = 'Trắc nghiệm';
          const upperQType = qTypeRaw.toUpperCase();
          
          if (upperQType.includes('TFNG') || upperQType.includes('TRUE')) {
             qType = 'TFNG';
          } else if (upperQType.includes('CHECKBOX') || upperQType.includes('COMBO') || upperQType.includes('NHIỀU ĐÁP ÁN')) {
             qType = 'Checkbox';
          } else if (upperQType.includes('KÉO THẢ') || upperQType.includes('MATCHING') || upperQType.includes('DRAG')) {
             qType = 'Kéo thả';
          } else if (upperQType.includes('DROPLIST') || upperQType.includes('NỐI')) {
             qType = 'Droplist';
          } else if (upperQType.includes('ĐIỀN TỪ') || upperQType.includes('FILL')) {
             qType = 'Điền từ';
          } else if (qTypeRaw) {
             qType = qTypeRaw;
          } else if (!qTypeRaw && currentSection && (!secTitle || currentSection.title === secTitle)) {
             qType = currentSection.questionType;
          }

          const qIdRaw = getCol(row, ['id', 'questionid'], ['câu']);
          if (String(qIdRaw).toLowerCase().trim() === 'id' || String(qIdRaw).toLowerCase().trim() === 'question id') return;
          
          const qId = qIdRaw ? String(qIdRaw).trim() : '';
          let qContent = cleanText(getCol(row, ['questiontext', 'questioncontent'], ['nộidung']));
          
          let optA = cleanText(getCol(row, ['optiona', 'a'], ['đápána', 'lựachọna']));
          let optB = cleanText(getCol(row, ['optionb', 'b'], ['đápánb', 'lựachọnb']));
          let optC = cleanText(getCol(row, ['optionc', 'c'], ['đápánc', 'lựachọnc']));
          let optD = cleanText(getCol(row, ['optiond', 'd'], ['đápánd', 'lựachọnd']));
          let optE = cleanText(getCol(row, ['optione', 'e'], ['đápáne', 'lựachọne']));
          let optF = cleanText(getCol(row, ['optionf', 'f'], ['đápánf', 'lựachọnf']));
          let optG = cleanText(getCol(row, ['optiong', 'g'], ['đápáng', 'lựachọng']));
          let optH = cleanText(getCol(row, ['optionh', 'h'], ['đápánh', 'lựachọnh']));
          let optI = cleanText(getCol(row, ['optioni', 'i'], ['đápáni', 'lựachọni']));
          let optJ = cleanText(getCol(row, ['optionj', 'j'], ['đápánj', 'lựachọnj']));
          let optK = cleanText(getCol(row, ['optionk', 'k'], ['đápánk', 'lựachọnk']));
          let optL = cleanText(getCol(row, ['optionl', 'l'], ['đápánl', 'lựachọnl']));
          
          const answer = cleanText(getCol(row, ['answer', 'correctanswer', 'đápánđúng', 'đápánchínhxác'], []));
          const exp = cleanText(getCol(row, ['explanation'], ['giảithích']));

          if ((qType === 'Checkbox' || qType === 'Trắc nghiệm') && qContent.includes('A.')) {
              const lines = qContent.split(/<br\s*\/?>/i);
              const newLines: string[] = [];
              const extracted: string[] = [];
              
              lines.forEach((line: string) => {
                  const match = line.trim().match(/^([A-L])[\.\):]\s*(.+)$/i);
                  if (match) {
                    extracted.push(match[2].trim());
                  } else {
                    newLines.push(line);
                  }
              });
              
              if (extracted.length >= 2) {
                  qContent = newLines.join('<br>').trim();
                  optA = extracted[0] || ''; optB = extracted[1] || '';
                  optC = extracted[2] || ''; optD = extracted[3] || '';
                  optE = extracted[4] || ''; optF = extracted[5] || '';
                  optG = extracted[6] || ''; optH = extracted[7] || '';
                  optI = extracted[8] || ''; optJ = extracted[9] || '';
                  optK = extracted[10] || ''; optL = extracted[11] || '';
              }
          }

          const isRealQuestion = (qId !== "" && !isNaN(parseInt(qId))) || (answer !== "");
          if (!partTitle && !secTitle && !partContent && !secContent && !isRealQuestion) return;

          if (partTitle && (!currentPart || currentPart.title !== partTitle)) {
            currentPart = { 
              id: Date.now().toString() + Math.random(), 
              title: partTitle, 
              content: partContent || '', 
              tags: '', 
              audioUrl: '', 
              explanation: '', 
              sections: [] 
            };
            newParts.push(currentPart);
            currentSection = null; 
          } else if (partContent && currentPart && !currentPart.content) {
            currentPart.content = partContent;
          }

          const options = [];
          if (optA) options.push(optA); if (optB) options.push(optB);
          if (optC) options.push(optC); if (optD) options.push(optD);
          if (optE) options.push(optE); if (optF) options.push(optF);
          if (optG) options.push(optG); if (optH) options.push(optH);
          if (optI) options.push(optI); if (optJ) options.push(optJ);
          if (optK) options.push(optK); if (optL) options.push(optL);

          let isNewSection = false;
          if (secTitle && (!currentSection || currentSection.title !== secTitle)) {
              isNewSection = true;
          }

          if (qType === 'Checkbox' && currentSection && currentSection.questionType === 'Checkbox') {
              const isFollowUp = (!qContent && options.length === 0);
              if (isFollowUp) {
                  isNewSection = false; 
              }
          }

          if (isNewSection || !currentSection) {
            currentSection = { 
              id: Date.now().toString() + Math.random(), 
              title: secTitle || (currentSection ? currentSection.title : `Section ${qId}`), 
              content: secContent || '', 
              tags: '', 
              questionType: qType, 
              audioUrl: '', 
              explanation: '', 
              questions: [] 
            };
            if (currentPart) currentPart.sections.push(currentSection);
          } else if (secContent && currentSection && !currentSection.content) {
            currentSection.content = secContent;
          }

          if (isRealQuestion && currentSection) {
            let finalOptions = options;
            
            if (options.length === 0) {
               if (qType === 'TFNG') {
                 finalOptions = ['TRUE', 'FALSE', 'NOT GIVEN'];
               } else if (qType === 'Trắc nghiệm') {
                 finalOptions = ['A', 'B', 'C', 'D'];
               } else if (qType === 'Droplist') {
                 if (currentSection.questions.length > 0) {
                    finalOptions = [...currentSection.questions[0].options];
                 } else {
                    finalOptions = []; 
                 }
               } else {
                 finalOptions = []; 
               }
            }

            if (qType === 'Checkbox' && answer.includes(',')) {
                const ansArr = answer.split(',').map(x => x.trim()).filter(Boolean);
                let baseIdMatch = qId.match(/\d+/);
                let baseId = baseIdMatch ? parseInt(baseIdMatch[0]) : null;
                
                ansArr.forEach((ans, idx) => {
                    let cid = qId;
                    if (baseId !== null) cid = String(baseId + idx);
                    else if (idx > 0) cid = qId + `_${idx}`;

                    currentSection.questions.push({
                       id: cid,
                       content: idx === 0 ? qContent : '', 
                       tags: '', 
                       audioUrl: '', 
                       explanation: idx === 0 ? exp : '', 
                       options: idx === 0 ? finalOptions : [], 
                       correctAnswer: ans 
                    });
                    importCount++;
                });
            } else {
                currentSection.questions.push({
                   id: qId ? qId : (Date.now().toString() + Math.random()),
                   content: qContent, 
                   tags: '', 
                   audioUrl: '', 
                   explanation: exp, 
                   options: finalOptions, 
                   correctAnswer: answer
                });
                importCount++;
            }
          }
        });

        if (newParts.length > 0) {
          setTestData((prev: any) => ({ ...prev, parts: isReplace ? newParts : [...prev.parts, ...newParts] }));
          alert(`🎉 Bóc tách thành công chính xác ${importCount} câu hỏi! Tự động cấu hình chuẩn Kéo Thả và Droplist.`);
        } else {
          alert("⚠️ Không tìm thấy câu hỏi nào hợp lệ. Anh kiểm tra lại tên các cột trong file.");
        }
      } catch (err) {
        console.error("Error parsing Excel:", err);
        alert("❌ Lỗi hệ thống khi đọc file. Hãy chắc chắn file không bị lỗi định dạng.");
      } finally {
        setUploadingId(null);
      }
    };
    reader.readAsArrayBuffer(file);
  };

  const handleDragOverExcel = (e: React.DragEvent) => { 
    e.preventDefault(); 
    setIsDraggingExcel(true); 
  };
  
  const handleDragLeaveExcel = (e: React.DragEvent) => { 
    e.preventDefault(); 
    setIsDraggingExcel(false); 
  };
  
  const handleExcelDrop = (e: React.DragEvent) => {
    e.preventDefault(); 
    setIsDraggingExcel(false);
    if (e.dataTransfer.files?.[0]) {
      processExcelFile(e.dataTransfer.files[0]);
    }
  };
  
  const handleExcelUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files?.[0]) { 
      processExcelFile(e.target.files[0]); 
      e.target.value = ''; 
    }
  };

  // ==========================================
  // QUẢN LÝ MẢNG
  // ==========================================
  const addPart = () => {
    const newData = { ...testData }; 
    if (!newData.parts) newData.parts = [];
    newData.parts.push({ 
      id: Date.now().toString(), 
      title: `Part ${newData.parts.length + 1}`, 
      content: '', 
      tags: '', 
      audioUrl: '', 
      explanation: '', 
      sections: [] 
    });
    setTestData(newData);
  };
  
  const removePart = (pIdx: number) => { 
    const newData = { ...testData }; 
    newData.parts.splice(pIdx, 1); 
    setTestData(newData); 
  };

  const addSection = (pIdx: number) => {
    const newData = { ...testData }; 
    if (!newData.parts[pIdx].sections) newData.parts[pIdx].sections = [];
    newData.parts[pIdx].sections.push({ 
      id: Date.now().toString(), 
      title: `Section ${newData.parts[pIdx].sections.length + 1}`, 
      content: '', 
      tags: '', 
      questionType: 'Trắc nghiệm', 
      audioUrl: '', 
      explanation: '', 
      questions: [] 
    });
    setTestData(newData);
  };
  
  const removeSection = (pIdx: number, sIdx: number) => { 
    const newData = { ...testData }; 
    newData.parts[pIdx].sections.splice(sIdx, 1); 
    setTestData(newData); 
  };

  // --- HÀM THÊM CÂU HỎI THÔNG MINH (SMART GUESSER) ---
  const addQuestion = (pIdx: number, sIdx: number) => {
    const newData = { ...testData }; 
    const section = newData.parts[pIdx].sections[sIdx];
    if (!section.questions) {
      section.questions = [];
    }
    
    let nextIdStr = '';
    
    if (section.questions.length > 0) {
       const lastId = parseInt(section.questions[section.questions.length - 1].id);
       if (!isNaN(lastId)) nextIdStr = String(lastId + 1);
    } else if (sIdx > 0 && newData.parts[pIdx].sections[sIdx - 1].questions?.length > 0) {
       const prevSecQs = newData.parts[pIdx].sections[sIdx - 1].questions;
       const lastId = parseInt(prevSecQs[prevSecQs.length - 1].id);
       if (!isNaN(lastId)) nextIdStr = String(lastId + 1);
    } else if (pIdx > 0) {
       const prevPart = newData.parts[pIdx - 1];
       if (prevPart.sections && prevPart.sections.length > 0) {
          const prevSecQs = prevPart.sections[prevPart.sections.length - 1].questions;
          if (prevSecQs && prevSecQs.length > 0) {
             const lastId = parseInt(prevSecQs[prevSecQs.length - 1].id);
             if (!isNaN(lastId)) nextIdStr = String(lastId + 1);
          }
       }
    }
    
    if (!nextIdStr) nextIdStr = Date.now().toString();

    const qType = section.questionType;
    let initialOptions = ['A', 'B', 'C', 'D'];
    
    if (["Điền từ", "Kéo thả", "Kéo thả vào Part", "Matching"].includes(qType)) {
      initialOptions = [];
    } else if (qType === 'Droplist') {
      if (section.questions.length > 0) {
        initialOptions = [...section.questions[0].options];
      } else {
        initialOptions = [];
      }
    }
    
    section.questions.push({ 
      id: nextIdStr, 
      content: '', 
      tags: '', 
      audioUrl: '', 
      explanation: '', 
      options: initialOptions, 
      correctAnswer: '' 
    });
    setTestData(newData);
  };
  
  const removeQuestion = (pIdx: number, sIdx: number, qIdx: number) => { 
    const newData = { ...testData }; 
    newData.parts[pIdx].sections[sIdx].questions.splice(qIdx, 1); 
    setTestData(newData); 
  };

  const addOption = (pIdx: number, sIdx: number, qIdx: number) => {
    const newData = { ...testData }; 
    if (!newData.parts[pIdx].sections[sIdx].questions[qIdx].options) {
        newData.parts[pIdx].sections[sIdx].questions[qIdx].options = [];
    }
    newData.parts[pIdx].sections[sIdx].questions[qIdx].options.push(''); 
    setTestData(newData);
  };
  
  const removeOption = (pIdx: number, sIdx: number, qIdx: number, oIdx: number) => {
    const newData = { ...testData }; 
    newData.parts[pIdx].sections[sIdx].questions[qIdx].options.splice(oIdx, 1); 
    setTestData(newData); 
  };

  const updateField = (path: number[], field: string, value: any) => {
    const newData = { ...testData };
    if (path.length === 1) {
      newData.parts[path[0]][field] = value;
    } else if (path.length === 2) {
      newData.parts[path[0]].sections[path[1]][field] = value;
    } else if (path.length === 3) {
      newData.parts[path[0]].sections[path[1]].questions[path[2]][field] = value;
    }
    setTestData(newData);
  };
  
  const updateOption = (pIdx: number, sIdx: number, qIdx: number, oIdx: number, value: string) => {
    const newData = { ...testData }; 
    newData.parts[pIdx].sections[sIdx].questions[qIdx].options[oIdx] = value; 
    setTestData(newData);
  };

  const handleSave = async () => { 
    const title = testData.basicInfo.title?.trim();
    if (!title) {
       alert("Anh vui lòng nhập Tên đề/Bài tập nhé!");
       return;
    }

    setIsSaving(true); 
    
    try {
       let query = supabase.from('tests').select('id').eq('title', title);
       
       if (testRecord.id && testRecord.mode !== 'import') {
           query = query.neq('id', testRecord.id);
       }

       const { data, error } = await query;

       if (!error && data && data.length > 0) {
           alert(`⚠️ Tên đề "${title}" đã tồn tại trên hệ thống!\nAnh vui lòng đổi sang tên khác để tránh trùng lặp dữ liệu nhé.`);
           setIsSaving(false);
           return;
       }
    } catch (err) {
       console.error("Lỗi kiểm tra trùng tên:", err);
    }

    onSave(testData); 
  };

  return (
    <div className="fixed inset-0 bg-[#f0f2f5] z-[60] flex flex-col animate-in fade-in">
      <div className="bg-white px-6 py-3 flex justify-between items-center shrink-0 border-b border-slate-200 shadow-sm relative z-20">
        <div className="flex items-center gap-3">
          <button onClick={onClose} className="text-slate-500 hover:text-slate-800 font-bold text-xl transition">←</button>
          <h2 className="font-black text-[15px] text-slate-800 uppercase tracking-tight">
            {isImportMode ? 'Import Đề Thi Bằng Excel/CSV' : 'Soạn Thảo Đề Thi'}
          </h2>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto relative custom-scrollbar">
        <div className="max-w-[1200px] mx-auto w-full p-4 md:p-8 space-y-8 pb-20"> 
          
          <div className="flex flex-col md:flex-row gap-4 mb-6">
            <button 
              onClick={() => setActiveTab('basic')} 
              className={`w-full md:w-1/2 py-3 rounded-t-xl font-black text-sm uppercase tracking-widest transition-all border-b-4 ${activeTab === 'basic' ? 'bg-white border-[#00a651] text-[#00a651] shadow-sm' : 'bg-slate-200/50 border-transparent text-slate-400 hover:bg-slate-200'}`}
            >
              Thông tin chính
            </button>
            <button 
              onClick={() => setActiveTab('content')} 
              className={`w-full md:w-1/2 py-3 rounded-t-xl font-black text-sm uppercase tracking-widest transition-all border-b-4 ${activeTab === 'content' ? 'bg-white border-[#00a651] text-[#00a651] shadow-sm' : 'bg-slate-200/50 border-transparent text-slate-400 hover:bg-slate-200'}`}
            >
              Cài đặt & Nội dung đề
            </button>
          </div>

          {activeTab === 'basic' && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-start animate-in slide-in-from-left-4">
              <div className="bg-white rounded-xl overflow-hidden border border-slate-200 shadow-sm p-6 space-y-5">
                <h3 className="font-black text-[#00a651] border-b border-slate-100 pb-2 mb-4 uppercase text-[13px]">Thông tin chính</h3>
                <div>
                  <label className="text-[12px] font-bold text-slate-600 block mb-1">Tên đề/Bài tập <span className="text-red-500">*</span></label>
                  <input 
                    value={testData.basicInfo.title} 
                    onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, title: e.target.value}})} 
                    placeholder="Ví dụ: Unit 1: Reading Practice" 
                    className="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none focus:border-[#00a651] text-[14px] transition" 
                  />
                </div>
              </div>

              <div className="bg-white rounded-xl overflow-hidden border border-slate-200 shadow-sm p-6 space-y-5">
                <h3 className="font-black text-[#00a651] border-b border-slate-100 pb-2 mb-4 uppercase text-[13px]">Cài đặt hệ thống</h3>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="text-[12px] font-bold text-slate-600 block mb-1">Thuộc Khóa học</label>
                    <select 
                      value={testData.basicInfo.courseId} 
                      onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, courseId: e.target.value}})} 
                      className="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] transition focus:border-[#00a651]"
                    >
                      <option value="all">Dùng chung</option>
                      {courses?.map((c: any) => <option key={c.id} value={c.id}>{c.title}</option>)}
                    </select>
                  </div>
                  <div>
                    <label className="text-[12px] font-bold text-slate-600 block mb-1">Phân loại (Mục đích)</label>
                    <select 
                      value={testData.basicInfo.category || 'exercise'} 
                      onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, category: e.target.value}})} 
                      className="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] transition focus:border-[#1e88e5]"
                    >
                      <option value="test">Đề thi (Test)</option>
                      <option value="exercise">Bài tập (Exercise)</option>
                      <option value="game">Mini Game (Trò chơi)</option>
                    </select>
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-4 mt-2">
                  <div>
                    <label className="text-[12px] font-bold text-slate-600 block mb-1">Kỹ năng / Dạng đề</label>
                    <select 
                      value={testData.basicInfo.skill} 
                      onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, skill: e.target.value}})} 
                      className="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] transition focus:border-[#00a651]"
                    >
                      <option value="SplitScreen (Standard)">SplitScreen (Standard)</option>
                      <option value="MCQ (Standard)">MCQ (Standard)</option>
                      <option value="IELTS-Listening">Listening (IELTS)</option>
                      <option value="IELTS-Reading">Reading (IELTS)</option>
                      <option value="Mixed-Paper">Mixed Paper (Có hình)</option>
                      <option value="IELTS-Writing">Writing (IELTS)</option>
                      <option value="IELTS-Speaking">Speaking (IELTS)</option>
                    </select>
                  </div>
                  <div>
                    <label className="text-[12px] font-bold text-slate-600 block mb-1">Thời gian làm (phút)</label>
                    <input 
                      type="number" 
                      value={testData.basicInfo.timeLimit} 
                      onChange={e => setTestData({...testData, basicInfo: {...testData.basicInfo, timeLimit: e.target.value}})} 
                      className="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg outline-none text-[14px] transition focus:border-[#00a651]" 
                    />
                  </div>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'content' && (
            <div className="animate-in slide-in-from-right-4 space-y-6">
              
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

              {testData.parts?.map((part: any, pIdx: number) => (
                <div key={part.id} className="border-2 border-[#00a651] rounded-2xl bg-white overflow-hidden shadow-sm">
                    <div className="bg-[#e6f4ea] px-6 py-4 border-b border-[#00a651]/20 flex justify-between items-center group">
                      <input 
                        value={part.title} 
                        onChange={(e) => updateField([pIdx], 'title', e.target.value)} 
                        className="font-black text-[#00a651] text-xl bg-transparent outline-none border-b border-dashed border-[#00a651]/50 focus:border-[#00a651] w-64" 
                        placeholder="Part Title..." 
                      />
                      <button 
                        onClick={() => removePart(pIdx)} 
                        className="text-red-500 font-bold px-3 py-1 bg-red-50 rounded-lg opacity-0 group-hover:opacity-100 transition hover:bg-red-500 hover:text-white"
                      >
                        Xóa Part ✖
                      </button>
                    </div>
                    
                    <div className="p-6 md:p-8 space-y-4 bg-slate-50 border-b border-slate-200">
                      <JoditEditorRow 
                        label="Nội dung Part (Bài đọc/Giới thiệu)" 
                        value={part.content} 
                        onChange={(e:any) => updateField([pIdx], 'content', e.target.value)} 
                      />
                      <MediaRow 
                        label="File Âm thanh Part" 
                        value={part.audioUrl} 
                        id={`part-${part.id}`} 
                        uploadingId={uploadingId} 
                        setUploadingId={setUploadingId} 
                        onUpload={(url: string) => updateField([pIdx], 'audioUrl', url)} 
                      />
                    </div>

                    <div className="p-6 md:p-8 space-y-8">
                      {part.sections?.map((sec: any, sIdx: number) => (
                        <div key={sec.id} className="border-2 border-[#3b82f6] rounded-xl bg-white overflow-hidden shadow-sm">
                          <div className="bg-[#3b82f6] px-6 py-3 flex justify-between items-center group">
                            <input 
                              value={sec.title} 
                              onChange={(e) => updateField([pIdx, sIdx], 'title', e.target.value)} 
                              className="font-black text-white text-base bg-transparent outline-none border-b border-dashed border-white/50 focus:border-white w-64 placeholder:text-white/60" 
                              placeholder="Section Title..." 
                            />
                            <button 
                              onClick={() => removeSection(pIdx, sIdx)} 
                              className="text-white hover:text-red-200 font-bold opacity-0 group-hover:opacity-100 transition"
                            >
                              ✖
                            </button>
                          </div>
                          
                          <div className="p-6 bg-blue-50/30 border-b border-blue-100 space-y-4">
                            <JoditEditorRow 
                              label="Nội dung Section (Đoạn văn/Hướng dẫn)" 
                              value={sec.content} 
                              onChange={(e:any) => updateField([pIdx, sIdx], 'content', e.target.value)} 
                            />
                            <div className="flex flex-col md:flex-row items-start md:items-center py-3 border-b border-slate-100 gap-2">
                              <label className="w-32 shrink-0 text-[13px] font-bold text-slate-600">Kiểu làm</label>
                              <select 
                                value={sec.questionType} 
                                onChange={(e) => updateField([pIdx, sIdx], 'questionType', e.target.value)} 
                                className="flex-1 w-full bg-white border border-slate-200 rounded-lg p-2.5 text-[14px] text-slate-700 outline-none focus:border-[#3b82f6] transition"
                              >
                                <option value="Kéo thả vào Part">Kéo thả vào Part</option>
                                <option value="Trắc nghiệm">Trắc nghiệm (4 đáp án dài)</option>
                                <option value="TFNG">True / False / Not Given (TFNG)</option>
                                <option value="Checkbox">Checkbox (Nhiều đáp án/ Combo)</option>
                                <option value="Droplist">Droplist (Sổ chọn)</option>
                                <option value="Kéo thả">Kéo thả (Matching / Kéo hộp từ)</option>
                                <option value="Điền từ">Điền từ (Gõ tay)</option>
                              </select>
                            </div>
                            <MediaRow 
                              label="File Âm thanh Section" 
                              value={sec.audioUrl} 
                              id={`sec-${sec.id}`} 
                              uploadingId={uploadingId} 
                              setUploadingId={setUploadingId} 
                              onUpload={(url: string) => updateField([pIdx, sIdx], 'audioUrl', url)} 
                            />
                            {testData.basicInfo?.skill === 'Mixed-Paper' && (
                              <MediaRow 
                                label="Hình ảnh Section (Tùy chọn)" 
                                value={sec.imageUrl} 
                                accept="image/*"
                                id={`sec-img-${sec.id}`} 
                                uploadingId={uploadingId} 
                                setUploadingId={setUploadingId} 
                                onUpload={(url: string) => updateField([pIdx, sIdx], 'imageUrl', url)} 
                              />
                            )}
                          </div>

                          <div className="p-6 space-y-6">
                            {sec.questions?.map((q: any, qIdx: number) => {
                              const rawText = String(q.content || '').replace(/<[^>]*>/g, '').trim();
                              const hasContent = rawText !== '' || String(q.content || '').includes('<img') || String(q.content || '').includes('<audio');
                              const isComboChild = sec.questionType === "Checkbox" && qIdx > 0 && !hasContent;

                              return (
                                <div key={`q-${pIdx}-${sIdx}-${qIdx}`} className={`border rounded-xl bg-white shadow-sm transition group relative ${isComboChild ? 'border-amber-300 bg-amber-50/20 ml-8 border-l-[6px]' : 'border-slate-200 hover:border-amber-300'}`}>
                                  <button 
                                    onClick={() => removeQuestion(pIdx, sIdx, qIdx)} 
                                    className="absolute -top-3 -right-3 bg-red-500 text-white w-7 h-7 rounded-full opacity-0 group-hover:opacity-100 transition shadow-lg z-10"
                                  >
                                    ✖
                                  </button>
                                  
                                  <div className="p-5">
                                      <div className="flex gap-4 items-start">
                                        <div className="flex flex-col items-center gap-1 shrink-0">
                                          <input 
                                            value={(q.id && String(q.id).length <= 5) ? q.id : ''}
                                            onChange={(e) => updateField([pIdx, sIdx, qIdx], 'id', e.target.value)}
                                            className="w-11 h-11 bg-amber-100 text-amber-700 text-[15px] font-black rounded-full flex items-center justify-center border-2 border-amber-300 text-center outline-none focus:bg-white focus:border-amber-500 focus:ring-2 focus:ring-amber-200 transition-all placeholder:text-amber-300 m-0 p-0"
                                            placeholder={String(qIdx + 1)}
                                            title="Sửa số thứ tự câu hỏi (ID)"
                                          />
                                          <span className="text-[10px] font-bold text-slate-400">Câu số</span>
                                        </div>
                                        <div className="flex-1 space-y-4 min-w-0">
                                          
                                          {isComboChild && (
                                              <div className="bg-amber-50 text-amber-800 p-3 rounded-lg text-[13px] font-bold border border-amber-200 flex items-start gap-3">
                                                  <span className="text-xl leading-none">🔗</span>
                                                  <p className="m-0 leading-relaxed">
                                                    Câu này đang được hệ thống <b>tự động gộp vào cụm Combo Checkbox phía trên</b> do rỗng Nội dung câu hỏi gốc.<br/>
                                                    Anh chỉ cần thiết lập Đáp án đúng cho nó. Nếu muốn tách nó thành nhóm mới, hãy điền nội dung vào ô bên dưới.
                                                  </p>
                                              </div>
                                          )}

                                          <div className="flex flex-col md:flex-row gap-4">
                                            <div className="flex-1">
                                              <JoditEditorRow 
                                                label={isComboChild ? "Nội dung câu hỏi (Nhập nội dung nếu muốn tách thành Combo mới)" : "Nội dung câu hỏi"}
                                                value={q.content} 
                                                onChange={(e:any) => updateField([pIdx, sIdx, qIdx], 'content', e.target.value)} 
                                              />
                                            </div>
                                            <div className="shrink-0 w-full md:w-32">
                                              <label className="text-[12px] font-bold text-slate-600 block mb-1">Đáp án đúng</label>
                                              <input 
                                                value={q.correctAnswer || ''} 
                                                onChange={(e) => updateField([pIdx, sIdx, qIdx], 'correctAnswer', e.target.value)} 
                                                className="w-full bg-emerald-50 border border-emerald-200 text-emerald-700 font-black text-center rounded-lg p-3 outline-none focus:ring-2 focus:ring-emerald-400" 
                                                placeholder="VD: A hoặc A,C" 
                                              />
                                            </div>
                                          </div>
                                          
                                          {testData.basicInfo?.skill === 'Mixed-Paper' && (
                                            <div className="mb-2">
                                              <MediaRow 
                                                label="Hình ảnh Câu hỏi (Tùy chọn)" 
                                                value={q.imageUrl} 
                                                accept="image/*"
                                                id={`q-img-${q.id}`} 
                                                uploadingId={uploadingId} 
                                                setUploadingId={setUploadingId} 
                                                onUpload={(url: string) => updateField([pIdx, sIdx, qIdx], 'imageUrl', url)} 
                                              />
                                            </div>
                                          )}

                                          <div className={`bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-3 ${isComboChild && (!q.options || q.options.length === 0) ? 'hidden' : ''}`}>
                                            <div className="flex justify-between items-center border-b border-slate-200 pb-2">
                                                <label className="text-[12px] font-bold text-slate-600">Các lựa chọn đáp án (Options)</label>
                                                <span className="text-[11px] text-slate-400 font-medium italic">
                                                   Dùng cho Trắc nghiệm, Droplist, Kéo thả...
                                                </span>
                                            </div>
                                            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                                              {q.options?.map((opt: string, oIdx: number) => (
                                                <div key={oIdx} className="flex items-center gap-2">
                                                  <div className="w-8 h-8 rounded-full bg-white border border-slate-300 text-slate-600 font-black text-[12px] flex items-center justify-center shrink-0 shadow-sm">
                                                    {String.fromCharCode(65+oIdx)}
                                                  </div>
                                                  <input 
                                                    value={opt || ''} 
                                                    onChange={(e) => updateOption(pIdx, sIdx, qIdx, oIdx, e.target.value)} 
                                                    placeholder="Nhập nội dung lựa chọn..." 
                                                    className="flex-1 bg-white border border-slate-200 rounded-lg p-2 text-[14px] outline-none focus:border-[#0a5482] transition min-w-0" 
                                                  />
                                                  <button 
                                                    onClick={() => removeOption(pIdx, sIdx, qIdx, oIdx)} 
                                                    className="text-slate-300 hover:text-red-500 font-bold px-1.5 py-1 text-lg shrink-0"
                                                    title="Xóa lựa chọn này"
                                                  >
                                                    ×
                                                  </button>
                                                </div>
                                              ))}
                                            </div>
                                            <button 
                                              onClick={() => addOption(pIdx, sIdx, qIdx)} 
                                              className="w-full mt-2 py-2 border-2 border-dashed border-slate-300 text-[#0a5482] rounded-lg text-[12px] font-bold hover:bg-slate-100 hover:border-[#0a5482] transition"
                                            >
                                              + Thêm lựa chọn (Option {String.fromCharCode(65 + (q.options?.length || 0))})
                                            </button>
                                          </div>

                                          <div className="w-full">
                                            <JoditEditorRow 
                                              label="Lời giải thích (Tùy chọn)" 
                                              value={q.explanation} 
                                              onChange={(e:any) => updateField([pIdx, sIdx, qIdx], 'explanation', e.target.value)} 
                                              placeholder="Giải thích vì sao đúng..." 
                                            />
                                          </div>
                                        </div>
                                      </div>
                                  </div>
                                </div>
                              );
                            })}
                            
                            <button 
                              onClick={() => addQuestion(pIdx, sIdx)} 
                              className="w-full border-2 border-dashed border-slate-300 text-slate-500 hover:border-[#00a651] hover:text-[#00a651] hover:bg-[#e6f4ea] py-4 rounded-xl font-bold transition flex justify-center items-center gap-2"
                            >
                              <span className="text-xl">+</span> Thêm Câu Hỏi Mới
                            </button>
                            
                          </div>
                        </div>
                      ))}
                      
                      <button 
                        onClick={() => addSection(pIdx)} 
                        className="bg-[#3b82f6] hover:bg-[#2563eb] text-white px-6 py-2.5 rounded-full text-[13px] font-bold shadow-md"
                      >
                        + Thêm Section Mới
                      </button>
                      
                    </div>
                </div>
              ))}
              
              {(!isImportMode || testData.parts?.length > 0) && (
                <div className="flex justify-center pt-8 border-t-2 border-dashed border-slate-200 pb-10">
                    <button 
                      onClick={addPart} 
                      className="bg-[#00a651] hover:bg-[#008f45] text-white px-10 py-4 rounded-full text-[15px] font-black shadow-lg hover:scale-105 transition-transform"
                    >
                      + THÊM PART MỚI
                    </button>
                </div>
              )}
            </div>
          )}
        </div>
      </div>

      <button 
        onClick={handleSave} 
        disabled={isSaving} 
        className="fixed bottom-10 right-10 w-20 h-20 bg-[#2bd6eb] hover:bg-[#1bc1d6] text-white rounded-full shadow-[0_10px_25px_rgba(43,214,235,0.4)] flex flex-col items-center justify-center z-[100] transition-all hover:scale-110 active:scale-95 disabled:opacity-50 disabled:hover:scale-100"
      >
        <span className="text-[26px] mb-0.5">{isSaving ? '⏳' : '💾'}</span>
        <span className="text-[10px] font-black uppercase tracking-wider">{isSaving ? 'Đang lưu' : 'Lưu Đề'}</span>
      </button>
    </div>
  );
}