import React, { useState, useRef } from 'react';
import { GoogleGenerativeAI } from '@google/generative-ai';
import './tailwind.css';

export default function IeltsSpeaking({ onBack }: { onBack?: () => void }) {
  const [isRecording, setIsRecording] = useState(false);
  const [recordingTime, setRecordingTime] = useState(0);
  const [isGrading, setIsGrading] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [aiResult, setAiResult] = useState<any>(null);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const timerRef = useRef<any>(null);

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;
      audioChunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          audioChunksRef.current.push(event.data);
        }
      };

      mediaRecorder.onstop = () => {
        stream.getTracks().forEach(track => track.stop());
      };

      mediaRecorder.start();
      setIsRecording(true);
      setRecordingTime(0);

      timerRef.current = setInterval(() => {
        setRecordingTime((prev) => prev + 1);
      }, 1000);

    } catch (err) {
      alert("Lỗi: Không thể truy cập Micro! Anh vui lòng cấp quyền sử dụng Micro cho trình duyệt nhé.");
      console.error(err);
    }
  };

  const stopAndSubmit = () => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
      clearInterval(timerRef.current);
      
      setTimeout(() => {
        processAudioAndGrade();
      }, 500);
    }
  };

  const blobToBase64 = (blob: Blob): Promise<string> => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onloadend = () => {
        const base64String = (reader.result as string).split(',')[1];
        resolve(base64String);
      };
      reader.onerror = reject;
      reader.readAsDataURL(blob);
    });
  };

  const processAudioAndGrade = async () => {
    setIsGrading(true);
    try {
      const apiKey = import.meta.env.VITE_GEMINI_API_KEY;
      if (!apiKey) {
        alert("Lỗi: Không tìm thấy API Key!");
        setIsGrading(false);
        return;
      }

      const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
      const base64Audio = await blobToBase64(audioBlob);

      const genAI = new GoogleGenerativeAI(apiKey);
      const model = genAI.getGenerativeModel({ 
        model: "gemini-2.5-flash", // Giữ nguyên model của anh
        generationConfig: { responseMimeType: "application/json" }
      });

      // Đã nâng cấp Thần chú: Ép AI không được dùng ngoặc kép bên trong văn bản
      const prompt = `
        Bạn là một Giám khảo IELTS chuyên nghiệp. Hãy NGHE đoạn ghi âm phần thi Speaking Part 2 của học sinh và chấm điểm.
        Đề bài Cue Card: "Describe a piece of technology that you find difficult to use."
        
        Nhiệm vụ:
        1. Nghe và bóc băng đoạn hội thoại (Transcript). Chú ý các chỗ phát âm sai.
        2. Chấm điểm theo 4 tiêu chí.
        
        LƯU Ý QUAN TRỌNG VỀ ĐỊNH DẠNG:
        - TUYỆT ĐỐI KHÔNG sử dụng dấu ngoặc kép (") ở bên trong nội dung nhận xét hoặc phần transcript. Nếu cần trích dẫn, hãy dùng dấu ngoặc đơn (').
        - Trả về CHÍNH XÁC định dạng JSON như sau:
        {
          "overall": 6.0,
          "criteria": [
            { "name": "Fluency & Coherence", "score": 6.0, "comment": "Nhận xét..." },
            { "name": "Lexical Resource", "score": 6.0, "comment": "Nhận xét..." },
            { "name": "Grammatical Range", "score": 5.5, "comment": "Nhận xét..." },
            { "name": "Pronunciation", "score": 6.0, "comment": "Nhận xét..." }
          ],
          "transcript": "Văn bản bóc băng tại đây...",
          "detailedFeedback": "Gợi ý cách trả lời..."
        }
      `;

      const result = await model.generateContent([
        prompt,
        {
          inlineData: {
            mimeType: "audio/webm",
            data: base64Audio
          }
        }
      ]);

      const textResponse = result.response.text().replace(/```json/g, '').replace(/```/g, '').trim();
      console.log("🤖 KẾT QUẢ AI TRẢ VỀ GỐC:", textResponse);
      
      const parsedResult = JSON.parse(textResponse);
      setAiResult(parsedResult);
      setIsSubmitted(true);

    } catch (error) {
      console.error("LỖI CHI TIẾT:", error);
      alert("AI đang phân tích bị lỗi định dạng. Anh vui lòng nói lại một đoạn khác thử nhé!");
    } finally {
      setIsGrading(false);
    }
  };

  const formatTime = (seconds: number) => {
    const m = Math.floor(seconds / 60).toString().padStart(2, '0');
    const s = (seconds % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  };

  return (
    <div className="min-h-screen bg-[#f0f2f5] font-sans flex flex-col text-slate-800">
      
      <header className={`px-6 py-3 flex justify-between items-center z-10 shrink-0 shadow ${isSubmitted ? 'bg-emerald-700' : 'bg-[#1f2937]'} text-white`}>
        <div className="flex items-center gap-4">
          <button onClick={onBack} className="bg-black/20 hover:bg-black/40 border border-white/20 text-sm px-3 py-1.5 rounded font-bold transition">⬅ Thoát</button>
          <div className="font-bold text-lg tracking-wide border-l border-white/30 pl-4">
            {isSubmitted ? 'IELTS SPEAKING - KẾT QUẢ' : 'IELTS SPEAKING PART 2'}
          </div>
        </div>
      </header>

      {isGrading && (
        <div className="flex-1 flex flex-col items-center justify-center bg-white/80 backdrop-blur-sm z-50 absolute inset-0">
          <div className="relative mb-8">
             <div className="text-6xl relative z-10">🎧</div>
             <div className="absolute inset-0 bg-blue-400 rounded-full animate-ping opacity-20 scale-150"></div>
          </div>
          <h2 className="text-2xl font-black text-slate-800">AI Đang Nghe Bạn Nói...</h2>
          <p className="text-slate-500 mt-2 font-medium">Giám khảo Gemini đang phân tích phát âm và ngữ điệu, vui lòng chờ chút nhé!</p>
        </div>
      )}

      {!isSubmitted && !isGrading ? (
        <main className="flex-1 flex flex-col md:flex-row overflow-hidden">
          
          <section className="w-full md:w-1/2 p-10 bg-white border-r border-slate-300 overflow-y-auto flex flex-col items-center justify-center">
            <div className="max-w-md w-full bg-amber-50 border border-amber-200 rounded-2xl p-8 shadow-sm">
              <div className="inline-block bg-amber-200 text-amber-800 font-black text-[12px] px-3 py-1 rounded-full uppercase tracking-wider mb-6">
                Candidate Task Card
              </div>
              <h2 className="font-black text-xl text-slate-800 mb-6 leading-tight">
                Describe a piece of technology that you find difficult to use.
              </h2>
              <div className="text-[16px] text-slate-700 font-medium space-y-3 mb-8">
                <p>You should say:</p>
                <ul className="list-disc pl-6 space-y-2 text-slate-600">
                  <li>what it is</li>
                  <li>what you use it for</li>
                  <li>why it is difficult to use</li>
                </ul>
                <p className="pt-2">and explain how you feel about this piece of technology.</p>
              </div>
              <div className="text-[14px] text-amber-700 font-bold bg-white p-4 rounded-xl border border-amber-100">
                ⏱ You will have to talk about the topic for 1 to 2 minutes.
              </div>
            </div>
          </section>

          <section className="w-full md:w-1/2 p-10 bg-slate-50 flex flex-col items-center justify-center relative">
            <div className="text-center">
              
              <div className="relative flex items-center justify-center w-48 h-48 mx-auto mb-8">
                {isRecording && (
                  <>
                    <div className="absolute inset-0 border-4 border-red-500 rounded-full animate-[ping_1.5s_ease-in-out_infinite] opacity-20"></div>
                    <div className="absolute inset-0 border-4 border-red-500 rounded-full animate-[ping_2s_ease-in-out_infinite] opacity-10"></div>
                  </>
                )}
                <div className={`w-32 h-32 rounded-full flex items-center justify-center text-5xl transition-all duration-300 shadow-xl ${isRecording ? 'bg-red-50 text-red-500 border-4 border-red-100 scale-110' : 'bg-white text-slate-400 border border-slate-200'}`}>
                  🎙️
                </div>
              </div>

              <div className={`text-4xl font-black font-mono mb-8 tabular-nums ${isRecording ? 'text-red-500' : 'text-slate-800'}`}>
                {formatTime(recordingTime)}
              </div>

              {!isRecording ? (
                <button onClick={startRecording} className="bg-[#2ab4e8] hover:bg-[#1d9ad1] text-white font-black text-lg px-8 py-4 rounded-2xl transition shadow-lg shadow-cyan-500/30 w-full max-w-xs">
                  ▶ Bắt đầu nói
                </button>
              ) : (
                <button onClick={stopAndSubmit} className="bg-red-500 hover:bg-red-600 text-white font-black text-lg px-8 py-4 rounded-2xl transition shadow-lg shadow-red-500/30 w-full max-w-xs flex items-center justify-center gap-3">
                  <span className="w-4 h-4 bg-white rounded-sm block"></span> Dừng & Chấm điểm
                </button>
              )}

              <p className="text-slate-400 font-medium mt-6 text-sm">
                *Hệ thống sẽ yêu cầu quyền truy cập Micro trên trình duyệt của bạn.
              </p>
            </div>
          </section>

        </main>
      ) : (
        isSubmitted && aiResult && (
        <main className="flex-1 overflow-y-auto p-8">
          <div className="max-w-6xl mx-auto space-y-8">
            
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 flex flex-col md:flex-row gap-8 items-center">
              <div className="w-40 h-40 shrink-0 rounded-full border-8 border-emerald-500 flex flex-col items-center justify-center bg-emerald-50 shadow-inner">
                <span className="text-sm font-bold text-emerald-700 uppercase">Overall</span>
                <span className="text-5xl font-black text-emerald-600">{aiResult.overall}</span>
              </div>
              <div className="flex-1 grid grid-cols-1 sm:grid-cols-2 gap-4 w-full">
                {aiResult.criteria.map((c: any, i: number) => (
                  <div key={i} className="bg-slate-50 p-4 rounded-xl border border-slate-200">
                    <div className="flex justify-between items-center mb-2">
                      <span className="font-bold text-slate-700">{c.name}</span>
                      <span className="font-black text-[#2ab4e8] text-lg">{c.score}</span>
                    </div>
                    <p className="text-sm text-slate-600 font-medium leading-relaxed">{c.comment}</p>
                  </div>
                ))}
              </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
                <h3 className="font-black text-xl text-slate-800 mb-6 flex items-center gap-2">🎧 AI Bóc băng (Transcript)</h3>
                <div className="p-6 bg-slate-50 border border-slate-200 rounded-xl text-[15px] leading-loose font-medium text-slate-700 italic">
                  "{aiResult.transcript}"
                </div>
              </div>

              <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
                <h3 className="font-black text-xl text-slate-800 mb-6 flex items-center gap-2">💡 Nhận xét & Gợi ý</h3>
                <div className="p-6 bg-blue-50 border border-blue-200 rounded-xl text-[15px] leading-loose font-medium text-blue-900">
                  {aiResult.detailedFeedback}
                </div>
              </div>
            </div>

          </div>
        </main>
        )
      )}
    </div>
  );
}