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

export default function LiveSpeakingTest() {
  const [status, setStatus] = useState<'IDLE' | 'CONNECTING' | 'CONNECTED'>('IDLE');
  const [transcript, setTranscript] = useState<string>('');
  const [isMicSending, setIsMicSending] = useState(false);
  
  const wsRef = useRef<WebSocket | null>(null);
  const audioCtxInputRef = useRef<AudioContext | null>(null);
  const audioCtxOutputRef = useRef<AudioContext | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const nextPlayTimeRef = useRef<number>(0);
  
  const isSetupCompleteRef = useRef<boolean>(false);

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
        
        const setupMsg = {
          setup: {
            model: "models/gemini-3.1-flash-live-preview",
            generationConfig: {
              responseModalities: ["AUDIO"],
              speechConfig: {
                voiceConfig: { prebuiltVoiceConfig: { voiceName: "Aoede" } }
              }
            },
            systemInstruction: {
              parts: [{ text: "Bạn là giám khảo IELTS tên Tony đến từ Anh. Hãy bắt đầu cuộc thi Speaking Part 1 bằng cách chào hỏi và hỏi tên tôi. Trả lời cực kỳ ngắn gọn." }]
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
            
            // 🚀 ĐÃ SỬA THEO YÊU CẦU CỦA LỖI 1007: THAY mediaChunks BẰNG audio
            ws.send(JSON.stringify({
              realtimeInput: {
                audio: { mimeType: "audio/pcm;rate=16000", data: base64Audio }
              }
            }));

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
          if (rawData instanceof Blob) {
            rawData = await rawData.text();
          }
          
          const msg = JSON.parse(rawData);
          
          if (msg.error) {
             console.error("🚨 LỖI:", msg.error);
             alert("LỖI NGẮT KẾT NỐI:\n" + msg.error);
             stopCall();
             return;
          }

          if (msg.setupComplete) {
             console.log("✅ GOOGLE ĐÃ SẴN SÀNG NGHE!");
             isSetupCompleteRef.current = true;
             
             // 🚀 GỬI LỆNH MỒI (KICKOFF) BẰNG CHUẨN MỚI CỦA 3.1
             const kickoffMsg = {
                realtimeInput: {
                    text: "Hello, I am ready for the Speaking Test. Please start."
                }
             };
             ws.send(JSON.stringify(kickoffMsg));
             return;
          }
          
          if (msg.serverContent?.modelTurn?.parts) {
             const parts = msg.serverContent.modelTurn.parts;
             for (let part of parts) {
                if (part.text) {
                   setTranscript(prev => prev + " " + part.text);
                }
                if (part.inlineData && part.inlineData.data) {
                   playAIAudio(part.inlineData.data);
                }
             }
          }
        } catch (error) { console.error("LỖI PARSE JSON:", error); }
      };

      ws.onclose = () => stopCall();

    } catch (error) {
      console.error(error);
      alert("Không thể truy cập Micro hoặc Lỗi kết nối!");
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
    if (wsRef.current) wsRef.current.close();
    if (streamRef.current) streamRef.current.getTracks().forEach(t => t.stop());
    if (audioCtxInputRef.current) audioCtxInputRef.current.close();
    if (audioCtxOutputRef.current) audioCtxOutputRef.current.close();
    
    setStatus('IDLE');
    isSetupCompleteRef.current = false;
    setIsMicSending(false);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-slate-900 text-white p-8 w-full">
      <div className="bg-slate-800 p-10 rounded-3xl shadow-2xl border border-slate-700 max-w-xl w-full text-center">
        <h2 className="text-3xl font-black mb-2 tracking-wide">Test Phòng Thi Live</h2>
        <p className="text-slate-400 mb-8 font-medium">Giao tiếp Real-time với Giám khảo AI</p>

        {status === 'IDLE' && (
          <button onClick={startCall} className="w-full bg-emerald-500 hover:bg-emerald-600 text-white font-bold py-4 rounded-xl text-lg transition-transform active:scale-95 shadow-lg shadow-emerald-500/30 flex items-center justify-center gap-3">
             <span className="text-2xl">📞</span> Gọi Giám Khảo Ngay
          </button>
        )}

        {status === 'CONNECTING' && (
           <div className="py-4 text-emerald-400 font-bold animate-pulse">
               Đang kết nối ống dẫn lên Server...
           </div>
        )}

        {status === 'CONNECTED' && (
          <div className="flex flex-col items-center">
            <div className="relative mb-8 mt-4">
               <div className={`absolute inset-0 bg-emerald-500 rounded-full transition-all duration-100 opacity-20 ${isMicSending ? 'scale-150' : 'scale-110'}`}></div>
               <div className="w-24 h-24 bg-emerald-500 rounded-full flex items-center justify-center text-4xl shadow-xl z-10 relative border-4 border-slate-800 transition-transform">
                  🎙️
               </div>
            </div>
            
            <p className="text-emerald-400 font-bold mb-6 tracking-widest uppercase text-sm">
                {isMicSending ? "ĐANG LẮNG NGHE..." : "ĐANG CHỜ TÍN HIỆU..."}
            </p>
            
            <div className="bg-slate-900 rounded-xl p-4 w-full text-left h-40 overflow-y-auto mb-6 border border-slate-700 font-mono text-sm text-slate-300">
               {transcript || "Chờ AI phản hồi..."}
            </div>

            <button onClick={stopCall} className="w-full bg-red-500 hover:bg-red-600 text-white font-bold py-4 rounded-xl text-lg transition-transform active:scale-95 shadow-lg shadow-red-500/30 flex items-center justify-center gap-3">
               <span className="text-2xl">🛑</span> Kết thúc (Cúp máy)
          </button>
          </div>
        )}
      </div>
    </div>
  );
}