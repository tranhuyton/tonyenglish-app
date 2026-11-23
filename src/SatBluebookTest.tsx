import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import {
  Clock,
  Eye,
  EyeOff,
  Bookmark,
  ChevronLeft,
  ChevronRight,
  ChevronDown,
  ChevronUp,
  Highlighter,
  Maximize2,
  Minimize2,
  CheckCircle2,
  XCircle,
  AlertTriangle,
  Sparkles,
  Award,
  BarChart3,
  BookOpen,
  LogOut,
  RotateCcw,
  Trash2,
  Info,
  ShieldAlert,
  Target,
  Layers,
  Filter,
  SlidersHorizontal,
  Calculator,
  Compass,
  X,
  ExternalLink,
  Zap,
} from 'lucide-react';
import katex from 'katex';
import 'katex/dist/katex.min.css';
import { supabase } from './supabase';

// ============================================================================
// TYPES — DIGITAL SAT BLUEBOOK SCHEMA (R&W + MATH)
// ============================================================================

export type SatChoiceLabel = 'A' | 'B' | 'C' | 'D';

export interface SatOptionItem {
  label: SatChoiceLabel;
  text: string;
}

export interface SatOptionAnalysisItem {
  status: 'correct' | 'trap';
  trapTag?: string;
  reasonVi: string;
}

export interface SatQuestion {
  id: string;
  number: number;
  domain: string;
  skill: string;
  difficulty?: string;
  questionFormat?: 'mcq' | 'spr';
  stimulusHtml: string;
  questionHtml: string;
  options: SatOptionItem[];
  correctAnswer: string;
  acceptedAnswers?: string[];
  correctDisplay?: string;
  explanation?: {
    summaryVi: string;
    keyTakeaway?: string;
    desmosTipVi?: string;
    optionAnalysis?: Partial<Record<SatChoiceLabel, SatOptionAnalysisItem>>;
  };
}

export interface SatModule {
  id: string;
  title: string;
  subtitle?: string;
  timeLimitMinutes: number;
  directionsHtml?: string;
  questions: SatQuestion[];
}

export interface SatContentJson {
  schemaVersion?: number;
  mode: 'adaptive_mock' | 'drill';
  section?: string;
  basicInfo: {
    title: string;
    subtitle?: string;
    courseId?: string;
    difficultyBadge?: string;
    targetTimeMinutes?: number;
    routingThreshold?: number;
  };
  drillModule?: SatModule;
  module1?: SatModule;
  module2_hard?: SatModule;
  module2_lower?: SatModule;
}

interface HighlightNote {
  id: string;
  text: string;
  color: 'yellow' | 'cyan' | 'pink';
  note?: string;
}

interface SatBluebookTestProps {
  onBack: () => void;
  testData?: any;
  onFinish?: (res: any) => void;
}

// ============================================================================
// DIGITAL SAT R&W SCALED SCORE CONVERSION (200 - 800)
// Calibrated to College Board Bluebook Multistage Adaptive R&W curves
// ============================================================================

function computeSatRwScaledScore(
  m1Correct: number,
  m1Total: number,
  m2Correct: number,
  m2Total: number,
  route: 'hard' | 'lower'
): number {
  const totalCorrect = m1Correct + m2Correct;
  const totalQ = Math.max(1, m1Total + m2Total);
  const ratio = totalCorrect / totalQ;

  if (route === 'hard') {
    // Hard Module 2 route: realistic College Board 54-question curve (range ~520 - 800)
    const missed = Math.max(0, totalQ - totalCorrect);
    if (totalQ === 54) {
      const hardTopMap: Record<number, number> = {
        0: 800,
        1: 790,
        2: 780,
        3: 770,
        4: 760,
        5: 750,
        6: 740,
        7: 730,
        8: 720,
        9: 710,
        10: 700,
        11: 690,
        12: 680,
        13: 670,
        14: 660,
        15: 650,
        16: 640,
        17: 630,
        18: 620,
        19: 610,
        20: 600,
      };
      if (missed in hardTopMap) return hardTopMap[missed];
      const rawEst = 600 - (missed - 20) * 10;
      return Math.max(460, Math.min(800, Math.round(rawEst / 10) * 10));
    }
    const scaled = 480 + ratio * 320;
    return Math.max(460, Math.min(800, Math.round(scaled / 10) * 10));
  } else {
    // Lower/Standard Module 2 route: capped at 600 (College Board routing cap ~580-610)
    const scaled = 200 + ratio * 400;
    return Math.max(200, Math.min(600, Math.round(scaled / 10) * 10));
  }
}

// ============================================================================
// DIGITAL SAT MATH SCALED SCORE CONVERSION (200 - 800)
// Calibrated to College Board Bluebook 44-question Multistage Adaptive Math
// ============================================================================

function computeSatMathScaledScore(
  m1Correct: number,
  m1Total: number,
  m2Correct: number,
  m2Total: number,
  route: 'hard' | 'lower'
): number {
  const totalCorrect = m1Correct + m2Correct;
  const totalQ = Math.max(1, m1Total + m2Total);
  const ratio = totalCorrect / totalQ;

  if (route === 'hard') {
    const missed = Math.max(0, totalQ - totalCorrect);
    if (totalQ === 44) {
      const hardMap: Record<number, number> = {
        0: 800,
        1: 790,
        2: 780,
        3: 760,
        4: 750,
        5: 740,
        6: 730,
        7: 710,
        8: 700,
        9: 690,
        10: 680,
        11: 660,
        12: 650,
        13: 640,
        14: 620,
        15: 610,
        16: 600,
      };
      if (missed in hardMap) return hardMap[missed];
      const rawEst = 600 - (missed - 16) * 10;
      return Math.max(460, Math.min(800, Math.round(rawEst / 10) * 10));
    }
    const scaled = 480 + ratio * 320;
    return Math.max(460, Math.min(800, Math.round(scaled / 10) * 10));
  } else {
    const scaled = 200 + ratio * 400;
    return Math.max(200, Math.min(600, Math.round(scaled / 10) * 10));
  }
}

// ============================================================================
// MATH LATEX (KaTeX) & SPR GRID-IN GRADING HELPERS
// Uses \( ... \) for inline math and \[ ... \] for display math so currency $50
// in word problems never collides with LaTeX delimiters.
// ============================================================================

function renderMathHtml(rawHtml?: string): string {
  if (!rawHtml) return '';
  if (!rawHtml.includes('\\(') && !rawHtml.includes('\\[')) return rawHtml;
  let out = rawHtml.replace(/\\\[([\s\S]*?)\\\]/g, (_m, expr) => {
    try {
      return katex.renderToString(expr.trim(), { displayMode: true, throwOnError: false, strict: false });
    } catch {
      return expr;
    }
  });
  out = out.replace(/\\\(([\s\S]*?)\\\)/g, (_m, expr) => {
    try {
      return katex.renderToString(expr.trim(), { displayMode: false, throwOnError: false, strict: false });
    } catch {
      return expr;
    }
  });
  return out;
}

function parseSatNumericValue(raw: string): number | null {
  const s = (raw || '').trim().replace(/\s+/g, '');
  if (!s) return null;
  if (!/^-?(\d+(\.\d+)?|\.\d+)(\/(\d+(\.\d+)?|\.\d+))?$/.test(s)) return null;
  if (s.includes('/')) {
    const parts = s.split('/');
    if (parts.length !== 2) return null;
    const num = Number(parts[0]);
    const den = Number(parts[1]);
    if (!Number.isFinite(num) || !Number.isFinite(den) || den === 0) return null;
    return num / den;
  }
  const val = Number(s);
  return Number.isFinite(val) ? val : null;
}

function isSatQuestionCorrect(q: SatQuestion, userRaw?: string): boolean {
  if (!userRaw || !userRaw.trim()) return false;
  if (q.questionFormat === 'spr') {
    const cleanUser = userRaw.trim().replace(/\s+/g, '');
    const candidates =
      q.acceptedAnswers && q.acceptedAnswers.length > 0
        ? q.acceptedAnswers
        : [String(q.correctAnswer || '')];
    for (const acc of candidates) {
      const cleanAcc = String(acc).trim().replace(/\s+/g, '');
      if (cleanUser.toLowerCase() === cleanAcc.toLowerCase()) return true;
    }
    const uVal = parseSatNumericValue(cleanUser);
    if (uVal === null) return false;
    for (const acc of candidates) {
      const aVal = parseSatNumericValue(String(acc));
      if (aVal !== null) {
        const tol = 1e-4 * Math.max(1, Math.abs(aVal));
        if (Math.abs(uVal - aVal) <= tol) return true;
      }
    }
    return false;
  }
  return userRaw === q.correctAnswer;
}

function formatSprPreviewLatex(raw: string): string {
  const s = (raw || '').trim().replace(/\s+/g, '');
  if (!s) return '';
  const fracMatch = s.match(/^(-?)(\d+(?:\.\d+)?)\/(\d+(?:\.\d+)?)$/);
  if (fracMatch) {
    return `${fracMatch[1]}\\frac{${fracMatch[2]}}{${fracMatch[3]}}`;
  }
  return s;
}

const DEFAULT_RW_DIRECTIONS = `
  <p class="mb-2">The questions in this section address a number of important reading and writing skills. Each question includes one or more passages, which may include a table or graph. Read each passage and question carefully, and then choose the best answer to the question based on the passage(s).</p>
  <p>All questions in this section are multiple-choice with four answer choices. Each question has a single best answer.</p>
`;

const DEFAULT_MATH_DIRECTIONS = `
  <p class="mb-2">The questions in this section address a number of important math skills. Use of a calculator is permitted for all questions. A built-in Desmos Graphing Calculator and Reference Sheet are available in the top toolbar.</p>
  <p class="mb-2">Unless otherwise indicated, all variables and expressions represent real numbers, figures are drawn to scale, and all figures lie in a plane.</p>
  <p>For <b>Student-Produced Response</b> questions, enter a single exact integer, decimal, or fraction (e.g. <code>-3/4</code>, <code>0.75</code>, or <code>.75</code>). Do not enter mixed numbers.</p>
`;

const MATH_DOMAINS_SET = new Set([
  'Algebra',
  'Advanced Math',
  'Problem-Solving and Data Analysis',
  'Geometry and Trigonometry',
]);

const DOMAIN_ORDER = [
  'Standard English Conventions',
  'Expression of Ideas',
  'Craft and Structure',
  'Information and Ideas',
  'Algebra',
  'Advanced Math',
  'Problem-Solving and Data Analysis',
  'Geometry and Trigonometry',
];

