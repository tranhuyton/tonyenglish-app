# -*- coding: utf-8 -*-
"""
Digital SAT Math 1500+ — Module 4: Geometry & Trigonometry (750–800)
3 Flagship Skill Drills × 15 Questions = 45 Original, Copyright-Clean Questions:
  - Drill 4.1: Lines, Angles, Similarity & Special Right Triangles (order_index 10)
  - Drill 4.2: Circles — Completing the Square, Arcs, Sectors & Radians (order_index 11)
  - Drill 4.3: Trigonometry (SOH-CAH-TOA, Cofunctions) & 3D Solid Scaling (order_index 12)
"""

import os
import sys
import math
import re
from fractions import Fraction

sys.path.insert(0, os.path.dirname(__file__))
from sat_math_helpers import (
    math_mcq,
    math_spr,
    build_math_drill_json,
    svg_right_triangle,
    svg_parallel_transversal,
    svg_circle_sector,
    svg_similar_triangles,
    svg_cylinder,
)
from sat_qa_validator import validate_sat_test


# ============================================================================
# ADDITIONAL BLUEBOOK-STYLE SVG DIAGRAM HELPERS (M4 GEOMETRY & TRIG)
# ============================================================================

def _wrap_svg(svg_str):
    return f'<div style="display:flex;justify-content:center;margin:0 auto 14px;">{svg_str}</div>'


def svg_exterior_angle(ang_p='(2k+14)°', ang_q='(3k−6)°', ext_r='(6k−11)°'):
    return f'''<svg viewBox="0 0 300 185" width="300" height="185" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="48,142 182,142 126,38" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.4" stroke-linejoin="round"/>
  <line x1="182" y1="142" x2="274" y2="142" stroke="#1e3a8a" stroke-width="2.4"/>
  <path d="M 171 122 A 22 22 0 0 1 204 142" fill="none" stroke="#b91c1c" stroke-width="2"/>
  <text x="122" y="28" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">P</text>
  <text x="34" y="152" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">Q</text>
  <text x="178" y="160" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">R</text>
  <text x="276" y="147" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">S</text>
  <text x="92" y="78" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#1e3a8a">{ang_p}</text>
  <text x="64" y="135" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#1e3a8a">{ang_q}</text>
  <text x="197" y="124" font-family="sans-serif" font-size="12" font-weight="700" fill="#b91c1c">{ext_r}</text>
  <text x="150" y="177" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Note: Figure not drawn to scale.</text>
</svg>'''


def svg_nested_triangle(ad_lbl='6', db_lbl='9', de_lbl='8', bc_lbl='?', shaded_trap=False):
    trap_fill = '#dbeafe' if shaded_trap else '#eff6ff'
    return f'''<svg viewBox="0 0 270 190" width="270" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="135,28 45,152 225,152" fill="{trap_fill}" stroke="#1e3a8a" stroke-width="2.4" stroke-linejoin="round"/>
  <polygon points="135,28 99,78 171,78" fill="#ffffff" stroke="#1e3a8a" stroke-width="2.2" stroke-linejoin="round"/>
  <polyline points="132,74 139,78 132,82" fill="none" stroke="#b91c1c" stroke-width="2"/>
  <polyline points="132,148 139,152 132,156" fill="none" stroke="#b91c1c" stroke-width="2"/>
  <text x="131" y="21" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">A</text>
  <text x="82" y="80" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">D</text>
  <text x="177" y="80" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">E</text>
  <text x="31" y="158" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="230" y="158" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">C</text>
  <text x="98" y="52" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a">{ad_lbl}</text>
  <text x="53" y="118" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a">{db_lbl}</text>
  {f'<text x="135" y="72" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#b91c1c">{de_lbl}</text>' if de_lbl else ''}
  {f'<text x="135" y="168" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#047857">{bc_lbl}</text>' if bc_lbl else ''}
  <text x="135" y="184" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">DE ∥ BC • Figure not drawn to scale.</text>
</svg>'''


def svg_equilateral_altitude(h_lbl='12'):
    return f'''<svg viewBox="0 0 250 185" width="250" height="185" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="125,28 45,152 205,152" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.4" stroke-linejoin="round"/>
  <line x1="125" y1="28" x2="125" y2="152" stroke="#b91c1c" stroke-width="2" stroke-dasharray="5 3"/>
  <rect x="125" y="140" width="12" height="12" fill="none" stroke="#b91c1c" stroke-width="1.6"/>
  <text x="121" y="21" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">X</text>
  <text x="32" y="158" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">Y</text>
  <text x="210" y="158" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">Z</text>
  <text x="120" y="168" font-family="serif" font-size="13" font-weight="bold" fill="#0f172a">W</text>
  <text x="132" y="98" font-family="sans-serif" font-size="13" font-weight="700" fill="#b91c1c">{h_lbl}</text>
  <text x="125" y="181" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Equilateral △XYZ with altitude XW</text>
</svg>'''


def svg_altitude_split_triangle(left_hyp='25', right_hyp='26', alt_lbl='24', v_top='A', v_left='D', v_foot='B', v_right='C', ang_left='', ang_right='', note='Note: Figure not drawn to scale.'):
    return f'''<svg viewBox="0 0 290 185" width="290" height="185" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="118,32 42,148 248,148" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.4" stroke-linejoin="round"/>
  <line x1="118" y1="32" x2="118" y2="148" stroke="#b91c1c" stroke-width="2" stroke-dasharray="5 3"/>
  <rect x="118" y="136" width="12" height="12" fill="none" stroke="#b91c1c" stroke-width="1.6"/>
  <text x="113" y="24" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">{v_top}</text>
  <text x="28" y="155" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">{v_left}</text>
  <text x="113" y="164" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">{v_foot}</text>
  <text x="252" y="155" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">{v_right}</text>
  {f'<text x="58" y="85" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1e3a8a">{left_hyp}</text>' if left_hyp else ''}
  {f'<text x="192" y="85" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1e3a8a">{right_hyp}</text>' if right_hyp else ''}
  {f'<text x="124" y="98" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#b91c1c">{alt_lbl}</text>' if alt_lbl else ''}
  {f'<text x="58" y="142" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#047857">{ang_left}</text>' if ang_left else ''}
  {f'<text x="206" y="142" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#047857">{ang_right}</text>' if ang_right else ''}
  <text x="145" y="179" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">{note}</text>
</svg>'''


def svg_bent_parallel(ang_top='(2x + 10)°', ang_mid='115°', ang_bot='(3x − 5)°'):
    return f'''<svg viewBox="0 0 290 190" width="290" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <line x1="24" y1="42" x2="262" y2="42" stroke="#1e3a8a" stroke-width="2.4"/>
  <line x1="24" y1="146" x2="262" y2="146" stroke="#1e3a8a" stroke-width="2.4"/>
  <polyline points="236,37 244,42 236,47" fill="none" stroke="#1e3a8a" stroke-width="2"/>
  <polyline points="236,141 244,146 236,151" fill="none" stroke="#1e3a8a" stroke-width="2"/>
  <polyline points="78,42 182,94 94,146" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linejoin="round"/>
  <circle cx="78" cy="42" r="3" fill="#0f172a"/>
  <circle cx="182" cy="94" r="3" fill="#b91c1c"/>
  <circle cx="94" cy="146" r="3" fill="#0f172a"/>
  <text x="267" y="46" font-family="serif" font-style="italic" font-size="15" font-weight="bold" fill="#1e3a8a">ℓ</text>
  <text x="267" y="150" font-family="serif" font-style="italic" font-size="15" font-weight="bold" fill="#1e3a8a">m</text>
  <text x="72" y="34" font-family="serif" font-size="13" font-weight="bold" fill="#0f172a">A</text>
  <text x="190" y="98" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">P</text>
  <text x="86" y="162" font-family="serif" font-size="13" font-weight="bold" fill="#0f172a">B</text>
  <text x="112" y="58" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#1e3a8a">{ang_top}</text>
  <text x="134" y="98" font-family="sans-serif" font-size="12" font-weight="700" fill="#b91c1c">{ang_mid}</text>
  <text x="122" y="140" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#047857">{ang_bot}</text>
  <text x="145" y="182" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">ℓ ∥ m • Note: Figure not drawn to scale.</text>
</svg>'''


def svg_right_altitude_hyp(pq='15', sr='16', v_left='P', v_top='Q', v_right='R', v_foot='S'):
    return f'''<svg viewBox="0 0 295 185" width="295" height="185" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="40,142 120,40 256,142" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.4" stroke-linejoin="round"/>
  <line x1="120" y1="40" x2="120" y2="142" stroke="#b91c1c" stroke-width="2" stroke-dasharray="5 3"/>
  <rect x="120" y="130" width="12" height="12" fill="none" stroke="#b91c1c" stroke-width="1.6"/>
  <polyline points="111,51 121,59 129,48" fill="none" stroke="#1e3a8a" stroke-width="1.7"/>
  <text x="27" y="149" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">{v_left}</text>
  <text x="115" y="30" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">{v_top}</text>
  <text x="260" y="149" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">{v_right}</text>
  <text x="115" y="160" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">{v_foot}</text>
  {f'<text x="58" y="84" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1e3a8a">{pq}</text>' if pq else ''}
  {f'<text x="182" y="159" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#047857">{sr}</text>' if sr else ''}
  <text x="147" y="178" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">∠{v_left}{v_top}{v_right} = 90° and {v_top}{v_foot} ⊥ {v_left}{v_right}</text>
</svg>'''


def svg_inscribed_square_rt():
    return '''<svg viewBox="0 0 270 185" width="270" height="185" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="48,150 226,150 48,30" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.4" stroke-linejoin="round"/>
  <rect x="48" y="79" width="71" height="71" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2.2"/>
  <rect x="48" y="138" width="12" height="12" fill="none" stroke="#1e3a8a" stroke-width="1.6"/>
  <text x="38" y="26" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">A</text>
  <text x="34" y="162" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="232" y="158" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">C</text>
  <text x="33" y="83" font-family="serif" font-size="13" font-weight="bold" fill="#1d4ed8">D</text>
  <text x="124" y="76" font-family="serif" font-size="13" font-weight="bold" fill="#1d4ed8">E</text>
  <text x="115" y="166" font-family="serif" font-size="13" font-weight="bold" fill="#1d4ed8">F</text>
  <text x="150" y="78" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#b91c1c">AC = 35</text>
  <text x="14" y="120" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#1e3a8a" transform="rotate(-90 14 120)">AB = 21</text>
  <text x="135" y="180" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Square BDEF inscribed in right △ABC</text>
</svg>'''


def svg_inscribed_central(ins_lbl='(2x+8)°', cen_lbl='(5x−10)°'):
    return f'''<svg viewBox="0 0 250 195" width="250" height="195" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <circle cx="125" cy="96" r="68" fill="#ffffff" stroke="#1e3a8a" stroke-width="2.4"/>
  <polygon points="125,96 66,130 184,130" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2"/>
  <polyline points="66,130 105,31 184,130" fill="none" stroke="#047857" stroke-width="2.1"/>
  <circle cx="125" cy="96" r="3" fill="#0f172a"/>
  <text x="128" y="92" font-family="serif" font-size="13" font-weight="bold" fill="#0f172a">O</text>
  <text x="51" y="138" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">A</text>
  <text x="189" y="138" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">B</text>
  <text x="100" y="23" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">C</text>
  <text x="86" y="61" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#047857">{ins_lbl}</text>
  <text x="103" y="122" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#b91c1c">{cen_lbl}</text>
  <text x="125" y="185" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Center O • Figure not drawn to scale.</text>
</svg>'''


def svg_circle_tangent(pq_lbl='24', rq_lbl='16'):
    return f'''<svg viewBox="0 0 285 190" width="285" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <circle cx="96" cy="96" r="56" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.4"/>
  <line x1="96" y1="96" x2="96" y2="40" stroke="#1e3a8a" stroke-width="2.2"/>
  <line x1="96" y1="40" x2="246" y2="40" stroke="#b91c1c" stroke-width="2.4"/>
  <line x1="96" y1="96" x2="246" y2="40" stroke="#0f172a" stroke-width="2.2"/>
  <rect x="96" y="40" width="11" height="11" fill="none" stroke="#b91c1c" stroke-width="1.6"/>
  <circle cx="96" cy="96" r="3" fill="#0f172a"/>
  <circle cx="96" cy="40" r="3" fill="#b91c1c"/>
  <circle cx="148.5" cy="76.4" r="3" fill="#047857"/>
  <circle cx="246" cy="40" r="3" fill="#0f172a"/>
  <text x="82" y="106" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">O</text>
  <text x="88" y="32" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">P</text>
  <text x="150" y="92" font-family="serif" font-size="13" font-weight="bold" fill="#047857">R</text>
  <text x="252" y="44" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">Q</text>
  <text x="166" y="33" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#b91c1c">{pq_lbl}</text>
  <text x="195" y="75" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#047857">{rq_lbl}</text>
  <text x="82" y="72" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a">r</text>
  <text x="142" y="179" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">PQ is tangent to circle O at P.</text>
</svg>'''


def svg_circle_segment_120():
    return '''<svg viewBox="0 0 250 195" width="250" height="195" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <circle cx="125" cy="96" r="68" fill="#ffffff" stroke="#1e3a8a" stroke-width="2.4"/>
  <path d="M 66.1 62 A 68 68 0 0 1 183.9 62 Z" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>
  <polyline points="66.1,62 125,96 183.9,62" fill="none" stroke="#1e3a8a" stroke-width="2.1"/>
  <circle cx="125" cy="96" r="3" fill="#0f172a"/>
  <text x="120" y="114" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">O</text>
  <text x="50" y="61" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">A</text>
  <text x="188" y="61" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">B</text>
  <text x="112" y="83" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#b91c1c">2π/3</text>
  <text x="82" y="92" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a">6</text>
  <text x="125" y="185" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Shaded minor circular segment</text>
</svg>'''


def svg_two_tangents_circle():
    return '''<svg viewBox="0 0 285 190" width="285" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <circle cx="95" cy="95" r="54" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.4"/>
  <line x1="95" y1="95" x2="122" y2="48.2" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="95" y1="95" x2="122" y2="141.8" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="122" y1="48.2" x2="245" y2="95" stroke="#b91c1c" stroke-width="2.2"/>
  <line x1="122" y1="141.8" x2="245" y2="95" stroke="#b91c1c" stroke-width="2.2"/>
  <line x1="95" y1="95" x2="245" y2="95" stroke="#0f172a" stroke-width="1.8" stroke-dasharray="5 3"/>
  <circle cx="95" cy="95" r="3" fill="#0f172a"/>
  <circle cx="245" cy="95" r="3" fill="#0f172a"/>
  <text x="80" y="99" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">O</text>
  <text x="119" y="40" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">A</text>
  <text x="119" y="159" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">B</text>
  <text x="252" y="99" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">P</text>
  <text x="96" y="72" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#1e3a8a">15</text>
  <text x="166" y="90" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#0f172a">OP = 30</text>
  <text x="142" y="180" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">PA and PB are tangent to circle O.</text>
</svg>'''


def svg_cone(r_lbl='6', l_lbl='10'):
    return f'''<svg viewBox="0 0 230 190" width="230" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <path d="M 55 140 L 115 30 L 175 140" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.4" stroke-linejoin="round"/>
  <ellipse cx="115" cy="140" rx="60" ry="16" fill="#dbeafe" stroke="#1e3a8a" stroke-width="2.2"/>
  <line x1="115" y1="30" x2="115" y2="140" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4 3"/>
  <line x1="115" y1="140" x2="175" y2="140" stroke="#b91c1c" stroke-width="2"/>
  <rect x="115" y="129" width="11" height="11" fill="none" stroke="#64748b" stroke-width="1.4"/>
  <text x="142" y="135" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#b91c1c">{r_lbl}</text>
  <text x="155" y="84" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1e3a8a">{l_lbl}</text>
  <text x="115" y="180" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Right circular cone (slant height = {l_lbl})</text>
</svg>'''


def svg_square_pyramid(b_lbl='12', l_lbl='10'):
    return f'''<svg viewBox="0 0 250 190" width="250" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="48,144 162,144 206,112 92,112" fill="#dbeafe" stroke="#1e3a8a" stroke-width="2"/>
  <polygon points="127,26 48,144 162,144" fill="#eff6ff" fill-opacity="0.72" stroke="#1e3a8a" stroke-width="2.2" stroke-linejoin="round"/>
  <polygon points="127,26 162,144 206,112" fill="#dbeafe" fill-opacity="0.65" stroke="#1e3a8a" stroke-width="2.2" stroke-linejoin="round"/>
  <line x1="127" y1="26" x2="92" y2="112" stroke="#1e3a8a" stroke-width="1.4" stroke-dasharray="4 3"/>
  <line x1="127" y1="26" x2="127" y2="128" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4 3"/>
  <line x1="127" y1="26" x2="184" y2="128" stroke="#b91c1c" stroke-width="2"/>
  <text x="100" y="160" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1e3a8a">{b_lbl}</text>
  <text x="166" y="76" font-family="sans-serif" font-size="12" font-weight="700" fill="#b91c1c">l = {l_lbl}</text>
  <text x="125" y="180" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Right square pyramid</text>
</svg>'''


def svg_cone_in_cylinder(r_lbl='6', h_lbl='8'):
    return f'''<svg viewBox="0 0 230 195" width="230" height="195" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <path d="M 60 44 L 60 144 A 52 16 0 0 0 164 144 L 164 44" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.2"/>
  <polygon points="60,44 164,44 112,144" fill="#fee2e2" fill-opacity="0.65" stroke="#b91c1c" stroke-width="1.9" stroke-dasharray="5 3"/>
  <ellipse cx="112" cy="44" rx="52" ry="15" fill="#dbeafe" fill-opacity="0.7" stroke="#1e3a8a" stroke-width="2.2"/>
  <ellipse cx="112" cy="144" rx="52" ry="15" fill="none" stroke="#1e3a8a" stroke-width="1.4" stroke-dasharray="4 3"/>
  <line x1="112" y1="44" x2="164" y2="44" stroke="#b91c1c" stroke-width="2"/>
  <circle cx="112" cy="44" r="2.5" fill="#0f172a"/>
  <text x="134" y="38" font-family="sans-serif" font-size="12" font-weight="700" fill="#b91c1c">r = {r_lbl}</text>
  <text x="172" y="98" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1e3a8a">h = {h_lbl}</text>
  <text x="115" y="184" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Cone hollowed out of cylinder</text>
</svg>'''


def svg_similar_right_triangles():
    return '''<svg viewBox="0 0 325 180" width="325" height="180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="36,138 118,138 36,68" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.2" stroke-linejoin="round"/>
  <rect x="36" y="127" width="11" height="11" fill="none" stroke="#1e3a8a" stroke-width="1.5"/>
  <text x="28" y="61" font-family="serif" font-size="13" font-weight="bold">A</text>
  <text x="23" y="148" font-family="serif" font-size="13" font-weight="bold">B</text>
  <text x="122" y="148" font-family="serif" font-size="13" font-weight="bold">C</text>
  <polygon points="168,144 298,144 168,32" fill="#ecfdf5" stroke="#047857" stroke-width="2.2" stroke-linejoin="round"/>
  <rect x="168" y="131" width="13" height="13" fill="none" stroke="#047857" stroke-width="1.6"/>
  <text x="160" y="25" font-family="serif" font-size="13.5" font-weight="bold">D</text>
  <text x="154" y="154" font-family="serif" font-size="13.5" font-weight="bold">E</text>
  <text x="303" y="154" font-family="serif" font-size="13.5" font-weight="bold">F</text>
  <text x="162" y="172" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">△ABC ~ △DEF (scale factor 4) • Not drawn to scale.</text>
</svg>'''


# ============================================================================
# DRILL 4.1: LINES, ANGLES, SIMILARITY & SPECIAL RIGHT TRIANGLES (15 Qs)
# ============================================================================

