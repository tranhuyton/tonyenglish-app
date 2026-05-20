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

  // GHIM BỘ NHỚ CHỐNG TRÌNH DUYỆT TỰ TẮT MIC
  const sourceNodeRef = useRef<MediaStreamAudioSourceNode | null>(null);
  const processorNodeRef = useRef<ScriptProcessorNode | null>(null);
  const gainNodeRef = useRef<GainNode | null>(null);

  const transcriptRef = useRef<string>(''); 
  const isIntendedCloseRef = useRef<boolean>(false); 

  const statusRef = useRef(status);
  
  useEffect(() => { 
      statusRef.current = status; 
  }, [status]);

  const startCallRef = useRef<(isReconnect?: boolean) => void>(() => {});
  const stopCallRef = useRef<() => void>(() => {});

  // Cập nhật ref để dùng trong event listener không bị out-of-date
  useEffect(() => { 
      startCallRef.current = startCall; 
      stopCallRef.current = stopCall;
  }, [examiner]);

  // KIỂM TRA LỆNH GỌI TỰ ĐỘNG NGAY KHI VỪA MỞ CỬA SỔ LÊN
  useEffect(() => {
      const autoStart = sessionStorage.getItem('tony_auto_start') === 'true';
      if (autoStart) {
          sessionStorage.removeItem('tony_auto_start');
          // Chờ 0.5s cho UI render mượt mà rồi bốc máy gọi luôn
          setTimeout(() => {
              if (startCallRef.current) {
                  startCallRef.current(false);
              }
          }, 500);
      }
  }, []);

  // 🚀 RADAR THÔNG MINH: XỬ LÝ LỖI LỒNG GIỌNG NÓI 
  useEffect(() => {
    const handleNavigationEvent = (e: any) => {
        if (e.detail === 'live-test') {
            onMaximize(); 
            const autoStart = sessionStorage.getItem('tony_auto_start') === 'true';
            
            if (autoStart) {
                sessionStorage.removeItem('tony_auto_start');
                
                if (statusRef.current === 'CONNECTED' || statusRef.current === 'CONNECTING') {
                    // ĐANG GỌI DỞ THÌ DẬP MÁY NGAY ĐỂ CẮT ĐỨT HÀNG ĐỢI ÂM THANH CŨ
                    if (stopCallRef.current) {
                        stopCallRef.current();
                    }
                    
                    // NGHỈ 0.5 GIÂY RỒI KHỞI ĐỘNG CUỘC GỌI MỚI VỚI DỮ LIỆU BÀI GIẢNG MỚI
                    setTimeout(() => {
                        if (startCallRef.current) {
                            startCallRef.current(false);
                        }
                    }, 500);
                } else {
                    // CHƯA GỌI -> BỐC MÁY GỌI BÌNH THƯỜNG
                    setTimeout(() => {
                        if (startCallRef.current) {
                            startCallRef.current(false);
                        }
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

  // 🚀 HÀM START CALL GỌI API GOOGLE GEMINI
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

      if (!audioCtxInputRef.current) {
          const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
          audioCtxInputRef.current = new AudioContextClass({ sampleRate: 16000 });
          audioCtxOutputRef.current = new AudioContextClass({ sampleRate: 24000 });
      }
      
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

      const wsUrl = 'wss://ubkvzgwespfvrlpjuxkp.supabase.co/functions/v1/live-speaking';
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
        
        if (mode === 'TUTOR' && tutorData) {
            systemPrompt = `Bạn là ${teacherName}, người Hà Nội. TÍNH CÁCH: Thanh lịch, chuẩn mực. 
            NGÔN NGỮ: Văn phong Hà Nội chuẩn. Tiếng Anh chuẩn giọng British English.
            BỐI CẢNH: ${tutorData.transcript}. 
            NHIỆM VỤ: ${tutorData.feedback}. Hãy giảng bài ân cần bằng song ngữ Việt-Anh.`;
        } else {
            systemPrompt = `Bạn là giám khảo IELTS tên ${teacherName}, người Hà Nội. Giao tiếp văn phong chuẩn miền Bắc. Phát âm tiếng Anh giọng British English.
            BỐI CẢNH: Hãy đóng vai giám khảo và yêu cầu tôi nói về chủ đề: "${currentTopic}".`;
        }

        if (isReconnect && transcriptRef.current) {
            systemPrompt += `\n\n[HỆ THỐNG]: Mạng vừa rớt. Đây là lịch sử nãy giờ: "${transcriptRef.current}". Tiếp tục giảng bài ngay, không cần xin lỗi.`;
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
          if (ws.readyState === WebSocket.OPEN && isSetupCompleteRef.current) {
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
                     text: isReconnect ? "Please continue." : "Hello, I am ready." 
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
              setTimeout(() => {
                  startCall(true);
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

  // 🚀 HÀM DẬP MÁY: XÓA SẠCH HÀNG ĐỢI ÂM THANH
  const stopCall = () => {
    isIntendedCloseRef.current = true;
    
    if (wsRef.current) {
        wsRef.current.close();
    }
    
    if (streamRef.current) {
        streamRef.current.getTracks().forEach(t => t.stop());
    }
    
    if (sourceNodeRef.current) {
        sourceNodeRef.current.disconnect();
    }
    
    if (processorNodeRef.current) {
        processorNodeRef.current.disconnect();
    }
    
    if (audioCtxInputRef.current) {
        audioCtxInputRef.current.close(); // Đóng thẻ này là âm thanh cũ bị xóa sạch ngay
    }
    
    if (audioCtxOutputRef.current) {
        audioCtxOutputRef.current.close();
    }
    
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
  // GIAO DIỆN WIDGET THU NHỎ
  // =========================================================================================
  if (viewState === 'MINIMIZED') {
      return (
          <div className="fixed bottom-6 right-6 z-[99999] bg-[#0f172a] border border-slate-700 shadow-2xl rounded-2xl p-4 flex flex-col gap-3 w-72 animate-in slide-in-from-bottom-5 font-sans">
             
             <div className="flex justify-between items-center">
                <div className="flex items-center gap-2 cursor-pointer" onClick={onMaximize}>
                   <div className={`w-3 h-3 rounded-full ${isMicSending ? 'bg-red-500 animate-pulse' : 'bg-emerald-500'}`}></div>
                   <span className="text-white font-bold text-[13px]">
                       {isMuted ? 'Đã tắt Mic' : (isMicSending ? 'Đang nghe...' : 'Gia sư đang đợi...')}
                   </span>
                </div>
                <button onClick={onMaximize} className="text-slate-400 hover:text-white p-1.5 bg-slate-800 rounded-lg">
                    Phóng to
                </button>
             </div>
             
             <div className="flex gap-2 mt-1">
                 <button 
                    onClick={toggleMute} 
                    className={`flex-1 font-bold py-2 rounded-xl text-[13px] transition-all shadow-md flex items-center justify-center gap-2 ${isMuted ? 'bg-amber-600 hover:bg-amber-500 text-white' : 'bg-slate-700 hover:bg-slate-600 text-white'}`}
                 >
                    {isMuted ? '🔇 Đã Tắt Mic' : '🎙️ Tắt Mic'}
                 </button>
                 
                 <button 
                     onClick={handleUserHangUp} 
                     className="flex-1 bg-red-600 hover:bg-red-500 text-white font-bold py-2 rounded-xl text-[13px] transition-all shadow-md flex items-center justify-center gap-2"
                 >
                    🛑 Dập máy
                 </button>
             </div>
             
          </div>
      );
  }

  // =========================================================================================
  // GIAO DIỆN TOÀN MÀN HÌNH CHÍNH
  // =========================================================================================
  
  // Lấy dữ liệu để render text trong trạng thái IDLE
  const currentMode = sessionStorage.getItem('tony_live_mode') || 'EXAMINER';
  const currentTopic = sessionStorage.getItem('tony_live_topic') || "Bài tập giao tiếp tổng hợp";
  
  return (
    <div className="fixed inset-0 z-[9999] flex flex-col items-center justify-center min-h-[100dvh] bg-[#020617]/95 backdrop-blur-md text-slate-200 p-4 w-full font-sans overflow-hidden animate-in fade-in duration-300">
      
      <div className="bg-[#0f172a] p-8 md:p-12 rounded-[2rem] shadow-2xl border border-slate-700 max-w-2xl w-full text-center relative z-10">
        
        <button 
            onClick={handleBackClick} 
            className="absolute top-6 left-6 text-slate-400 hover:text-white bg-slate-800 px-4 py-2 rounded-xl text-sm font-medium transition-all"
        >
          {status !== 'IDLE' ? '👇 Thu nhỏ (Nghe nền)' : '← Thoát'}
        </button>

        <div className="mb-10 mt-12">
           <h2 className="text-3xl md:text-4xl font-black mb-3 text-white tracking-tight">
               Gia Sư Giải Đáp 1-1
           </h2>
           <p className="text-emerald-400 font-medium text-[15px] opacity-90">
               Cùng thầy/cô phân tích nội dung bài học
           </p>
        </div>

        {status === 'IDLE' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
             
             <div className="bg-slate-800/50 p-5 rounded-2xl border border-slate-700 mb-8 text-left">
                <span className="block text-[11px] uppercase tracking-widest text-slate-400 font-bold mb-2">
                    Đang hỗ trợ nội dung:
                </span>
                <span className="text-[15px] font-medium text-slate-200 line-clamp-2">
                    {currentMode === 'TUTOR' ? "Chữa bài & Giải đáp thắc mắc chuyên sâu" : `"${currentTopic}"`}
                </span>
             </div>
             
             <div className="mb-8">
                <h3 className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-4">Lựa chọn Giám khảo</h3>
                <div className="flex justify-center gap-4">
                    <button 
                        onClick={() => setExaminer('TONY')} 
                        className={`relative w-28 py-3 rounded-2xl flex flex-col items-center gap-2 border-2 transition-all ${examiner === 'TONY' ? 'bg-slate-800 border-emerald-500' : 'bg-slate-900 border-transparent opacity-60'}`}
                    >
                       <div className="text-3xl">👨‍🏫</div>
                       <span className="text-[13px] font-bold">Thầy Tôn</span>
                    </button>
                    
                    <button 
                        onClick={() => setExaminer('DIEP')} 
                        className={`relative w-28 py-3 rounded-2xl flex flex-col items-center gap-2 border-2 transition-all ${examiner === 'DIEP' ? 'bg-slate-800 border-emerald-500' : 'bg-slate-900 border-transparent opacity-60'}`}
                    >
                       <div className="text-3xl">👩‍🏫</div>
                       <span className="text-[13px] font-bold">Cô Diệp</span>
                    </button>
                </div>
             </div>
             
             <button 
                 onClick={() => startCall(false)} 
                 className="w-full bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-4 rounded-2xl text-[16px] shadow-lg flex items-center justify-center gap-3 active:scale-95 transition-all"
             >
                 📞 Bắt Đầu Đàm Thoại
             </button>
          </div>
        )}

        {status === 'CONNECTING' && (
            <div className="py-12 flex flex-col items-center">
                <div className="w-12 h-12 border-4 border-emerald-500/30 border-t-emerald-500 rounded-full animate-spin mb-6"></div>
                <div className="text-emerald-400 font-bold animate-pulse">ĐANG THIẾT LẬP KẾT NỐI...</div>
            </div>
        )}

        {status === 'CONNECTED' && (
          <div className="flex flex-col items-center animate-in zoom-in-95 duration-500 w-full">
            
            <div className="relative mb-8">
                <div className={`absolute inset-0 rounded-full transition-all duration-300 opacity-20 ${!isMuted && isMicSending ? 'bg-red-500 scale-[1.3] animate-pulse' : 'bg-emerald-500 scale-100'}`}></div>
                <div className="w-32 h-32 rounded-full overflow-hidden border-4 border-slate-700 shadow-2xl relative z-10 bg-slate-800 flex items-center justify-center text-6xl">
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
                    className={`flex-1 font-bold py-4 rounded-2xl flex items-center justify-center gap-3 transition-all ${isMuted ? 'bg-amber-600 hover:bg-amber-500 text-white' : 'bg-slate-700 hover:bg-slate-600 text-white'}`}
                >
                   <span className="text-xl">{isMuted ? '🔇' : '🎙️'}</span> {isMuted ? 'Đã Tắt Mic' : 'Tắt Mic Tạm Thời'}
                </button>
                <button 
                    onClick={handleUserHangUp} 
                    className="flex-1 bg-red-600 hover:bg-red-500 text-white font-bold py-4 rounded-2xl shadow-lg flex items-center justify-center gap-3 active:scale-95 transition-all"
                >
                    <span className="text-xl">🛑</span> Dập Máy
                </button>
            </div>
            
          </div>
        )}
      </div>
    </div>
  );
}