import fitz

def extract_text(pdf_path, out_path, start_page, end_page):
    doc = fitz.open(pdf_path)
    with open(out_path, "w", encoding="utf-8") as f:
        for i in range(start_page, min(end_page, len(doc))):
            f.write(f"--- PAGE {i} ---\n")
            f.write(doc[i].get_text())
            f.write("\n")

extract_text("public/Reading strategies for the ielts test - Answer Key.pdf", "ielts_key.txt", 0, 15)
print("Extracted answer key")
