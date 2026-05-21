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
  taskType?: string; 
}

const TUTOR_PROMPTS = ["Tóm tắt bài học.", "Giải thích khái niệm khó.", "Cho ví dụ minh họa."];

export default function AITutorSidebar({ 
  isOpen, 
  onClose, 
  mode = 'tutor', 
  courseTitle, 
  lectureTitle, 
  htmlContent, 
  topicTitle, 
  topicImage, 
  taskType = 'task2' 
}: AITutorProps) {
  
  const [messages, setMessages] = useState<{ role: 'user' | 'ai'; text: string; isError?: boolean }[]>([]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [isExpanded, setIsExpanded] = useState(false);
  const [isMinimized, setIsMinimized] = useState(false);
  
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // 🚀 ĐÓN LỆNH QUÉT SẠCH LỊCH SỬ CHAT TỪ CÁC BÀI GIẢNG
  useEffect(() => {
    const handleClearChat = () => {
        setMessages([]);
    };
    window.addEventListener('tony-clear-chat', handleClearChat);
    return () => {
        window.removeEventListener('tony-clear-chat', handleClearChat);
    };
  }, []);

  const theme = useMemo(() => {
    if (mode === 'tutor') {
      return {
        headerBg: 'from-[#0a5482] to-[#1e88e5]',
        title: 'Trợ Lý Tony AI', 
        subtitle: 'Gia sư đồng hành 24/7', 
        icon: '🤖',
        userBg: 'bg-[#1e88e5]', 
        aiBorder: 'border-slate-200', 
        typingDot: 'bg-[#1e88e5]',
        btnColor: 'bg-[#1e88e5] hover:bg-[#1565c0]', 
        focusRing: 'focus-within:border-[#1e88e5] focus-within:ring-blue-50', 
        width: 'md:w-[400px]'
      };
    }
    
    switch (taskType) {
      case 'task1':
      case 'task2':
        return {
          headerBg: 'from-[#4c1d95] to-[#7c3aed]', 
          title: `IELTS AI Assessor (${taskType.toUpperCase()})`,
          subtitle: 'Chấm điểm & Sửa lỗi chuyên sâu', 
          icon: '🎓',
          userBg: 'bg-[#7c3aed]', 
          aiBorder: 'border-purple-200', 
          typingDot: 'bg-[#8b5cf6]',
          btnColor: 'bg-[#7c3aed] hover:bg-[#6d28d9]', 
          focusRing: 'focus-within:border-[#7c3aed] focus-within:ring-purple-50', 
          width: 'md:w-[500px]'
        };
      case 'math':
        return {
          headerBg: 'from-[#065f46] to-[#059669]', 
          title: 'Math AI Tutor (IGCSE/A-Level)',
          subtitle: 'Giải chi tiết từng bước lập luận', 
          icon: '📐',
          userBg: 'bg-[#059669]', 
          aiBorder: 'border-emerald-200', 
          typingDot: 'bg-[#059669]',
          btnColor: 'bg-[#059669] hover:bg-[#047857]', 
          focusRing: 'focus-within:border-[#059669] focus-within:ring-emerald-50', 
          width: 'md:w-[500px]'
        };
      case 'Science':
        return {
          headerBg: 'from-[#c2410c] to-[#ea580c]', 
          title: 'Science AI Tutor (IGCSE/A-Level)',
          subtitle: 'Phân tích hiện tượng & Thí nghiệm', 
          icon: '🧪',
          userBg: 'bg-[#ea580c]', 
          aiBorder: 'border-orange-200', 
          typingDot: 'bg-[#ea580c]',
          btnColor: 'bg-[#ea580c] hover:bg-[#c2410c]', 
          focusRing: 'focus-within:border-[#ea580c] focus-within:ring-orange-50', 
          width: 'md:w-[500px]'
        };
      case 'ESL':
        return {
          headerBg: 'from-[#0369a1] to-[#0284c7]', 
          title: 'Cambridge IGCSE ESL Examiner',
          subtitle: 'Strict Cambridge Evaluation Protocol', 
          icon: '📝',
          userBg: 'bg-[#0284c7]', 
          aiBorder: 'border-sky-200', 
          typingDot: 'bg-[#0284c7]',
          btnColor: 'bg-[#0284c7] hover:bg-[#0369a1]', 
          focusRing: 'focus-within:border-[#0284c7] focus-within:ring-sky-50', 
          width: 'md:w-[500px]'
        };
      case 'speaking':
        return {
          headerBg: 'from-[#1e3a8a] to-[#3b82f6]', 
          title: 'IELTS Speaking Assistant',
          subtitle: 'Lên ý tưởng & Bẻ lái Part 2', 
          icon: '🎙️',
          userBg: 'bg-[#3b82f6]', 
          aiBorder: 'border-blue-200', 
          typingDot: 'bg-[#3b82f6]',
          btnColor: 'bg-[#3b82f6] hover:bg-[#1d4ed8]', 
          focusRing: 'focus-within:border-[#3b82f6] focus-within:ring-blue-50', 
          width: 'md:w-[500px]'
        };
      case 'reading':
        return {
          headerBg: 'from-[#065f46] to-[#10b981]', 
          title: 'IELTS Reading Tutor',
          subtitle: 'Giải thích đáp án chi tiết', 
          icon: '📖',
          userBg: 'bg-[#10b981]', 
          aiBorder: 'border-emerald-200', 
          typingDot: 'bg-[#10b981]',
          btnColor: 'bg-[#10b981] hover:bg-[#059669]', 
          focusRing: 'focus-within:border-[#10b981] focus-within:ring-emerald-50', 
          width: 'md:w-[500px]'
        };
      default:
        return {
          headerBg: 'from-[#475569] to-[#64748b]',
          title: 'Tony AI Multi-Subject Tutor', 
          subtitle: 'Hỗ trợ học tập chuyên sâu', 
          icon: '✨',
          userBg: 'bg-[#64748b]', 
          aiBorder: 'border-slate-200', 
          typingDot: 'bg-[#64748b]',
          btnColor: 'bg-[#64748b] hover:bg-[#475569]', 
          focusRing: 'focus-within:border-[#64748b] focus-within:ring-slate-50', 
          width: 'md:w-[500px]'
        };
    }
  }, [mode, taskType]);

  const dynamicPrompts = useMemo(() => {
    if (mode === 'tutor') {
        return TUTOR_PROMPTS;
    }
    
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
      case 'speaking':
        return ["💡 Tư vấn kịch bản (Lego)", "🧠 Gợi ý từ vựng Band 8+", "✍️ Viết câu Mở bài (Hook) ấn tượng"];
      case 'reading':
        return ["💡 Tại sao đáp án này đúng?", "🔍 Tìm dẫn chứng trong bài đọc", "🧠 Dịch đoạn văn chứa đáp án"];
      default:
        return ["💡 Hướng dẫn phương pháp làm bài", "🔍 Kiểm tra đáp án"];
    }
  }, [mode, taskType]);

  const contextText = useMemo(() => {
    if (mode === 'ielts' || !htmlContent) {
        return '';
    }
    const doc = new DOMParser().parseFromString(htmlContent, 'text/html');
    return (doc.body.textContent || '').substring(0, 15000);
  }, [htmlContent, mode]);

  useEffect(() => { 
      if (messagesEndRef.current && !isMinimized) {
          messagesEndRef.current.scrollIntoView({ behavior: 'smooth' }); 
      }
  }, [messages, isTyping, isExpanded, isMinimized]);

  useEffect(() => {
    if (isOpen) {
       setIsMinimized(false);
       
       setTimeout(() => {
           if (textareaRef.current) {
               textareaRef.current.focus();
           }
       }, 300);
       
       // Chỉ tạo lời chào mới nếu chưa có lịch sử chat
       if (messages.length === 0) {
           let welcomeText = "";
           
           if (mode === 'ielts') {
              if (taskType === 'reading') {
                 welcomeText = `Chào em! Thầy đã nhận được yêu cầu giải thích:\n\n${topicTitle}\n\nEm muốn hỏi thêm thầy điều gì?`;
              } else {
                 welcomeText = `Chào em! Thầy đã nhận được yêu cầu phân tích.\n\n`;
                 if (topicTitle) {
                     welcomeText += `**📝 Đề bài:** "${topicTitle}"\n\n`;
                 }
                 if (topicImage) {
                     welcomeText += `**(📸 Đã nhận kèm hình ảnh/biểu đồ)**\n\n`;
                 }
                 
                 if (taskType === 'speaking') {
                     welcomeText += `Em cần thầy tư vấn Kịch bản Lego, gợi ý từ vựng hay viết câu mở bài (Hook) nào?`;
                 } else if (taskType === 'task1' || taskType === 'task2') {
                     welcomeText += `Em cần thầy lập dàn ý, gợi ý từ vựng hay chấm điểm bài làm của em?`;
                 } else {
                     welcomeText += `Em gửi câu hỏi hoặc dán nội dung vào đây để thầy hỗ trợ nhé!`;
                 }
              }
           } else {
              welcomeText = `Chào em! Thầy AI đã sẵn sàng hỗ trợ bài học **"${lectureTitle || 'này'}"**. Em cần thầy giải đáp gì không?`;
           }

           setMessages([{
               role: 'ai',
               text: welcomeText
           }]);
       }
    }
  }, [isOpen, mode, topicTitle, lectureTitle, topicImage, taskType]);

  const handleCallTutor = () => {
      const safeHtml = htmlContent ? htmlContent.replace(/<[^>]+>/g, '').slice(0, 2000) : 'Không có dữ liệu văn bản';
      const safeTitle = lectureTitle || 'Bài giảng English';
      
      const tutorContext = {
          overall: "N/A",
          transcript: `Học sinh đang học bài: "${safeTitle}". \nNội dung bài học: "${safeHtml}".`,
          feedback: "Bạn là gia sư đang dạy bài giảng này. Hãy chủ động chào học sinh, nhắc tên bài học và hỏi xem học sinh không hiểu phần nào trong nội dung trên để bạn giải thích bằng giọng nói ân cần."
      };
      
      sessionStorage.setItem('tony_live_mode', 'TUTOR');
      sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
      sessionStorage.setItem('tony_auto_start', 'true');
      
      setIsMinimized(true);
      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
  };

  const handleSendMessage = async (suggestedText?: string) => {
    const userMsg = typeof suggestedText === 'string' ? suggestedText : input.trim();
    
    if (!userMsg || isTyping) {
        return;
    }

    setMessages(prev => [...prev, { role: 'user', text: userMsg }]);
    setInput('');
    setIsTyping(true);
    
    if (textareaRef.current) {
        textareaRef.current.style.height = 'auto';
    }

    try {
      let endpoint = 'omni-ai-grader'; 
      let payload: any = {};

      if (mode === 'ielts') {
         if (taskType === 'reading') {
            const systemPrompt = `Bạn là gia sư IELTS Reading xuất sắc.
            Dưới đây là nội dung BÀI ĐỌC (Ẩn khỏi màn hình người dùng):
            """
            ${contextText}
            """
            
            Dưới đây là nội dung CÂU HỎI VÀ ĐÁP ÁN:
            """
            ${topicTitle}
            """
            
            Dựa vào 2 thông tin trên, hãy trả lời câu hỏi sau của học sinh bằng tiếng Việt một cách chi tiết, dễ hiểu, phân tích lý do đúng/sai và BẮT BUỘC trích dẫn câu văn/đoạn văn chứa bằng chứng trong BÀI ĐỌC:
            "${userMsg}"`;
            
            payload = { 
                prompt: systemPrompt, 
                taskType: 'tutor' 
            }; 
         } else {
             payload = { 
                content: `Đề bài: ${topicTitle}\n\nNội dung từ học sinh: ${userMsg}`,
                imageUrl: topicImage,
                taskType: taskType 
             };
         }
      } else {
         const systemPrompt = `Bạn là gia sư AI. Bài giảng: "${lectureTitle}". Nội dung: """${contextText}""". Hãy trả lời: "${userMsg}"`;
         payload = { 
             prompt: systemPrompt, 
             taskType: 'tutor' 
         }; 
      }

      const { data, error } = await supabase.functions.invoke(endpoint, { body: payload });
      
      if (error || data?.error) {
          throw new Error("AI đang bận, em thử lại sau nhé!");
      }

      let finalResponse = data.result || data.text || data.response;
      setMessages(prev => [...prev, { role: 'ai', text: finalResponse }]);
      
    } catch (error: any) {
      setMessages(prev => [...prev, { role: 'ai', text: error.message, isError: true }]);
    } finally { 
        setIsTyping(false); 
    }
  };

  const handleSuggestionClick = (p: string) => {
      if (p.includes('Chấm điểm')) { 
          setInput("Nhờ thầy chấm giúp bài làm sau:\n\n[Dán bài vào đây]"); 
          setTimeout(() => {
              if (textareaRef.current) {
                  textareaRef.current.focus();
              }
          }, 100); 
      } else {
          handleSendMessage(p);
      }
  };

  const formatMarkdown = (text: string) => {
    if (!text) return '';
    return text.replace(/\*\*(.*?)\*\*/g, '<b>$1</b>').replace(/\n/g, '<br/>');
  };

  if (!isOpen) return null;

  if (isMinimized) {
      return (
          <button 
              onClick={() => setIsMinimized(false)}
              className={`fixed bottom-[120px] right-6 z-[10000] w-14 h-14 rounded-full bg-gradient-to-r ${theme.headerBg} text-white shadow-2xl flex items-center justify-center text-2xl hover:scale-110 active:scale-95 transition-all duration-200 animate-in zoom-in group border-2 border-white`}
              title="Mở lại khung Chat AI"
          >
              <span className="group-hover:hidden">{theme.icon}</span>
              <span className="hidden group-hover:block text-xl">💬</span>
              
              <span className="absolute top-0 right-0 w-3.5 h-3.5 bg-red-500 border-2 border-white rounded-full animate-pulse"></span>
          </button>
      );
  }

  return (
    <>
      {isOpen && !isMinimized && (
          <div 
              className="fixed inset-0 bg-slate-900/40 z-[90] md:hidden" 
              onClick={() => { 
                  setIsMinimized(true); 
                  setIsExpanded(false); 
              }} 
          />
      )}
      
      <div className={`fixed top-0 md:top-[60px] bottom-0 right-0 w-full ${isExpanded ? 'md:w-[800px]' : theme.width} bg-[#f8fafc] shadow-2xl z-[100] flex flex-col transition-all duration-300 border-l border-slate-200 ${isOpen && !isMinimized ? 'translate-x-0' : 'translate-x-full'}`}>
        
        <div className={`h-16 bg-gradient-to-r ${theme.headerBg} text-white flex items-center justify-between px-5 shrink-0 shadow-sm z-10`}>
          <div className="flex items-center gap-3">
             <div className="w-10 h-10 bg-white/10 rounded-lg flex items-center justify-center text-lg">
                 {theme.icon}
             </div>
             <div>
                 <h3 className="font-bold text-[15px]">{theme.title}</h3>
                 <p className="text-[11px] text-white/80 uppercase">{theme.subtitle}</p>
             </div>
          </div>
          
          <div className="flex items-center gap-1">
             <button 
                 onClick={() => setIsExpanded(!isExpanded)} 
                 className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/20 text-white"
                 title="Phóng to"
             >
                {isExpanded ? "⛶" : "⬜"}
             </button>
             
             <button 
                 onClick={() => setIsMinimized(true)} 
                 className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/20 text-white font-bold pb-2"
                 title="Thu nhỏ Chat"
             >
                _
             </button>
             
             <button 
                 onClick={handleCallTutor}
                 className="bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-1.5 rounded-lg text-[12px] font-bold transition-all flex items-center gap-1.5 shadow-md active:scale-95 ml-2 mr-2"
                 title="Gọi điện trực tiếp"
             >
                 📞 Gọi Gia Sư
             </button>
             
             <button 
                 onClick={() => { 
                     if(window.confirm('Đóng cửa sổ này sẽ xóa lịch sử trò chuyện. Bạn có muốn thu nhỏ lại thay vì đóng hẳn không?')) {
                         setMessages([]); // Xóa lịch sử khi đóng hẳn
                         onClose(); 
                         setIsExpanded(false); 
                     } else {
                         setIsMinimized(true);
                     }
                 }} 
                 className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-red-500 transition-colors text-white text-lg font-bold"
                 title="Đóng hẳn"
             >
                 ✕
             </button>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto p-5 space-y-5 custom-scrollbar bg-slate-50/50">
          
          {mode === 'ielts' && topicImage && (
              <div className="mb-4 animate-in fade-in slide-in-from-top-2">
                  <div className="text-[11px] font-black text-slate-400 uppercase mb-2 tracking-widest">
                      Đề bài hình ảnh:
                  </div>
                  <div className="rounded-xl overflow-hidden border-4 border-white shadow-lg bg-white">
                    <img src={topicImage} alt="Task đề bài" className="w-full h-auto object-contain max-h-[300px]" />
                  </div>
              </div>
          )}

          {messages.map((msg, idx) => (
            <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-in fade-in`}>
               <div className={`max-w-[88%] p-3.5 text-[15px] shadow-sm ${msg.role === 'user' ? `${theme.userBg} text-white rounded-2xl rounded-tr-sm` : `bg-white border ${theme.aiBorder} text-slate-700 rounded-2xl rounded-tl-sm`}`}>
                  {msg.role === 'user' ? (
                      msg.text 
                  ) : (
                      <div dangerouslySetInnerHTML={{ __html: formatMarkdown(msg.text) }} />
                  )}
               </div>
            </div>
          ))}
          
          {isTyping && (
             <div className="flex justify-start">
                 <div className="bg-white border p-4 rounded-2xl flex items-center gap-1.5 shadow-sm">
                     <span className="w-2 h-2 bg-slate-300 rounded-full animate-bounce"></span>
                     <span className="w-2 h-2 bg-slate-300 rounded-full animate-bounce delay-100"></span>
                     <span className="w-2 h-2 bg-slate-300 rounded-full animate-bounce delay-200"></span>
                 </div>
             </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="p-4 bg-white border-t border-slate-200 shrink-0 z-10">
          <div className="flex flex-col gap-2 mb-4 max-w-sm mx-auto">
             {dynamicPrompts.map((p, i) => (
                <button 
                    key={i} 
                    onClick={() => handleSuggestionClick(p)} 
                    className="bg-white border border-slate-200 text-slate-600 text-[12px] font-bold py-2 px-4 rounded-xl text-left hover:bg-slate-50 transition-colors shadow-sm flex justify-between group"
                >
                  <span>{p}</span>
                  <span className="text-slate-300 group-hover:text-blue-500">→</span>
                </button>
             ))}
          </div>
          
          <div className={`flex items-end gap-2 bg-slate-50 border border-slate-200 rounded-2xl p-1.5 ${theme.focusRing} transition-all`}>
            <textarea 
                ref={textareaRef} 
                value={input} 
                onChange={(e) => { 
                    setInput(e.target.value); 
                    e.target.style.height = 'auto'; 
                    e.target.style.height = `${e.target.scrollHeight}px`; 
                }} 
                onKeyDown={(e) => { 
                    if (e.key === 'Enter' && !e.shiftKey) { 
                        e.preventDefault(); 
                        handleSendMessage(); 
                    } 
                }} 
                placeholder="Hỏi về đề bài này..." 
                className="flex-1 min-h-[40px] max-h-[150px] bg-transparent text-[14px] text-slate-700 font-medium px-3 py-2.5 outline-none resize-none" 
                rows={1} 
            />
            <button 
                onClick={() => handleSendMessage()} 
                disabled={!input.trim() || isTyping} 
                className={`w-10 h-10 shrink-0 rounded-xl ${theme.btnColor} text-white flex items-center justify-center transition-colors shadow-sm`}
            >
               <svg xmlns="http://www.w3.org/2000/svg" className="w-6 h-6 rotate-90" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                   <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
               </svg>
            </button>
          </div>
        </div>
        
      </div>
    </>
  );
}