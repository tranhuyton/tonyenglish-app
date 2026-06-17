import fitz
import sys

def extract_text(pdf_path, out_path, start_page, end_page):
    doc = fitz.open(pdf_path)
    with open(out_path, "w", encoding="utf-8") as f:
        for i in range(start_page, min(end_page, len(doc))):
            f.write(f"--- PAGE {i} ---\n")
            f.write(doc[i].get_text())
            f.write("\n")

extract_text("public/4000 english words volume 2.pdf", "pdf_vol2_text.txt", 0, 195)
extract_text("public/4000 Essential English Words 2 - Answer Key.pdf", "pdf_vol2_key.txt", 0, 30)
print("Done")
