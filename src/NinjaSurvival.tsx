import React, { useState, useMemo } from 'react';

// 🚀 LÁ CHẮN BẮT LỖI TỐI THƯỢNG (Chống trắng màn hình)
class ErrorBoundary extends React.Component<any, any> {
  constructor(props: any) { super(props); this.state = { hasError: false, errorMsg: '' }; }
  static getDerivedStateFromError(error: any) { return { hasError: true, errorMsg: error.toString() }; }
  render() {
    if (this.state.hasError) {
      return (
        <div className="h-screen bg-red-900 text-white font-bold p-10 flex flex-col items-center justify-center text-center">
          <h1 className="text-4xl mb-4 text-red-400">⚠️ LỖI SẬP GIAO DIỆN (CRASH)</h1>
          <p className="text-lg bg-black/50 p-4 border border-red-500 shadow-sm rounded-lg">{this.state.errorMsg}</p>
          <button onClick={() => window.location.reload()} className="mt-8 bg-red-600 text-white px-8 py-3 rounded-xl shadow-lg">Tải lại trang</button>
        </div>
      );
    }
    return this.props.children;
  }
}

// 🥷 COMPONENT LÕI CỦA GAME
function NinjaSurvivalCore({ onBack, testData }: { onBack?: () => void, testData?: any }) {
  
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
  const [lives, setLives] = useState(3);
  const [currentQIdx, setCurrentQIdx] = useState(0);
  const [gameStatus, setGameStatus] = useState<'playing' | 'won' | 'lost'>('playing');
  const [isAnimating, setIsAnimating] = useState(false);
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null);

  if (questions.length === 0) {
    return (
      <div className="h-screen bg-slate-900 text-white flex flex-col items-center justify-center font-sans">
        <h1 className="text-4xl font-black text-red-500 mb-4">🥷 NINJA SURVIVAL</h1>
        <p className="text-slate-400 mb-8 font-medium">Chưa có dữ liệu câu hỏi. Vui lòng tạo đề và Import Excel!</p>
        {onBack && <button onClick={onBack} className="bg-slate-700 hover:bg-slate-600 px-8 py-3 rounded-xl font-bold transition">Quay lại</button>}
      </div>
    );
  }

  const currentQuestion = questions[currentQIdx];

  const handleAnswer = (idx: number) => {
    if (gameStatus !== 'playing' || isAnimating || !currentQuestion) return;
    
    setSelectedAnswer(idx);
    setIsAnimating(true);

    const isCorrect = idx === currentQuestion.correct;

    setTimeout(() => {
      if (isCorrect) {
        setScore(prev => prev + 10);
        if (currentQIdx + 1 >= questions.length) { setGameStatus('won'); } 
        else { setCurrentQIdx(prev => prev + 1); }
      } else {
        const newLives = lives - 1;
        setLives(newLives);
        if (newLives <= 0) setGameStatus('lost');
      }
      setSelectedAnswer(null);
      setIsAnimating(false);
    }, 800);
  };

  const resetGame = () => {
    setCurrentQIdx(0); setScore(0); setLives(3); setGameStatus('playing'); setSelectedAnswer(null);
  };

  return (
    <div className="h-screen bg-slate-900 text-white flex flex-col font-sans relative overflow-hidden">
      <header className="p-6 flex justify-between items-center relative z-10">
        {onBack && <button onClick={onBack} className="bg-slate-800 hover:bg-red-600 text-slate-300 hover:text-white px-5 py-2.5 rounded-xl font-bold transition-colors shadow-lg z-50">← Rút lui</button>}
        <div className="flex gap-4 md:gap-8 items-center font-black text-lg md:text-xl bg-slate-800/50 px-4 md:px-6 py-2.5 rounded-full border border-slate-700 shadow-sm ml-auto">
          <div className="text-red-500 tracking-widest flex items-center gap-1">
            <span className="hidden sm:inline text-slate-400 text-sm">MÁU:</span> 
            {Array.from({ length: 3 }).map((_, i) => (<span key={i} className={`transition-all duration-300 ${i < lives ? 'opacity-100 scale-110 drop-shadow-[0_0_8px_rgba(239,68,68,0.8)]' : 'opacity-20 grayscale'}`}>❤️</span>))}
          </div>
          <div className="w-px h-6 bg-slate-600"></div>
          <div className="text-emerald-400 drop-shadow-[0_0_8px_rgba(52,211,153,0.5)]">
            <span className="hidden sm:inline text-slate-400 text-sm mr-2">ĐIỂM:</span>{score}
          </div>
        </div>
      </header>

      <main className="flex-1 flex flex-col items-center justify-center p-4 md:p-8 relative z-10">
        <div className="text-center max-w-3xl w-full">
          <h2 className="text-4xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-red-500 to-orange-500 mb-8 tracking-wider drop-shadow-lg uppercase italic transform -skew-x-6 hidden sm:block">Ninja Survival</h2>
          
          <div className="bg-slate-800/80 p-6 md:p-10 rounded-3xl border border-slate-700 shadow-[0_0_50px_rgba(0,0,0,0.5)] backdrop-blur-sm">
            {gameStatus === 'playing' && currentQuestion ? (
              <div className="animate-in fade-in zoom-in-95">
                <p className="text-slate-400 font-bold mb-6 uppercase tracking-widest text-sm bg-slate-900/50 inline-block px-5 py-2 rounded-full border border-slate-700/50">Mục tiêu {currentQIdx + 1} / {questions.length}</p>
                <div className="text-xl md:text-3xl font-medium mb-10 leading-relaxed text-slate-100" dangerouslySetInnerHTML={{ __html: currentQuestion.text || '' }} />
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  {currentQuestion.options.map((opt: string, i: number) => {
                    let btnClass = "bg-slate-700/50 border-slate-600 text-slate-200 hover:bg-slate-600 hover:border-red-500 hover:text-white";
                    if (selectedAnswer !== null) {
                      if (i === currentQuestion.correct) btnClass = "bg-emerald-600 border-emerald-400 text-white scale-[1.02] shadow-[0_0_15px_rgba(16,185,129,0.5)] z-10";
                      else if (i === selectedAnswer) btnClass = "bg-red-600 border-red-400 text-white scale-[1.02] shadow-[0_0_15px_rgba(239,68,68,0.5)] z-10";
                      else btnClass = "bg-slate-800/50 border-slate-700 text-slate-500 opacity-50";
                    }
                    return (
                      <button key={i} disabled={selectedAnswer !== null} onClick={() => handleAnswer(i)} className={`border-2 p-4 md:p-5 rounded-2xl font-bold text-base md:text-lg transition-all active:scale-95 text-left flex gap-4 items-center ${btnClass}`}>
                        <span className="w-8 h-8 rounded-full bg-slate-800 text-slate-400 flex items-center justify-center text-sm shrink-0 transition-colors shadow-inner">{String.fromCharCode(65+i)}</span>
                        <span dangerouslySetInnerHTML={{ __html: opt || '' }}></span>
                      </button>
                    )
                  })}
                </div>
              </div>
            ) : (
              <div className="text-center py-8 animate-in zoom-in-95">
                {gameStatus === 'won' ? (
                  <><div className="text-7xl mb-6 animate-bounce">🏆</div><h2 className="text-3xl md:text-4xl font-black text-emerald-400 mb-4 drop-shadow-lg">TUYỆT ĐỈNH NINJA!</h2><p className="text-slate-300 mb-8 text-lg">Bạn đã vượt qua mọi cạm bẫy với {score} điểm.</p></>
                ) : (
                  <><div className="text-7xl mb-6 grayscale animate-pulse">💀</div><h2 className="text-3xl md:text-4xl font-black text-red-500 mb-4 drop-shadow-lg">NHIỆM VỤ THẤT BẠI!</h2><p className="text-slate-300 mb-8 text-lg">Bạn đã hết máu. Hãy rèn luyện thêm và quay lại phục thù.</p></>
                )}
                <div className="flex flex-col sm:flex-row justify-center gap-4">
                  <button onClick={resetGame} className="bg-red-600 hover:bg-red-500 text-white font-black px-8 py-3.5 rounded-xl transition shadow-lg active:scale-95 border-b-4 border-red-800 active:border-b-0">🔄 Chơi Lại</button>
                  {onBack && <button onClick={onBack} className="bg-slate-700 hover:bg-slate-600 text-white font-black px-8 py-3.5 rounded-xl transition shadow-lg active:scale-95 border-b-4 border-slate-900 active:border-b-0">🚪 Thoát</button>}
                </div>
              </div>
            )}
          </div>
        </div>
      </main>
      <div className="absolute inset-0 z-0 opacity-5 pointer-events-none flex items-center justify-center text-[40rem] select-none filter blur-sm">🥷</div>
    </div>
  );
}

// Bọc Component vào Error Boundary để chống sập App
export default function NinjaSurvival(props: any) {
  return <ErrorBoundary><NinjaSurvivalCore {...props} /></ErrorBoundary>;
}