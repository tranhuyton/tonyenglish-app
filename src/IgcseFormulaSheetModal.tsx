import React from 'react';
import 'katex/dist/katex.min.css';
import { renderMathInHtml, IgcseMathCode, CalculatorPolicy } from './katexUtils';

interface IgcseFormulaSheetModalProps {
  isOpen: boolean;
  onClose: () => void;
  syllabus: IgcseMathCode;
  calculatorPolicy?: CalculatorPolicy;
  isEn?: boolean;
}

const FORMULA_0580 = [
  {
    group: 'Area & Mensuration (Đo lường 2D & 3D)',
    items: [
      { label: 'Area of a trapezium', tex: '\\(A = \\frac{1}{2}(a + b)h\\)' },
      { label: 'Curved surface area of cylinder', tex: '\\(A = 2\\pi r h\\)' },
      { label: 'Curved surface area of cone', tex: '\\(A = \\pi r l\\)' },
      { label: 'Surface area of sphere', tex: '\\(A = 4\\pi r^2\\)' },
      { label: 'Volume of prism', tex: '\\(V = A_{\\text{cross-section}} \\times l\\)' },
      { label: 'Volume of pyramid', tex: '\\(V = \\frac{1}{3} A_{\\text{base}} h\\)' },
      { label: 'Volume of cone', tex: '\\(V = \\frac{1}{3}\\pi r^2 h\\)' },
      { label: 'Volume of sphere', tex: '\\(V = \\frac{4}{3}\\pi r^3\\)' },
    ],
  },
  {
    group: 'Algebra & Financial Maths (Đại số)',
    items: [
      { label: 'Quadratic formula', tex: '\\(x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}\\)' },
      { label: 'Compound interest', tex: '\\(A = P\\left(1 + \\frac{r}{100}\\right)^n\\)' },
    ],
  },
  {
    group: 'Trigonometry (Lượng giác — Non-Right & Exact Values)',
    items: [
      { label: 'Sine rule', tex: '\\(\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C}\\)' },
      { label: 'Cosine rule', tex: '\\(a^2 = b^2 + c^2 - 2bc\\cos A\\)' },
      { label: 'Area of triangle', tex: '\\(A = \\frac{1}{2}ab\\sin C\\)' },
      { label: 'Exact values (Memorize for Paper 2 Non-Calc!)', tex: '\\(\\sin 30^\\circ = \\frac{1}{2},\\; \\sin 45^\\circ = \\frac{\\sqrt{2}}{2},\\; \\sin 60^\\circ = \\frac{\\sqrt{3}}{2},\\; \\tan 30^\\circ = \\frac{\\sqrt{3}}{3},\\; \\tan 60^\\circ = \\sqrt{3}\\)' },
    ],
  },
];

const FORMULA_0606 = [
  {
    group: 'Algebra, Series & Binomial (Đại số & Chuỗi)',
    items: [
      { label: 'Quadratic formula', tex: '\\(x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}\\)' },
      { label: 'Binomial theorem', tex: '\\((a+b)^n = a^n + \\binom{n}{1}a^{n-1}b + \\binom{n}{2}a^{n-2}b^2 + \\dots + b^n\\)' },
      { label: 'Arithmetic series', tex: '\\(u_n = a + (n-1)d,\\quad S_n = \\frac{n}{2}[2a + (n-1)d]\\)' },
      { label: 'Geometric series', tex: '\\(u_n = ar^{n-1},\\quad S_n = \\frac{a(1-r^n)}{1-r},\\quad S_\\infty = \\frac{a}{1-r}\\;(|r|<1)\\)' },
    ],
  },
  {
    group: 'Coordinate Geometry of the Circle (NEW 2025–2027) & Circular Measure',
    items: [
      { label: 'Circle equation (centre (a,b), radius r)', tex: '\\((x - a)^2 + (y - b)^2 = r^2\\)' },
      { label: 'Expanded form', tex: '\\(x^2 + y^2 + 2gx + 2fy + c = 0 \\implies \\text{centre } (-g,-f),\\; r = \\sqrt{g^2+f^2-c}\\)' },
      { label: 'Arc length & Sector area (θ in radians)', tex: '\\(s = r\\theta,\\qquad A = \\frac{1}{2}r^2\\theta\\)' },
    ],
  },
  {
    group: 'Trigonometry Identities (Lượng giác)',
    items: [
      { label: 'Pythagorean identities', tex: '\\(\\sin^2 A + \\cos^2 A = 1,\\quad \\sec^2 A = 1 + \\tan^2 A,\\quad \\csc^2 A = 1 + \\cot^2 A\\)' },
      { label: 'Sine & Cosine rules', tex: '\\(\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C},\\quad a^2 = b^2 + c^2 - 2bc\\cos A\\)' },
    ],
  },
  {
    group: 'Differentiation & Integration (Giải tích)',
    items: [
      { label: 'Product & Quotient rules', tex: '\\(\\frac{d}{dx}(uv) = u\\frac{dv}{dx} + v\\frac{du}{dx},\\quad \\frac{d}{dx}\\left(\\frac{u}{v}\\right) = \\frac{v\\frac{du}{dx} - u\\frac{dv}{dx}}{v^2}\\)' },
      { label: 'Standard derivatives', tex: '\\(\\frac{d}{dx}(\\sin ax)=a\\cos ax,\\; \\frac{d}{dx}(\\cos ax)=-a\\sin ax,\\; \\frac{d}{dx}(\\tan ax)=a\\sec^2 ax,\\; \\frac{d}{dx}(e^{ax})=ae^{ax},\\; \\frac{d}{dx}(\\ln x)=\\frac{1}{x}\\)' },
      { label: 'Standard integrals', tex: '\\(\\int (ax+b)^n\\,dx = \\frac{(ax+b)^{n+1}}{a(n+1)}+c,\\; \\int \\frac{1}{ax+b}\\,dx = \\frac{1}{a}\\ln|ax+b|+c,\\; \\int e^{ax+b}\\,dx = \\frac{1}{a}e^{ax+b}+c\\)' },
    ],
  },
];

