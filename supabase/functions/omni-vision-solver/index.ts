import { serve } from "https://deno.land/std@0.168.0/http/server.ts";

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
};

serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders });
  }

  try {
    const { imageUrl, content, history, prompt, courseTitle } = await req.json();
    
    // Lấy API Key từ biến môi trường của Supabase
    const GEMINI_API_KEY = Deno.env.get('GEMINI_API_KEY'); 

    let contents = [];
    
    // Nếu có lịch sử chat trước đó trên bảng đen, nạp vào để AI nhớ ngữ cảnh
    if (history && history.length > 0) {
        history.forEach((msg: any) => {
            contents.push({
                role: msg.role === 'model' || msg.role === 'ai' ? 'model' : 'user',
                parts: [{ text: msg.text || "" }]
            });
        });
    }

    // Cấu trúc gói tin chứa Ảnh và Text cho câu hỏi hiện tại
    let currentParts = [];
    if (prompt) {
        currentParts.push({ text: prompt });
    }

    if (imageUrl) {
        const mimeType = imageUrl.startsWith('data:image/png') ? 'image/png' : 'image/jpeg';
        const base64Data = imageUrl.includes(',') ? imageUrl.split(',')[1] : imageUrl;
        currentParts.push({
            inlineData: { mimeType: mimeType, data: base64Data } // <--- ĐÃ SỬA: inline_data -> inlineData, mime_type -> mimeType
        });
    }
    
    currentParts.push({ text: content || "Hãy giải chi tiết bức ảnh bài tập này giúp em." });
    contents.push({ role: "user", parts: currentParts });

    // Gọi Gemini 2.5 Flash
    console.log("Calling Gemini API with payload:", JSON.stringify({ contents }));
    
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${GEMINI_API_KEY}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ contents: contents })
    });

    const data = await response.json();
    console.log("Gemini API Response Status:", response.status);
    console.log("Gemini API Response Data:", JSON.stringify(data));

    const resultText = data.candidates?.[0]?.content?.parts?.[0]?.text;
    
    if (!resultText) {
        console.error("Failed to get text from Gemini. Error info:", data.error || data);
    }

    const finalResult = resultText || "Xin lỗi con, thầy đang bận chút xíu, con gửi lại đề bài nhé.";

    return new Response(JSON.stringify({ result: finalResult }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });

  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });
  }
});
