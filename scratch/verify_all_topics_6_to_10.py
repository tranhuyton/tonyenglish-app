import json
import os
import re
import sys

sys.path.append('scripts')
from audio_lecture_engine import sb

sys.stdout.reconfigure(encoding='utf-8')

LECTURES = [
    ("6_1", "c6fccfc5-088b-4145-9a23-9cbb2df1cce9", "6.1 Populations Grow and Decline"),
    ("6_2", "5390b0d7-995c-4c18-a092-b5cdd4eda49a", "6.2 Population Structures Change Over Time"),
    ("6_3", "33c91ae9-b13f-49d7-b29f-0c3b794d192d", "6.3 Causes and Impacts of International Migration"),
    ("7_1", "556bc6b6-1555-49a9-a043-35f059b44559", "7.1 Where People Live"),
    ("7_2", "30bae547-a9b0-4c09-8850-ce22b96cfea2", "7.2 The Opportunities and Challenges of Urbanisation"),
    ("7_3", "0b658b3f-bf70-4991-95d5-d65616b7ec1a", "7.3 The Management of Urban Growth"),
    ("8_1", "5ff5f837-df39-4488-bbd2-5138f4faed1e", "8.1 Measuring Development"),
    ("8_2", "9cf90212-43f4-4b28-8014-fd6c130db8ef", "8.2 The World is Developing Unevenly"),
    ("8_3", "7da208d1-559d-4e60-a6a3-ebfb8c2d232f", "8.3 Achieving Sustainable Development"),
    ("9_1", "6c14f92b-774a-45d1-a68d-2e9fe5e0b85d", "9.1 Changing Employment Structures"),
    ("9_2", "5b7da7e1-3da1-4bf4-9700-6e11d7a7ef6b", "9.2 The Impact of Globalisation and TNCs"),
    ("9_3", "53517557-9eb4-450d-a8dd-18b73c71938a", "9.3 Tourism is a Growing Industry"),
    ("10_1", "362104be-aedc-4cbe-87b2-29034e93cc9c", "10.1 How Our Food is Produced: Agricultural Systems"),
    ("10_2", "76dcafbf-e6b8-47f1-8618-be1b14e975ed", "10.2 Global Patterns of Food Supply and Demand"),
    ("10_3", "96d7f427-3b6d-43e3-84dc-f8f052f20033", "10.3 The Challenges of Food Supply: Insecurity & Solutions"),
    ("10_4", "199a26cd-1226-4ff7-b063-f7df7fa7b5ba", "10.4 How Our Energy is Produced: Sources & Systems"),
    ("10_5", "a3a8d904-d277-4eef-b8ff-52a913ebc5f6", "10.5 Global Patterns of Energy Supply and Demand"),
    ("10_6", "fb30c141-db3a-49e8-aa55-028c913640d4", "10.6 The Impacts of Energy Production"),
]

print("=== VERIFYING ALL 18 LECTURES (TOPICS 6 TO 10) ===")

# 1. Check manifests & audio files
all_audio_ok = True
for code, lid, title in LECTURES:
    m_path = f"public/audio/lectures/geography/{code}/manifest.json"
    if not os.path.exists(m_path):
        print(f"❌ Manifest missing: {m_path}")
        all_audio_ok = False
        continue
    with open(m_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    segments = data.get('segments', [])
    dur = data.get('totalDuration', 0)
    
    missing_files = []
    for s in segments:
        f_url = s.get('audioUrl', '')
        rel_f = os.path.join('public', f_url.lstrip('/'))
        if not os.path.exists(rel_f) or os.path.getsize(rel_f) == 0:
            missing_files.append(rel_f)
    
    if missing_files:
        print(f"❌ {code}: Missing {len(missing_files)} audio files!")
        all_audio_ok = False
    else:
        print(f"✅ {code:5s} [{len(segments):2d} segments, {dur:6.1f}s]: All audio files on disk verified!")

if all_audio_ok:
    print("\n🎉 ALL AUDIO FILES & MANIFESTS ARE 100% VALID!")

# 2. Check Supabase Page 1 HTML div balance
print("\n=== CHECKING SUPABASE PAGE 1 HTML DIV BALANCES ===")
all_html_ok = True
for code, lid, title in LECTURES:
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    if not res.data or not res.data[0].get('content_html'):
        print(f"❌ Supabase Page 1 not found for {code} ({lid})")
        all_html_ok = False
        continue
    html = res.data[0]['content_html']
    open_divs = len(re.findall(r'<div\b', html, re.I))
    close_divs = len(re.findall(r'</div\b', html, re.I))
    diff = open_divs - close_divs
    has_card = 'lecture-interactive-card' in html
    if diff == 0 and has_card:
        print(f"✅ {code:5s} ({lid[:8]}...): Open={open_divs:2d}, Close={close_divs:2d}, Diff={diff:2d}, Interactive Cards=YES")
    else:
        print(f"❌ {code:5s} ({lid[:8]}...): Open={open_divs:2d}, Close={close_divs:2d}, Diff={diff:2d}, Cards={has_card}")
        all_html_ok = False

if all_html_ok:
    print("\n🎉 ALL 18 SUPABASE PAGES HAVE DIFF=0 AND ARE 100% BALANCED!")
