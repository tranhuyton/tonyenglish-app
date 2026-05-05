import React, { useState, useEffect, useRef } from 'react';
import { supabase } from './supabase';

interface AITutorProps {
  isOpen: boolean;
  onClose: () => void;
  courseTitle: string;
  lectureTitle: string;
  htmlContent: string;
}

export default function AITutorSidebar({ isOpen, onClose, courseTitle, lectureTitle, htmlContent }: AITutorProps) {
  const [messages, setMessages] = useState<{ role: 'user' | 'ai'; text: string; isError?: boolean }[]>([]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  const extractTextFromHtml = (html: string) => {
    const doc = new DOMParser().parseFromString(html, 'text/html');
    return doc.body.textContent || '';
  };

  const handleSendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = input.trim();
    setMessages(prev => [...prev, { role: 'user', text: userMsg }]);
    setInput('');
    setIsTyping(true);

    try {
      const contextText = extractTextFromHtml(htmlContent);

      const systemPrompt = `
        Bạn là một gia sư AI thân thiện, chuyên nghiệp của nền tảng TonyEnglish. 
        Học sinh đang học môn: "${courseTitle}", bài: "${lectureTitle}".
        Nội dung bài học hiện tại mà học sinh đang đọc là:
        """
        ${contextText.substring(0, 15000)}
        """
        Dựa VÀO NỘI DUNG TRÊN, hãy trả lời câu hỏi của học sinh. Giải thích dễ hiểu, súc tích, thân thiện. 
        LƯU Ý: TRẢ LỜI BẰNG ĐỊNH DẠNG VĂN BẢN (TEXT) BÌNH THƯỜNG, KHÔNG ĐƯỢC TRẢ VỀ JSON.
        Câu hỏi của học sinh: "${userMsg}"
      `;

      const { data, error } = await supabase.functions.invoke('ai-grader', {
        body: { 
           prompt: systemPrompt,
           model: 'gemini-2.5-flash' 
        }
      });

      if (error) throw new Error(`Lỗi kết nối Supabase: ${error.message}`);
      if (data?.error) throw new Error(`Lỗi AI: ${data.error}`);

      let rawResponse = data.result;
      if (!rawResponse) throw new Error("AI không trả về kết quả nào.");

      // 🚀 BƯỚC 1: LỘT BỎ VỎ BỌC JSON (Nếu hàm ai-grader vẫn ngoan cố trả về JSON)
      let finalResponse = rawResponse;
      if (typeof rawResponse === 'string') {
          try {
             const parsed = JSON.parse(rawResponse);
             // Tìm trong cục JSON xem nội dung thực sự nằm ở chữ nào
             finalResponse = parsed.response || parsed.reply || parsed.text || parsed.answer || rawResponse;
          } catch(e) {
             // Không phải JSON thì giữ nguyên
             finalResponse = rawResponse;
          }
      } else if (typeof rawResponse === 'object') {
          finalResponse = rawResponse.response || rawResponse.reply || rawResponse.text || rawResponse.answer || JSON.stringify(rawResponse);
      }

      setMessages(prev => [...prev, { role: 'ai', text: finalResponse }]);
    } catch (error: any) {
      console.error("CHI TIẾT LỖI HOÀN CHỈNH:", error);
      setMessages(prev => [...prev, { 
          role: 'ai', 
          text: `Em đang bị lỗi kỹ thuật xíu ạ. Chi tiết: ${error.message}`,
          isError: true
      }]);
    } finally {
      setIsTyping(false);
    }
  };

  // 🚀 BƯỚC 2: HÀM BIÊN DỊCH MARKDOWN SIÊU TỐC
  const formatMarkdown = (text: string) => {
    if (!text) return '';
    let html = text;
    // Chuyển **chữ** thành <strong>chữ</strong>
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    // Chuyển *chữ* thành <em>chữ</em>
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
    // Chuyển ký tự xuống dòng (\n) thành thẻ <br/>
    html = html.replace(/\n/g, '<br/>');
    return html;
  };

  return (
    <>
      {isOpen && (
        <div className="fixed inset-0 bg-slate-900/20 z-[90] md:hidden" onClick={onClose} />
      )}

      <div 
        className={`fixed top-[60px] bottom-0 right-0 w-full md:w-[400px] bg-white border-l border-slate-200 shadow-[-5px_0_20px_rgba(0,0,0,0.05)] z-[100] flex flex-col transition-transform duration-300 ease-in-out ${isOpen ? 'translate-x-0' : 'translate-x-full'}`}
      >
        <div className="h-16 bg-gradient-to-r from-[#0a5482] to-[#3ea6e6] text-white flex items-center justify-between px-5 shrink-0">
          <div className="flex items-center gap-3">
             <div className="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center text-xl shadow-inner">🤖</div>
             <div>
                <h3 className="font-bold text-[15px] leading-tight">Gia sư AI</h3>
                <p className="text-[11px] text-blue-100">Đang đọc trang cùng bạn...</p>
             </div>
          </div>
          <button onClick={onClose} className="w-8 h-8 flex items-center justify-center rounded-full hover:bg-white/20 transition-colors">
            ✖
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-5 space-y-4 bg-[#f8fafc] custom-scrollbar">
          {messages.length === 0 ? (
            <div className="text-center text-slate-400 mt-10">
               <div className="text-5xl mb-3 opacity-50">👋</div>
               <p className="text-[14px]">Chào em! Thầy AI đã đọc xong nội dung bài <b>{lectureTitle}</b> rồi. Em có đoạn nào khó hiểu cứ hỏi Thầy nhé!</p>
            </div>
          ) : (
            messages.map((msg, idx) => (
              <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                 <div className={`max-w-[85%] p-3 text-[14px] leading-relaxed rounded-2xl shadow-sm ${
                    msg.role === 'user' ? 'bg-[#3ea6e6] text-white rounded-br-none' : 
                    msg.isError ? 'bg-red-50 border border-red-200 text-red-600 rounded-bl-none' :
                    'bg-white border border-slate-200 text-slate-700 rounded-bl-none'
                 }`}>
                    {/* Render chữ thường nếu là User, và Render HTML nếu là AI */}
                    {msg.role === 'user' ? (
                       msg.text
                    ) : (
                       <div dangerouslySetInnerHTML={{ __html: formatMarkdown(msg.text) }} />
                    )}
                 </div>
              </div>
            ))
          )}
          {isTyping && (
             <div className="flex justify-start">
               <div className="bg-white border border-slate-200 text-slate-500 p-3 rounded-2xl rounded-bl-none text-[13px] shadow-sm flex items-center gap-1">
                 <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce"></span>
                 <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce delay-100"></span>
                 <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce delay-200"></span>
               </div>
             </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="p-4 bg-white border-t border-slate-200 shrink-0">
          <div className="flex items-end gap-2 bg-slate-50 border border-slate-200 rounded-xl p-1.5 focus-within:border-[#3ea6e6] focus-within:bg-white transition-colors">
            <textarea 
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); handleSendMessage(); } }}
              placeholder="Hỏi Thầy AI về bài này..."
              className="flex-1 max-h-32 bg-transparent text-[14px] p-2 outline-none resize-none custom-scrollbar"
              rows={1}
            />
            <button 
              onClick={handleSendMessage}
              disabled={!input.trim() || isTyping}
              className="w-10 h-10 shrink-0 rounded-lg bg-[#3ea6e6] text-white flex items-center justify-center hover:bg-[#0284c7] disabled:opacity-50 disabled:hover:bg-[#3ea6e6] transition-colors mb-0.5"
            >
              ➤
            </button>
          </div>
        </div>
      </div>
    </>
  );
}