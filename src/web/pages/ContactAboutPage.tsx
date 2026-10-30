import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import { fixLegacyHtmlContent, updatePageSeo } from '../lib/utils';

export const ContactAboutPage: React.FC<{ mode: 'about' | 'contact' | 'opening' | 'sitemap' }> = ({ mode }) => {
  const { slug } = useParams<{ slug?: string }>();
  const { lang, t, options, footerCourses, footerNewsCates, footerAboutItems } = useApp();

  const [aboutList, setAboutList] = useState<any[]>([]);
  const [openingGroups, setOpeningGroups] = useState<any[]>([]);
  const [mobileCateOpen, setMobileCateOpen] = useState(false);

  // Contact form state
  const [contactName, setContactName] = useState('');
  const [contactPhone, setContactPhone] = useState('');
  const [contactEmail, setContactEmail] = useState('');
  const [contactMessage, setContactMessage] = useState('');
  const [contactSubmitted, setContactSubmitted] = useState(false);
  const [contactError, setContactError] = useState('');
  const [contactLoading, setContactLoading] = useState(false);

  useEffect(() => {
    async function loadData() {
      const [abRes, ugRes] = await Promise.all([
        supabase
          .from('te_about')
          .select('*')
          .eq('deleted', 0)
          .eq('about_status', 1)
          .order('about_order', { ascending: true }),
        supabase
          .from('te_user_group')
          .select('*')
          .eq('deleted', 0)
          .eq('ug_status', 1)
          .eq('ug_opening', 1),
      ]);
      if (abRes.data) setAboutList(abRes.data);
      if (ugRes.data) setOpeningGroups(ugRes.data);
    }
    loadData();
    setContactSubmitted(false);
    setContactError('');
  }, [mode, slug]);

  const cleanSlug = decodeURIComponent(slug || '')
    .trim()
    .replace(/\.html$/i, '');

  const currentAbout =
    mode === 'about'
      ? cleanSlug
        ? aboutList.find(
            (ab) =>
              (ab.about_title_url_vi || '').trim() === cleanSlug ||
              (ab.about_title_url_en || '').trim() === cleanSlug
          ) || aboutList[0]
        : aboutList[0]
      : null;

  const currentOpening =
    mode === 'opening'
      ? cleanSlug
        ? openingGroups.find((ug) => (ug.ug_name_url || '').trim() === cleanSlug) || openingGroups[0]
        : openingGroups[0]
      : null;

  const handleContactSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setContactError('');
    if (!contactName.trim() || !contactPhone.trim() || !contactEmail.trim() || !contactMessage.trim()) {
      setContactError(t('Please complete information on the items marked with') + ' (*)');
      return;
    }

    setContactLoading(true);
    const { data: maxRow } = await supabase
      .from('te_contact')
      .select('contact_id')
      .order('contact_id', { ascending: false })
      .limit(1);
    const nextId = maxRow && maxRow.length > 0 ? Number(maxRow[0].contact_id) + 1 : 5000;

    const { error } = await supabase.from('te_contact').insert({
      contact_id: nextId,
      contact_name: contactName.trim(),
      contact_phone: contactPhone.trim(),
      contact_email: contactEmail.trim(),
      contact_message: contactMessage.trim(),
      contact_title: 'Liên hệ từ website',
      contact_created_at: Math.floor(Date.now() / 1000),
      contact_status: 1,
      deleted: 0,
    });
    setContactLoading(false);

    if (error) {
      setContactError(error.message);
    } else {
      setContactSubmitted(true);
    }
  };

  const pageHeading =
    mode === 'about' && currentAbout
      ? lang === 'vi'
        ? currentAbout.about_title_vi
        : currentAbout.about_title_en
      : mode === 'opening'
      ? currentOpening
        ? lang === 'vi'
          ? currentOpening.ug_name_vi || currentOpening.ug_name
          : currentOpening.ug_name
        : t('Openning Class')
      : mode === 'sitemap'
      ? t('Site map')
      : t('Contact us');

  useEffect(() => {
    updatePageSeo(pageHeading);
  }, [pageHeading]);

  return (
    <div className="max-w-7xl mx-auto px-3.5 sm:px-6 py-4 sm:py-8">
      {/* BREADCRUMB */}
      <nav className="flex items-center gap-1.5 sm:gap-2 text-xs sm:text-[15px] font-semibold text-slate-500 mb-3.5 sm:mb-6 flex-wrap">
        <Link to="/" className="hover:text-[#0a5482] flex items-center gap-1">
          <span>🏠</span>
          <span>{t('Home')}</span>
        </Link>
        <span>/</span>
        <span className="text-[#0a5482] font-bold">{pageHeading}</span>
      </nav>

      <div className="flex flex-col lg:flex-row gap-4 sm:gap-8 xl:gap-12 items-start">
        {/* LEFT SIDEBAR: SUBTLE, NON-COMPETING ABOUT MENU */}
        <aside className="w-full lg:w-[260px] xl:w-[270px] shrink-0 bg-white rounded-2xl border border-slate-200/80 shadow-2xs overflow-hidden lg:sticky lg:top-24">
          <button
            type="button"
            onClick={() => setMobileCateOpen((prev) => !prev)}
            className="w-full bg-slate-100/80 px-4 py-3 border-b border-slate-200/70 flex items-center justify-between lg:pointer-events-none cursor-pointer text-left"
          >
            <h2 className="text-slate-600 lg:text-slate-500 font-bold text-xs uppercase tracking-widest flex items-center gap-2 min-w-0">
              <span className="opacity-80 shrink-0">ℹ️</span>
              <span className="shrink-0">{t('About us')}</span>
              <span className="lg:hidden font-semibold text-[#0a5482] normal-case tracking-normal truncate">
                • {pageHeading}
              </span>
            </h2>
            <span className="lg:hidden text-[11px] font-bold text-[#0a5482] bg-white px-2.5 py-1 rounded-lg border border-slate-200/80 shadow-2xs flex items-center gap-1 shrink-0 ml-2">
              <span>
                {mobileCateOpen
                  ? lang === 'vi'
                    ? 'Thu gọn'
                    : 'Hide'
                  : lang === 'vi'
                  ? 'Danh mục'
                  : 'Menu'}
              </span>
              <span>{mobileCateOpen ? '▲' : '▼'}</span>
            </span>
          </button>

          <ul className={`divide-y divide-slate-100 text-[14.5px] p-1.5 ${mobileCateOpen ? 'block' : 'hidden'} lg:block`}>
            {aboutList.map((ab) => {
              const title = lang === 'vi' ? ab.about_title_vi : ab.about_title_en;
              const urlSlug = lang === 'vi' ? ab.about_title_url_vi : ab.about_title_url_en;
              const isActive = mode === 'about' && currentAbout && currentAbout.about_id === ab.about_id;

              return (
                <li key={ab.about_id}>
                  <Link
                    to={`/about/${(urlSlug || '').trim()}`}
                    onClick={() => setMobileCateOpen(false)}
                    className={`block px-3.5 py-2.5 rounded-xl transition-colors ${
                      isActive
                        ? 'bg-sky-50/90 text-[#0a5482] font-semibold border-l-[3px] border-[#2ab4e8]'
                        : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                    }`}
                  >
                    {title}
                  </Link>
                </li>
              );
            })}

            <li>
              <Link
                to="/opening"
                onClick={() => setMobileCateOpen(false)}
                className={`block px-3.5 py-2.5 rounded-xl transition-colors ${
                  mode === 'opening'
                    ? 'bg-sky-50/90 text-[#0a5482] font-semibold border-l-[3px] border-[#2ab4e8]'
                    : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                }`}
              >
                📅 {t('Openning Class')}
              </Link>
              {mode === 'opening' && openingGroups.length > 0 && (
                <ul className="mt-0.5 mb-1 ml-2 pl-2 border-l border-slate-200/80 space-y-0.5">
                  {openingGroups.map((ug) => (
                    <li key={ug.ug_id}>
                      <Link
                        to={`/opening/${(ug.ug_name_url || '').trim()}`}
                        onClick={() => setMobileCateOpen(false)}
                        className={`block px-3 py-2 rounded-lg text-[13.5px] transition-all ${
                          currentOpening && currentOpening.ug_id === ug.ug_id
                            ? 'bg-sky-50 text-[#0a5482] font-semibold border-l-2 border-[#2ab4e8]'
                            : 'text-slate-500 font-normal hover:bg-slate-50 hover:text-slate-800'
                        }`}
                      >
                        {lang === 'vi' ? ug.ug_name_vi || ug.ug_name : ug.ug_name}
                      </Link>
                    </li>
                  ))}
                </ul>
              )}
            </li>

            <li>
              <Link
                to="/sitemap"
                onClick={() => setMobileCateOpen(false)}
                className={`block px-3.5 py-2.5 rounded-xl transition-colors ${
                  mode === 'sitemap'
                    ? 'bg-sky-50/90 text-[#0a5482] font-semibold border-l-[3px] border-[#2ab4e8]'
                    : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                }`}
              >
                🗺️ {t('Site map')}
              </Link>
            </li>

            <li>
              <Link
                to="/contact"
                onClick={() => setMobileCateOpen(false)}
                className={`block px-3.5 py-2.5 rounded-xl transition-colors ${
                  mode === 'contact'
                    ? 'bg-sky-50/90 text-[#0a5482] font-semibold border-l-[3px] border-[#2ab4e8]'
                    : 'text-slate-600 font-medium hover:bg-slate-50 hover:text-[#0a5482]'
                }`}
              >
                📞 {t('Contact')}
              </Link>
            </li>
          </ul>
        </aside>

        {/* RIGHT MAIN CONTENT */}
        <div className="flex-1 min-w-0 w-full">
          <div className="bg-white rounded-2xl sm:rounded-3xl border border-slate-200/90 shadow-sm overflow-hidden">
            {/* Header */}
            <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-4 sm:px-8 py-4 sm:py-6 text-white">
              <div className="text-[11px] sm:text-xs font-extrabold uppercase tracking-widest text-[#2ab4e8] mb-0.5 sm:mb-1">
                TonyEnglish Center
              </div>
              <h1 className="text-xl sm:text-3xl font-black tracking-tight">{pageHeading}</h1>
            </div>

            <div className="p-4 sm:p-8">
              {mode === 'about' && currentAbout ? (
                <div
                  className="legacy-prose text-justify"
                  dangerouslySetInnerHTML={{
                    __html: fixLegacyHtmlContent(
                      lang === 'vi' ? currentAbout.about_content_vi : currentAbout.about_content_en
                    ),
                  }}
                />
              ) : mode === 'opening' ? (
                <div className="space-y-6">
                  <div className="bg-sky-50 border border-sky-200 rounded-2xl p-5 sm:p-6">
                    <div className="inline-flex items-center gap-2 bg-[#0a5482] text-white text-xs font-black uppercase tracking-wider px-3 py-1 rounded-full mb-3">
                      <span>📅</span>
                      <span>{lang === 'vi' ? 'Lịch khai giảng & Tuyển sinh' : 'Enrollment Schedule'}</span>
                    </div>
                    <h2 className="text-xl sm:text-2xl font-black text-slate-800 mb-2">
                      {lang === 'vi'
                        ? 'Liên tục tuyển sinh các gói học 1 kèm 1 cho Giao tiếp tiếng Anh, IELTS, IGCSE'
                        : 'Continuous Enrollment for 1-on-1 Packages: English Communication, IELTS & IGCSE'}
                    </h2>
                    <p className="text-sm sm:text-base text-slate-600 leading-relaxed">
                      {lang === 'vi'
                        ? 'TonyEnglish liên tục khai giảng và nhận học viên các gói đào tạo 1 kèm 1 (One-on-One) cá nhân hóa theo trình độ, lịch học linh hoạt kết hợp hệ thống bài giảng tương tác & luyện đề AI 24/7:'
                        : 'TonyEnglish continuously enrolls students for personalized 1-on-1 training packages with flexible schedules and 24/7 AI-powered LMS practice:'}
                    </p>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
                    <div className="bg-white rounded-2xl border border-slate-200 p-5 flex flex-col justify-between shadow-2xs hover:shadow-md transition">
                      <div>
                        <span className="inline-block bg-indigo-50 text-indigo-700 border border-indigo-200 text-xs font-black px-3 py-1 rounded-full mb-3">
                          🎙️ GÓI HỌC 1 KÈM 1
                        </span>
                        <h3 className="text-lg font-black text-slate-800 mb-2">
                          Giao tiếp Tiếng Anh &amp; Văn phòng
                        </h3>
                        <p className="text-sm text-slate-600 leading-relaxed mb-4">
                          Chuẩn hóa phát âm IPA, luyện phản xạ giao tiếp đời sống, tiếng Anh văn phòng công sở và viết Email chuyên nghiệp.
                        </p>
                      </div>
                      <Link
                        to="/courses/english-communication 1"
                        className="text-sm font-black text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1"
                      >
                        <span>Xem đề cương khóa học</span>
                        <span>→</span>
                      </Link>
                    </div>

                    <div className="bg-white rounded-2xl border border-slate-200 p-5 flex flex-col justify-between shadow-2xs hover:shadow-md transition">
                      <div>
                        <span className="inline-block bg-sky-50 text-[#0a5482] border border-sky-200 text-xs font-black px-3 py-1 rounded-full mb-3">
                          🏆 GÓI HỌC 1 KÈM 1
                        </span>
                        <h3 className="text-lg font-black text-slate-800 mb-2">
                          Luyện thi IELTS 4 Kỹ Năng
                        </h3>
                        <p className="text-sm text-slate-600 leading-relaxed mb-4">
                          Lộ trình cá nhân hóa từ nền tảng đến Band 7.0+, kèm sát Speaking &amp; Writing 1-1 kết hợp phòng thi máy tính chuẩn IDP/BC.
                        </p>
                      </div>
                      <Link
                        to="/courses/ielts"
                        className="text-sm font-black text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1"
                      >
                        <span>Xem đề cương khóa học</span>
                        <span>→</span>
                      </Link>
                    </div>

                    <div className="bg-white rounded-2xl border border-slate-200 p-5 flex flex-col justify-between shadow-2xs hover:shadow-md transition">
                      <div>
                        <span className="inline-block bg-amber-50 text-amber-800 border border-amber-200 text-xs font-black px-3 py-1 rounded-full mb-3">
                          🌍 GÓI HỌC 1 KÈM 1
                        </span>
                        <h3 className="text-lg font-black text-slate-800 mb-2">
                          Chương trình Quốc tế Cambridge IGCSE
                        </h3>
                        <p className="text-sm text-slate-600 leading-relaxed mb-4">
                          Kèm sát các môn Sciences (0654/0610/0620/0625), Maths (0580/0606), Economics (0455), Business (0450), Geography (0460) &amp; ESL (0510).
                        </p>
                      </div>
                      <Link
                        to="/courses/luyen-thi-igcse-alevel-cap-toc"
                        className="text-sm font-black text-[#0a5482] hover:text-[#2ab4e8] inline-flex items-center gap-1"
                      >
                        <span>Xem đề cương khóa học</span>
                        <span>→</span>
                      </Link>
                    </div>
                  </div>
                </div>
              ) : mode === 'sitemap' ? (
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div className="bg-slate-50 rounded-2xl p-5 border border-slate-200/80">
                    <h3 className="font-black text-base text-[#0a5482] mb-3 pb-2 border-b border-slate-200">
                      📚 {t('Library')}
                    </h3>
                    <ul className="space-y-2 text-sm">
                      {footerNewsCates.map((nc) => (
                        <li key={nc.news_cc_id}>
                          <Link
                            to={`/news/category/${(nc.news_cc_name_url || '').trim()}`}
                            className="text-slate-700 hover:text-[#0a5482] font-medium"
                          >
                            • {lang === 'vi' ? nc.news_cc_name_vi || nc.news_cc_name : nc.news_cc_name}
                          </Link>
                        </li>
                      ))}
                    </ul>
                  </div>

                  <div className="bg-slate-50 rounded-2xl p-5 border border-slate-200/80">
                    <h3 className="font-black text-base text-[#0a5482] mb-3 pb-2 border-b border-slate-200">
                      🎓 {t('Courses')}
                    </h3>
                    <ul className="space-y-2 text-sm">
                      {footerCourses.map((c) => (
                        <li key={c.cc_id}>
                          <Link
                            to={`/courses/${(c.cc_name_url || '').trim()}`}
                            className="text-slate-700 hover:text-[#0a5482] font-medium"
                          >
                            • {lang === 'vi' ? c.cc_name_vi || c.cc_name : c.cc_name}
                          </Link>
                        </li>
                      ))}
                    </ul>
                  </div>

                  <div className="bg-slate-50 rounded-2xl p-5 border border-slate-200/80">
                    <h3 className="font-black text-base text-[#0a5482] mb-3 pb-2 border-b border-slate-200">
                      ℹ️ {t('About us')}
                    </h3>
                    <ul className="space-y-2 text-sm">
                      {footerAboutItems.map((ab) => {
                        const title = lang === 'vi' ? ab.about_title_vi : ab.about_title_en;
                        const urlSlug = lang === 'vi' ? ab.about_title_url_vi : ab.about_title_url_en;
                        return (
                          <li key={ab.about_id}>
                            <Link
                              to={`/about/${(urlSlug || '').trim()}`}
                              className="text-slate-700 hover:text-[#0a5482] font-medium"
                            >
                              • {title}
                            </Link>
                          </li>
                        );
                      })}
                    </ul>
                  </div>
                </div>
              ) : (
                /* DIRECT PHONE & ZALO CONTACT + MAP */
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-start">
                  <div className="space-y-5">
                    <div>
                      <span className="inline-block bg-emerald-100 text-emerald-800 font-black text-xs px-3 py-1 rounded-full uppercase tracking-wider mb-2">
                        {lang === 'vi' ? 'LIÊN HỆ TRỰC TIẾP 24/7' : 'DIRECT CONTACT 24/7'}
                      </span>
                      <h2 className="text-xl sm:text-2xl font-black text-[#0a5482] mb-1.5">
                        {lang === 'vi'
                          ? 'Gọi Điện Trực Tiếp Hoặc Nhắn Tin Qua Zalo'
                          : 'Call Directly or Chat via Zalo'}
                      </h2>
                      <p className="text-sm text-slate-600 leading-relaxed">
                        {lang === 'vi'
                          ? 'Để được tư vấn lộ trình học IELTS, Cambridge IGCSE, Giao tiếp tiếng Anh và đặt lịch học thử miễn phí nhanh nhất, quý phụ huynh và học viên vui lòng gọi điện hoặc nhắn Zalo trực tiếp cho thầy Trần Huy Tôn:'
                          : 'For course consultation and trial scheduling, please call or message us directly via Zalo:'}
                      </p>
                    </div>

                    <div className="space-y-3.5">
                      <a
                        href="https://zalo.me/0935058688"
                        target="_blank"
                        rel="noreferrer"
                        onClick={() => {
                          try {
                            const w = window as any;
                            if (typeof w.fbq === 'function') {
                              w.fbq('track', 'Lead', { content_name: 'Contact Page Zalo', contact_method: 'Zalo' });
                              w.fbq('track', 'Contact', { content_name: 'Contact Page Zalo', contact_method: 'Zalo' });
                            }
                          } catch (e) {}
                        }}
                        className="flex items-center justify-between gap-4 bg-[#0068ff] hover:bg-[#0057d6] text-white p-5 rounded-2xl shadow-lg shadow-blue-600/20 transition transform hover:-translate-y-0.5 active:scale-95 group"
                      >
                        <div className="flex items-center gap-3.5 min-w-0">
                          <div className="w-12 h-12 rounded-xl bg-white/20 flex items-center justify-center text-2xl shrink-0">
                            💬
                          </div>
                          <div className="min-w-0">
                            <div className="text-xs font-black text-cyan-200 uppercase tracking-wider">
                              {lang === 'vi' ? 'Nhắn tin Zalo trực tiếp' : 'Chat on Zalo'}
                            </div>
                            <div className="text-lg sm:text-xl font-black truncate">0935 058 688</div>
                            <div className="text-xs text-blue-100">
                              {lang === 'vi' ? 'Bấm để mở Zalo chat ngay (Mr. Trần Huy Tôn)' : 'Click to open Zalo chat'}
                            </div>
                          </div>
                        </div>
                        <span className="bg-white text-[#0068ff] font-black text-xs px-3.5 py-2 rounded-xl shrink-0 group-hover:bg-amber-300 group-hover:text-slate-950 transition">
                          {lang === 'vi' ? 'Mở Zalo ➜' : 'Open Zalo ➜'}
                        </span>
                      </a>

                      <a
                        href="tel:0935058688"
                        onClick={() => {
                          try {
                            const w = window as any;
                            if (typeof w.fbq === 'function') {
                              w.fbq('track', 'Lead', { content_name: 'Contact Page Phone', contact_method: 'Phone' });
                              w.fbq('track', 'Contact', { content_name: 'Contact Page Phone', contact_method: 'Phone' });
                            }
                          } catch (e) {}
                        }}
                        className="flex items-center justify-between gap-4 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 text-white p-5 rounded-2xl shadow-lg shadow-emerald-600/20 transition transform hover:-translate-y-0.5 active:scale-95 group"
                      >
                        <div className="flex items-center gap-3.5 min-w-0">
                          <div className="w-12 h-12 rounded-xl bg-white/20 flex items-center justify-center text-2xl shrink-0">
                            📞
                          </div>
                          <div className="min-w-0">
                            <div className="text-xs font-black text-emerald-200 uppercase tracking-wider">
                              {lang === 'vi' ? 'Gọi điện trực tiếp Hotline' : 'Direct Hotline'}
                            </div>
                            <div className="text-lg sm:text-xl font-black truncate">0935 058 688</div>
                            <div className="text-xs text-emerald-100">
                              {lang === 'vi' ? 'Tư vấn lộ trình & đặt lịch học thử miễn phí' : 'Direct consultation & trial booking'}
                            </div>
                          </div>
                        </div>
                        <span className="bg-white text-emerald-700 font-black text-xs px-3.5 py-2 rounded-xl shrink-0 group-hover:bg-amber-300 group-hover:text-slate-950 transition">
                          {lang === 'vi' ? 'Gọi ngay ➜' : 'Call now ➜'}
                        </span>
                      </a>
                    </div>

                    <div className="bg-sky-50 border border-sky-200/80 rounded-2xl p-4 text-xs sm:text-sm text-slate-700 space-y-1.5">
                      <div className="font-black text-[#0a5482] uppercase tracking-wider text-xs">
                        🎁 {lang === 'vi' ? 'Quyền lợi khi liên hệ trực tiếp:' : 'Benefits when contacting directly:'}
                      </div>
                      <p>✔ {lang === 'vi' ? 'Miễn phí 02 buổi học thử & Test đánh giá năng lực đầu vào trực tiếp.' : 'Free 2 trial lessons & placement assessment.'}</p>
                      <p>✔ {lang === 'vi' ? 'Cấp ngay tài khoản Lớp Học Thử trên hệ thống TonyEnglish trong 5 phút.' : 'Instant Trial Account activation on TonyEnglish LMS.'}</p>
                    </div>
                  </div>

                  <div className="space-y-4">
                    <h2 className="text-xl font-black text-[#0a5482] mb-1">{t('Map')}</h2>
                    <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200/80 text-sm space-y-2">
                      <p>
                        <strong className="text-slate-700">📍 {t('Address')}:</strong>{' '}
                        {options['company_address']
                          ? options['company_address'].replace(/<[^>]*>?/gm, '').trim()
                          : 'Tòa R2B Royal City, 72A Nguyễn Trãi, Thanh Xuân, Hà Nội'}
                      </p>
                      <p>
                        <strong className="text-slate-700">📞 Hotline / Zalo:</strong>{' '}
                        <a href="tel:0935058688" className="text-emerald-700 font-black hover:underline">
                          0935 058 688
                        </a>
                        {' • '}
                        <a
                          href="https://zalo.me/0935058688"
                          target="_blank"
                          rel="noreferrer"
                          className="text-[#0068ff] font-black hover:underline"
                        >
                          Chat Zalo
                        </a>
                      </p>
                    </div>

                    <div className="rounded-2xl overflow-hidden border border-slate-200 shadow-xs h-72">
                      <iframe
                        title="Google Map"
                        width="100%"
                        height="100%"
                        style={{ border: 0 }}
                        src={`https://maps.google.com/maps?q=${encodeURIComponent(
                          options['company_address']
                            ? options['company_address'].replace(/<[^>]*>?/gm, '').trim()
                            : 'R2B Royal City, 72A Nguyễn Trãi, Thanh Xuân, Hà Nội'
                        )}&output=embed`}
                      />
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
