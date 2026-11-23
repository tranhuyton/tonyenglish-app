# -*- coding: utf-8 -*-
"""
Designs and exports (as an idempotent PostgreSQL migration SQL file OR direct REST
publish when service/admin token is provided) complete Task Boards
(`board_templates`, `board_columns`, `board_cards`, `board_card_items`) for
Digital SAT 1500+ and ALL 9 other courses currently missing a Task Board (10 total),
bringing TonyEnglish to 16/16 course Task Board coverage, PLUS an idempotent
backfill assigning every active course board to all currently enrolled students.

Never modifies the 6 courses that already have populated Task Boards.

Usage:
  python scripts/generate_missing_course_boards.py --sql supabase_create_all_missing_boards.sql
"""

import json
import os
import re
import sys
import uuid
import urllib.request
import urllib.error

ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
env = dict(
    l.strip().split('=', 1)
    for l in open(ENV_PATH, encoding='utf-8')
    if '=' in l and not l.startswith('#')
)
BASE = env['VITE_SUPABASE_URL'].rstrip('/') + '/rest/v1/'
KEY = env['VITE_SUPABASE_ANON_KEY']
NS = uuid.UUID('871fdd8e-96a4-4e4b-92a2-2cd41021ee82')


def det_uuid(*parts):
    return str(uuid.uuid5(NS, '::'.join(str(p) for p in parts)))


def sql_str(val):
    if val is None:
        return 'NULL'
    return "'" + str(val).replace("'", "''") + "'"


def sb_get_all(path):
    rows = []
    offset = 0
    step = 1000
    while True:
        sep = '&' if '?' in path else '?'
        url = f"{BASE}{path}{sep}limit={step}&offset={offset}"
        req = urllib.request.Request(url, headers={'apikey': KEY, 'Authorization': f'Bearer {KEY}'})
        chunk = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
        rows.extend(chunk)
        if len(chunk) < step:
            break
        offset += step
    return rows


def natural_sort_key(text):
    parts = re.split(r'(\d+)', (text or '').strip().lower())
    return [int(p) if p.isdigit() else p for p in parts]


def lec_desc(lec_id, lec_title, course_id, task_id=None):
    return json.dumps(
        {
            'source': 'lecture',
            'lecture_id': lec_id,
            'lecture_title': lec_title,
            'course_id': course_id,
            'task_id': task_id,
        },
        ensure_ascii=False,
    )


def clean_test_title(raw):
    return re.sub(r'^Làm\s+(?:bài\s+tập|Bluebook\s+Drill)\s*:\s*', '', (raw or '').strip(), flags=re.IGNORECASE).strip()


def extract_lecture_items(lec, course_id, tests_by_id, default_manual_tasks=None):
    items = []
    tlist = lec.get('task_list') if isinstance(lec.get('task_list'), list) else []
    manual_tasks = [t for t in tlist if isinstance(t, dict) and (t.get('type') or 'manual') == 'manual' and (t.get('text') or t.get('title'))]
    ex_tasks = [t for t in tlist if isinstance(t, dict) and (t.get('type') in ('exercise', 'test') or t.get('test_id')) and t.get('test_id')]

    if manual_tasks:
        for mt in manual_tasks:
            txt = (mt.get('text') or mt.get('title') or '').strip()
            items.append(('manual', txt, lec_desc(lec['id'], lec['title'], course_id, mt.get('id')), None))
    elif default_manual_tasks:
        for txt in default_manual_tasks:
            items.append(('manual', txt, lec_desc(lec['id'], lec['title'], course_id, None), None))

    seen_tids = set()
    ex_tasks_sorted = sorted(
        ex_tasks,
        key=lambda x: natural_sort_key(tests_by_id.get(str(x['test_id']), {}).get('title') or x.get('text') or ''),
    )
    for ex in ex_tasks_sorted:
        tid = str(ex['test_id'])
        if tid in seen_tids:
            continue
        seen_tids.add(tid)
        db_t = tests_by_id.get(tid)
        title = clean_test_title(db_t['title'] if db_t else (ex.get('text') or 'Bài tập'))
        items.append(('test', title, '', tid))

    return items, seen_tids


