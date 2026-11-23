import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import {
  GraduationCap,
  Target,
  BookOpen,
  Video,
  Bot,
  Sparkles,
  CheckCircle2,
  ArrowRight,
  Calendar,
  MessageCircle,
  Globe,
  Layers,
  Award,
  MapPin,
  ChevronLeft,
  ChevronRight,
  Phone,
} from 'lucide-react';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import {
  resolveUploadUrl,
  truncateWords,
  stripTags,
  getYoutubeEmbedUrl,
  fixLegacyHtmlContent,
  updatePageSeo,
} from '../lib/utils';
import { trackUnifiedContact } from '../../lib/googleAnalytics';

type CardVariant = 'default' | 'horizontal' | 'compact';

function normalizeInternalLink(rawUrl: string | null | undefined, fallback = '/courses'): string {
  if (!rawUrl || !rawUrl.trim()) return fallback;
  const cleaned = rawUrl
    .trim()
    .replace(/^https?:\/\/(?:www\.)?tonyenglish\.vn/i, '')
    .replace(/^\/(?:vi|en)(?=\/|$)/i, '')
    .replace(/\/news\/index$/i, '/news')
    .replace(/\.html$/i, '');
  if (!cleaned) return fallback;
  return cleaned.startsWith('/') ? cleaned : `/${cleaned}`;
}

function getBalancedGridClass(count: number): string {
  if (count <= 1) return 'grid grid-cols-1 gap-6';
  const mobileSnap =
    'flex sm:grid overflow-x-auto sm:overflow-visible snap-x snap-mandatory pb-2 sm:pb-0 -mx-4 px-4 sm:mx-0 sm:px-0 custom-scrollbar [&>*]:w-[84vw] [&>*]:max-w-[340px] [&>*]:shrink-0 sm:[&>*]:w-auto sm:[&>*]:max-w-none sm:[&>*]:shrink [&>*]:snap-start';
  if (count === 2) return `${mobileSnap} sm:grid-cols-1 lg:grid-cols-2 gap-4 sm:gap-6`;
  if (count === 4) return `${mobileSnap} sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-5`;
  return `${mobileSnap} sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6`;
}

function getCardVariantForCount(count: number): CardVariant {
  if (count === 1 || count === 2) return 'horizontal';
  if (count === 4) return 'compact';
  return 'default';
}

interface ParsedTestimonial {
  badge: string;
  headline: string;
  summary: string;
  imageUrl: string | null;
  isDiagram: boolean;
  linkUrl: string;
  ctaLabel: string;
  useStructuredCard: boolean;
}

function parseTestimonialCard(
  testValue: any,
  lang: 'vi' | 'en',
  idx: number
): ParsedTestimonial {
  const rawTitle = (
    lang === 'vi'
      ? testValue.testimonial_title_vi || testValue.testimonial_title_en
      : testValue.testimonial_title_en || testValue.testimonial_title_vi
  )?.trim() || '';

  const rawHtml =
    (lang === 'vi'
      ? testValue.testimonial_content_vi || testValue.testimonial_content_en
      : testValue.testimonial_content_en || testValue.testimonial_content_vi) || '';

  const imgMatch = rawHtml.match(/<img\b[^>]*\bsrc=["']([^"']+)["'][^>]*>/i);
  const imageUrl = imgMatch?.[1] ? resolveUploadUrl(imgMatch[1]) : null;
  const isDiagram = Boolean(
    imageUrl &&
      (idx === 0 ||
        /\.(png|svg)(?:\?|$)/i.test(imageUrl) ||
        /(venn|blended|diagram|chart|method|hoc-tai)/i.test(imageUrl))
  );

  const linkMatch = rawHtml.match(/<a\b[^>]*\bhref=["']([^"']+)["'][^>]*>/i);
  const linkUrl = normalizeInternalLink(linkMatch?.[1], idx === 0 ? '/courses' : '/news');

  const plainText = stripTags(rawHtml);
  let headline = rawTitle;
  let summary = plainText;

  const colonIdx = plainText.indexOf(':');
  if (colonIdx > 5 && colonIdx <= 70) {
    headline = plainText.slice(0, colonIdx).trim();
    summary = plainText.slice(colonIdx + 1).trim();
  } else if (!headline) {
    headline =
      idx === 0
        ? lang === 'vi'
          ? 'Học trên lớp + Tài khoản Online'
          : 'Blended 1-on-1 & Online Portal'
        : lang === 'vi'
        ? 'Thư viện học liệu & Kho Video'
        : 'Library & Curated Video Store';
  }

  const badge =
    rawTitle ||
    (idx === 0
      ? lang === 'vi'
        ? 'Học tại TonyEnglish'
        : 'Study at TonyEnglish'
      : lang === 'vi'
      ? 'Thư viện & Kho Video'
      : 'Library & Video Hub');

  const ctaLabel = linkUrl.includes('/courses')
    ? lang === 'vi'
      ? 'Xem các khóa học'
      : 'Explore courses'
    : linkUrl.includes('/video')
    ? lang === 'vi'
      ? 'Mở Kho Video'
      : 'Explore videos'
    : lang === 'vi'
    ? 'Khám phá Thư viện'
    : 'Explore library';

  const useStructuredCard = Boolean(imageUrl && summary.length > 20 && !/<table\b|<iframe\b/i.test(rawHtml));

  return {
    badge,
    headline,
    summary,
    imageUrl,
    isDiagram,
    linkUrl,
    ctaLabel,
    useStructuredCard,
  };
}

