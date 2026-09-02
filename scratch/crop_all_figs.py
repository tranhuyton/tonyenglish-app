"""
Comprehensive crop + upload script for all Lecture 1.2 and 1.3 figures.
Crops at 200 DPI from Hodder PDF and uploads to Supabase.
"""
import fitz, glob, io, requests, os
from PIL import Image
import numpy as np

files = glob.glob('dist/Geography/Hodder*.pdf')
doc = fitz.open(files[0])
DPI = 200
SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
os.makedirs('scratch/fig_previews', exist_ok=True)

def render_page(idx):
    pix = doc[idx].get_pixmap(dpi=DPI)
    return Image.frombytes('RGB', [pix.width, pix.height], pix.samples)

def upload(png_bytes, path):
    r = requests.post(
        f'{SUPABASE_URL}/storage/v1/object/documents/{path}',
        data=png_bytes,
        headers={'apikey': KEY, 'Authorization': f'Bearer {KEY}',
                 'Content-Type': 'image/png', 'x-upsert': 'true'}
    )
    ok = r.status_code in (200, 201)
    print(f'  Upload {path}: {"OK" if ok else "FAIL"} ({r.status_code})')
    return ok

def crop_save_upload(img, y1, y2, fname, preview_fname, x_margin=80):
    W, H = img.size
    x1, x2 = x_margin, W - x_margin
    y1, y2 = max(0, y1), min(H, y2)
    cropped = img.crop((x1, y1, x2, y2))
    # Save preview
    preview = cropped.copy()
    preview.thumbnail((800, 800), Image.LANCZOS)
    preview.save(f'scratch/fig_previews/{preview_fname}', 'JPEG', quality=85)
    # Upload PNG
    buf = io.BytesIO()
    cropped.save(buf, 'PNG')
    upload(buf.getvalue(), f'geography/tasks/{fname}')
    print(f'  Size: {cropped.size}')

# ===== Scale factor: 80 DPI preview coords * 2.5 = 200 DPI =====
# Page size at 200 DPI: 3917x5542

print('Rendering pages...')
img23 = render_page(23)
img24 = render_page(24)
img25 = render_page(25)
img27 = render_page(27)
img28 = render_page(28)
img29 = render_page(29)
img30 = render_page(30)  # For Fig 1.32 delta formation
img32 = render_page(32)
img33 = render_page(33)
img34 = render_page(34)
img37 = render_page(37)
img39 = render_page(39)
print('All pages rendered.\n')

# ===== LECTURE 1.2 FIGURES =====
print('--- LECTURE 1.2 ---')

# Fig 1.18 (idx 23): Upper course V-shaped valley PHOTO (Switzerland)
# Visual: photo from y80~290 to ~1180 -> 200DPI: 725 to 2950
print('Fig 1.18...')
crop_save_upload(img23, 725, 2980, '1_2_fig118.png', 'fig118.jpg')

# Fig 1.19 (idx 24): Interlocking spurs (Waitaki River NZ) - top of page
# Visual: y80 ~10 to ~680 -> 200DPI: 25 to 1700
print('Fig 1.19...')
crop_save_upload(img24, 30, 1720, '1_2_fig119.png', 'fig119.jpg')

# Fig 1.20 (idx 24): Potholes (River Wharfe) - bottom of page
# Visual: y80 ~1155 to ~1865 -> 200DPI: 2890 to 4665
print('Fig 1.20...')
crop_save_upload(img24, 2880, 4680, '1_2_fig120.png', 'fig120.jpg')

# Fig 1.21 (idx 25): Waterfall formation diagram - top of page
# Visual: y80 ~10 to ~560 -> 200DPI: 25 to 1400
print('Fig 1.21...')
crop_save_upload(img25, 30, 1420, '1_2_fig121.png', 'fig121.jpg')

# Fig 1.22 (idx 25): Gorge of recession diagram - middle of page
# Visual: y80 ~1050 to ~1490 -> 200DPI: 2625 to 3725
print('Fig 1.22...')
crop_save_upload(img25, 2620, 3740, '1_2_fig122.png', 'fig122.jpg')

