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
  Play,
  Calendar,
  MessageCircle,
  Globe,
  Layers,
  Award,
  MapPin,
  ChevronLeft,
  ChevronRight,
} from 'lucide-react';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import { resolveUploadUrl, truncateWords, getYoutubeEmbedUrl, fixLegacyHtmlContent, updatePageSeo } from '../lib/utils';

export const HomePage: React.FC = () => {
  const { lang, t } = useApp();

  useEffect(() => {
    updatePageSeo(
      '',
      'TonyEnglish.vn - Trang học liệu cá nhân & Gia sư 1 kèm 1 cùng Thầy Tony (Tiếng Anh Giao tiếp, IELTS, Cambridge IGCSE tại nhà riêng R2B Royal City & Online).'
    );
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
  const renderCategorySection = (focusType: number, sectionTitleKey: string, icon: React.ReactNode) => {
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
    <div className="space-y-12 pb-8">
      {/* 1. MODERN EDTECH FLAGSHIP HERO + DYNAMIC SHOWCASE */}
      <section className="relative overflow-hidden bg-gradient-to-br from-[#06283d] via-[#0a5482] to-[#0f172a] text-white pt-8 pb-10 sm:pt-12 sm:pb-14 border-b border-slate-800/60">
        {/* Ambient Decorative Glows */}
        <div className="absolute -top-32 -left-24 w-96 h-96 bg-[#2ab4e8]/20 blur-3xl rounded-full pointer-events-none" />
        <div className="absolute -bottom-32 right-0 w-[28rem] h-[28rem] bg-amber-400/10 blur-3xl rounded-full pointer-events-none" />

        <div className="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-center">
            {/* Left Value Proposition (7 cols) */}
            <div className="lg:col-span-7 space-y-5">
              <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/15 px-3.5 py-1.5 rounded-full text-xs font-bold text-sky-200">
                <MapPin className="w-3.5 h-3.5 text-[#2ab4e8] shrink-0" />
                <span>
                  {lang === 'vi'
                    ? 'Gia sư 1 kèm 1 & Nhóm nhỏ • R2B Royal City, Hà Nội & Online'
                    : '1-on-1 & Small Group Tutoring • Royal City Hanoi & Online'}
                </span>
              </div>

              <h1 className="font-display font-black text-[28px] sm:text-[38px] xl:text-[44px] leading-[1.15] tracking-tight text-white">
                {lang === 'vi' ? (
                  <>
                    Chinh phục <span className="text-[#2ab4e8]">IELTS</span>,{' '}
                    <span className="text-amber-300">Cambridge IGCSE</span> &amp; Giao tiếp thực chiến cùng Thầy Tony
                  </>
                ) : (
                  <>
                    Master <span className="text-[#2ab4e8]">IELTS</span>,{' '}
                    <span className="text-amber-300">Cambridge IGCSE</span> &amp; Real-World English with Teacher Tony
                  </>
                )}
              </h1>

              <p className="text-slate-200/90 text-[15px] sm:text-[16.5px] leading-relaxed max-w-2xl">
                {lang === 'vi'
                  ? 'Kết hợp sự kèm cặp sát sao từng buổi của Thầy Tony với Hệ sinh thái Phòng học thông minh: Bài giảng song ngữ bám sát Syllabus, Kho đề Past Papers kèm Video chữa bài Full HD & Phòng thi AI chấm chữa 24/7.'
                  : 'Combining personalized 1-on-1 mentoring with an AI-powered Learning Portal: Bilingual syllabus lectures, Full HD past-paper video walkthroughs, and 24/7 AI exam grading.'}
              </p>

              {/* Primary & Secondary CTAs */}
              <div className="pt-1 flex flex-wrap items-center gap-3">
                <button
                  type="button"
                  onClick={() => window.dispatchEvent(new CustomEvent('tony-open-lms', { detail: 'register' }))}
                  className="bg-gradient-to-r from-amber-400 via-yellow-400 to-amber-500 hover:from-amber-500 hover:to-yellow-500 text-slate-950 font-extrabold text-sm sm:text-[15px] px-5 sm:px-6 py-3.5 rounded-2xl shadow-lg transition-all active:scale-95 inline-flex items-center gap-2 cursor-pointer"
                >
                  <Sparkles className="w-4 h-4" />
                  <span>{lang === 'vi' ? 'Vào Học Thử & Làm Đề Ngay' : 'Start Free Trial Now'}</span>
                  <ArrowRight className="w-4 h-4" />
                </button>

                <Link
                  to="/courses"
                  className="bg-white/12 hover:bg-white/22 text-white border border-white/25 font-bold text-sm sm:text-[15px] px-5 py-3.5 rounded-2xl backdrop-blur-xs transition-all active:scale-95 inline-flex items-center gap-2"
                >
                  <BookOpen className="w-4 h-4 text-[#2ab4e8]" />
                  <span>{lang === 'vi' ? 'Các Khóa Học' : 'Explore Courses'}</span>
                </Link>

                <a
                  href="https://zalo.me/0935058688"
                  target="_blank"
                  rel="noreferrer"
                  className="text-xs sm:text-sm font-bold text-sky-200 hover:text-white px-3 py-2 inline-flex items-center gap-1.5 transition-colors"
                >
                  <MessageCircle className="w-4 h-4 text-[#2ab4e8]" />
                  <span>Zalo tư vấn: 0935 058 688</span>
                </a>
              </div>

              {/* 4 Key Proof Metrics */}
              <div className="pt-3 grid grid-cols-2 sm:grid-cols-4 gap-2.5 sm:gap-3">
                <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-2xl px-3.5 py-2.5">
                  <div className="font-display font-black text-lg sm:text-xl text-white">2013–2026</div>
                  <div className="text-[11px] sm:text-xs text-sky-200/85 font-medium">Kinh nghiệm giảng dạy</div>
                </div>
                <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-2xl px-3.5 py-2.5">
                  <div className="font-display font-black text-lg sm:text-xl text-[#2ab4e8]">6.5 – 8.0+</div>
                  <div className="text-[11px] sm:text-xs text-sky-200/85 font-medium">Mục tiêu đầu ra IELTS</div>
                </div>
                <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-2xl px-3.5 py-2.5">
                  <div className="font-display font-black text-lg sm:text-xl text-amber-300">A / A*</div>
                  <div className="text-[11px] sm:text-xs text-sky-200/85 font-medium">Đầu ra Cambridge IGCSE</div>
                </div>
                <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-2xl px-3.5 py-2.5">
                  <div className="font-display font-black text-lg sm:text-xl text-emerald-300">Full HD + AI</div>
                  <div className="text-[11px] sm:text-xs text-sky-200/85 font-medium">Video giải đề &amp; Trợ lý 24/7</div>
                </div>
              </div>
            </div>

            {/* Right Showcase Frame (5 cols): Dynamic Banner Slider or Smart LMS Card */}
            <div className="lg:col-span-5">
              {curAd ? (
                <div className="rounded-3xl overflow-hidden bg-slate-900/85 backdrop-blur-md border border-white/20 shadow-2xl flex flex-col">
                  <div className="relative aspect-[16/9] bg-slate-950 overflow-hidden">
                    {ads.map((adItem, idx) => {
                      const isActive = idx === bannerIdx;
                      const targetLink = adItem.link
                        ? adItem.link.trim().replace(/^https?:\/\/(?:www\.)?tonyenglish\.vn(?:\/(?:vi|en))?/i, '') || '/courses'
                        : '/courses';
                      return (
                        <Link
                          key={adItem.ad_id || idx}
                          to={targetLink}
                          className={`absolute inset-0 block w-full h-full transition-opacity duration-500 ${
                            isActive ? 'opacity-100 z-[1]' : 'opacity-0 pointer-events-none z-0'
                          }`}
                        >
                          <img
                            src={resolveUploadUrl(adItem.image)}
                            alt={adItem.title || 'TonyEnglish'}
                            className="w-full h-full object-cover object-center"
                          />
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
                        <span className="bg-slate-900/80 text-white text-[11px] font-bold px-2.5 py-1 rounded-full backdrop-blur-xs">
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

                  <div className="p-5 sm:p-6 space-y-3 bg-gradient-to-b from-slate-900/95 to-[#0f172a]">
                    <div className="flex items-center justify-between gap-2">
                      <span className="inline-flex items-center gap-1.5 text-[11px] font-extrabold uppercase tracking-wider text-[#2ab4e8] bg-sky-500/15 border border-sky-400/25 px-2.5 py-0.5 rounded-full">
                        <Sparkles className="w-3 h-3" />
                        <span>Tiêu điểm TonyEnglish</span>
                      </span>
                      <button
                        type="button"
                        onClick={() => window.dispatchEvent(new CustomEvent('tony-open-lms'))}
                        className="text-xs font-extrabold text-amber-300 hover:text-amber-200 inline-flex items-center gap-1 cursor-pointer"
                      >
                        <GraduationCap className="w-3.5 h-3.5" />
                        <span>Mở Góc Học Viên →</span>
                      </button>
                    </div>

                    <div
                      className="text-[14.5px] sm:text-[15.5px] font-bold leading-relaxed text-white/95 legacy-prose [&_a]:text-sky-300 [&_p]:mb-1.5 line-clamp-2"
                      dangerouslySetInnerHTML={{
                        __html: fixLegacyHtmlContent(
                          lang === 'vi' ? curAd.meta_vi || curAd.meta : curAd.meta || curAd.meta_vi
                        ).replace(/^(?:\s*<br\s*\/?>\s*)+/i, ''),
                      }}
                    />

                    <div
                      className="text-xs text-slate-300/85 leading-relaxed pt-2.5 border-t border-white/10 line-clamp-2"
                      dangerouslySetInnerHTML={{
                        __html: fixLegacyHtmlContent(
                          lang === 'vi' ? curAd.desc_vi || curAd.desc : curAd.desc || curAd.desc_vi
                        ).replace(/^(?:\s*<br\s*\/?>\s*)+/i, ''),
                      }}
                    />
                  </div>
                </div>
              ) : (
                <div className="rounded-3xl bg-white/10 backdrop-blur-md border border-white/20 p-6 sm:p-7 shadow-2xl space-y-4">
                  <div className="inline-flex items-center gap-2 text-xs font-extrabold uppercase tracking-wider text-amber-300 bg-amber-400/15 border border-amber-300/30 px-3 py-1 rounded-full">
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

      {/* 1B. BENTO GRID: 4 TRỤ CỘT ĐÀO TẠO & HỆ SINH THÁI TONYENGLISH */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 -mt-4 sm:-mt-6 relative z-20">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <Link
            to="/igcse"
            className="bg-white hover:bg-sky-50/40 border border-slate-200/90 hover:border-[#2ab4e8] rounded-2xl p-5 shadow-xs hover:shadow-soft transition-all group flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between mb-3.5">
                <div className="w-11 h-11 rounded-xl bg-amber-50 border border-amber-200/80 text-amber-700 flex items-center justify-center group-hover:scale-105 transition-transform">
                  <Award className="w-5 h-5" />
                </div>
                <span className="text-[11px] font-extrabold uppercase tracking-wider text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded-full border border-amber-200/70">
                  Cambridge IGCSE
                </span>
              </div>
              <h3 className="font-display font-extrabold text-[16.5px] text-slate-900 group-hover:text-[#0a5482] mb-1.5">
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
            className="bg-white hover:bg-sky-50/40 border border-slate-200/90 hover:border-[#2ab4e8] rounded-2xl p-5 shadow-xs hover:shadow-soft transition-all group flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between mb-3.5">
                <div className="w-11 h-11 rounded-xl bg-sky-50 border border-sky-200/80 text-[#0a5482] flex items-center justify-center group-hover:scale-105 transition-transform">
                  <Target className="w-5 h-5" />
                </div>
                <span className="text-[11px] font-extrabold uppercase tracking-wider text-[#0a5482] bg-sky-50 px-2.5 py-0.5 rounded-full border border-sky-200/70">
                  Band 6.5 – 8.0+
                </span>
              </div>
              <h3 className="font-display font-extrabold text-[16.5px] text-slate-900 group-hover:text-[#0a5482] mb-1.5">
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
            to="/courses"
            className="bg-white hover:bg-sky-50/40 border border-slate-200/90 hover:border-[#2ab4e8] rounded-2xl p-5 shadow-xs hover:shadow-soft transition-all group flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between mb-3.5">
                <div className="w-11 h-11 rounded-xl bg-emerald-50 border border-emerald-200/80 text-emerald-700 flex items-center justify-center group-hover:scale-105 transition-transform">
                  <MessageCircle className="w-5 h-5" />
                </div>
                <span className="text-[11px] font-extrabold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200/70">
                  1-on-1 VIP
                </span>
              </div>
              <h3 className="font-display font-extrabold text-[16.5px] text-slate-900 group-hover:text-[#0a5482] mb-1.5">
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
            className="bg-gradient-to-br from-[#0a5482] to-[#0f172a] text-white rounded-2xl p-5 shadow-md hover:shadow-xl hover:-translate-y-0.5 transition-all group text-left flex flex-col justify-between cursor-pointer border border-sky-400/20"
          >
            <div>
              <div className="flex items-center justify-between mb-3.5">
                <div className="w-11 h-11 rounded-xl bg-[#2ab4e8] text-white flex items-center justify-center group-hover:scale-105 transition-transform shadow-sm">
                  <Bot className="w-5 h-5" />
                </div>
                <span className="text-[11px] font-extrabold uppercase tracking-wider text-amber-300 bg-white/10 px-2.5 py-0.5 rounded-full border border-white/15">
                  Smart LMS
                </span>
              </div>
              <h3 className="font-display font-extrabold text-[16.5px] text-white mb-1.5">
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

      {/* 2. MAIN 2-COLUMN CONTENT AREA */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
          {/* LEFT MAIN COLUMN (8 cols) */}
          <div className="lg:col-span-8 space-y-12">
            {/* SECTION 1: FOCUS ON (Tiêu điểm) */}
            <section className="space-y-5">
              <div className="flex items-center justify-between border-b border-slate-200 pb-3">
                <div className="flex items-center gap-2.5">
                  <span className="w-9 h-9 rounded-xl bg-sky-100 text-[#0a5482] flex items-center justify-center shadow-2xs">
                    <Sparkles className="w-4 h-4" />
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
            {renderCategorySection(5, 'Reading Practice', <BookOpen className="w-4 h-4" />)}

            {/* SECTION 3: LEARNING THROUGH CONVERSATION (focus = 4) */}
            {renderCategorySection(4, 'Learning Through Conversation', <MessageCircle className="w-4 h-4" />)}

            {/* SECTION 4: WORDS IN THE NEWS (focus = 1) */}
            {renderCategorySection(1, 'Words In The news', <Globe className="w-4 h-4" />)}

            {/* SECTION 5: VIDEOS STORE */}
            {featuredVideoParents.length > 0 && (
              <section className="space-y-5">
                <div className="flex items-center justify-between border-b border-slate-200 pb-3">
                  <div className="flex items-center gap-2.5">
                    <span className="w-9 h-9 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center shadow-2xs">
                      <Video className="w-4 h-4" />
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
            {renderCategorySection(3, 'Other learning materials', <Layers className="w-4 h-4" />)}
          </div>

          {/* RIGHT SIDEBAR (4 cols) */}
          <aside className="lg:col-span-4 space-y-6">
            {/* 1. ENROLMENT / OPENING CLASSES CARD */}
            <div className="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden">
              <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-6 py-4 flex items-center justify-between">
                <h3 className="text-white font-black text-base flex items-center gap-2">
                  <Calendar className="w-4 h-4 text-[#2ab4e8]" />
                  <span>{t('Enrolment')}</span>
                </h3>
                <Link to="/opening" className="text-sm font-bold text-[#2ab4e8] hover:underline">
                  {lang === 'vi' ? 'Chi tiết →' : 'More →'}
                </Link>
              </div>

              <div className="p-5 space-y-4">
                <div className="bg-sky-50/90 border border-sky-200/80 rounded-xl p-3.5">
                  <div className="flex items-center gap-2 text-xs font-black uppercase tracking-wider text-[#0a5482] mb-1">
                    <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" />
                    <span>{lang === 'vi' ? 'Thông báo tuyển sinh' : 'Enrollment Notice'}</span>
                  </div>
                  <p className="text-sm sm:text-[15px] font-bold text-slate-800 leading-snug">
                    {lang === 'vi'
                      ? 'Liên tục tuyển sinh gia sư các gói học 1 kèm 1 cho Giao tiếp tiếng Anh, IELTS, IGCSE.'
                      : 'Continuous 1-on-1 private tutoring enrollment for English Communication, IELTS, and IGCSE.'}
                  </p>
                </div>

                <div className="divide-y divide-slate-100">
                  <Link
                    to="/courses/english-communication 1"
                    className="py-3 first:pt-0 last:pb-0 flex items-center gap-3.5 group"
                  >
                    <div className="w-13 h-13 rounded-2xl bg-indigo-50 border border-indigo-200 text-indigo-700 flex flex-col items-center justify-center shrink-0 group-hover:bg-[#0a5482] group-hover:text-white group-hover:border-[#0a5482] transition-colors">
                      <span className="text-base font-black leading-none">1-1</span>
                      <span className="text-[10px] font-bold uppercase tracking-wider mt-0.5">VIP</span>
                    </div>
                    <div className="min-w-0">
                      <span className="text-[11px] font-bold uppercase tracking-wider text-[#2ab4e8] block">
                        {lang === 'vi' ? 'Gia sư tại nhà Thầy & Online' : '1-on-1 Private Tutoring'}
                      </span>
                      <h4 className="font-extrabold text-[15px] text-slate-800 group-hover:text-[#0a5482] transition-colors leading-snug">
                        {lang === 'vi' ? 'Giao tiếp Tiếng Anh (1 kèm 1)' : '1-on-1 English Communication'}
                      </h4>
                      <p className="text-xs text-slate-500 mt-0.5 line-clamp-1">
                        {lang === 'vi'
                          ? 'Phát âm chuẩn IPA, luyện phản xạ & tình huống thực tế'
                          : 'IPA pronunciation, reflex & real-life communication'}
                      </p>
                    </div>
                  </Link>

                  <Link
                    to="/courses/ielts"
                    className="py-3 first:pt-0 last:pb-0 flex items-center gap-3.5 group"
                  >
                    <div className="w-13 h-13 rounded-2xl bg-sky-50 border border-sky-200 text-[#0a5482] flex flex-col items-center justify-center shrink-0 group-hover:bg-[#0a5482] group-hover:text-white transition-colors">
                      <span className="text-base font-black leading-none">1-1</span>
                      <span className="text-[10px] font-bold uppercase tracking-wider mt-0.5">IELTS</span>
                    </div>
                    <div className="min-w-0">
                      <span className="text-[11px] font-bold uppercase tracking-wider text-[#2ab4e8] block">
                        {lang === 'vi' ? 'Gia sư tại nhà Thầy & Online' : '1-on-1 Private Tutoring'}
                      </span>
                      <h4 className="font-extrabold text-[15px] text-slate-800 group-hover:text-[#0a5482] transition-colors leading-snug">
                        {lang === 'vi' ? 'Luyện thi IELTS (1 kèm 1)' : '1-on-1 IELTS Preparation'}
                      </h4>
                      <p className="text-xs text-slate-500 mt-0.5 line-clamp-1">
                        {lang === 'vi'
                          ? 'Lộ trình cá nhân hóa 4 kỹ năng cam kết đầu ra Band 6.5 - 8.0+'
                          : 'Personalized 4-skill roadmap for Band 6.5 - 8.0+'}
                      </p>
                    </div>
                  </Link>

                  <Link
                    to="/courses/luyen-thi-igcse-alevel-cap-toc"
                    className="py-3 first:pt-0 last:pb-0 flex items-center gap-3.5 group"
                  >
                    <div className="w-13 h-13 rounded-2xl bg-amber-50 border border-amber-200 text-amber-700 flex flex-col items-center justify-center shrink-0 group-hover:bg-[#0a5482] group-hover:text-white group-hover:border-[#0a5482] transition-colors">
                      <span className="text-base font-black leading-none">1-1</span>
                      <span className="text-[10px] font-bold uppercase tracking-wider mt-0.5">IGCSE</span>
                    </div>
                    <div className="min-w-0">
                      <span className="text-[11px] font-bold uppercase tracking-wider text-[#2ab4e8] block">
                        {lang === 'vi' ? 'Gia sư tại nhà Thầy & Online' : '1-on-1 Private Tutoring'}
                      </span>
                      <h4 className="font-extrabold text-[15px] text-slate-800 group-hover:text-[#0a5482] transition-colors leading-snug">
                        {lang === 'vi' ? 'Chương trình Quốc tế IGCSE (1 kèm 1)' : '1-on-1 Cambridge IGCSE'}
                      </h4>
                      <p className="text-xs text-slate-500 mt-0.5 line-clamp-1">
                        {lang === 'vi'
                          ? 'Sciences, Maths, Economics, Business, Geography & ESL'
                          : 'Sciences, Maths, Economics, Business, Geography & ESL'}
                      </p>
                    </div>
                  </Link>
                </div>
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
