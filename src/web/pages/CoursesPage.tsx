import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import { encryptLegacyPass, fixLegacyHtmlContent, updatePageSeo } from '../lib/utils';

interface SyllabusPackageItem {
  id: string;
  category: 'comm' | 'office' | 'ielts' | 'igcse' | 'sat';
  courseSlug: string;
  badge: string;
  title: string;
  subtitle: string;
  icon: string;
  gradient: string;
  accentColor: string;
  stats: string[];
  highlights: string[];
  lmsCourseTitles: string[];
  moduleFilter?: (moduleTitle: string) => boolean;
}

const CONTACT_PHONE = '0935058688';
const CONTACT_PHONE_DISPLAY = '0935 058 688';
const CONTACT_ZALO_URL = 'https://zalo.me/0935058688';

const COURSE_SYLLABUS_PACKAGES: SyllabusPackageItem[] = [
  {
    id: 'ielts-premium',
    category: 'ielts',
    courseSlug: 'ielts',
    badge: 'LUYỆN THI IELTS 1 KÈM 1 & LMS',
    title: 'IELTS Premium Toàn Diện (4 Kỹ Năng)',
    subtitle:
      'Lộ trình bài bản từ nền tảng đến Band 7.0+ tích hợp phòng thi máy tính chuẩn IDP/BC & AI chấm chữa 24/7',
    icon: '🏆',
    gradient: 'from-sky-600 via-[#0a5482] to-indigo-900',
    accentColor: 'text-sky-600 bg-sky-50 border-sky-200',
    stats: ['9 Học phần chuyên sâu', '70+ Bài giảng tương tác', '367+ Đề luyện thi thực chiến'],
    highlights: [
      'Giao diện thi thử trên máy tính giống 100% phòng thi thật (Highlight, Note, Audio chuẩn)',
      'AI Giám khảo chấm chữa chi tiết IELTS Writing Task 1, Task 2 & Luyện phản xạ Speaking 1-1',
      'Video bài giảng & hệ thống bài tập thực hành gắn liền ngay trong từng bài học',
      'Kết hợp kèm cặp 1 kèm 1 cá nhân hóa theo đúng mục tiêu Band điểm và thời gian thi của học viên',
    ],
    lmsCourseTitles: ['IELTS Premium'],
  },
  {
    id: 'reflex-communication',
    category: 'comm',
    courseSlug: 'english-communication 1',
    badge: 'GIAO TIẾP & PHẢN XẠ 1 KÈM 1',
    title: 'Giao Tiếp & Phản Xạ Thực Chiến Cùng AI',
    subtitle:
      'Xóa bỏ nỗi sợ nói tiếng Anh với 160+ bài giảng Phát âm IPA, tình huống giao tiếp, Podcast hội thoại & phòng luyện nói 1-1',
    icon: '🎙️',
    gradient: 'from-indigo-600 via-violet-700 to-purple-900',
    accentColor: 'text-indigo-600 bg-indigo-50 border-indigo-200',
    stats: ['20 Học phần chủ đề', '160+ Bài giảng & Podcast', '102 Bài luyện phản xạ'],
    highlights: [
      'Chuẩn hóa phát âm bảng IPA, trọng âm, ngữ điệu và nối âm tự nhiên như người bản xứ (Pronunciation Mastery)',
      'Luyện nghe - nói qua các tình huống giao tiếp đời sống, công việc và thảo luận chủ đề xã hội',
      'Đàm thoại trực tiếp 1 kèm 1 cùng Giáo viên & AI Tutor thông minh, sửa lỗi phát âm & ngữ pháp tức thì',
      'Hệ thống Podcast hội thoại song ngữ giúp tắm ngôn ngữ và hình thành phản xạ tự nhiên',
    ],
    lmsCourseTitles: ['Pronunciation', 'Giao tiếp và phản xạ'],
  },
  {
    id: 'office-english',
    category: 'office',
    courseSlug: 'advanced-english-communication',
    badge: 'TIẾNG ANH CÔNG SỞ & THƯƠNG MẠI',
    title: 'Tiếng Anh Văn Phòng & Giao Tiếp Nâng Cao',
    subtitle:
      'Làm chủ tiếng Anh nơi công sở với 13 chuyên đề văn phòng, kỹ năng viết Email chuyên nghiệp và Thành ngữ giao tiếp',
    icon: '💼',
    gradient: 'from-emerald-600 via-teal-700 to-cyan-900',
    accentColor: 'text-emerald-700 bg-emerald-50 border-emerald-200',
    stats: ['15 Học phần chuyên sâu', '100+ Bài giảng tình huống', '3 Bước luyện trí nhớ độc quyền'],
    highlights: [
      'Trọn bộ 13 chuyên đề Tiếng Anh văn phòng: Công sở, Ngân hàng, Kinh doanh, Đàm phán, Công tác, Nhân sự, Mua hàng...',
      'Phương pháp 3 bước trên mỗi bài học: Nghe & Đọc hiểu — Đối chiếu Song ngữ — Learn by Heart (Luyện trí nhớ)',
      'Chuyên đề Viết thư tín & Email tiếng Anh thương mại chuyên nghiệp cho người đi làm',
      'Hệ thống Thành ngữ & Cụm từ thông dụng (Idioms & Phrases) giúp giao tiếp tự nhiên, thuyết phục',
    ],
    lmsCourseTitles: ['Tiếng Anh văn phòng', 'Giao tiếp và phản xạ'],
  },
  {
    id: 'igcse-sciences',
    category: 'igcse',
    courseSlug: 'luyen-thi-igcse-alevel-cap-toc',
    badge: 'CAMBRIDGE IGCSE 1 KÈM 1',
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
      'AI chấm điểm câu hỏi tự luận bám sát Marking Scheme chuẩn Cambridge kết hợp kèm 1-1',
    ],
    lmsCourseTitles: [
      'IGCSE Co-ordinated Sciences (0654)',
      'IGCSE Biology (0610)',
      'IGCSE Chemistry (0620)',
      'IGCSE Physics (0625)',
    ],
  },
  {
    id: 'igcse-business-econ',
    category: 'igcse',
    courseSlug: 'luyen-thi-igcse-alevel-cap-toc',
    badge: 'CAMBRIDGE IGCSE 1 KÈM 1',
    title: 'Kinh Tế & Kinh Doanh Quốc Tế (Economics 0455 & Business 0450)',
    subtitle:
      'Làm chủ thuật ngữ kinh tế, phân tích Case Study và kỹ năng viết luận đạt điểm A/A* kỳ thi Cambridge IGCSE',
    icon: '📈',
    gradient: 'from-amber-600 via-orange-700 to-rose-900',
    accentColor: 'text-amber-700 bg-amber-50 border-amber-200',
    stats: ['14 Học phần chuyên đề', '69 Bài giảng song ngữ', '155+ Đề thi & Case Study'],
    highlights: [
      'Cấu trúc bài giảng 4 trang độc quyền: Bản tiếng Anh, Bản tiếng Việt, Câu hỏi mẫu Paper 2 & Syllabus',
      'Tích hợp Audio Podcast giảng giải khái niệm kinh tế - doanh nghiệp dễ hiểu, sinh động',
      'Luyện tập Case Study chia đôi màn hình (Split-Screen) kèm AI chấm chữa theo Rubric Cambridge',
      'Lộ trình kèm 1-1 cá nhân hóa giúp học sinh nắm chắc kiến thức và kỹ thuật làm bài đạt A/A*',
    ],
    lmsCourseTitles: ['IGCSE Economics (0455)', 'IGCSE Business Studies (0450)'],
  },
  {
    id: 'igcse-geo-math-esl',
    category: 'igcse',
    courseSlug: 'luyen-thi-igcse-alevel-cap-toc',
    badge: 'CAMBRIDGE IGCSE 1 KÈM 1',
    title: 'IGCSE Geography (0460), Maths (0580 / 0606) & ESL (0510)',
    subtitle:
      'Trọn bộ bài giảng tương tác, Podcast học thuật và kho đề luyện thi chuyên sâu cho học sinh trường Quốc tế & Song ngữ',
    icon: '🌍',
    gradient: 'from-cyan-700 via-sky-800 to-slate-900',
    accentColor: 'text-cyan-700 bg-cyan-50 border-cyan-200',
    stats: ['15+ Học phần', '65+ Bài giảng & Podcast', '160+ Đề luyện chuyên sâu'],
    highlights: [
      'Geography 0460: Đầy đủ 11 chuyên đề kèm bản đồ, biểu đồ, Case Study & Podcast song ngữ',
      'Mathematics 0580 & Additional Maths 0606: Hệ thống công thức, ví dụ minh họa từng bước dễ hiểu',
      'English as a Second Language (0510): Luyện chuyên sâu Reading, Writing, Listening chuẩn format mới',
      'Hỗ trợ lộ trình kèm 1-1 cá nhân hóa và lịch báo bài tự động theo mục tiêu kỳ thi',
    ],
    lmsCourseTitles: [
      'IGCSE Geography (0460)',
      'IGCSE Mathematics (0580)',
      'IGCSE Additional Mathematics (0606)',
      'IGCSE English as a Second Language (0510)',
    ],
  },
];

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
  const { lang, t, user, options } = useApp();

  const [allCategories, setAllCategories] = useState<any[]>([]);
  const [currentCourse, setCurrentCourse] = useState<any | null>(null);
  const [lectureCount, setLectureCount] = useState(0);
  const [openParentId, setOpenParentId] = useState<number | null>(null);
  const [mobileCateOpen, setMobileCateOpen] = useState(false);

  // LMS Curriculum data (for course syllabus display)
  const [lmsCoursesWithModules, setLmsCoursesWithModules] = useState<
    Array<{
      id: string;
      title: string;
      modules: Array<{ id: string; title: string; lectures: Array<{ id: string; title: string }> }>;
    }>
  >([]);
  const [expandedModuleIds, setExpandedModuleIds] = useState<Record<string, boolean>>({});

  // Syllabus popup & Registration form state
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

  useEffect(() => {
    async function loadCoursesAndCurriculum() {
      const [cateRes, lmsCourseRes, lmsModRes, lmsLecRes] = await Promise.all([
        supabase
          .from('te_course_category')
          .select('*')
          .eq('deleted', 0)
          .eq('cc_status', 1)
          .order('cc_order', { ascending: true }),
        supabase.from('courses').select('id, title, order_index').order('order_index', { ascending: true }),
        supabase
          .from('lecture_modules')
          .select('id, course_id, title, order_index')
          .order('order_index', { ascending: true }),
        supabase
          .from('lectures')
          .select('id, module_id, title, order_index')
          .order('order_index', { ascending: true }),
      ]);

      // Build structured LMS curriculum tree (excluding Grammar and Vocabulary)
      if (lmsCourseRes.data && lmsModRes.data) {
        const lecsByMod: Record<string, Array<{ id: string; title: string }>> = {};
        (lmsLecRes.data || []).forEach((l: any) => {
          if (!lecsByMod[l.module_id]) lecsByMod[l.module_id] = [];
          lecsByMod[l.module_id].push({ id: l.id, title: l.title });
        });

        const modsByCourse: Record<
          string,
          Array<{ id: string; title: string; lectures: Array<{ id: string; title: string }> }>
        > = {};
        (lmsModRes.data || []).forEach((m: any) => {
          if (!modsByCourse[m.course_id]) modsByCourse[m.course_id] = [];
          modsByCourse[m.course_id].push({
            id: m.id,
            title: m.title,
            lectures: lecsByMod[m.id] || [],
          });
        });

        const structured = (lmsCourseRes.data || [])
          .filter((c: any) => (c.title || '').trim().toLowerCase() !== 'grammar and vocabulary')
          .map((c: any) => ({
            id: c.id,
            title: c.title,
            modules: modsByCourse[c.id] || [],
          }))
          .filter((c) => c.modules.length > 0);

        setLmsCoursesWithModules(structured);
      }

      if (cateRes.data) {
        const visibleCategories = cateRes.data.filter((c: any) => !isHiddenCourseCategory(c));
        setAllCategories(visibleCategories);

        if (slug && slug.toLowerCase() !== 'online') {
          const cleanSlug = decodeURIComponent(slug)
            .trim()
            .replace(/\.html$/i, '');
          const found = visibleCategories.find((c: any) => (c.cc_name_url || '').trim() === cleanSlug);
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
          } else {
            setCurrentCourse(null);
          }
        } else {
          setCurrentCourse(null);
          const firstParent = visibleCategories.find((c: any) => c.cc_parent === 0 && c.cc_homedisplay === 1);
          if (firstParent) setOpenParentId(firstParent.cc_id);
        }
      }
    }
    loadCoursesAndCurriculum();
    setShowJoinForm(false);
    setRegMessage(null);
  }, [slug]);

  const homeParents = allCategories.filter(
    (c) => Number(c.cc_parent) === 0 && Number(c.cc_homedisplay) === 1 && !isHiddenCourseCategory(c)
  );
  const subCategories = (parentId: number) =>
    allCategories.filter((c) => Number(c.cc_parent) === Number(parentId) && !isHiddenCourseCategory(c));

  const hasSubCategories = currentCourse
    ? allCategories.some((c) => Number(c.cc_parent) === Number(currentCourse.cc_id) && !isHiddenCourseCategory(c))
    : false;

  // Match current course to its Online Syllabus Packages & LMS Curriculum Modules
  const getMatchedSyllabusData = (course: any | null) => {
    if (!course) {
      return {
        packages: COURSE_SYLLABUS_PACKAGES,
        lmsCourses: lmsCoursesWithModules,
      };
    }

    const cid = Number(course.cc_id);
    const pid = Number(course.cc_parent);

    // 1. Giao tiếp căn bản (111) & children: Phát âm (114), Luyện phản xạ (115), Tình huống giao tiếp (116)
    if (cid === 111 || pid === 111) {
      const pkgs = COURSE_SYLLABUS_PACKAGES.filter((p) => p.category === 'comm');
      if (cid === 114) {
        // Phát âm
        return {
          packages: pkgs,
          lmsCourses: lmsCoursesWithModules.filter((c) => c.title === 'Pronunciation'),
        };
      }
      if (cid === 115) {
        // Luyện phản xạ
        return {
          packages: pkgs,
          lmsCourses: lmsCoursesWithModules
            .filter((c) => c.title === 'Giao tiếp và phản xạ')
            .map((c) => ({
              ...c,
              modules: c.modules.filter((_, idx) => idx < 5),
            })),
        };
      }
      if (cid === 116) {
        // Tình huống giao tiếp
        return {
          packages: pkgs,
          lmsCourses: lmsCoursesWithModules
            .filter((c) => c.title === 'Giao tiếp và phản xạ')
            .map((c) => ({
              ...c,
              modules: c.modules.filter((_, idx) => idx >= 5 && idx < 11),
            })),
        };
      }
      return {
        packages: pkgs,
        lmsCourses: lmsCoursesWithModules
          .filter((c) => c.title === 'Pronunciation' || c.title === 'Giao tiếp và phản xạ')
          .map((c) =>
            c.title === 'Giao tiếp và phản xạ' ? { ...c, modules: c.modules.filter((_, idx) => idx < 11) } : c
          ),
      };
    }

    // 2. Giao tiếp nâng cao (129) & children: Tiếng Anh văn phòng (123), Học viết Email (124), Thành ngữ (128)
    if (cid === 129 || pid === 129) {
      const pkgs = COURSE_SYLLABUS_PACKAGES.filter((p) => p.category === 'office');
      if (cid === 123) {
        // Tiếng Anh văn phòng
        return {
          packages: pkgs,
          lmsCourses: lmsCoursesWithModules.filter((c) => c.title === 'Tiếng Anh văn phòng'),
        };
      }
      if (cid === 124) {
        // Học viết Email
        return {
          packages: pkgs,
          lmsCourses: lmsCoursesWithModules
            .filter((c) => c.title === 'Giao tiếp và phản xạ' || c.title === 'Tiếng Anh văn phòng')
            .map((c) =>
              c.title === 'Giao tiếp và phản xạ'
                ? { ...c, modules: c.modules.filter((m) => m.title.toLowerCase().includes('email')) }
                : c
            ),
        };
      }
      if (cid === 128) {
        // Thành ngữ thông dụng
        return {
          packages: pkgs,
          lmsCourses: lmsCoursesWithModules
            .filter((c) => c.title === 'Giao tiếp và phản xạ')
            .map((c) => ({
              ...c,
              modules: c.modules.filter((m) => m.title.toLowerCase().includes('thành ngữ')),
            })),
        };
      }
      return {
        packages: pkgs,
        lmsCourses: lmsCoursesWithModules
          .filter((c) => c.title === 'Tiếng Anh văn phòng' || c.title === 'Giao tiếp và phản xạ')
          .map((c) =>
            c.title === 'Giao tiếp và phản xạ' ? { ...c, modules: c.modules.filter((_, idx) => idx >= 11) } : c
          ),
      };
    }

    // 3. Luyện thi IELTS (127)
    if (cid === 127) {
      return {
        packages: COURSE_SYLLABUS_PACKAGES.filter((p) => p.category === 'ielts'),
        lmsCourses: lmsCoursesWithModules.filter((c) => c.title === 'IELTS Premium'),
      };
    }

    // 4. Luyện thi IGCSE / A-Level (132)
    if (cid === 132) {
      return {
        packages: COURSE_SYLLABUS_PACKAGES.filter((p) => p.category === 'igcse'),
        lmsCourses: lmsCoursesWithModules.filter((c) => c.title.toUpperCase().includes('IGCSE')),
      };
    }

    // Fallback (e.g. SAT 133)
    return {
      packages: [],
      lmsCourses: [],
    };
  };

  const matchedSyllabus = getMatchedSyllabusData(currentCourse);
  const totalMatchedLectures = matchedSyllabus.lmsCourses.reduce(
    (sum, c) => sum + c.modules.reduce((mSum, m) => mSum + m.lectures.length, 0),
    0
  );
  const displayLectureCount = totalMatchedLectures > 0 ? totalMatchedLectures : lectureCount;

  const toggleModuleExpand = (modId: string) => {
    setExpandedModuleIds((prev) => ({ ...prev, [modId]: !prev[modId] }));
  };

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

  const courseTitle = currentCourse
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
    updatePageSeo(courseTitle, courseDescHtml);
  }, [courseTitle, courseDescHtml]);

  const childCoursesOfCurrent = currentCourse ? subCategories(currentCourse.cc_id) : [];

  // Reusable renderer for the Syllabus Content (used both inline on the page and in the Syllabus Modal)
  const renderSyllabusContent = (isModal = false) => {
    const { packages, lmsCourses } = matchedSyllabus;

    return (
      <div className="space-y-6">
        {/* 1. Package Overview & Highlights */}
        {packages.length > 0 && (
          <div className={`grid grid-cols-1 ${packages.length > 1 && !isModal ? 'md:grid-cols-2' : ''} gap-5`}>
            {packages.map((pkg) => (
              <div
                key={pkg.id}
                className="bg-white rounded-3xl border border-slate-200/90 shadow-xs hover:shadow-md transition-all duration-300 flex flex-col overflow-hidden"
              >
                <div className={`bg-gradient-to-br ${pkg.gradient} p-5 sm:p-6 text-white relative`}>
                  <div className="flex items-center justify-between gap-2 mb-2.5">
                    <span className="bg-white/20 backdrop-blur-md text-white text-[11px] font-black uppercase tracking-wider px-3 py-1 rounded-full border border-white/25">
                      {pkg.badge}
                    </span>
                    <span className="text-2xl sm:text-3xl">{pkg.icon}</span>
                  </div>
                  <h3 className="text-lg sm:text-xl font-black leading-snug mb-1.5">{pkg.title}</h3>
                  <p className="text-xs sm:text-sm text-white/90 font-medium leading-relaxed">{pkg.subtitle}</p>
                </div>

                <div className="bg-slate-50 px-5 py-3 border-b border-slate-100 flex flex-wrap gap-2">
                  {pkg.stats.map((st, idx) => (
                    <span
                      key={idx}
                      className={`text-xs font-bold px-2.5 py-1 rounded-lg border ${pkg.accentColor}`}
                    >
                      {st}
                    </span>
                  ))}
                </div>

                <div className="p-5 sm:p-6 flex-1 flex flex-col justify-between">
                  <ul className="space-y-2.5">
                    {pkg.highlights.map((item, i) => (
                      <li
                        key={i}
                        className="flex items-start gap-2.5 text-sm sm:text-[15px] text-slate-700 font-medium leading-relaxed"
                      >
                        <span className="text-emerald-500 font-black mt-0.5 shrink-0">✔</span>
                        <span>{item}</span>
                      </li>
                    ))}
                  </ul>

                  {!currentCourse && (
                    <div className="pt-4 mt-4 border-t border-slate-100 flex items-center justify-between gap-2">
                      <Link
                        to={`/courses/${pkg.courseSlug}`}
                        className="text-sm font-black text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1.5"
                      >
                        <span>Xem chi tiết &amp; Đề cương từng học phần</span>
                        <span>→</span>
                      </Link>
                      <a
                        href={CONTACT_ZALO_URL}
                        target="_blank"
                        rel="noreferrer"
                        className="bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs px-3.5 py-2 rounded-xl transition"
                      >
                        💬 Tư vấn Zalo
                      </a>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}

        {/* 2. Detailed LMS Curriculum Modules & Lectures */}
        {lmsCourses.length > 0 && currentCourse && (
          <div className="space-y-5">
            {lmsCourses.map((lmsCourse) => {
              const totalLecs = lmsCourse.modules.reduce((s, m) => s + m.lectures.length, 0);
              return (
                <div
                  key={lmsCourse.id}
                  className="bg-slate-50/80 rounded-2xl border border-slate-200/90 overflow-hidden"
                >
                  <div className="bg-white px-5 py-4 border-b border-slate-200/80 flex flex-wrap items-center justify-between gap-2">
                    <div className="flex items-center gap-2.5">
                      <span className="w-8 h-8 rounded-lg bg-sky-100 text-[#0a5482] flex items-center justify-center font-black text-base">
                        📚
                      </span>
                      <div>
                        <h4 className="font-black text-slate-800 text-base sm:text-lg">
                          Đề cương chi tiết: {lmsCourse.title}
                        </h4>
                        <p className="text-xs text-slate-500 font-semibold">
                          {lmsCourse.modules.length} học phần • {totalLecs} bài giảng chuyên sâu
                        </p>
                      </div>
                    </div>
                  </div>

                  <div className="p-4 sm:p-5 space-y-2.5">
                    {lmsCourse.modules.map((mod, mIdx) => {
                      const isExpanded =
                        expandedModuleIds[mod.id] !== undefined ? expandedModuleIds[mod.id] : mIdx === 0;
                      return (
                        <div
                          key={mod.id}
                          className="bg-white rounded-xl border border-slate-200/80 overflow-hidden shadow-2xs"
                        >
                          <button
                            type="button"
                            onClick={() => toggleModuleExpand(mod.id)}
                            className="w-full px-4 py-3 text-left flex items-center justify-between gap-3 hover:bg-sky-50/50 transition cursor-pointer"
                          >
                            <div className="flex items-center gap-2.5 min-w-0">
                              <span className="w-6 h-6 rounded-md bg-[#0a5482] text-white text-xs font-black flex items-center justify-center shrink-0">
                                {mIdx + 1}
                              </span>
                              <span className="font-extrabold text-sm sm:text-[15px] text-slate-800 truncate">
                                {mod.title}
                              </span>
                            </div>
                            <div className="flex items-center gap-2 shrink-0">
                              <span className="text-xs font-bold text-slate-500 bg-slate-100 px-2.5 py-0.5 rounded-full">
                                {mod.lectures.length} bài học
                              </span>
                              <span className="text-xs text-[#0a5482] font-black">
                                {isExpanded ? '▲' : '▼'}
                              </span>
                            </div>
                          </button>

                          {isExpanded && mod.lectures.length > 0 && (
                            <div className="px-4 pb-3.5 pt-1 border-t border-slate-100 bg-slate-50/40">
                              <ul className="grid grid-cols-1 sm:grid-cols-2 gap-1.5 pt-2">
                                {mod.lectures.map((lec, lIdx) => (
                                  <li
                                    key={lec.id}
                                    className="flex items-start gap-2 text-xs sm:text-[13.5px] text-slate-700 bg-white px-3 py-2 rounded-lg border border-slate-200/60"
                                  >
                                    <span className="text-[#2ab4e8] font-black shrink-0">
                                      {lIdx + 1}.
                                    </span>
                                    <span className="font-medium leading-snug">{lec.title}</span>
                                  </li>
                                ))}
                              </ul>
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>
              );
            })}
          </div>
        )}

        {/* Fallback legacy outline if any course has no matched package */}
        {packages.length === 0 && lmsCourses.length === 0 && currentCourse && (
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
        )}
      </div>
    );
  };

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
        <span className="text-[#0a5482] font-bold">{courseTitle}</span>
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
              <span className="opacity-80 shrink-0">🎓</span>
              <span className="shrink-0">{t('Courses')}</span>
              <span className="lg:hidden font-semibold text-[#0a5482] normal-case tracking-normal truncate">
                • {courseTitle}
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
            <ul className="divide-y divide-slate-100 text-[14.5px] p-1.5">
              <li>
                <Link
                  to="/courses"
                  onClick={() => setMobileCateOpen(false)}
                  className={`block px-3.5 py-2.5 rounded-xl transition-colors ${
                    !currentCourse
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
                  openParentId === parent.cc_id ||
                  (currentCourse &&
                    (currentCourse.cc_id === parent.cc_id || currentCourse.cc_parent === parent.cc_id));
                const parentName = lang === 'vi' ? parent.cc_name_vi || parent.cc_name : parent.cc_name;
                const isCurrentParent = currentCourse && currentCourse.cc_id === parent.cc_id;

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
                          const isActiveSub = currentCourse && currentCourse.cc_id === sub.cc_id;
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
          </div>
        </aside>

        {/* RIGHT MAIN CONTENT */}
        <div className="flex-1 min-w-0 w-full space-y-6">
          <div className="bg-white rounded-3xl border border-slate-200/80 shadow-xs overflow-hidden">
            {/* Course Header Banner */}
            <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-6 sm:px-8 py-6 text-white flex flex-wrap items-center justify-between gap-4">
              <div>
                <div className="text-xs sm:text-sm font-extrabold uppercase tracking-widest text-[#2ab4e8] mb-1">
                  🎓 {lang === 'vi' ? 'Chương trình đào tạo tại TonyEnglish' : 'Training Programs at TonyEnglish'}
                </div>
                <h1 className="text-2xl sm:text-3xl font-black tracking-tight">{courseTitle}</h1>
              </div>
              {currentCourse && (
                <button
                  type="button"
                  onClick={() => setShowSyllabusModal(true)}
                  className="bg-white/15 hover:bg-white/25 text-white border border-white/25 text-sm font-bold px-4 py-2 rounded-xl transition cursor-pointer flex items-center gap-1.5"
                >
                  <span>📋</span>
                  <span>{t('Courses Syllabus')}</span>
                </button>
              )}
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
                      <div className="font-black text-slate-800 text-base">{displayLectureCount} bài giảng</div>
                    </div>
                  </div>

                  <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200/70 flex items-center gap-3.5">
                    <div className="w-11 h-11 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center text-xl font-black">
                      💳
                    </div>
                    <div>
                      <div className="text-xs font-bold text-slate-400 uppercase">{t('Tuition fee')}</div>
                      <div className="font-black text-[#0a5482] text-base">
                        {currentCourse.cc_tuition || 'Học 1 kèm 1 / Liên hệ'}
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {/* Course Description HTML */}
              {courseDescHtml && (
                <div
                  className="legacy-prose text-justify"
                  dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(courseDescHtml) }}
                />
              )}

              {/* INLINE COURSE SYLLABUS (FROM ONLINE PACKAGES & LMS MODULES) */}
              <div className="pt-4 border-t border-slate-200/80 space-y-4">
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div>
                    <h2 className="text-xl sm:text-2xl font-black text-[#0a5482] flex items-center gap-2">
                      <span>📋</span>
                      <span>
                        {currentCourse
                          ? `${t('Courses Syllabus')}: ${courseTitle}`
                          : lang === 'vi'
                          ? 'Đề Cương Các Khóa Học Đào Tạo Tại TonyEnglish'
                          : 'Course Syllabuses at TonyEnglish'}
                      </span>
                    </h2>
                    <p className="text-xs sm:text-sm text-slate-500 font-medium mt-0.5">
                      Lộ trình học 1 kèm 1 kết hợp hệ thống bài giảng tương tác, Podcast &amp; luyện đề AI 24/7
                    </p>
                  </div>
                </div>

                {renderSyllabusContent(false)}
              </div>

              {/* Action Buttons for Course */}
              {currentCourse && (
                <div className="pt-6 border-t border-slate-200 flex flex-wrap items-center gap-3">
                  <button
                    type="button"
                    onClick={() => setShowJoinForm(!showJoinForm)}
                    className="bg-[#0a5482] hover:bg-[#084266] text-white font-black text-sm px-6 py-3 rounded-xl shadow-lg shadow-blue-900/15 transition active:scale-95 flex items-center gap-2 cursor-pointer"
                  >
                    <span>✍️</span>
                    <span>{t('Join now')}</span>
                  </button>

                  <button
                    type="button"
                    onClick={() => setShowSyllabusModal(true)}
                    className="bg-sky-50 hover:bg-sky-100 text-[#0a5482] border border-sky-200 font-extrabold text-sm px-5 py-3 rounded-xl transition flex items-center gap-2 cursor-pointer"
                  >
                    <span>📋</span>
                    <span>{t('Click here view to courses Syllabus')}</span>
                  </button>

                  <a
                    href={CONTACT_ZALO_URL}
                    target="_blank"
                    rel="noreferrer"
                    className="bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm px-5 py-3 rounded-xl shadow-md transition flex items-center gap-2"
                  >
                    <span>💬</span>
                    <span>Tư vấn Zalo: {CONTACT_PHONE_DISPLAY}</span>
                  </a>
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
                          .filter((c) => c.cc_parent !== 0 && c.cc_id !== currentCourse.cc_id && !isHiddenCourseCategory(c))
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
                      className="bg-[#0a5482] hover:bg-[#084266] text-white font-black text-sm px-8 py-3 rounded-xl shadow-md transition cursor-pointer"
                    >
                      {regSubmitting ? 'Đang gửi...' : t('Submit')}
                    </button>
                  </form>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* SYLLABUS MODAL */}
      {showSyllabusModal && currentCourse && (
        <div
          className="fixed inset-0 bg-slate-900/65 backdrop-blur-xs z-50 flex items-center justify-center p-4"
          onClick={() => setShowSyllabusModal(false)}
        >
          <div
            className="bg-white rounded-3xl w-full max-w-4xl max-h-[88vh] overflow-y-auto p-6 sm:p-8 shadow-2xl relative"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between pb-4 mb-5 border-b border-slate-200">
              <h2 className="text-xl font-black text-[#0a5482]">
                📋 {t('Courses Syllabus')} — {courseTitle}
              </h2>
              <button
                type="button"
                onClick={() => setShowSyllabusModal(false)}
                className="w-8 h-8 rounded-full bg-slate-100 hover:bg-rose-500 hover:text-white text-slate-600 font-bold flex items-center justify-center transition-colors cursor-pointer"
              >
                ✕
              </button>
            </div>
            {renderSyllabusContent(true)}
          </div>
        </div>
      )}
    </div>
  );
};
