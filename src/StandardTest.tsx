import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';
import './tailwind.css';

// =========================================================================================
// BỘ ICON CHUẨN IDP
// =========================================================================================
const UserIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
    <path fillRule="evenodd" d="M7.5 6a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM3.751 20.105a8.25 8.25 0 0116.498 0 .75.75 0 01-.437.695A18.683 18.683 0 0112 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 01-.437-.695z" clipRule="evenodd" />
  </svg>
);

const SettingsIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
    <path fillRule="evenodd" d="M11.078 2.25c-.917 0-1.699.663-1.85 1.567L9.05 4.889c-.02.12-.115.26-.297.348a7.493 7.493 0 00-.986.57c-.166.115-.334.126-.45.083L6.3 5.508a1.875 1.875 0 00-2.282.819l-.922 1.597a1.875 1.875 0 00.432 2.385l.84.692c.097.078.15.222.15.399v.111c0 .177-.053.321-.15.399l-.84.692a1.875 1.875 0 00-.432 2.385l.922 1.597a1.875 1.875 0 002.282.818l1.019-.382c.115-.043.283-.031.45.082.312.214.641.405.985.57.182.088.277.228.297.35l.178 1.071c.151.904.933 1.567 1.85 1.567h1.844c.916 0 1.699-.663 1.85-1.567l.178-1.072c.02-.12.114-.26.297-.349.344-.165.673-.356.985-.57.167-.114.335-.125.45-.082l1.02.382a1.875 1.875 0 002.28-.819l.923-1.597a1.875 1.875 0 00-.432-2.385l-.84-.692c-.098-.078-.15-.222-.15-.399v-.111c0-.177.052-.321.15-.399l.84-.692a1.875 1.875 0 00.432-2.385l-.923-1.597a1.875 1.875 0 00-2.28-.818l-1.02.382c-.114.043-.282.031-.449-.083a7.49 7.49 0 00-.985-.57c-.183-.087-.277-.227-.297-.348l-.179-1.072a1.875 1.875 0 00-1.85-1.567h-1.843zM12 15.75a3.75 3.75 0 110-7.5 3.75 3.75 0 010 7.5z" clipRule="evenodd" />
  </svg>
);

const FullscreenIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5">
    <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" />
  </svg>
);

const ExitFullscreenIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5">
    <path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" />
  </svg>
);

const BookmarkIcon = ({ filled }: { filled?: boolean }) => (
  <svg xmlns="http://www.w3.org/2000/svg" fill={filled ? "currentColor" : "none"} viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
    <path strokeLinecap="round" strokeLinejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
  </svg>
);

// =========================================================================================
// CÁC HÀM TIỆN ÍCH (UTILITIES)
// =========================================================================================
const stripHtmlRegex = /[<][^>]*[>]/g;

const cleanHtmlContent = (html: any) => {
  if (!html) return '';
  return String(html).replace(/style\s*=\s*(['"])(.*?)\1/gi, (match, quote, styleContent) => {
      let newStyle = styleContent
          .replace(/(?:^|;)\s*(max-height|min-height|height|overflow|overflow-y|overflow-x)\s*:[^;]+/gi, '')
          .replace(/^;+|;+$/g, '')
          .trim();
      if (newStyle) {
          return `style=${quote}${newStyle}${quote}`;
      }
      return '';
  });
};

const isRealContent = (htmlContent: any) => {
  const str = String(htmlContent || '');
  const rawText = str.replace(stripHtmlRegex, '').replace(/&nbsp;/gi, '').replace(/\s+/g, '');
  if (rawText !== '') return true;
  if (str.includes('<img')) return true;
  if (str.includes('<audio')) return true;
  return false;
};

const buildCheckboxCombos = (questions: any[]) => {
  const combos: any[][] = [];
  const safeQuestions = Array.isArray(questions) ? questions : [];

  safeQuestions.forEach((q: any) => {
    if (combos.length === 0) {
      combos.push([q]); 
      return;
    }
    
    const prevQ = combos[combos.length - 1][0];
    const contentEmpty = !isRealContent(q.content);
    
    const getOptStr = (qq: any) => {
        const opts = qq.options || [];
        return JSON.stringify(opts.map((o:any) => String(o).replace(stripHtmlRegex, '').trim()).filter(Boolean));
    };

    const currOpts = getOptStr(q);
    const prevOpts = getOptStr(prevQ);
    const hasSameOptions = currOpts === prevOpts && currOpts !== '[]';
    const hasNoOptions = currOpts === '[]';
    
    const normalizeText = (text: string) => {
        return String(text || '')
            .replace(stripHtmlRegex, '')
            .replace(/\(\d+\)|\[\d+\]|\d+\./g, '')
            .trim()
            .toLowerCase();
    };

    const currText = normalizeText(q.content);
    const prevText = normalizeText(prevQ.content);
    const hasSameContent = currText === prevText && currText !== '';

    if (contentEmpty || hasSameOptions || hasNoOptions || hasSameContent) {
        combos[combos.length - 1].push(q);
    } else {
        combos.push([q]); 
    }
  });

  return combos;
};

const isAnswerCorrect = (userAns: string, correctAns: string) => {
  if (!userAns || !correctAns) return false;
  
  const u = String(userAns).trim().toUpperCase().replace(/\s+/g, ' ');
  const cArr = String(correctAns).split('/').map(x => x.trim().toUpperCase().replace(/\s+/g, ' '));
  
  for (const c of cArr) {
    if (u === c) return true;
    
    const uMatch = u.match(/^([A-Z])[\.\):]\s*(.*)$/);
    if (uMatch) {
      if (uMatch[1] === c) return true;
      if (uMatch[2] === c) return true;
    }
    
    const cMatch = c.match(/^([A-Z])[\.\):]\s*(.*)$/);
    if (cMatch) {
      if (u === cMatch[1]) return true;
      if (u === cMatch[2]) return true;
    }

    if (c.includes('(') && c.includes(')')) {
      const withoutParens = c.replace(/\(.*?\)/g, '').replace(/\s+/g, ' ').trim();
      const withParensContent = c.replace(/[\(\)]/g, '').replace(/\s+/g, ' ').trim();
      
      if (u === withoutParens || u === withParensContent) return true;
      if (uMatch && (uMatch[2] === withoutParens || uMatch[2] === withParensContent)) return true;
    }
  }
  return false;
};

// =========================================================================================
// COMPONENT CHÍNH QUẢN LÝ BÀI THI STANDARD TEST
// =========================================================================================
export default function StandardTest({ 
    onBack, 
    testData, 
    onFinish 
}: { 
    onBack: () => void, 
    testData: any, 
    onFinish: (res: any) => void 
}) {
  
  // Xử lý an toàn dữ liệu đầu vào
  let safeData = testData || {};
  if (typeof safeData === 'string') {
    try { 
        safeData = JSON.parse(safeData); 
    } catch (e) { 
        safeData = {}; 
    }
  }

  let contentJSON = safeData?.content_json || safeData || {};
  if (typeof contentJSON === 'string') {
    try { 
        contentJSON = JSON.parse(contentJSON); 
    } catch (e) { 
        contentJSON = {}; 
    }
  }

  const basicInfo = contentJSON?.basicInfo || { title: "Standard Test", timeLimit: "60", skill: "" };
  const parts = Array.isArray(contentJSON?.parts) ? contentJSON.parts : [];
  
  const isListening = String(basicInfo.skill || safeData?.test_type || '').toLowerCase().includes('listening');
  const globalAudio = basicInfo.audioUrl || parts[0]?.audioUrl;

  const hasAnyAudio = useMemo(() => {
    let flag = !!globalAudio;
    if (!flag) {
      parts?.forEach((p: any) => {
        if (p?.audioUrl) {
            flag = true;
        }
        p?.sections?.forEach((s: any) => {
          if (s?.audioUrl) {
              flag = true;
          }
          s?.questions?.forEach((q: any) => { 
              if (q?.audioUrl) {
                  flag = true; 
              }
          });
        });
      });
    }
    return flag;
  }, [parts, globalAudio]);

  // 🚀 TỰ ĐỘNG KÍCH HOẠT REVIEW MODE NẾU NHẬN ĐƯỢC TÍN HIỆU TỪ STUDENT PORTAL
  const initIsReview = !!safeData?.isReview;
  const [testStarted, setTestStarted] = useState(initIsReview);
  const [isReviewMode, setIsReviewMode] = useState(initIsReview);
  const [scoreResult, setScoreResult] = useState({ 
      score: parseInt(safeData?.past_score || 0), 
      total: parseInt(safeData?.past_total || 0) 
  });
  
  const [showPalette, setShowPalette] = useState(false); 
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [showSettings, setShowSettings] = useState(false);
  const [fontSize, setFontSize] = useState<'S' | 'M' | 'L'>('M');
  
  const globalAudioRef = useRef<HTMLAudioElement>(null);
  const isFinishingRef = useRef(false);

  const [leftWidth, setLeftWidth] = useState(50); 
  const containerRef = useRef<HTMLDivElement>(null);
  const leftPaneRef = useRef<HTMLDivElement>(null);
  const rightPaneRef = useRef<HTMLDivElement>(null);

  // Xử lý Fullscreen
  useEffect(() => {
    const handleFullscreenChange = () => {
        setIsFullscreen(!!document.fullscreenElement);
    };
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    return () => {
        document.removeEventListener('fullscreenchange', handleFullscreenChange);
    };
  }, []);

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => console.error(err));
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
  };

  const handleExit = () => {
    if (document.fullscreenElement) {
        document.exitFullscreen().catch(() => {});
    }
    onBack();
  };

  // Kéo thả phân trang (Resizer - Chỉ dùng cho Reading)
  const handleMouseDown = (e: React.MouseEvent) => {
    if (isListening) return; // Không kéo thả ở giao diện Listening 1 cột
    e.preventDefault();
    document.body.style.cursor = 'col-resize';
    document.body.style.userSelect = 'none'; 
    
    const handleMouseMove = (moveEvent: MouseEvent) => {
      if (!containerRef.current || !leftPaneRef.current || !rightPaneRef.current) return;
      
      const containerRect = containerRef.current.getBoundingClientRect();
      const newWidth = ((moveEvent.clientX - containerRect.left) / containerRect.width) * 100;
      
      if (newWidth >= 25 && newWidth <= 75) {
        leftPaneRef.current.style.width = `${newWidth}%`;
        rightPaneRef.current.style.width = `${100 - newWidth}%`;
      }
    };

    const handleMouseUp = (upEvent: MouseEvent) => {
      document.body.style.cursor = 'default';
      document.body.style.userSelect = 'auto';
      
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);

      if (!containerRef.current) return;
      
      const containerRect = containerRef.current.getBoundingClientRect();
      let finalWidth = ((upEvent.clientX - containerRect.left) / containerRect.width) * 100;
      
      if (finalWidth < 25) finalWidth = 25;
      if (finalWidth > 75) finalWidth = 75;
      setLeftWidth(finalWidth);
    };

    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);
  };

  // ĐỔ BÊ TÔNG ĐÁP ÁN
  const [answers, setAnswers] = useState<Record<string, string>>(() => {
    if (initIsReview && safeData?.past_answers) {
        return safeData.past_answers;
    }
    try {
      const saved = localStorage.getItem(`std_ans_${safeData?.id}`);
      return saved ? JSON.parse(saved) : {};
    } catch (e) { 
        return {}; 
    }
  });

  const [marked, setMarked] = useState<Record<string, boolean>>(() => {
    try {
      const saved = localStorage.getItem(`standard_mark_${safeData?.id}`);
      return saved ? JSON.parse(saved) : {};
    } catch (e) { 
        return {}; 
    }
  });

  // Tự động lưu nháp
  useEffect(() => {
    if (!isReviewMode && !isFinishingRef.current && safeData?.id) {
      localStorage.setItem(`std_ans_${safeData.id}`, JSON.stringify(answers));
      localStorage.setItem(`standard_mark_${safeData.id}`, JSON.stringify(marked));
    }
  }, [answers, marked, safeData?.id, isReviewMode]);

  const handleAnswer = (qId: string, val: string) => { 
    if(!isReviewMode) {
        setAnswers(prev => ({ ...prev, [qId]: String(val) })); 
    }
  };
  
  const toggleMark = (qId: string) => { 
    if(!isReviewMode) {
        setMarked(prev => ({ ...prev, [qId]: !prev[qId] })); 
    }
  };

