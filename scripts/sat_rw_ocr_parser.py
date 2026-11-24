# -*- coding: utf-8 -*-
"""
Universal Bluebook R&W OCR parser for `scripts/ocr_data/<tag>_raw.json`.
Parses left (passage) and right (prompt + A/B/C/D options) Tesseract OCR text into clean
Bluebook SatQuestion fields, applying per-question patches (underlines, HTML tables, inline SVGs,
and targeted OCR typo replacements) so authoring scripts NEVER have to hardcode or recite
54 verbatim passages!
"""

import json
import os
import re


def clean_ocr_passage(raw_left: str) -> str:
    lines = []
    for ln in (raw_left or '').splitlines():
        s = ln.strip()
        if not s:
            lines.append('')
            continue
        # Strip top UI chrome / stray divider artifacts
        if re.match(r'^[\[\]\(\)=_\-—–\|\.\s0-9a-z]{1,4}$', s) and len(s) <= 3:
            continue
        if re.search(r'(Section\s+\d|Directions|Mark for Review|@D7SAT|@DSATuz|t\.me/)', s, re.I):
            continue
        lines.append(s)

    # Rejoin paragraphs cleanly
    paras = []
    buf = []
    for s in lines:
        if not s:
            if buf:
                paras.append(' '.join(buf))
                buf = []
        else:
            # Handle bullet points cleanly
            if re.match(r'^[•\-\*o○]\s+', s) and buf:
                paras.append(' '.join(buf))
                buf = [s]
            else:
                buf.append(s)
    if buf:
        paras.append(' '.join(buf))

    cleaned_paras = []
    for p in paras:
        p = re.sub(r'_{3,}', '_______', p)
        p = re.sub(r'\s+([.,;:?!])', r'\1', p)
        p = p.replace('’ ', '’').replace('‘ ', '‘').replace('“ ', '“').replace(' ”', '”')
        if p.strip():
            cleaned_paras.append(f'<p>{p.strip()}</p>')
    return '\n'.join(cleaned_paras)


def parse_ocr_right(raw_right: str):
    """Extracts (question_prompt, [optA, optB, optC, optD]) from cleaned right-pane OCR."""
    lines = [ln.strip() for ln in (raw_right or '').splitlines() if ln.strip()]
    # Drop everything up to and including 'Mark for Review' / top chrome
    start_idx = 0
    for i, ln in enumerate(lines):
        if re.search(r'Mark\s+for\s+Review|ABC', ln, re.I):
            start_idx = i + 1
    lines = lines[start_idx:]

    # Find end of question prompt (first line ending with '?' or ':')
    q_end = -1
    for i, ln in enumerate(lines):
        if ln.endswith('?') or ln.endswith('?\"') or ln.endswith("?'"):
            q_end = i
            break
    if q_end == -1:
        # Fallback: first 2 lines
        q_end = min(1, len(lines) - 1)

    q_text = ' '.join(lines[:q_end + 1]).strip()
    q_text = re.sub(r'^[‘\'\"`\-\[\]]+\s*', '', q_text)
    opt_lines = lines[q_end + 1:]

    # Group option lines using circle-badge markers like (A), (@, (®, (©, (B), (C), (D), ©, ®
    badge_re = re.compile(r'^[\(\[\{\s]*([A-D@®©O0Q68]|a|b|c|d)[\)\]\}\s]*[\)\]\}]?\s+(.*)$')
    # More specifically, Bluebook puts a circled letter at the start of each option block
    groups = []
    for ln in opt_lines:
        # Strip trailing stray ']' or ')' from box edge
        ln_clean = re.sub(r'\s*[\)\]\}\|]+$', '', ln).strip()
        if not ln_clean:
            continue
        is_new = bool(re.match(r'^[\(\[\{]\s*[A-D@®©0O8a-d]{1,2}\s*[\)\]\}]?\s+', ln_clean)) or bool(re.match(r'^[©®@]\s+', ln_clean))
        if is_new:
            txt = re.sub(r'^[\(\[\{]?\s*[A-D@®©0O8a-d]{1,2}\s*[\)\]\}]?\s+', '', ln_clean).strip()
            txt = re.sub(r'^[\(\[\{]\s*', '', txt).strip()
            groups.append(txt)
        else:
            # Sometimes option starts with bare '(' because circle A vanished
            if re.match(r'^[\(\[]\s+[A-Za-z0-9“"\']', ln_clean):
                txt = re.sub(r'^[\(\[]\s+', '', ln_clean).strip()
                groups.append(txt)
            elif groups:
                groups[-1] = (groups[-1] + ' ' + ln_clean).strip()
            else:
                groups.append(ln_clean)

    # Clean trailing box artifacts inside each option
    final_opts = []
    for g in groups:
        g = re.sub(r'\s*[\)\]\}\|]+$', '', g).strip()
        g = re.sub(r'\s+([.,;:?!])', r'\1', g)
        if g:
            final_opts.append(g)

    return q_text, final_opts


