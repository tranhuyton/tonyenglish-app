import React, { useState, useRef, useEffect } from 'react';

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
// COMPONENT PHÒNG LIVE TỐI THƯỢNG
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

  // KIỂM TRA LỆNH GỌI TỰ ĐỘNG NGAY KHI VỪA MỞ CỬA SỔ LÊN
  useEffect(() => {
      const autoStart = sessionStorage.getItem('tony_auto_start') === 'true';
      
      if (autoStart) {
          sessionStorage.removeItem('tony_auto_start');
          
          const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
          if (isMobile) {
              return; 
          }
          
          if (pendingCallTimeoutRef.current) clearTimeout(pendingCallTimeoutRef.current);
          pendingCallTimeoutRef.current = setTimeout(() => {
              if (startCallRef.current) {
                  startCallRef.current(false);
              }
          }, 500);
      }
  }, []);

  // RADAR THÔNG MINH BẮT TÍN HIỆU
  useEffect(() => {
    const handleNavigationEvent = (e: any) => {
        if (e.detail === 'live-test') {
            onMaximize(); 
            const autoStart = sessionStorage.getItem('tony_auto_start') === 'true';
            
            if (autoStart) {
                sessionStorage.removeItem('tony_auto_start');
                
                const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
                if (isMobile) {
                    if (statusRef.current === 'CONNECTED' || statusRef.current === 'CONNECTING') {
                        if (stopCallRef.current) stopCallRef.current();
                    }
                    return; 
                }

                if (pendingCallTimeoutRef.current) clearTimeout(pendingCallTimeoutRef.current);
                if (reconnectTimeoutRef.current) clearTimeout(reconnectTimeoutRef.current);
                
                if (statusRef.current === 'CONNECTED' || statusRef.current === 'CONNECTING') {
                    if (stopCallRef.current) stopCallRef.current();
                    pendingCallTimeoutRef.current = setTimeout(() => {
                        if (startCallRef.current) startCallRef.current(false);
                    }, 500);
                } else {
                    pendingCallTimeoutRef.current = setTimeout(() => {
                        if (startCallRef.current) startCallRef.current(false);
                    }, 300);
                }
            }
        }
    };
    
    window.addEventListener('tony-navigate', handleNavigationEvent);
    
    return () => {
        window.removeEventListener('tony-navigate', handleNavigationEvent);
    };
  }, [onMaximize]);

  const toggleMute = () => {
      isMutedRef.current = !isMutedRef.current;
      setIsMuted(isMutedRef.current);
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
        const voiceName = examiner === 'TONY' ? 'Puck' : 'Aoede';
        const teacherName = examiner === 'TONY' ? 'thầy Tôn' : 'cô Diệp';

        const mode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
        const tutorDataRaw = sessionStorage.getItem('tony_tutor_data');
        const tutorData = tutorDataRaw ? JSON.parse(tutorDataRaw) : null;
        const currentTopic = sessionStorage.getItem('tony_live_topic') || "Bài tập giao tiếp tổng hợp";

        let systemPrompt = "";
        
        // Cấu hình kiểm soát khoảng lặng, tối ưu cho phản hồi Realtime qua VPS riêng
        const promptKienNhan = `[KỶ LUẬT THÉP]: Người dùng đang luyện nói tiếng Anh nên tốc độ sẽ chậm, hay ngập ngừng và thường xuyên dừng lại để suy nghĩ từ vựng. BẠN PHẢI TUYỆT ĐỐI KIÊN NHẪN. Không bao giờ được cướp lời hoặc ngắt lời. Dù có khoảng lặng 2-3 giây, hãy kiên nhẫn đợi đến khi chắc chắn người dùng đã nói xong hoàn toàn ý của họ mới được phản hồi. Tốc độ nói của bạn cũng phải chậm rãi, điềm đạm và từ tốn.`;
        
        if (mode === 'TUTOR' && tutorData) {
            if (isReconnect && transcriptRef.current) {
                systemPrompt = `Bạn là ${teacherName}, người Hà Nội. TÍNH CÁCH: Thanh lịch, chuẩn mực. 
                NGÔN NGỮ: Văn phong Hà Nội chuẩn. Tiếng Anh chuẩn giọng British English.
                BỐI CẢNH BÀI HỌC: ${tutorData.transcript}.
                
                [LỆNH KHẨN CẤP TỪ HỆ THỐNG]: Cuộc trò chuyện vừa bị gián đoạn do lỗi mạng. Đây là lịch sử những gì BẠN ĐÃ NÓI nãy giờ: "${transcriptRef.current}".
                NHIỆM VỤ HIỆN TẠI: Tiếp tục cuộc đàm thoại ngay lập tức. TUYỆT ĐỐI KHÔNG chào hỏi lại, KHÔNG nhắc lại tên bài học, KHÔNG xin lỗi. Hãy đợi học sinh hỏi hoặc tiếp tục ý đang giảng dang dở một cách tự nhiên nhất.
                
                ${promptKienNhan}`;
            } else {
                systemPrompt = `Bạn là ${teacherName}, người Hà Nội. TÍNH CÁCH: Thanh lịch, chuẩn mực. 
                NGÔN NGỮ: Văn phong Hà Nội chuẩn. Tiếng Anh chuẩn giọng British English.
                BỐI CẢNH: ${tutorData.transcript}. 
                NHIỆM VỤ: ${tutorData.feedback}. 
                
                [QUY TẮC GIAO TIẾP NGHIÊM NGẶT]: Bạn CHỈ ĐƯỢC phép chào hỏi và giới thiệu tên bài học 1 LẦN DUY NHẤT ở câu nói đầu tiên. Từ các lượt hội thoại sau đó, TUYỆT ĐỐI KHÔNG lặp lại lời chào hay giới thiệu tên bài học nữa. Hãy đi thẳng vào việc giải đáp thắc mắc của học sinh. Trả lời ngắn gọn, tương tác qua lại tự nhiên như người thật.
                
                ${promptKienNhan}`;
            }
        } else {
            if (isReconnect && transcriptRef.current) {
                systemPrompt = `Bạn là giám khảo IELTS tên ${teacherName}, người Hà Nội. Giao tiếp văn phong chuẩn miền Bắc. Phát âm tiếng Anh giọng British English.
                BỐI CẢNH: Hãy đóng vai giám khảo và yêu cầu tôi nói về chủ đề: "${currentTopic}".
                
                [LỆNH KHẨN CẤP]: Mạng vừa rớt. Đây là lịch sử bạn đã nói: "${transcriptRef.current}". 
                TUYỆT ĐỐI KHÔNG chào lại, KHÔNG giới thiệu lại. Hãy tiếp tục phần thi ngay lập tức.
                
                ${promptKienNhan}`;
            } else {
                systemPrompt = `Bạn là giám khảo IELTS tên ${teacherName}, người Hà Nội. Giao tiếp văn phong chuẩn miền Bắc. Phát âm tiếng Anh giọng British English.
                BỐI CẢNH: Hãy đóng vai giám khảo và yêu cầu tôi nói về chủ đề: "${currentTopic}".
                
                [QUY TẮC]: Chỉ chào hỏi 1 lần duy nhất ở câu đầu tiên. Sau đó tương tác tự nhiên, hỏi và đợi tôi trả lời.
                
                ${promptKienNhan}`;
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

        sourceNodeRef.current = audioCtxInputRef.current!.createMediaStreamSource(streamRef.current!);
        processorNodeRef.current = audioCtxInputRef.current!.createScriptProcessor(4096, 1, 1);
        gainNodeRef.current = audioCtxInputRef.current!.createGain();
        gainNodeRef.current.gain.value = 0;

        processorNodeRef.current.onaudioprocess = (e) => {
          if (ws !== wsRef.current || ws.readyState !== WebSocket.OPEN) return;
            
          if (isSetupCompleteRef.current) {
            const inputData = e.inputBuffer.getChannelData(0);
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
             return;
          }
          
          if (msg.serverContent?.modelTurn?.parts) {
             for (let part of msg.serverContent.modelTurn.parts) {
                if (part.text) { 
                    transcriptRef.current += " " + part.text; 
                    setTranscript(transcriptRef.current); 
                }
                if (part.inlineData?.data) {
                    playAIAudio(part.inlineData.data);
                }
             }
          }
        } catch (error) {}
      };

      ws.onclose = () => { 
          if (!isIntendedCloseRef.current) {
              if (reconnectTimeoutRef.current) clearTimeout(reconnectTimeoutRef.current);
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
    
    if (reconnectTimeoutRef.current) clearTimeout(reconnectTimeoutRef.current);
    if (pendingCallTimeoutRef.current) clearTimeout(pendingCallTimeoutRef.current);

    try { if (wsRef.current) wsRef.current.close(); } catch(e) {}
    try { if (streamRef.current) streamRef.current.getTracks().forEach(t => t.stop()); } catch(e) {}
    try { if (sourceNodeRef.current) sourceNodeRef.current.disconnect(); } catch(e) {}
    try { if (processorNodeRef.current) processorNodeRef.current.disconnect(); } catch(e) {}
    try { if (gainNodeRef.current) gainNodeRef.current.disconnect(); } catch(e) {}
    try { if (audioCtxInputRef.current && audioCtxInputRef.current.state !== 'closed') audioCtxInputRef.current.close(); } catch(e) {}
    try { if (audioCtxOutputRef.current && audioCtxOutputRef.current.state !== 'closed') audioCtxOutputRef.current.close(); } catch(e) {}

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
  // GIAO DIỆN WIDGET THU NHỎ (🚀 DỜI SANG RIGHT-6 CHỐNG LỖI ĐÈ GIAO DIỆN LECTURE)
  // =========================================================================================
  if (viewState === 'MINIMIZED') {
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

  // =========================================================================================
  // GIAO DIỆN TOÀN MÀN HÌNH CHÍNH (ĐÃ FIX LỖI CUỘN TRÊN MOBILE)
  // =========================================================================================
  
  const currentMode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
  const currentTopic = sessionStorage.getItem('tony_live_topic') || "Bài tập giao tiếp tổng hợp";
  
  const handleYellowButtonClick = () => {
      if (onOpenAI) {
          onOpenAI(currentMode === 'TUTOR' ? 'tutor' : 'ielts');
      }
  };
  
  return (
    <div className="fixed inset-0 z-[9999] flex flex-col items-center justify-center min-h-[100dvh] bg-[#020617]/95 backdrop-blur-md text-slate-200 p-4 md:p-8 w-full font-sans overflow-y-auto custom-scrollbar animate-in fade-in duration-300">
      
      {onOpenAI && (
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

      <div className="bg-[#0f172a] p-6 md:p-12 rounded-[2rem] shadow-[0_20px_60px_rgba(0,0,0,0.8)] border border-slate-700 max-w-2xl w-full text-center relative z-10 max-h-[95dvh] overflow-y-auto custom-scrollbar my-auto">
        
        <button 
            onClick={handleBackClick} 
            className="absolute top-4 left-4 md:top-6 md:left-6 text-slate-400 hover:text-white bg-slate-800 hover:bg-slate-700 px-4 py-2 rounded-xl text-sm font-medium transition-all shadow-sm border border-slate-600"
        >
          {status !== 'IDLE' ? '👇 Thu nhỏ (Nghe nền)' : '← Thoát'}
        </button>

        <div className="mb-8 mt-12 md:mt-8">
           <h2 className="text-2xl md:text-4xl font-black mb-2 md:mb-3 text-white tracking-tight">
               {currentMode === 'TUTOR' ? 'Gia Sư Giải Đáp 1-1' : 'Phòng Luyện Nói 1-1'}
           </h2>
           <p className="text-emerald-400 font-medium text-[13px] md:text-[15px] opacity-90">
               {currentMode === 'TUTOR' ? 'Cùng thầy/cô phân tích nội dung bài học' : 'Đàm thoại tiếng Anh trực tiếp với Giám khảo ảo'}
           </p>
        </div>

        {status === 'IDLE' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
             
             <div className="bg-slate-800/50 p-4 md:p-5 rounded-2xl border border-slate-700 mb-6 md:mb-8 text-left shadow-inner flex flex-col">
                <span className="block text-[11px] uppercase tracking-widest text-slate-400 font-bold mb-2 shrink-0">
                    Đang hỗ trợ nội dung:
                </span>
                <div className="text-[14px] md:text-[15px] font-medium text-slate-200 max-h-[120px] md:max-h-[180px] overflow-y-auto custom-scrollbar pr-2 whitespace-pre-wrap">
                    {currentMode === 'TUTOR' ? "Chữa bài & Giải đáp thắc mắc chuyên sâu" : `"${currentTopic}"`}
                </div>
             </div>
             
             <div className="mb-6 md:mb-8 shrink-0">
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
            <div className="py-12 flex flex-col items-center animate-in zoom-in-95 duration-300">
                <div className="w-12 h-12 border-4 border-emerald-500/30 border-t-emerald-500 rounded-full animate-spin mb-6 shadow-[0_0_15px_rgba(16,185,129,0.5)]"></div>
                <div className="text-emerald-400 font-bold tracking-widest uppercase text-sm animate-pulse">ĐANG THIẾT LẬP KẾT NỐI...</div>
            </div>
        )}

        {status === 'CONNECTED' && (
          <div className="flex flex-col items-center animate-in zoom-in-95 duration-500 w-full h-full">
            
            <div className="relative mb-6 md:mb-8 shrink-0">
                <div className={`absolute inset-0 rounded-full transition-all duration-300 opacity-20 ${!isMuted && isMicSending ? 'bg-red-500 scale-[1.3] animate-pulse shadow-[0_0_30px_rgba(239,68,68,0.5)]' : 'bg-emerald-500 scale-100 shadow-[0_0_30px_rgba(16,185,129,0.5)]'}`}></div>
                <div className="w-24 h-24 md:w-32 md:h-32 rounded-full overflow-hidden border-4 border-slate-700 shadow-2xl relative z-10 bg-slate-800 flex items-center justify-center text-5xl md:text-6xl">
                    {examiner === 'TONY' ? '👨‍🏫' : '👩‍🏫'}
                </div>
            </div>
            
            <p className={`shrink-0 font-bold mb-4 md:mb-6 tracking-widest uppercase text-[10px] md:text-[12px] px-4 md:px-5 py-1.5 md:py-2 rounded-full border shadow-sm transition-colors ${isMuted ? 'bg-amber-950/50 text-amber-400 border-amber-800' : (isMicSending ? 'bg-red-950/50 text-red-400 border-red-800' : 'bg-emerald-950/50 text-emerald-400 border-emerald-800')}`}>
                {isMuted ? "🔇 ĐÃ TẮT MIC (CHỈ NGHE)" : (isMicSending ? "🔴 ĐANG GHI ÂM (BẠN NÓI)" : "🟢 AI ĐANG NGHE/PHẢN HỒI...")}
            </p>
            
            <div className="bg-[#020617] rounded-2xl p-4 md:p-6 w-full text-left h-36 md:h-48 overflow-y-auto mb-6 md:mb-8 border border-slate-800 font-mono text-[13px] md:text-[14px] text-slate-300 leading-relaxed shadow-inner custom-scrollbar relative flex-1 min-h-[120px]">
               {transcript || <span className="opacity-40 italic">Đang chờ tín hiệu âm thanh...</span>}
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