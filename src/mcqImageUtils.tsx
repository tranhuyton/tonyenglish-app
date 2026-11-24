import React, { useEffect, useRef, useState } from 'react';
import { useLmsLang } from './utils/lmsI18n';

export interface LightboxImageItem {
  src: string;
  caption?: string;
}

export interface LightboxState {
  items: LightboxImageItem[];
  index: number;
}

export interface ExtractLightboxOptions {
  includeSvg?: boolean;
  allowInsideLabel?: boolean;
  svgContainerSelector?: string;
}

const GENERIC_IMAGE_ALT_RE =
  /^(?:image|img|diagram|photo|picture|illustration|figure|section image|question image|part image|fill image|zoomed illustration|student work|bài làm)$/i;
const IMAGE_URL_EXT_RE = /\.(?:png|jpe?g|gif|webp|svg|bmp|avif)(?:\?.*)?$/i;

function getImageCaption(img: HTMLImageElement): string {
  const fig = img.closest('figure');
  const figCap = fig?.querySelector('figcaption')?.textContent?.trim();
  if (figCap) return figCap;
  const alt = (img.getAttribute('alt') || '').trim();
  if (alt && !GENERIC_IMAGE_ALT_RE.test(alt)) return alt;
  const title = (img.getAttribute('title') || '').trim();
  if (title && !GENERIC_IMAGE_ALT_RE.test(title)) return title;
  return '';
}

function isEligibleLightboxImg(
  img: HTMLImageElement,
  allowInsideLabel: boolean
): boolean {
  if (img.hasAttribute('data-no-lightbox') || img.classList.contains('no-lightbox')) {
    return false;
  }
  if (!allowInsideLabel && img.closest('label')) {
    return false;
  }
  if (img.closest('button') && !img.hasAttribute('data-lightbox')) {
    return false;
  }
  const anchor = img.closest('a[href]');
  if (anchor) {
    const href = (anchor.getAttribute('href') || '').trim();
    if (
      href &&
      href !== '#' &&
      !href.startsWith('javascript:') &&
      !IMAGE_URL_EXT_RE.test(href)
    ) {
      return false;
    }
  }
  const rect = img.getBoundingClientRect();
  if (rect.width > 0 && rect.width < 44 && rect.height > 0 && rect.height < 44) {
    return false;
  }
  if (
    img.naturalWidth > 0 &&
    img.naturalWidth < 48 &&
    img.naturalHeight > 0 &&
    img.naturalHeight < 48
  ) {
    return false;
  }
  const src = img.currentSrc || img.src;
  return Boolean(src);
}

function isEligibleLightboxSvg(
  svg: SVGSVGElement,
  svgContainerSelector?: string
): boolean {
  if (
    svg.classList.contains('lucide') ||
    svg.hasAttribute('data-no-lightbox') ||
    svg.classList.contains('no-lightbox')
  ) {
    return false;
  }
  if (svg.closest('button, a[href], label')) {
    return false;
  }
  if (svgContainerSelector && !svg.closest(svgContainerSelector)) {
    return false;
  }
  const rect = svg.getBoundingClientRect();
  return rect.width >= 90 && rect.height >= 60;
}

function svgElementToDataUri(svgEl: SVGSVGElement): string | null {
  try {
    const clone = svgEl.cloneNode(true) as SVGSVGElement;
    if (!clone.getAttribute('xmlns')) {
      clone.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    }
    const rect = svgEl.getBoundingClientRect();
    const vb = svgEl.getAttribute('viewBox');
    let w = rect.width || 400;
    let h = rect.height || 300;
    if (vb) {
      const parts = vb.trim().split(/[\s,]+/).map(Number);
      if (parts.length === 4 && parts[2] > 0 && parts[3] > 0) {
        w = parts[2];
        h = parts[3];
      }
    } else {
      clone.setAttribute('viewBox', `0 0 ${Math.round(w)} ${Math.round(h)}`);
    }
    const scale = w < 720 ? 720 / w : 1;
    clone.setAttribute('width', String(Math.round(w * scale)));
    clone.setAttribute('height', String(Math.round(h * scale)));
    const xml = new XMLSerializer().serializeToString(clone);
    return `data:image/svg+xml;charset=utf-8,${encodeURIComponent(xml)}`;
  } catch {
    return null;
  }
}

