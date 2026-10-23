import React, { useEffect, useRef, useState } from 'react';
import { Link, useParams, useSearchParams } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import {
  resolveUploadUrl,
  stripTags,
  fixLegacyHtmlContent,
  extractArticleVocabulary,
  parseCambridgeBilingual,
  updatePageSeo,
} from '../lib/utils';

const SPEED_OPTIONS = [0.75, 1, 1.25, 1.5];

const ArticleAudioPlayer: React.FC<{ src: string }> = ({ src }) => {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [playbackRate, setPlaybackRate] = useState(1);
  const [isMuted, setIsMuted] = useState(false);
  const [isSticky, setIsSticky] = useState(true);

  useEffect(() => {
    setIsPlaying(false);
    setCurrentTime(0);
    setDuration(0);
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.currentTime = 0;
      audioRef.current.playbackRate = playbackRate;
    }
  }, [src]);

  const formatTime = (sec: number) => {
    if (!sec || !isFinite(sec) || sec < 0) return '00:00';
    const m = Math.floor(sec / 60);
    const s = Math.floor(sec % 60);
    return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  };

  const togglePlay = () => {
    const audio = audioRef.current;
    if (!audio) return;
    if (audio.paused) {
      audio.play().catch(() => {});
    } else {
      audio.pause();
    }
  };

  const skipSeconds = (delta: number) => {
    const audio = audioRef.current;
    if (!audio) return;
    const maxDur = audio.duration && isFinite(audio.duration) ? audio.duration : duration || 0;
    const next = Math.max(0, Math.min(audio.currentTime + delta, maxDur || audio.currentTime + delta));
    audio.currentTime = next;
    setCurrentTime(next);
  };

  const handleSeek = (e: React.ChangeEvent<HTMLInputElement>) => {
    const audio = audioRef.current;
    const nextTime = parseFloat(e.target.value);
    setCurrentTime(nextTime);
    if (audio) {
      audio.currentTime = nextTime;
    }
  };

  const handleRateChange = (rate: number) => {
    setPlaybackRate(rate);
    if (audioRef.current) {
      audioRef.current.playbackRate = rate;
    }
  };

  const toggleMute = () => {
    const audio = audioRef.current;
    if (!audio) return;
    audio.muted = !isMuted;
    setIsMuted(!isMuted);
  };

  const progressPercent = duration > 0 ? Math.min(100, Math.max(0, (currentTime / duration) * 100)) : 0;

  return (
    <div
      className={`${
        isSticky ? 'sticky top-[62px] sm:top-[84px] z-30' : ''
      } bg-white/95 backdrop-blur-md border-2 border-sky-200/90 rounded-2xl p-3.5 sm:p-5 shadow-lg shadow-sky-900/5 transition-all`}
    >
      <audio
        ref={audioRef}
        src={src}
        preload="metadata"
        onTimeUpdate={() => {
          if (audioRef.current) setCurrentTime(audioRef.current.currentTime);
        }}
        onLoadedMetadata={() => {
          if (audioRef.current && isFinite(audioRef.current.duration)) {
            setDuration(audioRef.current.duration);
          }
        }}
        onDurationChange={() => {
          if (audioRef.current && isFinite(audioRef.current.duration)) {
            setDuration(audioRef.current.duration);
          }
        }}
        onPlay={() => setIsPlaying(true)}
        onPause={() => setIsPlaying(false)}
        onEnded={() => setIsPlaying(false)}
      />

      {/* Top row: Title + Skip/Play Controls + Speed/Pin */}
      <div className="flex flex-wrap items-center justify-between gap-3 mb-3.5">
        {/* Left: Audio Badge */}
        <div className="flex items-center gap-2.5 sm:gap-3">
          <span
            className={`w-10 h-10 sm:w-11 sm:h-11 rounded-xl flex items-center justify-center text-lg sm:text-xl shadow-xs transition-colors ${
              isPlaying ? 'bg-[#2ab4e8] text-white animate-pulse' : 'bg-[#0a5482] text-white'
            }`}
          >
            🎧
          </span>
          <div>
            <div className="font-black text-sm sm:text-base text-[#0a5482] leading-tight flex items-center gap-2">
              <span>Audio Luyện Nghe</span>
              {isPlaying && (
                <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[11px] font-bold bg-sky-100 text-[#0a5482]">
                  ● Đang phát
                </span>
              )}
            </div>
            <div className="text-xs text-slate-500 hidden sm:block">
              Kéo thanh trượt bên dưới hoặc bấm nút để tua nhanh và nghe cùng bài đọc
            </div>
          </div>
        </div>

        {/* Center: Play/Pause & Rewind/Forward Buttons */}
        <div className="flex items-center gap-1.5 sm:gap-2">
          <button
            type="button"
            onClick={() => skipSeconds(-10)}
            className="px-2.5 sm:px-3 py-2 rounded-xl bg-slate-100 hover:bg-sky-50 text-slate-700 hover:text-[#0a5482] border border-slate-200/80 hover:border-sky-200 font-extrabold text-xs sm:text-sm transition active:scale-95 cursor-pointer"
            title="Tua lùi 10 giây"
          >
            ⏪ -10s
          </button>
          <button
            type="button"
            onClick={() => skipSeconds(-5)}
            className="px-2.5 sm:px-3 py-2 rounded-xl bg-slate-100 hover:bg-sky-50 text-slate-700 hover:text-[#0a5482] border border-slate-200/80 hover:border-sky-200 font-extrabold text-xs sm:text-sm transition active:scale-95 cursor-pointer hidden xs:inline-flex sm:inline-flex"
            title="Tua lùi 5 giây"
          >
            -5s
          </button>

          <button
            type="button"
            onClick={togglePlay}
            className={`px-4 sm:px-6 py-2 sm:py-2.5 rounded-xl font-black text-xs sm:text-sm text-white shadow-sm transition active:scale-95 flex items-center gap-1.5 cursor-pointer ${
              isPlaying ? 'bg-amber-500 hover:bg-amber-600' : 'bg-[#0a5482] hover:bg-[#2ab4e8]'
            }`}
          >
            <span>{isPlaying ? '⏸' : '▶'}</span>
            <span>{isPlaying ? 'Tạm dừng' : 'Phát Audio'}</span>
          </button>

          <button
            type="button"
            onClick={() => skipSeconds(5)}
            className="px-2.5 sm:px-3 py-2 rounded-xl bg-slate-100 hover:bg-sky-50 text-slate-700 hover:text-[#0a5482] border border-slate-200/80 hover:border-sky-200 font-extrabold text-xs sm:text-sm transition active:scale-95 cursor-pointer hidden xs:inline-flex sm:inline-flex"
            title="Tua tới 5 giây"
          >
            +5s
          </button>
          <button
            type="button"
            onClick={() => skipSeconds(10)}
            className="px-2.5 sm:px-3 py-2 rounded-xl bg-slate-100 hover:bg-sky-50 text-slate-700 hover:text-[#0a5482] border border-slate-200/80 hover:border-sky-200 font-extrabold text-xs sm:text-sm transition active:scale-95 cursor-pointer"
            title="Tua tới 10 giây"
          >
            +10s ⏩
          </button>
        </div>

        {/* Right: Speed selector, Mute & Sticky Pin Toggle */}
        <div className="flex items-center gap-1.5 sm:gap-2 ml-auto sm:ml-0">
          <div className="inline-flex items-center bg-slate-100 p-0.5 rounded-xl border border-slate-200/80">
            {SPEED_OPTIONS.map((rate) => (
              <button
                key={rate}
                type="button"
                onClick={() => handleRateChange(rate)}
                className={`px-2 py-1 rounded-lg text-[11px] sm:text-xs font-extrabold transition cursor-pointer ${
                  playbackRate === rate
                    ? 'bg-[#0a5482] text-white shadow-2xs'
                    : 'text-slate-600 hover:text-[#0a5482]'
                }`}
                title={`Tốc độ ${rate}x`}
              >
                {rate}x
              </button>
            ))}
          </div>

          <button
            type="button"
            onClick={toggleMute}
            className="w-8 h-8 sm:w-9 sm:h-9 rounded-xl bg-slate-100 hover:bg-sky-50 border border-slate-200/80 text-slate-600 hover:text-[#0a5482] flex items-center justify-center text-sm transition cursor-pointer"
            title={isMuted ? 'Bật tiếng' : 'Tắt tiếng'}
          >
            {isMuted ? '🔇' : '🔊'}
          </button>

          <button
            type="button"
            onClick={() => setIsSticky(!isSticky)}
            className={`px-2.5 py-1.5 rounded-xl border text-xs font-bold transition cursor-pointer flex items-center gap-1 ${
              isSticky
                ? 'bg-sky-50 border-sky-200 text-[#0a5482]'
                : 'bg-slate-100 border-slate-200 text-slate-500 hover:text-slate-700'
            }`}
            title={isSticky ? 'Đang ghim chạy theo bài đọc (Bấm để bỏ ghim)' : 'Ghim thanh nghe chạy theo bài đọc'}
          >
            <span>📌</span>
            <span className="hidden md:inline">{isSticky ? 'Tự cuộn' : 'Ghim'}</span>
          </button>
        </div>
      </div>

      {/* Bottom row: Full-width Large Scrubber Bar */}
      <div className="flex items-center gap-3 sm:gap-4 w-full bg-slate-50/90 border border-slate-200/80 rounded-xl px-3 sm:px-4 py-2.5">
        <span className="text-xs sm:text-sm font-black font-mono text-[#0a5482] bg-white px-2.5 py-1 rounded-lg border border-slate-200/80 shadow-2xs shrink-0 min-w-[54px] text-center">
          {formatTime(currentTime)}
        </span>

        <div className="relative flex-1 h-7 flex items-center group">
          {/* Track background */}
          <div className="w-full h-3 sm:h-3.5 bg-slate-200 rounded-full overflow-hidden shadow-inner">
            <div
              className="h-full bg-gradient-to-r from-[#0a5482] to-[#2ab4e8] rounded-full transition-[width] duration-75"
              style={{ width: `${progressPercent}%` }}
            />
          </div>

          {/* Visible draggable thumb */}
          <div
            className="
              absolute w-5 h-5 sm:w-5.5 sm:h-5.5 bg-white border-[3px] border-[#0a5482]
              rounded-full shadow-md pointer-events-none transform -translate-x-1/2
              group-hover:scale-110 transition-transform
            "
            style={{ left: `${progressPercent}%` }}
          />

          {/* Full-width range input for smooth scrubbing */}
          <input
            type="range"
            min={0}
            max={duration > 0 ? duration : 100}
            step={0.1}
            value={currentTime}
            onChange={handleSeek}
            aria-label="Thanh tua thời gian audio"
            className="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-10"
          />
        </div>

        <span className="text-xs sm:text-sm font-black font-mono text-slate-600 bg-white px-2.5 py-1 rounded-lg border border-slate-200/80 shadow-2xs shrink-0 min-w-[54px] text-center">
          {formatTime(duration)}
        </span>
      </div>
    </div>
  );
};

export const NewsPage: React.FC<{ mode: 'list' | 'detail' }> = ({ mode }) => {
  const { slug } = useParams<{ slug?: string }>();
  const [searchParams, setSearchParams] = useSearchParams();
  const { lang, t, user } = useApp();

  const pageParam = parseInt(searchParams.get('page') || '1', 10) || 1;
  const searchQuery = searchParams.get('q') || '';

  const [allCategories, setAllCategories] = useState<any[]>([]);
  const [openParentId, setOpenParentId] = useState<number | null>(null);
  const [mobileCateOpen, setMobileCateOpen] = useState(false);

  // List view state
  const [currentCategory, setCurrentCategory] = useState<any | null>(null);
  const [newsList, setNewsList] = useState<any[]>([]);
  const [totalCount, setTotalCount] = useState(0);
  const [loading, setLoading] = useState(false);

  // Detail view state
  const [article, setArticle] = useState<any | null>(null);
  const [relatedNews, setRelatedNews] = useState<any[]>([]);
  const [showViTranslation, setShowViTranslation] = useState(false);
  const [showAudioPlayer, setShowAudioPlayer] = useState(false);
  const [showQuestion, setShowQuestion] = useState(false);
  const [showAnswer, setShowAnswer] = useState(false);
  const [showDialog, setShowDialog] = useState(false);
  const [showVocab, setShowVocab] = useState(false);
  const [camMode, setCamMode] = useState<'paragraph' | 'sentence' | 'english'>('paragraph');
  const [revealedParas, setRevealedParas] = useState<Record<number, boolean>>({});
  const [zoomImageUrl, setZoomImageUrl] = useState<string | null>(null);

  const pageSize = 10;

  useEffect(() => {
    async function loadCategories() {
      const { data } = await supabase
        .from('te_news_category')
        .select('*')
        .eq('deleted', 0)
        .eq('news_cc_status', 1)
        .order('news_cc_order_left', { ascending: true })
        .order('news_cc_id', { ascending: true });
      if (data) setAllCategories(data);
    }
    loadCategories();
  }, []);

  useEffect(() => {
    if (allCategories.length === 0) return;

    async function loadContent() {
      setLoading(true);
      const cleanSlug = decodeURIComponent(slug || '')
        .trim()
        .replace(/\.html$/i, '');

      if (mode === 'list') {
        setArticle(null);
        let targetCate: any = null;
        if (cleanSlug) {
          targetCate = allCategories.find((c) => (c.news_cc_name_url || '').trim() === cleanSlug);
        }
        setCurrentCategory(targetCate || null);

        if (targetCate) {
          setOpenParentId(targetCate.news_cc_parent === 0 ? targetCate.news_cc_id : targetCate.news_cc_parent);
          const childCates = allCategories.filter((c) => Number(c.news_cc_parent) === Number(targetCate.news_cc_id));
          const cateIds = childCates.length > 0 ? childCates.map((c) => c.news_cc_id) : [targetCate.news_cc_id];

          const isCambridgeCate =
            Number(targetCate.news_cc_id) === 38 || Number(targetCate.news_cc_parent) === 38;
          const curPageSize = isCambridgeCate ? 12 : pageSize;
          const from = (pageParam - 1) * curPageSize;
          const to = from + curPageSize - 1;

          let query = supabase
            .from('te_news')
            .select(
              'news_id,news_cc_id,news_desc,news_title,news_created_at,news_title_url,news_thumb,news_postday,news_byname,news_rank,public',
              { count: 'exact' }
            )
            .eq('deleted', 0)
            .eq('news_status', 1)
            .in('news_cc_id', cateIds);

          if (isCambridgeCate) {
            query = query
              .order('news_rank', { ascending: true, nullsFirst: false })
              .order('news_id', { ascending: true });
          } else {
            query = query.order('news_id', { ascending: false });
          }

          const { data, count } = await query.range(from, to);

          setNewsList(data || []);
          setTotalCount(count || 0);
        } else {
          const from = (pageParam - 1) * pageSize;
          const to = from + pageSize - 1;
          let query = supabase
            .from('te_news')
            .select(
              'news_id,news_cc_id,news_desc,news_title,news_created_at,news_title_url,news_thumb,news_postday,news_byname,public',
              { count: 'exact' }
            )
            .eq('deleted', 0)
            .eq('news_status', 1)
            .order('news_id', { ascending: false });

          if (searchQuery.trim()) {
            query = query.ilike('news_title', `%${searchQuery.trim()}%`);
          }

          const { data, count } = await query.range(from, to);
          setNewsList(data || []);
          setTotalCount(count || 0);
        }
      } else {
        // Detail mode
        setShowViTranslation(false);
        setShowAudioPlayer(false);
        setShowQuestion(false);
        setShowAnswer(false);
        setShowDialog(false);
        setShowVocab(false);
        setCamMode('paragraph');
        setRevealedParas({});
        setZoomImageUrl(null);

        const { data: rows } = await supabase
          .from('te_news')
          .select('*')
          .eq('deleted', 0)
          .eq('news_status', 1)
          .eq('news_title_url', cleanSlug)
          .order('news_id', { ascending: false })
          .limit(1);

        const found = rows && rows.length > 0 ? rows[0] : null;
        setArticle(found);

        if (found) {
          const cate = allCategories.find((c) => Number(c.news_cc_id) === Number(found.news_cc_id));
          setCurrentCategory(cate || null);
          if (cate) {
            setOpenParentId(cate.news_cc_parent === 0 ? cate.news_cc_id : cate.news_cc_parent);
          }

          const { data: rel } = await supabase
            .from('te_news')
            .select('news_id,news_title,news_title_url,news_byname,news_rank')
            .eq('deleted', 0)
            .eq('news_status', 1)
            .eq('news_cc_id', found.news_cc_id)
            .neq('news_id', found.news_id)
            .order('news_rank', { ascending: true, nullsFirst: false })
            .order('news_id', { ascending: false })
            .limit(11);
          setRelatedNews(rel || []);
        }
      }
      setLoading(false);
    }

    loadContent();
  }, [mode, slug, pageParam, searchQuery, allCategories]);

  const parentCategories = allCategories.filter(
    (c) => Number(c.news_cc_parent) === 0 && (Number(c.news_cc_block) === 0 || !!user)
  );
  const getSubCategories = (parentId: number) =>
    allCategories.filter((c) => Number(c.news_cc_parent) === Number(parentId));

  const cateDisplayName = currentCategory
    ? lang === 'vi'
      ? currentCategory.news_cc_name_vi || currentCategory.news_cc_name
      : currentCategory.news_cc_name
    : searchQuery
    ? `${t('Search')}: "${searchQuery}"`
    : t('Library');

  const effectivePageSize =
    currentCategory &&
    (Number(currentCategory.news_cc_id) === 38 || Number(currentCategory.news_cc_parent) === 38)
      ? 12
      : pageSize;
  const totalPages = Math.max(1, Math.ceil(totalCount / effectivePageSize));

  useEffect(() => {
    if (mode === 'detail' && article) {
      updatePageSeo(article.news_title, article.news_desc || article.news_content);
    } else {
      updatePageSeo(
        cateDisplayName,
        currentCategory
          ? lang === 'vi'
            ? currentCategory.news_cc_desc_vi || currentCategory.news_cc_desc
            : currentCategory.news_cc_desc
          : undefined
      );
    }
  }, [mode, article, cateDisplayName, currentCategory, lang]);

  const formatDate = (createdAt: number | string | undefined, postday: string | undefined) => {
    if (postday && postday.trim() !== '') return postday;
    if (!createdAt) return '';
    const d = new Date(Number(createdAt) * 1000);
    if (isNaN(d.getTime())) return '';
    return d.toLocaleDateString('en-US', { month: 'short', day: '2-digit', year: 'numeric' });
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
        <Link to="/news" className="hover:text-[#0a5482]">
          {t('Library')}
        </Link>
        {currentCategory && (
          <>
            <span>/</span>
            <Link
              to={`/news/category/${(currentCategory.news_cc_name_url || '').trim()}`}
              className="text-[#0a5482] font-bold hover:underline"
            >
              {cateDisplayName}
            </Link>
          </>
        )}
      </nav>

      <div className="flex flex-col lg:flex-row gap-4 sm:gap-8 xl:gap-12 items-start">
        {/* LEFT SIDEBAR: SUBTLE, NON-COMPETING LIBRARY MENU */}
        <aside className="w-full lg:w-[260px] xl:w-[270px] shrink-0 bg-white rounded-2xl border border-slate-200/80 shadow-2xs overflow-hidden lg:sticky lg:top-24">
          <button
            type="button"
            onClick={() => setMobileCateOpen((prev) => !prev)}
            className="w-full bg-slate-100/80 px-4 py-3 border-b border-slate-200/70 flex items-center justify-between lg:pointer-events-none cursor-pointer text-left"
          >
            <h2 className="text-slate-600 lg:text-slate-500 font-bold text-xs uppercase tracking-widest flex items-center gap-2 min-w-0">
              <span className="opacity-80 shrink-0">📚</span>
              <span className="shrink-0">{t('Library')}</span>
              {currentCategory && (
                <span className="lg:hidden font-semibold text-[#0a5482] normal-case tracking-normal truncate">
                  • {cateDisplayName}
                </span>
              )}
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

          <ul className={`divide-y divide-slate-100 text-[14.5px] p-1.5 ${mobileCateOpen ? 'block' : 'hidden'} lg:block`}>
            <li>
              <Link
                to="/news"
                onClick={() => setMobileCateOpen(false)}
                className={`block px-3.5 py-2.5 rounded-xl transition-colors ${
                  mode === 'list' && !slug
                    ? 'bg-sky-50/90 text-[#0a5482] font-semibold border-l-[3px] border-[#2ab4e8]'
                    : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                }`}
              >
                ⚡ {t('Lastest news')}
              </Link>
            </li>

            {parentCategories.map((parent) => {
              const subs = getSubCategories(parent.news_cc_id);
              const isOpen =
                openParentId === parent.news_cc_id ||
                (currentCategory &&
                  (currentCategory.news_cc_id === parent.news_cc_id ||
                    currentCategory.news_cc_parent === parent.news_cc_id));
              const pName = lang === 'vi' ? parent.news_cc_name_vi || parent.news_cc_name : parent.news_cc_name;
              const isCurrentParent = currentCategory && currentCategory.news_cc_id === parent.news_cc_id;

              return (
                <li key={parent.news_cc_id}>
                  <Link
                    to={`/news/category/${(parent.news_cc_name_url || '').trim()}`}
                    onClick={() => {
                      setOpenParentId(parent.news_cc_id);
                      if (subs.length === 0) setMobileCateOpen(false);
                    }}
                    className={`px-3.5 py-2.5 rounded-xl transition-colors flex items-center justify-between ${
                      isCurrentParent
                        ? 'bg-sky-50/90 text-[#0a5482] font-semibold border-l-[3px] border-[#2ab4e8]'
                        : isOpen
                        ? 'text-[#0a5482] font-semibold bg-slate-50/70'
                        : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                    }`}
                  >
                    <span>{pName}</span>
                    {subs.length > 0 && (
                      <span className={`text-xs transition-transform ${isOpen ? 'rotate-90 text-[#2ab4e8]' : 'text-slate-400'}`}>
                        ▸
                      </span>
                    )}
                  </Link>

                  {subs.length > 0 && isOpen && (
                    <ul className="mt-0.5 mb-1 ml-2 pl-2 border-l border-slate-200/80 space-y-0.5">
                      {subs.map((sub) => {
                        const sName = lang === 'vi' ? sub.news_cc_name_vi || sub.news_cc_name : sub.news_cc_name;
                        const isActiveSub = currentCategory && currentCategory.news_cc_id === sub.news_cc_id;
                        return (
                          <li key={sub.news_cc_id}>
                            <Link
                              to={`/news/category/${(sub.news_cc_name_url || '').trim()}`}
                              onClick={() => setMobileCateOpen(false)}
                              className={`block px-3 py-2 rounded-lg text-[13.5px] transition-all ${
                                isActiveSub
                                  ? 'bg-sky-50 text-[#0a5482] font-semibold border-l-2 border-[#2ab4e8]'
                                  : 'text-slate-500 font-normal hover:bg-slate-50 hover:text-slate-800'
                              }`}
                            >
                              {sName}
                            </Link>
                          </li>
                        );
                      })}
                    </ul>
                  )}
                </li>
              );
            })}

            <li>
              <Link
                to="/videos"
                onClick={() => setMobileCateOpen(false)}
                className="block px-3.5 py-2.5 rounded-xl font-medium text-slate-600 hover:text-[#0a5482] hover:bg-slate-50 transition-colors"
              >
                🎬 {t('Videos store')} →
              </Link>
            </li>
          </ul>
        </aside>

        {/* RIGHT MAIN CONTENT */}
        <div className="flex-1 min-w-0 w-full space-y-6">
          <div className="bg-white rounded-2xl sm:rounded-3xl border border-slate-200/90 shadow-sm">
            {/* Section Header */}
            <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] rounded-t-2xl sm:rounded-t-3xl px-4 sm:px-8 py-4 sm:py-6 text-white flex items-center justify-between flex-wrap gap-3 sm:gap-4">
              <div>
                <div className="text-[11px] sm:text-sm font-extrabold uppercase tracking-widest text-[#2ab4e8] mb-0.5 sm:mb-1">
                  TonyEnglish Learning Library
                </div>
                <h1 className="text-xl sm:text-3xl font-black tracking-tight">{cateDisplayName}</h1>
              </div>
              {mode === 'list' && totalCount > 0 && (
                <span className="bg-white/15 text-white text-xs sm:text-sm font-bold px-3 sm:px-4 py-1 sm:py-1.5 rounded-full border border-white/20">
                  {totalCount} {lang === 'vi' ? 'bài học' : 'articles'}
                </span>
              )}
            </div>

            <div className="p-4 sm:p-8">
              {loading ? (
                <div className="py-20 text-center text-slate-400 font-bold text-base">Đang tải dữ liệu...</div>
              ) : mode === 'list' ? (
                <>
                  {/* Category Description */}
                  {currentCategory &&
                    (lang === 'vi' ? currentCategory.news_cc_desc_vi : currentCategory.news_cc_desc) && (
                      <div
                        className="mb-6 p-5 bg-sky-50/70 border border-sky-100 rounded-2xl legacy-prose"
                        dangerouslySetInnerHTML={{
                          __html: fixLegacyHtmlContent(
                            lang === 'vi'
                              ? currentCategory.news_cc_desc_vi || currentCategory.news_cc_desc
                              : currentCategory.news_cc_desc
                          ),
                        }}
                      />
                    )}

                  {newsList.length > 0 ? (
                    <div className="space-y-5">
                      {newsList.map((item) => {
                        const itemUrl = `/news/view/${(item.news_title_url || '').trim()}`;
                        const isChartThumb = [59, 60, 61, 62, 73].includes(Number(item.news_cc_id));
                        return (
                          <div
                            key={item.news_id}
                            className="group bg-white hover:bg-slate-50/70 rounded-2xl border border-slate-200/80 p-4 sm:p-5 flex flex-col sm:flex-row gap-5 transition-all hover:shadow-md"
                          >
                            <Link
                              to={itemUrl}
                              className={`w-full sm:w-56 h-44 sm:h-36 rounded-xl overflow-hidden shrink-0 block ${
                                isChartThumb ? 'bg-white border border-slate-200/70 p-1.5' : 'bg-slate-100'
                              }`}
                            >
                              <img
                                src={resolveUploadUrl(item.news_thumb)}
                                alt={item.news_title}
                                onError={(e) => {
                                  (e.currentTarget as HTMLImageElement).src = '/uploads/No_Image_Wide.svg_1.png';
                                }}
                                className={`w-full h-full ${
                                  isChartThumb ? 'object-contain' : 'object-cover'
                                } group-hover:scale-105 transition-transform duration-500`}
                              />
                            </Link>

                            <div className="flex-1 flex flex-col justify-between min-w-0">
                              <div>
                                <Link
                                  to={itemUrl}
                                  className="text-lg sm:text-xl font-extrabold text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2 leading-snug mb-2"
                                >
                                  {item.news_title}
                                </Link>
                                <p className="text-slate-600 text-[15px] sm:text-base leading-relaxed line-clamp-2">
                                  {stripTags(item.news_desc).slice(0, 260)}...
                                </p>
                              </div>

                              <div className="pt-3 mt-3 border-t border-slate-100 flex items-center justify-between text-xs sm:text-sm text-slate-400">
                                <div className="flex items-center gap-2">
                                  {item.news_byname && (
                                    <span>
                                      {t('By')} <strong className="text-[#0a5482]">{item.news_byname}</strong> •
                                    </span>
                                  )}
                                  <span>{formatDate(item.news_created_at, item.news_postday)}</span>
                                </div>
                                <Link
                                  to={itemUrl}
                                  className="font-extrabold text-[#0a5482] group-hover:text-[#2ab4e8] transition-colors"
                                >
                                  {lang === 'vi' ? 'Xem bài học →' : 'Read →'}
                                </Link>
                              </div>
                            </div>
                          </div>
                        );
                      })}

                      {/* PAGINATION */}
                      {totalPages > 1 && (
                        <div className="pt-6 flex items-center justify-center gap-1.5 flex-wrap">
                          <button
                            type="button"
                            disabled={pageParam <= 1}
                            onClick={() => {
                              if (pageParam > 1) setSearchParams({ page: String(pageParam - 1) });
                            }}
                            className="px-4 py-2 rounded-xl border border-slate-200 text-sm font-bold text-slate-600 hover:bg-slate-100 disabled:opacity-40"
                          >
                            ‹ {t('Previous')}
                          </button>

                          {Array.from({ length: Math.min(10, totalPages) }, (_, idx) => {
                            const startPage = Math.max(1, Math.min(pageParam - 4, totalPages - 9));
                            const p = startPage + idx;
                            if (p > totalPages) return null;
                            return (
                              <button
                                key={p}
                                type="button"
                                onClick={() => setSearchParams({ page: String(p) })}
                                className={`w-10 h-10 rounded-xl text-sm font-black transition ${
                                  p === pageParam
                                    ? 'bg-[#0a5482] text-white shadow-sm'
                                    : 'border border-slate-200 text-slate-600 hover:bg-slate-100'
                                }`}
                              >
                                {p}
                              </button>
                            );
                          })}

                          <button
                            type="button"
                            disabled={pageParam >= totalPages}
                            onClick={() => {
                              if (pageParam < totalPages) setSearchParams({ page: String(pageParam + 1) });
                            }}
                            className="px-4 py-2 rounded-xl border border-slate-200 text-sm font-bold text-slate-600 hover:bg-slate-100 disabled:opacity-40"
                          >
                            {t('Next')} ›
                          </button>
                        </div>
                      )}
                    </div>
                  ) : (
                    <div className="py-16 text-center text-slate-500 font-bold text-base">{t('Not any news!!')}</div>
                  )}
                </>
              ) : article ? (
                /* ARTICLE DETAIL VIEW */
                <div className="space-y-6">
                  {/* Title & Meta */}
                  <div className="border-b border-slate-200 pb-5">
                    <h2 className="text-2xl sm:text-[32px] font-black text-slate-900 leading-tight mb-3">
                      {article.news_title}
                    </h2>
                    <div className="flex items-center justify-between flex-wrap gap-3 text-sm text-slate-500">
                      <div className="flex items-center gap-2">
                        {article.news_byname && (
                          <span>
                            {t('By')} <strong className="text-[#0a5482]">{article.news_byname}</strong> •
                          </span>
                        )}
                        <span>📅 {formatDate(article.news_created_at, article.news_postday)}</span>
                      </div>

                      {/* Bilingual Toggle Button (for non-Cambridge bilingual articles) */}
                      {article.news_desc_vi &&
                        article.news_desc_vi.trim() !== '' &&
                        !(article.news_content || '').includes('cambridge-bilingual') && (
                          <button
                            type="button"
                            onClick={() => setShowViTranslation(!showViTranslation)}
                            className="bg-sky-50 hover:bg-[#0a5482] text-[#0a5482] hover:text-white border border-sky-200 font-black text-sm px-4 py-2 rounded-full transition shadow-2xs"
                          >
                            🌐 {showViTranslation ? 'Xem bản Tiếng Anh (ENG)' : 'Xem bản dịch Tiếng Việt (VIE)'}
                          </button>
                        )}
                    </div>
                  </div>

                  {/* Sticky Full-Width Audio Player Box */}
                  {article.news_audio_file && article.news_audio_file.trim() !== '' && (
                    <ArticleAudioPlayer
                      key={article.news_id || article.news_audio_file}
                      src={resolveUploadUrl(article.news_audio_file, '')}
                    />
                  )}

                  {/* Lead / Intro */}
                  {article.news_desc && (
                    <div
                      className="p-5 bg-slate-50 rounded-2xl border-l-4 border-[#2ab4e8] italic font-medium text-slate-700 legacy-prose"
                      dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(article.news_desc) }}
                    />
                  )}

                  {/* Featured Image if enabled - Display full uploaded image without cropping */}
                  {article.news_thumb && Number(article.news_status_avatar) === 1 && (
                    <figure className="rounded-2xl overflow-hidden bg-white border border-slate-200/90 shadow-2xs p-2 sm:p-4 max-w-3xl mx-auto">
                      <img
                        src={resolveUploadUrl(article.news_thumb)}
                        alt={article.news_title}
                        onClick={() => setZoomImageUrl(resolveUploadUrl(article.news_thumb))}
                        onError={(e) => {
                          (e.currentTarget as HTMLImageElement).src = '/uploads/No_Image_Wide.svg_1.png';
                        }}
                        className="w-full h-auto max-h-[820px] object-contain mx-auto block cursor-zoom-in rounded-xl"
                      />
                      {article.news_desc_thumb && (
                        <figcaption className="pt-3 text-center text-sm italic text-slate-500">
                          {stripTags(article.news_desc_thumb)}
                        </figcaption>
                      )}
                    </figure>
                  )}

                  {/* Article Body (English or Vietnamese translation) & Extracted Vocabulary */}
                  {(() => {
                    const parsedEn = extractArticleVocabulary(article.news_content);
                    const cambridgeData = parseCambridgeBilingual(parsedEn.bodyHtml);
                    const parsedVi = showViTranslation ? extractArticleVocabulary(article.news_desc_vi) : null;
                    const displayBodyHtml = showViTranslation && parsedVi ? parsedVi.bodyHtml : parsedEn.bodyHtml;
                    const vocabItems = parsedEn.vocabItems;
                    const hasInteractiveBox =
                      vocabItems.length > 0 ||
                      (article.news_question && article.news_question.trim() !== '') ||
                      (article.news_conversation && article.news_conversation.trim() !== '');

                    return (
                      <>
                        {cambridgeData ? (
                          <div className="space-y-6 pt-1">
                            {/* Cambridge Bilingual Header & Reading Mode Bar */}
                            <div className="bg-slate-50/90 border border-slate-200/90 rounded-2xl p-4 sm:p-5 flex flex-col lg:flex-row lg:items-center justify-between gap-4">
                              <div>
                                {cambridgeData.titleVi && (
                                  <div className="text-base sm:text-lg font-extrabold text-[#0a5482] mb-1">
                                    🇻🇳 {cambridgeData.titleVi}
                                  </div>
                                )}
                                <p className="text-xs sm:text-sm text-slate-500">
                                  Chọn chế độ hiển thị bên phải để luyện đọc hiểu theo khổ hoặc đối chiếu từng câu
                                </p>
                              </div>

                              <div className="inline-flex bg-white p-1 rounded-xl border border-slate-200/90 shadow-2xs self-start lg:self-auto flex-wrap gap-1">
                                <button
                                  type="button"
                                  onClick={() => setCamMode('paragraph')}
                                  className={`px-3.5 py-2 rounded-lg text-xs sm:text-[13.5px] font-bold transition-all ${
                                    camMode === 'paragraph'
                                      ? 'bg-[#0a5482] text-white shadow-2xs'
                                      : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
                                  }`}
                                >
                                  📑 Dịch theo Khổ
                                </button>
                                <button
                                  type="button"
                                  onClick={() => setCamMode('sentence')}
                                  className={`px-3.5 py-2 rounded-lg text-xs sm:text-[13.5px] font-bold transition-all ${
                                    camMode === 'sentence'
                                      ? 'bg-[#0a5482] text-white shadow-2xs'
                                      : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
                                  }`}
                                >
                                  🔍 Soi từng Câu
                                </button>
                                <button
                                  type="button"
                                  onClick={() => setCamMode('english')}
                                  className={`px-3.5 py-2 rounded-lg text-xs sm:text-[13.5px] font-bold transition-all ${
                                    camMode === 'english'
                                      ? 'bg-[#0a5482] text-white shadow-2xs'
                                      : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
                                  }`}
                                >
                                  🇬🇧 Chỉ đọc Tiếng Anh
                                </button>
                              </div>
                            </div>

                            {/* Cambridge Paragraphs */}
                            <div className="space-y-5">
                              {cambridgeData.paragraphs.map((para, pIdx) => {
                                const badgeLabel = para.label || String.fromCharCode(65 + pIdx);

                                if (camMode === 'paragraph') {
                                  return (
                                    <div
                                      key={pIdx}
                                      className="rounded-2xl border border-slate-200/85 bg-white overflow-hidden shadow-2xs grid grid-cols-1 lg:grid-cols-2 divide-y lg:divide-y-0 lg:divide-x divide-slate-200/80"
                                    >
                                      {/* Left: English Paragraph */}
                                      <div className="p-5 sm:p-6">
                                        <div className="flex items-center gap-2.5 mb-3">
                                          <span className="inline-flex items-center justify-center px-2.5 py-0.5 rounded-lg bg-[#0a5482] text-white font-extrabold text-xs tracking-wide">
                                            Paragraph {badgeLabel}
                                          </span>
                                          <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
                                            English Original
                                          </span>
                                        </div>
                                        <p className="text-[16.5px] leading-[1.85] text-slate-800 text-justify font-normal">
                                          {para.enParagraph}
                                        </p>
                                      </div>

                                      {/* Right: Vietnamese Paragraph */}
                                      <div className="p-5 sm:p-6 bg-sky-50/35">
                                        <div className="flex items-center gap-2.5 mb-3">
                                          <span className="inline-flex items-center justify-center px-2.5 py-0.5 rounded-lg bg-sky-100 text-[#0a5482] font-extrabold text-xs tracking-wide">
                                            Khổ {badgeLabel}
                                          </span>
                                          <span className="text-xs font-semibold text-[#0a5482]/70 uppercase tracking-wider">
                                            Bản dịch Tiếng Việt
                                          </span>
                                        </div>
                                        <p className="text-[16px] leading-[1.85] text-slate-700 text-justify">
                                          {para.viParagraph}
                                        </p>
                                      </div>
                                    </div>
                                  );
                                }

                                if (camMode === 'sentence') {
                                  return (
                                    <div
                                      key={pIdx}
                                      className="rounded-2xl border border-slate-200/85 bg-white overflow-hidden shadow-2xs p-5 sm:p-6"
                                    >
                                      <div className="flex items-center gap-2.5 mb-4 pb-3 border-b border-slate-100">
                                        <span className="inline-flex items-center justify-center px-2.5 py-0.5 rounded-lg bg-[#0a5482] text-white font-extrabold text-xs">
                                          Khổ {badgeLabel}
                                        </span>
                                        <span className="text-xs font-semibold text-slate-400">
                                          {para.pairs.length} câu — Dịch chi tiết từng câu
                                        </span>
                                      </div>
                                      <div className="space-y-4">
                                        {para.pairs.map((pair, sIdx) => (
                                          <div
                                            key={sIdx}
                                            className="p-3.5 sm:p-4 rounded-xl bg-slate-50/70 border border-slate-200/60 space-y-1.5"
                                          >
                                            {pair.en && (
                                              <div className="text-[16px] sm:text-[16.5px] font-semibold text-[#0a5482] leading-relaxed">
                                                {pair.en}
                                              </div>
                                            )}
                                            {pair.vi && (
                                              <div className="text-[15.5px] text-slate-700 leading-relaxed pl-3 border-l-2 border-[#2ab4e8]">
                                                {pair.vi}
                                              </div>
                                            )}
                                          </div>
                                        ))}
                                      </div>
                                    </div>
                                  );
                                }

                                // camMode === 'english'
                                const isRevealed = !!revealedParas[pIdx];
                                return (
                                  <div
                                    key={pIdx}
                                    className="rounded-2xl border border-slate-200/85 bg-white overflow-hidden shadow-2xs p-5 sm:p-6 space-y-4"
                                  >
                                    <div className="flex items-center justify-between gap-2">
                                      <span className="inline-flex items-center justify-center px-2.5 py-0.5 rounded-lg bg-[#0a5482] text-white font-extrabold text-xs">
                                        Paragraph {badgeLabel}
                                      </span>
                                      <button
                                        type="button"
                                        onClick={() =>
                                          setRevealedParas((prev) => ({
                                            ...prev,
                                            [pIdx]: !prev[pIdx],
                                          }))
                                        }
                                        className="text-xs font-bold text-[#0a5482] hover:text-white bg-sky-50 hover:bg-[#0a5482] border border-sky-200 px-3 py-1 rounded-lg transition"
                                      >
                                        {isRevealed ? `Ẩn dịch khổ ${badgeLabel} ▲` : `💡 Xem dịch khổ ${badgeLabel} ▼`}
                                      </button>
                                    </div>
                                    <p className="text-[16.5px] leading-[1.85] text-slate-800 text-justify">
                                      {para.enParagraph}
                                    </p>
                                    {isRevealed && (
                                      <div className="p-4 rounded-xl bg-sky-50/60 border-l-4 border-[#2ab4e8] text-[16px] leading-[1.8] text-slate-700 text-justify">
                                        {para.viParagraph}
                                      </div>
                                    )}
                                  </div>
                                );
                              })}
                            </div>
                          </div>
                        ) : (
                          <div
                            className="legacy-prose text-justify pt-2"
                            dangerouslySetInnerHTML={{
                              __html: fixLegacyHtmlContent(displayBodyHtml),
                            }}
                          />
                        )}

                        {/* Interactive Vocabulary / Question / Answer / Conversation Dialog */}
                        {hasInteractiveBox && (
                          <div className="space-y-3 pt-5 border-t border-slate-100">
                            <div className="flex flex-wrap items-center gap-2.5">
                              {vocabItems.length > 0 && (
                                <button
                                  type="button"
                                  onClick={() => setShowVocab(!showVocab)}
                                  className={`inline-flex items-center gap-2.5 px-4 py-2 rounded-xl border text-[14.5px] font-semibold transition-all shadow-2xs group ${
                                    showVocab
                                      ? 'bg-[#0a5482] text-white border-[#0a5482]'
                                      : 'bg-slate-50/90 hover:bg-sky-50/80 text-slate-700 hover:text-[#0a5482] border-slate-200/90 hover:border-sky-200'
                                  }`}
                                >
                                  <svg
                                    className={`w-4 h-4 shrink-0 ${
                                      showVocab ? 'text-sky-200' : 'text-[#0a5482]'
                                    }`}
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                    strokeWidth={2}
                                  >
                                    <path
                                      strokeLinecap="round"
                                      strokeLinejoin="round"
                                      d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                                    />
                                  </svg>
                                  <span>
                                    Vocabulary {lang === 'vi' ? '— Từ vựng trong bài' : ''}
                                  </span>
                                  <span
                                    className={`px-2 py-0.5 rounded-md text-xs font-medium transition-colors ${
                                      showVocab
                                        ? 'bg-white/15 text-white'
                                        : 'bg-white border border-slate-200/80 text-slate-500 group-hover:border-sky-200 group-hover:text-[#0a5482]'
                                    }`}
                                  >
                                    {vocabItems.length} {lang === 'vi' ? 'từ' : 'items'}
                                  </span>
                                  <svg
                                    className={`w-4 h-4 shrink-0 transition-transform duration-200 ${
                                      showVocab
                                        ? 'rotate-180 text-sky-200'
                                        : 'text-slate-400 group-hover:text-[#0a5482]'
                                    }`}
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                    strokeWidth={2}
                                  >
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
                                  </svg>
                                </button>
                              )}

                              {article.news_question && article.news_question.trim() !== '' && (
                                <button
                                  type="button"
                                  onClick={() => {
                                    setShowQuestion(!showQuestion);
                                    if (showQuestion) setShowAnswer(false);
                                  }}
                                  className={`inline-flex items-center gap-2 px-4 py-2 rounded-xl border text-[14.5px] font-semibold transition-all shadow-2xs ${
                                    showQuestion
                                      ? 'bg-[#0a5482] text-white border-[#0a5482]'
                                      : 'bg-slate-50/90 hover:bg-sky-50/80 text-slate-700 hover:text-[#0a5482] border-slate-200/90 hover:border-sky-200'
                                  }`}
                                >
                                  <span>❓ {t('View Question')}</span>
                                  <span className="text-xs opacity-75">{showQuestion ? '▲' : '▼'}</span>
                                </button>
                              )}

                              {article.news_conversation && article.news_conversation.trim() !== '' && (
                                <button
                                  type="button"
                                  onClick={() => setShowDialog(!showDialog)}
                                  className={`inline-flex items-center gap-2 px-4 py-2 rounded-xl border text-[14.5px] font-semibold transition-all shadow-2xs ${
                                    showDialog
                                      ? 'bg-[#0a5482] text-white border-[#0a5482]'
                                      : 'bg-slate-50/90 hover:bg-sky-50/80 text-slate-700 hover:text-[#0a5482] border-slate-200/90 hover:border-sky-200'
                                  }`}
                                >
                                  <span>💬 {t('View Conversation Dialog')}</span>
                                  <span className="text-xs opacity-75">{showDialog ? '▲' : '▼'}</span>
                                </button>
                              )}
                            </div>

                            {vocabItems.length > 0 && showVocab && (
                              <div className="p-4 sm:p-5 bg-slate-50/60 rounded-2xl border border-slate-200/80">
                                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                                  {vocabItems.map((item, idx) => (
                                    <div
                                      key={idx}
                                      className="p-3.5 rounded-xl bg-white hover:bg-sky-50/30 border border-slate-200/70 transition flex items-start gap-3 shadow-2xs"
                                    >
                                      <span className="w-5 h-5 rounded-md bg-slate-100 text-slate-500 font-bold text-[11px] flex items-center justify-center shrink-0 mt-0.5">
                                        {idx + 1}
                                      </span>
                                      <div className="min-w-0 flex-1">
                                        <div className="font-bold text-[15.5px] text-[#0a5482] leading-snug">
                                          {item.term}
                                        </div>
                                        <div className="text-[14.5px] text-slate-600 leading-relaxed mt-0.5">
                                          {item.definition}
                                        </div>
                                      </div>
                                    </div>
                                  ))}
                                </div>
                              </div>
                            )}

                            {article.news_question && article.news_question.trim() !== '' && showQuestion && (
                              <div className="p-5 bg-slate-50/60 rounded-2xl border border-slate-200/80 space-y-4">
                                <div
                                  className="legacy-prose"
                                  dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(article.news_question) }}
                                />
                                {article.news_answer && article.news_answer.trim() !== '' && (
                                  <div>
                                    <button
                                      type="button"
                                      onClick={() => setShowAnswer(!showAnswer)}
                                      className="bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-sm px-4 py-2 rounded-xl transition"
                                    >
                                      ✅ {t('View Answer')}
                                    </button>
                                    {showAnswer && (
                                      <div
                                        className="mt-3 p-4 bg-emerald-50 border border-emerald-200 rounded-xl legacy-prose"
                                        dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(article.news_answer) }}
                                      />
                                    )}
                                  </div>
                                )}
                              </div>
                            )}

                            {article.news_conversation && article.news_conversation.trim() !== '' && showDialog && (
                              <div
                                className="p-5 bg-slate-50/60 rounded-2xl border border-slate-200/80 legacy-prose"
                                dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(article.news_conversation) }}
                              />
                            )}
                          </div>
                        )}
                      </>
                    );
                  })()}
                </div>
              ) : (
                <div className="py-16 text-center text-slate-500 font-bold text-base">{t('Not any news!!')}</div>
              )}
            </div>
          </div>

          {/* SEPARATE CARD FOR RELATED POSTS */}
          {!loading && mode === 'detail' && article && relatedNews.length > 0 && (
            <div className="bg-white rounded-3xl border border-slate-200/80 shadow-xs p-6 sm:p-8">
              <div className="flex items-center justify-between gap-3 pb-4 mb-5 border-b border-slate-100">
                <div className="flex items-center gap-3">
                  <span className="w-9 h-9 rounded-xl bg-sky-50 border border-sky-100 text-[#0a5482] flex items-center justify-center shrink-0">
                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.2}>
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"
                      />
                    </svg>
                  </span>
                  <div>
                    <h3 className="text-[17px] sm:text-[18.5px] font-extrabold text-slate-800 tracking-tight leading-snug">
                      {lang === 'vi' ? 'Bài đọc liên quan' : t('Related Post')}
                    </h3>
                    <p className="text-xs sm:text-[13px] text-slate-400">
                      {lang === 'vi' ? 'Các bài học khác trong cùng chuyên mục' : 'More articles in this category'}
                    </p>
                  </div>
                </div>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                {relatedNews.map((rel, idx) => (
                  <Link
                    key={rel.news_id}
                    to={`/news/view/${(rel.news_title_url || '').trim()}`}
                    className="group flex items-center justify-between gap-3 px-4 py-3.5 rounded-xl bg-slate-50/70 hover:bg-sky-50/70 border border-slate-200/70 hover:border-sky-200/90 transition-all"
                  >
                    <div className="flex items-center gap-3 min-w-0">
                      <span className="w-6 h-6 rounded-lg bg-white border border-slate-200/80 text-slate-400 group-hover:text-[#0a5482] group-hover:border-sky-200 text-xs font-bold flex items-center justify-center shrink-0 transition-colors">
                        {idx + 1}
                      </span>
                      <div className="min-w-0">
                        <span className="text-[15.5px] sm:text-[16px] font-semibold text-slate-700 group-hover:text-[#0a5482] leading-snug line-clamp-1 transition-colors block">
                          {rel.news_title}
                        </span>
                        {rel.news_byname && (
                          <span className="text-xs font-semibold text-slate-400 group-hover:text-sky-700 transition-colors block mt-0.5">
                            {rel.news_byname}
                          </span>
                        )}
                      </div>
                    </div>
                    <svg
                      className="w-4 h-4 text-slate-300 group-hover:text-[#0a5482] group-hover:translate-x-0.5 transition-all shrink-0"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      strokeWidth={2}
                    >
                      <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
                    </svg>
                  </Link>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Full Image Lightbox Modal */}
      {zoomImageUrl && (
        <div
          className="fixed inset-0 z-50 bg-slate-900/80 backdrop-blur-xs flex items-center justify-center p-4 cursor-zoom-out"
          onClick={() => setZoomImageUrl(null)}
        >
          <div className="relative max-w-5xl max-h-[92vh] bg-white rounded-2xl p-2 sm:p-4 shadow-2xl overflow-auto">
            <button
              type="button"
              onClick={() => setZoomImageUrl(null)}
              className="absolute top-3 right-3 w-9 h-9 rounded-full bg-slate-900/75 hover:bg-[#0a5482] text-white font-bold flex items-center justify-center shadow-md transition-colors cursor-pointer"
              aria-label="Close zoom"
            >
              ✕
            </button>
            <img
              src={zoomImageUrl}
              alt={article?.news_title || 'Full view'}
              className="max-w-full max-h-[85vh] w-auto h-auto object-contain mx-auto block rounded-lg"
            />
          </div>
        </div>
      )}
    </div>
  );
};
