import React, { useState, useRef, useEffect } from 'react';

// === HÀM HỖ TRỢ ĐỔI FORMAT ÂM THANH ===
// 1. Chuyển đổi âm thanh thu được (Float32) sang chuẩn PCM 16-bit mà Gemini yêu cầu
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

// 2. Mã hóa thành chuỗi Base64 để gửi qua WebSocket
const arrayBufferToBase64 = (buffer: ArrayBuffer) => {
  let binary = '';
  const bytes = new Uint8Array(buffer);
  for (let i = 0; i < bytes.byteLength; i++) binary += String.fromCharCode(bytes[i]);
  return window.btoa(binary);
};

// 3. Giải mã chuỗi Base64 của Gemini trả về thành ArrayBuffer
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
  
  const wsRef = useRef<WebSocket | null>(null);
  const audioCtxInputRef = useRef<AudioContext | null>(null);
  const audioCtxOutputRef = useRef<AudioContext | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const nextPlayTimeRef = useRef<number>(0);

  const startCall = async () => {
    try {
      setStatus('CONNECTING');

      // 1. Khởi tạo bộ xử lý âm thanh (Đầu vào 16kHz, Đầu ra 24kHz theo chuẩn Gemini)
      const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
      audioCtxInputRef.current = new AudioContextClass({ sampleRate: 16000 });
      audioCtxOutputRef.current = new AudioContextClass({ sampleRate: 24000 });
      nextPlayTimeRef.current = audioCtxOutputRef.current.currentTime;

      // 2. Mở kết nối tới Edge Function của anh (Thay bằng Project ID trong ảnh của anh)
      const wsUrl = 'wss://ubkvzgwespfvrlpjuxkp.supabase.co/functions/v1/live-speaking';
      const ws = new WebSocket(wsUrl);
      wsRef.current = ws;

      ws.onopen = async () => {
        setStatus('CONNECTED');
        
        // 3. Ngay khi kết nối, gửi lệnh SETUP mớm cho AI
        const setupMsg = {
          setup: {
            model: "models/gemini-2.0-flash-exp",
            systemInstruction: {
              parts: [{ text: "Bạn là giám khảo IELTS tên Tony đến từ Anh. Hãy bắt đầu cuộc thi Speaking Part 1 bằng cách chào hỏi và hỏi tên tôi. Trả lời cực kỳ ngắn gọn." }]
            }
          }
        };
        ws.send(JSON.stringify(setupMsg));

        // 4. Bật Micro và bắt đầu Stream âm thanh lên
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        streamRef.current = stream;
        
        const source = audioCtxInputRef.current!.createMediaStreamSource(stream);
        // Dùng ScriptProcessor để cắt âm thanh thành từng cục nhỏ (4096 frames)
        const processor = audioCtxInputRef.current!.createScriptProcessor(4096, 1, 1);
        
        processor.onaudioprocess = (e) => {
          if (ws.readyState === WebSocket.OPEN) {
            const inputData = e.inputBuffer.getChannelData(0);
            const pcm16Buffer = floatTo16BitPCM(inputData);
            const base64Audio = arrayBufferToBase64(pcm16Buffer);
            
            // Đóng gói và Gửi cục âm thanh nhỏ lên Gemini
            ws.send(JSON.stringify({
              realtimeInput: {
                mediaChunks: [{ mimeType: "audio/pcm;rate=16000", data: base64Audio }]
              }
            }));
          }
        };

        source.connect(processor);
        processor.connect(audioCtxInputRef.current!.destination);
      };

      // 5. Nghe âm thanh AI trả về và phát ra Loa
      ws.onmessage = (event) => {
        try {
          const msg = JSON.parse(event.data);
          
          // AI trả về Text (Transcript)
          if (msg.serverContent?.modelTurn?.parts) {
             const parts = msg.serverContent.modelTurn.parts;
             for (let part of parts) {
                if (part.text) {
                   setTranscript(prev => prev + part.text);
                }
                // AI trả về Giọng nói (Audio)
                if (part.inlineData && part.inlineData.data) {
                   playAIAudio(part.inlineData.data);
                }
             }
          }
        } catch (error) { console.error(error); }
      };

      ws.onclose = () => stopCall();

    } catch (error) {
      console.error(error);
      alert("Không thể truy cập Micro hoặc Lỗi kết nối!");
      setStatus('IDLE');
    }
  };

  // Hàm xếp hàng và phát giọng nói của AI
  const playAIAudio = (base64Audio: string) => {
    if (!audioCtxOutputRef.current) return;
    const ctx = audioCtxOutputRef.current;
    
    // Giải mã Base64 -> ArrayBuffer PCM 16-bit
    const pcmBuffer = base64ToArrayBuffer(base64Audio);
    const int16Array = new Int16Array(pcmBuffer);
    
    // Chuyển Int16 sang Float32 để Loa hiểu được
    const float32Array = new Float32Array(int16Array.length);
    for (let i = 0; i < int16Array.length; i++) {
        float32Array[i] = int16Array[i] / 32768.0;
    }

    // Tạo AudioBuffer 24kHz
    const audioBuffer = ctx.createBuffer(1, float32Array.length, 24000);
    audioBuffer.getChannelData(0).set(float32Array);

    // Chơi nhạc và nối vào Hàng đợi (Queue)
    const sourceNode = ctx.createBufferSource();
    sourceNode.buffer = audioBuffer;
    sourceNode.connect(ctx.destination);

    const playTime = Math.max(ctx.currentTime, nextPlayTimeRef.current);
    sourceNode.start(playTime);
    nextPlayTimeRef.current = playTime + audioBuffer.duration;
  };

  const stopCall = () => {
    wsRef.current?.close();
    if (streamRef.current) {
        streamRef.current.getTracks().forEach(t => t.stop());
    }
    if (audioCtxInputRef.current) audioCtxInputRef.current.close();
    if (audioCtxOutputRef.current) audioCtxOutputRef.current.close();
    
    setStatus('IDLE');
    setTranscript('');
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-slate-900 text-white p-8">
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
               <div className="absolute inset-0 bg-emerald-500 rounded-full animate-ping opacity-20 scale-150"></div>
               <div className="w-24 h-24 bg-emerald-500 rounded-full flex items-center justify-center text-4xl shadow-xl z-10 relative border-4 border-slate-800">
                  🎙️
               </div>
            </div>
            
            <p className="text-emerald-400 font-bold mb-6 tracking-widest uppercase text-sm">Đang trong cuộc gọi...</p>
            
            <div className="bg-slate-900 rounded-xl p-4 w-full text-left h-40 overflow-y-auto mb-6 border border-slate-700 font-mono text-sm text-slate-300">
               {transcript || "AI đang nghe..."}
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