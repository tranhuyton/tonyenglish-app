import os
import json

topics = ['3_1', '3_2', '3_3', '3_4', '4_1', '4_2', '4_3', '4_4', '5_1', '5_2', '5_3']
for t in topics:
    p = f'public/audio/lectures/geography/{t}/manifest.json'
    if not os.path.exists(p):
        print(f'{t}: MANIFEST NOT FOUND!')
        continue
    with open(p, 'r', encoding='utf-8') as f:
        m = json.load(f)
    ms = m.get('majorSections')
    ms_type = type(ms).__name__
    num_segs = len(m.get('segments', []))
    dur = m.get('totalDuration', 0)
    segs = [s.get('id') + ' (' + s.get('selector', '') + ')' for s in m.get('segments', [])]
    title = m.get('lectureTitle', '')
    print(f"{t}: {title} | MS: {ms_type} | Segs: {num_segs} | Dur: {dur:.1f}s")
    print("   Segments:", ", ".join(segs[:6]), "..." if len(segs) > 6 else "")
    if isinstance(ms, dict):
        print("   MajorSections keys:", list(ms.keys()))
    elif isinstance(ms, list):
        print("   MajorSections list:", [item.get('id') for item in ms])
