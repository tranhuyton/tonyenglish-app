import React, { useState, useEffect, useMemo, useRef } from 'react';
import { supabase } from './supabase';
import {
  WT2_PILLARS,
  WT2_STRUCTURES,
  WT2_SUBJECT_GROUPS,
  WT2_LINKER_ROLE_OPTIONS,
  WT2_LINKING_GROUPS,
  WT2_REFLEX_QUESTIONS,
  buildMultiIdeaParagraphs,
  detectWt2QuestionGuide,
  getBodyRoleLabels,
  getLinkerRoleForIdea,
  getRecommendedSentenceDepths,
  Wt2Category,
  Wt2BodyMode,
  MultiIdeaCount,
  IdeaSentenceDepth,
  LinkerRole,
  MultiBodyIdeaSpec,
  Wt2TemplateId,
  PillarSlotType,
  Wt2Pillar,
  ReflexQuestion
} from './wt2PillarData';

export interface Wt2StudioOpenPayload {
  topic: string;
  label?: string;
  category?: Wt2Category | 'auto';
  subType?: Wt2TemplateId;
  taskId?: string;
  presetPillar1?: number;
  presetPillar2?: number;
  /** Mở thẳng Phiên bản 1 ('single' - 1 ý sâu 4 câu) hoặc Phiên bản 2 ('multi' - 1–5 ý + Linking Words, 1–2 câu/ý) */
  bodyMode?: Wt2BodyMode;
}

interface Wt2PillarStudioModalProps {
  isOpen: boolean;
  onClose: () => void;
  payload: Wt2StudioOpenPayload | null;
  courseId?: string | null;
  onMarkTaskComplete?: (taskId: string) => void;
}

interface IdeaSelection {
  id: number;
  polarity: 'positive' | 'negative';
  sentences: IdeaSentenceDepth;
}

type MultiBodyTuple = [
  IdeaSelection,
  IdeaSelection,
  IdeaSelection,
  IdeaSelection,
  IdeaSelection
];

const CATEGORY_OPTIONS: { id: Wt2Category; label: string; shortDesc: string }[] = [
  { id: 'discussion', label: '1. Discussion', shortDesc: 'Discuss both views & opinion' },
  { id: 'argument', label: '2. Argument', shortDesc: 'Advantages & Disadvantages / Outweigh' },
  { id: 'opinion', label: '3. Opinion', shortDesc: 'Agree or Disagree (V1 / V2)' },
  { id: 'mixed', label: '4. Mixed', shortDesc: 'Problems-Solutions / Causes-Effects' },
  { id: 'twopart', label: '5. Two-part', shortDesc: '2 câu hỏi trực tiếp' }
];

const COL_LABELS: Record<PillarSlotType, { badge: string; vi: string; color: string }> = {
  pillar: { badge: 'Tên Trụ Ý', vi: 'Advantage / Disadvantage / Factor', color: 'bg-indigo-100 text-indigo-800 border-indigo-300' },
  cause: { badge: 'Cause', vi: 'Nguyên nhân / Giải thích', color: 'bg-sky-100 text-sky-800 border-sky-300' },
  effect: { badge: 'Effect', vi: 'Kết quả / Hệ quả', color: 'bg-amber-100 text-amber-800 border-amber-300' },
  example: { badge: 'Example', vi: 'Ví dụ & Số liệu khảo sát', color: 'bg-emerald-100 text-emerald-800 border-emerald-300' },
  compact_support: {
    badge: 'Triển khai gọn (Câu 2)',
    vi: 'Gộp gọn Nhân–Quả trong 1 câu',
    color: 'bg-teal-100 text-teal-800 border-teal-300'
  },
  compact_single: {
    badge: 'Câu gộp (1 câu/ý)',
    vi: 'Trụ ý + Nhân–Quả trọn vẹn 1 câu',
    color: 'bg-fuchsia-100 text-fuchsia-800 border-fuchsia-300'
  }
};

// Shuffled display order so students actively distinguish Cause / Example / Pillar / Effect
const SHUFFLED_COLS: PillarSlotType[] = ['cause', 'example', 'pillar', 'effect'];

// 3-Tier color & priority metadata matching Lecture "6. Task 2: Idea Pillars" (#28a745 / #007bff / #6f42c1)
const PILLAR_TIER_META: Record<
  1 | 2 | 3,
  {
    tier: 1 | 2 | 3;
    tabTitle: string;
    tabSub: string;
    shortBadge: string;
    headerTitle: string;
    priorityHint: string;
    optgroupLabel: string;
    activeTabCls: string;
    inactiveTabCls: string;
    headerCls: string;
    panelBorderCls: string;
    cardBorderCls: string;
    nameTextCls: string;
    pillBadgeCls: string;
  }
> = {
  1: {
    tier: 1,
    tabTitle: '🟢 Ưu tiên 1: Bảng Xanh Lá (9 Trụ ý)',
    tabSub: 'Phổ biến & dễ dùng nhất • Cần thuộc lòng',
    shortBadge: '🟢 Bảng Xanh Lá • Ưu tiên 1',
    headerTitle: 'TIER 1: BASIC (9 TRỤ Ý) — BẢNG MÀU XANH LÁ CÂY • ƯU TIÊN SỐ 1',
    priorityHint:
      'Những ý phổ biến & dễ dùng nhất — luôn dò nhặt ở bảng này trước tiên (bắt buộc học thuộc lòng).',
    optgroupLabel:
      '🟢 BẢNG XANH LÁ — ƯU TIÊN 1: Phổ biến & dễ dùng nhất • Cần thuộc (#1 - #9)',
    activeTabCls: 'bg-[#28a745] text-white border-[#28a745] shadow-xs',
    inactiveTabCls: 'bg-[#eaf8ee] text-[#19692c] border-[#28a745]/45 hover:bg-[#dcf2e2]',
    headerCls: 'bg-[#28a745] text-white',
    panelBorderCls: 'border-[#28a745]/45 bg-[#f6fcf8]',
    cardBorderCls: 'border-l-4 border-l-[#28a745] border-slate-200 hover:border-[#28a745]/65',
    nameTextCls: 'text-[#1e7e34]',
    pillBadgeCls: 'bg-[#eaf8ee] text-[#19692c] border-[#28a745]/40'
  },
  2: {
    tier: 2,
    tabTitle: '🔵 Ưu tiên 2: Bảng Xanh Da Trời (4 Trụ ý)',
    tabSub: 'Khi Xanh lá chưa hợp • Cần thuộc lòng',
    shortBadge: '🔵 Bảng Xanh Da Trời • Ưu tiên 2',
    headerTitle: 'TIER 2: ADVANCED (4 TRỤ Ý BỔ SUNG) — BẢNG XANH DA TRỜI • ƯU TIÊN SỐ 2',
    priorityHint:
      'Chỉ chuyển sang bảng này khi Bảng Xanh Lá chưa nhặt được ý phù hợp (cần học thuộc lòng cùng Bảng Xanh Lá).',
    optgroupLabel:
      '🔵 BẢNG XANH DA TRỜI — ƯU TIÊN 2: Dùng khi Xanh lá chưa khớp • Cần thuộc (#10 - #13)',
    activeTabCls: 'bg-[#007bff] text-white border-[#007bff] shadow-xs',
    inactiveTabCls: 'bg-[#e8f3ff] text-[#0056b3] border-[#007bff]/45 hover:bg-[#d8ebff]',
    headerCls: 'bg-[#007bff] text-white',
    panelBorderCls: 'border-[#007bff]/45 bg-[#f5faff]',
    cardBorderCls: 'border-l-4 border-l-[#007bff] border-slate-200 hover:border-[#007bff]/65',
    nameTextCls: 'text-[#0062cc]',
    pillBadgeCls: 'bg-[#e8f3ff] text-[#0056b3] border-[#007bff]/40'
  },
  3: {
    tier: 3,
    tabTitle: '🟣 Ưu tiên 3: Bảng Tím (6 Trụ ý)',
    tabSub: 'Dự phòng khi 2 bảng đầu chưa khớp',
    shortBadge: '🟣 Bảng Tím • Ưu tiên 3 (Dự phòng)',
    headerTitle: 'TIER 3: PRO MASTER (6 TRỤ Ý CHUYÊN SÂU) — BẢNG TÍM • ƯU TIÊN SỐ 3 (DỰ PHÒNG)',
    priorityHint:
      'Chỉ dùng tiếp khi cả Bảng Xanh Lá & Xanh Da Trời đều không khớp đề (học sinh chủ yếu cần thuộc 2 bảng đầu).',
    optgroupLabel:
      '🟣 BẢNG TÍM — ƯU TIÊN 3: Dự phòng khi 2 bảng đầu chưa khớp (#14 - #19)',
    activeTabCls: 'bg-[#6f42c1] text-white border-[#6f42c1] shadow-xs',
    inactiveTabCls: 'bg-[#f3effb] text-[#533094] border-[#6f42c1]/45 hover:bg-[#e8e0f8]',
    headerCls: 'bg-[#6f42c1] text-white',
    panelBorderCls: 'border-[#6f42c1]/45 bg-[#faf8fe]',
    cardBorderCls: 'border-l-4 border-l-[#6f42c1] border-slate-200 hover:border-[#6f42c1]/65',
    nameTextCls: 'text-[#59339d]',
    pillBadgeCls: 'bg-[#f3effb] text-[#533094] border-[#6f42c1]/40'
  }
};

const DEFAULT_LINKERS: Record<string, string> = {
  b1_link_solo: 'Specifically,',
  b1_link_start: 'Firstly,',
  b1_link_mid2: 'Furthermore,',
  b1_link_mid3: 'In addition,',
  b1_link_mid4: 'Beyond this,',
  b1_link_close: 'Finally,',
  b2_link_solo: 'In particular,',
  b2_link_start: 'To begin with,',
  b2_link_mid2: 'Moreover,',
  b2_link_mid3: 'Additionally,',
  b2_link_mid4: 'Equally importantly,',
  b2_link_close: 'Last but not least,'
};

function makeSlotUnitKey(
  bodyIndex: 1 | 2,
  col: PillarSlotType,
  ideaIndex?: 1 | 2 | 3 | 4 | 5
): string {
  return ideaIndex ? `${bodyIndex}_${ideaIndex}_${col}` : `${bodyIndex}_${col}`;
}

function swapBodyPrefixMap<T>(rec: Record<string, T>): Record<string, T> {
  const next: Record<string, T> = {};
  Object.entries(rec).forEach(([k, v]) => {
    if (k.startsWith('1_')) {
      next[`2_${k.slice(2)}`] = v;
    } else if (k.startsWith('2_')) {
      next[`1_${k.slice(2)}`] = v;
    } else {
      next[k] = v;
    }
  });
  return next;
}

function makeFiveSelections(
  candidates: { id: number; polarity: 'positive' | 'negative' }[],
  presetFirstId: number | undefined,
  defaultPolarity: 'positive' | 'negative',
  count: MultiIdeaCount = 2
): MultiBodyTuple {
  const depths = getRecommendedSentenceDepths(count);
  const fallbackPool = [1, 3, 5, 6, 7, 2, 4, 9, 10, 13, 16, 17];
  const chosenIds: number[] = [];
  if (presetFirstId && presetFirstId >= 1 && presetFirstId <= 19) {
    chosenIds.push(presetFirstId);
  }
  for (const c of candidates) {
    if (!chosenIds.includes(c.id)) chosenIds.push(c.id);
    if (chosenIds.length >= 5) break;
  }
  for (const fid of fallbackPool) {
    if (!chosenIds.includes(fid)) chosenIds.push(fid);
    if (chosenIds.length >= 5) break;
  }
  return [0, 1, 2, 3, 4].map((idx) => ({
    id: chosenIds[idx],
    polarity: candidates[idx]?.polarity ?? defaultPolarity,
    sentences: depths[idx]
  })) as MultiBodyTuple;
}

function defaultPolaritiesForTemplate(
  cat: Wt2Category,
  tpl: Wt2TemplateId
): { pol1: 'positive' | 'negative'; pol2: 'positive' | 'negative' } {
  if (cat === 'argument') return { pol1: 'positive', pol2: 'negative' };
  if (cat === 'mixed') {
    return { pol1: 'negative', pol2: tpl === 'mixed_ps' ? 'positive' : 'negative' };
  }
  return { pol1: 'positive', pol2: 'positive' };
}

function defaultTemplateForCategory(cat: Wt2Category, sub?: Wt2TemplateId): Wt2TemplateId {
  if (sub && WT2_STRUCTURES[sub]) return sub;
  switch (cat) {
    case 'discussion':
      return 'discussion';
    case 'argument':
      return 'argument';
    case 'opinion':
      return 'opinion_v2';
    case 'mixed':
      return 'mixed_ps';
    case 'twopart':
      return 'twopart';
  }
}

export function normalizeWt2TopicKey(raw: string): string {
  return (raw || '')
    .replace(/\s+/g, ' ')
    .trim()
    .toLowerCase();
}

interface Wt2StudioStateSnapshot {
  selectedCategory: Wt2Category;
  templateId: Wt2TemplateId;
  stance: 'agree' | 'disagree';
  difficulty: 'level1' | 'level2';
  bodyMode: Wt2BodyMode;
  swapBodies?: boolean;
  pillar1Id: number;
  pillar1Polarity: 'positive' | 'negative';
  pillar2Id: number;
  pillar2Polarity: 'positive' | 'negative';
  b1IdeaCount: MultiIdeaCount;
  b2IdeaCount: MultiIdeaCount;
  multiPillars: { 1: MultiBodyTuple; 2: MultiBodyTuple };
  linkers: Record<string, string>;
  slottedPillarKeys: Record<string, boolean>;
  memoryPillarTexts: Record<string, string>;
  topicInputs: Record<string, string>;
  essayDraft: string;
  checklist: [boolean, boolean, boolean, boolean];
}

interface SavedWt2Submission {
  id: string;
  createdAt: string;
  overall: number;
  formulaScore?: number;
  bodyMode: Wt2BodyMode;
  templateId: Wt2TemplateId;
  topic: string;
  essay: string;
  wordCount: number;
  aiFeedback: any;
  pillar1Summary?: string;
  pillar2Summary?: string;
  b1IdeaCount?: MultiIdeaCount;
  b2IdeaCount?: MultiIdeaCount;
  multiPillars?: { 1: MultiBodyTuple; 2: MultiBodyTuple };
  linkers?: Record<string, string>;
  studioState?: Partial<Wt2StudioStateSnapshot>;
}

const WT2_LOCAL_GRADED_PREFIX = 'tony_wt2_graded_v1_';
const WT2_LOCAL_WIP_PREFIX = 'tony_wt2_wip_v1_';

function clampIdeaCount(val: any, fallback: MultiIdeaCount = 2): MultiIdeaCount {
  const n = Number(val);
  if (n >= 1 && n <= 5) return Math.round(n) as MultiIdeaCount;
  return fallback;
}

function normalizeSavedMultiSide(
  rawArr: any,
  count: MultiIdeaCount,
  defaultPol: 'positive' | 'negative',
  fallbackIds: [number, number, number, number, number]
): MultiBodyTuple {
  const recDepths = getRecommendedSentenceDepths(count);
  const src = Array.isArray(rawArr) ? rawArr : [];
  return [0, 1, 2, 3, 4].map((idx) => {
    const item = src[idx];
    const id =
      item && typeof item.id === 'number' && item.id >= 1 && item.id <= 19
        ? item.id
        : fallbackIds[idx];
    const polarity: 'positive' | 'negative' =
      item?.polarity === 'negative'
        ? 'negative'
        : item?.polarity === 'positive'
        ? 'positive'
        : defaultPol;
    const sentences: IdeaSentenceDepth =
      item?.sentences === 1 || item?.sentences === 2 ? item.sentences : recDepths[idx];
    return { id, polarity, sentences };
  }) as MultiBodyTuple;
}

function parseSavedSubmissionRow(row: any): SavedWt2Submission | null {
  if (!row) return null;
  let d = row.details;
  if (typeof d === 'string') {
    try {
      d = JSON.parse(d);
    } catch {
      return null;
    }
  }
  if (!d || d.mode !== 'wt2_pillar_studio' || !d.aiFeedback || !d.topic) return null;
  const tpl: Wt2TemplateId =
    d.templateId && WT2_STRUCTURES[d.templateId as Wt2TemplateId]
      ? (d.templateId as Wt2TemplateId)
      : 'discussion';
  const bodyMode: Wt2BodyMode = d.bodyMode === 'multi' ? 'multi' : 'single';
  const b1Cnt = clampIdeaCount(d.studioState?.b1IdeaCount ?? d.b1IdeaCount, 2);
  const b2Cnt = clampIdeaCount(d.studioState?.b2IdeaCount ?? d.b2IdeaCount, 2);
  const rawMulti = d.studioState?.multiPillars || d.multiPillars;

  return {
    id: String(row.id || `local_${row.created_at || Date.now()}`),
    createdAt: String(row.created_at || new Date().toISOString()),
    overall: Number(d.aiFeedback?.overall ?? row.score ?? 0),
    formulaScore:
      d.aiFeedback?.formulaScore !== undefined ? Number(d.aiFeedback.formulaScore) : undefined,
    bodyMode,
    templateId: tpl,
    topic: String(d.topic),
    essay: String(d.essay || d.studioState?.essayDraft || ''),
    wordCount: Number(d.wordCount || 0),
    aiFeedback: d.aiFeedback,
    pillar1Summary: typeof d.pillar1 === 'string' ? d.pillar1 : undefined,
    pillar2Summary: typeof d.pillar2 === 'string' ? d.pillar2 : undefined,
    b1IdeaCount: b1Cnt,
    b2IdeaCount: b2Cnt,
    multiPillars: rawMulti
      ? {
          1: normalizeSavedMultiSide(rawMulti[1], b1Cnt, 'positive', [1, 3, 5, 6, 7]),
          2: normalizeSavedMultiSide(rawMulti[2], b2Cnt, 'negative', [2, 4, 9, 10, 13])
        }
      : undefined,
    linkers: d.studioState?.linkers || d.linkers || undefined,
    studioState: d.studioState || undefined
  };
}

function readLocalGradedForTopic(uid: string, normTopic: string): SavedWt2Submission[] {
  try {
    const raw = localStorage.getItem(`${WT2_LOCAL_GRADED_PREFIX}${uid}`);
    if (!raw) return [];
    const arr = JSON.parse(raw);
    if (!Array.isArray(arr)) return [];
    return arr.filter(
      (item: SavedWt2Submission) =>
        item && item.aiFeedback && normalizeWt2TopicKey(item.topic) === normTopic
    );
  } catch {
    return [];
  }
}

function saveLocalGradedRecord(uid: string, rec: SavedWt2Submission): void {
  try {
    const key = `${WT2_LOCAL_GRADED_PREFIX}${uid}`;
    const raw = localStorage.getItem(key);
    const prev: SavedWt2Submission[] = raw ? JSON.parse(raw) : [];
    const filtered = Array.isArray(prev) ? prev.filter((x) => x && x.id !== rec.id) : [];
    const next = [rec, ...filtered].slice(0, 80);
    localStorage.setItem(key, JSON.stringify(next));
  } catch {
    // ignore storage quota errors
  }
}

function readLocalWipDraft(uid: string, normTopic: string): Partial<Wt2StudioStateSnapshot> | null {
  if (!normTopic) return null;
  try {
    const raw = localStorage.getItem(`${WT2_LOCAL_WIP_PREFIX}${uid}`);
    if (!raw) return null;
    const map = JSON.parse(raw);
    return map && typeof map === 'object' ? map[normTopic] || null : null;
  } catch {
    return null;
  }
}

function writeLocalWipDraft(
  uid: string,
  normTopic: string,
  snapshot: Wt2StudioStateSnapshot | null
): void {
  if (!normTopic) return;
  try {
    const key = `${WT2_LOCAL_WIP_PREFIX}${uid}`;
    const raw = localStorage.getItem(key);
    const map: Record<string, Wt2StudioStateSnapshot> =
      raw && typeof JSON.parse(raw) === 'object' ? JSON.parse(raw) : {};
    if (!snapshot) {
      delete map[normTopic];
    } else {
      delete map[normTopic];
      map[normTopic] = snapshot;
      const allKeys = Object.keys(map);
      while (allKeys.length > 40) {
        const oldest = allKeys.shift();
        if (oldest) delete map[oldest];
      }
    }
    localStorage.setItem(key, JSON.stringify(map));
  } catch {
    // ignore storage quota errors
  }
}

function formatSavedTimestamp(iso?: string): string {
  if (!iso) return '';
  const d = new Date(iso);
  if (isNaN(d.getTime())) return '';
  const pad = (n: number) => String(n).padStart(2, '0');
  return `${pad(d.getHours())}:${pad(d.getMinutes())} • ${pad(d.getDate())}/${pad(
    d.getMonth() + 1
  )}/${d.getFullYear()}`;
}

