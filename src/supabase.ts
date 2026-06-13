import { createClient } from '@supabase/supabase-js';

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