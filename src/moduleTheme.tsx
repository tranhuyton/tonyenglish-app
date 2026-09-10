import React, { useState } from 'react';

export interface ModuleColorPreset {
  id: string;
  name: string;
  bg: string;
  text: string;
  border: string;
}

export const MODULE_COLOR_PRESETS: ModuleColorPreset[] = [
  {
    id: 'default',
    name: 'Mặc định (Xám nhạt)',
    bg: '#f8fafc',
    text: '#1e293b',
    border: '#e2e8f0',
  },
  {
    id: 'biology',
    name: 'Xanh lá nhạt (Biology)',
    bg: '#dcfce7',
    text: '#15803d',
    border: '#bbf7d0',
  },
  {
    id: 'chemistry',
    name: 'Đỏ nhạt (Chemistry)',
    bg: '#fee2e2',
    text: '#b91c1c',
    border: '#fecaca',
  },
  {
    id: 'physics',
    name: 'Tím nhạt (Physics)',
    bg: '#f3e8ff',
    text: '#7e22ce',
    border: '#e9d5ff',
  },
  {
    id: 'sky',
    name: 'Xanh dương nhạt',
    bg: '#e0f2fe',
    text: '#0369a1',
    border: '#bae6fd',
  },
  {
    id: 'amber',
    name: 'Vàng cam nhạt',
    bg: '#fef3c7',
    text: '#b45309',
    border: '#fde68a',
  },
  {
    id: 'pink',
    name: 'Hồng nhạt',
    bg: '#fce7f3',
    text: '#be185d',
    border: '#fbcfe8',
  },
  {
    id: 'teal',
    name: 'Ngọc bích nhạt',
    bg: '#ccfbf1',
    text: '#0f766e',
    border: '#99f6e4',
  },
];

export interface ModuleTheme {
  cleanTitle: string;
  bg: string;
  text: string;
  border: string;
  hasColor: boolean;
  colorTag?: string;
}

/**
 * Parses raw module title and returns clean title and theme colors.
 * Supports:
 * 1. Database fields (mod.bg_color / mod.text_color if added)
 * 2. Embedded tag in title: [color:bg,text] or [color:bg]
 * 3. Keyword-based automatic fallbacks (biology -> green, chemistry -> red, physics -> purple)
 */
