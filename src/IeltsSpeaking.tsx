import React, { useState, useRef, useEffect } from 'react';
import { supabase } from './supabase';
import './tailwind.css';

// =========================================================================================
// BỘ ICON CHUẨN IDP
// =========================================================================================
const UserIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
    <path fillRule="evenodd" d="M7.5 6a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM3.751 20.105a8.25 8.25 0 0116.498 0 .75.75 0 01-.437.695A18.683 18.683 0 0112 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 01-.437-.695z" clipRule="evenodd" />
  </svg>
);

const SettingsIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
    <path fillRule="evenodd" d="M11.078 2.25c-.917 0-1.699.663-1.85 1.567L9.05 4.889c-.02.12-.115.26-.297.348a7.493 7.493 0 00-.986.57c-.166.115-.334.126-.45.083L6.3 5.508a1.875 1.875 0 00-2.282.819l-.922 1.597a1.875 1.875 0 00.432 2.385l.84.692c.097.078.15.222.15.399v.111c0 .177-.053.321-.15.399l-.84.692a1.875 1.875 0 00-.432 2.385l.922 1.597a1.875 1.875 0 002.282.818l1.019-.382c.115-.043.283-.031.45.082.312.214.641.405.985.57.182.088.277.228.297.35l.178 1.071c.151.904.933 1.567 1.85 1.567h1.844c.916 0 1.699-.663 1.85-1.567l.178-1.072c.02-.12.114-.26.297-.349.344-.165.673-.356.985-.57.167-.114.335-.125.45-.082l1.02.382a1.875 1.875 0 002.28-.819l.923-1.597a1.875 1.875 0 00-.432-2.385l-.84-.692c-.098-.078-.15-.222-.15-.399v-.111c0-.177.052-.321.15-.399l.84-.692a1.875 1.875 0 00.432-2.385l-.923-1.597a1.875 1.875 0 00-2.28-.818l-1.02.382c-.114.043-.282.031-.449-.083a7.49 7.49 0 00-.985-.57c-.183-.087-.277-.227-.297-.348l-.179-1.072a1.875 1.875 0 00-1.85-1.567h-1.843zM12 15.75a3.75 3.75 0 110-7.5 3.75 3.75 0 010 7.5z" clipRule="evenodd" />
  </svg>
);

const NoteIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-4 h-4">
    <path strokeLinecap="round" strokeLinejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L6.832 19.82a4.5 4.5 0 01-1.89.11l-3.125-3.125a4.5 4.5 0 011.11-1.89l12.45-12.45c.414-.415 1.086-.415 1.498 0z" />
  </svg>
);

const PlayIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
    <path fillRule="evenodd" d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z" clipRule="evenodd" />
  </svg>
);

const TrashIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5">
    <path strokeLinecap="round" strokeLinejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
  </svg>
);

// === HÀM HỖ TRỢ XỬ LÝ ÂM THANH LIVE ===
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

