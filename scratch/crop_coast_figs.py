"""Crop and upload all Topic 2 (Coastal) figures from Hodder PDF at 200 DPI."""
import fitz, glob, io, os, requests
from PIL import Image, ImageDraw

os.makedirs('scratch/fig_previews_t2', exist_ok=True)

SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'

files = glob.glob('dist/Geography/Hodder*.pdf')
doc = fitz.open(files[0])

def render_page(idx, dpi=200):
    pix = doc[idx].get_pixmap(dpi=dpi)
    img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
    return img

def upload_and_preview(img, supabase_path, preview_name):
    # Save preview
    preview = img.copy()
    preview.thumbnail((800, 800), Image.LANCZOS)
    preview.save(f'scratch/fig_previews_t2/{preview_name}.jpg', 'JPEG', quality=85)
    # Upload
    buf = io.BytesIO()
    img.save(buf, 'PNG')
    r = requests.post(
        f'{SUPABASE_URL}/storage/v1/object/documents/geography/tasks/{supabase_path}',
        data=buf.getvalue(),
        headers={'apikey': KEY, 'Authorization': f'Bearer {KEY}',
                 'Content-Type': 'image/png', 'x-upsert': 'true'}
    )
    status = 'OK' if r.status_code in (200, 201) else f'FAIL({r.status_code})'
    print(f'  {supabase_path}: {status} | size: {img.size}')
    return r.status_code

# ── 2.1 FIGURES ──────────────────────────────────────────────────────────────

# Fig 2.2 — Hydraulic action on a coral coastline (idx 052, upper half = big photo)
print('Cropping Fig 2.2...')
p52 = render_page(52)
W, H = p52.size
# Photo takes top ~72% of page
fig22 = p52.crop((80, 80, W-80, int(H*0.72)))
upload_and_preview(fig22, '2_1_fig22.png', 'fig22')

# Fig 2.3 — Longshore drift diagram (idx 053, upper portion)
print('Cropping Fig 2.3...')
p53 = render_page(53)
# Diagram from roughly y=80 to y=2200 (below the longshore drift heading text)
fig23 = p53.crop((80, 80, W-80, 2300))
upload_and_preview(fig23, '2_1_fig23.png', 'fig23')

# Fig 2.6 — Constructive + Destructive waves diagram (idx 055, upper 2/3)
print('Cropping Fig 2.6...')
p55 = render_page(55)
# Both wave diagrams are in the upper portion of the page
fig26 = p55.crop((80, 80, W-80, 2400))
upload_and_preview(fig26, '2_1_fig26.png', 'fig26')

# ── 2.2 FIGURES ──────────────────────────────────────────────────────────────

# Fig 2.9 — Headlands and bays diagram (idx 058, upper diagram section)
print('Cropping Fig 2.9...')
p58 = render_page(58)
# Diagram from top of page to caption below diagram (~y=2300)
fig29 = p58.crop((80, 80, W-80, 2500))
upload_and_preview(fig29, '2_2_fig29.png', 'fig29')

# Fig 2.10 — Headlands and bays photo - Portugal (idx 058, lower photo)
print('Cropping Fig 2.10...')
# Photo is in the lower half of page 58
fig210 = p58.crop((80, 2600, W-80, int(H*0.88)))
upload_and_preview(fig210, '2_2_fig210.png', 'fig210')

# Fig 2.11 — Cave, arch, stack formation diagram (idx 059, upper portion)
print('Cropping Fig 2.11...')
p59 = render_page(59)
# Diagram takes upper ~55% of page
fig211 = p59.crop((80, 80, W-80, int(H*0.57)))
upload_and_preview(fig211, '2_2_fig211.png', 'fig211')

# Fig 2.12 — Arch at Durdle Door photo (idx 059, lower portion)
print('Cropping Fig 2.12...')
# Photo is in the lower half  
fig212 = p59.crop((80, int(H*0.58), W-80, int(H*0.92)))
upload_and_preview(fig212, '2_2_fig212.png', 'fig212')

# Fig 2.21 — Spit formation diagram (idx 064, lower portion)
print('Cropping Fig 2.21...')
p64 = render_page(64)
# Spit diagram is in lower half of page 64
fig221 = p64.crop((80, int(H*0.38), W-80, int(H*0.92)))
upload_and_preview(fig221, '2_2_fig221.png', 'fig221')

# Fig 2.25 — Sand dune formation (idx 067, upper portion)
print('Cropping Fig 2.25...')
p67 = render_page(67)
# Full diagram takes upper ~65% of page
fig225 = p67.crop((80, 80, W-80, int(H*0.65)))
upload_and_preview(fig225, '2_2_fig225.png', 'fig225')

# ── 2.3 FIGURES ──────────────────────────────────────────────────────────────

# Fig 2.29 — Rodney Bay, St Lucia tourist development photo (idx 071, upper photo)
print('Cropping Fig 2.29...')
p71 = render_page(71)
# Photo takes upper ~30% of page
fig229 = p71.crop((80, 80, W-80, int(H*0.32)))
upload_and_preview(fig229, '2_3_fig229.png', 'fig229')

print('\nAll figures done!')
