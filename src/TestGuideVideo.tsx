import React, { useState, useRef, useEffect, useMemo } from 'react';
import { supabase } from './supabase';

export interface VideoSourceInfo {
  type: 'youtube' | 'drive' | 'direct' | 'loom' | 'vimeo' | 'iframe';
  embedUrl: string;
  originalUrl: string;
}

export interface GuideVideoItem {
  id: string;
  title: string;
  url: string;
}

export function parseVideoSource(rawUrl: string | null | undefined): VideoSourceInfo | null {
  if (!rawUrl || typeof rawUrl !== 'string') return null;
  const url = rawUrl.trim();
  if (!url) return null;

  // 1. YouTube
  const ytMatch = url.match(/(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=|shorts\/))([\w-]{11})/i);
  if (ytMatch && ytMatch[1]) {
    const originParam = typeof window !== 'undefined' ? `&origin=${encodeURIComponent(window.location.origin)}&widget_referrer=${encodeURIComponent(window.location.origin)}` : '';
    return {
      type: 'youtube',
      embedUrl: `https://www.youtube.com/embed/${ytMatch[1]}?autoplay=1&rel=0&enablejsapi=1${originParam}`,
      originalUrl: url
    };
  }

  // 2. Google Drive
  const driveMatch = url.match(/drive\.google\.com\/(?:file\/d\/([a-zA-Z0-9_-]+)|open\?id=([a-zA-Z0-9_-]+))/i);
  if (driveMatch) {
    const fileId = driveMatch[1] || driveMatch[2];
    return {
      type: 'drive',
      embedUrl: `https://drive.google.com/file/d/${fileId}/preview`,
      originalUrl: url
    };
  }

  // 3. Loom
  const loomMatch = url.match(/loom\.com\/(?:share|embed)\/([a-zA-Z0-9]+)/i);
  if (loomMatch && loomMatch[1]) {
    return {
      type: 'loom',
      embedUrl: `https://www.loom.com/embed/${loomMatch[1]}?autoplay=1`,
      originalUrl: url
    };
  }

  // 4. Vimeo
  const vimeoMatch = url.match(/vimeo\.com\/(\d+)/i);
  if (vimeoMatch && vimeoMatch[1]) {
    return {
      type: 'vimeo',
      embedUrl: `https://player.vimeo.com/video/${vimeoMatch[1]}?autoplay=1`,
      originalUrl: url
    };
  }

  // 5. Direct video files (MP4, WebM, MOV, or Supabase storage video)
  const isDirectVideo = /\.(mp4|webm|mov|m4v|ogg)(\?.*)?$/i.test(url) ||
    url.includes('/test_assets/videos/') ||
    url.includes('video/mp4') ||
    url.includes('video/webm');
  if (isDirectVideo) {
    return {
      type: 'direct',
      embedUrl: url,
      originalUrl: url
    };
  }

  // 6. Generic embed or fallback
  return {
    type: 'iframe',
    embedUrl: url,
    originalUrl: url
  };
}

export function extractGuideVideos(testData: any): GuideVideoItem[] {
  if (!testData) return [];

  const rawList =
    (Array.isArray(testData?.guide_videos) && testData.guide_videos.length > 0 ? testData.guide_videos : null) ||
    (Array.isArray(testData?.content_json?.guide_videos) && testData.content_json.guide_videos.length > 0 ? testData.content_json.guide_videos : null) ||
    (Array.isArray(testData?.content_json?.basicInfo?.guide_videos) && testData.content_json.basicInfo.guide_videos.length > 0 ? testData.content_json.basicInfo.guide_videos : null) ||
    (Array.isArray(testData?.json_config?.guide_videos) && testData.json_config.guide_videos.length > 0 ? testData.json_config.guide_videos : null);

  const legacyUrlRaw =
    testData?.guide_video_url ||
    testData?.content_json?.guide_video_url ||
    testData?.content_json?.basicInfo?.guide_video_url ||
    testData?.json_config?.guide_video_url ||
    '';
  const legacyUrl = typeof legacyUrlRaw === 'string' ? legacyUrlRaw.trim() : '';

  const result: GuideVideoItem[] = [];
  const seenUrls = new Set<string>();

  if (rawList) {
    rawList.forEach((item: any, idx: number) => {
      const url = typeof item === 'string' ? item.trim() : String(item?.url || '').trim();
      if (!url || seenUrls.has(url)) return;
      seenUrls.add(url);
      result.push({
        id: String(item?.id || `v_${idx + 1}`),
        title: String(item?.title || '').trim() || `Video hướng dẫn #${result.length + 1}`,
        url,
      });
    });
  }

  if (result.length === 0 && legacyUrl) {
    const src = parseVideoSource(legacyUrl);
    result.push({
      id: 'v_1',
      title: src?.type === 'youtube' ? 'Video bài giảng / gợi ý (YouTube)' : 'Video hướng dẫn giải đề',
      url: legacyUrl,
    });
  }

  return result;
}

