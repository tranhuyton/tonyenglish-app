import React, { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';
import 'react-pdf/dist/Page/AnnotationLayer.css';
import 'react-pdf/dist/Page/TextLayer.css';

// Use same-origin local worker matched to react-pdf's bundled pdfjs-dist (5.4.296)
// for instant load & full iOS Safari compatibility (falls back to CDN if upgraded).
pdfjs.GlobalWorkerOptions.workerSrc =
  pdfjs.version === '5.4.296'
    ? '/pdf.worker-5.4.296.min.mjs'
    : `https://unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;

export type EbookTheme = 'light' | 'sepia' | 'dark';
export type EbookViewMode = 'page' | 'scroll';

export interface LibraryEbookViewerProps {
  pdfUrl: string;
  title: string;
  articleId: number | string;
  lang?: string;
  externalTheaterTrigger?: number;
  onEbookProgress?: (info: {
    currentPage: number;
    maxPage: number;
    totalPages: number | null;
    pagesTurned: number;
  }) => void;
}

const THEME_STORAGE_KEY = 'tony_ebook_theme';
const MODE_STORAGE_KEY = 'tony_ebook_view_mode';

const getInitialTheme = (): EbookTheme => {
  try {
    const saved = localStorage.getItem(THEME_STORAGE_KEY);
    if (saved === 'light' || saved === 'sepia' || saved === 'dark') return saved;
  } catch {}
  return 'light';
};

const getInitialViewMode = (): EbookViewMode => {
  try {
    const saved = localStorage.getItem(MODE_STORAGE_KEY);
    if (saved === 'page' || saved === 'scroll') return saved;
  } catch {}
  return 'page';
};

const ScrollPageSlot: React.FC<{
  pageNumber: number;
  shouldRender: boolean;
  width: number;
  estimatedHeight: number;
  devicePixelRatio: number;
  pageFilterClass: string;
  theme: EbookTheme;
  lang: string;
  onVisible: (pageNumber: number) => void;
  onPageMeasured: (aspectRatio: number) => void;
}> = React.memo(
  ({
    pageNumber,
    shouldRender,
    width,
    estimatedHeight,
    devicePixelRatio,
    pageFilterClass,
    theme,
    lang,
    onVisible,
    onPageMeasured,
  }) => {
    const slotRef = useRef<HTMLDivElement | null>(null);

    useEffect(() => {
      const el = slotRef.current;
      if (!el || typeof IntersectionObserver === 'undefined') return;
      const io = new IntersectionObserver(
        (entries) => {
          for (const entry of entries) {
            if (entry.isIntersecting && entry.intersectionRatio >= 0.35) {
              onVisible(pageNumber);
            }
          }
        },
        { threshold: [0.35, 0.6] }
      );
      io.observe(el);
      return () => io.disconnect();
    }, [pageNumber, onVisible]);

    const placeholderBg =
      theme === 'dark'
        ? 'bg-slate-900 border-slate-800 text-slate-500'
        : theme === 'sepia'
        ? 'bg-[#f6efe2] border-[#dfd2bc] text-[#8a7658]'
        : 'bg-white border-slate-200 text-slate-400';

    return (
      <div
        ref={slotRef}
        data-pdf-page={pageNumber}
        style={{
          width: `${width}px`,
          minHeight: `${estimatedHeight}px`,
        }}
        className={`relative mx-auto rounded-md overflow-hidden transition-shadow ${
          theme === 'dark'
            ? 'shadow-[0_8px_28px_rgba(0,0,0,0.6)]'
            : 'shadow-[0_6px_24px_rgba(15,23,42,0.12)]'
        }`}
      >
        {shouldRender ? (
          <div className={pageFilterClass}>
            <Page
              pageNumber={pageNumber}
              width={width}
              devicePixelRatio={devicePixelRatio}
              renderTextLayer={true}
              renderAnnotationLayer={true}
              onLoadSuccess={(page) => {
                if (page.originalWidth > 0 && page.originalHeight > 0) {
                  onPageMeasured(page.originalHeight / page.originalWidth);
                }
              }}
              className="bg-white"
              loading={
                <div
                  style={{ width: `${width}px`, height: `${estimatedHeight}px` }}
                  className={`flex flex-col items-center justify-center border ${placeholderBg}`}
                >
                  <span className="w-5 h-5 border-2 border-current/25 border-t-current rounded-full animate-spin mb-2" />
                  <span className="text-xs font-semibold">
                    {lang === 'vi' ? `Trang ${pageNumber}` : `Page ${pageNumber}`}
                  </span>
                </div>
              }
            />
          </div>
        ) : (
          <div
            style={{ width: `${width}px`, height: `${estimatedHeight}px` }}
            className={`flex items-center justify-center border ${placeholderBg}`}
          >
            <span className="text-xs font-bold opacity-75">
              {lang === 'vi' ? `Trang ${pageNumber}` : `Page ${pageNumber}`}
            </span>
          </div>
        )}
        <div
          className={`absolute bottom-2 right-2.5 px-2 py-0.5 rounded-full text-[10px] font-bold pointer-events-none select-none ${
            theme === 'dark'
              ? 'bg-slate-950/80 text-slate-300'
              : 'bg-slate-900/65 text-white'
          }`}
        >
          {pageNumber}
        </div>
      </div>
    );
  }
);

export const LibraryEbookViewer: React.FC<LibraryEbookViewerProps> = ({
  pdfUrl,
  title,
  articleId,
  lang = 'vi',
  externalTheaterTrigger = 0,
  onEbookProgress,
}) => {
  const storageKey = `tony_ebook_page_${articleId}`;

  const [numPages, setNumPages] = useState<number | null>(null);
  const [currentPage, setCurrentPage] = useState<number>(() => {
    try {
      const saved = parseInt(localStorage.getItem(storageKey) || '1', 10);
      return saved > 0 ? saved : 1;
    } catch {
      return 1;
    }
  });
  const [pageInput, setPageInput] = useState<string>(String(currentPage));
  const [isTwoPageMode, setIsTwoPageMode] = useState<boolean>(false);
  const [viewMode, setViewMode] = useState<EbookViewMode>(getInitialViewMode);
  const [theme, setTheme] = useState<EbookTheme>(getInitialTheme);
  const [zoomScale, setZoomScale] = useState<number>(1);
  const [isTheater, setIsTheater] = useState<boolean>(false);
  const [showJumpBar, setShowJumpBar] = useState<boolean>(false);
  const [loadError, setLoadError] = useState<boolean>(false);
  const [retryCount, setRetryCount] = useState<number>(0);
  const [isLoadingPage, setIsLoadingPage] = useState<boolean>(true);
  const [containerWidth, setContainerWidth] = useState<number>(760);
  const [pageAspectRatio, setPageAspectRatio] = useState<number>(1.38);

  const canvasAreaRef = useRef<HTMLDivElement | null>(null);
  const lastWidthRef = useRef<number>(760);
  const pagesTurnedRef = useRef<number>(0);
  const maxPageRef = useRef<number>(currentPage);
  const progressTimerRef = useRef<number | null>(null);
  const touchStartRef = useRef<{ x: number; y: number; t: number } | null>(null);
  const isProgrammaticScrollRef = useRef<boolean>(false);
  const onEbookProgressRef = useRef(onEbookProgress);
  onEbookProgressRef.current = onEbookProgress;

  // Reset / restore saved page when switching ebook articles
  useEffect(() => {
    let savedPage = 1;
    try {
      const raw = parseInt(localStorage.getItem(`tony_ebook_page_${articleId}`) || '1', 10);
      if (raw > 0) savedPage = raw;
    } catch {}
    setCurrentPage(savedPage);
    setPageInput(String(savedPage));
    setNumPages(null);
    setIsLoadingPage(true);
    setLoadError(false);
    setZoomScale(1);
    pagesTurnedRef.current = 0;
    maxPageRef.current = savedPage;
  }, [articleId, pdfUrl]);

  // Open theater fullscreen when triggered from top quick-action button
  useEffect(() => {
    if (externalTheaterTrigger > 0) {
      setIsTheater(true);
    }
  }, [externalTheaterTrigger]);

  // Persist theme & view mode
  useEffect(() => {
    try {
      localStorage.setItem(THEME_STORAGE_KEY, theme);
    } catch {}
  }, [theme]);

  useEffect(() => {
    try {
      localStorage.setItem(MODE_STORAGE_KEY, viewMode);
    } catch {}
  }, [viewMode]);

  // Persist current page to localStorage
  useEffect(() => {
    setPageInput(String(currentPage));
    try {
      localStorage.setItem(storageKey, String(currentPage));
    } catch {}
  }, [currentPage, storageKey]);

  // Lock body scroll in theater mode
  useEffect(() => {
    if (isTheater) {
      const prevOverflow = document.body.style.overflow;
      document.body.style.overflow = 'hidden';
      return () => {
        document.body.style.overflow = prevOverflow;
      };
    }
  }, [isTheater]);

  // Responsive width observer (debounced + >=4px threshold to prevent mobile PDF canvas crash/re-render loop)
  useEffect(() => {
    const el = canvasAreaRef.current;
    if (!el) return;
    let resizeTimer: number | null = null;
    const applyWidth = () => {
      const nextWidth = el.clientWidth;
      if (nextWidth > 0 && Math.abs(nextWidth - lastWidthRef.current) >= 4) {
        lastWidthRef.current = nextWidth;
        setContainerWidth(nextWidth);
      }
    };
    const scheduleUpdateWidth = () => {
      if (resizeTimer !== null) window.clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(applyWidth, 160);
    };
    if (el.clientWidth > 0) {
      lastWidthRef.current = el.clientWidth;
      setContainerWidth(el.clientWidth);
    }
    let ro: ResizeObserver | null = null;
    if (typeof ResizeObserver !== 'undefined') {
      ro = new ResizeObserver(() => scheduleUpdateWidth());
      ro.observe(el);
    } else {
      window.addEventListener('resize', scheduleUpdateWidth);
    }
    return () => {
      if (resizeTimer !== null) window.clearTimeout(resizeTimer);
      if (ro) ro.disconnect();
      else window.removeEventListener('resize', scheduleUpdateWidth);
    };
  }, [isTheater, viewMode, loadError]);

  const step = viewMode === 'page' && isTwoPageMode && containerWidth >= 960 ? 2 : 1;

  const scheduleProgressReport = useCallback(
    (page: number) => {
      if (page > maxPageRef.current) maxPageRef.current = page;
      if (pagesTurnedRef.current >= 2 && onEbookProgressRef.current) {
        if (progressTimerRef.current) window.clearTimeout(progressTimerRef.current);
        progressTimerRef.current = window.setTimeout(() => {
          onEbookProgressRef.current?.({
            currentPage: page,
            maxPage: maxPageRef.current,
            totalPages: numPages,
            pagesTurned: pagesTurnedRef.current,
          });
        }, 4000);
      }
    },
    [numPages]
  );

  const scrollToSlot = useCallback((targetPage: number, smooth = true) => {
    const container = canvasAreaRef.current;
    if (!container) return;
    const slot = container.querySelector<HTMLElement>(`[data-pdf-page="${targetPage}"]`);
    if (slot) {
      isProgrammaticScrollRef.current = true;
      slot.scrollIntoView({ behavior: smooth ? 'smooth' : 'auto', block: 'start' });
      window.setTimeout(() => {
        isProgrammaticScrollRef.current = false;
      }, 600);
    }
  }, []);

  const goToPage = useCallback(
    (target: number) => {
      const maxP = numPages || 9999;
      const clamped = Math.max(1, Math.min(target, maxP));
      if (clamped !== currentPage) {
        if (viewMode === 'page') {
          setIsLoadingPage(true);
        }
        setCurrentPage(clamped);
        pagesTurnedRef.current += 1;
        scheduleProgressReport(clamped);

        if (viewMode === 'scroll') {
          scrollToSlot(clamped, true);
        } else if (isTheater) {
          canvasAreaRef.current?.scrollTo({ top: 0, behavior: 'smooth' });
        } else {
          // Scroll gently to the top of the reader card when turning pages inline on mobile/desktop
          const viewerEl = document.getElementById('library-ebook-viewer');
          if (viewerEl) {
            const rect = viewerEl.getBoundingClientRect();
            if (rect.top < 0) {
              viewerEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
          }
        }
      } else if (viewMode === 'scroll') {
        scrollToSlot(clamped, true);
      }
    },
    [currentPage, isTheater, numPages, scheduleProgressReport, scrollToSlot, viewMode]
  );

  // When switching into scroll mode, jump immediately to current saved page
  useEffect(() => {
    if (viewMode === 'scroll' && numPages && currentPage > 1) {
      const t = window.setTimeout(() => scrollToSlot(currentPage, false), 120);
      return () => window.clearTimeout(t);
    }
  }, [viewMode, numPages, scrollToSlot]);

  useEffect(() => {
    return () => {
      if (progressTimerRef.current) window.clearTimeout(progressTimerRef.current);
    };
  }, []);

  const handlePrev = useCallback(() => {
    if (currentPage > 1) goToPage(currentPage - step);
  }, [currentPage, goToPage, step]);

  const handleNext = useCallback(() => {
    if (!numPages || currentPage < numPages) goToPage(currentPage + step);
  }, [currentPage, goToPage, numPages, step]);

  // Keyboard shortcuts (Escape / Left / Right in theater mode or focused viewer)
  useEffect(() => {
    if (!isTheater) return;
    const onKeyDown = (e: KeyboardEvent) => {
      const tag = (e.target as HTMLElement)?.tagName;
      if (tag === 'INPUT' || tag === 'TEXTAREA') return;
      if (e.key === 'Escape') {
        if (document.getElementById('addVdictOnYourWeb')) return;
        setIsTheater(false);
      } else if (e.key === 'ArrowRight' && viewMode === 'page') {
        handleNext();
      } else if (e.key === 'ArrowLeft' && viewMode === 'page') {
        handlePrev();
      }
    };
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [isTheater, viewMode, handleNext, handlePrev]);

  const handlePageInputKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      const parsed = parseInt(pageInput, 10);
      if (!isNaN(parsed)) {
        goToPage(parsed);
      } else {
        setPageInput(String(currentPage));
      }
      (e.target as HTMLInputElement).blur();
    }
  };

  // Natural swipe left/right to flip pages on touch devices when not zoomed in
  const handleTouchStart = (e: React.TouchEvent<HTMLDivElement>) => {
    if (viewMode !== 'page' || zoomScale > 1.05 || e.touches.length !== 1) {
      touchStartRef.current = null;
      return;
    }
    const t = e.touches[0];
    touchStartRef.current = { x: t.clientX, y: t.clientY, t: Date.now() };
  };

  const handleTouchEnd = (e: React.TouchEvent<HTMLDivElement>) => {
    if (!touchStartRef.current || viewMode !== 'page' || zoomScale > 1.05) return;
    const start = touchStartRef.current;
    touchStartRef.current = null;
    if (e.changedTouches.length !== 1) return;
    // Do not hijack swipe if user has highlighted text to look up a word
    const sel = typeof window !== 'undefined' ? window.getSelection()?.toString() : '';
    if (sel && sel.trim().length > 0) return;

    const end = e.changedTouches[0];
    const dx = end.clientX - start.x;
    const dy = end.clientY - start.y;
    const dt = Date.now() - start.t;
    if (dt < 650 && Math.abs(dx) >= 55 && Math.abs(dx) > Math.abs(dy) * 1.45) {
      if (dx < 0) handleNext();
      else handlePrev();
    }
  };

  const handleScrollPageVisible = useCallback(
    (visiblePage: number) => {
      if (isProgrammaticScrollRef.current) return;
      setCurrentPage((prev) => {
        if (prev === visiblePage) return prev;
        pagesTurnedRef.current += 1;
        scheduleProgressReport(visiblePage);
        return visiblePage;
      });
    },
    [scheduleProgressReport]
  );

  const handlePageMeasured = useCallback((ratio: number) => {
    if (ratio > 0.6 && ratio < 2.2) {
      setPageAspectRatio((prev) => (Math.abs(prev - ratio) > 0.03 ? ratio : prev));
    }
  }, []);

  const cycleTheme = () => {
    setTheme((prev) => (prev === 'light' ? 'sepia' : prev === 'sepia' ? 'dark' : 'light'));
  };

  const handleZoomOut = () =>
    setZoomScale((z) => Math.max(0.75, Math.round((z - 0.15) * 100) / 100));
  const handleZoomIn = () =>
    setZoomScale((z) => Math.min(2.2, Math.round((z + 0.15) * 100) / 100));

  // Responsive page sizing: edge-to-edge on mobile for maximum readability
  const isMobileViewport = containerWidth < 640;
  const horizontalPadding = isMobileViewport ? 12 : isTheater ? 64 : 48;
  const availableWidth = Math.max(260, containerWidth - horizontalPadding);
  const canShowTwoPages = viewMode === 'page' && isTwoPageMode && containerWidth >= 960;
  const basePageWidth = canShowTwoPages
    ? Math.min(540, Math.floor((availableWidth - 16) / 2))
    : Math.min(isTheater ? 880 : 780, availableWidth);
  const renderedPageWidth = Math.round(basePageWidth * zoomScale);
  const estimatedPageHeight = Math.round(renderedPageWidth * pageAspectRatio);

  // Clamp canvas DPR to stay crisp on Retina screens while avoiding iOS Safari OOM crashes when zoomed
  const safeDpr = useMemo(() => {
    if (typeof window === 'undefined') return 1.5;
    const nativeDpr = window.devicePixelRatio || 1;
    const cap = zoomScale > 1.35 ? 1.5 : 2;
    return Math.min(nativeDpr, cap);
  }, [zoomScale]);

  const fileWithRetry = useMemo(() => {
    if (retryCount === 0) return pdfUrl;
    const sep = pdfUrl.includes('?') ? '&' : '?';
    return `${pdfUrl}${sep}r=${retryCount}`;
  }, [pdfUrl, retryCount]);

  // Theme palettes
  const backdropClass =
    theme === 'dark'
      ? 'bg-[#090e1a]'
      : theme === 'sepia'
      ? 'bg-[#e8decb]'
      : 'bg-[#eef2f7]';

  const pageFilterClass =
    theme === 'dark'
      ? 'ebook-theme-dark'
      : theme === 'sepia'
      ? 'ebook-theme-sepia'
      : '';

  const themeIcon = theme === 'light' ? '☀️' : theme === 'sepia' ? '📜' : '🌙';
  const themeLabelVi = theme === 'light' ? 'Sáng' : theme === 'sepia' ? 'Giấy sách' : 'Ban đêm';
  const themeLabelEn = theme === 'light' ? 'Light' : theme === 'sepia' ? 'Sepia' : 'Night';

  const progressPct = numPages && numPages > 0 ? Math.min(100, Math.round((currentPage / numPages) * 100)) : 0;

  const pageNumbers = useMemo(() => {
    if (!numPages) return [];
    return Array.from({ length: numPages }, (_, i) => i + 1);
  }, [numPages]);

  return (
    <div
      id="library-ebook-viewer"
      className={
        isTheater
          ? `fixed inset-0 z-50 h-[100dvh] w-screen ${backdropClass} flex flex-col overflow-hidden`
          : `rounded-2xl sm:rounded-3xl border border-slate-200/90 ${backdropClass} overflow-hidden shadow-md scroll-mt-20 flex flex-col`
      }
    >
      {/* Reader Styles (book spread shadow + comfort reading filters + crisp text layer selection) */}
      <style>{`
        .ebook-page-left { box-shadow: inset -18px 0 28px -15px rgba(0,0,0,0.18), -4px 6px 24px rgba(15,23,42,0.18); }
        .ebook-page-right { box-shadow: inset 18px 0 28px -15px rgba(0,0,0,0.18), 4px 6px 24px rgba(15,23,42,0.18); }
        .ebook-page-single { box-shadow: 0 8px 28px rgba(15,23,42,0.14), 0 2px 6px rgba(15,23,42,0.08); }
        .ebook-theme-sepia .react-pdf__Page__canvas { filter: sepia(0.24) brightness(0.97) contrast(0.98); }
        .ebook-theme-dark .react-pdf__Page__canvas { filter: invert(0.89) hue-rotate(180deg) brightness(0.95) contrast(0.97); }
        .react-pdf__Page__textContent span::selection { background: rgba(42, 180, 232, 0.35); }
      `}</style>

      {/* Top Reader Toolbar — Single compact row on mobile, full controls on desktop */}
      <div className="bg-gradient-to-r from-[#0a5482] via-[#0d3b61] to-[#0f172a] px-3 sm:px-5 h-12 sm:h-14 text-white border-b border-white/10 flex items-center justify-between gap-2 shrink-0">
        {/* Left: Book Title & Tip */}
        <div className="flex items-center gap-2 min-w-0 flex-1">
          <span className="w-7 h-7 sm:w-8 sm:h-8 rounded-lg bg-white/15 border border-white/20 flex items-center justify-center text-sm sm:text-base shrink-0">
            📖
          </span>
          <div className="min-w-0">
            <div className="text-[13px] sm:text-[15px] font-extrabold tracking-tight truncate">
              {title}
            </div>
            <div className="text-[11px] text-sky-200/85 hidden md:block truncate">
              {lang === 'vi'
                ? 'Click đúp từ tiếng Anh trên trang để tra từ điển • Tự động lưu trang đang đọc'
                : 'Double-click any English word to look it up • Progress auto-saved'}
            </div>
          </div>
        </div>

        {/* Center: Desktop Spread & Comfort Theme Pills */}
        <div className="hidden lg:flex items-center gap-2 shrink-0">
          {viewMode === 'page' && (
            <button
              type="button"
              onClick={() => setIsTwoPageMode((v) => !v)}
              className={`inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-xs font-bold border transition cursor-pointer ${
                isTwoPageMode
                  ? 'bg-[#2ab4e8] text-white border-sky-300'
                  : 'bg-white/10 hover:bg-white/20 text-sky-100 border-white/15'
              }`}
              title={
                lang === 'vi'
                  ? 'Đọc 1 trang hoặc mở đôi 2 trang như sách giấy'
                  : 'Toggle single-page or 2-page spread'
              }
            >
              {isTwoPageMode
                ? lang === 'vi'
                  ? '📖 2 Trang'
                  : '📖 2 Pages'
                : lang === 'vi'
                ? '📄 1 Trang'
                : '📄 1 Page'}
            </button>
          )}

          {/* Reading Comfort Theme Segmented Control */}
          <div
            className="inline-flex items-center bg-slate-950/50 border border-white/15 rounded-lg p-0.5"
            role="group"
            aria-label={lang === 'vi' ? 'Chế độ màu trang sách' : 'Reading theme'}
          >
            {(
              [
                { id: 'light', icon: '☀️', vi: 'Sáng', en: 'Light' },
                { id: 'sepia', icon: '📜', vi: 'Giấy', en: 'Sepia' },
                { id: 'dark', icon: '🌙', vi: 'Tối', en: 'Night' },
              ] as const
            ).map((opt) => (
              <button
                key={opt.id}
                type="button"
                onClick={() => setTheme(opt.id)}
                className={`px-2 py-1 rounded-md text-[11px] font-bold transition cursor-pointer inline-flex items-center gap-1 ${
                  theme === opt.id
                    ? 'bg-white text-slate-900 shadow-xs'
                    : 'text-sky-100/85 hover:text-white'
                }`}
              >
                <span>{opt.icon}</span>
                <span>{lang === 'vi' ? opt.vi : opt.en}</span>
              </button>
            ))}
          </div>
        </div>

        {/* Right: Compact Action Controls */}
        <div className="flex items-center gap-1.5 shrink-0">
          {/* Mobile / Tablet Theme Cycle Button */}
          <button
            type="button"
            onClick={cycleTheme}
            className="lg:hidden inline-flex items-center gap-1 px-2 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 border border-white/15 text-[11px] font-bold text-sky-100 transition cursor-pointer"
            title={
              lang === 'vi'
                ? `Màu trang: ${themeLabelVi} (bấm để đổi Sáng / Giấy / Tối)`
                : `Theme: ${themeLabelEn} (tap to switch)`
            }
          >
            <span>{themeIcon}</span>
            <span className="hidden xs:inline">{lang === 'vi' ? themeLabelVi : themeLabelEn}</span>
          </button>

          {/* Page vs Continuous Scroll Mode Toggle */}
          <button
            type="button"
            onClick={() => setViewMode((m) => (m === 'page' ? 'scroll' : 'page'))}
            className="inline-flex items-center gap-1 px-2 sm:px-2.5 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 border border-white/15 text-[11px] sm:text-xs font-bold text-sky-100 transition cursor-pointer"
            title={
              lang === 'vi'
                ? 'Chuyển giữa chế độ Lật từng trang và Cuộn liên tục'
                : 'Switch between Single Page and Continuous Scroll'
            }
          >
            <span>{viewMode === 'page' ? '📜' : '📖'}</span>
            <span>
              {viewMode === 'page'
                ? lang === 'vi'
                  ? 'Cuộn'
                  : 'Scroll'
                : lang === 'vi'
                ? 'Lật trang'
                : 'Page'}
            </span>
          </button>

          {/* Download PDF (visible on sm+ or fullscreen) */}
          <a
            href={pdfUrl}
            target="_blank"
            rel="noopener noreferrer"
            download
            className={`${
              isTheater ? 'inline-flex' : 'hidden sm:inline-flex'
            } items-center gap-1 px-2.5 py-1.5 rounded-lg bg-emerald-500/90 hover:bg-emerald-500 text-white text-[11px] sm:text-xs font-extrabold transition`}
            title={lang === 'vi' ? 'Tải file PDF về máy' : 'Download PDF'}
          >
            <span>⬇</span>
            <span className="hidden sm:inline">{lang === 'vi' ? 'Tải PDF' : 'PDF'}</span>
          </a>

          {/* Fullscreen / Exit Fullscreen */}
          <button
            type="button"
            onClick={() => setIsTheater((v) => !v)}
            className={`px-2.5 sm:px-3 py-1.5 rounded-lg text-[11px] sm:text-xs font-extrabold transition cursor-pointer inline-flex items-center gap-1 ${
              isTheater
                ? 'bg-rose-500 hover:bg-rose-600 text-white shadow-xs'
                : 'bg-[#2ab4e8] hover:bg-sky-400 text-white shadow-xs'
            }`}
            aria-label={isTheater ? 'Exit fullscreen' : 'Fullscreen'}
          >
            <span>{isTheater ? '✕' : '⛶'}</span>
            <span className="hidden sm:inline">
              {isTheater
                ? lang === 'vi'
                  ? 'Đóng'
                  : 'Close'
                : lang === 'vi'
                ? 'Toàn màn hình'
                : 'Fullscreen'}
            </span>
          </button>
        </div>
      </div>

      {/* Thin Continuous Progress Indicator */}
      {numPages && numPages > 1 && (
        <div className="h-[3px] w-full bg-slate-900/20 shrink-0">
          <div
            className="h-full bg-gradient-to-r from-[#0a5482] to-[#2ab4e8] transition-all duration-300"
            style={{ width: `${progressPct}%` }}
          />
        </div>
      )}

      {/* Main Reading Viewport */}
      {loadError ? (
        <div className="p-8 sm:p-12 text-center flex flex-col items-center justify-center min-h-[360px] gap-4">
          <div className="w-14 h-14 rounded-2xl bg-sky-100 text-[#0a5482] flex items-center justify-center text-2xl">
            📄
          </div>
          <div className="max-w-md space-y-1.5">
            <h4 className={`text-base font-extrabold ${theme === 'dark' ? 'text-white' : 'text-slate-800'}`}>
              {lang === 'vi'
                ? 'Không thể tải trang sách vào khung đọc ngay lúc này'
                : 'Unable to load the PDF inside the reader right now'}
            </h4>
            <p className={`text-sm ${theme === 'dark' ? 'text-slate-400' : 'text-slate-500'}`}>
              {lang === 'vi'
                ? 'Bạn có thể bấm thử tải lại hoặc mở trực tiếp file PDF chuẩn sắc nét trên trình duyệt.'
                : 'Please retry loading or open the full PDF directly in a new tab.'}
            </p>
          </div>
          <div className="flex flex-wrap items-center justify-center gap-2.5">
            <button
              type="button"
              onClick={() => {
                setLoadError(false);
                setIsLoadingPage(true);
                setRetryCount((c) => c + 1);
              }}
              className="px-4 py-2 rounded-xl bg-[#0a5482] hover:bg-[#084266] text-white text-sm font-extrabold transition cursor-pointer"
            >
              🔄 {lang === 'vi' ? 'Thử tải lại' : 'Retry'}
            </button>
            <a
              href={pdfUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="px-4 py-2 rounded-xl bg-white hover:bg-slate-50 text-slate-800 border border-slate-300 text-sm font-extrabold transition"
            >
              📄 {lang === 'vi' ? 'Mở PDF trong tab mới' : 'Open PDF in New Tab'}
            </a>
          </div>
        </div>
      ) : (
        <div
          ref={canvasAreaRef}
          onTouchStart={handleTouchStart}
          onTouchEnd={handleTouchEnd}
          className={`relative flex flex-col items-center ${
            isTheater
              ? 'flex-1 overflow-auto py-3 sm:py-5 px-1.5 sm:px-6'
              : viewMode === 'scroll'
              ? 'h-[76vh] min-h-[480px] overflow-auto py-3 sm:py-5 px-1.5 sm:px-6'
              : zoomScale > 1.01
              ? 'overflow-x-auto overflow-y-visible py-3 sm:py-5 px-1.5 sm:px-6'
              : 'overflow-x-hidden py-3 sm:py-5 px-1.5 sm:px-6'
          } ${backdropClass} custom-scrollbar`}
          style={{ WebkitOverflowScrolling: 'touch' }}
        >
          {/* Floating unobtrusive loading badge (never collapses page height) */}
          {isLoadingPage && viewMode === 'page' && (
            <div className="absolute top-3 left-1/2 -translate-x-1/2 z-20 pointer-events-none px-3.5 py-1.5 rounded-full bg-slate-900/85 border border-sky-400/30 text-sky-100 text-xs font-bold flex items-center gap-2 shadow-lg backdrop-blur-xs">
              <span className="w-3 h-3 border-2 border-sky-300/30 border-t-sky-300 rounded-full animate-spin" />
              <span>{lang === 'vi' ? 'Đang tải trang sách...' : 'Loading page...'}</span>
            </div>
          )}

          {/* Desktop subtle side page-turn buttons in Page Mode */}
          {viewMode === 'page' && numPages && numPages > 1 && (
            <>
              <button
                type="button"
                onClick={handlePrev}
                disabled={currentPage <= 1}
                aria-label={lang === 'vi' ? 'Trang trước' : 'Previous page'}
                className="hidden sm:flex z-10 w-10 h-10 rounded-full bg-slate-900/70 hover:bg-[#0a5482] disabled:opacity-0 text-white items-center justify-center shadow-lg transition cursor-pointer backdrop-blur-xs"
                style={{ position: isTheater ? 'fixed' : 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)' }}
              >
                ←
              </button>
              <button
                type="button"
                onClick={handleNext}
                disabled={currentPage >= numPages}
                aria-label={lang === 'vi' ? 'Trang tiếp theo' : 'Next page'}
                className="hidden sm:flex z-10 w-10 h-10 rounded-full bg-slate-900/70 hover:bg-[#0a5482] disabled:opacity-0 text-white items-center justify-center shadow-lg transition cursor-pointer backdrop-blur-xs"
                style={{ position: isTheater ? 'fixed' : 'absolute', right: '12px', top: '50%', transform: 'translateY(-50%)' }}
              >
                →
              </button>
            </>
          )}

          <Document
            file={fileWithRetry}
            onLoadSuccess={({ numPages: loadedPages }) => {
              setNumPages(loadedPages);
              setLoadError(false);
              if (currentPage > loadedPages) {
                setCurrentPage(1);
              }
              setIsLoadingPage(false);
            }}
            onLoadError={() => {
              setIsLoadingPage(false);
              setLoadError(true);
            }}
            loading={
              <div
                style={{ width: `${renderedPageWidth}px`, height: `${estimatedPageHeight}px` }}
                className={`rounded-md flex flex-col items-center justify-center gap-3 border ${
                  theme === 'dark'
                    ? 'bg-slate-900 border-slate-800 text-sky-200'
                    : theme === 'sepia'
                    ? 'bg-[#f6efe2] border-[#dfd2bc] text-[#6d593e]'
                    : 'bg-white border-slate-200 text-[#0a5482]'
                }`}
              >
                <span className="w-7 h-7 border-[3px] border-current/25 border-t-current rounded-full animate-spin" />
                <span className="text-sm font-bold">
                  {lang === 'vi' ? 'Đang mở sách E-book...' : 'Opening E-book...'}
                </span>
              </div>
            }
          >
            {viewMode === 'scroll' ? (
              <div className="flex flex-col items-center gap-3.5 sm:gap-5 pb-4">
                {pageNumbers.map((pageNum) => (
                  <ScrollPageSlot
                    key={pageNum}
                    pageNumber={pageNum}
                    shouldRender={Math.abs(pageNum - currentPage) <= 2}
                    width={renderedPageWidth}
                    estimatedHeight={estimatedPageHeight}
                    devicePixelRatio={safeDpr}
                    pageFilterClass={pageFilterClass}
                    theme={theme}
                    lang={lang}
                    onVisible={handleScrollPageVisible}
                    onPageMeasured={handlePageMeasured}
                  />
                ))}
              </div>
            ) : (
              <div
                className={`flex justify-center items-start ${pageFilterClass} ${
                  canShowTwoPages ? 'gap-0' : ''
                }`}
                style={{ minHeight: `${estimatedPageHeight}px` }}
              >
                <Page
                  pageNumber={currentPage}
                  width={renderedPageWidth}
                  devicePixelRatio={safeDpr}
                  renderTextLayer={true}
                  renderAnnotationLayer={true}
                  onLoadSuccess={(page) => {
                    if (page.originalWidth > 0 && page.originalHeight > 0) {
                      handlePageMeasured(page.originalHeight / page.originalWidth);
                    }
                  }}
                  onRenderSuccess={() => setIsLoadingPage(false)}
                  onRenderError={() => {
                    setIsLoadingPage(false);
                  }}
                  className={`bg-white rounded-sm overflow-hidden ${
                    canShowTwoPages ? 'ebook-page-left' : 'ebook-page-single'
                  }`}
                  loading={
                    <div
                      style={{ width: `${renderedPageWidth}px`, height: `${estimatedPageHeight}px` }}
                      className="bg-white rounded-sm flex items-center justify-center text-slate-400 text-xs font-bold"
                    >
                      {lang === 'vi' ? `Đang tải trang ${currentPage}...` : `Loading page ${currentPage}...`}
                    </div>
                  }
                />

                {canShowTwoPages && numPages !== null && currentPage + 1 <= numPages && (
                  <Page
                    pageNumber={currentPage + 1}
                    width={renderedPageWidth}
                    devicePixelRatio={safeDpr}
                    renderTextLayer={true}
                    renderAnnotationLayer={true}
                    onRenderSuccess={() => setIsLoadingPage(false)}
                    onRenderError={() => setIsLoadingPage(false)}
                    className="bg-white rounded-sm overflow-hidden ebook-page-right"
                    loading={
                      <div
                        style={{ width: `${renderedPageWidth}px`, height: `${estimatedPageHeight}px` }}
                        className="bg-white rounded-sm flex items-center justify-center text-slate-400 text-xs font-bold"
                      >
                        {lang === 'vi'
                          ? `Đang tải trang ${currentPage + 1}...`
                          : `Loading page ${currentPage + 1}...`}
                      </div>
                    }
                  />
                )}
              </div>
            )}
          </Document>

          {/* Subtle mobile gesture hint below page */}
          {viewMode === 'page' && numPages && numPages > 1 && (
            <div
              className={`mt-2.5 text-[11px] font-medium text-center px-3 sm:hidden ${
                theme === 'dark'
                  ? 'text-slate-400'
                  : theme === 'sepia'
                  ? 'text-[#7c6a4e]'
                  : 'text-slate-500'
              }`}
            >
              {lang === 'vi'
                ? '💡 Vuốt trái/phải để lật trang • Bấm + để phóng to chữ'
                : '💡 Swipe left/right to turn pages • Tap + to zoom'}
            </div>
          )}
        </div>
      )}

      {/* Expandable Jump-to-Page Scrubber Bar (always shown on sm+ if >1 page, or toggled on mobile) */}
      {!loadError && numPages && numPages > 1 && (
        <div
          className={`${
            showJumpBar ? 'flex' : 'hidden sm:flex'
          } items-center gap-2.5 sm:gap-3 px-3.5 sm:px-5 py-2 border-t text-xs shrink-0 ${
            theme === 'dark'
              ? 'bg-slate-900 border-slate-800 text-slate-300'
              : theme === 'sepia'
              ? 'bg-[#e3d7c0] border-[#d3c4a8] text-[#5c4b34]'
              : 'bg-slate-100 border-slate-200 text-slate-600'
          }`}
        >
          <span className="font-extrabold text-[#0a5482] dark:text-sky-300 tabular-nums shrink-0" style={{ color: theme === 'dark' ? '#38bdf8' : '#0a5482' }}>
            {progressPct}%
          </span>
          <input
            type="range"
            min={1}
            max={numPages}
            value={currentPage}
            onChange={(e) => goToPage(parseInt(e.target.value, 10))}
            aria-label={lang === 'vi' ? 'Thanh trượt chuyển trang nhanh' : 'Quick page slider'}
            className="flex-1 h-1.5 accent-[#0a5482] cursor-pointer"
          />
          <div className="flex items-center gap-1 shrink-0">
            <span className="text-[11px] opacity-80">{lang === 'vi' ? 'Tới:' : 'Go:'}</span>
            <input
              type="text"
              inputMode="numeric"
              value={pageInput}
              onChange={(e) => setPageInput(e.target.value)}
              onKeyDown={handlePageInputKeyDown}
              onBlur={() => {
                const parsed = parseInt(pageInput, 10);
                if (!isNaN(parsed)) goToPage(parsed);
                else setPageInput(String(currentPage));
              }}
              aria-label={lang === 'vi' ? 'Nhập số trang' : 'Enter page number'}
              className={`w-12 text-center font-extrabold py-0.5 rounded-md border text-xs focus:outline-none focus:border-[#2ab4e8] ${
                theme === 'dark'
                  ? 'bg-slate-800 border-slate-700 text-white'
                  : 'bg-white border-slate-300 text-slate-800'
              }`}
            />
          </div>
          {currentPage > 1 && (
            <button
              type="button"
              onClick={() => goToPage(1)}
              className="text-[11px] font-bold underline opacity-80 hover:opacity-100 cursor-pointer shrink-0"
            >
              {lang === 'vi' ? 'Trang 1' : 'Cover'}
            </button>
          )}
        </div>
      )}

      {/* Thumb-Friendly Bottom Control Dock (Safe-Area Aware for iOS Safari) */}
      {!loadError && (
        <div
          className={`px-2.5 sm:px-5 pt-2 border-t flex items-center justify-between gap-1.5 sm:gap-3 shrink-0 ${
            isTheater ? 'pb-[max(0.65rem,env(safe-area-inset-bottom))]' : 'pb-2.5'
          } ${
            theme === 'dark'
              ? 'bg-slate-950 border-slate-800 text-slate-200'
              : theme === 'sepia'
              ? 'bg-[#dfd2ba] border-[#cbb998] text-[#473926]'
              : 'bg-white border-slate-200 text-slate-800'
          }`}
        >
          {/* Prev Page */}
          <button
            type="button"
            onClick={handlePrev}
            disabled={currentPage <= 1}
            className={`h-9 sm:h-10 px-3 sm:px-4 rounded-xl font-extrabold text-xs sm:text-sm inline-flex items-center gap-1 transition cursor-pointer disabled:opacity-35 disabled:cursor-default ${
              theme === 'dark'
                ? 'bg-slate-800 hover:bg-slate-700 text-white border border-slate-700'
                : 'bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200'
            }`}
          >
            <span>←</span>
            <span className="hidden xs:inline">{lang === 'vi' ? 'Trước' : 'Prev'}</span>
          </button>

          {/* Center: Page Counter Pill (tap to toggle mobile scrubber) + Zoom Controls */}
          <div className="flex items-center gap-1.5 sm:gap-2.5 min-w-0">
            <button
              type="button"
              onClick={() => setShowJumpBar((v) => !v)}
              className={`h-9 sm:h-10 px-2.5 sm:px-3.5 rounded-xl font-extrabold text-xs sm:text-sm tabular-nums inline-flex items-center gap-1 border transition cursor-pointer ${
                theme === 'dark'
                  ? 'bg-slate-900 border-slate-700 text-sky-300 hover:border-sky-500/50'
                  : 'bg-sky-50/80 border-sky-200 text-[#0a5482] hover:bg-sky-100'
              }`}
              title={lang === 'vi' ? 'Bấm để mở thanh chọn trang nhanh' : 'Tap to jump to page'}
            >
              <span>
                {currentPage} / {numPages || '…'}
              </span>
              <span className="text-[10px] opacity-70 sm:hidden">{showJumpBar ? '▲' : '▼'}</span>
            </button>

            {/* Zoom Controls — Now accessible on BOTH Mobile and Desktop */}
            <div
              className={`inline-flex items-center rounded-xl border h-9 sm:h-10 p-0.5 ${
                theme === 'dark'
                  ? 'bg-slate-900 border-slate-700'
                  : 'bg-slate-50 border-slate-200'
              }`}
            >
              <button
                type="button"
                onClick={handleZoomOut}
                disabled={zoomScale <= 0.75}
                className="w-7 sm:w-8 h-full rounded-lg hover:bg-black/10 disabled:opacity-30 font-black text-sm flex items-center justify-center cursor-pointer"
                aria-label={lang === 'vi' ? 'Thu nhỏ' : 'Zoom out'}
              >
                −
              </button>
              <button
                type="button"
                onClick={() => setZoomScale(1)}
                className="px-1 sm:px-1.5 text-[11px] font-mono font-extrabold tabular-nums cursor-pointer"
                title={lang === 'vi' ? 'Đặt lại 100%' : 'Reset zoom to 100%'}
              >
                {Math.round(zoomScale * 100)}%
              </button>
              <button
                type="button"
                onClick={handleZoomIn}
                disabled={zoomScale >= 2.2}
                className="w-7 sm:w-8 h-full rounded-lg hover:bg-black/10 disabled:opacity-30 font-black text-sm flex items-center justify-center cursor-pointer"
                aria-label={lang === 'vi' ? 'Phóng to' : 'Zoom in'}
              >
                +
              </button>
            </div>
          </div>

          {/* Next Page */}
          <button
            type="button"
            onClick={handleNext}
            disabled={numPages !== null && currentPage >= numPages}
            className="h-9 sm:h-10 px-3 sm:px-4 rounded-xl bg-[#0a5482] hover:bg-[#084266] disabled:opacity-35 text-white font-extrabold text-xs sm:text-sm inline-flex items-center gap-1 shadow-xs transition cursor-pointer disabled:cursor-default"
          >
            <span className="hidden xs:inline">{lang === 'vi' ? 'Sau' : 'Next'}</span>
            <span>→</span>
          </button>
        </div>
      )}
    </div>
  );
};

export default LibraryEbookViewer;
