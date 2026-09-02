import requests, json

KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
HDRS = {'apikey': KEY, 'Authorization': f'Bearer {KEY}'}

PAGE_IDS = {
    '2.1_p1': '4d3d8e74-308a-45b3-a271-300ca98aa673',
    '2.1_p2': '47c476d8-285c-41a9-a158-24194cfaf273',
    '2.2_p1': '55d26cc1-d2f2-4c0e-ac01-b5390cb4315d',
    '2.2_p2': 'ae8dd7f6-0215-45c3-bb94-f60f373c170f',
    '2.3_p1': '5d5f042f-1017-4ca5-ba80-5359f111ac0f',
    '2.3_p2': '225ae3ec-3ab8-485e-b935-551a8df25bed',
}

for name, pid in PAGE_IDS.items():
    r = requests.get(f'{URL}/rest/v1/lecture_pages?id=eq.{pid}&select=id,page_number,content_html', headers=HDRS)
    data = r.json()[0] if r.json() else {}
    html = data.get('content_html') or ''
    print(f'{name} ({pid[:8]}...): {len(html)} chars')
    if html:
        print(f'  Preview: {html[:150]}...')
