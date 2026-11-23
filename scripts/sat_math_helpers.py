# -*- coding: utf-8 -*-
"""
Shared builders & crisp SVG diagram generators for Digital SAT Math 1500+
(Drills, Adaptive Mock Tests, and Lecture Cards).
"""

from fractions import Fraction

def math_mcq(
    qid, number, domain, skill, difficulty,
    stimulus_html, question_html,
    options_dict, correct_label,
    summary_vi, key_takeaway, option_analysis,
    desmos_tip_vi=''
):
    """Builds a validated SAT Bluebook Math MCQ question object."""
    assert correct_label in ('A', 'B', 'C', 'D'), f"Bad label {correct_label}"
    opts = [{'label': lbl, 'text': options_dict[lbl]} for lbl in ('A', 'B', 'C', 'D')]
    oa = {}
    for lbl in ('A', 'B', 'C', 'D'):
        tag, reason = option_analysis[lbl]
        oa[lbl] = {
            'status': 'correct' if lbl == correct_label else 'trap',
            'trapTag': tag,
            'reasonVi': reason,
        }
    exp = {
        'summaryVi': summary_vi,
        'keyTakeaway': key_takeaway,
        'optionAnalysis': oa,
    }
    if desmos_tip_vi:
        exp['desmosTipVi'] = desmos_tip_vi
    return {
        'id': qid,
        'number': number,
        'domain': domain,
        'skill': skill,
        'difficulty': difficulty,
        'questionFormat': 'mcq',
        'stimulusHtml': stimulus_html,
        'questionHtml': question_html,
        'options': opts,
        'correctAnswer': correct_label,
        'explanation': exp,
    }

def math_spr(
    qid, number, domain, skill, difficulty,
    stimulus_html, question_html,
    accepted_answers, correct_display,
    summary_vi, key_takeaway,
    desmos_tip_vi=''
):
    """Builds a validated SAT Bluebook Student-Produced Response (Grid-In) question object."""
    assert len(accepted_answers) >= 1, "Must provide at least one accepted answer"
    exp = {
        'summaryVi': summary_vi,
        'keyTakeaway': key_takeaway,
    }
    if desmos_tip_vi:
        exp['desmosTipVi'] = desmos_tip_vi
    return {
        'id': qid,
        'number': number,
        'domain': domain,
        'skill': skill,
        'difficulty': difficulty,
        'questionFormat': 'spr',
        'stimulusHtml': stimulus_html,
        'questionHtml': question_html,
        'options': [],
        'correctAnswer': str(accepted_answers[0]),
        'acceptedAnswers': [str(a) for a in accepted_answers],
        'correctDisplay': correct_display,
        'explanation': exp,
    }

def build_math_drill_json(title, subtitle, skill_badge, questions, target_minutes=22):
    return {
        'schemaVersion': 2,
        'mode': 'drill',
        'section': 'Math',
        'basicInfo': {
            'title': title,
            'subtitle': subtitle,
            'difficultyBadge': skill_badge,
            'targetTimeMinutes': target_minutes,
        },
        'drillModule': {
            'id': 'drill',
            'title': title,
            'subtitle': subtitle,
            'timeLimitMinutes': target_minutes,
            'questions': questions,
        },
    }

def build_math_adaptive_mock_json(title, subtitle, m1_qs, m2_hard_qs, m2_lower_qs, routing_threshold=15):
    return {
        'schemaVersion': 2,
        'mode': 'adaptive_mock',
        'section': 'Math',
        'basicInfo': {
            'title': title,
            'subtitle': subtitle,
            'difficultyBadge': 'Full-Length Adaptive Math (200–800)',
            'targetTimeMinutes': 70,
            'routingThreshold': routing_threshold,
        },
        'module1': {
            'id': 'm1',
            'title': 'Section 2, Module 1: Math',
            'subtitle': '22 Questions • 35 Minutes • Routing Module',
            'timeLimitMinutes': 35,
            'questions': m1_qs,
        },
        'module2_hard': {
            'id': 'm2_hard',
            'title': 'Section 2, Module 2: Math (Hard)',
            'subtitle': '22 Questions • 35 Minutes • 650–800 Band',
            'timeLimitMinutes': 35,
            'questions': m2_hard_qs,
        },
        'module2_lower': {
            'id': 'm2_lower',
            'title': 'Section 2, Module 2: Math (Standard)',
            'subtitle': '22 Questions • 35 Minutes • Foundation Band',
            'timeLimitMinutes': 35,
            'questions': m2_lower_qs,
        },
    }

