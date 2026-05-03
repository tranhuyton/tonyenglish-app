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
    if (word.includes(' ')) return;

    const range = selection.getRangeAt(0);
    const rect = range.getBoundingClientRect();

    setDictPopup({
      show: true,
      x: rect.left + rect.width / 2,
      y: rect.top - 10,
      word: word.replace(/[.,;!?]/g, '') 
    });
    setNotePopup(prev => ({ ...prev, show: false }));
  };

  // THUẬT TOÁN 2: BÔI ĐEN HIỆN THANH GHI CHÚ
  const handleMouseUp = (e: React.MouseEvent) => {
    setTimeout(() => {
      const selection = window.getSelection();
      if (!selection || selection.toString().trim() === '') {
        return;
      }

      const text = selection.toString().trim();
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

  const mockTranslate = (word: string) => {
    const dict: Record<string, string> = {
      'sustainable': 'bền vững, thân thiện với môi trường',
      'paradigm': 'mô hình, hệ chuẩn',
      'unprecedented': 'chưa từng có tiền lệ',
      'cohesion': 'sự gắn kết, liên kết',
      'mitigate': 'giảm nhẹ, làm dịu bớt',
      'metamorphosis': 'sự lột xác, sự biến đổi hoàn toàn',
      'quintessential': 'tinh túy, tinh hoa, ví dụ điển hình',
      'degradation': 'sự suy thoái, sự giảm sút',
      'utopian': 'không tưởng, hoàn hảo đến mức không thực tế'
    };
    const lowerWord = word.toLowerCase();
    return dict[lowerWord] || 'Đang tải dữ liệu từ điển API...';
  };

  return (
    <div className="min-h-screen bg-[#FAFAFA] font-serif text-slate-800 relative selection:bg-amber-200">
      
      {/* THANH ĐIỀU HƯỚNG BÊN TRÊN */}
      <header className="fixed top-0 left-0 right-0 h-[70px] bg-white/95 backdrop-blur-sm border-b border-slate-200 flex items-center px-6 z-40 transition-all shadow-[0_4px_20px_rgba(0,0,0,0.02)]">
        <div className="max-w-[800px] w-full mx-auto flex items-center justify-between">
          <button onClick={onBack} className="flex items-center gap-2 text-slate-500 hover:text-[#1e88e5] font-sans font-bold text-[14px] transition-colors px-4 py-2 rounded-xl hover:bg-slate-50">
            <span className="text-xl leading-none">←</span> Quay lại
          </button>
          
          <div className="flex gap-2">
            <button className="w-10 h-10 rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 hover:text-amber-600 transition-colors font-sans" title="Đổi cỡ chữ">A<span className="text-[10px]">a</span></button>
            <button className="w-10 h-10 rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 hover:text-[#1e88e5] transition-colors" title="Nghe Audio (AI Đọc)">🎧</button>
          </div>
        </div>
      </header>

      {/* KHU VỰC ĐỌC BÀI */}
      <main className="pt-32 pb-40 px-6">
        <article className="max-w-[700px] mx-auto">
          {/* Tiêu đề bài báo */}
          <header className="mb-12">
            <div className="flex items-center gap-3 mb-6 font-sans">
              <span className="px-3 py-1 bg-amber-100 text-amber-800 text-[11px] font-black uppercase tracking-widest rounded-md">{article.category}</span>
              <span className="text-[13px] font-medium text-slate-400">{article.date}</span>
            </div>
            <h1 className="text-4xl lg:text-5xl font-black text-slate-900 leading-[1.15] tracking-tight mb-8">
              {article.title}
            </h1>
            <div className="flex items-center gap-6 text-[14px] text-slate-500 font-sans font-medium border-t border-slate-200 pt-6">
              <span className="flex items-center gap-2">⏱️ 5 min read</span>
              <span className="flex items-center gap-2">👀 1.2k views</span>
            </div>
          </header>

          {/* Nội dung bài báo */}
          <div 
            ref={containerRef}
            onDoubleClick={handleDoubleClick}
            onMouseUp={handleMouseUp}
            className="text-[20px] leading-[1.9] text-[#2c3e50] tracking-wide [&>p]:mb-8 [&>p>strong]:font-black [&>p>strong]:text-black [&>p>em]:text-[#1e88e5] [&>p>em]:font-medium"
            dangerouslySetInnerHTML={{ __html: article.content }} 
          />
        </article>
      </main>

      {/* POPUP TỪ ĐIỂN */}
      {dictPopup.show && (
        <div 
          className="fixed z-50 bg-white rounded-[1.5rem] shadow-[0_10px_40px_rgba(0,0,0,0.15)] border border-slate-100 p-6 w-80 animate-in zoom-in-95 fade-in duration-200 font-sans"
          style={{ 
            left: `${dictPopup.x}px`, 
            top: `${dictPopup.y}px`, 
            transform: 'translate(-50%, -100%)',
            marginTop: '-16px'
          }}
          onMouseDown={e => e.stopPropagation()} 
        >
          <div className="absolute -bottom-2 left-1/2 -translate-x-1/2 w-5 h-5 bg-white border-b border-r border-slate-100 rotate-45"></div>
          <div className="relative z-10">
            <div className="flex justify-between items-start mb-3">
              <h4 className="font-black text-2xl text-[#1e88e5]">{dictPopup.word}</h4>
              <button className="w-8 h-8 rounded-full bg-blue-50 text-blue-600 flex items-center justify-center hover:bg-[#1e88e5] hover:text-white transition-colors" title="Phát âm">🔊</button>
            </div>
            <p className="text-[10px] font-black text-emerald-600 uppercase tracking-widest mb-3 bg-emerald-50 inline-block px-2.5 py-1 rounded-md">Từ điển Anh-Việt</p>
            <p className="text-[15px] text-slate-700 font-medium leading-relaxed">
              {mockTranslate(dictPopup.word)}
            </p>
            <div className="mt-5 pt-4 border-t border-slate-100 flex gap-3">
              <button className="flex-1 bg-[#1e88e5] hover:bg-[#1565c0] text-white font-bold text-[13px] py-2.5 rounded-xl transition-colors shadow-sm">Lưu Flashcard</button>
              <button className="flex-1 bg-slate-100 hover:bg-slate-200 text-slate-600 font-bold text-[13px] py-2.5 rounded-xl transition-colors">Hỏi AI thêm</button>
            </div>
          </div>
        </div>
      )}

      {/* POPUP NOTE/HIGHLIGHT */}
      {notePopup.show && (
        <div 
          className="fixed z-50 bg-[#1e293b] rounded-2xl shadow-2xl p-2 flex items-center gap-1.5 animate-in slide-in-from-bottom-2 fade-in duration-200 font-sans border border-slate-700"
          style={{ 
            left: `${notePopup.x}px`, 
            top: `${notePopup.y}px`, 
            transform: 'translate(-50%, -100%)',
            marginTop: '-16px'
          }}
          onMouseDown={e => e.stopPropagation()}
        >
          <div className="absolute -bottom-1.5 left-1/2 -translate-x-1/2 w-4 h-4 bg-[#1e293b] border-b border-r border-slate-700 rotate-45"></div>
          
          <button className="w-10 h-10 rounded-xl flex items-center justify-center hover:bg-slate-800 transition-colors group" title="Highlight Vàng">
            <div className="w-5 h-5 rounded-full bg-yellow-400 shadow-[0_0_10px_rgba(250,204,21,0.5)] group-hover:scale-110 transition-transform"></div>
          </button>
          <button className="w-10 h-10 rounded-xl flex items-center justify-center hover:bg-slate-800 transition-colors group" title="Highlight Xanh">
            <div className="w-5 h-5 rounded-full bg-emerald-400 shadow-[0_0_10px_rgba(52,211,153,0.5)] group-hover:scale-110 transition-transform"></div>
          </button>
          <button className="w-10 h-10 rounded-xl flex items-center justify-center hover:bg-slate-800 transition-colors group" title="Highlight Đỏ">
            <div className="w-5 h-5 rounded-full bg-rose-400 shadow-[0_0_10px_rgba(251,113,133,0.5)] group-hover:scale-110 transition-transform"></div>
          </button>
          
          <div className="w-px h-6 bg-slate-600 mx-2"></div>
          
          <button className="px-4 h-10 rounded-xl flex items-center justify-center hover:bg-slate-800 text-white font-bold text-[13px] transition-colors gap-2">
            📝 Ghi chú
          </button>
          <button className="px-4 h-10 rounded-xl flex items-center justify-center hover:bg-slate-800 text-amber-400 font-bold text-[13px] transition-colors gap-2">
            ✨ Dịch AI
          </button>
        </div>
      )}

    </div>
  );
}