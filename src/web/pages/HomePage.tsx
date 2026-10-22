import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import { resolveUploadUrl, truncateWords, getYoutubeEmbedUrl, fixLegacyHtmlContent, updatePageSeo } from '../lib/utils';

export const HomePage: React.FC = () => {
  const { lang, t } = useApp();

  useEffect(() => {
    updatePageSeo('', 'Trung tâm tiếng Anh TonyEnglish - Học tiếng Anh giao tiếp, luyện thi TOEIC, IELTS trực tuyến.');
  }, []);

  const [ads, setAds] = useState<any[]>([]);
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
  const [openingClasses, setOpeningClasses] = useState<any[]>([]);
  const [popupVideo, setPopupVideo] = useState<any | null>(null);

  useEffect(() => {
    async function fetchHomeData() {
      const [adsRes, stickyRes, newsCateRes, vFocusRes, vEventRes, vCateRes, testiRes, openRes] = await Promise.all([
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
        supabase
          .from('te_user_group')
          .select('*')
          .eq('deleted', 0)
          .eq('ug_status', 1)
          .eq('ug_opening', 1),
      ]);

      if (adsRes.data) setAds(adsRes.data);
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
            .limit(1000);

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
      if (openRes.data) setOpeningClasses(openRes.data);
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

  const videoCateMap: Record<number, any> = {};
  allVideoCategories.forEach((vc) => {
    videoCateMap[vc.vc_id] = vc;
  });

  // Render a single modern news category card
  const renderNewsCateCard = (cate: any) => {
    const newsItem = latestNewsByCate[cate.news_cc_id];
    if (!newsItem) return null;

    const cateTitle = lang === 'vi' ? cate.news_cc_name_vi || cate.news_cc_name : cate.news_cc_name;
    const cateUrl = `/news/category/${(cate.news_cc_name_url || '').trim()}`;
    const articleUrl = `/news/view/${(newsItem.news_title_url || '').trim()}`;
    const rawTitle = (newsItem.news_title || '').trim();

    return (
      <div
        key={cate.news_cc_id}
        className="group bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden flex flex-col"
      >
        <div className="relative h-48 overflow-hidden bg-slate-100">
          <Link to={articleUrl} className="block w-full h-full">
            <img
              src={resolveUploadUrl(newsItem.news_thumb)}
              alt={rawTitle}
              onError={(e) => {
                (e.currentTarget as HTMLImageElement).src = '/uploads/No_Image_Wide.svg_1.png';
              }}
              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
          </Link>
          <Link
            to={cateUrl}
            className="absolute top-3 left-3 bg-[#0a5482]/90 backdrop-blur-xs text-white text-[11px] font-extrabold px-3 py-1 rounded-full shadow-md hover:bg-[#2ab4e8] transition-colors"
          >
            {cateTitle}
          </Link>
        </div>

        <div className="p-5 flex-1 flex flex-col justify-between">
          <div>
            <Link
              to={articleUrl}
              className="font-extrabold text-[17px] sm:text-[18px] text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2 leading-snug mb-2"
            >
              {rawTitle}
            </Link>
            <p className="text-slate-600 text-[15px] leading-relaxed line-clamp-3">
              {truncateWords(newsItem.news_desc, 165)}
            </p>
          </div>

          <div className="pt-4 mt-4 border-t border-slate-100 flex items-center justify-between">
            <Link
              to={cateUrl}
              className="text-sm font-extrabold text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1 transition-colors"
            >
              <span>{t('Related Post')}</span>
              <span>→</span>
            </Link>
            <Link
              to={articleUrl}
              className="text-sm font-bold text-slate-500 hover:text-slate-800 transition-colors"
            >
              {lang === 'vi' ? 'Đọc tiếp' : 'Read more'}
            </Link>
          </div>
        </div>
      </div>
    );
  };

  // Render a focus section (5 = Reading Practice, 4 = Learning Through Conversation, 1 = Words In The news, 3 = Other)
  const renderCategorySection = (focusType: number, sectionTitleKey: string, icon: string) => {
    const matchedCates = newsCategories.filter(
      (nc) => Number(nc.news_cc_focus) === focusType && !!latestNewsByCate[nc.news_cc_id]
    );
    if (matchedCates.length === 0 && !videoEvent) return null;

    const cards: React.ReactNode[] = [];
    if (videoEvent) {
      const vCateUrl = videoCateMap[videoEvent.vc_id]
        ? `/video/${(videoCateMap[videoEvent.vc_id].vc_name_url || '').trim()}/${(videoEvent.video_url || '').trim()}`
        : '/videos';
      cards.push(
        <div
          key={`video-event-${focusType}`}
          className="group bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden flex flex-col"
        >
          <div className="relative h-48 overflow-hidden bg-slate-100">
            <Link to={vCateUrl} className="block w-full h-full">
              <img
                src={resolveUploadUrl(videoEvent.video_thumb)}
                alt={videoEvent.video_desc}
                className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
              />
            </Link>
            <span className="absolute top-3 left-3 bg-rose-600 text-white text-xs font-extrabold px-3 py-1 rounded-full shadow-md">
              🎬 {t('Video')}
            </span>
          </div>
          <div className="p-5 flex-1 flex flex-col justify-between">
            <div>
              <Link
                to={vCateUrl}
                className="font-extrabold text-[17px] sm:text-[18px] text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2 leading-snug mb-2"
              >
                {truncateWords(videoEvent.video_desc, 120)}
              </Link>
              <p className="text-slate-600 text-[15px] leading-relaxed line-clamp-3">
                {truncateWords(videoEvent.video_cmt, 180)}
              </p>
            </div>
            <div className="pt-4 mt-4 border-t border-slate-100">
              <Link
                to={vCateUrl}
                className="text-sm font-extrabold text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1"
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
      const card = renderNewsCateCard(nc);
      if (card) cards.push(card);
    });

    if (cards.length === 0) return null;

    return (
      <section className="space-y-5">
        <div className="flex items-center justify-between border-b border-slate-200 pb-3">
          <div className="flex items-center gap-2.5">
            <span className="w-9 h-9 rounded-xl bg-sky-100 text-[#0a5482] flex items-center justify-center text-lg shadow-2xs">
              {icon}
            </span>
            <h2 className="text-xl sm:text-2xl font-black text-slate-800 tracking-tight">{t(sectionTitleKey)}</h2>
          </div>
          <Link to="/news" className="text-sm font-bold text-[#0a5482] hover:text-[#2ab4e8] transition-colors">
            {lang === 'vi' ? 'Xem tất cả →' : 'View all →'}
          </Link>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">{cards}</div>
      </section>
    );
  };

  const curAd = ads[bannerIdx];
  const curSticky = stickyNews[stickyIdx];
  const featuredVideoParents = allVideoCategories.filter((vc) => Number(vc.vc_type) === 1);
  const focusZeroCates = newsCategories.filter(
    (nc) => Number(nc.news_cc_focus) === 0 && !!latestNewsByCate[nc.news_cc_id]
  );

  return (
    <div className="space-y-10 pb-6">
      {/* 1. HERO BANNER SLIDER (.slide-main modernized) */}
      <section className="bg-gradient-to-b from-slate-100 to-slate-50 pt-6 pb-2">
        <div className="max-w-7xl mx-auto px-4 sm:px-6">
          {curAd ? (
            <div className="rounded-3xl overflow-hidden shadow-xl border border-slate-200/80 bg-[#0f172a] grid grid-cols-1 lg:grid-cols-12 relative">
              {/* Left Banner Image (7 cols) */}
              <div className="lg:col-span-7 relative min-h-[260px] sm:min-h-[360px] bg-slate-900 overflow-hidden">
                <Link
                  to={
                    curAd.link
                      ? curAd.link.trim().replace(/^https?:\/\/(?:www\.)?tonyenglish\.vn(?:\/(?:vi|en))?/i, '') || '/courses'
                      : '/courses'
                  }
                  className="block w-full h-full"
                >
                  <img
                    src={resolveUploadUrl(curAd.image)}
                    alt={curAd.title || 'TonyEnglish'}
                    className="w-full h-full object-cover"
                  />
                </Link>

                {/* Prev / Next Controls */}
                {ads.length > 1 && (
                  <div className="absolute bottom-4 right-4 flex items-center gap-2 z-10">
                    <button
                      type="button"
                      onClick={() => setBannerIdx((prev) => (prev - 1 + ads.length) % ads.length)}
                      className="w-9 h-9 rounded-full bg-slate-900/75 hover:bg-[#2ab4e8] text-white flex items-center justify-center transition shadow-md backdrop-blur-xs"
                      title="Previous"
                    >
                      ‹
                    </button>
                    <span className="bg-slate-900/75 text-white text-xs font-bold px-3 py-1.5 rounded-full backdrop-blur-xs">
                      {bannerIdx + 1} / {ads.length}
                    </span>
                    <button
                      type="button"
                      onClick={() => setBannerIdx((prev) => (prev + 1) % ads.length)}
                      className="w-9 h-9 rounded-full bg-slate-900/75 hover:bg-[#2ab4e8] text-white flex items-center justify-center transition shadow-md backdrop-blur-xs"
                      title="Next"
                    >
                      ›
                    </button>
                  </div>
                )}
              </div>

              {/* Right Content Panel (5 cols) */}
              <div
                className="lg:col-span-5 p-6 sm:p-8 lg:p-10 flex flex-col justify-between text-white relative"
                style={{
                  background: `linear-gradient(145deg, ${(curAd.color || '#0a5482').trim()} 0%, #0f172a 100%)`,
                }}
              >
                <div className="space-y-4">
                  <div className="inline-flex items-center gap-1.5 bg-white/15 backdrop-blur-xs text-white text-[11px] font-black uppercase tracking-wider px-3 py-1 rounded-full border border-white/20">
                    <span>✨</span>
                    <span>TonyEnglish Highlights</span>
                  </div>

                  <div
                    className="text-base sm:text-[17px] font-bold leading-relaxed text-white/95 legacy-prose [&_a]:text-sky-200 [&_p]:mb-2"
                    dangerouslySetInnerHTML={{
                      __html: fixLegacyHtmlContent(
                        lang === 'vi' ? curAd.meta_vi || curAd.meta : curAd.meta || curAd.meta_vi
                      ),
                    }}
                  />

                  <div
                    className="text-xs sm:text-sm text-white/80 leading-relaxed pt-2 border-t border-white/15"
                    dangerouslySetInnerHTML={{
                      __html: fixLegacyHtmlContent(
                        lang === 'vi' ? curAd.desc_vi || curAd.desc : curAd.desc || curAd.desc_vi
                      ),
                    }}
                  />
                </div>

                <div className="pt-6 mt-6 flex flex-wrap items-center gap-3">
                  <Link
                    to="/courses"
                    className="bg-white text-[#0a5482] hover:bg-sky-50 font-black text-xs sm:text-sm px-5 py-2.5 rounded-xl shadow-lg transition active:scale-95"
                  >
                    {lang === 'vi' ? 'Khám phá Khóa học ➜' : 'Explore Courses ➜'}
                  </Link>
                  <button
                    type="button"
                    onClick={() => window.dispatchEvent(new CustomEvent('tony-open-lms'))}
                    className="bg-white/15 hover:bg-white/25 text-white border border-white/25 font-bold text-xs sm:text-sm px-4 py-2.5 rounded-xl transition active:scale-95 cursor-pointer"
                  >
                    {lang === 'vi' ? '🎓 Góc Học Viên' : '🎓 Student Portal'}
                  </button>
                </div>
              </div>
            </div>
          ) : null}

          {/* Quick Ecosystem Navigation Strip */}
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 mt-6">
            <Link
              to="/courses"
              className="bg-white hover:bg-sky-50/60 border border-slate-200/90 rounded-2xl p-4 flex items-center gap-3.5 shadow-2xs hover:shadow-md transition-all group"
            >
              <div className="w-12 h-12 rounded-xl bg-blue-100 text-[#0a5482] flex items-center justify-center text-2xl shrink-0 group-hover:scale-110 transition-transform">
                🎯
              </div>
              <div>
                <div className="font-black text-[15px] sm:text-base text-slate-800 group-hover:text-[#0a5482]">{t('Courses')}</div>
                <div className="text-xs sm:text-sm text-slate-500">
                  {lang === 'vi' ? 'Giao tiếp, TOEIC & IELTS' : 'Communication, TOEIC & IELTS'}
                </div>
              </div>
            </Link>

            <Link
              to="/news"
              className="bg-white hover:bg-sky-50/60 border border-slate-200/90 rounded-2xl p-4 flex items-center gap-3.5 shadow-2xs hover:shadow-md transition-all group"
            >
              <div className="w-12 h-12 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center text-2xl shrink-0 group-hover:scale-110 transition-transform">
                📚
              </div>
              <div>
                <div className="font-black text-[15px] sm:text-base text-slate-800 group-hover:text-[#0a5482]">{t('Library')}</div>
                <div className="text-xs sm:text-sm text-slate-500">
                  {lang === 'vi' ? 'Luyện đọc, Nghe & Từ vựng' : 'Reading, Listening & Vocab'}
                </div>
              </div>
            </Link>

            <Link
              to="/videos"
              className="bg-white hover:bg-sky-50/60 border border-slate-200/90 rounded-2xl p-4 flex items-center gap-3.5 shadow-2xs hover:shadow-md transition-all group"
            >
              <div className="w-12 h-12 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center text-2xl shrink-0 group-hover:scale-110 transition-transform">
                🎬
              </div>
              <div>
                <div className="font-black text-[15px] sm:text-base text-slate-800 group-hover:text-[#0a5482]">{t('Videos Store')}</div>
                <div className="text-xs sm:text-sm text-slate-500">
                  {lang === 'vi' ? 'Học qua Video có phụ đề' : 'Learn with subtitled videos'}
                </div>
              </div>
            </Link>

            <button
              type="button"
              onClick={() => window.dispatchEvent(new CustomEvent('tony-open-lms'))}
              className="bg-gradient-to-br from-[#0a5482] to-[#0f172a] text-white rounded-2xl p-4 flex items-center gap-3.5 shadow-md hover:shadow-xl transition-all group text-left cursor-pointer"
            >
              <div className="w-12 h-12 rounded-xl bg-[#2ab4e8] text-white flex items-center justify-center text-2xl shrink-0 group-hover:scale-110 transition-transform">
                🤖
              </div>
              <div>
                <div className="font-black text-[15px] sm:text-base text-white flex items-center gap-1">
                  <span>{lang === 'vi' ? 'Góc Học Viên & Thi AI' : 'Student Portal'}</span>
                  <span className="text-[#2ab4e8]">➜</span>
                </div>
                <div className="text-xs sm:text-sm text-sky-200">
                  {lang === 'vi' ? 'Luyện đề & Chấm chữa AI' : 'AI Practice & Smart Grading'}
                </div>
              </div>
            </button>
          </div>
        </div>
      </section>

      {/* 2. MAIN 2-COLUMN CONTENT AREA */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
          {/* LEFT MAIN COLUMN (8 cols) */}
          <div className="lg:col-span-8 space-y-12">
            {/* SECTION 1: FOCUS ON (Tiêu điểm) */}
            <section className="space-y-5">
              <div className="flex items-center justify-between border-b border-slate-200 pb-3">
                <div className="flex items-center gap-2.5">
                  <span className="w-9 h-9 rounded-xl bg-sky-100 text-[#0a5482] flex items-center justify-center text-lg shadow-2xs">
                    🔥
                  </span>
                  <h2 className="text-xl sm:text-2xl font-black text-slate-800 tracking-tight">{t('Focus on')}</h2>
                </div>
                <Link to="/news" className="text-sm font-bold text-[#0a5482] hover:text-[#2ab4e8] transition-colors">
                  {lang === 'vi' ? 'Khám phá Thư viện →' : 'Explore Library →'}
                </Link>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* 1A. Latest Sticky News Card */}
                {curSticky && (
                  <div className="group bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden flex flex-col">
                    <div className="relative h-48 overflow-hidden bg-slate-100">
                      <Link to={`/news/view/${(curSticky.news_title_url || '').trim()}`} className="block w-full h-full">
                        <img
                          src={resolveUploadUrl(curSticky.news_thumb)}
                          alt={curSticky.news_title}
                          onError={(e) => {
                            (e.currentTarget as HTMLImageElement).src = '/uploads/No_Image_Wide.svg_1.png';
                          }}
                          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                        />
                      </Link>
                      <span className="absolute top-3 left-3 bg-[#2ab4e8] text-white text-xs font-extrabold px-3 py-1 rounded-full shadow-md">
                        ⚡ {t('Lastest News')}
                      </span>
                    </div>

                    <div className="p-5 flex-1 flex flex-col justify-between">
                      <div>
                        <Link
                          to={`/news/view/${(curSticky.news_title_url || '').trim()}`}
                          className="font-extrabold text-[17px] sm:text-[18px] text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2 leading-snug mb-2"
                        >
                          {(curSticky.news_title || '').trim()}
                        </Link>
                        <p className="text-slate-600 text-[15px] leading-relaxed line-clamp-3">
                          {truncateWords(curSticky.news_desc, 160)}
                        </p>
                      </div>

                      <div className="pt-4 mt-4 border-t border-slate-100 flex items-center justify-between">
                        <Link
                          to="/news"
                          className="text-sm font-extrabold text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1"
                        >
                          <span>{t('Related Post')}</span>
                          <span>→</span>
                        </Link>
                        {stickyNews.length > 1 && (
                          <div className="flex items-center gap-1">
                            <button
                              type="button"
                              onClick={() => setStickyIdx((prev) => (prev - 1 + stickyNews.length) % stickyNews.length)}
                              className="w-7 h-7 rounded-md bg-slate-100 hover:bg-slate-200 text-slate-600 text-sm font-bold"
                            >
                              ‹
                            </button>
                            <button
                              type="button"
                              onClick={() => setStickyIdx((prev) => (prev + 1) % stickyNews.length)}
                              className="w-7 h-7 rounded-md bg-slate-100 hover:bg-slate-200 text-slate-600 text-sm font-bold"
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
                  <div className="group bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden flex flex-col">
                    <div className="relative h-48 overflow-hidden bg-slate-100">
                      <button
                        type="button"
                        onClick={() => setPopupVideo(videoFocus)}
                        className="block w-full h-full text-left relative"
                      >
                        <img
                          src={resolveUploadUrl(videoFocus.video_thumb)}
                          alt={videoFocus.video_desc}
                          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                        />
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
                          className="font-extrabold text-[17px] sm:text-[18px] text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2 leading-snug mb-2"
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
                {focusZeroCates.map((nc) => renderNewsCateCard(nc))}
              </div>
            </section>

            {/* SECTION 2: READING PRACTICE (focus = 5) */}
            {renderCategorySection(5, 'Reading Practice', '📖')}

            {/* SECTION 3: LEARNING THROUGH CONVERSATION (focus = 4) */}
            {renderCategorySection(4, 'Learning Through Conversation', '💬')}

            {/* SECTION 4: WORDS IN THE NEWS (focus = 1) */}
            {renderCategorySection(1, 'Words In The news', '📰')}

            {/* SECTION 5: VIDEOS STORE */}
            {featuredVideoParents.length > 0 && (
              <section className="space-y-5">
                <div className="flex items-center justify-between border-b border-slate-200 pb-3">
                  <div className="flex items-center gap-2.5">
                    <span className="w-9 h-9 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center text-lg shadow-2xs">
                      🎬
                    </span>
                    <h2 className="text-xl sm:text-2xl font-black text-slate-800 tracking-tight">
                      {t('Videos store')}
                    </h2>
                  </div>
                  <Link to="/videos" className="text-sm font-bold text-[#0a5482] hover:text-[#2ab4e8] transition-colors">
                    {lang === 'vi' ? 'Xem toàn bộ Kho Video →' : 'All Videos →'}
                  </Link>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
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

                    return (
                      <div
                        key={vc.vc_id}
                        className="group bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 overflow-hidden flex flex-col"
                      >
                        <div className="relative h-48 overflow-hidden bg-slate-900">
                          <Link to={targetUrl} className="block w-full h-full relative">
                            <img
                              src={resolveUploadUrl(activeSub.vc_image || vc.vc_image)}
                              alt={subTitle}
                              onError={(e) => {
                                (e.currentTarget as HTMLImageElement).src = '/uploads/No_Image_Wide.svg_1.png';
                              }}
                              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 opacity-95"
                            />
                            <div className="absolute inset-0 bg-gradient-to-t from-slate-900/60 via-transparent to-transparent flex items-center justify-center">
                              <span className="w-11 h-11 rounded-full bg-white/90 text-[#0a5482] flex items-center justify-center text-base shadow-lg group-hover:scale-110 transition-transform">
                                ▶
                              </span>
                            </div>
                          </Link>
                          <span className="absolute top-3 left-3 bg-[#0a5482]/90 backdrop-blur-xs text-white text-xs font-extrabold px-3 py-1 rounded-full shadow-md">
                            {parentTitle}
                          </span>
                        </div>

                        <div className="p-5 flex-1 flex flex-col justify-between">
                          <div>
                            <Link
                              to={targetUrl}
                              className="font-extrabold text-[17px] sm:text-[18px] text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2 leading-snug mb-2"
                            >
                              {subTitle}
                            </Link>
                            <p className="text-slate-600 text-[15px] leading-relaxed line-clamp-3">
                              {truncateWords(descText, 165)}
                            </p>
                          </div>

                          <div className="pt-4 mt-4 border-t border-slate-100">
                            <Link
                              to={targetUrl}
                              className="text-sm font-extrabold text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1"
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
            {renderCategorySection(3, 'Other learning materials', '🗂️')}
          </div>

          {/* RIGHT SIDEBAR (4 cols) */}
          <aside className="lg:col-span-4 space-y-6">
            {/* 1. ENROLMENT / OPENING CLASSES CARD */}
            <div className="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden">
              <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-6 py-4 flex items-center justify-between">
                <h3 className="text-white font-black text-base flex items-center gap-2">
                  <span>📅</span>
                  <span>{t('Enrolment')}</span>
                </h3>
                <Link to="/opening" className="text-sm font-bold text-[#2ab4e8] hover:underline">
                  {lang === 'vi' ? 'Chi tiết →' : 'More →'}
                </Link>
              </div>

              <div className="p-5 divide-y divide-slate-100">
                {openingClasses.length > 0 ? (
                  openingClasses.map((cl) => {
                    const d = cl.ug_start_date ? new Date(cl.ug_start_date) : null;
                    const dayStr = d && !isNaN(d.getTime()) ? String(d.getDate()).padStart(2, '0') : '15';
                    const monthStr =
                      d && !isNaN(d.getTime()) ? d.toLocaleDateString('en-US', { month: 'short' }) : 'Oct';
                    const displayName =
                      lang === 'vi'
                        ? cl.ug_name_long_vi || cl.ug_name_vi || cl.ug_name
                        : cl.ug_name_long || cl.ug_name || cl.ug_name_vi;

                    return (
                      <Link
                        key={cl.ug_id}
                        to={`/opening/${(cl.ug_name_url || '').trim()}`}
                        className="py-3.5 first:pt-0 last:pb-0 flex items-center gap-4 group"
                      >
                        <div className="w-14 h-14 rounded-2xl bg-sky-50 border border-sky-200 text-[#0a5482] flex flex-col items-center justify-center shrink-0 group-hover:bg-[#0a5482] group-hover:text-white transition-colors">
                          <span className="text-lg font-black leading-none">{dayStr}</span>
                          <span className="text-[11px] font-bold uppercase tracking-wider mt-0.5">{monthStr}</span>
                        </div>
                        <div className="min-w-0">
                          <span className="text-xs font-bold uppercase tracking-wider text-[#2ab4e8] block">
                            {t('Openning Class')}
                          </span>
                          <h4 className="font-extrabold text-[15px] sm:text-base text-slate-800 group-hover:text-[#0a5482] transition-colors line-clamp-2">
                            {displayName}
                          </h4>
                        </div>
                      </Link>
                    );
                  })
                ) : (
                  <p className="text-base text-slate-500 py-2">{t('There are no public courses.')}</p>
                )}
              </div>
            </div>

            {/* 2. TESTIMONIALS POSITION 0 */}
            {testiPos0.map((testValue) => {
              const title =
                lang === 'vi'
                  ? testValue.testimonial_title_vi || testValue.testimonial_title_en
                  : testValue.testimonial_title_en || testValue.testimonial_title_vi;
              const contentHtml =
                lang === 'vi'
                  ? testValue.testimonial_content_vi || testValue.testimonial_content_en
                  : testValue.testimonial_content_en || testValue.testimonial_content_vi;
              return (
                <div
                  key={testValue.testimonial_id}
                  className="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden"
                >
                  {title && title.trim() !== '' && (
                    <div className="px-6 py-4 bg-slate-50 border-b border-slate-200">
                      <h3 className="font-black text-slate-800 text-base">{title}</h3>
                    </div>
                  )}
                  <div
                    className="p-5 legacy-prose"
                    dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(contentHtml) }}
                  />
                </div>
              );
            })}

            {/* 3. TESTIMONIALS POSITION 1 */}
            {testiPos1.map((testValue) => {
              const title =
                lang === 'vi'
                  ? testValue.testimonial_title_vi || testValue.testimonial_title_en
                  : testValue.testimonial_title_en || testValue.testimonial_title_vi;
              const contentHtml =
                lang === 'vi'
                  ? testValue.testimonial_content_vi || testValue.testimonial_content_en
                  : testValue.testimonial_content_en || testValue.testimonial_content_vi;
              return (
                <div
                  key={testValue.testimonial_id}
                  className="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden"
                >
                  {title && title.trim() !== '' && (
                    <div className="px-6 py-4 bg-slate-50 border-b border-slate-200">
                      <h3 className="font-black text-slate-800 text-base">{title}</h3>
                    </div>
                  )}
                  <div
                    className="p-5 legacy-prose"
                    dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(contentHtml) }}
                  />
                </div>
              );
            })}
          </aside>
        </div>
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
                className="w-8 h-8 rounded-full bg-slate-100 hover:bg-rose-500 hover:text-white text-slate-600 font-bold flex items-center justify-center transition-colors shrink-0"
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