export default function IgcseFormulaSheetModal({
  isOpen,
  onClose,
  syllabus,
  calculatorPolicy,
  isEn = false,
}: IgcseFormulaSheetModalProps) {
  if (!isOpen || !syllabus) return null;

  const groups = syllabus === '0606' ? FORMULA_0606 : FORMULA_0580;

  return (
    <div
      className="fixed inset-0 z-[100] bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-3 sm:p-6"
      onClick={onClose}
    >
      <div
        className="w-full max-w-3xl max-h-[88vh] bg-white rounded-2xl shadow-2xl border border-slate-200 flex flex-col overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="px-5 py-4 bg-gradient-to-r from-[#0a5482] to-[#1e3a8a] text-white flex items-center justify-between gap-3 shrink-0">
          <div>
            <div className="text-[11px] font-extrabold uppercase tracking-widest text-sky-200">
              Cambridge Official Reference • 2025–2027 Syllabus
            </div>
            <h3 className="text-lg font-black leading-tight mt-0.5">
              📐 {syllabus === '0606' ? 'IGCSE Additional Mathematics (0606)' : 'IGCSE Mathematics Extended (0580)'} — Formula Sheet
            </h3>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-white/15 hover:bg-white/25 text-white font-bold flex items-center justify-center cursor-pointer"
            title={isEn ? 'Close' : 'Đóng'}
          >
            ✕
          </button>
        </div>

        {calculatorPolicy && (
          <div
            className={`px-5 py-2.5 text-xs font-bold flex items-center gap-2 border-b ${
              calculatorPolicy === 'non-calculator'
                ? 'bg-rose-50 text-rose-800 border-rose-200'
                : 'bg-emerald-50 text-emerald-800 border-emerald-200'
            }`}
          >
            <span>{calculatorPolicy === 'non-calculator' ? '🚫' : '🧮'}</span>
            <span>
              {calculatorPolicy === 'non-calculator'
                ? isEn
                  ? 'NON-CALCULATOR PAPER: Electronic calculators MUST NOT be used. Leave answers in exact form (surds, π, fractions) unless stated otherwise.'
                  : 'ĐỀ KHÔNG DÙNG MÁY TÍNH (NON-CALCULATOR): Tuyệt đối không dùng máy tính cầm tay. Giữ đáp án ở dạng chính xác (căn thức, π, phân số tối giản).'
                : isEn
                  ? 'CALCULATOR ALLOWED: Give non-exact numerical answers correct to 3 significant figures, or 1 decimal place for angles in degrees.'
                  : 'ĐỀ ĐƯỢC DÙNG MÁY TÍNH (CALCULATOR): Làm tròn số thập phân đến 3 chữ số có nghĩa (3 s.f.), góc độ làm tròn 1 chữ số thập phân (1 d.p.).'}
            </span>
          </div>
        )}

        <div className="flex-1 overflow-y-auto p-5 space-y-5 bg-slate-50/70">
          {groups.map((grp) => (
            <div key={grp.group} className="bg-white rounded-xl border border-slate-200 p-4 shadow-2xs">
              <h4 className="font-black text-sm text-[#0a5482] uppercase tracking-wide mb-3 pb-2 border-b border-slate-100">
                {grp.group}
              </h4>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {grp.items.map((it) => (
                  <div
                    key={it.label}
                    className={`p-3 rounded-lg bg-slate-50 border border-slate-200/80 ${
                      it.tex.length > 75 ? 'sm:col-span-2' : ''
                    }`}
                  >
                    <div className="text-[11px] font-bold text-slate-500 mb-1">{it.label}</div>
                    <div
                      className="text-slate-900 text-sm overflow-x-auto"
                      dangerouslySetInnerHTML={{ __html: renderMathInHtml(it.tex) }}
                    />
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
