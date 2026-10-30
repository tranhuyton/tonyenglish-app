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
    formatted = formatted.replace(firstRegex, '<b class="font-black text-slate-950">$1</b>');
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
    const qText = userInput.trim() || 'Thầy giải chi tiết giúp em bài tập trong ảnh này với ạ.';
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
            courseTitle: cleanTitle(courseTitle || 'Tổng hợp'),
          },
        })
      );
    }, 600);
  };

  const isIelts = useMemo(() => {
    const t = (courseTitle || '').toLowerCase();
    return courseId === '239a64f0-c106-40e5-a6e2-4e685a0d70fb' || t.includes('ielts');
  }, [courseId, courseTitle]);

  const isIgcse0654 = useMemo(() => {
    const t = (courseTitle || '').toLowerCase();
    return (
      courseId === 'a2a949c7-c23e-45a7-82fa-cdeda5cc32a7' ||
      t.includes('co-ordinated') ||
      t.includes('0654')
    );
  }, [courseId, courseTitle]);

  const getCacheKey = (uid: string, cid: string) => `tony_ai_coach_chat_v5_${uid}_${cid}`;

  const askTonyAIBrain = async (
    snap: GlobalStudentSnapshot,
    userQuestion: string,
    isInitialAutoDiagnosis = false,
    imageBase64?: string | null
  ) => {
    setIsAiThinking(true);
    try {
      const imageInstruction = imageBase64
        ? `\n[HỌC VIÊN ĐÃ ĐÍNH KÈM 1 HÌNH ẢNH BÀI TẬP / ĐỀ BÀI]:
- Hãy quan sát thật kỹ hình ảnh đính kèm, đọc toàn bộ đề bài/câu hỏi/số liệu hoặc bài làm của học sinh trong ảnh.
- Giải chi tiết từng bước, giải thích rõ bản chất kiến thức, từ khóa ăn điểm (Marking Scheme) hoặc sửa lỗi sai cho học sinh một cách dễ hiểu nhất.
- Sau khi giải xong bài trong ảnh, hãy đối chiếu với Bản đồ khóa học ở trên để gợi ý bài giảng lý thuyết hoặc thư mục đề luyện tập liên quan kèm mã nút bấm [[ACTION:...]].\n`
        : '';

      const systemPrompt = `Bạn là "Thầy Tony AI" — người thầy chủ nhiệm kiêm gia sư trưởng trực tiếp dẫn dắt học viên tại TonyEnglish.vn.
Luôn xưng "Thầy" và gọi học viên bằng tên ("${snap.studentName}") hoặc "em". Giọng văn sống động, ấm áp, sát sao, đi thẳng vào dữ liệu thực tế của học viên (TUYỆT ĐỐI KHÔNG nói chung chung sáo rỗng, KHÔNG xưng con).

${snap.promptContext}
${imageInstruction}
[YÊU CẦU TRẢ LỜI]:
1. ${
        imageBase64
          ? 'Ưu tiên giải quyết thật chi tiết, cặn kẽ bài tập/câu hỏi trong hình ảnh mà học viên vừa gửi lên.'
          : `Nhìn thẳng vào số liệu thực tế của ${snap.studentName} ở trên (điểm các bài test gần nhất của khóa học này, bài giảng đang làm dở trên Bảng công việc, bài giảng tiếp theo chưa học, và tiến độ đọc Bài dịch Cambridge trong Thư viện).`
      }
2. Giao hoặc gợi ý các công việc cụ thể tiếp theo cần làm (viết rõ tên bài giảng, tên bộ đề hoặc tên mục Thư viện).
3. BẮT BUỘC chèn từ 1 đến 4 mã nút bấm hành động theo đúng cú pháp [[ACTION:OPEN_LECTURE:<ID>|<Nhãn nút>]], [[ACTION:OPEN_FOLDER:<ID>|<Nhãn nút>]], [[ACTION:OPEN_LIBRARY:<URL>|<Nhãn nút>]], [[ACTION:OPEN_AI_ROOM:<speaking|task1|task2>|<Nhãn nút>]], hoặc [[ACTION:OPEN_TAB:<board|analytics>|<Nhãn nút>]] ở cuối câu trả lời để học sinh bấm 1 click là mở thẳng bài đó.

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
        throw new Error('Hệ thống AI đang bận, vui lòng thử lại sau giây lát.');
      }

      const rawReply = data?.result || data?.text || data?.response || '';
      const { cleanedText, actions } = parseTutorResponseWithActions(rawReply);

      const aiMsg: CoachMessage = {
        role: 'ai',
        text: cleanedText,
        actions,
        timestamp: new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' }),
      };

      setMessages((prev) => {
        const next = isInitialAutoDiagnosis ? [aiMsg] : [...prev, aiMsg];
        try {
          sessionStorage.setItem(getCacheKey(snap.userId, courseId), JSON.stringify(next));
        } catch {}
        return next;
      });
    } catch (err: any) {
      // Fallback thông minh từ dữ liệu thật nếu mạng/API chập chờn
      const fallbackActions: TutorActionItem[] = [];
      const firstInProg = snap.taskProgress.inProgressLectures[0];
      const firstNextUp = snap.taskProgress.nextUpLectures[0];
      const targetLec = firstInProg || firstNextUp;

      if (targetLec) {
        fallbackActions.push({
          type: 'OPEN_LECTURE',
          target: targetLec.id,
          label: `📖 Học bài: ${targetLec.title}`,
        });
      }
      if (snap.isIelts) {
        fallbackActions.push({
          type: 'OPEN_LIBRARY',
          target: '/news/category/cambridge-ielts-reading-translation',
          label: '📚 Mở Thư viện: Bài dịch đọc Cambridge',
        });
        fallbackActions.push({
          type: 'OPEN_LIBRARY',
          target: '/news/category/cambridge-ielts-listening-translation',
          label: '🎧 Mở Thư viện: Bài dịch nghe Cambridge',
        });
      }
      fallbackActions.push({
        type: 'OPEN_TAB',
        target: 'board',
        label: '📋 Mở Bảng Công Việc',
      });

      const fallbackMsg: CoachMessage = {
        role: 'ai',
        text: `Chào **${snap.studentName}**! Thầy đã kiểm tra hồ sơ học tập của em: hiện tại em đã hoàn thành **${snap.taskProgress.completedTasks}/${snap.taskProgress.totalTasks} đầu việc (${snap.taskProgress.percent}%)** trên Bảng công việc${
          snap.recentTests[0]
            ? ` và bài kiểm tra gần nhất **${snap.recentTests[0].title}** đạt **${snap.recentTests[0].scoreLabel}**`
            : ''
        }.\n\nHôm nay thầy giao cho em ưu tiên hoàn thành bài giảng **${
          targetLec ? targetLec.title : 'tiếp theo trong lộ trình'
        }** và kết hợp đọc bài dịch song ngữ trong Thư viện nhé!`,
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
      const snap = await fetchGlobalStudentSnapshot(courseId, courseTitle);
      if (!isMounted) return;
      setIsLoadingSnapshot(false);

      if (!snap) return;
      setSnapshot(snap);

      // Check session cache first so we don't waste tokens on every tab switch
      try {
        const savedChat = sessionStorage.getItem(getCacheKey(snap.userId, courseId));
        if (savedChat) {
          const parsed = JSON.parse(savedChat);
          if (Array.isArray(parsed) && parsed.length > 0) {
            setMessages(parsed);
            return;
          }
        }
      } catch {}

      // Auto-trigger Thầy Tony AI's first live diagnosis!
      await askTonyAIBrain(
        snap,
        snap.isIelts
          ? 'Hãy phân tích hồ sơ học tập hiện tại của em (điểm các bài test gần nhất, các bài đang làm dở trên Bảng công việc, tiến độ đọc bài dịch Thư viện và khóa bổ trợ Grammar and Vocabulary) rồi chủ động giao cho em các việc cần làm ngay trong buổi học hôm nay (bao gồm cả việc làm thêm bài tập từ vựng/ngữ pháp trong khóa Grammar and Vocabulary) nhé!'
          : `Hãy phân tích hồ sơ học tập hiện tại của em trong khóa ${cleanTitle(courseTitle)} (điểm các bài kiểm tra gần nhất và các bài giảng đang làm dở / kế tiếp trên Bảng công việc) rồi chủ động giao cho em các việc cần làm ngay trong buổi học hôm nay nhé!`,
        true
      );
    };

    initBrain();
    return () => {
      isMounted = false;
    };
  }, [courseId, courseTitle]);

  const handleRefreshDiagnosis = async () => {
    setIsLoadingSnapshot(true);
    clearGlobalTutorCache();
    const freshSnap = await fetchGlobalStudentSnapshot(courseId, courseTitle, true);
    setIsLoadingSnapshot(false);
    if (!freshSnap) return;
    setSnapshot(freshSnap);

    await askTonyAIBrain(
      freshSnap,
      freshSnap.isIelts
        ? 'Em vừa cập nhật tiến độ học tập mới nhất. Thầy kiểm tra lại toàn bộ điểm số, Bảng công việc, Thư viện và khóa bổ trợ Grammar and Vocabulary để giao việc tiếp theo cho em nhé!'
        : 'Em vừa cập nhật tiến độ học tập mới nhất. Thầy kiểm tra lại toàn bộ điểm số, Bảng công việc và Thư viện để giao việc tiếp theo cho em nhé!',
      true
    );
  };

  const handleSendUserQuestion = async (customPrompt?: string) => {
    const rawQ = (customPrompt ?? userInput).trim();
    const imgToSend = customPrompt ? null : attachedImage;
    if ((!rawQ && !imgToSend) || isAiThinking || !snapshot) return;

    const q = rawQ || 'Thầy giải chi tiết giúp em bài tập trong hình ảnh này nhé!';

    if (!customPrompt) {
      setUserInput('');
      setAttachedImage(null);
    }
    const userMsg: CoachMessage = {
      role: 'user',
      text: q,
      imageUrl: imgToSend || undefined,
      timestamp: new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' }),
    };
    setMessages((prev) => [...prev, userMsg]);
    setTimeout(() => {
      chatBottomRef.current?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 80);

    await askTonyAIBrain(snapshot, q, false, imgToSend);
    setTimeout(() => {
      chatBottomRef.current?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 120);
  };

  if (!courseId || courseId === 'all') return null;

  const quickPrompts = isIelts
    ? [
        {
          icon: '🎯',
          label: 'Giao việc ưu tiên hôm nay',
          prompt:
            'Dựa vào điểm test gần nhất, các bài đang làm dở trên Bảng công việc và khóa bổ trợ Grammar & Vocabulary của em, hôm nay em nên ưu tiên làm những việc nào nhất hả thầy?',
        },
        {
          icon: '📚',
          label: 'Bổ trợ Grammar & Vocabulary',
          prompt:
            'Thầy kiểm tra lực học hiện tại của em và sai em làm thêm các bài tập phù hợp trong khóa Grammar and Vocabulary (như 4000 English Words, Vocabulary Organiser, Expand Vocabulary Through Reading hoặc bài tập Grammar) kèm nút mở bài để em tăng cường từ vựng và ngữ pháp phục vụ IELTS nhé!',
        },
        {
          icon: '🎧',
          label: 'Hôm nay em muốn cày Listening',
          prompt:
            'Hôm nay em muốn tập trung luyện kỹ năng Listening. Thầy xem điểm Listening và tiến độ đọc Bài dịch nghe Cambridge của em rồi giao bài cụ thể kèm nút mở bài giúp em nhé!',
        },
        {
          icon: '📖',
          label: 'Hôm nay em muốn cày Reading',
          prompt:
            'Hôm nay em muốn tập trung luyện kỹ năng Reading. Thầy xem điểm Reading, tiến độ đọc Bài dịch đọc Cambridge và từ vựng của em rồi giao bài cụ thể kèm nút mở bài giúp em nhé!',
        },
        {
          icon: '✍️',
          label: 'Hướng dẫn luyện Writing hôm nay',
          prompt:
            'Hôm nay em muốn học Writing (Task 1 & Task 2). Thầy xem trên Bảng công việc em đã học tới bài Writing nào rồi và giao bài học tiếp theo kèm phòng chấm AI cho em nhé!',
        },
        {
          icon: '🎙️',
          label: 'Hướng dẫn luyện Speaking hôm nay',
          prompt:
            'Hôm nay em muốn luyện Speaking. Thầy kiểm tra xem trong học phần Luyện thi Nói (Main Blocks / Plugin Blocks) em đã làm xong bài nào rồi và giao bài kế tiếp kèm phòng luyện Speaking AI cho em nhé!',
        },
      ]
    : isIgcse0654
    ? [
        {
          icon: '🎯',
          label: 'Giao việc ưu tiên hôm nay',
          prompt:
            'Dựa vào tiến độ các chương Biology, Chemistry, Physics và điểm test gần nhất của em, hôm nay em nên học chương nào và làm bài tập nào tiếp theo hả thầy?',
        },
        {
          icon: '🧬',
          label: 'Hôm nay em học Biology (B1–B19)',
          prompt:
            'Hôm nay em muốn học phân môn Biology (B1–B19). Thầy kiểm tra xem em đã học tới chương B mấy rồi và giao bài giảng + bộ đề Topic Paper tương ứng cho em nhé!',
        },
        {
          icon: '🧪',
          label: 'Hôm nay em học Chemistry (C1–C12)',
          prompt:
            'Hôm nay em muốn học phân môn Chemistry (C1–C12). Thầy kiểm tra xem em đã học tới chương C mấy rồi và giao bài giảng + bộ đề Topic Paper tương ứng cho em nhé!',
        },
        {
          icon: '⚡',
          label: 'Hôm nay em học Physics (P1–P6)',
          prompt:
            'Hôm nay em muốn học phân môn Physics (P1–P6). Thầy kiểm tra xem em đã học tới chương P mấy rồi và giao bài giảng + bộ đề Topic Paper tương ứng cho em nhé!',
        },
        {
          icon: '📄',
          label: 'Tư vấn luyện Past Papers (Paper 2, 4, 6)',
          prompt:
            'Thầy tư vấn giúp em hôm nay nên luyện đề Past Paper nào (Paper 2 Multiple Choice, Paper 4 Extended hay Paper 6 Practical) dựa trên lực học hiện tại của em nhé!',
        },
      ]
    : [
        {
          icon: '🎯',
          label: 'Giao việc ưu tiên hôm nay',
          prompt: `Dựa vào tiến độ học tập và điểm kiểm tra gần nhất của em trong khóa ${cleanTitle(courseTitle)}, hôm nay em nên ưu tiên học bài giảng nào và làm bài tập nào tiếp theo hả thầy?`,
        },
        {
          icon: '📖',
          label: 'Học tiếp bài giảng lý thuyết',
          prompt: `Thầy kiểm tra trên Bảng công việc của khóa ${cleanTitle(courseTitle)} xem em đang làm dở hoặc cần học tiếp bài giảng lý thuyết nào rồi giao việc kèm nút mở bài cho em nhé!`,
        },
        {
          icon: '📝',
          label: 'Chọn đề luyện tập hôm nay',
          prompt: `Thầy tư vấn và chọn giúp em thư mục đề luyện tập phù hợp nhất trong Kho đề của khóa ${cleanTitle(courseTitle)} để em làm bài hôm nay nhé!`,
        },
        {
          icon: '📊',
          label: 'Phân tích điểm yếu & Cách ôn tập',
          prompt: `Thầy phân tích giúp em kết quả các bài kiểm tra gần đây trong khóa ${cleanTitle(courseTitle)} xem em đang yếu ở chuyên đề nào và cần ôn lại bài giảng nào nhé!`,
        },
      ];

  const displayStudentName = extractStudentFirstName(snapshot?.studentName || studentName);
  const latestTest = snapshot?.recentTests?.[0] || null;
  const activeWorkLecture =
    snapshot?.taskProgress?.inProgressLectures?.[0] ||
    snapshot?.taskProgress?.nextUpLectures?.[0] ||
    null;

  return (
    <div
      className={`${
        onClose ? '' : 'mb-8'
      } rounded-2xl sm:rounded-3xl border-2 border-[#2ab4e8]/45 bg-white shadow-lg transition-all`}
    >
      {/* TOP HEADER BAR OF AI STUDY COACH */}
      <div
        className={`bg-gradient-to-r from-[#072f49] via-[#0a5482] to-[#0f172a] px-4 sm:px-5 py-2.5 sm:py-3 text-white flex flex-wrap items-center justify-between gap-2.5 rounded-t-[14px] sm:rounded-t-[22px] ${
          isWindowCollapsed ? 'rounded-b-[14px] sm:rounded-b-[22px]' : ''
        }`}
      >
        <div className="flex items-center gap-2 sm:gap-2.5 min-w-0 flex-wrap">
          <div className="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-gradient-to-br from-[#2ab4e8] to-sky-400 text-slate-950 flex items-center justify-center text-xl shadow-md shrink-0">
            👨‍🏫
          </div>
          <span className="bg-emerald-400/20 text-emerald-300 border border-emerald-400/30 text-[10px] sm:text-[11px] font-black uppercase tracking-wider px-2.5 py-1 rounded-full flex items-center gap-1.5 min-w-0">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping shrink-0" />
            <span className="truncate">
              Thầy Tony AI Chủ Nhiệm<span className="hidden sm:inline"> • Phân Tích Tiến Độ Tổng Thể</span>
            </span>
          </span>
          <span className="bg-[#0f172a]/85 text-sky-200 border border-sky-400/35 text-[11px] sm:text-xs font-extrabold px-2.5 py-1 rounded-xl flex items-center gap-1.5 max-w-[200px] sm:max-w-[260px] truncate">
            <span className="truncate">🎓 {cleanTitle(courseTitle)}</span>
          </span>
        </div>

        <div className="flex items-center gap-2 shrink-0 flex-wrap">
          {!isWindowCollapsed && (
            <button
              type="button"
              onClick={() => setIsStatsCollapsed(!isStatsCollapsed)}
              className="bg-white/10 hover:bg-white/20 text-white border border-white/20 text-xs font-extrabold px-3 py-1.5 rounded-xl transition cursor-pointer flex items-center gap-1.5"
              title={
                isStatsCollapsed
                  ? 'Mở lại bảng tóm tắt tiến độ phía trên'
                  : 'Ẩn bảng tóm tắt tiến độ phía trên để cửa sổ chat cao hơn'
              }
            >
              <span>{isStatsCollapsed ? 'Hiện tóm tắt' : 'Ẩn tóm tắt'}</span>
              <span>{isStatsCollapsed ? '▼' : '▲'}</span>
            </button>
          )}

          {!onClose ? (
            <button
              type="button"
              onClick={() => setIsWindowCollapsed(!isWindowCollapsed)}
              className="bg-amber-400/20 hover:bg-amber-400/30 text-amber-200 border border-amber-300/40 text-xs font-extrabold px-3 py-1.5 rounded-xl transition cursor-pointer flex items-center gap-1.5"
              title={isWindowCollapsed ? 'Mở lại cửa sổ tư vấn Thầy Tony AI' : 'Thu gọn toàn bộ cửa sổ Thầy Tony AI'}
            >
              <span>{isWindowCollapsed ? 'Mở cửa sổ chat ▼' : 'Thu gọn cửa sổ ▲'}</span>
            </button>
          ) : (
            <button
              type="button"
              onClick={onClose}
              className="px-3 py-1.5 rounded-xl bg-rose-500/80 hover:bg-rose-600 text-white border border-rose-400/50 font-black text-xs flex items-center gap-1.5 transition cursor-pointer"
              title="Đóng cửa sổ Thầy Tony AI"
            >
              <span>✕</span>
              <span className="hidden sm:inline">Đóng</span>
            </button>
          )}
        </div>
      </div>

      {!isWindowCollapsed && (
        <div className="p-3 sm:p-4 space-y-3.5 bg-gradient-to-b from-sky-50/50 to-white rounded-b-[14px] sm:rounded-b-[22px]">
          {/* 1. REAL-TIME STUDENT X-RAY RADAR (4 THẺ DỮ LIỆU TỔNG THỂ THỰC TẾ) */}
          {!isStatsCollapsed && snapshot && (
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-2 sm:gap-3 animate-in fade-in duration-150">
              {/* Card 1: Bảng công việc */}
              <div
                onClick={() =>
                  executeTutorAction(
                    { type: 'OPEN_TAB', target: 'board', label: 'Bảng công việc' },
                    courseId,
                    { onOpenLecture, onSelectFolder, onNavigate }
                  )
                }
                className="bg-white hover:bg-sky-50/60 border border-slate-200/90 hover:border-[#2ab4e8] rounded-xl sm:rounded-2xl p-2.5 sm:p-3.5 shadow-2xs transition cursor-pointer flex flex-col justify-between"
              >
                <div className="flex items-center justify-between gap-2">
                  <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-500">
                    📋 Bảng công việc
                  </span>
                  <span className="text-xs font-black text-[#0a5482] bg-sky-50 px-2 py-0.5 rounded-full border border-sky-200">
                    {snapshot.taskProgress.percent}%
                  </span>
                </div>
                <div className="mt-2">
                  <div className="text-base font-black text-slate-900">
                    {snapshot.taskProgress.completedTasks} / {snapshot.taskProgress.totalTasks} việc
                  </div>
                  <div className="text-[11.5px] text-slate-500 font-semibold truncate mt-0.5">
                    Xong trọn vẹn {snapshot.taskProgress.completedLecturesCount}/
                    {snapshot.taskProgress.totalLecturesCount} bài giảng
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
                className="bg-white hover:bg-emerald-50/60 border border-slate-200/90 hover:border-emerald-400 rounded-2xl p-3.5 shadow-2xs transition cursor-pointer flex flex-col justify-between"
              >
                <div className="flex items-center justify-between gap-2">
                  <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-500">
                    📖 Bài cần học ngay
                  </span>
                  <span className="text-[10.5px] font-black text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">
                    {snapshot.taskProgress.inProgressLectures.length > 0 ? 'Đang làm dở' : 'Bài kế tiếp'}
                  </span>
                </div>
                <div className="mt-2">
                  <div className="text-sm font-black text-slate-900 truncate" title={activeWorkLecture?.title}>
                    {activeWorkLecture ? activeWorkLecture.title : 'Đã hoàn thành hết bài'}
                  </div>
                  <div className="text-[11.5px] text-emerald-700 font-bold truncate mt-0.5">
                    {activeWorkLecture ? `Bấm để mở ngay bài này →` : 'Tuyệt vời!'}
                  </div>
                </div>
              </div>

              {/* Card 3: Điểm Test gần nhất */}
              <div
                onClick={() =>
                  executeTutorAction(
                    { type: 'OPEN_TAB', target: 'analytics', label: 'Tiến độ học' },
                    courseId,
                    { onOpenLecture, onSelectFolder, onNavigate }
                  )
                }
                className="bg-white hover:bg-amber-50/60 border border-slate-200/90 hover:border-amber-400 rounded-2xl p-3.5 shadow-2xs transition cursor-pointer flex flex-col justify-between"
              >
                <div className="flex items-center justify-between gap-2">
                  <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-500">
                    🎯 Điểm Test gần nhất
                  </span>
                  {latestTest && (
                    <span
                      className={`text-[10.5px] font-black px-2 py-0.5 rounded-full border ${
                        latestTest.isLow
                          ? 'bg-amber-50 text-amber-800 border-amber-200'
                          : 'bg-emerald-50 text-emerald-700 border-emerald-200'
                      }`}
                    >
                      {latestTest.scoreLabel}
                    </span>
                  )}
                </div>
                <div className="mt-2">
                  <div className="text-sm font-black text-slate-900 truncate" title={latestTest?.title}>
                    {latestTest ? latestTest.title : 'Chưa có bài kiểm tra'}
                  </div>
                  <div className="text-[11.5px] text-slate-500 font-semibold truncate mt-0.5">
                    {latestTest
                      ? `Ngày ${latestTest.dateLabel} • Kỹ năng ${latestTest.skill}`
                      : 'Hãy làm 1 đề để AI chẩn đoán lực học'}
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
                        label: 'Thư viện Bài dịch',
                      },
                      courseId,
                      { onOpenLecture, onSelectFolder, onNavigate }
                    )
                  }
                  className="bg-white hover:bg-indigo-50/60 border border-slate-200/90 hover:border-indigo-400 rounded-2xl p-3.5 shadow-2xs transition cursor-pointer flex flex-col justify-between"
                >
                  <div className="flex items-center justify-between gap-2">
                    <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-500">
                      📚 Thư viện Dịch Cam
                    </span>
                    <span className="text-[10.5px] font-black text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded-full border border-indigo-200">
                      Bắt buộc
                    </span>
                  </div>
                  <div className="mt-2">
                    <div className="text-sm font-black text-slate-900">
                      Đọc: {snapshot.libraryProgress.camReadingCount}/252 • Nghe:{' '}
                      {snapshot.libraryProgress.camListeningCount}/336
                    </div>
                    <div className="text-[11.5px] text-indigo-700 font-bold truncate mt-0.5">
                      Mở Thư viện Bài dịch Cambridge →
                    </div>
                  </div>
                </div>
              ) : (
                <div
                  onClick={() =>
                    executeTutorAction(
                      { type: 'OPEN_TAB', target: 'analytics', label: 'Tiến độ học' },
                      courseId,
                      { onOpenLecture, onSelectFolder, onNavigate }
                    )
                  }
                  className="bg-white hover:bg-indigo-50/60 border border-slate-200/90 hover:border-indigo-400 rounded-2xl p-3.5 shadow-2xs transition cursor-pointer flex flex-col justify-between"
                >
                  <div className="flex items-center justify-between gap-2">
                    <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-500">
                      📊 Tổng số bài thi
                    </span>
                    <span className="text-[10.5px] font-black text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded-full border border-indigo-200 truncate max-w-[110px]">
                      {isIgcse0654 ? 'IGCSE 0654' : 'Kho đề & Thi'}
                    </span>
                  </div>
                  <div className="mt-2">
                    <div className="text-sm font-black text-slate-900">
                      Đã làm {snapshot.recentTests.length} bài gần đây
                    </div>
                    <div className="text-[11.5px] text-indigo-700 font-bold truncate mt-0.5">
                      Xem chi tiết Báo cáo hiệu suất →
                    </div>
                  </div>
                </div>
              )}
            </div>
          )}

          {/* 2. DYNAMIC AI CONVERSATION & ACTIONABLE ADVICE STREAM */}
          <div className="bg-white rounded-2xl border border-sky-200/90 shadow-xs overflow-hidden">
            <div className="bg-sky-50/80 border-b border-sky-100 px-4 py-2.5 flex items-center justify-between gap-2 flex-wrap">
              <div className="flex items-center gap-2 flex-wrap">
                <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                <span className="text-xs font-extrabold uppercase tracking-wider text-[#0a5482] flex items-center gap-1.5 flex-wrap">
                  <span>Nhận xét &amp; Chỉ định công việc trực tiếp từ Thầy Tony AI cho</span>
                  <span className="font-black text-slate-950">{displayStudentName}</span>
                </span>
              </div>
              <div className="flex items-center gap-2 flex-wrap">
                <button
                  type="button"
                  onClick={handleRefreshDiagnosis}
                  disabled={isAiThinking || isLoadingSnapshot}
                  className="text-[11px] font-extrabold text-emerald-800 hover:bg-emerald-100 bg-emerald-50 border border-emerald-300 px-2.5 py-1 rounded-lg transition cursor-pointer flex items-center gap-1.5 disabled:opacity-50"
                  title="Quét lại điểm số & tiến độ mới nhất để Thầy AI tư vấn lại"
                >
                  <span className={isAiThinking || isLoadingSnapshot ? 'animate-spin' : ''}>🔄</span>
                  <span>Phân tích lại tiến độ</span>
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
                    Thầy Tony AI đang đọc bảng điểm, các bài đang làm dở và nhật ký Thư viện của{' '}
                    <span className="font-black text-slate-950">{displayStudentName}</span>...
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
                    <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-[#0a5482] to-[#073b5c] text-white flex items-center justify-center shrink-0 mr-3 mt-0.5 shadow-xs text-base">
                      👨‍🏫
                    </div>
                  )}

                  <div
                    className={`max-w-[92%] sm:max-w-[88%] rounded-2xl p-4 text-[13.5px] sm:text-[14.5px] leading-relaxed ${
                      msg.role === 'user'
                        ? 'bg-[#0a5482] text-white rounded-tr-xs font-semibold shadow-xs'
                        : 'bg-slate-50/90 border border-slate-200/90 text-slate-800 rounded-tl-xs shadow-2xs'
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
                              <span>⚡</span>
                              <span>Bấm vào đây để thực hiện ngay các việc Thầy vừa giao:</span>
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
                  <div className="w-8 h-8 rounded-xl bg-gradient-to-br from-[#0a5482] to-[#073b5c] text-white flex items-center justify-center shrink-0">
                    👨‍🏫
                  </div>
                  <div className="bg-slate-100 border border-slate-200 px-4 py-2.5 rounded-2xl flex items-center gap-2">
                    <span className="w-2 h-2 bg-[#2ab4e8] rounded-full animate-bounce" />
                    <span className="w-2 h-2 bg-[#0a5482] rounded-full animate-bounce delay-100" />
                    <span className="w-2 h-2 bg-[#2ab4e8] rounded-full animate-bounce delay-200" />
                    <span className="ml-1 text-slate-600">
                      Thầy Tony AI đang suy nghĩ và chọn bài phù hợp nhất cho{' '}
                      <span className="font-black text-slate-950">{displayStudentName}</span>...
                    </span>
                  </div>
                </div>
              )}

              <div ref={chatBottomRef} />
            </div>

            {/* 3. QUICK FOCUS PROMPTS & DIRECT CHAT INPUT */}
            <div className="p-3.5 sm:p-4 bg-slate-50 border-t border-slate-200/80 space-y-3">
              <div className="flex items-center gap-1.5 flex-wrap">
                <span className="text-[11px] font-extrabold text-slate-500 mr-1">
                  💡 Muốn đổi kỹ năng học hôm nay? Bấm hỏi Thầy ngay:
                </span>
                {quickPrompts.map((qp, idx) => (
                  <button
                    key={idx}
                    type="button"
                    disabled={isAiThinking}
                    onClick={() => handleSendUserQuestion(qp.prompt)}
                    className="bg-white hover:bg-[#0a5482] text-[#0a5482] hover:text-white border border-sky-200 hover:border-[#0a5482] text-xs font-extrabold px-3 py-1.5 rounded-xl transition shadow-2xs cursor-pointer disabled:opacity-50 flex items-center gap-1.5"
                  >
                    <span>{qp.icon}</span>
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
                        alt="Ảnh bài tập đính kèm"
                        className="h-14 w-auto object-cover bg-slate-50"
                      />
                      <button
                        type="button"
                        onClick={() => setAttachedImage(null)}
                        className="absolute -top-1 -right-1 w-5 h-5 bg-rose-500 hover:bg-rose-600 text-white rounded-full flex items-center justify-center text-[10px] font-bold shadow cursor-pointer"
                        title="Xóa ảnh"
                      >
                        ✕
                      </button>
                    </div>
                    <div className="text-xs">
                      <div className="font-extrabold text-[#0a5482]">📸 Đã đính kèm ảnh bài tập</div>
                      <div className="text-slate-500 text-[11px]">
                        Bấm <b>"Hỏi Thầy AI"</b> để giải ngay tại đây, hoặc đưa lên Bảng Đen để nghe giảng trực tiếp
                      </div>
                    </div>
                  </div>
                  <button
                    type="button"
                    onClick={handleOpenImageOnBlackboard}
                    className="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-extrabold px-3 py-2 rounded-xl shadow-2xs transition cursor-pointer flex items-center gap-1.5"
                  >
                    <span>👨‍🏫</span>
                    <span>Đưa ảnh lên Bảng Đen giảng trực tiếp</span>
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
                  className="bg-white hover:bg-sky-50 text-[#0a5482] border border-slate-300 hover:border-[#2ab4e8] font-bold text-xs sm:text-sm px-3 py-2.5 rounded-xl shadow-2xs transition cursor-pointer shrink-0 flex items-center gap-1.5 disabled:opacity-40"
                  title="Tải ảnh bài tập lên hoặc bấm Ctrl+V để dán ảnh chụp màn hình"
                >
                  <span>📷</span>
                  <span className="hidden sm:inline">Tải ảnh</span>
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
                  placeholder={`Nhắn hỏi Thầy hoặc Ctrl+V dán ảnh bài tập (VD: "Thầy giải giúp em câu này / hôm nay em nên học gì?")...`}
                  className="flex-1 bg-white border border-slate-300 focus:border-[#2ab4e8] rounded-xl px-4 py-2.5 text-xs sm:text-sm font-medium text-slate-800 outline-none shadow-2xs"
                />
                <button
                  type="submit"
                  disabled={(!userInput.trim() && !attachedImage) || isAiThinking}
                  className="bg-[#0a5482] hover:bg-[#084266] text-white font-extrabold text-xs sm:text-sm px-4 py-2.5 rounded-xl shadow-xs transition cursor-pointer disabled:opacity-40 shrink-0 flex items-center gap-1.5"
                >
                  <span>Hỏi Thầy AI</span>
                  <span>➤</span>
                </button>
              </form>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
