"""Fix 3 bad crops: fig1.25 (extra heading), fig1.32 (extra text), fig1.36 (cut bottom + extra text)"""
import fitz, glob, io, requests
from PIL import Image

files = glob.glob('dist/Geography/Hodder*.pdf')
doc = fitz.open(files[0])
DPI = 200
SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'

def render(idx): 
    pix = doc[idx].get_pixmap(dpi=DPI)
    return Image.frombytes('RGB', [pix.width, pix.height], pix.samples)

def upload(img, path):
    buf = io.BytesIO()
    img.save(buf, 'PNG')
    r = requests.post(f'{SUPABASE_URL}/storage/v1/object/documents/{path}',
        data=buf.getvalue(),
        headers={'apikey': KEY, 'Authorization': f'Bearer {KEY}',
                 'Content-Type': 'image/png', 'x-upsert': 'true'})
    print(f'  {path}: {"OK" if r.status_code in (200,201) else "FAIL"} ({r.status_code})')

def crop(img, y1, y2, margin_x=80):
    W, H = img.size
    return img.crop((margin_x, max(0,y1), W-margin_x, min(H,y2)))

# Fig 1.25 (idx 27): Remove heading text. Diagram starts at ~y=850
img27 = render(27)
fig125 = crop(img27, 850, 2740)
fig125.save('scratch/fig_previews/fig125_v2.jpg', 'JPEG', quality=85)
upload(fig125, 'geography/tasks/1_2_fig125.png')
print(f'Fig125 new size: {fig125.size}')

# Fig 1.32 (idx 30): Diagram only, starts at ~y=4020 (absolute on full page 30)
img30 = render(30)
H30 = img30.size[1]
# Page 30 at 200 DPI has 5542 rows. Bottom half was 2771-5542.
# Diagram (delta) starts at about 45% into the bottom half = 2771 + 0.45*2771 = 4018
fig132 = crop(img30, 4020, 5542)
fig132.save('scratch/fig_previews/fig132_v2.jpg', 'JPEG', quality=85)
upload(fig132, 'geography/tasks/1_2_fig132.png')
print(f'Fig132 new size: {fig132.size}')

# Fig 1.36 (idx 34): Remove text at top, extend bottom to capture full diagram + caption
# Diagram ("Physical causes" box) starts at ~y80=230 -> y200=575
# Caption at y80=870 -> y200=2175, add margin -> y2=2250
img34 = render(34)
fig136 = crop(img34, 560, 2260)
fig136.save('scratch/fig_previews/fig136_v2.jpg', 'JPEG', quality=85)
upload(fig136, 'geography/tasks/1_3_fig136.png')
print(f'Fig136 new size: {fig136.size}')

print('Done!')
