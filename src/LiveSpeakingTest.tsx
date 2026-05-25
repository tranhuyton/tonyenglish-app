import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import React, { useState, useRef, useEffect } from 'react';
import { supabase } from './supabase';

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
  
  const [isBlackboardMode, setIsBlackboardMode] = useState(false);
  const [isChatBubbleVisible, setIsChatBubbleVisible] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);

  useEffect(() => {
    const onFullscreenChange = () => setIsFullscreen(!!document.fullscreenElement);
    document.addEventListener('fullscreenchange', onFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', onFullscreenChange);
  }, []);

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
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
  
  const callStartTimeRef = useRef<number>(0);

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

  useEffect(() => {
      const handleBubbleState = (e: any) => {
          setIsChatBubbleVisible(e.detail);
      };
      window.addEventListener('tony-chat-bubble-state', handleBubbleState);
      const bubbleExists = !!document.querySelector('button[title="Mở lại khung Chat AI"]');
      setIsChatBubbleVisible(bubbleExists);
      return () => {
          window.removeEventListener('tony-chat-bubble-state', handleBubbleState);
      };
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
      return () => {
          window.dispatchEvent(new CustomEvent('tony-teacher-board-state', { detail: false }));
      };
  }, [viewState]);

  useEffect(() => {
      const autoStart = sessionStorage.getItem('tony_auto_start') === 'true';
      if (autoStart) {
          sessionStorage.removeItem('tony_auto_start');
          const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
          if (isMobile) return; 
          onMaximize();
      }
  }, [onMaximize]);

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
  // 👁️ MẮT THẦN CỦA AI BẢNG ĐEN
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
        callStartTimeRef.current = Date.now();
        
        if (!isBlackboardMode) {
            onMinimize();
        }

        const voiceName = examiner === 'TONY' ? 'Charon' : 'Kore';
        const teacherName = examiner === 'TONY' ? 'thầy Tôn' : 'cô Diệp';

        const mode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
        const tutorDataRaw = sessionStorage.getItem('tony_tutor_data');
        const tutorData = tutorDataRaw ? JSON.parse(tutorDataRaw) : null;
        const currentTopic = sessionStorage.getItem('tony_live_topic') || "Bài tập giao tiếp tổng hợp";

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

        // 🚀 THUẬT TOÁN ĐÃ ĐƯỢC CHUẨN HOÁ: ĐẨY TOÀN BỘ PCM LÊN CHUYỂN SERVER GOOGLE TỰ LỌC
        processorNodeRef.current.onaudioprocess = (e) => {
            if (ws !== wsRef.current || ws.readyState !== WebSocket.OPEN) {
                return;
            }
              
            if (isSetupCompleteRef.current) {
              const inputData = e.inputBuffer.getChannelData(0);
              
              if (isMutedRef.current) {
                  setIsMicSending(false);
                  return; 
              }
  
              const pcm16Buffer = floatTo16BitPCM(inputData);
              
              ws.send(JSON.stringify({ 
                  realtimeInput: { 
                      audio: { 
                          mimeType: "audio/pcm;rate=16000", 
                          data: arrayBufferToBase64(pcm16Buffer) 
                      } 
                  } 
              }));
              
              setIsMicSending(true);
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
    
    // 🚀 CHỐT SỔ VÀ GỬI BÁO CÁO THỜI LƯỢNG GỌI CHO ADMIN
    if (callStartTimeRef.current > 0) {
        const durationSecs = Math.round((Date.now() - callStartTimeRef.current) / 1000);
        callStartTimeRef.current = 0; 
        if (durationSecs > 5) { 
            supabase.auth.getUser().then(({ data: { user } }) => {
                if (user) {
                    let contextStr = "Luyện nói tự do";
                    const tutorDataRaw = sessionStorage.getItem('tony_tutor_data');
                    if (tutorDataRaw) {
                        try {
                            const parsed = JSON.parse(tutorDataRaw);
                            contextStr = parsed.transcript ? parsed.transcript.substring(0, 150) + '...' : "Hỏi bài tập chuyên sâu";
                        } catch(e){}
                    } else {
                        contextStr = sessionStorage.getItem('tony_live_topic') || "Luyện nói tự do";
                    }

                    supabase.from('activity_logs').insert([{
                        user_id: user.id,
                        action_type: 'call_tutor',
                        details: { duration: durationSecs, topic: contextStr }
                    }]).then();
                }
            });
        }
    }
    
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
          return (
              <button 
                  onClick={onMaximize}
                  className={`fixed bottom-8 right-8 z-[100000] w-14 h-14 rounded-full flex items-center justify-center shadow-[0_10px_30px_rgba(0,0,0,0.5)] transition-all duration-300 hover:scale-110 active:scale-95 border-2 ${status === 'CONNECTED' ? (isMicSending && !isMuted ? 'bg-red-500 border-red-300 animate-pulse' : 'bg-emerald-500 border-emerald-300') : 'bg-indigo-600 border-indigo-400'}`}
                  title="Mở Bảng Giáo Viên"
              >
                  <span className="text-2xl">{status === 'CONNECTED' ? '🎙️' : '👨‍🏫'}</span>
              </button>
          );
      } else {
          return (
              <div className="fixed bottom-6 right-6 z-[99998] bg-slate-900/95 backdrop-blur-md border border-slate-700 shadow-[0_20px_50px_rgba(0,0,0,0.5)] rounded-[1.5rem] p-4 flex flex-col gap-3 w-[280px] md:w-80 animate-in slide-in-from-bottom-5 font-sans transition-all">
                 <div className="flex justify-between items-center">
                    <div className="flex items-center gap-2.5 cursor-pointer flex-1 min-w-0" onClick={onMaximize}>
                       <div className={`w-3 h-3 shrink-0 rounded-full ${!isMuted && isMicSending ? 'bg-red-500 animate-pulse shadow-[0_0_10px_rgba(239,68,68,0.8)]' : 'bg-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.8)]'}`}></div>
                       <span className="text-white font-semibold text-[13px] truncate">
                           {isMuted ? 'Đã tắt Mic' : (isMicSending ? 'Đang gửi âm thanh...' : 'Gia sư đang đợi...')}
                       </span>
                    </div>
                    <button onClick={onMaximize} className="text-slate-400 hover:text-white w-8 h-8 flex items-center justify-center bg-slate-800 rounded-full shrink-0 ml-2 border border-slate-600 shadow-sm transition-colors" title="Phóng to">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0-4.5L15 15" /></svg>
                    </button>
                 </div>
                 <div className="flex gap-2 mt-1">
                     <button 
                        onClick={toggleMute} 
                        className={`flex-1 font-bold py-2 rounded-xl text-[12px] md:text-[13px] transition-all flex items-center justify-center gap-2 ${isMuted ? 'bg-amber-600 hover:bg-amber-500 text-white shadow-md shadow-amber-900/50' : 'bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-600'}`}
                     >
                        {isMuted ? '🔇 Đã Tắt Mic' : '🎙️ Tắt Mic'}
                     </button>
                     <button 
                         onClick={handleUserHangUp} 
                         className="flex-1 bg-red-500/10 hover:bg-red-500 text-red-500 hover:text-white font-bold py-2 rounded-xl text-[12px] md:text-[13px] transition-all flex items-center justify-center gap-2 border border-red-500/50 hover:border-red-500"
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
    
          {status === 'IDLE' && (
              <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[99998]" onClick={onMinimize} />
          )}
    
          <div className="fixed top-0 right-0 h-[100dvh] w-full md:w-[50vw] bg-[#1a1c21] shadow-[-30px_0_60px_rgba(0,0,0,0.8)] z-[100000] flex flex-col border-l-[6px] border-[#2c1808]/80 animate-in slide-in-from-right duration-500">
            
            {/* Header Bảng Đen (Nhỏ gọn, Tinh tế) */}
            <div className="h-14 bg-black/40 border-b border-white/5 flex items-center justify-between px-5 shrink-0 backdrop-blur-md">
              <div className="flex items-center gap-3">
                 <div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center text-sm border border-white/20">
                     ✏️
                 </div>
                 <div className="flex flex-col">
                     <h3 className="font-bold text-[13px] text-slate-300 uppercase tracking-widest leading-none">Tony Blackboard</h3>
                 </div>
              </div>
              
              <div className="flex items-center gap-1">
                 {status === 'CONNECTED' && (
                     <button 
                         onClick={handleClearBoard} 
                         className="text-[11px] text-slate-400 hover:text-white bg-white/5 hover:bg-white/10 px-3 py-1.5 rounded-lg font-bold uppercase tracking-wide transition-colors mr-2 border border-white/10"
                     >
                         Xóa Bảng
                     </button>
                 )}
                 
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
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
                 </button>
              </div>
            </div>
    
            <div className="flex-1 overflow-y-auto p-6 md:p-10 custom-scrollbar flex flex-col relative bg-[url('https://www.transparenttextures.com/patterns/black-paper.png')]">
              
              {status === 'IDLE' && (
                  <div className="m-auto text-center animate-in zoom-in-95 max-w-sm w-full bg-slate-900/80 p-8 rounded-[2rem] border border-slate-700/50 backdrop-blur-md shadow-2xl">
                     <div className="w-20 h-20 bg-gradient-to-tr from-[#0ea5e9] to-indigo-500 rounded-full flex items-center justify-center text-4xl shadow-lg border border-white/20 mx-auto mb-6">👨‍🏫</div>
                     <h3 className="text-xl font-black text-white mb-2 tracking-tight">Học Phần Gia Sư Live</h3>
                     <p className="text-[13px] text-slate-400 mb-8 font-medium">Vui lòng lựa chọn Thầy/Cô để mở kết nối đàm thoại giảng bài phối hợp viết bảng phấn.</p>
                     
                     <div className="flex justify-center gap-4 mb-8">
                        <button 
                            onClick={() => setExaminer('TONY')} 
                            className={`flex-1 py-4 rounded-2xl border-2 flex flex-col items-center gap-2 transition-all duration-300 ${examiner === 'TONY' ? 'bg-[#0ea5e9]/20 border-[#0ea5e9] shadow-[0_0_20px_rgba(14,165,233,0.3)]' : 'bg-slate-800 border-slate-700 opacity-70 hover:opacity-100 hover:border-slate-500'}`}
                        >
                           <span className="text-3xl drop-shadow-md">👨‍🏫</span>
                           <span className={`text-[12px] font-black uppercase tracking-widest ${examiner === 'TONY' ? 'text-[#0ea5e9]' : 'text-slate-400'}`}>Thầy Tôn</span>
                        </button>
                        <button 
                            onClick={() => setExaminer('DIEP')} 
                            className={`flex-1 py-4 rounded-2xl border-2 flex flex-col items-center gap-2 transition-all duration-300 ${examiner === 'DIEP' ? 'bg-[#0ea5e9]/20 border-[#0ea5e9] shadow-[0_0_20px_rgba(14,165,233,0.3)]' : 'bg-slate-800 border-slate-700 opacity-70 hover:opacity-100 hover:border-slate-500'}`}
                        >
                           <span className="text-3xl drop-shadow-md">👩‍🏫</span>
                           <span className={`text-[12px] font-black uppercase tracking-widest ${examiner === 'DIEP' ? 'text-[#0ea5e9]' : 'text-slate-400'}`}>Cô Diệp</span>
                        </button>
                     </div>
    
                     <button 
                         onClick={() => startCall(false)} 
                         className="w-full bg-[#0ea5e9] hover:bg-[#0284c7] text-white font-black py-4 rounded-xl shadow-[0_10px_20px_rgba(14,165,233,0.3)] transition-all flex items-center justify-center gap-2 text-sm uppercase tracking-wide active:scale-95"
                     >
                         📞 Bắt Đầu Đàm Thoại
                     </button>
                  </div>
              )}
    
              {status === 'CONNECTING' && (
                  <div className="m-auto flex flex-col items-center opacity-70">
                      <div className="w-12 h-12 border-4 border-slate-700 border-t-[#0ea5e9] rounded-full animate-spin mb-4" />
                      <div className="text-slate-400 font-bold tracking-widest text-xs uppercase animate-pulse">Đang mời giáo viên vào lớp...</div>
                  </div>
              )}
    
              {status === 'CONNECTED' && (
                  <div className="tony-chalkboard-content flex-1 w-full text-left pb-24">
                      {transcript ? (
                          <>
                             <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
                                 {transcript}
                             </ReactMarkdown>
                             <div ref={(el) => { if (el) el.scrollIntoView({ behavior: 'smooth' }); }} />
                          </>
                      ) : (
                          <div className="h-full flex flex-col items-center justify-center text-center opacity-30 italic text-slate-400" style={{fontFamily: 'sans-serif'}}>
                              <span className="text-4xl mb-4 grayscale">🎙️</span>
                              <span className="text-[15px] font-medium">Bảng đen trống.<br/>Thầy cô đang lắng nghe câu hỏi từ mic của em để viết bảng giải nghĩa...</span>
                          </div>
                      )}
                  </div>
              )}
    
            </div>
            
            {/* Thanh Control Bar nổi bồng bềnh */}
            {status === 'CONNECTED' && (
                <div className="absolute bottom-6 left-1/2 -translate-x-1/2 w-full max-w-sm px-4 z-50">
                    <div className="bg-slate-900/95 backdrop-blur-md border border-slate-700/80 rounded-full py-2 px-3 flex items-center justify-between gap-3 shadow-[0_20px_40px_rgba(0,0,0,0.8)]">
                        <div className="text-[11px] text-slate-400 pl-3 italic truncate flex-1 font-mono font-medium">
                            {!isMuted && isMicSending ? '🎙️ Đang ghi âm (Bạn nói)...' : '🔊 Thầy cô đang giảng bài...'}
                        </div>
                        
                        <div className="flex items-center gap-1.5 shrink-0">
                            <button 
                                onClick={toggleMute} 
                                className={`w-10 h-10 rounded-full flex items-center justify-center transition-all ${isMuted ? 'bg-amber-500 text-white shadow-[0_0_15px_rgba(245,158,11,0.4)]' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'}`}
                                title="Tắt/Mở Mic Con"
                            >
                                <span className="text-lg">{isMuted ? '🔇' : '🎙️'}</span>
                            </button>
                            <button 
                                onClick={handleUserHangUp} 
                                className="w-10 h-10 bg-red-500/20 hover:bg-red-500 text-red-500 hover:text-white rounded-full flex items-center justify-center transition-all active:scale-95 border border-red-500/50 hover:border-red-500"
                                title="Kết thúc đàm thoại"
                            >
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
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
  // 2️⃣ NHÂN CÁCH 2: GIAO DIỆN BÌNH THƯỜNG (EDTECH STYLE)
  // -------------------------------------------------------------------------
  return (
    <div className="fixed inset-0 z-[9999] flex flex-col items-center justify-center min-h-[100dvh] bg-slate-900/90 backdrop-blur-md text-slate-200 p-4 md:p-8 w-full font-sans animate-in fade-in duration-300">
      
      {onOpenAI && !isChatBubbleVisible && (
          <button 
             onClick={handleYellowButtonClick}
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
        
        <button 
            onClick={handleBackClick} 
            className="absolute top-6 left-6 text-slate-500 hover:text-slate-800 bg-slate-100 hover:bg-slate-200 px-4 py-2.5 rounded-xl text-[13px] font-bold transition-all shadow-sm border border-slate-200 z-20 flex items-center gap-2 uppercase tracking-wide"
        >
          {status !== 'IDLE' ? (
              <><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" /></svg> Thu nhỏ</>
          ) : (
              <><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" /></svg> Thoát</>
          )}
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
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 overflow-y-auto custom-scrollbar flex-1 pb-2 px-2">
             
             <div className="bg-slate-50 p-5 md:p-6 rounded-2xl border border-slate-200 mb-8 text-left shadow-sm flex flex-col">
                <span className="block text-[11px] uppercase tracking-widest text-slate-500 font-bold mb-2 shrink-0">
                    Chủ đề đàm thoại:
                </span>
                <div className="text-[15px] font-semibold text-slate-800 whitespace-pre-wrap leading-relaxed">
                    {currentMode === 'TUTOR' ? "Chữa bài & Giải đáp thắc mắc chuyên sâu" : `"${currentTopic}"`}
                </div>
             </div>
             
             <div className="mb-8 shrink-0">
                <h3 className="text-[12px] font-black text-slate-400 uppercase tracking-widest mb-4">Lựa chọn Giám khảo</h3>
                <div className="flex justify-center gap-4">
                    <button 
                        onClick={() => setExaminer('TONY')} 
                        className={`relative flex-1 py-4 rounded-2xl flex flex-col items-center gap-2 border-2 transition-all duration-300 ${examiner === 'TONY' ? 'bg-[#0ea5e9]/10 border-[#0ea5e9] shadow-sm' : 'bg-white border-slate-200 text-slate-500 hover:border-[#0ea5e9]/50'}`}
                    >
                       <div className="text-4xl drop-shadow-sm mb-1">👨‍🏫</div>
                       <span className={`text-[13px] font-black uppercase tracking-wider ${examiner === 'TONY' ? 'text-[#0ea5e9]' : 'text-slate-500'}`}>Thầy Tôn</span>
                       {examiner === 'TONY' && <div className="absolute -top-2 -right-2 w-6 h-6 bg-[#0ea5e9] rounded-full flex items-center justify-center text-white text-[12px] shadow-md border-2 border-white"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-4 h-4"><path fillRule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clipRule="evenodd" /></svg></div>}
                    </button>
                    
                    <button 
                        onClick={() => setExaminer('DIEP')} 
                        className={`relative flex-1 py-4 rounded-2xl flex flex-col items-center gap-2 border-2 transition-all duration-300 ${examiner === 'DIEP' ? 'bg-purple-500/10 border-purple-500 shadow-sm' : 'bg-white border-slate-200 text-slate-500 hover:border-purple-500/50'}`}
                    >
                       <div className="text-4xl drop-shadow-sm mb-1">👩‍🏫</div>
                       <span className={`text-[13px] font-black uppercase tracking-wider ${examiner === 'DIEP' ? 'text-purple-600' : 'text-slate-500'}`}>Cô Diệp</span>
                       {examiner === 'DIEP' && <div className="absolute -top-2 -right-2 w-6 h-6 bg-purple-500 rounded-full flex items-center justify-center text-white text-[12px] shadow-md border-2 border-white"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-4 h-4"><path fillRule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clipRule="evenodd" /></svg></div>}
                    </button>
                </div>
             </div>
             
             <button 
                 onClick={() => startCall(false)} 
                 className="w-full shrink-0 bg-[#0ea5e9] hover:bg-[#0284c7] text-white font-black py-4 md:py-5 rounded-2xl text-[15px] md:text-[16px] shadow-[0_10px_30px_rgba(14,165,233,0.3)] flex items-center justify-center gap-3 active:scale-95 transition-all uppercase tracking-wide"
             >
                 <span className="text-xl">📞</span> Bắt Đầu Đàm Thoại
             </button>
          </div>
        )}

        {status === 'CONNECTING' && (
            <div className="py-16 flex flex-col items-center animate-in zoom-in-95 duration-300 flex-1 justify-center">
                <div className="relative w-16 h-16 mb-8">
                    <div className="absolute inset-0 border-4 border-[#0ea5e9]/20 rounded-full"></div>
                    <div className="absolute inset-0 border-4 border-[#0ea5e9] border-t-transparent rounded-full animate-spin"></div>
                </div>
                <div className="text-slate-500 font-black tracking-widest uppercase text-sm animate-pulse">Đang thiết lập kết nối...</div>
            </div>
        )}

        {status === 'CONNECTED' && (
          <div className="flex flex-col items-center animate-in zoom-in-95 duration-500 w-full h-full flex-1 overflow-hidden px-2">
            
            <div className="relative mb-6 shrink-0 mt-4">
                {/* Hiệu ứng sóng âm Pulse Ring */}
                <div className={`absolute inset-0 rounded-full transition-all duration-300 opacity-20 ${!isMuted && isMicSending ? 'bg-red-500 scale-[1.5] animate-pulse shadow-[0_0_40px_rgba(239,68,68,0.5)]' : 'bg-[#0ea5e9] scale-100 shadow-[0_0_40px_rgba(14,165,233,0.5)]'}`}></div>
                <div className={`absolute inset-0 rounded-full transition-all duration-500 opacity-10 ${!isMuted && isMicSending ? 'bg-red-500 scale-[2] animate-pulse delay-75' : 'bg-[#0ea5e9] scale-[1.3]'}`}></div>
                
                <div className="w-24 h-24 rounded-full overflow-hidden border-4 border-white shadow-xl relative z-10 bg-slate-100 flex items-center justify-center text-5xl">
                    {examiner === 'TONY' ? '👨‍🏫' : '👩‍🏫'}
                </div>
            </div>
            
            <p className={`shrink-0 font-black mb-6 tracking-widest uppercase text-[10px] md:text-[11px] px-4 py-1.5 rounded-full border shadow-sm transition-colors ${isMuted ? 'bg-amber-50 text-amber-600 border-amber-200' : (isMicSending ? 'bg-red-50 text-red-600 border-red-200' : 'bg-sky-50 text-[#0ea5e9] border-sky-200')}`}>
                {isMuted ? "🔇 ĐÃ TẮT MIC (CHỈ NGHE)" : (isMicSending ? "🔴 ĐANG GHI ÂM (BẠN NÓI)" : "🟢 AI ĐANG NGHE/PHẢN HỒI...")}
            </p>
            
            <div className="bg-slate-50 rounded-2xl p-5 md:p-6 w-full text-left h-32 md:h-48 overflow-y-auto mb-8 border border-slate-200 shadow-inner custom-scrollbar flex-1 min-h-[140px]">
               {transcript ? (
                  <div className="prose prose-slate prose-sm max-w-none font-medium text-slate-700 leading-relaxed">
                      <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
                         {transcript}
                      </ReactMarkdown>
                  </div>
               ) : (
                  <div className="flex flex-col items-center justify-center h-full opacity-40">
                      <span className="text-3xl mb-2 grayscale">🎙️</span>
                      <span className="italic text-sm font-medium">Đang chờ tín hiệu âm thanh...</span>
                  </div>
               )}
               <div ref={(el) => { if (el) el.scrollIntoView({ behavior: 'smooth' }); }} />
            </div>
            
            <div className="flex flex-col sm:flex-row gap-3 md:gap-4 w-full shrink-0">
                <button 
                    onClick={toggleMute} 
                    className={`flex-1 font-black py-4 rounded-xl flex items-center justify-center gap-2 transition-all active:scale-95 shadow-sm border-2 text-[14px] uppercase tracking-wide ${isMuted ? 'bg-amber-500 text-white border-amber-500 shadow-amber-500/30' : 'bg-white text-slate-600 hover:text-slate-800 border-slate-200 hover:border-slate-300 hover:bg-slate-50'}`}
                >
                   <span className="text-xl">{isMuted ? '🔇' : '🎙️'}</span> {isMuted ? 'Đã Tắt Mic' : 'Tắt Mic Tạm Thời'}
                </button>
                <button 
                    onClick={handleUserHangUp} 
                    className="flex-1 bg-red-50/50 hover:bg-red-500 text-red-500 hover:text-white font-black py-4 rounded-xl flex items-center justify-center gap-2 active:scale-95 transition-all border-2 border-red-200 hover:border-red-500 text-[14px] uppercase tracking-wide shadow-sm"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg> Dập Máy
                </button>
            </div>
            
          </div>
        )}
      </div>
    </div>
  );
}