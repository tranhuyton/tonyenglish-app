import React, { useState, useEffect, useRef } from 'react';
import { supabase } from './supabase';
import './tailwind.css';
import { useLmsLang, LmsLangToggle } from './utils/lmsI18n';
import { ImageLightboxModal, LightboxState, extractLightboxFromClick } from './mcqImageUtils';

// --- BỘ ICON CHUẨN IDP ---
const UserIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path fillRule="evenodd" d="M7.5 6a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM3.751 20.105a8.25 8.25 0 0116.498 0 .75.75 0 01-.437.695A18.683 18.683 0 0112 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 01-.437-.695z" clipRule="evenodd" /></svg>;
const SettingsIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path fillRule="evenodd" d="M11.078 2.25c-.917 0-1.699.663-1.85 1.567L9.05 4.889c-.02.12-.115.26-.297.348a7.493 7.493 0 00-.986.57c-.166.115-.334.126-.45.083L6.3 5.508a1.875 1.875 0 00-2.282.819l-.922 1.597a1.875 1.875 0 00.432 2.385l.84.692c.097.078.15.222.15.399v.111c0 .177-.053.321-.15.399l-.84.692a1.875 1.875 0 00-.432 2.385l.922 1.597a1.875 1.875 0 002.282.818l1.019-.382c.115-.043.283-.031.45.082.312.214.641.405.985.57.182.088.277.228.297.35l.178 1.071c.151.904.933 1.567 1.85 1.567h1.844c.916 0 1.699-.663 1.85-1.567l.178-1.072c.02-.12.114-.26.297-.349.344-.165.673-.356.985-.57.167-.114.335-.125.45-.082l1.02.382a1.875 1.875 0 002.28-.819l.923-1.597a1.875 1.875 0 00-.432-2.385l-.84-.692c-.098-.078-.15-.222-.15-.399v-.111c0-.177.052-.321.15-.399l.84-.692a1.875 1.875 0 00.432-2.385l-.923-1.597a1.875 1.875 0 00-2.28-.818l-1.02.382c-.114.043-.282.031-.449-.083a7.49 7.49 0 00-.985-.57c-.183-.087-.277-.227-.297-.348l-.179-1.072a1.875 1.875 0 00-1.85-1.567h-1.843zM12 15.75a3.75 3.75 0 110-7.5 3.75 3.75 0 010 7.5z" clipRule="evenodd" /></svg>;
const UndoIcon = () => <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M9 15L3 9m0 0l6-6M3 9h12a6 6 0 010 12h-3" /></svg>;
const RedoIcon = () => <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M15 15l6-6m0 0l-6-6m6 6H9a6 6 0 000 12h3" /></svg>;
const BoldIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-4 h-4"><path fillRule="evenodd" d="M8.25 4.5A.75.75 0 007.5 5.25v13.5a.75.75 0 00.75.75h5.25a4.5 4.5 0 003.568-7.254 4.5 4.5 0 00-2.818-7.746H8.25zM9 10.5h4.125a2.25 2.25 0 000-4.5H9v4.5zm0 2.25v4.5h4.875a2.25 2.25 0 000-4.5H9z" clipRule="evenodd" /></svg>;
const ItalicIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-4 h-4"><path fillRule="evenodd" d="M12.984 4.15A.75.75 0 0113.5 4.5h4.5a.75.75 0 010 1.5h-2.316l-3.375 12h2.441a.75.75 0 010 1.5H10.5a.75.75 0 010-1.5h2.316l3.375-12H13.5a.75.75 0 01-.516-1.35z" clipRule="evenodd" /></svg>;
const UnderlineIcon = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-4 h-4"><path fillRule="evenodd" d="M6 3.75a.75.75 0 01.75.75v8.25a5.25 5.25 0 0010.5 0V4.5a.75.75 0 011.5 0v8.25a6.75 6.75 0 01-13.5 0V4.5a.75.75 0 01.75-.75zM3.75 20.25a.75.75 0 01.75-.75h15a.75.75 0 010 1.5h-15a.75.75 0 01-.75-.75z" clipRule="evenodd" /></svg>;

