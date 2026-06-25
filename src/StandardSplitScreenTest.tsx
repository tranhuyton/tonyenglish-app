import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import { supabase } from './supabase';
import { CustomAudioPlayer } from './CustomAudioPlayer';
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
          .replace(/(?:^|;)\s*(max-width|width|max-height|min-height|height|overflow|overflow-y|overflow-x)\s*:[^;]+/gi, '')
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

const parseStyle = (styleStr: string) => {
  const style: any = {};
  if (!styleStr) return style;
  styleStr.split(';').forEach(s => {
    const match = s.match(/^\s*([\w-]+)\s*:\s*(.+)\s*$/);
    if (match) {
      const [, key, val] = match;
      const lowerKey = key.toLowerCase();
      if (['height', 'max-height', 'min-height', 'overflow', 'overflow-y', 'overflow-x'].includes(lowerKey)) return;
      const camelKey = key.replace(/-([a-z])/g, g => g[1].toUpperCase());
      style[camelKey] = val;
    }
  });
  return style;
};

// =========================================================================================
// COMPONENT CHÍNH QUẢN LÝ BÀI THI STANDARD TEST
// =========================================================================================
export default function StandardSplitScreenTest({ 
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
  
  const isListening = basicInfo.skill?.toLowerCase() === 'listening' || basicInfo.category?.toLowerCase() === 'ielts-listening' || safeData?.test_type === 'IELTS-Listening';
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
  
  const [currentPartIndex, setCurrentPartIndex] = useState(0);
  
  const [showPalette, setShowPalette] = useState(false); 
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [showSettings, setShowSettings] = useState(false);
  const [fontSize, setFontSize] = useState<'S' | 'M' | 'L'>('M');
  
  const globalAudioRef = useRef<HTMLAudioElement>(null);
  const isFinishingRef = useRef(false);

  const [leftWidth, setLeftWidth] = useState(50); 
  const [isMobile, setIsMobile] = useState(window.innerWidth < 768);
  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 768);
    };
    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);
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

  const isDragging = useRef(false);

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
  
  const onDrag = (e: MouseEvent | TouchEvent) => {
    const clientX = 'touches' in e ? e.touches[0]?.clientX : e.clientX;
    if (clientX === undefined) return;
    
    if (isDragging.current && containerRef.current) {
        const containerRect = containerRef.current.getBoundingClientRect(); 
        const newLeftWidth = ((clientX - containerRect.left) / containerRect.width) * 100;
        if (newLeftWidth >= 10 && newLeftWidth <= 90) {
            setLeftWidth(newLeftWidth);
        }
    }
  };

  useEffect(() => {
      window.addEventListener('mousemove', onDrag); 
      window.addEventListener('mouseup', stopDrag); 
      window.addEventListener('touchmove', onDrag, { passive: false }); 
      window.addEventListener('touchend', stopDrag); 
      
      return () => {
          window.removeEventListener('mousemove', onDrag); 
          window.removeEventListener('mouseup', stopDrag); 
          window.removeEventListener('touchmove', onDrag); 
          window.removeEventListener('touchend', stopDrag); 
      };
  }, []);

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

  const [draggedOption, setDraggedOption] = useState<string | null>(null);

  // Dictionary popup state
  const [dictPopup, setDictPopup] = useState<{ show: boolean, word: string, x: number, y: number, rectTop: number, data: any, isLoading: boolean } | null>(null);

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

        } else if (qType === 'Đoạn văn') {
           s?.questions?.forEach((q: any) => {
             if (!q?.id) return;
             questionTypeStats[qType].total++;
             // Paragraphs are AI graded, so we skip adding them to the global auto-graded score/total
           });
        } else {
           s?.questions?.forEach((q: any) => {
             if (!q?.id) return;
             total++; 
             questionTypeStats[qType].total++;
             
             const uAns = String(answers[String(q.id)] || '').trim();
             const cAns = String(q.correctAnswer || '').trim();
             
             if (isAnswerCorrect(uAns, cAns)) { 
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
      const { data: { user } } = await supabase.auth.getSession().then(({data}) => ({ data: { user: data.session?.user } }));
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

  // Cuộn lên đầu trang khi đổi Part
  useEffect(() => {
    setTimeout(() => {
        if (leftPaneRef.current) leftPaneRef.current.scrollTop = 0;
        if (rightPaneRef.current) rightPaneRef.current.scrollTop = 0;
    }, 10);
  }, [currentPartIndex]);

  const formatTime = (sec: number) => {
    const m = Math.floor(sec / 60).toString().padStart(2, '0');
    const s = (sec % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  };

  const scrollToQuestion = (id: string) => {
    const targetPartIndex = questionToPartMap[String(id)];
    if (targetPartIndex !== undefined && targetPartIndex !== currentPartIndex) {
      setCurrentPartIndex(targetPartIndex);
      
      let attempts = 0;
      const checkAndScroll = () => {
        const el = document.getElementById(`q-${id}`);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
          el.classList.add('ring-4', 'ring-[#0ea5e9]/40', 'rounded-xl');
          setTimeout(() => {
              el.classList.remove('ring-4', 'ring-[#0ea5e9]/40', 'rounded-xl');
          }, 1500);
        } else if (attempts < 15) {
          attempts++;
          setTimeout(checkAndScroll, 100);
        }
      };
      setTimeout(checkAndScroll, 100);
      
    } else {
      const el = document.getElementById(`q-${id}`);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        el.classList.add('ring-4', 'ring-[#0ea5e9]/40', 'rounded-xl');
        setTimeout(() => {
            el.classList.remove('ring-4', 'ring-[#0ea5e9]/40', 'rounded-xl');
        }, 1500);
      }
    }
    setShowPalette(false);
  };

  // Quét ID câu hỏi để tạo Bảng điều hướng
  const { allQuestionIds, questionIndexMap, questionToPartMap, questionDataMap } = useMemo(() => {
    const ids: string[] = [];
    const partMap: Record<string, number> = {};
    const dataMap: Record<string, { qType: string, options: string[] }> = {};
    parts?.forEach((p: any, pIdx: number) => {
      p?.sections?.forEach((s: any) => {
        if (Array.isArray(s?.questions)) {
          s.questions.forEach((q: any) => {
            const qIdStr = String(q.id);
            if (q?.id && !ids.includes(qIdStr)) {
              ids.push(qIdStr);
              partMap[qIdStr] = pIdx;
              dataMap[qIdStr] = { qType: s.questionType, options: q.options || [] };
            }
          });
        }
        if (["Điền từ", "Điền khuyết", "Kéo thả vào Part", "Kéo thả", "Matching", "Droplist"].includes(s?.questionType)) {
          const combinedContent = String(s?.content || '') + ' ' + String(s?.questions?.[0]?.content || '');
          const matches = combinedContent.match(/\[\s*\d+\s*\]/g);
          if (matches) {
            matches.forEach((m: string) => {
              const num = m.replace(/\D/g, '').trim();
              if (!ids.includes(num)) {
                ids.push(num);
                partMap[num] = pIdx;
                const qInSec = (s.questions || []).find((qq: any) => String(qq.id) === num);
                dataMap[num] = { qType: s.questionType, options: qInSec?.options || s.questions?.[0]?.options || [] };
              }
            });
          }
        }
      });
    });
    
    ids.sort((a, b) => parseInt(a) - parseInt(b));
    const map = ids.reduce((acc: any, id: string, idx: number) => { 
        acc[id] = idx + 1; 
        return acc; 
    }, {});
    
    return { allQuestionIds: ids, questionIndexMap: map, questionToPartMap: partMap, questionDataMap: dataMap };
  }, [parts]);
  const handleDragScroll = useCallback((e: React.DragEvent<HTMLDivElement>) => {
    if (e.clientY === 0) return;
    const container = rightPaneRef.current;
    if (!container) return;
    const rect = container.getBoundingClientRect();
    const buffer = 80;
    const speed = 15;
    if (e.clientY - rect.top < buffer && e.clientY - rect.top > -50) {
      container.scrollTop -= speed;
    } else if (rect.bottom - e.clientY < buffer && rect.bottom - e.clientY > -50) {
      container.scrollTop += speed;
    }
  }, []);

  const { answeredCount, markedCount, totalCount } = useMemo(() => {
    return {
      answeredCount: Object.keys(answers).filter(k => answers[k] && answers[k].trim() !== '').length,
      markedCount: Object.values(marked).filter(Boolean).length,
      totalCount: allQuestionIds.length
    }
  }, [answers, marked, allQuestionIds]);

  const getCleanQuestionText = (htmlContent: string) => {
    let txt = cleanHtmlContent(String(htmlContent || '')).trim();
    txt = txt.replace(/^<p[^>]*>/i, '').replace(/<\/p>$/i, '').trim();
    const stripped = txt.replace(/^(<[^>]+>)*(Câu\s*\d+|\d+[\-\d]*)\s*[\.\):]?\s*(<\/[^>]+>)*\s*/i, '').trim();
    if (stripped.length > 0) txt = stripped;
    return txt;
  };

  const getCleanOptionText = (opt: string, index: number) => {
    let cleanOpt = cleanHtmlContent(String(opt || '')).replace(/^<p[^>]*>/i, '').replace(/<\/p>$/i, '').trim();
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

  // =========================================================================================
  // TỪ ĐIỂN BÔI ĐEN TRA TỪ (Dictionary Lookup)
  // =========================================================================================
  const triggerDictionary = useCallback((word: string, x: number, y: number, rectTop: number) => {
    setDictPopup({ show: true, word, x, y, rectTop, data: null, isLoading: true });
    Promise.allSettled([
      fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(word)}`)
        .then(r => r.ok ? r.json() : Promise.reject()),
      fetch(`https://api.mymemory.translated.net/get?q=${encodeURIComponent(word)}&langpair=en|vi`)
        .then(r => r.json())
    ]).then(([enRes, viRes]) => {
      let phonetics = '';
      let audio = '';
      let translation = 'Không tìm thấy bản dịch.';
      if (enRes.status === 'fulfilled' && enRes.value[0]) {
        phonetics = enRes.value[0].phonetics?.find((p:any) => p.text)?.text || '';
        audio = enRes.value[0].phonetics?.find((p:any) => p.audio)?.audio || '';
      }
      if (viRes.status === 'fulfilled' && viRes.value?.responseData?.translatedText) {
        translation = viRes.value.responseData.translatedText;
      }
      setDictPopup(prev => prev ? { ...prev, data: { phonetics, audio, translation }, isLoading: false } : null);
    });
  }, []);

  const handleTextSelection = useCallback(() => {
    setTimeout(() => {
      const selection = window.getSelection();
      if (!selection || selection.rangeCount === 0) return;
      const text = selection.toString().trim();
      if (!text) return;
      if (text.length > 0 && text.length < 40 && text.split(' ').length <= 4) {
        const range = selection.getRangeAt(0);
        const rect = range.getBoundingClientRect();
        triggerDictionary(text, rect.left + (rect.width / 2), rect.bottom, rect.top);
      }
    }, 100);
  }, [triggerDictionary]);

  // Close dictionary popup when clicking outside
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      const dictPop = document.getElementById('std-dict-popup');
      if (dictPop && !dictPop.contains(e.target as Node)) {
        setDictPopup(null);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // Drag-drop handlers
  const onDragStart = (e: React.DragEvent<HTMLDivElement>, option: string) => {
    if (isReviewMode) return;
    e.stopPropagation();
    setDraggedOption(option);
  };

  const onDrop = (qId: string) => {
    if (isReviewMode || !draggedOption) return;
    handleAnswer(qId, draggedOption);
    setDraggedOption(null);
  };

  const clearDragAnswer = (qId: string) => {
    if (isReviewMode) return;
    handleAnswer(qId, '');
  };

  // =========================================================================================
  // renderHtmlWithHoles - DOMParser-based renderer for drag-drop, inline droplist, matching
  // =========================================================================================
  const renderHtmlWithHoles = (htmlStr: any, sec: any) => {
    if (!htmlStr) return null;
    const safeText = String(htmlStr);

    if (typeof window === 'undefined') {
      return <span className="html-content-renderer" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(safeText) }} />;
    }

    const processedHtml = safeText.replace(/\[\s*(\d+)\s*\]/g, '<hole data-id="$1"></hole>');
    const cleanProcessedHtml = cleanHtmlContent(processedHtml);
    const parser = new DOMParser();
    const doc = parser.parseFromString(cleanProcessedHtml, 'text/html');

    const sectionQIds = (sec?.questions || []).map((q: any) => String(q.id));
    const selectedInSec = sectionQIds.map((id: string) => answers[id]?.trim().toUpperCase()).filter(Boolean);

    const renderNode = (node: ChildNode, pathKey: string): React.ReactNode => {
      if (node.nodeType === Node.TEXT_NODE) return node.textContent;
      if (node.nodeType === Node.ELEMENT_NODE) {
        const el = node as HTMLElement;
        const tagName = el.tagName.toLowerCase();

        if (tagName === 'hole') {
          const qNum = el.getAttribute('data-id');
          if (!qNum) return null;

          const userAns = String(answers[qNum] || '');
          const displayIndex = questionIndexMap[qNum] || qNum;
          const qInfo = questionDataMap[qNum] || { qType: sec?.questionType || 'Điền từ', options: [] };

          if (isReviewMode) {
            const qData = parts.flatMap((p: any) => Array.isArray(p?.sections) ? p.sections.flatMap((s: any) => s?.questions) : []).find((q: any) => String(q?.id) === String(qNum));
            const correctAns = String(qData?.correctAnswer || '');
            const isCorrect = isAnswerCorrect(userAns, correctAns);

            let displayUserAnsForReview = userAns;
            if (["Kéo thả", "Kéo thả vào Part", "Matching"].includes(sec.questionType)) {
              let allOpts: string[] = [];
              (sec?.questions || []).forEach((q: any) => {
                (q.options || []).forEach((o: any) => {
                  const cOpt = String(o).replace(stripHtmlRegex, '').trim();
                  if (cOpt && !allOpts.includes(cOpt)) allOpts.push(cOpt);
                });
              });
              if (userAns && /^[A-Z]$/i.test(userAns)) {
                const oIdx = userAns.toUpperCase().charCodeAt(0) - 65;
                if (allOpts[oIdx]) displayUserAnsForReview = allOpts[oIdx].replace(/^[A-Z][\.\):]\s*/i, '');
              } else if (userAns) {
                displayUserAnsForReview = userAns.replace(/^[A-Z][\.\):]\s*/i, '');
              }
            }

            return (
              <span key={pathKey} id={`q-${qNum}`} className="relative inline-flex flex-col items-center align-top mx-1.5 mt-1 group" style={{ textIndent: 0 }}>
                <span className={`px-2.5 py-0.5 text-[14px] font-bold text-white rounded-md shadow-sm border ${isCorrect ? 'bg-emerald-600 border-emerald-700' : 'bg-red-500 border-red-600'}`}>
                  {displayIndex}. {displayUserAnsForReview || '(trống)'}
                </span>
                {!isCorrect && (
                  <span className="absolute top-full left-1/2 -translate-x-1/2 mt-1.5 text-[11px] text-emerald-800 font-bold bg-emerald-100 px-2 py-0.5 border border-emerald-300 rounded text-center whitespace-nowrap z-10 shadow-sm opacity-0 group-hover:opacity-100 transition-opacity">
                    ĐA: {correctAns}
                  </span>
                )}
              </span>
            );
          }

          // Drag-drop / Matching: drop target
          if (["Kéo thả", "Kéo thả vào Part", "Matching"].includes(sec.questionType)) {
            let allOpts: string[] = [];
            (sec?.questions || []).forEach((q: any) => {
              (q.options || []).forEach((o: any) => {
                const cOpt = String(o).replace(stripHtmlRegex, '').trim();
                if (cOpt && !allOpts.includes(cOpt)) allOpts.push(cOpt);
              });
            });
            let displayUserAns = userAns;
            if (userAns && /^[A-Z]$/i.test(userAns)) {
              const oIdx = userAns.toUpperCase().charCodeAt(0) - 65;
              if (allOpts[oIdx]) displayUserAns = allOpts[oIdx].replace(/^[A-Z][\.\):]\s*/i, '');
            } else if (userAns) {
              displayUserAns = userAns.replace(/^[A-Z][\.\):]\s*/i, '');
            }

            return (
              <span
                key={pathKey}
                id={`q-${qNum}`}
                onDragOver={(e) => e.preventDefault()}
                onDrop={() => onDrop(qNum)}
                className={`inline-flex items-center justify-center align-middle mx-1 my-1 min-w-[120px] h-[32px] border rounded-lg transition-all px-2 cursor-pointer border-slate-300 bg-white hover:bg-slate-50 shadow-sm`}
                style={{ textIndent: 0 }}
              >
                <span className="shrink-0 inline-flex items-center justify-center leading-none font-bold text-white bg-slate-800 px-1.5 min-w-[24px] h-[24px] text-[12px] mr-2 rounded" style={{ color: '#ffffff', textIndent: 0 }}>
                  {displayIndex}
                </span>
                {userAns ? (
                  <div className="flex items-center justify-between w-full text-[#0ea5e9] font-sans text-[14px] font-bold" style={{ textIndent: 0 }}>
                    <span className="truncate">{displayUserAns}</span>
                    <button onClick={(e) => { e.stopPropagation(); clearDragAnswer(qNum); }} className="ml-2 hover:text-red-500 text-[14px] font-black font-sans">✕</button>
                  </div>
                ) : (
                  <span className="text-slate-400 text-[13px] italic font-sans w-full text-center" style={{ textIndent: 0 }}>Thả vào đây</span>
                )}
              </span>
            );
          }

          // Inline Droplist
          if (qInfo.qType === 'Droplist' || sec.questionType === 'Droplist') {
            const rawOptions = (qInfo.options && qInfo.options.length > 0) ? qInfo.options : (sec.questions?.[0]?.options || []);
            const validOptions = rawOptions.filter(Boolean);

            return (
              <span key={pathKey} id={`q-${qNum}`} className="inline-flex items-center align-middle mx-1 my-1 whitespace-nowrap" style={{ textIndent: 0 }}>
                <span className="shrink-0 inline-flex items-center justify-center leading-none text-white font-bold px-2 min-w-[28px] h-[30px] text-[13px] rounded-l-lg border border-slate-800 border-r-0 bg-slate-800" style={{ color: '#ffffff', textIndent: 0 }}>
                  {displayIndex}
                </span>
                <select
                  value={userAns}
                  onChange={(e) => handleAnswer(qNum, e.target.value)}
                  className="shrink-0 bg-white border border-slate-300 text-[#0ea5e9] font-bold font-sans text-[14px] h-[30px] px-1 rounded-r-lg outline-none focus:border-[#0ea5e9] cursor-pointer min-w-[100px] max-w-[200px] truncate"
                  style={{ textIndent: 0 }}
                >
                  <option value="">-- Chọn --</option>
                  {validOptions.map((opt: string, oIdx: number) => {
                    const val = opt.replace(stripHtmlRegex, '').trim();
                    const isSelectedElsewhere = selectedInSec.includes(val.toUpperCase()) && userAns.trim().toUpperCase() !== val.toUpperCase();
                    return (
                      <option key={oIdx} value={val}>
                        {val} {isSelectedElsewhere ? '(Đã chọn)' : ''}
                      </option>
                    );
                  })}
                </select>
              </span>
            );
          }

          // Default: Điền từ input
          return (
            <span key={pathKey} id={`q-${qNum}`} className="inline-flex items-center align-middle mx-1.5 scroll-mt-24" style={{ textIndent: 0 }}>
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

        // Generic HTML element rendering
        const props: any = { key: pathKey };
        Array.from(el.attributes).forEach(attr => {
          if (attr.name === 'class') {
            props.className = attr.value;
          } else if (attr.name === 'style') {
            props.style = parseStyle(attr.value);
          } else if (attr.name === 'for') {
            props.htmlFor = attr.value;
          } else if (attr.name.startsWith('data-') || attr.name.startsWith('aria-')) {
            props[attr.name] = attr.value;
          } else {
            const camelCaseAttr = attr.name.replace(/-([a-z])/g, g => g[1].toUpperCase());
            const reactProp = attr.name === 'colspan' ? 'colSpan' : attr.name === 'rowspan' ? 'rowSpan' : attr.name === 'cellpadding' ? 'cellPadding' : attr.name === 'cellspacing' ? 'cellSpacing' : attr.name === 'tabindex' ? 'tabIndex' : camelCaseAttr;
            props[reactProp] = attr.value;
          }
        });

        const children = Array.from(el.childNodes).map((child, i) => renderNode(child, `${pathKey}-${i}`));
        const voidElements = ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'];

        if (tagName === 'table') {
          props.className = `${props.className || ''} w-full border-collapse border border-slate-700 text-[15px]`.trim();
        } else if (tagName === 'th') {
          props.className = `${props.className || ''} border border-slate-700 bg-slate-100 p-3 font-bold text-left text-slate-800`.trim();
        } else if (tagName === 'td') {
          props.className = `${props.className || ''} border border-slate-700 p-3 text-left align-top`.trim();
        }

        if (voidElements.includes(tagName)) {
          return React.createElement(tagName, props);
        }

        const element = React.createElement(tagName, props, children.length > 0 ? children : null);
        if (tagName === 'table') {
          return React.createElement('div', { key: `${pathKey}-wrapper`, className: 'w-full overflow-x-auto custom-scrollbar my-6' }, element);
        }
        return element;
      }
      return null;
    };

    return Array.from(doc.body.childNodes).map((node, i) => renderNode(node, `root-${i}`));
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
      return <span key={index} dangerouslySetInnerHTML={{ __html: cleanHtmlContent(partText || '') }} />;
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

          {/* Nút Gọi Gia Sư AI đã bị gỡ theo yêu cầu */}

          <div className="flex items-center gap-6">
            {/* LABEL AND TIMER (TOP RIGHT) */}
            {!isReviewMode && testStarted && (
               <div className="flex items-center gap-3">
                 {basicInfo?.category === 'exercise' ? (
                     <span className="text-[#0ea5e9] font-black tracking-[0.2em] uppercase text-[15px]">BÀI TẬP</span>
                 ) : (
                     <>
                         <span className="text-rose-500 font-black tracking-[0.2em] uppercase text-[15px]">ĐỀ THI</span>
                         <div className="flex items-center gap-1.5 text-rose-600 bg-rose-50 px-3 py-1 rounded-lg border border-rose-100">
                             <span className="text-[14px]">⏱️</span> 
                             <span className="font-mono font-bold tracking-widest text-[16px]">{formatTime(timeLeft)}</span>
                         </div>
                     </>
                 )}
               </div>
            )}

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
            {isReviewMode && (
               <button 
                   onClick={() => {
                       if (window.confirm("Bạn có chắc chắn muốn làm lại bài thi này? Mọi kết quả cũ sẽ bị xóa.")) {
                           if (safeData?.id) {
                               localStorage.removeItem(`std_ans_${safeData.id}`);
                               localStorage.removeItem(`standard_mark_${safeData.id}`);
                               localStorage.removeItem(`standard_endtime_${safeData.id}`);
                           }
                           window.location.reload();
                       }
                   }} 
                   className="text-[13px] font-bold px-4 py-2 rounded-lg transition-colors flex items-center gap-2 shadow-sm border bg-emerald-600 text-white border-emerald-500 hover:bg-emerald-800"
               >
                 ↺ Làm lại
               </button>
            )}
            <button 
                onClick={handleExit} 
                className={`text-[13px] font-bold px-4 py-2 rounded-lg transition-colors flex items-center gap-2 shadow-sm border ${isReviewMode ? 'bg-emerald-600 text-white border-emerald-500 hover:bg-emerald-800' : 'bg-white hover:bg-slate-50 text-slate-600 border-slate-200'}`}
            >
              Thoát
            </button>
          </div>
        </header>

        {/* TAB BAR FOR NAVIGATION BETWEEN PARTS */}
        {parts.length > 1 && !isListening && (
          <div className={`border-b border-slate-200 px-6 pt-2 pb-0 flex gap-4 overflow-x-auto shrink-0 font-sans ${isReviewMode ? 'bg-emerald-50' : 'bg-white'}`}>
            {parts.map((p: any, index: number) => {
              const isActive = currentPartIndex === index;
              return (
                <button 
                  key={index} 
                  onClick={() => setCurrentPartIndex(index)} 
                  className={`px-4 py-2 text-[14px] font-bold transition-all whitespace-nowrap border-b-[3px] rounded-none ${isActive ? (isReviewMode ? 'text-emerald-700 border-emerald-600' : 'text-[#0ea5e9] border-[#0ea5e9]') : 'text-slate-500 border-transparent hover:text-slate-800'}`}
                >
                  {p.title || `Part ${index + 1}`}
                </button>
              )
            })}
          </div>
        )}

        <main className="flex flex-1 overflow-hidden relative bg-[#eeeeee]" ref={containerRef} onClick={() => showSettings && setShowSettings(false)}>
          
          {/* PANEL TRÁI (BÀI ĐỌC) - ẨN ĐI NẾU LÀ BÀI LISTENING */}
          {!isListening && (
            <React.Fragment>
              <div className="flex flex-col h-full bg-white relative" style={{ width: window.innerWidth > 768 ? `${leftWidth}%` : '100%', flex: 'none' }}>
                <section 
                    className={`p-8 md:p-10 overflow-y-auto custom-scrollbar flex-1 relative ${fontSize === 'S' ? 'text-[14px]' : fontSize === 'L' ? 'text-[18px]' : 'text-[16px]'}`} 
                    ref={leftPaneRef as any} 
                    onMouseUp={handleTextSelection}
                >
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
                    if (parts.length > 1 && !isListening && pIdx !== currentPartIndex) return null;
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
                        
                        {(isReviewMode || basicInfo?.category === 'exercise') && pIdx === 0 && globalAudio && (
                            <CustomAudioPlayer ref={globalAudioRef} src={globalAudio} className="mb-6 w-full" />
                        )}
                        
                        {part?.content && (
                          <div 
                              className="prose prose-slate max-w-none text-slate-800 text-[16px] leading-[1.9] whitespace-pre-wrap mb-8 text-justify bg-slate-50 p-6 md:p-8 rounded-2xl border border-slate-200 shadow-sm" 
                              dangerouslySetInnerHTML={{ __html: cleanHtmlContent(part.content || '') }} 
                          />
                        )}
                        
                        {/* Removed part?.sections?.map from left pane. Instructions belong in the right pane. */}
                      </div>
                    );
                  })}
                </section>
              </div>

              {/* THANH KÉO THẢ RESIZER */}
              <div 
                onMouseDown={startDrag}
                onTouchStart={startDrag}
                className="w-4 bg-[#e8e8e8] border-x border-[#c0c0c0] hover:bg-[#d4d4d4] cursor-col-resize flex flex-col justify-center items-center z-10 shrink-0 transition-colors shadow-sm"
                title="Kéo để điều chỉnh độ rộng"
              >
                 <div className="flex flex-col gap-1.5 opacity-40">
                    <div className="w-1 h-1 bg-black"></div>
                    <div className="w-1 h-1 bg-black"></div>
                    <div className="w-1 h-1 bg-black"></div>
                    <div className="w-1 h-1 bg-black"></div>
                 </div>
              </div>
            </React.Fragment>
          )}

          {/* PANEL PHẢI (CÂU HỎI VÀ NỘI DUNG LISTENING) */}
          <section 
              className={`p-8 md:p-10 overflow-y-auto custom-scrollbar html-content-renderer scroll-smooth ${isReviewMode ? 'bg-[#f4f4f4]' : 'bg-[#f4f4f4]'}`} 
              id="questions-container" 
              ref={rightPaneRef as any} 
              style={{ width: !isListening ? `${100 - leftWidth}%` : '100%', flex: 'none' }}
          >
             <div className={`mx-auto relative ${!isListening ? 'pr-8' : ''} ${fontSize === 'S' ? 'text-[14px]' : fontSize === 'L' ? 'text-[18px]' : 'text-[16px]'}`} style={{ width: !isListening ? '100%' : '768px', maxWidth: '100%' }}>
               
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
                  if (parts.length > 1 && !isListening && pIdx !== currentPartIndex) return null;
                  return (
                    <div key={`qpane-${part?.id || pIdx}`}>
                       
                       {/* NỘI DUNG PART SANG BÊN PHẢI NẾU LÀ LISTENING */}
                       {isListening && (
                           <div className="mb-8 bg-transparent">
                               {part?.title && <h3 className="font-black text-xl text-slate-800 mb-2">{part.title}</h3>}
                               {part?.content && <div className="text-[15px] text-slate-600 leading-relaxed mb-6" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(part.content || '') }} />}
                               {part?.imageUrl && <img src={part.imageUrl} className="max-w-full mb-6 rounded-xl shadow-sm border border-slate-200" alt="Part Image" />}
                           </div>
                       )}

                       {part?.sections?.map((sec: any, sIdx: number) => {
                          
                          let displaySecTitle = sec.title;
                          if (displaySecTitle && /Questions?\s+\d+/i.test(displaySecTitle)) {
                              let firstIdx = null;
                              let lastIdx = null;
                              
                              if (sec.questions?.length > 0) {
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

                             {/* NỘI DUNG VÀ HÌNH ẢNH SECTION (CHO CẢ LISTENING VÀ READING) */}
                             <div className="mb-6">
                                {isListening && displaySecTitle && <h4 className="font-bold text-[16px] text-slate-800 mb-4">{displaySecTitle}</h4>}
                                {sec?.imageUrl && <img src={sec.imageUrl} className="max-w-full mb-4 rounded-xl shadow-sm border border-slate-200" alt="Section Image" />}
                                {sec?.content && !( ["Điền từ", "Điền khuyết", "Kéo thả vào Part", "Kéo thả", "Matching", "Droplist"].includes(sec?.questionType) && /\[\s*\d+\s*\]/.test(String(sec.content || '')) ) && (
                                   <div className="prose prose-sm max-w-none text-slate-700 whitespace-pre-wrap leading-relaxed mb-6 bg-white p-5 rounded-xl border border-slate-200 shadow-sm" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(sec.content || '') }} />
                                )}
                             </div>
                             
                             {/* DẠNG BÀI INLINE: Điền từ, Kéo thả, Matching, Inline Droplist */}
                             {(() => {
                               // Build raw content text for inline types
                               const inlineTypes = ["Điền từ", "Điền khuyết", "Kéo thả vào Part", "Kéo thả", "Matching", "Droplist"];
                               if (!inlineTypes.includes(sec?.questionType)) return null;
                               
                               let rawContentText = '';
                               if (String(sec.content || '').match(/\[\s*\d+\s*\]/)) {
                                 rawContentText = sec.content;
                                 if (Array.isArray(sec.questions)) {
                                   sec.questions.forEach((q: any) => {
                                     if (q.content && q.content !== sec.content && String(q.content).match(/\[\s*\d+\s*\]/) && !/^\[\s*\d+\s*\]$/.test(String(q.content).replace(/<[^>]*>/g, '').trim())) {
                                       rawContentText += '<br><br>' + q.content;
                                     }
                                   });
                                 }
                               } else {
                                 if (Array.isArray(sec.questions)) {
                                   sec.questions.forEach((q: any) => {
                                     let qContent = String(q.content || '').trim();
                                     if (qContent) {
                                       if ((sec.questionType === "Điền từ" || sec.questionType === "Điền khuyết") && !/\[\s*\d+\s*\]/.test(qContent)) {
                                         qContent += ` [${q.id}]`;
                                       }
                                       rawContentText += (rawContentText ? '<br><br>' : '') + qContent;
                                     }
                                   });
                                 }
                               }
                               
                               const hasInlineBrackets = /\[\s*\d+\s*\]/.test(rawContentText);
                               const isInlineDroplist = sec.questionType === "Droplist" && hasInlineBrackets;
                               const isBlockDroplist = sec.questionType === "Droplist" && !hasInlineBrackets;
                               const isInlineDragDrop = ["Kéo thả", "Matching", "Kéo thả vào Part"].includes(sec.questionType) && hasInlineBrackets;
                               const isBlockDragDrop = ["Kéo thả", "Matching", "Kéo thả vào Part"].includes(sec.questionType) && !hasInlineBrackets;
                               
                               // Skip if this will be handled by block Droplist or block DragDrop sections below
                               if (isBlockDroplist || isBlockDragDrop) return null;
                               // Must have inline brackets for Điền từ too
                               if ((sec.questionType === "Điền từ" || sec.questionType === "Điền khuyết" || sec.questionType === "Kéo thả vào Part") && !hasInlineBrackets) return null;
                               
                               return (
                                <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 mb-6">
                                  {sec?.imageUrl && !isListening && (
                                      <img src={sec.imageUrl} className="max-w-full mb-6 rounded-lg border border-slate-200" alt="Fill Image" />
                                  )}
                                  
                                  {(() => {
                                    let mainContent = rawContentText;
                                    let wordBankItems: string[] = [];
                                    
                                    const splitKeywords = ['<br><br>Options:<br>', '<br>Options:<br>', 'Options:<br>', 'Options:'];
                                    for (const keyword of splitKeywords) {
                                      if (mainContent.includes(keyword)) {
                                        const partsArr = mainContent.split(keyword);
                                        mainContent = partsArr[0];
                                        wordBankItems = partsArr[1].split(/(?:<br\s*\/?>\s*)+/).filter((x: string) => x.replace(stripHtmlRegex, '').trim() !== '');
                                        break;
                                      }
                                    }
                                    
                                    return (
                                      <React.Fragment>
                                        <div className={`format-passage html-content-renderer text-[16px] text-slate-800 break-words font-sans ${isReviewMode ? 'leading-[3.0] pb-6' : 'leading-[2.0]'}`}>
                                          {renderHtmlWithHoles(cleanHtmlContent(mainContent), sec)}
                                        </div>
                                        {wordBankItems.length > 0 && (
                                          <div className="mt-8 p-5 bg-slate-50 border border-slate-200 rounded-xl font-sans">
                                            <p className="text-[13px] font-black text-slate-600 uppercase tracking-widest mb-4">Danh sách từ (Word Bank)</p>
                                            <div className="flex flex-wrap gap-3">
                                              {wordBankItems.map((item, idx) => {
                                                const text = item.replace(stripHtmlRegex, '').trim();
                                                return text ? (
                                                  <div key={idx} className="px-4 py-2 bg-white border border-slate-300 rounded-lg font-bold text-slate-800 min-w-[100px] flex items-center shadow-sm html-content-renderer" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(text) }} />
                                                ) : null;
                                              })}
                                            </div>
                                          </div>
                                        )}
                                      </React.Fragment>
                                    );
                                  })()}
                                  
                                  {/* Word bank for inline drag-drop */}
                                  {isInlineDragDrop && !isReviewMode && (
                                    <div className="mt-8 p-5 bg-slate-50 border border-slate-200 rounded-xl font-sans">
                                      <p className="text-[13px] font-black text-slate-600 uppercase tracking-widest mb-4">Danh sách lựa chọn (Kéo từ đây):</p>
                                      <div className="flex flex-wrap gap-3">
                                        {(() => {
                                          let allOptions: string[] = [];
                                          (sec.questions || []).forEach((q: any) => {
                                            if (Array.isArray(q.options)) {
                                              q.options.forEach((o: any) => {
                                                const cleanOpt = String(o).replace(stripHtmlRegex, '').trim();
                                                if (cleanOpt && !allOptions.includes(cleanOpt)) allOptions.push(cleanOpt);
                                              });
                                            }
                                          });
                                          const sectionQIds = (sec?.questions || []).map((q: any) => String(q.id));
                                          const selectedInSec = sectionQIds.map((id: string) => answers[id]?.trim().toUpperCase()).filter(Boolean);
                                          
                                          return allOptions.map((opt: string, oIdx: number) => {
                                            const prefix = `${String.fromCharCode(65 + oIdx)}. `;
                                            const displayOpt = /^[A-Z][\.\):]\s/.test(opt) ? opt : prefix + opt;
                                            const optLetter = String.fromCharCode(65 + oIdx);
                                            const isUsed = selectedInSec.includes(optLetter) || selectedInSec.includes(displayOpt.toUpperCase()) || selectedInSec.includes(opt.trim().toUpperCase());
                                            
                                            return (
                                              <div
                                                key={oIdx}
                                                draggable={!isUsed}
                                                onDragStart={(e) => onDragStart(e, displayOpt)}
                                                onDragEnd={() => setDraggedOption(null)}
                                                onDrag={handleDragScroll}
                                                className={`px-4 py-2 font-bold font-sans text-[14px] border rounded-lg transition-all select-none shadow-sm
                                                  ${isUsed
                                                    ? 'bg-slate-100 text-slate-400 opacity-50 cursor-not-allowed border-slate-200'
                                                    : 'bg-white text-slate-800 cursor-grab hover:bg-[#0ea5e9]/5 hover:border-[#0ea5e9] active:cursor-grabbing border-slate-300'
                                                  }`}
                                              >
                                                {displayOpt}
                                              </div>
                                            );
                                          });
                                        })()}
                                      </div>
                                    </div>
                                  )}
                                  
                                  {/* Review & Gia sư cho inline types */}
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
                                                 <div className="text-[14px] text-slate-700 italic leading-relaxed whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(explanationText) }} />
                                                 
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
                               );
                             })()}

                             {(sec?.questionType === "Trắc nghiệm" || sec?.questionType === "TFNG") && sec?.questions?.map((q: any) => {
                                if (!q?.id) return null;
                                const cleanQText = getCleanQuestionText(q.content);
                                const correctAns = String(q.correctAnswer || '').trim().toUpperCase();
                                const userAns = String(answers[String(q.id)] || '').trim().toUpperCase();
                                const isQuestionCorrect = isAnswerCorrect(userAns, correctAns);
                                const displayIdx = questionIndexMap[String(q.id)] || q.id;
                                
                                const isTFNG = sec?.questionType === "TFNG" || q.options?.some((opt: string) => ['TRUE', 'FALSE', 'NOT GIVEN', 'YES', 'NO'].includes(opt?.trim()?.toUpperCase()));

                                if (isTFNG) {
                                   return (
                                     <div 
                                         key={q.id} 
                                         id={`q-${q.id}`} 
                                         className={`bg-white p-6 rounded-2xl shadow-sm border transition-all mb-6 scroll-mt-20 relative group ${isReviewMode ? (isQuestionCorrect ? 'border-emerald-300 bg-emerald-50/20' : 'border-red-300 bg-red-50/20') : 'border-slate-200 hover:border-[#0ea5e9]/50'}`}
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
                                           {cleanQText && <div className="text-[16px] text-slate-800 font-medium leading-relaxed whitespace-pre-wrap mb-4" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(cleanQText) }} />}
                                           
                                           <div className="flex flex-row flex-wrap gap-4">
                                             {q.options?.map((opt: string, i: number) => {
                                                const safeOpt = String(opt || '');
                                                const val = safeOpt.replace(/<[^>]*>/g, '').trim().toUpperCase();
                                                const isSelected = userAns === val;
                                                const isCorrectOpt = isAnswerCorrect(val, correctAns);

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
                                                      <span className="text-[15px] font-semibold" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(safeOpt) }} />
                                                   </label>
                                                );
                                             })}
                                           </div>
                                           
                                           {isReviewMode && q.explanation && (
                                             <div className="mt-6 pt-4 border-t border-slate-100">
                                                <p className="text-[12px] font-black text-amber-600 uppercase mb-2">💡 Giải thích:</p>
                                                <div className="text-[14px] text-slate-700 italic leading-relaxed mb-3" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(String(q.explanation)) }} />
                                                
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
                                      className={`bg-white p-6 md:p-8 rounded-2xl border shadow-sm relative group scroll-mt-20 transition-colors mb-6 ${isReviewMode ? (isQuestionCorrect ? 'bg-emerald-50/30 border-emerald-200' : 'bg-red-50/30 border-red-200') : 'hover:border-[#0ea5e9]/50 border-slate-200'}`}
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
                                           {cleanQText && <div className="text-[16px] text-slate-800 leading-relaxed font-medium mb-3 whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(cleanQText) }} />}
                                        </div>
                                     </div>
                                     
                                     <div className="flex flex-col gap-2 pl-10">
                                        {q.options?.map((opt: any, i: number) => {
                                           const cleanOpt = getCleanOptionText(opt, i);
                                           const val = String.fromCharCode(65+i);
                                           const isSelected = userAns === val;
                                           const isCorrectOpt = isAnswerCorrect(val, correctAns);

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
                                                     <span dangerouslySetInnerHTML={{ __html: cleanHtmlContent(cleanOpt) }} />
                                                 </span>
                                              </label>
                                           );
                                        })}
                                     </div>

                                     {isReviewMode && q.explanation && (
                                        <div className="mt-8 pt-5 border-t border-slate-200 ml-10">
                                           <p className="text-[12px] font-black text-amber-600 uppercase tracking-widest mb-2">💡 Giải thích đáp án:</p>
                                           <div className="text-[14px] text-slate-700 italic leading-relaxed whitespace-pre-wrap border-l-[3px] border-slate-300 pl-3 mb-3" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(String(q.explanation)) }} />
                                           
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

                             {/* DẠNG BÀI DROPLIST KHỐI (chỉ khi KHÔNG CÓ [num] inline) */}
                             {sec?.questionType === "Droplist" && !/\[\s*\d+\s*\]/.test(String(sec.content || '') + ' ' + String(sec.questions?.[0]?.content || '')) && (
                                <div className="space-y-4 bg-white p-6 md:p-8 border border-slate-200 rounded-2xl shadow-sm mb-6">
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

                             {/* DẠNG BÀI KÉO THẢ / MATCHING BLOCK (khi KHÔNG CÓ [num] inline) */}
                             {(() => {
                               if (!["Kéo thả", "Matching", "Kéo thả vào Part"].includes(sec?.questionType)) return null;
                               const combinedContent = String(sec.content || '') + ' ' + String(sec.questions?.[0]?.content || '');
                               if (/\[\s*\d+\s*\]/.test(combinedContent)) return null; // inline mode handled above
                               
                               let allOpts: string[] = [];
                               (sec?.questions || []).forEach((q: any) => {
                                 (q.options || []).forEach((o: any) => {
                                   const cOpt = String(o).replace(stripHtmlRegex, '').trim();
                                   if (cOpt && !allOpts.includes(cOpt)) allOpts.push(cOpt);
                                 });
                               });
                               
                               return (
                                 <div className="bg-white p-6 md:p-8 rounded-2xl shadow-sm border-2 border-slate-200 mb-6">
                                   {sec?.content && (
                                     <div className="text-slate-600 text-[15px] leading-relaxed mb-6 html-content-renderer" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(sec.content) }} />
                                   )}
                                   {/* Block questions with drop targets */}
                                   <div className="space-y-4">
                                     {(Array.isArray(sec.questions) ? sec.questions : []).map((q: any) => {
                                       if (!q?.id) return null;
                                       const userAns = String(answers[String(q.id)] || '');
                                       const correctAns = String(q.correctAnswer || '').trim().toUpperCase();
                                       const isCorrect = isAnswerCorrect(userAns, correctAns);
                                       const displayIdx = questionIndexMap[String(q.id)] || q.id;
                                       
                                       let displayUserAns = userAns;
                                       if (userAns && /^[A-Z]$/i.test(userAns)) {
                                         const oIdx = userAns.toUpperCase().charCodeAt(0) - 65;
                                         if (allOpts[oIdx]) displayUserAns = allOpts[oIdx].replace(/^[A-Z][\.\):]\s*/i, '');
                                       } else if (userAns) {
                                         displayUserAns = userAns.replace(/^[A-Z][\.\):]\s*/i, '');
                                       }
                                       
                                       return (
                                         <div
                                           key={q.id}
                                           id={`q-${q.id}`}
                                           className={`py-4 px-5 rounded-xl border flex flex-col gap-4 transition-all scroll-mt-20 ${isReviewMode ? (isCorrect ? 'bg-emerald-50 border-emerald-200' : 'bg-red-50 border-red-200') : 'bg-white border-slate-200 hover:border-slate-300'}`}
                                         >
                                           <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 w-full">
                                             <div className="flex items-center gap-4 flex-1 min-w-0">
                                               <span className="font-bold text-white bg-slate-800 px-2 py-0.5 rounded text-[13px] shrink-0">{displayIdx}</span>
                                               <div className="text-[15px] text-slate-800 leading-relaxed font-sans html-content-renderer flex-1 min-w-0 break-words [&>p]:!m-0 [&>p]:!inline" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.content) }} />
                                             </div>
                                             <div className="shrink-0 flex items-center justify-start md:justify-end font-sans">
                                               {isReviewMode ? (
                                                 <div className="flex items-center gap-2 justify-start md:justify-end w-full">
                                                   <div className={`px-4 py-1.5 rounded-lg font-bold text-[14px] border min-w-[140px] text-center ${isCorrect ? 'bg-emerald-100 text-emerald-800 border-emerald-300' : 'bg-red-100 text-red-800 border-red-300'}`}>
                                                     {displayUserAns || '(trống)'}
                                                   </div>
                                                   {!isCorrect && (
                                                     <div className="text-[12px] font-bold text-emerald-700 bg-emerald-100 border border-emerald-300 px-2 py-0.5 rounded whitespace-nowrap">
                                                       ĐA: {correctAns}
                                                     </div>
                                                   )}
                                                 </div>
                                               ) : (
                                                 <span
                                                   onDragOver={(e) => e.preventDefault()}
                                                   onDrop={() => onDrop(String(q.id))}
                                                   className={`inline-flex items-center justify-between align-middle min-w-[140px] max-w-[250px] h-[36px] border rounded-lg transition-all px-2 border-slate-300 bg-white shadow-sm`}
                                                 >
                                                   {userAns ? (
                                                     <div className="flex items-center justify-between w-full text-[#0ea5e9] font-sans text-[14px] font-bold py-1">
                                                       <span className="truncate">{displayUserAns}</span>
                                                       <button onClick={(e) => { e.stopPropagation(); clearDragAnswer(String(q.id)); }} className="ml-2 hover:text-red-500 text-[12px] font-black font-sans">✕</button>
                                                     </div>
                                                   ) : (
                                                     <span className="text-slate-400 text-[13px] italic font-sans w-full text-center">Thả vào đây</span>
                                                   )}
                                                 </span>
                                               )}
                                             </div>
                                           </div>
                                           {isReviewMode && q.explanation && (
                                             <div className="w-full mt-2 border-t border-slate-200 pt-3 font-sans">
                                               <p className="text-[12px] font-black text-amber-600 uppercase mb-2">💡 Giải thích đáp án:</p>
                                               <div className="text-[14px] text-slate-600 italic leading-relaxed html-content-renderer mb-3" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.explanation) }} />
                                               <div className="flex items-center gap-2">
                                                 <button onClick={(e) => { e.stopPropagation(); askAIToExplain(String(q.id), q.content, q.explanation); }} className="px-3 py-1.5 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded text-[12px] transition shadow-sm border border-[#064e3b]">
                                                   💬 Chat với AI
                                                 </button>
                                                 <button onClick={(e) => { e.stopPropagation(); callTutorForQuestion(String(q.id), q.content, q.explanation); }} className="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded text-[12px] transition shadow-sm border border-emerald-600 flex items-center gap-1">
                                                   📞 Gọi Gia sư
                                                 </button>
                                               </div>
                                             </div>
                                           )}
                                         </div>
                                       );
                                     })}
                                   </div>
                                   
                                   {/* Draggable options word bank */}
                                   {!isReviewMode && (
                                     <div className="mt-8 p-5 bg-slate-50 border border-slate-200 rounded-xl font-sans">
                                       <p className="text-[13px] font-black text-slate-600 uppercase tracking-widest mb-4">Danh sách lựa chọn (Kéo từ đây):</p>
                                       <div className="flex flex-wrap gap-3">
                                         {(() => {
                                           const sectionQIds = (sec?.questions || []).map((q: any) => String(q.id));
                                           const selectedInSec = sectionQIds.map((id: string) => answers[id]?.trim().toUpperCase()).filter(Boolean);
                                           
                                           return allOpts.map((opt: string, oIdx: number) => {
                                             const prefix = `${String.fromCharCode(65 + oIdx)}. `;
                                             const displayOpt = /^[A-Z][\.\):]\s/.test(opt) ? opt : prefix + opt;
                                             const optLetter = String.fromCharCode(65 + oIdx);
                                             const isUsed = selectedInSec.includes(optLetter) || selectedInSec.includes(displayOpt.toUpperCase()) || selectedInSec.includes(opt.trim().toUpperCase());
                                             
                                             return (
                                               <div
                                                 key={oIdx}
                                                 draggable={!isUsed}
                                                 onDragStart={(e) => onDragStart(e, displayOpt)}
                                                 onDragEnd={() => setDraggedOption(null)}
                                                 onDrag={handleDragScroll}
                                                 className={`px-4 py-2 font-bold font-sans text-[14px] border rounded-lg transition-all select-none shadow-sm
                                                   ${isUsed
                                                     ? 'bg-slate-100 text-slate-400 opacity-50 cursor-not-allowed border-slate-200'
                                                     : 'bg-white text-slate-800 cursor-grab hover:bg-[#0ea5e9]/5 hover:border-[#0ea5e9] active:cursor-grabbing border-slate-300'
                                                   }`}
                                               >
                                                 {displayOpt}
                                               </div>
                                             );
                                           });
                                         })()}
                                       </div>
                                     </div>
                                   )}
                                 </div>
                               );
                             })()}

                             {/* DẠNG CHECKBOX GROUP */}
                             {sec?.questionType === "Checkbox" && (
                                <div className="space-y-6 mb-6">
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
                                                         dangerouslySetInnerHTML={{ __html: cleanHtmlContent(qText) }} 
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
                                                             <span dangerouslySetInnerHTML={{ __html: cleanHtmlContent(cleanOpt) }} />
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
                                                                <span dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.explanation) }} />
                                                                
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

                             {/* DẠNG ĐOẠN VĂN (PARAGRAPH AI GRADING) */}
                             {sec?.questionType === "Đoạn văn" && (
                                <div className="space-y-6 mb-6">
                                  {sec.questions?.map((q: any) => {
                                      const qNum = String(q.id);
                                      const userAns = String(answers[qNum] || '');
                                      const displayIndex = questionIndexMap[qNum] || qNum;
                                      
                                      return (
                                        <div key={q.id} id={`q-${qNum}`} className="bg-white p-6 md:p-8 rounded-2xl shadow-sm border border-slate-200 hover:border-[#0ea5e9]/40 transition-colors relative group scroll-mt-20 mb-4">
                                            <div className="flex gap-4">
                                                <div className="shrink-0 w-8 h-8 rounded-full bg-slate-800 text-white flex items-center justify-center font-bold text-[14px]">
                                                    {displayIndex}
                                                </div>
                                                <div className="flex-1 min-w-0">
                                                    <div className="text-slate-800 font-medium text-[16px] leading-[1.8] mb-4" dangerouslySetInnerHTML={{ __html: cleanHtmlContent(q.content || '') }} />
                                                    
                                                    {isReviewMode ? (
                                                        <div className="bg-slate-50 border border-slate-200 rounded-xl p-4">
                                                            <div className="text-[12px] font-bold text-slate-500 uppercase tracking-widest mb-2">Câu trả lời của bạn:</div>
                                                            <div className="text-slate-800 text-[15px] whitespace-pre-wrap">{userAns || '(Chưa trả lời)'}</div>
                                                            
                                                            <div className="mt-4 pt-4 border-t border-slate-200 flex flex-wrap gap-2">
                                                                <button 
                                                                    onClick={(e) => { 
                                                                        e.stopPropagation(); 
                                                                        askAIToExplain(String(q.id), q.content, q.explanation); 
                                                                    }} 
                                                                    className="px-4 py-2 bg-[#064e3b] hover:bg-[#047857] text-white font-bold rounded-lg text-[13px] transition shadow-sm border border-[#064e3b]"
                                                                >
                                                                    💬 Nhờ AI Chấm Điểm
                                                                </button>
                                                                <button 
                                                                    onClick={(e) => { 
                                                                        e.stopPropagation(); 
                                                                        callTutorForQuestion(String(q.id), q.content, q.explanation); 
                                                                    }} 
                                                                    className="px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-lg text-[13px] transition shadow-sm border border-emerald-600 flex items-center gap-1"
                                                                >
                                                                    📞 Gọi Gia sư
                                                                </button>
                                                            </div>
                                                        </div>
                                                    ) : (
                                                        <textarea 
                                                            value={userAns}
                                                            onChange={(e) => handleAnswer(qNum, e.target.value)}
                                                            placeholder="Nhập câu trả lời của bạn vào đây..."
                                                            className="w-full min-h-[120px] p-4 bg-slate-50 border border-slate-300 rounded-xl focus:outline-none focus:border-[#0ea5e9] focus:ring-1 focus:ring-[#0ea5e9] text-[15px] text-slate-800 resize-y transition-colors placeholder:text-slate-400"
                                                        />
                                                    )}
                                                </div>
                                            </div>
                                        </div>
                                      );
                                  })}
                                </div>
                             )}

                           </div>
                         );})}
                     </div>
                   );
                 })}
                 <div className="h-[200px]" />
              </div>
          </section>
          {/* RIGHT SIDEBAR FOR MCQ */}
          {isListening && (
            <aside className="w-auto mx-4 my-4 md:w-[280px] lg:w-[320px] shrink-0 flex flex-col bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden z-20 md:mx-0 md:my-0 md:absolute md:right-4 md:top-4 md:bottom-4 md:h-[calc(100%-2rem)] min-h-0">
                <div className="p-5 border-b border-slate-200 flex flex-col items-center shrink-0">
                  {isReviewMode ? (
                    <div className="bg-emerald-50 text-emerald-700 p-6 rounded-2xl border border-emerald-100 w-full text-center shadow-sm mb-4">
                      <p className="text-[12px] font-bold uppercase tracking-widest mb-2">Kết quả của bạn</p>
                      <p className="text-5xl font-black mb-4">
                          {scoreResult.score} <span className="text-2xl text-emerald-400">/ {scoreResult.total}</span>
                      </p>
                      
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
                      <span className="text-red-400">⏳</span> {formatTime(timeLeft)} phút
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
                
                <div className="flex-1 min-h-0 overflow-y-auto p-5 custom-scrollbar bg-white">
                  <p className="text-[12px] text-slate-400 mb-4">Bấm vào ô để đến câu hỏi</p>
                  <div className="grid grid-cols-5 gap-2">
                    {allQuestionIds.map(id => {
                      let isAns = answers[id] && answers[id].trim() !== '';
                      const isMarked = marked[id];
                      let btnStyle = 'w-10 h-10 flex items-center justify-center rounded-xl font-bold text-[13px] transition-all border '; 
                      
                      const section = parts.flatMap((p: any) => p.sections || []).find((s:any) => s.questions?.some((sq:any)=>String(sq.id)===id));
                      const qType = section?.questionType;

                      if (!isReviewMode && qType === 'Checkbox') {
                          const combos = buildCheckboxCombos(section?.questions);
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
                                      const c = buildCheckboxCombos(sec.questions);
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
                                      if(correctAnsSet.has(v)) pts++; 
                                  });
                                  const idxInCombo = comboIds.indexOf(id);
                                  isCorrect = idxInCombo < pts;
                              }
                          } else {
                              const q = section?.questions.find((q:any) => String(q.id) === id);
                              isCorrect = q && answers[id]?.trim().toUpperCase() === String(q.correctAnswer || '').trim().toUpperCase() && String(q.correctAnswer || '').trim() !== '';
                          }
                          btnStyle += isCorrect ? 'bg-emerald-500 text-white shadow-md shadow-emerald-500/30 border-transparent' : 'bg-red-500 text-white shadow-md shadow-red-500/30 border-transparent';
                      } else {
                          if (isAns) {
                              btnStyle += 'bg-[#0ea5e9] text-white shadow-md shadow-[#0ea5e9]/30 border-transparent cursor-pointer';
                          } else {
                              btnStyle += 'bg-slate-50 border-slate-200 text-slate-600 hover:bg-slate-100 hover:border-slate-300 cursor-pointer';
                              if (isMarked) {
                                  btnStyle = 'w-10 h-10 flex items-center justify-center rounded-xl font-bold text-[13px] transition-all border border-amber-400 bg-amber-50 text-amber-600 shadow-sm cursor-pointer hover:bg-amber-100';
                              }
                          }
                      }
                      
                      return (
                          <button key={id} id={'nav-' + id} onClick={() => scrollToQuestion(id)} className={btnStyle}>
                              {questionIndexMap[id]}
                          </button>
                      );
                    })}
                  </div>
                </div>
                <div className="p-5 border-t border-slate-200 bg-slate-50 flex gap-3 shrink-0 mt-auto">
                  {isReviewMode ? (
                     <button onClick={handleExit} className="flex-1 bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 py-4 rounded-xl text-[14px] font-black uppercase tracking-widest transition-colors shadow-sm">
                         Thoát
                     </button>
                  ) : (
                     <button onClick={handleFinish} className="flex-1 bg-[#0ea5e9] hover:bg-[#0284c7] text-white font-black py-4 rounded-xl text-[14px] uppercase tracking-widest transition-colors shadow-lg shadow-[#0ea5e9]/20">
                         Nộp bài
                     </button>
                  )}
                </div>
              </aside>
          )}
         </main>

         {!isListening && (
             <footer className="w-full h-[64px] bg-white border-t border-slate-200 shadow-[0_-4px_20px_rgba(0,0,0,0.03)] flex justify-between items-center px-6 shrink-0 select-none font-sans relative z-30">
               <div className="flex-1 flex justify-start sm:justify-center items-center gap-1.5 overflow-x-auto py-1 custom-scrollbar min-w-0">
                 {allQuestionIds.map(id => {
                    let isAns = answers[id] && answers[id].trim() !== '';
                    const isMarked = marked[id];
                    let btnClass = 'w-8 h-8 flex items-center justify-center font-bold text-[13px] transition-all box-border shrink-0 rounded-none border ';
                    
                    const section = parts.flatMap((p: any) => p.sections || []).find((s:any) => s.questions?.some((sq:any)=>String(sq.id)===id));
                    const qType = section?.questionType;

                    if (!isReviewMode && qType === 'Checkbox') {
                        const combos = buildCheckboxCombos(section?.questions);
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
                                    const c = buildCheckboxCombos(sec.questions);
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
                                    if(correctAnsSet.has(v)) pts++; 
                                });
                                const idxInCombo = comboIds.indexOf(id);
                                isCorrect = idxInCombo < pts;
                            }
                        } else {
                            const q = section?.questions.find((q:any) => String(q.id) === id);
                            isCorrect = q && answers[id]?.trim().toUpperCase() === String(q.correctAnswer || '').trim().toUpperCase() && String(q.correctAnswer || '').trim() !== '';
                        }
                        btnClass += isCorrect ? 'bg-emerald-500 text-white border-emerald-500' : 'bg-red-500 text-white border-red-500';
                    } else { 
                        if (isAns) {
                            btnClass += 'bg-[#0ea5e9] text-white border-[#0ea5e9] hover:bg-[#0284c7] hover:border-[#0284c7] cursor-pointer'; 
                        } else {
                            btnClass += isMarked 
                              ? 'border-amber-400 bg-amber-50 text-amber-600 cursor-pointer hover:bg-amber-100 hover:border-amber-500' 
                              : 'bg-white border-slate-300 text-slate-600 cursor-pointer hover:bg-slate-50 hover:border-slate-400 hover:text-[#0ea5e9]'; 
                        }
                    }
                    
                    return (
                        <button key={id} id={'nav-' + id} onClick={() => scrollToQuestion(id)} className={btnClass}>
                            {questionIndexMap[id]}
                        </button>
                    );
                 })}
               </div>

               <div className="flex items-center gap-4 shrink-0 pl-6 border-l border-slate-200">
                  {isReviewMode ? (
                    <div className="flex items-center gap-2">
                        <button 
                           onClick={() => {
                             const tutorContext = {
                               overall: scoreResult.score + '/' + scoreResult.total,
                               transcript: 'Bài test: ' + basicInfo.title + '. Điểm số của em là: ' + scoreResult.score + '/' + scoreResult.total + '.',
                               feedback: "Học sinh vừa làm xong bài test. Hãy chúc mừng và đưa ra nhận xét chung. Hỏi xem học sinh có muốn bạn chữa câu nào cụ thể không."
                             };
                             sessionStorage.setItem('tony_live_mode', 'TUTOR');
                             sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
                             sessionStorage.setItem('tony_auto_start', 'true');
                             window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
                           }}
                           className="bg-[#0ea5e9] hover:bg-[#0284c7] text-white px-4 sm:px-6 py-2.5 rounded-none text-[13px] sm:text-[14px] font-bold transition uppercase tracking-wide shadow-md shadow-[#0ea5e9]/20 flex items-center gap-2"
                        >
                            📞 Gọi Gia Sư
                        </button>
                        <button onClick={handleExit} className="bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 px-4 sm:px-6 py-2.5 rounded-none text-[13px] sm:text-[14px] font-bold transition uppercase tracking-wide">
                            Thoát
                        </button>
                    </div>
                  ) : (
                    <button onClick={handleFinish} className="bg-[#0ea5e9] hover:bg-[#0284c7] shadow-md shadow-[#0ea5e9]/20 text-white px-6 py-2.5 rounded-none text-[14px] font-bold transition ml-2 uppercase tracking-wide">
                        Nộp bài
                    </button>
                  )}
               </div>
             </footer>
         )} {/* ĐÓNG flex-1 flex overflow-hidden relative flex-col md:flex-row */}
      </div>
    );
  };

  return (
      <React.Fragment>
        {/* Audio: ẩn khi test (play background) */}
        {!isReviewMode && basicInfo?.category === 'test' && isListening && globalAudio && (
            <audio ref={globalAudioRef} src={globalAudio} preload="auto" className="hidden" />
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

      {/* DICTIONARY POPUP */}
      {dictPopup && dictPopup.show && (
        <div id="std-dict-popup" className="fixed bg-white rounded-2xl shadow-[0_20px_50px_rgba(0,0,0,0.15)] ring-1 ring-slate-900/5 w-[90vw] max-w-[340px] flex flex-col overflow-hidden animate-in fade-in zoom-in-95 duration-200"
          style={{ 
            zIndex: 99999, 
            left: Math.max(10, Math.min(dictPopup.x - 170, window.innerWidth - 350)), 
            ...(window.innerHeight - dictPopup.y < 300 ? { bottom: window.innerHeight - dictPopup.rectTop + 15 } : { top: dictPopup.y + 15 }), 
            maxHeight: '400px' 
          }}>
          <div className="bg-slate-50/80 backdrop-blur border-b border-slate-100 py-2.5 px-5 flex items-center justify-between shrink-0">
            <div className="flex items-center">
              <span className="text-base mr-2">📖</span>
              <span className="font-bold text-[11px] text-slate-500 tracking-widest uppercase">Từ điển AI</span>
            </div>
            <button onClick={() => setDictPopup(null)} className="text-slate-400 hover:text-slate-700 text-lg font-bold">✕</button>
          </div>
          <div className="bg-white border-b border-slate-100 p-5 shrink-0 relative">
            <h4 className="text-[20px] font-black text-slate-900 pr-10 leading-tight mb-1">
              {dictPopup.word}
            </h4>
            {dictPopup.data?.phonetics && (
              <span className="text-[14px] text-emerald-600 font-mono bg-emerald-50 px-2 py-0.5 rounded">
                {dictPopup.data.phonetics}
              </span>
            )}
            {dictPopup.data?.audio && (
              <button 
                onClick={() => { if(dictPopup.data.audio) { new Audio(dictPopup.data.audio).play(); } }} 
                className="absolute top-5 right-5 w-10 h-10 rounded-full bg-blue-50 text-[#0ea5e9] flex items-center justify-center hover:bg-[#0ea5e9] hover:text-white transition-colors shadow-sm"
              >
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path d="M13.5 4.06c0-1.336-1.616-2.005-2.56-1.06l-4.5 4.5H4.508c-1.141 0-2.318.664-2.66 1.905A9.76 9.76 0 001.5 12c0 .898.121 1.768.35 2.595.341 1.24 1.518 1.905 2.659 1.905h1.93l4.5 4.5c.945.945 2.561.276 2.561-1.06V4.06zM18.584 5.106a.75.75 0 011.06 0c3.808 3.807 3.808 9.98 0 13.788a.75.75 0 11-1.06-1.06 8.25 8.25 0 000-11.668.75.75 0 010-1.06z" /><path d="M15.932 7.757a.75.75 0 011.061 0 4.5 4.5 0 010 6.364.75.75 0 01-1.06-1.06 3 3 0 000-4.244.75.75 0 010-1.06z" /></svg>
              </button>
            )}
          </div>
          <div className="p-5 bg-slate-50 overflow-y-auto custom-scrollbar flex-1 text-[15px]" style={{ WebkitOverflowScrolling: 'touch' }}>
            {dictPopup.isLoading ? (
              <div className="flex flex-col items-center justify-center py-4 opacity-50">
                <span className="w-6 h-6 border-2 border-[#0ea5e9] border-t-transparent rounded-full animate-spin mb-2"></span>
                <span className="text-[13px] font-medium">Đang dịch...</span>
              </div>
            ) : (
              <div className="text-slate-700 leading-relaxed font-medium">
                {dictPopup.data?.translation}
              </div>
            )}
          </div>
        </div>
      )}

    </React.Fragment>
  );
}