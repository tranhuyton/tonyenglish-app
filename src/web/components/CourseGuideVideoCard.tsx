import React, { useEffect, useRef, useState } from 'react';
import { Play, Sparkles, CheckCircle2, Clock } from 'lucide-react';

export interface CourseGuideVideoConfig {
  videoUrl: string;
  posterUrl: string;
  duration: string;
  badgeVi: string;
  badgeEn: string;
  titleVi: string;
  titleEn: string;
  subtitleVi: string;
  subtitleEn: string;
  highlightsVi: string[];
  highlightsEn: string[];
}

const SUPABASE_GUIDE_BASE =
  'https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/test_assets/videos/guides';

export const COURSE_GUIDE_VIDEOS: Record<number, CourseGuideVideoConfig> = {
  // 0: Học cùng Thầy Tony (Trang tổng quan /courses)
  0: {
    videoUrl: `${SUPABASE_GUIDE_BASE}/study-with-tony-guide-tonyenglish.mp4`,
    posterUrl: '/images/course-showcases/study_tony_guide_poster.webp',
    duration: '01:59',
    badgeVi: 'VIDEO GIỚI THIỆU HỆ SINH THÁI TONYENGLISH',
    badgeEn: 'COMPLETE PLATFORM WALKTHROUGH',
    titleVi: 'Khám phá trọn bộ tính năng Học cùng Thầy Tony: Gia sư 1-1, AI 24/7 & Đọc E-book tra từ',
    titleEn: 'Explore Study with Mr. Tony: 1-on-1 Tutoring, 24/7 AI & Click-to-Lookup E-books',
    subtitleVi:
      'Xem tổng quan mô hình gia sư 1 kèm 1, 5 lộ trình trọng tâm, 450+ bài giảng song ngữ, kho 1.800+ đề thi chuẩn Quốc tế, trình đọc E-book PDF click đúp tra từ điển tức thì, Thư viện Cambridge, Kho Video và Góc Học Viên – Lịch báo bài.',
    subtitleEn:
      'Tour our 1-on-1 tutoring model, 5 core programs, 450+ bilingual lectures, 1,800+ exam simulators, built-in PDF E-book reader with instant double-click dictionary, Cambridge Library, Video Store, and Student Portal.',
    highlightsVi: [
      'Gia sư 1-1 tại Royal City & Online • Học thử 2–3 buổi',
      'Đọc sách E-book PDF & Click đúp tra từ điển tức thì',
      '450+ bài giảng, 1.800+ đề & Thầy Tony AI Chủ nhiệm',
    ],
    highlightsEn: [
      '1-on-1 Tutoring (Royal City & Online) • 2–3 Free Trials',
      'PDF E-book Reader with instant double-click dictionary',
      '450+ lectures, 1,800+ tests & Teacher Tony AI Coach',
    ],
  },
  // 111: Giao tiếp Căn bản
  111: {
    videoUrl: `${SUPABASE_GUIDE_BASE}/comm-basic-guide-tonyenglish.mp4`,
    posterUrl: '/images/course-showcases/comm_basic_guide_poster.webp',
    duration: '01:44',
    badgeVi: 'VIDEO HƯỚNG DẪN CHI TIẾT',
    badgeEn: 'PLATFORM WALKTHROUGH VIDEO',
    titleVi: 'Xem cách học Giao tiếp Căn bản: 44 âm IPA & Phản xạ AI trên TonyEnglish.vn',
    titleEn: 'See How to Master Basic Communication (44 IPA & AI Reflex) on TonyEnglish.vn',
    subtitleVi:
      'Khám phá lộ trình chuẩn hóa 44 âm IPA kèm sơ đồ khẩu hình, 90 mẫu câu phản xạ có micro chấm phát âm AI, hội thoại nhập vai Podcast Shadowing, 102 đề nghe và Thầy Tony AI Chủ nhiệm.',
    subtitleEn:
      'Explore our 44-sound IPA chart with articulation guides, 90 reflex sentence patterns with AI pronunciation scoring, role-play dialogues, 102 listening tests, and Teacher Tony AI Coach.',
    highlightsVi: [
      '32 bài Phát âm 44 âm IPA & sơ đồ khẩu hình',
      '90 mẫu câu Micro chấm AI & Nhập vai hội thoại',
      '102 đề luyện nghe & Thầy Tony AI Chủ nhiệm',
    ],
    highlightsEn: [
      '32 IPA pronunciation & articulation lessons',
      '90 reflex patterns with AI mic scoring & role-play',
      '102 listening drills & Teacher Tony AI Coach',
    ],
  },
  // 129: Giao tiếp Nâng cao
  129: {
    videoUrl: `${SUPABASE_GUIDE_BASE}/comm-adv-guide-tonyenglish.mp4`,
    posterUrl: '/images/course-showcases/comm_adv_guide_poster.webp',
    duration: '01:46',
    badgeVi: 'VIDEO HƯỚNG DẪN CHI TIẾT',
    badgeEn: 'PLATFORM WALKTHROUGH VIDEO',
    titleVi: 'Xem cách học Giao tiếp Nâng cao & Công sở (4 Học phần) trên TonyEnglish.vn',
    titleEn: 'See How to Master Advanced & Business English (4 Modules) on TonyEnglish.vn',
    subtitleVi:
      'Trải nghiệm trọn bộ 52 bài Tiếng Anh Văn phòng (Learn by Heart), 150 Thành ngữ bản xứ, 60 mẫu Email chuẩn quốc tế chấm AI, 24 tình huống Phỏng vấn STAR (Mock Interview AI) và Thầy Tony AI Chủ nhiệm.',
    subtitleEn:
      'Experience 52 Office English lessons with Active Recall, 150 native idioms, 60 Business Email models with AI coaching, 24 STAR Job Interview scenarios with AI Mock Interviews, and Teacher Tony AI Coach.',
    highlightsVi: [
      '52 bài Văn phòng & 150 Thành ngữ Active Recall',
      '60 mẫu Email & 24 Phỏng vấn STAR chấm AI 24/7',
      'Thầy Tony AI Chủ nhiệm đồng bộ 4 học phần',
    ],
    highlightsEn: [
      '52 Office lessons & 150 idioms with Active Recall',
      '60 Email models & 24 STAR AI Mock Interviews',
      'Teacher Tony AI Coach across all 4 modules',
    ],
  },
  // 132: Luyện thi IGCSE / A-Level cấp tốc
  132: {
    videoUrl: `${SUPABASE_GUIDE_BASE}/igcse-guide-tonyenglish.mp4`,
    posterUrl: '/images/course-showcases/igcse_guide_poster.webp',
    duration: '01:44',
    badgeVi: 'VIDEO HƯỚNG DẪN CHI TIẾT',
    badgeEn: 'PLATFORM WALKTHROUGH VIDEO',
    titleVi: 'Xem cách luyện thi Cambridge IGCSE đạt A–A* trên TonyEnglish.vn',
    titleEn: 'See How to Ace Cambridge IGCSE (A–A*) on TonyEnglish.vn',
    subtitleVi:
      'Trải nghiệm trực tiếp 10 môn IGCSE chuẩn Syllabus: Bài giảng song ngữ kèm Audio, kho 990+ đề Past Papers Paper 2/4/Case Study chấm AI sát Marking Scheme và Thầy Tony AI Chủ nhiệm.',
    subtitleEn:
      'Explore all 10 Cambridge IGCSE subjects: bilingual lectures with audio, 990+ Past Papers graded against Marking Schemes, and Teacher Tony AI Study Coach.',
    highlightsVi: [
      '10 môn chuẩn Syllabus & Audio song ngữ',
      '990+ đề Paper 2, Paper 4 & Case Study chấm AI',
      'Thầy Tony AI Chủ nhiệm theo sát tiến độ 24/7',
    ],
    highlightsEn: [
      '10 Syllabus-aligned bilingual subjects',
      '990+ Past Papers with Marking Scheme AI',
      'Teacher Tony AI Study Coach 24/7',
    ],
  },
  // 127: Luyện thi IELTS cấp tốc
  127: {
    videoUrl: `${SUPABASE_GUIDE_BASE}/ielts-guide-tonyenglish.mp4`,
    posterUrl: '/images/course-showcases/ielts_guide_poster.webp',
    duration: '02:02',
    badgeVi: 'VIDEO HƯỚNG DẪN CHI TIẾT',
    badgeEn: 'PLATFORM WALKTHROUGH VIDEO',
    titleVi: 'Xem cách luyện thi IELTS 4 kỹ năng chuẩn phòng thi IDP/BC trên TonyEnglish.vn',
    titleEn: 'See How to Master IELTS 4 Skills on Our IDP/BC Exam Simulator',
    subtitleVi:
      'Khám phá trọn bộ 79 bài giảng chiến thuật, 621 đề Cambridge 1–20 trên phòng thi máy tính chuẩn IDP/BC, AI chấm chữa Writing/Speaking 4 tiêu chí và Thầy Tony AI Chủ nhiệm.',
    subtitleEn:
      'Discover 79 strategy lectures, 621 Cambridge tests on our IDP/BC computer simulator, 4-criteria AI Writing & Speaking feedback, and Teacher Tony AI Coach.',
    highlightsVi: [
      '79 bài giảng chiến thuật & 621 đề chuẩn IDP/BC',
      'AI chấm Writing & Speaking chi tiết 4 tiêu chí',
      'Thư viện Cam 1–21 & Thầy Tony AI Chủ nhiệm',
    ],
    highlightsEn: [
      '79 strategy lectures & 621 IDP/BC tests',
      '4-criteria AI Writing & Speaking feedback',
      'Cambridge 1–21 Library & AI Study Coach',
    ],
  },
  // 133: Luyện thi SAT cấp tốc
  133: {
    videoUrl: `${SUPABASE_GUIDE_BASE}/sat-guide-tonyenglish.mp4`,
    posterUrl: '/images/course-showcases/sat_guide_poster.webp',
    duration: '01:46',
    badgeVi: 'VIDEO HƯỚNG DẪN CHI TIẾT',
    badgeEn: 'PLATFORM WALKTHROUGH VIDEO',
    titleVi: 'Xem cách luyện thi Digital SAT 1500+ trên Phòng thi Bluebook & Desmos',
    titleEn: 'See How to Score 1500+ on Digital SAT with Our Bluebook & Desmos Simulator',
    subtitleVi:
      'Khám phá 36 bài giảng chiến thuật R&W 1500+ & Math Desmos 800, kho 64+ đề trên phòng thi giả lập chuẩn Bluebook College Board tích hợp máy tính đồ thị Desmos và Thầy Tony AI Chủ nhiệm.',
    subtitleEn:
      'Discover 36 targeted 1500+ R&W & Desmos 800 lectures, 64+ drills & mocks on an authentic Bluebook simulator with built-in Desmos Graphing Calculator, and Teacher Tony AI Coach.',
    highlightsVi: [
      '36 bài chiến thuật R&W & Math Desmos 800',
      '64+ đề Phòng thi Bluebook tích hợp Desmos thật',
      'Thầy Tony AI Chủ nhiệm soi lỗi Hard Module 2',
    ],
    highlightsEn: [
      '36 R&W & Desmos 800 strategy lectures',
      '64+ tests on Bluebook simulator with live Desmos',
      'Teacher Tony AI Coach for Hard Module 2',
    ],
  },
};

