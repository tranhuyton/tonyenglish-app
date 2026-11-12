import React, { useState, useEffect, useMemo, useRef } from 'react';
import { supabase } from './supabase';
import {
  WT2_PILLARS,
  WT2_STRUCTURES,
  WT2_SUBJECT_GROUPS,
  WT2_REFLEX_QUESTIONS,
  Wt2Category,
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
}

interface Wt2PillarStudioModalProps {
  isOpen: boolean;
  onClose: () => void;
  payload: Wt2StudioOpenPayload | null;
  courseId?: string | null;
  onMarkTaskComplete?: (taskId: string) => void;
}

const CATEGORY_OPTIONS: { id: Wt2Category; label: string; shortDesc: string }[] = [
  { id: 'discussion', label: '1. Discussion', shortDesc: 'Discuss both views & opinion' },
  { id: 'argument', label: '2. Argument', shortDesc: 'Advantages & Disadvantages / Outweigh' },
  { id: 'opinion', label: '3. Opinion', shortDesc: 'Agree or Disagree (V1 / V2)' },
  { id: 'mixed', label: '4. Mixed', shortDesc: 'Problems-Solutions / Causes-Effects' },
  { id: 'twopart', label: '5. Two-part', shortDesc: '2 câu hỏi trực tiếp' }
];

const COL_LABELS: Record<PillarSlotType, { badge: string; vi: string; color: string }> = {
  pillar: { badge: 'Tên Trụ Ý', vi: 'Advantage / Disadvantage', color: 'bg-indigo-100 text-indigo-800 border-indigo-300' },
  cause: { badge: 'Cause', vi: 'Nguyên nhân / Giải thích', color: 'bg-sky-100 text-sky-800 border-sky-300' },
  effect: { badge: 'Effect', vi: 'Kết quả / Hệ quả', color: 'bg-amber-100 text-amber-800 border-amber-300' },
  example: { badge: 'Example', vi: 'Ví dụ & Số liệu khảo sát', color: 'bg-emerald-100 text-emerald-800 border-emerald-300' }
};

// Shuffled display order so students actively distinguish Cause / Example / Pillar / Effect
const SHUFFLED_COLS: PillarSlotType[] = ['cause', 'example', 'pillar', 'effect'];

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

