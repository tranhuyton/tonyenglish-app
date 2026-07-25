import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { encode as base64Encode } from "https://deno.land/std@0.168.0/encoding/base64.ts";

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
};

serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders });
  }

  try {
    const { testConfig, textAnswers, imageAnswers, pdfUrl } = await req.json();
    const GEMINI_API_KEY = Deno.env.get('GEMINI_API_KEY');

    if (!GEMINI_API_KEY) {
      throw new Error("GEMINI_API_KEY chưa được cấu hình trong Supabase Edge Functions.");
    }

    const parts: any[] = [];
    let pdfAttached = false;

    // ============================================================
    // 1. Gửi PDF đề thi cho Gemini Vision (nếu có)
    // ============================================================
    if (pdfUrl) {
      try {
        console.log(`[igcse-grader] Fetching exam PDF: ${pdfUrl}`);
        const pdfResponse = await fetch(pdfUrl);
        if (pdfResponse.ok) {
          const pdfBuffer = await pdfResponse.arrayBuffer();
          const pdfBase64 = base64Encode(new Uint8Array(pdfBuffer));
          
          parts.push({ text: "\n[ĐỀ THI GỐC (PDF) - QUAN TRỌNG: HÃY NHÌN KỸ TẤT CẢ HÌNH ẢNH (Fig), BẢNG BIỂU, ĐỒ THỊ TRONG PDF NÀY. Đặc biệt khi chấm câu nhận dạng từ hình ảnh, BẮT BUỘC phải đối chiếu hình trong PDF với bài làm học sinh]:" });
          parts.push({ inline_data: { mime_type: "application/pdf", data: pdfBase64 } });
          pdfAttached = true;
          console.log(`[igcse-grader] PDF attached successfully: ${(pdfBuffer.byteLength / 1024).toFixed(0)} KB`);
        } else {
          console.error(`[igcse-grader] Failed to fetch PDF: HTTP ${pdfResponse.status}`);
        }
      } catch (pdfErr) {
        console.error("[igcse-grader] Error fetching PDF:", pdfErr);
      }
    } else {
      console.log("[igcse-grader] No pdfUrl provided");
    }
    
    // ============================================================
    // 2. Gửi ảnh bài làm của học sinh (nếu có)
    // ============================================================
    if (imageAnswers && imageAnswers.length > 0) {
        imageAnswers.forEach((img: any) => {
            try {
                const mimeType = img.base64.split(';')[0].split(':')[1];
                const data = img.base64.split(',')[1];
                parts.push({ text: `\n[ẢNH BÀI LÀM CỦA HỌC SINH CHO CÂU HỎI ID: ${img.questionId}]:` });
                parts.push({ inline_data: { mime_type: mimeType, data: data } });
            } catch (e) {
                parts.push({ text: `\n[LỖI ẢNH cho câu ${img.questionId}: Không thể decode ảnh]` });
            }
        });
    }

    // ============================================================
    // 3. Prompt chấm điểm
    // ============================================================
    const prompt = `
Bạn là giám khảo Cambridge IGCSE cực kỳ nghiêm khắc và chính xác. Hãy chấm điểm bài làm của học sinh.

## ĐỀ THI GỐC:
${pdfAttached ? "✅ File PDF đề thi đã được đính kèm ở trên. BẮT BUỘC phải nhìn kỹ các hình ảnh (Fig), bảng biểu, đồ thị trong PDF để đối chiếu khi chấm." : "⚠️ Không có PDF đề thi đính kèm. Chấm dựa trên Marking Scheme text."}

## MARKING SCHEME CHUẨN:
${JSON.stringify(testConfig, null, 2)}

## BÀI LÀM CỦA HỌC SINH:
${JSON.stringify(textAnswers, null, 2)}

## QUY TẮC CHẤM ĐIỂM NGHIÊM NGẶT:
1. Chấm CHÍNH XÁC theo Marking Scheme (MS) của Cambridge. KHÔNG cho điểm thương hại.
2. Với câu hỏi tính toán: nếu kết quả đúng nhưng không ghi đơn vị → trừ 1 điểm.
3. Với câu hỏi vẽ đồ thị/bản vẽ (image_upload): phân tích chi tiết hình vẽ học sinh, đối chiếu với MS.
4. **CỰC KỲ QUAN TRỌNG — Câu hỏi nhận dạng từ hình ảnh (Fig):**
   - BẮT BUỘC nhìn từng hình trong PDF đề thi (ví dụ: hình các loại lá, hình sinh vật...)
   - Áp dụng dichotomous key từng bước cho TỪNG hình ảnh cụ thể
   - XÁC ĐỊNH tên chính xác cho TỪNG vị trí hình ảnh
   - Rồi mới so sánh với câu trả lời học sinh để tính số đáp án đúng/sai
   - Nếu học sinh hoán đổi vị trí (ví dụ: ghi cây A ở vị trí cây B) → phải trừ điểm
   - KHÔNG ĐƯỢC mặc định cho đúng khi chỉ thấy danh sách tên đúng mà không kiểm tra thứ tự
5. Mỗi câu chấm độc lập, cho partial marks nếu đúng một phần.
6. Feedback bằng Tiếng Việt, giải thích CHI TIẾT tại sao đúng/sai cho từng vị trí.

## YÊU CẦU JSON ĐẦU RA (Bắt buộc trả về JSON chuẩn, KHÔNG có backticks):
{
  "total_student_score": <tổng điểm đạt>,
  "total_max_score": <tổng điểm tối đa>,
  "general_feedback": "<Nhận xét tổng quan bằng tiếng Việt>",
  "details": [
    {
      "id": "<ID câu hỏi>",
      "student_score": <điểm đạt>,
      "max_score": <điểm tối đa>,
      "is_correct": <true/false>,
      "correct_answer": "<Đáp án đúng theo MS>",
      "examiner_comment": "<Giải thích chi tiết bằng tiếng Việt, nêu rõ từng vị trí đúng/sai>"
    }
  ]
}
`;

    parts.push({ text: prompt });

    console.log(`[igcse-grader] Sending to Gemini: ${parts.length} parts, PDF=${pdfAttached}, images=${imageAnswers?.length || 0}`);

    const response = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${GEMINI_API_KEY}`, 
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            contents: [{ role: "user", parts: parts }],
            generationConfig: {
                temperature: 0.1,
                maxOutputTokens: 65536,
                responseMimeType: "application/json"
            }
        })
      }
    );

    if (!response.ok) {
      const errText = await response.text();
      console.error(`[igcse-grader] Gemini API error: ${response.status} - ${errText.slice(0, 500)}`);
      throw new Error(`Gemini API error (${response.status}): ${errText.slice(0, 200)}`);
    }

    const data = await response.json();
    const finishReason = data.candidates?.[0]?.finishReason;
    const resultText = data.candidates?.[0]?.content?.parts?.[0]?.text || "{}";
    console.log(`[igcse-grader] Gemini response: ${resultText.length} chars, finishReason=${finishReason}`);

    // Parse ngay tại đây để tránh lỗi double-stringify với Vietnamese text
    let parsedResult;
    try {
      parsedResult = JSON.parse(resultText);
    } catch (parseErr) {
      console.error("[igcse-grader] Failed to parse Gemini JSON:", parseErr);
      // Thử clean backticks nếu có
      const cleaned = resultText.replace(/```json/gi, "").replace(/```/gi, "").trim();
      try {
        parsedResult = JSON.parse(cleaned);
      } catch {
        // Trả raw text để frontend hiển thị lỗi
        parsedResult = null;
      }
    }

    return new Response(JSON.stringify({ result: parsedResult, rawText: parsedResult ? null : resultText }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });

  } catch (error: any) {
    console.error("[igcse-grader] Fatal error:", error);
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });
  }
});
