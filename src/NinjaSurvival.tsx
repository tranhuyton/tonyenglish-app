import React, { useState } from 'react';

export default function NinjaSurvival({ onBack, testData }: { onBack: () => void, testData: any }) {
  // 🚀 Bóc tách toàn bộ câu hỏi từ Data truyền vào
  const questions = testData?.content_json?.parts?.flatMap((p: any) => 
    p.sections?.flatMap((s: any) => s.questions) || []
  ) || [];

  const [score, setScore] = useState(0);
  const [lives, setLives] = useState(3);
  const [currentQIdx, setCurrentQIdx] = useState(0);

  // Nếu đề thi không có câu hỏi nào
  if (questions.length === 0) {
    return (
      <div className="h-screen bg-slate-900 text-white flex flex-col items-center justify-center font-sans">
        <h1 className="text-3xl font-black text-red-500 mb-4">🥷 NINJA SURVIVAL</h1>
        <p className="text-slate-400 mb-8">Đề thi này chưa có câu hỏi nào để chơi!</p>
        <button onClick={onBack} className="bg-slate-700 hover:bg-slate-600 px-6 py-2 rounded-lg font-bold transition">Quay lại</button>
      </div>
    );
  }

  const currentQuestion = questions[currentQIdx];

  return (
    <div className="h-screen bg-slate-900 text-white flex flex-col font-sans relative overflow-hidden">
      {/* --- HEADER GAME --- */}
      <header className="p-6 flex justify-between items-center relative z-10">
        <button onClick={onBack} className="bg-slate-800 hover:bg-red-600 text-slate-300 hover:text-white px-5 py-2 rounded-xl font-bold transition-colors shadow-lg">
          ← Rút lui
        </button>
        <div className="flex gap-8 items-center font-black text-xl bg-slate-800/50 px-6 py-2 rounded-full border border-slate-700">
          <div className="text-red-500 tracking-widest">MÁU: {'❤️'.repeat(lives)}</div>
          <div className="w-px h-6 bg-slate-600"></div>
          <div className="text-emerald-400">ĐIỂM: {score}</div>
        </div>
      </header>

      {/* --- KHU VỰC CHƠI CHÍNH --- */}
      <main className="flex-1 flex flex-col items-center justify-center p-4 md:p-8 relative z-10">
        <div className="text-center max-w-3xl w-full">
          <h2 className="text-4xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-red-500 to-orange-500 mb-8 tracking-wider drop-shadow-lg uppercase italic transform -skew-x-6">
            Ninja Survival
          </h2>
          
          <div className="bg-slate-800/80 p-6 md:p-10 rounded-3xl border border-slate-700 shadow-[0_0_50px_rgba(0,0,0,0.5)] backdrop-blur-sm">
            <p className="text-slate-400 font-bold mb-6 uppercase tracking-widest text-sm bg-slate-900/50 inline-block px-4 py-1.5 rounded-full border border-slate-700/50">
              Mục tiêu {currentQIdx + 1} / {questions.length}
            </p>
            
            {/* Nội dung câu hỏi */}
            <div className="text-2xl md:text-3xl font-medium mb-10 leading-relaxed text-slate-100" dangerouslySetInnerHTML={{ __html: currentQuestion?.content || 'Nội dung câu hỏi...' }} />
            
            {/* Nút chọn đáp án */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {currentQuestion?.options?.map((opt: string, i: number) => (
                <button 
                  key={i}
                  className="bg-slate-700/50 hover:bg-slate-600 border-2 border-slate-600 hover:border-red-500 text-white p-5 rounded-2xl font-bold text-lg transition-all active:scale-95 text-left group flex gap-4 items-center"
                >
                  <span className="w-8 h-8 rounded-full bg-slate-800 text-slate-400 group-hover:bg-red-500 group-hover:text-white flex items-center justify-center text-sm shrink-0 transition-colors">
                    {String.fromCharCode(65+i)}
                  </span>
                  <span dangerouslySetInnerHTML={{ __html: opt }}></span>
                </button>
              ))}
            </div>
          </div>
        </div>
      </main>
      
      {/* Background Decor mờ ảo phía sau */}
      <div className="absolute inset-0 z-0 opacity-[0.03] pointer-events-none flex items-center justify-center text-[30rem] select-none filter blur-sm">
        🥷
      </div>
    </div>
  );
}