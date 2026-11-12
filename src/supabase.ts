import { createClient } from '@supabase/supabase-js';

/**
 * ============================================================================
 * ⚠️ CRITICAL MULTI-TENANT SUPABASE ARCHITECTURE WARNING FOR AI AGENTS ⚠️
 * ============================================================================
 * Hệ thống TonyEnglish (`tonyenglish-app` - `tonyenglish.vn`) dùng chung Supabase Project
 * (`ubkvzgwespfvrlpjuxkp.supabase.co`) và bảng `auth.users` với hệ thống
 * Tử Vi Thầy Tôn (`tuvi-ai` - `tuvithayton.vn`).
 *
 * QUY TẮC CÁCH LY BẮT BUỘC (KHÔNG ĐƯỢC VI PHẠM):
 * 1. `tonyenglish-app` CHỈ dùng bảng `public.profiles` (cùng `enrollments`, `class_students`).
 *    Bảng `public.tuvi_profiles` thuộc về Tử Vi Thầy Tôn — TUYỆT ĐỐI KHÔNG GHI VÀO ĐÓ.
 * 2. Mọi lệnh `supabase.auth.signUp` trong `tonyenglish-app` BẮT BUỘC truyền `options.data.app = 'tonyenglish'`.
 * 3. TUYỆT ĐỐI KHÔNG tự động chèn/upsert user vào `public.profiles` nếu `user.user_metadata?.app === 'tuvi'`.
 * ============================================================================
 */
export const TONYENGLISH_APP_ID = 'tonyenglish' as const;

export function isTonyEnglishAuthUser(
  user: { user_metadata?: Record<string, any> } | null | undefined
): boolean {
  if (!user) return false;
  return user.user_metadata?.app !== 'tuvi';
}

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {
  console.error("Lỗi: Chưa tìm thấy API Key của Supabase trong file .env!");
}

// Khởi tạo Supabase Client để gọi Database ở bất kỳ đâu trong dự án
// Custom lock function: bypass Navigator Locks API to prevent lock collision errors
// when React components mount/unmount quickly during navigation
const noopLock = async (_name: string, _acquireTimeout: number, fn: () => Promise<any>) => {
  return await fn();
};

export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    lock: noopLock as any,
    storageKey: 'sb-ubkvzgwespfvrlpjuxkp-auth-token',
    autoRefreshToken: true,
    persistSession: true,
    detectSessionInUrl: true,
  }
});