export function extractLightboxFromClick(
  e: React.MouseEvent | MouseEvent,
  root?: HTMLElement | null,
  options?: ExtractLightboxOptions
): LightboxState | null {
  const target = e.target as Element | null;
  if (!target || typeof target.closest !== 'function') return null;

  const allowInsideLabel = Boolean(options?.allowInsideLabel);
  const scanRoot = root || (e.currentTarget as HTMLElement | null);

  const imgEl = target.closest('img') as HTMLImageElement | null;
  if (imgEl && isEligibleLightboxImg(imgEl, allowInsideLabel)) {
    const anchor = imgEl.closest('a[href]');
    if (anchor) {
      e.preventDefault();
    }
    const clickedSrc = imgEl.currentSrc || imgEl.src;
    const items: LightboxImageItem[] = [];
    let clickedIndex = -1;

    if (scanRoot) {
      const allImgs = Array.from(scanRoot.querySelectorAll<HTMLImageElement>('img'));
      for (const el of allImgs) {
        if (!isEligibleLightboxImg(el, allowInsideLabel)) continue;
        const src = el.currentSrc || el.src;
        if (!src) continue;
        if (el === imgEl) clickedIndex = items.length;
        items.push({ src, caption: getImageCaption(el) });
      }
    }

    if (clickedIndex === -1 || items.length === 0) {
      return {
        items: [{ src: clickedSrc, caption: getImageCaption(imgEl) }],
        index: 0,
      };
    }
    return { items, index: clickedIndex };
  }

  if (options?.includeSvg) {
    const svgEl = target.closest('svg') as SVGSVGElement | null;
    if (svgEl && isEligibleLightboxSvg(svgEl, options.svgContainerSelector)) {
      const items: LightboxImageItem[] = [];
      let clickedIndex = -1;

      if (scanRoot) {
        const selector = options.svgContainerSelector
          ? `${options.svgContainerSelector} svg, img`
          : 'svg, img';
        const candidates = Array.from(scanRoot.querySelectorAll(selector));
        for (const el of candidates) {
          if (el.tagName.toLowerCase() === 'img') {
            const iEl = el as HTMLImageElement;
            if (!isEligibleLightboxImg(iEl, allowInsideLabel)) continue;
            items.push({ src: iEl.currentSrc || iEl.src, caption: getImageCaption(iEl) });
          } else if (el.tagName.toLowerCase() === 'svg') {
            const sEl = el as SVGSVGElement;
            if (!isEligibleLightboxSvg(sEl, options.svgContainerSelector)) continue;
            const uri = svgElementToDataUri(sEl);
            if (!uri) continue;
            if (sEl === svgEl) clickedIndex = items.length;
            const aria = (sEl.getAttribute('aria-label') || sEl.querySelector('title')?.textContent || '').trim();
            items.push({ src: uri, caption: aria });
          }
        }
      }

      if (clickedIndex === -1 || items.length === 0) {
        const uri = svgElementToDataUri(svgEl);
        if (!uri) return null;
        const aria = (svgEl.getAttribute('aria-label') || svgEl.querySelector('title')?.textContent || '').trim();
        return { items: [{ src: uri, caption: aria }], index: 0 };
      }
      return { items, index: clickedIndex };
    }
  }

  return null;
}

const ATTR_REGEX = /([a-zA-Z_:][-a-zA-Z0-9_:.]*)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'=<>`]+))/g;

/**
 * Strips artificial shrinking attributes/styles/classes (e.g. width="300",
 * max-width: 50%; width: auto !important, max-w-md, max-width: 240px..440px)
 * from <img> tags in test HTML while preserving multi-image flex/grid layouts
 * and clip-path crops.
 */
