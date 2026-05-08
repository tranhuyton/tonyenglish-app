import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';

interface AITutorProps {
  isOpen: boolean;
  onClose: () => void;
  courseTitle: string;
  lectureTitle: string;
  htmlContent: string;
}

const SUGGESTED_PROMPTS = [
  "Tóm tắt ngắn gọn bài học này giúp tôi.",
  "Giải thích các từ vựng/khái niệm khó trong bài.",
  "Đưa ra một ví dụ minh họa dễ hiểu."
];

export default function AITutorSidebar({ isOpen, onClose, courseTitle, lectureTitle, htmlContent }: AITutorProps) {
  const [messages, setMessages] = useState<{ role: 'user' | 'ai'; text: string; isError?: boolean }[]>([]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // 🚀 TỐI ƯU HIỆU SUẤT: Chỉ phân tích HTML 1 lần duy nhất để tránh giật lag khi gõ phím
  const contextText = useMemo(() => {
    const doc = new DOMParser().parseFromString(htmlContent, 'text/html');
    return (doc.body.textContent || '').substring(0, 15000);
  }, [htmlContent]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  useEffect(() => {
    if (isOpen) setTimeout(() => textareaRef.current?.focus(), 300);
  }, [isOpen]);

  const handleSendMessage = async (suggestedText?: string | React.MouseEvent) => {
    const userMsg = typeof suggestedText === 'string' ? suggestedText : input.trim();
    if (!userMsg || isTyping) return;

    setMessages(prev => [...prev, { role: 'user', text: userMsg }]);
    setInput('');
    setIsTyping(true);
    
    if (textareaRef.current) {
        textareaRef.current.style.height = 'auto'; // Reset chiều cao input
    }

    try {
      const systemPrompt = `
        Bạn là một gia sư AI thân thiện, chuyên nghiệp của nền tảng TonyEnglish. 
        Học sinh đang học môn: "${courseTitle}", bài: "${lectureTitle}".
        Nội dung bài học hiện tại mà học sinh đang đọc là:
        """
        ${contextText}
        """
        Dựa VÀO NỘI DUNG TRÊN, hãy trả lời câu hỏi của học sinh. Giải thích dễ hiểu, súc tích, thân thiện. Trình bày rõ ràng bằng danh sách gạch đầu dòng nếu cần.
        LƯU Ý: TRẢ LỜI BẰNG ĐỊNH DẠNG VĂN BẢN (TEXT) BÌNH THƯỜNG DÙNG CÚ PHÁP MARKDOWN. KHÔNG ĐƯỢC TRẢ VỀ JSON.
        Câu hỏi của học sinh: "${userMsg}"
      `;

      const { data, error } = await supabase.functions.invoke('ai-grader', {
        body: { prompt: systemPrompt, model: 'gemini-2.5-flash' }
      });

      if (error) throw new Error(`Lỗi kết nối Supabase: ${error.message}`);
      if (data?.error) throw new Error(`Lỗi AI: ${data.error}`);

      let rawResponse = data.result;
      if (!rawResponse) throw new Error("AI không trả về kết quả nào.");

      // Lột bỏ vỏ bọc JSON nếu API vẫn cố tình trả về
      let finalResponse = rawResponse;
      if (typeof rawResponse === 'string') {
          try {
             const parsed = JSON.parse(rawResponse);
             finalResponse = parsed.response || parsed.reply || parsed.text || parsed.answer || rawResponse;
          } catch(e) { finalResponse = rawResponse; }
      } else if (typeof rawResponse === 'object') {
          finalResponse = rawResponse.response || rawResponse.reply || rawResponse.text || rawResponse.answer || JSON.stringify(rawResponse);
      }

      setMessages(prev => [...prev, { role: 'ai', text: finalResponse }]);
    } catch (error: any) {
      console.error("CHI TIẾT LỖI:", error);
      setMessages(prev => [...prev, { 
          role: 'ai', 
          text: `Hệ thống AI đang tạm thời gián đoạn. Chi tiết lỗi: ${error.message}`,
          isError: true
      }]);
    } finally {
      setIsTyping(false);
    }
  };

  // 🚀 NÂNG CẤP TRÌNH BIÊN DỊCH MARKDOWN SIÊU NHANH
  const formatMarkdown = (text: string) => {
    if (!text) return '';
    let html = text
      .replace(/</g, '&lt;').replace(/>/g, '&gt;') // Lọc thẻ HTML rác
      .replace(/```([\s\S]*?)```/g, '<pre class="bg-slate-800 text-slate-100 p-3 rounded-lg my-2 overflow-x-auto text-[13px] font-mono custom-scrollbar">$1</pre>')
      .replace(/`([^`]+)`/g, '<code class="bg-blue-50 text-blue-600 px-1.5 py-0.5 rounded text-[13px] font-mono border border-blue-100">$1</code>')
      .replace(/\*\*(.*?)\*\*/g, '<strong class="font-bold text-slate-800">$1</strong>')
      .replace(/\*(.*?)\*/g, '<em class="italic text-slate-700">$1</em>')
      .replace(/^### (.*$)/gim, '<h3 class="font-bold text-lg text-slate-800 mt-4 mb-2">$1</h3>')
      .replace(/^## (.*$)/gim, '<h2 class="font-black text-xl text-[#0a5482] mt-4 mb-2">$1</h2>')
      .replace(/^# (.*$)/gim, '<h1 class="font-black text-2xl text-[#0a5482] mt-4 mb-3">$1</h1>')
      .replace(/^\s*[\-\*] (.*$)/gim, '<li class="ml-5 list-disc marker:text-[#1e88e5] mb-1">$1</li>')
      .replace(/^\s*\d+\. (.*$)/gim, '<li class="ml-5 list-decimal marker:text-[#1e88e5] font-bold mb-1"><span class="font-medium text-slate-700">$1</span></li>')
      .replace(/\n/g, '<br/>')
      .replace(/<\/li><br\/>/g, '</li>')
      .replace(/<\/h([1-3])><br\/>/g, '</h$1>')
      .replace(/<\/pre><br\/>/g, '</pre>');
    return html;
  };

  const handleTextareaInput = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setInput(e.target.value);
    e.target.style.height = 'auto';
    e.target.style.height = `${Math.min(e.target.scrollHeight, 120)}px`;
  };

  return (
    <>
      {isOpen && (
        <div 
          className="fixed inset-0 bg-slate-900/40 z-[90] md:hidden transition-opacity duration-300" 
          onClick={onClose} 
        />
      )}

      {/* Sidebar sử dụng transform-gpu để mượt mà nhất */}
      <div 
        className={`fixed top-0 md:top-[60px] bottom-0 right-0 w-full md:w-[420px] bg-[#f8fafc] shadow-2xl z-[100] flex flex-col transition-transform duration-300 ease-in-out transform-gpu will-change-transform border-l border-slate-200 ${isOpen ? 'translate-x-0' : 'translate-x-full'}`}
      >
        {/* HEADER */}
        <div className="h-16 bg-gradient-to-r from-[#0a5482] to-[#1e88e5] text-white flex items-center justify-between px-5 shrink-0 shadow-sm z-10">
          <div className="flex items-center gap-3">
             <div className="w-10 h-10 bg-white/10 rounded-lg border border-white/20 flex items-center justify-center shadow-inner">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M8.25 3v1.5M4.5 8.25H3m18 0h-1.5M4.5 12H3m18 0h-1.5m-15 3.75H3m18 0h-1.5M8.25 19.5V21M12 3v1.5m0 15V21m3.75-18v1.5m0 15V21m-9-1.5h10.5a2.25 2.25 0 002.25-2.25V6.75a2.25 2.25 0 00-2.25-2.25H6.75A2.25 2.25 0 004.5 6.75v10.5a2.25 2.25 0 002.25 2.25zm.75-12h9v9h-9v-9z" />
                </svg>
             </div>
             <div>
                <h3 className="font-bold text-[15px] leading-tight tracking-wide">Trợ Lý Tony AI</h3>
                <p className="text-[11px] text-blue-100 font-medium tracking-wider uppercase">Online & Sẵn sàng hỗ trợ</p>
             </div>
          </div>
          <button onClick={onClose} className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/20 transition-colors">
             <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>

        {/* KHU VỰC CHAT */}
        <div className="flex-1 overflow-y-auto p-5 space-y-5 bg-[#f8fafc] custom-scrollbar">
          {messages.length === 0 ? (
            <div className="text-center mt-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
               <div className="w-20 h-20 bg-blue-50 rounded-full flex items-center justify-center mx-auto mb-4 border border-blue-100 shadow-sm">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-10 h-10 text-[#1e88e5]">
                    <path d="M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z" />
                  </svg>
               </div>
               <h4 className="font-black text-slate-800 text-[16px] mb-2">Xin chào!</h4>
               <p className="text-[14px] text-slate-500 mb-6 leading-relaxed px-2">
                 Thầy AI đã đọc xong nội dung bài <b>{lectureTitle}</b> rồi. Em có phần nào chưa hiểu thì hỏi Thầy nhé!
               </p>
               
               {/* GỢI Ý CÂU HỎI THÔNG MINH */}
               <div className="flex flex-col gap-2 px-2">
                 {SUGGESTED_PROMPTS.map((prompt, idx) => (
                    <button 
                       key={idx} 
                       onClick={() => handleSendMessage(prompt)}
                       className="bg-white border border-slate-200 text-slate-600 text-[13px] font-bold py-2.5 px-4 rounded-xl text-left hover:border-[#1e88e5] hover:text-[#1e88e5] hover:bg-blue-50 transition-colors shadow-sm flex items-center justify-between group"
                    >
                       <span>{prompt}</span>
                       <span className="text-slate-300 group-hover:text-[#1e88e5] transition-colors">→</span>
                    </button>
                 ))}
               </div>
            </div>
          ) : (
            messages.map((msg, idx) => (
              <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-in fade-in duration-300`}>
                 <div className={`max-w-[88%] p-3.5 text-[14px] leading-[1.7] shadow-sm ${
                    msg.role === 'user' 
                        ? 'bg-[#1e88e5] text-white rounded-2xl rounded-tr-sm' 
                        : msg.isError 
                            ? 'bg-red-50 border border-red-200 text-red-600 rounded-2xl rounded-tl-sm' 
                            : 'bg-white border border-slate-200 text-slate-700 rounded-2xl rounded-tl-sm'
                 }`}>
                    {msg.role === 'user' ? (
                       msg.text
                    ) : (
                       <div className="space-y-1.5" dangerouslySetInnerHTML={{ __html: formatMarkdown(msg.text) }} />
                    )}
                 </div>
              </div>
            ))
          )}
          
          {/* HIỆU ỨNG GÕ CHỮ TRANG NHÃ */}
          {isTyping && (
             <div className="flex justify-start animate-in fade-in">
               <div className="bg-white border border-slate-200 p-4 rounded-2xl rounded-tl-sm shadow-sm flex items-center gap-1.5">
                 <span className="w-2 h-2 bg-[#1e88e5] rounded-full animate-bounce"></span>
                 <span className="w-2 h-2 bg-[#1e88e5] rounded-full animate-bounce" style={{ animationDelay: '0.15s' }}></span>
                 <span className="w-2 h-2 bg-[#1e88e5] rounded-full animate-bounce" style={{ animationDelay: '0.3s' }}></span>
               </div>
             </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* INPUT KHUNG CHAT TỰ CO GIÃN */}
        <div className="p-4 bg-white border-t border-slate-200 shrink-0 shadow-[0_-10px_20px_rgba(0,0,0,0.02)] z-10">
          <div className="flex items-end gap-2 bg-slate-50 border border-slate-200 rounded-2xl p-1.5 focus-within:border-[#1e88e5] focus-within:bg-white focus-within:ring-1 focus-within:ring-blue-100 transition-all shadow-inner">
            <textarea 
              ref={textareaRef}
              value={input}
              onChange={handleTextareaInput}
              onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); handleSendMessage(); } }}
              placeholder="Hỏi trợ lý Tony AI..."
              className="flex-1 min-h-[40px] max-h-[120px] bg-transparent text-[14px] text-slate-700 font-medium px-3 py-2.5 outline-none resize-none custom-scrollbar placeholder:text-slate-400 placeholder:font-normal"
              rows={1}
            />
            <button 
              onClick={() => handleSendMessage()}
              disabled={!input.trim() || isTyping}
              className="w-10 h-10 shrink-0 rounded-xl bg-[#1e88e5] text-white flex items-center justify-center hover:bg-[#1565c0] disabled:bg-slate-200 disabled:text-slate-400 transition-colors mb-0.5 shadow-sm"
            >
               <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5 ml-0.5">
                 <path d="M3.478 2.404a.75.75 0 00-.926.941l2.432 7.905H13.5a.75.75 0 010 1.5H4.984l-2.432 7.905a.75.75 0 00.926.94 60.519 60.519 0 0018.445-8.986.75.75 0 000-1.218A60.517 60.517 0 003.478 2.404z" />
               </svg>
            </button>
          </div>
          <p className="text-[10px] text-center text-slate-400 mt-2 font-medium">Nhấn Shift + Enter để xuống dòng. Vui lòng kiểm tra lại thông tin nếu cần.</p>
        </div>
      </div>
    </>
  );
}