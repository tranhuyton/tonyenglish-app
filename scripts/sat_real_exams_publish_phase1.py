# -*- coding: utf-8 -*-
"""
Master Phase-1 Publisher & Cross-Auditor for Digital SAT Real Past Exams (2024-2025):
Publishes all 5 text-verified Bluebook Real Exams into:
  🏛️ Real Past Exams (2024–2025)
    ├── 📖 Real Exams — Reading & Writing (2025)
    │     1. May 2025 Reading & Writing (Full Adaptive • 81 Qs)
    │     2. June 2025 Ver 1 Reading & Writing (54 Qs)
    └── 📐 Real Exams — Math (2024–2025)
          1. SAT October Math (43 Qs • Official Key)
          2. May 2025 Math (Full Adaptive • 66 Qs)
          3. June 2025 Ver 1 Math (Real M1 + M2)
Runs each module's independent verification suite (`verify_all_math()` / `verify_all()`),
checks Node KaTeX (`throwOnError: true`), checks zero watermark strings (`@DSATuz`, `@D7SAT`),
and upserts idempotently into live Supabase.
"""

import importlib
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.sat_real_exams_pipeline import upsert_real_sat_test

PHASE1_MODULES = [
    'scripts.sat_real_oct2025_math',
    'scripts.sat_real_may2025_rw',
    'scripts.sat_real_may2025_math',
    'scripts.sat_real_june2025_v1_rw',
    'scripts.sat_real_june2025_v1_math',
]


def check_no_watermarks(cj, code):
    raw = str(cj)
    for bad in ('@DSATuz', '@D7SAT', 'satuzhunters', 'Minh Nghĩa', 't.me/D7SAT', '______blank'):
        if bad.lower() in raw.lower():
            raise ValueError(f'{code}: leaked watermark/artifact token "{bad}"!')


def main():
    print("=== PUBLISHING PHASE 1 REAL SAT EXAMS (5 BLUEBOOK TESTS) ===", flush=True)
    total_q = 0
    for mod_name in PHASE1_MODULES:
        mod = importlib.import_module(mod_name)
        print(f"\n--- Verifying {mod_name} ({mod.TEST_CODE}) ---", flush=True)
        if hasattr(mod, 'verify_all_math'):
            mod.verify_all_math()
        elif hasattr(mod, 'verify_all'):
            mod.verify_all()
        check_no_watermarks(mod.TEST_DATA, mod.TEST_CODE)
        tid = upsert_real_sat_test(
            code=mod.TEST_CODE,
            folder_key=mod.FOLDER_KEY,
            title=mod.TEST_TITLE,
            order_index=mod.ORDER_INDEX,
            content_json=mod.TEST_DATA,
        )
        m1_n = len(mod.TEST_DATA['module1']['questions'])
        m2h_n = len(mod.TEST_DATA['module2_hard']['questions'])
        m2l_n = len(mod.TEST_DATA['module2_lower']['questions'])
        # Count unique questions (if routingThreshold==0, m2_hard==m2_lower)
        uniq = m1_n + m2h_n + (0 if mod.TEST_DATA['basicInfo'].get('routingThreshold', 1) == 0 else m2l_n)
        total_q += uniq
        print(f"  [VERIFIED & LIVE] {mod.TEST_TITLE} -> {tid} ({uniq} unique real Qs)", flush=True)
    print(f"\n[ALL PHASE 1 REAL EXAMS LIVE!] 5 Bluebook Tests, {total_q} unique verified real SAT questions!", flush=True)


if __name__ == '__main__':
    main()
