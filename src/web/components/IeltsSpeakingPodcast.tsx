import React, { useState, useEffect, useRef, useCallback } from 'react';

export interface OrangePhraseItem {
  en: string;
  vi: string;
}

export interface PodcastSentenceItem {
  id: number;
  en: string;
  enHtml: string;
  vi: string;
  orangePhrases: OrangePhraseItem[];
  enAudioUrl?: string;
  viAudioUrl?: string;
}

export interface PodcastSectionItem {
  sectionIndex: number;
  sectionTitle: string;
  partType: string;
  questionEn: string;
  questionVi: string;
  sentences: PodcastSentenceItem[];
}

export interface OrangeVocabItem {
  en: string;
  vi: string;
  exampleEn: string;
  exampleEnHtml: string;
  exampleVi: string;
  sentenceIndex: number;
  enAudioUrl?: string;
  viAudioUrl?: string;
}

export interface ArticlePodcastData {
  newsId: number;
  title: string;
  categoryId: number;
  sentenceCount: number;
  orangeCount: number;
  sections: PodcastSectionItem[];
  orangeVocab: OrangeVocabItem[];
}

type PracticeMode = 'shadowing' | 'reflex' | 'orange_drill';
type PlaybackPhase =
  | 'idle'
  | 'playing_en'
  | 'pause_shadow'
  | 'playing_vi'
  | 'pause_reflex'
  | 'playing_en_answer'
  | 'pause_absorb'
  | 'playing_orange_vi'
  | 'pause_orange_recall'
  | 'playing_orange_en'
  | 'playing_orange_example';

interface Props {
  newsId: number;
}

let cachedPodcastMap: Record<string, ArticlePodcastData> | null = null;

