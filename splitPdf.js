const { PDFDocument } = require('pdf-lib');
const fs = require('fs');
const path = require('path');

// 1. MẢNG JSON CÁC CHƯƠNG ĐÃ ĐƯỢC CĂN CHỈNH
const chapters = [
  { "chapter": "B1", "title": "Characteristics of living organisms", "startPage": 16, "endPage": 18 },
  { "chapter": "B2", "title": "Cells", "startPage": 19, "endPage": 38 },
  { "chapter": "B3", "title": "Biological molecules", "startPage": 39, "endPage": 42 },
  { "chapter": "B4", "title": "Enzymes", "startPage": 43, "endPage": 48 },
  { "chapter": "B5", "title": "Plant nutrition", "startPage": 49, "endPage": 66 },
  { "chapter": "B6", "title": "Animal nutrition", "startPage": 67, "endPage": 87 },
  { "chapter": "B7", "title": "Transport", "startPage": 88, "endPage": 107 },
  { "chapter": "B8", "title": "Gas exchange and respiration", "startPage": 108, "endPage": 117 },
  { "chapter": "B9", "title": "Co-ordination and response", "startPage": 118, "endPage": 134 },
  { "chapter": "B10", "title": "Reproduction", "startPage": 135, "endPage": 153 },
  { "chapter": "B11", "title": "Inheritance", "startPage": 154, "endPage": 176 },
  { "chapter": "B12", "title": "Organisms and their environment", "startPage": 177, "endPage": 183 },
  { "chapter": "B13", "title": "Human influences on ecosystems", "startPage": 184, "endPage": 190 },
  { "chapter": "C1", "title": "The particulate nature of matter", "startPage": 192, "endPage": 198 },
  { "chapter": "C2", "title": "Experimental techniques", "startPage": 199, "endPage": 205 },
  { "chapter": "C3", "title": "Atoms, elements and compounds", "startPage": 206, "endPage": 230 },
  { "chapter": "C4", "title": "Stoichiometry", "startPage": 231, "endPage": 243 },
  { "chapter": "C5", "title": "Electricity and chemistry", "startPage": 244, "endPage": 256 },
  { "chapter": "C6", "title": "Energy changes in chemical reactions", "startPage": 257, "endPage": 259 },
  { "chapter": "C7", "title": "Chemical reactions", "startPage": 260, "endPage": 268 },
  { "chapter": "C8", "title": "Acids, bases and salts", "startPage": 269, "endPage": 280 },
  { "chapter": "C9", "title": "The Periodic Table", "startPage": 281, "endPage": 289 },
  { "chapter": "C10", "title": "Metals", "startPage": 290, "endPage": 305 },
  { "chapter": "C11", "title": "Air and water", "startPage": 306, "endPage": 322 },
  { "chapter": "C12", "title": "Sulfur", "startPage": 323, "endPage": 325 },
  { "chapter": "C13", "title": "Carbonates", "startPage": 326, "endPage": 329 },
  { "chapter": "C14", "title": "Organic chemistry", "startPage": 330, "endPage": 345 },
  { "chapter": "P1", "title": "Motion", "startPage": 347, "endPage": 372 },
  { "chapter": "P2", "title": "Work, energy and power", "startPage": 373, "endPage": 384 },
  { "chapter": "P3", "title": "Thermal physics", "startPage": 385, "endPage": 401 },
  { "chapter": "P4", "title": "Properties of waves", "startPage": 402, "endPage": 421 },
  { "chapter": "P5", "title": "Electrical quantities, electricity and magnetism", "startPage": 422, "endPage": 435 },
  { "chapter": "P6", "title": "Electric circuits", "startPage": 436, "endPage": 446 },
  { "chapter": "P7", "title": "Electromagnetic effects", "startPage": 447, "endPage": 457 },
  { "chapter": "P8", "title": "Atomic physics", "startPage": 458, "endPage": 466 }
];

// 2. CHÚ Ý: Đảm bảo tên file khớp với file gốc
const bookPath = './Cambridge IGCSE Combined and Co-ordinated Sciences.pdf'; 
const outputFolder = './Chapters';

async function splitPdf() {
  if (!fs.existsSync(bookPath)) {
      console.error(`❌ LỖI: Không tìm thấy file gốc tại đường dẫn: ${bookPath}`);
      return;
  }

  if (!fs.existsSync(outputFolder)) fs.mkdirSync(outputFolder);

  console.log('⏳ Đang nạp file PDF gốc vào bộ nhớ...');
  const pdfBytes = fs.readFileSync(bookPath);

  for (const chap of chapters) {
    console.log(`✂️ Đang xử lý Chapter ${chap.chapter}: ${chap.title}...`);
    
    // Tải lại bản gốc cho mỗi chương để đảm bảo giữ 100% định dạng
    const pdfDoc = await PDFDocument.load(pdfBytes);
    const totalPages = pdfDoc.getPageCount();
    
    // Index bắt đầu từ 0
    const startIndex = Math.max(0, chap.startPage - 1);
    const endIndex = Math.min(totalPages - 1, chap.endPage - 1);
    
    // QUAN TRỌNG: Phải xóa từ trang cuối cùng ngược lên trên
    // Nếu xóa từ trên xuống dưới, index của các trang sẽ bị thay đổi liên tục gây lỗi
    
    // 1. Xóa các trang phía sau chương đang xét
    for (let i = totalPages - 1; i > endIndex; i--) {
        pdfDoc.removePage(i);
    }
    
    // 2. Xóa các trang phía trước chương đang xét
    for (let i = startIndex - 1; i >= 0; i--) {
        pdfDoc.removePage(i);
    }

    // Làm sạch tên file
    const safeTitle = chap.title.replace(/[^a-zA-Z0-9]/g, '_');
    const outPath = path.join(outputFolder, `Chap_${chap.chapter}_${safeTitle}.pdf`);
    
    const newPdfBytes = await pdfDoc.save();
    fs.writeFileSync(outPath, newPdfBytes);
    
    console.log(`✅ Đã lưu: ${outPath}`);
  }
  
  // Em sửa lại số log ở đây một chút vì mảng JSON của anh có 35 chương chứ không phải 16.
  console.log(`🎉 XUẤT SẮC! Đã cắt xong toàn bộ cuốn sách thành ${chapters.length} chương riêng biệt với chất lượng nguyên bản!`);
}

splitPdf().catch(console.error);