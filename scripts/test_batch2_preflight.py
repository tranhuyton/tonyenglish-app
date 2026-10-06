# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
from build_bio_batch2 import (
    T6_CODE, T6_ID, T6_TITLE, T6_SEGMENTS, T6_MAJOR_SECTIONS, transform_topic6_html,
    T7_CODE, T7_ID, T7_TITLE, T7_SEGMENTS, T7_MAJOR_SECTIONS, transform_topic7_html,
    T8_CODE, T8_ID, T8_TITLE, T8_SEGMENTS, T8_MAJOR_SECTIONS, transform_topic8_html,
    T9_CODE, T9_ID, T9_TITLE, T9_SEGMENTS, T9_MAJOR_SECTIONS, transform_topic9_html
)

sys.stdout.reconfigure(encoding='utf-8')

tasks = [
    ("Topic 6", T6_SEGMENTS, transform_topic6_html),
    ("Topic 7", T7_SEGMENTS, transform_topic7_html),
    ("Topic 8", T8_SEGMENTS, transform_topic8_html),
    ("Topic 9", T9_SEGMENTS, transform_topic9_html)
]

for name, segs, fn in tasks:
    p1, p2 = fn()
    d1 = p1.count('<div') - p1.count('</div>')
    d2 = p2.count('<div') - p2.count('</div>')
    s1 = BeautifulSoup(p1, 'html.parser')
    s2 = BeautifulSoup(p2, 'html.parser')
    
    missing_p1 = [s['selector'] for s in segs if not s1.select(s['selector'])]
    missing_p2 = [s['selector'] for s in segs if not s2.select(s['selector'])]
    
    print(f"{name}: Div diffs (P1={d1}, P2={d2}) | Total Segs={len(segs)} | Missing P1={missing_p1} | Missing P2={missing_p2}")
    assert d1 == 0 and d2 == 0, f"{name} div diff != 0!"
    assert not missing_p1, f"{name} missing in P1: {missing_p1}"
    assert not missing_p2, f"{name} missing in P2: {missing_p2}"

print("\n🎉 ALL BATCH 2 TOPICS (6, 7, 8, 9) PASSED PRE-FLIGHT WITH 100% SELECTORS AND 0 DIV DIFFS!")
