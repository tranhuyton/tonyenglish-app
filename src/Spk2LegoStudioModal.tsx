import React, { useState, useEffect, useMemo, useRef } from 'react';
import { supabase } from './supabase';
import {
  SPK2_LEGO_BLOCKS,
  SPK2_HOOK_FORMULAS,
  SPK2_CONNECTOR_BRIDGES,
  SPK2_PROMPTS_55,
  Spk2BlockId,
  Spk2LegoBlock,
  Spk2StageBrick,
  Spk2PromptItem,
  getSpk2BlockById,
  findSpk2PromptMeta,
  renderStageBrickText
} from './spk2LegoData';

export interface Spk2LegoStudioOpenPayload {
  topic: string;
  promptNum?: number;
  blindMode?: boolean;
  preferredBlockId?: Spk2BlockId;
}

interface Spk2LegoStudioModalProps {
  isOpen: boolean;
  onClose: () => void;
  payload: Spk2LegoStudioOpenPayload | null;
  courseId?: string | null;
}

interface AssembledLegoItem {
  uid: string;
  brick: Spk2StageBrick;
  bridgeBefore?: string;
}

interface Spk2AiEvaluation {
  overall: number;
  recognizedTranscript?: string;
  legoReview?: {
    hookSteeringCheck?: string;
    legoComboCheck?: string;
    cueCardCheck?: string;
  };
  criteria?: { name: string; score: number; comment: string }[];
  correctedHtml?: string;
  upgradedScript?: string;
  generalFeedback?: string;
}

function countWords(text: string): number {
  const cleaned = (text || '').trim();
  if (!cleaned) return 0;
  return cleaned.split(/\s+/).filter(Boolean).length;
}

function formatSeconds(sec: number): string {
  const m = Math.floor(sec / 60);
  const s = sec % 60;
  return `${m}:${s < 10 ? '0' : ''}${s}`;
}

function stripDefaultIntroIfHookPresent(stageText: string, hasCustomHook: boolean): string {
  if (!hasCustomHook) return stageText;
  const stripped = stageText
    .replace(/^I would like to talk about[^.]*\.\s*/i, '')
    .trim();
  if (!stripped) {
    // Single-sentence Stage 1 (e.g. Food Block Stage 1): preserve the dish/slot description seamlessly!
    return stageText.replace(/^I would like to talk about\s+/i, 'Specifically, it was ').trim();
  }
  return stripped;
}

function renderBrickWithSlotHighlights(
  brick: Spk2StageBrick,
  slotValues: Record<string, string>,
  mode: 'palette' | 'tower'
): React.ReactNode {
  if (!brick.templateEn || !brick.slots || brick.slots.length === 0) {
    return brick.textEn;
  }
  const parts = brick.templateEn.split(/(\{\{[a-z0-9_]+\}\})/gi);
  return parts.map((part, idx) => {
    const match = part.match(/^\{\{([a-z0-9_]+)\}\}$/i);
    if (!match) return <React.Fragment key={idx}>{part}</React.Fragment>;
    const slotId = match[1];
    const slotMeta = brick.slots.find((s) => s.id === slotId);
    if (!slotMeta) return <React.Fragment key={idx}>{part}</React.Fragment>;

    const rawOverride = slotValues[slotId];
    const hasCustom =
      mode === 'tower' &&
      rawOverride !== undefined &&
      rawOverride.trim() !== '' &&
      rawOverride.trim() !== slotMeta.defaultEn.trim();
    const displayVal = hasCustom ? rawOverride.trim() : slotMeta.defaultEn;

    if (mode === 'palette') {
      return (
        <span
          key={idx}
          title={`${slotMeta.labelVi} — ${slotMeta.hintVi}`}
          className="inline-flex items-baseline gap-1 px-1.5 py-0.5 mx-0.5 rounded bg-sky-50 text-sky-900 font-semibold border border-dashed border-sky-300"
        >
          <span>{slotMeta.defaultEn}</span>
          <span className="text-[10px] font-extrabold text-sky-600 uppercase">[...]</span>
        </span>
      );
    }

    return hasCustom ? (
      <span
        key={idx}
        title={`Đã tùy biến ${slotMeta.labelVi} (Mặc định gốc: "${slotMeta.defaultEn}")`}
        className="inline-flex items-baseline gap-1 px-1.5 py-0.5 mx-0.5 rounded bg-amber-100 text-amber-950 font-bold border border-amber-400"
      >
        <span>🎯 {displayVal}</span>
      </span>
    ) : (
      <span
        key={idx}
        title={`${slotMeta.labelVi} — Đang giữ mặc định gốc. Sửa ở ô bên dưới để bẻ lái sát đề!`}
        className="inline-flex items-baseline gap-1 px-1.5 py-0.5 mx-0.5 rounded bg-sky-50 text-sky-900 font-semibold border border-dashed border-sky-300"
      >
        <span>{displayVal}</span>
        <span className="text-[10px] font-extrabold text-sky-600">[...]</span>
      </span>
    );
  });
}

function defaultBridgeForBlock(blockId: Spk2BlockId): string {
  const found = SPK2_CONNECTOR_BRIDGES.find((b) => b.targetBlockId === blockId);
  if (found) return found.bridgeEn;
  const fallback = SPK2_CONNECTOR_BRIDGES.find((b) => b.targetBlockId === 'any');
  return fallback ? fallback.bridgeEn : '';
}