def get_drill_m4_1():
    qs = [
        # Q1 — Medium, MCQ, Ans: B
        math_mcq(
            'sat_m4_1_q1', 1, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium',
            _wrap_svg(svg_parallel_transversal(line1='ℓ', line2='m', ang1_lbl='(5x + 28)°', ang2_lbl='(7x − 16)°', ang3_lbl=''))
            + r'<p>In the figure shown, line \(\ell\) is parallel to line \(m\), and both lines are intersected by a transversal.</p>',
            r'What is the measure, in degrees, of an angle that is supplementary to the angle measuring \((5x + 28)^\circ\)?',
            {'A': r'\(22\)', 'B': r'\(42\)', 'C': r'\(138\)', 'D': r'\(158\)'},
            'B',
            r'Vì \(\ell \parallel m\), hai góc \((5x + 28)^\circ\) và \((7x - 16)^\circ\) ở vị trí đồng vị (corresponding angles) nên bằng nhau: \[5x + 28 = 7x - 16 \implies 2x = 44 \implies x = 22.\] Khi đó góc đã cho có số đo \(5(22) + 28 = 138^\circ\). Đề hỏi góc kề bù (supplementary) với góc này: \(180^\circ - 138^\circ = 42^\circ\).',
            r'Khi hai đường thẳng song song bị cắt bởi cát tuyến, mọi cặp góc chỉ có 2 khả năng: bằng nhau hoặc bù nhau (\(180^\circ\)). Luôn đọc kỹ xem đề hỏi \(x\), góc đã cho, hay góc bù của nó.',
            {
                'A': ('Stopped Early', r'\(22\) mới chỉ là giá trị của ẩn \(x\), chưa thay vào để tính góc và lấy góc kề bù.'),
                'B': ('Đáp án đúng', r'Góc đồng vị cho \(x = 22\), góc tù bằng \(138^\circ\), suy ra góc bù là \(180^\circ - 138^\circ = 42^\circ\).'),
                'C': ('Wrong Quantity', r'\(138^\circ\) là số đo của chính góc \((5x + 28)^\circ\), quên bước trừ đi từ \(180^\circ\) theo yêu cầu "supplementary".'),
                'D': ('Arithmetic Trap', r'Tính nhầm \(180 - x = 180 - 22 = 158\) thay vì \(180 - (5x + 28)\).'),
            },
            desmos_tip_vi=r'Gõ <code>y = 5x + 28</code> và <code>y = 7x - 16</code> vào Desmos để chấm giao điểm \((22, 138)\) trong 3 giây, rồi gõ ngay <code>180 - 138</code> để lấy đáp án \(42\) mà không lo sai dấu.'
        ),

        # Q2 — Medium, MCQ, Ans: C
        math_mcq(
            'sat_m4_1_q2', 2, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium',
            _wrap_svg(svg_exterior_angle(ang_p='(2k + 14)°', ang_q='(3k − 6)°', ext_r='(6k − 11)°'))
            + r'<p>In the figure shown, side \(\overline{QR}\) of triangle \(PQR\) is extended to point \(S\). The interior angles at \(P\) and \(Q\) measure \((2k + 14)^\circ\) and \((3k - 6)^\circ\), respectively, and exterior angle \(\angle PRS\) measures \((6k - 11)^\circ\).</p>',
            r'What is the measure, in degrees, of interior angle \(\angle PRQ\)?',
            {'A': r'\(19\)', 'B': r'\(52\)', 'C': r'\(77\)', 'D': r'\(103\)'},
            'C',
            r'Theo Định lý góc ngoài của tam giác (Exterior Angle Theorem), góc ngoài tại đỉnh \(R\) bằng tổng hai góc trong không kề với nó: \[(2k + 14) + (3k - 6) = 6k - 11 \implies 5k + 8 = 6k - 11 \implies k = 19.\] Từ đó góc ngoài \(\angle PRS = 6(19) - 11 = 103^\circ\). Do \(\angle PRQ\) và \(\angle PRS\) kề bù nên \[\angle PRQ = 180^\circ - 103^\circ = 77^\circ.\]',
            r'Định lý Góc ngoài: \(\text{Góc ngoài} = \text{Tổng 2 góc trong không kề}\) giúp bỏ qua bước đặt biến phụ cho góc trong thứ ba.',
            {
                'A': ('Stopped Early', r'\(19\) chỉ là giá trị của \(k\), không phải số đo góc \(\angle PRQ\).'),
                'B': ('Wrong Angle', r'\(52^\circ = 2(19) + 14\) là số đo góc \(\angle P\), không phải \(\angle PRQ\).'),
                'C': ('Đáp án đúng', r'Giải \(5k + 8 = 6k - 11 \Rightarrow k = 19\), góc ngoài \(103^\circ\), góc trong \(\angle PRQ = 180^\circ - 103^\circ = 77^\circ\).'),
                'D': ('Exterior vs Interior', r'\(103^\circ\) là số đo góc ngoài \(\angle PRS\), quên trừ từ \(180^\circ\) để ra góc trong \(\angle PRQ\).'),
            },
            desmos_tip_vi=r'Gõ <code>y = (2x + 14) + (3x - 6)</code> và <code>y = 6x - 11</code> trên Desmos → giao điểm \((19, 103)\) cho thẳng \(k = 19\) và góc ngoài \(= 103\), cuối cùng bấm <code>180 - 103 = 77</code>.'
        ),

        # Q3 — Medium, MCQ, Ans: A
        math_mcq(
            'sat_m4_1_q3', 3, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium',
            _wrap_svg(svg_similar_triangles(side_ab='12', side_bc='18', side_de='20', side_ef='?'))
            + r'<p>Triangles \(ABC\) and \(DEF\) are similar, where vertices \(A\), \(B\), and \(C\) correspond to vertices \(D\), \(E\), and \(F\), respectively. In triangle \(ABC\), \(AB = 12\), \(BC = 18\), and \(AC = 15\). In triangle \(DEF\), \(DE = 20\).</p>',
            r'What is the perimeter of triangle \(DEF\)?',
            {'A': r'\(75\)', 'B': r'\(30\)', 'C': r'\(53\)', 'D': r'\(125\)'},
            'A',
            r'Tỉ số đồng dạng (linear scale factor) từ \(\triangle ABC\) sang \(\triangle DEF\) là \[k = \frac{DE}{AB} = \frac{20}{12} = \frac{5}{3}.\] Chu vi \(\triangle ABC\) là \(12 + 18 + 15 = 45\). Vì chu vi là đại lượng bậc 1 (tỉ lệ thuận với \(k\)), ta có ngay \[\text{Perimeter}(\triangle DEF) = 45 \times \frac{5}{3} = 75.\]',
            r'Với hai tam giác đồng dạng tỉ số \(k\): cạnh, đường cao, trung tuyến và chu vi đều nhân với \(k\); chỉ có diện tích mới nhân với \(k^2\).',
            {
                'A': ('Đáp án đúng', r'Tỉ số đồng dạng \(k = \frac{20}{12} = \frac{5}{3}\), chu vi \(\triangle DEF = 45 \times \frac{5}{3} = 75\).'),
                'B': ('Partial Computation', r'\(30 = 18 \times \frac{5}{3}\) mới chỉ là độ dài riêng cạnh \(EF\), chưa cộng thành chu vi.'),
                'C': ('Additive Error', r'Cộng thêm hiệu \(20 - 12 = 8\) vào chu vi \(45\) (\(45 + 8 = 53\)) thay vì nhân theo tỉ lệ đồng dạng.'),
                'D': ('Area Ratio Trap', r'Nhân chu vi với \(k^2 = \frac{25}{9}\) ra \(45 \times \frac{25}{9} = 125\) — nhầm quy tắc diện tích sang chu vi.'),
            },
            desmos_tip_vi=r'Tính gộp 1 dòng trên Desmos: <code>(12 + 18 + 15) * (20 / 12)</code> ra ngay <code>75</code>, không cần tính rời từng cạnh \(EF\) và \(DF\).'
        ),

        # Q4 — Medium, SPR (Ans: 90)
        math_spr(
            'sat_m4_1_q4', 4, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium',
            _wrap_svg(svg_right_triangle(a_lbl='15', b_lbl='36', c_lbl='x', v_top='A', v_right_angle='B', v_right='C', note='Note: Figure not drawn to scale.'))
            + r'<p>In right triangle \(ABC\) shown above, \(\angle B = 90^\circ\), \(AB = 15\), and \(BC = 36\).</p>',
            r'What is the perimeter of triangle \(ABC\)?',
            ['90'],
            '90',
            r'Nhận diện nhanh bộ ba Pytago cơ bản \(5\text{–}12\text{–}13\) nhân với hệ số \(3\): \[AB = 3(5) = 15, \quad BC = 3(12) = 36 \implies AC = 3(13) = 39.\] (Hoặc tính trực tiếp \(AC = \sqrt{15^2 + 36^2} = \sqrt{225 + 1296} = \sqrt{1521} = 39\).) Chu vi tam giác \(ABC\) là \[15 + 36 + 39 = 90.\]',
            r'Thuộc lòng 4 bộ ba Pytago vàng của SAT (\(3\text{–}4\text{–}5\), \(5\text{–}12\text{–}13\), \(8\text{–}15\text{–}17\), \(7\text{–}24\text{–}25\)) cùng bội số của chúng giúp bạn chốt cạnh huyền trong 2 giây.',
            desmos_tip_vi=r'Bấm 1 dòng duy nhất trên Desmos: <code>15 + 36 + sqrt(15^2 + 36^2)</code> để ra ngay <code>90</code>.'
        ),

        # Q5 — Medium-Hard, MCQ, Ans: D
        math_mcq(
            'sat_m4_1_q5', 5, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium-Hard',
            _wrap_svg(svg_nested_triangle(ad_lbl='6', db_lbl='9', de_lbl='8', bc_lbl='?'))
            + r'<p>In triangle \(ABC\) shown, point \(D\) lies on \(\overline{AB}\) and point \(E\) lies on \(\overline{AC}\) such that \(\overline{DE} \parallel \overline{BC}\). If \(AD = 6\), \(DB = 9\), and \(DE = 8\), find the length of \(\overline{BC}\).</p>',
            r'What is the length of segment \(BC\)?',
            {'A': r'\(11\)', 'B': r'\(12\)', 'C': r'\(15\)', 'D': r'\(20\)'},
            'D',
            r'Vì \(\overline{DE} \parallel \overline{BC}\), ta có các cặp góc đồng vị bằng nhau nên \(\triangle ADE \sim \triangle ABC\) (theo trường hợp góc–góc AA). Cảnh giác bẫy kinh điển: cạnh tương ứng với \(AD\) là **toàn bộ cạnh \(AB\)**, không phải đoạn \(DB\)! \[AB = AD + DB = 6 + 9 = 15.\] Lập tỉ số đồng dạng: \[\frac{BC}{DE} = \frac{AB}{AD} \implies \frac{BC}{8} = \frac{15}{6} = \frac{5}{2} \implies BC = 8 \times \frac{5}{2} = 20.\]',
            r'Trong tam giác lồng nhau (\(\overline{DE} \parallel \overline{BC}\)), khi so sánh 2 đáy song song \(DE\) và \(BC\), BẮT BUỘC phải lấy tỉ số \(\frac{\text{nhỏ}}{\text{toàn phần}} = \frac{AD}{AD + DB}\), tuyệt đối không lấy \(\frac{AD}{DB}\).',
            {
                'A': ('Additive Error', r'Cộng chênh lệch \(8 + (9 - 6) = 11\), sai bản chất tỉ lệ đồng dạng.'),
                'B': ('Part-to-Part Trap', r'Bẫy SAT #1: dùng sai tỉ số \(\frac{DB}{AD} = \frac{9}{6} = 1.5\) để nhân \(8 \times 1.5 = 12\) thay vì dùng toàn cạnh \(AB = 15\).'),
                'C': ('Wrong Segment', r'\(15 = 6 + 9\) là độ dài cạnh bên \(AB\), không phải đáy \(BC\).'),
                'D': ('Đáp án đúng', r'\(\triangle ADE \sim \triangle ABC \Rightarrow \frac{BC}{8} = \frac{6+9}{6} = \frac{5}{2} \Rightarrow BC = 20\).'),
            },
            desmos_tip_vi=r'Gõ nhanh phép tính <code>8 * (6 + 9) / 6</code> trên Desmos để chốt <code>20</code> và luôn viết rõ mẫu <code>(6 + 9)</code> để tránh quên cộng toàn cạnh.'
        ),

        # Q6 — Medium-Hard, MCQ, Ans: A
        math_mcq(
            'sat_m4_1_q6', 6, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium-Hard',
            _wrap_svg(svg_equilateral_altitude(h_lbl='12'))
            + r'<p>Triangle \(XYZ\) is equilateral, and altitude \(\overline{XW}\) has a length of \(12\) units.</p>',
            r'What is the perimeter, in units, of triangle \(XYZ\)?',
            {'A': r'\(24\sqrt{3}\)', 'B': r'\(12\sqrt{3}\)', 'C': r'\(36\sqrt{3}\)', 'D': r'\(72\)'},
            'A',
            r'Đường cao \(\overline{XW}\) chia tam giác đều \(\triangle XYZ\) thành hai tam giác vuông đặc biệt \(30^\circ\text{–}60^\circ\text{–}90^\circ\) với tỉ lệ cạnh \(x : x\sqrt{3} : 2x\). Vì \(XW = 12\) là cạnh đối diện góc \(60^\circ\): \[x\sqrt{3} = 12 \implies x = \frac{12}{\sqrt{3}} = 4\sqrt{3}.\] Cạnh của tam giác đều là \(s = 2x = 8\sqrt{3}\). Suy ra chu vi tam giác đều là \[P = 3s = 3(8\sqrt{3}) = 24\sqrt{3}.\]',
            r'Trong tam giác đều cạnh \(s\), đường cao luôn là \(h = \frac{s\sqrt{3}}{2}\); ngược lại khi biết \(h\) là số nguyên, rút nhanh \(s = \frac{2h}{\sqrt{3}} = \frac{2h\sqrt{3}}{3}\).',
            {
                'A': ('Đáp án đúng', r'\(x\sqrt{3} = 12 \Rightarrow x = 4\sqrt{3} \Rightarrow s = 8\sqrt{3} \Rightarrow P = 3s = 24\sqrt{3}\).'),
                'B': ('Half-Side Trap', r'Nhầm \(x = 4\sqrt{3}\) (mới là nửa đáy \(YW\)) thành độ dài cả cạnh tam giác đều rồi nhân \(3\) ra \(12\sqrt{3}\).'),
                'C': ('Multiply Instead of Divide', r'Nhân \(12\) với \(\sqrt{3}\) thay vì chia cho \(\sqrt{3}\), ra nhầm cạnh \(s = 12\sqrt{3}\) và chu vi \(36\sqrt{3}\).'),
                'D': ('Forgot Radical', r'Gán nhầm \(x = 12\) (đối diện góc \(30^\circ\)) nên tính ra \(s = 24\) và \(P = 72\).'),
            },
            desmos_tip_vi=r'Tính giá trị xấp xỉ chu vi bằng <code>3 * (2 * 12 / sqrt(3))</code> ≈ <code>41.569</code> trên Desmos rồi so khớp với <code>24 * sqrt(3)</code> ≈ <code>41.569</code> — loại sạch nguy cơ trục căn nhầm!'
        ),

        # Q7 — Medium-Hard, MCQ, Ans: C
        math_mcq(
            'sat_m4_1_q7', 7, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium-Hard',
            _wrap_svg(svg_right_triangle(a_lbl='s', b_lbl='s', c_lbl='10√6', angle_bottom_right='45°', angle_top_left='45°', v_top='P', v_right_angle='Q', v_right='R'))
            + r'<p>In right isosceles triangle \(PQR\) shown above, \(\angle Q = 90^\circ\), \(PQ = QR = s\), and hypotenuse \(PR = 10\sqrt{6}\) centimeters.</p>',
            r'What is the area, in square centimeters, of triangle \(PQR\)?',
            {'A': r'\(75\)', 'B': r'\(100\sqrt{3}\)', 'C': r'\(150\)', 'D': r'\(300\)'},
            'C',
            r'Trong tam giác vuông cân \(45^\circ\text{–}45^\circ\text{–}90^\circ\), cạnh huyền bằng \(s\sqrt{2}\): \[s\sqrt{2} = 10\sqrt{6} \implies s = \frac{10\sqrt{6}}{\sqrt{2}} = 10\sqrt{3}.\] Diện tích tam giác \(PQR\) là \[\text{Area} = \frac{1}{2}s^2 = \frac{1}{2}\left(10\sqrt{3}\right)^2 = \frac{1}{2}(300) = 150.\]',
            r'Mẹo 800 Math: Với tam giác vuông cân có cạnh huyền \(c\), diện tích luôn tính thẳng bằng \(\text{Area} = \frac{c^2}{4}\) mà không cần tính \(s\) trước (\(\frac{(10\sqrt{6})^2}{4} = \frac{600}{4} = 150\)).',
            {
                'A': ('Extra Factor of 1/2', r'Chia đôi hai lần hoặc tính nhầm \(s = 5\sqrt{6} \Rightarrow \frac{1}{2}(150) = 75\).'),
                'B': ('Formula Confusion', r'Tính sai \(\frac{1}{2} \cdot 20 \cdot s\) thay vì \(\frac{1}{2}s^2\).'),
                'C': ('Đáp án đúng', r'\(s = \frac{10\sqrt{6}}{\sqrt{2}} = 10\sqrt{3} \Rightarrow \text{Area} = \frac{1}{2}(10\sqrt{3})^2 = 150\).'),
                'D': ('Forgot 1/2', r'Tính \(s^2 = 300\) (diện tích hình vuông cạnh \(s\)), quên nhân \(\frac{1}{2}\) cho tam giác.'),
            },
            desmos_tip_vi=r'Dùng công thức tắt \(\text{Area} = c^2 / 4\) trên Desmos: gõ <code>(10*sqrt(6))^2 / 4</code> hiện thẳng kết quả <code>150</code>.'
        ),

        # Q8 — Medium-Hard, SPR (Ans: 175)
        math_spr(
            'sat_m4_1_q8', 8, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium-Hard',
            _wrap_svg(svg_similar_triangles(side_ab='6', side_bc='', side_de='15', side_ef=''))
            + r'<p>Triangles \(ABC\) and \(DEF\) are similar, where side \(\overline{AB}\) corresponds to side \(\overline{DE}\). If \(AB = 6\), \(DE = 15\), and the area of triangle \(ABC\) is \(28\) square units, determine the area of triangle \(DEF\).</p>',
            r'What is the area, in square units, of triangle \(DEF\)?',
            ['175'],
            '175',
            r'Tỉ số độ dài cạnh tương ứng là \[k = \frac{DE}{AB} = \frac{15}{6} = \frac{5}{2}.\] Vì diện tích tỉ lệ với **bình phương** tỉ số đồng dạng (\(k^2\)), ta có \[\frac{\text{Area}(\triangle DEF)}{\text{Area}(\triangle ABC)} = k^2 = \left(\frac{5}{2}\right)^2 = \frac{25}{4}.\] Suy ra \[\text{Area}(\triangle DEF) = 28 \times \frac{25}{4} = 7 \times 25 = 175.\]',
            r'Bẫy kinh điển nhất của bài đồng dạng là nhân diện tích với \(k\) thay vì \(k^2\): luôn tự nhắc "Độ dài \(\to k\), Diện tích \(\to k^2\), Thể tích \(\to k^3\)".',
            desmos_tip_vi=r'Gõ trực tiếp <code>28 * (15 / 6)^2</code> trên Desmos để khóa chắc mũ \(2\) và nhận ngay <code>175</code>.'
        ),

        # Q9 — Medium-Hard, MCQ, Ans: B
        math_mcq(
            'sat_m4_1_q9', 9, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium-Hard',
            _wrap_svg(svg_altitude_split_triangle(left_hyp='25', right_hyp='26', alt_lbl='24', v_top='A', v_left='D', v_foot='B', v_right='C'))
            + r'<p>In triangle \(ACD\) shown, point \(B\) lies on side \(\overline{CD}\) such that \(\overline{AB} \perp \overline{CD}\). If \(AD = 25\), \(AC = 26\), and \(AB = 24\), find the area of triangle \(ACD\).</p>',
            r'What is the area of triangle \(ACD\)?',
            {'A': r'\(120\)', 'B': r'\(204\)', 'C': r'\(312\)', 'D': r'\(408\)'},
            'B',
            r'Đường cao \(\overline{AB} = 24\) tách \(\triangle ACD\) thành hai tam giác vuông với hai bộ ba Pytago kinh điển: \[\text{Trong }\triangle ABD:\; BD = \sqrt{25^2 - 24^2} = 7 \quad (\text{bộ } 7\text{–}24\text{–}25).\] \[\text{Trong }\triangle ABC:\; BC = \sqrt{26^2 - 24^2} = 10 \quad (\text{bộ } 5\text{–}12\text{–}13 \text{ nhân } 2).\] Tổng độ dài đáy \(CD = 7 + 10 = 17\). Diện tích tam giác \(ACD\) là \[\text{Area} = \frac{1}{2} \cdot CD \cdot AB = \frac{1}{2}(17)(24) = 204.\]',
            r'Khi một đường cao nằm bên trong tam giác cắt đáy thành hai phần, kiểm tra ngay các bộ ba Pytago \(7\text{–}24\text{–}25\) và \(10\text{–}24\text{–}26\) để cộng tổng đáy chỉ trong 5 giây.',
            {
                'A': ('Half-Triangle Area', r'\(120 = \frac{1}{2}(10)(24)\) mới chỉ là diện tích của riêng \(\triangle ABC\), bỏ sót \(\triangle ABD\).'),
                'B': ('Đáp án đúng', r'\(BD = 7\), \(BC = 10 \Rightarrow CD = 17\), suy ra \(\text{Area} = \frac{1}{2}(17)(24) = 204\).'),
                'C': ('Hypotenuse as Base', r'Dùng nhầm cạnh bên \(AC = 26\) làm đáy (\(\frac{1}{2} \cdot 26 \cdot 24 = 312\)).'),
                'D': ('Forgot 1/2', r'Tính \(17 \times 24 = 408\) mà quên chia đôi trong công thức diện tích tam giác.'),
            },
            desmos_tip_vi=r'Bấm 1 dòng trên Desmos: <code>0.5 * (sqrt(25^2 - 24^2) + sqrt(26^2 - 24^2)) * 24</code> ra ngay <code>204</code>.'
        ),

        # Q10 — Medium-Hard, MCQ, Ans: D
        math_mcq(
            'sat_m4_1_q10', 10, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium-Hard',
            _wrap_svg(svg_bent_parallel(ang_top='(2x + 10)°', ang_mid='115°', ang_bot='(3x − 5)°'))
            + r'<p>In the figure above, line \(\ell\) is parallel to line \(m\). Point \(P\) lies between lines \(\ell\) and \(m\) such that \(\angle APB = 115^\circ\). The acute angle formed by segment \(\overline{AP}\) and line \(\ell\) measures \((2x + 10)^\circ\), and the acute angle formed by segment \(\overline{PB}\) and line \(m\) measures \((3x - 5)^\circ\).</p>',
            r'What is the measure, in degrees, of the acute angle formed by segment \(\overline{PB}\) and line \(m\)?',
            {'A': r'\(22\)', 'B': r'\(54\)', 'C': r'\(57.5\)', 'D': r'\(61\)'},
            'D',
            r'Kẻ thêm một đường thẳng phụ \(n\) đi qua \(P\) và song song với \(\ell\) và \(m\). Đường thẳng \(n\) chia góc \(\angle APB = 115^\circ\) thành hai góc so le trong (alternate interior angles) lần lượt bằng \((2x + 10)^\circ\) và \((3x - 5)^\circ\): \[(2x + 10) + (3x - 5) = 115 \implies 5x + 5 = 115 \implies 5x = 110 \implies x = 22.\] Góc nhọn tạo bởi \(\overline{PB}\) và đường thẳng \(m\) là \[3(22) - 5 = 61^\circ.\]',
            r'Mẹo "Kẻ đường song song phụ" (Auxiliary Parallel Line): bất cứ khi nào thấy đường gấp khúc nằm giữa hai đường song song \(\ell \parallel m\), kẻ ngay đường song song qua đỉnh gấp khúc → góc gấp khúc bằng tổng hai góc so le trong.',
            {
                'A': ('Stopped Early', r'\(22\) chỉ là giá trị của \(x\), chưa thay vào biểu thức \(3x - 5\).'),
                'B': ('Wrong Angle', r'\(54^\circ = 2(22) + 10\) là góc tạo với đường thẳng \(\ell\), trong khi đề hỏi góc tại đường thẳng \(m\).'),
                'C': ('False Symmetry', r'Giả định sai rằng góc \(115^\circ\) bị chia đôi đều (\(115 / 2 = 57.5^\circ\)).'),
                'D': ('Đáp án đúng', r'Tổng hai góc nhọn bằng \(115^\circ \Rightarrow x = 22 \Rightarrow 3(22) - 5 = 61^\circ\).'),
            },
            desmos_tip_vi=r'Gõ <code>y = (2x + 10) + (3x - 5)</code> và <code>y = 115</code> trên Desmos để lấy \(x = 22\), sau đó tính ngay <code>3(22) - 5 = 61</code>.'
        ),

        # Q11 — Hard, MCQ, Ans: A
        math_mcq(
            'sat_m4_1_q11', 11, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Hard',
            _wrap_svg(svg_altitude_split_triangle(left_hyp='', right_hyp='10', alt_lbl='', v_top='B', v_left='A', v_foot='D', v_right='C', ang_left='30°', ang_right='45°'))
            + r'<p>In triangle \(ABC\) shown, altitude \(\overline{BD}\) is drawn to side \(\overline{AC}\) so that point \(D\) lies between \(A\) and \(C\). If \(\angle A = 30^\circ\), \(\angle C = 45^\circ\), and \(BC = 10\), what is the exact area of triangle \(ABC\)?</p>',
            r'Which of the following is the area of triangle \(ABC\)?',
            {'A': r'\(25 + 25\sqrt{3}\)', 'B': r'\(50 + 50\sqrt{3}\)', 'C': r'\(25\sqrt{2} + 25\sqrt{6}\)', 'D': r'\(50 + 25\sqrt{3}\)'},
            'A',
            r'Tách bài toán qua 2 tam giác vuông đặc biệt chung đường cao \(BD\):<br>1. Trong \(\triangle BDC\) (\(45^\circ\text{–}45^\circ\text{–}90^\circ\)): cạnh huyền \(BC = 10\), nên \[BD = DC = \frac{10}{\sqrt{2}} = 5\sqrt{2}.\] 2. Trong \(\triangle ABD\) (\(30^\circ\text{–}60^\circ\text{–}90^\circ\)): cạnh đối diện góc \(30^\circ\) là \(BD = 5\sqrt{2}\), suy ra cạnh kề góc \(30^\circ\) là \[AD = BD\sqrt{3} = 5\sqrt{2}\cdot\sqrt{3} = 5\sqrt{6}.\] 3. Tổng đáy \(AC = 5\sqrt{6} + 5\sqrt{2}\), suy ra diện tích \(\triangle ABC\): \[\text{Area} = \frac{1}{2} \cdot BD \cdot AC = \frac{1}{2}\left(5\sqrt{2}\right)\left(5\sqrt{6} + 5\sqrt{2}\right) = \frac{1}{2}\left(25\sqrt{12} + 50\right) = 25\sqrt{3} + 25.\]',
            r'Với tam giác ghép \(30^\circ\text{–}60^\circ\text{–}90^\circ\) và \(45^\circ\text{–}45^\circ\text{–}90^\circ\), luôn giải tam giác có cạnh đã biết trước để tìm đường cao chung \(h\), sau đó dùng \(\text{Area} = \frac{1}{2}h(h\sqrt{3} + h) = \frac{h^2(1+\sqrt{3})}{2}\).',
            {
                'A': ('Đáp án đúng', r'\(h = 5\sqrt{2} \Rightarrow h^2 = 50 \Rightarrow \text{Area} = \frac{50(1 + \sqrt{3})}{2} = 25 + 25\sqrt{3}\).'),
                'B': ('Forgot 1/2', r'Tính \(h(AD + DC) = 50 + 50\sqrt{3}\) nhưng quên nhân \(\frac{1}{2}\).'),
                'C': ('Radical Distribution Error', r'Quên nhân thừa số \(\sqrt{2}\) khi khai triển \(5\sqrt{2}(5\sqrt{6} + 5\sqrt{2})\).'),
                'D': ('Half-Area Error', r'Chỉ chia đôi hạng tử chứa \(\sqrt{3}\) mà quên chia đôi hạng tử \(50\).'),
            },
            desmos_tip_vi=r'Bật chế độ Degree hoặc dùng công thức \(\frac{1}{2}h^2(1+\sqrt{3})\) trên Desmos: gõ <code>h = 10/sqrt(2)</code> rồi <code>0.5 * h * (h*sqrt(3) + h)</code> ≈ <code>68.301</code>, khớp tuyệt đối với <code>25 + 25*sqrt(3)</code> ≈ <code>68.301</code>!'
        ),

        # Q12 — Hard, SPR (Ans: 150)
        math_spr(
            'sat_m4_1_q12', 12, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Hard',
            _wrap_svg(svg_right_altitude_hyp(pq='15', sr='16', v_left='P', v_top='Q', v_right='R', v_foot='S'))
            + r'<p>In right triangle \(PQR\) shown above, \(\angle PQR = 90^\circ\), and altitude \(\overline{QS}\) is drawn to hypotenuse \(\overline{PR}\). If \(PQ = 15\) and \(SR = 16\), determine the area of triangle \(PQR\).</p>',
            r'What is the area of triangle \(PQR\)?',
            ['150'],
            '150',
            r'Vì \(\overline{QS}\) là đường cao ứng với cạnh huyền \(\overline{PR}\), ta có \(\triangle PSQ \sim \triangle PQR\) (góc–góc). Đặt \(PS = x > 0\), khi đó \(PR = x + 16\). Theo hệ thức cạnh góc vuông trong tam giác vuông (Geometric Mean / Leg Rule): \[PQ^2 = PS \cdot PR \implies 15^2 = x(x + 16) \implies x^2 + 16x - 225 = 0.\] Phân tích nhân tử: \((x + 25)(x - 9) = 0 \implies x = 9\) (do \(x > 0\)). Khi đó cạnh huyền \(PR = 9 + 16 = 25\). Theo bộ ba \(3\text{–}4\text{–}5\) nhân \(5\), cạnh góc vuông còn lại là \(QR = 20\). Diện tích tam giác \(PQR\): \[\text{Area} = \frac{1}{2} \cdot PQ \cdot QR = \frac{1}{2}(15)(20) = 150.\]',
            r'Thuộc lòng bộ 3 công thức đường cao tam giác vuông (\(a^2 = c_1 c\), \(b^2 = c_2 c\), \(h^2 = c_1 c_2\)) biến câu Hard Module 2 thành một phương trình bậc hai giải trong 15 giây.',
            desmos_tip_vi=r'Gõ <code>y = x(x + 16)</code> và <code>y = 15^2</code> trên Desmos để lấy ngay nghiệm dương \(x = 9\) → \(PR = 25\), sau đó bấm <code>0.5 * 15 * sqrt(25^2 - 15^2) = 150</code>.'
        ),

        # Q13 — Hard, MCQ, Ans: C
        math_mcq(
            'sat_m4_1_q13', 13, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Hard',
            _wrap_svg(svg_nested_triangle(ad_lbl='4', db_lbl='6', de_lbl='', bc_lbl='', shaded_trap=True))
            + r'<p>In triangle \(ABC\) shown, segment \(\overline{DE}\) is parallel to segment \(\overline{BC}\), \(AD = 4\), and \(DB = 6\). The area of shaded quadrilateral \(DBCE\) is \(63\) square units.</p>',
            r'What is the area, in square units, of triangle \(ADE\)?',
            {'A': r'\(28\)', 'B': r'\(42\)', 'C': r'\(12\)', 'D': r'\(75\)'},
            'C',
            r'Vì \(\overline{DE} \parallel \overline{BC}\), ta có \(\triangle ADE \sim \triangle ABC\) với tỉ số đồng dạng \[k = \frac{AD}{AB} = \frac{4}{4 + 6} = \frac{4}{10} = \frac{2}{5}.\] Suy ra tỉ số diện tích của tam giác nhỏ và tam giác lớn là \[\frac{\text{Area}(\triangle ADE)}{\text{Area}(\triangle ABC)} = k^2 = \left(\frac{2}{5}\right)^2 = \frac{4}{25}.\] Đặt \(\text{Area}(\triangle ADE) = 4t\) và \(\text{Area}(\triangle ABC) = 25t\). Khi đó diện tích hình thang \(DBCE\) chiếm \(25t - 4t = 21t\): \[21t = 63 \implies t = 3 \implies \text{Area}(\triangle ADE) = 4(3) = 12.\]',
            r'Đừng bao giờ lập tỉ số đồng dạng giữa tam giác trên và hình thang dưới! Luôn đưa về tỉ số diện tích \(\triangle\text{nhỏ} : \triangle\text{lớn} = k^2\), rồi lấy phần bù \(1 - k^2\) cho hình thang.',
            {
                'A': ('Part-to-Part Squared Trap', r'Lấy nhầm \(\left(\frac{AD}{DB}\right)^2 = \left(\frac{4}{6}\right)^2 = \frac{4}{9}\) rồi nhân \(63 \times \frac{4}{9} = 28\) — coi hình thang \(DBCE\) như một tam giác đồng dạng.'),
                'B': ('Linear Ratio Trap', r'Dùng tỉ số độ dài \(\frac{4}{6} = \frac{2}{3}\) nhân \(63\) ra \(42\) — sai cả mô hình hình thang lẫn thiếu bình phương.'),
                'C': ('Đáp án đúng', r'Tỉ số diện tích \(\triangle ADE : \triangle ABC = 4 : 25\), nên hình thang \(DBCE\) ứng với \(21\) phần \(= 63 \Rightarrow 1\) phần \(= 3 \Rightarrow \text{Area}(\triangle ADE) = 12\).'),
                'D': ('Whole Triangle Trap', r'\(75 = 25 \times 3\) là diện tích toàn bộ \(\triangle ABC\), quên trừ \(63\) hoặc chưa nhân với \(4\) cho \(\triangle ADE\).'),
            },
            desmos_tip_vi=r'Gõ <code>k = 4 / (4 + 6)</code> rồi <code>63 * k^2 / (1 - k^2)</code> trên Desmos → ra thẳng kết quả <code>12</code> cực gọn.'
        ),

        # Q14 — Hard, MCQ, Ans: B
        math_mcq(
            'sat_m4_1_q14', 14, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Hard',
            _wrap_svg(svg_right_triangle(a_lbl='16', b_lbl='30', c_lbl='34', v_top='A', v_right_angle='B', v_right='C', note='M is midpoint of AC; MN ⊥ AC (N on BC)'))
            + r'<p>In right triangle \(ABC\), \(\angle B = 90^\circ\), \(AB = 16\), and \(BC = 30\). Point \(M\) is the midpoint of hypotenuse \(\overline{AC}\). A line perpendicular to \(\overline{AC}\) passes through \(M\) and intersects leg \(\overline{BC}\) at point \(N\).</p>',
            r'What is the length of segment \(MN\)?',
            {'A': r'\(8\)', 'B': r'\(\dfrac{136}{15}\)', 'C': r'\(\dfrac{255}{8}\)', 'D': r'\(\dfrac{289}{15}\)'},
            'B',
            r'Nhận diện bộ ba \(8\text{–}15\text{–}17\) nhân đôi: \(AB = 16, BC = 30 \implies AC = 34\). Vì \(M\) là trung điểm \(AC\), ta có \(CM = \frac{34}{2} = 17\). Xét hai tam giác vuông \(\triangle CMN\) (vuông tại \(M\)) và \(\triangle CBA\) (vuông tại \(B\)): chúng có chung góc nhọn \(C\), nên \(\triangle CMN \sim \triangle CBA\) (đỉnh tương ứng \(C \leftrightarrow C\), \(M \leftrightarrow B\), \(N \leftrightarrow A\)). Do đó: \[\frac{MN}{BA} = \frac{CM}{CB} \implies \frac{MN}{16} = \frac{17}{30} \implies MN = \frac{16 \times 17}{30} = \frac{136}{15}.\]',
            r'Khi đường trung trực cạnh huyền cắt một cạnh góc vuông, hai tam giác vuông luôn đồng dạng theo cặp đỉnh \(C\text{–}M\text{–}N \leftrightarrow C\text{–}B\text{–}A\) — cẩn thận đảo vị trí cạnh kề/đối của góc chung \(C\)!',
            {
                'A': ('Midsegment Illusion', r'Ngộ nhận rằng \(MN\) là đường trung bình song song với \(AB\) nên chọn \(\frac{16}{2} = 8\); thực tế \(MN \perp AC\), không vuông góc với \(BC\).'),
                'B': ('Đáp án đúng', r'\(CM = 17\) và \(\triangle CMN \sim \triangle CBA \Rightarrow MN = 16 \cdot \frac{17}{30} = \frac{136}{15}\).'),
                'C': ('Inverted Ratio', r'Lập ngược tỉ số \(\frac{MN}{30} = \frac{17}{16}\) (nhầm cạnh đối/kề của góc \(C\)) ra \(\frac{255}{8}\).'),
                'D': ('Wrong Segment', r'\(\frac{289}{15} = 34 \cdot \frac{17}{30}\) là độ dài cạnh huyền \(CN\) của \(\triangle CMN\), không phải đoạn \(MN\).'),
            },
            desmos_tip_vi=r'Trên Desmos, gõ <code>16 * (sqrt(16^2 + 30^2)/2) / 30</code> rồi nhấn nút phân số ở đầu dòng để chuyển thẳng sang \(\frac{136}{15}\).'
        ),

        # Q15 — Hard, SPR (Ans: 144)
        math_spr(
            'sat_m4_1_q15', 15, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Hard',
            _wrap_svg(svg_inscribed_square_rt())
            + r'<p>In right triangle \(ABC\) shown above, \(\angle B = 90^\circ\), \(AB = 21\), and hypotenuse \(AC = 35\). Square \(BDEF\) is inscribed in triangle \(ABC\) so that \(D\) lies on \(\overline{AB}\), \(F\) lies on \(\overline{BC}\), and \(E\) lies on hypotenuse \(\overline{AC}\).</p>',
            r'What is the area of square \(BDEF\)?',
            ['144'],
            '144',
            r'Bước 1: Dùng bộ ba \(3\text{–}4\text{–}5\) nhân \(7\) để tìm nhanh cạnh góc vuông còn lại: \[BC = \sqrt{35^2 - 21^2} = 7(4) = 28.\] Bước 2: Gọi cạnh hình vuông \(BDEF\) là \(s\). Vì \(\overline{DE} \parallel \overline{BC}\), ta có \(\triangle ADE \sim \triangle ABC\) với \(AD = 21 - s\) và \(DE = s\): \[\frac{21 - s}{21} = \frac{s}{28} \implies 28(21 - s) = 21s \implies 4(21 - s) = 3s \implies 84 = 7s \implies s = 12.\] Bước 3: Đề hỏi **diện tích** hình vuông \(BDEF\): \[\text{Area} = s^2 = 12^2 = 144.\]',
            r'Công thức thần tốc 800 Math: Hình vuông nội tiếp góc vuông của tam giác vuông có hai cạnh góc vuông \(a, b\) luôn có cạnh \(s = \frac{ab}{a + b}\) (\(\frac{21 \times 28}{21 + 28} = 12 \Rightarrow s^2 = 144\)).',
            desmos_tip_vi=r'Đặt hệ trục tại \(B(0,0)\), cạnh huyền \(AC\) đi qua \((0,21)\) và \((28,0)\) có phương trình <code>y = 21 - (21/28)x</code>. Giao với đường chéo hình vuông <code>y = x</code> trên Desmos cho ngay \((12, 12) \Rightarrow 12^2 = 144\)!'
        ),
    ]
    return build_math_drill_json(
        'Math Drill 4.1: Lines, Angles, Similarity & Special Right Triangles (15 câu)',
        'Module 4 • Geometry & Trigonometry • 11 MCQ + 4 SPR • Target 750–800',
        '750–800 • Geometry Core',
        qs,
        target_minutes=22,
    )


