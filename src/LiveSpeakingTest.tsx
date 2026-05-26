import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import React, { useState, useRef, useEffect } from 'react';

// =========================================================================================
// 🚀 CSS: STYLE CHỮ PHẤN VIẾT TAY CHO CHẾ ĐỘ BẢNG ĐEN
// =========================================================================================
const chalkboardStyleTag = `
  @import url('https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&display=swap');
  .tony-chalkboard-content, .tony-chalkboard-content p, .tony-chalkboard-content span, .tony-chalkboard-content div, .tony-chalkboard-content li { font-family: 'Kalam', cursive !important; color: #f8fafc !important; font-size: 1.5rem !important; line-height: 1.8 !important; letter-spacing: 0.04em !important; text-shadow: 0px 1px 3px rgba(0,0,0,0.8) !important; }
  .tony-chalkboard-content p { margin-bottom: 1.2rem !important; }
  .tony-chalkboard-content strong, .tony-chalkboard-content b { color: #fef08a !important; font-weight: 700 !important; }
  .tony-chalkboard-content h1, .tony-chalkboard-content h2, .tony-chalkboard-content h3 { color: #67e8f9 !important; font-weight: 700 !important; margin-top: 1.8rem !important; margin-bottom: 0.6rem !important; }
  .tony-chalkboard-content .katex { font-family: KaTeX_Math, 'Times New Roman', serif !important; font-size: 1.5rem !important; color: #fef08a !important; }
`;

type ChatMessage = { role: 'user' | 'model'; text: string; };

// === HÀM HỖ TRỢ XỬ LÝ ÂM THANH PCM CHUẨN GỐC ===
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
    for (let i = 0; i < len; i++) bytes[i] = binary_string.charCodeAt(i);
    return bytes.buffer;
};

