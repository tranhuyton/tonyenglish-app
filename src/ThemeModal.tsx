import { useState } from 'react';

// ============================================================================
// SHARED THEME SYSTEM (Extracted from TaskBoard.tsx)
// Reusable across TaskBoard, AssignmentCalendar, StudentPortal, LectureViewer
// ============================================================================

export interface BoardTheme {
  id: string;
  name: string;
  boardBg: string;
  titleBg: string;
  titleText?: string;
  isDark?: boolean;
}

export const DEFAULT_BOARD_THEME: BoardTheme = {
  id: 'light-blue',
  name: 'Xanh nhạt (Mặc định)',
  boardBg: '#e0f2fe',
  titleBg: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
  titleText: '#ffffff'
};

export const BOARD_THEMES: BoardTheme[] = [
  {
    id: 'light-blue',
    name: 'Xanh nhạt (Mặc định)',
    boardBg: '#e0f2fe',
    titleBg: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'sky-soft',
    name: 'Xanh lam êm dịu',
    boardBg: '#dbeafe',
    titleBg: 'linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'trello-ocean',
    name: 'Xanh Trello kinh điển',
    boardBg: '#0079bf',
    titleBg: 'linear-gradient(135deg, #005a9c 0%, #004377 100%)',
    titleText: '#ffffff',
    isDark: true
  },
  {
    id: 'teal-mint',
    name: 'Xanh ngọc / Bạc hà',
    boardBg: '#ccfbf1',
    titleBg: 'linear-gradient(135deg, #0f766e 0%, #115e59 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'purple-lavender',
    name: 'Tím Lavender',
    boardBg: '#ede9fe',
    titleBg: 'linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'sunset-orange',
    name: 'Cam hoàng hôn',
    boardBg: '#ffedd5',
    titleBg: 'linear-gradient(135deg, #ea580c 0%, #c2410c 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'rose-pastel',
    name: 'Hồng phấn Pastel',
    boardBg: '#ffe4e6',
    titleBg: 'linear-gradient(135deg, #e11d48 0%, #be123c 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'emerald-leaf',
    name: 'Xanh lá tươi mát',
    boardBg: '#dcfce7',
    titleBg: 'linear-gradient(135deg, #16a34a 0%, #15803d 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'slate-modern',
    name: 'Xám hiện đại',
    boardBg: '#e2e8f0',
    titleBg: 'linear-gradient(135deg, #334155 0%, #1e293b 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'midnight-dark',
    name: 'Đêm đen huyền bí',
    boardBg: '#0f172a',
    titleBg: 'linear-gradient(135deg, #1e293b 0%, #0f172a 100%)',
    titleText: '#ffffff',
    isDark: true
  }
];

export function getDarkerShade(hex: string, percent = 30): string {
  let c = hex.replace('#', '');
  if (c.length === 3) c = c.split('').map(x => x + x).join('');
  const num = parseInt(c, 16);
  if (isNaN(num)) return '#0284c7';
  let r = (num >> 16);
  let g = ((num >> 8) & 0x00FF);
  let b = (num & 0x0000FF);
  r = Math.max(0, Math.min(255, Math.floor(r * (1 - percent / 100))));
  g = Math.max(0, Math.min(255, Math.floor(g * (1 - percent / 100))));
  b = Math.max(0, Math.min(255, Math.floor(b * (1 - percent / 100))));
  return `#${((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1)}`;
}

/** Load theme from localStorage for a given key prefix + userId with optional fallbackKey */
export function loadTheme(storageKey: string, fallbackKey?: string): BoardTheme {
  try {
    const saved = localStorage.getItem(storageKey);
    if (saved) return JSON.parse(saved);
    if (fallbackKey) {
      const fbSaved = localStorage.getItem(fallbackKey);
      if (fbSaved) return JSON.parse(fbSaved);
    }
  } catch (e) {}
  return DEFAULT_BOARD_THEME;
}

/** Save theme to localStorage with optional fallbackKey */
export function saveTheme(storageKey: string, theme: BoardTheme, fallbackKey?: string): void {
  try {
    localStorage.setItem(storageKey, JSON.stringify(theme));
    if (fallbackKey) {
      localStorage.setItem(fallbackKey, JSON.stringify(theme));
    }
  } catch (e) {}
}

/** Generate a custom theme from a hex color */
export function createCustomTheme(hex: string): BoardTheme {
  const darker = getDarkerShade(hex, 28);
  const darker2 = getDarkerShade(darker, 15);
  return {
    id: 'custom',
    name: 'Màu tùy chọn',
    boardBg: hex,
    titleBg: `linear-gradient(135deg, ${darker} 0%, ${darker2} 100%)`,
    titleText: '#ffffff'
  };
}

// ============================================================================
// REUSABLE THEME MODAL COMPONENT
// ============================================================================

