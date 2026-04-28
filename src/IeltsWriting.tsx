import React, { useState } from 'react';
import { GoogleGenerativeAI } from '@google/generative-ai';
import './tailwind.css';

export default function IeltsWriting({ onBack }: { onBack?: () => void }) {
  const [text, setText] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [isGrading, setIsGrading] = useState(false);
  
  // State lưu kết quả từ AI
  const [aiResult, setAiResult] = useState<any>(null);

  const wordCount = text.trim() === '' ? 0 : text.trim().split(/\s+/).length;

  const handleSubmit = async () => {
    if (wordCount < 30) {
      alert("Anh gõ thêm tí nữa (ít nhất 30 chữ) cho AI nó có cái mà chấm nhé!");
      return;
    }
    if (!window.confirm("Bạn đã chắc chắn muốn nộp bài? Hệ thống sẽ bắt đầu chấm điểm.")) return;

    setIsGrading(true);

    try {
      // 1. Lấy API Key từ file .env
      const apiKey = import.meta.env.VITE_GEMINI_API_KEY;
      if (!apiKey) {
        alert("Lỗi: Chưa tìm thấy API Key trong file .env!");
        setIsGrading(false);
        return;
      }

      // 2. Khởi tạo Gemini AI
      const genAI = new GoogleGenerativeAI(apiKey);
      
      // Sử dụng model "gemini-1.5-flash-latest" để tránh lỗi 404
      const model = genAI.getGenerativeModel({ 
        model: "gemini-2.5-flash",
        generationConfig: {
          responseMimeType: "application/json", // Ép AI trả về JSON chuẩn
        }
      });

      // 3. Viết Prompt chấm điểm chuyên sâu
      const prompt = `
        Bạn là một Giám khảo IELTS vô cùng khắt khe. Hãy chấm bài Writing Task 2 sau.
        Đề bài: "More and more people are relying on artificial intelligence to complete their daily tasks. Is this a positive or negative development?"
        Bài làm của học sinh: "${text}"

        Hãy phân tích và trả về đúng định dạng JSON sau:
        {
          "overall": 6.5,
          "criteria": [
            { "name": "Task Response", "score": 6.5, "comment": "Nhận xét ngắn gọn..." },
            { "name": "Coherence & Cohesion", "score": 6.0, "comment": "Nhận xét ngắn gọn..." },
            { "name": "Lexical Resource", "score": 7.0, "comment": "Nhận xét ngắn gọn..." },
            { "name": "Grammar", "score": 6.5, "comment": "Nhận xét ngắn gọn..." }
          ],
          "detailedFeedback": "Văn bản bài làm kèm thẻ <span class='bg-red-200 text-red-800 line-through px-1'>từ sai</span> và <span class='bg-emerald-200 text-emerald-800 font-bold px-1'>từ đúng</span>."
        }
      `;

      // 4. Gọi AI và xử lý kết quả
      const result = await model.generateContent(prompt);
      const textResponse = result.response.text();
      
      console.log("🤖 AI Response:", textResponse);

      const parsedResult = JSON.parse(textResponse);
      
      setAiResult(parsedResult);
      setIsSubmitted(true);

    } catch (error) {
      console.error("LỖI CHI TIẾT:", error);
      alert("Có lỗi xảy ra khi gọi AI. Anh nhấn F12 xem tab Console để biết chi tiết nhé.");
    } finally {
      setIsGrading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#f0f2f5] font-sans flex flex-col text-slate-800">
      
      {/* Header */}
      <header className={`px-6 py-3 flex justify-between items-center z-10 shrink-0 shadow ${isSubmitted ? 'bg-emerald-700' : 'bg-[#1f2937]'} text-white`}>
        <div className="flex items-center gap-4">
          <button onClick={onBack} className="bg-black/20 hover:bg-black/40 border border-white/20 text-sm px-3 py-1.5 rounded font-bold transition">⬅ Thoát</button>
          <div className="font-bold text-lg tracking-wide border-l border-white/30 pl-4">
            {isSubmitted ? 'KẾT QUẢ CHẤM CHỮA' : 'IELTS WRITING TASK 2'}
          </div>
        </div>
        {!isSubmitted && (
          <div className="flex items-center gap-4">
            <div className="font-bold text-lg text-white">40:00</div>
            <button onClick={handleSubmit} disabled={isGrading} className="bg-blue-600 hover:bg-blue-500 disabled:bg-blue-400 border border-blue-500 text-white font-bold text-sm px-5 py-1.5 rounded transition shadow-sm">
              {isGrading ? 'Đang chấm...' : 'Nộp bài'}
            </button>
          </div>
        )}
      </header>

      {/* Màn hình chờ */}
      {isGrading && (
        <div className="flex-1 flex flex-col items-center justify-center bg-white/80 backdrop-blur-sm z-50 absolute inset-0">
          <div className="animate-spin text-6xl mb-4">🤖</div>
          <h2 className="text-2xl font-black text-slate-800">Giám khảo AI đang đọc bài...</h2>
          <p className="text-slate-500 mt-2 font-medium">Vui lòng chờ trong giây lát để nhận kết quả phân tích.</p>
        </div>
      )}

      {/* Nội dung chính */}
      {!isSubmitted && !isGrading ? (
        <main className="flex-1 flex overflow-hidden">
          {/* Đề bài */}
          <section className="w-1/2 p-10 bg-white border-r border-slate-300 overflow-y-auto">
            <div className="max-w-xl mx-auto">
              <h2 className="font-black text-2xl text-slate-800 mb-6">Writing Task 2</h2>
              <div className="p-5 bg-amber-50 border border-amber-200 rounded-lg mb-8 text-[15px] font-bold text-amber-800">
                You should spend about 40 minutes on this task. Write about the following topic:
              </div>
              <div className="text-[17px] leading-relaxed text-slate-800 font-medium mb-8">
                <strong>More and more people are relying on artificial intelligence to complete their daily tasks. Is this a positive or negative development?</strong>
              </div>
              <div className="p-5 bg-blue-50 border border-blue-200 rounded-lg text-[14px] text-blue-800 font-medium">
                Give reasons for your answer and include relevant examples. Write at least 250 words.
              </div>
            </div>
          </section>

          {/* Khung soạn thảo */}
          <section className="w-1/2 p-10 bg-slate-50 flex flex-col relative">
            <textarea 
              className="flex-1 w-full p-6 border-2 border-slate-300 rounded-xl resize-none focus:outline-none focus:border-blue-500 focus:ring-4 focus:ring-blue-500/20 text-[16px] font-serif shadow-sm bg-white"
              placeholder="Gõ bài viết của bạn tại đây..."
              value={text}
              onChange={(e) => setText(e.target.value)}
              spellCheck="false"
            />
            <div className="absolute bottom-16 right-16 bg-[#1f2937] text-white px-4 py-2 rounded-lg font-bold text-sm shadow-md">
              Word count: {wordCount}
            </div>
          </section>
        </main>
      ) : (
        isSubmitted && aiResult && (
        <main className="flex-1 overflow-y-auto p-8">
          <div className="max-w-6xl mx-auto space-y-8">
            
            {/* Điểm số */}
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
                      <span className="font-black text-blue-600 text-lg">{c.score}</span>
                    </div>
                    <p className="text-sm text-slate-600 font-medium leading-relaxed">{c.comment}</p>
                  </div>
                ))}
              </div>
            </div>

            {/* Chấm chữa chi tiết */}
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
              <h3 className="font-black text-xl text-slate-800 mb-6">✍️ Phân tích lỗi sai & Gợi ý</h3>
              <div className="p-6 bg-slate-50 border border-slate-200 rounded-xl text-[16px] leading-loose font-serif text-slate-800"
                   dangerouslySetInnerHTML={{__html: aiResult.detailedFeedback}}>
              </div>
              <div className="mt-6 flex gap-6 text-sm font-bold">
                 <div className="flex items-center gap-2"><span className="w-4 h-4 bg-red-200 block rounded"></span> <span className="text-slate-600">Lỗi cần sửa</span></div>
                 <div className="flex items-center gap-2"><span className="w-4 h-4 bg-emerald-200 block rounded"></span> <span className="text-slate-600">Gợi ý từ AI</span></div>
              </div>
            </div>

          </div>
        </main>
        )
      )}
    </div>
  );
}