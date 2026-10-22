import React, { useEffect, useState } from 'react';
import { Link, useParams, useNavigate } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import { resolveUploadUrl, getYoutubeEmbedUrl, fixLegacyHtmlContent, updatePageSeo } from '../lib/utils';

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
        <aside className="w-full lg:w-[260px] xl:w-[270px] shrink-0 bg-white rounded-2xl border border-slate-200/80 shadow-2xs overflow-hidden lg:sticky lg:top-24">
          <button
            type="button"
            onClick={() => setMobileCateOpen((prev) => !prev)}
            className="w-full bg-slate-100/80 px-4 py-3 border-b border-slate-200/70 flex items-center justify-between lg:pointer-events-none cursor-pointer text-left"
          >
            <h2 className="text-slate-600 lg:text-slate-500 font-bold text-xs uppercase tracking-widest flex items-center gap-2 min-w-0">
              <span className="opacity-80 shrink-0">🎬</span>
              <span className="shrink-0">{t('Video Menu')}</span>
              {activeCate && (
                <span className="lg:hidden font-semibold text-[#0a5482] normal-case tracking-normal truncate">
                  • {mainHeading}
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
                to="/videos"
                onClick={() => setMobileCateOpen(false)}
                className={`block px-3.5 py-2.5 rounded-xl transition-colors ${
                  !cateSlug
                    ? 'bg-sky-50/90 text-[#0a5482] font-semibold border-l-[3px] border-[#2ab4e8]'
                    : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                }`}
              >
                📺 {t('Video Category')}
              </Link>
            </li>
            {topCategories.map((vc) => {
              const isSelected =
                (vc.vc_name_url || '').trim() === cleanCateParam ||
                (parentCate && Number(parentCate.vc_id) === Number(vc.vc_id));
              return (
                <li key={vc.vc_id}>
                  <Link
                    to={`/videos/${(vc.vc_name_url || '').trim()}`}
                    onClick={() => setMobileCateOpen(false)}
                    className={`block px-3.5 py-2.5 rounded-xl transition-colors ${
                      isSelected
                        ? 'bg-sky-50/90 text-[#0a5482] font-semibold border-l-[3px] border-[#2ab4e8]'
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
                /* VIDEO CATEGORY GRID */
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                  {subCatesToDisplay.map((sub) => {
                    const childVideos = allVideoCates.filter((c) => Number(c.vc_parent) === Number(sub.vc_id));
                    const imgPath =
                      childVideos.find((c) => c.vc_image)?.vc_image || sub.vc_image || 'No_Image_Wide.svg_1.png';
                    const subTitle = lang === 'vi' ? sub.vc_name_vi || sub.vc_name : sub.vc_name;
                    const targetRoute = activeCate
                      ? `/video/${(sub.vc_name_url || '').trim()}`
                      : `/videos/${(sub.vc_name_url || '').trim()}`;

                    return (
                      <Link
                        key={sub.vc_id}
                        to={targetRoute}
                        className="group bg-white rounded-2xl border border-slate-200/80 overflow-hidden shadow-2xs hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col"
                      >
                        <div className="relative h-44 bg-slate-900 overflow-hidden">
                          <img
                            src={resolveUploadUrl(imgPath)}
                            alt={subTitle}
                            onError={(e) => {
                              (e.currentTarget as HTMLImageElement).src = '/uploads/No_Image_Wide.svg_1.png';
                            }}
                            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 opacity-95"
                          />
                          <div className="absolute inset-0 bg-gradient-to-t from-slate-900/70 via-transparent to-transparent flex items-center justify-center">
                            <span className="w-11 h-11 rounded-full bg-white/90 text-[#0a5482] flex items-center justify-center text-base shadow-lg group-hover:scale-110 transition-transform">
                              ▶
                            </span>
                          </div>
                        </div>
                        <div className="p-4 flex-1 flex items-center justify-between gap-2">
                          <h3 className="font-extrabold text-[15px] sm:text-base text-slate-800 group-hover:text-[#0a5482] line-clamp-2">
                            {subTitle}
                          </h3>
                          <span className="text-[#2ab4e8] font-black shrink-0">→</span>
                        </div>
                      </Link>
                    );
                  })}
                </div>
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

                      {/* Interactive Question / Answer / Subtitles */}
                      <div className="space-y-3">
                        {currentVideo.video_question && currentVideo.video_question.trim() !== '' && (
                          <div className="bg-sky-50/40 rounded-2xl border border-sky-200/80 overflow-hidden">
                            <button
                              type="button"
                              onClick={() => {
                                setShowQuestion(!showQuestion);
                                if (showQuestion) setShowAnswer(false);
                              }}
                              className="w-full px-5 py-4 flex items-center justify-between text-left font-bold text-[15.5px] sm:text-base text-[#0a5482] hover:bg-sky-50/80 transition"
                            >
                              <span>❓ {t('View Question')}</span>
                              <span className="text-xs">{showQuestion ? '▲' : '▼'}</span>
                            </button>

                            {showQuestion && (
                              <div className="p-5 pt-3 bg-white border-t border-sky-100 space-y-4">
                                <div
                                  className="legacy-prose"
                                  dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(currentVideo.video_question) }}
                                />
                                {currentVideo.video_answer && currentVideo.video_answer.trim() !== '' && (
                                  <div>
                                    <button
                                      type="button"
                                      onClick={() => setShowAnswer(!showAnswer)}
                                      className="bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm px-4 py-2 rounded-xl transition"
                                    >
                                      ✅ {t('View Answer')}
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
                        )}

                        {currentVideo.video_conversation && currentVideo.video_conversation.trim() !== '' && (
                          <div className="bg-sky-50/40 rounded-2xl border border-sky-200/80 overflow-hidden">
                            <button
                              type="button"
                              onClick={() => setShowSubtitles(!showSubtitles)}
                              className="w-full px-5 py-4 flex items-center justify-between text-left font-bold text-[15.5px] sm:text-base text-[#0a5482] hover:bg-sky-50/80 transition"
                            >
                              <span>💬 {t('Same video with subtitles')}</span>
                              <span className="text-xs">{showSubtitles ? '▲' : '▼'}</span>
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
                <span className="opacity-70 text-sm">🎞️</span>
                <span>{t('Video List')}</span>
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
                {videosInCate
                  .filter((vd) => !currentVideo || vd.video_id !== currentVideo.video_id)
                  .map((vd) => (
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
                      </div>
                      <div className="p-3.5">
                        <h4 className="font-medium text-sm sm:text-[14.5px] text-slate-500 group-hover:text-[#0a5482] line-clamp-2 transition-colors">
                          {vd.video_desc}
                        </h4>
                      </div>
                    </Link>
                  ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
