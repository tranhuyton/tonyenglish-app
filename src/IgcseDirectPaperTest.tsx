import React, { useState, useRef, useEffect } from 'react';
import { supabase } from './supabase';
import { Document, Page, pdfjs } from 'react-pdf';
import 'react-pdf/dist/Page/AnnotationLayer.css';
import 'react-pdf/dist/Page/TextLayer.css';
import { useLmsLang, LmsLangToggle } from './utils/lmsI18n';
import { ImageLightboxModal, LightboxState, extractLightboxFromClick } from './mcqImageUtils';
import 'katex/dist/katex.min.css';
import { renderIgcseLatex, detectCalculatorPolicy, detectIgcseMathSyllabus } from './katexUtils';
import IgcseFormulaSheetModal from './IgcseFormulaSheetModal';

pdfjs.GlobalWorkerOptions.workerSrc = `https://unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;

const escapeHtml = (str: string): string =>
  String(str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');

// LaTeX converters
const latexToText = (text: string): string => {
  if (!text) return '';
  const hasLatex = text.includes('\\') || /[\^_]\{/.test(text) || /[\^_]\(/.test(text);
  if (!hasLatex) return text;
  let r = text;
  const m: [RegExp, string][] = [
    [/\\alpha/g,'α'],[/\\beta/g,'β'],[/\\gamma/g,'γ'],[/\\delta/g,'δ'],[/\\theta/g,'θ'],
    [/\\lambda/g,'λ'],[/\\mu/g,'μ'],[/\\pi/g,'π'],[/\\sigma/g,'σ'],[/\\omega/g,'ω'],
    [/\\Omega/g,'Ω'],[/\\Delta/g,'Δ'],[/\\Sigma/g,'Σ'],[/\\Gamma/g,'Γ'],[/\\phi/g,'φ'],
    [/\\rho/g,'ρ'],[/\\tau/g,'τ'],[/\\epsilon/g,'ε'],[/\\varepsilon/g,'ε'],
    [/\\int/g,'∫'],[/\\sum/g,'Σ'],[/\\prod/g,'∏'],[/\\partial/g,'∂'],
    [/\\sqrt\{([^}]+)\}/g,'√($1)'],[/\\sqrt/g,'√'],
    [/\\frac\{([^}]+)\}\{([^}]+)\}/g,'($1)/($2)'],
    [/\\pm/g,'±'],[/\\mp/g,'∓'],[/\\times/g,'×'],[/\\div/g,'÷'],[/\\cdot/g,'·'],[/\\infty/g,'∞'],
    [/\\neq/g,'≠'],[/\\leq/g,'≤'],[/\\geq/g,'≥'],[/\\approx/g,'≈'],[/\\equiv/g,'≡'],
    [/\\sim/g,'∼'],[/\\propto/g,'∝'],
    [/\\angle/g,'∠'],[/\\triangle/g,'△'],[/\\perp/g,'⊥'],[/\\parallel/g,'∥'],
    [/\\cap/g,'∩'],[/\\cup/g,'∪'],[/\\in/g,'∈'],[/\\notin/g,'∉'],
    [/\\subset/g,'⊂'],[/\\subseteq/g,'⊆'],[/\\supset/g,'⊃'],[/\\emptyset/g,'∅'],
    [/\\rightarrow/g,'→'],[/\\leftarrow/g,'←'],[/\\Rightarrow/g,'⇒'],[/\\Leftrightarrow/g,'⇔'],
    [/\\vec\{([^}]+)\}/g,'$1⃗'],
    [/\\sin/g,'sin'],[/\\cos/g,'cos'],[/\\tan/g,'tan'],[/\\sec/g,'sec'],[/\\cot/g,'cot'],[/\\csc/g,'csc'],
    [/\\log/g,'log'],[/\\ln/g,'ln'],[/\\lim/g,'lim'],
    [/\^\{([^}]+)\}/g,'^($1)'],[/_\{([^}]+)\}/g,'_($1)'],
    [/\^\(([^)]+)\)/g,'^($1)'],[/_\(([^)]+)\)/g,'_($1)'],
    [/\^([0-9a-zA-Zα-ωΑ-Ω])/g,'^$1'],[/_([0-9a-zA-Zα-ωΑ-Ω])/g,'_$1'],
    [/\\,/g,' '],[/\\;/g,' '],[/\\!/g,''],
  ];
  for (const [p, s] of m) r = r.replace(p, s);
  r = r.replace(/\\([a-zA-Z]+)/g, '$1');
  return r;
};

const renderLatex = (text: string): string => renderIgcseLatex(text);

const DrawingPage = ({ pageNum, drawMode, penColor, scale, onStrokeDrawn, isEn }: any) => {
    const canvasRef = useRef<HTMLCanvasElement>(null);
    const isDrawingRef = useRef(false);
    const shapeStartRef = useRef<{x:number,y:number}|null>(null);
    const canvasSnapshot = useRef<ImageData|null>(null);
    const onStrokeDrawnRef = useRef(onStrokeDrawn);
    onStrokeDrawnRef.current = onStrokeDrawn;
    const [drawText, setDrawText] = useState('');
    const [textPos, setTextPos] = useState<{x:number,y:number}|null>(null);

    const resizeCanvas = () => {
        const cv = canvasRef.current;
        if (!cv) return;
        // canvas là sibling của .react-pdf__Page, nên phải tìm trong parentElement
        const pageEl = cv.parentElement?.querySelector('.react-pdf__Page');
        if (pageEl) {
            const rect = pageEl.getBoundingClientRect();
            // Nhân với devicePixelRatio để nét vẽ mịn màng trên iPad/Retina
            const dpr = window.devicePixelRatio || 1;
            const targetWidth = rect.width * dpr;
            const targetHeight = rect.height * dpr;
            
            if (cv.width !== targetWidth || cv.height !== targetHeight) {
                const ctx = cv.getContext('2d');
                let backup: ImageData | null = null;
                if (ctx && cv.width > 0 && cv.height > 0) {
                    backup = ctx.getImageData(0, 0, cv.width, cv.height);
                }
                cv.width = targetWidth;
                cv.height = targetHeight;
                if (ctx && backup) {
                    // Phục hồi lại hình vẽ cũ bằng cách scale lại cho khớp với kích thước mới
                    const tempCanvas = document.createElement('canvas');
                    tempCanvas.width = backup.width;
                    tempCanvas.height = backup.height;
                    tempCanvas.getContext('2d')?.putImageData(backup, 0, 0);
                    ctx.drawImage(tempCanvas, 0, 0, tempCanvas.width, tempCanvas.height, 0, 0, targetWidth, targetHeight);
                }
            }
        }
    };

    useEffect(() => {
        const observer = new ResizeObserver(resizeCanvas);
        const cv = canvasRef.current;
        if (cv && cv.parentElement) {
            observer.observe(cv.parentElement);
        }
        return () => observer.disconnect();
    }, []);

    useEffect(() => {
        // trigger resize on scale change
        const timer = window.setTimeout(resizeCanvas, 200);
        return () => window.clearTimeout(timer);
    }, [scale]);

    useEffect(() => {
        const cv = canvasRef.current;
        if (!cv) return;

        const handlePointerDown = (e: PointerEvent) => {
            if (!drawMode) return;
            // Dùng preventDefault để ngăn Safari cuộn trang khi dùng Apple Pencil
            e.preventDefault();
            
            const ctx = cv.getContext('2d'); if (!ctx) return;
            const rect = cv.getBoundingClientRect();
            const scaleX = cv.width / rect.width;
            const scaleY = cv.height / rect.height;
            const x = (e.clientX - rect.left) * scaleX;
            const y = (e.clientY - rect.top) * scaleY;
            
            if (drawMode === 'text') {
                // Lưu tọa độ thật trên CSS để ô input hiển thị đúng vị trí click
                setTextPos({x: e.clientX - rect.left, y: e.clientY - rect.top}); 
                setDrawText('');
                return;
            }
            isDrawingRef.current = true;
            if (['line','rect','circle','triangle'].includes(drawMode)) {
                shapeStartRef.current = {x, y};
                canvasSnapshot.current = ctx.getImageData(0, 0, cv.width, cv.height);
            } else {
                ctx.beginPath(); ctx.moveTo(x, y);
            }
        };

        const handlePointerMove = (e: PointerEvent) => {
            if (!drawMode) return;
            // Ngăn cuộn trang
            e.preventDefault();
            
            if (!isDrawingRef.current) return;
            const ctx = cv.getContext('2d'); if (!ctx) return;
            const rect = cv.getBoundingClientRect();
            const scaleX = cv.width / rect.width;
            const scaleY = cv.height / rect.height;
            const x = (e.clientX - rect.left) * scaleX;
            const y = (e.clientY - rect.top) * scaleY;
            
            const dpr = window.devicePixelRatio || 1;
            const start = shapeStartRef.current;
            if (['line','rect','circle','triangle'].includes(drawMode) && start && canvasSnapshot.current) {
                ctx.putImageData(canvasSnapshot.current, 0, 0);
                ctx.strokeStyle = penColor; ctx.lineWidth = 2 * scale * dpr; ctx.lineCap = 'round';
                ctx.globalCompositeOperation = 'source-over';
                ctx.beginPath();
                if (drawMode === 'line') { ctx.moveTo(start.x, start.y); ctx.lineTo(x, y); }
                else if (drawMode === 'rect') { ctx.rect(start.x, start.y, x - start.x, y - start.y); }
                else if (drawMode === 'circle') { const rx = Math.abs(x-start.x)/2, ry = Math.abs(y-start.y)/2; ctx.ellipse(start.x+(x-start.x)/2, start.y+(y-start.y)/2, rx, ry, 0, 0, Math.PI*2); }
                else if (drawMode === 'triangle') { ctx.moveTo(start.x+(x-start.x)/2, start.y); ctx.lineTo(x, y); ctx.lineTo(start.x, y); ctx.closePath(); }
                ctx.stroke();
                onStrokeDrawnRef.current?.();
            } else if (drawMode === 'pen' || drawMode === 'eraser') {
                ctx.strokeStyle = drawMode === 'eraser' ? 'rgba(0,0,0,1)' : penColor;
                ctx.lineWidth = drawMode === 'eraser' ? 20 * scale * dpr : 2 * scale * dpr;
                ctx.lineCap = 'round';
                ctx.globalCompositeOperation = drawMode === 'eraser' ? 'destination-out' : 'source-over';
                ctx.lineTo(x, y); ctx.stroke();
                onStrokeDrawnRef.current?.();
            }
        };

        const handlePointerUp = (e: PointerEvent) => {
            if (!drawMode) return;
            e.preventDefault();
            isDrawingRef.current = false; shapeStartRef.current = null; canvasSnapshot.current = null;
        };

        const handleContextMenu = (e: Event) => {
            if (drawMode) e.preventDefault();
        };

        const handleTouch = (e: TouchEvent) => {
            if (drawMode) {
                // Tắt triệt để mọi thao tác cuộn, zoom của iPad bằng touch
                if (e.cancelable) e.preventDefault();
            }
        };

        // Gắn sự kiện native (thay cho React Synthetic Events) để kiểm soát Safari tốt hơn
        cv.addEventListener('pointerdown', handlePointerDown, { passive: false });
        cv.addEventListener('pointermove', handlePointerMove, { passive: false });
        cv.addEventListener('pointerup', handlePointerUp, { passive: false });
        cv.addEventListener('pointercancel', handlePointerUp, { passive: false });
        cv.addEventListener('pointerleave', handlePointerUp, { passive: false });
        cv.addEventListener('contextmenu', handleContextMenu, { passive: false });
        
        // Bắt buộc phải chặn touchstart và touchmove trên Safari thì nó mới không ngắt quãng nét vẽ (chống dropped strokes)
        cv.addEventListener('touchstart', handleTouch, { passive: false });
        cv.addEventListener('touchmove', handleTouch, { passive: false });

        return () => {
            cv.removeEventListener('pointerdown', handlePointerDown);
            cv.removeEventListener('pointermove', handlePointerMove);
            cv.removeEventListener('pointerup', handlePointerUp);
            cv.removeEventListener('pointercancel', handlePointerUp);
            cv.removeEventListener('pointerleave', handlePointerUp);
            cv.removeEventListener('contextmenu', handleContextMenu);
            cv.removeEventListener('touchstart', handleTouch);
            cv.removeEventListener('touchmove', handleTouch);
        };
    }, [drawMode, penColor, scale]);

    return (
        <div 
            className="relative mb-6 shadow-xl w-fit mx-auto bg-white page-container select-none" 
            data-page={pageNum}
            style={{ WebkitUserSelect: 'none', WebkitTouchCallout: 'none' } as React.CSSProperties}
        >
            <Page 
                pageNumber={pageNum} 
                renderTextLayer={false} 
                renderAnnotationLayer={false} 
                scale={scale}
                className="pointer-events-none" 
            />
            <canvas
                ref={canvasRef}
                className={`absolute top-0 left-0 w-full h-full student-canvas ${drawMode ? (drawMode === 'eraser' ? 'cursor-cell pointer-events-auto' : drawMode === 'text' ? 'cursor-text pointer-events-auto' : 'cursor-crosshair pointer-events-auto') : 'pointer-events-none'}`}
                style={{ zIndex: 10, touchAction: 'none', WebkitUserSelect: 'none', WebkitTouchCallout: 'none' } as React.CSSProperties}
            />
            {drawMode === 'text' && textPos && (
                <input
                    autoFocus
                    value={drawText}
                    onChange={e => setDrawText(e.target.value)}
                    onKeyDown={e => {
                        if (e.key === 'Enter' && drawText) {
                            const ctx = canvasRef.current?.getContext('2d');
                            if (ctx) { 
                                const dpr = window.devicePixelRatio || 1;
                                ctx.globalCompositeOperation = 'source-over'; 
                                ctx.font = `bold ${16 * scale * dpr}px sans-serif`; 
                                ctx.fillStyle = penColor; 
                                // Phải nhân tọa độ CSS với DPR để vẽ đúng vị trí thật trên canvas
                                ctx.fillText(drawText, textPos.x * dpr, (textPos.y + 16 * scale) * dpr); 
                                onStrokeDrawnRef.current?.();
                            }
                            setTextPos(null); setDrawText('');
                        } else if (e.key === 'Escape') { setTextPos(null); setDrawText(''); }
                    }}
                    className="absolute bg-white/90 border-2 border-[#1e88e5] rounded px-2 py-1 text-[14px] outline-none min-w-[120px] shadow-lg"
                    style={{ left: textPos.x, top: textPos.y, zIndex: 20, WebkitUserSelect: 'text', WebkitTouchCallout: 'default' } as React.CSSProperties}
                    placeholder={isEn ? 'Type text and press Enter...' : 'Gõ text rồi Enter...'}
                />
            )}
        </div>
    );
};


export default function IgcseDirectPaperTest({ onBack, onStartTest, testData: propTestData }: { onBack?: () => void, onStartTest?: any, testData?: any }) {
  const [lang, setLang] = useLmsLang();
  const isEn = lang === 'en';
  const isEnRef = useRef(isEn);
  isEnRef.current = isEn;
  const [showFormulaSheet, setShowFormulaSheet] = useState(false);
  const [testData, setTestData] = useState<any>(() => {
      let raw = propTestData;
      if (!raw) {
          const saved = sessionStorage.getItem('lms_current_test');
          raw = saved ? JSON.parse(saved) : null;
      }
      if (!raw) return null;
      if (!raw.json_config?.questions && raw.content_json?.questions) {
          raw.json_config = { ...(raw.json_config || {}), questions: raw.content_json.questions, timeLimit: raw.content_json?.basicInfo?.timeLimit || raw.json_config?.timeLimit || 120 };
      }
      return raw;
  });
  
  const [isLoading, setIsLoading] = useState(!testData);
  const [imageLightbox, setImageLightbox] = useState<LightboxState | null>(null);
  const initIsReview = !!testData?.isReview;
  const [isReviewMode, setIsReviewMode] = useState(initIsReview);
  useEffect(() => { window.dispatchEvent(new CustomEvent('tony-review-mode-change', { detail: Boolean(isReviewMode) })); return () => { window.dispatchEvent(new CustomEvent('tony-review-mode-change', { detail: false })); }; }, [isReviewMode]);

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [gradeResult, setGradeResult] = useState<any>(() => {
      if (initIsReview && testData?.aiFeedback) return testData.aiFeedback;
      return null;
  });

  const [drawMode, setDrawMode] = useState<'pen'|'eraser'|'line'|'rect'|'circle'|'triangle'|'text'|null>(null);
  const [penColor, setPenColor] = useState('#111827');
  const [isFullscreen, setIsFullscreen] = useState(() => typeof document !== 'undefined' ? !!document.fullscreenElement : false);

  useEffect(() => {
    const onFsChange = () => setIsFullscreen(!!document.fullscreenElement);
    document.addEventListener('fullscreenchange', onFsChange);
    return () => document.removeEventListener('fullscreenchange', onFsChange);
  }, []);

  const handleSafeExit = () => {
    if (!isReviewMode && !gradeResult) {
      if (!window.confirm(isEn ? 'You are currently taking an IGCSE test. Are you sure you want to exit?' : 'Bạn đang làm bài thi IGCSE. Bạn có chắc muốn thoát ra ngoài không?')) return;
    }
    if (onBack) onBack();
  };
  const [numPages, setNumPages] = useState<number | null>(null);
  const [pdfError, setPdfError] = useState<string | null>(null);
  const [pdfReloadKey, setPdfReloadKey] = useState(0);
  const [zoomLevel, setZoomLevel] = useState<number>(1.2);
  
  const [timeLeft, setTimeLeft] = useState(7200); 
  const isFinishingRef = useRef(false);
  const hasUnsavedDrawingsRef = useRef(false);

  const [isRightPanelOpen, setIsRightPanelOpen] = useState(initIsReview);

  useEffect(() => {
    const handleBeforeUnload = (e: BeforeUnloadEvent) => {
      if (!isReviewMode && !gradeResult && hasUnsavedDrawingsRef.current) {
        e.preventDefault();
        e.returnValue = '';
      }
    };
    window.addEventListener('beforeunload', handleBeforeUnload);
    return () => window.removeEventListener('beforeunload', handleBeforeUnload);
  }, [isReviewMode, gradeResult]);

  const getSavedEndTime = (testId: string) => {
    if (!testId) return null;
    const saved = localStorage.getItem(`igcse_endtime_${testId}`);
    return saved ? parseInt(saved, 10) : null;
  };

  useEffect(() => {
    if (testData && !isReviewMode) {
       const isExercise = testData.content_json?.basicInfo?.category === 'exercise';
       if (isExercise) {
           setTimeLeft(999999);
           setIsLoading(false);
           return;
       }
       const rawTime = testData.json_config?.timeLimit || testData.timeLimit || testData.time_limit || 120;
       const initialSeconds = parseInt(rawTime) * 60;
       let currentEndTime = getSavedEndTime(testData.id);
       if (!currentEndTime) {
           currentEndTime = Date.now() + initialSeconds * 1000;
           localStorage.setItem(`igcse_endtime_${testData.id}`, currentEndTime.toString());
           setTimeLeft(initialSeconds);
       } else {
           const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
           setTimeLeft(remaining);
       }
       setIsLoading(false);
    } else if (isReviewMode) {
       setIsLoading(false);
    }
  }, [testData, isReviewMode]);

  const formatTime = (totalSeconds: number) => {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    const pad = (num: number) => num.toString().padStart(2, '0');
    if (hours > 0) return `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
    return `${pad(minutes)}:${pad(seconds)}`;
  };

  const handleDocumentLoadSuccess = ({ numPages }: { numPages: number }) => {
      setPdfError(null);
      setNumPages(numPages);
  };

  const handleZoomIn = () => setZoomLevel(prev => Math.min(prev + 0.2, 3.0));
  const handleZoomOut = () => setZoomLevel(prev => Math.max(prev - 0.2, 0.6));

  const handleSubmit = async (forceAutoSubmit: any = false) => {
    const isForced = forceAutoSubmit === true;
    if (isFinishingRef.current || isSubmitting) return;
    const isExercise = testData?.content_json?.basicInfo?.category === 'exercise';
    if (!isForced) {
      if (!isExercise && timeLeft > 0 && !window.confirm(isEn ? "Are you sure you want to submit the exam? AI image grading takes about 10–20 seconds." : "Bạn có chắc chắn muốn nộp bài thi? AI sẽ phân tích hình ảnh mất khoảng 10-20 giây.")) { return; }
      if (isExercise && !window.confirm(isEn ? "Are you sure you want to submit your work?" : "Bạn có chắc chắn muốn nộp bài?")) { return; }
    }

    const rawTime = testData.json_config?.timeLimit || testData.timeLimit || testData.time_limit || 120;
    const initialSeconds = (parseInt(rawTime) || 120) * 60;
    const savedEnd = testData?.id ? getSavedEndTime(testData.id) : null;
    const computedTimeSpent = savedEnd
      ? Math.max(0, initialSeconds - Math.max(0, Math.floor((savedEnd - Date.now()) / 1000)))
      : Math.max(0, initialSeconds - timeLeft);

    setIsSubmitting(true);
    isFinishingRef.current = true;

    try {
      const imageAnswers: { questionId: string, base64: string }[] = [];
      const textAnswers = {
        ALL: isEn
          ? "The student completed the exam directly on the PDF paper. Please review the attached page images. IMPORTANT: Write all grading feedback (general_feedback and every examiner_comment) exclusively in English."
          : "Học sinh làm bài trực tiếp trên giấy (PDF). Vui lòng xem các file đính kèm."
      };

      const pageContainers = document.querySelectorAll('.page-container');
      
      for (let i = 0; i < pageContainers.length; i++) {
          const container = pageContainers[i];
          const pageNum = container.getAttribute('data-page');
          const pdfCanvas = container.querySelector('.react-pdf__Page__canvas') as HTMLCanvasElement;
          const studentCanvas = container.querySelector('.student-canvas') as HTMLCanvasElement;
          
          if (pdfCanvas) {
              const compositeCanvas = document.createElement('canvas');
              compositeCanvas.width = pdfCanvas.width;
              compositeCanvas.height = pdfCanvas.height;
              const ctx = compositeCanvas.getContext('2d');
              
              if (ctx) {
                  // Giới hạn kích thước ảnh để tránh lỗi quá tải Payload của Supabase
                  const MAX_WIDTH = 800;
                  let scaleFactor = 1;
                  if (pdfCanvas.width > MAX_WIDTH) {
                      scaleFactor = MAX_WIDTH / pdfCanvas.width;
                  }

                  const targetWidth = pdfCanvas.width * scaleFactor;
                  const targetHeight = pdfCanvas.height * scaleFactor;

                  compositeCanvas.width = targetWidth;
                  compositeCanvas.height = targetHeight;
                  
                  ctx.fillStyle = '#ffffff';
                  ctx.fillRect(0, 0, targetWidth, targetHeight);
                  
                  // Vẽ PDF với kích thước đã thu nhỏ
                  ctx.drawImage(pdfCanvas, 0, 0, targetWidth, targetHeight);
                  
                  // Vẽ nét vẽ của học sinh với kích thước đã thu nhỏ
                  if (studentCanvas && studentCanvas.width > 0) {
                      ctx.drawImage(studentCanvas, 0, 0, studentCanvas.width, studentCanvas.height, 0, 0, targetWidth, targetHeight);
                  }
                  
                  // Optimize size: JPEG 40% (Giảm tối đa dung lượng, Gemini Vision vẫn đọc được)
                  const base64 = compositeCanvas.toDataURL('image/jpeg', 0.4);
                  imageAnswers.push({ questionId: `PAGE_${pageNum}`, base64 });
              }
          }
      }

      const { data, error } = await supabase.functions.invoke('igcse-grader', {
        body: { 
            testConfig: testData.json_config?.questions || [],
            textAnswers: textAnswers,
            imageAnswers: imageAnswers,
            pdfUrl: testData.insert_pdf_url || testData.pdf_url || null,
            lang: isEn ? 'en' : 'vi',
            feedbackLanguage: isEn ? 'English' : 'Vietnamese'
        }
      });

      if (error) throw new Error((isEn ? "Server error: " : "Lỗi gọi Server: ") + error.message);
      if (data?.error) throw new Error((isEn ? "Grading error: " : "Lỗi chấm điểm: ") + data.error);
      
      let gradedData;
      try {
          // Edge function giờ trả về parsed object trực tiếp
          if (data.result && typeof data.result === 'object') {
              gradedData = data.result;
          } else {
              // Fallback: parse string (backward compatible)
              let cleanJson = (data.result || data.rawText || "").replace(/```json/gi, "").replace(/```/gi, "").trim();
              cleanJson = cleanJson.replace(/[\n\r\t]+/g, ' ');
              cleanJson = cleanJson.replace(/,\s*([\}\]])/g, '$1');
              const jsonMatch = cleanJson.match(/\{[\s\S]*\}/);
              if (jsonMatch) cleanJson = jsonMatch[0];
              gradedData = JSON.parse(cleanJson);
          }
      } catch (parseErr: any) {
          console.error("Lỗi parse JSON từ AI:", parseErr);
          console.log("Raw AI Output:", data.result || data.rawText);
          gradedData = {
              total_student_score: 0,
              total_max_score: 0,
              general_feedback: (isEn
                ? "⚠️ AI returned malformed data (invalid characters). Raw AI output below:\n\n"
                : "⚠️ AI trả về dữ liệu bị lỗi định dạng (chứa ký tự không hợp lệ). Dưới đây là nội dung thô AI trả về:\n\n") + JSON.stringify(data.result || data.rawText),
              details: []
          };
      }
      
      // BẮT BUỘC TÍNH LẠI ĐIỂM (LLM thường cộng dồn sai)
      if (gradedData && Array.isArray(gradedData.details)) {
          let trueStudentScore = 0;
          let trueMaxScore = 0;
          gradedData.details.forEach((d: any) => {
              trueStudentScore += (Number(d.student_score) || 0);
              trueMaxScore += (Number(d.max_score) || 0);
          });
          gradedData.total_student_score = trueStudentScore;
          gradedData.total_max_score = trueMaxScore;
      }

      setGradeResult(gradedData);
      setIsReviewMode(true);
      setIsRightPanelOpen(true);
      setDrawMode(null);
      hasUnsavedDrawingsRef.current = false;

      try {
        const { data: { user } } = await supabase.auth.getUser();
        if (user) {
          await supabase.from('test_results').insert([{
            user_id: user.id, course_id: testData.course_id, test_title: testData.title || "IGCSE Direct Paper",
            test_type: 'IGCSE-Science', score: gradedData.total_student_score, total_score: gradedData.total_max_score,
            time_spent: computedTimeSpent,
            details: { test_id: testData.id, userAnswers: {}, aiFeedback: gradedData }
          }]);

          // Auto-complete test-type assignments (Chỉ hoàn thành nếu đạt từ 50% điểm trở lên)
          const isPassed = gradedData.total_max_score > 0 
            ? (gradedData.total_student_score / gradedData.total_max_score) >= 0.5 
            : (gradedData.total_student_score >= 5.0);
          if (isPassed) {
            await supabase.from('assignments')
              .update({ is_completed: true, updated_at: new Date().toISOString() })
              .eq('test_id', testData.id)
              .eq('user_id', user.id)
              .eq('task_type', 'test');
          }
          window.dispatchEvent(new CustomEvent('tony-refresh-lecture-progress'));
        }
      } catch (dbError) { console.error("DB save error:", dbError); }

      if (testData?.id) {
         localStorage.removeItem(`igcse_endtime_${testData.id}`);
      }

    } catch (err: any) {
      isFinishingRef.current = false;
      if (err.message && err.message.includes("Unexpected end of JSON input")) {
          alert(isEn ? "❌ Could not submit due to an interrupted connection or oversized image files. Please try again." : "❌ Không thể nộp bài do kết nối gián đoạn hoặc file ảnh quá nặng. Vui lòng thử nộp lại.");
      } else {
          alert((isEn ? "❌ An error occurred while grading: " : "❌ Có lỗi trong lúc chấm: ") + err.message);
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleSubmitRef = useRef(handleSubmit);
  handleSubmitRef.current = handleSubmit;

  useEffect(() => {
    if (isLoading || !testData || gradeResult || isFinishingRef.current || isReviewMode) return;
    if (testData.content_json?.basicInfo?.category === 'exercise') return;
    const timer = setInterval(() => {
        const currentEndTime = getSavedEndTime(testData.id);
        if (currentEndTime) {
            const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
            setTimeLeft(remaining);
            if (remaining <= 0) { clearInterval(timer); alert(isEnRef.current ? "⏰ Time's up!" : "⏰ Hết giờ làm bài!"); handleSubmitRef.current(true); }
        } else {
            setTimeLeft(prev => {
                if (prev <= 1) {
                    clearInterval(timer);
                    alert(isEnRef.current ? "⏰ Time's up!" : "⏰ Hết giờ làm bài!");
                    handleSubmitRef.current(true);
                    return 0;
                }
                return prev - 1;
            });
        }
    }, 1000);
    return () => clearInterval(timer);
  }, [isLoading, testData, gradeResult, isReviewMode]);

  const callAiTutor = (questionText: string, studentAns: string, correctAnswer: string) => {
      const tutorContext = {
          overall: 'IGCSE Review',
          transcript: isEn
            ? `Question: "${questionText}". \nStudent's answer: ${studentAns}. \nCorrect Cambridge Mark Scheme answer: "${correctAnswer}".`
            : `Câu hỏi: "${questionText}". \nĐáp án của học sinh: ${studentAns}. \nĐáp án đúng Cambridge MS: "${correctAnswer}".`,
          feedback: isEn
            ? "You are a Cambridge IGCSE tutor. The student is reviewing their exam and does not understand this question. Speak and explain exclusively in English. Warmly greet the student, read the question, and explain step-by-step why the official answer is correct. Use a supportive, clear tone and read any formulas clearly."
            : "Bạn là gia sư Cambridge IGCSE. Học sinh đang xem lại bài thi và không hiểu câu này. Hãy chủ động chào, đọc câu hỏi và giải thích chi tiết tại sao đáp án đúng là như vậy, phân tích từng bước lập luận. Dùng giọng điệu ân cần, dễ hiểu, nếu có công thức hãy đọc rõ ràng."
      };
      sessionStorage.setItem('tony_live_mode', 'TUTOR');
      sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
      sessionStorage.setItem('tony_auto_start', 'true');
      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
  };

  if (isLoading) return (
    <div className="h-[100dvh] w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold">
      <div className="animate-spin text-4xl mb-4">⏳</div>
      <p>{isEn ? 'Loading IGCSE exam (Direct mode)...' : 'Đang tải đề thi IGCSE (Direct)...'}</p>
    </div>
  );

  if (!testData || (!isReviewMode && (!testData.json_config || !testData.json_config.questions))) return (
    <div className="h-[100dvh] w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold gap-4">
      <p>{isEn ? '⚠️ No exam configuration found in the system.' : '⚠️ Chưa có cấu hình đề thi trong hệ thống.'}</p>
      <button onClick={onBack} className="bg-[#1e88e5] px-6 py-2 rounded hover:bg-blue-700 transition-colors">{isEn ? 'Go Back' : 'Quay lại'}</button>
    </div>
  );

  const questions = testData.json_config.questions || [];
  const pdfUrl = testData.insert_pdf_url || testData.pdf_url;
  const calcPolicy = detectCalculatorPolicy(testData?.title, testData?.content_json?.basicInfo);
  const mathSyllabus = detectIgcseMathSyllabus(testData?.title, testData?.course_id || testData?.content_json?.basicInfo?.courseId);

  const handleContainerScroll = (e: React.UIEvent<HTMLDivElement>) => {
      const el = e.currentTarget;
      if (el.scrollTop <= 0) el.scrollTop = 1;
      else if (el.scrollTop + el.clientHeight >= el.scrollHeight) el.scrollTop -= 1;
  };

  return (
    <div 
      className="h-[100dvh] w-screen flex flex-col bg-[#e5e7eb] font-sans text-slate-900 overflow-hidden select-none"
      style={{ WebkitUserSelect: 'none', WebkitTouchCallout: 'none' } as React.CSSProperties}
    >
      {/* Header */}
      <header className="h-14 w-full bg-white border-b border-slate-300 flex items-center justify-between px-3 sm:px-6 shrink-0 z-20 box-border gap-2">
        <div className="flex items-center gap-2.5 sm:gap-4 overflow-hidden min-w-0">
          <button type="button" onClick={handleSafeExit} className="text-slate-600 hover:text-[#0a5482] font-bold text-sm transition-colors whitespace-nowrap cursor-pointer">← {isEn ? 'Back' : 'Quay lại'}</button>
          <div className="h-5 w-px bg-slate-300 hidden sm:block"></div>
          <div className="truncate flex items-center gap-2 min-w-0">
            <h1 className="font-bold text-slate-900 text-[14px] sm:text-[15px] leading-tight truncate">{isReviewMode ? `[REVIEW] ${testData.title}` : testData.title}</h1>
            {calcPolicy && (
              <span className={`hidden lg:inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-[11px] font-black uppercase tracking-wide shrink-0 border ${calcPolicy === 'non-calculator' ? 'bg-rose-50 text-rose-700 border-rose-200' : 'bg-emerald-50 text-emerald-700 border-emerald-200'}`}>
                {calcPolicy === 'non-calculator' ? '🚫 Non-Calculator' : '🧮 Calculator'}
              </span>
            )}
            <span className="hidden xl:inline-block text-xs text-[#0a5482] font-semibold px-2 py-0.5 bg-sky-50 border border-sky-200/70 rounded-md shrink-0">{isEn ? 'Direct Draw Mode' : 'Chế độ vẽ trực tiếp'}</span>
          </div>
        </div>
        <div className="flex items-center gap-2 sm:gap-3 shrink-0">
          {mathSyllabus && (
            <button
              type="button"
              onClick={() => setShowFormulaSheet(true)}
              className="px-2.5 py-1 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200 text-xs font-extrabold whitespace-nowrap cursor-pointer transition-colors"
              title={isEn ? 'Open Official 2025–2027 Formula Sheet' : 'Mở bảng công thức Cambridge 2025–2027'}
            >
              📐 <span className="hidden sm:inline">Formulas</span>
            </button>
          )}
          <LmsLangToggle lang={lang} setLang={setLang} variant="light" />
          {!gradeResult && !isReviewMode && (
            <>
               <div className={`font-bold flex items-center gap-1.5 px-2.5 sm:px-3 py-1 rounded-lg text-xs sm:text-sm ${testData.content_json?.basicInfo?.category === 'exercise' ? 'text-[#0a5482] bg-sky-50 border border-sky-200' : (timeLeft <= 300 ? 'text-rose-600 bg-rose-50 border border-rose-200 animate-pulse' : 'text-slate-700 bg-slate-100')}`}>
                 {testData.content_json?.basicInfo?.category === 'exercise' ? (isEn ? 'EXERCISE' : 'BÀI TẬP') : <><span>⏱️</span> <span className="font-mono tracking-wider tabular-nums">{formatTime(timeLeft)}</span></>}
               </div>
               <button type="button" onClick={() => { if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(()=>{}); else document.exitFullscreen(); }} className="hidden sm:inline-flex text-slate-500 hover:text-[#0a5482] transition-colors text-lg px-1 cursor-pointer" title={isFullscreen ? (isEn ? 'Exit fullscreen' : 'Thoát toàn màn hình') : (isEn ? 'Fullscreen' : 'Toàn màn hình')}>
                 {isFullscreen ? '🔲' : '⛶'}
               </button>
               <button type="button" onClick={() => handleSubmit(false)} disabled={isSubmitting || !numPages} className="bg-[#0a5482] hover:bg-[#084266] text-white font-bold text-xs sm:text-sm px-4 sm:px-6 py-1.5 rounded-lg transition-colors active:scale-95 disabled:opacity-50 whitespace-nowrap shadow-sm cursor-pointer">
                 {isSubmitting ? (isEn ? 'Grading...' : 'Đang chấm...') : (isEn ? 'Submit' : 'Nộp Bài')}
               </button>
            </>
          )}
        </div>
      </header>

      {isSubmitting && (
        <div className="fixed inset-0 z-50 bg-slate-900/70 backdrop-blur-sm flex flex-col items-center justify-center text-white">
          <div className="w-16 h-16 border-4 border-white/30 border-t-white rounded-full animate-spin mb-6"></div>
          <p className="text-xl font-bold mb-2">🧠 {isEn ? 'AI is scanning and grading your paper...' : 'AI đang quét và chấm bài...'}</p>
          <p className="text-sm text-slate-300">{isEn ? 'This may take 10–20 seconds depending on the number of pages' : 'Quá trình này có thể mất 10 - 20 giây tùy số lượng trang'}</p>
        </div>
      )}

      {/* Main Content Area */}
      <div className="flex-1 flex overflow-hidden w-full select-none relative">
        
        {/* PDF Viewer */}
        <div className="flex-1 h-full flex flex-col shrink-0 bg-[#525659] min-w-0">
          <div className="bg-[#323639] border-b border-[#202224] px-3 sm:px-4 flex justify-between items-center gap-3 h-12 shrink-0 shadow-sm overflow-x-auto no-scrollbar">
            <div className="flex items-center gap-2.5 sm:gap-3 shrink-0">
              <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest hidden sm:inline-block">📄 {isEn ? 'Cambridge Exam Paper' : 'Đề thi Cambridge'}</span>
              <div className="flex items-center bg-slate-800 rounded px-1 py-0.5">
                 <button onClick={handleZoomOut} className="w-6 h-6 text-slate-400 hover:text-white flex items-center justify-center font-bold" title={isEn ? 'Zoom out' : 'Thu nhỏ'}>-</button>
                 <span className="text-[11px] text-slate-300 font-mono w-10 text-center">{Math.round(zoomLevel * 100)}%</span>
                 <button onClick={handleZoomIn} className="w-6 h-6 text-slate-400 hover:text-white flex items-center justify-center font-bold" title={isEn ? 'Zoom in' : 'Phóng to'}>+</button>
              </div>
            </div>
            {!isReviewMode && (
              <div className="flex items-center gap-1 shrink-0">
                <button onClick={() => setDrawMode(prev => prev === 'pen' ? null : 'pen')} className={`px-3 py-1.5 rounded text-[12px] font-bold transition-all whitespace-nowrap ${drawMode === 'pen' ? 'bg-[#0a5482] text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title={isEn ? 'Pen' : 'Bút vẽ'}>✏️ {isEn ? 'Draw' : 'Viết'}</button>
                <button onClick={() => setDrawMode(prev => prev === 'line' ? null : 'line')} className={`px-2 py-1.5 rounded text-[12px] font-bold transition-all ${drawMode === 'line' ? 'bg-[#0a5482] text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title={isEn ? 'Straight line' : 'Đường thẳng'}>📏</button>
                <button onClick={() => setDrawMode(prev => prev === 'rect' ? null : 'rect')} className={`px-2 py-1.5 rounded text-[12px] font-bold transition-all ${drawMode === 'rect' ? 'bg-[#0a5482] text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title={isEn ? 'Rectangle' : 'Hình chữ nhật'}>▬</button>
                <button onClick={() => setDrawMode(prev => prev === 'circle' ? null : 'circle')} className={`px-2 py-1.5 rounded text-[12px] font-bold transition-all ${drawMode === 'circle' ? 'bg-[#0a5482] text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title={isEn ? 'Ellipse' : 'Hình elip'}>⬭</button>
                <button onClick={() => setDrawMode(prev => prev === 'triangle' ? null : 'triangle')} className={`px-2 py-1.5 rounded text-[12px] font-bold transition-all ${drawMode === 'triangle' ? 'bg-[#0a5482] text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title={isEn ? 'Triangle' : 'Tam giác'}>△</button>
                <button onClick={() => setDrawMode(prev => prev === 'text' ? null : 'text')} className={`px-2 py-1.5 rounded text-[12px] font-bold transition-all ${drawMode === 'text' ? 'bg-[#0a5482] text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title={isEn ? 'Text' : 'Chữ'}>T</button>
                <button onClick={() => setDrawMode(prev => prev === 'eraser' ? null : 'eraser')} className={`px-2 py-1.5 rounded text-[12px] font-bold transition-all whitespace-nowrap ${drawMode === 'eraser' ? 'bg-orange-500 text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title={isEn ? 'Eraser' : 'Tẩy'}>🧹 {isEn ? 'Eraser' : 'Tẩy'}</button>
                {drawMode && (
                  <>
                    <div className="w-px h-5 bg-slate-600 mx-1.5"></div>
                    {['#ff3333','#2ab4e8','#22c55e','#f59e0b','#111827'].map(c => (
                      <button key={c} onClick={() => setPenColor(c)} className={`w-6 h-6 rounded-full border-2 transition-transform shrink-0 ${penColor === c ? 'border-white scale-110 shadow-[0_0_8px_rgba(255,255,255,0.5)]' : 'border-slate-600'}`} style={{ backgroundColor: c }} />
                    ))}
                    <div className="w-px h-5 bg-slate-600 mx-1.5"></div>
                    <button onClick={() => {
                        if (window.confirm(isEn ? "Are you sure you want to clear ALL drawings on ALL pages?" : "Bạn có chắc muốn xóa TẤT CẢ nét vẽ trên TẤT CẢ các trang?")) {
                            const canvases = document.querySelectorAll('.student-canvas');
                            canvases.forEach(c => {
                                const ctx = (c as HTMLCanvasElement).getContext('2d');
                                if (ctx) ctx.clearRect(0, 0, (c as HTMLCanvasElement).width, (c as HTMLCanvasElement).height);
                            });
                            hasUnsavedDrawingsRef.current = false;
                        }
                    }} className="px-3 py-1.5 rounded text-[12px] text-slate-400 hover:text-white hover:bg-red-500 font-bold bg-slate-800 whitespace-nowrap" title={isEn ? 'Clear all' : 'Xóa tất cả'}>🗑️ {isEn ? 'Clear all' : 'Xóa hết'}</button>
                  </>
                )}
              </div>
            )}
            {isReviewMode && (
               <button onClick={() => setIsRightPanelOpen(!isRightPanelOpen)} className="px-4 py-1.5 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm transition-colors shadow-sm">
                   {isRightPanelOpen ? (isEn ? 'Hide Results ➔' : 'Ẩn Kết Quả ➔') : (isEn ? '⬅ View Results' : '⬅ Xem Kết Quả')}
               </button>
            )}
          </div>
          
          <div onScroll={handleContainerScroll} className={`flex-1 overflow-auto bg-[#525659] p-4 md:p-8 custom-scrollbar ${drawMode ? (drawMode === 'eraser' ? 'cursor-cell' : drawMode === 'text' ? 'cursor-text' : 'cursor-crosshair') : ''}`}>
             {!pdfUrl ? (
                <div className="flex flex-col items-center justify-center h-full text-slate-400 p-8 text-center bg-[#525659]">
                  <span className="text-5xl mb-4">📄</span>
                  <p className="font-bold">{isEn ? 'No exam PDF file available.' : 'Không có file PDF đề thi.'}</p>
                  <p className="text-sm mt-2">{isEn ? 'Please check the lesson configuration.' : 'Vui lòng kiểm tra lại cấu hình bài giảng.'}</p>
                </div>
             ) : pdfError ? (
                <div className="flex flex-col items-center justify-center h-full text-white p-8 text-center bg-[#525659] gap-4">
                  <span className="text-5xl">⚠️</span>
                  <p className="font-bold text-lg">{isEn ? 'Unable to load exam PDF' : 'Không thể tải file PDF đề thi'}</p>
                  <p className="text-sm text-slate-300 max-w-md">{pdfError}</p>
                  <div className="flex flex-wrap items-center justify-center gap-3 mt-2">
                    <button
                      type="button"
                      onClick={() => { setPdfError(null); setPdfReloadKey(k => k + 1); }}
                      className="px-4 py-2 rounded-lg bg-[#0a5482] hover:bg-[#084266] text-white text-sm font-bold transition"
                    >
                      🔄 {isEn ? 'Try again' : 'Thử tải lại'}
                    </button>
                    <a
                      href={pdfUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="px-4 py-2 rounded-lg bg-white/15 hover:bg-white/25 text-white text-sm font-bold transition"
                    >
                      ↗ {isEn ? 'Open PDF in new tab' : 'Mở PDF trong tab mới'}
                    </a>
                  </div>
                </div>
             ) : (
                <Document 
                    key={pdfReloadKey}
                    file={pdfUrl} 
                    onLoadSuccess={handleDocumentLoadSuccess} 
                    onLoadError={(err: any) => setPdfError(err?.message || (isEn ? 'Connection error or invalid PDF format.' : 'Lỗi kết nối hoặc định dạng PDF không hợp lệ.'))}
                    loading={<div className="text-white text-center py-20 animate-pulse">{isEn ? 'Loading PDF file...' : 'Đang tải file PDF...'}</div>}
                >
                    {Array.from(new Array(numPages || 0), (el, index) => (
                        <DrawingPage 
                            key={`page_${index + 1}`} 
                            pageNum={index + 1} 
                            drawMode={drawMode} 
                            penColor={penColor}
                            scale={zoomLevel}
                            isEn={isEn}
                            onStrokeDrawn={() => { hasUnsavedDrawingsRef.current = true; }}
                        />
                    ))}
                </Document>
             )}
          </div>
        </div>

        {/* Right Slide Panel for Feedback */}
        <div className={`absolute top-0 right-0 h-full w-[450px] max-w-full bg-[#f8fafc] shadow-[-10px_0_30px_rgba(0,0,0,0.3)] transition-transform duration-300 ease-in-out z-30 flex flex-col ${isRightPanelOpen ? 'translate-x-0' : 'translate-x-full'}`}>
          <div className="bg-[#323639] border-b border-[#202224] px-6 flex justify-between items-center h-12 shrink-0 shadow-sm">
            <span className="font-bold text-slate-300 text-[12px] uppercase tracking-widest flex items-center gap-2">
              <span>✅</span> {isEn ? 'Score & Feedback' : 'Bảng Điểm & Nhận Xét'}
            </span>
            <button onClick={() => setIsRightPanelOpen(false)} className="text-slate-400 hover:text-white text-xl">✕</button>
          </div>

          <div
            className="flex-1 overflow-y-auto p-4 sm:p-6 custom-scrollbar"
            onClick={(e) => {
              const lb = extractLightboxFromClick(e, e.currentTarget);
              if (lb) setImageLightbox(lb);
            }}
          >
            {gradeResult ? (
                <>
                    <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 mb-6 text-center">
                        <h2 className="text-xl font-black text-slate-800 mb-1">Total Score</h2>
                        <div className="text-5xl font-black text-[#0a5482] mb-3 tabular-nums">
                            {gradeResult.total_student_score} <span className="text-2xl text-slate-400">/ {gradeResult.total_max_score}</span>
                        </div>
                        <div className="w-full bg-slate-200 rounded-full h-2.5 mb-3">
                          <div className="bg-gradient-to-r from-[#0a5482] via-[#2ab4e8] to-emerald-400 h-2.5 rounded-full transition-all" style={{ width: `${gradeResult.total_max_score > 0 ? Math.min(100, (gradeResult.total_student_score / gradeResult.total_max_score) * 100) : 0}%` }}></div>
                        </div>
                        <p className="text-[13px] text-slate-600 bg-slate-50 p-3 rounded-xl italic text-left">{gradeResult.general_feedback}</p>
                    </div>

                    <div className="space-y-6">
                        {questions.map((q: any, qIdx: number) => (
                            <div key={qIdx} className="bg-white rounded-xl shadow-sm border border-slate-200 p-4">
                                <h3 className="font-black text-slate-800 text-[16px] border-b border-slate-100 pb-2 mb-3">Question {q.question_number}</h3>
                                
                                <div className="space-y-4">
                                    {(q.sub_questions || []).map((sub: any) => {
                                        const normId = (s: any) => String(s || '').toLowerCase().replace(/^q/, '').replace(/[^a-z0-9]/g, '');
                                        const feedbackData = gradeResult?.details?.find((d:any) => d.id === sub.id) || gradeResult?.details?.find((d:any) => normId(d.id) === normId(sub.id) || ((q.sub_questions || []).length === 1 && String(d.id) === String(q.question_number)));
                                        if (!feedbackData) return null;
                                        
                                        const isCorrect = feedbackData.student_score === sub.max_marks;
                                        const isWrong = feedbackData.student_score === 0;

                                        return (
                                            <div key={sub.id} className={`p-3 rounded-lg border ${isCorrect ? 'bg-emerald-50 border-emerald-200' : isWrong ? 'bg-red-50 border-red-200' : 'bg-orange-50 border-orange-200'}`}>
                                                <div className="flex justify-between items-start mb-2">
                                                    <label className="font-semibold text-slate-800 text-[13px] leading-relaxed pr-2 whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: renderLatex(sub.label) }} />
                                                    <span className="font-bold text-slate-400 text-[11px] whitespace-nowrap bg-white px-2 py-0.5 rounded shadow-sm">[{feedbackData.student_score}/{sub.max_marks}]</span>
                                                </div>
                                                
                                                <div className="text-[13px] text-slate-700 bg-white/70 p-2.5 rounded-lg border border-slate-200/50">
                                                    <div className="font-semibold text-slate-500 mb-1 text-[11px] uppercase tracking-wider">{isEn ? 'AI Feedback:' : 'AI Nhận xét:'}</div>
                                                    <div dangerouslySetInnerHTML={{ __html: escapeHtml(String(feedbackData.examiner_comment || feedbackData.feedback || '')).replace(/\\n|\n/g, '<br/>') }} />{feedbackData.correct_answer && (<div className="mt-2 pt-2 border-t border-slate-200/70 text-[12.5px]"><span className="font-bold text-slate-500 uppercase text-[10px] tracking-widest block mb-0.5">{isEn ? 'Official Answer (Cambridge MS):' : 'Đáp án chuẩn (Cambridge MS):'}</span><span className="font-semibold text-emerald-700" dangerouslySetInnerHTML={{ __html: renderLatex(String(feedbackData.correct_answer)) }} /></div>)}
                                                </div>

                                                {!isCorrect && (
                                                    <div className="flex flex-col gap-2 mt-3">
                                                        <button onClick={() => {
                                                            const query = isEn
                                                              ? `Question: "${latexToText(sub.label)}"\nStudent's answer: "Written directly on paper"\nCorrect answer: "${latexToText(feedbackData.correct_answer || '')}"\n\nPlease explain in English in detail why my answer is wrong and how to solve this question.`
                                                              : `Câu hỏi: "${latexToText(sub.label)}"\nĐáp án học sinh: "Làm trên giấy"\nĐáp án đúng: "${latexToText(feedbackData.correct_answer || '')}"\n\nThầy giải thích chi tiết giúp em tại sao em sai ạ!`;
                                                            const subjectTask = /math|0580|0606/i.test(`${testData?.test_type || ''} ${testData?.skill || ''} ${testData?.title || ''}`) ? 'math' : 'Science';
                                                            const btn = document.createElement('button');
                                                            btn.className = 'btn-ai-trigger';
                                                            btn.setAttribute('data-topic', query);
                                                            btn.setAttribute('data-task', subjectTask);
                                                            document.body.appendChild(btn);
                                                            btn.click();
                                                            document.body.removeChild(btn);
                                                        }} className="flex items-center justify-center gap-2 px-3 py-1.5 bg-gradient-to-r from-blue-500 to-cyan-500 text-white font-bold text-[12px] rounded-lg shadow hover:shadow-md transition-all">
                                                            💬 {isEn ? 'Chat with AI Teacher' : 'Chat Thầy AI'}
                                                        </button>
                                                        <button onClick={() => callAiTutor(latexToText(sub.label), isEn ? "Written on paper" : "Làm trên giấy", latexToText(feedbackData.correct_answer || ''))} className="flex items-center justify-center gap-2 px-3 py-1.5 bg-gradient-to-r from-amber-400 to-orange-400 text-white font-bold text-[12px] rounded-lg shadow hover:shadow-md transition-all">
                                                            📞 {isEn ? 'Call AI Tutor' : 'Gọi Gia Sư'}
                                                        </button>
                                                    </div>
                                                )}
                                            </div>
                                        );
                                    })}
                                </div>
                            </div>
                        ))}
                    </div>
                </>
            ) : (
                <div className="flex items-center justify-center h-full text-slate-400 font-medium">
                    {isEn ? 'No grading results yet.' : 'Chưa có kết quả chấm điểm.'}
                </div>
            )}
          </div>
        </div>

      </div>
      <IgcseFormulaSheetModal
        isOpen={showFormulaSheet}
        onClose={() => setShowFormulaSheet(false)}
        syllabus={mathSyllabus}
        calculatorPolicy={calcPolicy}
        isEn={isEn}
      />
      <ImageLightboxModal
        items={imageLightbox?.items || null}
        initialIndex={imageLightbox?.index ?? 0}
        onClose={() => setImageLightbox(null)}
      />
    </div>
  );
}
