# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
from build_bio_batch5 import (
    T18_CODE, T18_ID, T18_TITLE, T18_SEGMENTS, T18_MAJOR_SECTIONS, transform_topic18_html,
    T19_CODE, T19_ID, T19_TITLE, T19_SEGMENTS, T19_MAJOR_SECTIONS, transform_topic19_html,
    T20_CODE, T20_ID, T20_TITLE, T20_SEGMENTS, T20_MAJOR_SECTIONS, transform_topic20_html,
    T21_CODE, T21_ID, T21_TITLE, T21_SEGMENTS, T21_MAJOR_SECTIONS, transform_topic21_html
)

sys.stdout.reconfigure(encoding='utf-8')

tasks = [
    ("Topic 18", T18_SEGMENTS, transform_topic18_html),
    ("Topic 19", T19_SEGMENTS, transform_topic19_html),
    ("Topic 20", T20_SEGMENTS, transform_topic20_html),
    ("Topic 21", T21_SEGMENTS, transform_topic21_html)
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

print("\n🎉 ALL BATCH 5 TOPICS (18, 19, 20, 21) PASSED PRE-FLIGHT WITH 100% SELECTORS AND 0 DIV DIFFS!")
