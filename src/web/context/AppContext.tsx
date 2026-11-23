import React, { createContext, useContext, useState, useEffect } from 'react';
import { supabase } from '../lib/supabase';
import { encryptLegacyPass } from '../lib/utils';
import { t as translate } from '../lib/i18n';
import { LANG_CHANGE_EVENT, setGlobalLang } from '../../utils/lmsI18n';

export interface TeUser {
  user_id: number;
  user_name: string;
  user_fullname?: string;
  user_email: string;
  user_phone?: string;
  user_avatar?: string;
  user_birthday?: string;
  user_gender?: number;
  user_address?: string;
  user_job?: string;
  user_university?: string;
  user_highSchool?: string;
  user_about?: string;
  user_signal?: string;
  user_yahoo?: string;
  user_skype?: string;
  user_pass?: string;
  user_salt?: string;
  user_receive_mess?: number;
  user_openwindow_newmess?: number;
  user_default_language?: number;
  [key: string]: any;
}

export interface TeAdmin {
  admin_id: number;
  admin_name: string;
  admin_role?: string;
  [key: string]: any;
}

interface AppContextType {
  lang: 'vi' | 'en';
  setLang: (l: 'vi' | 'en') => void;
  t: (key: string) => string;
  user: TeUser | null;
  setUser: (u: TeUser | null) => void;
  admin: TeAdmin | null;
  setAdmin: (a: TeAdmin | null) => void;
  options: Record<string, string>;
  footerCourses: any[];
  footerNewsCates: any[];
  footerAboutCates: any[];
  footerAboutItems: any[];
  selectedCourseId: number | null;
  setSelectedCourseId: (id: number | null) => void;
  userCoursesList: any[];
  loginModalOpen: boolean;
  setLoginModalOpen: (open: boolean) => void;
  loginUser: (usernameOrEmail: string, pass: string) => Promise<{ ok: boolean; error?: string }>;
  logoutUser: () => void;
}

const DEFAULT_OPTIONS: Record<string, string> = {
  company_address: 'R2B 2219, Royal City, 72 Nguyễn Trãi, Thanh Xuân, Hà Nội',
  company_tel: '+84 93 505 8688',
  company_phone: '0935 058 688',
  company_email: 'tranhuyton@gmail.com',
};

function sanitizeTeUser(u: TeUser): TeUser {
  const { user_pass: _pass, user_salt: _salt, ...safeUser } = u;
  return safeUser as TeUser;
}

const AppContext = createContext<AppContextType | null>(null);

