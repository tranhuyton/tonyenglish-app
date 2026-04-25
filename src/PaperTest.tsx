import React, { useState, useEffect } from 'react';
import './tailwind.css';

// 1. NHẬN DỮ LIỆU ĐỀ THI TỪ NGOÀI TRUYỀN VÀO QUA BIẾN `testData`
export default function PaperTest({ onBack, testData }: { onBack: () => void, testData: any }) {
  const [answers, setAnswers] = useState<Record<number, string>>(() => {
    const saved = localStorage.getItem(`answers_${testData.testId}`);
    return saved ? JSON.parse(saved) : {};
  });
  const [bookmarked, setBookmarked] = useState<number[]>(() => {
    const saved = localStorage.getItem(`bookmarks_${testData.testId}`);
    return saved ? JSON.parse(saved) : [];
  });
  const [isSubmitted, setIsSubmitted] = useState<boolean>(() => {
    return localStorage.getItem(`submitted_${testData.testId}`) === 'true';
  });

  // 2. KHI HỌC SINH ĐỔI ĐỀ KHÁC, CẬP NHẬT LẠI LOCALSTORAGE CỦA ĐỀ ĐÓ
  useEffect(() => {
    const savedAnswers = localStorage.getItem(`answers_${testData.testId}`);
    setAnswers(savedAnswers ? JSON.parse(savedAnswers) : {});
    
    const savedBookmarks = localStorage.getItem(`bookmarks_${testData.testId}`);
    setBookmarked(savedBookmarks ? JSON.parse(savedBookmarks) : []);
    
    const savedSubmit = localStorage.getItem(`submitted_${testData.testId}`);
    setIsSubmitted(savedSubmit === 'true');
  }, [testData.testId]);

  useEffect(() => {
    localStorage.setItem(`answers_${testData.testId}`, JSON.stringify(answers));
    localStorage.setItem(`bookmarks_${testData.testId}`, JSON.stringify(bookmarked));
    localStorage.setItem(`submitted_${testData.testId}`, isSubmitted.toString());
  }, [answers, bookmarked, isSubmitted, testData.testId]);

  const handleAnswer = (qId: number, option: string) => {
    if (isSubmitted) return; 
    setAnswers(prev => ({ ...prev, [qId]: option }));
  };

  const toggleBookmark = (qId: number) => {
    setBookmarked(prev => prev.includes(qId) ? prev.filter(id => id !== qId) : [...prev, qId]);
  };

 // --- HÀM NỘP BÀI VÀ BẮN ĐIỂM LÊN CLOUD ---
 const handleSubmit = async () => {
  const unanswered = testData.totalQuestions - Object.keys(answers).length;
  let confirmMsg = unanswered > 0 ? `Bạn còn ${unanswered} câu chưa làm. Vẫn nộp bài?` : "Bạn có chắc chắn muốn nộp bài?";
  
  if (window.confirm(confirmMsg)) {
    setIsSubmitted(true);
    window.scrollTo({ top: 0, behavior: 'smooth' }); // Tự động cuộn lên đầu xem điểm
    
    // 1. Chấm điểm ngay lập tức
    let finalScore = 0;
    testData.questions.forEach((q: any) => { if (answers[q.id] === q.correctAnswer) finalScore++; });
    const finalAccuracy = testData.questions.length > 0 ? Math.round((finalScore / testData.questions.length) * 100) : 0;

    // 2. Kéo thông tin xem Học sinh nào đang đăng nhập
    const { data: { session } } = await import('./supabase').then(m => m.supabase.auth.getSession());
    
    // 3. Đẩy điểm số lên Kho dữ liệu test_results
    if (session) {
      try {
        await import('./supabase').then(m => m.supabase.from('test_results').insert([{
          user_email: session.user.email,
          test_id: testData.testId || "offline_demo",
          test_title: testData.title || "Bài test",
          score: finalScore,
          total_questions: testData.totalQuestions,
          accuracy: finalAccuracy
        }]));
      } catch (err) {
        console.error("Lỗi lưu điểm:", err);
      }
    }
  }
};

  const clearDraft = () => {
    if (window.confirm("Xóa toàn bộ dữ liệu và làm lại từ đầu?")) {
      localStorage.removeItem(`answers_${testData.testId}`);
      localStorage.removeItem(`bookmarks_${testData.testId}`);
      localStorage.removeItem(`submitted_${testData.testId}`);
      setAnswers({}); setBookmarked([]); setIsSubmitted(false);
    }
  };

  const scrollToQuestion = (qId: number) => {
    const element = document.getElementById(`q-${qId}`);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'center' });
      element.classList.add('ring-2', 'ring-blue-400');
      setTimeout(() => element.classList.remove('ring-2', 'ring-blue-400'), 1500);
    }
  };

  let score = 0;
  testData.questions.forEach((q: any) => { if (answers[q.id] === q.correctAnswer) score++; });

  const totalQuestions = testData.totalQuestions; 
  const answeredCount = Object.keys(answers).length;
  const unansweredCount = totalQuestions - answeredCount;
  const navigationGrid = Array.from({ length: totalQuestions }, (_, i) => i + 1);
  const accuracy = testData.questions.length > 0 ? Math.round((score / testData.questions.length) * 100) : 0;

  return (
    <div className="flex flex-col h-screen bg-[#f3f4f6] font-sans text-gray-800 overflow-hidden">
      <header className="bg-white border-b border-gray-200 px-8 py-4 flex justify-between items-center shrink-0 z-10 shadow-sm">
        <div className="flex items-center gap-4">
          <button onClick={onBack} className="border border-gray-300 hover:bg-gray-100 text-sm px-3 py-1.5 rounded font-medium transition">⬅ Menu</button>
          <div className="font-bold text-gray-800 text-lg border-l border-gray-300 pl-4">{testData.title}</div>
        </div>
        <div className="flex items-center gap-4">
          <button onClick={clearDraft} className="text-red-500 hover:text-red-700 text-sm font-medium underline">
            {isSubmitted ? "Làm lại bài thi" : "Xóa nháp"}
          </button>
        </div>
      </header>

      <main className="max-w-7xl mx-auto w-full px-6 pt-6 pb-2 flex flex-col md:flex-row gap-8 items-start flex-1 overflow-hidden">
        <section className="flex-1 min-w-0 h-full overflow-y-auto pr-4 custom-scrollbar pb-10 space-y-6">
          {isSubmitted && (
            <div className="bg-gradient-to-r from-blue-600 to-[#5fc2f5] p-8 rounded-xl shadow-lg text-white">
              <h2 className="text-2xl font-bold mb-4">Kết quả bài làm</h2>
              <div className="flex gap-10">
                <div><p className="text-blue-100 text-sm uppercase font-bold tracking-wider mb-1">Số câu đúng</p><p className="text-4xl font-black">{score} / <span className="text-2xl text-blue-200">{testData.questions.length}</span></p></div>
                <div><p className="text-blue-100 text-sm uppercase font-bold tracking-wider mb-1">Độ chính xác</p><p className="text-4xl font-black">{accuracy}%</p></div>
              </div>
            </div>
          )}

          <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <h2 className="font-bold text-lg mb-2">{testData.partName}</h2>
            {testData.instructions && testData.instructions.map((inst: string, idx: number) => <p key={idx} className="text-gray-700 mb-2 leading-relaxed">{inst}</p>)}
            {!isSubmitted && testData.audioUrl && <div className="mt-4"><audio controls className="w-full h-10 outline-none"><source src={testData.audioUrl} type="audio/mpeg" /></audio></div>}
          </div>

          {testData.questions.map((q: any) => {
            const userAnswer = answers[q.id];
            const isCorrect = userAnswer === q.correctAnswer;
            const hasAnswered = userAnswer !== undefined;

            return (
              <div key={q.id} id={`q-${q.id}`} className={`bg-white border-2 rounded-xl p-6 shadow-sm transition-all relative ${isSubmitted ? (isCorrect ? 'border-green-400 bg-green-50/30' : (hasAnswered ? 'border-red-300 bg-red-50/30' : 'border-gray-300 opacity-80')) : 'border-transparent hover:border-gray-200'}`}>
                {!isSubmitted && (
                  <button onClick={() => toggleBookmark(q.id)} className={`absolute top-6 right-6 p-2 border rounded-md ${bookmarked.includes(q.id) ? 'bg-orange-50 border-orange-400 text-orange-500' : 'border-gray-200 text-gray-400'}`}>
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill={bookmarked.includes(q.id) ? "currentColor" : "none"} stroke="currentColor" strokeWidth="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
                  </button>
                )}
                <h3 className="font-bold text-gray-800 mb-2 flex items-center gap-2">Question {q.id}: {isSubmitted && hasAnswered && isCorrect && <span className="text-green-600 bg-green-100 px-2 py-0.5 rounded text-sm">✅ Đúng</span>}{isSubmitted && hasAnswered && !isCorrect && <span className="text-red-500 bg-red-100 px-2 py-0.5 rounded text-sm">❌ Sai</span>}</h3>
                <p className="text-gray-800 mb-5 font-medium">{q.text}</p>
                
                <div className="space-y-3">
                  {q.options.map((opt: string) => {
                    const isSelected = userAnswer === opt;
                    const isTheCorrectOption = opt === q.correctAnswer;
                    let optionClass = "border-gray-300 bg-gray-50"; 
                    let textClass = "text-gray-700";

                    if (!isSubmitted) {
                      if (isSelected) optionClass = "border-[#2b88c9] bg-[#2b88c9]";
                    } else {
                      if (isTheCorrectOption) { optionClass = "border-green-500 bg-green-500"; textClass = "text-green-700 font-bold"; }
                      else if (isSelected && !isCorrect) { optionClass = "border-red-500 bg-red-500"; textClass = "text-red-600 line-through opacity-70"; }
                      else { optionClass = "border-gray-200 bg-gray-100 opacity-50"; textClass = "text-gray-400"; }
                    }

                    return (
                      <label key={opt} className={`flex items-center gap-3 w-fit py-1 pr-3 rounded ${isSubmitted && isTheCorrectOption ? 'bg-green-100 border border-green-300' : 'border border-transparent'} ${!isSubmitted ? 'cursor-pointer group' : 'cursor-default'}`}>
                        <div className={`w-5 h-5 ml-2 rounded-full border flex items-center justify-center transition-colors ${optionClass} ${!isSubmitted && !isSelected ? 'group-hover:border-gray-400' : ''}`}>
                          {(isSelected || (isSubmitted && isTheCorrectOption)) && <div className="w-2 h-2 rounded-full bg-white"></div>}
                        </div>
                        <input type="radio" name={`q-${q.id}`} value={opt} checked={isSelected} onChange={() => handleAnswer(q.id, opt)} disabled={isSubmitted} className="hidden" />
                        <span className={textClass}>{opt}</span>
                      </label>
                    );
                  })}
                </div>
                {isSubmitted && q.explanation && (
                  <div className="mt-6 bg-[#f0f9ff] border border-[#bae6fd] p-4 rounded-lg relative">
                    <span className="absolute -top-3 left-4 bg-[#bae6fd] text-[#0369a1] text-xs font-bold px-2 py-0.5 rounded">Giải thích (Explanation)</span>
                    <p className="text-sm text-[#0c4a6e] mt-1 leading-relaxed">{q.explanation}</p>
                  </div>
                )}
              </div>
            );
          })}
          
          <div className="h-40 border-2 border-dashed border-gray-300 rounded-xl flex items-center justify-center text-gray-400 bg-white">
            (Hết bài thi)
          </div>
        </section>

        <aside className="w-[340px] shrink-0 h-full overflow-y-auto custom-scrollbar pb-10">
          <div className="bg-white border border-gray-200 rounded-xl p-5 shadow-sm">
            {!isSubmitted ? <div className="bg-[#fff1f2] border border-[#ffe4e6] text-[#e11d48] font-bold text-center py-3 rounded-lg mb-6">⏱ {testData.timeLimit}</div> : <div className="bg-gray-100 border border-gray-300 text-gray-600 font-bold text-center py-3 rounded-lg mb-6">✅ Đã nộp bài</div>}
            <h3 className="font-bold text-sm mb-4 text-gray-700">Danh sách câu hỏi</h3>
            
            {!isSubmitted && (
                <div className="flex flex-col gap-3 mb-6 text-sm">
                    <div className="flex justify-between items-center"><div className="flex items-center gap-2"><div className="w-3 h-3 rounded-full bg-gray-200"></div><span className="text-gray-600">Chưa trả lời</span></div><span className="font-bold">({unansweredCount})</span></div>
                    <div className="flex justify-between items-center"><div className="flex items-center gap-2"><div className="w-3 h-3 rounded-full bg-[#5fc2f5]"></div><span className="text-gray-600">Đã trả lời</span></div><span className="font-bold text-[#2b88c9]">({answeredCount})</span></div>
                </div>
            )}

            <div className="grid grid-cols-5 gap-3 mb-6">
              {navigationGrid.map(num => {
                const q = testData.questions.find((item: any) => item.id === num);
                const isAnswered = answers[num] !== undefined;
                const isBookmarked = bookmarked.includes(num);
                let btnClass = "bg-gray-100 text-gray-600 border border-transparent"; 
                if (!isSubmitted) {
                  if (isAnswered) btnClass = "bg-[#5fc2f5] text-white"; 
                  if (isBookmarked) btnClass += " ring-2 ring-orange-400"; 
                  btnClass += " hover:bg-gray-200 cursor-pointer";
                } else {
                  if (q) {
                    if (answers[num] === q.correctAnswer) btnClass = "bg-green-500 text-white shadow-sm"; 
                    else if (answers[num]) btnClass = "bg-red-500 text-white shadow-sm"; 
                    else btnClass = "bg-gray-200 text-gray-400"; 
                  } else { btnClass = "bg-gray-50 text-gray-300"; }
                  btnClass += " cursor-pointer hover:opacity-80";
                }
                return (
                  <button key={num} onClick={() => scrollToQuestion(num)} className={`w-10 h-10 rounded-full flex items-center justify-center text-[13px] font-bold transition-all ${btnClass}`}>{num}</button>
                );
              })}
            </div>
            {!isSubmitted && <button onClick={handleSubmit} className="w-full bg-[#2b88c9] hover:bg-[#1a6ea6] text-white font-bold py-3.5 rounded-lg transition-colors shadow-sm">Nộp bài & Chấm điểm</button>}
          </div>
        </aside>

      </main>

      <style dangerouslySetInnerHTML={{__html: `
        .custom-scrollbar::-webkit-scrollbar { width: 6px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
      `}} />
    </div>
  );
}