export async function saveTestGuideVideos(testId: string, rawVideos: GuideVideoItem[]) {
  if (!testId) throw new Error('Test ID is required');

  const seen = new Set<string>();
  const cleanVideos: GuideVideoItem[] = [];
  (rawVideos || []).forEach((item, idx) => {
    const url = String(item?.url || '').trim();
    if (!url || seen.has(url)) return;
    seen.add(url);
    cleanVideos.push({
      id: String(item?.id || `v_${Date.now()}_${idx}`),
      title: String(item?.title || '').trim() || `Video hướng dẫn #${cleanVideos.length + 1}`,
      url,
    });
  });

  const primaryUrl = cleanVideos[0]?.url || null;

  const { data: currentTest, error: fetchErr } = await supabase
    .from('tests')
    .select('id, content_json, json_config')
    .eq('id', testId)
    .single();

  if (fetchErr) {
    console.error('Error fetching test before saving videos:', fetchErr);
    throw fetchErr;
  }

  const currentContentJson = currentTest?.content_json || {};
  const currentBasicInfo = currentContentJson?.basicInfo || {};
  const currentJsonConfig = currentTest?.json_config || {};

  const updatedContentJson = {
    ...currentContentJson,
    guide_video_url: primaryUrl,
    guide_videos: cleanVideos,
    basicInfo: {
      ...currentBasicInfo,
      guide_video_url: primaryUrl,
      guide_videos: cleanVideos,
    }
  };

  const updatedJsonConfig = {
    ...currentJsonConfig,
    guide_video_url: primaryUrl,
    guide_videos: cleanVideos,
  };

  const { error: updateErr } = await supabase
    .from('tests')
    .update({
      content_json: updatedContentJson,
      json_config: updatedJsonConfig,
    })
    .eq('id', testId);

  if (updateErr) {
    console.error('Error updating test guide videos:', updateErr);
    throw updateErr;
  }

  try {
    const saved = sessionStorage.getItem('lms_current_test');
    if (saved) {
      const parsed = JSON.parse(saved);
      if (parsed && (parsed.id === testId || !parsed.id)) {
        parsed.content_json = updatedContentJson;
        parsed.json_config = updatedJsonConfig;
        parsed.guide_video_url = primaryUrl;
        parsed.guide_videos = cleanVideos;
        sessionStorage.setItem('lms_current_test', JSON.stringify(parsed));
      }
    }
  } catch (e) {
    console.warn('Could not update sessionStorage cache:', e);
  }

  return { content_json: updatedContentJson, json_config: updatedJsonConfig, videos: cleanVideos, primaryUrl };
}

export async function saveTestGuideVideo(testId: string, newVideoUrl: string | null) {
  const clean = newVideoUrl ? newVideoUrl.trim() : '';
  const items: GuideVideoItem[] = clean
    ? [{ id: 'v_1', title: 'Video hướng dẫn giải đề', url: clean }]
    : [];
  return saveTestGuideVideos(testId, items);
}

// Hook to manage multi-video state and operations
export function useTestGuideVideo(
  testData: any,
  onVideoChange?: (url: string | null, videos: GuideVideoItem[]) => void
) {
  const testId = testData?.id || '';
  const initialVideos = useMemo(() => extractGuideVideos(testData), [testData]);

  const [videos, setVideos] = useState<GuideVideoItem[]>(initialVideos);
  const [activeVideoIndex, setActiveVideoIndex] = useState<number>(0);
  const [isOpen, setIsOpen] = useState(false);
  const [isTheaterOpen, setIsTheaterOpen] = useState(false);
  const [isEditModalOpen, setIsEditModalOpen] = useState(false);

  useEffect(() => {
    const extracted = extractGuideVideos(testData);
    setVideos(extracted);
    setActiveVideoIndex((prev) => (prev < extracted.length ? prev : 0));
  }, [testData]);

  const safeIndex = activeVideoIndex < videos.length ? activeVideoIndex : 0;
  const videoUrl = videos[safeIndex]?.url || videos[0]?.url || null;

  const setVideoUrl = (url: string | null) => {
    if (!url) {
      setVideos([]);
      setActiveVideoIndex(0);
    } else {
      setVideos([{ id: 'v_1', title: 'Video hướng dẫn giải đề', url }]);
      setActiveVideoIndex(0);
    }
  };

  const handleSaveVideos = async (newVideos: GuideVideoItem[]) => {
    let savedList = newVideos;
    let primaryUrl = newVideos[0]?.url || null;
    if (testId) {
      const res = await saveTestGuideVideos(testId, newVideos);
      savedList = res.videos;
      primaryUrl = res.primaryUrl;
    }
    setVideos(savedList);
    setActiveVideoIndex((prev) => (prev < savedList.length ? prev : 0));
    if (onVideoChange) {
      onVideoChange(primaryUrl, savedList);
    }
  };

  const handleSaveVideo = async (newUrl: string | null) => {
    const nextList: GuideVideoItem[] = newUrl && newUrl.trim()
      ? [{ id: 'v_1', title: 'Video hướng dẫn giải đề', url: newUrl.trim() }]
      : [];
    await handleSaveVideos(nextList);
  };

  return {
    testId,
    videos,
    setVideos,
    activeVideoIndex: safeIndex,
    setActiveVideoIndex,
    videoUrl,
    setVideoUrl,
    isOpen,
    setIsOpen,
    isTheaterOpen,
    setIsTheaterOpen,
    isEditModalOpen,
    setIsEditModalOpen,
    handleSaveVideos,
    handleSaveVideo,
  };
}

