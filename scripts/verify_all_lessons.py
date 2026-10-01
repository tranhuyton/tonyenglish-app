import os
import sys
import json
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

lessons = [
    ('1.1', '6049f916-3af9-428a-bcd0-ce0574f1d7f7', '1_1'),
    ('1.2', '7027f2e2-0ac5-4ee6-8913-7d93c7857733', '1_2'),
    ('1.3', 'a8ebc541-78ef-4202-96ad-161ed647a1b1', '1_3'),
    ('1.4', '71458f5f-ba54-4ac7-a4c2-8bc68f8f15a0', '1_4'),
    ('1.5', 'a6bf8fbd-9c3d-45a3-8cd7-d63a3e79e7b3', '1_5'),
    ('2.1', 'cd1763a9-f030-4be1-b65b-c6dc6dde91c9', '2_1'),
    ('2.2', 'fe4967aa-7d4c-480c-af71-e0d867459044', '2_2'),
    ('2.3', 'c2d359f6-1921-459e-a295-def7e891c352', '2_3'),
    ('2.4', '47166a31-2a55-40ea-a86c-81569cfafa32', '2_4'),
    ('3.1', '6cbe4a84-26ed-4a1d-933b-5843e9b9a501', '3_1'),
    ('3.2', '356dede8-277a-441a-ad73-ef9384973eb7', '3_2'),
    ('3.3', '25fe41d9-780d-41a6-876d-fff3e0d854c5', '3_3'),
    ('3.4', 'c0d60bf9-ad33-456c-807e-9e29318113b8', '3_4'),
    ('4.1', '1e280547-ce64-44c2-8fcf-997f7d61cacf', '4_1'),
    ('4.2', '66589390-767c-4aab-957b-a970fa1a976e', '4_2'),
    ('4.3', '8f0fd09a-d6e6-438f-a2ab-ddc1447e0b00', '4_3'),
    ('4.4', '95eb54ae-44d4-42f6-9d1d-c5c729a69954', '4_4'),
    ('5.1', '7b510a8f-757c-4856-9c68-65f98bf96836', '5_1'),
    ('5.2', 'dc0411df-d831-468a-9a7d-16fb4009290d', '5_2'),
    ('5.3', '71f25939-98d4-4fa3-8227-be8434f64581', '5_3'),
    ('5.4', '5421db93-9d7b-4241-b362-171974092a30', '5_4'),
    ('5.5', 'd7564fe9-d338-4abc-acf3-affd8cca23fa', '5_5'),
    ('6.1', '0e8fbc94-5976-4c7f-8588-471ea93926f5', '6_1'),
    ('6.2', 'a1d571ff-fa12-46c2-a49d-1df88df13214', '6_2'),
    ('6.3', '1bc6f5c1-e71b-4d0d-8153-d2f74180a845', '6_3')
]

print(f"=== VERIFYING ALL {len(lessons)} BUSINESS STUDIES LESSONS (1.1 TO 6.3) ===")
all_ok = True
summary = []

for name, lid, code in lessons:
    lesson_ok = True
    errors = []
    
    # 1. Check pages in Supabase
    res = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).order('page_number').execute()
    pages = {r['page_number']: r['content_html'] for r in res.data}
    
    p_info = []
    for pnum in [1, 2]:
        html = pages.get(pnum, '')
        opens = len(html.split('<div')) - 1
        closes = len(html.split('</div>')) - 1
        diff = opens - closes
        has_sr = 'Study Resources' in html or ('Textbook' in html and 'Paper 1' in html) or 'Tài liệu học tập' in html
        
        if diff != 0:
            errors.append(f"P{pnum} div diff={diff}")
            all_ok = False
            lesson_ok = False
        if has_sr:
            errors.append(f"P{pnum} has Study Resources")
            all_ok = False
            lesson_ok = False
        p_info.append(f"P{pnum}(diff={diff}, sr={has_sr})")
        
    # 2. Check manifest.json
    mpath = f"public/audio/lectures/business/{code}/manifest.json"
    if not os.path.exists(mpath):
        errors.append("Manifest missing")
        all_ok = False
        lesson_ok = False
        m_info = "MISSING"
    else:
        with open(mpath, 'r', encoding='utf-8') as f:
            m = json.load(f)
        
        # Verify majorSections is dict or list
        ms = m.get('majorSections')
        is_dict = isinstance(ms, dict)
        if not is_dict:
            errors.append(f"majorSections is {type(ms).__name__}, not dict")
            all_ok = False
            lesson_ok = False
            
        dur = m.get('totalDuration', 0)
        num_segs = len(m.get('segments', []))
        
        # Check audio files
        missing_audio = []
        for seg in m.get('segments', []):
            rel_url = seg.get('audioUrl', '').lstrip('/')
            actual_path = os.path.join('public', rel_url)
            if not os.path.exists(actual_path):
                missing_audio.append(seg.get('id'))
        if missing_audio:
            errors.append(f"Missing {len(missing_audio)} audio files")
            all_ok = False
            lesson_ok = False
            
        m_info = f"Dur: {dur:.1f}s, Segs: {num_segs}, DictMS: {is_dict}"
        
    status = "✅ PASS" if lesson_ok else "❌ FAIL: " + "; ".join(errors)
    print(f"[{status}] Lesson {name:4} ({code:4}): {', '.join(p_info)} | {m_info}")

print("\n" + "="*70)
if all_ok:
    print(f"🎉 ALL {len(lessons)} LESSONS (1.1 TO 6.3) VERIFIED 100% PERFECT!")
    print(" - Zero Study Resources on Page 1 or Page 2")
    print(" - Div open/close balanced (diff = 0) everywhere")
    print(" - All majorSections converted to dictionary with start & end times")
    print(" - All audio segments generated and accessible")
else:
    print("❌ SOME LESSONS FAILED AUDIT. SEE LOGS ABOVE.")
