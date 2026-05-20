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
  for (let i = 0; i < bytes.byteLength; i++) binary += String.fromCharCode(bytes[i]);
  return window.btoa(binary);
};

const base64ToArrayBuffer = (base64: string) => {
  const binary_string = window.atob(base64);
  const len = binary_string.length;
  const bytes = new Uint8Array(len);
  for (let i = 0; i < len; i++) bytes[i] = binary_string.charCodeAt(i);
  return bytes.buffer;
};

// 🚀 COMPONENT CHÍNH QUẢN LÝ PHÒNG LIVE
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
    onOpenAI?: () => void 
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

  // 🚀 CÁC TÚI DỮ LIỆU ĐỂ GIỮ LIÊN LẠC KHI RỚT MẠNG
  const transcriptRef = useRef<string>(''); 
  const isIntendedCloseRef = useRef<boolean>(false); 
  const sourceNodeRef = useRef<MediaStreamAudioSourceNode | null>(null);
  const processorNodeRef = useRef<ScriptProcessorNode | null>(null);
  const gainNodeRef = useRef<GainNode | null>(null);

  const mode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
  const tutorDataRaw = sessionStorage.getItem('tony_tutor_data');
  const tutorData = tutorDataRaw ? JSON.parse(tutorDataRaw) : null;
  const currentTopic = sessionStorage.getItem('tony_live_topic') || "Bài tập giao tiếp tổng hợp";

  const statusRef = useRef(status);
  useEffect(() => { statusRef.current = status; }, [status]);

  const startCallRef = useRef<(isReconnect?: boolean) => void>(() => {});
  
  useEffect(() => {
    const handleContextSwitch = (e: any) => {
        if (e.detail === 'live-test') {
            onMaximize(); 
            
            const raw = sessionStorage.getItem('tony_tutor_data');
            if (raw) {
                const data = JSON.parse(raw);
                if (statusRef.current === 'CONNECTED' && wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
                    const msg = {
                        realtimeInput: {
                            text: `[HỆ THỐNG]: Học sinh vừa lật sang xem câu hỏi khác. Nhiệm vụ của bạn: DỪNG nói chuyện cũ, đọc nội dung câu hỏi mới này và chủ động giảng bài ngay lập tức. Nội dung câu mới: ${data.transcript}`
                        }
                    };
                    wsRef.current.send(JSON.stringify(msg));
                } else if (statusRef.current === 'IDLE') {
                    startCallRef.current(false);
                }
            }
        }
    };
    window.addEventListener('tony-navigate', handleContextSwitch);
    return () => window.removeEventListener('tony-navigate', handleContextSwitch);
  }, [onMaximize]);

  const handleBackClick = () => {
    if (status !== 'IDLE') {
        onMinimize();
    } else {
        sessionStorage.removeItem('tony_live_mode');
        sessionStorage.removeItem('tony_tutor_data');
        onClose();
    }
  };

  const toggleMute = () => {
      isMutedRef.current = !isMutedRef.current;
      setIsMuted(isMutedRef.current);
  };

  // 🚀 HÀM GỌI ĐIỆN VỚI TÍNH NĂNG TỰ ĐỘNG KHÔI PHỤC (AUTO-RECONNECT)
  const startCall = async (isReconnect = false) => {
    try {
      setStatus('CONNECTING');
      isSetupCompleteRef.current = false;
      setIsMicSending(false);
      
      // Chỉ reset lịch sử nếu là cuộc gọi mới tinh
      if (!isReconnect) {
          setTranscript('');
          transcriptRef.current = '';
      }
      
      isIntendedCloseRef.current = false;
      isMutedRef.current = false;
      setIsMuted(false);

      if (!audioCtxInputRef.current) {
          const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
          audioCtxInputRef.current = new AudioContextClass({ sampleRate: 16000 });
          audioCtxOutputRef.current = new AudioContextClass({ sampleRate: 24000 });
      }
      
      if (audioCtxInputRef.current.state === 'suspended') await audioCtxInputRef.current.resume();
      if (audioCtxOutputRef.current.state === 'suspended') await audioCtxOutputRef.current.resume();
      
      if (!streamRef.current) {
          streamRef.current = await navigator.mediaDevices.getUserMedia({ audio: true });
      }
      
      nextPlayTimeRef.current = audioCtxOutputRef.current.currentTime;

      const wsUrl = 'wss://ubkvzgwespfvrlpjuxkp.supabase.co/functions/v1/live-speaking';
      const ws = new WebSocket(wsUrl);
      wsRef.current = ws;

      ws.onopen = () => {
        setStatus('CONNECTED');
        const voiceName = examiner === 'TONY' ? 'Puck' : 'Aoede';
        const teacherName = examiner === 'TONY' ? 'thầy Tôn' : 'cô Diệp';

        const freshMode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
        const freshTutorDataRaw = sessionStorage.getItem('tony_tutor_data');
        const freshTutorData = freshTutorDataRaw ? JSON.parse(freshTutorDataRaw) : null;

        let systemPrompt = "";
        if (freshMode === 'TUTOR' && freshTutorData) {
            systemPrompt = `Bạn là ${teacherName}, một gia sư IELTS người Hà Nội. TÍNH CÁCH: Thanh lịch, ân cần, chuẩn mực. 
            NGÔN NGỮ: Bắt buộc dùng văn phong và từ ngữ chuẩn miền Bắc (Hà Nội) khi nói tiếng Việt. Khi phát âm tiếng Anh, BẮT BUỘC dùng chuẩn Anh-Anh (British English).
            BỐI CẢNH: Học sinh đang xem lại bài làm với kết quả Overall: ${freshTutorData.overall}. Dữ liệu câu đang hỏi: "${freshTutorData.transcript}". 
            NHIỆM VỤ: Chào thân thiện, sau đó phân tích lỗi sai hoặc giải thích chuyên sâu bằng tiếng Việt xen tiếng Anh.`;
        } else {
            systemPrompt = `Bạn là giám khảo IELTS tên ${teacherName}, người Hà Nội. TÍNH CÁCH: Thanh lịch, chuyên nghiệp. 
            NGÔN NGỮ: Bắt buộc giao tiếp bằng văn phong chuẩn miền Bắc (Hà Nội). Phát âm tiếng Anh chuẩn Anh-Anh (British English).
            BỐI CẢNH: Hãy đóng vai giám khảo và yêu cầu tôi nói về chủ đề: "${currentTopic}". Trả lời tự nhiên, ngắn gọn.`;
        }

        // 🚀 NHỒI LẠI TRÍ NHỚ CHO AI NẾU LÀ RECONNECT
        if (isReconnect && transcriptRef.current) {
            systemPrompt += `\n\n[HỆ THỐNG CHÚ Ý]: Cuộc gọi vừa bị gián đoạn do lỗi mạng. Đây là lịch sử trò chuyện nãy giờ: "${transcriptRef.current}". Hãy phân tích ngữ cảnh và tiếp tục cuộc trò chuyện một cách tự nhiên nhất, TUYỆT ĐỐI không cần xin lỗi hay nhắc lại việc rớt mạng.`;
        }

        const setupMsg = {
          setup: {
            model: "models/gemini-3.1-flash-live-preview",
            generationConfig: { responseModalities: ["AUDIO"], speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: voiceName } } } },
            systemInstruction: { parts: [{ text: systemPrompt }] }
          }
        };
        ws.send(JSON.stringify(setupMsg));

        if (processorNodeRef.current) {
            processorNodeRef.current.disconnect();
            if (sourceNodeRef.current) sourceNodeRef.current.disconnect(processorNodeRef.current);
        }
        if (gainNodeRef.current) gainNodeRef.current.disconnect();

        sourceNodeRef.current = audioCtxInputRef.current!.createMediaStreamSource(streamRef.current!);
        processorNodeRef.current = audioCtxInputRef.current!.createScriptProcessor(4096, 1, 1);
        gainNodeRef.current = audioCtxInputRef.current!.createGain();
        gainNodeRef.current.gain.value = 0;

        let chunkCounter = 0;
        processorNodeRef.current.onaudioprocess = (e) => {
          if (ws.readyState === WebSocket.OPEN && isSetupCompleteRef.current) {
            const inputData = e.inputBuffer.getChannelData(0);
            const dataToSend = isMutedRef.current ? new Float32Array(inputData.length) : inputData;
            const pcm16Buffer = floatTo16BitPCM(dataToSend);
            ws.send(JSON.stringify({ realtimeInput: { audio: { mimeType: "audio/pcm;rate=16000", data: arrayBufferToBase64(pcm16Buffer) } } }));
            
            chunkCounter++;
            if (chunkCounter % 5 === 0 && !isMutedRef.current) setIsMicSending(prev => !prev);
            else if (isMutedRef.current) setIsMicSending(false);
          }
        };

        sourceNodeRef.current.connect(processorNodeRef.current);
        processorNodeRef.current.connect(gainNodeRef.current);
        gainNodeRef.current.connect(audioCtxInputRef.current!.destination);
      };

      ws.onmessage = async (event) => {
        try {
          let rawData = event.data;
          if (rawData instanceof Blob) rawData = await rawData.text();
          const msg = JSON.parse(rawData);
          
          if (msg.error) {
             console.error("🚨 LỖI TỪ SERVER:", msg.error); 
             if (!isIntendedCloseRef.current) {
                 setTimeout(() => { if (!isIntendedCloseRef.current) startCall(true); }, 1000);
             }
             return;
          }

          if (msg.setupComplete) {
             isSetupCompleteRef.current = true;
             if (!isReconnect) {
                 const freshMode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
                 const helloMsg = freshMode === 'TUTOR' ? "Chào em, thầy/cô đang xem câu hỏi em chọn rồi, mình cùng giải quyết nhé!" : "Hello, I am ready for the Speaking Test. Please start.";
                 ws.send(JSON.stringify({ realtimeInput: { text: helloMsg } }));
             } else {
                 ws.send(JSON.stringify({ realtimeInput: { text: "(Hệ thống đã tự động kết nối lại thành công, bạn hãy tiếp tục bài giảng)" } }));
             }
             return;
          }
          
          if (msg.serverContent?.modelTurn?.parts) {
             const parts = msg.serverContent.modelTurn.parts;
             for (let part of parts) {
                if (part.text) {
                    transcriptRef.current += " " + part.text;
                    setTranscript(transcriptRef.current);
                }
                if (part.inlineData && part.inlineData.data) playAIAudio(part.inlineData.data);
             }
          }
        } catch (error) {}
      };

      // 🚀 NẾU RỚT MẠNG ĐỘT NGỘT: TỰ ĐỘNG GỌI LẠI TRONG 1 GIÂY
      ws.onclose = () => {
          if (!isIntendedCloseRef.current) {
              console.log("⚠️ Máy chủ ngắt kết nối quá hạn (Timeout). Đang tự động khôi phục...");
              setTimeout(() => {
                  if (!isIntendedCloseRef.current) startCall(true);
              }, 1000);
          }
      };

    } catch (error) {
      alert("Lỗi truy cập Micro hoặc rớt mạng. Vui lòng tải lại trang!");
      setStatus('IDLE');
    }
  };

  useEffect(() => { startCallRef.current = startCall; }, [examiner]);

  const playAIAudio = (base64Audio: string) => {
    if (!audioCtxOutputRef.current) return;
    const ctx = audioCtxOutputRef.current;
    if (ctx.state === 'suspended') ctx.resume();
    const pcmBuffer = base64ToArrayBuffer(base64Audio);
    const int16Array = new Int16Array(pcmBuffer);
    const float32Array = new Float32Array(int16Array.length);
    for (let i = 0; i < int16Array.length; i++) float32Array[i] = int16Array[i] / 32768.0;
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
    if (wsRef.current) wsRef.current.close();
    if (streamRef.current) streamRef.current.getTracks().forEach(t => t.stop());
    
    if (sourceNodeRef.current) sourceNodeRef.current.disconnect();
    if (processorNodeRef.current) processorNodeRef.current.disconnect();
    if (gainNodeRef.current) gainNodeRef.current.disconnect();

    if (audioCtxInputRef.current) audioCtxInputRef.current.close();
    if (audioCtxOutputRef.current) audioCtxOutputRef.current.close();
    
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

  if (viewState === 'MINIMIZED') {
      return (
          <div className="fixed bottom-6 right-6 z-[99999] bg-[#0f172a] border border-slate-700 shadow-2xl rounded-2xl p-4 flex flex-col gap-3 w-72 sm:w-80 animate-in slide-in-from-bottom-5 font-sans">
             <div className="flex justify-between items-center">
                <div className="flex items-center gap-2 cursor-pointer" onClick={onMaximize}>
                   <div className={`w-3 h-3 rounded-full shadow-lg ${isMicSending ? 'bg-red-500 animate-pulse shadow-red-500/50' : 'bg-emerald-500 shadow-emerald-500/50'}`}></div>
                   <span className="text-white font-bold text-[13px]">{status === 'CONNECTING' ? 'Đang khôi phục...' : (isMuted ? 'Đã tắt Mic' : (isMicSending ? 'Đang nghe bạn nói...' : 'Gia sư đang kết nối...'))}</span>
                </div>
                <button onClick={onMaximize} className="text-slate-400 hover:text-white p-1.5 bg-slate-800 hover:bg-slate-700 transition rounded-lg" title="Phóng to">
                   <svg xmlns="http://www.w3.org/2000/svg" className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" /></svg>
                </button>
             </div>
             
             <div className="text-[12px] text-slate-400 truncate italic bg-slate-900/50 px-3 py-2 rounded-lg border border-slate-800">
                 {transcript ? `"...${transcript.slice(-35)}"` : "Đang chờ tín hiệu..."}
             </div>
             
             <div className="flex gap-2 mt-1">
                 <button onClick={toggleMute} className={`flex-1 font-bold py-2 rounded-xl text-[13px] transition-all shadow-md flex items-center justify-center gap-2 ${isMuted ? 'bg-amber-600 hover:bg-amber-500 text-white' : 'bg-slate-700 hover:bg-slate-600 text-white'}`}>
                    {isMuted ? '🔇 Đã Tắt Mic' : '🎙️ Tắt Mic'}
                 </button>
                 <button onClick={handleUserHangUp} className="flex-1 bg-red-600/90 hover:bg-red-500 text-white font-bold py-2 rounded-xl text-[13px] transition-all shadow-md flex items-center justify-center gap-2">
                    🛑 Dập máy
                 </button>
             </div>
          </div>
      );
  }

  return (
    <div className="fixed inset-0 z-[9999] flex flex-col items-center justify-center min-h-[100dvh] bg-[#020617]/95 backdrop-blur-md text-slate-200 p-4 sm:p-8 w-full font-sans overflow-hidden animate-in fade-in duration-300">
      
      {mode !== 'TUTOR' && (
          <button 
             onClick={() => onOpenAI && onOpenAI()}
             className="absolute top-6 right-6 text-amber-400 hover:text-amber-300 transition-all flex items-center gap-2 font-bold bg-amber-950/40 px-3 py-2 md:px-5 md:py-2.5 rounded-xl border border-amber-800/60 shadow-[0_0_15px_rgba(217,119,6,0.15)] z-20 hover:scale-105 active:scale-95"
             title="Xem gợi ý kịch bản của AI"
          >
             <span className="text-lg">💡</span> 
             <span className="hidden sm:inline text-[13px] md:text-[14px]">Kịch bản AI</span>
          </button>
      )}

      <div className="bg-[#0f172a] p-8 md:p-12 rounded-[2rem] shadow-[0_20px_60px_rgba(0,0,0,0.8)] border border-slate-700 max-w-2xl w-full text-center relative z-10">
        
        <button 
          onClick={handleBackClick} 
          className="absolute top-6 left-6 text-slate-400 hover:text-white transition-colors flex items-center gap-2 font-medium bg-slate-800 hover:bg-slate-700 px-4 py-2 rounded-xl"
        >
          {status !== 'IDLE' ? '👇 Thu nhỏ (Nghe nền)' : '← Thoát'}
        </button>

        <div className="mb-10 mt-12 md:mt-6">
           <h2 className="text-3xl md:text-4xl font-black mb-3 text-white tracking-tight">
               {mode === 'TUTOR' ? 'Gia Sư Giải Đáp 1-1' : 'Phòng Luyện Nói 1-1'}
           </h2>
           <p className="text-emerald-400 font-medium text-[15px] max-w-md mx-auto leading-relaxed opacity-90">
               {mode === 'TUTOR' ? 'Cùng thầy/cô phân tích và sửa lỗi sai trong bài làm' : 'Tương tác giọng nói trực tiếp với Giám khảo ảo'}
           </p>
        </div>

        {status === 'IDLE' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
             {mode === 'TUTOR' && tutorData ? (
                <div className="bg-blue-900/20 p-4 rounded-xl border border-blue-800/50 mb-8 text-left max-w-full">
                   <div className="text-blue-400 font-bold text-[12px] uppercase mb-2 tracking-widest">Nội dung đang chữa (Band {tutorData.overall}):</div>
                   <div className="text-[14px] italic text-slate-300 line-clamp-3">"{tutorData.transcript}"</div>
                </div>
             ) : (
                <div className="bg-slate-800/50 p-4 rounded-2xl border border-slate-700 mb-8 inline-block max-w-full">
                   <span className="block text-[12px] uppercase tracking-widest text-slate-400 font-bold mb-1">Chủ đề luyện tập:</span>
                   <span className="text-[15px] font-medium text-slate-200 line-clamp-2 px-2 max-w-sm">{currentTopic}</span>
                </div>
             )}

             <div className="mb-8">
                <h3 className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-4">Lựa chọn Giám khảo</h3>
                <div className="flex justify-center gap-4">
                    <button 
                       onClick={() => setExaminer('TONY')}
                       className={`relative w-28 py-3 rounded-2xl flex flex-col items-center gap-2 transition-all duration-200 border-2 ${examiner === 'TONY' ? 'bg-slate-800 border-emerald-500 shadow-[0_0_20px_rgba(16,185,129,0.2)]' : 'bg-slate-900 border-transparent hover:border-slate-700 opacity-60'}`}
                    >
                       <div className="text-3xl">👨‍🏫</div>
                       <span className={`text-[13px] font-bold ${examiner === 'TONY' ? 'text-emerald-400' : 'text-slate-400'}`}>Thầy Tôn</span>
                       {examiner === 'TONY' && <div className="absolute -top-2 -right-2 w-5 h-5 bg-emerald-500 rounded-full flex items-center justify-center text-white text-[10px]">✓</div>}
                    </button>

                    <button 
                       onClick={() => setExaminer('DIEP')}
                       className={`relative w-28 py-3 rounded-2xl flex flex-col items-center gap-2 transition-all duration-200 border-2 ${examiner === 'DIEP' ? 'bg-slate-800 border-emerald-500 shadow-[0_0_20px_rgba(16,185,129,0.2)]' : 'bg-slate-900 border-transparent hover:border-slate-700 opacity-60'}`}
                    >
                       <div className="text-3xl">👩‍🏫</div>
                       <span className={`text-[13px] font-bold ${examiner === 'DIEP' ? 'text-emerald-400' : 'text-slate-400'}`}>Cô Diệp</span>
                       {examiner === 'DIEP' && <div className="absolute -top-2 -right-2 w-5 h-5 bg-emerald-500 rounded-full flex items-center justify-center text-white text-[10px]">✓</div>}
                    </button>
                </div>
             </div>

             <button onClick={() => startCall(false)} className="w-full bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-4 rounded-2xl text-[16px] transition-all active:scale-95 shadow-[0_10px_20px_rgba(16,185,129,0.3)] flex items-center justify-center gap-3">
               <span className="text-xl">📞</span> Bắt Đầu Đàm Thoại
             </button>
          </div>
        )}

        {status === 'CONNECTING' && (
           <div className="py-12 flex flex-col items-center justify-center animate-in zoom-in-95 duration-300">
               <div className="w-12 h-12 border-4 border-emerald-500/30 border-t-emerald-500 rounded-full animate-spin mb-6"></div>
               <div className="text-emerald-400 font-bold tracking-widest uppercase text-sm animate-pulse">Đang thiết lập kết nối mã hóa...</div>
           </div>
        )}

        {status === 'CONNECTED' && (
          <div className="flex flex-col items-center animate-in zoom-in-95 duration-500">
            <div className="relative mb-6">
                <div className={`absolute inset-0 rounded-full transition-all duration-200 opacity-20 ${!isMuted && isMicSending ? 'bg-red-500 scale-[1.3] animate-pulse' : 'bg-emerald-500 scale-100'}`}></div>
                <div className="w-32 h-32 rounded-full overflow-hidden border-4 border-slate-700 shadow-2xl relative z-10 bg-slate-800 flex items-center justify-center text-5xl">
                    {examiner === 'TONY' ? '👨‍🏫' : '👩‍🏫'}
                </div>
            </div>
            
            <p className={`font-bold mb-6 tracking-widest uppercase text-[12px] px-4 py-1.5 rounded-full border ${isMuted ? 'bg-amber-950/50 text-amber-400 border-amber-800' : (isMicSending ? 'bg-red-950/50 text-red-400 border-red-800' : 'bg-emerald-950/50 text-emerald-400 border-emerald-800')}`}>
                {isMuted ? "🔇 ĐÃ TẮT MIC (CHỈ NGHE)" : (isMicSending ? "🔴 ĐANG GHI ÂM (BẠN NÓI)" : "🟢 AI ĐANG NGHE/PHẢN HỒI...")}
            </p>
            
            <div className="bg-[#020617] rounded-2xl p-6 w-full text-left h-48 overflow-y-auto mb-8 border border-slate-800 font-mono text-[14px] text-slate-300 leading-relaxed shadow-inner custom-scrollbar relative">
               {transcript || <span className="opacity-40 italic">Đang chờ tín hiệu âm thanh...</span>}
            </div>

            <div className="flex gap-3 w-full">
                <button 
                   onClick={toggleMute} 
                   className={`flex-1 font-bold py-4 rounded-2xl text-[16px] transition-all active:scale-95 shadow-lg flex items-center justify-center gap-3 ${isMuted ? 'bg-amber-600 hover:bg-amber-500 text-white' : 'bg-slate-700 hover:bg-slate-600 text-white'}`}
                >
                   <span className="text-xl">{isMuted ? '🔇' : '🎙️'}</span> {isMuted ? 'Đã Tắt Mic' : 'Tắt Mic Tạm Thời'}
                </button>
                <button onClick={handleUserHangUp} className="flex-1 bg-red-600 hover:bg-red-500 text-white font-bold py-4 rounded-2xl text-[16px] transition-all active:scale-95 shadow-[0_10px_20px_rgba(220,38,38,0.3)] flex items-center justify-center gap-3">
                   <span className="text-xl">🛑</span> Dập Máy
                </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}