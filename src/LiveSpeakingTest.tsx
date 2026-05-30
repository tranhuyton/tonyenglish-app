import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import React, { useState, useRef, useEffect, useMemo } from 'react';
import { supabase } from './supabase';

// =========================================================================================
// 🚀 CSS: STYLE CHỮ PHẤN VIẾT TAY CHO CHẾ ĐỘ BẢNG ĐEN
// =========================================================================================
const chalkboardStyleTag = `
  @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');
  
  .tony-chalkboard-content, 
  .tony-chalkboard-content p,
  .tony-chalkboard-content span,
  .tony-chalkboard-content div,
  .tony-chalkboard-content li {
    font-family: 'Patrick Hand', 'Segoe UI', sans-serif !important;
    color: #f8fafc !important; 
    font-size: 1.5rem !important;
    line-height: 1.6 !important;
    letter-spacing: 0.02em !important;
    word-spacing: 0.08em !important;
    white-space: pre-wrap !important;
    word-break: break-word !important;
    text-shadow: 0px 1px 3px rgba(0,0,0,0.8) !important;
  }
  
  .tony-chalkboard-content p { 
    margin-bottom: 0.3rem !important; 
  }
  
  .tony-chalkboard-content ul,
  .tony-chalkboard-content ol {
    margin-top: 0.2rem !important;
    margin-bottom: 0.3rem !important;
    padding-left: 1.2rem !important;
  }
  
  .tony-chalkboard-content li {
    margin-bottom: 0.1rem !important;
  }
  
  .tony-chalkboard-content li p {
    margin-bottom: 0.1rem !important;
  }
  
  .tony-chalkboard-content strong,
  .tony-chalkboard-content b { 
    color: #fef08a !important; 
    font-weight: 700 !important; 
  }
  
  .tony-chalkboard-content h1, 
  .tony-chalkboard-content h2, 
  .tony-chalkboard-content h3 { 
    color: #67e8f9 !important; 
    font-weight: 700 !important; 
    margin-top: 1rem !important; 
    margin-bottom: 0.3rem !important; 
  }
  
  .tony-chalkboard-content .katex { 
    font-family: KaTeX_Math, 'Times New Roman', serif !important; 
    font-size: 1.5rem !important; 
    color: #fef08a !important; 
  }
`;

type ChatMessage = {
    role: 'user' | 'model';
    text: string;
};

// === HÀM HỖ TRỢ XỬ LÝ ÂM THANH PCM ===
const floatTo16BitPCM = (float32Array: Float32Array) => {
    const buffer = new ArrayBuffer(float32Array.length * 2);
    const view = new DataView(buffer);
    let offset = 0;
    
    for (let i = 0; i < float32Array.length; i++, offset += 2) {
        let s = Math.max(-1, Math.min(1, float32Array[i]));
        view.setInt16(offset, s < 0 ? s * 0x8000 : s * 0x7FFF, true);
    }
    
    return buffer;
};

const arrayBufferToBase64 = (buffer: ArrayBuffer) => {
    let binary = '';
    const bytes = new Uint8Array(buffer);
    
    for (let i = 0; i < bytes.byteLength; i++) {
        binary += String.fromCharCode(bytes[i]);
    }
    
    return window.btoa(binary);
};

const base64ToArrayBuffer = (base64: string) => {
    const binary_string = window.atob(base64);
    const len = binary_string.length;
    const bytes = new Uint8Array(len);
    
    for (let i = 0; i < len; i++) {
        bytes[i] = binary_string.charCodeAt(i);
    }
    
    return bytes.buffer;
};