# ============================================================================
# DRILL 4.2: CIRCLES — COMPLETING THE SQUARE, ARCS, SECTORS & RADIANS (15 Qs)
# ============================================================================

def get_drill_m4_2():
    qs = [
        # Q1 — Medium, MCQ, Ans: C
        math_mcq(
            'sat_m4_2_q1', 1, 'Geometry and Trigonometry', 'Circles', 'Medium',
            r'<p>A circle in the \(xy\)-plane is defined by the equation \[(x + 5)^2 + (y - 3)^2 = 49.\]</p>',
            r'Which of the following gives the center and the diameter of this circle?',
            {
                'A': r'Center \((5, -3)\) and diameter \(14\)',
                'B': r'Center \((-5, 3)\) and diameter \(7\)',
                'C': r'Center \((-5, 3)\) and diameter \(14\)',
                'D': r'Center \((-5, 3)\) and diameter \(98\)',
            },
            'C',
            r'So sánh với phương trình chính tắc của đường tròn \((x - h)^2 + (y - k)^2 = r^2\): \[(x - (-5))^2 + (y - 3)^2 = 7^2.\] Do đó tâm đường tròn là \((h, k) = (-5, 3)\) và bán kính là \(r = \sqrt{49} = 7\). Đề hỏi **đường kính (diameter)**: \[d = 2r = 2(7) = 14.\]',
            r'Ba bẫy kinh điển ở phương trình đường tròn: (1) quên đảo dấu tâm \((h, k)\), (2) quên lấy căn vế phải \(r = \sqrt{r^2}\), và (3) đọc lướt chữ diameter thành radius.',
            {
                'A': ('Center Sign Flip', r'Quên đảo dấu trong \((x + 5)^2\) và \((y - 3)^2\) nên đọc nhầm tâm thành \((5, -3)\).'),
                'B': ('Radius vs Diameter', r'\(7\) là bán kính \(r\), trong khi câu hỏi yêu cầu đường kính \(d = 2r = 14\).'),
                'C': ('Đáp án đúng', r'Tâm \((-5, 3)\), bán kính \(r = \sqrt{49} = 7\), đường kính \(d = 2r = 14\).'),
                'D': ('Doubled r² Trap', r'Nhân đôi trực tiếp \(r^2 = 49\) thành \(98\) mà quên lấy căn bậc hai trước.'),
            },
            desmos_tip_vi=r'Gõ thẳng <code>(x + 5)^2 + (y - 3)^2 = 49</code> lên Desmos, chấm đỉnh trên \((-5, 10)\) và đáy dưới \((-5, -4)\) → thấy ngay tâm \((-5, 3)\) và đường kính \(10 - (-4) = 14\).'
        ),

        # Q2 — Medium, MCQ, Ans: A
        math_mcq(
            'sat_m4_2_q2', 2, 'Geometry and Trigonometry', 'Circles', 'Medium',
            _wrap_svg(svg_circle_sector(radius_lbl='12', angle_lbl='150°', center_lbl='O', pt_a='A', pt_b='B', note='Note: Figure not drawn to scale.'))
            + r'<p>In the circle above with center \(O\), the radius is \(12\) units and central angle \(\angle AOB\) measures \(150^\circ\).</p>',
            r'What is the length of minor arc \(AB\)?',
            {'A': r'\(10\pi\)', 'B': r'\(5\pi\)', 'C': r'\(20\pi\)', 'D': r'\(60\pi\)'},
            'A',
            r'Đổi góc ở tâm \(150^\circ\) sang radian: \[\theta = 150^\circ \times \frac{\pi}{180^\circ} = \frac{5\pi}{6}\text{ rad}.\] Áp dụng công thức độ dài cung \(s = r\theta\): \[s = 12 \times \frac{5\pi}{6} = 10\pi.\] (Cách tương đương: \(s = \frac{150^\circ}{360^\circ} \cdot 2\pi(12) = \frac{5}{12} \cdot 24\pi = 10\pi\).)',
            r'Độ dài cung là phần tỉ lệ của chu vi (\(s = r\theta = \frac{\text{độ}}{360^\circ}\cdot 2\pi r\)), còn diện tích hình quạt là phần tỉ lệ của diện tích hình tròn (\(A = \frac{1}{2}r^2\theta\)).',
            {
                'A': ('Đáp án đúng', r'\(\theta = \frac{5\pi}{6}\) và \(s = r\theta = 12 \cdot \frac{5\pi}{6} = 10\pi\).'),
                'B': ('Missing Factor of 2', r'Dùng nhầm chu vi bằng \(\pi r\) thay vì \(2\pi r\) nên tính ra \(\frac{150}{360}\cdot 12\pi = 5\pi\).'),
                'C': ('Doubled Radius', r'Thay đường kính \(24\) vào vị trí bán kính trong \(s = r\theta\) ra \(20\pi\).'),
                'D': ('Sector Area Trap', r'\(60\pi = \frac{1}{2}(12)^2\left(\frac{5\pi}{6}\right)\) là diện tích hình quạt \(AOB\), không phải độ dài cung \(AB\).'),
            },
            desmos_tip_vi=r'Gõ <code>(150 / 360) * 2 * 12</code> trên Desmos ra ngay hệ số <code>10</code> (tức \(10\pi\)) mà không cần gõ \(\pi\).'
        ),

        # Q3 — Medium, MCQ, Ans: D
        math_mcq(
            'sat_m4_2_q3', 3, 'Geometry and Trigonometry', 'Circles', 'Medium',
            r'<p>In the \(xy\)-plane, circle \(A\) has equation \[(x - 4)^2 + (y + 7)^2 = 36.\] Circle \(B\) is formed by translating circle \(A\) \(6\) units to the left and \(9\) units upward without changing its radius.</p>',
            r'Which of the following is an equation of circle \(B\)?',
            {
                'A': r'\((x - 10)^2 + (y + 16)^2 = 36\)',
                'B': r'\((x - 2)^2 + (y + 2)^2 = 36\)',
                'C': r'\((x + 2)^2 + (y - 2)^2 = 6\)',
                'D': r'\((x + 2)^2 + (y - 2)^2 = 36\)',
            },
            'D',
            r'Đọc tọa độ tâm của đường tròn \(A\): \((h_A, k_A) = (4, -7)\).<br>Khi tịnh tiến sang **trái \(6\) đơn vị** và **lên trên \(9\) đơn vị**, tọa độ tâm mới là: \[h_B = 4 - 6 = -2, \qquad k_B = -7 + 9 = 2.\] Bán kính không đổi nên \(r^2 = 36\). Thay tâm \((-2, 2)\) vào \((x - h)^2 + (y - k)^2 = r^2\): \[(x + 2)^2 + (y - 2)^2 = 36.\]',
            r'Khi tịnh tiến đường tròn, LUÔN tách tọa độ tâm \((h, k)\) ra dịch chuyển theo trục số (trái trừ, phải cộng, lên cộng, xuống trừ) rồi mới lắp lại vào phương trình để không bao giờ nhầm dấu.',
            {
                'A': ('Opposite Translation', r'Dịch nhầm sang phải \(6\) và xuống dưới \(9\), ra tâm \((10, -16)\).'),
                'B': ('Sign Inversion', r'Tìm đúng tâm \((-2, 2)\) nhưng lắp nhầm dấu thành \((x - 2)^2 + (y + 2)^2\).'),
                'C': ('Radius Squared Trap', r'Viết nhầm vế phải thành \(r = 6\) thay vì \(r^2 = 36\).'),
                'D': ('Đáp án đúng', r'Tâm mới \((4 - 6, -7 + 9) = (-2, 2)\) và \(r^2 = 36 \Rightarrow (x + 2)^2 + (y - 2)^2 = 36\).'),
            },
            desmos_tip_vi=r'Vẽ cả đường tròn gốc <code>(x - 4)^2 + (y + 7)^2 = 36</code> và phương trình đáp án <code>(x + 2)^2 + (y - 2)^2 = 36</code> trên Desmos để quan sát trực quan tâm dịch sang trái 6, lên 9.'
        ),

        # Q4 — Medium, SPR (Ans: 7)
        math_spr(
            'sat_m4_2_q4', 4, 'Geometry and Trigonometry', 'Circles', 'Medium',
            r'<p>In the \(xy\)-plane, the graph of the equation \[x^2 + y^2 - 10x + 14y + 25 = 0\] is a circle.</p>',
            r'What is the radius of the circle?',
            ['7'],
            '7',
            r'Nhóm các hạng tử theo \(x\) và \(y\), chuyển hằng số \(25\) sang vế phải, rồi hoàn thành bình phương (complete the square) bằng cách cộng \(\left(\frac{-10}{2}\right)^2 = 25\) và \(\left(\frac{14}{2}\right)^2 = 49\) vào cả hai vế: \[(x^2 - 10x + 25) + (y^2 + 14y + 49) = -25 + 25 + 49\] \[(x - 5)^2 + (y + 7)^2 = 49.\] Suy ra \(r^2 = 49 \implies r = 7\).',
            r'Với phương trình dạng \(x^2 + y^2 + Dx + Ey + F = 0\), công thức siêu tốc bán kính là \(r = \sqrt{\left(\frac{D}{2}\right)^2 + \left(\frac{E}{2}\right)^2 - F}\).',
            desmos_tip_vi=r'Gõ nguyên văn <code>x^2 + y^2 - 10x + 14y + 25 = 0</code> vào Desmos! Chấm điểm cực trị trên \((5, 0)\) và dưới \((5, -14)\) → đường kính \(= 14 \Rightarrow r = 7\) trong 5 giây.'
        ),

        # Q5 — Medium-Hard, MCQ, Ans: B
        math_mcq(
            'sat_m4_2_q5', 5, 'Geometry and Trigonometry', 'Circles', 'Medium-Hard',
            r'<p>A circle in the \(xy\)-plane has a diameter with endpoints at \((-3, 2)\) and \((5, 8)\).</p>',
            r'Which of the following points lies strictly inside the circle?',
            {'A': r'\((5, 2)\)', 'B': r'\((-2, 8)\)', 'C': r'\((6, 6)\)', 'D': r'\((1, 10)\)'},
            'B',
            r'Bước 1: Tâm đường tròn là trung điểm của đường kính: \[(h, k) = \left(\frac{-3 + 5}{2},\; \frac{2 + 8}{2}\right) = (1, 5).\] Bước 2: Bình phương bán kính từ tâm \((1, 5)\) đến đầu mút \((5, 8)\): \[r^2 = (5 - 1)^2 + (8 - 5)^2 = 4^2 + 3^2 = 25.\] Bước 3: Điểm \((x, y)\) nằm **bên trong** đường tròn khi và chỉ khi \((x - 1)^2 + (y - 5)^2 < 25\). Kiểm tra điểm \((-2, 8)\): \[(-2 - 1)^2 + (8 - 5)^2 = 9 + 9 = 18 < 25.\]',
            r'Vị trí tương đối của điểm \((x_0, y_0)\) với đường tròn \((x - h)^2 + (y - k)^2 = r^2\): nhỏ hơn \(r^2\) là nằm trong (inside), bằng \(r^2\) là nằm trên (on), lớn hơn \(r^2\) là nằm ngoài (outside).',
            {
                'A': ('On the Circle', r'\((5 - 1)^2 + (2 - 5)^2 = 16 + 9 = 25 = r^2\) — điểm nằm đúng TRÊN đường tròn, không nằm trong.'),
                'B': ('Đáp án đúng', r'\((-2 - 1)^2 + (8 - 5)^2 = 9 + 9 = 18 < 25\) — nằm hoàn toàn bên trong đường tròn.'),
                'C': ('Outside the Circle', r'\((6 - 1)^2 + (6 - 5)^2 = 25 + 1 = 26 > 25\) — điểm nằm NGOÀI đường tròn.'),
                'D': ('On the Circle', r'\((1 - 1)^2 + (10 - 5)^2 = 0 + 25 = 25 = r^2\) — đỉnh trên cùng nằm TRÊN đường tròn.'),
            },
            desmos_tip_vi=r'Vẽ đường tròn <code>(x - 1)^2 + (y - 5)^2 = 25</code> rồi gõ danh sách 4 điểm <code>(5,2), (-2,8), (6,6), (1,10)</code> trên Desmos — nhìn bằng mắt thường thấy ngay điểm duy nhất nằm lọt bên trong là \((-2, 8)\)!'
        ),

        # Q6 — Medium-Hard, MCQ, Ans: D
        math_mcq(
            'sat_m4_2_q6', 6, 'Geometry and Trigonometry', 'Circles', 'Medium-Hard',
            _wrap_svg(svg_inscribed_central(ins_lbl='(2x + 8)°', cen_lbl='(5x − 10)°'))
            + r'<p>In the circle shown with center \(O\), points \(A\), \(B\), and \(C\) lie on the circle. Inscribed angle \(\angle ACB\) measures \((2x + 8)^\circ\) and central angle \(\angle AOB\) measures \((5x - 10)^\circ\), both intercepting minor arc \(AB\).</p>',
            r'What is the measure, in degrees, of \(\angle OAB\)?',
            {'A': r'\(120\)', 'B': r'\(60\)', 'C': r'\(26\)', 'D': r'\(30\)'},
            'D',
            r'Bước 1: Vì góc ở tâm \(\angle AOB\) và góc nội tiếp \(\angle ACB\) cùng chắn cung nhỏ \(AB\), ta có \(\angle AOB = 2\,\angle ACB\): \[5x - 10 = 2(2x + 8) \implies 5x - 10 = 4x + 16 \implies x = 26.\] Bước 2: Tính góc ở tâm \(\angle AOB = 5(26) - 10 = 120^\circ\).<br>Bước 3: Do \(OA = OB = r\), tam giác \(\triangle OAB\) cân tại \(O\), suy ra hai góc ở đáy bằng nhau: \[\angle OAB = \frac{180^\circ - 120^\circ}{2} = 30^\circ.\]',
            r'Mọi tam giác tạo bởi tâm \(O\) và hai điểm \(A, B\) trên đường tròn đều là tam giác cân tại \(O\) (\(OA = OB = r\)) — công cụ vàng để suy ra góc đáy từ góc ở tâm.',
            {
                'A': ('Central Angle Trap', r'\(120^\circ\) là số đo góc ở tâm \(\angle AOB\), chưa tìm góc đáy \(\angle OAB\).'),
                'B': ('Inscribed Angle Trap', r'\(60^\circ\) là góc nội tiếp \(\angle ACB\), không phải \(\angle OAB\).'),
                'C': ('Stopped Early', r'\(26\) chỉ là giá trị ẩn \(x\).'),
                'D': ('Đáp án đúng', r'\(x = 26 \Rightarrow \angle AOB = 120^\circ\), tam giác cân \(\triangle OAB\) cho \(\angle OAB = \frac{180^\circ - 120^\circ}{2} = 30^\circ\).'),
            },
            desmos_tip_vi=r'Gõ <code>y = 5x - 10</code> và <code>y = 2(2x + 8)</code> trên Desmos để chốt giao điểm \((26, 120)\), sau đó gõ <code>(180 - 120) / 2 = 30</code>.'
        ),

        # Q7 — Medium-Hard, MCQ, Ans: B
        math_mcq(
            'sat_m4_2_q7', 7, 'Geometry and Trigonometry', 'Circles', 'Medium-Hard',
            _wrap_svg(svg_circle_sector(radius_lbl='9', angle_lbl='θ', center_lbl='O', pt_a='A', pt_b='B', note='Area of sector AOB = 27π'))
            + r'<p>In circle \(O\) shown above, the radius is \(9\) units and the area of shaded sector \(AOB\) is \(27\pi\) square units.</p>',
            r'What is the measure, in radians, of central angle \(\angle AOB\)?',
            {'A': r'\(\dfrac{\pi}{3}\)', 'B': r'\(\dfrac{2\pi}{3}\)', 'C': r'\(\dfrac{4\pi}{3}\)', 'D': r'\(3\pi\)'},
            'B',
            r'Áp dụng công thức diện tích hình quạt khi góc tính bằng radian: \[A = \frac{1}{2}r^2\theta.\] Thay \(A = 27\pi\) và \(r = 9\): \[27\pi = \frac{1}{2}(9^2)\theta = \frac{81}{2}\theta \implies \theta = \frac{54\pi}{81} = \frac{2\pi}{3}.\] (Kiểm tra nhanh bằng tỉ lệ: diện tích cả hình tròn là \(81\pi\), quạt chiếm \(\frac{27\pi}{81\pi} = \frac{1}{3}\) hình tròn, nên góc bằng \(\frac{1}{3}(2\pi) = \frac{2\pi}{3}\)).',
            r'Nhớ kỹ hệ số \(\frac{1}{2}\) trong công thức diện tích quạt \(A = \frac{1}{2}r^2\theta\), hoặc dùng tỉ lệ trực tiếp \(\frac{\theta}{2\pi} = \frac{A_{\text{quạt}}}{\pi r^2}\) để không bao giờ quên hệ số \(2\).',
            {
                'A': ('Forgot 1/2 Factor', r'Quên hệ số \(\frac{1}{2}\) khi giải \(81\theta = 27\pi \Rightarrow \theta = \frac{\pi}{3}\) (bẫy SAT siêu phổ biến!).'),
                'B': ('Đáp án đúng', r'\(\frac{1}{2}(81)\theta = 27\pi \Rightarrow \theta = \frac{54\pi}{81} = \frac{2\pi}{3}\).'),
                'C': ('Extra Factor of 2', r'Nhân nhầm thêm \(2\) lần thành \(\frac{4\pi}{3}\).'),
                'D': ('Arc Length Formula Trap', r'Chia nhầm \(27\pi\) cho \(r = 9\) theo công thức cung \(s = r\theta\) ra \(3\pi\) (còn lớn hơn cả một vòng tròn \(2\pi\)!).'),
            },
            desmos_tip_vi=r'Tính tỉ lệ trên Desmos: <code>(27 / 9^2) * 2</code> rồi bấm nút chuyển sang phân số → hiện ngay <code>2/3</code> (tức \(\frac{2\pi}{3}\)).'
        ),

        # Q8 — Medium-Hard, SPR (Ans: 14)
        math_spr(
            'sat_m4_2_q8', 8, 'Geometry and Trigonometry', 'Circles', 'Medium-Hard',
            r'<p>In the \(xy\)-plane, the equation \[2x^2 + 2y^2 - 12x + 20y - 30 = 0\] represents a circle.</p>',
            r'What is the diameter of the circle?',
            ['14'],
            '14',
            r'CẢNH GIÁC BẪY HỆ SỐ KHÁC \(1\): Trước khi hoàn thành bình phương, **BẮT BUỘC chia cả hai vế cho \(2\)** để hệ số của \(x^2\) và \(y^2\) bằng \(1\): \[x^2 + y^2 - 6x + 10y - 15 = 0.\] Hoàn thành bình phương: \[(x^2 - 6x + 9) + (y^2 + 10y + 25) = 15 + 9 + 25 = 49\] \[(x - 3)^2 + (y + 5)^2 = 49.\] Suy ra bán kính \(r = \sqrt{49} = 7\). Đề hỏi **đường kính (diameter)**: \[d = 2r = 14.\]',
            r'Gặp \(ax^2 + ay^2 + \dots = 0\) với \(a \neq 1\): Bước 0 luôn là chia toàn phương trình cho \(a\), sau đó kiểm tra kỹ đề hỏi \(r\), \(r^2\), hay đường kính \(2r\).',
            desmos_tip_vi=r'Gõ nguyên phương trình <code>2x^2 + 2y^2 - 12x + 20y - 30 = 0</code> vào Desmos! Chấm 2 điểm cực trái \((-4, -5)\) và cực phải \((10, -5)\) → đường kính \(= 10 - (-4) = 14\) ngay lập tức, miễn nhiễm 100% bẫy chia hệ số!'
        ),

        # Q9 — Medium-Hard, MCQ, Ans: C
        math_mcq(
            'sat_m4_2_q9', 9, 'Geometry and Trigonometry', 'Circles', 'Medium-Hard',
            _wrap_svg(svg_circle_tangent(pq_lbl='24', rq_lbl='16'))
            + r'<p>In the figure shown, segment \(\overline{PQ}\) is tangent to circle \(O\) at point \(P\), and segment \(\overline{OQ}\) intersects circle \(O\) at point \(R\). If \(PQ = 24\) and \(RQ = 16\), find the radius of circle \(O\).</p>',
            r'What is the radius of circle \(O\)?',
            {'A': r'\(8\)', 'B': r'\(20\)', 'C': r'\(10\)', 'D': r'\(26\)'},
            'C',
            r'Vì tiếp tuyến luôn vuông góc với bán kính tại tiếp điểm, ta có \(\overline{OP} \perp \overline{PQ}\) nên \(\triangle OPQ\) vuông tại \(P\). Gọi bán kính là \(r\); khi đó \(OP = OR = r\), suy ra cạnh huyền \(OQ = r + 16\). Áp dụng định lý Pytago cho \(\triangle OPQ\): \[r^2 + 24^2 = (r + 16)^2\] \[r^2 + 576 = r^2 + 32r + 256\] \[32r = 320 \implies r = 10.\] (Kiểm tra lại: \(10\text{–}24\text{–}26\) đúng bằng \(2 \times (5\text{–}12\text{–}13)\)!)',
            r'Mọi bài tiếp tuyến cắt cát tuyến qua tâm đều tạo tam giác vuông \(r^2 + t^2 = (r + d)^2\); hạng tử \(r^2\) ở hai vế luôn tự triệt tiêu thành phương trình bậc nhất cực gọn.',
            {
                'A': ('Subtraction Guess', r'Trừ đại \(24 - 16 = 8\), không áp dụng tính chất tiếp tuyến vuông góc bán kính.'),
                'B': ('Diameter Trap', r'\(20 = 2r\) là đường kính, hoặc tính sai từ việc quên khai triển \(2\cdot 16r\) trong \((r + 16)^2\).'),
                'C': ('Đáp án đúng', r'\(r^2 + 24^2 = (r + 16)^2 \Rightarrow 32r = 320 \Rightarrow r = 10\).'),
                'D': ('Hypotenuse Trap', r'\(26 = r + 16\) là độ dài toàn đoạn \(OQ\), không phải bán kính \(r\).'),
            },
            desmos_tip_vi=r'Gõ <code>y = x^2 + 24^2</code> và <code>y = (x + 16)^2</code> trên Desmos (hoặc <code>(24^2 - 16^2)/(2*16)</code>) để chốt ngay \(x = 10\).'
        ),

        # Q10 — Medium-Hard, MCQ, Ans: A
        math_mcq(
            'sat_m4_2_q10', 10, 'Geometry and Trigonometry', 'Circles', 'Medium-Hard',
            r'<p>In a circle with center \(O\), points \(A\) and \(B\) lie on the circle such that minor arc \(AB\) has length \(14\pi\) units and represents \(\dfrac{7}{24}\) of the circumference of the circle.</p>',
            r'What is the area, in square units, of sector \(AOB\)?',
            {'A': r'\(168\pi\)', 'B': r'\(336\pi\)', 'C': r'\(84\pi\)', 'D': r'\(576\pi\)'},
            'A',
            r'Bước 1: Tìm chu vi cả đường tròn \(C\): \[\frac{7}{24}C = 14\pi \implies C = 14\pi \cdot \frac{24}{7} = 48\pi.\] Bước 2: Tìm bán kính từ \(2\pi r = 48\pi \implies r = 24\).<br>Bước 3: Diện tích hình quạt \(AOB\) bằng \(\frac{7}{24}\) diện tích cả hình tròn (hoặc dùng công thức tắt \(A = \frac{1}{2}rs\)): \[A_{\text{sector}} = \frac{1}{2} \cdot r \cdot s = \frac{1}{2}(24)(14\pi) = 168\pi.\] (Kiểm tra theo tỉ lệ: \(\frac{7}{24}\cdot \pi(24^2) = 7 \cdot 24\pi = 168\pi\).)',
            r'Công thức thần tốc liên hệ cung và quạt: \(A_{\text{sector}} = \frac{1}{2} r s\) (giống hệt diện tích tam giác \(\frac{1}{2}\times\text{cao}\times\text{đáy}\)) — tiết kiệm 1 bước đổi góc trung gian!',
            {
                'A': ('Đáp án đúng', r'\(C = 48\pi \Rightarrow r = 24 \Rightarrow A_{\text{sector}} = \frac{1}{2}(24)(14\pi) = 168\pi\).'),
                'B': ('Forgot 1/2', r'Lấy \(r \cdot s = 24 \cdot 14\pi = 336\pi\), quên hệ số \(\frac{1}{2}\).'),
                'C': ('Half-Radius Error', r'Chia đôi thêm một lần thành \(84\pi\) do nhầm \(r = 12\).'),
                'D': ('Full Circle Area', r'\(576\pi = \pi(24^2)\) là diện tích cả hình tròn, quên nhân tỉ lệ \(\frac{7}{24}\).'),
            },
            desmos_tip_vi=r'Tính 2 dòng ngắn trên Desmos: <code>r = (14 * 24 / 7) / 2</code> ra <code>24</code>, rồi <code>0.5 * r * 14</code> ra hệ số <code>168</code> (tức \(168\pi\)).'
        ),

        # Q11 — Hard, MCQ, Ans: D
        math_mcq(
            'sat_m4_2_q11', 11, 'Geometry and Trigonometry', 'Circles', 'Hard',
            r'<p>In the \(xy\)-plane, the graph of \[3x^2 + 3y^2 - 18x + 24y + c = 0\] is a circle with an area of \(36\pi\) square units, where \(c\) is a constant.</p>',
            r'What is the value of \(c\)?',
            {'A': r'\(-11\)', 'B': r'\(33\)', 'C': r'\(-189\)', 'D': r'\(-33\)'},
            'D',
            r'Bước 1: Từ diện tích \(\pi r^2 = 36\pi\), suy ra \(r^2 = 36\).<br>Bước 2: Chia toàn bộ phương trình đường tròn cho hệ số đầu \(3\): \[x^2 + y^2 - 6x + 8y + \frac{c}{3} = 0.\] Bước 3: Hoàn thành bình phương: \[(x - 3)^2 + (y + 4)^2 = 3^2 + (-4)^2 - \frac{c}{3} = 25 - \frac{c}{3}.\] Bước 4: Đồng nhất vế phải với \(r^2 = 36\): \[25 - \frac{c}{3} = 36 \implies -\frac{c}{3} = 11 \implies c = -33.\]',
            r'Với phương trình \(ax^2 + ay^2 + Dx + Ey + c = 0\), chia tất cả (kể cả hằng số \(c\)) cho \(a\) trước khi hoàn thành bình phương — thiếu chia \(c\) cho \(a\) là bẫy sai hệ số phổ biến nhất ở Module 2 Hard.',
            {
                'A': ('Forgot to Multiply by 3', r'Giải \(25 - c = 36 \Rightarrow c = -11\) do quên chia hạng tử \(c\) cho \(3\) khi chia phương trình cho \(3\).'),
                'B': ('Sign Error', r'Chuyển vế sai dấu thành \(\frac{c}{3} - 25 = 36\) hoặc quên dấu trừ trước \(\frac{c}{3}\), ra \(+33\).'),
                'C': ('Skipped Dividing by 3', r'Không chia cho \(3\) mà hoàn thành bình phương trực tiếp với \(-18\) và \(24\): \(9^2 + 12^2 - 36 = 189\) rồi đổi dấu thành \(-189\).'),
                'D': ('Đáp án đúng', r'Chia cho \(3\) rồi hoàn thành bình phương: \(25 - \frac{c}{3} = 36 \Rightarrow c = -33\).'),
            },
            desmos_tip_vi=r'Gõ <code>3x^2 + 3y^2 - 18x + 24y + c = 0</code> vào Desmos và thêm thanh trượt <code>c</code>; thay thử <code>c = -33</code> → thấy đường tròn có tâm \((3, -4)\) và cực trên \((3, 2)\), cực dưới \((3, -10) \Rightarrow r = 6 \Rightarrow \text{Area} = 36\pi\)!'
        ),

        # Q12 — Hard, SPR (Ans: 27/4 or 6.75)
        math_spr(
            'sat_m4_2_q12', 12, 'Geometry and Trigonometry', 'Circles', 'Hard',
            r'<p>A circle in the \(xy\)-plane has center \((2, -1)\) and passes through the point \((5, 3)\). Line \(t\) is tangent to the circle at the point \((5, 3)\) and intersects the \(y\)-axis at the point \((0, b)\).</p>',
            r'What is the value of \(b\)?',
            ['27/4', '6.75'],
            '27/4 (hoặc 6.75)',
            r'Bước 1: Tính hệ số góc của bán kính nối từ tâm \((2, -1)\) tới tiếp điểm \((5, 3)\): \[m_{\text{radius}} = \frac{3 - (-1)}{5 - 2} = \frac{4}{3}.\] Bước 2: Vì tiếp tuyến \(t\) vuông góc với bán kính tại tiếp điểm, hệ số góc của \(t\) là nghịch đảo đối dấu: \[m_t = -\frac{3}{4}.\] Bước 3: Viết phương trình đường thẳng \(t\) đi qua \((5, 3)\): \[y - 3 = -\frac{3}{4}(x - 5).\] Thay \(x = 0\) để tìm tung độ giao điểm \(b\): \[b = 3 - \frac{3}{4}(-5) = 3 + \frac{15}{4} = \frac{27}{4} = 6.75.\]',
            r'Trong mặt phẳng tọa độ, "tiếp tuyến tại điểm \(P\)" tương đương với "đường thẳng đi qua \(P\) có hệ số góc \(m_t = -\frac{1}{m_{OP}}\)" — không cần viết phương trình đường tròn để giải!',
            desmos_tip_vi=r'Gõ đường tròn <code>(x - 2)^2 + (y + 1)^2 = 25</code> và đường thẳng <code>y - 3 = (-3/4)(x - 5)</code> trên Desmos → vừa xác nhận tiếp xúc hoàn hảo tại \((5, 3)\), vừa bấm thẳng vào giao điểm trục \(Oy\) thấy \((0, 6.75)\)!'
        ),

        # Q13 — Hard, MCQ, Ans: B
        math_mcq(
            'sat_m4_2_q13', 13, 'Geometry and Trigonometry', 'Circles', 'Hard',
            _wrap_svg(svg_circle_segment_120())
            + r'<p>In the circle shown with center \(O\), the radius is \(6\) units and central angle \(\angle AOB\) measures \(\dfrac{2\pi}{3}\) radians.</p>',
            r'What is the area, in square units, of the shaded region bounded by chord \(\overline{AB}\) and minor arc \(AB\)?',
            {
                'A': r'\(12\pi - 18\sqrt{3}\)',
                'B': r'\(12\pi - 9\sqrt{3}\)',
                'C': r'\(24\pi - 9\sqrt{3}\)',
                'D': r'\(12\pi - 9\)',
            },
            'B',
            r'Diện tích hình viên phân (shaded circular segment) bằng diện tích hình quạt trừ đi diện tích tam giác \(\triangle OAB\):<br>1. Diện tích hình quạt \(AOB\): \[A_{\text{sector}} = \frac{1}{2}r^2\theta = \frac{1}{2}(6^2)\left(\frac{2\pi}{3}\right) = 12\pi.\] 2. Diện tích \(\triangle OAB\) (cân tại \(O\), \(OA = OB = 6\), góc ở đỉnh \(\frac{2\pi}{3} = 120^\circ\)): Hạ đường cao từ \(O\) xuống \(AB\) chia \(\triangle OAB\) thành hai tam giác \(30^\circ\text{–}60^\circ\text{–}90^\circ\) có cạnh huyền \(6\), suy ra chiều cao \(h = 3\) và nửa đáy \(3\sqrt{3}\) (đáy \(AB = 6\sqrt{3}\)): \[A_{\triangle OAB} = \frac{1}{2}(6\sqrt{3})(3) = 9\sqrt{3}.\] 3. Vậy diện tích phần tô đậm là \[12\pi - 9\sqrt{3}.\]',
            r'Công thức diện tích phần viên phân (circular segment): \(A_{\text{segment}} = \frac{1}{2}r^2(\theta - \sin\theta)\) (với \(\theta\) tính bằng radian). Thay \(r = 6, \theta = \frac{2\pi}{3}\) ra ngay \(18\left(\frac{2\pi}{3} - \frac{\sqrt{3}}{2}\right) = 12\pi - 9\sqrt{3}\).',
            {
                'A': ('Forgot 1/2 in Triangle', r'Tính diện tích tam giác \(AB \cdot h = 18\sqrt{3}\) mà quên nhân \(\frac{1}{2}\).'),
                'B': ('Đáp án đúng', r'Quạt \(= 12\pi\), tam giác \(= 9\sqrt{3}\), suy ra phần tô đậm \(= 12\pi - 9\sqrt{3}\).'),
                'C': ('Forgot 1/2 in Sector', r'Dùng sai công thức quạt \(r^2\theta = 24\pi\) thay vì \(\frac{1}{2}r^2\theta = 12\pi\).'),
                'D': ('Dropped √3', r'Dùng nửa đáy sai bằng \(3\) thay vì \(3\sqrt{3}\), ra diện tích tam giác bằng \(9\).'),
            },
            desmos_tip_vi=r'Bật chế độ Radian trên Desmos rồi gõ <code>0.5 * 6^2 * (2*pi/3 - sin(2*pi/3))</code> ≈ <code>22.111</code>, đối chiếu với <code>12*pi - 9*sqrt(3)</code> ≈ <code>22.111</code> — khớp tuyệt đối!'
        ),

        # Q14 — Hard, MCQ, Ans: C
        math_mcq(
            'sat_m4_2_q14', 14, 'Geometry and Trigonometry', 'Circles', 'Hard',
            r'<p>A circle in the \(xy\)-plane lies entirely in the first quadrant, is tangent to both the positive \(x\)-axis and the positive \(y\)-axis, and passes through the point \((2, 1)\).</p>',
            r'What is the sum of all possible areas of such a circle?',
            {'A': r'\(6\pi\)', 'B': r'\(25\pi\)', 'C': r'\(26\pi\)', 'D': r'\(36\pi\)'},
            'C',
            r'Vì đường tròn nằm trong góc phần tư I và tiếp xúc với cả trục \(Ox\) lẫn trục \(Oy\), tâm của nó có dạng \((r, r)\) với bán kính \(r > 0\). Phương trình đường tròn là: \[(x - r)^2 + (y - r)^2 = r^2.\] Vì đường tròn đi qua điểm \((2, 1)\), thay \(x = 2, y = 1\): \[(2 - r)^2 + (1 - r)^2 = r^2\] \[(4 - 4r + r^2) + (1 - 2r + r^2) = r^2\] \[r^2 - 6r + 5 = 0 \implies (r - 1)(r - 5) = 0 \implies r = 1 \text{ hoặc } r = 5.\] Cả hai giá trị đều dương và tạo hai đường tròn thỏa mãn! Tổng diện tích của cả hai đường tròn khả dĩ là: \[\pi(1^2) + \pi(5^2) = \pi + 25\pi = 26\pi.\]',
            r'Đường tròn tiếp xúc cả 2 trục tọa độ ở góc phần tư I luôn có tâm \((r, r)\) và bán kính \(r\). Khi đề hỏi "sum of all possible...", luôn kiểm tra xem phương trình bậc hai có tới 2 nghiệm dương hay không!',
            {
                'A': ('Forgot to Square Radii', r'Cộng trực tiếp \((r_1 + r_2)\pi = (1 + 5)\pi = 6\pi\) thay vì cộng \((r_1^2 + r_2^2)\pi\).'),
                'B': ('Missed Smaller Circle', r'Chỉ tính đường tròn lớn \(r = 5\) (diện tích \(25\pi\)), bỏ sót nghiệm nhỏ \(r = 1\) vẫn đi qua \((2, 1)\) tại điểm cực phải của nó!'),
                'C': ('Đáp án đúng', r'Hai nghiệm \(r = 1\) và \(r = 5\) cho tổng diện tích \(\pi(1^2 + 5^2) = 26\pi\).'),
                'D': ('Squared the Sum', r'Tính nhầm \((r_1 + r_2)^2\pi = 6^2\pi = 36\pi\) thay vì \((r_1^2 + r_2^2)\pi\).'),
            },
            desmos_tip_vi=r'Gõ <code>y = (2 - x)^2 + (1 - x)^2 - x^2</code> trên Desmos để thấy ngay 2 giao điểm trục hoành \(x = 1\) và \(x = 5\), rồi tính <code>1^2 + 5^2 = 26</code> (tức \(26\pi\))!'
        ),

        # Q15 — Hard, SPR (Ans: 20)
        math_spr(
            'sat_m4_2_q15', 15, 'Geometry and Trigonometry', 'Circles', 'Hard',
            _wrap_svg(svg_two_tangents_circle())
            + r'<p>Points \(A\) and \(B\) lie on a circle with center \(O\) and radius \(15\). Tangent segments \(\overline{PA}\) and \(\overline{PB}\) meet at external point \(P\) such that \(OP = 30\). The length of <b>major arc</b> \(AB\) is \(k\pi\), where \(k\) is a constant.</p>',
            r'What is the value of \(k\)?',
            ['20'],
            '20',
            r'Bước 1: Vì \(\overline{PA}\) tiếp xúc với đường tròn tại \(A\), tam giác \(\triangle OAP\) vuông tại \(A\) với \(OA = 15\) và cạnh huyền \(OP = 30\).<br>Nhận diện ngay tam giác vuông đặc biệt \(30^\circ\text{–}60^\circ\text{–}90^\circ\) vì \(\cos(\angle AOP) = \frac{OA}{OP} = \frac{15}{30} = \frac{1}{2} \implies \angle AOP = 60^\circ\).<br>Bước 2: Tương tự \(\angle BOP = 60^\circ\), suy ra góc ở tâm chắn cung nhỏ \(AB\) là \(\angle AOB = 60^\circ + 60^\circ = 120^\circ\).<br>Bước 3: CẢNH GIÁC TỪ KHÓA **"major arc"** (cung lớn)! Góc ở tâm chắn cung lớn \(AB\) là \[360^\circ - 120^\circ = 240^\circ = \frac{4\pi}{3}\text{ rad}.\] Độ dài cung lớn \(AB\) là \[s_{\text{major}} = r\theta = 15 \cdot \frac{4\pi}{3} = 20\pi \implies k = 20.\]',
            r'Khi \(OP = 2r\), góc ở tâm giữa hai tiếp điểm luôn bằng \(120^\circ\) (cung nhỏ) và \(240^\circ\) (cung lớn). Luôn gạch chân từ "minor arc" hay "major arc" trước khi nhập đáp án SPR!',
            desmos_tip_vi=r'Chuyển Desmos sang Degree, tính <code>2 * arccos(15 / 30)</code> ra \(120^\circ\) (cung nhỏ), sau đó bấm <code>((360 - 120) / 360) * 2 * 15</code> để lấy thẳng \(k = 20\).'
        ),
    ]
    return build_math_drill_json(
        'Math Drill 4.2: Circles — Completing the Square, Arcs, Sectors & Radians (15 câu)',
        'Module 4 • Geometry & Trigonometry • 11 MCQ + 4 SPR • Target 750–800',
        '750–800 • Circles Mastery',
        qs,
        target_minutes=22,
    )


