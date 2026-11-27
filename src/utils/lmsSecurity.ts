import { supabase } from '../supabase';

/**
 * Hệ thống 4 lớp bảo vệ giáo án & chống chia sẻ tài khoản cho TonyEnglish LMS
 * - Lưu metadata gọn trong `profiles.avatar_url` (JSON) -> KHÔNG cần thay đổi schema DB
 * - Tự động bỏ qua hoàn toàn cho tài khoản Admin
 * - Giữ nguyên 100% tính năng bôi đen & click đúp tra từ điển (DictionaryWidget)
 */

export interface RegisteredDeviceInfo {
  id: string;
  label: string;
  firstSeen: string;
  lastSeen: string;
}

export interface StudentSecurityConfig {
  active_session_token?: string;
  active_device_id?: string;
  active_session_at?: string;
  devices?: RegisteredDeviceInfo[];
  max_devices?: number; // Mặc định: 2 thiết bị (VD: 1 Laptop + 1 iPad/Điện thoại)
  expires_at?: string | null; // ISO string: Tự động khóa khi hết hạn (VD: Học thử 7 ngày, Gói năm 365 ngày)
  ai_monthly_limit?: number; // 0 = không giới hạn (offline/admin), 20 = học thử, 80 = gói online
  ai_usage?: {
    month: string; // YYYY-MM
    count: number;
  };
}

export type SessionCheckResult =
  | { ok: true; updatedMeta: Record<string, any>; sessionToken: string; expiresAt?: string | null }
  | {
      ok: false;
      reason: 'expired' | 'device_limit';
      expiresAt?: string | null;
      devices?: RegisteredDeviceInfo[];
      maxDevices?: number;
    };

const DEVICE_STORAGE_KEY = 'tony_lms_device_id_v1';
const SESSION_TOKEN_KEY = 'tony_lms_active_session_token';
const BURST_STORAGE_KEY = 'tony_lms_content_burst_v1';
const BURST_ALERT_COOLDOWN_KEY = 'tony_lms_burst_alert_ts';

export const DEFAULT_TRIAL_DAYS = 7;
export const DEFAULT_MAX_DEVICES = 2;
export const DEFAULT_TRIAL_AI_LIMIT = 20;
export const DEFAULT_ONLINE_AI_LIMIT = 80;

export function getOrCreateDeviceId(): string {
  try {
    const existing = localStorage.getItem(DEVICE_STORAGE_KEY);
    if (existing && existing.length >= 12) return existing;
    const rand =
      typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function'
        ? crypto.randomUUID()
        : `dev_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 12)}`;
    localStorage.setItem(DEVICE_STORAGE_KEY, rand);
    return rand;
  } catch {
    return `ephemeral_${Date.now().toString(36)}`;
  }
}

export function getCurrentDeviceLabel(): string {
  if (typeof navigator === 'undefined') return 'Unknown Device';
  const ua = navigator.userAgent || '';
  const os = /iPad/i.test(ua)
    ? 'iPad'
    : /iPhone/i.test(ua)
      ? 'iPhone'
      : /Android/i.test(ua)
        ? 'Android'
        : /Macintosh|Mac OS/i.test(ua)
          ? 'Mac'
          : /Windows/i.test(ua)
            ? 'Windows'
            : 'Device';
  const browser = /Edg\//i.test(ua)
    ? 'Edge'
    : /Chrome\//i.test(ua) && !/Edg\//i.test(ua)
      ? 'Chrome'
      : /Safari\//i.test(ua) && !/Chrome\//i.test(ua)
        ? 'Safari'
        : /Firefox\//i.test(ua)
          ? 'Firefox'
          : 'Browser';
  return `${os} • ${browser}`;
}

export function parseProfileMetaSafe(avatarUrl?: string | null): Record<string, any> {
  if (!avatarUrl) return {};
  const raw = String(avatarUrl).trim();
  if (raw.startsWith('{')) {
    try {
      const parsed = JSON.parse(raw);
      if (parsed && typeof parsed === 'object') return parsed;
    } catch {
      return {};
    }
  }
  if (raw.startsWith('http')) {
    return { account_type: 'online', provider: 'google', google_avatar: raw };
  }
  return {};
}

