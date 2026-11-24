# -*- coding: utf-8 -*-
"""
Idempotently upgrades Module & Folder architecture for BOTH:
  - IGCSE - Maths-0580 (7211abb0-ccba-479f-92ad-2d218121f717):
      4 color-coded Modules + 2 new dedicated 2025-2027 folders:
      `🚫 Paper 2: Non-Calculator Mastery (2025–2027)` & `🧮 Paper 4: Calculator Mastery (2025–2027)`
      + renames `Topic 9: Statistic` -> `Topic 9: Statistics`
      + labels existing 6 Past Papers clearly with [Non-Calc] vs [Calculator]
  - IGCSE - Maths-0606 (0a8d7434-262a-4462-89c1-2b01c6ea1e4e):
      5 color-coded Modules + 4 clean Folders:
      `📘 Topical Drills — Part 1: Algebra, Logs & Circle (Ch. 1–7B)`
      `📐 Topical Drills — Part 2: Trig, Series, Vectors & Calculus (Ch. 8–16)`
      `🚫 Paper 1 Non-Calculator Specialist Drills (2025–2027)`
      `📜 Past Papers & Full Mock Exams (2025–2027)` (renamed from `Test`)

Preserves 100% of existing Lecture UUIDs & Test UUIDs!
Saves all resolved IDs into `scripts/igcse_maths_ids.json`.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from igcse_maths_pipeline import (
    COURSE_0580_ID,
    COURSE_0606_ID,
    sb_get,
    sb_post,
    sb_patch,
    load_ids,
    save_ids,
)


def ensure_module(course_id, title, order_index, existing_mods, reuse_id=None):
    if reuse_id:
        sb_patch(f'lecture_modules?id=eq.{reuse_id}', {'title': title, 'order_index': order_index})
        print(f"  [UPDATED MOD] #{order_index} {title} ({reuse_id})")
        return reuse_id
    for m in existing_mods:
        if (m.get('title') or '').strip() == title.strip():
            sb_patch(f'lecture_modules?id=eq.{m["id"]}', {'order_index': order_index})
            print(f"  [EXISTS MOD]  #{order_index} {title} ({m['id']})")
            return m['id']
    created = sb_post('lecture_modules', {
        'course_id': course_id,
        'title': title,
        'order_index': order_index,
    })
    mid = created[0]['id']
    print(f"  [CREATED MOD] #{order_index} {title} ({mid})")
    return mid


def ensure_folder(course_id, title, display_order, existing_folders, reuse_id=None, thumbnail_url=None):
    if reuse_id:
        payload = {'title': title, 'display_order': display_order}
        if thumbnail_url:
            payload['thumbnail_url'] = thumbnail_url
        sb_patch(f'folders?id=eq.{reuse_id}', payload)
        print(f"  [UPDATED FOLDER] #{display_order} {title} ({reuse_id})")
        return reuse_id
    for f in existing_folders:
        if (f.get('title') or '').strip() == title.strip():
            sb_patch(f'folders?id=eq.{f["id"]}', {'display_order': display_order})
            print(f"  [EXISTS FOLDER]  #{display_order} {title} ({f['id']})")
            return f['id']
    payload = {
        'course_id': course_id,
        'title': title,
        'display_order': display_order,
    }
    if thumbnail_url:
        payload['thumbnail_url'] = thumbnail_url
    created = sb_post('folders', payload)
    fid = created[0]['id']
    print(f"  [CREATED FOLDER] #{display_order} {title} ({fid})")
    return fid


def setup_0580(ids):
    print("\n=== SETTING UP IGCSE MATHS 0580 (2025-2027 ARCHITECTURE) ===", flush=True)
    mods = sb_get(f'lecture_modules?course_id=eq.{COURSE_0580_ID}&order=order_index.asc&select=*')
    lecs = sb_get(f'lectures?course_id=eq.{COURSE_0580_ID}&order=order_index.asc&select=id,title,order_index,module_id')
    folders = sb_get(f'folders?course_id=eq.{COURSE_0580_ID}&order=display_order.asc&select=*')
    tests = sb_get(f'tests?course_id=eq.{COURSE_0580_ID}&test_type=eq.IGCSE-Direct&select=id,title,content_json')

    m1_id = ensure_module(COURSE_0580_ID, '1. Number & Algebra (2025–2027) [color:#dbeafe,#1e3a8a]', 1, mods, reuse_id='70d82f30-861b-45ad-81a3-52af4e97847b')
    m2_id = ensure_module(COURSE_0580_ID, '2. Coordinate, Geometry & Mensuration [color:#d1fae5,#065f46]', 2, mods)
    m3_id = ensure_module(COURSE_0580_ID, '3. Trigonometry, Vectors, Prob & Stats [color:#fef3c7,#b45309]', 3, mods)
    m4_id = ensure_module(COURSE_0580_ID, '4. Paper 2 (Non-Calc) & Paper 4 (Calc) Mastery [color:#fee2e2,#991b1b]', 4, mods)

    # Re-assign existing 10 lectures cleanly to their thematic modules (preserving UUIDs!)
    mod_map = {
        'ba51741b-3534-4ceb-b6a3-15a9c73e0676': (m1_id, 1),  # Topic 1: Number
        '1a32c5e3-4c4c-4af8-9c97-20beff177f28': (m1_id, 2),  # Topic 2: Algebra and graphs
        '2fd58c65-e34a-4246-a7f5-6b8d6c217389': (m2_id, 1),  # Topic 3: Coordinate geometry
        'fc09421c-8575-48fa-a89e-4107213f13a4': (m2_id, 2),  # Topic 4: Geometry
        'adaa9f75-8966-4fce-a899-af02bd6be790': (m2_id, 3),  # Topic 5: Mensuration
        '4f18be76-c754-4401-86a6-7ac3c74ae400': (m3_id, 1),  # Topic 6: Trigonometry
        '43613f7b-d2d6-48d3-970c-19619c42a0fe': (m3_id, 2),  # Topic 7: Vectors and transformation
        '4876cb39-b169-47a2-94b1-d4737dc767e8': (m3_id, 3),  # Topic 8: Probability
        '86c531a2-1c21-40a3-828f-b59e531a2bee': (m3_id, 4),  # Topic 9: Statistics
        '975e20ef-ab09-4aca-a1fb-a1e64f07a91e': (m4_id, 1),  # Year End Revision
    }
    for lid, (mid, oidx) in mod_map.items():
        sb_patch(f'lectures?id=eq.{lid}', {'module_id': mid, 'order_index': oidx})
    print("  [OK] Mapped 10 existing 0580 lectures across 4 Modules (UUIDs preserved).")

    # Fix Topic 9 folder typo `Statistic` -> `Statistics`
    for f in folders:
        if f.get('title') == 'Topic 9: Statistic':
            sb_patch(f'folders?id=eq.{f["id"]}', {'title': 'Topic 9: Statistics'})
            print("  [FIXED] Folder typo 'Topic 9: Statistic' -> 'Topic 9: Statistics'")

    # Create 2 dedicated Calculator vs Non-Calculator folders
    f_noncalc = ensure_folder(
        COURSE_0580_ID,
        '🚫 Paper 2: Non-Calculator Mastery (2025–2027)',
        10,
        folders,
        thumbnail_url='/images/maths_0580_cover.jpg',
    )
    f_calc = ensure_folder(
        COURSE_0580_ID,
        '🧮 Paper 4: Calculator Mastery (2025–2027)',
        11,
        folders,
        thumbnail_url='/images/maths_0580_cover.jpg',
    )

    # Clearly tag existing 6 IGCSE-Direct Past Papers with Non-Calculator vs Calculator metadata
    for t in tests:
        title = t.get('title') or ''
        cj = t.get('content_json') or {}
        bi = cj.get('basicInfo') or {}
        if any(code in title for code in ('0580/21', '0580/22', '0580/23')):
            bi['calculatorPolicy'] = 'non-calculator'
            new_title = title if 'Non-Calc' in title else title.replace('Paper 2 (Extended)', 'Paper 2 (Extended • 🚫 Non-Calc)')
        elif any(code in title for code in ('0580/41', '0580/42', '0580/43')):
            bi['calculatorPolicy'] = 'calculator'
            new_title = title if 'Calculator' in title else title.replace('Paper 4 (Extended)', 'Paper 4 (Extended • 🧮 Calculator)')
        else:
            continue
        cj['basicInfo'] = bi
        sb_patch(f'tests?id=eq.{t["id"]}', {'title': new_title, 'content_json': cj})
    print("  [OK] Tagged 6 existing 0580 Past Papers with Non-Calculator vs Calculator policies.")

    ids['m0580'] = {
        'course_id': COURSE_0580_ID,
        'modules': {'m1': m1_id, 'm2': m2_id, 'm3': m3_id, 'm4': m4_id},
        'folders': {
            'non_calc': f_noncalc,
            'calc': f_calc,
            'past_papers': next((f['id'] for f in folders if f['title'] == 'Past Papers'), None),
        },
        'lectures': {
            't1': 'ba51741b-3534-4ceb-b6a3-15a9c73e0676',
            't2': '1a32c5e3-4c4c-4af8-9c97-20beff177f28',
            't3': '2fd58c65-e34a-4246-a7f5-6b8d6c217389',
            't4': 'fc09421c-8575-48fa-a89e-4107213f13a4',
            't5': 'adaa9f75-8966-4fce-a899-af02bd6be790',
            't6': '4f18be76-c754-4401-86a6-7ac3c74ae400',
            't7': '43613f7b-d2d6-48d3-970c-19619c42a0fe',
            't8': '4876cb39-b169-47a2-94b1-d4737dc767e8',
            't9': '86c531a2-1c21-40a3-828f-b59e531a2bee',
            'rev': '975e20ef-ab09-4aca-a1fb-a1e64f07a91e',
        },
    }


def setup_0606(ids):
    print("\n=== SETTING UP IGCSE MATHS 0606 (2025-2027 ARCHITECTURE) ===", flush=True)
    mods = sb_get(f'lecture_modules?course_id=eq.{COURSE_0606_ID}&order=order_index.asc&select=*')
    folders = sb_get(f'folders?course_id=eq.{COURSE_0606_ID}&order=display_order.asc&select=*')

    m1_id = ensure_module(COURSE_0606_ID, '1. Functions, Quadratics & Polynomials [color:#dbeafe,#1e3a8a]', 1, mods, reuse_id='3ef0e2b1-077f-4dee-9e7d-73771d15310d')
    m2_id = ensure_module(COURSE_0606_ID, '2. Logs, Exponentials & Coordinate Geometry (incl. Circle 2025+) [color:#d1fae5,#065f46]', 2, mods)
    m3_id = ensure_module(COURSE_0606_ID, '3. Circular Measure, Trigonometry & Series [color:#fef3c7,#b45309]', 3, mods)
    m4_id = ensure_module(COURSE_0606_ID, '4. Vectors, Calculus & Kinematics [color:#f3e8ff,#6b21a8]', 4, mods)
    m5_id = ensure_module(COURSE_0606_ID, '5. Paper 1 (Non-Calc) & Paper 2 (Calc) Exam Mastery [color:#fee2e2,#991b1b]', 5, mods)

    # Map existing 16 chapters cleanly across Modules 1–4 (preserving all 16 UUIDs!)
    lec_map = {
        'c1':  ('fb709e70-5e87-4170-a402-3df6f8cd8ab2', m1_id, 1),
        'c2':  ('62e0cae0-9060-4d03-bd41-18c5b802750b', m1_id, 2),
        'c3':  ('c9c6fcb7-eca7-440e-bc23-cf7b073aaf11', m1_id, 3),
        'c4':  ('17ae5c54-c9f3-49b1-9445-182fb99f9f83', m1_id, 4),
        'c5':  ('325cf10f-5f1c-415f-80ef-0deeed81b19b', m1_id, 5),
        'c6':  ('634a0bca-84ef-4488-94c1-341365b348c3', m2_id, 1),
        'c7':  ('e59e63bd-7f93-41b2-8c56-0234feabb0a7', m2_id, 2),
        # c7b (Circle) will be order_index 3 in m2_id!
        'c8':  ('22e303ce-cd22-426c-89ac-706897703fa6', m3_id, 1),
        'c9':  ('b7057bbf-6016-49ce-b66b-82c55bb46cb7', m3_id, 2),
        'c10': ('af96781b-036b-412e-97ff-075ab08e8297', m3_id, 3),
        'c11': ('c9006f7d-0a9f-4ec3-9206-b8679cfc69ba', m3_id, 4),
        'c12': ('6954f6f9-de52-42cd-93a7-43329dd28c0d', m4_id, 1),
        'c13': ('8c56b240-1273-4d62-968c-603c2ccb651c', m4_id, 2),
        'c14': ('ee577f38-f621-4539-9e94-c374ab08c8df', m4_id, 3),
        'c15': ('54a14d81-be80-4fd6-98b6-1213cde55629', m4_id, 4),
        'c16': ('43e0d3a5-23cd-498a-b2eb-17a60b2b80d8', m4_id, 5),
    }
    for code, (lid, mid, oidx) in lec_map.items():
        sb_patch(f'lectures?id=eq.{lid}', {'module_id': mid, 'order_index': oidx})
    print("  [OK] Mapped 16 existing 0606 lectures across Modules 1–4 (UUIDs preserved).")

    # Rename `Test` folder -> `📜 Past Papers & Full Mock Exams (2025–2027)`
    existing_test_folder = next((f['id'] for f in folders if f['title'] in ('Test', '📜 Past Papers & Full Mock Exams (2025–2027)')), None)
    f_p1 = ensure_folder(COURSE_0606_ID, '📘 Topical Drills — Part 1: Algebra, Logs & Circle (Ch. 1–7B)', 1, folders, thumbnail_url='/images/maths_0606_cover.jpg')
    f_p2 = ensure_folder(COURSE_0606_ID, '📐 Topical Drills — Part 2: Trig, Series, Vectors & Calculus (Ch. 8–16)', 2, folders, thumbnail_url='/images/maths_0606_cover.jpg')
    f_nc = ensure_folder(COURSE_0606_ID, '🚫 Paper 1: Non-Calculator Specialist Drills (2025–2027)', 3, folders, thumbnail_url='/images/maths_0606_cover.jpg')
    f_pp = ensure_folder(COURSE_0606_ID, '📜 Past Papers & Full Mock Exams (2025–2027)', 4, folders, reuse_id=existing_test_folder, thumbnail_url='/images/maths_0606_cover.jpg')

    # Tag existing 0606/12/Summer2025 with non-calculator policy
    t606 = sb_get(f'tests?course_id=eq.{COURSE_0606_ID}&select=id,title,content_json')
    for t in t606:
        if '0606/12/Summer2025' in (t.get('title') or ''):
            cj = t.get('content_json') or {}
            bi = cj.get('basicInfo') or {}
            bi['calculatorPolicy'] = 'non-calculator'
            cj['basicInfo'] = bi
            sb_patch(f'tests?id=eq.{t["id"]}', {'content_json': cj})
            print("  [OK] Tagged 0606/12/Summer2025 as Paper 1 Non-Calculator.")

    ids['m0606'] = {
        'course_id': COURSE_0606_ID,
        'modules': {'m1': m1_id, 'm2': m2_id, 'm3': m3_id, 'm4': m4_id, 'm5': m5_id},
        'folders': {'drills_p1': f_p1, 'drills_p2': f_p2, 'non_calc': f_nc, 'past_papers': f_pp},
        'lectures': {code: lid for code, (lid, _, _) in lec_map.items()},
    }


def main():
    ids = load_ids()
    setup_0580(ids)
    setup_0606(ids)
    save_ids(ids)
    print(f"\n[DONE] Saved updated IGCSE Maths IDs to scripts/igcse_maths_ids.json!", flush=True)


if __name__ == '__main__':
    main()