def chunk_list(seq, n):
    return [seq[i:i + n] for i in range(0, len(seq), n)]


def build_sat_board(course, mods, lecs, folders, tests):
    cid = course['id']
    tests_by_id = {str(t['id']): t for t in tests}
    cols = []
    used_test_ids = set()

    for m in sorted(mods, key=lambda x: x.get('order_index') or 999):
        m_lecs = sorted([l for l in lecs if l.get('module_id') == m['id']], key=lambda x: x.get('order_index') or 999)
        cards = []
        for l in m_lecs:
            items, tids = extract_lecture_items(l, cid, tests_by_id)
            used_test_ids.update(tids)
            cards.append({'title': l['title'], 'items': items})
        cols.append({'title': m['title'], 'cards': cards})

    f_by_id = {f['id']: f for f in folders}
    rw_vocab_games, math_games, rw_mocks, math_mocks = [], [], [], []
    for t in sorted(tests, key=lambda x: (x.get('order_index') or 999, natural_sort_key(x['title']))):
        if str(t['id']) in used_test_ids:
            continue
        ftitle = (f_by_id.get(t.get('folder_id'), {}).get('title') or '').lower()
        ttitle = (t.get('title') or '').lower()
        if 'vocab' in ftitle or 'vocab' in ttitle:
            rw_vocab_games.append(t)
        elif 'formula' in ftitle or 'desmos' in ftitle or 'game' in ftitle:
            math_games.append(t)
        elif 'math' in ftitle or 'math' in ttitle:
            math_mocks.append(t)
        else:
            rw_mocks.append(t)

    rw_vocab_games.sort(key=lambda x: natural_sort_key(x['title']))
    math_games.sort(key=lambda x: natural_sort_key(x['title']))
    rw_mocks.sort(key=lambda x: natural_sort_key(x['title']))
    math_mocks.sort(key=lambda x: natural_sort_key(x['title']))

    game_cards = []
    if rw_vocab_games:
        game_cards.append({
            'title': '1. Elite SAT Vocabulary Games (Set 1–5: 250 từ)',
            'items': [('test', t['title'], '', str(t['id'])) for t in rw_vocab_games[:5]],
        })
        if len(rw_vocab_games) > 5:
            game_cards.append({
                'title': '2. Elite SAT Vocabulary Games (Set 6–10: 250 từ)',
                'items': [('test', t['title'], '', str(t['id'])) for t in rw_vocab_games[5:]],
            })
    if math_games:
        game_cards.append({
            'title': '3. Math Formula & Desmos 800 Games (100 thẻ)',
            'items': [('test', t['title'], '', str(t['id'])) for t in math_games],
        })
    cols.append({
        'title': '⚡ Speed Games (500 Từ vựng & 100 Công thức) [color:#f3e8ff,#6b21a8]',
        'cards': game_cards,
    })

    mock_cards = []
    if rw_mocks:
        mock_cards.append({
            'title': '1. R&W Adaptive Mock Tests #1–#4 (Đợt 1)',
            'items': [('test', t['title'], '', str(t['id'])) for t in rw_mocks[:4]],
        })
        if len(rw_mocks) > 4:
            mock_cards.append({
                'title': '2. R&W Adaptive Mock Tests #5–#8 (Đợt 2)',
                'items': [('test', t['title'], '', str(t['id'])) for t in rw_mocks[4:]],
            })
    if math_mocks:
        mock_cards.append({
            'title': '3. Math Adaptive Mock Tests #1–#4 (Đợt 1)',
            'items': [('test', t['title'], '', str(t['id'])) for t in math_mocks[:4]],
        })
        if len(math_mocks) > 4:
            mock_cards.append({
                'title': '4. Math Adaptive Mock Tests #5–#8 (Đợt 2)',
                'items': [('test', t['title'], '', str(t['id'])) for t in math_mocks[4:]],
            })
    cols.append({
        'title': '🎯 Full-Length Adaptive Mock Tests (Bluebook) [color:#e0f2fe,#0369a1]',
        'cards': mock_cards,
    })

    return 'Bảng công việc Digital SAT 1500+', cols


