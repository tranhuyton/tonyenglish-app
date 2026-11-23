import React, { useState, useEffect } from 'react';

export type AppLang = 'vi' | 'en';

export const LANG_STORAGE_KEY = 'te_lang';
export const LANG_CHANGE_EVENT = 'tony-lang-change';

export function getLmsLang(): AppLang {
  try {
    const saved = localStorage.getItem(LANG_STORAGE_KEY);
    return saved === 'en' ? 'en' : 'vi';
  } catch {
    return 'vi';
  }
}

export function setGlobalLang(next: AppLang): void {
  try {
    localStorage.setItem(LANG_STORAGE_KEY, next);
  } catch {}
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent<AppLang>(LANG_CHANGE_EVENT, { detail: next }));
  }
}

export function useLmsLang(): [AppLang, (next: AppLang) => void] {
  const [lang, setLangState] = useState<AppLang>(() => getLmsLang());

  useEffect(() => {
    const onCustom = (e: Event) => {
      const ce = e as CustomEvent<AppLang>;
      if (ce.detail === 'en' || ce.detail === 'vi') {
        setLangState(ce.detail);
      } else {
        setLangState(getLmsLang());
      }
    };
    const onStorage = (e: StorageEvent) => {
      if (e.key === LANG_STORAGE_KEY) {
        setLangState(e.newValue === 'en' ? 'en' : 'vi');
      }
    };
    window.addEventListener(LANG_CHANGE_EVENT, onCustom);
    window.addEventListener('storage', onStorage);
    return () => {
      window.removeEventListener(LANG_CHANGE_EVENT, onCustom);
      window.removeEventListener('storage', onStorage);
    };
  }, []);

  const updateLang = (next: AppLang) => {
    setLangState(next);
    setGlobalLang(next);
  };

  return [lang, updateLang];
}

/**
 * Localize course display title based on active UI language.
 * Rule:
 * - Individual IGCSE courses (e.g. IGCSE-Biology-0610, IGCSE - Maths-0580, IGCSE-ESL-0510...)
 *   keep their exact original English name in BOTH Vietnamese and English interfaces.
 * - All other courses dynamically localize their display name between VI and EN
 *   (e.g. "Grammar and Vocabulary" <-> "Ngữ pháp và Từ vựng").
 */
