import React, { useEffect, useState } from 'react';
import { Link, useParams, useLocation } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import { encryptLegacyPass, fixLegacyHtmlContent, updatePageSeo } from '../lib/utils';

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

const FEATURED_ONLINE_PACKAGES: PackageCardItem[] = [
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
      'Có lớp học thử miễn phí các học phần đầu để trải nghiệm trước khi đăng ký',
    ],
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
      'Học thử miễn phí các bài giảng mẫu trong từng học phần',
    ],
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
      'Phù hợp cho học sinh THCS, THPT, sinh viên và người mất gốc cần lấy lại nền tảng nhanh',
    ],
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
      'AI chấm điểm câu hỏi tự luận bám sát Marking Scheme chuẩn Cambridge',
    ],
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
      'Mở học thử các bài giảng đầu mỗi chương để học sinh trải nghiệm phương pháp học',
    ],
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
      'Hỗ trợ lộ trình cá nhân hóa và lịch báo bài tự động theo mục tiêu kỳ thi',
    ],
  },
];

export const CoursesPage: React.FC<{ forcedMode?: 'online' | 'offline' }> = ({ forcedMode }) => {
  const { slug } = useParams<{ slug?: string }>();
  const location = useLocation();
  const { lang, t, user, options } = useApp();

  const isOnlineView =
    forcedMode === 'online' ||
    slug?.toLowerCase() === 'online' ||
    location.pathname.toLowerCase().includes('/courses/online') ||
    location.pathname.toLowerCase().startsWith('/khoa-hoc') ||
    location.pathname.toLowerCase().startsWith('/hoc-thu') ||
    location.pathname.toLowerCase().startsWith('/dang-ky') ||
    location.pathname.toLowerCase().startsWith('/promo');

  const [allCategories, setAllCategories] = useState<any[]>([]);
  const [currentCourse, setCurrentCourse] = useState<any | null>(null);
  const [lectureCount, setLectureCount] = useState(0);
  const [openParentId, setOpenParentId] = useState<number | null>(null);
  const [mobileCateOpen, setMobileCateOpen] = useState(false);

  // Offline Syllabus popup & Registration form state
  const [showSyllabusModal, setShowSyllabusModal] = useState(false);
  const [showJoinForm, setShowJoinForm] = useState(false);

  const [regName, setRegName] = useState('');
  const [regBirthday, setRegBirthday] = useState('');
  const [regGender, setRegGender] = useState('1');
  const [regPhone, setRegPhone] = useState('');
  const [regEmail, setRegEmail] = useState('');
  const [regCity, setRegCity] = useState('');
  const [regWork, setRegWork] = useState('');
  const [regExtraCourses, setRegExtraCourses] = useState<number[]>([]);
  const [regMessage, setRegMessage] = useState<{ text: string; isError: boolean } | null>(null);
  const [regSubmitting, setRegSubmitting] = useState(false);

  // Online Courses & Trial Form state
  const [dbOnlineCourses, setDbOnlineCourses] = useState<any[]>([]);
  const [selectedOnlineCat, setSelectedOnlineCat] = useState<'all' | 'english' | 'igcse'>('all');
  const [onlineFullName, setOnlineFullName] = useState('');
  const [onlinePhone, setOnlinePhone] = useState('');
  const [onlineStudentEmail, setOnlineStudentEmail] = useState('');
  const [selectedOnlineCourseTitle, setSelectedOnlineCourseTitle] = useState('IELTS Premium Toàn Diện (4 Kỹ Năng)');
  const [onlineNote, setOnlineNote] = useState('');
  const [isOnlineSubmitting, setIsOnlineSubmitting] = useState(false);
  const [onlineSubmittedSuccess, setOnlineSubmittedSuccess] = useState(false);
  const [copiedZaloText, setCopiedZaloText] = useState(false);

  useEffect(() => {
    const params = new URLSearchParams(location.search);
    const catParam = params.get('cat');
    if (catParam === 'english' || catParam === 'igcse') {
      setSelectedOnlineCat(catParam);
    } else if (catParam === 'all') {
      setSelectedOnlineCat('all');
    }
  }, [location.search]);

  useEffect(() => {
    async function loadCourses() {
      const [offlineRes, onlineRes] = await Promise.all([
        supabase
          .from('te_course_category')
          .select('*')
          .eq('deleted', 0)
          .eq('cc_status', 1)
          .order('cc_order', { ascending: true }),
        supabase
          .from('courses')
          .select('id, title, type, order_index')
          .order('order_index', { ascending: true }),
      ]);

      if (onlineRes.data) {
        setDbOnlineCourses(onlineRes.data);
      }

      if (offlineRes.data) {
        setAllCategories(offlineRes.data);
        if (slug && slug.toLowerCase() !== 'online') {
          const cleanSlug = decodeURIComponent(slug)
            .trim()
            .replace(/\.html$/i, '');
          const found = offlineRes.data.find((c: any) => (c.cc_name_url || '').trim() === cleanSlug);
          if (found) {
            setCurrentCourse(found);
            setOpenParentId(found.cc_parent === 0 ? found.cc_id : found.cc_parent);
            const { count } = await supabase
              .from('te_lecture')
              .select('lecture_id', { count: 'exact', head: true })
              .eq('deleted', 0)
              .eq('lecture_status', 1)
              .eq('cc_id', found.cc_id);
            setLectureCount(count || 0);
          }
        } else {
          setCurrentCourse(null);
          const firstParent = offlineRes.data.find((c: any) => c.cc_parent === 0 && c.cc_homedisplay === 1);
          if (firstParent) setOpenParentId(firstParent.cc_id);
        }
      }
    }
    loadCourses();
    setShowJoinForm(false);
    setRegMessage(null);
  }, [slug]);

  // Only show homeParents (cc_homedisplay === 1) for Offline Courses; hide extraParents
  const homeParents = allCategories.filter((c) => Number(c.cc_parent) === 0 && Number(c.cc_homedisplay) === 1);
  const subCategories = (parentId: number) =>
    allCategories.filter((c) => Number(c.cc_parent) === Number(parentId));

  const hasSubCategories = currentCourse
    ? allCategories.some((c) => Number(c.cc_parent) === Number(currentCourse.cc_id))
    : false;

  const handleJoinSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setRegMessage(null);
    if (!currentCourse) return;

    if (user) {
      setRegSubmitting(true);
      const coursesToJoin = [currentCourse.cc_id, ...regExtraCourses];
      for (const cid of coursesToJoin) {
        await supabase.from('te_user_courses').insert({
          user_id: user.user_id,
          cc_id: cid,
        });
      }
      setRegSubmitting(false);
      setRegMessage({
        text: `${t('Thank you')}! ${t('We will contact you soon about the Time-table and Avaibility of The course.')}`,
        isError: false,
      });
      return;
    }

    if (!regName.trim() || !regEmail.trim() || !regPhone.trim() || !regCity.trim()) {
      setRegMessage({
        text: `${t('Please complete information on the items marked with')} (*) !`,
        isError: true,
      });
      return;
    }

    setRegSubmitting(true);
    const salt = String(Math.floor(Math.random() * 900) + 100);
    const cleanUsername = regName.toLowerCase().replace(/[^a-z0-9]/g, '') + salt;
    const now = Math.floor(Date.now() / 1000);

    const { data: maxRow } = await supabase
      .from('te_user')
      .select('user_id')
      .order('user_id', { ascending: false })
      .limit(1);
    const nextUserId = maxRow && maxRow.length > 0 ? Number(maxRow[0].user_id) + 1 : 1000;

    const { error: uErr } = await supabase.from('te_user').insert({
      user_id: nextUserId,
      user_name: cleanUsername,
      user_fullname: regName.trim(),
      user_salt: salt,
      user_pass: encryptLegacyPass(salt, '123456'),
      user_created_at: now,
      user_phone: regPhone.trim(),
      user_email: regEmail.trim(),
      user_address: regCity.trim(),
      user_birthday: regBirthday.trim(),
      user_gender: parseInt(regGender, 10),
      user_job: regWork.trim(),
      user_status: 1,
      user_active: 1,
      deleted: 0,
    });

    if (uErr) {
      setRegSubmitting(false);
      setRegMessage({ text: uErr.message, isError: true });
      return;
    }

    const { data: maxUcRow } = await supabase
      .from('te_user_courses')
      .select('uc_id')
      .order('uc_id', { ascending: false })
      .limit(1);
    let nextUcId = maxUcRow && maxUcRow.length > 0 ? Number(maxUcRow[0].uc_id) + 1 : 10000;

    const coursesToJoin = Array.from(new Set([currentCourse.cc_id, ...regExtraCourses]));
    for (const cid of coursesToJoin) {
      await supabase.from('te_user_courses').insert({
        uc_id: nextUcId++,
        user_id: nextUserId,
        cc_id: cid,
      });
    }

    setRegSubmitting(false);
    setRegMessage({
      text: `${t('Thank you')}! ${t('We will contact you soon about the Time-table and Avaibility of The course.')}`,
      isError: false,
    });
  };

  // Online Trial Registration Helpers
  const scrollToOnlineRegister = (courseName?: string) => {
    if (courseName) {
      setSelectedOnlineCourseTitle(courseName);
    }
    setOnlineSubmittedSuccess(false);
    const el = document.getElementById('dang-ky-hoc-thu');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  const buildOnlineRegistrationMessage = () => {
    return [
      `🎁 ĐĂNG KÝ KHÓA HỌC ONLINE & HỌC THỬ - TONYENGLISH`,
      `--------------------------------------------`,
      `👤 Họ và tên: ${onlineFullName.trim() || '(Chưa nhập)'}`,
      `📞 Số điện thoại / Zalo: ${onlinePhone.trim() || '(Chưa nhập)'}`,
      `✉️ Email nhận tài khoản học thử: ${onlineStudentEmail.trim() || '(Chưa nhập)'}`,
      `📚 Khóa học Online quan tâm: ${selectedOnlineCourseTitle}`,
      onlineNote.trim() ? `📝 Ghi chú / Trình độ hiện tại: ${onlineNote.trim()}` : '',
      `--------------------------------------------`,
      `🌐 Gửi từ trang Khóa học Online TonyEnglish.vn`,
    ]
      .filter(Boolean)
      .join('\n');
  };

  const buildOnlineMailtoUrl = () => {
    const subject = encodeURIComponent(
      `[TonyEnglish] Đăng ký khóa học Online & Học thử: ${selectedOnlineCourseTitle} - ${
        onlineFullName.trim() || onlinePhone.trim()
      }`
    );
    const body = encodeURIComponent(buildOnlineRegistrationMessage());
    return `mailto:${CONTACT_EMAIL}?subject=${subject}&body=${body}`;
  };

  const handleOnlineSubmitRegistration = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!onlineFullName.trim() || !onlinePhone.trim()) {
      alert('Vui lòng nhập Họ tên và Số điện thoại / Zalo để TonyEnglish liên hệ cấp tài khoản học thử nhé!');
      return;
    }

    setIsOnlineSubmitting(true);
    try {
      try {
        await fetch(`https://formsubmit.co/ajax/${CONTACT_EMAIL}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json',
          },
          body: JSON.stringify({
            _subject: `[TonyEnglish Online] Đăng ký học thử: ${selectedOnlineCourseTitle} - ${onlineFullName.trim()} (${onlinePhone.trim()})`,
            Ho_va_ten: onlineFullName.trim(),
            So_dien_thoai_Zalo: onlinePhone.trim(),
            Email_hoc_vien: onlineStudentEmail.trim() || 'Không điền',
            Khoa_hoc_dang_ky: selectedOnlineCourseTitle,
            Ghi_chu: onlineNote.trim() || 'Không có',
            Nguon: window.location.href,
          }),
        });
      } catch (ajaxErr) {
        console.warn('FormSubmit AJAX fallback to mailto:', ajaxErr);
      }

      setOnlineSubmittedSuccess(true);
      window.location.href = buildOnlineMailtoUrl();
    } finally {
      setIsOnlineSubmitting(false);
    }
  };

  const handleChatZaloWithContent = async () => {
    const msg = buildOnlineRegistrationMessage();
    try {
      await navigator.clipboard.writeText(msg);
      setCopiedZaloText(true);
      setTimeout(() => setCopiedZaloText(false), 4000);
    } catch (e) {}
    window.open(CONTACT_ZALO_URL, '_blank');
  };

  const courseTitle = isOnlineView
    ? lang === 'vi'
      ? 'Các khóa học Online & Học thử miễn phí'
      : 'Online Courses & Free Trial'
    : currentCourse
    ? lang === 'vi'
      ? currentCourse.cc_name_vi || currentCourse.cc_name
      : currentCourse.cc_name
    : t('Study at TonyEnglish');

  const courseDescHtml = currentCourse
    ? lang === 'vi'
      ? currentCourse.cc_desc_vi || currentCourse.cc_desc
      : currentCourse.cc_desc || currentCourse.cc_desc_vi
    : options['studyEnglish'] || '';

  useEffect(() => {
    updatePageSeo(courseTitle, isOnlineView ? 'Các khóa học Online tích hợp AI & Lớp học thử miễn phí tại TonyEnglish' : courseDescHtml);
  }, [courseTitle, courseDescHtml, isOnlineView]);

  const childCoursesOfCurrent = currentCourse ? subCategories(currentCourse.cc_id) : [];
  const filteredOnlinePackages = FEATURED_ONLINE_PACKAGES.filter((pkg) =>
    selectedOnlineCat === 'all' ? true : pkg.category === selectedOnlineCat
  );

  return (
    <div className="max-w-7xl mx-auto px-3.5 sm:px-6 py-4 sm:py-8">
      {/* BREADCRUMB */}
      <nav className="flex items-center gap-1.5 sm:gap-2 text-xs sm:text-[15px] font-semibold text-slate-500 mb-3.5 sm:mb-6 flex-wrap">
        <Link to="/" className="hover:text-[#0a5482] flex items-center gap-1">
          <span>🏠</span>
          <span>{t('Home')}</span>
        </Link>
        <span>/</span>
        <Link to="/courses" className="hover:text-[#0a5482]">
          {t('Courses')}
        </Link>
        <span>/</span>
        <span className="text-[#0a5482] font-bold">
          {isOnlineView ? (lang === 'vi' ? 'Các khóa học Online' : 'Online Courses') : courseTitle}
        </span>
      </nav>

      <div className="flex flex-col lg:flex-row gap-4 sm:gap-8 xl:gap-12 items-start">
        {/* LEFT SIDEBAR: SUBTLE, NON-COMPETING COURSES MENU */}
        <aside className="w-full lg:w-[260px] xl:w-[270px] shrink-0 bg-white rounded-2xl border border-slate-200/80 shadow-2xs overflow-hidden lg:sticky lg:top-24">
          <button
            type="button"
            onClick={() => setMobileCateOpen((prev) => !prev)}
            className="w-full bg-slate-100/80 px-4 py-3 border-b border-slate-200/70 flex items-center justify-between lg:pointer-events-none cursor-pointer text-left"
          >
            <h2 className="text-slate-600 lg:text-slate-500 font-bold text-xs uppercase tracking-widest flex items-center gap-2 min-w-0">
              <span className="opacity-80 shrink-0">🎓</span>
              <span className="shrink-0">{t('Courses')}</span>
              <span className="lg:hidden font-semibold text-[#0a5482] normal-case tracking-normal truncate">
                • {isOnlineView ? (lang === 'vi' ? 'Khóa Online' : 'Online') : courseTitle}
              </span>
            </h2>
            <span className="lg:hidden text-[11px] font-bold text-[#0a5482] bg-white px-2.5 py-1 rounded-lg border border-slate-200/80 shadow-2xs flex items-center gap-1 shrink-0 ml-2">
              <span>
                {mobileCateOpen
                  ? lang === 'vi'
                    ? 'Thu gọn'
                    : 'Hide'
                  : lang === 'vi'
                  ? 'Danh mục'
                  : 'Categories'}
              </span>
              <span>{mobileCateOpen ? '▲' : '▼'}</span>
            </span>
          </button>

          <div className={`${mobileCateOpen ? 'block' : 'hidden'} lg:block`}>
            {/* GROUP 1: KHÓA HỌC OFFLINE */}
            <div className="px-4 pt-3 pb-1.5 flex items-center gap-1.5">
              <span className="text-xs opacity-75">🏢</span>
              <span className="text-[11px] font-bold uppercase tracking-wider text-slate-400">
                {lang === 'vi' ? 'Khóa học Offline' : 'Offline Courses'}
              </span>
            </div>

            <ul className="divide-y divide-slate-100 text-[14.5px] px-1.5 pb-1.5">
              <li>
                <Link
                  to="/courses"
                  onClick={() => setMobileCateOpen(false)}
                  className={`block px-3.5 py-2.5 rounded-xl transition-colors ${
                    !isOnlineView && !currentCourse
                      ? 'bg-sky-50/90 text-[#0a5482] font-semibold border-l-[3px] border-[#2ab4e8]'
                      : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                  }`}
                >
                  {t('Study at TonyEnglish')}
                </Link>
              </li>

              {homeParents.map((parent) => {
                const subs = subCategories(parent.cc_id);
                const isOpen =
                  !isOnlineView &&
                  (openParentId === parent.cc_id ||
                    (currentCourse &&
                      (currentCourse.cc_id === parent.cc_id || currentCourse.cc_parent === parent.cc_id)));
                const parentName = lang === 'vi' ? parent.cc_name_vi || parent.cc_name : parent.cc_name;
                const isCurrentParent = !isOnlineView && currentCourse && currentCourse.cc_id === parent.cc_id;

                return (
                  <li key={parent.cc_id}>
                    <div className="flex items-center justify-between">
                      <Link
                        to={`/courses/${(parent.cc_name_url || '').trim()}`}
                        onClick={() => {
                          setOpenParentId(parent.cc_id);
                          if (subs.length === 0) setMobileCateOpen(false);
                        }}
                        className={`flex-1 px-3.5 py-2.5 rounded-xl transition-colors flex items-center justify-between ${
                          isCurrentParent
                            ? 'bg-sky-50/90 text-[#0a5482] font-semibold border-l-[3px] border-[#2ab4e8]'
                            : isOpen
                            ? 'text-[#0a5482] font-semibold bg-slate-50/70'
                            : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                        }`}
                      >
                        <span>{parentName}</span>
                        {subs.length > 0 && (
                          <span
                            className={`text-xs transition-transform ${
                              isOpen ? 'rotate-90 text-[#2ab4e8]' : 'text-slate-400'
                            }`}
                          >
                            ▸
                          </span>
                        )}
                      </Link>
                    </div>

                    {subs.length > 0 && isOpen && (
                      <ul className="mt-0.5 mb-1 ml-2 pl-2 border-l border-slate-200/80 space-y-0.5">
                        {subs.map((sub) => {
                          const subName = lang === 'vi' ? sub.cc_name_vi || sub.cc_name : sub.cc_name;
                          const isActiveSub = !isOnlineView && currentCourse && currentCourse.cc_id === sub.cc_id;
                          return (
                            <li key={sub.cc_id}>
                              <Link
                                to={`/courses/${(sub.cc_name_url || '').trim()}`}
                                onClick={() => setMobileCateOpen(false)}
                                className={`block px-3 py-2 rounded-lg text-[13.5px] transition-all ${
                                  isActiveSub
                                    ? 'bg-sky-50 text-[#0a5482] font-semibold border-l-2 border-[#2ab4e8]'
                                    : 'text-slate-500 font-normal hover:bg-slate-50 hover:text-slate-800'
                                }`}
                              >
                                {subName}
                              </Link>
                            </li>
                          );
                        })}
                      </ul>
                    )}
                  </li>
                );
              })}
            </ul>

            {/* GROUP 2: CÁC KHÓA HỌC ONLINE */}
            <div className="px-4 pt-3 pb-1.5 border-t border-slate-200/70 flex items-center gap-1.5">
              <span className="text-xs opacity-75">💻</span>
              <span className="text-[11px] font-bold uppercase tracking-wider text-slate-400">
                {lang === 'vi' ? 'Khóa học Online & Học thử' : 'Online Courses'}
              </span>
            </div>

            <ul className="divide-y divide-slate-100 text-[14.5px] px-1.5 pb-2">
              <li>
                <Link
                  to="/courses/online"
                  onClick={() => {
                    setSelectedOnlineCat('all');
                    setMobileCateOpen(false);
                  }}
                  className={`px-3.5 py-2.5 rounded-xl transition-colors flex items-center justify-between ${
                    isOnlineView
                      ? 'bg-sky-50/90 text-[#0a5482] font-semibold border-l-[3px] border-[#2ab4e8]'
                      : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                  }`}
                >
                  <span>{lang === 'vi' ? 'Các khóa học Online' : 'Online Courses'}</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-50 text-amber-700 border border-amber-200">
                    Học thử
                  </span>
                </Link>

                <ul className="mt-0.5 mb-1 ml-2 pl-2 border-l border-slate-200/80 space-y-0.5">
                  <li>
                    <Link
                      to="/courses/online?cat=all"
                      onClick={() => {
                        setSelectedOnlineCat('all');
                        setMobileCateOpen(false);
                      }}
                      className={`block px-3 py-2 rounded-lg text-[13.5px] transition-all ${
                        isOnlineView && selectedOnlineCat === 'all'
                          ? 'bg-sky-50 text-[#0a5482] font-semibold border-l-2 border-[#2ab4e8]'
                          : 'text-slate-500 font-normal hover:bg-slate-50 hover:text-slate-800'
                      }`}
                    >
                      Tất cả khóa học Online ({FEATURED_ONLINE_PACKAGES.length})
                    </Link>
                  </li>
                  <li>
                    <Link
                      to="/courses/online?cat=english"
                      onClick={() => {
                        setSelectedOnlineCat('english');
                        setMobileCateOpen(false);
                      }}
                      className={`block px-3 py-2 rounded-lg text-[13.5px] transition-all ${
                        isOnlineView && selectedOnlineCat === 'english'
                          ? 'bg-sky-50 text-[#0a5482] font-semibold border-l-2 border-[#2ab4e8]'
                          : 'text-slate-500 font-normal hover:bg-slate-50 hover:text-slate-800'
                      }`}
                    >
                      IELTS &amp; Tiếng Anh Giao Tiếp
                    </Link>
                  </li>
                  <li>
                    <Link
                      to="/courses/online?cat=igcse"
                      onClick={() => {
                        setSelectedOnlineCat('igcse');
                        setMobileCateOpen(false);
                      }}
                      className={`block px-3 py-2 rounded-lg text-[13.5px] transition-all ${
                        isOnlineView && selectedOnlineCat === 'igcse'
                          ? 'bg-sky-50 text-[#0a5482] font-semibold border-l-2 border-[#2ab4e8]'
                          : 'text-slate-500 font-normal hover:bg-slate-50 hover:text-slate-800'
                      }`}
                    >
                      Quốc tế Cambridge IGCSE
                    </Link>
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </aside>

        {/* RIGHT MAIN CONTENT */}
        <div className="flex-1 min-w-0 w-full space-y-6">
          {/* TOP MODE SWITCHER: OFFLINE vs ONLINE */}
          <div className="bg-white rounded-2xl p-2 border border-slate-200/80 shadow-xs grid grid-cols-1 sm:grid-cols-2 gap-2">
            <Link
              to="/courses"
              className={`flex items-center justify-center gap-2.5 py-3 px-4 rounded-xl font-black text-sm sm:text-base transition-all ${
                !isOnlineView
                  ? 'bg-[#0a5482] text-white shadow-md'
                  : 'bg-slate-50 text-slate-600 hover:bg-slate-100 hover:text-[#0a5482]'
              }`}
            >
              <span className="text-lg">🏢</span>
              <span>{lang === 'vi' ? 'Các khóa học Offline (Tại Trung tâm)' : 'Offline Courses'}</span>
            </Link>
            <Link
              to="/courses/online"
              className={`flex items-center justify-center gap-2.5 py-3 px-4 rounded-xl font-black text-sm sm:text-base transition-all ${
                isOnlineView
                  ? 'bg-gradient-to-r from-[#0a5482] to-[#2ab4e8] text-white shadow-md'
                  : 'bg-amber-50/70 text-amber-900 border border-amber-200/70 hover:bg-amber-100/80'
              }`}
            >
              <span className="text-lg">💻</span>
              <span>{lang === 'vi' ? 'Các khóa học Online & Học thử' : 'Online Courses & Free Trial'}</span>
            </Link>
          </div>

          {!isOnlineView ? (
            /* ================= OFFLINE COURSES VIEW ================= */
            <div className="bg-white rounded-3xl border border-slate-200/80 shadow-xs overflow-hidden">
              {/* Course Header Banner */}
              <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-6 sm:px-8 py-6 text-white flex flex-wrap items-center justify-between gap-4">
                <div>
                  <div className="text-xs sm:text-sm font-extrabold uppercase tracking-widest text-[#2ab4e8] mb-1">
                    🏢 Chương trình đào tạo Offline tại Trung tâm
                  </div>
                  <h1 className="text-2xl sm:text-3xl font-black tracking-tight">{courseTitle}</h1>
                </div>
                <Link
                  to="/courses/online"
                  className="bg-white/15 hover:bg-white/25 text-white border border-white/25 text-sm font-bold px-4 py-2 rounded-xl transition"
                >
                  💻 Xem thêm Khóa học Online ➜
                </Link>
              </div>

              <div className="p-6 sm:p-8 space-y-6">
                {/* Subcategory Quick Cards if parent category has children */}
                {childCoursesOfCurrent.length > 0 && (
                  <div className="bg-slate-50 rounded-2xl p-5 border border-slate-200/80">
                    <h3 className="text-xs sm:text-sm font-black uppercase tracking-wider text-slate-500 mb-3">
                      {lang === 'vi' ? 'Các cấp độ / chuyên đề trong khóa học này:' : 'Courses in this category:'}
                    </h3>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                      {childCoursesOfCurrent.map((sub) => (
                        <Link
                          key={sub.cc_id}
                          to={`/courses/${(sub.cc_name_url || '').trim()}`}
                          className="bg-white hover:bg-sky-50 border border-slate-200 rounded-xl p-4 flex items-center justify-between group transition shadow-2xs"
                        >
                          <div>
                            <div className="font-extrabold text-[15px] sm:text-base text-slate-800 group-hover:text-[#0a5482]">
                              {lang === 'vi' ? sub.cc_name_vi || sub.cc_name : sub.cc_name}
                            </div>
                            {sub.cc_tuition && (
                              <div className="text-sm text-slate-500 mt-0.5">
                                {t('Tuition fee')}: <strong className="text-[#0a5482]">{sub.cc_tuition}</strong>
                              </div>
                            )}
                          </div>
                          <span className="text-[#2ab4e8] font-black group-hover:translate-x-1 transition-transform">
                            →
                          </span>
                        </Link>
                      ))}
                    </div>
                  </div>
                )}

                {/* Course Metadata Info Cards (when viewing a specific leaf course) */}
                {currentCourse && !hasSubCategories && (
                  <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200/70 flex items-center gap-3.5">
                      <div className="w-11 h-11 rounded-xl bg-blue-100 text-[#0a5482] flex items-center justify-center text-xl font-black">
                        🏷️
                      </div>
                      <div>
                        <div className="text-xs font-bold text-slate-400 uppercase">{t('Course Code')}</div>
                        <div className="font-black text-slate-800 text-base">{currentCourse.cc_code || 'TE-PRO'}</div>
                      </div>
                    </div>

                    <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200/70 flex items-center gap-3.5">
                      <div className="w-11 h-11 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center text-xl font-black">
                        📚
                      </div>
                      <div>
                        <div className="text-xs font-bold text-slate-400 uppercase">{t('Number of Lecture')}</div>
                        <div className="font-black text-slate-800 text-base">{lectureCount} bài giảng</div>
                      </div>
                    </div>

                    <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200/70 flex items-center gap-3.5">
                      <div className="w-11 h-11 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center text-xl font-black">
                        💳
                      </div>
                      <div>
                        <div className="text-xs font-bold text-slate-400 uppercase">{t('Tuition fee')}</div>
                        <div className="font-black text-[#0a5482] text-base">{currentCourse.cc_tuition || 'Liên hệ'}</div>
                      </div>
                    </div>
                  </div>
                )}

                {/* Course Description HTML */}
                <div
                  className="legacy-prose text-justify"
                  dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(courseDescHtml) }}
                />

                {/* Action Buttons for Offline Course */}
                {currentCourse && !hasSubCategories && (
                  <div className="pt-6 border-t border-slate-200 flex flex-wrap items-center gap-3">
                    <button
                      type="button"
                      onClick={() => setShowJoinForm(!showJoinForm)}
                      className="bg-[#0a5482] hover:bg-[#084266] text-white font-black text-sm px-6 py-3 rounded-xl shadow-lg shadow-blue-900/15 transition active:scale-95 flex items-center gap-2"
                    >
                      <span>✍️</span>
                      <span>{t('Join now')}</span>
                    </button>

                    <button
                      type="button"
                      onClick={() => setShowSyllabusModal(true)}
                      className="bg-sky-50 hover:bg-sky-100 text-[#0a5482] border border-sky-200 font-extrabold text-sm px-5 py-3 rounded-xl transition flex items-center gap-2"
                    >
                      <span>📋</span>
                      <span>{t('Click here view to courses Syllabus')}</span>
                    </button>

                    {currentCourse.cc_trial === 1 && (
                      <Link
                        to={`/trial/${(currentCourse.cc_name_url || '').trim()}`}
                        className="bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm px-5 py-3 rounded-xl shadow-md transition flex items-center gap-2"
                      >
                        <span>🎧</span>
                        <span>Học thử (Trial)</span>
                      </Link>
                    )}
                  </div>
                )}

                {/* JOIN NOW REGISTRATION FORM */}
                {showJoinForm && currentCourse && (
                  <div className="mt-6 bg-slate-50 rounded-2xl p-6 sm:p-8 border border-slate-200">
                    <h2 className="text-xl font-black text-[#0a5482] mb-1">{t('Submission form')}</h2>
                    <p className="text-xs text-slate-500 mb-6">
                      {t('Please complete information on the items marked with')} (
                      <span className="text-rose-500">*</span>)
                    </p>

                    {regMessage && (
                      <div
                        className={`p-4 mb-6 rounded-xl font-bold text-sm border ${
                          regMessage.isError
                            ? 'bg-rose-50 text-rose-700 border-rose-200'
                            : 'bg-emerald-50 text-emerald-700 border-emerald-200'
                        }`}
                      >
                        {regMessage.text}
                      </div>
                    )}

                    <form onSubmit={handleJoinSubmit} className="space-y-4 max-w-2xl">
                      {!user && (
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                          <div>
                            <label className="block text-xs font-bold text-slate-600 mb-1">
                              {t('Full Name')} <span className="text-rose-500">*</span>
                            </label>
                            <input
                              type="text"
                              required
                              value={regName}
                              onChange={(e) => setRegName(e.target.value)}
                              className="w-full bg-white border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
                            />
                          </div>

                          <div>
                            <label className="block text-xs font-bold text-slate-600 mb-1">
                              {t('Phone')} <span className="text-rose-500">*</span>
                            </label>
                            <input
                              type="text"
                              required
                              value={regPhone}
                              onChange={(e) => setRegPhone(e.target.value)}
                              className="w-full bg-white border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
                            />
                          </div>

                          <div>
                            <label className="block text-xs font-bold text-slate-600 mb-1">
                              Email <span className="text-rose-500">*</span>
                            </label>
                            <input
                              type="email"
                              required
                              value={regEmail}
                              onChange={(e) => setRegEmail(e.target.value)}
                              className="w-full bg-white border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
                            />
                          </div>

                          <div>
                            <label className="block text-xs font-bold text-slate-600 mb-1">
                              {t('City')} <span className="text-rose-500">*</span>
                            </label>
                            <input
                              type="text"
                              required
                              value={regCity}
                              onChange={(e) => setRegCity(e.target.value)}
                              className="w-full bg-white border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
                            />
                          </div>

                          <div>
                            <label className="block text-xs font-bold text-slate-600 mb-1">{t('Birthday')}</label>
                            <input
                              type="text"
                              placeholder="DD/MM/YYYY"
                              value={regBirthday}
                              onChange={(e) => setRegBirthday(e.target.value)}
                              className="w-full bg-white border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
                            />
                          </div>

                          <div>
                            <label className="block text-xs font-bold text-slate-600 mb-1">{t('Gender')}</label>
                            <select
                              value={regGender}
                              onChange={(e) => setRegGender(e.target.value)}
                              className="w-full bg-white border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
                            >
                              <option value="1">{t('Male')}</option>
                              <option value="0">{t('Female')}</option>
                            </select>
                          </div>

                          <div className="sm:col-span-2">
                            <label className="block text-xs font-bold text-slate-600 mb-1">{t('Work')}</label>
                            <input
                              type="text"
                              value={regWork}
                              onChange={(e) => setRegWork(e.target.value)}
                              className="w-full bg-white border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
                            />
                          </div>
                        </div>
                      )}

                      <div>
                        <label className="block text-xs font-bold text-slate-600 mb-1.5">
                          {t('Additional Courses')} (Giữ Ctrl để chọn nhiều):
                        </label>
                        <select
                          multiple
                          value={regExtraCourses.map(String)}
                          onChange={(e) => {
                            const opts = Array.from(e.target.selectedOptions).map((o) => parseInt(o.value, 10));
                            setRegExtraCourses(opts);
                          }}
                          className="w-full bg-white border border-slate-300 rounded-xl p-3 text-sm h-28 focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
                        >
                          {allCategories
                            .filter((c) => c.cc_parent !== 0 && c.cc_id !== currentCourse.cc_id)
                            .map((c) => (
                              <option key={c.cc_id} value={c.cc_id}>
                                {lang === 'vi' ? c.cc_name_vi || c.cc_name : c.cc_name}
                              </option>
                            ))}
                        </select>
                      </div>

                      <button
                        type="submit"
                        disabled={regSubmitting}
                        className="bg-[#0a5482] hover:bg-[#084266] text-white font-black text-sm px-8 py-3 rounded-xl shadow-md transition"
                      >
                        {regSubmitting ? 'Đang gửi...' : t('Submit')}
                      </button>
                    </form>
                  </div>
                )}
              </div>
            </div>
          ) : (
            /* ================= ONLINE COURSES & FREE TRIAL VIEW ================= */
            <div className="space-y-8">
              {/* 1. ONLINE HERO BANNER */}
              <div className="rounded-3xl overflow-hidden bg-gradient-to-br from-[#072f49] via-[#0a5482] to-[#0f172a] text-white p-6 sm:p-8 lg:p-10 shadow-xl relative">
                <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-md border border-white/20 text-cyan-200 font-black text-xs px-3.5 py-1.5 rounded-full mb-4">
                  <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
                  <span>💻 HỆ THỐNG KHÓA HỌC ONLINE &amp; LUYỆN THI AI 24/7</span>
                </div>

                <h1 className="text-2xl sm:text-4xl font-black tracking-tight leading-tight mb-4">
                  Các Khóa Học Online Đóng Gói Thông Minh:{' '}
                  <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#5ce1e6] via-[#2ab4e8] to-amber-300">
                    IELTS, Tiếng Anh &amp; Cambridge IGCSE
                  </span>
                </h1>

                <p className="text-sm sm:text-base text-blue-100/90 font-medium leading-relaxed mb-6">
                  Kết hợp hoàn hảo giữa <b>Bài giảng tương tác song ngữ</b>, <b>Podcast học thuật</b>,{' '}
                  <b>Trợ lý AI chấm chữa Speaking/Writing 24/7</b> và <b>Kho 1.800+ đề thi chuẩn quốc tế</b>. Cho phép
                  học viên <b>vào Lớp Học Thử miễn phí</b> để trải nghiệm thực tế trước khi đăng ký!
                </p>

                <div className="flex flex-wrap items-center gap-3">
                  <button
                    type="button"
                    onClick={() => scrollToOnlineRegister()}
                    className="bg-gradient-to-r from-amber-400 to-orange-500 hover:from-amber-500 hover:to-orange-600 text-slate-950 font-black text-xs sm:text-sm px-6 py-3.5 rounded-xl shadow-lg transition active:scale-95 flex items-center gap-2 cursor-pointer"
                  >
                    <span>🎁 Đăng Ký Học Thử Miễn Phí</span>
                    <span>➜</span>
                  </button>

                  <a
                    href={CONTACT_ZALO_URL}
                    target="_blank"
                    rel="noreferrer"
                    className="bg-[#0068ff] hover:bg-[#0057d6] text-white font-black text-xs sm:text-sm px-5 py-3.5 rounded-xl shadow-lg border border-white/20 transition active:scale-95 flex items-center gap-2"
                  >
                    <span>💬 Nhắn Zalo: {CONTACT_PHONE_DISPLAY}</span>
                  </a>

                  <button
                    type="button"
                    onClick={() => window.dispatchEvent(new CustomEvent('tony-open-lms'))}
                    className="bg-white/10 hover:bg-white/20 text-white font-bold text-xs sm:text-sm px-5 py-3.5 rounded-xl border border-white/25 transition flex items-center gap-2 cursor-pointer"
                  >
                    <span>🎓 Vào Phòng Học LMS</span>
                  </button>
                </div>
              </div>

              {/* 2. FILTER TABS & FEATURED ONLINE PACKAGES */}
              <div className="space-y-6">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                  <div>
                    <h2 className="text-xl sm:text-2xl font-black text-slate-800">
                      Danh Sách Các Khóa Học Online Trọn Gói
                    </h2>
                    <p className="text-xs sm:text-sm text-slate-500 font-medium">
                      Tất cả các khóa học Online đều mở Lớp Học Thử miễn phí học phần đầu tiên
                    </p>
                  </div>

                  <div className="inline-flex flex-wrap items-center gap-1.5 bg-slate-200/70 p-1.5 rounded-2xl">
                    <button
                      type="button"
                      onClick={() => setSelectedOnlineCat('all')}
                      className={`px-3.5 py-2 rounded-xl text-xs font-black transition cursor-pointer ${
                        selectedOnlineCat === 'all'
                          ? 'bg-[#0a5482] text-white shadow-sm'
                          : 'text-slate-600 hover:text-slate-900'
                      }`}
                    >
                      🌟 Tất cả ({FEATURED_ONLINE_PACKAGES.length})
                    </button>
                    <button
                      type="button"
                      onClick={() => setSelectedOnlineCat('english')}
                      className={`px-3.5 py-2 rounded-xl text-xs font-black transition cursor-pointer ${
                        selectedOnlineCat === 'english'
                          ? 'bg-[#0a5482] text-white shadow-sm'
                          : 'text-slate-600 hover:text-slate-900'
                      }`}
                    >
                      🔥 IELTS &amp; Giao Tiếp
                    </button>
                    <button
                      type="button"
                      onClick={() => setSelectedOnlineCat('igcse')}
                      className={`px-3.5 py-2 rounded-xl text-xs font-black transition cursor-pointer ${
                        selectedOnlineCat === 'igcse'
                          ? 'bg-[#0a5482] text-white shadow-sm'
                          : 'text-slate-600 hover:text-slate-900'
                      }`}
                    >
                      🌍 Cambridge IGCSE
                    </button>
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {filteredOnlinePackages.map((pkg) => (
                    <div
                      key={pkg.id}
                      className="bg-white rounded-3xl border border-slate-200/90 shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col overflow-hidden"
                    >
                      <div className={`bg-gradient-to-br ${pkg.gradient} p-6 text-white relative`}>
                        <div className="flex items-center justify-between gap-2 mb-3">
                          <span className="bg-white/20 backdrop-blur-md text-white text-xs font-black uppercase tracking-wider px-3 py-1 rounded-full border border-white/25">
                            {pkg.badge}
                          </span>
                          <span className="text-3xl">{pkg.icon}</span>
                        </div>
                        <h3 className="text-xl sm:text-[22px] font-black leading-snug mb-2">{pkg.title}</h3>
                        <p className="text-sm sm:text-[15px] text-white/90 font-medium leading-relaxed">{pkg.subtitle}</p>
                      </div>

                      <div className="bg-slate-50 px-6 py-3 border-b border-slate-100 flex flex-wrap gap-2">
                        {pkg.stats.map((st, idx) => (
                          <span
                            key={idx}
                            className={`text-xs sm:text-[13px] font-bold px-2.5 py-1 rounded-lg border ${pkg.accentColor}`}
                          >
                            {st}
                          </span>
                        ))}
                      </div>

                      <div className="p-6 flex-1 flex flex-col justify-between">
                        <ul className="space-y-3 mb-6">
                          {pkg.highlights.map((item, i) => (
                            <li
                              key={i}
                              className="flex items-start gap-2.5 text-[15px] sm:text-base text-slate-700 font-medium leading-relaxed"
                            >
                              <span className="text-emerald-500 font-black mt-0.5 shrink-0">✔</span>
                              <span>{item}</span>
                            </li>
                          ))}
                        </ul>

                        <div className="pt-4 border-t border-slate-100">
                          <div className="flex items-center justify-between mb-3.5 bg-amber-50/70 border border-amber-200/80 rounded-2xl px-4 py-2.5">
                            <div>
                              <span className="text-xs font-bold text-slate-500 uppercase block">
                                Học phí khóa học Online
                              </span>
                              <span className="text-base sm:text-lg font-black text-[#0a5482]">Liên hệ tư vấn</span>
                            </div>
                            <span className="bg-amber-100 text-amber-800 text-xs font-black px-3 py-1 rounded-full border border-amber-300">
                              🎁 Có Học Thử
                            </span>
                          </div>

                          <div className="grid grid-cols-2 gap-2.5">
                            <button
                              type="button"
                              onClick={() => scrollToOnlineRegister(pkg.title)}
                              className="bg-[#0a5482] hover:bg-[#084266] text-white font-black text-sm py-3 px-3 rounded-xl shadow-md transition active:scale-95 flex items-center justify-center gap-1.5 cursor-pointer"
                            >
                              <span>🎁 Đăng ký học thử</span>
                            </button>
                            <a
                              href={CONTACT_ZALO_URL}
                              target="_blank"
                              rel="noreferrer"
                              className="bg-emerald-600 hover:bg-emerald-700 text-white font-black text-sm py-3 px-3 rounded-xl shadow-md transition active:scale-95 flex items-center justify-center gap-1.5"
                            >
                              <span>💬 Nhắn Zalo</span>
                            </a>
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* 3. REGISTRATION FORM FOR ONLINE COURSES & FREE TRIAL */}
              <div
                id="dang-ky-hoc-thu"
                className="bg-white rounded-3xl shadow-xl border border-slate-200 overflow-hidden grid grid-cols-1 lg:grid-cols-12"
              >
                <div className="lg:col-span-5 bg-gradient-to-br from-[#0a5482] via-[#083b5c] to-slate-900 text-white p-6 sm:p-8 flex flex-col justify-between">
                  <div>
                    <span className="inline-block bg-amber-400 text-slate-950 font-black text-[11px] px-3 py-1 rounded-full uppercase tracking-wider mb-3">
                      CẤP TÀI KHOẢN HỌC THỬ TRONG 5 PHÚT
                    </span>
                    <h2 className="text-xl sm:text-2xl font-black leading-tight mb-3">
                      Đăng Ký Học Thử Khóa Học Online
                    </h2>
                    <p className="text-blue-100/85 text-xs sm:text-sm font-medium leading-relaxed mb-6">
                      Điền form đăng ký bên cạnh để gửi Email hoặc <b>nhắn tin / gọi điện ngay qua Zalo</b> để được
                      kích hoạt Lớp Học Thử miễn phí!
                    </p>

                    <div className="space-y-3">
                      <a
                        href={CONTACT_ZALO_URL}
                        target="_blank"
                        rel="noreferrer"
                        className="flex items-center gap-3.5 bg-white/10 hover:bg-white/15 border border-white/20 p-3.5 rounded-2xl transition"
                      >
                        <div className="w-10 h-10 rounded-xl bg-[#0068ff] flex items-center justify-center text-xl shrink-0">
                          💬
                        </div>
                        <div className="min-w-0">
                          <div className="text-[11px] font-bold text-cyan-300 uppercase">Nhắn tin Zalo trực tiếp</div>
                          <div className="text-base font-black text-white">{CONTACT_PHONE_DISPLAY}</div>
                        </div>
                      </a>

                      <a
                        href={`tel:${CONTACT_PHONE}`}
                        className="flex items-center gap-3.5 bg-white/10 hover:bg-white/15 border border-white/20 p-3.5 rounded-2xl transition"
                      >
                        <div className="w-10 h-10 rounded-xl bg-emerald-500 flex items-center justify-center text-xl shrink-0">
                          📞
                        </div>
                        <div className="min-w-0">
                          <div className="text-[11px] font-bold text-emerald-300 uppercase">Hotline tư vấn</div>
                          <div className="text-base font-black text-white">{CONTACT_PHONE_DISPLAY}</div>
                        </div>
                      </a>
                    </div>
                  </div>

                  <div className="mt-6 pt-4 border-t border-white/15 text-xs text-blue-200/80 space-y-1">
                    <p>✔ Mở tài khoản học thử miễn phí các học phần mẫu</p>
                    <p>✔ Học mọi lúc mọi nơi trên Máy tính, iPad và Điện thoại</p>
                  </div>
                </div>

                <div className="lg:col-span-7 p-6 sm:p-8">
                  <h3 className="text-xl font-black text-slate-800 mb-1">
                    🎁 Form Đăng Ký Nhận Tài Khoản Học Thử Online
                  </h3>
                  <p className="text-xs text-slate-500 font-medium mb-5">
                    Điền thông tin bên dưới rồi chọn <b>Gửi Email</b> hoặc <b>Nhắn qua Zalo {CONTACT_PHONE_DISPLAY}</b>.
                  </p>

                  <form onSubmit={handleOnlineSubmitRegistration} className="space-y-4">
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-xs font-black text-slate-600 uppercase tracking-wider mb-1">
                          Họ và tên Học viên / Phụ huynh *
                        </label>
                        <input
                          type="text"
                          required
                          value={onlineFullName}
                          onChange={(e) => setOnlineFullName(e.target.value)}
                          placeholder="VD: Nguyễn Minh Anh"
                          className="w-full border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm font-medium outline-none focus:ring-2 focus:ring-[#0a5482] bg-slate-50 focus:bg-white"
                        />
                      </div>

                      <div>
                        <label className="block text-xs font-black text-slate-600 uppercase tracking-wider mb-1">
                          Số điện thoại / Zalo *
                        </label>
                        <input
                          type="tel"
                          required
                          value={onlinePhone}
                          onChange={(e) => setOnlinePhone(e.target.value)}
                          placeholder="VD: 0901234567"
                          className="w-full border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm font-medium outline-none focus:ring-2 focus:ring-[#0a5482] bg-slate-50 focus:bg-white"
                        />
                      </div>
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-xs font-black text-slate-600 uppercase tracking-wider mb-1">
                          Email nhận tài khoản học thử
                        </label>
                        <input
                          type="email"
                          value={onlineStudentEmail}
                          onChange={(e) => setOnlineStudentEmail(e.target.value)}
                          placeholder="VD: hocvien@gmail.com"
                          className="w-full border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm font-medium outline-none focus:ring-2 focus:ring-[#0a5482] bg-slate-50 focus:bg-white"
                        />
                      </div>

                      <div>
                        <label className="block text-xs font-black text-slate-600 uppercase tracking-wider mb-1">
                          Khóa học Online muốn học thử *
                        </label>
                        <select
                          value={selectedOnlineCourseTitle}
                          onChange={(e) => setSelectedOnlineCourseTitle(e.target.value)}
                          className="w-full border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm font-bold text-slate-800 outline-none focus:ring-2 focus:ring-[#0a5482] bg-slate-50 focus:bg-white"
                        >
                          <optgroup label="Các Gói Combo Online Nổi Bật">
                            {FEATURED_ONLINE_PACKAGES.map((pkg) => (
                              <option key={pkg.id} value={pkg.title}>
                                {pkg.title}
                              </option>
                            ))}
                          </optgroup>
                          {dbOnlineCourses.length > 0 && (
                            <optgroup label="Từng Môn Học Cụ Thể">
                              {dbOnlineCourses.map((c) => (
                                <option key={c.id} value={c.title}>
                                  {c.title}
                                </option>
                              ))}
                            </optgroup>
                          )}
                        </select>
                      </div>
                    </div>

                    <div>
                      <label className="block text-xs font-black text-slate-600 uppercase tracking-wider mb-1">
                        Ghi chú thêm (Trình độ hiện tại / Mục tiêu)
                      </label>
                      <textarea
                        rows={2}
                        value={onlineNote}
                        onChange={(e) => setOnlineNote(e.target.value)}
                        placeholder="VD: Em muốn đăng ký học thử khóa IELTS / Giao tiếp phản xạ AI..."
                        className="w-full border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm font-medium outline-none focus:ring-2 focus:ring-[#0a5482] bg-slate-50 focus:bg-white resize-none"
                      />
                    </div>

                    {onlineSubmittedSuccess && (
                      <div className="bg-emerald-50 border border-emerald-200 rounded-2xl p-3.5 text-emerald-900 text-xs font-medium">
                        ✅ Đã tạo yêu cầu đăng ký học thử thành công! Bạn có thể bấm nút{' '}
                        <b>Nhắn Zalo {CONTACT_PHONE_DISPLAY}</b> bên dưới để được cấp tài khoản ngay lập tức.
                      </div>
                    )}

                    {copiedZaloText && (
                      <div className="bg-blue-50 border border-blue-200 rounded-xl p-3 text-blue-800 text-xs font-bold">
                        📋 Đã tự động copy nội dung đăng ký! Bạn chỉ cần nhấn &quot;Dán (Paste)&quot; vào khung chat
                        Zalo {CONTACT_PHONE_DISPLAY}.
                      </div>
                    )}

                    <div className="pt-1 flex flex-col sm:flex-row gap-3">
                      <button
                        type="submit"
                        disabled={isOnlineSubmitting}
                        className="flex-1 bg-gradient-to-r from-[#0a5482] to-[#0e6ba8] hover:from-[#084266] hover:to-[#0a5482] text-white font-black text-xs sm:text-sm py-3.5 px-4 rounded-xl shadow-lg transition active:scale-95 disabled:opacity-50 flex items-center justify-center gap-2 cursor-pointer"
                      >
                        <span>✉️</span>
                        <span>{isOnlineSubmitting ? 'Đang gửi...' : 'Gửi Email Đăng Ký Học Thử'}</span>
                      </button>

                      <button
                        type="button"
                        onClick={handleChatZaloWithContent}
                        className="flex-1 bg-[#0068ff] hover:bg-[#0057d6] text-white font-black text-xs sm:text-sm py-3.5 px-4 rounded-xl shadow-lg transition active:scale-95 flex items-center justify-center gap-2 cursor-pointer"
                      >
                        <span>💬</span>
                        <span>Nhắn Zalo: {CONTACT_PHONE_DISPLAY}</span>
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* SYLLABUS MODAL */}
      {showSyllabusModal && currentCourse && (
        <div
          className="fixed inset-0 bg-slate-900/65 backdrop-blur-xs z-50 flex items-center justify-center p-4"
          onClick={() => setShowSyllabusModal(false)}
        >
          <div
            className="bg-white rounded-3xl w-full max-w-3xl max-h-[85vh] overflow-y-auto p-6 sm:p-8 shadow-2xl relative"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between pb-4 mb-5 border-b border-slate-200">
              <h2 className="text-xl font-black text-[#0a5482]">
                📋 {t('Courses Syllabus')} — {courseTitle}
              </h2>
              <button
                type="button"
                onClick={() => setShowSyllabusModal(false)}
                className="w-8 h-8 rounded-full bg-slate-100 hover:bg-rose-500 hover:text-white text-slate-600 font-bold flex items-center justify-center transition-colors"
              >
                ✕
              </button>
            </div>
            <div
              className="legacy-prose"
              dangerouslySetInnerHTML={{
                __html: fixLegacyHtmlContent(
                  currentCourse.cc_Outline ||
                    (lang === 'vi' ? currentCourse.cc_desc_vi : currentCourse.cc_desc) ||
                    'Đang cập nhật đề cương.'
                ),
              }}
            />
          </div>
        </div>
      )}
    </div>
  );
};
