import React, { useState, useMemo, useEffect, useRef } from 'react';
import { supabase } from './supabase';
import {
  fetchGlobalStudentSnapshot,
  parseTutorResponseWithActions,
  executeTutorAction,
  GlobalStudentSnapshot,
  TutorActionItem,
  clearGlobalTutorCache,
  extractStudentFirstName,
} from './globalTutorContext';
import { useLmsLang, getLocalizedCourseTitle } from './utils/lmsI18n';
import {
  ClipboardList,
  BookOpen,
  Target,
  Library,
  BarChart3,
  RefreshCw,
  Sparkles,
  Camera,
  Send,
  X,
  ChevronDown,
  ChevronUp,
  Zap,
  GraduationCap,
  Lightbulb,
  MonitorPlay,
  CalendarClock,
  Check,
  RotateCcw,
} from 'lucide-react';

// Academic Luxury (Option C) subtle identity accent — synced 100% with StudentPortal.tsx
const getCoachCourseAccent = (courseTitle?: string | null) => {
  const t = (courseTitle || '').toLowerCase();
  if (t.includes('ielts') || (t.includes('esl') && !t.includes('igcse'))) {
    return {
      stripe: 'from-rose-600 via-rose-500 to-rose-400',
      dot: 'bg-rose-500',
      pill: 'bg-rose-500/20 border-rose-300/40 text-rose-100',
    };
  }
  if (t.includes('sat')) {
    return {
      stripe: 'from-amber-500 via-amber-400 to-yellow-400',
      dot: 'bg-amber-400',
      pill: 'bg-amber-500/20 border-amber-300/45 text-amber-100',
    };
  }
  if (
    t.includes('igcse') ||
    t.includes('a-level') ||
    t.includes('biology') ||
    t.includes('chemistry') ||
    t.includes('physics') ||
    t.includes('geography') ||
    t.includes('science') ||
    t.includes('0580') ||
    t.includes('0606') ||
    t.includes('math') ||
    t.includes('econ') ||
    t.includes('business')
  ) {
    return {
      stripe: 'from-emerald-600 via-emerald-500 to-teal-400',
      dot: 'bg-emerald-500',
      pill: 'bg-emerald-500/20 border-emerald-300/40 text-emerald-100',
    };
  }
  if (
    t.includes('pronunciation') ||
    t.includes('phát âm') ||
    t.includes('reflex') ||
    t.includes('phản ứng') ||
    t.includes('phản xạ') ||
    t.includes('tình huống') ||
    t.includes('communication') ||
    t.includes('giao tiếp')
  ) {
    return {
      stripe: 'from-sky-500 via-[#0284c7] to-cyan-400',
      dot: 'bg-sky-400',
      pill: 'bg-sky-500/20 border-sky-300/40 text-sky-100',
    };
  }
  return {
    stripe: 'from-indigo-600 via-indigo-500 to-sky-400',
    dot: 'bg-indigo-400',
    pill: 'bg-indigo-500/20 border-indigo-300/40 text-indigo-100',
  };
};

export interface StudyCoachProps {
  courseId: string;
  courseTitle: string;
  studentName?: string;
  lectures?: any[];
  folders?: any[];
  availableCourses?: { id: string; title: string }[];
  onSwitchCourse?: (courseId: string) => void;
  onClose?: () => void;
  onOpenLecture: (courseId: string, lectureId?: string) => void;
  onSelectFolder: (folderId: string, targetCourseId?: string) => void;
  onNavigate?: (view: string) => void;
  onOpenAIChat?: (initialPrompt?: string) => void;
}

const cleanTitle = (raw: string) =>
  (raw || '')
    .replace(/\s*\[color:[^\]]*\]/gi, '')
    .replace(/\s*\[bg:[^\]]*\]/gi, '')
    .trim();

export const isCoachSupportedCourse = (courseId?: string | null, courseTitle?: string | null): boolean => {
  if (!courseId && !courseTitle) return false;
  return String(courseId || '').toLowerCase() !== 'all';
};

const escapeRegExp = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

