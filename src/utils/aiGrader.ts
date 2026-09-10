import { supabase } from '../supabase';

export interface AIGradeResult {
  total_student_score: number;
  total_max_score: number;
  general_feedback: string;
  details: {
    question_id: string;
    student_score: number;
    max_score: number;
    examiner_comment: string;
  }[];
}

export const gradeAIQuestions = async (
  aiQuestions: any[], 
  answers: Record<string, string>
): Promise<AIGradeResult | null> => {
  if (!aiQuestions || aiQuestions.length === 0) return null;

  // Build the context for AI
  const aiPayload = aiQuestions.map(q => {
    return {
      question_id: String(q.id),
      question_content: (q.content || "").replace(/<[^>]+>/g, ''), // strip basic html
      question_type: q.qType, // Đoạn văn or Điền từ AI
      correct_answer_or_guideline: q.correctAnswer || "Tự luận - Không có đáp án mẫu cụ thể",
      student_answer: answers[String(q.id)] || "[Bỏ trống]"
    };
  });

  const prompt = `
    Bạn là một giáo viên tiếng Anh/Giám khảo chấm thi thông minh và công bằng.
    Nhiệm vụ của bạn là chấm điểm các câu hỏi trắc nghiệm dạng điền từ và viết đoạn văn (essay) của học sinh.

    THÔNG TIN CÁC CÂU HỎI VÀ BÀI LÀM:
    ${JSON.stringify(aiPayload, null, 2)}

    YÊU CẦU CHẤM ĐIỂM:
    1. Với dạng "Điền từ AI" (Fill in the blanks):
       - Học sinh trả lời 1 từ hoặc 1 cụm từ.
       - Điểm tối đa mỗi câu là 1 điểm.
       - Hãy chấp nhận các từ đồng nghĩa hợp lý, các cách diễn đạt tương đương hoặc các lỗi chính tả vô cùng nhỏ không làm sai nghĩa. 
       - Nếu đúng cho 1 điểm, sai cho 0 điểm.
    2. Với dạng "Đoạn văn" (Essay/Paragraph):
       - Học sinh viết một đoạn văn bản dài.
       - Điểm tối đa mỗi bài viết là 10 điểm.
       - Đánh giá dựa trên: Ngữ pháp, Từ vựng, Bám sát chủ đề. 
       - Cho điểm linh hoạt từ 0 đến 10 tùy vào chất lượng bài viết.
    3. Đưa ra nhận xét (examiner_comment) chi tiết nhưng ngắn gọn bằng tiếng Việt cho MỖI câu hỏi để học sinh biết vì sao được điểm đó.

    BẠN BẮT BUỘC PHẢI TRẢ VỀ KẾT QUẢ DƯỚI ĐỊNH DẠNG JSON SAU (chỉ trả về JSON hợp lệ, không chứa markdown text hay markdown block như \`\`\`json):
    {
      "total_student_score": 0,
      "total_max_score": 0,
      "general_feedback": "Nhận xét tổng quan...",
      "details": [
        {
          "question_id": "ID_CÂU_HỎI_TRONG_PAYLOAD",
          "student_score": 0,
          "max_score": 1,
          "examiner_comment": "Giải thích chi tiết tại sao..."
        }
      ]
    }
  `;

  try {
    const { data, error } = await supabase.functions.invoke('ai-grader', {
      body: { prompt: prompt, model: 'gemini-2.5-flash' }
    });

    if (error) throw new Error("Lỗi gọi Server Edge Function: " + error.message);
    if (data?.error) throw new Error("Lỗi chấm điểm AI: " + data.error);

    // Xử lý làm sạch JSON đề phòng AI trả về markdown backticks
    const aiResponseText = String(data.result || data.text || data).replace(/\`\`\`(json)?/gi, "").trim();
    const gradedData = JSON.parse(aiResponseText);
    
    return gradedData as AIGradeResult;
  } catch (error) {
    console.error("AI Grader error:", error);
    return null;
  }
};
