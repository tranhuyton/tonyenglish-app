import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import React, { useState, useRef, useEffect } from 'react';
import { supabase } from './supabase';

// =========================================================================================
// 🚀 CSS: STYLE CHỮ PHẤN VIẾT TAY CHO CHẾ ĐỘ BẢNG ĐEN
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
    onOpenAI 
}: { 
    viewState: 'FULLSCREEN' | 'MINIMIZED', 
    onMinimize: () => void, 
    onMaximize: () => void, 
    onClose: () => void, 
    onOpenAI?: (passedMode?: string) => void 
}) {
  const [status, setStatus] = useState<'IDLE' | 'CONNECTING' | 'CONNECTED'>('IDLE');
  const [examiner, setExaminer] = useState<'TONY' | 'DIEP'>('TONY');
  
  const [isRecording, setIsRecording] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isTextOnlyMode, setIsTextOnlyMode] = useState(false); 
  
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [liveTranscript, setLiveTranscript] = useState<string>('');
  const [currentDraft, setCurrentDraft] = useState<string>('');
  
  const [chatInput, setChatInput] = useState<string>('');
  
  const [isBlackboardMode, setIsBlackboardMode] = useState(false);
  const [isChatBubbleVisible, setIsChatBubbleVisible] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);

  // REFS QUAN TRỌNG ĐIỀU KHIỂN LUỒNG
  const wsRef = useRef<WebSocket | null>(null);
  const isSetupCompleteRef = useRef<boolean>(false);
  const isMicOpenRef = useRef<boolean>(false); 
  const isRecordingRef = useRef<boolean>(false); 
  const transcriptRef = useRef<string>('');
  const callStartTimeRef = useRef<number>(0);
  const isTextOnlyModeRef = useRef<boolean>(false); 
  
  // Audio Input (Mic)
  const streamRef = useRef<MediaStream | null>(null);
  const audioCtxInputRef = useRef<AudioContext | null>(null);
  const sourceNodeRef = useRef<MediaStreamAudioSourceNode | null>(null);
  const processorNodeRef = useRef<ScriptProcessorNode | null>(null);
  const recognitionRef = useRef<any>(null); 
  
  // Audio Output (Loa)
  const audioCtxOutputRef = useRef<AudioContext | null>(null);
  const nextPlayTimeRef = useRef<number>(0);

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const pendingImageRef = useRef<string | null>(null);

  // FULLSCREEN CONTROL
  useEffect(() => {
    const onFullscreenChange = () => setIsFullscreen(!!document.fullscreenElement);
    document.addEventListener('fullscreenchange', onFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', onFullscreenChange);
  }, []);

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(e => console.log(e));
    } else {
        document.exitFullscreen();
    }
  };

  // UI STATE CONTROL
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
      if (messagesEndRef.current) {
          messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
      }
  }, [messages, liveTranscript, currentDraft, isProcessing, isRecording]);

  useEffect(() => {
    const handleNewPageImage = (e: any) => { 
        pendingImageRef.current = e.detail.split(',')[1]; 
    };
    window.addEventListener('tony-send-page-image', handleNewPageImage);
    return () => window.removeEventListener('tony-send-page-image', handleNewPageImage);
  }, []);

  // 🚀 KHỞI TẠO WEB SPEECH API ĐỂ CHẠY CHỮ NHÁP
  useEffect(() => {
      const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
      if (SpeechRecognition) {
          const recognition = new SpeechRecognition();
          recognition.continuous = true;
          recognition.interimResults = true;
          recognition.lang = 'en-GB'; 
          
          recognition.onresult = (event: any) => {
              let final = '';
              for (let i = event.resultIndex; i < event.results.length; ++i) {
                  if (event.results[i].isFinal) {
                      final += event.results[i][0].transcript;
                  }
              }
              if (final) {
                  setCurrentDraft(prev => prev + final + ' ');
              } else {
                  setCurrentDraft(event.results[event.results.length - 1][0].transcript);
              }
          };

          recognition.onerror = () => {};
          
          recognition.onend = () => {
              if (isMicOpenRef.current) {
                  try {
                      recognition.start();
                  } catch(e) {}
              }
          };
          
          recognitionRef.current = recognition;
      }
      return () => {
          if (recognitionRef.current) {
              recognitionRef.current.stop();
          }
      };
  }, []);

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
        ? `[KỶ LUẬT THÉP VÀ CÁCH TRÌNH BÀY BẢNG]: Bạn bắt buộc dùng văn phong chuẩn giọng miền Bắc (Hà Nội). Lời nói đang được chép lên bảng đen dạng Markdown. BẮT BUỘC dùng ký hiệu LaTeX ($...$ và $$...$$) để viết MỌI công thức toán học, và LUÔN LUÔN IN ĐẬM (**từ khóa**) các đáp án, danh từ riêng hoặc kết quả quan trọng để hệ thống tự vẽ bằng phấn vàng nổi bật.`
        : `[KỶ LUẬT THÉP]: Bạn bắt buộc dùng văn phong chuẩn giọng miền Bắc (Hà Nội). Trả lời ngắn gọn, tự nhiên. BẮT BUỘC dùng ký hiệu LaTeX ($...$ và $$...$$) cho công thức toán, và IN ĐẬM (**từ khóa**) các đáp án quan trọng để hệ thống tự vẽ bằng phấn vàng nổi bật.`;
        
        if (mode === 'TUTOR' && tutorData) {
            return `Bạn là ${teacherName}, người Hà Nội. BỐI CẢNH BÀI HỌC: ${tutorData.transcript}. NHIỆM VỤ: ${tutorData.feedback}. ${promptKienNhan} ${contextInstruction}`;
        } else {
            return `Bạn là giám khảo IELTS tên ${teacherName}, người Hà Nội. Hãy yêu cầu tôi nói về chủ đề: "${currentTopic}". Luôn lắng nghe và phản hồi trực tiếp dựa trên nội dung của thí sinh. ${promptKienNhan} ${contextInstruction}`;
        }
  };

  // =========================================================================================
  // 🚀 KẾT NỐI WEBSOCKET VOICE.TONYENGLISH.VN
  // =========================================================================================
  const startSession = async (isTextMode = false) => {
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

          // Chỉ lấy Micro nếu KHÔNG phải chế độ Chat Text
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
              
              // 🔥 SỬA LỖI Ở ĐÂY: LUÔN GỬI "AUDIO" ĐỂ MÁY CHỦ KHÔNG ĐÁ VĂNG
              ws.send(JSON.stringify({
                  setup: {
                      model: "models/gemini-3.1-flash-live-preview",
                      generationConfig: { 
                          responseModalities: ["AUDIO"], 
                          speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: voiceName } } } 
                      },
                      systemInstruction: { parts: [{ text: sysPrompt }] }
                  }
              }));

              if (!isTextMode && audioCtxInputRef.current && streamRef.current) {
                  sourceNodeRef.current = audioCtxInputRef.current.createMediaStreamSource(streamRef.current);
                  processorNodeRef.current = audioCtxInputRef.current.createScriptProcessor(4096, 1, 1);

                  processorNodeRef.current.onaudioprocess = (e) => {
                      if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN && isSetupCompleteRef.current && isMicOpenRef.current) {
                          const inputData = e.inputBuffer.getChannelData(0);
                          const pcm16Buffer = floatTo16BitPCM(inputData);
                          
                          wsRef.current.send(JSON.stringify({
                              realtimeInput: {
                                  audio: { 
                                      mimeType: "audio/pcm;rate=16000",
                                      data: arrayBufferToBase64(pcm16Buffer)
                                  }
                              }
                          }));
                      }
                  };

                  sourceNodeRef.current.connect(processorNodeRef.current);
                  processorNodeRef.current.connect(audioCtxInputRef.current.destination);
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

                  if (msg.serverContent || msg.response) {
                      const foundText = extractText(msg);
                      const hasModelTurnStarted = !!msg.serverContent?.modelTurn; 

                      if (hasModelTurnStarted || foundText) {
                          if (isMicOpenRef.current) {
                              isMicOpenRef.current = false;
                              isRecordingRef.current = false;
                              setIsRecording(false); 
                              
                              try { if (recognitionRef.current) recognitionRef.current.stop(); } catch(e){}

                              if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
                                  wsRef.current.send(JSON.stringify({ 
                                      clientContent: { turnComplete: true } 
                                  }));
                              }
                          }
                      }

                      if (foundText) {
                          transcriptRef.current += foundText;
                          setLiveTranscript(transcriptRef.current);
                      }

                      // CHỈ PHÁT AUDIO NẾU KHÔNG PHẢI CHẾ ĐỘ TEXT-ONLY
                      if (!isTextOnlyModeRef.current && msg.serverContent?.modelTurn?.parts) {
                          for (let part of msg.serverContent.modelTurn.parts) {
                              if (part.inlineData?.data) {
                                  playAIAudio(part.inlineData.data);
                              }
                          }
                      }
                  }

                  if (msg.serverContent?.turnComplete) {
                      if (transcriptRef.current) {
                          setMessages(prev => [...prev, { role: 'model', text: transcriptRef.current }]);
                          transcriptRef.current = '';
                          setLiveTranscript('');
                      }
                      setIsProcessing(false);
                      setIsSpeaking(false);
                  }
              } catch (e) {
                  console.error("Lỗi parse WS message:", e);
              }
          };

          ws.onclose = () => {
              setStatus('IDLE');
          };
      } catch (e) {
          alert("Lỗi: Không thể khởi tạo. Nếu dùng Voice, hãy cấp quyền Micro.");
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
  // 💬 XỬ LÝ CHAT TEXT TRONG BẢNG ĐEN
  // =========================================================================================
  const sendTextMessage = () => {
      const text = chatInput.trim();
      if (!text) return;
      
      if (isSpeaking) stopAIAudio(); 
      setIsProcessing(true);
      setMessages(prev => [...prev, { role: 'user', text: text }]);
      setChatInput('');

      if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
          let finalParts: any[] = [];
          if (pendingImageRef.current) {
              finalParts.push({ inlineData: { mimeType: "image/jpeg", data: pendingImageRef.current } });
              finalParts.push({ text: `[HỆ THỐNG]: Học sinh vừa lật sách và có nhắn tin như sau: "${text}". Hãy phân tích ảnh đính kèm và giải đáp nội dung tin nhắn.` });
              pendingImageRef.current = null;
          } else {
              finalParts.push({ text: text });
          }

          wsRef.current.send(JSON.stringify({
              clientContent: { turns: [{ role: "user", parts: finalParts }], turnComplete: true }
          }));
      } else {
          alert("Kết nối đang bị gián đoạn, vui lòng chờ...");
          setIsProcessing(false);
      }
  };

  // =========================================================================================
  // 🎙️ ĐIỀU KHIỂN VAN BỘ ĐÀM (PUSH-TO-TALK LÊN WEBSOCKET)
  // =========================================================================================
  const handleToggleRecording = () => {
      if (isSpeaking) {
          stopAIAudio(); 
      }
      
      if (isRecording) {
          isMicOpenRef.current = false;
          isRecordingRef.current = false;
          setIsRecording(false);
          setIsProcessing(true);
          
          try { 
              if (recognitionRef.current) recognitionRef.current.stop(); 
          } catch(e) {}

          if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
              const userTextHistory = currentDraft.trim() || "(Đã gửi đoạn hội thoại âm thanh)";
              setMessages(prev => [...prev, { role: 'user', text: userTextHistory }]);
              setCurrentDraft('');

              let finalParts: any[] = [];
              if (pendingImageRef.current) {
                  finalParts.push({ inlineData: { mimeType: "image/jpeg", data: pendingImageRef.current } });
                  finalParts.push({ text: "[HỆ THỐNG]: Học sinh vừa nói xong và có lật sách. Hãy phân tích ảnh đính kèm và phản hồi đoạn âm thanh trên." });
                  pendingImageRef.current = null;
              } else {
                  finalParts.push({ text: "[HỆ THỐNG]: Học sinh vừa nói xong. Hãy phản hồi." });
              }

              wsRef.current.send(JSON.stringify({
                  clientContent: { turns: [{ role: "user", parts: finalParts }], turnComplete: true }
              }));
          }
      } else {
          if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
              setCurrentDraft('');
              isMicOpenRef.current = true;
              isRecordingRef.current = true;
              setIsRecording(true);
              try { 
                  if (recognitionRef.current) recognitionRef.current.start(); 
              } catch(e) {}
          } else {
              alert("Kết nối đang bị gián đoạn, vui lòng chờ...");
          }
      }
  };

  const stopCall = () => {
    isMicOpenRef.current = false;
    isRecordingRef.current = false;
    setIsTextOnlyMode(false); 
    stopAIAudio();
    
    if (processorNodeRef.current) processorNodeRef.current.disconnect();
    if (sourceNodeRef.current) sourceNodeRef.current.disconnect();
    if (streamRef.current) streamRef.current.getTracks().forEach(t => t.stop());
    if (wsRef.current) wsRef.current.close();
    if (audioCtxInputRef.current && audioCtxInputRef.current.state !== 'closed') audioCtxInputRef.current.close();
    if (audioCtxOutputRef.current && audioCtxOutputRef.current.state !== 'closed') audioCtxOutputRef.current.close();
    
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
  };

  const handleUserHangUp = () => { 
      stopCall(); 
      sessionStorage.removeItem('tony_live_mode'); 
      sessionStorage.removeItem('tony_tutor_data'); 
      onClose(); 
  };

  // =========================================================================================
  // 🟢 GIAO DIỆN KHI THU NHỎ (MINIMIZED WIDGET ICON)
  // =========================================================================================
  if (viewState === 'MINIMIZED') {
      if (isBlackboardMode) {
          return (
              <button 
                  onClick={onMaximize} 
                  className={`fixed bottom-8 right-8 z-[100000] w-14 h-14 rounded-full flex items-center justify-center shadow-[0_10px_30px_rgba(0,0,0,0.5)] transition-all duration-300 hover:scale-110 active:scale-95 border-2 ${status === 'CONNECTED' ? (isRecording ? 'bg-red-500 border-red-300 animate-pulse' : (isSpeaking ? 'bg-sky-500 border-sky-300 animate-pulse' : 'bg-emerald-500 border-emerald-300')) : 'bg-indigo-600 border-indigo-400'}`} 
                  title="Mở Bảng Giáo Viên"
              >
                  <span className="text-2xl">{status === 'CONNECTED' ? (isTextOnlyMode ? '💬' : '🎙️') : '👨‍🏫'}</span>
              </button>
          );
      } else {
          return (
              <div className="fixed bottom-6 right-6 z-[99998] bg-slate-900/95 backdrop-blur-md border border-slate-700 shadow-[0_20px_50px_rgba(0,0,0,0.5)] rounded-[1.5rem] p-4 flex flex-col gap-3 w-[280px] md:w-80 animate-in slide-in-from-bottom-5 font-sans transition-all">
                 <div className="flex justify-between items-center">
                    <div className="flex items-center gap-2.5 cursor-pointer flex-1 min-w-0" onClick={onMaximize}>
                       <div className={`w-3 h-3 shrink-0 rounded-full ${isRecording ? 'bg-red-500 animate-pulse shadow-[0_0_10px_rgba(239,68,68,0.8)]' : (isSpeaking ? 'bg-sky-500 animate-pulse shadow-[0_0_10px_rgba(14,165,233,0.8)]' : (isProcessing ? 'bg-amber-500 animate-pulse' : 'bg-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.8)]'))}`}></div>
                       <span className="text-white font-semibold text-[13px] truncate">
                           {isRecording ? 'Đang truyền trực tiếp...' : (isProcessing ? 'AI đang phân tích...' : (isSpeaking ? 'Thầy cô đang nói...' : 'Sẵn sàng...'))}
                       </span>
                    </div>
                    <button onClick={onMaximize} className="text-slate-400 hover:text-white w-8 h-8 flex items-center justify-center bg-slate-800 rounded-full shrink-0 ml-2 border border-slate-600 shadow-sm transition-colors" title="Phóng to">↗️</button>
                 </div>
                 <div className="flex gap-2 mt-1">
                     {!isTextOnlyMode && (
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
                         className="flex-1 bg-slate-800 hover:bg-red-500 text-slate-300 hover:text-white font-bold py-2 rounded-xl text-[12px] md:text-[13px] transition-all flex items-center justify-center gap-2 border border-slate-600 hover:border-red-500"
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
  const currentMode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
  const currentTopic = sessionStorage.getItem('tony_live_topic') || "Bài tập giao tiếp tổng hợp";
  
  // -------------------------------------------------------------------------
  // 1️⃣ GIAO DIỆN BẢNG ĐEN (KHI MỞ SÁCH PDF)
  // -------------------------------------------------------------------------
  if (isBlackboardMode) {
      return (
        <>
          <style>{chalkboardStyleTag}</style>
          {status === 'IDLE' && <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[99998]" onClick={onMinimize} />}
          <div className="fixed top-0 right-0 h-[100dvh] w-full md:w-[50vw] bg-[#1a1c21] shadow-[-30px_0_60px_rgba(0,0,0,0.8)] z-[100000] flex flex-col border-l-[6px] border-[#2c1808]/80 animate-in slide-in-from-right duration-500">
            
            {/* Header */}
            <div className="h-14 bg-black/40 border-b border-white/5 flex items-center justify-between px-5 shrink-0 backdrop-blur-md">
              <div className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center text-sm border border-white/20">✏️</div>
                  <div className="flex flex-col">
                      <h3 className="font-bold text-[13px] text-slate-300 uppercase tracking-widest leading-none">Tony Blackboard</h3>
                  </div>
              </div>
              <div className="flex items-center gap-1">
                 {status === 'CONNECTED' && (
                     <button onClick={() => {setMessages([]); setCurrentDraft('');}} className="text-[11px] text-slate-400 hover:text-white bg-white/5 hover:bg-white/10 px-3 py-1.5 rounded-lg font-bold uppercase tracking-wide transition-colors mr-2 border border-white/10">Xóa Bảng</button>
                 )}
                 <button onClick={toggleFullscreen} className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/10 text-slate-400 transition-colors">🔲</button>
                 <button onClick={onMinimize} className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/10 text-slate-400 transition-colors">❌</button>
              </div>
            </div>
    
            <div className="flex-1 overflow-y-auto p-6 md:p-10 custom-scrollbar flex flex-col relative bg-[url('https://www.transparenttextures.com/patterns/black-paper.png')] pb-32">
              
              {/* MÀN HÌNH CHỜ (IDLE) - NÚT VÀO LỚP */}
              {status === 'IDLE' && (
                  <div className="m-auto text-center animate-in zoom-in-95 max-w-sm w-full bg-slate-900/80 p-8 rounded-[2rem] border border-slate-700/50 backdrop-blur-md shadow-2xl">
                     <div className="w-20 h-20 bg-gradient-to-tr from-[#0ea5e9] to-indigo-500 rounded-full flex items-center justify-center text-4xl shadow-lg border border-white/20 mx-auto mb-6">👨‍🏫</div>
                     <h3 className="text-xl font-black text-white mb-2 tracking-tight">Học Phần Gia Sư</h3>
                     <p className="text-[13px] text-slate-400 mb-8 font-medium">Vui lòng lựa chọn Thầy/Cô để mở kết nối đàm thoại giảng bài trực tiếp.</p>
                     
                     <div className="flex justify-center gap-4 mb-8">
                        <button onClick={() => setExaminer('TONY')} className={`flex-1 py-4 rounded-2xl border-2 flex flex-col items-center gap-2 transition-all duration-300 ${examiner === 'TONY' ? 'bg-[#0ea5e9]/20 border-[#0ea5e9] shadow-[0_0_20px_rgba(14,165,233,0.3)]' : 'bg-slate-800 border-slate-700 opacity-70 hover:opacity-100'}`}>
                            <span className="text-3xl drop-shadow-md">👨‍🏫</span>
                            <span className={`text-[12px] font-black uppercase tracking-widest ${examiner === 'TONY' ? 'text-[#0ea5e9]' : 'text-slate-400'}`}>Thầy Tôn</span>
                        </button>
                        <button onClick={() => setExaminer('DIEP')} className={`flex-1 py-4 rounded-2xl border-2 flex flex-col items-center gap-2 transition-all duration-300 ${examiner === 'DIEP' ? 'bg-[#0ea5e9]/20 border-[#0ea5e9] shadow-[0_0_20px_rgba(14,165,233,0.3)]' : 'bg-slate-800 border-slate-700 opacity-70 hover:opacity-100'}`}>
                            <span className="text-3xl drop-shadow-md">👩‍🏫</span>
                            <span className={`text-[12px] font-black uppercase tracking-widest ${examiner === 'DIEP' ? 'text-[#0ea5e9]' : 'text-slate-400'}`}>Cô Diệp</span>
                        </button>
                     </div>

                     <div className="flex flex-col gap-3">
                         <button onClick={() => startSession(false)} className="w-full bg-[#0ea5e9] hover:bg-[#0284c7] text-white font-black py-4 rounded-xl shadow-[0_10px_20px_rgba(14,165,233,0.3)] transition-all flex items-center justify-center gap-2 text-sm uppercase tracking-wide active:scale-95">
                             📞 Vào Lớp (Đàm Thoại Voice)
                         </button>
                         <button onClick={() => startSession(true)} className="w-full bg-slate-700 hover:bg-slate-600 text-white font-bold py-3 rounded-xl transition-all flex items-center justify-center gap-2 text-sm uppercase tracking-wide border border-slate-500">
                             📝 Vào Lớp (Chỉ Chat Nhắn Tin)
                         </button>
                     </div>
                  </div>
              )}
    
              {status === 'CONNECTING' && (
                  <div className="m-auto flex flex-col items-center opacity-70">
                      <div className="w-12 h-12 border-4 border-slate-700 border-t-[#0ea5e9] rounded-full animate-spin mb-4" />
                      <div className="text-slate-400 font-bold tracking-widest text-xs uppercase animate-pulse">Đang mời giáo viên vào lớp...</div>
                  </div>
              )}

              {status === 'CONNECTED' && (
                  <div className="tony-chalkboard-content flex-1 w-full text-left">
                      {messages.length === 0 && !isRecording && !liveTranscript && !currentDraft ? (
                          <div className="h-full flex flex-col items-center justify-center text-center opacity-30 italic text-slate-400" style={{fontFamily: 'sans-serif'}}>
                              <span className="text-4xl mb-4 grayscale">{isTextOnlyMode ? '💬' : '🎙️'}</span>
                              <span className="text-[15px] font-medium">Bảng đen trống.<br/>Gõ câu hỏi vào thanh công cụ bên dưới để hỏi bài.</span>
                          </div>
                      ) : (
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
                             
                             {isRecording && currentDraft && (
                                 <div className="mb-6 p-4 rounded-xl bg-white/10 border border-[#0ea5e9]/50 text-sky-300 animate-pulse">
                                     <strong className="text-xs uppercase tracking-widest opacity-50 block mb-2 font-sans">Đang ghi âm...</strong>
                                     {currentDraft}
                                 </div>
                             )}
                             
                             {isProcessing && !liveTranscript && (
                                 <div className="text-amber-300 italic animate-pulse font-sans">
                                     Thầy cô đang đọc câu hỏi và viết bảng...
                                 </div>
                             )}
                             <div ref={messagesEndRef} />
                          </>
                      )}
                  </div>
              )}
            </div>
            
            {/* THANH CONTROL BAR Ở DƯỚI BẢNG ĐEN */}
            {status === 'CONNECTED' && (
                <div className="absolute bottom-6 left-1/2 -translate-x-1/2 w-full max-w-2xl px-4 z-50">
                    {isTextOnlyMode && (
                        <p className="text-center text-[10px] uppercase tracking-widest text-sky-400 mb-2 font-bold animate-pulse">
                            💬 ĐANG Ở CHẾ ĐỘ CHAT VĂN BẢN (KHÔNG VOICE)
                        </p>
                    )}
                    {!isTextOnlyMode && (
                        <p className={`text-center text-[10px] uppercase tracking-widest mb-2 font-bold transition-colors ${isRecording ? 'text-red-400 animate-pulse' : 'text-slate-400'}`}>
                            {isRecording ? "🔴 ĐANG GHI ÂM (BẠN NÓI)" : (isProcessing ? "🧠 AI ĐANG SUY NGHĨ..." : (isSpeaking ? "🟢 THẦY CÔ ĐANG NÓI..." : "⏳ SẴN SÀNG LƯỢT TIẾP THEO"))}
                        </p>
                    )}
                    
                    <div className="bg-slate-900/95 backdrop-blur-md border border-slate-700/80 rounded-full p-2 flex items-center justify-between gap-3 shadow-[0_20px_40px_rgba(0,0,0,0.8)]">
                        
                        {/* Ô NHẬP TEXT CHAT TRỰC TIẾP TRONG BẢNG ĐEN */}
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
                               className="w-full bg-slate-800/80 text-white placeholder-slate-400 text-[14px] rounded-full px-4 py-2.5 border border-slate-600 focus:outline-none focus:border-[#0ea5e9] transition-colors"
                           />
                        </div>
                        
                        <div className="flex items-center gap-2 shrink-0 pr-1">
                            {!isTextOnlyMode ? (
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
          </div>
        </>
      );
  }

  // -------------------------------------------------------------------------
  // 2️⃣ NHÂN CÁCH 2: GIAO DIỆN BÌNH THƯỜNG (EDTECH STYLE)
  // -------------------------------------------------------------------------
  return (
    <div className="fixed inset-0 z-[9999] flex flex-col items-center justify-center min-h-[100dvh] bg-slate-900/90 backdrop-blur-md text-slate-200 p-4 md:p-8 w-full font-sans animate-in fade-in duration-300">
      
      {/* Cái nút mở Khung Chat Text (Sidebar) vẫn để dành cho giao diện thường */}
      {onOpenAI && !isChatBubbleVisible && (
          <button 
             onClick={() => {
                 if (onOpenAI) onOpenAI(currentMode === 'TUTOR' ? 'tutor' : 'ielts');
                 onMinimize();
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
                    <button onClick={() => setExaminer('TONY')} className={`relative flex-1 py-4 rounded-2xl flex flex-col items-center gap-2 border-2 transition-all duration-300 ${examiner === 'TONY' ? 'bg-[#0ea5e9]/10 border-[#0ea5e9] shadow-sm' : 'bg-white border-slate-200 text-slate-500 hover:border-[#0ea5e9]/50'}`}>
                       <div className="text-4xl drop-shadow-sm mb-1">👨‍🏫</div>
                       <span className={`text-[13px] font-black uppercase tracking-wider ${examiner === 'TONY' ? 'text-[#0ea5e9]' : 'text-slate-500'}`}>Thầy Tôn</span>
                    </button>
                    <button onClick={() => setExaminer('DIEP')} className={`relative flex-1 py-4 rounded-2xl flex flex-col items-center gap-2 border-2 transition-all duration-300 ${examiner === 'DIEP' ? 'bg-purple-500/10 border-purple-500 shadow-sm' : 'bg-white border-slate-200 text-slate-500 hover:border-purple-500/50'}`}>
                       <div className="text-4xl drop-shadow-sm mb-1">👩‍🏫</div>
                       <span className={`text-[13px] font-black uppercase tracking-wider ${examiner === 'DIEP' ? 'text-purple-600' : 'text-slate-500'}`}>Cô Diệp</span>
                    </button>
                </div>
             </div>
             
             <button onClick={() => startSession(false)} className="w-full shrink-0 bg-[#0ea5e9] hover:bg-[#0284c7] text-white font-black py-4 md:py-5 rounded-2xl text-[15px] md:text-[16px] shadow-[0_10px_30px_rgba(14,165,233,0.3)] flex items-center justify-center gap-3 active:scale-95 transition-all uppercase tracking-wide">
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
               {messages.length > 0 || isRecording || liveTranscript || currentDraft ? (
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
                      
                      {isRecording && currentDraft && (
                          <div className="p-3 rounded-lg bg-blue-50/50 text-blue-900 border border-blue-100/50 border-dashed animate-pulse">
                              <strong className="block text-[10px] uppercase tracking-widest opacity-50 mb-1">Đang ghi âm...</strong>
                              {currentDraft}
                          </div>
                      )}
                      <div ref={messagesEndRef} />
                  </div>
               ) : (
                  <div className="flex flex-col items-center justify-center h-full opacity-40">
                      <span className="text-3xl mb-2 grayscale">🎙️</span>
                      <span className="italic text-sm font-medium">Lịch sử trống.<br/>Nhấn nút bên dưới để bắt đầu nói.</span>
                  </div>
               )}
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