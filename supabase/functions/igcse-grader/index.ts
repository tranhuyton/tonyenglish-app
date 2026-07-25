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
    const { testConfig, textAnswers, imageAnswers, pdfUrl } = await req.json();
    const GEMINI_API_KEY = Deno.env.get('GEMINI_API_KEY');

    if (!GEMINI_API_KEY) {
      throw new Error("GEMINI_API_KEY chưa được cấu hình trong Supabase Edge Functions.");
    }

    const parts: any[] = [];

    // ============================================================
    // 1. Gửi PDF đề thi cho Gemini Vision (nếu có)
    // ============================================================
    if (pdfUrl) {
      try {
        console.log(`Fetching exam PDF: ${pdfUrl}`);
        const pdfResponse = await fetch(pdfUrl);
        if (pdfResponse.ok) {
          const pdfBuffer = await pdfResponse.arrayBuffer();
          const pdfBase64 = btoa(
            new Uint8Array(pdfBuffer).reduce((data, byte) => data + String.fromCharCode(byte), '')
          );
          parts.push({ text: "\n[ĐỀ THI GỐC (PDF) - HÃY NHÌN KỸ TẤT CẢ CÁC HÌNH ẢNH, BẢNG BIỂU, ĐỒ THỊ TRONG ĐỀ ĐỂ CHẤM CHÍNH XÁC]:" });
          parts.push({ inline_data: { mime_type: "application/pdf", data: pdfBase64 } });
          console.log(`PDF attached: ${(pdfBuffer.byteLength / 1024).toFixed(0)} KB`);
        } else {
          console.warn(`Failed to fetch PDF (${pdfResponse.status}), proceeding without it`);
        }
      } catch (pdfErr) {
        console.warn("Error fetching PDF, proceeding without:", pdfErr);
      }
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
${pdfUrl ? "File PDF đề thi đã được đính kèm ở trên. HÃY NHÌN KỸ các hình ảnh (Fig), bảng biểu, đồ thị trong đề để đối chiếu với bài làm học sinh." : "(Không có PDF đề thi đính kèm)"}

## THÔNG TIN ĐỀ THI & MARKING SCHEME CHUẨN:
${JSON.stringify(testConfig, null, 2)}

## BÀI LÀM TEXT CỦA HỌC SINH:
(Các câu có ghi "[HỌC SINH ĐÃ CHỤP ẢNH BẢN VẼ...]" thì hãy dùng thị giác nhìn các bức ảnh đã gửi ở trên để chấm)
${JSON.stringify(textAnswers, null, 2)}

## QUY TẮC CHẤM ĐIỂM:
1. Chấm CHÍNH XÁC theo Marking Scheme (MS) của Cambridge. Không cho điểm thương hại.
2. Với câu hỏi tính toán: nếu kết quả đúng nhưng không ghi đơn vị → trừ 1 điểm.
3. Với câu hỏi vẽ đồ thị/bản vẽ (image_upload): phân tích chi tiết hình vẽ học sinh, đối chiếu với mô tả MS.
4. **QUAN TRỌNG - Câu hỏi nhận dạng hình ảnh:** Khi chấm các câu yêu cầu học sinh nhận dạng từ hình ảnh (ví dụ: dùng key để xác định loài từ hình vẽ), BẮT BUỘC phải:
   - Nhìn kỹ từng hình ảnh trong PDF đề thi (Fig)
   - Đối chiếu đặc điểm hình ảnh với dichotomous key
   - So sánh kết quả với câu trả lời của học sinh
   - KHÔNG được chấm đúng nếu chỉ dựa vào tên đúng mà thứ tự sai
5. Mỗi câu chấm độc lập, cho partial marks nếu đúng một phần.
6. Feedback phải bằng Tiếng Việt, dễ hiểu cho học sinh.

## YÊU CẦU JSON ĐẦU RA (Bắt buộc trả về JSON chuẩn, KHÔNG có backticks):
{
  "total_student_score": <tổng điểm đạt>,
  "total_max_score": <tổng điểm tối đa>,
  "general_feedback": "<Nhận xét tổng quan toàn bộ bài thi bằng tiếng Việt>",
  "details": [
    {
      "id": "<ID câu hỏi, ví dụ q1_a>",
      "student_score": <điểm đạt>,
      "max_score": <điểm tối đa>,
      "is_correct": <true/false>,
      "correct_answer": "<Copy nguyên Marking Scheme chuẩn>",
      "examiner_comment": "<Giải thích chi tiết bằng tiếng Việt>"
    }
  ]
}
`;

    parts.push({ text: prompt });

    const response = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${GEMINI_API_KEY}`, 
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            contents: [{ role: "user", parts: parts }],
            generationConfig: {
                temperature: 0.1,
                maxOutputTokens: 8192,
                responseMimeType: "application/json"
            }
        })
      }
    );

    if (!response.ok) {
      const errText = await response.text();
      throw new Error(`Gemini API error (${response.status}): ${errText.slice(0, 200)}`);
    }

    const data = await response.json();
    const resultText = data.candidates?.[0]?.content?.parts?.[0]?.text || "{}";

    return new Response(JSON.stringify({ result: resultText }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });

  } catch (error: any) {
    console.error("igcse-grader error:", error);
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });
  }
});