export const AppProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [lang, setLangState] = useState<'vi' | 'en'>(() => {
    return (localStorage.getItem('te_lang') as 'vi' | 'en') || 'vi';
  });
  const [user, setUserState] = useState<TeUser | null>(() => {
    try {
      const saved = localStorage.getItem('te_user');
      if (!saved) return null;
      const parsed = JSON.parse(saved);
      if (parsed && ('user_pass' in parsed || 'user_salt' in parsed)) {
        const cleaned = sanitizeTeUser(parsed);
        localStorage.setItem('te_user', JSON.stringify(cleaned));
        return cleaned;
      }
      return parsed;
    } catch {
      return null;
    }
  });
  const [admin, setAdminState] = useState<TeAdmin | null>(() => {
    try {
      const saved = localStorage.getItem('te_admin');
      return saved ? JSON.parse(saved) : null;
    } catch {
      return null;
    }
  });
  const [options, setOptions] = useState<Record<string, string>>(DEFAULT_OPTIONS);
  const [footerCourses, setFooterCourses] = useState<any[]>([]);
  const [footerNewsCates, setFooterNewsCates] = useState<any[]>([]);
  const [footerAboutCates, setFooterAboutCates] = useState<any[]>([]);
  const [footerAboutItems, setFooterAboutItems] = useState<any[]>([]);
  const [selectedCourseId, setSelectedCourseIdState] = useState<number | null>(() => {
    const saved = localStorage.getItem('te_cc_id');
    return saved ? parseInt(saved, 10) : null;
  });
  const [userCoursesList, setUserCoursesList] = useState<any[]>([]);
  const [loginModalOpen, setLoginModalOpen] = useState(false);

  const setLang = (l: 'vi' | 'en') => {
    setLangState(l);
    setGlobalLang(l);
  };

  useEffect(() => {
    const syncFromGlobal = (e: Event) => {
      const ce = e as CustomEvent<'vi' | 'en'>;
      if (ce.detail === 'en' || ce.detail === 'vi') {
        setLangState(ce.detail);
      }
    };
    window.addEventListener(LANG_CHANGE_EVENT, syncFromGlobal);
    return () => window.removeEventListener(LANG_CHANGE_EVENT, syncFromGlobal);
  }, []);

  const setUser = (u: TeUser | null) => {
    const safeUser = u ? sanitizeTeUser(u) : null;
    setUserState(safeUser);
    if (safeUser) localStorage.setItem('te_user', JSON.stringify(safeUser));
    else localStorage.removeItem('te_user');
  };

  const setAdmin = (a: TeAdmin | null) => {
    if (a) {
      const { admin_pass: _pass, admin_salt: _salt, ...safeAdmin } = a;
      setAdminState(safeAdmin as TeAdmin);
      localStorage.setItem('te_admin', JSON.stringify(safeAdmin));
    } else {
      setAdminState(null);
      localStorage.removeItem('te_admin');
    }
  };

  const setSelectedCourseId = (id: number | null) => {
    setSelectedCourseIdState(id);
    if (id !== null) localStorage.setItem('te_cc_id', String(id));
    else localStorage.removeItem('te_cc_id');
  };

  const t = (key: string) => translate(lang, key);

  useEffect(() => {
    async function loadGlobalLayoutData() {
      const [optRes, courseRes, newsCateRes, aboutCateRes, aboutRes] = await Promise.all([
        supabase.from('te_options').select('*').eq('language', lang),
        supabase
          .from('te_course_category')
          .select('cc_id,cc_name,cc_name_vi,cc_name_url,cc_code,cc_parent,cc_homedisplay,cc_order')
          .eq('deleted', 0)
          .eq('cc_status', 1)
          .eq('cc_parent', 0)
          .order('cc_order', { ascending: true }),
        supabase
          .from('te_news_category')
          .select('news_cc_id,news_cc_name,news_cc_name_vi,news_cc_name_url,news_cc_parent,news_cc_order_left')
          .eq('deleted', 0)
          .eq('news_cc_status', 1)
          .eq('news_cc_parent', 0)
          .order('news_cc_order_left', { ascending: true })
          .limit(6),
        supabase
          .from('te_about_category')
          .select('*')
          .eq('deleted', 0)
          .eq('ac_status', 1)
          .order('ac_order', { ascending: true }),
        supabase
          .from('te_about')
          .select('*')
          .eq('deleted', 0)
          .eq('about_status', 1)
          .order('about_order', { ascending: true }),
      ]);

      if (optRes.data) {
        const map: Record<string, string> = {};
        optRes.data.forEach((row: any) => {
          if (row.option_key && row.option_value !== null && row.option_value !== undefined && String(row.option_value).trim() !== '') {
            map[row.option_key] = row.option_value;
          }
        });
        setOptions((prev) => ({ ...DEFAULT_OPTIONS, ...prev, ...map }));
      }
      if (courseRes.data) {
        setFooterCourses(
          courseRes.data.filter(
            (c: any) =>
              Number(c.cc_id) !== 112 &&
              (c.cc_name_url || '').trim().toLowerCase() !== 'grammar-and-vocabulary'
          )
        );
      }
      if (newsCateRes.data) setFooterNewsCates(newsCateRes.data);
      if (aboutCateRes.data) setFooterAboutCates(aboutCateRes.data);
      if (aboutRes.data) setFooterAboutItems(aboutRes.data);
    }
    loadGlobalLayoutData();
  }, [lang]);

  useEffect(() => {
    async function loadUserCourses() {
      if (!user) {
        setUserCoursesList([]);
        return;
      }
      const { data: ucData } = await supabase
        .from('te_user_class')
        .select('cl_id')
        .eq('user_id', user.user_id);

      const clIds = (ucData || []).map((r: any) => r.cl_id);
      if (clIds.length > 0) {
        const { data: clData } = await supabase
          .from('te_class_category')
          .select('c_id')
          .in('cl_id', clIds)
          .eq('deleted', 0)
          .eq('cl_status', 1);
        const cIds = Array.from(new Set((clData || []).map((r: any) => r.c_id)));
        if (cIds.length > 0) {
          const { data: courses } = await supabase
            .from('te_course_category')
            .select('cc_id,cc_name,cc_name_vi,cc_name_url,cc_code')
            .in('cc_id', cIds);
          if (courses && courses.length > 0) {
            setUserCoursesList(courses);
            if (!selectedCourseId || !courses.some((c: any) => c.cc_id === selectedCourseId)) {
              setSelectedCourseId(courses[0].cc_id);
            }
            return;
          }
        }
      }
      // Fallback: load all courses with lectures so student/demo user can browse all lectures
      const { data: allSubCourses } = await supabase
        .from('te_course_category')
        .select('cc_id,cc_name,cc_name_vi,cc_name_url,cc_code')
        .eq('deleted', 0)
        .eq('cc_status', 1)
        .neq('cc_parent', 0)
        .order('cc_order', { ascending: true });
      if (allSubCourses && allSubCourses.length > 0) {
        const filteredSubs = allSubCourses.filter(
          (c: any) =>
            Number(c.cc_id) !== 112 &&
            Number(c.cc_parent) !== 112 &&
            (c.cc_name_url || '').trim().toLowerCase() !== 'grammar-and-vocabulary'
        );
        setUserCoursesList(filteredSubs);
        if (!selectedCourseId && filteredSubs.length > 0) setSelectedCourseId(filteredSubs[0].cc_id);
      }
    }
    loadUserCourses();
  }, [user]);

  const loginUser = async (usernameOrEmail: string, pass: string): Promise<{ ok: boolean; error?: string }> => {
    const clean = usernameOrEmail.trim();
    if (!clean || !pass) {
      return { ok: false, error: t('Please enter imformation!') };
    }
    // Find user safely via parameterized queries (no PostgREST .or() string interpolation)
    const [byEmailRes, byNameRes] = await Promise.all([
      supabase
        .from('te_user')
        .select('*')
        .eq('deleted', 0)
        .eq('user_email', clean)
        .limit(5),
      supabase
        .from('te_user')
        .select('*')
        .eq('deleted', 0)
        .eq('user_name', clean)
        .limit(5),
    ]);
    const seenIds = new Set<number>();
    const users: any[] = [];
    for (const row of [...(byEmailRes.data || []), ...(byNameRes.data || [])]) {
      if (!seenIds.has(row.user_id)) {
        seenIds.add(row.user_id);
        users.push(row);
      }
    }

    if (users.length === 0) {
      return { ok: false, error: lang === 'vi' ? 'Tài khoản hoặc email không tồn tại!' : 'User or Email does not exist!' };
    }

    for (const candidate of users) {
      const hashed = encryptLegacyPass(candidate.user_salt || '', pass);
      if (candidate.user_pass === hashed) {
        setUser(candidate);
        setLoginModalOpen(false);
        return { ok: true };
      }
    }
    return { ok: false, error: lang === 'vi' ? 'Mật khẩu không chính xác!' : 'Incorrect password!' };
  };

  const logoutUser = () => {
    setUser(null);
  };

  return (
    <AppContext.Provider
      value={{
        lang,
        setLang,
        t,
        user,
        setUser,
        admin,
        setAdmin,
        options,
        footerCourses,
        footerNewsCates,
        footerAboutCates,
        footerAboutItems,
        selectedCourseId,
        setSelectedCourseId,
        userCoursesList,
        loginModalOpen,
        setLoginModalOpen,
        loginUser,
        logoutUser,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useApp = () => {
  const ctx = useContext(AppContext);
  if (!ctx) throw new Error('useApp must be used within AppProvider');
  return ctx;
};