def build_module_lecture_board(course, board_title, mods, lecs, tests, default_manual_tasks=None, empty_lec_task=None):
    cid = course['id']
    tests_by_id = {str(t['id']): t for t in tests}
    cols = []
    for m in sorted(mods, key=lambda x: x.get('order_index') or 999):
        m_lecs = sorted([l for l in lecs if l.get('module_id') == m['id']], key=lambda x: x.get('order_index') or 999)
        if not m_lecs:
            continue
        cards = []
        for l in m_lecs:
            fallback = default_manual_tasks
            if fallback is None and empty_lec_task:
                fallback = [empty_lec_task(l)]
            items, _ = extract_lecture_items(l, cid, tests_by_id, default_manual_tasks=fallback)
            cards.append({'title': l['title'], 'items': items})
        cols.append({'title': m['title'], 'cards': cards})
    return board_title, cols


def build_maths_0580_board(course, mods, lecs, tests):
    cid = course['id']
    tests_by_id = {str(t['id']): t for t in tests}
    sorted_lecs = sorted(lecs, key=lambda x: x.get('order_index') or 999)
    part1, part2, rev = [], [], []
    for l in sorted_lecs:
        title_low = (l['title'] or '').lower()
        items, _ = extract_lecture_items(l, cid, tests_by_id)
        card = {'title': l['title'], 'items': items}
        m = re.search(r'topic\s*(\d+)', title_low)
        if m:
            num = int(m.group(1))
            if num <= 5:
                part1.append(card)
            else:
                part2.append(card)
        else:
            rev.append(card)
    cols = [
        {'title': 'Part 1: Number, Algebra & Geometry (Topic 1–5) [color:#dcfce7,#15803d]', 'cards': part1},
        {'title': 'Part 2: Trig, Vectors, Probability & Stats (Topic 6–9) [color:#fef9c3,#713f12]', 'cards': part2},
        {'title': 'Past Papers & Year End Revision [color:#e0f2fe,#0369a1]', 'cards': rev},
    ]
    return 'Bảng công việc IGCSE Maths 0580', cols


def build_maths_0606_board(course, mods, lecs, tests):
    cid = course['id']
    tests_by_id = {str(t['id']): t for t in tests}
    sorted_lecs = sorted(lecs, key=lambda x: x.get('order_index') or 999)
    default_tasks = [
        'Học kỹ lý thuyết & ghi chép công thức trọng tâm',
        'Luyện giải ví dụ mẫu & tự tổng kết dạng bài',
    ]
    buckets = [[], [], [], []]
    for idx, l in enumerate(sorted_lecs):
        items, _ = extract_lecture_items(l, cid, tests_by_id, default_manual_tasks=default_tasks)
        card = {'title': l['title'], 'items': items}
        if idx < 5:
            buckets[0].append(card)
        elif idx < 9:
            buckets[1].append(card)
        elif idx < 13:
            buckets[2].append(card)
        else:
            buckets[3].append(card)

    if tests:
        buckets[3].append({
            'title': 'Past Papers (Đề thi thật Cambridge 0606)',
            'items': [('test', t['title'], '', str(t['id'])) for t in sorted(tests, key=lambda x: natural_sort_key(x['title']))],
        })

    cols = [
        {'title': 'Part 1: Functions, Quadratics & Polynomials (Ch. 1–5) [color:#e0e7ff,#3730a3]', 'cards': buckets[0]},
        {'title': 'Part 2: Logs, Coordinate & Circular Measure (Ch. 6–9) [color:#ccfbf1,#0f766e]', 'cards': buckets[1]},
        {'title': 'Part 3: Combinatorics, Series & Vectors (Ch. 10–13) [color:#fef3c7,#b45309]', 'cards': buckets[2]},
        {'title': 'Part 4: Calculus, Kinematics & Past Papers (Ch. 14–16) [color:#ffe4e6,#be123c]', 'cards': buckets[3]},
    ]
    return 'Bảng công việc IGCSE Maths 0606', cols