// 1. The Trigger Button in the Header / Toolbar
export function TestGuideVideoButton({
  videoUrl,
  videos,
  isOpen,
  onToggleOpen,
  onOpenEditModal,
  isReviewMode = false,
  className = '',
  buttonTheme = 'dark',
}: {
  videoUrl: string | null | undefined;
  videos?: GuideVideoItem[];
  isOpen: boolean;
  onToggleOpen: () => void;
  onOpenEditModal: () => void;
  isReviewMode?: boolean;
  className?: string;
  buttonTheme?: 'dark' | 'light';
}) {
  const count = videos && videos.length > 0 ? videos.length : (videoUrl && videoUrl.trim() !== '' ? 1 : 0);
  const hasVideo = count > 0;

  return (
    <div className={`flex items-center gap-1.5 ${className}`}>
      {hasVideo ? (
        <>
          <button
            type="button"
            onClick={onToggleOpen}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-[12px] font-bold transition-all shadow-sm active:scale-95 ${
              isOpen
                ? 'bg-amber-500 hover:bg-amber-600 text-white'
                : buttonTheme === 'dark'
                ? 'bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 text-white border border-blue-400/30'
                : 'bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white'
            }`}
            title={isOpen ? 'Đóng video hướng dẫn' : `Bật video hướng dẫn & gợi ý cách giải (${count} video)`}
          >
            <span className="text-[13px]">{isOpen ? '⏹' : '🎬'}</span>
            <span>
              {isOpen
                ? 'Đóng Video'
                : `${isReviewMode ? 'Video chữa đề' : 'Video gợi ý / giải'}${count > 1 ? ` (${count})` : ''}`}
            </span>
            {!isOpen && (
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping ml-0.5"></span>
            )}
          </button>

          <button
            type="button"
            onClick={onOpenEditModal}
            className={`p-1.5 rounded-lg text-[12px] transition ${
              buttonTheme === 'dark'
                ? 'text-slate-400 hover:text-white hover:bg-white/10'
                : 'text-slate-500 hover:text-slate-800 hover:bg-slate-200'
            }`}
            title="Quản lý / Thêm nhiều video hướng dẫn"
          >
            ⚙️
          </button>
        </>
      ) : (
        <button
          type="button"
          onClick={onOpenEditModal}
          className={`flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-[11px] font-bold transition border border-dashed active:scale-95 ${
            buttonTheme === 'dark'
              ? 'text-slate-400 hover:text-white hover:bg-white/10 border-slate-600'
              : 'text-slate-500 hover:text-blue-600 hover:bg-blue-50 border-slate-300'
          }`}
          title="Tải lên hoặc dán link video hướng dẫn cho đề thi này"
        >
          <span>➕</span>
          <span>Thêm Video gợi ý</span>
        </button>
      )}
    </div>
  );
}

// 2. The Video Player View (Single Unified DOM Element across Inline & Theater Modal -> Zero Dual Audio & Seamless Playback)
export function TestGuideVideoPlayer({
  videoUrl,
  videos,
  activeVideoIndex = 0,
  onSelectVideo,
  isOpen,
  onClose,
  isTheaterOpen,
  onToggleTheater,
  testTitle,
}: {
  videoUrl: string | null | undefined;
  videos?: GuideVideoItem[];
  activeVideoIndex?: number;
  onSelectVideo?: (index: number) => void;
  isOpen: boolean;
  onClose: () => void;
  isTheaterOpen: boolean;
  onToggleTheater: (open: boolean) => void;
  testTitle?: string;
}) {
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const iframeRef = useRef<HTMLIFrameElement | null>(null);
  const prevIsOpenRef = useRef<boolean>(isOpen);

  const effectiveVideos = useMemo<GuideVideoItem[]>(() => {
    if (videos && videos.length > 0) return videos;
    if (videoUrl && videoUrl.trim()) {
      return [{ id: 'v_1', title: 'Video hướng dẫn & gợi ý giải bài', url: videoUrl.trim() }];
    }
    return [];
  }, [videos, videoUrl]);

  const safeIdx = activeVideoIndex < effectiveVideos.length ? activeVideoIndex : 0;
  const activeItem = effectiveVideos[safeIdx] || null;
  const sourceInfo = useMemo(() => parseVideoSource(activeItem?.url || videoUrl), [activeItem, videoUrl]);

  const pauseCurrentMedia = () => {
    if (videoRef.current) {
      try {
        videoRef.current.pause();
      } catch {
        // ignore
      }
    }
    if (iframeRef.current?.contentWindow && sourceInfo?.type === 'youtube') {
      try {
        iframeRef.current.contentWindow.postMessage(
          JSON.stringify({ event: 'command', func: 'pauseVideo', args: [] }),
          '*'
        );
      } catch {
        // ignore
      }
    }
  };

  // Ensure closing inline via external button (e.g. "Đóng Video" in toolbar) also closes theater & stops audio
  useEffect(() => {
    if (prevIsOpenRef.current && !isOpen) {
      pauseCurrentMedia();
      if (isTheaterOpen) {
        onToggleTheater(false);
      }
    }
    prevIsOpenRef.current = isOpen;
  }, [isOpen, isTheaterOpen, onToggleTheater]);

  // Allow Escape key to exit Theater Mode smoothly back to inline view
  useEffect(() => {
    if (!isTheaterOpen) return;
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault();
        onToggleTheater(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isTheaterOpen, onToggleTheater]);

  if (!sourceInfo) return null;

  const handleOpenTheater = () => {
    onToggleTheater(true);
    // Resume seamlessly from current position without creating a second player
    if (videoRef.current) {
      if (videoRef.current.ended) {
        videoRef.current.currentTime = 0;
      }
      if (videoRef.current.paused) {
        videoRef.current.play().catch(() => {});
      }
    } else if (iframeRef.current?.contentWindow && sourceInfo.type === 'youtube') {
      try {
        iframeRef.current.contentWindow.postMessage(
          JSON.stringify({ event: 'command', func: 'playVideo', args: [] }),
          '*'
        );
      } catch {
        // ignore
      }
    }
  };

  const handleExitTheater = () => {
    onToggleTheater(false);
  };

  const handleCloseCompletely = () => {
    pauseCurrentMedia();
    if (isTheaterOpen) {
      onToggleTheater(false);
    }
    onClose();
  };

  const renderVideoTabs = () => {
    if (effectiveVideos.length <= 1) return null;
    return (
      <div className="px-3 py-2 bg-[#1f1f23] border-b border-[#3f3f46] flex flex-wrap items-center gap-1.5">
        <span className="text-[11px] font-bold text-slate-400 mr-1 shrink-0">
          📚 Chọn video ({effectiveVideos.length}):
        </span>
        {effectiveVideos.map((v, idx) => {
          const isSelected = idx === safeIdx;
          const vSrc = parseVideoSource(v.url);
          const badge = vSrc?.type === 'youtube' ? 'YT' : vSrc?.type === 'direct' ? 'HD' : 'LINK';
          return (
            <button
              key={v.id || idx}
              type="button"
              onClick={() => onSelectVideo?.(idx)}
              className={`px-2.5 py-1 rounded-lg text-[11.5px] font-bold transition flex items-center gap-1.5 border ${
                isSelected
                  ? 'bg-blue-600 text-white border-blue-400 shadow-sm'
                  : 'bg-[#27272a] hover:bg-[#323238] text-slate-300 border-[#3f3f46]'
              }`}
            >
              <span className={`w-4 h-4 rounded-full text-[10px] flex items-center justify-center font-black ${
                isSelected ? 'bg-white text-blue-700' : 'bg-slate-700 text-slate-300'
              }`}>
                {idx + 1}
              </span>
              <span className="max-w-[240px] truncate">{v.title || `Video #${idx + 1}`}</span>
              <span className={`text-[9px] px-1.5 py-0.2 rounded font-extrabold uppercase ${
                isSelected ? 'bg-blue-800/80 text-blue-100' : 'bg-slate-800 text-slate-400'
              }`}>
                {badge}
              </span>
            </button>
          );
        })}
      </div>
    );
  };

  const renderPlayer = (isFullTheater = false) => {
    if (sourceInfo.type === 'direct') {
      return (
        <video
          key={sourceInfo.embedUrl}
          ref={videoRef}
          src={sourceInfo.embedUrl}
          controls
          autoPlay
          playsInline
          className={`w-full h-full object-contain ${isFullTheater ? 'max-h-[82vh]' : ''}`}
        >
          Trình duyệt của bạn không hỗ trợ phát video này.
        </video>
      );
    }

    return (
      <iframe
        key={sourceInfo.embedUrl}
        ref={iframeRef}
        src={sourceInfo.embedUrl}
        title={activeItem?.title || 'Video hướng dẫn & gợi ý'}
        referrerPolicy="strict-origin-when-cross-origin"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowFullScreen
        className="w-full h-full border-0"
      />
    );
  };

  const isVisible = isOpen || isTheaterOpen;

  return (
    <>
      {/* Placeholder in inline layout while expanded to Theater Mode so scroll position stays stable */}
      {isOpen && isTheaterOpen ? (
        <div
          key="inline-theater-placeholder"
          className="w-full max-w-[860px] mx-auto my-2.5 rounded-2xl bg-slate-900/5 border border-dashed border-slate-300 aspect-video flex flex-col items-center justify-center gap-2.5 text-slate-500 text-xs font-medium shrink-0"
        >
          <span>🎬 Video đang phát ở chế độ phóng to toàn màn hình</span>
          <button
            type="button"
            onClick={handleExitTheater}
            className="px-3 py-1.5 bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 rounded-lg text-[11.5px] font-bold transition shadow-sm cursor-pointer"
          >
            🗗 Thu nhỏ về khung này
          </button>
        </div>
      ) : null}

      {/* SINGLE UNIFIED PLAYER: keeps exact same <video> / <iframe> DOM instance between Inline and Theater */}
      {isVisible ? (
        <div
          key="unified-guide-video-container"
          className={
            isTheaterOpen
              ? 'fixed inset-0 z-[110] bg-black/90 backdrop-blur-md flex flex-col p-4 sm:p-6'
              : 'w-full max-w-[860px] mx-auto my-2.5 rounded-2xl bg-[#18181b] border border-slate-700/80 shadow-xl overflow-hidden shrink-0'
          }
        >
          <div
            key="player-header"
            className={
              isTheaterOpen
                ? 'flex justify-between items-center text-white mb-2 px-2 shrink-0 gap-3'
                : 'px-4 py-2.5 bg-[#27272a] border-b border-[#3f3f46] flex items-center justify-between text-white text-[12px] gap-2'
            }
          >
            {isTheaterOpen ? (
              <>
                <div className="flex items-center gap-3 truncate">
                  <span className="text-red-500 text-lg shrink-0">▶</span>
                  <h3 className="font-bold text-base sm:text-lg truncate">
                    {testTitle ? `[Video Hướng Dẫn] ${testTitle}` : (activeItem?.title || 'Video hướng dẫn & gợi ý cách giải')}
                  </h3>
                </div>
                <div className="flex items-center gap-2 shrink-0">
                  <button
                    type="button"
                    onClick={handleExitTheater}
                    className="px-3.5 py-1.5 bg-slate-700 hover:bg-slate-600 text-white rounded-lg font-bold text-xs sm:text-sm transition flex items-center gap-1.5 shadow-lg cursor-pointer"
                    title="Thu nhỏ về khung bên dưới và tiếp tục xem"
                  >
                    ✕ Thoát toàn màn hình
                  </button>
                  <button
                    type="button"
                    onClick={handleCloseCompletely}
                    className="px-3.5 py-1.5 bg-red-600 hover:bg-red-700 text-white rounded-lg font-bold text-xs sm:text-sm transition flex items-center gap-1.5 shadow-lg cursor-pointer"
                    title="Đóng hẳn video"
                  >
                    ⏹ Đóng hẳn
                  </button>
                </div>
              </>
            ) : (
              <>
                <div className="flex items-center gap-2 font-bold truncate">
                  <span className="w-2 h-2 rounded-full bg-red-500 animate-pulse shrink-0" />
                  <span className="truncate">{activeItem?.title || 'Video hướng dẫn & gợi ý giải bài'}</span>
                  <span className="text-[10px] font-semibold px-2 py-0.5 rounded-md bg-sky-500/20 text-sky-300 border border-sky-400/30 uppercase tracking-wider shrink-0">
                    {sourceInfo.type === 'youtube' ? 'YouTube' : sourceInfo.type === 'drive' ? 'Google Drive' : sourceInfo.type === 'direct' ? 'Full HD 1080p' : 'Embed'}
                  </span>
                </div>
                <div className="flex items-center gap-2 shrink-0">
                  <button
                    type="button"
                    onClick={handleOpenTheater}
                    className="px-2.5 py-1 bg-white/10 hover:bg-white/20 text-slate-200 hover:text-white rounded-lg text-[11px] font-semibold transition flex items-center gap-1 cursor-pointer"
                    title="Mở toàn màn hình và phát tiếp từ chỗ đang xem"
                  >
                    <span>⛶</span> Phóng to
                  </button>
                  <button
                    type="button"
                    onClick={handleCloseCompletely}
                    className="px-2.5 py-1 text-slate-400 hover:text-red-400 hover:bg-white/10 rounded-lg transition font-bold cursor-pointer"
                    title="Đóng video"
                  >
                    ✕ Đóng
                  </button>
                </div>
              </>
            )}
          </div>

          <div
            key="player-tabs"
            className={
              effectiveVideos.length <= 1
                ? 'hidden'
                : isTheaterOpen
                ? 'w-full max-w-5xl mx-auto mb-2 rounded-xl overflow-hidden border border-slate-700 shrink-0'
                : 'w-full shrink-0'
            }
          >
            {renderVideoTabs()}
          </div>

          <div
            key="player-stage"
            className={
              isTheaterOpen
                ? 'flex-1 w-full max-w-5xl mx-auto aspect-video max-h-[calc(100vh-96px)] min-h-0 bg-black rounded-xl overflow-hidden shadow-2xl border border-slate-800 flex items-center justify-center'
                : 'relative w-full aspect-video bg-black flex items-center justify-center'
            }
          >
            {renderPlayer(isTheaterOpen)}
          </div>
        </div>
      ) : null}
    </>
  );
}

