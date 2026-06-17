import fitz
import sys

def extract_text(pdf_path, out_path, start_page, end_page):
    try:
        doc = fitz.open(pdf_path)
        with open(out_path, "w", encoding="utf-8") as f:
            for i in range(start_page, min(end_page, len(doc))):
                f.write(f"--- PAGE {i} ---\n")
                f.write(doc[i].get_text())
                f.write("\n")
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")

extract_text("public/4000 english words volume 3.pdf", "pdf_vol3_text.txt", 0, 20)
extract_text("public/4000 Essential English Words 3 - Answer Key.pdf", "pdf_vol3_key.txt", 0, 5)
print("Done")