def build_esl_0510_board(course, mods, lecs, folders, tests):
    cid = course['id']
    tests_by_id = {str(t['id']): t for t in tests}
    cols = []
    linked_tids = set()

    for m in sorted(mods, key=lambda x: x.get('order_index') or 999):
        m_lecs = sorted([l for l in lecs if l.get('module_id') == m['id']], key=lambda x: x.get('order_index') or 999)
        cards = []
        for l in m_lecs:
            items, tids = extract_lecture_items(
                l, cid, tests_by_id,
                default_manual_tasks=['Học kỹ bài giảng & ghi chú chiến thuật làm bài'],
            )
            linked_tids.update(tids)
            cards.append({'title': l['title'], 'items': items})
        cols.append({'title': m['title'], 'cards': cards})

    year_colors = {
        '2024': '[color:#dcfce7,#15803d]',
        '2025': '[color:#fef3c7,#b45309]',
        '2026': '[color:#f3e8ff,#7e22ce]',
    }
    for year in ('2024', '2025', '2026'):
        year_folder = next((f for f in folders if (f.get('title') or '').strip() == year), None)
        if not year_folder:
            continue
        session_folders = sorted(
            [f for f in folders if f.get('parent_id') == year_folder['id']],
            key=lambda x: (x.get('display_order') or 999, natural_sort_key(x['title'])),
        )
        cards = []
        for sf in session_folders:
            sf_tests = sorted(
                [t for t in tests if t.get('folder_id') == sf['id'] and str(t['id']) not in linked_tids],
                key=lambda x: natural_sort_key(x['title']),
            )
            if sf_tests:
                cards.append({
                    'title': sf['title'],
                    'items': [('test', t['title'], '', str(t['id'])) for t in sf_tests],
                })
        if cards:
            cols.append({'title': f'Past Papers {year} {year_colors[year]}', 'cards': cards})

    return 'Bảng công việc IGCSE ESL 0510', cols


def build_grammar_vocab_board(course, mods, lecs, folders, tests):
    cid = course['id']
    tests_by_id = {str(t['id']): t for t in tests}
    cols = []

    for m in sorted(mods, key=lambda x: x.get('order_index') or 999):
        m_lecs = sorted([l for l in lecs if l.get('module_id') == m['id']], key=lambda x: x.get('order_index') or 999)
        cards = []
        for l in m_lecs:
            items, _ = extract_lecture_items(
                l, cid, tests_by_id,
                default_manual_tasks=['Học lý thuyết bài giảng & ghi chép cấu trúc ví dụ'],
            )
            cards.append({'title': l['title'], 'items': items})
        cols.append({'title': m['title'], 'cards': cards})

    top_folders = sorted([f for f in folders if not f.get('parent_id')], key=lambda x: x.get('display_order') or 999)
    folder_styles = {
        'grammar': ('Bài tập Ngữ pháp (Grammar) [color:#dcfce7,#15803d]', None),
        'vocabulary organiser': ('Vocabulary Organiser [color:#ffedd5,#c2410c]', None),
        '4000 english words': ('4000 English Words [color:#e0e7ff,#4338ca]', None),
        'expand vocabulary through reading': ('Expand Vocabulary Through Reading [color:#fce7f3,#be185d]', 8),
    }

    for tf in top_folders:
        key = (tf['title'] or '').strip().lower()
        col_title, chunk_sz = folder_styles.get(key, (f"{tf['title']} [color:#e0f2fe,#0369a1]", 10))
        sub_folders = sorted(
            [f for f in folders if f.get('parent_id') == tf['id']],
            key=lambda x: (x.get('display_order') or 999, natural_sort_key(x['title'])),
        )
        cards = []
        if sub_folders:
            for sf in sub_folders:
                sf_tests = sorted(
                    [t for t in tests if t.get('folder_id') == sf['id']],
                    key=lambda x: (x.get('order_index') or 999, natural_sort_key(x['title'])),
                )
                if sf_tests:
                    cards.append({
                        'title': sf['title'],
                        'items': [('test', t['title'], '', str(t['id'])) for t in sf_tests],
                    })
        else:
            direct_tests = sorted(
                [t for t in tests if t.get('folder_id') == tf['id']],
                key=lambda x: (x.get('order_index') or 999, natural_sort_key(x['title'])),
            )
            if direct_tests:
                sz = chunk_sz or 10
                for g_idx, grp in enumerate(chunk_list(direct_tests, sz)):
                    start_n = g_idx * sz + 1
                    end_n = start_n + len(grp) - 1
                    cards.append({
                        'title': f'{g_idx + 1}. Reading Pack {start_n}–{end_n}',
                        'items': [('test', t['title'], '', str(t['id'])) for t in grp],
                    })
        if cards:
            cols.append({'title': col_title, 'cards': cards})

    return 'Bảng công việc Grammar and Vocabulary', cols


