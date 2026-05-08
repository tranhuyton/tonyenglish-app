import React, { useState, useEffect, useMemo } from 'react';

// 🚀 LÁ CHẮN BẮT LỖI TỐI THƯỢNG (Chống trắng màn hình)
class ErrorBoundary extends React.Component<any, any> {
  constructor(props: any) { super(props); this.state = { hasError: false, errorMsg: '' }; }
  static getDerivedStateFromError(error: any) { return { hasError: true, errorMsg: error.toString() }; }
  render() {
    if (this.state.hasError) {
      return (
        <div className="h-screen bg-red-50 text-red-600 font-bold p-10 flex flex-col items-center justify-center text-center">
          <h1 className="text-4xl mb-4">⚠️ LỖI SẬP GIAO DIỆN (CRASH)</h1>
          <p className="text-lg bg-white p-4 border border-red-200 shadow-sm rounded-lg">{this.state.errorMsg}</p>
          <button onClick={() => window.location.reload()} className="mt-8 bg-red-600 text-white px-8 py-3 rounded-xl shadow-lg">Tải lại trang</button>
        </div>
      );
    }
    return this.props.children;
  }
}

// 🎮 COMPONENT LÕI CỦA GAME
function VocabRacingCore({ onBack, testData }: { onBack?: () => void, testData?: any }) {
  
  // Rút ruột dữ liệu siêu an toàn
  const questions = useMemo(() => {
    let safeData = testData?.content_json;
    if (typeof safeData === 'string') {
      try { safeData = JSON.parse(safeData); } catch (e) { safeData = {}; }
    }
    if (!safeData?.parts || !Array.isArray(safeData.parts)) return [];

    let qs: any[] = [];
    safeData.parts.forEach((p: any) => {
       if (p?.sections && Array.isArray(p.sections)) {
           p.sections.forEach((s: any) => {
               if (s?.questions && Array.isArray(s.questions)) qs.push(...s.questions);
           });
       }
    });

    return qs.map((q: any, i: number) => {
        let cIdx = 0;
        let ansStr = String(q.correctAnswer || '').trim().toUpperCase();
        if (['A','B','C','D'].includes(ansStr)) {
           cIdx = ansStr.charCodeAt(0) - 65;
        } else if (Array.isArray(q.options)) {
           let fIdx = q.options.findIndex((o:any)=>String(o).trim().toUpperCase()===ansStr);
           if (fIdx !== -1) cIdx = fIdx;
        }
        return {
            id: q.id || i,
            text: String(q.content || 'Câu hỏi trống'),
            options: Array.isArray(q.options) && q.options.length > 0 ? q.options.map(String) : ['A','B','C','D'],
            correct: cIdx
        };
    });
  }, [testData]);

  const [score, setScore] = useState(0);
  const [currentQIdx, setCurrentQIdx] = useState(0);
  const [gameStatus, setGameStatus] = useState<'playing' | 'won' | 'timeout'>('playing');
  const [isAnimating, setIsAnimating] = useState(false);
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null);
  const [timeLeft, setTimeLeft] = useState(15);

  // Bộ đếm giờ
  useEffect(() => {
    if (gameStatus !== 'playing' || isAnimating || questions.length === 0) return;
    if (timeLeft <= 0) {
       handleAnswer(-1); 
       return;
    }
    const timer = setInterval(() => setTimeLeft(prev => prev - 1), 1000);
    return () => clearInterval(timer);
  }, [timeLeft, gameStatus, isAnimating, questions.length]);

  // Cảnh báo thiếu dữ liệu
  if (questions.length === 0) {
    return (
      <div className="h-screen bg-slate-50 text-slate-800 flex flex-col items-center justify-center font-sans">
        <h1 className="text-4xl font-black text-blue-600 mb-4">🏎️ VOCAB RACING</h1>
        <p className="text-slate-500 mb-8 font-medium">Chưa có dữ liệu câu hỏi. Vui lòng tạo đề và Import Excel!</p>
        {onBack && <button onClick={onBack} className="bg-slate-300 hover:bg-slate-400 px-8 py-3 rounded-xl font-bold transition shadow-sm">Thoát</button>}
      </div>
    );
  }

  const currentQuestion = questions[currentQIdx];
  const progress = questions.length > 0 ? (currentQIdx / questions.length) * 100 : 0;

  const handleAnswer = (idx: number) => {
    if (gameStatus !== 'playing' || isAnimating) return;
    setSelectedAnswer(idx);
    setIsAnimating(true);

    const isCorrect = idx === currentQuestion?.correct;

    setTimeout(() => {
      if (isCorrect) setScore(prev => prev + 10);
      if (currentQIdx + 1 >= questions.length) { 
        setGameStatus('won'); 
      } else { 
        setCurrentQIdx(prev => prev + 1); 
        setTimeLeft(15); 
      }
      setSelectedAnswer(null);
      setIsAnimating(false);
    }, 1000);
  };

  const resetGame = () => {
    setCurrentQIdx(0); setScore(0); setTimeLeft(15); setGameStatus('playing'); setSelectedAnswer(null);
  };

  return (
    <div className="h-screen bg-slate-50 text-slate-800 flex flex-col font-sans relative overflow-hidden">
      <header className="px-6 py-4 flex justify-between items-center bg-white shadow-sm relative z-10 border-b border-slate-200">
        {onBack && <button onClick={onBack} className="bg-slate-100 hover:bg-slate-200 text-slate-600 px-5 py-2.5 rounded-xl font-bold transition-colors">← Thoát</button>}
        <h1 className="font-black text-2xl text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 italic transform -skew-x-12 hidden md:block">VOCAB RACING</h1>
        <div className="font-black text-lg text-blue-700 bg-blue-50 px-5 py-2 rounded-xl border border-blue-200 shadow-inner">Điểm: {score}</div>
      </header>

      <div className="w-full h-5 bg-slate-800 relative z-10 shadow-inner overflow-hidden border-y border-slate-900">
        <div className="h-full bg-gradient-to-r from-blue-500 to-cyan-400 transition-all duration-700 ease-out relative" style={{ width: `${progress}%` }}>
           <div className="absolute right-0 top-1/2 -translate-y-1/2 translate-x-1/2 text-2xl drop-shadow-md z-20">🏎️</div>
        </div>
        <div className="absolute right-2 top-1/2 -translate-y-1/2 text-xl opacity-50">🏁</div>
      </div>

      <main className="flex-1 flex flex-col items-center justify-center p-4 md:p-8 relative z-10 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')]">
        <div className="w-full max-w-4xl bg-white p-6 md:p-12 rounded-[2rem] shadow-2xl border border-slate-100 relative">
          
          {gameStatus === 'playing' && currentQuestion ? (
            <div className="animate-in fade-in zoom-in-95">
              <div className="flex justify-between items-center mb-8 border-b border-slate-100 pb-6">
                <span className="bg-slate-100 text-slate-500 px-4 py-2 rounded-lg font-bold text-sm uppercase tracking-widest border border-slate-200">Chặng {currentQIdx + 1} / {questions.length}</span>
                <span className={`flex items-center gap-2 font-black border px-4 py-2 rounded-lg text-lg ${timeLeft <= 5 ? 'text-rose-600 bg-rose-50 border-rose-200 animate-pulse' : 'text-blue-600 bg-blue-50 border-blue-200'}`}>
                  <span className="animate-pulse">⏱️</span> {timeLeft}s
                </span>
              </div>
              <div className="text-xl md:text-3xl font-black text-center mb-10 text-slate-800 leading-snug" dangerouslySetInnerHTML={{ __html: currentQuestion.text || '' }} />
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 md:gap-6">
                {currentQuestion.options.map((opt: string, i: number) => {
                  let btnClass = "bg-slate-50 border-slate-200 text-slate-700 hover:bg-blue-50 hover:border-blue-400 hover:text-blue-700";
                  if (selectedAnswer !== null) {
                    if (i === currentQuestion.correct) btnClass = "bg-emerald-50 border-emerald-400 text-emerald-700 shadow-md scale-[1.02] z-10";
                    else if (i === selectedAnswer) btnClass = "bg-rose-50 border-rose-400 text-rose-700 shadow-md scale-[1.02] z-10";
                    else btnClass = "bg-slate-50 border-slate-100 text-slate-400 opacity-50";
                  }
                  return (
                    <button key={i} disabled={selectedAnswer !== null} onClick={() => handleAnswer(i)} className={`border-2 p-5 md:p-6 rounded-2xl font-bold text-base md:text-lg transition-all active:scale-95 flex items-center gap-4 shadow-sm ${btnClass}`}>
                      <span className="w-10 h-10 rounded-full bg-white shadow-sm border border-slate-200 flex items-center justify-center text-sm shrink-0">{String.fromCharCode(65+i)}</span>
                      <span className="flex-1 text-left leading-relaxed" dangerouslySetInnerHTML={{ __html: opt || '' }}></span>
                    </button>
                  )
                })}
              </div>
            </div>
          ) : (
            <div className="text-center py-8 animate-in zoom-in-95">
               <div className="text-6xl mb-4">🏁</div>
               <h2 className="text-3xl md:text-4xl font-black text-blue-600 mb-2 uppercase">Về Đích!</h2>
               <p className="text-slate-500 font-medium mb-8 text-lg">Bạn đã hoàn thành chặng đua với <span className="font-bold text-emerald-600">{score} điểm</span>.</p>
               <div className="flex justify-center gap-4">
                 <button onClick={resetGame} className="bg-blue-600 hover:bg-blue-700 text-white font-black px-8 py-3.5 rounded-xl transition shadow-lg">Đua Lại</button>
                 {onBack && <button onClick={onBack} className="bg-slate-100 hover:bg-slate-200 text-slate-600 font-black px-8 py-3.5 rounded-xl transition">Thoát</button>}
               </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

// Bọc Component vào Error Boundary để chống sập App
export default function VocabRacing(props: any) {
  return <ErrorBoundary><VocabRacingCore {...props} /></ErrorBoundary>;
}