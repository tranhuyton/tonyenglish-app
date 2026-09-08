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
  - **CẤM** sử dụng `questionType` là `"Khác"` hay `"True/False"`. App không có logic UI render riêng cho loại bài này.
  - Thay vào đó, PHẢI LUÔN sử dụng `questionType` là `"TFNG"` cho BẤT KỲ dạng bài True/False nào (kể cả bài chỉ có 2 lựa chọn). (KHÔNG sử dụng Droplist cho dạng bài này vì TFNG sẽ hiển thị giao diện Radio Button trực quan hơn).
  - **Số lượng Options (QUAN TRỌNG):** Phải thiết lập mảng `options` BÁM SÁT vào đúng số lượng và loại đáp án mà bài toán yêu cầu:
    - Nếu đề bài CHỈ yêu cầu True/False (2 lựa chọn): Set mảng `options` đúng 2 phần tử là `["True", "False"]`. (TUYỆT ĐỐI KHÔNG được tự ý thêm "Not Given" vào nếu đề không nhắc đến).
    - Nếu đề bài yêu cầu True/False/Not Given: Set mảng `options` là `["True", "False", "Not Given"]`.
    - Nếu đề bài yêu cầu Yes/No/Not Given: Set mảng `options` là `["Yes", "No", "Not Given"]`.
    - Nếu dạng bài yêu cầu chọn `A/I/N` (Accurate/Inaccurate/Not Given) thì phải quy đổi CHUẨN HÓA thành `"Yes", "No", "Not Given"`. TUYỆT ĐỐI không được dùng `["A", "I", "N"]`.
  - Đồng thời cập nhật trường `content` (hướng dẫn) của Section thành tên dạng bài rõ ràng, ví dụ: `<p>Yes No Not Given</p>` hoặc `<p>True / False</p>`.

## 5. Cẩn trọng khi chia Section (Đặc biệt tránh gộp nhầm Trắc nghiệm vào TFNG)
- Khi xử lý dữ liệu, KHÔNG được gộp các câu hỏi dạng Trắc nghiệm, Checkbox (VD: "Circle the appropriate letter", "Choose the reasons...") vào chung một Section với bài "Yes No Not Given" (TFNG) chỉ vì chúng đứng liền kề nhau mà không có tiêu đề "Task X" phân tách rõ ràng.
- Nếu gộp nhầm, các câu hỏi Trắc nghiệm/Checkbox sẽ bị mất mảng `options` (A, B, C, D) gốc và bị gán đè thành mảng `["Yes", "No", "Not Given"]`, dẫn đến câu hỏi rỗng nội dung `<p></p>` và lỗi giao diện.
- Giải pháp: Phải luôn tách các dạng bài có format options khác nhau thành các Section ĐỘC LẬP (VD: Section Trắc nghiệm riêng, Section Checkbox riêng, Section TFNG riêng).

## 6. Tiêu đề Part (Part Title)
- **Tuyệt đối KHÔNG** gán các tiêu đề dư thừa như "Listening Activity No. X" vào thuộc tính `title` của Part, vì giao diện đã hiển thị sẵn thông tin này ở thanh Header phía trên.
- Chỉ sử dụng Part Title cho các hướng dẫn chung chung thật sự cần thiết, nhưng tốt nhất nên đưa hướng dẫn này vào `part.content` để hiển thị thành một khối văn bản gọn gàng ở đầu khung câu hỏi bên phải.

## 7. Định dạng Transcript
- **Cách chia đoạn:** Khi nhập liệu Transcript, mỗi lượt lời của một người nói phải được đặt gọn trong MỘT thẻ `<p>` riêng biệt. TUYỆT ĐỐI KHÔNG gộp toàn bộ bài hội thoại vào chung một thẻ `<p>` rồi dùng `<br>` hoặc `\n` để xuống dòng (điều này sẽ gây ra lỗi khoảng trống kép do thuộc tính `whitespace-pre-wrap` trên giao diện).
- **Bôi đậm tên người nói:** Tên nhân vật ở đầu mỗi câu thoại phải được bôi đậm để dễ theo dõi (Ví dụ: `<p><b>Customer 1:</b> Yes, good morning.</p>`).
- **Không chứa hướng dẫn làm bài:** Transcript (nằm ở `part.explanation`) chỉ chứa nội dung lời thoại thuần túy của file Audio. TUYỆT ĐỐI KHÔNG để rớt lại các câu hướng dẫn đề bài (VD: "You will hear a job interview. As you listen...") vào trong khu vực này.

