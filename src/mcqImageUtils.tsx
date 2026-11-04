import React, { useEffect, useState } from 'react';

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
  onClose,
}: {
  src: string | null;
  onClose: () => void;
}) {
  const [zoom, setZoom] = useState(1);

  useEffect(() => {
    setZoom(1);
  }, [src]);

  useEffect(() => {
    if (!src) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
      else if (e.key === '+' || e.key === '=') setZoom((z) => Math.min(3, +(z + 0.25).toFixed(2)));
      else if (e.key === '-') setZoom((z) => Math.max(0.5, +(z - 0.25).toFixed(2)));
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [src, onClose]);

  if (!src) return null;

  return (
    <div
      className="fixed inset-0 bg-slate-900/85 backdrop-blur-sm flex flex-col z-[100000] animate-in fade-in duration-150"
      onClick={onClose}
    >
      <div
        className="flex items-center justify-between px-4 md:px-6 py-3 bg-slate-900/90 border-b border-slate-700/80 text-white shrink-0"
        onClick={(e) => e.stopPropagation()}
      >
        <span className="text-xs md:text-sm font-semibold text-slate-300">
          🔍 Xem chi tiết hình minh họa (bấm ra ngoài hoặc nhấn Esc để đóng)
        </span>
        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={() => setZoom((z) => Math.max(0.5, +(z - 0.25).toFixed(2)))}
            className="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold text-sm border border-slate-600 transition"
            title="Thu nhỏ"
          >
            −
          </button>
          <button
            type="button"
            onClick={() => setZoom(1)}
            className="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-sky-300 font-bold text-xs md:text-sm border border-slate-600 min-w-[64px] transition"
            title="Đặt lại 100%"
          >
            {Math.round(zoom * 100)}%
          </button>
          <button
            type="button"
            onClick={() => setZoom((z) => Math.min(3, +(z + 0.25).toFixed(2)))}
            className="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold text-sm border border-slate-600 transition"
            title="Phóng to"
          >
            +
          </button>
          <button
            type="button"
            onClick={onClose}
            className="ml-2 px-3.5 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs md:text-sm transition shadow"
          >
            ✕ Đóng
          </button>
        </div>
      </div>

      <div className="flex-1 overflow-auto flex p-4 md:p-8">
        <div
          className="m-auto bg-white p-3 md:p-6 rounded-2xl shadow-2xl shrink-0"
          style={
            zoom === 1
              ? { maxWidth: 'min(92vw, 1150px)' }
              : { width: `${Math.round(zoom * 85)}vw`, maxWidth: `${Math.round(zoom * 1150)}px` }
          }
          onClick={(e) => e.stopPropagation()}
        >
          <img
            src={src}
            alt="Zoomed Illustration"
            className={zoom === 1 ? 'max-h-[80vh] w-auto max-w-full h-auto block mx-auto object-contain select-none' : 'w-full h-auto block object-contain select-none'}
          />
        </div>
      </div>
    </div>
  );
}
