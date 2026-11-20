import React, { useEffect, useRef, useState } from 'react';
import { Link, useParams, useNavigate } from 'react-router-dom';
import {
  Home,
  Video,
  Play,
  Tv,
  Subtitles,
  HelpCircle,
  ChevronDown,
  ChevronUp,
  ArrowRight,
  Film,
  CheckCircle2,
} from 'lucide-react';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import { resolveUploadUrl, getYoutubeEmbedUrl, fixLegacyHtmlContent, updatePageSeo } from '../lib/utils';
import { VideoInteractiveQuiz, parseVideoQuizData } from '../components/VideoInteractiveQuiz';
import {
  insertLibraryReadLog,
  insertLibraryExerciseLog,
  updateLibraryReadDuration,
  LibraryReadLogInput,
} from '../lib/libraryActivityLogger';

export const VideosPage: React.FC<{ mode: 'cate' | 'watch' }> = ({ mode }) => {
  const { cateSlug, videoSlug } = useParams<{ cateSlug?: string; videoSlug?: string }>();
  const { lang, t } = useApp();
  const navigate = useNavigate();

  const [allVideoCates, setAllVideoCates] = useState<any[]>([]);
  const [videosInCate, setVideosInCate] = useState<any[]>([]);
  const [currentVideo, setCurrentVideo] = useState<any | null>(null);

  const [showQuestion, setShowQuestion] = useState(false);
  const [showAnswer, setShowAnswer] = useState(false);
  const [showSubtitles, setShowSubtitles] = useState(false);
  const [mobileCateOpen, setMobileCateOpen] = useState(false);
  const videoOpenedAtRef = useRef<number>(Date.now());

  useEffect(() => {
    async function loadVideoCategories() {
      const { data } = await supabase
        .from('te_video_category')
        .select('*')
        .eq('deleted', 0)
        .eq('vc_status', 1)
        .order('vc_order', { ascending: true });
      if (data) setAllVideoCates(data);
    }
    loadVideoCategories();
  }, []);

  useEffect(() => {
    if (allVideoCates.length === 0) return;

    async function loadModeData() {
      setShowQuestion(false);
      setShowAnswer(false);
      setShowSubtitles(false);

      const cleanCateSlug = decodeURIComponent(cateSlug || '')
        .trim()
        .replace(/\.html$/i, '');
      const cleanVideoSlug = decodeURIComponent(videoSlug || '')
        .trim()
        .replace(/\.html$/i, '');

      if (mode === 'cate') {
        if (cleanCateSlug) {
          const target = allVideoCates.find((vc) => (vc.vc_name_url || '').trim() === cleanCateSlug);
          if (target) {
            const subCates = allVideoCates.filter((vc) => Number(vc.vc_parent) === Number(target.vc_id));
            if (subCates.length === 0) {
              navigate(`/video/${cleanCateSlug}`, { replace: true });
              return;
            }
          }
        }
      } else {
        const targetCate = allVideoCates.find((vc) => (vc.vc_name_url || '').trim() === cleanCateSlug);
        if (cleanVideoSlug) {
          const { data: vRows } = await supabase
            .from('te_video')
            .select('*')
            .eq('deleted', 0)
            .eq('video_status', 1)
            .eq('video_url', cleanVideoSlug)
            .limit(1);
          const cur = vRows && vRows.length > 0 ? vRows[0] : null;
          setCurrentVideo(cur);
          if (cur) {
            const { data: list } = await supabase
              .from('te_video')
              .select('*')
              .eq('deleted', 0)
              .eq('video_status', 1)
              .eq('vc_id', cur.vc_id)
              .order('video_order', { ascending: true });
            setVideosInCate(list || []);
          }
        } else if (targetCate) {
          const { data: list } = await supabase
            .from('te_video')
            .select('*')
            .eq('deleted', 0)
            .eq('video_status', 1)
            .eq('vc_id', targetCate.vc_id)
            .order('video_order', { ascending: true });
          setVideosInCate(list || []);
          setCurrentVideo(list && list.length > 0 ? list[0] : null);
        }
      }
    }

    loadModeData();
  }, [mode, cateSlug, videoSlug, allVideoCates]);

  const topCategories = allVideoCates.filter((vc) => Number(vc.vc_parent) === 0);
  const cleanCateParam = decodeURIComponent(cateSlug || '')
    .trim()
    .replace(/\.html$/i, '');
  const activeCate = cleanCateParam
    ? allVideoCates.find((vc) => (vc.vc_name_url || '').trim() === cleanCateParam)
    : null;
  const parentCate =
    activeCate && activeCate.vc_parent
      ? allVideoCates.find((vc) => Number(vc.vc_id) === Number(activeCate.vc_parent))
      : null;

  const subCatesToDisplay = activeCate
    ? allVideoCates.filter((vc) => Number(vc.vc_parent) === Number(activeCate.vc_id))
    : topCategories;

  const mainHeading = activeCate
    ? lang === 'vi'
      ? activeCate.vc_name_vi || activeCate.vc_name
      : activeCate.vc_name
    : lang === 'vi'
    ? 'Danh mục Video'
    : 'Video Category';

  useEffect(() => {
    if (mode === 'watch' && currentVideo) {
      updatePageSeo(currentVideo.video_desc, currentVideo.video_cmt);
    } else {
      updatePageSeo(`${mainHeading} - ${t('Videos Store')}`, activeCate?.vc_desc_vi || activeCate?.vc_desc);
    }
  }, [mode, currentVideo, mainHeading, activeCate]);

  // Ghi nhận học viên xem Video trong Thư viện sau 5 giây + cập nhật thời lượng khi rời trang
  useEffect(() => {
    if (mode !== 'watch' || !currentVideo?.video_id) return;
    videoOpenedAtRef.current = Date.now();
    const vid = Number(currentVideo.video_id);
    const sessionKey = `tony_lib_vid_${vid}`;
    if (sessionStorage.getItem(sessionKey)) return;

    const vCate =
      allVideoCates.find((vc) => Number(vc.vc_id) === Number(currentVideo.vc_id)) || activeCate;
    const vParent =
      vCate && vCate.vc_parent
        ? allVideoCates.find((vc) => Number(vc.vc_id) === Number(vCate.vc_parent))
        : parentCate;
    const quizList = parseVideoQuizData(currentVideo.video_question);
    const hasLegacyQa =
      !quizList &&
      Boolean(currentVideo.video_question && String(currentVideo.video_question).trim() !== '');
    const cateSlugForUrl = (vCate?.vc_name_url || cleanCateParam || '').trim();
    const vidSlugForUrl = (currentVideo.video_url || '').trim();
    const urlPath = vidSlugForUrl
      ? `/video/${cateSlugForUrl}/${vidSlugForUrl}`
      : `/video/${cateSlugForUrl}`;

    const logDetails: LibraryReadLogInput = {
      activity_kind: 'watch_video',
      video_id: vid,
      article_title: currentVideo.video_desc || 'Video tiếng Anh',
      article_slug: vidSlugForUrl,
      url_path: urlPath,
      category_id: Number(currentVideo.vc_id) || undefined,
      parent_category_id: Number(vParent?.vc_id || vCate?.vc_id || 0) || undefined,
      category_name:
        vParent?.vc_name_vi || vParent?.vc_name || vCate?.vc_name_vi || vCate?.vc_name || 'Kho Video',
      sub_category_name: vCate?.vc_name_vi || vCate?.vc_name || '',
      library_type: 'library_video',
      has_quiz: Boolean(quizList && quizList.length > 0),
      quiz_question_count: quizList?.length || 0,
      has_legacy_qa: hasLegacyQa,
    };

    let insertedLogId: string | null = null;
    const timer = window.setTimeout(async () => {
      try {
        sessionStorage.setItem(sessionKey, '1');
      } catch {}
      insertedLogId = await insertLibraryReadLog(logDetails);
    }, 5000);

    return () => {
      window.clearTimeout(timer);
      const elapsedSec = Math.round((Date.now() - videoOpenedAtRef.current) / 1000);
      if (insertedLogId && elapsedSec >= 15) {
        updateLibraryReadDuration(insertedLogId, logDetails, elapsedSec);
      }
    };
  }, [mode, currentVideo?.video_id, allVideoCates.length]);

  return (
    <div className="max-w-7xl mx-auto px-3.5 sm:px-6 py-4 sm:py-8">
      {/* BREADCRUMB */}
      <nav className="flex items-center gap-1.5 sm:gap-2 text-xs sm:text-[15px] font-semibold text-slate-500 mb-3.5 sm:mb-6 flex-wrap">
        <Link to="/" className="hover:text-[#0a5482] flex items-center gap-1">
          <Home className="w-3.5 h-3.5 shrink-0" />
          <span>{t('Home')}</span>
        </Link>
        <span>/</span>
        <Link to="/videos" className="hover:text-[#0a5482]">
          {t('Videos Store')}
        </Link>
        {parentCate && (
          <>
            <span>/</span>
            <Link to={`/videos/${(parentCate.vc_name_url || '').trim()}`} className="hover:text-[#0a5482]">
              {lang === 'vi' ? parentCate.vc_name_vi || parentCate.vc_name : parentCate.vc_name}
            </Link>
          </>
        )}
        {activeCate && (
          <>
            <span>/</span>
            <span className="text-[#0a5482] font-bold">{mainHeading}</span>
          </>
        )}
      </nav>

      <div className="flex flex-col lg:flex-row gap-4 sm:gap-8 xl:gap-12 items-start">
        {/* LEFT SIDEBAR: SUBTLE, NON-COMPETING VIDEO MENU */}
        <aside className="w-full lg:w-[260px] xl:w-[270px] shrink-0 bg-white rounded-2xl border border-slate-200/80 shadow-sm overflow-hidden lg:sticky lg:top-24">
          <button
            type="button"
            onClick={() => setMobileCateOpen((prev) => !prev)}
            className="w-full bg-slate-100/80 px-4 py-3 border-b border-slate-200/70 flex items-center justify-between lg:pointer-events-none cursor-pointer text-left"
          >
            <h2 className="text-slate-600 lg:text-slate-500 font-bold text-xs uppercase tracking-widest flex items-center gap-2 min-w-0">
              <Video className="w-4 h-4 opacity-80 shrink-0 text-[#0a5482]" />
              <span className="hidden lg:inline shrink-0">{t('Video Menu')}</span>
              <span className="lg:hidden font-bold text-[#0a5482] text-[13px] normal-case tracking-normal truncate">
                {activeCate ? mainHeading : t('Video Category')}
              </span>
            </h2>
            <span className="lg:hidden text-[11px] font-bold text-[#0a5482] bg-white px-2.5 py-1 rounded-lg border border-slate-200/80 shadow-sm flex items-center gap-1 shrink-0 ml-2">
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

          <ul className={`divide-y divide-slate-100 text-[14.5px] p-1.5 ${mobileCateOpen ? 'block' : 'hidden'} lg:block`}>
            <li>
              <Link
                to="/videos"
                onClick={() => setMobileCateOpen(false)}
                className={`flex items-center gap-2 px-3.5 py-2.5 rounded-xl transition-colors relative ${
                  !cateSlug
                    ? "bg-sky-50/90 text-[#0a5482] font-semibold pl-4 before:content-[''] before:absolute before:left-1.5 before:top-2 before:bottom-2 before:w-1 before:rounded-full before:bg-[#2ab4e8]"
                    : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                }`}
              >
                <Tv className="w-4 h-4 shrink-0" />
                <span>{t('Video Category')}</span>
              </Link>
            </li>
            {topCategories.length === 0 && (
              <li className="py-2 px-2 space-y-2 animate-pulse">
                {[1, 2, 3, 4].map((n) => (
                  <div key={n} className="h-9 rounded-xl bg-slate-100" />
                ))}
              </li>
            )}
            {topCategories.map((vc) => {
              const isSelected =
                (vc.vc_name_url || '').trim() === cleanCateParam ||
                (parentCate && Number(parentCate.vc_id) === Number(vc.vc_id));
              return (
                <li key={vc.vc_id}>
                  <Link
                    to={`/videos/${(vc.vc_name_url || '').trim()}`}
                    onClick={() => setMobileCateOpen(false)}
                    className={`block px-3.5 py-2.5 rounded-xl transition-colors relative leading-snug ${
                      isSelected
                        ? "bg-sky-50/90 text-[#0a5482] font-semibold pl-4 before:content-[''] before:absolute before:left-1.5 before:top-2 before:bottom-2 before:w-1 before:rounded-full before:bg-[#2ab4e8]"
                        : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                    }`}
                  >
                    {lang === 'vi' ? vc.vc_name_vi || vc.vc_name : vc.vc_name}
                  </Link>
                </li>
              );
            })}
          </ul>
        </aside>

        {/* RIGHT MAIN CONTENT */}
        <div className="flex-1 min-w-0 w-full space-y-6">
          <div className="bg-white rounded-2xl sm:rounded-3xl border border-slate-200/90 shadow-sm overflow-hidden">
            {/* Header */}
            <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-4 sm:px-8 py-4 sm:py-6 text-white">
              <div className="text-[11px] sm:text-sm font-extrabold uppercase tracking-widest text-[#2ab4e8] mb-0.5 sm:mb-1">
                TonyEnglish Video Channel
              </div>
              <h1 className="text-xl sm:text-3xl font-black tracking-tight">{mainHeading}</h1>
            </div>

            <div className="p-4 sm:p-8">
              {mode === 'cate' ? (
                allVideoCates.length === 0 ? (
                  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 animate-pulse">
                    {[1, 2, 3, 4, 5, 6].map((n) => (
                      <div key={n} className="rounded-2xl border border-slate-200 overflow-hidden bg-white">
                        <div className="h-44 bg-slate-100" />
                        <div className="p-4 space-y-2">
                          <div className="h-4 bg-slate-100 rounded w-3/4" />
                          <div className="h-3 bg-slate-100 rounded w-1/2" />
                        </div>
                      </div>
                    ))}
                  </div>
                ) : (
                /* VIDEO CATEGORY GRID (Balanced Bento span when 5 items so no empty slot on row 2) */
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                  {subCatesToDisplay.map((sub, sIdx) => {
                    const childVideos = allVideoCates.filter((c) => Number(c.vc_parent) === Number(sub.vc_id));
                    const imgPath =
                      childVideos.find((c) => c.vc_image)?.vc_image || sub.vc_image || 'No_Image_Wide.svg_1.png';
                    const subTitle = lang === 'vi' ? sub.vc_name_vi || sub.vc_name : sub.vc_name;
                    const targetRoute = activeCate
                      ? `/video/${(sub.vc_name_url || '').trim()}`
                      : `/videos/${(sub.vc_name_url || '').trim()}`;
                    const isBentoLead = subCatesToDisplay.length === 5 && sIdx === 0;

                    return (
                      <Link
                        key={sub.vc_id}
                        to={targetRoute}
                        className={`group bg-white rounded-2xl border border-slate-200/80 overflow-hidden shadow-2xs hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col ${
                          isBentoLead ? 'sm:col-span-2' : ''
                        }`}
                      >
                        <div className={`relative ${isBentoLead ? 'h-48 sm:h-52' : 'h-44'} bg-slate-800 overflow-hidden`}>
                          <img
                            src={resolveUploadUrl(imgPath)}
                            alt={subTitle}
                            loading={sIdx < 3 ? 'eager' : 'lazy'}
                            onError={(e) => {
                              (e.currentTarget as HTMLImageElement).src = '/uploads/No_Image_Wide.svg_1.png';
                            }}
                            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 brightness-105"
                          />
                          <div className="absolute inset-0 bg-gradient-to-t from-slate-900/50 via-transparent to-transparent pointer-events-none" />
                          <span className="absolute bottom-3 right-3 w-10 h-10 rounded-full bg-white/95 text-[#0a5482] flex items-center justify-center shadow-lg group-hover:scale-110 group-hover:bg-[#2ab4e8] group-hover:text-white transition-all">
                            <Play className="w-4 h-4 fill-current ml-0.5" />
                          </span>
                        </div>
                        <div className="p-4 sm:p-5 flex-1 flex flex-col justify-between gap-2.5">
                          <div className="flex items-start justify-between gap-2">
                            <h3 className="font-extrabold text-[15px] sm:text-base text-slate-800 group-hover:text-[#0a5482] line-clamp-2 leading-snug">
                              {subTitle}
                            </h3>
                            <ArrowRight className="w-4 h-4 text-[#2ab4e8] shrink-0 mt-0.5 group-hover:translate-x-0.5 transition-transform" />
                          </div>
                          {childVideos.length > 0 && (
                            <div className="flex items-center gap-1.5">
                              <span className="inline-flex items-center gap-1 bg-sky-50 text-[#0a5482] border border-sky-200/80 text-[11px] font-extrabold px-2.5 py-0.5 rounded-full">
                                <Film className="w-3 h-3" />
                                <span>{childVideos.length} {lang === 'vi' ? 'chủ đề' : 'topics'}</span>
                              </span>
                            </div>
                          )}
                        </div>
                      </Link>
                    );
                  })}
                </div>
                )
              ) : (
                /* VIDEO WATCH VIEW */
                <div className="space-y-8">
                  {currentVideo && (
                    <div className="space-y-5">
                      {currentVideo.video_link && (
                        <div className="aspect-video w-full rounded-2xl overflow-hidden bg-slate-950 shadow-lg border border-slate-800">
                          <iframe
                            width="100%"
                            height="100%"
                            src={getYoutubeEmbedUrl(currentVideo.video_link)}
                            title={currentVideo.video_desc}
                            frameBorder="0"
                            referrerPolicy="strict-origin-when-cross-origin"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                            allowFullScreen
                          />
                        </div>
                      )}

                      <div>
                        <h2 className="text-xl sm:text-2xl font-black text-slate-900 mb-3">
                          {currentVideo.video_desc}
                        </h2>
                        {currentVideo.video_cmt && (
                          <div
                            className="p-5 bg-slate-50 rounded-2xl border border-slate-200/80 legacy-prose"
                            dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(currentVideo.video_cmt) }}
                          />
                        )}
                      </div>

                      {/* Subtitles & Interactive Quiz / Legacy Question */}
                      <div className="space-y-5">
                        {currentVideo.video_conversation && currentVideo.video_conversation.trim() !== '' && (
                          <div className="bg-sky-50/40 rounded-2xl border border-sky-200/80 overflow-hidden">
                            <button
                              type="button"
                              onClick={() => setShowSubtitles(!showSubtitles)}
                              className="w-full px-5 py-4 flex items-center justify-between text-left font-bold text-[15.5px] sm:text-base text-[#0a5482] hover:bg-sky-50/80 transition"
                            >
                              <span className="inline-flex items-center gap-2">
                                <Subtitles className="w-4 h-4 shrink-0 text-[#0a5482]" />
                                <span>{t('Same video with subtitles')}</span>
                              </span>
                              {showSubtitles ? <ChevronUp className="w-4 h-4 shrink-0" /> : <ChevronDown className="w-4 h-4 shrink-0" />}
                            </button>
                            {showSubtitles && (
                              <div
                                className="p-5 bg-white border-t border-sky-100 legacy-prose"
                                dangerouslySetInnerHTML={{
                                  __html: fixLegacyHtmlContent(currentVideo.video_conversation),
                                }}
                              />
                            )}
                          </div>
                        )}

                        {(() => {
                          const quizQuestions = parseVideoQuizData(currentVideo.video_question);
                          const vCate =
                            allVideoCates.find((vc) => Number(vc.vc_id) === Number(currentVideo.vc_id)) ||
                            activeCate;
                          const vParent =
                            vCate && vCate.vc_parent
                              ? allVideoCates.find((vc) => Number(vc.vc_id) === Number(vCate.vc_parent))
                              : parentCate;
                          const cateSlugForUrl = (vCate?.vc_name_url || cleanCateParam || '').trim();
                          const vidSlugForUrl = (currentVideo.video_url || '').trim();
                          const urlPath = vidSlugForUrl
                            ? `/video/${cateSlugForUrl}/${vidSlugForUrl}`
                            : `/video/${cateSlugForUrl}`;
                          const resolvedCategoryName =
                            vParent?.vc_name_vi ||
                            vParent?.vc_name ||
                            vCate?.vc_name_vi ||
                            vCate?.vc_name ||
                            'Kho Video';
                          const resolvedSubName = vCate?.vc_name_vi || vCate?.vc_name || '';

                          if (quizQuestions) {
                            return (
                              <VideoInteractiveQuiz
                                key={currentVideo.video_id}
                                videoId={currentVideo.video_id}
                                videoTitle={currentVideo.video_desc}
                                questions={quizQuestions}
                                lang={lang}
                                onQuizSubmit={(summary) => {
                                  insertLibraryExerciseLog({
                                    exercise_kind: 'video_quiz',
                                    video_id: Number(currentVideo.video_id),
                                    item_title: currentVideo.video_desc || 'Video tiếng Anh',
                                    article_slug: vidSlugForUrl,
                                    url_path: urlPath,
                                    category_id: Number(currentVideo.vc_id) || undefined,
                                    parent_category_id:
                                      Number(vParent?.vc_id || vCate?.vc_id || 0) || undefined,
                                    category_name: resolvedCategoryName,
                                    sub_category_name: resolvedSubName,
                                    library_type: 'library_video',
                                    score: summary.score,
                                    total_questions: summary.totalQuestions,
                                    percent: summary.percent,
                                    answered_count: summary.answeredCount,
                                    time_spent_sec: summary.timeSpentSec,
                                    question_results: summary.questionResults,
                                  });
                                }}
                              />
                            );
                          }

                          if (currentVideo.video_question && currentVideo.video_question.trim() !== '') {
                            return (
                              <div className="bg-sky-50/40 rounded-2xl border border-sky-200/80 overflow-hidden">
                                <button
                                  type="button"
                                  onClick={() => {
                                    setShowQuestion(!showQuestion);
                                    if (showQuestion) setShowAnswer(false);
                                  }}
                                  className="w-full px-5 py-4 flex items-center justify-between text-left font-bold text-[15.5px] sm:text-base text-[#0a5482] hover:bg-sky-50/80 transition"
                                >
                                  <span className="inline-flex items-center gap-2">
                                    <HelpCircle className="w-4 h-4 shrink-0 text-[#0a5482]" />
                                    <span>{t('View Question')}</span>
                                  </span>
                                  {showQuestion ? <ChevronUp className="w-4 h-4 shrink-0" /> : <ChevronDown className="w-4 h-4 shrink-0" />}
                                </button>

                                {showQuestion && (
                                  <div className="p-5 pt-3 bg-white border-t border-sky-100 space-y-4">
                                    <div
                                      className="legacy-prose"
                                      dangerouslySetInnerHTML={{
                                        __html: fixLegacyHtmlContent(currentVideo.video_question),
                                      }}
                                    />
                                    {currentVideo.video_answer && currentVideo.video_answer.trim() !== '' && (
                                      <div>
                                        <button
                                          type="button"
                                          onClick={() => {
                                            const nextShow = !showAnswer;
                                            setShowAnswer(nextShow);
                                            if (nextShow && currentVideo?.video_id) {
                                              const qaKey = `tony_lib_vid_qa_${currentVideo.video_id}`;
                                              if (!sessionStorage.getItem(qaKey)) {
                                                try {
                                                  sessionStorage.setItem(qaKey, '1');
                                                } catch {}
                                                insertLibraryExerciseLog({
                                                  exercise_kind: 'qa_practice',
                                                  video_id: Number(currentVideo.video_id),
                                                  item_title: currentVideo.video_desc || 'Video tiếng Anh',
                                                  article_slug: vidSlugForUrl,
                                                  url_path: urlPath,
                                                  category_id: Number(currentVideo.vc_id) || undefined,
                                                  parent_category_id:
                                                    Number(vParent?.vc_id || vCate?.vc_id || 0) ||
                                                    undefined,
                                                  category_name: resolvedCategoryName,
                                                  sub_category_name: resolvedSubName,
                                                  library_type: 'library_video',
                                                  time_spent_sec: Math.max(
                                                    1,
                                                    Math.round(
                                                      (Date.now() - videoOpenedAtRef.current) / 1000
                                                    )
                                                  ),
                                                });
                                              }
                                            }
                                          }}
                                          className="inline-flex items-center gap-1.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm px-4 py-2 rounded-xl transition"
                                        >
                                          <CheckCircle2 className="w-4 h-4" />
                                          <span>{t('View Answer')}</span>
                                        </button>
                                        {showAnswer && (
                                          <div
                                            className="mt-3 p-4 bg-emerald-50 border border-emerald-200 rounded-xl legacy-prose"
                                            dangerouslySetInnerHTML={{
                                              __html: fixLegacyHtmlContent(currentVideo.video_answer),
                                            }}
                                          />
                                        )}
                                      </div>
                                    )}
                                  </div>
                                )}
                              </div>
                            );
                          }

                          return null;
                        })()}
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>

          {/* SEPARATE AIRY BLOCK FOR VIDEO LIST IN THIS CATEGORY */}
          {mode !== 'cate' && videosInCate.length > 1 && (
            <div className="bg-white/70 rounded-2xl border border-slate-200/60 px-6 py-5 sm:px-8 sm:py-6">
              <h3 className="text-xs sm:text-[13px] font-bold uppercase tracking-widest text-slate-400 mb-4 flex items-center gap-2">
                <Film className="w-4 h-4 opacity-70 text-[#0a5482]" />
                <span>{t('Video List')}</span>
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
                {videosInCate
                  .filter((vd) => !currentVideo || vd.video_id !== currentVideo.video_id)
                  .map((vd) => {
                    const vdQuiz = parseVideoQuizData(vd.video_question);
                    return (
                      <Link
                        key={vd.video_id}
                        to={`/video/${cleanCateParam}/${(vd.video_url || '').trim()}`}
                        className="group bg-white/80 hover:bg-white rounded-2xl border border-slate-200/60 overflow-hidden hover:shadow-md transition-all flex flex-col"
                      >
                        <div className="relative h-36 bg-slate-900 overflow-hidden">
                          <img
                            src={resolveUploadUrl(vd.video_thumb)}
                            alt={vd.video_desc}
                            onError={(e) => {
                              (e.currentTarget as HTMLImageElement).src = '/uploads/No_Image_Wide.svg_1.png';
                            }}
                            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                          />
                          <div className="absolute inset-0 bg-slate-900/20 flex items-center justify-center">
                            <span className="w-9 h-9 rounded-full bg-white/90 text-[#0a5482] flex items-center justify-center text-xs shadow-md">
                              ▶
                            </span>
                          </div>
                          {vdQuiz && (
                            <span className="absolute bottom-2 right-2 bg-[#0a5482]/90 text-white text-[10.5px] font-extrabold px-2 py-0.5 rounded-md shadow-sm">
                              📝 {vdQuiz.length} {lang === 'vi' ? 'câu Quiz' : 'Qs'}
                            </span>
                          )}
                        </div>
                        <div className="p-3.5">
                          <h4 className="font-medium text-sm sm:text-[14.5px] text-slate-500 group-hover:text-[#0a5482] line-clamp-2 transition-colors">
                            {vd.video_desc}
                          </h4>
                        </div>
                      </Link>
                    );
                  })}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