export function parseModuleTheme(rawTitle?: string, modObj?: any): ModuleTheme {
  const titleStr = rawTitle || (modObj?.title) || '';
  
  // 1. Extract [color:bg,text] or [color:bg]
  const colorTagRegex = /\[color:\s*([#a-zA-Z0-9]+)(?:,\s*([#a-zA-Z0-9]+))?\]/i;
  const match = titleStr.match(colorTagRegex);
  
  const cleanTitle = titleStr.replace(colorTagRegex, '').trim();
  
  let bg = modObj?.bg_color || '';
  let text = modObj?.text_color || '';
  let border = '';
  let hasExplicitColor = false;

  if (bg) {
    hasExplicitColor = true;
    if (!text) text = '#1e293b';
  } else if (match) {
    bg = match[1];
    text = match[2] || '#1e293b';
    hasExplicitColor = true;
  }

  // 2. Keyword fallback if no explicit color was defined
  if (!bg) {
    const lower = cleanTitle.toLowerCase();
    if (lower.includes('biology') || lower.includes('sinh học')) {
      bg = '#dcfce7';
      text = '#15803d';
      border = '#bbf7d0';
      hasExplicitColor = true;
    } else if (lower.includes('chemistry') || lower.includes('hóa học')) {
      bg = '#fee2e2';
      text = '#b91c1c';
      border = '#fecaca';
      hasExplicitColor = true;
    } else if (lower.includes('physics') || lower.includes('vật lý') || lower.includes('vật lí')) {
      bg = '#f3e8ff';
      text = '#7e22ce';
      border = '#e9d5ff';
      hasExplicitColor = true;
    }
  }

  // Generate a matching border if none set
  if (bg && !border) {
    const preset = MODULE_COLOR_PRESETS.find(p => p.bg.toLowerCase() === bg.toLowerCase());
    if (preset) {
      border = preset.border;
    } else {
      border = 'rgba(0, 0, 0, 0.08)';
    }
  }

  return {
    cleanTitle: cleanTitle || titleStr,
    bg: bg || '#f8fafc',
    text: text || '#1e293b',
    border: border || '#e2e8f0',
    hasColor: hasExplicitColor,
    colorTag: match ? match[0] : undefined,
  };
}

/**
 * Formats clean title with [color:bg,text] tag for persistence
 */
export function formatModuleTitleWithColor(cleanTitle: string, bg?: string, text?: string): string {
  const trimmed = (cleanTitle || '').trim();
  if (!bg || bg === '#f8fafc' || bg === 'default') {
    return trimmed;
  }
  const textColor = text || '#1e293b';
  return `${trimmed} [color:${bg},${textColor}]`;
}

/**
 * Interactive color selector component for Admin UI
 */
export const ModuleColorSelector: React.FC<{
  selectedBg?: string;
  selectedText?: string;
  onChange: (bg: string, text: string) => void;
}> = ({ selectedBg, selectedText, onChange }) => {
  const currentBg = selectedBg || '#f8fafc';
  const currentText = selectedText || '#1e293b';
  const [showCustom, setShowCustom] = useState(false);

  return (
    <div className="space-y-3">
      <div className="flex items-center justify-between">
        <label className="text-[12px] md:text-[13px] font-bold text-slate-700">
          Màu sắc Học Phần (Nền & Chữ):
        </label>
        <button
          type="button"
          onClick={() => setShowCustom(!showCustom)}
          className="text-[11px] font-bold text-blue-600 hover:text-blue-800 transition"
        >
          {showCustom ? '← Chọn theo mẫu' : '⚙️ Tùy chỉnh màu'}
        </button>
      </div>

      {!showCustom ? (
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
          {MODULE_COLOR_PRESETS.map((preset) => {
            const isSelected = currentBg.toLowerCase() === preset.bg.toLowerCase();
            return (
              <button
                key={preset.id}
                type="button"
                onClick={() => onChange(preset.bg, preset.text)}
                style={{
                  backgroundColor: preset.bg,
                  color: preset.text,
                  borderColor: isSelected ? preset.text : preset.border,
                }}
                className={`flex items-center gap-2 px-2.5 py-2 rounded-xl text-left border-2 transition-all text-[11px] md:text-xs font-bold shadow-sm ${
                  isSelected ? 'ring-2 ring-offset-1 ring-blue-500 scale-[1.02]' : 'hover:opacity-90'
                }`}
              >
                <span
                  className="w-3.5 h-3.5 rounded-full border border-black/10 shrink-0"
                  style={{ backgroundColor: preset.text }}
                />
                <span className="truncate">{preset.name}</span>
              </button>
            );
          })}
        </div>
      ) : (
        <div className="p-3 bg-slate-50 border border-slate-200 rounded-xl flex flex-wrap gap-4 items-center">
          <div className="flex items-center gap-2">
            <span className="text-xs font-semibold text-slate-600">Màu nền:</span>
            <input
              type="color"
              value={currentBg.startsWith('#') ? currentBg : '#f8fafc'}
              onChange={(e) => onChange(e.target.value, currentText)}
              className="w-8 h-8 rounded border border-slate-300 cursor-pointer"
            />
            <input
              type="text"
              value={currentBg}
              onChange={(e) => onChange(e.target.value, currentText)}
              className="w-20 px-2 py-1 text-xs border border-slate-300 rounded font-mono"
            />
          </div>
          <div className="flex items-center gap-2">
            <span className="text-xs font-semibold text-slate-600">Màu chữ:</span>
            <input
              type="color"
              value={currentText.startsWith('#') ? currentText : '#1e293b'}
              onChange={(e) => onChange(currentBg, e.target.value)}
              className="w-8 h-8 rounded border border-slate-300 cursor-pointer"
            />
            <input
              type="text"
              value={currentText}
              onChange={(e) => onChange(currentBg, e.target.value)}
              className="w-20 px-2 py-1 text-xs border border-slate-300 rounded font-mono"
            />
          </div>
        </div>
      )}

      {/* Live Preview Box */}
      <div className="pt-1">
        <span className="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Xem trước hiển thị:</span>
        <div
          style={{
            backgroundColor: currentBg,
            color: currentText,
            borderColor: showCustom
              ? 'rgba(0,0,0,0.1)'
              : MODULE_COLOR_PRESETS.find((p) => p.bg.toLowerCase() === currentBg.toLowerCase())?.border ||
                'rgba(0,0,0,0.1)',
          }}
          className="mt-1 px-4 py-2.5 rounded-xl border flex items-center justify-between font-bold text-xs md:text-sm shadow-sm transition-colors"
        >
          <div className="flex items-center gap-2 truncate">
            <span className="opacity-70 text-[11px] font-semibold">01</span>
            <span className="truncate">Tên Học Phần Xem Trước</span>
          </div>
          <span className="text-[10px] opacity-70">▼</span>
        </div>
      </div>
    </div>
  );
};
