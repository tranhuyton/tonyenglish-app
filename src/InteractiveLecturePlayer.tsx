import React, { useState, useEffect, useRef, useCallback } from 'react';
import { 
  Play, Pause, RotateCcw, RotateCw, SkipBack, SkipForward, 
  Volume2, VolumeX, ExternalLink, List, ChevronDown, ChevronUp, 
  Sparkles, CheckCircle2, Headphones, Radio
} from 'lucide-react';

export interface LectureSegment {
  id: string;
  title: string;
  selector: string;
  en: string;
  vi: string;
  audioUrl: string;
  duration: number;
  startTime: number;
  endTime: number;
}

export interface LectureManifest {
  lectureId: string;
  courseTitle: string;
  lectureTitle: string;
  totalDuration: number;
  segments: LectureSegment[];
}

interface InteractiveLecturePlayerProps {
  manifestUrl?: string;
  onHighlightSection?: (selector: string, autoScroll: boolean) => void;
  activeSectionFromIframe?: string | null;
  onClearActiveSection?: () => void;
}

export default function InteractiveLecturePlayer({
  manifestUrl = '/audio/lectures/geography/1_1/manifest.json',
  onHighlightSection,
  activeSectionFromIframe,
  onClearActiveSection
}: InteractiveLecturePlayerProps) {
  const [manifest, setManifest] = useState<LectureManifest | null>(null);
  const [currentSegmentIndex, setCurrentSegmentIndex] = useState<number>(0);
  const [isPlaying, setIsPlaying] = useState<boolean>(false);
  const [currentTime, setCurrentTime] = useState<number>(0);
  const [playbackRate, setPlaybackRate] = useState<number>(1.0);
  const [isMuted, setIsMuted] = useState<boolean>(false);
  const [autoScroll, setAutoScroll] = useState<boolean>(true);
  const [showChapters, setShowChapters] = useState<boolean>(false);
  const [isMinimized, setIsMinimized] = useState<boolean>(false);

  const audioRef = useRef<HTMLAudioElement | null>(null);

  // 1. Tải Manifest
  useEffect(() => {
    let isMounted = true;
    fetch(manifestUrl)
      .then(res => {
        if (!res.ok) throw new Error('Cannot load manifest');
        return res.json();
      })
      .then(data => {
        if (isMounted) setManifest(data);
      })
      .catch(err => {
        console.warn('InteractiveLecturePlayer: Manifest not available for this lecture', err);
      });
    return () => { isMounted = false; };
  }, [manifestUrl]);

  const currentSegment = manifest?.segments[currentSegmentIndex] || null;

  // 2. Highlight mục đang giảng (bắn event & gọi callback)
  useEffect(() => {
    if (currentSegment) {
      if (onHighlightSection) {
        onHighlightSection(currentSegment.selector, autoScroll);
      }
      window.dispatchEvent(new CustomEvent('tony-lecture-highlight-section', {
        detail: { selector: currentSegment.selector, autoScroll }
      }));
    }
  }, [currentSegment, autoScroll, onHighlightSection]);

  // 3. Xử lý khi học sinh click trực tiếp vào thẻ trên trang bài giảng (qua window event hoặc prop)
  const jumpToSection = useCallback((secId: string) => {
    if (!manifest) return;
    const cleanId = secId.replace('#', '');
    const idx = manifest.segments.findIndex(s => 
      s.id === cleanId || 
      s.selector === `#${cleanId}` ||
      s.selector.includes(cleanId)
    );
    if (idx !== -1) {
      setCurrentSegmentIndex(idx);
      setIsPlaying(true);
      if (audioRef.current) {
        audioRef.current.currentTime = 0;
        audioRef.current.src = manifest.segments[idx].audioUrl;
        audioRef.current.playbackRate = playbackRate;
        audioRef.current.play().catch(console.warn);
      }
    }
  }, [manifest, playbackRate]);

  useEffect(() => {
    if (activeSectionFromIframe) {
      jumpToSection(activeSectionFromIframe);
      if (onClearActiveSection) onClearActiveSection();
    }
  }, [activeSectionFromIframe, jumpToSection, onClearActiveSection]);

  useEffect(() => {
    const handlePlaySectionEvent = (e: any) => {
      if (e.detail?.sectionId) {
        jumpToSection(e.detail.sectionId);
      }
    };
    window.addEventListener('tony-lecture-play-section', handlePlaySectionEvent);
    return () => window.removeEventListener('tony-lecture-play-section', handlePlaySectionEvent);
  }, [jumpToSection]);

  // 4. Phát audio khi chuyển segment
  useEffect(() => {
    if (!manifest || !currentSegment) return;
    
    if (!audioRef.current) {
      audioRef.current = new Audio();
    }
    
    const audio = audioRef.current;
    audio.src = currentSegment.audioUrl;
    audio.playbackRate = playbackRate;
    audio.muted = isMuted;

    const handleTimeUpdate = () => {
      const segStart = currentSegment.startTime || 0;
      setCurrentTime(segStart + audio.currentTime);
    };

    const handleEnded = () => {
      // Chuyển sang segment tiếp theo
      if (currentSegmentIndex < manifest.segments.length - 1) {
        setCurrentSegmentIndex(prev => prev + 1);
      } else {
        setIsPlaying(false);
        setCurrentTime(manifest.totalDuration);
      }
    };

    audio.addEventListener('timeupdate', handleTimeUpdate);
    audio.addEventListener('ended', handleEnded);

    if (isPlaying) {
      audio.play().catch(console.warn);
    }

    return () => {
      audio.removeEventListener('timeupdate', handleTimeUpdate);
      audio.removeEventListener('ended', handleEnded);
    };
  }, [currentSegmentIndex, manifest, isPlaying]);

  // Điều khiển Play / Pause
  const togglePlay = useCallback(() => {
    if (!audioRef.current) return;
    if (isPlaying) {
      audioRef.current.pause();
      setIsPlaying(false);
    } else {
      audioRef.current.playbackRate = playbackRate;
      audioRef.current.play().then(() => setIsPlaying(true)).catch(console.warn);
    }
  }, [isPlaying, playbackRate]);

  // Tua lại / tới 5s
  const handleSkip = useCallback((seconds: number) => {
    if (!audioRef.current || !manifest || !currentSegment) return;
    
    const newSegTime = audioRef.current.currentTime + seconds;
    if (newSegTime >= 0 && newSegTime <= currentSegment.duration) {
      audioRef.current.currentTime = newSegTime;
    } else if (newSegTime < 0) {
      // Quay về segment trước nếu có
      if (currentSegmentIndex > 0) {
        setCurrentSegmentIndex(prev => prev - 1);
      } else {
        audioRef.current.currentTime = 0;
      }
    } else {
      // Chuyển segment tiếp theo nếu có
      if (currentSegmentIndex < manifest.segments.length - 1) {
        setCurrentSegmentIndex(prev => prev + 1);
      }
    }
  }, [currentSegment, currentSegmentIndex, manifest]);

  // Chuyển sang segment cụ thể
  const handleSelectSegment = useCallback((index: number) => {
    if (!manifest) return;
    setCurrentSegmentIndex(index);
    setIsPlaying(true);
    setShowChapters(false);
    if (audioRef.current) {
      audioRef.current.src = manifest.segments[index].audioUrl;
      audioRef.current.playbackRate = playbackRate;
      audioRef.current.play().catch(console.warn);
    }
  }, [manifest, playbackRate]);

  // Đổi tốc độ phát
  const handleChangeSpeed = useCallback((speed: number) => {
    setPlaybackRate(speed);
    if (audioRef.current) {
      audioRef.current.playbackRate = speed;
    }
  }, []);

  // Format thời gian mm:ss
  const formatTime = (secs: number) => {
    if (isNaN(secs) || secs < 0) return '00:00';
    const m = Math.floor(secs / 60);
    const s = Math.floor(secs % 60);
    return `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
  };

  if (!manifest) return null;

  const totalDuration = manifest.totalDuration || 1;
  const progressPercent = Math.min(100, Math.max(0, (currentTime / totalDuration) * 100));

  return (
    <div className="w-full max-w-[960px] mx-auto mb-8 transition-all duration-300">
      <div className="bg-gradient-to-br from-[#0a5482] via-[#084266] to-[#032b44] text-white rounded-2xl shadow-xl border border-sky-500/30 overflow-hidden">
        
        {/* TOP BRANDING BAR: Logo TonyEnglish & link tonyenglish.vn */}
        <div className="px-5 py-3 bg-black/20 border-b border-white/10 flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <a 
              href="https://tonyenglish.vn/vi" 
              target="_blank" 
              rel="noopener noreferrer" 
              className="flex items-center gap-2 group hover:opacity-90 transition-opacity"
              title="Truy cập website chính thức TonyEnglish"
            >
              <img 
                src="/logo-shield.png" 
                alt="TonyEnglish Shield" 
                className="h-7 w-auto object-contain drop-shadow" 
              />
              <div className="flex flex-col text-left leading-none">
                <span className="text-[13px] font-black text-white tracking-wider group-hover:text-[#2bd6eb] transition-colors">
                  TONYENGLISH TEST CENTRE
                </span>
                <span className="text-[11px] font-bold text-sky-300 flex items-center gap-1">
                  tonyenglish.vn <ExternalLink className="w-2.5 h-2.5 opacity-70" />
                </span>
              </div>
            </a>

            <div className="hidden sm:flex items-center gap-2 pl-3 border-l border-white/15">
              <span className="flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-sky-400/20 text-[#2bd6eb] text-[11px] font-bold border border-sky-400/30">
                <Radio className="w-3 h-3 animate-pulse text-rose-400" />
                Song ngữ Cambridge
              </span>
              <span className="text-[11px] text-slate-300">
                🇬🇧 Giọng Anh - Anh Nam & 🇻🇳 Tiếng Việt (Giọng Nam Hà Nội)
              </span>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => setShowChapters(!showChapters)}
              className="px-3 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 text-xs font-bold transition-all flex items-center gap-1.5 text-sky-200"
              title="Xem danh sách các phân đoạn bài giảng"
            >
              <List className="w-3.5 h-3.5" />
              <span>Mục lục ({currentSegmentIndex + 1}/{manifest.segments.length})</span>
            </button>

            <button
              onClick={() => setIsMinimized(!isMinimized)}
              className="p-1.5 rounded-lg bg-white/10 hover:bg-white/20 text-sky-200 transition-all"
              title={isMinimized ? "Mở rộng thanh nghe giảng" : "Thu gọn"}
            >
              {isMinimized ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
            </button>
          </div>
        </div>

        {/* PLAYER MAIN CONTENT */}
        {!isMinimized && (
          <div className="p-4 md:p-6 space-y-4">
            
            {/* SUBTITLE & SECTION INFO */}
            <div className="bg-black/25 rounded-xl p-4 border border-white/10 backdrop-blur-sm">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-extrabold text-[#2bd6eb] uppercase tracking-wider flex items-center gap-1.5">
                  <Headphones className="w-3.5 h-3.5 animate-bounce" />
                  Đang phát: {currentSegment?.title}
                </span>
                <span className="text-[11px] font-semibold text-sky-200/80">
                  {formatTime(currentTime)} / {formatTime(totalDuration)}
                </span>
              </div>

              {/* Lời thoại song ngữ */}
              <div className="space-y-2 mt-2">
                <div className="flex items-start gap-2">
                  <span className="text-xs shrink-0 select-none font-bold bg-blue-500/30 px-1.5 py-0.5 rounded text-blue-200">🇬🇧 UK</span>
                  <p className="text-[14px] md:text-[15px] font-semibold text-white leading-relaxed">
                    {currentSegment?.en}
                  </p>
                </div>
                <div className="flex items-start gap-2 pt-1 border-t border-white/10">
                  <span className="text-xs shrink-0 select-none font-bold bg-amber-500/30 px-1.5 py-0.5 rounded text-amber-200">🇻🇳 VI</span>
                  <p className="text-[13px] md:text-[14px] font-medium text-amber-200/95 leading-relaxed italic">
                    {currentSegment?.vi}
                  </p>
                </div>
              </div>
            </div>

            {/* TIMELINE PROGRESS BAR */}
            <div className="space-y-1.5">
              <div 
                className="w-full bg-white/20 hover:bg-white/30 h-2.5 rounded-full cursor-pointer overflow-hidden transition-all relative group"
                onClick={(e) => {
                  const rect = e.currentTarget.getBoundingClientRect();
                  const clickRatio = (e.clientX - rect.left) / rect.width;
                  const targetSec = clickRatio * totalDuration;
                  // Tìm segment tương ứng
                  const foundIdx = manifest.segments.findIndex(s => targetSec >= s.startTime && targetSec <= s.endTime);
                  if (foundIdx !== -1) {
                    handleSelectSegment(foundIdx);
                  }
                }}
              >
                <div 
                  className="bg-gradient-to-r from-[#2bd6eb] to-emerald-400 h-full rounded-full transition-all duration-150 relative"
                  style={{ width: `${progressPercent}%` }}
                />
              </div>
              <div className="flex justify-between text-[11px] font-mono font-medium text-sky-200/70">
                <span>{formatTime(currentTime)}</span>
                <span className="text-xs font-sans text-sky-300">
                  💡 Nhấn vào thẻ trên bài giảng để nghe giảng riêng thẻ đó
                </span>
                <span>{formatTime(totalDuration)}</span>
              </div>
            </div>

            {/* CONTROLS ROW */}
            <div className="flex flex-wrap items-center justify-between gap-4 pt-2">
              
              {/* Playback rate controls */}
              <div className="flex items-center gap-1">
                <span className="text-[11px] text-sky-200/70 mr-1 hidden sm:inline">Tốc độ:</span>
                {[0.8, 1.0, 1.25, 1.5].map(rate => (
                  <button
                    key={rate}
                    onClick={() => handleChangeSpeed(rate)}
                    className={`px-2 py-1 rounded-md text-xs font-bold transition-all ${
                      playbackRate === rate 
                        ? 'bg-[#2bd6eb] text-[#032b44] shadow' 
                        : 'bg-white/10 hover:bg-white/20 text-white'
                    }`}
                  >
                    {rate}x
                  </button>
                ))}
              </div>

              {/* Main Player Buttons */}
              <div className="flex items-center gap-2">
                <button
                  onClick={() => currentSegmentIndex > 0 && handleSelectSegment(currentSegmentIndex - 1)}
                  disabled={currentSegmentIndex === 0}
                  className="p-2 rounded-xl bg-white/10 hover:bg-white/20 disabled:opacity-30 text-white transition-all"
                  title="Phân đoạn trước"
                >
                  <SkipBack className="w-4 h-4" />
                </button>

                <button
                  onClick={() => handleSkip(-5)}
                  className="p-2 rounded-xl bg-white/10 hover:bg-white/20 text-white transition-all text-xs font-bold flex items-center gap-1"
                  title="Tua lại 5 giây"
                >
                  <RotateCcw className="w-3.5 h-3.5" />
                  <span className="text-[10px]">5s</span>
                </button>

                <button
                  onClick={togglePlay}
                  className="w-12 h-12 rounded-full bg-gradient-to-r from-[#2bd6eb] to-sky-400 hover:from-white hover:to-[#2bd6eb] text-[#032b44] flex items-center justify-center shadow-lg hover:scale-105 active:scale-95 transition-all"
                  title={isPlaying ? "Tạm dừng" : "Phát bài giảng"}
                >
                  {isPlaying ? (
                    <Pause className="w-6 h-6 fill-[#032b44]" />
                  ) : (
                    <Play className="w-6 h-6 fill-[#032b44] ml-0.5" />
                  )}
                </button>

                <button
                  onClick={() => handleSkip(5)}
                  className="p-2 rounded-xl bg-white/10 hover:bg-white/20 text-white transition-all text-xs font-bold flex items-center gap-1"
                  title="Tua tới 5 giây"
                >
                  <span className="text-[10px]">5s</span>
                  <RotateCw className="w-3.5 h-3.5" />
                </button>

                <button
                  onClick={() => currentSegmentIndex < manifest.segments.length - 1 && handleSelectSegment(currentSegmentIndex + 1)}
                  disabled={currentSegmentIndex === manifest.segments.length - 1}
                  className="p-2 rounded-xl bg-white/10 hover:bg-white/20 disabled:opacity-30 text-white transition-all"
                  title="Phân đoạn tiếp theo"
                >
                  <SkipForward className="w-4 h-4" />
                </button>
              </div>

              {/* Options: Auto scroll toggle & Mute */}
              <div className="flex items-center gap-3">
                <label className="flex items-center gap-2 cursor-pointer text-xs font-semibold text-sky-200 select-none">
                  <input
                    type="checkbox"
                    checked={autoScroll}
                    onChange={(e) => setAutoScroll(e.target.checked)}
                    className="w-4 h-4 accent-[#2bd6eb] rounded cursor-pointer"
                  />
                  <span className="hidden sm:inline">Cuộn theo lời giảng</span>
                </label>

                <button
                  onClick={() => {
                    const next = !isMuted;
                    setIsMuted(next);
                    if (audioRef.current) audioRef.current.muted = next;
                  }}
                  className="p-2 rounded-xl bg-white/10 hover:bg-white/20 text-white transition-all"
                  title={isMuted ? "Bật âm" : "Tắt âm"}
                >
                  {isMuted ? <VolumeX className="w-4 h-4 text-rose-400" /> : <Volume2 className="w-4 h-4" />}
                </button>
              </div>

            </div>

          </div>
        )}

        {/* CHAPTERS DRAWER (Danh sách mục lục phân đoạn) */}
        {showChapters && !isMinimized && (
          <div className="border-t border-white/15 bg-black/40 p-4 max-h-60 overflow-y-auto space-y-1.5 animate-in fade-in duration-200">
            <div className="text-xs font-bold text-sky-300 mb-2 flex items-center gap-1">
              <Sparkles className="w-3.5 h-3.5 text-amber-400" />
              Chọn phân đoạn để nghe giảng ngay:
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
              {manifest.segments.map((seg, idx) => (
                <button
                  key={seg.id}
                  onClick={() => handleSelectSegment(idx)}
                  className={`flex items-center justify-between p-2.5 rounded-xl text-left text-xs font-medium transition-all ${
                    idx === currentSegmentIndex
                      ? 'bg-[#2bd6eb]/20 text-[#2bd6eb] border border-[#2bd6eb]/40 font-bold'
                      : 'bg-white/5 hover:bg-white/10 text-slate-200 border border-transparent'
                  }`}
                >
                  <div className="flex items-center gap-2 truncate pr-2">
                    <span className="w-5 h-5 rounded-full bg-white/10 flex items-center justify-center text-[10px] shrink-0 font-bold">
                      {idx + 1}
                    </span>
                    <span className="truncate">{seg.title}</span>
                  </div>
                  <span className="text-[10px] opacity-70 shrink-0 font-mono">
                    {formatTime(seg.duration)}
                  </span>
                </button>
              ))}
            </div>
          </div>
        )}

      </div>
    </div>
  );
}
