import fitz

def pdf_to_images(pdf_path, prefix, start_page, end_page):
    doc = fitz.open(pdf_path)
    for i in range(start_page, min(end_page, len(doc))):
        page = doc[i]
        pix = page.get_pixmap(dpi=150)
        out_path = f"{prefix}_page_{i}.png"
        pix.save(out_path)
        print(f"Saved {out_path}")

pdf_to_images("public/Reading strategies for the ielts test.pdf", "ielts_book", 10, 25)
