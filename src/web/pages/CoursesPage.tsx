import React, { useEffect, useState } from 'react';
import { Link, useLocation, useNavigate, useParams } from 'react-router-dom';
import {
  Home,
  GraduationCap,
  Phone,
  MessageCircle,
  BookOpen,
  History,
  ChevronDown,
  ChevronUp,
} from 'lucide-react';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import { fixLegacyHtmlContent, updatePageSeo } from '../lib/utils';
import { trackTonyContact } from '../../lib/googleAnalytics';

const CONTACT_ZALO_URL = 'https://zalo.me/0935058688';
const CONTACT_PHONE = '0935058688';
const CONTACT_PHONE_DISPLAY = '0935 058 688';

// Button tap fires Contact only (prevents premature Lead inflation from cancelled calls / blocked WebView popups)
const trackCourseConversion = (method: 'Zalo' | 'Phone' | 'Messenger', courseName: string) => {
  trackTonyContact(method, courseName);
  try {
    const w = window as any;
    if (typeof w.fbq === 'function') {
      w.fbq('track', 'Contact', {
        site_domain: 'tonyenglish.vn',
        content_name: courseName,
        contact_method: method,
      });
    }
  } catch (e) {}
};

// Normalize legacy course naming typos / spacing for cleaner display
const normalizeCourseDisplayName = (raw: string): string =>
  (raw || '')
    .replace(/IGCSE\s*\/\s*Alevel/gi, 'IGCSE / A-Level')
    .replace(/Giao Tiếp Căn bản/g, 'Giao tiếp Căn bản')
    .trim();

// Hidden course IDs ("Ngữ pháp và Từ vựng" / Grammar and Vocabulary)
const isHiddenCourseCategory = (c: any) => {
  if (!c) return false;
  const id = Number(c.cc_id);
  const parentId = Number(c.cc_parent);
  const slug = (c.cc_name_url || '').trim().toLowerCase();
  return id === 112 || parentId === 112 || slug === 'grammar-and-vocabulary';
};

