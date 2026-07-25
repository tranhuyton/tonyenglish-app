import React, { useState, useRef, useEffect } from 'react';
import { supabase } from './supabase';
import { Document, Page, pdfjs } from 'react-pdf';
import 'react-pdf/dist/Page/AnnotationLayer.css';
import 'react-pdf/dist/Page/TextLayer.css';

pdfjs.GlobalWorkerOptions.workerSrc = `//unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;

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

const renderLatex = (text: string): string => {
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
    [/\\frac\{([^}]+)\}\{([^}]+)\}/g,'<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;font-size:0.85em;line-height:1.1"><span style="border-bottom:1px solid currentColor;padding:0 2px">$1</span><span style="padding:0 2px">$2</span></span>'],
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
    [/\^\{([^}]+)\}/g,'<sup>$1</sup>'],[/_\{([^}]+)\}/g,'<sub>$1</sub>'],
    [/\^\(([^)]+)\)/g,'<sup>$1</sup>'],[/_\(([^)]+)\)/g,'<sub>$1</sub>'],
    [/\^([0-9a-zA-Zα-ωΑ-Ω])/g,'<sup>$1</sup>'],[/_([0-9a-zA-Zα-ωΑ-Ω])/g,'<sub>$1</sub>'],
    [/\\,/g,' '],[/\\;/g,' '],[/\\!/g,''],
  ];
  for (const [p, s] of m) r = r.replace(p, s);
  r = r.replace(/\\([a-zA-Z]+)/g, '$1');
  return r;
};

const DrawingPage = ({ pageNum, drawMode, penColor, scale }: any) => {
    const canvasRef = useRef<HTMLCanvasElement>(null);
    const [isDrawing, setIsDrawing] = useState(false);
    const [shapeStart, setShapeStart] = useState<{x:number,y:number}|null>(null);
    const canvasSnapshot = useRef<ImageData|null>(null);
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
        setTimeout(resizeCanvas, 200);
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
            setIsDrawing(true);
            if (['line','rect','circle','triangle'].includes(drawMode)) {
                setShapeStart({x, y});
                canvasSnapshot.current = ctx.getImageData(0, 0, cv.width, cv.height);
            } else {
                ctx.beginPath(); ctx.moveTo(x, y);
            }
        };

        const handlePointerMove = (e: PointerEvent) => {
            if (!drawMode) return;
            // Ngăn cuộn trang
            e.preventDefault();
            
            if (!isDrawing) return;
            const ctx = cv.getContext('2d'); if (!ctx) return;
            const rect = cv.getBoundingClientRect();
            const scaleX = cv.width / rect.width;
            const scaleY = cv.height / rect.height;
            const x = (e.clientX - rect.left) * scaleX;
            const y = (e.clientY - rect.top) * scaleY;
            
            const dpr = window.devicePixelRatio || 1;
            if (['line','rect','circle','triangle'].includes(drawMode) && shapeStart && canvasSnapshot.current) {
                ctx.putImageData(canvasSnapshot.current, 0, 0);
                ctx.strokeStyle = penColor; ctx.lineWidth = 2 * scale * dpr; ctx.lineCap = 'round';
                ctx.globalCompositeOperation = 'source-over';
                ctx.beginPath();
                if (drawMode === 'line') { ctx.moveTo(shapeStart.x, shapeStart.y); ctx.lineTo(x, y); }
                else if (drawMode === 'rect') { ctx.rect(shapeStart.x, shapeStart.y, x - shapeStart.x, y - shapeStart.y); }
                else if (drawMode === 'circle') { const rx = Math.abs(x-shapeStart.x)/2, ry = Math.abs(y-shapeStart.y)/2; ctx.ellipse(shapeStart.x+(x-shapeStart.x)/2, shapeStart.y+(y-shapeStart.y)/2, rx, ry, 0, 0, Math.PI*2); }
                else if (drawMode === 'triangle') { ctx.moveTo(shapeStart.x+(x-shapeStart.x)/2, shapeStart.y); ctx.lineTo(x, y); ctx.lineTo(shapeStart.x, y); ctx.closePath(); }
                ctx.stroke();
            } else if (drawMode === 'pen' || drawMode === 'eraser') {
                ctx.strokeStyle = drawMode === 'eraser' ? 'rgba(0,0,0,1)' : penColor;
                ctx.lineWidth = drawMode === 'eraser' ? 20 * scale * dpr : 2 * scale * dpr;
                ctx.lineCap = 'round';
                ctx.globalCompositeOperation = drawMode === 'eraser' ? 'destination-out' : 'source-over';
                ctx.lineTo(x, y); ctx.stroke();
            }
        };

        const handlePointerUp = (e: PointerEvent) => {
            if (!drawMode) return;
            e.preventDefault();
            setIsDrawing(false); setShapeStart(null); canvasSnapshot.current = null;
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
    }, [drawMode, isDrawing, penColor, scale, shapeStart, textPos]);

    const stopDrawing = () => { setIsDrawing(false); setShapeStart(null); canvasSnapshot.current = null; };

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
                            }
                            setTextPos(null); setDrawText('');
                        } else if (e.key === 'Escape') { setTextPos(null); setDrawText(''); }
                    }}
                    className="absolute bg-white/90 border-2 border-[#1e88e5] rounded px-2 py-1 text-[14px] outline-none min-w-[120px] shadow-lg"
                    style={{ left: textPos.x, top: textPos.y, zIndex: 20, WebkitUserSelect: 'text', WebkitTouchCallout: 'default' } as React.CSSProperties}
                    placeholder="Gõ text rồi Enter..."
                />
            )}
        </div>
    );
};


export default function IgcseDirectPaperTest({ onBack, onStartTest, testData: propTestData }: { onBack?: () => void, onStartTest?: any, testData?: any }) {
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
  const initIsReview = !!testData?.isReview;
  const [isReviewMode, setIsReviewMode] = useState(initIsReview);

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [gradeResult, setGradeResult] = useState<any>(() => {
      if (initIsReview && testData?.aiFeedback) return testData.aiFeedback;
      return null;
  });

  const [drawMode, setDrawMode] = useState<'pen'|'eraser'|'line'|'rect'|'circle'|'triangle'|'text'|null>(null);
  const [penColor, setPenColor] = useState('#111827');
  const [numPages, setNumPages] = useState<number | null>(null);
  const [zoomLevel, setZoomLevel] = useState<number>(1.2);
  
  const [timeLeft, setTimeLeft] = useState(7200); 
  const isFinishingRef = useRef(false);

  const [isRightPanelOpen, setIsRightPanelOpen] = useState(initIsReview);

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
      setNumPages(numPages);
  };

  const handleZoomIn = () => setZoomLevel(prev => Math.min(prev + 0.2, 3.0));
  const handleZoomOut = () => setZoomLevel(prev => Math.max(prev - 0.2, 0.6));

  const handleSubmit = async () => {
    const isExercise = testData?.content_json?.basicInfo?.category === 'exercise';
    if (!isExercise && timeLeft > 0 && !window.confirm("Bạn có chắc chắn muốn nộp bài thi? AI sẽ phân tích hình ảnh mất khoảng 10-20 giây.")) { return; }
    if (isExercise && !window.confirm("Bạn có chắc chắn muốn nộp bài?")) { return; }

    setIsSubmitting(true);
    isFinishingRef.current = true;
    
    if (testData?.id) {
       localStorage.removeItem(`igcse_endtime_${testData.id}`);
    }

    try {
      const imageAnswers: { questionId: string, base64: string }[] = [];
      const textAnswers = { "ALL": "Học sinh làm bài trực tiếp trên giấy (PDF). Vui lòng xem các file đính kèm." };

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
            pdfUrl: testData.insert_pdf_url || testData.pdf_url || null
        }
      });

      if (error) throw new Error("Lỗi gọi Server: " + error.message);
      if (data?.error) throw new Error("Lỗi chấm điểm: " + data.error);
      
      let cleanJson = (data.result || "").replace(/```json/gi, "").replace(/```/gi, "").trim();
      // Loại bỏ các ký tự điều khiển/xuống dòng thực tế (literal newlines/tabs) bị dính trong chuỗi trả về
      // vì JSON.parse sẽ crash nếu gặp literal \n bên trong một string value
      cleanJson = cleanJson.replace(/[\n\r\t]+/g, ' ');
      // Xóa dấu phẩy thừa (trailing commas) nếu có
      cleanJson = cleanJson.replace(/,\s*([\}\]])/g, '$1');
      // Thử lọc lấy phần thân JSON bằng Regex nếu AI trả về kèm theo text thừa ở đầu/cuối
      const jsonMatch = cleanJson.match(/\{[\s\S]*\}/);
      if (jsonMatch) cleanJson = jsonMatch[0];

      let gradedData;
      try {
          gradedData = JSON.parse(cleanJson);
      } catch (parseErr: any) {
          console.error("Lỗi parse JSON từ AI:", parseErr);
          console.log("Raw AI Output:", cleanJson);
          gradedData = {
              total_student_score: 0,
              total_max_score: 0,
              general_feedback: "⚠️ AI trả về dữ liệu bị lỗi định dạng (chứa ký tự không hợp lệ). Dưới đây là nội dung thô AI trả về:\n\n" + cleanJson,
              details: []
          };
      }

      setGradeResult(gradedData);
      setIsReviewMode(true);
      setIsRightPanelOpen(true);
      setDrawMode(null);

      try {
        const { data: { user } } = await supabase.auth.getUser();
        if (user) {
          const rawTime = testData.json_config?.timeLimit || testData.timeLimit || testData.time_limit || 120;
          const initialSeconds = parseInt(rawTime) * 60;
          const timeSpentSecs = initialSeconds - timeLeft;
          
          await supabase.from('test_results').insert([{
            user_id: user.id, course_id: testData.course_id, test_title: testData.title || "IGCSE Direct Paper",
            test_type: 'IGCSE-Science', score: gradedData.total_student_score, total_score: gradedData.total_max_score,
            time_spent: timeSpentSecs > 0 ? timeSpentSecs : 0,
            details: { test_id: testData.id, userAnswers: {}, aiFeedback: gradedData }
          }]);
        }
      } catch (dbError) { console.error("DB save error:", dbError); }

    } catch (err: any) {
      if (err.message && err.message.includes("Unexpected end of JSON input")) {
          alert("❌ Không thể nộp bài do kết nối gián đoạn hoặc file ảnh quá nặng. Vui lòng thử nộp lại.");
      } else {
          alert("❌ Có lỗi trong lúc chấm: " + err.message);
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  useEffect(() => {
    if (isLoading || !testData || gradeResult || isFinishingRef.current || isReviewMode) return;
    if (testData.content_json?.basicInfo?.category === 'exercise') return;
    const timer = setInterval(() => {
        const currentEndTime = getSavedEndTime(testData.id);
        if (currentEndTime) {
            const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
            setTimeLeft(remaining);
            if (remaining <= 0) { clearInterval(timer); alert("⏰ Hết giờ làm bài!"); handleSubmit(); }
        } else { setTimeLeft(prev => Math.max(0, prev - 1)); }
    }, 1000);
    return () => clearInterval(timer);
  }, [isLoading, testData, gradeResult, isReviewMode]);

  const callAiTutor = (questionText: string, studentAns: string, correctAnswer: string) => {
      const tutorContext = {
          overall: 'IGCSE Review',
          transcript: `Câu hỏi: "${questionText}". \nĐáp án của học sinh: ${studentAns}. \nĐáp án đúng Cambridge MS: "${correctAnswer}".`,
          feedback: "Bạn là gia sư Cambridge IGCSE. Học sinh đang xem lại bài thi và không hiểu câu này. Hãy chủ động chào, đọc câu hỏi và giải thích chi tiết tại sao đáp án đúng là như vậy, phân tích từng bước lập luận. Dùng giọng điệu ân cần, dễ hiểu, nếu có công thức hãy đọc rõ ràng."
      };
      sessionStorage.setItem('tony_live_mode', 'TUTOR');
      sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
      sessionStorage.setItem('tony_auto_start', 'true');
      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
  };

  if (isLoading) return (
    <div className="h-screen w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold">
      <div className="animate-spin text-4xl mb-4">⏳</div>
      <p>Đang tải đề thi IGCSE (Direct)...</p>
    </div>
  );

  if (!testData || (!isReviewMode && (!testData.json_config || !testData.json_config.questions))) return (
    <div className="h-screen w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold gap-4">
      <p>⚠️ Chưa có cấu hình đề thi trong hệ thống.</p>
      <button onClick={onBack} className="bg-[#1e88e5] px-6 py-2 rounded hover:bg-blue-700 transition-colors">Quay lại</button>
    </div>
  );

  const questions = testData.json_config.questions || [];
  const pdfUrl = testData.insert_pdf_url || testData.pdf_url;

  const handleContainerScroll = (e: React.UIEvent<HTMLDivElement>) => {
      const el = e.currentTarget;
      if (el.scrollTop <= 0) el.scrollTop = 1;
      else if (el.scrollTop + el.clientHeight >= el.scrollHeight) el.scrollTop -= 1;
  };

  return (
    <div 
      className="h-screen w-screen flex flex-col bg-[#e5e7eb] font-sans text-slate-900 overflow-hidden select-none"
      style={{ WebkitUserSelect: 'none', WebkitTouchCallout: 'none' } as React.CSSProperties}
    >
      {/* Header */}
      <header className="h-14 w-full bg-white border-b border-slate-300 flex items-center justify-between px-4 sm:px-6 shrink-0 z-20 box-border">
        <div className="flex items-center gap-3 sm:gap-4 overflow-hidden">
          <button onClick={onBack} className="text-slate-600 hover:text-black font-bold text-sm transition-colors whitespace-nowrap">← Quay lại</button>
          <div className="h-5 w-px bg-slate-300 hidden sm:block"></div>
          <div className="truncate flex items-baseline gap-2">
            <h1 className="font-bold text-black text-[15px] leading-tight truncate">{isReviewMode ? `[REVIEW] ${testData.title}` : testData.title}</h1>
            <span className="text-xs text-slate-500 font-medium px-2 py-0.5 bg-slate-100 rounded">Chế độ vẽ trực tiếp</span>
          </div>
        </div>
        {!gradeResult && !isReviewMode && (
          <div className="flex items-center gap-2 sm:gap-4 shrink-0">
             <div className={`font-bold flex items-center gap-2 px-3 py-1 rounded ${testData.content_json?.basicInfo?.category === 'exercise' ? 'text-[#0ea5e9] bg-[#0ea5e9]/10' : (timeLeft <= 300 ? 'text-red-600 bg-red-50 animate-pulse' : 'text-slate-600')}`}>
               {testData.content_json?.basicInfo?.category === 'exercise' ? 'BÀI TẬP' : <><span>⏱️</span> <span className="hidden sm:inline font-mono tracking-widest">{formatTime(timeLeft)}</span></>}
             </div>
             <button onClick={() => { if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(()=>{}); else document.exitFullscreen(); }} className="text-slate-500 hover:text-black transition-colors text-lg px-1" title="Toàn màn hình">
               {document.fullscreenElement ? '🔲' : '⛶'}
             </button>
             <button onClick={handleSubmit} disabled={isSubmitting || !numPages} className="bg-[#1e88e5] hover:bg-blue-700 text-white font-bold text-sm px-6 py-1.5 rounded transition-colors active:scale-95 disabled:opacity-50 whitespace-nowrap">
               {isSubmitting ? 'Đang chấm...' : 'Nộp Bài'}
             </button>
          </div>
        )}
      </header>

      {isSubmitting && (
        <div className="fixed inset-0 z-50 bg-slate-900/70 backdrop-blur-sm flex flex-col items-center justify-center text-white">
          <div className="w-16 h-16 border-4 border-white/30 border-t-white rounded-full animate-spin mb-6"></div>
          <p className="text-xl font-bold mb-2">🧠 AI đang quét và chấm bài...</p>
          <p className="text-sm text-slate-300">Quá trình này có thể mất 10 - 20 giây tùy số lượng trang</p>
        </div>
      )}

      {/* Main Content Area */}
      <div className="flex-1 flex overflow-hidden w-full select-none relative">
        
        {/* PDF Viewer */}
        <div className="flex-1 h-full flex flex-col shrink-0 bg-[#525659]">
          <div className="bg-[#323639] border-b border-[#202224] px-4 flex justify-between items-center h-12 shrink-0 shadow-sm">
            <div className="flex items-center gap-3">
              <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest hidden sm:inline-block">📄 Đề thi Cambridge</span>
              <div className="flex items-center bg-slate-800 rounded px-1 py-0.5">
                 <button onClick={handleZoomOut} className="w-6 h-6 text-slate-400 hover:text-white flex items-center justify-center font-bold" title="Thu nhỏ">-</button>
                 <span className="text-[11px] text-slate-300 font-mono w-10 text-center">{Math.round(zoomLevel * 100)}%</span>
                 <button onClick={handleZoomIn} className="w-6 h-6 text-slate-400 hover:text-white flex items-center justify-center font-bold" title="Phóng to">+</button>
              </div>
            </div>
            {!isReviewMode && (
              <div className="flex items-center gap-1">
                <button onClick={() => setDrawMode(prev => prev === 'pen' ? null : 'pen')} className={`px-3 py-1.5 rounded text-[12px] font-bold transition-all ${drawMode === 'pen' ? 'bg-[#1e88e5] text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title="Bút vẽ">✏️ Viết</button>
                <button onClick={() => setDrawMode(prev => prev === 'line' ? null : 'line')} className={`px-2 py-1.5 rounded text-[12px] font-bold transition-all ${drawMode === 'line' ? 'bg-[#1e88e5] text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title="Đường thẳng">📏</button>
                <button onClick={() => setDrawMode(prev => prev === 'rect' ? null : 'rect')} className={`px-2 py-1.5 rounded text-[12px] font-bold transition-all ${drawMode === 'rect' ? 'bg-[#1e88e5] text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title="Hình chữ nhật">▬</button>
                <button onClick={() => setDrawMode(prev => prev === 'circle' ? null : 'circle')} className={`px-2 py-1.5 rounded text-[12px] font-bold transition-all ${drawMode === 'circle' ? 'bg-[#1e88e5] text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title="Hình elip">⬭</button>
                <button onClick={() => setDrawMode(prev => prev === 'triangle' ? null : 'triangle')} className={`px-2 py-1.5 rounded text-[12px] font-bold transition-all ${drawMode === 'triangle' ? 'bg-[#1e88e5] text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title="Tam giác">△</button>
                <button onClick={() => setDrawMode(prev => prev === 'text' ? null : 'text')} className={`px-2 py-1.5 rounded text-[12px] font-bold transition-all ${drawMode === 'text' ? 'bg-[#1e88e5] text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title="Chữ">T</button>
                <button onClick={() => setDrawMode(prev => prev === 'eraser' ? null : 'eraser')} className={`px-2 py-1.5 rounded text-[12px] font-bold transition-all ${drawMode === 'eraser' ? 'bg-orange-500 text-white' : 'text-slate-400 hover:text-white bg-slate-800'}`} title="Tẩy">🧹 Tẩy</button>
                {drawMode && (
                  <>
                    <div className="w-px h-5 bg-slate-600 mx-2"></div>
                    {['#ff3333','#1e88e5','#22c55e','#f59e0b','#111827'].map(c => (
                      <button key={c} onClick={() => setPenColor(c)} className={`w-6 h-6 rounded-full border-2 transition-transform ${penColor === c ? 'border-white scale-110 shadow-[0_0_8px_rgba(255,255,255,0.5)]' : 'border-slate-600'}`} style={{ backgroundColor: c }} />
                    ))}
                    <div className="w-px h-5 bg-slate-600 mx-2"></div>
                    <button onClick={() => {
                        if (window.confirm("Bạn có chắc muốn xóa TẤT CẢ nét vẽ trên TẤT CẢ các trang?")) {
                            const canvases = document.querySelectorAll('.student-canvas');
                            canvases.forEach(c => {
                                const ctx = (c as HTMLCanvasElement).getContext('2d');
                                if (ctx) ctx.clearRect(0, 0, (c as HTMLCanvasElement).width, (c as HTMLCanvasElement).height);
                            });
                        }
                    }} className="px-3 py-1.5 rounded text-[12px] text-slate-400 hover:text-white hover:bg-red-500 font-bold bg-slate-800" title="Xóa tất cả">🗑️ Xóa hết</button>
                  </>
                )}
              </div>
            )}
            {isReviewMode && (
               <button onClick={() => setIsRightPanelOpen(!isRightPanelOpen)} className="px-4 py-1.5 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm transition-colors shadow-sm">
                   {isRightPanelOpen ? 'Ẩn Kết Quả ➔' : '⬅ Xem Kết Quả'}
               </button>
            )}
          </div>
          
          <div onScroll={handleContainerScroll} className={`flex-1 overflow-auto bg-[#525659] p-4 md:p-8 custom-scrollbar ${drawMode ? (drawMode === 'eraser' ? 'cursor-cell' : drawMode === 'text' ? 'cursor-text' : 'cursor-crosshair') : ''}`}>
             {!pdfUrl ? (
                <div className="flex flex-col items-center justify-center h-full text-slate-400 p-8 text-center bg-[#525659]">
                  <span className="text-5xl mb-4">📄</span>
                  <p className="font-bold">Không có file PDF đề thi.</p>
                  <p className="text-sm mt-2">Vui lòng kiểm tra lại cấu hình bài giảng.</p>
                </div>
             ) : (
                <Document 
                    file={pdfUrl} 
                    onLoadSuccess={handleDocumentLoadSuccess} 
                    loading={<div className="text-white text-center py-20 animate-pulse">Đang tải file PDF...</div>}
                >
                    {Array.from(new Array(numPages || 0), (el, index) => (
                        <DrawingPage 
                            key={`page_${index + 1}`} 
                            pageNum={index + 1} 
                            drawMode={drawMode} 
                            penColor={penColor}
                            scale={zoomLevel}
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
              <span>✅</span> Bảng Điểm & Nhận Xét
            </span>
            <button onClick={() => setIsRightPanelOpen(false)} className="text-slate-400 hover:text-white text-xl">✕</button>
          </div>

          <div className="flex-1 overflow-y-auto p-4 sm:p-6 custom-scrollbar">
            {gradeResult ? (
                <>
                    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 mb-6 text-center">
                        <h2 className="text-xl font-black text-slate-800 mb-1">Total Score</h2>
                        <div className="text-5xl font-black text-[#1e88e5] mb-3">
                            {gradeResult.total_student_score} <span className="text-2xl text-slate-400">/ {gradeResult.total_max_score}</span>
                        </div>
                        <div className="w-full bg-slate-200 rounded-full h-2.5 mb-3">
                          <div className="bg-gradient-to-r from-[#1e88e5] to-emerald-400 h-2.5 rounded-full transition-all" style={{ width: `${Math.min(100, (gradeResult.total_student_score / gradeResult.total_max_score) * 100)}%` }}></div>
                        </div>
                        <p className="text-[13px] text-slate-600 bg-slate-50 p-3 rounded-lg italic text-left">{gradeResult.general_feedback}</p>
                    </div>

                    <div className="space-y-6">
                        {questions.map((q: any, qIdx: number) => (
                            <div key={qIdx} className="bg-white rounded-xl shadow-sm border border-slate-200 p-4">
                                <h3 className="font-black text-slate-800 text-[16px] border-b border-slate-100 pb-2 mb-3">Question {q.question_number}</h3>
                                
                                <div className="space-y-4">
                                    {(q.sub_questions || []).map((sub: any) => {
                                        const feedbackData = gradeResult?.details?.find((d:any) => d.id === sub.id);
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
                                                    <div className="font-semibold text-slate-500 mb-1 text-[11px] uppercase tracking-wider">AI Nhận xét:</div>
                                                    <div dangerouslySetInnerHTML={{ __html: feedbackData.feedback?.replace(/\\n/g, '<br/>') || '' }} />
                                                </div>

                                                {!isCorrect && (
                                                    <div className="flex flex-col gap-2 mt-3">
                                                        <button onClick={() => {
                                                            const query = `Câu hỏi: "${latexToText(sub.label)}"\nĐáp án học sinh: "Làm trên giấy"\nĐáp án đúng: "${latexToText(feedbackData.correct_answer || '')}"\n\nThầy giải thích chi tiết giúp em tại sao em sai ạ!`;
                                                            const subjectTask = (testData?.test_type || testData?.skill || '').includes('Math') ? 'math' : 'Science';
                                                            const btn = document.createElement('button');
                                                            btn.className = 'btn-ai-trigger';
                                                            btn.setAttribute('data-topic', query);
                                                            btn.setAttribute('data-task', subjectTask);
                                                            document.body.appendChild(btn);
                                                            btn.click();
                                                            document.body.removeChild(btn);
                                                        }} className="flex items-center justify-center gap-2 px-3 py-1.5 bg-gradient-to-r from-blue-500 to-cyan-500 text-white font-bold text-[12px] rounded-lg shadow hover:shadow-md transition-all">
                                                            💬 Chat Thầy AI
                                                        </button>
                                                        <button onClick={() => callAiTutor(latexToText(sub.label), "Làm trên giấy", latexToText(feedbackData.correct_answer || ''))} className="flex items-center justify-center gap-2 px-3 py-1.5 bg-gradient-to-r from-amber-400 to-orange-400 text-white font-bold text-[12px] rounded-lg shadow hover:shadow-md transition-all">
                                                            📞 Gọi Gia Sư
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
                    Chưa có kết quả chấm điểm.
                </div>
            )}
          </div>
        </div>

        <div className="fixed bottom-2 right-2 text-[10px] text-white/50 z-[100] font-mono pointer-events-none bg-black/20 px-1 rounded">
          v3.0-final
        </div>
        
      </div>
    </div>
  );
}
