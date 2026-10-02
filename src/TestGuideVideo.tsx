import React, { useState, useRef, useEffect, useMemo } from 'react';
import { supabase } from './supabase';

export interface VideoSourceInfo {
  type: 'youtube' | 'drive' | 'direct' | 'loom' | 'vimeo' | 'iframe';
  embedUrl: string;
  originalUrl: string;
}

export function parseVideoSource(rawUrl: string | null | undefined): VideoSourceInfo | null {
  if (!rawUrl || typeof rawUrl !== 'string') return null;
  const url = rawUrl.trim();
  if (!url) return null;

  // 1. YouTube
  const ytMatch = url.match(/(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=|shorts\/))([\w-]{11})/i);
  if (ytMatch && ytMatch[1]) {
    return {
      type: 'youtube',
      embedUrl: `https://www.youtube-nocookie.com/embed/${ytMatch[1]}?autoplay=1&rel=0`,
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

export async function saveTestGuideVideo(testId: string, newVideoUrl: string | null) {
  if (!testId) throw new Error('Test ID is required');

  const { data: currentTest, error: fetchErr } = await supabase
    .from('tests')
    .select('id, content_json, json_config')
    .eq('id', testId)
    .single();

  if (fetchErr) {
    console.error('Error fetching test before saving video:', fetchErr);
    throw fetchErr;
  }

  const currentContentJson = currentTest?.content_json || {};
  const currentBasicInfo = currentContentJson?.basicInfo || {};
  const currentJsonConfig = currentTest?.json_config || {};

  const updatedContentJson = {
    ...currentContentJson,
    guide_video_url: newVideoUrl || null,
    basicInfo: {
      ...currentBasicInfo,
      guide_video_url: newVideoUrl || null,
    }
  };

  const updatedJsonConfig = {
    ...currentJsonConfig,
    guide_video_url: newVideoUrl || null,
  };

  const { error: updateErr } = await supabase
    .from('tests')
    .update({
      content_json: updatedContentJson,
      json_config: updatedJsonConfig,
    })
    .eq('id', testId);

  if (updateErr) {
    console.error('Error updating test guide video URL:', updateErr);
    throw updateErr;
  }

  // Update sessionStorage if current test is cached
  try {
    const saved = sessionStorage.getItem('lms_current_test');
    if (saved) {
      const parsed = JSON.parse(saved);
      if (parsed && (parsed.id === testId || !parsed.id)) {
        parsed.content_json = updatedContentJson;
        parsed.json_config = updatedJsonConfig;
        parsed.guide_video_url = newVideoUrl || null;
        sessionStorage.setItem('lms_current_test', JSON.stringify(parsed));
      }
    }
  } catch (e) {
    console.warn('Could not update sessionStorage cache:', e);
  }

  return { content_json: updatedContentJson, json_config: updatedJsonConfig };
}

// Hook to manage video state and operations
export function useTestGuideVideo(testData: any, onVideoChange?: (url: string | null) => void) {
  const testId = testData?.id || '';
  const initialUrl = 
    testData?.guide_video_url ||
    testData?.content_json?.guide_video_url ||
    testData?.content_json?.basicInfo?.guide_video_url ||
    testData?.json_config?.guide_video_url ||
    null;

  const [videoUrl, setVideoUrl] = useState<string | null>(initialUrl);
  const [isOpen, setIsOpen] = useState(false);
  const [isTheaterOpen, setIsTheaterOpen] = useState(false);
  const [isEditModalOpen, setIsEditModalOpen] = useState(false);

  useEffect(() => {
    const currentUrl = 
      testData?.guide_video_url ||
      testData?.content_json?.guide_video_url ||
      testData?.content_json?.basicInfo?.guide_video_url ||
      testData?.json_config?.guide_video_url ||
      null;
    setVideoUrl(currentUrl);
  }, [testData]);

  const handleSaveVideo = async (newUrl: string | null) => {
    if (testId) {
      await saveTestGuideVideo(testId, newUrl);
    }
    setVideoUrl(newUrl);
    if (onVideoChange) {
      onVideoChange(newUrl);
    }
  };

  return {
    testId,
    videoUrl,
    setVideoUrl,
    isOpen,
    setIsOpen,
    isTheaterOpen,
    setIsTheaterOpen,
    isEditModalOpen,
    setIsEditModalOpen,
    handleSaveVideo,
  };
}

// 1. The Trigger Button in the Header / Toolbar
export function TestGuideVideoButton({
  videoUrl,
  isOpen,
  onToggleOpen,
  onOpenEditModal,
  isReviewMode = false,
  className = '',
  buttonTheme = 'dark',
}: {
  videoUrl: string | null | undefined;
  isOpen: boolean;
  onToggleOpen: () => void;
  onOpenEditModal: () => void;
  isReviewMode?: boolean;
  className?: string;
  buttonTheme?: 'dark' | 'light';
}) {
  const hasVideo = !!videoUrl && videoUrl.trim() !== '';

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
            title={isOpen ? 'Đóng video hướng dẫn' : 'Bật video hướng dẫn & gợi ý cách giải'}
          >
            <span className="text-[13px]">{isOpen ? '⏹' : '🎬'}</span>
            <span>{isOpen ? 'Đóng Video' : (isReviewMode ? 'Video chữa đề' : 'Video gợi ý / giải')}</span>
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
            title="Sửa hoặc thay đổi video hướng dẫn"
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

// 2. The Video Player View (Inline & Theater Modal)
export function TestGuideVideoPlayer({
  videoUrl,
  isOpen,
  onClose,
  isTheaterOpen,
  onToggleTheater,
  testTitle,
}: {
  videoUrl: string | null | undefined;
  isOpen: boolean;
  onClose: () => void;
  isTheaterOpen: boolean;
  onToggleTheater: (open: boolean) => void;
  testTitle?: string;
}) {
  const sourceInfo = useMemo(() => parseVideoSource(videoUrl), [videoUrl]);

  if (!sourceInfo) return null;

  const renderPlayer = (isFullTheater = false) => {
    if (sourceInfo.type === 'direct') {
      return (
        <video
          src={sourceInfo.embedUrl}
          controls
          autoPlay
          playsInline
          className={`w-full h-full object-contain ${isFullTheater ? 'max-h-[80vh]' : 'max-h-[380px]'}`}
        >
          Trình duyệt của bạn không hỗ trợ phát video này.
        </video>
      );
    }

    return (
      <iframe
        src={sourceInfo.embedUrl}
        title="Video hướng dẫn & gợi ý"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowFullScreen
        className="w-full h-full border-0"
      />
    );
  };

  return (
    <>
      {/* INLINE COLLAPSIBLE PLAYER */}
      {isOpen && (
        <div className="w-full bg-[#18181b] border-b border-slate-700 shadow-xl overflow-hidden shrink-0 animate-in slide-in-from-top-2 duration-200">
          <div className="px-4 py-2 bg-[#27272a] border-b border-[#3f3f46] flex items-center justify-between text-white text-[12px]">
            <div className="flex items-center gap-2 font-bold truncate">
              <span className="text-red-500 animate-pulse text-sm">▶</span>
              <span className="truncate">Video hướng dẫn & gợi ý giải bài</span>
              <span className="text-[10px] font-semibold px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30 uppercase tracking-wider">
                {sourceInfo.type === 'youtube' ? 'YouTube' : sourceInfo.type === 'drive' ? 'Google Drive' : sourceInfo.type === 'direct' ? 'Tệp Video' : 'Embed'}
              </span>
            </div>
            <div className="flex items-center gap-2 shrink-0">
              <button
                type="button"
                onClick={() => onToggleTheater(true)}
                className="px-2.5 py-1 bg-white/10 hover:bg-white/20 text-slate-200 hover:text-white rounded text-[11px] font-medium transition flex items-center gap-1"
                title="Mở toàn màn hình / Xem rộng"
              >
                <span>⛶</span> Phóng to
              </button>
              <button
                type="button"
                onClick={onClose}
                className="px-2 py-1 text-slate-400 hover:text-red-400 hover:bg-white/10 rounded transition font-bold"
                title="Đóng video"
              >
                ✕ Đóng
              </button>
            </div>
          </div>

          <div className="relative w-full aspect-video bg-black flex items-center justify-center max-h-[380px]">
            {renderPlayer(false)}
          </div>
        </div>
      )}

      {/* THEATER FULLSCREEN MODAL */}
      {isTheaterOpen && (
        <div className="fixed inset-0 z-[100] bg-black/90 backdrop-blur-md flex flex-col p-4 sm:p-6 animate-in fade-in duration-200">
          <div className="flex justify-between items-center text-white mb-3 px-2">
            <div className="flex items-center gap-3 truncate">
              <span className="text-red-500 text-lg">▶</span>
              <h3 className="font-bold text-base sm:text-lg truncate">
                {testTitle ? `[Video Hướng Dẫn] ${testTitle}` : 'Video hướng dẫn & gợi ý cách giải'}
              </h3>
            </div>
            <button
              type="button"
              onClick={() => onToggleTheater(false)}
              className="px-4 py-1.5 bg-red-600 hover:bg-red-700 text-white rounded-lg font-bold text-sm transition flex items-center gap-2 shadow-lg"
            >
              ✕ Thoát toàn màn hình
            </button>
          </div>

          <div className="flex-1 w-full max-w-5xl mx-auto aspect-video bg-black rounded-xl overflow-hidden shadow-2xl border border-slate-800 flex items-center justify-center">
            {renderPlayer(true)}
          </div>
        </div>
      )}
    </>
  );
}

// 3. The Modal to Upload Video File or Paste Video Link
export function TestGuideVideoEditModal({
  isOpen,
  onClose,
  initialUrl,
  onSave,
  testTitle,
}: {
  isOpen: boolean;
  onClose: () => void;
  initialUrl: string | null | undefined;
  onSave: (url: string | null) => Promise<void>;
  testTitle?: string;
}) {
  const [activeTab, setActiveTab] = useState<'link' | 'upload'>('link');
  const [linkInput, setLinkInput] = useState(initialUrl || '');
  const [isUploading, setIsUploading] = useState(false);
  const [uploadPercent, setUploadPercent] = useState(0);
  const [isSaving, setIsSaving] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (isOpen) {
      setLinkInput(initialUrl || '');
      setErrorMessage(null);
      setSuccessMessage(null);
      setIsUploading(false);
      setIsSaving(false);
      setUploadPercent(0);
    }
  }, [isOpen, initialUrl]);

  const previewSource = useMemo(() => parseVideoSource(linkInput), [linkInput]);

  if (!isOpen) return null;

  const handleFileUpload = async (file: File) => {
    if (!file) return;
    const isVideo = file.type.startsWith('video/') || /\.(mp4|webm|mov|m4v|ogg)$/i.test(file.name);
    if (!isVideo) {
      setErrorMessage('⚠️ Vui lòng chỉ tải lên file định dạng video (.mp4, .webm, .mov)!');
      return;
    }

    setErrorMessage(null);
    setIsUploading(true);
    setUploadPercent(10);

    try {
      const cleanName = file.name.replace(/[^a-zA-Z0-9._-]/g, '_');
      const storagePath = `videos/guide_${Date.now()}_${cleanName}`;

      setUploadPercent(30);
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
      setLinkInput(publicUrl);
      setSuccessMessage('✅ Đã tải file video lên thành công!');
      setActiveTab('link');
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
      const cleanUrl = linkInput.trim();
      await onSave(cleanUrl ? cleanUrl : null);
      setSuccessMessage('Đã lưu video thành công!');
      setTimeout(() => {
        onClose();
      }, 500);
    } catch (err: any) {
      console.error('Save video error:', err);
      setErrorMessage('❌ Không thể lưu video: ' + (err.message || 'Đã có lỗi xảy ra'));
    } finally {
      setIsSaving(false);
    }
  };

  const handleDelete = async () => {
    if (!window.confirm('Bạn có chắc chắn muốn xóa video hướng dẫn của đề này?')) return;
    setIsSaving(true);
    try {
      await onSave(null);
      setLinkInput('');
      setSuccessMessage('Đã xóa video!');
      setTimeout(() => {
        onClose();
      }, 500);
    } catch (err: any) {
      setErrorMessage('Lỗi khi xóa video: ' + err.message);
    } finally {
      setIsSaving(false);
    }
  };

  return (
    <div className="fixed inset-0 z-[120] bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 animate-in fade-in">
      <div className="bg-white rounded-2xl shadow-2xl border border-slate-200 w-full max-w-lg overflow-hidden flex flex-col max-h-[90vh]">
        {/* Header */}
        <div className="px-6 py-4 bg-slate-900 text-white flex justify-between items-center">
          <div className="flex items-center gap-2">
            <span className="text-xl">🎬</span>
            <div>
              <h3 className="font-bold text-base">Cài đặt Video Hướng Dẫn & Gợi Ý</h3>
              <p className="text-[11px] text-slate-400 truncate max-w-xs">{testTitle || 'Gợi ý cách giải bài tập'}</p>
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

        {/* Tab selection */}
        <div className="flex border-b border-slate-200 bg-slate-50 px-6 pt-3 gap-2">
          <button
            type="button"
            onClick={() => setActiveTab('link')}
            className={`pb-3 px-3 text-[13px] font-bold transition border-b-2 ${
              activeTab === 'link'
                ? 'border-blue-600 text-blue-600'
                : 'border-transparent text-slate-500 hover:text-slate-800'
            }`}
          >
            🔗 Dán link Video
          </button>
          <button
            type="button"
            onClick={() => setActiveTab('upload')}
            className={`pb-3 px-3 text-[13px] font-bold transition border-b-2 ${
              activeTab === 'upload'
                ? 'border-blue-600 text-blue-600'
                : 'border-transparent text-slate-500 hover:text-slate-800'
            }`}
          >
            📁 Tải file từ máy tính
          </button>
        </div>

        {/* Content */}
        <div className="p-6 overflow-y-auto space-y-4 flex-1">
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

          {activeTab === 'link' ? (
            <div className="space-y-4">
              <div>
                <label className="block text-[13px] font-bold text-slate-700 mb-1">
                  Đường dẫn Video (YouTube, Google Drive, MP4...)
                </label>
                <div className="relative">
                  <input
                    type="url"
                    value={linkInput}
                    onChange={(e) => setLinkInput(e.target.value)}
                    placeholder="https://www.youtube.com/watch?v=... hoặc link Google Drive"
                    className="w-full p-3 pr-9 bg-slate-50 border border-slate-300 rounded-xl text-[14px] outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white transition"
                  />
                  {linkInput && (
                    <button
                      type="button"
                      onClick={() => setLinkInput('')}
                      className="absolute right-3 top-3 text-slate-400 hover:text-slate-600 text-sm font-bold"
                    >
                      ✕
                    </button>
                  )}
                </div>
                <p className="text-[11px] text-slate-500 mt-1.5 leading-relaxed">
                  💡 Hỗ trợ: <b>YouTube</b> (watch, share, shorts), <b>Google Drive</b> (quyền "Bất kỳ ai có đường link"), <b>Loom</b>, <b>Vimeo</b> hoặc link file video trực tiếp (MP4, WebM).
                </p>
              </div>

              {/* Live Preview */}
              {previewSource && (
                <div className="mt-4 p-3 bg-slate-50 border border-slate-200 rounded-xl">
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-[11px] font-bold uppercase tracking-wider text-slate-500">Xem trước video</span>
                    <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-blue-100 text-blue-700 uppercase">
                      {previewSource.type}
                    </span>
                  </div>
                  <div className="aspect-video w-full bg-black rounded-lg overflow-hidden max-h-[220px]">
                    {previewSource.type === 'direct' ? (
                      <video src={previewSource.embedUrl} controls className="w-full h-full object-contain" />
                    ) : (
                      <iframe src={previewSource.embedUrl} className="w-full h-full border-0" title="Preview" />
                    )}
                  </div>
                </div>
              )}
            </div>
          ) : (
            <div className="space-y-4">
              <div
                onClick={() => fileInputRef.current?.click()}
                onDragOver={(e) => e.preventDefault()}
                onDrop={(e) => {
                  e.preventDefault();
                  const file = e.dataTransfer.files?.[0];
                  if (file) handleFileUpload(file);
                }}
                className={`border-2 border-dashed rounded-2xl p-8 flex flex-col items-center justify-center cursor-pointer transition ${
                  isUploading
                    ? 'border-blue-400 bg-blue-50'
                    : 'border-slate-300 hover:border-blue-500 bg-slate-50 hover:bg-blue-50/50'
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

                <span className="text-4xl mb-2">{isUploading ? '⏳' : '🎬'}</span>
                <p className="font-bold text-slate-700 text-sm mb-1">
                  {isUploading ? 'Đang tải video lên máy chủ...' : 'Nhấp hoặc Kéo thả file video vào đây'}
                </p>
                <p className="text-[12px] text-slate-500">Hỗ trợ các định dạng: .mp4, .webm, .mov (Tối đa 100MB)</p>

                {isUploading && (
                  <div className="w-full max-w-xs mt-4">
                    <div className="w-full bg-slate-200 rounded-full h-2.5 overflow-hidden">
                      <div
                        className="bg-blue-600 h-2.5 rounded-full transition-all duration-300"
                        style={{ width: `${uploadPercent}%` }}
                      ></div>
                    </div>
                    <p className="text-center text-[11px] font-bold text-blue-600 mt-1">{uploadPercent}%</p>
                  </div>
                )}
              </div>

              <div className="p-3 bg-amber-50 border border-amber-200 rounded-xl text-[12px] text-amber-800">
                💡 <b>Mẹo:</b> Đối với video bài giảng dài hoặc độ phân giải cao (&gt;50MB), bạn nên tải video lên YouTube (chế độ không công khai - <i>Unlisted</i>) rồi dán link sang tab <b>Dán link Video</b> để video tải nhanh và mượt hơn.
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="px-6 py-4 bg-slate-50 border-t border-slate-200 flex justify-between items-center gap-3">
          {initialUrl ? (
            <button
              type="button"
              onClick={handleDelete}
              disabled={isSaving || isUploading}
              className="px-3 py-2 text-red-600 hover:bg-red-50 rounded-xl text-[13px] font-bold transition disabled:opacity-50"
            >
              🗑 Xóa video này
            </button>
          ) : (
            <div></div>
          )}

          <div className="flex items-center gap-3">
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
              {isSaving ? 'Đang lưu...' : '💾 Lưu Video'}
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
  onVideoChange?: (url: string | null) => void;
  isReviewMode?: boolean;
  buttonTheme?: 'dark' | 'light';
  className?: string;
}) {
  const {
    videoUrl,
    isOpen,
    setIsOpen,
    isTheaterOpen,
    setIsTheaterOpen,
    isEditModalOpen,
    setIsEditModalOpen,
    handleSaveVideo,
  } = useTestGuideVideo(testData, onVideoChange);

  return (
    <div className={className}>
      <TestGuideVideoButton
        videoUrl={videoUrl}
        isOpen={isOpen}
        onToggleOpen={() => setIsOpen(!isOpen)}
        onOpenEditModal={() => setIsEditModalOpen(true)}
        isReviewMode={isReviewMode}
        buttonTheme={buttonTheme}
      />

      <TestGuideVideoPlayer
        videoUrl={videoUrl}
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
        onSave={handleSaveVideo}
        testTitle={testData?.title}
      />
    </div>
  );
}
