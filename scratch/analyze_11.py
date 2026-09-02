import requests

KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
HDRS = {'apikey': KEY, 'Authorization': f'Bearer {KEY}'}

# Fetch 1.1 P1 full content
r = requests.get(f'{URL}/rest/v1/lecture_pages?id=eq.90d85cb0-b984-4083-864a-8ead0c4119f7&select=content_html', headers=HDRS)
html = (r.json()[0] or {}).get('content_html') or ''

# Extract image URLs
import re
imgs = re.findall(r'src="([^"]+)"', html)
print('=== IMAGE URLs in 1.1 P1 ===')
for i in imgs: print(' ', i)

# Extract h2 headings (sections)
h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
print('\n=== SECTIONS (h2) ===')
for h in h2s: print(' ', re.sub(r'<[^>]+>', '', h).strip())

# Extract h3 headings
h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', html, re.DOTALL)
print('\n=== SUB-SECTIONS (h3) ===')
for h in h3s: print(' ', re.sub(r'<[^>]+>', '', h).strip())

print(f'\nTotal chars: {len(html)}')
