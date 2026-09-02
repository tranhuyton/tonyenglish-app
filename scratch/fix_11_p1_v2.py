"""Fix 1.1 page 1: Remove ALL border-radius and box-shadow from img tags using tag-level parsing."""
import json, re, requests

SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'

# Load fixed HTML from previous step
with open('scratch/fixed_11_p1.html', encoding='utf-8') as f:
    html = f.read()

def clean_img_style(match):
    """Clean style attr in img tags: remove border-radius and box-shadow of any value."""
    tag = match.group(0)
    # Find style= attribute in this img tag
    def fix_style(smatch):
        style = smatch.group(1)
        # Remove border-radius: <any value>;
        style = re.sub(r'border-radius:\s*[^;]+;?\s*', '', style)
        # Remove box-shadow: <any value (including rgba)>;
        style = re.sub(r'box-shadow:\s*[^;]*(?:rgba\([^)]*\))[^;]*;?\s*', '', style)
        # Also remove simple box-shadow patterns
        style = re.sub(r'box-shadow:\s*none;?\s*', '', style)
        # Clean up double semicolons / trailing whitespace
        style = re.sub(r';\s*;', ';', style)
        style = style.strip(' ;')
        return f'style="{style}"'
    tag = re.sub(r'style="([^"]*)"', fix_style, tag)
    return tag

# Apply fix to all img tags
html_fixed = re.sub(r'<img[^>]+>', clean_img_style, html)

# Verify
img_tags = re.findall(r'<img[^>]+>', html_fixed)
issues = [t for t in img_tags if 'border-radius' in t or 'box-shadow' in t]
print(f'Remaining img tags with issues: {len(issues)}')
for t in issues:
    print(' ', t[:300])

print(f'Fixed length: {len(html_fixed)}')

# Upload
r = requests.patch(
    f'{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.90d85cb0-b984-4083-864a-8ead0c4119f7',
    json={'content_html': html_fixed},
    headers={
        'apikey': KEY, 'Authorization': f'Bearer {KEY}',
        'Content-Type': 'application/json', 'Prefer': 'return=minimal'
    }
)
print(f'PATCH: HTTP {r.status_code}')
print('Done!')
