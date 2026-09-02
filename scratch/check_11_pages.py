import requests, sys

KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
HDRS = {'apikey': KEY, 'Authorization': f'Bearer {KEY}'}

pages = {
    '1.1_p1': '90d85cb0-b984-4083-864a-8ead0c4119f7',
    '1.1_p2': 'c27766f1-0030-4641-8d82-d3771b354e01',
}

for name, pid in pages.items():
    r = requests.get(f'{URL}/rest/v1/lecture_pages?id=eq.{pid}&select=id,content_html', headers=HDRS)
    html = (r.json()[0] or {}).get('content_html') or ''
    print(f'\n=== {name} ({pid[:8]}): {len(html)} chars ===')
    # Print first 3000 chars
    print(html[:3000])
    print('...[truncated]...')
