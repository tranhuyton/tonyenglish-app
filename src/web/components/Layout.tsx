import React, { useState, useEffect, useRef } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import {
  Phone,
  MessageCircle,
  Search,
  BookOpen,
  GraduationCap,
  Settings,
  User,
  Sparkles,
  Globe,
  Video,
  Calendar,
  MapPin,
  Map as MapIcon,
  Gift,
  Lock,
  Mail,
  ArrowRight,
  ChevronDown,
  X,
} from 'lucide-react';
import { useApp } from '../context/AppContext';
import { supabase, isTonyEnglishAuthUser, isTonyEnglishAdmin, TONYENGLISH_APP_ID } from '../lib/supabase';

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

  // Always jump to top of page when navigating between routes (especially on mobile & SPA transitions)
  useEffect(() => {
    const scrollTopNow = () => {
      window.scrollTo({ top: 0, left: 0, behavior: 'auto' });
      document.documentElement.scrollTop = 0;
      document.body.scrollTop = 0;
    };
    scrollTopNow();
    const rafId = window.requestAnimationFrame(scrollTopNow);
    return () => window.cancelAnimationFrame(rafId);
  }, [location.pathname, location.search]);

  // LMS Supabase Auth State
  const [lmsRole, setLmsRole] = useState<'admin' | 'student' | null>(null);

  useEffect(() => {
    let active = true;

    const resolveLmsRole = async (authUser: any | null | undefined) => {
      if (!authUser || !isTonyEnglishAuthUser(authUser)) {
        if (active) setLmsRole(null);
        return;
      }
      try {
        const { data: profile } = await supabase
          .from('profiles')
          .select('role, status')
          .eq('id', authUser.id)
          .maybeSingle();
        if (!active) return;
        if (isTonyEnglishAdmin(authUser, profile)) {
          setLmsRole('admin');
        } else if (profile?.status !== 'inactive') {
          setLmsRole('student');
        } else {
          setLmsRole(null);
        }
      } catch (e) {
        console.warn('Session check warning:', e);
        if (active) {
          setLmsRole(isTonyEnglishAdmin(authUser, null) ? 'admin' : 'student');
        }
      }
    };

    const checkSession = async () => {
      try {
        const { data: { session } } = await supabase.auth.getSession();
        await resolveLmsRole(session?.user);
      } catch (e) {
        console.warn('Session check warning:', e);
      }
    };
    checkSession();

    const { data: { subscription } } = supabase.auth.onAuthStateChange((_event, session) => {
      resolveLmsRole(session?.user);
    });
    return () => {
      active = false;
      subscription.unsubscribe();
    };
  }, []);

  // Listen to custom event 'tony-open-lms' from anywhere in Web Portal
  useEffect(() => {
    const handleOpenLms = (e: Event) => {
      const customEvt = e as CustomEvent;
      if (lmsRole === 'admin' || lmsRole === 'student') {
        onNavigateLms?.('student-resume');
      } else {
        if (customEvt?.detail === 'register' || customEvt?.detail?.tab === 'register') {
          setAuthTab('register');
        }
        setForgotPasswordMode(false);
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
  const searchBarRef = useRef<HTMLDivElement | null>(null);
  const searchDropdownOpenRef = useRef(searchDropdownOpen);
  searchDropdownOpenRef.current = searchDropdownOpen;

  // Dictionary / Translate modal popup
  const [popupModal, setPopupModal] = useState<{ title: string; url?: string; content?: string } | null>(null);

  // Double-click quick lookup tooltip state (autosearch.js replica)
  const [quickDict, setQuickDict] = useState<{ word: string; x: number; y: number } | null>(null);
  const quickDictRef = useRef(quickDict);
  quickDictRef.current = quickDict;

  useEffect(() => {
    const handleDblClick = (e: MouseEvent) => {
      const target = e.target as HTMLElement | null;
      if (
        target &&
        (target.tagName === 'INPUT' ||
          target.tagName === 'TEXTAREA' ||
          target.isContentEditable ||
          target.closest('#addVdictOnYourWeb') ||
          target.closest('[role="dialog"]'))
      ) {
        return;
      }
      const selection = window.getSelection()?.toString().trim() || '';
      const cleanWord = selection.replace(/^[^a-zA-Z0-9À-ỹ]+|[^a-zA-Z0-9À-ỹ]+$/g, '').toLowerCase();
      if (cleanWord.length > 1 && cleanWord.length <= 40) {
        const margin = 8;
        const tipWidth = Math.min(326, window.innerWidth - margin * 2);
        const tipHeight = 250;
        let left = e.clientX + 12;
        let top = e.clientY + 12;
        if (left + tipWidth > window.innerWidth - margin) {
          left = e.clientX - tipWidth - 12;
        }
        left = Math.max(margin, Math.min(left, window.innerWidth - tipWidth - margin));
        if (top + tipHeight > window.innerHeight - margin) {
          top = e.clientY - tipHeight - 12;
        }
        top = Math.max(margin, Math.min(top, window.innerHeight - tipHeight - margin));
        setQuickDict({ word: cleanWord, x: Math.round(left), y: Math.round(top) });
      }
    };

    const handleMouseDown = (e: MouseEvent) => {
      const target = e.target as HTMLElement | null;
      if (quickDictRef.current && target && !target.closest('#addVdictOnYourWeb')) {
        setQuickDict(null);
      }
      if (searchDropdownOpenRef.current && searchBarRef.current && target && !searchBarRef.current.contains(target)) {
        setSearchDropdownOpen(false);
      }
    };

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.ctrlKey && e.shiftKey && (e.key === 'A' || e.key === 'a')) {
        const selection = window.getSelection()?.toString().trim() || '';
        const cleanWord = selection.replace(/^[^a-zA-Z0-9À-ỹ]+|[^a-zA-Z0-9À-ỹ]+$/g, '').toLowerCase();
        if (cleanWord.length > 1) {
          const margin = 8;
          const tipWidth = Math.min(326, window.innerWidth - margin * 2);
          const tipHeight = 250;
          setQuickDict({
            word: cleanWord,
            x: Math.max(margin, Math.round((window.innerWidth - tipWidth) / 2)),
            y: Math.max(margin, Math.round((window.innerHeight - tipHeight) / 2)),
          });
        }
      } else if (e.key === 'Escape') {
        if (quickDictRef.current) {
          e.stopPropagation();
          setQuickDict(null);
          return;
        }
        setSearchDropdownOpen(false);
        setPopupModal(null);
        setLoginModalOpen(false);
        setForgotPasswordMode(false);
        setMobileMenuOpen(false);
      }
    };

    document.addEventListener('dblclick', handleDblClick);
    document.addEventListener('mousedown', handleMouseDown);
    document.addEventListener('keydown', handleKeyDown);
    return () => {
      document.removeEventListener('dblclick', handleDblClick);
      document.removeEventListener('mousedown', handleMouseDown);
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  // Unified Login, Register & Forgot Password modal state
  const [authTab, setAuthTab] = useState<'login' | 'register'>('login');
  const [loginUsername, setLoginUsername] = useState('');
  const [loginPassword, setLoginPassword] = useState('');
  const [regFullName, setRegFullName] = useState('');
  const [regPhone, setRegPhone] = useState('');
  const [regEmail, setRegEmail] = useState('');
  const [regPassword, setRegPassword] = useState('');
  const [loginError, setLoginError] = useState('');
  const [loginLoading, setLoginLoading] = useState(false);

  const [forgotPasswordMode, setForgotPasswordMode] = useState(false);
  const [resetEmail, setResetEmail] = useState('');
  const [isResetting, setIsResetting] = useState(false);
  const [resetSentSuccess, setResetSentSuccess] = useState(false);
  const [resetError, setResetError] = useState('');

  useEffect(() => {
    if (!loginModalOpen) return;
    setLoginLoading(false);
    setLoginError('');
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    return () => {
      document.body.style.overflow = prevOverflow;
    };
  }, [loginModalOpen]);

  const handleRegisterSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoginError('');
    setLoginLoading(true);
    const cleanEmail = regEmail.trim().toLowerCase();
    const cleanName = regFullName.trim();
    const cleanPhone = regPhone.replace(/\D/g, '').trim();

    if (!cleanName || !cleanPhone || !cleanEmail || regPassword.length < 6) {
      setLoginError('Vui lòng điền đầy đủ Họ tên, Số điện thoại, Email và Mật khẩu (tối thiểu 6 ký tự).');
      setLoginLoading(false);
      return;
    }

    if (!/^\d{9,15}$/.test(cleanPhone)) {
      setLoginError('Số điện thoại không hợp lệ! Vui lòng chỉ nhập chữ số (9–15 số, ví dụ: 0987654321).');
      setLoginLoading(false);
      return;
    }

    try {
      const { data, error } = await supabase.auth.signUp({
        email: cleanEmail,
        password: regPassword,
        options: {
          data: {
            full_name: cleanName,
            phone: cleanPhone,
            role: 'student',
            account_type: 'online',
            app: TONYENGLISH_APP_ID,
          },
        },
      });

      if (error) throw error;

      if (data?.user) {
        if (!isTonyEnglishAuthUser(data.user)) {
          await supabase.auth.signOut();
          setLoginError(
            lang === 'vi'
              ? 'Email này thuộc hệ thống khác và không thể đăng ký tự động tại TonyEnglish. Vui lòng dùng email khác hoặc liên hệ Thầy Tony.'
              : 'This email belongs to another platform. Please use a different email address.'
          );
          setLoginLoading(false);
          return;
        }
        try {
          await supabase.from('profiles').upsert({
            id: data.user.id,
            email: cleanEmail,
            full_name: cleanName,
            phone: cleanPhone || null,
            role: 'student',
            status: 'active',
            avatar_url: JSON.stringify({ account_type: 'online', provider: 'email' }),
          });
        } catch (e) {}
        try {
          await supabase.rpc('update_user_profile', {
            target_user_id: data.user.id,
            new_full_name: cleanName,
            new_role: 'student',
            new_phone: cleanPhone,
          });
        } catch (e) {}
      }

      // Sign in immediately if session not returned directly
      if (!data?.session) {
        const { data: signInData, error: signInError } = await supabase.auth.signInWithPassword({
          email: cleanEmail,
          password: regPassword,
        });
        if (signInError || !signInData?.session) {
          setLoginError(
            lang === 'vi'
              ? 'Tài khoản đã được tạo! Vui lòng xác nhận email (nếu có) hoặc chuyển sang tab Đăng nhập.'
              : 'Account created! Please verify your email or sign in on the Sign In tab.'
          );
          setAuthTab('login');
          setLoginUsername(cleanEmail);
          setLoginLoading(false);
          return;
        }
      }

      setLoginModalOpen(false);
      try {
        const w = window as any;
        if (typeof w.gtag === 'function') {
          w.gtag('event', 'sign_up', {
            method: 'email',
            has_phone: Boolean(cleanPhone),
            signup_source: 'trial_modal',
          });
          w.gtag('event', 'generate_lead', {
            lead_source: 'trial_modal',
            has_phone: Boolean(cleanPhone),
          });
        }
      } catch (e) {}
      onNavigateLms?.('portal');
    } catch (err: any) {
      if (err?.message?.includes('already registered')) {
        setLoginError('Email này đã được đăng ký! Vui lòng chuyển sang tab Đăng nhập.');
      } else {
        setLoginError('Lỗi đăng ký: ' + (err?.message || 'Vui lòng thử lại.'));
      }
    } finally {
      setLoginLoading(false);
    }
  };

  const path = location.pathname;
  const lowerRoutePath = path.toLowerCase();
  const isHome = lowerRoutePath === '/' || lowerRoutePath === '/vi' || lowerRoutePath === '/en';
  const isCourses =
    lowerRoutePath.includes('/courses') ||
    lowerRoutePath.startsWith('/khoa-hoc') ||
    lowerRoutePath.startsWith('/hoc-thu') ||
    lowerRoutePath.startsWith('/dang-ky') ||
    lowerRoutePath.startsWith('/promo');
  const isNews = lowerRoutePath.includes('/news') || lowerRoutePath.includes('/view/');
  const isVideos = lowerRoutePath.includes('/videos') || lowerRoutePath.includes('/video') || lowerRoutePath.includes('/videocate');
  const isAbout = lowerRoutePath.includes('/about') || lowerRoutePath.includes('/opening') || lowerRoutePath.includes('/sitemap');
  const isContact = lowerRoutePath.includes('/contact');
  const isLecture = lowerRoutePath.startsWith('/user/lecture') || lowerRoutePath.startsWith('/trial');
  const isAdminCp = lowerRoutePath.startsWith('/admincp');

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
      localStorage.removeItem('tony_oauth_redirect_portal');
    } catch (e) {}

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
          if (!isTonyEnglishAuthUser(data.user)) {
            await supabase.auth.signOut();
            setLoginError(
              lang === 'vi'
                ? 'Tài khoản này chưa được đăng ký trên hệ thống TonyEnglish. Vui lòng sử dụng tài khoản học viên TonyEnglish hoặc đăng ký học thử mới.'
                : 'This account is not registered on TonyEnglish. Please sign in with a TonyEnglish student account or create a free trial account.'
            );
            setLoginLoading(false);
            return;
          }

          let profile: any = null;
          try {
            const profilePromise = supabase
              .from('profiles')
              .select('role, status')
              .eq('id', data.user.id)
              .maybeSingle();
            const profileTimeout = new Promise<any>((_, reject) =>
              setTimeout(() => reject('TIMEOUT'), 4000)
            );
            const res = await Promise.race([profilePromise, profileTimeout]);
            profile = res?.data;
          } catch (pErr) {
            console.warn('Profile status check warning:', pErr);
          }

          const isAdmin = isTonyEnglishAdmin(data.user, profile);

          if (!isAdmin && profile?.status === 'inactive') {
            await supabase.auth.signOut();
            setLoginError(
              '⛔ Tài khoản học của bạn hiện đang ở trạng thái TẠM DỪNG. Vui lòng liên hệ Thầy Tony để được kích hoạt lại!'
            );
            setLoginLoading(false);
            return;
          }

          setLoginModalOpen(false);
          if (isAdmin) {
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
    : 'R2B 2219, Royal City, 72 Nguyễn Trãi, Thanh Xuân, Hà Nội';
  const phoneText = options['company_tel'] || options['company_phone'] || '0935 058 688';
  const emailText = options['company_email'] || 'tranhuyton@gmail.com';
  const lowerPath = location.pathname.toLowerCase();
  const registerTrialTitle =
    lang === 'en'
      ? lowerPath.includes('igcse')
        ? 'IGCSE Free Trial Sign Up'
        : lowerPath.includes('ielts')
        ? 'IELTS Free Trial Sign Up'
        : 'Start Your Free Trial'
      : lowerPath.includes('igcse')
      ? 'Đăng ký học thử IGCSE'
      : lowerPath.includes('ielts')
      ? 'Đăng ký học thử IELTS'
      : 'Đăng ký học thử miễn phí';
  const registerTrialSub =
    lang === 'en'
      ? lowerPath.includes('igcse')
        ? 'Create a free account to try Bilingual IGCSE Lectures & Past Papers'
        : lowerPath.includes('ielts')
        ? 'Create a free account to try IELTS Mock Tests & 24/7 AI Grading'
        : 'Create a free account to explore Lectures, Past Papers & AI Exam Lab'
      : lowerPath.includes('igcse')
      ? 'Tạo tài khoản miễn phí để học thử Bài giảng & Kho đề IGCSE Online'
      : lowerPath.includes('ielts')
      ? 'Tạo tài khoản miễn phí để trải nghiệm Phòng thi IELTS & AI Chấm bài'
      : 'Tạo tài khoản miễn phí để trải nghiệm Bài giảng, Kho đề & Phòng thi AI';

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 text-slate-800 font-sans">
      {/* 1. COMPACT DESKTOP TOP UTILITY BAR (Hidden on Mobile for Clean Above-the-Fold UX) */}
      <div className="hidden md:block bg-[#0f172a] text-slate-300 border-b border-slate-800/90 text-[12.5px]">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 h-10 flex items-center justify-between gap-3">
          {/* Left info */}
          <div className="flex items-center gap-4">
            <a
              href="tel:0935058688"
              className="inline-flex items-center gap-1.5 text-slate-200 hover:text-[#2ab4e8] font-semibold transition"
            >
              <Phone className="w-3.5 h-3.5 text-[#2ab4e8]" />
              <span>{phoneText}</span>
            </a>
            <a
              href="https://zalo.me/0935058688"
              target="_blank"
              rel="noreferrer"
              className="hidden lg:inline-flex items-center gap-1.5 text-cyan-300 hover:text-white font-semibold transition"
            >
              <MessageCircle className="w-3.5 h-3.5" />
              <span>Zalo: 0935 058 688</span>
            </a>
            <span className="hidden xl:inline-flex items-center gap-1.5 bg-slate-800/90 text-sky-300 px-3 py-0.5 rounded-full text-[11.5px] font-semibold border border-slate-700/80">
              <Sparkles className="w-3 h-3 text-[#2ab4e8]" />
              <span>{lang === 'vi' ? 'Click đúp vào từ tiếng Anh bất kỳ để tra từ điển' : 'Double-click any English word to look up'}</span>
            </span>
          </div>

          {/* Right tools: Search/Dictionary + Course selector + Language */}
          <div className="flex items-center justify-end gap-2.5 ml-auto">
            {/* Smart Dictionary & Search Bar */}
            <div ref={searchBarRef} className="relative flex items-center bg-slate-800/95 border border-slate-700 hover:border-[#2ab4e8]/70 rounded-lg focus-within:border-[#2ab4e8] focus-within:ring-2 focus-within:ring-[#2ab4e8]/20 transition-all">
              <button
                type="button"
                onClick={() => setSearchDropdownOpen(!searchDropdownOpen)}
                className="px-2.5 py-1 text-[11.5px] font-bold text-[#2ab4e8] border-r border-slate-700 hover:bg-slate-700/60 rounded-l-lg flex items-center gap-1 whitespace-nowrap shrink-0 cursor-pointer"
                title="Chọn chế độ tra cứu"
              >
                {searchMode === 'dic' ? <BookOpen className="w-3.5 h-3.5" /> : searchMode === 'web' ? <Search className="w-3.5 h-3.5" /> : <Globe className="w-3.5 h-3.5" />}
                <span>
                  {searchMode === 'dic'
                    ? lang === 'vi'
                      ? 'Từ điển'
                      : 'Dict'
                    : searchMode === 'web'
                    ? lang === 'vi'
                      ? 'Tìm bài'
                      : 'Search'
                    : lang === 'vi'
                    ? 'Dịch'
                    : 'Translate'}
                </span>
                <ChevronDown className="w-3 h-3 opacity-75" />
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
                className="bg-transparent text-white placeholder-slate-400 text-[12.5px] px-2.5 py-1 w-44 lg:w-52 focus:outline-none"
              />
              <button
                type="button"
                onClick={() => handleSearchSubmit()}
                className="px-2.5 py-1 text-slate-300 hover:text-white hover:bg-[#0a5482] rounded-r-lg transition-colors shrink-0 cursor-pointer"
                title="Tra cứu"
              >
                <Search className="w-3.5 h-3.5" />
              </button>

              {searchDropdownOpen && (
                <div className="absolute right-0 top-full mt-1.5 w-56 bg-white text-slate-800 rounded-xl shadow-xl border border-slate-200 py-1.5 z-50 animate-in fade-in slide-in-from-top-2">
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
                    className={`w-full text-left px-3.5 py-2.5 text-[13px] font-semibold flex items-center justify-between hover:bg-slate-50 cursor-pointer ${
                      searchMode === 'dic' ? 'text-[#0a5482] bg-sky-50/60' : 'text-slate-700'
                    }`}
                  >
                    <span className="inline-flex items-center gap-2"><BookOpen className="w-4 h-4 text-[#0a5482]" /> {t('Look up dictionary')}</span>
                    {searchMode === 'dic' && <span className="text-[#2ab4e8] font-black">✓</span>}
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      setSearchMode('web');
                      setSearchDropdownOpen(false);
                    }}
                    className={`w-full text-left px-3.5 py-2.5 text-[13px] font-semibold flex items-center justify-between hover:bg-slate-50 cursor-pointer ${
                      searchMode === 'web' ? 'text-[#0a5482] bg-sky-50/60' : 'text-slate-700'
                    }`}
                  >
                    <span className="inline-flex items-center gap-2"><Search className="w-4 h-4 text-[#0a5482]" /> {t('TonyEnglish.vn search')}</span>
                    {searchMode === 'web' && <span className="text-[#2ab4e8] font-black">✓</span>}
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      setSearchMode('trans');
                      setSearchDropdownOpen(false);
                      window.open('https://translate.google.com/?hl=en&tab=wT#en/vi/', '_blank');
                    }}
                    className={`w-full text-left px-3.5 py-2.5 text-[13px] font-semibold flex items-center justify-between hover:bg-slate-50 cursor-pointer ${
                      searchMode === 'trans' ? 'text-[#0a5482] bg-sky-50/60' : 'text-slate-700'
                    }`}
                  >
                    <span className="inline-flex items-center gap-2"><Globe className="w-4 h-4 text-[#0a5482]" /> {t('Google translate')}</span>
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
                className="bg-slate-800 text-sky-300 border border-slate-700 rounded-lg px-2.5 py-1 text-xs font-semibold focus:outline-none"
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
                className={`px-2 py-0.5 rounded-md text-[11px] font-bold transition-all cursor-pointer ${
                  lang === 'vi' ? 'bg-[#2ab4e8] text-white shadow-sm' : 'text-slate-400 hover:text-white'
                }`}
              >
                VN
              </button>
              <button
                type="button"
                onClick={() => setLang('en')}
                className={`px-2 py-0.5 rounded-md text-[11px] font-bold transition-all cursor-pointer ${
                  lang === 'en' ? 'bg-[#2ab4e8] text-white shadow-sm' : 'text-slate-400 hover:text-white'
                }`}
              >
                EN
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* 2. MAIN STICKY GLASSMORPHIC NAVBAR */}
      <nav className="bg-white/90 backdrop-blur-lg border-b border-slate-200/80 sticky top-0 z-40 shadow-2xs">
        <div className="max-w-7xl mx-auto px-3 sm:px-6 h-16 sm:h-[74px] flex items-center justify-between gap-1.5 sm:gap-4">
          {/* Brand Logo */}
          <Link to="/" className="flex items-center gap-1.5 sm:gap-2.5 xl:gap-3 hover:opacity-90 transition-opacity shrink-0 min-w-0">
            <img
              src="/logo-shield.png"
              onError={(e) => {
                const img = e.currentTarget as HTMLImageElement;
                img.onerror = null;
                img.src = '/themes/tony/assets/img/logo%20khong%20chu.png';
              }}
              alt="TonyEnglish"
              className="h-7 sm:h-9 xl:h-10 w-auto object-contain shrink-0"
            />
            <div className="flex flex-col items-start leading-none">
              <div className="font-display font-black text-[16px] sm:text-[21px] xl:text-[24px] tracking-tight whitespace-nowrap">
                <span className="text-[#2ab4e8]">TONY</span>
                <span className="text-[#0a5482]">ENGLISH</span>
              </div>
              <span className="text-[9px] xl:text-[10.5px] font-bold uppercase tracking-wider xl:tracking-widest text-slate-400 mt-0.5 hidden sm:block">
                The future begins here
              </span>
            </div>
          </Link>

          {/* Desktop Navigation Links */}
          <div className="hidden lg:flex items-center gap-0.5 xl:gap-1">
            {navItems.map((item) => (
              <Link
                key={item.to}
                to={item.to}
                className={`px-3 xl:px-3.5 py-2 rounded-xl text-[13.5px] xl:text-[14.5px] font-bold transition-all whitespace-nowrap ${
                  item.active
                    ? 'bg-sky-50 text-[#0a5482] shadow-2xs border border-sky-200/70'
                    : 'text-slate-600 hover:text-[#0a5482] hover:bg-slate-50 border border-transparent'
                }`}
              >
                {item.label}
              </Link>
            ))}

            {user && (
              <Link
                to="/user/lecture"
                className={`px-3 xl:px-3.5 py-2 rounded-xl text-[13.5px] xl:text-[14.5px] font-bold transition-all whitespace-nowrap inline-flex items-center gap-1.5 ${
                  isLecture
                    ? 'bg-sky-50 text-[#0a5482] border border-sky-200/70'
                    : 'text-slate-600 hover:text-[#0a5482] hover:bg-slate-50 border border-transparent'
                }`}
              >
                <BookOpen className="w-4 h-4 text-[#2ab4e8]" />
                <span>{t('Lectures')}</span>
              </Link>
            )}
          </div>

          {/* Right Action Buttons (Unified LMS) */}
          <div className="flex items-center gap-1 sm:gap-2 shrink-0">
            {lmsRole ? (
              <>
                {lmsRole === 'admin' && (
                  <button
                    type="button"
                    onClick={() => onNavigateLms?.('student-resume')}
                    className="bg-emerald-50 hover:bg-emerald-100 text-emerald-700 text-[11px] sm:text-[13px] font-extrabold px-2 py-1.5 sm:px-3.5 sm:py-2 rounded-xl transition border border-emerald-200 shadow-2xs active:scale-95 whitespace-nowrap inline-flex items-center gap-1 sm:gap-1.5 cursor-pointer"
                  >
                    <GraduationCap className="w-4 h-4 hidden sm:inline" />
                    <span>{lang === 'vi' ? 'Góc Học Viên' : 'Student Portal'}</span>
                  </button>
                )}
                <button
                  type="button"
                  onClick={() => (lmsRole === 'admin' ? onNavigateLms?.('admin') : onNavigateLms?.('student-resume'))}
                  title={lmsRole === 'admin' ? (lang === 'vi' ? 'Quản Trị' : 'Admin Setting') : (lang === 'vi' ? 'Góc Học Viên' : 'Student Portal')}
                  className={`bg-gradient-to-r from-[#0a5482] to-[#1e74a8] hover:from-[#084266] hover:to-[#0a5482] text-white font-extrabold rounded-xl transition shadow-sm active:scale-95 whitespace-nowrap inline-flex items-center justify-center gap-1 sm:gap-1.5 cursor-pointer ${
                    lmsRole === 'admin'
                      ? 'text-[12px] sm:text-[14px] px-2 py-1.5 sm:px-3.5 sm:py-2.5'
                      : 'text-[11.5px] sm:text-[13.5px] px-2.5 py-1.5 sm:px-4 sm:py-2.5'
                  }`}
                >
                  {lmsRole === 'admin' ? (
                    <>
                      <Settings className="w-4 h-4" />
                      <span className="hidden 2xl:inline">
                        {lang === 'vi' ? 'Quản Trị' : 'Admin'}
                      </span>
                    </>
                  ) : (
                    <>
                      <GraduationCap className="w-3.5 h-3.5 sm:w-4 sm:h-4 text-[#2ab4e8]" />
                      <span>{lang === 'vi' ? 'Góc Học Viên' : 'Student Portal'}</span>
                      <ArrowRight className="w-3.5 h-3.5 hidden sm:inline" />
                    </>
                  )}
                </button>
              </>
            ) : user ? (
              <div className="flex items-center gap-1.5 sm:gap-2">
                <Link
                  to="/user/profile"
                  className="bg-slate-100 hover:bg-slate-200 text-[#0a5482] text-xs sm:text-[14px] font-bold px-2.5 py-1.5 sm:px-3.5 sm:py-2 rounded-xl transition flex items-center gap-1.5"
                >
                  <User className="w-4 h-4" />
                  <span className="max-w-[76px] sm:max-w-[120px] truncate">
                    {user.user_fullname?.trim() ? user.user_fullname.trim().split(' ').slice(-1)[0] : user.user_name}
                  </span>
                </Link>
              </div>
            ) : (
              <div className="flex items-center gap-1.5 sm:gap-2">
                <button
                  type="button"
                  onClick={() => {
                    setAuthTab('register');
                    setForgotPasswordMode(false);
                    setLoginModalOpen(true);
                  }}
                  className="hidden sm:inline-flex items-center gap-1.5 bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200/90 text-[13px] font-extrabold px-3.5 min-h-[40px] py-2 rounded-xl transition active:scale-95 whitespace-nowrap cursor-pointer"
                >
                  <Gift className="w-3.5 h-3.5 text-amber-600 shrink-0" />
                  <span>{lang === 'vi' ? 'Học thử' : 'Trial'}</span>
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setAuthTab('login');
                    setForgotPasswordMode(false);
                    setLoginModalOpen(true);
                  }}
                  className="bg-[#0a5482] hover:bg-[#084266] text-white text-[12px] sm:text-[14px] font-extrabold px-3 sm:px-4.5 min-h-[38px] sm:min-h-[40px] py-1.5 sm:py-2.5 rounded-xl transition shadow-sm active:scale-95 whitespace-nowrap cursor-pointer"
                >
                  {t('Login')}
                </button>
              </div>
            )}

            {/* Mobile Hamburger Button */}
            <button
              type="button"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="lg:hidden min-w-[38px] min-h-[38px] sm:min-w-[42px] sm:min-h-[42px] flex items-center justify-center rounded-xl text-slate-600 hover:bg-slate-100 cursor-pointer"
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

        {/* Mobile Dropdown Menu (Includes Search Mode Switcher + Language + Trial CTA) */}
        {mobileMenuOpen && (
          <div className="lg:hidden bg-white border-b border-slate-200 px-4 py-3.5 space-y-2.5 shadow-xl animate-in fade-in slide-in-from-top-2">
            {/* Mobile Quick Dictionary / Article Search / Translate */}
            <div className="space-y-2 pb-2.5 border-b border-slate-100">
              <div className="flex items-center justify-between gap-2">
                <div className="inline-flex items-center bg-slate-100 rounded-xl p-0.5 border border-slate-200/80 gap-0.5">
                  <button
                    type="button"
                    onClick={() => setSearchMode('dic')}
                    className={`px-2.5 py-1 rounded-lg text-[11.5px] font-bold transition cursor-pointer ${
                      searchMode === 'dic' ? 'bg-white text-[#0a5482] shadow-2xs' : 'text-slate-500'
                    }`}
                  >
                    {lang === 'vi' ? 'Từ điển' : 'Dict'}
                  </button>
                  <button
                    type="button"
                    onClick={() => setSearchMode('web')}
                    className={`px-2.5 py-1 rounded-lg text-[11.5px] font-bold transition cursor-pointer ${
                      searchMode === 'web' ? 'bg-white text-[#0a5482] shadow-2xs' : 'text-slate-500'
                    }`}
                  >
                    {lang === 'vi' ? 'Tìm bài' : 'Articles'}
                  </button>
                  <button
                    type="button"
                    onClick={() => setSearchMode('trans')}
                    className={`px-2.5 py-1 rounded-lg text-[11.5px] font-bold transition cursor-pointer ${
                      searchMode === 'trans' ? 'bg-white text-[#0a5482] shadow-2xs' : 'text-slate-500'
                    }`}
                  >
                    {lang === 'vi' ? 'Dịch' : 'Translate'}
                  </button>
                </div>

                <div className="flex items-center bg-slate-100 rounded-xl p-0.5 border border-slate-200 shrink-0">
                  <button
                    type="button"
                    onClick={() => setLang('vi')}
                    className={`px-2 py-1 rounded-lg text-xs font-bold cursor-pointer ${lang === 'vi' ? 'bg-[#0a5482] text-white' : 'text-slate-500'}`}
                  >
                    VN
                  </button>
                  <button
                    type="button"
                    onClick={() => setLang('en')}
                    className={`px-2 py-1 rounded-lg text-xs font-bold cursor-pointer ${lang === 'en' ? 'bg-[#0a5482] text-white' : 'text-slate-500'}`}
                  >
                    EN
                  </button>
                </div>
              </div>

              <form
                onSubmit={(e) => {
                  handleSearchSubmit(e);
                  setMobileMenuOpen(false);
                }}
                className="flex items-center bg-slate-100 border border-slate-200 rounded-xl overflow-hidden focus-within:border-[#2ab4e8] focus-within:bg-white transition-colors"
              >
                <Search className="w-4 h-4 text-slate-400 shrink-0 ml-3" />
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder={
                    searchMode === 'dic'
                      ? t('Look up dictionary')
                      : searchMode === 'web'
                      ? t('TonyEnglish.vn search')
                      : t('Google translate')
                  }
                  className="bg-transparent text-slate-800 placeholder-slate-400 text-sm px-2.5 py-2.5 flex-1 min-w-0 focus:outline-none"
                />
                <button
                  type="submit"
                  className="px-3.5 py-2.5 bg-[#0a5482] hover:bg-[#084266] text-white text-xs font-extrabold shrink-0 cursor-pointer"
                >
                  {lang === 'vi' ? 'Tìm' : 'Go'}
                </button>
              </form>
            </div>

            {navItems.map((item) => (
              <Link
                key={item.to}
                to={item.to}
                onClick={() => setMobileMenuOpen(false)}
                className={`block px-3.5 py-2.5 rounded-xl text-[15px] font-bold ${
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
                  className="flex items-center gap-2 px-3.5 py-2.5 rounded-xl text-[15px] font-bold text-slate-700 hover:bg-slate-50"
                >
                  <BookOpen className="w-4 h-4 text-[#0a5482]" />
                  <span>{t('Lectures')}</span>
                </Link>
                <Link
                  to="/user/profile"
                  onClick={() => setMobileMenuOpen(false)}
                  className="flex items-center gap-2 px-3.5 py-2.5 rounded-xl text-[15px] font-bold text-slate-700 hover:bg-slate-50"
                >
                  <User className="w-4 h-4 text-[#0a5482]" />
                  <span>{t('Profile')}</span>
                </Link>
              </>
            )}

            {!lmsRole && !user && (
              <div className="pt-1">
                <button
                  type="button"
                  onClick={() => {
                    setMobileMenuOpen(false);
                    setAuthTab('register');
                    setForgotPasswordMode(false);
                    setLoginModalOpen(true);
                  }}
                  className="w-full py-2.5 px-4 rounded-xl bg-gradient-to-r from-amber-400 via-yellow-400 to-amber-500 text-slate-950 font-extrabold text-sm shadow-xs inline-flex items-center justify-center gap-2 cursor-pointer"
                >
                  <Gift className="w-4 h-4 shrink-0" />
                  <span>{lang === 'vi' ? 'Đăng ký Học thử Miễn phí' : 'Start Free Trial'}</span>
                </button>
              </div>
            )}

            <div className="pt-2 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-slate-500 px-1">
              <a href="tel:0935058688" className="inline-flex items-center gap-1.5 text-[#0a5482] font-bold">
                <Phone className="w-3.5 h-3.5" /> {phoneText}
              </a>
              <a href="https://zalo.me/0935058688" target="_blank" rel="noreferrer" className="inline-flex items-center gap-1.5 text-sky-600 font-bold">
                <MessageCircle className="w-3.5 h-3.5" /> {lang === 'vi' ? 'Zalo tư vấn' : 'Zalo Chat'}
              </a>
            </div>
          </div>
        )}
      </nav>

      {/* 3. MAIN PAGE CONTENT */}
      <main className="flex-1">{children}</main>

      {/* 4. MODERN UNIFIED FOOTER */}
      <footer className={`bg-[#0f172a] text-slate-400 pt-14 border-t border-slate-800 mt-16 ${isCourses ? 'pb-24 sm:pb-10' : 'pb-10'}`}>
        <div className="max-w-7xl mx-auto px-4 sm:px-6">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 pb-10 border-b border-slate-800">
            {/* Col 1: Brand & Contact */}
            <div className="space-y-4">
              <Link to="/" className="flex items-center gap-3">
                <img
                  src="/logo-shield.png"
                  onError={(e) => {
                    const img = e.currentTarget as HTMLImageElement;
                    img.onerror = null;
                    img.src = '/themes/tony/assets/img/logo%20khong%20chu.png';
                  }}
                  alt="TonyEnglish"
                  className="h-9 w-auto object-contain"
                />
                <div className="font-black text-2xl tracking-tight text-white">
                  <span className="text-[#2ab4e8]">TONY</span>ENGLISH
                </div>
              </Link>
              <p className="text-[15px] text-slate-300 leading-relaxed">
                {lang === 'vi'
                  ? 'Trang học liệu cá nhân & Lớp gia sư 1 kèm 1 cùng Thầy Tony (Tiếng Anh Giao Tiếp, IELTS, Cambridge IGCSE) tại nhà riêng R2B Royal City & Online.'
                  : 'Personal English resource hub & 1-on-1 private tutoring with Mr. Tony (Communication, IELTS & Cambridge IGCSE) at R2B Royal City Hanoi & Online.'}
              </p>
              <div className="space-y-2.5 text-sm text-slate-300 pt-1">
                <p className="flex items-start gap-2.5">
                  <MapPin className="w-4 h-4 text-[#2ab4e8] shrink-0 mt-0.5" />
                  <span>
                    {lang === 'vi' ? 'Địa chỉ:' : 'Address:'} {addressText}
                  </span>
                </p>
                <p className="flex items-center gap-2.5">
                  <Phone className="w-4 h-4 text-[#2ab4e8] shrink-0" />
                  <a href="tel:0935058688" className="hover:text-white transition">
                    {lang === 'vi' ? 'Liên hệ:' : 'Contact:'} {phoneText}
                  </a>
                </p>
                <p className="flex items-center gap-2.5">
                  <MessageCircle className="w-4 h-4 text-cyan-400 shrink-0" />
                  <a
                    href="https://zalo.me/0935058688"
                    target="_blank"
                    rel="noreferrer"
                    className="text-cyan-400 hover:text-cyan-300 font-semibold transition"
                  >
                    {lang === 'vi' ? 'Zalo tư vấn: 0935 058 688' : 'Zalo Consultation: 0935 058 688'}
                  </a>
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
                {footerCourses.slice(0, 6).map((c: any) => {
                  const rawLabel = lang === 'vi' ? c.cc_name_vi || c.cc_name : c.cc_name;
                  const cleanLabel = String(rawLabel || '')
                    .replace(/IGCSE\s*\/\s*Alevel/gi, 'IGCSE / A-Level')
                    .replace(/Giao Tiếp Căn bản/g, 'Giao tiếp Căn bản')
                    .trim();
                  const cleanSlugUrl = encodeURIComponent((c.cc_name_url || '').trim());
                  return (
                    <li key={c.cc_id}>
                      <Link to={`/courses/${cleanSlugUrl}`} className="hover:text-[#2ab4e8] transition-colors">
                        {cleanLabel}
                      </Link>
                    </li>
                  );
                })}
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
                  <Link to="/videos" className="inline-flex items-center gap-1.5 text-[#2ab4e8] font-semibold hover:underline">
                    <Video className="w-4 h-4 shrink-0" />
                    <span>{t('Videos Store')} →</span>
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
                  <Link to="/opening" className="inline-flex items-center gap-1.5 hover:text-[#2ab4e8] transition-colors">
                    <Calendar className="w-3.5 h-3.5 text-[#2ab4e8] shrink-0" />
                    <span>{t('Openning Class')}</span>
                  </Link>
                </li>
                <li>
                  <Link to="/sitemap" className="inline-flex items-center gap-1.5 hover:text-[#2ab4e8] transition-colors">
                    <MapIcon className="w-3.5 h-3.5 text-[#2ab4e8] shrink-0" />
                    <span>{t('Site map')}</span>
                  </Link>
                </li>
                <li className="pt-2 flex flex-wrap gap-2">
                  <button
                    type="button"
                    onClick={() => window.dispatchEvent(new CustomEvent('tony-open-lms'))}
                    className="inline-flex items-center gap-1.5 bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold px-3 py-1.5 rounded-lg border border-slate-700 transition cursor-pointer"
                  >
                    <GraduationCap className="w-3.5 h-3.5 text-[#2ab4e8]" />
                    <span>{lang === 'vi' ? 'Góc Học Viên' : 'Student Portal'}</span>
                  </button>
                  <button
                    type="button"
                    onClick={() => onNavigateLms?.(lmsRole === 'admin' ? 'admin' : 'admin-login')}
                    className="inline-flex items-center gap-1.5 bg-slate-800/70 hover:bg-slate-700 text-slate-300 text-xs font-bold px-3 py-1.5 rounded-lg border border-slate-700 transition cursor-pointer"
                  >
                    <Settings className="w-3.5 h-3.5 text-slate-400" />
                    <span>{lang === 'vi' ? 'Quản Trị' : 'Admin Setting'}</span>
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
          className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 animate-in fade-in"
          onClick={() => {
            setLoginModalOpen(false);
            setForgotPasswordMode(false);
          }}
        >
          <div
            role="dialog"
            aria-modal="true"
            className="bg-white rounded-3xl w-full max-w-md max-h-[90dvh] overflow-y-auto shadow-2xl border border-slate-200/80 animate-in zoom-in-95"
            onClick={(e) => e.stopPropagation()}
          >
            {!forgotPasswordMode ? (
              <>
                <div className="bg-slate-50/90 px-7 sm:px-8 pt-6 pb-4 border-b border-slate-200/80">
                  <div className="flex justify-between items-start mb-4">
                    <div>
                      <h2 className="text-xl sm:text-2xl font-black text-slate-800">
                        {authTab === 'login' ? t('Sign in') : registerTrialTitle}
                      </h2>
                      <p className="text-xs text-slate-500 mt-1 leading-relaxed">
                        {authTab === 'login'
                          ? lang === 'vi'
                            ? 'Đăng nhập vào Góc Học Viên & Hệ thống Luyện Thi TonyEnglish'
                            : 'Sign in to TonyEnglish Student Portal & AI Exam Lab'
                          : registerTrialSub}
                      </p>
                    </div>
                    <button
                      type="button"
                      onClick={() => setLoginModalOpen(false)}
                      className="text-slate-400 hover:text-red-500 text-2xl font-bold transition-colors leading-none cursor-pointer"
                    >
                      &times;
                    </button>
                  </div>

                  {/* Tabs: Đăng nhập / Đăng ký học thử */}
                  <div className="grid grid-cols-2 gap-1.5 bg-slate-200/70 p-1 rounded-xl">
                    <button
                      type="button"
                      onClick={() => {
                        setAuthTab('login');
                        setLoginError('');
                      }}
                      className={`py-2 px-2 rounded-lg text-xs font-extrabold transition-all inline-flex items-center justify-center gap-1.5 cursor-pointer ${
                        authTab === 'login'
                          ? 'bg-white text-[#0a5482] shadow-xs'
                          : 'text-slate-600 hover:text-slate-900'
                      }`}
                    >
                      <Lock className="w-3.5 h-3.5" />
                      <span>{lang === 'vi' ? 'Đăng nhập' : 'Sign in'}</span>
                    </button>
                    <button
                      type="button"
                      onClick={() => {
                        setAuthTab('register');
                        setLoginError('');
                      }}
                      className={`py-2 px-2 rounded-lg text-xs font-extrabold transition-all inline-flex items-center justify-center gap-1.5 cursor-pointer ${
                        authTab === 'register'
                          ? 'bg-white text-[#0a5482] shadow-xs'
                          : 'text-slate-600 hover:text-slate-900'
                      }`}
                    >
                      <Gift className="w-3.5 h-3.5 text-amber-600 shrink-0" />
                      <span className="whitespace-nowrap">{lang === 'vi' ? 'Đăng ký học thử' : 'Free Trial'}</span>
                    </button>
                  </div>
                </div>

                {authTab === 'login' ? (
                  <form onSubmit={handleLoginSubmit} className="p-7 sm:p-8 space-y-5">
                    <div className="space-y-1.5">
                      <label className="text-xs font-bold text-slate-500 uppercase tracking-wider">
                        {lang === 'vi' ? 'Email Học Viên / Username' : 'Student Email / Username'}
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
                          className="text-xs font-bold text-[#2ab4e8] hover:text-[#0a5482] transition-colors cursor-pointer"
                        >
                          {lang === 'vi' ? 'Quên mật khẩu?' : 'Forgot password?'}
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
                      className="w-full bg-[#0a5482] hover:bg-[#084266] disabled:bg-slate-400 text-white font-black py-3.5 rounded-xl shadow-lg transition-transform active:scale-95 text-sm cursor-pointer"
                    >
                      {loginLoading
                        ? lang === 'vi'
                          ? 'ĐANG XỬ LÝ...'
                          : 'SIGNING IN...'
                        : lang === 'vi'
                        ? 'ĐĂNG NHẬP VÀO GÓC HỌC VIÊN →'
                        : 'SIGN IN TO STUDENT PORTAL →'}
                    </button>
                  </form>
                ) : (
                  <form onSubmit={handleRegisterSubmit} className="p-7 sm:p-8 space-y-4">
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                      <div className="space-y-1">
                        <label className="text-[11px] font-bold text-slate-500 uppercase tracking-wider">
                          {lang === 'vi' ? 'Họ và tên *' : 'Full Name *'}
                        </label>
                        <input
                          type="text"
                          required
                          placeholder={lang === 'vi' ? 'Nguyễn Văn A' : 'Your full name'}
                          value={regFullName}
                          onChange={(e) => setRegFullName(e.target.value)}
                          className="w-full border border-slate-300 rounded-xl px-3.5 py-2.5 outline-none focus:ring-2 focus:ring-[#2ab4e8] text-sm font-medium bg-white"
                        />
                      </div>
                      <div className="space-y-1">
                        <label className="text-[11px] font-bold text-slate-500 uppercase tracking-wider">
                          {lang === 'vi' ? 'Số điện thoại *' : 'Phone Number *'}
                        </label>
                        <input
                          type="tel"
                          required
                          inputMode="numeric"
                          pattern="[0-9]{9,15}"
                          maxLength={15}
                          placeholder="0987654321"
                          value={regPhone}
                          onChange={(e) => setRegPhone(e.target.value.replace(/\D/g, '').slice(0, 15))}
                          className="w-full border border-slate-300 rounded-xl px-3.5 py-2.5 outline-none focus:ring-2 focus:ring-[#2ab4e8] text-sm font-medium bg-white"
                        />
                      </div>
                    </div>

                    <div className="space-y-1">
                      <label className="text-[11px] font-bold text-slate-500 uppercase tracking-wider">
                        {lang === 'vi' ? 'Email đăng nhập *' : 'Email Address *'}
                      </label>
                      <input
                        type="email"
                        required
                        placeholder="email@gmail.com"
                        value={regEmail}
                        onChange={(e) => setRegEmail(e.target.value)}
                        className="w-full border border-slate-300 rounded-xl px-3.5 py-2.5 outline-none focus:ring-2 focus:ring-[#2ab4e8] text-sm font-medium bg-white"
                      />
                    </div>

                    <div className="space-y-1">
                      <label className="text-[11px] font-bold text-slate-500 uppercase tracking-wider">
                        {lang === 'vi' ? 'Mật khẩu (tối thiểu 6 ký tự) *' : 'Password (min 6 characters) *'}
                      </label>
                      <input
                        type="password"
                        required
                        minLength={6}
                        placeholder="••••••••"
                        value={regPassword}
                        onChange={(e) => setRegPassword(e.target.value)}
                        className="w-full border border-slate-300 rounded-xl px-3.5 py-2.5 outline-none focus:ring-2 focus:ring-[#2ab4e8] text-sm font-medium bg-white"
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
                      className="w-full bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-600 hover:to-yellow-600 disabled:bg-slate-400 text-slate-950 font-black py-3.5 rounded-xl shadow-lg transition-transform active:scale-95 text-sm cursor-pointer inline-flex items-center justify-center gap-2"
                    >
                      <Gift className="w-4 h-4 shrink-0" />
                      <span>
                        {loginLoading
                          ? lang === 'vi'
                            ? 'ĐANG TẠO TÀI KHOẢN...'
                            : 'CREATING ACCOUNT...'
                          : lang === 'vi'
                          ? 'ĐĂNG KÝ & VÀO HỌC THỬ NGAY →'
                          : 'CREATE FREE TRIAL ACCOUNT →'}
                      </span>
                    </button>
                  </form>
                )}
              </>
            ) : (
              <>
                <div className="bg-slate-50 px-8 py-6 border-b border-slate-200 flex justify-between items-center">
                  <div>
                    <h2 className="text-xl font-black text-slate-800">
                      {lang === 'vi' ? 'Khôi phục mật khẩu' : 'Reset Password'}
                    </h2>
                    <p className="text-xs text-slate-500 mt-0.5">
                      {lang === 'vi' ? 'Nhận liên kết đặt lại mật khẩu qua Email' : 'Receive a password reset link via email'}
                    </p>
                  </div>
                  <button
                    type="button"
                    onClick={() => {
                      setForgotPasswordMode(false);
                      setLoginModalOpen(false);
                    }}
                    className="text-slate-400 hover:text-red-500 text-2xl font-bold transition-colors cursor-pointer"
                  >
                    &times;
                  </button>
                </div>

                {resetSentSuccess ? (
                  <div className="p-8 text-center space-y-5">
                    <div className="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto">
                      <Mail className="w-7 h-7" />
                    </div>
                    <div className="space-y-2">
                      <h3 className="text-lg font-black text-slate-800">
                        {lang === 'vi' ? 'Đã gửi Email khôi phục!' : 'Recovery Email Sent!'}
                      </h3>
                      <p className="text-sm text-slate-600 leading-relaxed">
                        {lang === 'vi' ? (
                          <>
                            Hệ thống đã gửi liên kết đặt lại mật khẩu tới{' '}
                            <span className="font-bold text-[#0a5482]">{resetEmail.trim()}</span>. Vui lòng kiểm tra hộp thư
                            đến (hoặc mục Spam/Quảng cáo).
                          </>
                        ) : (
                          <>
                            We have sent a password reset link to{' '}
                            <span className="font-bold text-[#0a5482]">{resetEmail.trim()}</span>. Please check your inbox
                            (or Spam folder).
                          </>
                        )}
                      </p>
                    </div>
                    <button
                      type="button"
                      onClick={() => {
                        setForgotPasswordMode(false);
                        setResetSentSuccess(false);
                      }}
                      className="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-3.5 rounded-xl transition text-sm cursor-pointer"
                    >
                      {lang === 'vi' ? '← Quay lại Đăng nhập' : '← Back to Sign In'}
                    </button>
                  </div>
                ) : (
                  <form onSubmit={handleForgotPassword} className="p-8 space-y-5">
                    <p className="text-sm text-slate-600 leading-relaxed">
                      {lang === 'vi'
                        ? 'Nhập địa chỉ Email tài khoản học viên của bạn. Hệ thống sẽ gửi đường dẫn để bạn tạo mật khẩu mới.'
                        : 'Enter your student account email address and we will send you a link to set a new password.'}
                    </p>
                    <div className="space-y-1.5">
                      <label className="text-xs font-bold text-slate-500 uppercase tracking-wider">
                        {lang === 'vi' ? 'Email của bạn' : 'Your Email'}
                      </label>
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
                      className="w-full bg-[#0a5482] hover:bg-[#084266] disabled:bg-slate-400 text-white font-black py-3.5 rounded-xl shadow-lg transition-transform active:scale-95 text-sm cursor-pointer"
                    >
                      {isResetting
                        ? lang === 'vi'
                          ? 'ĐANG GỬI EMAIL...'
                          : 'SENDING EMAIL...'
                        : lang === 'vi'
                        ? 'GỬI LIÊN KẾT ĐẶT LẠI MẬT KHẨU'
                        : 'SEND PASSWORD RESET LINK'}
                    </button>
                    <button
                      type="button"
                      onClick={() => setForgotPasswordMode(false)}
                      className="w-full text-center text-sm font-bold text-slate-500 hover:text-slate-800 transition-colors pt-1 cursor-pointer"
                    >
                      {lang === 'vi' ? '← Quay lại màn hình Đăng nhập' : '← Back to Sign In'}
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
          className="fixed inset-0 bg-slate-900/45 backdrop-blur-xs z-50 flex items-center justify-center p-3 sm:p-6 animate-in fade-in"
          onClick={() => setPopupModal(null)}
        >
          <div
            role="dialog"
            aria-modal="true"
            className="bg-white rounded-2xl border border-slate-200/90 w-full max-w-[920px] h-[82vh] max-h-[720px] shadow-2xl flex flex-col overflow-hidden animate-in zoom-in-95"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="px-4 sm:px-5 py-3 bg-slate-50/90 border-b border-slate-200 flex flex-wrap items-center justify-between gap-2.5 shrink-0">
              <div className="flex items-center gap-2.5 min-w-0">
                <img
                  src="/logo-shield.png"
                  onError={(e) => {
                    const img = e.currentTarget as HTMLImageElement;
                    img.onerror = null;
                    img.src = '/themes/tony/assets/img/logo%20khong%20chu.png';
                  }}
                  alt="TonyEnglish"
                  className="h-6 w-auto object-contain shrink-0"
                />
                <div className="font-display font-black text-sm tracking-tight shrink-0">
                  <span className="text-[#2ab4e8]">TONY</span>
                  <span className="text-[#0a5482]">DICT</span>
                </div>
                <span className="hidden sm:inline-block text-slate-300 mx-0.5">|</span>
                <h3 className="font-bold text-slate-700 text-xs sm:text-sm truncate">{popupModal.title}</h3>
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
                  className="flex items-center bg-white border border-slate-300 rounded-xl overflow-hidden focus-within:border-[#2ab4e8] focus-within:ring-2 focus-within:ring-[#2ab4e8]/20 shadow-2xs transition-all"
                >
                  <input
                    type="text"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    autoCapitalize="none"
                    autoCorrect="off"
                    spellCheck={false}
                    placeholder={lang === 'vi' ? 'Nhập từ khác...' : 'Type another word...'}
                    className="px-2.5 py-1.5 text-xs sm:text-sm text-slate-800 w-28 sm:w-44 focus:outline-none"
                  />
                  <button
                    type="submit"
                    className="px-3 py-1.5 bg-[#0a5482] hover:bg-[#084266] text-white text-xs font-bold cursor-pointer transition-colors"
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
                  className="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-sky-50 hover:bg-sky-100 text-[#0a5482] border border-sky-200 text-xs font-bold cursor-pointer transition-colors"
                  title="Mở giao diện từ điển đầy đủ"
                >
                  <BookOpen className="w-3.5 h-3.5" />
                  <span>Khung đầy đủ</span>
                </button>

                <button
                  type="button"
                  onClick={() => setPopupModal(null)}
                  className="w-8 h-8 rounded-xl bg-white hover:bg-rose-50 text-slate-500 hover:text-rose-600 border border-slate-200 flex items-center justify-center transition-colors cursor-pointer shrink-0"
                  title="Đóng (Esc)"
                  aria-label="Đóng"
                >
                  <X className="w-4 h-4" />
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

      {/* 7. MODERN DOUBLE-CLICK QUICK DICTIONARY POPUP */}
      {quickDict && (
        <div
          id="addVdictOnYourWeb"
          style={{
            position: 'fixed',
            left: `${quickDict.x}px`,
            top: `${quickDict.y}px`,
            width: '326px',
            maxWidth: 'calc(100vw - 16px)',
            zIndex: 999999,
          }}
          className="bg-white rounded-2xl border border-slate-200/95 shadow-2xl overflow-hidden animate-in fade-in zoom-in-95"
        >
          <div className="flex items-center justify-between bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-3 py-2 text-white">
            <button
              type="button"
              onClick={() => {
                setPopupModal({
                  title: `${t('Look up dictionary')}: "${quickDict.word}"`,
                  url: `https://dic.tienganh123.com/fast_dict.php?word=${encodeURIComponent(quickDict.word)}&dict=ev_ve&m=yes`,
                });
                setQuickDict(null);
              }}
              className="flex items-center gap-2 min-w-0 cursor-pointer hover:opacity-90 transition-opacity"
              title="Bấm để mở Từ điển lớn"
            >
              <BookOpen className="w-3.5 h-3.5 text-[#2ab4e8] shrink-0" />
              <span className="text-xs font-extrabold tracking-tight truncate">
                Tra nhanh: <span className="text-sky-200">{quickDict.word}</span>
              </span>
            </button>
            <button
              type="button"
              onClick={() => setQuickDict(null)}
              className="w-6 h-6 rounded-lg bg-white/15 hover:bg-white/25 text-white flex items-center justify-center transition-colors cursor-pointer shrink-0 ml-2"
              title="Đóng (Esc)"
              aria-label="Đóng"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          </div>
          <div className="bg-white w-full h-[210px]">
            <iframe
              src={`https://dic.tienganh123.com/fast_dict.php?word=${encodeURIComponent(quickDict.word)}&dict=ev_ve&m=yes`}
              style={{
                width: '100%',
                height: '210px',
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
