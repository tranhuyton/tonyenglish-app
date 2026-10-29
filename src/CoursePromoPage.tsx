import React, { useState, useEffect } from 'react';
import { supabase } from './supabase';

interface CoursePromoPageProps {
  onNavigate: (view: string) => void;
  onStartTest?: (type: string, data: any) => void;
}

interface PackageCardItem {
  id: string;
  category: 'english' | 'igcse';
  badge: string;
  title: string;
  subtitle: string;
  icon: string;
  gradient: string;
  accentColor: string;
  stats: string[];
  highlights: string[];
}

const CONTACT_PHONE = '0935058688';
const CONTACT_PHONE_DISPLAY = '0935 058 688';
const CONTACT_ZALO_URL = 'https://zalo.me/0935058688';
const CONTACT_EMAIL = 'tranhuyton@gmail.com';

const trackMetaPixelEvent = (eventName: string, params?: Record<string, any>, isCustom = false) => {
  try {
    const w = window as any;
    if (typeof w.fbq === 'function') {
      w.fbq(isCustom ? 'trackCustom' : 'track', eventName, {
        site_domain: 'tonyenglish.vn',
        content_category: 'TonyEnglish_IELTS_IGCSE',
        ...params,
      });
    }
  } catch (e) {}
};

const FEATURED_PACKAGES: PackageCardItem[] = [
  {
    id: 'ielts-premium',
    category: 'english',
    badge: 'BÁN CHẠY NHẤT',
    title: 'IELTS Premium Toàn Diện (4 Kỹ Năng)',
    subtitle: 'Lộ trình bài bản từ nền tảng đến Band 7.0+ tích hợp phòng thi máy tính chuẩn IDP/BC & AI chấm chữa 24/7',
    icon: '🏆',
    gradient: 'from-sky-600 via-[#0a5482] to-indigo-900',
    accentColor: 'text-sky-600 bg-sky-50 border-sky-200',
    stats: ['9 Học phần chuyên sâu', '70+ Bài giảng tương tác', '367+ Đề luyện thi thực chiến'],
    highlights: [
      'Giao diện thi thử trên máy tính giống 100% phòng thi thật (Highlight, Note, Audio chuẩn)',
      'AI Giám khảo chấm chữa chi tiết IELTS Writing Task 1, Task 2 & Luyện phản xạ Speaking 1-1',
      'Video bài giảng & hệ thống bài tập thực hành gắn liền ngay trong từng bài học',
      'Có lớp học thử miễn phí các học phần đầu để trải nghiệm trước khi đăng ký'
    ]
  },
  {
    id: 'reflex-communication',
    category: 'english',
    badge: 'ĐỘT PHÁ PHẢN XẠ AI',
    title: 'Giao Tiếp & Phản Xạ Thực Chiến Cùng AI',
    subtitle: 'Xóa bỏ nỗi sợ nói tiếng Anh với 124 bài giảng tình huống, Podcast hội thoại & phòng luyện nói AI thời gian thực',
    icon: '🎙️',
    gradient: 'from-indigo-600 via-violet-700 to-purple-900',
    accentColor: 'text-indigo-600 bg-indigo-50 border-indigo-200',
    stats: ['13 Học phần chủ đề', '124 Bài giảng & Podcast', '102 Bài luyện phản xạ'],
    highlights: [
      'Luyện nghe - nói qua các tình huống giao tiếp đời sống, công việc và học thuật',
      'Đàm thoại trực tiếp bằng giọng nói với AI Tutor thông minh, sửa lỗi phát âm & ngữ pháp tức thì',
      'Hệ thống Podcast hội thoại song ngữ giúp tắm ngôn ngữ mọi lúc mọi nơi',
      'Học thử miễn phí các bài giảng mẫu trong từng học phần'
    ]
  },
  {
    id: 'grammar-vocab-pronunciation',
    category: 'english',
    badge: 'NỀN TẢNG VỮNG CHẮC',
    title: 'Combo Ngữ Pháp, Từ Vựng & Phát Âm Chuẩn Quốc Tế',
    subtitle: 'Xây gốc tiếng Anh toàn diện: Hệ thống hóa toàn bộ chủ điểm Ngữ pháp, Từ vựng học thuật và Phát âm IPA',
    icon: '📚',
    gradient: 'from-emerald-600 via-teal-700 to-cyan-900',
    accentColor: 'text-emerald-700 bg-emerald-50 border-emerald-200',
    stats: ['11 Học phần cốt lõi', '62 Bài giảng trực quan', '490+ Bài tập & Mini Test'],
    highlights: [
      'Bao gồm trọn bộ 2 khóa: Grammar & Vocabulary và Pronunciation Mastery',
      'Học từ vựng qua ngữ cảnh đọc hiểu (Immersion Reading) kết hợp Game tương tác ghi nhớ sâu',
      'Giải thích chi tiết từng câu hỏi trắc nghiệm, tự động thống kê lỗi sai cần khắc phục',
      'Phù hợp cho học sinh THCS, THPT, sinh viên và người mất gốc cần lấy lại nền tảng nhanh'
    ]
  },
  {
    id: 'igcse-sciences',
    category: 'igcse',
    badge: 'CAMBRIDGE IGCSE',
    title: 'Tổ Hợp Khoa Học Quốc Tế Cambridge IGCSE Sciences',
    subtitle: 'Bao gồm: Co-ordinated Sciences (0654), Biology (0610), Chemistry (0620), Physics (0625)',
    icon: '🧬',
    gradient: 'from-blue-700 via-indigo-800 to-slate-900',
    accentColor: 'text-blue-700 bg-blue-50 border-blue-200',
    stats: ['Song ngữ Anh - Việt', '60+ Bài giảng & Mô phỏng', '600+ Đề Past Papers & Topical'],
    highlights: [
      'Bài giảng thiết kế trực quan kèm bản dịch song ngữ Anh - Việt & Audio giảng bài từng mục',
      'Mô phỏng thí nghiệm khoa học tương tác trực tiếp ngay trên trang bài giảng',
      'Kho đề thi Past Papers (Paper 2, Paper 4, Paper 6) phân loại theo chuyên đề & năm thi',
      'AI chấm điểm câu hỏi tự luận bám sát Marking Scheme chuẩn Cambridge'
    ]
  },
  {
    id: 'igcse-business-econ',
    category: 'igcse',
    badge: 'CAMBRIDGE IGCSE',
    title: 'Kinh Tế & Kinh Doanh Quốc Tế (Economics 0455 & Business 0450)',
    subtitle: 'Làm chủ thuật ngữ kinh tế, phân tích Case Study và kỹ năng viết luận đạt điểm A/A* kỳ thi Cambridge IGCSE',
    icon: '📈',
    gradient: 'from-amber-600 via-orange-700 to-rose-900',
    accentColor: 'text-amber-700 bg-amber-50 border-amber-200',
    stats: ['14 Học phần chuyên đề', '69 Bài giảng song ngữ', '155+ Đề thi & Case Study'],
    highlights: [
      'Cấu trúc bài giảng 4 trang độc quyền: Bản tiếng Anh, Bản tiếng Việt, Câu hỏi mẫu Paper 2 & Syllabus',
      'Tích hợp Audio Podcast giảng giải khái niệm kinh tế - doanh nghiệp dễ hiểu, sinh động',
      'Luyện tập Case Study chia đôi màn hình (Split-Screen) kèm AI chấm chữa theo Rubric Cambridge',
      'Mở học thử các bài giảng đầu mỗi chương để học sinh trải nghiệm phương pháp học'
    ]
  },
  {
    id: 'igcse-geo-math-esl',
    category: 'igcse',
    badge: 'CAMBRIDGE IGCSE',
    title: 'IGCSE Geography (0460), Maths (0580 / 0606) & ESL (0510)',
    subtitle: 'Trọn bộ bài giảng tương tác, Podcast học thuật và kho đề luyện thi chuyên sâu cho học sinh trường Quốc tế & Song ngữ',
    icon: '🌍',
    gradient: 'from-cyan-700 via-sky-800 to-slate-900',
    accentColor: 'text-cyan-700 bg-cyan-50 border-cyan-200',
    stats: ['15+ Học phần', '65+ Bài giảng & Podcast', '160+ Đề luyện chuyên sâu'],
    highlights: [
      'Geography 0460: Đầy đủ 11 chuyên đề kèm bản đồ, biểu đồ, Case Study & Podcast song ngữ',
      'Mathematics 0580 & Additional Maths 0606: Hệ thống công thức, ví dụ minh họa từng bước dễ hiểu',
      'English as a Second Language (0510): Luyện chuyên sâu Reading, Writing, Listening chuẩn format mới',
      'Hỗ trợ lộ trình cá nhân hóa và lịch báo bài tự động theo mục tiêu kỳ thi'
    ]
  }
];

