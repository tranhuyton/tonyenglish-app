import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {
  console.error("Lỗi: Chưa tìm thấy API Key của Supabase trong file .env!");
}

// Khởi tạo Supabase Client để gọi Database ở bất kỳ đâu trong dự án
export const supabase = createClient(supabaseUrl, supabaseAnonKey);