const formatSimpleMarkdown = (text: string, studentFirstName?: string, fullRawName?: string) => {
  if (!text) return '';
  let formatted = text;

  const cleanFull = (fullRawName || '').trim();
  const cleanFirst = (studentFirstName || '').trim();
  // If AI ever writes the full name (e.g. "Trần Huy Tôn"), shorten it to the first name ("Tôn")
  if (cleanFull && cleanFirst && cleanFull.length > cleanFirst.length && cleanFull.includes(' ')) {
    const fullNameRegex = new RegExp(escapeRegExp(cleanFull), 'gi');
    formatted = formatted.replace(fullNameRegex, cleanFirst);
  }

  formatted = formatted
    .replace(/^### (.*$)/gim, '<h4 class="font-black text-[#0a5482] text-[15px] mt-3 mb-1">$1</h4>')
    .replace(/^## (.*$)/gim, '<h3 class="font-black text-[#0a5482] text-[16px] mt-3.5 mb-1.5">$1</h3>')
    .replace(/^# (.*$)/gim, '<h2 class="font-black text-[#0a5482] text-[17px] mt-4 mb-2">$1</h2>')
    .replace(/^---$/gim, '<hr class="my-2.5 border-slate-200" />')
    .replace(
      /^[*\-] (.*$)/gim,
      '<div class="flex items-start my-1.5"><span class="inline-block w-1.5 h-1.5 rounded-full bg-[#2ab4e8] mt-2 mr-2.5 shrink-0"></span><span class="flex-1">$1</span></div>'
    )
    .replace(/\*\*(.*?)\*\*/g, '<b class="font-extrabold text-[#0a5482]">$1</b>')
    .replace(/(?<!\*)\*(?!\s)([^*]+?)(?<!\s)\*(?!\*)/g, '<i class="italic">$1</i>')
    .replace(
      /`([^`]+)`/g,
      '<span class="text-[#0a5482] font-bold px-1.5 py-0.5 bg-sky-50 border border-sky-200 rounded-md text-xs">$1</span>'
    )
    .replace(/(<\/h[2-4]>|<\/div>|<hr[^>]*>)\n+/gi, '$1')
    .replace(/\n/g, '<br/>');

  if (
    cleanFirst &&
    cleanFirst.length >= 2 &&
    cleanFirst.toLowerCase() !== 'em' &&
    cleanFirst.toLowerCase() !== 'học viên'
  ) {
    const firstRegex = new RegExp(`(?<![\\p{L}])(${escapeRegExp(cleanFirst)})(?![\\p{L}])`, 'gu');
    formatted = formatted
      .split(/(<[^>]+>)/g)
      .map((part) =>
        part.startsWith('<') && part.endsWith('>')
          ? part
          : part.replace(firstRegex, '<b class="font-black text-slate-950">$1</b>')
      )
      .join('');
  }

  return formatted;
};

interface CoachMessage {
  role: 'user' | 'ai';
  text: string;
  imageUrl?: string;
  actions?: TutorActionItem[];
  timestamp?: string;
}

export default function CourseStudyCoach({
  courseId,
  courseTitle,
  studentName = '',
  availableCourses,
  onSwitchCourse,
  onClose,
  onOpenLecture,
  onSelectFolder,
  onNavigate,
}: StudyCoachProps) {
  const [lang] = useLmsLang();
  const isEn = lang === 'en';
  const [isWindowCollapsed, setIsWindowCollapsed] = useState(false);
  const [isStatsCollapsed, setIsStatsCollapsed] = useState(false);
  const [isCourseDropdownOpen, setIsCourseDropdownOpen] = useState(false);
  const [snapshot, setSnapshot] = useState<GlobalStudentSnapshot | null>(null);
  const [isLoadingSnapshot, setIsLoadingSnapshot] = useState(true);
  const [isAiThinking, setIsAiThinking] = useState(false);
  const [messages, setMessages] = useState<CoachMessage[]>([]);
  const [userInput, setUserInput] = useState('');
  const [attachedImage, setAttachedImage] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const chatBottomRef = useRef<HTMLDivElement>(null);

  const processImageFile = (file: File) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      const img = new Image();
      img.onload = () => {
        const canvas = document.createElement('canvas');
        const MAX_DIM = 900;
        let width = img.width;
        let height = img.height;
        if (width > height) {
          if (width > MAX_DIM) {
            height *= MAX_DIM / width;
            width = MAX_DIM;
          }
        } else {
          if (height > MAX_DIM) {
            width *= MAX_DIM / height;
            height = MAX_DIM;
          }
        }
        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext('2d');
        if (ctx) {
          ctx.fillStyle = '#ffffff';
          ctx.fillRect(0, 0, width, height);
          ctx.drawImage(img, 0, 0, width, height);
          setAttachedImage(canvas.toDataURL('image/jpeg', 0.72));
        }
      };
      img.src = e.target?.result as string;
    };
    reader.readAsDataURL(file);
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      processImageFile(e.target.files[0]);
      e.target.value = '';
    }
  };

  const handlePaste = (e: React.ClipboardEvent) => {
    const items = e.clipboardData?.items;
    if (!items) return;
    for (let i = 0; i < items.length; i++) {
      if (items[i].type.indexOf('image') !== -1) {
        const file = items[i].getAsFile();
        if (file) processImageFile(file);
        e.preventDefault();
        break;
      }
    }
  };

  const handleOpenImageOnBlackboard = () => {
    if (!attachedImage) return;
    const imgToSend = attachedImage;
    const qText = userInput.trim() || (isEn ? 'Please solve and explain the exercise in this image step by step.' : 'Thầy giải chi tiết giúp em bài tập trong ảnh này với ạ.');
    setAttachedImage(null);
    setUserInput('');

    sessionStorage.setItem('tony_live_mode', 'TUTOR');
    window.dispatchEvent(new CustomEvent('tony-open-image-board', { detail: imgToSend }));
    (window as any).tonyPendingImage = imgToSend;
    window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
    setTimeout(() => {
      window.dispatchEvent(
        new CustomEvent('tony-force-start', {
          detail: {
            mode: 'vision_mode',
            image: imgToSend,
            query: qText,
            courseTitle: getLocalizedCourseTitle(cleanTitle(courseTitle || (isEn ? 'General' : 'Tổng hợp')), lang),
          },
        })
      );
    }, 600);
  };

  const isIelts = useMemo(() => {
    const t = (courseTitle || '').toLowerCase();
    return courseId === '239a64f0-c106-40e5-a6e2-4e685a0d70fb' || t.includes('ielts');
  }, [courseId, courseTitle]);

  const isSat = useMemo(() => {
    const t = (courseTitle || '').toLowerCase();
    return !isIelts && t.includes('sat');
  }, [isIelts, courseTitle]);

  const isIgcse0654 = useMemo(() => {
    const t = (courseTitle || '').toLowerCase();
    return (
      courseId === 'a2a949c7-c23e-45a7-82fa-cdeda5cc32a7' ||
      t.includes('co-ordinated') ||
      t.includes('0654')
    );
  }, [courseId, courseTitle]);

  const isIgcseSubject = useMemo(() => {
    const t = (courseTitle || '').toLowerCase();
    return (
      !isIelts &&
      !isSat &&
      !isIgcse0654 &&
      (t.includes('igcse') ||
        t.includes('a-level') ||
        t.includes('biology') ||
        t.includes('chemistry') ||
        t.includes('physics') ||
        t.includes('geography') ||
        t.includes('science') ||
        t.includes('0580') ||
        t.includes('0606') ||
        t.includes('math') ||
        t.includes('econ') ||
        t.includes('business'))
    );
  }, [isIelts, isSat, isIgcse0654, courseTitle]);

  const isCommCourse = useMemo(() => {
    const t = (courseTitle || '').toLowerCase();
    return (
      !isIelts &&
      !isSat &&
      !isIgcse0654 &&
      !isIgcseSubject &&
      (t.includes('văn phòng') ||
        t.includes('office') ||
        t.includes('thành ngữ') ||
        t.includes('idiom') ||
        t.includes('email') ||
        t.includes('phỏng vấn') ||
        t.includes('interview') ||
        t.includes('pronunciation') ||
        t.includes('phát âm') ||
        t.includes('reflex') ||
        t.includes('phản ứng') ||
        t.includes('phản xạ') ||
        t.includes('tình huống') ||
        t.includes('communication') ||
        t.includes('giao tiếp'))
    );
  }, [isIelts, isSat, isIgcse0654, isIgcseSubject, courseTitle]);

  const getCacheKey = (uid: string, cid: string, currentLang: string) =>
    `tony_ai_coach_chat_v7_${uid}_${cid}_${currentLang}`;

  const askTonyAIBrain = async (
    snap: GlobalStudentSnapshot,
    userQuestion: string,
    isInitialAutoDiagnosis = false,
    imageBase64?: string | null,
    priorHistory: CoachMessage[] = []
  ) => {
    setIsAiThinking(true);
    try {
      const imageInstruction = imageBase64
        ? isEn
          ? `\n[THE STUDENT ATTACHED AN EXERCISE / QUESTION IMAGE]:
- Examine the attached image carefully and read all questions, figures, or student answers.
- Provide a clear step-by-step solution, highlight key marking-scheme concepts, and correct any mistakes.
- Match the topic against the course catalog above and attach relevant clickable [[ACTION:...]] buttons.\n`
          : `\n[HỌC VIÊN ĐÃ ĐÍNH KÈM 1 HÌNH ẢNH BÀI TẬP / ĐỀ BÀI]:
- Hãy quan sát thật kỹ hình ảnh đính kèm, đọc toàn bộ đề bài/câu hỏi/số liệu hoặc bài làm của học sinh trong ảnh.
- Giải chi tiết từng bước, giải thích rõ bản chất kiến thức, từ khóa ăn điểm (Marking Scheme) hoặc sửa lỗi sai cho học sinh một cách dễ hiểu nhất.
- Sau khi giải xong bài trong ảnh, hãy đối chiếu với Bản đồ khóa học ở trên để gợi ý bài giảng lý thuyết hoặc thư mục đề luyện tập liên quan kèm mã nút bấm [[ACTION:...]].\n`
        : '';

      // Multi-turn conversation memory (last 8 turns, compactly truncated)
      const recentTurns = !isInitialAutoDiagnosis ? priorHistory.slice(-8) : [];
      const historyBlock =
        recentTurns.length > 0
          ? isEn
            ? `\n[CONVERSATION HISTORY IN THIS SESSION (remember context & earlier advice)]:\n${recentTurns
                .map((m) => {
                  const roleLabel = m.role === 'user' ? snap.studentName : 'Teacher Tony AI';
                  const snippet = (m.text || '').replace(/\s+/g, ' ').trim().slice(0, 520);
                  return `- ${roleLabel}: ${snippet}${m.text.length > 520 ? '...' : ''}`;
                })
                .join('\n')}\n`
            : `\n[LỊCH SỬ HỘI THOẠI GẦN ĐÂY TRONG PHIÊN NÀY (hãy nhớ ngữ cảnh câu trước để trả lời liền mạch)]:\n${recentTurns
                .map((m) => {
                  const roleLabel = m.role === 'user' ? snap.studentName : 'Thầy Tony AI';
                  const snippet = (m.text || '').replace(/\s+/g, ' ').trim().slice(0, 520);
                  return `- ${roleLabel}: ${snippet}${m.text.length > 520 ? '...' : ''}`;
                })
                .join('\n')}\n`
          : '';

      const systemPrompt = isEn
        ? `You are "Teacher Tony AI" — the lead mentor and personal academic coach at TonyEnglish.vn.
[STRICT LANGUAGE RULE]: The student is using the ENGLISH interface. You MUST write your ENTIRE greeting, analysis, recommendations, AND ALL [[ACTION:...|Button Label]] labels exclusively in warm, clear, natural ENGLISH (unless the student explicitly requests Vietnamese). Address the student by first name ("${snap.studentName}") or "you".

${snap.promptContext}
${historyBlock}${imageInstruction}
[RESPONSE REQUIREMENTS]:
1. ${
            imageBase64
              ? 'Focus first on solving and explaining the exercise/question in the uploaded image clearly step-by-step.'
              : `Look directly at ${snap.studentName}'s real data above (overdue/today Study Calendar deadlines first, recent test scores in this course, in-progress lectures on the Task Board, next lectures, and Library progress if applicable).`
          }
2. Assign or suggest specific, concrete next steps (citing exact lecture titles, practice folders, or calendar deadlines). Keep continuity with the conversation history above if the student is asking a follow-up question.
3. ALWAYS append 1 to 4 clickable action tags using the exact syntax [[ACTION:OPEN_LECTURE:<ID>|<English Label>]], [[ACTION:OPEN_FOLDER:<ID>|<English Label>]], [[ACTION:OPEN_LIBRARY:<URL>|<English Label>]], [[ACTION:OPEN_AI_ROOM:<speaking|task1|task2>|<English Label>]], or [[ACTION:OPEN_TAB:<calendar|board|analytics>|<English Label>]] at the end of your reply.

Student's current request: "${userQuestion}"`
        : `Bạn là "Thầy Tony AI" — người thầy chủ nhiệm kiêm gia sư trưởng trực tiếp dẫn dắt học viên tại TonyEnglish.vn.
Luôn xưng "Thầy" và gọi học viên bằng tên ("${snap.studentName}") hoặc "em". Giọng văn sống động, ấm áp, sát sao, đi thẳng vào dữ liệu thực tế của học viên (TUYỆT ĐỐI KHÔNG nói chung chung sáo rỗng, KHÔNG xưng con).

${snap.promptContext}
${historyBlock}${imageInstruction}
[YÊU CẦU TRẢ LỜI]:
1. ${
            imageBase64
              ? 'Ưu tiên giải quyết thật chi tiết, cặn kẽ bài tập/câu hỏi trong hình ảnh mà học viên vừa gửi lên.'
              : `Nhìn thẳng vào số liệu thực tế của ${snap.studentName} ở trên (ưu tiên hàng đầu các bài QUÁ HẠN / HẠN HÔM NAY trên Lịch báo bài nếu có, sau đó tới điểm test gần nhất, bài giảng đang làm dở trên Bảng công việc, bài giảng tiếp theo chưa học, và tiến độ Thư viện nếu là IELTS).`
          }
2. Giao hoặc gợi ý các công việc cụ thể tiếp theo cần làm (viết rõ tên bài giảng, tên bộ đề hoặc deadline cần xử lý). Nếu học viên đang hỏi nối tiếp tin nhắn trước, hãy bám sát lịch sử hội thoại ở trên để trả lời liền mạch.
3. BẮT BUỘC chèn từ 1 đến 4 mã nút bấm hành động theo đúng cú pháp [[ACTION:OPEN_LECTURE:<ID>|<Nhãn nút>]], [[ACTION:OPEN_FOLDER:<ID>|<Nhãn nút>]], [[ACTION:OPEN_LIBRARY:<URL>|<Nhãn nút>]], [[ACTION:OPEN_AI_ROOM:<speaking|task1|task2>|<Nhãn nút>]], hoặc [[ACTION:OPEN_TAB:<calendar|board|analytics>|<Nhãn nút>]] ở cuối câu trả lời để học sinh bấm 1 click là mở thẳng bài đó.

Yêu cầu hiện tại từ học viên: "${userQuestion}"`;

      const { data, error } = await supabase.functions.invoke('omni-ai-grader', {
        body: {
          prompt: systemPrompt,
          taskType: 'tutor',
          imageUrl: imageBase64 || undefined,
          imageUrls: imageBase64 ? [imageBase64] : undefined,
        },
      });

      if (error || data?.error) {
        throw new Error(isEn ? 'AI is currently busy. Please try again shortly.' : 'Hệ thống AI đang bận, vui lòng thử lại sau giây lát.');
      }

      const rawReply = data?.result || data?.text || data?.response || '';
      const { cleanedText, actions } = parseTutorResponseWithActions(rawReply);

      const aiMsg: CoachMessage = {
        role: 'ai',
        text: cleanedText,
        actions,
        timestamp: new Date().toLocaleTimeString(isEn ? 'en-US' : 'vi-VN', { hour: '2-digit', minute: '2-digit' }),
      };

      setMessages((prev) => {
        const next = isInitialAutoDiagnosis ? [aiMsg] : [...prev, aiMsg];
        try {
          sessionStorage.setItem(getCacheKey(snap.userId, courseId, lang), JSON.stringify(next));
        } catch {}
        return next;
      });
    } catch (err: any) {
      // Fallback thông minh từ dữ liệu thật theo đúng hệ khóa học nếu mạng/API chập chờn
      const fallbackActions: TutorActionItem[] = [];
      const firstInProg = snap.taskProgress.inProgressLectures[0];
      const firstNextUp = snap.taskProgress.nextUpLectures[0];
      const targetLec = firstInProg || firstNextUp;
      const urgentCount = (snap.deadlines?.overdue?.length || 0) + (snap.deadlines?.dueToday?.length || 0);

      if (urgentCount > 0) {
        fallbackActions.push({
          type: 'OPEN_TAB',
          target: 'calendar',
          label: isEn ? `📅 View ${urgentCount} Urgent Deadlines` : `📅 Xem ${urgentCount} bài đến hạn trên Lịch`,
        });
      }
      if (targetLec) {
        fallbackActions.push({
          type: 'OPEN_LECTURE',
          target: targetLec.id,
          label: isEn ? `📖 Open Lesson: ${targetLec.title}` : `📖 Học bài: ${targetLec.title}`,
        });
      }
      if (snap.isIelts) {
        fallbackActions.push({
          type: 'OPEN_LIBRARY',
          target: '/news/category/cambridge-ielts-reading-translation',
          label: isEn ? '📚 Open Library: Cambridge Reading' : '📚 Mở Thư viện: Bài dịch đọc Cambridge',
        });
      }
      fallbackActions.push({
        type: 'OPEN_TAB',
        target: 'board',
        label: isEn ? '📋 Open Task Board' : '📋 Mở Bảng Công Việc',
      });

      const courseSpecificTailVi = snap.isIelts
        ? ' và kết hợp đọc thêm bài dịch song ngữ trong Thư viện Cambridge nhé!'
        : snap.isSat
        ? ' rồi vào Kho đề Digital SAT luyện Reading & Writing / Math 1500+ nhé!'
        : snap.isIgcse0654 || snap.isIgcseSubject
        ? ' rồi làm bài Past Papers tương ứng trong Kho đề để nắm chắc Marking Scheme nhé!'
        : ' rồi thực hành bài tập ứng dụng tương ứng trong Kho đề nhé!';

      const courseSpecificTailEn = snap.isIelts
        ? ' and read Cambridge bilingual translations in the Library!'
        : snap.isSat
        ? ' and practice Reading & Writing / Math 1500+ in the SAT Test Bank!'
        : snap.isIgcse0654 || snap.isIgcseSubject
        ? ' and practice topical Past Papers to master the Cambridge Marking Scheme!'
        : ' and complete the matching practice set in the Test Bank!';

      const urgentLineVi =
        urgentCount > 0
          ? `\n\n⚠️ Em đang có **${urgentCount} nhiệm vụ quá hạn / hạn hôm nay** trên Lịch báo bài — nhớ xử lý trước tiên nhé.`
          : '';
      const urgentLineEn =
        urgentCount > 0
          ? `\n\n⚠️ You have **${urgentCount} overdue or due-today tasks** on your Study Calendar — let's clear those first.`
          : '';

      const fallbackMsg: CoachMessage = {
        role: 'ai',
        text: isEn
          ? `Hello **${snap.studentName}**! I've checked your learning snapshot: you have completed **${snap.taskProgress.completedTasks}/${snap.taskProgress.totalTasks} tasks (${snap.taskProgress.percent}%)** on your Task Board${
              snap.recentTests[0]
                ? `, and your latest test **${snap.recentTests[0].title}** scored **${snap.recentTests[0].scoreLabel}**`
                : ''
            }.${urgentLineEn}\n\nFor today's study session, let's prioritize finishing **${
              targetLec ? targetLec.title : 'your next lesson in the roadmap'
            }**${courseSpecificTailEn}`
          : `Chào **${snap.studentName}**! Thầy đã kiểm tra hồ sơ học tập của em: hiện tại em đã hoàn thành **${snap.taskProgress.completedTasks}/${snap.taskProgress.totalTasks} đầu việc (${snap.taskProgress.percent}%)** trên Bảng công việc${
              snap.recentTests[0]
                ? ` và bài kiểm tra gần nhất **${snap.recentTests[0].title}** đạt **${snap.recentTests[0].scoreLabel}**`
                : ''
            }.${urgentLineVi}\n\nHôm nay thầy giao cho em ưu tiên hoàn thành bài giảng **${
              targetLec ? targetLec.title : 'tiếp theo trong lộ trình'
            }**${courseSpecificTailVi}`,
        actions: fallbackActions,
      };

      setMessages((prev) => (isInitialAutoDiagnosis ? [fallbackMsg] : [...prev, fallbackMsg]));
    } finally {
      setIsAiThinking(false);
    }
  };

      // Load real-time snapshot & initial proactive AI diagnosis
  useEffect(() => {
    if (!courseId || courseId === 'all') return;
    let isMounted = true;

    const initBrain = async () => {
      setIsLoadingSnapshot(true);
      setMessages([]);
      const snap = await fetchGlobalStudentSnapshot(courseId, courseTitle, false, lang);
      if (!isMounted) return;
      setIsLoadingSnapshot(false);

      if (!snap) return;
      setSnapshot(snap);

      // Check session cache first so we don't waste tokens on every tab switch
      try {
        const savedChat = sessionStorage.getItem(getCacheKey(snap.userId, courseId, lang));
        if (savedChat) {
          const parsed = JSON.parse(savedChat);
          if (Array.isArray(parsed) && parsed.length > 0) {
            setMessages(parsed);
            return;
          }
        }
      } catch {}

      const localizedTitle = getLocalizedCourseTitle(cleanTitle(courseTitle), lang);
      // Auto-trigger Teacher Tony AI's first live diagnosis!
      await askTonyAIBrain(
        snap,
        isEn
          ? snap.isIelts
            ? 'Please analyze my current learning progress (recent test scores, in-progress tasks on my Task Board, Cambridge Library progress, and my companion Grammar and Vocabulary course) and recommend my top priority study tasks for today!'
            : `Please analyze my current learning progress in ${localizedTitle} (recent test scores and in-progress/next lessons on my Task Board) and recommend my top priority study tasks for today!`
          : snap.isIelts
          ? 'Hãy phân tích hồ sơ học tập hiện tại của em (điểm các bài test gần nhất, các bài đang làm dở trên Bảng công việc, tiến độ đọc bài dịch Thư viện và khóa bổ trợ Grammar and Vocabulary) rồi chủ động giao cho em các việc cần làm ngay trong buổi học hôm nay (bao gồm cả việc làm thêm bài tập từ vựng/ngữ pháp trong khóa Grammar and Vocabulary) nhé!'
          : `Hãy phân tích hồ sơ học tập hiện tại của em trong khóa ${cleanTitle(courseTitle)} (điểm các bài kiểm tra gần nhất và các bài giảng đang làm dở / kế tiếp trên Bảng công việc) rồi chủ động giao cho em các việc cần làm ngay trong buổi học hôm nay nhé!`,
        true
      );
    };

    initBrain();
    return () => {
      isMounted = false;
    };
  }, [courseId, courseTitle, lang]);

  const handleRefreshDiagnosis = async () => {
    setIsLoadingSnapshot(true);
    clearGlobalTutorCache();
    const freshSnap = await fetchGlobalStudentSnapshot(courseId, courseTitle, true, lang);
    setIsLoadingSnapshot(false);
    if (!freshSnap) return;
    setSnapshot(freshSnap);

    await askTonyAIBrain(
      freshSnap,
      isEn
        ? freshSnap.isIelts
          ? 'I just updated my latest study progress. Please re-analyze all my test scores, Task Board, Cambridge Library, and Grammar and Vocabulary course to assign my next tasks!'
          : 'I just updated my latest study progress. Please re-analyze all my test scores, Task Board, and Library progress to assign my next study tasks!'
        : freshSnap.isIelts
        ? 'Em vừa cập nhật tiến độ học tập mới nhất. Thầy kiểm tra lại toàn bộ điểm số, Bảng công việc, Thư viện và khóa bổ trợ Grammar and Vocabulary để giao việc tiếp theo cho em nhé!'
        : 'Em vừa cập nhật tiến độ học tập mới nhất. Thầy kiểm tra lại toàn bộ điểm số, Bảng công việc và Thư viện để giao việc tiếp theo cho em nhé!',
      true
    );
  };

  const handleSendUserQuestion = async (customPrompt?: string) => {
    const rawQ = (customPrompt ?? userInput).trim();
    const imgToSend = customPrompt ? null : attachedImage;
    if ((!rawQ && !imgToSend) || isAiThinking || !snapshot) return;

    const q = rawQ || (isEn ? 'Please solve and explain the exercise in this image step by step!' : 'Thầy giải chi tiết giúp em bài tập trong hình ảnh này nhé!');

    if (!customPrompt) {
      setUserInput('');
      setAttachedImage(null);
    }
    const userMsg: CoachMessage = {
      role: 'user',
      text: q,
      imageUrl: imgToSend || undefined,
      timestamp: new Date().toLocaleTimeString(isEn ? 'en-US' : 'vi-VN', { hour: '2-digit', minute: '2-digit' }),
    };
    const priorSnapshot = [...messages, userMsg];
    setMessages(priorSnapshot);
    setTimeout(() => {
      chatBottomRef.current?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 80);

    await askTonyAIBrain(snapshot, q, false, imgToSend, messages);
    setTimeout(() => {
      chatBottomRef.current?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 120);
  };

  const handleResetChatSession = () => {
    if (!snapshot || isAiThinking) return;
    try {
      sessionStorage.removeItem(getCacheKey(snapshot.userId, courseId, lang));
    } catch {}
    handleRefreshDiagnosis();
  };

  if (!courseId || courseId === 'all') return null;

  const localizedCourseName = getLocalizedCourseTitle(cleanTitle(courseTitle), lang);
  const courseAccent = getCoachCourseAccent(courseTitle);

  const quickPrompts = isIelts
    ? isEn
      ? [
          {
            label: "Today's Top Priorities",
            prompt:
              'Based on my urgent deadlines, latest test scores, in-progress lectures on my Task Board, and companion Grammar & Vocabulary course, what should I prioritize studying today?',
          },
          {
            label: 'Grammar & Vocab Boost',
            prompt:
              'Please review my current level and assign suitable exercises from Grammar and Vocabulary (such as 4000 English Words, Vocabulary Organiser, Expand Vocabulary Through Reading, or Grammar drills) with quick-open buttons!',
          },
          {
            label: 'Listening Focus',
            prompt:
              'Today I want to focus on Listening. Please check my Listening scores and Cambridge Listening translation progress, then assign specific tasks with quick-open buttons!',
          },
          {
            label: 'Reading Focus',
            prompt:
              'Today I want to focus on Reading. Please check my Reading scores, Cambridge Reading translation progress, and vocabulary, then assign specific tasks with quick-open buttons!',
          },
          {
            label: 'Writing Plan',
            prompt:
              'Today I want to practice Writing (Task 1 & Task 2). Please check my Writing progress on the Task Board and assign my next lesson plus the AI Writing Grader!',
          },
          {
            label: 'Speaking Plan',
            prompt:
              'Today I want to practice Speaking. Please check which Main Blocks / Plugin Blocks lessons I finished and assign the next lesson plus the IELTS Speaking AI Room!',
          },
        ]
      : [
          {
            label: 'Giao việc ưu tiên hôm nay',
            prompt:
              'Dựa vào bài đến hạn trên Lịch báo bài, điểm test gần nhất, các bài đang làm dở trên Bảng công việc và khóa bổ trợ Grammar & Vocabulary của em, hôm nay em nên ưu tiên làm những việc nào nhất hả thầy?',
          },
          {
            label: 'Bổ trợ Grammar & Vocab',
            prompt:
              'Thầy kiểm tra lực học hiện tại của em và giao thêm các bài tập phù hợp trong khóa Grammar and Vocabulary (như 4000 English Words, Vocabulary Organiser, Expand Vocabulary Through Reading hoặc bài tập Grammar) kèm nút mở bài để em tăng cường từ vựng và ngữ pháp phục vụ IELTS nhé!',
          },
          {
            label: 'Cày Listening hôm nay',
            prompt:
              'Hôm nay em muốn tập trung luyện kỹ năng Listening. Thầy xem điểm Listening và tiến độ đọc Bài dịch nghe Cambridge của em rồi giao bài cụ thể kèm nút mở bài giúp em nhé!',
          },
          {
            label: 'Cày Reading hôm nay',
            prompt:
              'Hôm nay em muốn tập trung luyện kỹ năng Reading. Thầy xem điểm Reading, tiến độ đọc Bài dịch đọc Cambridge và từ vựng của em rồi giao bài cụ thể kèm nút mở bài giúp em nhé!',
          },
          {
            label: 'Luyện Writing hôm nay',
            prompt:
              'Hôm nay em muốn học Writing (Task 1 & Task 2). Thầy xem trên Bảng công việc em đã học tới bài Writing nào rồi và giao bài học tiếp theo kèm phòng chấm AI cho em nhé!',
          },
          {
            label: 'Luyện Speaking hôm nay',
            prompt:
              'Hôm nay em muốn luyện Speaking. Thầy kiểm tra xem trong học phần Luyện thi Nói (Main Blocks / Plugin Blocks) em đã làm xong bài nào rồi và giao bài kế tiếp kèm phòng luyện Speaking AI cho em nhé!',
          },
        ]
    : isSat
    ? isEn
      ? [
          {
            label: "Today's SAT Priorities",
            prompt:
              'Based on my Digital SAT 1500+ progress, deadlines, and recent scores, what should I prioritize studying today to push past 1500+?',
          },
          {
            label: 'Reading & Writing (R&W)',
            prompt:
              'Today I want to focus on Digital SAT Reading & Writing (Craft & Structure, Information & Ideas, Standard English Conventions). Please check my progress and assign the next lesson + practice folder!',
          },
          {
            label: 'Math 1500+ & Desmos',
            prompt:
              'Today I want to sharpen Digital SAT Math (Algebra, Advanced Math, Geometry & Desmos speed tricks). Please assign the right lesson and practice folder!',
          },
          {
            label: 'Hard M2 Boss Drills',
            prompt:
              'Am I ready for Hard Module 2 Boss Drills (750–800 level)? Please check my recent scores and recommend the best strategy + folder!',
          },
          {
            label: 'Real Past Exams Strategy',
            prompt:
              'Please recommend which Real Past Exam (2024–2025) I should attempt next and give me pacing tips for Module 1 & Module 2!',
          },
        ]
      : [
          {
            label: 'Ưu tiên SAT 1500+ hôm nay',
            prompt:
              'Dựa vào tiến độ khóa Digital SAT 1500+, lịch báo bài và điểm kiểm tra gần nhất của em, hôm nay em nên ưu tiên học và luyện phần nào để bứt phá lên 1500+ hả thầy?',
          },
          {
            label: 'Luyện Reading & Writing',
            prompt:
              'Hôm nay em muốn tập trung luyện Reading & Writing (Craft & Structure, Information & Ideas, Standard English Conventions). Thầy kiểm tra tiến độ và giao bài giảng + thư mục đề phù hợp cho em nhé!',
          },
          {
            label: 'Luyện Math 1500+ & Desmos',
            prompt:
              'Hôm nay em muốn cày Math 1500+ (Algebra, Advanced Math, Geometry và mẹo bấm nhanh Desmos). Thầy giao bài giảng và thư mục đề phù hợp giúp em nhé!',
          },
          {
            label: 'Chiến Hard M2 Boss Drills',
            prompt:
              'Lực học hiện tại của em đã đủ vào bộ Hard M2 Boss Drills (120 Câu Trùm Cuối 750–800) chưa hả thầy? Thầy phân tích điểm số và chỉ đường cho em nhé!',
          },
          {
            label: 'Chiến thuật Real Past Exams',
            prompt:
              'Thầy tư vấn cho em lịch làm đề Real Past Exams (2024–2025) và cách phân bổ thời gian Module 1 / Module 2 để không bị mất điểm đáng tiếc nhé!',
          },
        ]
    : isIgcse0654
    ? isEn
      ? [
          {
            label: "Today's Top Priorities",
            prompt:
              'Based on my deadlines, progress across Biology, Chemistry, Physics, and latest test scores, which chapter and practice exercises should I study next today?',
          },
          {
            label: 'Biology (B1–B19)',
            prompt:
              'Today I want to study Biology (B1–B19). Please check which chapter I am on and assign the matching theory lecture + Topic Paper practice!',
          },
          {
            label: 'Chemistry (C1–C12)',
            prompt:
              'Today I want to study Chemistry (C1–C12). Please check which chapter I am on and assign the matching theory lecture + Topic Paper practice!',
          },
          {
            label: 'Physics (P1–P6)',
            prompt:
              'Today I want to study Physics (P1–P6). Please check which chapter I am on and assign the matching theory lecture + Topic Paper practice!',
          },
          {
            label: 'Past Papers (P2, P4, P6)',
            prompt:
              'Please recommend which Past Paper (Paper 2 Multiple Choice, Paper 4 Extended, or Paper 6 Practical) I should practice today based on my current performance!',
          },
        ]
      : [
          {
            label: 'Giao việc ưu tiên hôm nay',
            prompt:
              'Dựa vào lịch báo bài, tiến độ các chương Biology, Chemistry, Physics và điểm test gần nhất của em, hôm nay em nên học chương nào và làm bài tập nào tiếp theo hả thầy?',
          },
          {
            label: 'Học Biology (B1–B19)',
            prompt:
              'Hôm nay em muốn học phân môn Biology (B1–B19). Thầy kiểm tra xem em đã học tới chương B mấy rồi và giao bài giảng + bộ đề Topic Paper tương ứng cho em nhé!',
          },
          {
            label: 'Học Chemistry (C1–C12)',
            prompt:
              'Hôm nay em muốn học phân môn Chemistry (C1–C12). Thầy kiểm tra xem em đã học tới chương C mấy rồi và giao bài giảng + bộ đề Topic Paper tương ứng cho em nhé!',
          },
          {
            label: 'Học Physics (P1–P6)',
            prompt:
              'Hôm nay em muốn học phân môn Physics (P1–P6). Thầy kiểm tra xem em đã học tới chương P mấy rồi và giao bài giảng + bộ đề Topic Paper tương ứng cho em nhé!',
          },
          {
            label: 'Luyện Past Papers (P2, P4, P6)',
            prompt:
              'Thầy tư vấn giúp em hôm nay nên luyện đề Past Paper nào (Paper 2 Multiple Choice, Paper 4 Extended hay Paper 6 Practical) dựa trên lực học hiện tại của em nhé!',
          },
        ]
    : isIgcseSubject
    ? isEn
      ? [
          {
            label: "Today's A* Priorities",
            prompt: `Based on my deadlines, progress, and recent test scores in ${localizedCourseName}, which topic and past paper should I prioritize today to aim for A/A*?`,
          },
          {
            label: 'Continue Theory Chapter',
            prompt: `Please check my Task Board in ${localizedCourseName} for any in-progress or next syllabus chapter and assign it with a quick-open button!`,
          },
          {
            label: 'Marking Scheme & Command Words',
            prompt: `Please explain the most important Cambridge Marking Scheme keywords and command words (State, Describe, Explain, Evaluate/Calculate) for my current topic in ${localizedCourseName}!`,
          },
          {
            label: 'Topical & Past Papers',
            prompt: `Please recommend the best Past Paper / Topical practice folder in ${localizedCourseName} for me to attempt today!`,
          },
        ]
      : [
          {
            label: 'Lộ trình A/A* hôm nay',
            prompt: `Dựa vào lịch báo bài, tiến độ bài giảng và điểm gần nhất của em trong môn ${cleanTitle(courseTitle)}, hôm nay em nên ưu tiên học chương nào và luyện đề nào để hướng tới điểm A/A*?`,
          },
          {
            label: 'Học tiếp chương Lý thuyết',
            prompt: `Thầy kiểm tra Bảng công việc môn ${cleanTitle(courseTitle)} xem em đang học dở hoặc cần học tiếp chương nào theo Syllabus rồi giao bài kèm nút mở nhanh giúp em nhé!`,
          },
          {
            label: 'Từ khóa Marking Scheme ăn điểm',
            prompt: `Thầy nhắc giúp em những từ khóa Marking Scheme và Command Words (State, Describe, Explain, Evaluate/Calculate) dễ mất điểm nhất ở chuyên đề em đang học trong môn ${cleanTitle(courseTitle)} nhé!`,
          },
          {
            label: 'Chọn đề Topical / Past Papers',
            prompt: `Thầy chọn giúp em thư mục đề Topical hoặc Past Papers phù hợp nhất trong Kho đề môn ${cleanTitle(courseTitle)} để em luyện tay hôm nay nhé!`,
          },
        ]
    : isCommCourse
    ? isEn
      ? [
          {
            label: "Today's Practice Plan",
            prompt: `Based on my progress and deadlines in ${localizedCourseName}, which lesson and practical exercise should I focus on today?`,
          },
          {
            label: 'Live Roleplay with Teacher Tony',
            prompt: `Let's do a realistic 1-on-1 roleplay right here in this chat based on my current topic in ${localizedCourseName}! You start with the first prompt/question and correct my English after each reply.`,
          },
          {
            label: 'Natural Expressions & Phrases',
            prompt: `Give me 5 high-impact, natural British/International English expressions related to my current lesson in ${localizedCourseName}, with clear workplace/real-life examples!`,
          },
          {
            label: 'Next Lesson & Drills',
            prompt: `Check my Task Board in ${localizedCourseName} and assign my next theory lecture plus practice folder with quick-open buttons!`,
          },
        ]
      : [
          {
            label: 'Kế hoạch luyện hôm nay',
            prompt: `Dựa vào tiến độ và lịch báo bài trong khóa ${cleanTitle(courseTitle)}, hôm nay em nên học bài giảng nào và thực hành phần nào tiếp theo hả thầy?`,
          },
          {
            label: 'Đóng vai thực chiến cùng Thầy',
            prompt: `Thầy ơi mình tập đóng vai (roleplay) thực tế theo đúng chủ đề em đang học trong khóa ${cleanTitle(courseTitle)} ngay tại đây nhé! Thầy mở lời tình huống / đặt câu hỏi trước rồi sửa cách diễn đạt cho em thật tự nhiên nhé.`,
          },
          {
            label: '5 mẫu câu / cụm từ đắt giá',
            prompt: `Thầy cho em 5 mẫu câu / cụm từ tự nhiên và chuyên nghiệp nhất gắn với bài em đang học trong khóa ${cleanTitle(courseTitle)} kèm ví dụ ứng dụng thực tế nhé!`,
          },
          {
            label: 'Mở bài học & Bài tập tiếp theo',
            prompt: `Thầy kiểm tra Bảng công việc khóa ${cleanTitle(courseTitle)} rồi gửi nút mở nhanh bài giảng kế tiếp và bài thực hành trong Kho đề cho em nhé!`,
          },
        ]
    : isEn
    ? [
        {
          label: "Today's Top Priorities",
          prompt: `Based on my deadlines, learning progress, and latest test scores in ${localizedCourseName}, which lecture and practice exercises should I prioritize today?`,
        },
        {
          label: 'Continue Theory Lecture',
          prompt: `Please check my Task Board in ${localizedCourseName} for any in-progress or next theory lecture and assign it with a quick-open button!`,
        },
        {
          label: 'Pick Practice Tests',
          prompt: `Please recommend the best practice test folder in ${localizedCourseName} for me to work on today!`,
        },
        {
          label: 'Analyze Weak Areas',
          prompt: `Please analyze my recent test scores in ${localizedCourseName}, identify my weakest topics, and tell me which lessons to review!`,
        },
      ]
    : [
        {
          label: 'Giao việc ưu tiên hôm nay',
          prompt: `Dựa vào lịch báo bài, tiến độ học tập và điểm kiểm tra gần nhất của em trong khóa ${cleanTitle(courseTitle)}, hôm nay em nên ưu tiên học bài giảng nào và làm bài tập nào tiếp theo hả thầy?`,
        },
        {
          label: 'Học tiếp bài giảng lý thuyết',
          prompt: `Thầy kiểm tra trên Bảng công việc của khóa ${cleanTitle(courseTitle)} xem em đang làm dở hoặc cần học tiếp bài giảng lý thuyết nào rồi giao việc kèm nút mở bài cho em nhé!`,
        },
        {
          label: 'Chọn đề luyện tập hôm nay',
          prompt: `Thầy tư vấn và chọn giúp em thư mục đề luyện tập phù hợp nhất trong Kho đề của khóa ${cleanTitle(courseTitle)} để em làm bài hôm nay nhé!`,
        },
        {
          label: 'Phân tích điểm yếu & Ôn tập',
          prompt: `Thầy phân tích giúp em kết quả các bài kiểm tra gần đây trong khóa ${cleanTitle(courseTitle)} xem em đang yếu ở chuyên đề nào và cần ôn lại bài giảng nào nhé!`,
        },
      ];

  const displayStudentName = extractStudentFirstName(snapshot?.studentName || studentName, lang);
  const latestTest = snapshot?.recentTests?.[0] || null;
  const activeWorkLecture =
    snapshot?.taskProgress?.inProgressLectures?.[0] ||
    snapshot?.taskProgress?.nextUpLectures?.[0] ||
    null;
  const overdueList = snapshot?.deadlines?.overdue || [];
  const dueTodayList = snapshot?.deadlines?.dueToday || [];
  const upcomingSoonList = snapshot?.deadlines?.upcomingSoon || [];
  const urgentDeadlineCount = overdueList.length + dueTodayList.length;
  const canSwitchCourses = Boolean(availableCourses && availableCourses.length > 1 && onSwitchCourse);

  return (
    <div
      className={`${
        onClose ? '' : 'mb-8'
      } rounded-2xl sm:rounded-3xl border border-slate-200/90 ring-1 ring-[#0a5482]/10 bg-white shadow-lg transition-all`}
    >
      {/* TOP HEADER BAR OF AI STUDY COACH (Academic Luxury Option C + Course Identity Hairline & Interactive Course Switcher) */}
      <div
        className={`relative bg-gradient-to-r from-[#073b5c] via-[#0a5482] to-[#0f172a] px-4 sm:px-5 py-3 sm:py-3.5 text-white flex flex-wrap items-center justify-between gap-2.5 rounded-t-[15px] sm:rounded-t-[23px] ${
          isWindowCollapsed ? 'rounded-b-[15px] sm:rounded-b-[23px]' : ''
        }`}
      >
        {/* Clipped Decorative Layer (Course Identity Hairline + Subtle Ambient Glow) */}
        <div
          className={`absolute inset-0 overflow-hidden rounded-t-[15px] sm:rounded-t-[23px] pointer-events-none ${
            isWindowCollapsed ? 'rounded-b-[15px] sm:rounded-b-[23px]' : ''
          }`}
        >
          <div className={`absolute top-0 inset-x-0 h-[3.5px] bg-gradient-to-r ${courseAccent.stripe}`} />
          <div className="absolute -top-16 -right-12 w-56 h-56 bg-[#2ab4e8]/15 blur-3xl rounded-full" />
        </div>

        <div className="relative z-20 flex items-center gap-2 sm:gap-2.5 min-w-0 flex-wrap">
          <div className="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-amber-400/15 border border-amber-300/35 text-amber-300 flex items-center justify-center shadow-sm shrink-0">
            <Sparkles className="w-5 h-5" />
          </div>
          <span className="bg-emerald-400/15 text-emerald-200 border border-emerald-400/30 text-[10px] sm:text-[11px] font-black uppercase tracking-wider px-2.5 py-1 rounded-full flex items-center gap-1.5 min-w-0">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping shrink-0" />
            <span className="truncate">
              {isEn ? (
                <>Teacher Tony AI Mentor<span className="hidden sm:inline"> • Full Progress Analysis</span></>
              ) : (
                <>Thầy Tony AI Chủ Nhiệm<span className="hidden sm:inline"> • Phân Tích Tiến Độ Tổng Thể</span></>
              )}
            </span>
          </span>

          {/* INTERACTIVE COURSE SWITCHER DROPDOWN */}
          {canSwitchCourses ? (
            <div className="relative">
              <button
                type="button"
                onClick={() => setIsCourseDropdownOpen((prev) => !prev)}
                className={`bg-white/12 hover:bg-white/20 text-white border border-white/25 text-[11px] sm:text-xs font-extrabold px-2.5 sm:px-3 py-1.5 rounded-xl flex items-center gap-1.5 max-w-[215px] sm:max-w-[290px] transition cursor-pointer shadow-2xs`}
                title={isEn ? 'Switch course to get tailored coaching' : 'Bấm để chuyển nhanh sang khóa học khác cần Thầy tư vấn'}
              >
                <span className={`w-2 h-2 rounded-full ${courseAccent.dot} shrink-0 ring-2 ring-white/30`} />
                <GraduationCap className="w-3.5 h-3.5 text-sky-200 shrink-0 hidden sm:block" />
                <span className="truncate">{localizedCourseName}</span>
                <ChevronDown
                  className={`w-3.5 h-3.5 text-sky-200 shrink-0 transition-transform duration-200 ${
                    isCourseDropdownOpen ? 'rotate-180' : ''
                  }`}
                />
              </button>

              {isCourseDropdownOpen && (
                <>
                  <div
                    className="fixed inset-0 z-40"
                    onClick={() => setIsCourseDropdownOpen(false)}
                  />
                  <div className="absolute left-0 top-full mt-2 w-72 sm:w-80 max-h-80 overflow-y-auto bg-white text-slate-800 rounded-2xl shadow-2xl border border-slate-200/95 p-1.5 z-50 animate-in fade-in slide-in-from-top-2 duration-150 custom-scrollbar">
                    <div className="px-3 py-1.5 text-[10.5px] font-black uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-1 flex items-center justify-between">
                      <span>{isEn ? 'Switch Course Advisor' : 'Chuyển khóa học tư vấn'}</span>
                      <span className="text-slate-400 font-bold">{availableCourses!.length}</span>
                    </div>
                    {availableCourses!.map((c) => {
                      const isActive = String(c.id) === String(courseId);
                      const itemAccent = getCoachCourseAccent(c.title);
                      return (
                        <button
                          key={c.id}
                          type="button"
                          onClick={() => {
                            setIsCourseDropdownOpen(false);
                            if (!isActive && onSwitchCourse) {
                              onSwitchCourse(String(c.id));
                            }
                          }}
                          className={`w-full text-left px-3 py-2 rounded-xl text-xs font-bold flex items-center justify-between gap-2 transition cursor-pointer ${
                            isActive
                              ? 'bg-sky-50 text-[#0a5482] font-extrabold'
                              : 'text-slate-700 hover:bg-slate-50 hover:text-[#0a5482]'
                          }`}
                        >
                          <div className="flex items-center gap-2 min-w-0">
                            <span className={`w-2 h-2 rounded-full ${itemAccent.dot} shrink-0`} />
                            <span className="truncate">{getLocalizedCourseTitle(cleanTitle(c.title), lang)}</span>
                          </div>
                          {isActive && <Check className="w-3.5 h-3.5 text-[#0a5482] shrink-0" />}
                        </button>
                      );
                    })}
                  </div>
                </>
              )}
            </div>
          ) : (
            <span className="bg-white/10 text-sky-100 border border-white/15 text-[11px] sm:text-xs font-bold px-2.5 py-1 rounded-xl flex items-center gap-1.5 max-w-[200px] sm:max-w-[260px] truncate">
              <span className={`w-2 h-2 rounded-full ${courseAccent.dot} shrink-0`} />
              <GraduationCap className="w-3.5 h-3.5 text-sky-300 shrink-0" />
              <span className="truncate">{localizedCourseName}</span>
            </span>
          )}
        </div>

        <div className="relative z-10 flex items-center gap-2 shrink-0 flex-wrap">
          {!isWindowCollapsed && (
            <button
              type="button"
              onClick={() => setIsStatsCollapsed(!isStatsCollapsed)}
              className="bg-white/10 hover:bg-white/20 text-white border border-white/20 text-xs font-extrabold px-3 py-1.5 rounded-xl transition cursor-pointer flex items-center gap-1.5"
              title={
                isStatsCollapsed
                  ? (isEn ? 'Show summary cards above' : 'Mở lại bảng tóm tắt tiến độ phía trên')
                  : (isEn ? 'Hide summary cards for a taller chat view' : 'Ẩn bảng tóm tắt tiến độ phía trên để cửa sổ chat cao hơn')
              }
            >
              <span>{isStatsCollapsed ? (isEn ? 'Show Summary' : 'Hiện tóm tắt') : (isEn ? 'Hide Summary' : 'Ẩn tóm tắt')}</span>
              {isStatsCollapsed ? <ChevronDown className="w-3.5 h-3.5" /> : <ChevronUp className="w-3.5 h-3.5" />}
            </button>
          )}

          {!onClose ? (
            <button
              type="button"
              onClick={() => setIsWindowCollapsed(!isWindowCollapsed)}
              className="bg-amber-400/15 hover:bg-amber-400/25 text-amber-200 border border-amber-300/35 text-xs font-extrabold px-3 py-1.5 rounded-xl transition cursor-pointer flex items-center gap-1.5"
              title={isWindowCollapsed ? (isEn ? 'Expand Teacher Tony AI window' : 'Mở lại cửa sổ tư vấn Thầy Tony AI') : (isEn ? 'Collapse Teacher Tony AI window' : 'Thu gọn toàn bộ cửa sổ Thầy Tony AI')}
            >
              <span>{isWindowCollapsed ? (isEn ? 'Open Chat' : 'Mở cửa sổ chat') : (isEn ? 'Collapse' : 'Thu gọn cửa sổ')}</span>
              {isWindowCollapsed ? <ChevronDown className="w-3.5 h-3.5" /> : <ChevronUp className="w-3.5 h-3.5" />}
            </button>
          ) : (
            <button
              type="button"
              onClick={onClose}
              className="px-3 py-1.5 rounded-xl bg-white/12 hover:bg-rose-600 text-white border border-white/20 hover:border-rose-500 font-bold text-xs flex items-center gap-1.5 transition cursor-pointer"
              title={isEn ? 'Close Teacher Tony AI' : 'Đóng cửa sổ Thầy Tony AI'}
            >
              <X className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">{isEn ? 'Close' : 'Đóng'}</span>
            </button>
          )}
        </div>
      </div>

      {!isWindowCollapsed && (
        <div className="p-3 sm:p-4 space-y-3.5 bg-gradient-to-b from-slate-50/80 to-white rounded-b-[15px] sm:rounded-b-[23px]">
          {/* URGENT STUDY CALENDAR DEADLINES ALERT STRIP */}
          {!isStatsCollapsed && snapshot && urgentDeadlineCount > 0 && (
            <div
              onClick={() =>
                executeTutorAction(
                  { type: 'OPEN_TAB', target: 'calendar', label: isEn ? 'Study Calendar' : 'Lịch báo bài' },
                  courseId,
                  { onOpenLecture, onSelectFolder, onNavigate }
                )
              }
              className="bg-rose-50/80 hover:bg-rose-50 border border-rose-200/90 border-l-4 border-l-rose-500 rounded-xl sm:rounded-2xl px-3.5 py-2.5 flex flex-wrap items-center justify-between gap-2.5 cursor-pointer transition shadow-2xs"
            >
              <div className="flex items-center gap-2.5 min-w-0">
                <div className="w-8 h-8 rounded-xl bg-rose-100 text-rose-600 flex items-center justify-center shrink-0">
                  <CalendarClock className="w-4 h-4" />
                </div>
                <div className="min-w-0">
                  <div className="text-xs font-extrabold text-rose-900 flex items-center gap-2 flex-wrap">
                    <span>
                      {isEn
                        ? `${overdueList.length > 0 ? `${overdueList.length} overdue` : ''}${overdueList.length > 0 && dueTodayList.length > 0 ? ' • ' : ''}${dueTodayList.length > 0 ? `${dueTodayList.length} due today` : ''} on Study Calendar`
                        : `${overdueList.length > 0 ? `${overdueList.length} bài quá hạn` : ''}${overdueList.length > 0 && dueTodayList.length > 0 ? ' • ' : ''}${dueTodayList.length > 0 ? `${dueTodayList.length} bài hạn hôm nay` : ''} trên Lịch báo bài`}
                    </span>
                    {upcomingSoonList.length > 0 && (
                      <span className="text-[10.5px] font-bold bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full">
                        +{upcomingSoonList.length} {isEn ? 'upcoming' : 'sắp đến hạn'}
                      </span>
                    )}
                  </div>
                  <div className="text-[11.5px] text-rose-700/90 font-semibold truncate">
                    {(overdueList[0] || dueTodayList[0])?.title}
                  </div>
                </div>
              </div>
              <span className="text-[11px] font-extrabold text-rose-700 bg-white border border-rose-200 px-2.5 py-1 rounded-lg shrink-0">
                {isEn ? 'Open Calendar →' : 'Mở Lịch báo bài →'}
              </span>
            </div>
          )}

          {/* 1. REAL-TIME STUDENT X-RAY RADAR (4 THẺ DỮ LIỆU TỔNG THỂ THỰC TẾ — BORDER ACCENT OPTION C) */}
          {!isStatsCollapsed && snapshot && (
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-2 sm:gap-3 animate-in fade-in duration-150">
              {/* Card 1: Bảng công việc */}
              <div
                onClick={() =>
                  executeTutorAction(
                    { type: 'OPEN_TAB', target: 'board', label: isEn ? 'Task Board' : 'Bảng công việc' },
                    courseId,
                    { onOpenLecture, onSelectFolder, onNavigate }
                  )
                }
                className="bg-white hover:bg-sky-50/50 border border-slate-200/90 border-l-[3.5px] border-l-[#0a5482] hover:border-[#0a5482]/50 rounded-xl sm:rounded-2xl p-2.5 sm:p-3.5 shadow-2xs transition cursor-pointer flex flex-col justify-between"
              >
                <div className="flex items-center justify-between gap-2">
                  <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-500 flex items-center gap-1.5">
                    <ClipboardList className="w-3.5 h-3.5 text-[#0a5482] shrink-0" />
                    <span>{isEn ? 'Task Board' : 'Bảng công việc'}</span>
                  </span>
                  <span className="text-xs font-black text-[#0a5482] bg-sky-50 px-2 py-0.5 rounded-full border border-sky-200">
                    {snapshot.taskProgress.percent}%
                  </span>
                </div>
                <div className="mt-2">
                  <div className="text-base font-black text-slate-900">
                    {snapshot.taskProgress.completedTasks} / {snapshot.taskProgress.totalTasks} {isEn ? 'tasks' : 'việc'}
                  </div>
                  <div className="text-[11.5px] text-slate-500 font-semibold truncate mt-0.5">
                    {isEn
                      ? `Finished ${snapshot.taskProgress.completedLecturesCount}/${snapshot.taskProgress.totalLecturesCount} lectures`
                      : `Xong trọn vẹn ${snapshot.taskProgress.completedLecturesCount}/${snapshot.taskProgress.totalLecturesCount} bài giảng`}
                  </div>
                </div>
              </div>

              {/* Card 2: Bài đang học dở / kế tiếp */}
              <div
                onClick={() => {
                  if (activeWorkLecture) {
                    executeTutorAction(
                      {
                        type: 'OPEN_LECTURE',
                        target: activeWorkLecture.id,
                        label: activeWorkLecture.title,
                      },
                      courseId,
                      { onOpenLecture, onSelectFolder, onNavigate }
                    );
                  }
                }}
                className="bg-white hover:bg-emerald-50/50 border border-slate-200/90 border-l-[3.5px] border-l-emerald-500 hover:border-emerald-400 rounded-xl sm:rounded-2xl p-2.5 sm:p-3.5 shadow-2xs transition cursor-pointer flex flex-col justify-between"
              >
                <div className="flex items-center justify-between gap-2">
                  <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-500 flex items-center gap-1.5">
                    <BookOpen className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                    <span>{isEn ? 'Next Lesson' : 'Bài cần học ngay'}</span>
                  </span>
                  <span className="text-[10.5px] font-black text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">
                    {snapshot.taskProgress.inProgressLectures.length > 0
                      ? (isEn ? 'In Progress' : 'Đang làm dở')
                      : (isEn ? 'Up Next' : 'Bài kế tiếp')}
                  </span>
                </div>
                <div className="mt-2">
                  <div className="text-sm font-black text-slate-900 truncate" title={activeWorkLecture?.title}>
                    {activeWorkLecture ? activeWorkLecture.title : (isEn ? 'All lessons completed' : 'Đã hoàn thành hết bài')}
                  </div>
                  <div className="text-[11.5px] text-emerald-700 font-bold truncate mt-0.5">
                    {activeWorkLecture ? (isEn ? 'Click to open lesson →' : 'Bấm để mở ngay bài này →') : (isEn ? 'Awesome work!' : 'Tuyệt vời!')}
                  </div>
                </div>
              </div>

              {/* Card 3: Điểm Test gần nhất */}
              <div
                onClick={() =>
                  executeTutorAction(
                    { type: 'OPEN_TAB', target: 'analytics', label: isEn ? 'Progress Analytics' : 'Tiến độ học' },
                    courseId,
                    { onOpenLecture, onSelectFolder, onNavigate }
                  )
                }
                className="bg-white hover:bg-amber-50/50 border border-slate-200/90 border-l-[3.5px] border-l-amber-500 hover:border-amber-400 rounded-xl sm:rounded-2xl p-2.5 sm:p-3.5 shadow-2xs transition cursor-pointer flex flex-col justify-between"
              >
                <div className="flex items-center justify-between gap-2">
                  <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-500 flex items-center gap-1.5">
                    <Target className="w-3.5 h-3.5 text-amber-600 shrink-0" />
                    <span>{isEn ? 'Latest Test' : 'Điểm Test gần nhất'}</span>
                  </span>
                  {latestTest && (
                    <span
                      className={`text-[10.5px] font-black px-2 py-0.5 rounded-full border ${
                        latestTest.isLow
                          ? 'bg-rose-50 text-rose-700 border-rose-200'
                          : 'bg-emerald-50 text-emerald-700 border-emerald-200'
                      }`}
                    >
                      {latestTest.scoreLabel}
                    </span>
                  )}
                </div>
                <div className="mt-2">
                  <div className="text-sm font-black text-slate-900 truncate" title={latestTest?.title}>
                    {latestTest ? latestTest.title : (isEn ? 'No test attempts yet' : 'Chưa có bài kiểm tra')}
                  </div>
                  <div className="text-[11.5px] text-slate-500 font-semibold truncate mt-0.5">
                    {latestTest
                      ? (isEn ? `${latestTest.dateLabel} • ${latestTest.skill}` : `Ngày ${latestTest.dateLabel} • Kỹ năng ${latestTest.skill}`)
                      : (isEn ? 'Take a test for AI diagnostics' : 'Hãy làm 1 đề để AI chẩn đoán lực học')}
                  </div>
                </div>
              </div>

              {/* Card 4: Thư viện Bài dịch Cambridge (IELTS) hoặc Kỹ năng tổng hợp */}
              {isIelts ? (
                <div
                  onClick={() =>
                    executeTutorAction(
                      {
                        type: 'OPEN_LIBRARY',
                        target: '/news/category/cambridge-ielts-reading-translation',
                        label: isEn ? 'Cambridge Library' : 'Thư viện Bài dịch',
                      },
                      courseId,
                      { onOpenLecture, onSelectFolder, onNavigate }
                    )
                  }
                  className="bg-white hover:bg-indigo-50/50 border border-slate-200/90 border-l-[3.5px] border-l-indigo-500 hover:border-indigo-400 rounded-xl sm:rounded-2xl p-2.5 sm:p-3.5 shadow-2xs transition cursor-pointer flex flex-col justify-between"
                >
                  <div className="flex items-center justify-between gap-2">
                    <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-500 flex items-center gap-1.5">
                      <Library className="w-3.5 h-3.5 text-indigo-600 shrink-0" />
                      <span>{isEn ? 'Cambridge Library' : 'Thư viện Dịch Cam'}</span>
                    </span>
                    <span className="text-[10.5px] font-black text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded-full border border-indigo-200">
                      {isEn ? 'Required' : 'Bắt buộc'}
                    </span>
                  </div>
                  <div className="mt-2">
                    <div className="text-sm font-black text-slate-900">
                      {isEn ? 'Reading' : 'Đọc'}: {snapshot.libraryProgress.camReadingCount}/252 • {isEn ? 'Listening' : 'Nghe'}:{' '}
                      {snapshot.libraryProgress.camListeningCount}/336
                    </div>
                    <div className="text-[11.5px] text-indigo-700 font-bold truncate mt-0.5">
                      {isEn ? 'Open Cambridge Translations →' : 'Mở Thư viện Bài dịch Cambridge →'}
                    </div>
                  </div>
                </div>
              ) : (
                <div
                  onClick={() =>
                    executeTutorAction(
                      { type: 'OPEN_TAB', target: 'analytics', label: isEn ? 'Progress Analytics' : 'Tiến độ học' },
                      courseId,
                      { onOpenLecture, onSelectFolder, onNavigate }
                    )
                  }
                  className="bg-white hover:bg-indigo-50/50 border border-slate-200/90 border-l-[3.5px] border-l-indigo-500 hover:border-indigo-400 rounded-xl sm:rounded-2xl p-2.5 sm:p-3.5 shadow-2xs transition cursor-pointer flex flex-col justify-between"
                >
                  <div className="flex items-center justify-between gap-2">
                    <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-500 flex items-center gap-1.5">
                      <BarChart3 className="w-3.5 h-3.5 text-indigo-600 shrink-0" />
                      <span>{isEn ? 'Total Tests' : 'Tổng số bài thi'}</span>
                    </span>
                    <span className="text-[10.5px] font-black text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded-full border border-indigo-200 truncate max-w-[115px]">
                      {isSat ? 'SAT 1500+' : isIgcse0654 ? 'IGCSE 0654' : isIgcseSubject ? 'IGCSE A*' : (isEn ? 'Test Bank' : 'Kho đề & Thi')}
                    </span>
                  </div>
                  <div className="mt-2">
                    <div className="text-sm font-black text-slate-900">
                      {isEn ? `${snapshot.recentTests.length} recent tests completed` : `Đã làm ${snapshot.recentTests.length} bài gần đây`}
                    </div>
                    <div className="text-[11.5px] text-indigo-700 font-bold truncate mt-0.5">
                      {isEn ? 'View Performance Report →' : 'Xem chi tiết Báo cáo hiệu suất →'}
                    </div>
                  </div>
                </div>
              )}
            </div>
          )}

          {/* 2. DYNAMIC AI CONVERSATION & ACTIONABLE ADVICE STREAM */}
          <div className="bg-white rounded-2xl border border-slate-200/90 shadow-xs overflow-hidden">
            <div className="bg-slate-50 border-b border-slate-200/80 px-4 py-2.5 flex items-center justify-between gap-2 flex-wrap">
              <div className="flex items-center gap-2 flex-wrap">
                <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                <span className="text-xs font-extrabold uppercase tracking-wider text-[#0a5482] flex items-center gap-1.5 flex-wrap">
                  <span>{isEn ? 'Direct Coaching & Study Plan from Teacher Tony AI for' : 'Nhận xét & Chỉ định công việc trực tiếp từ Thầy Tony AI cho'}</span>
                  <span className="font-black text-slate-950">{displayStudentName}</span>
                </span>
              </div>
              <div className="flex items-center gap-2 flex-wrap">
                {messages.length > 1 && (
                  <button
                    type="button"
                    onClick={handleResetChatSession}
                    disabled={isAiThinking || isLoadingSnapshot}
                    className="text-[11px] font-bold text-slate-600 hover:text-rose-700 hover:bg-rose-50 bg-white border border-slate-200 hover:border-rose-200 px-2.5 py-1 rounded-lg transition cursor-pointer flex items-center gap-1 disabled:opacity-50"
                    title={isEn ? 'Clear chat history and start fresh' : 'Làm mới cuộc trò chuyện cho khóa này'}
                  >
                    <RotateCcw className="w-3 h-3" />
                    <span>{isEn ? 'New Chat' : 'Đoạn chat mới'}</span>
                  </button>
                )}
                <button
                  type="button"
                  onClick={handleRefreshDiagnosis}
                  disabled={isAiThinking || isLoadingSnapshot}
                  className="text-[11px] font-extrabold text-[#0a5482] hover:bg-sky-100 bg-sky-50 border border-sky-200 px-2.5 py-1 rounded-lg transition cursor-pointer flex items-center gap-1.5 disabled:opacity-50"
                  title={isEn ? 'Rescan latest scores & progress for updated AI advice' : 'Quét lại điểm số & tiến độ mới nhất để Thầy AI tư vấn lại'}
                >
                  <RefreshCw className={`w-3.5 h-3.5 ${isAiThinking || isLoadingSnapshot ? 'animate-spin' : ''}`} />
                  <span>{isEn ? 'Re-analyze Progress' : 'Phân tích lại tiến độ'}</span>
                </button>
              </div>
            </div>

            <div
              className={`p-4 sm:p-5 space-y-4 ${
                isStatsCollapsed ? 'max-h-[54vh]' : 'max-h-[42vh]'
              } overflow-y-auto custom-scrollbar transition-all`}
            >
              {isLoadingSnapshot && messages.length === 0 && (
                <div className="flex items-center gap-3 py-6 justify-center text-slate-600 font-semibold text-sm">
                  <div className="w-5 h-5 border-2 border-[#0a5482]/30 border-t-[#0a5482] rounded-full animate-spin" />
                  <span>
                    {isEn ? (
                      <>
                        Teacher Tony AI is reading test scores, tasks &amp; library activity for{' '}
                        <span className="font-black text-slate-950">{displayStudentName}</span>...
                      </>
                    ) : (
                      <>
                        Thầy Tony AI đang đọc bảng điểm, các bài đang làm dở và nhật ký Thư viện của{' '}
                        <span className="font-black text-slate-950">{displayStudentName}</span>...
                      </>
                    )}
                  </span>
                </div>
              )}

              {messages.map((msg, idx) => (
                <div
                  key={idx}
                  className={`flex w-full ${
                    msg.role === 'user' ? 'justify-end' : 'justify-start'
                  } animate-in fade-in duration-200`}
                >
                  {msg.role === 'ai' && (
                    <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-[#0a5482] to-[#073b5c] text-amber-300 flex items-center justify-center shrink-0 mr-3 mt-0.5 shadow-xs">
                      <Sparkles className="w-4 h-4" />
                    </div>
                  )}

                  <div
                    className={`max-w-[92%] sm:max-w-[88%] rounded-2xl p-4 text-[13.5px] sm:text-[14.5px] leading-relaxed ${
                      msg.role === 'user'
                        ? 'bg-[#0a5482] text-white rounded-tr-sm font-semibold shadow-xs'
                        : 'bg-slate-50/90 border border-slate-200/90 text-slate-800 rounded-tl-sm shadow-2xs'
                    }`}
                  >
                    {msg.role === 'user' ? (
                      <div className="space-y-2">
                        {msg.imageUrl && (
                          <img
                            src={msg.imageUrl}
                            alt="Ảnh bài tập đính kèm"
                            className="max-h-48 w-auto rounded-xl border border-white/25 object-contain bg-white"
                          />
                        )}
                        <div>{msg.text}</div>
                      </div>
                    ) : (
                      <div>
                        <div
                          className="prose prose-sm max-w-none text-slate-700 leading-relaxed"
                          dangerouslySetInnerHTML={{
                            __html: formatSimpleMarkdown(msg.text, displayStudentName, studentName),
                          }}
                        />

                        {msg.actions && msg.actions.length > 0 && (
                          <div className="mt-4 pt-3.5 border-t border-slate-200/80">
                            <div className="text-[11px] font-black uppercase tracking-wider text-[#0a5482] mb-2 flex items-center gap-1.5">
                              <Zap className="w-3.5 h-3.5 text-amber-500 shrink-0" />
                              <span>{isEn ? 'Click below to jump straight into your assigned tasks:' : 'Bấm vào đây để thực hiện ngay các việc Thầy vừa giao:'}</span>
                            </div>
                            <div className="flex flex-wrap gap-2">
                              {msg.actions.map((act, aIdx) => {
                                const btnColor =
                                  act.type === 'OPEN_LECTURE'
                                    ? 'bg-[#0a5482] hover:bg-[#084266] text-white'
                                    : act.type === 'OPEN_FOLDER'
                                    ? 'bg-emerald-600 hover:bg-emerald-700 text-white'
                                    : act.type === 'OPEN_LIBRARY'
                                    ? 'bg-amber-500 hover:bg-amber-600 text-slate-950'
                                    : act.type === 'OPEN_AI_ROOM'
                                    ? 'bg-indigo-600 hover:bg-indigo-700 text-white'
                                    : act.type === 'OPEN_TAB' && act.target === 'calendar'
                                    ? 'bg-rose-600 hover:bg-rose-700 text-white'
                                    : 'bg-sky-100 hover:bg-sky-200 text-[#0a5482] border border-sky-300';

                                return (
                                  <button
                                    key={aIdx}
                                    type="button"
                                    onClick={() =>
                                      executeTutorAction(act, courseId, {
                                        onOpenLecture,
                                        onSelectFolder,
                                        onNavigate,
                                      })
                                    }
                                    className={`inline-flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs sm:text-[13px] font-extrabold shadow-xs hover:shadow-md active:scale-95 transition-all cursor-pointer ${btnColor}`}
                                  >
                                    <span>{act.label}</span>
                                    <span>→</span>
                                  </button>
                                );
                              })}
                            </div>
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                </div>
              ))}

              {isAiThinking && (
                <div className="flex items-center gap-3 text-slate-600 text-xs sm:text-sm font-semibold py-2">
                  <div className="w-8 h-8 rounded-xl bg-gradient-to-br from-[#0a5482] to-[#073b5c] text-amber-300 flex items-center justify-center shrink-0">
                    <Sparkles className="w-4 h-4" />
                  </div>
                  <div className="bg-slate-100 border border-slate-200 px-4 py-2.5 rounded-2xl flex items-center gap-2">
                    <span className="w-2 h-2 bg-[#0284c7] rounded-full animate-bounce" />
                    <span className="w-2 h-2 bg-[#0a5482] rounded-full animate-bounce [animation-delay:150ms]" />
                    <span className="w-2 h-2 bg-[#0284c7] rounded-full animate-bounce [animation-delay:300ms]" />
                    <span className="ml-1 text-slate-600">
                      {isEn ? (
                        <>
                          Teacher Tony AI is thinking and picking the best study tasks for{' '}
                          <span className="font-black text-slate-950">{displayStudentName}</span>...
                        </>
                      ) : (
                        <>
                          Thầy Tony AI đang suy nghĩ và chọn bài phù hợp nhất cho{' '}
                          <span className="font-black text-slate-950">{displayStudentName}</span>...
                        </>
                      )}
                    </span>
                  </div>
                </div>
              )}

              <div ref={chatBottomRef} />
            </div>

            {/* 3. QUICK FOCUS PROMPTS & DIRECT CHAT INPUT */}
            <div className="p-3.5 sm:p-4 bg-slate-50 border-t border-slate-200/80 space-y-3">
              <div className="flex items-center gap-1.5 flex-wrap">
                <span className="text-[11px] font-extrabold text-slate-500 mr-1 inline-flex items-center gap-1">
                  <Lightbulb className="w-3.5 h-3.5 text-amber-500 shrink-0" />
                  <span>{isEn ? 'Want to focus on a specific skill today? Ask Teacher Tony:' : 'Muốn đổi kỹ năng học hôm nay? Bấm hỏi Thầy ngay:'}</span>
                </span>
                {quickPrompts.map((qp, idx) => (
                  <button
                    key={idx}
                    type="button"
                    disabled={isAiThinking}
                    onClick={() => handleSendUserQuestion(qp.prompt)}
                    className="bg-white hover:bg-[#0a5482] text-[#0a5482] hover:text-white border border-slate-200 hover:border-[#0a5482] text-xs font-extrabold px-3 py-1.5 rounded-xl transition shadow-2xs cursor-pointer disabled:opacity-50 flex items-center gap-1.5"
                  >
                    <span className={`w-1.5 h-1.5 rounded-full ${courseAccent.dot} shrink-0`} />
                    <span>{qp.label}</span>
                  </button>
                ))}
              </div>

              {attachedImage && (
                <div className="flex flex-wrap items-center justify-between gap-3 bg-white border border-sky-200 rounded-xl p-2.5 animate-in fade-in duration-150">
                  <div className="flex items-center gap-3">
                    <div className="relative inline-block border border-slate-200 rounded-lg overflow-hidden shadow-2xs">
                      <img
                        src={attachedImage}
                        alt={isEn ? 'Attached exercise image' : 'Ảnh bài tập đính kèm'}
                        className="h-14 w-auto object-cover bg-slate-50"
                      />
                      <button
                        type="button"
                        onClick={() => setAttachedImage(null)}
                        className="absolute -top-1 -right-1 w-5 h-5 bg-rose-500 hover:bg-rose-600 text-white rounded-full flex items-center justify-center shadow cursor-pointer"
                        title={isEn ? 'Remove image' : 'Xóa ảnh'}
                      >
                        <X className="w-3 h-3" />
                      </button>
                    </div>
                    <div className="text-xs">
                      <div className="font-extrabold text-[#0a5482] flex items-center gap-1.5">
                        <Camera className="w-3.5 h-3.5 text-[#0a5482] shrink-0" />
                        <span>{isEn ? 'Exercise image attached' : 'Đã đính kèm ảnh bài tập'}</span>
                      </div>
                      <div className="text-slate-500 text-[11px]">
                        {isEn ? (
                          <>Click <b>"Ask AI Coach"</b> to solve right here, or open on the Blackboard for live explanation</>
                        ) : (
                          <>Bấm <b>"Hỏi Thầy AI"</b> để giải ngay tại đây, hoặc đưa lên Bảng Đen để nghe giảng trực tiếp</>
                        )}
                      </div>
                    </div>
                  </div>
                  <button
                    type="button"
                    onClick={handleOpenImageOnBlackboard}
                    className="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-extrabold px-3 py-2 rounded-xl shadow-2xs transition cursor-pointer flex items-center gap-1.5"
                  >
                    <MonitorPlay className="w-3.5 h-3.5" />
                    <span>{isEn ? 'Solve Live on Blackboard' : 'Đưa ảnh lên Bảng Đen giảng trực tiếp'}</span>
                  </button>
                </div>
              )}

              <form
                onSubmit={(e) => {
                  e.preventDefault();
                  handleSendUserQuestion();
                }}
                className="flex items-center gap-2"
              >
                <button
                  type="button"
                  onClick={() => fileInputRef.current?.click()}
                  disabled={isAiThinking}
                  className="bg-white hover:bg-sky-50 text-[#0a5482] border border-slate-300 hover:border-[#0a5482] font-bold text-xs sm:text-sm px-3 py-2.5 rounded-xl shadow-2xs transition cursor-pointer shrink-0 flex items-center gap-1.5 disabled:opacity-40"
                  title={isEn ? 'Upload an exercise image or press Ctrl+V to paste a screenshot' : 'Tải ảnh bài tập lên hoặc bấm Ctrl+V để dán ảnh chụp màn hình'}
                >
                  <Camera className="w-4 h-4" />
                  <span className="hidden sm:inline">{isEn ? 'Upload' : 'Tải ảnh'}</span>
                </button>
                <input
                  type="file"
                  ref={fileInputRef}
                  className="hidden"
                  accept="image/png, image/jpeg, image/jpg, image/webp"
                  onChange={handleFileChange}
                />

                <input
                  type="text"
                  value={userInput}
                  onChange={(e) => setUserInput(e.target.value)}
                  onPaste={handlePaste}
                  disabled={isAiThinking}
                  placeholder={
                    isEn
                      ? 'Ask Teacher Tony or press Ctrl+V to paste a question image (e.g. "What should I study today?")...'
                      : 'Nhắn hỏi Thầy hoặc Ctrl+V dán ảnh bài tập (VD: "Thầy giải giúp em câu này / hôm nay em nên học gì?")...'
                  }
                  className="flex-1 min-w-0 bg-white border border-slate-300 focus:border-[#0a5482] rounded-xl px-4 py-2.5 text-xs sm:text-sm font-medium text-slate-800 outline-none shadow-2xs"
                />
                <button
                  type="submit"
                  disabled={(!userInput.trim() && !attachedImage) || isAiThinking}
                  className="bg-[#0a5482] hover:bg-[#084266] text-white font-extrabold text-xs sm:text-sm px-4 py-2.5 rounded-xl shadow-xs transition cursor-pointer disabled:opacity-40 shrink-0 flex items-center gap-1.5"
                >
                  <span>{isEn ? 'Ask AI Coach' : 'Hỏi Thầy AI'}</span>
                  <Send className="w-3.5 h-3.5" />
                </button>
              </form>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