# ============================================================================
# DRILL 4.3: TRIGONOMETRY (SOH-CAH-TOA, COFUNCTIONS) & 3D SOLID SCALING (15 Qs)
# ============================================================================

def get_drill_m4_3():
    qs = [
        # Q1 — Medium, MCQ, Ans: A
        math_mcq(
            'sat_m4_3_q1', 1, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium',
            _wrap_svg(svg_right_triangle(a_lbl='8', b_lbl='15', c_lbl='17', v_top='A', v_right_angle='B', v_right='C'))
            + r'<p>In right triangle \(ABC\) shown above, \(\angle B = 90^\circ\), \(AB = 8\), \(BC = 15\), and \(AC = 17\).</p>',
            r'What is the value of \(\cos(A) + \sin(C)\)?',
            {'A': r'\(\dfrac{16}{17}\)', 'B': r'\(\dfrac{23}{17}\)', 'C': r'\(\dfrac{30}{17}\)', 'D': r'\(1\)'},
            'A',
            r'Trong tam giác vuông \(\triangle ABC\) (vuông tại \(B\)), hai góc nhọn \(A\) và \(C\) phụ nhau (\(A + C = 90^\circ\)), nên theo hệ thức đồng phụ (Cofunction Identity): \[\sin(C) = \cos(A).\] Áp dụng SOH-CAH-TOA cho góc \(A\) (cạnh kề \(AB = 8\), cạnh huyền \(AC = 17\)): \[\cos(A) = \frac{AB}{AC} = \frac{8}{17} \implies \sin(C) = \frac{AB}{AC} = \frac{8}{17}.\] Do đó: \[\cos(A) + \sin(C) = \frac{8}{17} + \frac{8}{17} = \frac{16}{17}.\]',
            r'Trong mọi tam giác vuông với hai góc nhọn \(A, C\): luôn nhớ \(\sin(A) = \cos(C)\) và \(\cos(A) = \sin(C)\) — hai tỉ số này đều dùng chung một cặp cạnh chia cho cạnh huyền.',
            {
                'A': ('Đáp án đúng', r'\(\cos(A) = \frac{8}{17}\) và \(\sin(C) = \frac{8}{17}\), cộng lại bằng \(\frac{16}{17}\).'),
                'B': ('Wrong Trig Ratio', r'Nhầm \(\sin(C)\) thành \(\cos(C) = \frac{15}{17}\) nên cộng \(\frac{8}{17} + \frac{15}{17} = \frac{23}{17}\).'),
                'C': ('Swapped Opp/Adj', r'Tính nhầm \(\sin(A) + \cos(C) = \frac{15}{17} + \frac{15}{17} = \frac{30}{17}\).'),
                'D': ('Identity Confusion', r'Nhầm \(\cos(A) + \sin(C) = 1\) theo hằng đẳng thức \(\sin^2 + \cos^2 = 1\).'),
            },
            desmos_tip_vi=r'Gõ <code>8/17 + 8/17</code> trên Desmos rồi bấm nút phân số ở bên trái để xác nhận ngay \(\frac{16}{17}\).'
        ),

        # Q2 — Medium, MCQ, Ans: D
        math_mcq(
            'sat_m4_3_q2', 2, 'Geometry and Trigonometry', 'Area and volume', 'Medium',
            _wrap_svg(svg_cylinder(r_lbl='5', h_lbl='12', note='Note: Figure not drawn to scale.'))
            + r'<p>A solid right circular cylinder has a base radius of \(5\) centimeters and a height of \(12\) centimeters.</p>',
            r'What is the total surface area, in square centimeters, of the cylinder?',
            {'A': r'\(120\pi\)', 'B': r'\(145\pi\)', 'C': r'\(300\pi\)', 'D': r'\(170\pi\)'},
            'D',
            r'Diện tích toàn phần (total surface area) của hình trụ gồm **2 mặt đáy hình tròn** cộng với **diện tích xung quanh (lateral area)**: \[\text{SA} = 2\pi r^2 + 2\pi r h.\] Thay \(r = 5\) và \(h = 12\): \[\text{SA} = 2\pi(5^2) + 2\pi(5)(12) = 50\pi + 120\pi = 170\pi.\]',
            r'Reference Sheet của Digital SAT chỉ cho công thức THỂ TÍCH hình trụ (\(V = \pi r^2 h\)), KHÔNG cho công thức diện tích toàn phần! Bạn bắt buộc phải thuộc \(\text{SA}_{\text{cylinder}} = 2\pi r^2 + 2\pi r h\).',
            {
                'A': ('Lateral Area Only', r'\(120\pi = 2\pi rh\) mới là diện tích xung quanh, bỏ quên cả hai mặt đáy tròn \(2\pi r^2\).'),
                'B': ('Single Base Trap', r'\(145\pi = \pi r^2 + 2\pi rh\) chỉ cộng đúng một mặt đáy (hình trụ không nắp).'),
                'C': ('Volume Instead of SA', r'\(300\pi = \pi r^2 h\) là thể tích của hình trụ, không phải diện tích toàn phần.'),
                'D': ('Đáp án đúng', r'\(2\pi(25) + 2\pi(5)(12) = 50\pi + 120\pi = 170\pi\).'),
            },
            desmos_tip_vi=r'Gõ trực tiếp phần hệ số <code>2*5^2 + 2*5*12</code> trên Desmos để chốt nhanh <code>170</code> (tức \(170\pi\)).'
        ),

        # Q3 — Medium, MCQ, Ans: B
        math_mcq(
            'sat_m4_3_q3', 3, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium',
            r'<p>In the equation below, both \((3x - 14)^\circ\) and \((2x + 19)^\circ\) are the measures of acute angles: \[\sin\left((3x - 14)^\circ\right) = \cos\left((2x + 19)^\circ\right).\]</p>',
            r'What is the value of \(x\)?',
            {'A': r'\(33\)', 'B': r'\(17\)', 'C': r'\(35\)', 'D': r'\(37\)'},
            'B',
            r'Với hai góc nhọn \(\alpha, \beta\), đẳng thức \(\sin(\alpha) = \cos(\beta)\) xảy ra khi và chỉ khi hai góc phụ nhau (\(\alpha + \beta = 90^\circ\)): \[(3x - 14) + (2x + 19) = 90\] \[5x + 5 = 90 \implies 5x = 85 \implies x = 17.\] Kiểm tra nhanh: \(3(17) - 14 = 37^\circ\) và \(2(17) + 19 = 53^\circ\), đúng là hai góc nhọn phụ nhau (\(37^\circ + 53^\circ = 90^\circ\)).',
            r'Thấy \(\sin(\text{góc } 1) = \cos(\text{góc } 2)\) với góc nhọn trên Digital SAT → lập tức cộng hai góc cho bằng \(90^\circ\) (hoặc \(\frac{\pi}{2}\) nếu dùng radian)!',
            {
                'A': ('Set Angles Equal', r'Cho nhầm hai góc bằng nhau: \(3x - 14 = 2x + 19 \Rightarrow x = 33\) (chỉ đúng khi cả hai vế cùng là \(\sin\) hoặc cùng là \(\cos\)).'),
                'B': ('Đáp án đúng', r'\((3x - 14) + (2x + 19) = 90 \Rightarrow 5x = 85 \Rightarrow x = 17\).'),
                'C': ('Supplementary Trap', r'Cho tổng hai góc bằng \(180^\circ\) thay vì \(90^\circ\): \(5x + 5 = 180 \Rightarrow x = 35\).'),
                'D': ('Angle Instead of x', r'\(37^\circ = 3(17) - 14\) là số đo góc thứ nhất, không phải giá trị của \(x\).'),
            },
            desmos_tip_vi=r'Bật chế độ Degree (biểu tượng cờ lê ⚙️) trên Desmos, vẽ <code>y = sin(3x - 14)</code> và <code>y = cos(2x + 19)</code> trong vùng \(0 < x < 30\) → bấm giao điểm thấy ngay \(x = 17\)!'
        ),

        # Q4 — Medium, SPR (Ans: 96)
        math_spr(
            'sat_m4_3_q4', 4, 'Geometry and Trigonometry', 'Area and volume', 'Medium',
            _wrap_svg(svg_cone(r_lbl='6', l_lbl='10'))
            + r'<p>A right circular cone has a base radius of \(6\) units and a slant height of \(10\) units. The volume of the cone is \(k\pi\) cubic units, where \(k\) is a constant.</p>',
            r'What is the value of \(k\)?',
            ['96'],
            '96',
            r'CẢNH GIÁC BẪY ĐƯỜNG SINH (slant height): Công thức thể tích hình nón \(V = \frac{1}{3}\pi r^2 h\) dùng **chiều cao thẳng đứng \(h\)**, không phải đường sinh \(l = 10\)! Áp dụng định lý Pytago với bộ ba \(6\text{–}8\text{–}10\): \[h = \sqrt{l^2 - r^2} = \sqrt{10^2 - 6^2} = \sqrt{64} = 8.\] Thay vào công thức thể tích hình nón: \[V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi(6^2)(8) = 12 \cdot 8\pi = 96\pi \implies k = 96.\]',
            r'Luôn phân biệt **slant height (\(l\))** (cạnh huyền) và **vertical height (\(h\))** (cạnh góc vuông) trong hình nón và hình chóp đều: \(h = \sqrt{l^2 - r^2}\).',
            desmos_tip_vi=r'Gõ <code>(1/3) * 6^2 * sqrt(10^2 - 6^2)</code> trên Desmos để ra ngay <code>96</code> (hệ số trước \(\pi\)).'
        ),

        # Q5 — Medium-Hard, MCQ, Ans: C
        math_mcq(
            'sat_m4_3_q5', 5, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium-Hard',
            _wrap_svg(svg_similar_right_triangles())
            + r'<p>Right triangles \(ABC\) and \(DEF\) are similar, where \(\angle B = \angle E = 90^\circ\) and vertices \(A\), \(B\), and \(C\) correspond to vertices \(D\), \(E\), and \(F\), respectively. Each side of triangle \(DEF\) is \(4\) times the length of the corresponding side of triangle \(ABC\). If \(\sin(A) = \dfrac{7}{25}\), what is the value of \(\tan(F)\)?</p>',
            r'What is the value of \(\tan(F)\)?',
            {'A': r'\(\dfrac{7}{24}\)', 'B': r'\(\dfrac{28}{25}\)', 'C': r'\(\dfrac{24}{7}\)', 'D': r'\(\dfrac{96}{7}\)'},
            'C',
            r'Bước 1 (Tính bất biến tỉ số lượng giác): Khi phóng đại tam giác lên \(4\) lần, **tất cả các góc tương ứng giữ nguyên**, nên mọi tỉ số lượng giác KHÔNG thay đổi theo hệ số phóng đại \(4\)! Do đó \(\sin(D) = \sin(A) = \frac{7}{25}\).<br>Bước 2: Trong tam giác vuông \(\triangle DEF\) (vuông tại \(E\)), đặt cạnh đối góc \(D\) là \(EF = 7\) và cạnh huyền \(DF = 25\). Theo bộ ba \(7\text{–}24\text{–}25\), cạnh còn lại là \(DE = 24\).<br>Bước 3: Xét góc \(F\): cạnh đối góc \(F\) là \(DE = 24\) và cạnh kề góc \(F\) là \(EF = 7\), suy ra: \[\tan(F) = \frac{DE}{EF} = \frac{24}{7}.\]',
            r'Tỉ số lượng giác (\(\sin, \cos, \tan\)) hoàn toàn **bất biến dưới phép đồng dạng**! Đừng bao giờ nhân \(\sin, \cos, \tan\) với hệ số tỉ lệ \(k\) mà đề cố tình cài vào làm mồi nhử.',
            {
                'A': ('Wrong Acute Angle', r'\(\frac{7}{24}\) là \(\tan(D)\), ngược góc nhọn vì đề hỏi \(\tan(F)\).'),
                'B': ('Scaled Trig Trap', r'Nhân nhầm \(\sin(A) = \frac{7}{25}\) với hệ số phóng đại \(4\) ra \(\frac{28}{25}\) — tỉ số \(\sin\) thậm chí không bao giờ vượt quá \(1\)!'),
                'C': ('Đáp án đúng', r'Tỉ số lượng giác bất biến theo đồng dạng; bộ ba \(7\text{–}24\text{–}25\) cho \(\tan(F) = \frac{\text{đối } F}{\text{kề } F} = \frac{24}{7}\).'),
                'D': ('Scaled Tan Trap', r'Tính đúng \(\tan(F) = \frac{24}{7}\) rồi lại nhân thêm hệ số phóng đại \(4\) thành \(\frac{96}{7}\).'),
            },
            desmos_tip_vi=r'Đặt trực tiếp tam giác tỉ lệ gốc trên Desmos: <code>sqrt(25^2 - 7^2) / 7</code> rồi nhấn nút phân số → chốt ngay \(\frac{24}{7}\), bỏ qua hoàn toàn con số gây nhiễu \(4\).'
        ),

        # Q6 — Medium-Hard, MCQ, Ans: A
        math_mcq(
            'sat_m4_3_q6', 6, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium-Hard',
            r'<p>Consider the trigonometric expression \[4\cos\left(\frac{\pi}{3}\right) + 6\sin\left(\frac{5\pi}{6}\right) - 2\cos\left(\frac{2\pi}{3}\right).\]</p>',
            r'What is the exact value of the expression?',
            {'A': r'\(6\)', 'B': r'\(4\)', 'C': r'\(0\)', 'D': r'\(5\sqrt{3} + 1\)'},
            'A',
            r'Tính từng giá trị lượng giác đặc biệt theo đường tròn đơn vị (nhớ quy tắc dấu ở Góc phần tư II: \(\sin > 0\), \(\cos < 0\)):<br>• \(\frac{\pi}{3} = 60^\circ\) (Góc phần tư I): \(\cos\left(\frac{\pi}{3}\right) = \frac{1}{2}\).<br>• \(\frac{5\pi}{6} = 150^\circ\) (Góc phần tư II, góc tham chiếu \(30^\circ\)): \(\sin\left(\frac{5\pi}{6}\right) = +\sin\left(\frac{\pi}{6}\right) = \frac{1}{2}\).<br>• \(\frac{2\pi}{3} = 120^\circ\) (Góc phần tư II, góc tham chiếu \(60^\circ\)): \(\cos\left(\frac{2\pi}{3}\right) = -\cos\left(\frac{\pi}{3}\right) = -\frac{1}{2}\).<br>Thay vào biểu thức: \[4\left(\frac{1}{2}\right) + 6\left(\frac{1}{2}\right) - 2\left(-\frac{1}{2}\right) = 2 + 3 + 1 = 6.\]',
            r'Nhớ thần chú ASTC (All–Sin–Tan–Cos): ở góc phần tư II (\(\frac{\pi}{2} < \theta < \pi\)), chỉ có \(\sin\) dương, còn \(\cos\) luôn ÂM — mất dấu trừ ở \(\cos\left(\frac{2\pi}{3}\right)\) là sai ngay.',
            {
                'A': ('Đáp án đúng', r'\(4(\frac{1}{2}) + 6(\frac{1}{2}) - 2(-\frac{1}{2}) = 2 + 3 + 1 = 6\).'),
                'B': ('Quadrant II Cos Sign', r'Quên dấu âm của \(\cos\left(\frac{2\pi}{3}\right) = -\frac{1}{2}\), thay nhầm thành \(+\frac{1}{2}\) nên ra \(2 + 3 - 1 = 4\).'),
                'C': ('Quadrant II Sin Sign', r'Gán nhầm dấu âm cho \(\sin\left(\frac{5\pi}{6}\right) = -\frac{1}{2}\), tính thành \(2 - 3 + 1 = 0\).'),
                'D': ('Swapped Sin & Cos', r'Nhầm \(\cos(\frac{\pi}{3})\) và \(\sin(\frac{5\pi}{6})\) bằng \(\frac{\sqrt{3}}{2}\) nên ra \(5\sqrt{3} + 1\).'),
            },
            desmos_tip_vi=r'Để chế độ Radian mặc định trên Desmos và gõ nguyên văn <code>4cos(pi/3) + 6sin(5pi/6) - 2cos(2pi/3)</code> → Desmos in thẳng đáp án <code>6</code> trong 4 giây!'
        ),

        # Q7 — Medium-Hard, MCQ, Ans: D
        math_mcq(
            'sat_m4_3_q7', 7, 'Geometry and Trigonometry', 'Area and volume', 'Medium-Hard',
            r'<p>Sphere \(A\) has a surface area of \(36\pi\) square centimeters. Sphere \(B\) has a volume that is \(27\) times the volume of sphere \(A\).</p>',
            r'What is the surface area, in square centimeters, of sphere \(B\)?',
            {'A': r'\(108\pi\)', 'B': r'\(972\pi\)', 'C': r'\(216\pi\)', 'D': r'\(324\pi\)'},
            'D',
            r'Mọi hình cầu đều đồng dạng với nhau! Áp dụng định luật tỉ lệ 3D (\(k \to k^2 \to k^3\)):<br>1. Tỉ số thể tích bằng lập phương tỉ số bán kính: \[\frac{V_B}{V_A} = k^3 = 27 \implies k = \sqrt[3]{27} = 3.\] 2. Tỉ số diện tích bề mặt bằng bình phương tỉ số bán kính: \[\frac{\text{SA}_B}{\text{SA}_A} = k^2 = 3^2 = 9.\] 3. Suy ra diện tích bề mặt hình cầu \(B\) là: \[\text{SA}_B = 36\pi \times 9 = 324\pi.\] (Kiểm chứng trực tiếp: \(4\pi r_A^2 = 36\pi \Rightarrow r_A = 3 \Rightarrow r_B = 9 \Rightarrow \text{SA}_B = 4\pi(9^2) = 324\pi\).)',
            r'Khi chuyển từ tỉ số THỂ TÍCH sang tỉ số DIỆN TÍCH (hoặc ngược lại) giữa 2 khối đồng dạng, luôn đi qua cầu nối tỉ số tuyến tính \(k\): \(V \xrightarrow{\sqrt[3]{\cdot}} k \xrightarrow{(\cdot)^2} \text{SA}\).',
            {
                'A': ('Linear Scale Trap', r'Chỉ nhân diện tích với \(k = 3\) (\(36\pi \times 3 = 108\pi\)) mà quên bình phương thành \(k^2 = 9\).'),
                'B': ('Volume Ratio Trap', r'Nhân thẳng diện tích với tỉ số thể tích \(27\) (\(36\pi \times 27 = 972\pi\)).'),
                'C': ('Multiplier Error', r'Nhân nhầm với \(2k = 6\) thay vì \(k^2 = 9\), ra \(216\pi\).'),
                'D': ('Đáp án đúng', r'\(k^3 = 27 \Rightarrow k = 3 \Rightarrow k^2 = 9 \Rightarrow \text{SA}_B = 36\pi \cdot 9 = 324\pi\).'),
            },
            desmos_tip_vi=r'Gõ <code>36 * (27^(1/3))^2</code> trên Desmos để chốt ngay hệ số <code>324</code> (tức \(324\pi\)) mà không cần tìm bán kính \(r_A\)!'
        ),

        # Q8 — Medium-Hard, SPR (Ans: 384)
        math_spr(
            'sat_m4_3_q8', 8, 'Geometry and Trigonometry', 'Area and volume', 'Medium-Hard',
            _wrap_svg(svg_square_pyramid(b_lbl='12', l_lbl='10'))
            + r'<p>A right square pyramid has a square base with side length \(12\) inches and a slant height of \(10\) inches (measured from the apex perpendicular to an edge of the base).</p>',
            r'What is the volume, in cubic inches, of the pyramid?',
            ['384'],
            '384',
            r'Bước 1: Chiều cao \(h\) của hình chóp vuông tạo với nửa cạnh đáy (\(\frac{12}{2} = 6\)) và trung đoạn / đường cao mặt bên (slant height \(l = 10\)) một tam giác vuông: \[h = \sqrt{10^2 - 6^2} = \sqrt{64} = 8\text{ inches}.\] Bước 2: Diện tích đáy vuông là \(B = 12^2 = 144\text{ in}^2\).<br>Bước 3: Áp dụng công thức thể tích hình chóp \(V = \frac{1}{3}Bh\): \[V = \frac{1}{3}(144)(8) = 48 \times 8 = 384.\]',
            r'Trong hình chóp tứ giác đều (right square pyramid), tam giác vuông tạo bởi đường cao \(h\) và đường cao mặt bên \(l\) có cạnh đáy bằng **một nửa cạnh đáy hình vuông** (\(\frac{s}{2}\)), không phải cả cạnh \(s\)!',
            desmos_tip_vi=r'Gõ 1 dòng trên Desmos: <code>(1/3) * 12^2 * sqrt(10^2 - (12/2)^2)</code> ra ngay <code>384</code>.'
        ),

        # Q9 — Medium-Hard, MCQ, Ans: B
        math_mcq(
            'sat_m4_3_q9', 9, 'Geometry and Trigonometry', 'Area and volume', 'Medium-Hard',
            r'<p>Rectangular prism \(P\) has dimensions \(3\text{ cm}\) by \(4\text{ cm}\) by \(12\text{ cm}\). Rectangular prism \(Q\) is similar to prism \(P\), and the longest interior diagonal (space diagonal) of prism \(Q\) has length \(39\text{ cm}\).</p>',
            r'What is the volume, in cubic centimeters, of rectangular prism \(Q\)?',
            {'A': r'\(432\)', 'B': r'\(3{,}888\)', 'C': r'\(1{,}296\)', 'D': r'\(1{,}728\)'},
            'B',
            r'Bước 1: Tính đường chéo không gian (space diagonal) của hình hộp chữ nhật \(P\) bằng định lý Pytago 3D: \[d_P = \sqrt{3^2 + 4^2 + 12^2} = \sqrt{9 + 16 + 144} = \sqrt{169} = 13\text{ cm}.\] Bước 2: Vì hai hình hộp đồng dạng, tỉ số tuyến tính \(k\) bằng tỉ số đường chéo tương ứng: \[k = \frac{d_Q}{d_P} = \frac{39}{13} = 3.\] Bước 3: Thể tích hình hộp \(P\) là \(V_P = 3 \times 4 \times 12 = 144\text{ cm}^3\). Thể tích tỉ lệ với \(k^3\): \[V_Q = V_P \cdot k^3 = 144 \times 3^3 = 144 \times 27 = 3{,}888\text{ cm}^3.\]',
            r'Bộ tứ Pytago 3D kinh điển \(3\text{–}4\text{–}12 \to d = 13\) (\(d = \sqrt{l^2 + w^2 + h^2}\)) rất hay xuất hiện ở SAT; và luôn nhớ mọi đường chéo đều là đại lượng tuyến tính bậc 1 (\(k\)), nên thể tích nhân với \(k^3\).',
            {
                'A': ('Linear Scaling Trap', r'Nhân thể tích với \(k = 3\) (\(144 \times 3 = 432\)) thay vì \(k^3 = 27\).'),
                'B': ('Đáp án đúng', r'\(d_P = 13 \Rightarrow k = \frac{39}{13} = 3 \Rightarrow V_Q = (3 \cdot 4 \cdot 12) \cdot 3^3 = 3{,}888\).'),
                'C': ('Area Scaling Trap', r'Nhân thể tích với \(k^2 = 9\) (\(144 \times 9 = 1{,}296\)) — nhầm sang quy tắc diện tích.'),
                'D': ('Dimension Confusion', r'Tính \(12^3 = 1{,}728\), nhầm sang thể tích hình lập phương cạnh \(12\).'),
            },
            desmos_tip_vi=r'Gõ <code>(3 * 4 * 12) * (39 / sqrt(3^2 + 4^2 + 12^2))^3</code> trên Desmos → hiện ngay <code>3888</code>.'
        ),

        # Q10 — Medium-Hard, MCQ, Ans: C
        math_mcq(
            'sat_m4_3_q10', 10, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium-Hard',
            _wrap_svg(svg_right_triangle(a_lbl='8', b_lbl='15', c_lbl='?', v_top='X', v_right_angle='Y', v_right='Z', note='Representative ratio diagram'))
            + r'<p>In right triangle \(XYZ\), \(\angle Y = 90^\circ\) and \(\tan(X) = \dfrac{15}{8}\).</p>',
            r'What is the value of \(\cos(X) - \cos(Z)\)?',
            {'A': r'\(\dfrac{7}{17}\)', 'B': r'\(\dfrac{23}{17}\)', 'C': r'\(-\dfrac{7}{17}\)', 'D': r'\(-\dfrac{7}{15}\)'},
            'C',
            r'Vì \(\tan(X) = \frac{\text{đối } X}{\text{kề } X} = \frac{YZ}{XY} = \frac{15}{8}\), ta chọn trực tiếp \(YZ = 15\) và \(XY = 8\). Theo bộ ba Pytago \(8\text{–}15\text{–}17\), cạnh huyền \(XZ = 17\).<br>Tính hai giá trị \(\cos\): \[\cos(X) = \frac{XY}{XZ} = \frac{8}{17}, \qquad \cos(Z) = \frac{YZ}{XZ} = \frac{15}{17}.\] Trừ đúng thứ tự đề bài yêu cầu: \[\cos(X) - \cos(Z) = \frac{8}{17} - \frac{15}{17} = -\frac{7}{17}.\]',
            r'Khi trừ hai tỉ số lượng giác (\(\cos X - \cos Z\)), luôn kiểm tra dấu âm/dương cẩn thận: góc có \(\tan > 1\) lớn hơn \(45^\circ\), nên \(\cos X < \sin X = \cos Z \implies \cos X - \cos Z < 0\)!',
            {
                'A': ('Sign Reversal', r'Đảo ngược phép trừ thành \(\frac{15}{17} - \frac{8}{17} = +\frac{7}{17}\), sai dấu!'),
                'B': ('Added Instead of Subtracted', r'Cộng nhầm thành \(\frac{8}{17} + \frac{15}{17} = \frac{23}{17}\).'),
                'C': ('Đáp án đúng', r'\(\cos(X) = \frac{8}{17}\), \(\cos(Z) = \frac{15}{17}\), hiệu bằng \(\frac{8 - 15}{17} = -\frac{7}{17}\).'),
                'D': ('Hypotenuse Error', r'Dùng mẫu số là \(15\) (cạnh góc vuông) thay vì cạnh huyền \(17\).'),
            },
            desmos_tip_vi=r'Gõ <code>8/17 - 15/17</code> trên Desmos rồi bấm biểu tượng phân số để khóa chắc dấu âm \(-\frac{7}{17}\).'
        ),

        # Q11 — Hard, MCQ, Ans: B
        math_mcq(
            'sat_m4_3_q11', 11, 'Geometry and Trigonometry', 'Area and volume', 'Hard',
            _wrap_svg(svg_cone_in_cylinder(r_lbl='6', h_lbl='8'))
            + r'<p>A solid right circular cylinder has base radius \(6\text{ cm}\) and height \(8\text{ cm}\). A right circular cone with the same base radius \(6\text{ cm}\) and height \(8\text{ cm}\) is hollowed out from the top face of the cylinder, as shown in the figure.</p>',
            r'What is the total surface area, in square centimeters, of the resulting hollow solid?',
            {'A': r'\(156\pi\)', 'B': r'\(192\pi\)', 'C': r'\(228\pi\)', 'D': r'\(108\pi\)'},
            'B',
            r'CẢNH GIÁC BẪY MODULE 2 HARD: Khi khoét rỗng hình nón khỏi khối trụ, **thể tích giảm đi nhưng diện tích bề mặt LẠI TĂNG LÊN** vì lộ thêm mặt nón bên trong! Liệt kê đủ 3 phần bề mặt có thể chạm tay vào (để sơn phủ):<br>1. **Đáy dưới hình tròn** (còn nguyên): \(\pi r^2 = \pi(6^2) = 36\pi\).<br>2. **Mặt xung quanh bên ngoài hình trụ**: \(2\pi r h = 2\pi(6)(8) = 96\pi\).<br>3. **Mặt xung quanh bên trong của phễu nón** (đường sinh \(l = \sqrt{6^2 + 8^2} = 10\)): \(\pi r l = \pi(6)(10) = 60\pi\).<br>(Lưu ý: Mặt đáy trên của trụ đã bị khoét mất nên KHÔNG tính!).<br>Tổng diện tích bề mặt khối rỗng là: \[36\pi + 96\pi + 60\pi = 192\pi.\]',
            r'Quy tắc "Nhúng vào thùng sơn" cho khối ghép/khoét rỗng: diện tích toàn phần = TỔNG mọi bề mặt tiếp xúc với sơn (ngoài + trong), KHÔNG bao giờ trừ diện tích xung quanh của phần bị khoét!',
            {
                'A': ('Missing Bottom Base', r'\(156\pi = 96\pi + 60\pi\) đã bỏ quên mặt đáy tròn bên dưới (\(36\pi\)) vẫn còn nguyên.'),
                'B': ('Đáp án đúng', r'Đáy dưới \(36\pi\) + vỏ trụ \(96\pi\) + lòng nón \(60\pi\) (với \(l = 10\)) \(= 192\pi\).'),
                'C': ('Double-Counted Top Base', r'\(228\pi = 72\pi + 96\pi + 60\pi\) tính thừa mặt đáy trên vốn đã bị khoét mất.'),
                'D': ('Subtracted Cavity Area', r'Trừ lòng nón khỏi diện tích toàn phần trụ (\(168\pi - 60\pi = 108\pi\)) — nhầm tư duy thể tích sang diện tích bề mặt!'),
            },
            desmos_tip_vi=r'Tách rõ 3 số hạng trên Desmos: <code>6^2 + 2*6*8 + 6*sqrt(6^2 + 8^2)</code> ra ngay hệ số <code>192</code> (tức \(192\pi\)).'
        ),

        # Q12 — Hard, SPR (Ans: 64/5 or 12.8)
        math_spr(
            'sat_m4_3_q12', 12, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Hard',
            _wrap_svg(svg_right_altitude_hyp(pq='12', sr='?', v_left='A', v_top='B', v_right='C', v_foot='D'))
            + r'<p>In right triangle \(ABC\) shown above, \(\angle B = 90^\circ\), and altitude \(\overline{BD}\) is drawn to hypotenuse \(\overline{AC}\). If \(AB = 12\) and \(\cos(A) = \dfrac{3}{5}\), determine the length of segment \(\overline{CD}\).</p>',
            r'What is the length of segment \(CD\)?',
            ['64/5', '12.8'],
            '64/5 (hoặc 12.8)',
            r'Dùng \(\cos(A) = \frac{3}{5}\) lần lượt trong hai tam giác vuông cùng chứa góc nhọn \(A\) (\(\triangle ABC\) và \(\triangle ADB\)):<br>1. Trong tam giác vuông lớn \(\triangle ABC\): \[\cos(A) = \frac{AB}{AC} = \frac{3}{5} \implies \frac{12}{AC} = \frac{3}{5} \implies AC = 20.\] 2. Trong tam giác vuông nhỏ \(\triangle ADB\) (vuông tại \(D\), cạnh huyền \(AB = 12\)): \[\cos(A) = \frac{AD}{AB} = \frac{3}{5} \implies AD = 12 \cdot \frac{3}{5} = \frac{36}{5} = 7.2.\] 3. Trừ để lấy đoạn \(CD\): \[CD = AC - AD = 20 - \frac{36}{5} = \frac{64}{5} = 12.8.\]',
            r'Áp dụng cùng một tỉ số lượng giác \(\cos(A)\) trong cả tam giác vuông lớn và tam giác vuông nhỏ chứa góc \(A\) giúp tìm ngay \(AC\) và \(AD\) chỉ trong 2 phép nhân/chia!',
            desmos_tip_vi=r'Gõ trực tiếp <code>12 / (3/5) - 12 * (3/5)</code> trên Desmos → hiện <code>12.8</code> (bấm nút phân số ra <code>64/5</code>), cả hai đều được chấm đúng!'
        ),

        # Q13 — Hard, MCQ, Ans: A
        math_mcq(
            'sat_m4_3_q13', 13, 'Geometry and Trigonometry', 'Area and volume', 'Hard',
            r'<p>Right circular cylinder \(X\) has radius \(r\) and height \(h\). Right circular cone \(Y\) has a base radius that is \(50\%\) greater than the radius of cylinder \(X\) and a height that is \(20\%\) less than the height of cylinder \(X\).</p>',
            r'The volume of cone \(Y\) is what percent of the volume of cylinder \(X\)?',
            {'A': r'\(60\%\)', 'B': r'\(40\%\)', 'C': r'\(180\%\)', 'D': r'\(120\%\)'},
            'A',
            r'Biểu diễn kích thước của hình nón \(Y\) theo hình trụ \(X\):<br>• Tăng \(50\%\): \(r_Y = 1.5r = \frac{3}{2}r\).<br>• Giảm \(20\%\): \(h_Y = 0.8h = \frac{4}{5}h\).<br>Lập tỉ số thể tích (chú ý hệ số \(\frac{1}{3}\) của hình nón và bình phương ở \(r_Y^2\)!): \[\frac{V_Y}{V_X} = \frac{\frac{1}{3}\pi r_Y^2 h_Y}{\pi r^2 h} = \frac{1}{3}\left(\frac{3}{2}\right)^2\left(\frac{4}{5}\right) = \frac{1}{3} \cdot \frac{9}{4} \cdot \frac{4}{5} = \frac{3}{5} = 0.60 = 60\%.\]',
            r'Mẹo Plug-In 800 Math: Khi bài so sánh tỉ lệ % giữa 2 khối phụ thuộc \(r, h\), đặt luôn \(r = 10, h = 10\) → mọi tính toán trở thành số nguyên sạch sẽ, không thể nhầm lũy thừa!',
            {
                'A': ('Đáp án đúng', r'\(\frac{1}{3}(1.5)^2(0.8) = \frac{1}{3}(2.25)(0.8) = 0.60 = 60\%\).'),
                'B': ('Forgot to Square Radius', r'Quên bình phương hệ số bán kính \(1.5\): tính \(\frac{1}{3}(1.5)(0.8) = 0.40 = 40\%\).'),
                'C': ('Forgot 1/3 Cone Factor', r'Dùng công thức trụ thay vì nón: \((1.5)^2(0.8) = 1.80 = 180\%\).'),
                'D': ('Missed Both 1/3 and Square', r'Nhân thẳng \(1.5 \times 0.8 = 1.20 = 120\%\), sai cả bình phương lẫn hệ số \(\frac{1}{3}\).'),
            },
            desmos_tip_vi=r'Gõ <code>(1/3) * (1.5)^2 * (0.8) * 100</code> trên Desmos để chốt thẳng <code>60</code> (\(60\%\)).'
        ),

        # Q14 — Hard, MCQ, Ans: D
        math_mcq(
            'sat_m4_3_q14', 14, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Hard',
            r'<p>For a real number \(x\) with \(0 < x < \dfrac{\pi}{4}\), suppose that \[\sin\left(2x + \frac{\pi}{9}\right) = \cos\left(x + \frac{\pi}{18}\right).\]</p>',
            r'What is the value of \(\tan\left(2x + \dfrac{\pi}{9}\right)\)?',
            {'A': r'\(\dfrac{\sqrt{3}}{3}\)', 'B': r'\(\dfrac{1}{2}\)', 'C': r'\(\dfrac{\sqrt{3}}{2}\)', 'D': r'\(\sqrt{3}\)'},
            'D',
            r'Bước 1: Với \(0 < x < \frac{\pi}{4}\), cả hai góc \(2x + \frac{\pi}{9}\) và \(x + \frac{\pi}{18}\) đều là góc nhọn trong \(\left(0, \frac{11\pi}{18}\right)\) và thực tế nằm trong \(\left(0, \frac{\pi}{2}\right)\) tại nghiệm. Theo đồng phụ radian \(\sin(\alpha) = \cos(\beta) \iff \alpha + \beta = \frac{\pi}{2}\): \[\left(2x + \frac{\pi}{9}\right) + \left(x + \frac{\pi}{18}\right) = \frac{\pi}{2}.\] Quy đồng mẫu số \(18\): \[3x + \frac{2\pi + \pi}{18} = \frac{\pi}{2} \implies 3x + \frac{\pi}{6} = \frac{\pi}{2} \implies 3x = \frac{\pi}{3} \implies x = \frac{\pi}{9}.\] Bước 2: Thay \(x = \frac{\pi}{9}\) vào góc cần tính: \[2x + \frac{\pi}{9} = \frac{2\pi}{9} + \frac{\pi}{9} = \frac{3\pi}{9} = \frac{\pi}{3}\; (60^\circ).\] Bước 3: Tính \(\tan\left(\frac{\pi}{3}\right) = \sqrt{3}\).',
            r'Công thức đồng phụ dạng Radian \(\sin(\alpha) = \cos(\beta) \implies \alpha + \beta = \frac{\pi}{2}\) xuất hiện đều đặn trong top câu Hard Module 2; luôn đổi nhanh về mẫu chung trước khi giải \(x\).',
            {
                'A': ('Complementary Angle Trap', r'\(\frac{\sqrt{3}}{3} = \tan\left(\frac{\pi}{6}\right)\) là giá trị của góc còn lại \(x + \frac{\pi}{18}\), không phải \(2x + \frac{\pi}{9}\).'),
                'B': ('Cos Instead of Tan', r'\(\frac{1}{2} = \cos\left(\frac{\pi}{3}\right)\), đọc nhầm hàm lượng giác câu hỏi.'),
                'C': ('Sin Instead of Tan', r'\(\frac{\sqrt{3}}{2} = \sin\left(\frac{\pi}{3}\right)\), đọc nhầm hàm \(\sin\) thay vì \(\tan\).'),
                'D': ('Đáp án đúng', r'\(x = \frac{\pi}{9} \Rightarrow 2x + \frac{\pi}{9} = \frac{\pi}{3} \Rightarrow \tan\left(\frac{\pi}{3}\right) = \sqrt{3}\).'),
            },
            desmos_tip_vi=r'Để Desmos ở chế độ Radian, vẽ <code>y = sin(2x + pi/9)</code> và <code>y = cos(x + pi/18)</code> với \(0 < x < \pi/4\) → chấm giao điểm lấy \(x \approx 0.34907\), gõ <code>tan(2*0.34906585 + pi/9)</code> ra <code>1.73205...</code> \(= \sqrt{3}\)!'
        ),

        # Q15 — Hard, SPR (Ans: 375)
        math_spr(
            'sat_m4_3_q15', 15, 'Geometry and Trigonometry', 'Area and volume', 'Hard',
            r'<p>Two similar right square pyramids, Pyramid \(A\) and Pyramid \(B\), have total surface areas of \(108\text{ cm}^2\) and \(300\text{ cm}^2\), respectively. The volume of Pyramid \(A\) is \(81\text{ cm}^3\).</p>',
            r'What is the volume, in cubic centimeters, of Pyramid \(B\)?',
            ['375'],
            '375',
            r'Áp dụng định luật tỉ lệ 3D cho hai hình chóp đồng dạng:<br>Bước 1: Lập tỉ số diện tích toàn phần (\(k^2\)) và rút gọn về phân số tối giản: \[k^2 = \frac{\text{SA}_B}{\text{SA}_A} = \frac{300}{108} = \frac{25}{9}.\] Bước 2: Lấy căn bậc hai để tìm tỉ số độ dài tuyến tính (\(k\)): \[k = \sqrt{\frac{25}{9}} = \frac{5}{3}.\] Bước 3: Lập phương \(k\) để lấy tỉ số thể tích (\(k^3\)): \[k^3 = \left(\frac{5}{3}\right)^3 = \frac{125}{27}.\] Bước 4: Tính thể tích hình chóp \(B\): \[V_B = V_A \cdot k^3 = 81 \times \frac{125}{27} = 3 \times 125 = 375\text{ cm}^3.\]',
            r'Công thức tổng quát 800-Level cho 2 khối đồng dạng: \(\frac{V_B}{V_A} = \left(\frac{\text{SA}_B}{\text{SA}_A}\right)^{3/2}\). Luyện thành phản xạ "rút gọn phân số SA \(\to\) căn bậc hai \(\to\) lập phương" để giải trong 15 giây.',
            desmos_tip_vi=r'Gõ một dòng duy nhất trên Desmos: <code>81 * (300 / 108)^(3/2)</code> → hiện thẳng kết quả chính xác <code>375</code>!'
        ),
    ]
    return build_math_drill_json(
        'Math Drill 4.3: Trigonometry (SOH-CAH-TOA, Cofunctions) & 3D Solid Scaling (15 câu)',
        'Module 4 • Geometry & Trigonometry • 11 MCQ + 4 SPR • Target 750–800',
        '750–800 • Trig & 3D Scaling',
        qs,
        target_minutes=22,
    )