export const Wt2PillarStudioModal: React.FC<Wt2PillarStudioModalProps> = ({
  isOpen,
  onClose,
  payload,
  courseId,
  onMarkTaskComplete
}) => {
  const [step, setStep] = useState<1 | 2 | 3>(1);
  const [difficulty, setDifficulty] = useState<'level1' | 'level2'>('level1');
  const [bodyMode, setBodyMode] = useState<Wt2BodyMode>('single');
  const [showPillarTableDrawer, setShowPillarTableDrawer] = useState(false);
  const [drawerTierTab, setDrawerTierTab] = useState<1 | 2 | 3>(1);

  // Editable prompt support (when launched from Structure / Idea Pillars pages without a locked taskId)
  const [activeTopic, setActiveTopic] = useState<string>('');
  const [isEditingTopic, setIsEditingTopic] = useState<boolean>(false);

  // Category & Template configuration
  const isAutoCategory = !payload?.category || payload.category === 'auto';
  const [hasConfirmedCategory, setHasConfirmedCategory] = useState<boolean>(!isAutoCategory);
  const [showAutoGuide, setShowAutoGuide] = useState<boolean>(false);
  const [selectedCategory, setSelectedCategory] = useState<Wt2Category>('discussion');
  const [templateId, setTemplateId] = useState<Wt2TemplateId>('discussion');
  const [stance, setStance] = useState<'agree' | 'disagree'>('disagree');
  const [swapBodies, setSwapBodies] = useState<boolean>(false);

  const questionGuide = useMemo(
    () => detectWt2QuestionGuide(activeTopic || payload?.topic || ''),
    [activeTopic, payload?.topic]
  );

  // Phiên bản 1: 1 Pillar per Body (4 full PEEL sentences)
  const [pillar1Id, setPillar1Id] = useState<number>(1);
  const [pillar1Polarity, setPillar1Polarity] = useState<'positive' | 'negative'>('positive');
  const [pillar2Id, setPillar2Id] = useState<number>(2);
  const [pillar2Polarity, setPillar2Polarity] = useState<'positive' | 'negative'>('negative');

  // Phiên bản 2: 1–5 Pillars per Body + Linking Words (1–2 compact sentences per idea)
  const [b1IdeaCount, setB1IdeaCount] = useState<MultiIdeaCount>(2);
  const [b2IdeaCount, setB2IdeaCount] = useState<MultiIdeaCount>(2);
  const [multiPillars, setMultiPillars] = useState<{
    1: MultiBodyTuple;
    2: MultiBodyTuple;
  }>({
    1: [
      { id: 1, polarity: 'positive', sentences: 2 },
      { id: 3, polarity: 'positive', sentences: 2 },
      { id: 5, polarity: 'positive', sentences: 1 },
      { id: 6, polarity: 'positive', sentences: 1 },
      { id: 7, polarity: 'positive', sentences: 1 }
    ],
    2: [
      { id: 2, polarity: 'negative', sentences: 2 },
      { id: 4, polarity: 'negative', sentences: 2 },
      { id: 9, polarity: 'negative', sentences: 1 },
      { id: 10, polarity: 'negative', sentences: 1 },
      { id: 13, polarity: 'negative', sentences: 1 }
    ]
  });
  const [linkers, setLinkers] = useState<Record<string, string>>({ ...DEFAULT_LINKERS });

  // Interactive Slot State: key = makeSlotUnitKey(bodyIndex, col, ideaIndex) -> boolean
  const [slottedPillarKeys, setSlottedPillarKeys] = useState<Record<string, boolean>>({});
  // Level 2 Memory Mode custom typed text for pillar slots
  const [memoryPillarTexts, setMemoryPillarTexts] = useState<Record<string, string>>({});
  // Topic-specific short inputs: key = slotKey
  const [topicInputs, setTopicInputs] = useState<Record<string, string>>({});

  // Tap-to-place active card (works seamlessly on mobile/iPad & desktop alongside HTML5 drag-drop)
  const [selectedCard, setSelectedCard] = useState<{
    bodyIndex: 1 | 2;
    ideaIndex?: 1 | 2 | 3 | 4 | 5;
    col: PillarSlotType;
  } | null>(null);
  const [slotFeedback, setSlotFeedback] = useState<{ type: 'error' | 'ok'; msg: string } | null>(null);

  // Step 2: Editable essay, helper bank tab & checklist
  const [essayDraft, setEssayDraft] = useState<string>('');
  const [helperBankTab, setHelperBankTab] = useState<'subjects' | 'linkers'>('subjects');
  const [activeSubjectGroup, setActiveSubjectGroup] = useState<string>('age');
  const [activeLinkingGroup, setActiveLinkingGroup] = useState<string>('adding');
  const [checklist, setChecklist] = useState<[boolean, boolean, boolean, boolean]>([false, false, false, false]);
  const textareaRef = useRef<HTMLTextAreaElement | null>(null);

  // Step 3: AI Grading Result + Per-Topic Saved History
  const [isGrading, setIsGrading] = useState(false);
  const [gradeError, setGradeError] = useState<string | null>(null);
  const [aiEvaluation, setAiEvaluation] = useState<any | null>(null);
  const [taskMarkedDone, setTaskMarkedDone] = useState(false);
  const [currentUserId, setCurrentUserId] = useState<string>('guest');
  const [savedSubmissions, setSavedSubmissions] = useState<SavedWt2Submission[]>([]);
  const [selectedSavedId, setSelectedSavedId] = useState<string | null>(null);
  const [restoredDraftNotice, setRestoredDraftNotice] = useState<boolean>(false);
  const readyForWipSaveTopicRef = useRef<string>('');

  const applySavedSubmissionToState = (rec: SavedWt2Submission, jumpToStep3: boolean) => {
    const st = rec.studioState;
    const tpl: Wt2TemplateId =
      st?.templateId && WT2_STRUCTURES[st.templateId] ? st.templateId : rec.templateId;
    const cat: Wt2Category =
      st?.selectedCategory || WT2_STRUCTURES[tpl]?.category || 'discussion';
    const nextMode: Wt2BodyMode = st?.bodyMode || rec.bodyMode || 'single';
    const { pol1: defPol1, pol2: defPol2 } = defaultPolaritiesForTemplate(cat, tpl);

    setHasConfirmedCategory(true);
    setSelectedCategory(cat);
    setTemplateId(tpl);
    setBodyMode(nextMode);
    setSwapBodies(Boolean(st?.swapBodies));
    setHelperBankTab(nextMode === 'multi' ? 'linkers' : 'subjects');
    if (st?.stance) setStance(st.stance);
    if (st?.difficulty) setDifficulty(st.difficulty);

    // Restore Phiên bản 1 Pillars (either from studioState or parsed from legacy summary string)
    if (st?.pillar1Id) {
      setPillar1Id(st.pillar1Id);
      setPillar1Polarity(st.pillar1Polarity || defPol1);
    } else if (rec.pillar1Summary) {
      const m1 = rec.pillar1Summary.match(/^#(\d+)\b.*?\((positive|negative)\)/i);
      if (m1) {
        setPillar1Id(Number(m1[1]));
        setPillar1Polarity(m1[2].toLowerCase() === 'negative' ? 'negative' : 'positive');
      }
    }

    if (st?.pillar2Id) {
      setPillar2Id(st.pillar2Id);
      setPillar2Polarity(st.pillar2Polarity || defPol2);
    } else if (rec.pillar2Summary) {
      const m2 = rec.pillar2Summary.match(/^#(\d+)\b.*?\((positive|negative)\)/i);
      if (m2) {
        setPillar2Id(Number(m2[1]));
        setPillar2Polarity(m2[2].toLowerCase() === 'negative' ? 'negative' : 'positive');
      }
    }

    // Restore Phiên bản 2 Multi-Pillars & Linkers
    const b1Cnt = clampIdeaCount(st?.b1IdeaCount ?? rec.b1IdeaCount, 2);
    const b2Cnt = clampIdeaCount(st?.b2IdeaCount ?? rec.b2IdeaCount, 2);
    setB1IdeaCount(b1Cnt);
    setB2IdeaCount(b2Cnt);
    if (rec.multiPillars) {
      setMultiPillars(rec.multiPillars);
    }
    if (rec.linkers) {
      setLinkers({ ...DEFAULT_LINKERS, ...rec.linkers });
    }

    setSlottedPillarKeys(st?.slottedPillarKeys || {});
    setMemoryPillarTexts(st?.memoryPillarTexts || {});
    setTopicInputs(st?.topicInputs || {});
    setChecklist(st?.checklist || [true, true, true, true]);
    setEssayDraft(rec.essay || st?.essayDraft || '');
    setAiEvaluation(rec.aiFeedback);
    setSelectedSavedId(rec.id);
    setGradeError(null);
    setRestoredDraftNotice(false);
    if (jumpToStep3) {
      setStep(3);
    }
  };

  const resetInputsForTopic = (topicStr: string, keepSavedList: boolean) => {
    const autoMode = !payload?.category || payload.category === 'auto';
    const guide = detectWt2QuestionGuide(topicStr);
    const initCat: Wt2Category =
      !autoMode && payload?.category ? payload.category : guide.recommendedCategory;
    const initTpl = defaultTemplateForCategory(
      initCat,
      payload?.subType || (autoMode ? guide.recommendedTemplate : undefined)
    );
    const initBodyMode: Wt2BodyMode = payload?.bodyMode || 'single';
    const { pol1, pol2 } = defaultPolaritiesForTemplate(initCat, initTpl);

    setStep(1);
    setDrawerTierTab(1);
    setBodyMode(initBodyMode);
    setHelperBankTab(initBodyMode === 'multi' ? 'linkers' : 'subjects');
    setHasConfirmedCategory(!autoMode);
    setShowAutoGuide(false);
    setSelectedCategory(initCat);
    setTemplateId(initTpl);
    setStance('disagree');
    setSwapBodies(false);

    const p1 = payload?.presetPillar1 || guide.suggestedPillar1.id || (initCat === 'mixed' ? 12 : 1);
    const p2 = payload?.presetPillar2 || guide.suggestedPillar2.id || (initCat === 'mixed' ? 16 : 2);
    setPillar1Id(p1);
    setPillar2Id(p2);
    setPillar1Polarity(pol1);
    setPillar2Polarity(pol2);

    setB1IdeaCount(2);
    setB2IdeaCount(2);
    const gMulti = guide.suggestedMultiPillars;
    setMultiPillars({
      1: makeFiveSelections(gMulti.b1, payload?.presetPillar1, pol1, 2),
      2: makeFiveSelections(gMulti.b2, payload?.presetPillar2, pol2, 2)
    });
    setLinkers({ ...DEFAULT_LINKERS });

    setSlottedPillarKeys({});
    setMemoryPillarTexts({});
    setTopicInputs({});
    setSelectedCard(null);
    setSlotFeedback(null);
    setEssayDraft('');
    setChecklist([false, false, false, false]);
    setIsGrading(false);
    setGradeError(null);
    setAiEvaluation(null);
    setSelectedSavedId(null);
    setRestoredDraftNotice(false);
    if (!keepSavedList) {
      setSavedSubmissions([]);
      setTaskMarkedDone(false);
    }
  };

  const handleStartFreshAttempt = () => {
    const curTopic = activeTopic || payload?.topic || '';
    writeLocalWipDraft(currentUserId, normalizeWt2TopicKey(curTopic), null);
    resetInputsForTopic(curTopic, true);
  };

  // Reset state & auto-restore saved AI evaluation (or WIP draft) when modal opens with a payload
  useEffect(() => {
    if (!isOpen || !payload) return;
    let cancelled = false;
    const initTopic = payload.topic || '';
    readyForWipSaveTopicRef.current = '';
    setActiveTopic(initTopic);
    setIsEditingTopic(false);
    resetInputsForTopic(initTopic, false);

    const loadSavedForTopic = async (topicStr: string) => {
      const normTopic = normalizeWt2TopicKey(topicStr);
      if (!normTopic) {
        readyForWipSaveTopicRef.current = normTopic;
        return;
      }

      let uid = 'guest';
      try {
        const {
          data: { user }
        } = await supabase.auth.getUser();
        if (user?.id) uid = user.id;
      } catch {
        // fallback to guest local storage
      }
      if (cancelled) return;
      setCurrentUserId(uid);

      // 1. Read local graded cache first + query Supabase test_results for user
      const localList = readLocalGradedForTopic(uid, normTopic);
      let dbList: SavedWt2Submission[] = [];
      if (uid !== 'guest') {
        try {
          const { data: rows } = await supabase
            .from('test_results')
            .select('id, test_title, score, created_at, details')
            .eq('user_id', uid)
            .eq('test_type', 'IELTS-Writing')
            .order('created_at', { ascending: false })
            .limit(300);
          if (rows && Array.isArray(rows)) {
            dbList = rows
              .map(parseSavedSubmissionRow)
              .filter(
                (item): item is SavedWt2Submission =>
                  item !== null && normalizeWt2TopicKey(item.topic) === normTopic
              );
          }
        } catch {
          // ignore network errors and rely on localList
        }
      }
      if (cancelled) return;

      // Merge & deduplicate (DB records take priority over local cache with identical essay+score)
      const merged: SavedWt2Submission[] = [...dbList];
      for (const loc of localList) {
        const alreadyInDb = merged.some(
          (m) =>
            m.id === loc.id ||
            (m.essay.trim() === loc.essay.trim() && Number(m.overall) === Number(loc.overall))
        );
        if (!alreadyInDb) merged.push(loc);
      }
      merged.sort(
        (a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime()
      );

      if (merged.length > 0) {
        setSavedSubmissions(merged);
        // If caller forced a specific bodyMode (e.g. demo button on Page 5), prefer matching mode
        const preferred = payload.bodyMode
          ? merged.find((m) => m.bodyMode === payload.bodyMode)
          : merged[0];
        if (preferred) {
          applySavedSubmissionToState(preferred, true);
        }
        readyForWipSaveTopicRef.current = normTopic;
        return;
      }

      // 2. Otherwise restore un-submitted WIP draft if any exists for this topic
      const wip = readLocalWipDraft(uid, normTopic);
      if (wip) {
        const hasWork =
          Object.values(wip.topicInputs || {}).some((v) => String(v || '').trim().length > 0) ||
          Object.values(wip.slottedPillarKeys || {}).some(Boolean) ||
          Object.values(wip.memoryPillarTexts || {}).some((v) => String(v || '').trim().length > 0) ||
          String(wip.essayDraft || '').trim().length > 0;
        if (hasWork) {
          setHasConfirmedCategory(true);
          if (wip.selectedCategory) setSelectedCategory(wip.selectedCategory);
          if (wip.templateId && WT2_STRUCTURES[wip.templateId]) setTemplateId(wip.templateId);
          if (wip.stance) setStance(wip.stance);
          setSwapBodies(Boolean(wip.swapBodies));
          if (wip.difficulty) setDifficulty(wip.difficulty);
          if (wip.bodyMode) {
            setBodyMode(wip.bodyMode);
            setHelperBankTab(wip.bodyMode === 'multi' ? 'linkers' : 'subjects');
          }
          if (wip.pillar1Id) setPillar1Id(wip.pillar1Id);
          if (wip.pillar1Polarity) setPillar1Polarity(wip.pillar1Polarity);
          if (wip.pillar2Id) setPillar2Id(wip.pillar2Id);
          if (wip.pillar2Polarity) setPillar2Polarity(wip.pillar2Polarity);
          const b1Cnt = clampIdeaCount(wip.b1IdeaCount, 2);
          const b2Cnt = clampIdeaCount(wip.b2IdeaCount, 2);
          setB1IdeaCount(b1Cnt);
          setB2IdeaCount(b2Cnt);
          if (wip.multiPillars) {
            setMultiPillars({
              1: normalizeSavedMultiSide(wip.multiPillars[1], b1Cnt, 'positive', [1, 3, 5, 6, 7]),
              2: normalizeSavedMultiSide(wip.multiPillars[2], b2Cnt, 'negative', [2, 4, 9, 10, 13])
            });
          }
          if (wip.linkers) setLinkers({ ...DEFAULT_LINKERS, ...wip.linkers });
          if (wip.slottedPillarKeys) setSlottedPillarKeys(wip.slottedPillarKeys);
          if (wip.memoryPillarTexts) setMemoryPillarTexts(wip.memoryPillarTexts);
          if (wip.topicInputs) setTopicInputs(wip.topicInputs);
          if (wip.checklist) setChecklist(wip.checklist);
          if (wip.essayDraft) {
            setEssayDraft(wip.essayDraft);
            if (wip.essayDraft.trim().length > 0) setStep(2);
          }
          setRestoredDraftNotice(true);
        }
      }

      readyForWipSaveTopicRef.current = normTopic;
    };

    loadSavedForTopic(initTopic);
    return () => {
      cancelled = true;
    };
  }, [isOpen, payload]);

  // Auto-save WIP draft per topic whenever student works in Step 1 / Step 2 before AI grading
  useEffect(() => {
    if (!isOpen || !payload || isGrading || aiEvaluation) return;
    const curTopic = activeTopic || payload.topic || '';
    const normTopic = normalizeWt2TopicKey(curTopic);
    if (!normTopic || readyForWipSaveTopicRef.current !== normTopic) return;

    const hasAnyInput =
      Object.values(topicInputs).some((v) => v.trim().length > 0) ||
      Object.values(slottedPillarKeys).some(Boolean) ||
      Object.values(memoryPillarTexts).some((v) => v.trim().length > 0) ||
      essayDraft.trim().length > 0;

    if (!hasAnyInput) return;

    writeLocalWipDraft(currentUserId, normTopic, {
      selectedCategory,
      templateId,
      stance,
      difficulty,
      bodyMode,
      swapBodies,
      pillar1Id,
      pillar1Polarity,
      pillar2Id,
      pillar2Polarity,
      b1IdeaCount,
      b2IdeaCount,
      multiPillars,
      linkers,
      slottedPillarKeys,
      memoryPillarTexts,
      topicInputs,
      essayDraft,
      checklist
    });
  }, [
    isOpen,
    payload,
    isGrading,
    aiEvaluation,
    activeTopic,
    currentUserId,
    selectedCategory,
    templateId,
    stance,
    difficulty,
    bodyMode,
    swapBodies,
    pillar1Id,
    pillar1Polarity,
    pillar2Id,
    pillar2Polarity,
    b1IdeaCount,
    b2IdeaCount,
    multiPillars,
    linkers,
    slottedPillarKeys,
    memoryPillarTexts,
    topicInputs,
    essayDraft,
    checklist
  ]);

  const syncMultiPolarities = (pol1: 'positive' | 'negative', pol2: 'positive' | 'negative') => {
    setMultiPillars((prev) => ({
      1: prev[1].map((item) => ({ ...item, polarity: pol1 })) as MultiBodyTuple,
      2: prev[2].map((item) => ({ ...item, polarity: pol2 })) as MultiBodyTuple
    }));
  };

  const handleCategoryChange = (cat: Wt2Category) => {
    setHasConfirmedCategory(true);
    setSelectedCategory(cat);
    const nextTpl =
      cat === questionGuide.recommendedCategory
        ? questionGuide.recommendedTemplate
        : defaultTemplateForCategory(cat);
    setTemplateId(nextTpl);
    setSwapBodies(false);
    setSlottedPillarKeys({});
    setSelectedCard(null);
    const { pol1, pol2 } = defaultPolaritiesForTemplate(cat, nextTpl);
    setPillar1Polarity(pol1);
    setPillar2Polarity(pol2);
    syncMultiPolarities(pol1, pol2);
  };

  const handleApplyRecommendedGuide = () => {
    setShowAutoGuide(true);
    setHasConfirmedCategory(true);
    setSelectedCategory(questionGuide.recommendedCategory);
    setTemplateId(questionGuide.recommendedTemplate);
    setSwapBodies(false);
    setPillar1Id(questionGuide.suggestedPillar1.id);
    setPillar1Polarity(questionGuide.suggestedPillar1.polarity);
    setPillar2Id(questionGuide.suggestedPillar2.id);
    setPillar2Polarity(questionGuide.suggestedPillar2.polarity);
    setMultiPillars({
      1: makeFiveSelections(
        questionGuide.suggestedMultiPillars.b1,
        undefined,
        questionGuide.suggestedPillar1.polarity,
        b1IdeaCount
      ),
      2: makeFiveSelections(
        questionGuide.suggestedMultiPillars.b2,
        undefined,
        questionGuide.suggestedPillar2.polarity,
        b2IdeaCount
      )
    });
    setSlottedPillarKeys({});
    setSelectedCard(null);
  };

  const handleSwapBodies = () => {
    const nextSwap = !swapBodies;
    const nextRoles = getBodyRoleLabels(templateId, nextSwap);
    setSwapBodies(nextSwap);

    // Swap Phiên bản 1 Pillar IDs & Polarities
    const prevP1Id = pillar1Id;
    const prevP1Pol = pillar1Polarity;
    setPillar1Id(pillar2Id);
    setPillar1Polarity(pillar2Polarity);
    setPillar2Id(prevP1Id);
    setPillar2Polarity(prevP1Pol);

    // Swap Phiên bản 2 Idea Counts & Multi-Pillar Tuples
    const prevB1Cnt = b1IdeaCount;
    setB1IdeaCount(b2IdeaCount);
    setB2IdeaCount(prevB1Cnt);
    setMultiPillars((prev) => ({
      1: prev[2],
      2: prev[1]
    }));

    // Swap placed cards & Level 2 typed memory texts between Body 1 ('1_*') and Body 2 ('2_*')
    setSlottedPillarKeys((prev) => swapBodyPrefixMap(prev));
    setMemoryPillarTexts((prev) => swapBodyPrefixMap(prev));
    setSelectedCard(null);
    setSlotFeedback({
      type: 'ok',
      msg: `🔄 Đã đảo vị trí Body 1 ↔ Body 2 (${nextRoles.b1Short} → ${nextRoles.b2Short}) và tự động cập nhật câu cuối Mở bài + câu đầu Kết bài!`
    });
  };

  const handleBodyModeSwitch = (nextMode: Wt2BodyMode) => {
    if (nextMode === bodyMode) return;
    setBodyMode(nextMode);
    setSelectedCard(null);
    setSlotFeedback(null);
    setHelperBankTab(nextMode === 'multi' ? 'linkers' : 'subjects');
  };

  const changeBodyIdeaCount = (bodyIdx: 1 | 2, nextCount: MultiIdeaCount) => {
    if (bodyIdx === 1) {
      setB1IdeaCount(nextCount);
    } else {
      setB2IdeaCount(nextCount);
    }
    const recommended = getRecommendedSentenceDepths(nextCount);
    setMultiPillars((prev) => ({
      ...prev,
      [bodyIdx]: prev[bodyIdx].map((item, idx) => ({
        ...item,
        sentences: recommended[idx]
      })) as MultiBodyTuple
    }));
    setSelectedCard(null);
  };

  const applyBodySentencePreset = (
    bodyIdx: 1 | 2,
    preset: 'all1' | 'balanced' | 'all2'
  ) => {
    const count = bodyIdx === 1 ? b1IdeaCount : b2IdeaCount;
    const balanced = getRecommendedSentenceDepths(count);
    setMultiPillars((prev) => ({
      ...prev,
      [bodyIdx]: prev[bodyIdx].map((item, idx) => ({
        ...item,
        sentences:
          preset === 'all1' ? 1 : preset === 'all2' ? 2 : balanced[idx]
      })) as MultiBodyTuple
    }));
    setSelectedCard(null);
  };

  const updateMultiIdea = (
    bodyIdx: 1 | 2,
    ideaIdx: 1 | 2 | 3 | 4 | 5,
    patch: Partial<IdeaSelection>
  ) => {
    setMultiPillars((prev) => {
      const nextBody = [...prev[bodyIdx]] as MultiBodyTuple;
      nextBody[ideaIdx - 1] = { ...nextBody[ideaIdx - 1], ...patch };
      return { ...prev, [bodyIdx]: nextBody };
    });
    if (patch.id !== undefined) {
      setSlottedPillarKeys((prev) => ({
        ...prev,
        [makeSlotUnitKey(bodyIdx, 'pillar', ideaIdx)]: false,
        [makeSlotUnitKey(bodyIdx, 'compact_support', ideaIdx)]: false,
        [makeSlotUnitKey(bodyIdx, 'compact_single', ideaIdx)]: false
      }));
    }
  };

  const pillar1 = useMemo(
    () => WT2_PILLARS.find((p) => p.id === pillar1Id) || WT2_PILLARS[0],
    [pillar1Id]
  );
  const pillar2 = useMemo(
    () => WT2_PILLARS.find((p) => p.id === pillar2Id) || WT2_PILLARS[1],
    [pillar2Id]
  );

  const branch1 = pillar1[pillar1Polarity];
  const branch2 = pillar2[pillar2Polarity];

  const getPillarById = (id: number): Wt2Pillar =>
    WT2_PILLARS.find((p) => p.id === id) || WT2_PILLARS[0];

  const structureDef = WT2_STRUCTURES[templateId];
  const bodyRoles = useMemo(
    () => getBodyRoleLabels(templateId, swapBodies),
    [templateId, swapBodies]
  );

  const b1Specs = useMemo<MultiBodyIdeaSpec[]>(
    () =>
      multiPillars[1].slice(0, b1IdeaCount).map((sel, idx) => ({
        ideaIndex: (idx + 1) as 1 | 2 | 3 | 4 | 5,
        sentences: sel.sentences
      })),
    [multiPillars, b1IdeaCount]
  );

  const b2Specs = useMemo<MultiBodyIdeaSpec[]>(
    () =>
      multiPillars[2].slice(0, b2IdeaCount).map((sel, idx) => ({
        ideaIndex: (idx + 1) as 1 | 2 | 3 | 4 | 5,
        sentences: sel.sentences
      })),
    [multiPillars, b2IdeaCount]
  );

  const paragraphs = useMemo(() => {
    if (bodyMode === 'multi') {
      return buildMultiIdeaParagraphs(templateId, stance, b1Specs, b2Specs, swapBodies);
    }
    return structureDef.buildParagraphs(stance, swapBodies);
  }, [bodyMode, templateId, structureDef, stance, b1Specs, b2Specs, swapBodies]);

  const resolveBranch = (bodyIndex: 1 | 2, ideaIndex?: 1 | 2 | 3 | 4 | 5) => {
    if (ideaIndex) {
      const sel = multiPillars[bodyIndex][ideaIndex - 1];
      const p = getPillarById(sel.id);
      return p[sel.polarity];
    }
    return bodyIndex === 1 ? branch1 : branch2;
  };

  const getBranchValue = (
    bodyIndex: 1 | 2,
    col: PillarSlotType,
    ideaIndex?: 1 | 2 | 3 | 4 | 5
  ): string => {
    const b = resolveBranch(bodyIndex, ideaIndex);
    switch (col) {
      case 'pillar':
        return b.pillarSlot;
      case 'cause':
        return b.causeSlot;
      case 'effect':
        return b.effectSlot;
      case 'example':
        return b.exampleSlot;
      case 'compact_support':
        return b.compactSupportSlot.replace(/\.+$/, '');
      case 'compact_single':
        return b.compactOneSentenceSlot.replace(/\.+$/, '');
    }
  };

  const getBranchAnchor = (
    bodyIndex: 1 | 2,
    col: PillarSlotType,
    ideaIndex?: 1 | 2 | 3 | 4 | 5
  ): string => {
    const b = resolveBranch(bodyIndex, ideaIndex);
    if (col === 'compact_support' || col === 'compact_single') {
      return b.compactAnchor;
    }
    const idx = col === 'pillar' ? 0 : col === 'cause' ? 1 : col === 'effect' ? 2 : 3;
    return b.anchors[idx];
  };

  // Detect duplicate Pillar IDs within the same Body in Phiên bản 2
  const getDuplicatePillarWarning = (bodyIdx: 1 | 2): string | null => {
    const count = bodyIdx === 1 ? b1IdeaCount : b2IdeaCount;
    if (count < 2) return null;
    const activeIds = multiPillars[bodyIdx].slice(0, count).map((x) => x.id);
    if (new Set(activeIds).size < activeIds.length) {
      return `Body ${bodyIdx} đang chọn trùng Trụ ý giữa các ý! Em hãy chọn ${count} Trụ ý khác nhau để lập luận đa chiều nhé.`;
    }
    return null;
  };

  // Detect duplicate Linking Words within a Body or across Body 1 & Body 2 in Phiên bản 2
  const crossBodyLinkerWarning = useMemo(() => {
    if (bodyMode !== 'multi') return null;
    const b1Used = Array.from({ length: b1IdeaCount }, (_, idx) => {
      const role = getLinkerRoleForIdea((idx + 1) as 1 | 2 | 3 | 4 | 5, b1IdeaCount);
      return linkers[`b1_link_${role}`] || WT2_LINKER_ROLE_OPTIONS[role][0].en;
    });
    const b2Used = Array.from({ length: b2IdeaCount }, (_, idx) => {
      const role = getLinkerRoleForIdea((idx + 1) as 1 | 2 | 3 | 4 | 5, b2IdeaCount);
      return linkers[`b2_link_${role}`] || WT2_LINKER_ROLE_OPTIONS[role][0].en;
    });

    const dupInB1 = b1Used.filter((w, i) => b1Used.indexOf(w) !== i);
    const dupInB2 = b2Used.filter((w, i) => b2Used.indexOf(w) !== i);
    if (dupInB1.length > 0 || dupInB2.length > 0) {
      const words = Array.from(new Set([...dupInB1, ...dupInB2])).join(', ');
      return `Lưu ý Coherence: Từ nối "${words}" đang bị lặp lại ngay trong cùng 1 đoạn Body — em hãy chọn từ nối khác cho các ý tiếp theo nhé!`;
    }

    const overlap = Array.from(new Set(b1Used.filter((w) => b2Used.includes(w))));
    if (overlap.length > 0) {
      return `Mẹo Band 8.0+ Coherence: Từ nối "${overlap.join(', ')}" đang dùng lặp ở cả Body 1 và Body 2 — em nên đổi sang từ nối khác (VD: Furthermore ↔ Moreover / In addition) để ăn điểm đa dạng từ nối!`;
    }
    return null;
  }, [bodyMode, linkers, b1IdeaCount, b2IdeaCount]);

  // Required unique pillar slots in current template & mode
  const requiredPillarUnitKeys = useMemo(() => {
    const s = new Set<string>();
    paragraphs.forEach((p) =>
      p.tokens.forEach((t) => {
        if (t.type === 'pillar_slot' && t.bodyIndex && t.pillarCol) {
          s.add(makeSlotUnitKey(t.bodyIndex, t.pillarCol, t.ideaIndex));
        }
      })
    );
    return Array.from(s);
  }, [paragraphs]);

  const slottedCount = useMemo(
    () => requiredPillarUnitKeys.filter((k) => slottedPillarKeys[k]).length,
    [requiredPillarUnitKeys, slottedPillarKeys]
  );

  const attemptPlaceCard = (
    sourceBody: 1 | 2,
    sourceCol: PillarSlotType,
    targetBody: 1 | 2,
    targetCol: PillarSlotType,
    sourceIdea?: 1 | 2 | 3 | 4 | 5,
    targetIdea?: 1 | 2 | 3 | 4 | 5
  ) => {
    if (sourceBody !== targetBody) {
      setSlotFeedback({
        type: 'error',
        msg: `Thẻ này thuộc Trụ ý của Body ${sourceBody} — em hãy thả vào đoạn Body ${sourceBody} nhé!`
      });
      return;
    }
    if ((sourceIdea || 0) !== (targetIdea || 0)) {
      setSlotFeedback({
        type: 'error',
        msg: `Thẻ này thuộc Ý ${sourceIdea} của Body ${sourceBody} — em hãy thả vào đúng vị trí Ý ${sourceIdea} (không thả nhầm sang Ý ${targetIdea}) nhé!`
      });
      return;
    }
    if (sourceCol !== targetCol) {
      setSlotFeedback({
        type: 'error',
        msg: `Chưa khớp loại thẻ! Thẻ em chọn là [${COL_LABELS[sourceCol].badge}], còn ô này cần [${COL_LABELS[targetCol].badge}].`
      });
      return;
    }
    const unitKey = makeSlotUnitKey(targetBody, targetCol, targetIdea);
    setSlottedPillarKeys((prev) => ({ ...prev, [unitKey]: true }));
    setSelectedCard(null);
    setSlotFeedback({
      type: 'ok',
      msg: targetIdea
        ? `Chuẩn xác! Đã lắp thẻ [${COL_LABELS[targetCol].badge}] vào Body ${targetBody} • Ý ${targetIdea}.`
        : `Chuẩn xác! Đã lắp thẻ [${COL_LABELS[targetCol].badge}] vào Body ${targetBody}.`
    });
  };

  const handleAutoFillAllPillarSlots = () => {
    const next: Record<string, boolean> = {};
    requiredPillarUnitKeys.forEach((k) => {
      next[k] = true;
    });
    setSlottedPillarKeys((prev) => ({ ...prev, ...next }));
    setSlotFeedback({
      type: 'ok',
      msg:
        bodyMode === 'multi'
          ? 'Đã lắp toàn bộ các thẻ Trụ ý rút gọn (1–2 câu/ý) + Linking Words vào Khung bất biến Phiên bản 2!'
          : 'Đã lắp toàn bộ các thẻ Pillar vào đúng vị trí trong Khung bất biến!'
    });
  };

  // Assemble Step 1 into Step 2 editable draft
  const buildAssembledEssay = (): string => {
    return paragraphs
      .map((para) => {
        const raw = para.tokens
          .map((tok) => {
            if (tok.type === 'text') return tok.text || '';
            if (tok.type === 'linker_select' && tok.slotKey) {
              const role: LinkerRole = tok.linkerRole || 'start';
              return linkers[tok.slotKey] || WT2_LINKER_ROLE_OPTIONS[role][0].en;
            }
            if (tok.type === 'topic_input' && tok.slotKey) {
              const val = (topicInputs[tok.slotKey] || '').trim();
              return val || `[${tok.placeholder || 'nội dung theo đề'}]`;
            }
            if (tok.type === 'pillar_slot' && tok.bodyIndex && tok.pillarCol) {
              const unitKey = makeSlotUnitKey(tok.bodyIndex, tok.pillarCol, tok.ideaIndex);
              if (difficulty === 'level2') {
                const typed = (memoryPillarTexts[unitKey] || '').trim().replace(/\.+$/, '');
                return (
                  typed ||
                  `[Viết từ mỏ neo: ${getBranchAnchor(tok.bodyIndex, tok.pillarCol, tok.ideaIndex)}]`
                );
              }
              if (slottedPillarKeys[unitKey]) {
                return getBranchValue(tok.bodyIndex, tok.pillarCol, tok.ideaIndex);
              }
              return `[${tok.placeholder || COL_LABELS[tok.pillarCol].badge}]`;
            }
            return '';
          })
          .join('');
        return raw
          .replace(/\s+\./g, '.')
          .replace(/\.{2,}/g, '.')
          .replace(/\s+,/g, ',')
          .replace(/\s{2,}/g, ' ')
          .trim();
      })
      .join('\n\n');
  };

  const handleProceedToStep2 = () => {
    if (!hasConfirmedCategory) {
      alert('Em hãy đọc câu hỏi cuối đề bài và bấm chọn 1 trong 5 Dạng bài ở Bước 1A trước nhé!');
      return;
    }
    const assembled = buildAssembledEssay();
    // Only overwrite if draft is empty or user confirms replacing
    if (!essayDraft.trim() || window.confirm('Cập nhật lại bản nháp Bước 2 theo các ô vừa ghép ở Bước 1?')) {
      setEssayDraft(assembled);
    }
    setStep(2);
  };

  // Step 2: Live Seam & Quality Diagnostics
  const wordCount = useMemo(() => {
    const trimmed = essayDraft.trim();
    if (!trimmed) return 0;
    return trimmed.split(/\s+/).length;
  }, [essayDraft]);

  const bracketWarnings = useMemo(() => {
    const matches = essayDraft.match(/\[[^\]]+\]/g);
    return matches ? Array.from(new Set(matches)) : [];
  }, [essayDraft]);

  const duplicateConnectorWarnings = useMemo(() => {
    const low = essayDraft.toLowerCase();
    const found: string[] = [];
    if (low.includes('because of the fact that this is because')) found.push('Lặp "because of the fact that this is because"');
    if (low.includes('as a result, as a result')) found.push('Lặp "As a result, as a result"');
    if (low.includes('consequently, consequently') || low.includes('consequently, as a result'))
      found.push('Lặp từ nối kết quả (Consequently + As a result)');
    if (low.includes('for instance, for example') || low.includes('for example, for instance'))
      found.push('Lặp từ nối ví dụ (For instance + For example)');

    const trackedLinkers = [
      'specifically,',
      'in particular,',
      'notably,',
      'firstly,',
      'to begin with,',
      'first and foremost,',
      'furthermore,',
      'moreover,',
      'in addition,',
      'additionally,',
      'besides this,',
      'beyond this,',
      'equally importantly,',
      'what is more,',
      'on top of that,',
      'finally,',
      'last but not least,',
      'ultimately,'
    ];
    trackedLinkers.forEach((lk) => {
      const escaped = lk.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const hits = low.match(new RegExp(`\\b${escaped}`, 'g'));
      if (hits && hits.length >= 2) {
        found.push(`Lặp từ nối "${lk}" (${hits.length} lần — nên đổi từ nối khác để đa dạng Coherence)`);
      }
    });
    return found;
  }, [essayDraft]);

  const highlightBracketInEditor = (tag: string) => {
    const el = textareaRef.current;
    if (!el) return;
    const idx = essayDraft.indexOf(tag);
    if (idx >= 0) {
      el.focus();
      el.setSelectionRange(idx, idx + tag.length);
    }
  };

  const insertSubjectAtCursor = (word: string) => {
    const el = textareaRef.current;
    if (!el) {
      setEssayDraft((prev) => `${prev} ${word}`);
      return;
    }
    const start = el.selectionStart ?? essayDraft.length;
    const end = el.selectionEnd ?? essayDraft.length;
    const next = essayDraft.slice(0, start) + word + essayDraft.slice(end);
    setEssayDraft(next);
    setTimeout(() => {
      el.focus();
      el.setSelectionRange(start + word.length, start + word.length);
    }, 10);
  };

  // Step 3: Submit to AI Grader Edge Function
  const handleSubmitToAiGrader = async () => {
    if (wordCount < 80) {
      alert('Bài viết còn quá ngắn. Em hãy hoàn thiện các đoạn và tự biên tập trước khi nộp chấm AI nhé!');
      return;
    }
    setStep(3);
    setIsGrading(true);
    setGradeError(null);

    const topicToGrade = (activeTopic || payload?.topic || '').trim();
    const b1MultiDesc = multiPillars[1]
      .slice(0, b1IdeaCount)
      .map((sel, idx) => {
        const ideaIdx = (idx + 1) as 1 | 2 | 3 | 4 | 5;
        const role = getLinkerRoleForIdea(ideaIdx, b1IdeaCount);
        const p = getPillarById(sel.id);
        const lk = linkers[`b1_link_${role}`] || WT2_LINKER_ROLE_OPTIONS[role][0].en;
        return `Ý 1.${ideaIdx} [${lk} • ${sel.sentences} câu]: ${p.code} ${p.name} (${sel.polarity === 'positive' ? '+' : '-'})`;
      })
      .join(' | ');
    const b2MultiDesc = multiPillars[2]
      .slice(0, b2IdeaCount)
      .map((sel, idx) => {
        const ideaIdx = (idx + 1) as 1 | 2 | 3 | 4 | 5;
        const role = getLinkerRoleForIdea(ideaIdx, b2IdeaCount);
        const p = getPillarById(sel.id);
        const lk = linkers[`b2_link_${role}`] || WT2_LINKER_ROLE_OPTIONS[role][0].en;
        return `Ý 2.${ideaIdx} [${lk} • ${sel.sentences} câu]: ${p.code} ${p.name} (${sel.polarity === 'positive' ? '+' : '-'})`;
      })
      .join(' | ');

    try {
      const orderLine = swapBodies
        ? `- Thứ tự thân bài: ĐÃ ĐẢO VỊ TRÍ BODY 1 ↔ BODY 2 (${bodyRoles.orderHint} — câu cuối Mở bài và câu đầu Kết bài cũng được đảo tương ứng)`
        : `- Thứ tự thân bài: ${bodyRoles.orderHint}`;

      const formulaBlock =
        bodyMode === 'multi'
          ? `- Chế độ luyện: PHIÊN BẢN 2 — LINH HOẠT 1–5 TRỤ Ý / BODY + LINKING WORDS (Mỗi Trụ ý rút gọn súc tích 1–2 câu thay vì 4 câu PEEL)
- Khung bất biến áp dụng: ${structureDef.name}
${orderLine}
- Body 1 (${bodyRoles.b1Short} • ${b1IdeaCount} Trụ ý): ${b1MultiDesc}
- Body 2 (${bodyRoles.b2Short} • ${b2IdeaCount} Trụ ý): ${b2MultiDesc}`
          : `- Chế độ luyện: PHIÊN BẢN 1 — 1 TRỤ Ý SÂU / BODY (Triển khai 4 câu PEEL: Giới thiệu → Nhân → Quả → Ví dụ)
- Khung bất biến áp dụng: ${structureDef.name}
${orderLine}
- Trụ ý Body 1 (${bodyRoles.b1Short}): ${pillar1.code} ${pillar1.name} (${branch1.label})
- Trụ ý Body 2 (${bodyRoles.b2Short}): ${pillar2.code} ${pillar2.name} (${branch2.label})`;

      const swapHint = swapBodies
        ? ' Lưu ý học viên đang chủ động ĐẢO VỊ TRÍ BODY 1 ↔ BODY 2 (đẩy vế nhiều ý/quan trọng hơn xuống Body 2), hãy kiểm tra xem câu cuối Mở bài và câu đầu Kết bài đã khớp thứ tự đã đảo chưa.'
        : '';

      const reviewJsonHint =
        bodyMode === 'multi'
          ? `  "formulaReview": {
    "structureCheck": "Nhận xét xem ${isAutoCategory ? `em nhận diện dạng bài (${structureDef.name}) đã khớp câu hỏi đề chưa, và ` : ''}em đã có Câu mở đoạn (Topic Sentence chia chuẩn số ít cho đoạn 1 ý / số nhiều cho đoạn 2–5 ý) + giữ chuẩn Khung bất biến Phiên bản 2 của dạng ${structureDef.name} chưa...${swapHint}",
    "pillarFitCheck": "Nhận xét xem các Trụ ý ở Body 1 (${b1IdeaCount} ý) và Body 2 (${b2IdeaCount} ý) đã bám sát đề bài, triển khai gọn 1–2 câu/ý súc tích (cân đối độ dài đoạn văn, không bị liệt kê cụt ngủn cũng không bị lan man quá dài) chưa...",
    "seamGrammarCheck": "Nhận xét cách dùng bộ Linking Words (Specifically / Firstly / To begin with / Furthermore / Moreover / In addition / Beyond this / Finally...) đã hợp vai trò, không lặp từ nối và ngữ pháp tại các mối nối đã mượt tự nhiên chưa..."
  },`
          : `  "formulaReview": {
    "structureCheck": "Nhận xét xem ${isAutoCategory ? `em nhận diện dạng bài (${structureDef.name}) đã khớp với yêu cầu câu hỏi của đề chưa, và ` : ''}em đã giữ đúng Khung bất biến của dạng ${structureDef.name} chưa...${swapHint}",
    "pillarFitCheck": "Nhận xét xem 2 Trụ ý (${pillar1.name} & ${pillar2.name}) em chọn và ví dụ đưa vào đã bám sát đề bài chưa...",
    "seamGrammarCheck": "Nhận xét các mối nối ngữ pháp (sau due to / related to / chủ ngữ S / từ nối) đã mượt tự nhiên chưa và chỉ cách gọt..."
  },`;

      const prompt = `
Bạn là Giám khảo IELTS Writing chấm bài kiêm Thầy giáo hướng dẫn phương pháp "Khung Cấu Trúc Bất Biến + Bảng 19 Idea Pillars" của hệ thống TonyEnglish.
QUY TẮC XƯNG HÔ BẮT BUỘC: Xưng "Thầy" và gọi học viên là "em" (TUYỆT ĐỐI KHÔNG xưng "tôi/bạn" hay "con"). Nhận xét ân cần, khích lệ, chỉ rõ điểm làm tốt và cách sửa mượt hơn.

1. ĐỀ BÀI IELTS WRITING TASK 2:
"""
${topicToGrade}
"""

2. CÔNG THỨC TONYENGLISH HỌC VIÊN ĐANG LUYỆN:
${formulaBlock}

3. BÀI LÀM SAU KHI GHÉP & TỰ BIÊN TẬP CỦA HỌC VIÊN (${wordCount} từ):
"""
${essayDraft}
"""

Hãy chấm kép bài làm trên (vừa theo 4 tiêu chí IELTS chuẩn, vừa theo độ nhuần nhuyễn khi lắp Khung bất biến + Trụ ý Pillars theo đúng Phiên bản học viên đang luyện) và trả về ĐÚNG ĐỊNH DẠNG JSON THUẦN TÚY SAU (KHÔNG bọc markdown \`\`\`json):
{
  "overall": 7.0,
  "formulaScore": 8.5,
${reviewJsonHint}
  "criteria": [
    { "name": "Task Response", "score": 7.0, "comment": "Nhận xét tiếng Việt..." },
    { "name": "Coherence & Cohesion", "score": 7.5, "comment": "Nhận xét tiếng Việt..." },
    { "name": "Lexical Resource", "score": 7.0, "comment": "Nhận xét tiếng Việt..." },
    { "name": "Grammatical Range & Accuracy", "score": 7.0, "comment": "Nhận xét tiếng Việt..." }
  ],
  "correctedHtml": "Toàn bộ bài làm của học viên giữ chia đoạn bằng thẻ <br/><br/>, trong đó các chỗ sai ngữ pháp/còn gượng hoặc còn sót ký hiệu nháp được bọc bằng <span class='bg-red-100 text-red-700 line-through px-1 rounded'>cụm chưa chuẩn</span> kèm ngay sau đó là <span class='bg-emerald-100 text-emerald-800 font-bold px-1 rounded'>cụm sửa mượt chuẩn Band 8.0+</span>.",
  "generalFeedback": "Lời khuyên tổng kết ngắn gọn 2-3 câu của Thầy giúp em nhớ sâu công thức này khi vào phòng thi."
}
      `.trim();

      const { data, error } = await supabase.functions.invoke('ai-grader', {
        body: {
          prompt,
          imageUrls: [],
          model: 'gemini-2.5-pro'
        }
      });

      if (error) throw new Error(error.message);
      if (data?.error) throw new Error(data.error);

      const cleaned = String(data.result || '')
        .replace(/```(json)?/gi, '')
        .trim();
      const parsed = JSON.parse(cleaned);
      setAiEvaluation(parsed);

      // Save practice record + full studio snapshot to test_results & local cache
      const studioSnapshot: Wt2StudioStateSnapshot = {
        selectedCategory,
        templateId,
        stance,
        difficulty,
        bodyMode,
        swapBodies,
        pillar1Id,
        pillar1Polarity,
        pillar2Id,
        pillar2Polarity,
        b1IdeaCount,
        b2IdeaCount,
        multiPillars,
        linkers,
        slottedPillarKeys,
        memoryPillarTexts,
        topicInputs,
        essayDraft,
        checklist
      };

      const p1Summary =
        bodyMode === 'multi'
          ? b1MultiDesc
          : `${pillar1.code} ${pillar1.name} (${pillar1Polarity})`;
      const p2Summary =
        bodyMode === 'multi'
          ? b2MultiDesc
          : `${pillar2.code} ${pillar2.name} (${pillar2Polarity})`;

      let savedId = `local_${Date.now()}`;
      let savedCreatedAt = new Date().toISOString();
      let uid = currentUserId;

      const {
        data: { user }
      } = await supabase.auth.getUser();
      if (user) {
        uid = user.id;
        setCurrentUserId(uid);
        const { data: inserted } = await supabase
          .from('test_results')
          .insert([
            {
              user_id: user.id,
              course_id: courseId || null,
              test_title: `[WT2 Pillars ${bodyMode === 'multi' ? 'V2-Multi' : 'V1-PEEL'}] ${payload?.label || structureDef.name}`,
              test_type: 'IELTS-Writing',
              score: parsed.overall || 0,
              total_score: 9,
              time_spent: 0,
              details: {
                mode: 'wt2_pillar_studio',
                bodyMode,
                topic: topicToGrade,
                templateId,
                pillar1: p1Summary,
                pillar2: p2Summary,
                ...(bodyMode === 'multi'
                  ? { b1IdeaCount, b2IdeaCount, multiPillars, linkers }
                  : {}),
                essay: essayDraft,
                wordCount,
                aiFeedback: parsed,
                studioState: studioSnapshot
              }
            }
          ])
          .select('id, created_at')
          .single();

        if (inserted?.id) savedId = String(inserted.id);
        if (inserted?.created_at) savedCreatedAt = String(inserted.created_at);
      }

      const newSavedRec: SavedWt2Submission = {
        id: savedId,
        createdAt: savedCreatedAt,
        overall: Number(parsed.overall || 0),
        formulaScore:
          parsed.formulaScore !== undefined ? Number(parsed.formulaScore) : undefined,
        bodyMode,
        templateId,
        topic: topicToGrade,
        essay: essayDraft,
        wordCount,
        aiFeedback: parsed,
        pillar1Summary: p1Summary,
        pillar2Summary: p2Summary,
        b1IdeaCount,
        b2IdeaCount,
        multiPillars,
        linkers,
        studioState: studioSnapshot
      };

      saveLocalGradedRecord(uid, newSavedRec);
      writeLocalWipDraft(uid, normalizeWt2TopicKey(topicToGrade), null);
      setRestoredDraftNotice(false);
      setSavedSubmissions((prev) => [
        newSavedRec,
        ...prev.filter((x) => x.id !== newSavedRec.id)
      ]);
      setSelectedSavedId(newSavedRec.id);

      window.dispatchEvent(
        new CustomEvent('tony-wt2-graded', {
          detail: {
            topic: topicToGrade,
            overall: Number(parsed.overall || 0),
            formulaScore: parsed.formulaScore
          }
        })
      );

      // Auto-tick lecture task if taskId provided
      if (payload?.taskId && onMarkTaskComplete && !taskMarkedDone) {
        onMarkTaskComplete(payload.taskId);
        setTaskMarkedDone(true);
      }
    } catch (err: any) {
      console.error('WT2 Pillar AI Grader error:', err);
      setGradeError(err?.message || 'Không thể kết nối máy chủ chấm bài AI. Em vui lòng thử lại nhé!');
    } finally {
      setIsGrading(false);
    }
  };

  if (!isOpen || !payload) return null;

  return (
    <div className="fixed inset-0 z-[120] bg-slate-900/70 backdrop-blur-xs flex items-center justify-center p-2 sm:p-4 overflow-y-auto">
      <div className="bg-slate-50 w-full max-w-6xl rounded-2xl shadow-2xl border border-slate-200 flex flex-col max-h-[94vh] overflow-hidden">
        {/* ==================== STICKY HEADER ==================== */}
        <div className="bg-gradient-to-r from-[#0a5482] via-[#0d6efd] to-[#2563eb] text-white px-4 sm:px-6 py-3.5 flex flex-wrap items-center justify-between gap-3 shrink-0">
          <div className="flex items-center gap-2.5 min-w-0">
            <span className="text-xl">✍️</span>
            <div className="min-w-0">
              <div className="flex items-center gap-2 flex-wrap">
                <h2 className="font-extrabold text-base sm:text-lg tracking-tight truncate">
                  Phòng Luyện Ghép Khung Bất Biến + Idea Pillars
                </h2>
                {payload.label && (
                  <span className="bg-white/20 text-white text-xs font-bold px-2.5 py-0.5 rounded-full">
                    {payload.label}
                  </span>
                )}
              </div>
              <p className="text-xs text-sky-100 hidden sm:block">
                3 bước chuẩn phòng thi: Chọn &amp; Kéo thả Pillars → Tự mài mượt mối nối → Giám khảo AI chấm kép
              </p>
            </div>
          </div>

          {/* Stepper Pills */}
          <div className="flex items-center gap-1.5 bg-slate-950/25 p-1 rounded-xl">
            {[
              { n: 1 as const, label: '1. Ghép Khung + Pillars' },
              { n: 2 as const, label: '2. Tự Edit Mối Nối' },
              { n: 3 as const, label: '3. Chấm AI Kép' }
            ].map((s) => (
              <button
                key={s.n}
                onClick={() => {
                  if (s.n === 1) setStep(1);
                  if (s.n === 2) {
                    if (!hasConfirmedCategory) {
                      alert('Em hãy chọn 1 trong 5 Dạng bài ở Bước 1A để mở Khung bất biến trước nhé!');
                      return;
                    }
                    if (!essayDraft.trim()) setEssayDraft(buildAssembledEssay());
                    setStep(2);
                  }
                  if (s.n === 3) {
                    if (aiEvaluation) {
                      setStep(3);
                    } else if (savedSubmissions.length > 0) {
                      applySavedSubmissionToState(savedSubmissions[0], true);
                    }
                  }
                }}
                className={`px-2.5 sm:px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${
                  step === s.n
                    ? 'bg-white text-[#0a5482] shadow-xs'
                    : s.n === 3 && !aiEvaluation && savedSubmissions.length === 0
                    ? 'text-white/50 cursor-not-allowed'
                    : 'text-white/90 hover:bg-white/15'
                }`}
              >
                {s.label}
              </button>
            ))}
          </div>

          <button
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-white/15 hover:bg-white/30 flex items-center justify-center text-white font-bold text-lg cursor-pointer"
            title="Đóng"
          >
            ✕
          </button>
        </div>

        {/* ==================== PROMPT BANNER + MODE BAR ==================== */}
        <div className="bg-amber-50 border-b border-amber-200 px-4 sm:px-6 py-3 flex flex-col lg:flex-row lg:items-center justify-between gap-3 shrink-0">
          <div className="text-sm text-slate-800 leading-relaxed flex-1 space-y-1.5">
            <div className="flex flex-wrap items-center gap-1.5">
              <span className="inline-block bg-amber-500 text-white text-[11px] font-extrabold uppercase px-2 py-0.5 rounded">
                Đề bài
              </span>
              {!isEditingTopic && (
                <span className="font-semibold">{activeTopic || payload.topic}</span>
              )}
              {!payload.taskId && (
                <button
                  type="button"
                  onClick={() => {
                    if (isEditingTopic) {
                      setIsEditingTopic(false);
                      const nextNorm = normalizeWt2TopicKey(activeTopic);
                      if (nextNorm && nextNorm !== readyForWipSaveTopicRef.current) {
                        readyForWipSaveTopicRef.current = nextNorm;
                        resetInputsForTopic(activeTopic, false);
                        const locHits = readLocalGradedForTopic(currentUserId, nextNorm);
                        if (locHits.length > 0) {
                          setSavedSubmissions(locHits);
                          applySavedSubmissionToState(locHits[0], true);
                        }
                      }
                    } else {
                      setIsEditingTopic(true);
                    }
                  }}
                  className="ml-1 px-2 py-0.5 rounded-md bg-white border border-amber-300 hover:bg-amber-100 text-[11px] font-bold text-amber-900 cursor-pointer"
                  title="Tự nhập đề IELTS Task 2 bất kỳ để luyện ghép"
                >
                  {isEditingTopic ? '✓ Xong đề bài' : '✏️ Đổi đề khác'}
                </button>
              )}
            </div>
            {isEditingTopic && !payload.taskId && (
              <textarea
                rows={2}
                value={activeTopic}
                onChange={(e) => setActiveTopic(e.target.value)}
                placeholder="Dán hoặc gõ đề bài IELTS Writing Task 2 bất kỳ vào đây..."
                className="w-full rounded-lg border border-amber-300 bg-white px-3 py-1.5 text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-amber-500"
              />
            )}
          </div>

          <div className="flex items-center gap-2 shrink-0 flex-wrap">
            <div className="inline-flex rounded-lg border border-amber-300 bg-white p-0.5 text-xs font-bold">
              <button
                onClick={() => setDifficulty('level1')}
                className={`px-2.5 py-1 rounded-md cursor-pointer transition-all ${
                  difficulty === 'level1'
                    ? 'bg-sky-600 text-white'
                    : 'text-slate-600 hover:bg-slate-100'
                }`}
                title="Hiện đầy đủ câu chữ bảng Pillars để kéo thả"
              >
                📖 Level 1: Có câu gợi ý
              </button>
              <button
                onClick={() => setDifficulty('level2')}
                className={`px-2.5 py-1 rounded-md cursor-pointer transition-all ${
                  difficulty === 'level2'
                    ? 'bg-purple-600 text-white'
                    : 'text-slate-600 hover:bg-slate-100'
                }`}
                title="Chỉ hiện Từ khóa mỏ neo để luyện thuộc lòng phòng thi"
              >
                {bodyMode === 'multi'
                  ? '🧠 Level 2: Thuộc lòng (Mỏ neo gọn)'
                  : '🧠 Level 2: Thuộc lòng (4 Mỏ neo)'}
              </button>
            </div>

            {difficulty === 'level1' && (
              <button
                onClick={() => setShowPillarTableDrawer((v) => !v)}
                className="px-3 py-1.5 rounded-lg bg-white border border-sky-300 text-sky-700 hover:bg-sky-50 text-xs font-bold cursor-pointer shadow-2xs"
              >
                {showPillarTableDrawer ? 'Ẩn bảng 19 Trụ ý ▲' : '🟢🔵🟣 Bảng 19 Trụ ý (3 bảng ưu tiên)'}
              </button>
            )}
          </div>
        </div>

        {/* ==================== OPTIONAL 19-PILLAR QUICK DRAWER (3 COLOR-CODED PRIORITY TABS) ==================== */}
        {showPillarTableDrawer && difficulty === 'level1' && (() => {
          const activeMeta = PILLAR_TIER_META[drawerTierTab];
          const getTierAssignedBadge = (tier: 1 | 2 | 3): string | null => {
            if (bodyMode === 'single') {
              const tags: string[] = [];
              if (pillar1.tier === tier) tags.push(`B1(${pillar1.code})`);
              if (pillar2.tier === tier) tags.push(`B2(${pillar2.code})`);
              return tags.length > 0 ? `✓ ${tags.join(' • ')}` : null;
            }
            const usedB1 = multiPillars[1]
              .slice(0, b1IdeaCount)
              .filter((s) => (WT2_PILLARS.find((x) => x.id === s.id)?.tier ?? 1) === tier).length;
            const usedB2 = multiPillars[2]
              .slice(0, b2IdeaCount)
              .filter((s) => (WT2_PILLARS.find((x) => x.id === s.id)?.tier ?? 1) === tier).length;
            const total = usedB1 + usedB2;
            return total > 0 ? `✓ Đang chọn ${total} ý` : null;
          };

          return (
            <div className="bg-white border-b border-slate-200 px-4 sm:px-6 py-3 max-h-96 overflow-y-auto shrink-0 space-y-2.5">
              {/* Top Priority Rule Strip */}
              <div className="flex flex-wrap items-center justify-between gap-2">
                <div className="text-xs text-slate-600 font-semibold leading-snug">
                  <span className="font-extrabold uppercase text-slate-800 mr-1.5">
                    Thứ tự ưu tiên nhặt ý:
                  </span>
                  <span className="font-bold text-[#19692c]">1. Bảng Xanh Lá</span> →{' '}
                  <span className="font-bold text-[#0056b3]">2. Bảng Xanh Da Trời</span> →{' '}
                  <span className="font-bold text-[#533094]">3. Bảng Tím (Dự phòng)</span>
                  <span className="hidden md:inline text-slate-500">
                    {' '}
                    • Chủ yếu chỉ cần thuộc lòng Bảng Xanh Lá &amp; Xanh Da Trời!
                  </span>
                </div>
                <button
                  onClick={() => setShowPillarTableDrawer(false)}
                  className="text-xs font-bold text-slate-500 hover:text-slate-800 cursor-pointer shrink-0"
                >
                  Đóng bảng ▲
                </button>
              </div>

              {/* Quick 1–5 Idea Count Selector right inside Drawer when Phiên bản 2 is active */}
              {bodyMode === 'multi' && (
                <div className="bg-indigo-50/80 border border-indigo-200 rounded-lg px-3 py-1.5 flex flex-wrap items-center justify-between gap-2 text-xs">
                  <span className="font-extrabold text-indigo-950">
                    🔗 Phiên bản 2 • Chỉnh nhanh số ý mỗi Body (Min 1 – Max 5):
                  </span>
                  <div className="flex flex-wrap items-center gap-3">
                    <div className="flex items-center gap-1">
                      <span className="font-bold text-violet-800 text-[11px]">Body 1:</span>
                      <div className="inline-flex rounded-md border border-violet-300 bg-white overflow-hidden">
                        {([1, 2, 3, 4, 5] as const).map((n) => (
                          <button
                            key={`drw_b1_${n}`}
                            type="button"
                            onClick={() => changeBodyIdeaCount(1, n)}
                            className={`px-2 py-0.5 text-[11px] font-extrabold cursor-pointer ${
                              b1IdeaCount === n
                                ? 'bg-violet-600 text-white'
                                : 'text-violet-800 hover:bg-violet-50'
                            }`}
                          >
                            {n} ý
                          </button>
                        ))}
                      </div>
                    </div>
                    <div className="flex items-center gap-1">
                      <span className="font-bold text-amber-800 text-[11px]">Body 2:</span>
                      <div className="inline-flex rounded-md border border-amber-300 bg-white overflow-hidden">
                        {([1, 2, 3, 4, 5] as const).map((n) => (
                          <button
                            key={`drw_b2_${n}`}
                            type="button"
                            onClick={() => changeBodyIdeaCount(2, n)}
                            className={`px-2 py-0.5 text-[11px] font-extrabold cursor-pointer ${
                              b2IdeaCount === n
                                ? 'bg-amber-500 text-white'
                                : 'text-amber-800 hover:bg-amber-50'
                            }`}
                          >
                            {n} ý
                          </button>
                        ))}
                      </div>
                    </div>
                    <button
                      type="button"
                      onClick={handleSwapBodies}
                      className={`px-2.5 py-0.5 rounded-md border text-[11px] font-extrabold cursor-pointer transition-colors ${
                        swapBodies
                          ? 'bg-emerald-600 text-white border-emerald-700'
                          : 'bg-white text-indigo-800 border-indigo-300 hover:bg-indigo-100'
                      }`}
                      title="Đảo vị trí Body 1 ↔ Body 2 (tự động đổi câu cuối Mở bài & câu đầu Kết bài)"
                    >
                      🔄 Đảo B1 ↔ B2
                    </button>
                  </div>
                </div>
              )}

              {/* 3 Color-Coded Inner Tabs (#28a745 Green | #007bff Sky Blue | #6f42c1 Purple) */}
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-1.5">
                {([1, 2, 3] as const).map((tier) => {
                  const meta = PILLAR_TIER_META[tier];
                  const isActive = drawerTierTab === tier;
                  const assignedBadge = getTierAssignedBadge(tier);
                  return (
                    <button
                      key={tier}
                      type="button"
                      onClick={() => setDrawerTierTab(tier)}
                      className={`rounded-lg border px-3 py-1.5 text-left transition-all cursor-pointer flex items-center justify-between gap-2 ${
                        isActive ? meta.activeTabCls : meta.inactiveTabCls
                      }`}
                    >
                      <div className="min-w-0">
                        <div className="text-xs font-extrabold truncate">{meta.tabTitle}</div>
                        <div
                          className={`text-[10.5px] truncate ${
                            isActive ? 'text-white/90 font-medium' : 'opacity-85 font-medium'
                          }`}
                        >
                          {meta.tabSub}
                        </div>
                      </div>
                      {assignedBadge && (
                        <span
                          className={`px-1.5 py-0.5 rounded text-[10px] font-extrabold shrink-0 ${
                            isActive
                              ? 'bg-white/25 text-white border border-white/40'
                              : 'bg-white/90 text-slate-800 border border-black/10'
                          }`}
                        >
                          {assignedBadge}
                        </span>
                      )}
                    </button>
                  );
                })}
              </div>

              {/* Active Color Table Container (matching "6. Task 2: Idea Pillars") */}
              <div className={`rounded-xl border overflow-hidden ${activeMeta.panelBorderCls}`}>
                <div
                  className={`px-3 py-1.5 flex flex-wrap items-center justify-between gap-1.5 ${activeMeta.headerCls}`}
                >
                  <span className="text-[11px] sm:text-xs font-extrabold tracking-wide uppercase">
                    {activeMeta.headerTitle}
                  </span>
                  <span className="text-[11px] text-white/95 font-medium">
                    {activeMeta.priorityHint}
                  </span>
                </div>

                <div className="p-2.5 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2">
                  {WT2_PILLARS.filter((p) => p.tier === drawerTierTab).map((p) => (
                    <div
                      key={p.id}
                      className={`border rounded-lg p-2 bg-white text-xs shadow-2xs transition-all ${
                        bodyMode === 'multi'
                          ? 'flex flex-col justify-between gap-1.5'
                          : 'flex items-center justify-between gap-2'
                      } ${activeMeta.cardBorderCls}`}
                    >
                      <div className="min-w-0">
                        <div className={`font-extrabold truncate ${activeMeta.nameTextCls}`}>
                          {p.icon} {p.id}. {p.name}
                        </div>
                        <div className="text-[11px] text-slate-500 truncate">{p.viName}</div>
                      </div>
                      {bodyMode === 'single' ? (
                        <div className="flex items-center gap-1 shrink-0">
                          <button
                            onClick={() => {
                              setPillar1Id(p.id);
                              setSlottedPillarKeys((prev) => ({
                                ...prev,
                                '1_pillar': false,
                                '1_cause': false,
                                '1_effect': false,
                                '1_example': false
                              }));
                            }}
                            className={`px-2 py-1 rounded font-bold cursor-pointer ${
                              pillar1Id === p.id
                                ? 'bg-violet-600 text-white'
                                : 'bg-violet-100 text-violet-700 hover:bg-violet-200'
                            }`}
                          >
                            Body 1
                          </button>
                          <button
                            onClick={() => {
                              setPillar2Id(p.id);
                              setSlottedPillarKeys((prev) => ({
                                ...prev,
                                '2_pillar': false,
                                '2_cause': false,
                                '2_effect': false,
                                '2_example': false
                              }));
                            }}
                            className={`px-2 py-1 rounded font-bold cursor-pointer ${
                              pillar2Id === p.id
                                ? 'bg-amber-500 text-white'
                                : 'bg-amber-100 text-amber-800 hover:bg-amber-200'
                            }`}
                          >
                            Body 2
                          </button>
                        </div>
                      ) : (
                        <div className="flex flex-wrap items-center justify-between gap-1.5 pt-1 border-t border-slate-100">
                          <div className="flex items-center gap-0.5 flex-wrap">
                            <span className="text-[10px] font-extrabold text-violet-700 mr-0.5">
                              B1:
                            </span>
                            {(
                              Array.from(
                                { length: b1IdeaCount },
                                (_, i) => (i + 1) as 1 | 2 | 3 | 4 | 5
                              )
                            ).map((ideaIdx) => (
                              <button
                                key={`b1_${ideaIdx}`}
                                onClick={() => updateMultiIdea(1, ideaIdx, { id: p.id })}
                                className={`px-1.5 py-0.5 rounded text-[10.5px] font-extrabold cursor-pointer ${
                                  multiPillars[1][ideaIdx - 1].id === p.id
                                    ? 'bg-violet-600 text-white'
                                    : 'bg-violet-100 text-violet-700 hover:bg-violet-200'
                                }`}
                                title={`Gán vào Body 1 • Ý ${ideaIdx}`}
                              >
                                Ý{ideaIdx}
                              </button>
                            ))}
                          </div>
                          <div className="flex items-center gap-0.5 flex-wrap">
                            <span className="text-[10px] font-extrabold text-amber-700 mr-0.5">
                              B2:
                            </span>
                            {(
                              Array.from(
                                { length: b2IdeaCount },
                                (_, i) => (i + 1) as 1 | 2 | 3 | 4 | 5
                              )
                            ).map((ideaIdx) => (
                              <button
                                key={`b2_${ideaIdx}`}
                                onClick={() => updateMultiIdea(2, ideaIdx, { id: p.id })}
                                className={`px-1.5 py-0.5 rounded text-[10.5px] font-extrabold cursor-pointer ${
                                  multiPillars[2][ideaIdx - 1].id === p.id
                                    ? 'bg-amber-500 text-white'
                                    : 'bg-amber-100 text-amber-800 hover:bg-amber-200'
                                }`}
                                title={`Gán vào Body 2 • Ý ${ideaIdx}`}
                              >
                                Ý{ideaIdx}
                              </button>
                            ))}
                          </div>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          );
        })()}

        {/* ==================== MAIN SCROLLABLE BODY ==================== */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-5">
          {/* Quick Saved-Evaluation / WIP-Draft Banner when on Step 1 or Step 2 */}
          {step !== 3 && savedSubmissions.length > 0 && (
            <div className="bg-emerald-50 border border-emerald-300 rounded-xl px-4 py-2.5 flex flex-wrap items-center justify-between gap-2 text-xs text-emerald-950 shadow-2xs">
              <div className="flex items-center gap-2 flex-wrap">
                <span className="px-2 py-0.5 rounded-full bg-emerald-600 text-white font-extrabold text-[11px]">
                  💾 Đã lưu {savedSubmissions.length} bài chấm
                </span>
                <span className="font-semibold">
                  Đề này đã có kết quả chấm chữa AI (Lần gần nhất:{' '}
                  <strong>Band {savedSubmissions[0].overall}</strong>
                  {savedSubmissions[0].createdAt
                    ? ` • ${formatSavedTimestamp(savedSubmissions[0].createdAt)}`
                    : ''}
                  ).
                </span>
              </div>
              <div className="flex items-center gap-2 shrink-0">
                <button
                  type="button"
                  onClick={() => applySavedSubmissionToState(savedSubmissions[0], true)}
                  className="px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold cursor-pointer"
                >
                  👁️ Xem bài chấm &amp; lời chữa đã lưu →
                </button>
                <button
                  type="button"
                  onClick={handleStartFreshAttempt}
                  className="px-2.5 py-1 rounded-lg border border-emerald-300 bg-white hover:bg-emerald-100 text-emerald-900 font-bold cursor-pointer"
                >
                  🆕 Làm bản mới
                </button>
              </div>
            </div>
          )}

          {step !== 3 && savedSubmissions.length === 0 && restoredDraftNotice && (
            <div className="bg-sky-50 border border-sky-300 rounded-xl px-4 py-2 flex flex-wrap items-center justify-between gap-2 text-xs text-sky-950">
              <span>
                📝 <strong>Đã tự động khôi phục bản nháp</strong> em đang ghép dở cho đề này.
              </span>
              <button
                type="button"
                onClick={handleStartFreshAttempt}
                className="px-2.5 py-1 rounded-md border border-sky-300 bg-white hover:bg-sky-100 text-sky-800 font-bold cursor-pointer shrink-0"
              >
                🔄 Xóa nháp &amp; Làm lại từ đầu
              </button>
            </div>
          )}

          {/* -------------------- STEP 1: CHOOSE PILLARS & SLOT -------------------- */}
          {step === 1 && (
            <>
              {/* 1A. Structure Type / Sub-type Selector */}
              <div className="bg-white rounded-xl border border-slate-200 p-4 shadow-2xs space-y-3">
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div>
                    <span className="text-xs font-extrabold uppercase tracking-wider text-sky-600">
                      {isAutoCategory
                        ? 'Bước 1A • Nhận Diện Dạng Đề & Chọn Khung Bất Biến'
                        : 'Bước 1A • Khung Cấu Trúc Bất Biến'}
                    </span>
                    <h3 className="font-bold text-slate-900 text-sm sm:text-base">
                      {!hasConfirmedCategory ? (
                        <span className="text-amber-700">
                          🎯 Đọc câu hỏi cuối đề bài và bấm chọn đúng 1 trong 5 Dạng bài bên dưới:
                        </span>
                      ) : (
                        <>
                          {structureDef.name}{' '}
                          <span className="font-normal text-slate-500 text-xs sm:text-sm">
                            — {swapBodies ? bodyRoles.orderHint : structureDef.viSubtitle}
                          </span>
                          {swapBodies && (
                            <span className="ml-2 inline-block bg-emerald-100 text-emerald-800 border border-emerald-300 text-[11px] font-extrabold px-2 py-0.5 rounded-full align-middle">
                              🔄 Đã đảo Body 1 ↔ 2
                            </span>
                          )}
                        </>
                      )}
                    </h3>
                  </div>

                  <div className="flex flex-wrap items-center gap-2">
                    {isAutoCategory && (
                      <button
                        type="button"
                        onClick={handleApplyRecommendedGuide}
                        className="px-3 py-1.5 rounded-lg bg-amber-50 hover:bg-amber-100 border border-amber-300 text-amber-900 text-xs font-extrabold cursor-pointer transition-colors"
                        title="Nhờ Thầy gợi ý Dạng đề chuẩn + các Trụ ý phù hợp nhất cho đề này"
                      >
                        💡 Gợi ý Dạng đề &amp; Trụ ý
                      </button>
                    )}

                    {/* Sub-version selectors for Opinion / Mixed */}
                    {hasConfirmedCategory && selectedCategory === 'opinion' && (
                      <>
                        <select
                          value={templateId}
                          onChange={(e) => {
                            setTemplateId(e.target.value as Wt2TemplateId);
                            setSwapBodies(false);
                          }}
                          className="text-xs font-bold border border-slate-300 rounded-lg px-2.5 py-1.5 bg-white text-slate-800"
                        >
                          <option value="opinion_v1">Version 1: One-sided (100% Agree/Disagree)</option>
                          <option value="opinion_v2">Version 2: Concession (Nhượng bộ &amp; Phản biện)</option>
                        </select>
                        <div className="inline-flex rounded-lg border border-slate-300 overflow-hidden text-xs font-bold">
                          <button
                            onClick={() => setStance('agree')}
                            className={`px-2.5 py-1.5 cursor-pointer ${
                              stance === 'agree' ? 'bg-emerald-600 text-white' : 'bg-white text-slate-600'
                            }`}
                          >
                            Agree (Đồng ý)
                          </button>
                          <button
                            onClick={() => setStance('disagree')}
                            className={`px-2.5 py-1.5 cursor-pointer ${
                              stance === 'disagree' ? 'bg-rose-600 text-white' : 'bg-white text-slate-600'
                            }`}
                          >
                            Disagree (Phản đối)
                          </button>
                        </div>
                      </>
                    )}

                    {hasConfirmedCategory && selectedCategory === 'mixed' && (
                      <select
                        value={templateId}
                        onChange={(e) => {
                          const next = e.target.value as Wt2TemplateId;
                          setTemplateId(next);
                          setSwapBodies(false);
                          const nextPol2 = next === 'mixed_ps' ? 'positive' : 'negative';
                          setPillar1Polarity('negative');
                          setPillar2Polarity(nextPol2);
                          syncMultiPolarities('negative', nextPol2);
                        }}
                        className="text-xs font-bold border border-slate-300 rounded-lg px-2.5 py-1.5 bg-white text-slate-800"
                      >
                        <option value="mixed_ps">Trang 1: Problems / Causes &amp; Solutions</option>
                        <option value="mixed_ce">Trang 3: Causes &amp; Effects</option>
                      </select>
                    )}
                  </div>
                </div>

                {/* Category selector shown when launched in 'auto' mode (e.g. from 7. Task 2: Questions) */}
                {isAutoCategory && (
                  <div className="space-y-2.5 pt-2 border-t border-slate-100">
                    <div className="grid grid-cols-2 sm:grid-cols-5 gap-2">
                      {CATEGORY_OPTIONS.map((c) => {
                        const isChosen = hasConfirmedCategory && selectedCategory === c.id;
                        return (
                          <button
                            key={c.id}
                            onClick={() => handleCategoryChange(c.id)}
                            className={`p-2.5 rounded-xl border text-left transition-all cursor-pointer ${
                              isChosen
                                ? 'border-sky-600 bg-sky-50 ring-2 ring-sky-500 shadow-2xs'
                                : 'border-slate-200 hover:border-sky-400 hover:bg-slate-50'
                            }`}
                          >
                            <div className="text-xs font-extrabold text-slate-800">{c.label}</div>
                            <div className="text-[11px] text-slate-500 truncate">{c.shortDesc}</div>
                          </button>
                        );
                      })}
                    </div>

                    {hasConfirmedCategory && (
                      questionGuide.acceptedCategories.includes(selectedCategory) ? (
                        <div className="bg-emerald-50 border border-emerald-200 rounded-lg px-3 py-2 text-xs text-emerald-900 flex flex-wrap items-center justify-between gap-2">
                          <span>
                            <strong>✅ Nhận diện dạng đề chuẩn xác!</strong> {questionGuide.signalHint}
                          </span>
                          {showAutoGuide && (
                            <span className="font-bold text-emerald-700">
                              🎯 Đã gợi ý sẵn bộ Trụ ý bám sát đề!
                            </span>
                          )}
                        </div>
                      ) : (
                        <div className="bg-amber-50 border border-amber-300 rounded-lg px-3 py-2 text-xs text-amber-950 flex flex-wrap items-center justify-between gap-2">
                          <span>
                            <strong>💡 Gợi ý nhận diện đề:</strong> {questionGuide.signalHint}. (Em vẫn có thể tự luyện theo khung đang chọn hoặc bấm áp dụng khung chuẩn).
                          </span>
                          <button
                            type="button"
                            onClick={handleApplyRecommendedGuide}
                            className="px-2.5 py-1 rounded-md bg-amber-600 hover:bg-amber-700 text-white font-bold cursor-pointer shrink-0"
                          >
                            Chuyển sang Khung chuẩn + Trụ ý gợi ý
                          </button>
                        </div>
                      )
                    )}
                  </div>
                )}
              </div>

              {!hasConfirmedCategory ? (
                <div className="bg-sky-50/70 border-2 border-dashed border-sky-300 rounded-2xl p-8 text-center space-y-2">
                  <div className="text-2xl">🧭</div>
                  <div className="font-extrabold text-slate-800 text-sm sm:text-base">
                    Bước đầu tiên khi vào phòng thi: Phân loại đúng Dạng đề!
                  </div>
                  <p className="text-xs sm:text-sm text-slate-600 max-w-xl mx-auto">
                    Hãy bấm chọn 1 trong 5 dạng bài (<strong>Discussion, Argument, Opinion, Mixed, Two-part</strong>) ở khung trên để hệ thống mở đúng <strong>Khung Cấu Trúc Bất Biến</strong> và bảng kéo thả <strong>19 Idea Pillars</strong> nhé!
                  </p>
                </div>
              ) : (
                <>
              {/* 1B-0. BODY STRATEGY VERSION SWITCHER (PHIÊN BẢN 1 vs PHIÊN BẢN 2) */}
              <div className="bg-white rounded-xl border border-slate-200 p-4 shadow-2xs space-y-3">
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div>
                    <span className="text-xs font-extrabold uppercase tracking-wider text-indigo-600">
                      Bước 1B • Chọn Chiến Thuật Triển Khai Đoạn Body (2 Phiên Bản Linh Hoạt)
                    </span>
                    <p className="text-xs text-slate-500 mt-0.5">
                      Cùng 1 bảng 19 Idea Pillars — em có thể đào sâu 1 ý/Body (4 câu PEEL) hoặc ghép linh hoạt <strong>1–5 ý/Body</strong> kèm Linking Words (support gọn <strong>1–2 câu/ý</strong>):
                    </p>
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  <button
                    type="button"
                    onClick={() => handleBodyModeSwitch('single')}
                    className={`p-3.5 rounded-xl border-2 text-left transition-all cursor-pointer ${
                      bodyMode === 'single'
                        ? 'border-sky-600 bg-sky-50/80 ring-2 ring-sky-400 shadow-xs'
                        : 'border-slate-200 bg-slate-50/50 hover:border-sky-300 hover:bg-white'
                    }`}
                  >
                    <div className="flex items-center justify-between gap-2 mb-1">
                      <span className="font-extrabold text-xs sm:text-sm text-slate-900">
                        🎯 Phiên bản 1: 1 Trụ Ý Sâu / Body (4 câu PEEL)
                      </span>
                      {bodyMode === 'single' && (
                        <span className="bg-sky-600 text-white text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full">
                          Đang chọn
                        </span>
                      )}
                    </div>
                    <p className="text-xs text-slate-600 leading-relaxed">
                      Mỗi Body tập trung mổ xẻ sâu <strong>1 Trụ ý duy nhất</strong> qua đủ 4 câu: <em>Giới thiệu Trụ ý → Nhân (Cause) → Quả (Effect) → Ví dụ số liệu (Example)</em>. Không cần từ nối liệt kê.
                    </p>
                  </button>

                  <button
                    type="button"
                    onClick={() => handleBodyModeSwitch('multi')}
                    className={`p-3.5 rounded-xl border-2 text-left transition-all cursor-pointer ${
                      bodyMode === 'multi'
                        ? 'border-indigo-600 bg-indigo-50/80 ring-2 ring-indigo-400 shadow-xs'
                        : 'border-slate-200 bg-slate-50/50 hover:border-indigo-300 hover:bg-white'
                    }`}
                  >
                    <div className="flex items-center justify-between gap-2 mb-1">
                      <span className="font-extrabold text-xs sm:text-sm text-slate-900">
                        🔗 Phiên bản 2: Linh Hoạt 1–5 Trụ Ý / Body + Support 1–2 Câu/Ý
                      </span>
                      {bodyMode === 'multi' ? (
                        <span className="bg-indigo-600 text-white text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full">
                          Đang chọn
                        </span>
                      ) : (
                        <span className="bg-indigo-100 text-indigo-800 text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full">
                          1–5 ý • Linh hoạt
                        </span>
                      )}
                    </div>
                    <p className="text-xs text-slate-600 leading-relaxed">
                      Tùy chọn độc lập <strong>Min 1 – Max 5 ý</strong> cho từng Body • Tự đổi <strong>Topic Sentence</strong> (số ít / số nhiều) + <strong>Linking Words</strong> thông minh + chọn riêng <strong>1 câu gộp</strong> hoặc <strong>2 câu support</strong> cho từng ý.
                    </p>
                  </button>
                </div>

                {bodyMode === 'multi' && (
                  <div className="bg-slate-50 border border-indigo-200/80 rounded-xl px-3.5 py-2.5 text-xs text-slate-700 leading-relaxed space-y-1">
                    <div className="font-extrabold text-indigo-900">
                      💡 Công thức vàng phân bổ 1–2 câu support theo số ý (vừa chuẩn Band 8.0+ vừa kịp 40 phút thi):
                    </div>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-2 pt-0.5 text-[11.5px]">
                      <div className="bg-white rounded-lg border border-slate-200 px-2.5 py-1.5">
                        <strong className="text-indigo-800">• 1–2 ý / Body:</strong> Dùng{' '}
                        <strong>2 câu/ý</strong> (<em>Nêu Trụ ý + 1 câu Nhân–Quả</em>) → Đoạn dài 3–5 câu (~70–105 từ).
                      </div>
                      <div className="bg-white rounded-lg border border-slate-200 px-2.5 py-1.5">
                        <strong className="text-violet-800">• 3 ý / Body:</strong> Chuẩn nhất là{' '}
                        <strong>Ý 1 (2 câu) + Ý 2, 3 (1 câu gộp)</strong> → Đoạn 5 câu (~105 từ), vừa có điểm nhấn vừa đa diện.
                      </div>
                      <div className="bg-white rounded-lg border border-slate-200 px-2.5 py-1.5">
                        <strong className="text-fuchsia-800">• 4–5 ý / Body:</strong> Ưu tiên{' '}
                        <strong>1 câu phức gộp/ý</strong> → Đoạn 5–6 câu (~120–145 từ). Vẫn có thể bật <strong>2 câu</strong> cho ý đinh!
                      </div>
                    </div>
                  </div>
                )}

                {questionGuide.pluralNotice && (
                  <div className="bg-indigo-50 border border-indigo-200 rounded-lg px-3 py-2 text-xs text-indigo-950 flex flex-wrap items-center justify-between gap-2">
                    <span>
                      <strong>✨ Mẹo ăn trọn Task Response:</strong> {questionGuide.pluralNotice}
                    </span>
                    {bodyMode === 'single' && (
                      <button
                        type="button"
                        onClick={() => handleBodyModeSwitch('multi')}
                        className="px-2.5 py-1 rounded-md bg-indigo-600 hover:bg-indigo-700 text-white font-bold cursor-pointer shrink-0"
                      >
                        Thử Phiên bản 2 (1–5 ý + Linking) →
                      </button>
                    )}
                  </div>
                )}
              </div>

              {/* 1B-SWAP. BODY ORDER & SWAP BAR (BODY 1 ↔ BODY 2) */}
              <div
                className={`rounded-xl border px-4 py-3 shadow-2xs space-y-2.5 transition-colors ${
                  swapBodies
                    ? 'bg-emerald-50/75 border-emerald-300'
                    : 'bg-white border-slate-200'
                }`}
              >
                <div className="flex flex-wrap items-center justify-between gap-3">
                  <div className="space-y-1 min-w-0">
                    <div className="flex flex-wrap items-center gap-1.5 text-xs">
                      <span className="font-extrabold uppercase tracking-wide text-slate-700">
                        📐 Thứ tự thân bài:
                      </span>
                      <span className="px-2 py-0.5 rounded-md bg-violet-100 text-violet-900 border border-violet-300 font-extrabold">
                        Body 1: {bodyRoles.b1Short}
                      </span>
                      <span className="text-slate-400 font-extrabold">→</span>
                      <span className="px-2 py-0.5 rounded-md bg-amber-100 text-amber-900 border border-amber-300 font-extrabold">
                        Body 2: {bodyRoles.b2Short}
                      </span>
                      {swapBodies && (
                        <span className="px-2 py-0.5 rounded-full bg-emerald-600 text-white text-[10.5px] font-extrabold">
                          ✓ Đã đảo vị trí
                        </span>
                      )}
                    </div>
                    <p className="text-[11.5px] text-slate-600 leading-snug">
                      Thông thường <strong>Body 2</strong> nên là đoạn nhiều ý hơn (hoặc vế em nghiêng về). Khi đảo vị trí, hệ thống sẽ <strong>tự động chuyển toàn bộ Trụ ý giữa 2 đoạn</strong>, đồng thời <strong>đổi luôn câu cuối Mở bài &amp; câu đầu Kết bài</strong> cho khớp mạch logic!
                    </p>
                  </div>

                  <button
                    type="button"
                    onClick={handleSwapBodies}
                    className={`px-3.5 py-2 rounded-xl border text-xs font-extrabold cursor-pointer transition-all shrink-0 shadow-2xs ${
                      swapBodies
                        ? 'bg-emerald-600 hover:bg-emerald-700 text-white border-emerald-700'
                        : 'bg-indigo-600 hover:bg-indigo-700 text-white border-indigo-700'
                    }`}
                  >
                    {swapBodies
                      ? '🔄 Đảo lại Body 1 ↔ Body 2 (Về mặc định)'
                      : '🔄 Đảo vị trí Body 1 ↔ Body 2'}
                  </button>
                </div>

                {bodyMode === 'multi' && b1IdeaCount > b2IdeaCount && (
                  <div className="bg-amber-50 border border-amber-300 rounded-lg px-3 py-2 flex flex-wrap items-center justify-between gap-2 text-xs text-amber-950">
                    <span>
                      💡 <strong>Mẹo bố cục Band 8.0+:</strong> Hiện <strong>Body 1 ({b1IdeaCount} ý — {bodyRoles.b1Short})</strong> đang nhiều ý hơn <strong>Body 2 ({b2IdeaCount} ý — {bodyRoles.b2Short})</strong>. Thông thường đoạn nhiều ý hơn nên được đẩy xuống <strong>Body 2</strong> để mạch văn nặng dần và kết luận thuyết phục hơn!
                    </span>
                    <button
                      type="button"
                      onClick={handleSwapBodies}
                      className="px-3 py-1 rounded-lg bg-amber-600 hover:bg-amber-700 text-white font-extrabold cursor-pointer shrink-0"
                    >
                      🔄 Đẩy nhóm {b1IdeaCount} ý xuống Body 2
                    </button>
                  </div>
                )}
              </div>

              {/* 1B. Pick Pillars & Drag/Click Cards (Version 1 vs Version 2) */}
              {bodyMode === 'single' ? (
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                  {[
                    {
                      bodyIdx: 1 as const,
                      title:
                        templateId === 'mixed_ps' && swapBodies
                          ? 'Body 1 • Giải pháp & Kết quả (By doing so)'
                          : `Body 1 • ${bodyRoles.b1Short} (1 ý sâu • 4 câu)`,
                      accent: 'border-violet-300 bg-violet-50/40',
                      headerBadge: 'bg-violet-600 text-white',
                      pillar: pillar1,
                      setPillarId: setPillar1Id,
                      polarity: pillar1Polarity,
                      setPolarity: setPillar1Polarity,
                      colsToShow:
                        templateId === 'mixed_ps' && swapBodies
                          ? (['effect'] as PillarSlotType[])
                          : SHUFFLED_COLS
                    },
                    {
                      bodyIdx: 2 as const,
                      title:
                        templateId === 'mixed_ps' && !swapBodies
                          ? 'Body 2 • Giải pháp & Kết quả (By doing so)'
                          : `Body 2 • ${bodyRoles.b2Short} (1 ý sâu • 4 câu)`,
                      accent: 'border-amber-300 bg-amber-50/40',
                      headerBadge: 'bg-amber-500 text-white',
                      pillar: pillar2,
                      setPillarId: setPillar2Id,
                      polarity: pillar2Polarity,
                      setPolarity: setPillar2Polarity,
                      colsToShow:
                        templateId === 'mixed_ps' && !swapBodies
                          ? (['effect'] as PillarSlotType[])
                          : SHUFFLED_COLS
                    }
                  ].map((cfg) => (
                    <div
                      key={cfg.bodyIdx}
                      className={`rounded-xl border-2 ${cfg.accent} p-4 space-y-3`}
                    >
                      <div className="flex flex-wrap items-center justify-between gap-2">
                        <span className={`text-xs font-extrabold px-2.5 py-1 rounded-full ${cfg.headerBadge}`}>
                          {cfg.title}
                        </span>

                        <div className="inline-flex rounded-lg border border-slate-300 bg-white overflow-hidden text-xs font-bold">
                          <button
                            onClick={() => cfg.setPolarity('positive')}
                            className={`px-2.5 py-1 cursor-pointer ${
                              cfg.polarity === 'positive'
                                ? 'bg-emerald-600 text-white'
                                : 'text-slate-600 hover:bg-slate-50'
                            }`}
                          >
                            (+) Tích cực
                          </button>
                          <button
                            onClick={() => cfg.setPolarity('negative')}
                            className={`px-2.5 py-1 cursor-pointer ${
                              cfg.polarity === 'negative'
                                ? 'bg-rose-600 text-white'
                                : 'text-slate-600 hover:bg-slate-50'
                            }`}
                          >
                            (-) Tiêu cực
                          </button>
                        </div>
                      </div>

                      <div className="space-y-1.5">
                        <div className="flex flex-wrap items-center justify-between gap-1.5 text-[11px]">
                          <span
                            className={`px-2 py-0.5 rounded-md border font-extrabold ${
                              PILLAR_TIER_META[cfg.pillar.tier].pillBadgeCls
                            }`}
                          >
                            {PILLAR_TIER_META[cfg.pillar.tier].shortBadge}
                          </span>
                          {difficulty === 'level1' && (
                            <button
                              type="button"
                              onClick={() => {
                                setDrawerTierTab(cfg.pillar.tier);
                                setShowPillarTableDrawer(true);
                              }}
                              className="text-sky-700 hover:text-sky-900 font-bold cursor-pointer underline decoration-dotted"
                            >
                              Đổi nhanh từ 3 bảng màu ▲
                            </button>
                          )}
                        </div>
                        <select
                          value={cfg.pillar.id}
                          onChange={(e) => {
                            const nextId = Number(e.target.value);
                            cfg.setPillarId(nextId);
                            setSlottedPillarKeys((prev) => ({
                              ...prev,
                              [`${cfg.bodyIdx}_pillar`]: false,
                              [`${cfg.bodyIdx}_cause`]: false,
                              [`${cfg.bodyIdx}_effect`]: false,
                              [`${cfg.bodyIdx}_example`]: false
                            }));
                          }}
                          className="w-full text-sm font-bold border border-slate-300 rounded-lg px-3 py-2 bg-white text-slate-800 shadow-2xs"
                        >
                          {([1, 2, 3] as const).map((tier) => (
                            <optgroup key={tier} label={PILLAR_TIER_META[tier].optgroupLabel}>
                              {WT2_PILLARS.filter((p) => p.tier === tier).map((p) => (
                                <option key={p.id} value={p.id}>
                                  {p.id}. {p.name} — {p.viName}
                                </option>
                              ))}
                            </optgroup>
                          ))}
                        </select>
                      </div>

                      <div className="text-xs text-slate-600 font-medium">
                        {difficulty === 'level1'
                          ? '👇 Kéo thả (hoặc bấm chọn thẻ rồi bấm vào ô [...] tương ứng bên dưới) để lắp vào Khung:'
                          : '🧠 Chế độ Thuộc lòng: Nhìn 4 Từ khóa mỏ neo dưới đây và tự gõ câu hoàn chỉnh vào Khung bên dưới:'}
                      </div>

                      {/* Draggable / Clickable Cards */}
                      <div className="space-y-2">
                        {cfg.colsToShow.map((col) => {
                          const unitKey = `${cfg.bodyIdx}_${col}`;
                          const isPlaced = !!slottedPillarKeys[unitKey];
                          const isSelected =
                            selectedCard?.bodyIndex === cfg.bodyIdx &&
                            !selectedCard?.ideaIndex &&
                            selectedCard?.col === col;
                          const textDisplay =
                            difficulty === 'level1'
                              ? getBranchValue(cfg.bodyIdx, col)
                              : `🔑 Mỏ neo: ${getBranchAnchor(cfg.bodyIdx, col)}`;

                          return (
                            <div
                              key={col}
                              draggable={difficulty === 'level1' && !isPlaced}
                              onDragStart={(e) => {
                                e.dataTransfer.setData(
                                  'application/json',
                                  JSON.stringify({ bodyIndex: cfg.bodyIdx, col })
                                );
                                setSelectedCard({ bodyIndex: cfg.bodyIdx, col });
                              }}
                              onClick={() => {
                                if (difficulty === 'level2') return;
                                if (isPlaced) {
                                  setSlottedPillarKeys((prev) => ({ ...prev, [unitKey]: false }));
                                  return;
                                }
                                setSelectedCard(
                                  isSelected ? null : { bodyIndex: cfg.bodyIdx, col }
                                );
                              }}
                              className={`p-2.5 rounded-lg border text-xs leading-relaxed transition-all select-none ${
                                difficulty === 'level2'
                                  ? 'bg-purple-50 border-purple-200 text-purple-900 font-semibold'
                                  : isPlaced
                                  ? 'bg-emerald-50/80 border-emerald-300 text-emerald-800 opacity-65 cursor-pointer'
                                  : isSelected
                                  ? 'bg-sky-50 border-sky-500 ring-2 ring-sky-400 shadow-sm cursor-pointer'
                                  : 'bg-white border-slate-200 hover:border-sky-400 shadow-2xs cursor-grab active:cursor-grabbing'
                              }`}
                            >
                              <div className="flex items-center justify-between gap-2 mb-1">
                                <span
                                  className={`text-[10px] font-extrabold uppercase px-2 py-0.5 rounded border ${
                                    difficulty === 'level1'
                                      ? 'bg-slate-100 text-slate-700 border-slate-300'
                                      : COL_LABELS[col].color
                                  }`}
                                >
                                  {difficulty === 'level1'
                                    ? isPlaced
                                      ? `✓ Đã lắp [${COL_LABELS[col].badge}] (Bấm để gỡ)`
                                      : 'Thẻ ý tưởng (Đoán đúng cột & thả vào khung)'
                                    : COL_LABELS[col].badge}
                                </span>
                                {isSelected && !isPlaced && (
                                  <span className="text-[11px] font-bold text-sky-700 animate-pulse">
                                    👉 Bấm vào ô [...] bên dưới để thả!
                                  </span>
                                )}
                              </div>
                              <div>{textDisplay}</div>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                /* ============ PHIÊN BẢN 2: LINH HOẠT 1–5 TRỤ Ý / BODY + SUPPORT 1–2 CÂU/Ý ============ */
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                  {[
                    {
                      bodyIdx: 1 as const,
                      title: `Body 1 • ${bodyRoles.b1Short}`,
                      accent: 'border-violet-300 bg-violet-50/40',
                      headerBadge: 'bg-violet-600 text-white',
                      activeCountBtn: 'bg-violet-600 text-white',
                      ideaCount: b1IdeaCount
                    },
                    {
                      bodyIdx: 2 as const,
                      title: `Body 2 • ${bodyRoles.b2Short}`,
                      accent: 'border-amber-300 bg-amber-50/40',
                      headerBadge: 'bg-amber-500 text-white',
                      activeCountBtn: 'bg-amber-500 text-white',
                      ideaCount: b2IdeaCount
                    }
                  ].map((bCfg) => {
                    const dupWarn = getDuplicatePillarWarning(bCfg.bodyIdx);
                    const ideaIndices = Array.from(
                      { length: bCfg.ideaCount },
                      (_, idx) => (idx + 1) as 1 | 2 | 3 | 4 | 5
                    );
                    const activeSels = multiPillars[bCfg.bodyIdx].slice(0, bCfg.ideaCount);
                    const totalBodySentences =
                      1 + activeSels.reduce((acc, s) => acc + s.sentences, 0);
                    const estBodyWords =
                      18 +
                      activeSels.reduce(
                        (acc, s) => acc + (s.sentences === 2 ? 38 : 25),
                        0
                      );
                    const balancedSlice = getRecommendedSentenceDepths(
                      bCfg.ideaCount
                    ).slice(0, bCfg.ideaCount);
                    const isAll1 = activeSels.every((s) => s.sentences === 1);
                    const isAll2 = activeSels.every((s) => s.sentences === 2);
                    const isBalanced = activeSels.every(
                      (s, i) => s.sentences === balancedSlice[i]
                    );

                    return (
                      <div
                        key={bCfg.bodyIdx}
                        className={`rounded-xl border-2 ${bCfg.accent} p-4 space-y-3`}
                      >
                        {/* Header Row: Body Title + 1..5 Idea Count Buttons */}
                        <div className="flex flex-wrap items-center justify-between gap-2">
                          <span
                            className={`text-xs font-extrabold px-2.5 py-1 rounded-full ${bCfg.headerBadge}`}
                          >
                            {bCfg.title}
                          </span>

                          <div className="flex items-center gap-1.5">
                            <span className="text-[11px] font-bold text-slate-600">
                              Số ý:
                            </span>
                            <div className="inline-flex rounded-lg border border-slate-300 bg-white overflow-hidden text-xs font-extrabold shadow-2xs">
                              {([1, 2, 3, 4, 5] as const).map((cnt) => (
                                <button
                                  key={cnt}
                                  type="button"
                                  onClick={() => changeBodyIdeaCount(bCfg.bodyIdx, cnt)}
                                  className={`px-2.5 py-1 cursor-pointer transition-colors border-r last:border-r-0 border-slate-200 ${
                                    bCfg.ideaCount === cnt
                                      ? bCfg.activeCountBtn
                                      : 'text-slate-700 hover:bg-slate-100'
                                  }`}
                                  title={`Chọn ${cnt} Trụ ý cho Body ${bCfg.bodyIdx} (tự động cân bằng 1–2 câu/ý)`}
                                >
                                  {cnt} ý
                                </button>
                              ))}
                            </div>
                          </div>
                        </div>

                        {/* Live Sentence & Word Estimate + Quick Batch Presets */}
                        <div className="bg-white/85 border border-slate-200 rounded-lg px-2.5 py-1.5 flex flex-wrap items-center justify-between gap-2 text-[11px]">
                          <span className="font-bold text-slate-700">
                            📏 Dự kiến đoạn:{' '}
                            <strong className="text-indigo-800">
                              {totalBodySentences} câu (~{estBodyWords} từ)
                            </strong>{' '}
                            <span className="text-slate-500 font-normal">
                              (1 mở đoạn + {totalBodySentences - 1} câu thân)
                            </span>
                          </span>

                          <div className="inline-flex items-center rounded-md border border-slate-300 bg-slate-50 overflow-hidden font-bold">
                            <button
                              type="button"
                              onClick={() => applyBodySentencePreset(bCfg.bodyIdx, 'all1')}
                              className={`px-2 py-0.5 cursor-pointer border-r border-slate-200 ${
                                isAll1
                                  ? 'bg-fuchsia-600 text-white'
                                  : 'text-slate-600 hover:bg-white'
                              }`}
                              title="Rút gọn tất cả các ý trong Body này thành 1 câu phức/ý"
                            >
                              Tất cả 1 câu
                            </button>
                            <button
                              type="button"
                              onClick={() =>
                                applyBodySentencePreset(bCfg.bodyIdx, 'balanced')
                              }
                              className={`px-2 py-0.5 cursor-pointer border-r border-slate-200 ${
                                isBalanced && !isAll1 && !isAll2
                                  ? 'bg-emerald-600 text-white'
                                  : 'text-emerald-800 hover:bg-white'
                              }`}
                              title="Tự động cân bằng số câu chuẩn Band 8.0+ theo số ý đã chọn"
                            >
                              ⚡ Cân bằng
                            </button>
                            <button
                              type="button"
                              onClick={() => applyBodySentencePreset(bCfg.bodyIdx, 'all2')}
                              className={`px-2 py-0.5 cursor-pointer ${
                                isAll2
                                  ? 'bg-indigo-600 text-white'
                                  : 'text-slate-600 hover:bg-white'
                              }`}
                              title="Triển khai đầy đủ 2 câu (Nêu ý + Nhân–Quả) cho mọi ý trong Body này"
                            >
                              Tất cả 2 câu
                            </button>
                          </div>
                        </div>

                        {totalBodySentences >= 8 && (
                          <div className="bg-sky-50 border border-sky-300 text-sky-950 rounded-lg px-3 py-1.5 text-xs flex flex-wrap items-center justify-between gap-2">
                            <span>
                              ⏱️ <strong>Mẹo kịp 40 phút phòng thi:</strong> Body {bCfg.bodyIdx} đang dài{' '}
                              <strong>{totalBodySentences} câu (~{estBodyWords} từ)</strong>. Khi ghép{' '}
                              {bCfg.ideaCount} ý, em nên để 1 câu gộp/ý (hoặc chỉ giữ 2 câu ở ý đầu)!
                            </span>
                            <button
                              type="button"
                              onClick={() =>
                                applyBodySentencePreset(bCfg.bodyIdx, 'balanced')
                              }
                              className="px-2 py-0.5 rounded bg-sky-600 hover:bg-sky-700 text-white font-extrabold text-[11px] cursor-pointer shrink-0"
                            >
                              ⚡ Cân bằng chuẩn
                            </button>
                          </div>
                        )}

                        {dupWarn && (
                          <div className="bg-amber-100 border border-amber-300 text-amber-950 rounded-lg px-3 py-1.5 text-xs font-bold">
                            ⚠️ {dupWarn}
                          </div>
                        )}

                        <div className="space-y-3">
                          {ideaIndices.map((ideaIdx) => {
                            const sel = multiPillars[bCfg.bodyIdx][ideaIdx - 1];
                            const role = getLinkerRoleForIdea(ideaIdx, bCfg.ideaCount);
                            const roleOpts = WT2_LINKER_ROLE_OPTIONS[role];
                            const linkKey = `b${bCfg.bodyIdx}_link_${role}`;
                            const colsForIdea: PillarSlotType[] =
                              sel.sentences === 2
                                ? ideaIdx % 2 === 1
                                  ? ['compact_support', 'pillar']
                                  : ['pillar', 'compact_support']
                                : ['compact_single'];

                            return (
                              <div
                                key={ideaIdx}
                                className="bg-white/90 rounded-xl border border-slate-200 p-3 space-y-2 shadow-2xs"
                              >
                                {/* Row 1: Sub-idea label + Role-based Linking Word + 1-2 Sentence Toggle + Polarity */}
                                <div className="flex flex-wrap items-center justify-between gap-2">
                                  <div className="flex items-center gap-1.5 flex-wrap">
                                    <span className="px-2 py-0.5 rounded-md bg-slate-800 text-white text-[11px] font-extrabold">
                                      Ý {bCfg.bodyIdx}.{ideaIdx}
                                    </span>
                                    <select
                                      value={linkers[linkKey] || roleOpts[0].en}
                                      onChange={(e) =>
                                        setLinkers((prev) => ({
                                          ...prev,
                                          [linkKey]: e.target.value
                                        }))
                                      }
                                      title="Từ nối tự động gợi ý theo vị trí của ý trong đoạn"
                                      className="text-xs font-extrabold border border-indigo-300 rounded-md px-2 py-0.5 bg-indigo-50 text-indigo-900 cursor-pointer max-w-[230px]"
                                    >
                                      {roleOpts.map((opt) => (
                                        <option key={opt.en} value={opt.en}>
                                          🔗 {opt.en} ({opt.vi})
                                        </option>
                                      ))}
                                    </select>
                                  </div>

                                  <div className="flex items-center gap-1.5 flex-wrap">
                                    {/* Per-Idea 1 sentence vs 2 sentences toggle */}
                                    <div
                                      className="inline-flex rounded-md border border-indigo-300 bg-white overflow-hidden text-[11px] font-extrabold"
                                      title="Chọn triển khai ý này bằng 1 câu phức gộp gọn hoặc 2 câu (Nêu ý + Nhân–Quả)"
                                    >
                                      <button
                                        type="button"
                                        onClick={() =>
                                          updateMultiIdea(bCfg.bodyIdx, ideaIdx, {
                                            sentences: 1
                                          })
                                        }
                                        className={`px-2 py-0.5 cursor-pointer ${
                                          sel.sentences === 1
                                            ? 'bg-fuchsia-600 text-white'
                                            : 'text-slate-600 hover:bg-slate-50'
                                        }`}
                                        title="1 câu phức gộp trọn Trụ ý + Nhân–Quả"
                                      >
                                        1 câu
                                      </button>
                                      <button
                                        type="button"
                                        onClick={() =>
                                          updateMultiIdea(bCfg.bodyIdx, ideaIdx, {
                                            sentences: 2
                                          })
                                        }
                                        className={`px-2 py-0.5 cursor-pointer border-l border-indigo-200 ${
                                          sel.sentences === 2
                                            ? 'bg-indigo-600 text-white'
                                            : 'text-slate-600 hover:bg-slate-50'
                                        }`}
                                        title="2 câu: 1 câu giới thiệu Trụ ý + 1 câu support Nhân–Quả"
                                      >
                                        2 câu
                                      </button>
                                    </div>

                                    <div className="inline-flex rounded-md border border-slate-300 bg-white overflow-hidden text-[11px] font-bold">
                                      <button
                                        type="button"
                                        onClick={() =>
                                          updateMultiIdea(bCfg.bodyIdx, ideaIdx, {
                                            polarity: 'positive'
                                          })
                                        }
                                        className={`px-1.5 py-0.5 cursor-pointer ${
                                          sel.polarity === 'positive'
                                            ? 'bg-emerald-600 text-white'
                                            : 'text-slate-600 hover:bg-slate-50'
                                        }`}
                                        title="Nhánh Tích cực (+)"
                                      >
                                        (+)
                                      </button>
                                      <button
                                        type="button"
                                        onClick={() =>
                                          updateMultiIdea(bCfg.bodyIdx, ideaIdx, {
                                            polarity: 'negative'
                                          })
                                        }
                                        className={`px-1.5 py-0.5 cursor-pointer border-l border-slate-200 ${
                                          sel.polarity === 'negative'
                                            ? 'bg-rose-600 text-white'
                                            : 'text-slate-600 hover:bg-slate-50'
                                        }`}
                                        title="Nhánh Tiêu cực (-)"
                                      >
                                        (-)
                                      </button>
                                    </div>
                                  </div>
                                </div>

                                {/* Row 2: 19-Pillar dropdown + Tier priority badge */}
                                {(() => {
                                  const selPillar =
                                    WT2_PILLARS.find((x) => x.id === sel.id) || WT2_PILLARS[0];
                                  return (
                                    <div className="space-y-1">
                                      <div className="flex flex-wrap items-center justify-between gap-1 text-[10.5px]">
                                        <span
                                          className={`px-1.5 py-0.5 rounded border font-extrabold ${
                                            PILLAR_TIER_META[selPillar.tier].pillBadgeCls
                                          }`}
                                        >
                                          {PILLAR_TIER_META[selPillar.tier].shortBadge}
                                        </span>
                                        {difficulty === 'level1' && (
                                          <button
                                            type="button"
                                            onClick={() => {
                                              setDrawerTierTab(selPillar.tier);
                                              setShowPillarTableDrawer(true);
                                            }}
                                            className="text-sky-700 hover:text-sky-900 font-bold cursor-pointer underline decoration-dotted"
                                          >
                                            Mở 3 bảng màu ▲
                                          </button>
                                        )}
                                      </div>
                                      <select
                                        value={sel.id}
                                        onChange={(e) =>
                                          updateMultiIdea(bCfg.bodyIdx, ideaIdx, {
                                            id: Number(e.target.value)
                                          })
                                        }
                                        className="w-full text-xs sm:text-sm font-bold border border-slate-300 rounded-lg px-2.5 py-1.5 bg-white text-slate-800"
                                      >
                                        {([1, 2, 3] as const).map((tier) => (
                                          <optgroup
                                            key={tier}
                                            label={PILLAR_TIER_META[tier].optgroupLabel}
                                          >
                                            {WT2_PILLARS.filter((p) => p.tier === tier).map((p) => (
                                              <option key={p.id} value={p.id}>
                                                {p.id}. {p.name} — {p.viName}
                                              </option>
                                            ))}
                                          </optgroup>
                                        ))}
                                      </select>
                                    </div>
                                  );
                                })()}

                                {/* Row 3: Compact 1–2 sentence draggable/clickable cards */}
                                <div className="space-y-1.5">
                                  {colsForIdea.map((col) => {
                                    const unitKey = makeSlotUnitKey(bCfg.bodyIdx, col, ideaIdx);
                                    const isPlaced = !!slottedPillarKeys[unitKey];
                                    const isSelected =
                                      selectedCard?.bodyIndex === bCfg.bodyIdx &&
                                      selectedCard?.ideaIndex === ideaIdx &&
                                      selectedCard?.col === col;
                                    const textDisplay =
                                      difficulty === 'level1'
                                        ? getBranchValue(bCfg.bodyIdx, col, ideaIdx)
                                        : `🔑 Mỏ neo gọn: ${getBranchAnchor(
                                            bCfg.bodyIdx,
                                            col,
                                            ideaIdx
                                          )}`;

                                    return (
                                      <div
                                        key={col}
                                        draggable={difficulty === 'level1' && !isPlaced}
                                        onDragStart={(e) => {
                                          e.dataTransfer.setData(
                                            'application/json',
                                            JSON.stringify({
                                              bodyIndex: bCfg.bodyIdx,
                                              ideaIndex: ideaIdx,
                                              col
                                            })
                                          );
                                          setSelectedCard({
                                            bodyIndex: bCfg.bodyIdx,
                                            ideaIndex: ideaIdx,
                                            col
                                          });
                                        }}
                                        onClick={() => {
                                          if (difficulty === 'level2') return;
                                          if (isPlaced) {
                                            setSlottedPillarKeys((prev) => ({
                                              ...prev,
                                              [unitKey]: false
                                            }));
                                            return;
                                          }
                                          setSelectedCard(
                                            isSelected
                                              ? null
                                              : {
                                                  bodyIndex: bCfg.bodyIdx,
                                                  ideaIndex: ideaIdx,
                                                  col
                                                }
                                          );
                                        }}
                                        className={`p-2 rounded-lg border text-xs leading-relaxed transition-all select-none ${
                                          difficulty === 'level2'
                                            ? 'bg-purple-50 border-purple-200 text-purple-900 font-semibold'
                                            : isPlaced
                                            ? 'bg-emerald-50/80 border-emerald-300 text-emerald-800 opacity-65 cursor-pointer'
                                            : isSelected
                                            ? 'bg-sky-50 border-sky-500 ring-2 ring-sky-400 shadow-sm cursor-pointer'
                                            : 'bg-slate-50/80 border-slate-200 hover:border-indigo-400 cursor-grab active:cursor-grabbing'
                                        }`}
                                      >
                                        <div className="flex items-center justify-between gap-2 mb-0.5">
                                          <span
                                            className={`text-[10px] font-extrabold uppercase px-2 py-0.5 rounded border ${COL_LABELS[col].color}`}
                                          >
                                            {isPlaced
                                              ? `✓ Đã lắp [${COL_LABELS[col].badge} • B${bCfg.bodyIdx}.${ideaIdx}] (Bấm để gỡ)`
                                              : `${COL_LABELS[col].badge} (Ý ${bCfg.bodyIdx}.${ideaIdx})`}
                                          </span>
                                          {isSelected && !isPlaced && (
                                            <span className="text-[11px] font-bold text-sky-700 animate-pulse">
                                              👉 Bấm ô [B{bCfg.bodyIdx}•Ý{ideaIdx}] bên dưới!
                                            </span>
                                          )}
                                        </div>
                                        <div>{textDisplay}</div>
                                      </div>
                                    );
                                  })}
                                </div>
                              </div>
                            );
                          })}
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}

              {crossBodyLinkerWarning && (
                <div className="bg-amber-50 border border-amber-300 rounded-xl px-4 py-2.5 flex flex-wrap items-center justify-between gap-2 text-xs text-amber-950">
                  <span>🔗 {crossBodyLinkerWarning}</span>
                  <button
                    type="button"
                    onClick={() => setLinkers({ ...DEFAULT_LINKERS })}
                    className="px-2.5 py-1 rounded-md bg-amber-600 hover:bg-amber-700 text-white font-bold cursor-pointer shrink-0"
                  >
                    ⚡ Đổi bộ từ nối chuẩn không trùng
                  </button>
                </div>
              )}

              {/* Feedback Toast for Slot Placement */}
              <div className="flex flex-wrap items-center justify-between gap-2 bg-white border border-slate-200 rounded-xl px-4 py-2.5">
                <div className="text-xs font-bold text-slate-700 flex items-center gap-2 flex-wrap">
                  <span>
                    Tiến độ lắp thẻ Pillar:{' '}
                    <span className="text-sky-700 font-extrabold">
                      {difficulty === 'level2'
                        ? 'Chế độ tự gõ từ mỏ neo'
                        : `${slottedCount} / ${requiredPillarUnitKeys.length} ô`}
                    </span>
                  </span>
                  {slotFeedback && (
                    <span
                      className={`px-2.5 py-1 rounded-full text-xs font-bold ${
                        slotFeedback.type === 'ok'
                          ? 'bg-emerald-100 text-emerald-800'
                          : 'bg-rose-100 text-rose-700'
                      }`}
                    >
                      {slotFeedback.msg}
                    </span>
                  )}
                </div>

                {difficulty === 'level1' && (
                  <button
                    onClick={handleAutoFillAllPillarSlots}
                    className="text-xs font-bold text-sky-700 hover:text-sky-900 underline cursor-pointer"
                  >
                    {bodyMode === 'multi'
                      ? '⚡ Lắp nhanh toàn bộ thẻ Trụ ý rút gọn (1–2 câu/ý)'
                      : '⚡ Đã thuộc thứ tự cột? Bấm lắp nhanh toàn bộ thẻ Pillar'}
                  </button>
                )}
              </div>

              {/* 1C. Invariant Structure Canvas */}
              <div className="space-y-4">
                {paragraphs.map((para, pIdx) => (
                  <div
                    key={pIdx}
                    className="bg-white rounded-xl p-4 sm:p-5 shadow-2xs border border-slate-200"
                    style={{ borderLeft: `5px solid ${para.borderColor}` }}
                  >
                    <h4
                      className="font-extrabold text-sm sm:text-base mb-3"
                      style={{ color: para.borderColor }}
                    >
                      {para.sectionTitle}
                    </h4>
                    <div className="text-[15px] leading-[2.3] text-slate-800">
                      {para.tokens.map((tok, tIdx) => {
                        if (tok.type === 'text') {
                          return (
                            <span key={tIdx} className="font-semibold text-slate-800">
                              {tok.text}
                            </span>
                          );
                        }

                        if (tok.type === 'linker_select' && tok.slotKey) {
                          const role: LinkerRole = tok.linkerRole || 'start';
                          const roleOpts = WT2_LINKER_ROLE_OPTIONS[role];
                          const curVal = linkers[tok.slotKey] || roleOpts[0].en;
                          return (
                            <select
                              key={tIdx}
                              value={curVal}
                              onChange={(e) =>
                                setLinkers((prev) => ({
                                  ...prev,
                                  [tok.slotKey!]: e.target.value
                                }))
                              }
                              title="Chọn Linking Word mở ý (tránh lặp từ nối giữa các câu/đoạn)"
                              className="inline-block mx-1 my-0.5 px-2.5 py-0.5 rounded-lg border-2 border-indigo-300 bg-indigo-50 text-indigo-900 font-extrabold text-sm cursor-pointer focus:outline-none focus:ring-2 focus:ring-indigo-500"
                            >
                              {roleOpts.map((opt) => (
                                <option key={opt.en} value={opt.en}>
                                  🔗 {opt.en}
                                </option>
                              ))}
                            </select>
                          );
                        }

                        if (tok.type === 'topic_input' && tok.slotKey) {
                          const val = topicInputs[tok.slotKey] || '';
                          return (
                            <input
                              key={tIdx}
                              type="text"
                              value={val}
                              onChange={(e) =>
                                setTopicInputs((prev) => ({
                                  ...prev,
                                  [tok.slotKey!]: e.target.value
                                }))
                              }
                              placeholder={tok.placeholder}
                              style={{
                                width: `${Math.min(520, Math.max(210, (val.length || (tok.placeholder?.length || 24)) * 7.8))}px`,
                                maxWidth: '100%'
                              }}
                              className="inline-block mx-1 my-0.5 px-3 py-0.5 rounded-lg border border-sky-300 bg-sky-50/70 text-sky-900 font-medium text-sm focus:outline-none focus:ring-2 focus:ring-sky-500 focus:bg-white placeholder:text-sky-600/70"
                            />
                          );
                        }

                        if (tok.type === 'pillar_slot' && tok.bodyIndex && tok.pillarCol) {
                          const unitKey = makeSlotUnitKey(
                            tok.bodyIndex,
                            tok.pillarCol,
                            tok.ideaIndex
                          );
                          const colInfo = COL_LABELS[tok.pillarCol];
                          const slotTag = tok.ideaIndex
                            ? `${colInfo.badge} • B${tok.bodyIndex}.${tok.ideaIndex}`
                            : `${colInfo.badge} ${tok.bodyIndex}`;

                          // Level 2: Free-recall input with anchor hint
                          if (difficulty === 'level2') {
                            const memVal = memoryPillarTexts[unitKey] || '';
                            return (
                              <span key={tIdx} className="inline-block mx-1 my-1 align-middle max-w-full">
                                <input
                                  type="text"
                                  value={memVal}
                                  onChange={(e) =>
                                    setMemoryPillarTexts((prev) => ({
                                      ...prev,
                                      [unitKey]: e.target.value
                                    }))
                                  }
                                  placeholder={`[${slotTag}] 🔑 ${getBranchAnchor(
                                    tok.bodyIndex,
                                    tok.pillarCol,
                                    tok.ideaIndex
                                  )}`}
                                  style={{ width: '460px', maxWidth: '100%' }}
                                  className="px-3 py-1 rounded-lg border-2 border-purple-300 bg-purple-50/70 text-purple-950 font-medium text-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:bg-white"
                                />
                              </span>
                            );
                          }

                          // Level 1: Droppable / Click-to-place slot
                          const isFilled = !!slottedPillarKeys[unitKey];
                          const filledText = getBranchValue(
                            tok.bodyIndex,
                            tok.pillarCol,
                            tok.ideaIndex
                          );

                          return (
                            <span
                              key={tIdx}
                              onDragOver={(e) => e.preventDefault()}
                              onDrop={(e) => {
                                e.preventDefault();
                                try {
                                  const raw = JSON.parse(
                                    e.dataTransfer.getData('application/json')
                                  );
                                  attemptPlaceCard(
                                    raw.bodyIndex,
                                    raw.col,
                                    tok.bodyIndex!,
                                    tok.pillarCol!,
                                    raw.ideaIndex,
                                    tok.ideaIndex
                                  );
                                } catch {
                                  // ignore invalid drag payload
                                }
                              }}
                              onClick={() => {
                                if (selectedCard) {
                                  attemptPlaceCard(
                                    selectedCard.bodyIndex,
                                    selectedCard.col,
                                    tok.bodyIndex!,
                                    tok.pillarCol!,
                                    selectedCard.ideaIndex,
                                    tok.ideaIndex
                                  );
                                } else if (isFilled) {
                                  setSlottedPillarKeys((prev) => ({
                                    ...prev,
                                    [unitKey]: false
                                  }));
                                }
                              }}
                              title={
                                isFilled
                                  ? 'Bấm để gỡ thẻ ra'
                                  : 'Kéo thẻ Pillar thả vào đây (hoặc bấm chọn thẻ ở trên rồi bấm vào ô này)'
                              }
                              className={`inline mx-1 px-3 py-1 rounded-xl border-2 text-sm transition-all cursor-pointer ${
                                isFilled
                                  ? 'bg-emerald-50 border-emerald-400 text-emerald-950 font-medium'
                                  : selectedCard
                                  ? 'bg-amber-50 border-dashed border-amber-500 text-amber-900 font-bold animate-pulse'
                                  : 'bg-slate-100 border-dashed border-slate-400 text-slate-600 font-bold hover:border-sky-500 hover:text-sky-700'
                              }`}
                            >
                              {isFilled ? `✅ ${filledText}` : `📥 [${slotTag}]`}
                            </span>
                          );
                        }

                        return null;
                      })}
                    </div>
                  </div>
                ))}
              </div>
                </>
              )}
            </>
          )}

          {/* -------------------- STEP 2: SELF-EDIT & POLISH SEAMS -------------------- */}
          {step === 2 && (
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-5">
              {/* Left 8 cols: Main Essay Editor */}
              <div className="lg:col-span-8 space-y-3">
                <div className="bg-white rounded-xl border border-slate-200 p-4 shadow-2xs space-y-3">
                  <div className="flex flex-wrap items-center justify-between gap-2">
                    <div>
                      <span className="text-xs font-extrabold uppercase text-sky-600">
                        Bước 2 • Tự Biên Tập &amp; Mài Mượt Mối Nối
                      </span>
                      <h3 className="font-bold text-slate-900 text-sm sm:text-base">
                        Thay toàn bộ chỗ <code className="bg-amber-100 px-1 rounded">[...]</code>{' '}
                        bằng từ ngữ gắn sát đề bài &amp; kiểm tra ngữ pháp
                      </h3>
                    </div>

                    <div className="flex items-center gap-2">
                      <span
                        className={`px-3 py-1 rounded-full text-xs font-extrabold ${
                          wordCount >= 250
                            ? 'bg-emerald-100 text-emerald-800 border border-emerald-300'
                            : 'bg-amber-100 text-amber-800 border border-amber-300'
                        }`}
                      >
                        📝 {wordCount} / 250+ words {wordCount >= 250 ? '✓ Đạt chuẩn' : '(Cần ≥ 250 từ)'}
                      </span>
                    </div>
                  </div>

                  {/* Live Bracket & Seam Detector */}
                  {bracketWarnings.length > 0 ? (
                    <div className="bg-amber-50 border border-amber-300 rounded-lg p-3 space-y-1.5">
                      <div className="text-xs font-extrabold text-amber-900">
                        ⚠️ Phát hiện {bracketWarnings.length} vị trí ký hiệu nháp cần em thay bằng từ cụ thể của đề bài (Bấm vào thẻ để nhảy tới đúng chỗ đó):
                      </div>
                      <div className="flex flex-wrap gap-1.5">
                        {bracketWarnings.map((tag) => (
                          <button
                            key={tag}
                            onClick={() => highlightBracketInEditor(tag)}
                            className="px-2.5 py-1 rounded-md bg-white border border-amber-400 text-amber-900 text-xs font-bold hover:bg-amber-100 cursor-pointer"
                          >
                            🔍 {tag}
                          </button>
                        ))}
                      </div>
                    </div>
                  ) : (
                    <div className="bg-emerald-50 border border-emerald-300 rounded-lg px-3 py-2 text-xs font-bold text-emerald-800">
                      ✅ Tuyệt vời! Không còn sót ký hiệu ngoặc vuông [...] nháp nào trong bài viết.
                    </div>
                  )}

                  {duplicateConnectorWarnings.length > 0 && (
                    <div className="bg-rose-50 border border-rose-300 rounded-lg px-3 py-2 text-xs font-bold text-rose-800">
                      ⚠️ Lưu ý gọt từ nối bị lặp: {duplicateConnectorWarnings.join(' • ')}
                    </div>
                  )}

                  <textarea
                    ref={textareaRef}
                    value={essayDraft}
                    onChange={(e) => setEssayDraft(e.target.value)}
                    rows={16}
                    spellCheck
                    className="w-full rounded-xl border border-slate-300 p-4 text-[15.5px] leading-relaxed text-slate-800 font-sans focus:outline-none focus:ring-2 focus:ring-sky-500 bg-white resize-y"
                    placeholder="Bài viết ghép từ Khung bất biến + Trụ ý Pillars sẽ hiện tại đây để em biên tập..."
                  />
                </div>
              </div>

              {/* Right 4 cols: Subject Bank S / Linking Words + 4-Point Checklist */}
              <div className="lg:col-span-4 space-y-4">
                {/* Click-to-insert Helper Bank (Subjects S | Linking Words) */}
                <div className="bg-white rounded-xl border border-slate-200 p-4 shadow-2xs space-y-3">
                  <div className="grid grid-cols-2 gap-1 bg-slate-100 p-1 rounded-xl text-xs font-extrabold">
                    <button
                      type="button"
                      onClick={() => setHelperBankTab('subjects')}
                      className={`py-1.5 px-2 rounded-lg cursor-pointer transition-all ${
                        helperBankTab === 'subjects'
                          ? 'bg-white text-indigo-800 shadow-2xs'
                          : 'text-slate-600 hover:text-slate-900'
                      }`}
                    >
                      👤 Chủ ngữ (S)
                    </button>
                    <button
                      type="button"
                      onClick={() => setHelperBankTab('linkers')}
                      className={`py-1.5 px-2 rounded-lg cursor-pointer transition-all ${
                        helperBankTab === 'linkers'
                          ? 'bg-white text-indigo-800 shadow-2xs'
                          : 'text-slate-600 hover:text-slate-900'
                      }`}
                    >
                      🔗 Linking Words
                    </button>
                  </div>

                  {helperBankTab === 'subjects' ? (
                    <>
                      <div>
                        <span className="text-[11px] font-extrabold uppercase text-indigo-600">
                          Kho Chủ Ngữ (S) Nâng Cao — Trang 4 Pillars
                        </span>
                        <p className="text-xs text-slate-500 mt-0.5">
                          Bôi đen chữ <code className="bg-slate-100 px-1 rounded">[S]</code> hoặc{' '}
                          <code className="bg-slate-100 px-1 rounded">people</code> bên trái rồi bấm từ để thay thế ngay:
                        </p>
                      </div>

                      <div className="grid grid-cols-2 gap-1.5">
                        {WT2_SUBJECT_GROUPS.map((g) => (
                          <button
                            key={g.id}
                            onClick={() => setActiveSubjectGroup(g.id)}
                            className={`px-2 py-1.5 rounded-lg text-[11px] font-bold text-left truncate cursor-pointer border ${
                              activeSubjectGroup === g.id
                                ? 'bg-indigo-600 text-white border-indigo-600'
                                : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                            }`}
                          >
                            {g.title}
                          </button>
                        ))}
                      </div>

                      {WT2_SUBJECT_GROUPS.filter((g) => g.id === activeSubjectGroup).map((g) => (
                        <div key={g.id} className="space-y-2">
                          <div className="text-[11px] text-slate-500 italic">{g.subtitle}</div>
                          <div className="flex flex-wrap gap-1.5">
                            {g.chips.map((c) => (
                              <button
                                key={c.en}
                                onClick={() => insertSubjectAtCursor(c.en)}
                                className="px-2.5 py-1 rounded-lg bg-indigo-50 hover:bg-indigo-100 border border-indigo-200 text-xs text-indigo-900 font-bold cursor-pointer transition-colors"
                                title={`Chèn "${c.en}" (${c.vi})`}
                              >
                                + {c.en}{' '}
                                <span className="font-normal text-indigo-600 text-[11px]">
                                  ({c.vi})
                                </span>
                              </button>
                            ))}
                          </div>
                        </div>
                      ))}
                    </>
                  ) : (
                    <>
                      <div>
                        <span className="text-[11px] font-extrabold uppercase text-indigo-600">
                          Kho Linking Words Điểm Cao — Trang 5 Pillars
                        </span>
                        <p className="text-xs text-slate-500 mt-0.5">
                          Đặt con trỏ vào đầu câu hoặc giữa 2 mệnh đề bên trái rồi bấm để chèn mượt mà:
                        </p>
                      </div>

                      <div className="grid grid-cols-2 gap-1.5">
                        {WT2_LINKING_GROUPS.map((g) => (
                          <button
                            key={g.id}
                            onClick={() => setActiveLinkingGroup(g.id)}
                            className={`px-2 py-1.5 rounded-lg text-[11px] font-bold text-left truncate cursor-pointer border ${
                              activeLinkingGroup === g.id
                                ? 'bg-indigo-600 text-white border-indigo-600'
                                : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                            }`}
                          >
                            {g.title}
                          </button>
                        ))}
                      </div>

                      {WT2_LINKING_GROUPS.filter((g) => g.id === activeLinkingGroup).map((g) => (
                        <div key={g.id} className="space-y-2">
                          <div className="text-[11px] text-slate-500 italic">{g.subtitle}</div>
                          <div className="flex flex-wrap gap-1.5">
                            {g.chips.map((c) => (
                              <button
                                key={c.en}
                                onClick={() => insertSubjectAtCursor(c.en)}
                                className="px-2.5 py-1 rounded-lg bg-violet-50 hover:bg-violet-100 border border-violet-200 text-xs text-violet-900 font-bold cursor-pointer transition-colors"
                                title={`Chèn "${c.en}" (${c.vi})`}
                              >
                                + {c.en.trim()}{' '}
                                <span className="font-normal text-violet-600 text-[11px]">
                                  ({c.vi})
                                </span>
                              </button>
                            ))}
                          </div>
                        </div>
                      ))}
                    </>
                  )}
                </div>

                {/* 4-Point Self-Edit Checklist */}
                <div className="bg-white rounded-xl border border-slate-200 p-4 shadow-2xs space-y-2.5">
                  <div className="text-xs font-extrabold uppercase text-emerald-700">
                    ✅ Checklist 4 Điểm Mài Mối Nối Trước Khi Nộp
                  </div>
                  {(bodyMode === 'multi'
                    ? [
                        'Đã thay hết [S] và [...] bằng chủ ngữ & danh từ sát đề bài',
                        'Mỗi Body có Topic Sentence chia chuẩn số ít (1 ý) / số nhiều (2–5 ý) + Linking Words đa dạng (không lặp từ nối)',
                        'Mỗi Trụ ý được triển khai súc tích 1–2 câu (có Nhân–Quả gọn, không liệt kê cụt ngủn)',
                        'Độ dài bài viết đạt từ 250–320 từ chuẩn mực, chia rõ 4 đoạn văn'
                      ]
                    : [
                        'Đã thay hết [S] và [...] bằng chủ ngữ & danh từ sát đề bài',
                        'Sau giới từ "due to / related to / of" đã chia chuẩn V-ing hoặc Cụm danh từ',
                        'Ví dụ số liệu (WHO, VietnamWorks, World Bank...) đã gắn đúng ngữ cảnh đề',
                        'Độ dài bài viết đạt từ 250 từ trở lên, chia rõ 4 đoạn văn'
                      ]
                  ).map((item, idx) => (
                    <label
                      key={idx}
                      className="flex items-start gap-2 text-xs text-slate-700 cursor-pointer select-none"
                    >
                      <input
                        type="checkbox"
                        checked={checklist[idx]}
                        onChange={(e) => {
                          const next = [...checklist] as [boolean, boolean, boolean, boolean];
                          next[idx] = e.target.checked;
                          setChecklist(next);
                        }}
                        className="mt-0.5 rounded border-slate-300 text-emerald-600 focus:ring-emerald-500"
                      />
                      <span>{item}</span>
                    </label>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* -------------------- STEP 3: AI DUAL EVALUATION -------------------- */}
          {step === 3 && (
            <div className="space-y-5">
              {isGrading && (
                <div className="bg-white rounded-2xl border border-slate-200 p-10 text-center space-y-3 shadow-xs">
                  <div className="w-12 h-12 border-4 border-sky-200 border-t-sky-600 rounded-full animate-spin mx-auto" />
                  <h3 className="font-extrabold text-slate-900 text-lg">
                    Giám khảo AI đang chấm kép bài viết của em...
                  </h3>
                  <p className="text-sm text-slate-500 max-w-md mx-auto">
                    {bodyMode === 'multi'
                      ? `Đang đối chiếu 4 tiêu chí IELTS quốc tế cùng công thức Phiên bản 2 (Topic Sentence + ${b1IdeaCount + b2IdeaCount} Trụ ý rút gọn 1–2 câu/ý + Linking Words).`
                      : `Đang đối chiếu đồng thời 4 tiêu chí IELTS chuẩn quốc tế và độ nhuần nhuyễn của Khung bất biến + Trụ ý (${pillar1.name} & ${pillar2.name}).`}
                  </p>
                </div>
              )}

              {!isGrading && gradeError && (
                <div className="bg-rose-50 border border-rose-200 rounded-xl p-6 text-center space-y-3">
                  <div className="text-rose-700 font-bold">{gradeError}</div>
                  <div className="flex justify-center gap-3">
                    <button
                      onClick={() => setStep(2)}
                      className="px-4 py-2 rounded-lg border border-slate-300 bg-white text-slate-700 text-sm font-bold cursor-pointer"
                    >
                      ← Quay lại Bước 2
                    </button>
                    <button
                      onClick={handleSubmitToAiGrader}
                      className="px-4 py-2 rounded-lg bg-sky-600 text-white text-sm font-bold cursor-pointer"
                    >
                      🔄 Chấm lại
                    </button>
                  </div>
                </div>
              )}

              {!isGrading && aiEvaluation && (
                <>
                  {/* Saved Submission History & Quick Actions Bar */}
                  <div className="bg-emerald-50/90 border border-emerald-300 rounded-xl px-4 py-3 flex flex-wrap items-center justify-between gap-3 text-xs">
                    <div className="flex items-center gap-2 flex-wrap">
                      <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-emerald-600 text-white font-extrabold">
                        💾 Đã lưu bài chấm vào đề này
                      </span>
                      {(() => {
                        const activeRec =
                          savedSubmissions.find((x) => x.id === selectedSavedId) ||
                          savedSubmissions[0];
                        return activeRec?.createdAt ? (
                          <span className="text-emerald-900 font-semibold">
                            🕒 Chấm lúc: {formatSavedTimestamp(activeRec.createdAt)}
                          </span>
                        ) : null;
                      })()}

                      {savedSubmissions.length > 1 && (
                        <div className="flex items-center gap-1 flex-wrap ml-1">
                          <span className="text-slate-600 font-bold">Lịch sử các lần chấm:</span>
                          {savedSubmissions.map((rec, idx) => {
                            const attemptNo = savedSubmissions.length - idx;
                            const isCurrent =
                              (selectedSavedId ? rec.id === selectedSavedId : idx === 0);
                            return (
                              <button
                                key={rec.id}
                                type="button"
                                onClick={() => applySavedSubmissionToState(rec, true)}
                                className={`px-2.5 py-1 rounded-lg border font-extrabold cursor-pointer transition-all ${
                                  isCurrent
                                    ? 'bg-indigo-600 text-white border-indigo-600 shadow-2xs'
                                    : 'bg-white text-slate-700 border-slate-300 hover:border-indigo-400'
                                }`}
                              >
                                Lần #{attemptNo}: Band {rec.overall} (
                                {rec.bodyMode === 'multi' ? 'V2 Đa ý' : 'V1 PEEL'})
                              </button>
                            );
                          })}
                        </div>
                      )}
                    </div>

                    <div className="flex items-center gap-2 flex-wrap">
                      <button
                        type="button"
                        onClick={() => setStep(2)}
                        className="px-3 py-1.5 rounded-lg bg-white border border-sky-300 text-sky-800 hover:bg-sky-50 font-extrabold cursor-pointer"
                      >
                        ✏️ Sửa bài viết này (Bước 2)
                      </button>
                      <button
                        type="button"
                        onClick={handleStartFreshAttempt}
                        className="px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold cursor-pointer"
                        title="Giữ nguyên lịch sử chấm cũ và mở khung trống để luyện ghép lại đề này từ đầu"
                      >
                        🆕 Luyện ghép lại từ đầu (Bước 1)
                      </button>
                    </div>
                  </div>

                  {/* Hero Score Banner */}
                  <div className="bg-gradient-to-r from-slate-900 via-[#0a5482] to-indigo-900 text-white rounded-2xl p-5 sm:p-6 flex flex-wrap items-center justify-between gap-4 shadow-md">
                    <div className="space-y-1">
                      <div className="flex items-center gap-2 flex-wrap">
                        <span className="bg-emerald-400/20 text-emerald-200 border border-emerald-400/40 text-xs font-extrabold px-2.5 py-0.5 rounded-full">
                          ✓ Hoàn thành chấm kép ({bodyMode === 'multi' ? 'Phiên bản 2 • Đa ý' : 'Phiên bản 1 • PEEL'})
                        </span>
                        {taskMarkedDone && (
                          <span className="bg-amber-400/20 text-amber-200 border border-amber-400/40 text-xs font-extrabold px-2.5 py-0.5 rounded-full">
                            🎯 Đã tự động tích xanh bài tập Topic trên thanh tiến độ!
                          </span>
                        )}
                      </div>
                      <h3 className="text-lg sm:text-xl font-black">
                        Kết Quả Đánh Giá Từ Giám Khảo TonyEnglish AI
                      </h3>
                      <p className="text-xs sm:text-sm text-sky-100 max-w-2xl">
                        {aiEvaluation.generalFeedback}
                      </p>
                    </div>

                    <div className="flex items-center gap-3">
                      <div className="bg-white/10 border border-white/20 rounded-2xl px-4 py-3 text-center">
                        <div className="text-[11px] uppercase font-bold text-sky-200">
                          IELTS Overall
                        </div>
                        <div className="text-3xl font-black text-amber-300">
                          {aiEvaluation.overall}
                        </div>
                      </div>
                      <div className="bg-white/10 border border-white/20 rounded-2xl px-4 py-3 text-center">
                        <div className="text-[11px] uppercase font-bold text-emerald-200">
                          Khung + Pillars
                        </div>
                        <div className="text-3xl font-black text-emerald-300">
                          {aiEvaluation.formulaScore ?? '8.5'}
                          <span className="text-sm font-bold text-white/70">/10</span>
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* TonyEnglish Formula Review (3 cards) */}
                  {aiEvaluation.formulaReview && (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                      <div className="bg-sky-50 border border-sky-200 rounded-xl p-4 space-y-1.5">
                        <div className="text-xs font-extrabold uppercase text-sky-800">
                          📐 1. Độ chuẩn Khung Bất Biến
                        </div>
                        <p className="text-xs sm:text-sm text-slate-700 leading-relaxed">
                          {aiEvaluation.formulaReview.structureCheck}
                        </p>
                      </div>
                      <div className="bg-violet-50 border border-violet-200 rounded-xl p-4 space-y-1.5">
                        <div className="text-xs font-extrabold uppercase text-violet-800">
                          {bodyMode === 'multi'
                            ? '🏛️ 2. Độ khớp Đa Trụ Ý (Rút gọn 1–2 câu/ý)'
                            : '🏛️ 2. Độ khớp 2 Trụ Ý Pillars'}
                        </div>
                        <p className="text-xs sm:text-sm text-slate-700 leading-relaxed">
                          {aiEvaluation.formulaReview.pillarFitCheck}
                        </p>
                      </div>
                      <div className="bg-amber-50 border border-amber-200 rounded-xl p-4 space-y-1.5">
                        <div className="text-xs font-extrabold uppercase text-amber-900">
                          {bodyMode === 'multi'
                            ? '🔗 3. Linking Words & Ngữ Pháp Mối Nối'
                            : '🔗 3. Ngữ Pháp Tại Mối Nối'}
                        </div>
                        <p className="text-xs sm:text-sm text-slate-700 leading-relaxed">
                          {aiEvaluation.formulaReview.seamGrammarCheck}
                        </p>
                      </div>
                    </div>
                  )}

                  {/* 4 IELTS Criteria */}
                  {Array.isArray(aiEvaluation.criteria) && (
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                      {aiEvaluation.criteria.map((c: any, idx: number) => (
                        <div
                          key={idx}
                          className="bg-white border border-slate-200 rounded-xl p-4 shadow-2xs space-y-1.5"
                        >
                          <div className="flex items-center justify-between">
                            <span className="font-extrabold text-sm text-slate-900">{c.name}</span>
                            <span className="px-2.5 py-0.5 rounded-lg bg-sky-100 text-sky-800 font-black text-sm">
                              Band {c.score}
                            </span>
                          </div>
                          <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
                            {c.comment}
                          </p>
                        </div>
                      ))}
                    </div>
                  )}

                  {/* Inline Red/Green Corrected Essay */}
                  {aiEvaluation.correctedHtml && (
                    <div className="bg-white border border-slate-200 rounded-xl p-5 shadow-2xs space-y-3">
                      <div className="flex items-center justify-between flex-wrap gap-2 border-b border-slate-100 pb-2.5">
                        <h4 className="font-extrabold text-slate-900 text-sm sm:text-base">
                          🖊️ Bài Chữa Chi Tiết Trực Tiếp Trên Câu Chữ Của Em
                        </h4>
                        <div className="flex items-center gap-3 text-xs">
                          <span className="bg-red-100 text-red-700 line-through px-2 py-0.5 rounded">
                            Chỗ còn gượng / sai
                          </span>
                          <span className="bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded">
                            Bản nâng cấp mượt Band 8.0+
                          </span>
                        </div>
                      </div>
                      <div
                        className="text-[15.5px] leading-8 text-slate-800"
                        dangerouslySetInnerHTML={{ __html: aiEvaluation.correctedHtml }}
                      />
                    </div>
                  )}
                </>
              )}
            </div>
          )}
        </div>

        {/* ==================== STICKY FOOTER ACTIONS ==================== */}
        <div className="bg-white border-t border-slate-200 px-4 sm:px-6 py-3 flex flex-wrap items-center justify-between gap-3 shrink-0">
          {step === 1 && (
            <>
              <div className="text-xs text-slate-500">
                Mẹo: Chưa cần hoàn hảo 100% ở Bước 1 — sang Bước 2 em sẽ được gọt câu tự do!
              </div>
              <button
                onClick={handleProceedToStep2}
                className="px-5 py-2.5 rounded-xl bg-gradient-to-r from-[#0a5482] to-sky-600 hover:from-[#084268] hover:to-sky-700 text-white font-extrabold text-sm shadow-sm cursor-pointer transition-all"
              >
                Sang Bước 2: Ghép thành bài &amp; Tự biên tập →
              </button>
            </>
          )}

          {step === 2 && (
            <>
              <button
                onClick={() => setStep(1)}
                className="px-4 py-2 rounded-xl border border-slate-300 text-slate-700 hover:bg-slate-50 font-bold text-xs sm:text-sm cursor-pointer"
              >
                ← Quay lại Bước 1 đổi Trụ ý
              </button>
              <button
                onClick={handleSubmitToAiGrader}
                className="px-5 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 text-white font-extrabold text-sm shadow-sm cursor-pointer transition-all"
              >
                🚀 Nộp Bài Cho Giám Khảo AI Chấm Điểm (Bước 3)
              </button>
            </>
          )}

          {step === 3 && !isGrading && (
            <>
              <div className="flex items-center gap-2 flex-wrap">
                <button
                  onClick={() => setStep(2)}
                  className="px-4 py-2 rounded-xl border border-sky-300 bg-sky-50 text-sky-800 hover:bg-sky-100 font-bold text-xs sm:text-sm cursor-pointer"
                >
                  ✏️ Quay lại Bước 2 sửa theo góp ý AI để nâng Band
                </button>
                <button
                  onClick={handleStartFreshAttempt}
                  className="px-3.5 py-2 rounded-xl border border-indigo-300 bg-indigo-50 text-indigo-800 hover:bg-indigo-100 font-bold text-xs sm:text-sm cursor-pointer"
                >
                  🆕 Ghép bản mới từ đầu
                </button>
              </div>
              <button
                onClick={onClose}
                className="px-5 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-extrabold text-sm cursor-pointer"
              >
                ✅ Hoàn tất &amp; Đóng (Đã lưu)
              </button>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

// ============================================================================
// MINI-GAME PHẢN XẠ 60 GIÂY: BẮT DẠNG KHUNG + NHẶT 2 TRỤ Ý & FLASH-DRILL 19 PILLARS
// ============================================================================

interface Wt2PillarReflexModalProps {
  isOpen: boolean;
  initialTab?: 'reflex' | 'anchors';
  onClose: () => void;
  onLaunchStudioFromReflex?: (payload: Wt2StudioOpenPayload) => void;
}

const STORAGE_MEMORIZED_KEY = 'tony_wt2_memorized_pillars_v1';

export const Wt2PillarReflexModal: React.FC<Wt2PillarReflexModalProps> = ({
  isOpen,
  initialTab = 'reflex',
  onClose,
  onLaunchStudioFromReflex
}) => {
  const [tab, setTab] = useState<'reflex' | 'anchors'>(initialTab);

  // ---- Tab 1: 60s Topic Reflex State ----
  const [deck, setDeck] = useState<ReflexQuestion[]>([]);
  const [qIdx, setQIdx] = useState(0);
  const [pickedCat, setPickedCat] = useState<Wt2Category | null>(null);
  const [pickedPillars, setPickedPillars] = useState<number[]>([]);
  const [reflexTierTab, setReflexTierTab] = useState<1 | 2 | 3>(1);
  const [checked, setChecked] = useState(false);
  const [score, setScore] = useState(0);
  const [streak, setStreak] = useState(0);
  const [timerEnabled, setTimerEnabled] = useState(true);
  const [secondsLeft, setSecondsLeft] = useState(60);

  // ---- Tab 2: 4-Anchor Memory Drill State ----
  const [anchorMode, setAnchorMode] = useState<'cards' | 'quiz'>('cards');
  const [tierFilter, setTierFilter] = useState<0 | 1 | 2 | 3>(1);
  const [quizCoreOnly, setQuizCoreOnly] = useState<boolean>(true);
  const [flippedIds, setFlippedIds] = useState<Record<number, boolean>>({});
  const [memorizedIds, setMemorizedIds] = useState<number[]>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_MEMORIZED_KEY);
      return saved ? JSON.parse(saved) : [];
    } catch {
      return [];
    }
  });

  // Anchor Speed Quiz state
  const [anchorQuizItem, setAnchorQuizItem] = useState<{
    clueType: string;
    clueText: string;
    correctId: number;
    options: Wt2Pillar[];
  } | null>(null);
  const [anchorQuizPicked, setAnchorQuizPicked] = useState<number | null>(null);
  const [anchorQuizStreak, setAnchorQuizStreak] = useState(0);

  const startNewReflexRound = () => {
    const shuffled = [...WT2_REFLEX_QUESTIONS].sort(() => Math.random() - 0.5).slice(0, 10);
    setDeck(shuffled);
    setQIdx(0);
    setPickedCat(null);
    setPickedPillars([]);
    setReflexTierTab(1);
    setChecked(false);
    setScore(0);
    setStreak(0);
    setSecondsLeft(60);
  };

  const generateNextAnchorQuiz = (overrideCoreOnly?: boolean) => {
    const coreOnly = overrideCoreOnly !== undefined ? overrideCoreOnly : quizCoreOnly;
    const pool = coreOnly ? WT2_PILLARS.filter((p) => p.tier <= 2) : WT2_PILLARS;
    const target = pool[Math.floor(Math.random() * pool.length)];
    const distractors = pool
      .filter((p) => p.id !== target.id)
      .sort(() => Math.random() - 0.5)
      .slice(0, 3);
    const options = [target, ...distractors].sort(() => Math.random() - 0.5);
    const branch = Math.random() > 0.5 ? target.positive : target.negative;
    const clueTypes = [
      { label: 'Số liệu & Ví dụ đặc trưng (Example)', idx: 3 },
      { label: 'Mỏ neo Nguyên nhân (Cause)', idx: 1 },
      { label: 'Mỏ neo Kết quả (Effect)', idx: 2 }
    ];
    const chosen = clueTypes[Math.floor(Math.random() * clueTypes.length)];
    setAnchorQuizItem({
      clueType: chosen.label,
      clueText: branch.anchors[chosen.idx],
      correctId: target.id,
      options
    });
    setAnchorQuizPicked(null);
  };

  useEffect(() => {
    if (!isOpen) return;
    setTab(initialTab);
    startNewReflexRound();
    generateNextAnchorQuiz();
  }, [isOpen, initialTab]);

  // 60s countdown timer for Tab 1
  useEffect(() => {
    if (!isOpen || tab !== 'reflex' || !timerEnabled || checked || deck.length === 0 || qIdx >= deck.length)
      return;
    if (secondsLeft <= 0) {
      setChecked(true);
      setStreak(0);
      return;
    }
    const id = window.setInterval(() => setSecondsLeft((s) => s - 1), 1000);
    return () => window.clearInterval(id);
  }, [isOpen, tab, timerEnabled, checked, secondsLeft, deck.length, qIdx]);

  const toggleMemorized = (id: number) => {
    setMemorizedIds((prev) => {
      const next = prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id];
      try {
        localStorage.setItem(STORAGE_MEMORIZED_KEY, JSON.stringify(next));
      } catch {
        // ignore storage quota errors
      }
      return next;
    });
  };

  if (!isOpen) return null;

  const currentQ = deck[qIdx];
  const togglePickPillar = (id: number) => {
    if (checked) return;
    setPickedPillars((prev) => {
      if (prev.includes(id)) return prev.filter((x) => x !== id);
      if (prev.length >= 2) return [prev[1], id];
      return [...prev, id];
    });
  };

  const handleCheckReflex = () => {
    if (!currentQ || !pickedCat || pickedPillars.length < 2) return;
    const catOk = pickedCat === currentQ.correctCategory;
    const pillarHits = pickedPillars.filter((id) => currentQ.bestPillars.includes(id)).length;
    const earned = (catOk ? 1 : 0) + (pillarHits >= 2 ? 2 : pillarHits === 1 ? 1 : 0);
    setScore((s) => s + earned);
    if (catOk && pillarHits >= 1) {
      setStreak((st) => st + 1);
    } else {
      setStreak(0);
    }
    setChecked(true);
  };

  const handleNextQuestion = () => {
    setQIdx((i) => i + 1);
    setPickedCat(null);
    setPickedPillars([]);
    setReflexTierTab(1);
    setChecked(false);
    setSecondsLeft(60);
  };

  return (
    <div className="fixed inset-0 z-[125] bg-slate-900/75 backdrop-blur-xs flex items-center justify-center p-2 sm:p-4 overflow-y-auto">
      <div className="bg-slate-50 w-full max-w-5xl rounded-2xl shadow-2xl border border-slate-200 flex flex-col max-h-[93vh] overflow-hidden">
        {/* Header */}
        <div className="bg-gradient-to-r from-indigo-900 via-violet-800 to-purple-800 text-white px-4 sm:px-6 py-3.5 flex flex-wrap items-center justify-between gap-3 shrink-0">
          <div className="flex items-center gap-2.5">
            <span className="text-2xl">⚡</span>
            <div>
              <h2 className="font-extrabold text-base sm:text-lg">
                Phòng Luyện Phản Xạ Khung Bất Biến &amp; Thuộc Lòng 19 Idea Pillars
              </h2>
              <p className="text-xs text-purple-200">
                Rèn phản xạ 60 giây đầu giờ thi: Đọc đề nhảy số ngay Dạng Khung + 2 Trụ ý chuẩn xác
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <div className="inline-flex bg-black/25 p-1 rounded-xl text-xs font-bold">
              <button
                onClick={() => setTab('reflex')}
                className={`px-3 py-1.5 rounded-lg cursor-pointer ${
                  tab === 'reflex' ? 'bg-white text-indigo-900' : 'text-white/85 hover:bg-white/10'
                }`}
              >
                ⚡ Phản Xạ Đọc Đề 60s
              </button>
              <button
                onClick={() => setTab('anchors')}
                className={`px-3 py-1.5 rounded-lg cursor-pointer ${
                  tab === 'anchors' ? 'bg-white text-indigo-900' : 'text-white/85 hover:bg-white/10'
                }`}
              >
                🧠 Thuộc Lòng 19 Pillars ({memorizedIds.length}/19)
              </button>
            </div>

            <button
              onClick={onClose}
              className="w-8 h-8 rounded-full bg-white/15 hover:bg-white/30 flex items-center justify-center text-white font-bold cursor-pointer"
            >
              ✕
            </button>
          </div>
        </div>

        {/* Body */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6">
          {/* ==================== TAB 1: 60s TOPIC REFLEX ==================== */}
          {tab === 'reflex' && (
            <div className="space-y-4">
              {qIdx >= deck.length && deck.length > 0 ? (
                <div className="bg-white rounded-2xl border border-slate-200 p-8 text-center space-y-4 shadow-xs">
                  <div className="text-5xl">🏆</div>
                  <h3 className="text-2xl font-black text-slate-900">
                    Hoàn thành Vòng Phản Xạ 10 Đề IELTS Task 2!
                  </h3>
                  <p className="text-slate-600 text-base">
                    Tổng điểm phản xạ của em:{' '}
                    <span className="font-black text-indigo-700 text-xl">{score} / 30 điểm</span>
                  </p>
                  <div className="flex justify-center gap-3 pt-2">
                    <button
                      onClick={startNewReflexRound}
                      className="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold text-sm cursor-pointer"
                    >
                      🔄 Chơi vòng 10 đề ngẫu nhiên mới
                    </button>
                    <button
                      onClick={() => setTab('anchors')}
                      className="px-5 py-2.5 rounded-xl border border-indigo-300 bg-indigo-50 text-indigo-800 font-bold text-sm cursor-pointer"
                    >
                      🧠 Ôn thẻ 4 Mỏ neo 19 Pillars
                    </button>
                  </div>
                </div>
              ) : currentQ ? (
                <>
                  {/* Status Bar */}
                  <div className="flex flex-wrap items-center justify-between gap-2 bg-white border border-slate-200 rounded-xl px-4 py-2.5">
                    <div className="flex items-center gap-3 text-xs sm:text-sm font-bold text-slate-700">
                      <span>
                        Đề <span className="text-indigo-700">{qIdx + 1}</span> / {deck.length}
                      </span>
                      <span>•</span>
                      <span>
                        Điểm: <span className="text-emerald-700">{score}</span>
                      </span>
                      <span>•</span>
                      <span>🔥 Chuỗi đúng: {streak}</span>
                    </div>

                    <div className="flex items-center gap-2">
                      <button
                        onClick={() => setTimerEnabled((v) => !v)}
                        className="text-xs font-bold text-slate-500 hover:text-slate-800 cursor-pointer"
                      >
                        {timerEnabled ? '⏱️ Tắt đếm giờ' : '⏱️ Bật đếm 60s'}
                      </button>
                      {timerEnabled && (
                        <span
                          className={`px-3 py-1 rounded-full text-xs font-black ${
                            secondsLeft <= 15
                              ? 'bg-rose-100 text-rose-700 animate-pulse'
                              : 'bg-indigo-100 text-indigo-800'
                          }`}
                        >
                          ⏳ {secondsLeft}s
                        </span>
                      )}
                    </div>
                  </div>

                  {/* Prompt Card */}
                  <div className="bg-gradient-to-br from-amber-50 to-orange-50 border-l-4 border-amber-500 rounded-xl p-4 sm:p-5 shadow-2xs">
                    <div className="text-[11px] font-extrabold uppercase text-amber-800 mb-1">
                      Đọc lướt đề bài và bắt từ khóa câu hỏi cuối đề:
                    </div>
                    <p className="text-slate-900 font-bold text-base sm:text-[17px] leading-relaxed">
                      {currentQ.prompt}
                    </p>
                  </div>

                  {/* Question A: Pick Category */}
                  <div className="bg-white rounded-xl border border-slate-200 p-4 space-y-2.5">
                    <div className="text-xs font-extrabold uppercase text-indigo-700">
                      Bước 1 • Đề này dùng Khung Bất Biến của dạng nào? (Chọn 1)
                    </div>
                    <div className="grid grid-cols-2 sm:grid-cols-5 gap-2">
                      {CATEGORY_OPTIONS.map((c) => {
                        const isPicked = pickedCat === c.id;
                        const isAnswer = currentQ.correctCategory === c.id;
                        let style = 'border-slate-200 bg-slate-50 hover:bg-slate-100 text-slate-800';
                        if (checked) {
                          if (isAnswer) style = 'border-emerald-500 bg-emerald-50 text-emerald-900 ring-2 ring-emerald-400';
                          else if (isPicked) style = 'border-rose-400 bg-rose-50 text-rose-800';
                        } else if (isPicked) {
                          style = 'border-indigo-600 bg-indigo-50 text-indigo-900 ring-2 ring-indigo-500';
                        }
                        return (
                          <button
                            key={c.id}
                            disabled={checked}
                            onClick={() => setPickedCat(c.id)}
                            className={`p-2.5 rounded-xl border text-left transition-all cursor-pointer ${style}`}
                          >
                            <div className="font-extrabold text-xs sm:text-sm">{c.label}</div>
                            <div className="text-[11px] opacity-80 truncate">{c.shortDesc}</div>
                          </button>
                        );
                      })}
                    </div>
                  </div>

                  {/* Question B: Pick 2 Pillars (3 Color-Coded Priority Tabs) */}
                  <div className="bg-white rounded-xl border border-slate-200 p-4 space-y-2.5">
                    <div className="flex items-center justify-between flex-wrap gap-2">
                      <span className="text-xs font-extrabold uppercase text-violet-700">
                        Bước 2 • Nhặt nhanh 2 Trụ Ý theo thứ tự ưu tiên ({pickedPillars.length}/2 đã chọn)
                      </span>
                      <span className="text-[11px] font-semibold text-slate-500">
                        🟢 Xanh Lá trước → 🔵 Xanh Da Trời → 🟣 Tím (Dự phòng)
                      </span>
                    </div>

                    {/* 3 Color-Coded Inner Priority Tabs */}
                    <div className="grid grid-cols-1 sm:grid-cols-3 gap-1.5">
                      {([1, 2, 3] as const).map((tier) => {
                        const meta = PILLAR_TIER_META[tier];
                        const isActive = reflexTierTab === tier;
                        const pickedInTier = pickedPillars.filter(
                          (id) => (WT2_PILLARS.find((p) => p.id === id)?.tier ?? 1) === tier
                        ).length;
                        const hasPrimaryInTier =
                          checked &&
                          currentQ.primaryPair.some(
                            (id) => (WT2_PILLARS.find((p) => p.id === id)?.tier ?? 1) === tier
                          );

                        return (
                          <button
                            key={tier}
                            type="button"
                            onClick={() => setReflexTierTab(tier)}
                            className={`rounded-lg border px-2.5 py-1.5 text-left transition-all cursor-pointer flex items-center justify-between gap-1.5 ${
                              isActive ? meta.activeTabCls : meta.inactiveTabCls
                            }`}
                          >
                            <div className="min-w-0">
                              <div className="text-xs font-extrabold truncate">{meta.tabTitle}</div>
                              <div
                                className={`text-[10px] truncate ${
                                  isActive ? 'text-white/90' : 'opacity-85'
                                }`}
                              >
                                {meta.tabSub}
                              </div>
                            </div>
                            <div className="flex items-center gap-1 shrink-0">
                              {pickedInTier > 0 && (
                                <span
                                  className={`px-1.5 py-0.5 rounded text-[10px] font-extrabold ${
                                    isActive
                                      ? 'bg-white/25 text-white border border-white/40'
                                      : 'bg-white text-slate-800 border border-black/10'
                                  }`}
                                >
                                  Đã chọn {pickedInTier}
                                </span>
                              )}
                              {hasPrimaryInTier && (
                                <span className="px-1.5 py-0.5 rounded text-[10px] font-extrabold bg-amber-300 text-amber-950">
                                  ⭐ Đáp án
                                </span>
                              )}
                            </div>
                          </button>
                        );
                      })}
                    </div>

                    <div
                      className={`rounded-xl border overflow-hidden ${
                        PILLAR_TIER_META[reflexTierTab].panelBorderCls
                      }`}
                    >
                      <div
                        className={`px-3 py-1.5 flex flex-wrap items-center justify-between gap-1.5 ${
                          PILLAR_TIER_META[reflexTierTab].headerCls
                        }`}
                      >
                        <span className="text-[11px] font-extrabold uppercase">
                          {PILLAR_TIER_META[reflexTierTab].headerTitle}
                        </span>
                        <span className="text-[10.5px] text-white/95 font-medium">
                          {PILLAR_TIER_META[reflexTierTab].priorityHint}
                        </span>
                      </div>
                      <div className="p-2.5 grid grid-cols-2 sm:grid-cols-3 gap-2">
                        {WT2_PILLARS.filter((p) => p.tier === reflexTierTab).map((p) => {
                          const isPicked = pickedPillars.includes(p.id);
                          const isBest = currentQ.bestPillars.includes(p.id);
                          const isPrimary = currentQ.primaryPair.includes(p.id);
                          const tierMeta = PILLAR_TIER_META[p.tier];
                          let cls = `bg-white text-slate-800 ${tierMeta.cardBorderCls}`;
                          if (checked) {
                            if (isPrimary)
                              cls =
                                'border-2 border-emerald-600 bg-emerald-50 text-emerald-950 ring-2 ring-emerald-400';
                            else if (isBest)
                              cls = 'border-2 border-teal-400 bg-teal-50/70 text-teal-900';
                            else if (isPicked)
                              cls = 'border-2 border-rose-400 bg-rose-50 text-rose-800';
                          } else if (isPicked) {
                            cls =
                              'border-2 border-violet-600 bg-violet-50 text-violet-950 ring-2 ring-violet-500';
                          }

                          return (
                            <button
                              key={p.id}
                              disabled={checked}
                              onClick={() => togglePickPillar(p.id)}
                              className={`p-2 rounded-lg border text-left text-xs transition-all cursor-pointer ${cls}`}
                            >
                              <div
                                className={`font-extrabold truncate ${
                                  !checked && !isPicked ? tierMeta.nameTextCls : ''
                                }`}
                              >
                                {p.icon} {p.id}. {p.name}
                              </div>
                              <div className="text-[11px] text-slate-500 truncate">{p.viName}</div>
                            </button>
                          );
                        })}
                      </div>
                    </div>
                  </div>

                  {/* Explanation Box after Check */}
                  {checked && (
                    <div className="bg-emerald-50 border border-emerald-300 rounded-xl p-4 space-y-2">
                      <div className="flex flex-wrap items-center justify-between gap-2">
                        <div className="font-extrabold text-emerald-950 text-sm">
                          🎯 Đáp án chuẩn: {currentQ.subTypeLabel} • Cặp Trụ ý vàng:{' '}
                          {currentQ.primaryPair
                            .map((id) => {
                              const p = WT2_PILLARS.find((x) => x.id === id);
                              return p ? `${p.code} ${p.name}` : `#${id}`;
                            })
                            .join(' + ')}
                        </div>
                        {onLaunchStudioFromReflex && (
                          <div className="flex flex-wrap items-center gap-1.5">
                            <button
                              onClick={() => {
                                onClose();
                                onLaunchStudioFromReflex({
                                  topic: currentQ.prompt,
                                  label: 'Từ Mini-Game Phản Xạ',
                                  category: currentQ.correctCategory,
                                  presetPillar1: currentQ.primaryPair[0],
                                  presetPillar2: currentQ.primaryPair[1],
                                  bodyMode: 'single'
                                });
                              }}
                              className="px-3 py-1.5 rounded-lg bg-[#0a5482] hover:bg-[#084268] text-white text-xs font-extrabold cursor-pointer"
                            >
                              🎯 Ghép Phiên bản 1 (1 ý sâu)
                            </button>
                            <button
                              onClick={() => {
                                onClose();
                                onLaunchStudioFromReflex({
                                  topic: currentQ.prompt,
                                  label: 'Từ Mini-Game Phản Xạ • Đa ý',
                                  category: currentQ.correctCategory,
                                  presetPillar1: currentQ.primaryPair[0],
                                  presetPillar2: currentQ.primaryPair[1],
                                  bodyMode: 'multi'
                                });
                              }}
                              className="px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-extrabold cursor-pointer"
                            >
                              🔗 Ghép Phiên bản 2 (Đa ý + Linking)
                            </button>
                          </div>
                        )}
                      </div>
                      <div className="text-xs text-emerald-900">
                        <strong>Từ khóa nhận diện:</strong> {currentQ.triggerWords}
                      </div>
                      <p className="text-xs sm:text-sm text-slate-800 leading-relaxed">
                        {currentQ.explanation}
                      </p>
                    </div>
                  )}

                  {/* Footer CTA for Reflex Question */}
                  <div className="flex justify-end gap-3">
                    {!checked ? (
                      <button
                        disabled={!pickedCat || pickedPillars.length < 2}
                        onClick={handleCheckReflex}
                        className={`px-6 py-2.5 rounded-xl font-extrabold text-sm transition-all ${
                          pickedCat && pickedPillars.length === 2
                            ? 'bg-indigo-600 hover:bg-indigo-700 text-white cursor-pointer shadow-sm'
                            : 'bg-slate-200 text-slate-400 cursor-not-allowed'
                        }`}
                      >
                        ⚡ Chốt Đáp Án Phản Xạ!
                      </button>
                    ) : (
                      <button
                        onClick={handleNextQuestion}
                        className="px-6 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm cursor-pointer shadow-sm"
                      >
                        Đề tiếp theo →
                      </button>
                    )}
                  </div>
                </>
              ) : null}
            </div>
          )}

          {/* ==================== TAB 2: 4-ANCHOR MEMORY DRILL ==================== */}
          {tab === 'anchors' && (() => {
            const coreMemorizedCount = memorizedIds.filter((id) => {
              const p = WT2_PILLARS.find((x) => x.id === id);
              return p && p.tier <= 2;
            }).length;

            return (
              <div className="space-y-4">
                {/* Priority Memorization Strategy Banner */}
                <div className="bg-gradient-to-r from-[#eaf8ee] via-[#e8f3ff] to-[#f3effb] border border-slate-200 rounded-xl px-4 py-2.5 flex flex-wrap items-center justify-between gap-2 text-xs">
                  <div className="text-slate-800 leading-relaxed">
                    <strong className="text-[#19692c]">🎯 Thứ tự ưu tiên học thuộc:</strong> Học sinh chủ yếu chỉ cần thuộc nằm lòng{' '}
                    <strong className="text-[#19692c]">Bảng Xanh Lá (9 ý dễ dùng nhất)</strong> +{' '}
                    <strong className="text-[#0056b3]">Bảng Xanh Da Trời (4 ý bổ sung)</strong> ={' '}
                    <strong>13 Trụ ý cốt lõi</strong>. Khi đi thi, dò Bảng Xanh Lá trước → chưa khớp mới sang Xanh Da Trời → bất đắc dĩ mới dùng{' '}
                    <strong className="text-[#533094]">Bảng Tím (6 ý dự phòng)</strong>.
                  </div>
                  <span className="px-2.5 py-1 rounded-full bg-white border border-emerald-300 text-emerald-800 font-extrabold shrink-0">
                    ✓ Đã thuộc cốt lõi: {coreMemorizedCount}/13 ý
                  </span>
                </div>

                <div className="flex flex-wrap items-center justify-between gap-2 bg-white border border-slate-200 rounded-xl p-3">
                  <div className="inline-flex rounded-lg bg-slate-100 p-1 text-xs font-bold">
                    <button
                      onClick={() => setAnchorMode('cards')}
                      className={`px-3 py-1.5 rounded-md cursor-pointer ${
                        anchorMode === 'cards'
                          ? 'bg-white text-indigo-900 shadow-2xs'
                          : 'text-slate-600'
                      }`}
                    >
                      🃏 Thẻ 4 Từ Khóa Mỏ Neo
                    </button>
                    <button
                      onClick={() => setAnchorMode('quiz')}
                      className={`px-3 py-1.5 rounded-md cursor-pointer ${
                        anchorMode === 'quiz'
                          ? 'bg-white text-indigo-900 shadow-2xs'
                          : 'text-slate-600'
                      }`}
                    >
                      🎯 Quiz Bắn Tốc Độ Nhớ Số Liệu &amp; Cụm Vàng
                    </button>
                  </div>

                  {anchorMode === 'cards' ? (
                    <div className="flex flex-wrap items-center gap-1.5 text-xs font-bold">
                      {([1, 2, 3] as const).map((t) => {
                        const meta = PILLAR_TIER_META[t];
                        const isActive = tierFilter === t;
                        const lbl =
                          t === 1
                            ? '🟢 Ưu tiên 1: Xanh Lá (9)'
                            : t === 2
                            ? '🔵 Ưu tiên 2: Xanh Da Trời (4)'
                            : '🟣 Ưu tiên 3: Tím • Dự phòng (6)';
                        return (
                          <button
                            key={t}
                            onClick={() => setTierFilter(t)}
                            className={`px-2.5 py-1 rounded-lg border cursor-pointer transition-all ${
                              isActive ? meta.activeTabCls : meta.inactiveTabCls
                            }`}
                          >
                            {lbl}
                          </button>
                        );
                      })}
                      <button
                        onClick={() => setTierFilter(0)}
                        className={`px-2.5 py-1 rounded-lg border cursor-pointer transition-all ${
                          tierFilter === 0
                            ? 'bg-slate-800 text-white border-slate-800'
                            : 'bg-slate-100 text-slate-600 border-slate-200 hover:bg-slate-200'
                        }`}
                      >
                        Tất cả (19)
                      </button>
                    </div>
                  ) : (
                    <div className="inline-flex rounded-lg border border-slate-200 bg-slate-50 p-0.5 text-xs font-bold">
                      <button
                        type="button"
                        onClick={() => {
                          setQuizCoreOnly(true);
                          generateNextAnchorQuiz(true);
                        }}
                        className={`px-2.5 py-1 rounded-md cursor-pointer ${
                          quizCoreOnly
                            ? 'bg-[#28a745] text-white shadow-2xs'
                            : 'text-slate-600 hover:bg-slate-100'
                        }`}
                      >
                        🟢🔵 13 Trụ ý cốt lõi (Cần thuộc)
                      </button>
                      <button
                        type="button"
                        onClick={() => {
                          setQuizCoreOnly(false);
                          generateNextAnchorQuiz(false);
                        }}
                        className={`px-2.5 py-1 rounded-md cursor-pointer ${
                          !quizCoreOnly
                            ? 'bg-[#6f42c1] text-white shadow-2xs'
                            : 'text-slate-600 hover:bg-slate-100'
                        }`}
                      >
                        Tất cả 19 Trụ ý
                      </button>
                    </div>
                  )}
                </div>

                {anchorMode === 'cards' ? (
                  <div className="space-y-2.5">
                    {tierFilter !== 0 && (
                      <div
                        className={`rounded-xl px-3.5 py-2 flex flex-wrap items-center justify-between gap-2 ${
                          PILLAR_TIER_META[tierFilter].headerCls
                        }`}
                      >
                        <span className="text-xs font-extrabold uppercase">
                          {PILLAR_TIER_META[tierFilter].headerTitle}
                        </span>
                        <span className="text-xs text-white/95 font-medium">
                          {PILLAR_TIER_META[tierFilter].priorityHint}
                        </span>
                      </div>
                    )}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      {WT2_PILLARS.filter((p) => tierFilter === 0 || p.tier === tierFilter).map(
                        (p) => {
                          const isFlipped = !!flippedIds[p.id];
                          const isDone = memorizedIds.includes(p.id);
                          const pMeta = PILLAR_TIER_META[p.tier];

                          return (
                            <div
                              key={p.id}
                              className={`rounded-xl border p-4 bg-white shadow-2xs flex flex-col justify-between gap-3 transition-all ${
                                isDone
                                  ? 'border-2 border-emerald-400 bg-emerald-50/25'
                                  : pMeta.cardBorderCls
                              }`}
                            >
                              <div className="flex items-start justify-between gap-2">
                                <div>
                                  <div className="flex items-center gap-1.5 flex-wrap mb-0.5">
                                    <span
                                      className={`font-black text-sm sm:text-base ${pMeta.nameTextCls}`}
                                    >
                                      {p.icon} {p.id}. {p.name}
                                    </span>
                                    <span
                                      className={`text-[10px] font-extrabold px-1.5 py-0.5 rounded border ${pMeta.pillBadgeCls}`}
                                    >
                                      {pMeta.shortBadge}
                                    </span>
                                  </div>
                                  <div className="text-xs text-slate-500">{p.viName}</div>
                                </div>
                                <button
                                  onClick={() => toggleMemorized(p.id)}
                                  className={`px-2.5 py-1 rounded-full text-xs font-bold cursor-pointer border shrink-0 ${
                                    isDone
                                      ? 'bg-emerald-600 text-white border-emerald-600'
                                      : 'bg-slate-50 text-slate-600 border-slate-300 hover:bg-slate-100'
                                  }`}
                                >
                                  {isDone ? '✓ Đã thuộc lòng' : 'Đánh dấu đã thuộc'}
                                </button>
                              </div>

                              {!isFlipped ? (
                                <div className="bg-indigo-50/60 border border-indigo-200 rounded-lg p-3 space-y-1.5 text-xs">
                                  <div className="font-extrabold text-indigo-900 uppercase text-[11px]">
                                    🔑 4 Từ Khóa Neo Trí Nhớ (Nhẩm thành câu trước khi lật):
                                  </div>
                                  <div>
                                    <strong>1. Tên Trụ ý:</strong> {p.positive.anchors[0]} /{' '}
                                    {p.negative.anchors[0]}
                                  </div>
                                  <div>
                                    <strong>2. Cause:</strong> {p.positive.anchors[1]}
                                  </div>
                                  <div>
                                    <strong>3. Effect:</strong> {p.positive.anchors[2]}
                                  </div>
                                  <div>
                                    <strong>4. Example:</strong> {p.positive.anchors[3]}
                                  </div>
                                </div>
                              ) : (
                                <div className="bg-slate-50 border border-slate-200 rounded-lg p-3 space-y-2 text-xs leading-relaxed">
                                  <div>
                                    <span className="font-extrabold text-emerald-700">
                                      (+) Nhánh Tích cực (4 câu PEEL):
                                    </span>{' '}
                                    {p.positive.pillarSlot} → {p.positive.causeSlot} →{' '}
                                    {p.positive.effectSlot} → <em>{p.positive.exampleSlot}</em>
                                  </div>
                                  <div className="border-t border-slate-200 pt-2">
                                    <span className="font-extrabold text-rose-700">
                                      (-) Nhánh Tiêu cực (4 câu PEEL):
                                    </span>{' '}
                                    {p.negative.pillarSlot} → {p.negative.causeSlot} →{' '}
                                    {p.negative.effectSlot} → <em>{p.negative.exampleSlot}</em>
                                  </div>
                                  <div className="border-t border-indigo-200 pt-2 bg-indigo-50/60 -mx-3 -mb-3 p-2.5 rounded-b-lg space-y-1">
                                    <div className="font-extrabold text-indigo-800 text-[11px] uppercase">
                                      🔗 Rút gọn 1–2 câu cho Phiên bản 2 (Đa Trụ ý + Linking Words):
                                    </div>
                                    <div>
                                      <strong className="text-emerald-700">(+):</strong>{' '}
                                      {p.positive.compactOneSentenceSlot}.
                                    </div>
                                    <div>
                                      <strong className="text-rose-700">(-):</strong>{' '}
                                      {p.negative.compactOneSentenceSlot}.
                                    </div>
                                  </div>
                                </div>
                              )}

                              <button
                                onClick={() =>
                                  setFlippedIds((prev) => ({ ...prev, [p.id]: !prev[p.id] }))
                                }
                                className="w-full py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold cursor-pointer"
                              >
                                {isFlipped
                                  ? '🙈 Ẩn câu đầy đủ (Quay về 4 Từ khóa mỏ neo)'
                                  : '👀 Lật xem câu đầy đủ (+/-) trong bảng Pillars'}
                              </button>
                            </div>
                          );
                        }
                      )}
                    </div>
                  </div>
                ) : (
                  anchorQuizItem && (
                    <div className="bg-white rounded-2xl border border-slate-200 p-6 max-w-2xl mx-auto space-y-5 shadow-xs">
                      <div className="flex items-center justify-between text-xs font-bold text-slate-600">
                        <span>🎯 Nhìn cụm mỏ neo → Bấm chọn đúng Trụ ý trong 3 giây!</span>
                        <span className="text-indigo-700 font-extrabold">
                          🔥 Chuỗi đúng liên tiếp: {anchorQuizStreak}
                        </span>
                      </div>

                      <div className="bg-purple-50 border-l-4 border-purple-600 rounded-xl p-5 space-y-1.5">
                        <div className="text-[11px] font-extrabold uppercase text-purple-700">
                          {anchorQuizItem.clueType}
                        </div>
                        <div className="text-lg font-black text-slate-900">
                          “{anchorQuizItem.clueText}”
                        </div>
                      </div>

                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        {anchorQuizItem.options.map((opt) => {
                          const isPicked = anchorQuizPicked === opt.id;
                          const isRight = opt.id === anchorQuizItem.correctId;
                          const optMeta = PILLAR_TIER_META[opt.tier];
                          let cls = `bg-white text-slate-800 ${optMeta.cardBorderCls}`;
                          if (anchorQuizPicked !== null) {
                            if (isRight)
                              cls =
                                'border-2 border-emerald-500 bg-emerald-50 text-emerald-950 ring-2 ring-emerald-400';
                            else if (isPicked)
                              cls = 'border-2 border-rose-400 bg-rose-50 text-rose-800';
                          }
                          return (
                            <button
                              key={opt.id}
                              disabled={anchorQuizPicked !== null}
                              onClick={() => {
                                setAnchorQuizPicked(opt.id);
                                if (opt.id === anchorQuizItem.correctId) {
                                  setAnchorQuizStreak((s) => s + 1);
                                } else {
                                  setAnchorQuizStreak(0);
                                }
                              }}
                              className={`p-3.5 rounded-xl border text-left transition-all cursor-pointer ${cls}`}
                            >
                              <div className={`font-extrabold text-sm ${optMeta.nameTextCls}`}>
                                {opt.icon} {opt.id}. {opt.name}
                              </div>
                              <div className="text-xs text-slate-500">{opt.viName}</div>
                            </button>
                          );
                        })}
                      </div>

                      {anchorQuizPicked !== null && (
                        <div className="flex justify-end">
                          <button
                            onClick={() => generateNextAnchorQuiz()}
                            className="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold text-sm cursor-pointer"
                          >
                            Câu tiếp theo →
                          </button>
                        </div>
                      )}
                    </div>
                  )
                )}
              </div>
            );
          })()}
        </div>
      </div>
    </div>
  );
};