def build_giao_tiep_board(course, mods, lecs, folders, tests):
    cid = course['id']
    sorted_mods = sorted(mods, key=lambda x: x.get('order_index') or 999)

    def strip_color(t):
        return re.sub(r'\s*\[color:[^\]]+\]\s*$', '', t or '').strip()

    def build_stage_cards(mod_slice):
        cards = []
        for idx, m in enumerate(mod_slice):
            m_lecs = sorted([l for l in lecs if l.get('module_id') == m['id']], key=lambda x: x.get('order_index') or 999)
            items = [
                ('manual', f"Luyện phản xạ: {l['title']}", lec_desc(l['id'], l['title'], cid, None), None)
                for l in m_lecs
            ]
            cards.append({'title': f"{idx + 1}. {strip_color(m['title'])}", 'items': items})
        return cards

    cols = [
        {'title': 'Giai đoạn 1: Mẫu câu 01–30 & Ôn tập [color:#ccfbf1,#0f766e]', 'cards': build_stage_cards(sorted_mods[0:4])},
        {'title': 'Giai đoạn 2: Mẫu câu 31–60 & Ôn tập [color:#e0f2fe,#0369a1]', 'cards': build_stage_cards(sorted_mods[4:8])},
        {'title': 'Giai đoạn 3: Mẫu câu 61–90 & Ôn tập [color:#f3e8ff,#7e22ce]', 'cards': build_stage_cards(sorted_mods[8:12])},
    ]

    if len(sorted_mods) >= 13:
        m13 = sorted_mods[12]
        m13_lecs = sorted([l for l in lecs if l.get('module_id') == m13['id']], key=lambda x: x.get('order_index') or 999)
        cols.append({
            'title': m13['title'],
            'cards': [
                {
                    'title': f"{idx + 1}. {l['title']}",
                    'items': [('manual', 'Học bài giảng & luyện phản xạ tình huống', lec_desc(l['id'], l['title'], cid, None), None)],
                }
                for idx, l in enumerate(m13_lecs)
            ],
        })

    top_folders = sorted([f for f in folders if not f.get('parent_id')], key=lambda x: x.get('display_order') or 999)
    listen_colors = ['[color:#dcfce7,#15803d]', '[color:#ffedd5,#c2410c]', '[color:#ffe4e6,#be123c]']
    for f_idx, tf in enumerate(top_folders):
        f_tests = sorted(
            [t for t in tests if t.get('folder_id') == tf['id']],
            key=lambda x: (x.get('order_index') or 999, natural_sort_key(x['title'])),
        )
        cards = []
        for g_idx, grp in enumerate(chunk_list(f_tests, 12)):
            s_n = g_idx * 12 + 1
            e_n = s_n + len(grp) - 1
            cards.append({
                'title': f'{g_idx + 1}. Listening Pack {s_n}–{e_n}',
                'items': [('test', t['title'], '', str(t['id'])) for t in grp],
            })
        color = listen_colors[f_idx % len(listen_colors)]
        cols.append({'title': f"{tf['title']} {color}", 'cards': cards})

    return 'Bảng công việc Giao tiếp và phản xạ', cols


