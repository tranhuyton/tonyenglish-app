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
                <div
                  className="legacy-prose"
                  dangerouslySetInnerHTML={{
                    __html: fixLegacyHtmlContent(
                      currentOpening
                        ? lang === 'vi'
                          ? currentOpening.ug_content_vi || currentOpening.ug_content_en
                          : currentOpening.ug_content_en || currentOpening.ug_content_vi
                        : t('There are no public courses.')
                    ),
                  }}
                />
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
                /* CONTACT FORM & MAP */
                <>
                  {contactSubmitted ? (
                    <div className="py-14 text-center space-y-4">
                      <div className="w-16 h-16 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-3xl mx-auto">
                        ✓
                      </div>
                      <h3 className="text-xl font-black text-[#0a5482]">
                        {t('Thank you for contacting us. We will respond to you as soon as possible.')}
                      </h3>
                    </div>
                  ) : (
                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                      <div>
                        <h2 className="text-xl font-black text-[#0a5482] mb-1">{t('Send message')}</h2>
                        <p className="text-xs text-slate-500 mb-5">
                          {t('Please feel free to contact us at anytime')}
                        </p>

                        {contactError && (
                          <div className="p-3.5 mb-4 rounded-xl bg-rose-50 border border-rose-200 text-rose-700 text-xs font-bold">
                            ⚠️ {contactError}
                          </div>
                        )}

                        <form onSubmit={handleContactSubmit} className="space-y-4">
                          <div>
                            <label className="block text-xs font-bold text-slate-600 mb-1">{t('Your name')} *</label>
                            <input
                              type="text"
                              required
                              value={contactName}
                              onChange={(e) => setContactName(e.target.value)}
                              className="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8] focus:bg-white"
                            />
                          </div>

                          <div>
                            <label className="block text-xs font-bold text-slate-600 mb-1">
                              {t('Your phone number')} *
                            </label>
                            <input
                              type="text"
                              required
                              value={contactPhone}
                              onChange={(e) => setContactPhone(e.target.value)}
                              className="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8] focus:bg-white"
                            />
                          </div>

                          <div>
                            <label className="block text-xs font-bold text-slate-600 mb-1">
                              {t('Your email address')} *
                            </label>
                            <input
                              type="email"
                              required
                              value={contactEmail}
                              onChange={(e) => setContactEmail(e.target.value)}
                              className="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8] focus:bg-white"
                            />
                          </div>

                          <div>
                            <label className="block text-xs font-bold text-slate-600 mb-1">{t('Your message')} *</label>
                            <textarea
                              rows={4}
                              required
                              value={contactMessage}
                              onChange={(e) => setContactMessage(e.target.value)}
                              className="w-full bg-slate-50 border border-slate-300 rounded-xl p-4 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8] focus:bg-white"
                            />
                          </div>

                          <button
                            type="submit"
                            disabled={contactLoading}
                            className="bg-[#0a5482] hover:bg-[#084266] text-white font-black text-sm px-8 py-3 rounded-xl shadow-lg transition"
                          >
                            {contactLoading ? '...' : `${t('Send')} ➜`}
                          </button>
                        </form>
                      </div>

                      <div className="space-y-4">
                        <h2 className="text-xl font-black text-[#0a5482] mb-1">{t('Map')}</h2>
                        <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200/80 text-sm space-y-1.5">
                          <p>
                            <strong className="text-slate-700">{t('Address')}:</strong>{' '}
                            {options['company_address']
                              ? options['company_address'].replace(/<[^>]*>?/gm, '').trim()
                              : 'Hà Nội, Việt Nam'}
                          </p>
                          <p>
                            <strong className="text-slate-700">{t('Tel')}:</strong>{' '}
                            {options['company_fax'] || options['company_phone'] || '0982 042 882'}
                          </p>
                          <p>
                            <strong className="text-slate-700">Email:</strong>{' '}
                            <a
                              className="text-[#0a5482] font-bold hover:underline"
                              href={`mailto:${options['company_email'] || 'contact@tonyenglish.vn'}`}
                            >
                              {options['company_email'] || 'contact@tonyenglish.vn'}
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
                                : 'Hanoi, Vietnam'
                            )}&output=embed`}
                          />
                        </div>
                      </div>
                    </div>
                  )}
                </>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