export default function IeltsWriting({ onBack, testData: propTestData, onFinish }: { onBack?: () => void, testData?: any, onFinish?: (res: any) => void }) {
  const [lang, setLang] = useLmsLang();
  const isEn = lang === 'en';
  const [imageLightbox, setImageLightbox] = useState<LightboxState | null>(null);
  
  const [testData, setTestData] = useState<any>(() => {
     if (propTestData) return propTestData;
     try {
       const saved = sessionStorage.getItem('lms_current_test');
       return saved ? JSON.parse(saved) : null;
     } catch (e) { return null; }
  });

  let safeData = testData || {};
  if (typeof safeData === 'string') {
    try { safeData = JSON.parse(safeData); } catch (e) { safeData = {}; }
  }
  let contentJSON = safeData?.content_json || safeData || {};
  if (typeof contentJSON === 'string') {
    try { contentJSON = JSON.parse(contentJSON); } catch (e) { contentJSON = {}; }
  }
  const basicInfo = contentJSON?.basicInfo || { title: "IELTS Writing", timeLimit: "60" };
  const parts = Array.isArray(contentJSON?.parts) ? contentJSON.parts : [];

  const allQuestions: any[] = [];
  if (Array.isArray(parts)) {
    parts.forEach((p: any) => {
      if (p && Array.isArray(p.sections)) {
        p.sections.forEach((s: any) => {
          if (s && Array.isArray(s.questions)) {
            s.questions.forEach((q: any) => {
              if (q) {
                // Thu gom dữ liệu mỏng nhẹ, loại bỏ partTitle, partContent
                allQuestions.push({ ...q, secTitle: s.title, secContent: s.content });
              }
            });
          }
        });
      }
    });
  }

  const [answers, setAnswers] = useState<Record<string, string>>(() => {
     if (!safeData?.id) return {};
     try {
        const saved = localStorage.getItem(`ielts_writing_ans_${safeData.id}`);
        const parsed = saved ? JSON.parse(saved) : {};
        return (typeof parsed === 'object' && parsed !== null) ? parsed : {};
     } catch(e) { return {}; }
  });
  const answersRef = useRef(answers);
  useEffect(() => { answersRef.current = answers; }, [answers]);

  const [currentTaskIndex, setCurrentTaskIndex] = useState(0);
  const currentTask = allQuestions[currentTaskIndex];
  
  const [reviewFlags, setReviewFlags] = useState<Record<number, boolean>>({});

  const [isSubmitted, setIsSubmitted] = useState(false);
  useEffect(() => { window.dispatchEvent(new CustomEvent('tony-review-mode-change', { detail: Boolean(isSubmitted) })); return () => { window.dispatchEvent(new CustomEvent('tony-review-mode-change', { detail: false })); }; }, [isSubmitted]);
  const [isGrading, setIsGrading] = useState(false);
  const isFinishingRef = useRef(false);
  const [aiResult, setAiResult] = useState<any>(null);

  const parseTime = (t: any) => parseInt(t) || 60;
  const [timeLeft, setTimeLeft] = useState(() => parseTime(basicInfo.timeLimit) * 60);
  const timeLeftRef = useRef(timeLeft);
  useEffect(() => { timeLeftRef.current = timeLeft; }, [timeLeft]);

  // Resize Left/Right Column logic
  const [leftWidth, setLeftWidth] = useState(50);
  const [isDesktop, setIsDesktop] = useState(() => typeof window !== 'undefined' ? window.innerWidth >= 768 : true);
  const [editorFontSize, setEditorFontSize] = useState<'S' | 'M' | 'L'>('M');
  const containerRef = useRef<HTMLElement>(null);
  const isDragging = useRef(false);

  useEffect(() => {
    const onResize = () => setIsDesktop(window.innerWidth >= 768);
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []);

  const handleSafeExit = () => {
    const hasDraft = Object.values(answers).some((v) => String(v || '').trim().length > 0);
    if (!isSubmitted && hasDraft) {
      if (!window.confirm(isEn ? 'You have an unsubmitted essay. Are you sure you want to exit?' : 'Bạn đang có bài viết chưa nộp. Bạn có chắc muốn thoát không?')) return;
    }
    if (onBack) onBack();
  };

  const startDrag = () => { 
      isDragging.current = true; 
      document.body.style.cursor = 'col-resize'; 
      document.body.style.userSelect = 'none'; 
  };
  
  const stopDrag = () => { 
      isDragging.current = false; 
      document.body.style.cursor = 'default'; 
      document.body.style.userSelect = 'auto'; 
  };
  
  const onDrag = (e: MouseEvent) => {
    if (!isDragging.current || !containerRef.current) return;
    const containerRect = containerRef.current.getBoundingClientRect(); 
    const newLeftWidth = ((e.clientX - containerRect.left) / containerRect.width) * 100;
    if (newLeftWidth > 20 && newLeftWidth < 80) setLeftWidth(newLeftWidth);
  };

  useEffect(() => { 
      window.addEventListener('mousemove', onDrag); 
      window.addEventListener('mouseup', stopDrag); 
      return () => { 
          window.removeEventListener('mousemove', onDrag); 
          window.removeEventListener('mouseup', stopDrag); 
      }; 
  }, []);

  useEffect(() => {
    if (isSubmitted || isGrading) return;
    const timer = setInterval(() => setTimeLeft(prev => {
        if (prev <= 1) { clearInterval(timer); handleSubmitRef.current(true); return 0; }
        return prev - 1;
    }), 1000);
    return () => clearInterval(timer);
  }, [isSubmitted, isGrading]);

  const formatTime = (secs: number) => {
    if (isNaN(secs)) return '60 minutes left';
    if (secs < 60) {
      const m = Math.floor(Math.max(0, secs) / 60).toString().padStart(2, '0');
      const s = (Math.max(0, secs) % 60).toString().padStart(2, '0');
      return `${m}:${s}`;
    }
    const m = Math.floor(secs / 60);
    return `${m} minutes left`;
  };

  useEffect(() => {
    if (safeData?.id && !isSubmitted && !isGrading && !isFinishingRef.current) {
      localStorage.setItem(`ielts_writing_ans_${safeData.id}`, JSON.stringify(answers));
    }
  }, [answers, safeData?.id, isSubmitted, isGrading]);

  const handleAnswerChange = (qId: string, value: string) => {
    setAnswers(prev => ({ ...prev, [qId]: value }));
  };

  const handleReviewToggle = () => {
    setReviewFlags(prev => ({ ...prev, [currentTaskIndex]: !prev[currentTaskIndex] }));
  };

  const getWordCount = (text: any) => {
    if (!text || typeof text !== 'string') return 0;
    const str = text.trim();
    return str === '' ? 0 : str.split(/\s+/).length;
  };

  const handleSubmit = async (forceAutoSubmit: any = false) => {
    const isForced = forceAutoSubmit === true;
    if (isGrading || isFinishingRef.current) return;
    const currentAnswers = answersRef.current;

    let totalWords = 0;
    Object.values(currentAnswers).forEach(ans => totalWords += getWordCount(ans));

    if (!isForced) {
      if (totalWords < 50) {
        alert(isEn ? "Your essay is too short. Please write at least 50 words before submitting." : "Bạn chưa viết đủ bài. Vui lòng hoàn thiện tối thiểu 50 từ trước khi nộp.");
        return;
      }
      if (!window.confirm(isEn ? "Are you sure you want to submit your test? Your essay will be sent to the AI Examiner for grading." : "Bạn có chắc chắn muốn nộp bài thi? Hệ thống sẽ gửi bài cho Giám khảo AI chấm điểm.")) return;
    }

    isFinishingRef.current = true;
    setIsGrading(true);

    try {
      // 🚀 NHẶT LINK ẢNH TỪ TẤT CẢ CÁC TASK ĐỂ GỬI CHO AI CHẤM
      const collectedImages: string[] = [];
      allQuestions.forEach(q => {
         if (q.imageUrl && typeof q.imageUrl === 'string') collectedImages.push(q.imageUrl);
         if (q.content) {
             const imgRegex = /<img[^>]+src="([^">]+)"/g;
             let match;
             while ((match = imgRegex.exec(q.content)) !== null) {
                 collectedImages.push(match[1]);
             }
         }
      });

      const prompt = isEn ? `
        You are a dedicated, encouraging IELTS Writing Examiner. Do not overly penalize minor phrasing slips if the main ideas remain clear. If the essay demonstrates strong argument structure and rich vocabulary, consider awarding higher bands (from 7.0 to 8.5).
        IMPORTANT: Write ALL feedback, criterion comments, corrections, and generalFeedback strictly in English.

        EXAM PROMPT INFORMATION (Task 1 and Task 2 instructions):
        ${JSON.stringify(allQuestions.map((q, i) => `Task ${i+1} (${q.secTitle}): ${q.secContent} ${q.content}`))}

        Note: For Task 1, chart/diagram/map images are attached. CAREFULLY ANALYZE these images to verify whether the candidate accurately described the figures and key features (for Task Achievement).

        STUDENT'S ESSAY RESPONSES (mapped by question ID):
        ${JSON.stringify(currentAnswers)}

        Analyze all tasks completed by the student and return ONLY the exact JSON format below (no markdown code fences):
        {
          "overall": 7.5,
          "tasks": [
            {
              "task_name": "Task 1",
              "score": 7.0,
              "criteria": [
                { "name": "Task Achievement", "score": 7.0, "comment": "Detailed English feedback referencing the original chart/prompt..." },
                { "name": "Coherence & Cohesion", "score": 7.0, "comment": "Detailed English feedback..." },
                { "name": "Lexical Resource", "score": 7.5, "comment": "Detailed English feedback..." },
                { "name": "Grammatical Range", "score": 7.0, "comment": "Detailed English feedback..." }
              ],
              "feedback": "Student's essay text annotated with <span class='bg-red-200 text-red-800 line-through px-1'>incorrect phrase</span> and <span class='bg-emerald-200 text-emerald-800 font-bold px-1'>improved phrase</span>..."
            }
          ],
          "generalFeedback": "Overall English summary of strengths and areas for improvement..."
        }
      ` : `
        Bạn là một Giám khảo IELTS tận tâm, chấm điểm theo hướng khuyến khích học sinh. Không quá khắt khe ở các lỗi diễn đạt nhỏ nếu ý chính vẫn rõ ràng. Bài viết có sử dụng cấu trúc lập luận tốt và từ vựng phong phú thì nên cân nhắc ưu tiên mức điểm cao (từ 7.0 đến 8.5).
        
        THÔNG TIN ĐỀ BÀI (Chứa các yêu cầu của Task 1 và Task 2):
        ${JSON.stringify(allQuestions.map((q, i) => `Task ${i+1} (${q.secTitle}): ${q.secContent} ${q.content}`))}

        Lưu ý: Đối với Task 1, tôi đã gửi kèm hình ảnh biểu đồ/bản đồ trong tệp đính kèm. Bạn HÃY PHÂN TÍCH ẢNH NÀY để đối chiếu xem học sinh mô tả số liệu, đặc điểm có đúng với hình hay không (để chấm tiêu chí Task Achievement).

        BÀI LÀM CỦA HỌC SINH (Map theo ID câu hỏi):
        ${JSON.stringify(currentAnswers)}

        Hãy phân tích tất cả các Task học sinh đã làm và trả về ĐÚNG định dạng JSON sau (không dùng markdown block):
        {
          "overall": 7.5,
          "tasks": [
            {
              "task_name": "Task 1",
              "score": 7.0,
              "criteria": [
                { "name": "Task Achievement", "score": 7.0, "comment": "Nhận xét dựa trên hình ảnh gốc..." },
                { "name": "Coherence & Cohesion", "score": 7.0, "comment": "Nhận xét..." },
                { "name": "Lexical Resource", "score": 7.5, "comment": "Nhận xét..." },
                { "name": "Grammatical Range", "score": 7.0, "comment": "Nhận xét..." }
              ],
              "feedback": "Văn bản bài làm kèm thẻ <span class='bg-red-200 text-red-800 line-through px-1'>từ sai</span> và <span class='bg-emerald-200 text-emerald-800 font-bold px-1'>từ đúng</span>..."
            }
          ],
          "generalFeedback": "Nhận xét tổng quan điểm mạnh điểm yếu..."
        }
      `;

      const { data, error } = await supabase.functions.invoke('ai-grader', {
        body: { 
           prompt: prompt,
           imageUrls: collectedImages, // 🚀 BƠM MẢNG ẢNH VÀO ĐÂY NÈ!
           model: 'gemini-2.5-pro'
        }
      });

      if (error) throw new Error((isEn ? "Server error: " : "Lỗi gọi Server: ") + error.message);
      if (data?.error) throw new Error((isEn ? "AI grading error: " : "Lỗi chấm điểm AI: ") + data.error);

      const textResponse = data.result.replace(/\u0060{3}(json)?/gi, "").trim();
      const parsedResult = JSON.parse(textResponse);
      
      setAiResult(parsedResult);
      setIsSubmitted(true);

      const { data: { user } } = await supabase.auth.getUser();
      if (user) {
        const timeSpentSecs = Math.max(0, (parseTime(basicInfo.timeLimit) * 60) - timeLeftRef.current);
        await supabase.from('test_results').insert([{
          user_id: user.id,
          course_id: safeData?.course_id || null,
          test_title: basicInfo.title,
          test_type: 'IELTS-Writing',
          score: parsedResult.overall,
          total_score: 9,
          time_spent: timeSpentSecs,
          details: { test_id: safeData?.id, userAnswers: currentAnswers, aiFeedback: parsedResult, bandScore: parsedResult.overall }
        }]);
      }

      // Chỉ xóa bản nháp sau khi chấm & lưu thành công
      if (safeData?.id) localStorage.removeItem(`ielts_writing_ans_${safeData.id}`);

    } catch (error: any) {
      isFinishingRef.current = false;
      console.error("LỖI CHI TIẾT:", error);
      alert((isEn ? "AI grading system error. Please try again: " : "Hệ thống chấm điểm AI bị lỗi. Vui lòng thử lại: ") + error.message);
    } finally {
      setIsGrading(false);
    }
  };

  const handleSubmitRef = useRef(handleSubmit);
  handleSubmitRef.current = handleSubmit;

  if (!testData || allQuestions.length === 0) {
    return (
      <div className="h-[100dvh] w-full flex flex-col items-center justify-center gap-4 bg-[#eeeeee] font-bold text-slate-800 p-6 text-center">
        <p className="text-base">⚠️ {isEn ? 'IELTS Writing exam content not found.' : 'Không tìm thấy nội dung đề thi IELTS Writing.'}</p>
        {onBack && (
          <button
            type="button"
            onClick={onBack}
            className="px-5 py-2.5 bg-[#0a5482] hover:bg-[#084266] text-white rounded-xl text-sm font-bold transition shadow-sm cursor-pointer"
          >
            ← {isEn ? 'Back' : 'Quay lại'}
          </button>
        )}
      </div>
    );
  }

  return (
    <div className="h-[100dvh] flex flex-col bg-[#eeeeee] font-sans text-slate-900 overflow-hidden">
      
      {/* Đã tinh chỉnh khoảng cách dòng (leading) và margin dưới của thẻ P */}
      <style>{`
          .format-passage p { margin-top: 0 !important; margin-bottom: 0.5rem !important; }
          .format-passage p:last-child { margin-bottom: 0 !important; }
          .format-passage br { display: block; content: ""; margin-bottom: 0.25rem; }
      `}</style>

      {/* HEADER */}
      <header className="h-[52px] bg-[#1e293b] text-white flex justify-between items-center gap-3 px-4 shrink-0 select-none z-20 border-b border-slate-700">
        <div className="flex items-center gap-2 min-w-0 flex-1">
          <UserIcon />
          <span className="font-bold text-[14px] truncate text-white">{basicInfo.title}</span>
        </div>
        
        <div className={`font-bold text-[14px] sm:text-[15px] tracking-wider shrink-0 tabular-nums px-3 py-1 rounded-lg bg-white/10 ${timeLeft <= 300 && !isSubmitted ? 'text-rose-400 animate-pulse' : 'text-white'}`}>
           {isSubmitted ? 'TEST FINISHED' : formatTime(timeLeft)}
        </div>

        <div className="flex items-center justify-end gap-2 sm:gap-3 shrink-0 flex-1">
           <LmsLangToggle lang={lang} setLang={setLang} variant="dark" />
           {isSubmitted ? (
              <button type="button" onClick={onBack} className="text-[13px] font-bold bg-[#2ab4e8] hover:bg-[#1fa0d4] text-white px-4 py-1.5 rounded-lg transition cursor-pointer">
                {isEn ? 'Back to Student Portal' : 'Quay lại Góc Học Viên'}
              </button>
           ) : (
              <button type="button" onClick={handleSafeExit} className="text-[13px] font-bold px-3.5 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 text-slate-100 border border-white/15 transition cursor-pointer">
                {isEn ? 'Exit' : 'Thoát'}
              </button>
           )}
        </div>
      </header>

      {isGrading && (
        <div className="flex-1 flex flex-col items-center justify-center bg-white/95 z-50 absolute inset-0 pt-10">
          <div className="relative flex items-center justify-center w-28 h-28 mb-6">
             <svg className="absolute inset-0 w-full h-full animate-spin text-[#0a5482]" viewBox="0 0 100 100">
               <circle cx="50" cy="50" r="45" fill="none" stroke="currentColor" strokeWidth="8" strokeDasharray="200" strokeLinecap="round" />
             </svg>
             <span className="font-black text-xl text-[#0a5482]">AI</span>
          </div>
          <h2 className="text-xl font-black text-slate-800 mb-2">{isEn ? 'Grading IELTS Writing...' : 'Đang chấm điểm IELTS Writing...'}</h2>
          <p className="text-slate-500 text-sm font-medium">{isEn ? 'Please wait a moment while the AI Examiner evaluates your essay.' : 'Vui lòng đợi trong giây lát để giám khảo AI phân tích bài viết của bạn.'}</p>
        </div>
      )}

      {!isSubmitted && !isGrading && currentTask && (() => {
        const currentWordCount = getWordCount(answers[currentTask.id]);
        const minTargetWords = currentTaskIndex === 0 && allQuestions.length > 1 ? 150 : 250;
        const meetsTarget = currentWordCount >= minTargetWords;
        const fontSizeClass = editorFontSize === 'S' ? 'text-[14px]' : editorFontSize === 'L' ? 'text-[18px]' : 'text-[16px]';
        return (
        <div className="flex-1 flex flex-col overflow-hidden bg-[#eeeeee]">

          <main className="flex-1 flex flex-col md:flex-row overflow-y-auto md:overflow-hidden relative" ref={containerRef as any}>
            
            {/* CỘT TRÁI - ĐỀ BÀI (CHUẨN UI IDP/BC) */}
            <section
              className="p-5 sm:p-8 md:p-10 md:overflow-y-auto custom-scrollbar border-b md:border-b-0 md:border-r border-slate-300 flex flex-col bg-white shrink-0"
              style={{ width: isDesktop ? `${leftWidth}%` : '100%' }}
              onClick={(e) => {
                const lb = extractLightboxFromClick(e, e.currentTarget);
                if (lb) setImageLightbox(lb);
              }}
            >
              <div className={`format-passage max-w-none leading-[1.7] text-slate-900 font-serif break-words ${fontSizeClass}`}>
                
                {/* Chỉ giữ lại Tên Section (Task) và Nội Dung */}
                {currentTask.secTitle && (
                    <p className="font-bold text-[16px] text-[#0a5482] mb-4">[{currentTask.secTitle}]</p>
                )}

                {currentTask.secContent && (
                  <div className="mb-4 whitespace-pre-wrap" dangerouslySetInnerHTML={{__html: currentTask.secContent}} />
                )}
                
                {currentTask.content && (
                  <div className="mb-4 whitespace-pre-wrap" dangerouslySetInnerHTML={{__html: currentTask.content}} />
                )}

                {currentTask.imageUrl && (
                  <div className="mt-6 relative group inline-block max-w-[700px] w-full">
                    <img
                      src={currentTask.imageUrl}
                      alt="Diagram"
                      title={isEn ? 'Click to enlarge diagram' : 'Bấm để phóng to biểu đồ'}
                      className="w-full max-w-[700px] h-auto block rounded-xl border border-slate-200 cursor-zoom-in transition hover:shadow-md"
                    />
                    <span className="pointer-events-none absolute bottom-3 right-3 px-2.5 py-1 rounded-lg bg-slate-900/75 text-white text-[11px] font-sans font-bold opacity-0 group-hover:opacity-100 transition-opacity shadow">
                      🔍 {isEn ? 'Click to zoom' : 'Bấm để phóng to'}
                    </span>
                  </div>
                )}

              </div>
              <div className="h-8 md:h-[100px]" />
            </section>

            {/* THANH KÉO DÃN Ở GIỮA (Desktop only) */}
            <div className="hidden md:flex w-4 bg-[#e8e8e8] hover:bg-[#d4d4d4] cursor-col-resize flex-col justify-center items-center z-10 border-x border-slate-300 transition-colors shrink-0" onMouseDown={startDrag}>
               <div className="flex flex-col gap-1.5 opacity-40">
                  <div className="w-1 h-1 bg-black"></div>
                  <div className="w-1 h-1 bg-black"></div>
                  <div className="w-1 h-1 bg-black"></div>
                  <div className="w-1 h-1 bg-black"></div>
               </div>
            </div>

            {/* CỘT PHẢI - BÀI VIẾT CỦA HỌC SINH */}
            <section
              className="p-4 sm:p-6 md:p-8 flex flex-col md:overflow-hidden relative bg-slate-100 flex-1 md:flex-none min-h-[380px] md:min-h-0"
              style={{ width: isDesktop ? `calc(${100 - leftWidth}% - 16px)` : '100%' }}
            >
              
              <div className="flex-1 bg-white border border-slate-300 rounded-xl shadow-sm flex flex-col overflow-hidden">
                {/* THANH TOOLBAR THỰC DỤNG CỦA TEXTAREA */}
                <div className="min-h-[44px] border-b border-slate-200 flex items-center justify-between flex-wrap gap-2 px-4 py-2 shrink-0 bg-slate-50">
                   <div className="flex items-center gap-2">
                      <span className="px-2.5 py-0.5 rounded-md bg-[#0a5482] text-white text-xs font-extrabold">
                        Task {currentTaskIndex + 1}
                      </span>
                      <span className={`text-xs font-bold px-2.5 py-0.5 rounded-full border ${meetsTarget ? 'bg-emerald-50 text-emerald-700 border-emerald-200' : 'bg-amber-50 text-amber-800 border-amber-200'}`}>
                        {currentWordCount} / {minTargetWords}+ {isEn ? 'words' : 'từ'}
                      </span>
                   </div>
                   <div className="flex items-center gap-1 bg-white border border-slate-200 rounded-lg p-0.5">
                      {(['S', 'M', 'L'] as const).map((sz) => (
                        <button
                          key={sz}
                          type="button"
                          onClick={() => setEditorFontSize(sz)}
                          className={`px-2 py-0.5 rounded text-xs font-extrabold transition cursor-pointer ${
                            editorFontSize === sz
                              ? 'bg-[#0a5482] text-white'
                              : 'text-slate-600 hover:bg-slate-100'
                          }`}
                          title={isEn ? `Font size ${sz}` : `Cỡ chữ ${sz}`}
                        >
                          {sz === 'S' ? 'A-' : sz === 'M' ? 'A' : 'A+'}
                        </button>
                      ))}
                   </div>
                </div>
                
                <textarea 
                  className={`flex-1 w-full p-5 sm:p-7 outline-none resize-none text-slate-900 font-serif custom-scrollbar leading-[1.7] bg-white min-h-[260px] ${fontSizeClass}`}
                  placeholder="Start typing your essay here..."
                  value={answers[currentTask.id] || ''}
                  onChange={(e) => handleAnswerChange(currentTask.id, e.target.value)}
                  spellCheck="false"
                />
              </div>
              
              <div className="mt-2.5 flex items-center justify-between text-[13px] text-slate-600 font-bold tracking-wide">
                <span>Word Count: <strong className={meetsTarget ? 'text-emerald-700' : 'text-slate-900'}>{currentWordCount}</strong></span>
                <span className="text-xs font-medium text-slate-500">{isEn ? `Minimum target: ${minTargetWords} words` : `Mục tiêu tối thiểu: ${minTargetWords} từ`}</span>
              </div>

            </section>
          </main>

          {/* THANH FOOTER */}
          <footer className="h-[60px] bg-white border-t border-slate-300 flex justify-between items-center px-4 sm:px-6 shrink-0 select-none">
             
             <div className="flex items-center h-full min-w-0">
                <div className="flex items-center gap-2 h-full pr-4 sm:pr-6 border-r border-slate-200 shrink-0">
                  <input 
                    type="checkbox" 
                    id="review" 
                    className="w-4 h-4 cursor-pointer accent-[#0a5482]" 
                    checked={!!reviewFlags[currentTaskIndex]}
                    onChange={handleReviewToggle}
                  />
                  <label htmlFor="review" className="text-[13px] sm:text-[14px] font-bold text-slate-700 cursor-pointer whitespace-nowrap">Review</label>
                </div>
                
                <div className="flex-1 flex justify-start items-center gap-2 overflow-x-auto px-4 py-1 custom-scrollbar min-w-0">
                   {allQuestions.map((q, idx) => {
                      const isActive = idx === currentTaskIndex;
                      const isReview = reviewFlags[idx];
                      
                      const shapeClass = isReview ? 'rounded-full' : 'rounded-lg';
                      const bgClass = isActive ? 'bg-[#0a5482] text-white border-[#0a5482] shadow-sm' : 'bg-white text-slate-700 border-slate-300 hover:bg-slate-100 cursor-pointer';

                      return (
                        <div key={q.id} className="flex items-center gap-2 h-full shrink-0">
                           <span className="text-[13px] font-bold text-slate-600 hidden sm:block">Task {idx + 1}:</span>
                           <button 
                             type="button"
                             onClick={() => setCurrentTaskIndex(idx)}
                             className={`w-9 h-9 flex items-center justify-center font-bold text-[14px] border transition-all ${shapeClass} ${bgClass}`}
                           >
                             {idx + 1}
                           </button>
                        </div>
                      )
                   })}
                </div>
             </div>

             <div className="flex items-center gap-3 shrink-0 pl-4 border-l border-slate-200">
                <div className="hidden sm:flex items-center gap-1.5">
                   <button type="button" onClick={() => setCurrentTaskIndex(prev => Math.max(0, prev - 1))} disabled={currentTaskIndex === 0} className="w-8 h-8 flex items-center justify-center text-slate-700 hover:bg-slate-100 border border-slate-300 bg-white rounded-lg transition disabled:opacity-30 cursor-pointer">←</button>
                   <button type="button" onClick={() => setCurrentTaskIndex(prev => Math.min(allQuestions.length - 1, prev + 1))} disabled={currentTaskIndex === allQuestions.length - 1} className="w-8 h-8 flex items-center justify-center text-slate-700 hover:bg-slate-100 border border-slate-300 bg-white rounded-lg transition disabled:opacity-30 cursor-pointer">→</button>
                </div>
                
                <button 
                  type="button"
                  onClick={() => handleSubmit(false)}
                  className="bg-[#0a5482] hover:bg-[#084266] text-white px-5 sm:px-6 py-2 rounded-xl text-[13px] sm:text-[14px] font-black transition uppercase tracking-wide shadow-sm cursor-pointer"
                >
                  {isEn ? 'Submit' : 'Nộp bài'}
                </button>
             </div>

          </footer>

        </div>
        );
      })()}

      {isSubmitted && aiResult && (
        <main
          className="flex-1 overflow-y-auto p-4 md:p-8 custom-scrollbar bg-slate-50"
          onClick={(e) => {
            const lb = extractLightboxFromClick(e, e.currentTarget);
            if (lb) setImageLightbox(lb);
          }}
        >
          <div className="max-w-5xl mx-auto space-y-6">
            
            <div className="bg-gradient-to-br from-[#073b5c] via-[#0a5482] to-[#0f172a] p-7 sm:p-9 rounded-3xl shadow-xl border border-sky-400/20 text-white relative overflow-hidden">
              <div className="absolute -top-16 -right-16 w-56 h-56 bg-[#2ab4e8]/20 blur-3xl rounded-full pointer-events-none" />
              <div className="relative z-10 flex flex-col sm:flex-row items-center justify-between gap-6">
                <div className="text-center sm:text-left">
                  <span className="inline-flex items-center gap-1.5 text-xs font-extrabold uppercase tracking-widest text-[#2ab4e8] mb-2">
                    ✍️ IELTS Writing AI Evaluation
                  </span>
                  <h2 className="text-2xl sm:text-3xl font-black tracking-tight mb-1">{basicInfo.title}</h2>
                  <p className="text-sky-100/80 text-sm">{isEn ? 'Evaluated across the 4 official IELTS Writing criteria' : 'Kết quả đánh giá theo 4 tiêu chí chuẩn giám khảo IELTS'}</p>
                </div>
                <div className="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl px-8 py-4 text-center shrink-0">
                  <span className="text-[11px] font-extrabold text-sky-200 uppercase tracking-widest block mb-1">Overall Band</span>
                  <span className="text-5xl sm:text-6xl font-black text-white tabular-nums">{aiResult.overall}</span>
                </div>
              </div>
            </div>

            <div className="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200/90 shadow-sm">
                <h3 className="font-black text-lg text-[#0a5482] mb-3.5 flex items-center gap-2">💡 {isEn ? 'Overall Feedback' : 'Nhận xét tổng quan'}</h3>
                <div className="p-5 bg-sky-50/70 border border-sky-200/70 rounded-xl text-[15px] leading-[1.8] font-medium text-slate-800 font-sans">
                  {aiResult.generalFeedback}
                </div>
            </div>

            {Array.isArray(aiResult.tasks) && aiResult.tasks.map((task: any, idx: number) => (
              <div className="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200/90 shadow-sm space-y-6" key={idx}>
                <div className="flex flex-wrap justify-between items-center gap-3 pb-4 border-b border-slate-200">
                  <h3 className="font-black text-xl sm:text-2xl text-slate-900">{task.task_name}</h3>
                  <span className="font-black text-base text-white bg-[#0a5482] px-4 py-1.5 rounded-xl shadow-sm">Band {task.score}</span>
                </div>
                
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  {Array.isArray(task.criteria) && task.criteria.map((c: any, i: number) => (
                    <div key={i} className="bg-slate-50 p-4 rounded-xl border border-slate-200/80">
                      <div className="flex justify-between items-center mb-2">
                        <span className="font-bold text-slate-800 text-sm">{c.name}</span>
                        <span className="font-black text-[#0a5482] bg-sky-100 px-2.5 py-0.5 rounded-lg text-sm tabular-nums">{c.score}</span>
                      </div>
                      <p className="text-sm text-slate-600 font-medium leading-relaxed font-sans">{c.comment}</p>
                    </div>
                  ))}
                </div>

                <div>
                  <h4 className="font-black text-base text-slate-800 mb-3">✍️ {isEn ? 'Your Essay & Detailed Corrections' : 'Bài làm & Gợi ý sửa lỗi chi tiết'}</h4>
                  <div className="p-5 sm:p-6 bg-slate-50 border border-slate-200/80 rounded-xl text-[15.5px] leading-[1.85] font-sans text-slate-800" dangerouslySetInnerHTML={{__html: task.feedback}} />
                </div>
              </div>
            ))}
          </div>
        </main>
      )}
      <ImageLightboxModal
        items={imageLightbox?.items || null}
        initialIndex={imageLightbox?.index ?? 0}
        onClose={() => setImageLightbox(null)}
      />
    </div>
  );
}