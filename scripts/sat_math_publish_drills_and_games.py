# -*- coding: utf-8 -*-
"""
Validates and publishes all 12 Digital SAT Math 1500+ Skill Drills (180 Qs)
and 2 Formula & Desmos Speed Games (100 cards) to Supabase.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import sb, load_ids, save_ids, upsert_sat_drill
from sat_qa_validator import validate_sat_test

import sat_math_drills_m1 as m1
import sat_math_drills_m2 as m2
import sat_math_drills_m3 as m3
import sat_math_drills_m4 as m4
import sat_math_games_100 as games_mod

def main():
    print("=== 1. VERIFYING MATH & QA FOR ALL 12 MATH DRILLS (180 Qs) ===", flush=True)
    for mod in (m1, m2, m3, m4):
        mod.verify_all_math()

    all_drills = m1.get_drills() + m2.get_drills() + m3.get_drills() + m4.get_drills()
    assert len(all_drills) == 12, f"Expected 12 math drills, got {len(all_drills)}"

    seen_ids = set()
    total_qs = 0
    for drill_key, title, order_idx, cj in all_drills:
        errs = validate_sat_test(cj, title)
        if errs:
            print(f"[QA FAILED] {title}:", flush=True)
            for e in errs:
                print("  -", e, flush=True)
            sys.exit(1)
        qs = cj['drillModule']['questions']
        total_qs += len(qs)
        for q in qs:
            assert q['id'] not in seen_ids, f"Duplicate question ID across math drills: {q['id']}"
            seen_ids.add(q['id'])
        print(f"  [QA OK] {drill_key}: {len(qs)} Qs", flush=True)

    print(f"\nAll 12 Math Drills verified ({total_qs} unique Qs). Publishing to Supabase...", flush=True)
    for drill_key, title, order_idx, cj in all_drills:
        upsert_sat_drill(drill_key, title, order_idx, cj, folder_key='math_drills')

    print("\n=== 2. PUBLISHING 2 FORMULA & DESMOS SPEED GAMES (100 CARDS) ===", flush=True)
    ids = load_ids()
    course_id = ids['course_id']
    folder_id = ids['folders']['math_games']

    games = games_mod.get_math_games(course_id)
    assert len(games) == 2, f"Expected 2 math games, got {len(games)}"

    for gkey, title, order_idx, theme, cjson in games:
        qs = cjson['parts'][0]['sections'][0]['questions']
        assert len(qs) == 50, f"{gkey} has {len(qs)} cards, expected 50"
        payload = {
            'course_id': course_id,
            'folder_id': folder_id,
            'title': title,
            'test_type': 'MCQ (Standard)',
            'content_json': cjson,
            'is_published': True,
            'order_index': order_idx,
        }
        existing_id = ids.get('math_games', {}).get(gkey)
        tid = None
        if existing_id:
            res = sb.table('tests').update(payload).eq('id', existing_id).execute().data
            if res:
                tid = existing_id
                print(f"  [UPDATED GAME] {title} ({theme})", flush=True)
        if not tid:
            found = sb.table('tests').select('id').eq('course_id', course_id).eq('title', title).execute().data
            if found:
                tid = found[0]['id']
                sb.table('tests').update(payload).eq('id', tid).execute()
                print(f"  [UPDATED GAME] {title} ({theme})", flush=True)
            else:
                tid = sb.table('tests').insert(payload).execute().data[0]['id']
                print(f"  [CREATED GAME] {title} ({theme}) -> {tid}", flush=True)
        ids.setdefault('math_games', {})[gkey] = tid

    save_ids(ids)
    print(f"\n[DONE] Published 12 Math Drills ({total_qs} Qs) + 2 Speed Games (100 cards)!", flush=True)

if __name__ == '__main__':
    main()
