"""Fix Lecture 1.1 Page 1: Remove border-radius and box-shadow from img tags."""
import json, re, requests

SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'

# Load existing page 1 HTML
with open('scratch/pages_6286cb6f.json', encoding='utf-8') as f:
    pages = json.load(f)

p1 = next(p for p in pages if p['page_number'] == 1)
PAGE_ID = p1['id']
html = p1['content_html']

print(f'Page 1 ID: {PAGE_ID}')
print(f'Original length: {len(html)}')

# Fix 1: Remove border-radius: 12px from img style attrs
html = re.sub(r';\s*border-radius:\s*12px', '', html)
html = re.sub(r'border-radius:\s*12px;\s*', '', html)

# Fix 2: Remove box-shadow from img tags (keep on divs/containers - only remove where on img)
# Pattern: in img tags, remove box-shadow property
# Use simple replacement of the known shadow value in img contexts
html = re.sub(r';\s*box-shadow:\s*0 4px 6px rgba\(0,0,0,0\.1\)', '', html)
html = re.sub(r'box-shadow:\s*0 4px 6px rgba\(0,0,0,0\.1\);\s*', '', html)

# Fix 3: Normalize max-width to 420px for images (was 450px in old style)
html = html.replace('max-width: 450px;', 'max-width: 420px;')
html = html.replace('max-width: 100%;', 'max-width: 420px;')

print(f'Fixed length: {len(html)}')

# Count remaining border-radius/box-shadow in img tags (verify cleanup)
img_tags = re.findall(r'<img[^>]+>', html)
issues = [t for t in img_tags if 'border-radius' in t or 'box-shadow' in t]
print(f'Remaining img tags with border-radius/box-shadow: {len(issues)}')
for t in issues:
    print(' ', t[:200])

# Save fixed HTML for review
with open('scratch/fixed_11_p1.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Saved to scratch/fixed_11_p1.html')

# PATCH to Supabase
r = requests.patch(
    f'{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.{PAGE_ID}',
    json={'content_html': html},
    headers={
        'apikey': KEY,
        'Authorization': f'Bearer {KEY}',
        'Content-Type': 'application/json',
        'Prefer': 'return=minimal'
    }
)
print(f'PATCH result: HTTP {r.status_code}')
