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
  ChevronRight,
  ArrowRight,
  Film,
  CheckCircle2,
  Headphones,
  MessageSquare,
  Globe,
  Atom,
  Landmark,
} from 'lucide-react';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import { resolveUploadUrl, getYoutubeEmbedUrl, fixLegacyHtmlContent, updatePageSeo } from '../lib/utils';
import { VideoInteractiveQuiz, parseVideoQuizData } from '../components/VideoInteractiveQuiz';
import { getLocalizedVideoComment } from '../data/studyTipsEn';
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
  const [catesLoaded, setCatesLoaded] = useState(false);
  const [loadingWatch, setLoadingWatch] = useState(false);
  const [videosInCate, setVideosInCate] = useState<any[]>([]);
  const [currentVideo, setCurrentVideo] = useState<any | null>(null);

  const [showQuestion, setShowQuestion] = useState(false);
  const [showAnswer, setShowAnswer] = useState(false);
  const [showSubtitles, setShowSubtitles] = useState(false);
  const [mobileCateOpen, setMobileCateOpen] = useState(false);
  const videoOpenedAtRef = useRef<number>(Date.now());

  useEffect(() => {
    async function loadVideoCategories() {
      try {
        const { data } = await supabase
          .from('te_video_category')
          .select('*')
          .eq('deleted', 0)
          .eq('vc_status', 1)
          .order('vc_order', { ascending: true, nullsFirst: false })
          .order('vc_id', { ascending: true });
        if (data) setAllVideoCates(data);
      } finally {
        setCatesLoaded(true);
      }
    }
    loadVideoCategories();
  }, []);

  useEffect(() => {
    if (!catesLoaded) return;

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
        setLoadingWatch(false);
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
        setLoadingWatch(true);
        try {
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
            } else {
              setVideosInCate([]);
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
          } else {
            setCurrentVideo(null);
            setVideosInCate([]);
          }
        } finally {
          setLoadingWatch(false);
        }
      }
    }

    loadModeData();
  }, [mode, cateSlug, videoSlug, allVideoCates, catesLoaded]);

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
        <aside className="w-full lg:w-[272px] xl:w-[288px] shrink-0 bg-white rounded-2xl border border-slate-200/80 shadow-sm overflow-hidden lg:sticky lg:top-24">
          <button
            type="button"
            onClick={() => setMobileCateOpen((prev) => !prev)}
            className="w-full bg-slate-100/80 px-4 py-3 border-b border-slate-200/70 flex items-center justify-between lg:pointer-events-none cursor-pointer text-left"
          >
            <h2 className="text-slate-600 lg:text-slate-500 font-bold text-xs uppercase tracking-widest flex items-center gap-2 min-w-0">
              <Video className="w-4 h-4 opacity-85 shrink-0 text-[#0a5482]" />
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

          <div
            className={`text-[14px] p-2 space-y-2.5 ${
              mobileCateOpen ? 'block' : 'hidden'
            } lg:block lg:max-h-[calc(100vh-8.5rem)] lg:overflow-y-auto overscroll-contain`}
          >
            {/* All Video Categories */}
            <div>
              <Link
                to="/videos"
                onClick={() => setMobileCateOpen(false)}
                className={`flex items-center gap-2.5 px-2.5 py-2.5 rounded-xl transition-all relative ${
                  !cateSlug
                    ? "bg-sky-50/95 text-[#0a5482] font-bold pl-3.5 before:content-[''] before:absolute before:left-1 before:top-2 before:bottom-2 before:w-1 before:rounded-full before:bg-[#2ab4e8]"
                    : 'text-slate-700 font-semibold hover:bg-slate-50 hover:text-[#0a5482]'
                }`}
              >
                <span
                  className={`w-7 h-7 rounded-lg flex items-center justify-center shrink-0 transition-colors ${
                    !cateSlug ? 'bg-[#0a5482] text-white shadow-xs' : 'bg-sky-50 text-[#0a5482]'
                  }`}
                >
                  <Tv className="w-3.5 h-3.5" />
                </span>
                <span className="leading-snug">{t('Video Category')}</span>
              </Link>
            </div>

            {topCategories.length === 0 ? (
              <div className="pt-2 border-t border-slate-100 px-1 space-y-2 animate-pulse">
                {[1, 2, 3, 4, 5].map((n) => (
                  <div key={n} className="h-9 rounded-xl bg-slate-100" />
                ))}
              </div>
            ) : (
              (() => {
                const isLangPractice = (vc: any) => {
                  const id = Number(vc.vc_id);
                  const key = `${vc.vc_name_url || ''} ${vc.vc_name || ''} ${vc.vc_name_vi || ''}`.toLowerCase();
                  return (
                    id === 12 ||
                    id === 61 ||
                    key.includes('audio-book') ||
                    key.includes('sách nói') ||
                    key.includes('learning-english') ||
                    key.includes('giao tiếp')
                  );
                };

                const getVideoCateIcon = (vc: any) => {
                  const id = Number(vc.vc_id);
                  const key = `${vc.vc_name_url || ''} ${vc.vc_name || ''} ${vc.vc_name_vi || ''}`.toLowerCase();
                  if (id === 12 || key.includes('audio-book') || key.includes('sách nói')) {
                    return { Icon: Headphones, idleBg: 'bg-indigo-50 text-indigo-600' };
                  }
                  if (id === 61 || key.includes('learning-english') || key.includes('giao tiếp')) {
                    return { Icon: MessageSquare, idleBg: 'bg-sky-50 text-[#0a5482]' };
                  }
                  if (id === 25 || key.includes('society') || key.includes('culture') || key.includes('văn hóa')) {
                    return { Icon: Globe, idleBg: 'bg-rose-50 text-rose-600' };
                  }
                  if (id === 22 || key.includes('science') || key.includes('khoa học')) {
                    return { Icon: Atom, idleBg: 'bg-emerald-50 text-emerald-700' };
                  }
                  if (id === 21 || key.includes('history') || key.includes('lịch sử')) {
                    return { Icon: Landmark, idleBg: 'bg-amber-50 text-amber-700' };
                  }
                  return { Icon: Film, idleBg: 'bg-slate-100 text-slate-600' };
                };

                const practiceCates = topCategories.filter(isLangPractice);
                const discoveryCates = topCategories.filter((vc) => !isLangPractice(vc));

                const renderVideoCateItem = (vc: any) => {
                  const subs = allVideoCates.filter((c) => Number(c.vc_parent) === Number(vc.vc_id));
                  const isDirectSelected = (vc.vc_name_url || '').trim() === cleanCateParam;
                  const hasActiveChild = Boolean(parentCate && Number(parentCate.vc_id) === Number(vc.vc_id));
                  const isSelected = isDirectSelected || hasActiveChild;
                  const { Icon, idleBg } = getVideoCateIcon(vc);
                  const title = lang === 'vi' ? vc.vc_name_vi || vc.vc_name : vc.vc_name;

                  return (
                    <li key={vc.vc_id}>
                      <Link
                        to={`/videos/${(vc.vc_name_url || '').trim()}`}
                        onClick={() => setMobileCateOpen(false)}
                        className={`px-2.5 py-2 rounded-xl transition-all flex items-center justify-between gap-2 relative ${
                          isDirectSelected
                            ? "bg-sky-50/95 text-[#0a5482] font-bold pl-3.5 before:content-[''] before:absolute before:left-1 before:top-2 before:bottom-2 before:w-1 before:rounded-full before:bg-[#2ab4e8]"
                            : hasActiveChild
                            ? 'text-[#0a5482] font-semibold bg-slate-50/80'
                            : 'text-slate-700 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                        }`}
                      >
                        <span className="flex items-center gap-2.5 min-w-0">
                          <span
                            className={`w-7 h-7 rounded-lg flex items-center justify-center shrink-0 transition-colors ${
                              isSelected ? 'bg-[#0a5482] text-white shadow-xs' : idleBg
                            }`}
                          >
                            <Icon className="w-3.5 h-3.5" />
                          </span>
                          <span className="leading-snug">{title}</span>
                        </span>
                        {subs.length > 0 && (
                          <span className="flex items-center gap-1 shrink-0">
                            <span
                              className={`text-[10.5px] font-extrabold px-1.5 py-0.5 rounded-md tabular-nums ${
                                isSelected
                                  ? 'bg-sky-100 text-[#0a5482]'
                                  : 'bg-slate-100 text-slate-500'
                              }`}
                            >
                              {subs.length}
                            </span>
                            <ChevronRight
                              className={`w-3.5 h-3.5 transition-transform duration-200 ${
                                isSelected ? 'rotate-90 text-[#0a5482]' : 'text-slate-400'
                              }`}
                            />
                          </span>
                        )}
                      </Link>

                      {subs.length > 0 && isSelected && (
                        <ul className="mt-1 mb-1.5 ml-5 pl-2.5 border-l-2 border-sky-100 space-y-0.5">
                          {subs.map((sub, subIdx) => {
                            const subTitle = lang === 'vi' ? sub.vc_name_vi || sub.vc_name : sub.vc_name;
                            const isActiveSub = (sub.vc_name_url || '').trim() === cleanCateParam;
                            const stepLabel = String(subIdx + 1).padStart(2, '0');
                            return (
                              <li key={sub.vc_id}>
                                <Link
                                  to={`/video/${(sub.vc_name_url || '').trim()}`}
                                  onClick={() => setMobileCateOpen(false)}
                                  className={`flex items-center gap-2 px-2.5 py-1.5 rounded-lg text-[13px] transition-all ${
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
                                  <span className="leading-snug line-clamp-2">{subTitle}</span>
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
                    {practiceCates.length > 0 && (
                      <div className="pt-2.5 border-t border-slate-100">
                        <div className="px-2.5 pb-1.5 text-[10.5px] font-extrabold uppercase tracking-widest text-slate-400">
                          {lang === 'vi' ? 'Luyện nghe & Giao tiếp' : 'Listening & Communication'}
                        </div>
                        <ul className="space-y-1">{practiceCates.map(renderVideoCateItem)}</ul>
                      </div>
                    )}

                    {discoveryCates.length > 0 && (
                      <div className="pt-2.5 border-t border-slate-100">
                        <div className="px-2.5 pb-1.5 text-[10.5px] font-extrabold uppercase tracking-widest text-slate-400">
                          {lang === 'vi' ? 'Khám phá Kiến thức' : 'Knowledge & Documentaries'}
                        </div>
                        <ul className="space-y-1">{discoveryCates.map(renderVideoCateItem)}</ul>
                      </div>
                    )}
                  </>
                );
              })()
            )}
          </div>
        </aside>

        {/* RIGHT MAIN CONTENT */}
        <div className="flex-1 min-w-0 w-full space-y-6">
          {(() => {
            const vKey = `${activeCate?.vc_name_url || ''} ${activeCate?.vc_name || ''} ${activeCate?.vc_name_vi || ''}`.toLowerCase();
            const isDiscovery =
              Boolean(activeCate) &&
              (vKey.includes('ted') ||
                vKey.includes('science') ||
                vKey.includes('khoa học') ||
                vKey.includes('discovery') ||
                vKey.includes('khám phá') ||
                vKey.includes('documentary') ||
                vKey.includes('finance') ||
                vKey.includes('business') ||
                vKey.includes('kinh'));
            const vHeader = isDiscovery
              ? {
                  stripe: 'from-amber-400 via-emerald-400 to-indigo-400',
                  bg: 'from-[#4f46e5] via-[#4338ca] to-[#0f766e]',
                  orb1: 'bg-amber-300/25',
                  orb2: 'bg-teal-300/25',
                }
              : {
                  stripe: 'from-amber-400 via-rose-500 to-fuchsia-500',
                  bg: 'from-[#be123c] via-[#9f1239] to-[#312e81]',
                  orb1: 'bg-amber-300/30',
                  orb2: 'bg-rose-400/25',
                };
            const cardAccents = [
              { pill: 'bg-rose-50 text-rose-700 border-rose-200/80', hoverText: 'group-hover:text-rose-700', arrow: 'text-rose-500' },
              { pill: 'bg-emerald-50 text-emerald-700 border-emerald-200/80', hoverText: 'group-hover:text-emerald-700', arrow: 'text-emerald-500' },
              { pill: 'bg-amber-50 text-amber-800 border-amber-200/80', hoverText: 'group-hover:text-amber-700', arrow: 'text-amber-500' },
              { pill: 'bg-indigo-50 text-indigo-700 border-indigo-200/80', hoverText: 'group-hover:text-indigo-700', arrow: 'text-indigo-500' },
            ];
            return (
          <div className="bg-white rounded-2xl sm:rounded-3xl border border-slate-200/90 shadow-sm overflow-hidden">
            {/* Vibrant Cinema Top Ribbon */}
            <div className={`h-1.5 w-full bg-gradient-to-r ${vHeader.stripe}`} />
            {/* Cinema Header */}
            <div className={`relative overflow-hidden bg-gradient-to-r ${vHeader.bg} px-4 sm:px-8 py-4 sm:py-6 text-white`}>
              <div className={`pointer-events-none absolute -top-12 -right-10 w-48 h-48 rounded-full blur-3xl ${vHeader.orb1}`} />
              <div className={`pointer-events-none absolute -bottom-12 left-1/3 w-40 h-40 rounded-full blur-3xl ${vHeader.orb2}`} />
              <div className="relative z-10">
                <div className="inline-flex items-center gap-1.5 text-[10.5px] sm:text-xs font-extrabold uppercase tracking-widest text-amber-100 bg-amber-400/20 border border-amber-200/40 px-2.5 py-0.5 rounded-full mb-1.5">
                  <span>🎬</span>
                  <span>TonyEnglish Video Channel</span>
                </div>
                <h1 className="text-xl sm:text-3xl font-black tracking-tight">{mainHeading}</h1>
              </div>
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
                    const cAccent = cardAccents[sIdx % cardAccents.length];

                    return (
                      <Link
                        key={sub.vc_id}
                        to={targetRoute}
                        className={`group bg-white rounded-2xl border border-slate-200/80 hover:border-rose-200 overflow-hidden shadow-2xs hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col ${
                          isBentoLead ? 'sm:col-span-2' : ''
                        }`}
                      >
                        <div className={`relative ${isBentoLead ? 'h-48 sm:h-52' : 'h-44'} bg-slate-800 overflow-hidden`}>
                          <img
                            src={resolveUploadUrl(imgPath)}
                            alt={subTitle}
                            loading={sIdx < 3 ? 'eager' : 'lazy'}
                            onError={(e) => {
                              const img = e.currentTarget as HTMLImageElement;
                              img.onerror = null;
                              img.src = '/uploads/No_Image_Wide.svg_1.png';
                            }}
                            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 brightness-105"
                          />
                          <div className="absolute inset-0 bg-gradient-to-t from-slate-900/50 via-transparent to-transparent pointer-events-none" />
                          <span className="absolute bottom-3 right-3 w-10 h-10 rounded-full bg-white/95 text-rose-600 flex items-center justify-center shadow-lg group-hover:scale-110 group-hover:bg-rose-600 group-hover:text-white transition-all">
                            <Play className="w-4 h-4 fill-current ml-0.5" />
                          </span>
                        </div>
                        <div className="p-4 sm:p-5 flex-1 flex flex-col justify-between gap-2.5">
                          <div className="flex items-start justify-between gap-2">
                            <h3 className={`font-extrabold text-[15px] sm:text-base text-slate-800 ${cAccent.hoverText} line-clamp-2 leading-snug transition-colors`}>
                              {subTitle}
                            </h3>
                            <ArrowRight className={`w-4 h-4 ${cAccent.arrow} shrink-0 mt-0.5 group-hover:translate-x-0.5 transition-transform`} />
                          </div>
                          {childVideos.length > 0 && (
                            <div className="flex items-center gap-1.5">
                              <span className={`inline-flex items-center gap-1 border text-[11px] font-extrabold px-2.5 py-0.5 rounded-full ${cAccent.pill}`}>
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
                  {!catesLoaded || loadingWatch ? (
                    <div className="space-y-5 animate-pulse">
                      <div className="aspect-video w-full rounded-2xl bg-slate-200" />
                      <div className="space-y-3">
                        <div className="h-7 bg-slate-200 rounded-xl w-3/4" />
                        <div className="h-4 bg-slate-100 rounded w-full" />
                        <div className="h-4 bg-slate-100 rounded w-5/6" />
                      </div>
                    </div>
                  ) : !currentVideo ? (
                    <div className="py-14 px-6 text-center rounded-2xl bg-slate-50 border border-slate-200/80 space-y-4">
                      <div className="w-14 h-14 rounded-2xl bg-sky-100 text-[#0a5482] flex items-center justify-center mx-auto">
                        <Film className="w-7 h-7" />
                      </div>
                      <div className="space-y-1.5">
                        <h2 className="text-lg sm:text-xl font-black text-slate-800">
                          {lang === 'vi' ? 'Không tìm thấy video bạn yêu cầu' : 'Video not found'}
                        </h2>
                        <p className="text-sm text-slate-500 max-w-md mx-auto">
                          {lang === 'vi'
                            ? 'Video này có thể đã được chuyển sang danh mục khác hoặc không còn tồn tại trong Kho Video.'
                            : 'This video may have been moved or is no longer available in the Video Store.'}
                        </p>
                      </div>
                      <Link
                        to="/videos"
                        className="inline-flex items-center gap-2 bg-[#0a5482] hover:bg-[#084266] text-white font-bold text-sm px-5 py-2.5 rounded-xl transition shadow-xs"
                      >
                        <span>{lang === 'vi' ? '← Quay về Kho Video' : '← Back to Video Store'}</span>
                      </Link>
                    </div>
                  ) : (
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
                            dangerouslySetInnerHTML={{
                              __html: fixLegacyHtmlContent(getLocalizedVideoComment(currentVideo, lang)),
                            }}
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
            );
          })()}

          {/* SEPARATE AIRY BLOCK FOR VIDEO LIST IN THIS CATEGORY */}
          {mode !== 'cate' && videosInCate.length > 1 && (
            <div className="bg-white/90 rounded-2xl border border-rose-200/60 px-6 py-5 sm:px-8 sm:py-6">
              <h3 className="text-xs sm:text-[13px] font-extrabold uppercase tracking-widest text-rose-700 mb-4 flex items-center gap-2">
                <Film className="w-4 h-4 text-rose-600" />
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
                        className="group bg-white hover:bg-rose-50/30 rounded-2xl border border-slate-200/70 hover:border-rose-200 overflow-hidden hover:shadow-md transition-all flex flex-col"
                      >
                        <div className="relative h-36 bg-slate-900 overflow-hidden">
                          <img
                            src={resolveUploadUrl(vd.video_thumb)}
                            alt={vd.video_desc}
                            onError={(e) => {
                              const img = e.currentTarget as HTMLImageElement;
                              img.onerror = null;
                              img.src = '/uploads/No_Image_Wide.svg_1.png';
                            }}
                            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                          />
                          <div className="absolute inset-0 bg-slate-900/20 flex items-center justify-center">
                            <span className="w-9 h-9 rounded-full bg-white/95 text-rose-600 group-hover:bg-rose-600 group-hover:text-white flex items-center justify-center text-xs shadow-md transition-colors">
                              ▶
                            </span>
                          </div>
                          {vdQuiz && (
                            <span className="absolute bottom-2 right-2 bg-amber-400 text-slate-950 text-[10.5px] font-extrabold px-2 py-0.5 rounded-md shadow-sm">
                              📝 {vdQuiz.length} {lang === 'vi' ? 'câu Quiz' : 'Qs'}
                            </span>
                          )}
                        </div>
                        <div className="p-3.5">
                          <h4 className="font-semibold text-sm sm:text-[14.5px] text-slate-600 group-hover:text-rose-700 line-clamp-2 transition-colors">
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