export default function LiveSpeakingTest({ viewState, onMinimize, onMaximize, onClose, onOpenAI }: { viewState: 'FULLSCREEN' | 'MINIMIZED', onMinimize: () => void, onMaximize: () => void, onClose: () => void, onOpenAI?: (passedMode?: string) => void }) {
  const [status, setStatus] = useState<'IDLE' | 'CONNECTING' | 'CONNECTED'>('IDLE');
  const [examiner, setExaminer] = useState<'TONY' | 'DIEP'>('TONY');
  
  const [isRecording, setIsRecording] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [liveTranscript, setLiveTranscript] = useState<string>('');
  const [currentDraft, setCurrentDraft] = useState<string>('');
  
  const [isBlackboardMode, setIsBlackboardMode] = useState(false);
  const [isChatBubbleVisible, setIsChatBubbleVisible] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);

  // REFS QUAN TRỌNG
  const wsRef = useRef<WebSocket | null>(null);
  const isSetupCompleteRef = useRef<boolean>(false);
  const isMicOpenRef = useRef<boolean>(false); // VAN BỘ ĐÀM
  const transcriptRef = useRef<string>('');
  const callStartTimeRef = useRef<number>(0);
  
  // Audio Input (Mic)
  const streamRef = useRef<MediaStream | null>(null);
  const audioCtxInputRef = useRef<AudioContext | null>(null);
  const sourceNodeRef = useRef<MediaStreamAudioSourceNode | null>(null);
  const processorNodeRef = useRef<ScriptProcessorNode | null>(null);
  const recognitionRef = useRef<any>(null); // Để hiển thị Text nháp
  
  // Audio Output (Loa)
  const audioCtxOutputRef = useRef<AudioContext | null>(null);
  const nextPlayTimeRef = useRef<number>(0);

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const pendingImageRef = useRef<string | null>(null);

  useEffect(() => {
    const onFullscreenChange = () => setIsFullscreen(!!document.fullscreenElement);
    document.addEventListener('fullscreenchange', onFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', onFullscreenChange);
  }, []);

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(e => console.log(e));
    else document.exitFullscreen();
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
          window.dispatchEvent(new CustomEvent('tony-teacher-board-state', { detail: hasPdf && viewState === 'FULLSCREEN' }));
      };
      checkMode();
      return () => window.dispatchEvent(new CustomEvent('tony-teacher-board-state', { detail: false }));
  }, [viewState]);

  useEffect(() => {
      if (messagesEndRef.current) messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
  }, [messages, liveTranscript, currentDraft, isProcessing, isRecording]);

  useEffect(() => {
    const handleNewPageImage = (e: any) => { pendingImageRef.current = e.detail.split(',')[1]; };
    window.addEventListener('tony-send-page-image', handleNewPageImage);
    return () => window.removeEventListener('tony-send-page-image', handleNewPageImage);
  }, []);

  // KHỞI TẠO BỘ NGHE NHÁP (Chỉ để hiện UI, không gửi lên Google)
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
                  if (event.results[i].isFinal) final += event.results[i][0].transcript;
              }
              if (final) setCurrentDraft(prev => prev + final + ' ');
              else setCurrentDraft(event.results[event.results.length - 1][0].transcript);
          };

          recognition.onerror = () => {};
          recognitionRef.current = recognition;
      }
      return () => {
          if (recognitionRef.current) recognitionRef.current.stop();
      };
  }, []);

  const handleBackClick = () => {
    if (status !== 'IDLE') onMinimize();
    else { sessionStorage.removeItem('tony_live_mode'); sessionStorage.removeItem('tony_tutor_data'); onClose(); }
  };

  const buildSystemPrompt = () => {
        const mode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
        const tutorDataRaw = sessionStorage.getItem('tony_tutor_data');
        const tutorData = tutorDataRaw ? JSON.parse(tutorDataRaw) : null;
        const currentTopic = sessionStorage.getItem('tony_live_topic') || "Bài tập giao tiếp tổng hợp";
        const teacherName = examiner === 'TONY' ? 'thầy Tôn' : 'cô Diệp';

        const hiddenContextRaw = sessionStorage.getItem('tony_lecture_context') || '';
        const cleanTextContext = hiddenContextRaw.replace(/\[IMAGE_ANSWER:\s*(https?:\/\/[^\]]+)\]/g, '[CÓ BỨC ẢNH ĐÁP ÁN ĐÍNH KÈM]').trim();
        const contextInstruction = cleanTextContext ? `\n\n[TÀI LIỆU DÀNH CHO BẠN ĐỂ DẠY HỌC SINH]:\n"""\n${cleanTextContext}\n"""` : '';

        let promptKienNhan = isBlackboardMode 
        ? `[KỶ LUẬT THÉP VÀ CÁCH TRÌNH BÀY BẢNG]: Bạn bắt buộc dùng văn phong chuẩn giọng miền Bắc (Hà Nội). Lời nói đang được phát lại cho học sinh nghe. Đồng thời lời nói cũng đang được viết lên bảng đen. Dùng ký hiệu LaTeX ($...$ và $$...$$) để viết mọi công thức toán học.`
        : `[KỶ LUẬT THÉP]: Bạn bắt buộc dùng văn phong chuẩn giọng miền Bắc (Hà Nội). Trả lời ngắn gọn, tự nhiên. Dùng ký hiệu LaTeX ($...$ và $$...$$) cho công thức toán.`;
        
        if (mode === 'TUTOR' && tutorData) {
            return `Bạn là ${teacherName}, người Hà Nội. BỐI CẢNH BÀI HỌC: ${tutorData.transcript}. NHIỆM VỤ: ${tutorData.feedback}. ${promptKienNhan} ${contextInstruction}`;
        } else {
            return `Bạn là giám khảo IELTS tên ${teacherName}, người Hà Nội. Hãy yêu cầu thí sinh nói về chủ đề: "${currentTopic}". Lắng nghe và đánh giá tự nhiên. ${promptKienNhan} ${contextInstruction}`;
        }
  };

  // =========================================================================================
  // 🚀 KẾT NỐI WEBSOCKET VOICE.TONYENGLISH.VN VÀ MỞ LUỒNG MIC
  // =========================================================================================
  const startSession = async () => {
      setStatus('CONNECTING');
      setMessages([]);
      transcriptRef.current = '';
      setLiveTranscript('');
      isMicOpenRef.current = false;
      isSetupCompleteRef.current = false;
      callStartTimeRef.current = Date.now();
      
      if (!isBlackboardMode) onMinimize();

      try {
          // 1. CHUẨN BỊ MIC & AUDIO CONTEXT
          streamRef.current = await navigator.mediaDevices.getUserMedia({ audio: true });
          const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
          audioCtxInputRef.current = new AudioContextClass({ sampleRate: 16000 });
          audioCtxOutputRef.current = new AudioContextClass({ sampleRate: 24000 });
          
          if (audioCtxInputRef.current.state === 'suspended') await audioCtxInputRef.current.resume();
          if (audioCtxOutputRef.current.state === 'suspended') await audioCtxOutputRef.current.resume();
          nextPlayTimeRef.current = audioCtxOutputRef.current.currentTime;

          // 2. KẾT NỐI WEBSOCKET
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
                      systemInstruction: { parts: [{ text: sysPrompt }] }
                  }
              }));

              // 3. THIẾT LẬP BỘ LỌC ÂM THANH (VAN BỘ ĐÀM)
              sourceNodeRef.current = audioCtxInputRef.current!.createMediaStreamSource(streamRef.current!);
              processorNodeRef.current = audioCtxInputRef.current!.createScriptProcessor(4096, 1, 1);

              processorNodeRef.current.onaudioprocess = (e) => {
                  // 🚨 KHÔI PHỤC KEY "audio" THEO CHUẨN GỐC CỦA ANH
                  if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN && isSetupCompleteRef.current && isMicOpenRef.current) {
                      const inputData = e.inputBuffer.getChannelData(0);
                      const pcm16Buffer = floatTo16BitPCM(inputData);
                      wsRef.current.send(JSON.stringify({
                          realtimeInput: {
                              audio: { // Chìa khóa ở đây ạ!
                                  mimeType: "audio/pcm;rate=16000",
                                  data: arrayBufferToBase64(pcm16Buffer)
                              }
                          }
                      }));
                  }
              };

              sourceNodeRef.current.connect(processorNodeRef.current);
              processorNodeRef.current.connect(audioCtxInputRef.current!.destination);
          };

          ws.onmessage = async (event) => {
              try {
                  let rawData = event.data;
                  if (rawData instanceof Blob) rawData = await rawData.text();
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
                  
                  // 🚨 KHÔI PHỤC HÀM "BÓC CHỮ" THẦN THÁNH BẢN GỐC
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
                          setLiveTranscript(transcriptRef.current);
                      }

                      if (msg.serverContent?.modelTurn?.parts) {
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
              } catch (e) {}
          };

          ws.onclose = () => { setStatus('IDLE'); };
      } catch (e) {
          alert("Lỗi: Không thể truy cập Micro. Vui lòng cấp quyền cho trình duyệt.");
          setStatus('IDLE');
      }
  };

  const playAIAudio = (base64Audio: string) => {
      if (!audioCtxOutputRef.current) return;
      const ctx = audioCtxOutputRef.current;
      
      const pcmBuffer = base64ToArrayBuffer(base64Audio);
      const int16Array = new Int16Array(pcmBuffer);
      const float32Array = new Float32Array(int16Array.length);
      for (let i = 0; i < int16Array.length; i++) float32Array[i] = int16Array[i] / 32768.0;
      
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
  // 🎙️ ĐIỀU KHIỂN VAN BỘ ĐÀM (PUSH-TO-TALK LÊN WEBSOCKET)
  // =========================================================================================
  const handleToggleRecording = () => {
      if (isSpeaking) stopAIAudio(); 
      
      if (isRecording) {
          // BẤM NÚT "XONG": ĐÓNG VAN & GỬI LỆNH CHỐT
          isMicOpenRef.current = false;
          setIsRecording(false);
          setIsProcessing(true);
          
          try { recognitionRef.current?.stop(); } catch(e) {}

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
          // BẤM NÚT "NHẤN NÓI": MỞ VAN CHO ÂM THANH CHẢY LÊN WEBSOCKET
          if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
              setCurrentDraft('');
              isMicOpenRef.current = true;
              setIsRecording(true);
              try { recognitionRef.current?.start(); } catch(e) {}
          } else {
              alert("Kết nối đang bị gián đoạn, vui lòng chờ...");
          }
      }
  };

  const stopCall = () => {
    isMicOpenRef.current = false;
    if (processorNodeRef.current) processorNodeRef.current.disconnect();
    if (sourceNodeRef.current) sourceNodeRef.current.disconnect();
    if (streamRef.current) streamRef.current.getTracks().forEach(t => t.stop());
    if (wsRef.current) wsRef.current.close();
    
    if (audioCtxInputRef.current && audioCtxInputRef.current.state !== 'closed') audioCtxInputRef.current.close();
    if (audioCtxOutputRef.current && audioCtxOutputRef.current.state !== 'closed') audioCtxOutputRef.current.close();
    
    setStatus('IDLE'); setIsRecording(false);
  };

  const handleUserHangUp = () => { stopCall(); sessionStorage.removeItem('tony_live_mode'); sessionStorage.removeItem('tony_tutor_data'); onClose(); };

  // =========================================================================================
  // 🟢 GIAO DIỆN KHI THU NHỎ (MINIMIZED WIDGET ICON)
  // =========================================================================================
  if (viewState === 'MINIMIZED') {
      if (isBlackboardMode) {
          return (
              <button onClick={onMaximize} className={`fixed bottom-8 right-8 z-[100000] w-14 h-14 rounded-full flex items-center justify-center shadow-[0_10px_30px_rgba(0,0,0,0.5)] transition-all duration-300 hover:scale-110 active:scale-95 border-2 ${status === 'CONNECTED' ? (isRecording ? 'bg-red-500 border-red-300 animate-pulse' : (isSpeaking ? 'bg-sky-500 border-sky-300 animate-pulse' : 'bg-emerald-500 border-emerald-300')) : 'bg-indigo-600 border-indigo-400'}`} title="Mở Bảng Giáo Viên">
                  <span className="text-2xl">{status === 'CONNECTED' ? '🎙️' : '👨‍🏫'}</span>
              </button>
          );
      } else {
          return (
              <div className="fixed bottom-6 right-6 z-[99998] bg-slate-900/95 backdrop-blur-md border border-slate-700 shadow-[0_20px_50px_rgba(0,0,0,0.5)] rounded-[1.5rem] p-4 flex flex-col gap-3 w-[280px] md:w-80 animate-in slide-in-from-bottom-5 font-sans transition-all">
                 <div className="flex justify-between items-center">
                    <div className="flex items-center gap-2.5 cursor-pointer flex-1 min-w-0" onClick={onMaximize}>
                       <div className={`w-3 h-3 shrink-0 rounded-full ${isRecording ? 'bg-red-500 animate-pulse shadow-[0_0_10px_rgba(239,68,68,0.8)]' : (isSpeaking ? 'bg-sky-500 animate-pulse shadow-[0_0_10px_rgba(14,165,233,0.8)]' : (isProcessing ? 'bg-amber-500 animate-pulse' : 'bg-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.8)]'))}`}></div>
                       <span className="text-white font-semibold text-[13px] truncate">{isRecording ? 'Đang truyền trực tiếp...' : (isProcessing ? 'AI đang phân tích...' : (isSpeaking ? 'Thầy cô đang nói...' : 'Sẵn sàng...'))}</span>
                    </div>
                    <button onClick={onMaximize} className="text-slate-400 hover:text-white w-8 h-8 flex items-center justify-center bg-slate-800 rounded-full shrink-0 ml-2 border border-slate-600 shadow-sm transition-colors" title="Phóng to">↗️</button>
                 </div>
                 <div className="flex gap-2 mt-1">
                     <button onClick={handleToggleRecording} disabled={isProcessing} className={`flex-1 font-bold py-2 rounded-xl text-[12px] md:text-[13px] transition-all flex items-center justify-center gap-2 disabled:opacity-50 ${isRecording ? 'bg-red-500 hover:bg-red-600 text-white shadow-md shadow-red-900/50' : 'bg-[#0ea5e9] hover:bg-sky-500 text-white shadow-md shadow-sky-900/50'}`}>
                        {isRecording ? '⏹️ Xong' : (isSpeaking ? '⏹️ Ngắt lời' : '🎙️ Nhấn nói')}
                     </button>
                     <button onClick={handleUserHangUp} className="flex-1 bg-slate-800 hover:bg-red-500 text-slate-300 hover:text-white font-bold py-2 rounded-xl text-[12px] md:text-[13px] transition-all flex items-center justify-center gap-2 border border-slate-600 hover:border-red-500">🛑 Dập máy</button>
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
  const handleYellowButtonClick = () => { if (onOpenAI) onOpenAI(currentMode === 'TUTOR' ? 'tutor' : 'ielts'); };

  if (isBlackboardMode) {
      return (
        <>
          <style>{chalkboardStyleTag}</style>
          {status === 'IDLE' && <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[99998]" onClick={onMinimize} />}
          <div className="fixed top-0 right-0 h-[100dvh] w-full md:w-[50vw] bg-[#1a1c21] shadow-[-30px_0_60px_rgba(0,0,0,0.8)] z-[100000] flex flex-col border-l-[6px] border-[#2c1808]/80 animate-in slide-in-from-right duration-500">
            <div className="h-14 bg-black/40 border-b border-white/5 flex items-center justify-between px-5 shrink-0 backdrop-blur-md">
              <div className="flex items-center gap-3"><div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center text-sm border border-white/20">✏️</div><div className="flex flex-col"><h3 className="font-bold text-[13px] text-slate-300 uppercase tracking-widest leading-none">Tony Blackboard</h3></div></div>
              <div className="flex items-center gap-1">
                 {status === 'CONNECTED' && <button onClick={() => {setMessages([]); setCurrentDraft('');}} className="text-[11px] text-slate-400 hover:text-white bg-white/5 hover:bg-white/10 px-3 py-1.5 rounded-lg font-bold uppercase tracking-wide transition-colors mr-2 border border-white/10">Xóa Bảng</button>}
                 <button onClick={toggleFullscreen} className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/10 text-slate-400 transition-colors">🔲</button>
                 <button onClick={onMinimize} className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/10 text-slate-400 transition-colors">❌</button>
              </div>
            </div>
    
            <div className="flex-1 overflow-y-auto p-6 md:p-10 custom-scrollbar flex flex-col relative bg-[url('https://www.transparenttextures.com/patterns/black-paper.png')]">
              {status === 'IDLE' && (
                  <div className="m-auto text-center animate-in zoom-in-95 max-w-sm w-full bg-slate-900/80 p-8 rounded-[2rem] border border-slate-700/50 backdrop-blur-md shadow-2xl">
                     <div className="w-20 h-20 bg-gradient-to-tr from-[#0ea5e9] to-indigo-500 rounded-full flex items-center justify-center text-4xl shadow-lg border border-white/20 mx-auto mb-6">👨‍🏫</div>
                     <h3 className="text-xl font-black text-white mb-2 tracking-tight">Học Phần Gia Sư</h3>
                     <p className="text-[13px] text-slate-400 mb-8 font-medium">Vui lòng lựa chọn Thầy/Cô để mở kết nối đàm thoại (Truyền âm qua WebSocket).</p>
                     <div className="flex justify-center gap-4 mb-8">
                        <button onClick={() => setExaminer('TONY')} className={`flex-1 py-4 rounded-2xl border-2 flex flex-col items-center gap-2 transition-all duration-300 ${examiner === 'TONY' ? 'bg-[#0ea5e9]/20 border-[#0ea5e9] shadow-[0_0_20px_rgba(14,165,233,0.3)]' : 'bg-slate-800 border-slate-700 opacity-70 hover:opacity-100'}`}><span className="text-3xl drop-shadow-md">👨‍🏫</span><span className={`text-[12px] font-black uppercase tracking-widest ${examiner === 'TONY' ? 'text-[#0ea5e9]' : 'text-slate-400'}`}>Thầy Tôn</span></button>
                        <button onClick={() => setExaminer('DIEP')} className={`flex-1 py-4 rounded-2xl border-2 flex flex-col items-center gap-2 transition-all duration-300 ${examiner === 'DIEP' ? 'bg-[#0ea5e9]/20 border-[#0ea5e9] shadow-[0_0_20px_rgba(14,165,233,0.3)]' : 'bg-slate-800 border-slate-700 opacity-70 hover:opacity-100'}`}><span className="text-3xl drop-shadow-md">👩‍🏫</span><span className={`text-[12px] font-black uppercase tracking-widest ${examiner === 'DIEP' ? 'text-[#0ea5e9]' : 'text-slate-400'}`}>Cô Diệp</span></button>
                     </div>
                     <button onClick={startSession} className="w-full bg-[#0ea5e9] hover:bg-[#0284c7] text-white font-black py-4 rounded-xl shadow-[0_10px_20px_rgba(14,165,233,0.3)] transition-all flex items-center justify-center gap-2 text-sm uppercase tracking-wide active:scale-95">📞 Bắt Đầu Đàm Thoại</button>
                  </div>
              )}
    
              {status === 'CONNECTING' && (
                  <div className="m-auto flex flex-col items-center opacity-70">
                      <div className="w-12 h-12 border-4 border-slate-700 border-t-[#0ea5e9] rounded-full animate-spin mb-4" />
                      <div className="text-slate-400 font-bold tracking-widest text-xs uppercase animate-pulse">Đang kết nối WebSocket...</div>
                  </div>
              )}

              {status === 'CONNECTED' && (
                  <div className="tony-chalkboard-content flex-1 w-full text-left pb-32">
                      {messages.length === 0 && !isRecording && !liveTranscript ? (
                          <div className="h-full flex flex-col items-center justify-center text-center opacity-30 italic text-slate-400" style={{fontFamily: 'sans-serif'}}>
                              <span className="text-4xl mb-4 grayscale">🎙️</span><span className="text-[15px] font-medium">Bảng đen trống.<br/>Nhấn nút bên dưới để bắt đầu nói.</span>
                          </div>
                      ) : (
                          <>
                             {messages.map((m, i) => (
                                 <div key={i} className={`mb-6 p-4 rounded-xl ${m.role === 'user' ? 'bg-white/5 border border-white/10 text-sky-200' : 'text-white'}`}>
                                     <strong className="text-xs uppercase tracking-widest opacity-50 block mb-2 font-sans">{m.role === 'user' ? 'Em nói:' : (examiner === 'TONY' ? 'Thầy Tôn:' : 'Cô Diệp:')}</strong>
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
                                     <strong className="text-xs uppercase tracking-widest opacity-50 block mb-2 font-sans">Đang ghi âm...</strong>{currentDraft}
                                 </div>
                             )}
                             {isProcessing && !liveTranscript && <div className="text-amber-300 italic animate-pulse font-sans">Thầy cô đang phân tích giọng và viết bảng...</div>}
                             <div ref={messagesEndRef} />
                          </>
                      )}
                  </div>
              )}
            </div>
            
            {status === 'CONNECTED' && (
                <div className="absolute bottom-6 left-1/2 -translate-x-1/2 w-full max-w-sm px-4 z-50">
                    <div className="bg-slate-900/95 backdrop-blur-md border border-slate-700/80 rounded-full py-2 px-3 flex items-center justify-between gap-3 shadow-[0_20px_40px_rgba(0,0,0,0.8)]">
                        <div className="flex-1">
                            <button onClick={handleToggleRecording} disabled={isProcessing} className={`w-full py-2.5 rounded-full font-bold text-xs uppercase tracking-widest transition-all disabled:opacity-50 shadow-md ${isRecording ? 'bg-red-500 text-white shadow-red-500/50' : (isSpeaking ? 'bg-sky-500 text-white' : 'bg-[#0ea5e9] text-white hover:bg-sky-500')}`}>
                                {isRecording ? '⏹️ Xong. Phân tích đi' : (isSpeaking ? '⏹️ Ngắt lời Thầy/Cô' : '🎙️ Nhấn để hỏi bài')}
                            </button>
                        </div>
                        <button onClick={handleUserHangUp} className="w-10 h-10 bg-red-500/20 hover:bg-red-500 text-red-500 hover:text-white rounded-full flex items-center justify-center transition-all active:scale-95 border border-red-500/50" title="Kết thúc đàm thoại">❌</button>
                    </div>
                </div>
            )}
          </div>
        </>
      );
  }

  return (
    <div className="fixed inset-0 z-[9999] flex flex-col items-center justify-center min-h-[100dvh] bg-slate-900/90 backdrop-blur-md text-slate-200 p-4 md:p-8 w-full font-sans animate-in fade-in duration-300">
      {onOpenAI && !isChatBubbleVisible && (
          <button onClick={handleYellowButtonClick} className="absolute top-4 right-4 md:top-6 md:right-6 text-white hover:text-white transition-all flex items-center gap-2 font-bold bg-gradient-to-r from-amber-500 to-orange-500 px-4 py-2.5 md:px-5 md:py-3 rounded-2xl shadow-[0_10px_25px_rgba(245,158,11,0.3)] z-20 hover:scale-105 active:scale-95 hover:shadow-[0_15px_35px_rgba(245,158,11,0.4)]" title="Mở khung chat Text">
             <span className="text-xl drop-shadow-sm">💬</span> <span className="hidden sm:inline text-[13px] md:text-[14px] drop-shadow-sm uppercase tracking-wider">{currentMode === 'TUTOR' ? 'Mở khung chat' : 'Kịch bản AI'}</span>
          </button>
      )}

      <div className="bg-white p-6 md:p-10 rounded-[2.5rem] shadow-[0_30px_80px_rgba(0,0,0,0.5)] max-w-[600px] w-full text-center relative z-10 max-h-[90dvh] flex flex-col my-auto overflow-hidden ring-1 ring-slate-900/5">
        <button onClick={handleBackClick} className="absolute top-6 left-6 text-slate-500 hover:text-slate-800 bg-slate-100 hover:bg-slate-200 px-4 py-2.5 rounded-xl text-[13px] font-bold transition-all shadow-sm border border-slate-200 z-20 flex items-center gap-2 uppercase tracking-wide">
          {status !== 'IDLE' ? '⬇ Thu nhỏ' : '🚪 Thoát'}
        </button>

        <div className="mb-8 mt-12 md:mt-10 shrink-0">
           <h2 className="text-2xl md:text-[32px] font-black mb-2 text-slate-800 tracking-tight leading-tight">{currentMode === 'TUTOR' ? 'Gia Sư Giải Đáp 1-1' : 'Phòng Luyện Nói 1-1'}</h2>
           <p className="text-[#0ea5e9] font-bold text-[13px] md:text-[15px] uppercase tracking-widest">{currentMode === 'TUTOR' ? 'Phân tích nội dung bài học cùng chuyên gia' : 'Đàm thoại trực tiếp với Giám khảo IELTS'}</p>
        </div>

        {status === 'IDLE' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 overflow-y-auto custom-scrollbar flex-1 pb-2 px-2">
             <div className="bg-slate-50 p-5 md:p-6 rounded-2xl border border-slate-200 mb-8 text-left shadow-sm flex flex-col">
                <span className="block text-[11px] uppercase tracking-widest text-slate-500 font-bold mb-2 shrink-0">Chủ đề đàm thoại:</span>
                <div className="text-[15px] font-semibold text-slate-800 whitespace-pre-wrap leading-relaxed">{currentMode === 'TUTOR' ? "Chữa bài & Giải đáp thắc mắc chuyên sâu" : `"${currentTopic}"`}</div>
             </div>
             
             <div className="mb-8 shrink-0">
                <h3 className="text-[12px] font-black text-slate-400 uppercase tracking-widest mb-4">Lựa chọn Giám khảo</h3>
                <div className="flex justify-center gap-4">
                    <button onClick={() => setExaminer('TONY')} className={`relative flex-1 py-4 rounded-2xl flex flex-col items-center gap-2 border-2 transition-all duration-300 ${examiner === 'TONY' ? 'bg-[#0ea5e9]/10 border-[#0ea5e9] shadow-sm' : 'bg-white border-slate-200 text-slate-500 hover:border-[#0ea5e9]/50'}`}>
                       <div className="text-4xl drop-shadow-sm mb-1">👨‍🏫</div><span className={`text-[13px] font-black uppercase tracking-wider ${examiner === 'TONY' ? 'text-[#0ea5e9]' : 'text-slate-500'}`}>Thầy Tôn</span>
                    </button>
                    <button onClick={() => setExaminer('DIEP')} className={`relative flex-1 py-4 rounded-2xl flex flex-col items-center gap-2 border-2 transition-all duration-300 ${examiner === 'DIEP' ? 'bg-purple-500/10 border-purple-500 shadow-sm' : 'bg-white border-slate-200 text-slate-500 hover:border-purple-500/50'}`}>
                       <div className="text-4xl drop-shadow-sm mb-1">👩‍🏫</div><span className={`text-[13px] font-black uppercase tracking-wider ${examiner === 'DIEP' ? 'text-purple-600' : 'text-slate-500'}`}>Cô Diệp</span>
                    </button>
                </div>
             </div>
             <button onClick={startSession} className="w-full shrink-0 bg-[#0ea5e9] hover:bg-[#0284c7] text-white font-black py-4 md:py-5 rounded-2xl text-[15px] md:text-[16px] shadow-[0_10px_30px_rgba(14,165,233,0.3)] flex items-center justify-center gap-3 active:scale-95 transition-all uppercase tracking-wide">
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
                <div className="text-slate-500 font-black tracking-widest uppercase text-sm animate-pulse">Đang kết nối WebSocket...</div>
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
            
            <p className={`shrink-0 font-black mb-6 tracking-widest uppercase text-[10px] md:text-[11px] px-4 py-1.5 rounded-full border shadow-sm transition-colors ${isRecording ? 'bg-red-50 text-red-600 border-red-200' : (isSpeaking ? 'bg-sky-50 text-[#0ea5e9] border-sky-200 animate-pulse' : 'bg-slate-50 text-slate-500 border-slate-200')}`}>
                {isRecording ? "🔴 ĐANG THU ÂM TRỰC TIẾP" : (isProcessing && !liveTranscript ? "🧠 AI ĐANG SUY NGHĨ..." : (isSpeaking || liveTranscript ? "🟢 THẦY CÔ ĐANG NÓI..." : "⏳ SẴN SÀNG LƯỢT TIẾP THEO"))}
            </p>
            
            <div className="bg-slate-50 rounded-2xl p-5 md:p-6 w-full text-left h-32 md:h-48 overflow-y-auto mb-8 border border-slate-200 shadow-inner custom-scrollbar flex-1 min-h-[140px]">
               {messages.length > 0 || isRecording || liveTranscript ? (
                  <div className="prose prose-slate prose-sm max-w-none font-medium text-slate-700 leading-relaxed space-y-4">
                      {messages.map((m, i) => (
                          <div key={i} className={`p-3 rounded-lg ${m.role === 'user' ? 'bg-blue-50 text-blue-900 border border-blue-100' : 'bg-white border border-slate-200'}`}>
                              <strong className="block text-[10px] uppercase tracking-widest opacity-50 mb-1">{m.role === 'user' ? 'Ghi âm của em:' : 'Giám khảo:'}</strong>
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
                              <strong className="block text-[10px] uppercase tracking-widest opacity-50 mb-1">Đang ghi âm...</strong>{currentDraft}
                          </div>
                      )}
                      <div ref={messagesEndRef} />
                  </div>
               ) : (
                  <div className="flex flex-col items-center justify-center h-full opacity-40">
                      <span className="text-3xl mb-2 grayscale">🎙️</span><span className="italic text-sm font-medium">Lịch sử trống.<br/>Nhấn nút bên dưới để bắt đầu nói.</span>
                  </div>
               )}
            </div>
            
            <div className="flex flex-col sm:flex-row gap-3 md:gap-4 w-full shrink-0">
                <button onClick={handleToggleRecording} disabled={isProcessing && !liveTranscript} className={`flex-1 font-black py-4 rounded-xl flex items-center justify-center gap-2 transition-all active:scale-95 shadow-md border-2 text-[13px] uppercase tracking-wide disabled:opacity-50 ${isRecording ? 'bg-red-500 text-white border-red-500 shadow-red-500/30' : (isSpeaking ? 'bg-sky-500 text-white border-sky-500' : 'bg-[#0ea5e9] text-white border-[#0ea5e9] hover:bg-sky-500')}`}>
                   <span className="text-xl">{isRecording ? '⏹️' : (isSpeaking ? '⏹️' : '🎙️')}</span> {isRecording ? 'Gửi trả lời' : (isSpeaking ? 'Ngắt lời' : 'Nhấn nói')}
                </button>
                <button onClick={handleUserHangUp} className="flex-1 bg-white hover:bg-red-50 text-red-500 font-black py-4 rounded-xl flex items-center justify-center gap-2 active:scale-95 transition-all border-2 border-red-200 hover:border-red-500 text-[13px] uppercase tracking-wide shadow-sm">
                    🚪 Rời phòng
                </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}