// =========================================================================================
// MAIN COMPONENT
// =========================================================================================
export default function LiveSpeakingTest({ 
    viewState, 
    onMinimize, 
    onMaximize, 
    onClose, 
    onOpenAI,
    courseTitle
}: { 
    viewState: 'FULLSCREEN' | 'MINIMIZED', 
    onMinimize: () => void, 
    onMaximize: () => void, 
    onClose: () => void, 
    onOpenAI?: (passedMode?: string) => void,
    courseTitle?: string
}) {
  const [status, setStatus] = useState<'IDLE' | 'CONNECTING' | 'CONNECTED'>('IDLE');
  // 🚀 PERSIST: Đọc giọng đã chọn từ sessionStorage (nếu có)
  const [examiner, setExaminer] = useState<'TONY' | 'DIEP'>(() => {
    return (sessionStorage.getItem('tony_voice_examiner') as 'TONY' | 'DIEP') || 'TONY';
  });
  const hasVoiceChosen = !!sessionStorage.getItem('tony_voice_examiner');
  
  const [isRecording, setIsRecording] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isTextOnlyMode, setIsTextOnlyMode] = useState(false); 
  const [isVisionMode, setIsVisionMode] = useState(false); // 🚀 Cờ đánh dấu não Mắt Thần
  const [isPendingVision, setIsPendingVision] = useState(() => {
      return typeof window !== 'undefined' && !!(window as any).tonyPendingImage;
  });
  const [activeVisionImage, setActiveVisionImage] = useState<string | null>(() => {
      return typeof window !== 'undefined' ? ((window as any).tonyLatestPdfPageImage || null) : null;
  });

  // Drag-and-drop state for minimized widget
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [isDragging, setIsDragging] = useState(false);
  const isDraggingRef = useRef(false);
  const dragStartRef = useRef({ x: 0, y: 0 });
  const positionRef = useRef({ x: 0, y: 0 });
  const hasDraggedRef = useRef(false);

  useEffect(() => {
      positionRef.current = position;
  }, [position]);

  useEffect(() => {
      const handleMouseMove = (e: MouseEvent | TouchEvent) => {
          if (!isDraggingRef.current) return;
          const clientX = 'touches' in e ? e.touches[0].clientX : e.clientX;
          const clientY = 'touches' in e ? e.touches[0].clientY : e.clientY;
          
          const dx = clientX - dragStartRef.current.x;
          const dy = clientY - dragStartRef.current.y;
          
          const screenW = window.innerWidth;
          const screenH = window.innerHeight;
          
          const limitX = Math.max(-screenW + 100, Math.min(50, dx));
          const limitY = Math.max(-screenH + 100, Math.min(50, dy));
          
          setPosition({ x: limitX, y: limitY });
          
          if (Math.abs(dx - positionRef.current.x) > 5 || Math.abs(dy - positionRef.current.y) > 5) {
              hasDraggedRef.current = true;
          }
      };

      const handleMouseUp = () => {
          isDraggingRef.current = false;
          setIsDragging(false);
      };

      window.addEventListener('mousemove', handleMouseMove, { passive: false });
      window.addEventListener('mouseup', handleMouseUp);
      window.addEventListener('touchmove', handleMouseMove, { passive: false });
      window.addEventListener('touchend', handleMouseUp);

      return () => {
          window.removeEventListener('mousemove', handleMouseMove);
          window.removeEventListener('mouseup', handleMouseUp);
          window.removeEventListener('touchmove', handleMouseMove);
          window.removeEventListener('touchend', handleMouseUp);
      };
  }, []);

  const handleDragStart = (e: React.MouseEvent | React.TouchEvent) => {
      const target = e.target as HTMLElement;
      if (target.closest('button') || target.closest('input') || target.closest('a') || target.closest('svg') || target.closest('path')) {
          return;
      }
      
      isDraggingRef.current = true;
      setIsDragging(true);
      hasDraggedRef.current = false;
      const clientX = 'touches' in e ? e.touches[0].clientX : e.clientX;
      const clientY = 'touches' in e ? e.touches[0].clientY : e.clientY;
      dragStartRef.current = {
          x: clientX - positionRef.current.x,
          y: clientY - positionRef.current.y
      };
  };

  const handleWidgetClick = (e: React.MouseEvent) => {
      if (hasDraggedRef.current) {
          e.stopPropagation();
          e.preventDefault();
          hasDraggedRef.current = false;
          return;
      }
      onMaximize();
  };
  
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [liveTranscript, setLiveTranscript] = useState<string>('');
  const [currentDraft, setCurrentDraft] = useState<string>('');
  const [chatInput, setChatInput] = useState<string>('');
  
  const [isBlackboardMode, setIsBlackboardMode] = useState(false);
  const [isChatBubbleVisible, setIsChatBubbleVisible] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [splitWidthVw, setSplitWidthVw] = useState(50);
  const isSplitDraggingRef = useRef(false);

  // REFS QUAN TRỌNG ĐIỀU KHIỂN LUỒNG
  const wsRef = useRef<WebSocket | null>(null);
  const isSetupCompleteRef = useRef<boolean>(false);
  const isMicOpenRef = useRef<boolean>(false); 
  const isRecordingRef = useRef<boolean>(false); 
  const interruptedRef = useRef<boolean>(false); // Flag: đang trong trạng thái ngắt lời AI
  const recordingTimeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null); // Auto-stop sau 30s
  const transcriptRef = useRef<string>('');
  const callStartTimeRef = useRef<number>(0);
  const isTextOnlyModeRef = useRef<boolean>(false); 
  
  // Audio Input/Output
  const streamRef = useRef<MediaStream | null>(null);
  const audioCtxInputRef = useRef<AudioContext | null>(null);
  const sourceNodeRef = useRef<MediaStreamAudioSourceNode | null>(null);
  const processorNodeRef = useRef<ScriptProcessorNode | null>(null);
  const geminiUserTranscriptRef = useRef<string>('');
  const audioCtxOutputRef = useRef<AudioContext | null>(null);
  const nextPlayTimeRef = useRef<number>(0);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // 🚀 QUẢN LÝ REF HÀM ĐỂ TỰ CHẠY
  const startSessionRef = useRef<any>(null);
  const startVisionSessionRef = useRef<any>(null);
  const stopCallRef = useRef<any>(null);

  useEffect(() => {
      startSessionRef.current = startSession;
      startVisionSessionRef.current = startVisionSession;
      stopCallRef.current = stopCall;
  });

  // 🚀 DỌN DẸP TOÀN BỘ KHI COMPONENT BỊ UNMOUNT (ĐÓNG HẲN WIDGET TRÁNH TRÔI LỆNH)
  useEffect(() => {
      return () => {
          if (stopCallRef.current) {
              stopCallRef.current();
          }
      };
  }, []);

  // 🚀 AUTO-START: Nếu đã chọn giọng trước đó → bỏ qua prompt, vào session luôn
  useEffect(() => {
      if (hasVoiceChosen && status === 'IDLE' && !isPendingVision) {
          // Đợi 1 tick để refs được gán
          const timer = setTimeout(() => {
              const mode = sessionStorage.getItem('tony_live_mode');
              if (startSessionRef.current) {
                  startSessionRef.current(mode === 'TUTOR'); // TUTOR → text mode
              }
          }, 100);
          return () => clearTimeout(timer);
      }
  }, []); // Chỉ chạy 1 lần khi mount

  // =========================================================================================
  // 🚀 KHỞI TẠO NÃO MẮT THẦN (VISION AI QUA EDGE FUNCTION - KHÔNG DÙNG WEBSOCKET)
  // =========================================================================================
  const startVisionSession = async (image: string, query: string, courseTitleOverride?: string) => {
      if (typeof window !== 'undefined') {
          (window as any).tonyPendingImage = null;
      }
      setIsPendingVision(false);
      setActiveVisionImage(image);

      const finalCourseTitle = courseTitleOverride || courseTitle || sessionStorage.getItem('tony_live_topic') || "Tổng hợp";
      setIsVisionMode(true);
      setIsTextOnlyMode(true);
      setStatus('CONNECTED');
      setMessages([{ role: 'user', text: `*(📸 Đã gửi ảnh bài tập)*\n\n${query}` }]);
      setIsProcessing(true);
      setLiveTranscript('');

      try {
          // Gọi API chuyên giải ảnh tĩnh
          const { data, error } = await supabase.functions.invoke('omni-vision-solver', {
              body: {
                  imageUrl: image,
                  content: query,
                  courseTitle: finalCourseTitle,
                  prompt: `[KỶ LUẬT CHUYÊN MÔN TUYỆT ĐỐI]
Bạn là một gia sư AI nghiêm khắc chuyên dạy môn "${finalCourseTitle}".
Bạn chỉ được phép giải quyết các câu hỏi và bài tập thuộc phạm vi môn học "${finalCourseTitle}".

QUY TẮC KIỂM TRA MÔN HỌC BẮT BUỘC:
1. Phân tích ảnh và câu hỏi của học sinh để xác định xem đề bài này có thuộc môn "${finalCourseTitle}" hay không.
   - Ví dụ: Nếu môn học là "Giao Tiếp Phản Xạ" hoặc các khóa tiếng Anh giao tiếp, nhưng đề bài lại là Toán học (có các biểu thức đại số, hình học, tích phân, tính toán số học, giải phương trình), Vật lý, Hóa học,... thì đề bài đó KHÔNG thuộc môn học này.
   - Ví dụ: Nếu môn học là "Toán" hoặc "Toán học", nhưng đề bài lại là Tiếng Anh giao tiếp, Tiếng Anh thương mại, Ngữ pháp tiếng Anh,... thì đề bài đó KHÔNG thuộc môn học này.

2. NẾU ĐỀ BÀI KHÔNG LIÊN QUAN TỚI MÔN HỌC "${finalCourseTitle}":
   - Bạn BẮT BUỘC PHẢI TỪ CHỐI GIẢI ĐÁP NGAY LẬP TỨC.
   - Câu trả lời từ chối bắt buộc phải viết: "Thầy/Cô không thể giải bài này vì nó thuộc môn học khác, không nằm trong phạm vi của khóa học ${finalCourseTitle}. Con vui lòng gửi đề bài đúng môn học nhé!"
   - Tuyệt đối KHÔNG giải thích thêm, KHÔNG đưa ra lời khuyên hay đáp án mẫu của đề bài đó.

3. NẾU ĐỀ BÀI LIÊN QUAN TỚI MÔN HỌC "${finalCourseTitle}":
   - Hãy đi thẳng vào giải chi tiết từng bước cho học sinh.
   - TUYỆT ĐỐI KHÔNG giới thiệu dông dài lý do tại sao bạn nhận giải (ví dụ: cấm nói "Vì đề này thuộc môn ${finalCourseTitle} nên thầy giải..."). Trả lời trực tiếp vào câu hỏi.
   - BẮT BUỘC sử dụng ký hiệu LaTeX ($...$ và $$...$$) để viết MỌI công thức toán học, và LUÔN LUÔN IN ĐẬM (**từ khóa**) các từ quan trọng, đáp án, danh từ riêng hoặc kết quả quan trọng để hệ thống tự vẽ bằng phấn vàng nổi bật.`
              }
          });

          if (error || !data) {
              throw new Error("Lỗi kết nối bộ não Mắt Thần.");
          }

          const resultText = data.result || "Thầy đang bị mờ mắt một chút, con chụp lại đề bài gửi lại cho thầy nhé.";
          
          setIsProcessing(false);
          
          // 🚀 HIỆU ỨNG VIẾT PHẤN LÊN BẢNG (TYPING EFFECT)
          let currentIndex = 0;
          setLiveTranscript('');
          
          const typingInterval = setInterval(() => {
              setLiveTranscript(prev => prev + resultText.charAt(currentIndex));
              currentIndex++;
              
              if (currentIndex >= resultText.length) {
                  clearInterval(typingInterval);
                  setMessages(prev => [...prev, { role: 'model', text: resultText }]);
                  setLiveTranscript('');
              }
          }, 15); // Tốc độ gõ 15 mili-giây/ký tự (Cực mượt)

      } catch (err) {
          setIsProcessing(false);
          setMessages(prev => [...prev, { role: 'model', text: "Hệ thống Mắt Thần đang quá tải, con vui lòng thử lại sau nhé!" }]);
      }
  };

  // 🚀 LẮNG NGHE LỆNH ÉP KHỞI ĐỘNG (TỪ SIDEBAR BẮN QUA)
  useEffect(() => {
      const handleForceStart = (e: any) => {
          const { mode, image, query, courseTitle } = e.detail;

          const runSession = () => {
              // 🧠 CHIA NÃO: NẾU LÀ CHẾ ĐỘ VISION (Có ảnh đính kèm)
              if (mode === 'vision_mode' && image) {
                  if (startVisionSessionRef.current) {
                      startVisionSessionRef.current(image, query, courseTitle);
                  }
              } 
              // 🧠 CHIA NÃO: NẾU LÀ CHẾ ĐỘ TEXT/VOICE BÌNH THƯỜNG
              else if (startSessionRef.current) {
                  startSessionRef.current(mode === 'text_mode');
              }
          };

          if (status !== 'IDLE') {
              if (stopCallRef.current) stopCallRef.current();
              setTimeout(runSession, 500);
          } else {
              runSession();
          }
      };
      
      window.addEventListener('tony-force-start', handleForceStart);
      return () => window.removeEventListener('tony-force-start', handleForceStart);
  }, [status]);

  // 🚀 LẮNG NGHE LỆNH RESTART (KHI USER BẤM GỌI CÂU KHÁC KHI ĐANG GỌI)
  useEffect(() => {
      const handleRestart = () => {
          console.log('🔄 Restart call: dập máy cũ, gọi lại với context mới');
          if (stopCallRef.current) stopCallRef.current();
          setMessages([]);
          setLiveTranscript('');
          // Đợi 500ms cho mọi thứ dọn sạch, rồi auto-start lại
          setTimeout(() => {
              if (startSessionRef.current) {
                  const mode = sessionStorage.getItem('tony_live_mode');
                  // Nếu là TUTOR mode (chữa bài) → tự động vào bằng text mode
                  startSessionRef.current(mode === 'TUTOR');
              }
          }, 500);
      };
      window.addEventListener('tony-restart-call', handleRestart);
      return () => window.removeEventListener('tony-restart-call', handleRestart);
  }, []);

  // 🚀 LẮNG NGHE LỆNH ÉP ĐÓNG CUỘC GỌI & DỌN DẸP SẠCH SẼ (VÍ DỤ KHI ĐÓNG BẢNG/PDF)
  useEffect(() => {
      const handleForceClose = () => {
          if (stopCallRef.current) {
              stopCallRef.current();
          }
          sessionStorage.removeItem('tony_live_mode');
          sessionStorage.removeItem('tony_tutor_data');
          onClose();
      };
      window.addEventListener('tony-force-close', handleForceClose);
      return () => window.removeEventListener('tony-force-close', handleForceClose);
  }, [onClose]);

  useEffect(() => {
    const handleNavigationEvent = (e: any) => {
        if (e.detail === 'live-test') {
            onMaximize();
        }
    };
    window.addEventListener('tony-navigate', handleNavigationEvent);
    return () => window.removeEventListener('tony-navigate', handleNavigationEvent);
  }, [onMaximize]);

  // 🚀 KHÔI PHỤC HÀM FULLSCREEN CHỐNG TRẮNG MÀN HÌNH
  useEffect(() => {
    const onFullscreenChange = () => setIsFullscreen(!!document.fullscreenElement);
    document.addEventListener('fullscreenchange', onFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', onFullscreenChange);
  }, []);

  // 🚀 LẮNG NGHE ẢNH TRANG PDF HIỆN TẠI ĐỂ UPDATE CHO NÃO MẮT THẦN
  useEffect(() => {
      const handleSendPageImage = (e: any) => {
          setActiveVisionImage(e.detail);
      };
      window.addEventListener('tony-send-page-image', handleSendPageImage);
      return () => window.removeEventListener('tony-send-page-image', handleSendPageImage);
  }, []);

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(e => console.log(e));
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
  };

  useEffect(() => {
      const handleBubbleState = (e: any) => setIsChatBubbleVisible(e.detail);
      window.addEventListener('tony-chat-bubble-state', handleBubbleState);
      const bubbleExists = !!document.querySelector('button[title="Mở lại khung Chat AI"]');
      setIsChatBubbleVisible(bubbleExists);
      return () => window.removeEventListener('tony-chat-bubble-state', handleBubbleState);
  }, []);

  useEffect(() => {
      const checkMode = () => {
          const hasPdf = document.querySelector('.react-pdf__Document') !== null;
          setIsBlackboardMode(hasPdf);
          if (hasPdf && viewState === 'FULLSCREEN') {
              window.dispatchEvent(new CustomEvent('tony-teacher-board-state', { detail: true }));
          } else {
              window.dispatchEvent(new CustomEvent('tony-teacher-board-state', { detail: false }));
          }
      };
      checkMode();
      
      const interval = setInterval(checkMode, 500);
      return () => {
          clearInterval(interval);
          window.dispatchEvent(new CustomEvent('tony-teacher-board-state', { detail: false }));
      };
  }, [viewState]);

  useEffect(() => {
      if (messagesEndRef.current) {
          messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
      }
  }, [messages, liveTranscript, currentDraft, isProcessing, isRecording]);





  const handleBackClick = () => {
    if (status !== 'IDLE') {
        onMinimize();
    } else {
        sessionStorage.removeItem('tony_live_mode');
        sessionStorage.removeItem('tony_tutor_data');
        onClose();
    }
  };

  const buildSystemPrompt = () => {
        const mode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
        const tutorDataRaw = sessionStorage.getItem('tony_tutor_data');
        const tutorData = tutorDataRaw ? JSON.parse(tutorDataRaw) : null;
        const currentTopic = sessionStorage.getItem('tony_live_topic') || "Bài tập giao tiếp tổng hợp";
        const teacherName = examiner === 'TONY' ? 'thầy Tôn' : 'cô Diệp';

        const hiddenContextRaw = sessionStorage.getItem('tony_lecture_context') || '';
        const imgRegex = /\[IMAGE_ANSWER:\s*(https?:\/\/[^\]]+)\]/g;
        const cleanTextContext = hiddenContextRaw.replace(imgRegex, '[CÓ BỨC ẢNH ĐÁP ÁN ĐÍNH KÈM]').trim();
        const contextInstruction = cleanTextContext 
            ? `\n\n[TÀI LIỆU DÀNH CHO BẠN ĐỂ DẠY HỌC SINH]:\n"""\n${cleanTextContext}\n"""` 
            : '';

        let promptKienNhan = isBlackboardMode 
        ? `[KỶ LUẬT THÉP VÀ CÁCH TRÌNH BÀY BẢNG]: Bạn bắt buộc dùng văn phong và từ vựng chuẩn miền Bắc (Hà Nội). Lời nói đang được chép lên bảng đen dạng Markdown. BẮT BUỘC dùng ký hiệu LaTeX ($...$ và $$...$$) để viết MỌI công thức toán học, và LUÔN LUÔN IN ĐẬM (**từ khóa**) các đáp án, danh từ riêng hoặc kết quả quan trọng để hệ thống tự vẽ bằng phấn vàng nổi bật. Tuyệt đối không tự giới thiệu mình là người Hà Nội hoặc nhắc đến xuất thân của mình với học sinh.`
        : `[KỶ LUẬT THÉP]: Bạn bắt buộc dùng văn phong và từ vựng chuẩn miền Bắc (Hà Nội). Trả lời ngắn gọn, tự nhiên. BẮT BUỘC dùng ký hiệu LaTeX ($...$ và $$...$$) cho công thức toán, và IN ĐẬM (**từ khóa**) các đáp án quan trọng để hệ thống tự vẽ bằng phấn vàng nổi bật. Tuyệt đối không tự giới thiệu mình là người Hà Nội hoặc nhắc đến xuất thân của mình với học sinh.`;
        
        if (mode === 'TUTOR' && tutorData) {
            return `Bạn là ${teacherName}. BỐI CẢNH BÀI HỌC: ${tutorData.transcript}. NHIỆM VỤ: ${tutorData.feedback}. ${promptKienNhan} ${contextInstruction}`;
        } else {
            return `Bạn là giám khảo IELTS tên ${teacherName}. Hãy yêu cầu tôi nói về chủ đề: "${currentTopic}". Luôn lắng nghe và phản hồi trực tiếp dựa trên nội dung của thí sinh. ${promptKienNhan} ${contextInstruction}`;
        }
  };

  // =========================================================================================
  // 🚀 KHỞI TẠO NÃO MỒM (WEBSOCKET AI CHO ĐÀM THOẠI/CHAT TEXT BÌNH THƯỜNG)
  // =========================================================================================
  const startSession = async (isTextMode = false) => {
      if (typeof window !== 'undefined') {
          (window as any).tonyPendingImage = null;
      }
      setIsPendingVision(false);

      // 🚀 DỌN DẸP PHIÊN CŨ (NẾU CÓ) ĐỂ TRÁNH LẶP KẾT NỐI & TIẾNG VỌNG SONG SONG
      if (wsRef.current) {
          try { wsRef.current.close(); } catch(e) {}
          wsRef.current = null;
      }
      if (processorNodeRef.current) {
          try { processorNodeRef.current.disconnect(); } catch(e) {}
          processorNodeRef.current = null;
      }
      if (sourceNodeRef.current) {
          try { sourceNodeRef.current.disconnect(); } catch(e) {}
          sourceNodeRef.current = null;
      }
      if (audioCtxInputRef.current) {
          try { if (audioCtxInputRef.current.state !== 'closed') audioCtxInputRef.current.close(); } catch(e) {}
          audioCtxInputRef.current = null;
      }
      if (audioCtxOutputRef.current) {
          try { if (audioCtxOutputRef.current.state !== 'closed') audioCtxOutputRef.current.close(); } catch(e) {}
          audioCtxOutputRef.current = null;
      }
      if (streamRef.current) {
          try { streamRef.current.getTracks().forEach(t => t.stop()); } catch(e) {}
          streamRef.current = null;
      }

      // 🧠 CHIA NÃO: Nếu là chat văn bản và có trang tài liệu PDF đang mở, chuyển thẳng sang chế độ giải ảnh Vision
      if (isTextMode && activeVisionImage) {
          setIsVisionMode(true);
          setIsTextOnlyMode(true);
          isTextOnlyModeRef.current = true;
          setStatus('CONNECTED');
          
          const welcomeMsg = examiner === 'TONY' 
              ? "Chào con! Thầy đã nhìn thấy trang tài liệu PDF của con ở bên trái rồi. Con cần thầy trợ giúp giải câu nào hay phần nào trên trang này, hãy gõ câu hỏi xuống dưới nhé!"
              : "Chào con! Cô đã nhìn thấy trang tài liệu PDF của con ở bên trái rồi. Con cần cô trợ giúp giải câu nào hay phần nào trên trang này, hãy gõ câu hỏi xuống dưới nhé!";
          
          setMessages([{ role: 'model', text: welcomeMsg }]);
          setLiveTranscript('');
          isMicOpenRef.current = false;
          isRecordingRef.current = false;
          isSetupCompleteRef.current = false;
          callStartTimeRef.current = Date.now();
          return;
      }

      setIsVisionMode(false); 
      setIsTextOnlyMode(isTextMode);
      isTextOnlyModeRef.current = isTextMode; 
      
      setStatus('CONNECTING');
      setMessages([]);
      transcriptRef.current = '';
      setLiveTranscript('');
      isMicOpenRef.current = false;
      isRecordingRef.current = false;
      isSetupCompleteRef.current = false;
      callStartTimeRef.current = Date.now();
      
      if (!isBlackboardMode) {
          onMinimize();
      }

      try {
          const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
          audioCtxOutputRef.current = new AudioContextClass({ sampleRate: 24000 });
          if (audioCtxOutputRef.current.state === 'suspended') {
              await audioCtxOutputRef.current.resume();
          }
          nextPlayTimeRef.current = audioCtxOutputRef.current.currentTime;

          if (!isTextMode) {
              if (!streamRef.current) {
                  streamRef.current = await navigator.mediaDevices.getUserMedia({ audio: true });
              }
              audioCtxInputRef.current = new AudioContextClass({ sampleRate: 16000 });
              if (audioCtxInputRef.current.state === 'suspended') {
                  await audioCtxInputRef.current.resume();
              }
          }

          const wsUrl = 'wss://voice.tonyenglish.vn';
          const ws = new WebSocket(wsUrl);
          wsRef.current = ws;

          ws.onopen = () => {
              setStatus('CONNECTED');
              const voiceName = examiner === 'TONY' ? 'Charon' : 'Kore';
              const sysPrompt = buildSystemPrompt();
              
              ws.send(JSON.stringify({
                  setup: {
                      model: "models/gemini-3.1-flash-live-preview",
                      generationConfig: { 
                          responseModalities: ["AUDIO"], 
                          speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: voiceName } } } 
                      },
                      systemInstruction: { parts: [{ text: sysPrompt }] },
                      inputAudioTranscription: {},
                      outputAudioTranscription: {},
                      // 🚀 TẮT VAD: AI chỉ trả lời khi user THẢ nút "Nhấn nói"
                      // Không tự động cắt ngang khi user ngừng nói giữa chừng
                      realtimeInputConfig: {
                          automaticActivityDetection: { disabled: true }
                      }
                  }
              }));

              if (!isTextMode && audioCtxInputRef.current && streamRef.current) {
                  sourceNodeRef.current = audioCtxInputRef.current.createMediaStreamSource(streamRef.current);
                  processorNodeRef.current = audioCtxInputRef.current.createScriptProcessor(4096, 1, 1);

                  processorNodeRef.current.onaudioprocess = (e) => {
                      if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN && isSetupCompleteRef.current && isMicOpenRef.current) {
                          const inputData = e.inputBuffer.getChannelData(0);
                          const pcm16Buffer = floatTo16BitPCM(inputData);
                          const base64Data = arrayBufferToBase64(pcm16Buffer);
                          
                          wsRef.current.send(JSON.stringify({
                              realtimeInput: {
                                  audio: { 
                                      mimeType: "audio/pcm;rate=16000",
                                      data: base64Data
                                  }
                              }
                          }));
                      }
                  };

                  // Tạo GainNode với gain = 0 để cản tiếng vọng mic ra loa của máy
                  const silenceGain = audioCtxInputRef.current.createGain();
                  silenceGain.gain.setValueAtTime(0, audioCtxInputRef.current.currentTime);

                  sourceNodeRef.current.connect(processorNodeRef.current);
                  processorNodeRef.current.connect(silenceGain);
                  silenceGain.connect(audioCtxInputRef.current.destination);
              }
          };

          ws.onmessage = async (event) => {
              try {
                  let rawData = event.data;
                  if (rawData instanceof Blob) {
                      rawData = await rawData.text();
                  }
                  const msg = JSON.parse(rawData);
                  
                  if (msg.setupComplete) {
                      isSetupCompleteRef.current = true;
                      
                      ws.send(JSON.stringify({ 
                          clientContent: { 
                              turns: [{ role: "user", parts: [{ text: "[HỆ THỐNG]: Học sinh vừa bước vào lớp. Hãy cất tiếng chào, giới thiệu bản thân." }] }], 
                              turnComplete: true 
                          } 
                      }));
                      return;
                  }
                  
                  // ============================================================
                  // 🔍 DEBUG: Log tất cả message keys để xác định format từ server proxy
                  // Anh mở DevTools (F12) → Console để xem log này
                  // ============================================================
                  const msgKeys = Object.keys(msg);
                  console.log("📩 WS MSG keys:", msgKeys.join(', '), msg.serverContent ? '| serverContent keys: ' + Object.keys(msg.serverContent).join(', ') : '');
                  
                  // ============================================================
                  // BƯỚC 1: Tìm inputTranscription ở MỌI VỊ TRÍ CÓ THỂ
                  // Proxy có thể đặt nó ở top-level, trong serverContent, hoặc nơi khác
                  // ============================================================
                  const inputTx = msg.inputTranscription 
                      || msg.serverContent?.inputTranscription 
                      || msg.serverContent?.modelTurn?.inputTranscription
                      || null;
                  
                  if (inputTx) {
                      const userText = (inputTx.text || '').trim();
                      if (userText) {
                          console.log("✅ USER TRANSCRIPT FOUND:", userText, "| partial:", inputTx.partial);
                          geminiUserTranscriptRef.current = userText;
                          setCurrentDraft(userText);
                          
                          setMessages(prev => {
                              const next = [...prev];
                              for (let i = next.length - 1; i >= 0; i--) {
                                  if (next[i].role === 'user') {
                                      let currentText = next[i].text;
                                      if (currentText.startsWith('🎤') || currentText === '(Đã gửi đoạn hội thoại âm thanh)') {
                                          next[i] = { ...next[i], text: userText };
                                      } else {
                                          if (userText.startsWith(currentText)) {
                                              next[i] = { ...next[i], text: userText };
                                          } else if (!currentText.includes(userText)) {
                                              next[i] = { ...next[i], text: currentText + " " + userText };
                                          }
                                      }
                                      break;
                                  }
                              }
                              return next;
                          });
                      }
                  }
                  
                  // ============================================================
                  // BƯỚC 1.5: Tìm outputTranscription (text lời AI nói) ở mọi vị trí
                  // ============================================================
                  const outputTx = msg.outputTranscription 
                      || msg.serverContent?.outputTranscription 
                      || null;
                  
                  if (outputTx) {
                      const aiText = (outputTx.text || '').trim();
                      if (aiText) {
                          console.log("🤖 AI TRANSCRIPT:", aiText);
                          transcriptRef.current += aiText;
                          setLiveTranscript(transcriptRef.current);
                      }
                  }

                  // ============================================================
                  // BƯỚC 2: Xử lý modelTurn (AI đang phản hồi — audio chunks)
                  // ⚠️ BỎ QUA nếu: user đang ghi âm HOẶC vừa ngắt lời (response cũ)
                  // ============================================================
                  if (msg.serverContent?.modelTurn && !isRecordingRef.current && !interruptedRef.current) {
                      const parts = msg.serverContent.modelTurn.parts || [];
                      for (const part of parts) {
                          if (part.text && typeof part.text === 'string') {
                              transcriptRef.current += part.text;
                              setLiveTranscript(transcriptRef.current);
                          }
                          if (!isTextOnlyModeRef.current && part.inlineData?.data) {
                              playAIAudio(part.inlineData.data);
                          }
                      }
                  }

                  // ============================================================
                  // BƯỚC 3: Xử lý turnComplete (AI nói xong — finalize)
                  // ⚠️ Nếu interruptedRef = true → đây là turnComplete của response CŨ
                  // → bỏ qua, không setIsProcessing(false), chờ response MỚI
                  // ============================================================
                  if (msg.serverContent?.turnComplete) {
                      if (interruptedRef.current) {
                          // Response cũ kết thúc → bỏ qua, giữ interruptedRef = true
                          // (sẽ được clear khi user thả nút)
                          console.log('⏭️ Bỏ qua turnComplete cũ (đã ngắt lời)');
                          transcriptRef.current = '';
                          setLiveTranscript('');
                      } else {
                          if (transcriptRef.current) {
                              setMessages(prev => [...prev, { role: 'model', text: transcriptRef.current }]);
                              transcriptRef.current = '';
                              setLiveTranscript('');
                          }
                          setIsProcessing(false);
                          setIsSpeaking(false);
                      }
                  }
              } catch (e) {
                  console.error("Lỗi parse WS message:", e);
              }
          };

          ws.onerror = (err) => {
              console.error("WebSocket error:", err);
          };

          ws.onclose = (event) => {
              console.warn("WebSocket closed. Code:", event.code, "Reason:", event.reason);
              setStatus('IDLE');
          };
      } catch (e) {
          alert("Lỗi: Không thể khởi tạo kết nối.");
          setStatus('IDLE');
      }
  };

  const playAIAudio = (base64Audio: string) => {
      if (!audioCtxOutputRef.current) return;
      const ctx = audioCtxOutputRef.current;
      
      const pcmBuffer = base64ToArrayBuffer(base64Audio);
      const int16Array = new Int16Array(pcmBuffer);
      const float32Array = new Float32Array(int16Array.length);
      for (let i = 0; i < int16Array.length; i++) {
          float32Array[i] = int16Array[i] / 32768.0;
      }
      
      const audioBuffer = ctx.createBuffer(1, float32Array.length, 24000);
      audioBuffer.getChannelData(0).set(float32Array);
      
      const sourceNode = ctx.createBufferSource();
      sourceNode.buffer = audioBuffer;
      sourceNode.connect(ctx.destination);
      
      setIsSpeaking(true);
      const playTime = Math.max(ctx.currentTime, nextPlayTimeRef.current);
      sourceNode.start(playTime);
      nextPlayTimeRef.current = playTime + audioBuffer.duration;
  };

  const stopAIAudio = () => {
      if (audioCtxOutputRef.current && audioCtxOutputRef.current.state !== 'closed') {
          audioCtxOutputRef.current.close();
          const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
          audioCtxOutputRef.current = new AudioContextClass({ sampleRate: 24000 });
          nextPlayTimeRef.current = 0;
      }
      setIsSpeaking(false);
  };

  // =========================================================================================
  // 💬 XỬ LÝ CHAT TEXT TRONG BẢNG ĐEN (ĐIỀU HƯỚNG TỚI NÃO TƯƠNG ỨNG)
  // =========================================================================================
  const sendTextMessage = async () => {
      const text = chatInput.trim();
      if (!text) return;
      
      setChatInput('');
      
      // 🚀 NẾU ĐANG Ở NÃO MẮT THẦN (VISION MODE) -> Gọi lại API Edge Function
      if (isVisionMode) {
          setIsProcessing(true);
          setMessages(prev => [...prev, { role: 'user', text: text }]);
          
          try {
              const finalCourseTitle = courseTitle || sessionStorage.getItem('tony_live_topic') || "Tổng hợp";
              const { data, error } = await supabase.functions.invoke('omni-vision-solver', {
                  body: {
                      imageUrl: activeVisionImage || undefined,
                      content: text,
                      history: messages,
                      courseTitle: finalCourseTitle,
                      prompt: `[KỶ LUẬT CHUYÊN MÔN TUYỆT ĐỐI]
Bạn là một gia sư AI nghiêm khắc chuyên dạy môn "${finalCourseTitle}".
Bạn chỉ được phép giải quyết các câu hỏi và bài tập thuộc phạm vi môn học "${finalCourseTitle}".

QUY TẮC KIỂM TRA MÔN HỌC BẮT BUỘC:
1. Phân tích ảnh và câu hỏi của học sinh để xác định xem đề bài này có thuộc môn "${finalCourseTitle}" hay không.
   - Ví dụ: Nếu môn học là "Giao Tiếp Phản Xạ" hoặc các khóa tiếng Anh giao tiếp, nhưng đề bài lại là Toán học (có các biểu thức đại số, hình học, tích phân, tính toán số học, giải phương trình), Vật lý, Hóa học,... thì đề bài đó KHÔNG thuộc môn học này.
   - Ví dụ: Nếu môn học là "Toán" hoặc "Toán học", nhưng đề bài lại là Tiếng Anh giao tiếp, Tiếng Anh thương mại, Ngữ pháp tiếng Anh,... thì đề bài đó KHÔNG thuộc môn học này.

2. NẾU ĐỀ BÀI KHÔNG LIÊN QUAN TỚI MÔN HỌC "${finalCourseTitle}":
   - Bạn BẮT BUỘC PHẢI TỪ CHỐI GIẢI ĐÁP NGAY LẬP TỨC.
   - Câu trả lời từ chối bắt buộc phải viết: "Thầy/Cô không thể giải bài này vì nó thuộc môn học khác, không nằm trong phạm vi của khóa học ${finalCourseTitle}. Con vui lòng gửi đề bài đúng môn học nhé!"
   - Tuyệt đối KHÔNG giải thích thêm, KHÔNG đưa ra lời khuyên hay đáp án mẫu của đề bài đó.

3. NẾU ĐỀ BÀI LIÊN QUAN TỚI MÔN HỌC "${finalCourseTitle}":
   - Hãy đi thẳng vào giải chi tiết từng bước cho học sinh.
   - TUYỆT ĐỐI KHÔNG giới thiệu dông dài lý do tại sao bạn nhận giải (ví dụ: cấm nói "Vì đề này thuộc môn ${finalCourseTitle} nên thầy giải..."). Trả lời trực tiếp vào câu hỏi.
   - BẮT BUỘC sử dụng ký hiệu LaTeX ($...$ và $$...$$) để viết MỌI công thức toán học, và LUÔN LUÔN IN ĐẬM (**từ khóa**) các từ quan trọng, đáp án, danh từ riêng hoặc kết quả quan trọng để hệ thống tự vẽ bằng phấn vàng nổi bật.`
                  }
              });

              if (error || !data) throw new Error("Lỗi API Vision");

              const resultText = data.result || "Dạ hệ thống vừa gặp trục trặc một xíu, con gõ lại câu hỏi nha.";
              setIsProcessing(false);
              
              // 🚀 Lại kích hoạt hiệu ứng viết phấn
              let currentIndex = 0;
              setLiveTranscript('');
              const typingInterval = setInterval(() => {
                  setLiveTranscript(prev => prev + resultText.charAt(currentIndex));
                  currentIndex++;
                  if (currentIndex >= resultText.length) {
                      clearInterval(typingInterval);
                      setMessages(prev => [...prev, { role: 'model', text: resultText }]);
                      setLiveTranscript('');
                  }
              }, 15);

          } catch (err) {
              setIsProcessing(false);
              setMessages(prev => [...prev, { role: 'model', text: "Hệ thống đang quá tải, con vui lòng thử lại sau nhé!" }]);
          }
          return;
      }

      // 🚀 NẾU LÀ NÃO MỒM BÌNH THƯỜNG -> Gửi qua WebSocket
      if (isSpeaking) stopAIAudio(); 
      setIsProcessing(true);
      setMessages(prev => [...prev, { role: 'user', text: text }]);

      if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
          wsRef.current.send(JSON.stringify({
              clientContent: { turns: [{ role: "user", parts: [{ text: text }] }], turnComplete: true }
          }));
      } else {
          alert("Kết nối đang bị gián đoạn, vui lòng chờ...");
          setIsProcessing(false);
      }
  };

  const handleToggleRecording = () => {
      if (isSpeaking) stopAIAudio(); 
      
      if (isRecording) {
          // ====== DỪNG GHI ÂM ======
          isMicOpenRef.current = false;
          isRecordingRef.current = false;
          interruptedRef.current = false; // ✅ Clear flag → sẵn sàng nhận response MỚI
          setIsRecording(false);
          setIsProcessing(true);
          
          // Xóa auto-timeout nếu có
          if (recordingTimeoutRef.current) {
              clearTimeout(recordingTimeoutRef.current);
              recordingTimeoutRef.current = null;
          }
          
          if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
              setCurrentDraft('');

              // 🚀 GỬI activityEnd → báo hiệu user ngừng nói
              // Sau đó gửi turnComplete để AI bắt đầu phản hồi câu hỏi MỚI
              wsRef.current.send(JSON.stringify({
                  realtimeInput: { activityEnd: {} }
              }));
              wsRef.current.send(JSON.stringify({
                  clientContent: { turnComplete: true }
              }));

              // Đợi 800ms để nhận nốt inputTranscription cuối rồi cập nhật UI cho đẹp
              setTimeout(() => {
                  const finalSpeechText = geminiUserTranscriptRef.current.trim();
                  
                  // Cập nhật tin nhắn placeholder bằng text thật
                  setMessages(prev => {
                      const next = [...prev];
                      for (let i = next.length - 1; i >= 0; i--) {
                          if (next[i].role === 'user') {
                              let currentText = next[i].text;
                              if (currentText.startsWith('🎤') || currentText === '(Đã gửi đoạn hội thoại âm thanh)') {
                                  next[i] = { ...next[i], text: finalSpeechText || "(Đã gửi đoạn hội thoại âm thanh)" };
                              }
                              break;
                          }
                      }
                      return next;
                  });

                  geminiUserTranscriptRef.current = '';
              }, 800);
          } else {
              setIsProcessing(false);
          }
      } else {
          // ====== BẮT ĐẦU GHI ÂM ======
          if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
              setCurrentDraft('');
              geminiUserTranscriptRef.current = '';
              
              // 🚀 Nếu AI đang nói → ngắt lời
              if (isSpeaking) stopAIAudio();
              if (transcriptRef.current) {
                  setMessages(prev => [...prev, { role: 'model', text: transcriptRef.current + ' _(bị ngắt)_' }]);
                  transcriptRef.current = '';
                  setLiveTranscript('');
              }
              setIsProcessing(false);
              
              // 🚀 NGẮT LỜI: CHỈ gửi activityStart để ngắt output của AI
              // ⚠️ KHÔNG gửi turnComplete ở đây — nó sẽ trigger AI trả lời response rác!
              // turnComplete chỉ gửi khi user THẢ NÚT (dừng ghi âm)
              interruptedRef.current = true; // Bật flag → bỏ qua mọi modelTurn/turnComplete cũ
              
              // Thêm placeholder cho lời user
              setMessages(prev => [...prev, { role: 'user', text: '🎤 Đang nghe...' }]);
              
              // 🚀 GỬI activityStart → server tự hiểu user đang interrupt
              wsRef.current.send(JSON.stringify({
                  realtimeInput: { activityStart: {} }
              }));
              
              isMicOpenRef.current = true;
              isRecordingRef.current = true;
              setIsRecording(true);
              
              // ⏱️ AUTO-TIMEOUT 30s: tự động dừng ghi âm nếu user quên thả nút
              // Tránh tốn token audio khi im lặng
              recordingTimeoutRef.current = setTimeout(() => {
                  if (isRecordingRef.current) {
                      console.log('⏱️ Auto-stop recording sau 30s');
                      handleToggleRecording(); // Tự động bấm "Xong"
                  }
              }, 30000);
          } else {
              alert("Kết nối đang bị gián đoạn, vui lòng chờ...");
          }
      }
  };

  const stopCall = () => {
    if (typeof window !== 'undefined') {
        (window as any).tonyPendingImage = null;
    }
    setIsPendingVision(false);
    setActiveVisionImage(null);

    isMicOpenRef.current = false;
    isRecordingRef.current = false;
    setIsTextOnlyMode(false); 
    setIsVisionMode(false); 
    stopAIAudio();
    
    if (processorNodeRef.current) {
        try { processorNodeRef.current.disconnect(); } catch(e) {}
        processorNodeRef.current = null;
    }
    if (sourceNodeRef.current) {
        try { sourceNodeRef.current.disconnect(); } catch(e) {}
        sourceNodeRef.current = null;
    }
    if (streamRef.current) {
        try { streamRef.current.getTracks().forEach(t => t.stop()); } catch(e) {}
        streamRef.current = null;
    }
    if (wsRef.current) {
        try { wsRef.current.close(); } catch(e) {}
        wsRef.current = null;
    }
    if (audioCtxInputRef.current) {
        try { if (audioCtxInputRef.current.state !== 'closed') audioCtxInputRef.current.close(); } catch(e) {}
        audioCtxInputRef.current = null;
    }
    if (audioCtxOutputRef.current) {
        try { if (audioCtxOutputRef.current.state !== 'closed') audioCtxOutputRef.current.close(); } catch(e) {}
        audioCtxOutputRef.current = null;
    }
    
    if (callStartTimeRef.current > 0) {
        const durationSecs = Math.round((Date.now() - callStartTimeRef.current) / 1000);
        callStartTimeRef.current = 0; 
        if (durationSecs > 5) { 
            supabase.auth.getUser().then(({ data: { user } }) => {
                if (user) {
                    supabase.from('activity_logs').insert([{ 
                        user_id: user.id, 
                        action_type: 'call_tutor', 
                        details: { duration: durationSecs, topic: sessionStorage.getItem('tony_live_topic') || "Luyện nói/Hỏi bài AI" } 
                    }]).then();
                }
            });
        }
    }
    setStatus('IDLE'); 
    setIsRecording(false);
    setCurrentDraft('');
    geminiUserTranscriptRef.current = '';
  };

  const handleUserHangUp = () => { 
      stopCall(); 
      sessionStorage.removeItem('tony_live_mode'); 
      sessionStorage.removeItem('tony_tutor_data'); 
      onClose(); 
  };

  // 🚀 TỐI ƯU HÓA MEMOIZE: CHỈ RENDER LẠI DANH SÁCH TIN NHẮN KHI CẦN THIẾT
  // Tránh bị giật lag khi gõ văn bản vào ô input (vì khi gõ input, component re-render nhưng không cần chạy lại ReactMarkdown/KaTeX)
  const renderedBlackboardMessages = useMemo(() => {
      if (messages.length === 0 && !isRecording && !liveTranscript && !currentDraft) {
          return (
              <div className="h-full flex flex-col items-center justify-center text-center opacity-30 italic text-slate-400" style={{fontFamily: 'sans-serif'}}>
                  <span className="text-4xl mb-4 grayscale">{isTextOnlyMode ? '💬' : '🎙️'}</span>
                  <span className="text-[15px] font-medium">Bảng đen trống.<br/>Gõ câu hỏi vào thanh công cụ bên dưới để hỏi bài.</span>
              </div>
          );
      }
      return (
          <>
             {messages.map((m, i) => (
                 <div key={i} className={`mb-6 p-4 rounded-xl ${m.role === 'user' ? 'bg-white/5 border border-white/10 text-sky-200' : 'text-white'}`}>
                     <strong className="text-xs uppercase tracking-widest opacity-50 block mb-2 font-sans">{m.role === 'user' ? 'Câu hỏi của em:' : (examiner === 'TONY' ? 'Thầy Tôn:' : 'Cô Diệp:')}</strong>
                     <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>{m.text}</ReactMarkdown>
                 </div>
             ))}
             
             {liveTranscript && (
                 <div className="mb-6 p-4 rounded-xl text-white">
                     <strong className="text-xs uppercase tracking-widest opacity-50 block mb-2 font-sans">{examiner === 'TONY' ? 'Thầy Tôn:' : 'Cô Diệp:'}</strong>
                     <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>{liveTranscript}</ReactMarkdown>
                 </div>
             )}
             
             {isRecording && (
                 <div className="mb-6 p-4 rounded-xl bg-white/10 border border-[#0ea5e9]/50 text-sky-300 animate-pulse">
                     <strong className="text-xs uppercase tracking-widest opacity-50 block mb-2 font-sans">Đang ghi âm...</strong>
                     {currentDraft.trim() || "🎤 Đang thu âm giọng nói của con..."}
                 </div>
             )}
             
             {isProcessing && !liveTranscript && (
                 <div className="text-amber-300 italic animate-pulse font-sans">
                     Thầy cô đang đọc đề bài và viết bảng...
                 </div>
             )}
             <div ref={messagesEndRef} />
          </>
      );
  }, [messages, liveTranscript, currentDraft, isRecording, isProcessing, isTextOnlyMode, examiner]);

  const renderedTraditionalMessages = useMemo(() => {
      if (messages.length === 0 && !isRecording && !liveTranscript && !currentDraft) {
          return (
              <div className="flex flex-col items-center justify-center h-full opacity-40">
                  <span className="text-3xl mb-2 grayscale">🎙️</span>
                  <span className="italic text-sm font-medium">Lịch sử trống.<br/>Nhấn nút bên dưới để bắt đầu nói.</span>
              </div>
          );
      }
      return (
          <div className="prose prose-slate prose-sm max-w-none font-medium text-slate-700 leading-relaxed space-y-4">
              {messages.map((m, i) => (
                  <div key={i} className={`p-3 rounded-lg ${m.role === 'user' ? 'bg-blue-50 text-blue-900 border border-blue-100' : 'bg-white border border-slate-200'}`}>
                      <strong className="block text-[10px] uppercase tracking-widest opacity-50 mb-1">
                          {m.role === 'user' ? 'Em nói:' : 'Giám khảo:'}
                      </strong>
                      <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>{m.text}</ReactMarkdown>
                  </div>
              ))}
              
              {liveTranscript && (
                  <div className={`p-3 rounded-lg bg-white border border-slate-200`}>
                      <strong className="block text-[10px] uppercase tracking-widest opacity-50 mb-1">Giám khảo:</strong>
                      <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>{liveTranscript}</ReactMarkdown>
                  </div>
              )}
              
              {isRecording && (
                  <div className="p-3 rounded-lg bg-blue-50/50 text-blue-900 border border-blue-100/50 border-dashed animate-pulse">
                      <strong className="block text-[10px] uppercase tracking-widest opacity-50 mb-1">Đang ghi âm...</strong>
                      {currentDraft.trim() || "🎤 Đang thu âm giọng nói của con..."}
                  </div>
              )}
              <div ref={messagesEndRef} />
          </div>
      );
  }, [messages, isRecording, liveTranscript, currentDraft]);

  const currentMode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
  const currentTopic = sessionStorage.getItem('tony_live_topic') || "Bài tập giao tiếp tổng hợp";
  
  const handleYellowButtonClick = () => { 
      if (onOpenAI) {
          onOpenAI(currentMode === 'TUTOR' ? 'tutor' : 'ielts'); 
      }
  };

  // =========================================================================================
  // 🟢 GIAO DIỆN KHI THU NHỎ (MINIMIZED WIDGET ICON)
  // =========================================================================================
  if (viewState === 'MINIMIZED') {
      if (isBlackboardMode) {
          return (
              <button 
                  onClick={handleWidgetClick} 
                  onMouseDown={handleDragStart}
                  onTouchStart={handleDragStart}
                  style={{ transform: `translate3d(${position.x}px, ${position.y}px, 0)` }}
                  className={`fixed bottom-8 right-8 z-[100000] w-14 h-14 rounded-full flex items-center justify-center shadow-[0_10px_30px_rgba(0,0,0,0.5)] border-2 ${isDragging ? '' : 'transition-all duration-300 hover:scale-110 active:scale-95'} ${status === 'CONNECTED' ? (isRecording ? 'bg-red-500 border-red-300 animate-pulse' : (isSpeaking || isProcessing ? 'bg-sky-500 border-sky-300 animate-pulse' : 'bg-emerald-500 border-emerald-300')) : 'bg-indigo-600 border-indigo-400'}`} 
                  title="Mở Bảng Giáo Viên"
              >
                  <span className="text-2xl">{status === 'CONNECTED' ? (isTextOnlyMode ? '💬' : '🎙️') : '👨‍🏫'}</span>
              </button>
          );
      } else {
          return (
              <div 
                  onMouseDown={handleDragStart}
                  onTouchStart={handleDragStart}
                  style={{ transform: `translate3d(${position.x}px, ${position.y}px, 0)` }}
                  className={`fixed bottom-6 right-6 z-[99998] bg-slate-900/95 backdrop-blur-md border border-slate-700 shadow-[0_20px_50px_rgba(0,0,0,0.5)] rounded-[1.5rem] p-4 flex flex-col gap-3 w-[280px] md:w-80 font-sans cursor-move select-none ${isDragging ? '' : 'transition-all duration-300 animate-in slide-in-from-bottom-5'}`}
              >
                 <div className="flex justify-between items-center">
                    <div className="flex items-center gap-2.5 cursor-pointer flex-1 min-w-0" onClick={handleWidgetClick}>
                       <div className={`w-3 h-3 shrink-0 rounded-full ${isRecording ? 'bg-red-500 animate-pulse shadow-[0_0_10px_rgba(239,68,68,0.8)]' : (isSpeaking ? 'bg-sky-500 animate-pulse shadow-[0_0_10px_rgba(14,165,233,0.8)]' : (isProcessing ? 'bg-amber-500 animate-pulse' : 'bg-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.8)]'))}`}></div>
                       <span className="text-white font-semibold text-[13px] truncate">
                           {isRecording ? 'Đang truyền trực tiếp...' : (isProcessing ? 'AI đang phân tích...' : (isSpeaking || liveTranscript ? 'Thầy cô đang nói...' : 'Sẵn sàng...'))}
                       </span>
                    </div>
                    <button onClick={onMaximize} className="text-slate-400 hover:text-white w-8 h-8 flex items-center justify-center bg-slate-800 rounded-full shrink-0 ml-2 border border-slate-600 shadow-sm transition-colors" title="Phóng to">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M4.5 19.5l15-15m0 0H8.25m11.25 0v11.25" /></svg>
                    </button>
                 </div>
                 <div className="flex gap-2 mt-1">
                     {!isTextOnlyMode && !isVisionMode && (
                         <button 
                             onClick={handleToggleRecording} 
                             disabled={isProcessing && !isSpeaking} 
                             className={`flex-1 font-bold py-2 rounded-xl text-[12px] md:text-[13px] transition-all flex items-center justify-center gap-2 disabled:opacity-50 ${isRecording ? 'bg-red-500 hover:bg-red-600 text-white shadow-md shadow-red-900/50' : (isSpeaking ? 'bg-sky-500 hover:bg-sky-600 text-white shadow-md shadow-sky-900/50' : 'bg-[#0ea5e9] hover:bg-sky-500 text-white shadow-md shadow-sky-900/50')}`}
                         >
                            {isRecording ? '⏹️ Xong' : (isSpeaking ? '⏹️ Ngắt lời' : '🎙️ Nhấn nói')}
                         </button>
                     )}
                     <button 
                         onClick={handleUserHangUp} 
                         className="flex-1 bg-slate-800 hover:bg-red-50 text-slate-300 hover:text-white font-bold py-2 rounded-xl text-[12px] md:text-[13px] transition-all flex items-center justify-center gap-2 border border-slate-600 hover:border-red-500"
                     >
                         🛑 Dập máy
                     </button>
                 </div>
              </div>
          );
      }
  }

  // =========================================================================================
  // 🟢 GIAO DIỆN CHÍNH (FULLSCREEN)
  // =========================================================================================
  
  // -------------------------------------------------------------------------
  // 1️⃣ GIAO DIỆN BẢNG ĐEN (KHI MỞ SÁCH PDF HOẶC GIẢI ẢNH SIDEBAR)
  // -------------------------------------------------------------------------
  if (isBlackboardMode) {
      return (
        <>
          <style>{chalkboardStyleTag}</style>
          {status === 'IDLE' && <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[99998]" onClick={onMinimize} />}
          <div 
            className="fixed top-0 right-0 h-[100dvh] w-full bg-[#1a1c21] shadow-[-30px_0_60px_rgba(0,0,0,0.8)] z-[100000] flex flex-row animate-in slide-in-from-right duration-500"
            style={{ width: `${splitWidthVw}vw` }}
          >
            {/* Drag handle */}
            <div 
              className="w-[8px] shrink-0 cursor-col-resize bg-[#2c1808]/80 hover:bg-[#0ea5e9]/60 active:bg-[#0ea5e9] transition-colors relative group hidden md:flex items-center justify-center"
              onMouseDown={(e) => {
                e.preventDefault();
                isSplitDraggingRef.current = true;
                document.body.style.cursor = 'col-resize';
                document.body.style.userSelect = 'none';
                const handleMouseMove = (ev: MouseEvent) => {
                  if (!isSplitDraggingRef.current) return;
                  const vw = ((window.innerWidth - ev.clientX) / window.innerWidth) * 100;
                  const clamped = Math.max(25, Math.min(75, vw));
                  setSplitWidthVw(clamped);
                  window.dispatchEvent(new CustomEvent('tony-board-resize', { detail: clamped }));
                };
                const handleMouseUp = () => {
                  isSplitDraggingRef.current = false;
                  document.body.style.cursor = '';
                  document.body.style.userSelect = '';
                  window.removeEventListener('mousemove', handleMouseMove);
                  window.removeEventListener('mouseup', handleMouseUp);
                };
                window.addEventListener('mousemove', handleMouseMove);
                window.addEventListener('mouseup', handleMouseUp);
              }}
            >
              <div className="w-[3px] h-10 rounded-full bg-white/20 group-hover:bg-white/50 transition-colors"></div>
            </div>
            {/* Main content column */}
            <div className="flex-1 flex flex-col min-w-0">
            
            <div className="h-14 bg-black/40 border-b border-white/5 flex items-center justify-between px-5 shrink-0 backdrop-blur-md">
              <div className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center text-sm border border-white/20">✏️</div>
                  <div className="flex flex-col">
                      <h3 className="font-bold text-[13px] text-slate-300 uppercase tracking-widest leading-none">Tony Blackboard {isVisionMode && "(Vision)"}</h3>
                      {status === 'CONNECTED' && (
                          <span className={`text-[9px] uppercase tracking-widest font-bold mt-1 leading-none transition-colors ${isTextOnlyMode ? 'text-sky-400' : (isRecording ? 'text-red-400' : (isProcessing ? 'text-amber-400' : (isSpeaking || liveTranscript ? 'text-emerald-400' : 'text-slate-500')))}`}>
                              {isTextOnlyMode 
                                  ? (isVisionMode ? "💬 Giải bài tập bằng ảnh" : "💬 Chat văn bản") 
                                  : (isRecording ? "🔴 Đang ghi âm" : (isProcessing ? "🧠 AI đang suy nghĩ..." : (isSpeaking || liveTranscript ? "🟢 Thầy cô đang nói..." : "⏳ Sẵn sàng lượt tiếp")))}
                          </span>
                      )}
                  </div>
              </div>
              <div className="flex items-center gap-1">
                 {status === 'CONNECTED' && (
                     <button onClick={() => {setMessages([]); setCurrentDraft('');}} className="text-[11px] text-slate-400 hover:text-white bg-white/5 hover:bg-white/10 px-3 py-1.5 rounded-lg font-bold uppercase tracking-wide transition-colors mr-2 border border-white/10">Xóa Bảng</button>
                 )}
                 <button onClick={toggleFullscreen} className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/10 text-slate-400 transition-colors">
                     {isFullscreen ? (
                         <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" /></svg>
                     ) : (
                         <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0-4.5L15 15" /></svg>
                     )}
                 </button>
                 <button onClick={onMinimize} className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/10 text-slate-400 transition-colors">
                     <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
                 </button>
              </div>
            </div>
    
            <div className="flex-1 overflow-y-auto p-6 md:p-10 custom-scrollbar flex flex-col relative bg-[url('https://www.transparenttextures.com/patterns/black-paper.png')] pb-32">
              
              {status === 'IDLE' && (
                  isPendingVision ? (
                      <div className="m-auto flex flex-col items-center opacity-70">
                          <div className="w-12 h-12 border-4 border-slate-700 border-t-[#0ea5e9] rounded-full animate-spin mb-4" />
                          <div className="text-slate-400 font-bold tracking-widest text-xs uppercase animate-pulse">Đang chuẩn bị bảng đen...</div>
                      </div>
                  ) : (
                      <div className="m-auto text-center animate-in zoom-in-95 max-w-sm w-full bg-slate-900/80 p-8 rounded-[2rem] border border-slate-700/50 backdrop-blur-md shadow-2xl">
                         <div className="w-20 h-20 bg-gradient-to-tr from-[#0ea5e9] to-indigo-500 rounded-full flex items-center justify-center text-4xl shadow-lg border border-white/20 mx-auto mb-6">👨‍🏫</div>
                         <h3 className="text-xl font-black text-white mb-2 tracking-tight">Học Phần Gia Sư</h3>
                         <p className="text-[13px] text-slate-400 mb-8 font-medium">Vui lòng lựa chọn Thầy/Cô để mở kết nối đàm thoại giảng bài trực tiếp.</p>
                         
                         <div className="flex justify-center gap-4 mb-8">
                            <button onClick={() => { setExaminer('TONY'); sessionStorage.setItem('tony_voice_examiner', 'TONY'); }} className={`flex-1 py-4 rounded-2xl border-2 flex flex-col items-center gap-2 transition-all duration-300 ${examiner === 'TONY' ? 'bg-[#0ea5e9]/20 border-[#0ea5e9] shadow-[0_0_20px_rgba(14,165,233,0.3)]' : 'bg-slate-800 border-slate-700 opacity-70 hover:opacity-100 hover:border-slate-500'}`}>
                                <span className="text-3xl drop-shadow-md">👨‍🏫</span>
                                <span className={`text-[12px] font-black uppercase tracking-widest ${examiner === 'TONY' ? 'text-[#0ea5e9]' : 'text-slate-400'}`}>Thầy Tôn</span>
                            </button>
                            <button onClick={() => { setExaminer('DIEP'); sessionStorage.setItem('tony_voice_examiner', 'DIEP'); }} className={`flex-1 py-4 rounded-2xl border-2 flex flex-col items-center gap-2 transition-all duration-300 ${examiner === 'DIEP' ? 'bg-[#0ea5e9]/20 border-[#0ea5e9] shadow-[0_0_20px_rgba(14,165,233,0.3)]' : 'bg-slate-800 border-slate-700 opacity-70 hover:opacity-100 hover:border-slate-500'}`}>
                                <span className="text-3xl drop-shadow-md">👩‍🏫</span>
                                <span className={`text-[12px] font-black uppercase tracking-widest ${examiner === 'DIEP' ? 'text-[#0ea5e9]' : 'text-slate-400'}`}>Cô Diệp</span>
                            </button>
                         </div>
    
                         <div className="flex flex-col gap-3">
                             <button 
                                 onClick={() => startSession(true)} 
                                 className="w-full bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-600 hover:to-teal-700 text-white font-black py-4 rounded-xl shadow-[0_10px_25px_rgba(16,185,129,0.35)] relative overflow-hidden flex items-center justify-center gap-2 text-sm uppercase tracking-wide active:scale-95 transition-all border border-emerald-400/20"
                             >
                                 💬 Vào Lớp (Chỉ Chat Nhắn Tin)
                                 <span className="absolute top-0 right-0 bg-yellow-400 text-slate-900 text-[8px] font-extrabold px-2.5 py-0.5 rounded-bl-lg uppercase tracking-wider shadow-sm">
                                     Hiệu quả & Tiết kiệm ⭐
                                 </span>
                             </button>
                             <button 
                                 onClick={() => startSession(false)} 
                                 className="w-full bg-slate-800/80 hover:bg-slate-700 text-slate-400 hover:text-slate-300 font-bold py-3 rounded-xl border border-slate-700 transition-all flex items-center justify-center gap-2 text-sm uppercase tracking-wide active:scale-95"
                             >
                                 📞 Vào Lớp (Đàm Thoại Voice)
                             </button>
                         </div>
                      </div>
                  )
              )}
    
              {status === 'CONNECTING' && (
                  <div className="m-auto flex flex-col items-center opacity-70">
                      <div className="w-12 h-12 border-4 border-slate-700 border-t-[#0ea5e9] rounded-full animate-spin mb-4" />
                      <div className="text-slate-400 font-bold tracking-widest text-xs uppercase animate-pulse">Đang mời giáo viên vào lớp...</div>
                  </div>
              )}

              {status === 'CONNECTED' && (
                  <div className="tony-chalkboard-content flex-1 w-full text-left">
                      {renderedBlackboardMessages}
                  </div>
              )}
            </div>
            
            {status === 'CONNECTED' && (
                <div className="absolute bottom-6 left-1/2 -translate-x-1/2 w-full max-w-2xl px-4 z-50">
                    
                    <div className="bg-slate-900/95 backdrop-blur-md border border-slate-700/80 rounded-full p-2 flex items-center justify-between gap-3 shadow-[0_20px_40px_rgba(0,0,0,0.8)]">
                        
                        <div className="flex-1 px-2">
                           <input 
                               type="text"
                               value={chatInput}
                               onChange={(e) => setChatInput(e.target.value)}
                               onKeyDown={(e) => {
                                   if (e.key === 'Enter' && chatInput.trim()) {
                                       sendTextMessage();
                                   }
                               }}
                               placeholder={isRecording ? "Đang thu âm qua mic..." : "💬 Gõ câu hỏi vào đây (Enter để gửi)..."}
                               disabled={isRecording || isProcessing}
                               className="w-full bg-slate-800/80 text-white placeholder-slate-400 text-[16px] md:text-[14px] rounded-full px-4 py-2.5 border border-slate-600 focus:outline-none focus:border-[#0ea5e9] transition-colors"
                           />
                        </div>
                        
                        <div className="flex items-center gap-2 shrink-0 pr-1">
                            {!isTextOnlyMode && !isVisionMode ? (
                                <button 
                                    onClick={handleToggleRecording} 
                                    disabled={isProcessing && !isSpeaking}
                                    className={`w-11 h-11 rounded-full flex items-center justify-center transition-all font-bold disabled:opacity-50 ${isRecording ? 'bg-red-500 text-white shadow-[0_0_15px_rgba(239,68,68,0.5)]' : (isSpeaking ? 'bg-sky-500 text-white shadow-[0_0_15px_rgba(14,165,233,0.5)]' : 'bg-emerald-500 text-white hover:bg-emerald-400')}`}
                                    title={isRecording ? "Kết thúc ghi âm" : (isSpeaking ? "Ngắt lời Thầy/Cô" : "Nhấn để nói")}
                                >
                                    <span className="text-xl">{isRecording ? '⏹️' : (isSpeaking ? '⏹️' : '🎙️')}</span>
                                </button>
                            ) : (
                                <button
                                    onClick={sendTextMessage}
                                    disabled={isProcessing || !chatInput.trim()}
                                    className="w-11 h-11 bg-emerald-500 hover:bg-emerald-400 text-white rounded-full flex items-center justify-center transition-all disabled:opacity-50"
                                    title="Gửi tin nhắn"
                                >
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path d="M3.478 2.404a.75.75 0 00-.926.941l2.432 7.905H13.5a.75.75 0 010 1.5H4.984l-2.432 7.905a.75.75 0 00.926.94 60.519 60.519 0 0018.445-8.986.75.75 0 000-1.218A60.517 60.517 0 003.478 2.404z" /></svg>
                                </button>
                            )}
                            <button 
                                onClick={handleUserHangUp} 
                                className="w-11 h-11 bg-red-500/20 hover:bg-red-500 text-red-500 hover:text-white rounded-full flex items-center justify-center transition-all active:scale-95 border border-red-500/50 hover:border-red-500"
                                title="Rời phòng đàm thoại"
                            >
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
                            </button>
                        </div>
                    </div>
                </div>
            )}
           </div>{/* end main content column */}
          </div>{/* end outer panel */}
        </>
      );
  }

  // -------------------------------------------------------------------------
  // 2️⃣ CHẾ ĐỘ THOẠI TRUYỀN THỐNG (FULLSCREEN KHÔNG CHIA ĐÔI)
  // -------------------------------------------------------------------------
  return (
    <div className="fixed inset-0 z-[9999] flex flex-col items-center justify-center min-h-[100dvh] bg-slate-900/90 backdrop-blur-md text-slate-200 p-4 md:p-8 w-full font-sans animate-in fade-in duration-300">
      
      {onOpenAI && !isChatBubbleVisible && (
          <button 
             onClick={() => {
                 if (onOpenAI) onOpenAI(currentMode === 'TUTOR' ? 'tutor' : 'ielts');
                 // Không minimize → sidebar hiện cùng lúc với cuộc gọi
             }}
             className="absolute top-4 right-4 md:top-6 md:right-6 text-white hover:text-white transition-all flex items-center gap-2 font-bold bg-gradient-to-r from-amber-500 to-orange-500 px-4 py-2.5 md:px-5 md:py-3 rounded-2xl shadow-[0_10px_25px_rgba(245,158,11,0.3)] z-20 hover:scale-105 active:scale-95 hover:shadow-[0_15px_35px_rgba(245,158,11,0.4)]"
             title={currentMode === 'TUTOR' ? 'Mở lại khung Chat Text' : 'Xem gợi ý kịch bản IELTS'}
          >
             <span className="text-xl drop-shadow-sm">💬</span> 
             <span className="hidden sm:inline text-[13px] md:text-[14px] drop-shadow-sm uppercase tracking-wider">
                 {currentMode === 'TUTOR' ? 'Mở khung chat' : 'Kịch bản AI'}
             </span>
          </button>
      )}

      <div className="bg-white p-6 md:p-10 rounded-[2.5rem] shadow-[0_30px_80px_rgba(0,0,0,0.5)] max-w-[600px] w-full text-center relative z-10 max-h-[90dvh] flex flex-col my-auto overflow-hidden ring-1 ring-slate-900/5">
        <button onClick={handleBackClick} className="absolute top-6 left-6 text-slate-500 hover:text-slate-800 bg-slate-100 hover:bg-slate-200 px-4 py-2.5 rounded-xl text-[13px] font-bold transition-all shadow-sm border border-slate-200 z-20 flex items-center gap-2 uppercase tracking-wide">
          {status !== 'IDLE' ? '⬇ Thu nhỏ' : '🚪 Thoát'}
        </button>

        <div className="mb-8 mt-12 md:mt-10 shrink-0">
           <h2 className="text-2xl md:text-[32px] font-black mb-2 text-slate-800 tracking-tight leading-tight">
               {currentMode === 'TUTOR' ? 'Gia Sư Giải Đáp 1-1' : 'Phòng Luyện Nói 1-1'}
           </h2>
           <p className="text-[#0ea5e9] font-bold text-[13px] md:text-[15px] uppercase tracking-widest">
               {currentMode === 'TUTOR' ? 'Phân tích nội dung bài học cùng chuyên gia' : 'Đàm thoại trực tiếp với Giám khảo IELTS'}
           </p>
        </div>

        {status === 'IDLE' && (
          isPendingVision ? (
              <div className="py-16 flex flex-col items-center animate-in zoom-in-95 duration-300 flex-1 justify-center">
                  <div className="relative w-16 h-16 mb-8">
                      <div className="absolute inset-0 border-4 border-[#0ea5e9]/20 rounded-full"></div>
                      <div className="absolute inset-0 border-4 border-[#0ea5e9] border-t-transparent rounded-full animate-spin"></div>
                  </div>
                  <div className="text-slate-500 font-black tracking-widest uppercase text-sm animate-pulse">
                      Đang tải đề bài...
                  </div>
              </div>
          ) : (
              <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 overflow-y-auto custom-scrollbar flex-1 pb-2 px-2">
                 <div className="bg-slate-50 p-5 md:p-6 rounded-2xl border border-slate-200 mb-8 text-left shadow-sm flex flex-col">
                    <span className="block text-[11px] uppercase tracking-widest text-slate-500 font-bold mb-2 shrink-0">Chủ đề đàm thoại:</span>
                    <div className="text-[15px] font-semibold text-slate-800 whitespace-pre-wrap leading-relaxed">
                        {currentMode === 'TUTOR' ? "Chữa bài & Giải đáp thắc mắc chuyên sâu" : `"${currentTopic}"`}
                    </div>
                 </div>
                 
                 <div className="mb-8 shrink-0">
                    <h3 className="text-[12px] font-black text-slate-400 uppercase tracking-widest mb-4">Lựa chọn Giám khảo</h3>
                    <div className="flex justify-center gap-4">
                        <button onClick={() => { setExaminer('TONY'); sessionStorage.setItem('tony_voice_examiner', 'TONY'); }} className={`relative flex-1 py-4 rounded-2xl flex flex-col items-center gap-2 border-2 transition-all duration-300 ${examiner === 'TONY' ? 'bg-[#0ea5e9]/10 border-[#0ea5e9] shadow-sm' : 'bg-white border-slate-200 text-slate-500 hover:border-[#0ea5e9]/50'}`}>
                           <div className="text-4xl drop-shadow-sm mb-1">👨‍🏫</div>
                           <span className={`text-[13px] font-black uppercase tracking-wider ${examiner === 'TONY' ? 'text-[#0ea5e9]' : 'text-slate-500'}`}>Thầy Tôn</span>
                        </button>
                        <button onClick={() => { setExaminer('DIEP'); sessionStorage.setItem('tony_voice_examiner', 'DIEP'); }} className={`relative flex-1 py-4 rounded-2xl flex flex-col items-center gap-2 border-2 transition-all duration-300 ${examiner === 'DIEP' ? 'bg-purple-500/10 border-purple-500 shadow-sm' : 'bg-white border-slate-200 text-slate-500 hover:border-purple-500/50'}`}>
                           <div className="text-4xl drop-shadow-sm mb-1">👩‍🏫</div>
                           <span className={`text-[13px] font-black uppercase tracking-wider ${examiner === 'DIEP' ? 'text-purple-600' : 'text-slate-500'}`}>Cô Diệp</span>
                        </button>
                    </div>
                 </div>
                 
                 <button onClick={() => startSession(false)} className="w-full shrink-0 bg-[#0ea5e9] hover:bg-[#0284c7] text-white font-black py-4 md:py-5 rounded-2xl text-[15px] md:text-[16px] shadow-[0_10px_30px_rgba(14,165,233,0.3)] flex items-center justify-center gap-3 active:scale-95 transition-all uppercase tracking-wide">
                     <span className="text-xl">📞</span> Bắt Đầu Đàm Thoại
                 </button>
              </div>
          )
        )}

        {status === 'CONNECTING' && (
            <div className="py-16 flex flex-col items-center animate-in zoom-in-95 duration-300 flex-1 justify-center">
                <div className="relative w-16 h-16 mb-8">
                    <div className="absolute inset-0 border-4 border-[#0ea5e9]/20 rounded-full"></div>
                    <div className="absolute inset-0 border-4 border-[#0ea5e9] border-t-transparent rounded-full animate-spin"></div>
                </div>
                <div className="text-slate-500 font-black tracking-widest uppercase text-sm animate-pulse">
                    Đang kết nối WebSocket...
                </div>
            </div>
        )}

        {status === 'CONNECTED' && (
          <div className="flex flex-col items-center animate-in zoom-in-95 duration-500 w-full h-full flex-1 overflow-hidden px-2">
            <div className="relative mb-6 shrink-0 mt-4">
                <div className={`absolute inset-0 rounded-full transition-all duration-300 opacity-20 ${isRecording ? 'bg-red-500 scale-[1.5] animate-pulse shadow-[0_0_40px_rgba(239,68,68,0.5)]' : 'bg-[#0ea5e9] scale-100 shadow-[0_0_40px_rgba(14,165,233,0.5)]'}`}></div>
                <div className={`absolute inset-0 rounded-full transition-all duration-500 opacity-10 ${isRecording ? 'bg-red-500 scale-[2] animate-pulse delay-75' : 'bg-[#0ea5e9] scale-[1.3]'}`}></div>
                <div className="w-24 h-24 rounded-full overflow-hidden border-4 border-white shadow-xl relative z-10 bg-slate-100 flex items-center justify-center text-5xl">
                    {examiner === 'TONY' ? '👨‍🏫' : '👩‍🏫'}
                </div>
            </div>
            
            <p className={`shrink-0 font-black mb-6 tracking-widest uppercase text-[10px] md:text-[11px] px-4 py-1.5 rounded-full border shadow-sm transition-colors ${isRecording ? 'bg-red-50 text-red-600 border-red-200' : (isProcessing && !liveTranscript ? "bg-amber-50 text-amber-600 border-amber-200" : (isSpeaking || liveTranscript ? 'bg-sky-50 text-[#0ea5e9] border-sky-200 animate-pulse' : 'bg-slate-50 text-slate-500 border-slate-200'))}`}>
                {isRecording ? "🔴 ĐANG THU ÂM TRỰC TIẾP" : (isProcessing && !liveTranscript ? "🧠 AI ĐANG SUY NGHĨ..." : (isSpeaking || liveTranscript ? "🟢 THẦY CÔ ĐANG NÓI..." : "⏳ SẴN SÀNG LƯỢT TIẾP THEO"))}
            </p>
            
            <div className="bg-slate-50 rounded-2xl p-5 md:p-6 w-full text-left h-32 md:h-48 overflow-y-auto mb-8 border border-slate-200 shadow-inner custom-scrollbar flex-1 min-h-[140px]">
               {renderedTraditionalMessages}
            </div>
            
            <div className="flex flex-col sm:flex-row gap-3 md:gap-4 w-full shrink-0">
                <button 
                    onClick={handleToggleRecording} 
                    disabled={isProcessing && !isSpeaking} 
                    className={`flex-1 font-black py-4 rounded-xl flex items-center justify-center gap-2 transition-all active:scale-95 shadow-md border-2 text-[13px] uppercase tracking-wide disabled:opacity-50 ${isRecording ? 'bg-red-500 text-white border-red-500 shadow-red-500/30' : (isSpeaking ? 'bg-sky-500 text-white border-sky-500' : 'bg-[#0ea5e9] text-white border-[#0ea5e9] hover:bg-sky-500')}`}
                >
                   <span className="text-xl">{isRecording ? '⏹️' : (isSpeaking ? '⏹️' : '🎙️')}</span> 
                   {isRecording ? 'Gửi trả lời' : (isSpeaking ? 'Ngắt lời' : 'Nhấn nói')}
                </button>
                <button 
                    onClick={handleUserHangUp} 
                    className="flex-1 bg-white hover:bg-red-50 text-red-500 font-black py-4 rounded-xl flex items-center justify-center gap-2 active:scale-95 transition-all border-2 border-red-200 hover:border-red-500 text-[13px] uppercase tracking-wide shadow-sm"
                >
                    🚪 Rời phòng
                </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}