export const Wt2PillarStudioModal: React.FC<Wt2PillarStudioModalProps> = ({
  isOpen,
  onClose,
  payload,
  courseId,
  onMarkTaskComplete
}) => {
  const [step, setStep] = useState<1 | 2 | 3>(1);
  const [difficulty, setDifficulty] = useState<'level1' | 'level2'>('level1');
  const [showPillarTableDrawer, setShowPillarTableDrawer] = useState(false);

  // Category & Template configuration
  const isAutoCategory = !payload?.category || payload.category === 'auto';
  const [selectedCategory, setSelectedCategory] = useState<Wt2Category>('discussion');
  const [templateId, setTemplateId] = useState<Wt2TemplateId>('discussion');
  const [stance, setStance] = useState<'agree' | 'disagree'>('disagree');

  // Chosen Pillars for Body 1 & Body 2
  const [pillar1Id, setPillar1Id] = useState<number>(1);
  const [pillar1Polarity, setPillar1Polarity] = useState<'positive' | 'negative'>('positive');
  const [pillar2Id, setPillar2Id] = useState<number>(2);
  const [pillar2Polarity, setPillar2Polarity] = useState<'positive' | 'negative'>('negative');

  // Interactive Slot State: key = `${bodyIndex}_${pillarCol}` -> boolean (slotted)
  const [slottedPillarKeys, setSlottedPillarKeys] = useState<Record<string, boolean>>({});
  // Level 2 Memory Mode custom typed text for pillar slots
  const [memoryPillarTexts, setMemoryPillarTexts] = useState<Record<string, string>>({});
  // Topic-specific short inputs: key = slotKey
  const [topicInputs, setTopicInputs] = useState<Record<string, string>>({});

  // Tap-to-place active card (works seamlessly on mobile/iPad & desktop alongside HTML5 drag-drop)
  const [selectedCard, setSelectedCard] = useState<{ bodyIndex: 1 | 2; col: PillarSlotType } | null>(null);
  const [slotFeedback, setSlotFeedback] = useState<{ type: 'error' | 'ok'; msg: string } | null>(null);

  // Step 2: Editable essay & checklist
  const [essayDraft, setEssayDraft] = useState<string>('');
  const [activeSubjectGroup, setActiveSubjectGroup] = useState<string>('age');
  const [checklist, setChecklist] = useState<[boolean, boolean, boolean, boolean]>([false, false, false, false]);
  const textareaRef = useRef<HTMLTextAreaElement | null>(null);

  // Step 3: AI Grading Result
  const [isGrading, setIsGrading] = useState(false);
  const [gradeError, setGradeError] = useState<string | null>(null);
  const [aiEvaluation, setAiEvaluation] = useState<any | null>(null);
  const [taskMarkedDone, setTaskMarkedDone] = useState(false);

  // Reset state when modal opens with a new payload
  useEffect(() => {
    if (!isOpen || !payload) return;
    const initCat: Wt2Category =
      payload.category && payload.category !== 'auto' ? payload.category : 'discussion';
    const initTpl = defaultTemplateForCategory(initCat, payload.subType);

    setStep(1);
    setSelectedCategory(initCat);
    setTemplateId(initTpl);
    setStance('disagree');

    const p1 = payload.presetPillar1 || (initCat === 'mixed' ? 12 : 1);
    const p2 = payload.presetPillar2 || (initCat === 'mixed' ? 16 : 2);
    setPillar1Id(p1);
    setPillar2Id(p2);

    if (initCat === 'argument') {
      setPillar1Polarity('positive');
      setPillar2Polarity('negative');
    } else if (initCat === 'mixed') {
      setPillar1Polarity('negative');
      setPillar2Polarity(initTpl === 'mixed_ps' ? 'positive' : 'negative');
    } else {
      setPillar1Polarity('positive');
      setPillar2Polarity('positive');
    }

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
    setTaskMarkedDone(false);
  }, [isOpen, payload]);

  const handleCategoryChange = (cat: Wt2Category) => {
    setSelectedCategory(cat);
    const nextTpl = defaultTemplateForCategory(cat);
    setTemplateId(nextTpl);
    setSlottedPillarKeys({});
    if (cat === 'argument') {
      setPillar1Polarity('positive');
      setPillar2Polarity('negative');
    } else if (cat === 'mixed') {
      setPillar1Polarity('negative');
      setPillar2Polarity(nextTpl === 'mixed_ps' ? 'positive' : 'negative');
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

  const structureDef = WT2_STRUCTURES[templateId];
  const paragraphs = useMemo(() => structureDef.buildParagraphs(stance), [structureDef, stance]);

  const getBranchValue = (bodyIndex: 1 | 2, col: PillarSlotType): string => {
    const b = bodyIndex === 1 ? branch1 : branch2;
    switch (col) {
      case 'pillar':
        return b.pillarSlot;
      case 'cause':
        return b.causeSlot;
      case 'effect':
        return b.effectSlot;
      case 'example':
        return b.exampleSlot;
    }
  };

  const getBranchAnchor = (bodyIndex: 1 | 2, col: PillarSlotType): string => {
    const b = bodyIndex === 1 ? branch1 : branch2;
    const idx = col === 'pillar' ? 0 : col === 'cause' ? 1 : col === 'effect' ? 2 : 3;
    return b.anchors[idx];
  };

  // Required unique pillar slots in current template
  const requiredPillarUnitKeys = useMemo(() => {
    const s = new Set<string>();
    paragraphs.forEach((p) =>
      p.tokens.forEach((t) => {
        if (t.type === 'pillar_slot' && t.bodyIndex && t.pillarCol) {
          s.add(`${t.bodyIndex}_${t.pillarCol}`);
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
    targetCol: PillarSlotType
  ) => {
    if (sourceBody !== targetBody) {
      setSlotFeedback({
        type: 'error',
        msg: `Thẻ này thuộc Trụ ý của Body ${sourceBody} — em hãy thả vào đoạn Body ${sourceBody} nhé!`
      });
      return;
    }
    if (sourceCol !== targetCol) {
      setSlotFeedback({
        type: 'error',
        msg: `Chưa khớp cột! Thẻ em chọn là [${COL_LABELS[sourceCol].badge}] (${COL_LABELS[sourceCol].vi}), còn ô này cần [${COL_LABELS[targetCol].badge}].`
      });
      return;
    }
    const unitKey = `${targetBody}_${targetCol}`;
    setSlottedPillarKeys((prev) => ({ ...prev, [unitKey]: true }));
    setSelectedCard(null);
    setSlotFeedback({
      type: 'ok',
      msg: `Chuẩn xác! Đã lắp thẻ [${COL_LABELS[targetCol].badge}] vào Body ${targetBody}.`
    });
  };

  const handleAutoFillAllPillarSlots = () => {
    const next: Record<string, boolean> = {};
    requiredPillarUnitKeys.forEach((k) => {
      next[k] = true;
    });
    setSlottedPillarKeys(next);
    setSlotFeedback({
      type: 'ok',
      msg: 'Đã lắp toàn bộ các thẻ Pillar vào đúng vị trí trong Khung bất biến!'
    });
  };

  // Assemble Step 1 into Step 2 editable draft
  const buildAssembledEssay = (): string => {
    return paragraphs
      .map((para) => {
        const raw = para.tokens
          .map((tok) => {
            if (tok.type === 'text') return tok.text || '';
            if (tok.type === 'topic_input' && tok.slotKey) {
              const val = (topicInputs[tok.slotKey] || '').trim();
              return val || `[${tok.placeholder || 'nội dung theo đề'}]`;
            }
            if (tok.type === 'pillar_slot' && tok.bodyIndex && tok.pillarCol) {
              const unitKey = `${tok.bodyIndex}_${tok.pillarCol}`;
              if (difficulty === 'level2') {
                const typed = (memoryPillarTexts[unitKey] || '').trim();
                return typed || `[Viết từ mỏ neo: ${getBranchAnchor(tok.bodyIndex, tok.pillarCol)}]`;
              }
              if (slottedPillarKeys[unitKey]) {
                return getBranchValue(tok.bodyIndex, tok.pillarCol);
              }
              return `[${tok.placeholder || COL_LABELS[tok.pillarCol].badge}]`;
            }
            return '';
          })
          .join('');
        return raw.replace(/\s+\./g, '.').replace(/\s+,/g, ',').replace(/\s{2,}/g, ' ').trim();
      })
      .join('\n\n');
  };

  const handleProceedToStep2 = () => {
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

    try {
      const prompt = `
Bạn là Giám khảo IELTS Writing chấm bài kiêm Thầy giáo hướng dẫn phương pháp "Khung Cấu Trúc Bất Biến + Bảng 19 Idea Pillars" của hệ thống TonyEnglish.
QUY TẮC XƯNG HÔ BẮT BUỘC: Xưng "Thầy" và gọi học viên là "em" (TUYỆT ĐỐI KHÔNG xưng "tôi/bạn" hay "con"). Nhận xét ân cần, khích lệ, chỉ rõ điểm làm tốt và cách sửa mượt hơn.

1. ĐỀ BÀI IELTS WRITING TASK 2:
"""
${payload?.topic || ''}
"""

2. CÔNG THỨC TONYENGLISH HỌC VIÊN ĐANG LUYỆN:
- Khung bất biến áp dụng: ${structureDef.name} (${structureDef.viSubtitle})
- Trụ ý Body 1 đã chọn: ${pillar1.code} ${pillar1.name} (${branch1.label})
- Trụ ý Body 2 đã chọn: ${pillar2.code} ${pillar2.name} (${branch2.label})

3. BÀI LÀM SAU KHI GHÉP & TỰ BIÊN TẬP CỦA HỌC VIÊN (${wordCount} từ):
"""
${essayDraft}
"""

Hãy chấm kép bài làm trên (vừa theo 4 tiêu chí IELTS chuẩn, vừa theo độ nhuần nhuyễn khi lắp Khung bất biến + Trụ ý Pillars) và trả về ĐÚNG ĐỊNH DẠNG JSON THUẦN TÚY SAU (KHÔNG bọc markdown \`\`\`json):
{
  "overall": 7.0,
  "formulaScore": 8.5,
  "formulaReview": {
    "structureCheck": "Nhận xét xem em đã giữ đúng Khung bất biến của dạng ${structureDef.name} chưa...",
    "pillarFitCheck": "Nhận xét xem 2 Trụ ý (${pillar1.name} & ${pillar2.name}) em chọn và ví dụ đưa vào đã bám sát đề bài chưa...",
    "seamGrammarCheck": "Nhận xét các mối nối ngữ pháp (sau due to / related to / chủ ngữ S / từ nối) đã mượt tự nhiên chưa và chỉ cách gọt..."
  },
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

      // Save practice record to test_results
      const {
        data: { user }
      } = await supabase.auth.getUser();
      if (user) {
        await supabase.from('test_results').insert([
          {
            user_id: user.id,
            course_id: courseId || null,
            test_title: `[WT2 Pillars] ${payload?.label || structureDef.name}`,
            test_type: 'IELTS-Writing',
            score: parsed.overall || 0,
            total_score: 9,
            time_spent: 0,
            details: {
              mode: 'wt2_pillar_studio',
              topic: payload?.topic,
              templateId,
              pillar1: `${pillar1.code} ${pillar1.name} (${pillar1Polarity})`,
              pillar2: `${pillar2.code} ${pillar2.name} (${pillar2Polarity})`,
              essay: essayDraft,
              wordCount,
              aiFeedback: parsed
            }
          }
        ]);
      }

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
                    if (!essayDraft.trim()) setEssayDraft(buildAssembledEssay());
                    setStep(2);
                  }
                  if (s.n === 3 && aiEvaluation) setStep(3);
                }}
                className={`px-2.5 sm:px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${
                  step === s.n
                    ? 'bg-white text-[#0a5482] shadow-xs'
                    : s.n === 3 && !aiEvaluation
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
          <div className="text-sm text-slate-800 leading-relaxed flex-1">
            <span className="inline-block bg-amber-500 text-white text-[11px] font-extrabold uppercase px-2 py-0.5 rounded mr-2">
              Đề bài
            </span>
            <span className="font-semibold">{payload.topic}</span>
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
                title="Chỉ hiện 4 Từ khóa mỏ neo để luyện thuộc lòng phòng thi"
              >
                🧠 Level 2: Thuộc lòng (4 Mỏ neo)
              </button>
            </div>

            {difficulty === 'level1' && (
              <button
                onClick={() => setShowPillarTableDrawer((v) => !v)}
                className="px-3 py-1.5 rounded-lg bg-white border border-sky-300 text-sky-700 hover:bg-sky-50 text-xs font-bold cursor-pointer shadow-2xs"
              >
                {showPillarTableDrawer ? 'Ẩn bảng 19 Trụ ý' : '📋 Tra cứu nhanh 19 Trụ ý'}
              </button>
            )}
          </div>
        </div>

        {/* ==================== OPTIONAL 19-PILLAR QUICK DRAWER ==================== */}
        {showPillarTableDrawer && difficulty === 'level1' && (
          <div className="bg-white border-b border-slate-200 px-4 sm:px-6 py-3 max-h-60 overflow-y-auto shrink-0">
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-extrabold uppercase text-slate-500">
                Bảng Tra Cứu Nhanh 19 Idea Pillars (Bấm để gán ngay vào Body 1 hoặc Body 2)
              </span>
              <button
                onClick={() => setShowPillarTableDrawer(false)}
                className="text-xs font-bold text-slate-500 hover:text-slate-800 cursor-pointer"
              >
                Đóng bảng ▲
              </button>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2">
              {WT2_PILLARS.map((p) => (
                <div
                  key={p.id}
                  className="border border-slate-200 rounded-lg p-2 bg-slate-50/70 flex items-center justify-between gap-2 text-xs"
                >
                  <div className="min-w-0">
                    <div className="font-bold text-slate-800 truncate">
                      {p.icon} {p.code}. {p.name}{' '}
                      <span className="text-[10px] text-slate-400 font-semibold">(T{p.tier})</span>
                    </div>
                    <div className="text-[11px] text-slate-500 truncate">{p.viName}</div>
                  </div>
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
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ==================== MAIN SCROLLABLE BODY ==================== */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-5">
          {/* -------------------- STEP 1: CHOOSE PILLARS & SLOT -------------------- */}
          {step === 1 && (
            <>
              {/* 1A. Structure Type / Sub-type Selector */}
              <div className="bg-white rounded-xl border border-slate-200 p-4 shadow-2xs space-y-3">
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div>
                    <span className="text-xs font-extrabold uppercase tracking-wider text-sky-600">
                      Bước 1A • Khung Cấu Trúc Bất Biến
                    </span>
                    <h3 className="font-bold text-slate-900 text-sm sm:text-base">
                      {structureDef.name}{' '}
                      <span className="font-normal text-slate-500 text-xs sm:text-sm">
                        — {structureDef.viSubtitle}
                      </span>
                    </h3>
                  </div>

                  {/* Sub-version selectors for Opinion / Mixed */}
                  <div className="flex flex-wrap items-center gap-2">
                    {selectedCategory === 'opinion' && (
                      <>
                        <select
                          value={templateId}
                          onChange={(e) => setTemplateId(e.target.value as Wt2TemplateId)}
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

                    {selectedCategory === 'mixed' && (
                      <select
                        value={templateId}
                        onChange={(e) => {
                          const next = e.target.value as Wt2TemplateId;
                          setTemplateId(next);
                          setPillar2Polarity(next === 'mixed_ps' ? 'positive' : 'negative');
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
                  <div className="grid grid-cols-2 sm:grid-cols-5 gap-2 pt-2 border-t border-slate-100">
                    {CATEGORY_OPTIONS.map((c) => (
                      <button
                        key={c.id}
                        onClick={() => handleCategoryChange(c.id)}
                        className={`p-2 rounded-lg border text-left transition-all cursor-pointer ${
                          selectedCategory === c.id
                            ? 'border-sky-500 bg-sky-50 ring-1 ring-sky-500'
                            : 'border-slate-200 hover:bg-slate-50'
                        }`}
                      >
                        <div className="text-xs font-extrabold text-slate-800">{c.label}</div>
                        <div className="text-[11px] text-slate-500 truncate">{c.shortDesc}</div>
                      </button>
                    ))}
                  </div>
                )}
              </div>

              {/* 1B. Pick 2 Pillars & Drag/Click Cards */}
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                {[
                  {
                    bodyIdx: 1 as const,
                    title: 'Trụ ý cho Body Paragraph 1',
                    accent: 'border-violet-300 bg-violet-50/40',
                    headerBadge: 'bg-violet-600 text-white',
                    pillar: pillar1,
                    setPillarId: setPillar1Id,
                    polarity: pillar1Polarity,
                    setPolarity: setPillar1Polarity,
                    colsToShow: SHUFFLED_COLS
                  },
                  {
                    bodyIdx: 2 as const,
                    title:
                      templateId === 'mixed_ps'
                        ? 'Trụ ý cho Kết Quả Giải Pháp (Body 2 - By doing so)'
                        : 'Trụ ý cho Body Paragraph 2',
                    accent: 'border-amber-300 bg-amber-50/40',
                    headerBadge: 'bg-amber-500 text-white',
                    pillar: pillar2,
                    setPillarId: setPillar2Id,
                    polarity: pillar2Polarity,
                    setPolarity: setPillar2Polarity,
                    colsToShow:
                      templateId === 'mixed_ps' ? (['effect'] as PillarSlotType[]) : SHUFFLED_COLS
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
                      {[1, 2, 3].map((tier) => (
                        <optgroup
                          key={tier}
                          label={
                            tier === 1
                              ? '🟢 TIER 1: BASIC (#1 - #9)'
                              : tier === 2
                              ? '🔵 TIER 2: ADVANCED (#10 - #13)'
                              : '🟣 TIER 3: PRO MASTER (#14 - #19)'
                          }
                        >
                          {WT2_PILLARS.filter((p) => p.tier === tier).map((p) => (
                            <option key={p.id} value={p.id}>
                              {p.code}. {p.name} — {p.viName}
                            </option>
                          ))}
                        </optgroup>
                      ))}
                    </select>

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
                          selectedCard?.bodyIndex === cfg.bodyIdx && selectedCard?.col === col;
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

              {/* Feedback Toast for Slot Placement */}
              <div className="flex flex-wrap items-center justify-between gap-2 bg-white border border-slate-200 rounded-xl px-4 py-2.5">
                <div className="text-xs font-bold text-slate-700 flex items-center gap-2">
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
                    ⚡ Đã thuộc thứ tự cột? Bấm lắp nhanh toàn bộ thẻ Pillar
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
                          const unitKey = `${tok.bodyIndex}_${tok.pillarCol}`;
                          const colInfo = COL_LABELS[tok.pillarCol];

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
                                  placeholder={`[${colInfo.badge} B${tok.bodyIndex}] 🔑 ${getBranchAnchor(
                                    tok.bodyIndex,
                                    tok.pillarCol
                                  )}`}
                                  style={{ width: '440px', maxWidth: '100%' }}
                                  className="px-3 py-1 rounded-lg border-2 border-purple-300 bg-purple-50/70 text-purple-950 font-medium text-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:bg-white"
                                />
                              </span>
                            );
                          }

                          // Level 1: Droppable / Click-to-place slot
                          const isFilled = !!slottedPillarKeys[unitKey];
                          const filledText = getBranchValue(tok.bodyIndex, tok.pillarCol);

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
                                    tok.pillarCol!
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
                                    tok.pillarCol!
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
                              {isFilled
                                ? `✅ ${filledText}`
                                : `📥 [${colInfo.badge} ${tok.bodyIndex}]`}
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

              {/* Right 4 cols: Subject Bank S + 4-Point Checklist */}
              <div className="lg:col-span-4 space-y-4">
                {/* Click-to-insert Subject Bank */}
                <div className="bg-white rounded-xl border border-slate-200 p-4 shadow-2xs space-y-3">
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
                </div>

                {/* 4-Point Self-Edit Checklist */}
                <div className="bg-white rounded-xl border border-slate-200 p-4 shadow-2xs space-y-2.5">
                  <div className="text-xs font-extrabold uppercase text-emerald-700">
                    ✅ Checklist 4 Điểm Mài Mối Nối Trước Khi Nộp
                  </div>
                  {[
                    'Đã thay hết [S] và [...] bằng chủ ngữ & danh từ sát đề bài',
                    'Sau giới từ "due to / related to / of" đã chia chuẩn V-ing hoặc Cụm danh từ',
                    'Ví dụ số liệu (WHO, VietnamWorks, World Bank...) đã gắn đúng ngữ cảnh đề',
                    'Độ dài bài viết đạt từ 250 từ trở lên, chia rõ 4 đoạn văn'
                  ].map((item, idx) => (
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
                    Đang đối chiếu đồng thời 4 tiêu chí IELTS chuẩn quốc tế và độ nhuần nhuyễn của Khung bất biến + Trụ ý ({pillar1.name} &amp; {pillar2.name}).
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
                  {/* Hero Score Banner */}
                  <div className="bg-gradient-to-r from-slate-900 via-[#0a5482] to-indigo-900 text-white rounded-2xl p-5 sm:p-6 flex flex-wrap items-center justify-between gap-4 shadow-md">
                    <div className="space-y-1">
                      <div className="flex items-center gap-2 flex-wrap">
                        <span className="bg-emerald-400/20 text-emerald-200 border border-emerald-400/40 text-xs font-extrabold px-2.5 py-0.5 rounded-full">
                          ✓ Hoàn thành chấm kép
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
                          🏛️ 2. Độ khớp 2 Trụ Ý Pillars
                        </div>
                        <p className="text-xs sm:text-sm text-slate-700 leading-relaxed">
                          {aiEvaluation.formulaReview.pillarFitCheck}
                        </p>
                      </div>
                      <div className="bg-amber-50 border border-amber-200 rounded-xl p-4 space-y-1.5">
                        <div className="text-xs font-extrabold uppercase text-amber-900">
                          🔗 3. Ngữ Pháp Tại Mối Nối
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
              <button
                onClick={() => setStep(2)}
                className="px-4 py-2 rounded-xl border border-sky-300 bg-sky-50 text-sky-800 hover:bg-sky-100 font-bold text-xs sm:text-sm cursor-pointer"
              >
                ✏️ Quay lại Bước 2 sửa theo góp ý AI để nâng Band
              </button>
              <button
                onClick={onClose}
                className="px-5 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-extrabold text-sm cursor-pointer"
              >
                ✅ Hoàn tất &amp; Đóng
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
  const [checked, setChecked] = useState(false);
  const [score, setScore] = useState(0);
  const [streak, setStreak] = useState(0);
  const [timerEnabled, setTimerEnabled] = useState(true);
  const [secondsLeft, setSecondsLeft] = useState(60);

  // ---- Tab 2: 4-Anchor Memory Drill State ----
  const [anchorMode, setAnchorMode] = useState<'cards' | 'quiz'>('cards');
  const [tierFilter, setTierFilter] = useState<0 | 1 | 2 | 3>(0);
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
    setChecked(false);
    setScore(0);
    setStreak(0);
    setSecondsLeft(60);
  };

  const generateNextAnchorQuiz = () => {
    const target = WT2_PILLARS[Math.floor(Math.random() * WT2_PILLARS.length)];
    const distractors = WT2_PILLARS.filter((p) => p.id !== target.id)
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

                  {/* Question B: Pick 2 Pillars */}
                  <div className="bg-white rounded-xl border border-slate-200 p-4 space-y-2.5">
                    <div className="flex items-center justify-between flex-wrap gap-2">
                      <span className="text-xs font-extrabold uppercase text-violet-700">
                        Bước 2 • Nhặt nhanh 2 Trụ Ý khớp nhất cho Body 1 &amp; Body 2 ({pickedPillars.length}/2 đã chọn)
                      </span>
                    </div>
                    <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-2">
                      {WT2_PILLARS.map((p) => {
                        const isPicked = pickedPillars.includes(p.id);
                        const isBest = currentQ.bestPillars.includes(p.id);
                        const isPrimary = currentQ.primaryPair.includes(p.id);
                        let cls = 'border-slate-200 bg-white hover:border-violet-400 text-slate-800';
                        if (checked) {
                          if (isPrimary)
                            cls = 'border-emerald-600 bg-emerald-50 text-emerald-950 ring-2 ring-emerald-400';
                          else if (isBest)
                            cls = 'border-teal-400 bg-teal-50/70 text-teal-900';
                          else if (isPicked)
                            cls = 'border-rose-400 bg-rose-50 text-rose-800';
                        } else if (isPicked) {
                          cls = 'border-violet-600 bg-violet-50 text-violet-950 ring-2 ring-violet-500';
                        }

                        return (
                          <button
                            key={p.id}
                            disabled={checked}
                            onClick={() => togglePickPillar(p.id)}
                            className={`p-2 rounded-lg border text-left text-xs transition-all cursor-pointer ${cls}`}
                          >
                            <div className="font-extrabold truncate">
                              {p.icon} {p.code}. {p.name}
                            </div>
                            <div className="text-[11px] text-slate-500 truncate">{p.viName}</div>
                          </button>
                        );
                      })}
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
                          <button
                            onClick={() => {
                              onClose();
                              onLaunchStudioFromReflex({
                                topic: currentQ.prompt,
                                label: 'Từ Mini-Game Phản Xạ',
                                category: currentQ.correctCategory,
                                presetPillar1: currentQ.primaryPair[0],
                                presetPillar2: currentQ.primaryPair[1]
                              });
                            }}
                            className="px-3 py-1.5 rounded-lg bg-[#0a5482] hover:bg-[#084268] text-white text-xs font-extrabold cursor-pointer"
                          >
                            ✍️ Luyện ghép bài hoàn chỉnh cho đề này luôn!
                          </button>
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
          {tab === 'anchors' && (
            <div className="space-y-4">
              <div className="flex flex-wrap items-center justify-between gap-2 bg-white border border-slate-200 rounded-xl p-3">
                <div className="inline-flex rounded-lg bg-slate-100 p-1 text-xs font-bold">
                  <button
                    onClick={() => setAnchorMode('cards')}
                    className={`px-3 py-1.5 rounded-md cursor-pointer ${
                      anchorMode === 'cards' ? 'bg-white text-indigo-900 shadow-2xs' : 'text-slate-600'
                    }`}
                  >
                    🃏 Thẻ 4 Từ Khóa Mỏ Neo (19 Trụ ý)
                  </button>
                  <button
                    onClick={() => setAnchorMode('quiz')}
                    className={`px-3 py-1.5 rounded-md cursor-pointer ${
                      anchorMode === 'quiz' ? 'bg-white text-indigo-900 shadow-2xs' : 'text-slate-600'
                    }`}
                  >
                    🎯 Quiz Bắn Tốc Độ Nhớ Số Liệu &amp; Cụm Vàng
                  </button>
                </div>

                {anchorMode === 'cards' && (
                  <div className="flex items-center gap-1.5 text-xs font-bold">
                    {[
                      { t: 0 as const, lbl: 'Tất cả (19)' },
                      { t: 1 as const, lbl: 'Tier 1 (9)' },
                      { t: 2 as const, lbl: 'Tier 2 (4)' },
                      { t: 3 as const, lbl: 'Tier 3 (6)' }
                    ].map((f) => (
                      <button
                        key={f.t}
                        onClick={() => setTierFilter(f.t)}
                        className={`px-2.5 py-1 rounded-lg cursor-pointer ${
                          tierFilter === f.t
                            ? 'bg-indigo-600 text-white'
                            : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                        }`}
                      >
                        {f.lbl}
                      </button>
                    ))}
                  </div>
                )}
              </div>

              {anchorMode === 'cards' ? (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {WT2_PILLARS.filter((p) => tierFilter === 0 || p.tier === tierFilter).map((p) => {
                    const isFlipped = !!flippedIds[p.id];
                    const isDone = memorizedIds.includes(p.id);

                    return (
                      <div
                        key={p.id}
                        className={`rounded-xl border-2 p-4 bg-white shadow-2xs flex flex-col justify-between gap-3 transition-all ${
                          isDone ? 'border-emerald-400 bg-emerald-50/25' : 'border-slate-200'
                        }`}
                      >
                        <div className="flex items-center justify-between gap-2">
                          <div>
                            <span className="font-black text-slate-900 text-sm sm:text-base">
                              {p.icon} {p.code}. {p.name}
                            </span>
                            <div className="text-xs text-slate-500">{p.viName}</div>
                          </div>
                          <button
                            onClick={() => toggleMemorized(p.id)}
                            className={`px-2.5 py-1 rounded-full text-xs font-bold cursor-pointer border ${
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
                              <span className="font-extrabold text-emerald-700">(+) Nhánh Tích cực:</span>{' '}
                              {p.positive.pillarSlot} → {p.positive.causeSlot} → {p.positive.effectSlot} →{' '}
                              <em>{p.positive.exampleSlot}</em>
                            </div>
                            <div className="border-t border-slate-200 pt-2">
                              <span className="font-extrabold text-rose-700">(-) Nhánh Tiêu cực:</span>{' '}
                              {p.negative.pillarSlot} → {p.negative.causeSlot} → {p.negative.effectSlot} →{' '}
                              <em>{p.negative.exampleSlot}</em>
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
                  })}
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
                        let cls = 'border-slate-200 bg-slate-50 hover:border-indigo-400 text-slate-800';
                        if (anchorQuizPicked !== null) {
                          if (isRight)
                            cls = 'border-emerald-500 bg-emerald-50 text-emerald-950 ring-2 ring-emerald-400';
                          else if (isPicked)
                            cls = 'border-rose-400 bg-rose-50 text-rose-800';
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
                            <div className="font-extrabold text-sm">
                              {opt.icon} {opt.code}. {opt.name}
                            </div>
                            <div className="text-xs text-slate-500">{opt.viName}</div>
                          </button>
                        );
                      })}
                    </div>

                    {anchorQuizPicked !== null && (
                      <div className="flex justify-end">
                        <button
                          onClick={generateNextAnchorQuiz}
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
          )}
        </div>
      </div>
    </div>
  );
};
