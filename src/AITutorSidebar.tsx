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
  topicImage?: string; 
  taskType?: string; // 🚀 Thêm cổng nhận taskType
}

const TUTOR_PROMPTS = ["Tóm tắt bài học.", "Giải thích khái niệm khó.", "Cho ví dụ minh họa."];

export default function AITutorSidebar({ isOpen, onClose, mode = 'tutor', courseTitle, lectureTitle, htmlContent, topicTitle, topicImage, taskType = 'task2' }: AITutorProps) {
  const [messages, setMessages] = useState<{ role: 'user' | 'ai'; text: string; isError?: boolean }[]>([]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [isExpanded, setIsExpanded] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // 🎨 BỘ CHỌN THEME TỰ ĐỘNG BIẾN HÌNH THEO MÔN HỌC
  const theme = useMemo(() => {
    if (mode === 'tutor') {
      return {
        headerBg: 'from-[#0a5482] to-[#1e88e5]',
        title: 'Trợ Lý Tony AI', subtitle: 'Gia sư đồng hành 24/7', icon: '🤖',
        userBg: 'bg-[#1e88e5]', aiBorder: 'border-slate-200', typingDot: 'bg-[#1e88e5]',
        btnColor: 'bg-[#1e88e5] hover:bg-[#1565c0]', focusRing: 'focus-within:border-[#1e88e5] focus-within:ring-blue-50', width: 'md:w-[400px]'
      };
    }
    
    switch (taskType) {
      case 'task1':
      case 'task2':
        return {
          headerBg: 'from-[#4c1d95] to-[#7c3aed]', // 🟣 IELTS: Tím
          title: `IELTS AI Assessor (${taskType.toUpperCase()})`,
          subtitle: 'Chấm điểm & Sửa lỗi chuyên sâu', icon: '🎓',
          userBg: 'bg-[#7c3aed]', aiBorder: 'border-purple-200', typingDot: 'bg-[#8b5cf6]',
          btnColor: 'bg-[#7c3aed] hover:bg-[#6d28d9]', focusRing: 'focus-within:border-[#7c3aed] focus-within:ring-purple-50', width: 'md:w-[500px]'
        };
      case 'math':
        return {
          headerBg: 'from-[#065f46] to-[#059669]', // 🟢 Math: Xanh Lá
          title: 'Math AI Tutor (IGCSE/A-Level)',
          subtitle: 'Giải chi tiết từng bước lập luận', icon: '📐',
          userBg: 'bg-[#059669]', aiBorder: 'border-emerald-200', typingDot: 'bg-[#059669]',
          btnColor: 'bg-[#059669] hover:bg-[#047857]', focusRing: 'focus-within:border-[#059669] focus-within:ring-emerald-50', width: 'md:w-[500px]'
        };
      case 'Science':
        return {
          headerBg: 'from-[#c2410c] to-[#ea580c]', // 🟠 Science: Cam
          title: 'Science AI Tutor (IGCSE/A-Level)',
          subtitle: 'Phân tích hiện tượng & Thí nghiệm', icon: '🧪',
          userBg: 'bg-[#ea580c]', aiBorder: 'border-orange-200', typingDot: 'bg-[#ea580c]',
          btnColor: 'bg-[#ea580c] hover:bg-[#c2410c]', focusRing: 'focus-within:border-[#ea580c] focus-within:ring-orange-50', width: 'md:w-[500px]'
        };
      case 'ESL':
        return {
          headerBg: 'from-[#0369a1] to-[#0284c7]', // 🔵 ESL: Xanh dương
          title: 'Cambridge IGCSE ESL Examiner',
          subtitle: 'Strict Cambridge Evaluation Protocol', icon: '📝',
          userBg: 'bg-[#0284c7]', aiBorder: 'border-sky-200', typingDot: 'bg-[#0284c7]',
          btnColor: 'bg-[#0284c7] hover:bg-[#0369a1]', focusRing: 'focus-within:border-[#0284c7] focus-within:ring-sky-50', width: 'md:w-[500px]'
        };
      default:
        return {
          headerBg: 'from-[#475569] to-[#64748b]',
          title: 'Tony AI Multi-Subject Tutor', subtitle: 'Hỗ trợ học tập chuyên sâu', icon: '✨',
          userBg: 'bg-[#64748b]', aiBorder: 'border-slate-200', typingDot: 'bg-[#64748b]',
          btnColor: 'bg-[#64748b] hover:bg-[#475569]', focusRing: 'focus-within:border-[#64748b] focus-within:ring-slate-50', width: 'md:w-[500px]'
        };
    }
  }, [mode, taskType]);

  // 🧠 BỘ GỢI Ý ĐỘNG THEO MÔN HỌC
  const dynamicPrompts = useMemo(() => {
    if (mode === 'tutor') return TUTOR_PROMPTS;
    switch (taskType) {
      case 'task1':
      case 'task2':
        return ["💡 Nhờ lập dàn ý", "📝 Chấm điểm bài viết", "🧠 Gợi ý từ vựng Band 8.0+"];
      case 'math':
        return ["📐 Gợi ý bước giải tiếp theo", "🔍 Kiểm tra lỗi sai bước làm", "💡 Tìm phương pháp giải khác"];
      case 'Science':
        return ["🧪 Giải thích định luật/hiện tượng", "📊 Phân tích bảng số liệu thí nghiệm", "📝 Hướng dẫn viết câu trả lời tự luận"];
      case 'ESL':
        return ["📝 Chấm điểm theo chuẩn Cambridge", "✍️ Sửa lỗi diễn đạt Line-by-line", "🚀 Nâng cấp lên bài mẫu Band 9"];
      default:
        return ["💡 Hướng dẫn phương pháp làm bài", "🔍 Kiểm tra đáp án"];
    }
  }, [mode, taskType]);

  const contextText = useMemo(() => {
    if (mode === 'ielts' || !htmlContent) return '';
    const doc = new DOMParser().parseFromString(htmlContent, 'text/html');
    return (doc.body.textContent || '').substring(0, 15000);
  }, [htmlContent, mode]);

  useEffect(() => { messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' }); }, [messages, isTyping, isExpanded]);

  useEffect(() => {
    if (isOpen) {
       setTimeout(() => textareaRef.current?.focus(), 300);
       setMessages([{
           role: 'ai',
           text: mode === 'ielts' 
             ? `Chào em! Thầy đã nhận được đề bài. ${topicImage ? "Thầy đã thấy hình ảnh/biểu đồ của em rồi!" : ""} Em gửi câu hỏi hoặc dán bài làm vào đây để thầy hỗ trợ nhé!` 
             : `Chào em! Thầy AI đã sẵn sàng hỗ trợ bài học **"${lectureTitle || 'này'}"**. Em cần thầy giải đáp gì không?`
       }]);
    }
  }, [isOpen, mode, topicTitle, lectureTitle, topicImage]);

  const handleSendMessage = async (suggestedText?: string) => {
    const userMsg = typeof suggestedText === 'string' ? suggestedText : input.trim();
    if (!userMsg || isTyping) return;

    setMessages(prev => [...prev, { role: 'user', text: userMsg }]);
    setInput('');
    setIsTyping(true);
    if (textareaRef.current) textareaRef.current.style.height = 'auto';

    try {
      let endpoint = 'omni-ai-grader'; // 🚀 LUÔN GỌI VÀO ÔNG TỔNG QUẢN
      let payload: any = {};

      if (mode === 'ielts') {
         payload = { 
            content: `Đề bài: ${topicTitle}\n\nNội dung từ học sinh: ${userMsg}`,
            imageUrl: topicImage,
            taskType: taskType // 🚀 GỬI NHÃN MÀ WEB BẮT ĐƯỢC CHUẨN 100%
         };
      } else {
         const systemPrompt = `Bạn là gia sư AI. Bài giảng: "${lectureTitle}". Nội dung: """${contextText}""". Hãy trả lời: "${userMsg}"`;
         payload = { prompt: systemPrompt, model: 'gemini-1.5-flash', taskType: 'tutor' };
      }

      const { data, error } = await supabase.functions.invoke(endpoint, { body: payload });
      if (error || data?.error) throw new Error("AI đang bận, em thử lại sau nhé!");

      let finalResponse = data.result || data.text || data.response;
      setMessages(prev => [...prev, { role: 'ai', text: finalResponse }]);
    } catch (error: any) {
      setMessages(prev => [...prev, { role: 'ai', text: error.message, isError: true }]);
    } finally { setIsTyping(false); }
  };

  const handleSuggestionClick = (p: string) => {
      if (p.includes('Chấm điểm')) { setInput("Nhờ thầy chấm giúp bài làm sau:\n\n[Dán bài vào đây]"); setTimeout(() => textareaRef.current?.focus(), 100); }
      else handleSendMessage(p);
  };

  const formatMarkdown = (text: string) => {
    if (!text) return '';
    return text.replace(/\*\*(.*?)\*\*/g, '<b>$1</b>').replace(/\n/g, '<br/>');
  };

  return (
    <>
      {isOpen && <div className="fixed inset-0 bg-slate-900/40 z-[90] md:hidden" onClick={() => { onClose(); setIsExpanded(false); }} />}
      <div className={`fixed top-0 md:top-[60px] bottom-0 right-0 w-full ${isExpanded ? 'md:w-[800px]' : theme.width} bg-[#f8fafc] shadow-2xl z-[100] flex flex-col transition-all duration-300 border-l border-slate-200 ${isOpen ? 'translate-x-0' : 'translate-x-full'}`}>
        <div className={`h-16 bg-gradient-to-r ${theme.headerBg} text-white flex items-center justify-between px-5 shrink-0 shadow-sm z-10`}>
          <div className="flex items-center gap-3">
             <div className="w-10 h-10 bg-white/10 rounded-lg flex items-center justify-center text-lg">{theme.icon}</div>
             <div><h3 className="font-bold text-[15px]">{theme.title}</h3><p className="text-[11px] text-white/80 uppercase">{theme.subtitle}</p></div>
          </div>
          <div className="flex items-center gap-1">
             <button onClick={() => setIsExpanded(!isExpanded)} className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/20 text-white">
                {isExpanded ? "⛶" : "⬜"}
             </button>
             <button onClick={() => { onClose(); setIsExpanded(false); }} className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/20 text-white">✕</button>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto p-5 space-y-5 custom-scrollbar bg-slate-50/50">
          
          {mode === 'ielts' && topicImage && (
              <div className="mb-4 animate-in fade-in slide-in-from-top-2">
                  <div className="text-[11px] font-black text-slate-400 uppercase mb-2 tracking-widest">Đề bài hình ảnh:</div>
                  <div className="rounded-xl overflow-hidden border-4 border-white shadow-lg bg-white">
                    <img src={topicImage} alt="Task đề bài" className="w-full h-auto object-contain max-h-[300px]" />
                  </div>
              </div>
          )}

          {messages.map((msg, idx) => (
            <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-in fade-in`}>
               <div className={`max-w-[88%] p-3.5 text-[15px] shadow-sm ${msg.role === 'user' ? `${theme.userBg} text-white rounded-2xl rounded-tr-sm` : `bg-white border ${theme.aiBorder} text-slate-700 rounded-2xl rounded-tl-sm`}`}>
                  {msg.role === 'user' ? msg.text : <div dangerouslySetInnerHTML={{ __html: formatMarkdown(msg.text) }} />}
               </div>
            </div>
          ))}
          {isTyping && (
             <div className="flex justify-start"><div className="bg-white border p-4 rounded-2xl flex items-center gap-1.5 shadow-sm"><span className="w-2 h-2 bg-slate-300 rounded-full animate-bounce"></span><span className="w-2 h-2 bg-slate-300 rounded-full animate-bounce delay-100"></span><span className="w-2 h-2 bg-slate-300 rounded-full animate-bounce delay-200"></span></div></div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="p-4 bg-white border-t border-slate-200 shrink-0 z-10">
          <div className="flex flex-col gap-2 mb-4 max-w-sm mx-auto">
             {/* 🚀 ĐÃ THAY BẰNG MẢNG GỢI Ý ĐỘNG THEO MÔN */}
             {dynamicPrompts.map((p, i) => (
                <button key={i} onClick={() => handleSuggestionClick(p)} className="bg-white border border-slate-200 text-slate-600 text-[12px] font-bold py-2 px-4 rounded-xl text-left hover:bg-slate-50 transition-colors shadow-sm flex justify-between group">
                  <span>{p}</span><span className="text-slate-300 group-hover:text-blue-500">→</span>
                </button>
             ))}
          </div>
          <div className={`flex items-end gap-2 bg-slate-50 border border-slate-200 rounded-2xl p-1.5 ${theme.focusRing} transition-all`}>
            <textarea ref={textareaRef} value={input} onChange={(e) => { setInput(e.target.value); e.target.style.height = 'auto'; e.target.style.height = `${e.target.scrollHeight}px`; }} onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); handleSendMessage(); } }} placeholder="Hỏi về đề bài này..." className="flex-1 min-h-[40px] max-h-[150px] bg-transparent text-[14px] text-slate-700 font-medium px-3 py-2.5 outline-none resize-none" rows={1} />
            <button onClick={() => handleSendMessage()} disabled={!input.trim() || isTyping} className={`w-10 h-10 shrink-0 rounded-xl ${theme.btnColor} text-white flex items-center justify-center transition-colors shadow-sm`}>➤</button>
          </div>
        </div>
      </div>
    </>
  );
}