export const CoursesPage: React.FC = () => {
  const { slug } = useParams<{ slug?: string }>();
  const location = useLocation();
  const navigate = useNavigate();
  const { lang, t, options } = useApp();

  const scrollToCourseTop = () => {
    if (typeof window === 'undefined') return;
    window.scrollTo({ top: 0, left: 0, behavior: 'auto' });
    document.documentElement.scrollTop = 0;
    document.body.scrollTop = 0;
    requestAnimationFrame(() => {
      window.scrollTo({ top: 0, left: 0, behavior: 'auto' });
    });
  };

  const [allCategories, setAllCategories] = useState<any[]>([]);
  const [categoriesLoaded, setCategoriesLoaded] = useState(false);
  const [currentCourse, setCurrentCourse] = useState<any | null>(null);
  const [openParentId, setOpenParentId] = useState<number | null>(null);
  const [mobileCateOpen, setMobileCateOpen] = useState(false);
  const [showMobileStickyBar, setShowMobileStickyBar] = useState(false);
  const [showLegacyGallery, setShowLegacyGallery] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setShowMobileStickyBar(window.scrollY > 360);
    };
    handleScroll();
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Load course categories once on mount (removed 3 unused LMS curriculum queries for faster landing page load)
  useEffect(() => {
    async function loadCourseCategories() {
      try {
        const { data } = await supabase
          .from('te_course_category')
          .select('*')
          .eq('deleted', 0)
          .eq('cc_status', 1)
          .order('cc_order', { ascending: true });

        if (data) {
          const visibleCategories = data.filter((c: any) => !isHiddenCourseCategory(c));
          setAllCategories(visibleCategories);
        }
      } finally {
        setCategoriesLoaded(true);
      }
    }
    loadCourseCategories();
  }, []);

  // Jump to top immediately whenever user navigates to a different course slug
  useEffect(() => {
    scrollToCourseTop();
  }, [slug, location.pathname, location.search]);

  const hasRequestedCourseSlug = (() => {
    if (slug && slug.toLowerCase() !== 'online') return true;
    try {
      const params = new URLSearchParams(location.search);
      return Boolean(params.get('course'));
    } catch {
      return false;
    }
  })();

  // Resolve currentCourse synchronously from loaded categories whenever slug changes
  useEffect(() => {
    if (allCategories.length === 0) return;

    let effectiveSlug = slug && slug.toLowerCase() !== 'online' ? slug : '';
    if (!effectiveSlug) {
      try {
        const params = new URLSearchParams(location.search);
        const courseQuery = (params.get('course') || '').toLowerCase();
        if (courseQuery.includes('igcse') || courseQuery.includes('cambridge')) {
          effectiveSlug = 'luyen-thi-igcse-alevel-cap-toc';
        } else if (courseQuery.includes('ielts')) {
          effectiveSlug = 'ielts';
        } else if (courseQuery.includes('sat')) {
          effectiveSlug = 'luyen-thi-sat-cap-toc';
        }
      } catch (e) {}
    }

    if (effectiveSlug) {
      const cleanSlug = decodeURIComponent(effectiveSlug)
        .trim()
        .replace(/\.html$/i, '');
      const found = allCategories.find((c: any) => (c.cc_name_url || '').trim() === cleanSlug);
      if (found) {
        setCurrentCourse(found);
        setOpenParentId(found.cc_parent === 0 ? found.cc_id : found.cc_parent);
      } else {
        setCurrentCourse(null);
      }
    } else {
      setCurrentCourse(null);
      const firstParent = allCategories.find((c: any) => c.cc_parent === 0 && c.cc_homedisplay === 1);
      if (firstParent) setOpenParentId(firstParent.cc_id);
    }
  }, [slug, location.search, allCategories]);

  const isResolvingSpecificCourse = hasRequestedCourseSlug && !categoriesLoaded;

  const homeParents = allCategories.filter(
    (c) => Number(c.cc_parent) === 0 && Number(c.cc_homedisplay) === 1 && !isHiddenCourseCategory(c)
  );
  const subCategories = (parentId: number) =>
    allCategories.filter((c) => Number(c.cc_parent) === Number(parentId) && !isHiddenCourseCategory(c));

  const courseTitle = currentCourse
    ? normalizeCourseDisplayName(
        lang === 'vi' ? currentCourse.cc_name_vi || currentCourse.cc_name : currentCourse.cc_name
      )
    : t('Study at TonyEnglish');

  // Zalo fallback modal & clipboard states
  const [zaloFallbackHint, setZaloFallbackHint] = useState(false);
  const [showZaloModal, setShowZaloModal] = useState(false);
  const [copiedPhone, setCopiedPhone] = useState(false);

  const copyPhoneToClipboard = () => {
    let copied = false;
    try {
      const ta = document.createElement('textarea');
      ta.value = CONTACT_PHONE;
      ta.setAttribute('readonly', '');
      ta.style.position = 'fixed';
      ta.style.top = '-9999px';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      ta.setSelectionRange(0, CONTACT_PHONE.length);
      copied = document.execCommand('copy');
      document.body.removeChild(ta);
    } catch (e) {}
    try {
      if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
        navigator.clipboard.writeText(CONTACT_PHONE).catch(() => {});
        copied = true;
      }
    } catch (e) {}
    if (copied) {
      setCopiedPhone(true);
    }
  };

  const handleCopyPhone = () => {
    copyPhoneToClipboard();
    setCopiedPhone(true);
  };

  const handleZaloClick = (e: React.MouseEvent<HTMLElement>, cTitle: string) => {
    trackCourseConversion('Zalo', cTitle);
    copyPhoneToClipboard();
    const ua = typeof navigator !== 'undefined' ? navigator.userAgent || '' : '';
    const isMobileOrInApp = /FBAN|FBIOS|FB_IAB|Instagram|TikTok|Line|iPhone|iPad|iPod|Android/i.test(ua);
    if (isMobileOrInApp) {
      // Prevent Facebook In-App Browser from stranding users on zalo.me's blank white screen
      e.preventDefault();
      setZaloFallbackHint(true);
      setShowZaloModal(true);
    }
  };

  useEffect(() => {
    if (!showZaloModal) return;
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setShowZaloModal(false);
    };
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [showZaloModal]);

  const handleProseClick = (e: React.MouseEvent<HTMLDivElement>) => {
    const anchor = (e.target as HTMLElement | null)?.closest('a');
    if (!anchor) return;
    const href = (anchor.getAttribute('href') || '').trim();
    if (/zalo\.me/i.test(href)) {
      handleZaloClick(e, courseTitle);
      return;
    }
    if (/^tel:/i.test(href)) {
      trackCourseConversion('Phone', courseTitle);
      return;
    }
    const internalMatch = href.match(/^(?:https?:\/\/(?:www\.)?tonyenglish\.vn)?(\/.*)$/i);
    if (
      internalMatch &&
      !e.metaKey &&
      !e.ctrlKey &&
      !e.shiftKey &&
      !e.altKey &&
      anchor.getAttribute('target') !== '_blank'
    ) {
      e.preventDefault();
      navigate(internalMatch[1]);
      scrollToCourseTop();
    }
  };

  const rawCourseDescHtml = currentCourse
    ? lang === 'vi'
      ? currentCourse.cc_desc_vi || currentCourse.cc_desc
      : currentCourse.cc_desc || currentCourse.cc_desc_vi
    : options['studyEnglish'] || '';

  // Ensure any tuition fee text inside legacy HTML descriptions always displays "Liên hệ"
  // and map any legacy 2017 screenshot URLs to the new 2026 web screenshots
  const baseCourseDescHtml = rawCourseDescHtml
    .replace(/25\s*triệu\s*\(1\s*kèm\s*1\)\s*hoặc\s*35\s*triệu\s*\(1\s*kèm\s*2\)/gi, 'Liên hệ')
    .replace(/18\s*triệu\s*\/\s*gói/gi, 'Liên hệ')
    .replace(/https?:\/\/image\.ibb\.co\/e244MF\/2017_01_23_3\.png/g, '/images/web-2026/01_bai_giang_ngu_am_1.png')
    .replace(/https?:\/\/image\.ibb\.co\/eXAdgF\/2017_01_23_1\.png/g, '/images/web-2026/02_bai_giang_ngu_am_2.png')
    .replace(/https?:\/\/image\.ibb\.co\/nrCDFa\/2017_01_23_2\.png/g, '/images/web-2026/03_goc_hoc_vien_ai.png')
    .replace(/https?:\/\/image\.ibb\.co\/eV611F\/2017_01_23_5\.png/g, '/images/web-2026/04_lich_bao_bai.png')
    .replace(/https?:\/\/image\.ibb\.co\/kRtHQa\/2017_01_23_6\.png/g, '/images/web-2026/05_bai_giang_igcse_song_ngu.png')
    .replace(/https?:\/\/image\.ibb\.co\/fASNrF\/2017_01_17_1\.png/g, '/images/web-2026/06_thu_vien_click_dup_tra_tu.png')
    .replace(/https?:\/\/image\.ibb\.co\/gcTj5a\/2017_01_23_7\.png/g, '/images/web-2026/07_thu_vien_cambridge_song_ngu.png')
    .replace(/https?:\/\/image\.ibb\.co\/mK97Qa\/2017_01_17_2\.png/g, '/images/web-2026/08_tu_dien_anh_viet.png')
    .replace(/https?:\/\/image\.ibb\.co\/ktVE5a\/2017_01_17_3\.png/g, '/images/web-2026/09_tu_dien_viet_anh.png')
    .replace(/https?:\/\/image\.ibb\.co\/nEwAdv\/2017_01_17_5\.png/g, '/images/web-2026/10_kho_video_phu_de.png');

  const courseDescHtml =
    !currentCourse && !baseCourseDescHtml.includes('/courses/ielts')
      ? baseCourseDescHtml
          .replace(
            /<strong>\s*Nghe\s*[–-]\s*Nói\s+phản\s+xạ\s*<\/strong>/gi,
            '<a href="/courses/english-communication%201"><strong>Nghe – Nói phản xạ</strong></a>'
          )
          .replace(
            /<strong>\s*IELTS,\s*Cambridge\s*IGCSE\s*\/\s*A-Level\s*và\s*Digital\s*SAT\s*<\/strong>/gi,
            '<a href="/courses/ielts"><strong>IELTS</strong></a>, <a href="/courses/luyen-thi-igcse-alevel-cap-toc"><strong>Cambridge IGCSE / A-Level</strong></a> và <a href="/courses/luyen-thi-sat-cap-toc"><strong>Digital SAT</strong></a>'
          )
      : baseCourseDescHtml;

  useEffect(() => {
    updatePageSeo(courseTitle, courseDescHtml);
  }, [courseTitle, courseDescHtml]);

  const childCoursesOfCurrent = currentCourse ? subCategories(currentCourse.cc_id) : [];

  const getCourseVisualConfig = (course: any | null) => {
    const cid = course ? Number(course.cc_id) : 0;
    const pid = course ? Number(course.cc_parent) : 0;

    if (cid === 127 || pid === 127) {
      return {
        image: '/images/courses/course-ielts.jpg',
        badge: lang === 'vi' ? '🏆 LUYỆN THI IELTS 4 KỸ NĂNG CẤP TỐC' : '🏆 INTENSIVE IELTS 4 SKILLS',
        caption:
          lang === 'vi'
            ? 'Rèn tư duy logic giải đề sắc bén cùng Thầy Tony (Cựu DHS Anh Quốc) & Phòng thi máy tính chuẩn IDP/BC'
            : 'Master IELTS 4 skills with British-trained mentorship & Computer-based Mock Tests',
        highlights:
          lang === 'vi'
            ? [
                '💻 Phòng thi thử chuẩn 100% IDP/BC',
                '✍️ Chấm chữa chi tiết Writing & Speaking',
                '🎁 Tặng 1 buổi Test & 2 buổi học thử',
              ]
            : ['💻 100% IDP/BC Mock Exam Lab', '✍️ Detailed Writing & Speaking Feedback', '🎁 Free Placement Test & 2 Trial Lessons'],
      };
    }

    if (cid === 132 || pid === 132) {
      return {
        image: '/images/courses/course-igcse.jpg',
        badge: lang === 'vi' ? '🌍 CHƯƠNG TRÌNH QUỐC TẾ CAMBRIDGE IGCSE & A-LEVEL' : '🌍 CAMBRIDGE IGCSE & A-LEVEL',
        caption:
          lang === 'vi'
            ? 'Xây gốc thuật ngữ học thuật & Luyện 600+ đề Past Papers đạt điểm A/A* các môn Toán, Khoa học, Kinh tế, Kinh doanh, Địa lý, ESL'
            : 'Build academic terminology & practice 600+ Past Papers to achieve A/A* grades',
        highlights:
          lang === 'vi'
            ? [
                '🧬 Bài giảng Song ngữ Anh - Việt & Mô phỏng',
                '📊 Sciences, Maths, Economics, Business, ESL',
                '📝 Chấm bài theo sát Marking Scheme Cambridge',
              ]
            : ['🧬 Bilingual Interactive Lectures', '📊 Sciences, Maths, Economics, Business, ESL', '📝 Cambridge Marking Scheme Grading'],
      };
    }

    if (cid === 133 || pid === 133) {
      return {
        image: '/images/courses/course-sat.jpg',
        badge: lang === 'vi' ? '🎯 LUYỆN THI DIGITAL SAT CẤP TỐC' : '🎯 DIGITAL SAT PREPARATION',
        caption:
          lang === 'vi'
            ? 'Làm chủ tư duy Đọc hiểu học thuật (Reading & Writing) và Toán SAT (Math) theo cấu trúc Digital SAT mới nhất'
            : 'Master Digital SAT Reading & Writing and Math with targeted strategies',
        highlights:
          lang === 'vi'
            ? [
                '📐 Chiến thuật giải nhanh SAT Math & Desmos',
                '📖 Phân tích chuyên sâu Reading & Writing',
                '🔥 Kho đề thực chiến bám sát College Board',
              ]
            : ['📐 Fast SAT Math & Desmos Strategies', '📖 Deep Reading & Writing Analysis', '🔥 Authentic College Board Practice'],
      };
    }

    if (cid === 111 || pid === 111) {
      return {
        image: '/images/courses/course-comm-basic.jpg',
        badge: lang === 'vi' ? '🎙️ GIAO TIẾP CĂN BẢN, PHÁT ÂM IPA & PHẢN XẠ' : '🎙️ BASIC COMMUNICATION & PRONUNCIATION',
        caption:
          lang === 'vi'
            ? 'Chuẩn hóa phát âm Anh - Anh (British English), xóa bỏ nỗi sợ nói và hình thành phản xạ giao tiếp tự nhiên'
            : 'Master British English pronunciation, build speaking confidence and natural reflexes',
        highlights:
          lang === 'vi'
            ? [
                '🗣️ Chuẩn hóa 44 âm IPA & Ngữ điệu tự nhiên',
                '⚡ Phản xạ nghe - nói qua 28+ chủ đề thực tế',
                '🎧 Podcast hội thoại song ngữ & Luyện nói AI',
              ]
            : ['🗣️ Standard 44 IPA Sounds & Intonation', '⚡ 28+ Real-life Speaking Topics', '🎧 Bilingual Podcasts & AI Speaking'],
      };
    }

    if (cid === 129 || pid === 129) {
      return {
        image: '/images/courses/course-comm-advanced.jpg',
        badge: lang === 'vi' ? '💼 GIAO TIẾP NÂNG CAO, VĂN PHÒNG & THƯƠNG MẠI' : '💼 ADVANCED & BUSINESS ENGLISH',
        caption:
          lang === 'vi'
            ? 'Làm chủ tiếng Anh công sở, đàm phán kinh doanh, viết Email thương mại chuyên nghiệp và Thành ngữ bản xứ'
            : 'Excel in corporate English, business negotiations, professional emails & idioms',
        highlights:
          lang === 'vi'
            ? [
                '🏢 13 Chuyên đề Tiếng Anh Văn phòng & Tài chính',
                '✉️ Kỹ năng viết Email & Thư tín thương mại',
                '💬 Phương pháp 3 Bước luyện trí nhớ độc quyền',
              ]
            : ['🏢 13 Corporate & Finance Topics', '✉️ Professional Business Email Writing', '💬 3-Step Memory Retention Method'],
      };
    }

    return {
      image: '/images/courses/course-overview.jpg',
      badge:
        lang === 'vi'
          ? '🇬🇧 LỚP GIA SƯ 1 KÈM 1 CÙNG THẦY TONY (ANH NGỮ & CAMBRIDGE)'
          : '🇬🇧 1-ON-1 PRIVATE TUTORING WITH MR. TONY',
      caption:
        lang === 'vi'
          ? 'Gia sư 1 kèm 1 trực tiếp tại nhà riêng của Thầy Tony (R2B Royal City) & Online, kết hợp Bài giảng Song ngữ, Kho 1.800+ Đề thi & AI 24/7'
          : 'Personalized 1-on-1 private tutoring at Mr. Tony’s home (R2B Royal City) & Online with 24/7 AI-powered self-study resources',
      highlights:
        lang === 'vi'
          ? [
              '🎯 Kèm gia sư cá nhân 1-1 cùng Thầy Tony',
              '🎧 450+ Bài giảng Song ngữ & Podcast',
              '🤖 Phòng thi chuẩn Quốc tế & AI Chấm chữa 24/7',
            ]
          : ['🎯 1-on-1 Private Tutoring with Mr. Tony', '🎧 450+ Bilingual Lectures & Podcasts', '🤖 24/7 AI Grading & Exam Lab'],
    };
  };

  return (
    <div className="max-w-7xl mx-auto px-3.5 sm:px-6 py-4 sm:py-8">
      {/* BREADCRUMB */}
      <nav className="flex items-center gap-1.5 sm:gap-2 text-xs sm:text-[15px] font-semibold text-slate-500 mb-3.5 sm:mb-6 flex-wrap">
        <Link to="/" className="hover:text-[#0a5482] inline-flex items-center gap-1.5">
          <Home className="w-3.5 h-3.5 text-[#0a5482]" />
          <span>{t('Home')}</span>
        </Link>
        <span>/</span>
        <Link to="/courses" className="hover:text-[#0a5482]">
          {t('Courses')}
        </Link>
        <span>/</span>
        <span className="text-[#0a5482] font-bold">
          {isResolvingSpecificCourse ? (lang === 'vi' ? 'Đang tải khóa học...' : 'Loading course...') : courseTitle}
        </span>
      </nav>

      <div className="flex flex-col lg:flex-row gap-4 sm:gap-8 xl:gap-12 items-start">
        {/* LEFT SIDEBAR: UNIFIED COURSES MENU */}
        <aside className="w-full lg:w-[260px] xl:w-[270px] shrink-0 bg-white rounded-2xl border border-slate-200/80 shadow-2xs overflow-hidden lg:sticky lg:top-24">
          <button
            type="button"
            onClick={() => setMobileCateOpen((prev) => !prev)}
            className="w-full bg-slate-100/80 px-4 py-3 border-b border-slate-200/70 flex items-center justify-between lg:pointer-events-none cursor-pointer text-left"
          >
            <h2 className="text-slate-600 lg:text-slate-500 font-bold text-xs uppercase tracking-widest flex items-center gap-2 min-w-0">
              <GraduationCap className="w-4 h-4 text-[#0a5482] shrink-0" />
              <span className="hidden lg:inline shrink-0">{t('Courses')}</span>
              <span className="lg:hidden font-bold text-[#0a5482] text-[13px] normal-case tracking-normal truncate">
                {isResolvingSpecificCourse ? (lang === 'vi' ? 'Đang tải...' : 'Loading...') : courseTitle}
              </span>
            </h2>
            <span className="lg:hidden text-[11px] font-bold text-[#0a5482] bg-white px-2.5 py-1 rounded-lg border border-slate-200/80 shadow-2xs inline-flex items-center gap-1 shrink-0 ml-2">
              <span>
                {mobileCateOpen
                  ? lang === 'vi'
                    ? 'Thu gọn'
                    : 'Hide'
                  : lang === 'vi'
                  ? 'Danh mục'
                  : 'Categories'}
              </span>
              {mobileCateOpen ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
            </span>
          </button>

          <div className={`${mobileCateOpen ? 'block' : 'hidden'} lg:block`}>
            <ul className="divide-y divide-slate-100 text-[14.5px] p-2 space-y-1">
              <li className="py-0.5">
                <Link
                  to="/courses"
                  onClick={() => {
                    setMobileCateOpen(false);
                    scrollToCourseTop();
                  }}
                  className={`block px-3.5 py-3 rounded-xl transition-colors relative ${
                    !currentCourse
                      ? "bg-sky-50/90 text-[#0a5482] font-semibold pl-4 before:content-[''] before:absolute before:left-1.5 before:top-2 before:bottom-2 before:w-1 before:rounded-full before:bg-[#2ab4e8]"
                      : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                  }`}
                >
                  {t('Study at TonyEnglish')}
                </Link>
              </li>

              {homeParents.length === 0 && (
                <li className="py-2 px-2 space-y-2 animate-pulse">
                  {[1, 2, 3, 4].map((n) => (
                    <div key={n} className="h-9 rounded-xl bg-slate-100" />
                  ))}
                </li>
              )}

              {homeParents.map((parent) => {
                const subs = subCategories(parent.cc_id);
                const isOpen =
                  openParentId === parent.cc_id ||
                  (currentCourse &&
                    (currentCourse.cc_id === parent.cc_id || currentCourse.cc_parent === parent.cc_id));
                const parentName = normalizeCourseDisplayName(
                  lang === 'vi' ? parent.cc_name_vi || parent.cc_name : parent.cc_name
                );
                const isCurrentParent = currentCourse && currentCourse.cc_id === parent.cc_id;

                return (
                  <li key={parent.cc_id} className="py-0.5">
                    <div className="flex items-center justify-between">
                      <Link
                        to={`/courses/${(parent.cc_name_url || '').trim()}`}
                        onClick={() => {
                          setOpenParentId(parent.cc_id);
                          if (subs.length === 0) setMobileCateOpen(false);
                          scrollToCourseTop();
                        }}
                        className={`flex-1 px-3.5 py-3 rounded-xl transition-colors flex items-center justify-between relative ${
                          isCurrentParent
                            ? "bg-sky-50/90 text-[#0a5482] font-semibold pl-4 before:content-[''] before:absolute before:left-1.5 before:top-2 before:bottom-2 before:w-1 before:rounded-full before:bg-[#2ab4e8]"
                            : isOpen
                            ? 'text-[#0a5482] font-semibold bg-slate-50/70'
                            : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                        }`}
                      >
                        <span className="leading-snug pr-1">{parentName}</span>
                        {subs.length > 0 && (
                          <span
                            className={`text-xs transition-transform shrink-0 ${
                              isOpen ? 'rotate-90 text-[#2ab4e8]' : 'text-slate-400'
                            }`}
                          >
                            ▸
                          </span>
                        )}
                      </Link>
                    </div>

                    {subs.length > 0 && isOpen && (
                      <ul className="mt-1 mb-1.5 ml-3 pl-2.5 border-l border-slate-200/80 space-y-1">
                        {subs.map((sub) => {
                          const subName = lang === 'vi' ? sub.cc_name_vi || sub.cc_name : sub.cc_name;
                          const isActiveSub = currentCourse && currentCourse.cc_id === sub.cc_id;
                          return (
                            <li key={sub.cc_id}>
                              <Link
                                to={`/courses/${(sub.cc_name_url || '').trim()}`}
                                onClick={() => {
                                  setMobileCateOpen(false);
                                  scrollToCourseTop();
                                }}
                                className={`block px-3 py-2.5 rounded-lg text-[13.5px] transition-all relative ${
                                  isActiveSub
                                    ? "bg-sky-50 text-[#0a5482] font-semibold pl-3.5 before:content-[''] before:absolute before:left-1 before:top-1.5 before:bottom-1.5 before:w-0.5 before:rounded-full before:bg-[#2ab4e8]"
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
          </div>
        </aside>

        {/* RIGHT MAIN CONTENT */}
        <div className="flex-1 min-w-0 w-full space-y-6">
          <div className="bg-white rounded-2xl sm:rounded-3xl border border-slate-200/90 shadow-sm overflow-hidden">
            {/* Section Header (Unified with Library / NewsPage Header) */}
            <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-4 sm:px-8 py-4 sm:py-6 text-white flex items-center justify-between flex-wrap gap-3 sm:gap-4">
              <div>
                <div className="text-[11px] sm:text-sm font-extrabold uppercase tracking-widest text-[#2ab4e8] mb-0.5 sm:mb-1">
                  {lang === 'vi' ? 'Lớp Gia Sư 1 Kèm 1 Cùng Thầy Tony' : '1-on-1 Private Tutoring with Mr. Tony'}
                </div>
                {isResolvingSpecificCourse ? (
                  <div className="h-8 sm:h-9 w-64 sm:w-80 bg-white/15 rounded-xl animate-pulse mt-1" />
                ) : (
                  <h1 className="text-xl sm:text-3xl font-black tracking-tight">{courseTitle}</h1>
                )}
              </div>
            </div>

            {isResolvingSpecificCourse ? (
              <div className="p-4 sm:p-8 space-y-5 animate-pulse">
                <div className="h-28 rounded-2xl bg-sky-50 border border-sky-100" />
                <div className="space-y-3 max-w-[74ch]">
                  <div className="h-6 bg-slate-100 rounded-lg w-2/3" />
                  <div className="h-4 bg-slate-100 rounded w-full" />
                  <div className="h-4 bg-slate-100 rounded w-11/12" />
                  <div className="h-4 bg-slate-100 rounded w-4/5" />
                  <div className="h-44 bg-slate-100 rounded-2xl w-full mt-4" />
                </div>
              </div>
            ) : (
            <div className="p-4 sm:p-8 space-y-6">

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
                        onClick={scrollToCourseTop}
                        className="bg-white hover:bg-sky-50 border border-slate-200 rounded-xl p-4 flex items-center justify-between group transition shadow-2xs"
                      >
                        <div>
                          <div className="font-extrabold text-[15px] sm:text-base text-slate-800 group-hover:text-[#0a5482]">
                            {lang === 'vi' ? sub.cc_name_vi || sub.cc_name : sub.cc_name}
                          </div>
                          <div className="text-xs sm:text-sm text-slate-500 mt-0.5">
                            {t('Tuition fee')}:{' '}
                            <strong className="text-[#0a5482]">{lang === 'vi' ? 'Liên hệ' : 'Contact Mr. Tony'}</strong>
                          </div>
                        </div>
                        <span className="text-[#2ab4e8] font-black group-hover:translate-x-1 transition-transform">
                          →
                        </span>
                      </Link>
                    ))}
                  </div>
                </div>
              )}

              {/* Quick Above-the-Fold Direct Call & Zalo Box */}
              <div
                id="khung-dang-ky-tu-van"
                className="rounded-2xl bg-gradient-to-br from-sky-50 via-blue-50/80 to-emerald-50/60 border border-sky-200/90 p-4 sm:p-5 space-y-3 shadow-xs"
              >
                <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-3.5">
                  <div className="space-y-1.5">
                    <div className="inline-flex items-start sm:items-center gap-1.5 text-[11px] sm:text-xs font-extrabold uppercase tracking-wide text-emerald-800 bg-emerald-100/80 border border-emerald-200 px-3 py-1 sm:py-0.5 rounded-2xl sm:rounded-full leading-snug">
                      <span className="shrink-0">🏠</span>
                      <span>
                        {lang === 'vi'
                          ? 'Học tại căn hộ nhà riêng Thầy Tony (R2B 2219 Royal City) & Online'
                          : 'At Mr. Tony’s Residence (R2B 2219 Royal City) & Online'}
                      </span>
                    </div>
                    <div className="text-sm sm:text-base font-black text-[#0a5482] leading-snug">
                      {lang === 'vi'
                        ? '🎁 Kiểm tra đầu vào & Học thử miễn phí 2–3 buổi — Con thấy thật sự hợp thầy, hợp phương pháp mới đăng ký!'
                        : '🎁 Free Placement Test & 2–3 Trial Lessons — Only enroll if it truly fits your child!'}
                    </div>
                    <p className="text-xs sm:text-sm text-slate-600 font-medium">
                      {lang === 'vi'
                        ? 'Quý phụ huynh gọi trực tiếp hoặc bấm Zalo để thầy Tony tư vấn lộ trình & xếp lịch học thử cho con:'
                        : 'Please call directly or message via Zalo for personalized consultation with Mr. Tony:'}
                    </p>
                  </div>

                  <div className="flex flex-wrap items-center gap-2.5 shrink-0">
                    <a
                      href={`tel:${CONTACT_PHONE}`}
                      onClick={() => trackCourseConversion('Phone', courseTitle)}
                      className="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs sm:text-sm px-4 py-2.5 rounded-xl shadow-xs transition whitespace-nowrap"
                    >
                      <Phone className="w-4 h-4 shrink-0" />
                      <span>{lang === 'vi' ? `Gọi: ${CONTACT_PHONE_DISPLAY}` : `Call: ${CONTACT_PHONE_DISPLAY}`}</span>
                    </a>

                    <a
                      href={CONTACT_ZALO_URL}
                      target="_blank"
                      rel="noreferrer"
                      onClick={(e) => handleZaloClick(e, courseTitle)}
                      className="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 bg-[#0068ff] hover:bg-[#0057d6] text-white font-extrabold text-xs sm:text-sm px-4 py-2.5 rounded-xl shadow-xs transition whitespace-nowrap"
                    >
                      <MessageCircle className="w-4 h-4 shrink-0" />
                      <span>{lang === 'vi' ? `Zalo: ${CONTACT_PHONE_DISPLAY}` : `Zalo: ${CONTACT_PHONE_DISPLAY}`}</span>
                    </a>
                  </div>
                </div>

                {/* Fallback helper when Facebook/Instagram In-App Browser blocks jumping directly to Zalo app */}
                {zaloFallbackHint && (
                  <div className="rounded-xl bg-amber-50 border border-amber-200 px-3.5 py-2.5 flex flex-wrap items-center justify-between gap-2 text-xs text-amber-950 font-semibold">
                    <span>
                      ✅ Đã copy số Zalo <strong>0935 058 688</strong> — Nếu trình duyệt Facebook chặn chuyển app, anh/chị mở <strong>Zalo</strong> rồi dán số vào ô Tìm kiếm nhé:
                    </span>
                    <button
                      type="button"
                      onClick={handleCopyPhone}
                      className="px-3 py-1.5 rounded-lg bg-white border border-amber-300 text-amber-900 font-extrabold hover:bg-amber-100 transition cursor-pointer shrink-0"
                    >
                      {copiedPhone ? '✅ Đã copy 0935058688' : '📋 Copy SĐT: 0935 058 688'}
                    </button>
                  </div>
                )}
              </div>

              {/* Course Description HTML */}
              {courseDescHtml && (
                <div className="pt-2 sm:pt-3 space-y-6">
                  <div
                    className="legacy-prose course-tab-prose text-left sm:text-justify max-w-[74ch]"
                    onClick={handleProseClick}
                    dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(courseDescHtml) }}
                  />
                  <div className="rounded-xl bg-sky-50/90 border border-sky-200 px-4 py-3.5 flex flex-wrap items-center justify-between gap-2">
                    <div className="space-y-0.5">
                      <div className="text-sm sm:text-base font-extrabold text-slate-800">
                        💳 {lang === 'vi' ? 'Học phí:' : 'Tuition fee:'}{' '}
                        <span className="text-[#0a5482] font-black">
                          {lang === 'vi' ? 'Liên hệ' : 'Contact Mr. Tony'}
                        </span>
                      </div>
                      <div className="text-xs sm:text-[13px] font-bold text-emerald-700">
                        {lang === 'vi'
                          ? '✨ Học thử miễn phí 2–3 buổi tại R2B Royal City — Thấy thật sự hợp thầy mới đăng ký'
                          : '✨ 2–3 Free Trial Lessons at R2B Royal City before enrollment'}
                      </div>
                    </div>
                    <div className="text-xs sm:text-sm font-bold text-slate-600">
                      Hotline / Zalo Thầy Tony: <strong className="text-[#0a5482]">{CONTACT_PHONE_DISPLAY}</strong>
                    </div>
                  </div>
                </div>
              )}

              {/* Keepsake Archive: Legacy 2013-2017 Web Interface Screenshots */}
              {!currentCourse && (
                <div className="rounded-2xl border border-amber-200/80 bg-amber-50/50 overflow-hidden">
                  <button
                    type="button"
                    onClick={() => setShowLegacyGallery((prev) => !prev)}
                    className="w-full px-4 sm:px-5 py-3.5 flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 sm:gap-3 text-left hover:bg-amber-100/50 transition cursor-pointer"
                  >
                    <div className="flex items-start sm:items-center gap-2.5 min-w-0">
                      <span className="w-8 h-8 rounded-xl bg-amber-100 border border-amber-200/80 text-amber-800 flex items-center justify-center shrink-0 mt-0.5 sm:mt-0">
                        <History className="w-4 h-4" />
                      </span>
                      <div className="min-w-0">
                        <div className="font-extrabold text-[13px] sm:text-sm text-amber-950 leading-snug">
                          Góc Kỷ Niệm: Giao diện TonyEnglish phiên bản đầu tiên (2013 – 2017)
                        </div>
                        <div className="text-[11.5px] text-amber-800/85 font-medium leading-relaxed mt-0.5">
                          Lưu trữ 10 hình ảnh chụp màn hình kỷ niệm của trang web TonyEnglish thế hệ cũ
                        </div>
                      </div>
                    </div>
                    <span className="self-start sm:self-center inline-flex items-center gap-1 px-3 py-1.5 rounded-lg bg-white border border-amber-200 text-amber-900 font-bold text-xs shrink-0 shadow-2xs">
                      <span>{showLegacyGallery ? 'Thu gọn' : 'Xem ảnh kỷ niệm'}</span>
                      {showLegacyGallery ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
                    </span>
                  </button>

                  {showLegacyGallery && (
                    <div className="p-4 sm:p-6 border-t border-amber-200/70 bg-white space-y-5">
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {[
                          { src: '/images/legacy-2017/01_2017_01_23_3_bai_giang_ngu_am_1.png', caption: '1. Giao diện Bài giảng Ngữ âm: Vị trí Cấu Âm (2017)' },
                          { src: '/images/legacy-2017/02_2017_01_23_1_bai_giang_ngu_am_2.png', caption: '2. Giao diện Bài giảng Ngữ âm: Nguyên Âm Đơn (2017)' },
                          { src: '/images/legacy-2017/03_2017_01_23_2_muc_tin_nhan.png', caption: '3. Giao diện mục Tin nhắn trao đổi với Thầy Tony (2017)' },
                          { src: '/images/legacy-2017/04_2017_01_23_5_thong_bao_tin_nhan.png', caption: '4. Giao diện khi có thông báo tin nhắn mới (2017)' },
                          { src: '/images/legacy-2017/05_2017_01_23_6_cau_hinh_tai_khoan.png', caption: '5. Giao diện Cấu hình tài khoản & Chọn khóa học (2017)' },
                          { src: '/images/legacy-2017/06_2017_01_17_1_tra_tu_click_dup.png', caption: '6. Tính năng tra từ nhanh bằng Click đúp trong Thư viện (2017)' },
                          { src: '/images/legacy-2017/07_2017_01_23_7_so_tay_ghi_chep.png', caption: '7. Tính năng Sổ tay ghi chép từ vựng cá nhân (2017)' },
                          { src: '/images/legacy-2017/08_2017_01_17_2_tu_dien_anh_viet.png', caption: '8. Thanh tra từ điển từ Anh sang Việt (2017)' },
                          { src: '/images/legacy-2017/09_2017_01_17_3_tu_dien_viet_anh.png', caption: '9. Thanh tra từ điển từ Việt sang Anh (2017)' },
                          { src: '/images/legacy-2017/10_2017_01_17_5_tinh_nang_khac.png', caption: '10. Các tính năng Tìm kiếm, Nhận diện giọng nói & Dịch câu (2017)' },
                        ].map((item) => (
                          <div key={item.src} className="rounded-xl border border-slate-200 overflow-hidden bg-slate-50 shadow-2xs">
                            <img src={item.src} alt={item.caption} className="w-full h-auto object-cover" loading="lazy" />
                            <div className="px-3 py-2 text-center text-xs font-semibold text-slate-600 border-t border-slate-200/80">
                              {item.caption}
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              )}

              {/* Action Buttons for Course (Phone Call & Zalo Consultation) */}
              <div className="pt-6 border-t border-slate-200 flex flex-wrap items-center gap-3">
                <a
                  href={`tel:${CONTACT_PHONE}`}
                  onClick={() => trackCourseConversion('Phone', courseTitle)}
                  className="bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm px-5 py-3 rounded-xl shadow-md transition inline-flex items-center gap-2"
                >
                  <Phone className="w-4 h-4 shrink-0" />
                  <span>
                    {lang === 'vi'
                      ? `Gọi trực tiếp: ${CONTACT_PHONE_DISPLAY}`
                      : `Call directly: ${CONTACT_PHONE_DISPLAY}`}
                  </span>
                </a>

                <a
                  href={CONTACT_ZALO_URL}
                  target="_blank"
                  rel="noreferrer"
                  onClick={(e) => handleZaloClick(e, courseTitle)}
                  className="bg-[#0068ff] hover:bg-[#0057d6] text-white font-extrabold text-sm px-5 py-3 rounded-xl shadow-md transition inline-flex items-center gap-2"
                >
                  <MessageCircle className="w-4 h-4 shrink-0" />
                  <span>
                    {lang === 'vi'
                      ? `Tư vấn qua Zalo: ${CONTACT_PHONE_DISPLAY}`
                      : `Consult via Zalo: ${CONTACT_PHONE_DISPLAY}`}
                  </span>
                </a>
              </div>

              {/* BẢNG DANH MỤC CÁC KHÓA HỌC TẠI TONYENGLISH (KHỐI BẢNG LINK PHỄU CÓ ẢNH CÂN ĐỐI BÊN DƯỚI) */}
              {homeParents.length > 0 && (
                <div className="pt-6 border-t border-slate-200">
                  <div className="bg-slate-50 rounded-2xl border border-slate-200/90 overflow-hidden shadow-xs">
                    <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-5 py-4 text-white flex items-center gap-3">
                      <span className="w-9 h-9 rounded-xl bg-white/10 border border-white/15 text-[#2ab4e8] flex items-center justify-center shrink-0">
                        <BookOpen className="w-4 h-4" />
                      </span>
                      <div>
                        <h2 className="text-base sm:text-lg font-black tracking-tight">
                          {lang === 'vi'
                            ? 'Danh Mục Các Gói Gia Sư 1 Kèm 1 Cùng Thầy Tony'
                            : '1-on-1 Private Tutoring Packages with Mr. Tony'}
                        </h2>
                        <p className="text-xs text-sky-200 font-medium">
                          {lang === 'vi'
                            ? 'Bấm vào từng gói học bên dưới để xem chi tiết nội dung và lộ trình ôn luyện'
                            : 'Click on any tutoring package below to view full details'}
                        </p>
                      </div>
                    </div>

                    <div className="divide-y divide-slate-200/80 bg-white">
                      {homeParents.map((parent) => {
                        const subs = subCategories(parent.cc_id);
                        const parentName = normalizeCourseDisplayName(
                          lang === 'vi' ? parent.cc_name_vi || parent.cc_name : parent.cc_name
                        );
                        const parentUrl = `/courses/${(parent.cc_name_url || '').trim()}`;
                        const isActiveRow =
                          currentCourse &&
                          (currentCourse.cc_id === parent.cc_id || currentCourse.cc_parent === parent.cc_id);
                        const rowVisual = getCourseVisualConfig(parent);

                        let defaultSubjectsText = '';
                        if (Number(parent.cc_id) === 127) {
                          defaultSubjectsText =
                            lang === 'vi'
                              ? 'IELTS 4 Kỹ năng (Listening, Reading, Writing, Speaking) & Phòng thi máy tính chuẩn IDP/BC'
                              : 'IELTS 4 Skills (Listening, Reading, Writing, Speaking) & Computer-based Mock Tests';
                        } else if (Number(parent.cc_id) === 132) {
                          defaultSubjectsText =
                            lang === 'vi'
                              ? 'Cambridge IGCSE & A-Level: Maths (0580/0606), Sciences (0654/0610/0620/0625), Economics (0455), Business (0450), Geography (0460), ESL (0510)'
                              : 'Cambridge IGCSE & A-Level: Maths, Co-ordinated Sciences, Biology, Chemistry, Physics, Economics, Business, Geography, ESL';
                        } else if (Number(parent.cc_id) === 133) {
                          defaultSubjectsText =
                            lang === 'vi'
                              ? 'Digital SAT Reading & Writing, SAT Math chuyên sâu theo cấu trúc mới nhất'
                              : 'Digital SAT Reading & Writing, SAT Math';
                        }

                        return (
                          <div
                            key={parent.cc_id}
                            className={`p-4 sm:p-5 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4 hover:bg-sky-50/50 transition group ${
                              isActiveRow ? 'bg-sky-50/40' : ''
                            }`}
                          >
                            {/* Left: Vivid Course Thumbnail + Title & Sub-courses */}
                            <div className="flex flex-col sm:flex-row items-start sm:items-center gap-4 flex-1 min-w-0">
                              <Link
                                to={parentUrl}
                                onClick={scrollToCourseTop}
                                className="w-full sm:w-44 md:w-48 aspect-[16/10] rounded-xl overflow-hidden border border-slate-200 shadow-2xs shrink-0 relative bg-slate-900 block"
                              >
                                <img
                                  src={rowVisual.image}
                                  alt={parentName}
                                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                                />
                              </Link>

                              <div className="flex-1 min-w-0 space-y-2">
                                <div className="flex flex-wrap items-center gap-2">
                                  <Link
                                    to={parentUrl}
                                    onClick={scrollToCourseTop}
                                    className="font-black text-base sm:text-lg text-[#0a5482] hover:text-[#2ab4e8] transition leading-snug"
                                  >
                                    {parentName}
                                  </Link>
                                  {isActiveRow && (
                                    <span className="bg-emerald-100 text-emerald-800 text-[10px] font-black uppercase px-2 py-0.5 rounded-full border border-emerald-200">
                                      {lang === 'vi' ? 'Đang xem' : 'Viewing'}
                                    </span>
                                  )}
                                </div>

                                <p className="text-xs sm:text-[13.5px] text-slate-600 font-medium leading-relaxed">
                                  {defaultSubjectsText || rowVisual.caption}
                                </p>

                                <div className="text-xs sm:text-sm font-bold text-slate-700 flex flex-wrap items-center gap-x-2 gap-y-0.5">
                                  <span>
                                    💳 {lang === 'vi' ? 'Học phí:' : 'Tuition fee:'}{' '}
                                    <strong className="text-[#0a5482]">
                                      {lang === 'vi' ? 'Liên hệ' : 'Contact Mr. Tony'}
                                    </strong>
                                  </span>
                                  <span className="text-emerald-700 font-extrabold text-xs">
                                    {lang === 'vi'
                                      ? '• Học thử miễn phí 2–3 buổi thấy hợp mới đăng ký'
                                      : '• 2–3 Free Trial Lessons'}
                                  </span>
                                </div>

                                {subs.length > 0 && (
                                  <div className="flex flex-wrap gap-1.5 pt-0.5">
                                    {subs.map((sub) => (
                                      <Link
                                        key={sub.cc_id}
                                        to={`/courses/${(sub.cc_name_url || '').trim()}`}
                                        onClick={scrollToCourseTop}
                                        className="inline-flex items-center gap-1 text-xs font-bold text-[#0a5482] bg-slate-100 hover:bg-sky-100 border border-slate-200 hover:border-sky-300 px-2.5 py-1 rounded-lg transition"
                                      >
                                        <span>• {lang === 'vi' ? sub.cc_name_vi || sub.cc_name : sub.cc_name}</span>
                                        <span className="text-[#2ab4e8]">→</span>
                                      </Link>
                                    ))}
                                  </div>
                                )}
                              </div>
                            </div>

                            {/* Right: Direct Action Button */}
                            <div className="flex items-center sm:items-end justify-end shrink-0 pt-2 sm:pt-0 border-t sm:border-t-0 border-slate-100">
                              <Link
                                to={parentUrl}
                                onClick={scrollToCourseTop}
                                className="w-full sm:w-auto inline-flex items-center justify-center gap-1.5 bg-[#0a5482] hover:bg-[#084266] text-white font-bold text-xs sm:text-sm px-4 py-2.5 rounded-xl shadow-2xs transition whitespace-nowrap"
                              >
                                <span>{lang === 'vi' ? 'Xem chi tiết' : 'View course'}</span>
                                <span>→</span>
                              </Link>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                </div>
              )}
            </div>
            )}
          </div>
        </div>
      </div>

      {/* MOBILE STICKY BOTTOM BAR (Appears smoothly after scrolling past top CTA, never duplicates hero CTA) */}
      <div
        className={`sm:hidden fixed bottom-0 left-0 right-0 z-40 bg-white/95 backdrop-blur-md border-t border-slate-200/90 px-3 py-2 shadow-[0_-4px_20px_rgba(15,23,42,0.1)] grid grid-cols-2 gap-2 transition-all duration-300 ${
          showMobileStickyBar ? 'translate-y-0 opacity-100' : 'translate-y-full opacity-0 pointer-events-none'
        }`}
      >
        <a
          href={`tel:${CONTACT_PHONE}`}
          onClick={() => trackCourseConversion('Phone', courseTitle)}
          className="inline-flex items-center justify-center gap-1.5 bg-emerald-600 active:bg-emerald-700 text-white font-extrabold text-xs py-2.5 px-3 rounded-xl shadow-xs whitespace-nowrap"
        >
          <Phone className="w-3.5 h-3.5 shrink-0" />
          <span>{lang === 'vi' ? `Gọi: ${CONTACT_PHONE_DISPLAY}` : `Call: ${CONTACT_PHONE_DISPLAY}`}</span>
        </a>
        <a
          href={CONTACT_ZALO_URL}
          target="_blank"
          rel="noreferrer"
          onClick={(e) => handleZaloClick(e, courseTitle)}
          className="inline-flex items-center justify-center gap-1.5 bg-[#0068ff] active:bg-[#0057d6] text-white font-extrabold text-xs py-2.5 px-3 rounded-xl shadow-xs whitespace-nowrap"
        >
          <MessageCircle className="w-3.5 h-3.5 shrink-0" />
          <span>Zalo: {CONTACT_PHONE_DISPLAY}</span>
        </a>
      </div>

      {/* ANTI-BLOCK ZALO CONNECT MODAL FOR FACEBOOK/INSTAGRAM IN-APP BROWSERS */}
      {showZaloModal && (
        <div
          className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-3.5"
          onClick={() => setShowZaloModal(false)}
        >
          <div
            role="dialog"
            aria-modal="true"
            className="bg-white rounded-3xl max-w-md w-full overflow-hidden shadow-2xl border border-slate-200"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="bg-gradient-to-r from-[#0068ff] to-[#0a5482] px-5 py-4 text-white flex items-center justify-between gap-3">
              <div className="flex items-center gap-2.5">
                <span className="text-xl">💬</span>
                <div>
                  <h3 className="font-black text-base sm:text-lg leading-tight">
                    {lang === 'vi' ? 'Nhắn Zalo trực tiếp Thầy Tony' : 'Connect via Zalo with Mr. Tony'}
                  </h3>
                  <p className="text-[11px] sm:text-xs text-sky-100 font-medium">
                    R2B 2219 Royal City • Học thử 2–3 buổi miễn phí
                  </p>
                </div>
              </div>
              <button
                type="button"
                onClick={() => setShowZaloModal(false)}
                className="w-8 h-8 rounded-full bg-white/15 hover:bg-white/25 text-white font-black text-sm flex items-center justify-center cursor-pointer transition shrink-0"
                aria-label="Đóng"
              >
                ✕
              </button>
            </div>

            <div className="p-5 space-y-4">
              <div className="rounded-2xl bg-emerald-50 border border-emerald-200 p-3.5 flex items-center justify-between gap-2">
                <div>
                  <div className="text-[11px] font-extrabold uppercase tracking-wide text-emerald-700">
                    {copiedPhone ? '✅ Đã tự động sao chép số Zalo' : 'Số điện thoại / Zalo Thầy Tony'}
                  </div>
                  <div className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight mt-0.5">
                    {CONTACT_PHONE_DISPLAY}
                  </div>
                </div>
                <button
                  type="button"
                  onClick={handleCopyPhone}
                  className="px-3 py-2 rounded-xl bg-white border border-emerald-300 text-emerald-900 font-extrabold text-xs hover:bg-emerald-100 transition cursor-pointer shrink-0 shadow-2xs"
                >
                  {copiedPhone ? '✅ Đã copy' : '📋 Copy số'}
                </button>
              </div>

              <div className="rounded-xl bg-amber-50/90 border border-amber-200/90 px-3.5 py-2.5 text-xs sm:text-[13px] text-amber-950 leading-relaxed font-medium">
                💡 <strong>Mẹo mở nhanh từ Facebook:</strong> Hệ thống đã copy sẵn số <strong>0935058688</strong>. Nếu bấm nút bên dưới bị trình duyệt Facebook chặn, anh/chị chỉ cần mở app <strong>Zalo</strong> trên điện thoại → bấm ô <strong>Tìm kiếm</strong> → <strong>Dán (0935058688)</strong> là nhắn tin cho thầy được ngay ạ!
              </div>

              <div className="space-y-2.5 pt-0.5">
                <a
                  href={CONTACT_ZALO_URL}
                  target="_blank"
                  rel="noreferrer"
                  className="w-full inline-flex items-center justify-center gap-2 bg-[#0068ff] hover:bg-[#0057d6] text-white font-extrabold text-sm py-3 px-4 rounded-xl shadow-md transition"
                >
                  <span>💬</span>
                  <span>{lang === 'vi' ? 'Mở ứng dụng Zalo ngay' : 'Open Zalo App Now'}</span>
                </a>

                <a
                  href={`tel:${CONTACT_PHONE}`}
                  onClick={() => trackCourseConversion('Phone', courseTitle)}
                  className="w-full inline-flex items-center justify-center gap-2 bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm py-3 px-4 rounded-xl shadow-xs transition"
                >
                  <span>📞</span>
                  <span>
                    {lang === 'vi'
                      ? `Hoặc Gọi trực tiếp: ${CONTACT_PHONE_DISPLAY}`
                      : `Or Call Directly: ${CONTACT_PHONE_DISPLAY}`}
                  </span>
                </a>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
