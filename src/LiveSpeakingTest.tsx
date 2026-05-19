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

// 🚀 THÊM PROP onBack ĐỂ XỬ LÝ NÚT QUAY LẠI
export default function LiveSpeakingTest({ onBack }: { onBack?: () => void }) {
  const [status, setStatus] = useState<'IDLE' | 'CONNECTING' | 'CONNECTED'>('IDLE');
  const [transcript, setTranscript] = useState<string>('');
  const [isMicSending, setIsMicSending] = useState(false);
  
  // 🚀 STATE CHỌN GIÁM KHẢO
  const [examiner, setExaminer] = useState<'TONY' | 'DIEP'>('TONY');
  
  const wsRef = useRef<WebSocket | null>(null);
  const audioCtxInputRef = useRef<AudioContext | null>(null);
  const audioCtxOutputRef = useRef<AudioContext | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const nextPlayTimeRef = useRef<number>(0);
  
  const isSetupCompleteRef = useRef<boolean>(false);

  // Xử lý nút quay lại an toàn
  const handleBackClick = () => {
    if (onBack) {
       onBack();
    } else {
       sessionStorage.setItem('lms_current_view', 'lecture');
       window.location.reload();
    }
  };

  const startCall = async () => {
    try {
      setStatus('CONNECTING');
      isSetupCompleteRef.current = false;
      setIsMicSending(false);
      setTranscript('');

      const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
      audioCtxInputRef.current = new AudioContextClass({ sampleRate: 16000 });
      audioCtxOutputRef.current = new AudioContextClass({ sampleRate: 24000 });
      
      if (audioCtxInputRef.current.state === 'suspended') await audioCtxInputRef.current.resume();
      if (audioCtxOutputRef.current.state === 'suspended') await audioCtxOutputRef.current.resume();
      
      nextPlayTimeRef.current = audioCtxOutputRef.current.currentTime;

      const wsUrl = 'wss://ubkvzgwespfvrlpjuxkp.supabase.co/functions/v1/live-speaking';
      const ws = new WebSocket(wsUrl);
      wsRef.current = ws;

      ws.onopen = async () => {
        setStatus('CONNECTED');
        
        const customTopic = sessionStorage.getItem('tony_live_topic') || "Please ask me an IELTS speaking question.";
        
        // 🚀 ĐỔI GIỌNG NAM/NỮ DỰA VÀO LỰA CHỌN (Puck = Giọng Nam, Aoede = Giọng Nữ)
        const voiceName = examiner === 'TONY' ? 'Puck' : 'Aoede';
        const examinerName = examiner === 'TONY' ? 'Tony' : 'Diệp';

        const setupMsg = {
          setup: {
            model: "models/gemini-3.1-flash-live-preview",
            generationConfig: {
              responseModalities: ["AUDIO"],
              speechConfig: {
                voiceConfig: { prebuiltVoiceConfig: { voiceName: voiceName } }
              }
            },
            systemInstruction: {
              parts: [{ text: `Bạn là giám khảo IELTS tên ${examinerName}. Hãy đóng vai giám khảo và yêu cầu tôi nói về chủ đề sau đây: "${customTopic}". Trả lời cực kỳ tự nhiên, ngắn gọn.` }]
            }
          }
        };
        ws.send(JSON.stringify(setupMsg));

        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        streamRef.current = stream;
        
        const source = audioCtxInputRef.current!.createMediaStreamSource(stream);
        const processor = audioCtxInputRef.current!.createScriptProcessor(4096, 1, 1);
        
        const muteNode = audioCtxInputRef.current!.createGain();
        muteNode.gain.value = 0;

        let chunkCounter = 0;
        
        processor.onaudioprocess = (e) => {
          if (ws.readyState === WebSocket.OPEN && isSetupCompleteRef.current) {
            const inputData = e.inputBuffer.getChannelData(0);
            const pcm16Buffer = floatTo16BitPCM(inputData);
            const base64Audio = arrayBufferToBase64(pcm16Buffer);
            
            ws.send(JSON.stringify({ realtimeInput: { audio: { mimeType: "audio/pcm;rate=16000", data: base64Audio } } }));

            chunkCounter++;
            if (chunkCounter % 5 === 0) setIsMicSending(prev => !prev);
          }
        };

        source.connect(processor);
        processor.connect(muteNode);
        muteNode.connect(audioCtxInputRef.current!.destination);
      };

      ws.onmessage = async (event) => {
        try {
          let rawData = event.data;
          if (rawData instanceof Blob) rawData = await rawData.text();
          
          const msg = JSON.parse(rawData);
          
          if (msg.error) {
             console.error("🚨 LỖI:", msg.error);
             alert("LỖI NGẮT KẾT NỐI:\n" + msg.error);
             stopCall();
             return;
          }

          if (msg.setupComplete) {
             isSetupCompleteRef.current = true;
             const kickoffMsg = { realtimeInput: { text: "Hello, I am ready for the Speaking Test. Please start." } };
             ws.send(JSON.stringify(kickoffMsg));
             return;
          }
          
          if (msg.serverContent?.modelTurn?.parts) {
             const parts = msg.serverContent.modelTurn.parts;
             for (let part of parts) {
                if (part.text) setTranscript(prev => prev + " " + part.text);
                if (part.inlineData && part.inlineData.data) playAIAudio(part.inlineData.data);
             }
          }
        } catch (error) { console.error("LỖI PARSE JSON:", error); }
      };

      ws.onclose = () => stopCall();

    } catch (error) {
      console.error(error);
      alert("Không thể truy cập Micro. Vui lòng kiểm tra quyền cài đặt của trình duyệt!");
      setStatus('IDLE');
    }
  };

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
    if (wsRef.current) wsRef.current.close();
    if (streamRef.current) streamRef.current.getTracks().forEach(t => t.stop());
    if (audioCtxInputRef.current) audioCtxInputRef.current.close();
    if (audioCtxOutputRef.current) audioCtxOutputRef.current.close();
    
    setStatus('IDLE');
    isSetupCompleteRef.current = false;
    setIsMicSending(false);
  };

  // Lấy chủ đề hiện tại để hiển thị cho học sinh biết
  const currentTopic = sessionStorage.getItem('tony_live_topic') || "Bài tập giao tiếp tổng hợp";

  return (
    <div className="flex flex-col items-center justify-center min-h-[100dvh] bg-[#020617] text-slate-200 p-4 sm:p-8 w-full font-sans">
      <div className="bg-[#0f172a] p-8 md:p-12 rounded-[2rem] shadow-[0_20px_60px_rgba(0,0,0,0.4)] border border-slate-800 max-w-2xl w-full text-center relative">
        
        <button 
          onClick={handleBackClick} 
          className="absolute top-6 left-6 text-slate-400 hover:text-white transition-colors flex items-center gap-2 font-medium"
        >
          <span className="text-xl">←</span> Quay lại
        </button>

        <div className="mb-10 mt-6">
           <h2 className="text-3xl md:text-4xl font-black mb-3 text-white tracking-tight">Phòng Luyện Nói 1-1</h2>
           <p className="text-emerald-400 font-medium text-[15px] max-w-md mx-auto leading-relaxed opacity-90">
             Tương tác giọng nói trực tiếp với Giám khảo ảo.
           </p>
        </div>

        {status === 'IDLE' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
             <div className="bg-slate-800/50 p-4 rounded-2xl border border-slate-700 mb-8 inline-block">
                <span className="block text-[12px] uppercase tracking-widest text-slate-400 font-bold mb-1">Chủ đề luyện tập:</span>
                <span className="text-[15px] font-medium text-slate-200 line-clamp-2 px-2 max-w-sm">{currentTopic}</span>
             </div>

             <div className="mb-8">
                <h3 className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-4">Lựa chọn Giám khảo</h3>
                <div className="flex justify-center gap-4">
                    {/* NÚT CHỌN GIÁM KHẢO TÔN */}
                    <button 
                       onClick={() => setExaminer('TONY')}
                       className={`relative w-28 py-3 rounded-2xl flex flex-col items-center gap-2 transition-all duration-200 border-2 ${examiner === 'TONY' ? 'bg-slate-800 border-emerald-500 shadow-[0_0_20px_rgba(16,185,129,0.2)]' : 'bg-slate-900 border-transparent hover:border-slate-700 opacity-60'}`}
                    >
                       <div className="text-3xl">👨‍🏫</div>
                       <span className={`text-[13px] font-bold ${examiner === 'TONY' ? 'text-emerald-400' : 'text-slate-400'}`}>Mr. Tôn</span>
                       {examiner === 'TONY' && <div className="absolute -top-2 -right-2 w-5 h-5 bg-emerald-500 rounded-full flex items-center justify-center text-white text-[10px]">✓</div>}
                    </button>

                    {/* NÚT CHỌN GIÁM KHẢO DIỆP */}
                    <button 
                       onClick={() => setExaminer('DIEP')}
                       className={`relative w-28 py-3 rounded-2xl flex flex-col items-center gap-2 transition-all duration-200 border-2 ${examiner === 'DIEP' ? 'bg-slate-800 border-emerald-500 shadow-[0_0_20px_rgba(16,185,129,0.2)]' : 'bg-slate-900 border-transparent hover:border-slate-700 opacity-60'}`}
                    >
                       <div className="text-3xl">👩‍🏫</div>
                       <span className={`text-[13px] font-bold ${examiner === 'DIEP' ? 'text-emerald-400' : 'text-slate-400'}`}>Ms. Diệp</span>
                       {examiner === 'DIEP' && <div className="absolute -top-2 -right-2 w-5 h-5 bg-emerald-500 rounded-full flex items-center justify-center text-white text-[10px]">✓</div>}
                    </button>
                </div>
             </div>

             <button onClick={startCall} className="w-full bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-4 rounded-2xl text-[16px] transition-all active:scale-95 shadow-[0_10px_20px_rgba(16,185,129,0.3)] flex items-center justify-center gap-3">
               <span className="text-xl">📞</span> Bắt Đầu Đàm Thoại
             </button>
          </div>
        )}

        {status === 'CONNECTING' && (
           <div className="py-12 flex flex-col items-center justify-center animate-in zoom-in-95 duration-300">
               <div className="w-12 h-12 border-4 border-emerald-500/30 border-t-emerald-500 rounded-full animate-spin mb-6"></div>
               <div className="text-emerald-400 font-bold tracking-widest uppercase text-sm animate-pulse">
                  Đang thiết lập kết nối mã hóa...
               </div>
           </div>
        )}

        {status === 'CONNECTED' && (
          <div className="flex flex-col items-center animate-in zoom-in-95 duration-500">
            
            {/* KHU VỰC AVATAR (Chờ chèn Video Loop sau này) */}
            <div className="relative mb-6">
                <div className={`absolute inset-0 bg-emerald-500 rounded-full transition-all duration-200 opacity-20 ${isMicSending ? 'scale-[1.3] animate-pulse' : 'scale-100'}`}></div>
                <div className="w-32 h-32 rounded-full overflow-hidden border-4 border-slate-700 shadow-2xl relative z-10 bg-slate-800 flex items-center justify-center text-5xl">
                    {/* Tạm thời dùng icon, sau này ốp thẻ <video> vào đây */}
                    {examiner === 'TONY' ? '👨‍🏫' : '👩‍🏫'}
                </div>
            </div>
            
            <p className="text-emerald-400 font-bold mb-6 tracking-widest uppercase text-[12px] bg-emerald-950/50 px-4 py-1.5 rounded-full border border-emerald-800">
                {isMicSending ? "🔴 ĐANG GHI ÂM (BẠN NÓI)" : "🟢 GIÁM KHẢO ĐANG NGHE/PHẢN HỒI..."}
            </p>
            
            <div className="bg-[#020617] rounded-2xl p-6 w-full text-left h-48 overflow-y-auto mb-8 border border-slate-800 font-mono text-[14px] text-slate-300 leading-relaxed shadow-inner custom-scrollbar relative">
               {transcript || <span className="opacity-40 italic">Đang chờ tín hiệu âm thanh...</span>}
            </div>

            <button onClick={stopCall} className="w-full bg-red-600 hover:bg-red-500 text-white font-bold py-4 rounded-2xl text-[16px] transition-all active:scale-95 shadow-[0_10px_20px_rgba(220,38,38,0.3)] flex items-center justify-center gap-3">
               <span className="text-xl">🛑</span> Kết Thúc (Cúp Máy)
            </button>
          </div>
        )}
      </div>
    </div>
  );
}