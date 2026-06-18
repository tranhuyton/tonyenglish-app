import sys

try:
    import fitz  # PyMuPDF
    doc = fitz.open('public/4000 english words volume 6.pdf')
    text = ""
    for i in range(20):
        text += doc[i].get_text()
    with open('public/unit1_vol6_text.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully extracted using PyMuPDF")
except ImportError:
    try:
        import PyPDF2
        reader = PyPDF2.PdfReader('public/4000 english words volume 6.pdf')
        text = ""
        for i in range(20):
            text += reader.pages[i].extract_text()
        with open('public/unit1_vol6_text.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Successfully extracted using PyPDF2")
    except ImportError:
        print("Neither PyMuPDF nor PyPDF2 is installed.")
