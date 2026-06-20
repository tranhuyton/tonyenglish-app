# QUY TẮC NHẬP LIỆU DỮ LIỆU BÀI TẬP VÀO DATABASE (SUPABASE)
Các agent khi làm việc với cấu trúc dữ liệu JSON của bài test trong Supabase **phải TUYỆT ĐỐI tuân thủ** các quy tắc sau để tránh làm sập UI (`StandardMCQTest.tsx`):

## 1. Cấu trúc Part và Section (Đặc biệt với dạng bài Listening)
- **Tất cả các dạng bài (Task) trong cùng 1 bài nghe PHẢI nằm chung trong 1 Part duy nhất.** (Ví dụ: `parts[0]`)
- Mỗi Task (Ví dụ: Task 1, Task 2, Task 3...) sẽ là một object nằm trong mảng `sections` của Part đó.
- KHÔNG chia thành nhiều Part trừ khi đó là các phần nghe hoàn toàn tách biệt có file audio riêng.

## 2. Tiêu đề và Nội dung (Title & Content)
- **CẤM gán chuỗi HTML vào thuộc tính `title` của section.** UI sẽ hiển thị raw HTML thay vì render.
- Đưa các thẻ tiêu đề dạng `<p class="font-bold text-lg text-slate-800 mb-2 mt-4">Task 1</p>` gộp chung vào đầu thuộc tính `content` của section.

## 3. Quy tắc gắn Lời giải thích (Explanation & Transcript)
- **Hiển thị Transcript màu vàng:** Để UI ở chế độ "Chữa Bài" (Review Mode) hiển thị khung "Audio Transcript" màu vàng chuẩn xác: Toàn bộ nội dung Transcript (lời hội thoại) phải được đưa vào trường `explanation` của **Part** (chứ không phải `explanation` của Section). Nếu có nhiều transcript, hãy nối chúng lại.
- **Giải thích chi tiết cho từng câu:** 
  - Tại trường `explanation` của TỪNG câu hỏi (từng object trong mảng `questions` của Section), PHẢI viết lời giải thích chi tiết.
  - Lời giải thích TỪNG CÂU phải được lập luận rõ ràng, trích dẫn/dịch sát nghĩa một phần của Transcript để làm bằng chứng.
  - TUYỆT ĐỐI KHÔNG copy toàn bộ Transcript nhét vào phần giải thích của từng câu hỏi.

## 4. Quy định về Question Type (Encoding & DropList)
- **Cẩn thận khi lưu tiếng Việt có dấu:** Các chuỗi quy định dạng bài (`questionType`) như `"Điền từ"`, `"Trắc nghiệm"`, `"Kéo thả"`, `"Kéo thả vào Part"`, `"Matching"` phải được bảo toàn chuẩn xác encoding UTF-8 (Không được để biến dạng thành ký tự rác như `─Éiß╗ün tß╗½`). NẾU BỊ RÁC CHỮ, APP SẼ TRẮNG MÀN HÌNH KHI NỘP BÀI.
- **Xử lý dạng bài True/False/Not Given (T/F/NG) hoặc Yes/No/Not Given (Y/N/NG):**
  - **CẤM** sử dụng `questionType` là `"Khác"`. App không có logic UI render cho loại bài này.
  - Thay vào đó, PHẢI sử dụng `questionType` là `"TFNG"`. (KHÔNG sử dụng Droplist cho dạng bài này vì TFNG sẽ hiển thị giao diện Radio Button trực quan hơn).
  - Từ nay về sau, nếu dạng bài yêu cầu chọn `A/I/N` (Accurate/Inaccurate/Not Given) thì phải quy đổi CHUẨN HÓA thành `"Yes", "No", "Not Given"`.
  - Set mảng `options` của câu hỏi T/F/NG hoặc Y/N/NG thống nhất là `["Yes", "No", "Not Given"]` hoặc `["True", "False", "Not Given"]` để tạo giao diện chọn chuẩn, tuyệt đối không được dùng `["A", "I", "N"]`.
  - Đồng thời cập nhật trường `content` (hướng dẫn) của Section thành tên dạng bài rõ ràng, ví dụ: `<p>Yes No Not Given</p>`.

## 5. Cẩn trọng khi chia Section (Đặc biệt tránh gộp nhầm Trắc nghiệm vào TFNG)
- Khi xử lý dữ liệu, KHÔNG được gộp các câu hỏi dạng Trắc nghiệm, Checkbox (VD: "Circle the appropriate letter", "Choose the reasons...") vào chung một Section với bài "Yes No Not Given" (TFNG) chỉ vì chúng đứng liền kề nhau mà không có tiêu đề "Task X" phân tách rõ ràng.
- Nếu gộp nhầm, các câu hỏi Trắc nghiệm/Checkbox sẽ bị mất mảng `options` (A, B, C, D) gốc và bị gán đè thành mảng `["Yes", "No", "Not Given"]`, dẫn đến câu hỏi rỗng nội dung `<p></p>` và lỗi giao diện.
- Giải pháp: Phải luôn tách các dạng bài có format options khác nhau thành các Section ĐỘC LẬP (VD: Section Trắc nghiệm riêng, Section Checkbox riêng, Section TFNG riêng).

Tuân thủ nghiêm ngặt các điều trên để tránh mọi lỗi logic hay crash UI do dữ liệu dị dạng!
