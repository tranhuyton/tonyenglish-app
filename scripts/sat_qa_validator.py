import sys
import re

VALID_LABELS = {'A', 'B', 'C', 'D'}
VALID_RW_DOMAINS = {
    'Standard English Conventions',
    'Expression of Ideas',
    'Craft and Structure',
    'Information and Ideas',
}
VALID_MATH_DOMAINS = {
    'Algebra',
    'Advanced Math',
    'Problem-Solving and Data Analysis',
    'Geometry and Trigonometry',
}
VALID_DOMAINS = VALID_RW_DOMAINS | VALID_MATH_DOMAINS

SPR_NUM_RE = re.compile(r'^-?(\d+(\.\d+)?|\.\d+)(/(\d+(\.\d+)?|\.\d+))?$')

def validate_question(q, idx, context_name=''):
    errors = []
    prefix = f"[{context_name} Q{idx+1}]"
    if not q.get('id'):
        errors.append(f"{prefix} Missing id")
    if q.get('number') != idx + 1:
        errors.append(f"{prefix} Number mismatch: expected {idx+1}, got {q.get('number')}")
    if q.get('domain') not in VALID_DOMAINS:
        errors.append(f"{prefix} Invalid domain: {q.get('domain')}")
    if not q.get('skill') or len(q['skill']) < 3:
        errors.append(f"{prefix} Missing skill")
    if not q.get('stimulusHtml') or len(q['stimulusHtml'].strip()) < 15:
        errors.append(f"{prefix} Stimulus too short or missing")
    if not q.get('questionHtml') or len(q['questionHtml'].strip()) < 10:
        errors.append(f"{prefix} Question stem too short or missing")

    qfmt = q.get('questionFormat', 'mcq')
    exp = q.get('explanation') or {}
    if not exp.get('summaryVi') or len(exp['summaryVi'].strip()) < 20:
        errors.append(f"{prefix} Missing or too short summaryVi")

    if qfmt == 'spr':
        acc = q.get('acceptedAnswers') or []
        ans = str(q.get('correctAnswer') or '').strip()
        if not ans:
            errors.append(f"{prefix} SPR missing correctAnswer")
        if not acc:
            errors.append(f"{prefix} SPR missing acceptedAnswers")
        for a in acc:
            s = str(a).strip()
            if not SPR_NUM_RE.match(s):
                errors.append(f"{prefix} Invalid SPR acceptedAnswer format: {a}")
            elif '/' in s:
                den = float(s.split('/')[1])
                if den == 0:
                    errors.append(f"{prefix} Division by zero in SPR acceptedAnswer: {a}")
        return errors

    opts = q.get('options') or []
    if len(opts) != 4:
        errors.append(f"{prefix} Must have exactly 4 options, got {len(opts)}")
    else:
        labels = [o.get('label') for o in opts]
        if labels != ['A', 'B', 'C', 'D']:
            errors.append(f"{prefix} Option labels must be A,B,C,D, got {labels}")
        seen_texts = set()
        for o in opts:
            txt = (o.get('text') or '').strip()
            if not txt:
                errors.append(f"{prefix} Empty option {o.get('label')}")
            if txt.lower() in seen_texts:
                errors.append(f"{prefix} Duplicate option text: {txt}")
            seen_texts.add(txt.lower())

    ans = q.get('correctAnswer')
    if ans not in VALID_LABELS:
        errors.append(f"{prefix} Invalid correctAnswer: {ans}")

    oa = exp.get('optionAnalysis') or {}
    for lbl in ['A', 'B', 'C', 'D']:
        item = oa.get(lbl)
        if not item:
            errors.append(f"{prefix} Missing optionAnalysis[{lbl}]")
            continue
        expected_status = 'correct' if lbl == ans else 'trap'
        if item.get('status') != expected_status:
            errors.append(f"{prefix} optionAnalysis[{lbl}].status={item.get('status')} != {expected_status}")
        if not item.get('reasonVi') or len(item['reasonVi'].strip()) < 10:
            errors.append(f"{prefix} optionAnalysis[{lbl}].reasonVi too short")
    return errors

def validate_sat_test(content_json, test_title=''):
    errors = []
    mode = content_json.get('mode')
    if mode not in ('drill', 'adaptive_mock'):
        errors.append(f"[{test_title}] Invalid mode: {mode}")
        return errors

    modules = []
    if mode == 'drill':
        if not content_json.get('drillModule'):
            errors.append(f"[{test_title}] Missing drillModule")
        else:
            modules.append(('drill', content_json['drillModule']))
    else:
        for mk in ('module1', 'module2_hard', 'module2_lower'):
            if not content_json.get(mk):
                errors.append(f"[{test_title}] Missing {mk}")
            else:
                modules.append((mk, content_json[mk]))

    all_ids = set()
    for m_name, mod in modules:
        qs = mod.get('questions') or []
        if len(qs) == 0:
            errors.append(f"[{test_title}:{m_name}] Empty questions")
            continue
        ans_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        mcq_count = 0
        for i, q in enumerate(qs):
            if q.get('id') in all_ids:
                errors.append(f"[{test_title}:{m_name}] Duplicate question id: {q.get('id')}")
            all_ids.add(q.get('id'))
            errors.extend(validate_question(q, i, f"{test_title}:{m_name}"))
            if q.get('questionFormat', 'mcq') != 'spr' and q.get('correctAnswer') in ans_counts:
                ans_counts[q['correctAnswer']] += 1
                mcq_count += 1
        # Check answer balance for MCQ questions (no single letter > 55% for >=10 MCQ questions)
        if mcq_count >= 10:
            max_ratio = max(ans_counts.values()) / mcq_count
            if max_ratio > 0.55:
                errors.append(f"[{test_title}:{m_name}] Imbalanced answer keys: {ans_counts}")

    return errors

if __name__ == '__main__':
    print("SAT QA Validator (R&W + Math + SPR) ready.")