export const HomePage: React.FC = () => {
  const { lang, t } = useApp();

  useEffect(() => {
    updatePageSeo(
      '',
      'TonyEnglish.vn - Lớp gia sư 1 kèm 1 trực tiếp cùng Thầy Tony (7 năm tu nghiệp UK) tại nhà riêng R2B 2219 Royal City & Online: IELTS, Cambridge IGCSE / A-Level, Digital SAT 1500+ & Giao tiếp. Học thử miễn phí 2-3 buổi. Zalo/Hotline: 0935 058 688.',
      { canonicalPath: '/', image: '/images/courses/course-overview.jpg' }
    );
  }, []);

  const [ads, setAds] = useState<any[]>([]);
  const [adsLoaded, setAdsLoaded] = useState(false);
  const [bannerIdx, setBannerIdx] = useState(0);

  const [stickyNews, setStickyNews] = useState<any[]>([]);
  const [stickyIdx, setStickyIdx] = useState(0);

  const [newsCategories, setNewsCategories] = useState<any[]>([]);
  const [latestNewsByCate, setLatestNewsByCate] = useState<Record<number, any>>({});

  const [videoFocus, setVideoFocus] = useState<any | null>(null);
  const [videoEvent, setVideoEvent] = useState<any | null>(null);
  const [allVideoCategories, setAllVideoCategories] = useState<any[]>([]);
  const [videoSlideIdx, setVideoSlideIdx] = useState(0);

  const [testimonials, setTestimonials] = useState<any[]>([]);
  const [popupVideo, setPopupVideo] = useState<any | null>(null);

  useEffect(() => {
    async function fetchHomeData() {
      try {
        const [adsRes, stickyRes, newsCateRes, vFocusRes, vEventRes, vCateRes, testiRes] = await Promise.all([
          supabase
            .from('te_ads')
            .select('*')
            .eq('deleted', 0)
            .eq('status', 1)
            .eq('ad_type', 6)
            .order('rank', { ascending: true })
            .limit(10),
          supabase
            .from('te_news')
            .select('news_id,news_cc_id,news_title,news_title_url,news_thumb,news_desc')
            .eq('deleted', 0)
            .eq('news_status', 1)
            .eq('news_stick', 1)
            .order('news_id', { ascending: false })
            .limit(10),
          supabase
            .from('te_news_category')
            .select(
              'news_cc_id,news_cc_parent,news_cc_name,news_cc_name_vi,news_cc_name_url,news_cc_thumb,news_cc_desc,news_cc_focus,news_cc_order'
            )
            .eq('deleted', 0)
            .eq('news_cc_status', 1)
            .order('news_cc_order', { ascending: true }),
          supabase
            .from('te_video')
            .select('*')
            .eq('deleted', 0)
            .eq('video_status', 1)
            .eq('video_focus', 1)
            .limit(10),
          supabase
            .from('te_video')
            .select('*')
            .eq('deleted', 0)
            .eq('video_status', 1)
            .eq('video_focus', 2)
            .limit(10),
          supabase
            .from('te_video_category')
            .select('*')
            .eq('deleted', 0)
            .eq('vc_status', 1)
            .order('vc_order', { ascending: true }),
          supabase
            .from('te_testimonial')
            .select('*')
            .eq('deleted', 0)
            .eq('testimonial_status', 1)
            .order('testimonial_order', { ascending: true }),
        ]);

        if (adsRes.data) setAds(adsRes.data);
        setAdsLoaded(true);
        if (stickyRes.data) setStickyNews(stickyRes.data);

        if (newsCateRes.data) {
          setNewsCategories(newsCateRes.data);
          const focusCates = newsCateRes.data.filter((c: any) =>
            [0, 1, 2, 3, 4, 5].includes(Number(c.news_cc_focus))
          );
          const targetCateIds = new Set<number>();
          const parentMap: Record<number, number> = {};

          for (const fc of focusCates) {
            const fcId = Number(fc.news_cc_id);
            targetCateIds.add(fcId);
            for (const ch of newsCateRes.data) {
              if (Number(ch.news_cc_parent) === fcId) {
                targetCateIds.add(Number(ch.news_cc_id));
                parentMap[Number(ch.news_cc_id)] = fcId;
              }
            }
          }

          if (targetCateIds.size > 0) {
            const { data: homeNews } = await supabase
              .from('te_news')
              .select('news_id,news_cc_id,news_title,news_title_url,news_thumb,news_desc')
              .eq('deleted', 0)
              .eq('news_status', 1)
              .in('news_cc_id', Array.from(targetCateIds))
              .order('news_id', { ascending: false })
              .limit(300);

            if (homeNews) {
              const stickyIdSet = new Set((stickyRes.data || []).map((s: any) => s.news_id));
              const byCate: Record<number, any[]> = {};

              for (const item of homeNews) {
                if (stickyIdSet.has(item.news_id)) continue;
                const cid = Number(item.news_cc_id);
                const pid = parentMap[cid];
                if (!byCate[cid]) byCate[cid] = [];
                byCate[cid].push(item);
                if (pid) {
                  if (!byCate[pid]) byCate[pid] = [];
                  byCate[pid].push(item);
                }
              }

              const chosenMap: Record<number, any> = {};
              for (const fc of focusCates) {
                const cid = Number(fc.news_cc_id);
                const candidates = byCate[cid] || [];
                if (candidates.length > 0) {
                  const withThumb = candidates.find((n) => n.news_thumb && n.news_thumb.trim() !== '');
                  chosenMap[cid] = withThumb || candidates[0];
                }
              }
              setLatestNewsByCate(chosenMap);
            }
          }
        }

        if (vFocusRes.data && vFocusRes.data.length > 0) {
          const rnd = Math.floor(Math.random() * vFocusRes.data.length);
          setVideoFocus(vFocusRes.data[rnd]);
        }
        if (vEventRes.data && vEventRes.data.length > 0) {
          const rnd = Math.floor(Math.random() * vEventRes.data.length);
          setVideoEvent(vEventRes.data[rnd]);
        }
        if (vCateRes.data) setAllVideoCategories(vCateRes.data);
        if (testiRes.data) setTestimonials(testiRes.data);
      } catch (err) {
        console.warn('Home data fetch warning:', err);
      } finally {
        setAdsLoaded(true);
      }
    }

    fetchHomeData();
  }, []);

  // Auto-advance top banner, sticky news, and video category slides
  useEffect(() => {
    const timer = setInterval(() => {
      if (ads.length > 1) setBannerIdx((prev) => (prev + 1) % ads.length);
      if (stickyNews.length > 1) setStickyIdx((prev) => (prev + 1) % stickyNews.length);
      setVideoSlideIdx((prev) => prev + 1);
    }, 6000);
    return () => clearInterval(timer);
  }, [ads.length, stickyNews.length]);

  const testiPos0 = testimonials.filter((tItem) => Number(tItem.testimonial_position) === 0);
  const testiPos1 = testimonials.filter((tItem) => Number(tItem.testimonial_position) === 1);
  const allTestimonials = [...testiPos0, ...testiPos1];

  const videoCateMap: Record<number, any> = {};
  allVideoCategories.forEach((vc) => {
    videoCateMap[vc.vc_id] = vc;
  });

  // Render a single modern news category card (supports default, horizontal 2-up, and compact 4-up layouts)
  const renderNewsCateCard = (cate: any, variant: CardVariant = 'default') => {
    const newsItem = latestNewsByCate[cate.news_cc_id];
    if (!newsItem) return null;

    const cateTitle = lang === 'vi' ? cate.news_cc_name_vi || cate.news_cc_name : cate.news_cc_name;
    const cateUrl = `/news/category/${(cate.news_cc_name_url || '').trim()}`;
    const articleUrl = `/news/view/${(newsItem.news_title_url || '').trim()}`;
    const rawTitle = (newsItem.news_title || '').trim();
    const thumbSrc = resolveUploadUrl(newsItem.news_thumb);

    if (variant === 'horizontal') {
      return (
        <div
          key={cate.news_cc_id}
          className="group bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden flex flex-col sm:flex-row h-full"
        >
          <div className="relative h-48 sm:h-auto sm:w-52 md:w-56 sm:min-h-[216px] shrink-0 overflow-hidden bg-slate-100">
            <Link to={articleUrl} className="block w-full h-full">
              {thumbSrc && (
                <img
                  src={thumbSrc}
                  alt={rawTitle}
                  onError={(e) => {
                    const img = e.currentTarget as HTMLImageElement;
                    img.onerror = null;
                    img.src = '/uploads/No_Image_Wide.svg_1.png';
                  }}
                  className="w-full h-full object-cover object-[50%_20%] group-hover:scale-105 transition-transform duration-500"
                />
              )}
            </Link>
            <Link
              to={cateUrl}
              className="absolute top-3 left-3 bg-[#0a5482]/90 backdrop-blur-xs text-white text-[11px] font-extrabold px-3 py-1 rounded-full shadow-md hover:bg-[#2ab4e8] transition-colors"
            >
              {cateTitle}
            </Link>
          </div>

          <div className="p-5 flex-1 flex flex-col justify-between min-w-0">
            <div>
              <Link
                to={articleUrl}
                className="font-extrabold text-[17px] text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2 leading-snug mb-2 block"
              >
                {rawTitle}
              </Link>
              <p className="text-slate-600 text-[14.5px] leading-relaxed line-clamp-3">
                {truncateWords(newsItem.news_desc, 165)}
              </p>
            </div>

            <div className="pt-3.5 mt-4 border-t border-slate-100 flex items-center justify-between gap-2">
              <Link
                to={cateUrl}
                className="text-xs sm:text-sm font-extrabold text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1 transition-colors"
              >
                <span>{t('Related Post')}</span>
                <span>→</span>
              </Link>
              <Link
                to={articleUrl}
                className="text-xs sm:text-sm font-bold text-slate-500 hover:text-slate-800 transition-colors"
              >
                {lang === 'vi' ? 'Đọc tiếp' : 'Read more'}
              </Link>
            </div>
          </div>
        </div>
      );
    }

    const isCompact = variant === 'compact';

    return (
      <div
        key={cate.news_cc_id}
        className="group bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden flex flex-col h-full"
      >
        <div className={`relative ${isCompact ? 'h-44' : 'h-48'} overflow-hidden bg-slate-100`}>
          <Link to={articleUrl} className="block w-full h-full">
            {thumbSrc && (
              <img
                src={thumbSrc}
                alt={rawTitle}
                onError={(e) => {
                  const img = e.currentTarget as HTMLImageElement;
                  img.onerror = null;
                  img.src = '/uploads/No_Image_Wide.svg_1.png';
                }}
                className="w-full h-full object-cover object-[50%_20%] group-hover:scale-105 transition-transform duration-500"
              />
            )}
          </Link>
          <Link
            to={cateUrl}
            className="absolute top-3 left-3 max-w-[calc(100%-24px)] truncate bg-[#0a5482]/90 backdrop-blur-xs text-white text-[11px] font-extrabold px-2.5 py-1 rounded-full shadow-md hover:bg-[#2ab4e8] transition-colors"
          >
            {cateTitle}
          </Link>
        </div>

        <div className={`${isCompact ? 'p-4' : 'p-5'} flex-1 flex flex-col justify-between`}>
          <div>
            <Link
              to={articleUrl}
              className={`font-extrabold ${
                isCompact ? 'text-[15.5px]' : 'text-[17px] sm:text-[18px]'
              } text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2 leading-snug mb-2 block`}
            >
              {rawTitle}
            </Link>
            <p className={`text-slate-600 ${isCompact ? 'text-[13.5px]' : 'text-[15px]'} leading-relaxed line-clamp-3`}>
              {truncateWords(newsItem.news_desc, isCompact ? 130 : 165)}
            </p>
          </div>

          <div className={`${isCompact ? 'pt-3 mt-3.5' : 'pt-4 mt-4'} border-t border-slate-100 flex items-center justify-between gap-2`}>
            <Link
              to={cateUrl}
              className={`${isCompact ? 'text-xs' : 'text-sm'} font-extrabold text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1 transition-colors`}
            >
              <span>{t('Related Post')}</span>
              <span>→</span>
            </Link>
            <Link
              to={articleUrl}
              className={`${isCompact ? 'text-xs' : 'text-sm'} font-bold text-slate-500 hover:text-slate-800 transition-colors`}
            >
              {lang === 'vi' ? 'Đọc tiếp' : 'Read more'}
            </Link>
          </div>
        </div>
      </div>
    );
  };

  // Render a focus section with adaptive column count so there are never orphan cards or empty right columns
  const renderCategorySection = (focusType: number, sectionTitleKey: string, icon: React.ReactNode) => {
    const matchedCates = newsCategories.filter(
      (nc) => Number(nc.news_cc_focus) === focusType && !!latestNewsByCate[nc.news_cc_id]
    );
    const includeVideoEvent = focusType === 5 && Boolean(videoEvent);
    const totalCount = matchedCates.length + (includeVideoEvent ? 1 : 0);
    if (totalCount === 0) return null;

    const variant = getCardVariantForCount(totalCount);
    const gridClass = getBalancedGridClass(totalCount);
    const cards: React.ReactNode[] = [];

    if (includeVideoEvent && videoEvent) {
      const vCateUrl = videoCateMap[videoEvent.vc_id]
        ? `/video/${(videoCateMap[videoEvent.vc_id].vc_name_url || '').trim()}/${(videoEvent.video_url || '').trim()}`
        : '/videos';
      const isHorizontal = variant === 'horizontal';
      const isCompact = variant === 'compact';
      const videoEventThumb = resolveUploadUrl(videoEvent.video_thumb);

      cards.push(
        <div
          key={`video-event-${focusType}`}
          className={`group bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden flex ${
            isHorizontal ? 'flex-col sm:flex-row' : 'flex-col'
          } h-full`}
        >
          <div
            className={`relative overflow-hidden bg-slate-100 ${
              isHorizontal ? 'h-48 sm:h-auto sm:w-52 md:w-56 sm:min-h-[216px] shrink-0' : isCompact ? 'h-44' : 'h-48'
            }`}
          >
            <Link to={vCateUrl} className="block w-full h-full">
              {videoEventThumb && (
                <img
                  src={videoEventThumb}
                  alt={videoEvent.video_desc}
                  onError={(e) => {
                    const img = e.currentTarget as HTMLImageElement;
                    img.onerror = null;
                    img.src = '/uploads/No_Image_Wide.svg_1.png';
                  }}
                  className="w-full h-full object-cover object-[50%_20%] group-hover:scale-105 transition-transform duration-500"
                />
              )}
            </Link>
            <span className="absolute top-3 left-3 bg-rose-600 text-white text-xs font-extrabold px-3 py-1 rounded-full shadow-md">
              🎬 {t('Video')}
            </span>
          </div>
          <div className={`${isCompact ? 'p-4' : 'p-5'} flex-1 flex flex-col justify-between min-w-0`}>
            <div>
              <Link
                to={vCateUrl}
                className={`font-extrabold ${
                  isCompact ? 'text-[15.5px]' : 'text-[17px]'
                } text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2 leading-snug mb-2 block`}
              >
                {truncateWords(videoEvent.video_desc, 120)}
              </Link>
              <p className={`text-slate-600 ${isCompact ? 'text-[13.5px]' : 'text-[14.5px]'} leading-relaxed line-clamp-3`}>
                {truncateWords(videoEvent.video_cmt, isCompact ? 130 : 180)}
              </p>
            </div>
            <div className={`${isCompact ? 'pt-3 mt-3.5' : 'pt-4 mt-4'} border-t border-slate-100`}>
              <Link
                to={vCateUrl}
                className={`${isCompact ? 'text-xs' : 'text-sm'} font-extrabold text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1`}
              >
                <span>{t('Related Post')}</span>
                <span>→</span>
              </Link>
            </div>
          </div>
        </div>
      );
    }

    matchedCates.forEach((nc) => {
      const card = renderNewsCateCard(nc, variant);
      if (card) cards.push(card);
    });

    if (cards.length === 0) return null;

    return (
      <section className="space-y-5">
        <div className="flex items-center justify-between gap-3 border-b border-slate-200 pb-3">
          <div className="flex items-center gap-2.5 min-w-0">
            <span className="w-9 h-9 rounded-xl bg-sky-100 text-[#0a5482] flex items-center justify-center text-lg shadow-2xs shrink-0">
              {icon}
            </span>
            <h2 className="text-lg sm:text-2xl font-black text-slate-800 tracking-tight leading-snug">
              {t(sectionTitleKey)}
            </h2>
          </div>
          <Link
            to="/news"
            className="text-xs sm:text-sm font-bold text-[#0a5482] hover:text-[#2ab4e8] transition-colors whitespace-nowrap shrink-0"
          >
            {lang === 'vi' ? 'Xem tất cả →' : 'View all →'}
          </Link>
        </div>
        <div className={gridClass}>{cards}</div>
      </section>
    );
  };

  const fixHeroCopyTypos = (text: string) =>
    text.replace(/\bhộ trợ\b/gi, (m) => (m[0] === 'H' ? 'Hỗ trợ' : 'hỗ trợ'));

  const curAd = ads[bannerIdx];
  const curAdLink = curAd ? normalizeInternalLink(curAd.link, '/courses') : '/courses';
  const curAdMetaText = curAd
    ? fixHeroCopyTypos(stripTags(lang === 'vi' ? curAd.meta_vi || curAd.meta : curAd.meta || curAd.meta_vi))
    : '';
  const curAdDescText = curAd
    ? fixHeroCopyTypos(stripTags(lang === 'vi' ? curAd.desc_vi || curAd.desc : curAd.desc || curAd.desc_vi))
    : '';
  const showDistinctAdDesc =
    Boolean(curAdDescText) &&
    curAdDescText.toLowerCase() !== curAdMetaText.toLowerCase() &&
    !curAdMetaText.toLowerCase().includes(curAdDescText.toLowerCase());

  const curSticky = stickyNews[stickyIdx];
  const featuredVideoParents = allVideoCategories.filter((vc) => Number(vc.vc_type) === 1);
  const videoStoreVariant = getCardVariantForCount(featuredVideoParents.length);
  const videoStoreGridClass = getBalancedGridClass(featuredVideoParents.length);

  const focusZeroCates = newsCategories.filter(
    (nc) => Number(nc.news_cc_focus) === 0 && !!latestNewsByCate[nc.news_cc_id]
  );

  return (
    <div className="pb-2">
      {/* 1. MODERN EDTECH FLAGSHIP HERO + DYNAMIC SHOWCASE */}
      <section className="relative overflow-hidden bg-gradient-to-br from-[#06283d] via-[#0a5482] to-[#0f172a] text-white pt-7 pb-14 sm:pt-9 sm:pb-16 lg:pt-10 lg:pb-20 border-b border-slate-800/60">
        {/* Ambient Decorative Glows */}
        <div className="absolute -top-32 -left-24 w-96 h-96 bg-[#2ab4e8]/20 blur-3xl rounded-full pointer-events-none" />
        <div className="absolute -bottom-32 right-0 w-[28rem] h-[28rem] bg-amber-400/10 blur-3xl rounded-full pointer-events-none" />

        <div className="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-7 lg:gap-9 items-stretch">
            {/* Left Value Proposition (7 cols) */}
            <div className="lg:col-span-7 flex flex-col justify-between space-y-4 sm:space-y-5">
              <div className="space-y-4">
                <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/15 px-3.5 py-1.5 rounded-full text-xs font-bold text-sky-200">
                  <MapPin className="w-3.5 h-3.5 text-[#2ab4e8] shrink-0" />
                  <span>
                    {lang === 'vi'
                      ? 'Gia sư 1 kèm 1 & Nhóm nhỏ • R2B Royal City, Hà Nội & Online'
                      : '1-on-1 & Small Group Tutoring • Royal City Hanoi & Online'}
                  </span>
                </div>

                <h1 className="font-display font-black text-[26px] sm:text-[33px] xl:text-[38px] leading-[1.18] tracking-tight text-white">
                  {lang === 'vi' ? (
                    <>
                      Chinh phục <span className="text-[#2ab4e8]">IELTS</span>,{' '}
                      <span className="text-amber-300">Cambridge IGCSE</span> &amp; Giao tiếp thực chiến{' '}
                      <span className="whitespace-nowrap">cùng Thầy Tony</span>
                    </>
                  ) : (
                    <>
                      Master <span className="text-[#2ab4e8]">IELTS</span>,{' '}
                      <span className="text-amber-300">Cambridge IGCSE</span> &amp; Real-World English{' '}
                      <span className="whitespace-nowrap">with Teacher Tony</span>
                    </>
                  )}
                </h1>

                <p className="text-slate-200/90 text-[14.5px] sm:text-[15.5px] leading-relaxed max-w-2xl">
                  {lang === 'vi'
                    ? 'Kết hợp sự kèm cặp sát sao từng buổi của Thầy Tony với Hệ sinh thái Phòng học thông minh: Bài giảng song ngữ bám sát Syllabus, Kho đề Past Papers kèm Video chữa bài Full HD & Phòng thi AI chấm chữa 24/7.'
                    : 'Combining personalized 1-on-1 mentoring with an AI-powered Learning Portal: Bilingual syllabus lectures, Full HD past-paper video walkthroughs, and 24/7 AI exam grading.'}
                </p>

                {/* Primary & Secondary CTAs (Single Clean Row on Desktop) */}
                <div className="pt-1 flex flex-wrap items-center gap-3">
                  <button
                    type="button"
                    onClick={() => window.dispatchEvent(new CustomEvent('tony-open-lms', { detail: 'register' }))}
                    className="bg-gradient-to-r from-amber-400 via-yellow-400 to-amber-500 hover:from-amber-500 hover:to-yellow-500 text-slate-950 font-extrabold text-sm sm:text-[15px] px-5 sm:px-6 py-3 rounded-2xl shadow-lg transition-all active:scale-95 inline-flex items-center gap-2 cursor-pointer whitespace-nowrap"
                  >
                    <Sparkles className="w-4 h-4 shrink-0" />
                    <span>{lang === 'vi' ? 'Vào Học Thử & Làm Đề Ngay' : 'Start Free Trial Now'}</span>
                    <ArrowRight className="w-4 h-4 shrink-0" />
                  </button>

                  <Link
                    to="/courses"
                    className="bg-white/12 hover:bg-white/22 text-white border border-white/25 font-bold text-sm sm:text-[15px] px-5 py-3 rounded-2xl backdrop-blur-xs transition-all active:scale-95 inline-flex items-center gap-2 whitespace-nowrap"
                  >
                    <BookOpen className="w-4 h-4 text-[#2ab4e8] shrink-0" />
                    <span>{lang === 'vi' ? 'Các Khóa Học' : 'Explore Courses'}</span>
                  </Link>

                  <a
                    href="https://zalo.me/0935058688"
                    target="_blank"
                    rel="noreferrer"
                    onClick={() => trackUnifiedContact('Zalo', 'HomePage_Hero_Mobile')}
                    className="md:hidden inline-flex items-center gap-1.5 text-xs font-bold text-sky-200 hover:text-white bg-white/10 border border-white/15 px-3.5 py-2.5 rounded-xl transition-colors"
                  >
                    <MessageCircle className="w-3.5 h-3.5 text-[#2ab4e8]" />
                    <span>Zalo: 0935 058 688</span>
                  </a>
                </div>
              </div>

              {/* 4 Key Proof Metrics (Uniform 1-line subtitle for clean horizontal alignment) */}
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 sm:gap-3 pt-1">
                <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-2xl px-3.5 py-2.5">
                  <div className="font-display font-black text-[17px] sm:text-lg text-white leading-tight">2013–2026</div>
                  <div className="text-[11px] sm:text-xs text-sky-200/85 font-medium mt-0.5 truncate">
                    {lang === 'vi' ? '13+ năm giảng dạy' : '13+ years teaching'}
                  </div>
                </div>
                <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-2xl px-3.5 py-2.5">
                  <div className="font-display font-black text-[17px] sm:text-lg text-[#2ab4e8] leading-tight">6.5 – 8.0+</div>
                  <div className="text-[11px] sm:text-xs text-sky-200/85 font-medium mt-0.5 truncate">
                    {lang === 'vi' ? 'Mục tiêu IELTS' : 'IELTS Band Target'}
                  </div>
                </div>
                <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-2xl px-3.5 py-2.5">
                  <div className="font-display font-black text-[17px] sm:text-lg text-amber-300 leading-tight">A / A*</div>
                  <div className="text-[11px] sm:text-xs text-sky-200/85 font-medium mt-0.5 truncate">
                    {lang === 'vi' ? 'Cambridge IGCSE' : 'Cambridge IGCSE'}
                  </div>
                </div>
                <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-2xl px-3.5 py-2.5">
                  <div className="font-display font-black text-[17px] sm:text-lg text-emerald-300 leading-tight">Full HD + AI</div>
                  <div className="text-[11px] sm:text-xs text-sky-200/85 font-medium mt-0.5 truncate">
                    {lang === 'vi' ? 'Video & AI 24/7' : 'Video & 24/7 AI'}
                  </div>
                </div>
              </div>
            </div>

            {/* Right Showcase Frame (5 cols): Full-height aligned with left column */}
            <div className="lg:col-span-5 flex">
              {curAd ? (
                <div className="w-full rounded-3xl overflow-hidden bg-slate-900/90 backdrop-blur-md border border-white/20 shadow-2xl flex flex-col">
                  <div className="relative aspect-[16/9] bg-slate-950 overflow-hidden shrink-0">
                    {ads.map((adItem, idx) => {
                      const isActive = idx === bannerIdx;
                      const targetLink = normalizeInternalLink(adItem.link, '/courses');
                      const adImgSrc = resolveUploadUrl(adItem.image);
                      return (
                        <Link
                          key={adItem.id || adItem.ad_id || idx}
                          to={targetLink}
                          className={`absolute inset-0 block w-full h-full transition-opacity duration-500 ${
                            isActive ? 'opacity-100 z-[1]' : 'opacity-0 pointer-events-none z-0'
                          }`}
                        >
                          {adImgSrc && (
                            <img
                              src={adImgSrc}
                              alt={adItem.title || 'TonyEnglish'}
                              loading={isActive ? 'eager' : 'lazy'}
                              onError={(e) => {
                                const img = e.currentTarget as HTMLImageElement;
                                img.onerror = null;
                                img.src = '/uploads/No_Image_Wide.svg_1.png';
                              }}
                              className="w-full h-full object-cover object-center"
                            />
                          )}
                        </Link>
                      );
                    })}

                    {ads.length > 1 && (
                      <div className="absolute bottom-3 right-3 flex items-center gap-1.5 z-10">
                        <button
                          type="button"
                          onClick={() => setBannerIdx((prev) => (prev - 1 + ads.length) % ads.length)}
                          className="w-8 h-8 rounded-full bg-slate-900/80 hover:bg-[#2ab4e8] text-white flex items-center justify-center transition backdrop-blur-xs cursor-pointer"
                          title="Previous"
                        >
                          <ChevronLeft className="w-4 h-4" />
                        </button>
                        <span className="bg-slate-900/80 text-white text-[11px] font-bold px-2.5 py-1 rounded-full backdrop-blur-xs tabular-nums">
                          {bannerIdx + 1} / {ads.length}
                        </span>
                        <button
                          type="button"
                          onClick={() => setBannerIdx((prev) => (prev + 1) % ads.length)}
                          className="w-8 h-8 rounded-full bg-slate-900/80 hover:bg-[#2ab4e8] text-white flex items-center justify-center transition backdrop-blur-xs cursor-pointer"
                          title="Next"
                        >
                          <ChevronRight className="w-4 h-4" />
                        </button>
                      </div>
                    )}
                  </div>

                  <div className="p-4 sm:p-5 flex-1 flex flex-col justify-between gap-3 min-h-[176px] sm:min-h-[188px] bg-gradient-to-b from-slate-900/95 to-[#0f172a]">
                    <div className="space-y-2.5">
                      <div className="flex items-center justify-between gap-2">
                        <span className="inline-flex items-center gap-1.5 text-[11px] font-extrabold uppercase tracking-wider text-[#2ab4e8] bg-sky-500/15 border border-sky-400/25 px-2.5 py-0.5 rounded-full whitespace-nowrap">
                          <Sparkles className="w-3 h-3 shrink-0" />
                          <span>
                            {lang === 'vi' ? 'Tiêu điểm' : 'Highlight'}
                            <span className="hidden sm:inline"> TonyEnglish</span>
                          </span>
                        </span>
                        <button
                          type="button"
                          onClick={() => window.dispatchEvent(new CustomEvent('tony-open-lms'))}
                          className="text-xs font-extrabold text-amber-300 hover:text-amber-200 inline-flex items-center gap-1 cursor-pointer whitespace-nowrap shrink-0"
                        >
                          <GraduationCap className="w-3.5 h-3.5 shrink-0" />
                          <span>{lang === 'vi' ? 'Góc Học Viên →' : 'Student Portal →'}</span>
                        </button>
                      </div>

                      <Link
                        to={curAdLink}
                        className="block text-[15px] sm:text-[16px] font-extrabold leading-snug text-white hover:text-[#2ab4e8] transition-colors line-clamp-2 h-[2.75rem] sm:h-[2.85rem] overflow-hidden hero-ad-prose"
                      >
                        {curAdMetaText || curAdDescText || (lang === 'vi' ? 'Khám phá lộ trình học tại TonyEnglish' : 'Explore TonyEnglish Programs')}
                      </Link>

                      {showDistinctAdDesc ? (
                        <p className="text-xs sm:text-[13px] text-slate-300/85 leading-relaxed line-clamp-2 h-[2.5rem] sm:h-[2.65rem] overflow-hidden">
                          {curAdDescText}
                        </p>
                      ) : (
                        <p className="text-xs sm:text-[13px] text-slate-300/80 leading-relaxed line-clamp-2 h-[2.5rem] sm:h-[2.65rem] overflow-hidden">
                          {lang === 'vi'
                            ? 'Lộ trình cá nhân hóa 1 kèm 1 cùng Thầy Tony, kết hợp hệ sinh thái Bài giảng & Phòng thi AI 24/7.'
                            : 'Personalized 1-on-1 roadmap with Mr. Tony, combining bilingual lectures & 24/7 AI Exam Lab.'}
                        </p>
                      )}
                    </div>

                    <div className="pt-2.5 border-t border-white/10 flex items-center justify-between gap-2">
                      <Link
                        to={curAdLink}
                        className="text-xs font-bold text-sky-300 hover:text-white inline-flex items-center gap-1 transition-colors"
                      >
                        <span>{lang === 'vi' ? 'Xem chi tiết chương trình' : 'View program details'}</span>
                        <ArrowRight className="w-3.5 h-3.5" />
                      </Link>
                      {ads.length > 1 && (
                        <div className="flex items-center gap-1.5">
                          {ads.map((_, idx) => (
                            <button
                              key={idx}
                              type="button"
                              onClick={() => setBannerIdx(idx)}
                              aria-label={`Slide ${idx + 1}`}
                              className={`h-1.5 rounded-full transition-all cursor-pointer ${
                                idx === bannerIdx ? 'w-5 bg-[#2ab4e8]' : 'w-1.5 bg-white/25 hover:bg-white/50'
                              }`}
                            />
                          ))}
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              ) : !adsLoaded ? (
                <div className="w-full rounded-3xl overflow-hidden bg-slate-900/80 backdrop-blur-md border border-white/15 shadow-2xl flex flex-col animate-pulse">
                  <div className="aspect-[16/9] bg-slate-800/80 shrink-0" />
                  <div className="p-4 sm:p-5 flex-1 flex flex-col justify-between gap-3 min-h-[176px] sm:min-h-[188px]">
                    <div className="space-y-2.5">
                      <div className="flex items-center justify-between">
                        <div className="h-5 w-32 rounded-full bg-white/10" />
                        <div className="h-4 w-24 rounded-full bg-white/10" />
                      </div>
                      <div className="h-[2.75rem] sm:h-[2.85rem] space-y-2">
                        <div className="h-4 w-11/12 rounded-lg bg-white/15" />
                        <div className="h-4 w-2/3 rounded-lg bg-white/15" />
                      </div>
                      <div className="h-[2.5rem] sm:h-[2.65rem] space-y-1.5">
                        <div className="h-3.5 w-full rounded-lg bg-white/10" />
                        <div className="h-3.5 w-3/4 rounded-lg bg-white/10" />
                      </div>
                    </div>
                    <div className="pt-2.5 border-t border-white/10 flex items-center justify-between">
                      <div className="h-3.5 w-36 rounded bg-white/10" />
                      <div className="h-2 w-16 rounded-full bg-white/10" />
                    </div>
                  </div>
                </div>
              ) : (
                <div className="w-full rounded-3xl bg-white/10 backdrop-blur-md border border-white/20 p-6 sm:p-7 shadow-2xl flex flex-col justify-center space-y-4">
                  <div className="inline-flex items-center gap-2 text-xs font-extrabold uppercase tracking-wider text-amber-300 bg-amber-400/15 border border-amber-300/30 px-3 py-1 rounded-full self-start">
                    <Sparkles className="w-3.5 h-3.5" />
                    <span>Trải nghiệm Hệ sinh thái LMS</span>
                  </div>
                  <h3 className="text-xl font-black text-white">Phòng Học &amp; Luyện Đề Thông Minh 24/7</h3>
                  <ul className="space-y-2.5 text-sm text-slate-200">
                    <li className="flex items-start gap-2.5">
                      <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                      <span>Bài giảng IGCSE Song ngữ Anh – Việt bám sát Syllabus Cambridge</span>
                    </li>
                    <li className="flex items-start gap-2.5">
                      <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                      <span>Kho đề Past Papers có Video hướng dẫn giải chi tiết từng câu (1080p)</span>
                    </li>
                    <li className="flex items-start gap-2.5">
                      <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                      <span>Phòng thi IELTS Computer-delivered &amp; AI chấm Writing/Speaking tức thì</span>
                    </li>
                  </ul>
                </div>
              )}
            </div>
          </div>
        </div>
      </section>

      {/* 1B. BENTO GRID: 4 TRỤ CỘT ĐÀO TẠO & HỆ SINH THÁI TONYENGLISH (True Seamless Overlap onto Hero) */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 -mt-8 sm:-mt-10 relative z-20">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <Link
            to="/courses/luyen-thi-igcse-alevel-cap-toc"
            className="bg-white hover:bg-sky-50/40 border border-slate-200/90 hover:border-[#2ab4e8] rounded-2xl p-5 shadow-md hover:shadow-soft hover:-translate-y-0.5 transition-all group flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between mb-3">
                <div className="w-10 h-10 rounded-xl bg-amber-50 border border-amber-200/80 text-amber-700 flex items-center justify-center group-hover:scale-105 transition-transform">
                  <Award className="w-5 h-5" />
                </div>
                <span className="text-[11px] font-extrabold uppercase tracking-wider text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded-full border border-amber-200/70">
                  Cambridge IGCSE
                </span>
              </div>
              <h3 className="font-display font-extrabold text-[16px] text-slate-900 group-hover:text-[#0a5482] mb-1.5">
                {lang === 'vi' ? 'Hệ Quốc tế IGCSE (A/A*)' : 'Cambridge IGCSE Prep'}
              </h3>
              <p className="text-xs sm:text-[13px] text-slate-500 leading-relaxed">
                {lang === 'vi'
                  ? 'Sciences, Business, Economics, Geography, Maths & ESL — Lý thuyết song ngữ & Video giải Past Papers.'
                  : 'Bilingual syllabus notes, topical quizzes & Full HD past paper walkthroughs.'}
              </p>
            </div>
            <div className="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-extrabold text-[#0a5482]">
              <span>{lang === 'vi' ? 'Xem các môn IGCSE' : 'Explore IGCSE'}</span>
              <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
            </div>
          </Link>

          <Link
            to="/courses/ielts"
            className="bg-white hover:bg-sky-50/40 border border-slate-200/90 hover:border-[#2ab4e8] rounded-2xl p-5 shadow-md hover:shadow-soft hover:-translate-y-0.5 transition-all group flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between mb-3">
                <div className="w-10 h-10 rounded-xl bg-sky-50 border border-sky-200/80 text-[#0a5482] flex items-center justify-center group-hover:scale-105 transition-transform">
                  <Target className="w-5 h-5" />
                </div>
                <span className="text-[11px] font-extrabold uppercase tracking-wider text-[#0a5482] bg-sky-50 px-2.5 py-0.5 rounded-full border border-sky-200/70">
                  Band 6.5 – 8.0+
                </span>
              </div>
              <h3 className="font-display font-extrabold text-[16px] text-slate-900 group-hover:text-[#0a5482] mb-1.5">
                {lang === 'vi' ? 'Luyện thi IELTS 1 kèm 1' : '1-on-1 IELTS Coaching'}
              </h3>
              <p className="text-xs sm:text-[13px] text-slate-500 leading-relaxed">
                {lang === 'vi'
                  ? 'Lộ trình cá nhân hóa 4 kỹ năng, phòng thi máy tính chuẩn IDP/BC & AI chấm Writing/Speaking chi tiết.'
                  : 'Personalized 4-skill roadmap with computer-delivered mock tests & AI grading.'}
              </p>
            </div>
            <div className="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-extrabold text-[#0a5482]">
              <span>{lang === 'vi' ? 'Lộ trình IELTS' : 'IELTS Roadmap'}</span>
              <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
            </div>
          </Link>

          <Link
            to="/courses/english-communication%201"
            className="bg-white hover:bg-sky-50/40 border border-slate-200/90 hover:border-[#2ab4e8] rounded-2xl p-5 shadow-md hover:shadow-soft hover:-translate-y-0.5 transition-all group flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between mb-3">
                <div className="w-10 h-10 rounded-xl bg-emerald-50 border border-emerald-200/80 text-emerald-700 flex items-center justify-center group-hover:scale-105 transition-transform">
                  <MessageCircle className="w-5 h-5" />
                </div>
                <span className="text-[11px] font-extrabold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200/70">
                  1-on-1 VIP
                </span>
              </div>
              <h3 className="font-display font-extrabold text-[16px] text-slate-900 group-hover:text-[#0a5482] mb-1.5">
                {lang === 'vi' ? 'Giao tiếp & Phản xạ Công sở' : 'Executive Communication'}
              </h3>
              <p className="text-xs sm:text-[13px] text-slate-500 leading-relaxed">
                {lang === 'vi'
                  ? 'Chuẩn hóa phát âm IPA, Podcast Shadowing song ngữ & luyện hội thoại phản xạ thực tế cùng AI.'
                  : 'IPA pronunciation mastery, bilingual shadowing podcasts & AI reflex speaking.'}
              </p>
            </div>
            <div className="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-extrabold text-[#0a5482]">
              <span>{lang === 'vi' ? 'Khám phá khóa học' : 'View Courses'}</span>
              <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
            </div>
          </Link>

          <button
            type="button"
            onClick={() => window.dispatchEvent(new CustomEvent('tony-open-lms'))}
            className="bg-gradient-to-br from-[#0a5482] to-[#0f172a] text-white rounded-2xl p-5 shadow-lg hover:shadow-xl hover:-translate-y-0.5 transition-all group text-left flex flex-col justify-between cursor-pointer border border-sky-400/25"
          >
            <div>
              <div className="flex items-center justify-between mb-3">
                <div className="w-10 h-10 rounded-xl bg-[#2ab4e8] text-white flex items-center justify-center group-hover:scale-105 transition-transform shadow-sm">
                  <Bot className="w-5 h-5" />
                </div>
                <span className="text-[11px] font-extrabold uppercase tracking-wider text-amber-300 bg-white/10 px-2.5 py-0.5 rounded-full border border-white/15">
                  Smart LMS
                </span>
              </div>
              <h3 className="font-display font-extrabold text-[16px] text-white mb-1.5">
                {lang === 'vi' ? 'Góc Học Viên & Phòng Thi AI' : 'Student Portal & AI Lab'}
              </h3>
              <p className="text-xs sm:text-[13px] text-sky-100/85 leading-relaxed">
                {lang === 'vi'
                  ? 'Lịch báo bài cá nhân, Bảng công việc hàng ngày, Kho đề Past Papers & Trợ lý Thầy Tony AI 24/7.'
                  : 'Personal study calendar, daily taskboard, past papers & 24/7 AI Study Coach.'}
              </p>
            </div>
            <div className="mt-4 pt-3 border-t border-white/15 flex items-center justify-between text-xs font-extrabold text-[#2ab4e8]">
              <span>{lang === 'vi' ? 'Truy cập Góc Học Viên' : 'Open Student Portal'}</span>
              <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
            </div>
          </button>
        </div>
      </section>

      {/* MAIN CONTENT BODY (Clean Vertical Rhythm Below Bento) */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 mt-12 sm:mt-14 space-y-12 sm:space-y-14">
        {/* 2. BALANCED TOP 2-COLUMN BAND: FOCUS ON (8 cols) + 1-ON-1 ENROLMENT ROADMAP (4 cols) — Exact Top & Bottom Alignment */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-7 lg:gap-8 items-stretch">
          {/* LEFT COLUMN (8 cols): FOCUS ON */}
          <section className="lg:col-span-8 flex flex-col space-y-5">
            <div className="flex items-center justify-between gap-3 border-b border-slate-200 pb-3">
              <div className="flex items-center gap-2.5 min-w-0">
                <span className="w-9 h-9 rounded-xl bg-sky-100 text-[#0a5482] flex items-center justify-center shadow-2xs shrink-0">
                  <Sparkles className="w-4 h-4" />
                </span>
                <h2 className="text-lg sm:text-2xl font-black text-slate-800 tracking-tight leading-snug">
                  {t('Focus on')}
                </h2>
              </div>
              <Link
                to="/news"
                className="text-xs sm:text-sm font-bold text-[#0a5482] hover:text-[#2ab4e8] transition-colors whitespace-nowrap shrink-0"
              >
                {lang === 'vi' ? 'Khám phá Thư viện →' : 'Explore Library →'}
              </Link>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 flex-1">
              {/* 1A. Latest Sticky News Card */}
              {curSticky && (
                <div className="group bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden flex flex-col h-full">
                  <div className="relative h-48 overflow-hidden bg-slate-100">
                    <Link
                      to={`/news/view/${(curSticky.news_title_url || '').trim()}`}
                      className="block w-full h-full"
                    >
                      {resolveUploadUrl(curSticky.news_thumb) && (
                        <img
                          src={resolveUploadUrl(curSticky.news_thumb)}
                          alt={curSticky.news_title}
                          onError={(e) => {
                            const img = e.currentTarget as HTMLImageElement;
                            img.onerror = null;
                            img.src = '/uploads/No_Image_Wide.svg_1.png';
                          }}
                          className="w-full h-full object-cover object-[50%_20%] group-hover:scale-105 transition-transform duration-500"
                        />
                      )}
                    </Link>
                    <span className="absolute top-3 left-3 bg-[#0a5482]/95 backdrop-blur-xs text-white text-xs font-extrabold px-3 py-1 rounded-full shadow-md border border-white/15 inline-flex items-center gap-1">
                      <Sparkles className="w-3 h-3 text-amber-300 shrink-0" />
                      <span>{t('Lastest News')}</span>
                    </span>
                  </div>

                  <div className="p-5 flex-1 flex flex-col justify-between">
                    <div>
                      <Link
                        to={`/news/view/${(curSticky.news_title_url || '').trim()}`}
                        className="font-extrabold text-[17px] sm:text-[18px] text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2 min-h-[3rem] leading-snug mb-2 block"
                      >
                        {(curSticky.news_title || '').trim()}
                      </Link>
                      <p className="text-slate-600 text-[15px] leading-relaxed line-clamp-3 min-h-[4.3rem]">
                        {truncateWords(curSticky.news_desc, 160)}
                      </p>
                    </div>

                    <div className="pt-4 mt-4 border-t border-slate-100 flex items-center justify-between gap-2">
                      <Link
                        to="/news"
                        className="text-sm font-extrabold text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1"
                      >
                        <span>{t('Related Post')}</span>
                        <span>→</span>
                      </Link>
                      {stickyNews.length > 1 && (
                        <div className="flex items-center gap-1.5">
                          <span className="text-[11px] font-bold text-slate-400 tabular-nums">
                            {stickyIdx + 1}/{stickyNews.length}
                          </span>
                          <button
                            type="button"
                            onClick={() => setStickyIdx((prev) => (prev - 1 + stickyNews.length) % stickyNews.length)}
                            className="w-7 h-7 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-600 text-sm font-bold cursor-pointer flex items-center justify-center"
                            title="Previous"
                          >
                            ‹
                          </button>
                          <button
                            type="button"
                            onClick={() => setStickyIdx((prev) => (prev + 1) % stickyNews.length)}
                            className="w-7 h-7 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-600 text-sm font-bold cursor-pointer flex items-center justify-center"
                            title="Next"
                          >
                            ›
                          </button>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              )}

              {/* 1B. Video Focus (if present) */}
              {videoFocus && (
                <div className="group bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden flex flex-col h-full">
                  <div className="relative h-48 overflow-hidden bg-slate-100">
                    <button
                      type="button"
                      onClick={() => setPopupVideo(videoFocus)}
                      className="block w-full h-full text-left relative cursor-pointer"
                    >
                      {resolveUploadUrl(videoFocus.video_thumb) && (
                        <img
                          src={resolveUploadUrl(videoFocus.video_thumb)}
                          alt={videoFocus.video_desc}
                          onError={(e) => {
                            const img = e.currentTarget as HTMLImageElement;
                            img.onerror = null;
                            img.src = '/uploads/No_Image_Wide.svg_1.png';
                          }}
                          className="w-full h-full object-cover object-[50%_20%] group-hover:scale-105 transition-transform duration-500"
                        />
                      )}
                      <div className="absolute inset-0 bg-slate-900/25 flex items-center justify-center">
                        <span className="w-12 h-12 rounded-full bg-white/90 text-[#0a5482] flex items-center justify-center text-lg shadow-lg">
                          ▶
                        </span>
                      </div>
                    </button>
                    <span className="absolute top-3 left-3 bg-rose-600 text-white text-xs font-extrabold px-3 py-1 rounded-full shadow-md">
                      🎬 {t('Video')}
                    </span>
                  </div>

                  <div className="p-5 flex-1 flex flex-col justify-between">
                    <div>
                      <Link
                        to={
                          videoCateMap[videoFocus.vc_id]
                            ? `/video/${(videoCateMap[videoFocus.vc_id].vc_name_url || '').trim()}/${(
                                videoFocus.video_url || ''
                              ).trim()}`
                            : '/videos'
                        }
                        className="font-extrabold text-[17px] sm:text-[18px] text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2 leading-snug mb-2 block"
                      >
                        {truncateWords(videoFocus.video_desc, 150)}
                      </Link>
                      <p className="text-slate-600 text-[15px] leading-relaxed line-clamp-3">
                        {truncateWords(videoFocus.video_cmt, 180)}
                      </p>
                    </div>

                    <div className="pt-4 mt-4 border-t border-slate-100">
                      <Link
                        to={
                          videoCateMap[videoFocus.vc_id]
                            ? `/video/${(videoCateMap[videoFocus.vc_id].vc_name_url || '').trim()}/${(
                                videoFocus.video_url || ''
                              ).trim()}`
                            : '/videos'
                        }
                        className="text-sm font-extrabold text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1"
                      >
                        <span>{t('Related Post')}</span>
                        <span>→</span>
                      </Link>
                    </div>
                  </div>
                </div>
              )}

              {/* 1C. Focus 0 Categories (e.g. Bí kíp học) */}
              {focusZeroCates.map((nc) => renderNewsCateCard(nc, 'default'))}
            </div>
          </section>

          {/* RIGHT COLUMN (4 cols): 1-ON-1 ENROLMENT ROADMAP (Matched Section Header + Exact Height Alignment) */}
          <aside className="lg:col-span-4 flex flex-col space-y-5">
            <div className="flex items-center justify-between gap-3 border-b border-slate-200 pb-3">
              <div className="flex items-center gap-2.5 min-w-0">
                <span className="w-9 h-9 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center shadow-2xs shrink-0">
                  <Calendar className="w-4 h-4" />
                </span>
                <h2 className="text-lg sm:text-2xl font-black text-slate-800 tracking-tight leading-snug">
                  {t('Enrolment')}
                </h2>
              </div>
              <Link
                to="/opening"
                className="text-xs sm:text-sm font-bold text-[#0a5482] hover:text-[#2ab4e8] transition-colors whitespace-nowrap shrink-0"
              >
                {lang === 'vi' ? 'Chi tiết →' : 'More →'}
              </Link>
            </div>

            <div className="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden flex flex-col flex-1">
              <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-5 py-3.5 text-white">
                <div className="flex items-center gap-2 text-[11px] font-extrabold uppercase tracking-wider text-emerald-300 mb-1">
                  <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
                  <span>{lang === 'vi' ? 'Đang nhận học viên 1 kèm 1' : 'Open for 1-on-1 Enrollment'}</span>
                </div>
                <p className="text-[13.5px] font-bold text-white/95 leading-snug">
                  {lang === 'vi'
                    ? 'Học trực tiếp tại R2B Royal City & Online 1-1 cùng Thầy Tony'
                    : 'Private home tutoring at R2B Royal City & Online with Mr. Tony'}
                </p>
              </div>

              <div className="p-5 flex-1 flex flex-col justify-between gap-4">
                <ol className="space-y-3.5">
                  <li className="flex items-start gap-3">
                    <span className="w-7 h-7 rounded-xl bg-sky-50 border border-sky-200 text-[#0a5482] font-black text-xs flex items-center justify-center shrink-0 mt-0.5">
                      01
                    </span>
                    <div className="min-w-0">
                      <h3 className="font-extrabold text-[14.5px] text-slate-800 leading-snug">
                        {lang === 'vi' ? 'Kiểm tra trình độ đầu vào 1-1' : '1-on-1 Placement Assessment'}
                      </h3>
                      <p className="text-xs text-slate-500 leading-relaxed mt-0.5">
                        {lang === 'vi'
                          ? 'Đánh giá chính xác điểm mạnh – yếu của học viên ngay buổi đầu.'
                          : 'Pinpoint exact strengths and gaps in the initial session.'}
                      </p>
                    </div>
                  </li>

                  <li className="flex items-start gap-3">
                    <span className="w-7 h-7 rounded-xl bg-amber-50 border border-amber-200 text-amber-700 font-black text-xs flex items-center justify-center shrink-0 mt-0.5">
                      02
                    </span>
                    <div className="min-w-0">
                      <h3 className="font-extrabold text-[14.5px] text-slate-800 leading-snug">
                        {lang === 'vi' ? 'Thiết kế lộ trình cá nhân hóa' : 'Personalized Study Roadmap'}
                      </h3>
                      <p className="text-xs text-slate-500 leading-relaxed mt-0.5">
                        {lang === 'vi'
                          ? 'Bám sát Syllabus IGCSE, mục tiêu Band IELTS hoặc Giao tiếp công sở.'
                          : 'Tailored to IGCSE Syllabus, IELTS targets, or Executive English.'}
                      </p>
                    </div>
                  </li>

                  <li className="flex items-start gap-3">
                    <span className="w-7 h-7 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-700 font-black text-xs flex items-center justify-center shrink-0 mt-0.5">
                      03
                    </span>
                    <div className="min-w-0">
                      <h3 className="font-extrabold text-[14.5px] text-slate-800 leading-snug">
                        {lang === 'vi' ? 'Kèm sát & học trên Smart LMS' : 'Live Mentoring + Smart LMS'}
                      </h3>
                      <p className="text-xs text-slate-500 leading-relaxed mt-0.5">
                        {lang === 'vi'
                          ? 'Lịch linh hoạt, kho đề Past Papers có Video chữa & AI chấm bài 24/7.'
                          : 'Flexible schedule with HD video walkthroughs & 24/7 AI feedback.'}
                      </p>
                    </div>
                  </li>
                </ol>

                <div className="pt-3.5 border-t border-slate-100 grid grid-cols-2 gap-2.5">
                  <a
                    href="https://zalo.me/0935058688"
                    target="_blank"
                    rel="noreferrer"
                    onClick={() => trackUnifiedContact('Zalo', 'HomePage_Sidebar_Consult')}
                    className="bg-[#0a5482] hover:bg-[#084266] text-white font-extrabold text-xs px-3 py-2.5 rounded-xl transition inline-flex items-center justify-center gap-1.5 shadow-xs whitespace-nowrap"
                  >
                    <MessageCircle className="w-3.5 h-3.5 text-[#2ab4e8] shrink-0" />
                    <span>{lang === 'vi' ? 'Nhắn Zalo tư vấn' : 'Zalo Consult'}</span>
                  </a>
                  <button
                    type="button"
                    onClick={() => window.dispatchEvent(new CustomEvent('tony-open-lms', { detail: 'register' }))}
                    className="bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200/90 font-extrabold text-xs px-3 py-2.5 rounded-xl transition inline-flex items-center justify-center gap-1.5 cursor-pointer whitespace-nowrap"
                  >
                    <Sparkles className="w-3.5 h-3.5 text-amber-600 shrink-0" />
                    <span>{lang === 'vi' ? 'Học thử miễn phí' : 'Free Trial'}</span>
                  </button>
                </div>
              </div>
            </div>
          </aside>
        </div>

        {/* 3. FULL-WIDTH SYMMETRICAL SHOWCASE BAND: HỌC TẠI TONYENGLISH (Clean Normalized Cards) */}
        {allTestimonials.length > 0 && (
          <section className="space-y-5">
            <div className="flex items-center justify-between gap-3 border-b border-slate-200 pb-3">
              <div className="flex items-center gap-2.5 min-w-0">
                <span className="w-9 h-9 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center shadow-2xs shrink-0">
                  <GraduationCap className="w-4 h-4" />
                </span>
                <h2 className="text-lg sm:text-2xl font-black text-slate-800 tracking-tight leading-snug">
                  {lang === 'vi' ? 'Phương pháp Học tại TonyEnglish' : 'The TonyEnglish Learning Ecosystem'}
                </h2>
              </div>
              <Link
                to="/courses"
                className="text-xs sm:text-sm font-bold text-[#0a5482] hover:text-[#2ab4e8] transition-colors whitespace-nowrap shrink-0"
              >
                {lang === 'vi' ? 'Xem các khóa học →' : 'View courses →'}
              </Link>
            </div>

            <div className={`grid grid-cols-1 ${allTestimonials.length >= 2 ? 'lg:grid-cols-2' : ''} gap-6`}>
              {allTestimonials.map((testValue, idx) => {
                const parsed = parseTestimonialCard(testValue, lang, idx);
                const rawHtml =
                  (lang === 'vi'
                    ? testValue.testimonial_content_vi || testValue.testimonial_content_en
                    : testValue.testimonial_content_en || testValue.testimonial_content_vi) || '';

                if (!parsed.useStructuredCard) {
                  return (
                    <div
                      key={testValue.testimonial_id}
                      className="bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-md transition-shadow overflow-hidden flex flex-col"
                    >
                      <div className="px-6 py-3.5 bg-gradient-to-r from-slate-50 to-sky-50/40 border-b border-slate-200/80 flex items-center gap-2">
                        <span className="w-1.5 h-4 rounded-full bg-[#2ab4e8] shrink-0" />
                        <h3 className="font-black text-slate-800 text-base">{parsed.badge}</h3>
                      </div>
                      <div
                        className="p-5 sm:p-6 legacy-prose testimonial-legacy-prose text-[15px]"
                        dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(rawHtml) }}
                      />
                    </div>
                  );
                }

                return (
                  <Link
                    key={testValue.testimonial_id}
                    to={parsed.linkUrl}
                    className="group bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden flex flex-col sm:flex-row h-full"
                  >
                    {/* Identical Media Box for Symmetrical Visual Height */}
                    <div
                      className={`relative h-56 sm:h-auto sm:w-56 md:w-60 sm:min-h-[240px] shrink-0 overflow-hidden ${
                        parsed.isDiagram
                          ? 'bg-gradient-to-br from-sky-50/80 via-white to-slate-50 flex items-center justify-center p-4 pt-12 sm:pt-11 border-b sm:border-b-0 sm:border-r border-slate-100'
                          : 'bg-slate-100'
                      }`}
                    >
                      {parsed.imageUrl && (
                        <img
                          src={parsed.imageUrl}
                          alt={parsed.headline}
                          onError={(e) => {
                            const img = e.currentTarget as HTMLImageElement;
                            img.onerror = null;
                            img.src = '/uploads/No_Image_Wide.svg_1.png';
                          }}
                          className={
                            parsed.isDiagram
                              ? 'max-h-40 sm:max-h-44 w-full object-contain group-hover:scale-105 transition-transform duration-500'
                              : 'w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500'
                          }
                        />
                      )}
                      <span className="absolute top-3 left-3 bg-[#0a5482]/90 backdrop-blur-xs text-white text-[11px] font-extrabold px-3 py-1 rounded-full shadow-md">
                        {parsed.badge}
                      </span>
                    </div>

                    {/* Clean Typography Content */}
                    <div className="p-5 sm:p-6 flex-1 flex flex-col justify-between min-w-0">
                      <div>
                        <h3 className="font-display font-extrabold text-[17px] sm:text-[18px] text-slate-800 group-hover:text-[#0a5482] transition-colors leading-snug mb-2.5">
                          {parsed.headline}
                        </h3>
                        <p className="text-slate-600 text-[14.5px] leading-relaxed line-clamp-5">
                          {parsed.summary}
                        </p>
                      </div>

                      <div className="pt-4 mt-4 border-t border-slate-100 flex items-center justify-between text-xs sm:text-sm font-extrabold text-[#0a5482] group-hover:text-[#2ab4e8] transition-colors">
                        <span>{parsed.ctaLabel}</span>
                        <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                      </div>
                    </div>
                  </Link>
                );
              })}
            </div>
          </section>
        )}

        {/* 4. FULL-WIDTH MAGAZINE SECTIONS (Adaptive 2-up Horizontal / 4-up Compact / 3-up — Zero Orphan Slots) */}
        <div className="space-y-12 sm:space-y-14">
          {/* SECTION 2: READING PRACTICE (focus = 5) */}
          {renderCategorySection(5, 'Reading Practice', <BookOpen className="w-4 h-4" />)}

          {/* SECTION 3: LEARNING THROUGH CONVERSATION (focus = 4) */}
          {renderCategorySection(4, 'Learning Through Conversation', <MessageCircle className="w-4 h-4" />)}

          {/* SECTION 4: WORDS IN THE NEWS (focus = 1) */}
          {renderCategorySection(1, 'Words In The news', <Globe className="w-4 h-4" />)}

          {/* SECTION 5: VIDEOS STORE */}
          {featuredVideoParents.length > 0 && (
            <section className="space-y-5">
              <div className="flex items-center justify-between gap-3 border-b border-slate-200 pb-3">
                <div className="flex items-center gap-2.5 min-w-0">
                  <span className="w-9 h-9 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center shadow-2xs shrink-0">
                    <Video className="w-4 h-4" />
                  </span>
                  <h2 className="text-lg sm:text-2xl font-black text-slate-800 tracking-tight leading-snug">
                    {t('Videos store')}
                  </h2>
                </div>
                <Link
                  to="/videos"
                  className="text-xs sm:text-sm font-bold text-[#0a5482] hover:text-[#2ab4e8] transition-colors whitespace-nowrap shrink-0"
                >
                  {lang === 'vi' ? 'Xem Kho Video →' : 'All Videos →'}
                </Link>
              </div>

              <div className={videoStoreGridClass}>
                {featuredVideoParents.map((vc) => {
                  const childCates = allVideoCategories.filter(
                    (sub) => Number(sub.vc_parent) === Number(vc.vc_id)
                  );
                  const activeSub =
                    childCates.length > 0 ? childCates[videoSlideIdx % childCates.length] : vc;
                  const parentTitle = lang === 'vi' ? vc.vc_name_vi || vc.vc_name : vc.vc_name;
                  const subTitle =
                    lang === 'vi'
                      ? activeSub.vc_name_vi || activeSub.vc_name
                      : activeSub.vc_name || parentTitle;
                  const descText =
                    lang === 'vi' ? vc.vc_desc_vi || vc.vc_desc : vc.vc_desc || vc.vc_desc_vi;
                  const targetUrl =
                    childCates.length > 0
                      ? `/video/${(activeSub.vc_name_url || '').trim()}`
                      : `/videos/${(vc.vc_name_url || '').trim()}`;
                  const isCompact = videoStoreVariant === 'compact';
                  const isHorizontal = videoStoreVariant === 'horizontal';

                  return (
                    <div
                      key={vc.vc_id}
                      className={`group bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden flex ${
                        isHorizontal ? 'flex-col sm:flex-row' : 'flex-col'
                      } h-full`}
                    >
                      <div
                        className={`relative overflow-hidden bg-slate-900 ${
                          isHorizontal
                            ? 'h-48 sm:h-auto sm:w-52 md:w-56 sm:min-h-[216px] shrink-0'
                            : isCompact
                            ? 'h-44'
                            : 'h-48'
                        }`}
                      >
                        <Link to={targetUrl} className="block w-full h-full relative">
                          {resolveUploadUrl(activeSub.vc_image || vc.vc_image) && (
                            <img
                              src={resolveUploadUrl(activeSub.vc_image || vc.vc_image)}
                              alt={subTitle}
                              onError={(e) => {
                                const img = e.currentTarget as HTMLImageElement;
                                img.onerror = null;
                                img.src = '/uploads/No_Image_Wide.svg_1.png';
                              }}
                              className="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500 opacity-95"
                            />
                          )}
                          <div className="absolute inset-0 bg-gradient-to-t from-slate-900/55 via-transparent to-transparent flex items-center justify-center">
                            <span className="w-11 h-11 rounded-full bg-white/95 text-[#0a5482] flex items-center justify-center text-base shadow-lg group-hover:scale-110 transition-transform">
                              ▶
                            </span>
                          </div>
                        </Link>
                        <span className="absolute top-3 left-3 max-w-[calc(100%-24px)] truncate bg-[#0a5482]/90 backdrop-blur-xs text-white text-[11px] font-extrabold px-2.5 py-1 rounded-full shadow-md">
                          {parentTitle}
                        </span>
                      </div>

                      <div className={`${isCompact ? 'p-4' : 'p-5'} flex-1 flex flex-col justify-between min-w-0`}>
                        <div>
                          <Link
                            to={targetUrl}
                            className={`font-extrabold ${
                              isCompact ? 'text-[15.5px] min-h-[2.6rem]' : 'text-[17px] sm:text-[18px] min-h-[3rem]'
                            } text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2 leading-snug mb-2 block`}
                          >
                            {subTitle}
                          </Link>
                          <p
                            className={`text-slate-600 ${
                              isCompact ? 'text-[13.5px] min-h-[3.9rem]' : 'text-[15px] min-h-[4.3rem]'
                            } leading-relaxed line-clamp-3`}
                          >
                            {truncateWords(descText, isCompact ? 130 : 165)}
                          </p>
                        </div>

                        <div className={`${isCompact ? 'pt-3 mt-3.5' : 'pt-4 mt-4'} border-t border-slate-100`}>
                          <Link
                            to={targetUrl}
                            className={`${isCompact ? 'text-xs' : 'text-sm'} font-extrabold text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1`}
                          >
                            <span>{t('Related Post')}</span>
                            <span>→</span>
                          </Link>
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            </section>
          )}

          {/* SECTION 6: OTHER LEARNING MATERIALS (focus = 3) */}
          {renderCategorySection(3, 'Other learning materials', <Layers className="w-4 h-4" />)}
        </div>

        {/* 5. FINAL CONVERSION CTA BANNER BEFORE FOOTER */}
        <section className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-[#06283d] via-[#0a5482] to-[#0f172a] text-white p-6 sm:p-8 lg:p-10 shadow-xl border border-sky-400/20">
          <div className="absolute -top-24 -right-24 w-72 h-72 bg-[#2ab4e8]/20 blur-3xl rounded-full pointer-events-none" />
          <div className="relative z-10 flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
            <div className="space-y-2 max-w-2xl">
              <div className="inline-flex items-center gap-1.5 text-[11px] font-extrabold uppercase tracking-wider text-amber-300 bg-white/10 border border-white/15 px-3 py-1 rounded-full">
                <Sparkles className="w-3.5 h-3.5" />
                <span>{lang === 'vi' ? 'Đồng hành 1 kèm 1 cùng Thầy Tony' : '1-on-1 Mentoring with Teacher Tony'}</span>
              </div>
              <h2 className="font-display font-black text-xl sm:text-2xl lg:text-[28px] leading-tight text-white">
                {lang === 'vi'
                  ? 'Sẵn sàng bứt phá điểm số IELTS, Cambridge IGCSE & Giao tiếp?'
                  : 'Ready to Accelerate Your IELTS, Cambridge IGCSE & English Fluency?'}
              </h2>
              <p className="text-slate-200/90 text-sm sm:text-[15px] leading-relaxed">
                {lang === 'vi'
                  ? 'Tạo tài khoản miễn phí để trải nghiệm Kho bài giảng song ngữ, Phòng thi AI chấm chữa 24/7 hoặc nhắn Zalo đặt lịch kiểm tra trình độ đầu vào cùng Thầy Tony.'
                  : 'Create a free account to explore bilingual lectures & 24/7 AI mock exams, or message Mr. Tony directly on Zalo for a 1-on-1 placement assessment.'}
              </p>
            </div>

            <div className="flex flex-wrap items-center gap-3 shrink-0">
              <button
                type="button"
                onClick={() => window.dispatchEvent(new CustomEvent('tony-open-lms', { detail: 'register' }))}
                className="bg-gradient-to-r from-amber-400 via-yellow-400 to-amber-500 hover:from-amber-500 hover:to-yellow-500 text-slate-950 font-extrabold text-sm px-5 py-3 rounded-2xl shadow-lg transition-all active:scale-95 inline-flex items-center gap-2 cursor-pointer whitespace-nowrap"
              >
                <Sparkles className="w-4 h-4 shrink-0" />
                <span>{lang === 'vi' ? 'Vào Học Thử Miễn Phí' : 'Start Free Trial'}</span>
                <ArrowRight className="w-4 h-4 shrink-0" />
              </button>

              <a
                href="https://zalo.me/0935058688"
                target="_blank"
                rel="noreferrer"
                onClick={() => trackUnifiedContact('Zalo', 'HomePage_Bottom_CTA')}
                className="bg-white/12 hover:bg-white/22 text-white border border-white/25 font-bold text-sm px-5 py-3 rounded-2xl backdrop-blur-xs transition-all active:scale-95 inline-flex items-center gap-2 whitespace-nowrap"
              >
                <Phone className="w-4 h-4 text-[#2ab4e8] shrink-0" />
                <span>{lang === 'vi' ? 'Zalo: 0935 058 688' : 'Zalo: 0935 058 688'}</span>
              </a>
            </div>
          </div>
        </section>
      </div>

      {/* FOCUS VIDEO POPUP MODAL */}
      {popupVideo && (
        <div
          className="fixed inset-0 bg-slate-900/75 backdrop-blur-xs z-50 flex items-center justify-center p-4"
          onClick={() => setPopupVideo(null)}
        >
          <div
            className="bg-white rounded-3xl w-full max-w-3xl max-h-[90vh] overflow-y-auto shadow-2xl p-6 relative"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between pb-4 mb-4 border-b border-slate-200">
              <h3 className="font-black text-lg text-[#0a5482] pr-6">{popupVideo.video_desc}</h3>
              <button
                type="button"
                onClick={() => setPopupVideo(null)}
                className="w-8 h-8 rounded-full bg-slate-100 hover:bg-rose-500 hover:text-white text-slate-600 font-bold flex items-center justify-center transition-colors shrink-0 cursor-pointer"
              >
                ✕
              </button>
            </div>
            {popupVideo.video_link && (
              <div className="aspect-video w-full rounded-2xl overflow-hidden bg-black">
                <iframe
                  width="100%"
                  height="100%"
                  src={getYoutubeEmbedUrl(popupVideo.video_link)}
                  title={popupVideo.video_desc}
                  frameBorder="0"
                  referrerPolicy="strict-origin-when-cross-origin"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                  allowFullScreen
                />
              </div>
            )}
            {popupVideo.video_cmt && (
              <div
                className="mt-4 legacy-prose text-sm"
                dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(popupVideo.video_cmt) }}
              />
            )}
          </div>
        </div>
      )}
    </div>
  );
};
