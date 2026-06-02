import React, { useState, useRef, useEffect, useMemo } from 'react';
import { supabase } from './supabase';

export default function IgcsePaperTest({ onBack, onStartTest, testData: propTestData }: { onBack?: () => void, onStartTest?: any, testData?: any }) {
  const [testData, setTestData] = useState<any>(() => {
      let raw = propTestData;
      if (!raw) {
          const saved = sessionStorage.getItem('lms_current_test');
          raw = saved ? JSON.parse(saved) : null;
      }
      if (!raw) return null;
      // Normalize: ensure json_config.questions exists from either json_config or content_json
      if (!raw.json_config?.questions && raw.content_json?.questions) {
          raw.json_config = { ...(raw.json_config || {}), questions: raw.content_json.questions, timeLimit: raw.content_json?.basicInfo?.timeLimit || raw.json_config?.timeLimit || 120 };
      }
      return raw;
  });
  
  const [isLoading, setIsLoading] = useState(!testData);
  const initIsReview = !!testData?.isReview;
  const [isReviewMode, setIsReviewMode] = useState(initIsReview);

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
  const [isDragging, setIsDragging] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  // Drawing on PDF
  const [drawMode, setDrawMode] = useState<'pen'|'eraser'|'line'|'rect'|'circle'|'triangle'|'text'|null>(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [penColor, setPenColor] = useState('#ff3333');
  const drawCanvasRef = useRef<HTMLCanvasElement>(null);
  const [shapeStart, setShapeStart] = useState<{x:number,y:number}|null>(null);
  const canvasSnapshot = useRef<ImageData|null>(null);
  const [drawText, setDrawText] = useState('');
  const [textPos, setTextPos] = useState<{x:number,y:number}|null>(null);

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

  // Initialize timer
  useEffect(() => {
    if (testData && !isReviewMode) {
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
    if (!cv || !drawMode) return;
    const parent = cv.parentElement;
    if (!parent) return;
    const resize = () => { cv.width = parent.clientWidth; cv.height = parent.clientHeight; };
    resize();
    const ro = new ResizeObserver(resize);
    ro.observe(parent);
    return () => ro.disconnect();
  }, [drawMode, leftWidth]);

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

  // LaTeX → Unicode/HTML converter for question labels
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
  
  const charTabs = {
    sci: {
      label: '🧪 Science',
      groups: [
        { label: 'Chỉ số dưới', chars: ['₀','₁','₂','₃','₄','₅','₆','₇','₈','₉'] },
        { label: 'Chỉ số trên', chars: ['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹','⁺','⁻','ⁿ'] },
        { label: 'Hóa học & Vật lý', chars: ['→','⇌','Δ','°','±','×','÷','≈','≠','≤','≥','∞','α','β','γ','θ','λ','μ','Ω','π'] },
      ]
    },
    geo: {
      label: '📐 Hình học',
      groups: [
        { label: 'Hình học', chars: ['∠','△','⊥','∥','∼','≡','°'] },
        { label: 'Ký hiệu', chars: ['π','√','²','³','±','≈','≠','≤','≥','∞','→','⇒','⇔'] },
      ]
    },
    alg: {
      label: '📊 Đại số',
      groups: [
        { label: 'Chỉ số', chars: ['₀','₁','₂','₃','ₙ','⁰','¹','²','³','ⁿ','⁺','⁻'] },
        { label: 'Phép toán', chars: ['±','∓','×','÷','·','√','∛','≈','≠','≡','∝','≤','≥'] },
        { label: 'Cao cấp', chars: ['∫','Σ','∏','∂','∞','ℝ','ℤ','ℕ','|'] },
        { label: 'Lượng giác', chars: ['θ','α','β','γ','φ','π','°'] },
      ]
    },
    set: {
      label: '{ } Tập hợp',
      groups: [
        { label: 'Tập hợp', chars: ['∩','∪','⊂','⊆','⊃','⊇','∈','∉','∅'] },
        { label: 'Logic', chars: ['∀','∃','¬','∧','∨','⇒','⇔','∴','∵'] },
        { label: 'Mũi tên', chars: ['→','←','↔','⇒','⇐','⇔','↑','↓'] },
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
    input.type = 'file'; input.accept = 'image/*'; input.capture = 'environment';
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
          if (error) { alert('Lỗi OCR: ' + error.message); }
          else if (data?.text) {
            const current = answers[subId] || '';
            handleAnswerChange(subId, current ? current + '\n' + data.text : data.text);
          }
          setOcrLoading(prev => ({...prev, [subId]: false}));
        };
        reader.readAsDataURL(file);
      } catch(err) {
        alert('Lỗi OCR'); setOcrLoading(prev => ({...prev, [subId]: false}));
      }
    };
    input.click();
  };

  // Submit and grade via edge function
  const handleSubmit = async () => {
    const currentAnswers = answersRef.current;
    if (Object.keys(currentAnswers).length === 0 && timeLeft > 0) {
      alert("⚠️ Bạn chưa điền câu trả lời nào cả!"); return;
    }
    if (timeLeft > 0 && !window.confirm("Bạn có chắc chắn muốn nộp bài thi?")) { return; }

    setIsSubmitting(true);
    isFinishingRef.current = true;
    
    if (testData?.id) {
       localStorage.removeItem(`igcse_endtime_${testData.id}`);
       localStorage.removeItem(`igcse_ans_${testData.id}`);
    }

    try {
      // Separate image answers from text answers
      const imageAnswers: { questionId: string, base64: string }[] = [];
      const textAnswers: Record<string, string> = {};

      for (const [key, val] of Object.entries(currentAnswers)) {
          if (val.startsWith('data:image')) {
              imageAnswers.push({ questionId: key, base64: val });
              textAnswers[key] = "[HỌC SINH ĐÃ CHỤP ẢNH BẢN VẼ - HÃY XEM TRONG PHẦN ĐÍNH KÈM]";
          } else {
              textAnswers[key] = val;
          }
      }

      // Call IGCSE grading edge function
      const { data, error } = await supabase.functions.invoke('igcse-grader', {
        body: { 
            testConfig: testData.json_config?.questions || [],
            textAnswers: textAnswers,
            imageAnswers: imageAnswers
        }
      });

      if (error) throw new Error("Lỗi gọi Server: " + error.message);
      if (data?.error) throw new Error("Lỗi chấm điểm: " + data.error);
      
      const cleanJson = (data.result || "").replace(/```json/gi, "").replace(/```/gi, "").trim();
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

      // Save to database
      try {
        const { data: { user } } = await supabase.auth.getUser();
        if (user) {
          const rawTime = testData.json_config?.timeLimit || testData.timeLimit || testData.time_limit || 120;
          const initialSeconds = parseInt(rawTime) * 60;
          const timeSpentSecs = initialSeconds - timeLeft;
          
          await supabase.from('test_results').insert([{
            user_id: user.id, course_id: testData.course_id, test_title: testData.title || "IGCSE Paper",
            test_type: 'IGCSE-Science', score: gradedData.total_student_score, total_score: gradedData.total_max_score,
            time_spent: timeSpentSecs > 0 ? timeSpentSecs : 0,
            details: { test_id: testData.id, userAnswers: currentAnswers, aiFeedback: gradedData }
          }]);
        }
      } catch (dbError) { console.error("DB save error:", dbError); }

    } catch (err: any) {
      alert("❌ Có lỗi trong lúc chấm: " + err.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  // Timer countdown
  useEffect(() => {
    if (isLoading || !testData || gradeResult || isFinishingRef.current || isReviewMode) return;
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

  // Drag resize handler
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!isDragging || !containerRef.current) return;
      const containerWidth = containerRef.current.getBoundingClientRect().width;
      const newLeftWidth = (e.clientX / containerWidth) * 100;
      if (newLeftWidth > 20 && newLeftWidth < 80) setLeftWidth(newLeftWidth);
    };
    const handleMouseUp = () => setIsDragging(false);
    if (isDragging) { document.addEventListener('mousemove', handleMouseMove); document.addEventListener('mouseup', handleMouseUp); }
    return () => { document.removeEventListener('mousemove', handleMouseMove); document.removeEventListener('mouseup', handleMouseUp); };
  }, [isDragging]);

  // Call AI Tutor for wrong answers
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

  // Answered count for progress
  const allSubQuestions = useMemo(() => {
    if (!testData?.json_config?.questions) return [];
    return testData.json_config.questions.flatMap((q: any) => q.sub_questions || []);
  }, [testData]);

  const answeredCount = useMemo(() => {
    return allSubQuestions.filter((sq: any) => answers[sq.id]?.trim()).length;
  }, [allSubQuestions, answers]);

  // Loading state
  if (isLoading) return (
    <div className="h-screen w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold">
      <div className="animate-spin text-4xl mb-4">⏳</div>
      <p>Đang tải đề thi IGCSE...</p>
    </div>
  );

  // No test data
  if (!testData || (!isReviewMode && (!testData.json_config || !testData.json_config.questions))) return (
    <div className="h-screen w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold gap-4">
      <p>⚠️ Chưa có cấu hình đề thi trong hệ thống.</p>
      <button onClick={onBack} className="bg-[#1e88e5] px-6 py-2 rounded hover:bg-blue-700 transition-colors">Quay lại</button>
    </div>
  );

  const questions = testData.json_config.questions || [];

  const handleContainerScroll = (e: React.UIEvent<HTMLDivElement>) => {
      const el = e.currentTarget;
      if (el.scrollTop <= 0) el.scrollTop = 1;
      else if (el.scrollTop + el.clientHeight >= el.scrollHeight) el.scrollTop -= 1;
  };

  return (
    <div className="h-screen w-screen flex flex-col bg-white font-sans text-slate-900 overflow-hidden">
      {/* Header */}
      <header className="h-14 w-full bg-white border-b border-slate-300 flex items-center justify-between px-4 sm:px-6 shrink-0 z-20 box-border">
        <div className="flex items-center gap-3 sm:gap-4 overflow-hidden">
          <button onClick={onBack} className="text-slate-600 hover:text-black font-bold text-sm transition-colors whitespace-nowrap">← Quay lại</button>
          <div className="h-5 w-px bg-slate-300 hidden sm:block"></div>
          <div className="truncate flex items-baseline gap-2">
            <h1 className="font-bold text-black text-[15px] leading-tight truncate">{isReviewMode ? `[REVIEW] ${testData.title}` : testData.title}</h1>
            {!isReviewMode && (
              <span className="text-xs text-slate-400 whitespace-nowrap">({answeredCount}/{allSubQuestions.length} câu)</span>
            )}
          </div>
        </div>
        {!gradeResult && !isReviewMode && (
          <div className="flex items-center gap-2 sm:gap-4 shrink-0">
             <div className={`font-bold flex items-center gap-2 px-3 py-1 rounded ${timeLeft <= 300 ? 'text-red-600 bg-red-50 animate-pulse' : 'text-slate-600'}`}>
               <span>⏱️</span> <span className="hidden sm:inline font-mono tracking-widest">{formatTime(timeLeft)}</span>
             </div>
             <button onClick={() => { if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(()=>{}); else document.exitFullscreen(); }} className="text-slate-500 hover:text-black transition-colors text-lg px-1" title="Toàn màn hình">
               {document.fullscreenElement ? '🔲' : '⛶'}
             </button>
             <button onClick={handleSubmit} disabled={isSubmitting} className="bg-[#1e88e5] hover:bg-blue-700 text-white font-bold text-sm px-6 py-1.5 rounded transition-colors active:scale-95 disabled:opacity-50 whitespace-nowrap">
               {isSubmitting ? 'Đang chấm...' : 'Nộp Bài'}
             </button>
          </div>
        )}
      </header>

      {/* Submitting overlay */}
      {isSubmitting && (
        <div className="fixed inset-0 z-50 bg-slate-900/70 backdrop-blur-sm flex flex-col items-center justify-center text-white">
          <div className="w-16 h-16 border-4 border-white/30 border-t-white rounded-full animate-spin mb-6"></div>
          <p className="text-xl font-bold mb-2">🧠 AI đang chấm bài...</p>
          <p className="text-sm text-slate-300">Gemini Vision đang phân tích bài làm và hình vẽ của bạn</p>
        </div>
      )}

      {/* Split Screen */}
      <div ref={containerRef} className="flex-1 flex overflow-hidden w-full select-none bg-[#525659]">
        {/* Left: PDF Viewer with Drawing Canvas */}
        <div style={{ width: `${leftWidth}%` }} className="h-full flex flex-col shrink-0 bg-[#525659]">
          <div className="bg-[#323639] border-b border-[#202224] px-4 flex justify-between items-center h-10 shrink-0 shadow-sm">
            <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest">📄 Đề thi Cambridge</span>
            {!isReviewMode && (
              <div className="flex items-center gap-1">
                <button onClick={() => setDrawMode(prev => prev === 'pen' ? null : 'pen')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'pen' ? 'bg-[#1e88e5] text-white' : 'text-slate-400 hover:text-white'}`} title="Bút vẽ">✏️</button>
                <button onClick={() => setDrawMode(prev => prev === 'line' ? null : 'line')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'line' ? 'bg-[#1e88e5] text-white' : 'text-slate-400 hover:text-white'}`} title="Đường thẳng">📏</button>
                <button onClick={() => setDrawMode(prev => prev === 'rect' ? null : 'rect')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'rect' ? 'bg-[#1e88e5] text-white' : 'text-slate-400 hover:text-white'}`} title="Hình chữ nhật">▬</button>
                <button onClick={() => setDrawMode(prev => prev === 'circle' ? null : 'circle')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'circle' ? 'bg-[#1e88e5] text-white' : 'text-slate-400 hover:text-white'}`} title="Hình elip">⬭</button>
                <button onClick={() => setDrawMode(prev => prev === 'triangle' ? null : 'triangle')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'triangle' ? 'bg-[#1e88e5] text-white' : 'text-slate-400 hover:text-white'}`} title="Tam giác">△</button>
                <button onClick={() => setDrawMode(prev => prev === 'text' ? null : 'text')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'text' ? 'bg-[#1e88e5] text-white' : 'text-slate-400 hover:text-white'}`} title="Chữ">T</button>
                <button onClick={() => setDrawMode(prev => prev === 'eraser' ? null : 'eraser')} className={`px-2 py-1 rounded text-[11px] font-bold transition-all ${drawMode === 'eraser' ? 'bg-orange-500 text-white' : 'text-slate-400 hover:text-white'}`} title="Tẩy">🧹</button>
                {drawMode && (
                  <>
                    <div className="w-px h-4 bg-slate-600 mx-1"></div>
                    {['#ff3333','#1e88e5','#22c55e','#f59e0b','#ffffff'].map(c => (
                      <button key={c} onClick={() => setPenColor(c)} className={`w-5 h-5 rounded-full border-2 transition-transform ${penColor === c ? 'border-white scale-110' : 'border-slate-600'}`} style={{ backgroundColor: c }} />
                    ))}
                    <div className="w-px h-4 bg-slate-600 mx-1"></div>
                    <button onClick={() => { const cv = drawCanvasRef.current; if (cv) { const ctx = cv.getContext('2d'); ctx?.clearRect(0,0,cv.width,cv.height); } }} className="px-2 py-1 rounded text-[11px] text-slate-400 hover:text-red-400 font-bold" title="Xóa tất cả">🗑️</button>
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
                 <p className="font-bold">Không có file PDF đề thi.</p>
                 <p className="text-sm mt-2">Admin chưa upload PDF cho đề này.</p>
               </div>
             )}
             {/* Drawing overlay canvas */}
             {(drawMode) && (
               <>
                 <canvas
                   ref={drawCanvasRef}
                   className="absolute inset-0 w-full h-full"
                   style={{ cursor: drawMode === 'text' ? 'text' : drawMode === 'eraser' ? 'cell' : 'crosshair', zIndex: 10 }}
                   onMouseDown={(e) => {
                     const cv = drawCanvasRef.current; if (!cv) return;
                     const ctx = cv.getContext('2d'); if (!ctx) return;
                     const rect = e.currentTarget.getBoundingClientRect();
                     const x = e.clientX - rect.left, y = e.clientY - rect.top;
                     
                     if (drawMode === 'text') {
                       setTextPos({x, y}); setDrawText('');
                       return;
                     }
                     setIsDrawing(true);
                     if (['line','rect','circle','triangle'].includes(drawMode!)) {
                       setShapeStart({x, y});
                       canvasSnapshot.current = ctx.getImageData(0, 0, cv.width, cv.height);
                     } else {
                       ctx.beginPath(); ctx.moveTo(x, y);
                     }
                   }}
                   onMouseMove={(e) => {
                     if (!isDrawing) return;
                     const cv = drawCanvasRef.current; if (!cv) return;
                     const ctx = cv.getContext('2d'); if (!ctx) return;
                     const rect = e.currentTarget.getBoundingClientRect();
                     const x = e.clientX - rect.left, y = e.clientY - rect.top;
                     
                     if (['line','rect','circle','triangle'].includes(drawMode!) && shapeStart && canvasSnapshot.current) {
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
                       ctx.strokeStyle = drawMode === 'eraser' ? 'rgba(0,0,0,0)' : penColor;
                       ctx.lineWidth = drawMode === 'eraser' ? 20 : 2;
                       ctx.lineCap = 'round';
                       ctx.globalCompositeOperation = drawMode === 'eraser' ? 'destination-out' : 'source-over';
                       ctx.lineTo(x, y); ctx.stroke();
                     }
                   }}
                   onMouseUp={() => { setIsDrawing(false); setShapeStart(null); canvasSnapshot.current = null; }}
                   onMouseLeave={() => { setIsDrawing(false); setShapeStart(null); canvasSnapshot.current = null; }}
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
                     placeholder="Gõ text rồi Enter..."
                   />
                 )}
               </>
             )}
          </div>
        </div>

        {/* Drag Handle */}
        <div onMouseDown={() => setIsDragging(true)} className={`w-[6px] h-full bg-[#202224] hover:bg-[#1e88e5] cursor-col-resize flex items-center justify-center shrink-0 z-10 transition-colors ${isDragging ? 'bg-[#1e88e5]' : ''}`}>
          <div className="flex flex-col gap-1"><div className="w-[2px] h-[2px] bg-slate-500"></div><div className="w-[2px] h-[2px] bg-slate-500"></div><div className="w-[2px] h-[2px] bg-slate-500"></div></div>
        </div>

        {/* Right: Answer Sheet */}
        <div style={{ width: `calc(${100 - leftWidth}% - 6px)` }} className="h-full flex flex-col shrink-0 bg-[#f8fafc]">
          <div className="bg-[#323639] border-b border-[#202224] px-6 flex justify-between items-center h-10 shrink-0 shadow-sm">
            <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest flex items-center gap-2">
              {gradeResult ? <><span>✅</span> Kết quả chấm điểm IGCSE</> : <><span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> Answer Sheet (Phiếu trả lời)</>}
            </span>
          </div>

          <div onScroll={handleContainerScroll} className={`flex-1 overflow-y-auto p-4 sm:p-8 ${isDragging ? 'pointer-events-none' : ''} custom-scrollbar`}>
            {/* Score Summary */}
            {gradeResult && (
                <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 mb-8 text-center">
                    <h2 className="text-2xl font-black text-slate-800 mb-2">Total Score</h2>
                    <div className="text-5xl font-black text-[#1e88e5] mb-4">
                        {gradeResult.total_student_score} <span className="text-2xl text-slate-400">/ {gradeResult.total_max_score}</span>
                    </div>
                    <div className="w-full bg-slate-200 rounded-full h-3 mb-4">
                      <div className="bg-gradient-to-r from-[#1e88e5] to-emerald-400 h-3 rounded-full transition-all" style={{ width: `${Math.min(100, (gradeResult.total_student_score / gradeResult.total_max_score) * 100)}%` }}></div>
                    </div>
                    <p className="text-[14px] text-slate-600 bg-slate-50 p-4 rounded-lg italic text-left">{gradeResult.general_feedback}</p>
                </div>
            )}

            {/* Questions */}
            <div className="space-y-8">
                {questions.map((q: any, qIdx: number) => (
                    <div key={qIdx} className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
                        <div className="flex gap-3 mb-6 items-baseline border-b border-slate-100 pb-4">
                            <h3 className="font-black text-slate-800 text-[18px]">Question {q.question_number}</h3>
                        </div>
                        
                        <div className="space-y-6">
                            {(q.sub_questions || []).map((sub: any) => {
                                const feedbackData = gradeResult?.details?.find((d:any) => d.id === sub.id);
                                const isCorrect = feedbackData?.student_score === sub.max_marks;
                                const isWrong = feedbackData && feedbackData?.student_score === 0;

                                return (
                                    <div key={sub.id} className={`p-4 rounded-lg border ${isReviewMode ? (isCorrect ? 'bg-emerald-50 border-emerald-200' : isWrong ? 'bg-red-50 border-red-200' : 'bg-orange-50 border-orange-200') : 'bg-slate-50 border-slate-200'}`}>
                                        <div className="flex justify-between items-start mb-3">
                                            <label className="font-semibold text-slate-800 text-[14px] leading-relaxed pr-4 whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: renderLatex(sub.label) }} />
                                            <span className="font-bold text-slate-400 text-[12px] whitespace-nowrap">[{sub.max_marks} marks]</span>
                                        </div>

                                        {/* Render input by question type */}
                                        {sub.type === 'short_answer' ? (
                                            <div className="relative">
                                                <div className="flex items-center gap-2">
                                                    <input ref={(el) => { inputRefs.current[sub.id] = el; }} type="text" value={answers[sub.id] || ''} onChange={(e) => handleAnswerChange(sub.id, e.target.value)} disabled={isReviewMode} placeholder="Điền đáp án ngắn..." className={`w-full max-w-sm px-4 py-2 border rounded-md text-[14px] outline-none transition-all ${isReviewMode ? 'bg-white border-slate-300' : 'focus:border-[#1e88e5] focus:ring-1 focus:ring-[#1e88e5]'}`}/>
                                                    {!isReviewMode && (
                                                        <button type="button" onClick={() => setShowPalette(prev => ({...prev, [sub.id]: !prev[sub.id]}))} className={`shrink-0 px-2.5 py-1.5 rounded-md text-[12px] font-bold border transition-all ${showPalette[sub.id] ? 'bg-[#1e88e5] text-white border-[#1e88e5]' : 'bg-white text-slate-500 border-slate-300 hover:border-[#1e88e5] hover:text-[#1e88e5]'}`} title="Bảng ký tự công thức">
                                                            f<sub>x</sub>
                                                        </button>
                                                    )}
                                                    {!isReviewMode && (
                                                      <button type="button" onClick={() => handleOcr(sub.id)} disabled={ocrLoading[sub.id]} className="shrink-0 px-2.5 py-1.5 rounded-md text-[12px] font-bold border transition-all bg-white text-slate-500 border-slate-300 hover:border-emerald-500 hover:text-emerald-600 disabled:opacity-50" title="Chụp ảnh bài làm → AI chuyển thành text">
                                                        {ocrLoading[sub.id] ? '⏳' : '📷'}
                                                      </button>
                                                    )}
                                                </div>
                                                {showPalette[sub.id] && !isReviewMode && (
                                                    <div className="absolute z-30 top-full mt-1 left-0 bg-white border border-slate-200 rounded-xl shadow-xl p-0 w-[380px] overflow-hidden">
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
                                                    <textarea ref={(el) => { inputRefs.current[sub.id] = el; }} value={answers[sub.id] || ''} onChange={(e) => handleAnswerChange(sub.id, e.target.value)} disabled={isReviewMode} placeholder="Viết câu trả lời tự luận..." className={`w-full px-4 py-3 border rounded-md min-h-[80px] text-[14px] outline-none transition-all resize-y ${isReviewMode ? 'bg-white border-slate-300' : 'focus:border-[#1e88e5] focus:ring-1 focus:ring-[#1e88e5]'}`}/>
                                                    {!isReviewMode && (
                                                        <button type="button" onClick={() => setShowPalette(prev => ({...prev, [sub.id]: !prev[sub.id]}))} className={`shrink-0 mt-1 px-2.5 py-1.5 rounded-md text-[12px] font-bold border transition-all ${showPalette[sub.id] ? 'bg-[#1e88e5] text-white border-[#1e88e5]' : 'bg-white text-slate-500 border-slate-300 hover:border-[#1e88e5] hover:text-[#1e88e5]'}`} title="Bảng ký tự công thức">
                                                            f<sub>x</sub>
                                                        </button>
                                                    )}
                                                    {!isReviewMode && (
                                                      <button type="button" onClick={() => handleOcr(sub.id)} disabled={ocrLoading[sub.id]} className="shrink-0 mt-1 px-2.5 py-1.5 rounded-md text-[12px] font-bold border transition-all bg-white text-slate-500 border-slate-300 hover:border-emerald-500 hover:text-emerald-600 disabled:opacity-50" title="Chụp ảnh bài làm → AI chuyển thành text">
                                                        {ocrLoading[sub.id] ? '⏳' : '📷'}
                                                      </button>
                                                    )}
                                                </div>
                                                {showPalette[sub.id] && !isReviewMode && (
                                                    <div className="absolute z-30 top-full mt-1 left-0 bg-white border border-slate-200 rounded-xl shadow-xl p-0 w-[380px] overflow-hidden">
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
                                                        <img src={answers[sub.id]} alt="Bài làm" className="max-h-[250px] object-contain rounded" />
                                                        {!isReviewMode && (
                                                            <button onClick={() => handleAnswerChange(sub.id, '')} className="absolute -top-3 -right-3 bg-red-500 text-white w-7 h-7 rounded-full shadow-md font-bold hover:scale-110 transition-transform">✕</button>
                                                        )}
                                                    </div>
                                                ) : (
                                                    <label className={`flex flex-col items-center justify-center w-full h-32 border-2 border-dashed border-slate-300 rounded-lg bg-white transition-colors ${!isReviewMode ? 'cursor-pointer hover:bg-sky-50 hover:border-sky-400' : 'opacity-50'}`}>
                                                        <div className="flex flex-col items-center justify-center pt-5 pb-6">
                                                            <span className="text-3xl mb-2">📸</span>
                                                            <p className="text-sm text-slate-500 font-semibold">Nhấn để chọn ảnh hoặc Ctrl+V để dán từ clipboard</p>
                                                            <p className="text-xs text-slate-400 mt-1">Ảnh sẽ tự động nén nhỏ {"<"} 1MB</p>
                                                        </div>
                                                        <input type="file" className="hidden" accept="image/*" capture="environment" onChange={(e) => {
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
                                                      Điểm đạt: {feedbackData.student_score} / {sub.max_marks}
                                                    </span>
                                                </div>
                                                <p className="text-[13px] text-slate-700 mt-2 mb-3"><span className="font-bold text-slate-900">Nhận xét: </span> {feedbackData.examiner_comment}</p>
                                                <div className="bg-white p-3 rounded border border-slate-200 text-[13px]">
                                                    <span className="font-bold text-slate-500 uppercase text-[10px] tracking-widest block mb-1">Đáp án đúng (Cambridge MS):</span>
                                                    <span className="font-medium text-emerald-600" dangerouslySetInnerHTML={{ __html: renderLatex(feedbackData.correct_answer || '') }} />
                                                </div>

                                                {!isCorrect && (
                                                    <div className="flex items-center gap-2 mt-4">
                                                        <button onClick={() => {
                                                            const query = `Câu hỏi: "${latexToText(sub.label)}"\nĐáp án học sinh: "${answers[sub.id] || 'Bỏ trống'}"\nĐáp án đúng: "${latexToText(feedbackData.correct_answer || '')}"\n\nThầy giải thích chi tiết giúp em tại sao em sai ạ!`;
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
                                                            💬 Chat Thầy AI
                                                        </button>
                                                        <button onClick={() => callAiTutor(latexToText(sub.label), answers[sub.id] || "Bỏ trống", latexToText(feedbackData.correct_answer || ''))} className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-amber-400 to-orange-400 text-white font-bold text-[12px] rounded-lg shadow-md hover:shadow-lg transition-all active:scale-95">
                                                            📞 Gọi Gia Sư
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
                ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
