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
    const { testConfig, textAnswers, imageAnswers, pdfUrl, insertPdfUrl, insertPdfUrl2, subjectHint, mode, image } = await req.json();
    const GEMINI_API_KEY = Deno.env.get('GEMINI_API_KEY');

    if (!GEMINI_API_KEY) {
      throw new Error("GEMINI_API_KEY chưa được cấu hình trong Supabase Edge Functions.");
    }

    // ============================================================
    // OCR Mode: chụp ảnh bài làm → chuyển thành text
    // ============================================================
    if (mode === 'ocr' && image) {
      const mimeType = image.split(';')[0].split(':')[1] || 'image/jpeg';
      const base64Data = image.split(',')[1];
      
      const ocrResponse = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${GEMINI_API_KEY}`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: [{ role: "user", parts: [
              { text: "Extract ALL text from this image. Return ONLY the raw text content, preserving line breaks. If there are mathematical formulas, convert them to plain text notation." },
              { inline_data: { mime_type: mimeType, data: base64Data } }
            ]}],
            generationConfig: { temperature: 0.1, maxOutputTokens: 4096 }
          })
        }
      );
      
      const ocrData = await ocrResponse.json();
      const ocrText = ocrData.candidates?.[0]?.content?.parts?.[0]?.text || "";
      
      return new Response(JSON.stringify({ text: ocrText }), {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });
    }

    // ============================================================
    // Grading Mode
    // ============================================================
    const parts: any[] = [];
    let pdfAttached = false;

    // 1. Gửi PDF đề thi (Question Paper) cho Gemini Vision (nếu có)
    if (pdfUrl) {
      try {
        console.log(`[igcse-grader] Fetching Question Paper PDF: ${pdfUrl}`);
        const pdfResponse = await fetch(pdfUrl);
        if (pdfResponse.ok) {
          const pdfBuffer = await pdfResponse.arrayBuffer();
          const pdfBase64 = base64Encode(new Uint8Array(pdfBuffer));
          
          parts.push({ text: "\n[QUESTION PAPER (PDF) — ĐỌC KỸ TOÀN BỘ NỘI DUNG VĂN BẢN, HÌNH ẢNH, BẢNG BIỂU TRONG FILE NÀY. Đây là đề thi chính.]::" });
          parts.push({ inline_data: { mime_type: "application/pdf", data: pdfBase64 } });
          pdfAttached = true;
          console.log(`[igcse-grader] Question Paper attached: ${(pdfBuffer.byteLength / 1024).toFixed(0)} KB`);
        } else {
          console.error(`[igcse-grader] Failed to fetch Question Paper: HTTP ${pdfResponse.status}`);
        }
      } catch (pdfErr) {
        console.error("[igcse-grader] Error fetching Question Paper:", pdfErr);
      }
    } else {
      console.log("[igcse-grader] No pdfUrl provided");
    }

    // 1b. Gửi PDF Insert 1 / Resource Booklet (nếu có)
    if (insertPdfUrl) {
      try {
        console.log(`[igcse-grader] Fetching Insert 1 PDF: ${insertPdfUrl}`);
        const insertResponse = await fetch(insertPdfUrl);
        if (insertResponse.ok) {
          const insertBuffer = await insertResponse.arrayBuffer();
          const insertBase64 = base64Encode(new Uint8Array(insertBuffer));

          parts.push({ text: "\n[INSERT 1 / RESOURCE BOOKLET (PDF) — Tài liệu bổ sung chứa dữ liệu, bảng biểu, biểu đồ, bản đồ. ĐỌC KỸ và đối chiếu khi chấm bài.]:" });
          parts.push({ inline_data: { mime_type: "application/pdf", data: insertBase64 } });
          console.log(`[igcse-grader] Insert 1 PDF attached: ${(insertBuffer.byteLength / 1024).toFixed(0)} KB`);
        } else {
          console.error(`[igcse-grader] Failed to fetch Insert 1 PDF: HTTP ${insertResponse.status}`);
        }
      } catch (insertErr) {
        console.error("[igcse-grader] Error fetching Insert 1 PDF:", insertErr);
      }
    }

    // 1c. Gửi PDF Insert 2 (nếu có)
    if (insertPdfUrl2) {
      try {
        console.log(`[igcse-grader] Fetching Insert 2 PDF: ${insertPdfUrl2}`);
        const insert2Response = await fetch(insertPdfUrl2);
        if (insert2Response.ok) {
          const insert2Buffer = await insert2Response.arrayBuffer();
          const insert2Base64 = base64Encode(new Uint8Array(insert2Buffer));

          parts.push({ text: "\n[INSERT 2 (PDF) — Tài liệu bổ sung thứ hai. ĐỌC KỸ NỘI DUNG FILE NÀY và đối chiếu với bài làm của học sinh.]:" });
          parts.push({ inline_data: { mime_type: "application/pdf", data: insert2Base64 } });
          console.log(`[igcse-grader] Insert 2 PDF attached: ${(insert2Buffer.byteLength / 1024).toFixed(0)} KB`);
        } else {
          console.error(`[igcse-grader] Failed to fetch Insert 2 PDF: HTTP ${insert2Response.status}`);
        }
      } catch (insert2Err) {
        console.error("[igcse-grader] Error fetching Insert 2 PDF:", insert2Err);
      }
    }
    
    // 2. Gửi ảnh bài làm của học sinh (nếu có)
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

    // 3. Xây dựng prompt thông minh theo từng loại môn
    const isBusinessOrEcon = subjectHint === 'business' || subjectHint === 'economics' ||
      JSON.stringify(testConfig).toLowerCase().includes('business') ||
      JSON.stringify(testConfig).toLowerCase().includes('opportunity cost') ||
      JSON.stringify(testConfig).toLowerCase().includes('stakeholder');

    const subjectRules = isBusinessOrEcon ? `
## QUY TẮC CHẤM CHUYÊN BIỆT CHO BUSINESS STUDIES / ECONOMICS:
1. **Câu "Identify" / "State" (AO1 — thường 1 điểm/ý):** Học sinh chỉ cần nêu đúng khái niệm/ví dụ hợp lệ. KHÔNG yêu cầu phải khớp chính xác từ khóa trong MS. Bất kỳ ý nào hợp lý và có trong bài đọc (case study) đều được chấp nhận.
   Ví dụ: Nếu MS ghi "sunbeds" nhưng học sinh viết "scissors" hoặc "hairdryer" — nếu vật dụng đó THỰC SỰ được nhắc đến trong case study → VẪN ĐƯỢC ĐIỂM.
2. **Câu "Define" (AO1 — thường 2 điểm):** Chấp nhận mọi định nghĩa đúng về mặt nội dung, không bắt buộc phải giống sách giáo khoa từng chữ. Cho 1 điểm nếu định nghĩa đúng một phần.
3. **Câu "Outline" (AO1+AO2 — thường 2 điểm/ý):** 1 điểm cho ý lý thuyết (Knowledge), 1 điểm cho ngữ cảnh áp dụng vào case study (Application). Chấp nhận bất kỳ ví dụ hợp lý nào từ bài đọc.
4. **Câu "Explain" (AO1+AO2+AO3 — thường 3 điểm/ý):** 1 điểm Knowledge + 1 điểm Application + 1 điểm Analysis (chuỗi lập luận nguyên nhân → hệ quả). Chấp nhận lập luận logic dù khác MS.
5. **Câu "Do you think" / "Evaluate" / "Recommend" (AO1+AO2+AO3 — thường 6 điểm):** Cho điểm dựa trên chất lượng lập luận, có nêu được cả hai phía (pros/cons), có kết luận. KHÔNG yêu cầu kết luận phải giống MS.
6. **NGUYÊN TẮC VÀNG:** Marking Scheme chỉ là GỢI Ý đáp án, không phải danh sách duy nhất. Nếu học sinh đưa ra ý khác nhưng hợp lý và có căn cứ từ case study → PHẢI cho điểm.
` : `
## QUY TẮC CHẤM CHUYÊN BIỆT CHO SCIENCE / MATHS:
1. Chấm CHÍNH XÁC theo Marking Scheme. Đáp án khoa học cần chính xác về thuật ngữ.
2. Với câu hỏi tính toán: nếu kết quả đúng nhưng không ghi đơn vị → trừ 1 điểm.
3. Với câu hỏi vẽ đồ thị/bản vẽ (image_upload): phân tích chi tiết, đối chiếu với MS.
4. Câu hỏi nhận dạng từ hình ảnh (Fig): BẮT BUỘC nhìn hình trong PDF, áp dụng dichotomous key, kiểm tra thứ tự.
5. Nếu học sinh hoán đổi vị trí (ghi cây A ở vị trí cây B) → trừ điểm.
`;

    const prompt = `
Bạn là giám khảo Cambridge IGCSE chuyên nghiệp. Hãy chấm điểm bài làm của học sinh một cách CÔNG BẰNG và CHÍNH XÁC.

## TÀI LIỆU THAM KHẢO (CASE STUDY / ĐỀ THI):
${pdfAttached ? "✅ File PDF đã được đính kèm ở trên. BẮT BUỘC phải ĐỌC KỸ TOÀN BỘ nội dung văn bản trong PDF này (bao gồm case study, bảng số liệu, hình ảnh). Đây là nguồn thông tin CHÍNH để xác định câu trả lời nào hợp lệ." : "⚠️ Không có PDF đính kèm. Chấm dựa trên Marking Scheme text."}

## MARKING SCHEME (GỢI Ý ĐÁP ÁN):
${JSON.stringify(testConfig, null, 2)}

## BÀI LÀM CỦA HỌC SINH:
${JSON.stringify(textAnswers, null, 2)}

${subjectRules}

## QUY TẮC CHẤM CHUNG:
1. ĐỌC KỸ toàn bộ nội dung PDF trước khi chấm bất kỳ câu nào.
2. Mỗi câu chấm INDEPENDENTLY — cho partial marks nếu đúng một phần.
${isBusinessOrEcon 
  ? "3. Marking Scheme là HƯỚNG DẪN gợi ý, không phải danh sách đáp án duy nhất. Nếu học sinh trả lời khác MS nhưng câu trả lời HỢP LÝ, CÓ CĂN CỨ từ case study → VẪN CHO ĐIỂM."
  : "3. Chấm CHÍNH XÁC theo Marking Scheme. Thuật ngữ khoa học, công thức, tên loài phải ĐÚNG CHÍNH XÁC. KHÔNG chấp nhận đáp án thay thế trừ khi MS ghi rõ (accept equivalent)."}
4. Khi trả lời bằng tiếng Anh mà đề hỏi tiếng Anh → chấm nội dung, KHÔNG trừ điểm vì lỗi ngữ pháp nhẹ.
5. Feedback bằng Tiếng Việt, giải thích tại sao đúng/sai và gợi ý cải thiện.

## YÊU CẦU JSON ĐẦU RA (Bắt buộc trả về JSON chuẩn, KHÔNG có backticks):
{
  "total_student_score": <tổng điểm đạt>,
  "total_max_score": <tổng điểm tối đa>,
  "general_feedback": "<Nhận xét tổng quan bằng tiếng Việt — khen ngợi điểm tốt, chỉ ra điểm cần cải thiện>",
  "details": [
    {
      "id": "<ID câu hỏi — lấy từ question_number trong testConfig>",
      "student_score": <điểm đạt>,
      "max_score": <điểm tối đa>,
      "is_correct": <true/false>,
      "correct_answer": "<Đáp án đúng theo MS>",
      "examiner_comment": "<Giải thích chi tiết bằng tiếng Việt: tại sao đạt/mất điểm, trích dẫn cụ thể từ case study nếu liên quan>"
    }
  ]
}
`;

    parts.push({ text: prompt });

    console.log(`[igcse-grader] Sending to Gemini: ${parts.length} parts, PDF=${pdfAttached}, images=${imageAnswers?.length || 0}, subject=${isBusinessOrEcon ? 'Business/Econ' : 'Science/Maths'}`);

    const response = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${GEMINI_API_KEY}`, 
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            contents: [{ role: "user", parts: parts }],
            generationConfig: {
                temperature: 0.2,
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

    let parsedResult;
    try {
      parsedResult = JSON.parse(resultText);
    } catch (parseErr) {
      console.error("[igcse-grader] Failed to parse Gemini JSON:", parseErr);
      const cleaned = resultText.replace(/```json/gi, "").replace(/```/gi, "").trim();
      try {
        parsedResult = JSON.parse(cleaned);
      } catch {
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
