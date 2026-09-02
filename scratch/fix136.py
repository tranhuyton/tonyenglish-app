import fitz, glob, io, requests
from PIL import Image

files = glob.glob('dist/Geography/Hodder*.pdf')
doc = fitz.open(files[0])

# Render page 34 at BOTH 80 and 200 DPI for reference
pix80 = doc[34].get_pixmap(dpi=80)
img80 = Image.frombytes('RGB', [pix80.width, pix80.height], pix80.samples)
print(f'Page 34 at 80DPI: {img80.size}')

pix200 = doc[34].get_pixmap(dpi=200)
img200 = Image.frombytes('RGB', [pix200.width, pix200.height], pix200.samples)
print(f'Page 34 at 200DPI: {img200.size}')

W, H = img200.size

# Crop from Physical causes diagram start to well below caption
# At 80DPI: Physical causes top ~y=230, diagram ends with caption ~y=880
# At 200DPI: 230*2.5=575, 880*2.5=2200
# Give plenty of margin: start at 600 (just after "Elsewhere..." text at y80=220)
# End at 2350 to safely include full caption
fig136 = img200.crop((80, 600, W-80, 2350))
print(f'Fig136 final size: {fig136.size}')

# Save preview
preview = fig136.copy()
preview.thumbnail((800, 800), Image.LANCZOS)
preview.save('scratch/fig_previews/fig136_v3.jpg', 'JPEG', quality=85)
print('Preview saved.')

# Upload
buf = io.BytesIO()
fig136.save(buf, 'PNG')

SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
r = requests.post(f'{SUPABASE_URL}/storage/v1/object/documents/geography/tasks/1_3_fig136.png',
    data=buf.getvalue(),
    headers={'apikey': KEY, 'Authorization': f'Bearer {KEY}',
             'Content-Type': 'image/png', 'x-upsert': 'true'})
print(f'Upload: {"OK" if r.status_code in (200,201) else "FAIL"} ({r.status_code})')
