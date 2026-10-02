import json
import os
import sys
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

all_chem = [f"c{i}" for i in range(1, 13)]
all_phys = [f"p{i}" for i in range(1, 7)]

all_pass = True

for code in all_chem + all_phys:
    mf_path = f"public/audio/lectures/science/{code}/manifest.json"
    html_path = f"scripts/raw_science_chem_phys/{code}_p1_transformed.html"
    
    with open(mf_path, 'r', encoding='utf-8') as f:
        mf = json.load(f)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    major_secs = mf.get("majorSections", {})
    if not isinstance(major_secs, dict):
        print(f"[{code.upper()}] ERROR: majorSections is not a dict!")
        all_pass = False
        continue
    
    missing_secs = []
    for sec_key, timing in major_secs.items():
        # Timing check
        if not isinstance(timing, dict) or "start" not in timing or "end" not in timing:
            print(f"[{code.upper()}] ERROR: timing invalid for {sec_key}: {timing}")
            all_pass = False
        
        # DOM check: find card with data-lecture-section or id
        elem = soup.find(attrs={"data-lecture-section": sec_key})
        if not elem:
            # try id
            norm_id = "sec-" + sec_key.replace("_", "-").replace("sec-", "")
            elem = soup.find(id=norm_id) or soup.find(id=sec_key)
        
        if not elem:
            missing_secs.append(sec_key)
        else:
            # check that elem is a div with class lecture-interactive-card
            classes = elem.get('class', [])
            if elem.name != 'div' or 'lecture-interactive-card' not in classes:
                print(f"[{code.upper()}] WARNING: {sec_key} is on <{elem.name} class='{classes}'>, not <div class='lecture-interactive-card'>")
                all_pass = False
                
    if missing_secs:
        print(f"[{code.upper()}] FAIL: Missing selectors in HTML: {missing_secs}")
        all_pass = False
    else:
        print(f"[{code.upper()}] PASS: All {len(major_secs)} sections have corresponding <div class='lecture-interactive-card'>")

print(f"\nAUDIT PASSED FOR ALL 18 LESSONS? {all_pass}")