def build_van_phong_board(course, mods, lecs):
    cid = course['id']
    sorted_mods = sorted(mods, key=lambda x: x.get('order_index') or 999)

    def strip_color(t):
        return re.sub(r'\s*\[color:[^\]]+\]\s*$', '', t or '').strip()

    def build_topic_cards(mod_slice):
        cards = []
        for m in mod_slice:
            m_lecs = sorted([l for l in lecs if l.get('module_id') == m['id']], key=lambda x: x.get('order_index') or 999)
            items = [
                ('manual', f"Hoàn thành bài giảng: {l['title']}", lec_desc(l['id'], l['title'], cid, None), None)
                for l in m_lecs
            ]
            cards.append({'title': strip_color(m['title']), 'items': items})
        return cards

    cols = [
        {'title': 'Phần 1: Văn phòng, Thương mại & Công tác (1–4) [color:#ccfbf1,#0f766e]', 'cards': build_topic_cards(sorted_mods[0:4])},
        {'title': 'Phần 2: Tiếp khách, Mua sắm & Ẩm thực (5–7) [color:#fce7f3,#be185d]', 'cards': build_topic_cards(sorted_mods[4:7])},
        {'title': 'Phần 3: Nhân sự, Tài chính & Phát triển SP (8–10) [color:#ffedd5,#c2410c]', 'cards': build_topic_cards(sorted_mods[7:10])},
        {'title': 'Phần 4: Sản xuất, Tài sản & Y tế (11–13) [color:#e0f2fe,#0369a1]', 'cards': build_topic_cards(sorted_mods[10:13])},
    ]
    return 'Bảng công việc Tiếng Anh văn phòng', cols


def generate_all_specs():
    courses = sb_get_all('courses?select=id,title,type,order_index&order=order_index.asc,id.asc')
    boards = sb_get_all('board_templates?select=*&order=id.asc')
    cols = sb_get_all('board_columns?select=*&order=order_index.asc,id.asc')
    mods = sb_get_all('lecture_modules?select=*&order=order_index.asc,id.asc')
    lecs = sb_get_all('lectures?select=id,course_id,module_id,title,order_index,task_list&order=order_index.asc,id.asc')
    folders = sb_get_all('folders?select=*&order=display_order.asc,id.asc')
    tests = sb_get_all('tests?select=id,course_id,folder_id,title,test_type,order_index&order=order_index.asc,id.asc')

    specs = []
    for c in courses:
        cid = c['id']
        title_low = (c['title'] or '').lower()
        c_mods = [m for m in mods if m.get('course_id') == cid]
        c_lecs = [l for l in lecs if l.get('course_id') == cid]
        c_folders = [f for f in folders if f.get('course_id') == cid]
        c_tests = [t for t in tests if t.get('course_id') == cid]

        c_boards = [b for b in boards if b.get('course_id') == cid]
        has_populated = any(any(col.get('board_template_id') == b['id'] for col in cols) for b in c_boards)
        if has_populated:
            continue

        existing_stub_id = c_boards[0]['id'] if c_boards else det_uuid('board_tpl', cid)

        if 'sat' in title_low or c.get('type') == 'SAT':
            b_title, spec_cols = build_sat_board(c, c_mods, c_lecs, c_folders, c_tests)
        elif 'physics-0625' in title_low:
            b_title, spec_cols = build_module_lecture_board(
                c, 'Bảng công việc IGCSE Physics 0625', c_mods, c_lecs, c_tests,
                empty_lec_task=lambda l: f"Nghe trọn {l['title']} & ghi chú kiến thức trọng tâm",
            )
        elif 'chemistry-0620' in title_low:
            b_title, spec_cols = build_module_lecture_board(
                c, 'Bảng công việc IGCSE Chemistry 0620', c_mods, c_lecs, c_tests,
                empty_lec_task=lambda l: f"Nghe trọn {l['title']} & ghi chú kiến thức trọng tâm",
            )
        elif 'maths-0580' in title_low:
            b_title, spec_cols = build_maths_0580_board(c, c_mods, c_lecs, c_tests)
        elif 'maths-0606' in title_low:
            b_title, spec_cols = build_maths_0606_board(c, c_mods, c_lecs, c_tests)
        elif 'esl-0510' in title_low:
            b_title, spec_cols = build_esl_0510_board(c, c_mods, c_lecs, c_folders, c_tests)
        elif 'grammar and vocabulary' in title_low:
            b_title, spec_cols = build_grammar_vocab_board(c, c_mods, c_lecs, c_folders, c_tests)
        elif 'phát âm' in title_low:
            b_title, spec_cols = build_module_lecture_board(
                c, 'Bảng công việc Phát Âm', c_mods, c_lecs, c_tests,
                default_manual_tasks=[
                    'Xem bài giảng & ghi nhớ khẩu hình / quy tắc phát âm',
                    'Luyện đọc to theo audio mẫu & tự ghi âm kiểm tra',
                ],
            )
        elif 'giao tiếp' in title_low:
            b_title, spec_cols = build_giao_tiep_board(c, c_mods, c_lecs, c_folders, c_tests)
        elif 'văn phòng' in title_low:
            b_title, spec_cols = build_van_phong_board(c, c_mods, c_lecs)
        else:
            b_title, spec_cols = build_module_lecture_board(
                c, f"Bảng công việc {c['title']}", c_mods, c_lecs, c_tests,
                default_manual_tasks=['Học bài giảng & ghi chú kiến thức trọng tâm'],
            )

        specs.append({
            'course': c,
            'tpl_id': existing_stub_id,
            'title': b_title,
            'columns': spec_cols,
        })
    return specs