export function getLocalizedCourseTitle(rawTitle: string | null | undefined, lang: AppLang): string {
  const title = (rawTitle || '').trim();
  if (!title) return '';
  const low = title.toLowerCase();

  // Keep all individual IGCSE LMS courses unchanged in both VI and EN
  const isPublicPromoIgcse =
    low.includes('luyện thi') || low.includes('cấp tốc') || low.includes('intensive');
  if (low.includes('igcse') && !isPublicPromoIgcse) {
    return title;
  }

  // Public promo IGCSE / A-Level category
  if (low.includes('igcse') && isPublicPromoIgcse) {
    return lang === 'vi'
      ? 'Luyện thi IGCSE / A-Level cấp tốc'
      : 'Intensive IGCSE / A-Level Preparation';
  }

  // Exact & keyword mapping for all non-IGCSE courses (both LMS & Web categories)
  if (low === 'ielts premium' || low === 'luyện thi ielts chuyên sâu') {
    return lang === 'vi' ? 'Luyện thi IELTS Chuyên sâu' : 'IELTS Premium';
  }
  if (low === 'ielts' || low.includes('luyện thi ielts cấp tốc') || low.includes('intensive ielts')) {
    return lang === 'vi' ? 'Luyện thi IELTS cấp tốc' : 'Intensive IELTS Preparation';
  }
  if (
    low.includes('grammar and vocabulary') ||
    low.includes('ngữ pháp và từ vựng') ||
    low.includes('ngữ pháp & từ vựng')
  ) {
    return lang === 'vi' ? 'Ngữ pháp và Từ vựng' : 'Grammar and Vocabulary';
  }
  if (low === 'digital sat 1500+' || low === 'luyện thi digital sat 1500+') {
    return lang === 'vi' ? 'Luyện thi Digital SAT 1500+' : 'Digital SAT 1500+';
  }
  if (low.includes('luyện thi sat') || low.includes('intensive digital sat')) {
    return lang === 'vi' ? 'Luyện thi SAT cấp tốc' : 'Intensive Digital SAT 1500+ Preparation';
  }
  if (low === 'phát âm' || low === 'pronunciation') {
    return lang === 'vi' ? 'Phát Âm' : 'Pronunciation';
  }
  if (
    low.includes('giao tiếp và phản xạ') ||
    low.includes('communication & speaking reflex') ||
    low.includes('communication and speaking reflex')
  ) {
    return lang === 'vi' ? 'Giao tiếp và Phản xạ' : 'Communication & Speaking Reflex';
  }
  if (low === 'luyện phản xạ' || low === 'basic english' || low === 'speaking reflex') {
    return lang === 'vi' ? 'Luyện phản xạ' : 'Speaking Reflex';
  }
  if (
    low === 'tình huống giao tiếp' ||
    low === 'regular english' ||
    low === 'real-life conversations'
  ) {
    return lang === 'vi' ? 'Tình huống Giao tiếp' : 'Real-Life Conversations';
  }
  if (
    low === 'giao tiếp căn bản' ||
    low === 'english communication' ||
    low === 'basic english communication'
  ) {
    return lang === 'vi' ? 'Giao tiếp Căn bản' : 'Basic English Communication';
  }
  if (low === 'giao tiếp nâng cao' || low === 'advanced english communication') {
    return lang === 'vi' ? 'Giao tiếp Nâng cao' : 'Advanced English Communication';
  }
  if (
    low.includes('tiếng anh văn phòng') ||
    low.includes('office & business english') ||
    low.includes('business & office english') ||
    low === 'toeic'
  ) {
    return lang === 'vi' ? 'Tiếng Anh văn phòng' : 'Business & Office English';
  }
  if (
    low.includes('thành ngữ thông dụng') ||
    low.includes('idioms and phrases') ||
    low.includes('idioms & phrases')
  ) {
    return lang === 'vi' ? 'Thành ngữ thông dụng' : 'Idioms & Phrases';
  }
  if (
    low.includes('học viết email') ||
    low.includes('writing email') ||
    low.includes('business email writing')
  ) {
    return lang === 'vi' ? 'Học viết Email' : 'Business Email Writing';
  }
  if (
    low.includes('phỏng vấn xin việc') ||
    low.includes('job interview english') ||
    low.includes('job interview')
  ) {
    return lang === 'vi' ? 'Luyện Phỏng vấn Xin việc' : 'Job Interview English';
  }

  return title;
}

/** Compact VN | EN pill switcher for LMS headers (StudentPortal, LectureViewer, Test Runners) */
export const LmsLangToggle: React.FC<{
  lang: AppLang;
  setLang: (l: AppLang) => void;
  variant?: 'light' | 'dark';
  className?: string;
}> = ({ lang, setLang, variant = 'light', className = '' }) => {
  const isDark = variant === 'dark';
  return React.createElement(
    'div',
    {
      className: `inline-flex items-center p-0.5 rounded-lg border text-[11px] font-black shrink-0 ${
        isDark
          ? 'bg-slate-800/80 border-slate-700/80'
          : 'bg-slate-100 border-slate-200/90'
      } ${className}`,
      role: 'group',
      'aria-label': 'Language switch',
    },
    React.createElement(
      'button',
      {
        type: 'button',
        onClick: () => setLang('vi'),
        title: 'Tiếng Việt',
        className: `px-2 py-1 rounded-md transition-all cursor-pointer leading-none ${
          lang === 'vi'
            ? isDark
              ? 'bg-[#2ab4e8] text-white shadow-sm'
              : 'bg-[#0a5482] text-white shadow-sm'
            : isDark
            ? 'text-slate-300 hover:text-white'
            : 'text-slate-500 hover:text-slate-800'
        }`,
      },
      'VN'
    ),
    React.createElement(
      'button',
      {
        type: 'button',
        onClick: () => setLang('en'),
        title: 'English',
        className: `px-2 py-1 rounded-md transition-all cursor-pointer leading-none ${
          lang === 'en'
            ? isDark
              ? 'bg-[#2ab4e8] text-white shadow-sm'
              : 'bg-[#0a5482] text-white shadow-sm'
            : isDark
            ? 'text-slate-300 hover:text-white'
            : 'text-slate-500 hover:text-slate-800'
        }`,
      },
      'EN'
    )
  );
};
