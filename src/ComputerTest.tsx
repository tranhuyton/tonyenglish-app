import React, { useState, useRef, useEffect } from 'react';
import './tailwind.css';

export default function ComputerTest({ onBack }: { onBack: () => void }) {
  const [answers, setAnswers] = useState<Record<string, string>>(() => {
    const saved = localStorage.getItem('ielts_computer_answers');
    return saved ? JSON.parse(saved) : {};
  });

  useEffect(() => {
    localStorage.setItem('ielts_computer_answers', JSON.stringify(answers));
  }, [answers]);

  const handleAnswer = (qNum: string, value: string) => {
    setAnswers(prev => ({ ...prev, [qNum]: value }));
  };

  const clearDraft = () => {
    if(window.confirm('Bạn có chắc muốn xóa bản nháp và làm lại từ đầu?')) {
      localStorage.removeItem('ielts_computer_answers');
      setAnswers({});
    }
  };

  // --- LOGIC COPY, HIGHLIGHT & NOTE ---
  const [highlightMenu, setHighlightMenu] = useState({ x: 0, y: 0, show: false });
  const [currentRange, setCurrentRange] = useState<Range | null>(null);

  const handleMouseUp = () => {
    const selection = window.getSelection();
    if (selection && selection.toString().trim().length > 0) {
      const range = selection.getRangeAt(0);
      const rect = range.getBoundingClientRect();
      // Điều chỉnh vị trí y một chút để menu không đè lên text (giống ảnh)
      setHighlightMenu({ x: rect.left + rect.width / 2, y: rect.top - 10, show: true });
      setCurrentRange(range);
    } else {
      setHighlightMenu({ ...highlightMenu, show: false });
      setCurrentRange(null);
    }
  };

  const handleCopy = async () => {
    if (currentRange) {
      try {
        await navigator.clipboard.writeText(currentRange.toString());
      } catch (err) {
        console.error('Failed to copy text: ', err);
      }
      setHighlightMenu({ ...highlightMenu, show: false });
      window.getSelection()?.removeAllRanges();
    }
  };

  const applyHighlight = () => {
    if (currentRange) {
      const span = document.createElement('span');
      span.className = 'bg-yellow-300 cursor-pointer rounded-sm';
      span.title = "Click để xóa highlight";
      span.onclick = function() {
        const parent = this.parentNode;
        if (parent) {
          const textNode = document.createTextNode(this.textContent || '');
          parent.replaceChild(textNode, this);
        }
      };
      try {
        currentRange.surroundContents(span);
      } catch (e) {
        alert("Lưu ý: Chỉ nên bôi đen gọn trong 1 đoạn văn để highlight không bị lỗi nhé!");
      }
      setHighlightMenu({ ...highlightMenu, show: false });
      window.getSelection()?.removeAllRanges();
    }
  };

  const handleNote = () => {
    if (currentRange) {
      const noteText = window.prompt("Nhập nội dung ghi chú của bạn:");
      if (noteText && noteText.trim() !== "") {
        const span = document.createElement('span');
        // Thêm gạch chân đỏ để phân biệt Note với Highlight thường
        span.className = 'bg-yellow-300 cursor-pointer rounded-sm border-b-2 border-red-500';
        span.title = `Ghi chú: ${noteText}`;
        span.dataset.note = noteText; // Lưu data note vào DOM
        span.onclick = function() {
          // Khi click vào đoạn có note, hỏi xem muốn xóa không
          if(window.confirm(`Ghi chú của bạn: "${this.dataset.note}"\n\nBạn có muốn xóa ghi chú này không?`)) {
            const parent = this.parentNode;
            if (parent) {
              const textNode = document.createTextNode(this.textContent || '');
              parent.replaceChild(textNode, this);
            }
          }
        };
        try {
          currentRange.surroundContents(span);
        } catch (e) {
          alert("Lưu ý: Chỉ nên bôi đen gọn trong 1 đoạn văn để không bị lỗi nhé!");
        }
      }
      setHighlightMenu({ ...highlightMenu, show: false });
      window.getSelection()?.removeAllRanges();
    }
  };


  // --- LOGIC KÉO THẢ ---
  const [leftWidth, setLeftWidth] = useState(50);
  const containerRef = useRef<HTMLElement>(null);
  const isDragging = useRef(false);

  const startDrag = () => {
    isDragging.current = true;
    document.body.style.cursor = 'col-resize';
    document.body.style.userSelect = 'none';
  };

  const onDrag = (e: MouseEvent) => {
    if (!isDragging.current || !containerRef.current) return;
    const containerRect = containerRef.current.getBoundingClientRect();
    const newLeftWidth = ((e.clientX - containerRect.left) / containerRect.width) * 100;
    if (newLeftWidth > 20 && newLeftWidth < 80) setLeftWidth(newLeftWidth);
  };

  const stopDrag = () => {
    isDragging.current = false;
    document.body.style.cursor = 'default';
    document.body.style.userSelect = 'auto';
  };

  useEffect(() => {
    window.addEventListener('mousemove', onDrag);
    window.addEventListener('mouseup', stopDrag);
    return () => {
      window.removeEventListener('mousemove', onDrag);
      window.removeEventListener('mouseup', stopDrag);
    };
  }, []);

  const scrollToQuestion = (qNum: number | string) => {
    const element = document.getElementById(`q-${qNum}`);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'center' });
      element.classList.add('bg-yellow-200', 'transition-colors', 'duration-500');
      setTimeout(() => element.classList.remove('bg-yellow-200'), 1500);
    }
  };

  const renderInlineQuestion = (text: string) => {
    const parts = text.split(/(\[\d+\])/g);
    return parts.map((part, index) => {
      const match = part.match(/\[(\d+)\]/);
      if (match) {
        const qNum = match[1];
        return (
          <span key={index} id={`q-${qNum}`} className="inline-flex items-center mx-1 rounded">
            <span className="bg-gray-200 text-black font-bold px-2 py-0.5 border border-gray-400 border-r-0 text-sm">{qNum}</span>
            <input type="text" className="w-32 px-2 py-0.5 border border-gray-400 focus:outline-none focus:border-black focus:ring-1 focus:ring-black text-sm text-black" value={answers[qNum] || ''} onChange={(e) => handleAnswer(qNum, e.target.value)} autoComplete="off" />
          </span>
        );
      }
      return <span key={index}>{part}</span>;
    });
  };

  const footerQuestions = Array.from({ length: 13 }, (_, i) => i + 1);

  return (
    <div className="flex flex-col h-screen bg-white font-sans text-gray-900 relative">
      
      {/* POPUP MENU HIGHLIGHT, COPY, NOTE (Thiết kế giống ảnh mẫu) */}
      {highlightMenu.show && (
        <div 
          style={{ left: highlightMenu.x, top: highlightMenu.y, transform: 'translate(-50%, -100%)' }} 
          className="fixed z-50 bg-white text-gray-800 rounded shadow-[0_4px_15px_rgba(0,0,0,0.15)] border border-gray-200 text-sm flex flex-col py-1 min-w-[130px]"
          // Dùng onMouseDown với preventDefault để không bị mất bôi đen khi bấm vào menu
          onMouseDown={(e) => e.preventDefault()}
        >
          <button onClick={handleCopy} className="flex items-center gap-3 px-4 py-2 hover:bg-gray-100 text-left w-full transition-colors">
            <svg className="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"></path></svg>
            <span className="font-medium">Copy</span>
          </button>
          
          <button onClick={applyHighlight} className="flex items-center gap-3 px-4 py-2 hover:bg-gray-100 text-left w-full transition-colors">
            <svg className="w-4 h-4 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg>
            <span className="font-medium">Highlight</span>
          </button>

          <button onClick={handleNote} className="flex items-center gap-3 px-4 py-2 hover:bg-gray-100 text-left w-full transition-colors">
            <svg className="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
            <span className="font-medium">Note</span>
          </button>
        </div>
      )}

      <header className="bg-[#1f2937] text-white px-6 py-3 flex justify-between items-center z-10 shrink-0">
        <div className="flex items-center gap-4">
          <button onClick={onBack} className="bg-gray-600 hover:bg-gray-500 text-sm px-3 py-1.5 rounded font-bold transition">⬅ Menu</button>
          <div className="font-bold text-lg tracking-wide border-l border-gray-500 pl-4">IELTS Reading - Computer Delivered</div>
        </div>
        <div className="flex items-center gap-4">
          <button onClick={clearDraft} className="text-sm text-red-400 hover:text-red-300 underline font-medium">Xóa nháp</button>
          <div className="font-bold text-[#ef4444] text-lg flex items-center gap-2">Time left: 59:59</div>
        </div>
      </header>

      {/* Gắn sự kiện onMouseUp vào Main để bắt vùng bôi đen */}
      <main className="flex flex-1 overflow-hidden relative" ref={containerRef} onMouseUp={handleMouseUp}>
        
        <section className="p-8 overflow-y-auto leading-relaxed custom-scrollbar" style={{ width: `${leftWidth}%`, flex: 'none' }}>
          <h2 className="font-bold text-xl mb-4">Reading Passage 1</h2>
          <p className="font-bold mb-6 text-gray-700">You should spend about 20 minutes on Questions 1-13.</p>
          <h3 className="font-bold text-center mb-6 text-2xl">The History of Bicycles</h3>
          <div className="text-justify space-y-4">
            <p>The bicycle was not invented by one single person. Rather, it evolved over a period of many years. The first precursor to the modern bicycle was created in 1817 by a German baron named Karl von Drais. His machine, known as the "running machine", was made of wood and had no pedals. Riders propelled themselves by pushing their feet against the ground.</p>
            <p>It wasn't until the 1860s that pedals were added to the front wheel, creating what became known as the velocipede. This invention was significantly improved in the 1870s with the introduction of the penny-farthing, a bicycle with a massive front wheel and a tiny rear wheel. Although it allowed for higher speeds, it was notoriously dangerous to ride due to its height and poor weight distribution.</p>
            <p>The modern bicycle design, featuring two wheels of the same size and a chain drive to the rear wheel, emerged in the late 1880s. This design, called the "safety bicycle," revolutionized personal transport and made cycling accessible to a much broader public.</p>
            <div className="h-[600px] mt-8 flex items-center justify-center text-gray-400 border-2 border-dashed border-gray-200 bg-gray-50">
              (Giả lập bài đọc rất dài - Hãy thử bôi đen chữ để test tính năng Highlight, Copy, Note anh nhé)
            </div>
          </div>
        </section>

        <div className="w-2 bg-gray-200 hover:bg-gray-300 cursor-col-resize flex flex-col justify-center items-center z-10 border-x border-gray-300" onMouseDown={startDrag}>
          <div className="w-0.5 h-10 bg-gray-500"></div>
        </div>

        <section className="p-8 overflow-y-auto leading-relaxed bg-[#f9fafb] custom-scrollbar" style={{ width: `${100 - leftWidth}%`, flex: 'none' }}>
          <div className="mb-12">
            <h3 className="font-bold text-lg mb-2">Questions 1 - 5</h3>
            <p className="italic mb-2 text-gray-600">Complete the notes below.</p>
            <div className="border border-gray-300 bg-white p-6 shadow-sm">
              <h4 className="font-bold mb-4">Bicycle Development</h4>
              <ul className="space-y-4 list-none">
                <li>• 1817: Karl von Drais invented a wooden machine without {renderInlineQuestion("[1]")}.</li>
                <li>• 1860s: The velocipede was created by adding pedals to the {renderInlineQuestion("[2]")} wheel.</li>
                <li>• 1880s: The {renderInlineQuestion("[3]")} bicycle introduced two equal-sized wheels.</li>
              </ul>
            </div>
          </div>

          <div className="mb-10">
            <h3 className="font-bold text-lg mb-4">Questions 6 - 8</h3>
            <div className="space-y-6">
              {[
                { id: 6, text: "Karl von Drais was the sole inventor of the modern bicycle." },
                { id: 7, text: "The running machine was propelled by the rider's feet touching the ground." },
                { id: 8, text: "The penny-farthing was popular among women." }
              ].map(q => (
                <div key={q.id} id={`q-${q.id}`} className="p-3 rounded border border-transparent hover:border-gray-200">
                  <div className="flex gap-4 mb-3"><span className="font-bold bg-gray-200 px-2 py-0.5 rounded border border-gray-300 text-sm">{q.id}</span><p>{q.text}</p></div>
                  <div className="flex gap-8 ml-10">
                    {['TRUE', 'FALSE', 'NOT GIVEN'].map(option => (
                      <label key={option} className="flex items-center gap-2 cursor-pointer">
                        <input type="radio" name={`q${q.id}`} value={option} checked={answers[q.id.toString()] === option} onChange={(e) => handleAnswer(q.id.toString(), e.target.value)} className="w-4 h-4 cursor-pointer accent-black" />
                        <span className="font-medium text-sm">{option}</span>
                      </label>
                    ))}
                  </div>
                </div>
              ))}
            </div>
            <div className="h-[400px]"></div>
          </div>
        </section>
      </main>

      <footer className="bg-[#f0f0f0] border-t border-gray-300 p-2 flex justify-between items-center shrink-0 z-20">
        <div className="flex items-center gap-2 ml-4">
          <input type="checkbox" id="review" className="w-4 h-4 cursor-pointer accent-black" />
          <label htmlFor="review" className="text-sm font-bold cursor-pointer">Review</label>
        </div>
        <div className="flex-1 flex justify-center items-center gap-1.5 overflow-x-auto px-4 py-1">
          {footerQuestions.map(num => {
            const isAnswered = answers[num.toString()] && answers[num.toString()].trim() !== '';
            return (
              <button key={num} onClick={() => scrollToQuestion(num)} className={`w-8 h-8 flex items-center justify-center font-bold text-sm bg-white cursor-pointer transition-all box-border ${isAnswered ? 'border-b-[4px] border-b-black border-t border-x border-gray-400 text-black' : 'border border-gray-400 text-black hover:bg-gray-100'}`}>
                {num}
              </button>
            )
          })}
        </div>
      </footer>
      
      <style dangerouslySetInnerHTML={{__html: `
        .custom-scrollbar::-webkit-scrollbar { width: 8px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
      `}} />
    </div>
  );
}