// NỘP BÀI VÀ TÍNH ĐIỂM
const handleFinish = async () => {
  if (!isReviewMode) {
    if (!window.confirm("Bạn có chắc chắn muốn nộp bài?")) {
        return;
    }
    
    isFinishingRef.current = true;
    if (safeData?.id) {
      localStorage.removeItem(`std_ans_${safeData.id}`);
      localStorage.removeItem(`standard_mark_${safeData.id}`);
      localStorage.removeItem(`standard_endtime_${safeData.id}`);
    }

    let score = 0; 
    let total = 0;
    let questionTypeStats: Record<string, { correct: number, total: number }> = {};

    parts?.forEach((p: any) => {
      p?.sections?.forEach((s: any) => {
        const qType = s.questionType || 'Khác';
        if (!questionTypeStats[qType]) {
            questionTypeStats[qType] = { correct: 0, total: 0 };
        }

        if (qType === 'Checkbox') {
           const combos: any[][] = [];
           
           s.questions?.forEach((q: any) => {
               const rawText = String(q.content || '').replace(/<[^>]*>/g, '').trim();
               const hasRealContent = rawText !== '' || String(q.content || '').includes('<img') || String(q.content || '').includes('<audio');
               if (combos.length === 0 || hasRealContent) {
                   combos.push([q]);
               } else {
                   combos[combos.length - 1].push(q);
               }
           });

           combos.forEach(combo => {
               const comboIds = combo.map((q: any) => String(q.id));
               const userAnsComboSet = new Set(
                   comboIds.map(id => answers[id])
                           .filter(v => v && v.trim() !== '')
                           .flatMap(x => x.split(',').map(v => v.trim().toUpperCase()))
               );
               
               const correctAnsComboSet = new Set(
                   combo.flatMap((q:any) => String(q.correctAnswer).split(',').map((x:string) => x.trim().toUpperCase()).filter(Boolean))
               );
               
               let comboPoints = 0;
               userAnsComboSet.forEach(ans => { 
                   if (correctAnsComboSet.has(ans)) {
                       comboPoints++; 
                   }
               });
               comboPoints = Math.min(comboPoints, combo.length); 
               
               score += comboPoints;
               total += combo.length;
               questionTypeStats[qType].correct += comboPoints;
               questionTypeStats[qType].total += combo.length;
           });

        } else {
           s?.questions?.forEach((q: any) => {
             if (!q?.id) return;
             total++; 
             questionTypeStats[qType].total++;
             
             const uAns = String(answers[String(q.id)] || '').trim().toUpperCase();
             const cAns = String(q.correctAnswer || '').trim().toUpperCase();
             
             if (uAns === cAns && cAns !== '') { 
                 score++; 
                 questionTypeStats[qType].correct++; 
             }
           });
        }
      });
    });

    setScoreResult({ score, total });
    setIsReviewMode(true);
    setShowPalette(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });

    try {
      const { data: { user } } = await supabase.auth.getUser();
      if (user) {
        const timeSpentSecs = parseInitialTime(basicInfo.timeLimit) - timeLeft;
        await supabase.from('test_results').insert([{
          user_id: user.id,
          course_id: safeData?.course_id || safeData?.content_json?.basicInfo?.courseId || null,
          test_title: basicInfo.title || safeData?.title || "Standard Test",
          test_type: safeData?.test_type || 'Standard',
          score: score, 
          total_score: total,
          time_spent: timeSpentSecs > 0 ? timeSpentSecs : 0,
          details: { 
              test_id: safeData?.id, 
              userAnswers: answers, 
              type_stats: questionTypeStats 
          }
        }]);
      await supabase.from('activity_logs').insert([{
        user_id: user.id, 
        action_type: 'finish_test',
        details: { 
            test_title: basicInfo.title || "Bài kiểm tra", 
            score: score,
            total: total
        }
      }]);  
      }
    } catch (error) { 
        console.error("Lỗi lưu kết quả thi:", error); 
    }

  } else {
    if (document.fullscreenElement) {
        document.exitFullscreen().catch(() => {});
    }
    if (onFinish) {
        onFinish({ score: scoreResult.score, total: scoreResult.total, testTitle: basicInfo.title });
    } else {
        onBack();
    }
  }
};

  const parseInitialTime = (val: any) => {
    if (!val) return 3600;
    if (typeof val === 'number') return val * 60;
    const num = parseInt(val);
    if (isNaN(num)) return 3600;
    return num * 60;
  };

  const getSavedEndTime = () => {
    if (!safeData?.id) return null;
    const saved = localStorage.getItem(`standard_endtime_${safeData.id}`);
    if (saved) return parseInt(saved, 10);
    return null;
  };

  const [timeLeft, setTimeLeft] = useState(() => parseInitialTime(basicInfo.timeLimit));
  
  // Countdown Timer
  useEffect(() => {
    if (!testStarted || isReviewMode) return;
    if (basicInfo?.category === 'exercise') return;
    
    const timer = setInterval(() => { 
        const currentEndTime = getSavedEndTime();
        if (currentEndTime) {
            const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
            setTimeLeft(remaining);
            if (remaining <= 0) {
                clearInterval(timer);
                alert("⏰ Hết giờ làm bài!");
                handleFinish();
            }
        } else { 
            setTimeLeft(prev => prev - 1); 
        }
    }, 1000);
    
    return () => clearInterval(timer);
  }, [testStarted, isReviewMode]);

  const formatTime = (sec: number) => {
    const m = Math.floor(sec / 60).toString().padStart(2, '0');
    const s = (sec % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  };

  const scrollToQuestion = (id: string) => {
    const el = document.getElementById(`q-${id}`);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      el.classList.add('ring-4', 'ring-[#0ea5e9]/40', 'rounded-xl');
      setTimeout(() => {
          el.classList.remove('ring-4', 'ring-[#0ea5e9]/40', 'rounded-xl');
      }, 1500);
    }
    setShowPalette(false);
  };

  // Quét ID câu hỏi để tạo Bảng điều hướng
  const { allQuestionIds, questionIndexMap } = useMemo(() => {
    const ids: string[] = [];
    parts?.forEach((p: any) => {
      p?.sections?.forEach((s: any) => {
        if (s?.questionType === "Điền từ" || s?.questionType === "Kéo thả vào Part") {
          const matches = String(s?.content || s?.questions?.[0]?.content || '').match(/\[(\d+)\]/g);
          if (matches) {
            matches.forEach((m: string) => {
              const num = m.replace(/\D/g, '');
              if (!ids.includes(num)) {
                  ids.push(num);
              }
            });
          }
        } else {
          s?.questions?.forEach((q: any) => {
            if (q?.id && !ids.includes(String(q.id))) {
                ids.push(String(q.id));
            }
          });
        }
      });
    });
    
    ids.sort((a, b) => parseInt(a) - parseInt(b));
    const map = ids.reduce((acc: any, id: string, idx: number) => { 
        acc[id] = idx + 1; 
        return acc; 
    }, {});
    
    return { allQuestionIds: ids, questionIndexMap: map };
  }, [parts]);

  const { answeredCount, markedCount, totalCount } = useMemo(() => {
    return {
      answeredCount: Object.keys(answers).filter(k => answers[k] && answers[k].trim() !== '').length,
      markedCount: Object.values(marked).filter(Boolean).length,
      totalCount: allQuestionIds.length
    }
  }, [answers, marked, allQuestionIds]);

  const getCleanQuestionText = (htmlContent: string) => {
    let txt = String(htmlContent || '').trim();
    txt = txt.replace(/^<p[^>]*>/i, '').replace(/<\/p>$/i, '').trim();
    txt = txt.replace(/^(<[^>]+>)*(Câu\s*\d+|\d+[\-\d]*)\s*[\.\):]?\s*(<\/[^>]+>)*\s*/i, '').trim();
    return txt;
  };

  const getCleanOptionText = (opt: string, index: number) => {
    let cleanOpt = String(opt || '').replace(/^<p[^>]*>/i, '').replace(/<\/p>$/i, '').trim();
    const expectedLetter = String.fromCharCode(65 + index);
    const match = cleanOpt.match(/^(<[^>]+>)*([a-zA-Z])([\.\):]?)\s*(<\/[^>]+>)*\s*([\s\S]*)/i);
    
    if (match && match[2].toUpperCase() === expectedLetter) {
        if (match[3] !== '' || match[5] === '') {
            return match[5].trim();
        }
    }
    return cleanOpt;
  };

  // =========================================================================================
  // CÔNG CỤ TƯƠNG TÁC VỚI GIA SƯ AI (CHAT VÀ VOICE)
  // =========================================================================================
  const askAIToExplain = (questionId: string, qContent: string, qExplanation: string) => {
     const displayPrompt = `**Câu hỏi số ${questionIndexMap[questionId] || questionId}:**\n${qContent.replace(/<[^>]+>/g, '')}\n\n**Đáp án & Giải thích gốc:**\n${qExplanation.replace(/<[^>]+>/g, '')}`;
     
     const fakeBtn = document.createElement('button');
     fakeBtn.className = 'btn-ai-trigger hidden';
     fakeBtn.setAttribute('data-task', 'reading');
     fakeBtn.setAttribute('data-topic', displayPrompt);
     document.body.appendChild(fakeBtn);
     fakeBtn.click();
     
     setTimeout(() => { 
         fakeBtn.remove(); 
     }, 100);
  };

  const callTutorForQuestion = (qId: string, qContent: string, qExplanation: string) => {
      const qIdx = questionIndexMap[String(qId)] || qId;
      const plainContent = String(qContent || '').replace(/<[^>]+>/g, '').trim();
      const plainExplanation = String(qExplanation || 'Không có lời giải thích.').replace(/<[^>]+>/g, '').trim();
      const userAns = String(answers[String(qId)] || '(trống)');
      
      const tutorContext = {
          overall: scoreResult.score + '/' + scoreResult.total,
          transcript: `Câu hỏi số ${qIdx}: "${plainContent}". \nĐáp án của học sinh: ${userAns}. \nGiải thích đáp án đúng: "${plainExplanation}".`,
          feedback: "Học sinh đang xem lại câu hỏi này trong bài kiểm tra. Hãy giải thích chi tiết tại sao đáp án lại như vậy, phân tích ngữ pháp/từ vựng liên quan."
      };
      
      sessionStorage.setItem('tony_live_mode', 'TUTOR');
      sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
      sessionStorage.setItem('tony_auto_start', 'true'); // ÉP AI TỰ ĐỘNG BỐC MÁY
      
      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
  };

  // Component Hiển thị Đoạn văn Đục lỗ
  const renderInlineQuestion = (text: any) => {
    if (!text) return null;
    const safeText = String(text);
    const textParts = safeText.split(/(\[\d+\])/g);
    
    return textParts.map((partText, index) => {
      const match = partText.match(/\[(\d+)\]/);
      
      if (match) {
        const qNum = match[1]; 
        const userAns = String(answers[qNum] || '');
        const displayIndex = questionIndexMap[qNum] || qNum;
        
        if (isReviewMode) {
          const qData = parts.flatMap((p: any) => p?.sections?.flatMap((s: any) => s?.questions) || []).find((q: any) => String(q?.id) === String(qNum));
          const correctAns = String(qData?.correctAnswer || '');
          const isCorrect = userAns.trim().toUpperCase() === correctAns.trim().toUpperCase();
          
          return (
            <span key={index} className="relative inline-flex flex-col items-center align-top mx-1.5 mt-1 group">
              <span className={`px-2.5 py-0.5 text-[14px] font-bold text-white rounded-md shadow-sm border ${isCorrect ? 'bg-emerald-600 border-emerald-700' : 'bg-red-500 border-red-600'}`}>
                {displayIndex}. {userAns || '(trống)'}
              </span>
              {!isCorrect && (
                <span className="absolute top-full left-1/2 -translate-x-1/2 mt-1.5 text-[11px] text-emerald-800 font-bold bg-emerald-100 px-2 py-0.5 border border-emerald-300 rounded text-center whitespace-nowrap z-10 shadow-sm opacity-0 group-hover:opacity-100 transition-opacity">
                  ĐA: {correctAns}
                </span>
              )}
            </span>
          );
        }

        return (
          <span key={index} id={`q-${qNum}`} className="inline-flex items-center align-middle mx-1.5 scroll-mt-24">
            <span className="font-bold text-[14px] mr-1.5 text-slate-500">{displayIndex}.</span>
            <input 
              type="text" 
              className="w-28 border-b-[2px] border-slate-300 focus:outline-none focus:border-[#0ea5e9] bg-transparent text-center text-[#0ea5e9] font-bold px-1 text-[15px] pb-[1px] transition-colors" 
              value={userAns} 
              onChange={(e) => handleAnswer(qNum, e.target.value)} 
              autoComplete="off" 
              spellCheck="false"
            />
          </span>
        );
      }
      return <span key={index} dangerouslySetInnerHTML={{ __html: partText || '' }} />;
    });
  };

  const handleStartTest = () => {
    setTestStarted(true);
    let currentEndTime = getSavedEndTime();
    
    if (!currentEndTime) {
        const initialSeconds = parseInitialTime(basicInfo.timeLimit);
        currentEndTime = Date.now() + initialSeconds * 1000;
        if (safeData?.id) {
            localStorage.setItem(`standard_endtime_${safeData.id}`, currentEndTime.toString());
        }
        setTimeLeft(initialSeconds);
    } else {
        const remaining = Math.max(0, Math.floor((currentEndTime - Date.now()) / 1000));
        setTimeLeft(remaining);
        if (remaining <= 0 && basicInfo?.category !== 'exercise') {
            alert("⏰ Bài thi này đã hết thời gian làm bài!");
            handleFinish();
            return;
        }
    }

    if (globalAudioRef.current && isListening) {
      globalAudioRef.current.play().catch(e => {
        console.error("Autoplay blocked:", e);
        alert("Trình duyệt chặn phát âm thanh tự động. Vui lòng bấm Bắt Đầu lại.");
      });
    }
  };

  // =========================================================================================
  // GIAO DIỆN CHUNG (GỘP CHO CẢ ĐỌC VÀ NGHE)
  // =========================================================================================
  const renderTestLayout = () => {
    return (
      <div className="flex flex-col h-[100dvh] font-sans bg-[#f1f5f9] overflow-hidden text-slate-800">
        
        <header className={`h-[60px] border-b border-slate-200 flex justify-between items-center px-6 shrink-0 shadow-sm z-20 ${isReviewMode ? 'bg-emerald-700 text-white border-none' : 'bg-white text-slate-800'}`}>
          <div className="font-black text-[16px] flex items-center gap-3 uppercase tracking-tight">
            <span className={`text-xl ${isReviewMode ? 'opacity-100' : 'opacity-70'}`}>
                {(isListening && hasAnyAudio) ? '🎧' : '📖'}
            </span>
            <span className="truncate max-w-[200px] md:max-w-xl">
                {isReviewMode ? `[CHỮA BÀI] ${basicInfo?.title}` : basicInfo?.title}
            </span>
          </div>
          
          {isReviewMode && (
            <div className="absolute left-1/2 -translate-x-1/2 hidden md:flex items-center gap-4">
               <button 
                  onClick={() => {
                    const tutorContext = {
                      overall: scoreResult.score + '/' + scoreResult.total,
                      transcript: `Bài test: ${basicInfo.title}. Điểm số của em là: ${scoreResult.score}/${scoreResult.total}.`,
                      feedback: "Học sinh vừa làm xong bài test. Hãy chúc mừng và đưa ra nhận xét chung. Hỏi xem học sinh có muốn bạn chữa câu nào cụ thể không."
                    };
                    sessionStorage.setItem('tony_live_mode', 'TUTOR');
                    sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
                    sessionStorage.setItem('tony_auto_start', 'true');
                    window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
                  }}
                  className="bg-emerald-600 hover:bg-emerald-500 text-white px-5 py-1.5 rounded-full text-[13px] font-bold transition uppercase tracking-wider shadow flex items-center gap-2"
               >
                  📞 Gọi Gia Sư AI (Tổng kết)
               </button>
            </div>
          )}

          <div className="flex items-center gap-4">
            {/* ⚙ NÚT CÀI ĐẶT */}
            <div className="relative">
              <button 
                  onClick={() => setShowSettings(!showSettings)} 
                  className={`flex items-center gap-2 opacity-70 hover:opacity-100 transition text-[13px] font-bold ${showSettings ? 'opacity-100' : ''}`}
                  title="Cài đặt"
              >
                 <SettingsIcon /> Cài đặt
              </button>
              
              {showSettings && (
                <div className="absolute right-0 top-full mt-2 bg-white border border-slate-200 rounded-xl shadow-xl p-5 w-[220px] z-50 animate-in fade-in slide-in-from-top-2 duration-200">
                  <div className="mb-5">
                    <p className="text-[12px] font-bold text-slate-500 uppercase tracking-widest mb-3">Cài đặt kích cỡ chữ</p>
                    <div className="flex gap-2 justify-center">
                      {(['S', 'M', 'L'] as const).map(size => (
                        <button 
                            key={size}
                            onClick={() => setFontSize(size)}
                            className={`w-10 h-10 rounded-full font-black text-[14px] transition-all border-2 ${
                              fontSize === size 
                                ? 'bg-[#0ea5e9] text-white border-[#0ea5e9] shadow-md scale-110' 
                                : 'bg-slate-100 text-slate-600 border-slate-200 hover:bg-slate-200'
                            }`}
                        >
                          {size}
                        </button>
                      ))}
                    </div>
                  </div>
                  
                  {(isListening && hasAnyAudio && globalAudioRef.current) && (
                    <div>
                      <p className="text-[12px] font-bold text-slate-500 uppercase tracking-widest mb-3">Cài đặt âm thanh</p>
                      <div className="flex items-center gap-2">
                        <span className="text-lg">🔈</span>
                        <input 
                            type="range" 
                            min="0" max="1" step="0.05" 
                            defaultValue="1" 
                            onChange={(e) => { 
                                if(globalAudioRef.current) {
                                    globalAudioRef.current.volume = parseFloat(e.target.value);
                                } 
                            }} 
                            className="w-full accent-[#0ea5e9] cursor-pointer" 
                        />
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>

            <button 
                onClick={toggleFullscreen} 
                className="hover:text-current opacity-70 hover:opacity-100 transition" 
                title="Toàn màn hình"
            >
               {isFullscreen ? <ExitFullscreenIcon /> : <FullscreenIcon />}
            </button>
            <button 
                onClick={handleExit} 
                className={`text-[13px] font-bold px-4 py-2 rounded-lg transition-colors flex items-center gap-2 shadow-sm border ${isReviewMode ? 'bg-emerald-600 text-white border-emerald-500 hover:bg-emerald-800' : 'bg-white hover:bg-slate-50 text-slate-600 border-slate-200'}`}
            >
              Thoát
            </button>
          </div>
        </header>

        <div className="flex-1 flex overflow-hidden relative flex-col md:flex-row" ref={containerRef} onClick={() => showSettings && setShowSettings(false)}>
          
          {/* PANEL TRÁI (BÀI ĐỌC) - ẨN ĐI NẾU LÀ BÀI LISTENING */}
          {!isListening && (
              <div 
                  className="bg-white overflow-y-auto custom-scrollbar w-full md:w-auto" 
                  ref={leftPaneRef} 
                  style={{ width: window.innerWidth > 768 ? `${leftWidth}%` : '100%' }}
              >
                <div className={`p-6 md:p-10 ${fontSize === 'S' ? 'text-[14px]' : fontSize === 'L' ? 'text-[18px]' : 'text-[16px]'}`}>
                  {isReviewMode && (
                    <div className="bg-emerald-50 rounded-2xl shadow-sm border border-emerald-100 p-6 mb-8 text-center relative">
                       <h3 className="text-emerald-700 font-bold uppercase tracking-widest text-xs mb-2">Kết quả bài làm</h3>
                       <div className="text-5xl font-black text-emerald-600">
                           {scoreResult.score} <span className="text-2xl text-emerald-400">/ {scoreResult.total}</span>
                       </div>
                       
                       <div className="mt-4 md:hidden">
                          <button 
                              onClick={() => {
                                const tutorContext = {
                                  overall: scoreResult.score + '/' + scoreResult.total,
                                  transcript: `Bài test: ${basicInfo.title}. Điểm số của em là: ${scoreResult.score}/${scoreResult.total}.`,
                                  feedback: "Học sinh vừa làm xong bài test. Hãy chúc mừng và đưa ra nhận xét chung. Hỏi xem học sinh có muốn bạn chữa câu nào cụ thể không."
                                };
                                sessionStorage.setItem('tony_live_mode', 'TUTOR');
                                sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
                                sessionStorage.setItem('tony_auto_start', 'true');
                                window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
                              }}
                              className="bg-emerald-600 text-white px-5 py-2 rounded-full text-[13px] font-bold shadow flex items-center justify-center gap-2 mx-auto"
                          >
                              📞 Gọi Gia Sư AI
                          </button>
                       </div>
                    </div>
                  )}

                  {parts?.map((part: any, pIdx: number) => {
                    return (
                      <div key={part?.id || pIdx} className="mb-12">
                        {part?.title && (
                            <h3 className="font-black text-xl text-slate-800 mb-6 uppercase tracking-tight border-b-2 border-slate-800 pb-3">
                                {part.title}
                            </h3>
                        )}
                        
                        {part?.imageUrl && (
                            <img src={part.imageUrl} className="max-w-full mb-6 rounded-xl shadow-sm border border-slate-200" alt="Part Image" />
                        )}
                        
                        {part?.content && (
                          <div 
                              className="prose prose-slate max-w-none text-slate-800 text-[16px] leading-[1.9] whitespace-pre-wrap mb-8 text-justify bg-slate-50 p-6 md:p-8 rounded-2xl border border-slate-200 shadow-sm" 
                              dangerouslySetInnerHTML={{ __html: part.content || '' }} 
                          />
                        )}
                        
                        {part?.sections?.map((sec: any, sIdx: number) => {
                          let displaySecTitle = sec.title;
                          
                          if (displaySecTitle && /Questions?\s+\d+/i.test(displaySecTitle)) {
                              let firstIdx = null;
                              let lastIdx = null;
                              
                              if (sec.questionType === "Điền từ" || sec.questionType === "Kéo thả vào Part") {
                                  const matches = Array.from(String(sec.content || sec.questions?.[0]?.content || '').matchAll(/\[(\d+)\]/g));
                                  if (matches.length > 0) {
                                      firstIdx = questionIndexMap[matches[0][1]];
                                      lastIdx = questionIndexMap[matches[matches.length - 1][1]];
                                  }
                              } else if (sec.questions?.length > 0) {
                                  firstIdx = questionIndexMap[sec.questions[0].id];
                                  lastIdx = questionIndexMap[sec.questions[sec.questions.length - 1].id];
                              }
                              
                              if (firstIdx && lastIdx) {
                                  displaySecTitle = displaySecTitle.replace(/Questions?\s+\d+(-\d+)?/i, firstIdx === lastIdx ? `Question ${firstIdx}` : `Questions ${firstIdx}-${lastIdx}`);
                              }
                          }

                          return (
                            <div key={sec?.id || sIdx} className="mb-8">
                              {displaySecTitle && (
                                  <h4 className="font-bold text-[15px] text-slate-800 bg-slate-100 border border-slate-200 inline-block px-4 py-1.5 rounded-lg mb-4">
                                      {displaySecTitle}
                                  </h4>
                              )}
                              
                              {sec?.imageUrl && (
                                  <img src={sec.imageUrl} className="max-w-full mb-4 rounded-xl shadow-sm border border-slate-200" alt="Section Image" />
                              )}
                              
                              {sec?.content && sec?.questionType !== "Điền từ" && sec?.questionType !== "Kéo thả vào Part" && (
                                <div 
                                    className="prose prose-sm max-w-none text-slate-700 whitespace-pre-wrap leading-relaxed bg-white p-5 rounded-xl border border-slate-200 shadow-sm" 
                                    dangerouslySetInnerHTML={{ __html: sec.content || '' }} 
                                />
                              )}
                            </div>
                          )
                        })}
                      </div>
                    );
                  })}
                </div>
              </div>
          )}

          {/* THANH KÉO THẢ RESIZER - ẨN ĐI NẾU LÀ BÀI LISTENING */}
          {!isListening && (
              <div 
                onMouseDown={handleMouseDown}
                className="hidden md:flex w-2.5 bg-slate-100 hover:bg-[#0ea5e9] cursor-col-resize flex-col justify-center items-center transition-colors shrink-0 z-10 border-x border-slate-200 group shadow-sm active:bg-blue-600"
                title="Kéo để điều chỉnh độ rộng"
              >
                <div className="flex flex-col gap-1.5 opacity-40 group-hover:opacity-100 transition-opacity">
                  <div className="w-1 h-1 rounded-full bg-slate-600 group-hover:bg-white"></div>
                  <div className="w-1 h-1 rounded-full bg-slate-600 group-hover:bg-white"></div>
                  <div className="w-1 h-1 rounded-full bg-slate-600 group-hover:bg-white"></div>
                </div>
              </div>
          )}

          {/* PANEL PHẢI (CÂU HỎI VÀ NỘI DUNG LISTENING) */}
          <div 
              className="bg-[#f8fafc] overflow-y-auto custom-scrollbar scroll-smooth w-full md:w-auto flex-1" 
              id="questions-container" 
              ref={rightPaneRef} 
              style={!isListening && window.innerWidth > 768 ? { width: `${100 - leftWidth}%`, flex: 'none' } : { flex: 1 }}
          >
             <div className={`p-6 md:p-10 max-w-3xl mx-auto ${fontSize === 'S' ? 'text-[14px]' : fontSize === 'L' ? 'text-[18px]' : 'text-[16px]'}`}>
               
               {/* NẾU LÀ BÀI LISTENING CÓ CHẾ ĐỘ XEM LẠI, HIỂN THỊ ĐIỂM Ở ĐÂY CHO ĐẸP */}
               {isListening && isReviewMode && (
                   <div className="bg-emerald-50 rounded-2xl shadow-sm border border-emerald-100 p-6 mb-8 text-center relative">
                      <h3 className="text-emerald-700 font-bold uppercase tracking-widest text-xs mb-2">Kết quả bài làm</h3>
                      <div className="text-5xl font-black text-emerald-600">
                          {scoreResult.score} <span className="text-2xl text-emerald-400">/ {scoreResult.total}</span>
                      </div>
                   </div>
               )}

               {parts?.map((part: any, pIdx: number) => {
                  return (
                    <div key={`qpane-${part?.id || pIdx}`}>
                       
                       {/* NỘI DUNG PART SANG BÊN PHẢI NẾU LÀ LISTENING */}
                       {isListening && (
                           <div className="mb-8 bg-transparent">
                               {part?.title && <h3 className="font-black text-xl text-slate-800 mb-2">{part.title}</h3>}
                               {part?.content && <div className="text-[15px] text-slate-600 leading-relaxed mb-6" dangerouslySetInnerHTML={{ __html: part.content || '' }} />}
                               {part?.imageUrl && <img src={part.imageUrl} className="max-w-full mb-6 rounded-xl shadow-sm border border-slate-200" alt="Part Image" />}
                           </div>
                       )}

                       {part?.sections?.map((sec: any, sIdx: number) => {
                          
                          let displaySecTitle = sec.title;
                          if (displaySecTitle && /Questions?\s+\d+/i.test(displaySecTitle)) {
                              let firstIdx = null;
                              let lastIdx = null;
                              
                              if (sec.questionType === "Điền từ" || sec.questionType === "Kéo thả vào Part") {
                                  const matches = Array.from(String(sec.content || sec.questions?.[0]?.content || '').matchAll(/\[(\d+)\]/g));
                                  if (matches.length > 0) {
                                      firstIdx = questionIndexMap[matches[0][1]];
                                      lastIdx = questionIndexMap[matches[matches.length - 1][1]];
                                  }
                              } else if (sec.questions?.length > 0) {
                                  firstIdx = questionIndexMap[sec.questions[0].id];
                                  lastIdx = questionIndexMap[sec.questions[sec.questions.length - 1].id];
                              }
                              
                              if (firstIdx && lastIdx) {
                                  displaySecTitle = displaySecTitle.replace(/Questions?\s+\d+(-\d+)?/i, firstIdx === lastIdx ? `Question ${firstIdx}` : `Questions ${firstIdx}-${lastIdx}`);
                              }
                          }

                          return (
                          <div key={`qsec-${sec?.id || sIdx}`} className="mb-12">
                              
                             {displaySecTitle && !isListening && (
                                 <div className="bg-slate-200/60 border border-slate-300 px-4 py-2 mb-4 rounded-lg inline-block">
                                     <h4 className="font-bold text-[14px] text-slate-800">{displaySecTitle}</h4>
                                 </div>
                             )}

                             {/* NỘI DUNG SECTION SANG BÊN PHẢI NẾU LÀ LISTENING */}
                             {isListening && (
                                 <div className="mb-6">
                                    {displaySecTitle && <h4 className="font-bold text-[16px] text-slate-800 mb-4">{displaySecTitle}</h4>}
                                    {sec?.imageUrl && <img src={sec.imageUrl} className="max-w-full mb-4 rounded-xl shadow-sm border border-slate-200" alt="Section Image" />}
                                    {sec?.content && sec?.questionType !== "Điền từ" && sec?.questionType !== "Kéo thả vào Part" && (
                                       <div className="text-slate-600 text-[15px] leading-relaxed mb-6" dangerouslySetInnerHTML={{ __html: sec.content || '' }} />
                                    )}
                                 </div>
                             )}
                             
                             {(sec?.questionType === "Điền từ" || sec?.questionType === "Kéo thả vào Part") && (
                               <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 mb-6">
                                 {sec?.imageUrl && !isListening && (
                                     <img src={sec.imageUrl} className="max-w-full mb-6 rounded-lg border border-slate-200" alt="Fill Image" />
                                 )}
                                 
                                 <div className="space-y-5 leading-[2.5] text-[16px] text-slate-800 text-justify">
                                   {renderInlineQuestion(sec?.content || '')}
                                 </div>
                                 
                                 {/* 🚀 THÊM REVIEW VÀ GỌI GIA SƯ CHO PHẦN ĐIỀN TỪ CỦA READING */}
                                 {isReviewMode && (
                                    <div className="mt-8 pt-6 border-t border-slate-200 space-y-4">
                                       <p className="text-[14px] font-black text-slate-800 uppercase tracking-widest mb-4">💡 Giải thích chi tiết & Gia Sư AI:</p>
                                       {sec.questions?.map((q: any) => {
                                          if (!q?.id) return null;
                                          const qIdx = questionIndexMap[String(q.id)] || q.id;
                                          const explanationText = q.explanation || 'Không có lời giải thích.';
                                          
                                          return (
                                             <div key={`expl-${q.id}`} className="bg-slate-50 p-5 rounded-xl border border-slate-200">
                                                <div className="flex items-center gap-2 mb-2">
                                                    <span className="bg-slate-800 text-white font-bold px-2 py-0.5 text-[13px] rounded">Câu {qIdx}</span>
                                                </div>
                                                <div className="text-[14px] text-slate-700 italic leading-relaxed whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: explanationText }} />
                                                
                                                <div className="flex items-center gap-2 mt-4 pt-4 border-t border-slate-200">
                                                    <button 
                                                        onClick={(e) => { 
                                                            e.stopPropagation(); 
                                                            askAIToExplain(String(q.id), sec.content || '', explanationText); 
                                                        }} 
                                                        className="px-4 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded text-[13px] transition shadow-sm border border-[#064e3b]"
                                                    >
                                                        💬 Chat với AI
                                                    </button>
                                                    <button 
                                                        onClick={(e) => { 
                                                            e.stopPropagation(); 
                                                            callTutorForQuestion(String(q.id), sec.content || '', explanationText); 
                                                        }} 
                                                        className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded text-[13px] transition shadow-sm border border-emerald-600 flex items-center gap-1"
                                                    >
                                                        📞 Gọi Gia sư
                                                    </button>
                                                </div>
                                             </div>
                                          );
                                       })}
                                    </div>
                                 )}
                               </div>
                             )}

                             {(sec?.questionType === "Trắc nghiệm" || sec?.questionType === "TFNG") && sec?.questions?.map((q: any) => {
                                if (!q?.id) return null;
                                const cleanQText = getCleanQuestionText(q.content);
                                const correctAns = String(q.correctAnswer || '').trim().toUpperCase();
                                const userAns = String(answers[String(q.id)] || '').trim().toUpperCase();
                                const isQuestionCorrect = userAns === correctAns;
                                const displayIdx = questionIndexMap[String(q.id)] || q.id;
                                
                                const isTFNG = sec?.questionType === "TFNG" || q.options?.some((opt: string) => ['TRUE', 'FALSE', 'NOT GIVEN', 'YES', 'NO'].includes(opt?.trim()?.toUpperCase()));

                                if (isTFNG) {
                                   return (
                                     <div 
                                         key={q.id} 
                                         id={`q-${q.id}`} 
                                         className={`bg-white p-6 rounded-2xl shadow-sm border transition-all mb-4 scroll-mt-20 relative group ${isReviewMode ? (isQuestionCorrect ? 'border-emerald-300 bg-emerald-50/20' : 'border-red-300 bg-red-50/20') : 'border-slate-200 hover:border-[#0ea5e9]/50'}`}
                                     >
                                        {!isReviewMode && (
                                          <button 
                                              onClick={() => toggleMark(String(q.id))} 
                                              className={`absolute top-5 right-5 transition-colors ${marked[String(q.id)] ? 'text-amber-500' : 'text-slate-200 hover:text-slate-400'}`}
                                          >
                                             <BookmarkIcon filled={!!marked[String(q.id)]} />
                                          </button>
                                        )}
                                        
                                        {isReviewMode && (
                                            <div className="absolute top-5 right-5 font-bold text-[12px]">
                                                {isQuestionCorrect ? <span className="text-emerald-700 bg-emerald-100 px-3 py-1 rounded-md">✅ Đúng</span> : <span className="text-red-700 bg-red-100 px-3 py-1 rounded-md">❌ Sai</span>}
                                            </div>
                                        )}

                                       <div className="flex gap-4 mb-2">
                                         <span className="font-bold text-slate-800 shrink-0 w-6 text-right pt-[2px]">{displayIdx}.</span>
                                         <div className="flex-1">
                                           {q.imageUrl && <img src={q.imageUrl} className="max-w-[80%] mb-4 rounded border border-slate-200" alt="Question" />}
                                           {cleanQText && <div className="text-[16px] text-slate-800 font-medium leading-relaxed whitespace-pre-wrap mb-4" dangerouslySetInnerHTML={{ __html: cleanQText }} />}
                                           
                                           <div className="flex flex-row flex-wrap gap-4">
                                             {q.options?.map((opt: string, i: number) => {
                                                const safeOpt = String(opt || '');
                                                const val = safeOpt.replace(/<[^>]*>/g, '').trim().toUpperCase();
                                                const isSelected = userAns === val;
                                                const isCorrectOpt = correctAns === val;

                                                let labelStyle = "flex items-center gap-2 p-1.5 transition rounded-lg border border-transparent";
                                                
                                                if (isReviewMode) {
                                                   if (isCorrectOpt) {
                                                       labelStyle += " font-bold text-emerald-800 bg-emerald-100 border-emerald-300";
                                                   } else if (isSelected) {
                                                       labelStyle += " text-red-600 line-through opacity-70 bg-red-50 border-red-200";
                                                   } else {
                                                       labelStyle += " opacity-50 border-slate-100";
                                                   }
                                                } else {
                                                   labelStyle += " cursor-pointer hover:bg-slate-50 hover:text-[#0ea5e9] border-slate-100";
                                                }

                                                return (
                                                   <label key={i} className={labelStyle}>
                                                      <input 
                                                          type="radio" 
                                                          name={`q-${q.id}`} 
                                                          value={val} 
                                                          checked={isSelected} 
                                                          onChange={() => handleAnswer(String(q.id), val)} 
                                                          disabled={isReviewMode} 
                                                          className="w-4 h-4 accent-[#0ea5e9] cursor-pointer" 
                                                      />
                                                      <span className="text-[15px] font-semibold" dangerouslySetInnerHTML={{ __html: safeOpt }} />
                                                   </label>
                                                );
                                             })}
                                           </div>
                                           
                                           {isReviewMode && q.explanation && (
                                             <div className="mt-6 pt-4 border-t border-slate-100">
                                                <p className="text-[12px] font-black text-amber-600 uppercase mb-2">💡 Giải thích:</p>
                                                <div className="text-[14px] text-slate-700 italic leading-relaxed mb-3" dangerouslySetInnerHTML={{ __html: String(q.explanation) }} />
                                                
                                                {/* 🚀 THÊM NÚT GỌI GIA SƯ */}
                                                <div className="flex items-center gap-2 mt-3">
                                                    <button 
                                                        onClick={(e) => { 
                                                            e.stopPropagation(); 
                                                            askAIToExplain(String(q.id), q.content, q.explanation); 
                                                        }} 
                                                        className="px-3 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded text-[12px] transition shadow-sm border border-[#064e3b]"
                                                    >
                                                        💬 Chat với AI
                                                    </button>
                                                    <button 
                                                        onClick={(e) => { 
                                                            e.stopPropagation(); 
                                                            callTutorForQuestion(String(q.id), q.content, q.explanation); 
                                                        }} 
                                                        className="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded text-[12px] transition shadow-sm border border-emerald-600 flex items-center gap-1"
                                                    >
                                                        📞 Gọi Gia sư
                                                    </button>
                                                </div>
                                             </div>
                                           )}
                                         </div>
                                       </div>
                                     </div>
                                   );
                                }

                                return (
                                  <div 
                                      key={q.id} 
                                      id={`q-${q.id}`} 
                                      className={`bg-white p-6 md:p-8 rounded-2xl border shadow-sm relative group scroll-mt-20 transition-colors ${isReviewMode ? (isQuestionCorrect ? 'bg-emerald-50/30 border-emerald-200' : 'bg-red-50/30 border-red-200') : 'hover:border-[#0ea5e9]/50 border-slate-200'}`}
                                  >
                                     {!isReviewMode && (
                                        <button 
                                            onClick={() => toggleMark(String(q.id))} 
                                            className={`absolute top-6 right-6 transition-colors ${marked[String(q.id)] ? 'text-amber-500' : 'text-slate-300 hover:text-slate-400'}`}
                                        >
                                           <BookmarkIcon filled={!!marked[String(q.id)]} />
                                        </button>
                                     )}
                                     
                                     {isReviewMode && (
                                        <div className="absolute top-6 right-6 font-bold text-[12px]">
                                           {isQuestionCorrect ? <span className="text-emerald-700 bg-emerald-100 px-3 py-1.5 rounded-lg">✅ Đúng</span> : <span className="text-red-700 bg-red-100 px-3 py-1.5 rounded-lg">❌ Sai</span>}
                                        </div>
                                     )}

                                     {isListening && (
                                        <div className="flex justify-between items-center mb-5 border-b border-slate-100 pb-3 pr-8">
                                            <h3 className="font-bold text-lg text-slate-800">Question {displayIdx}:</h3>
                                        </div>
                                     )}

                                     <div className="flex gap-4 mb-5 pr-10 items-start">
                                        {!isListening && (
                                           <span className="font-bold text-white bg-slate-800 px-2 py-0.5 rounded text-[13px] mt-0.5">{displayIdx}</span>
                                        )}
                                        <div className="flex-1 w-full">
                                           {q.imageUrl && <img src={q.imageUrl} className={`mb-4 rounded-xl border border-slate-200 shadow-sm ${isListening ? 'max-w-[400px] w-full mx-auto block' : 'max-w-[80%]'}`} alt="Question Image" />}
                                           {cleanQText && <div className="text-[16px] text-slate-800 leading-relaxed font-medium mb-3 whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: cleanQText }} />}
                                        </div>
                                     </div>
                                     
                                     <div className="flex flex-col gap-2 pl-10">
                                        {q.options?.map((opt: any, i: number) => {
                                           const cleanOpt = getCleanOptionText(opt, i);
                                           const val = String.fromCharCode(65+i);
                                           const isSelected = userAns === val;
                                           const isCorrectOpt = correctAns === val;

                                           let labelStyle = "flex items-start gap-4 p-3 rounded-xl transition-colors border border-transparent";
                                           let circleStyle = "border-slate-300 bg-white";
                                           let textStyle = "text-slate-800";
                                           
                                           if (isReviewMode) {
                                              if (isCorrectOpt) { 
                                                  labelStyle += " bg-emerald-50 border-emerald-200"; 
                                                  circleStyle = "border-emerald-500 bg-emerald-500 text-white"; 
                                                  textStyle = "font-bold text-emerald-900"; 
                                              }
                                              else if (isSelected) { 
                                                  labelStyle += " bg-red-50 border-red-200"; 
                                                  circleStyle = "border-red-500 bg-red-500 text-white"; 
                                                  textStyle = "line-through text-red-700 opacity-70"; 
                                              }
                                              else { 
                                                  labelStyle += " opacity-50"; 
                                              }
                                           } else {
                                              labelStyle += " cursor-pointer hover:bg-slate-50";
                                              if (isSelected) { 
                                                  labelStyle += " bg-blue-50/50 border-blue-200"; 
                                                  circleStyle = "border-[#0ea5e9] bg-[#0ea5e9] text-white shadow-inner"; 
                                                  textStyle = "font-bold text-[#0ea5e9]"; 
                                              }
                                           }

                                           return (
                                              <label key={i} className={labelStyle}>
                                                 <input 
                                                     type="radio" 
                                                     name={`q-${q.id}`} 
                                                     value={val} 
                                                     checked={isSelected} 
                                                     onChange={() => handleAnswer(String(q.id), val)} 
                                                     disabled={isReviewMode} 
                                                     className="hidden" 
                                                 />
                                                 <div className="pt-0.5">
                                                    <div className={`w-[22px] h-[22px] rounded-full border-2 flex items-center justify-center shrink-0 transition-colors shadow-sm ${circleStyle}`}>
                                                       {(isSelected || isCorrectOpt) && <div className="w-2 h-2 rounded-full bg-white"></div>}
                                                    </div>
                                                 </div>
                                                 <span className={`text-[16px] leading-relaxed ${textStyle}`}>
                                                     <span className="font-bold mr-2">{val}.</span> 
                                                     <span dangerouslySetInnerHTML={{ __html: cleanOpt }} />
                                                 </span>
                                              </label>
                                           );
                                        })}
                                     </div>

                                     {isReviewMode && q.explanation && (
                                        <div className="mt-8 pt-5 border-t border-slate-200 ml-10">
                                           <p className="text-[12px] font-black text-amber-600 uppercase tracking-widest mb-2">💡 Giải thích đáp án:</p>
                                           <div className="text-[14px] text-slate-700 italic leading-relaxed whitespace-pre-wrap border-l-[3px] border-slate-300 pl-3 mb-3" dangerouslySetInnerHTML={{ __html: String(q.explanation) }} />
                                           
                                           <div className="flex items-center gap-2 mt-3">
                                               <button 
                                                   onClick={(e) => { 
                                                       e.stopPropagation(); 
                                                       askAIToExplain(String(q.id), q.content, q.explanation); 
                                                   }} 
                                                   className="px-3 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded text-[12px] transition shadow-sm border border-[#064e3b]"
                                               >
                                                  💬 Chat với AI
                                               </button>
                                               <button 
                                                   onClick={(e) => { 
                                                       e.stopPropagation(); 
                                                       callTutorForQuestion(String(q.id), q.content, q.explanation); 
                                                   }} 
                                                   className="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded text-[12px] transition shadow-sm border border-emerald-600 flex items-center gap-1"
                                               >
                                                  📞 Gọi Gia sư
                                               </button>
                                           </div>
                                        </div>
                                     )}
                                  </div>
                                );
                             })}

                             {/* DẠNG BÀI DROPLIST KHỐI */}
                             {sec?.questionType === "Droplist" && (
                                <div className="space-y-4 bg-white p-6 md:p-8 border border-gray-200 rounded-xl shadow-sm">
                                  {sec.questions?.map((q: any) => {
                                      if (!q?.id) return null;
                                      const correctAns = String(q.correctAnswer || '').trim().toUpperCase(); 
                                      const userAns = String(answers[String(q.id)] || '').trim(); 
                                      const isCorrect = isAnswerCorrect(userAns, correctAns);
                                      const displayIdx = questionIndexMap[String(q.id)] || q.id;
                                      const validOptions = q.options?.filter(Boolean) || sec.questions[0]?.options?.filter(Boolean) || [];
                                      
                                      return (
                                        <div 
                                            key={q.id} 
                                            id={`q-${q.id}`} 
                                            className={`p-4 rounded-lg border flex flex-col gap-4 transition-all scroll-mt-20 ${isReviewMode ? (isCorrect ? 'bg-emerald-50 border-emerald-200' : 'bg-red-50 border-red-200') : 'bg-white border-gray-200 hover:border-gray-300'}`}
                                        >
                                          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 w-full">
                                            <div className="flex items-center gap-4 flex-1 min-w-0">
                                              <span className="font-bold text-white bg-slate-800 px-2 py-0.5 rounded text-[13px] shrink-0">{displayIdx}</span>
                                              <div className="text-[15px] text-gray-800 leading-relaxed font-serif format-passage html-content-renderer flex-1 min-w-0 break-words [&>p]:!m-0 [&>p]:!inline" dangerouslySetInnerHTML={{ __html: getCleanQuestionText(q.content) }} />
                                            </div>
                                            <div className="shrink-0 flex items-center justify-start md:justify-end font-sans">
                                               {isReviewMode ? (
                                                   <div className="flex items-center gap-2 justify-start md:justify-end w-full">
                                                       <div className={`px-4 py-1.5 rounded font-bold text-[14px] border min-w-[140px] text-center ${isCorrect ? 'bg-emerald-100 text-emerald-800 border-emerald-300' : 'bg-red-100 text-red-800 border-red-300'}`}>
                                                          {userAns || '(trống)'}
                                                       </div>
                                                       {!isCorrect && (
                                                           <div className="text-[12px] font-bold text-emerald-700 bg-emerald-100 border border-emerald-300 px-2 py-0.5 rounded whitespace-nowrap">
                                                               ĐA: {correctAns}
                                                           </div>
                                                       )}
                                                   </div>
                                                ) : (
                                                   <select 
                                                     value={userAns}
                                                     onChange={(e) => handleAnswer(String(q.id), e.target.value)}
                                                     className="bg-transparent border-0 border-b-2 border-gray-400 text-blue-800 font-bold text-center text-[15px] h-[36px] px-2 outline-none focus:border-blue-600 cursor-pointer w-auto min-w-[140px] max-w-[250px]"
                                                   >
                                                     <option value="">---</option>
                                                     {validOptions.map((opt: string, oIdx: number) => {
                                                        const val = opt.replace(stripHtmlRegex, '').trim();
                                                        return <option key={oIdx} value={val}>{val}</option>;
                                                     })}
                                                   </select>
                                                )}
                                            </div>
                                          </div>
                                          
                                          {isReviewMode && q.explanation && (
                                             <div className="w-full mt-2 border-t border-gray-300 pt-3 flex-none basis-full font-sans">
                                                <p className="text-[12px] font-black text-amber-600 uppercase mb-2">💡 Giải thích đáp án:</p>
                                                <div className="text-[14px] text-gray-600 italic leading-relaxed font-serif format-passage html-content-renderer mb-3" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.explanation) }} />
                                                <div className="flex items-center gap-2">
                                                    <button 
                                                        onClick={(e) => { 
                                                            e.stopPropagation(); 
                                                            askAIToExplain(String(q.id), q.content, q.explanation); 
                                                        }} 
                                                        className="px-3 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded text-[12px] transition shadow-sm border border-[#064e3b]"
                                                    >
                                                        💬 Chat với AI
                                                    </button>
                                                    <button 
                                                        onClick={(e) => { 
                                                            e.stopPropagation(); 
                                                            callTutorForQuestion(String(q.id), q.content, q.explanation); 
                                                        }} 
                                                        className="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded text-[12px] transition shadow-sm border border-emerald-600 flex items-center gap-1"
                                                    >
                                                        📞 Gọi Gia sư
                                                    </button>
                                                </div>
                                             </div>
                                          )}
                                        </div>
                                      )
                                  })}
                                </div>
                             )}

                             {/* DẠNG CHECKBOX GROUP */}
                             {sec?.questionType === "Checkbox" && (
                                <div className="space-y-6">
                                  {(() => {
                                      const combos: any[][] = [];
                                      sec.questions?.forEach((q: any) => {
                                          const rawText = String(q.content || '').replace(/<[^>]*>/g, '').trim();
                                          const hasRealContent = rawText !== '' || String(q.content || '').includes('<img') || String(q.content || '').includes('<audio');
                                          if (combos.length === 0 || hasRealContent) {
                                              combos.push([q]);
                                          } else {
                                              combos[combos.length - 1].push(q);
                                          }
                                      });

                                      return combos.map((combo, comboIndex) => {
                                          const comboIds = combo.map((q: any) => String(q.id));
                                          const maxAllowed = combo.length;
                                          
                                          const userAnsArr = Array.from(new Set(comboIds.map(id => answers[id]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase()))));
                                          const correctAnsComboSet = new Set(combo.flatMap((q:any) => String(q.correctAnswer).split(',').map((x:string)=>x.trim().toUpperCase()).filter(Boolean)));
                                          const validOptions = combo[0]?.options?.filter((opt: any) => String(opt || '').trim() !== '') || [];
                                          
                                          let comboPoints = 0;
                                          userAnsArr.forEach((ans:string) => { 
                                              if (correctAnsComboSet.has(ans)) {
                                                  comboPoints++; 
                                              }
                                          });
                                          const isPerfect = comboPoints === maxAllowed;
                                          const isPartial = comboPoints > 0 && comboPoints < maxAllowed;

                                          let containerClass = "bg-white p-6 md:p-8 rounded-2xl shadow-sm border transition-colors relative group scroll-mt-20 mb-4 ";
                                          if (isReviewMode) {
                                              if (isPerfect) containerClass += "border-emerald-300 bg-emerald-50/30";
                                              else if (isPartial) containerClass += "border-amber-300 bg-amber-50/30";
                                              else containerClass += "border-red-300 bg-red-50/30";
                                          } else {
                                              containerClass += "border-slate-200 hover:border-[#0ea5e9]/40";
                                          }

                                          const handleComboChange = (optionValue: string, isChecked: boolean) => {
                                              setAnswers(prev => {
                                                  let currentSelected = Array.from(new Set(comboIds.map(id => prev[id]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase()))));
                                                  
                                                  if (isChecked) {
                                                      if (currentSelected.length >= maxAllowed) {
                                                          alert(`Lưu ý: Chỉ yêu cầu chọn tối đa ${maxAllowed} đáp án.`);
                                                          return prev;
                                                      }
                                                      if (!currentSelected.includes(optionValue)) {
                                                          currentSelected.push(optionValue);
                                                      }
                                                  } else {
                                                      currentSelected = currentSelected.filter((v:string) => v !== optionValue);
                                                  }
                                                  
                                                  const next = { ...prev };
                                                  comboIds.forEach((id, idx) => { 
                                                      next[id] = currentSelected[idx] || ''; 
                                                  }); 
                                                  return next;
                                              });
                                          };

                                          const qText = getCleanQuestionText(combo[0]?.content);
                                          const firstQIdx = questionIndexMap[comboIds[0]] || comboIds[0];
                                          const lastQIdx = questionIndexMap[comboIds[comboIds.length - 1]] || comboIds[comboIds.length - 1];
                                          const displayIndexText = comboIds.length > 1 ? `Câu ${firstQIdx}-${lastQIdx}` : `Câu ${firstQIdx}`;

                                          return (
                                             <div key={`combo-${comboIndex}`} id={`q-${combo[0].id}`} className={containerClass}>
                                               
                                               {!isReviewMode && (
                                                  <button 
                                                      onClick={() => toggleMark(String(combo[0].id))} 
                                                      className={`absolute top-6 right-6 transition-colors ${marked[String(combo[0].id)] ? 'text-amber-500' : 'text-slate-300 hover:text-slate-400'}`}
                                                  >
                                                     <BookmarkIcon filled={!!marked[String(combo[0].id)]} />
                                                  </button>
                                               )}
                                               
                                               {isReviewMode && (
                                                  <div className="absolute top-6 right-6 font-bold text-[12px]">
                                                     {isPerfect ? <span className="text-emerald-700 bg-emerald-100 px-3 py-1.5 rounded-lg">✅ Đúng hết</span> 
                                                     : isPartial ? <span className="text-amber-700 bg-amber-100 px-3 py-1.5 rounded-lg">⚠️ 1 phần</span>
                                                     : <span className="text-red-700 bg-red-100 px-3 py-1.5 rounded-lg">❌ Sai hết</span>}
                                                  </div>
                                               )}

                                               <div className="flex flex-col mb-4 pr-16">
                                                 <div className="font-bold text-white bg-slate-800 inline-block px-3 py-1 rounded w-fit text-[14px] mb-4">
                                                     {displayIndexText}
                                                 </div>
                                                 
                                                 {qText && (
                                                     <div 
                                                         className="text-[16px] font-medium leading-relaxed text-slate-800 mb-2 whitespace-pre-wrap" 
                                                         dangerouslySetInnerHTML={{ __html: qText }} 
                                                     />
                                                 )}
                                                 
                                                 <div className={`flex flex-col gap-2.5 mt-2`}>
                                                   {validOptions.map((opt: any, i: number) => {
                                                     const cleanOpt = getCleanOptionText(opt, i);
                                                     const optionValue = String.fromCharCode(65+i); 
                                                     const isSelected = userAnsArr.includes(optionValue); 
                                                     const isCorrectOpt = correctAnsComboSet.has(optionValue);
                                                     
                                                     let labelClass = "flex items-start gap-4 p-3 rounded-xl transition-colors border border-transparent -ml-3 ";
                                                     if (isReviewMode) { 
                                                        if (isCorrectOpt && isSelected) {
                                                            labelClass += " bg-emerald-50 border-emerald-400 font-bold text-emerald-900"; 
                                                        } else if (isCorrectOpt && !isSelected) {
                                                            labelClass += " bg-amber-50 border-amber-300 font-bold text-amber-800"; 
                                                        } else if (isSelected && !isCorrectOpt) {
                                                            labelClass += " bg-red-50 border-red-300 text-red-700 line-through opacity-70";
                                                        } else {
                                                            labelClass += " opacity-50 border-transparent bg-transparent"; 
                                                        }
                                                     } else { 
                                                        labelClass += " cursor-pointer hover:bg-slate-50 border-transparent bg-transparent"; 
                                                        if (isSelected) {
                                                            labelClass += " bg-blue-50/50 border-[#0ea5e9]/30 font-bold text-[#0ea5e9]";
                                                        }
                                                     }
                                                     
                                                     return (
                                                       <label key={i} className={labelClass}>
                                                         <input 
                                                             type="checkbox" 
                                                             checked={isSelected} 
                                                             onChange={(e) => handleComboChange(optionValue, e.target.checked)} 
                                                             className="mt-1 w-5 h-5 accent-[#0ea5e9] rounded cursor-pointer shrink-0" 
                                                             disabled={isReviewMode} 
                                                         />
                                                         <span className="text-[16px] leading-relaxed text-slate-800">
                                                             <span className="font-bold mr-2 font-sans">{optionValue}.</span> 
                                                             <span dangerouslySetInnerHTML={{ __html: cleanOpt }} />
                                                         </span>
                                                       </label>
                                                     )
                                                   })}
                                                 </div>
                                               </div>

                                               {isReviewMode && (
                                                 <div className="mt-6 ml-[3.5rem] pt-4 border-t border-slate-200 font-sans">
                                                    <p className="text-[12px] font-black text-amber-600 uppercase mb-3">💡 Giải thích đáp án:</p>
                                                    {combo.map((q:any) => {
                                                        if (!q.explanation || String(q.explanation).trim() === '') return null;
                                                        return (
                                                            <div key={q.id} className="text-[14px] text-gray-600 italic leading-relaxed mb-3 last:mb-0 border-l-[3px] border-slate-300 pl-4 bg-slate-50 py-3 pr-3 rounded-r-xl">
                                                                <span className="font-bold text-white px-2 py-0.5 bg-slate-800 rounded text-[11px] mr-2 font-sans not-italic">Câu {questionIndexMap[String(q.id)] || q.id}</span>
                                                                <span dangerouslySetInnerHTML={{ __html: q.explanation }} />
                                                                
                                                                <div className="flex items-center gap-2 mt-3 not-italic">
                                                                    <button 
                                                                        onClick={(e) => { 
                                                                            e.stopPropagation(); 
                                                                            askAIToExplain(String(q.id), q.content, q.explanation); 
                                                                        }} 
                                                                        className="px-3 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded text-[12px] transition shadow-sm border border-[#064e3b]"
                                                                    >
                                                                       💬 Chat với AI
                                                                    </button>
                                                                    <button 
                                                                        onClick={(e) => { 
                                                                            e.stopPropagation(); 
                                                                            callTutorForQuestion(String(q.id), q.content, q.explanation); 
                                                                        }} 
                                                                        className="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded text-[12px] transition shadow-sm border border-emerald-600 flex items-center gap-1"
                                                                    >
                                                                       📞 Gọi Gia sư
                                                                    </button>
                                                                </div>
                                                            </div>
                                                        )
                                                    })}
                                                 </div>
                                               )}
                                             </div>
                                          )
                                      });
                                  })()}
                                </div>
                             )}

                           </div>
                         );})}
                     </div>
                   );
                 })}
             </div>
          </div>

          {/* BẢNG PALETTE ĐIỀU HƯỚNG CÂU HỎI */}
          <aside className="w-full lg:w-[320px] shrink-0 lg:sticky top-4 h-auto lg:h-[calc(100vh-80px)] flex flex-col bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden z-20 m-4 lg:m-6 lg:ml-0">
            <div className="p-5 border-b border-slate-200 flex flex-col items-center">
              {isReviewMode ? (
                <div className="bg-emerald-50 text-emerald-700 p-6 rounded-2xl border border-emerald-100 w-full text-center shadow-sm mb-4">
                  <p className="text-[12px] font-bold uppercase tracking-widest mb-2">Kết quả của bạn</p>
                  <p className="text-5xl font-black mb-4">
                      {scoreResult.score} <span className="text-2xl text-emerald-400">/ {scoreResult.total}</span>
                  </p>
                  
                  {/* 🚀 NÚT GỌI GIA SƯ TỔNG QUAN */}
                  <button 
                      onClick={() => {
                        const tutorContext = {
                          overall: scoreResult.score + '/' + scoreResult.total,
                          transcript: `Bài test: ${basicInfo.title}. Điểm số của em là: ${scoreResult.score}/${scoreResult.total}.`,
                          feedback: "Học sinh vừa làm xong bài test. Hãy chúc mừng và đưa ra nhận xét chung. Hỏi xem học sinh có muốn bạn chữa câu nào cụ thể không."
                        };
                        sessionStorage.setItem('tony_live_mode', 'TUTOR');
                        sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
                        sessionStorage.setItem('tony_auto_start', 'true');
                        window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
                      }}
                      className="bg-emerald-600 hover:bg-emerald-500 text-white px-5 py-2.5 rounded-full text-[13px] font-bold transition uppercase tracking-wider shadow flex items-center justify-center gap-2 w-full"
                  >
                      📞 Gọi Gia Sư AI
                  </button>
                </div>
              ) : basicInfo?.category === 'exercise' ? (
                <div className="bg-emerald-50 text-emerald-600 px-6 py-2.5 rounded-lg font-black text-[18px] mb-4 border border-emerald-200 flex items-center justify-center gap-2 w-full shadow-sm tracking-widest uppercase">
                    BÀI TẬP
                </div>
              ) : (
                <div className="bg-red-50 text-red-500 px-6 py-2.5 rounded-lg font-bold text-[18px] mb-4 border border-red-100 flex items-center justify-center gap-2 w-full shadow-sm tracking-wider">
                  <span className="text-red-400">⏱</span> {formatTime(timeLeft)} phút
                </div>
              )}
              
              <div className="w-full text-[14px] font-bold text-slate-800 mb-3 text-left">
                  Danh sách câu hỏi
              </div>
              
              <div className="w-full flex flex-wrap gap-x-4 gap-y-2 text-[12px] font-medium text-slate-600 mb-2">
                 <div className="flex items-center gap-1.5">
                     <div className="w-3 h-3 rounded-full bg-slate-200"></div> Chưa trả lời ({totalCount - answeredCount})
                 </div>
                 <div className="flex items-center gap-1.5">
                     <div className="w-3 h-3 rounded-full bg-[#0ea5e9]"></div> Đã trả lời ({answeredCount})
                 </div>
                 {!isReviewMode && (
                   <div className="flex items-center gap-1.5 w-full mt-1">
                       <div className="w-3 h-3 rounded-full border-2 border-amber-500 bg-amber-50"></div> Đánh dấu ({markedCount})
                   </div>
                 )}
              </div>
            </div>
            
            <div className="flex-1 overflow-y-auto p-5 custom-scrollbar bg-white">
              <p className="text-[12px] text-slate-400 mb-4">Bấm vào ô để đến câu hỏi</p>
              <div className="grid grid-cols-5 gap-2">
                {allQuestionIds.map(id => {
                  let isAns = answers[id] && answers[id].trim() !== '';
                  const isMarked = marked[id];
                  let btnStyle = 'bg-slate-100 text-slate-600 hover:bg-slate-200'; 
                  
                  const section = parts.flatMap((p: any) => p.sections || []).find((s:any) => s.questions?.some((sq:any)=>String(sq.id)===id));
                  const qType = section?.questionType;

                  if (!isReviewMode && qType === 'Checkbox') {
                      const combos: any[][] = [];
                      section.questions?.forEach((q: any) => {
                          const rawText = String(q.content || '').replace(/<[^>]*>/g, '').trim();
                          const hasRealContent = rawText !== '' || String(q.content || '').includes('<img') || String(q.content || '').includes('<audio');
                          if (combos.length === 0 || hasRealContent) {
                              combos.push([q]);
                          } else {
                              combos[combos.length - 1].push(q);
                          }
                      });
                      const myCombo = combos.find((c: any[]) => c.some((q:any) => String(q.id) === id));
                      if (myCombo) {
                          const comboIds = myCombo.map((q:any) => String(q.id));
                          const userAnsArr = Array.from(new Set(comboIds.map(cid => answers[cid]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim()))));
                          const idxInCombo = comboIds.indexOf(id);
                          isAns = idxInCombo < userAnsArr.length;
                      }
                  }

                  if (isReviewMode) {
                    let isCorrect = false;
                    if (qType === 'Checkbox') {
                        const combos: any[][] = [];
                        parts.flatMap((p:any) => p.sections || []).forEach(sec => {
                            if (sec.questionType === 'Checkbox') {
                               const c: any[][] = [];
                               sec.questions?.forEach((q: any) => {
                                   const rawText = String(q.content || '').replace(/<[^>]*>/g, '').trim();
                                   const hasRealContent = rawText !== '' || String(q.content || '').includes('<img') || String(q.content || '').includes('<audio');
                                   if (c.length === 0 || hasRealContent) {
                                       c.push([q]); 
                                   } else {
                                       c[c.length - 1].push(q);
                                   }
                               });
                               combos.push(...c);
                            }
                        });
                        const myCombo = combos.find(c => c.some((q:any) => String(q.id) === id)) || [];
                        if (myCombo.length > 0) {
                            const comboIds = myCombo.map((q:any) => String(q.id));
                            const userAnsSet = new Set(comboIds.map(cid => answers[cid]).filter(v => v && v.trim() !== '').flatMap(x => x.split(',').map(v=>v.trim().toUpperCase())));
                            const correctAnsSet = new Set(myCombo.flatMap((q:any)=>String(q.correctAnswer || '').split(',').map((x:string)=>x.trim().toUpperCase()).filter(Boolean)));
                            let pts = 0; 
                            userAnsSet.forEach((v:string) => { 
                                if(correctAnsSet.has(v)) {
                                    pts++; 
                                }
                            });
                            const idxInCombo = comboIds.indexOf(id);
                            isCorrect = idxInCombo < pts;
                        }
                    } else {
                        const q = section?.questions.find((q:any) => String(q.id) === id);
                        isCorrect = q && answers[id]?.trim().toUpperCase() === String(q.correctAnswer || '').trim().toUpperCase();
                    }
                    btnStyle = isCorrect ? 'bg-emerald-100 text-emerald-700' : 'bg-red-100 text-red-700';
                  } else if (isAns) { 
                    btnStyle = 'bg-[#0ea5e9] text-white shadow-sm'; 
                  }
                  
                  return (
                    <button 
                        key={id} 
                        onClick={() => scrollToQuestion(id)} 
                        className={`relative h-9 w-9 mx-auto flex items-center justify-center rounded-full text-[13px] font-medium transition-all ${btnStyle} ${!isReviewMode && isMarked ? 'ring-2 ring-amber-400 ring-offset-1 bg-amber-50' : ''}`}
                    >
                      {questionIndexMap[id]}
                    </button>
                  )
                })}
              </div>
            </div>

            <div className="p-5 border-t border-slate-200 bg-white shrink-0">
              <button 
                  onClick={handleFinish} 
                  className={`w-full text-white font-bold py-3 rounded-xl transition-colors shadow-sm text-[14px] ${isReviewMode ? 'bg-emerald-600 hover:bg-emerald-700' : 'bg-[#2b85c4] hover:bg-[#1d6b9e]'}`}
              >
                {isReviewMode ? 'Thoát Xem Lại' : 'Nộp bài'}
              </button>
            </div>
          </aside>

        </div>
      </div>
    );
  };

  return (
    <React.Fragment>
      {/* Audio: ẩn khi test, hiện controls khi review */}
      {isListening && globalAudio && (
        <audio 
            ref={globalAudioRef} 
            src={globalAudio} 
            preload="auto" 
            controls={isReviewMode}
            className={isReviewMode ? 'fixed bottom-4 left-1/2 -translate-x-1/2 z-50 w-[90%] max-w-xl shadow-2xl rounded-full' : 'hidden'}
        />
      )}

      {!testStarted ? (
        <div className="flex flex-col h-[100dvh] items-center justify-center bg-[#f8fafc] font-sans p-4">
          <div className="bg-white p-10 md:p-12 rounded-3xl shadow-2xl border border-slate-200 w-full max-w-xl text-center animate-in zoom-in-95 duration-300">
            <div className="w-24 h-24 bg-blue-50 border border-blue-100 rounded-full flex items-center justify-center mx-auto mb-6 shadow-inner text-[#0ea5e9]">
               <span className="text-5xl">{(isListening && hasAnyAudio) ? '🎧' : '📖'}</span>
            </div>
            
            <h1 className="text-[24px] md:text-[28px] font-black text-slate-800 mb-3 leading-tight">
                {basicInfo?.title}
            </h1>
            
            <div className="flex items-center justify-center gap-2 text-slate-500 mb-8 font-medium bg-slate-50 inline-flex px-5 py-2.5 rounded-xl border border-slate-100 mx-auto">
               {basicInfo?.category === 'exercise' ? (
                   <span className="text-emerald-600 font-black tracking-widest uppercase">BÀI TẬP</span>
               ) : (
                   <>
                       <span className="text-lg">⏱</span> Thời gian làm bài: <span className="font-bold text-slate-800">{formatTime(parseInitialTime(basicInfo?.timeLimit))}</span>
                   </>
               )}
            </div>
            
            {(isListening && hasAnyAudio) && (
              <div className="bg-amber-50 border border-amber-200 p-5 rounded-xl text-amber-800 text-[14px] font-medium mb-8 text-left leading-relaxed shadow-sm flex items-start gap-4">
                <span className="text-2xl mt-1">⚠️</span>
                <div>
                   <span className="font-black block mb-1">LƯU Ý BÀI THI LISTENING</span> 
                   File âm thanh sẽ được <span className="font-bold underline">tự động phát</span> ngay khi bạn bấm nút Bắt Đầu bên dưới. Vui lòng đeo tai nghe và kiểm tra lại âm lượng thiết bị.
                </div>
              </div>
            )}

            <div className="flex flex-col sm:flex-row gap-3 justify-center mt-2">
              <button 
                  onClick={onBack} 
                  className="w-full sm:w-auto flex-1 bg-white px-8 py-4 rounded-xl font-bold text-slate-600 hover:text-slate-800 hover:bg-slate-50 border border-slate-200 transition-colors uppercase tracking-widest text-[13px] shadow-sm"
              >
                  Quay lại
              </button>
              <button 
                  onClick={handleStartTest} 
                  className="w-full sm:w-auto flex-[2] bg-[#0ea5e9] hover:bg-[#0284c7] text-white font-black px-10 py-4 rounded-xl shadow-lg transition-colors uppercase tracking-widest text-[13px] active:scale-95"
              >
                  Bắt Đầu Làm Bài
              </button>
            </div>
          </div>
        </div>
      ) : (
        renderTestLayout()
      )}
    </React.Fragment>
  );
}