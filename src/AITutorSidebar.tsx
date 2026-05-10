import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';

interface AITutorProps {
  isOpen: boolean;
  onClose: () => void;
  mode?: 'tutor' | 'ielts'; 
  courseTitle?: string;
  lectureTitle?: string;
  htmlContent?: string;
  topicTitle?: string; 
}

const TUTOR_PROMPTS = [
  "Tóm tắt ngắn gọn bài học này giúp tôi.",
  "Giải thích các khái niệm khó trong bài.",
  "Đưa ra một ví dụ minh họa dễ hiểu."
];

const IELTS_PROMPTS = [
  "💡 Nhờ Giám khảo lập dàn ý (Pillars)",
  "📝 Chấm điểm bài viết của tôi",
  "🧠 Gợi ý từ vựng Band 8.0+"
];

export default function AITutorSidebar({ 
  isOpen, 
  onClose, 
  mode = 'tutor', 
  courseTitle, 
  lectureTitle, 
  htmlContent, 
  topicTitle 
}: AITutorProps) {
  
  const [messages, setMessages] = useState<{ role: 'user' | 'ai'; text: string; isError?: boolean }[]>([]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const hasAutoStarted = useRef<string | null>(null);

  const theme = mode === 'ielts' ? {
    headerBg: 'from-[#064e3b] to-[#0f766e]', title: 'IELTS Task 2 Assessor', subtitle: 'Giám khảo AI Độc quyền',
    icon: '🎓', userBg: 'bg-[#0f766e]', aiBorder: 'border-emerald-200', typingDot: 'bg-[#10b981]',
    btnColor: 'bg-[#0f766e] hover:bg-[#064e3b]', focusRing: 'focus-within:border-[#0f766e] focus-within:ring-teal-50',
    width: 'md:w-[550px]' 
  } : {
    headerBg: 'from-[#0a5482] to-[#1e88e5]', title: 'Trợ Lý Tony AI', subtitle: 'Online & Sẵn sàng hỗ trợ',
    icon: '🤖', userBg: 'bg-[#1e88e5]', aiBorder: 'border-slate-200', typingDot: 'bg-[#1e88e5]',
    btnColor: 'bg-[#1e88e5] hover:bg-[#1565c0]', focusRing: 'focus-within:border-[#1e88e5] focus-within:ring-blue-50',
    width: 'md:w-[400px]'
  };

  const contextText = useMemo(() => {
    if (mode === 'ielts') return '';
    if (htmlContent) {
        const doc = new DOMParser().parseFromString(htmlContent, 'text/html');
        return (doc.body.textContent || '').substring(0, 15000);
    }
    const lectureContainer = document.querySelector('.lecture-content'); 
    return (lectureContainer?.textContent || '').substring(0, 15000);
  }, [htmlContent, mode, isOpen]);

  useEffect(() => { messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' }); }, [messages, isTyping]);

  useEffect(() => {
    if (isOpen) {
       setTimeout(() => textareaRef.current?.focus(), 300);
       
       if (mode === 'ielts' && topicTitle && hasAutoStarted.current !== topicTitle) {
           hasAutoStarted.current = topicTitle;
           setMessages([]); 
           const autoMsg = `Nhờ Giám khảo phân tích cấu trúc, chọn Trụ ý và viết bài mẫu Band 8.0+ cho đề bài sau:\n"${topicTitle}"`;
           handleSendMessage(autoMsg, true); 
       } else if (mode === 'tutor' && htmlContent && hasAutoStarted.current !== lectureTitle) {
           hasAutoStarted.current = lectureTitle || 'tutor';
           setMessages([]);
           const autoMsg = `Hãy tóm tắt siêu ngắn gọn (khoảng 3-4 gạch đầu dòng) nội dung chính của bài học này để tôi dễ hình dung nhất.`;
           handleSendMessage(autoMsg, true);
       }
    }
  }, [isOpen, mode, topicTitle, htmlContent, lectureTitle]);

  const handleSendMessage = async (suggestedText?: string, isAutoStart = false) => {
    const userMsg = typeof suggestedText === 'string' ? suggestedText : input.trim();
    if (!userMsg || isTyping) return;

    if (!isAutoStart) {
        setMessages(prev => [...prev, { role: 'user', text: userMsg }]);
    } else {
        if (mode === 'ielts') {
            setMessages([{ role: 'ai', text: `Chào em! Thầy là **Giám khảo IELTS Task 2**. Thầy đang phân tích đề bài và lập dàn ý cho em đây. Đợi thầy vài giây nhé...` }]);
        } else {
            setMessages([{ role: 'ai', text: `Chào em! Thầy AI đang đọc bài học và tóm tắt lại cho em. Đợi thầy một chút nhé...` }]);
        }
    }
    
    setInput('');
    setIsTyping(true);
    if (textareaRef.current) textareaRef.current.style.height = 'auto';

    try {
      let endpoint = 'ai-grader'; 
      let payload: any = {};

      if (mode === 'ielts') {
         endpoint = 'task-2-ai-grader'; 
         payload = { content: isAutoStart ? userMsg : `Đề bài đang giải: ${topicTitle}\n\nYêu cầu/Bài làm của học sinh:\n${userMsg}` };
      } else {
         const systemPrompt = `Bạn là gia sư AI. Môn: "${courseTitle || ''}", Bài: "${lectureTitle || ''}". Nội dung: """${contextText}""". Hãy trả lời câu hỏi: "${userMsg}" bằng text thường, thân thiện.`;
         payload = { prompt: systemPrompt, model: 'gemini-2.5-flash' };
      }

      const { data, error } = await supabase.functions.invoke(endpoint, { body: payload });

      if (error) throw new Error(error.message);
      if (data?.error) throw new Error(data.error);

      // 🚀 BẮT MỌI LỖI TRẢ VỀ TỪ BACKEND
      let finalResponse = "Không có phản hồi từ AI";
      if (data) {
         finalResponse = data.text || data.result || data.response || data.reply || JSON.stringify(data);
      }
      
      if (typeof finalResponse === 'string' && finalResponse.startsWith('{')) {
          try {
             const parsed = JSON.parse(finalResponse);
             finalResponse = parsed.text || parsed.result || parsed.response || parsed.reply || finalResponse;
          } catch(e) {}
      }

      if (isAutoStart) {
          setMessages([{ role: 'ai', text: finalResponse }]);
      } else {
          setMessages(prev => [...prev, { role: 'ai', text: finalResponse }]);
      }
    } catch (error: any) {
      console.error("LỖI GỌI AI:", error);
      setMessages(prev => [...prev, { role: 'ai', text: `Hệ thống AI đang bận. Chi tiết: ${error.message}`, isError: true }]);
    } finally {
      setIsTyping(false);
    }
  };

  const handleSuggestionClick = (prompt: string) => {
      if (prompt.includes('Chấm điểm')) {
          setInput("Nhờ Giám khảo chấm điểm bài làm IELTS Task 2 sau của tôi:\n\n[Anh/chị dán bài viết vào đây...]");
          setTimeout(() => textareaRef.current?.focus(), 100);
      } else {
          handleSendMessage(prompt);
      }
  };

  const formatMarkdown = (text: string) => {
    if (!text) return '';
    return text
      .replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/\*\*(.*?)\*\*/g, '<strong class="font-bold text-slate-800">$1</strong>')
      .replace(/\*(.*?)\*/g, '<em class="italic text-slate-700">$1</em>')
      .replace(/^### (.*$)/gim, `<h3 class="font-bold text-[16px] text-slate-800 mt-5 mb-2 border-b ${mode==='ielts' ? 'border-emerald-200' : 'border-blue-200'} pb-1">$1</h3>`)
      .replace(/^## (.*$)/gim, `<h2 class="font-black text-[18px] ${mode==='ielts' ? 'text-[#0d9488]' : 'text-[#1e88e5]'} mt-6 mb-3 uppercase tracking-tight">$1</h2>`)
      .replace(/^# (.*$)/gim, `<h1 class="font-black text-[20px] ${mode==='ielts' ? 'text-[#0f766e]' : 'text-[#0a5482]'} mt-6 mb-4">$1</h1>`)
      .replace(/^\s*[\-\*] (.*$)/gim, `<li class="ml-5 list-disc ${mode==='ielts' ? 'marker:text-[#10b981]' : 'marker:text-[#1e88e5]'} mb-1.5 leading-relaxed">$1</li>`)
      .replace(/\n/g, '<br/>')
      .replace(/(?:^|\n)> (.*)/g, `<blockquote class="border-l-4 ${mode==='ielts' ? 'border-emerald-500 bg-emerald-50' : 'border-blue-500 bg-blue-50'} pl-3 italic text-slate-600 my-3 py-2 rounded-r-lg">$1</blockquote>`);
  };

  const handleTextareaInput = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setInput(e.target.value);
    e.target.style.height = 'auto';
    e.target.style.height = `${Math.min(e.target.scrollHeight, mode==='ielts' ? 250 : 120)}px`;
  };

  return (
    <>
      {isOpen && <div className="fixed inset-0 bg-slate-900/50 transition-opacity" style={{ zIndex: 9998 }} onClick={onClose} />}

      <div className={`fixed top-0 md:top-[60px] bottom-0 right-0 w-full ${theme.width} bg-[#f8fafc] shadow-2xl flex flex-col transition-transform duration-300 ease-in-out transform-gpu border-l border-slate-200 ${isOpen ? 'translate-x-0' : 'translate-x-full'}`} style={{ zIndex: 9999 }}>
        
        <div className={`h-[70px] bg-gradient-to-r ${theme.headerBg} text-white flex items-center justify-between px-6 shrink-0 shadow-md z-10 transition-colors`}>
          <div className="flex items-center gap-4">
             <div className="w-12 h-12 bg-white/20 rounded-xl border border-white/20 flex items-center justify-center shadow-inner text-2xl">{theme.icon}</div>
             <div>
                <h3 className="font-black text-[16px] leading-tight tracking-wide uppercase">{theme.title}</h3>
                <p className="text-[12px] text-white/80 font-medium tracking-wider uppercase mt-0.5">{theme.subtitle}</p>
             </div>
          </div>
          <button onClick={onClose} className="w-9 h-9 flex items-center justify-center rounded-xl bg-white/10 hover:bg-white/20 transition-colors">
             <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>

        {mode === 'ielts' && topicTitle && (
            <div className="bg-white p-5 border-b border-slate-200 shrink-0 z-10 shadow-sm">
               <div className="text-[11px] font-black text-slate-400 uppercase tracking-widest mb-2 flex items-center gap-2">
                 <span className="text-[#0f766e] text-lg leading-none">📝</span> Đề thi đang phân tích:
               </div>
               <div className="font-serif text-[14px] leading-relaxed text-slate-800 border-l-[3px] border-[#0f766e] pl-4 italic bg-slate-50 py-2 pr-3 rounded-r-lg max-h-[85px] overflow-y-auto custom-scrollbar">
                 {topicTitle}
               </div>
            </div>
        )}

        <div className="flex-1 overflow-y-auto p-5 md:p-6 space-y-6 custom-scrollbar scroll-smooth">
          {messages.length === 0 && mode === 'tutor' && (
            <div className="text-center mt-6 animate-in fade-in slide-in-from-bottom-4">
               <div className="w-20 h-20 bg-blue-50 rounded-full flex items-center justify-center mx-auto mb-4 border border-blue-100 shadow-sm text-4xl">👋</div>
               <h4 className="font-black text-slate-800 text-[16px] mb-2">Xin chào!</h4>
               <p className="text-[14px] text-slate-500 mb-6 leading-relaxed px-2">Thầy AI đã đọc xong bài học rồi. Em có phần nào chưa hiểu thì hỏi Thầy nhé!</p>
            </div>
          )}

          {messages.map((msg, idx) => (
             <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-in fade-in`}>
                <div className={`max-w-[92%] p-4 text-[15px] leading-[1.8] shadow-sm ${msg.role === 'user' ? `${theme.userBg} text-white rounded-2xl rounded-tr-sm font-medium` : msg.isError ? 'bg-red-50 border border-red-200 text-red-600 rounded-2xl rounded-tl-sm' : `bg-white border ${theme.aiBorder} text-slate-700 rounded-2xl rounded-tl-sm`}`}>
                   {msg.role === 'user' ? msg.text : <div className="space-y-1.5 break-words" dangerouslySetInnerHTML={{ __html: formatMarkdown(msg.text) }} />}
                </div>
             </div>
          ))}
          
          {isTyping && (
             <div className="flex justify-start animate-in fade-in">
               <div className={`bg-white border ${theme.aiBorder} px-5 py-4 rounded-2xl rounded-tl-sm shadow-sm flex items-center gap-3`}>
                 <span className={`text-[12px] font-bold uppercase tracking-widest ${mode==='ielts'?'text-emerald-700':'text-blue-700'}`}>{mode==='ielts'?'Giám khảo đang viết':'Trợ lý đang gõ'}</span>
                 <div className="flex items-center gap-1.5 mt-0.5">
                   <span className={`w-2 h-2 ${theme.typingDot} rounded-full animate-bounce`}></span>
                   <span className={`w-2 h-2 ${theme.typingDot} rounded-full animate-bounce`} style={{ animationDelay: '0.15s' }}></span>
                   <span className={`w-2 h-2 ${theme.typingDot} rounded-full animate-bounce`} style={{ animationDelay: '0.3s' }}></span>
                 </div>
               </div>
             </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="p-4 md:p-5 bg-white border-t border-slate-200 shrink-0 shadow-[0_-10px_20px_rgba(0,0,0,0.02)] z-10">
          
          <div className="flex gap-2 mb-3 overflow-x-auto custom-scrollbar pb-1">
             {(mode === 'ielts' ? IELTS_PROMPTS : TUTOR_PROMPTS).map((prompt, idx) => (
                <button 
                   key={idx} 
                   onClick={() => handleSuggestionClick(prompt)} 
                   className={`shrink-0 text-[12px] font-bold px-3 py-1.5 rounded-lg transition-colors border ${mode === 'ielts' ? 'text-[#0f766e] bg-emerald-50 hover:bg-emerald-100 border-emerald-100' : 'text-blue-700 bg-blue-50 hover:bg-blue-100 border-blue-100'}`}
                >
                   {prompt}
                </button>
             ))}
          </div>

          <div className={`flex items-end gap-2 bg-slate-50 border border-slate-200 rounded-2xl p-1.5 ${theme.focusRing} transition-all shadow-inner`}>
            <textarea 
              ref={textareaRef}
              value={input}
              onChange={handleTextareaInput}
              onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); handleSendMessage(); } }}
              placeholder={mode === 'ielts' ? "Dán bài viết hoặc hỏi Giám khảo..." : "Hỏi trợ lý AI..."}
              className="flex-1 min-h-[40px] max-h-[200px] bg-transparent text-[14px] text-slate-700 font-medium px-3 py-2.5 outline-none resize-none custom-scrollbar placeholder:text-slate-400 placeholder:font-normal"
              rows={1}
            />
            <button onClick={() => handleSendMessage()} disabled={!input.trim() || isTyping} className={`w-11 h-11 shrink-0 rounded-xl ${theme.btnColor} text-white flex items-center justify-center disabled:bg-slate-200 disabled:text-slate-400 transition-colors mb-0.5 shadow-sm`}>
               ➤
            </button>
          </div>
          <p className="text-[10.5px] text-center text-slate-400 mt-2 font-medium">Nhấn <kbd className="bg-slate-100 px-1 py-0.5 rounded border border-slate-200">Shift</kbd> + <kbd className="bg-slate-100 px-1 py-0.5 rounded border border-slate-200">Enter</kbd> để xuống dòng.</p>
        </div>
      </div>
    </>
  );
}