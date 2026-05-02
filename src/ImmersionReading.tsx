import React, { useState, useEffect, useRef } from 'react';

export default function ImmersionReading({ onBack }: { onBack?: () => void }) {
  // States cho Từ điển (Nhấp đúp)
  const [dictPopup, setDictPopup] = useState<{ show: boolean, x: number, y: number, word: string }>({ show: false, x: 0, y: 0, word: '' });
  
  // States cho Ghi chú/Highlight (Bôi đen)
  const [notePopup, setNotePopup] = useState<{ show: boolean, x: number, y: number, text: string }>({ show: false, x: 0, y: 0, text: '' });
  
  // Mock dữ liệu 1 bài báo mẫu
  const article = {
    title: "The Evolution of Urban Planning: Building Sustainable Cities",
    category: "Academic Reading",
    date: "02/05/2026",
    content: `
      <p>The concept of <strong>urban planning</strong> has undergone a massive transformation over the past century. Historically, cities were designed with a primary focus on industrial efficiency and vehicular transport. This led to the creation of sprawling metropolises characterized by severe traffic congestion and unprecedented levels of air pollution.</p>
      
      <p>However, contemporary urban planners are pivoting towards a more <em>sustainable paradigm</em>. The integration of expansive green spaces, the promotion of pedestrian-friendly infrastructure, and the implementation of robust public transit systems are now at the forefront of municipal development.</p>
      
      <p>A quintessential example of this shift is the "15-minute city" concept. This framework envisions neighborhoods where residents can access their essential daily needs—such as employment, education, healthcare, and leisure—within a 15-minute walk or bicycle ride from their homes. Such initiatives not only mitigate environmental degradation but also significantly enhance community well-being and social cohesion.</p>
      
      <p>To implement these changes effectively, city councils are increasingly relying on artificial intelligence and big data analytics to monitor traffic flows and optimize resource allocation. The metamorphosis of our urban landscapes is no longer a distant utopian dream; it is an impending necessity for the survival of our ecosystem.</p>
    `
  };

  const containerRef = useRef<HTMLDivElement>(null);

  // Xử lý khi click ra ngoài để đóng các Popup
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (dictPopup.show || notePopup.show) {
        setDictPopup(prev => ({ ...prev, show: false }));
        setNotePopup(prev => ({ ...prev, show: false }));
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, [dictPopup.show, notePopup.show]);

  // THUẬT TOÁN 1: NHẤP ĐÚP HIỆN TỪ ĐIỂN
  const handleDoubleClick = (e: React.MouseEvent) => {
    const selection = window.getSelection();
    if (!selection || selection.toString().trim() === '') return;

    const word = selection.toString().trim();
    // Bỏ qua nếu bôi đen cả 1 đoạn dài (chứa dấu cách)
    if (word.includes(' ')) return;

    const range = selection.getRangeAt(0);
    const rect = range.getBoundingClientRect();

    setDictPopup({
      show: true,
      x: rect.left + rect.width / 2,
      y: rect.top - 10,
      word: word.replace(/[.,;!?]/g, '') // Lọc bỏ dấu câu thừa
    });
    setNotePopup(prev => ({ ...prev, show: false }));
  };

  // THUẬT TOÁN 2: BÔI ĐEN HIỆN THANH GHI CHÚ
  const handleMouseUp = (e: React.MouseEvent) => {
    // Tránh xung đột với Double Click
    setTimeout(() => {
      const selection = window.getSelection();
      if (!selection || selection.toString().trim() === '') {
        return;
      }

      const text = selection.toString().trim();
      // Chỉ hiện thanh Highlight khi bôi đen cụm từ (có dấu cách)
      if (text.includes(' ') && !dictPopup.show) {
        const range = selection.getRangeAt(0);
        const rect = range.getBoundingClientRect();

        setNotePopup({
          show: true,
          x: rect.left + rect.width / 2,
          y: rect.top - 10,
          text: text
        });
      }
    }, 50);
  };

  // Giả lập Dữ liệu từ điển API
  const mockTranslate = (word: string) => {
    const dict: Record<string, string> = {
      'sustainable': 'bền vững, thân thiện với môi trường',
      'paradigm': 'mô hình, hệ chuẩn',
      'unprecedented': 'chưa từng có tiền lệ',
      'cohesion': 'sự gắn kết, sự liên kết',
      'mitigate': 'giảm nhẹ, làm dịu bớt',
      'metamorphosis': 'sự lột xác, sự biến đổi hoàn toàn'
    };
    const lowerWord = word.toLowerCase();
    return dict[lowerWord] || 'Đang tải dữ liệu từ điển API...';
  };

  return (
    <div className="min-h-screen bg-[#FDFCF8] font-sans text-slate-800 relative selection:bg-blue-200">
      
      {/* THANH ĐIỀU HƯỚNG BÊN TRÊN */}
      <header className="fixed top-0 left-0 right-0 h-16 bg-white/80 backdrop-blur-md border-b border-slate-200 flex items-center px-6 z-40 transition-all">
        <div className="max-w-4xl w-full mx-auto flex items-center justify-between">
          <button onClick={onBack} className="flex items-center gap-2 text-slate-500 hover:text-[#0a5482] font-bold text-sm transition-colors px-4 py-2 rounded-full hover:bg-slate-100">
            <span className="text-lg leading-none">←</span> Quay lại
          </button>
          
          <div className="flex gap-3">
            <button className="w-10 h-10 rounded-full flex items-center justify-center text-slate-400 hover:bg-slate-100 hover:text-amber-500 transition-colors tooltip-trigger" title="Đổi cỡ chữ">A<span className="text-[10px]">a</span></button>
            <button className="w-10 h-10 rounded-full flex items-center justify-center text-slate-400 hover:bg-slate-100 hover:text-[#0a5482] transition-colors tooltip-trigger" title="Nghe Audio (AI Đọc)">🎧</button>
          </div>
        </div>
      </header>

      {/* KHU VỰC ĐỌC BÀI (DISTRACTION-FREE) */}
      <main className="pt-32 pb-32 px-6">
        <article className="max-w-2xl mx-auto">
          {/* Tiêu đề bài báo */}
          <header className="mb-12 text-center sm:text-left">
            <div className="flex items-center justify-center sm:justify-start gap-3 mb-6">
              <span className="px-3 py-1 bg-[#0a5482] text-white text-[11px] font-black uppercase tracking-widest rounded-md">{article.category}</span>
              <span className="text-sm font-medium text-slate-400">{article.date}</span>
            </div>
            <h1 className="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 leading-[1.2] tracking-tight mb-6">
              {article.title}
            </h1>
            <div className="flex items-center justify-center sm:justify-start gap-4 text-sm text-slate-500 font-medium border-t border-slate-200 pt-6">
              <span className="flex items-center gap-2">⏱️ 5 min read</span>
              <span className="flex items-center gap-2">👀 1.2k views</span>
            </div>
          </header>

          {/* Nội dung bài báo - ĐÃ FIX LỖI __html VÀ CSS CĂN BẢN */}
          <div 
            ref={containerRef}
            onDoubleClick={handleDoubleClick}
            onMouseUp={handleMouseUp}
            className="font-serif text-[19px] leading-[1.9] text-[#333333] [&>p]:mb-6 [&>p>strong]:font-black [&>p>strong]:text-black [&>p>em]:text-[#0a5482]"
            dangerouslySetInnerHTML={{ __html: article.content }} 
          />
        </article>
      </main>

      {/* ========================================================= */}
      {/* POPUP 1: TỪ ĐIỂN (HIỂN THỊ KHI CLICK ĐÚP 1 TỪ) */}
      {/* ========================================================= */}
      {dictPopup.show && (
        <div 
          className="fixed z-50 bg-white rounded-2xl shadow-2xl border border-slate-200 p-5 w-72 animate-in zoom-in-95 fade-in duration-200"
          style={{ 
            left: `${dictPopup.x}px`, 
            top: `${dictPopup.y}px`, 
            transform: 'translate(-50%, -100%)',
            marginTop: '-12px'
          }}
          onMouseDown={e => e.stopPropagation()} // Chống click nhầm đóng popup
        >
          <div className="absolute -bottom-2 left-1/2 -translate-x-1/2 w-4 h-4 bg-white border-b border-r border-slate-200 rotate-45"></div>
          <div className="relative z-10">
            <div className="flex justify-between items-start mb-2">
              <h4 className="font-black text-xl text-[#0a5482]">{dictPopup.word}</h4>
              <button className="text-slate-400 hover:text-[#0a5482] transition-colors" title="Phát âm">🔊</button>
            </div>
            <p className="text-[11px] font-bold text-slate-400 uppercase tracking-widest mb-3 border-b border-slate-100 pb-2">Từ điển Anh-Việt</p>
            <p className="text-[14px] text-slate-700 font-medium leading-relaxed">
              {mockTranslate(dictPopup.word)}
            </p>
            <div className="mt-4 pt-3 border-t border-slate-100 flex gap-2">
              <button className="flex-1 bg-blue-50 hover:bg-blue-100 text-[#0a5482] font-bold text-xs py-2 rounded-lg transition-colors">Lưu Flashcard</button>
              <button className="flex-1 bg-slate-50 hover:bg-slate-100 text-slate-600 font-bold text-xs py-2 rounded-lg transition-colors">Hỏi AI thêm</button>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================= */}
      {/* POPUP 2: CÔNG CỤ NOTE (HIỂN THỊ KHI BÔI ĐEN ĐOẠN DÀI) */}
      {/* ========================================================= */}
      {notePopup.show && (
        <div 
          className="fixed z-50 bg-slate-900 rounded-xl shadow-2xl p-1.5 flex items-center gap-1 animate-in slide-in-from-bottom-2 fade-in duration-200"
          style={{ 
            left: `${notePopup.x}px`, 
            top: `${notePopup.y}px`, 
            transform: 'translate(-50%, -100%)',
            marginTop: '-12px'
          }}
          onMouseDown={e => e.stopPropagation()}
        >
          <div className="absolute -bottom-1.5 left-1/2 -translate-x-1/2 w-3 h-3 bg-slate-900 rotate-45"></div>
          
          <button className="w-8 h-8 rounded-lg flex items-center justify-center hover:bg-slate-800 transition-colors group" title="Highlight Vàng">
            <div className="w-4 h-4 rounded-full bg-yellow-400 border-2 border-slate-900 group-hover:scale-110 transition-transform"></div>
          </button>
          <button className="w-8 h-8 rounded-lg flex items-center justify-center hover:bg-slate-800 transition-colors group" title="Highlight Xanh">
            <div className="w-4 h-4 rounded-full bg-emerald-400 border-2 border-slate-900 group-hover:scale-110 transition-transform"></div>
          </button>
          <button className="w-8 h-8 rounded-lg flex items-center justify-center hover:bg-slate-800 transition-colors group" title="Highlight Đỏ">
            <div className="w-4 h-4 rounded-full bg-rose-400 border-2 border-slate-900 group-hover:scale-110 transition-transform"></div>
          </button>
          
          <div className="w-px h-5 bg-slate-700 mx-1"></div>
          
          <button className="px-3 h-8 rounded-lg flex items-center justify-center hover:bg-slate-800 text-white font-bold text-xs transition-colors gap-1.5">
            📝 Nháp Note
          </button>
          <button className="px-3 h-8 rounded-lg flex items-center justify-center hover:bg-slate-800 text-amber-400 font-bold text-xs transition-colors gap-1.5">
            ✨ Dịch AI
          </button>
        </div>
      )}

    </div>
  );
}