export const IeltsSpeakingPodcast: React.FC<Props> = ({ newsId }) => {
  const [data, setData] = useState<ArticlePodcastData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [mode, setMode] = useState<PracticeMode>('shadowing');
  const [selectedSectionIdx, setSelectedSectionIdx] = useState<number>(0); // 0 = All sections

  // Playback state
  const [isPlaying, setIsPlaying] = useState<boolean>(false);
  const [activeItemIdx, setActiveItemIdx] = useState<number>(0);
  const [phase, setPhase] = useState<PlaybackPhase>('idle');
  const [countdownSec, setCountdownSec] = useState<number>(0);
  const [playbackRate, setPlaybackRate] = useState<number>(1.0);
  const [pauseBonusSec, setPauseBonusSec] = useState<number>(2); // Extra pause seconds

  // UI toggles for Reflex & Orange Drill modes
  const [hideReflexEnAll, setHideReflexEnAll] = useState<boolean>(true);
  const [revealedReflexIds, setRevealedReflexIds] = useState<Record<number, boolean>>({});
  const [hideOrangeHintInReflex, setHideOrangeHintInReflex] = useState<boolean>(false);
  const [hideOrangeEnInDrill, setHideOrangeEnInDrill] = useState<boolean>(false);
  const [revealedOrangeDrillIdx, setRevealedOrangeDrillIdx] = useState<Record<number, boolean>>({});

  // Refs for async podcast loop control
  const runIdRef = useRef<number>(0);
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const countdownTimerRef = useRef<number | null>(null);
  const cardRefs = useRef<Record<number, HTMLDivElement | null>>({});

  // Load podcast dataset
  useEffect(() => {
    let mounted = true;
    const load = async () => {
      try {
        setLoading(true);
        if (!cachedPodcastMap) {
          const resp = await fetch('/data/ielts_speaking_podcasts.json');
          if (resp.ok) {
            cachedPodcastMap = await resp.json();
          }
        }
        if (mounted && cachedPodcastMap) {
          setData(cachedPodcastMap[String(newsId)] || null);
        }
      } catch (e) {
        console.error('Failed to load IELTS speaking podcast data:', e);
      } finally {
        if (mounted) setLoading(false);
      }
    };
    load();
    return () => {
      mounted = false;
    };
  }, [newsId]);

  const stopAllPlayback = useCallback(() => {
    runIdRef.current += 1;
    setIsPlaying(false);
    setPhase('idle');
    setCountdownSec(0);
    if (countdownTimerRef.current) {
      window.clearInterval(countdownTimerRef.current);
      countdownTimerRef.current = null;
    }
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.onended = null;
      audioRef.current.onerror = null;
      audioRef.current = null;
    }
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
  }, []);

  // Stop playback when article, mode, or section changes, or on unmount
  useEffect(() => {
    stopAllPlayback();
    setActiveItemIdx(0);
  }, [newsId, mode, selectedSectionIdx, stopAllPlayback]);

  useEffect(() => {
    return () => {
      stopAllPlayback();
    };
  }, [stopAllPlayback]);

  // Flatten sentences for current section filter
  const activeSentences: Array<PodcastSentenceItem & { sectionTitle: string; questionEn: string; questionVi: string; isFirstInSection: boolean }> = React.useMemo(() => {
    if (!data) return [];
    const list: Array<PodcastSentenceItem & { sectionTitle: string; questionEn: string; questionVi: string; isFirstInSection: boolean }> = [];
    for (const sec of data.sections) {
      if (selectedSectionIdx !== 0 && sec.sectionIndex !== selectedSectionIdx) continue;
      sec.sentences.forEach((s, idx) => {
        list.push({
          ...s,
          sectionTitle: sec.sectionTitle,
          questionEn: sec.questionEn,
          questionVi: sec.questionVi,
          isFirstInSection: idx === 0,
        });
      });
    }
    return list;
  }, [data, selectedSectionIdx]);

  // Speak helper returning a Promise that resolves when speech/audio finishes
  const speakTextAsync = useCallback(
    (text: string, langCode: 'en' | 'vi', mp3Url: string | undefined, currentRunId: number): Promise<void> => {
      return new Promise((resolve) => {
        if (runIdRef.current !== currentRunId) {
          resolve();
          return;
        }

        const cleanText = text.replace(/\s+/g, ' ').trim();
        if (!cleanText) {
          resolve();
          return;
        }

        // Helper to play via HTMLAudioElement (either static MP3 or Google TTS stream)
        const playViaAudioUrl = (url: string, onFailFallback?: () => void) => {
          if (runIdRef.current !== currentRunId) {
            resolve();
            return;
          }
          const audio = document.createElement('audio');
          audio.setAttribute('referrerpolicy', 'no-referrer');
          audio.src = url;
          audio.playbackRate = playbackRate;
          audioRef.current = audio;
          let settled = false;
          const finish = () => {
            if (!settled) {
              settled = true;
              resolve();
            }
          };
          audio.onended = finish;
          audio.onerror = () => {
            if (!settled) {
              settled = true;
              if (onFailFallback) onFailFallback();
              else resolve();
            }
          };
          audio.play().catch(() => {
            if (!settled) {
              settled = true;
              if (onFailFallback) onFailFallback();
              else resolve();
            }
          });
        };

        // Helper to play via Web Speech API
        const playViaWebSpeech = (onFailFallback?: () => void) => {
          if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
            if (onFailFallback) onFailFallback();
            else resolve();
            return;
          }
          const synth = window.speechSynthesis;
          synth.cancel();
          const voices = synth.getVoices();
          const targetPrefix = langCode === 'vi' ? 'vi' : 'en';
          const matchingVoices = voices.filter((v) => v.lang.toLowerCase().startsWith(targetPrefix));

          // If Vietnamese is requested and the device has no vi-VN voice installed, use Google TTS stream first
          if (langCode === 'vi' && matchingVoices.length === 0 && onFailFallback) {
            onFailFallback();
            return;
          }

          const utter = new SpeechSynthesisUtterance(cleanText);
          utter.lang = langCode === 'vi' ? 'vi-VN' : 'en-GB';
          utter.rate = playbackRate;
          if (matchingVoices.length > 0) {
            // Prefer Google/Microsoft neural voices if available
            const preferred =
              matchingVoices.find((v) => /natural|neural|google|hoaimy|namminh|sonia|ryan/i.test(v.name)) ||
              matchingVoices[0];
            utter.voice = preferred;
          }

          let settled = false;
          const wordCount = cleanText.split(/\s+/).length;
          const timeoutMs = Math.max(4000, Math.min(25000, wordCount * 650));
          const safetyTimer = window.setTimeout(() => {
            if (!settled) {
              settled = true;
              resolve();
            }
          }, timeoutMs);

          utter.onend = () => {
            if (!settled) {
              settled = true;
              window.clearTimeout(safetyTimer);
              resolve();
            }
          };
          utter.onerror = () => {
            if (!settled) {
              settled = true;
              window.clearTimeout(safetyTimer);
              if (onFailFallback) onFailFallback();
              else resolve();
            }
          };
          synth.speak(utter);
        };

        // Google Translate TTS stream URL (chunked to <=180 chars at word/clause boundaries)
        const playViaGoogleTts = () => {
          const tl = langCode === 'vi' ? 'vi' : 'en';
          const words = cleanText.split(' ');
          const chunks: string[] = [];
          let cur = '';
          for (const w of words) {
            if ((cur + ' ' + w).trim().length > 180) {
              if (cur) chunks.push(cur.trim());
              cur = w;
            } else {
              cur = (cur + ' ' + w).trim();
            }
          }
          if (cur) chunks.push(cur.trim());

          let idx = 0;
          const playNextChunk = () => {
            if (runIdRef.current !== currentRunId || idx >= chunks.length) {
              resolve();
              return;
            }
            const gUrl = `https://translate.googleapis.com/translate_tts?ie=UTF-8&client=tw-ob&tl=${tl}&q=${encodeURIComponent(chunks[idx])}`;
            idx += 1;
            const audio = document.createElement('audio');
            audio.setAttribute('referrerpolicy', 'no-referrer');
            audio.src = gUrl;
            audio.playbackRate = playbackRate;
            audioRef.current = audio;
            audio.onended = () => playNextChunk();
            audio.onerror = () => playViaWebSpeech();
            audio.play().catch(() => playViaWebSpeech());
          };
          playNextChunk();
        };

        if (mp3Url) {
          playViaAudioUrl(mp3Url, () => playViaWebSpeech(() => playViaGoogleTts()));
        } else {
          playViaWebSpeech(() => playViaGoogleTts());
        }
      });
    },
    [playbackRate]
  );

  // Countdown pause helper returning a Promise
  const waitCountdownAsync = useCallback((seconds: number, currentRunId: number): Promise<void> => {
    return new Promise((resolve) => {
      if (runIdRef.current !== currentRunId || seconds <= 0) {
        setCountdownSec(0);
        resolve();
        return;
      }
      let remaining = Math.round(seconds * 10) / 10;
      setCountdownSec(Math.ceil(remaining));

      if (countdownTimerRef.current) {
        window.clearInterval(countdownTimerRef.current);
      }

      countdownTimerRef.current = window.setInterval(() => {
        if (runIdRef.current !== currentRunId) {
          if (countdownTimerRef.current) window.clearInterval(countdownTimerRef.current);
          countdownTimerRef.current = null;
          setCountdownSec(0);
          resolve();
          return;
        }
        remaining -= 0.25;
        if (remaining <= 0) {
          if (countdownTimerRef.current) window.clearInterval(countdownTimerRef.current);
          countdownTimerRef.current = null;
          setCountdownSec(0);
          resolve();
        } else {
          setCountdownSec(Math.ceil(remaining));
        }
      }, 250);
    });
  }, []);

  // Scroll active card into view smoothly during podcast playback
  const scrollToCard = (key: number) => {
    const el = cardRefs.current[key];
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  };

  // Start continuous Podcast loop from startIndex
  const startPodcastFrom = useCallback(
    async (startIndex: number) => {
      if (!data) return;
      stopAllPlayback();
      const myRunId = runIdRef.current + 1;
      runIdRef.current = myRunId;
      setIsPlaying(true);

      if (mode === 'shadowing') {
        for (let i = startIndex; i < activeSentences.length; i++) {
          if (runIdRef.current !== myRunId) break;
          const item = activeSentences[i];
          setActiveItemIdx(i);
          scrollToCard(item.id);

          // 1. Play English sentence
          setPhase('playing_en');
          await speakTextAsync(item.en, 'en', item.enAudioUrl, myRunId);
          if (runIdRef.current !== myRunId) break;

          // 2. Pause for student to shadow aloud
          const words = item.en.split(/\s+/).length;
          const shadowPause = Math.max(3, Math.min(10, Math.round(words * 0.38) + pauseBonusSec));
          setPhase('pause_shadow');
          await waitCountdownAsync(shadowPause, myRunId);
        }
      } else if (mode === 'reflex') {
        for (let i = startIndex; i < activeSentences.length; i++) {
          if (runIdRef.current !== myRunId) break;
          const item = activeSentences[i];
          setActiveItemIdx(i);
          scrollToCard(item.id);

          // 1. Play Vietnamese prompt
          setPhase('playing_vi');
          await speakTextAsync(item.vi, 'vi', item.viAudioUrl, myRunId);
          if (runIdRef.current !== myRunId) break;

          // 2. Pause for student to translate aloud into English using the orange phrases
          const words = item.en.split(/\s+/).length;
          const reflexPause = Math.max(3.5, Math.min(12, Math.round(words * 0.42) + pauseBonusSec));
          setPhase('pause_reflex');
          await waitCountdownAsync(reflexPause, myRunId);
          if (runIdRef.current !== myRunId) break;

          // 3. Reveal English sentence and play native English answer
          setRevealedReflexIds((prev) => ({ ...prev, [item.id]: true }));
          setPhase('playing_en_answer');
          await speakTextAsync(item.en, 'en', item.enAudioUrl, myRunId);
          if (runIdRef.current !== myRunId) break;

          // 4. Short absorb pause before next sentence
          setPhase('pause_absorb');
          await waitCountdownAsync(2, myRunId);
        }
      } else if (mode === 'orange_drill') {
        const vocabList = data.orangeVocab;
        for (let i = startIndex; i < vocabList.length; i++) {
          if (runIdRef.current !== myRunId) break;
          const vItem = vocabList[i];
          setActiveItemIdx(i);
          scrollToCard(10000 + i);

          // 1. Play Vietnamese meaning of the orange phrase
          setPhase('playing_orange_vi');
          await speakTextAsync(vItem.vi, 'vi', vItem.viAudioUrl, myRunId);
          if (runIdRef.current !== myRunId) break;

          // 2. Pause for student to recall & speak the orange English expression
          setPhase('pause_orange_recall');
          await waitCountdownAsync(Math.max(2.5, pauseBonusSec + 1.5), myRunId);
          if (runIdRef.current !== myRunId) break;

          // 3. Reveal & play the English orange expression
          setRevealedOrangeDrillIdx((prev) => ({ ...prev, [i]: true }));
          setPhase('playing_orange_en');
          await speakTextAsync(vItem.en, 'en', vItem.enAudioUrl, myRunId);
          if (runIdRef.current !== myRunId) break;

          await waitCountdownAsync(1, myRunId);
          if (runIdRef.current !== myRunId) break;

          // 4. Play the example sentence in context + pause to shadow
          setPhase('playing_orange_example');
          await speakTextAsync(vItem.exampleEn, 'en', undefined, myRunId);
          if (runIdRef.current !== myRunId) break;

          setPhase('pause_shadow');
          const exWords = vItem.exampleEn.split(/\s+/).length;
          await waitCountdownAsync(Math.max(3, Math.min(8, Math.round(exWords * 0.35) + 1)), myRunId);
        }
      }

      if (runIdRef.current === myRunId) {
        setIsPlaying(false);
        setPhase('idle');
        setCountdownSec(0);
      }
    },
    [data, mode, activeSentences, pauseBonusSec, speakTextAsync, stopAllPlayback, waitCountdownAsync]
  );

  // Play a single phrase or sentence on click without starting the full podcast loop
  const playSingleSnippet = useCallback(
    async (text: string, langCode: 'en' | 'vi', mp3Url?: string) => {
      stopAllPlayback();
      const myRunId = runIdRef.current + 1;
      runIdRef.current = myRunId;
      setPhase(langCode === 'en' ? 'playing_en' : 'playing_vi');
      await speakTextAsync(text, langCode, mp3Url, myRunId);
      if (runIdRef.current === myRunId) {
        setPhase('idle');
      }
    },
    [speakTextAsync, stopAllPlayback]
  );

  if (loading) {
    return (
      <div className="my-6 p-6 rounded-2xl bg-slate-50 border border-slate-200 text-center text-slate-500 font-semibold text-sm">
        ⏳ Đang tải Podcast luyện nói IELTS & Cụm từ màu da cam...
      </div>
    );
  }

  if (!data || data.sentenceCount === 0) {
    return null;
  }

  const totalItemsInCurrentMode = mode === 'orange_drill' ? data.orangeVocab.length : activeSentences.length;

  const getPhaseBannerText = () => {
    switch (phase) {
      case 'playing_en':
        return '🔊 Đang phát câu Tiếng Anh mẫu — Hãy lắng nghe ngữ điệu & cách nhấn cụm từ da cam!';
      case 'pause_shadow':
        return `🎙️ TỚI LƯỢT BẠN NÓI NHẠI! Hãy đọc to câu trên và nhấn mạnh cụm từ màu da cam (${countdownSec}s)...`;
      case 'playing_vi':
        return '🇻🇳 Đang đọc câu Tiếng Việt — Hãy chuẩn bị dịch sang Tiếng Anh!';
      case 'pause_reflex':
        return `⚡ PHẢN XẠ DỊCH VIỆT - ANH! Hãy nói to câu Tiếng Anh có dùng cụm từ da cam (${countdownSec}s)...`;
      case 'playing_en_answer':
        return '🇬🇧 Đáp án câu Tiếng Anh mẫu — Hãy đối chiếu với câu bạn vừa dịch!';
      case 'pause_absorb':
        return `✨ Nghỉ chuyển câu (${countdownSec}s)...`;
      case 'playing_orange_vi':
        return '🇻🇳 Nghe nghĩa Tiếng Việt của cụm từ màu da cam...';
      case 'pause_orange_recall':
        return `🍊 HÃY BẬT RA CỤM TỪ MÀU DA CAM BẰNG TIẾNG ANH! (${countdownSec}s)...`;
      case 'playing_orange_en':
        return '🇬🇧 Đáp án cụm từ văn nói màu da cam!';
      case 'playing_orange_example':
        return '📖 Nghe câu ví dụ áp dụng cụm từ màu da cam trong bài nói mẫu...';
      default:
        return 'Bấm "▶ Phát Podcast" để luyện tự động toàn bài hoặc bấm vào từng câu / cụm từ da cam bên dưới.';
    }
  };

  return (
    <div className="my-6 rounded-3xl border-2 border-[#0a5482]/15 bg-gradient-to-br from-sky-50/70 via-white to-orange-50/40 shadow-sm overflow-hidden">
      {/* Top Header Banner */}
      <div className="bg-gradient-to-r from-[#0a5482] via-[#0e6ba8] to-[#0a5482] px-5 py-4 sm:px-6 sm:py-5 text-white">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-3">
          <div>
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/15 text-sky-100 text-xs font-extrabold uppercase tracking-wider mb-2">
              <span>🎧 IELTS Speaking Interactive Podcast</span>
              <span>•</span>
              <span className="text-amber-300">🍊 Mastering Spoken Expressions</span>
            </div>
            <h3 className="text-lg sm:text-xl font-black leading-snug">
              Podcast Luyện Nói Theo Câu, Phản Xạ Dịch Việt - Anh & Cụm Từ Màu Da Cam
            </h3>
            <p className="text-xs sm:text-sm text-sky-100/90 mt-1">
              Luyện nói nhại từng câu (Shadowing), nghe Tiếng Việt bật ra Tiếng Anh và làm chủ{' '}
              <strong className="text-amber-300">{data.orangeCount} từ & cụm từ màu da cam</strong> cực đắt giá trong văn nói IELTS.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-2 shrink-0">
            <span className="px-3.5 py-1.5 rounded-xl bg-white/10 border border-white/15 text-xs font-bold">
              🗣️ {data.sentenceCount} câu mẫu
            </span>
            <span className="px-3.5 py-1.5 rounded-xl bg-[#ff6600] text-white text-xs font-extrabold shadow-2xs">
              🍊 {data.orangeCount} cụm từ da cam
            </span>
          </div>
        </div>

        {/* 3 Practice Mode Switcher Tabs */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 mt-4 pt-3 border-t border-white/15">
          <button
            type="button"
            onClick={() => setMode('shadowing')}
            className={`px-4 py-2.5 rounded-xl text-left transition-all flex items-center gap-2.5 ${
              mode === 'shadowing'
                ? 'bg-white text-[#0a5482] font-black shadow-md'
                : 'bg-white/10 hover:bg-white/20 text-white font-semibold'
            }`}
          >
            <span className="text-lg">🗣️</span>
            <div className="min-w-0">
              <div className="text-xs sm:text-sm leading-tight truncate">1. Nói nhại theo câu (Shadowing)</div>
              <div className={`text-[11px] truncate ${mode === 'shadowing' ? 'text-slate-500 font-medium' : 'text-sky-200'}`}>
                Nghe câu mẫu EN → Nghỉ để nói theo
              </div>
            </div>
          </button>

          <button
            type="button"
            onClick={() => setMode('reflex')}
            className={`px-4 py-2.5 rounded-xl text-left transition-all flex items-center gap-2.5 ${
              mode === 'reflex'
                ? 'bg-white text-[#0a5482] font-black shadow-md'
                : 'bg-white/10 hover:bg-white/20 text-white font-semibold'
            }`}
          >
            <span className="text-lg">⚡</span>
            <div className="min-w-0">
              <div className="text-xs sm:text-sm leading-tight truncate">2. Nghe Việt – Dịch sang Anh</div>
              <div className={`text-[11px] truncate ${mode === 'reflex' ? 'text-slate-500 font-medium' : 'text-sky-200'}`}>
                Nghe câu VI + Gợi ý cụm cam → Dịch EN
              </div>
            </div>
          </button>

          <button
            type="button"
            onClick={() => setMode('orange_drill')}
            className={`px-4 py-2.5 rounded-xl text-left transition-all flex items-center gap-2.5 ${
              mode === 'orange_drill'
                ? 'bg-[#ff6600] text-white font-black shadow-md ring-2 ring-white'
                : 'bg-white/10 hover:bg-white/20 text-white font-semibold'
            }`}
          >
            <span className="text-lg">🍊</span>
            <div className="min-w-0">
              <div className="text-xs sm:text-sm leading-tight truncate">
                3. Luyện Cụm từ Da cam ({data.orangeCount})
              </div>
              <div className={`text-[11px] truncate ${mode === 'orange_drill' ? 'text-orange-100 font-medium' : 'text-sky-200'}`}>
                Nghe nghĩa VI → Bật ra cụm từ cam + Ví dụ
              </div>
            </div>
          </button>
        </div>
      </div>

      {/* Podcast Player Control Bar */}
      <div className="p-4 sm:p-5 bg-white border-b border-slate-200/80 space-y-3">
        {/* Section Filter Pills (when in shadowing or reflex mode and multiple sections exist) */}
        {mode !== 'orange_drill' && data.sections.length > 1 && (
          <div className="flex items-center gap-1.5 overflow-x-auto pb-1">
            <span className="text-xs font-bold text-slate-400 shrink-0 mr-1">Phần luyện:</span>
            <button
              type="button"
              onClick={() => setSelectedSectionIdx(0)}
              className={`px-3 py-1 rounded-lg text-xs font-bold shrink-0 transition ${
                selectedSectionIdx === 0
                  ? 'bg-[#0a5482] text-white'
                  : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
              }`}
            >
              Tất cả ({ data.sentenceCount } câu)
            </button>
            {data.sections.map((sec) => (
              <button
                key={sec.sectionIndex}
                type="button"
                onClick={() => setSelectedSectionIdx(sec.sectionIndex)}
                className={`px-3 py-1 rounded-lg text-xs font-bold shrink-0 transition ${
                  selectedSectionIdx === sec.sectionIndex
                    ? 'bg-[#0a5482] text-white'
                    : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                }`}
              >
                {sec.sectionTitle} ({sec.sentences.length})
              </button>
            ))}
          </div>
        )}

        {/* Main Transport Controls & Settings */}
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div className="flex flex-wrap items-center gap-2">
            {!isPlaying ? (
              <button
                type="button"
                onClick={() => startPodcastFrom(activeItemIdx < totalItemsInCurrentMode ? activeItemIdx : 0)}
                className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-[#ff6600] hover:bg-[#e65c00] text-white font-black text-sm shadow-sm transition cursor-pointer"
              >
                <span>▶</span>
                <span>
                  {activeItemIdx > 0 && activeItemIdx < totalItemsInCurrentMode
                    ? `Tiếp tục Podcast (Câu ${activeItemIdx + 1}/${totalItemsInCurrentMode})`
                    : `Phát Podcast Tự Động (${totalItemsInCurrentMode} ${mode === 'orange_drill' ? 'cụm từ' : 'câu'})`}
                </span>
              </button>
            ) : (
              <button
                type="button"
                onClick={stopAllPlayback}
                className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-black text-sm shadow-sm transition cursor-pointer"
              >
                <span>⏹</span>
                <span>Dừng Podcast</span>
              </button>
            )}

            <button
              type="button"
              disabled={activeItemIdx <= 0}
              onClick={() => {
                const prev = Math.max(0, activeItemIdx - 1);
                setActiveItemIdx(prev);
                if (isPlaying) startPodcastFrom(prev);
              }}
              className="px-3 py-2 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 text-xs font-bold text-slate-700 disabled:opacity-40 cursor-pointer"
              title="Câu trước"
            >
              ⏮ Trước
            </button>

            <button
              type="button"
              onClick={() => startPodcastFrom(activeItemIdx)}
              className="px-3 py-2 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 text-xs font-bold text-slate-700 cursor-pointer"
              title="Phát lại câu hiện tại"
            >
              🔁 Lặp lại #{activeItemIdx + 1}
            </button>

            <button
              type="button"
              disabled={activeItemIdx >= totalItemsInCurrentMode - 1}
              onClick={() => {
                const next = Math.min(totalItemsInCurrentMode - 1, activeItemIdx + 1);
                setActiveItemIdx(next);
                if (isPlaying) startPodcastFrom(next);
              }}
              className="px-3 py-2 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 text-xs font-bold text-slate-700 disabled:opacity-40 cursor-pointer"
              title="Câu tiếp theo"
            >
              Tiếp ⏭
            </button>
          </div>

          {/* Speed & Pause Duration Controls */}
          <div className="flex flex-wrap items-center gap-2 text-xs">
            <div className="inline-flex items-center gap-1 bg-slate-100 px-2.5 py-1.5 rounded-xl font-bold text-slate-700">
              <span>Tốc độ:</span>
              {[0.85, 1.0, 1.15].map((r) => (
                <button
                  key={r}
                  type="button"
                  onClick={() => setPlaybackRate(r)}
                  className={`px-2 py-0.5 rounded-md transition ${
                    playbackRate === r ? 'bg-[#0a5482] text-white' : 'text-slate-600 hover:bg-slate-200'
                  }`}
                >
                  {r}x
                </button>
              ))}
            </div>

            <div className="inline-flex items-center gap-1 bg-slate-100 px-2.5 py-1.5 rounded-xl font-bold text-slate-700">
              <span>Thời gian nghỉ để nói:</span>
              {[
                { label: 'Nhanh', val: 1 },
                { label: 'Vừa', val: 2.5 },
                { label: 'Dài', val: 4.5 },
              ].map((opt) => (
                <button
                  key={opt.label}
                  type="button"
                  onClick={() => setPauseBonusSec(opt.val)}
                  className={`px-2 py-0.5 rounded-md transition ${
                    pauseBonusSec === opt.val ? 'bg-[#ff6600] text-white' : 'text-slate-600 hover:bg-slate-200'
                  }`}
                >
                  {opt.label}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Live Phase Indicator Banner */}
        <div
          className={`px-4 py-2.5 rounded-xl text-xs sm:text-sm font-bold flex items-center justify-between gap-3 transition-all ${
            phase.startsWith('pause_')
              ? 'bg-amber-50 border-2 border-[#ff6600] text-[#c2410c]'
              : phase !== 'idle'
              ? 'bg-sky-50 border border-sky-200 text-[#0a5482]'
              : 'bg-slate-50 border border-slate-200/80 text-slate-600'
          }`}
        >
          <span>{getPhaseBannerText()}</span>
          {countdownSec > 0 && (
            <span className="px-2.5 py-1 rounded-lg bg-[#ff6600] text-white font-black text-xs shrink-0">
              ⏱️ {countdownSec}s
            </span>
          )}
        </div>

        {/* Mode-specific helper bar (e.g. hide/show English answers in Reflex mode or Drill mode) */}
        {mode === 'reflex' && (
          <div className="flex flex-wrap items-center justify-between gap-2 pt-1 text-xs">
            <span className="text-slate-500 font-medium">
              💡 <strong>Cách luyện phản xạ:</strong> Nghe câu Tiếng Việt và nhìn gợi ý <strong>Cụm từ da cam 🍊</strong>, tự dịch to ra Tiếng Anh trước khi xem đáp án.
            </span>
            <div className="flex flex-wrap items-center gap-2">
              <button
                type="button"
                onClick={() => {
                  setHideReflexEnAll(!hideReflexEnAll);
                  setRevealedReflexIds({});
                }}
                className="px-3 py-1 rounded-lg border border-sky-200 bg-sky-50 text-[#0a5482] font-bold hover:bg-[#0a5482] hover:text-white transition"
              >
                {hideReflexEnAll ? '👁️ Hiện tất cả câu Tiếng Anh' : '🙈 Ẩn câu Tiếng Anh để tự dịch'}
              </button>
              <button
                type="button"
                onClick={() => setHideOrangeHintInReflex(!hideOrangeHintInReflex)}
                className="px-3 py-1 rounded-lg border border-orange-200 bg-orange-50 text-[#c2410c] font-bold hover:bg-[#ff6600] hover:text-white transition"
              >
                {hideOrangeHintInReflex ? '🍊 Hiện gợi ý Cụm từ da cam' : '🎯 Thử thách: Ẩn gợi ý Cụm từ da cam'}
              </button>
            </div>
          </div>
        )}

        {mode === 'orange_drill' && (
          <div className="flex flex-wrap items-center justify-between gap-2 pt-1 text-xs">
            <span className="text-slate-500 font-medium">
              💡 <strong>Cách làm chủ cụm từ màu da cam:</strong> Nghe nghĩa Tiếng Việt → Tự bật ra cụm từ Tiếng Anh → Nghe và nói nhại luôn câu ví dụ chứa cụm từ đó.
            </span>
            <button
              type="button"
              onClick={() => {
                setHideOrangeEnInDrill(!hideOrangeEnInDrill);
                setRevealedOrangeDrillIdx({});
              }}
              className="px-3 py-1 rounded-lg border border-orange-200 bg-orange-50 text-[#c2410c] font-bold hover:bg-[#ff6600] hover:text-white transition"
            >
              {hideOrangeEnInDrill ? '👁️ Hiện tất cả cụm từ Tiếng Anh' : '🙈 Che cụm từ Tiếng Anh để tự kiểm tra'}
            </button>
          </div>
        )}
      </div>

      {/* Main Content List (Scrollable max height so page remains easy to navigate) */}
      <div className="p-4 sm:p-6 max-h-[680px] overflow-y-auto space-y-4">
        {/* MODE 1 & 2: SENTENCE BY SENTENCE */}
        {mode !== 'orange_drill' &&
          activeSentences.map((item, idx) => {
            const isCurrent = isPlaying && activeItemIdx === idx;
            const isReflexEnVisible = !hideReflexEnAll || !!revealedReflexIds[item.id];

            return (
              <React.Fragment key={item.id}>
                {/* Section / Question Divider */}
                {item.isFirstInSection && (
                  <div className="p-4 rounded-2xl bg-[#0a5482]/5 border border-[#0a5482]/15 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                    <div>
                      <span className="inline-block px-2.5 py-0.5 rounded-md bg-[#0a5482] text-white text-[11px] font-extrabold uppercase tracking-wider mb-1">
                        {item.sectionTitle}
                      </span>
                      {item.questionEn && (
                        <div className="font-extrabold text-slate-900 text-sm sm:text-base">{item.questionEn}</div>
                      )}
                      {item.questionVi && (
                        <div className="text-xs sm:text-sm text-slate-600 italic mt-0.5">🇻🇳 {item.questionVi}</div>
                      )}
                    </div>
                    {item.questionEn && (
                      <button
                        type="button"
                        onClick={() => playSingleSnippet(item.questionEn, 'en')}
                        className="self-start sm:self-center shrink-0 px-3 py-1.5 rounded-xl bg-white border border-slate-200 hover:border-[#0a5482] text-xs font-bold text-[#0a5482] shadow-2xs cursor-pointer"
                      >
                        🔊 Nghe câu hỏi
                      </button>
                    )}
                  </div>
                )}

                {/* Sentence Card */}
                <div
                  ref={(el) => {
                    cardRefs.current[item.id] = el;
                  }}
                  className={`p-4 sm:p-5 rounded-2xl border transition-all ${
                    isCurrent
                      ? 'bg-amber-50/70 border-2 border-[#ff6600] shadow-md ring-2 ring-[#ff6600]/20'
                      : 'bg-white hover:bg-slate-50/60 border-slate-200/80 shadow-2xs'
                  }`}
                >
                  <div className="flex items-start justify-between gap-3">
                    <div className="flex items-start gap-3 min-w-0 flex-1">
                      <span
                        className={`w-7 h-7 rounded-lg text-xs font-black flex items-center justify-center shrink-0 mt-0.5 ${
                          isCurrent ? 'bg-[#ff6600] text-white' : 'bg-[#0a5482]/10 text-[#0a5482]'
                        }`}
                      >
                        {item.id}
                      </span>

                      <div className="min-w-0 flex-1 space-y-2">
                        {mode === 'shadowing' ? (
                          <>
                            {/* English Sentence with Orange Highlights */}
                            <div
                              className="text-[16px] sm:text-[17px] leading-relaxed text-slate-900 font-medium"
                              dangerouslySetInnerHTML={{ __html: item.enHtml }}
                            />
                            {/* Vietnamese Translation */}
                            <div className="text-[14.5px] sm:text-[15px] leading-relaxed text-slate-600 pl-3 border-l-2 border-sky-300">
                              🇻🇳 {item.vi}
                            </div>
                          </>
                        ) : (
                          <>
                            {/* REFLEX MODE: Show Vietnamese First */}
                            <div className="text-[16px] sm:text-[17px] leading-relaxed text-slate-900 font-bold">
                              🇻🇳 {item.vi}
                            </div>

                            {/* English Sentence (Toggleable / Auto-revealed in podcast) */}
                            {isReflexEnVisible ? (
                              <div
                                className="p-3 rounded-xl bg-emerald-50/70 border border-emerald-200 text-[15.5px] sm:text-[16.5px] leading-relaxed text-slate-900 font-medium"
                                dangerouslySetInnerHTML={{ __html: `🇬🇧 ${item.enHtml}` }}
                              />
                            ) : (
                              <button
                                type="button"
                                onClick={() => setRevealedReflexIds((prev) => ({ ...prev, [item.id]: true }))}
                                className="px-3.5 py-2 rounded-xl border border-dashed border-slate-300 hover:border-[#0a5482] text-xs font-bold text-slate-500 hover:text-[#0a5482] bg-slate-50 transition cursor-pointer"
                              >
                                👁️ Bấm để đối chiếu câu Tiếng Anh mẫu
                              </button>
                            )}
                          </>
                        )}

                        {/* Orange Spoken Expressions Badges in this Sentence */}
                        {item.orangePhrases.length > 0 && !(mode === 'reflex' && hideOrangeHintInReflex) && (
                          <div className="flex flex-wrap items-center gap-1.5 pt-1">
                            <span className="text-[11px] font-extrabold text-[#c2410c] uppercase tracking-wider mr-1">
                              🍊 Cụm từ da cam:
                            </span>
                            {item.orangePhrases.map((op, opIdx) => (
                              <button
                                key={opIdx}
                                type="button"
                                onClick={() => playSingleSnippet(op.en, 'en')}
                                className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-orange-50 hover:bg-[#ff6600] text-[#c2410c] hover:text-white border border-orange-200/90 text-xs font-bold transition cursor-pointer"
                                title="Bấm để nghe phát âm cụm từ màu da cam này"
                              >
                                <span>🔊</span>
                                <span className="underline decoration-dotted">{op.en}</span>
                                <span className="opacity-80 font-normal">({op.vi})</span>
                              </button>
                            ))}
                          </div>
                        )}
                      </div>
                    </div>

                    {/* Sentence Action Buttons */}
                    <div className="flex flex-col sm:flex-row items-end sm:items-center gap-1.5 shrink-0">
                      <button
                        type="button"
                        onClick={() => playSingleSnippet(item.en, 'en', item.enAudioUrl)}
                        className="px-2.5 py-1.5 rounded-lg bg-sky-50 hover:bg-[#0a5482] text-[#0a5482] hover:text-white border border-sky-200 text-xs font-bold transition cursor-pointer"
                        title="Nghe câu Tiếng Anh"
                      >
                        🔊 EN
                      </button>
                      <button
                        type="button"
                        onClick={() => playSingleSnippet(item.vi, 'vi', item.viAudioUrl)}
                        className="px-2.5 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-700 text-slate-700 hover:text-white text-xs font-bold transition cursor-pointer"
                        title="Nghe câu Tiếng Việt"
                      >
                        🇻🇳 VI
                      </button>
                      <button
                        type="button"
                        onClick={() => startPodcastFrom(idx)}
                        className="px-2.5 py-1.5 rounded-lg bg-orange-50 hover:bg-[#ff6600] text-[#c2410c] hover:text-white border border-orange-200 text-xs font-bold transition cursor-pointer"
                        title="Phát Podcast bắt đầu từ câu này"
                      >
                        ▶ Từ đây
                      </button>
                    </div>
                  </div>
                </div>
              </React.Fragment>
            );
          })}

        {/* MODE 3: ORANGE SPOKEN EXPRESSIONS DRILL */}
        {mode === 'orange_drill' && (
          <div className="grid grid-cols-1 gap-3.5">
            {data.orangeVocab.map((vItem, vIdx) => {
              const isCurrent = isPlaying && activeItemIdx === vIdx;
              const isEnVisible = !hideOrangeEnInDrill || !!revealedOrangeDrillIdx[vIdx];

              return (
                <div
                  key={vIdx}
                  ref={(el) => {
                    cardRefs.current[10000 + vIdx] = el;
                  }}
                  className={`p-4 sm:p-5 rounded-2xl border transition-all ${
                    isCurrent
                      ? 'bg-orange-50/80 border-2 border-[#ff6600] shadow-md ring-2 ring-[#ff6600]/20'
                      : 'bg-white hover:bg-orange-50/20 border-slate-200/85 shadow-2xs'
                  }`}
                >
                  <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-100">
                    <div className="flex items-center gap-3 flex-wrap">
                      <span className="px-2.5 py-1 rounded-lg bg-[#ff6600] text-white font-black text-xs">
                        🍊 #{vIdx + 1}
                      </span>

                      {isEnVisible ? (
                        <button
                          type="button"
                          onClick={() => playSingleSnippet(vItem.en, 'en', vItem.enAudioUrl)}
                          className="text-lg sm:text-xl font-black text-[#ff6600] hover:underline flex items-center gap-1.5 text-left cursor-pointer"
                        >
                          <span>{vItem.en}</span>
                          <span className="text-sm">🔊</span>
                        </button>
                      ) : (
                        <button
                          type="button"
                          onClick={() => setRevealedOrangeDrillIdx((prev) => ({ ...prev, [vIdx]: true }))}
                          className="px-3.5 py-1.5 rounded-xl border border-dashed border-[#ff6600] bg-orange-50 text-[#c2410c] text-xs font-extrabold cursor-pointer"
                        >
                          👁️ Hiện cụm từ Tiếng Anh
                        </button>
                      )}

                      <span className="text-slate-300 font-bold">—</span>
                      <span className="text-base sm:text-[17px] font-bold text-slate-800">🇻🇳 {vItem.vi}</span>
                    </div>

                    <div className="flex items-center gap-1.5 shrink-0">
                      <button
                        type="button"
                        onClick={() => playSingleSnippet(vItem.en, 'en', vItem.enAudioUrl)}
                        className="px-3 py-1.5 rounded-lg bg-orange-50 hover:bg-[#ff6600] text-[#c2410c] hover:text-white border border-orange-200 text-xs font-bold transition cursor-pointer"
                      >
                        🔊 Nghe cụm từ
                      </button>
                      <button
                        type="button"
                        onClick={() => playSingleSnippet(vItem.exampleEn, 'en')}
                        className="px-3 py-1.5 rounded-lg bg-sky-50 hover:bg-[#0a5482] text-[#0a5482] hover:text-white border border-sky-200 text-xs font-bold transition cursor-pointer"
                      >
                        🔊 Nghe câu ví dụ
                      </button>
                      <button
                        type="button"
                        onClick={() => startPodcastFrom(vIdx)}
                        className="px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-800 text-slate-700 hover:text-white text-xs font-bold transition cursor-pointer"
                      >
                        ▶ Luyện từ đây
                      </button>
                    </div>
                  </div>

                  {/* Example Sentence in Context */}
                  <div className="mt-3 pl-3 border-l-3 border-[#ff6600]/60 space-y-1">
                    <div className="text-xs font-bold text-slate-400 uppercase tracking-wider">
                      Câu áp dụng trong bài (Câu #{vItem.sentenceIndex}):
                    </div>
                    <div
                      className="text-[15.5px] sm:text-[16px] text-slate-800 leading-relaxed"
                      dangerouslySetInnerHTML={{ __html: vItem.exampleEnHtml }}
                    />
                    <div className="text-[14px] text-slate-600 italic">🇻🇳 {vItem.exampleVi}</div>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
};