interface CourseGuideVideoCardProps {
  courseId: number | null | undefined;
  lang: 'vi' | 'en';
}

export const CourseGuideVideoCard: React.FC<CourseGuideVideoCardProps> = ({ courseId, lang }) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const videoRef = useRef<HTMLVideoElement | null>(null);

  const config =
    courseId !== null && courseId !== undefined ? COURSE_GUIDE_VIDEOS[Number(courseId)] : undefined;

  useEffect(() => {
    setIsPlaying(false);
  }, [courseId]);

  if (!config) return null;

  const handleStartPlay = () => {
    setIsPlaying(true);
    try {
      const fbq = (window as any)?.fbq;
      if (typeof fbq === 'function') {
        fbq('trackCustom', 'CourseGuideVideoPlay', {
          course_id: Number(courseId),
          course_title: config.titleVi,
        });
      }
    } catch {
      // ignore tracking errors
    }
  };

  const highlights = lang === 'vi' ? config.highlightsVi : config.highlightsEn;

  return (
    <section className="rounded-2xl overflow-hidden border border-sky-200/80 bg-gradient-to-br from-[#07182c] via-[#0a2947] to-[#0a5482] text-white shadow-md">
      <div className="p-4 sm:p-6 space-y-4">
        {/* Header Row */}
        <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-2.5">
          <div className="space-y-1.5 min-w-0">
            <div className="flex flex-wrap items-center gap-2">
              <span className="inline-flex items-center gap-1.5 text-[11px] font-black uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-400/40 px-2.5 py-0.5 rounded-full">
                <Sparkles className="w-3.5 h-3.5" />
                <span>{lang === 'vi' ? config.badgeVi : config.badgeEn}</span>
              </span>
              <span className="inline-flex items-center gap-1 text-[11px] font-extrabold bg-white/10 text-sky-200 border border-white/15 px-2.5 py-0.5 rounded-full">
                <Clock className="w-3 h-3" />
                <span>{config.duration} • Full HD</span>
              </span>
            </div>
            <h2 className="text-base sm:text-xl font-black text-white leading-snug">
              {lang === 'vi' ? config.titleVi : config.titleEn}
            </h2>
            <p className="text-xs sm:text-[13.5px] text-sky-100/90 leading-relaxed max-w-3xl">
              {lang === 'vi' ? config.subtitleVi : config.subtitleEn}
            </p>
          </div>
        </div>

        {/* 16:9 Lazy Click-to-Play Video Stage */}
        <div className="relative w-full aspect-video rounded-xl overflow-hidden bg-slate-950 border border-white/15 shadow-xl">
          {!isPlaying ? (
            <button
              type="button"
              onClick={handleStartPlay}
              aria-label={lang === 'vi' ? 'Phát video hướng dẫn khóa học' : 'Play course guide video'}
              className="group relative w-full h-full block text-left cursor-pointer focus:outline-none"
            >
              <img
                src={config.posterUrl}
                alt={lang === 'vi' ? config.titleVi : config.titleEn}
                loading="eager"
                className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-[1.02]"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-slate-950/65 via-slate-950/15 to-transparent transition-opacity group-hover:from-slate-950/50" />
              <div className="absolute inset-0 flex flex-col items-center justify-center gap-3 p-4">
                <span className="w-16 h-16 sm:w-20 sm:h-20 rounded-full bg-gradient-to-br from-[#0ea5e9] to-[#059669] text-white flex items-center justify-center shadow-[0_0_0_8px_rgba(14,165,233,0.28)] group-hover:scale-110 group-hover:shadow-[0_0_0_12px_rgba(14,165,233,0.36)] transition-all duration-300">
                  <Play className="w-7 h-7 sm:w-9 sm:h-9 fill-current ml-1" />
                </span>
                <span className="px-4 py-1.5 rounded-full bg-slate-950/80 backdrop-blur-xs border border-white/25 text-xs sm:text-sm font-extrabold text-white shadow-lg">
                  {lang === 'vi'
                    ? `▶ Bấm xem video hướng dẫn (${config.duration})`
                    : `▶ Watch walkthrough video (${config.duration})`}
                </span>
              </div>
            </button>
          ) : (
            <video
              ref={videoRef}
              src={config.videoUrl}
              poster={config.posterUrl}
              controls
              autoPlay
              playsInline
              preload="auto"
              controlsList="nodownload"
              className="w-full h-full object-contain bg-black"
            >
              {lang === 'vi'
                ? 'Trình duyệt của bạn không hỗ trợ phát video HTML5.'
                : 'Your browser does not support HTML5 video playback.'}
            </video>
          )}
        </div>

        {/* Key Highlights Strip */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
          {highlights.map((item, idx) => (
            <div
              key={idx}
              className="flex items-center gap-2 px-3 py-2 rounded-xl bg-white/8 border border-white/12 text-xs sm:text-[13px] font-bold text-sky-50"
            >
              <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
              <span className="leading-snug">{item}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
