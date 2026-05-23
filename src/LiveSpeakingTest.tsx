import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import React, { useState, useRef, useEffect } from 'react';

// =========================================================================================
// 🚀 CSS: STYLE CHỮ PHẤN VIẾT TAY CHO CHẾ ĐỘ BẢNG ĐEN (ĐÃ CẬP NHẬT PHẤN VÀNG)
// =========================================================================================
const chalkboardStyleTag = `
  @import url('https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&display=swap');
  
  .tony-chalkboard-content, 
  .tony-chalkboard-content p,
  .tony-chalkboard-content span,
  .tony-chalkboard-content div,
  .tony-chalkboard-content li {
    font-family: 'Kalam', cursive !important;
    color: #f8fafc !important; 
    font-size: 1.5rem !important;
    line-height: 1.8 !important;
    letter-spacing: 0.04em !important;
    text-shadow: 0px 1px 3px rgba(0,0,0,0.8) !important;
  }
  
  .tony-chalkboard-content p { 
    margin-bottom: 1.2rem !important; 
  }
  
  /* Phấn vàng nổi bật cho đáp án in đậm khi AI viết dấu ** */
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
    margin-top: 1.8rem !important; 
    margin-bottom: 0.6rem !important; 
  }
  
  /* Phấn vàng nổi bật rực rỡ cho mọi công thức Toán học KaTeX */
  .tony-chalkboard-content .katex { 
    font-family: KaTeX_Math, 'Times New Roman', serif !important; 
    font-size: 1.5rem !important; 
    color: #fef08a !important; 
  }
`;