# ============================================================================
# CRISP OFFICIAL BLUEBOOK-STYLE SVG DIAGRAM GENERATORS
# ============================================================================

def svg_right_triangle(a_lbl='a', b_lbl='b', c_lbl='c', angle_bottom_right='', angle_top_left='', v_top='A', v_right_angle='B', v_right='C', note=''):
    return f'''<svg viewBox="0 0 260 185" width="260" height="185" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="52,145 210,145 52,32" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.4" stroke-linejoin="round"/>
  <rect x="52" y="131" width="14" height="14" fill="none" stroke="#1e3a8a" stroke-width="1.8"/>
  <text x="42" y="28" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">{v_top}</text>
  <text x="38" y="158" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">{v_right_angle}</text>
  <text x="216" y="156" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">{v_right}</text>
  <text x="16" y="95" font-family="sans-serif" font-size="13" font-weight="700" fill="#1e3a8a">{a_lbl}</text>
  <text x="122" y="166" font-family="sans-serif" font-size="13" font-weight="700" fill="#1e3a8a">{b_lbl}</text>
  <text x="140" y="78" font-family="sans-serif" font-size="13" font-weight="700" fill="#0f172a">{c_lbl}</text>
  {f'<text x="162" y="138" font-family="sans-serif" font-size="12" font-weight="700" fill="#b91c1c">{angle_bottom_right}</text>' if angle_bottom_right else ''}
  {f'<text x="58" y="64" font-family="sans-serif" font-size="12" font-weight="700" fill="#b91c1c">{angle_top_left}</text>' if angle_top_left else ''}
  {f'<text x="130" y="180" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">{note}</text>' if note else ''}
</svg>'''

def svg_parallel_transversal(line1='ℓ', line2='m', ang1_lbl='', ang2_lbl='', ang3_lbl='', note='Note: Figure not drawn to scale.'):
    return f'''<svg viewBox="0 0 280 185" width="280" height="185" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <line x1="25" y1="58" x2="250" y2="58" stroke="#1e3a8a" stroke-width="2.4"/>
  <line x1="25" y1="126" x2="250" y2="126" stroke="#1e3a8a" stroke-width="2.4"/>
  <line x1="92" y1="16" x2="188" y2="165" stroke="#0f172a" stroke-width="2.2"/>
  <text x="256" y="62" font-family="serif" font-style="italic" font-size="15" font-weight="bold" fill="#1e3a8a">{line1}</text>
  <text x="256" y="130" font-family="serif" font-style="italic" font-size="15" font-weight="bold" fill="#1e3a8a">{line2}</text>
  <polyline points="222,53 230,58 222,63" fill="none" stroke="#1e3a8a" stroke-width="2"/>
  <polyline points="222,121 230,126 222,131" fill="none" stroke="#1e3a8a" stroke-width="2"/>
  {f'<text x="128" y="49" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#b91c1c">{ang1_lbl}</text>' if ang1_lbl else ''}
  {f'<text x="172" y="117" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#b91c1c">{ang2_lbl}</text>' if ang2_lbl else ''}
  {f'<text x="115" y="143" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#047857">{ang3_lbl}</text>' if ang3_lbl else ''}
  <text x="140" y="179" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">{note}</text>
</svg>'''

def svg_circle_sector(radius_lbl='r', angle_lbl='θ', center_lbl='O', pt_a='A', pt_b='B', note=''):
    return f'''<svg viewBox="0 0 240 195" width="240" height="195" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <circle cx="120" cy="94" r="68" fill="#ffffff" stroke="#1e3a8a" stroke-width="2.4"/>
  <path d="M 120 94 L 188 94 A 68 68 0 0 0 154 35 Z" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>
  <circle cx="120" cy="94" r="3" fill="#0f172a"/>
  <text x="106" y="106" font-family="serif" font-size="13" font-weight="bold" fill="#0f172a">{center_lbl}</text>
  <text x="193" y="98" font-family="serif" font-size="13" font-weight="bold" fill="#0f172a">{pt_a}</text>
  <text x="157" y="29" font-family="serif" font-size="13" font-weight="bold" fill="#0f172a">{pt_b}</text>
  <text x="148" y="111" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1e3a8a">{radius_lbl}</text>
  <text x="134" y="81" font-family="sans-serif" font-size="12" font-weight="700" fill="#b91c1c">{angle_lbl}</text>
  {f'<text x="120" y="185" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">{note}</text>' if note else ''}
</svg>'''

