import json
import sys
import os

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

print("=== UPDATING MAJORSECTIONS IN MANIFESTS B1 TO B19 ===")

for i in range(1, 20):
    code = f"b{i}"
    mpath = f"public/audio/lectures/science/{code}/manifest.json"
    
    with open(mpath, 'r', encoding='utf-8') as f:
        m = json.load(f)
        
    segs = m.get('segments', [])
    new_ms = {}
    
    # 1. intro
    new_ms["intro"] = {"start": 0, "end": 0}
    new_ms["sec-header"] = {"start": 0, "end": 0}
    
    # 2. Each section
    for idx, s in enumerate(segs):
        sid = s['id']
        if sid == 'intro':
            continue
        
        # Calculate range (to next sec_ or end of segments)
        start_idx = idx
        end_idx = idx
        for j in range(idx + 1, len(segs)):
            if segs[j]['id'].startswith('sec_'):
                break
            end_idx = j
            
        new_ms[sid] = {"start": start_idx, "end": end_idx}
        dom_id = sid.replace('_', '-')
        new_ms[dom_id] = {"start": start_idx, "end": end_idx}
        
    m['majorSections'] = new_ms
    
    with open(mpath, 'w', encoding='utf-8') as f:
        json.dump(m, f, ensure_ascii=False, indent=2)
        
    print(f"Updated {code.upper():4}: {len(new_ms)} keys in majorSections dictionary")

print("\n🎉 ALL 19 MANIFESTS SUCCESSFULLY UPDATED TO DICTIONARIES!")
