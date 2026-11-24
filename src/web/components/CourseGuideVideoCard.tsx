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
};

interface CourseGuideVideoCardProps {
  courseId: number | null | undefined;
  lang: 'vi' | 'en';
}

export const CourseGuideVideoCard: React.FC<CourseGuideVideoCardProps> = ({ courseId, lang }) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const videoRef = useRef<HTMLVideoElement | null>(null);

  const config = courseId ? COURSE_GUIDE_VIDEOS[Number(courseId)] : undefined;

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
