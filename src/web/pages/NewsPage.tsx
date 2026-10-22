import React, { useEffect, useState } from 'react';
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

export const NewsPage: React.FC<{ mode: 'list' | 'detail' }> = ({ mode }) => {
  const { slug } = useParams<{ slug?: string }>();
  const [searchParams, setSearchParams] = useSearchParams();
  const { lang, t, user } = useApp();

  const pageParam = parseInt(searchParams.get('page') || '1', 10) || 1;
  const searchQuery = searchParams.get('q') || '';

  const [allCategories, setAllCategories] = useState<any[]>([]);
  const [openParentId, setOpenParentId] = useState<number | null>(null);

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

          const from = (pageParam - 1) * pageSize;
          const to = from + pageSize - 1;

          const { data, count } = await supabase
            .from('te_news')
            .select(
              'news_id,news_desc,news_title,news_created_at,news_title_url,news_thumb,news_postday,news_byname,public',
              { count: 'exact' }
            )
            .eq('deleted', 0)
            .eq('news_status', 1)
            .in('news_cc_id', cateIds)
            .order('news_id', { ascending: false })
            .range(from, to);

          setNewsList(data || []);
          setTotalCount(count || 0);
        } else {
          const from = (pageParam - 1) * pageSize;
          const to = from + pageSize - 1;
          let query = supabase
            .from('te_news')
            .select(
              'news_id,news_desc,news_title,news_created_at,news_title_url,news_thumb,news_postday,news_byname,public',
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
            .select('news_id,news_title,news_title_url')
            .eq('deleted', 0)
            .eq('news_status', 1)
            .eq('news_cc_id', found.news_cc_id)
            .neq('news_id', found.news_id)
            .order('news_id', { ascending: false })
            .limit(10);
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

  const totalPages = Math.max(1, Math.ceil(totalCount / pageSize));

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
    <div className="max-w-7xl mx-auto px-4 sm:px-6 py-8">
      {/* BREADCRUMB */}
      <nav className="flex items-center gap-2 text-sm sm:text-[15px] font-semibold text-slate-500 mb-6 flex-wrap">
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

      <div className="flex flex-col lg:flex-row gap-8 xl:gap-12 items-start">
        {/* LEFT SIDEBAR: SUBTLE, NON-COMPETING LIBRARY MENU */}
        <aside className="w-full lg:w-[260px] xl:w-[270px] shrink-0 bg-white/80 rounded-2xl border border-slate-200/70 overflow-hidden sticky top-24">
          <div className="bg-slate-100/80 px-4 py-3 border-b border-slate-200/70">
            <h2 className="text-slate-500 font-bold text-xs uppercase tracking-widest flex items-center gap-2">
              <span className="opacity-80">📚</span>
              <span>{t('Library')}</span>
            </h2>
          </div>

          <ul className="divide-y divide-slate-100 text-[14.5px] p-1.5">
            <li>
              <Link
                to="/news"
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
                    onClick={() => setOpenParentId(parent.news_cc_id)}
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
                className="block px-3.5 py-2.5 rounded-xl font-medium text-slate-600 hover:text-[#0a5482] hover:bg-slate-50 transition-colors"
              >
                🎬 {t('Videos store')} →
              </Link>
            </li>
          </ul>
        </aside>

        {/* RIGHT MAIN CONTENT */}
        <div className="flex-1 min-w-0 w-full space-y-6">
          <div className="bg-white rounded-3xl border border-slate-200/90 shadow-sm overflow-hidden">
            {/* Section Header */}
            <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-6 sm:px-8 py-6 text-white flex items-center justify-between flex-wrap gap-4">
              <div>
                <div className="text-xs sm:text-sm font-extrabold uppercase tracking-widest text-[#2ab4e8] mb-1">
                  TonyEnglish Learning Library
                </div>
                <h1 className="text-2xl sm:text-3xl font-black tracking-tight">{cateDisplayName}</h1>
              </div>
              {mode === 'list' && totalCount > 0 && (
                <span className="bg-white/15 text-white text-sm font-bold px-4 py-1.5 rounded-full border border-white/20">
                  {totalCount} {lang === 'vi' ? 'bài học' : 'articles'}
                </span>
              )}
            </div>

            <div className="p-6 sm:p-8">
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
                        return (
                          <div
                            key={item.news_id}
                            className="group bg-white hover:bg-slate-50/70 rounded-2xl border border-slate-200/80 p-4 sm:p-5 flex flex-col sm:flex-row gap-5 transition-all hover:shadow-md"
                          >
                            <Link
                              to={itemUrl}
                              className="w-full sm:w-56 h-44 sm:h-36 rounded-xl overflow-hidden bg-slate-100 shrink-0 block"
                            >
                              <img
                                src={resolveUploadUrl(item.news_thumb)}
                                alt={item.news_title}
                                onError={(e) => {
                                  (e.currentTarget as HTMLImageElement).src = '/uploads/No_Image_Wide.svg_1.png';
                                }}
                                className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
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

                  {/* Audio Player Box */}
                  {article.news_audio_file && article.news_audio_file.trim() !== '' && (
                    <div className="bg-gradient-to-r from-sky-50 to-slate-50 border border-sky-200/80 rounded-2xl p-4 sm:p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                      <div className="flex items-center gap-3.5">
                        <span className="w-11 h-11 rounded-xl bg-[#0a5482] text-white flex items-center justify-center text-xl shadow-xs">
                          🎧
                        </span>
                        <div>
                          <div className="font-black text-base text-[#0a5482]">Audio Luyện Nghe</div>
                          <div className="text-sm text-slate-500">Bấm Play để vừa nghe vừa đọc bài</div>
                        </div>
                      </div>
                      {!showAudioPlayer ? (
                        <button
                          type="button"
                          onClick={() => setShowAudioPlayer(true)}
                          className="bg-[#2ab4e8] hover:bg-[#0a5482] text-white font-black text-sm px-5 py-2.5 rounded-xl shadow-xs transition"
                        >
                          ▶ Nghe Audio (Listen)
                        </button>
                      ) : (
                        <audio
                          controls
                          autoPlay
                          src={resolveUploadUrl(article.news_audio_file, '')}
                          className="w-full sm:w-80 h-10"
                        />
                      )}
                    </div>
                  )}

                  {/* Lead / Intro */}
                  {article.news_desc && (
                    <div
                      className="p-5 bg-slate-50 rounded-2xl border-l-4 border-[#2ab4e8] italic font-medium text-slate-700 legacy-prose"
                      dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(article.news_desc) }}
                    />
                  )}

                  {/* Featured Image if enabled */}
                  {article.news_thumb && Number(article.news_status_avatar) === 1 && (
                    <figure className="rounded-2xl overflow-hidden bg-slate-100 border border-slate-200 max-w-xl mx-auto">
                      <img
                        src={resolveUploadUrl(article.news_thumb)}
                        alt={article.news_title}
                        className="w-full h-auto object-cover"
                      />
                      {article.news_desc_thumb && (
                        <figcaption className="p-3 text-center text-sm italic text-slate-500">
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
                          <div className="space-y-4 pt-5 border-t border-slate-200">
                            {vocabItems.length > 0 && (
                              <div className="bg-slate-50/90 rounded-2xl border border-slate-200/90 overflow-hidden shadow-2xs">
                                <button
                                  type="button"
                                  onClick={() => setShowVocab(!showVocab)}
                                  className="w-full px-5 py-4 flex items-center justify-between text-left hover:bg-sky-50/70 transition group"
                                >
                                  <div className="flex items-center gap-3 flex-wrap">
                                    <span className="w-9 h-9 rounded-xl bg-[#0a5482] text-white flex items-center justify-center text-base shadow-2xs">
                                      📖
                                    </span>
                                    <div>
                                      <span className="font-extrabold text-[16px] sm:text-[17px] text-[#0a5482] group-hover:text-[#073d60]">
                                        Vocabulary {lang === 'vi' ? '— Từ vựng trong bài' : ''}
                                      </span>
                                      <span className="ml-2.5 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-bold bg-sky-100 text-[#0a5482]">
                                        {vocabItems.length} {lang === 'vi' ? 'từ & cụm từ' : 'items'}
                                      </span>
                                    </div>
                                  </div>
                                  <span className="inline-flex items-center gap-1.5 text-xs sm:text-sm font-bold text-[#0a5482] bg-white px-3.5 py-1.5 rounded-xl border border-slate-200 group-hover:border-sky-300 shadow-2xs">
                                    <span>{showVocab ? (lang === 'vi' ? 'Thu gọn' : 'Hide') : lang === 'vi' ? 'Xem từ vựng' : 'Show'}</span>
                                    <span>{showVocab ? '▲' : '▼'}</span>
                                  </span>
                                </button>

                                {showVocab && (
                                  <div className="p-4 sm:p-5 bg-white border-t border-slate-200/80">
                                    <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                                      {vocabItems.map((item, idx) => (
                                        <div
                                          key={idx}
                                          className="p-4 rounded-xl bg-slate-50/70 hover:bg-sky-50/40 border border-slate-200/70 transition flex items-start gap-3"
                                        >
                                          <span className="w-6 h-6 rounded-lg bg-[#0a5482]/10 text-[#0a5482] font-extrabold text-xs flex items-center justify-center shrink-0 mt-0.5">
                                            {idx + 1}
                                          </span>
                                          <div className="min-w-0 flex-1">
                                            <div className="font-extrabold text-[16px] text-[#0a5482] leading-snug">
                                              {item.term}
                                            </div>
                                            <div className="text-[14.5px] sm:text-[15px] text-slate-600 leading-relaxed mt-1">
                                              {item.definition}
                                            </div>
                                          </div>
                                        </div>
                                      ))}
                                    </div>
                                  </div>
                                )}
                              </div>
                            )}

                            {article.news_question && article.news_question.trim() !== '' && (
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
                                      dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(article.news_question) }}
                                    />
                                    {article.news_answer && article.news_answer.trim() !== '' && (
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
                                            dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(article.news_answer) }}
                                          />
                                        )}
                                      </div>
                                    )}
                                  </div>
                                )}
                              </div>
                            )}

                            {article.news_conversation && article.news_conversation.trim() !== '' && (
                              <div className="bg-sky-50/40 rounded-2xl border border-sky-200/80 overflow-hidden">
                                <button
                                  type="button"
                                  onClick={() => setShowDialog(!showDialog)}
                                  className="w-full px-5 py-4 flex items-center justify-between text-left font-bold text-[15.5px] sm:text-base text-[#0a5482] hover:bg-sky-50/80 transition"
                                >
                                  <span>💬 {t('View Conversation Dialog')}</span>
                                  <span className="text-xs">{showDialog ? '▲' : '▼'}</span>
                                </button>
                                {showDialog && (
                                  <div
                                    className="p-5 bg-white border-t border-sky-100 legacy-prose"
                                    dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(article.news_conversation) }}
                                  />
                                )}
                              </div>
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

          {/* SEPARATE AIRY BLOCK FOR RELATED POSTS */}
          {!loading && mode === 'detail' && article && relatedNews.length > 0 && (
            <div className="bg-white/70 rounded-2xl border border-slate-200/60 px-6 py-5 sm:px-8 sm:py-6">
              <h3 className="text-xs sm:text-[13px] font-bold uppercase tracking-widest text-slate-400 mb-3.5 flex items-center gap-2">
                <span className="opacity-70 text-sm">📌</span>
                <span>{t('Related Post')}</span>
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-1">
                {relatedNews.map((rel) => (
                  <Link
                    key={rel.news_id}
                    to={`/news/view/${(rel.news_title_url || '').trim()}`}
                    className="group py-2 px-3 -mx-3 rounded-lg hover:bg-slate-100/70 text-[14px] sm:text-[14.5px] font-normal text-slate-500 hover:text-[#0a5482] transition-colors flex items-center gap-2.5"
                  >
                    <span className="w-1.5 h-1.5 rounded-full bg-slate-300 group-hover:bg-[#2ab4e8] shrink-0 transition-colors" />
                    <span className="line-clamp-1">{rel.news_title}</span>
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