// === HÀM HỖ TRỢ ĐỔI FORMAT ÂM THANH ===
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
// COMPONENT PHÒNG LIVE TỐI THƯỢNG (HỖ TRỢ 2 NHÂN CÁCH: BÌNH THƯỜNG & BẢNG ĐEN)
// =========================================================================================
export default function LiveSpeakingTest({ 
    viewState, 
    onMinimize, 
    onMaximize, 
    onClose, 
    onOpenAI 
}: { 
    viewState: 'FULLSCREEN' | 'MINIMIZED', 
    onMinimize: () => void, 
    onMaximize: () => void, 
    onClose: () => void, 
    onOpenAI?: (passedMode?: string) => void 
}) {
  const [status, setStatus] = useState<'IDLE' | 'CONNECTING' | 'CONNECTED'>('IDLE');
  const [transcript, setTranscript] = useState<string>('');
  const [isMicSending, setIsMicSending] = useState(false);
  const [examiner, setExaminer] = useState<'TONY' | 'DIEP'>('TONY');
  
  // 🚀 ĐỘC CHIÊU: Tự nhận diện xem có đang mở PDF không để đổi giao diện
  const [isBlackboardMode, setIsBlackboardMode] = useState(false);
  
  // 🚀 TÍNH NĂNG MỚI: THEO DÕI TRẠNG THÁI CỦA BONG BÓNG CHAT
  const [isChatBubbleVisible, setIsChatBubbleVisible] = useState(false);

  // 🚀 STATE MỚI: QUẢN LÝ TOÀN MÀN HÌNH CHO CẢ TRANG
  const [isFullscreen, setIsFullscreen] = useState(false);

  useEffect(() => {
    const onFullscreenChange = () => setIsFullscreen(!!document.fullscreenElement);
    document.addEventListener('fullscreenchange', onFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', onFullscreenChange);
  }, []);

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
        // Phóng to toàn bộ thẻ <html>, che cả thanh trình duyệt
        document.documentElement.requestFullscreen().catch(err => console.log(err));
    } else {
        document.exitFullscreen();
    }
  };

  const [isMuted, setIsMuted] = useState(false);
  const isMutedRef = useRef(false); 
  
  const wsRef = useRef<WebSocket | null>(null);
  const audioCtxInputRef = useRef<AudioContext | null>(null);
  const audioCtxOutputRef = useRef<AudioContext | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const nextPlayTimeRef = useRef<number>(0);
  const isSetupCompleteRef = useRef<boolean>(false);

  const sourceNodeRef = useRef<MediaStreamAudioSourceNode | null>(null);
  const processorNodeRef = useRef<ScriptProcessorNode | null>(null);
  const gainNodeRef = useRef<GainNode | null>(null);

  const transcriptRef = useRef<string>(''); 
  const isIntendedCloseRef = useRef<boolean>(false); 

  const reconnectTimeoutRef = useRef<any>(null);
  const pendingCallTimeoutRef = useRef<any>(null);

  const statusRef = useRef(status);
  
  useEffect(() => { 
      statusRef.current = status; 
  }, [status]);

  const startCallRef = useRef<(isReconnect?: boolean) => void>(() => {});
  const stopCallRef = useRef<() => void>(() => {});

  useEffect(() => { 
      startCallRef.current = startCall; 
      stopCallRef.current = stopCall;
  }, [examiner]);

  // LẮNG NGHE SỰ KIỆN BONG BÓNG CHAT TỪ AITutorSidebar
  useEffect(() => {
      const handleBubbleState = (e: any) => {
          setIsChatBubbleVisible(e.detail);
      };
      
      window.addEventListener('tony-chat-bubble-state', handleBubbleState);
      
      // Khởi tạo trạng thái lần đầu (phòng trường hợp event bị bỏ lỡ)
      const bubbleExists = !!document.querySelector('button[title="Mở lại khung Chat AI"]');
      setIsChatBubbleVisible(bubbleExists);
      
      return () => {
          window.removeEventListener('tony-chat-bubble-state', handleBubbleState);
      };
  }, []);

  // TỰ ĐỘNG NHẬN DIỆN MÔI TRƯỜNG & BÁO CHO PDF DÃN MÀN HÌNH
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
      
      // Cleanup khi dập máy/tắt popup
      return () => {
          window.dispatchEvent(new CustomEvent('tony-teacher-board-state', { detail: false }));
      };
  }, [viewState]);

  // KIỂM TRA LỆNH GỌI TỰ ĐỘNG NGAY KHI VỪA MỞ CỬA SỔ LÊN
  useEffect(() => {
      const autoStart = sessionStorage.getItem('tony_auto_start') === 'true';
      
      if (autoStart) {
          sessionStorage.removeItem('tony_auto_start');
          
          const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
          if (isMobile) {
              return; 
          }
          
          // 🚀 ĐÃ SỬA: Chỉ mở bự lên sảnh chờ để đợi học sinh thong thả chọn người, KHÔNG auto call nữa!
          onMaximize();
      }
  }, [onMaximize]);

  // RADAR THÔNG MINH BẮT TÍN HIỆU ĐIỀU HƯỚNG TỪ NGOÀI VÀO
  useEffect(() => {
    const handleNavigationEvent = (e: any) => {
        if (e.detail === 'live-test') {
            onMaximize(); 
            sessionStorage.removeItem('tony_auto_start');
        }
    };
    
    window.addEventListener('tony-navigate', handleNavigationEvent);
    
    return () => {
        window.removeEventListener('tony-navigate', handleNavigationEvent);
    };
  }, [onMaximize]);

  // =========================================================================================
  // 👁️ MẮT THẦN: GÓI CHẶT ẢNH VÀO TIN NHẮN ĐỂ TRỊ BỆNH ẢO GIÁC LẬT TRANG SÁCH
  // =========================================================================================
  useEffect(() => {
    const handleNewPageImage = (e: any) => {
        const base64ImageWithPrefix = e.detail; 
        const base64Data = base64ImageWithPrefix.split(',')[1];

        if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
            
            wsRef.current.send(JSON.stringify({
                clientContent: {
                    turns: [{
                        role: "user",
                        parts: [
                            {
                                inlineData: {
                                    mimeType: "image/jpeg",
                                    data: base64Data
                                }
                            },
                            { 
                                text: "[HỆ THỐNG ĐIỀU HƯỚNG]: Học sinh vừa lật sách. TÔI ĐÃ ĐÍNH KÈM BỨC ẢNH CỦA TRANG SÁCH VÀO TIN NHẮN NÀY. Bạn BẮT BUỘC phải 'mở mắt' ra đọc kỹ biểu đồ, công thức, văn bản trong bức ảnh này. TUYỆT ĐỐI KHÔNG BỊA CHUYỆN (Hallucinate) NẾU CHƯA NHÌN RÕ. Hãy giữ im lặng và đợi học sinh cất tiếng hỏi." 
                            }
                        ]
                    }],
                    turnComplete: true
                }
            }));
        }
    };

    window.addEventListener('tony-send-page-image', handleNewPageImage);
    return () => window.removeEventListener('tony-send-page-image', handleNewPageImage);
  }, []);

  const toggleMute = () => {
      isMutedRef.current = !isMutedRef.current;
      setIsMuted(isMutedRef.current);
  };

  const handleClearBoard = () => {
      setTranscript('');
      transcriptRef.current = '';
  };

  const handleBackClick = () => {
    if (status !== 'IDLE') {
        onMinimize();
    } else {
        sessionStorage.removeItem('tony_live_mode');
        sessionStorage.removeItem('tony_tutor_data');
        onClose();
    }
  };

  const startCall = async (isReconnect = false) => {
    try {
      setStatus('CONNECTING');
      isSetupCompleteRef.current = false;
      setIsMicSending(false);
      
      if (!isReconnect) { 
          setTranscript(''); 
          transcriptRef.current = ''; 
      }
      
      isIntendedCloseRef.current = false;

      if (audioCtxInputRef.current && audioCtxInputRef.current.state !== 'closed') {
          try { audioCtxInputRef.current.close(); } catch(e) {}
      }
      if (audioCtxOutputRef.current && audioCtxOutputRef.current.state !== 'closed') {
          try { audioCtxOutputRef.current.close(); } catch(e) {}
      }

      const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
      audioCtxInputRef.current = new AudioContextClass({ sampleRate: 16000 });
      audioCtxOutputRef.current = new AudioContextClass({ sampleRate: 24000 });
      
      if (audioCtxInputRef.current.state === 'suspended') {
          await audioCtxInputRef.current.resume();
      }
      if (audioCtxOutputRef.current.state === 'suspended') {
          await audioCtxOutputRef.current.resume();
      }
      
      if (!streamRef.current) {
          streamRef.current = await navigator.mediaDevices.getUserMedia({ audio: true });
      }
      
      nextPlayTimeRef.current = audioCtxOutputRef.current.currentTime;

      const wsUrl = 'wss://voice.tonyenglish.vn';
      const ws = new WebSocket(wsUrl);
      wsRef.current = ws;

      ws.onopen = () => {
        setStatus('CONNECTED');
        
        // 🚀 AUTO-MINIMIZE: Nhanh gọn lẹ, nếu ở giao diện thường, kết nối xong tự cụp xuống luôn!
        if (!isBlackboardMode) {
            onMinimize();
        }

        const voiceName = examiner === 'TONY' ? 'Charon' : 'Kore';
        const teacherName = examiner === 'TONY' ? 'thầy Tôn' : 'cô Diệp';

        const mode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
        const tutorDataRaw = sessionStorage.getItem('tony_tutor_data');
        const tutorData = tutorDataRaw ? JSON.parse(tutorDataRaw) : null;
        const currentTopic = sessionStorage.getItem('tony_live_topic') || "Bài tập giao tiếp tổng hợp";

        // ====================================================================
        // THUẬT TOÁN BƠM BÍ KÍP (TEXT + ẢNH) VÀO NÃO AI KHI MỞ KẾT NỐI
        // ====================================================================
        const hiddenContextRaw = sessionStorage.getItem('tony_lecture_context') || '';
        const imgRegex = /\[IMAGE_ANSWER:\s*(https?:\/\/[^\]]+)\]/g;
        let match;
        const answerImageUrls: string[] = [];
        while ((match = imgRegex.exec(hiddenContextRaw)) !== null) {
            answerImageUrls.push(match[1]);
        }
        
        const cleanTextContext = hiddenContextRaw.replace(imgRegex, '[CÓ BỨC ẢNH ĐÁP ÁN ĐÍNH KÈM]').trim();
        const contextInstruction = cleanTextContext 
            ? `\n\n[TÀI LIỆU/ĐÁP ÁN THAM KHẢO DÀNH RIÊNG CHO BẠN]:\n"""\n${cleanTextContext}\n"""\n(Bạn đã biết toàn bộ thông tin này, kết hợp với các BỨC ẢNH ĐÁP ÁN gửi kèm để giải thích cho học sinh. TUYỆT ĐỐI KHÔNG tiết lộ với học sinh là bạn đang đọc từ tài liệu ẩn).` 
            : '';

        let systemPrompt = "";
        
       // 🚀 KỶ LUẬT SƯ PHẠM VÀ MẬT LỆNH ÉP AI GIAO TIẾP RA PHẤN VÀNG
       const promptKienNhan = isBlackboardMode 
       ? `[KỶ LUẬT THÉP VÀ CÁCH TRÌNH BÀY BẢNG]: 
         1. BẠN BẮT BUỘC PHẢI PHÁT ÂM VÀ SỬ DỤNG TỪ VỰNG CHUẨN GIỌNG MIỀN BẮC (HÀ NỘI). TUYỆT ĐỐI KHÔNG ĐƯỢC DÙNG THANH ĐIỆU HOẶC PHƯƠNG NGỮ MIỀN NAM.
         2. Người dùng đang luyện học nên tốc độ sẽ chậm, hay ngập ngừng. BẠN PHẢI TUYỆT ĐỐI KIÊN NHẪN. Không cướp lời. Đợi hết khoảng lặng mới được phản hồi. Tốc độ nói của bạn phải chậm rãi.
         3. [QUY TẮC VIẾT BẢNG PHẤN VÀNG]: Phản hồi văn bản của bạn đang được CHÉP LÊN BẢNG ĐEN dạng chữ viết tay. Hãy giải ngắn gọn từng bước, dùng gạch đầu dòng. BẮT BUỘC dùng ký hiệu LaTeX ($...$ cho inline, $$...$$ cho block) để viết MỌI công thức toán học, và IN ĐẬM (**đáp án**) các kết quả quan trọng để hệ thống tự vẽ bằng phấn vàng nổi bật.`
       : `[KỶ LUẬT THÉP]: 
         1. BẠN BẮT BUỘC PHẢI PHÁT ÂM VÀ SỬ DỤNG TỪ VỰNG CHUẨN GIỌNG MIỀN BẮC (HÀ NỘI). TUYỆT ĐỐI KHÔNG ĐƯỢC DÙNG THANH ĐIỆU HOẶC PHƯƠNG NGỮ MIỀN NAM.
         2. Người dùng đang luyện nói tiếng Anh nên tốc độ sẽ chậm, hay ngập ngừng. BẠN PHẢI TUYỆT ĐỐI KIÊN NHẪN. Không cướp lời. Đợi hết khoảng lặng mới được phản hồi. Tốc độ nói của bạn phải chậm rãi.
         3. [QUY TẮC TOÁN HỌC]: Bạn phải luôn bao bọc các công thức toán học bằng ký hiệu LaTeX tiêu chuẩn ($...$ và $$...$$) để màn hình học sinh tự động vẽ hình ảnh công thức toán học sạch đẹp.`;
        
        if (mode === 'TUTOR' && tutorData) {
            if (isReconnect && transcriptRef.current) {
                systemPrompt = `Bạn là ${teacherName}, người Hà Nội. TÍNH CÁCH: Thanh lịch, chuẩn mực. 
                NGÔN NGỮ: Văn phong Hà Nội chuẩn. Tiếng Anh chuẩn giọng British English.
                BỐI CẢNH BÀI HỌC: ${tutorData.transcript}.
                
                [LỆNH KHẨN CẤP TỪ HỆ THỐNG]: Cuộc trò chuyện vừa bị gián đoạn do lỗi mạng. Đây là lịch sử những gì BẠN ĐÃ NÓI nãy giờ: "${transcriptRef.current}".
                NHIỆM VỤ HIỆN TẠI: Tiếp tục cuộc đàm thoại ngay lập tức. TUYỆT ĐỐI KHÔNG chào hỏi lại.
                
                ${promptKienNhan} ${contextInstruction}`;
            } else {
                systemPrompt = `Bạn là ${teacherName}, người Hà Nội. TÍNH CÁCH: Thanh lịch, chuẩn mực. 
                NGÔN NGỮ: Văn phong Hà Nội chuẩn. Tiếng Anh chuẩn giọng British English.
                BỐI CẢNH: ${tutorData.transcript}. 
                NHIỆM VỤ: ${tutorData.feedback}. 
                
                [QUY TẮC GIAO TIẾP NGHIÊM NGẶT]: Bạn CHỈ ĐƯỢC phép chào hỏi 1 LẦN DUY NHẤT ở câu nói đầu tiên.
                
                ${promptKienNhan} ${contextInstruction}`;
            }
        } else {
            if (isReconnect && transcriptRef.current) {
                systemPrompt = `Bạn là giám khảo IELTS tên ${teacherName}, người Hà Nội. Giao tiếp văn phong chuẩn miền Bắc. Phát âm tiếng Anh giọng British English.
                BỐI CẢNH: Hãy đóng vai giám khảo và yêu cầu tôi nói về chủ đề: "${currentTopic}".
                
                [LỆNH KHẨN CẤP]: Mạng vừa rớt. Đây là lịch sử bạn đã nói: "${transcriptRef.current}". 
                TUYỆT ĐỐI KHÔNG chào lại, KHÔNG giới thiệu lại. Hãy tiếp tục phần thi.
                
                ${promptKienNhan} ${contextInstruction}`;
            } else {
                systemPrompt = `Bạn là giám khảo IELTS tên ${teacherName}, người Hà Nội. Giao tiếp văn phong chuẩn miền Bắc. Phát âm tiếng Anh giọng British English.
                BỐI CẢNH: Hãy đóng vai giám khảo và yêu cầu tôi nói về chủ đề: "${currentTopic}".
                
                [QUY TẮC]: Chỉ chào hỏi 1 lần duy nhất ở câu đầu tiên.
                
                ${promptKienNhan} ${contextInstruction}`;
            }
        }

        ws.send(JSON.stringify({
          setup: {
            model: "models/gemini-3.1-flash-live-preview",
            generationConfig: { 
                responseModalities: ["AUDIO"], 
                speechConfig: { 
                    voiceConfig: { 
                        prebuiltVoiceConfig: { voiceName: voiceName } 
                    } 
                } 
            },
            systemInstruction: { 
                parts: [{ text: systemPrompt }] 
            }
          }
        }));

        const fetchImageAsBase64 = async (url: string) => {
            try {
                const response = await fetch(url);
                const blob = await response.blob();
                return new Promise<string>((resolve) => {
                    const reader = new FileReader();
                    reader.onloadend = () => resolve((reader.result as string).split(',')[1]);
                    reader.readAsDataURL(blob);
                });
            } catch (e) { 
                return null; 
            }
        };
        (window as any).tonyPendingAnswerImages = answerImageUrls;
        (window as any).tonyFetchImageAsBase64 = fetchImageAsBase64;

        sourceNodeRef.current = audioCtxInputRef.current!.createMediaStreamSource(streamRef.current!);
        processorNodeRef.current = audioCtxInputRef.current!.createScriptProcessor(4096, 1, 1);
        gainNodeRef.current = audioCtxInputRef.current!.createGain();
        gainNodeRef.current.gain.value = 0;

        processorNodeRef.current.onaudioprocess = (e) => {
            if (ws !== wsRef.current || ws.readyState !== WebSocket.OPEN) {
                return;
            }
              
            if (isSetupCompleteRef.current) {
              const inputData = e.inputBuffer.getChannelData(0);
              
              // =========================================================================
              // 🧠 THUẬT TOÁN KIỂM TRA LỌC IM LẶNG VAD (RMS ENERGY CHECKER)
              // =========================================================================
              let sum = 0;
              for (let i = 0; i < inputData.length; i++) {
                sum += inputData[i] * inputData[i];
              }
              const rms = Math.sqrt(sum / inputData.length);
              
              // Ngưỡng im lặng vàng chống cháy token: 0.008
              if (!isMutedRef.current && rms <= 0.008) {
                  setIsMicSending(false);
                  return; // Chặn đứng, không gửi block này lên server Google nữa
              }
  
              const dataToSend = isMutedRef.current ? new Float32Array(inputData.length) : inputData;
              const pcm16Buffer = floatTo16BitPCM(dataToSend);
              
              ws.send(JSON.stringify({ 
                  realtimeInput: { 
                      audio: { 
                          mimeType: "audio/pcm;rate=16000", 
                          data: arrayBufferToBase64(pcm16Buffer) 
                      } 
                  } 
              }));
              
              if (!isMutedRef.current) {
                  setIsMicSending(true);
              } else {
                  setIsMicSending(false);
              }
            }
          };

        sourceNodeRef.current.connect(processorNodeRef.current);
        processorNodeRef.current.connect(gainNodeRef.current);
        gainNodeRef.current.connect(audioCtxInputRef.current!.destination);
      };

      ws.onmessage = async (event) => {
        if (ws !== wsRef.current) return;

        try {
          let rawData = event.data;
          if (rawData instanceof Blob) {
              rawData = await rawData.text();
          }
          const msg = JSON.parse(rawData);
          
          if (msg.setupComplete) {
             isSetupCompleteRef.current = true;
             ws.send(JSON.stringify({ 
                 realtimeInput: { 
                     text: isReconnect ? "[HỆ THỐNG]: Đã kết nối lại. Bỏ qua lời chào, tiếp tục ngay." : "Hello, I am ready." 
                 } 
             }));

             const pendingImages = (window as any).tonyPendingAnswerImages || [];
             if (pendingImages.length > 0) {
                 const imageParts: any[] = [{ 
                     text: "[HỆ THỐNG GỬI MẬT THƯ]: Dưới đây là các hình ảnh chứa LỜI GIẢI / ĐÁP ÁN của bài học này. Hãy GHI NHỚ chúng để đối chiếu khi học sinh hỏi bài." 
                 }];
                 
                 for (const url of pendingImages) {
                     const b64 = await (window as any).tonyFetchImageAsBase64(url);
                     if (b64) {
                         imageParts.push({ 
                             inlineData: { mimeType: "image/jpeg", data: b64 } 
                         });
                     }
                 }
                 
                 ws.send(JSON.stringify({
                     clientContent: { 
                         turns: [{ role: "user", parts: imageParts }], 
                         turnComplete: true 
                     }
                 }));
             }
             return;
          }
          
          // =========================================================================================
          // 🚀 THUẬT TOÁN "MÁY HÚT BỤI" TÌM CHỮ TRONG MỌI CẤU TRÚC JSON PHỨC TẠP
          // =========================================================================================
          if (msg.serverContent || msg.response) {
             const extractText = (obj: any): string => {
                 let res = "";
                 if (!obj) return res;
                 if (Array.isArray(obj)) {
                     obj.forEach(item => res += extractText(item));
                 } else if (typeof obj === 'object') {
                     if (obj.type === 'response.audio.delta' || obj.type === 'audio') return res;
                     for (const [key, value] of Object.entries(obj)) {
                         if ((key === 'text' || key === 'transcript' || (key === 'delta' && obj.type === 'response.audio_transcript.delta')) && typeof value === 'string') {
                             res += value;
                         } else if (key !== 'inlineData' && key !== 'audio' && key !== 'mediaChunks' && key !== 'pcm') {
                             res += extractText(value);
                         }
                     }
                 }
                 return res;
             };
             
             const foundText = extractText(msg);
             if (foundText) {
                 transcriptRef.current += foundText;
                 setTranscript(transcriptRef.current);
             }

             if (msg.serverContent?.modelTurn?.parts) {
                 for (let part of msg.serverContent.modelTurn.parts) {
                     if (part.inlineData?.data) {
                         playAIAudio(part.inlineData.data);
                     }
                 }
             }
          }
        } catch (error) {
            console.error("Lỗi parse WS message:", error);
        }
      };

      ws.onclose = () => { 
          if (!isIntendedCloseRef.current) {
              if (reconnectTimeoutRef.current) {
                  clearTimeout(reconnectTimeoutRef.current);
              }
              reconnectTimeoutRef.current = setTimeout(() => {
                  if (!isIntendedCloseRef.current) {
                      startCall(true);
                  }
              }, 1000);
          }
      };
      
    } catch (error) { 
        setStatus('IDLE'); 
    }
  };

  const playAIAudio = (base64Audio: string) => {
    if (!audioCtxOutputRef.current) return;
    
    const ctx = audioCtxOutputRef.current;
    if (ctx.state === 'suspended') {
        ctx.resume();
    }
    
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
    
    const playTime = Math.max(ctx.currentTime, nextPlayTimeRef.current);
    sourceNode.start(playTime);
    nextPlayTimeRef.current = playTime + audioBuffer.duration;
  };

  const stopCall = () => {
    isIntendedCloseRef.current = true;
    
    if (reconnectTimeoutRef.current) {
        clearTimeout(reconnectTimeoutRef.current);
    }
    if (pendingCallTimeoutRef.current) {
        clearTimeout(pendingCallTimeoutRef.current);
    }

    try { 
        if (wsRef.current) wsRef.current.close(); 
    } catch(e) {}
    
    try { 
        if (streamRef.current) streamRef.current.getTracks().forEach(t => t.stop()); 
    } catch(e) {}
    
    try { 
        if (sourceNodeRef.current) sourceNodeRef.current.disconnect(); 
    } catch(e) {}
    
    try { 
        if (processorNodeRef.current) processorNodeRef.current.disconnect(); 
    } catch(e) {}
    
    try { 
        if (gainNodeRef.current) gainNodeRef.current.disconnect(); 
    } catch(e) {}
    
    try { 
        if (audioCtxInputRef.current && audioCtxInputRef.current.state !== 'closed') {
            audioCtxInputRef.current.close(); 
        }
    } catch(e) {}
    
    try { 
        if (audioCtxOutputRef.current && audioCtxOutputRef.current.state !== 'closed') {
            audioCtxOutputRef.current.close(); 
        }
    } catch(e) {}

    wsRef.current = null;
    streamRef.current = null;
    sourceNodeRef.current = null;
    processorNodeRef.current = null;
    gainNodeRef.current = null;
    audioCtxInputRef.current = null;
    audioCtxOutputRef.current = null;

    setStatus('IDLE');
    isSetupCompleteRef.current = false;
    setIsMicSending(false);
  };

  const handleUserHangUp = () => { 
      stopCall(); 
      sessionStorage.removeItem('tony_live_mode');
      sessionStorage.removeItem('tony_tutor_data');
      onClose(); 
  };


  // =========================================================================================
  // 🟢 GIAO DIỆN KHI THU NHỎ (MINIMIZED WIDGET ICON) - CHUNG CHO CẢ 2 CHẾ ĐỘ
  // =========================================================================================
  if (viewState === 'MINIMIZED') {
      if (isBlackboardMode) {
          // Giao diện bong bóng nhỏ ở góc phải (Dành cho bảng đen)
          return (
              <button 
                  onClick={onMaximize}
                  className={`fixed bottom-8 right-8 z-[100000] w-14 h-14 rounded-full flex items-center justify-center shadow-[0_10px_25px_rgba(0,0,0,0.5)] transition-all hover:scale-110 active:scale-95 border-2 ${status === 'CONNECTED' ? (isMicSending ? 'bg-red-500 border-red-300 animate-pulse' : 'bg-emerald-500 border-emerald-300') : 'bg-indigo-600 border-indigo-400'}`}
                  title="Mở Bảng Giáo Viên"
              >
                  <span className="text-2xl">{status === 'CONNECTED' ? '🎙️' : '👨‍🏫'}</span>
              </button>
          );
      } else {
          // Giao diện Widget chữ nhật như cũ (Dành cho chế độ bình thường)
          return (
              <div className="fixed bottom-6 right-6 z-[99998] bg-[#0f172a] border border-slate-700 shadow-[0_20px_50px_rgba(0,0,0,0.5)] rounded-2xl p-4 flex flex-col gap-3 w-[260px] md:w-72 animate-in slide-in-from-bottom-5 font-sans">
                 <div className="flex justify-between items-center">
                    <div className="flex items-center gap-2 cursor-pointer flex-1 min-w-0" onClick={onMaximize}>
                       <div className={`w-3 h-3 shrink-0 rounded-full ${isMicSending ? 'bg-red-500 animate-pulse shadow-[0_0_8px_rgba(239,68,68,0.8)]' : 'bg-emerald-500 shadow-[0_0_8px_rgba(16,185,129,0.8)]'}`}></div>
                       <span className="text-white font-bold text-[12px] md:text-[13px] truncate">
                           {isMuted ? 'Đã tắt Mic' : (isMicSending ? 'Đang nghe...' : 'Gia sư đang đợi...')}
                       </span>
                    </div>
                    <button onClick={onMaximize} className="text-slate-400 hover:text-white p-1.5 bg-slate-800 rounded-lg shrink-0 ml-2 border border-slate-600 shadow-sm" title="Phóng to">
                        <svg xmlns="http://www.w3.org/2000/svg" className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" /></svg>
                    </button>
                 </div>
                 <div className="flex gap-2 mt-1">
                     <button 
                        onClick={toggleMute} 
                        className={`flex-1 font-bold py-2 rounded-xl text-[12px] md:text-[13px] transition-all shadow-md flex items-center justify-center gap-2 ${isMuted ? 'bg-amber-600 hover:bg-amber-500 text-white' : 'bg-slate-700 hover:bg-slate-600 text-white border border-slate-600'}`}
                     >
                        {isMuted ? '🔇 Đã Tắt Mic' : '🎙️ Tắt Mic'}
                     </button>
                     <button 
                         onClick={handleUserHangUp} 
                         className="flex-1 bg-red-600/90 hover:bg-red-500 text-white font-bold py-2 rounded-xl text-[12px] md:text-[13px] transition-all shadow-md flex items-center justify-center gap-2 border border-red-500"
                     >
                        🛑 Dập máy
                     </button>
                 </div>
              </div>
          );
      }
  }

  // =========================================================================================
  // 🟢 GIAO DIỆN CHÍNH (ĐƯỢC CHIA LÀM 2 THEO ĐÚNG YÊU CẦU)
  // =========================================================================================
  const currentMode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
  const currentTopic = sessionStorage.getItem('tony_live_topic') || "Bài tập giao tiếp tổng hợp";
  
  const handleYellowButtonClick = () => {
      if (onOpenAI) {
          onOpenAI(currentMode === 'TUTOR' ? 'tutor' : 'ielts');
      }
  };

  // -------------------------------------------------------------------------
  // 1️⃣ NHÂN CÁCH 1: BẢNG ĐEN PHẤN TRẮNG (SPLIT SCREEN BÊN PHẢI KHI ĐỌC PDF)
  // -------------------------------------------------------------------------
  if (isBlackboardMode) {
      return (
        <>
          <style>{chalkboardStyleTag}</style>
    
          {/* Lớp phủ mờ nhẹ khi ở sảnh chờ chọn Giáo viên */}
          {status === 'IDLE' && (
              <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-[99998]" onClick={onMinimize} />
          )}
    
          {/* BẢNG ĐEN TRƯỢT KHÍT 50% KHÔNG GIAN BÊN PHẢI MÀN HÌNH */}
          <div className="fixed top-0 right-0 h-[100dvh] w-full md:w-[50vw] bg-[#1e2024] shadow-[-20px_0_60px_rgba(0,0,0,0.7)] z-[100000] flex flex-col border-l border-slate-800 animate-in slide-in-from-right duration-500">
            
            {/* THANH ĐIỀU KHIỂN TRÊN CÙNG */}
            <div className="h-16 bg-[#141619] border-b border-slate-800 flex items-center justify-between px-6 shrink-0">
              <div className="flex items-center gap-3">
                 <div className="text-xl">✏️</div>
                 <div>
                     <h3 className="font-bold text-[14px] text-slate-200 tracking-wider uppercase">Virtual Blackboard</h3>
                     <p className="text-[10px] text-slate-500 uppercase tracking-widest font-bold">Bảng Phấn Giáo Viên Tony</p>
                 </div>
              </div>
              
              <div className="flex items-center gap-2 md:gap-3">
                 {status === 'CONNECTED' && (
                     <button 
                         onClick={handleClearBoard} 
                         className="text-[11px] text-slate-400 hover:text-white border border-slate-700 hover:border-slate-500 px-3 py-1 rounded font-bold uppercase tracking-wide transition-colors"
                     >
                         Xóa Bảng
                     </button>
                 )}
                 
                 {/* 🚀 NÚT FULLSCREEN MỚI ÉP CẢ TRANG LÊN TOÀN MÀN HÌNH */}
                 <button 
                     onClick={toggleFullscreen} 
                     className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/10 text-slate-400 transition-colors" 
                     title={isFullscreen ? "Thu nhỏ" : "Toàn màn hình"}
                 >
                    {isFullscreen ? (
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" /></svg>
                    ) : (
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0-4.5L15 15" /></svg>
                    )}
                 </button>
                 
                 <button 
                     onClick={onMinimize} 
                     className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/10 text-slate-400 transition-colors"
                     title="Thu nhỏ về góc màn hình"
                 >
                    <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M9 5l7 7-7 7" /></svg>
                 </button>
              </div>
            </div>
    
            {/* THÂN BẢNG ĐEN CHỨA CHỮ PHẤN RENDER TOÁN HỌC KATEX */}
            <div className="flex-1 overflow-y-auto p-6 md:p-10 custom-scrollbar flex flex-col relative bg-[#1e2024]">
              
              {status === 'IDLE' && (
                  <div className="m-auto text-center animate-in zoom-in-95 max-w-sm">
                     <div className="w-20 h-20 bg-slate-800 rounded-full flex items-center justify-center text-4xl shadow-inner border border-slate-700 mx-auto mb-5">👨‍🏫</div>
                     <h3 className="text-lg font-bold text-slate-200 mb-1">Học Phần Gia Sư Live</h3>
                     <p className="text-xs text-slate-400 mb-6">Vui lòng lựa chọn Thầy/Cô để mở kết nối đàm thoại giảng bài phối hợp viết bảng phấn.</p>
                     
                     <div className="flex justify-center gap-4 mb-6">
                        <button 
                            onClick={() => setExaminer('TONY')} 
                            className={`w-24 py-2.5 rounded-xl border-2 flex flex-col items-center gap-1 transition-all ${examiner === 'TONY' ? 'bg-emerald-500/10 border-emerald-500 shadow-md' : 'bg-slate-800/40 border-transparent opacity-60 hover:opacity-100'}`}
                        >
                           <span className="text-2xl">👨‍🏫</span>
                           <span className={`text-[11px] font-bold ${examiner === 'TONY' ? 'text-emerald-400' : 'text-slate-400'}`}>Thầy Tôn</span>
                        </button>
                        <button 
                            onClick={() => setExaminer('DIEP')} 
                            className={`w-24 py-2.5 rounded-xl border-2 flex flex-col items-center gap-1 transition-all ${examiner === 'DIEP' ? 'bg-emerald-500/10 border-emerald-500 shadow-md' : 'bg-slate-800/40 border-transparent opacity-60 hover:opacity-100'}`}
                        >
                           <span className="text-2xl">👩‍🏫</span>
                           <span className={`text-[11px] font-bold ${examiner === 'DIEP' ? 'text-emerald-400' : 'text-slate-400'}`}>Cô Diệp</span>
                        </button>
                     </div>
    
                     <button 
                         onClick={() => startCall(false)} 
                         className="w-full bg-blue-600 hover:bg-blue-500 text-white font-bold py-3 rounded-xl shadow-lg transition-all flex items-center justify-center gap-2 text-sm border border-blue-500 active:scale-95"
                     >
                         📞 Bắt Đầu Đàm Thoại Với Giáo Viên
                     </button>
                  </div>
              )}
    
              {status === 'CONNECTING' && (
                  <div className="m-auto flex flex-col items-center opacity-60">
                      <div className="w-10 h-10 border-4 border-slate-700 border-t-slate-300 rounded-full animate-spin mb-4" />
                      <div className="text-slate-400 font-bold tracking-widest text-xs uppercase animate-pulse">Đang mời giáo viên vào lớp học...</div>
                  </div>
              )}
    
              {status === 'CONNECTED' && (
                  <div className="tony-chalkboard-content flex-1 w-full text-left">
                      {transcript ? (
                          <>
                             <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
                                 {transcript}
                             </ReactMarkdown>
                             <div ref={(el) => { if (el) el.scrollIntoView({ behavior: 'smooth' }); }} />
                          </>
                      ) : (
                          <div className="h-full flex items-center justify-center text-center opacity-30 italic text-sm text-slate-400" style={{fontFamily: 'sans-serif'}}>
                              Bảng đen trống.<br/>Thầy cô đang lắng nghe câu hỏi từ mic của em để viết bảng giải nghĩa...
                          </div>
                      )}
                  </div>
              )}
    
            </div>
    
            {/* THANH DOCK ĐIỀU KHIỂN ĐÁY DÀNH CHO VOICE CHUYÊN DỤNG */}
            {status === 'CONNECTED' && (
                <div className="p-6 bg-gradient-to-t from-[#141619] to-transparent shrink-0">
                    <div className="bg-[#24292f] border border-slate-700 rounded-full py-2.5 px-4 flex items-center justify-between gap-4 shadow-2xl max-w-md mx-auto">
                        <div className="text-xs text-slate-400 pl-3 italic truncate flex-1 font-mono">
                            {isMicSending ? '🎙️ Đang ghi âm nói (Học sinh)...' : '🔊 Thầy cô đang viết bảng giảng bài...'}
                        </div>
                        
                        <div className="flex items-center gap-2 shrink-0">
                            <button 
                                onClick={toggleMute} 
                                className={`w-9 h-9 rounded-full flex items-center justify-center transition-all shadow-md ${isMuted ? 'bg-amber-600 text-white border border-amber-500' : 'bg-slate-700 text-slate-300 hover:bg-slate-600 border border-slate-600'}`}
                                title="Tắt/Mở Mic Con"
                            >
                                <span className="text-md">{isMuted ? '🔇' : '🎙️'}</span>
                            </button>
                            <button 
                                onClick={handleUserHangUp} 
                                className="w-9 h-9 bg-red-600 hover:bg-red-500 text-white rounded-full flex items-center justify-center transition-all active:scale-95 shadow-md shadow-red-900/50 border border-red-500"
                                title="Kết thúc đàm thoại"
                            >
                                <span className="text-md">🛑</span>
                            </button>
                        </div>
                    </div>
                </div>
            )}
    
          </div>
        </>
      );
  }

  // -------------------------------------------------------------------------
  // 2️⃣ NHÂN CÁCH 2: GIAO DIỆN BÌNH THƯỜNG (LOẠI BỎ OUTER SCROLLBAR - CHỈ CUỘN TRONG Ô TEXT)
  // -------------------------------------------------------------------------
  return (
    <div className="fixed inset-0 z-[9999] flex flex-col items-center justify-center min-h-[100dvh] bg-[#020617]/95 backdrop-blur-md text-slate-200 p-4 md:p-8 w-full font-sans animate-in fade-in duration-300">
      
      {/* 🚀 ĐIỀU KIỆN MỚI: CHỈ HIỂN THỊ NẾU BONG BÓNG CHAT KHÔNG TỒN TẠI */}
      {onOpenAI && !isChatBubbleVisible && (
          <button 
             onClick={handleYellowButtonClick}
             className="absolute top-4 right-4 md:top-6 md:right-6 text-amber-400 hover:text-amber-300 transition-all flex items-center gap-2 font-bold bg-amber-950/40 px-3 py-2 md:px-5 md:py-2.5 rounded-xl border border-amber-800/60 shadow-[0_0_15px_rgba(217,119,6,0.15)] z-20 hover:scale-105 active:scale-95"
             title={currentMode === 'TUTOR' ? 'Mở lại khung Chat Text' : 'Xem gợi ý kịch bản IELTS'}
          >
             <span className="text-lg">💬</span> 
             <span className="hidden sm:inline text-[13px] md:text-[14px]">
                 {currentMode === 'TUTOR' ? 'Mở khung chat' : 'Kịch bản AI'}
             </span>
          </button>
      )}

      {/* 🚀 ĐÃ SỬA: Đổi overflow-y-auto thành overflow-hidden để xoá scrollbar bao ngoài */}
      <div className="bg-[#0f172a] p-6 md:p-8 rounded-[2rem] shadow-[0_20px_60px_rgba(0,0,0,0.8)] border border-slate-700 max-w-2xl w-full text-center relative z-10 max-h-[95dvh] flex flex-col my-auto overflow-hidden">
        
        <button 
            onClick={handleBackClick} 
            className="absolute top-4 left-4 md:top-6 md:left-6 text-slate-400 hover:text-white bg-slate-800 hover:bg-slate-700 px-4 py-2 rounded-xl text-sm font-medium transition-all shadow-sm border border-slate-600 z-20"
        >
          {status !== 'IDLE' ? '👇 Thu nhỏ (Nghe nền)' : '← Thoát'}
        </button>

        <div className="mb-6 mt-12 md:mt-8 shrink-0">
           <h2 className="text-2xl md:text-3xl font-black mb-2 text-white tracking-tight">
               {currentMode === 'TUTOR' ? 'Gia Sư Giải Đáp 1-1' : 'Phòng Luyện Nói 1-1'}
           </h2>
           <p className="text-emerald-400 font-medium text-[13px] md:text-[14px] opacity-90">
               {currentMode === 'TUTOR' ? 'Cùng thầy/cô phân tích nội dung bài học' : 'Đàm thoại tiếng Anh trực tiếp với Giám khảo ảo'}
           </p>
        </div>

        {status === 'IDLE' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 overflow-y-auto custom-scrollbar flex-1 pb-2">
             
             <div className="bg-slate-800/50 p-4 rounded-2xl border border-slate-700 mb-6 text-left shadow-inner flex flex-col">
                <span className="block text-[11px] uppercase tracking-widest text-slate-400 font-bold mb-2 shrink-0">
                    Đang hỗ trợ nội dung:
                </span>
                <div className="text-[14px] font-medium text-slate-200 whitespace-pre-wrap">
                    {currentMode === 'TUTOR' ? "Chữa bài & Giải đáp thắc mắc chuyên sâu" : `"${currentTopic}"`}
                </div>
             </div>
             
             <div className="mb-6 shrink-0">
                <h3 className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-4">Lựa chọn Giám khảo</h3>
                <div className="flex justify-center gap-3 md:gap-4">
                    <button 
                        onClick={() => setExaminer('TONY')} 
                        className={`relative w-24 md:w-28 py-3 rounded-2xl flex flex-col items-center gap-2 border-2 transition-all ${examiner === 'TONY' ? 'bg-slate-800 border-emerald-500 shadow-[0_0_20px_rgba(16,185,129,0.2)]' : 'bg-slate-900 border-transparent opacity-60 hover:bg-slate-800'}`}
                    >
                       <div className="text-3xl drop-shadow-md">👨‍🏫</div>
                       <span className={`text-[12px] md:text-[13px] font-bold ${examiner === 'TONY' ? 'text-emerald-400' : 'text-slate-400'}`}>Thầy Tôn</span>
                       {examiner === 'TONY' && <div className="absolute -top-2 -right-2 w-5 h-5 bg-emerald-500 rounded-full flex items-center justify-center text-white text-[10px] shadow-sm">✓</div>}
                    </button>
                    
                    <button 
                        onClick={() => setExaminer('DIEP')} 
                        className={`relative w-24 md:w-28 py-3 rounded-2xl flex flex-col items-center gap-2 border-2 transition-all ${examiner === 'DIEP' ? 'bg-slate-800 border-emerald-500 shadow-[0_0_20px_rgba(16,185,129,0.2)]' : 'bg-slate-900 border-transparent opacity-60 hover:bg-slate-800'}`}
                    >
                       <div className="text-3xl drop-shadow-md">👩‍🏫</div>
                       <span className={`text-[12px] md:text-[13px] font-bold ${examiner === 'DIEP' ? 'text-emerald-400' : 'text-slate-400'}`}>Cô Diệp</span>
                       {examiner === 'DIEP' && <div className="absolute -top-2 -right-2 w-5 h-5 bg-emerald-500 rounded-full flex items-center justify-center text-white text-[10px] shadow-sm">✓</div>}
                    </button>
                </div>
             </div>
             
             <button 
                 onClick={() => startCall(false)} 
                 className="w-full shrink-0 bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-4 rounded-2xl text-[15px] md:text-[16px] shadow-[0_10px_20px_rgba(16,185,129,0.3)] flex items-center justify-center gap-3 active:scale-95 transition-all border border-emerald-500"
             >
                 <span className="text-xl">📞</span> Bắt Đầu Đàm Thoại
             </button>
          </div>
        )}

        {status === 'CONNECTING' && (
            <div className="py-12 flex flex-col items-center animate-in zoom-in-95 duration-300 flex-1 justify-center">
                <div className="w-12 h-12 border-4 border-emerald-500/30 border-t-emerald-500 rounded-full animate-spin mb-6 shadow-[0_0_15px_rgba(16,185,129,0.5)]"></div>
                <div className="text-emerald-400 font-bold tracking-widest uppercase text-sm animate-pulse">ĐANG THIẾT LẬP KẾT NỐI...</div>
            </div>
        )}

        {status === 'CONNECTED' && (
          <div className="flex flex-col items-center animate-in zoom-in-95 duration-500 w-full h-full flex-1 overflow-hidden">
            
            <div className="relative mb-4 shrink-0">
                <div className={`absolute inset-0 rounded-full transition-all duration-300 opacity-20 ${!isMuted && isMicSending ? 'bg-red-500 scale-[1.3] animate-pulse shadow-[0_0_30px_rgba(239,68,68,0.5)]' : 'bg-emerald-500 scale-100 shadow-[0_0_30px_rgba(16,185,129,0.5)]'}`}></div>
                <div className="w-20 h-20 rounded-full overflow-hidden border-4 border-slate-700 shadow-xl relative z-10 bg-slate-800 flex items-center justify-center text-4xl">
                    {examiner === 'TONY' ? '👨‍🏫' : '👩‍🏫'}
                </div>
            </div>
            
            <p className={`shrink-0 font-bold mb-4 tracking-widest uppercase text-[10px] md:text-[11px] px-4 py-1.5 rounded-full border shadow-sm transition-colors ${isMuted ? 'bg-amber-950/50 text-amber-400 border-amber-800' : (isMicSending ? 'bg-red-950/50 text-red-400 border-red-800' : 'bg-emerald-950/50 text-emerald-400 border-emerald-800')}`}>
                {isMuted ? "🔇 ĐÃ TẮT MIC (CHỈ NGHE)" : (isMicSending ? "🔴 ĐANG GHI ÂM (BẠN NÓI)" : "🟢 AI ĐANG NGHE/PHẢN HỒI...")}
            </p>
            
            {/* 🚀 CHỈ ĐỂ DUY NHẤT VÙNG NÀY ĐƯỢC CUỘN */}
            <div className="bg-[#020617] rounded-2xl p-4 md:p-6 w-full text-left h-32 md:h-40 overflow-y-auto mb-6 border border-slate-800 font-mono text-[13px] md:text-[14px] text-slate-300 leading-relaxed shadow-inner custom-scrollbar flex-1 min-h-[120px] prose prose-invert max-w-none">
               {transcript ? (
                  <ReactMarkdown 
                     remarkPlugins={[remarkMath]} 
                     rehypePlugins={[rehypeKatex]}
                  >
                     {transcript}
                  </ReactMarkdown>
               ) : (
                  <span className="opacity-40 italic">Đang chờ tín hiệu âm thanh...</span>
               )}
               <div ref={(el) => { if (el) el.scrollIntoView({ behavior: 'smooth' }); }} />
            </div>
            
            <div className="flex flex-col sm:flex-row gap-3 w-full shrink-0">
                <button 
                    onClick={toggleMute} 
                    className={`flex-1 font-bold py-3 md:py-4 rounded-2xl flex items-center justify-center gap-2 md:gap-3 transition-all active:scale-95 shadow-lg border ${isMuted ? 'bg-amber-600 hover:bg-amber-500 text-white border-amber-500' : 'bg-slate-700 hover:bg-slate-600 text-white border-slate-600'}`}
                >
                   <span className="text-lg md:text-xl">{isMuted ? '🔇' : '🎙️'}</span> {isMuted ? 'Đã Tắt Mic' : 'Tắt Mic Tạm Thời'}
                </button>
                <button 
                    onClick={handleUserHangUp} 
                    className="flex-1 bg-red-600 hover:bg-red-500 text-white font-bold py-3 md:py-4 rounded-2xl shadow-[0_10px_20px_rgba(220,38,38,0.3)] flex items-center justify-center gap-2 md:gap-3 active:scale-95 transition-all border border-red-500"
                >
                    <span className="text-lg md:text-xl">🛑</span> Dập Máy
                </button>
            </div>
            
          </div>
        )}
      </div>
    </div>
  );
}