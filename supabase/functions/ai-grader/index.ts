import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { encodeBase64 } from "https://deno.land/std@0.208.0/encoding/base64.ts";

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
};

serve(async (req) => {
  // Xử lý CORS cho trình duyệt
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders });
  }

  try {
    const GEMINI_API_KEY = Deno.env.get('GEMINI_API_KEY');
    if (!GEMINI_API_KEY) {
      throw new Error("Chưa cấu hình GEMINI_API_KEY trên Supabase.");
    }

    // 🚀 ĐÃ THÊM BIẾN imageUrls ĐỂ ĐÓN NHẬN ẢNH TỪ BÀI THI
    const { prompt, base64Audio, imageUrls, model = 'gemini-2.5-flash' } = await req.json();

    let parts: any[] = [{ text: prompt }];

    // Dành cho bài thi Speaking (Nếu có Audio)
    if (base64Audio) {
        parts.push({ inlineData: { mimeType: "audio/webm", data: base64Audio } });
    }

    // 🚀 Dành cho bài thi Writing Task 1 (Nếu có Mảng hình ảnh)
    if (imageUrls && Array.isArray(imageUrls) && imageUrls.length > 0) {
        for (const url of imageUrls) {
            try {
                console.log("Đang tải ảnh:", url);
                const imgRes = await fetch(url);
                if (imgRes.ok) {
                    const arrayBuffer = await imgRes.arrayBuffer();
                    const base64Data = encodeBase64(arrayBuffer);
                    const mimeType = imgRes.headers.get('content-type') || 'image/jpeg';
                    parts.push({
                        inlineData: { mimeType: mimeType, data: base64Data }
                    });
                }
            } catch (e) {
                console.error("Lỗi khi tải ảnh vào AI:", e);
            }
        }
    }

    const contents = [{ parts: parts }];

    // Truyền biến ${model} vào URL để hệ thống linh hoạt chuyển đổi AI
    const googleResponse = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${GEMINI_API_KEY}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: contents,
        generationConfig: { responseMimeType: "application/json" }
      })
    });
    
    const googleData = await googleResponse.json();
    
    if (!googleResponse.ok) {
       throw new Error(googleData.error?.message || "Google API Error");
    }

    const textResult = googleData.candidates[0].content.parts[0].text;
    
    return new Response(
      JSON.stringify({ result: textResult }),
      { headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
    );

  } catch (error: any) {
    return new Response(
      JSON.stringify({ error: error.message }),
      { headers: { ...corsHeaders, 'Content-Type': 'application/json' }, status: 400 }
    );
  }
});