export default function CoursePromoPage({ onNavigate }: CoursePromoPageProps) {
  const [dbCourses, setDbCourses] = useState<any[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<'all' | 'english' | 'igcse'>('all');

  // Form state
  const [fullName, setFullName] = useState('');
  const [phone, setPhone] = useState('');
  const [studentEmail, setStudentEmail] = useState('');
  const [selectedCourseTitle, setSelectedCourseTitle] = useState('IELTS Premium Toàn Diện');
  const [note, setNote] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submittedSuccess, setSubmittedSuccess] = useState(false);
  const [copiedLink, setCopiedLink] = useState(false);
  const [copiedZaloText, setCopiedZaloText] = useState(false);

  useEffect(() => {
    document.title = 'Các Gói Khóa Học Online & Đăng Ký Học Thử | TonyEnglish';
    fetchPublicCourses();

    // Check if URL has ?course=...
    try {
      const params = new URLSearchParams(window.location.search);
      const courseParam = params.get('course');
      if (courseParam) {
        setSelectedCourseTitle(courseParam);
      }
      trackMetaPixelEvent('ViewContent', {
        content_name: courseParam || 'Trang Khóa Học IELTS & IGCSE',
      });
    } catch (e) {}
  }, []);

  const fetchPublicCourses = async () => {
    try {
      const { data } = await supabase
        .from('courses')
        .select('id, title, type, order_index')
        .order('order_index');
      if (data) setDbCourses(data);
    } catch (err) {
      console.warn('Error fetching courses:', err);
    }
  };

  const scrollToRegister = (courseName?: string) => {
    if (courseName) {
      setSelectedCourseTitle(courseName);
    }
    trackMetaPixelEvent('InitiateCheckout', {
      content_name: courseName || selectedCourseTitle,
    });
    setSubmittedSuccess(false);
    const el = document.getElementById('dang-ky-hoc-thu');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  const buildRegistrationMessage = () => {
    return [
      `🎁 ĐĂNG KÝ HỌC THỬ & TƯ VẤN KHÓA HỌC - TONYENGLISH`,
      `--------------------------------------------`,
      `👤 Họ và tên: ${fullName.trim() || '(Chưa nhập)'}`,
      `📞 Số điện thoại / Zalo: ${phone.trim() || '(Chưa nhập)'}`,
      `✉️ Email nhận tài khoản học thử: ${studentEmail.trim() || '(Chưa nhập)'}`,
      `📚 Gói khóa học quan tâm: ${selectedCourseTitle}`,
      note.trim() ? `📝 Ghi chú / Trình độ hiện tại: ${note.trim()}` : '',
      `--------------------------------------------`,
      `🌐 Gửi từ trang đăng ký khóa học TonyEnglish`
    ].filter(Boolean).join('\n');
  };

  const buildMailtoUrl = () => {
    const subject = encodeURIComponent(`[TonyEnglish] Đăng ký học thử & Tư vấn: ${selectedCourseTitle} - ${fullName.trim() || phone.trim()}`);
    const body = encodeURIComponent(buildRegistrationMessage());
    return `mailto:${CONTACT_EMAIL}?subject=${subject}&body=${body}`;
  };

  const handleSubmitRegistration = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!fullName.trim() || !phone.trim()) {
      alert('Vui lòng nhập Họ tên và Số điện thoại / Zalo để TonyEnglish liên hệ cấp tài khoản học thử nhé!');
      return;
    }

    setIsSubmitting(true);
    try {
      // 1. Gửi email tự động qua FormSubmit AJAX tới tranhuyton@gmail.com
      try {
        await fetch(`https://formsubmit.co/ajax/${CONTACT_EMAIL}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          body: JSON.stringify({
            _subject: `[TonyEnglish Ads] Đăng ký học thử: ${selectedCourseTitle} - ${fullName.trim()} (${phone.trim()})`,
            Ho_va_ten: fullName.trim(),
            So_dien_thoai_Zalo: phone.trim(),
            Email_hoc_vien: studentEmail.trim() || 'Không điền',
            Khoa_hoc_dang_ky: selectedCourseTitle,
            Ghi_chu: note.trim() || 'Không có',
            Nguon: window.location.href
          })
        });
      } catch (ajaxErr) {
        console.warn('FormSubmit AJAX fallback to mailto:', ajaxErr);
      }

      setSubmittedSuccess(true);
      trackMetaPixelEvent('Lead', {
        content_name: selectedCourseTitle,
      });
      trackMetaPixelEvent('TonyEnglish_Lead', {
        course: selectedCourseTitle,
      }, true);
      // Mở luôn trình gửi email mặc định với nội dung điền sẵn để đảm bảo 100% gửi tới anh
      window.location.href = buildMailtoUrl();
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleChatZaloWithContent = async () => {
    trackMetaPixelEvent('Contact', {
      content_name: selectedCourseTitle,
      contact_method: 'Zalo',
    });
    trackMetaPixelEvent('TonyEnglish_ZaloContact', {
      course: selectedCourseTitle,
    }, true);
    const msg = buildRegistrationMessage();
    try {
      await navigator.clipboard.writeText(msg);
      setCopiedZaloText(true);
      setTimeout(() => setCopiedZaloText(false), 4000);
    } catch (e) {}
    window.open(CONTACT_ZALO_URL, '_blank');
  };

  const handleCopyPromoLink = async () => {
    const promoUrl = `${window.location.origin}/khoa-hoc`;
    try {
      await navigator.clipboard.writeText(promoUrl);
      setCopiedLink(true);
      setTimeout(() => setCopiedLink(false), 3000);
    } catch (e) {
      prompt('Copy đường link trang quảng cáo dưới đây:', promoUrl);
    }
  };

  const filteredPackages = FEATURED_PACKAGES.filter(pkg =>
    selectedCategory === 'all' ? true : pkg.category === selectedCategory
  );

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-800 flex flex-col relative selection:bg-[#2ab4e8]/20 selection:text-[#0a5482]">
      {/* TOP BAR THÔNG BÁO ƯU ĐÃI HỌC THỬ */}
      <div className="bg-gradient-to-r from-[#0a5482] via-[#0e6ba8] to-[#0a5482] text-white text-xs sm:text-sm py-2.5 px-4 text-center font-medium border-b border-white/10">
        <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-center gap-x-4 gap-y-1">
          <span className="inline-flex items-center gap-1.5 font-bold text-amber-300">
            <span>🎁</span> ĐẶC QUYỀN HỌC THỬ MIỄN PHÍ:
          </span>
          <span>Trải nghiệm thực tế các học phần & bài giảng trên hệ thống trước khi đăng ký chính thức!</span>
          <a
            href={CONTACT_ZALO_URL}
            target="_blank"
            rel="noreferrer"
            className="underline font-black text-cyan-200 hover:text-white transition"
          >
            Zalo/Hotline: {CONTACT_PHONE_DISPLAY} ➜
          </a>
        </div>
      </div>

      {/* NAVBAR */}
      <header className="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-40 shadow-xs">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 h-16 sm:h-20 flex items-center justify-between gap-3">
          <div
            onClick={() => onNavigate('home')}
            className="flex items-center gap-2.5 cursor-pointer hover:opacity-85 transition-opacity shrink-0"
            title="Về trang chủ TonyEnglish"
          >
            <img src="/logo-shield.png" alt="TonyEnglish" className="h-9 sm:h-11 w-auto object-contain" />
            <div className="flex flex-col leading-none">
              <div className="font-black text-[18px] sm:text-[23px] tracking-tight">
                <span className="text-[#2ab4e8]">TONY</span>
                <span className="text-[#0a5482]">ENGLISH</span>
              </div>
              <span className="text-[10px] font-bold text-slate-400 uppercase tracking-widest hidden sm:inline">
                Online Academy & AI Testing
              </span>
            </div>
          </div>

          <div className="hidden lg:flex items-center gap-6 text-sm font-bold text-slate-600">
            <a href="#cac-goi-hoc" className="hover:text-[#0a5482] transition">Các gói khóa học</a>
            <a href="#che-do-hoc-thu" className="hover:text-[#0a5482] transition">Trải nghiệm Học thử</a>
            <a href="#danh-sach-mon" className="hover:text-[#0a5482] transition">Danh mục môn học</a>
            <a href="#dang-ky-hoc-thu" className="hover:text-[#0a5482] transition">Đăng ký & Liên hệ</a>
          </div>

          <div className="flex items-center gap-2 sm:gap-2.5 shrink-0">
            <button
              onClick={handleCopyPromoLink}
              className="hidden md:inline-flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold border border-slate-200 bg-slate-50 hover:bg-slate-100 text-slate-600 transition"
              title="Copy đường link trang quảng cáo này để gắn vào bài chạy Ads Facebook"
            >
              <span>{copiedLink ? '✅ Đã copy link' : '🔗 Copy Link Ads'}</span>
            </button>

            <a
              href={CONTACT_ZALO_URL}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-1.5 bg-blue-600 hover:bg-blue-700 text-white text-xs sm:text-sm font-black px-3.5 py-2 sm:px-4 sm:py-2.5 rounded-xl shadow-md shadow-blue-600/20 transition active:scale-95"
            >
              <span>💬</span>
              <span>Zalo {CONTACT_PHONE_DISPLAY}</span>
            </a>

            <button
              onClick={() => scrollToRegister()}
              className="bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white text-xs sm:text-sm font-black px-3.5 py-2 sm:px-5 sm:py-2.5 rounded-xl shadow-md shadow-orange-500/25 transition active:scale-95 whitespace-nowrap"
            >
              🎁 Đăng ký học thử
            </button>
          </div>
        </div>
      </header>

      <main className="flex-1">
        {/* HERO BANNER */}
        <section className="relative overflow-hidden bg-gradient-to-br from-[#072f49] via-[#0a5482] to-[#0f172a] text-white pt-12 pb-20 md:pt-20 md:pb-28">
          <div className="absolute -top-24 -right-24 w-96 h-96 bg-[#2ab4e8]/20 rounded-full blur-3xl pointer-events-none" />
          <div className="absolute -bottom-24 -left-24 w-96 h-96 bg-amber-400/15 rounded-full blur-3xl pointer-events-none" />

          <div className="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">
              <div className="lg:col-span-7 text-center lg:text-left">
                <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-md border border-white/20 text-cyan-200 font-black text-xs sm:text-sm px-4 py-1.5 rounded-full mb-6">
                  <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
                  <span>HỆ THỐNG ĐÀO TẠO & LUYỆN THI QUỐC TẾ TÍCH HỢP AI 24/7</span>
                </div>

                <h1 className="text-3xl sm:text-5xl lg:text-[54px] font-black tracking-tight leading-[1.15] mb-6">
                  Đóng Gói Lộ Trình Học Thông Minh{' '}
                  <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#5ce1e6] via-[#2ab4e8] to-amber-300">
                    IELTS, Tiếng Anh & Cambridge IGCSE
                  </span>
                </h1>

                <p className="text-base sm:text-lg text-blue-100/90 font-medium leading-relaxed mb-8 max-w-2xl mx-auto lg:mx-0">
                  Kết hợp hoàn hảo giữa <b>Bài giảng tương tác song ngữ</b>, <b>Podcast học thuật</b>, <b>Trợ lý AI chấm chữa Speaking/Writing 24/7</b> và <b>Kho 1.800+ đề thi chuẩn quốc tế</b>. Cho phép học viên <b>vào Lớp Học Thử miễn phí</b> để trải nghiệm thực tế trước khi đăng ký!
                </p>

                {/* CTA BUTTONS */}
                <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-center lg:justify-start gap-3.5 mb-10">
                  <button
                    onClick={() => scrollToRegister()}
                    className="bg-gradient-to-r from-amber-400 to-orange-500 hover:from-amber-500 hover:to-orange-600 text-slate-950 font-black text-base px-7 py-4 rounded-2xl shadow-xl shadow-orange-500/30 transition transform hover:-translate-y-0.5 active:scale-95 flex items-center justify-center gap-2"
                  >
                    <span>🎁 Đăng Ký Học Thử Miễn Phí</span>
                    <span>➜</span>
                  </button>

                  <a
                    href={CONTACT_ZALO_URL}
                    target="_blank"
                    rel="noreferrer"
                    className="bg-[#0068ff] hover:bg-[#0057d6] text-white font-black text-base px-6 py-4 rounded-2xl shadow-xl shadow-blue-600/30 border border-white/20 transition transform hover:-translate-y-0.5 active:scale-95 flex items-center justify-center gap-2"
                  >
                    <span>💬 Nhắn Zalo: {CONTACT_PHONE_DISPLAY}</span>
                  </a>

                  <a
                    href={`tel:${CONTACT_PHONE}`}
                    className="bg-white/10 hover:bg-white/20 text-white font-bold text-base px-6 py-4 rounded-2xl border border-white/25 transition flex items-center justify-center gap-2"
                  >
                    <span>📞 Gọi: {CONTACT_PHONE_DISPLAY}</span>
                  </a>
                </div>

                {/* KEY STATS */}
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4 pt-6 border-t border-white/15">
                  <div className="bg-white/5 rounded-2xl p-3.5 border border-white/10">
                    <div className="text-2xl sm:text-3xl font-black text-[#5ce1e6]">14+</div>
                    <div className="text-xs text-blue-100/80 font-medium mt-0.5">Khóa học chuyên sâu</div>
                  </div>
                  <div className="bg-white/5 rounded-2xl p-3.5 border border-white/10">
                    <div className="text-2xl sm:text-3xl font-black text-amber-300">450+</div>
                    <div className="text-xs text-blue-100/80 font-medium mt-0.5">Bài giảng & Podcast</div>
                  </div>
                  <div className="bg-white/5 rounded-2xl p-3.5 border border-white/10">
                    <div className="text-2xl sm:text-3xl font-black text-emerald-300">1.800+</div>
                    <div className="text-xs text-blue-100/80 font-medium mt-0.5">Đề thi & Bài tập</div>
                  </div>
                  <div className="bg-white/5 rounded-2xl p-3.5 border border-white/10">
                    <div className="text-2xl sm:text-3xl font-black text-pink-300">24/7</div>
                    <div className="text-xs text-blue-100/80 font-medium mt-0.5">AI Tutor chấm chữa</div>
                  </div>
                </div>
              </div>

              {/* PREVIEW MOCKUP CARD: MINH HỌA GIAO DIỆN LỚP HỌC THỬ */}
              <div className="lg:col-span-5">
                <div className="bg-white text-slate-800 rounded-3xl shadow-2xl border border-white/20 overflow-hidden">
                  <div className="bg-slate-900 px-5 py-3.5 flex items-center justify-between text-white">
                    <div className="flex items-center gap-2">
                      <span className="w-3 h-3 rounded-full bg-rose-500" />
                      <span className="w-3 h-3 rounded-full bg-amber-400" />
                      <span className="w-3 h-3 rounded-full bg-emerald-400" />
                      <span className="text-xs font-bold text-slate-300 ml-2">Mô phỏng Lớp Học Thử TonyEnglish</span>
                    </div>
                    <span className="bg-amber-400/20 text-amber-300 border border-amber-400/40 text-[10px] font-black uppercase px-2.5 py-0.5 rounded-full">
                      🎁 Chế độ Học thử
                    </span>
                  </div>

                  <div className="p-5 sm:p-6 bg-slate-50">
                    <div className="flex items-center justify-between mb-3">
                      <div>
                        <p className="text-[11px] font-black uppercase tracking-wider text-[#0a5482]">Mục lục khóa học hiển thị đầy đủ 100%</p>
                        <h3 className="font-black text-slate-800 text-base">Học viên được mở thử học phần / bài giảng mẫu</h3>
                      </div>
                    </div>

                    <div className="space-y-2.5">
                      {/* Unlocked lecture */}
                      <div className="bg-white border-2 border-[#2ab4e8] rounded-xl p-3 flex items-center justify-between shadow-xs">
                        <div className="flex items-center gap-3 min-w-0">
                          <div className="w-6 h-6 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center font-black text-xs shrink-0">✓</div>
                          <div className="min-w-0">
                            <p className="text-xs font-black text-slate-800 truncate">Bài 1.1: Bài giảng tương tác + Audio Podcast</p>
                            <div className="flex items-center gap-1.5 mt-1">
                              <span className="text-[10px] bg-red-50 text-red-600 border border-red-100 px-1.5 py-0.5 rounded font-bold">▶ Video</span>
                              <span className="text-[10px] bg-emerald-50 text-emerald-700 border border-emerald-200 px-1.5 py-0.5 rounded font-bold">🎧 Podcast</span>
                              <span className="text-[10px] bg-sky-50 text-sky-700 border border-sky-200 px-1.5 py-0.5 rounded font-bold">🎯 Bài tập</span>
                            </div>
                          </div>
                        </div>
                        <span className="bg-emerald-500 text-white text-[10px] font-black px-2.5 py-1 rounded-lg shrink-0">HỌC THỬ NGAY</span>
                      </div>

                      {/* Unlocked lecture 2 */}
                      <div className="bg-white border border-indigo-200 rounded-xl p-3 flex items-center justify-between">
                        <div className="flex items-center gap-3 min-w-0">
                          <div className="w-6 h-6 rounded-full bg-indigo-100 text-indigo-600 flex items-center justify-center text-xs shrink-0">🤖</div>
                          <div className="min-w-0">
                            <p className="text-xs font-bold text-slate-800 truncate">Bài 1.2: Luyện phản xạ thực chiến cùng Trợ lý AI</p>
                            <span className="text-[10px] text-indigo-600 font-semibold">Đàm thoại & chấm chữa trực tiếp</span>
                          </div>
                        </div>
                        <span className="bg-indigo-50 text-indigo-700 border border-indigo-200 text-[10px] font-black px-2.5 py-1 rounded-lg shrink-0">MỞ THỬ</span>
                      </div>

                      {/* Grayed out locked lectures */}
                      <div className="bg-slate-200/75 border border-slate-200 rounded-xl p-3 flex items-center justify-between opacity-70 select-none">
                        <div className="flex items-center gap-3 min-w-0">
                          <div className="w-6 h-6 rounded-full bg-slate-300 text-slate-500 flex items-center justify-center text-xs shrink-0">🔒</div>
                          <div className="min-w-0">
                            <p className="text-xs font-medium text-slate-500 truncate">Bài 1.3: Chuyên đề nâng cao & Kho đề thực chiến</p>
                            <span className="text-[10px] text-slate-400">Mở khóa khi đăng ký gói học chính thức</span>
                          </div>
                        </div>
                        <span className="bg-slate-300 text-slate-600 text-[10px] font-bold px-2 py-0.5 rounded shrink-0">Khóa</span>
                      </div>

                      <div className="bg-slate-200/75 border border-slate-200 rounded-xl p-3 flex items-center justify-between opacity-60 select-none">
                        <div className="flex items-center gap-3 min-w-0">
                          <div className="w-6 h-6 rounded-full bg-slate-300 text-slate-500 flex items-center justify-center text-xs shrink-0">🔒</div>
                          <div className="min-w-0">
                            <p className="text-xs font-medium text-slate-500 truncate">Học phần 02: Luyện đề Past Papers & AI Chấm bài</p>
                            <span className="text-[10px] text-slate-400">Dành cho học viên chính thức</span>
                          </div>
                        </div>
                        <span className="bg-slate-300 text-slate-600 text-[10px] font-bold px-2 py-0.5 rounded shrink-0">Khóa</span>
                      </div>
                    </div>

                    <div className="mt-4 pt-4 border-t border-slate-200 flex items-center justify-between gap-2">
                      <div className="text-xs text-slate-600 font-medium">
                        💡 Học thử thực tế ngay trên tài khoản riêng của bạn!
                      </div>
                      <button
                        onClick={() => scrollToRegister()}
                        className="bg-[#0a5482] hover:bg-[#084266] text-white text-xs font-black px-3.5 py-2 rounded-xl transition shrink-0"
                      >
                        Nhận TK Học Thử ➜
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* SECTION: CÁC GÓI KHÓA HỌC NỔI BẬT */}
        <section id="cac-goi-hoc" className="py-16 md:py-24 max-w-7xl mx-auto px-4 sm:px-6">
          <div className="text-center max-w-3xl mx-auto mb-12">
            <span className="inline-block bg-blue-100 text-[#0a5482] font-black text-xs px-3.5 py-1.5 rounded-full uppercase tracking-wider mb-3">
              CÁC GÓI HỌC ONLINE ĐÓNG GÓI TRỌN BỘ
            </span>
            <h2 className="text-3xl sm:text-4xl font-black text-slate-800 tracking-tight mb-4">
              Chọn Gói Học Phù Hợp & Đăng Ký Học Thử Ngay
            </h2>
            <p className="text-slate-600 font-medium text-base">
              Tất cả các gói học đều được cấp tài khoản <b>Lớp Học Thử</b> để học viên xem toàn bộ lộ trình và học thử các bài giảng mẫu trước khi quyết định.
            </p>

            {/* FILTER TABS */}
            <div className="inline-flex flex-wrap items-center justify-center gap-2 bg-slate-200/70 p-1.5 rounded-2xl mt-8">
              <button
                onClick={() => setSelectedCategory('all')}
                className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-black transition ${
                  selectedCategory === 'all' ? 'bg-[#0a5482] text-white shadow-sm' : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                🌟 Tất cả gói học ({FEATURED_PACKAGES.length})
              </button>
              <button
                onClick={() => setSelectedCategory('english')}
                className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-black transition ${
                  selectedCategory === 'english' ? 'bg-[#0a5482] text-white shadow-sm' : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                🔥 IELTS & Tiếng Anh Giao Tiếp / Nền Tảng
              </button>
              <button
                onClick={() => setSelectedCategory('igcse')}
                className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-black transition ${
                  selectedCategory === 'igcse' ? 'bg-[#0a5482] text-white shadow-sm' : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                🌍 Chương Trình Quốc Tế Cambridge IGCSE
              </button>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-7">
            {filteredPackages.map(pkg => (
              <div
                key={pkg.id}
                className="bg-white rounded-3xl border border-slate-200/90 shadow-sm hover:shadow-2xl transition-all duration-300 flex flex-col overflow-hidden group"
              >
                {/* Card Header */}
                <div className={`bg-gradient-to-br ${pkg.gradient} p-6 text-white relative`}>
                  <div className="flex items-center justify-between gap-2 mb-4">
                    <span className="bg-white/20 backdrop-blur-md text-white text-[11px] font-black uppercase tracking-wider px-3 py-1 rounded-full border border-white/25">
                      {pkg.badge}
                    </span>
                    <span className="text-3xl">{pkg.icon}</span>
                  </div>
                  <h3 className="text-xl font-black leading-snug mb-2">{pkg.title}</h3>
                  <p className="text-xs text-white/85 font-medium leading-relaxed">{pkg.subtitle}</p>
                </div>

                {/* Stats bar */}
                <div className="bg-slate-50 px-6 py-3 border-b border-slate-100 flex flex-wrap gap-2">
                  {pkg.stats.map((st, idx) => (
                    <span
                      key={idx}
                      className={`text-[11px] font-bold px-2.5 py-1 rounded-lg border ${pkg.accentColor}`}
                    >
                      {st}
                    </span>
                  ))}
                </div>

                {/* Highlights */}
                <div className="p-6 flex-1 flex flex-col justify-between">
                  <ul className="space-y-3 mb-6">
                    {pkg.highlights.map((item, i) => (
                      <li key={i} className="flex items-start gap-2.5 text-sm text-slate-600 font-medium leading-snug">
                        <span className="text-emerald-500 font-black mt-0.5 shrink-0">✔</span>
                        <span>{item}</span>
                      </li>
                    ))}
                  </ul>

                  <div className="pt-5 border-t border-slate-100">
                    <div className="flex items-center justify-between mb-4 bg-amber-50/70 border border-amber-200/80 rounded-2xl px-4 py-3">
                      <div>
                        <span className="text-[11px] font-bold text-slate-500 uppercase block">Học phí gói khóa học</span>
                        <span className="text-lg font-black text-[#0a5482]">Liên hệ tư vấn</span>
                      </div>
                      <span className="bg-amber-100 text-amber-800 text-[11px] font-black px-2.5 py-1 rounded-full border border-amber-300">
                        🎁 Có Học Thử
                      </span>
                    </div>

                    <div className="grid grid-cols-2 gap-2.5">
                      <button
                        onClick={() => scrollToRegister(pkg.title)}
                        className="bg-[#0a5482] hover:bg-[#084266] text-white font-black text-xs sm:text-sm py-3 px-3 rounded-xl shadow-md transition active:scale-95 flex items-center justify-center gap-1.5"
                      >
                        <span>🎁 Đăng ký học thử</span>
                      </button>
                      <a
                        href={CONTACT_ZALO_URL}
                        target="_blank"
                        rel="noreferrer"
                        className="bg-emerald-600 hover:bg-emerald-700 text-white font-black text-xs sm:text-sm py-3 px-3 rounded-xl shadow-md transition active:scale-95 flex items-center justify-center gap-1.5"
                      >
                        <span>💬 Nhắn Zalo</span>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* SECTION: QUY TRÌNH HỌC THỬ 3 BƯỚC */}
        <section id="che-do-hoc-thu" className="py-16 bg-white border-y border-slate-200">
          <div className="max-w-7xl mx-auto px-4 sm:px-6">
            <div className="text-center max-w-3xl mx-auto mb-12">
              <span className="inline-block bg-amber-100 text-amber-800 font-black text-xs px-3.5 py-1.5 rounded-full uppercase tracking-wider mb-3">
                TRẢI NGHIỆM TRƯỚC - ĐĂNG KÝ SAU
              </span>
              <h2 className="text-3xl font-black text-slate-800 mb-3">
                Chế Độ "Lớp Học Thử" Của TonyEnglish Hoạt Động Thế Nào?
              </h2>
              <p className="text-slate-600 font-medium">
                Phụ huynh và học viên hoàn toàn yên tâm kiểm chứng chất lượng bài giảng, âm thanh Podcast và công nghệ AI trước khi đóng học phí.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="bg-slate-50 rounded-3xl p-7 border border-slate-200/80 relative">
                <div className="w-12 h-12 rounded-2xl bg-[#0a5482] text-white font-black text-xl flex items-center justify-center mb-5 shadow-md">
                  01
                </div>
                <h3 className="text-lg font-black text-slate-800 mb-2">Gửi Yêu Cầu Đăng Ký Học Thử</h3>
                <p className="text-sm text-slate-600 font-medium leading-relaxed">
                  Điền thông tin vào form bên dưới để gửi Email trực tiếp cho thầy Tôn hoặc nhắn/gọi ngay qua <b>Zalo {CONTACT_PHONE_DISPLAY}</b> môn học bạn muốn trải nghiệm.
                </p>
              </div>

              <div className="bg-slate-50 rounded-3xl p-7 border border-slate-200/80 relative">
                <div className="w-12 h-12 rounded-2xl bg-[#2ab4e8] text-white font-black text-xl flex items-center justify-center mb-5 shadow-md">
                  02
                </div>
                <h3 className="text-lg font-black text-slate-800 mb-2">Vào Lớp Học Thử Trên Hệ Thống</h3>
                <p className="text-sm text-slate-600 font-medium leading-relaxed">
                  Bạn được cấp tài khoản vào <b>Lớp Học Thử</b>: nhìn thấy <b>100% danh mục học phần & bài giảng</b> của cả khóa học, và được mở khóa học thử một số học phần hoặc bài giảng tiêu biểu.
                </p>
              </div>

              <div className="bg-slate-50 rounded-3xl p-7 border border-slate-200/80 relative">
                <div className="w-12 h-12 rounded-2xl bg-emerald-600 text-white font-black text-xl flex items-center justify-center mb-5 shadow-md">
                  03
                </div>
                <h3 className="text-lg font-black text-slate-800 mb-2">Mở Khóa Toàn Bộ Khóa Học Chính Thức</h3>
                <p className="text-sm text-slate-600 font-medium leading-relaxed">
                  Sau khi học thử ưng ý, bạn liên hệ Zalo <b>{CONTACT_PHONE_DISPLAY}</b> để nhận tư vấn học phí ưu đãi và mở khóa toàn bộ các bài giảng màu xám còn lại cùng kho đề thi.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* SECTION: DANH MỤC TẤT CẢ MÔN HỌC TRÊN HỆ THỐNG */}
        {dbCourses.length > 0 && (
          <section id="danh-sach-mon" className="py-16 max-w-7xl mx-auto px-4 sm:px-6">
            <div className="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-4">
              <div>
                <span className="text-xs font-black uppercase tracking-widest text-[#0a5482] block mb-2">
                  DANH SÁCH KHÓA HỌC TRÊN HỆ THỐNG
                </span>
                <h2 className="text-2xl sm:text-3xl font-black text-slate-800">
                  Tất Cả {dbCourses.length} Khóa Học Đang Mở Lớp Học Thử
                </h2>
              </div>
              <a
                href={CONTACT_ZALO_URL}
                target="_blank"
                rel="noreferrer"
                className="text-sm font-black text-[#0a5482] hover:underline flex items-center gap-1"
              >
                <span>📞 Cần tư vấn chọn môn? Gọi/Zalo {CONTACT_PHONE_DISPLAY}</span>
                <span>➜</span>
              </a>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
              {dbCourses.map((course, index) => {
                const isIgcse = (course.title || '').toLowerCase().includes('igcse');
                const isIelts = (course.title || '').toLowerCase().includes('ielts');
                return (
                  <div
                    key={course.id}
                    className="bg-white rounded-2xl border border-slate-200 p-5 hover:border-[#2ab4e8] hover:shadow-lg transition-all flex flex-col justify-between"
                  >
                    <div>
                      <div className="flex items-center justify-between gap-2 mb-3">
                        <span
                          className={`text-[10px] font-black uppercase px-2.5 py-1 rounded-full ${
                            isIelts
                              ? 'bg-rose-50 text-rose-700 border border-rose-200'
                              : isIgcse
                                ? 'bg-indigo-50 text-indigo-700 border border-indigo-200'
                                : 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                          }`}
                        >
                          {isIelts ? 'IELTS' : isIgcse ? 'Cambridge IGCSE' : 'Tiếng Anh'}
                        </span>
                        <span className="text-xs font-bold text-slate-400">#{(index + 1).toString().padStart(2, '0')}</span>
                      </div>

                      <h4 className="font-black text-slate-800 text-base mb-2 leading-snug">{course.title}</h4>
                      <p className="text-xs text-slate-500 font-medium mb-4">
                        Bài giảng tương tác + Kho đề luyện + Lớp học thử miễn phí
                      </p>
                    </div>

                    <div className="pt-3 border-t border-slate-100 flex items-center justify-between gap-2">
                      <div>
                        <span className="text-[10px] font-bold text-slate-400 uppercase block">Học phí</span>
                        <span className="text-sm font-black text-[#0a5482]">Liên hệ</span>
                      </div>
                      <button
                        onClick={() => scrollToRegister(course.title)}
                        className="bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-300 font-black text-xs px-3 py-2 rounded-xl transition active:scale-95"
                      >
                        🎁 Học thử ngay
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          </section>
        )}

        {/* SECTION: FORM ĐĂNG KÝ HỌC THỬ & LIÊN HỆ TRỰC TIẾP */}
        <section id="dang-ky-hoc-thu" className="py-16 md:py-24 bg-gradient-to-b from-slate-100 to-slate-200/70">
          <div className="max-w-6xl mx-auto px-4 sm:px-6">
            <div className="bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden grid grid-cols-1 lg:grid-cols-12">
              {/* LEFT COLUMN: DIRECT CONTACT INFO */}
              <div className="lg:col-span-5 bg-gradient-to-br from-[#0a5482] via-[#083b5c] to-slate-900 text-white p-8 sm:p-10 flex flex-col justify-between">
                <div>
                  <span className="inline-block bg-amber-400 text-slate-950 font-black text-xs px-3 py-1 rounded-full uppercase tracking-wider mb-4">
                    HỖ TRỢ TƯ VẤN & CẤP TÀI KHOẢN NHANH
                  </span>
                  <h2 className="text-2xl sm:text-3xl font-black leading-tight mb-4">
                    Đăng Ký Học Thử & Nhận Báo Giá Khóa Học
                  </h2>
                  <p className="text-blue-100/85 text-sm font-medium leading-relaxed mb-8">
                    Anh/chị phụ huynh và các bạn học viên có thể điền form đăng ký bên cạnh để gửi Email trực tiếp, hoặc <b>nhắn tin / gọi điện ngay qua Zalo</b> để được kích hoạt Lớp Học Thử trong 5 phút!
                  </p>

                  <div className="space-y-4">
                    {/* ZALO / PHONE CARD */}
                    <a
                      href={CONTACT_ZALO_URL}
                      target="_blank"
                      rel="noreferrer"
                      className="flex items-center gap-4 bg-white/10 hover:bg-white/15 border border-white/20 p-4 rounded-2xl transition group"
                    >
                      <div className="w-12 h-12 rounded-2xl bg-[#0068ff] flex items-center justify-center text-2xl shrink-0 shadow-lg">
                        💬
                      </div>
                      <div className="min-w-0">
                        <div className="text-xs font-bold text-cyan-300 uppercase tracking-wider">Nhắn tin Zalo trực tiếp</div>
                        <div className="text-lg font-black text-white group-hover:text-amber-300 transition">
                          {CONTACT_PHONE_DISPLAY}
                        </div>
                        <div className="text-xs text-blue-200">Bấm để mở Zalo chat ngay (Mr. Tôn)</div>
                      </div>
                    </a>

                    {/* CALL CARD */}
                    <a
                      href={`tel:${CONTACT_PHONE}`}
                      className="flex items-center gap-4 bg-white/10 hover:bg-white/15 border border-white/20 p-4 rounded-2xl transition group"
                    >
                      <div className="w-12 h-12 rounded-2xl bg-emerald-500 flex items-center justify-center text-2xl shrink-0 shadow-lg">
                        📞
                      </div>
                      <div className="min-w-0">
                        <div className="text-xs font-bold text-emerald-300 uppercase tracking-wider">Hotline tư vấn khóa học</div>
                        <div className="text-lg font-black text-white group-hover:text-emerald-300 transition">
                          {CONTACT_PHONE_DISPLAY}
                        </div>
                        <div className="text-xs text-blue-200">Hỗ trợ tư vấn lộ trình & báo giá chi tiết</div>
                      </div>
                    </a>

                    {/* EMAIL CARD */}
                    <a
                      href={buildMailtoUrl()}
                      className="flex items-center gap-4 bg-white/10 hover:bg-white/15 border border-white/20 p-4 rounded-2xl transition group"
                    >
                      <div className="w-12 h-12 rounded-2xl bg-amber-500 flex items-center justify-center text-2xl shrink-0 shadow-lg">
                        ✉️
                      </div>
                      <div className="min-w-0">
                        <div className="text-xs font-bold text-amber-300 uppercase tracking-wider">Email nhận đăng ký học thử</div>
                        <div className="text-base font-black text-white truncate group-hover:text-amber-300 transition">
                          {CONTACT_EMAIL}
                        </div>
                        <div className="text-xs text-blue-200">Gửi email yêu cầu mở tài khoản học thử</div>
                      </div>
                    </a>
                  </div>
                </div>

                <div className="mt-8 pt-6 border-t border-white/15 text-xs text-blue-200/80 space-y-1.5">
                  <p>✔ Mở tài khoản học thử miễn phí các học phần / bài giảng mẫu</p>
                  <p>✔ Học phí linh hoạt theo từng môn hoặc combo trọn gói: <b>Liên hệ</b></p>
                  <p>✔ Học mọi lúc mọi nơi trên Máy tính, iPad và Điện thoại</p>
                </div>
              </div>

              {/* RIGHT COLUMN: REGISTRATION FORM */}
              <div className="lg:col-span-7 p-8 sm:p-10">
                <div className="mb-6">
                  <h3 className="text-2xl font-black text-slate-800 mb-1">
                    🎁 Form Đăng Ký Nhận Tài Khoản Học Thử
                  </h3>
                  <p className="text-sm text-slate-500 font-medium">
                    Điền thông tin bên dưới rồi chọn <b>Gửi Email</b> hoặc <b>Nhắn qua Zalo {CONTACT_PHONE_DISPLAY}</b>.
                  </p>
                </div>

                <form onSubmit={handleSubmitRegistration} className="space-y-4">
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <label className="block text-xs font-black text-slate-600 uppercase tracking-wider mb-1.5">
                        Họ và tên Học viên / Phụ huynh *
                      </label>
                      <input
                        type="text"
                        required
                        value={fullName}
                        onChange={(e) => setFullName(e.target.value)}
                        placeholder="VD: Nguyễn Minh Anh"
                        className="w-full border border-slate-300 rounded-xl px-4 py-3 text-sm font-medium outline-none focus:ring-2 focus:ring-[#0a5482] bg-slate-50 focus:bg-white transition"
                      />
                    </div>

                    <div>
                      <label className="block text-xs font-black text-slate-600 uppercase tracking-wider mb-1.5">
                        Số điện thoại / Zalo liên hệ *
                      </label>
                      <input
                        type="tel"
                        required
                        value={phone}
                        onChange={(e) => setPhone(e.target.value)}
                        placeholder="VD: 0901234567"
                        className="w-full border border-slate-300 rounded-xl px-4 py-3 text-sm font-medium outline-none focus:ring-2 focus:ring-[#0a5482] bg-slate-50 focus:bg-white transition"
                      />
                    </div>
                  </div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <label className="block text-xs font-black text-slate-600 uppercase tracking-wider mb-1.5">
                        Email nhận tài khoản học thử
                      </label>
                      <input
                        type="email"
                        value={studentEmail}
                        onChange={(e) => setStudentEmail(e.target.value)}
                        placeholder="VD: hocvien@gmail.com"
                        className="w-full border border-slate-300 rounded-xl px-4 py-3 text-sm font-medium outline-none focus:ring-2 focus:ring-[#0a5482] bg-slate-50 focus:bg-white transition"
                      />
                    </div>

                    <div>
                      <label className="block text-xs font-black text-slate-600 uppercase tracking-wider mb-1.5">
                        Khóa học muốn đăng ký học thử *
                      </label>
                      <select
                        value={selectedCourseTitle}
                        onChange={(e) => setSelectedCourseTitle(e.target.value)}
                        className="w-full border border-slate-300 rounded-xl px-4 py-3 text-sm font-bold text-slate-800 outline-none focus:ring-2 focus:ring-[#0a5482] bg-slate-50 focus:bg-white transition"
                      >
                        <optgroup label="Các Gói Combo Nổi Bật">
                          {FEATURED_PACKAGES.map(pkg => (
                            <option key={pkg.id} value={pkg.title}>{pkg.title}</option>
                          ))}
                        </optgroup>
                        {dbCourses.length > 0 && (
                          <optgroup label="Từng Môn Học Cụ Thể">
                            {dbCourses.map(c => (
                              <option key={c.id} value={c.title}>{c.title}</option>
                            ))}
                          </optgroup>
                        )}
                      </select>
                    </div>
                  </div>

                  <div>
                    <label className="block text-xs font-black text-slate-600 uppercase tracking-wider mb-1.5">
                      Ghi chú thêm (Lớp đang học / Mục tiêu / Học phần muốn học thử)
                    </label>
                    <textarea
                      rows={3}
                      value={note}
                      onChange={(e) => setNote(e.target.value)}
                      placeholder="VD: Em đang học lớp 9 chương trình Cambridge, muốn đăng ký học thử môn IGCSE Economics & Science..."
                      className="w-full border border-slate-300 rounded-xl px-4 py-3 text-sm font-medium outline-none focus:ring-2 focus:ring-[#0a5482] bg-slate-50 focus:bg-white transition resize-none"
                    />
                  </div>

                  {submittedSuccess && (
                    <div className="bg-emerald-50 border border-emerald-200 rounded-2xl p-4 text-emerald-900 text-xs sm:text-sm font-medium space-y-2 animate-in fade-in">
                      <div className="font-black text-emerald-700 flex items-center gap-1.5">
                        <span>✅</span>
                        <span>Đã tạo yêu cầu đăng ký học thử thành công!</span>
                      </div>
                      <p>
                        Hệ thống đã gửi thông tin tới email <b>{CONTACT_EMAIL}</b>. Để được cấp tài khoản học thử nhanh nhất ngay lập tức, bạn có thể bấm nút <b>Nhắn Zalo {CONTACT_PHONE_DISPLAY}</b> bên dưới nhé!
                      </p>
                    </div>
                  )}

                  {copiedZaloText && (
                    <div className="bg-blue-50 border border-blue-200 rounded-xl p-3 text-blue-800 text-xs font-bold">
                      📋 Đã tự động copy nội dung đăng ký! Bạn chỉ cần nhấn "Dán (Paste)" vào khung chat Zalo {CONTACT_PHONE_DISPLAY}.
                    </div>
                  )}

                  <div className="pt-2 flex flex-col sm:flex-row gap-3">
                    <button
                      type="submit"
                      disabled={isSubmitting}
                      className="flex-1 bg-gradient-to-r from-[#0a5482] to-[#0e6ba8] hover:from-[#084266] hover:to-[#0a5482] text-white font-black text-sm py-4 px-5 rounded-2xl shadow-lg shadow-blue-900/20 transition active:scale-95 disabled:opacity-50 flex items-center justify-center gap-2"
                    >
                      <span>✉️</span>
                      <span>{isSubmitting ? 'Đang gửi Email...' : 'Gửi Email Đăng Ký Học Thử'}</span>
                    </button>

                    <button
                      type="button"
                      onClick={handleChatZaloWithContent}
                      className="flex-1 bg-[#0068ff] hover:bg-[#0057d6] text-white font-black text-sm py-4 px-5 rounded-2xl shadow-lg shadow-blue-600/25 transition active:scale-95 flex items-center justify-center gap-2"
                    >
                      <span>💬</span>
                      <span>Nhắn Zalo: {CONTACT_PHONE_DISPLAY}</span>
                    </button>
                  </div>

                  <div className="text-center pt-1">
                    <a
                      href={`tel:${CONTACT_PHONE}`}
                      className="inline-flex items-center gap-1.5 text-xs font-black text-emerald-700 hover:text-emerald-800 hover:underline"
                    >
                      <span>📞 Hoặc gọi trực tiếp Hotline: {CONTACT_PHONE_DISPLAY} (Mr. Trần Huy Tôn)</span>
                    </a>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* FOOTER */}
      <footer className="bg-slate-900 text-slate-400 py-10 border-t border-slate-800 pb-24 md:pb-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col md:flex-row justify-between items-center gap-6">
          <div className="flex items-center gap-3">
            <img src="/logo-shield.png" alt="TonyEnglish" className="h-8 w-auto object-contain" />
            <div>
              <div className="font-black text-lg tracking-tight text-white">TONYENGLISH ONLINE ACADEMY</div>
              <div className="text-xs text-slate-400">Hotline / Zalo: {CONTACT_PHONE_DISPLAY} • Email: {CONTACT_EMAIL}</div>
            </div>
          </div>
          <div className="flex items-center gap-4 text-xs font-bold">
            <button onClick={() => onNavigate('home')} className="text-slate-300 hover:text-white transition">
              Trang chủ hệ thống
            </button>
            <span>•</span>
            <a href={CONTACT_ZALO_URL} target="_blank" rel="noreferrer" className="text-cyan-400 hover:text-cyan-300 transition">
              Zalo {CONTACT_PHONE_DISPLAY}
            </a>
            <span>•</span>
            <a href={`tel:${CONTACT_PHONE}`} className="text-emerald-400 hover:text-emerald-300 transition">
              Gọi {CONTACT_PHONE_DISPLAY}
            </a>
          </div>
        </div>
      </footer>

      {/* STICKY MOBILE BOTTOM BAR (CỰC KỲ HIỆU QUẢ CHO KHÁCH TỪ QUẢNG CÁO FACEBOOK TRÊN ĐIỆN THOẠI) */}
      <div className="fixed bottom-0 inset-x-0 z-50 bg-white/95 backdrop-blur-md border-t border-slate-200 p-2.5 flex items-center gap-2 md:hidden shadow-[0_-4px_20px_rgba(0,0,0,0.08)]">
        <a
          href={`tel:${CONTACT_PHONE}`}
          className="flex-1 bg-emerald-600 text-white font-black text-xs py-3 rounded-xl flex items-center justify-center gap-1 shadow-sm active:scale-95"
        >
          <span>📞</span>
          <span>Gọi {CONTACT_PHONE_DISPLAY}</span>
        </a>
        <a
          href={CONTACT_ZALO_URL}
          target="_blank"
          rel="noreferrer"
          className="flex-1 bg-[#0068ff] text-white font-black text-xs py-3 rounded-xl flex items-center justify-center gap-1 shadow-sm active:scale-95"
        >
          <span>💬</span>
          <span>Zalo Tư Vấn</span>
        </a>
        <button
          onClick={() => scrollToRegister()}
          className="flex-1 bg-gradient-to-r from-amber-500 to-orange-500 text-white font-black text-xs py-3 rounded-xl flex items-center justify-center gap-1 shadow-sm active:scale-95"
        >
          <span>🎁</span>
          <span>Học Thử</span>
        </button>
      </div>
    </div>
  );
}