# ============================================================================
# PUBLIC MODULE API
# ============================================================================

def get_drills():
    """Returns list of 3 tuples: (drill_key, title, order_index, content_json)."""
    return [
        (
            'drill_m4_1',
            'Math Drill 4.1: Lines, Angles, Similarity & Special Right Triangles (15 câu)',
            10,
            get_drill_m4_1(),
        ),
        (
            'drill_m4_2',
            'Math Drill 4.2: Circles — Completing the Square, Arcs, Sectors & Radians (15 câu)',
            11,
            get_drill_m4_2(),
        ),
        (
            'drill_m4_3',
            'Math Drill 4.3: Trigonometry (SOH-CAH-TOA, Cofunctions) & 3D Solid Scaling (15 câu)',
            12,
            get_drill_m4_3(),
        ),
    ]


# ============================================================================
# 100% PROGRAMMATIC MATH & SCHEMA VERIFICATION (ALL 45 QUESTIONS)
# ============================================================================

def _parse_spr_exact(s):
    s = s.strip()
    if '/' in s:
        a, b = s.split('/')
        return Fraction(a) / Fraction(b)
    return Fraction(s)


def _check_latex_and_strings(obj, path=''):
    """Recursively verifies no $ math delimiters, balanced \\(...\\)/\\[...\\], and no stray control chars."""
    if isinstance(obj, str):
        assert '$' not in obj, f"Forbidden '$' found at {path}: {obj[:80]}"
        for ch, name in [('\x08', '\\b'), ('\x0c', '\\f'), ('\r', '\\r'), ('\t', '\\t')]:
            assert ch not in obj, f"Unescaped control char {name} found at {path}: {repr(obj[:80])}"
        assert obj.count(r'\(') == obj.count(r'\)'), f"Unbalanced \\(...\\) at {path}: {obj[:120]}"
        assert obj.count(r'\[') == obj.count(r'\]'), f"Unbalanced \\[...\\] at {path}: {obj[:120]}"
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            _check_latex_and_strings(item, f"{path}[{i}]")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            _check_latex_and_strings(v, f"{path}.{k}")


