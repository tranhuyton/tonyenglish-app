import React, { useEffect, useRef, useState } from 'react';
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
  ChevronLeft,
  ChevronRight,
  X,
  ZoomIn,
  Sparkles,
  Mic,
  Briefcase,
  Award,
  Globe,
  Target,
  MapPin,
  Gift,
  CreditCard,
} from 'lucide-react';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import { fixLegacyHtmlContent, updatePageSeo } from '../lib/utils';
import { trackTonyContact, trackUnifiedViewCourse } from '../../lib/googleAnalytics';
import { CourseShowcaseGallery } from '../components/CourseShowcaseGallery';
import { CourseGuideVideoCard } from '../components/CourseGuideVideoCard';

const CONTACT_ZALO_URL = 'https://zalo.me/0935058688';
const CONTACT_PHONE = '0935058688';
const CONTACT_PHONE_DISPLAY = '0935 058 688';

const WEB_2026_CAPTIONS: Record<string, string> = {
  '01_bai_giang_ngu_am_1.png': '1. Giao diện Bài giảng Ngữ âm: Vị trí Cấu Âm & Sơ đồ nguyên âm chuẩn Anh-Anh',
  '02_bai_giang_ngu_am_2.png': '2. Giao diện Bài giảng Ngữ âm: Hệ thống Nguyên Âm Đơn & Âm thanh tương tác',
  '03_goc_hoc_vien_ai.png': '3. Góc Học Viên tích hợp lộ trình cá nhân hóa & Trợ lý AI 24/7',
  '04_lich_bao_bai.png': '4. Lịch báo bài & theo dõi tiến độ học tập từng ngày cùng Thầy Tony',
  '05_bai_giang_igcse_song_ngu.png': '5. Bài giảng Song ngữ Cambridge IGCSE kèm Video & Audio giảng bài',
  '06_thu_vien_click_dup_tra_tu.png': '6. Thư viện đọc hiểu tích hợp Click đúp tra từ điển nhanh tức thì',
  '07_thu_vien_cambridge_song_ngu.png': '7. Thư viện tài liệu & sách học thuật Cambridge song ngữ Anh – Việt',
  '08_tu_dien_anh_viet.png': '8. Hệ thống Từ điển Anh – Việt tích hợp sẵn trên mọi trang học',
  '09_tu_dien_viet_anh.png': '9. Hệ thống Từ điển Việt – Anh tra cứu nhanh từ vựng & cụm từ',
  '10_kho_video_phu_de.png': '10. Kho Video luyện nghe có phụ đề song ngữ tương tác',
};

const WEB_2026_CAPTIONS_EN: Record<string, string> = {
  '01_bai_giang_ngu_am_1.png': '1. Interactive Phonetics Lecture: Places of Articulation & British Vowel Chart',
  '02_bai_giang_ngu_am_2.png': '2. Interactive Phonetics Lecture: Monophthong Vowels & Native Audio',
  '03_goc_hoc_vien_ai.png': '3. Student Portal with Personalised Roadmap & 24/7 AI Study Advisor',
  '04_lich_bao_bai.png': '4. Daily Assignment Calendar & Homework Progress Tracking with Mr. Tony',
  '05_bai_giang_igcse_song_ngu.png': '5. Bilingual Cambridge IGCSE Lectures with Video & Audio Walkthroughs',
  '06_thu_vien_click_dup_tra_tu.png': '6. Online Reading Library with Instant Double-Click Dictionary Lookup',
  '07_thu_vien_cambridge_song_ngu.png': '7. Side-by-Side Bilingual Cambridge IELTS Reading & Listening Library',
  '08_tu_dien_anh_viet.png': '8. Built-in English–Vietnamese Dictionary Available on Every Page',
  '09_tu_dien_viet_anh.png': '9. Built-in Vietnamese–English Bidirectional Vocabulary Lookup',
  '10_kho_video_phu_de.png': '10. Curated Video Store with Interactive Bilingual Subtitles',
};