def svg_similar_triangles(side_ab='', side_bc='', side_de='', side_ef='', v1='A', v2='B', v3='C', v4='D', v5='E', v6='F'):
    return f'''<svg viewBox="0 0 320 175" width="320" height="175" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="30,136 125,136 58,56" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.2"/>
  <text x="53" y="48" font-family="serif" font-size="13" font-weight="bold">{v1}</text>
  <text x="18" y="146" font-family="serif" font-size="13" font-weight="bold">{v2}</text>
  <text x="129" y="146" font-family="serif" font-size="13" font-weight="bold">{v3}</text>
  <text x="16" y="96" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a">{side_ab}</text>
  <text x="70" y="155" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a">{side_bc}</text>
  <polygon points="168,144 300,144 208,30" fill="#ecfdf5" stroke="#047857" stroke-width="2.2"/>
  <text x="204" y="22" font-family="serif" font-size="13" font-weight="bold">{v4}</text>
  <text x="154" y="152" font-family="serif" font-size="13" font-weight="bold">{v5}</text>
  <text x="303" y="152" font-family="serif" font-size="13" font-weight="bold">{v6}</text>
  <text x="158" y="86" font-family="sans-serif" font-size="12" font-weight="700" fill="#047857">{side_de}</text>
  <text x="226" y="163" font-family="sans-serif" font-size="12" font-weight="700" fill="#047857">{side_ef}</text>
</svg>'''

def svg_cylinder(r_lbl='r', h_lbl='h', note=''):
    return f'''<svg viewBox="0 0 220 190" width="220" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <path d="M 60 44 L 60 140 A 50 16 0 0 0 160 140 L 160 44" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.2"/>
  <ellipse cx="110" cy="44" rx="50" ry="16" fill="#dbeafe" stroke="#1e3a8a" stroke-width="2.2"/>
  <ellipse cx="110" cy="140" rx="50" ry="16" fill="none" stroke="#1e3a8a" stroke-width="1.5" stroke-dasharray="4 3"/>
  <line x1="110" y1="44" x2="160" y2="44" stroke="#b91c1c" stroke-width="2"/>
  <circle cx="110" cy="44" r="2.5" fill="#0f172a"/>
  <text x="130" y="39" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#b91c1c">{r_lbl}</text>
  <text x="169" y="97" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1e3a8a">{h_lbl}</text>
  {f'<text x="110" y="180" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">{note}</text>' if note else ''}
</svg>'''

def svg_parabola_vertex(h_lbl='h', k_lbl='k', opens_up=True, pt_lbl='', note=''):
    path_d = "M 45 36 Q 130 220 215 36" if opens_up else "M 45 162 Q 130 -22 215 162"
    vy = 128 if opens_up else 70
    label_y = vy + 18 if opens_up else vy - 10
    return f'''<svg viewBox="0 0 260 190" width="260" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <line x1="20" y1="100" x2="245" y2="100" stroke="#94a3b8" stroke-width="1.6"/>
  <line x1="100" y1="12" x2="100" y2="176" stroke="#94a3b8" stroke-width="1.6"/>
  <text x="238" y="95" font-family="serif" font-style="italic" font-size="13" fill="#475569">x</text>
  <text x="106" y="22" font-family="serif" font-style="italic" font-size="13" fill="#475569">y</text>
  <path d="{path_d}" fill="none" stroke="#1d4ed8" stroke-width="2.6"/>
  <circle cx="130" cy="{vy}" r="4" fill="#dc2626"/>
  <text x="136" y="{label_y}" font-family="sans-serif" font-size="12" font-weight="700" fill="#dc2626">({h_lbl}, {k_lbl})</text>
  {f'<text x="165" y="48" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#0f172a">{pt_lbl}</text>' if pt_lbl else ''}
  {f'<text x="130" y="185" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">{note}</text>' if note else ''}
</svg>'''

def build_math_table(headers, rows, caption=''):
    th = ''.join(f'<th>{h}</th>' for h in headers)
    trs = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    cap = f'<div style="font-weight:800;font-size:13.5px;color:#0f172a;margin-bottom:6px;">{caption}</div>' if caption else ''
    return f'{cap}<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'