def verify_all_math():
    """Programmatically asserts exact math for all 45 M4 questions + schema invariants."""
    drills = get_drills()
    assert len(drills) == 3, f"Expected 3 drills, got {len(drills)}"

    # ------------------------------------------------------------------
    # DRILL 4.1 EXACT MATH ASSERTIONS (Q1..Q15)
    # ------------------------------------------------------------------
    # Q1: 5x + 28 = 7x - 16 => x = 22, angle = 138, supplement = 42
    x1 = Fraction(28 + 16, 7 - 5)
    ang1 = 5 * x1 + 28
    assert x1 == 22 and ang1 == 7 * x1 - 16 == 138 and 180 - ang1 == 42

    # Q2: (2k+14) + (3k-6) = 6k-11 => k = 19, ext = 103, interior PRQ = 77
    k2 = Fraction(14 - 6 + 11, 6 - 5)
    ext2 = 6 * k2 - 11
    assert k2 == 19 and ext2 == 103 and (2 * k2 + 14) + (3 * k2 - 6) == ext2
    assert 180 - ext2 == 77

    # Q3: Similar triangles, k = 20/12 = 5/3, P(ABC) = 45, P(DEF) = 75
    assert Fraction(12 + 18 + 15) * Fraction(20, 12) == 75

    # Q4 (SPR): 15-36-39 right triangle perimeter = 90
    hyp4 = math.isqrt(15**2 + 36**2)
    assert hyp4**2 == 15**2 + 36**2 and hyp4 == 39
    spr_4_1_q4 = Fraction(15 + 36 + hyp4)
    assert spr_4_1_q4 == 90

    # Q5: Nested DE || BC, AD=6, DB=9, DE=8 => BC = 8*(15/6) = 20
    assert Fraction(8) * Fraction(6 + 9, 6) == 20

    # Q6: Equilateral triangle altitude h = 12 => P = 3 * (2*12/sqrt(3)) = 24*sqrt(3)
    p6 = 3 * (2 * 12 / math.sqrt(3))
    assert math.isclose(p6, 24 * math.sqrt(3), rel_tol=1e-12)

    # Q7: 45-45-90 hypotenuse = 10*sqrt(6) => s = 10*sqrt(3), Area = s^2/2 = 150
    s7_sq = Fraction(100 * 6, 2)
    assert s7_sq / 2 == 150

    # Q8 (SPR): Similar triangles area ratio (15/6)^2 * 28 = 175
    spr_4_1_q8 = Fraction(28) * Fraction(15, 6) ** 2
    assert spr_4_1_q8 == 175

    # Q9: Altitude AB=24, AD=25, AC=26 => BD=7, BC=10, CD=17, Area = 204
    bd9 = math.isqrt(25**2 - 24**2)
    bc9 = math.isqrt(26**2 - 24**2)
    assert bd9 == 7 and bc9 == 10 and Fraction(1, 2) * (bd9 + bc9) * 24 == 204

    # Q10: Bent parallel (2x+10)+(3x-5)=115 => x=22, 3x-5 = 61
    x10 = Fraction(115 - 10 + 5, 5)
    assert x10 == 22 and 3 * x10 - 5 == 61 and (2 * x10 + 10) + (3 * x10 - 5) == 115

    # Q11: Composite 30-60-90 & 45-45-90, BC=10 => BD=DC=5*sqrt(2), AD=5*sqrt(6), Area = 25 + 25*sqrt(3)
    bd11 = 10 / math.sqrt(2)
    area11 = 0.5 * bd11 * (bd11 * math.sqrt(3) + bd11)
    assert math.isclose(area11, 25 + 25 * math.sqrt(3), rel_tol=1e-12)

    # Q12 (SPR): Right triangle altitude QS, PQ=15, SR=16 => x(x+16)=225 => x=9, PR=25, QR=20, Area=150
    ps12 = Fraction(9)
    assert ps12 * (ps12 + 16) == 15**2
    pr12 = ps12 + 16
    qr12 = math.isqrt(int(pr12)**2 - 15**2)
    spr_4_1_q12 = Fraction(1, 2) * 15 * qr12
    assert qr12 == 20 and spr_4_1_q12 == 150

    # Q13: DE || BC, AD=4, DB=6 => k = 2/5, k^2 = 4/25, trap = 21/25 = 63 => Area(ADE) = 12
    k13 = Fraction(4, 4 + 6)
    area_ade13 = Fraction(63) * (k13**2) / (1 - k13**2)
    assert area_ade13 == 12

    # Q14: 16-30-34 right triangle, M midpoint of AC => CM=17, MN = 16*(17/30) = 136/15
    ac14 = math.isqrt(16**2 + 30**2)
    assert ac14 == 34
    mn14 = Fraction(16) * Fraction(ac14, 2) / Fraction(30)
    cn14 = Fraction(ac14) * Fraction(ac14, 2) / Fraction(30)
    assert mn14 == Fraction(136, 15) and cn14 < 30  # verify N strictly on segment BC

    # Q15 (SPR): Right triangle AB=21, AC=35 => BC=28; inscribed square s = ab/(a+b) = 12 => Area = 144
    bc15 = math.isqrt(35**2 - 21**2)
    assert bc15 == 28
    s15 = Fraction(21 * bc15, 21 + bc15)
    spr_4_1_q15 = s15**2
    assert s15 == 12 and spr_4_1_q15 == 144

    # ------------------------------------------------------------------
    # DRILL 4.2 EXACT MATH ASSERTIONS (Q1..Q15)
    # ------------------------------------------------------------------
    # Q1: (x+5)^2 + (y-3)^2 = 49 => center (-5, 3), r=7, d=14
    assert (-5, 3) == (-5, 3) and 2 * math.isqrt(49) == 14

    # Q2: r=12, angle=150 deg = 5pi/6 => arc = 10pi
    assert Fraction(12) * Fraction(150, 180) == 10

    # Q3: Center (4,-7) shifted (-6, +9) => (-2, 2), r^2 = 36
    assert (4 - 6, -7 + 9) == (-2, 2)

    # Q4 (SPR): x^2 + y^2 - 10x + 14y + 25 = 0 => r^2 = 25 + 49 - 25 = 49 => r = 7
    r4_2_sq = Fraction(-10, 2)**2 + Fraction(14, 2)**2 - 25
    spr_4_2_q4 = Fraction(math.isqrt(int(r4_2_sq)))
    assert r4_2_sq == 49 and spr_4_2_q4 == 7

    # Q5: Diameter (-3,2) to (5,8) => center (1,5), r^2 = 25; only B (-2,8) strictly inside
    cx5, cy5 = Fraction(-3 + 5, 2), Fraction(2 + 8, 2)
    r5_sq = (5 - cx5)**2 + (8 - cy5)**2
    assert (cx5, cy5) == (1, 5) and r5_sq == 25
    assert (5 - cx5)**2 + (2 - cy5)**2 == r5_sq   # A: on
    assert (-2 - cx5)**2 + (8 - cy5)**2 < r5_sq    # B: inside (18 < 25)
    assert (6 - cx5)**2 + (6 - cy5)**2 > r5_sq     # C: outside (26 > 25)
    assert (1 - cx5)**2 + (10 - cy5)**2 == r5_sq   # D: on

    # Q6: 5x - 10 = 2(2x + 8) => x = 26, central = 120, base angle OAB = 30
    x6_2 = Fraction(10 + 16, 5 - 4)
    cen6 = 5 * x6_2 - 10
    assert x6_2 == 26 and cen6 == 120 and Fraction(180 - cen6, 2) == 30

    # Q7: r=9, sector area = 27pi => (1/2)(81)theta = 27pi => theta/pi = 2/3
    assert Fraction(2 * 27, 9**2) == Fraction(2, 3)

    # Q8 (SPR): 2x^2 + 2y^2 - 12x + 20y - 30 = 0 => x^2 + y^2 - 6x + 10y - 15 = 0 => r^2 = 9+25+15 = 49 => d = 14
    r8_2_sq = Fraction(-6, 2)**2 + Fraction(10, 2)**2 - (-15)
    spr_4_2_q8 = Fraction(2 * math.isqrt(int(r8_2_sq)))
    assert r8_2_sq == 49 and spr_4_2_q8 == 14

    # Q9: Tangent PQ=24, RQ=16 => r^2 + 24^2 = (r+16)^2 => 32r = 320 => r = 10
    r9_2 = Fraction(24**2 - 16**2, 2 * 16)
    assert r9_2 == 10 and r9_2**2 + 24**2 == (r9_2 + 16)**2

    # Q10: Arc 14pi is 7/24 of C => C = 48pi => r = 24 => sector = (1/2)(24)(14pi) = 168pi
    c10_coeff = Fraction(14) / Fraction(7, 24)
    r10_2 = c10_coeff / 2
    assert r10_2 == 24 and Fraction(1, 2) * r10_2 * 14 == 168

    # Q11: 3x^2 + 3y^2 - 18x + 24y + c = 0, area = 36pi => r^2 = 36 => 25 - c/3 = 36 => c = -33
    c11_2 = 3 * (Fraction(-6, 2)**2 + Fraction(8, 2)**2 - 36)
    assert c11_2 == -33

    # Q12 (SPR): Center (2,-1), tangent at (5,3) => m_r = 4/3, m_t = -3/4 => y-intercept b = 27/4 = 6.75
    m_r12 = Fraction(3 - (-1), 5 - 2)
    m_t12 = -1 / m_r12
    spr_4_2_q12 = Fraction(3) + m_t12 * (0 - 5)
    assert m_r12 == Fraction(4, 3) and m_t12 == Fraction(-3, 4) and spr_4_2_q12 == Fraction(27, 4)

    # Q13: r=6, theta=2pi/3 => segment area = 12pi - 9*sqrt(3)
    seg13 = 0.5 * 6**2 * (2 * math.pi / 3 - math.sin(2 * math.pi / 3))
    assert math.isclose(seg13, 12 * math.pi - 9 * math.sqrt(3), rel_tol=1e-12)

    # Q14: (2-r)^2 + (1-r)^2 = r^2 => r^2 - 6r + 5 = 0 => r in {1, 5} => sum of areas / pi = 26
    roots14 = [r for r in range(1, 20) if (2 - r)**2 + (1 - r)**2 == r**2]
    assert roots14 == [1, 5] and sum(r**2 for r in roots14) == 26

    # Q15 (SPR): r=15, OP=30 => angle AOP = 60 deg, minor AOB = 120 deg, major = 240 deg = 4pi/3 => major arc = 20pi => k = 20
    ang_aop = math.acos(15 / 30)
    major_theta = 2 * math.pi - 2 * ang_aop
    k15_val = 15 * major_theta / math.pi
    spr_4_2_q15 = Fraction(20)
    assert math.isclose(k15_val, float(spr_4_2_q15), rel_tol=1e-12)

    # ------------------------------------------------------------------
    # DRILL 4.3 EXACT MATH ASSERTIONS (Q1..Q15)
    # ------------------------------------------------------------------
    # Q1: 8-15-17 => cos(A) + sin(C) = 8/17 + 8/17 = 16/17
    assert 8**2 + 15**2 == 17**2 and Fraction(8, 17) + Fraction(8, 17) == Fraction(16, 17)

    # Q2: Cylinder r=5, h=12 => SA/pi = 2*25 + 2*5*12 = 170
    assert 2 * 5**2 + 2 * 5 * 12 == 170

    # Q3: (3x-14) + (2x+19) = 90 => x = 17
    x3_3 = Fraction(90 + 14 - 19, 5)
    assert x3_3 == 17 and 0 < 3 * x3_3 - 14 < 90 and 0 < 2 * x3_3 + 19 < 90

    # Q4 (SPR): Cone r=6, l=10 => h=8, V/pi = (1/3)*36*8 = 96
    h4_3 = math.isqrt(10**2 - 6**2)
    spr_4_3_q4 = Fraction(1, 3) * (6**2) * h4_3
    assert h4_3 == 8 and spr_4_3_q4 == 96

    # Q5: Similar right triangles scale 4, sin(A)=7/25 => adj=24 => tan(F) = 24/7
    adj5_3 = math.isqrt(25**2 - 7**2)
    assert adj5_3 == 24 and Fraction(adj5_3, 7) == Fraction(24, 7)

    # Q6: 4cos(pi/3) + 6sin(5pi/6) - 2cos(2pi/3) = 6
    val6_3 = 4 * math.cos(math.pi / 3) + 6 * math.sin(5 * math.pi / 6) - 2 * math.cos(2 * math.pi / 3)
    assert math.isclose(val6_3, 6.0, rel_tol=1e-12)

    # Q7: V_B/V_A = 27 => k = 3 => SA_B = 36pi * 9 = 324pi
    assert 3**3 == 27 and 36 * (3**2) == 324

    # Q8 (SPR): Square pyramid base=12, l=10 => h = sqrt(10^2 - 6^2) = 8, V = (1/3)*144*8 = 384
    h8_3 = math.isqrt(10**2 - 6**2)
    spr_4_3_q8 = Fraction(1, 3) * (12**2) * h8_3
    assert h8_3 == 8 and spr_4_3_q8 == 384

    # Q9: Prism 3x4x12, d=13, Q has d=39 => k=3, V_Q = 144 * 27 = 3888
    d9_3 = math.isqrt(3**2 + 4**2 + 12**2)
    k9_3 = Fraction(39, d9_3)
    assert d9_3 == 13 and k9_3 == 3 and (3 * 4 * 12) * (k9_3**3) == 3888

    # Q10: tan(X) = 15/8 => hyp = 17 => cos(X) - cos(Z) = 8/17 - 15/17 = -7/17
    assert Fraction(8, 17) - Fraction(15, 17) == Fraction(-7, 17)

    # Q11: Hollow cone-in-cylinder r=6, h=8 => l=10, SA/pi = 36 + 96 + 60 = 192
    l11_3 = math.isqrt(6**2 + 8**2)
    assert l11_3 == 10 and (6**2 + 2 * 6 * 8 + 6 * l11_3) == 192

    # Q12 (SPR): AB=12, cos(A)=3/5 => AC=20, AD=36/5, CD = 64/5 = 12.8
    ac12_3 = Fraction(12) / Fraction(3, 5)
    ad12_3 = Fraction(12) * Fraction(3, 5)
    spr_4_3_q12 = ac12_3 - ad12_3
    assert ac12_3 == 20 and ad12_3 == Fraction(36, 5) and spr_4_3_q12 == Fraction(64, 5)

    # Q13: Cone Y r=1.5r, h=0.8h vs Cylinder X => (1/3)(9/4)(4/5) = 3/5 = 60%
    ratio13_3 = Fraction(1, 3) * Fraction(3, 2)**2 * Fraction(4, 5)
    assert ratio13_3 == Fraction(3, 5) and ratio13_3 * 100 == 60

    # Q14: (2x + pi/9) + (x + pi/18) = pi/2 => x = pi/9 => 2x + pi/9 = pi/3 => tan = sqrt(3)
    x14_3_coeff = (Fraction(1, 2) - Fraction(1, 9) - Fraction(1, 18)) / 3
    angle14_3_coeff = 2 * x14_3_coeff + Fraction(1, 9)
    assert x14_3_coeff == Fraction(1, 9) and 0 < x14_3_coeff < Fraction(1, 4)
    assert angle14_3_coeff == Fraction(1, 3)
    assert math.isclose(math.tan(float(angle14_3_coeff) * math.pi), math.sqrt(3), rel_tol=1e-12)
    assert math.isclose(
        math.sin(float(angle14_3_coeff) * math.pi),
        math.cos(float(x14_3_coeff + Fraction(1, 18)) * math.pi),
        rel_tol=1e-12,
    )

    # Q15 (SPR): Similar square pyramids SA 108 vs 300 => k^2 = 25/9, k = 5/3, k^3 = 125/27 => V_B = 81 * 125/27 = 375
    k15_sq = Fraction(300, 108)
    assert k15_sq == Fraction(25, 9)
    k15_3 = Fraction(math.isqrt(k15_sq.numerator), math.isqrt(k15_sq.denominator))
    spr_4_3_q15 = Fraction(81) * (k15_3**3)
    assert k15_3 == Fraction(5, 3) and spr_4_3_q15 == 375

    # ------------------------------------------------------------------
    # CROSS-CHECK SPR ACCEPTED ANSWERS + METADATA + LATEX INTEGRITY
    # ------------------------------------------------------------------
    expected_spr = {
        'sat_m4_1_q4': spr_4_1_q4,
        'sat_m4_1_q8': spr_4_1_q8,
        'sat_m4_1_q12': spr_4_1_q12,
        'sat_m4_1_q15': spr_4_1_q15,
        'sat_m4_2_q4': spr_4_2_q4,
        'sat_m4_2_q8': spr_4_2_q8,
        'sat_m4_2_q12': spr_4_2_q12,
        'sat_m4_2_q15': spr_4_2_q15,
        'sat_m4_3_q4': spr_4_3_q4,
        'sat_m4_3_q8': spr_4_3_q8,
        'sat_m4_3_q12': spr_4_3_q12,
        'sat_m4_3_q15': spr_4_3_q15,
    }

    expected_order = [10, 11, 12]
    expected_keys = ['drill_m4_1', 'drill_m4_2', 'drill_m4_3']
    total_q = 0

    for d_idx, (d_key, d_title, order_idx, content_json) in enumerate(drills):
        assert d_key == expected_keys[d_idx], f"Unexpected drill_key {d_key}"
        assert order_idx == expected_order[d_idx], f"Unexpected order_index {order_idx}"
        _check_latex_and_strings(content_json, d_key)

        qs = content_json['drillModule']['questions']
        assert len(qs) == 15, f"{d_key} must have 15 questions, got {len(qs)}"

        mcq_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        spr_count = 0

        for i, q in enumerate(qs):
            n = i + 1
            total_q += 1
            expected_id = f'sat_m4_{d_idx + 1}_q{n}'
            assert q['id'] == expected_id, f"Expected id {expected_id}, got {q['id']}"
            assert q['domain'] == 'Geometry and Trigonometry', f"Bad domain in {expected_id}"

            expected_diff = 'Medium' if n <= 4 else ('Medium-Hard' if n <= 10 else 'Hard')
            assert q['difficulty'] == expected_diff, f"{expected_id} difficulty {q['difficulty']} != {expected_diff}"

            exp = q['explanation']
            assert exp.get('summaryVi') and len(exp['summaryVi']) >= 40, f"{expected_id} summaryVi too short"
            assert exp.get('desmosTipVi') and len(exp['desmosTipVi']) >= 20, f"{expected_id} missing desmosTipVi"
            assert exp.get('keyTakeaway') and len(exp['keyTakeaway']) >= 20, f"{expected_id} missing keyTakeaway"

            if q['questionFormat'] == 'spr':
                spr_count += 1
                assert expected_id in expected_spr, f"Unexpected SPR {expected_id}"
                assert q.get('correctDisplay'), f"{expected_id} missing correctDisplay"
                assert r'\(' not in q['correctDisplay'], f"{expected_id} correctDisplay must be plain text"
                exact_val = expected_spr[expected_id]
                for acc in q['acceptedAnswers']:
                    assert _parse_spr_exact(acc) == exact_val, (
                        f"{expected_id} acceptedAnswer {acc} != exact {exact_val}"
                    )
            else:
                assert q['questionFormat'] == 'mcq'
                mcq_counts[q['correctAnswer']] += 1
                oa = exp['optionAnalysis']
                for lbl in ('A', 'B', 'C', 'D'):
                    assert oa[lbl]['trapTag'], f"{expected_id} missing trapTag for {lbl}"
                    assert r'\(' not in oa[lbl]['trapTag'], f"{expected_id} trapTag must be plain text"

        assert spr_count == 4, f"{d_key} expected 4 SPR, got {spr_count}"
        assert sum(mcq_counts.values()) == 11, f"{d_key} expected 11 MCQ"
        assert min(mcq_counts.values()) >= 2 and max(mcq_counts.values()) <= 3, (
            f"{d_key} imbalanced MCQ keys: {mcq_counts}"
        )

    assert total_q == 45, f"Expected 45 total questions, got {total_q}"


if __name__ == '__main__':
    verify_all_math()
    for drill_key, title, order_index, content_json in get_drills():
        errs = validate_sat_test(content_json, title)
        if errs:
            print(f"QA ERRORS in {drill_key}:")
            for e in errs:
                print("  -", e)
            sys.exit(1)
    print("ALL 3 M4 DRILLS (45 Qs) VERIFIED & QA PASSED!")
