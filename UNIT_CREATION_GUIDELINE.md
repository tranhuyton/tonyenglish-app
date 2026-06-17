# QUY TRÌNH CHUẨN: TẠO UNIT MỚI CHO BỘ "4000 ESSENTIAL ENGLISH WORDS"

Tài liệu này là bộ khung (framework) bắt buộc dành cho bất kỳ AI nào tiếp nhận nhiệm vụ tạo các Unit tiếp theo (Unit 4, 5, 6...) thuộc khóa học "4000 Essential English Words". Vui lòng đọc kỹ và tuân thủ 100% định dạng dưới đây để tránh làm vỡ giao diện hệ thống.

---

## BƯỚC 1: TRÍCH XUẤT VÀ XỬ LÝ NỘI DUNG TỪ PDF
- Đọc nội dung Unit tương ứng từ file `public/4000 english words volume 1.pdf`.
- Lấy chính xác 20 từ vựng, phần định nghĩa (Detailed Meanings), và bài đọc (Comprehensive Reading).
- Lấy toàn bộ các câu hỏi bài tập liên quan đến 20 từ vựng và bài đọc hiểu.

---

## BƯỚC 2: TẠO ẢNH MINH HOẠ BẰNG AI (TỐI QUAN TRỌNG)
**Tuyệt đối KHÔNG** cắt hình ảnh nhàm chán từ file PDF (trừ khi người dùng ép buộc). Toàn bộ ảnh đều phải được tạo bằng AI (`generate_image`) với chất lượng cao nhất:
1. **Ảnh Word List 1 & 2**: Tạo 2 bức ảnh minh hoạ sinh động, phong cách hoạt hình (colorful, cute cartoon, storybook style). Trên ảnh phải có dòng chữ nghệ thuật "FUN WORD ADVENTURES! VOCABULARY FOR KIDS" và lồng ghép 10 từ vựng của mỗi phần trôi nổi trong không gian ảnh.
2. **Ảnh Bài Đọc (Story)**: Đọc nội dung câu chuyện và tạo 1 bức ảnh minh họa sát với bối cảnh truyện (phong cách: high quality, colorful, cute cartoon, storybook style). 
3. **Lưu ý**: Đặt tên ảnh theo cấu trúc `unitX_word_list_1.png`, `unitX_word_list_2.png`, `unitX_story.png` và di chuyển tất cả vào thư mục `public/`.

---

## BƯỚC 3: XÂY DỰNG JSON VÀ HTML ĐÚNG CHUẨN CHO DATABASE
Nội dung của bài học được đẩy vào cột `content_json` trên cơ sở dữ liệu Supabase.
**🚨 YÊU CẦU BẮT BUỘC VỀ CẤU TRÚC JSON:**
Toàn bộ `content_json` phải tuân thủ nghiêm ngặt cấu trúc có khối `basicInfo` (chứa tiêu đề hiển thị cho AdminPanel) và mảng `parts` (mỗi part bắt buộc phải có trường `id` như `"part1"`, `"part2"`):
```json
{
  "basicInfo": {
    "skill": "Standard-Reading",
    "title": "Unit X",
    "category": "exercise",
    "timeLimit": 0
  },
  "parts": [
    {
      "id": "part1",
      "title": "Word List",
      "content": "...",
      "sections": [ ... ]
    },
    {
      "id": "part2",
      "title": "Comprehensive Reading",
      "content": "...",
      "sections": [ ... ]
    }
  ]
}
```

Dưới đây là quy định chi tiết về HTML cho từng tab:

### Tab 1: Word List (`parts[0]`)
HTML của Word List phải bọc trong các thẻ `div` với flex-direction và khoảng cách (`gap`) chuẩn như sau. KHÔNG được tự ý chèn thêm số thứ tự hay khung nền xám!

**🚨 CẢNH BÁO CỰC KỲ QUAN TRỌNG VỀ FORMAT HTML 🚨**
- **TUYỆT ĐỐI KHÔNG ĐƯỢC THÊM KÝ TỰ XUỐNG DÒNG (`\n`), KÝ TỰ TAB (`\t`) HAY THỤT LỀ (INDENT) VÀO TRONG CHUỖI HTML!**
- Toàn bộ chuỗi HTML phải nằm trên **MỘT DÒNG DUY NHẤT** (Minified HTML).
- Nếu bạn dùng template string (backticks) rồi tự ý format HTML cho dễ đọc (xuống dòng, thụt lề), Next.js/React trên frontend sẽ render các khoảng trắng dư thừa này, làm **VỠ HOÀN TOÀN GIAO DIỆN**.
- Bắt buộc phải loại bỏ mọi ký tự `\n`, `\r` và các khoảng trắng dư thừa giữa các thẻ HTML trước khi đưa vào `content_json`.

```html
<!-- Dán đoạn HTML này vào parts[0].content -->
<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unitX_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unitX_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;"><div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">word</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">[phiên âm]</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">loại_từ.</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">Định nghĩa tiếng Anh ở đây.</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ Câu ví dụ tiếng Anh ở đây.</div></div></div></div></div></div>
```