def build_rw_questions_from_ocr(raw_json_path, mod_prefix, page_start, page_end, meta_map, patches=None):
    """
    meta_map: dict[q_num (1..27)] -> {
        'domain': ..., 'skill': ..., 'difficulty': ...,
        'answer': 'A'|'B'|'C'|'D',
        'explanation': { 'summaryVi': ..., 'keyTakeaway': ..., 'optionAnalysis': { 'A':..., 'B':..., 'C':..., 'D':... } }
    }
    patches: optional dict[q_num] -> {
        'replace': [(old, new), ...],          # applied to stimulus + question + options
        'stimulusHtml': '...',                 # full override (e.g. table/chart/underlined)
        'prependStimulusHtml': '...',          # prepend clean HTML table or SVG above passage
        'questionHtml': '...',                 # override prompt
        'options': ['optA', 'optB', 'optC', 'optD'],  # override 4 options if OCR missed/merged
    }
    """
    patches = patches or {}
    rows = json.load(open(raw_json_path, encoding='utf-8'))
    by_page = {r['page']: r for r in rows}

    questions = []
    for idx, pno in enumerate(range(page_start, page_end + 1), start=1):
        row = by_page[pno]
        stim = clean_ocr_passage(row['left'])
        if row.get('boxed'):
            q_txt = ' '.join((row.get('prompt') or '').splitlines()).strip()
            q_txt = re.sub(r'^.*?Mark\s+for\s+Review\s*(?:ABC)?\s*', '', q_txt, flags=re.I).strip()
            q_txt = re.sub(r'^[‘\'\"`\-\[\]0-9]+\s*', '', q_txt).strip()
            opts = [re.sub(r'\s+', ' ', (o or '')).strip() for o in (row.get('options') or [])]
            opts = [re.sub(r'\s+([.,;:?!])', r'\1', o) for o in opts]
        else:
            q_txt, opts = parse_ocr_right(row.get('right', ''))
        pt = patches.get(idx, {})

        if 'stimulusHtml' in pt:
            stim = pt['stimulusHtml']
        elif 'prependStimulusHtml' in pt:
            stim = pt['prependStimulusHtml'] + '\n' + stim

        if 'questionHtml' in pt:
            q_txt = pt['questionHtml']
        if 'options' in pt:
            opts = list(pt['options'])

        for old, new in pt.get('replace', []):
            stim = stim.replace(old, new)
            q_txt = q_txt.replace(old, new)
            opts = [o.replace(old, new) for o in opts]

        if len(opts) != 4:
            raise ValueError(f"{mod_prefix} Q{idx} (p.{pno}): expected 4 options, got {len(opts)} -> {opts}")

        m = meta_map[idx]
        questions.append({
            'id': f'{mod_prefix}_q{idx:02d}',
            'number': idx,
            'domain': m['domain'],
            'skill': m['skill'],
            'difficulty': m.get('difficulty', 'Medium'),
            'questionFormat': 'mcq',
            'stimulusHtml': stim,
            'questionHtml': f'<p>{q_txt}</p>' if not q_txt.startswith('<') else q_txt,
            'options': [
                {'label': lbl, 'text': opts[i]}
                for i, lbl in enumerate(['A', 'B', 'C', 'D'])
            ],
            'correctAnswer': m['answer'],
            'explanation': m['explanation'],
        })
    return questions


if __name__ == '__main__':
    import sys
    fp = sys.argv[1]
    rows = json.load(open(fp, encoding='utf-8'))
    bad = []
    for r in rows:
        q, opts = parse_ocr_right(r['right'])
        if len(opts) != 4 or not q:
            bad.append((r['page'], len(opts), q[:50], opts))
    print(f"Parsed {len(rows)} pages from {fp}: {len(rows)-len(bad)}/54 cleanly auto-parsed into 4 options! Needs patch ({len(bad)}): {[b[0] for b in bad]}")
    for b in bad[:10]:
        print("  ", b)
