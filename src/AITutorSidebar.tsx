import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';

interface AITutorProps {
  isOpen: boolean;
  onClose: () => void;
  mode?: 'tutor' | 'ielts' | 'parent_mode'; 
  courseTitle?: string;
  lectureTitle?: string;
  htmlContent?: string;
  topicTitle?: string; 
  topicImage?: string; 
  taskType?: string; 
  isCallActive?: boolean;
}

const TUTOR_PROMPTS = [
  "Tóm tắt bài học", 
  "Giải thích khái niệm khó", 
  "Cho ví dụ minh họa"
];

export default function AITutorSidebar({ 
  isOpen, 
  onClose, 
  mode = 'tutor', 
  courseTitle, 
  lectureTitle, 
  htmlContent, 
  topicTitle, 
  topicImage, 
  taskType = 'task2',
  isCallActive = false
}: AITutorProps) {
  
  const [messages, setMessages] = useState<{ role: 'user' | 'ai'; text: string; isError?: boolean }[]>([]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [isExpanded, setIsExpanded] = useState(false);
  const [isMinimized, setIsMinimized] = useState(false);
  
  const [attachedImage, setAttachedImage] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    const isBubbleShowing = isOpen && isMinimized;
    window.dispatchEvent(new CustomEvent('tony-chat-bubble-state', { detail: isBubbleShowing }));
    
    return () => {
        window.dispatchEvent(new CustomEvent('tony-chat-bubble-state', { detail: false }));
    };
  }, [isOpen, isMinimized]);

  useEffect(() => {
    const handleClearChat = () => {
        setMessages([]);
    };
    window.addEventListener('tony-clear-chat', handleClearChat);
    
    return () => {
        window.removeEventListener('tony-clear-chat', handleClearChat);
    };
  }, []);

  // 🚀 HELPER: Tạo welcome message dựa trên context hiện tại
  const generateWelcome = () => {
    let welcomeText = "";
    if (mode === 'parent_mode') {
      const studentName = sessionStorage.getItem('tony_parent_target_student') || 'học sinh';
      welcomeText = `Dạ chào anh/chị! Tôi là Trợ lý AI chủ nhiệm của bé **${studentName}**.\n\nHệ thống đã tổng hợp xong dữ liệu học tập của cháu trong 14 ngày qua. Anh/chị cần xem báo cáo tổng quan hay có câu hỏi cụ thể nào về tình hình của cháu không ạ?`;
    } else if (mode === 'ielts') {
      if (taskType === 'reading') {
        welcomeText = `Chào em! Thầy đã nhận được yêu cầu giải thích:\n\n**${topicTitle}**\n\nEm muốn hỏi thêm thầy điều gì?`;
      } else {
        welcomeText = `Chào em! Thầy đã nhận được yêu cầu phân tích.\n\n`;
        if (topicTitle) welcomeText += `**📝 Đề bài:** "${topicTitle}"\n\n`;
        if (topicImage) welcomeText += `*(📸 Đã nhận kèm hình ảnh/biểu đồ)*\n\n`;
        if (taskType === 'speaking') welcomeText += `Em cần thầy tư vấn Kịch bản Lego, gợi ý từ vựng hay viết câu mở bài (Hook) nào?`;
        else if (taskType === 'task1' || taskType === 'task2') welcomeText += `Em cần thầy lập dàn ý, gợi ý từ vựng hay chấm điểm bài làm của em?`;
        else welcomeText += `Em gửi câu hỏi hoặc dán nội dung vào đây để thầy hỗ trợ nhé!`;
      }
    } else {
      welcomeText = `Chào em! Thầy AI đã sẵn sàng hỗ trợ bài học **"${lectureTitle || 'này'}"**. Em có thể chat hỏi bài hoặc **Paste (Ctrl+V) / Tải ảnh lên** để thầy giải đáp nhé!`;
    }
    return [{ role: 'ai' as const, text: welcomeText }];
  };

  // 🚀 AUTO-RESET: Xóa chat cũ khi user chuyển sang câu hỏi/bài giảng khác
  const contextKey = `${topicTitle || ''}|${lectureTitle || ''}`;
  const prevContextRef = useRef(contextKey);
  useEffect(() => {
    const newKey = `${topicTitle || ''}|${lectureTitle || ''}`;
    if (isOpen && newKey !== prevContextRef.current && prevContextRef.current !== '|') {
      // Đặt welcome message mới NGAY LẬP (không phụ thuộc effect khác)
      setMessages(generateWelcome());
    }
    prevContextRef.current = newKey;
  }, [topicTitle, lectureTitle, isOpen]);

  const theme = useMemo(() => {
    if (mode === 'parent_mode') {
      return {
        headerBg: 'from-[#f59e0b] to-[#ea580c]', 
        title: 'Trợ lý Phụ huynh', 
        subtitle: 'Báo cáo học tập AI', 
        icon: '👨‍👩‍👧‍👦',
        userBg: 'bg-gradient-to-br from-[#f59e0b] to-[#ea580c]', 
        aiBorder: 'border-orange-100', 
        aiBg: 'bg-white',
        btnColor: 'bg-[#f59e0b] hover:bg-[#ea580c]', 
        focusRing: 'focus-within:border-[#f59e0b] focus-within:ring-4 focus-within:ring-[#f59e0b]/10', 
        width: 'md:w-[450px]'
      };
    }

    if (mode === 'tutor') {
      return {
        headerBg: 'from-[#0ea5e9] to-[#0284c7]',
        title: 'Tony AI Tutor', 
        subtitle: 'Gia sư đồng hành 24/7', 
        icon: '🤖',
        userBg: 'bg-gradient-to-br from-[#0ea5e9] to-[#0284c7]', 
        aiBorder: 'border-slate-100', 
        aiBg: 'bg-white',
        btnColor: 'bg-[#0ea5e9] hover:bg-[#0284c7]', 
        focusRing: 'focus-within:border-[#0ea5e9] focus-within:ring-4 focus-within:ring-[#0ea5e9]/10', 
        width: 'md:w-[420px]'
      };
    }
    
    switch (taskType) {
      case 'task1':
      case 'task2':
        return {
          headerBg: 'from-[#8b5cf6] to-[#6d28d9]', 
          title: `IELTS Assessor (${taskType.toUpperCase()})`,
          subtitle: 'Chấm điểm & Sửa lỗi chuyên sâu', 
          icon: '🎓',
          userBg: 'bg-gradient-to-br from-[#8b5cf6] to-[#6d28d9]', 
          aiBorder: 'border-purple-100', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#8b5cf6] hover:bg-[#7c3aed]', 
          focusRing: 'focus-within:border-[#8b5cf6] focus-within:ring-4 focus-within:ring-[#8b5cf6]/10', 
          width: 'md:w-[500px]'
        };
      case 'math':
        return {
          headerBg: 'from-[#10b981] to-[#059669]', 
          title: 'Math AI Tutor',
          subtitle: 'Giải chi tiết từng bước lập luận', 
          icon: '📐',
          userBg: 'bg-gradient-to-br from-[#10b981] to-[#059669]', 
          aiBorder: 'border-emerald-100', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#10b981] hover:bg-[#059669]', 
          focusRing: 'focus-within:border-[#10b981] focus-within:ring-4 focus-within:ring-[#10b981]/10', 
          width: 'md:w-[500px]'
        };
      case 'Science':
        return {
          headerBg: 'from-[#f97316] to-[#ea580c]', 
          title: 'Science AI Tutor',
          subtitle: 'Phân tích hiện tượng & Thí nghiệm', 
          icon: '🧪',
          userBg: 'bg-gradient-to-br from-[#f97316] to-[#ea580c]', 
          aiBorder: 'border-orange-100', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#f97316] hover:bg-[#ea580c]', 
          focusRing: 'focus-within:border-[#f97316] focus-within:ring-4 focus-within:ring-[#f97316]/10', 
          width: 'md:w-[500px]'
        };
      case 'ESL':
        return {
          headerBg: 'from-[#0284c7] to-[#0369a1]', 
          title: 'Cambridge IGCSE ESL',
          subtitle: 'Strict Cambridge Evaluation Protocol', 
          icon: '📝',
          userBg: 'bg-gradient-to-br from-[#0284c7] to-[#0369a1]', 
          aiBorder: 'border-sky-100', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#0284c7] hover:bg-[#0369a1]', 
          focusRing: 'focus-within:border-[#0284c7] focus-within:ring-4 focus-within:ring-[#0284c7]/10', 
          width: 'md:w-[500px]'
        };
      case 'speaking':
        return {
          headerBg: 'from-[#3b82f6] to-[#2563eb]', 
          title: 'Speaking Assistant',
          subtitle: 'Lên ý tưởng & Bẻ lái Part 2', 
          icon: '🎙️',
          userBg: 'bg-gradient-to-br from-[#3b82f6] to-[#2563eb]', 
          aiBorder: 'border-blue-100', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#3b82f6] hover:bg-[#2563eb]', 
          focusRing: 'focus-within:border-[#3b82f6] focus-within:ring-4 focus-within:ring-[#3b82f6]/10', 
          width: 'md:w-[500px]'
        };
      case 'reading':
        return {
          headerBg: 'from-[#14b8a6] to-[#0d9488]', 
          title: 'IELTS Reading Tutor',
          subtitle: 'Giải thích đáp án chi tiết', 
          icon: '📖',
          userBg: 'bg-gradient-to-br from-[#14b8a6] to-[#0d9488]', 
          aiBorder: 'border-teal-100', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#14b8a6] hover:bg-[#0d9488]', 
          focusRing: 'focus-within:border-[#14b8a6] focus-within:ring-4 focus-within:ring-[#14b8a6]/10', 
          width: 'md:w-[500px]'
        };
      default:
        return {
          headerBg: 'from-[#64748b] to-[#475569]',
          title: 'Tony AI Multi-Tutor', 
          subtitle: 'Hỗ trợ học tập chuyên sâu', 
          icon: '✨',
          userBg: 'bg-gradient-to-br from-[#64748b] to-[#475569]', 
          aiBorder: 'border-slate-100', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#64748b] hover:bg-[#475569]', 
          focusRing: 'focus-within:border-[#64748b] focus-within:ring-4 focus-within:ring-[#64748b]/10', 
          width: 'md:w-[500px]'
        };
    }
  }, [mode, taskType]);

  const dynamicPrompts = useMemo(() => {
    if (mode === 'parent_mode') {
        return ["📊 Tình hình học tập tuần qua", "📈 Cháu có tiến bộ không?", "💡 Có cần nhắc nhở cháu môn gì?"];
    }

    if (mode === 'tutor') {
        return TUTOR_PROMPTS;
    }
    
    switch (taskType) {
      case 'task1':
      case 'task2':
        return ["💡 Nhờ lập dàn ý", "📝 Chấm điểm bài viết", "🧠 Gợi ý từ vựng Band 8.0+"];
      case 'math':
        return ["📐 Gợi ý bước giải tiếp theo", "🔍 Kiểm tra lỗi sai", "💡 Tìm phương pháp khác"];
      case 'Science':
        return ["🧪 Giải thích hiện tượng", "📊 Phân tích số liệu", "📝 Hướng dẫn tự luận"];
      case 'ESL':
        return ["📝 Chấm điểm Cambridge", "✍️ Sửa lỗi diễn đạt", "🚀 Nâng cấp Band 9"];
      case 'speaking':
        return ["💡 Tư vấn kịch bản (Lego)", "🧠 Gợi ý từ vựng Band 8+", "✍️ Viết câu Mở bài ấn tượng"];
      case 'reading':
        return ["💡 Tại sao đáp án này đúng?", "🔍 Tìm dẫn chứng", "🧠 Dịch đoạn văn"];
      default:
        return ["💡 Hướng dẫn phương pháp", "🔍 Kiểm tra đáp án"];
    }
  }, [mode, taskType]);

  const contextText = useMemo(() => {
    if (mode === 'ielts' || mode === 'parent_mode' || !htmlContent) {
        return '';
    }
    const doc = new DOMParser().parseFromString(htmlContent, 'text/html');
    return (doc.body.textContent || '').substring(0, 15000);
  }, [htmlContent, mode]);

  useEffect(() => { 
      if (messagesEndRef.current && !isMinimized) {
          messagesEndRef.current.scrollIntoView({ behavior: 'smooth' }); 
      }
  }, [messages, isTyping, isExpanded, isMinimized, attachedImage]);

  useEffect(() => {
    if (isOpen) {
       setIsMinimized(false);
       
       setTimeout(() => {
           if (textareaRef.current) {
               textareaRef.current.focus();
           }
       }, 300);
       
       if (messages.length === 0) {
           setMessages(generateWelcome());
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
      
      setIsMinimized(true);
      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
  };

  const handlePaste = (e: React.ClipboardEvent) => {
      if (mode === 'parent_mode') return; 
      
      const items = e.clipboardData.items;
      for (let i = 0; i < items.length; i++) {
          if (items[i].type.indexOf('image') !== -1) {
              const file = items[i].getAsFile();
              if (file) {
                  processImageFile(file);
              }
              e.preventDefault();
              break;
          }
      }
  };

  // MÁY ÉP ẢNH TỰ ĐỘNG THU NHỎ XUỐNG CÒN 800px VÀ NÉN 60%
  const processImageFile = (file: File) => {
      const reader = new FileReader();
      reader.onload = (e) => {
          const img = new Image();
          img.onload = () => {
              const canvas = document.createElement('canvas');
              const MAX_WIDTH = 800; 
              const MAX_HEIGHT = 800;
              let width = img.width;
              let height = img.height;

              if (width > height) {
                  if (width > MAX_WIDTH) {
                      height *= MAX_WIDTH / width;
                      width = MAX_WIDTH;
                  }
              } else {
                  if (height > MAX_HEIGHT) {
                      width *= MAX_HEIGHT / height;
                      height = MAX_HEIGHT;
                  }
              }
              
              canvas.width = width;
              canvas.height = height;
              const ctx = canvas.getContext('2d');
              
              if (ctx) {
                  ctx.fillStyle = '#ffffff';
                  ctx.fillRect(0, 0, canvas.width, canvas.height);
                  ctx.drawImage(img, 0, 0, width, height);
                  
                  const resizedBase64 = canvas.toDataURL('image/jpeg', 0.6); 
                  setAttachedImage(resizedBase64);
              }
          };
          img.src = e.target?.result as string;
      };
      reader.readAsDataURL(file);
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
      if (e.target.files && e.target.files[0]) {
          processImageFile(e.target.files[0]);
      }
  };

  const handleSendMessage = async (suggestedText?: string) => {
    const userMsg = typeof suggestedText === 'string' ? suggestedText : input.trim();
    const currentImage = attachedImage; 
    
    if (!userMsg && !currentImage) {
        return;
    }
    if (isTyping) {
        return;
    }

    const displayMsg = currentImage ? `*(📸 Đã đính kèm hình ảnh)*\n\n${userMsg}` : userMsg;
    setMessages(prev => [...prev, { role: 'user', text: displayMsg }]);
    
    setInput('');
    setAttachedImage(null); 
    setIsTyping(true);
    
    if (textareaRef.current) {
        textareaRef.current.style.height = 'auto';
    }

    try {
      if (currentImage && mode === 'tutor') {
          sessionStorage.setItem('tony_live_mode', 'TUTOR');
          
          // Bắn ảnh sang nửa trái hiển thị
          window.dispatchEvent(new CustomEvent('tony-open-image-board', { detail: currentImage }));
          
          // Ghi nhớ Biến Toàn Cục an toàn hơn Storage
          (window as any).tonyPendingImage = currentImage;
          
          setIsMinimized(true);
          
          // Mở Bảng đen ra
          window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
          
          // 🚀 BẮN LỆNH KHỞI ĐỘNG NÃO MẮT (VISION_MODE) KÈM THEO ẢNH CHUẨN XÁC
          setTimeout(() => {
              window.dispatchEvent(new CustomEvent('tony-force-start', { 
                  detail: { 
                      mode: 'vision_mode',
                      image: currentImage, // <--- ĐÃ TRUYỀN ẢNH THÀNH CÔNG VÀO LỆNH
                      query: userMsg || "Thầy giải chi tiết giúp em bài này với ạ.",
                      courseTitle: courseTitle || "Tổng hợp"
                  } 
              }));
          }, 600);
          
          setIsTyping(false);
          return; 
      }

      // NẾU KHÔNG CÓ ẢNH THÌ CHAT TRONG SIDEBAR NHƯ BÌNH THƯỜNG
      let endpoint = 'omni-ai-grader'; 
      let payload: any = {};

      if (mode === 'parent_mode') {
         const parentContext = sessionStorage.getItem('tony_parent_ai_context') || 'Không có dữ liệu học tập gần đây.';
         const studentName = sessionStorage.getItem('tony_parent_target_student') || 'học sinh';
         
         const systemPrompt = `Bạn là "Trợ lý Chủ nhiệm Tony AI". Nhiệm vụ của bạn là báo cáo tình hình học tập của học sinh ${studentName} cho phụ huynh.

         DƯỚI ĐÂY LÀ DỮ LIỆU HỌC TẬP THỰC TẾ TRONG 14 NGÀY QUA CỦA CHÁU:
         """
         ${parentContext}
         """

         QUY TẮC TRẢ LỜI ĐẶC BIỆT CẦN TUÂN THỦ:
         1. Bạn ĐANG TRỰC TIẾP CHAT VỚI PHỤ HUYNH. Hãy trả lời vô cùng lễ phép, lịch sự, ân cần. BẮT BUỘC xưng hô là "Dạ, thưa anh/chị" và xưng mình là "Trợ lý AI / Hệ thống".
         2. KHI PHỤ HUYNH HỎI: Chỉ dựa CHÍNH XÁC vào dữ liệu cung cấp ở trên để trả lời.
         3. ĐÁNH GIÁ TIẾN BỘ: Nếu thấy điểm tăng, hãy chúc mừng gia đình. Nếu điểm thấp, hãy động viên và khuyên phụ huynh nhắc nhở cháu thêm. Trình bày dạng bullet point cho dễ đọc.
         4. TUYỆT ĐỐI KHÔNG bịa đặt dữ liệu (hallucinate). NẾU KHÔNG CÓ DỮ LIỆU trả lời: "Dạ hệ thống ghi nhận dạo gần đây cháu chưa có hoạt động làm bài kiểm tra mới trên nền tảng ạ."
         
         CÂU HỎI TỪ PHỤ HUYNH: "${userMsg}"
         HÃY TRẢ LỜI LỊCH SỰ BẰNG TIẾNG VIỆT:`;

         payload = { 
             prompt: systemPrompt, 
             taskType: 'tutor' 
         };

      } else if (mode === 'ielts') {
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
             const unicodeInstruction = (taskType === 'math' || taskType === 'Science') 
                 ? `\n\n[QUAN TRỌNG VỀ ĐỊNH DẠNG]: TUYỆT ĐỐI KHÔNG SỬ DỤNG MÃ LATEX HAY KATEX (NHƯ \\frac, \\pm, \\sqrt, v.v.). BẠN PHẢI SỬ DỤNG CÁC KÝ TỰ UNICODE THÔNG THƯỜNG NHƯ x², ½, ⅓, √, ±, ∫, π, α, β, θ... ĐỂ HỌC SINH DỄ ĐỌC. SỬ DỤNG DẤU \` ĐỂ BỌC CÔNG THỨC VÀ BIẾN SỐ.` 
                 : '';
             payload = { 
                content: `Đề bài: ${topicTitle}\n\nNội dung từ học sinh: ${userMsg}${unicodeInstruction}`,
                imageUrl: currentImage || topicImage,
                imageUrls: currentImage ? [currentImage] : (topicImage ? [topicImage] : []),
                taskType: taskType 
             };
         }
      } else {
         const subjectRule = courseTitle ? `\n[KỶ LUẬT CHUYÊN MÔN]: Đây là lớp học môn: "${courseTitle}". Nếu câu hỏi không liên quan đến môn học này, bạn PHẢI TỪ CHỐI KHÉO LÉO.` : '';
         const systemPrompt = `Bạn là gia sư AI. Bài giảng: "${lectureTitle}". Nội dung: """${contextText}""". ${subjectRule}\nHãy trả lời học sinh: "${userMsg}"`;
         
         payload = { 
             prompt: systemPrompt, 
             taskType: 'tutor' 
         }; 
      }

      const { data, error } = await supabase.functions.invoke(endpoint, { body: payload });
      
      if (error || data?.error) {
          throw new Error("AI đang bận, hệ thống không thể kết nối ngay lúc này.");
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
    return text
        .replace(/\*\*(.*?)\*\*/g, '<b class="font-bold text-slate-800">$1</b>')
        .replace(/\*(.*?)\*/g, '<i class="italic">$1</i>')
        .replace(/`([^`]+)`/g, '<span class="italic text-[#0ea5e9] font-medium px-1">$1</span>')
        .replace(/\n/g, '<br/>');
  };

  if (!isOpen) {
      return null;
  }

  if (isMinimized) {
      return (
          <button 
              onClick={() => { setIsMinimized(false); }}
              className={`fixed bottom-[90px] md:bottom-[120px] right-3 md:right-8 z-[100000] w-12 h-12 md:w-16 md:h-16 rounded-full bg-gradient-to-tr ${theme.headerBg} text-white shadow-[0_8px_30px_rgba(0,0,0,0.25)] flex items-center justify-center text-xl md:text-2xl hover:scale-105 active:scale-95 transition-all duration-300 animate-in zoom-in group border-2 md:border-[3px] border-white/50 backdrop-blur-sm`}
              title="Mở lại khung Chat AI"
          >
              <span className="group-hover:hidden drop-shadow-md">
                  {theme.icon}
              </span>
              <span className="hidden group-hover:block drop-shadow-md">
                  💬
              </span>
              <span className="absolute top-0 right-0 w-3 h-3 md:w-4 md:h-4 bg-red-500 border-2 border-white rounded-full flex items-center justify-center">
                  <span className="absolute w-full h-full bg-red-500 rounded-full animate-ping opacity-75"></span>
              </span>
          </button>
      );
  }

  return (
    <>
      {isOpen && !isMinimized && (
          <div 
              className="fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-[99999] md:hidden transition-opacity" 
              onClick={() => { 
                  setIsMinimized(true); 
                  setIsExpanded(false); 
              }} 
          />
      )}
      
      <div 
          className={
              `fixed top-0 md:top-[64px] bottom-0 right-0 w-full ` + 
              `${isExpanded ? 'md:w-[800px]' : theme.width} ` + 
              `bg-[#f8fafc] shadow-[-10px_0_40px_rgba(0,0,0,0.1)] ` + 
              `z-[100000] flex flex-col transition-all duration-400 ease-out border-l border-slate-200 ` + 
              `${isOpen && !isMinimized ? 'translate-x-0' : 'translate-x-full'}`
          }
      >
        
        {/* HEADER SECTION */}
        <div 
            className={
                `h-[68px] md:h-[72px] bg-gradient-to-r ${theme.headerBg} ` + 
                `text-white flex items-center justify-between px-3 md:px-5 shrink-0 ` + 
                `shadow-md z-20 relative overflow-hidden`
            }
        >
          <div className="absolute inset-0 bg-white/5 mix-blend-overlay pointer-events-none"></div>
          
          <div className="flex items-center gap-2 md:gap-3 relative z-10 flex-1 min-w-0">
             <div className="w-10 h-10 md:w-11 md:h-11 bg-white/20 backdrop-blur-md rounded-xl flex items-center justify-center text-lg md:text-xl shadow-inner border border-white/10 shrink-0">
                 {theme.icon}
             </div>
             <div className="flex flex-col min-w-0">
                 <h3 className="font-bold text-[14px] md:text-[16px] leading-tight tracking-wide truncate">
                     {theme.title}
                 </h3>
                 <div className="flex items-center gap-1.5 mt-0.5">
                     <span className="w-2 h-2 bg-emerald-400 rounded-full animate-pulse shrink-0"></span>
                     <p className="text-[10px] md:text-[11px] text-white/90 font-medium uppercase tracking-wider truncate">
                         {theme.subtitle}
                     </p>
                 </div>
             </div>
          </div>
          
          <div className="flex items-center gap-1.5 md:gap-2 relative z-10 shrink-0 pl-2">
             
             {mode !== 'parent_mode' && (
                 <button 
                     onClick={handleCallTutor}
                     className="flex bg-white/10 hover:bg-white text-white hover:text-slate-900 border border-white/20 px-2 py-1.5 md:px-3 md:py-1.5 rounded-full text-[11px] md:text-[12px] font-bold transition-all items-center gap-1 shadow-sm active:scale-95"
                     title="Vào lớp Học trực tiếp với Gia Sư AI"
                 >
                     <span className="animate-pulse">👨‍🏫</span>
                     <span className="hidden sm:inline">Lên Bảng</span>
                     <span className="sm:hidden">Lên Bảng</span>
                 </button>
             )}

             <button 
                 onClick={() => { setIsExpanded(!isExpanded); }} 
                 className="hidden md:flex w-8 h-8 md:w-9 md:h-9 items-center justify-center rounded-full hover:bg-white/20 text-white transition-colors"
                 title="Phóng to"
             >
                {isExpanded ? (
                    <svg 
                        xmlns="http://www.w3.org/2000/svg" 
                        fill="none" 
                        viewBox="0 0 24 24" 
                        strokeWidth={2} 
                        stroke="currentColor" 
                        className="w-4 h-4 md:w-5 md:h-5"
                    >
                        <path 
                            strokeLinecap="round" 
                            strokeLinejoin="round" 
                            d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" 
                        />
                    </svg>
                ) : (
                    <svg 
                        xmlns="http://www.w3.org/2000/svg" 
                        fill="none" 
                        viewBox="0 0 24 24" 
                        strokeWidth={2} 
                        stroke="currentColor" 
                        className="w-4 h-4 md:w-5 md:h-5"
                    >
                        <path 
                            strokeLinecap="round" 
                            strokeLinejoin="round" 
                            d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0-4.5L15 15" 
                        />
                    </svg>
                )}
             </button>
             
             <button 
                 onClick={() => { setIsMinimized(true); }} 
                 className="w-8 h-8 md:w-9 md:h-9 flex items-center justify-center rounded-full hover:bg-white/20 text-white transition-colors"
                 title="Thu nhỏ Chat"
             >
                <svg 
                    xmlns="http://www.w3.org/2000/svg" 
                    fill="none" 
                    viewBox="0 0 24 24" 
                    strokeWidth={2.5} 
                    stroke="currentColor" 
                    className="w-4 h-4 md:w-5 md:h-5"
                >
                    <path 
                        strokeLinecap="round" 
                        strokeLinejoin="round" 
                        d="M19.5 8.25l-7.5 7.5-7.5-7.5" 
                    />
                </svg>
             </button>
             
             <button 
                 onClick={() => { 
                     if(window.confirm('Đóng cửa sổ này sẽ xóa lịch sử trò chuyện. Bạn có muốn thu nhỏ lại thay vì đóng hẳn không?')) {
                         setMessages([]);
                         onClose(); 
                         setIsExpanded(false); 
                     } else {
                         setIsMinimized(true);
                     }
                 }} 
                 className="w-8 h-8 md:w-9 md:h-9 flex items-center justify-center rounded-full hover:bg-red-500/80 transition-colors text-white text-lg font-bold ml-0.5"
                 title="Đóng hẳn"
             >
                 <svg 
                     xmlns="http://www.w3.org/2000/svg" 
                     fill="none" 
                     viewBox="0 0 24 24" 
                     strokeWidth={2.5} 
                     stroke="currentColor" 
                     className="w-4 h-4 md:w-5 md:h-5"
                 >
                     <path 
                         strokeLinecap="round" 
                         strokeLinejoin="round" 
                         d="M6 18L18 6M6 6l12 12" 
                     />
                 </svg>
             </button>
          </div>
        </div>

        {/* CHAT AREA SECTION */}
        <div 
            className="flex-1 overflow-y-auto p-4 md:p-6 space-y-6 custom-scrollbar bg-[url('/chat-pattern.png')] bg-repeat bg-[length:200px] bg-slate-50/90 bg-blend-overlay" 
            style={{ WebkitOverflowScrolling: 'touch' }}
        >
          {mode === 'ielts' && topicImage && (
              <div className="mb-6 animate-in fade-in slide-in-from-top-2 flex justify-center">
                  <div className="w-full max-w-sm rounded-2xl overflow-hidden border border-slate-200 shadow-sm bg-white p-2">
                      <div className="text-[10px] font-bold text-slate-400 uppercase mb-2 px-1 tracking-widest flex items-center gap-1">
                          <svg 
                              xmlns="http://www.w3.org/2000/svg" 
                              viewBox="0 0 20 20" 
                              fill="currentColor" 
                              className="w-3 h-3"
                          >
                              <path 
                                  fillRule="evenodd" 
                                  d="M1 5.25A2.25 2.25 0 013.25 3h13.5A2.25 2.25 0 0119 5.25v9.5A2.25 2.25 0 0116.75 17H3.25A2.25 2.25 0 011 14.75v-9.5zm1.5 5.81v3.69c0 .414.336.75.75.75h13.5a.75.75 0 00.75-.75v-2.69l-2.22-2.219a2.25 2.25 0 00-3.182 0l-1.44 1.439a2.25 2.25 0 01-3.182 0L5.06 7.29a2.25 2.25 0 00-3.182 0l-2.22 2.22zM3.25 4.5a.75.75 0 00-.75.75v.59l2.22-2.22a.75.75 0 011.06 0l1.44 1.44a.75.75 0 001.06 0l2.67-2.67a.75.75 0 011.06 0l2.22 2.22V5.25a.75.75 0 00-.75-.75H3.25z" 
                                  clipRule="evenodd" 
                              />
                          </svg>
                          Đề bài đính kèm
                      </div>
                      <img 
                          src={topicImage} 
                          alt="Task đề bài" 
                          className="w-full h-auto object-contain max-h-[250px] rounded-lg bg-slate-50" 
                      />
                  </div>
              </div>
          )}

          {messages.map((msg, idx) => (
            <div 
                key={idx} 
                className={`flex w-full ${msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-in fade-in slide-in-from-bottom-2`}
            >
               {msg.role === 'ai' && (
                   <div className="w-7 h-7 md:w-8 md:h-8 rounded-full bg-white border border-slate-200 flex items-center justify-center shrink-0 mr-2 mt-1 shadow-sm text-xs md:text-sm">
                       {theme.icon}
                   </div>
               )}
               
               <div 
                   className={
                       `max-w-[85%] p-3.5 md:p-4 text-[14px] md:text-[15px] leading-relaxed shadow-sm ` +
                       `${msg.role === 'user' ? `${theme.userBg} text-white rounded-2xl rounded-tr-sm` : `${theme.aiBg} border ${theme.aiBorder} text-slate-700 rounded-2xl rounded-tl-sm`}`
                   }
               >
                  {msg.role === 'user' ? (
                      <div className="whitespace-pre-wrap">
                          {msg.text}
                      </div>
                  ) : (
                      <div 
                          className="prose prose-sm prose-slate max-w-none" 
                          dangerouslySetInnerHTML={{ 
                              __html: formatMarkdown(msg.text) 
                          }} 
                      />
                  )}
               </div>
            </div>
          ))}
          
          {isTyping && (
             <div className="flex justify-start w-full animate-in fade-in">
                 <div className="w-7 h-7 md:w-8 md:h-8 rounded-full bg-white border border-slate-200 flex items-center justify-center shrink-0 mr-2 mt-1 shadow-sm text-xs md:text-sm opacity-70">
                     {theme.icon}
                 </div>
                 <div className="bg-white border border-slate-100 px-4 py-3 rounded-2xl rounded-tl-sm flex items-center gap-1.5 shadow-sm">
                     <span className="w-2 h-2 bg-slate-300 rounded-full animate-bounce"></span>
                     <span className="w-2 h-2 bg-slate-300 rounded-full animate-bounce delay-100"></span>
                     <span className="w-2 h-2 bg-slate-300 rounded-full animate-bounce delay-200"></span>
                 </div>
             </div>
          )}
          <div ref={messagesEndRef} className="h-4" />
        </div>

        {/* INPUT AREA SECTION */}
        <div className="p-3 md:p-4 bg-white border-t border-slate-200 shrink-0 z-10 pb-5 md:pb-4">
          
          {/* Gợi ý starter prompts */}
          <div className="flex items-center gap-2 mb-3 overflow-x-auto custom-scrollbar pb-2 hide-scroll-bar">
             {dynamicPrompts.map((p, i) => (
                <button 
                    key={i} 
                    onClick={() => { handleSuggestionClick(p); }} 
                    className="shrink-0 bg-slate-50 border border-slate-200 text-slate-600 hover:text-slate-900 text-[12px] md:text-[13px] font-semibold py-1.5 px-4 rounded-full hover:bg-slate-100 transition-colors shadow-sm whitespace-nowrap"
                >
                  {p}
                </button>
             ))}
          </div>

          {/* 🚀 THUMBNAIL ẢNH ĐÍNH KÈM */}
          {attachedImage && (
              <div className="mb-3 flex items-center animate-in slide-in-from-bottom-2">
                  <div className="relative inline-block border border-slate-200 rounded-xl overflow-hidden shadow-sm">
                      <img 
                          src={attachedImage} 
                          alt="Ảnh đính kèm" 
                          className="h-16 w-auto object-cover bg-slate-50" 
                      />
                      <button 
                          onClick={() => { setAttachedImage(null); }} 
                          className="absolute -top-1 -right-1 w-5 h-5 bg-red-500 text-white rounded-full flex items-center justify-center text-[10px] font-bold shadow-md hover:bg-red-600 border border-white"
                          title="Xóa ảnh"
                      >
                          ✕
                      </button>
                  </div>
                  {mode === 'tutor' && (
                      <span className="ml-3 text-[11px] font-bold text-sky-500 uppercase tracking-widest bg-sky-50 px-2 py-1 rounded-md animate-pulse">
                          ✨ AI Sẽ Lên Bảng Đen Để Giải Ảnh Này
                      </span>
                  )}
              </div>
          )}
          
          <div className={`relative flex items-end bg-slate-50 border border-slate-200 rounded-2xl p-1.5 ${theme.focusRing} transition-all duration-200`}>
            
            {/* NÚT GHIM CHỌN FILE FILE INPUT */}
            {mode !== 'parent_mode' && (
                <button 
                    onClick={() => { fileInputRef.current?.click(); }} 
                    className="w-10 h-10 shrink-0 flex items-center justify-center text-slate-400 hover:text-[#0ea5e9] hover:bg-sky-50 rounded-xl transition-colors self-end mb-[2px]" 
                    title="Đính kèm ảnh bài tập / Dán ảnh bằng Ctrl+V"
                >
                    <svg 
                        xmlns="http://www.w3.org/2000/svg" 
                        fill="none" 
                        viewBox="0 0 24 24" 
                        strokeWidth={2} 
                        stroke="currentColor" 
                        className="w-5 h-5"
                    >
                        <path 
                            strokeLinecap="round" 
                            strokeLinejoin="round" 
                            d="M18.375 12.739l-7.693 7.693a4.5 4.5 0 01-6.364-6.364l10.94-10.94A3 3 0 1119.5 7.372L8.552 18.32m.009-.01l-.01.01m5.699-9.941l-7.81 7.81a1.5 1.5 0 002.112 2.13" 
                        />
                    </svg>
                    <input 
                        type="file" 
                        ref={fileInputRef} 
                        className="hidden" 
                        accept="image/png, image/jpeg, image/jpg" 
                        onChange={handleFileChange} 
                    />
                </button>
            )}

            <textarea 
                ref={textareaRef} 
                value={input} 
                onChange={(e) => { 
                    setInput(e.target.value); 
                    e.target.style.height = 'auto'; 
                    e.target.style.height = `${Math.min(e.target.scrollHeight, 150)}px`; 
                }} 
                onKeyDown={(e) => { 
                    if (e.key === 'Enter' && !e.shiftKey) { 
                        e.preventDefault(); 
                        handleSendMessage(); 
                    } 
                }} 
                onPaste={handlePaste} 
                placeholder={mode === 'parent_mode' ? "Hỏi AI về tình hình của bé..." : "Ctrl+V để dán ảnh hoặc gõ câu hỏi..."}
                className="flex-1 min-h-[44px] max-h-[120px] bg-transparent text-[16px] md:text-[15px] text-slate-700 font-medium px-3 py-3 outline-none resize-none custom-scrollbar leading-relaxed" 
                rows={1} 
            />
            
            <button 
                onClick={() => { handleSendMessage(); }} 
                disabled={(!input.trim() && !attachedImage) || isTyping} 
                className={`absolute right-2 bottom-2 w-9 h-9 md:w-10 md:h-10 shrink-0 rounded-xl ${theme.btnColor} text-white flex items-center justify-center transition-all shadow-md disabled:opacity-50 disabled:shadow-none disabled:hover:scale-100 active:scale-95`}
            >
               <svg 
                   xmlns="http://www.w3.org/2000/svg" 
                   className="w-5 h-5 -translate-y-[1px] translate-x-[1px]" 
                   viewBox="0 0 20 20" 
                   fill="currentColor"
                >
                   <path 
                       d="M3.105 2.289a.75.75 0 00-.826.95l1.414 4.925A1.5 1.5 0 005.135 9.25h6.115a.75.75 0 010 1.5H5.135a1.5 1.5 0 00-1.442 1.086l-1.414 4.926a.75.75 0 00.826.95 28.896 28.896 0 0015.293-7.154.75.75 0 000-1.115A28.897 28.897 0 003.105 2.289z" 
                   />
               </svg>
            </button>
          </div>
          
          <div className="text-center mt-2">
              <span className="text-[9px] md:text-[10px] text-slate-400 font-medium">
                  Tony AI có thể mắc lỗi. Vui lòng kiểm tra lại thông tin.
              </span>
          </div>
        </div>
      </div>
    </>
  );
}