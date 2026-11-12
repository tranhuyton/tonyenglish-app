import React, { useEffect, useRef, useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';
import 'react-pdf/dist/Page/AnnotationLayer.css';
import 'react-pdf/dist/Page/TextLayer.css';

pdfjs.GlobalWorkerOptions.workerSrc = `//unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;

export interface LibraryEbookViewerProps {
  pdfUrl: string;
  title: string;
  articleId: number | string;
  lang?: string;
  externalTheaterTrigger?: number;
}

export const LibraryEbookViewer: React.FC<LibraryEbookViewerProps> = ({
  pdfUrl,
  title,
  articleId,
  lang = 'vi',
  externalTheaterTrigger = 0,
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
  const [zoomScale, setZoomScale] = useState<number>(1);
  const [isTheater, setIsTheater] = useState<boolean>(false);
  const [useNativeFallback, setUseNativeFallback] = useState<boolean>(false);
  const [isLoadingPage, setIsLoadingPage] = useState<boolean>(true);
  const [containerWidth, setContainerWidth] = useState<number>(760);

  const canvasAreaRef = useRef<HTMLDivElement | null>(null);

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
    setUseNativeFallback(false);
  }, [articleId, pdfUrl]);

  // Open theater fullscreen when triggered from top quick-action button
  useEffect(() => {
    if (externalTheaterTrigger > 0) {
      setIsTheater(true);
    }
  }, [externalTheaterTrigger]);

  // Persist current page to localStorage
  useEffect(() => {
    setPageInput(String(currentPage));
    try {
      localStorage.setItem(storageKey, String(currentPage));
    } catch {}
  }, [currentPage, storageKey]);

  // Lock body scroll in theater mode & support Escape / Left / Right keys
  useEffect(() => {
    if (isTheater) {
      const prevOverflow = document.body.style.overflow;
      document.body.style.overflow = 'hidden';
      return () => {
        document.body.style.overflow = prevOverflow;
      };
    }
  }, [isTheater]);

  // Responsive width observer so PDF pages fit crisply on mobile, tablet & desktop
  useEffect(() => {
    const el = canvasAreaRef.current;
    if (!el) return;
    const updateWidth = () => {
      if (el.clientWidth > 0) {
        setContainerWidth(el.clientWidth);
      }
    };
    updateWidth();
    let ro: ResizeObserver | null = null;
    if (typeof ResizeObserver !== 'undefined') {
      ro = new ResizeObserver(() => updateWidth());
      ro.observe(el);
    } else {
      window.addEventListener('resize', updateWidth);
    }
    return () => {
      if (ro) ro.disconnect();
      else window.removeEventListener('resize', updateWidth);
    };
  }, [isTheater, useNativeFallback]);

  const step = isTwoPageMode ? 2 : 1;

  const goToPage = (target: number) => {
    const maxP = numPages || 9999;
    const clamped = Math.max(1, Math.min(target, maxP));
    if (clamped !== currentPage) {
      setIsLoadingPage(true);
      setCurrentPage(clamped);
      canvasAreaRef.current?.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const handlePrev = () => {
    if (currentPage > 1) goToPage(currentPage - step);
  };

  const handleNext = () => {
    if (!numPages || currentPage < numPages) goToPage(currentPage + step);
  };

  useEffect(() => {
    if (!isTheater) return;
    const onKeyDown = (e: KeyboardEvent) => {
      const tag = (e.target as HTMLElement)?.tagName;
      if (tag === 'INPUT' || tag === 'TEXTAREA') return;
      if (e.key === 'Escape') {
        setIsTheater(false);
      } else if (e.key === 'ArrowRight') {
        handleNext();
      } else if (e.key === 'ArrowLeft') {
        handlePrev();
      }
    };
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [isTheater, currentPage, numPages, isTwoPageMode]);

  const handlePageInputKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      const parsed = parseInt(pageInput, 10);
      if (!isNaN(parsed)) {
        goToPage(parsed);
      } else {
        setPageInput(String(currentPage));
      }
    }
  };

  // Compute responsive page width before applying user zoom
  const horizontalPadding = containerWidth < 640 ? 20 : 48;
  const availableWidth = Math.max(260, containerWidth - horizontalPadding);
  const basePageWidth = isTwoPageMode && containerWidth >= 900
    ? Math.min(520, Math.floor((availableWidth - 12) / 2))
    : Math.min(isTheater ? 860 : 760, availableWidth);
  const renderedPageWidth = Math.round(basePageWidth * zoomScale);

  return (
    <div
      id="library-ebook-viewer"
      className={
        isTheater
          ? 'fixed inset-0 z-50 bg-slate-950 flex flex-col'
          : 'rounded-2xl sm:rounded-3xl border-2 border-sky-200/90 bg-slate-900 overflow-hidden shadow-lg scroll-mt-24'
      }
    >
      {/* Top Reader Toolbar */}
      <div className="bg-gradient-to-r from-[#0a5482] via-[#0d3b61] to-[#0f172a] px-3.5 sm:px-6 py-3 sm:py-3.5 text-white border-b border-white/10 flex flex-wrap items-center justify-between gap-2.5">
        {/* Left: Book Title & Dictionary Tip */}
        <div className="flex items-center gap-2.5 min-w-0">
          <span className="w-9 h-9 rounded-xl bg-white/15 border border-white/20 flex items-center justify-center text-lg shrink-0">
            📖
          </span>
          <div className="min-w-0">
            <div className="text-sm sm:text-[15.5px] font-black tracking-tight truncate max-w-[230px] sm:max-w-[360px]">
              {title}
            </div>
            <div className="text-[11px] sm:text-xs text-sky-200/90 hidden sm:block">
              {lang === 'vi'
                ? '💡 Click đúp vào từ tiếng Anh bất kỳ trên trang sách để tra từ điển ngay'
                : '💡 Double-click any English word on the page to look it up'}
            </div>
          </div>
        </div>

        {/* Center: Page Navigation & Spread Toggle */}
        {!useNativeFallback && (
          <div className="flex items-center gap-1.5 sm:gap-2 flex-wrap">
            {/* 1-Page / 2-Page Book Spread */}
            <button
              type="button"
              onClick={() => setIsTwoPageMode(!isTwoPageMode)}
              className={`hidden lg:inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl text-xs font-extrabold border transition cursor-pointer ${
                isTwoPageMode
                  ? 'bg-[#2ab4e8] text-white border-sky-300 shadow-xs'
                  : 'bg-white/10 hover:bg-white/20 text-sky-100 border-white/15'
              }`}
              title="Chuyển chế độ đọc 1 trang hoặc 2 trang mở đôi như sách thật"
            >
              <span>{isTwoPageMode ? '📖 2 Trang' : '📄 1 Trang'}</span>
            </button>

            {/* Prev / Page Input / Next */}
            <div className="inline-flex items-center gap-1 bg-slate-950/55 border border-white/15 rounded-xl p-1">
              <button
                type="button"
                onClick={handlePrev}
                disabled={currentPage <= 1}
                className="px-2.5 py-1 rounded-lg bg-white/10 hover:bg-[#2ab4e8] disabled:opacity-30 text-white text-xs font-black transition cursor-pointer disabled:cursor-default"
                title="Trang trước"
              >
                ←
              </button>

              <div className="flex items-center text-xs font-bold px-1.5 text-sky-100">
                <span className="hidden xs:inline mr-1 opacity-80">{lang === 'vi' ? 'Trang' : 'P.'}</span>
                <input
                  type="text"
                  value={pageInput}
                  onChange={(e) => setPageInput(e.target.value)}
                  onKeyDown={handlePageInputKeyDown}
                  onBlur={() => {
                    const parsed = parseInt(pageInput, 10);
                    if (!isNaN(parsed)) goToPage(parsed);
                    else setPageInput(String(currentPage));
                  }}
                  aria-label="Số trang"
                  className="w-11 text-center bg-slate-900 text-white font-extrabold py-0.5 rounded-md border border-sky-300/30 focus:outline-none focus:border-[#2ab4e8]"
                />
                <span className="mx-1 opacity-70">/</span>
                <span>{numPages || '--'}</span>
              </div>

              <button
                type="button"
                onClick={handleNext}
                disabled={numPages !== null && currentPage >= numPages}
                className="px-2.5 py-1 rounded-lg bg-white/10 hover:bg-[#2ab4e8] disabled:opacity-30 text-white text-xs font-black transition cursor-pointer disabled:cursor-default"
                title="Trang tiếp theo"
              >
                →
              </button>
            </div>

            {/* Zoom Controls */}
            <div className="hidden sm:inline-flex items-center bg-slate-950/55 border border-white/15 rounded-xl p-1 gap-0.5">
              <button
                type="button"
                onClick={() => setZoomScale((z) => Math.max(0.6, Math.round((z - 0.15) * 100) / 100))}
                className="w-7 h-7 rounded-lg hover:bg-white/15 text-white font-black text-sm flex items-center justify-center cursor-pointer"
                title="Thu nhỏ"
              >
                −
              </button>
              <button
                type="button"
                onClick={() => setZoomScale(1)}
                className="px-1.5 text-[11px] font-mono font-extrabold text-sky-200 hover:text-white cursor-pointer"
                title="Đặt lại 100%"
              >
                {Math.round(zoomScale * 100)}%
              </button>
              <button
                type="button"
                onClick={() => setZoomScale((z) => Math.min(2.2, Math.round((z + 0.15) * 100) / 100))}
                className="w-7 h-7 rounded-lg hover:bg-white/15 text-white font-black text-sm flex items-center justify-center cursor-pointer"
                title="Phóng to"
              >
                +
              </button>
            </div>
          </div>
        )}

        {/* Right: Viewer Mode, Download, Fullscreen */}
        <div className="flex items-center gap-1.5 ml-auto sm:ml-0">
          <button
            type="button"
            onClick={() => setUseNativeFallback((v) => !v)}
            className="px-2.5 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/15 text-[11px] sm:text-xs font-bold text-sky-100 transition cursor-pointer"
            title="Chuyển đổi giữa chế độ lật trang thông minh (hỗ trợ tra từ điển) và chế độ cuộn PDF gốc của trình duyệt"
          >
            {useNativeFallback
              ? lang === 'vi'
                ? '📖 Chế độ Lật trang'
                : '📖 Book Mode'
              : lang === 'vi'
              ? '📜 Cuộn PDF'
              : '📜 Scroll PDF'}
          </button>

          <a
            href={pdfUrl}
            target="_blank"
            rel="noopener noreferrer"
            download
            className="px-2.5 sm:px-3 py-1.5 rounded-xl bg-emerald-500/90 hover:bg-emerald-500 text-white text-[11px] sm:text-xs font-extrabold transition shadow-xs inline-flex items-center gap-1"
            title="Mở / Tải file PDF về máy"
          >
            <span>⬇</span>
            <span className="hidden xs:inline">{lang === 'vi' ? 'Tải PDF' : 'PDF'}</span>
          </a>

          <button
            type="button"
            onClick={() => setIsTheater((v) => !v)}
            className={`px-3 py-1.5 rounded-xl text-xs font-extrabold transition cursor-pointer inline-flex items-center gap-1.5 ${
              isTheater
                ? 'bg-rose-500 hover:bg-rose-600 text-white shadow-sm'
                : 'bg-[#2ab4e8] hover:bg-sky-400 text-white shadow-sm'
            }`}
          >
            <span>{isTheater ? '✕' : '⛶'}</span>
            <span>
              {isTheater
                ? lang === 'vi'
                  ? 'Thu nhỏ'
                  : 'Exit Fullscreen'
                : lang === 'vi'
                ? 'Toàn màn hình'
                : 'Fullscreen'}
            </span>
          </button>
        </div>
      </div>

      {/* Quick Progress Scrubber + Saved Page Reset */}
      {!useNativeFallback && numPages && numPages > 1 && (
        <div className="bg-slate-900/95 border-b border-slate-800 px-4 sm:px-6 py-2 flex items-center gap-3 text-xs text-slate-300">
          <span className="font-semibold text-sky-300 shrink-0">
            {Math.round((currentPage / numPages) * 100)}%
          </span>
          <input
            type="range"
            min={1}
            max={numPages}
            value={currentPage}
            onChange={(e) => goToPage(parseInt(e.target.value, 10))}
            aria-label="Thanh trượt chuyển trang nhanh"
            className="flex-1 h-1.5 accent-[#2ab4e8] cursor-pointer"
          />
          {currentPage > 1 && (
            <button
              type="button"
              onClick={() => goToPage(1)}
              className="text-[11px] font-bold text-slate-400 hover:text-white underline cursor-pointer shrink-0"
            >
              {lang === 'vi' ? 'Về bìa đầu (Trang 1)' : 'Back to Cover'}
            </button>
          )}
        </div>
      )}

      {/* Main Reading Viewport */}
      <style>{`
        .ebook-page-left { box-shadow: inset -18px 0 28px -15px rgba(0,0,0,0.22), -4px 6px 24px rgba(0,0,0,0.45); }
        .ebook-page-right { box-shadow: inset 18px 0 28px -15px rgba(0,0,0,0.22), 4px 6px 24px rgba(0,0,0,0.45); }
        .ebook-page-single { box-shadow: 0 10px 36px rgba(0,0,0,0.45), 0 2px 10px rgba(0,0,0,0.28); }
      `}</style>

      {useNativeFallback ? (
        <div className={isTheater ? 'flex-1 w-full bg-slate-900' : 'w-full h-[78vh] min-h-[620px] bg-slate-900'}>
          <iframe
            src={`${pdfUrl}#view=FitH`}
            title={title}
            className="w-full h-full border-0 bg-white"
          />
        </div>
      ) : (
        <div
          ref={canvasAreaRef}
          className={`${
            isTheater ? 'flex-1' : 'max-h-[82vh] min-h-[540px]'
          } overflow-auto flex flex-col items-center justify-start p-3 sm:p-6 bg-[#0b1220] relative custom-scrollbar`}
        >
          {isLoadingPage && (
            <div className="sticky top-4 z-10 mb-3 px-4 py-2 rounded-full bg-slate-900/90 border border-sky-400/30 text-sky-200 text-xs font-bold flex items-center gap-2 shadow-lg">
              <span className="w-3.5 h-3.5 border-2 border-sky-400/30 border-t-sky-400 rounded-full animate-spin" />
              <span>{lang === 'vi' ? 'Đang tải trang sách...' : 'Loading page...'}</span>
            </div>
          )}

          <Document
            file={pdfUrl}
            onLoadSuccess={({ numPages: loadedPages }) => {
              setNumPages(loadedPages);
              if (currentPage > loadedPages) {
                setCurrentPage(1);
              }
              setIsLoadingPage(false);
            }}
            onLoadError={() => {
              setIsLoadingPage(false);
              setUseNativeFallback(true);
            }}
            loading={null}
          >
            <div
              className={`flex justify-center items-start ${
                isTwoPageMode ? 'gap-0 flex-col lg:flex-row' : ''
              }`}
            >
              <Page
                pageNumber={currentPage}
                width={renderedPageWidth}
                renderTextLayer={true}
                renderAnnotationLayer={true}
                onRenderSuccess={() => setIsLoadingPage(false)}
                className={`bg-white rounded-xs overflow-hidden ${
                  isTwoPageMode && containerWidth >= 900 ? 'ebook-page-left' : 'ebook-page-single'
                }`}
                loading={null}
              />

              {isTwoPageMode &&
                containerWidth >= 900 &&
                numPages !== null &&
                currentPage + 1 <= numPages && (
                  <Page
                    pageNumber={currentPage + 1}
                    width={renderedPageWidth}
                    renderTextLayer={true}
                    renderAnnotationLayer={true}
                    onRenderSuccess={() => setIsLoadingPage(false)}
                    className="bg-white rounded-xs overflow-hidden hidden lg:block ebook-page-right"
                    loading={null}
                  />
                )}
            </div>
          </Document>

          {/* Bottom Page Turn Bar for effortless continuous reading */}
          {numPages && numPages > 1 && (
            <div className="mt-5 flex items-center justify-center gap-3 pb-2">
              <button
                type="button"
                onClick={handlePrev}
                disabled={currentPage <= 1}
                className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-[#0a5482] disabled:opacity-35 text-white text-xs sm:text-sm font-extrabold border border-slate-700 transition cursor-pointer disabled:cursor-default"
              >
                ← {lang === 'vi' ? 'Trang trước' : 'Previous Page'}
              </button>
              <span className="text-xs sm:text-sm font-bold text-slate-300 px-2">
                {lang === 'vi' ? `Trang ${currentPage} / ${numPages}` : `Page ${currentPage} of ${numPages}`}
              </span>
              <button
                type="button"
                onClick={handleNext}
                disabled={currentPage >= numPages}
                className="px-4 py-2 rounded-xl bg-[#0a5482] hover:bg-[#2ab4e8] disabled:opacity-35 text-white text-xs sm:text-sm font-extrabold border border-sky-400/30 transition cursor-pointer disabled:cursor-default"
              >
                {lang === 'vi' ? 'Trang tiếp theo' : 'Next Page'} →
              </button>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default LibraryEbookViewer;
