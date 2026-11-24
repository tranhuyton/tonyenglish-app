import React, { useState, useRef, useEffect, useMemo } from 'react';
import { supabase } from './supabase';
import { useTestGuideVideo, TestGuideVideoButton, TestGuideVideoPlayer, TestGuideVideoEditModal } from './TestGuideVideo';
import { useLmsLang, LmsLangToggle } from './utils/lmsI18n';
import { ImageLightboxModal, LightboxState, extractLightboxFromClick } from './mcqImageUtils';

export default function SplitScreenTest({ onBack, onStartTest, testData: propTestData }: { onBack?: () => void, onStartTest?: any, testData?: any }) {
  const [lang, setLang] = useLmsLang();
  const isEn = lang === 'en';
  // LẤY ĐÚNG ĐỀ THI TỪ THƯ VIỆN TRUYỀN VÀO (ưu tiên prop, fallback sessionStorage)
  const [testData, setTestData] = useState<any>(() => {
     if (propTestData) return propTestData;
     const saved = sessionStorage.getItem('lms_current_test');
     return saved ? JSON.parse(saved) : null;
  });
  const [isLoading, setIsLoading] = useState(!testData);
  const [imageLightbox, setImageLightbox] = useState<LightboxState | null>(null);

  // 🚀 NHẬN TÍN HIỆU TỪ STUDENT PORTAL XEM CÓ PHẢI LÀ CHẾ ĐỘ XEM LẠI LỊCH SỬ KHÔNG
  const initIsReview = !!testData?.isReview;
  const [isReviewMode, setIsReviewMode] = useState(initIsReview);
  useEffect(() => { window.dispatchEvent(new CustomEvent('tony-review-mode-change', { detail: Boolean(isReviewMode) })); return () => { window.dispatchEvent(new CustomEvent('tony-review-mode-change', { detail: false })); }; }, [isReviewMode]);
  const isExercise = testData?.content_json?.basicInfo?.category === 'exercise';

  // KHÔI PHỤC BẢN NHÁP HOẶC ĐÁP ÁN LỊCH SỬ
  const [answers, setAnswers] = useState<Record<string, string>>(() => {
     if (initIsReview && testData?.past_answers) {
         return testData.past_answers;
     }
     if (!testData?.id) return {};
     try {
        const saved = localStorage.getItem(`case_study_ans_${testData.id}`);
        return saved ? JSON.parse(saved) : {};
     } catch(e) { return {}; }
  });
  
  const answersRef = useRef(answers);
  useEffect(() => { answersRef.current = answers; }, [answers]);

  const [isSubmitting, setIsSubmitting] = useState(false);
  
  // 🚀 NẾU LÀ REVIEW MODE, ĐỔ LUÔN DỮ LIỆU CHẤM CŨ TỪ DATABASE VÀO MÀN HÌNH KẾT QUẢ
  const [gradeResult, setGradeResult] = useState<any>(() => {
      if (initIsReview && testData?.aiFeedback) {
          return testData.aiFeedback;
      }
      return null;
  });

  const [leftWidth, setLeftWidth] = useState(50); 
  const [paperViewMode, setPaperViewMode] = useState<'split' | 'text-only'>('split');
  const [isDragging, setIsDragging] = useState(false);
  const [isDesktop, setIsDesktop] = useState(() => typeof window !== 'undefined' ? window.innerWidth >= 768 : true);
  const [mobileTab, setMobileTab] = useState<'pdf' | 'answers'>(initIsReview ? 'answers' : 'pdf');
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const onResize = () => setIsDesktop(window.innerWidth >= 768);
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []);

  // 📎 Toggle PDF: Question Paper vs Insert 1 vs Insert 2
  const [leftPdfView, setLeftPdfView] = useState<'question' | 'insert' | 'insert2'>('question');
  const questionPdfUrl = testData?.insert_pdf_url || testData?.pdf_url || testData?.content_json?.basicInfo?.insert_pdf_url || null;
  const insertPdfUrl = testData?.resource_pdf_url || testData?.content_json?.basicInfo?.resource_pdf_url || null;
  const insert2PdfUrl = testData?.resource_pdf_url_2 || testData?.content_json?.basicInfo?.resource_pdf_url_2 || null;
  const hasInsertPdf = !!insertPdfUrl;
  const hasInsert2Pdf = !!insert2PdfUrl;
  const hasAnyInsert = hasInsertPdf || hasInsert2Pdf;

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

  // --- THUẬT TOÁN ĐỒNG HỒ ĐẾM NGƯỢC ---
  const [timeLeft, setTimeLeft] = useState(5400); 
  const isFinishingRef = useRef(false);

  const getSavedEndTime = (testId: string) => {
    if (!testId) return null;
    const saved = localStorage.getItem(`case_study_endtime_${testId}`);
    return saved ? parseInt(saved, 10) : null;
  };

  // TỰ ĐỘNG LƯU NHÁP
  useEffect(() => {
    if (testData?.id && !isFinishingRef.current && !gradeResult && !isReviewMode) {
      localStorage.setItem(`case_study_ans_${testData.id}`, JSON.stringify(answers));
    }
  }, [answers, testData?.id, gradeResult, isReviewMode]);

  // Khởi tạo thời gian thực cho bài thi — skip cho exercises
  useEffect(() => {
    if (testData && !isReviewMode) {
       const isExercise = testData.content_json?.basicInfo?.category === 'exercise';
       if (isExercise) {
           setTimeLeft(999999);
           setIsLoading(false);
           return;
       }
       const rawTime = testData.content_json?.basicInfo?.timeLimit || testData.timeLimit;
       const configuredTime = parseInt(rawTime) || 90;
       const initialSeconds = configuredTime * 60;

       let currentEndTime = getSavedEndTime(testData.id);
       if (!currentEndTime) {
           currentEndTime = Date.now() + initialSeconds * 1000;
           localStorage.setItem(`case_study_endtime_${testData.id}`, currentEndTime.toString());
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

  const handleAnswerChange = (inputId: string, value: string) => {
    if (isReviewMode) return;
    setAnswers(prev => ({ ...prev, [inputId]: value }));
  };

  const handleSubmit = async (forceAutoSubmit: any = false) => {
    const isForced = forceAutoSubmit === true;
    if (isFinishingRef.current || isSubmitting) return;
    const currentAnswers = answersRef.current;
    const isExerciseMode = testData?.content_json?.basicInfo?.category === 'exercise';
    if (!isForced && Object.keys(currentAnswers).length === 0) {
      alert(isEn ? "⚠️ You haven't filled in any answers yet!" : "⚠️ Bạn chưa điền câu trả lời nào cả!");
      return;
    }

    if (!isForced) {
      if (!isExerciseMode && timeLeft > 0 && !window.confirm(isEn ? "Are you sure you want to submit this exam?" : "Bạn có chắc chắn muốn nộp bài thi?")) {
        return; 
      }
      if (isExerciseMode && !window.confirm(isEn ? "Are you sure you want to submit this practice?" : "Bạn có chắc chắn muốn nộp bài tập?")) {
        return;
      }
    }

    const rawTime = testData.content_json?.basicInfo?.timeLimit || testData.timeLimit;
    const initialSeconds = (parseInt(rawTime) || 90) * 60;
    const savedEnd = testData?.id ? getSavedEndTime(testData.id) : null;
    const computedTimeSpent = savedEnd
      ? Math.max(0, initialSeconds - Math.max(0, Math.floor((savedEnd - Date.now()) / 1000)))
      : Math.max(0, initialSeconds - timeLeft);

    setIsSubmitting(true);
    isFinishingRef.current = true;

    try {
      // 🚀 AI đọc được PDF đề thi + Insert/Resource + JSON Marking Scheme
      const resolveUrl = (url: string | null) => {
        if (!url) return null;
        if (url.startsWith('http')) return url;
        return `${window.location.origin}${url.startsWith('/') ? '' : '/'}${url}`;
      };
      const fullPdfUrl = resolveUrl(questionPdfUrl);
      const fullInsertPdfUrl = resolveUrl(insertPdfUrl);
      const fullInsert2PdfUrl = resolveUrl(insert2PdfUrl);

      const { data, error } = await supabase.functions.invoke('igcse-grader', {
        body: { 
          testConfig: testData.json_config?.questions || [],
          textAnswers: currentAnswers,
          imageAnswers: [],
          pdfUrl: fullPdfUrl,
          insertPdfUrl: fullInsertPdfUrl,
          insertPdfUrl2: fullInsert2PdfUrl
        }
      });

      if (error) throw new Error((isEn ? "Server error: " : "Lỗi gọi Server: ") + error.message);
      if (data?.error) throw new Error((isEn ? "AI grading error: " : "Lỗi chấm điểm AI: ") + data.error);

      // igcse-grader trả về parsed object trực tiếp
      let gradedData;
      if (data.result && typeof data.result === 'object') {
        gradedData = data.result;
      } else {
        // Fallback: parse string (backward compatible)
        const cleanJson = (data.result || data.rawText || "").replace(/```json/gi, "").replace(/```/gi, "").trim();
        gradedData = JSON.parse(cleanJson);
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
      setMobileTab('answers');

      // 🚀 LƯU DB & BẮN PHÁO HIỆU CHO ADMIN
      try {
        const { data: { user } } = await supabase.auth.getSession().then(({data}) => ({ data: { user: data.session?.user } }));
        if (user) {
          await supabase.from('test_results').insert([{
            user_id: user.id,
            course_id: testData.course_id,
            test_title: testData.title || "Case Study Test",
            test_type: testData.test_type || 'Case-Study',
            score: gradedData.total_student_score,
            total_score: gradedData.total_max_score,
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

          // Bắn thông báo Activity
          await supabase.from('activity_logs').insert([{
            user_id: user.id,
            action_type: 'finish_test',
            details: { test_title: testData.title || "Case Study Test", score: gradedData.total_student_score, total: gradedData.total_max_score }
          }]);
        }
      } catch (dbError) {
        console.error("Lỗi lưu DB:", dbError);
      }

      // Chỉ xóa nháp sau khi chấm & lưu thành công
      if (testData?.id) {
         localStorage.removeItem(`case_study_endtime_${testData.id}`);
         localStorage.removeItem(`case_study_ans_${testData.id}`);
      }

    } catch (err: any) {
      isFinishingRef.current = false;
      if (err.message && err.message.includes("Unexpected end of JSON input")) {
        alert(isEn ? "❌ Could not submit due to an unstable connection or oversized PDF. Please try again." : "❌ Không thể nộp bài do kết nối gián đoạn hoặc file PDF quá nặng. Vui lòng thử nộp lại.");
      } else {
        console.error("Lỗi khi chấm bài:", err);
        alert((isEn ? "❌ An error occurred: " : "❌ Đã có lỗi xảy ra: ") + err.message);
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleSubmitRef = useRef(handleSubmit);
  handleSubmitRef.current = handleSubmit;

  // Đồng hồ chạy liên tục
  useEffect(() => {
    if (isLoading || !testData || gradeResult || isFinishingRef.current || isReviewMode) return;
    if (testData.content_json?.basicInfo?.category === 'exercise') return;
    
    const timer = setInterval(() => {
        const currentEndTime = getSavedEndTime(testData.id);
        if (currentEndTime) {
            const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
            setTimeLeft(remaining);
            if (remaining <= 0) {
                clearInterval(timer);
                alert(isEn ? "⏰ Time is up! Your exam is being submitted automatically." : "⏰ Hết giờ làm bài! Hệ thống tự động nộp bài.");
                handleSubmitRef.current(true);
            }
        } else {
            setTimeLeft(prev => {
                if (prev <= 1) {
                    clearInterval(timer);
                    alert(isEn ? "⏰ Time is up! Your exam is being submitted automatically." : "⏰ Hết giờ làm bài! Hệ thống tự động nộp bài.");
                    handleSubmitRef.current(true);
                    return 0;
                }
                return prev - 1;
            });
        }
    }, 1000);
    
    return () => clearInterval(timer);
  }, [isLoading, testData, gradeResult, isReviewMode]);

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!isDragging || !containerRef.current) return;
      const containerWidth = containerRef.current.getBoundingClientRect().width;
      const newLeftWidth = (e.clientX / containerWidth) * 100;
      if (newLeftWidth > 20 && newLeftWidth < 80) setLeftWidth(newLeftWidth);
    };
    const handleMouseUp = () => setIsDragging(false);
    if (isDragging) {
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('mouseup', handleMouseUp);
    }
    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, [isDragging]);

  const allQuestions = useMemo(() => {
    return testData?.json_config?.questions || testData?.content_json?.questions || [];
  }, [testData]);

  const hasRichPaper = useMemo(() => {
    return allQuestions.some(
      (q: any) =>
        Boolean(q?.stem_html) ||
        Boolean(q?.section_banner) ||
        (Array.isArray(q?.images) && q.images.length > 0)
    );
  }, [allQuestions]);

  const answeredQuestionCount = useMemo(() => {
    return allQuestions.filter((q: any) =>
      (q.inputs || []).some((_: any, i: number) => Boolean(answers[`${q.question_number}_input_${i}`]?.trim()))
    ).length;
  }, [allQuestions, answers]);

  if (isLoading) {
    return (
      <div className="h-[100dvh] w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold">
        <div className="animate-spin text-4xl mb-4">⏳</div>
        <p>{isEn ? 'Loading exam & documents...' : 'Đang tải đề thi và tài liệu...'}</p>
      </div>
    );
  }

  if (!testData || (!isReviewMode && (!testData.json_config || !testData.json_config.questions))) {
    return (
      <div className="h-[100dvh] w-screen flex flex-col items-center justify-center bg-[#525659] text-white font-bold gap-4">
        <p>{isEn ? '⚠️ Exam not found or configuration data is invalid.' : '⚠️ Chưa có đề thi nào trong hệ thống hoặc dữ liệu bị lỗi.'}</p>
        <button onClick={onBack} className="bg-[#1e88e5] text-white px-6 py-2 rounded-none">{isEn ? 'Back' : 'Quay lại'}</button>
      </div>
    );
  }

  const findStudentAnswer = (qn: any): string | null => {
    const qnStr = String(qn ?? '').trim();
    if (!qnStr) return null;
    const directKey = `${qnStr}_input_0`;
    if (answers[directKey]) return answers[directKey];
    if (answers[qnStr]) return answers[qnStr];
    const matchEntry = Object.entries(answers).find(([k]) => k === qnStr || k.startsWith(qnStr + '_'));
    return matchEntry?.[1] || null;
  };

  const activePdfUrl = leftPdfView === 'insert2' && insert2PdfUrl ? insert2PdfUrl 
    : leftPdfView === 'insert' && insertPdfUrl ? insertPdfUrl 
    : questionPdfUrl;

  // 🚀 GỌI GIA SƯ AI (VOICE) CHO TỪNG CÂU HỎI
  const callAiTutor = (questionText: string, studentAns: string, feedback: string) => {
      const tutorContext = {
          overall: 'Case Study Review',
          transcript: isEn
            ? `Question: "${questionText}". \nStudent answer: ${studentAns}. \nFeedback: "${feedback}".`
            : `Câu hỏi: "${questionText}". \nĐáp án của học sinh: ${studentAns}. \nNhận xét: "${feedback}".`,
          feedback: isEn
            ? "You are a Cambridge IGCSE tutor. The student is reviewing a Case Study question and needs help. Greet them warmly in English, walk through the question, explain why marks were lost, and break down the reasoning step by step."
            : "Bạn là gia sư Cambridge IGCSE. Học sinh đang xem lại bài Case Study và không hiểu câu này. Hãy chủ động chào, đọc câu hỏi và giải thích chi tiết tại sao điểm lại bị trừ, phân tích từng bước lập luận. Dùng giọng điệu ân cần, dễ hiểu."
      };
      sessionStorage.setItem('tony_live_mode', 'TUTOR');
      sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
      sessionStorage.setItem('tony_auto_start', 'true');
      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
  };

  const showPdfPane = !hasRichPaper || paperViewMode === 'split';

  const renderRichImages = (images?: Array<{ url: string; caption?: string; max_width?: number }>) => {
    if (!Array.isArray(images) || images.length === 0) return null;
    return (
      <div className="grid gap-3 my-3.5 grid-cols-1">
        {images.map((img, idx) => (
          <figure
            key={`${img.url}-${idx}`}
            className="group bg-white border border-slate-200 rounded-xl p-3 sm:p-4 shadow-xs hover:border-sky-300 hover:shadow-md transition-all text-center"
          >
            <img
              src={img.url}
              alt={img.caption || 'Cambridge Geography figure'}
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

  return (
    <div className="h-[100dvh] w-screen flex flex-col bg-white font-sans text-slate-900 overflow-hidden">
      <style>{`
        .geo-rich-stem { font-size: 14.5px; line-height: 1.65; color: #1e293b; }
        .geo-rich-stem p { margin: 0 0 0.55rem 0; }
        .geo-rich-stem p:last-child { margin-bottom: 0; }
        .geo-rich-stem .igcse-table-wrap { overflow-x: auto; margin: 0.75rem 0; }
        .geo-rich-stem .igcse-table-title { text-align: center; font-weight: 800; font-size: 13px; color: #0f172a; margin-bottom: 0.35rem; }
        .geo-rich-stem .igcse-table { width: auto; min-width: min(100%, 360px); margin: 0 auto; border-collapse: collapse; background: #ffffff; font-size: 13.5px; }
        .geo-rich-stem .igcse-table th, .geo-rich-stem .igcse-table td { border: 1px solid #94a3b8; padding: 0.45rem 0.85rem; text-align: center; vertical-align: middle; }
        .geo-rich-stem .igcse-table.igcse-table-left td:last-child { text-align: left; }
        .geo-rich-stem .igcse-table th { background: #f1f5f9; font-weight: 700; color: #0f172a; }
        .geo-rich-stem .igcse-hypothesis-box { background: #f0f9ff; border: 1px solid #bae6fd; border-left: 4px solid #0a5482; border-radius: 8px; padding: 0.7rem 1rem; margin: 0.6rem 0; }
        .geo-rich-stem .igcse-note-box { background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 0.85rem 1rem; margin: 0.65rem 0; }
        .geo-rich-stem .igcse-choice-pills { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0.4rem 0; }
        .geo-rich-stem .igcse-choice-pills span { padding: 0.3rem 0.85rem; border-radius: 999px; background: #ffffff; border: 1px solid #94a3b8; font-weight: 700; font-size: 13.5px; color: #0f172a; }
      `}</style>
      
      {/* HEADER TỔNG */}
      <header className="h-14 w-full bg-white border-b border-slate-300 flex items-center justify-between px-3 sm:px-6 shrink-0 z-20 box-border gap-2">
        <div className="flex items-center gap-2.5 sm:gap-4 overflow-hidden min-w-0">
          <button onClick={onBack} className="text-slate-600 hover:text-black font-bold text-sm transition-colors whitespace-nowrap">{isEn ? '← Back' : '← Quay lại'}</button>
          <div className="h-5 w-px bg-slate-300 hidden sm:block"></div>
          <div className="truncate flex items-baseline gap-2 min-w-0">
            <h1 className="font-bold text-black text-[14px] sm:text-[15px] leading-tight truncate">
              {isReviewMode ? `[REVIEW] ${testData.title || (isEn ? 'Case Study Exam' : 'Bài thi Case Study')}` : testData.title || (isEn ? 'Case Study Exam' : 'Bài thi Case Study')}
            </h1>
            {!isReviewMode && allQuestions.length > 0 && (
              <span className="text-xs text-slate-400 whitespace-nowrap hidden sm:inline">
                ({answeredQuestionCount}/{allQuestions.length} {isEn ? 'questions' : 'câu'})
              </span>
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
                title={isEn ? 'Show original PDF/Insert on the left alongside Text & Figures' : 'Xem song song PDF/Insert bên trái và Đề Text + Hình bên phải'}
              >
                📄|📝 <span className="hidden md:inline">{isEn ? 'Split PDF' : 'Song song'}</span>
              </button>
              <button
                type="button"
                onClick={() => setPaperViewMode('text-only')}
                className={`px-2 sm:px-2.5 py-1 rounded-md text-[11px] sm:text-xs font-bold transition-all whitespace-nowrap cursor-pointer ${paperViewMode === 'text-only' ? 'bg-[#0a5482] text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'}`}
                title={isEn ? 'Hide left PDF/Insert and work directly on Text + Figures paper' : 'Ẩn PDF/Insert bên trái — Chỉ làm trực tiếp trên bản Text + Hình'}
              >
                📝 <span className="hidden md:inline">{isEn ? 'Text + Figures' : 'Chỉ Text + Hình'}</span>
              </button>
            </div>
          )}
          <LmsLangToggle lang={lang} setLang={setLang} variant="light" />
          {!gradeResult && !isReviewMode && (
            <>
               <div className={`font-bold flex items-center gap-1.5 px-2.5 sm:px-3 py-1 rounded text-xs sm:text-sm ${testData.content_json?.basicInfo?.category === 'exercise' ? 'text-[#0ea5e9] bg-[#0ea5e9]/10' : (timeLeft <= 300 ? 'text-red-600 bg-red-50 animate-pulse' : 'text-slate-600 bg-slate-100')}`}>
                 {testData.content_json?.basicInfo?.category === 'exercise' ? (isEn ? 'PRACTICE' : 'BÀI TẬP') : <><span>⏱️</span> <span className="font-mono tracking-wider sm:tracking-widest tabular-nums">{formatTime(timeLeft)}</span></>}
               </div>
               <button 
                 onClick={() => handleSubmit(false)} 
                 disabled={isSubmitting}
                 className="bg-[#1e88e5] hover:bg-blue-700 text-white font-bold text-xs sm:text-sm px-4 sm:px-6 py-1.5 rounded-lg transition-colors active:scale-95 disabled:opacity-50 whitespace-nowrap"
               >
                 {isSubmitting ? (isEn ? 'Submitting...' : 'Đang nộp...') : (isEn ? 'Submit' : 'Nộp Bài')}
               </button>
            </>
          )}
        </div>
      </header>

      {/* MOBILE VIEW SWITCHER (< md) — hidden when PDF pane is hidden */}
      {showPdfPane && (
      <div className="md:hidden flex border-b border-slate-300 bg-slate-100 shrink-0 z-10">
        <button
          type="button"
          onClick={() => setMobileTab('pdf')}
          className={`flex-1 py-2.5 text-xs font-bold uppercase tracking-wider transition-colors border-b-2 ${mobileTab === 'pdf' ? 'bg-white text-[#1e88e5] border-[#1e88e5]' : 'text-slate-600 border-transparent'}`}
        >
          {isEn ? '📄 Question Paper' : '📄 Đề bài PDF'}
        </button>
        <button
          type="button"
          onClick={() => setMobileTab('answers')}
          className={`flex-1 py-2.5 text-xs font-bold uppercase tracking-wider transition-colors border-b-2 ${mobileTab === 'answers' ? 'bg-white text-[#1e88e5] border-[#1e88e5]' : 'text-slate-600 border-transparent'}`}
        >
          {gradeResult ? (isEn ? '✅ Results' : '✅ Kết quả') : hasRichPaper ? (isEn ? '📝 Text + Answers' : '📝 Đề Text & Bài làm') : (isEn ? '✏️ Answers' : '✏️ Bài làm')}
        </button>
      </div>
      )}

      {/* WORKSPACE - SPLIT SCREEN */}
      <div ref={containerRef} className={`flex-1 flex overflow-hidden w-full bg-[#525659] ${isDragging ? 'select-none' : ''}`}>
        
        {/* NỬA TRÁI: PDF HOẶC TEXT */}
        {showPdfPane && (
        <div
          style={{ width: isDesktop ? `${leftWidth}%` : '100%' }}
          className={`${!isDesktop && mobileTab !== 'pdf' ? 'hidden' : 'flex'} h-full flex-col shrink-0 bg-[#525659]`}
        >
          <div className="bg-[#323639] border-b border-[#202224] px-3 sm:px-4 flex justify-between items-center gap-2 h-10 shrink-0 shadow-sm overflow-x-auto no-scrollbar">
            {hasAnyInsert ? (
              <div className="flex items-center gap-1 shrink-0">
                <button 
                  onClick={() => setLeftPdfView('question')} 
                  className={`px-3 py-1.5 rounded text-[10px] font-bold uppercase tracking-wider transition-all ${leftPdfView === 'question' ? 'bg-[#1e88e5] text-white shadow-sm' : 'text-slate-400 hover:text-white hover:bg-white/10'}`}
                >
                  📝 Question Paper
                </button>
                {hasInsertPdf && (
                  <button 
                    onClick={() => setLeftPdfView('insert')} 
                    className={`px-3 py-1.5 rounded text-[10px] font-bold uppercase tracking-wider transition-all ${leftPdfView === 'insert' ? 'bg-amber-500 text-white shadow-sm' : 'text-slate-400 hover:text-white hover:bg-white/10'}`}
                  >
                    📎 Insert{hasInsert2Pdf ? ' 1' : ''}
                  </button>
                )}
                {hasInsert2Pdf && (
                  <button 
                    onClick={() => setLeftPdfView('insert2')} 
                    className={`px-3 py-1.5 rounded text-[10px] font-bold uppercase tracking-wider transition-all ${leftPdfView === 'insert2' ? 'bg-violet-500 text-white shadow-sm' : 'text-slate-400 hover:text-white hover:bg-white/10'}`}
                  >
                    📎 Insert 2
                  </button>
                )}
              </div>
            ) : (
              <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest shrink-0">{isEn ? 'Question Paper' : 'Đề thi'}</span>
            )}
            {activePdfUrl && !(leftPdfView === 'question' && testData?.content_json?.basicInfo?.leftPaneType === 'text') && (
              <a
                href={activePdfUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="px-2.5 py-1 rounded bg-white/10 hover:bg-white/20 text-slate-200 hover:text-white text-[11px] font-bold transition shrink-0 whitespace-nowrap"
                title={isEn ? "Open PDF in a new tab (recommended on iPad/Mobile)" : "Mở file PDF trong tab mới (khuyên dùng trên iPad/Mobile)"}
              >
                {isEn ? '↗ Open PDF' : '↗ Mở PDF'}
              </a>
            )}
          </div>
          <div className={`flex-1 w-full h-full overflow-hidden ${isDragging ? 'pointer-events-none' : ''}`}>
             {(() => {
               // Ưu tiên hiển thị text nếu đang xem Question Paper và có cấu hình text
               if (leftPdfView === 'question' && testData?.content_json?.basicInfo?.leftPaneType === 'text') {
                 return (
                   <div
                     className="w-full h-full bg-white overflow-y-auto p-6 sm:p-8 custom-scrollbar html-content-renderer"
                     onClick={(e) => {
                       const lb = extractLightboxFromClick(e, e.currentTarget);
                       if (lb) setImageLightbox(lb);
                     }}
                   >
                     <div 
                       className="prose max-w-none prose-slate"
                       dangerouslySetInnerHTML={{ __html: testData.content_json.basicInfo.left_text_content || '' }}
                     />
                   </div>
                 );
               }

               if (activePdfUrl) {
                 return <iframe key={activePdfUrl} src={`${activePdfUrl}#toolbar=0&navpanes=0&scrollbar=0&view=FitH`} className="w-full h-full border-none bg-transparent" title={leftPdfView === 'insert2' ? 'PDF Insert 2' : leftPdfView === 'insert' ? 'PDF Insert 1' : 'PDF Question Paper'} />;
               }
               return <div className="flex flex-col items-center justify-center h-full text-slate-400 p-8 text-center bg-[#525659]">📄<p className="font-bold">{isEn ? 'No document attached.' : 'Không có tài liệu đính kèm.'}</p></div>;
             })()}
          </div>
        </div>
        )}

        {/* THANH KÉO (RESIZER - Desktop only) */}
        {showPdfPane && (
        <div onMouseDown={() => setIsDragging(true)} className={`hidden md:flex w-[6px] h-full bg-[#202224] hover:bg-[#1e88e5] cursor-col-resize items-center justify-center shrink-0 z-10 transition-colors ${isDragging ? 'bg-[#1e88e5]' : ''}`}>
          <div className="flex flex-col gap-1">
            <div className="w-[2px] h-[2px] bg-slate-500"></div><div className="w-[2px] h-[2px] bg-slate-500"></div><div className="w-[2px] h-[2px] bg-slate-500"></div>
          </div>
        </div>
        )}

        {/* NỬA PHẢI: KHU VỰC LÀM BÀI / KẾT QUẢ CHẤM */}
        <div
          style={{ width: isDesktop ? (showPdfPane ? `calc(${100 - leftWidth}% - 6px)` : '100%') : '100%' }}
          className={`${!isDesktop && showPdfPane && mobileTab !== 'answers' ? 'hidden' : 'flex'} h-full flex-col shrink-0 ${hasRichPaper ? 'bg-[#f1f5f9]' : 'bg-[#525659]'}`}
        >
          
          <div className="bg-[#323639] border-b border-[#202224] px-4 sm:px-6 flex justify-between items-center h-10 shrink-0 shadow-sm gap-2">
            <div className="flex items-center gap-2 min-w-0">
              <span className="font-bold text-slate-300 text-[11px] uppercase tracking-widest flex items-center gap-2 truncate">
                {gradeResult ? (
                  <><span>✅</span> {isEn ? 'AI Grading Results' : 'Kết quả chấm điểm AI'}</>
                ) : hasRichPaper ? (
                  <><span className="w-1.5 h-1.5 rounded-full bg-sky-400 animate-pulse shrink-0"></span> {isEn ? 'Structured Paper (Text + Figures)' : 'Đề Text + Hình & Phiếu trả lời'}</>
                ) : (
                  <><span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse shrink-0"></span> {isEn ? 'Answer Workspace' : 'Khu vực làm bài'}</>
                )}
              </span>
              {hasRichPaper && !showPdfPane && questionPdfUrl && (
                <a
                  href={questionPdfUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-2 py-0.5 rounded bg-white/10 hover:bg-white/20 text-slate-200 hover:text-white text-[11px] font-bold transition whitespace-nowrap shrink-0"
                  title={isEn ? 'Open Question Paper PDF in a new tab' : 'Mở PDF đề gốc trong tab mới'}
                >
                  ↗ {isEn ? 'QP PDF' : 'PDF đề'}
                </a>
              )}
              {hasRichPaper && !showPdfPane && insertPdfUrl && (
                <a
                  href={insertPdfUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/35 text-amber-200 hover:text-white text-[11px] font-bold transition whitespace-nowrap shrink-0"
                  title={isEn ? 'Open Insert PDF in a new tab' : 'Mở Insert PDF trong tab mới'}
                >
                  📎 Insert{hasInsert2Pdf ? ' 1' : ''}
                </a>
              )}
              {hasRichPaper && !showPdfPane && insert2PdfUrl && (
                <a
                  href={insert2PdfUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-2 py-0.5 rounded bg-violet-500/20 hover:bg-violet-500/35 text-violet-200 hover:text-white text-[11px] font-bold transition whitespace-nowrap shrink-0"
                  title={isEn ? 'Open Insert 2 (Survey Map) PDF in a new tab' : 'Mở Insert 2 (Bản đồ) trong tab mới'}
                >
                  📎 Insert 2
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

          {/* Sticky Question Jump Bar for Rich Geography Papers */}
          {hasRichPaper && !gradeResult && allQuestions.length > 1 && (
            <div className="bg-white border-b border-slate-200 px-4 sm:px-6 py-2 flex items-center justify-between gap-3 shrink-0 overflow-x-auto no-scrollbar">
              <div className="flex items-center gap-1.5 shrink-0">
                <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider mr-1 hidden sm:inline">
                  {isEn ? 'Jump:' : 'Câu:'}
                </span>
                {allQuestions.map((q: any, qIdx: number) => {
                  const isDone = (q.inputs || []).some((_: any, i: number) => Boolean(answers[`${q.question_number}_input_${i}`]?.trim()));
                  return (
                    <button
                      key={`geo-jump-${qIdx}`}
                      type="button"
                      onClick={() => {
                        document.getElementById(`geo-question-${qIdx}`)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
                      }}
                      className={`px-2 py-0.5 rounded-md text-[11.5px] font-extrabold border transition-all cursor-pointer whitespace-nowrap ${
                        isDone
                          ? 'bg-emerald-50 text-emerald-700 border-emerald-300 hover:bg-emerald-100'
                          : 'bg-slate-50 text-slate-600 border-slate-200 hover:border-slate-400 hover:text-slate-900'
                      }`}
                      title={`Question ${q.question_number} [${q.total_marks}m]`}
                    >
                      {q.question_number}
                      {isDone && <span className="ml-0.5 text-[10px]">✓</span>}
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
            className={`flex-1 overflow-y-auto p-4 sm:p-5 ${isDragging ? 'pointer-events-none' : ''}`}
            onClick={(e) => {
              const lb = extractLightboxFromClick(e, e.currentTarget);
              if (lb) setImageLightbox(lb);
            }}
          >
            
            {/* 1. NẾU ĐÃ CHẤM XONG HOẶC LÀ REVIEW MODE -> HIỂN THỊ KẾT QUẢ */}
            {gradeResult ? (
              <div className={`w-full bg-white shadow-xl mb-5 px-6 py-12 sm:px-16 sm:py-16 min-h-[85vh] ${!showPdfPane ? 'max-w-4xl mx-auto rounded-xl' : ''}`}>
                <div className="border-b-4 border-black pb-8 mb-10 text-center">
                  <h2 className="text-3xl font-black text-black mb-3">{isEn ? 'AI Grading Results' : 'Kết Quả Chấm Điểm (AI)'}</h2>
                  <div className="text-6xl font-black text-[#1e88e5] mb-6">
                    {gradeResult.total_student_score} <span className="text-3xl text-slate-400">/ {gradeResult.total_max_score}</span>
                  </div>
                  <p className="text-[16px] text-slate-700 italic bg-slate-100 p-6 border-l-4 border-[#1e88e5] text-left">
                    <span className="font-bold not-italic block mb-2 text-black uppercase text-sm">{isEn ? 'Overall Feedback:' : 'Nhận xét tổng quan:'}</span>
                    {gradeResult.general_feedback}
                  </p>
                </div>

                <div className="space-y-10">
                  {(gradeResult.details || []).map((item: any, idx: number) => (
                    <div key={idx} className="border border-slate-300 p-6 sm:p-8 shadow-sm relative">
                      <div className="flex justify-between items-center mb-6 border-b border-slate-200 pb-4">
                        <h4 className="font-black text-xl text-black">{isEn ? `Question ${item.question_number}` : `Câu ${item.question_number}`}</h4>
                        <span className={`font-black px-4 py-2 text-[15px] ${item.student_score === item.max_score ? 'bg-emerald-100 text-emerald-700 border border-emerald-300' : item.student_score === 0 ? 'bg-red-100 text-red-700 border border-red-300' : 'bg-orange-100 text-orange-700 border border-orange-300'}`}>
                          {isEn ? 'Score:' : 'Đạt:'} {item.student_score} / {item.max_score}
                        </span>
                      </div>
                      
                      <div className="mb-4">
                         <span className="font-bold text-slate-500 uppercase text-[11px] tracking-widest block mb-2">{isEn ? 'Your Answer:' : 'Bài làm của bạn:'}</span>
                         <div className="bg-slate-50 p-4 border border-slate-200 text-[14px] text-slate-600 italic whitespace-pre-wrap">
                            {findStudentAnswer(item.question_number || item.id) || (isEn ? "No answer provided..." : "Không có câu trả lời...")}
                         </div>
                      </div>

                      <div>
                        <span className="font-bold text-[#0a5482] uppercase text-[11px] tracking-widest block mb-2">Examiner Feedback:</span>
                        <p className="text-[15px] text-black leading-relaxed whitespace-pre-wrap font-medium">
                          {item.examiner_comment}
                        </p>
                      </div>

                      {item.correct_answer && (
                        <div className="mt-4 bg-white p-3 rounded border border-slate-200 text-[13px]">
                          <span className="font-bold text-slate-500 uppercase text-[10px] tracking-widest block mb-1">{isEn ? 'Correct Answer (Cambridge MS):' : 'Đáp án đúng (Cambridge MS):'}</span>
                          <span className="font-medium text-emerald-600 whitespace-pre-wrap">{item.correct_answer}</span>
                        </div>
                      )}

                      {item.student_score < item.max_score && (
                        <div className="flex items-center gap-2 mt-5">
                          <button onClick={() => {
                              const qn = item.question_number || item.id || '';
                              const studentAns = findStudentAnswer(qn) || (isEn ? 'Blank' : 'Bỏ trống');
                              const query = isEn
                                ? `Question ${qn}\nStudent answer: "${studentAns}"\nScore: ${item.student_score}/${item.max_score}\nFeedback: "${item.examiner_comment}"${item.correct_answer ? `\nCorrect answer: "${item.correct_answer}"` : ''}\n\nPlease explain in detail in English why marks were deducted!`
                                : `Câu hỏi số ${qn}\nĐáp án học sinh: "${studentAns}"\nĐiểm: ${item.student_score}/${item.max_score}\nNhận xét: "${item.examiner_comment}"${item.correct_answer ? `\nĐáp án đúng: "${item.correct_answer}"` : ''}\n\nThầy giải thích chi tiết giúp em tại sao em bị trừ điểm ạ!`;
                              const btn = document.createElement('button');
                              btn.className = 'btn-ai-trigger';
                              btn.setAttribute('data-topic', query);
                              btn.setAttribute('data-task', 'reading');
                              document.body.appendChild(btn);
                              btn.click();
                              document.body.removeChild(btn);
                          }} className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-blue-500 to-cyan-500 text-white font-bold text-[12px] rounded-lg shadow-md hover:shadow-lg transition-all active:scale-95">
                              {isEn ? '💬 Ask AI Tutor' : '💬 Chat Thầy AI'}
                          </button>
                          <button onClick={() => {
                              const qn = item.question_number || item.id || '';
                              const studentAns = findStudentAnswer(qn) || (isEn ? 'Blank' : 'Bỏ trống');
                              callAiTutor(isEn ? `Question ${qn}` : `Câu ${qn}`, studentAns, item.examiner_comment || '');
                          }} className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-amber-400 to-orange-400 text-white font-bold text-[12px] rounded-lg shadow-md hover:shadow-lg transition-all active:scale-95">
                              {isEn ? '📞 Call AI Tutor' : '📞 Gọi Gia Sư'}
                          </button>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
                
                {!initIsReview && (
                  <div className="mt-12 flex justify-center">
                    <button onClick={() => {
                        setGradeResult(null);
                        setIsReviewMode(false);
                        if (testData?.id) {
                           localStorage.removeItem(`case_study_ans_${testData.id}`);
                           const rawTime = testData.content_json?.basicInfo?.timeLimit || testData.timeLimit;
                           const initialSeconds = (parseInt(rawTime) || 90) * 60;
                           const newEndTime = Date.now() + initialSeconds * 1000;
                           localStorage.setItem(`case_study_endtime_${testData.id}`, newEndTime.toString());
                           setTimeLeft(initialSeconds);
                        }
                        setAnswers({});
                        isFinishingRef.current = false;
                    }} className="border-2 border-black hover:bg-slate-100 text-black font-bold px-10 py-3 transition-colors">
                      {isEn ? 'Retake Exam' : 'Làm lại bài thi'}
                    </button>
                  </div>
                )}
              </div>
            ) : (
              /* 2. NẾU CHƯA CHẤM -> HIỂN THỊ KHUNG LÀM BÀI */
              <div className={!showPdfPane ? 'max-w-4xl mx-auto' : ''}>
                {allQuestions.map((q: any, index: number) => {
                  const hasQRich = Boolean(q?.stem_html) || Boolean(q?.section_banner) || (Array.isArray(q?.images) && q.images.length > 0);
                  if (hasRichPaper) {
                    return (
                      <div key={index} id={`geo-question-${index}`} className="scroll-mt-4 mb-6">
                        {q.section_banner && (
                          <div className="bg-gradient-to-r from-[#0a5482] to-[#0f6ea8] text-white px-5 py-3 rounded-t-xl font-extrabold text-[14px] sm:text-[15px] tracking-wide shadow-xs flex items-center gap-2">
                            <span>🌍</span>
                            <span>{q.section_banner}</span>
                          </div>
                        )}
                        <div className={`w-full bg-white shadow-sm border border-slate-200 p-5 sm:p-7 ${q.section_banner ? 'rounded-b-xl border-t-0' : 'rounded-xl'}`}>
                          <div className="flex flex-wrap items-center justify-between gap-2 pb-3 mb-4 border-b border-slate-100">
                            <div className="flex items-center gap-2 flex-wrap">
                              <span className="inline-flex items-center justify-center px-2.5 py-0.5 rounded-md bg-slate-900 text-white font-black text-[13px]">
                                {q.question_number}
                              </span>
                              {q.page_ref && (
                                <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-slate-100 text-slate-500 border border-slate-200 text-[11px] font-bold">
                                  📄 {q.page_ref}
                                </span>
                              )}
                            </div>
                            <span className="text-[12px] font-bold text-[#0a5482] bg-sky-50 border border-sky-200 px-2.5 py-0.5 rounded-full whitespace-nowrap">
                              [{q.total_marks} {Number(q.total_marks) === 1 ? 'mark' : 'marks'}]
                            </span>
                          </div>

                          {hasQRich && (q.stem_html || (Array.isArray(q.images) && q.images.length > 0)) && (
                            <div className="mb-5 bg-slate-50/80 border border-slate-200/80 rounded-xl p-4 sm:p-5">
                              {q.stem_html && (
                                <div className="geo-rich-stem" dangerouslySetInnerHTML={{ __html: q.stem_html }} />
                              )}
                              {renderRichImages(q.images)}
                            </div>
                          )}

                          <div className="mb-4">
                            <h3 className="font-semibold text-slate-900 text-[15px] sm:text-[15.5px] leading-relaxed whitespace-pre-wrap">
                              {q.question_text}
                            </h3>
                          </div>

                          <div className="space-y-4">
                            {(q.inputs || []).map((input: any, i: number) => {
                              const inputId = `${q.question_number}_input_${i}`;
                              const minH = Number(q.total_marks) <= 2 ? 'min-h-[84px]' : 'min-h-[124px]';
                              return (
                                <div key={inputId} className="space-y-1.5">
                                  {input.label && (
                                    <label className="block text-[13px] font-bold text-slate-600">{input.label}</label>
                                  )}
                                  <textarea
                                    value={answers[inputId] || ''}
                                    onChange={(e) => handleAnswerChange(inputId, e.target.value)}
                                    disabled={isReviewMode}
                                    placeholder={isEn ? 'Write your answer here...' : 'Nhập câu trả lời của bạn...'}
                                    className={`w-full border border-slate-300 rounded-lg p-3.5 ${minH} text-[14.5px] text-slate-900 leading-relaxed outline-none focus:border-[#0a5482] focus:ring-2 focus:ring-[#0a5482]/15 transition-all resize-y bg-white disabled:bg-slate-50`}
                                  />
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      </div>
                    );
                  }

                  return (
                    <div key={index} className="w-full bg-white shadow-xl mb-5 px-6 py-12 sm:px-16 sm:py-20 min-h-[85vh]">
                      <div className="flex gap-3 mb-8 items-baseline">
                        <div className="font-bold text-black text-[16px] sm:text-[18px] min-w-[30px]">{q.question_number}</div>
                        <div className="flex-1">
                          <h3 className="font-medium text-black text-[15px] sm:text-[16px] leading-relaxed inline whitespace-pre-wrap">{q.question_text}</h3>
                          <span className="inline-block text-slate-500 text-[12px] font-bold ml-2 uppercase tracking-wider">[{q.total_marks} marks]</span>
                        </div>
                      </div>
                      <div className="space-y-8 pl-0 sm:pl-[42px]">
                        {(q.inputs || []).map((input: any, i: number) => {
                          const inputId = `${q.question_number}_input_${i}`;
                          return (
                            <div key={inputId} className="space-y-2">
                              <label className="block text-[14px] font-semibold text-black">{input.label}</label>
                              <textarea
                                value={answers[inputId] || ''}
                                onChange={(e) => handleAnswerChange(inputId, e.target.value)}
                                disabled={isReviewMode}
                                className="w-full border border-slate-400 rounded-none p-4 min-h-[120px] text-[15px] text-black leading-relaxed outline-none focus:border-[#1e88e5] focus:ring-1 focus:ring-[#1e88e5] transition-all resize-y bg-transparent disabled:bg-slate-50"
                              />
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  );
                })}
                
                {!isReviewMode && (
                  <div className={`w-full bg-white ${hasRichPaper ? 'rounded-xl shadow-sm border border-slate-200 px-6 py-5' : 'shadow-xl px-8 py-8 sm:px-16 border-t border-slate-100'} flex justify-end mb-12`}>
                     <button 
                       onClick={() => handleSubmit(false)} 
                       disabled={isSubmitting}
                       className={`bg-[#0a5482] hover:bg-[#084266] text-white font-bold px-10 py-3 ${hasRichPaper ? 'rounded-lg' : 'rounded-none'} transition-transform active:scale-95 flex items-center gap-2 shadow-md disabled:opacity-50 cursor-pointer`}
                     >
                       {isSubmitting ? (isEn ? 'AI is grading...' : 'AI đang chấm bài...') : (isExercise ? (isEn ? 'Finish & Submit Practice' : 'Hoàn tất & Nộp bài tập') : (isEn ? 'Finish & Submit Exam' : 'Hoàn tất & Nộp bài thi'))}
                     </button>
                  </div>
                )}
              </div>
            )}

          </div>
        </div>

      </div>
      <ImageLightboxModal
        items={imageLightbox?.items || null}
        initialIndex={imageLightbox?.index ?? 0}
        onClose={() => setImageLightbox(null)}
      />
    </div>
  );
}