// =========================================================================================
// MAIN COMPONENT
// =========================================================================================
export default function IeltsSpeaking({ 
  onBack, 
  testData: propTestData, 
  onFinish 
}: { 
  onBack?: () => void, 
  testData?: any, 
  onFinish?: (res: any) => void 
}) {
  
  // 1. Tải dữ liệu bài test
  const [testData, setTestData] = useState<any>(() => {
     if (propTestData) {
         return propTestData;
     }
     try {
       const saved = sessionStorage.getItem('lms_current_test');
       if (saved) {
           return JSON.parse(saved);
       }
       return null;
     } catch (e) { 
         return null; 
     }
  });

  // 2. Xử lý an toàn dữ liệu JSON
  let safeData = testData || {};
  if (typeof safeData === 'string') {
    try { 
        safeData = JSON.parse(safeData); 
    } catch (e) { 
        safeData = {}; 
    }
  }

  let contentJSON = safeData?.content_json || safeData || {};
  if (typeof contentJSON === 'string') {
    try { 
        contentJSON = JSON.parse(contentJSON); 
    } catch (e) { 
        contentJSON = {}; 
    }
  }

  const basicInfo = contentJSON?.basicInfo || { title: "IELTS Speaking", timeLimit: "15" };
  const parts = Array.isArray(contentJSON?.parts) ? contentJSON.parts : [];

  // 3. Xây dựng danh sách câu hỏi phẳng
  const allQuestions: any[] = [];
  
  if (Array.isArray(parts)) {
    parts.forEach((p: any, pIdx: number) => {
      if (p && Array.isArray(p.sections)) {
        p.sections.forEach((s: any, sIdx: number) => {
          if (s && Array.isArray(s.questions)) {
            s.questions.forEach((q: any, qIdx: number) => {
              if (q) {
                let maxTime = 60; // Mặc định Part 1 / Part 3 là 60s
                
                const titleToCheck = ((p.title || '') + ' ' + (s.title || '')).toLowerCase();
                
                if (titleToCheck.includes('part 2') || titleToCheck.includes('cue card')) {
                    maxTime = 180; // Part 2 là 180s (3 phút)
                } else if (titleToCheck.includes('part 3') || titleToCheck.includes('discussion')) {
                    maxTime = 60;
                }

                allQuestions.push({
                  ...q,
                  globalIndex: allQuestions.length,
                  partTitle: p.title,
                  partContent: p.content,
                  partIndex: pIdx,
                  secTitle: s.title,
                  secIndex: sIdx,
                  maxTime: maxTime,
                  isPart2: maxTime === 180 
                });
              }
            });
          }
        });
      }
    });
  }

  // 4. Các state điều khiển ứng dụng
  const [currentQIndex, setCurrentQIndex] = useState(0);
  const currentQ = allQuestions[currentQIndex];
  const totalQuestions = allQuestions.length;

  const [notes, setNotes] = useState<Record<string, string>>({}); 
  const [recordedBlobs, setRecordedBlobs] = useState<Record<string, Blob[]>>({}); 
  const [audioUrls, setAudioUrls] = useState<Record<string, string>>({}); 
  const [reviewFlags, setReviewFlags] = useState<Record<number, boolean>>({});

  // 🚀 TRẠNG THÁI GỌI ĐIỆN LIVE VỚI AI
  const [liveStatus, setLiveStatus] = useState<'IDLE' | 'CONNECTING' | 'CONNECTED'>('IDLE');
  const [liveTranscript, setLiveTranscript] = useState<string>('');
  const [isMicSending, setIsMicSending] = useState(false);
  const [recordingTime, setRecordingTime] = useState(0);

  const wsRef = useRef<WebSocket | null>(null);
  const audioCtxInputRef = useRef<AudioContext | null>(null);
  const audioCtxOutputRef = useRef<AudioContext | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const nextPlayTimeRef = useRef<number>(0);
  const isSetupCompleteRef = useRef<boolean>(false);
  
  // 🚀 GHIM BỘ NHỚ CHỐNG GARBAGE COLLECTION CHO AUDIO NODE
  const sourceNodeRef = useRef<MediaStreamAudioSourceNode | null>(null);
  const processorNodeRef = useRef<ScriptProcessorNode | null>(null);
  const gainNodeRef = useRef<GainNode | null>(null);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const timerRef = useRef<any>(null);
  const playbackAudioRef = useRef<HTMLAudioElement | null>(null);
  const [isPlayingRecording, setIsPlayingRecording] = useState(false);

  const stopRecordingPlayback = () => {
    if (playbackAudioRef.current) {
      playbackAudioRef.current.pause();
      playbackAudioRef.current.currentTime = 0;
      playbackAudioRef.current = null;
    }
    setIsPlayingRecording(false);
  };

  useEffect(() => {
    stopRecordingPlayback();
    return () => stopRecordingPlayback();
  }, [currentQIndex]);

  const toggleRecordingPlayback = (url: string) => {
    if (isPlayingRecording && playbackAudioRef.current) {
      stopRecordingPlayback();
      return;
    }
    stopRecordingPlayback();
    const audio = new Audio(url);
    playbackAudioRef.current = audio;
    audio.onended = () => {
      setIsPlayingRecording(false);
      playbackAudioRef.current = null;
    };
    audio.play().then(() => setIsPlayingRecording(true)).catch(() => setIsPlayingRecording(false));
  };

  const handleSafeExit = () => {
    const hasProgress = liveStatus !== 'IDLE' || Object.keys(recordedBlobs).length > 0;
    if (!isSubmitted && hasProgress) {
      if (!window.confirm('Bạn đang có bản ghi âm chưa nộp. Bạn có chắc muốn thoát không?')) return;
    }
    stopRecordingPlayback();
    if (onBack) onBack();
  };
  
  const [isGrading, setIsGrading] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);
  useEffect(() => { window.dispatchEvent(new CustomEvent('tony-review-mode-change', { detail: Boolean(isSubmitted) })); return () => { window.dispatchEvent(new CustomEvent('tony-review-mode-change', { detail: false })); }; }, [isSubmitted]);
  const [aiResult, setAiResult] = useState<any>(null);

  // 5. Điều khiển thời gian đếm ngược tổng
  const parseTime = (t: any) => parseInt(t) || 15; 
  const [timeLeft, setTimeLeft] = useState(() => parseTime(basicInfo.timeLimit) * 60);

  useEffect(() => {
    if (isSubmitted || isGrading) return;
    const timer = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) { clearInterval(timer); handleFinalSubmit(); return 0; }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timer);
  }, [isSubmitted, isGrading]);

  useEffect(() => {
    // Dọn dẹp kết nối khi unmount component
    return () => stopLiveCall();
  }, []);

  const formatTime = (secs: number) => {
    if (isNaN(secs)) return '00:00';
    const m = Math.floor(secs / 60).toString().padStart(2, '0');
    const s = (secs % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  };

  const formatTotalTime = (secs: number) => {
    if (isNaN(secs)) return '15 minutes left';
    const m = Math.floor(secs / 60);
    return `${m} minutes left`;
  };

  // =========================================================================================
  // LOGIC LIVE CALL VÀ THU ÂM KÉP (MEDIA RECORDER + GEMINI WEBSOCKET)
  // =========================================================================================
  const startLiveCall = async () => {
    if (!currentQ?.id) return;
    
    try {
      setLiveStatus('CONNECTING');
      isSetupCompleteRef.current = false;
      setIsMicSending(false);
      setLiveTranscript('');
      setRecordingTime(0);

      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      streamRef.current = stream;

      // 1. CHẠY THU ÂM NGẦM BẰNG MEDIA RECORDER
      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;
      audioChunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) audioChunksRef.current.push(event.data);
      };

      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
        const audioUrl = URL.createObjectURL(audioBlob);
        setRecordedBlobs(prev => ({ ...prev, [currentQ.id]: [audioBlob] }));
        setAudioUrls(prev => ({ ...prev, [currentQ.id]: audioUrl }));
      };

      mediaRecorder.start();

      timerRef.current = setInterval(() => {
        setRecordingTime(prev => {
           if (prev >= currentQ.maxTime - 1) {
              stopLiveCall(); // Hết giờ thì ngắt
              return currentQ.maxTime;
           }
           return prev + 1;
        });
      }, 1000);

      // 2. MỞ LUỒNG TRỰC TIẾP VỚI GEMINI AI
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
        setLiveStatus('CONNECTED');
        
        const plainQuestion = currentQ.content ? currentQ.content.replace(/<[^>]+>/g, '') : "Please ask me an IELTS speaking question.";
        const setupMsg = {
          setup: {
            model: "models/gemini-3.1-flash-live-preview",
            generationConfig: {
              responseModalities: ["AUDIO"],
              speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Puck" } } }
            },
            systemInstruction: {
              parts: [{ text: `Bạn là giám khảo IELTS tên Tony đến từ nước Anh. Hãy đóng vai giám khảo và hỏi tôi câu hỏi sau đây. Trả lời cực kỳ ngắn gọn và tự nhiên như đang giao tiếp. Câu hỏi: ${plainQuestion}` }]
            }
          }
        };
        ws.send(JSON.stringify(setupMsg));
        
        // Gán vào Ref để chống Garbage Collection
        sourceNodeRef.current = audioCtxInputRef.current!.createMediaStreamSource(stream);
        processorNodeRef.current = audioCtxInputRef.current!.createScriptProcessor(4096, 1, 1);
        gainNodeRef.current = audioCtxInputRef.current!.createGain();
        gainNodeRef.current.gain.value = 0;

        let chunkCounter = 0;
        processorNodeRef.current.onaudioprocess = (e) => {
          if (ws.readyState === WebSocket.OPEN && isSetupCompleteRef.current) {
            const inputData = e.inputBuffer.getChannelData(0);
            const pcm16Buffer = floatTo16BitPCM(inputData);
            const base64Audio = arrayBufferToBase64(pcm16Buffer);
            
            ws.send(JSON.stringify({
              realtimeInput: { audio: { mimeType: "audio/pcm;rate=16000", data: base64Audio } }
            }));

            chunkCounter++;
            if (chunkCounter % 5 === 0) setIsMicSending(prev => !prev);
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
             console.error("🚨 LỖI:", msg.error);
             stopLiveCall();
             return;
          }

          if (msg.setupComplete) {
             isSetupCompleteRef.current = true;
             const kickoffMsg = { realtimeInput: { text: "Hello, I am ready. Please ask me the question." } };
             ws.send(JSON.stringify(kickoffMsg));
             return;
          }
          
          if (msg.serverContent?.modelTurn?.parts) {
             const parts = msg.serverContent.modelTurn.parts;
             for (let part of parts) {
                if (part.text) setLiveTranscript(prev => prev + " " + part.text);
                if (part.inlineData && part.inlineData.data) playAIAudio(part.inlineData.data);
             }
          }
        } catch (error) {}
      };

      ws.onclose = () => stopLiveCall();

    } catch (err) {
      alert("System Error: Unable to access microphone. Please check your browser permissions.");
      setLiveStatus('IDLE');
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

  const stopLiveCall = () => {
    if (mediaRecorderRef.current && mediaRecorderRef.current.state !== 'inactive') {
      mediaRecorderRef.current.stop();
    }
    if (wsRef.current) wsRef.current.close();
    if (streamRef.current) streamRef.current.getTracks().forEach(t => t.stop());
    
    if (sourceNodeRef.current) sourceNodeRef.current.disconnect();
    if (processorNodeRef.current) processorNodeRef.current.disconnect();
    if (gainNodeRef.current) gainNodeRef.current.disconnect();

    if (audioCtxInputRef.current) audioCtxInputRef.current.close();
    if (audioCtxOutputRef.current) audioCtxOutputRef.current.close();
    
    setLiveStatus('IDLE');
    isSetupCompleteRef.current = false;
    setIsMicSending(false);
    clearInterval(timerRef.current);
  };

  const deleteRecording = () => {
    if (!window.confirm("Bạn có chắc chắn muốn xóa file ghi âm này để thu lại từ đầu?")) {
        return;
    }
    
    const newBlobs = { ...recordedBlobs }; 
    delete newBlobs[currentQ.id];
    
    const newUrls = { ...audioUrls }; 
    delete newUrls[currentQ.id];
    
    setRecordedBlobs(newBlobs);
    setAudioUrls(newUrls);
    setRecordingTime(0);
    setLiveTranscript('');
  };

  // =========================================================================================
  // LOGIC ĐIỀU HƯỚNG CÂU HỎI
  // =========================================================================================
  const handleReviewToggle = () => {
    setReviewFlags(prev => ({ 
        ...prev, 
        [currentQIndex]: !prev[currentQIndex] 
    }));
  };

  const goToNext = () => {
    if (liveStatus !== 'IDLE') stopLiveCall(); 
    if (currentQIndex < totalQuestions - 1) {
        setCurrentQIndex(prev => prev + 1);
    }
  };

  const goToPrev = () => {
    if (liveStatus !== 'IDLE') stopLiveCall();
    if (currentQIndex > 0) {
        setCurrentQIndex(prev => prev - 1);
    }
  };

  const goToQuestion = (idx: number) => {
    if (liveStatus !== 'IDLE') stopLiveCall();
    setCurrentQIndex(idx);
  };

  const blobToBase64 = (blob: Blob): Promise<string> => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onloadend = () => {
          resolve((reader.result as string).split(',')[1]);
      };
      reader.onerror = reject;
      reader.readAsDataURL(blob);
    });
  };

  // =========================================================================================
  // LOGIC NỘP BÀI CHẤM ĐIỂM (AI GRADER)
  // =========================================================================================
  const handleFinalSubmit = async () => {
    if (liveStatus !== 'IDLE') {
        stopLiveCall();
    }
    
    const answeredQuestions = Object.keys(recordedBlobs).length;
    if (answeredQuestions === 0) {
      alert("Bạn chưa gọi điện với Giám khảo câu nào cả! Vui lòng hoàn thành ít nhất 1 câu.");
      return;
    }

    if (!window.confirm(`Bạn đã hoàn thành ${answeredQuestions}/${totalQuestions} câu. Bạn đã sẵn sàng nộp bài cho hệ thống chấm điểm?`)) {
        return;
    }

    setIsGrading(true);

    try {
      const allChunks: Blob[] = [];
      
      allQuestions.forEach(q => { 
          if (recordedBlobs[q.id]) {
              allChunks.push(...recordedBlobs[q.id]); 
          }
      });
      
      const combinedBlob = new Blob(allChunks, { type: 'audio/webm' });
      const base64Audio = await blobToBase64(combinedBlob);

      const prompt = `
        Bạn là Giám khảo IELTS. Hãy nghe đoạn ghi âm tổng hợp các câu trả lời sau:
        ${JSON.stringify(allQuestions.map((q, i) => `Câu ${i+1} (${q.partTitle}): ${q.content}`))}
        
        Nhiệm vụ:
        1. Chấm điểm Overall và 4 tiêu chí.
        2. Cung cấp Lời giải chi tiết (Transcript).
        3. Đưa ra các gợi ý cải thiện Phát âm, Từ vựng, Trôi chảy.
        
        LƯU Ý ĐỊNH DẠNG:
        - KHÔNG dùng dấu ngoặc kép (") bên trong nội dung string. Dùng dấu (').
        - Trả về ĐÚNG CẤU TRÚC JSON sau:
        {
          "overall": 6.5,
          "criteria": {
            "pronunciation": 6.0,
            "grammar": 6.5,
            "lexicalResource": 7.0,
            "fluency": 6.5
          },
          "transcript": "Văn bản bóc băng...",
          "feedback": {
            "general": "Nhận xét tổng quan...",
            "pronunciation": "Các lỗi phát âm cần sửa...",
            "vocabulary": "Từ vựng có thể nâng cấp...",
            "fluency": "Cách nói trôi chảy hơn...",
            "modelAnswer": "Gợi ý câu trả lời mẫu..."
          }
        }
      `;

      const { data, error } = await supabase.functions.invoke('ai-grader', {
        body: { 
            prompt: prompt, 
            base64Audio: base64Audio, 
            model: 'gemini-2.5-flash' 
        }
      });

      if (error) {
          throw new Error("Lỗi gọi Server: " + error.message);
      }
      if (data?.error) {
          throw new Error("Lỗi chấm điểm AI: " + data.error);
      }

      const textResponse = data.result.replace(/\u0060{3}(json)?/gi, "").trim();
      const parsedResult = JSON.parse(textResponse);
      
      setAiResult(parsedResult);
      setIsSubmitted(true);

      const { data: { user } } = await supabase.auth.getUser();
      if (user) {
        await supabase.from('test_results').insert([{
          user_id: user.id,
          course_id: safeData?.course_id || null,
          test_title: basicInfo.title,
          test_type: 'IELTS-Speaking',
          score: parsedResult.overall,
          total_score: 9,
          time_spent: (parseTime(basicInfo.timeLimit) * 60) - timeLeft,
          details: { 
              test_id: safeData?.id, 
              aiFeedback: parsedResult, 
              bandScore: parsedResult.overall 
          }
        }]);
      }
      
    } catch (error: any) {
      console.error("LỖI CHI TIẾT:", error);
      alert("System Error during AI grading. Please try again: " + error.message);
    } finally {
      setIsGrading(false);
    }
  };

  // =========================================================================================
  // GIAO DIỆN CHÍNH
  // =========================================================================================
  if (!testData || allQuestions.length === 0) {
      return (
          <div className="h-screen flex items-center justify-center bg-[#eeeeee] font-bold text-slate-500">
              Loading test data...
          </div>
      );
  }

  return (
    <div className="h-screen flex flex-col bg-[#eeeeee] font-sans text-black overflow-hidden">
      
      {/* HEADER */}
      <header className="h-[52px] bg-[#1e293b] text-white flex justify-between items-center gap-3 px-4 shrink-0 select-none z-20 border-b border-slate-700">
        <div className="flex items-center gap-2 min-w-0 flex-1">
          <UserIcon />
          <span className="font-bold text-[14px] truncate text-white">
              {basicInfo.title}
          </span>
        </div>
        
        <div className={`font-bold text-[14px] sm:text-[15px] tracking-wider shrink-0 tabular-nums px-3 py-1 rounded-lg bg-white/10 ${timeLeft <= 300 && !isSubmitted ? 'text-rose-400 animate-pulse' : 'text-white'}`}>
           {isSubmitted ? 'TEST FINISHED' : formatTotalTime(timeLeft)}
        </div>

        <div className="flex items-center justify-end gap-3 shrink-0 flex-1">
           {isSubmitted ? (
              <button type="button" onClick={onBack} className="text-[13px] font-bold bg-[#2ab4e8] hover:bg-[#1fa0d4] text-white px-4 py-1.5 rounded-lg transition cursor-pointer">
                  Quay lại Góc Học Viên
              </button>
           ) : (
              <button type="button" onClick={handleSafeExit} className="text-[13px] font-bold px-3.5 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 text-slate-100 border border-white/15 transition cursor-pointer">
                  Thoát
              </button>
           )}
        </div>
      </header>

      {/* OVERLAY ĐANG CHẤM ĐIỂM */}
      {isGrading && (
        <div className="flex-1 flex flex-col items-center justify-center bg-white/95 z-50 absolute inset-0 pt-10">
          <div className="relative flex items-center justify-center w-28 h-28 mb-6">
             <svg className="absolute inset-0 w-full h-full animate-spin text-[#0a5482]" viewBox="0 0 100 100">
               <circle cx="50" cy="50" r="45" fill="none" stroke="currentColor" strokeWidth="8" strokeDasharray="200" strokeLinecap="round" />
             </svg>
             <span className="font-black text-xl text-[#0a5482]">AI</span>
          </div>
          <h2 className="text-xl font-black text-slate-800 mb-2">Đang chấm điểm IELTS Speaking...</h2>
          <p className="text-slate-500 font-medium text-sm">Vui lòng đợi trong giây lát để giám khảo AI phân tích bài nói của bạn.</p>
        </div>
      )}

      {/* MÀN HÌNH LÀM BÀI */}
      {!isSubmitted && !isGrading && currentQ && (
        <div className="flex-1 flex flex-col overflow-hidden bg-[#eeeeee]">
          
          <div className="h-[52px] bg-white border-b border-slate-300 flex items-center px-5 sm:px-8 shrink-0">
            <h2 className="font-black text-[16px] sm:text-[18px] text-[#0a5482] truncate">
                {currentQ.partTitle}
            </h2>
          </div>

          <main className="flex-1 flex flex-col md:flex-row overflow-y-auto md:overflow-hidden relative">
            
            {/* Cột trái: Đề bài */}
            <section className="w-full md:w-1/2 p-5 sm:p-8 md:p-10 md:overflow-y-auto custom-scrollbar border-b md:border-b-0 md:border-r border-slate-300 flex flex-col bg-white shrink-0">
              <div className="max-w-2xl text-[16px] leading-[1.8] text-slate-900 font-sans break-words">
                {currentQ.partContent && (
                  <div className="mb-6 text-[15px] font-medium" dangerouslySetInnerHTML={{__html: currentQ.partContent}} />
                )}
                {currentQ.content && (
                  <div className={`mb-6 text-slate-900 text-[16px] tracking-tight leading-[1.8] ${currentQ.isPart2 ? 'bg-slate-50 p-5 sm:p-6 border border-slate-200 rounded-2xl' : ''}`}>
                    {currentQ.secTitle && currentQ.secTitle.toLowerCase() !== 'section 1' && (
                        <div className="font-bold text-[#0a5482] mb-3">{currentQ.secTitle}</div>
                    )}
                    <div dangerouslySetInnerHTML={{__html: currentQ.content}} />
                  </div>
                )}
              </div>
            </section>

            {/* Cột phải: Ghi chú & Điều khiển Gọi điện */}
            <section className="w-full md:w-1/2 bg-slate-100 flex flex-col md:overflow-hidden relative shrink-0 md:shrink">
              
              <div className="flex-1 p-5 sm:p-8 md:p-10 pb-0 flex flex-col gap-5 md:overflow-hidden">
                  
                  {/* 🚀 KHUNG TRANSCRIPT LIVE: HIỆN LÊN KHI ĐANG GỌI */}
                  {(liveStatus !== 'IDLE' || liveTranscript) && (
                     <div className="flex-1 min-h-[200px] bg-slate-900 border border-slate-700 rounded-2xl flex flex-col overflow-hidden shadow-inner">
                        <div className="h-11 border-b border-slate-700 flex items-center px-4 gap-3 shrink-0 bg-slate-800">
                           <div className={`w-2.5 h-2.5 rounded-full ${isMicSending ? 'bg-emerald-500 animate-pulse' : 'bg-slate-500'}`}></div>
                           <span className="text-[12px] font-bold text-emerald-400 uppercase tracking-widest">
                               {liveStatus === 'CONNECTING' ? 'Connecting...' : 'Live Interview Transcript'}
                           </span>
                        </div>
                        <div className="flex-1 p-5 overflow-y-auto custom-scrollbar text-[14.5px] text-slate-200 font-mono leading-[1.8]">
                           {liveTranscript || <span className="opacity-50 italic">AI Examiner is listening...</span>}
                        </div>
                     </div>
                  )}

                  {/* KHUNG NOTES: TỰ THU GỌN KHI CÓ LIVE TRANSCRIPT */}
                  <div className={`bg-white border border-slate-200/90 rounded-2xl shadow-sm flex flex-col overflow-hidden transition-all duration-300 ${liveStatus === 'IDLE' && !liveTranscript ? 'flex-1 min-h-[220px]' : 'h-40 shrink-0'}`}>
                    <div className="h-11 border-b border-slate-200 flex items-center px-4 gap-2 shrink-0 bg-slate-50">
                       <NoteIcon />
                       <span className="text-[12.5px] font-extrabold text-slate-700 uppercase tracking-widest">Notes</span>
                    </div>
                    <textarea 
                      className="flex-1 w-full p-5 outline-none resize-none text-[15px] text-slate-900 font-sans custom-scrollbar leading-[1.8]"
                      placeholder="You can make some notes here..."
                      value={notes[currentQ.id] || ''}
                      onChange={(e) => setNotes(prev => ({...prev, [currentQ.id]: e.target.value}))}
                      spellCheck="false"
                    />
                  </div>
              </div>

              <div className="p-5 sm:p-8 md:p-10 shrink-0">
                  <div className="min-h-[82px] bg-white border border-slate-200/90 rounded-2xl shadow-sm flex items-center justify-between px-4 sm:px-6 py-3">
                      
                      {audioUrls[currentQ.id] ? (
                         <div className="flex items-center gap-3 sm:gap-4 w-full">
                            <button
                              type="button"
                              onClick={() => toggleRecordingPlayback(audioUrls[currentQ.id])}
                              className={`w-10 h-10 rounded-xl flex items-center justify-center transition cursor-pointer shrink-0 ${
                                isPlayingRecording
                                  ? 'bg-[#0a5482] text-white shadow-sm'
                                  : 'bg-sky-50 border border-sky-200 hover:bg-sky-100 text-[#0a5482]'
                              }`}
                              title={isPlayingRecording ? 'Dừng phát' : 'Nghe lại bản ghi'}
                            >
                               {isPlayingRecording ? <span className="text-xs font-black">❚❚</span> : <PlayIcon />}
                            </button>
                            <div className="flex-1 h-2 bg-slate-200 rounded-full overflow-hidden">
                               <div className={`h-full rounded-full transition-all ${isPlayingRecording ? 'bg-[#2ab4e8] animate-pulse w-full' : 'bg-[#0a5482] w-full'}`}></div>
                            </div>
                            <span className="text-[13px] font-bold text-slate-700 hidden sm:block">
                              {isPlayingRecording ? 'Đang phát...' : 'Interview Saved'}
                            </span>
                            <button
                              type="button"
                              onClick={() => { stopRecordingPlayback(); deleteRecording(); }}
                              className="w-10 h-10 rounded-xl text-slate-600 hover:text-white hover:bg-rose-600 transition flex items-center justify-center border border-slate-200 cursor-pointer shrink-0"
                              title="Xóa & Ghi lại"
                            >
                               <TrashIcon />
                            </button>
                         </div>
                      ) : (
                         <div className="flex items-center flex-wrap gap-3 sm:gap-5 w-full">
                            {liveStatus === 'IDLE' ? (
                               <button type="button" onClick={startLiveCall} className="px-6 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl flex items-center gap-2.5 transition active:scale-95 text-[14.5px] shadow-md shadow-emerald-600/20 cursor-pointer">
                                 📞 Bắt đầu gọi Giám khảo
                               </button>
                            ) : liveStatus === 'CONNECTING' ? (
                               <div className="text-emerald-600 font-bold animate-pulse flex items-center gap-2 text-[15px] px-4">
                                  Đang kết nối...
                               </div>
                            ) : (
                               <button type="button" onClick={stopLiveCall} className="px-6 py-2.5 bg-rose-600 hover:bg-rose-700 text-white font-bold rounded-xl flex items-center gap-2.5 transition active:scale-95 text-[14.5px] shadow-md shadow-rose-600/20 cursor-pointer">
                                 🛑 Kết thúc cuộc gọi
                               </button>
                            )}
                            
                            {liveStatus === 'CONNECTED' ? (
                               <div className="font-mono text-[15px] text-emerald-600 font-bold tracking-wider tabular-nums flex items-center gap-2 ml-auto">
                                 <span className="w-2.5 h-2.5 bg-emerald-500 rounded-full animate-ping"></span>
                                 {formatTime(recordingTime)} <span className="text-slate-700">/ {formatTime(currentQ.maxTime)}</span>
                               </div>
                            ) : liveStatus === 'IDLE' && (
                               <div className="text-[12.5px] text-slate-600 font-bold tracking-wider uppercase ml-auto">Max: {formatTime(currentQ.maxTime)}</div>
                            )}
                         </div>
                      )}

                  </div>
              </div>

            </section>
          </main>

          {/* Footer Navigation */}
          <footer className="h-[60px] bg-white border-t border-slate-300 flex justify-between items-center px-4 sm:px-6 shrink-0 select-none overflow-x-auto custom-scrollbar">
             
             <div className="flex items-center h-full shrink-0">
                <label className="flex items-center gap-2 cursor-pointer h-full pr-4 sm:pr-6 border-r border-slate-200">
                   <input 
                     type="checkbox" 
                     className="w-4 h-4 cursor-pointer accent-[#0a5482]" 
                     checked={!!reviewFlags[currentQIndex]}
                     onChange={handleReviewToggle}
                   />
                   <span className="text-[13px] sm:text-[14px] font-bold text-slate-700 whitespace-nowrap">Review</span>
                </label>
                
                <div className="flex items-center gap-2 h-full pl-4 sm:pl-6">
                   {allQuestions.map((q, idx) => {
                      const isActive = idx === currentQIndex;
                      const isReview = reviewFlags[idx];
                      const isAnswered = !!recordedBlobs[q.id];
                      
                      const shapeClass = isReview ? 'rounded-full' : 'rounded-lg';
                      
                      let bgClass = 'bg-white text-slate-700 border-slate-300 hover:bg-slate-100';
                      if (isActive) {
                          bgClass = 'bg-[#0a5482] text-white border-[#0a5482] shadow-sm';
                      } else if (isAnswered) {
                          bgClass = 'bg-emerald-100 text-emerald-800 border-emerald-400 font-black';
                      }

                      return (
                        <button 
                          key={q.id}
                          type="button"
                          onClick={() => goToQuestion(idx)}
                          className={`w-8 h-9 flex items-center justify-center font-bold text-[13px] border transition-all cursor-pointer ${shapeClass} ${bgClass}`}
                          title={`Part ${q.partIndex + 1} - Question ${idx + 1}`}
                        >
                          {idx + 1}
                        </button>
                      )
                   })}
                </div>
             </div>

             <div className="flex items-center gap-3 sm:gap-5 shrink-0 pl-4">
                <div className="flex items-center gap-2">
                   <button type="button" onClick={goToPrev} disabled={currentQIndex === 0} className="w-9 h-9 flex items-center justify-center text-slate-700 hover:bg-slate-100 border border-slate-300 bg-white rounded-lg transition disabled:opacity-30 cursor-pointer">←</button>
                   <button type="button" onClick={goToNext} disabled={currentQIndex === totalQuestions - 1} className="w-9 h-9 flex items-center justify-center text-slate-700 hover:bg-slate-100 border border-slate-300 bg-white rounded-lg transition disabled:opacity-30 cursor-pointer">→</button>
                </div>
                
                <button 
                  type="button"
                  onClick={handleFinalSubmit}
                  className="bg-[#0a5482] hover:bg-[#084266] text-white px-6 sm:px-7 py-2 rounded-xl text-[13px] sm:text-[14px] font-black transition active:scale-95 uppercase tracking-wide shadow-sm cursor-pointer"
                >
                  Nộp bài
                </button>
             </div>

          </footer>

        </div>
      )}

      {/* MÀN HÌNH HIỂN THỊ KẾT QUẢ CHẤM ĐIỂM */}
      {isSubmitted && aiResult && (
        <main className="flex-1 overflow-y-auto p-4 md:p-8 custom-scrollbar bg-slate-50">
          <div className="max-w-5xl mx-auto space-y-6">
            
            <div className="bg-gradient-to-br from-[#073b5c] via-[#0a5482] to-[#0f172a] p-7 sm:p-9 rounded-3xl shadow-xl border border-sky-400/20 text-white relative overflow-hidden">
              <div className="absolute -top-16 -right-16 w-56 h-56 bg-[#2ab4e8]/20 blur-3xl rounded-full pointer-events-none" />
              <div className="relative z-10 flex flex-col md:flex-row gap-6 items-center justify-between">
                <div className="text-center md:text-left">
                  <span className="inline-flex items-center gap-1.5 text-xs font-extrabold uppercase tracking-widest text-[#2ab4e8] mb-2">
                    🎙️ IELTS Speaking AI Evaluation
                  </span>
                  <h2 className="text-2xl sm:text-3xl font-black tracking-tight mb-2">{basicInfo.title}</h2>
                  <button 
                    type="button"
                    onClick={() => {
                      const tutorContext = {
                        transcript: aiResult.transcript,
                        criteria: aiResult.criteria,
                        feedback: JSON.stringify(aiResult.detailedFeedback || aiResult.feedback),
                        overall: aiResult.overall
                      };
                      sessionStorage.setItem('tony_live_mode', 'TUTOR');
                      sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
                      sessionStorage.setItem('tony_auto_start', 'true');
                      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
                    }}
                    className="mt-2 inline-flex items-center justify-center gap-2 bg-[#2ab4e8] hover:bg-[#1fa0d4] text-white font-black py-2.5 px-6 rounded-xl transition-all shadow-lg active:scale-95 cursor-pointer text-sm"
                  >
                    <span>📞</span> Gọi Gia sư AI giải thích lỗi sai
                  </button>
                </div>
                <div className="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl px-8 py-4 text-center shrink-0">
                  <span className="text-[11px] font-extrabold text-sky-200 uppercase tracking-widest block mb-1">
                      Overall Band
                  </span>
                  <span className="text-5xl sm:text-6xl font-black text-white tabular-nums">
                      {aiResult.overall}
                  </span>
                </div>
              </div>
            </div>

            <div className="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200/90 shadow-sm">
                <h3 className="font-black text-lg text-[#0a5482] mb-3.5 flex items-center gap-2">💡 Nhận xét tổng quan</h3>
                <div className="p-5 bg-sky-50/70 border border-sky-200/70 rounded-xl text-[15px] leading-[1.8] font-medium text-slate-800 font-sans">
                  {aiResult.generalFeedback || 'Hệ thống đã ghi nhận bài thi Speaking của bạn.'}
                </div>
            </div>

            <div className="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200/90 shadow-sm space-y-6">
                <div className="flex justify-between items-center pb-4 border-b border-slate-200">
                  <h3 className="font-black text-xl text-slate-900">Chi tiết các tiêu chí</h3>
                </div>
                
                <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
                   <div className="bg-slate-50 p-5 rounded-2xl border border-slate-200/80 text-center">
                      <div className="text-[11px] text-slate-500 font-extrabold uppercase tracking-wider mb-1.5">Pronunciation</div>
                      <div className="text-3xl font-black text-[#0a5482] tabular-nums">{aiResult.criteria?.pronunciation || 0.0}</div>
                   </div>
                   <div className="bg-slate-50 p-5 rounded-2xl border border-slate-200/80 text-center">
                      <div className="text-[11px] text-slate-500 font-extrabold uppercase tracking-wider mb-1.5">Grammar</div>
                      <div className="text-3xl font-black text-[#0a5482] tabular-nums">{aiResult.criteria?.grammar || 0.0}</div>
                   </div>
                   <div className="bg-slate-50 p-5 rounded-2xl border border-slate-200/80 text-center">
                      <div className="text-[11px] text-slate-500 font-extrabold uppercase tracking-wider mb-1.5">Lexical Resource</div>
                      <div className="text-3xl font-black text-[#0a5482] tabular-nums">{aiResult.criteria?.lexicalResource || 0.0}</div>
                   </div>
                   <div className="bg-slate-50 p-5 rounded-2xl border border-slate-200/80 text-center">
                      <div className="text-[11px] text-slate-500 font-extrabold uppercase tracking-wider mb-1.5">Fluency</div>
                      <div className="text-3xl font-black text-[#0a5482] tabular-nums">{aiResult.criteria?.fluency || 0.0}</div>
                   </div>
                </div>

                <div className="space-y-5 pt-2">
                   <div>
                      <h4 className="font-black text-slate-800 mb-2.5 uppercase tracking-widest text-[12px]">🎧 Bóc băng (Transcript)</h4>
                      <div className="p-5 bg-amber-50/70 border border-amber-200/80 rounded-xl text-[15px] leading-[1.8] font-sans text-slate-800 italic whitespace-pre-wrap">
                         "{aiResult.transcript}"
                      </div>
                   </div>
                   
                   {aiResult.detailedFeedback && (
                   <div>
                      <h4 className="font-black text-slate-800 mb-2.5 uppercase tracking-widest text-[12px]">💡 Gợi ý sửa lỗi chi tiết</h4>
                      <div className="p-5 bg-slate-50 border border-slate-200/80 rounded-xl text-[15px] leading-[1.8] font-medium text-slate-800 whitespace-pre-wrap font-sans">
                         {aiResult.detailedFeedback}
                      </div>
                   </div>
                   )}
                </div>
            </div>

          </div>
        </main>
      )}
    </div>
  );
}