export const Spk2LegoStudioModal: React.FC<Spk2LegoStudioModalProps> = ({
  isOpen,
  onClose,
  payload,
  courseId
}) => {
  const [step, setStep] = useState<1 | 2 | 3>(1);
  const [activePrompt, setActivePrompt] = useState<Spk2PromptItem>(() =>
    findSpk2PromptMeta(payload?.topic || '', payload?.promptNum, payload?.preferredBlockId)
  );
  const [showTonyHint, setShowTonyHint] = useState<boolean>(false);
  const [showPromptPicker, setShowPromptPicker] = useState<boolean>(false);

  // Step 1: Lego Palette & Tower State
  const [blockFilter, setBlockFilter] = useState<'all' | 'main' | 'plugin'>('all');
  const [brickViewMode, setBrickViewMode] = useState<'en' | 'keywords' | 'vi'>('en');
  const [expandedBlockIds, setExpandedBlockIds] = useState<Spk2BlockId[]>(['person']);
  const [dragBrickId, setDragBrickId] = useState<string | null>(null);
  const [isDragOverTower, setIsDragOverTower] = useState<boolean>(false);

  const [hookText, setHookText] = useState<string>('');
  const [selectedHookFormulaId, setSelectedHookFormulaId] = useState<string>('');
  const [towerItems, setTowerItems] = useState<AssembledLegoItem[]>([]);
  const [slotValues, setSlotValues] = useState<Record<string, string>>({});
  const [closingText, setClosingText] = useState<string>('');

  // Step 2: Script Editor + 2-Minute Speaking Practice & Audio Recording
  const [scriptDraft, setScriptDraft] = useState<string>('');
  const [teleprompterMode, setTeleprompterMode] = useState<'keywords' | 'vi' | 'full'>('keywords');
  const [practiceSecondsLeft, setPracticeSecondsLeft] = useState<number>(120);
  const [isTimerRunning, setIsTimerRunning] = useState<boolean>(false);

  const [isRecording, setIsRecording] = useState<boolean>(false);
  const [recordSeconds, setRecordSeconds] = useState<number>(0);
  const [recordedAudioUrl, setRecordedAudioUrl] = useState<string | null>(null);
  const [recordedBase64, setRecordedBase64] = useState<string | null>(null);
  const [isPlayingTts, setIsPlayingTts] = useState<boolean>(false);

  // Step 3: AI Grading
  const [isGrading, setIsGrading] = useState<boolean>(false);
  const [gradeError, setGradeError] = useState<string | null>(null);
  const [aiEvaluation, setAiEvaluation] = useState<Spk2AiEvaluation | null>(null);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const recordTimerRef = useRef<number | null>(null);
  const practiceTimerRef = useRef<number | null>(null);

  // Initialize / Reset whenever modal opens with a prompt
  const initForPrompt = (
    promptMeta: Spk2PromptItem,
    blind?: boolean,
    focusBlockId?: Spk2BlockId
  ) => {
    setStep(1);
    setActivePrompt(promptMeta);
    setShowTonyHint(!blind && false); // Always let student try assembling first; 1 click to reveal hint!
    setShowPromptPicker(false);
    setHookText('');
    setSelectedHookFormulaId('');
    setTowerItems([]);
    setSlotValues({});
    setClosingText('');
    setScriptDraft('');
    const initialExpanded: Spk2BlockId[] = [promptMeta.recommendedBlockId];
    if (focusBlockId && !initialExpanded.includes(focusBlockId)) {
      initialExpanded.unshift(focusBlockId);
    }
    setExpandedBlockIds(initialExpanded);
    setAiEvaluation(null);
    setGradeError(null);
    stopAllTimersAndMedia();
    setRecordedAudioUrl(null);
    setRecordedBase64(null);
    setRecordSeconds(0);
    setPracticeSecondsLeft(120);
  };

  useEffect(() => {
    if (isOpen && payload) {
      const meta = findSpk2PromptMeta(
        payload.topic,
        payload.promptNum,
        payload.preferredBlockId
      );
      initForPrompt(meta, payload.blindMode, payload.preferredBlockId);
    }
    return () => {
      stopAllTimersAndMedia();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [isOpen, payload]);

  const stopAllTimersAndMedia = () => {
    if (practiceTimerRef.current) {
      window.clearInterval(practiceTimerRef.current);
      practiceTimerRef.current = null;
    }
    setIsTimerRunning(false);

    if (recordTimerRef.current) {
      window.clearInterval(recordTimerRef.current);
      recordTimerRef.current = null;
    }
    if (mediaRecorderRef.current && mediaRecorderRef.current.state !== 'inactive') {
      try {
        mediaRecorderRef.current.stop();
      } catch (e) {}
    }
    setIsRecording(false);

    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      try {
        window.speechSynthesis.cancel();
      } catch (e) {}
    }
    setIsPlayingTts(false);
  };

  // Countdown Timer Effect
  useEffect(() => {
    if (!isTimerRunning) {
      if (practiceTimerRef.current) {
        window.clearInterval(practiceTimerRef.current);
        practiceTimerRef.current = null;
      }
      return;
    }
    practiceTimerRef.current = window.setInterval(() => {
      setPracticeSecondsLeft((prev) => {
        if (prev <= 1) {
          setIsTimerRunning(false);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => {
      if (practiceTimerRef.current) {
        window.clearInterval(practiceTimerRef.current);
        practiceTimerRef.current = null;
      }
    };
  }, [isTimerRunning]);

  // Distinct Lego blocks currently on the tower
  const distinctBlockIds = useMemo(() => {
    const ids: Spk2BlockId[] = [];
    for (const item of towerItems) {
      if (!ids.includes(item.brick.blockId)) {
        ids.push(item.brick.blockId);
      }
    }
    return ids;
  }, [towerItems]);

  // Anti-Off-Topic Radar stats for "..." Adaptive Slots on the Tower
  const towerSlotStats = useMemo(() => {
    let totalSlots = 0;
    let customizedSlots = 0;
    let availablePromptSuggestions = 0;
    const customizedDetails: { stageTitle: string; labelVi: string; value: string }[] = [];

    for (const item of towerItems) {
      for (const sl of item.brick.slots || []) {
        totalSlots += 1;
        const val = slotValues[sl.id];
        const isCustom =
          val !== undefined && val.trim() !== '' && val.trim() !== sl.defaultEn.trim();
        if (isCustom) {
          customizedSlots += 1;
          customizedDetails.push({
            stageTitle: item.brick.stageTitle,
            labelVi: sl.labelVi,
            value: val.trim()
          });
        }
        if (activePrompt.slotSuggestions?.[sl.id]) {
          availablePromptSuggestions += 1;
        }
      }
    }
    return {
      totalSlots,
      customizedSlots,
      availablePromptSuggestions,
      customizedDetails
    };
  }, [towerItems, slotValues, activePrompt]);

  // Build preview text from Step 1 tower (including customized "..." slots)
  const assembledPreviewText = useMemo(() => {
    const chunks: string[] = [];
    const cleanHook = hookText.trim();
    if (cleanHook) {
      chunks.push(cleanHook);
    }

    towerItems.forEach((item, idx) => {
      const prevBlockId = idx > 0 ? towerItems[idx - 1].brick.blockId : null;
      const isBlockTransition = prevBlockId !== null && prevBlockId !== item.brick.blockId;
      const bridge = isBlockTransition ? (item.bridgeBefore || '').trim() : '';

      const stageWithSlots = renderStageBrickText(item.brick, slotValues);

      const cleanStage =
        idx === 0 && cleanHook && item.brick.stageNumber === 1
          ? stripDefaultIntroIfHookPresent(stageWithSlots, true)
          : isBlockTransition && item.brick.stageNumber === 1 && bridge
          ? stripDefaultIntroIfHookPresent(stageWithSlots, true)
          : stageWithSlots;

      if (bridge) {
        chunks.push(`${bridge} ${cleanStage}`.trim());
      } else {
        chunks.push(cleanStage);
      }
    });

    const cleanClosing = closingText.trim();
    if (cleanClosing) {
      chunks.push(cleanClosing);
    }

    return chunks.join('\n\n');
  }, [hookText, towerItems, closingText, slotValues]);

  const activeWordCount = step === 1 ? countWords(assembledPreviewText) : countWords(scriptDraft);
  const estimatedSpeakSec = Math.round((activeWordCount / 125) * 60); // ~125 wpm natural Band 7.0+ pace

  // Filtered blocks on Step 1 palette
  const filteredBlocks = useMemo(() => {
    if (blockFilter === 'main') return SPK2_LEGO_BLOCKS.filter((b) => b.type === 'main');
    if (blockFilter === 'plugin') return SPK2_LEGO_BLOCKS.filter((b) => b.type === 'plugin');
    return SPK2_LEGO_BLOCKS;
  }, [blockFilter]);

  const toggleExpandBlock = (blockId: Spk2BlockId) => {
    setExpandedBlockIds((prev) =>
      prev.includes(blockId) ? prev.filter((x) => x !== blockId) : [...prev, blockId]
    );
  };

  const updateSlotValue = (slotId: string, val: string) => {
    setSlotValues((prev) => ({ ...prev, [slotId]: val }));
  };

  const resetSlotToDefault = (slotId: string) => {
    setSlotValues((prev) => {
      const next = { ...prev };
      delete next[slotId];
      return next;
    });
  };

  const applyPromptSlotsToTower = () => {
    const next: Record<string, string> = { ...slotValues };
    for (const item of towerItems) {
      for (const sl of item.brick.slots || []) {
        if (activePrompt.slotSuggestions?.[sl.id]) {
          next[sl.id] = activePrompt.slotSuggestions[sl.id];
        } else if (!next[sl.id] && !activePrompt.isDirectMatch && sl.examples.length > 0) {
          next[sl.id] = sl.examples[0].valueEn;
        }
      }
    }
    setSlotValues(next);
  };

  const addSingleBrickToTower = (brick: Spk2StageBrick) => {
    setTowerItems((prev) => {
      const lastBlockId = prev.length > 0 ? prev[prev.length - 1].brick.blockId : null;
      const needsBridge = lastBlockId !== null && lastBlockId !== brick.blockId;
      return [
        ...prev,
        {
          uid: `${brick.id}_${Date.now()}_${Math.random().toString(36).slice(2, 6)}`,
          brick,
          bridgeBefore: needsBridge ? defaultBridgeForBlock(brick.blockId) : ''
        }
      ];
    });
  };

  const addWholeBlockToTower = (block: Spk2LegoBlock) => {
    setTowerItems((prev) => {
      const lastBlockId = prev.length > 0 ? prev[prev.length - 1].brick.blockId : null;
      const needsBridge = lastBlockId !== null && lastBlockId !== block.id;
      const added: AssembledLegoItem[] = block.stages.map((st, i) => ({
        uid: `${st.id}_${Date.now()}_${i}_${Math.random().toString(36).slice(2, 5)}`,
        brick: st,
        bridgeBefore: i === 0 && needsBridge ? defaultBridgeForBlock(block.id) : ''
      }));
      return [...prev, ...added];
    });
  };

  const applyRecommendedCombo = () => {
    const mainBlock = getSpk2BlockById(activePrompt.recommendedBlockId);
    setHookText(activePrompt.sampleHookEn);
    setClosingText(activePrompt.sampleClosingEn);
    setSelectedHookFormulaId('recommended');
    setSlotValues({ ...(activePrompt.slotSuggestions || {}) });

    const newItems: AssembledLegoItem[] = mainBlock.stages.map((st, idx) => ({
      uid: `${st.id}_rec_${idx}_${Date.now()}`,
      brick: st,
      bridgeBefore: ''
    }));

    if (activePrompt.recommendedPluginIds.length > 0) {
      const pluginBlock = getSpk2BlockById(activePrompt.recommendedPluginIds[0]);
      // Snap Stages 2 & 4 of the Plugin block with a smooth connector bridge so total length stays ~200-235 words!
      const selectedPluginStages = [pluginBlock.stages[1], pluginBlock.stages[3]].filter(Boolean);
      selectedPluginStages.forEach((st, pIdx) => {
        newItems.push({
          uid: `${st.id}_plug_${pIdx}_${Date.now()}`,
          brick: st,
          bridgeBefore: pIdx === 0 ? defaultBridgeForBlock(pluginBlock.id) : ''
        });
      });
    }

    setTowerItems(newItems);
  };

  const moveTowerItem = (index: number, dir: -1 | 1) => {
    const nextIdx = index + dir;
    if (nextIdx < 0 || nextIdx >= towerItems.length) return;
    setTowerItems((prev) => {
      const copy = [...prev];
      const [moved] = copy.splice(index, 1);
      copy.splice(nextIdx, 0, moved);
      return copy;
    });
  };

  const removeTowerItem = (uid: string) => {
    setTowerItems((prev) => prev.filter((x) => x.uid !== uid));
  };

  const updateBridgeText = (uid: string, val: string) => {
    setTowerItems((prev) =>
      prev.map((x) => (x.uid === uid ? { ...x, bridgeBefore: val } : x))
    );
  };

  const handleProceedToStep2 = () => {
    if (towerItems.length === 0) return;
    setScriptDraft(assembledPreviewText);
    setStep(2);
  };

  // Golden Band 7.5+ Phrases Check in current script
  const detectedGoldenPhrases = useMemo(() => {
    const checks = [
      { label: 'If my memory serves me well / As far as I recall', regex: /memory serves me well|as far as i (recall|remember)/i },
      { label: "If it hadn't been for / If it weren't for (Đảo ngữ/ĐK loại 3)", regex: /if (it hadn't been|i hadn't|it weren't) for|if i hadn't (had|gone)/i },
      { label: 'Although / Even though (Mệnh đề nhượng bộ)', regex: /\b(although|even though)\b/i },
      { label: 'Not only ... but also ...', regex: /not only\b[\s\S]*?\bbut\b/i },
      { label: 'Idioms (piece of cake / blown away / tied the knot / thick and thin)', regex: /piece of cake|blown away|tied the knot|thick and thin|walking on sticks|springs to my mind/i }
    ];
    return checks.map((c) => ({
      label: c.label,
      matched: c.regex.test(scriptDraft)
    }));
  }, [scriptDraft]);

  // TTS Model Reading
  const handleToggleTts = () => {
    if (typeof window === 'undefined' || !('speechSynthesis' in window)) return;
    if (isPlayingTts) {
      window.speechSynthesis.cancel();
      setIsPlayingTts(false);
      return;
    }
    const text = (scriptDraft || assembledPreviewText).trim();
    if (!text) return;
    window.speechSynthesis.cancel();
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = 'en-GB';
    utter.rate = 0.96;
    const voices = window.speechSynthesis.getVoices();
    const gbVoice =
      voices.find((v) => v.lang.includes('en-GB') && /Google|Natural|Daniel|Libby|Sonia/i.test(v.name)) ||
      voices.find((v) => v.lang.includes('en-GB')) ||
      voices.find((v) => v.lang.startsWith('en'));
    if (gbVoice) utter.voice = gbVoice;
    utter.onend = () => setIsPlayingTts(false);
    utter.onerror = () => setIsPlayingTts(false);
    setIsPlayingTts(true);
    window.speechSynthesis.speak(utter);
  };

  // Voice Recording in Step 2
  const handleStartRecording = async () => {
    try {
      stopAllTimersAndMedia();
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream);
      audioChunksRef.current = [];

      recorder.ondataavailable = (ev) => {
        if (ev.data && ev.data.size > 0) {
          audioChunksRef.current.push(ev.data);
        }
      };

      recorder.onstop = () => {
        stream.getTracks().forEach((t) => t.stop());
        if (recordTimerRef.current) {
          window.clearInterval(recordTimerRef.current);
          recordTimerRef.current = null;
        }
        const blob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
        if (blob.size > 0) {
          const url = URL.createObjectURL(blob);
          setRecordedAudioUrl(url);
          const reader = new FileReader();
          reader.onloadend = () => {
            const res = String(reader.result || '');
            const commaIdx = res.indexOf(',');
            if (commaIdx !== -1) {
              setRecordedBase64(res.slice(commaIdx + 1));
            }
          };
          reader.readAsDataURL(blob);
        }
      };

      mediaRecorderRef.current = recorder;
      recorder.start();
      setIsRecording(true);
      setRecordSeconds(0);
      setPracticeSecondsLeft(120);
      setIsTimerRunning(true);

      recordTimerRef.current = window.setInterval(() => {
        setRecordSeconds((prev) => {
          if (prev >= 135) {
            handleStopRecording();
            return prev;
          }
          return prev + 1;
        });
      }, 1000);
    } catch (err: any) {
      alert('Không thể truy cập Microphone. Vui lòng cấp quyền Micro trên trình duyệt để thu âm nhé!');
    }
  };

  const handleStopRecording = () => {
    if (mediaRecorderRef.current && mediaRecorderRef.current.state !== 'inactive') {
      mediaRecorderRef.current.stop();
    }
    setIsRecording(false);
    setIsTimerRunning(false);
  };

  // Step 3: Submit to AI Grader (Script OR Audio + Script)
  const handleGradeWithAI = async (useAudio: boolean) => {
    const finalScript = (scriptDraft || assembledPreviewText).trim();
    if (!finalScript && !recordedBase64) return;

    stopAllTimersAndMedia();
    setStep(3);
    setIsGrading(true);
    setGradeError(null);
    setAiEvaluation(null);

    try {
      const chosenBlocksSummary = distinctBlockIds
        .map((id) => {
          const b = getSpk2BlockById(id);
          return `${b.code}. ${b.name}`;
        })
        .join(' + ');

      const audioNote =
        useAudio && recordedBase64
          ? `Học viên CÓ đính kèm file ghi âm giọng nói thực tế (audio/webm). Hãy lắng nghe kỹ file âm thanh để:
1) Chép lại chính xác những gì học viên thực sự nói vào trường "recognizedTranscript".
2) Chấm điểm Phát âm (Pronunciation), Độ trôi chảy (Fluency) & Ngữ điệu thực tế kết hợp với Kịch bản Lego học viên đã soạn.`
          : `Học viên gửi Kịch bản bài nói Speaking Part 2 đã tự lắp ghép từ hệ thống Lego Blocks (chưa gửi file ghi âm). Hãy chấm chất lượng Kịch bản nói, Độ mượt của câu Hook bẻ lái, Từ vựng, Ngữ pháp và khả năng đạt Band cao khi nói kịch bản này trong 2 phút.`;

      const customizedSlotsSummary =
        towerSlotStats.customizedDetails.length > 0
          ? towerSlotStats.customizedDetails
              .map((d) => `- ${d.stageTitle} (${d.labelVi}): "${d.value}"`)
              .join('\n')
          : 'Chưa tùy biến khe "..." nào trong thân bài (đang giữ nguyên văn mẫu gốc).';

      const prompt = `
Bạn là Giám khảo IELTS Speaking kiêm Huấn luyện viên chiến thuật "Lego Blocks & Hook Bẻ Lái" của TonyEnglish.vn. Luôn xưng "Thầy" và gọi học viên là "em".

ĐỀ BÀI CUE CARD (IELTS SPEAKING PART 2):
"${activePrompt.title}"
You should say:
${activePrompt.cueBullets.map((b) => `- ${b}`).join('\n')}

CÁC KHỐI LEGO HỌC VIÊN ĐÃ CHỌN LẮP GHÉP:
${chosenBlocksSummary || 'Tự viết tự do'}

CÁC KHE TÙY BIẾN "..." (MỎ NEO CHỐNG LẠC ĐỀ TRONG THÂN BÀI):
${customizedSlotsSummary}

KỊCH BẢN BÀI NÓI HỌC VIÊN ĐÃ LẮP & CHỈNH SỬA (${countWords(finalScript)} từ):
"""
${finalScript}
"""

CHẾ ĐỘ CHẤM:
${audioNote}

YÊU CẦU ĐÁNH GIÁ:
1. Kiểm tra xem Câu Hook mở bài đã "bẻ lái" mượt mà, tự nhiên từ đề bài "${activePrompt.title}" sang Khối Lego (${chosenBlocksSummary}) mà KHÔNG bị lạc đề (off-topic) chưa.
2. ĐẶC BIỆT kiểm tra các Khe tùy biến "..." trong thân bài (Stages 1–4): Học viên đã khéo léo cài từ khóa/ngữ cảnh của đề bài vào giữa thân bài chưa, hay câu Hook nói một đằng mà thân bài giữ nguyên chi tiết mẫu gốc gây mâu thuẫn / lộ bài học vẹt?
3. Kiểm tra các khớp nối đại từ/thì động từ/ngữ cảnh giữa Câu Hook, các Stage của Main Block/Plugin Block và Câu chốt cuối bài, đồng thời kiểm tra các cấu trúc ăn điểm Band 7.5+ ("If my memory serves me well", "If it hadn't been for...", "Not only... but also...", "Although / Even though").

TRẢ VỀ DUY NHẤT JSON HỢP LỆ (KHÔNG markdown backticks):
{
  "overall": 7.5,
  "recognizedTranscript": "${useAudio && recordedBase64 ? 'Chép lại lời học viên nói trong audio...' : ''}",
  "legoReview": {
    "hookSteeringCheck": "Nhận xét chi tiết bằng tiếng Việt về độ mượt và logic của câu Hook bẻ lái...",
    "legoComboCheck": "Nhận xét về cách kết hợp các khối Lego, cách tùy biến các khe '...' chống lạc đề và việc vận dụng cấu trúc vàng...",
    "cueCardCheck": "Nhận xét xem bài nói đã bao phủ khéo léo các ý trên Cue Card xuyên suốt thân bài và câu chốt chưa..."
  },
  "criteria": [
    { "name": "Fluency & Coherence", "score": 7.5, "comment": "Nhận xét tiếng Việt..." },
    { "name": "Lexical Resource", "score": 7.5, "comment": "Nhận xét tiếng Việt..." },
    { "name": "Grammatical Range & Accuracy", "score": 7.5, "comment": "Nhận xét tiếng Việt..." },
    { "name": "${useAudio && recordedBase64 ? 'Pronunciation (Qua Audio)' : 'Natural Spoken Delivery'}", "score": 7.0, "comment": "Nhận xét tiếng Việt..." }
  ],
  "correctedHtml": "Toàn bộ kịch bản của học viên giữ chia đoạn bằng <br/><br/>, chỗ nào nối còn gượng/sai ngữ pháp/lệch đại từ thì bọc <span class='bg-red-100 text-red-700 line-through px-1 rounded'>cụm gốc</span> và đặt ngay sau đó <span class='bg-emerald-100 text-emerald-800 font-bold px-1 rounded'>cụm sửa mượt tự nhiên</span>.",
  "upgradedScript": "Bản kịch bản nói Band 8.0+ hoàn chỉnh (khoảng 190-230 từ), giữ nguyên 90% câu chữ các Khối Lego gốc của học viên nhưng gọt câu Hook và câu chốt mượt như người bản xứ.",
  "generalFeedback": "Lời khen và 2 mẹo nhỏ của Thầy để em nói bài này tự nhiên nhất trong phòng thi."
}
      `.trim();

      const { data, error } = await supabase.functions.invoke('ai-grader', {
        body: {
          prompt,
          base64Audio: useAudio && recordedBase64 ? recordedBase64 : undefined,
          model: 'gemini-2.5-flash'
        }
      });

      if (error) throw new Error(error.message);
      if (data?.error) throw new Error(data.error);

      const cleaned = String(data?.result || '')
        .replace(/```(?:json)?/gi, '')
        .replace(/```/g, '')
        .trim();
      const parsed: Spk2AiEvaluation = JSON.parse(cleaned);
      setAiEvaluation(parsed);

      const {
        data: { user }
      } = await supabase.auth.getUser();
      if (user) {
        await supabase.from('test_results').insert([
          {
            user_id: user.id,
            course_id: courseId || null,
            test_title: `[Speaking Lego] #${activePrompt.num || ''} ${activePrompt.title}`.trim(),
            test_type: 'IELTS-Speaking',
            score: parsed.overall || 0,
            total_score: 9,
            time_spent: recordSeconds || 0,
            details: {
              mode: 'spk2_lego_studio',
              topic: activePrompt.title,
              blocksUsed: distinctBlockIds,
              hasAudio: Boolean(useAudio && recordedBase64),
              script: finalScript,
              wordCount: countWords(finalScript),
              aiFeedback: parsed
            }
          }
        ]);
      }
    } catch (err: any) {
      setGradeError(err?.message || 'Hệ thống AI đang bận, em vui lòng bấm chấm lại nhé!');
    } finally {
      setIsGrading(false);
    }
  };

  // Trigger Live 1-1 Speaking Examiner directly with this topic
  const handleLaunchLiveExaminer = () => {
    stopAllTimersAndMedia();
    const topicStr = activePrompt.title;
    onClose();
    setTimeout(() => {
      const fakeLiveBtn = document.createElement('button');
      fakeLiveBtn.className = 'btn-live-trigger hidden';
      fakeLiveBtn.setAttribute('data-topic', topicStr);
      document.body.appendChild(fakeLiveBtn);
      fakeLiveBtn.click();
      setTimeout(() => fakeLiveBtn.remove(), 120);
    }, 80);
  };

  // Trigger AI Tutor Sidebar directly with this topic
  const handleOpenAiSidebar = () => {
    stopAllTimersAndMedia();
    const topicStr = activePrompt.title;
    onClose();
    setTimeout(() => {
      const fakeAiBtn = document.createElement('button');
      fakeAiBtn.className = 'btn-ai-trigger hidden';
      fakeAiBtn.setAttribute('data-task', 'speaking');
      fakeAiBtn.setAttribute('data-topic', topicStr);
      document.body.appendChild(fakeAiBtn);
      fakeAiBtn.click();
      setTimeout(() => fakeAiBtn.remove(), 120);
    }, 80);
  };

  if (!isOpen) return null;

  const recommendedMain = getSpk2BlockById(activePrompt.recommendedBlockId);

  return (
    <div className="fixed inset-0 z-[9998] bg-slate-950/75 backdrop-blur-sm flex items-center justify-center p-2 sm:p-4 overflow-y-auto">
      <div className="bg-white w-full max-w-6xl rounded-2xl shadow-2xl border border-slate-200 flex flex-col max-h-[95vh] overflow-hidden">
        {/* ==================== TOP STUDIO HEADER ==================== */}
        <div className="bg-gradient-to-r from-[#1e1b4b] via-[#312e81] to-[#4c1d95] text-white px-4 sm:px-6 py-3.5 flex flex-wrap items-center justify-between gap-3 shrink-0">
          <div className="flex items-center gap-3 min-w-0">
            <div className="w-10 h-10 rounded-xl bg-amber-400 text-slate-900 font-black text-xl flex items-center justify-center shadow-md shrink-0">
              🧩
            </div>
            <div className="min-w-0">
              <div className="flex items-center gap-2 flex-wrap">
                <span className="text-[11px] font-extrabold uppercase tracking-wider px-2 py-0.5 rounded-full bg-amber-400/20 text-amber-300 border border-amber-300/30">
                  Xưởng Lắp Ghép Lego • Speaking Part 2
                </span>
                <button
                  type="button"
                  onClick={() => setShowPromptPicker((v) => !v)}
                  className="text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-white/15 hover:bg-white/25 text-indigo-100 transition cursor-pointer"
                >
                  📚 Đổi đề khác (55 đề) ▾
                </button>
              </div>
              <h2 className="text-sm sm:text-base font-extrabold text-white truncate mt-0.5">
                {activePrompt.num ? `Đề #${activePrompt.num}: ` : ''}
                {activePrompt.title}
              </h2>
            </div>
          </div>

          {/* Stepper Pills + Close */}
          <div className="flex items-center gap-2 flex-wrap">
            <div className="flex items-center bg-black/25 rounded-xl p-1 gap-1">
              <button
                type="button"
                onClick={() => setStep(1)}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold transition cursor-pointer ${
                  step === 1
                    ? 'bg-amber-400 text-slate-950 shadow'
                    : 'text-indigo-200 hover:text-white'
                }`}
              >
                1. Lắp Hook & Lego
              </button>
              <button
                type="button"
                disabled={towerItems.length === 0 && !scriptDraft.trim()}
                onClick={() => {
                  if (!scriptDraft.trim() && assembledPreviewText.trim()) {
                    setScriptDraft(assembledPreviewText);
                  }
                  setStep(2);
                }}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold transition cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed ${
                  step === 2
                    ? 'bg-amber-400 text-slate-950 shadow'
                    : 'text-indigo-200 hover:text-white'
                }`}
              >
                2. Gọt & Tập Nói 2p
              </button>
              <button
                type="button"
                disabled={!scriptDraft.trim() && !assembledPreviewText.trim()}
                onClick={() => {
                  if (!scriptDraft.trim() && assembledPreviewText.trim()) {
                    setScriptDraft(assembledPreviewText);
                  }
                  setStep(3);
                }}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold transition cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed ${
                  step === 3
                    ? 'bg-amber-400 text-slate-950 shadow'
                    : 'text-indigo-200 hover:text-white'
                }`}
              >
                3. AI Chấm Điểm
              </button>
            </div>

            <button
              type="button"
              onClick={() => {
                stopAllTimersAndMedia();
                onClose();
              }}
              className="w-8 h-8 rounded-lg bg-white/10 hover:bg-red-500/80 text-white font-bold flex items-center justify-center transition cursor-pointer"
              title="Đóng"
            >
              ✕
            </button>
          </div>
        </div>

        {/* ==================== 55 PROMPT SWITCHER DRAWER ==================== */}
        {showPromptPicker && (
          <div className="bg-indigo-950 text-white px-5 py-3 border-b border-indigo-800 max-h-56 overflow-y-auto shrink-0">
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-bold text-amber-300 uppercase tracking-wider">
                Chọn nhanh 1 trong 55 đề thi thật IELTS Speaking Part 2:
              </span>
              <button
                type="button"
                onClick={() => setShowPromptPicker(false)}
                className="text-xs text-indigo-300 hover:text-white cursor-pointer"
              >
                Thu gọn ▲
              </button>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-1.5">
              {SPK2_PROMPTS_55.map((p) => (
                <button
                  key={p.num}
                  type="button"
                  onClick={() => initForPrompt(p, false)}
                  className={`text-left px-2.5 py-1.5 rounded-lg text-xs transition truncate cursor-pointer ${
                    activePrompt.num === p.num
                      ? 'bg-amber-400 text-slate-950 font-bold'
                      : 'bg-white/5 hover:bg-white/15 text-indigo-100'
                  }`}
                >
                  {p.num}. {p.title}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* ==================== CUE CARD + TONY HINT STRIP ==================== */}
        <div className="bg-slate-50 border-b border-slate-200 px-4 sm:px-6 py-3 shrink-0">
          <div className="flex flex-wrap items-start justify-between gap-3">
            <div className="flex-1 min-w-[260px]">
              <div className="flex items-center gap-2 flex-wrap mb-1">
                <span className="text-xs font-extrabold uppercase tracking-wider text-purple-700 bg-purple-100 px-2 py-0.5 rounded-md">
                  🗂️ Cue Card Đề Thi
                </span>
                <span className="text-xs text-slate-600 font-medium">
                  You should say:{' '}
                  {activePrompt.cueBullets.map((b, idx) => (
                    <span key={idx} className="inline-block bg-white border border-slate-200 rounded px-2 py-0.5 mr-1.5 mb-1 text-[11.5px] text-slate-700">
                      • {b}
                    </span>
                  ))}
                </span>
              </div>
            </div>

            <div className="flex items-center gap-2 flex-wrap">
              <div
                className={`px-3 py-1 rounded-lg text-xs font-bold border ${
                  activeWordCount >= 150 && activeWordCount <= 255
                    ? 'bg-emerald-50 border-emerald-300 text-emerald-800'
                    : activeWordCount > 255
                    ? 'bg-amber-50 border-amber-300 text-amber-800'
                    : 'bg-slate-100 border-slate-200 text-slate-700'
                }`}
              >
                🎙️ {activeWordCount} từ (~{formatSeconds(estimatedSpeakSec)} / mục tiêu 1:30–2:00)
              </div>

              <button
                type="button"
                onClick={() => setShowTonyHint((v) => !v)}
                className="px-3 py-1 rounded-lg text-xs font-bold bg-amber-100 hover:bg-amber-200 text-amber-900 border border-amber-300 transition cursor-pointer"
              >
                {showTonyHint ? '🙈 Ẩn Gợi ý Bẻ lái' : '💡 Xem Gợi ý Chiến thuật'}
              </button>
            </div>
          </div>

          {showTonyHint && (
            <div className="mt-2.5 bg-amber-50/90 border border-amber-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div className="text-xs text-slate-800 leading-relaxed space-y-1">
                <div>
                  <span className="font-extrabold text-amber-900">🎯 Khối Lego khuyên dùng: </span>
                  <span className="inline-flex items-center gap-1 font-bold px-2 py-0.5 rounded bg-white border border-amber-300 text-slate-900 mr-1.5">
                    {recommendedMain.emoji} {recommendedMain.code}. {recommendedMain.name}
                  </span>
                  {activePrompt.recommendedPluginIds.map((pid) => {
                    const pb = getSpk2BlockById(pid);
                    return (
                      <span
                        key={pid}
                        className="inline-flex items-center gap-1 font-bold px-2 py-0.5 rounded bg-white border border-purple-200 text-purple-900 mr-1"
                      >
                        + 🔌 {pb.emoji} {pb.name}
                      </span>
                    );
                  })}
                </div>
                <div>
                  <span className="font-extrabold text-amber-900">🔗 Logic bẻ lái: </span>
                  {activePrompt.hookLogicVi}
                </div>
              </div>
              <button
                type="button"
                onClick={applyRecommendedCombo}
                className="shrink-0 px-3.5 py-2 rounded-xl bg-amber-500 hover:bg-amber-600 text-white text-xs font-extrabold shadow-sm transition cursor-pointer"
              >
                ⚡ Lắp nhanh Combo Mẫu này
              </button>
            </div>
          )}
        </div>

        {/* ==================== MAIN MODAL BODY ==================== */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 bg-slate-100/70">
          {/* ========================================================= */}
          {/* STEP 1: SELECT HOOK & SNAP LEGO BLOCKS                    */}
          {/* ========================================================= */}
          {step === 1 && (
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-5">
              {/* LEFT 6 COLS: 9 LEGO BLOCKS PALETTE */}
              <div className="lg:col-span-6 bg-white rounded-2xl border border-slate-200 shadow-sm p-4 flex flex-col">
                <div className="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-slate-100">
                  <div>
                    <h3 className="text-sm font-extrabold text-slate-900 uppercase tracking-wide">
                      🧱 Kho 9 Khối Lego Cốt Lõi
                    </h3>
                    <p className="text-xs text-slate-500">
                      Bấm <b>+ Lắp cả khối</b> hoặc mở từng khối để <b>kéo thả / chọn lẻ từng Stage</b> (Tối đa 1–3 khối)
                    </p>
                  </div>

                  {/* View Mode Switcher */}
                  <div className="flex bg-slate-100 rounded-lg p-0.5 text-[11px] font-bold">
                    <button
                      type="button"
                      onClick={() => setBrickViewMode('en')}
                      className={`px-2 py-1 rounded-md cursor-pointer ${
                        brickViewMode === 'en' ? 'bg-white text-slate-900 shadow-sm' : 'text-slate-600'
                      }`}
                    >
                      📖 Câu Anh
                    </button>
                    <button
                      type="button"
                      onClick={() => setBrickViewMode('keywords')}
                      className={`px-2 py-1 rounded-md cursor-pointer ${
                        brickViewMode === 'keywords' ? 'bg-white text-orange-700 shadow-sm' : 'text-slate-600'
                      }`}
                    >
                      🔑 Keyword
                    </button>
                    <button
                      type="button"
                      onClick={() => setBrickViewMode('vi')}
                      className={`px-2 py-1 rounded-md cursor-pointer ${
                        brickViewMode === 'vi' ? 'bg-white text-emerald-700 shadow-sm' : 'text-slate-600'
                      }`}
                    >
                      🇻🇳 Nghĩa Việt
                    </button>
                  </div>
                </div>

                {/* Filter Tabs: All / 6 Main / 3 Plugin */}
                <div className="flex gap-1.5 my-3">
                  <button
                    type="button"
                    onClick={() => setBlockFilter('all')}
                    className={`px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
                      blockFilter === 'all'
                        ? 'bg-indigo-600 text-white'
                        : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                    }`}
                  >
                    Tất cả (9)
                  </button>
                  <button
                    type="button"
                    onClick={() => setBlockFilter('main')}
                    className={`px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
                      blockFilter === 'main'
                        ? 'bg-blue-600 text-white'
                        : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                    }`}
                  >
                    🎯 6 Main Blocks
                  </button>
                  <button
                    type="button"
                    onClick={() => setBlockFilter('plugin')}
                    className={`px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
                      blockFilter === 'plugin'
                        ? 'bg-purple-600 text-white'
                        : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                    }`}
                  >
                    🔌 3 Plugin Blocks
                  </button>
                </div>

                {/* Scrollable Block List */}
                <div className="space-y-2.5 max-h-[540px] overflow-y-auto pr-1">
                  {filteredBlocks.map((block) => {
                    const isExpanded = expandedBlockIds.includes(block.id);
                    const isUsed = distinctBlockIds.includes(block.id);
                    return (
                      <div
                        key={block.id}
                        className={`rounded-xl border-2 transition ${
                          isUsed ? `${block.borderClass} bg-slate-50/70` : 'border-slate-200 bg-white'
                        }`}
                      >
                        <div className="p-3 flex items-center justify-between gap-2">
                          <button
                            type="button"
                            onClick={() => toggleExpandBlock(block.id)}
                            className="flex items-center gap-2.5 text-left min-w-0 flex-1 cursor-pointer"
                          >
                            <span className="text-xl shrink-0">{block.emoji}</span>
                            <div className="min-w-0">
                              <div className="flex items-center gap-1.5 flex-wrap">
                                <span
                                  className={`text-[10.5px] font-extrabold px-2 py-0.5 rounded-full ${block.badgeBg} ${block.badgeText}`}
                                >
                                  {block.type === 'main' ? `MAIN ${block.code}` : `PLUGIN ${block.code}`}
                                </span>
                                <span className="text-sm font-extrabold text-slate-900 truncate">
                                  {block.name}
                                </span>
                              </div>
                              <p className="text-[11.5px] text-slate-500 line-clamp-1 mt-0.5">
                                {block.usedFor}
                              </p>
                            </div>
                          </button>

                          <div className="flex items-center gap-1.5 shrink-0">
                            <button
                              type="button"
                              onClick={() => addWholeBlockToTower(block)}
                              className="px-2.5 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold shadow-sm transition cursor-pointer"
                            >
                              + Cả khối
                            </button>
                            <button
                              type="button"
                              onClick={() => toggleExpandBlock(block.id)}
                              className="w-7 h-7 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold flex items-center justify-center cursor-pointer"
                              title="Mở 4 Stage lẻ"
                            >
                              {isExpanded ? '▲' : '▼'}
                            </button>
                          </div>
                        </div>

                        {isExpanded && (
                          <div className="px-3 pb-3 pt-1 border-t border-slate-100 space-y-2">
                            {block.stages.map((st) => {
                              const alreadyInTower = towerItems.some((t) => t.brick.id === st.id);
                              return (
                                <div
                                  key={st.id}
                                  draggable
                                  onDragStart={() => setDragBrickId(st.id)}
                                  onDragEnd={() => setDragBrickId(null)}
                                  className={`p-2.5 rounded-lg border text-xs transition cursor-grab active:cursor-grabbing ${
                                    alreadyInTower
                                      ? 'bg-emerald-50/60 border-emerald-300'
                                      : 'bg-slate-50 hover:bg-indigo-50/40 border-slate-200'
                                  }`}
                                >
                                  <div className="flex items-center justify-between gap-2 mb-1">
                                    <span className="font-extrabold text-slate-800">
                                      🧱 {st.stageTitle}
                                    </span>
                                    <button
                                      type="button"
                                      onClick={() => addSingleBrickToTower(st)}
                                      className="px-2 py-0.5 rounded bg-white hover:bg-indigo-600 hover:text-white text-indigo-700 border border-indigo-200 font-bold text-[11px] transition cursor-pointer"
                                    >
                                      + Lắp Stage {st.stageNumber}
                                    </button>
                                  </div>

                                  {brickViewMode === 'en' && (
                                    <p className="text-slate-700 leading-relaxed">
                                      {renderBrickWithSlotHighlights(st, {}, 'palette')}
                                    </p>
                                  )}
                                  {brickViewMode === 'vi' && (
                                    <p className="text-emerald-900 leading-relaxed">{st.textVi}</p>
                                  )}
                                  {brickViewMode === 'keywords' && (
                                    <div className="flex flex-wrap items-center gap-1 mt-1">
                                      {st.keywords.map((kw, ki) => (
                                        <React.Fragment key={ki}>
                                          <span className="px-2 py-0.5 rounded-full bg-orange-100 text-orange-800 font-bold text-[11px]">
                                            {kw}
                                          </span>
                                          {ki < st.keywords.length - 1 && (
                                            <span className="text-orange-400 font-bold">➔</span>
                                          )}
                                        </React.Fragment>
                                      ))}
                                    </div>
                                  )}
                                </div>
                              );
                            })}
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>

              {/* RIGHT 6 COLS: STUDENT'S ASSEMBLED SPEAKING TOWER */}
              <div className="lg:col-span-6 bg-white rounded-2xl border border-slate-200 shadow-sm p-4 flex flex-col">
                <div className="flex items-center justify-between gap-2 pb-3 border-b border-slate-100">
                  <div>
                    <h3 className="text-sm font-extrabold text-slate-900 uppercase tracking-wide">
                      🏗️ Tháp Bài Nói 2 Phút Của Em
                    </h3>
                    <p className="text-xs text-slate-500">
                      1) <b>Câu Hook bẻ lái</b> ➔ 2) Lắp <b>Lego & Điền khe <code className="text-amber-700 font-extrabold">...</code></b> ➔ 3) <b>Câu chốt bám đề</b>
                    </p>
                  </div>
                  {towerItems.length > 0 && (
                    <button
                      type="button"
                      onClick={() => {
                        setTowerItems([]);
                        setSlotValues({});
                        setHookText('');
                        setClosingText('');
                      }}
                      className="text-xs font-bold text-red-600 hover:text-red-700 px-2 py-1 rounded hover:bg-red-50 cursor-pointer"
                    >
                      🧹 Xóa làm lại
                    </button>
                  )}
                </div>

                {/* Warning if > 3 distinct Lego blocks */}
                {distinctBlockIds.length > 3 && (
                  <div className="mt-2.5 bg-red-50 border border-red-200 rounded-xl px-3 py-2 text-xs text-red-800 font-semibold">
                    ⚠️ Lưu ý quy tắc vàng của thầy Tony: Em đang ghép <b>{distinctBlockIds.length} khối</b> khác nhau. Chỉ nên kết hợp <b>tối đa 2–3 khối</b> để nói trôi chảy vừa vặn trong 2 phút nhé!
                  </div>
                )}

                <div className="space-y-3 mt-3 flex-1 overflow-y-auto pr-1 max-h-[540px]">
                  {/* 1. TOP CAP: STEERING HOOK */}
                  <div className="rounded-xl border-2 border-amber-300 bg-amber-50/60 p-3">
                    <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
                      <span className="text-xs font-extrabold text-amber-900 uppercase">
                        🔗 Tầng 1: Câu Hook Mở Bài (Bẻ Lái Từ Đề Vào Lego)
                      </span>
                      <button
                        type="button"
                        onClick={() => {
                          setHookText(activePrompt.sampleHookEn);
                          setSelectedHookFormulaId('recommended');
                        }}
                        className="text-[11px] font-bold px-2.5 py-1 rounded-lg bg-amber-500 hover:bg-amber-600 text-white transition cursor-pointer"
                      >
                        ✨ Điền Hook mẫu đề này
                      </button>
                    </div>

                    {/* 5 Universal Hook Formula Pills */}
                    <div className="flex flex-wrap gap-1 mb-2">
                      {SPK2_HOOK_FORMULAS.map((hf) => (
                        <button
                          key={hf.id}
                          type="button"
                          onClick={() => {
                            setSelectedHookFormulaId(hf.id);
                            setHookText(hf.templateEn);
                          }}
                          title={hf.guideVi}
                          className={`text-[11px] px-2 py-0.5 rounded-md font-semibold border transition cursor-pointer ${
                            selectedHookFormulaId === hf.id
                              ? 'bg-amber-700 text-white border-amber-700'
                              : 'bg-white text-amber-900 border-amber-200 hover:bg-amber-100'
                          }`}
                        >
                          {hf.name}
                        </button>
                      ))}
                    </div>

                    <textarea
                      rows={2}
                      value={hookText}
                      onChange={(e) => setHookText(e.target.value)}
                      placeholder="Chọn 1 mẫu câu Hook ở trên rồi sửa phần [...] (hoặc tự gõ 1-2 câu mở bài dẫn từ đề thi vào khối Lego em chọn)..."
                      className="w-full rounded-lg border border-amber-300 bg-white px-3 py-2 text-xs sm:text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-amber-400"
                    />
                  </div>

                  {/* 2. MIDDLE BODY: LEGO BRICKS DROPZONE */}
                  <div
                    onDragOver={(e) => {
                      e.preventDefault();
                      setIsDragOverTower(true);
                    }}
                    onDragLeave={() => setIsDragOverTower(false)}
                    onDrop={(e) => {
                      e.preventDefault();
                      setIsDragOverTower(false);
                      if (!dragBrickId) return;
                      for (const b of SPK2_LEGO_BLOCKS) {
                        const found = b.stages.find((s) => s.id === dragBrickId);
                        if (found) {
                          addSingleBrickToTower(found);
                          break;
                        }
                      }
                      setDragBrickId(null);
                    }}
                    className={`rounded-xl border-2 border-dashed p-3 transition min-h-[180px] ${
                      isDragOverTower
                        ? 'border-indigo-500 bg-indigo-50/70'
                        : 'border-slate-300 bg-slate-50/70'
                    }`}
                  >
                    <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
                      <span className="text-xs font-extrabold text-slate-700 uppercase">
                        🧱 Tầng 2: Thân Bài Lego & Khe <code className="text-amber-700">...</code> ({towerItems.length} viên gạch • {distinctBlockIds.length} khối)
                      </span>
                      {towerItems.length > 0 ? (
                        <button
                          type="button"
                          onClick={applyPromptSlotsToTower}
                          className="text-[11px] font-bold px-2.5 py-1 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white shadow-2xs transition cursor-pointer"
                        >
                          ✨ Tự điền các khe '...' theo Đề này
                        </button>
                      ) : (
                        <span className="text-[11px] text-slate-500">
                          Kéo thả hoặc bấm + ở cột trái
                        </span>
                      )}
                    </div>

                    {/* Anti-Off-Topic Radar Banner when bricks are on the tower */}
                    {towerItems.length > 0 && towerSlotStats.totalSlots > 0 && (
                      <div
                        className={`mb-2.5 rounded-lg border px-2.5 py-2 text-[11.5px] leading-relaxed flex flex-wrap items-center justify-between gap-2 ${
                          activePrompt.isDirectMatch
                            ? 'bg-sky-50 border-sky-200 text-sky-900'
                            : towerSlotStats.customizedSlots === 0
                            ? 'bg-amber-50 border-amber-300 text-amber-950'
                            : 'bg-emerald-50 border-emerald-300 text-emerald-950'
                        }`}
                      >
                        {activePrompt.isDirectMatch ? (
                          <span>
                            ✅ <b>Đề khớp trực tiếp với khung gốc:</b> Đã tùy biến{' '}
                            <b>
                              {towerSlotStats.customizedSlots}/{towerSlotStats.totalSlots}
                            </b>{' '}
                            khe <code>...</code> (em có thể giữ mặc định hoặc đổi nhẹ chi tiết cá nhân).
                          </span>
                        ) : towerSlotStats.customizedSlots === 0 ? (
                          <span>
                            🛡️ <b>Radar Chống Lạc Đề:</b> Đây là đề bẻ lái! Em đang giữ nguyên{' '}
                            <b>0/{towerSlotStats.totalSlots}</b> khe <code>...</code> mặc định. Hãy sửa ít nhất{' '}
                            <b>2 khe ...</b> bên dưới để gài từ khóa đề bài vào giữa thân bài, tránh bị bắt lỗi học vẹt nhé!
                          </span>
                        ) : (
                          <span>
                            🛡️ <b>Chống Lạc Đề An Toàn:</b> Em đã tùy biến{' '}
                            <b>
                              {towerSlotStats.customizedSlots}/{towerSlotStats.totalSlots}
                            </b>{' '}
                            khe <code>...</code> bám sát đề bài xuyên suốt thân bài!
                          </span>
                        )}
                      </div>
                    )}

                    {towerItems.length === 0 ? (
                      <div className="py-10 text-center text-xs text-slate-400">
                        <div className="text-3xl mb-2">🧩</div>
                        Chưa có khối Lego nào được lắp.<br />
                        Hãy chọn <b>+ Cả khối</b> hoặc kéo từng <b>Stage</b> từ cột bên trái thả vào đây!
                      </div>
                    ) : (
                      <div className="space-y-2.5">
                        {towerItems.map((item, index) => {
                          const blk = getSpk2BlockById(item.brick.blockId);
                          const prevBlockId = index > 0 ? towerItems[index - 1].brick.blockId : null;
                          const isTransition = prevBlockId !== null && prevBlockId !== item.brick.blockId;

                          return (
                            <div key={item.uid} className="space-y-1.5">
                              {/* Connector Bridge if switching to a Plugin / 2nd Block */}
                              {isTransition && (
                                <div className="bg-purple-50 border border-purple-200 rounded-lg p-2">
                                  <div className="flex items-center justify-between gap-2 mb-1">
                                    <span className="text-[11px] font-extrabold text-purple-800">
                                      🔌 Khớp nối chuyển sang khối {blk.name}:
                                    </span>
                                    <select
                                      value=""
                                      onChange={(e) => {
                                        if (e.target.value) updateBridgeText(item.uid, e.target.value);
                                      }}
                                      className="text-[11px] bg-white border border-purple-200 rounded px-1.5 py-0.5 text-purple-900"
                                    >
                                      <option value="">Đổi mẫu câu nối...</option>
                                      {SPK2_CONNECTOR_BRIDGES.map((cb) => (
                                        <option key={cb.id} value={cb.bridgeEn}>
                                          {cb.labelVi}
                                        </option>
                                      ))}
                                    </select>
                                  </div>
                                  <input
                                    type="text"
                                    value={item.bridgeBefore || ''}
                                    onChange={(e) => updateBridgeText(item.uid, e.target.value)}
                                    placeholder="Câu nối mượt sang khối tiếp theo..."
                                    className="w-full bg-white border border-purple-200 rounded px-2.5 py-1 text-xs text-slate-800"
                                  />
                                </div>
                              )}

                              {/* Snapped Lego Brick Card */}
                              <div className={`bg-white rounded-xl border-2 ${blk.borderClass} p-2.5 shadow-sm`}>
                                <div className="flex items-center justify-between gap-2 mb-1">
                                  <div className="flex items-center gap-1.5 min-w-0">
                                    <span
                                      className={`text-[10px] font-extrabold px-2 py-0.5 rounded-full ${blk.badgeBg} ${blk.badgeText}`}
                                    >
                                      {blk.emoji} {blk.code}
                                    </span>
                                    <span className="text-xs font-extrabold text-slate-800 truncate">
                                      {item.brick.stageTitle}
                                    </span>
                                  </div>
                                  <div className="flex items-center gap-1 shrink-0">
                                    <button
                                      type="button"
                                      onClick={() => moveTowerItem(index, -1)}
                                      disabled={index === 0}
                                      className="w-6 h-6 rounded bg-slate-100 hover:bg-slate-200 disabled:opacity-30 text-xs font-bold cursor-pointer"
                                      title="Đẩy lên"
                                    >
                                      ↑
                                    </button>
                                    <button
                                      type="button"
                                      onClick={() => moveTowerItem(index, 1)}
                                      disabled={index === towerItems.length - 1}
                                      className="w-6 h-6 rounded bg-slate-100 hover:bg-slate-200 disabled:opacity-30 text-xs font-bold cursor-pointer"
                                      title="Đẩy xuống"
                                    >
                                      ↓
                                    </button>
                                    <button
                                      type="button"
                                      onClick={() => removeTowerItem(item.uid)}
                                      className="w-6 h-6 rounded bg-red-50 hover:bg-red-100 text-red-600 text-xs font-bold cursor-pointer"
                                      title="Gỡ viên gạch này"
                                    >
                                      ✕
                                    </button>
                                  </div>
                                </div>

                                {brickViewMode === 'keywords' ? (
                                  <div className="flex flex-wrap items-center gap-1">
                                    {item.brick.keywords.map((kw, ki) => (
                                      <React.Fragment key={ki}>
                                        <span className="px-2 py-0.5 rounded-full bg-orange-100 text-orange-800 font-bold text-[11px]">
                                          {kw}
                                        </span>
                                        {ki < item.brick.keywords.length - 1 && (
                                          <span className="text-orange-400 font-bold">➔</span>
                                        )}
                                      </React.Fragment>
                                    ))}
                                  </div>
                                ) : brickViewMode === 'vi' ? (
                                  <p className="text-xs text-emerald-900 leading-relaxed">{item.brick.textVi}</p>
                                ) : (
                                  <p className="text-xs text-slate-700 leading-relaxed">
                                    {renderBrickWithSlotHighlights(item.brick, slotValues, 'tower')}
                                  </p>
                                )}

                                {/* Interactive Adaptive "..." Topic-Anchor Slot Editor */}
                                {item.brick.slots && item.brick.slots.length > 0 && (
                                  <div className="mt-2 pt-2 border-t border-slate-100 space-y-2">
                                    {item.brick.slots.map((sl) => {
                                      const rawVal = slotValues[sl.id];
                                      const isCustomized =
                                        rawVal !== undefined &&
                                        rawVal.trim() !== '' &&
                                        rawVal.trim() !== sl.defaultEn.trim();
                                      const promptSug = activePrompt.slotSuggestions?.[sl.id];

                                      return (
                                        <div
                                          key={sl.id}
                                          className={`rounded-lg p-2 border transition ${
                                            isCustomized
                                              ? 'bg-amber-50/70 border-amber-300'
                                              : 'bg-slate-50/90 border-slate-200'
                                          }`}
                                        >
                                          <div className="flex flex-wrap items-center justify-between gap-1.5 mb-1">
                                            <span className="text-[11px] font-extrabold text-slate-800 flex items-center gap-1">
                                              <span>🎯 {sl.labelVi}</span>
                                              {isCustomized ? (
                                                <span className="text-[10px] px-1.5 py-0.2 rounded bg-emerald-100 text-emerald-800 font-bold">
                                                  Đã bẻ lái ✓
                                                </span>
                                              ) : (
                                                <span className="text-[10px] px-1.5 py-0.2 rounded bg-sky-100 text-sky-800 font-semibold">
                                                  Mặc định gốc
                                                </span>
                                              )}
                                            </span>

                                            <div className="flex items-center gap-1 flex-wrap">
                                              {promptSug && (
                                                <button
                                                  type="button"
                                                  onClick={() => updateSlotValue(sl.id, promptSug)}
                                                  title={`Gợi ý sát đề: "${promptSug}"`}
                                                  className="text-[10.5px] font-bold px-2 py-0.5 rounded bg-indigo-600 hover:bg-indigo-700 text-white transition cursor-pointer"
                                                >
                                                  ✨ Khớp đề này
                                                </button>
                                              )}
                                              {rawVal !== undefined && (
                                                <button
                                                  type="button"
                                                  onClick={() => resetSlotToDefault(sl.id)}
                                                  title={`Khôi phục mặc định gốc: "${sl.defaultEn}"`}
                                                  className="text-[10.5px] font-semibold px-1.5 py-0.5 rounded bg-white border border-slate-300 hover:bg-slate-100 text-slate-600 cursor-pointer"
                                                >
                                                  ↺ Gốc
                                                </button>
                                              )}
                                            </div>
                                          </div>

                                          <input
                                            type="text"
                                            value={rawVal !== undefined ? rawVal : sl.defaultEn}
                                            onChange={(e) => updateSlotValue(sl.id, e.target.value)}
                                            placeholder={sl.hintVi}
                                            className="w-full rounded-md border border-slate-300 bg-white px-2.5 py-1 text-xs text-slate-900 focus:outline-none focus:ring-2 focus:ring-amber-400"
                                          />

                                          {sl.examples && sl.examples.length > 0 && (
                                            <div className="flex flex-wrap items-center gap-1 mt-1.5">
                                              <span className="text-[10px] font-semibold text-slate-400 mr-0.5">
                                                Mẫu nhanh:
                                              </span>
                                              {sl.examples.map((ex, ei) => (
                                                <button
                                                  key={ei}
                                                  type="button"
                                                  onClick={() => updateSlotValue(sl.id, ex.valueEn)}
                                                  title={ex.valueEn}
                                                  className={`text-[10.5px] px-2 py-0.5 rounded-full border transition cursor-pointer ${
                                                    rawVal === ex.valueEn
                                                      ? 'bg-amber-600 text-white border-amber-600 font-bold'
                                                      : 'bg-white hover:bg-amber-50 text-slate-700 border-slate-200'
                                                  }`}
                                                >
                                                  {ex.tagVi}
                                                </button>
                                              ))}
                                            </div>
                                          )}
                                        </div>
                                      );
                                    })}
                                  </div>
                                )}
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    )}
                  </div>

                  {/* 3. BOTTOM BASEPLATE: CLOSING TIE-BACK */}
                  <div className="rounded-xl border-2 border-emerald-300 bg-emerald-50/60 p-3">
                    <div className="flex flex-wrap items-center justify-between gap-2 mb-1.5">
                      <span className="text-xs font-extrabold text-emerald-900 uppercase">
                        🎯 Tầng 3: Câu Chốt Bám Đề (Khóa Chặt Điểm Task Relevance)
                      </span>
                      <button
                        type="button"
                        onClick={() => setClosingText(activePrompt.sampleClosingEn)}
                        className="text-[11px] font-bold px-2.5 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white transition cursor-pointer"
                      >
                        ✨ Điền Câu chốt mẫu
                      </button>
                    </div>
                    <textarea
                      rows={2}
                      value={closingText}
                      onChange={(e) => setClosingText(e.target.value)}
                      placeholder="Viết 1 câu kết nhắc lại đúng từ khóa đề bài để giám khảo thấy bài nói bám sát 100% Cue Card..."
                      className="w-full rounded-lg border border-emerald-300 bg-white px-3 py-1.5 text-xs sm:text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-400"
                    />
                  </div>
                </div>

                {/* Proceed CTA */}
                <div className="pt-3 mt-3 border-t border-slate-100 flex items-center justify-between gap-3">
                  <button
                    type="button"
                    onClick={handleOpenAiSidebar}
                    className="px-3 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition cursor-pointer"
                  >
                    💬 Nhờ AI Tư Vấn Thêm
                  </button>
                  <button
                    type="button"
                    disabled={towerItems.length === 0}
                    onClick={handleProceedToStep2}
                    className="px-5 py-2.5 rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 disabled:opacity-40 disabled:cursor-not-allowed text-white text-xs sm:text-sm font-extrabold shadow-md transition cursor-pointer"
                  >
                    Sang Bước 2: Gọt Mượt & Tập Nói 2 Phút ➔
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* ========================================================= */}
          {/* STEP 2: POLISH SEAMS & 2-MINUTE SPEAK-OUT / RECORDER      */}
          {/* ========================================================= */}
          {step === 2 && (
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-5">
              {/* LEFT 6 COLS: EDITABLE MERGED SCRIPT + GOLDEN PHRASES */}
              <div className="lg:col-span-6 bg-white rounded-2xl border border-slate-200 shadow-sm p-4 flex flex-col">
                <div className="flex items-center justify-between gap-2 pb-3 border-b border-slate-100">
                  <div>
                    <h3 className="text-sm font-extrabold text-slate-900 uppercase">
                      ✍️ Kịch Bản Hoàn Chỉnh (Tự Chỉnh Cho Mượt)
                    </h3>
                    <p className="text-xs text-slate-500">
                      Hãy đổi nhẹ đại từ, mốc thời gian hoặc chi tiết nhỏ để câu Hook ăn khớp 100% với thân bài Lego!
                    </p>
                  </div>
                  <button
                    type="button"
                    onClick={() => setScriptDraft(assembledPreviewText)}
                    className="text-xs font-bold text-indigo-600 hover:text-indigo-800 px-2 py-1 rounded hover:bg-indigo-50 cursor-pointer"
                  >
                    ↺ Khôi phục bản ghép Bước 1
                  </button>
                </div>

                <textarea
                  rows={12}
                  value={scriptDraft}
                  onChange={(e) => setScriptDraft(e.target.value)}
                  className="w-full mt-3 rounded-xl border border-slate-300 bg-slate-50/50 focus:bg-white p-3.5 text-sm text-slate-800 leading-relaxed focus:outline-none focus:ring-2 focus:ring-indigo-500 flex-1"
                />

                {/* Golden Structures Checklist */}
                <div className="mt-3 bg-indigo-50/70 border border-indigo-100 rounded-xl p-3">
                  <div className="text-xs font-extrabold text-indigo-950 mb-1.5">
                    🏆 Checklist Cấu Trúc Ăn Điểm Band 7.5+ Trong Kịch Bản Của Em:
                  </div>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-1.5">
                    {detectedGoldenPhrases.map((gp, idx) => (
                      <div
                        key={idx}
                        className={`text-[11.5px] px-2.5 py-1 rounded-lg font-semibold flex items-center gap-1.5 ${
                          gp.matched
                            ? 'bg-emerald-100 text-emerald-900'
                            : 'bg-white text-slate-500 border border-slate-200'
                        }`}
                      >
                        <span>{gp.matched ? '✅' : '⬜'}</span>
                        <span className="truncate">{gp.label}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              {/* RIGHT 6 COLS: 2-MINUTE SPEAKING BOOTH & KEYWORD TELEPROMPTER */}
              <div className="lg:col-span-6 bg-white rounded-2xl border border-slate-200 shadow-sm p-4 flex flex-col">
                <div className="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-slate-100">
                  <div>
                    <h3 className="text-sm font-extrabold text-slate-900 uppercase">
                      🎙️ Phòng Luyện Nói Phản Xạ 2 Phút
                    </h3>
                    <p className="text-xs text-slate-500">
                      Tập nói to theo <b>Chuỗi Keyword</b> để nhớ sâu vào não (không học vẹt) và thu âm để AI chấm!
                    </p>
                  </div>

                  <button
                    type="button"
                    onClick={handleToggleTts}
                    className={`px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
                      isPlayingTts
                        ? 'bg-rose-600 text-white'
                        : 'bg-sky-100 hover:bg-sky-200 text-sky-900'
                    }`}
                  >
                    {isPlayingTts ? '⏹ Dừng giọng mẫu' : '🔊 Nghe giọng mẫu Anh-Anh'}
                  </button>
                </div>

                {/* Timer + Mic Recorder Bar */}
                <div className="my-3 bg-slate-900 text-white rounded-xl p-3.5 flex flex-wrap items-center justify-between gap-3">
                  <div className="flex items-center gap-3">
                    <div className="text-2xl font-black font-mono text-amber-400 tabular-nums">
                      ⏱ {formatSeconds(practiceSecondsLeft)}
                    </div>
                    <div className="flex gap-1.5">
                      <button
                        type="button"
                        onClick={() => setIsTimerRunning((r) => !r)}
                        className="px-2.5 py-1 rounded-lg bg-white/15 hover:bg-white/25 text-xs font-bold cursor-pointer"
                      >
                        {isTimerRunning ? 'Tạm dừng' : 'Đếm ngược 2p'}
                      </button>
                      <button
                        type="button"
                        onClick={() => {
                          setIsTimerRunning(false);
                          setPracticeSecondsLeft(120);
                        }}
                        className="px-2 py-1 rounded-lg bg-white/10 hover:bg-white/20 text-xs cursor-pointer"
                      >
                        Reset
                      </button>
                    </div>
                  </div>

                  {/* Mic Recording Button */}
                  <div className="flex items-center gap-2">
                    {!isRecording ? (
                      <button
                        type="button"
                        onClick={handleStartRecording}
                        className="px-3.5 py-1.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white text-xs font-extrabold flex items-center gap-1.5 shadow cursor-pointer"
                      >
                        🎙️ {recordedAudioUrl ? 'Thu âm lại (2 phút)' : 'Bấm Thu Âm Tập Nói'}
                      </button>
                    ) : (
                      <button
                        type="button"
                        onClick={handleStopRecording}
                        className="px-3.5 py-1.5 rounded-xl bg-amber-400 text-slate-950 text-xs font-extrabold flex items-center gap-1.5 animate-pulse cursor-pointer"
                      >
                        ⏹ Dừng thu ({formatSeconds(recordSeconds)})
                      </button>
                    )}
                  </div>
                </div>

                {recordedAudioUrl && (
                  <div className="mb-3 bg-emerald-50 border border-emerald-200 rounded-xl p-2.5 flex flex-wrap items-center justify-between gap-2">
                    <span className="text-xs font-bold text-emerald-900">
                      ✅ Đã thu âm bản nói ({formatSeconds(recordSeconds)}) — Nghe lại hoặc gửi AI chấm phát âm:
                    </span>
                    <audio controls src={recordedAudioUrl} className="h-8 max-w-[260px]" />
                  </div>
                )}

                {/* Teleprompter Mode Tabs */}
                <div className="flex gap-1.5 mb-2.5">
                  <button
                    type="button"
                    onClick={() => setTeleprompterMode('keywords')}
                    className={`px-3 py-1.5 rounded-lg text-xs font-bold cursor-pointer ${
                      teleprompterMode === 'keywords'
                        ? 'bg-orange-600 text-white'
                        : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                    }`}
                  >
                    🔑 Nhìn Chuỗi Keyword (Speak Out)
                  </button>
                  <button
                    type="button"
                    onClick={() => setTeleprompterMode('vi')}
                    className={`px-3 py-1.5 rounded-lg text-xs font-bold cursor-pointer ${
                      teleprompterMode === 'vi'
                        ? 'bg-emerald-600 text-white'
                        : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                    }`}
                  >
                    🇻🇳 Nhìn Tiếng Việt Dịch Ngược
                  </button>
                  <button
                    type="button"
                    onClick={() => setTeleprompterMode('full')}
                    className={`px-3 py-1.5 rounded-lg text-xs font-bold cursor-pointer ${
                      teleprompterMode === 'full'
                        ? 'bg-indigo-600 text-white'
                        : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                    }`}
                  >
                    📖 Hiện Full Script
                  </button>
                </div>

                {/* Teleprompter Screen */}
                <div className="flex-1 bg-amber-50/50 border border-amber-200 rounded-xl p-3.5 overflow-y-auto max-h-[300px] space-y-2.5">
                  {teleprompterMode === 'keywords' && (
                    <>
                      {hookText.trim() && (
                        <div className="bg-white rounded-lg p-2.5 border border-amber-200">
                          <div className="text-[11px] font-extrabold text-amber-800 uppercase mb-0.5">
                            🔗 Mở bài (Hook Bẻ Lái):
                          </div>
                          <div className="text-xs text-slate-800 font-semibold">{hookText}</div>
                        </div>
                      )}
                      {towerItems.map((it) => {
                        const blk = getSpk2BlockById(it.brick.blockId);
                        const customStageSlots = (it.brick.slots || []).filter((sl) => {
                          const v = slotValues[sl.id];
                          return v !== undefined && v.trim() !== '' && v.trim() !== sl.defaultEn.trim();
                        });
                        return (
                          <div key={it.uid} className="bg-white rounded-lg p-2.5 border border-orange-200">
                            <div className="text-[11px] font-extrabold text-orange-800 mb-1">
                              {blk.emoji} {blk.name} — {it.brick.stageTitle}
                            </div>
                            <div className="flex flex-wrap items-center gap-1.5">
                              {it.brick.keywords.map((kw, ki) => (
                                <React.Fragment key={ki}>
                                  <span className="px-2.5 py-0.5 rounded-full bg-orange-100 text-orange-900 font-bold text-xs">
                                    {kw}
                                  </span>
                                  {ki < it.brick.keywords.length - 1 && (
                                    <span className="text-orange-400 font-bold">➔</span>
                                  )}
                                </React.Fragment>
                              ))}
                            </div>
                            {customStageSlots.length > 0 && (
                              <div className="mt-1.5 pt-1.5 border-t border-amber-100 space-y-1">
                                {customStageSlots.map((sl) => (
                                  <div
                                    key={sl.id}
                                    className="text-[11.5px] px-2 py-0.5 rounded bg-amber-50 border border-amber-200 text-amber-950 font-semibold"
                                  >
                                    🎯 <b>Khe '...' bám đề:</b> {slotValues[sl.id]}
                                  </div>
                                ))}
                              </div>
                            )}
                          </div>
                        );
                      })}
                      {closingText.trim() && (
                        <div className="bg-white rounded-lg p-2.5 border border-emerald-200">
                          <div className="text-[11px] font-extrabold text-emerald-800 uppercase mb-0.5">
                            🎯 Câu chốt bám đề:
                          </div>
                          <div className="text-xs text-slate-800 font-semibold">{closingText}</div>
                        </div>
                      )}
                    </>
                  )}

                  {teleprompterMode === 'vi' && (
                    <div className="space-y-2">
                      {hookText.trim() && (
                        <div className="p-2.5 rounded-lg bg-white border border-amber-200 text-xs">
                          <b className="text-amber-800">Hook mở bài:</b> {hookText}
                        </div>
                      )}
                      {towerItems.map((it) => (
                        <div key={it.uid} className="p-2.5 rounded-lg bg-white border border-emerald-200 text-xs text-slate-800 leading-relaxed">
                          <b className="text-emerald-700">{it.brick.stageTitle}:</b> {it.brick.textVi}
                        </div>
                      ))}
                      {closingText.trim() && (
                        <div className="p-2.5 rounded-lg bg-white border border-emerald-200 text-xs">
                          <b className="text-emerald-800">Câu chốt:</b> {closingText}
                        </div>
                      )}
                    </div>
                  )}

                  {teleprompterMode === 'full' && (
                    <div className="text-sm text-slate-800 whitespace-pre-line leading-relaxed bg-white p-3 rounded-lg border border-slate-200">
                      {scriptDraft}
                    </div>
                  )}
                </div>

                {/* Bottom Actions */}
                <div className="pt-3 mt-3 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2">
                  <button
                    type="button"
                    onClick={() => setStep(1)}
                    className="px-3 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold cursor-pointer"
                  >
                    ← Quay lại Lắp Lego
                  </button>

                  <div className="flex flex-wrap items-center gap-2">
                    <button
                      type="button"
                      onClick={() => handleGradeWithAI(false)}
                      className="px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-extrabold shadow transition cursor-pointer"
                    >
                      🤖 Chấm Kịch Bản Lego
                    </button>
                    {recordedBase64 && (
                      <button
                        type="button"
                        onClick={() => handleGradeWithAI(true)}
                        className="px-4 py-2.5 rounded-xl bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-700 hover:to-amber-700 text-white text-xs font-extrabold shadow transition cursor-pointer"
                      >
                        🎙️ Chấm Cả Giọng Nói + Kịch Bản
                      </button>
                    )}
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* ========================================================= */}
          {/* STEP 3: AI LEGO COACH & EXAMINER FEEDBACK                 */}
          {/* ========================================================= */}
          {step === 3 && (
            <div className="space-y-4">
              {isGrading && (
                <div className="bg-white rounded-2xl border border-slate-200 p-10 text-center shadow-sm">
                  <div className="inline-block w-12 h-12 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mb-3" />
                  <h3 className="text-base font-extrabold text-slate-900">
                    Giám khảo AI đang phân tích pha "Bẻ lái" Hook & các Khối Lego của em...
                  </h3>
                  <p className="text-xs text-slate-500 mt-1">
                    Đang kiểm tra độ bám đề Cue Card, mối nối ngữ pháp và các cấu trúc ăn điểm Band 7.5+...
                  </p>
                </div>
              )}

              {gradeError && (
                <div className="bg-red-50 border border-red-200 rounded-2xl p-5 text-center">
                  <p className="text-sm font-bold text-red-700 mb-3">⚠️ {gradeError}</p>
                  <button
                    type="button"
                    onClick={() => handleGradeWithAI(Boolean(recordedBase64))}
                    className="px-4 py-2 rounded-xl bg-red-600 hover:bg-red-700 text-white text-xs font-bold cursor-pointer"
                  >
                    Thử chấm lại ngay
                  </button>
                </div>
              )}

              {!isGrading && !gradeError && !aiEvaluation && (
                <div className="bg-white rounded-2xl border border-slate-200 p-8 text-center">
                  <p className="text-sm text-slate-600 mb-4">
                    Em đã sẵn sàng nộp kịch bản (hoặc bản thu âm) để Giám khảo AI của TonyEnglish chấm điểm!
                  </p>
                  <div className="flex justify-center gap-3">
                    <button
                      type="button"
                      onClick={() => handleGradeWithAI(false)}
                      className="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-extrabold shadow cursor-pointer"
                    >
                      🤖 Bấm Chấm Kịch Bản Ngay
                    </button>
                    {recordedBase64 && (
                      <button
                        type="button"
                        onClick={() => handleGradeWithAI(true)}
                        className="px-5 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-700 text-white text-sm font-extrabold shadow cursor-pointer"
                      >
                        🎙️ Chấm Giọng Thu Âm + Kịch Bản
                      </button>
                    )}
                  </div>
                </div>
              )}

              {aiEvaluation && (
                <div className="space-y-4">
                  {/* Top Band Banner + Live Call CTA */}
                  <div className="bg-gradient-to-r from-indigo-900 via-purple-900 to-slate-900 text-white rounded-2xl p-5 flex flex-wrap items-center justify-between gap-4 shadow-lg">
                    <div className="flex items-center gap-4">
                      <div className="w-20 h-20 rounded-2xl bg-amber-400 text-slate-950 flex flex-col items-center justify-center shadow-lg shrink-0">
                        <span className="text-[10px] font-extrabold uppercase">Band</span>
                        <span className="text-3xl font-black leading-none">{aiEvaluation.overall}</span>
                      </div>
                      <div>
                        <div className="text-xs font-bold text-amber-300 uppercase tracking-wider">
                          Kết Quả Đánh Giá Kịch Bản & Phản Xạ Lego
                        </div>
                        <p className="text-sm text-indigo-100 mt-1 max-w-2xl leading-relaxed">
                          {aiEvaluation.generalFeedback}
                        </p>
                      </div>
                    </div>

                    <button
                      type="button"
                      onClick={handleLaunchLiveExaminer}
                      className="px-4 py-3 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs sm:text-sm font-extrabold shadow-lg transition cursor-pointer"
                    >
                      📞 Vào Thi Thật Live 1-1 Đề Này Ngay!
                    </button>
                  </div>

                  {/* Recognized Audio Transcript if Audio was submitted */}
                  {aiEvaluation.recognizedTranscript && (
                    <div className="bg-rose-50/70 border border-rose-200 rounded-2xl p-4">
                      <h4 className="text-xs font-extrabold text-rose-900 uppercase mb-1">
                        🎙️ Lời Thoại AI Nghe Được Từ Bản Thu Âm Của Em:
                      </h4>
                      <p className="text-sm text-slate-800 italic leading-relaxed">
                        "{aiEvaluation.recognizedTranscript}"
                      </p>
                    </div>
                  )}

                  {/* 3 Tactical Lego Checks */}
                  {aiEvaluation.legoReview && (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                      <div className="bg-white rounded-xl border border-amber-200 p-3.5">
                        <div className="text-xs font-extrabold text-amber-800 uppercase mb-1">
                          🔗 1. Độ Mượt Pha Bẻ Lái (Hook)
                        </div>
                        <p className="text-xs text-slate-700 leading-relaxed">
                          {aiEvaluation.legoReview.hookSteeringCheck}
                        </p>
                      </div>
                      <div className="bg-white rounded-xl border border-indigo-200 p-3.5">
                        <div className="text-xs font-extrabold text-indigo-800 uppercase mb-1">
                          🧱 2. Tổ Hợp Lego & Cấu Trúc Vàng
                        </div>
                        <p className="text-xs text-slate-700 leading-relaxed">
                          {aiEvaluation.legoReview.legoComboCheck}
                        </p>
                      </div>
                      <div className="bg-white rounded-xl border border-emerald-200 p-3.5">
                        <div className="text-xs font-extrabold text-emerald-800 uppercase mb-1">
                          🎯 3. Độ Bám Đề Cue Card
                        </div>
                        <p className="text-xs text-slate-700 leading-relaxed">
                          {aiEvaluation.legoReview.cueCardCheck}
                        </p>
                      </div>
                    </div>
                  )}

                  {/* 4 IELTS Speaking Criteria */}
                  {aiEvaluation.criteria && aiEvaluation.criteria.length > 0 && (
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
                      {aiEvaluation.criteria.map((c, idx) => (
                        <div key={idx} className="bg-white rounded-xl border border-slate-200 p-3.5">
                          <div className="flex items-center justify-between mb-1">
                            <span className="text-xs font-extrabold text-slate-800">{c.name}</span>
                            <span className="px-2 py-0.5 rounded-md bg-indigo-100 text-indigo-900 font-black text-xs">
                              {c.score}
                            </span>
                          </div>
                          <p className="text-xs text-slate-600 leading-relaxed">{c.comment}</p>
                        </div>
                      ))}
                    </div>
                  )}

                  {/* Side-by-side: Red/Green Seam Corrections + Band 8.0+ Natural Lego Script */}
                  <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    {aiEvaluation.correctedHtml && (
                      <div className="bg-white rounded-2xl border border-slate-200 p-4">
                        <h4 className="text-xs font-extrabold text-slate-900 uppercase mb-2">
                          🖍️ Sửa Chi Tiết Các Mối Nối (Đỏ = Chưa Mượt • Xanh = Sửa Chuẩn)
                        </h4>
                        <div
                          className="text-sm text-slate-800 leading-relaxed"
                          dangerouslySetInnerHTML={{ __html: aiEvaluation.correctedHtml }}
                        />
                      </div>
                    )}

                    {aiEvaluation.upgradedScript && (
                      <div className="bg-emerald-50/60 rounded-2xl border border-emerald-200 p-4 flex flex-col">
                        <div className="flex items-center justify-between gap-2 mb-2">
                          <h4 className="text-xs font-extrabold text-emerald-900 uppercase">
                            🌟 Bản Nâng Cấp Mượt Band 8.0+ (Giữ Nguyên Khối Lego Của Em)
                          </h4>
                          <button
                            type="button"
                            onClick={() => {
                              setScriptDraft(aiEvaluation.upgradedScript || '');
                              setStep(2);
                            }}
                            className="text-[11px] font-bold px-2.5 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white cursor-pointer"
                          >
                            📥 Chép sang Bước 2 để Tập Nói
                          </button>
                        </div>
                        <p className="text-sm text-slate-800 whitespace-pre-line leading-relaxed flex-1">
                          {aiEvaluation.upgradedScript}
                        </p>
                      </div>
                    )}
                  </div>

                  <div className="flex justify-between items-center pt-2">
                    <button
                      type="button"
                      onClick={() => setStep(2)}
                      className="px-4 py-2 rounded-xl bg-white border border-slate-300 hover:bg-slate-50 text-xs font-bold text-slate-700 cursor-pointer"
                    >
                      ← Quay lại chỉnh sửa & thu âm lại
                    </button>
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
