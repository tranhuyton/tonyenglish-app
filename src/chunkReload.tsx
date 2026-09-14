import React from 'react';

/**
 * Quản lý tự động tải lại trang khi gặp lỗi Stale Chunk / 404 Dynamic Import.
 * Xảy ra khi hệ thống triển khai bản build mới trên máy chủ, các mã băm (hash) của
 * chunk JS cũ bị xóa hoặc đổi tên khiến trình duyệt đang mở phiên cũ tải về trả về 404 (MIME HTML).
 */

const RELOAD_KEY = 'tony_chunk_reload_ts';
const RELOAD_COOLDOWN_MS = 15000; // 15 giây cooldown tránh vòng lặp reload vô tận

/**
 * Kiểm tra xem lỗi có phải do chunk/module script tải không thành công không
 */
export function isChunkLoadError(error: any): boolean {
  if (!error) return false;
  const msg = (
    (typeof error === 'string' ? error : '') ||
    error.message ||
    error.name ||
    error.stack ||
    ''
  ).toLowerCase();

  return (
    msg.includes('failed to fetch dynamically imported module') ||
    msg.includes('dynamically imported module') ||
    msg.includes('importing a module script failed') ||
    msg.includes('text/html') ||
    msg.includes('loading chunk') ||
    msg.includes('chunkloaderror') ||
    msg.includes('failed to load module script') ||
    msg.includes('error loading dynamically imported module')
  );
}

/**
 * Kích hoạt reload trang thông minh có cooldown
 * Trả về true nếu reload thành công, false nếu đang trong thời gian cooldown
 */
export function triggerChunkReload(force: boolean = false): boolean {
  try {
    const lastReload = parseInt(sessionStorage.getItem(RELOAD_KEY) || '0', 10);
    const now = Date.now();

    if (!force && now - lastReload < RELOAD_COOLDOWN_MS) {
      console.warn('[ChunkReload] Bỏ qua reload vì đang trong thời gian cooldown (15s).');
      return false;
    }

    sessionStorage.setItem(RELOAD_KEY, now.toString());
    console.info('[ChunkReload] Phát hiện chunk mã nguồn mới sau khi cập nhật hệ thống, đang tự động làm mới trang...');
    window.location.reload();
    return true;
  } catch (e) {
    window.location.reload();
    return true;
  }
}

/**
 * Lắng nghe toàn cục các sự kiện lỗi module / chunk trên window
 */
export function initChunkErrorListener(): void {
  if (typeof window === 'undefined') return;

  // 1. Vite cụ thể phát sự kiện 'vite:preloadError' khi không tải được dynamic import
  window.addEventListener('vite:preloadError', (event: any) => {
    console.warn('[VitePreloadError] Bắt được lỗi nạp trước module:', event);
    event.preventDefault?.();
    triggerChunkReload();
  });

  // 2. Bắt các promise rejection chưa được handle từ dynamic import
  window.addEventListener('unhandledrejection', (event) => {
    if (isChunkLoadError(event.reason)) {
      console.warn('[UnhandledRejection] Phát hiện lỗi nạp chunk động:', event.reason);
      triggerChunkReload();
    }
  });

  // 3. Bắt lỗi window runtime từ việc nạp script
  window.addEventListener('error', (event) => {
    if (isChunkLoadError(event.message || event.error)) {
      console.warn('[WindowError] Phát hiện lỗi script chunk:', event.message);
      triggerChunkReload();
    }
  });
}

/**
 * Bọc React.lazy với cơ chế tự phục hồi: Nếu lỗi do chunk cũ, tự động reload trang mượt mà
 * thay vì làm sập ứng dụng thành màn hình trắng.
 */
