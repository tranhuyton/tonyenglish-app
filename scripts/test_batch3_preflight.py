# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
from build_bio_batch3 import (
    T10_CODE, T10_ID, T10_TITLE, T10_SEGMENTS, T10_MAJOR_SECTIONS, transform_topic10_html,
    T11_CODE, T11_ID, T11_TITLE, T11_SEGMENTS, T11_MAJOR_SECTIONS, transform_topic11_html,
    T12_CODE, T12_ID, T12_TITLE, T12_SEGMENTS, T12_MAJOR_SECTIONS, transform_topic12_html,
    T13_CODE, T13_ID, T13_TITLE, T13_SEGMENTS, T13_MAJOR_SECTIONS, transform_topic13_html
)

sys.stdout.reconfigure(encoding='utf-8')

tasks = [
    ("Topic 10", T10_SEGMENTS, transform_topic10_html),
    ("Topic 11", T11_SEGMENTS, transform_topic11_html),
    ("Topic 12", T12_SEGMENTS, transform_topic12_html),
    ("Topic 13", T13_SEGMENTS, transform_topic13_html)
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

print("\n🎉 ALL BATCH 3 TOPICS (10, 11, 12, 13) PASSED PRE-FLIGHT WITH 100% SELECTORS AND 0 DIV DIFFS!")