// 3. Multi-Video Manager Modal (Add / Upload / Reorder / Keep Existing Videos)
export function TestGuideVideoEditModal({
  isOpen,
  onClose,
  initialUrl,
  initialVideos,
  onSave,
  onSaveVideos,
  testTitle,
}: {
  isOpen: boolean;
  onClose: () => void;
  initialUrl?: string | null | undefined;
  initialVideos?: GuideVideoItem[];
  onSave?: (url: string | null) => Promise<void>;
  onSaveVideos?: (videos: GuideVideoItem[]) => Promise<void>;
  testTitle?: string;
}) {
  const [items, setItems] = useState<GuideVideoItem[]>([]);
  const [previewIdx, setPreviewIdx] = useState<number>(0);
  const [isUploading, setIsUploading] = useState(false);
  const [uploadPercent, setUploadPercent] = useState(0);
  const [isSaving, setIsSaving] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (isOpen) {
      let seed: GuideVideoItem[] = [];
      if (initialVideos && initialVideos.length > 0) {
        seed = initialVideos.map((v, i) => ({
          id: v.id || `v_${i + 1}`,
          title: v.title || `Video hướng dẫn #${i + 1}`,
          url: v.url || '',
        }));
      } else if (initialUrl && initialUrl.trim()) {
        seed = [{ id: 'v_1', title: 'Video hướng dẫn #1', url: initialUrl.trim() }];
      } else {
        seed = [{ id: `v_${Date.now()}`, title: 'Video hướng dẫn #1', url: '' }];
      }
      setItems(seed);
      setPreviewIdx(0);
      setErrorMessage(null);
      setSuccessMessage(null);
      setIsUploading(false);
      setIsSaving(false);
      setUploadPercent(0);
    }
  }, [isOpen, initialVideos, initialUrl]);

  const activePreviewUrl = items[previewIdx]?.url || '';
  const previewSource = useMemo(() => parseVideoSource(activePreviewUrl), [activePreviewUrl]);

  if (!isOpen) return null;

  const addEmptySlot = () => {
    const nextNum = items.length + 1;
    const next = [...items, { id: `v_${Date.now()}_${nextNum}`, title: `Video hướng dẫn #${nextNum}`, url: '' }];
    setItems(next);
    setPreviewIdx(next.length - 1);
  };

  const updateItem = (idx: number, field: 'title' | 'url', val: string) => {
    setItems((prev) => prev.map((it, i) => (i === idx ? { ...it, [field]: val } : it)));
    setPreviewIdx(idx);
  };

  const removeItem = (idx: number) => {
    setItems((prev) => {
      const next = prev.filter((_, i) => i !== idx);
      return next.length > 0 ? next : [{ id: `v_${Date.now()}`, title: 'Video hướng dẫn #1', url: '' }];
    });
    setPreviewIdx(0);
  };

  const moveItem = (idx: number, dir: -1 | 1) => {
    const target = idx + dir;
    if (target < 0 || target >= items.length) return;
    const next = [...items];
    const tmp = next[idx];
    next[idx] = next[target];
    next[target] = tmp;
    setItems(next);
    setPreviewIdx(target);
  };

  const handleFileUpload = async (file: File) => {
    if (!file) return;
    const isVideo = file.type.startsWith('video/') || /\.(mp4|webm|mov|m4v|ogg)$/i.test(file.name);
    if (!isVideo) {
      setErrorMessage('⚠️ Vui lòng chỉ tải lên file định dạng video (.mp4, .webm, .mov)!');
      return;
    }

    setErrorMessage(null);
    setIsUploading(true);
    setUploadPercent(15);

    try {
      const cleanName = file.name.replace(/[^a-zA-Z0-9._-]/g, '_');
      const storagePath = `videos/guide_${Date.now()}_${cleanName}`;

      setUploadPercent(35);
      const { error: uploadError } = await supabase.storage
        .from('test_assets')
        .upload(storagePath, file, {
          cacheControl: '3600',
          upsert: false,
          contentType: file.type || 'video/mp4',
        });

      if (uploadError) throw uploadError;

      setUploadPercent(85);
      const { data: urlData } = supabase.storage.from('test_assets').getPublicUrl(storagePath);
      const publicUrl = urlData?.publicUrl;

      if (!publicUrl) throw new Error('Không lấy được link public từ storage.');

      setUploadPercent(100);
      const baseTitle = file.name.replace(/\.[^.]+$/, '');

      // Fill an empty slot if one exists; otherwise APPEND a new video so existing videos are preserved!
      setItems((prev) => {
        const emptyIndex = prev.findIndex((x) => !x.url.trim());
        if (emptyIndex >= 0) {
          const updated = [...prev];
          updated[emptyIndex] = {
            ...updated[emptyIndex],
            title: updated[emptyIndex].title || baseTitle,
            url: publicUrl,
          };
          setPreviewIdx(emptyIndex);
          return updated;
        }
        const appended = [
          ...prev,
          { id: `v_${Date.now()}`, title: baseTitle || `Video hướng dẫn #${prev.length + 1}`, url: publicUrl },
        ];
        setPreviewIdx(appended.length - 1);
        return appended;
      });

      setSuccessMessage('✅ Đã tải video mới lên và thêm vào danh sách (giữ nguyên các video cũ)!');
    } catch (err: any) {
      console.error('Upload video error:', err);
      setErrorMessage('❌ Lỗi upload video: ' + (err.message || 'Không thể tải file lên'));
    } finally {
      setIsUploading(false);
      if (fileInputRef.current) fileInputRef.current.value = '';
    }
  };

  const handleSave = async () => {
    setIsSaving(true);
    setErrorMessage(null);
    try {
      const validList = items
        .map((it, i) => ({
          id: it.id || `v_${i + 1}`,
          title: it.title.trim() || `Video hướng dẫn #${i + 1}`,
          url: it.url.trim(),
        }))
        .filter((it) => it.url !== '');

      if (onSaveVideos) {
        await onSaveVideos(validList);
      } else if (onSave) {
        await onSave(validList[0]?.url || null);
      }

      setSuccessMessage(`Đã lưu ${validList.length} video hướng dẫn thành công!`);
      setTimeout(() => {
        onClose();
      }, 450);
    } catch (err: any) {
      console.error('Save videos error:', err);
      setErrorMessage('❌ Không thể lưu danh sách video: ' + (err.message || 'Đã có lỗi xảy ra'));
    } finally {
      setIsSaving(false);
    }
  };

  const handleClearAll = async () => {
    if (!window.confirm('Bạn có chắc chắn muốn xóa TẤT CẢ video hướng dẫn của đề này?')) return;
    setIsSaving(true);
    try {
      if (onSaveVideos) {
        await onSaveVideos([]);
      } else if (onSave) {
        await onSave(null);
      }
      setSuccessMessage('Đã xóa toàn bộ video!');
      setTimeout(() => onClose(), 450);
    } catch (err: any) {
      setErrorMessage('Lỗi khi xóa video: ' + err.message);
    } finally {
      setIsSaving(false);
    }
  };

  const hasAnySavedVideo = (initialVideos && initialVideos.length > 0) || !!(initialUrl && initialUrl.trim());

  return (
    <div className="fixed inset-0 z-[120] bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 animate-in fade-in">
      <div className="bg-white rounded-2xl shadow-2xl border border-slate-200 w-full max-w-2xl overflow-hidden flex flex-col max-h-[92vh]">
        {/* Header */}
        <div className="px-6 py-4 bg-slate-900 text-white flex justify-between items-center">
          <div className="flex items-center gap-2.5">
            <span className="text-xl">🎬</span>
            <div>
              <h3 className="font-bold text-base">Quản lý Danh sách Video Hướng Dẫn & Giải Đề</h3>
              <p className="text-[11px] text-slate-400 truncate max-w-md">
                {testTitle || 'Hỗ trợ gắn nhiều video cùng lúc (YouTube, Google Drive, MP4...)'}
              </p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="text-slate-400 hover:text-white text-xl font-bold p-1 transition"
          >
            ✕
          </button>
        </div>

        {/* Content */}
        <div className="p-5 overflow-y-auto space-y-4 flex-1">
          {errorMessage && (
            <div className="p-3 bg-red-50 border border-red-200 text-red-700 text-[13px] rounded-xl flex items-center gap-2">
              <span>⚠️</span>
              <span className="flex-1">{errorMessage}</span>
            </div>
          )}

          {successMessage && (
            <div className="p-3 bg-emerald-50 border border-emerald-200 text-emerald-700 text-[13px] rounded-xl flex items-center gap-2">
              <span>✅</span>
              <span className="flex-1">{successMessage}</span>
            </div>
          )}

          {/* Video List */}
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <label className="text-[13px] font-extrabold text-slate-700 uppercase tracking-wide">
                Danh sách Video ({items.filter((x) => x.url.trim()).length} video hợp lệ)
              </label>
              <button
                type="button"
                onClick={addEmptySlot}
                className="px-3 py-1.5 bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-200 rounded-lg text-[12px] font-bold transition flex items-center gap-1"
              >
                ➕ Thêm link Video khác
              </button>
            </div>

            {items.map((item, idx) => {
              const isPreviewing = idx === previewIdx;
              return (
                <div
                  key={item.id || idx}
                  className={`p-3.5 rounded-xl border transition ${
                    isPreviewing ? 'bg-blue-50/40 border-blue-300' : 'bg-slate-50 border-slate-200'
                  }`}
                >
                  <div className="flex items-center justify-between gap-2 mb-2">
                    <div className="flex items-center gap-2 flex-1">
                      <span className="w-6 h-6 rounded-full bg-slate-800 text-white text-[11px] font-black flex items-center justify-center shrink-0">
                        {idx + 1}
                      </span>
                      <input
                        type="text"
                        value={item.title}
                        onChange={(e) => updateItem(idx, 'title', e.target.value)}
                        placeholder={`Tên hiển thị (VD: Video ${idx + 1} - Chữa chi tiết từng câu)`}
                        className="flex-1 px-2.5 py-1.5 bg-white border border-slate-300 rounded-lg text-[13px] font-bold text-slate-800 outline-none focus:ring-2 focus:ring-blue-500"
                      />
                    </div>
                    <div className="flex items-center gap-1 shrink-0">
                      <button
                        type="button"
                        onClick={() => setPreviewIdx(idx)}
                        className={`px-2 py-1 rounded text-[11px] font-bold transition ${
                          isPreviewing ? 'bg-blue-600 text-white' : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-100'
                        }`}
                        title="Xem trước video này"
                      >
                        👁 Xem
                      </button>
                      <button
                        type="button"
                        onClick={() => moveItem(idx, -1)}
                        disabled={idx === 0}
                        className="px-1.5 py-1 bg-white border border-slate-200 rounded text-[11px] text-slate-600 hover:bg-slate-100 disabled:opacity-30"
                        title="Đưa lên trên"
                      >
                        ↑
                      </button>
                      <button
                        type="button"
                        onClick={() => moveItem(idx, 1)}
                        disabled={idx === items.length - 1}
                        className="px-1.5 py-1 bg-white border border-slate-200 rounded text-[11px] text-slate-600 hover:bg-slate-100 disabled:opacity-30"
                        title="Đưa xuống dưới"
                      >
                        ↓
                      </button>
                      <button
                        type="button"
                        onClick={() => removeItem(idx)}
                        className="px-2 py-1 bg-white border border-red-200 text-red-600 hover:bg-red-50 rounded text-[11px] font-bold transition"
                        title="Xóa video này khỏi danh sách"
                      >
                        ✕
                      </button>
                    </div>
                  </div>

                  <input
                    type="url"
                    value={item.url}
                    onChange={(e) => updateItem(idx, 'url', e.target.value)}
                    onFocus={() => setPreviewIdx(idx)}
                    placeholder="Dán link YouTube, Google Drive hoặc link file .mp4..."
                    className="w-full px-3 py-2 bg-white border border-slate-300 rounded-lg text-[13px] outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
              );
            })}
          </div>

          {/* Drag & Drop Uploader (appends without overwriting!) */}
          <div
            onClick={() => fileInputRef.current?.click()}
            onDragOver={(e) => e.preventDefault()}
            onDrop={(e) => {
              e.preventDefault();
              const file = e.dataTransfer.files?.[0];
              if (file) handleFileUpload(file);
            }}
            className={`border-2 border-dashed rounded-xl p-4 flex items-center justify-between gap-4 cursor-pointer transition ${
              isUploading
                ? 'border-blue-400 bg-blue-50'
                : 'border-slate-300 hover:border-blue-500 bg-slate-50 hover:bg-blue-50/40'
            }`}
          >
            <input
              ref={fileInputRef}
              type="file"
              accept="video/mp4,video/webm,video/quicktime,video/x-m4v"
              onChange={(e) => {
                const file = e.target.files?.[0];
                if (file) handleFileUpload(file);
              }}
              className="hidden"
            />
            <div className="flex items-center gap-3">
              <span className="text-2xl">{isUploading ? '⏳' : '📁'}</span>
              <div>
                <p className="font-bold text-slate-700 text-[13px]">
                  {isUploading
                    ? `Đang tải video lên máy chủ (${uploadPercent}%)...`
                    : 'Tải thêm file .mp4 từ máy tính (Tự động thêm mới, giữ nguyên video cũ)'}
                </p>
                <p className="text-[11px] text-slate-500">
                  Nhấp hoặc kéo thả file .mp4 / .webm / .mov vào đây để tải lên Host
                </p>
              </div>
            </div>
            <span className="px-3 py-1.5 bg-white border border-slate-300 rounded-lg text-[12px] font-bold text-slate-700 shrink-0">
              Chọn tệp
            </span>
          </div>

          {/* Live Preview of Selected Video */}
          {previewSource && (
            <div className="p-3 bg-slate-50 border border-slate-200 rounded-xl">
              <div className="flex items-center justify-between mb-2">
                <span className="text-[11px] font-bold uppercase tracking-wider text-slate-600">
                  Đang xem trước #{previewIdx + 1}: {items[previewIdx]?.title}
                </span>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-blue-100 text-blue-700 uppercase">
                  {previewSource.type}
                </span>
              </div>
              <div className="aspect-video w-full bg-black rounded-lg overflow-hidden max-h-[210px]">
                {previewSource.type === 'direct' ? (
                  <video key={previewSource.embedUrl} src={previewSource.embedUrl} controls className="w-full h-full object-contain" />
                ) : (
                  <iframe
                    key={previewSource.embedUrl}
                    src={previewSource.embedUrl}
                    referrerPolicy="strict-origin-when-cross-origin"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    className="w-full h-full border-0"
                    title="Preview"
                  />
                )}
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="px-6 py-3.5 bg-slate-50 border-t border-slate-200 flex justify-between items-center gap-3">
          {hasAnySavedVideo ? (
            <button
              type="button"
              onClick={handleClearAll}
              disabled={isSaving || isUploading}
              className="px-3 py-2 text-red-600 hover:bg-red-50 rounded-xl text-[12.5px] font-bold transition disabled:opacity-50"
            >
              🗑 Xóa tất cả
            </button>
          ) : (
            <div></div>
          )}

          <div className="flex items-center gap-2.5">
            <button
              type="button"
              onClick={onClose}
              disabled={isSaving || isUploading}
              className="px-4 py-2 border border-slate-300 hover:bg-white text-slate-700 rounded-xl text-[13px] font-bold transition"
            >
              Hủy
            </button>
            <button
              type="button"
              onClick={handleSave}
              disabled={isSaving || isUploading}
              className="px-5 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-xl text-[13px] font-bold transition shadow-sm disabled:opacity-50 flex items-center gap-2"
            >
              {isSaving ? 'Đang lưu...' : '💾 Lưu danh sách Video'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

// 4. Combined All-in-One Component
export default function TestGuideVideo({
  testData,
  onVideoChange,
  isReviewMode = false,
  buttonTheme = 'dark',
  className = '',
}: {
  testData: any;
  onVideoChange?: (url: string | null, videos?: GuideVideoItem[]) => void;
  isReviewMode?: boolean;
  buttonTheme?: 'dark' | 'light';
  className?: string;
}) {
  const {
    videos,
    activeVideoIndex,
    setActiveVideoIndex,
    videoUrl,
    isOpen,
    setIsOpen,
    isTheaterOpen,
    setIsTheaterOpen,
    isEditModalOpen,
    setIsEditModalOpen,
    handleSaveVideos,
  } = useTestGuideVideo(testData, onVideoChange);

  return (
    <div className={className}>
      <TestGuideVideoButton
        videoUrl={videoUrl}
        videos={videos}
        isOpen={isOpen}
        onToggleOpen={() => setIsOpen(!isOpen)}
        onOpenEditModal={() => setIsEditModalOpen(true)}
        isReviewMode={isReviewMode}
        buttonTheme={buttonTheme}
      />

      <TestGuideVideoPlayer
        videoUrl={videoUrl}
        videos={videos}
        activeVideoIndex={activeVideoIndex}
        onSelectVideo={setActiveVideoIndex}
        isOpen={isOpen}
        onClose={() => setIsOpen(false)}
        isTheaterOpen={isTheaterOpen}
        onToggleTheater={setIsTheaterOpen}
        testTitle={testData?.title}
      />

      <TestGuideVideoEditModal
        isOpen={isEditModalOpen}
        onClose={() => setIsEditModalOpen(false)}
        initialUrl={videoUrl}
        initialVideos={videos}
        onSaveVideos={handleSaveVideos}
        testTitle={testData?.title}
      />
    </div>
  );
}


// 5. Reusable Multi-Video Form Field for Admin Editor Modals (CaseStudy, MCQ, IGCSE)
export function GuideVideoListField({
  videos,
  legacyUrl,
  onChange,
}: {
  videos?: GuideVideoItem[];
  legacyUrl?: string | null;
  onChange: (primaryUrl: string, nextVideos: GuideVideoItem[]) => void;
}) {
  const [isUploading, setIsUploading] = useState(false);
  const fileRef = useRef<HTMLInputElement>(null);

  const list: GuideVideoItem[] = useMemo(() => {
    if (Array.isArray(videos) && videos.length > 0) return videos;
    if (legacyUrl && legacyUrl.trim()) {
      return [{ id: 'v_1', title: 'Video hướng dẫn #1', url: legacyUrl.trim() }];
    }
    return [{ id: 'v_1', title: 'Video hướng dẫn #1', url: '' }];
  }, [videos, legacyUrl]);

  const emit = (next: GuideVideoItem[]) => {
    const nonEmpty = next.filter((x) => x.url.trim() !== '');
    const primary = nonEmpty[0]?.url?.trim() || '';
    onChange(primary, next);
  };

  const handleUpload = async (file: File) => {
    if (!file) return;
    setIsUploading(true);
    try {
      const cleanName = file.name.replace(/[^a-zA-Z0-9._-]/g, '_');
      const storagePath = `videos/guide_${Date.now()}_${cleanName}`;
      const { error } = await supabase.storage.from('test_assets').upload(storagePath, file, {
        cacheControl: '3600',
        upsert: false,
        contentType: file.type || 'video/mp4',
      });
      if (error) throw error;
      const { data } = supabase.storage.from('test_assets').getPublicUrl(storagePath);
      const publicUrl = data?.publicUrl || '';
      const baseTitle = file.name.replace(/\.[^.]+$/, '');
      const emptyIdx = list.findIndex((x) => !x.url.trim());
      if (emptyIdx >= 0) {
        const next = [...list];
        next[emptyIdx] = { ...next[emptyIdx], title: next[emptyIdx].title || baseTitle, url: publicUrl };
        emit(next);
      } else {
        emit([...list, { id: `v_${Date.now()}`, title: baseTitle || `Video hướng dẫn #${list.length + 1}`, url: publicUrl }]);
      }
    } catch (e: any) {
      alert('Lỗi tải video lên: ' + (e.message || e));
    } finally {
      setIsUploading(false);
      if (fileRef.current) fileRef.current.value = '';
    }
  };

  return (
    <div className="space-y-2.5">
      <div className="flex items-center justify-between">
        <label className="text-[12.5px] font-bold text-slate-600">
          🎬 Danh sách Video hướng dẫn & gợi ý <span className="text-slate-400 font-normal">(Hỗ trợ nhiều video)</span>
        </label>
        <div className="flex items-center gap-1.5">
          <input
            ref={fileRef}
            type="file"
            accept="video/mp4,video/webm,video/quicktime"
            onChange={(e) => { const f = e.target.files?.[0]; if (f) handleUpload(f); }}
            className="hidden"
          />
          <button
            type="button"
            onClick={() => fileRef.current?.click()}
            disabled={isUploading}
            className="px-2.5 py-1 bg-emerald-50 hover:bg-emerald-100 text-emerald-700 border border-emerald-200 rounded-lg text-[11.5px] font-bold transition"
          >
            {isUploading ? '⏳ Đang tải...' : '📁 Tải .mp4'}
          </button>
          <button
            type="button"
            onClick={() => emit([...list, { id: `v_${Date.now()}`, title: `Video hướng dẫn #${list.length + 1}`, url: '' }])}
            className="px-2.5 py-1 bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-200 rounded-lg text-[11.5px] font-bold transition"
          >
            ➕ Thêm Video
          </button>
        </div>
      </div>

      {list.map((item, idx) => (
        <div key={item.id || idx} className="p-2.5 bg-slate-50 border border-slate-200 rounded-xl space-y-1.5">
          <div className="flex items-center gap-2">
            <span className="w-5 h-5 rounded-full bg-slate-700 text-white text-[10px] font-black flex items-center justify-center shrink-0">
              {idx + 1}
            </span>
            <input
              type="text"
              value={item.title}
              onChange={(e) => {
                const next = [...list];
                next[idx] = { ...next[idx], title: e.target.value };
                emit(next);
              }}
              placeholder={`Tên hiển thị (VD: Video #${idx + 1} - Chữa chi tiết)`}
              className="flex-1 px-2.5 py-1 bg-white border border-slate-200 rounded-lg text-[12.5px] font-semibold outline-none focus:border-blue-500"
            />
            {list.length > 1 && (
              <button
                type="button"
                onClick={() => emit(list.filter((_, i) => i !== idx))}
                className="px-2 py-1 text-red-500 hover:bg-red-50 rounded text-[11px] font-bold"
                title="Xóa video này"
              >
                ✕
              </button>
            )}
          </div>
          <input
            type="text"
            value={item.url}
            onChange={(e) => {
              const next = [...list];
              next[idx] = { ...next[idx], url: e.target.value };
              emit(next);
            }}
            placeholder="Dán link YouTube, Google Drive hoặc link file .mp4..."
            className="w-full px-2.5 py-1.5 bg-white border border-slate-200 rounded-lg text-[13px] outline-none focus:border-blue-500"
          />
        </div>
      ))}
    </div>
  );
}
