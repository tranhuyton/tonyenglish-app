import React, { useState, useEffect, useRef, useCallback } from 'react';

const TEST_VIEWS = [
  'computer',
  'paper',
  'mixed-paper',
  'standard',
  'standard-splitscreen',
  'case-study',
  'igcse',
  'igcse-direct',
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
      const popupWidth = 340;
      const popupHeight = 265;
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
      {/* POPUP TRA NHANH KHI CLICK ĐÚP CHUỘT (LẤY TỪ DIC.TIENGANH123.COM) */}
      {quickDict && (
        <div
          id="tony-quick-dict-popup"
          ref={popupRef}
          style={{
            position: 'fixed',
            left: `${quickDict.x}px`,
            top: `${quickDict.y}px`,
            width: '340px',
            maxWidth: 'calc(100vw - 24px)',
            zIndex: 99999,
          }}
          className="bg-white rounded-2xl shadow-[0_20px_50px_rgba(0,0,0,0.22)] border border-slate-200 overflow-hidden animate-in fade-in zoom-in-95 duration-150"
        >
          <div className="bg-gradient-to-r from-[#005683] to-[#0284c7] text-white px-3.5 py-2 flex items-center justify-between gap-2">
            <div className="flex items-center gap-1.5 min-w-0">
              <span className="text-sm shrink-0">📖</span>
              <span className="font-bold text-[13px] truncate">
                Tra nhanh: <span className="text-amber-200 underline">{quickDict.word}</span>
              </span>
            </div>
            <div className="flex items-center gap-1.5 shrink-0">
              <button
                type="button"
                onClick={() => {
                  setStandaloneOpen(true);
                  setQuickDict(null);
                }}
                className="text-[11px] font-semibold bg-white/15 hover:bg-white/25 text-white px-2 py-0.5 rounded-md transition-colors cursor-pointer"
                title="Mở bảng từ điển đầy đủ"
              >
                Từ điển lớn ↗
              </button>
              <button
                type="button"
                onClick={() => setQuickDict(null)}
                className="w-6 h-6 rounded-full hover:bg-white/20 flex items-center justify-center text-white font-bold text-sm transition-colors cursor-pointer"
                title="Đóng (Esc)"
              >
                ✕
              </button>
            </div>
          </div>

          <div className="bg-white w-full h-[225px]">
            <iframe
              key={quickDict.word}
              src={`https://dic.tienganh123.com/fast_dict.php?word=${encodeURIComponent(quickDict.word)}&dict=ev_ve&m=yes`}
              className="w-full h-full border-0"
              title={`Tra từ: ${quickDict.word}`}
            />
          </div>
        </div>
      )}

      {/* MODAL TỪ ĐIỂN RIÊNG BIỆT (STANDALONE DICTIONARY - DIC.TIENGANH123.COM/V2/) */}
      {standaloneOpen && (
        <div
          id="tony-standalone-dict-modal"
          className="fixed inset-0 z-[99998] bg-slate-900/65 backdrop-blur-xs flex items-center justify-center p-3 sm:p-6 animate-in fade-in duration-150"
          onClick={() => setStandaloneOpen(false)}
        >
          <div
            className="bg-white rounded-2xl shadow-2xl border border-slate-200 w-full max-w-[920px] h-[82vh] max-h-[720px] flex flex-col overflow-hidden animate-in zoom-in-95 duration-150"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="bg-gradient-to-r from-[#005683] to-[#0284c7] text-white px-5 py-3 flex items-center justify-between gap-4 shrink-0">
              <div className="flex items-center gap-2.5 min-w-0">
                <span className="text-xl">📖</span>
                <div>
                  <h3 className="font-extrabold text-[15px] sm:text-base leading-tight">
                    Từ điển Anh - Việt / Việt - Anh / Đồng nghĩa
                  </h3>
                  <p className="text-[11px] text-sky-100 hidden sm:block">
                    Mẹo: Click đúp chuột vào bất kỳ từ nào trong Bài giảng hoặc Phần chữa bài để tra nhanh tại chỗ
                  </p>
                </div>
              </div>
              <button
                type="button"
                onClick={() => setStandaloneOpen(false)}
                className="w-8 h-8 rounded-full bg-white/15 hover:bg-rose-500 text-white font-bold flex items-center justify-center transition-colors cursor-pointer shrink-0"
                title="Đóng (Esc)"
              >
                ✕
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