def export_sql(specs, out_path):
    lines = [
        '-- ============================================================================',
        '-- KHỞI TẠO TOÀN BỘ 10 BẢNG CÔNG VIỆC CÒN THIẾU (DIGITAL SAT 1500+ & 9 KHÓA)',
        '-- + GÁN TỰ ĐỘNG BẢNG CÔNG VIỆC CHO TOÀN BỘ HỌC VIÊN ĐÃ ENROLL (16/16 KHÓA)',
        '-- Chạy 1 lần trên Supabase SQL Editor (Idempotent - giữ nguyên tiến độ cũ)',
        '-- ============================================================================',
        'BEGIN;',
        '',
    ]

    total_cols = 0
    total_cards = 0
    total_items = 0

    for sp in specs:
        cid = sp['course']['id']
        cname = sp['course']['title']
        tpl_id = sp['tpl_id']
        b_title = sp['title']
        c_cols = len(sp['columns'])
        c_cards = sum(len([cd for cd in col['cards'] if cd['items']]) for col in sp['columns'])
        c_items = sum(len(cd['items']) for col in sp['columns'] for cd in col['cards'])
        total_cols += c_cols
        total_cards += c_cards
        total_items += c_items

        print(f"  [SPEC] {cname:<34} -> {b_title:<42} | cols={c_cols:<2} cards={c_cards:<3} items={c_items}")

        lines.append(f"-- ----------------------------------------------------------------------------")
        lines.append(f"-- COURSE: {cname} ({cid}) | {c_cols} cols, {c_cards} cards, {c_items} items")
        lines.append(f"-- ----------------------------------------------------------------------------")
        lines.append(
            f"INSERT INTO board_templates (id, course_id, title, is_active) "
            f"VALUES ({sql_str(tpl_id)}, {sql_str(cid)}, {sql_str(b_title)}, true) "
            f"ON CONFLICT (id) DO UPDATE SET title = EXCLUDED.title, is_active = true;"
        )

        # Skip populating columns/cards/items if this board template already has columns
        lines.append("DO $$")
        lines.append("BEGIN")
        lines.append(f"  IF NOT EXISTS (SELECT 1 FROM board_columns WHERE board_template_id = {sql_str(tpl_id)}) THEN")

        col_values = []
        card_values = []
        item_values = []

        for col_idx, col in enumerate(sp['columns'], start=1):
            col_id = det_uuid('col', tpl_id, col_idx)
            col_values.append(
                f"({sql_str(col_id)}, {sql_str(cid)}, {sql_str(tpl_id)}, {sql_str(col['title'])}, {col_idx})"
            )
            card_order = 0
            for card in col['cards']:
                if not card['items']:
                    continue
                card_order += 1
                card_id = det_uuid('card', col_id, card_order)
                card_values.append(
                    f"({sql_str(card_id)}, {sql_str(col_id)}, {sql_str(card['title'])}, {card_order})"
                )
                for item_idx, (t_type, title, desc, test_id) in enumerate(card['items'], start=1):
                    item_id = det_uuid('item', card_id, item_idx)
                    item_values.append(
                        f"({sql_str(item_id)}, {sql_str(card_id)}, {sql_str(t_type)}, "
                        f"{sql_str(title)}, {sql_str(desc or '')}, {sql_str(test_id)}, {item_idx})"
                    )

        if col_values:
            lines.append("    INSERT INTO board_columns (id, course_id, board_template_id, title, order_index) VALUES")
            lines.append("      " + ",\n      ".join(col_values))
            lines.append("    ON CONFLICT (id) DO NOTHING;")
        if card_values:
            lines.append("    INSERT INTO board_cards (id, column_id, title, order_index) VALUES")
            lines.append("      " + ",\n      ".join(card_values))
            lines.append("    ON CONFLICT (id) DO NOTHING;")
        if item_values:
            for chunk in chunk_list(item_values, 150):
                lines.append("    INSERT INTO board_card_items (id, card_id, task_type, title, description, test_id, order_index) VALUES")
                lines.append("      " + ",\n      ".join(chunk))
                lines.append("    ON CONFLICT (id) DO NOTHING;")

        lines.append("  END IF;")
        lines.append("END $$;")
        lines.append("")

    # Idempotent backfill: assign active course board to EVERY enrolled student across ALL 16 courses!
    lines.extend([
        '-- ============================================================================',
        '-- TỰ ĐỘNG GÁN BẢNG CÔNG VIỆC CHO TOÀN BỘ HỌC VIÊN ĐÃ ENROLL (CẢ 16 KHÓA)',
        '-- Chỉ gán cho các cặp (user_id, board_template_id) chưa có trong assignments.',
        '-- Không ghi đè hay làm mất tiến độ đã tick của học viên cũ.',
        '-- ============================================================================',
        'WITH primary_boards AS (',
        '  SELECT DISTINCT ON (course_id) id AS board_template_id, course_id, title AS board_template_title',
        '  FROM board_templates',
        '  WHERE course_id IS NOT NULL',
        '  ORDER BY course_id, is_active DESC NULLS LAST, created_at ASC',
        ')',
        'INSERT INTO assignments (',
        '  user_id, title, description, task_type, test_id,',
        '  category, card_title, card_order, order_index, due_date,',
        '  board_template_id, board_template_title',
        ')',
        'SELECT',
        '  e.user_id,',
        '  i.title,',
        "  COALESCE(i.description, ''),",
        '  i.task_type,',
        '  i.test_id,',
        '  col.title,',
        '  card.title,',
        '  COALESCE(card.order_index, 0),',
        '  COALESCE(i.order_index, 0),',
        '  NULL,',
        '  pb.board_template_id,',
        '  pb.board_template_title',
        'FROM enrollments e',
        'JOIN primary_boards pb ON pb.course_id = e.course_id',
        'JOIN board_columns col ON col.board_template_id = pb.board_template_id',
        'JOIN board_cards card ON card.column_id = col.id',
        'JOIN board_card_items i ON i.card_id = card.id',
        'WHERE NOT EXISTS (',
        '  SELECT 1 FROM assignments a',
        '  WHERE a.user_id = e.user_id',
        '    AND a.category IS NOT NULL',
        '    AND (a.board_template_id = pb.board_template_id OR a.board_template_title = pb.board_template_title)',
        ');',
        '',
        'COMMIT;',
        '',
    ])

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"\n[DONE] Generated {out_path}: {len(specs)} boards | {total_cols} cols | {total_cards} cards | {total_items} items")


if __name__ == '__main__':
    specs = generate_all_specs()
    out_sql = 'supabase_create_all_missing_boards.sql'
    if '--sql' in sys.argv:
        idx = sys.argv.index('--sql')
        if idx + 1 < len(sys.argv):
            out_sql = sys.argv[idx + 1]
    export_sql(specs, out_sql)