## 8. Cấu trúc dữ liệu dạng bài "Điền từ"
Đối với các bài tập có dạng `questionType` là `"Điền từ"` (hoặc Inline Droplist, Matching, Kéo thả), UI renderer phân chia khu vực hiển thị dựa vào dấu ngoặc vuông `[ 1 ]`. Để UI hiển thị đẹp nhất, BẮT BUỘC phải tuân thủ phân tách:
- **Hướng dẫn làm bài:** Phải nằm ở `section.content` và được định dạng in đậm (VD: `<p class="font-bold text-[16px] text-slate-800 mb-4">Listen carefully and fill the missing words...</p>`). TUYỆT ĐỐI KHÔNG để chứa các dấu ngoặc vuông `[ ]` trong `section.content`, nếu không UI sẽ hiểu lầm đây là nội dung câu hỏi và đẩy hết vào trong thẻ bọc (wrapper).
- **Đoạn văn bản chứa chỗ trống:** BẮT BUỘC phải cắt toàn bộ đoạn văn bản chứa các chỗ trống `[ 1 ]`, `[ 2 ]`... và dán tất cả vào thuộc tính `content` của **Câu hỏi số 1** (`questions[0].content`). UI sẽ tự động đọc đoạn văn bản này, tìm tất cả các chỗ trống và bọc nó trong một chiếc card giao diện riêng biệt cực kỳ đẹp mắt nằm bên dưới dòng hướng dẫn.

## 9. Đánh số ID câu hỏi (Question IDs)
- Khi khởi tạo dữ liệu câu hỏi trong JSON, thuộc tính `id` của mỗi câu hỏi (`questions[i].id`) BẮT BUỘC phải là số hoặc chuỗi chứa số thuần túy (ví dụ: "1", "1000", Date.now().toString()).
- TUYỆT ĐỐI KHÔNG được sử dụng chuỗi ngẫu nhiên (UUID, hex, v.v.) làm ID, vì điều này sẽ gây lỗi hiển thị số thứ tự câu hỏi lộn xộn trên giao diện (do UI dùng hàm `parseInt()`).

## 10. Dạng bài Checkbox (Chọn nhiều đáp án)
- Với các bài tập yêu cầu chọn nhiều đáp án cùng lúc (VD: "Select THREE answer choices", câu Summary), bắt buộc phải gộp chúng vào MỘT Section duy nhất có `questionType: "Checkbox"`.
- BẮT BUỘC thiết lập thuộc tính `content` của tất cả các câu hỏi con bên trong section này thành chuỗi rỗng (`""`).
- Lý do: Giao diện UI (`StandardMCQTest.tsx`) sử dụng logic gộp nhóm (`buildCheckboxCombos`). Nếu các câu hỏi con có `content` khác nhau (VD: "Chọn đáp án 1", "Chọn đáp án 2"), UI sẽ tách chúng thành các khối riêng lẻ. Chỉ khi `content` hoàn toàn giống nhau (hoặc rỗng), UI mới gom chúng lại thành MỘT khối duy nhất (VD: Câu 13-15) cho phép người dùng tick chọn nhiều ô cùng lúc và chấm điểm chính xác theo tổ hợp.

# QUY TẮC TRÍCH XUẤT VÀ HIGHLIGHT OCR CHO BÀI TẬP ĐỌC HIỂU
Các agent khi thực hiện trích xuất nội dung văn bản (OCR) từ hình ảnh để đưa vào Supabase (content_json) **PHẢI** tuân thủ nghiêm ngặt các bước sau để tránh việc làm rác dữ liệu:

