# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
from build_bio_batch4 import (
    T14_CODE, T14_ID, T14_TITLE, T14_SEGMENTS, T14_MAJOR_SECTIONS, transform_topic14_html,
    T15_CODE, T15_ID, T15_TITLE, T15_SEGMENTS, T15_MAJOR_SECTIONS, transform_topic15_html,
    T16_CODE, T16_ID, T16_TITLE, T16_SEGMENTS, T16_MAJOR_SECTIONS, transform_topic16_html,
    T17_CODE, T17_ID, T17_TITLE, T17_SEGMENTS, T17_MAJOR_SECTIONS, transform_topic17_html
)

sys.stdout.reconfigure(encoding='utf-8')

tasks = [
    ("Topic 14", T14_SEGMENTS, transform_topic14_html),
    ("Topic 15", T15_SEGMENTS, transform_topic15_html),
    ("Topic 16", T16_SEGMENTS, transform_topic16_html),
    ("Topic 17", T17_SEGMENTS, transform_topic17_html)
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

print("\n🎉 ALL BATCH 4 TOPICS (14, 15, 16, 17) PASSED PRE-FLIGHT WITH 100% SELECTORS AND 0 DIV DIFFS!")
