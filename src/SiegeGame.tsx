import React, { useState, useEffect, useMemo } from 'react';

// Dữ liệu dự phòng (Phòng trường hợp anh test độc lập không qua Supabase)
const DUMMY_QUESTIONS = [
  { id: 1, text: "Từ nào sau đây đồng nghĩa với 'Renewable'?", options: ["Exhaustible", "Sustainable", "Limited", "Depleted"], correct: 1 },
  { id: 2, text: "Chọn giới từ đúng: 'She is good ___ solving problems.'", options: ["in", "on", "at", "about"], correct: 2 },
  { id: 3, text: "Đâu là năng lượng tái tạo?", options: ["Coal", "Natural Gas", "Solar Energy", "Nuclear"], correct: 2 },
  { id: 4, text: "IELTS Writing Task 2 yêu cầu viết ít nhất bao nhiêu từ?", options: ["150", "200", "250", "300"], correct: 2 },
  { id: 5, text: "Hoàn thành câu: 'If it rains, we ___ at home.'", options: ["will stay", "would stay", "stayed", "staying"], correct: 0 },
];

export default function SiegeGame({ onBack, testData }: { onBack?: () => void, testData?: any }) {
  
  // 🚀 LỌC VÀ CHUYỂN ĐỔI DỮ LIỆU ĐỘNG TỪ SUPABASE
  const questions = useMemo(() => {
    if (!testData) return DUMMY_QUESTIONS; 
    
    let safeContent = testData?.content_json || {};
    if (typeof safeContent === 'string') {
      try { safeContent = JSON.parse(safeContent); } catch (e) { safeContent = {}; }
    }
    const parts = Array.isArray(safeContent?.parts) ? safeContent.parts : [];
    const rawQuestions = parts.flatMap((p: any) => 
      Array.isArray(p.sections) ? p.sections.flatMap((s: any) => Array.isArray(s.questions) ? s.questions : []) : []
    );

    if (rawQuestions.length === 0) return [];

    return rawQuestions.map((q: any, idx: number) => {
      let correctIdx = 0;
      const correctStr = String(q.correctAnswer || '').trim().toUpperCase();
      
      // Thuật toán nhận diện đáp án (Chuyển A,B,C,D thành 0,1,2,3)
      if (['A', 'B', 'C', 'D', 'E', 'F'].includes(correctStr)) {
          correctIdx = correctStr.charCodeAt(0) - 65;
      } else if (q.options) {
          const foundIdx = q.options.findIndex((o: any) => String(o).trim().toUpperCase() === correctStr);
          if (foundIdx !== -1) correctIdx = foundIdx;
      }
      
      return {
          id: q.id || idx,
          text: q.content || 'Nội dung câu hỏi bị trống',
          options: q.options && q.options.length > 0 ? q.options : ['A', 'B', 'C', 'D'],
          correct: correctIdx
      };
    });
  }, [testData]);

  const [currentIndex, setCurrentIndex] = useState(0);
  
  // Trạng thái Game
  const [hp, setHp] = useState(3); // 3 Mạng
  const [progress, setProgress] = useState(0); // 0% đến 100%
  // Tự động tính giờ: 15s cho mỗi câu hỏi
  const [timeLeft, setTimeLeft] = useState(questions.length > 0 && testData ? questions.length * 15 : 60); 
  const [gameStatus, setGameStatus] = useState<'playing' | 'won' | 'lost_hp' | 'lost_time'>('playing');

  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null);
  const [isAnimating, setIsAnimating] = useState(false);

  // Xử lý đếm ngược thời gian
  useEffect(() => {
    if (gameStatus !== 'playing') return;
    const timer = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          clearInterval(timer);
          setGameStatus('lost_time');
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timer);
  }, [gameStatus]);

  // Bắt lỗi rỗng
  if (!questions || questions.length === 0) {
    return (
      <div className="min-h-screen bg-slate-900 text-white flex flex-col items-center justify-center font-sans">
        <h1 className="text-3xl font-black text-amber-500 mb-4">🏰 GRAMMAR SIEGE</h1>
        <p className="text-slate-400 mb-8">Trận địa này chưa được thiết lập câu hỏi!</p>
        <button onClick={onBack} className="bg-slate-700 hover:bg-slate-600 px-6 py-2 rounded-lg font-bold transition">Quay lại</button>
      </div>
    );
  }

  const currentQ = questions[currentIndex];

  const handleAnswer = (optionIndex: number) => {
    if (gameStatus !== 'playing' || isAnimating || !currentQ) return;
    
    setSelectedAnswer(optionIndex);
    setIsAnimating(true);

    const isCorrect = optionIndex === currentQ.correct;
    const step = 100 / questions.length; // Trả lời đúng tiến thêm bao nhiêu %

    setTimeout(() => {
      if (isCorrect) {
        const newProgress = progress + step;
        setProgress(newProgress);
        
        if (newProgress >= 99) { // >= 99 để bù trừ sai số
          setGameStatus('won');
        } else {
          setCurrentIndex(prev => prev + 1);
        }
      } else {
        const newHp = hp - 1;
        setHp(newHp);
        if (newHp <= 0) {
          setGameStatus('lost_hp');
        }
      }
      setSelectedAnswer(null);
      setIsAnimating(false);
    }, 1000); // Đợi 1s để học sinh nhìn thấy kết quả Đúng/Sai rồi mới chuyển câu
  };

  const resetGame = () => {
    setCurrentIndex(0);
    setHp(3);
    setProgress(0);
    setTimeLeft(questions.length > 0 && testData ? questions.length * 15 : 60);
    setGameStatus('playing');
    setSelectedAnswer(null);
  };

  return (
    <div className="min-h-[100dvh] bg-slate-900 flex flex-col items-center justify-center font-sans p-4 relative overflow-hidden">
      
      {/* 🚀 NÚT THOÁT SỚM (LUÔN NỔI Ở GÓC TRÁI) */}
      {onBack && (
        <button 
          onClick={onBack}
          className="absolute top-4 left-4 md:top-8 md:left-8 bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white px-4 py-2.5 rounded-xl font-bold border border-slate-600 backdrop-blur-md transition-all flex items-center gap-2 z-50 shadow-lg active:scale-95"
        >
          <span className="text-xl leading-none -mt-0.5">←</span> 
          <span className="hidden sm:inline">Thoát Game</span>
          <span className="sm:hidden">Thoát</span>
        </button>
      )}

      {/* BACKGROUND MÔ PHỎNG CHIẾN TRƯỜNG */}
      <div className="absolute inset-0 opacity-20 pointer-events-none">
        <div className="absolute bottom-0 w-full h-1/2 bg-gradient-to-t from-orange-900 to-transparent"></div>
      </div>

      <div className="w-full max-w-3xl bg-slate-800 rounded-[2rem] shadow-[0_0_50px_rgba(0,0,0,0.5)] border-4 border-slate-700 p-6 md:p-10 relative z-10 mt-12 md:mt-0">
        
        {/* HEADER: THANH HP VÀ TIMER */}
        <div className="flex justify-between items-center mb-8 bg-slate-900/50 p-4 rounded-2xl border border-slate-700 shadow-inner">
          <div className="flex items-center gap-2">
            <span className="text-slate-400 font-black uppercase tracking-widest text-[11px] md:text-sm mr-1 md:mr-2">Sinh lực:</span>
            {Array.from({ length: 3 }).map((_, i) => (
              <span key={i} className={`text-xl md:text-2xl transition-all duration-300 ${i < hp ? 'text-red-500 scale-110 drop-shadow-[0_0_8px_rgba(239,68,68,0.8)]' : 'text-slate-600 grayscale'}`}>
                ❤️
              </span>
            ))}
          </div>
          <div className={`flex items-center gap-2 font-mono text-xl md:text-2xl font-black px-4 py-2 rounded-xl border-2 shadow-sm ${timeLeft <= 10 ? 'bg-red-900/50 text-red-400 border-red-500 animate-pulse' : 'bg-slate-800 text-amber-400 border-amber-600/50'}`}>
            ⏱️ {Math.floor(timeLeft / 60).toString().padStart(2, '0')}:{(timeLeft % 60).toString().padStart(2, '0')}
          </div>
        </div>

        {/* BẢN ĐỒ TIẾN QUÂN (WAR PROGRESS BAR) */}
        <div className="mb-12 relative w-full h-12 md:h-16 bg-slate-700 rounded-full border-4 border-slate-600 overflow-visible shadow-inner">
          {/* Vạch đích (Cổng thành) */}
          <div className="absolute right-0 top-1/2 -translate-y-1/2 translate-x-1/3 text-4xl md:text-5xl z-20 drop-shadow-2xl">
            🏰
          </div>
          
          {/* Thanh màu tiến độ */}
          <div 
            className="h-full bg-gradient-to-r from-amber-600 to-orange-500 rounded-full transition-all duration-700 ease-out relative shadow-lg"
            style={{ width: `${progress}%` }}
          >
            {/* Quân lính (Hiệp sĩ) đang tiến lên */}
            <div className="absolute right-0 top-1/2 -translate-y-1/2 translate-x-1/2 text-3xl md:text-4xl drop-shadow-lg transition-transform hover:scale-110 z-30">
              🤺
            </div>
            
            {/* Lửa cháy chạy dọc thanh */}
            <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4IiBoZWlnaHQ9IjgiPgo8cmVjdCB3aWR0aD0iOCIgaGVpZ2h0PSI4IiBmaWxsPSIjZmZmIiBmaWxsLW9wYWNpdHk9IjAuMSIvPgo8L3N2Zz4=')] opacity-20 rounded-full"></div>
          </div>
        </div>

        {/* KHU VỰC CÂU HỎI & TRẢ LỜI */}
        {gameStatus === 'playing' && currentQ && (
          <div className="animate-in fade-in zoom-in-95 duration-300">
            <div className="text-center mb-8">
              <span className="inline-block bg-slate-700 text-amber-400 font-bold px-4 py-1.5 rounded-full text-xs md:text-sm mb-4 border border-slate-600 shadow-sm uppercase tracking-wider">
                Ải thứ {currentIndex + 1} / {questions.length}
              </span>
              <h2 className="text-xl md:text-3xl font-black text-white leading-snug" dangerouslySetInnerHTML={{ __html: currentQ.text }}>
              </h2>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 md:gap-4">
              {currentQ.options.map((opt: string, idx: number) => {
                let btnStateClass = "bg-slate-700 text-slate-200 border-slate-600 hover:bg-slate-600 hover:border-slate-500 shadow-md";
                
                if (selectedAnswer !== null) {
                  if (idx === currentQ.correct) {
                    btnStateClass = "bg-emerald-600 text-white border-emerald-400 shadow-[0_0_20px_rgba(16,185,129,0.5)] z-10 scale-[1.02]"; 
                  } else if (idx === selectedAnswer) {
                    btnStateClass = "bg-red-600 text-white border-red-400 shadow-[0_0_20px_rgba(239,68,68,0.5)] z-10 scale-[1.02]"; 
                  } else {
                    btnStateClass = "bg-slate-800 text-slate-500 border-slate-700 opacity-50"; 
                  }
                }

                return (
                  <button 
                    key={idx}
                    disabled={selectedAnswer !== null}
                    onClick={() => handleAnswer(idx)}
                    className={`w-full text-left px-5 py-4 md:px-6 md:py-5 rounded-2xl border-2 font-bold text-base md:text-lg transition-all duration-300 transform active:scale-95 flex gap-3 items-center ${btnStateClass}`}
                  >
                    <span className="inline-block w-8 md:w-10 text-slate-400 font-black opacity-60 shrink-0">{String.fromCharCode(65+idx)}.</span>
                    <span dangerouslySetInnerHTML={{ __html: opt }}></span>
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* MÀN HÌNH KẾT QUẢ (THẮNG / THUA) */}
        {gameStatus !== 'playing' && (
          <div className="text-center py-6 md:py-10 animate-in zoom-in-95 duration-500">
            {gameStatus === 'won' && (
              <>
                <div className="text-6xl md:text-7xl mb-4 md:mb-6 animate-bounce">🏆</div>
                <h2 className="text-3xl md:text-4xl font-black text-emerald-400 mb-3 md:mb-4 drop-shadow-lg">CÔNG THÀNH THÀNH CÔNG!</h2>
                <p className="text-slate-300 text-base md:text-lg mb-8 max-w-lg mx-auto">Chiến lược tuyệt vời! Đội quân của bạn đã phá vỡ cổng thành và giành chiến thắng.</p>
              </>
            )}
            {gameStatus === 'lost_hp' && (
              <>
                <div className="text-6xl md:text-7xl mb-4 md:mb-6 animate-pulse grayscale">💀</div>
                <h2 className="text-3xl md:text-4xl font-black text-red-500 mb-3 md:mb-4 drop-shadow-lg">BẠN ĐÃ TỬ TRẬN!</h2>
                <p className="text-slate-300 text-base md:text-lg mb-8 max-w-lg mx-auto">Bạn đã trúng quá nhiều tên của địch. Đội quân buộc phải rút lui để bảo toàn lực lượng.</p>
              </>
            )}
            {gameStatus === 'lost_time' && (
              <>
                <div className="text-6xl md:text-7xl mb-4 md:mb-6 animate-pulse">⏳</div>
                <h2 className="text-3xl md:text-4xl font-black text-amber-500 mb-3 md:mb-4 drop-shadow-lg">HẾT THỜI GIAN!</h2>
                <p className="text-slate-300 text-base md:text-lg mb-8 max-w-lg mx-auto">Viện binh của địch đã tới trước khi bạn kịp phá cổng thành. Hãy thao tác nhanh hơn ở lần sau!</p>
              </>
            )}

            <div className="flex flex-col sm:flex-row justify-center gap-3 md:gap-4">
              <button onClick={resetGame} className="bg-amber-500 hover:bg-amber-600 text-slate-900 font-black px-8 py-3.5 rounded-xl border-b-4 border-amber-700 active:border-b-0 active:translate-y-1 transition-all shadow-lg flex items-center justify-center gap-2">
                <span className="text-xl">🔄</span> CHƠI LẠI
              </button>
              {onBack && (
                <button onClick={onBack} className="bg-slate-700 hover:bg-slate-600 text-white font-black px-8 py-3.5 rounded-xl border-b-4 border-slate-900 active:border-b-0 active:translate-y-1 transition-all shadow-lg flex items-center justify-center gap-2">
                  <span className="text-xl">🚪</span> RỜI KHỎI TRẬN ĐỊA
                </button>
              )}
            </div>
          </div>
        )}

      </div>
    </div>
  );
}