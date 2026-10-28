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

const UNICODE_FORMAT_INSTRUCTION = `
[QUY TẮC ĐỊNH DẠNG BẮT BUỘC - BẢO ĐẢM HIỂN THỊ CHUẨN UNICODE]:
- TUYỆT ĐỐI KHÔNG SỬ DỤNG MÃ LATEX HOẶC KÝ TỰ LATEX (CẤM dùng dấu $, $$, \\rightarrow, \\to, \\frac, \\pm, \\sqrt, ^{...}, _{...}, v.v.).
- BẮT BUỘC sử dụng ký tự UNICODE tiêu chuẩn trực tiếp trong câu trả lời:
  + Mũi tên phản ứng hóa học: dùng mũi tên Unicode → (hoặc ⇌, ↑, ↓). CẤM viết \\rightarrow.
  + Số mũ / Chỉ số ion trên (superscript): dùng các ký tự Unicode ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁿ (Ví dụ: Cu²⁺, Fe³⁺, SO₄²⁻, Zn²⁺, 2e⁻, x², cm³, 10⁻³). CẤM viết Cu^{2+}, SO_4^{2-}.
  + Chỉ số hóa học dưới (subscript): dùng các ký tự Unicode ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ (Ví dụ: H₂O, CO₂, O₂, CuSO₄, ZnSO₄, H₂SO₄, Fe₂O₃, Ca(OH)₂). CẤM viết O_2, CuSO_4.
  + Trạng thái chất trong hóa học: viết thường trong ngoặc đơn thông thường: (s), (l), (g), (aq).
  + Phương trình hóa học ví dụ chuẩn:
    2Mg (s) + O₂ (g) → 2MgO (s)
    Zn (s) + CuSO₄ (aq) → ZnSO₄ (aq) + Cu (s)
    Zn (s) + Cu²⁺ (aq) → Zn²⁺ (aq) + Cu (s)
    Zn → Zn²⁺ + 2e⁻
    Cu²⁺ + 2e⁻ → Cu
  + Ký hiệu toán học & khoa học: dùng ±, ×, ÷, √, °, ℃, ≈, ≠, ≤, ≥, Δ, π, α, β, θ, λ, Ω, μ.
  + Để nhấn mạnh công thức hoặc tên chất, hãy dùng in đậm **...** hoặc backtick \`...\`, tuyệt đối không bọc bằng dấu $.
- Trình bày mạch lạc, phân tách rõ ràng bằng gạch đầu dòng, các tiêu đề dùng in đậm **...** để dễ đọc.`;

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
    const handleSendCoachPrompt = (e: any) => {
        const promptText = e.detail?.prompt;
        if (promptText && typeof promptText === 'string') {
            setIsMinimized(false);
            setInput(promptText);
            setTimeout(() => {
                if (textareaRef.current) {
                    textareaRef.current.focus();
                }
            }, 150);
        }
    };
    window.addEventListener('tony-clear-chat', handleClearChat);
    window.addEventListener('tony-send-ai-prompt', handleSendCoachPrompt);
    
    return () => {
        window.removeEventListener('tony-clear-chat', handleClearChat);
        window.removeEventListener('tony-send-ai-prompt', handleSendCoachPrompt);
    };
  }, []);

  // 🚀 HELPER: Tạo welcome message dựa trên context hiện tại
  const generateWelcome = () => {
    let welcomeText = "";
    if (mode === 'parent_mode') {
      let studentName = 'học sinh';
      try { studentName = sessionStorage.getItem('tony_parent_target_student') || 'học sinh'; } catch(e) {}
      welcomeText = `Dạ chào anh/chị! Tôi là Trợ lý AI chủ nhiệm của bé **${studentName}**.\n\nHệ thống đã tổng hợp xong dữ liệu học tập của cháu trong 14 ngày qua. Anh/chị cần xem báo cáo tổng quan hay có câu hỏi cụ thể nào về tình hình của cháu không ạ?`;
    } else if (mode === 'ielts') {
      const isReflex = (topicTitle || '').toLowerCase().includes('phản xạ') || (topicTitle || '').toLowerCase().includes('giao tiếp');
      if (isReflex) {
        welcomeText = `Chào em! Thầy là Huấn luyện viên Luyện Phản Xạ Giao Tiếp.\n\n🎯 **Nội dung:** Luyện phản xạ cấu trúc câu giao tiếp thực chiến.\n\nEm có thể bấm chọn gợi ý bên dưới hoặc gửi câu hỏi để thầy gợi ý mẫu câu, từ vựng và hỗ trợ em luyện tập nhé!`;
      } else if (taskType === 'reading') {
        welcomeText = `Chào em! Thầy đã nhận được yêu cầu giải thích:\n\n**${topicTitle}**\n\nEm muốn hỏi thêm thầy điều gì?`;
      } else if (taskType === 'speaking') {
        welcomeText = `Chào em! Thầy là trợ lý Speaking.\n\n`;
        if (topicTitle) {
          welcomeText += `🎙️ **Chủ đề đang chọn:**\n*"${topicTitle}"*\n\nThầy đã nhận diện chủ đề trên! Em có thể bấm chọn gợi ý bên dưới để nhờ thầy **Tư vấn kịch bản (Lego)**, **Gợi ý từ vựng Band 8+**, hoặc cùng thầy luyện tập trả lời nhé!`;
        } else {
          welcomeText += `Em gửi đề bài hoặc paste câu hỏi vào đây, thầy sẽ tư vấn Kịch bản Lego, gợi ý từ vựng Band 8+ hoặc cùng em luyện tập trả lời nhé!`;
        }
      } else if (taskType === 'task1') {
        welcomeText = `Chào em! Thầy là trợ lý Writing Task 1.\n\n`;
        if (topicTitle) {
          welcomeText += `📋 **Đề bài đang chọn:**\n*"${topicTitle}"*\n\nThầy đã nhận diện đề bài này! Em có thể bấm chọn gợi ý bên dưới để nhờ thầy **Phân tích biểu đồ**, **Lập dàn ý**, hoặc dán bài viết của em vào đây để thầy **Chấm điểm & sửa lỗi** nhé!`;
        } else {
          welcomeText += `Em gửi đề bài hoặc paste nội dung vào đây, thầy sẽ phân tích biểu đồ, lập dàn ý, hoặc chấm điểm bài viết cho em nhé!`;
        }
      } else if (taskType === 'task2') {
        welcomeText = `Chào em! Thầy là trợ lý Writing Task 2.\n\n`;
        if (topicTitle) {
          welcomeText += `📋 **Đề bài đang chọn:**\n*"${topicTitle}"*\n\nThầy đã nhận diện đề bài này! Em hãy bấm chọn các nút gợi ý bên dưới để nhờ thầy **Lập dàn ý (Pillars)**, **Gợi ý từ vựng Band 8.0+**, hoặc dán bài viết của em vào đây để thầy **Chấm điểm & sửa lỗi** chi tiết nhé!`;
        } else {
          welcomeText += `Em gửi đề bài hoặc paste nội dung vào đây, thầy sẽ lập dàn ý, gợi ý từ vựng, hoặc chấm điểm bài làm cho em nhé!`;
        }
      } else {
        welcomeText = `Chào em! Thầy đã sẵn sàng hỗ trợ.\n\n`;
        if (topicTitle) welcomeText += `📋 **Đề bài / Câu hỏi:**\n*"${topicTitle}"*\n\n`;
        welcomeText += `Em gửi câu hỏi hoặc chọn các gợi ý bên dưới để thầy hỗ trợ nhé!`;
      }
      if (topicImage) welcomeText += `\n\n*(📷 Thầy đã nhận được hình ảnh/biểu đồ kèm theo)*`;
    } else {
      welcomeText = `Chào em! Thầy AI đã sẵn sàng hỗ trợ bài học **"${lectureTitle || 'này'}"**. Em có thể chat hỏi bài hoặc **Paste (Ctrl+V) / Tải ảnh lên** để thầy giải đáp nhé!`;
    }
    return [{ role: 'ai' as const, text: welcomeText }];
  };

  // 🚀 AUTO-RESET: Cập nhật / reset chat khi đổi topic, đổi bài giảng hoặc mở lên
  const prevContextRef = useRef({ topic: topicTitle, lecture: lectureTitle, mode, taskType });
  useEffect(() => {
    if (isOpen) {
      const prev = prevContextRef.current;
      const contextChanged = prev.topic !== topicTitle || prev.lecture !== lectureTitle || prev.mode !== mode || prev.taskType !== taskType;
      
      if (contextChanged || messages.length === 0) {
        setMessages(generateWelcome());
      }
      prevContextRef.current = { topic: topicTitle, lecture: lectureTitle, mode, taskType };
    }
  }, [topicTitle, lectureTitle, taskType, mode, isOpen]);

  const theme = useMemo(() => {
    if (mode === 'parent_mode') {
      return {
        headerBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]', 
        title: 'Trợ lý Phụ huynh', 
        subtitle: 'TonyEnglish • Báo cáo AI', 
        icon: '👨‍👩‍👧‍👦',
        userBg: 'bg-gradient-to-br from-[#0a5482] to-[#073b5c]', 
        aiBorder: 'border-slate-200/90', 
        aiBg: 'bg-white',
        btnColor: 'bg-[#0a5482] hover:bg-[#084266]', 
        focusRing: 'focus-within:border-[#2ab4e8] focus-within:bg-white focus-within:ring-4 focus-within:ring-[#2ab4e8]/10', 
        width: 'md:w-[440px]'
      };
    }

    if (mode === 'tutor') {
      return {
        headerBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]',
        title: 'Tony AI Tutor', 
        subtitle: 'Gia sư đồng hành 24/7', 
        icon: '🤖',
        userBg: 'bg-gradient-to-br from-[#0a5482] to-[#073b5c]', 
        aiBorder: 'border-slate-200/90', 
        aiBg: 'bg-white',
        btnColor: 'bg-[#0a5482] hover:bg-[#084266]', 
        focusRing: 'focus-within:border-[#2ab4e8] focus-within:bg-white focus-within:ring-4 focus-within:ring-[#2ab4e8]/10', 
        width: 'md:w-[420px]'
      };
    }
    
    switch (taskType) {
      case 'task1':
        return {
          headerBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]', 
          title: `IELTS Assessor (Task 1)`,
          subtitle: 'Chấm điểm & Sửa lỗi chuyên sâu', 
          icon: '📝',
          userBg: 'bg-gradient-to-br from-[#0a5482] to-[#073b5c]', 
          aiBorder: 'border-slate-200/90', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#0a5482] hover:bg-[#084266]', 
          focusRing: 'focus-within:border-[#2ab4e8] focus-within:bg-white focus-within:ring-4 focus-within:ring-[#2ab4e8]/10', 
          width: 'md:w-[480px]'
        };
      case 'task2':
        return {
          headerBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]', 
          title: `IELTS Assessor (${taskType.toUpperCase()})`,
          subtitle: 'Chấm điểm & Sửa lỗi chuyên sâu', 
          icon: '🎓',
          userBg: 'bg-gradient-to-br from-[#0a5482] to-[#073b5c]', 
          aiBorder: 'border-slate-200/90', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#0a5482] hover:bg-[#084266]', 
          focusRing: 'focus-within:border-[#2ab4e8] focus-within:bg-white focus-within:ring-4 focus-within:ring-[#2ab4e8]/10', 
          width: 'md:w-[480px]'
        };
      case 'math':
        return {
          headerBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]', 
          title: 'Math AI Tutor',
          subtitle: 'Giải chi tiết từng bước lập luận', 
          icon: '📐',
          userBg: 'bg-gradient-to-br from-[#0a5482] to-[#073b5c]', 
          aiBorder: 'border-slate-200/90', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#0a5482] hover:bg-[#084266]', 
          focusRing: 'focus-within:border-[#2ab4e8] focus-within:bg-white focus-within:ring-4 focus-within:ring-[#2ab4e8]/10', 
          width: 'md:w-[480px]'
        };
      case 'Science':
        return {
          headerBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]', 
          title: 'Science AI Tutor',
          subtitle: 'Phân tích hiện tượng & Thí nghiệm', 
          icon: '🧪',
          userBg: 'bg-gradient-to-br from-[#0a5482] to-[#073b5c]', 
          aiBorder: 'border-slate-200/90', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#0a5482] hover:bg-[#084266]', 
          focusRing: 'focus-within:border-[#2ab4e8] focus-within:bg-white focus-within:ring-4 focus-within:ring-[#2ab4e8]/10', 
          width: 'md:w-[480px]'
        };
      case 'speaking':
        return {
          headerBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]', 
          title: 'Speaking Assistant',
          subtitle: 'Lên ý tưởng & Bẻ lõi Part 2', 
          icon: '🎙️',
          userBg: 'bg-gradient-to-br from-[#0a5482] to-[#073b5c]', 
          aiBorder: 'border-slate-200/90', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#0a5482] hover:bg-[#084266]', 
          focusRing: 'focus-within:border-[#2ab4e8] focus-within:bg-white focus-within:ring-4 focus-within:ring-[#2ab4e8]/10', 
          width: 'md:w-[480px]'
        };
      case 'ESL':
        return {
          headerBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]', 
          title: 'Cambridge IGCSE ESL',
          subtitle: 'Strict Cambridge Evaluation Protocol', 
          icon: '📝',
          userBg: 'bg-gradient-to-br from-[#0a5482] to-[#073b5c]', 
          aiBorder: 'border-slate-200/90', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#0a5482] hover:bg-[#084266]', 
          focusRing: 'focus-within:border-[#2ab4e8] focus-within:bg-white focus-within:ring-4 focus-within:ring-[#2ab4e8]/10', 
          width: 'md:w-[480px]'
        };
      case 'reading':
        return {
          headerBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]', 
          title: 'IELTS Reading Tutor',
          subtitle: 'Giải thích đáp án chi tiết', 
          icon: '📖',
          userBg: 'bg-gradient-to-br from-[#0a5482] to-[#073b5c]', 
          aiBorder: 'border-slate-200/90', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#0a5482] hover:bg-[#084266]', 
          focusRing: 'focus-within:border-[#2ab4e8] focus-within:bg-white focus-within:ring-4 focus-within:ring-[#2ab4e8]/10', 
          width: 'md:w-[480px]'
        };
      default:
        return {
          headerBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]',
          title: 'Tony AI Multi-Tutor', 
          subtitle: 'Hỗ trợ học tập chuyên sâu', 
          icon: '✨',
          userBg: 'bg-gradient-to-br from-[#0a5482] to-[#073b5c]', 
          aiBorder: 'border-slate-200/90', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#0a5482] hover:bg-[#084266]', 
          focusRing: 'focus-within:border-[#2ab4e8] focus-within:bg-white focus-within:ring-4 focus-within:ring-[#2ab4e8]/10', 
          width: 'md:w-[480px]'
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

    const isReflex = (topicTitle || '').toLowerCase().includes('phản xạ') || (topicTitle || '').toLowerCase().includes('giao tiếp');
    if (isReflex) {
        return ["💡 Gợi ý mẫu câu phản xạ", "🧠 Mở rộng từ vựng giao tiếp", "✍️ Sửa lỗi phát âm / diễn đạt"];
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
    return (doc.body.textContent || '').substring(0, 40000);
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
            "${userMsg}"
            ${UNICODE_FORMAT_INSTRUCTION}`;
            
            payload = { 
                prompt: systemPrompt, 
                taskType: 'tutor' 
            }; 
         } else {
             payload = { 
                content: `Đề bài: ${topicTitle}\n\nNội dung từ học sinh: ${userMsg}\n\n[QUY TẮC XƯNG HÔ]: BẮT BUỘC xưng Thầy/Cô và gọi Em (TUYỆT ĐỐI CẤM xưng con). Hướng dẫn ân cần, giải thích chi tiết, chuẩn xác.\n${UNICODE_FORMAT_INSTRUCTION}`,
                imageUrl: currentImage || topicImage,
                imageUrls: currentImage ? [currentImage] : (topicImage ? [topicImage] : []),
                taskType: taskType 
             };
         }
      } else {
         const subjectRule = courseTitle ? `\n[KỶ LUẬT CHUYÊN MÔN]: Đây là lớp học môn: "${courseTitle}". Nếu câu hỏi không liên quan đến môn học này, bạn PHẢI TỪ CHỐI KHÉO LÉO.` : '';
         const systemPrompt = `Bạn là gia sư AI tận tâm, chuyên nghiệp. Luôn xưng Thầy/Cô và gọi Em (TUYỆT ĐỐI CẤM xưng con). Bài giảng: "${lectureTitle}". Nội dung: """${contextText}""". ${subjectRule}\n${UNICODE_FORMAT_INSTRUCTION}\nHãy trả lời học sinh: "${userMsg}"`;
         
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

  const convertLatexToUnicode = (text: string): string => {
    if (!text) return '';

    let r = text;

    // 1. Chuyển đổi các lệnh LaTeX phổ biến sang ký tự Unicode
    const symbolMap: [RegExp, string][] = [
      // Mũi tên phản ứng & logic
      [/\\rightleftharpoons/g, '⇌'],
      [/\\leftrightarrow/g, '⇌'],
      [/\\longrightarrow/g, '→'],
      [/\\rightarrow/g, '→'],
      [/\\to\b/g, '→'],
      [/\\longleftarrow/g, '←'],
      [/\\leftarrow/g, '←'],
      [/\\uparrow/g, '↑'],
      [/\\downarrow/g, '↓'],
      [/\\Rightarrow/g, '⇒'],
      [/\\Leftarrow/g, '⇐'],
      [/\\Leftrightarrow/g, '⇔'],

      // Ký hiệu toán - lý - hóa
      [/\\%/g, '%'],
      [/\\pm/g, '±'],
      [/\\mp/g, '∓'],
      [/\\times/g, '×'],
      [/\\cdot/g, '·'],
      [/\\div/g, '÷'],
      [/\\approx/g, '≈'],
      [/\\neq/g, '≠'],
      [/\\leq/g, '≤'],
      [/\\geq/g, '≥'],
      [/\\le\b/g, '≤'],
      [/\\ge\b/g, '≥'],
      [/\\equiv/g, '≡'],
      [/\\infty/g, '∞'],
      [/\\degree/g, '°'],
      [/\\\^\\circ/g, '°'],
      [/\^\{\\circ\}/g, '°'],
      [/\^\\circ/g, '°'],
      [/\\circ\b/g, '°'],

      // Chữ cái Hy Lạp
      [/\\alpha/g, 'α'],
      [/\\beta/g, 'β'],
      [/\\gamma/g, 'γ'],
      [/\\delta/g, 'δ'],
      [/\\theta/g, 'θ'],
      [/\\lambda/g, 'λ'],
      [/\\mu/g, 'μ'],
      [/\\pi/g, 'π'],
      [/\\sigma/g, 'σ'],
      [/\\omega/g, 'ω'],
      [/\\Omega/g, 'Ω'],
      [/\\Delta\s*(?=[A-Za-z])/g, 'Δ'],
      [/\\Delta/g, 'Δ'],
      [/\\Sigma/g, 'Σ'],

      // Cấu trúc toán / hóa
      [/\\sqrt\{([^}]+)\}/g, '√($1)'],
      [/\\sqrt\b/g, '√'],
      [/\\frac\{([^}]+)\}\{([^}]+)\}/g, '($1)/($2)'],
      [/\\mathrm\{([^}]+)\}/g, '$1'],
      [/\\text\{([^}]+)\}/g, '$1'],
      [/\\mathbf\{([^}]+)\}/g, '**$1**'],
      [/\\left/g, ''],
      [/\\right/g, ''],
    ];

    for (const [pattern, repl] of symbolMap) {
      r = r.replace(pattern, repl);
    }

    // 2. Chuyển đổi số mũ & điện tích ion (superscript: Cu^{2+}, SO_4^{2-}, x^2...)
    const supMap: Record<string, string> = {
      '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
      '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
      '+': '⁺', '-': '⁻', '=': '⁼', '(': '⁽', ')': '⁾',
      'n': 'ⁿ', 'i': 'ⁱ', 'x': 'ˣ', 'y': 'ʸ'
    };

    const toSup = (chars: string) => {
      let allMapped = true;
      for (const c of chars) {
        if (!supMap[c]) {
          allMapped = false;
          break;
        }
      }
      if (allMapped) {
        return chars.split('').map(c => supMap[c]).join('');
      }
      return `<sup>${chars}</sup>`;
    };

    r = r.replace(/\^\{([^}]+)\}/g, (_, inner) => toSup(inner));
    r = r.replace(/\^([0-9+\-n])/g, (_, char) => supMap[char] || `<sup>${char}</sup>`);

    // 3. Chuyển đổi chỉ số hóa học dưới (subscript: O_2, CuSO_4, H_2O...)
    const subMap: Record<string, string> = {
      '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
      '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
      '+': '₊', '-': '₋', '=': '₌', '(': '₍', ')': '₎',
      'a': 'ₐ', 'e': 'ₑ', 'o': 'ₒ', 'x': 'ₓ', 'h': 'ₕ',
      'k': 'ₖ', 'l': 'ₗ', 'm': 'ₘ', 'n': 'ₙ', 'p': 'ₚ',
      's': 'ₛ', 't': 'ₜ'
    };

    const toSub = (chars: string) => {
      let allMapped = true;
      for (const c of chars) {
        if (!subMap[c]) {
          allMapped = false;
          break;
        }
      }
      if (allMapped) {
        return chars.split('').map(c => subMap[c]).join('');
      }
      return `<sub>${chars}</sub>`;
    };

    r = r.replace(/_\{([^}]+)\}/g, (_, inner) => toSub(inner));
    r = r.replace(/_([0-9+\-])/g, (_, char) => subMap[char] || `<sub>${char}</sub>`);

    // 4. Bóc tách dấu bọc $ ... $ và $$ ... $$
    r = r.replace(/\$\$([^$]+)\$\$/g, '$1');
    r = r.replace(/\$([^$\n]+)\$/g, '$1');

    // 5. Loại bỏ dấu gạch chéo ngược LaTeX thừa trước các từ thông thường
    r = r.replace(/\\([a-zA-Z]+)/g, '$1');

    return r;
  };

  const formatMarkdown = (text: string) => {
    if (!text) return '';
    // 1. Tự động chuyển toàn bộ mã LaTeX / công thức toán-lý-hóa về Unicode
    let formatted = convertLatexToUnicode(text);

    // 2. Format tiêu đề Markdown (###, ##, #)
    formatted = formatted.replace(/^### (.*$)/gim, '<h3 class="font-bold text-slate-800 text-[15px] mt-3 mb-1">$1</h3>');
    formatted = formatted.replace(/^## (.*$)/gim, '<h2 class="font-bold text-slate-800 text-[16px] mt-3.5 mb-1.5">$1</h2>');
    formatted = formatted.replace(/^# (.*$)/gim, '<h1 class="font-bold text-slate-900 text-[17px] mt-4 mb-2">$1</h1>');

    // 3. Format đường kẻ phân cách (---)
    formatted = formatted.replace(/^---$/gim, '<hr class="my-2.5 border-slate-200" />');

    // 4. Format gạch đầu dòng (* item hoặc - item)
    formatted = formatted.replace(/^[*\-] (.*$)/gim, '<div class="flex items-start my-1"><span class="inline-block w-1.5 h-1.5 rounded-full bg-[#2ab4e8] mt-2 mr-2 shrink-0"></span><span>$1</span></div>');

    // 5. In đậm và in nghiêng
    formatted = formatted.replace(/\*\*(.*?)\*\*/g, '<b class="font-bold text-slate-900">$1</b>');
    formatted = formatted.replace(/(?<!\*)\*(?!\s)([^*]+?)(?<!\s)\*(?!\*)/g, '<i class="italic">$1</i>');

    // 6. Code inline
    formatted = formatted.replace(/`([^`]+)`/g, '<span class="text-[#0a5482] font-semibold px-1.5 py-0.5 bg-sky-50 border border-sky-100 rounded-md">$1</span>');

    // 7. Dọn dẹp khoảng trống thừa trước khi xuống dòng
    formatted = formatted.replace(/(<\/h[1-3]>|<\/div>|<hr[^>]*>)\n+/gi, '$1');
    formatted = formatted.replace(/\n/g, '<br/>');

    return formatted;
  };

  if (!isOpen) {
      return null;
  }

  if (isMinimized) {
      return (
          <button 
              onClick={() => { setIsMinimized(false); }}
              className={`fixed bottom-[90px] md:bottom-[110px] right-3 md:right-7 z-[100000] w-13 h-13 md:w-15 md:h-15 rounded-2xl bg-gradient-to-br ${theme.headerBg} text-white shadow-[0_12px_32px_rgba(10,84,130,0.35)] flex items-center justify-center text-xl md:text-2xl hover:scale-105 active:scale-95 transition-all duration-300 animate-in zoom-in group border-2 border-[#2ab4e8]/60 backdrop-blur-sm cursor-pointer`}
              title="Mở lại khung Chat Tony AI Tutor"
          >
              <span className="group-hover:hidden drop-shadow-md">
                  {theme.icon}
              </span>
              <span className="hidden group-hover:block drop-shadow-md">
                  💬
              </span>
              <span className="absolute -top-1 -right-1 w-3.5 h-3.5 bg-emerald-400 border-2 border-[#073b5c] rounded-full flex items-center justify-center">
                  <span className="absolute w-full h-full bg-emerald-400 rounded-full animate-ping opacity-75"></span>
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
              `bg-[#f8fafc] shadow-[-12px_0_40px_rgba(15,23,42,0.12)] ` + 
              `z-[100000] flex flex-col transition-all duration-400 ease-out border-l border-slate-200/90 ` + 
              `${isOpen && !isMinimized ? 'translate-x-0' : 'translate-x-full'}`
          }
      >
        
        {/* HEADER SECTION (Synchronized with TonyEnglish.vn Design System) */}
        <div 
            className={
                `bg-gradient-to-r ${theme.headerBg} ` + 
                `text-white flex items-center justify-between px-3.5 md:px-4 py-3 shrink-0 ` + 
                `shadow-md z-20 relative overflow-hidden border-b border-white/15`
            }
        >
          <div className="absolute -top-12 -right-12 w-36 h-36 bg-[#2ab4e8]/20 blur-2xl rounded-full pointer-events-none"></div>
          
          <div className="flex items-center gap-2.5 relative z-10 flex-1 min-w-0">
             <div className="w-9 h-9 md:w-10 md:h-10 bg-white/12 backdrop-blur-md rounded-xl flex items-center justify-center text-base md:text-lg border border-white/20 shadow-2xs shrink-0">
                 {theme.icon}
             </div>
             <div className="flex flex-col min-w-0">
                 <div className="flex items-center gap-1.5">
                     <span className="w-1.5 h-1.5 bg-emerald-400 rounded-full animate-pulse shrink-0"></span>
                     <p className="text-[9.5px] md:text-[10px] text-[#2ab4e8] font-extrabold uppercase tracking-widest truncate">
                         {theme.subtitle}
                     </p>
                 </div>
                 <h3 className="font-black text-[14px] md:text-[15.5px] leading-tight tracking-tight text-white truncate mt-0.5">
                     {theme.title}
                 </h3>
             </div>
          </div>
          
          <div className="flex items-center gap-1.5 relative z-10 shrink-0 pl-2">
             
             {mode !== 'parent_mode' && (
                 <button 
                     onClick={handleCallTutor}
                     className="flex bg-[#2ab4e8] hover:bg-[#1fa0d4] text-white border border-white/25 px-2.5 py-1.5 rounded-xl text-[11px] md:text-xs font-extrabold transition-all items-center gap-1 shadow-xs active:scale-95 cursor-pointer shrink-0"
                     title="Vào lớp Học trực tiếp với Gia Sư AI trên Bảng Đen"
                 >
                     <span>👨‍🏫</span>
                     <span>Lên Bảng</span>
                 </button>
             )}

             <button 
                 onClick={() => { setIsExpanded(!isExpanded); }} 
                 className="hidden md:flex w-8 h-8 items-center justify-center rounded-xl bg-white/10 hover:bg-white/20 border border-white/15 text-white transition-all cursor-pointer"
                 title={isExpanded ? "Thu gọn khung" : "Mở rộng khung"}
             >
                {isExpanded ? (
                    <svg 
                        xmlns="http://www.w3.org/2000/svg" 
                        fill="none" 
                        viewBox="0 0 24 24" 
                        strokeWidth={2} 
                        stroke="currentColor" 
                        className="w-4 h-4"
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
                        className="w-4 h-4"
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
                 className="w-8 h-8 flex items-center justify-center rounded-xl bg-white/10 hover:bg-white/20 border border-white/15 text-white transition-all cursor-pointer"
                 title="Thu nhỏ Chat"
             >
                <svg 
                    xmlns="http://www.w3.org/2000/svg" 
                    fill="none" 
                    viewBox="0 0 24 24" 
                    strokeWidth={2.5} 
                    stroke="currentColor" 
                    className="w-4 h-4"
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
                 className="w-8 h-8 flex items-center justify-center rounded-xl bg-white/10 hover:bg-rose-500 border border-white/15 hover:border-rose-400 transition-all text-white cursor-pointer"
                 title="Đóng hẳn"
             >
                 <svg 
                     xmlns="http://www.w3.org/2000/svg" 
                     fill="none" 
                     viewBox="0 0 24 24" 
                     strokeWidth={2.5} 
                     stroke="currentColor" 
                     className="w-4 h-4"
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

        {/* ACTIVE LESSON / TOPIC CONTEXT STRIP */}
        {mode !== 'parent_mode' && (topicTitle || lectureTitle || courseTitle) && (
          <div className="bg-white border-b border-slate-200/80 px-4 py-2 flex items-center gap-2 shrink-0 shadow-2xs">
            <span className="w-1 h-3.5 rounded-full bg-[#2ab4e8] shrink-0"></span>
            <span className="text-[10.5px] font-extrabold uppercase tracking-wider text-[#0a5482] shrink-0">
              {mode === 'ielts' ? 'Đang luyện:' : 'Đang học:'}
            </span>
            <span className="text-xs font-semibold text-slate-600 truncate" title={topicTitle || lectureTitle || courseTitle}>
              {topicTitle || lectureTitle || courseTitle}
            </span>
          </div>
        )}

        {/* CHAT AREA SECTION */}
        <div 
            className="flex-1 overflow-y-auto p-4 md:p-5 space-y-4 custom-scrollbar bg-[#f8fafc]" 
            style={{ WebkitOverflowScrolling: 'touch' }}
        >
          {mode === 'ielts' && topicImage && (
              <div className="mb-4 animate-in fade-in slide-in-from-top-2 flex justify-center">
                  <div className="w-full max-w-sm rounded-2xl overflow-hidden border border-slate-200/90 shadow-xs bg-white p-2.5">
                      <div className="text-[10px] font-extrabold text-[#0a5482] uppercase mb-2 px-1 tracking-widest flex items-center gap-1.5">
                          <span className="w-1.5 h-1.5 rounded-full bg-[#2ab4e8]"></span>
                          Đề bài đính kèm
                      </div>
                      <img 
                          src={topicImage} 
                          alt="Task đề bài" 
                          className="w-full h-auto object-contain max-h-[240px] rounded-xl bg-slate-50" 
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
                   <div className="w-8 h-8 rounded-xl bg-gradient-to-br from-[#0a5482] to-[#073b5c] text-white border border-sky-200/50 flex items-center justify-center shrink-0 mr-2.5 mt-0.5 shadow-xs text-xs md:text-sm">
                       {theme.icon}
                   </div>
               )}
               
               <div 
                   className={
                       `max-w-[85%] p-3.5 md:p-4 text-[13.5px] md:text-[14.5px] leading-relaxed ` +
                       `${msg.role === 'user' ? `${theme.userBg} text-white rounded-2xl rounded-tr-xs shadow-sm` : `${theme.aiBg} border ${theme.aiBorder} text-slate-700 rounded-2xl rounded-tl-xs shadow-xs`}`
                   }
               >
                  {msg.role === 'user' ? (
                      <div className="whitespace-pre-wrap font-medium">
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
                 <div className="w-8 h-8 rounded-xl bg-gradient-to-br from-[#0a5482] to-[#073b5c] text-white border border-sky-200/50 flex items-center justify-center shrink-0 mr-2.5 mt-0.5 shadow-xs text-xs md:text-sm opacity-80">
                     {theme.icon}
                 </div>
                 <div className="bg-white border border-slate-200/90 px-4 py-3 rounded-2xl rounded-tl-xs flex items-center gap-1.5 shadow-xs">
                     <span className="w-2 h-2 bg-[#2ab4e8] rounded-full animate-bounce"></span>
                     <span className="w-2 h-2 bg-[#0a5482] rounded-full animate-bounce delay-100"></span>
                     <span className="w-2 h-2 bg-[#2ab4e8] rounded-full animate-bounce delay-200"></span>
                 </div>
             </div>
          )}
          <div ref={messagesEndRef} className="h-2" />
        </div>

        {/* INPUT AREA SECTION */}
        <div className="p-3 md:p-4 bg-white border-t border-slate-200/90 shrink-0 z-10 pb-4 md:pb-4">
          
          {/* Gợi ý starter prompts (Wrap gọn gàng không bị cắt chữ) */}
          <div className="flex flex-wrap items-center gap-1.5 mb-2.5">
             {dynamicPrompts.map((p, i) => (
                <button 
                    key={i} 
                    onClick={() => { handleSuggestionClick(p); }} 
                    className="bg-sky-50/80 hover:bg-[#0a5482] border border-sky-200/90 hover:border-[#0a5482] text-[#0a5482] hover:text-white text-[11.5px] md:text-[12px] font-bold py-1.5 px-3 rounded-xl transition-all shadow-2xs cursor-pointer"
                >
                  {p}
                </button>
             ))}
          </div>

          {/* 🚀 THUMBNAIL ẢNH ĐÍNH KÈM */}
          {attachedImage && (
              <div className="mb-3 flex items-center animate-in slide-in-from-bottom-2">
                  <div className="relative inline-block border border-slate-200 rounded-xl overflow-hidden shadow-xs">
                      <img 
                          src={attachedImage} 
                          alt="Ảnh đính kèm" 
                          className="h-16 w-auto object-cover bg-slate-50" 
                      />
                      <button 
                          onClick={() => { setAttachedImage(null); }} 
                          className="absolute -top-1 -right-1 w-5 h-5 bg-rose-500 text-white rounded-full flex items-center justify-center text-[10px] font-bold shadow-md hover:bg-rose-600 border border-white cursor-pointer"
                          title="Xóa ảnh"
                      >
                          ✕
                      </button>
                  </div>
                  {mode === 'tutor' && (
                      <span className="ml-3 text-[11px] font-extrabold text-[#0a5482] uppercase tracking-wider bg-sky-50 border border-sky-200 px-2.5 py-1 rounded-lg animate-pulse">
                          ✨ AI Sẽ Lên Bảng Đen Để Giải Ảnh Này
                      </span>
                  )}
              </div>
          )}
          
          <div className={`relative flex items-end gap-1 bg-slate-50/90 border border-slate-200/90 rounded-2xl p-1.5 ${theme.focusRing} transition-all duration-200`}>
            
            {/* NÚT GHIM CHỌN FILE FILE INPUT */}
            {mode !== 'parent_mode' && (
                <button 
                    onClick={() => { fileInputRef.current?.click(); }} 
                    className="w-9 h-9 md:w-10 md:h-10 shrink-0 flex items-center justify-center text-slate-400 hover:text-[#0a5482] hover:bg-sky-50 rounded-xl transition-colors self-end mb-[1px] cursor-pointer" 
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
                className="flex-1 min-h-[40px] max-h-[120px] bg-transparent text-[15px] md:text-[14.5px] text-slate-700 font-medium px-2 py-2 outline-none resize-none custom-scrollbar leading-relaxed" 
                rows={1} 
            />
            
            <button 
                onClick={() => { handleSendMessage(); }} 
                disabled={(!input.trim() && !attachedImage) || isTyping} 
                className={`w-9 h-9 md:w-10 md:h-10 shrink-0 rounded-xl ${theme.btnColor} text-white flex items-center justify-center transition-all shadow-sm disabled:opacity-40 disabled:shadow-none active:scale-95 self-end mb-[1px] cursor-pointer`}
            >
               <svg 
                   xmlns="http://www.w3.org/2000/svg" 
                   className="w-4 h-4 md:w-5 md:h-5 -translate-y-[1px] translate-x-[1px]" 
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
              <span className="text-[10px] text-slate-400 font-medium">
                  Tony AI có thể mắc lỗi. Vui lòng kiểm tra lại thông tin.
              </span>
          </div>
        </div>
      </div>
    </>
  );
}