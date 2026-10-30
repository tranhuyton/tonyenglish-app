import React, { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useApp } from '../context/AppContext';
import { supabase } from '../../supabase';

export const Layout: React.FC<{
  children: React.ReactNode;
  onNavigateLms?: (view: string) => void;
}> = ({ children, onNavigateLms }) => {
  const {
    lang,
    setLang,
    t,
    user,
    options,
    footerCourses,
    footerNewsCates,
    footerAboutItems,
    selectedCourseId,
    setSelectedCourseId,
    userCoursesList,
    loginModalOpen,
    setLoginModalOpen,
    loginUser,
  } = useApp();

  const location = useLocation();
  const navigate = useNavigate();

  // LMS Supabase Auth State
  const [lmsRole, setLmsRole] = useState<'admin' | 'student' | null>(null);

  useEffect(() => {
    const checkSession = async () => {
      try {
        const { data: { session } } = await supabase.auth.getSession();
        if (session?.user) {
          const email = session.user.email?.toLowerCase() || '';
          if (email.includes('admin')) {
            setLmsRole('admin');
            return;
          }
          const { data: profile } = await supabase
            .from('profiles')
            .select('role, status')
            .eq('id', session.user.id)
            .maybeSingle();
          if (profile?.role === 'admin') {
            setLmsRole('admin');
          } else if (profile?.status !== 'inactive') {
            setLmsRole('student');
          }
        } else {
          setLmsRole(null);
        }
      } catch (e) {
        console.warn('Session check warning:', e);
      }
    };
    checkSession();

    const { data: { subscription } } = supabase.auth.onAuthStateChange((_event, session) => {
      if (!session?.user) {
        setLmsRole(null);
      } else {
        const email = session.user.email?.toLowerCase() || '';
        setLmsRole(email.includes('admin') ? 'admin' : 'student');
      }
    });
    return () => subscription.unsubscribe();
  }, []);

  // Listen to custom event 'tony-open-lms' from anywhere in Web Portal
  useEffect(() => {
    const handleOpenLms = () => {
      if (lmsRole === 'admin' || lmsRole === 'student') {
        onNavigateLms?.('student-resume');
      } else {
        setLoginModalOpen(true);
      }
    };
    window.addEventListener('tony-open-lms', handleOpenLms);
    return () => window.removeEventListener('tony-open-lms', handleOpenLms);
  }, [lmsRole, onNavigateLms, setLoginModalOpen]);

  // Search / Dictionary / Translate state
  const [searchMode, setSearchMode] = useState<'dic' | 'web' | 'trans'>('dic');
  const [searchDropdownOpen, setSearchDropdownOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  // Dictionary / Translate modal popup
  const [popupModal, setPopupModal] = useState<{ title: string; url?: string; content?: string } | null>(null);

  // Double-click quick lookup tooltip state (autosearch.js replica)
  const [quickDict, setQuickDict] = useState<{ word: string; x: number; y: number } | null>(null);

  useEffect(() => {
    const handleDblClick = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      if (target && (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA' || target.isContentEditable)) {
        return;
      }
      const selection = window.getSelection()?.toString().trim() || '';
      const cleanWord = selection.replace(/^[^a-zA-Z0-9À-ỹ]+|[^a-zA-Z0-9À-ỹ]+$/g, '').toLowerCase();
      if (cleanWord.length > 1 && cleanWord.length <= 40) {
        const winWidth = window.innerWidth - 20;
        const winHeight = window.innerHeight - 20;
        const tipWidth = 320;
        const tipHeight = 245;
        let left = e.pageX + 12;
        let top = e.pageY + 10;
        if (e.clientX + 12 + tipWidth > winWidth) {
          left = Math.max(5, e.pageX - tipWidth);
        }
        if (e.clientY + 10 + tipHeight > winHeight) {
          top = Math.max(5, e.pageY - tipHeight - 10);
        }
        setQuickDict({ word: cleanWord, x: left, y: top });
      }
    };

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.ctrlKey && e.shiftKey && (e.key === 'A' || e.key === 'a')) {
        const selection = window.getSelection()?.toString().trim() || '';
        const cleanWord = selection.replace(/^[^a-zA-Z0-9À-ỹ]+|[^a-zA-Z0-9À-ỹ]+$/g, '').toLowerCase();
        if (cleanWord.length > 1) {
          setQuickDict({
            word: cleanWord,
            x: Math.max(20, window.scrollX + window.innerWidth / 2 - 155),
            y: Math.max(20, window.scrollY + window.innerHeight / 2 - 120),
          });
        }
      } else if (e.key === 'Escape') {
        setQuickDict(null);
      }
    };

    document.addEventListener('dblclick', handleDblClick);
    document.addEventListener('keydown', handleKeyDown);
    return () => {
      document.removeEventListener('dblclick', handleDblClick);
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  // Unified Login & Forgot Password modal state
  const [loginUsername, setLoginUsername] = useState('');
  const [loginPassword, setLoginPassword] = useState('');
  const [loginError, setLoginError] = useState('');
  const [loginLoading, setLoginLoading] = useState(false);

  const [forgotPasswordMode, setForgotPasswordMode] = useState(false);
  const [resetEmail, setResetEmail] = useState('');
  const [isResetting, setIsResetting] = useState(false);
  const [resetSentSuccess, setResetSentSuccess] = useState(false);
  const [resetError, setResetError] = useState('');

  const path = location.pathname;
  const isHome = path === '/' || path === '/vi' || path === '/en';
  const isCourses = path.includes('/courses');
  const isNews = path.includes('/news') || path.includes('/view/');
  const isVideos = path.includes('/videos') || path.includes('/video') || path.includes('/videocate');
  const isAbout = path.includes('/about') || path.includes('/opening') || path.includes('/sitemap');
  const isContact = path.includes('/contact');
  const isLecture = path.startsWith('/user/lecture') || path.startsWith('/trial');
  const isAdminCp = path.startsWith('/admincp');

  const handleSearchSubmit = (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    const q = searchQuery.trim();
    if (searchMode === 'dic') {
      const cleanWord = q.replace(/^[^a-zA-Z0-9À-ỹ]+|[^a-zA-Z0-9À-ỹ]+$/g, '').toLowerCase();
      setPopupModal({
        title: cleanWord ? `${t('Look up dictionary')}: "${cleanWord}"` : t('Look up dictionary'),
        url: cleanWord
          ? `https://dic.tienganh123.com/fast_dict.php?word=${encodeURIComponent(cleanWord)}&dict=ev_ve&m=yes`
          : `https://dic.tienganh123.com/v2/`,
      });
      return;
    }
    if (!q) return;
    if (searchMode === 'web') {
      navigate(`/news?q=${encodeURIComponent(q)}`);
    } else if (searchMode === 'trans') {
      window.open(`https://translate.google.com/?sl=en&tl=vi&text=${encodeURIComponent(q)}&op=translate`, '_blank');
    }
  };

  const handleLoginSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoginError('');
    setLoginLoading(true);
    const cleanInput = loginUsername.trim().toLowerCase();

    try {
      // 1. Primary: Authenticate with Supabase Auth (Unified LMS + Web accounts)
      if (cleanInput.includes('@')) {
        const loginPromise = supabase.auth.signInWithPassword({
          email: cleanInput,
          password: loginPassword,
        });
        const timeoutPromise = new Promise<any>((_, reject) =>
          setTimeout(() => reject(new Error('TIMEOUT')), 12000)
        );
        const { data, error } = await Promise.race([loginPromise, timeoutPromise]);

        if (!error && data?.user) {
          const isAdmin = cleanInput.includes('admin');
          let profile: any = null;
          try {
            const profilePromise = supabase
              .from('profiles')
              .select('role, status')
              .eq('id', data.user.id)
              .single();
            const profileTimeout = new Promise<any>((_, reject) =>
              setTimeout(() => reject('TIMEOUT'), 4000)
            );
            const res = await Promise.race([profilePromise, profileTimeout]);
            profile = res?.data;
          } catch (pErr) {
            console.warn('Profile status check warning:', pErr);
          }

          if (profile?.role !== 'admin' && !isAdmin && profile?.status === 'inactive') {
            await supabase.auth.signOut();
            setLoginError(
              '⛔ Tài khoản học của bạn hiện đang ở trạng thái TẠM DỪNG. Vui lòng liên hệ trung tâm để được kích hoạt lại!'
            );
            setLoginLoading(false);
            return;
          }

          setLoginModalOpen(false);
          if (profile?.role === 'admin' || isAdmin) {
            onNavigateLms?.('admin');
          } else {
            onNavigateLms?.('student-resume');
          }
          setLoginLoading(false);
          return;
        }
      }

      // 2. Fallback: Legacy te_users account (for non-email usernames from 2013)
      const res = await loginUser(loginUsername, loginPassword);
      if (res.ok) {
        setLoginModalOpen(false);
        navigate('/user/lecture');
      } else {
        setLoginError('Sai thông tin đăng nhập! Vui lòng kiểm tra lại Email và Mật khẩu.');
      }
    } catch (err: any) {
      if (err.message === 'TIMEOUT') {
        setLoginError('⏳ Máy chủ đang phản hồi chậm. Vui lòng thử lại!');
      } else {
        setLoginError('Đã có lỗi xảy ra khi kết nối máy chủ.');
      }
    } finally {
      setLoginLoading(false);
    }
  };

  const handleForgotPassword = async (e: React.FormEvent) => {
    e.preventDefault();
    const cleanEmail = resetEmail.trim().toLowerCase();
    if (!cleanEmail) return;
    setIsResetting(true);
    setResetError('');
    try {
      const { data: profile } = await supabase
        .from('profiles')
        .select('id, email')
        .ilike('email', cleanEmail)
        .maybeSingle();

      if (!profile) {
        setResetError('Email này không tồn tại trong danh sách học viên của hệ thống TonyEnglish.');
        return;
      }

      const { error } = await supabase.auth.resetPasswordForEmail(cleanEmail, {
        redirectTo: `${window.location.origin}/`,
      });
      if (error) throw error;
      setResetSentSuccess(true);
    } catch (err: any) {
      setResetError(err.message || 'Không thể gửi email đặt lại mật khẩu. Vui lòng kiểm tra lại địa chỉ email.');
    } finally {
      setIsResetting(false);
    }
  };

  // If on AdminCP route, render children full-bleed
  if (isAdminCp) {
    return <>{children}</>;
  }

  const navItems = [
    { to: '/', label: t('Home'), active: isHome },
    { to: '/courses', label: t('Courses'), active: isCourses },
    { to: '/news', label: t('Library'), active: isNews },
    { to: '/videos', label: t('Videos Store'), active: isVideos },
    { to: '/about', label: t('About us'), active: isAbout },
    { to: '/contact', label: t('Contact'), active: isContact },
  ];

  const addressText = options['company_address']
    ? options['company_address'].replace(/<[^>]*>?/gm, '').trim()
    : 'Số 10, ngõ 121 Thái Hà, Đống Đa, Hà Nội';
  const phoneText = options['company_tel'] || options['company_phone'] || '0982 042 882';
  const emailText = options['company_email'] || 'contact@tonyenglish.vn';

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 text-slate-800 font-sans">
      {/* 1. TOP UTILITY BAR */}
      <div className="bg-[#0f172a] text-slate-300 border-b border-slate-800 text-[13px] sm:text-sm">
        <div className="max-w-7xl mx-auto px-3 sm:px-6 py-1.5 sm:py-2 flex flex-wrap items-center justify-between gap-2 sm:gap-3">
          {/* Left info (Desktop / Tablet) */}
          <div className="hidden md:flex items-center gap-4 flex-wrap">
            <span className="inline-flex items-center gap-1.5 text-slate-200 font-semibold">
              <span className="text-[#2ab4e8]">📞</span> {phoneText}
            </span>
            <span className="hidden lg:inline-flex items-center gap-1.5 text-slate-300">
              <span className="text-[#2ab4e8]">✉️</span> {emailText}
            </span>
            <span className="inline-flex items-center gap-1.5 bg-slate-800/90 text-sky-300 px-3 py-1 rounded-full text-xs font-semibold border border-slate-700">
              💡 {lang === 'vi' ? 'Click đúp vào từ tiếng Anh bất kỳ để tra từ điển' : 'Double-click any English word to look up'}
            </span>
          </div>

          {/* Right tools: Search/Dictionary + Course selector + Language */}
          <div className="flex items-center justify-between md:justify-end gap-2 sm:gap-2.5 w-full md:w-auto ml-auto">
            {/* Smart Dictionary & Search Bar */}
            <div className="relative flex-1 md:flex-initial flex items-center bg-slate-800/95 border border-sky-400/50 hover:border-[#2ab4e8] rounded-lg focus-within:border-[#2ab4e8] focus-within:ring-2 focus-within:ring-[#2ab4e8]/25 shadow-xs transition-all min-w-0">
              <button
                type="button"
                onClick={() => setSearchDropdownOpen(!searchDropdownOpen)}
                className="px-2 sm:px-2.5 py-1.5 text-xs font-bold text-[#2ab4e8] border-r border-slate-600/80 hover:bg-slate-700/60 rounded-l-lg flex items-center gap-1 whitespace-nowrap shrink-0"
                title="Chọn chế độ tra cứu"
              >
                {searchMode === 'dic' ? '📖 Từ điển' : searchMode === 'web' ? '🔍 Tìm bài' : '🌐 Dịch'}
                <span className="text-[10px] opacity-75">▼</span>
              </button>
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter') handleSearchSubmit(e);
                }}
                autoCapitalize="none"
                autoCorrect="off"
                spellCheck={false}
                placeholder={
                  searchMode === 'dic'
                    ? t('Look up dictionary')
                    : searchMode === 'web'
                    ? t('TonyEnglish.vn search')
                    : t('Google translate')
                }
                className="bg-transparent text-white placeholder-slate-400 text-[13px] px-2.5 sm:px-3 py-1.5 flex-1 md:w-48 min-w-0 focus:outline-none"
              />
              <button
                type="button"
                onClick={() => handleSearchSubmit()}
                className="px-2 sm:px-2.5 py-1.5 text-slate-300 hover:text-white hover:bg-[#0a5482] rounded-r-lg transition-colors shrink-0"
                title="Tra cứu"
              >
                🔍
              </button>

              {searchDropdownOpen && (
                <div className="absolute right-0 top-full mt-1.5 w-56 bg-white text-slate-800 rounded-xl shadow-xl border border-slate-200 py-1.5 z-50">
                  <button
                    type="button"
                    onClick={() => {
                      setSearchMode('dic');
                      setSearchDropdownOpen(false);
                      if (!searchQuery.trim()) {
                        setPopupModal({
                          title: t('Look up dictionary'),
                          url: 'https://dic.tienganh123.com/v2/',
                        });
                      }
                    }}
                    className={`w-full text-left px-3.5 py-2.5 text-[13px] font-semibold flex items-center justify-between hover:bg-slate-50 ${
                      searchMode === 'dic' ? 'text-[#0a5482] bg-sky-50/60' : 'text-slate-700'
                    }`}
                  >
                    <span>📖 {t('Look up dictionary')}</span>
                    {searchMode === 'dic' && <span className="text-[#2ab4e8] font-black">✓</span>}
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      setSearchMode('web');
                      setSearchDropdownOpen(false);
                    }}
                    className={`w-full text-left px-3.5 py-2.5 text-[13px] font-semibold flex items-center justify-between hover:bg-slate-50 ${
                      searchMode === 'web' ? 'text-[#0a5482] bg-sky-50/60' : 'text-slate-700'
                    }`}
                  >
                    <span>🔍 {t('TonyEnglish.vn search')}</span>
                    {searchMode === 'web' && <span className="text-[#2ab4e8] font-black">✓</span>}
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      setSearchMode('trans');
                      setSearchDropdownOpen(false);
                      window.open('https://translate.google.com/?hl=en&tab=wT#en/vi/', '_blank');
                    }}
                    className={`w-full text-left px-3.5 py-2.5 text-[13px] font-semibold flex items-center justify-between hover:bg-slate-50 ${
                      searchMode === 'trans' ? 'text-[#0a5482] bg-sky-50/60' : 'text-slate-700'
                    }`}
                  >
                    <span>🌐 {t('Google translate')}</span>
                    <span className="text-xs text-slate-400">↗</span>
                  </button>
                </div>
              )}
            </div>

            {/* Logged-in Legacy Course Selector */}
            {user && userCoursesList.length > 0 && (
              <select
                value={selectedCourseId || ''}
                onChange={(e) => {
                  const val = parseInt(e.target.value, 10);
                  setSelectedCourseId(val);
                  if (!path.startsWith('/user/lecture')) {
                    navigate('/user/lecture');
                  }
                }}
                className="bg-slate-800 text-sky-300 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs font-semibold focus:outline-none hidden sm:block"
              >
                {userCoursesList.map((cc: any) => (
                  <option key={cc.cc_id} value={cc.cc_id}>
                    {lang === 'vi' ? cc.cc_name_vi || cc.cc_name : cc.cc_name}
                  </option>
                ))}
              </select>
            )}

            {/* Language Switcher */}
            <div className="flex items-center bg-slate-800 rounded-lg p-0.5 border border-slate-700">
              <button
                type="button"
                onClick={() => setLang('vi')}
                className={`px-2.5 py-1 rounded-md text-xs font-bold transition-all ${
                  lang === 'vi' ? 'bg-[#2ab4e8] text-white shadow-sm' : 'text-slate-400 hover:text-white'
                }`}
              >
                VN
              </button>
              <button
                type="button"
                onClick={() => setLang('en')}
                className={`px-2.5 py-1 rounded-md text-xs font-bold transition-all ${
                  lang === 'en' ? 'bg-[#2ab4e8] text-white shadow-sm' : 'text-slate-400 hover:text-white'
                }`}
              >
                EN
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* 2. MAIN STICKY NAVBAR */}
      <nav className="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-40 shadow-xs">
        <div className="max-w-7xl mx-auto px-3 sm:px-6 h-15 sm:h-20 flex items-center justify-between gap-2 sm:gap-4">
          {/* Brand Logo */}
          <Link to="/" className="flex items-center gap-2 sm:gap-3 hover:opacity-90 transition-opacity shrink-0">
            <img
              src="/logo-shield.png"
              onError={(e) => {
                (e.currentTarget as HTMLImageElement).src = '/themes/tony/assets/img/logo khong chu.png';
              }}
              alt="TonyEnglish"
              className="h-8 sm:h-11 w-auto object-contain"
            />
            <div className="flex flex-col items-start leading-none">
              <div className="font-black text-[18px] sm:text-[25px] tracking-tight">
                <span className="text-[#2ab4e8]">TONY</span>
                <span className="text-[#0a5482]">ENGLISH</span>
              </div>
              <span className="text-[11px] font-bold uppercase tracking-widest text-slate-400 mt-0.5 hidden sm:block">
                The future begins here
              </span>
            </div>
          </Link>

          {/* Desktop Navigation Links */}
          <div className="hidden lg:flex items-center gap-1 xl:gap-2">
            {navItems.map((item) => (
              <Link
                key={item.to}
                to={item.to}
                className={`px-4 py-2 rounded-xl text-[15px] xl:text-[16px] font-bold transition-all whitespace-nowrap ${
                  item.active
                    ? 'bg-sky-50 text-[#0a5482] shadow-2xs border border-sky-100'
                    : 'text-slate-700 hover:text-[#0a5482] hover:bg-slate-50'
                }`}
              >
                {item.label}
              </Link>
            ))}

            {user && (
              <Link
                to="/user/lecture"
                className={`px-4 py-2 rounded-xl text-[15px] xl:text-[16px] font-bold transition-all whitespace-nowrap ${
                  isLecture
                    ? 'bg-sky-50 text-[#0a5482] border border-sky-100'
                    : 'text-slate-700 hover:text-[#0a5482] hover:bg-slate-50'
                }`}
              >
                📖 {t('Lectures')}
              </Link>
            )}
          </div>

          {/* Right Action Buttons (Unified LMS) */}
          <div className="flex items-center gap-1.5 sm:gap-3 shrink-0">
            {lmsRole ? (
              <>
                {lmsRole === 'admin' && (
                  <button
                    type="button"
                    onClick={() => onNavigateLms?.('student-resume')}
                    className="bg-emerald-50 hover:bg-emerald-100 text-emerald-700 text-[11px] sm:text-[14px] font-black uppercase tracking-wider px-2.5 py-1.5 sm:px-4 sm:py-2.5 rounded-xl transition border border-emerald-200 shadow-2xs active:scale-95 whitespace-nowrap"
                  >
                    🎓 {lang === 'vi' ? 'Góc Học Viên' : 'Student Portal'}
                  </button>
                )}
                <button
                  type="button"
                  onClick={() => (lmsRole === 'admin' ? onNavigateLms?.('admin') : onNavigateLms?.('student-resume'))}
                  className="bg-gradient-to-r from-[#2ab4e8] to-[#0a5482] hover:opacity-95 text-white text-[11px] sm:text-[15px] font-black px-2.5 py-1.5 sm:px-5 sm:py-2.5 rounded-xl transition shadow-md shadow-sky-500/20 active:scale-95 whitespace-nowrap"
                >
                  {lmsRole === 'admin' ? (
                    <>
                      ⚙️ {lang === 'vi' ? 'Quản Trị' : 'Admin Setting'}
                      <span className="hidden sm:inline"> ➜</span>
                    </>
                  ) : (
                    <>
                      🎓 {lang === 'vi' ? 'Góc Học Viên' : 'Student Portal'}
                      <span className="hidden sm:inline"> ➜</span>
                    </>
                  )}
                </button>
              </>
            ) : user ? (
              <div className="flex items-center gap-2">
                <Link
                  to="/user/profile"
                  className="bg-slate-100 hover:bg-slate-200 text-[#0a5482] text-xs sm:text-[15px] font-bold px-3 py-1.5 sm:px-3.5 sm:py-2 rounded-xl transition flex items-center gap-1.5 sm:gap-2"
                >
                  <span>👤</span>
                  <span className="max-w-[90px] sm:max-w-[120px] truncate">
                    {user.user_fullname?.trim() ? user.user_fullname.trim().split(' ').slice(-1)[0] : user.user_name}
                  </span>
                </Link>
              </div>
            ) : (
              <button
                type="button"
                onClick={() => {
                  setForgotPasswordMode(false);
                  setLoginModalOpen(true);
                }}
                className="bg-[#0a5482] hover:bg-[#084266] text-white text-xs sm:text-[15px] font-bold px-3.5 py-2 sm:px-5 sm:py-2.5 rounded-xl transition shadow-md shadow-blue-900/15 active:scale-95 whitespace-nowrap"
              >
                {t('Login')}
              </button>
            )}

            {/* Mobile Hamburger Button */}
            <button
              type="button"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="lg:hidden p-1.5 sm:p-2 rounded-xl text-slate-600 hover:bg-slate-100"
              aria-label="Menu"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                {mobileMenuOpen ? (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                ) : (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                )}
              </svg>
            </button>
          </div>
        </div>

        {/* Mobile Dropdown Menu */}
        {mobileMenuOpen && (
          <div className="lg:hidden bg-white border-b border-slate-200 px-4 py-3 space-y-1.5 shadow-lg">
            {navItems.map((item) => (
              <Link
                key={item.to}
                to={item.to}
                onClick={() => setMobileMenuOpen(false)}
                className={`block px-4 py-2.5 rounded-xl text-base font-bold ${
                  item.active ? 'bg-sky-50 text-[#0a5482]' : 'text-slate-700 hover:bg-slate-50'
                }`}
              >
                {item.label}
              </Link>
            ))}
            {user && (
              <>
                <Link
                  to="/user/lecture"
                  onClick={() => setMobileMenuOpen(false)}
                  className="block px-4 py-2.5 rounded-xl text-base font-bold text-slate-700 hover:bg-slate-50"
                >
                  📖 {t('Lectures')}
                </Link>
                <Link
                  to="/user/profile"
                  onClick={() => setMobileMenuOpen(false)}
                  className="block px-4 py-2.5 rounded-xl text-base font-bold text-slate-700 hover:bg-slate-50"
                >
                  👤 {t('Profile')}
                </Link>
              </>
            )}
          </div>
        )}
      </nav>

      {/* 3. MAIN PAGE CONTENT */}
      <main className="flex-1">{children}</main>

      {/* 4. MODERN UNIFIED FOOTER */}
      <footer className="bg-[#0f172a] text-slate-400 pt-14 pb-10 border-t border-slate-800 mt-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 pb-10 border-b border-slate-800">
            {/* Col 1: Brand & Contact */}
            <div className="space-y-4">
              <Link to="/" className="flex items-center gap-3">
                <img
                  src="/logo-shield.png"
                  onError={(e) => {
                    (e.currentTarget as HTMLImageElement).src = '/themes/tony/assets/img/logo khong chu.png';
                  }}
                  alt="TonyEnglish"
                  className="h-9 w-auto object-contain"
                />
                <div className="font-black text-2xl tracking-tight text-white">
                  <span className="text-[#2ab4e8]">TONY</span>ENGLISH
                </div>
              </Link>
              <p className="text-[15px] text-slate-300 leading-relaxed">
                Hệ sinh thái đào tạo Tiếng Anh Giao Tiếp, TOEIC, IELTS &amp; Luyện thi thông minh tích hợp AI.
              </p>
              <div className="space-y-2 text-sm text-slate-300 pt-1">
                <p className="flex items-start gap-2">
                  <span className="text-[#2ab4e8] mt-0.5">📍</span>
                  <span>
                    {t('Address')}: {addressText}
                  </span>
                </p>
                <p className="flex items-center gap-2">
                  <span className="text-[#2ab4e8]">📞</span>
                  <span>
                    {t('Contact')}: {phoneText}
                  </span>
                </p>
                <p className="flex items-center gap-2">
                  <span className="text-[#2ab4e8]">✉️</span>
                  <span>Email: {emailText}</span>
                </p>
              </div>
            </div>

            {/* Col 2: Courses */}
            <div>
              <h3 className="text-white font-black text-[15px] uppercase tracking-wider mb-4">{t('Courses')}</h3>
              <ul className="space-y-2.5 text-[15px]">
                <li>
                  <Link to="/courses" className="hover:text-[#2ab4e8] transition-colors">
                    {t('Study at TonyEnglish')}
                  </Link>
                </li>
                {footerCourses.slice(0, 6).map((c: any) => (
                  <li key={c.cc_id}>
                    <Link to={`/courses/${(c.cc_name_url || '').trim()}`} className="hover:text-[#2ab4e8] transition-colors">
                      {lang === 'vi' ? c.cc_name_vi || c.cc_name : c.cc_name}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>

            {/* Col 3: Library & Videos */}
            <div>
              <h3 className="text-white font-black text-[15px] uppercase tracking-wider mb-4">
                {t('Library')} &amp; {t('Videos Store')}
              </h3>
              <ul className="space-y-2.5 text-[15px]">
                {footerNewsCates.slice(0, 6).map((nc: any) => (
                  <li key={nc.news_cc_id}>
                    <Link
                      to={`/news/category/${(nc.news_cc_name_url || '').trim()}`}
                      className="hover:text-[#2ab4e8] transition-colors"
                    >
                      {lang === 'vi' ? nc.news_cc_name_vi || nc.news_cc_name : nc.news_cc_name}
                    </Link>
                  </li>
                ))}
                <li>
                  <Link to="/videos" className="text-[#2ab4e8] font-semibold hover:underline">
                    🎬 {t('Videos Store')} →
                  </Link>
                </li>
              </ul>
            </div>

            {/* Col 4: About & Ecosystem */}
            <div>
              <h3 className="text-white font-black text-[15px] uppercase tracking-wider mb-4">{t('About us')}</h3>
              <ul className="space-y-2.5 text-[15px]">
                {footerAboutItems.slice(0, 4).map((ab: any) => {
                  const title = lang === 'vi' ? ab.about_title_vi : ab.about_title_en;
                  const urlSlug = lang === 'vi' ? ab.about_title_url_vi : ab.about_title_url_en;
                  return (
                    <li key={ab.about_id}>
                      <Link to={`/about/${(urlSlug || '').trim()}`} className="hover:text-[#2ab4e8] transition-colors">
                        {title}
                      </Link>
                    </li>
                  );
                })}
                <li>
                  <Link to="/opening" className="hover:text-[#2ab4e8] transition-colors">
                    📅 {t('Openning Class')}
                  </Link>
                </li>
                <li>
                  <Link to="/sitemap" className="hover:text-[#2ab4e8] transition-colors">
                    🗺️ {t('Site map')}
                  </Link>
                </li>
                <li className="pt-2 flex flex-wrap gap-2">
                  <button
                    type="button"
                    onClick={() => window.dispatchEvent(new CustomEvent('tony-open-lms'))}
                    className="inline-flex items-center gap-1.5 bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold px-3 py-1.5 rounded-lg border border-slate-700 transition cursor-pointer"
                  >
                    🎓 {lang === 'vi' ? 'Góc Học Viên' : 'Student Portal'}
                  </button>
                  <button
                    type="button"
                    onClick={() => onNavigateLms?.(lmsRole === 'admin' ? 'admin' : 'admin-login')}
                    className="inline-flex items-center gap-1.5 bg-slate-800/70 hover:bg-slate-700 text-slate-300 text-xs font-bold px-3 py-1.5 rounded-lg border border-slate-700 transition cursor-pointer"
                  >
                    ⚙️ {lang === 'vi' ? 'Quản Trị' : 'Admin Setting'}
                  </button>
                </li>
              </ul>
            </div>
          </div>

          <div className="pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-500">
            <p>© 2013–2026 TonyEnglish.vn — The future begins here. All rights reserved.</p>
            <div className="flex items-center gap-4">
              <Link to="/sitemap" className="hover:text-slate-300">
                {t('Site map')}
              </Link>
              <span>•</span>
              <Link to="/contact" className="hover:text-slate-300">
                {t('Contact')}
              </Link>
            </div>
          </div>
        </div>
      </footer>

      {/* 5. UNIFIED LOGIN & FORGOT PASSWORD MODAL */}
      {loginModalOpen && (
        <div
          className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4"
          onClick={() => {
            setLoginModalOpen(false);
            setForgotPasswordMode(false);
          }}
        >
          <div
            className="bg-white rounded-3xl w-full max-w-md shadow-2xl overflow-hidden"
            onClick={(e) => e.stopPropagation()}
          >
            {!forgotPasswordMode ? (
              <>
                <div className="bg-slate-50 px-8 py-6 border-b border-slate-200 flex justify-between items-center">
                  <div>
                    <h2 className="text-2xl font-black text-slate-800">{t('Sign in')}</h2>
                    <p className="text-xs text-slate-500 mt-0.5">Đăng nhập vào Phòng Học &amp; Luyện Thi TonyEnglish</p>
                  </div>
                  <button
                    type="button"
                    onClick={() => setLoginModalOpen(false)}
                    className="text-slate-400 hover:text-red-500 text-2xl font-bold transition-colors"
                  >
                    &times;
                  </button>
                </div>

                <form onSubmit={handleLoginSubmit} className="p-8 space-y-5">
                  <div className="space-y-1.5">
                    <label className="text-xs font-bold text-slate-500 uppercase tracking-wider">
                      Email Học Viên / Username
                    </label>
                    <input
                      type="text"
                      required
                      placeholder="hocvien@tonyenglish.vn"
                      value={loginUsername}
                      onChange={(e) => setLoginUsername(e.target.value)}
                      className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#2ab4e8] text-sm font-medium bg-white"
                    />
                  </div>

                  <div className="space-y-1.5">
                    <div className="flex items-center justify-between">
                      <label className="text-xs font-bold text-slate-500 uppercase tracking-wider">
                        {t('Enter your password')}
                      </label>
                      <button
                        type="button"
                        onClick={() => {
                          setForgotPasswordMode(true);
                          setResetEmail(loginUsername);
                          setResetSentSuccess(false);
                          setResetError('');
                        }}
                        className="text-xs font-bold text-[#2ab4e8] hover:text-[#0a5482] transition-colors"
                      >
                        Quên mật khẩu?
                      </button>
                    </div>
                    <input
                      type="password"
                      required
                      placeholder="••••••••"
                      value={loginPassword}
                      onChange={(e) => setLoginPassword(e.target.value)}
                      className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#2ab4e8] text-sm font-medium bg-white"
                    />
                  </div>

                  {loginError && (
                    <div className="p-3 bg-rose-50 border border-rose-200 rounded-xl text-rose-700 text-xs font-bold">
                      {loginError}
                    </div>
                  )}

                  <button
                    type="submit"
                    disabled={loginLoading}
                    className="w-full bg-[#0a5482] hover:bg-[#084266] disabled:bg-slate-400 text-white font-black py-3.5 rounded-xl shadow-lg transition-transform active:scale-95 text-sm"
                  >
                    {loginLoading ? '⏳ ĐANG XỬ LÝ...' : 'ĐĂNG NHẬP VÀO LỚP HỌC ➜'}
                  </button>

                  <div className="pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-bold">
                    <Link
                      to="/courses/online"
                      onClick={() => setLoginModalOpen(false)}
                      className="text-[#0a5482] hover:underline"
                    >
                      💻 Các khóa học Online &amp; Học thử
                    </Link>
                    <Link
                      to="/courses"
                      onClick={() => setLoginModalOpen(false)}
                      className="text-slate-500 hover:text-[#0a5482] transition-colors"
                    >
                      Các khóa học Offline →
                    </Link>
                  </div>
                </form>
              </>
            ) : (
              <>
                <div className="bg-slate-50 px-8 py-6 border-b border-slate-200 flex justify-between items-center">
                  <div>
                    <h2 className="text-xl font-black text-slate-800">Khôi phục mật khẩu</h2>
                    <p className="text-xs text-slate-500 mt-0.5">Nhận liên kết đặt lại mật khẩu qua Email</p>
                  </div>
                  <button
                    type="button"
                    onClick={() => {
                      setForgotPasswordMode(false);
                      setLoginModalOpen(false);
                    }}
                    className="text-slate-400 hover:text-red-500 text-2xl font-bold transition-colors"
                  >
                    &times;
                  </button>
                </div>

                {resetSentSuccess ? (
                  <div className="p-8 text-center space-y-5">
                    <div className="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto text-3xl">
                      ✉️
                    </div>
                    <div className="space-y-2">
                      <h3 className="text-lg font-black text-slate-800">Đã gửi Email khôi phục!</h3>
                      <p className="text-sm text-slate-600 leading-relaxed">
                        Chúng tôi đã gửi liên kết đặt lại mật khẩu tới{' '}
                        <span className="font-bold text-[#0a5482]">{resetEmail.trim()}</span>. Vui lòng kiểm tra hộp thư
                        đến (hoặc mục Spam/Quảng cáo).
                      </p>
                    </div>
                    <button
                      type="button"
                      onClick={() => {
                        setForgotPasswordMode(false);
                        setResetSentSuccess(false);
                      }}
                      className="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-3.5 rounded-xl transition text-sm"
                    >
                      ← Quay lại Đăng nhập
                    </button>
                  </div>
                ) : (
                  <form onSubmit={handleForgotPassword} className="p-8 space-y-5">
                    <p className="text-sm text-slate-600 leading-relaxed">
                      Nhập địa chỉ Email tài khoản học viên của bạn. Hệ thống sẽ gửi đường dẫn để bạn tạo mật khẩu mới.
                    </p>
                    <div className="space-y-1.5">
                      <label className="text-xs font-bold text-slate-500 uppercase tracking-wider">Email của bạn</label>
                      <input
                        type="email"
                        required
                        placeholder="hocvien@tonyenglish.vn"
                        value={resetEmail}
                        onChange={(e) => setResetEmail(e.target.value)}
                        className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#2ab4e8] text-sm font-medium"
                      />
                    </div>
                    {resetError && (
                      <div className="p-3 bg-rose-50 border border-rose-200 rounded-xl text-rose-600 text-xs font-semibold">
                        ⚠️ {resetError}
                      </div>
                    )}
                    <button
                      type="submit"
                      disabled={isResetting}
                      className="w-full bg-[#0a5482] hover:bg-[#084266] disabled:bg-slate-400 text-white font-black py-3.5 rounded-xl shadow-lg transition-transform active:scale-95 text-sm"
                    >
                      {isResetting ? '⏳ ĐANG GỬI EMAIL...' : 'GỬI LIÊN KẾT ĐẶT LẠI MẬT KHẨU'}
                    </button>
                    <button
                      type="button"
                      onClick={() => setForgotPasswordMode(false)}
                      className="w-full text-center text-sm font-bold text-slate-500 hover:text-slate-800 transition-colors pt-1"
                    >
                      ← Quay lại màn hình Đăng nhập
                    </button>
                  </form>
                )}
              </>
            )}
          </div>
        </div>
      )}

      {/* 6. DICTIONARY POPUP MODAL */}
      {popupModal && (
        <div
          className="fixed inset-0 bg-slate-900/20 z-50 flex items-center justify-center p-3 sm:p-6"
          onClick={() => setPopupModal(null)}
        >
          <div
            className="bg-white rounded-xl border-2 border-slate-300 w-full max-w-[920px] h-[82vh] max-h-[720px] shadow-2xl flex flex-col overflow-hidden"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="px-5 py-2.5 bg-white border-b border-slate-300 flex flex-wrap items-center justify-between gap-2.5 shrink-0">
              <div className="flex items-center gap-2.5 min-w-0">
                <img
                  src="/logo-text.png"
                  onError={(e) => {
                    (e.currentTarget as HTMLImageElement).style.display = 'none';
                  }}
                  alt="TONYENGLISH"
                  className="h-6 w-auto object-contain"
                />
                <img
                  src="/logo-shield-old.png"
                  onError={(e) => {
                    (e.currentTarget as HTMLImageElement).src = '/logo-shield.png';
                  }}
                  alt="TonyEnglish"
                  className="h-6 w-auto object-contain"
                />
                <span className="hidden sm:inline-block text-slate-300 mx-0.5">|</span>
                <h3 className="font-bold text-[#0a5482] text-xs sm:text-sm truncate">{popupModal.title}</h3>
              </div>

              <div className="flex items-center gap-2 ml-auto">
                <form
                  onSubmit={(e) => {
                    e.preventDefault();
                    const cleanWord = searchQuery
                      .trim()
                      .replace(/^[^a-zA-Z0-9À-ỹ]+|[^a-zA-Z0-9À-ỹ]+$/g, '')
                      .toLowerCase();
                    if (cleanWord) {
                      setPopupModal({
                        title: `${t('Look up dictionary')}: "${cleanWord}"`,
                        url: `https://dic.tienganh123.com/fast_dict.php?word=${encodeURIComponent(cleanWord)}&dict=ev_ve&m=yes`,
                      });
                    }
                  }}
                  className="flex items-center bg-white border-2 border-[#0a5482]/35 rounded-xl overflow-hidden focus-within:border-[#2ab4e8] shadow-2xs"
                >
                  <input
                    type="text"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    autoCapitalize="none"
                    autoCorrect="off"
                    spellCheck={false}
                    placeholder={lang === 'vi' ? 'Nhập từ khác...' : 'Type another word...'}
                    className="px-2.5 py-1 text-xs sm:text-sm text-slate-800 w-28 sm:w-44 focus:outline-none"
                  />
                  <button
                    type="submit"
                    className="px-3 py-1 bg-[#0a5482] hover:bg-[#084266] text-white text-xs font-bold cursor-pointer"
                  >
                    Tra
                  </button>
                </form>

                <button
                  type="button"
                  onClick={() =>
                    setPopupModal({
                      title: t('Look up dictionary'),
                      url: 'https://dic.tienganh123.com/v2/',
                    })
                  }
                  className="hidden sm:inline-flex items-center gap-1 px-2.5 py-1 rounded-xl bg-sky-50 hover:bg-sky-100 text-[#0a5482] border border-sky-300 text-xs font-bold cursor-pointer"
                  title="Mở giao diện từ điển đầy đủ"
                >
                  📖 Khung đầy đủ
                </button>

                <button
                  type="button"
                  onClick={() => setPopupModal(null)}
                  className="p-1 hover:opacity-80 transition-opacity cursor-pointer shrink-0"
                  title="Đóng (Esc)"
                >
                  <img
                    src="https://dic.tienganh123.com/image/close.gif"
                    alt="Close"
                    className="w-5 h-5 block"
                  />
                </button>
              </div>
            </div>
            {popupModal.url && (
              <iframe
                src={popupModal.url}
                className="w-full flex-1 border-0 bg-white"
                title={popupModal.title}
              />
            )}
          </div>
        </div>
      )}

      {/* 7. DOUBLE-CLICK QUICK DICTIONARY POPUP (autosearch.js replica with TonyEnglish branding) */}
      {quickDict && (
        <div
          id="addVdictOnYourWeb"
          style={{
            background: '#FFF',
            position: 'absolute',
            border: '1px solid #CCC',
            left: `${quickDict.x}px`,
            top: `${quickDict.y}px`,
            width: '315px',
            padding: '2px',
            zIndex: 999999,
            boxShadow: '0 6px 24px rgba(0,0,0,0.18)',
          }}
        >
          <div
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              background: '#ffffff',
              padding: '3px 4px 4px 6px',
              borderBottom: '1px solid #CCC',
            }}
          >
            <div
              onClick={() => {
                setPopupModal({
                  title: t('Look up dictionary'),
                  url: 'https://dic.tienganh123.com/v2/',
                });
                setQuickDict(null);
              }}
              style={{ display: 'flex', alignItems: 'center', gap: '5px', cursor: 'pointer' }}
              title="Bấm để mở Từ điển lớn"
            >
              <img
                src="/logo-text.png"
                alt="TONYENGLISH"
                style={{ height: '20px', width: 'auto', objectFit: 'contain' }}
              />
              <img
                src="/logo-shield-old.png"
                alt="Shield"
                style={{ height: '20px', width: 'auto', objectFit: 'contain' }}
              />
            </div>
            <button
              type="button"
              onClick={() => setQuickDict(null)}
              style={{
                border: 'none',
                background: 'transparent',
                padding: 0,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
              }}
              title="Đóng (Esc)"
            >
              <img
                src="https://dic.tienganh123.com/image/close.gif"
                alt="Close"
                style={{ width: '16px', height: '16px', display: 'block' }}
              />
            </button>
          </div>
          <div style={{ background: '#fff', width: '100%', height: '205px' }}>
            <iframe
              src={`https://dic.tienganh123.com/fast_dict.php?word=${encodeURIComponent(quickDict.word)}&dict=ev_ve&m=yes`}
              style={{
                width: '100%',
                height: '205px',
                border: 0,
              }}
              title={`Quick Lookup: ${quickDict.word}`}
            />
          </div>
        </div>
      )}
    </div>
  );
};