export function normalizeHtmlImages(rawHtml: string): string {
  if (!rawHtml || !/<img\b/i.test(rawHtml)) return rawHtml;

  const imgCount = (rawHtml.match(/<img\b/gi) || []).length;
  const preserveGridClasses =
    imgCount > 1 &&
    Array.from(rawHtml.matchAll(/class\s*=\s*(['"])(.*?)\1/gi)).some((cm) => {
      const c = cm[2];
      return /\bgrid\b/i.test(c) || (/\bflex\b/i.test(c) && !/\bflex-col\b/i.test(c));
    });

  return rawHtml.replace(/<img\b[^>]*>/gi, (imgTag) => {
    const isSelfClosing = /\/\s*>$/.test(imgTag);
    const attrs: Record<string, string> = {};
    const attrOrder: string[] = [];

    ATTR_REGEX.lastIndex = 0;
    let m: RegExpExecArray | null;
    while ((m = ATTR_REGEX.exec(imgTag)) !== null) {
      const rawName = m[1];
      const val = m[2] ?? m[3] ?? m[4] ?? '';
      const key = rawName.toLowerCase() === 'classname' ? 'class' : rawName.toLowerCase();
      if (!(key in attrs)) attrOrder.push(key);
      attrs[key] = val;
    }

    if (!attrs.src) return imgTag;

    delete attrs.width;
    delete attrs.height;

    const rawStyle = attrs.style || '';
    const hasClipPath = /clip-path\s*:/i.test(rawStyle);

    if (rawStyle) {
      const keptStyles: string[] = [];
      rawStyle.split(';').forEach((decl) => {
        const idx = decl.indexOf(':');
        if (idx === -1) return;
        const prop = decl.slice(0, idx).trim().toLowerCase();
        const val = decl.slice(idx + 1).trim();
        if (!prop || !val) return;
        if (
          prop === 'width' ||
          prop === 'max-width' ||
          prop === 'min-width' ||
          prop === 'height' ||
          prop === 'max-height' ||
          prop === 'min-height' ||
          prop === 'object-fit' ||
          prop === 'border' ||
          prop.startsWith('border-') ||
          prop === 'box-shadow' ||
          prop === 'margin' ||
          prop === 'margin-left' ||
          prop === 'margin-right' ||
          prop === 'margin-top' ||
          (!hasClipPath && prop === 'margin-bottom')
        ) {
          return;
        }
        keptStyles.push(`${prop}: ${val}`);
      });
      if (keptStyles.length > 0) {
        attrs.style = keptStyles.join('; ');
      } else {
        delete attrs.style;
      }
    }

    if (hasClipPath) {
      attrs['data-preserve-size'] = '1';
      if (!attrOrder.includes('data-preserve-size')) attrOrder.push('data-preserve-size');
    }

    const rawTokens = (attrs.class || '').split(/\s+/).filter(Boolean);
    const cleanedTokens = rawTokens.filter((tok) => {
      if (/^(?:border|rounded|shadow)(?:-|$)/i.test(tok)) return false;
      if (!preserveGridClasses && !hasClipPath) {
        if (/^(?:[a-z]+:)?(?:max-w-|min-w-|max-h-|min-h-|w-(?!full\b)|h-(?!auto\b))/i.test(tok)) {
          return false;
        }
      }
      return true;
    });

    const markerClass = preserveGridClasses || hasClipPath ? 'mcq-zoomable-img' : 'mcq-cropped-img';
    if (!cleanedTokens.includes(markerClass)) cleanedTokens.push(markerClass);
    attrs.class = cleanedTokens.join(' ');
    if (!attrOrder.includes('class')) attrOrder.push('class');

    const rebuiltAttrs = attrOrder
      .filter((k) => k in attrs)
      .map((k) => {
        const v = attrs[k];
        return v.includes('"') && !v.includes("'") ? `${k}='${v}'` : `${k}="${v.replace(/"/g, '&quot;')}"`;
      })
      .join(' ');

    return `<img ${rebuiltAttrs}${isSelfClosing ? ' />' : '>'}`;
  });
}

/**
 * Computes crisp, readable display dimensions for cropped PDF illustrations
 * based on intrinsic pixel dimensions & aspect ratio so wide 4-panel strips,
 * 4-column tables, graphs, apparatus, and geometry diagrams are all easy to read.
 */
export function applySmartMcqImageSizing(img: HTMLImageElement | null): void {
  if (!img || img.dataset.preserveSize === '1') return;

  if (img.closest('.part-passage-box')) {
    img.style.width = '100%';
    img.style.maxWidth = '100%';
    img.style.height = 'auto';
    return;
  }

  const nw = img.naturalWidth;
  const nh = img.naturalHeight;
  if (!nw || !nh) return;

  // Respect horizontal multi-image flex/grid containers inside rich HTML
  let parent = img.parentElement;
  for (let depth = 0; depth < 3 && parent; depth++) {
    const cls = parent.className || '';
    if (
      (/\bgrid\b/.test(cls) || (/\bflex\b/.test(cls) && !/\bflex-col\b/.test(cls))) &&
      parent.querySelectorAll('img').length > 1
    ) {
      img.style.cursor = 'zoom-in';
      return;
    }
    if (parent.classList?.contains('html-content-renderer')) break;
    parent = parent.parentElement;
  }

  const ar = nw / nh;

  if (nw < 140 && nh < 90) {
    img.dataset.inlineImg = '1';
    img.style.width = `${Math.round(nw * 1.35)}px`;
    img.style.maxWidth = '100%';
    img.style.height = 'auto';
    return;
  }

  const maxUpscale = Math.round(nw * 1.85);
  let targetWidth: number;
  if (ar >= 2.2) {
    // Wide 4-panel strips (ESL 0510), 4-column option tables, wide multi-stage diagrams
    targetWidth = Math.min(940, Math.max(Math.min(780, maxUpscale), Math.round(nw * 1.65)));
  } else if (ar >= 1.55) {
    // Wide landscape graphs, 2x2 graph grids (A/B/C/D), wide apparatus
    targetWidth = Math.min(860, Math.max(Math.min(680, maxUpscale), Math.round(nw * 1.45)));
  } else if (ar >= 1.15) {
    // Medium landscape diagrams, apparatus, charts
    targetWidth = Math.min(740, Math.max(Math.min(560, maxUpscale), Math.round(nw * 1.45)));
  } else if (ar >= 0.8) {
    // Near-square diagrams (circle geometry, anatomical cross-sections)
    targetWidth = Math.min(600, Math.max(Math.min(460, maxUpscale), Math.round(nw * 1.35)));
  } else {
    // Tall portrait diagrams (thermometers, burettes, vertical columns)
    targetWidth = Math.min(560, Math.max(Math.min(380, maxUpscale), Math.round(nw * 1.3)));
  }

  const maxComfortHeight = ar < 0.85 ? 720 : 580;
  if (targetWidth / ar > maxComfortHeight) {
    targetWidth = Math.max(Math.min(360, nw), Math.round(maxComfortHeight * ar));
  }

  img.style.width = `${targetWidth}px`;
  img.style.maxWidth = '100%';
  img.style.height = 'auto';
  img.style.cursor = 'zoom-in';
}

export function scanContainerMcqImages(root: HTMLElement | null): void {
  if (!root) return;
  const imgs = root.querySelectorAll<HTMLImageElement>('img.mcq-cropped-img');
  imgs.forEach((img) => {
    if (img.complete && img.naturalWidth > 0) {
      applySmartMcqImageSizing(img);
    }
  });
}

export function McqImageZoomModal({
  src,
  caption,
  items,
  initialIndex = 0,
  onClose,
}: {
  src?: string | null;
  caption?: string;
  items?: LightboxImageItem[] | null;
  initialIndex?: number;
  onClose: () => void;
}) {
  const [lang] = useLmsLang();
  const isEn = lang === 'en';
  const [zoom, setZoom] = useState(1);
  const modalRef = useRef<HTMLDivElement>(null);

  const resolvedItems: LightboxImageItem[] =
    items && items.length > 0
      ? items
      : src
      ? [{ src, caption }]
      : [];

  const isOpen = resolvedItems.length > 0;
  const safeInitial = Math.max(0, Math.min(initialIndex, Math.max(0, resolvedItems.length - 1)));
  const [activeIndex, setActiveIndex] = useState(safeInitial);

  useEffect(() => {
    setActiveIndex(safeInitial);
    setZoom(1);
  }, [src, items, safeInitial]);

  useEffect(() => {
    if (!isOpen) return;
    // Pull keyboard focus out of iframes (e.g. LectureViewer) so Esc/+/-/arrows work immediately
    requestAnimationFrame(() => {
      try {
        modalRef.current?.focus({ preventScroll: true });
      } catch {
        modalRef.current?.focus();
      }
    });
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
      } else if (e.key === '+' || e.key === '=') {
        setZoom((z) => Math.min(3, +(z + 0.25).toFixed(2)));
      } else if (e.key === '-') {
        setZoom((z) => Math.max(0.5, +(z - 0.25).toFixed(2)));
      } else if (e.key === '0') {
        setZoom(1);
      } else if (e.key === 'ArrowLeft' && resolvedItems.length > 1) {
        setZoom(1);
        setActiveIndex((prev) => (prev - 1 + resolvedItems.length) % resolvedItems.length);
      } else if (e.key === 'ArrowRight' && resolvedItems.length > 1) {
        setZoom(1);
        setActiveIndex((prev) => (prev + 1) % resolvedItems.length);
      }
    };
    window.addEventListener('keydown', onKey);
    return () => {
      document.body.style.overflow = prevOverflow;
      window.removeEventListener('keydown', onKey);
    };
  }, [isOpen, resolvedItems.length, onClose]);

  if (!isOpen) return null;

  const activeItem = resolvedItems[activeIndex] || resolvedItems[0];
  if (!activeItem?.src) return null;

  const hasMultiple = resolvedItems.length > 1;
  const goPrev = () => {
    setZoom(1);
    setActiveIndex((prev) => (prev - 1 + resolvedItems.length) % resolvedItems.length);
  };
  const goNext = () => {
    setZoom(1);
    setActiveIndex((prev) => (prev + 1) % resolvedItems.length);
  };

  return (
    <div
      ref={modalRef}
      tabIndex={-1}
      role="dialog"
      aria-modal="true"
      aria-label={isEn ? 'Image Lightbox' : 'Phóng to hình ảnh'}
      className="fixed inset-0 bg-slate-950/90 backdrop-blur-md flex flex-col z-[100000] outline-none animate-in fade-in duration-150"
      onClick={onClose}
      data-testid="tony-image-lightbox"
    >
      {/* Top bar */}
      <div
        className="flex items-center justify-between gap-3 px-4 md:px-6 py-3 bg-slate-900/95 border-b border-slate-700/80 text-white shrink-0"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center gap-2.5 min-w-0">
          {hasMultiple && (
            <span className="px-2.5 py-1 rounded-full bg-white/15 text-xs font-extrabold tracking-wide shrink-0 tabular-nums">
              {activeIndex + 1} / {resolvedItems.length}
            </span>
          )}
          <span className="text-xs md:text-sm font-semibold text-slate-200 truncate">
            {activeItem.caption
              ? activeItem.caption
              : isEn
              ? '🔍 Image Lightbox — click image to zoom, Esc to close'
              : '🔍 Xem chi tiết hình ảnh — bấm vào ảnh để phóng to, nhấn Esc để đóng'}
          </span>
        </div>
        <div className="flex items-center gap-1.5 sm:gap-2 shrink-0">
          <button
            type="button"
            onClick={() => setZoom((z) => Math.max(0.5, +(z - 0.25).toFixed(2)))}
            className="px-2.5 sm:px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold text-sm border border-slate-600 transition cursor-pointer"
            title={isEn ? 'Zoom out (-)' : 'Thu nhỏ (-)'}
            aria-label={isEn ? 'Zoom out' : 'Thu nhỏ'}
          >
            −
          </button>
          <button
            type="button"
            onClick={() => setZoom(1)}
            className="px-2.5 sm:px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-sky-300 font-bold text-xs md:text-sm border border-slate-600 min-w-[58px] sm:min-w-[64px] transition cursor-pointer tabular-nums"
            title={isEn ? 'Reset to 100% (0)' : 'Đặt lại 100% (0)'}
          >
            {Math.round(zoom * 100)}%
          </button>
          <button
            type="button"
            onClick={() => setZoom((z) => Math.min(3, +(z + 0.25).toFixed(2)))}
            className="px-2.5 sm:px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold text-sm border border-slate-600 transition cursor-pointer"
            title={isEn ? 'Zoom in (+)' : 'Phóng to (+)'}
            aria-label={isEn ? 'Zoom in' : 'Phóng to'}
          >
            +
          </button>
          <button
            type="button"
            onClick={onClose}
            className="ml-1 sm:ml-2 px-3 sm:px-3.5 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs md:text-sm transition shadow cursor-pointer"
          >
            ✕ {isEn ? 'Close' : 'Đóng'}
          </button>
        </div>
      </div>

      {/* Main viewport */}
      <div className="flex-1 overflow-auto relative flex p-4 md:p-8">
        {hasMultiple && (
          <button
            type="button"
            onClick={(e) => {
              e.stopPropagation();
              goPrev();
            }}
            className="fixed left-3 md:left-6 top-1/2 -translate-y-1/2 z-20 w-10 h-10 md:w-12 md:h-12 rounded-full bg-slate-900/80 hover:bg-slate-800 text-white border border-white/20 flex items-center justify-center shadow-lg transition cursor-pointer"
            aria-label={isEn ? 'Previous image' : 'Ảnh trước'}
            title={isEn ? 'Previous (←)' : 'Ảnh trước (←)'}
          >
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
            </svg>
          </button>
        )}

        <div
          className="m-auto bg-white p-3 md:p-5 rounded-2xl shadow-2xl shrink-0 transition-all duration-150"
          style={
            zoom === 1
              ? { maxWidth: 'min(92vw, 1200px)' }
              : { width: `${Math.round(zoom * 85)}vw`, maxWidth: `${Math.round(zoom * 1200)}px` }
          }
          onClick={(e) => e.stopPropagation()}
        >
          <img
            src={activeItem.src}
            alt={activeItem.caption || (isEn ? 'Zoomed Illustration' : 'Hình minh họa phóng to')}
            onClick={() => setZoom((z) => (z === 1 ? 1.75 : 1))}
            title={
              zoom === 1
                ? isEn
                  ? 'Click to zoom in (175%)'
                  : 'Bấm để phóng to (175%)'
                : isEn
                ? 'Click to reset (100%)'
                : 'Bấm để thu về 100%'
            }
            className={
              zoom === 1
                ? 'max-h-[78vh] w-auto max-w-full h-auto block mx-auto object-contain select-none cursor-zoom-in'
                : 'w-full h-auto block object-contain select-none cursor-zoom-out'
            }
          />
        </div>

        {hasMultiple && (
          <button
            type="button"
            onClick={(e) => {
              e.stopPropagation();
              goNext();
            }}
            className="fixed right-3 md:right-6 top-1/2 -translate-y-1/2 z-20 w-10 h-10 md:w-12 md:h-12 rounded-full bg-slate-900/80 hover:bg-slate-800 text-white border border-white/20 flex items-center justify-center shadow-lg transition cursor-pointer"
            aria-label={isEn ? 'Next image' : 'Ảnh tiếp theo'}
            title={isEn ? 'Next (→)' : 'Ảnh tiếp (→)'}
          >
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
            </svg>
          </button>
        )}
      </div>

      {/* Subtle footer hint */}
      <div
        className="hidden sm:flex items-center justify-center px-4 py-2 text-[11px] font-medium text-slate-400 bg-slate-900/80 border-t border-slate-800 shrink-0"
        onClick={(e) => e.stopPropagation()}
      >
        {isEn
          ? `Click image to toggle zoom • + / - adjust zoom${hasMultiple ? ' • ← / → switch image' : ''} • Esc or click backdrop to close`
          : `Bấm vào ảnh để phóng to / thu nhỏ • + / - chỉnh mức phóng${hasMultiple ? ' • ← / → chuyển ảnh' : ''} • Esc hoặc bấm nền tối để đóng`}
      </div>
    </div>
  );
}

export const ImageLightboxModal = McqImageZoomModal;