export function getCurrentYearMonth(): string {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`;
}

export function isAccountExpired(expiresAt?: string | null): boolean {
  if (!expiresAt) return false;
  const ms = new Date(expiresAt).getTime();
  return Number.isFinite(ms) && Date.now() > ms;
}

export function getRemainingDays(expiresAt?: string | null): number | null {
  if (!expiresAt) return null;
  const ms = new Date(expiresAt).getTime();
  if (!Number.isFinite(ms)) return null;
  const diff = ms - Date.now();
  return Math.ceil(diff / (24 * 60 * 60 * 1000));
}

/**
 * 1. Đăng ký phiên học duy nhất (Single Active Session) + Kiểm tra Hạn sử dụng & Giới hạn 2 thiết bị
 */
export async function verifyAndRegisterLmsSession(params: {
  userId: string;
  userEmail?: string;
  userFullName?: string;
  existingMeta: Record<string, any>;
  isAdmin: boolean;
  isOnlineTrialOnly: boolean;
  isOnlineStudent: boolean;
  createdAt?: string | null;
}): Promise<SessionCheckResult> {
  const {
    userId,
    userEmail,
    userFullName,
    existingMeta,
    isAdmin,
    isOnlineTrialOnly,
    isOnlineStudent,
    createdAt,
  } = params;

  if (isAdmin) {
    return { ok: true, updatedMeta: existingMeta, sessionToken: 'admin_bypass', expiresAt: null };
  }

  const nowIso = new Date().toISOString();
  const prevSec: StudentSecurityConfig = {
    ...(existingMeta.security && typeof existingMeta.security === 'object' ? existingMeta.security : {}),
  };

  // Tự động gắn hạn học thử 7 ngày cho tài khoản Online Trial mới chưa có ngày hết hạn
  let resolvedExpiresAt = prevSec.expires_at ?? null;
  if (isOnlineTrialOnly && !resolvedExpiresAt) {
    const baseMs = createdAt ? new Date(createdAt).getTime() : Date.now();
    const safeBaseMs = Number.isFinite(baseMs) ? baseMs : Date.now();
    // Nếu tài khoản cũ tạo trước khi triển khai tính năng này, cho thêm 7 ngày từ hôm nay để tránh cắt đột ngột khách đang thử
    const trialStartMs = Math.max(safeBaseMs, Date.now() - 24 * 60 * 60 * 1000);
    resolvedExpiresAt = new Date(trialStartMs + DEFAULT_TRIAL_DAYS * 24 * 60 * 60 * 1000).toISOString();
  }

  // Kiểm tra hết hạn (chỉ chặn khi đã quá hạn)
  if (isAccountExpired(resolvedExpiresAt)) {
    return {
      ok: false,
      reason: 'expired',
      expiresAt: resolvedExpiresAt,
    };
  }

  // Kiểm tra giới hạn số thiết bị (mặc định tối đa 2 thiết bị cho học viên Online; học viên Offline giới hạn thoáng 3 thiết bị)
  const maxDevices =
    typeof prevSec.max_devices === 'number' && prevSec.max_devices > 0
      ? prevSec.max_devices
      : isOnlineStudent
        ? DEFAULT_MAX_DEVICES
        : 3;

  const deviceId = getOrCreateDeviceId();
  const deviceLabel = getCurrentDeviceLabel();
  const existingDevices: RegisteredDeviceInfo[] = Array.isArray(prevSec.devices)
    ? prevSec.devices.filter((d) => d && typeof d.id === 'string')
    : [];

  const foundIdx = existingDevices.findIndex((d) => d.id === deviceId);
  if (foundIdx === -1 && existingDevices.length >= maxDevices) {
    // Ghi cảnh báo đỏ lên AdminPanel (activity_logs)
    try {
      await supabase.from('activity_logs').insert([
        {
          user_id: userId,
          action_type: 'security_alert',
          details: {
            alert_type: 'multi_device_blocked',
            message: `Cố đăng nhập thiết bị thứ ${existingDevices.length + 1}/${maxDevices} (${deviceLabel})`,
            device_label: deviceLabel,
            registered_devices: existingDevices.map((d) => d.label),
            email: userEmail || '',
            full_name: userFullName || '',
          },
        },
      ]);
    } catch {
      // ignore log errors
    }

    return {
      ok: false,
      reason: 'device_limit',
      devices: existingDevices,
      maxDevices,
    };
  }

  const nextDevices = [...existingDevices];
  if (foundIdx >= 0) {
    nextDevices[foundIdx] = {
      ...nextDevices[foundIdx],
      label: deviceLabel,
      lastSeen: nowIso,
    };
  } else {
    nextDevices.push({
      id: deviceId,
      label: deviceLabel,
      firstSeen: nowIso,
      lastSeen: nowIso,
    });
  }

  // Tạo hoặc tái sử dụng session token cho tab hiện tại để kích hoạt Single Active Session
  let sessionToken = '';
  try {
    sessionToken = sessionStorage.getItem(SESSION_TOKEN_KEY) || '';
  } catch {
    sessionToken = '';
  }
  if (!sessionToken) {
    sessionToken = `sess_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 10)}`;
    try {
      sessionStorage.setItem(SESSION_TOKEN_KEY, sessionToken);
    } catch {
      // ignore
    }
  }

  // Gắn mặc định hạn mức AI cho tài khoản Online nếu chưa thiết lập
  const defaultAiLimit =
    typeof prevSec.ai_monthly_limit === 'number'
      ? prevSec.ai_monthly_limit
      : isOnlineTrialOnly
        ? DEFAULT_TRIAL_AI_LIMIT
        : isOnlineStudent
          ? DEFAULT_ONLINE_AI_LIMIT
          : 0; // 0 = không giới hạn (học viên Offline 30tr/45tr)

  const nextSec: StudentSecurityConfig = {
    ...prevSec,
    active_session_token: sessionToken,
    active_device_id: deviceId,
    active_session_at: nowIso,
    devices: nextDevices,
    max_devices: maxDevices,
    expires_at: resolvedExpiresAt,
    ai_monthly_limit: defaultAiLimit,
    ai_usage: prevSec.ai_usage || { month: getCurrentYearMonth(), count: 0 },
  };

  const updatedMeta = {
    ...existingMeta,
    security: nextSec,
  };

  try {
    await supabase
      .from('profiles')
      .update({ avatar_url: JSON.stringify(updatedMeta) })
      .eq('id', userId);
  } catch (e) {
    console.warn('[LMS Security] Failed to persist session metadata:', e);
  }

  return {
    ok: true,
    updatedMeta,
    sessionToken,
    expiresAt: resolvedExpiresAt,
  };
}

/**
 * 2. Theo dõi Single Active Session (Realtime + Fallback Poll 45s)
 * Hễ máy khác đăng nhập bằng cùng tài khoản -> Đá ngay thiết bị hiện tại!
 */
export function startSingleSessionWatcher(params: {
  userId: string;
  sessionToken: string;
  isAdmin: boolean;
  onKicked: (reason: 'another_device' | 'expired' | 'inactive') => void;
}): () => void {
  const { userId, sessionToken, isAdmin, onKicked } = params;
  if (isAdmin || !userId || !sessionToken || sessionToken === 'admin_bypass') {
    return () => {};
  }

  let stopped = false;

  const inspectProfileRow = (row: any) => {
    if (stopped || !row) return;
    if (row.status === 'inactive') {
      stopped = true;
      onKicked('inactive');
      return;
    }
    const meta = parseProfileMetaSafe(row.avatar_url);
    const sec: StudentSecurityConfig = meta.security || {};
    if (isAccountExpired(sec.expires_at)) {
      stopped = true;
      onKicked('expired');
      return;
    }
    if (sec.active_session_token && sec.active_session_token !== sessionToken) {
      stopped = true;
      onKicked('another_device');
    }
  };

  const channel = supabase
    .channel(`lms_single_session_${userId}`)
    .on(
      'postgres_changes',
      {
        event: 'UPDATE',
        schema: 'public',
        table: 'profiles',
        filter: `id=eq.${userId}`,
      },
      (payload: any) => {
        inspectProfileRow(payload?.new);
      }
    )
    .subscribe();

  const pollTimer = window.setInterval(async () => {
    if (stopped || document.hidden) return;
    try {
      const { data } = await supabase
        .from('profiles')
        .select('status, avatar_url')
        .eq('id', userId)
        .maybeSingle();
      inspectProfileRow(data);
    } catch {
      // ignore transient network errors
    }
  }, 45_000);

  return () => {
    stopped = true;
    window.clearInterval(pollTimer);
    supabase.removeChannel(channel);
  };
}

/**
 * 3. Bảo vệ nội dung thân thiện với Click đúp Tra Từ Điển (DictionaryWidget):
 * - KHÔNG khóa bôi đen (giữ 100% double-click tra từ!)
 * - Chặn copy đoạn văn dài (> 35 ký tự) ngoài ô nhập liệu (input/textarea)
 * - Chặn in PDF (Ctrl+P & @media print) và Ctrl+S
 * - Tự gắn controlsList="nodownload" cho thẻ <audio>
 */
export function installLmsContentGuard(isEn = false): () => void {
  if (typeof window === 'undefined' || typeof document === 'undefined') return () => {};

  const STYLE_ID = 'tony-lms-print-guard-style';
  if (!document.getElementById(STYLE_ID)) {
    const style = document.createElement('style');
    style.id = STYLE_ID;
    style.textContent = `
      @media print {
        body * { display: none !important; visibility: hidden !important; }
        body::after {
          content: "© Nội dung bài giảng & đề thi độc quyền thuộc TonyEnglish.vn — Không hỗ trợ in ấn hoặc xuất PDF.";
          display: block !important;
          visibility: visible !important;
          padding: 48px 24px;
          text-align: center;
          font-family: sans-serif;
          font-size: 18px;
          font-weight: 700;
          color: #0f172a;
        }
      }
    `;
    document.head.appendChild(style);
  }

  let toastTimeout: number | null = null;
  const showGuardToast = (msg: string) => {
    const TOAST_ID = 'tony-lms-guard-toast';
    let el = document.getElementById(TOAST_ID);
    if (!el) {
      el = document.createElement('div');
      el.id = TOAST_ID;
      el.style.cssText =
        'position:fixed;bottom:24px;left:50%;transform:translateX(-50%);z-index:99999;background:#0f172a;color:#f8fafc;padding:10px 18px;border-radius:12px;font-size:13px;font-weight:700;box-shadow:0 10px 30px rgba(0,0,0,0.28);border:1px solid rgba(251,191,36,0.5);pointer-events:none;transition:opacity 0.25s;';
      document.body.appendChild(el);
    }
    el.textContent = msg;
    el.style.opacity = '1';
    if (toastTimeout) window.clearTimeout(toastTimeout);
    toastTimeout = window.setTimeout(() => {
      if (el) el.style.opacity = '0';
    }, 2800);
  };

  const isEditableTarget = (target: EventTarget | null): boolean => {
    const el = target as HTMLElement | null;
    if (!el) return false;
    const tag = (el.tagName || '').toLowerCase();
    return tag === 'input' || tag === 'textarea' || Boolean(el.isContentEditable);
  };

  const handleCopyOrCut = (e: ClipboardEvent) => {
    if (isEditableTarget(e.target)) return;
    const selectedText = window.getSelection()?.toString().trim() || '';
    // Cho phép copy từ vựng ngắn <= 35 ký tự (1–3 từ) để học sinh tra cứu bình thường
    if (selectedText.length <= 35) return;

    e.preventDefault();
    try {
      e.clipboardData?.setData(
        'text/plain',
        '© Tài liệu học tập độc quyền thuộc bản quyền TonyEnglish.vn — Vui lòng không sao chép nội dung dài.'
      );
    } catch {
      // ignore
    }
    showGuardToast(
      isEn
        ? '🔒 Copying full passages is disabled (double-click any word to use the dictionary).'
        : '🔒 Tính năng sao chép đoạn dài bị khóa để bảo vệ bản quyền (bạn vẫn click đúp tra từ điển bình thường).'
    );
  };

  const handleKeyDown = (e: KeyboardEvent) => {
    const key = (e.key || '').toLowerCase();
    if ((e.ctrlKey || e.metaKey) && (key === 'p' || key === 's')) {
      e.preventDefault();
      showGuardToast(
        isEn
          ? '🔒 Printing and saving course materials as PDF is disabled.'
          : '🔒 Tính năng in / lưu PDF giáo án bị khóa để bảo vệ bản quyền TonyEnglish.vn.'
      );
    }
  };

  // Gắn nodownload cho mọi thẻ <audio> & <video> trong LMS
  const hardenMediaElements = () => {
    document.querySelectorAll('audio, video').forEach((media) => {
      if (!media.getAttribute('controlsList')?.includes('nodownload')) {
        media.setAttribute('controlsList', 'nodownload noplaybackrate');
      }
      media.setAttribute('oncontextmenu', 'return false;');
    });
  };
  hardenMediaElements();
  const observer = new MutationObserver(() => hardenMediaElements());
  observer.observe(document.body, { childList: true, subtree: true });

  document.addEventListener('copy', handleCopyOrCut);
  document.addEventListener('cut', handleCopyOrCut);
  window.addEventListener('keydown', handleKeyDown, true);

  return () => {
    document.removeEventListener('copy', handleCopyOrCut);
    document.removeEventListener('cut', handleCopyOrCut);
    window.removeEventListener('keydown', handleKeyDown, true);
    observer.disconnect();
    const styleEl = document.getElementById(STYLE_ID);
    if (styleEl) styleEl.remove();
    const toastEl = document.getElementById('tony-lms-guard-toast');
    if (toastEl) toastEl.remove();
    if (toastTimeout) window.clearTimeout(toastTimeout);
  };
}

/**
 * 4. Cảnh báo mở bài hàng loạt (Anti-Scraping Burst Detector)
 * Nếu học viên không phải Admin mở >= 15 bài giảng/đề thi khác nhau trong 10 phút -> Báo đỏ về AdminPanel!
 */
export async function trackLmsContentAccessBurst(params: {
  userId?: string | null;
  isAdmin: boolean;
  itemType: 'lecture' | 'test';
  itemId: string;
  itemTitle?: string;
}): Promise<void> {
  const { userId, isAdmin, itemType, itemId, itemTitle } = params;
  if (isAdmin || !userId || !itemId) return;

  try {
    const now = Date.now();
    const TEN_MIN_MS = 10 * 60 * 1000;
    const raw = sessionStorage.getItem(BURST_STORAGE_KEY);
    const list: Array<{ k: string; t: number }> = raw ? JSON.parse(raw) : [];
    const recent = list.filter((x) => now - x.t <= TEN_MIN_MS);
    const key = `${itemType}:${itemId}`;
    if (!recent.some((x) => x.k === key)) {
      recent.push({ k: key, t: now });
    }
    sessionStorage.setItem(BURST_STORAGE_KEY, JSON.stringify(recent.slice(-40)));

    if (recent.length >= 15) {
      const lastAlertTs = Number(sessionStorage.getItem(BURST_ALERT_COOLDOWN_KEY) || '0');
      if (now - lastAlertTs > 30 * 60 * 1000) {
        sessionStorage.setItem(BURST_ALERT_COOLDOWN_KEY, String(now));
        await supabase.from('activity_logs').insert([
          {
            user_id: userId,
            action_type: 'security_alert',
            details: {
              alert_type: 'rapid_scraping_burst',
              message: `Mở liên tục ${recent.length} bài giảng/đề thi khác nhau trong 10 phút (gần nhất: ${itemTitle || itemId})`,
              count_10m: recent.length,
              last_item: itemTitle || itemId,
            },
          },
        ]);
      }
    }
  } catch {
    // ignore storage errors
  }
}

/**
 * 5. Kiểm tra & trừ Hạn mức AI theo tháng (chống dùng chung tài khoản làm đội chi phí API)
 */
export async function checkAndConsumeAiQuota(params: {
  isEn?: boolean;
}): Promise<{ allowed: boolean; remaining: number | null; limit: number; used: number; errorMessage?: string }> {
  const { isEn = false } = params;
  try {
    const {
      data: { session },
    } = await supabase.auth.getSession();
    const user = session?.user;
    if (!user?.id) {
      return { allowed: true, remaining: null, limit: 0, used: 0 };
    }

    const { data: profile } = await supabase
      .from('profiles')
      .select('role, avatar_url')
      .eq('id', user.id)
      .maybeSingle();

    if (!profile || profile.role === 'admin') {
      return { allowed: true, remaining: null, limit: 0, used: 0 };
    }

    const meta = parseProfileMetaSafe(profile.avatar_url);
    const sec: StudentSecurityConfig = { ...(meta.security || {}) };
    const isOnline = meta.account_type === 'online';
    const limit =
      typeof sec.ai_monthly_limit === 'number'
        ? sec.ai_monthly_limit
        : isOnline
          ? DEFAULT_ONLINE_AI_LIMIT
          : 0;

    // 0 = không giới hạn (học viên Offline 30tr/45tr)
    if (limit <= 0) {
      return { allowed: true, remaining: null, limit: 0, used: 0 };
    }

    const curMonth = getCurrentYearMonth();
    const prevUsage = sec.ai_usage && sec.ai_usage.month === curMonth ? sec.ai_usage : { month: curMonth, count: 0 };

    if (prevUsage.count >= limit) {
      return {
        allowed: false,
        remaining: 0,
        limit,
        used: prevUsage.count,
        errorMessage: isEn
          ? `⚠️ You have reached your monthly AI limit (${limit}/${limit} requests for ${curMonth}). Contact Mr. Tony (Zalo 0935 058 688) to expand your quota or upgrade!`
          : `⚠️ Em đã dùng hết hạn mức trợ lý AI tháng ${curMonth} (${limit}/${limit} lượt). Liên hệ Thầy Tony (Zalo 0935 058 688) để mở thêm hạn mức hoặc nâng cấp gói nhé!`,
      };
    }

    const nextCount = prevUsage.count + 1;
    const nextMeta = {
      ...meta,
      security: {
        ...sec,
        ai_monthly_limit: limit,
        ai_usage: { month: curMonth, count: nextCount },
      },
    };
    await supabase
      .from('profiles')
      .update({ avatar_url: JSON.stringify(nextMeta) })
      .eq('id', user.id);

    return {
      allowed: true,
      remaining: Math.max(0, limit - nextCount),
      limit,
      used: nextCount,
    };
  } catch {
    return { allowed: true, remaining: null, limit: 0, used: 0 };
  }
}