1. **Lọc rác Header/Footer**: Trước khi xử lý phân tách đoạn văn, phải dùng Regular Expression mạnh để quét và xóa SẠCH các đoạn rác xuất phát từ header/footer của trang sách. Ví dụ: www.ibttoefl.co.kr, Art&Literature, Humanities... Tuyệt đối không để sót các chuỗi số hoặc ký tự lạ xen ngang vào giữa đoạn văn.
2. **Cắt đuôi phần Câu hỏi**: Tesseract OCR thường quét luôn cả phần câu hỏi trắc nghiệm bên dưới đoạn văn. Phải xử lý cắt gọn (truncate) văn bản ngay trước điểm bắt đầu của câu hỏi đầu tiên. Cần thận trọng với các pattern như 1. According to..., Directions: để loại bỏ hoàn toàn phần câu hỏi.
3. **Phân đoạn văn (Paragraphing)**: Các dòng văn bản phải được merge (nối) cẩn thận thành các đoạn văn hoàn chỉnh. Dựa vào dấu chấm kết thúc câu và chữ cái viết hoa đầu dòng để nhận diện xuống khổ. Gắn thẻ `<p>` với style có `text-indent` và `margin-bottom` để văn bản hiển thị đẹp mắt.
4. **Highlight Highlighted Sentence**: Khi thực hiện bôi đậm câu được tô sáng (highlighted sentence) từ yêu cầu của câu hỏi, không được dùng chuỗi string khớp hoàn toàn vì OCR có thể làm sai khác khoảng trắng hoặc dấu câu. Thay vào đó, trích xuất 5 từ đầu và 5 từ cuối của câu, sau đó dùng Regex để tìm và bọc thẻ highlight thật an toàn.

# QUY TẮC CẮT ẢNH TỪ SÁCH GIÁO KHOA (IMAGE CROPPING)
Các agent khi thực hiện dùng Python PIL để cắt ảnh (cropping) từ các file PDF/Ảnh chụp SGK **BẮT BUỘC** phải ghi nhớ những kinh nghiệm xương máu sau:

1. **HIỂU RÕ KÍCH THƯỚC ẢNH GỐC (ABSOLUTE DIMENSIONS):** 
   - Tuyệt đối không được "đoán" hoặc dùng mắt ước lượng toạ độ (x, y) trên các ảnh preview bị thu nhỏ. Việc vẽ đường kẻ đỏ test trên ảnh bị thu nhỏ (VD: `img.resize(...)`) sẽ dẫn đến việc chọn toạ độ bị sai lệch hoàn toàn so với ảnh gốc (có thể làm mất một nửa bức ảnh mà không hề hay biết). 
   - LUÔN LUÔN dùng lệnh `im.size` để kiểm tra chính xác chiều cao và chiều rộng của ảnh gốc nguyên bản trước khi chốt toạ độ cắt.
2. **XỬ LÝ CHỮ RÁC DÍNH VÀO BIỂU ĐỒ BẰNG TẨY TRẮNG (WHITE-OUT):**
   - Khi một đoạn text (VD: "Source C:", "Figure 1") nằm ngang hàng (chồng chéo toạ độ Y) với phần mép của biểu đồ bên cạnh, **TUYỆT ĐỐI KHÔNG** được cắt lẹm (crop) phần mép dưới của biểu đồ chỉ để loại bỏ đoạn text đó. 
   - Thay vào đó, BẮT BUỘC phải mở rộng toạ độ crop `(x1, y1, x2, y2)` bao trọn hoàn toàn biểu đồ, sau đó dùng `ImageDraw.Draw(im).rectangle(..., fill='white')` để vẽ một hộp màu trắng đè gọn gàng lên phần chữ rác (white-out) nhằm bảo toàn 100% hình ảnh.
3. **CẨN TRỌNG VỚI CÁC MÉP ẢNH / BIỂU ĐỒ ẨN:**
   - Cần chừa lề (margin) an toàn để không vô tình cắt mất các chi tiết nhỏ nhưng quan trọng: Ví dụ nét võng xuống của lòng sông, phần gạch chân của một biểu đồ, hay các nét chữ kéo dài xuống dưới như chữ `y, g, p`.
4. **KHÔNG TỰ SUY DIỄN DO ẢNH GỐC BỊ CẮT:**
   - Đôi khi hình ảnh trong sách giáo khoa nguyên bản bị dàn trang làm cắt cụt một cách đột ngột. Nếu người dùng phàn nàn "ảnh bị thiếu", agent cần phải crop thử một vùng rất lớn của ảnh gốc để kiểm tra xem bên dưới thật sự có nội dung hay không. Đừng hoảng hốt chỉnh lại toạ độ nếu chính bản PDF gốc đã bị cắt ngang ở đúng vị trí đó.
