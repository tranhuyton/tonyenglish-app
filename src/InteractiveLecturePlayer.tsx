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
  majorSections?: Record<string, { start: number; end: number }>;
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

  // Playback modes:
  // 'single': Đọc riêng tiểu mục -> đọc xong tự dừng, không đọc tiếp.
  // 'section': Đọc mục lớn -> đọc lần lượt hết tiểu mục này đến tiểu mục khác trong mục lớn.
  // 'all': Đọc toàn bộ bài giảng.
  const [playMode, setPlayMode] = useState<'single' | 'section' | 'all'>('all');
  const [sectionEndIndex, setSectionEndIndex] = useState<number | null>(null);

  // Định nghĩa các mục lớn và khoảng index các tiểu mục tương ứng
  const MAJOR_SECTION_RANGES: Record<string, { start: number; end: number }> = {
    intro: { start: 0, end: 7 },
    drainage_basin: { start: 1, end: 7 },
    bradshaw_model: { start: 8, end: 10 },
    water_cycle: { start: 11, end: 18 },
    fluvial_processes: { start: 19, end: 28 },
  };

  const audioRef = useRef<HTMLAudioElement | null>(null);

  // Lưu trạng thái vào Refs để event listener luôn đọc được giá trị mới nhất
  const playModeRef = useRef(playMode);
  playModeRef.current = playMode;

  const sectionEndIndexRef = useRef(sectionEndIndex);
  sectionEndIndexRef.current = sectionEndIndex;

  const currentSegmentIndexRef = useRef(currentSegmentIndex);
  currentSegmentIndexRef.current = currentSegmentIndex;

  const manifestRef = useRef(manifest);
  manifestRef.current = manifest;

  const isPlayingRef = useRef(isPlaying);
  isPlayingRef.current = isPlaying;

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

  useEffect(() => {
    const handleReHighlight = () => {
      if (currentSegment) {
        window.dispatchEvent(new CustomEvent('tony-lecture-highlight-section', {
          detail: { selector: currentSegment.selector, autoScroll: true }
        }));
      }
    };
    window.addEventListener('tony-lecture-rehighlight', handleReHighlight);
    return () => window.removeEventListener('tony-lecture-rehighlight', handleReHighlight);
  }, [currentSegment]);

  // Xử lý khi kết thúc 1 audio segment
  const handleEnded = useCallback(() => {
    const curIdx = currentSegmentIndexRef.current;
    const mode = playModeRef.current;
    const endIdx = sectionEndIndexRef.current;
    const man = manifestRef.current;
    if (!man) return;

    if (mode === 'single') {
      // Khi bấm vào mỗi tiểu mục: đọc xong tiểu mục nào thì dừng chỗ đấy không đọc tiếp
      setIsPlaying(false);
      if (audioRef.current) {
        audioRef.current.currentTime = 0;
      }
    } else if (mode === 'section') {
      // Khi bấm vào mục lớn: đọc lần lượt hết tiểu mục này đến tiểu mục khác trong mục lớn
      if (endIdx !== null && curIdx < endIdx) {
        setCurrentSegmentIndex(curIdx + 1);
        setIsPlaying(true);
      } else {
        // Đã đọc xong toàn bộ tiểu mục của mục lớn -> Dừng lại
        setIsPlaying(false);
        if (audioRef.current) {
          audioRef.current.currentTime = 0;
        }
      }
    } else {
      // Chế độ phát toàn bộ bài
      if (curIdx < man.segments.length - 1) {
        setCurrentSegmentIndex(curIdx + 1);
        setIsPlaying(true);
      } else {
        setIsPlaying(false);
        if (audioRef.current) {
          audioRef.current.currentTime = 0;
        }
      }
    }
  }, []);

  // Khởi tạo Audio Element và gán listeners
  useEffect(() => {
    const audio = new Audio();
    audioRef.current = audio;

    const handleTimeUpdate = () => {
      const curIdx = currentSegmentIndexRef.current;
      const man = manifestRef.current;
      const seg = man?.segments[curIdx];
      const segStart = seg?.startTime || 0;
      setCurrentTime(segStart + audio.currentTime);
    };

    audio.addEventListener('timeupdate', handleTimeUpdate);
    audio.addEventListener('ended', handleEnded);

    return () => {
      audio.removeEventListener('timeupdate', handleTimeUpdate);
      audio.removeEventListener('ended', handleEnded);
      audio.pause();
      audio.src = '';
    };
  }, [handleEnded]);

  // Nạp audio source khi currentSegmentIndex thay đổi
  useEffect(() => {
    if (!manifest || !audioRef.current) return;
    const seg = manifest.segments[currentSegmentIndex];
    if (!seg) return;

    const audio = audioRef.current;
    audio.src = seg.audioUrl;
    audio.playbackRate = playbackRate;
    audio.muted = isMuted;
    audio.currentTime = 0;

    if (isPlaying) {
      audio.play().catch(console.warn);
    }
  }, [currentSegmentIndex, manifest]);

  // Điều khiển Play / Pause đồng bộ với audioRef
  useEffect(() => {
    if (!audioRef.current) return;
    if (isPlaying) {
      if (audioRef.current.paused) {
        audioRef.current.play().catch(console.warn);
      }
    } else {
      if (!audioRef.current.paused) {
        audioRef.current.pause();
      }
    }
  }, [isPlaying]);

  // Điều khiển Tốc độ phát
  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.playbackRate = playbackRate;
    }
  }, [playbackRate]);

  // Điều khiển Tắt âm
  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.muted = isMuted;
    }
  }, [isMuted]);

  // 3. Xử lý khi học sinh click trực tiếp vào thẻ trên trang bài giảng (qua window event hoặc prop)
  const jumpToSection = useCallback((secId: string) => {
    if (!manifest) return;
    const cleanId = secId.replace('#', '');
    const idx = manifest.segments.findIndex(s => 
      s.id === cleanId || 
      s.selector === `#${cleanId}` ||
      s.selector.includes(cleanId)
    );
    if (idx === -1) return;

    const ranges = manifest.majorSections || MAJOR_SECTION_RANGES;
    const range = ranges[cleanId];
    const isMajor = !!range;

    const curIdx = currentSegmentIndexRef.current;
    const isCurrentlyPlaying = isPlayingRef.current;
    const audio = audioRef.current;

    // A. Kiểm tra xem có đang click lại vào đúng mục/tiểu mục đang được chọn không
    const isSameSegment = idx === curIdx;
    const isInsideActiveSection = isMajor && curIdx >= range.start && curIdx <= range.end && playModeRef.current === 'section';

    if (isSameSegment || isInsideActiveSection) {
      if (isCurrentlyPlaying) {
        // Đang đọc mà bấm vào một lần nữa thì dừng (pause)
        audio?.pause();
        setIsPlaying(false);
      } else {
        // Bấm thêm lần nữa lại tiếp tục play
        audio?.play().then(() => setIsPlaying(true)).catch(console.warn);
      }
      return;
    }

    // B. Click vào một mục / tiểu mục mới
    if (isMajor) {
      // Khi bấm vào mục lớn: đọc lần lượt hết tiểu mục này đến tiểu mục khác
      setPlayMode('section');
      setSectionEndIndex(range.end);
      setCurrentSegmentIndex(range.start);
      setIsPlaying(true);
    } else {
      // Khi bấm vào mỗi tiểu mục: đọc xong tiểu mục nào thì dừng chỗ đấy không đọc tiếp
      setPlayMode('single');
      setSectionEndIndex(null);
      setCurrentSegmentIndex(idx);
      setIsPlaying(true);
    }
  }, [manifest]);

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

  // Điều khiển Play / Pause từ nút trên thanh Player
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
      if (currentSegmentIndex > 0) {
        setCurrentSegmentIndex(prev => prev - 1);
      } else {
        audioRef.current.currentTime = 0;
      }
    } else {
      if (currentSegmentIndex < manifest.segments.length - 1) {
        setCurrentSegmentIndex(prev => prev + 1);
      }
    }
  }, [currentSegment, currentSegmentIndex, manifest]);

  // Chuyển sang segment cụ thể từ Mục lục hoặc Prev/Next
  const handleSelectSegment = useCallback((index: number) => {
    if (!manifest) return;
    const seg = manifest.segments[index];
    const ranges = manifest.majorSections || MAJOR_SECTION_RANGES;
    const range = ranges[seg.id];
    if (range) {
      setPlayMode('section');
      setSectionEndIndex(range.end);
    } else {
      setPlayMode('single');
      setSectionEndIndex(null);
    }
    setCurrentSegmentIndex(index);
    setIsPlaying(true);
    setShowChapters(false);
  }, [manifest]);

  // Đổi tốc độ phát
  const handleChangeSpeed = useCallback((speed: number) => {
    setPlaybackRate(speed);
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
    <div className="w-full max-w-[960px] mx-auto mb-10 transition-all duration-300">
      <div className="bg-gradient-to-br from-[#0a5482] via-[#084266] to-[#032b44] text-white rounded-2xl shadow-xl border border-sky-500/30 overflow-hidden">
        
        {/* TOP BRANDING BAR: Logo TonyEnglish & link tonyenglish.vn */}
        <div className="px-5 py-3 bg-black/20 border-b border-white/10 flex items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <a 
              href="https://tonyenglish.vn/vi" 
              target="_blank" 
              rel="noopener noreferrer" 
              className="flex items-center gap-2 group hover:opacity-90 transition-opacity shrink-0"
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

            <div className="hidden sm:flex items-center pl-3 border-l border-white/15">
              <span className="flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-sky-400/20 text-[#2bd6eb] text-[11px] font-bold border border-sky-400/30">
                <Radio className="w-3 h-3 animate-pulse text-rose-400" />
                Song ngữ Cambridge
              </span>
            </div>
          </div>

          <div className="flex items-center gap-2 shrink-0">
            <button
              onClick={() => setShowChapters(!showChapters)}
              className="px-3 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 text-xs font-bold transition-all flex items-center gap-1.5 text-sky-200 hover:text-white"
              title="Xem danh sách các phân đoạn bài giảng"
            >
              <List className="w-3.5 h-3.5 text-[#2bd6eb]" />
              <span>Mục lục ({currentSegmentIndex + 1}/{manifest.segments.length})</span>
            </button>

            <button
              onClick={() => setIsMinimized(!isMinimized)}
              className="p-1.5 rounded-lg bg-white/10 hover:bg-white/20 text-sky-200 hover:text-white transition-all"
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
              <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
                <div className="flex items-center gap-2 flex-wrap">
                  <span className="text-xs font-extrabold text-[#2bd6eb] uppercase tracking-wider flex items-center gap-1.5">
                    <Headphones className="w-3.5 h-3.5 animate-bounce" />
                    Đang phát: {currentSegment?.title}
                  </span>
                  {playMode === 'single' ? (
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-400/20 text-amber-300 border border-amber-400/30">
                      🎯 Tiểu mục (Tự dừng khi đọc xong)
                    </span>
                  ) : playMode === 'section' ? (
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-400/20 text-emerald-300 border border-emerald-400/30">
                      🔁 Mục lớn (Đọc lần lượt từng phần)
                    </span>
                  ) : (
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-sky-400/20 text-sky-300 border border-sky-400/30">
                      ▶️ Toàn bài
                    </span>
                  )}
                </div>
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
                  💡 Nhấn vào thẻ để nghe riêng & tự dừng • Nhấn lần nữa để Tạm dừng / Tiếp tục • Nhấn mục lớn để nghe lần lượt
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
