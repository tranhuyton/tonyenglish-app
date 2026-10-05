import os
import sys
import re
import json
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
with open(env_path, 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

COURSE_ID = 'f21fe521-aaf9-4917-8c2a-1931666237b5'
BASE_AUDIO_DIR = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'economics')
LECTURE_VIEWER_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'LectureViewer.tsx')

def check_div_balance(html):
    opens = len(re.findall(r'<div\b', html, flags=re.IGNORECASE))
    closes = len(re.findall(r'</div\s*>', html, flags=re.IGNORECASE))
    return opens, closes, opens - closes

def has_study_resources(html):
    patterns = [
        r'Thanh Tài liệu học tập',
        r'Study Resources Bar',
        r'id=[\'"]study-resources-bar[\'"]',
        r'class=[\'"][^\'"]*study-resources[^\'"]*[\'"]'
    ]
    for p in patterns:
        if re.search(p, html, flags=re.IGNORECASE):
            return True
    return False

def verify_all():
    print("=" * 70)
    print("MASTER AUDIT: CAMBRIDGE IGCSE ECONOMICS (LECTURES 1 - 23)")
    print("=" * 70)

    TARGET_LECTURE_IDS = [
        # Topic 1 (1-4)
        ('1fba7e8c-742f-4697-b93e-a0205fc7d825', 1),
        ('34bbcc7c-6b51-40fd-9585-9eb3c37da582', 2),
        ('9b0e6a87-ed26-43bb-a20c-ffa636f9ef11', 3),
        ('9d5f779b-5254-48ed-8284-3918eaacd579', 4),
        # Topic 2 (5-15)
        ('d6e6ad94-1106-43ae-b37c-1b36832f03e6', 5),
        ('71e51517-0174-49fc-9796-802abee0c5a5', 6),
        ('06450a33-0477-4bd2-9d1b-4e424f8e973d', 7),
        ('d15b56e7-9b09-4120-829c-1955efd21602', 8),
        ('763cd322-6b7d-43b0-a18d-15da34137d9d', 9),
        ('16314014-7787-41dc-9ff5-47fd1d2c7409', 10),
        ('4a5f97fd-91d2-41f4-8cbb-b928f5aea5e9', 11),
        ('38954a57-c9bc-4714-b53e-e404e78379cd', 12),
        ('6f3173be-e12a-4a93-8f76-8cb09fb026fe', 13),
        ('69df5ed2-ce91-4e2a-b818-0e2957483b12', 14),
        ('1af33337-f02c-45ff-a8d0-040864272c98', 15),
        # Topic 3 (16-23)
        ('3adca75c-b852-48be-9cbf-5074ae12e430', 16),
        ('123d8a13-d619-45cd-b363-702e9039627a', 17),
        ('95fb66bf-66f0-4bbd-a7e4-418f191f487a', 18),
        ('1943e7bc-cdee-45b1-93d5-830b704a4017', 19),
        ('07e42111-1e2c-4810-bce3-02d8df497c97', 20),
        ('604d1490-caed-47aa-a562-a6a902790a30', 21),
        ('d2019792-c956-44e2-98ed-c247617a9162', 22),
        ('4a814791-86ae-4aab-b9e2-a94b2565c55c', 23),
    ]

    id_to_order = dict(TARGET_LECTURE_IDS)
    target_ids = set(id_to_order.keys())

    # 1. Fetch lectures from Supabase
    res = sb.table('lectures').select('id, title, order_index').in_('id', list(target_ids)).execute()
    lectures = sorted(res.data, key=lambda r: id_to_order.get(r['id'], 999))
    
    # Read LectureViewer.tsx to check manifest mapping
    with open(LECTURE_VIEWER_PATH, 'r', encoding='utf-8') as f:
        lv_code = f.read()

    all_passed = True
    summary_report = []

    for lec in lectures:
        order = id_to_order.get(lec['id'], lec.get('order_index', 0))
        lec_id = lec['id']
        title = lec['title']

        print(f"\n--- [Lecture {order:02d}] {title} ({lec_id}) ---")
        lec_ok = True

        # Check Page 1 in Supabase
        p1 = sb.table('lecture_pages').select('content_html').eq('lecture_id', lec_id).eq('page_number', 1).execute()
        if not p1.data:
            print("  ❌ Page 1 missing in Supabase!")
            lec_ok = False
            p1_html = ""
        else:
            p1_html = p1.data[0]['content_html'] or ""
            opens, closes, diff = check_div_balance(p1_html)
            sr = has_study_resources(p1_html)
            if diff != 0:
                print(f"  ❌ Page 1 Div Imbalance: {diff} (opens={opens}, closes={closes})")
                lec_ok = False
            else:
                print(f"  ✅ Page 1 Div Balance: diff=0")

            if sr:
                print("  ❌ Page 1 Still contains Study Resources!")
                lec_ok = False
            else:
                print("  ✅ Page 1 Study Resources: REMOVED")

            if 'id="sec-header"' not in p1_html and "id='sec-header'" not in p1_html:
                print("  ⚠️ Page 1 Header Banner (#sec-header) missing!")
            else:
                print("  ✅ Page 1 Header Banner: Present")

        # Check Page 2 in Supabase
        p2 = sb.table('lecture_pages').select('content_html').eq('lecture_id', lec_id).eq('page_number', 2).execute()
        if p2.data:
            p2_html = p2.data[0]['content_html'] or ""
            opens, closes, diff = check_div_balance(p2_html)
            sr = has_study_resources(p2_html)
            if diff != 0:
                print(f"  ❌ Page 2 Div Imbalance: {diff}")
                lec_ok = False
            else:
                print(f"  ✅ Page 2 Div Balance: diff=0")

            if sr:
                print("  ❌ Page 2 Still contains Study Resources!")
                lec_ok = False
            else:
                print("  ✅ Page 2 Study Resources: REMOVED")

        # Check Manifest in LectureViewer.tsx
        expected_manifest_path = f"/audio/lectures/economics/{order}/manifest.json"
        if f"'{lec_id}': '{expected_manifest_path}'" in lv_code or f'"{lec_id}": "{expected_manifest_path}"' in lv_code:
            print(f"  ✅ Manifest Mapped in LectureViewer.tsx: {expected_manifest_path}")
        else:
            print(f"  ❌ Manifest NOT properly mapped in LectureViewer.tsx for {lec_id}")
            lec_ok = False

        # Check Manifest & Audio on disk
        manifest_file = os.path.join(BASE_AUDIO_DIR, str(order), "manifest.json")
        if not os.path.exists(manifest_file):
            print(f"  ⏳ Audio/Manifest not yet generated on disk: {manifest_file}")
            lec_ok = False
        else:
            try:
                with open(manifest_file, 'r', encoding='utf-8') as mf:
                    manifest_data = json.load(mf)
                total_dur = manifest_data.get('totalDuration', 0)
                items = manifest_data.get('segments') or manifest_data.get('items', [])
                print(f"  ✅ Manifest on disk: {len(items)} segments, duration={total_dur:.2f}s")
                
                # Check each audio file and target selector
                missing_audio = 0
                missing_sel = 0
                for it in items:
                    af = it.get('audioUrl') or it.get('audioFile')
                    if af:
                        af_path = os.path.join(BASE_AUDIO_DIR, str(order), os.path.basename(af))
                        if not os.path.exists(af_path) or os.path.getsize(af_path) < 1000:
                            missing_audio += 1
                    sel = it.get('targetSelector') or it.get('selector')
                    if sel and p1_html:
                        if sel.startswith('#') and f'id="{sel[1:]}"' not in p1_html and f"id='{sel[1:]}'" not in p1_html:
                            missing_sel += 1
                if missing_audio > 0:
                    print(f"  ❌ Missing or corrupted audio files: {missing_audio}")
                    lec_ok = False
                else:
                    print(f"  ✅ All {len(items)} audio files exist and verified")
                
                if missing_sel > 0:
                    print(f"  ❌ Selectors missing in Supabase Page 1: {missing_sel}")
                    lec_ok = False
                else:
                    print(f"  ✅ All {len(items)} selectors match Page 1 HTML")

            except Exception as e:
                print(f"  ❌ Error reading manifest: {e}")
                lec_ok = False

        summary_report.append((order, title, lec_ok))
        if not lec_ok:
            all_passed = False

    print("\n" + "=" * 70)
    print("FINAL SUMMARY REPORT (LECTURES 1 - 23)")
    print("=" * 70)
    for order, title, ok in summary_report:
        status_str = "✅ PASS" if ok else "⏳ PENDING / FAIL"
        print(f"Lec {order:02d}: {status_str} | {title}")

    return all_passed

if __name__ == '__main__':
    verify_all()