### Câu hỏi trắc nghiệm của Word List (`parts[0].sections`)
Trích xuất bài tập Word List và đẩy vào `sections`. **BẮT BUỘC:** `questionType` phải là `"Trắc nghiệm"`.

```json
[
  {
    "id": "sec1_wordlist",
    "title": "Part A: Choose the right definition for the given word.",
    "content": "",
    "questionType": "Trắc nghiệm",
    "questions": [
      {
        "id": "1",
        "content": "1. friendly",
        "options": ["space", "a list of information", "acting or behaving nicely", "a picture"],
        "correctAnswer": "acting or behaving nicely",
        "explanation": "friendly nghĩa là thân thiện (acting or behaving nicely)."
      }
    ]
  }
]
```

---

### Tab 2: Comprehensive Reading (`parts[1]`)
HTML của bài đọc phải đảm bảo **3 YẾU TỐ**: 
1. **KHÔNG** đặt thẻ `<img src...>` vào bên trong chuỗi HTML. Ảnh minh hoạ phải được truyền qua trường `imageUrl` của object `parts[1]`.
2. **In đậm** (`<b>`) tất cả 20 từ vựng mục tiêu khi chúng xuất hiện trong bài đọc.
3. Các đoạn văn (`<p>`) bắt buộc phải dùng CHÍNH XÁC thông số `style="margin-bottom: 1rem;"`. TUYỆT ĐỐI KHÔNG chèn thêm `font-size`, `line-height`, `color` hay bất kỳ CSS nào khác để tránh làm hỏng font chữ chuẩn của hệ thống. Đồng thời KHÔNG dùng `text-transform: uppercase` ở thẻ `<h1>`.
3. Thẻ `<div>` bọc ngoài cùng phải có CHÍNH XÁC `style="font-family: Arial, sans-serif; "`.

**🚨 CẢNH BÁO HTML 🚨:** Giống như Tab 1, toàn bộ HTML của Tab 2 phải được minified thành **MỘT DÒNG DUY NHẤT**. Tuyệt đối không chứa ký tự xuống dòng (`\n`).

```html
<!-- Dán đoạn HTML này vào parts[1].content -->
<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Tên Câu Chuyện</h1><p style="margin-bottom: 1rem;">Đoạn văn đầu tiên chứa từ vựng được <b>in đậm</b>.</p><p style="margin-bottom: 1rem;">Đoạn văn thứ hai tiếp tục <b>in đậm</b> từ vựng học được trong unit.</p></div>
```

**Quy định nghiêm ngặt cho HTML Bài đọc:**
1. Thẻ `<h1>` giữ NGUYÊN các thuộc tính CSS như trên.
2. Các đoạn văn (`<p>`) bắt buộc phải dùng CHÍNH XÁC thông số `style="margin-bottom: 1rem;"`. TUYỆT ĐỐI KHÔNG chèn thêm font-size, line-height, color hay bất kỳ CSS nào khác để tránh làm hỏng font chữ chuẩn của hệ thống.
3. Toàn bộ chuỗi HTML phải **minified (viết trên cùng 1 dòng)** khi đưa vào code JSON.

Object JSON của Tab 2 sẽ như sau (LƯU Ý phải có `imageUrl`):
```json
{
  "id": "part2",
  "title": "Comprehensive Reading",
  "content": "<div ...>...</div>",
  "imageUrl": "/unitX_story.png",
  "sections": [
    ...
  ]
}
```

### Câu hỏi đọc hiểu (`parts[1].sections`)
Trích xuất câu hỏi đọc hiểu vào mảng sections. **BẮT BUỘC:** `questionType` phải là `"Trắc nghiệm"` và ID câu hỏi phải là duy nhất.

```json
[
  {
    "id": "sec3",
    "title": "Answer the questions based on the story.",
    "content": "",
    "questionType": "Trắc nghiệm",
    "questions": [
      {
        "id": "16",
        "content": "1. What is this story about?",
        "options": ["A", "B", "C", "D"],
        "correctAnswer": "A",
        "explanation": "Chi tiết giải thích lý do chọn A."
      }
    ]
  }
]
```

---

## BƯỚC 4: LƯU VÀ PUSH CODE (BẮT BUỘC)
Sau khi cập nhật xong database qua API Supabase, BẮT BUỘC phải thực hiện thao tác đẩy code chứa các file ảnh AI vừa tạo lên hệ thống lưu trữ Github:

1. Di chuyển vào thư mục dự án.
2. Thêm toàn bộ các thay đổi và file ảnh mới: `git add public/unitX_*.png`
3. Commit rõ ràng: `git commit -m "Add assets and implement Unit X"`
4. Đẩy code lên web: `git push`

**CẢNH BÁO:** Bỏ qua bước đẩy code này sẽ khiến toàn bộ công sức đổ sông đổ bể vì hệ thống Frontend (Vercel/Netlify) sẽ không lấy được hình ảnh hiển thị cho người dùng!
