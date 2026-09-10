import PyPDF2
import sys
import json

def extract_text(pdf_path, out_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for i in range(len(reader.pages)):
            text += f"\n--- PAGE {i+1} ---\n"
            text += reader.pages[i].extract_text()
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    extract_text('public/Geography/09_TOPIC_9_Changing_economies.pdf', 'scratch/topic_9_text.txt')
