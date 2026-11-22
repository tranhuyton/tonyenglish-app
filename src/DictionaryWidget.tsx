import React, { useState, useEffect, useRef, useCallback } from 'react';
import { X, BookOpen, Maximize2 } from 'lucide-react';

const TEST_VIEWS = [
  'computer',
  'paper',
  'mixed-paper',
  'standard',
  'standard-splitscreen',
  'case-study',
  'igcse',
  'igcse-direct',
  'sat-bluebook',
  'ielts-writing',
  'ielts-speaking',
];

interface DictionaryWidgetProps {
  currentView: string;
  initialIsReview?: boolean;
}

export default function DictionaryWidget({ currentView, initialIsReview = false }: DictionaryWidgetProps) {
  const [isReviewMode, setIsReviewMode] = useState<boolean>(initialIsReview);
  const [quickDict, setQuickDict] = useState<{ word: string; x: number; y: number } | null>(null);
  const [standaloneOpen, setStandaloneOpen] = useState<boolean>(false);
  const popupRef = useRef<HTMLDivElement>(null);

  // Đồng bộ trạng thái khởi tạo khi đổi bài test hoặc đổi view
  useEffect(() => {
    if (TEST_VIEWS.includes(currentView)) {
      setIsReviewMode(Boolean(initialIsReview));
    } else {
      setIsReviewMode(false);
    }
  }, [currentView, initialIsReview]);

  // Chỉ bật tính năng Từ điển khi đang ở:
  // 1. Bài giảng (currentView === 'lecture')
  // 2. Phần chữa bài của các bài test/thi (TEST_VIEWS.includes(currentView) && isReviewMode === true)
  const isEnabled = currentView === 'lecture' || (TEST_VIEWS.includes(currentView) && isReviewMode);

  const openQuickLookupAt = useCallback((rawWord: string, clientX: number, clientY: number, rectTop?: number) => {
    const cleanWord = rawWord
      .replace(/^[^a-zA-Z0-9À-ỹ'-]+|[^a-zA-Z0-9À-ỹ'-]+$/g, '')
      .trim()
      .toLowerCase();

    if (cleanWord.length > 1 && cleanWord.length <= 45 && cleanWord.split(/\s+/).length <= 3) {
      const popupWidth = 315;
      const popupHeight = 240;
      const margin = 12;

      let x = clientX - popupWidth / 2;
      if (x < margin) x = margin;
      if (x + popupWidth > window.innerWidth - margin) {
        x = Math.max(margin, window.innerWidth - popupWidth - margin);
      }

      let y = clientY + 12;
      if (y + popupHeight > window.innerHeight - margin) {
        const topAnchor = typeof rectTop === 'number' ? rectTop : clientY;
        y = Math.max(margin, topAnchor - popupHeight - 12);
      }

      setQuickDict({ word: cleanWord, x: Math.round(x), y: Math.round(y) });
    }
  }, []);

  // Lắng nghe sự kiện chuyển sang chế độ Chữa bài (Review Mode), mở từ điển lớn, hoặc mở tra nhanh từ iframe bài giảng
  useEffect(() => {
    const handleReviewChange = (e: Event) => {
      const customEvent = e as CustomEvent<boolean>;
      setIsReviewMode(Boolean(customEvent.detail));
    };
    const handleOpenStandalone = () => {
      setStandaloneOpen(true);
    };
    const handleOpenQuick = (e: Event) => {
      const customEvent = e as CustomEvent<{ word: string; x: number; y: number; rectTop?: number }>;
      if (customEvent.detail?.word) {
        openQuickLookupAt(
          customEvent.detail.word,
          customEvent.detail.x,
          customEvent.detail.y,
          customEvent.detail.rectTop
        );
      }
    };
    const handleCloseQuick = () => {
      setQuickDict(null);
    };

    window.addEventListener('tony-review-mode-change', handleReviewChange);
    window.addEventListener('tony-open-standalone-dictionary', handleOpenStandalone);
    window.addEventListener('tony-open-quick-dictionary', handleOpenQuick);
    window.addEventListener('tony-close-quick-dictionary', handleCloseQuick);
    return () => {
      window.removeEventListener('tony-review-mode-change', handleReviewChange);
      window.removeEventListener('tony-open-standalone-dictionary', handleOpenStandalone);
      window.removeEventListener('tony-open-quick-dictionary', handleOpenQuick);
      window.removeEventListener('tony-close-quick-dictionary', handleCloseQuick);
    };
  }, [openQuickLookupAt]);

  // Tự động đóng mọi popup nếu chuyển sang trạng thái làm bài thi hoặc trang không hỗ trợ
  useEffect(() => {
    if (!isEnabled) {
      setQuickDict(null);
      setStandaloneOpen(false);
    }
  }, [isEnabled]);

  // Bắt sự kiện Click đúp chuột (dblclick) và tổ hợp phím Ctrl + Shift + A (giống autosearch.js)
  useEffect(() => {
    if (!isEnabled) return;

    const handleDblClick = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      if (!target) return;
      if (
        target.tagName === 'INPUT' ||
        target.tagName === 'TEXTAREA' ||
        target.isContentEditable ||
        target.closest('#tony-quick-dict-popup') ||
        target.closest('#tony-standalone-dict-modal')
      ) {
        return;
      }

      const selection = window.getSelection();
      if (!selection) return;
      const rawText = selection.toString().trim();
      if (!rawText) return;

      let rectBottom = e.clientY;
      let rectTop = e.clientY;
      let centerX = e.clientX;
      if (selection.rangeCount > 0) {
        const rect = selection.getRangeAt(0).getBoundingClientRect();
        if (rect.width > 0 || rect.height > 0) {
          centerX = rect.left + rect.width / 2;
          rectBottom = rect.bottom;
          rectTop = rect.top;
        }
      }
      openQuickLookupAt(rawText, centerX, rectBottom, rectTop);
    };

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.ctrlKey && e.shiftKey && (e.key === 'A' || e.key === 'a')) {
        const rawText = window.getSelection()?.toString().trim() || '';
        if (rawText) {
          openQuickLookupAt(rawText, window.innerWidth / 2, window.innerHeight / 2 - 40, window.innerHeight / 2 - 40);
        }
      } else if (e.key === 'Escape') {
        setQuickDict(null);
        setStandaloneOpen(false);
      }
    };

    const handleMouseDown = (e: MouseEvent) => {
      if (popupRef.current && !popupRef.current.contains(e.target as Node)) {
        setQuickDict(null);
      }
    };

    document.addEventListener('dblclick', handleDblClick);
    document.addEventListener('keydown', handleKeyDown);
    document.addEventListener('mousedown', handleMouseDown);
    return () => {
      document.removeEventListener('dblclick', handleDblClick);
      document.removeEventListener('keydown', handleKeyDown);
      document.removeEventListener('mousedown', handleMouseDown);
    };
  }, [isEnabled, openQuickLookupAt]);

  if (!isEnabled) return null;

  return (
    <>
      {/* POPUP TRA NHANH KHI CLICK ĐÚP CHUỘT (TONYDICT MODERN) */}
      {quickDict && (
        <div
          id="tony-quick-dict-popup"
          ref={popupRef}
          className="fixed z-[999999] bg-white rounded-2xl border border-slate-200/90 shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-150"
          style={{
            left: `${quickDict.x}px`,
            top: `${quickDict.y}px`,
            width: '320px',
            maxWidth: 'calc(100vw - 24px)',
          }}
        >
          <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-3 py-2 flex items-center justify-between gap-2 text-white">
            <button
              type="button"
              onClick={() => {
                setStandaloneOpen(true);
                setQuickDict(null);
              }}
              className="flex items-center gap-2 min-w-0 hover:opacity-90 transition cursor-pointer text-left"
              title="Bấm để mở Từ điển lớn"
            >
              <img
                src="/logo-shield.png"
                alt="TonyDict"
                className="h-5 w-auto object-contain shrink-0"
              />
              <span className="font-black text-xs tracking-tight truncate">
                <span className="text-[#2ab4e8]">TONY</span>DICT
              </span>
              <span className="text-[11px] font-semibold text-sky-200/90 truncate max-w-[120px]">
                • {quickDict.word}
              </span>
            </button>

            <div className="flex items-center gap-1 shrink-0">
              <button
                type="button"
                onClick={() => {
                  setStandaloneOpen(true);
                  setQuickDict(null);
                }}
                className="w-6 h-6 rounded-lg flex items-center justify-center text-white/75 hover:text-white hover:bg-white/15 transition cursor-pointer"
                title="Mở toàn màn hình Từ điển"
              >
                <Maximize2 className="w-3.5 h-3.5" />
              </button>
              <button
                type="button"
                onClick={() => setQuickDict(null)}
                className="w-6 h-6 rounded-lg flex items-center justify-center text-white/75 hover:text-white hover:bg-white/15 transition cursor-pointer"
                title="Đóng (Esc)"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          </div>

          <div className="bg-white w-full h-[210px]">
            <iframe
              key={quickDict.word}
              src={`https://dic.tienganh123.com/fast_dict.php?word=${encodeURIComponent(quickDict.word)}&dict=ev_ve&m=yes`}
              className="w-full h-[210px] border-0 block"
              title={`Tra từ: ${quickDict.word}`}
            />
          </div>
        </div>
      )}

      {/* MODAL TỪ ĐIỂN RIÊNG BIỆT (STANDALONE DICTIONARY - TONYDICT MODERN) */}
      {standaloneOpen && (
        <div
          id="tony-standalone-dict-modal"
          className="fixed inset-0 z-[99998] bg-slate-900/55 backdrop-blur-sm flex items-center justify-center p-3 sm:p-6 animate-in fade-in duration-150"
          onClick={() => setStandaloneOpen(false)}
        >
          <div
            className="bg-white rounded-2xl shadow-2xl border border-slate-200/90 w-full max-w-[940px] h-[84vh] max-h-[740px] flex flex-col overflow-hidden animate-in zoom-in-95 duration-150"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-4 sm:px-5 py-3 flex items-center justify-between gap-3 text-white shrink-0">
              <div className="flex items-center gap-2.5 min-w-0">
                <img
                  src="/logo-shield.png"
                  alt="TonyDict"
                  className="h-7 w-auto object-contain shrink-0"
                />
                <div className="flex items-center gap-2 min-w-0">
                  <span className="font-black text-base tracking-tight shrink-0">
                    <span className="text-[#2ab4e8]">TONY</span>DICT
                  </span>
                  <span className="hidden sm:inline-block text-white/30">|</span>
                  <span className="hidden sm:inline-flex items-center gap-1.5 text-xs font-semibold text-sky-100/90 truncate">
                    <BookOpen className="w-3.5 h-3.5 text-[#2ab4e8] shrink-0" />
                    <span>Từ điển Anh - Việt / Việt - Anh / Đồng nghĩa</span>
                  </span>
                </div>
              </div>
              <button
                type="button"
                onClick={() => setStandaloneOpen(false)}
                className="w-8 h-8 rounded-xl bg-white/10 hover:bg-white/20 text-white flex items-center justify-center transition cursor-pointer shrink-0"
                title="Đóng (Esc)"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <div className="flex-1 bg-white w-full overflow-hidden">
              <iframe
                src="https://dic.tienganh123.com/v2/"
                className="w-full h-full border-0"
                title="Từ điển riêng biệt TonyEnglish"
              />
            </div>
          </div>
        </div>
      )}
    </>
  );
}