export function lazyWithRetry<T extends React.ComponentType<any>>(
  factory: () => Promise<{ default: T }>
): React.LazyExoticComponent<T> {
  return React.lazy(async () => {
    try {
      return await factory();
    } catch (error: any) {
      console.warn('[lazyWithRetry] Không thể tải component động:', error);

      if (isChunkLoadError(error)) {
        const reloaded = triggerChunkReload();
        if (reloaded) {
          // Trả về một Promise không bao giờ resolve để React giữ nguyên Suspense fallback
          // (vòng xoay "Đang tải...") trong lúc trình duyệt làm mới trang, tránh chớp nháy màn hình trắng.
          return new Promise<{ default: T }>(() => {});
        }
      }

      // Nếu không phải lỗi chunk hoặc đang trong cooldown, throw để ErrorBoundary xử lý
      throw error;
    }
  });
}

interface ErrorBoundaryProps {
  children: React.ReactNode;
  fallback?: React.ReactNode;
}

interface ErrorBoundaryState {
  hasError: boolean;
  error: any;
}

/**
 * Component Bọc Error Boundary chống màn hình trắng toàn trang
 */
export class AppErrorBoundary extends React.Component<ErrorBoundaryProps, ErrorBoundaryState> {
  constructor(props: ErrorBoundaryProps) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: any) {
    return { hasError: true, error };
  }

  componentDidCatch(error: any, errorInfo: any) {
    console.error('[AppErrorBoundary] Bắt được lỗi giao diện:', error, errorInfo);
    if (isChunkLoadError(error)) {
      triggerChunkReload();
    }
  }

  handleReload = () => {
    try {
      sessionStorage.removeItem(RELOAD_KEY);
    } catch (e) {}
    window.location.reload();
  };

  handleGoHome = () => {
    try {
      sessionStorage.removeItem('lms_current_view');
    } catch (e) {}
    window.location.href = '/';
  };

  render() {
    if (this.state.hasError) {
      if (this.props.fallback) {
        return this.props.fallback;
      }

      const isChunk = isChunkLoadError(this.state.error);

      return (
        <div className="min-h-screen bg-gradient-to-br from-slate-50 via-sky-50 to-blue-50 flex items-center justify-center p-4">
          <div className="bg-white/95 backdrop-blur-md border border-slate-200/80 shadow-2xl rounded-3xl p-8 max-w-md w-full text-center animate-in fade-in zoom-in-95 duration-300">
            <div className="w-16 h-16 rounded-2xl bg-amber-100 text-amber-600 flex items-center justify-center text-3xl mx-auto mb-5 shadow-inner">
              {isChunk ? '🔄' : '⚠️'}
            </div>
            
            <h2 className="text-xl font-black text-slate-800 mb-2">
              {isChunk ? 'Đã có bản cập nhật mới' : 'Có sự cố khi tải nội dung'}
            </h2>
            
            <p className="text-sm text-slate-600 mb-6 leading-relaxed">
              {isChunk 
                ? 'Hệ thống vừa cập nhật tính năng mới. Vui lòng bấm nút bên dưới để tải lại phiên bản mới nhất.'
                : 'Đã xảy ra lỗi tạm thời khi kết nối đến trang này. Vui lòng tải lại hoặc quay về trang chủ.'}
            </p>

            <div className="flex flex-col gap-3">
              <button
                type="button"
                onClick={this.handleReload}
                className="w-full py-3.5 px-6 rounded-xl bg-gradient-to-r from-[#0ea5e9] to-[#0284c7] hover:from-[#0284c7] hover:to-[#0369a1] text-white font-bold text-sm shadow-md hover:shadow-lg transition-all active:scale-95 flex items-center justify-center gap-2"
              >
                <span>🔄</span>
                <span>Tải lại trang ngay</span>
              </button>

              <button
                type="button"
                onClick={this.handleGoHome}
                className="w-full py-3 px-6 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-sm transition-all active:scale-95 flex items-center justify-center gap-2"
              >
                <span>🏠</span>
                <span>Quay về trang chủ</span>
              </button>
            </div>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}