function SatMathReferenceModal({ onClose }: { onClose: () => void }) {
  return (
    <div className="fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl border border-slate-300 shadow-2xl max-w-3xl w-full max-h-[88vh] flex flex-col overflow-hidden">
        <div className="px-5 py-3.5 bg-[#0f172a] text-white flex items-center justify-between shrink-0">
          <div className="flex items-center gap-2">
            <Compass className="w-4 h-4 text-sky-300" />
            <span className="font-black text-sm tracking-tight">Official Digital SAT Math Reference Sheet</span>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg hover:bg-white/15 text-slate-200 hover:text-white cursor-pointer"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        <div className="p-5 sm:p-6 overflow-y-auto space-y-5 text-slate-800 text-xs sm:text-sm">
          {/* 2D Geometry Grid */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <div className="rounded-xl border border-slate-200 p-3 text-center bg-slate-50/70">
              <svg viewBox="0 0 100 72" className="w-20 h-14 mx-auto mb-1">
                <circle cx="50" cy="36" r="28" fill="#eff6ff" stroke="#1e3a8a" strokeWidth="2" />
                <line x1="50" y1="36" x2="78" y2="36" stroke="#1e3a8a" strokeWidth="1.8" />
                <circle cx="50" cy="36" r="2.2" fill="#1e3a8a" />
                <text x="62" y="32" fontSize="11" fontStyle="italic" fill="#0f172a">r</text>
              </svg>
              <div className="font-bold text-slate-900">Circle</div>
              <div className="font-mono text-[12px] text-blue-900">A = πr² &nbsp;|&nbsp; C = 2πr</div>
            </div>

            <div className="rounded-xl border border-slate-200 p-3 text-center bg-slate-50/70">
              <svg viewBox="0 0 100 72" className="w-20 h-14 mx-auto mb-1">
                <rect x="16" y="16" width="68" height="40" fill="#eff6ff" stroke="#1e3a8a" strokeWidth="2" />
                <text x="48" y="68" fontSize="11" fontStyle="italic" fill="#0f172a">ℓ</text>
                <text x="87" y="40" fontSize="11" fontStyle="italic" fill="#0f172a">w</text>
              </svg>
              <div className="font-bold text-slate-900">Rectangle</div>
              <div className="font-mono text-[12px] text-blue-900">A = ℓw</div>
            </div>

            <div className="rounded-xl border border-slate-200 p-3 text-center bg-slate-50/70">
              <svg viewBox="0 0 100 72" className="w-20 h-14 mx-auto mb-1">
                <polygon points="15,58 85,58 42,14" fill="#eff6ff" stroke="#1e3a8a" strokeWidth="2" />
                <line x1="42" y1="14" x2="42" y2="58" stroke="#1e3a8a" strokeWidth="1.5" strokeDasharray="3 2" />
                <rect x="42" y="51" width="7" height="7" fill="none" stroke="#1e3a8a" strokeWidth="1.2" />
                <text x="45" y="42" fontSize="10" fontStyle="italic" fill="#0f172a">h</text>
                <text x="48" y="69" fontSize="10" fontStyle="italic" fill="#0f172a">b</text>
              </svg>
              <div className="font-bold text-slate-900">Triangle</div>
              <div className="font-mono text-[12px] text-blue-900">A = ½bh</div>
            </div>

            <div className="rounded-xl border border-slate-200 p-3 text-center bg-slate-50/70">
              <svg viewBox="0 0 100 72" className="w-20 h-14 mx-auto mb-1">
                <polygon points="18,58 82,58 18,16" fill="#eff6ff" stroke="#1e3a8a" strokeWidth="2" />
                <rect x="18" y="50" width="8" height="8" fill="none" stroke="#1e3a8a" strokeWidth="1.4" />
                <text x="8" y="40" fontSize="11" fontStyle="italic" fill="#0f172a">a</text>
                <text x="48" y="69" fontSize="11" fontStyle="italic" fill="#0f172a">b</text>
                <text x="53" y="34" fontSize="11" fontStyle="italic" fill="#0f172a">c</text>
              </svg>
              <div className="font-bold text-slate-900">Pythagorean</div>
              <div className="font-mono text-[12px] text-blue-900">c² = a² + b²</div>
            </div>
          </div>

          {/* Special Right Triangles */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div className="rounded-xl border border-indigo-200 bg-indigo-50/50 p-3.5 flex items-center gap-4">
              <svg viewBox="0 0 120 76" className="w-28 h-16 shrink-0">
                <polygon points="18,62 102,62 18,14" fill="#ffffff" stroke="#3730a3" strokeWidth="2" />
                <rect x="18" y="54" width="8" height="8" fill="none" stroke="#3730a3" strokeWidth="1.3" />
                <text x="6" y="41" fontSize="10" fontStyle="italic" fill="#1e1b4b">x</text>
                <text x="48" y="73" fontSize="10" fontStyle="italic" fill="#1e1b4b">x√3</text>
                <text x="62" y="33" fontSize="10" fontStyle="italic" fill="#1e1b4b">2x</text>
                <text x="21" y="29" fontSize="8.5" fill="#4338ca">60°</text>
                <text x="77" y="59" fontSize="8.5" fill="#4338ca">30°</text>
              </svg>
              <div>
                <div className="font-black text-indigo-950">30°–60°–90° Special Right</div>
                <div className="text-xs text-slate-700 mt-1">
                  Tỉ lệ 3 cạnh: <b>x : x√3 : 2x</b> (đối diện 30° : 60° : 90°).
                </div>
              </div>
            </div>

            <div className="rounded-xl border border-indigo-200 bg-indigo-50/50 p-3.5 flex items-center gap-4">
              <svg viewBox="0 0 100 76" className="w-24 h-16 shrink-0">
                <polygon points="20,62 76,62 20,10" fill="#ffffff" stroke="#3730a3" strokeWidth="2" />
                <rect x="20" y="54" width="8" height="8" fill="none" stroke="#3730a3" strokeWidth="1.3" />
                <text x="9" y="40" fontSize="10" fontStyle="italic" fill="#1e1b4b">s</text>
                <text x="45" y="73" fontSize="10" fontStyle="italic" fill="#1e1b4b">s</text>
                <text x="51" y="33" fontSize="10" fontStyle="italic" fill="#1e1b4b">s√2</text>
                <text x="23" y="27" fontSize="8.5" fill="#4338ca">45°</text>
                <text x="57" y="59" fontSize="8.5" fill="#4338ca">45°</text>
              </svg>
              <div>
                <div className="font-black text-indigo-950">45°–45°–90° Special Right</div>
                <div className="text-xs text-slate-700 mt-1">
                  Tỉ lệ 3 cạnh: <b>s : s : s√2</b> (đường chéo hình vuông).
                </div>
              </div>
            </div>
          </div>

          {/* 3D Volumes */}
          <div className="grid grid-cols-2 sm:grid-cols-5 gap-2.5">
            {[
              { name: 'Rect. Prism', formula: 'V = ℓwh' },
              { name: 'Cylinder', formula: 'V = πr²h' },
              { name: 'Sphere', formula: 'V = (4/3)πr³' },
              { name: 'Cone', formula: 'V = (1/3)πr²h' },
              { name: 'Pyramid', formula: 'V = (1/3)ℓwh' },
            ].map((s) => (
              <div key={s.name} className="rounded-xl border border-slate-200 bg-slate-50 p-3 text-center">
                <div className="text-[11px] font-bold text-slate-600">{s.name}</div>
                <div className="font-mono font-black text-xs text-slate-900 mt-1">{s.formula}</div>
              </div>
            ))}
          </div>

          {/* Official Notes */}
          <div className="rounded-xl bg-blue-50 border border-blue-200 p-3.5 text-xs text-slate-700 space-y-1">
            <div>• The number of degrees of arc in a circle is <b>360</b>.</div>
            <div>• The number of radians of arc in a circle is <b>2π</b>.</div>
            <div>• The sum of the measures in degrees of the angles of a triangle is <b>180</b>.</div>
          </div>
        </div>
      </div>
    </div>
  );
}

const HIGHLIGHT_STYLES: Record<'yellow' | 'cyan' | 'pink', { bg: string; ring: string; label: string }> = {
  yellow: { bg: '#fef08a', ring: '#eab308', label: 'Vàng' },
  cyan: { bg: '#bae6fd', ring: '#0284c7', label: 'Xanh dương' },
  pink: { bg: '#fbcfe8', ring: '#db2777', label: 'Hồng' },
};

const formatTimer = (secs: number) => {
  const safe = Math.max(0, Math.floor(secs));
  const m = Math.floor(safe / 60);
  const s = safe % 60;
  return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
};

// ============================================================================
// MAIN COMPONENT
// ============================================================================

export default function SatBluebookTest({ onBack, testData, onFinish }: SatBluebookTestProps) {
  const safeTest = testData || {};
  const content: SatContentJson = useMemo(() => {
    let raw = safeTest?.content_json || safeTest;
    if (typeof raw === 'string') {
      try {
        raw = JSON.parse(raw);
      } catch {
        raw = {};
      }
    }
    return raw as SatContentJson;
  }, [safeTest]);

  const isAdaptiveMock = content?.mode === 'adaptive_mock';
  const testTitle = safeTest?.title || content?.basicInfo?.title || 'Digital SAT Practice';

  const isMathSection = useMemo(() => {
    const sec = (content?.section || '').toLowerCase();
    if (sec === 'math' || sec.includes('math')) return true;
    const sampleQs = content?.drillModule?.questions || content?.module1?.questions || [];
    return sampleQs.some((q) => MATH_DOMAINS_SET.has(q.domain));
  }, [content]);

  const routingThreshold = content?.basicInfo?.routingThreshold ?? (isMathSection ? 15 : 18);

  const isHistoryReview = Boolean(safeTest?.isReview);
  const pastDetails = safeTest?.past_details || safeTest?.details || {};

  // ---- PHASE STATE ----
  // intro -> testing -> check_work -> routing_transition -> testing (M2) -> summary | review
  type Phase = 'intro' | 'testing' | 'check_work' | 'routing_transition' | 'summary' | 'review';

  const initialRoute: 'hard' | 'lower' | 'drill' = useMemo(() => {
    if (!isAdaptiveMock) return 'drill';
    const savedRoute = safeTest?.past_routing || pastDetails?.routing;
    if (savedRoute === 'lower') return 'lower';
    return 'hard';
  }, [isAdaptiveMock, safeTest, pastDetails]);

  const [phase, setPhase] = useState<Phase>(isHistoryReview ? 'review' : 'intro');
  const [activeStage, setActiveStage] = useState<'drill' | 'm1' | 'm2_hard' | 'm2_lower'>(
    isAdaptiveMock ? 'm1' : 'drill'
  );
  const [m2Route, setM2Route] = useState<'hard' | 'lower' | 'drill'>(initialRoute);
  const [directHardMode, setDirectHardMode] = useState<boolean>(false);

  // ---- ANSWERS, FLAGS, ELIMINATIONS, HIGHLIGHTS ----
  const [answers, setAnswers] = useState<Record<string, string>>(() => {
    const past = safeTest?.past_answers || pastDetails?.userAnswers;
    return past && typeof past === 'object' ? { ...past } : {};
  });
  const [flagged, setFlagged] = useState<Record<string, boolean>>(() => {
    const pastFlags = pastDetails?.flagged;
    if (Array.isArray(pastFlags)) {
      const map: Record<string, boolean> = {};
      pastFlags.forEach((id: string) => {
        map[id] = true;
      });
      return map;
    }
    return {};
  });
  const [eliminated, setEliminated] = useState<Record<string, Record<string, boolean>>>({});
  const [eliminatorEnabled, setEliminatorEnabled] = useState<boolean>(false);

  // ---- MATH TOOLS (DESMOS GRAPHING CALCULATOR & REFERENCE SHEET) ----
  const [showCalculator, setShowCalculator] = useState<boolean>(false);
  const [hasOpenedCalculator, setHasOpenedCalculator] = useState<boolean>(false);
  const [calcExpanded, setCalcExpanded] = useState<boolean>(false);
  const [calcMode, setCalcMode] = useState<'sat' | 'standard'>('sat');
  const [showReference, setShowReference] = useState<boolean>(false);

  const toggleCalculator = () => {
    setHasOpenedCalculator(true);
    setShowCalculator((v) => !v);
  };

  // Per-question Highlights & Notes
  const [highlightsByQ, setHighlightsByQ] = useState<Record<string, HighlightNote[]>>({});
  const [selectionPopup, setSelectionPopup] = useState<{
    text: string;
    x: number;
    y: number;
  } | null>(null);
  const [pendingNoteText, setPendingNoteText] = useState<string>('');
  const [showNoteInput, setShowNoteInput] = useState<boolean>(false);
  const [showHighlightsDrawer, setShowHighlightsDrawer] = useState<boolean>(false);

  // ---- NAVIGATION & UI STATE ----
  const [currentIdx, setCurrentIdx] = useState<number>(0);
  const [showNavigator, setShowNavigator] = useState<boolean>(false);
  const [showDirections, setShowDirections] = useState<boolean>(false);
  const [hideTimer, setHideTimer] = useState<boolean>(false);
  const [isFullscreen, setIsFullscreen] = useState<boolean>(false);
  const [fontSize, setFontSize] = useState<'sm' | 'md' | 'lg'>('md');
  const [leftPanePct, setLeftPanePct] = useState<number>(50);
  const [isDraggingDivider, setIsDraggingDivider] = useState<boolean>(false);
  const [showExitConfirm, setShowExitConfirm] = useState<boolean>(false);

  // ---- REVIEW MODE FILTERS ----
  const [reviewFilter, setReviewFilter] = useState<'all' | 'incorrect' | 'flagged'>('all');
  const [reviewModuleFilter, setReviewModuleFilter] = useState<'all' | 'm1' | 'm2'>('all');
  const [reviewIdx, setReviewIdx] = useState<number>(0);

  // ---- TIMERS & PERSISTENCE ----
  const [secondsLeft, setSecondsLeft] = useState<number>(32 * 60);
  const [totalTimeSpentSecs, setTotalTimeSpentSecs] = useState<number>(0);
  const [hasSavedResult, setHasSavedResult] = useState<boolean>(isHistoryReview);
  const [isSavingResult, setIsSavingResult] = useState<boolean>(false);

  const stimulusRef = useRef<HTMLDivElement | null>(null);
  const workspaceRef = useRef<HTMLDivElement | null>(null);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  // Notify DictionaryWidget when entering/leaving review mode
  useEffect(() => {
    const isRev = phase === 'review' || phase === 'summary';
    window.dispatchEvent(new CustomEvent('tony-review-mode-change', { detail: isRev }));
    return () => {
      window.dispatchEvent(new CustomEvent('tony-review-mode-change', { detail: false }));
    };
  }, [phase]);

  // Active module during testing
  const currentModule: SatModule | null = useMemo(() => {
    if (!isAdaptiveMock) return content?.drillModule || content?.module1 || null;
    if (activeStage === 'm1') return content?.module1 || null;
    if (activeStage === 'm2_hard') return content?.module2_hard || null;
    if (activeStage === 'm2_lower') return content?.module2_lower || content?.module2_hard || null;
    return content?.module1 || null;
  }, [isAdaptiveMock, activeStage, content]);

  const currentQuestions: SatQuestion[] = currentModule?.questions || [];
  const activeQuestion: SatQuestion | null = currentQuestions[currentIdx] || null;

  // All completed questions for Summary & Review
  const completedQuestionList: Array<SatQuestion & { moduleTag: 'm1' | 'm2' | 'drill'; moduleLabel: string }> =
    useMemo(() => {
      if (!isAdaptiveMock) {
        const qs = content?.drillModule?.questions || content?.module1?.questions || [];
        return qs.map((q) => ({
          ...q,
          moduleTag: 'drill' as const,
          moduleLabel: content?.drillModule?.title || 'Skill Drill',
        }));
      }
      if (directHardMode) {
        const qs = content?.module2_hard?.questions || [];
        return qs.map((q) => ({
          ...q,
          moduleTag: 'm2' as const,
          moduleLabel: 'Module 2 (Hard Practice)',
        }));
      }
      const m1Qs = (content?.module1?.questions || []).map((q) => ({
        ...q,
        moduleTag: 'm1' as const,
        moduleLabel: 'Module 1',
      }));
      const m2Source =
        m2Route === 'lower'
          ? content?.module2_lower?.questions || []
          : content?.module2_hard?.questions || [];
      const m2Qs = m2Source.map((q) => ({
        ...q,
        moduleTag: 'm2' as const,
        moduleLabel: m2Route === 'lower' ? 'Module 2 (Standard)' : 'Module 2 (Hard)',
      }));
      return [...m1Qs, ...m2Qs];
    }, [isAdaptiveMock, directHardMode, m2Route, content]);

  // Filtered review questions
  const filteredReviewQuestions = useMemo(() => {
    return completedQuestionList.filter((q) => {
      if (reviewModuleFilter !== 'all' && q.moduleTag !== reviewModuleFilter) return false;
      if (reviewFilter === 'incorrect') {
        return !isSatQuestionCorrect(q, answers[q.id]);
      }
      if (reviewFilter === 'flagged') {
        return Boolean(flagged[q.id]);
      }
      return true;
    });
  }, [completedQuestionList, reviewModuleFilter, reviewFilter, answers, flagged]);

  const activeReviewQuestion =
    filteredReviewQuestions[Math.min(reviewIdx, Math.max(0, filteredReviewQuestions.length - 1))] || null;

  // ---- SCORING ANALYTICS ----
  const analytics = useMemo(() => {
    let totalCorrect = 0;
    let m1Correct = 0;
    let m1Total = 0;
    let m2Correct = 0;
    let m2Total = 0;

    const domainStats: Record<string, { correct: number; total: number }> = {};
    const skillStats: Record<string, { correct: number; total: number; domain: string }> = {};

    completedQuestionList.forEach((q) => {
      const isRight = isSatQuestionCorrect(q, answers[q.id]);
      if (isRight) totalCorrect++;

      if (q.moduleTag === 'm1') {
        m1Total++;
        if (isRight) m1Correct++;
      } else if (q.moduleTag === 'm2') {
        m2Total++;
        if (isRight) m2Correct++;
      }

      const dom = q.domain || 'General';
      if (!domainStats[dom]) domainStats[dom] = { correct: 0, total: 0 };
      domainStats[dom].total++;
      if (isRight) domainStats[dom].correct++;

      const sk = q.skill || 'General';
      if (!skillStats[sk]) skillStats[sk] = { correct: 0, total: 0, domain: dom };
      skillStats[sk].total++;
      if (isRight) skillStats[sk].correct++;
    });

    const totalQ = completedQuestionList.length;
    const accuracyPct = totalQ > 0 ? Math.round((totalCorrect / totalQ) * 100) : 0;

    let scaledScore: number | null = null;
    if (isAdaptiveMock && !directHardMode) {
      scaledScore = isMathSection
        ? computeSatMathScaledScore(
            m1Correct,
            m1Total,
            m2Correct,
            m2Total,
            m2Route === 'lower' ? 'lower' : 'hard'
          )
        : computeSatRwScaledScore(
            m1Correct,
            m1Total,
            m2Correct,
            m2Total,
            m2Route === 'lower' ? 'lower' : 'hard'
          );
    }

    return {
      totalCorrect,
      totalQ,
      accuracyPct,
      m1Correct,
      m1Total,
      m2Correct,
      m2Total,
      scaledScore,
      domainStats,
      skillStats,
    };
  }, [completedQuestionList, answers, isAdaptiveMock, directHardMode, m2Route, isMathSection]);

  // ---- TIMER TICK ----
  useEffect(() => {
    if (phase !== 'testing' && phase !== 'check_work') {
      if (timerRef.current) {
        clearInterval(timerRef.current);
        timerRef.current = null;
      }
      return;
    }

    timerRef.current = setInterval(() => {
      setTotalTimeSpentSecs((prev) => prev + 1);
      setSecondsLeft((prev) => {
        if (prev <= 1) {
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => {
      if (timerRef.current) {
        clearInterval(timerRef.current);
        timerRef.current = null;
      }
    };
  }, [phase]);

  // Auto-advance when timer hits 0 during active module
  const handleSubmitCurrentModuleRef = useRef<() => void>(() => {});

  useEffect(() => {
    if ((phase === 'testing' || phase === 'check_work') && secondsLeft === 0) {
      handleSubmitCurrentModuleRef.current();
    }
  }, [secondsLeft, phase]);

  // ---- FULLSCREEN SYNC ----
  useEffect(() => {
    const onFsChange = () => setIsFullscreen(Boolean(document.fullscreenElement));
    document.addEventListener('fullscreenchange', onFsChange);
    return () => document.removeEventListener('fullscreenchange', onFsChange);
  }, []);

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen?.().catch(() => {});
    } else {
      document.exitFullscreen?.().catch(() => {});
    }
  };

  // ---- RESIZABLE DIVIDER ----
  useEffect(() => {
    if (!isDraggingDivider) return;
    const handleMove = (e: MouseEvent) => {
      if (!workspaceRef.current) return;
      const rect = workspaceRef.current.getBoundingClientRect();
      const pct = ((e.clientX - rect.left) / rect.width) * 100;
      setLeftPanePct(Math.max(30, Math.min(70, pct)));
    };
    const handleUp = () => setIsDraggingDivider(false);
    window.addEventListener('mousemove', handleMove);
    window.addEventListener('mouseup', handleUp);
    return () => {
      window.removeEventListener('mousemove', handleMove);
      window.removeEventListener('mouseup', handleUp);
    };
  }, [isDraggingDivider]);

  // ---- KEYBOARD SHORTCUTS DURING TESTING ----
  useEffect(() => {
    if (phase !== 'testing' || showNoteInput || showExitConfirm) return;
    const onKeyDown = (e: KeyboardEvent) => {
      const tag = (e.target as HTMLElement)?.tagName;
      if (tag === 'INPUT' || tag === 'TEXTAREA') return;
      if (!activeQuestion) return;

      if (e.key === 'ArrowRight') {
        e.preventDefault();
        if (currentIdx < currentQuestions.length - 1) setCurrentIdx((i) => i + 1);
        else setPhase('check_work');
      } else if (e.key === 'ArrowLeft') {
        e.preventDefault();
        if (currentIdx > 0) setCurrentIdx((i) => i - 1);
      } else if (e.key.toLowerCase() === 'f') {
        setFlagged((prev) => ({ ...prev, [activeQuestion.id]: !prev[activeQuestion.id] }));
      } else if (activeQuestion.questionFormat !== 'spr') {
        const keyMap: Record<string, SatChoiceLabel> = {
          '1': 'A',
          '2': 'B',
          '3': 'C',
          '4': 'D',
          a: 'A',
          b: 'B',
          c: 'C',
          d: 'D',
        };
        const choice = keyMap[e.key.toLowerCase()];
        if (choice) {
          handleSelectOption(activeQuestion.id, choice);
        }
      }
    };
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [phase, showNoteInput, showExitConfirm, activeQuestion, currentIdx, currentQuestions.length]);

  // ---- START TEST HANDLERS ----
  const startTest = (jumpToHardM2: boolean = false) => {
    setAnswers({});
    setFlagged({});
    setEliminated({});
    setHighlightsByQ({});
    setTotalTimeSpentSecs(0);
    setHasSavedResult(false);
    setCurrentIdx(0);

    if (!isAdaptiveMock) {
      setDirectHardMode(false);
      setActiveStage('drill');
      setM2Route('drill');
      const mins = content?.drillModule?.timeLimitMinutes || content?.basicInfo?.targetTimeMinutes || 20;
      setSecondsLeft(mins * 60);
      setPhase('testing');
      return;
    }

    if (jumpToHardM2 && content?.module2_hard) {
      setDirectHardMode(true);
      setActiveStage('m2_hard');
      setM2Route('hard');
      setSecondsLeft((content.module2_hard.timeLimitMinutes || (isMathSection ? 35 : 32)) * 60);
      setPhase('testing');
      return;
    }

    setDirectHardMode(false);
    setActiveStage('m1');
    setM2Route('hard');
    setSecondsLeft((content?.module1?.timeLimitMinutes || (isMathSection ? 35 : 32)) * 60);
    setPhase('testing');
  };

  // ---- SELECT & ELIMINATE ----
  const handleSprChange = (qId: string, val: string) => {
    setAnswers((prev) => {
      if (!val) {
        const copy = { ...prev };
        delete copy[qId];
        return copy;
      }
      return { ...prev, [qId]: val };
    });
  };
  const handleSelectOption = (qId: string, label: SatChoiceLabel) => {
    setAnswers((prev) => ({ ...prev, [qId]: label }));
    // Un-eliminate if the user selects it
    setEliminated((prev) => {
      if (!prev[qId]?.[label]) return prev;
      return {
        ...prev,
        [qId]: { ...prev[qId], [label]: false },
      };
    });
  };

  const toggleEliminateOption = (qId: string, label: SatChoiceLabel) => {
    setEliminated((prev) => {
      const nextVal = !prev[qId]?.[label];
      // If eliminating the currently selected answer, deselect it
      if (nextVal && answers[qId] === label) {
        setAnswers((ansPrev) => {
          const copy = { ...ansPrev };
          delete copy[qId];
          return copy;
        });
      }
      return {
        ...prev,
        [qId]: { ...(prev[qId] || {}), [label]: nextVal },
      };
    });
  };

  // ---- STIMULUS HIGHLIGHT & ANNOTATE ----
  const handleStimulusMouseUp = () => {
    if (phase !== 'testing') return;
    const sel = window.getSelection();
    if (!sel || sel.isCollapsed) {
      setSelectionPopup(null);
      setShowNoteInput(false);
      return;
    }
    const text = sel.toString().trim();
    if (text.length < 2 || text.length > 400) {
      setSelectionPopup(null);
      return;
    }
    const range = sel.getRangeAt(0);
    if (stimulusRef.current && !stimulusRef.current.contains(range.commonAncestorContainer)) {
      return;
    }
    const rect = range.getBoundingClientRect();
    setSelectionPopup({
      text,
      x: Math.max(130, Math.min(window.innerWidth - 150, rect.left + rect.width / 2)),
      y: Math.max(70, rect.top - 10),
    });
    setPendingNoteText('');
    setShowNoteInput(false);
  };

  const applyHighlight = (color: 'yellow' | 'cyan' | 'pink', note?: string) => {
    if (!selectionPopup || !activeQuestion) return;
    const qId = activeQuestion.id;
    const newItem: HighlightNote = {
      id: `hl_${Date.now()}_${Math.random().toString(36).slice(2, 6)}`,
      text: selectionPopup.text,
      color,
      note: note?.trim() || undefined,
    };
    setHighlightsByQ((prev) => ({
      ...prev,
      [qId]: [...(prev[qId] || []), newItem],
    }));
    window.getSelection()?.removeAllRanges();
    setSelectionPopup(null);
    setShowNoteInput(false);
    setPendingNoteText('');
  };

  const removeHighlight = (qId: string, hlId: string) => {
    setHighlightsByQ((prev) => ({
      ...prev,
      [qId]: (prev[qId] || []).filter((h) => h.id !== hlId),
    }));
  };

  const renderHighlightedStimulusHtml = useCallback((html: string, qId: string) => {
    const list = highlightsByQ[qId];
    let out = html || '';
    if (list && list.length > 0) {
      list.forEach((item) => {
        const escaped = item.text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        const bg = HIGHLIGHT_STYLES[item.color].bg;
        const titleAttr = item.note ? ` title="Note: ${item.note.replace(/"/g, '&quot;')}"` : '';
        // Replace first plain-text occurrence safely outside HTML tags
        const parts = out.split(/(<[^>]+>)/g);
        let replaced = false;
        for (let i = 0; i < parts.length; i++) {
          if (parts[i].startsWith('<')) continue;
          if (!replaced && new RegExp(escaped).test(parts[i])) {
            parts[i] = parts[i].replace(
              new RegExp(escaped),
              `<mark style="background:${bg}; padding:1px 2px; border-radius:3px; color:#0f172a;"${titleAttr}>$&</mark>`
            );
            replaced = true;
          }
        }
        out = parts.join('');
      });
    }
    return renderMathHtml(out);
  }, [highlightsByQ]);

  // ---- SAVE RESULT TO SUPABASE ----
  const saveResultToSupabase = useCallback(
    async (finalRoute: 'hard' | 'lower' | 'drill') => {
      if (hasSavedResult || isHistoryReview) return;
      setIsSavingResult(true);
      try {
        const { data: userData } = await supabase.auth.getUser();
        const user = userData?.user;

        // Recompute accurately with finalRoute
        const m1Qs = content?.module1?.questions || [];
        const m2Qs =
          finalRoute === 'lower'
            ? content?.module2_lower?.questions || []
            : content?.module2_hard?.questions || [];
        const list = !isAdaptiveMock
          ? content?.drillModule?.questions || content?.module1?.questions || []
          : directHardMode
          ? content?.module2_hard?.questions || []
          : [...m1Qs, ...m2Qs];

        let rawCorrect = 0;
        let m1Correct = 0;
        let m2Correct = 0;
        const domainStats: Record<string, { correct: number; total: number }> = {};
        const skillStats: Record<string, { correct: number; total: number }> = {};

        list.forEach((q) => {
          const ok = isSatQuestionCorrect(q, answers[q.id]);
          if (ok) rawCorrect++;
          if (isAdaptiveMock && !directHardMode) {
            if (m1Qs.some((m) => m.id === q.id)) {
              if (ok) m1Correct++;
            } else if (ok) {
              m2Correct++;
            }
          }
          const d = q.domain || 'General';
          if (!domainStats[d]) domainStats[d] = { correct: 0, total: 0 };
          domainStats[d].total++;
          if (ok) domainStats[d].correct++;

          const s = q.skill || 'General';
          if (!skillStats[s]) skillStats[s] = { correct: 0, total: 0 };
          skillStats[s].total++;
          if (ok) skillStats[s].correct++;
        });

        const totalQ = list.length;
        const scaled =
          isAdaptiveMock && !directHardMode
            ? isMathSection
              ? computeSatMathScaledScore(
                  m1Correct,
                  m1Qs.length,
                  m2Correct,
                  m2Qs.length,
                  finalRoute === 'lower' ? 'lower' : 'hard'
                )
              : computeSatRwScaledScore(
                  m1Correct,
                  m1Qs.length,
                  m2Correct,
                  m2Qs.length,
                  finalRoute === 'lower' ? 'lower' : 'hard'
                )
            : null;

        const savedScore = scaled !== null ? scaled : rawCorrect;
        const savedTotal = scaled !== null ? 800 : totalQ;

        if (user) {
          await supabase.from('test_results').insert([
            {
              user_id: user.id,
              course_id: safeTest?.course_id || content?.basicInfo?.courseId || null,
              test_title: testTitle,
              test_type: safeTest?.test_type || 'SAT-Bluebook',
              score: savedScore,
              total_score: savedTotal,
              time_spent: totalTimeSpentSecs,
              details: {
                test_id: safeTest?.id,
                test_type: 'SAT-Bluebook',
                mode: isAdaptiveMock ? (directHardMode ? 'hard_practice' : 'adaptive_mock') : 'drill',
                routing: finalRoute,
                sat_scaled_score: scaled,
                raw_score: rawCorrect,
                raw_total: totalQ,
                userAnswers: answers,
                flagged: Object.keys(flagged).filter((k) => flagged[k]),
                domain_stats: domainStats,
                skill_stats: skillStats,
                type_stats: skillStats,
              },
            },
          ]);

          const isPassed = totalQ > 0 ? rawCorrect / totalQ >= 0.5 : false;
          if (isPassed && safeTest?.id) {
            await supabase
              .from('assignments')
              .update({ is_completed: true, updated_at: new Date().toISOString() })
              .eq('test_id', safeTest.id)
              .eq('user_id', user.id)
              .eq('task_type', 'test');
          }

          window.dispatchEvent(new CustomEvent('tony-refresh-lecture-progress'));

          await supabase.from('activity_logs').insert([
            {
              user_id: user.id,
              action_type: 'finish_test',
              details: {
                test_title: testTitle,
                score: savedScore,
                total: savedTotal,
              },
            },
          ]);
        }

        setHasSavedResult(true);
        if (onFinish) {
          onFinish({ score: savedScore, total: savedTotal, testTitle });
        }
      } catch (err) {
        console.error('Error saving SAT Bluebook result:', err);
      } finally {
        setIsSavingResult(false);
      }
    },
    [
      hasSavedResult,
      isHistoryReview,
      content,
      isAdaptiveMock,
      directHardMode,
      answers,
      flagged,
      safeTest,
      testTitle,
      totalTimeSpentSecs,
      onFinish,
      isMathSection,
    ]
  );

  // ---- SUBMIT CURRENT MODULE ----
  const handleSubmitCurrentModule = useCallback(() => {
    setShowNavigator(false);
    setSelectionPopup(null);

    if (isAdaptiveMock && activeStage === 'm1') {
      // Grade Module 1 to determine adaptive routing to Module 2 Hard vs Lower
      const m1Qs = content?.module1?.questions || [];
      let m1Score = 0;
      m1Qs.forEach((q) => {
        if (isSatQuestionCorrect(q, answers[q.id])) m1Score++;
      });
      const route: 'hard' | 'lower' = m1Score >= routingThreshold ? 'hard' : 'lower';
      setM2Route(route);
      setPhase('routing_transition');
      return;
    }

    // Final submission (either Drill finished, Direct Hard M2 finished, or Adaptive M2 finished)
    const finalRoute: 'hard' | 'lower' | 'drill' = isAdaptiveMock ? m2Route : 'drill';
    setPhase('summary');
    saveResultToSupabase(finalRoute);
  }, [isAdaptiveMock, activeStage, content, answers, routingThreshold, m2Route, saveResultToSupabase]);

  handleSubmitCurrentModuleRef.current = handleSubmitCurrentModule;

  const proceedToModule2 = () => {
    const nextStage = m2Route === 'lower' ? 'm2_lower' : 'm2_hard';
    const nextMod = m2Route === 'lower' ? content?.module2_lower || content?.module2_hard : content?.module2_hard;
    setActiveStage(nextStage);
    setCurrentIdx(0);
    setSecondsLeft((nextMod?.timeLimitMinutes || (isMathSection ? 35 : 32)) * 60);
    setPhase('testing');
  };

  const handleExit = () => {
    if (document.fullscreenElement) {
      document.exitFullscreen?.().catch(() => {});
    }
    onBack();
  };

  // Persistent Desmos Graphing Calculator + Official Reference Sheet Overlays
  const mathOverlays = isMathSection ? (
    <>
      {hasOpenedCalculator && (
        <div
          className={`${
            showCalculator ? 'fixed' : 'hidden'
          } z-50 bottom-20 right-4 bg-white rounded-2xl border-2 border-slate-300 shadow-2xl flex flex-col overflow-hidden transition-all ${
            calcExpanded
              ? 'w-[min(94vw,820px)] h-[min(78vh,640px)]'
              : 'w-[min(94vw,470px)] h-[min(72vh,540px)]'
          }`}
        >
          <div className="shrink-0 px-3.5 py-2 bg-[#0f172a] text-white flex items-center justify-between gap-2">
            <div className="flex items-center gap-2 min-w-0">
              <Calculator className="w-4 h-4 text-emerald-400 shrink-0" />
              <span className="text-xs font-black truncate">Desmos Graphing Calculator (SAT Bluebook)</span>
            </div>
            <div className="flex items-center gap-1.5 shrink-0">
              <button
                type="button"
                onClick={() => setCalcMode((m) => (m === 'sat' ? 'standard' : 'sat'))}
                className="px-2 py-0.5 rounded bg-white/10 hover:bg-white/20 text-[10px] font-bold text-sky-200 cursor-pointer"
                title="Đổi phiên bản Desmos (SAT Testing / Standard)"
              >
                {calcMode === 'sat' ? 'SAT Mode' : 'Full Mode'}
              </button>
              <a
                href={
                  calcMode === 'sat'
                    ? 'https://www.desmos.com/testing/cb-sat-ap/graphing'
                    : 'https://www.desmos.com/calculator'
                }
                target="_blank"
                rel="noreferrer"
                className="p-1 rounded hover:bg-white/15 text-slate-300 hover:text-white"
                title="Mở Desmos ở tab mới"
              >
                <ExternalLink className="w-3.5 h-3.5" />
              </a>
              <button
                type="button"
                onClick={() => setCalcExpanded((v) => !v)}
                className="p-1 rounded hover:bg-white/15 text-slate-300 hover:text-white cursor-pointer"
                title={calcExpanded ? 'Thu nhỏ' : 'Mở rộng'}
              >
                {calcExpanded ? <Minimize2 className="w-3.5 h-3.5" /> : <Maximize2 className="w-3.5 h-3.5" />}
              </button>
              <button
                type="button"
                onClick={() => setShowCalculator(false)}
                className="p-1 rounded hover:bg-rose-500/30 text-slate-300 hover:text-white cursor-pointer"
                title="Ẩn máy tính (vẫn giữ nguyên hàm đang vẽ)"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          </div>
          <iframe
            key={calcMode}
            src={
              calcMode === 'sat'
                ? 'https://www.desmos.com/testing/cb-sat-ap/graphing'
                : 'https://www.desmos.com/calculator'
            }
            title="SAT Desmos Graphing Calculator"
            className="flex-1 w-full border-0 bg-white"
            allow="clipboard-read; clipboard-write"
          />
        </div>
      )}
      {showReference && <SatMathReferenceModal onClose={() => setShowReference(false)} />}
    </>
  ) : null;

  // ============================================================================
  // RENDER: EMPTY / INVALID TEST FALLBACK
  // ============================================================================
  if (!content || (!content.drillModule && !content.module1)) {
    return (
      <div className="min-h-screen bg-slate-50 flex flex-col items-center justify-center p-6">
        <div className="bg-white rounded-2xl border border-slate-200 shadow-lg max-w-md w-full p-8 text-center">
          <AlertTriangle className="w-12 h-12 text-amber-500 mx-auto mb-3" />
          <h2 className="text-xl font-black text-slate-900 mb-2">Dữ liệu đề SAT chưa sẵn sàng</h2>
          <p className="text-slate-600 text-sm mb-6">
            Đề thi này chưa có cấu trúc câu hỏi Digital SAT hợp lệ (`content_json`). Vui lòng báo Thầy Tony kiểm tra lại.
          </p>
          <button
            onClick={handleExit}
            className="px-6 py-2.5 rounded-xl bg-[#0050b3] hover:bg-[#003d8a] text-white font-bold text-sm"
          >
            Quay lại
          </button>
        </div>
      </div>
    );
  }

  // ============================================================================
  // RENDER 1: INTRO / PRE-EXAM LAUNCH SCREEN (BLUEBOOK STYLE)
  // ============================================================================
  if (phase === 'intro') {
    const m1Len = content.module1?.questions?.length || (isMathSection ? 22 : 27);
    const qCount = isAdaptiveMock
      ? m1Len * 2
      : content.drillModule?.questions?.length || 0;
    const modTime = isAdaptiveMock
      ? content.module1?.timeLimitMinutes || (isMathSection ? 35 : 32)
      : content.drillModule?.timeLimitMinutes || content.basicInfo?.targetTimeMinutes || 20;

    return (
      <div className="min-h-screen bg-gradient-to-br from-[#f0f5ff] via-white to-[#eef2ff] flex flex-col">
        {/* Top Bluebook Brand Bar */}
        <header className="h-16 px-6 bg-white border-b border-slate-200 flex items-center justify-between shadow-sm">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-[#1e3a8a] text-white flex items-center justify-center font-black text-sm shadow">
              SAT
            </div>
            <div>
              <div className="text-sm font-black text-slate-900 tracking-tight">
                TonyEnglish Bluebook™ Simulator
              </div>
              <div className="text-[11px] font-semibold text-slate-500">
                {isMathSection
                  ? 'Digital SAT 1500+ • Math & Desmos Engine'
                  : 'Digital SAT 1500+ • Reading & Writing Engine'}
              </div>
            </div>
          </div>
          <button
            onClick={handleExit}
            className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-lg text-xs font-bold text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition"
          >
            <LogOut className="w-4 h-4" /> Thoát
          </button>
        </header>

        <main className="flex-1 flex items-center justify-center p-4 sm:p-8">
          <div className="max-w-2xl w-full bg-white rounded-3xl border border-slate-200/90 shadow-xl overflow-hidden">
            {/* Official Bluebook Banner */}
            <div className="bg-gradient-to-r from-[#0f172a] via-[#1e3a8a] to-[#0050b3] p-7 sm:p-8 text-white relative overflow-hidden">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/15 border border-white/25 text-xs font-bold tracking-wide uppercase mb-4">
                <Sparkles className="w-3.5 h-3.5 text-amber-300" />
                {isAdaptiveMock
                  ? isMathSection
                    ? 'Full-Length Adaptive Math Mock Test'
                    : 'Full-Length Adaptive Mock Test'
                  : 'Bluebook Skill Drill • Target 1500+'}
              </div>
              <h1 className="text-2xl sm:text-3xl font-black tracking-tight leading-tight">
                {testTitle}
              </h1>
              {content.basicInfo?.subtitle && (
                <p className="mt-2 text-blue-100 text-sm sm:text-base">{content.basicInfo.subtitle}</p>
              )}
            </div>

            {/* Specs Grid */}
            <div className="p-6 sm:p-8 space-y-6">
              <div className="grid grid-cols-3 gap-3 sm:gap-4">
                <div className="rounded-2xl bg-slate-50 border border-slate-200 p-4 text-center">
                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-500">Số câu hỏi</div>
                  <div className="mt-1 text-xl sm:text-2xl font-black text-slate-900">{qCount}</div>
                  <div className="text-[11px] text-slate-500">
                    {isAdaptiveMock ? `2 Modules × ${m1Len}` : 'Chuẩn Bluebook'}
                  </div>
                </div>
                <div className="rounded-2xl bg-slate-50 border border-slate-200 p-4 text-center">
                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-500">Thời gian</div>
                  <div className="mt-1 text-xl sm:text-2xl font-black text-[#1e3a8a]">
                    {isAdaptiveMock ? `${modTime}p × 2` : `${modTime} phút`}
                  </div>
                  <div className="text-[11px] text-slate-500">Đếm ngược chuẩn</div>
                </div>
                <div className="rounded-2xl bg-slate-50 border border-slate-200 p-4 text-center">
                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-500">Chế độ</div>
                  <div className="mt-1 text-base sm:text-lg font-black text-emerald-700 mt-1.5">
                    {isAdaptiveMock ? 'Adaptive' : '1500+ Drill'}
                  </div>
                  <div className="text-[11px] text-slate-500">
                    {isAdaptiveMock
                      ? 'Thang 200–800'
                      : isMathSection
                      ? 'MCQ + Grid-In'
                      : 'Trap Analysis'}
                  </div>
                </div>
              </div>

              {/* Bluebook Tools Briefing */}
              <div className="rounded-2xl bg-blue-50/70 border border-blue-200/80 p-4 sm:p-5 space-y-2.5">
                <div className="text-xs font-black uppercase tracking-wider text-[#1e3a8a] flex items-center gap-1.5">
                  <Info className="w-4 h-4" /> Công cụ mô phỏng chuẩn Bluebook đã tích hợp
                </div>
                <ul className="text-xs sm:text-sm text-slate-700 space-y-1.5 list-disc pl-5">
                  {isMathSection ? (
                    <>
                      <li>
                        <b>Máy tính đồ thị Desmos (SAT Edition):</b> Mở ngay trên thanh công cụ — giữ nguyên đồ thị &amp; bảng hồi quy khi chuyển câu.
                      </li>
                      <li>
                        <b>Reference Sheet chuẩn College Board:</b> Bảng công thức Hình học 2D, 3D &amp; Tam giác đặc biệt 30–60–90, 45–45–90 tra nhanh 1 chạm.
                      </li>
                      <li>
                        <b>Hỗ trợ cả Trắc nghiệm (MCQ) &amp; Tự điền số (SPR Grid-In):</b> Tự động nhận diện phân số (<code>-3/4</code>), số thập phân (<code>-0.75</code>) tương đương.
                      </li>
                    </>
                  ) : (
                    <>
                      <li>
                        <b>Highlight &amp; Ghi chú:</b> Bôi đen bất kỳ cụm từ nào trong đoạn văn bên trái để tô màu &amp; ghi chú ý chính.
                      </li>
                      <li>
                        <b>Option Eliminator (ABC):</b> Bật nút gạch loại trừ để gạch ngang đáp án bẫy y hệt khi thi thật.
                      </li>
                    </>
                  )}
                  <li>
                    <b>Mark for Review &amp; Question Navigator:</b> Gắn cờ câu khó và nhảy nhanh giữa các câu; phím tắt{' '}
                    <code className="px-1 py-0.5 bg-white border border-blue-200 rounded text-[11px] font-bold">A–D</code>,{' '}
                    <code className="px-1 py-0.5 bg-white border border-blue-200 rounded text-[11px] font-bold">←/→</code>,{' '}
                    <code className="px-1 py-0.5 bg-white border border-blue-200 rounded text-[11px] font-bold">F</code>.
                  </li>
                  {isAdaptiveMock && (
                    <li>
                      <b>Phân nhánh Thích ứng (Adaptive Routing):</b> Đạt từ <b>{routingThreshold}/{m1Len}</b> ở Module 1 để vào nhánh <b>Module 2 Hard (vùng 650–800)</b>.
                    </li>
                  )}
                </ul>
              </div>

              {/* Start Buttons */}
              <div className="flex flex-col sm:flex-row gap-3 pt-1">
                <button
                  onClick={() => startTest(false)}
                  className="flex-1 py-3.5 px-6 rounded-xl bg-[#0050b3] hover:bg-[#003d8a] text-white font-black text-sm sm:text-base shadow-lg shadow-blue-900/20 transition flex items-center justify-center gap-2 cursor-pointer"
                >
                  <span>{isAdaptiveMock ? 'Bắt đầu Thi Thử Adaptive (Module 1)' : 'Bắt đầu Làm Bài Luyện'}</span>
                  <ChevronRight className="w-5 h-5" />
                </button>
                {isAdaptiveMock && content.module2_hard && (
                  <button
                    onClick={() => startTest(true)}
                    className="py-3.5 px-5 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-300 font-extrabold text-xs sm:text-sm transition flex items-center justify-center gap-1.5 cursor-pointer"
                    title={`Chế độ luyện trực tiếp ${m1Len} câu Hard Module 2 cho mục tiêu 750–800`}
                  >
                    <Target className="w-4 h-4 text-amber-600" />
                    <span>Luyện thẳng Module 2 Hard</span>
                  </button>
                )}
              </div>
            </div>
          </div>
        </main>
      </div>
    );
  }

  // ============================================================================
  // RENDER 2: MODULE 1 -> MODULE 2 ADAPTIVE TRANSITION SCREEN
  // ============================================================================
  if (phase === 'routing_transition') {
    const m1Qs = content.module1?.questions || [];
    const m1Right = m1Qs.filter((q) => isSatQuestionCorrect(q, answers[q.id])).length;
    const defaultModLen = isMathSection ? 22 : 27;
    const defaultModMin = isMathSection ? 35 : 32;

    return (
      <div className="min-h-screen bg-[#f8fafc] flex flex-col items-center justify-center p-6">
        <div className="max-w-xl w-full bg-white rounded-3xl border border-slate-200 shadow-xl p-8 text-center space-y-5">
          <div className="w-16 h-16 rounded-2xl bg-[#1e3a8a] text-white flex items-center justify-center mx-auto shadow-lg">
            <Layers className="w-8 h-8" />
          </div>
          <div>
            <div className="text-xs font-black uppercase tracking-widest text-blue-600 mb-1">
              Module 1 Complete • Adaptive Engine
            </div>
            <h2 className="text-2xl font-black text-slate-900">Chuẩn bị bước vào Module 2</h2>
            <p className="text-sm text-slate-600 mt-2 leading-relaxed">
              Hệ thống đã ghi nhận bài làm <b>Module 1</b> của bạn và định tuyến bộ câu hỏi <b>Module 2</b> phù hợp theo cơ chế thi thích ứng chuẩn College Board Digital SAT.
            </p>
          </div>

          <div className="rounded-2xl bg-slate-50 border border-slate-200 p-4 flex items-center justify-around text-left">
            <div>
              <div className="text-[11px] font-bold uppercase text-slate-500">Module 2</div>
              <div className="text-lg font-black text-slate-900">
                {m2Route === 'hard'
                  ? content.module2_hard?.questions?.length || defaultModLen
                  : content.module2_lower?.questions?.length || defaultModLen}{' '}
                câu hỏi
              </div>
            </div>
            <div className="h-9 w-px bg-slate-200" />
            <div>
              <div className="text-[11px] font-bold uppercase text-slate-500">Thời gian</div>
              <div className="text-lg font-black text-[#1e3a8a]">
                {m2Route === 'hard'
                  ? content.module2_hard?.timeLimitMinutes || defaultModMin
                  : content.module2_lower?.timeLimitMinutes || defaultModMin}{' '}
                phút
              </div>
            </div>
            <div className="h-9 w-px bg-slate-200" />
            <div>
              <div className="text-[11px] font-bold uppercase text-slate-500">Trạng thái</div>
              <div
                className={`text-sm font-black px-2.5 py-0.5 rounded-full inline-block mt-0.5 ${
                  m2Route === 'hard'
                    ? 'bg-emerald-100 text-emerald-800'
                    : 'bg-amber-100 text-amber-800'
                }`}
              >
                {m2Route === 'hard' ? 'Hard Module 2 🔥' : 'Standard Module 2'}
              </div>
            </div>
          </div>

          <p className="text-xs text-slate-500">
            (Kết quả tạm tính Module 1: <b>{m1Right}/{m1Qs.length}</b> — ngưỡng vào Hard Module 2 là ≥ {routingThreshold}/{m1Qs.length})
          </p>

          <button
            onClick={proceedToModule2}
            className="w-full py-3.5 px-6 rounded-xl bg-[#0050b3] hover:bg-[#003d8a] text-white font-black text-base shadow-lg shadow-blue-900/20 transition flex items-center justify-center gap-2 cursor-pointer"
          >
            <span>Bắt đầu Module 2 ngay</span>
            <ChevronRight className="w-5 h-5" />
          </button>
        </div>
      </div>
    );
  }

  // ============================================================================
  // RENDER 3: SCORE REPORT SUMMARY DASHBOARD
  // ============================================================================
  if (phase === 'summary') {
    const avgSecPerQ =
      analytics.totalQ > 0 ? Math.round(totalTimeSpentSecs / analytics.totalQ) : 0;

    return (
      <div className="min-h-screen bg-[#f4f7fb] flex flex-col">
        <header className="h-16 px-4 sm:px-8 bg-white border-b border-slate-200 flex items-center justify-between sticky top-0 z-30 shadow-sm">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-[#1e3a8a] text-white flex items-center justify-center font-black text-xs">
              SAT
            </div>
            <div>
              <div className="text-sm font-black text-slate-900 line-clamp-1">{testTitle}</div>
              <div className="text-[11px] font-semibold text-slate-500">Official-Style Score Report</div>
            </div>
          </div>
          <div className="flex items-center gap-2.5">
            <button
              onClick={() => {
                setReviewFilter('all');
                setReviewModuleFilter('all');
                setReviewIdx(0);
                setPhase('review');
              }}
              className="px-4 py-2 rounded-xl bg-[#0050b3] hover:bg-[#003d8a] text-white font-bold text-xs sm:text-sm flex items-center gap-1.5 cursor-pointer"
            >
              <BookOpen className="w-4 h-4" /> Chữa bài chi tiết
            </button>
            <button
              onClick={handleExit}
              className="px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs sm:text-sm cursor-pointer"
            >
              Về danh sách
            </button>
          </div>
        </header>

        <main className="max-w-5xl w-full mx-auto p-4 sm:p-8 space-y-6">
          {/* Top Hero Score Card */}
          <div className="bg-gradient-to-br from-[#0f172a] via-[#1e3a8a] to-[#0050b3] rounded-3xl p-6 sm:p-8 text-white shadow-xl">
            <div className="flex flex-col md:flex-row items-center justify-between gap-6">
              <div className="space-y-2 text-center md:text-left">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/15 border border-white/25 text-xs font-bold uppercase tracking-wide">
                  <Award className="w-4 h-4 text-amber-300" />
                  {analytics.scaledScore !== null
                    ? m2Route === 'hard'
                      ? 'Adaptive Route: Hard Module 2 🔥'
                      : 'Adaptive Route: Standard Module 2'
                    : directHardMode
                    ? 'Hard Module 2 Practice Complete'
                    : 'Skill Drill Complete'}
                </div>
                <h1 className="text-2xl sm:text-3xl font-black">{testTitle}</h1>
                <p className="text-blue-100 text-sm max-w-xl">
                  {analytics.scaledScore !== null
                    ? analytics.scaledScore >= (isMathSection ? 780 : 750)
                      ? isMathSection
                        ? 'Xuất sắc! Phong độ Math của bạn đang ở ngưỡng 780–800 — sẵn sàng chinh phục SAT 1500+!'
                        : 'Xuất sắc! Phong độ Reading & Writing của bạn đang đạt chuẩn mục tiêu 1500+ (750–800 R&W).'
                      : analytics.scaledScore >= 700
                      ? isMathSection
                        ? 'Rất tốt! Bạn đã vượt mốc 700 Math — hãy mở Chữa bài chi tiết để luyện mẹo Desmos 10 giây và xử lý các câu Hard Module 2.'
                        : 'Rất tốt! Bạn đã vượt mốc 700 R&W — hãy mở Chữa bài chi tiết để xử lý nốt 4–7 bẫy Hard Module 2.'
                      : isMathSection
                      ? 'Hãy xem kỹ phân tích 4 Content Domains, lời giải đại số từng bước và mẹo Desmos để nâng tốc độ lên ngưỡng 750–800.'
                      : 'Hãy xem kỹ phân tích 4 Content Domains và bẫy đáp án từng câu để nâng tốc độ Grammar và độ chính xác Reading.'
                    : analytics.accuracyPct >= 85
                    ? 'Độ chính xác ấn tượng ở ngưỡng 1500+! Xem nhanh các câu sai/đánh dấu để khóa chắc tuyệt đối kỹ năng này.'
                    : 'Hãy bấm "Chữa bài chi tiết" để đọc lời giải chi tiết và phân tích bẫy cho từng câu chưa đúng nhé.'}
                </p>
                {isSavingResult && (
                  <div className="text-xs text-sky-200 animate-pulse">Đang lưu kết quả vào hồ sơ học tập...</div>
                )}
              </div>

              {/* Big Score Display */}
              <div className="shrink-0 bg-white/10 backdrop-blur-md border border-white/25 rounded-2xl px-8 py-5 text-center min-w-[200px]">
                {analytics.scaledScore !== null ? (
                  <>
                    <div className="text-[11px] font-bold uppercase tracking-widest text-blue-200">
                      {isMathSection ? 'Math Section Score' : 'Reading & Writing Score'}
                    </div>
                    <div className="text-5xl font-black tracking-tight mt-1 text-white">
                      {analytics.scaledScore}
                    </div>
                    <div className="text-xs font-semibold text-blue-200 mt-0.5">
                      trên thang 200 – 800
                    </div>
                  </>
                ) : (
                  <>
                    <div className="text-[11px] font-bold uppercase tracking-widest text-blue-200">
                      Độ chính xác
                    </div>
                    <div className="text-5xl font-black tracking-tight mt-1 text-white">
                      {analytics.totalCorrect}
                      <span className="text-2xl text-blue-200">/{analytics.totalQ}</span>
                    </div>
                    <div className="text-xs font-semibold text-emerald-300 mt-0.5">
                      {analytics.accuracyPct}% chính xác
                    </div>
                  </>
                )}
              </div>
            </div>

            {/* Secondary Metrics Strip */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-6 pt-6 border-t border-white/15">
              <div className="bg-white/10 rounded-xl px-4 py-3">
                <div className="text-[11px] text-blue-200 font-semibold">Câu đúng tổng</div>
                <div className="text-lg font-black">
                  {analytics.totalCorrect} / {analytics.totalQ} ({analytics.accuracyPct}%)
                </div>
              </div>
              {isAdaptiveMock && !directHardMode && (
                <>
                  <div className="bg-white/10 rounded-xl px-4 py-3">
                    <div className="text-[11px] text-blue-200 font-semibold">Module 1</div>
                    <div className="text-lg font-black">
                      {analytics.m1Correct} / {analytics.m1Total}
                    </div>
                  </div>
                  <div className="bg-white/10 rounded-xl px-4 py-3">
                    <div className="text-[11px] text-blue-200 font-semibold">
                      Module 2 ({m2Route === 'hard' ? 'Hard' : 'Standard'})
                    </div>
                    <div className="text-lg font-black">
                      {analytics.m2Correct} / {analytics.m2Total}
                    </div>
                  </div>
                </>
              )}
              <div className="bg-white/10 rounded-xl px-4 py-3">
                <div className="text-[11px] text-blue-200 font-semibold">Tốc độ trung bình</div>
                <div className="text-lg font-black">
                  {avgSecPerQ}s / câu
                  <span className="text-xs font-normal text-blue-200 ml-1">
                    (chuẩn ≤{isMathSection ? 95 : 71}s)
                  </span>
                </div>
              </div>
            </div>
          </div>

          {/* Domain & Skill Analytics */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* 4 Content Domains */}
            <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
              <h3 className="text-base font-black text-slate-900 flex items-center gap-2 mb-4">
                <BarChart3 className="w-5 h-5 text-[#0050b3]" /> Phân tích theo 4 Content Domains
              </h3>
              <div className="space-y-4">
                {Object.entries(analytics.domainStats)
                  .sort((a, b) => {
                    const ia = DOMAIN_ORDER.indexOf(a[0]);
                    const ib = DOMAIN_ORDER.indexOf(b[0]);
                    return (ia === -1 ? 99 : ia) - (ib === -1 ? 99 : ib);
                  })
                  .map(([domain, st]) => {
                    const pct = st.total > 0 ? Math.round((st.correct / st.total) * 100) : 0;
                    const barColor =
                      pct >= 85 ? 'bg-emerald-500' : pct >= 65 ? 'bg-amber-500' : 'bg-rose-500';
                    return (
                      <div key={domain}>
                        <div className="flex items-center justify-between text-sm mb-1.5">
                          <span className="font-bold text-slate-800">{domain}</span>
                          <span className="font-black text-slate-700">
                            {st.correct}/{st.total}{' '}
                            <span className="text-xs font-semibold text-slate-500">({pct}%)</span>
                          </span>
                        </div>
                        <div className="h-2.5 w-full rounded-full bg-slate-100 overflow-hidden">
                          <div
                            className={`h-full rounded-full transition-all duration-500 ${barColor}`}
                            style={{ width: `${pct}%` }}
                          />
                        </div>
                      </div>
                    );
                  })}
              </div>
            </div>

            {/* Granular Skill Breakdown */}
            <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
              <h3 className="text-base font-black text-slate-900 flex items-center gap-2 mb-4">
                <Target className="w-5 h-5 text-indigo-600" /> Chi tiết từng Kỹ năng (Skills)
              </h3>
              <div className="space-y-2.5 max-h-[300px] overflow-y-auto pr-1">
                {Object.entries(analytics.skillStats).map(([skill, st]) => {
                  const pct = st.total > 0 ? Math.round((st.correct / st.total) * 100) : 0;
                  return (
                    <div
                      key={skill}
                      className="flex items-center justify-between px-3.5 py-2.5 rounded-xl bg-slate-50 border border-slate-200/80"
                    >
                      <div>
                        <div className="text-sm font-bold text-slate-800">{skill}</div>
                        <div className="text-[11px] text-slate-500">{st.domain}</div>
                      </div>
                      <div
                        className={`px-2.5 py-1 rounded-lg text-xs font-black ${
                          pct >= 85
                            ? 'bg-emerald-100 text-emerald-800'
                            : pct >= 65
                            ? 'bg-amber-100 text-amber-800'
                            : 'bg-rose-100 text-rose-800'
                        }`}
                      >
                        {st.correct}/{st.total} ({pct}%)
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>

          {/* Action Footer */}
          <div className="flex flex-wrap items-center justify-center gap-3 pt-2">
            <button
              onClick={() => {
                setReviewFilter('incorrect');
                setReviewModuleFilter('all');
                setReviewIdx(0);
                setPhase('review');
              }}
              className="px-6 py-3 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-black text-sm shadow-md transition flex items-center gap-2 cursor-pointer"
            >
              <ShieldAlert className="w-4 h-4" />
              Xem ngay {analytics.totalQ - analytics.totalCorrect} câu sai &amp; Phân tích bẫy
            </button>
            <button
              onClick={() => {
                setReviewFilter('all');
                setReviewModuleFilter('all');
                setReviewIdx(0);
                setPhase('review');
              }}
              className="px-6 py-3 rounded-xl bg-[#0050b3] hover:bg-[#003d8a] text-white font-black text-sm shadow-md transition flex items-center gap-2 cursor-pointer"
            >
              <BookOpen className="w-4 h-4" /> Chữa toàn bộ {analytics.totalQ} câu
            </button>
            <button
              onClick={() => startTest(false)}
              className="px-5 py-3 rounded-xl bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 font-bold text-sm transition flex items-center gap-2 cursor-pointer"
            >
              <RotateCcw className="w-4 h-4" /> Làm lại đề này
            </button>
          </div>
        </main>
      </div>
    );
  }

  // ============================================================================
  // RENDER 4: REVIEW MODE (DETAILED TRAP ANALYSIS + MATH STEP-BY-STEP & DESMOS)
  // ============================================================================
  if (phase === 'review') {
    const q = activeReviewQuestion;
    const safeIdx = Math.min(reviewIdx, Math.max(0, filteredReviewQuestions.length - 1));
    const userAns = q ? answers[q.id] : undefined;
    const isCorrect = q ? isSatQuestionCorrect(q, userAns) : false;

    return (
      <div className="h-screen flex flex-col bg-[#f8fafc] overflow-hidden">
        {/* Top Review Header */}
        <header className="shrink-0 bg-white border-b border-slate-200 px-4 sm:px-6 py-3 flex flex-wrap items-center justify-between gap-3 shadow-sm z-20">
          <div className="flex items-center gap-3">
            <button
              onClick={() => setPhase('summary')}
              className="px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs flex items-center gap-1 cursor-pointer"
            >
              <BarChart3 className="w-3.5 h-3.5" /> Báo cáo điểm
            </button>
            <div>
              <div className="text-sm font-black text-slate-900 line-clamp-1">
                Chữa bài: {testTitle}
              </div>
              <div className="text-[11px] font-semibold text-slate-500">
                {analytics.scaledScore !== null
                  ? `Scaled Score: ${analytics.scaledScore}/800 • `
                  : ''}
                Đúng {analytics.totalCorrect}/{analytics.totalQ} ({analytics.accuracyPct}%)
                {!isMathSection && ' • Click đúp từ bất kỳ để tra từ điển'}
              </div>
            </div>
          </div>

          {/* Filter Bar */}
          <div className="flex flex-wrap items-center gap-2">
            {isMathSection && (
              <>
                <button
                  onClick={toggleCalculator}
                  className={`px-2.5 py-1.5 rounded-lg border text-xs font-bold inline-flex items-center gap-1 transition cursor-pointer ${
                    showCalculator
                      ? 'bg-emerald-600 text-white border-emerald-600'
                      : 'bg-white border-slate-300 text-slate-700 hover:bg-emerald-50 hover:border-emerald-400'
                  }`}
                >
                  <Calculator className="w-3.5 h-3.5" /> Desmos
                </button>
                <button
                  onClick={() => setShowReference(true)}
                  className="px-2.5 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-blue-50 hover:border-blue-400 text-xs font-bold text-slate-700 inline-flex items-center gap-1 cursor-pointer"
                >
                  <Compass className="w-3.5 h-3.5" /> Reference
                </button>
              </>
            )}
            {isAdaptiveMock && !directHardMode && (
              <div className="inline-flex rounded-lg bg-slate-100 p-0.5 text-xs font-bold">
                {(['all', 'm1', 'm2'] as const).map((m) => (
                  <button
                    key={m}
                    onClick={() => {
                      setReviewModuleFilter(m);
                      setReviewIdx(0);
                    }}
                    className={`px-2.5 py-1 rounded-md transition cursor-pointer ${
                      reviewModuleFilter === m
                        ? 'bg-white text-[#0050b3] shadow-sm'
                        : 'text-slate-600 hover:text-slate-900'
                    }`}
                  >
                    {m === 'all' ? 'Cả 2 Mod' : m === 'm1' ? 'Module 1' : 'Module 2'}
                  </button>
                ))}
              </div>
            )}

            <div className="inline-flex items-center rounded-lg bg-slate-100 p-0.5 text-xs font-bold">
              <Filter className="w-3.5 h-3.5 text-slate-400 mx-1.5" />
              {(
                [
                  { id: 'all', label: `Tất cả (${completedQuestionList.length})` },
                  { id: 'incorrect', label: `Câu sai (${analytics.totalQ - analytics.totalCorrect})` },
                  { id: 'flagged', label: `Đánh dấu (${Object.values(flagged).filter(Boolean).length})` },
                ] as const
              ).map((f) => (
                <button
                  key={f.id}
                  onClick={() => {
                    setReviewFilter(f.id);
                    setReviewIdx(0);
                  }}
                  className={`px-2.5 py-1 rounded-md transition cursor-pointer ${
                    reviewFilter === f.id
                      ? 'bg-[#0050b3] text-white shadow-sm'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  {f.label}
                </button>
              ))}
            </div>

            <button
              onClick={handleExit}
              className="px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs cursor-pointer"
            >
              Thoát
            </button>
          </div>
        </header>

        {/* Question Strip */}
        <div className="shrink-0 bg-white border-b border-slate-200 px-4 py-2 overflow-x-auto flex items-center gap-1.5">
          {filteredReviewQuestions.map((item, i) => {
            const ok = isSatQuestionCorrect(item, answers[item.id]);
            const isActive = i === safeIdx;
            return (
              <button
                key={item.id}
                onClick={() => setReviewIdx(i)}
                className={`shrink-0 h-8 min-w-[36px] px-2 rounded-lg text-xs font-black border transition flex items-center justify-center gap-1 cursor-pointer ${
                  isActive
                    ? 'ring-2 ring-[#0050b3] ring-offset-1 '
                    : ''
                }${
                  ok
                    ? 'bg-emerald-50 border-emerald-300 text-emerald-800'
                    : 'bg-rose-50 border-rose-300 text-rose-800'
                }`}
              >
                <span>{item.moduleTag === 'm2' ? `M2·${item.number}` : item.number}</span>
                {flagged[item.id] && <span className="w-1.5 h-1.5 rounded-full bg-amber-500" />}
              </button>
            );
          })}
        </div>

        {/* Review Split Workspace */}
        {!q ? (
          <div className="flex-1 flex flex-col items-center justify-center p-8 text-center">
            <CheckCircle2 className="w-14 h-14 text-emerald-500 mb-3" />
            <h3 className="text-lg font-black text-slate-900">Không có câu nào trong bộ lọc này!</h3>
            <p className="text-sm text-slate-500 mt-1">
              Bạn đã làm đúng hết hoặc chưa đánh dấu câu nào. Chọn lại "Tất cả" để xem toàn bộ bài chữa.
            </p>
            <button
              onClick={() => {
                setReviewFilter('all');
                setReviewModuleFilter('all');
                setReviewIdx(0);
              }}
              className="mt-4 px-5 py-2 rounded-xl bg-[#0050b3] text-white font-bold text-sm cursor-pointer"
            >
              Xem tất cả câu hỏi
            </button>
          </div>
        ) : (
          <div className="flex-1 flex flex-col lg:flex-row overflow-hidden">
            {/* Left Stimulus Pane */}
            <div className="lg:w-1/2 h-1/2 lg:h-full overflow-y-auto p-5 sm:p-8 bg-white border-b lg:border-b-0 lg:border-r border-slate-200">
              <div className="max-w-2xl mx-auto">
                <div className="flex flex-wrap items-center gap-2 mb-4">
                  <span className="px-2.5 py-1 rounded-md bg-slate-900 text-white text-xs font-black">
                    {q.moduleLabel} • Câu {q.number}
                  </span>
                  {q.questionFormat === 'spr' && (
                    <span className="px-2.5 py-1 rounded-md bg-purple-50 text-purple-800 border border-purple-200 text-xs font-black">
                      SPR Grid-In
                    </span>
                  )}
                  <span className="px-2.5 py-1 rounded-md bg-blue-50 text-[#1e3a8a] border border-blue-200 text-xs font-bold">
                    {q.domain}
                  </span>
                  <span className="px-2.5 py-1 rounded-md bg-indigo-50 text-indigo-700 border border-indigo-200 text-xs font-bold">
                    {q.skill}
                  </span>
                  {q.difficulty && (
                    <span className="px-2.5 py-1 rounded-md bg-amber-50 text-amber-800 border border-amber-200 text-xs font-bold">
                      {q.difficulty}
                    </span>
                  )}
                </div>

                <div
                  className={`sat-stimulus-prose ${isMathSection ? 'font-sans' : 'font-serif'} text-[16px] leading-[1.8] text-slate-900 space-y-4`}
                  dangerouslySetInnerHTML={{ __html: renderHighlightedStimulusHtml(q.stimulusHtml, q.id) }}
                />
              </div>
            </div>

            {/* Right Review & Trap Analysis Pane */}
            <div className="lg:w-1/2 h-1/2 lg:h-full overflow-y-auto p-5 sm:p-8 bg-[#f8fafc]">
              <div className="max-w-2xl mx-auto space-y-5">
                {/* Status Banner */}
                <div
                  className={`rounded-2xl p-4 border flex items-center justify-between ${
                    isCorrect
                      ? 'bg-emerald-50 border-emerald-300 text-emerald-900'
                      : 'bg-rose-50 border-rose-300 text-rose-900'
                  }`}
                >
                  <div className="flex items-center gap-2.5">
                    {isCorrect ? (
                      <CheckCircle2 className="w-6 h-6 text-emerald-600 shrink-0" />
                    ) : (
                      <XCircle className="w-6 h-6 text-rose-600 shrink-0" />
                    )}
                    <div>
                      <div className="font-black text-sm">
                        {isCorrect ? 'Chính xác!' : 'Chưa chính xác'}
                      </div>
                      <div className="text-xs opacity-90">
                        Bạn {q.questionFormat === 'spr' ? 'nhập' : 'chọn'}:{' '}
                        <b>{userAns || 'Bỏ trống'}</b> • Đáp án đúng:{' '}
                        <b>{q.correctDisplay || q.correctAnswer}</b>
                      </div>
                    </div>
                  </div>
                  <div className="flex items-center gap-1.5">
                    <button
                      disabled={safeIdx <= 0}
                      onClick={() => setReviewIdx((i) => Math.max(0, i - 1))}
                      className="p-2 rounded-lg bg-white border border-slate-300 disabled:opacity-40 hover:bg-slate-100 cursor-pointer"
                    >
                      <ChevronLeft className="w-4 h-4 text-slate-800" />
                    </button>
                    <button
                      disabled={safeIdx >= filteredReviewQuestions.length - 1}
                      onClick={() =>
                        setReviewIdx((i) => Math.min(filteredReviewQuestions.length - 1, i + 1))
                      }
                      className="p-2 rounded-lg bg-white border border-slate-300 disabled:opacity-40 hover:bg-slate-100 cursor-pointer"
                    >
                      <ChevronRight className="w-4 h-4 text-slate-800" />
                    </button>
                  </div>
                </div>

                {/* Question Stem */}
                <div
                  className="text-[15.5px] font-semibold text-slate-900 leading-relaxed"
                  dangerouslySetInnerHTML={{ __html: renderMathHtml(q.questionHtml) }}
                />

                {/* SPR Comparison Card OR 4 MCQ Options with Trap Breakdown */}
                {q.questionFormat === 'spr' ? (
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div
                      className={`rounded-xl border-2 p-4 ${
                        isCorrect
                          ? 'bg-emerald-50/70 border-emerald-500'
                          : 'bg-rose-50/70 border-rose-400'
                      }`}
                    >
                      <div className="text-[11px] font-black uppercase tracking-wider text-slate-500 mb-1">
                        Đáp án bạn nhập
                      </div>
                      <div
                        className="text-xl font-black text-slate-900"
                        dangerouslySetInnerHTML={{
                          __html: userAns
                            ? renderMathHtml(`\\(${formatSprPreviewLatex(userAns)}\\)`)
                            : '<span class="text-slate-400 text-sm font-semibold">Bỏ trống</span>',
                        }}
                      />
                    </div>
                    <div className="rounded-xl border-2 border-emerald-500 bg-emerald-50/70 p-4">
                      <div className="text-[11px] font-black uppercase tracking-wider text-emerald-700 mb-1">
                        Đáp án chuẩn được chấp nhận
                      </div>
                      <div className="text-xl font-black text-emerald-950 font-mono">
                        {q.correctDisplay || (q.acceptedAnswers || [q.correctAnswer]).join(' | ')}
                      </div>
                    </div>
                  </div>
                ) : (
                  <div className="space-y-3">
                    {q.options.map((opt) => {
                      const isRightOpt = opt.label === q.correctAnswer;
                      const isUserWrongOpt = userAns === opt.label && !isRightOpt;
                      const analysis = q.explanation?.optionAnalysis?.[opt.label];

                      return (
                        <div
                          key={opt.label}
                          className={`rounded-xl border-2 p-4 transition ${
                            isRightOpt
                              ? 'bg-emerald-50/70 border-emerald-500'
                              : isUserWrongOpt
                              ? 'bg-rose-50/70 border-rose-400'
                              : 'bg-white border-slate-200'
                          }`}
                        >
                          <div className="flex items-start gap-3">
                            <span
                              className={`w-7 h-7 rounded-full shrink-0 flex items-center justify-center font-black text-xs border ${
                                isRightOpt
                                  ? 'bg-emerald-600 text-white border-emerald-600'
                                  : isUserWrongOpt
                                  ? 'bg-rose-600 text-white border-rose-600'
                                  : 'bg-slate-100 text-slate-700 border-slate-300'
                              }`}
                            >
                              {opt.label}
                            </span>
                            <div className="flex-1 min-w-0">
                              <div
                                className="text-sm font-semibold text-slate-900 leading-relaxed"
                                dangerouslySetInnerHTML={{ __html: renderMathHtml(opt.text) }}
                              />
                              {analysis && (
                                <div className="mt-2.5 pt-2.5 border-t border-slate-200/80 text-xs leading-relaxed">
                                  <span
                                    className={`inline-block px-2 py-0.5 rounded font-black mr-2 mb-1 ${
                                      isRightOpt
                                        ? 'bg-emerald-600 text-white'
                                        : 'bg-slate-800 text-amber-300'
                                    }`}
                                  >
                                    {analysis.trapTag || (isRightOpt ? 'Đáp án đúng' : 'Bẫy nhiễu')}
                                  </span>
                                  <span
                                    className="text-slate-700"
                                    dangerouslySetInnerHTML={{ __html: renderMathHtml(analysis.reasonVi) }}
                                  />
                                </div>
                              )}
                            </div>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                )}

                {/* Core Summary, Desmos 10s Tip & 1500+ Golden Takeaway */}
                {q.explanation && (
                  <div className="rounded-2xl bg-white border border-blue-200 shadow-sm p-5 space-y-3">
                    <div className="text-xs font-black uppercase tracking-wider text-[#1e3a8a] flex items-center gap-1.5">
                      <Sparkles className="w-4 h-4 text-blue-600" />
                      {isMathSection ? 'Lời giải chi tiết & Chiến lược 800 Math' : 'Phân tích chiến lược 1500+'}
                    </div>
                    <div
                      className="text-sm text-slate-800 leading-relaxed whitespace-pre-line"
                      dangerouslySetInnerHTML={{ __html: renderMathHtml(q.explanation.summaryVi) }}
                    />
                    {q.explanation.desmosTipVi && (
                      <div className="rounded-xl bg-emerald-50 border border-emerald-200 px-4 py-3 text-xs sm:text-sm text-emerald-950 font-medium">
                        <div className="font-black text-emerald-800 flex items-center gap-1.5 mb-1">
                          <Zap className="w-4 h-4 text-emerald-600" /> Mẹo Desmos 10 giây (800-Level Shortcut)
                        </div>
                        <div
                          dangerouslySetInnerHTML={{ __html: renderMathHtml(q.explanation.desmosTipVi) }}
                        />
                      </div>
                    )}
                    {q.explanation.keyTakeaway && (
                      <div className="rounded-xl bg-amber-50 border border-amber-200 px-4 py-3 text-xs sm:text-sm text-amber-950 font-semibold">
                        <span className="font-black text-amber-700">💡 Quy tắc vàng 1500+: </span>
                        <span
                          dangerouslySetInnerHTML={{ __html: renderMathHtml(q.explanation.keyTakeaway) }}
                        />
                      </div>
                    )}
                  </div>
                )}
              </div>
            </div>
          </div>
        )}
        {mathOverlays}
      </div>
    );
  }

  // ============================================================================
  // RENDER 5: CHECK YOUR WORK SCREEN (OFFICIAL BLUEBOOK INTERSTITIAL)
  // ============================================================================
  if (phase === 'check_work' && currentModule) {
    const unansweredCount = currentQuestions.filter((q) => !answers[q.id]).length;
    const flaggedCount = currentQuestions.filter((q) => flagged[q.id]).length;

    return (
      <div className="min-h-screen bg-[#f8fafc] flex flex-col">
        {/* Authentic Bluebook Header */}
        <header className="h-16 px-6 bg-white border-b-2 border-dashed border-[#0050b3]/40 flex items-center justify-between">
          <div>
            <div className="text-sm font-black text-slate-900">{currentModule.title}</div>
            <div className="text-[11px] font-semibold text-slate-500">Check Your Work</div>
          </div>
          <div className="flex items-center gap-2 font-mono font-black text-lg text-slate-900">
            <Clock className={`w-5 h-5 ${secondsLeft < 300 ? 'text-rose-600 animate-pulse' : 'text-[#0050b3]'}`} />
            <span className={secondsLeft < 300 ? 'text-rose-600' : ''}>
              {hideTimer ? '••:••' : formatTimer(secondsLeft)}
            </span>
          </div>
          <button
            onClick={() => setPhase('testing')}
            className="px-4 py-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-xs cursor-pointer"
          >
            Quay lại làm bài
          </button>
        </header>

        <main className="flex-1 flex items-center justify-center p-6">
          <div className="max-w-2xl w-full bg-white rounded-3xl border border-slate-200 shadow-lg p-7 sm:p-9 space-y-6">
            <div className="text-center space-y-1.5">
              <h2 className="text-2xl font-black text-slate-900">Check Your Work</h2>
              <p className="text-sm text-slate-600">
                Kiểm tra lại các câu chưa trả lời hoặc đã gắn cờ trước khi chuyển sang bước tiếp theo.
              </p>
            </div>

            <div className="flex items-center justify-center gap-6 text-xs font-bold text-slate-600 border-y border-slate-200 py-3">
              <span className="flex items-center gap-1.5">
                <span className="w-4 h-4 rounded bg-[#0050b3] inline-block" /> Đã trả lời (
                {currentQuestions.length - unansweredCount})
              </span>
              <span className="flex items-center gap-1.5">
                <span className="w-4 h-4 rounded border-2 border-dashed border-slate-400 inline-block" /> Chưa trả lời (
                {unansweredCount})
              </span>
              <span className="flex items-center gap-1.5">
                <Bookmark className="w-4 h-4 text-amber-500 fill-amber-500" /> Gắn cờ ({flaggedCount})
              </span>
            </div>

            <div className="grid grid-cols-6 sm:grid-cols-9 gap-2.5">
              {currentQuestions.map((q, idx) => {
                const isAns = Boolean(answers[q.id]);
                const isFlg = Boolean(flagged[q.id]);
                return (
                  <button
                    key={q.id}
                    onClick={() => {
                      setCurrentIdx(idx);
                      setPhase('testing');
                    }}
                    className={`relative h-11 rounded-lg font-black text-sm transition cursor-pointer ${
                      isAns
                        ? 'bg-[#0050b3] text-white hover:bg-[#003d8a]'
                        : 'bg-white text-[#0050b3] border-2 border-dashed border-slate-400 hover:border-[#0050b3]'
                    }`}
                  >
                    {q.number}
                    {isFlg && (
                      <Bookmark className="w-3.5 h-3.5 text-amber-400 fill-amber-400 absolute -top-1.5 -right-1.5 drop-shadow" />
                    )}
                  </button>
                );
              })}
            </div>

            {unansweredCount > 0 && (
              <div className="rounded-xl bg-amber-50 border border-amber-200 px-4 py-3 text-xs sm:text-sm text-amber-900 flex items-center gap-2">
                <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0" />
                <span>
                  Bạn vẫn còn <b>{unansweredCount} câu chưa chọn đáp án</b>. Trên Digital SAT không bị trừ điểm câu sai — tuyệt đối đừng bỏ trống câu nào!
                </span>
              </div>
            )}

            <div className="flex flex-col sm:flex-row gap-3 pt-2">
              <button
                onClick={() => setPhase('testing')}
                className="sm:w-1/3 py-3 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-sm cursor-pointer"
              >
                ← Kiểm tra lại
              </button>
              <button
                onClick={handleSubmitCurrentModule}
                className="flex-1 py-3 rounded-xl bg-[#0050b3] hover:bg-[#003d8a] text-white font-black text-sm shadow-md transition cursor-pointer"
              >
                {isAdaptiveMock && activeStage === 'm1'
                  ? 'Nộp Module 1 & Chuyển sang Module 2 →'
                  : 'Nộp bài & Xem báo cáo điểm 200–800 →'}
              </button>
            </div>
          </div>
        </main>
      </div>
    );
  }

  // ============================================================================
  // RENDER 6: ACTIVE BLUEBOOK SPLIT-SCREEN EXAM WORKSPACE
  // ============================================================================
  const q = activeQuestion;
  const activeHighlights = q ? highlightsByQ[q.id] || [] : [];
  const stimulusFontClass =
    fontSize === 'sm' ? 'text-[14.5px]' : fontSize === 'lg' ? 'text-[18.5px]' : 'text-[16px]';

  return (
    <div className="h-screen w-screen flex flex-col bg-white overflow-hidden select-none">
      {/* === OFFICIAL BLUEBOOK TOP HEADER === */}
      <header className="shrink-0 h-16 px-4 sm:px-6 bg-[#f8fafc] flex items-center justify-between relative z-30">
        {/* Left: Section Title & Directions */}
        <div className="flex flex-col min-w-0">
          <div className="text-xs sm:text-sm font-black text-slate-900 truncate max-w-[180px] sm:max-w-[300px]">
            {currentModule?.title || (isMathSection ? 'Section 2: Math' : 'Section 1: Reading and Writing')}
          </div>
          <button
            onClick={() => setShowDirections((v) => !v)}
            className="inline-flex items-center gap-1 text-[11px] font-bold text-slate-600 hover:text-[#0050b3] w-fit cursor-pointer"
          >
            <span>Directions</span>
            {showDirections ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
          </button>
        </div>

        {/* Center: Official Bluebook Timer with Hide Toggle */}
        <div className="flex flex-col items-center">
          <div
            className={`font-mono font-black text-lg sm:text-xl tracking-tight leading-none ${
              secondsLeft < 300 ? 'text-rose-600 animate-pulse' : 'text-slate-900'
            }`}
          >
            {hideTimer ? (
              <span className="inline-flex items-center gap-1 text-slate-500 text-sm">
                <Clock className="w-4 h-4" /> Hidden
              </span>
            ) : (
              formatTimer(secondsLeft)
            )}
          </div>
          <button
            onClick={() => setHideTimer((v) => !v)}
            className="mt-1 px-2.5 py-0.5 rounded-full border border-slate-300 bg-white hover:bg-slate-100 text-[10px] font-bold text-slate-700 inline-flex items-center gap-1 cursor-pointer"
          >
            {hideTimer ? <Eye className="w-3 h-3" /> : <EyeOff className="w-3 h-3" />}
            <span>{hideTimer ? 'Show' : 'Hide'}</span>
          </button>
        </div>

        {/* Right: Bluebook Tools (Desmos & Reference for Math, Highlights, Font Size, Fullscreen, Exit) */}
        <div className="flex items-center gap-1.5 sm:gap-2">
          {isMathSection && (
            <>
              <button
                onClick={toggleCalculator}
                className={`px-2.5 py-1.5 rounded-lg border text-xs font-bold inline-flex items-center gap-1.5 transition cursor-pointer ${
                  showCalculator
                    ? 'bg-emerald-600 border-emerald-600 text-white shadow-sm'
                    : 'bg-white border-slate-300 text-slate-700 hover:bg-emerald-50 hover:border-emerald-400'
                }`}
                title="Mở Máy tính đồ thị Desmos (SAT Edition)"
              >
                <Calculator className="w-3.5 h-3.5" />
                <span className="hidden md:inline">Calculator</span>
              </button>

              <button
                onClick={() => setShowReference((v) => !v)}
                className={`px-2.5 py-1.5 rounded-lg border text-xs font-bold inline-flex items-center gap-1.5 transition cursor-pointer ${
                  showReference
                    ? 'bg-[#0050b3] border-[#0050b3] text-white shadow-sm'
                    : 'bg-white border-slate-300 text-slate-700 hover:bg-blue-50 hover:border-blue-400'
                }`}
                title="Bảng công thức Hình học SAT Reference Sheet"
              >
                <Compass className="w-3.5 h-3.5" />
                <span className="hidden md:inline">Reference</span>
              </button>
            </>
          )}

          <button
            onClick={() => setShowHighlightsDrawer((v) => !v)}
            className={`px-2.5 py-1.5 rounded-lg border text-xs font-bold inline-flex items-center gap-1.5 transition cursor-pointer ${
              showHighlightsDrawer || activeHighlights.length > 0
                ? 'bg-amber-50 border-amber-300 text-amber-900'
                : 'bg-white border-slate-300 text-slate-700 hover:bg-slate-100'
            }`}
            title="Bôi đen đoạn văn bên trái để Highlight & Ghi chú"
          >
            <Highlighter className="w-3.5 h-3.5" />
            <span className="hidden lg:inline">Highlights</span>
            {activeHighlights.length > 0 && (
              <span className="px-1.5 py-0.2 rounded-full bg-amber-400 text-amber-950 text-[10px] font-black">
                {activeHighlights.length}
              </span>
            )}
          </button>

          <button
            onClick={() =>
              setFontSize((prev) => (prev === 'sm' ? 'md' : prev === 'md' ? 'lg' : 'sm'))
            }
            className="px-2.5 py-1.5 rounded-lg bg-white border border-slate-300 hover:bg-slate-100 text-xs font-black text-slate-700 hidden sm:inline-flex items-center gap-1 cursor-pointer"
            title="Thay đổi cỡ chữ"
          >
            <SlidersHorizontal className="w-3.5 h-3.5" />
            <span>{fontSize.toUpperCase()}</span>
          </button>

          <button
            onClick={toggleFullscreen}
            className="p-2 rounded-lg bg-white border border-slate-300 hover:bg-slate-100 text-slate-700 cursor-pointer"
            title="Toàn màn hình"
          >
            {isFullscreen ? <Minimize2 className="w-4 h-4" /> : <Maximize2 className="w-4 h-4" />}
          </button>

          <button
            onClick={() => setShowExitConfirm(true)}
            className="px-2.5 py-1.5 rounded-lg bg-white border border-slate-300 hover:bg-rose-50 hover:border-rose-300 hover:text-rose-700 text-xs font-bold text-slate-700 cursor-pointer"
          >
            Thoát
          </button>
        </div>
      </header>

      {/* Authentic College Board Bluebook Dashed Accent Strip */}
      <div
        className="shrink-0 h-1.5 w-full"
        style={{
          backgroundImage:
            'repeating-linear-gradient(90deg, #1e3a8a 0px, #1e3a8a 26px, transparent 26px, transparent 34px, #3b82f6 34px, #3b82f6 60px, transparent 60px, transparent 68px)',
        }}
      />

      {/* Directions Popover */}
      {showDirections && (
        <div className="absolute top-16 left-4 sm:left-6 z-40 max-w-lg bg-white rounded-2xl border border-slate-300 shadow-2xl p-5 text-sm text-slate-700 leading-relaxed">
          <div className="flex items-center justify-between mb-2">
            <span className="font-black text-slate-900">
              {isMathSection ? 'Directions — Math' : 'Directions — Reading and Writing'}
            </span>
            <button
              onClick={() => setShowDirections(false)}
              className="text-xs font-bold text-[#0050b3] hover:underline cursor-pointer"
            >
              Đóng
            </button>
          </div>
          <div
            dangerouslySetInnerHTML={{
              __html:
                currentModule?.directionsHtml ||
                (isMathSection ? DEFAULT_MATH_DIRECTIONS : DEFAULT_RW_DIRECTIONS),
            }}
          />
        </div>
      )}

      {/* Highlights & Notes Drawer */}
      {showHighlightsDrawer && q && (
        <div className="absolute top-20 right-4 z-40 w-80 bg-white rounded-2xl border border-slate-300 shadow-2xl p-4 space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-xs font-black uppercase tracking-wider text-slate-800">
              Highlights &amp; Notes (Câu {q.number})
            </span>
            <button
              onClick={() => setShowHighlightsDrawer(false)}
              className="text-xs font-bold text-slate-500 hover:text-slate-900 cursor-pointer"
            >
              Đóng
            </button>
          </div>
          {activeHighlights.length === 0 ? (
            <p className="text-xs text-slate-500 leading-relaxed">
              Bôi đen bất kỳ đoạn chữ nào trong văn bản bên trái để tô màu highlight hoặc gắn ghi chú nhanh.
            </p>
          ) : (
            <div className="space-y-2 max-h-64 overflow-y-auto">
              {activeHighlights.map((hl) => (
                <div
                  key={hl.id}
                  className="rounded-xl border border-slate-200 p-2.5 text-xs space-y-1 bg-slate-50"
                >
                  <div className="flex items-start justify-between gap-2">
                    <span
                      className="px-1.5 py-0.5 rounded font-semibold text-slate-900"
                      style={{ background: HIGHLIGHT_STYLES[hl.color].bg }}
                    >
                      "{hl.text}"
                    </span>
                    <button
                      onClick={() => removeHighlight(q.id, hl.id)}
                      className="text-slate-400 hover:text-rose-600 shrink-0 cursor-pointer"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                  {hl.note && <div className="text-slate-700 italic">📝 {hl.note}</div>}
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Floating Selection Highlight Toolbar */}
      {selectionPopup && (
        <div
          className="fixed z-50 -translate-x-1/2 -translate-y-full bg-slate-900 text-white rounded-xl shadow-2xl px-3 py-2 flex flex-col gap-2 border border-slate-700"
          style={{ left: selectionPopup.x, top: selectionPopup.y }}
          onMouseDown={(e) => e.preventDefault()}
        >
          <div className="flex items-center gap-2">
            <span className="text-[11px] font-bold text-slate-300">Highlight:</span>
            {(['yellow', 'cyan', 'pink'] as const).map((c) => (
              <button
                key={c}
                onClick={() => applyHighlight(c)}
                className="w-5 h-5 rounded-full border-2 border-white/80 hover:scale-110 transition cursor-pointer"
                style={{ background: HIGHLIGHT_STYLES[c].bg }}
                title={HIGHLIGHT_STYLES[c].label}
              />
            ))}
            <div className="w-px h-4 bg-slate-700 mx-0.5" />
            <button
              onClick={() => setShowNoteInput((v) => !v)}
              className="text-[11px] font-bold text-amber-300 hover:text-amber-200 cursor-pointer"
            >
              + Note
            </button>
          </div>
          {showNoteInput && (
            <div className="flex items-center gap-1.5" onMouseDown={(e) => e.stopPropagation()}>
              <input
                type="text"
                value={pendingNoteText}
                onChange={(e) => setPendingNoteText(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter') applyHighlight('yellow', pendingNoteText);
                }}
                placeholder="Ghi chú ngắn..."
                className="bg-slate-800 border border-slate-600 rounded-lg px-2 py-1 text-xs text-white outline-none w-44"
                autoFocus
              />
              <button
                onClick={() => applyHighlight('yellow', pendingNoteText)}
                className="px-2 py-1 rounded-lg bg-amber-400 text-slate-950 font-black text-xs cursor-pointer"
              >
                Lưu
              </button>
            </div>
          )}
        </div>
      )}

      {/* === MAIN SPLIT-SCREEN WORKSPACE === */}
      {q && (
        <div ref={workspaceRef} className="flex-1 flex flex-col lg:flex-row overflow-hidden relative">
          {/* LEFT PANE: PASSAGE / DATA / DUAL-TEXT */}
          <div
            ref={stimulusRef}
            onMouseUp={handleStimulusMouseUp}
            style={{ width: undefined }}
            className="h-1/2 lg:h-full overflow-y-auto px-6 sm:px-10 py-6 sm:py-8 bg-white select-text lg:shrink-0"
            data-pane="left"
          >
            <style>{`
              @media (min-width: 1024px) {
                [data-pane="left"] { width: ${leftPanePct}% !important; }
                [data-pane="right"] { width: ${100 - leftPanePct}% !important; }
              }
              .sat-stimulus-prose table { width: 100%; border-collapse: collapse; margin: 12px 0; font-family: 'Segoe UI', system-ui, sans-serif; font-size: 13.5px; }
              .sat-stimulus-prose th, .sat-stimulus-prose td { border: 1px solid #cbd5e1; padding: 8px 10px; text-align: left; }
              .sat-stimulus-prose th { background: #f1f5f9; font-weight: 800; color: #0f172a; }
              .sat-stimulus-prose svg { max-width: 100%; height: auto; display: block; margin: 12px auto; }
              .sat-stimulus-prose ul { list-style-type: disc; padding-left: 22px; margin: 10px 0; }
              .sat-stimulus-prose li { margin-bottom: 6px; }
            `}</style>
            <div
              className={`sat-stimulus-prose max-w-2xl mx-auto ${isMathSection ? 'font-sans' : 'font-serif'} ${stimulusFontClass} leading-[1.85] text-slate-900 space-y-4`}
              dangerouslySetInnerHTML={{ __html: renderHighlightedStimulusHtml(q.stimulusHtml, q.id) }}
            />
            {q.questionFormat === 'spr' && (
              <div className="max-w-2xl mx-auto mt-6 rounded-2xl border border-slate-200 bg-slate-50 p-4 text-xs text-slate-700 space-y-2 leading-relaxed">
                <div className="font-black text-slate-900 uppercase tracking-wide text-[11px]">
                  Student-Produced Response Directions
                </div>
                <ul className="list-disc pl-4 space-y-1">
                  <li>Nhập một đáp án số chính xác (số nguyên, phân số <code>a/b</code>, hoặc số thập phân).</li>
                  <li>Với phân số hoặc số thập phân tương đương (ví dụ <code>3/4</code>, <code>0.75</code>, <code>.75</code>), mọi cách viết đúng đều được chấm điểm tối đa.</li>
                  <li>Nếu đáp án là số âm, đặt dấu trừ <code>-</code> ở đầu (ví dụ <code>-5/2</code> hoặc <code>-2.5</code>).</li>
                  <li><b>Không nhập hỗn số</b>: thay vì <code>1 1/2</code>, hãy nhập <code>3/2</code> hoặc <code>1.5</code>.</li>
                </ul>
              </div>
            )}
          </div>

          {/* DRAGGABLE CENTER DIVIDER (Desktop) */}
          <div
            onMouseDown={() => setIsDraggingDivider(true)}
            className={`hidden lg:flex w-2.5 shrink-0 cursor-col-resize items-center justify-center bg-slate-100 hover:bg-blue-100 border-x border-slate-200 transition ${
              isDraggingDivider ? 'bg-blue-200' : ''
            }`}
            title="Kéo để thay đổi độ rộng 2 khung"
          >
            <div className="w-1 h-10 rounded-full bg-slate-400" />
          </div>

          {/* RIGHT PANE: QUESTION & CHOICES / SPR GRID-IN */}
          <div
            data-pane="right"
            className="h-1/2 lg:h-full overflow-y-auto px-6 sm:px-10 py-6 sm:py-8 bg-white border-t lg:border-t-0 border-slate-200"
          >
            <div className="max-w-2xl mx-auto space-y-5">
              {/* Official Bluebook Question Action Strip */}
              <div className="flex items-center justify-between bg-slate-100/90 border-b-2 border-dashed border-slate-300 rounded-t-xl px-3 py-2">
                <div className="flex items-center gap-3">
                  <span className="w-8 h-8 rounded-md bg-slate-900 text-white font-black text-sm flex items-center justify-center">
                    {q.number}
                  </span>
                  <button
                    onClick={() =>
                      setFlagged((prev) => ({ ...prev, [q.id]: !prev[q.id] }))
                    }
                    className={`inline-flex items-center gap-1.5 text-xs font-bold px-2.5 py-1 rounded-lg transition cursor-pointer ${
                      flagged[q.id]
                        ? 'bg-amber-100 text-amber-900'
                        : 'text-slate-600 hover:bg-slate-200'
                    }`}
                  >
                    <Bookmark
                      className={`w-4 h-4 ${
                        flagged[q.id] ? 'text-amber-500 fill-amber-500' : 'text-slate-500'
                      }`}
                    />
                    <span>Mark for Review</span>
                  </button>
                </div>

                {/* Official ABC Option Eliminator Toggle (MCQ only) */}
                {q.questionFormat !== 'spr' ? (
                  <button
                    onClick={() => setEliminatorEnabled((v) => !v)}
                    className={`px-2.5 py-1 rounded-lg border text-xs font-black tracking-tight transition cursor-pointer ${
                      eliminatorEnabled
                        ? 'bg-[#0050b3] text-white border-[#0050b3] shadow-sm'
                        : 'bg-white text-slate-700 border-slate-300 hover:bg-slate-200'
                    }`}
                    title="Bật/Tắt chế độ gạch loại trừ đáp án sai (Option Eliminator)"
                  >
                    <span className="line-through decoration-2">ABC</span>
                  </button>
                ) : (
                  <span className="px-2.5 py-1 rounded-lg bg-purple-100 text-purple-800 text-[11px] font-black">
                    Student-Produced Response
                  </span>
                )}
              </div>

              {/* Question Prompt */}
              <div
                className={`${stimulusFontClass} font-medium text-slate-900 leading-relaxed select-text`}
                dangerouslySetInnerHTML={{ __html: renderMathHtml(q.questionHtml) }}
              />

              {/* SPR Grid-In Box OR 4 Answer Choice Cards */}
              {q.questionFormat === 'spr' ? (
                <div className="space-y-4 pt-2">
                  <div className="rounded-2xl border-2 border-slate-300 focus-within:border-[#0050b3] bg-slate-50/50 p-5 space-y-3 transition">
                    <label className="block text-xs font-black uppercase tracking-wider text-slate-600">
                      Nhập đáp án số của bạn (Exact Answer)
                    </label>
                    <div className="flex items-center gap-2">
                      <input
                        type="text"
                        inputMode="decimal"
                        value={answers[q.id] || ''}
                        onChange={(e) => handleSprChange(q.id, e.target.value)}
                        placeholder="VD: 12, -3/4, 0.75"
                        maxLength={14}
                        className="flex-1 bg-white border-2 border-slate-300 focus:border-[#0050b3] rounded-xl px-4 py-3 font-mono text-lg font-black text-slate-900 outline-none select-text"
                      />
                      {answers[q.id] && (
                        <button
                          type="button"
                          onClick={() => handleSprChange(q.id, '')}
                          className="px-3 py-3 rounded-xl border border-slate-300 bg-white hover:bg-slate-100 text-xs font-bold text-slate-600 cursor-pointer"
                        >
                          Xóa
                        </button>
                      )}
                    </div>
                    {answers[q.id] && parseSatNumericValue(answers[q.id]) === null && (
                      <div className="text-xs font-bold text-rose-600 flex items-center gap-1.5">
                        <AlertTriangle className="w-3.5 h-3.5" />
                        Định dạng chưa hợp lệ — chỉ nhập số, dấu chấm <code>.</code>, dấu gạch phân số <code>/</code> hoặc dấu âm <code>-</code> ở đầu.
                      </div>
                    )}
                    <div className="pt-2 border-t border-slate-200 flex items-center justify-between">
                      <span className="text-xs font-bold text-slate-500">Answer Preview:</span>
                      <div
                        className="min-h-[32px] px-4 py-1 rounded-lg bg-white border border-slate-200 text-lg font-bold text-slate-900 flex items-center"
                        dangerouslySetInnerHTML={{
                          __html:
                            answers[q.id] && parseSatNumericValue(answers[q.id]) !== null
                              ? renderMathHtml(`\\(${formatSprPreviewLatex(answers[q.id])}\\)`)
                              : '<span class="text-slate-400 text-xs font-normal">—</span>',
                        }}
                      />
                    </div>
                  </div>
                </div>
              ) : (
                <div className="space-y-3 pt-1">
                  {q.options.map((opt) => {
                    const isSelected = answers[q.id] === opt.label;
                    const isEliminated = Boolean(eliminated[q.id]?.[opt.label]);

                    return (
                      <div key={opt.label} className="flex items-center gap-2">
                        <button
                          type="button"
                          onClick={() => handleSelectOption(q.id, opt.label)}
                          className={`flex-1 text-left rounded-xl border-2 px-4 py-3.5 transition flex items-start gap-3.5 relative cursor-pointer ${
                            isSelected
                              ? 'border-[#0050b3] bg-blue-50/60 shadow-sm'
                              : isEliminated
                              ? 'border-slate-200 bg-slate-50/70 opacity-50'
                              : 'border-slate-300 bg-white hover:border-[#0050b3]/60 hover:bg-slate-50'
                          }`}
                        >
                          <span
                            className={`w-7 h-7 rounded-full shrink-0 flex items-center justify-center font-black text-xs border-2 mt-0.5 transition ${
                              isSelected
                                ? 'bg-[#0050b3] text-white border-[#0050b3]'
                                : 'bg-white text-slate-800 border-slate-700'
                            }`}
                          >
                            {opt.label}
                          </span>
                          <span
                            className={`flex-1 text-[15px] leading-relaxed text-slate-900 ${
                              isEliminated ? 'line-through decoration-slate-500 decoration-2' : ''
                            }`}
                            dangerouslySetInnerHTML={{ __html: renderMathHtml(opt.text) }}
                          />
                        </button>

                        {/* Option Eliminator Strikethrough Button */}
                        {eliminatorEnabled && (
                          <button
                            type="button"
                            onClick={() => toggleEliminateOption(q.id, opt.label)}
                            className={`shrink-0 w-9 h-9 rounded-full border text-xs font-black transition flex items-center justify-center cursor-pointer ${
                              isEliminated
                                ? 'bg-slate-800 text-white border-slate-800'
                                : 'bg-white text-slate-600 border-slate-300 hover:bg-slate-100'
                            }`}
                            title={isEliminated ? 'Khôi phục đáp án' : `Gạch loại trừ đáp án ${opt.label}`}
                          >
                            {isEliminated ? (
                              <span className="text-[10px]">Undo</span>
                            ) : (
                              <span className="line-through">{opt.label}</span>
                            )}
                          </button>
                        )}
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* === OFFICIAL BLUEBOOK BOTTOM FOOTER === */}
      <div
        className="shrink-0 h-1.5 w-full"
        style={{
          backgroundImage:
            'repeating-linear-gradient(90deg, #1e3a8a 0px, #1e3a8a 26px, transparent 26px, transparent 34px, #3b82f6 34px, #3b82f6 60px, transparent 60px, transparent 68px)',
        }}
      />
      <footer className="shrink-0 h-16 px-4 sm:px-6 bg-[#f8fafc] flex items-center justify-between relative z-30">
        {/* Left: Test Identifier */}
        <div className="hidden sm:flex items-center gap-2 min-w-0">
          <span className="text-xs font-black text-slate-800 truncate max-w-[240px]">
            {testTitle}
          </span>
        </div>

        {/* Center: Official Question Navigator Pill */}
        <div className="relative mx-auto sm:mx-0">
          <button
            onClick={() => setShowNavigator((v) => !v)}
            className="px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs sm:text-sm inline-flex items-center gap-2 shadow cursor-pointer"
          >
            <span>
              Question {q?.number || currentIdx + 1} of {currentQuestions.length}
            </span>
            {showNavigator ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
          </button>

          {/* Navigator Popover */}
          {showNavigator && (
            <div className="absolute bottom-14 left-1/2 -translate-x-1/2 w-[330px] sm:w-[420px] bg-white rounded-2xl border border-slate-300 shadow-2xl p-5 z-50">
              <div className="flex items-center justify-between pb-3 border-b border-slate-200">
                <span className="text-sm font-black text-slate-900 truncate">
                  {currentModule?.title}
                </span>
                <button
                  onClick={() => setShowNavigator(false)}
                  className="text-xs font-bold text-slate-500 hover:text-slate-900 cursor-pointer"
                >
                  ✕
                </button>
              </div>

              <div className="flex items-center justify-center gap-4 text-[11px] font-bold text-slate-600 py-2.5 border-b border-slate-100">
                <span className="flex items-center gap-1">
                  <span className="w-3 h-3 rounded bg-[#0050b3] inline-block" /> Answered
                </span>
                <span className="flex items-center gap-1">
                  <span className="w-3 h-3 rounded border border-dashed border-slate-400 inline-block" /> Unanswered
                </span>
                <span className="flex items-center gap-1">
                  <Bookmark className="w-3 h-3 text-amber-500 fill-amber-500" /> For Review
                </span>
              </div>

              <div className="grid grid-cols-7 sm:grid-cols-9 gap-2 py-4 max-h-60 overflow-y-auto">
                {currentQuestions.map((item, idx) => {
                  const isAns = Boolean(answers[item.id]);
                  const isFlg = Boolean(flagged[item.id]);
                  const isCur = idx === currentIdx;
                  return (
                    <button
                      key={item.id}
                      onClick={() => {
                        setCurrentIdx(idx);
                        setShowNavigator(false);
                      }}
                      className={`relative h-9 rounded-md font-black text-xs transition cursor-pointer ${
                        isCur ? 'ring-2 ring-slate-900 ring-offset-1 ' : ''
                      }${
                        isAns
                          ? 'bg-[#0050b3] text-white'
                          : 'bg-white text-[#0050b3] border border-dashed border-slate-400 hover:border-[#0050b3]'
                      }`}
                    >
                      {item.number}
                      {isFlg && (
                        <Bookmark className="w-3 h-3 text-amber-400 fill-amber-400 absolute -top-1 -right-1" />
                      )}
                    </button>
                  );
                })}
              </div>

              <button
                onClick={() => {
                  setShowNavigator(false);
                  setPhase('check_work');
                }}
                className="w-full py-2 rounded-xl border-2 border-[#0050b3] text-[#0050b3] hover:bg-blue-50 font-black text-xs transition cursor-pointer"
              >
                Go to Review Page (Check Your Work)
              </button>
            </div>
          )}
        </div>

        {/* Right: Back / Next Buttons */}
        <div className="flex items-center gap-2">
          <button
            disabled={currentIdx <= 0}
            onClick={() => setCurrentIdx((i) => Math.max(0, i - 1))}
            className="px-4 py-2 rounded-full bg-white border border-slate-300 hover:bg-slate-100 disabled:opacity-40 text-slate-800 font-bold text-xs sm:text-sm cursor-pointer"
          >
            Back
          </button>
          <button
            onClick={() => {
              if (currentIdx < currentQuestions.length - 1) {
                setCurrentIdx((i) => i + 1);
              } else {
                setPhase('check_work');
              }
            }}
            className="px-5 py-2 rounded-full bg-[#0050b3] hover:bg-[#003d8a] text-white font-black text-xs sm:text-sm shadow cursor-pointer"
          >
            {currentIdx < currentQuestions.length - 1 ? 'Next' : 'Check Work'}
          </button>
        </div>
      </footer>

      {/* Exit Confirmation Modal */}
      {showExitConfirm && (
        <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl border border-slate-200 shadow-2xl max-w-sm w-full p-6 space-y-4 text-center">
            <AlertTriangle className="w-10 h-10 text-amber-500 mx-auto" />
            <h3 className="text-lg font-black text-slate-900">Thoát khỏi bài thi?</h3>
            <p className="text-sm text-slate-600">
              Bài làm hiện tại chưa được nộp. Bạn có chắc muốn thoát về trang danh sách không?
            </p>
            <div className="flex gap-2.5 pt-1">
              <button
                onClick={() => setShowExitConfirm(false)}
                className="flex-1 py-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-sm cursor-pointer"
              >
                Tiếp tục làm
              </button>
              <button
                onClick={handleExit}
                className="flex-1 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-bold text-sm cursor-pointer"
              >
                Thoát ngay
              </button>
            </div>
          </div>
        </div>
      )}
      {mathOverlays}
    </div>
  );
}
