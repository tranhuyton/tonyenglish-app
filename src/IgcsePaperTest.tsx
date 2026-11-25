import React, { useState, useRef, useEffect, useMemo } from 'react';
import { supabase } from './supabase';
import { useTestGuideVideo, TestGuideVideoButton, TestGuideVideoPlayer, TestGuideVideoEditModal } from './TestGuideVideo';
import { useLmsLang, LmsLangToggle } from './utils/lmsI18n';
import { ImageLightboxModal, LightboxState, extractLightboxFromClick } from './mcqImageUtils';
import 'katex/dist/katex.min.css';
import { renderIgcseLatex, detectCalculatorPolicy, detectIgcseMathSyllabus } from './katexUtils';
import IgcseFormulaSheetModal from './IgcseFormulaSheetModal';

export default function IgcsePaperTest({ onBack, onStartTest, testData: propTestData }: { onBack?: () => void, onStartTest?: any, testData?: any }) {
  const [lang, setLang] = useLmsLang();
  const isEn = lang === 'en';
  const isEnRef = useRef(isEn);
  isEnRef.current = isEn;

  const [testData, setTestData] = useState<any>(() => {
      let raw = propTestData;
      if (!raw) {
          const saved = sessionStorage.getItem('lms_current_test');
          raw = saved ? JSON.parse(saved) : null;
      }
      if (!raw) return null;
      // Normalize: ensure json_config.questions and insert_pdf_url exist from either top-level or content_json
      if (!raw.json_config?.questions && raw.content_json?.questions) {
          raw.json_config = { ...(raw.json_config || {}), questions: raw.content_json.questions, timeLimit: raw.content_json?.basicInfo?.timeLimit || raw.json_config?.timeLimit || 120 };
      }
      if (!raw.insert_pdf_url) {
          raw.insert_pdf_url = raw.pdf_url || raw.content_json?.basicInfo?.insert_pdf_url || raw.content_json?.basicInfo?.pdf_url || raw.content_json?.pdf_url || raw.json_config?.insert_pdf_url || raw.json_config?.pdf_url || null;
      }
      return raw;
  });
  
  const [isLoading, setIsLoading] = useState(!testData);
  const [imageLightbox, setImageLightbox] = useState<LightboxState | null>(null);
  const [showFormulaSheet, setShowFormulaSheet] = useState(false);
  const initIsReview = !!testData?.isReview;
  const [isReviewMode, setIsReviewMode] = useState(initIsReview);
  useEffect(() => { window.dispatchEvent(new CustomEvent('tony-review-mode-change', { detail: Boolean(isReviewMode) })); return () => { window.dispatchEvent(new CustomEvent('tony-review-mode-change', { detail: false })); }; }, [isReviewMode]);

  const [answers, setAnswers] = useState<Record<string, string>>(() => {
      if (initIsReview && testData?.past_answers) return testData.past_answers;
      if (!testData?.id) return {};
      try {
         const saved = localStorage.getItem(`igcse_ans_${testData.id}`);
         return saved ? JSON.parse(saved) : {};
      } catch(e) { return {}; }
  });
  
  const answersRef = useRef(answers);
  useEffect(() => { answersRef.current = answers; }, [answers]);

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [gradeResult, setGradeResult] = useState<any>(() => {
      if (initIsReview && testData?.aiFeedback) return testData.aiFeedback;
      return null;
  });

  const [leftWidth, setLeftWidth] = useState(50); 
  const [paperViewMode, setPaperViewMode] = useState<'split' | 'text-only'>('split');
  const [isDragging, setIsDragging] = useState(false);
  const [isDesktop, setIsDesktop] = useState(() => typeof window !== 'undefined' ? window.innerWidth >= 768 : true);
  const [isFullscreen, setIsFullscreen] = useState(() => typeof document !== 'undefined' ? !!document.fullscreenElement : false);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const onResize = () => setIsDesktop(window.innerWidth >= 768);
    const onFsChange = () => setIsFullscreen(!!document.fullscreenElement);
    window.addEventListener('resize', onResize);
    document.addEventListener('fullscreenchange', onFsChange);
    return () => {
      window.removeEventListener('resize', onResize);
      document.removeEventListener('fullscreenchange', onFsChange);
    };
  }, []);

  const handleSafeExit = () => {
    if (!isReviewMode && !gradeResult) {
      if (!window.confirm(isEn ? 'You are currently taking an IGCSE test. Are you sure you want to exit?' : 'Bạn đang làm bài thi IGCSE. Bạn có chắc muốn thoát ra ngoài không?')) return;
    }
    if (onBack) onBack();
  };

  // Drawing on PDF
  const [drawMode, setDrawMode] = useState<'pen'|'eraser'|'line'|'rect'|'circle'|'triangle'|'text'|null>(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [penColor, setPenColor] = useState('#ff3333');
  const drawCanvasRef = useRef<HTMLCanvasElement>(null);
  const [shapeStart, setShapeStart] = useState<{x:number,y:number}|null>(null);
  const canvasSnapshot = useRef<ImageData|null>(null);
  const [drawText, setDrawText] = useState('');
  const [textPos, setTextPos] = useState<{x:number,y:number}|null>(null);

  // 🎬 Video hướng dẫn & gợi ý (Hỗ trợ nhiều video)
  const {
    videos: guideVideos,
    activeVideoIndex: activeGuideVideoIndex,
    setActiveVideoIndex: setActiveGuideVideoIndex,
    videoUrl: guideVideoUrl,
    isOpen: isGuideVideoOpen,
    setIsOpen: setIsGuideVideoOpen,
    isTheaterOpen: isGuideVideoTheaterOpen,
    setIsTheaterOpen: setIsGuideVideoTheaterOpen,
    isEditModalOpen: isGuideVideoEditModalOpen,
    setIsEditModalOpen: setIsGuideVideoEditModalOpen,
    handleSaveVideos: handleSaveGuideVideos,
  } = useTestGuideVideo(testData, (newUrl, newVideos) => {
    setTestData((prev: any) => ({
      ...prev,
      guide_video_url: newUrl,
      guide_videos: newVideos,
      content_json: {
        ...(prev?.content_json || {}),
        guide_video_url: newUrl,
        guide_videos: newVideos,
        basicInfo: {
          ...(prev?.content_json?.basicInfo || {}),
          guide_video_url: newUrl,
          guide_videos: newVideos,
        }
      }
    }));
  });

  const [timeLeft, setTimeLeft] = useState(7200); 
  const isFinishingRef = useRef(false);

  const getSavedEndTime = (testId: string) => {
    if (!testId) return null;
    const saved = localStorage.getItem(`igcse_endtime_${testId}`);
    return saved ? parseInt(saved, 10) : null;
  };

  // Auto-save answers to localStorage
  useEffect(() => {
    if (testData?.id && !isFinishingRef.current && !gradeResult && !isReviewMode) {
      localStorage.setItem(`igcse_ans_${testData.id}`, JSON.stringify(answers));
    }
  }, [answers, testData?.id, gradeResult, isReviewMode]);

  // Initialize timer — skip entirely for exercises
  useEffect(() => {
    if (testData && !isReviewMode) {
       const isExercise = testData.content_json?.basicInfo?.category === 'exercise';
       if (isExercise) {
           // Exercises have no timer — just mark loading done
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

  // Resize drawing canvas to match container
  useEffect(() => {
    const cv = drawCanvasRef.current;
    if (!cv) return;
    const parent = cv.parentElement;
    if (!parent) return;
    const resize = () => { 
        if (cv.width !== parent.clientWidth || cv.height !== parent.clientHeight) {
            const ctx = cv.getContext('2d');
            let tempCanvas: HTMLCanvasElement | null = null;
            if (cv.width > 0 && cv.height > 0) {
                tempCanvas = document.createElement('canvas');
                tempCanvas.width = cv.width;
                tempCanvas.height = cv.height;
                tempCanvas.getContext('2d')?.drawImage(cv, 0, 0);
            }
            cv.width = parent.clientWidth; 
            cv.height = parent.clientHeight;
            if (tempCanvas && ctx) {
                ctx.drawImage(tempCanvas, 0, 0);
            }
        }
    };
    resize();
    const ro = new ResizeObserver(resize);
    ro.observe(parent);
    return () => ro.disconnect();
  }, [leftWidth, paperViewMode]);

  const handleAnswerChange = (inputId: string, value: string) => {
    if (isReviewMode) return;
    setAnswers(prev => ({ ...prev, [inputId]: value }));
  };

  // Image compression at browser - resize to max 1000px and compress JPEG 60%
  const handleImageUpload = (questionId: string, file: File) => {
      const reader = new FileReader();
      reader.onload = (e) => {
          const img = new Image();
          img.onload = () => {
              const canvas = document.createElement('canvas');
              const MAX_WIDTH = 1000; 
              const MAX_HEIGHT = 1000;
              let width = img.width;
              let height = img.height;

              if (width > height) {
                  if (width > MAX_WIDTH) { height *= MAX_WIDTH / width; width = MAX_WIDTH; }
              } else {
                  if (height > MAX_HEIGHT) { width *= MAX_HEIGHT / height; height = MAX_HEIGHT; }
              }
              
              canvas.width = width;
              canvas.height = height;
              const ctx = canvas.getContext('2d');
              if (ctx) {
                  ctx.fillStyle = '#ffffff'; 
                  ctx.fillRect(0, 0, canvas.width, canvas.height);
                  ctx.drawImage(img, 0, 0, width, height);
                  const resizedBase64 = canvas.toDataURL('image/jpeg', 0.6);
                  handleAnswerChange(questionId, resizedBase64);
              }
          };
          img.src = e.target?.result as string;
      };
      reader.readAsDataURL(file);
  };

  useEffect(() => {
    const handleGlobalPaste = (e: ClipboardEvent) => {
      if (isReviewMode) return;
      const items = e.clipboardData?.items;
      if (!items) return;
      
      let imageFile: File | null = null;
      for (let i = 0; i < items.length; i++) {
          if (items[i].type.startsWith('image/')) {
              e.preventDefault();
              imageFile = items[i].getAsFile();
              break;
          }
      }
      if (!imageFile) return;

      const imageSubIds: string[] = [];
      const questions = testData?.json_config?.questions || [];
      questions.forEach((q: any) => {
          (q.sub_questions || []).forEach((sub: any) => {
              if (sub.type !== 'short_answer' && sub.type !== 'long_answer') {
                  imageSubIds.push(sub.id);
              }
          });
      });

      if (imageSubIds.length > 0) {
          const emptyId = imageSubIds.find(id => !answers[id]);
          const targetId = emptyId || imageSubIds[imageSubIds.length - 1];
          handleImageUpload(targetId, imageFile);
      }
    };

    window.addEventListener('paste', handleGlobalPaste);
    return () => window.removeEventListener('paste', handleGlobalPaste);
  }, [testData, answers, isReviewMode]);

  const escapeHtml = (str: string): string =>
    String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

  // LaTeX → KaTeX / HTML renderer for question labels & marking schemes
  const renderLatex = (text: string): string => renderIgcseLatex(text);

  // LaTeX → Unicode/Plain Text converter for AI prompt and chat display
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

  // Unicode character palette for formula insertion
  const [showPalette, setShowPalette] = useState<Record<string, boolean>>({});
  const [paletteTab, setPaletteTab] = useState<'sci'|'geo'|'alg'|'set'>('sci');
  const inputRefs = useRef<Record<string, HTMLInputElement | HTMLTextAreaElement | null>>({});

  useEffect(() => {
    const hasOpen = Object.values(showPalette).some(Boolean);
    if (!hasOpen) return;
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setShowPalette({});
      }
    };
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [showPalette]);
  
  const charTabs = {
    sci: {
      label: '🧪 Science',
      groups: [
        { label: isEn ? 'Subscript' : 'Chỉ số dưới', chars: ['₀','₁','₂','₃','₄','₅','₆','₇','₈','₉'] },
        { label: isEn ? 'Superscript' : 'Chỉ số trên', chars: ['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹','⁺','⁻','ⁿ'] },
        { label: isEn ? 'Chemistry & Physics' : 'Hóa học & Vật lý', chars: ['→','⇌','Δ','°','±','×','÷','≈','≠','≤','≥','∞','α','β','γ','θ','λ','μ','Ω','π'] },
      ]
    },
    geo: {
      label: isEn ? '📐 Geometry' : '📐 Hình học',
      groups: [
        { label: isEn ? 'Geometry' : 'Hình học', chars: ['∠','△','⊥','∥','∼','≡','°'] },
        { label: isEn ? 'Symbols' : 'Ký hiệu', chars: ['π','√','²','³','±','≈','≠','≤','≥','∞','→','⇒','⇔'] },
      ]
    },
    alg: {
      label: isEn ? '📊 Algebra' : '📊 Đại số',
      groups: [
        { label: isEn ? 'Scripts' : 'Chỉ số', chars: ['₀','₁','₂','₃','ₙ','⁰','¹','²','³','ⁿ','⁺','⁻'] },
        { label: isEn ? 'Operators' : 'Phép toán', chars: ['±','∓','×','÷','·','√','∛','≈','≠','≡','∝','≤','≥'] },
        { label: isEn ? 'Advanced' : 'Cao cấp', chars: ['∫','Σ','∏','∂','∞','ℝ','ℤ','ℕ','|'] },
        { label: isEn ? 'Trigonometry' : 'Lượng giác', chars: ['θ','α','β','γ','φ','π','°'] },
      ]
    },
    set: {
      label: isEn ? '{ } Sets' : '{ } Tập hợp',
      groups: [
        { label: isEn ? 'Sets' : 'Tập hợp', chars: ['∩','∪','⊂','⊆','⊃','⊇','∈','∉','∅'] },
        { label: 'Logic', chars: ['∀','∃','¬','∧','∨','⇒','⇔','∴','∵'] },
        { label: isEn ? 'Arrows' : 'Mũi tên', chars: ['→','←','↔','⇒','⇐','⇔','↑','↓'] },
      ]
    },
  };

  const insertChar = (subId: string, char: string) => {
    const el = inputRefs.current[subId];
    if (!el) {
      handleAnswerChange(subId, (answers[subId] || '') + char);
      return;
    }
    const start = el.selectionStart ?? el.value.length;
    const end = el.selectionEnd ?? start;
    const val = el.value;
    const newVal = val.slice(0, start) + char + val.slice(end);
    handleAnswerChange(subId, newVal);
    requestAnimationFrame(() => {
      el.focus();
      el.setSelectionRange(start + char.length, start + char.length);
    });
  };

  // OCR: Image to text via Gemini Vision
  const [ocrLoading, setOcrLoading] = useState<Record<string, boolean>>({});
  const handleOcr = async (subId: string) => {
    const input = document.createElement('input');
    input.type = 'file'; input.accept = 'image/*';
    input.onchange = async (e: any) => {
      const file = e.target.files?.[0];
      if (!file) return;
      setOcrLoading(prev => ({...prev, [subId]: true}));
      try {
        const reader = new FileReader();
        reader.onload = async (ev) => {
          const base64 = (ev.target?.result as string);
          const { data, error } = await supabase.functions.invoke('igcse-grader', {
            body: { mode: 'ocr', image: base64 }
          });
          if (error) { alert((isEnRef.current ? 'OCR Error: ' : 'Lỗi OCR: ') + error.message); }
          else if (data?.text) {
            const current = answers[subId] || '';
            handleAnswerChange(subId, current ? current + '\n' + data.text : data.text);
          }
          setOcrLoading(prev => ({...prev, [subId]: false}));
        };
        reader.readAsDataURL(file);
      } catch(err) {
        alert(isEnRef.current ? 'OCR Error' : 'Lỗi OCR'); setOcrLoading(prev => ({...prev, [subId]: false}));
      }
    };
    input.click();
  };

  // Submit and grade via edge function
  const handleSubmit = async (forceAutoSubmit: any = false) => {
    const isForced = forceAutoSubmit === true;
    if (isFinishingRef.current || isSubmitting) return;
    const currentAnswers = answersRef.current;
    const isExercise = testData?.content_json?.basicInfo?.category === 'exercise';
    if (!isForced && Object.keys(currentAnswers).length === 0) {
      alert(isEn ? "⚠️ You haven't entered any answers yet!" : "⚠️ Bạn chưa điền câu trả lời nào cả!"); return;
    }
    if (!isForced) {
      if (!isExercise && timeLeft > 0 && !window.confirm(isEn ? "Are you sure you want to submit the exam?" : "Bạn có chắc chắn muốn nộp bài thi?")) { return; }
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
      const compressImage = (base64Str: string, maxWidth = 800, quality = 0.5): Promise<string> => {
          return new Promise((resolve) => {
              const img = new Image();
              img.onload = () => {
                  const canvas = document.createElement('canvas');
                  let scaleFactor = 1;
                  if (img.width > maxWidth) scaleFactor = maxWidth / img.width;
                  canvas.width = img.width * scaleFactor;
                  canvas.height = img.height * scaleFactor;
                  const ctx = canvas.getContext('2d');
                  ctx?.drawImage(img, 0, 0, canvas.width, canvas.height);
                  resolve(canvas.toDataURL('image/jpeg', quality));
              };
              img.src = base64Str;
          });
      };

      // Separate image answers from text answers
      const imageAnswers: { questionId: string, base64: string }[] = [];
      const textAnswers: Record<string, string> = {};

      for (const [key, val] of Object.entries(currentAnswers)) {
          if (val && typeof val === 'string' && val.startsWith('data:image')) {
              const compressedBase64 = await compressImage(val);
              imageAnswers.push({ questionId: key, base64: compressedBase64 });
              textAnswers[key] = isEn
                ? "[STUDENT UPLOADED A DRAWING IMAGE - PLEASE VIEW IN THE ATTACHMENTS]"
                : "[HỌC SINH ĐÃ CHỤP ẢNH BẢN VẼ - HÃY XEM TRONG PHẦN ĐÍNH KÈM]";
          } else {
              textAnswers[key] = val;
          }
      }

      // Call IGCSE grading edge function
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
              const cleanJson = (data.result || data.rawText || "").replace(/```json/gi, "").replace(/```/gi, "").trim();
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

      // Save to database
      try {
        const { data: { user } } = await supabase.auth.getUser();
        if (user) {
          await supabase.from('test_results').insert([{
            user_id: user.id, course_id: testData.course_id, test_title: testData.title || "IGCSE Paper",
            test_type: 'IGCSE-Science', score: gradedData.total_student_score, total_score: gradedData.total_max_score,
            time_spent: computedTimeSpent,
            details: { test_id: testData.id, userAnswers: currentAnswers, aiFeedback: gradedData }
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

      // Chỉ xóa bản nháp sau khi chấm & lưu thành công
      if (testData?.id) {
         localStorage.removeItem(`igcse_endtime_${testData.id}`);
         localStorage.removeItem(`igcse_ans_${testData.id}`);
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

  // Timer countdown
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

  // Drag resize handler
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent | TouchEvent) => {
      if (!isDragging || !containerRef.current) return;
      const clientX = 'touches' in e ? e.touches[0]?.clientX : e.clientX;
      if (clientX === undefined) return;
      const containerWidth = containerRef.current.getBoundingClientRect().width;
      const newLeftWidth = (clientX / containerWidth) * 100;
      if (newLeftWidth > 20 && newLeftWidth < 80) setLeftWidth(newLeftWidth);
    };
    const handleMouseUp = () => setIsDragging(false);
    if (isDragging) { 
        document.addEventListener('mousemove', handleMouseMove); 
        document.addEventListener('mouseup', handleMouseUp); 
        document.addEventListener('touchmove', handleMouseMove, { passive: false }); 
        document.addEventListener('touchend', handleMouseUp); 
    }
    return () => { 
        document.removeEventListener('mousemove', handleMouseMove); 
        document.removeEventListener('mouseup', handleMouseUp); 
        document.removeEventListener('touchmove', handleMouseMove); 
        document.removeEventListener('touchend', handleMouseUp); 
    };
  }, [isDragging]);

  // Call AI Tutor for wrong answers
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

  // Answered count for progress
  const allSubQuestions = useMemo(() => {
    if (!testData?.json_config?.questions) return [];
    return testData.json_config.questions.flatMap((q: any) => q.sub_questions || []);
  }, [testData]);

  const answeredCount = useMemo(() => {
    return allSubQuestions.filter((sq: any) => answers[sq.id]?.trim()).length;
  }, [allSubQuestions, answers]);

  const hasRichPaper = useMemo(() => {
    const qs = testData?.json_config?.questions || [];
    return qs.some(
      (q: any) =>
        Boolean(q?.stem_html) ||
        (Array.isArray(q?.images) && q.images.length > 0) ||
        (q?.sub_questions || []).some(
          (s: any) => Boolean(s?.stem_html) || (Array.isArray(s?.images) && s.images.length > 0)
        )
    );
  }, [testData]);

  // Loading state
  if (isLoading) return (
    <div className="h-[100dvh] w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold">
      <div className="animate-spin text-4xl mb-4">⏳</div>
      <p>{isEn ? 'Loading IGCSE exam...' : 'Đang tải đề thi IGCSE...'}</p>
    </div>
  );

  // No test data
  if (!testData || (!isReviewMode && (!testData.json_config || !testData.json_config.questions))) return (
    <div className="h-[100dvh] w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold gap-4">
      <p>{isEn ? '⚠️ No exam configuration found in the system.' : '⚠️ Chưa có cấu hình đề thi trong hệ thống.'}</p>
      <button onClick={onBack} className="bg-[#1e88e5] px-6 py-2 rounded hover:bg-blue-700 transition-colors">{isEn ? 'Go Back' : 'Quay lại'}</button>
    </div>
  );

  const questions = testData.json_config.questions || [];
  const showPdfPane = !hasRichPaper || paperViewMode === 'split';
  const cleanRichLabel = (label: string) =>
    hasRichPaper ? String(label || '').replace(/\s*\[(Hình Ảnh|Table)\]/gi, '').trim() : String(label || '');
  const renderRichImages = (images?: Array<{ url: string; caption?: string; max_width?: number }>) => {
    if (!Array.isArray(images) || images.length === 0) return null;
    return (
      <div className={`grid gap-3 my-3 ${images.length > 1 ? 'grid-cols-1' : 'grid-cols-1'}`}>
        {images.map((img, idx) => (
          <figure
            key={`${img.url}-${idx}`}
            className="group bg-white border border-slate-200 rounded-xl p-3 sm:p-4 shadow-xs hover:border-sky-300 hover:shadow-md transition-all text-center"
          >
            <img
              src={img.url}
              alt={img.caption || 'Cambridge exam figure'}
              title={isEn ? 'Click to enlarge figure' : 'Bấm để phóng to hình'}
              loading="lazy"
              style={img.max_width ? { maxWidth: `${img.max_width}px` } : undefined}
              className="w-full h-auto mx-auto object-contain cursor-zoom-in rounded"
            />
            {img.caption && (
              <figcaption className="mt-2 text-[12.5px] font-semibold text-slate-600 flex items-center justify-center gap-1.5 flex-wrap">
                <span>{img.caption}</span>
                <span className="text-[11px] font-medium text-sky-600 opacity-75 group-hover:opacity-100">
                  🔍 {isEn ? 'Zoom' : 'Phóng to'}
                </span>
              </figcaption>
            )}
          </figure>
        ))}
      </div>
    );
  };
  const calcPolicy = detectCalculatorPolicy(testData?.title, testData?.content_json?.basicInfo);
  const mathSyllabus = detectIgcseMathSyllabus(testData?.title, testData?.course_id || testData?.content_json?.basicInfo?.courseId);

  const handleContainerScroll = (e: React.UIEvent<HTMLDivElement>) => {
      const el = e.currentTarget;
      if (el.scrollTop <= 0) el.scrollTop = 1;
      else if (el.scrollTop + el.clientHeight >= el.scrollHeight) el.scrollTop -= 1;
  };

  return (
    <div className="h-[100dvh] w-screen flex flex-col bg-white font-sans text-slate-900 overflow-hidden">
      <style>{`
        .igcse-rich-stem { font-size: 14.5px; line-height: 1.65; color: #1e293b; }
        .igcse-rich-stem p { margin: 0 0 0.55rem 0; }
        .igcse-rich-stem p:last-child { margin-bottom: 0; }
        .igcse-rich-stem ul { list-style: disc; padding-left: 1.35rem; margin: 0.4rem 0 0.6rem 0; }
        .igcse-rich-stem li { margin-bottom: 0.25rem; }
        .igcse-table-wrap { overflow-x: auto; margin: 0.75rem 0; }
        .igcse-table-title { text-align: center; font-weight: 800; font-size: 13px; color: #0f172a; margin-bottom: 0.35rem; letter-spacing: 0.01em; }
        .igcse-table { width: auto; min-width: min(100%, 360px); margin: 0 auto; border-collapse: collapse; background: #ffffff; font-size: 13.5px; }
        .igcse-table th, .igcse-table td { border: 1px solid #94a3b8; padding: 0.45rem 0.85rem; text-align: center; vertical-align: middle; }
        .igcse-table th { background: #f1f5f9; font-weight: 700; color: #0f172a; }
        .igcse-table td.igcse-shaded { background: #cbd5e1; }
        .igcse-eq-box { margin: 0.75rem auto; max-width: 440px; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; padding: 0.75rem 1rem; text-align: center; }
        .igcse-eq-main { font-size: 16px; font-weight: 700; color: #0f172a; letter-spacing: 0.01em; }
        .igcse-eq-sub { display: flex; justify-content: space-between; gap: 1rem; max-width: 300px; margin: 0.45rem auto 0; font-size: 12px; color: #475569; line-height: 1.3; }
        .igcse-nuclide-box { display: flex; justify-content: center; margin: 0.6rem 0; }
        .igcse-nuclide { display: inline-flex; align-items: center; gap: 3px; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; padding: 0.4rem 1rem; font-family: Georgia, 'Times New Roman', serif; }
        .igcse-nuclide-nums { display: inline-flex; flex-direction: column; align-items: flex-end; font-size: 13px; font-weight: 700; line-height: 1.1; color: #0f172a; }
        .igcse-nuclide-sym { font-size: 24px; font-weight: 700; color: #0f172a; line-height: 1; }
        .igcse-quote-box { background: #ffffff; border: 1px solid #cbd5e1; border-left: 4px solid #0a5482; border-radius: 8px; padding: 0.75rem 1rem; margin: 0.5rem 0; font-size: 14px; line-height: 1.75; color: #0f172a; }
      `}</style>
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
            {!isReviewMode && (
              <span className="text-xs text-slate-400 whitespace-nowrap hidden xs:inline">({answeredCount}/{allSubQuestions.length} {isEn ? 'questions' : 'câu'})</span>
            )}
          </div>
        </div>
        <div className="flex items-center gap-2 sm:gap-3 shrink-0">
          {hasRichPaper && (
            <div className="inline-flex items-center bg-slate-100 p-0.5 rounded-lg border border-slate-200 shrink-0" role="group" aria-label={isEn ? 'Paper view mode' : 'Chế độ xem đề'}>
              <button
                type="button"
                onClick={() => setPaperViewMode('split')}
                className={`px-2 sm:px-2.5 py-1 rounded-md text-[11px] sm:text-xs font-bold transition-all whitespace-nowrap cursor-pointer ${paperViewMode === 'split' ? 'bg-white text-[#0a5482] shadow-xs' : 'text-slate-600 hover:text-slate-900'}`}
                title={isEn ? 'Show original PDF on the left alongside Text & Figures' : 'Xem song song PDF bên trái và Đề Text + Hình bên phải'}
              >
                📄|📝 <span className="hidden md:inline">{isEn ? 'Split PDF' : 'Song song'}</span>
              </button>
              <button
                type="button"
                onClick={() => setPaperViewMode('text-only')}
                className={`px-2 sm:px-2.5 py-1 rounded-md text-[11px] sm:text-xs font-bold transition-all whitespace-nowrap cursor-pointer ${paperViewMode === 'text-only' ? 'bg-[#0a5482] text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'}`}
                title={isEn ? 'Hide left PDF and work directly on Text + Figures paper' : 'Ẩn PDF bên trái — Chỉ làm trực tiếp trên bản Text + Hình'}
              >
                📝 <span className="hidden md:inline">{isEn ? 'Text + Figures' : 'Chỉ Text + Hình'}</span>
              </button>
            </div>
          )}
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
               <button type="button" onClick={() => handleSubmit(false)} disabled={isSubmitting} className="bg-[#0a5482] hover:bg-[#084266] text-white font-bold text-xs sm:text-sm px-4 sm:px-6 py-1.5 rounded-lg transition-colors active:scale-95 disabled:opacity-50 whitespace-nowrap shadow-sm cursor-pointer">
                 {isSubmitting ? (isEn ? 'Grading...' : 'Đang chấm...') : (isEn ? 'Submit' : 'Nộp Bài')}
               </button>
            </>
          )}
        </div>
      </header>

      {/* Submitting overlay */}
      {isSubmitting && (
        <div className="fixed inset-0 z-50 bg-slate-900/70 backdrop-blur-sm flex flex-col items-center justify-center text-white">
          <div className="w-16 h-16 border-4 border-white/30 border-t-white rounded-full animate-spin mb-6"></div>
          <p className="text-xl font-bold mb-2">🧠 {isEn ? 'AI is grading your paper...' : 'AI đang chấm bài...'}</p>
          <p className="text-sm text-slate-300">{isEn ? 'Gemini Vision is analyzing your answers and drawings' : 'Gemini Vision đang phân tích bài làm và hình vẽ của bạn'}</p>
        </div>
      )}

      {/* Split Screen */}
      <div ref={containerRef} className={`flex-1 flex flex-col md:flex-row overflow-hidden w-full bg-[#525659] ${isDragging ? 'select-none' : ''}`}>
        {/* Left: PDF Viewer with Drawing Canvas */}
        {showPdfPane && (
        <div style={{ width: isDesktop ? `${leftWidth}%` : '100%' }} className="h-[46vh] md:h-full flex flex-col shrink-0 bg-[#525659] border-b md:border-b-0 border-slate-700">
          <div className="bg-[#323639] border-b border-[#202224] px-3 sm:px-4 flex justify-between items-center gap-2 h-10 shrink-0 shadow-sm overflow-x-auto no-scrollbar">
            <div className="flex items-center gap-2 shrink-0">
              <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest shrink-0">📄 {isEn ? 'Cambridge Exam Paper' : 'Đề thi Cambridge'}</span>
              {testData.insert_pdf_url && (
                <a
                  href={testData.insert_pdf_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-2 py-0.5 rounded bg-white/10 hover:bg-white/20 text-slate-200 hover:text-white text-[11px] font-bold transition whitespace-nowrap"
                  title={isEn ? 'Open PDF in a new tab' : 'Mở file PDF trong tab mới'}
                >
                  ↗ {isEn ? 'Open PDF' : 'Mở PDF'}
                </a>
              )}
            </div>
            {!isReviewMode && (
              <div className="flex items-center gap-1 shrink-0">
                <button onClick={() => setDrawMode(prev => prev === 'pen' ? null : 'pen')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'pen' ? 'bg-[#0a5482] text-white' : 'text-slate-400 hover:text-white'}`} title={isEn ? 'Pen' : 'Bút vẽ'}>✏️</button>
                <button onClick={() => setDrawMode(prev => prev === 'line' ? null : 'line')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'line' ? 'bg-[#0a5482] text-white' : 'text-slate-400 hover:text-white'}`} title={isEn ? 'Straight line' : 'Đường thẳng'}>📏</button>
                <button onClick={() => setDrawMode(prev => prev === 'rect' ? null : 'rect')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'rect' ? 'bg-[#0a5482] text-white' : 'text-slate-400 hover:text-white'}`} title={isEn ? 'Rectangle' : 'Hình chữ nhật'}>▬</button>
                <button onClick={() => setDrawMode(prev => prev === 'circle' ? null : 'circle')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'circle' ? 'bg-[#0a5482] text-white' : 'text-slate-400 hover:text-white'}`} title={isEn ? 'Ellipse' : 'Hình elip'}>⬭</button>
                <button onClick={() => setDrawMode(prev => prev === 'triangle' ? null : 'triangle')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'triangle' ? 'bg-[#0a5482] text-white' : 'text-slate-400 hover:text-white'}`} title={isEn ? 'Triangle' : 'Tam giác'}>△</button>
                <button onClick={() => setDrawMode(prev => prev === 'text' ? null : 'text')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'text' ? 'bg-[#0a5482] text-white' : 'text-slate-400 hover:text-white'}`} title={isEn ? 'Text' : 'Chữ'}>T</button>
                <button onClick={() => setDrawMode(prev => prev === 'eraser' ? null : 'eraser')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'eraser' ? 'bg-orange-500 text-white' : 'text-slate-400 hover:text-white'}`} title={isEn ? 'Eraser' : 'Tẩy'}>🧹</button>
                {drawMode && (
                  <>
                    <div className="w-px h-4 bg-slate-600 mx-1"></div>
                    {['#ff3333','#2ab4e8','#22c55e','#f59e0b','#ffffff'].map(c => (
                      <button key={c} onClick={() => setPenColor(c)} className={`w-5 h-5 rounded-full border-2 transition-transform shrink-0 ${penColor === c ? 'border-white scale-110' : 'border-slate-600'}`} style={{ backgroundColor: c }} />
                    ))}
                    <div className="w-px h-4 bg-slate-600 mx-1"></div>
                    <button onClick={() => { const cv = drawCanvasRef.current; if (cv) { const ctx = cv.getContext('2d'); ctx?.clearRect(0,0,cv.width,cv.height); } }} className="px-2 py-1 rounded text-[11px] text-slate-400 hover:text-red-400 font-bold" title={isEn ? 'Clear all' : 'Xóa tất cả'}>🗑️</button>
                  </>
                )}
              </div>
            )}
          </div>
          <div onScroll={handleContainerScroll} className={`flex-1 w-full h-full relative ${isDragging ? 'pointer-events-none' : ''} overflow-auto custom-scrollbar`}>
             {testData.insert_pdf_url ? (
               <iframe src={`${testData.insert_pdf_url}#toolbar=0&navpanes=0&scrollbar=0&view=FitH`} className="w-full h-full border-none bg-transparent" title="PDF Paper" />
             ) : (
               <div className="flex flex-col items-center justify-center h-full text-slate-400 p-8 text-center bg-[#525659]">
                 <span className="text-5xl mb-4">📄</span>
                 <p className="font-bold">{isEn ? 'No exam PDF file available.' : 'Không có file PDF đề thi.'}</p>
                 <p className="text-sm mt-2">{isEn ? 'No PDF has been uploaded for this exam yet.' : 'Admin chưa upload PDF cho đề này.'}</p>
               </div>
             )}
             {/* Drawing overlay canvas */}
             {(true) && (
               <>
                 <canvas
                   ref={drawCanvasRef}
                   className={`absolute inset-0 w-full h-full ${!drawMode ? 'pointer-events-none' : ''}`}
                   style={{ cursor: drawMode === 'text' ? 'text' : drawMode === 'eraser' ? 'cell' : drawMode ? 'crosshair' : 'auto', touchAction: drawMode ? 'none' : 'auto', zIndex: 10 }}
                   onPointerDown={(e) => {
                     if (!drawMode) return;
                     e.preventDefault();
                     const cv = drawCanvasRef.current; if (!cv) return;
                     const ctx = cv.getContext('2d'); if (!ctx) return;
                     const rect = e.currentTarget.getBoundingClientRect();
                     const x = e.clientX - rect.left, y = e.clientY - rect.top;
                     
                     if (drawMode === 'text') {
                       setTextPos({x, y}); setDrawText('');
                       return;
                     }
                     try { e.currentTarget.setPointerCapture(e.pointerId); } catch {}
                     setIsDrawing(true);
                     if (['line','rect','circle','triangle'].includes(drawMode)) {
                       setShapeStart({x, y});
                       canvasSnapshot.current = ctx.getImageData(0, 0, cv.width, cv.height);
                     } else {
                       ctx.beginPath(); ctx.moveTo(x, y);
                     }
                   }}
                   onPointerMove={(e) => {
                     if (!isDrawing || !drawMode) return;
                     e.preventDefault();
                     const cv = drawCanvasRef.current; if (!cv) return;
                     const ctx = cv.getContext('2d'); if (!ctx) return;
                     const rect = e.currentTarget.getBoundingClientRect();
                     const x = e.clientX - rect.left, y = e.clientY - rect.top;
                     
                     if (['line','rect','circle','triangle'].includes(drawMode) && shapeStart && canvasSnapshot.current) {
                       ctx.putImageData(canvasSnapshot.current, 0, 0);
                       ctx.strokeStyle = penColor; ctx.lineWidth = 2; ctx.lineCap = 'round';
                       ctx.globalCompositeOperation = 'source-over';
                       ctx.beginPath();
                       if (drawMode === 'line') { ctx.moveTo(shapeStart.x, shapeStart.y); ctx.lineTo(x, y); }
                       else if (drawMode === 'rect') { ctx.rect(shapeStart.x, shapeStart.y, x - shapeStart.x, y - shapeStart.y); }
                       else if (drawMode === 'circle') { const rx = Math.abs(x-shapeStart.x)/2, ry = Math.abs(y-shapeStart.y)/2; ctx.ellipse(shapeStart.x+(x-shapeStart.x)/2, shapeStart.y+(y-shapeStart.y)/2, rx, ry, 0, 0, Math.PI*2); }
                       else if (drawMode === 'triangle') { ctx.moveTo(shapeStart.x+(x-shapeStart.x)/2, shapeStart.y); ctx.lineTo(x, y); ctx.lineTo(shapeStart.x, y); ctx.closePath(); }
                       ctx.stroke();
                     } else if (drawMode === 'pen' || drawMode === 'eraser') {
                       ctx.strokeStyle = drawMode === 'eraser' ? 'rgba(0,0,0,1)' : penColor;
                       ctx.lineWidth = drawMode === 'eraser' ? 20 : 2;
                       ctx.lineCap = 'round';
                       ctx.globalCompositeOperation = drawMode === 'eraser' ? 'destination-out' : 'source-over';
                       ctx.lineTo(x, y); ctx.stroke();
                     }
                   }}
                   onPointerUp={(e) => { try { e.currentTarget.releasePointerCapture(e.pointerId); } catch {} setIsDrawing(false); setShapeStart(null); canvasSnapshot.current = null; }}
                   onPointerCancel={() => { setIsDrawing(false); setShapeStart(null); canvasSnapshot.current = null; }}
                   onPointerLeave={() => { setIsDrawing(false); setShapeStart(null); canvasSnapshot.current = null; }}
                 />
                 {/* Text input overlay */}
                 {drawMode === 'text' && textPos && (
                   <input
                     autoFocus
                     value={drawText}
                     onChange={e => setDrawText(e.target.value)}
                     onKeyDown={e => {
                       if (e.key === 'Enter' && drawText) {
                         const ctx = drawCanvasRef.current?.getContext('2d');
                         if (ctx) { ctx.globalCompositeOperation = 'source-over'; ctx.font = 'bold 16px sans-serif'; ctx.fillStyle = penColor; ctx.fillText(drawText, textPos.x, textPos.y); }
                         setTextPos(null); setDrawText('');
                       } else if (e.key === 'Escape') { setTextPos(null); setDrawText(''); }
                     }}
                     className="absolute bg-white/90 border-2 border-[#1e88e5] rounded px-2 py-1 text-[14px] outline-none min-w-[120px]"
                     style={{ left: textPos.x, top: textPos.y, zIndex: 20 }}
                     placeholder={isEn ? 'Type text and press Enter...' : 'Gõ text rồi Enter...'}
                   />
                 )}
               </>
             )}
          </div>
        </div>
        )}

        {/* Drag Handle (Desktop only) */}
        {showPdfPane && (
        <div onMouseDown={() => setIsDragging(true)} onTouchStart={() => setIsDragging(true)} className={`hidden md:flex w-[6px] h-full bg-[#202224] hover:bg-[#2ab4e8] cursor-col-resize items-center justify-center shrink-0 z-10 transition-colors ${isDragging ? 'bg-[#2ab4e8]' : ''}`}>
          <div className="flex flex-col gap-1"><div className="w-[2px] h-[2px] bg-slate-500"></div><div className="w-[2px] h-[2px] bg-slate-500"></div><div className="w-[2px] h-[2px] bg-slate-500"></div></div>
        </div>
        )}

        {/* Right: Answer Sheet (+ Rich Exam Text & Figures when enabled) */}
        <div style={{ width: isDesktop ? (showPdfPane ? `calc(${100 - leftWidth}% - 6px)` : '100%') : '100%' }} className="flex-1 md:flex-none md:h-full min-h-0 flex flex-col shrink-0 bg-[#f8fafc]">
          <div className="bg-[#323639] border-b border-[#202224] px-4 sm:px-6 flex justify-between items-center h-10 shrink-0 shadow-sm gap-2">
            <div className="flex items-center gap-2 min-w-0">
              <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest flex items-center gap-2 truncate">
                {gradeResult
                  ? <><span>✅</span> {isEn ? 'IGCSE Grading Results' : 'Kết quả chấm điểm IGCSE'}</>
                  : hasRichPaper
                    ? <><span className="w-1.5 h-1.5 rounded-full bg-sky-400 animate-pulse shrink-0"></span> {isEn ? 'Structured Paper (Text + Figures)' : 'Đề Text + Hình & Phiếu trả lời'}</>
                    : <><span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse shrink-0"></span> {isEn ? 'Answer Sheet' : 'Answer Sheet (Phiếu trả lời)'}</>}
              </span>
              {hasRichPaper && !showPdfPane && testData.insert_pdf_url && (
                <a
                  href={testData.insert_pdf_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-2 py-0.5 rounded bg-white/10 hover:bg-white/20 text-slate-200 hover:text-white text-[11px] font-bold transition whitespace-nowrap shrink-0"
                  title={isEn ? 'Open original PDF in a new tab' : 'Mở file PDF gốc trong tab mới'}
                >
                  ↗ {isEn ? 'Original PDF' : 'PDF gốc'}
                </a>
              )}
            </div>

            {/* 🎬 NÚT BẬT / THÊM VIDEO HƯỚNG DẪN */}
            <TestGuideVideoButton
              videoUrl={guideVideoUrl}
              videos={guideVideos}
              isOpen={isGuideVideoOpen}
              onToggleOpen={() => setIsGuideVideoOpen(!isGuideVideoOpen)}
              onOpenEditModal={() => setIsGuideVideoEditModalOpen(true)}
              isReviewMode={isReviewMode || !!gradeResult}
              buttonTheme="dark"
            />
          </div>

          {/* Compact Question Jump Navigator for Rich Structured Papers */}
          {hasRichPaper && questions.length > 1 && (
            <div className="bg-white border-b border-slate-200 px-4 sm:px-6 py-2 flex items-center justify-between gap-3 shrink-0 overflow-x-auto no-scrollbar">
              <div className="flex items-center gap-1.5 shrink-0">
                <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider mr-1 hidden sm:inline">
                  {isEn ? 'Jump:' : 'Câu:'}
                </span>
                {questions.map((q: any, qIdx: number) => {
                  const subs = q.sub_questions || [];
                  const done = subs.filter((s: any) => answers[s.id]?.trim()).length;
                  const allDone = subs.length > 0 && done === subs.length;
                  const partial = done > 0 && done < subs.length;
                  return (
                    <button
                      key={`jump-${qIdx}`}
                      type="button"
                      onClick={() => {
                        const target = document.getElementById(`igcse-question-${qIdx}`);
                        target?.scrollIntoView({ behavior: 'smooth', block: 'start' });
                      }}
                      className={`px-2.5 py-1 rounded-md text-[12px] font-extrabold border transition-all cursor-pointer whitespace-nowrap ${
                        allDone
                          ? 'bg-emerald-50 text-emerald-700 border-emerald-300 hover:bg-emerald-100'
                          : partial
                            ? 'bg-sky-50 text-[#0a5482] border-sky-300 hover:bg-sky-100'
                            : 'bg-slate-50 text-slate-600 border-slate-200 hover:border-slate-400 hover:text-slate-900'
                      }`}
                      title={`Question ${q.question_number}${q.page_ref ? ` (PDF ${q.page_ref})` : ''} — ${done}/${subs.length}`}
                    >
                      Q{q.question_number}
                      {allDone && <span className="ml-1 text-[10px]">✓</span>}
                    </button>
                  );
                })}
              </div>
              <span className="hidden lg:inline-flex items-center gap-1 text-[11px] font-semibold text-sky-700 bg-sky-50 border border-sky-200 px-2.5 py-0.5 rounded-full whitespace-nowrap shrink-0">
                ✨ {isEn ? 'Interactive Text + Figures' : 'Đề Text + Hình (Thử nghiệm)'}
              </span>
            </div>
          )}

          {/* 🎬 INLINE VIDEO PLAYER (Right below header, stays visible while scrolling) */}
          <TestGuideVideoPlayer
            videoUrl={guideVideoUrl}
            videos={guideVideos}
            activeVideoIndex={activeGuideVideoIndex}
            onSelectVideo={setActiveGuideVideoIndex}
            isOpen={isGuideVideoOpen}
            onClose={() => setIsGuideVideoOpen(false)}
            isTheaterOpen={isGuideVideoTheaterOpen}
            onToggleTheater={setIsGuideVideoTheaterOpen}
            testTitle={testData?.title}
          />

          {/* 🎬 MODAL CÀI ĐẶT / UPLOAD VIDEO */}
          <TestGuideVideoEditModal
            isOpen={isGuideVideoEditModalOpen}
            onClose={() => setIsGuideVideoEditModalOpen(false)}
            initialUrl={guideVideoUrl}
            initialVideos={guideVideos}
            onSaveVideos={handleSaveGuideVideos}
            testTitle={testData?.title}
          />

          <div
            onScroll={handleContainerScroll}
            onClick={(e) => {
              const lb = extractLightboxFromClick(e, e.currentTarget);
              if (lb) setImageLightbox(lb);
            }}
            className={`flex-1 overflow-y-auto p-4 sm:p-8 ${isDragging ? 'pointer-events-none' : ''} custom-scrollbar`}
          >
            <div className={!showPdfPane ? 'max-w-4xl mx-auto' : ''}>
            {/* Score Summary */}
            {gradeResult && (
                <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 mb-8 text-center">
                    <h2 className="text-xl font-black text-slate-800 mb-2">Total Score</h2>
                    <div className="text-5xl font-black text-[#0a5482] mb-4 tabular-nums">
                        {gradeResult.total_student_score} <span className="text-2xl text-slate-400">/ {gradeResult.total_max_score}</span>
                    </div>
                    <div className="w-full bg-slate-200 rounded-full h-3 mb-4">
                      <div className="bg-gradient-to-r from-[#0a5482] via-[#2ab4e8] to-emerald-400 h-3 rounded-full transition-all" style={{ width: `${gradeResult.total_max_score > 0 ? Math.min(100, (gradeResult.total_student_score / gradeResult.total_max_score) * 100) : 0}%` }}></div>
                    </div>
                    <p className="text-[14px] text-slate-600 bg-slate-50 p-4 rounded-xl italic text-left">{gradeResult.general_feedback}</p>
                </div>
            )}

            {/* Questions */}
            <div className="space-y-8">
                {questions.map((q: any, qIdx: number) => {
                    const qTotalMarks = Math.round(((q.sub_questions || []).reduce((acc: number, s: any) => acc + (Number(s.max_marks) || 0), 0)) * 10) / 10;
                    return (
                    <div id={`igcse-question-${qIdx}`} key={qIdx} className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 sm:p-6 scroll-mt-4">
                        <div className="flex flex-wrap justify-between items-center gap-2 mb-5 border-b border-slate-100 pb-3.5">
                            <div className="flex items-center gap-2.5 flex-wrap">
                                <h3 className="font-black text-slate-800 text-[18px]">Question {q.question_number}</h3>
                                {q.page_ref && (
                                    <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-slate-100 text-slate-500 border border-slate-200 text-[11px] font-bold">
                                        📄 PDF {q.page_ref}
                                    </span>
                                )}
                            </div>
                            {qTotalMarks > 0 && (
                                <span className="text-[12px] font-bold text-[#0a5482] bg-sky-50 border border-sky-200 px-2.5 py-0.5 rounded-full whitespace-nowrap">
                                    [Total: {qTotalMarks} {qTotalMarks === 1 ? 'mark' : 'marks'}]
                                </span>
                            )}
                        </div>

                        {(q.stem_html || (Array.isArray(q.images) && q.images.length > 0)) && (
                            <div className="mb-6 bg-slate-50/80 border border-slate-200/80 rounded-xl p-4 sm:p-5">
                                {q.stem_html && (
                                    <div className="igcse-rich-stem" dangerouslySetInnerHTML={{ __html: q.stem_html }} />
                                )}
                                {renderRichImages(q.images)}
                            </div>
                        )}
                        
                        <div className="space-y-6">
                            {(q.sub_questions || []).map((sub: any) => {
                                const feedbackData = gradeResult?.details?.find((d:any) => d.id === sub.id);
                                const isCorrect = feedbackData?.student_score === sub.max_marks;
                                const isWrong = feedbackData && feedbackData?.student_score === 0;

                                return (
                                    <div key={sub.id} className={`p-4 rounded-lg border ${isReviewMode ? (isCorrect ? 'bg-emerald-50 border-emerald-200' : isWrong ? 'bg-red-50 border-red-200' : 'bg-orange-50 border-orange-200') : 'bg-slate-50 border-slate-200'}`}>
                                        {(sub.stem_html || (Array.isArray(sub.images) && sub.images.length > 0)) && (
                                            <div className="mb-3.5 pb-3 border-b border-slate-200/70">
                                                {sub.stem_html && (
                                                    <div className="igcse-rich-stem" dangerouslySetInnerHTML={{ __html: sub.stem_html }} />
                                                )}
                                                {renderRichImages(sub.images)}
                                            </div>
                                        )}
                                        <div className="flex justify-between items-start gap-3 mb-3">
                                            <label className="font-semibold text-slate-800 text-[14px] leading-relaxed whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: renderLatex(cleanRichLabel(sub.label)) }} />
                                            <div className="flex items-center gap-1.5 shrink-0">
                                                {sub.unit && sub.type === 'long_answer' && (
                                                    <span className="px-2 py-0.5 rounded bg-sky-50 text-[#0a5482] border border-sky-200 text-[11px] font-bold whitespace-nowrap">
                                                        {isEn ? 'Unit:' : 'Đơn vị:'} {sub.unit}
                                                    </span>
                                                )}
                                                <span className="font-bold text-slate-400 text-[12px] whitespace-nowrap">[{sub.max_marks} {Number(sub.max_marks) === 1 ? 'mark' : 'marks'}]</span>
                                            </div>
                                        </div>

                                        {/* Render input by question type */}
                                        {sub.type === 'short_answer' ? (
                                            <div className="relative">
                                                <div className="flex items-center gap-2">
                                                    <input ref={(el) => { inputRefs.current[sub.id] = el; }} type="text" value={answers[sub.id] || ''} onChange={(e) => handleAnswerChange(sub.id, e.target.value)} disabled={isReviewMode} placeholder={isEn ? 'Enter short answer...' : 'Điền đáp án ngắn...'} className={`w-full max-w-sm px-4 py-2 border rounded-md text-[14px] outline-none transition-all ${isReviewMode ? 'bg-white border-slate-300' : 'bg-white focus:border-[#1e88e5] focus:ring-1 focus:ring-[#1e88e5]'}`}/>
                                                    {sub.unit && (
                                                        <span className="shrink-0 px-2.5 py-2 rounded-md bg-slate-100 border border-slate-200 text-slate-700 text-[13px] font-extrabold whitespace-nowrap">
                                                            {sub.unit}
                                                        </span>
                                                    )}
                                                    {!isReviewMode && (
                                                        <button type="button" onClick={() => setShowPalette(prev => ({...prev, [sub.id]: !prev[sub.id]}))} className={`shrink-0 px-2.5 py-1.5 rounded-md text-[12px] font-bold border transition-all ${showPalette[sub.id] ? 'bg-[#1e88e5] text-white border-[#1e88e5]' : 'bg-white text-slate-500 border-slate-300 hover:border-[#1e88e5] hover:text-[#1e88e5]'}`} title={isEn ? 'Formula symbol palette' : 'Bảng ký tự công thức'}>
                                                            f<sub>x</sub>
                                                        </button>
                                                    )}
                                                    {!isReviewMode && (
                                                      <button type="button" onClick={() => handleOcr(sub.id)} disabled={ocrLoading[sub.id]} className="shrink-0 px-2.5 py-1.5 rounded-md text-[12px] font-bold border transition-all bg-white text-slate-500 border-slate-300 hover:border-emerald-500 hover:text-emerald-600 disabled:opacity-50" title={isEn ? 'Upload photo of your work → AI converts to text' : 'Chụp ảnh bài làm → AI chuyển thành text'}>
                                                        {ocrLoading[sub.id] ? '⏳' : '📷'}
                                                      </button>
                                                    )}
                                                </div>
                                                {showPalette[sub.id] && !isReviewMode && (
                                                    <div className="absolute z-30 top-full mt-1 left-0 bg-white border border-slate-200 rounded-xl shadow-xl p-0 w-[min(380px,calc(100vw-2rem))] overflow-hidden">
                                                        <div className="flex border-b border-slate-200 bg-slate-50">
                                                            {(Object.keys(charTabs) as Array<keyof typeof charTabs>).map(k => (
                                                                <button key={k} type="button" onClick={() => setPaletteTab(k)} className={`flex-1 px-2 py-2 text-[11px] font-bold transition-all ${paletteTab === k ? 'text-[#1e88e5] border-b-2 border-[#1e88e5] bg-white' : 'text-slate-500 hover:text-slate-700'}`}>{charTabs[k].label}</button>
                                                            ))}
                                                        </div>
                                                        <div className="p-3">
                                                            {charTabs[paletteTab].groups.map((group, gi) => (
                                                                <div key={gi} className="mb-2 last:mb-0">
                                                                    <div className="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">{group.label}</div>
                                                                    <div className="flex flex-wrap gap-1">
                                                                        {group.chars.map(c => (
                                                                            <button key={c} type="button" onClick={() => insertChar(sub.id, c)} className="w-8 h-8 flex items-center justify-center rounded border border-slate-200 bg-slate-50 hover:bg-[#1e88e5] hover:text-white hover:border-[#1e88e5] text-[14px] font-medium transition-all active:scale-90">{c}</button>
                                                                        ))}
                                                                    </div>
                                                                </div>
                                                            ))}
                                                        </div>
                                                    </div>
                                                )}
                                            </div>
                                        ) : sub.type === 'long_answer' ? (
                                            <div className="relative">
                                                <div className="flex items-start gap-2">
                                                    <textarea ref={(el) => { inputRefs.current[sub.id] = el; }} value={answers[sub.id] || ''} onChange={(e) => handleAnswerChange(sub.id, e.target.value)} disabled={isReviewMode} placeholder={isEn ? 'Write your detailed answer...' : 'Viết câu trả lời tự luận...'} className={`w-full px-4 py-3 border rounded-md min-h-[80px] text-[14px] outline-none transition-all resize-y ${isReviewMode ? 'bg-white border-slate-300' : 'bg-white focus:border-[#1e88e5] focus:ring-1 focus:ring-[#1e88e5]'}`}/>
                                                    {!isReviewMode && (
                                                        <button type="button" onClick={() => setShowPalette(prev => ({...prev, [sub.id]: !prev[sub.id]}))} className={`shrink-0 mt-1 px-2.5 py-1.5 rounded-md text-[12px] font-bold border transition-all ${showPalette[sub.id] ? 'bg-[#1e88e5] text-white border-[#1e88e5]' : 'bg-white text-slate-500 border-slate-300 hover:border-[#1e88e5] hover:text-[#1e88e5]'}`} title={isEn ? 'Formula symbol palette' : 'Bảng ký tự công thức'}>
                                                            f<sub>x</sub>
                                                        </button>
                                                    )}
                                                    {!isReviewMode && (
                                                      <button type="button" onClick={() => handleOcr(sub.id)} disabled={ocrLoading[sub.id]} className="shrink-0 mt-1 px-2.5 py-1.5 rounded-md text-[12px] font-bold border transition-all bg-white text-slate-500 border-slate-300 hover:border-emerald-500 hover:text-emerald-600 disabled:opacity-50" title={isEn ? 'Upload photo of your work → AI converts to text' : 'Chụp ảnh bài làm → AI chuyển thành text'}>
                                                        {ocrLoading[sub.id] ? '⏳' : '📷'}
                                                      </button>
                                                    )}
                                                </div>
                                                {showPalette[sub.id] && !isReviewMode && (
                                                    <div className="absolute z-30 top-full mt-1 left-0 bg-white border border-slate-200 rounded-xl shadow-xl p-0 w-[min(380px,calc(100vw-2rem))] overflow-hidden">
                                                        <div className="flex border-b border-slate-200 bg-slate-50">
                                                            {(Object.keys(charTabs) as Array<keyof typeof charTabs>).map(k => (
                                                                <button key={k} type="button" onClick={() => setPaletteTab(k)} className={`flex-1 px-2 py-2 text-[11px] font-bold transition-all ${paletteTab === k ? 'text-[#1e88e5] border-b-2 border-[#1e88e5] bg-white' : 'text-slate-500 hover:text-slate-700'}`}>{charTabs[k].label}</button>
                                                            ))}
                                                        </div>
                                                        <div className="p-3">
                                                            {charTabs[paletteTab].groups.map((group, gi) => (
                                                                <div key={gi} className="mb-2 last:mb-0">
                                                                    <div className="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">{group.label}</div>
                                                                    <div className="flex flex-wrap gap-1">
                                                                        {group.chars.map(c => (
                                                                            <button key={c} type="button" onClick={() => insertChar(sub.id, c)} className="w-8 h-8 flex items-center justify-center rounded border border-slate-200 bg-slate-50 hover:bg-[#1e88e5] hover:text-white hover:border-[#1e88e5] text-[14px] font-medium transition-all active:scale-90">{c}</button>
                                                                        ))}
                                                                    </div>
                                                                </div>
                                                            ))}
                                                        </div>
                                                    </div>
                                                )}
                                            </div>
                                        ) : (
                                            /* Image Upload type */
                                            <div className="w-full mt-2" tabIndex={0} onPaste={(e) => {
                                                if (isReviewMode) return;
                                                const items = e.clipboardData?.items;
                                                if (!items) return;
                                                for (let i = 0; i < items.length; i++) {
                                                    if (items[i].type.startsWith('image/')) {
                                                        e.preventDefault();
                                                        const file = items[i].getAsFile();
                                                        if (file) handleImageUpload(sub.id, file);
                                                        return;
                                                    }
                                                }
                                            }}>
                                                {answers[sub.id] ? (
                                                    <div className="relative inline-block border-2 border-slate-300 rounded-lg p-2 bg-white shadow-sm">
                                                        <img src={answers[sub.id]} alt={isEn ? 'Student work' : 'Bài làm'} title={isEn ? 'Click to enlarge' : 'Bấm để phóng to'} className="max-h-[250px] object-contain rounded cursor-zoom-in" />
                                                        {!isReviewMode && (
                                                            <button onClick={() => handleAnswerChange(sub.id, '')} className="absolute -top-3 -right-3 bg-red-500 text-white w-7 h-7 rounded-full shadow-md font-bold hover:scale-110 transition-transform">✕</button>
                                                        )}
                                                    </div>
                                                ) : (
                                                    <label className={`flex flex-col items-center justify-center w-full h-32 border-2 border-dashed border-slate-300 rounded-lg bg-white transition-colors ${!isReviewMode ? 'cursor-pointer hover:bg-sky-50 hover:border-sky-400' : 'opacity-50'}`}>
                                                        <div className="flex flex-col items-center justify-center pt-5 pb-6">
                                                            <span className="text-3xl mb-2">📸</span>
                                                            <p className="text-sm text-slate-500 font-semibold">{isEn ? 'Click to choose an image or press Ctrl+V to paste from clipboard' : 'Nhấn để chọn ảnh hoặc Ctrl+V để dán từ clipboard'}</p>
                                                            <p className="text-xs text-slate-400 mt-1">{isEn ? 'Images are automatically compressed to < 1MB' : 'Ảnh sẽ tự động nén nhỏ < 1MB'}</p>
                                                        </div>
                                                        <input type="file" className="hidden" accept="image/*" onChange={(e) => {
                                                            if(e.target.files && e.target.files[0]) handleImageUpload(sub.id, e.target.files[0]);
                                                        }} disabled={isReviewMode}/>
                                                    </label>
                                                )}
                                            </div>
                                        )}

                                        {/* Review feedback */}
                                        {isReviewMode && feedbackData && (
                                            <div className="mt-4 pt-4 border-t border-slate-200/60">
                                                <div className="flex justify-between items-center mb-2">
                                                    <span className={`font-bold text-[12px] uppercase tracking-wider px-2 py-1 rounded ${isCorrect ? 'bg-emerald-200 text-emerald-800' : isWrong ? 'bg-red-200 text-red-800' : 'bg-orange-200 text-orange-800'}`}>
                                                      {isEn ? 'Score' : 'Điểm đạt'}: {feedbackData.student_score} / {sub.max_marks}
                                                    </span>
                                                </div>
                                                <p className="text-[13px] text-slate-700 mt-2 mb-3"><span className="font-bold text-slate-900">{isEn ? 'Examiner Comment: ' : 'Nhận xét: '}</span> {feedbackData.examiner_comment}</p>
                                                <div className="bg-white p-3 rounded border border-slate-200 text-[13px]">
                                                    <span className="font-bold text-slate-500 uppercase text-[10px] tracking-widest block mb-1">{isEn ? 'Correct Answer (Cambridge MS):' : 'Đáp án đúng (Cambridge MS):'}</span>
                                                    <span className="font-medium text-emerald-600" dangerouslySetInnerHTML={{ __html: renderLatex(feedbackData.correct_answer || '') }} />
                                                </div>

                                                {!isCorrect && (
                                                    <div className="flex items-center gap-2 mt-4">
                                                        <button onClick={() => {
                                                            const query = isEn
                                                              ? `Question: "${latexToText(sub.label)}"\nStudent's answer: "${answers[sub.id] || 'Blank'}"\nCorrect answer: "${latexToText(feedbackData.correct_answer || '')}"\n\nPlease explain in English in detail why my answer is wrong and how to solve this question.`
                                                              : `Câu hỏi: "${latexToText(sub.label)}"\nĐáp án học sinh: "${answers[sub.id] || 'Bỏ trống'}"\nĐáp án đúng: "${latexToText(feedbackData.correct_answer || '')}"\n\nThầy giải thích chi tiết giúp em tại sao em sai ạ!`;
                                                            const subjectTask = (testData?.test_type || testData?.skill || '').includes('Math') ? 'math' : 'Science';
                                                            // Open AI Sidebar for text chat
                                                            const btn = document.createElement('button');
                                                            btn.className = 'btn-ai-trigger';
                                                            btn.setAttribute('data-topic', query);
                                                            btn.setAttribute('data-task', subjectTask);
                                                            document.body.appendChild(btn);
                                                            btn.click();
                                                            document.body.removeChild(btn);
                                                        }} className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-blue-500 to-cyan-500 text-white font-bold text-[12px] rounded-lg shadow-md hover:shadow-lg transition-all active:scale-95">
                                                            💬 {isEn ? 'Chat with AI Teacher' : 'Chat Thầy AI'}
                                                        </button>
                                                        <button onClick={() => callAiTutor(latexToText(sub.label), answers[sub.id] || (isEn ? "Blank" : "Bỏ trống"), latexToText(feedbackData.correct_answer || ''))} className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-amber-400 to-orange-400 text-white font-bold text-[12px] rounded-lg shadow-md hover:shadow-lg transition-all active:scale-95">
                                                            📞 {isEn ? 'Call AI Tutor' : 'Gọi Gia Sư'}
                                                        </button>
                                                    </div>
                                                )}
                                            </div>
                                        )}
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                    );
                })}
            </div>
            </div>
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