const LEGACY_GALLERY_ITEMS = [
  { src: '/images/legacy-2017/01_2017_01_23_3_bai_giang_ngu_am_1.png', caption: '1. Giao diện Bài giảng Ngữ âm: Vị trí Cấu Âm (2017)', captionEn: '1. Phonetics Lecture Interface: Articulation Guide (2017)' },
  { src: '/images/legacy-2017/02_2017_01_23_1_bai_giang_ngu_am_2.png', caption: '2. Giao diện Bài giảng Ngữ âm: Nguyên Âm Đơn (2017)', captionEn: '2. Phonetics Lecture Interface: Vowel Monophthongs (2017)' },
  { src: '/images/legacy-2017/03_2017_01_23_2_muc_tin_nhan.png', caption: '3. Giao diện mục Tin nhắn trao đổi với Thầy Tony (2017)', captionEn: '3. Direct Messaging Inbox with Mr. Tony (2017)' },
  { src: '/images/legacy-2017/04_2017_01_23_5_thong_bao_tin_nhan.png', caption: '4. Giao diện khi có thông báo tin nhắn mới (2017)', captionEn: '4. New Message Notification Window (2017)' },
  { src: '/images/legacy-2017/05_2017_01_23_6_cau_hinh_tai_khoan.png', caption: '5. Giao diện Cấu hình tài khoản & Chọn khóa học (2017)', captionEn: '5. Account Settings & Course Selection Interface (2017)' },
  { src: '/images/legacy-2017/06_2017_01_17_1_tra_tu_click_dup.png', caption: '6. Tính năng tra từ nhanh bằng Click đúp trong Thư viện (2017)', captionEn: '6. Instant Double-Click Dictionary Lookup in Library (2017)' },
  { src: '/images/legacy-2017/07_2017_01_23_7_so_tay_ghi_chep.png', caption: '7. Tính năng Sổ tay ghi chép từ vựng cá nhân (2017)', captionEn: '7. Personal Vocabulary Notebook Tool (2017)' },
  { src: '/images/legacy-2017/08_2017_01_17_2_tu_dien_anh_viet.png', caption: '8. Thanh tra từ điển từ Anh sang Việt (2017)', captionEn: '8. English-to-Vietnamese Lookup Bar (2017)' },
  { src: '/images/legacy-2017/09_2017_01_17_3_tu_dien_viet_anh.png', caption: '9. Thanh tra từ điển từ Việt sang Anh (2017)', captionEn: '9. Vietnamese-to-English Lookup Bar (2017)' },
  { src: '/images/legacy-2017/10_2017_01_17_5_tinh_nang_khac.png', caption: '10. Các tính năng Tìm kiếm, Nhận diện giọng nói & Dịch câu (2017)', captionEn: '10. Search, Voice Recognition & Sentence Translation Tools (2017)' },
];

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

  const hasRequestedCourseSlug = (() => {
    if (slug && slug.toLowerCase() !== 'online') return true;
    try {
      const params = new URLSearchParams(location.search);
      return Boolean(params.get('course'));
    } catch {
      return false;
    }
  })();

  const [allCategories, setAllCategories] = useState<any[]>([]);
  const [categoriesLoaded, setCategoriesLoaded] = useState(false);
  const [currentCourse, setCurrentCourse] = useState<any | null>(null);
  const [openParentIds, setOpenParentIds] = useState<number[]>([]);
  const [mobileCateOpen, setMobileCateOpen] = useState<boolean>(() => !hasRequestedCourseSlug);
  const [showMobileStickyBar, setShowMobileStickyBar] = useState(false);
  const [showLegacyGallery, setShowLegacyGallery] = useState(false);
  const [imageLightbox, setImageLightbox] = useState<{
    items: { src: string; caption: string }[];
    index: number;
  } | null>(null);

  // On "Học cùng Thầy Tony" (/courses), expand mobile course catalog by default so parents see all courses immediately;
  // collapse automatically when navigating into a specific course page.
  useEffect(() => {
    setMobileCateOpen(!hasRequestedCourseSlug);
  }, [hasRequestedCourseSlug]);

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
      if (cleanSlug.toLowerCase() === 'toeic') {
        const officeCourse = allCategories.find(
          (c: any) => Number(c.cc_id) === 123 || (c.cc_name_url || '').trim() === 'business-office-english'
        );
        if (officeCourse) {
          setCurrentCourse(officeCourse);
          const pid = Number(officeCourse.cc_parent) === 0 ? Number(officeCourse.cc_id) : Number(officeCourse.cc_parent);
          setOpenParentIds([pid]);
          const canonical = (officeCourse.cc_name_url || '').trim();
          if (canonical && canonical !== 'toeic') {
            navigate(`/courses/${encodeURIComponent(canonical)}`, { replace: true });
          }
          return;
        }
      }
      const found = allCategories.find((c: any) => (c.cc_name_url || '').trim() === cleanSlug);
      if (found) {
        setCurrentCourse(found);
        const pid = Number(found.cc_parent) === 0 ? Number(found.cc_id) : Number(found.cc_parent);
        setOpenParentIds([pid]);
      } else {
        setCurrentCourse(null);
        const allParentIds = allCategories
          .filter((c: any) => Number(c.cc_parent) === 0 && Number(c.cc_homedisplay) === 1)
          .map((c: any) => Number(c.cc_id));
        setOpenParentIds(allParentIds);
      }
    } else {
      setCurrentCourse(null);
      // On "Học cùng Thầy Tony", expand ALL parent groups so parents immediately see every course & sub-course
      const allParentIds = allCategories
        .filter((c: any) => Number(c.cc_parent) === 0 && Number(c.cc_homedisplay) === 1)
        .map((c: any) => Number(c.cc_id));
      setOpenParentIds(allParentIds);
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

  useEffect(() => {
    if (!imageLightbox) return;
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setImageLightbox(null);
      } else if (e.key === 'ArrowRight') {
        setImageLightbox((prev) =>
          prev ? { ...prev, index: (prev.index + 1) % prev.items.length } : null
        );
      } else if (e.key === 'ArrowLeft') {
        setImageLightbox((prev) =>
          prev ? { ...prev, index: (prev.index - 1 + prev.items.length) % prev.items.length } : null
        );
      }
    };
    window.addEventListener('keydown', onKeyDown);
    return () => {
      document.body.style.overflow = prevOverflow;
      window.removeEventListener('keydown', onKeyDown);
    };
  }, [imageLightbox]);

  const handleProseClick = (e: React.MouseEvent<HTMLDivElement>) => {
    const target = e.target as HTMLElement | null;
    const clickedImg = target?.closest('img') as HTMLImageElement | null;
    if (clickedImg) {
      e.preventDefault();
      const allImgs = Array.from(e.currentTarget.querySelectorAll('img')) as HTMLImageElement[];
      const items = allImgs
        .map((img) => {
          const src = img.getAttribute('src') || img.src || '';
          const fileName = src.split('/').pop()?.split('?')[0] || '';
          const caption =
            (lang === 'en' ? WEB_2026_CAPTIONS_EN[fileName] : WEB_2026_CAPTIONS[fileName]) ||
            (img.getAttribute('alt') || '').trim() ||
            (img.getAttribute('title') || '').trim() ||
            courseTitle;
          return { src, caption };
        })
        .filter((item) => Boolean(item.src));
      const clickedIndex = allImgs.indexOf(clickedImg);
      if (items.length > 0) {
        setImageLightbox({ items, index: clickedIndex >= 0 ? clickedIndex : 0 });
      }
      return;
    }

    const anchor = target?.closest('a');
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

  const lastTrackedCourseKeyRef = useRef<string>('');

  const resolveCourseOgImage = (course: any | null): string => {
    const cid = course ? Number(course.cc_id) : 0;
    const pid = course ? Number(course.cc_parent) : 0;
    if (cid === 127 || pid === 127) return '/images/courses/course-ielts.jpg';
    if (cid === 132 || pid === 132) return '/images/courses/course-igcse.jpg';
    if (cid === 133 || pid === 133) return '/images/courses/course-sat.jpg';
    if (cid === 111 || pid === 111) return '/images/courses/course-comm-basic.jpg';
    if (cid === 129 || pid === 129) return '/images/courses/course-comm-advanced.jpg';
    return '/images/courses/course-overview.jpg';
  };

  useEffect(() => {
    if (isResolvingSpecificCourse) return;
    const canonicalSlug = currentCourse ? (currentCourse.cc_name_url || '').trim() : '';
    const canonicalPath = canonicalSlug ? `/courses/${encodeURIComponent(canonicalSlug).replace(/%2F/gi, '/')}` : '/courses';
    updatePageSeo(courseTitle, courseDescHtml, {
      canonicalPath,
      image: resolveCourseOgImage(currentCourse),
    });

    if (categoriesLoaded) {
      const courseKey = currentCourse ? `course_${currentCourse.cc_id}` : 'course_overview';
      if (lastTrackedCourseKeyRef.current !== courseKey) {
        lastTrackedCourseKeyRef.current = courseKey;
        trackUnifiedViewCourse(courseTitle, currentCourse ? String(currentCourse.cc_id) : 'overview');
      }
    }
  }, [courseTitle, courseDescHtml, currentCourse, isResolvingSpecificCourse, categoriesLoaded]);

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

  // Academic Luxury 60-30-10 palette: cohesive Deep Ocean Navy base + disciplined 10% signature course accent
  const getCourseTheme = (course: any | null) => {
    const cid = course ? Number(course.cc_id) : 0;
    const pid = course ? Number(course.cc_parent) : 0;

    if (cid === 127 || pid === 127) {
      return {
        themeKey: 'ielts',
        heroBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]',
        topStripe: 'from-rose-600 via-rose-500 to-amber-400',
        orbPrimary: 'bg-rose-400/20',
        orbSecondary: 'bg-[#2ab4e8]/15',
        eyebrowText: 'text-rose-200',
        eyebrowBadge: 'bg-rose-500/20 border-rose-300/35 text-rose-100',
        pillBg: 'bg-white/10 border-white/20 text-white',
        rowTitle: 'text-slate-900 hover:text-rose-700',
        rowBadge: 'bg-rose-50 text-rose-800 border-rose-200/80',
        rowBtn: 'bg-[#0a5482] hover:bg-[#084266] text-white',
        rowHover: 'hover:bg-slate-50/80',
        rowActive: 'bg-rose-50/40 border-l-4 border-l-rose-600',
      };
    }

    if (cid === 132 || pid === 132) {
      return {
        themeKey: 'igcse',
        heroBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]',
        topStripe: 'from-emerald-600 via-emerald-500 to-teal-400',
        orbPrimary: 'bg-emerald-400/20',
        orbSecondary: 'bg-[#2ab4e8]/15',
        eyebrowText: 'text-emerald-200',
        eyebrowBadge: 'bg-emerald-500/20 border-emerald-300/35 text-emerald-100',
        pillBg: 'bg-white/10 border-white/20 text-white',
        rowTitle: 'text-slate-900 hover:text-emerald-700',
        rowBadge: 'bg-emerald-50 text-emerald-800 border-emerald-200/80',
        rowBtn: 'bg-[#0a5482] hover:bg-[#084266] text-white',
        rowHover: 'hover:bg-slate-50/80',
        rowActive: 'bg-emerald-50/40 border-l-4 border-l-emerald-600',
      };
    }

    if (cid === 133 || pid === 133) {
      return {
        themeKey: 'sat',
        heroBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]',
        topStripe: 'from-amber-500 via-amber-400 to-yellow-300',
        orbPrimary: 'bg-amber-400/20',
        orbSecondary: 'bg-[#2ab4e8]/15',
        eyebrowText: 'text-amber-200',
        eyebrowBadge: 'bg-amber-400/20 border-amber-300/35 text-amber-100',
        pillBg: 'bg-white/10 border-white/20 text-white',
        rowTitle: 'text-slate-900 hover:text-amber-700',
        rowBadge: 'bg-amber-50 text-amber-800 border-amber-200/80',
        rowBtn: 'bg-[#0a5482] hover:bg-[#084266] text-white',
        rowHover: 'hover:bg-slate-50/80',
        rowActive: 'bg-amber-50/40 border-l-4 border-l-amber-600',
      };
    }

    if (cid === 111 || pid === 111) {
      return {
        themeKey: 'comm-basic',
        heroBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]',
        topStripe: 'from-[#0284c7] via-[#2ab4e8] to-sky-300',
        orbPrimary: 'bg-[#2ab4e8]/20',
        orbSecondary: 'bg-sky-300/15',
        eyebrowText: 'text-sky-200',
        eyebrowBadge: 'bg-sky-400/20 border-sky-300/35 text-sky-100',
        pillBg: 'bg-white/10 border-white/20 text-white',
        rowTitle: 'text-slate-900 hover:text-[#0a5482]',
        rowBadge: 'bg-sky-50 text-[#0a5482] border-sky-200/80',
        rowBtn: 'bg-[#0a5482] hover:bg-[#084266] text-white',
        rowHover: 'hover:bg-slate-50/80',
        rowActive: 'bg-sky-50/45 border-l-4 border-l-[#0284c7]',
      };
    }

    if (cid === 129 || pid === 129) {
      return {
        themeKey: 'comm-advanced',
        heroBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]',
        topStripe: 'from-indigo-500 via-indigo-400 to-[#2ab4e8]',
        orbPrimary: 'bg-indigo-400/20',
        orbSecondary: 'bg-[#2ab4e8]/15',
        eyebrowText: 'text-indigo-200',
        eyebrowBadge: 'bg-indigo-400/20 border-indigo-300/35 text-indigo-100',
        pillBg: 'bg-white/10 border-white/20 text-white',
        rowTitle: 'text-slate-900 hover:text-indigo-700',
        rowBadge: 'bg-indigo-50 text-indigo-800 border-indigo-200/80',
        rowBtn: 'bg-[#0a5482] hover:bg-[#084266] text-white',
        rowHover: 'hover:bg-slate-50/80',
        rowActive: 'bg-indigo-50/40 border-l-4 border-l-indigo-600',
      };
    }

    return {
      themeKey: 'overview',
      heroBg: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]',
      topStripe: 'from-[#2ab4e8] via-amber-400 to-[#0a5482]',
      orbPrimary: 'bg-[#2ab4e8]/20',
      orbSecondary: 'bg-amber-300/15',
      eyebrowText: 'text-amber-200',
      eyebrowBadge: 'bg-amber-400/20 border-amber-300/35 text-amber-100',
      pillBg: 'bg-white/10 border-white/20 text-white',
      rowTitle: 'text-slate-900 hover:text-[#0a5482]',
      rowBadge: 'bg-sky-50 text-[#0a5482] border-sky-200/80',
      rowBtn: 'bg-[#0a5482] hover:bg-[#084266] text-white',
      rowHover: 'hover:bg-slate-50/80',
      rowActive: 'bg-sky-50/45 border-l-4 border-l-[#0a5482]',
    };
  };

  const activeVisual = getCourseVisualConfig(currentCourse);
  const activeTheme = getCourseTheme(currentCourse);
  const subCardAccents = [
    {
      badge: 'bg-sky-50 text-[#0a5482] border border-sky-200/80',
      card: 'hover:bg-sky-50/40 hover:border-[#0a5482]/40',
      title: 'group-hover:text-[#0a5482]',
      arrow: 'text-[#0284c7]',
    },
  ];

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
        {/* LEFT SIDEBAR: STRUCTURED & GROUPED COURSES MENU */}
        <aside className="w-full lg:w-[272px] xl:w-[288px] shrink-0 bg-white rounded-2xl border border-slate-200/80 shadow-sm overflow-hidden lg:sticky lg:top-24">
          <button
            type="button"
            onClick={() => setMobileCateOpen((prev) => !prev)}
            className="w-full bg-slate-100/80 px-4 py-3 border-b border-slate-200/70 flex items-center justify-between lg:pointer-events-none cursor-pointer text-left"
          >
            <h2 className="text-slate-600 lg:text-slate-500 font-bold text-xs uppercase tracking-widest flex items-center gap-2 min-w-0">
              <GraduationCap className="w-4 h-4 text-[#0a5482] shrink-0" />
              <span className="hidden lg:inline shrink-0">{t('Courses')}</span>
              <span className="lg:hidden font-bold text-[#0a5482] text-[13px] normal-case tracking-normal truncate">
                {mobileCateOpen
                  ? lang === 'vi'
                    ? 'Danh mục Khóa học'
                    : 'Course Catalog'
                  : isResolvingSpecificCourse
                  ? lang === 'vi'
                    ? 'Đang tải...'
                    : 'Loading...'
                  : courseTitle}
              </span>
            </h2>
            <span className="lg:hidden text-[11px] font-bold text-[#0a5482] bg-white px-2.5 py-1 rounded-lg border border-sky-200/90 shadow-2xs inline-flex items-center gap-1 shrink-0 ml-2">
              <span>
                {mobileCateOpen
                  ? lang === 'vi'
                    ? 'Thu gọn'
                    : 'Collapse'
                  : lang === 'vi'
                  ? 'Danh mục'
                  : 'Categories'}
              </span>
              {mobileCateOpen ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
            </span>
          </button>

          <div className={`${mobileCateOpen ? 'block' : 'hidden'} lg:block p-2.5 space-y-3 text-[14px]`}>
            {/* GROUP 1: OVERVIEW */}
            <div>
              <div className="px-2.5 pb-1.5 text-[10.5px] font-extrabold uppercase tracking-widest text-slate-400">
                {lang === 'vi' ? 'Tổng quan' : 'Overview'}
              </div>
              <Link
                to="/courses"
                onClick={() => {
                  setMobileCateOpen(false);
                  scrollToCourseTop();
                }}
                className={`flex items-center gap-2.5 px-2.5 py-2.5 rounded-xl transition-all relative ${
                  !currentCourse
                    ? "bg-sky-50/95 text-[#0a5482] font-bold pl-3.5 before:content-[''] before:absolute before:left-1 before:top-2 before:bottom-2 before:w-1 before:rounded-full before:bg-[#2ab4e8]"
                    : 'text-slate-600 font-semibold hover:bg-slate-50 hover:text-[#0a5482]'
                }`}
              >
                <span
                  className={`w-7 h-7 rounded-lg flex items-center justify-center shrink-0 transition-colors ${
                    !currentCourse ? 'bg-[#0a5482] text-white shadow-xs' : 'bg-sky-50 text-[#0a5482]'
                  }`}
                >
                  <Sparkles className="w-3.5 h-3.5" />
                </span>
                <span className="leading-snug">{t('Study at TonyEnglish')}</span>
              </Link>
            </div>

            {homeParents.length === 0 ? (
              <div className="pt-2 border-t border-slate-100 px-1 space-y-2 animate-pulse">
                {[1, 2, 3, 4].map((n) => (
                  <div key={n} className="h-9 rounded-xl bg-slate-100" />
                ))}
              </div>
            ) : (
              (() => {
                const isCommParent = (p: any) => {
                  const key = `${p.cc_name_url || ''} ${p.cc_name || ''} ${p.cc_name_vi || ''}`.toLowerCase();
                  return Number(p.cc_id) === 111 || Number(p.cc_id) === 129 || key.includes('communication') || key.includes('giao tiếp') || key.includes('giao tiep');
                };

                const commParents = homeParents.filter(isCommParent);
                const examParents = homeParents.filter((p) => !isCommParent(p));

                const getParentIcon = (p: any) => {
                  const key = `${p.cc_name_url || ''} ${p.cc_name || ''} ${p.cc_name_vi || ''}`.toLowerCase();
                  if (key.includes('advanced') || key.includes('nâng cao') || key.includes('nang cao')) {
                    return { Icon: Briefcase, idleBg: 'bg-indigo-50 text-indigo-600' };
                  }
                  if (key.includes('communication') || key.includes('giao tiếp') || key.includes('giao tiep')) {
                    return { Icon: Mic, idleBg: 'bg-sky-50 text-[#0a5482]' };
                  }
                  if (key.includes('ielts')) {
                    return { Icon: Award, idleBg: 'bg-rose-50 text-rose-600' };
                  }
                  if (key.includes('igcse') || key.includes('alevel') || key.includes('a-level')) {
                    return { Icon: Globe, idleBg: 'bg-emerald-50 text-emerald-700' };
                  }
                  if (key.includes('sat')) {
                    return { Icon: Target, idleBg: 'bg-amber-50 text-amber-700' };
                  }
                  return { Icon: BookOpen, idleBg: 'bg-slate-100 text-slate-600' };
                };

                const renderParentItem = (parent: any) => {
                  const subs = subCategories(parent.cc_id);
                  const isOpen =
                    openParentIds.includes(Number(parent.cc_id)) ||
                    (currentCourse &&
                      (currentCourse.cc_id === parent.cc_id || currentCourse.cc_parent === parent.cc_id));
                  const parentName = normalizeCourseDisplayName(
                    lang === 'vi' ? parent.cc_name_vi || parent.cc_name : parent.cc_name
                  );
                  const isCurrentParent = currentCourse && currentCourse.cc_id === parent.cc_id;
                  const hasActiveChild = currentCourse && currentCourse.cc_parent === parent.cc_id;
                  const { Icon, idleBg } = getParentIcon(parent);

                  return (
                    <li key={parent.cc_id}>
                      <Link
                        to={`/courses/${(parent.cc_name_url || '').trim()}`}
                        onClick={() => {
                          setOpenParentIds([Number(parent.cc_id)]);
                          if (subs.length === 0 || isOpen) setMobileCateOpen(false);
                          scrollToCourseTop();
                        }}
                        className={`px-2.5 py-2.5 rounded-xl transition-all flex items-center justify-between gap-2 relative ${
                          isCurrentParent
                            ? "bg-sky-50/95 text-[#0a5482] font-bold pl-3.5 before:content-[''] before:absolute before:left-1 before:top-2 before:bottom-2 before:w-1 before:rounded-full before:bg-[#2ab4e8]"
                            : hasActiveChild || isOpen
                            ? 'text-[#0a5482] font-semibold bg-slate-50/80'
                            : 'text-slate-700 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                        }`}
                      >
                        <span className="flex items-center gap-2.5 min-w-0">
                          <span
                            className={`w-7 h-7 rounded-lg flex items-center justify-center shrink-0 transition-colors ${
                              isCurrentParent ? 'bg-[#0a5482] text-white shadow-xs' : idleBg
                            }`}
                          >
                            <Icon className="w-3.5 h-3.5" />
                          </span>
                          <span className="leading-snug">{parentName}</span>
                        </span>
                        {subs.length > 0 && (
                          <span className="flex items-center gap-1 shrink-0">
                            <span
                              className={`text-[10.5px] font-extrabold px-1.5 py-0.5 rounded-md tabular-nums ${
                                isOpen || isCurrentParent
                                  ? 'bg-sky-100 text-[#0a5482]'
                                  : 'bg-slate-100 text-slate-500'
                              }`}
                            >
                              {subs.length}
                            </span>
                            <ChevronRight
                              className={`w-3.5 h-3.5 transition-transform duration-200 ${
                                isOpen ? 'rotate-90 text-[#0a5482]' : 'text-slate-400'
                              }`}
                            />
                          </span>
                        )}
                      </Link>

                      {subs.length > 0 && isOpen && (
                        <ul className="mt-1 mb-1.5 ml-5 pl-2.5 border-l-2 border-sky-100 space-y-1">
                          {subs.map((sub, subIdx) => {
                            const subName = lang === 'vi' ? sub.cc_name_vi || sub.cc_name : sub.cc_name;
                            const isActiveSub = currentCourse && currentCourse.cc_id === sub.cc_id;
                            const stepLabel = String(subIdx + 1).padStart(2, '0');
                            return (
                              <li key={sub.cc_id}>
                                <Link
                                  to={`/courses/${(sub.cc_name_url || '').trim()}`}
                                  onClick={() => {
                                    setMobileCateOpen(false);
                                    scrollToCourseTop();
                                  }}
                                  className={`flex items-center gap-2 px-2.5 py-2 rounded-lg text-[13px] transition-all ${
                                    isActiveSub
                                      ? 'bg-sky-50 text-[#0a5482] font-bold'
                                      : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                                  }`}
                                >
                                  <span
                                    className={`text-[10px] font-black px-1.5 py-0.5 rounded-md tabular-nums shrink-0 ${
                                      isActiveSub
                                        ? 'bg-[#0a5482] text-white'
                                        : 'bg-slate-100 text-slate-500'
                                    }`}
                                  >
                                    {stepLabel}
                                  </span>
                                  <span className="leading-snug">{subName}</span>
                                </Link>
                              </li>
                            );
                          })}
                        </ul>
                      )}
                    </li>
                  );
                };

                return (
                  <>
                    {commParents.length > 0 && (
                      <div className="pt-2.5 border-t border-slate-100">
                        <div className="px-2.5 pb-1.5 text-[10.5px] font-extrabold uppercase tracking-widest text-slate-400">
                          {lang === 'vi' ? 'Tiếng Anh Giao tiếp' : 'English Communication'}
                        </div>
                        <ul className="space-y-1">{commParents.map(renderParentItem)}</ul>
                      </div>
                    )}

                    {examParents.length > 0 && (
                      <div className="pt-2.5 border-t border-slate-100">
                        <div className="px-2.5 pb-1.5 text-[10.5px] font-extrabold uppercase tracking-widest text-slate-400">
                          {lang === 'vi' ? 'Luyện thi Quốc tế' : 'International Exams'}
                        </div>
                        <ul className="space-y-1">{examParents.map(renderParentItem)}</ul>
                      </div>
                    )}
                  </>
                );
              })()
            )}

            {/* Mobile-only bottom collapse button for easy dismissal after browsing all courses */}
            <div className="lg:hidden pt-2 border-t border-slate-100">
              <button
                type="button"
                onClick={() => setMobileCateOpen(false)}
                className="w-full py-2 px-3 rounded-xl bg-slate-50 hover:bg-slate-100 active:scale-[0.99] text-[12.5px] font-bold text-slate-600 inline-flex items-center justify-center gap-1.5 transition-all cursor-pointer"
              >
                <ChevronUp className="w-4 h-4 text-[#0a5482]" />
                <span>{lang === 'vi' ? 'Thu gọn danh mục' : 'Collapse catalog'}</span>
              </button>
            </div>
          </div>
        </aside>

        {/* RIGHT MAIN CONTENT */}
        <div className="flex-1 min-w-0 w-full space-y-6">
          <div className="bg-white rounded-2xl sm:rounded-3xl border border-slate-200/90 shadow-sm overflow-hidden">
            {/* Refined Single-Accent Top Bar */}
            <div className={`h-1 w-full bg-gradient-to-r ${activeTheme.topStripe}`} />

            {/* Section Header (Academic Deep Ocean Navy + Subtle Course Accent) */}
            <div className={`relative overflow-hidden bg-gradient-to-br ${activeTheme.heroBg} px-4 sm:px-8 py-5 sm:py-7 text-white`}>
              {/* Soft decorative color orbs */}
              <div className={`pointer-events-none absolute -top-12 -right-10 w-52 h-52 rounded-full blur-3xl ${activeTheme.orbPrimary}`} />
              <div className={`pointer-events-none absolute -bottom-14 left-1/3 w-44 h-44 rounded-full blur-3xl ${activeTheme.orbSecondary}`} />

              <div className="relative z-10 space-y-2.5">
                <div className={`inline-flex items-center gap-1.5 text-[10.5px] sm:text-xs font-extrabold uppercase tracking-widest px-3 py-1 rounded-full border ${activeTheme.eyebrowBadge}`}>
                  <Sparkles className="w-3.5 h-3.5 shrink-0" />
                  <span>
                    {lang === 'vi' ? 'Lớp Gia Sư 1 Kèm 1 Cùng Thầy Tony' : '1-on-1 Private Tutoring with Mr. Tony'}
                  </span>
                </div>
                {isResolvingSpecificCourse ? (
                  <div className="h-8 sm:h-9 w-64 sm:w-80 bg-white/15 rounded-xl animate-pulse mt-1" />
                ) : (
                  <>
                    <h1 className="text-xl sm:text-3xl font-black tracking-tight text-white">
                      {courseTitle}
                    </h1>
                    {activeVisual.highlights && activeVisual.highlights.length > 0 && (
                      <div className="flex flex-wrap items-center gap-2 pt-1">
                        {activeVisual.highlights.map((hl, idx) => (
                          <span
                            key={idx}
                            className={`inline-flex items-center text-[11px] sm:text-xs font-bold px-3 py-1 rounded-xl border backdrop-blur-xs leading-snug ${activeTheme.pillBg}`}
                          >
                            {hl}
                          </span>
                        ))}
                      </div>
                    )}
                  </>
                )}
              </div>
            </div>

            {isResolvingSpecificCourse ? (
              <div className="p-4 sm:p-8 space-y-5 animate-pulse">
                <div className="h-28 rounded-2xl bg-slate-100 border border-slate-200" />
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

              {/* Quick Above-the-Fold Consultation Box (Academic Luxury — 2 Disciplined Hues: Navy & Gold) */}
              <div
                id="khung-dang-ky-tu-van"
                className="relative overflow-hidden rounded-2xl bg-slate-50/90 border border-slate-200/90 border-l-4 border-l-amber-400 p-4 sm:p-5 space-y-3 shadow-2xs"
              >
                <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
                  <div className="space-y-1.5">
                    <div className="flex flex-wrap items-center gap-2">
                      <div className="inline-flex items-center gap-1.5 text-[11px] sm:text-xs font-bold text-[#0a5482] bg-white border border-slate-200/90 px-2.5 py-1 rounded-xl leading-snug">
                        <MapPin className="w-3.5 h-3.5 text-[#0284c7] shrink-0" />
                        <span>
                          {lang === 'vi'
                            ? 'R2B 2219 Royal City (Nhà riêng Thầy Tony) & Online'
                            : 'Mr. Tony’s Residence (R2B 2219 Royal City) & Online'}
                        </span>
                      </div>
                      <span className="inline-flex items-center gap-1 text-[10.5px] sm:text-[11px] font-extrabold uppercase tracking-wide bg-amber-100 text-amber-900 border border-amber-200/90 px-2.5 py-1 rounded-xl">
                        <Gift className="w-3.5 h-3.5 text-amber-700 shrink-0" />
                        <span>{lang === 'vi' ? 'Miễn phí 2–3 buổi' : '2–3 Free Trials'}</span>
                      </span>
                    </div>
                    <div className="text-sm sm:text-base font-black text-slate-900 leading-snug">
                      {lang === 'vi' ? (
                        <>
                          Kiểm tra đầu vào &amp;{' '}
                          <span className="text-[#0a5482]">Học thử miễn phí 2–3 buổi</span> — Con thấy thật sự hợp thầy, hợp phương pháp mới đăng ký!
                        </>
                      ) : (
                        <>
                          Free Placement Test &amp;{' '}
                          <span className="text-[#0a5482]">2–3 Free Trial Lessons</span> — Only enroll if it truly fits your child!
                        </>
                      )}
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
                      className="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 bg-[#0a5482] hover:bg-[#084266] text-white font-extrabold text-xs sm:text-sm px-4 py-2.5 rounded-xl shadow-xs transition whitespace-nowrap"
                    >
                      <Phone className="w-4 h-4 shrink-0" />
                      <span>{lang === 'vi' ? `Gọi: ${CONTACT_PHONE_DISPLAY}` : `Call: ${CONTACT_PHONE_DISPLAY}`}</span>
                    </a>

                    <a
                      href={CONTACT_ZALO_URL}
                      target="_blank"
                      rel="noreferrer"
                      onClick={(e) => handleZaloClick(e, courseTitle)}
                      className="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 bg-white hover:bg-sky-50 text-[#0a5482] border border-slate-300 hover:border-[#0068ff] font-extrabold text-xs sm:text-sm px-4 py-2.5 rounded-xl shadow-2xs transition whitespace-nowrap"
                    >
                      <MessageCircle className="w-4 h-4 text-[#0068ff] shrink-0" />
                      <span>{lang === 'vi' ? `Zalo: ${CONTACT_PHONE_DISPLAY}` : `Zalo: ${CONTACT_PHONE_DISPLAY}`}</span>
                    </a>
                  </div>
                </div>

                {/* Fallback helper when Facebook/Instagram In-App Browser blocks jumping directly to Zalo app */}
                {zaloFallbackHint && (
                  <div className="rounded-xl bg-amber-50 border border-amber-200 px-3.5 py-2.5 flex flex-wrap items-center justify-between gap-2 text-xs text-amber-950 font-semibold">
                    <span>
                      {lang === 'vi' ? (
                        <>✅ Đã copy số Zalo <strong>0935 058 688</strong> — Nếu trình duyệt Facebook chặn chuyển app, anh/chị mở <strong>Zalo</strong> rồi dán số vào ô Tìm kiếm nhé:</>
                      ) : (
                        <>✅ Copied Zalo number <strong>0935 058 688</strong> — If an in-app browser blocks opening Zalo, simply open <strong>Zalo</strong> and paste this number into Search:</>
                      )}
                    </span>
                    <button
                      type="button"
                      onClick={handleCopyPhone}
                      className="px-3 py-1.5 rounded-lg bg-white border border-amber-300 text-amber-900 font-extrabold hover:bg-amber-100 transition cursor-pointer shrink-0"
                    >
                      {copiedPhone
                        ? lang === 'vi' ? '✅ Đã copy 0935058688' : '✅ Copied 0935058688'
                        : lang === 'vi' ? '📋 Copy SĐT: 0935 058 688' : '📋 Copy Phone: 0935 058 688'}
                    </button>
                  </div>
                )}
              </div>

              {/* Featured Walkthrough Video (Study with Mr. Tony + 5 Flagship Courses — Above-the-Fold for Ads) */}
              <CourseGuideVideoCard courseId={currentCourse ? Number(currentCourse.cc_id) : 0} lang={lang} />

              {/* Course Description HTML */}
              {courseDescHtml && (
                <div className="pt-2 sm:pt-3">
                  <div
                    data-course-theme={activeTheme.themeKey}
                    className="legacy-prose course-tab-prose text-left sm:text-justify max-w-[74ch] [&_img]:cursor-zoom-in [&_img]:rounded-xl [&_img]:border [&_img]:border-slate-200/90 [&_img]:shadow-2xs [&_img]:transition-all [&_img:hover]:ring-2 [&_img:hover]:ring-[#2ab4e8]/70 [&_img:hover]:shadow-lg"
                    onClick={handleProseClick}
                    dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(courseDescHtml) }}
                  />
                </div>
              )}

              {/* Curated Live LMS Screenshots: Theory Lectures & Practice Test Bank */}
              {currentCourse && (
                <CourseShowcaseGallery courseId={Number(currentCourse.cc_id)} lang={lang} />
              )}

              {/* Subcategory Quick Cards if parent category has children (placed below screenshots showcase) */}
              {childCoursesOfCurrent.length > 0 && (
                <div className="bg-slate-50/90 rounded-2xl p-5 border border-slate-200/90">
                  <h3 className="text-xs sm:text-sm font-black uppercase tracking-wider text-[#0a5482] mb-3 flex items-center gap-2">
                    <span className="w-1.5 h-4 rounded-full bg-[#0a5482]" />
                    <span>{lang === 'vi' ? 'Các cấp độ / chuyên đề trong khóa học này:' : 'Courses in this category:'}</span>
                  </h3>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    {childCoursesOfCurrent.map((sub, subIdx) => {
                      const accent = subCardAccents[subIdx % subCardAccents.length];
                      return (
                        <Link
                          key={sub.cc_id}
                          to={`/courses/${(sub.cc_name_url || '').trim()}`}
                          onClick={scrollToCourseTop}
                          className={`bg-white border border-slate-200 rounded-xl px-4 py-3.5 flex items-center justify-between gap-3 group transition shadow-2xs ${accent.card}`}
                        >
                          <div className="flex items-center gap-2.5 min-w-0">
                            <span className={`w-6 h-6 rounded-lg text-[11px] font-black flex items-center justify-center shrink-0 shadow-2xs ${accent.badge}`}>
                              {String(subIdx + 1).padStart(2, '0')}
                            </span>
                            <div className={`font-extrabold text-[15px] sm:text-base text-slate-800 transition-colors ${accent.title}`}>
                              {lang === 'vi' ? sub.cc_name_vi || sub.cc_name : sub.cc_name}
                            </div>
                          </div>
                          <span className={`font-black group-hover:translate-x-1 transition-transform shrink-0 ${accent.arrow}`}>
                            →
                          </span>
                        </Link>
                      );
                    })}
                  </div>
                </div>
              )}

              {courseDescHtml && (
                <div className="rounded-2xl bg-slate-50/90 border border-slate-200/90 border-l-4 border-l-[#0a5482] px-4 sm:px-5 py-4 flex flex-wrap items-center justify-between gap-3 shadow-2xs">
                  <div className="space-y-1">
                    <div className="text-sm sm:text-base font-extrabold text-slate-900 flex flex-wrap items-center gap-2">
                      <CreditCard className="w-4 h-4 text-[#0a5482] shrink-0" />
                      <span>{lang === 'vi' ? 'Học phí:' : 'Tuition fee:'}</span>
                      <span className="inline-flex items-center px-2.5 py-0.5 rounded-full bg-sky-50 text-[#0a5482] border border-sky-200 text-xs sm:text-sm font-black">
                        {lang === 'vi' ? 'Liên hệ tư vấn' : 'Contact Mr. Tony'}
                      </span>
                    </div>
                    <div className="text-xs sm:text-[13px] font-semibold text-slate-600 flex items-center gap-1.5">
                      <Sparkles className="w-3.5 h-3.5 text-amber-500 shrink-0" />
                      <span>
                        {lang === 'vi'
                          ? 'Học thử miễn phí 2–3 buổi tại R2B Royal City — Thấy thật sự hợp thầy mới đăng ký'
                          : '2–3 Free Trial Lessons at R2B Royal City before enrollment'}
                      </span>
                    </div>
                  </div>
                  <a
                    href={`tel:${CONTACT_PHONE}`}
                    onClick={() => trackCourseConversion('Phone', courseTitle)}
                    className="inline-flex items-center gap-1.5 text-xs sm:text-sm font-extrabold text-[#0a5482] bg-white hover:bg-sky-50 border border-slate-300 hover:border-[#0a5482] px-3.5 py-2 rounded-xl shadow-2xs transition"
                  >
                    <Phone className="w-3.5 h-3.5 text-[#0284c7]" />
                    <span>{lang === 'vi' ? 'Hotline / Zalo:' : 'Hotline / Zalo:'}</span>
                    <strong className="text-slate-900">{CONTACT_PHONE_DISPLAY}</strong>
                  </a>
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
                          {lang === 'vi'
                            ? 'Góc Kỷ Niệm: Giao diện TonyEnglish phiên bản đầu tiên (2013 – 2017)'
                            : 'Keepsake Archive: First-Generation TonyEnglish Web Interface (2013 – 2017)'}
                        </div>
                        <div className="text-[11.5px] text-amber-800/85 font-medium leading-relaxed mt-0.5">
                          {lang === 'vi'
                            ? 'Lưu trữ 10 hình ảnh chụp màn hình kỷ niệm của trang web TonyEnglish thế hệ cũ'
                            : 'Archive of 10 original screenshots from the classic TonyEnglish.vn platform'}
                        </div>
                      </div>
                    </div>
                    <span className="self-start sm:self-center inline-flex items-center gap-1 px-3 py-1.5 rounded-lg bg-white border border-amber-200 text-amber-900 font-bold text-xs shrink-0 shadow-2xs">
                      <span>
                        {showLegacyGallery
                          ? lang === 'vi' ? 'Thu gọn' : 'Collapse'
                          : lang === 'vi' ? 'Xem ảnh kỷ niệm' : 'View archive photos'}
                      </span>
                      {showLegacyGallery ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
                    </span>
                  </button>

                  {showLegacyGallery && (
                    <div className="p-4 sm:p-6 border-t border-amber-200/70 bg-white space-y-5">
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {LEGACY_GALLERY_ITEMS.map((item, idx) => {
                          const itemCap = lang === 'vi' ? item.caption : item.captionEn;
                          return (
                            <button
                              key={item.src}
                              type="button"
                              onClick={() =>
                                setImageLightbox({
                                  items: LEGACY_GALLERY_ITEMS.map((it) => ({
                                    src: it.src,
                                    caption: lang === 'vi' ? it.caption : it.captionEn,
                                  })),
                                  index: idx,
                                })
                              }
                              className="group text-left rounded-xl border border-slate-200 hover:border-[#2ab4e8] overflow-hidden bg-slate-50 shadow-2xs hover:shadow-md transition cursor-zoom-in"
                            >
                              <div className="relative overflow-hidden">
                                <img
                                  src={item.src}
                                  alt={itemCap}
                                  className="w-full h-auto object-cover group-hover:scale-[1.02] transition-transform duration-300"
                                  loading="lazy"
                                />
                                <span className="absolute bottom-2 right-2 inline-flex items-center gap-1 px-2 py-1 rounded-lg bg-slate-900/80 text-white text-[11px] font-bold opacity-90 sm:opacity-0 sm:group-hover:opacity-100 transition-opacity shadow-sm">
                                  <ZoomIn className="w-3.5 h-3.5" />
                                  <span>{lang === 'vi' ? 'Phóng to' : 'Zoom'}</span>
                                </span>
                              </div>
                              <div className="px-3 py-2 text-center text-xs font-semibold text-slate-600 group-hover:text-[#0a5482] border-t border-slate-200/80">
                                {itemCap}
                              </div>
                            </button>
                          );
                        })}
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
                  className="bg-[#0a5482] hover:bg-[#084266] text-white font-extrabold text-sm px-5 py-3 rounded-xl shadow-sm transition inline-flex items-center gap-2"
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
                  className="bg-white hover:bg-sky-50 text-[#0a5482] border border-slate-300 hover:border-[#0068ff] font-extrabold text-sm px-5 py-3 rounded-xl shadow-2xs transition inline-flex items-center gap-2"
                >
                  <MessageCircle className="w-4 h-4 text-[#0068ff] shrink-0" />
                  <span>
                    {lang === 'vi'
                      ? `Tư vấn qua Zalo: ${CONTACT_PHONE_DISPLAY}`
                      : `Consult via Zalo: ${CONTACT_PHONE_DISPLAY}`}
                  </span>
                </a>
              </div>

              {/* BẢNG DANH MỤC CÁC KHÓA HỌC TẠI TONYENGLISH */}
              {homeParents.length > 0 && (
                <div className="pt-6 border-t border-slate-200">
                  <div className="bg-slate-50 rounded-2xl border border-slate-200/90 overflow-hidden shadow-xs">
                    <div className="h-[3px] w-full bg-gradient-to-r from-[#2ab4e8] via-amber-400 to-[#0a5482]" />
                    <div className="bg-gradient-to-br from-[#073b5c] via-[#0a5482] to-[#0f172a] px-5 py-4 text-white flex items-center gap-3">
                      <span className="w-9 h-9 rounded-xl bg-white/10 border border-white/20 text-amber-300 flex items-center justify-center shrink-0">
                        <BookOpen className="w-4 h-4" />
                      </span>
                      <div>
                        <h2 className="text-base sm:text-lg font-black tracking-tight">
                          {lang === 'vi'
                            ? 'Danh Mục Các Gói Gia Sư 1 Kèm 1 Cùng Thầy Tony'
                            : '1-on-1 Private Tutoring Packages with Mr. Tony'}
                        </h2>
                        <p className="text-xs text-sky-200/90 font-medium">
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
                        const rowTheme = getCourseTheme(parent);

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
                            className={`p-4 sm:p-5 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4 transition group ${
                              isActiveRow ? rowTheme.rowActive : rowTheme.rowHover
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
                                    className={`font-black text-base sm:text-lg transition leading-snug ${rowTheme.rowTitle}`}
                                  >
                                    {parentName}
                                  </Link>
                                  {isActiveRow && (
                                    <span className={`text-[10px] font-black uppercase px-2 py-0.5 rounded-full border ${rowTheme.rowBadge}`}>
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
                                    <strong className="text-rose-600">
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
                                        className={`inline-flex items-center gap-1 text-xs font-bold border px-2.5 py-1 rounded-lg transition ${rowTheme.rowBadge} hover:opacity-85`}
                                      >
                                        <span>• {lang === 'vi' ? sub.cc_name_vi || sub.cc_name : sub.cc_name}</span>
                                        <span>→</span>
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
                                className={`w-full sm:w-auto inline-flex items-center justify-center gap-1.5 font-bold text-xs sm:text-sm px-4 py-2.5 rounded-xl shadow-2xs transition whitespace-nowrap ${rowTheme.rowBtn}`}
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
          className="inline-flex items-center justify-center gap-1.5 bg-[#0a5482] active:bg-[#084266] text-white font-extrabold text-xs py-2.5 px-3 rounded-xl shadow-xs whitespace-nowrap"
        >
          <Phone className="w-3.5 h-3.5 shrink-0" />
          <span>{lang === 'vi' ? `Gọi: ${CONTACT_PHONE_DISPLAY}` : `Call: ${CONTACT_PHONE_DISPLAY}`}</span>
        </a>
        <a
          href={CONTACT_ZALO_URL}
          target="_blank"
          rel="noreferrer"
          onClick={(e) => handleZaloClick(e, courseTitle)}
          className="inline-flex items-center justify-center gap-1.5 bg-white active:bg-sky-50 text-[#0a5482] border border-slate-300 font-extrabold text-xs py-2.5 px-3 rounded-xl shadow-2xs whitespace-nowrap"
        >
          <MessageCircle className="w-3.5 h-3.5 text-[#0068ff] shrink-0" />
          <span>Zalo: {CONTACT_PHONE_DISPLAY}</span>
        </a>
      </div>

      {/* IMAGE LIGHTBOX MODAL FOR COURSE OVERVIEW (2026 & 2013-2017 SCREENSHOTS) */}
      {imageLightbox && imageLightbox.items[imageLightbox.index] && (
        <div
          className="fixed inset-0 z-[70] bg-slate-950/90 backdrop-blur-sm flex items-center justify-center p-3 sm:p-6"
          onClick={() => setImageLightbox(null)}
        >
          <div
            role="dialog"
            aria-modal="true"
            className="relative max-w-6xl w-full flex flex-col items-center gap-3"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="w-full flex items-center justify-between gap-3 text-white px-1">
              <div className="flex items-center gap-2 min-w-0">
                <span className="px-2.5 py-1 rounded-lg bg-white/15 border border-white/20 text-xs font-extrabold shrink-0">
                  {imageLightbox.index + 1} / {imageLightbox.items.length}
                </span>
                <span className="font-bold text-sm sm:text-base truncate">
                  {imageLightbox.items[imageLightbox.index].caption}
                </span>
              </div>
              <button
                type="button"
                onClick={() => setImageLightbox(null)}
                className="w-9 h-9 rounded-full bg-white/15 hover:bg-white/25 text-white flex items-center justify-center transition cursor-pointer shrink-0"
                aria-label={lang === 'vi' ? 'Đóng' : 'Close'}
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="relative w-full flex items-center justify-center">
              {imageLightbox.items.length > 1 && (
                <button
                  type="button"
                  onClick={() =>
                    setImageLightbox((prev) =>
                      prev
                        ? { ...prev, index: (prev.index - 1 + prev.items.length) % prev.items.length }
                        : null
                    )
                  }
                  className="absolute left-2 sm:left-3 z-10 w-10 h-10 sm:w-11 sm:h-11 rounded-full bg-slate-900/75 hover:bg-slate-900 text-white border border-white/20 flex items-center justify-center shadow-lg transition cursor-pointer"
                  aria-label="Previous image"
                >
                  <ChevronLeft className="w-6 h-6" />
                </button>
              )}

              <img
                src={imageLightbox.items[imageLightbox.index].src}
                alt={imageLightbox.items[imageLightbox.index].caption}
                className="max-h-[78vh] w-auto max-w-full rounded-xl sm:rounded-2xl border border-white/15 shadow-2xl object-contain bg-white"
              />

              {imageLightbox.items.length > 1 && (
                <button
                  type="button"
                  onClick={() =>
                    setImageLightbox((prev) =>
                      prev ? { ...prev, index: (prev.index + 1) % prev.items.length } : null
                    )
                  }
                  className="absolute right-2 sm:right-3 z-10 w-10 h-10 sm:w-11 sm:h-11 rounded-full bg-slate-900/75 hover:bg-slate-900 text-white border border-white/20 flex items-center justify-center shadow-lg transition cursor-pointer"
                  aria-label="Next image"
                >
                  <ChevronRight className="w-6 h-6" />
                </button>
              )}
            </div>
          </div>
        </div>
      )}

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
                    {lang === 'vi'
                      ? 'R2B 2219 Royal City • Học thử 2–3 buổi miễn phí'
                      : 'R2B 2219 Royal City • 2–3 Free Trial Sessions'}
                  </p>
                </div>
              </div>
              <button
                type="button"
                onClick={() => setShowZaloModal(false)}
                className="w-8 h-8 rounded-full bg-white/15 hover:bg-white/25 text-white font-black text-sm flex items-center justify-center cursor-pointer transition shrink-0"
                aria-label={lang === 'vi' ? 'Đóng' : 'Close'}
              >
                ✕
              </button>
            </div>

            <div className="p-5 space-y-4">
              <div className="rounded-2xl bg-emerald-50 border border-emerald-200 p-3.5 flex items-center justify-between gap-2">
                <div>
                  <div className="text-[11px] font-extrabold uppercase tracking-wide text-emerald-700">
                    {copiedPhone
                      ? lang === 'vi' ? '✅ Đã tự động sao chép số Zalo' : '✅ Zalo Number Automatically Copied'
                      : lang === 'vi' ? 'Số điện thoại / Zalo Thầy Tony' : "Mr. Tony's Phone / Zalo"}
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
                  {copiedPhone
                    ? lang === 'vi' ? '✅ Đã copy' : '✅ Copied'
                    : lang === 'vi' ? '📋 Copy số' : '📋 Copy number'}
                </button>
              </div>

              <div className="rounded-xl bg-amber-50/90 border border-amber-200/90 px-3.5 py-2.5 text-xs sm:text-[13px] text-amber-950 leading-relaxed font-medium">
                {lang === 'vi' ? (
                  <>💡 <strong>Mẹo mở nhanh từ Facebook:</strong> Hệ thống đã copy sẵn số <strong>0935058688</strong>. Nếu bấm nút bên dưới bị trình duyệt Facebook chặn, anh/chị chỉ cần mở app <strong>Zalo</strong> trên điện thoại → bấm ô <strong>Tìm kiếm</strong> → <strong>Dán (0935058688)</strong> là nhắn tin cho thầy được ngay ạ!</>
                ) : (
                  <>💡 <strong>Quick Tip from Mobile Apps:</strong> We already copied <strong>0935058688</strong>. If an in-app browser blocks opening Zalo directly, simply open <strong>Zalo</strong> → tap <strong>Search</strong> → <strong>Paste (0935058688)</strong> to message Mr. Tony right away!</>
                )}
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
