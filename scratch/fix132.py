import fitz, glob, io, requests
from PIL import Image

files = glob.glob('dist/Geography/Hodder*.pdf')
doc = fitz.open(files[0])
DPI = 200
SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'

pix = doc[30].get_pixmap(dpi=DPI)
img30 = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
W, H = img30.size
print(f'Page 30 at 200DPI: {W}x{H}')

# Fig 1.32 delta diagram: start earlier to capture full diagram including "Sea or lake" label
# Previous crop started at 4020 and cut the top arrow. Try 3820.
# End at H-180 to avoid page footer/number
fig132 = img30.crop((80, 3820, W-80, H-180))
fig132.save('scratch/fig_previews/fig132_v3.jpg', 'JPEG', quality=85)
print(f'Fig132 v3 size: {fig132.size}')

buf = io.BytesIO()
fig132.save(buf, 'PNG')
r = requests.post(f'{SUPABASE_URL}/storage/v1/object/documents/geography/tasks/1_2_fig132.png',
    data=buf.getvalue(),
    headers={'apikey': KEY, 'Authorization': f'Bearer {KEY}',
             'Content-Type': 'image/png', 'x-upsert': 'true'})
print(f'Upload: {"OK" if r.status_code in (200,201) else "FAIL"} ({r.status_code})')