export function BoardThemeModal({
  isOpen,
  currentTheme,
  onSelectTheme,
  onApplyCustomColor,
  onClose
}: {
  isOpen: boolean;
  currentTheme: BoardTheme;
  onSelectTheme: (theme: BoardTheme) => void;
  onApplyCustomColor: (hex: string) => void;
  onClose: () => void;
}) {
  const [customHex, setCustomHex] = useState(currentTheme.boardBg.startsWith('#') ? currentTheme.boardBg : '#e0f2fe');

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/45 backdrop-blur-xs p-4 animate-in fade-in duration-200">
      <div 
        className="fixed inset-0" 
        onClick={onClose}
      />
      <div className="relative bg-white rounded-3xl shadow-2xl border border-slate-200 w-full max-w-lg overflow-hidden flex flex-col z-10 animate-in zoom-in-95 duration-200">
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-100 flex items-center justify-between bg-slate-50/70">
          <div className="flex items-center gap-2.5">
            <span className="text-2xl">🎨</span>
            <div>
              <h3 className="font-bold text-slate-800 text-base">Đổi màu nền (Trello Style)</h3>
              <p className="text-slate-400 text-xs mt-0.5">Chọn màu nền yêu thích cho không gian làm việc</p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-white hover:bg-slate-100 border border-slate-200 text-slate-500 flex items-center justify-center font-bold text-sm transition-all cursor-pointer shadow-xs"
          >
            ✕
          </button>
        </div>

        {/* Body */}
        <div className="p-6 space-y-5 max-h-[70vh] overflow-y-auto custom-scrollbar">
          {/* Preset Palettes */}
          <div>
            <label className="text-xs font-bold text-slate-500 uppercase tracking-wider block mb-3">
              Bảng màu gợi ý
            </label>
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
              {BOARD_THEMES.map((theme) => {
                const isSelected = currentTheme.id === theme.id || currentTheme.boardBg === theme.boardBg;
                return (
                  <button
                    key={theme.id}
                    type="button"
                    onClick={() => {
                      onSelectTheme(theme);
                      onClose();
                    }}
                    className={`rounded-2xl p-2.5 border text-left transition-all cursor-pointer flex flex-col gap-2 group hover:scale-[1.02] hover:shadow-md ${
                      isSelected 
                        ? 'border-sky-500 ring-2 ring-sky-400/40 shadow-sm bg-sky-50/20' 
                        : 'border-slate-200 hover:border-slate-300 bg-white'
                    }`}
                  >
                    {/* Mini board preview */}
                    <div 
                      className="w-full h-14 rounded-xl border border-black/5 p-1.5 flex flex-col justify-between shadow-inner"
                      style={{ background: theme.boardBg }}
                    >
                      {/* Mini Title bar */}
                      <div 
                        className="h-2.5 w-full rounded-md shadow-2xs"
                        style={{ background: theme.titleBg }}
                      />
                      {/* Mini Columns */}
                      <div className="flex gap-1 h-6">
                        <div className="w-1/3 bg-white/90 rounded-sm shadow-2xs" />
                        <div className="w-1/3 bg-white/90 rounded-sm shadow-2xs" />
                        <div className="w-1/3 bg-white/90 rounded-sm shadow-2xs" />
                      </div>
                    </div>

                    <div className="flex items-center justify-between px-0.5">
                      <span className="font-bold text-xs text-slate-700 truncate group-hover:text-sky-600">
                        {theme.name}
                      </span>
                      {isSelected && (
                        <span className="text-[11px] font-black text-sky-600 shrink-0">✓</span>
                      )}
                    </div>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Custom Color Picker */}
          <div className="pt-4 border-t border-slate-100">
            <label className="text-xs font-bold text-slate-500 uppercase tracking-wider block mb-2.5">
              Hoặc chọn mã màu tùy thích
            </label>
            <div className="flex items-center gap-3">
              <input
                type="color"
                value={customHex}
                onChange={(e) => setCustomHex(e.target.value)}
                className="w-11 h-10 rounded-xl cursor-pointer border border-slate-200 p-0.5 bg-white shadow-xs shrink-0"
              />
              <input
                type="text"
                value={customHex}
                onChange={(e) => setCustomHex(e.target.value)}
                placeholder="#e0f2fe"
                className="flex-1 px-3.5 py-2 text-xs font-mono font-bold rounded-xl border border-slate-200 bg-slate-50 focus:bg-white focus:border-sky-500 outline-none uppercase"
              />
              <button
                type="button"
                onClick={() => {
                  onApplyCustomColor(customHex);
                  onClose();
                }}
                className="px-4 py-2 rounded-xl text-xs font-bold text-white bg-sky-600 hover:bg-sky-700 transition-all cursor-pointer shadow-xs active:scale-95 shrink-0"
              >
                Áp dụng
              </button>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-3.5 border-t border-slate-100 bg-slate-50/70 flex items-center justify-between">
          <button
            type="button"
            onClick={() => {
              onSelectTheme(DEFAULT_BOARD_THEME);
              onClose();
            }}
            className="text-xs font-bold text-slate-500 hover:text-sky-600 transition-colors cursor-pointer"
          >
            ↺ Khôi phục mặc định (Xanh nhạt)
          </button>
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-1.5 rounded-xl text-xs font-bold bg-white border border-slate-200 hover:bg-slate-100 text-slate-700 transition-all cursor-pointer shadow-xs"
          >
            Đóng
          </button>
        </div>
      </div>
    </div>
  );
}
