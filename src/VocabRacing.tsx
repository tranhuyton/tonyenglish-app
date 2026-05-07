import React, { useState } from 'react';

export default function VocabRacing({ onBack, testData }: { onBack: () => void, testData: any }) {
  // 🚀 Bóc tách toàn bộ câu hỏi từ Data truyền vào
  const questions = testData?.content_json?.parts?.flatMap((p: any) => 
    p.sections?.flatMap((s: any) => s.questions) || []
  ) || [];

  const [score, setScore] = useState(0);
  const [currentQIdx, setCurrentQIdx] = useState(0);
  
  // Tính % đường đua
  const progress = questions.length > 0 ? (currentQIdx / questions.length) * 100 : 0;

  // Nếu đề thi không có câu hỏi nào
  if (questions.length === 0) {
    return (
      <div className="h-screen bg-slate-50 text-slate-800 flex flex-col items-center justify-center font-sans">
        <h1 className="text-3xl font-black text-blue-600 mb-4">🏎️ VOCAB RACING</h1>
        <p className="text-slate-500 mb-8">Đường đua chưa có câu hỏi nào!</p>
        <button onClick={onBack} className="bg-slate-300 hover:bg-slate-400 px-6 py-2 rounded-lg font-bold transition">Quay lại</button>
      </div>
    );
  }

  const currentQuestion = questions[currentQIdx];

  return (
    <div className="h-screen bg-slate-50 text-slate-800 flex flex-col font-sans relative overflow-hidden">
      {/* --- HEADER GAME --- */}
      <header className="px-6 py-4 flex justify-between items-center bg-white shadow-sm relative z-10 border-b border-slate-200">
        <button onClick={onBack} className="bg-slate-100 hover:bg-slate-200 text-slate-600 px-5 py-2.5 rounded-xl font-bold transition-colors">
          ← Rời đường đua
        </button>
        <h1 className="font-black text-2xl text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 italic transform -skew-x-12 hidden md:block">
          VOCAB RACING
        </h1>
        <div className="font-black text-lg text-blue-700 bg-blue-50 px-5 py-2 rounded-xl border border-blue-200 shadow-inner uppercase tracking-wider">
          Điểm: {score}
        </div>
      </header>

      {/* --- THANH TIẾN ĐỘ ĐƯỜNG ĐUA --- */}
      <div className="w-full h-4 bg-slate-200 relative z-10 shadow-inner overflow-hidden">
        <div 
          className="h-full bg-gradient-to-r from-blue-500 to-cyan-400 transition-all duration-700 ease-out relative"
          style={{ width: `${progress}%` }}
        >
           {/* Xe đua nhấp nháy chạy trên thanh */}
           <div className="absolute right-0 top-1/2 -translate-y-1/2 translate-x-1/2 text-2xl drop-shadow-md z-20">
             🏎️
           </div>
        </div>
        <div className="absolute right-2 top-1/2 -translate-y-1/2 text-xl opacity-50">🏁</div>
      </div>

      {/* --- KHU VỰC CHƠI CHÍNH --- */}
      <main className="flex-1 flex flex-col items-center justify-center p-4 md:p-8 relative z-10 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')]">
        <div className="w-full max-w-4xl bg-white p-6 md:p-12 rounded-[2rem] md:rounded-[3rem] shadow-2xl border border-slate-100 relative">
          
          <div className="flex justify-between items-center mb-8 border-b border-slate-100 pb-6">
            <span className="bg-slate-100 text-slate-500 px-4 py-2 rounded-lg font-bold text-sm uppercase tracking-widest border border-slate-200">
              Chặng {currentQIdx + 1} / {questions.length}
            </span>
            <span className="flex items-center gap-2 font-black text-rose-600 bg-rose-50 border border-rose-200 px-4 py-2 rounded-lg text-lg">
              <span className="animate-pulse">⏱️</span> 10s
            </span>
          </div>
          
          {/* Nội dung câu hỏi */}
          <div className="text-2xl md:text-3xl font-black text-center mb-10 text-slate-800 leading-snug" dangerouslySetInnerHTML={{ __html: currentQuestion?.content || 'Nội dung câu hỏi...' }} />
          
          {/* Nút chọn đáp án */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 md:gap-6">
            {currentQuestion?.options?.map((opt: string, i: number) => (
              <button 
                key={i}
                className="bg-slate-50 hover:bg-blue-50 border-2 border-slate-200 hover:border-blue-400 text-slate-700 hover:text-blue-700 p-5 md:p-6 rounded-2xl font-bold text-lg transition-all active:scale-95 flex items-center gap-4 group shadow-sm hover:shadow-md"
              >
                <span className="w-10 h-10 rounded-full bg-white shadow-sm border border-slate-200 group-hover:border-blue-300 group-hover:bg-blue-100 flex items-center justify-center text-sm shrink-0 transition-colors">
                  {String.fromCharCode(65+i)}
                </span>
                <span className="flex-1 text-left leading-relaxed" dangerouslySetInnerHTML={{ __html: opt }}></span>
              </button>
            ))}
          </div>
          
        </div>
      </main>
    </div>
  );
}