# Fig 1.25 (idx 27): Cross-section of meander (large diagram)
# Visual: y80 ~265 to ~1090 -> 200DPI: 663 to 2725
print('Fig 1.25...')
crop_save_upload(img27, 660, 2740, '1_2_fig125.png', 'fig125.jpg')

# Fig 1.26 (idx 27): Processes on inside/outside banks
# Visual: y80 ~1600 to ~1900 -> 200DPI: 4000 to 4750
print('Fig 1.26...')
crop_save_upload(img27, 3990, 4770, '1_2_fig126.png', 'fig126.jpg')

# Fig 1.27 (idx 28): Meander PHOTO (Marsyangdi River Nepal) - top
# Visual: y80 ~10 to ~580 -> 200DPI: 25 to 1450
print('Fig 1.27...')
crop_save_upload(img28, 30, 1470, '1_2_fig127.png', 'fig127.jpg')

# Fig 1.28 (idx 28): Oxbow lake formation (sequence diagram) - bottom
# Visual: y80 ~1610 to ~2150 -> 200DPI: 4025 to 5375
print('Fig 1.28...')
crop_save_upload(img28, 4010, 5380, '1_2_fig128.png', 'fig128.jpg')

# Fig 1.29 (idx 29): Floodplain cross-section (diagram) - top
# Visual: y80 ~10 to ~400 -> 200DPI: 25 to 1000
print('Fig 1.29...')
crop_save_upload(img29, 30, 1010, '1_2_fig129.png', 'fig129.jpg')

# Fig 1.30 (idx 29): Floodplain PHOTO (River Tuul, Mongolia)
# Visual: y80 ~445 to ~1190 -> 200DPI: 1113 to 2975
print('Fig 1.30...')
crop_save_upload(img29, 1100, 2990, '1_2_fig130.png', 'fig130.jpg')

# Fig 1.32 (idx 30): Delta formation diagram - on PAGE 30 (caption at top of page 31)
# Need to inspect page 30 - render done above
# This is typically at the BOTTOM of page 30 (end of 1.2 section)
# Just crop a wide range from middle down
print('Fig 1.32 (from page 30)...')
W30, H30 = img30.size
# Delta formation is likely in the lower half of page 30
# Crop from 50% height down
crop_save_upload(img30, H30//2, H30, '1_2_fig132.png', 'fig132.jpg')

print('\n--- LECTURE 1.3 ---')

# Fig 1.34 (idx 32): Farming in Nile valley PHOTO
# Visual: y80 ~755 to ~1415 -> 200DPI: 1888 to 3538
print('Fig 1.34...')
crop_save_upload(img32, 1880, 3550, '1_3_fig134.png', 'fig134.jpg')

# Fig 1.35 (idx 33): Danube locks PHOTO - top of page
# Visual: y80 ~10 to ~740 -> 200DPI: 25 to 1850
print('Fig 1.35...')
crop_save_upload(img33, 30, 1870, '1_3_fig135.png', 'fig135.jpg')

# Fig 1.36 (idx 34): Natural + human causes of floods DIAGRAM
# Visual: y80 ~155 to ~840 -> 200DPI: 388 to 2100
print('Fig 1.36...')
crop_save_upload(img34, 380, 2120, '1_3_fig136.png', 'fig136.jpg')

# Fig 1.38 (idx 37): Hard engineering (two photos: Thames + Zermatt)
# Visual: y80 ~10 to ~1300 -> 200DPI: 25 to 3250
print('Fig 1.38...')
crop_save_upload(img37, 30, 3280, '1_3_fig138.png', 'fig138.jpg')

# Fig 1.40 (idx 39): SuDS methods diagram
# Visual: y80 ~685 to ~1760 -> 200DPI: 1713 to 4400
print('Fig 1.40...')
crop_save_upload(img39, 1700, 4420, '1_3_fig140.png', 'fig140.jpg')

print('\nAll figures cropped and uploaded!')
print('Check previews in scratch/fig_previews/')
