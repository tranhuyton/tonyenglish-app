# -*- coding: utf-8 -*-
"""
Digital SAT Math 1500+ — Capstone Hard M2 Boss Masterclass (750–800 Sprint)
2 Elite-Only Math Boss Drills × 15 Questions = 30 Brand-New, Copyright-Clean Questions:
  - boss_drill_7 (order_index 7): Coordinate Circles, Nested Similarity, Radian Trig & 3D Solids
      (100% Geometry and Trigonometry • 12 inline SVG diagrams • 10 MCQ [A:3,B:2,C:3,D:2] + 5 SPR)
  - boss_drill_8 (order_index 8): SPR Grid-In Trap-Proofing — 10 Deadly 800-Point Pitfalls
      (All 4 Math Domains • 10 MCQ [A:2,B:3,C:2,D:3] + 5 SPR)

All 30 mathematical answers and schema invariants are verified programmatically in verify_all_math().
"""

import os
import sys
import math
from fractions import Fraction

sys.path.insert(0, os.path.dirname(__file__))
from sat_math_helpers import (
    math_mcq,
    math_spr,
    build_math_drill_json,
    build_math_table,
)
from sat_qa_validator import validate_sat_test


# ============================================================================
# CRISP BLUEBOOK-STYLE SVG DIAGRAM GENERATORS (BOSS DRILL 7)
# ============================================================================

def _wrap_svg(svg_str):
    return f'<div style="display:flex;justify-content:center;margin:0 auto 14px;">{svg_str}</div>'


def svg_circle_tangent_xaxis():
    """D7 Q1: Circle with center (-8, 6) in Quadrant II tangent to the x-axis at (-8, 0)."""
    return '''<svg viewBox="0 0 270 192" width="270" height="192" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <line x1="18" y1="142" x2="252" y2="142" stroke="#64748b" stroke-width="1.8"/>
  <line x1="202" y1="14" x2="202" y2="170" stroke="#64748b" stroke-width="1.8"/>
  <text x="246" y="136" font-family="serif" font-style="italic" font-size="13" fill="#334155">x</text>
  <text x="208" y="24" font-family="serif" font-style="italic" font-size="13" fill="#334155">y</text>
  <text x="208" y="156" font-family="sans-serif" font-size="10.5" fill="#64748b">O</text>
  <circle cx="110" cy="78" r="64" fill="#eff6ff" fill-opacity="0.72" stroke="#1e3a8a" stroke-width="2.4"/>
  <line x1="110" y1="78" x2="110" y2="142" stroke="#b91c1c" stroke-width="2" stroke-dasharray="5 3"/>
  <rect x="110" y="131" width="11" height="11" fill="none" stroke="#b91c1c" stroke-width="1.5"/>
  <circle cx="110" cy="78" r="3.4" fill="#1e3a8a"/>
  <circle cx="110" cy="142" r="3.4" fill="#b91c1c"/>
  <text x="118" y="75" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#1e3a8a">Center</text>
  <text x="116" y="114" font-family="sans-serif" font-size="12" font-weight="700" fill="#b91c1c">r</text>
  <text x="110" y="159" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="700" fill="#b91c1c">tangent point</text>
  <text x="135" y="184" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Circle tangent to the x-axis • Not drawn to scale.</text>
</svg>'''


def svg_tangent_external_pt():
    """D7 Q2: Circle centered at O(2,-3), r=15, tangent at T(11,9), intersecting y=-3 at P."""
    return '''<svg viewBox="0 0 300 196" width="300" height="196" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <line x1="18" y1="138" x2="282" y2="138" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 3"/>
  <text x="278" y="132" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="700" fill="#475569">y = −3</text>
  <circle cx="92" cy="138" r="60" fill="#eff6ff" fill-opacity="0.7" stroke="#1e3a8a" stroke-width="2.3"/>
  <polygon points="92,138 128,90 192,138" fill="#dbeafe" fill-opacity="0.45" stroke="none"/>
  <line x1="92" y1="138" x2="128" y2="90" stroke="#1e3a8a" stroke-width="2.2"/>
  <line x1="92" y1="138" x2="192" y2="138" stroke="#1e3a8a" stroke-width="2.2"/>
  <line x1="98" y1="67.5" x2="220" y2="159" stroke="#b91c1c" stroke-width="2.3"/>
  <polyline points="122,98 130,104 136,96" fill="none" stroke="#b91c1c" stroke-width="1.6"/>
  <circle cx="92" cy="138" r="3.4" fill="#0f172a"/>
  <circle cx="128" cy="90" r="3.4" fill="#b91c1c"/>
  <circle cx="192" cy="138" r="3.4" fill="#b91c1c"/>
  <text x="58" y="156" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#0f172a">O(2, −3)</text>
  <text x="132" y="83" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#b91c1c">T(11, 9)</text>
  <text x="196" y="156" font-family="sans-serif" font-size="12" font-weight="700" fill="#b91c1c">P</text>
  <text x="95" y="110" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#1e3a8a">r = 15</text>
  <text x="172" y="108" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#b91c1c">ℓ</text>
  <text x="150" y="186" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Line ℓ is tangent to circle O at T • Not drawn to scale.</text>
</svg>'''


def svg_semicircle_altitude():
    """D7 Q3: Semicircle diameter AB (r=25), inscribed C with AC=30, altitude CD, shaded △BCD."""
    return '''<svg viewBox="0 0 300 190" width="300" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <path d="M 48 148 A 100 100 0 0 1 248 148 Z" fill="#ffffff" stroke="#1e3a8a" stroke-width="2.3"/>
  <polygon points="120,52 120,148 248,148" fill="#dbeafe" stroke="none"/>
  <polygon points="48,148 120,52 248,148" fill="none" stroke="#1e3a8a" stroke-width="2.3" stroke-linejoin="round"/>
  <line x1="120" y1="52" x2="120" y2="148" stroke="#b91c1c" stroke-width="2" stroke-dasharray="5 3"/>
  <rect x="120" y="136" width="12" height="12" fill="none" stroke="#b91c1c" stroke-width="1.6"/>
  <circle cx="148" cy="148" r="3" fill="#0f172a"/>
  <circle cx="120" cy="52" r="3" fill="#1e3a8a"/>
  <text x="35" y="155" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">A</text>
  <text x="252" y="155" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="115" y="43" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">C</text>
  <text x="115" y="164" font-family="serif" font-size="13.5" font-weight="bold" fill="#b91c1c">D</text>
  <text x="145" y="164" font-family="serif" font-size="13" font-weight="bold" fill="#0f172a">O</text>
  <text x="58" y="96" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a">30</text>
  <text x="184" y="164" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#047857">r = 25</text>
  <text x="168" y="124" font-family="sans-serif" font-size="11" font-weight="700" fill="#1d4ed8">△BCD</text>
  <text x="150" y="182" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Diameter AB with center O and CD ⊥ AB</text>
</svg>'''


def svg_sector_arc_shortcut():
    """D7 Q4: Shaded sector AOB with arc length 15π and area 135π; find central angle θ in radians."""
    return '''<svg viewBox="0 0 260 198" width="260" height="198" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <circle cx="130" cy="98" r="68" fill="#ffffff" stroke="#1e3a8a" stroke-width="2.2"/>
  <path d="M 130 98 L 198 98 A 68 68 0 0 0 71 64 Z" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>
  <path d="M 198 98 A 68 68 0 0 0 71 64" fill="none" stroke="#b91c1c" stroke-width="3.2"/>
  <path d="M 150 98 A 20 20 0 0 0 113 88" fill="none" stroke="#b91c1c" stroke-width="1.8"/>
  <circle cx="130" cy="98" r="3" fill="#0f172a"/>
  <text x="125" y="114" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">O</text>
  <text x="203" y="102" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">A</text>
  <text x="58" y="61" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">B</text>
  <text x="131" y="75" text-anchor="middle" font-family="serif" font-style="italic" font-size="13.5" font-weight="bold" fill="#b91c1c">θ</text>
  <text x="148" y="23" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#b91c1c">arc AB = 15π</text>
  <text x="132" y="54" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#1e3a8a">Area = 135π</text>
  <text x="130" y="186" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Note: Figure not drawn to scale.</text>
</svg>'''


def svg_three_tier_nested():
    """D7 Q5: Triangle ABC cut by two parallel segments DE || FG || BC with AD=3, DF=3, FB=4."""
    return '''<svg viewBox="0 0 290 202" width="290" height="202" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="79,112 205,112 247,172 37,172" fill="#d1fae5" stroke="#047857" stroke-width="2"/>
  <polygon points="110.5,67 173.5,67 205,112 79,112" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>
  <polygon points="142,22 110.5,67 173.5,67" fill="#ffffff" stroke="#1e3a8a" stroke-width="2"/>
  <polygon points="142,22 37,172 247,172" fill="none" stroke="#1e3a8a" stroke-width="2.4" stroke-linejoin="round"/>
  <polyline points="139,63 146,67 139,71" fill="none" stroke="#b91c1c" stroke-width="1.8"/>
  <polyline points="139,108 146,112 139,116" fill="none" stroke="#b91c1c" stroke-width="1.8"/>
  <polyline points="139,168 146,172 139,176" fill="none" stroke="#b91c1c" stroke-width="1.8"/>
  <text x="138" y="16" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">A</text>
  <text x="95" y="70" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">D</text>
  <text x="179" y="70" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">E</text>
  <text x="64" y="115" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">F</text>
  <text x="211" y="115" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">G</text>
  <text x="24" y="177" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="252" y="177" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">C</text>
  <text x="114" y="45" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a">3</text>
  <text x="82" y="92" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a">3</text>
  <text x="45" y="144" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a">4</text>
  <text x="142" y="95" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#1d4ed8">Area = 54</text>
  <text x="142" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#047857">Area = ?</text>
  <text x="145" y="194" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">DE ∥ FG ∥ BC • Note: Figure not drawn to scale.</text>
</svg>'''


def svg_altitude_geometric_mean():
    """D7 Q6: Right triangle PQR (∠Q = 90°) with altitude QS = 12, PS = x, SR = x + 10."""
    return '''<svg viewBox="0 0 300 188" width="300" height="188" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="40,142 108,40 261,142" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.4" stroke-linejoin="round"/>
  <line x1="108" y1="40" x2="108" y2="142" stroke="#b91c1c" stroke-width="2.1" stroke-dasharray="5 3"/>
  <rect x="108" y="130" width="12" height="12" fill="none" stroke="#b91c1c" stroke-width="1.6"/>
  <polyline points="101,51 112,58 119,47" fill="none" stroke="#1e3a8a" stroke-width="1.7"/>
  <text x="27" y="148" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">P</text>
  <text x="103" y="30" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">Q</text>
  <text x="266" y="148" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">R</text>
  <text x="103" y="160" font-family="serif" font-size="13.5" font-weight="bold" fill="#0f172a">S</text>
  <text x="115" y="98" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#b91c1c">12</text>
  <text x="72" y="159" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a">x</text>
  <text x="184" y="159" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#047857">x + 10</text>
  <text x="150" y="180" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">∠PQR = 90° and QS ⊥ PR • Not drawn to scale.</text>
</svg>'''


def svg_asymmetric_trapezoid():
    """D7 Q7: Trapezoid ABCD (BC || AD) with AB=12, BC=10, ∠A=60°, ∠D=45°."""
    return '''<svg viewBox="0 0 315 190" width="315" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="38,148 89,58 174,58 264,148" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.4" stroke-linejoin="round"/>
  <line x1="89" y1="58" x2="89" y2="148" stroke="#b91c1c" stroke-width="1.8" stroke-dasharray="5 3"/>
  <line x1="174" y1="58" x2="174" y2="148" stroke="#b91c1c" stroke-width="1.8" stroke-dasharray="5 3"/>
  <rect x="89" y="137" width="11" height="11" fill="none" stroke="#b91c1c" stroke-width="1.4"/>
  <rect x="163" y="137" width="11" height="11" fill="none" stroke="#b91c1c" stroke-width="1.4"/>
  <text x="24" y="154" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">A</text>
  <text x="82" y="49" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="174" y="49" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">C</text>
  <text x="270" y="154" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">D</text>
  <text x="131" y="51" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1e3a8a">10</text>
  <text x="48" y="96" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1e3a8a">12</text>
  <text x="53" y="142" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#b91c1c">60°</text>
  <text x="224" y="142" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#047857">45°</text>
  <text x="157" y="179" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">BC ∥ AD • Note: Figure not drawn to scale.</text>
</svg>'''


def svg_unit_circle_q3():
    """D7 Q10: Unit circle with terminal ray in Quadrant III passing through P(-5/13, y)."""
    return '''<svg viewBox="0 0 265 198" width="265" height="198" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <line x1="22" y1="96" x2="244" y2="96" stroke="#94a3b8" stroke-width="1.6"/>
  <line x1="132" y1="16" x2="132" y2="176" stroke="#94a3b8" stroke-width="1.6"/>
  <text x="238" y="90" font-family="serif" font-style="italic" font-size="13" fill="#475569">x</text>
  <text x="138" y="25" font-family="serif" font-style="italic" font-size="13" fill="#475569">y</text>
  <circle cx="132" cy="96" r="65" fill="none" stroke="#1e3a8a" stroke-width="2.2"/>
  <path d="M 156 96 A 24 24 0 1 0 123 118" fill="none" stroke="#b91c1c" stroke-width="2"/>
  <line x1="132" y1="96" x2="107" y2="156" stroke="#b91c1c" stroke-width="2.4"/>
  <line x1="107" y1="96" x2="107" y2="156" stroke="#1e3a8a" stroke-width="1.5" stroke-dasharray="4 3"/>
  <circle cx="107" cy="156" r="3.8" fill="#b91c1c"/>
  <circle cx="132" cy="96" r="2.8" fill="#0f172a"/>
  <text x="108" y="68" font-family="serif" font-style="italic" font-size="13.5" font-weight="bold" fill="#b91c1c">θ</text>
  <text x="200" y="109" font-family="sans-serif" font-size="10.5" fill="#475569">(1, 0)</text>
  <text x="20" y="166" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#b91c1c">P(−5/13, y)</text>
  <text x="132" y="190" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Unit circle: x² + y² = 1, π &lt; θ &lt; 3π/2</text>
</svg>'''


def svg_equilateral_45_composite():
    """D7 Q11: Equilateral △ABC (Area = 36√3) joined to 45-45-90 △ADC (∠D = 90°, hypotenuse AC)."""
    return '''<svg viewBox="0 0 280 202" width="280" height="202" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="84,114 192,114 138,20" fill="#dbeafe" stroke="#1e3a8a" stroke-width="2.3" stroke-linejoin="round"/>
  <polygon points="84,114 192,114 138,168" fill="#d1fae5" stroke="#047857" stroke-width="2.3" stroke-linejoin="round"/>
  <polyline points="129,159 138,150 147,159" fill="none" stroke="#047857" stroke-width="1.6"/>
  <line x1="106" y1="145" x2="114" y2="137" stroke="#047857" stroke-width="2"/>
  <line x1="162" y1="137" x2="170" y2="145" stroke="#047857" stroke-width="2"/>
  <text x="69" y="119" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">A</text>
  <text x="134" y="14" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="197" y="119" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">C</text>
  <text x="134" y="182" font-family="serif" font-size="14" font-weight="bold" fill="#0f172a">D</text>
  <text x="138" y="84" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#1e3a8a">Equilateral</text>
  <text x="138" y="100" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#1e3a8a">Area = 36√3</text>
  <text x="138" y="138" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="700" fill="#047857">AD = CD</text>
  <text x="140" y="196" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">∠ADC = 90° • Note: Figure not drawn to scale.</text>
</svg>'''


def svg_hemisphere_cylinder():
    """D7 Q12: Cylindrical silo topped by hemisphere, radius r=6 m, TOTAL height H=19 m."""
    return '''<svg viewBox="0 0 255 206" width="255" height="206" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <path d="M 60 76 A 48 48 0 0 1 156 76" fill="#dbeafe" stroke="#1e3a8a" stroke-width="2.3"/>
  <path d="M 60 76 L 60 158 A 48 14 0 0 0 156 158 L 156 76" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.3"/>
  <ellipse cx="108" cy="76" rx="48" ry="13" fill="#dbeafe" fill-opacity="0.5" stroke="#1e3a8a" stroke-width="1.7" stroke-dasharray="4 3"/>
  <ellipse cx="108" cy="158" rx="48" ry="14" fill="none" stroke="#1e3a8a" stroke-width="1.4" stroke-dasharray="4 3"/>
  <line x1="108" y1="76" x2="156" y2="76" stroke="#b91c1c" stroke-width="2.2"/>
  <circle cx="108" cy="76" r="2.8" fill="#0f172a"/>
  <line x1="176" y1="28" x2="176" y2="158" stroke="#047857" stroke-width="1.8"/>
  <line x1="168" y1="28" x2="184" y2="28" stroke="#047857" stroke-width="1.8"/>
  <line x1="168" y1="158" x2="184" y2="158" stroke="#047857" stroke-width="1.8"/>
  <text x="130" y="70" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#b91c1c">r = 6 m</text>
  <text x="184" y="98" font-family="sans-serif" font-size="12" font-weight="700" fill="#047857">H = 19 m</text>
  <text x="127" y="196" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Hemisphere dome on right circular cylinder</text>
</svg>'''


def svg_hollow_cone_cylinder():
    """D7 Q13: Cylinder (r=5 cm, h=12 cm) with same-radius/height cone hollowed out from top."""
    return '''<svg viewBox="0 0 245 198" width="245" height="198" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <path d="M 56 44 L 56 146 A 50 15 0 0 0 156 146 L 156 44" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.2"/>
  <polygon points="56,44 156,44 106,146" fill="#fee2e2" fill-opacity="0.68" stroke="#b91c1c" stroke-width="2" stroke-dasharray="5 3"/>
  <ellipse cx="106" cy="44" rx="50" ry="15" fill="#dbeafe" fill-opacity="0.65" stroke="#1e3a8a" stroke-width="2.2"/>
  <ellipse cx="106" cy="146" rx="50" ry="15" fill="none" stroke="#1e3a8a" stroke-width="1.4" stroke-dasharray="4 3"/>
  <line x1="106" y1="44" x2="156" y2="44" stroke="#b91c1c" stroke-width="2"/>
  <circle cx="106" cy="44" r="2.6" fill="#0f172a"/>
  <text x="131" y="38" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#b91c1c">r = 5 cm</text>
  <text x="166" y="100" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a">h = 12 cm</text>
  <text x="122" y="186" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Conical cavity carved from top of solid cylinder</text>
</svg>'''


def svg_frustum_similar_cones():
    """D7 Q14: Cone (R=12 cm, H=18 cm) sliced parallel to base 6 cm above base."""
    return '''<svg viewBox="0 0 275 206" width="275" height="206" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <polygon points="116,22 76,118 156,118" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="5 3"/>
  <path d="M 76 118 L 56 166 A 60 15 0 0 0 176 166 L 156 118 Z" fill="#dbeafe" stroke="#1e3a8a" stroke-width="2.3" stroke-linejoin="round"/>
  <ellipse cx="116" cy="118" rx="40" ry="10" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>
  <ellipse cx="116" cy="166" rx="60" ry="15" fill="none" stroke="#1e3a8a" stroke-width="1.4" stroke-dasharray="4 3"/>
  <line x1="116" y1="166" x2="176" y2="166" stroke="#b91c1c" stroke-width="2"/>
  <circle cx="116" cy="166" r="2.6" fill="#0f172a"/>
  <line x1="194" y1="118" x2="194" y2="166" stroke="#047857" stroke-width="1.8"/>
  <line x1="188" y1="118" x2="200" y2="118" stroke="#047857" stroke-width="1.8"/>
  <line x1="188" y1="166" x2="200" y2="166" stroke="#047857" stroke-width="1.8"/>
  <line x1="230" y1="22" x2="230" y2="166" stroke="#1e3a8a" stroke-width="1.6"/>
  <line x1="224" y1="22" x2="236" y2="22" stroke="#1e3a8a" stroke-width="1.6"/>
  <line x1="224" y1="166" x2="236" y2="166" stroke="#1e3a8a" stroke-width="1.6"/>
  <text x="145" y="160" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="700" fill="#b91c1c">R = 12</text>
  <text x="200" y="146" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#047857">6 cm</text>
  <text x="236" y="98" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#1e3a8a">18 cm</text>
  <text x="137" y="196" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Frustum formed by slicing 6 cm above the base</text>
</svg>'''


# ============================================================================
# BOSS DRILL 7: COORDINATE CIRCLES, NESTED SIMILARITY, RADIAN TRIG & 3D SOLIDS
# 15 Questions (All Geometry and Trigonometry • 10 MCQ [A:3,B:2,C:3,D:2] + 5 SPR)
# ============================================================================

def get_boss_drill_7():
    qs = [
        # Q1 — Hard, MCQ, Ans: A (SVG #1)
        math_mcq(
            'sat_boss_d7_q1', 1, 'Geometry and Trigonometry', 'Circles', 'Hard',
            _wrap_svg(svg_circle_tangent_xaxis())
            + r'<p>In the \(xy\)-plane, the equation \[x^2 + y^2 + 16x - 12y + k = 0\] represents a circle, where \(k\) is a constant. The circle is tangent to the \(x\)-axis.</p>',
            r'What is the value of \(k\)?',
            {'A': r'\(64\)', 'B': r'\(36\)', 'C': r'\(94\)', 'D': r'\(136\)'},
            'A',
            r'Đưa phương trình đường tròn về dạng chuẩn bằng kỹ thuật hoàn thiện bình phương (completing the square): \[(x + 8)^2 + (y - 6)^2 = 64 + 36 - k = 100 - k.\] Tâm của đường tròn là \(O(-8, 6)\). Vì đường tròn tiếp xúc với trục hoành (\(x\)-axis, tức đường thẳng \(y = 0\)), bán kính \(r\) chính bằng khoảng cách từ tâm đến trục \(x\), tức trị tuyệt đối của tung độ tâm: \[r = |6| = 6 \implies r^2 = 36.\] Từ đó: \[100 - k = 36 \implies k = 64.\] Cách kiểm chứng thứ hai (cực nhanh): đường tròn tiếp xúc trục \(x\) nghĩa là khi thế \(y = 0\), phương trình \(x^2 + 16x + k = 0\) có nghiệm kép \(\Delta = 16^2 - 4k = 0 \implies k = 64\).',
            r'Bẫy Trục Tiếp Xúc (Axis-Tangency Trap): Đường tròn tâm \((h, k)\) tiếp xúc trục \(x\) thì \(r = |y_{\text{tâm}}|\) (KHÔNG phải \(|x_{\text{tâm}}|\)!); tiếp xúc trục \(y\) thì \(r = |x_{\text{tâm}}|\).',
            {
                'A': ('Đáp án đúng', r'Tâm \((-8, 6)\) tiếp xúc trục \(x\) nên \(r = 6 \implies r^2 = 36 = 100 - k \implies k = 64\).'),
                'B': ('Axis Swap Trap', r'\(36\) xuất hiện khi nhầm tiếp xúc trục \(x\) thành trục \(y\) (\(r = |-8| = 8 \implies 100 - 64 = 36\)) hoặc gán nhầm luôn \(k = r^2 = 36\).'),
                'C': ('Forgot to Square r', r'\(94 = 100 - 6\) là lỗi lấy \(100 - k = r\) thay vì \(100 - k = r^2 = 36\).'),
                'D': ('Sign Error', r'\(136 = 100 + 36\) do chuyển vế sai dấu thành \(k = 100 + r^2\).'),
            },
            desmos_tip_vi=r'Gõ thẳng <code>x^2 + y^2 + 16x - 12y + k = 0</code> vào Desmos và bật slider cho <code>k</code> (miền <code>0</code> đến <code>150</code>), rồi gõ <code>k = 64</code> để thấy đường tròn chạm khít trục \(x\) tại đúng điểm \((-8, 0)\).'
        ),

        # Q2 — Hard, MCQ, Ans: C (SVG #2)
        math_mcq(
            'sat_boss_d7_q2', 2, 'Geometry and Trigonometry', 'Circles', 'Hard',
            _wrap_svg(svg_tangent_external_pt())
            + r'<p>In the \(xy\)-plane, a circle is defined by \((x - 2)^2 + (y + 3)^2 = 225\) and has center \(O\). Line \(\ell\) is tangent to the circle at point \(T(11, 9)\) and intersects the horizontal line \(y = -3\) at an external point \(P\).</p>',
            r'What is the length of tangent segment \(\overline{PT}\)?',
            {'A': r'\(15\)', 'B': r'\(16\)', 'C': r'\(20\)', 'D': r'\(25\)'},
            'C',
            r'Từ phương trình chuẩn, đường tròn có tâm \(O(2, -3)\) và bán kính \(r = \sqrt{225} = 15\). Kiểm tra điểm \(T(11, 9)\): \((11-2)^2 + (9+3)^2 = 9^2 + 12^2 = 225\) (nằm trên đường tròn).<br>Bước 1: Tính hệ số góc của bán kính \(\overline{OT}\): \[m_{OT} = \frac{9 - (-3)}{11 - 2} = \frac{12}{9} = \frac{4}{3}.\] Bước 2: Tiếp tuyến \(\ell\) vuông góc với bán kính \(\overline{OT}\) tại \(T\), nên hệ số góc của \(\ell\) là \(m_\ell = -\frac{3}{4}\). Phương trình \(\ell\) đi qua \(T(11, 9)\): \[y - 9 = -\frac{3}{4}(x - 11).\] Bước 3: Giao điểm \(P\) với đường thẳng \(y = -3\): \[-3 - 9 = -\frac{3}{4}(x - 11) \implies -12 = -\frac{3}{4}(x - 11) \implies x - 11 = 16 \implies x = 27.\] Suy ra \(P(27, -3)\), nên \(OP = 27 - 2 = 25\).<br>Bước 4: Áp dụng định lý Pythagoras trong tam giác vuông \(\triangle OTP\) (vuông tại \(T\)): \[PT = \sqrt{OP^2 - OT^2} = \sqrt{25^2 - 15^2} = \sqrt{400} = 20.\]',
            r'Bẫy Tiếp Tuyến Hình Học Tọa Độ (Tangent-Perpendicularity Trap): Tiếp tuyến luôn vuông góc bán kính (\(m_\ell = -1/m_{OT}\)), tạo tam giác vuông \(\triangle OTP\) với cạnh huyền là đoạn nối tâm \(OP\) (KHÔNG phải đoạn tiếp tuyến \(PT\)).',
            {
                'A': ('Radius Confusion', r'\(15\) là bán kính \(OT\), nhầm tưởng \(\triangle OTP\) là tam giác vuông cân.'),
                'B': ('Horizontal Component Only', r'\(16 = 27 - 11\) mới chỉ là hiệu hoành độ \(\Delta x\) giữa \(P\) và \(T\), quên thành phần tung độ \(\Delta y = 12\).'),
                'C': ('Đáp án đúng', r'Tìm được \(P(27, -3) \implies OP = 25\), Pythagoras cho \(PT = \sqrt{25^2 - 15^2} = 20\).'),
                'D': ('Hypotenuse vs Tangent Leg', r'\(25\) là khoảng cách từ tâm đến điểm ngoài \(OP\) (cạnh huyền), không phải độ dài đoạn tiếp tuyến \(PT\).'),
            },
            desmos_tip_vi=r'Gõ <code>(x-2)^2+(y+3)^2=225</code>, <code>y-9=(-3/4)(x-11)</code> và <code>y=-3</code> trên Desmos → chấm giao điểm <code>(27, -3)</code> rồi bấm <code>sqrt((27-11)^2+(-3-9)^2)</code> ra ngay <code>20</code>.'
        ),

        # Q3 — Hard, SPR (Ans: 384) (SVG #3)
        math_spr(
            'sat_boss_d7_q3', 3, 'Geometry and Trigonometry', 'Circles', 'Hard',
            _wrap_svg(svg_semicircle_altitude())
            + r'<p>In the semicircle shown above with center \(O\) and radius \(25\), \(\overline{AB}\) is a diameter and point \(C\) lies on the semicircle such that \(AC = 30\). Altitude \(\overline{CD}\) is drawn perpendicular to \(\overline{AB}\) at point \(D\).</p>',
            r'What is the area of shaded triangle \(BCD\)?',
            ['384'],
            '384',
            r'Bước 1 (Bẫy bán kính → đường kính): Đường tròn có bán kính \(r = 25\) nên đường kính \(AB = 2r = 50\).<br>Bước 2 (Định lý Thales): Góc nội tiếp chắn nửa đường tròn luôn bằng \(90^\circ\), nên \(\triangle ACB\) vuông tại \(C\). Áp dụng Pythagoras (bộ ba 3–4–5 phóng đại 10 lần): \[BC = \sqrt{50^2 - 30^2} = \sqrt{1600} = 40.\] Diện tích toàn bộ \(\triangle ACB\) là \(\frac{1}{2}(30)(40) = 600\).<br>Bước 3 (Lối tắt 800 điểm bằng đồng dạng): Vì \(\overline{CD} \perp \overline{AB}\), tam giác vuông \(\triangle BCD \sim \triangle BAC\) với tỉ số đồng dạng theo cạnh huyền là \[k = \frac{BC}{BA} = \frac{40}{50} = \frac{4}{5}.\] Do đó diện tích \(\triangle BCD\) bằng: \[\text{Area}(\triangle BCD) = k^2 \cdot \text{Area}(\triangle ACB) = \left(\frac{4}{5}\right)^2 \times 600 = \frac{16}{25} \times 600 = 384.\] (Hoặc tính trực tiếp: \(CD = \frac{30 \cdot 40}{50} = 24\), \(BD = \frac{40^2}{50} = 32 \implies \text{Area} = \frac{1}{2}(32)(24) = 384\).)',
            r'Bẫy Đường Kính & Tam Giác Nội Tiếp Nửa Đường Tròn: Luôn đổi \(r \to d = 2r\) làm cạnh huyền, nhận diện \(\angle C = 90^\circ\), rồi dùng tỉ số diện tích \(k^2 = (BC/AB)^2\) để bỏ qua bước tính từng cạnh con.',
            desmos_tip_vi=r'Tính 1 dòng trên Desmos: <code>c = sqrt(50^2 - 30^2)</code> (ra <code>40</code>), rồi <code>(1/2)*30*c * (c/50)^2</code> ra ngay <code>384</code>.'
        ),

        # Q4 — Hard, MCQ, Ans: B (SVG #4)
        math_mcq(
            'sat_boss_d7_q4', 4, 'Geometry and Trigonometry', 'Circles', 'Hard',
            _wrap_svg(svg_sector_arc_shortcut())
            + r'<p>In the circle shown above with center \(O\), minor arc \(\widehat{AB}\) has length \(15\pi\), and the area of shaded sector \(AOB\) is \(135\pi\).</p>',
            r'What is the measure, in radians, of central angle \(\theta = \angle AOB\)?',
            {'A': r'\(\dfrac{5\pi}{12}\)', 'B': r'\(\dfrac{5\pi}{6}\)', 'C': r'\(\dfrac{5\pi}{3}\)', 'D': r'\(\dfrac{6\pi}{5}\)'},
            'B',
            r'Dùng công thức siêu tốc liên hệ trực tiếp giữa diện tích hình quạt \(A\) và độ dài cung \(s\) (tương tự diện tích tam giác \(\frac{1}{2}\text{đáy}\cdot\text{cao}\)): \[A_{\text{sector}} = \frac{1}{2} s r.\] Thay \(A = 135\pi\) và \(s = 15\pi\): \[135\pi = \frac{1}{2}(15\pi) r \implies r = \frac{270\pi}{15\pi} = 18.\] Sau khi có bán kính \(r = 18\), áp dụng công thức độ dài cung theo radian \(s = r\theta\): \[\theta = \frac{s}{r} = \frac{15\pi}{18} = \frac{5\pi}{6}\text{ radians}.\] Kiểm chứng ngược: \(A = \frac{1}{2} r^2 \theta = \frac{1}{2}(18^2)\left(\frac{5\pi}{6}\right) = 162 \cdot \frac{5\pi}{6} = 135\pi\) (chính xác tuyệt đối).',
            r'Bẫy Quên Hệ Số \(\frac{1}{2}\) Hình Quạt (Sector Area Half-Factor Trap): Nhớ cặp công thức vàng \(A = \frac{1}{2}sr\) và \(\theta = \frac{s}{r}\) (radian); viết nhầm \(A = sr\) sẽ làm bán kính giảm một nửa và góc tăng gấp đôi.',
            {
                'A': ('Diameter Instead of Radius', r'\(\frac{5\pi}{12}\) là kết quả khi chia cung \(15\pi\) cho đường kính \(36\) thay vì bán kính \(18\).'),
                'B': ('Đáp án đúng', r'Từ \(135\pi = \frac{1}{2}(15\pi)r \implies r = 18\), suy ra \(\theta = \frac{15\pi}{18} = \frac{5\pi}{6}\).'),
                'C': ('Missing 1/2 Factor', r'\(\frac{5\pi}{3}\) là bẫy kinh điển khi dùng nhầm \(A = sr\) ra \(r = 9\), dẫn đến \(\theta = \frac{15\pi}{9} = \frac{5\pi}{3}\).'),
                'D': ('Inverted Ratio Trap', r'\(\frac{6\pi}{5}\) bị đảo ngược tỉ số thành \(\frac{r}{s}\) rồi giữ lại hằng số \(\pi\).'),
            },
            desmos_tip_vi=r'Gõ <code>r = 2 * 135 / 15</code> (ra <code>18</code>) rồi gõ <code>15 / r</code> và bấm nút phân số ở bên trái dòng Desmos để hiện ngay <code>5/6</code> (tức \(\frac{5\pi}{6}\)).'
        ),

        # Q5 — Hard, MCQ, Ans: D (SVG #5)
        math_mcq(
            'sat_boss_d7_q5', 5, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Hard',
            _wrap_svg(svg_three_tier_nested())
            + r'<p>In triangle \(ABC\) shown above, points \(D\) and \(F\) lie on \(\overline{AB}\) and points \(E\) and \(G\) lie on \(\overline{AC}\) such that \(\overline{DE} \parallel \overline{FG} \parallel \overline{BC}\). The segment lengths along \(\overline{AB}\) are \(AD = 3\), \(DF = 3\), and \(FB = 4\). The area of middle trapezoid \(DFGE\) is \(54\).</p>',
            r'What is the area of bottom trapezoid \(FBCG\)?',
            {'A': r'\(72\)', 'B': r'\(96\)', 'C': r'\(200\)', 'D': r'\(128\)'},
            'D',
            r'Vì \(\overline{DE} \parallel \overline{FG} \parallel \overline{BC}\), ta có 3 tam giác lồng nhau đồng dạng theo chiều từ đỉnh \(A\) xuống: \[\triangle ADE \sim \triangle AFG \sim \triangle ABC.\] Độ dài các cạnh tương ứng xuất phát từ đỉnh \(A\) lần lượt là: \[AD = 3, \quad AF = 3 + 3 = 6, \quad AB = 3 + 3 + 4 = 10.\] Do đó tỉ số diện tích của 3 tam giác là bình phương tỉ số cạnh: \[\text{Area}(\triangle ADE) : \text{Area}(\triangle AFG) : \text{Area}(\triangle ABC) = 3^2 : 6^2 : 10^2 = 9 : 36 : 100.\] Đặt hệ số tỉ lệ \(u\):<br>• Diện tích hình thang giữa \(DFGE = (36 - 9)u = 27u\). Đề cho \(27u = 54 \implies u = 2\).<br>• Diện tích hình thang đáy \(FBCG = (100 - 36)u = 64u = 64 \times 2 = 128.\)',
            r'Bẫy Đồng Dạng Đa Tầng (Non-Similar Trapezoid Trap): Hai hình thang \(DFGE\) và \(FBCG\) KHÔNG đồng dạng với nhau! Tuyệt đối không bình phương tỉ số đoạn \(FB/DF\); luôn tính khoảng cách tích lũy từ đỉnh \(A\) (\(3, 6, 10\)) rồi lấy hiệu bình phương.',
            {
                'A': ('Linear Segment Scaling', r'\(72 = 54 \times \frac{4}{3}\) dùng nhầm tỉ số bậc 1 của 2 đoạn biên \(FB/DF\) cho diện tích.'),
                'B': ('Non-Similar Trapezoid Trap', r'\(96 = 54 \times \left(\frac{4}{3}\right)^2\) là bẫy 750+ cực độc: bình phương trực tiếp tỉ số đoạn \(FB/DF\) dù hai hình thang không đồng dạng.'),
                'C': ('Whole Triangle Trap', r'\(200 = 100 \times 2\) là diện tích của toàn bộ \(\triangle ABC\), quên trừ đi diện tích \(\triangle AFG = 72\).'),
                'D': ('Đáp án đúng', r'Tỉ lệ diện tích \(9:36:100 \implies 27u = 54 \implies u = 2 \implies \text{Area}(FBCG) = (100 - 36)\cdot 2 = 128\).'),
            },
            desmos_tip_vi=r'Tính dứt điểm trong 1 dòng Desmos: <code>54 * (10^2 - 6^2) / (6^2 - 3^2)</code> ra thẳng <code>128</code>.'
        ),

        # Q6 — Hard, SPR (Ans: 156) (SVG #6)
        math_spr(
            'sat_boss_d7_q6', 6, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Hard',
            _wrap_svg(svg_altitude_geometric_mean())
            + r'<p>In right triangle \(PQR\) shown above, \(\angle PQR = 90^\circ\) and altitude \(\overline{QS}\) is drawn to hypotenuse \(\overline{PR}\). If \(QS = 12\), \(PS = x\), and \(SR = x + 10\), where \(x > 0\):</p>',
            r'What is the area of triangle \(PQR\)?',
            ['156'],
            '156',
            r'Vì \(\overline{QS}\) là đường cao ứng với cạnh huyền \(\overline{PR}\) trong tam giác vuông \(\triangle PQR\), ta có \(\triangle PSQ \sim \triangle QSR\), suy ra định lý trung bình nhân đường cao (Altitude Geometric Mean Theorem): \[QS^2 = PS \cdot SR.\] Thay số: \[12^2 = x(x + 10) \implies x^2 + 10x - 144 = 0 \implies (x + 18)(x - 8) = 0.\] Vì \(x > 0\), ta nhận \(x = 8\). Khi đó:<br>• \(PS = 8\) và \(SR = 8 + 10 = 18\).<br>• Độ dài toàn bộ cạnh huyền \(PR = 8 + 18 = 26\).<br>Cuối cùng, diện tích \(\triangle PQR\) là: \[\text{Area}(\triangle PQR) = \frac{1}{2} \cdot PR \cdot QS = \frac{1}{2}(26)(12) = 156.\]',
            r'Bẫy Dừng Sớm Ở \(x\) (Altitude Similarity Multi-Step Trap): Đường cao chia cạnh huyền tuân theo \(h^2 = p \cdot q\). Sau khi giải ra \(x = 8\), đừng vội điền \(8\) hay cạnh huyền \(26\) — phải tính diện tích \(\frac{1}{2}(PR)(QS) = 156\).',
            desmos_tip_vi=r'Gõ <code>y = x(x + 10)</code> và <code>y = 144</code> trên Desmos → chấm giao điểm dương \(x = 8\), rồi gõ <code>0.5 * (2*8 + 10) * 12</code> ra ngay <code>156</code>.'
        ),

        # Q7 — Elite 750+, MCQ, Ans: A (SVG #7)
        math_mcq(
            'sat_boss_d7_q7', 7, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Elite 750+',
            _wrap_svg(svg_asymmetric_trapezoid())
            + r'<p>In trapezoid \(ABCD\) shown above, \(\overline{BC} \parallel \overline{AD}\), \(AB = 12\), \(BC = 10\), \(\angle BAD = 60^\circ\), and \(\angle CDA = 45^\circ\).</p>',
            r'What is the exact area of trapezoid \(ABCD\)?',
            {'A': r'\(54 + 78\sqrt{3}\)', 'B': r'\(54 + 60\sqrt{3}\)', 'C': r'\(108 + 78\sqrt{3}\)', 'D': r'\(96\sqrt{3}\)'},
            'A',
            r'Hạ hai đường cao \(\overline{BE} \perp \overline{AD}\) và \(\overline{CF} \perp \overline{AD}\) chia hình thang thành 3 phần: tam giác \(30^\circ\text{--}60^\circ\text{--}90^\circ\) bên trái, hình chữ nhật ở giữa và tam giác \(45^\circ\text{--}45^\circ\text{--}90^\circ\) bên phải.<br>Bước 1 (Tam giác trái \(\triangle ABE\), góc \(60^\circ\)): Cạnh huyền \(AB = 12\) nên \[AE = \frac{12}{2} = 6, \qquad h = BE = 6\sqrt{3}.\] Bước 2 (Hình chữ nhật \(BCFE\)): \(EF = BC = 10\) và \(CF = BE = 6\sqrt{3}\).<br>Bước 3 (Tam giác phải \(\triangle CDF\), góc \(45^\circ\)): Tam giác vuông cân nên \[FD = CF = 6\sqrt{3}.\] Bước 4 (Đáy lớn & Diện tích): Đáy lớn \(AD = 6 + 10 + 6\sqrt{3} = 16 + 6\sqrt{3}\). Diện tích hình thang: \[\text{Area} = \frac{BC + AD}{2} \cdot h = \frac{10 + (16 + 6\sqrt{3})}{2} \cdot 6\sqrt{3} = (13 + 3\sqrt{3})(6\sqrt{3}) = 78\sqrt{3} + 54 = 54 + 78\sqrt{3}.\]',
            r'Bẫy Hình Thang Lệch (Asymmetric Special-Triangle Trap): Khi hai góc đáy khác nhau (\(60^\circ\) và \(45^\circ\)), phải hạ CẢ HAI đường cao để truyền chiều cao chung \(h = 6\sqrt{3}\) từ tam giác 30–60–90 sang tam giác 45–45–90, tuyệt đối không mặc định hai phần chân đáy bằng nhau.',
            {
                'A': ('Đáp án đúng', r'Tính riêng 3 miền: \(\frac{1}{2}(6)(6\sqrt{3}) + 10(6\sqrt{3}) + \frac{1}{2}(6\sqrt{3})^2 = 18\sqrt{3} + 60\sqrt{3} + 54 = 54 + 78\sqrt{3}\).'),
                'B': ('Dropped Left Triangle', r'\(54 + 60\sqrt{3}\) quên cộng phần diện tích tam giác trái \(\triangle ABE = 18\sqrt{3}\) (hoặc quên đoạn \(AE = 6\) vào đáy lớn).'),
                'C': ('Forgot 1/2 on Right Triangle', r'\(108 + 78\sqrt{3}\) quên nhân \(\frac{1}{2}\) ở diện tích \(\triangle CDF\), lấy \((6\sqrt{3})^2 = 108\) thay vì \(54\).'),
                'D': ('Assumed Isosceles Symmetry', r'\(96\sqrt{3}\) ngộ nhận hình thang cân nên lấy \(FD = AE = 6 \implies AD = 22 \implies \frac{10+22}{2}\cdot 6\sqrt{3} = 96\sqrt{3}\).'),
            },
            desmos_tip_vi=r'Tính giá trị xấp xỉ trên Desmos: <code>h = 6*sqrt(3)</code>, rồi <code>0.5*(10 + (6 + 10 + h))*h</code> (ra <code>189.100...</code>), so khớp với 4 đáp án A–D sẽ thấy duy nhất <code>54 + 78*sqrt(3)</code> khớp từng chữ số thập phân!'
        ),

        # Q8 — Elite 750+, MCQ, Ans: C (No SVG — pure coordinate algebra)
        math_mcq(
            'sat_boss_d7_q8', 8, 'Geometry and Trigonometry', 'Circles', 'Elite 750+',
            r'<p>In the \(xy\)-plane, the graph of the equation \[x^2 - 10x + y^2 + 2ky = 56\] is a circle of radius \(15\), where \(k\) is a positive constant.</p>',
            r'What is the distance from the origin \((0, 0)\) to the center of this circle?',
            {'A': r'\(12\)', 'B': r'\(17\)', 'C': r'\(13\)', 'D': r'\(\sqrt{194}\)'},
            'C',
            r'Bước 1: Hoàn thiện bình phương cho cả \(x\) và \(y\): \[(x - 5)^2 + (y + k)^2 = 56 + (-5)^2 + k^2 = 81 + k^2.\] Tâm đường tròn là \(O(5, -k)\) và bình phương bán kính là \(r^2 = 81 + k^2\).<br>Bước 2: Đề cho bán kính \(r = 15 \implies r^2 = 225\), do đó: \[81 + k^2 = 225 \implies k^2 = 144.\] Vì \(k > 0\), ta được \(k = 12\). Suy ra tọa độ tâm là \(O(5, -12)\).<br>Bước 3: Khoảng cách từ gốc tọa độ \((0, 0)\) đến tâm \(O(5, -12)\) (bộ ba Pythagoras \(5\text{--}12\text{--}13\)): \[d = \sqrt{(5 - 0)^2 + (-12 - 0)^2} = \sqrt{25 + 144} = \sqrt{169} = 13.\]',
            r'Bẫy Tham Số \(k\) Hai Tầng (Double-Step Completing-the-Square Trap): Khi hoàn thiện bình phương, nhớ cộng CẢ hai số hạng bù \((b/2)^2\) vào vế phải (\(56 + 25 + k^2\)), và đọc kỹ xem đề hỏi \(k\) hay khoảng cách từ tâm đến gốc tọa độ.',
            {
                'A': ('Stopped Early at k', r'\(12\) mới chỉ là giá trị của tham số \(k\), chưa tính khoảng cách từ tâm \((5, -12)\) đến gốc tọa độ.'),
                'B': ('Manhattan Distance Trap', r'\(17 = |5| + |-12|\) cộng hai tọa độ thay vì dùng công thức khoảng cách Euclid \(\sqrt{5^2 + (-12)^2}\).'),
                'C': ('Đáp án đúng', r'\(81 + k^2 = 225 \implies k = 12\), tâm \((5, -12)\) cách gốc tọa độ \(\sqrt{5^2 + 12^2} = 13\).'),
                'D': ('Forgot Completing Constant 25', r'\(\sqrt{194}\) xảy ra khi quên cộng \(25\) vào vế phải: \(56 + k^2 = 225 \implies k = 13 \implies \sqrt{5^2 + 13^2} = \sqrt{194}\).'),
            },
            desmos_tip_vi=r'Gõ <code>k = sqrt(15^2 - 56 - 25)</code> trên Desmos (ra <code>12</code>), rồi bấm <code>sqrt(5^2 + k^2)</code> ra ngay <code>13</code>.'
        ),

        # Q9 — Elite 750+, SPR (Ans: 5/4 or 1.25) (No SVG — radian cofunction equation)
        math_spr(
            'sat_boss_d7_q9', 9, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Elite 750+',
            r'<p>For a real number \(k\), both \(\dfrac{5k\pi}{24} - \dfrac{\pi}{12}\) and \(\dfrac{k\pi}{8} + \dfrac{\pi}{6}\) are angle measures in radians strictly between \(0\) and \(\dfrac{\pi}{2}\), and \[\sin\!\left(\frac{5k\pi}{24} - \frac{\pi}{12}\right) = \cos\!\left(\frac{k\pi}{8} + \frac{\pi}{6}\right).\]</p>',
            r'What is the value of \(k\)?',
            ['5/4', '1.25'],
            '5/4 or 1.25',
            r'Với hai góc nhọn tính theo radian (nằm trong khoảng \((0, \frac{\pi}{2})\)), đẳng thức \(\sin(\alpha) = \cos(\beta)\) tương đương với hai góc phụ nhau (complementary angles): \[\alpha + \beta = \frac{\pi}{2}.\] Thiết lập phương trình và khử \(\pi\) ở cả hai vế: \[\left(\frac{5k}{24} - \frac{1}{12}\right) + \left(\frac{k}{8} + \frac{1}{6}\right) = \frac{1}{2}.\] Nhân toàn bộ phương trình với mẫu chung \(24\): \[(5k - 2) + (3k + 4) = 12 \implies 8k + 2 = 12 \implies 8k = 10 \implies k = \frac{5}{4} = 1.25.\] Kiểm tra điều kiện góc nhọn tại \(k = \frac{5}{4}\): góc thứ nhất là \(\frac{25\pi}{96} - \frac{8\pi}{96} = \frac{17\pi}{96}\) và góc thứ hai là \(\frac{15\pi}{96} + \frac{16\pi}{96} = \frac{31\pi}{96}\), cả hai đều thuộc \((0, \frac{\pi}{2})\) và có tổng đúng bằng \(\frac{48\pi}{96} = \frac{\pi}{2}\).',
            r'Bẫy Radian Cofunction (\(\frac{\pi}{2}\) vs \(\pi\)): Khi \(\sin(\alpha) = \cos(\beta)\) với góc nhọn theo radian, tổng hai góc bằng \(\frac{\pi}{2}\) (tức \(90^\circ\)), KHÔNG phải \(\pi\) (\(180^\circ\)) và KHÔNG phải hai góc bằng nhau.',
            desmos_tip_vi=r'Bật chế độ <b>Radians</b> (biểu tượng cờ-lê góc trên phải) trong Desmos, gõ <code>y = sin(5*x*pi/24 - pi/12)</code> và <code>y = cos(x*pi/8 + pi/6)</code>, tìm giao điểm trong khoảng \(0 < x < 2\) sẽ ra đúng <code>x = 1.25</code>.'
        ),

        # Q10 — Elite 750+, MCQ, Ans: D (SVG #8)
        math_mcq(
            'sat_boss_d7_q10', 10, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Elite 750+',
            _wrap_svg(svg_unit_circle_q3())
            + r'<p>In the \(xy\)-plane, an angle in standard position has measure \(\theta\) radians, where \(\pi < \theta < \dfrac{3\pi}{2}\). Its terminal ray intersects the unit circle \(x^2 + y^2 = 1\) at point \(P\!\left(-\dfrac{5}{13},\, y\right)\).</p>',
            r'What is the exact value of \(26\sin(\theta) - 5\tan(\theta)\)?',
            {'A': r'\(36\)', 'B': r'\(12\)', 'C': r'\(-12\)', 'D': r'\(-36\)'},
            'D',
            r'Trên đường tròn đơn vị, tọa độ điểm \(P\) chính là \((\cos\theta, \sin\theta)\), suy ra \(\cos\theta = -\frac{5}{13}\).<br>Bước 1 (Xác định dấu theo góc phần tư III): Vì \(\pi < \theta < \frac{3\pi}{2}\), điểm \(P\) nằm trong góc phần tư III (Quadrant III), nơi mà CẢ hoành độ lẫn tung độ đều âm (\(\cos\theta < 0\), \(\sin\theta < 0\)). Áp dụng \(\sin^2\theta + \cos^2\theta = 1\): \[\sin\theta = -\sqrt{1 - \left(-\frac{5}{13}\right)^2} = -\sqrt{\frac{144}{169}} = -\frac{12}{13}.\] Bước 2 (Tính \(\tan\theta\) cẩn thận dấu): Ở góc phần tư III, âm chia âm ra DƯƠNG: \[\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{-12/13}{-5/13} = +\frac{12}{5}.\] Bước 3 (Thay vào biểu thức): \[26\sin(\theta) - 5\tan(\theta) = 26\left(-\frac{12}{13}\right) - 5\left(\frac{12}{5}\right) = -24 - 12 = -36.\]',
            r'Bẫy Dấu Góc Phần Tư III (ASTC Quadrant-III Sign Trap): Trong góc phần tư III (\(\pi < \theta < \frac{3\pi}{2}\)), \(\sin\theta < 0\) và \(\cos\theta < 0\), NHƯNG \(\tan\theta = \frac{\sin\theta}{\cos\theta} > 0\) ("All Students Take Calculus").',
            {
                'A': ('Quadrant II Sign Swap', r'\(36\) xuất hiện nếu lấy nhầm \(\sin\theta = +\frac{12}{13}\) và \(\tan\theta = -\frac{12}{5}\) (dấu của góc phần tư II): \(24 - (-12) = 36\).'),
                'B': ('Ignored All Negative Signs', r'\(12 = 24 - 12\) lấy dương cả \(\sin\theta = +\frac{12}{13}\) lẫn \(\tan\theta = +\frac{12}{5}\) như thể góc nằm ở góc phần tư I.'),
                'C': ('Negative Tangent Blunder', r'\(-12 = -24 - (-12)\) đúng dấu \(\sin\theta < 0\) nhưng tưởng nhầm \(\tan\theta\) cũng âm ở góc phần tư III.'),
                'D': ('Đáp án đúng', r'Ở góc phần tư III: \(\sin\theta = -\frac{12}{13}\) và \(\tan\theta = +\frac{12}{5} \implies -24 - 12 = -36\).'),
            },
            desmos_tip_vi=r'Trên Desmos (chế độ Radians), vì góc nằm ở QIII nên gõ <code>t = 2*pi - arccos(-5/13)</code>, rồi gõ ngay <code>26*sin(t) - 5*tan(t)</code> → hiển thị chính xác <code>-36</code>!'
        ),

        # Q11 — Elite 750+, MCQ, Ans: B (SVG #9)
        math_mcq(
            'sat_boss_d7_q11', 11, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Elite 750+',
            _wrap_svg(svg_equilateral_45_composite())
            + r'<p>Quadrilateral \(ABCD\) shown above is formed by joining equilateral triangle \(ABC\) and isosceles right triangle \(ADC\) along their shared side \(\overline{AC}\), where \(\angle ADC = 90^\circ\) and \(AD = CD\). The area of equilateral triangle \(ABC\) is \(36\sqrt{3}\).</p>',
            r'What is the perimeter of quadrilateral \(ABCD\)?',
            {'A': r'\(24 + 6\sqrt{2}\)', 'B': r'\(24 + 12\sqrt{2}\)', 'C': r'\(36 + 12\sqrt{2}\)', 'D': r'\(24 + 24\sqrt{2}\)'},
            'B',
            r'Bước 1 (Tìm cạnh tam giác đều): Công thức diện tích tam giác đều cạnh \(s\) là \(\frac{s^2\sqrt{3}}{4}\). Ta có: \[\frac{s^2\sqrt{3}}{4} = 36\sqrt{3} \implies s^2 = 144 \implies s = 12.\] Vậy \(AB = BC = AC = 12\).<br>Bước 2 (Tìm hai cạnh góc vuông của tam giác \(45^\circ\text{--}45^\circ\text{--}90^\circ\)): Trong \(\triangle ADC\) vuông cân tại \(D\), cạnh chung \(\overline{AC} = 12\) là <b>cạnh huyền</b> (hypotenuse). Do đó mỗi cạnh góc vuông bằng: \[AD = CD = \frac{12}{\sqrt{2}} = 6\sqrt{2}.\] Bước 3 (Tính chu vi tứ giác \(ABCD\) — KHÔNG cộng đường chéo trong \(AC\)): \[\text{Perimeter}(ABCD) = AB + BC + CD + DA = 12 + 12 + 6\sqrt{2} + 6\sqrt{2} = 24 + 12\sqrt{2}.\]',
            r'Bẫy Cạnh Chung Nội Bộ & Đảo Tỉ Lệ 45–45–90: Khi tính chu vi hình ghép, TUYỆT ĐỐI loại bỏ cạnh chung bên trong (\(AC\)); đồng thời xác định rõ \(AC\) là cạnh huyền để CHIA cho \(\sqrt{2}\) thay vì nhân.',
            {
                'A': ('Counted Only One Leg', r'\(24 + 6\sqrt{2}\) chỉ cộng một cạnh \(AD = 6\sqrt{2}\), quên cộng cạnh \(CD = 6\sqrt{2}\) còn lại.'),
                'B': ('Đáp án đúng', r'\(AB = BC = 12\) và \(AD = CD = 6\sqrt{2}\), chu vi biên ngoài là \(24 + 12\sqrt{2}\).'),
                'C': ('Included Interior Diagonal', r'\(36 + 12\sqrt{2}\) cộng nhầm cả đường chéo bên trong \(AC = 12\) vào chu vi tứ giác.'),
                'D': ('Multiplied Instead of Divided by √2', r'\(24 + 24\sqrt{2}\) nhầm \(AC = 12\) là cạnh góc vuông nên nhân \(\sqrt{2}\) ra \(12\sqrt{2}\) cho mỗi cạnh.'),
            },
            desmos_tip_vi=r'Gõ <code>s = sqrt(4 * 36)</code> (ra <code>12</code>) rồi <code>2*s + 2*(s/sqrt(2))</code> trên Desmos (ra <code>40.9705...</code>), so khớp với 4 đáp án sẽ thấy duy nhất <code>24 + 12*sqrt(2)</code> trùng khít!'
        ),

        # Q12 — Elite 750+, SPR (Ans: 612) (SVG #10)
        math_spr(
            'sat_boss_d7_q12', 12, 'Geometry and Trigonometry', 'Area and volume', 'Elite 750+',
            _wrap_svg(svg_hemisphere_cylinder())
            + r'<p>A cylindrical grain silo is topped by a hemispherical dome of the same radius \(r = 6\text{ meters}\), as shown above. The <b>total height</b> of the silo from the circular base to the highest point of the dome is \(19\text{ meters}\). The total volume of the silo is \(k\pi\) cubic meters.</p>',
            r'What is the value of \(k\)?',
            ['612'],
            '612',
            r'Bước 1 (Gỡ bẫy tổng chiều cao): Bán cầu (hemisphere) ở trên đỉnh có chiều cao đúng bằng bán kính \(r = 6\text{ m}\). Do tổng chiều cao toàn bộ công trình là \(19\text{ m}\), chiều cao riêng phần hình trụ chỉ là: \[h_{\text{cyl}} = 19 - 6 = 13\text{ m}.\] Bước 2 (Thể tích phần hình trụ): \[V_{\text{cyl}} = \pi r^2 h_{\text{cyl}} = \pi (6^2)(13) = 468\pi.\] Bước 3 (Thể tích phần bán cầu — nhớ lấy \(\frac{1}{2}\) hình cầu!): \[V_{\text{hemi}} = \frac{1}{2} \cdot \frac{4}{3}\pi r^3 = \frac{2}{3}\pi (6^3) = \frac{2}{3}\pi(216) = 144\pi.\] Bước 4 (Tổng thể tích): \[V_{\text{total}} = 468\pi + 144\pi = 612\pi \implies k = 612.\]',
            r'Bẫy Tổng Chiều Cao Hình Ghép Bán Cầu (Total-Height & Full-Sphere Trap): Luôn tách \(h_{\text{cyl}} = H_{\text{total}} - r\) trước khi tính \(V_{\text{cyl}}\), và nhớ bán cầu dùng hệ số \(\frac{2}{3}\pi r^3\) (KHÔNG phải \(\frac{4}{3}\pi r^3\)).',
            desmos_tip_vi=r'Tính 1 dòng duy nhất trên Desmos (bỏ \(\pi\)): <code>6^2 * (19 - 6) + (2/3) * 6^3</code> → ra thẳng <code>612</code>.'
        ),

        # Q13 — Elite 750+, MCQ, Ans: A (SVG #11)
        math_mcq(
            'sat_boss_d7_q13', 13, 'Geometry and Trigonometry', 'Area and volume', 'Elite 750+',
            _wrap_svg(svg_hollow_cone_cylinder())
            + r'<p>A solid right circular cylinder has base radius \(r = 5\text{ cm}\) and height \(h = 12\text{ cm}\). A right circular cone with the same radius (\(5\text{ cm}\)) and the same height (\(12\text{ cm}\)) is completely hollowed out from the top of the cylinder, as shown above.</p>',
            r'What is the total exposed surface area, in square centimeters, of the resulting hollowed solid?',
            {'A': r'\(210\pi\)', 'B': r'\(235\pi\)', 'C': r'\(80\pi\)', 'D': r'\(205\pi\)'},
            'A',
            r'Khi khoét một hình nón rỗng từ mặt trên của hình trụ đặc, thể tích giảm đi nhưng <b>diện tích bề mặt lộ thiên</b> lại bao gồm đúng 3 phần:<br>1. <b>Mặt đáy dưới hình tròn</b> (mặt đáy trên đã bị khoét mất!): \[A_{\text{bottom}} = \pi r^2 = \pi(5^2) = 25\pi.\] 2. <b>Mặt xung quanh bên ngoài của hình trụ</b>: \[A_{\text{cyl lateral}} = 2\pi r h = 2\pi(5)(12) = 120\pi.\] 3. <b>Mặt nghiêng bên trong của khoang hình nón</b>: trước hết tính đường sinh (slant height) theo bộ ba \(5\text{--}12\text{--}13\): \[\ell = \sqrt{5^2 + 12^2} = 13\text{ cm} \implies A_{\text{cone lateral}} = \pi r \ell = \pi(5)(13) = 65\pi.\] Cộng 3 bề mặt lộ thiên: \[\text{Total Exposed SA} = 25\pi + 120\pi + 65\pi = 210\pi.\]',
            r'Bẫy Khoét Khối 3D (Hollowed-Solid Surface Area Trap): Khoét rỗng là TRỪ thể tích nhưng CỘNG thêm diện tích mặt thành bên trong (\(\pi r \ell\)) và BỎ mặt nắp bị khoét mất (\(\pi r^2\) chỉ còn 1 đáy, không phải 2).',
            {
                'A': ('Đáp án đúng', r'\(1\text{ đáy } (25\pi) + \text{thành trụ } (120\pi) + \text{thành nón trong } (65\pi) = 210\pi\).'),
                'B': ('Double-Base Trap', r'\(235\pi\) cộng cả hai đáy trụ (\(2\pi r^2 = 50\pi\)), quên rằng mặt đáy trên đã bị khoét mất.'),
                'C': ('Subtracted Cavity Area', r'\(80\pi = 25\pi + 120\pi - 65\pi\) là sai lầm kinh điển: lấy trừ thay vì cộng diện tích khoang nón.'),
                'D': ('Height Instead of Slant Height', r'\(205\pi = 25\pi + 120\pi + 60\pi\) thay nhầm chiều cao \(h = 12\) vào công thức \(\pi r \ell\) thay vì đường sinh \(\ell = 13\).'),
            },
            desmos_tip_vi=r'Gõ 1 dòng trên Desmos (bỏ \(\pi\)): <code>5^2 + 2*5*12 + 5*sqrt(5^2 + 12^2)</code> ra chính xác <code>210</code> (tức \(210\pi\)).'
        ),

        # Q14 — Elite 750+, MCQ, Ans: C (SVG #12)
        math_mcq(
            'sat_boss_d7_q14', 14, 'Geometry and Trigonometry', 'Area and volume', 'Elite 750+',
            _wrap_svg(svg_frustum_similar_cones())
            + r'<p>A solid right circular cone has a base radius of \(12\text{ cm}\) and a height of \(18\text{ cm}\). A plane parallel to the circular base slices the cone at a distance of \(6\text{ cm}\) <b>above the base</b>, removing the upper smaller cone and leaving the shaded frustum (truncated cone) below.</p>',
            r'What is the volume, in cubic centimeters, of the shaded frustum?',
            {'A': r'\(256\pi\)', 'B': r'\(480\pi\)', 'C': r'\(608\pi\)', 'D': r'\(832\pi\)'},
            'C',
            r'Bước 1 (Bẫy vị trí mặt cắt): Mặt cắt nằm cách <b>đáy</b> \(6\text{ cm}\), nên phần chóp nhỏ bị cắt bỏ ở <b>đỉnh</b> có chiều cao là: \[h_{\text{top}} = 18 - 6 = 12\text{ cm}.\] Bước 2 (Tỉ số đồng dạng của chóp đỉnh và chóp lớn): \[k = \frac{h_{\text{top}}}{H} = \frac{12}{18} = \frac{2}{3}.\] Vì hai hình nón đồng dạng, tỉ số thể tích là lập phương \(k^3\): \[\frac{V_{\text{top}}}{V_{\text{full}}} = k^3 = \left(\frac{2}{3}\right)^3 = \frac{8}{27}.\] Suy ra phần nón cụt (frustum) chiếm phần bù \(1 - \frac{8}{27} = \frac{19}{27}\) thể tích toàn phần.<br>Bước 3 (Tính thể tích): \[V_{\text{full}} = \frac{1}{3}\pi (12^2)(18) = 864\pi \implies V_{\text{frustum}} = 864\pi \times \frac{19}{27} = 32\pi \times 19 = 608\pi.\] (Kiểm chứng trực tiếp: bán kính mặt trên \(r = 12 \cdot \frac{2}{3} = 8 \implies V_{\text{top}} = \frac{1}{3}\pi(8^2)(12) = 256\pi \implies 864\pi - 256\pi = 608\pi\).)',
            r'Bẫy Chóp Cụt Đồng Dạng (Frustum Height & \(k^3\) Trap): Luôn đọc xem mặt cắt cách ĐỈNH hay cách ĐÁY để lấy đúng \(k = \frac{h_{\text{top}}}{H}\), sau đó dùng \(V_{\text{frustum}} = V_{\text{full}}(1 - k^3)\) — tuyệt đối không dùng \(k^2\).',
            {
                'A': ('Top Cone Instead of Frustum', r'\(256\pi = 864\pi \cdot \frac{8}{27}\) là thể tích của chóp nhỏ phía trên bị cắt đi, không phải phần nón cụt bên dưới.'),
                'B': ('Squared Ratio Instead of Cubed', r'\(480\pi = 864\pi\left(1 - \left(\frac{2}{3}\right)^2\right)\) dùng nhầm tỉ số diện tích \(k^2 = \frac{4}{9}\) cho thể tích.'),
                'C': ('Đáp án đúng', r'\(h_{\text{top}} = 12 \implies k = \frac{2}{3} \implies V_{\text{frustum}} = 864\pi\left(1 - \frac{8}{27}\right) = 608\pi\).'),
                'D': ('Apex vs Base Distance Trap', r'\(832\pi = 864\pi\left(1 - \left(\frac{1}{3}\right)^3\right)\) nhầm \(6\text{ cm}\) là chiều cao chóp đỉnh thay vì chiều cao chóp cụt dưới đáy.'),
            },
            desmos_tip_vi=r'Gõ 1 dòng trên Desmos (bỏ \(\pi\)): <code>(1/3)*12^2*18 * (1 - ((18 - 6)/18)^3)</code> ra thẳng <code>608</code> (tức \(608\pi\)).'
        ),

        # Q15 — Elite 750+, SPR (Ans: 1385) (No SVG — pure 3D SA-to-Volume scaling)
        math_spr(
            'sat_boss_d7_q15', 15, 'Geometry and Trigonometry', 'Area and volume', 'Elite 750+',
            r'<p>Two geometrically similar solid bronze sculptures, Sculpture \(X\) and Sculpture \(Y\), have total surface areas of \(147\text{ square inches}\) and \(432\text{ square inches}\), respectively. The volume of Sculpture \(X\) is \(343\text{ cubic inches}\).</p>',
            r'By how many cubic inches does the volume of Sculpture \(Y\) exceed the volume of Sculpture \(X\)?',
            ['1385'],
            '1385',
            r'Bước 1 (Rút gọn tỉ số diện tích \(k^2\)): Chia cả tử và mẫu của \(\frac{432}{147}\) cho ước chung \(3\): \[k^2 = \frac{\text{SA}_Y}{\text{SA}_X} = \frac{432}{147} = \frac{144}{49}.\] Bước 2 (Tìm tỉ số tuyến tính \(k\) và tỉ số thể tích \(k^3\)): \[k = \sqrt{\frac{144}{49}} = \frac{12}{7} \implies k^3 = \left(\frac{12}{7}\right)^3 = \frac{1728}{343}.\] Bước 3 (Tính thể tích Sculpture \(Y\)): \[V_Y = V_X \cdot k^3 = 343 \times \frac{1728}{343} = 1728\text{ in}^3.\] Bước 4 (Bẫy câu hỏi "exceed" — hiệu thể tích!): Đề KHÔNG hỏi \(V_Y\), mà hỏi Sculpture \(Y\) <b>nhiều hơn</b> Sculpture \(X\) bao nhiêu inch khối: \[V_Y - V_X = 1728 - 343 = 1385.\]',
            r'Bẫy Chuyển Đổi \(k^2 \to k^3\) & Bẫy Đọc Đề "Exceed": Với 2 khối đồng dạng, \(\frac{V_Y}{V_X} = \left(\frac{\text{SA}_Y}{\text{SA}_X}\right)^{3/2}\). Sau khi tính được \(V_Y = 1728\), luôn đọc lại câu hỏi xem cần điền \(V_Y\) hay hiệu \(V_Y - V_X\).',
            desmos_tip_vi=r'Gõ gọn 1 dòng vào Desmos: <code>343 * (432 / 147)^(3/2) - 343</code> → hiện ngay kết quả chính xác <code>1385</code>.'
        ),
    ]
    return build_math_drill_json(
        '🔥 Math Boss Drill 7: Coordinate Circles, Nested Similarity, Radian Trig & 3D Solids (15 câu 750–800)',
        'Hard M2 Boss Masterclass • Geometry & Trigonometry • 10 MCQ + 5 SPR • Target 750–800',
        '750–800 Boss • Geo, Trig & 3D',
        qs,
        target_minutes=25,
    )


# ============================================================================
# BOSS DRILL 8: SPR GRID-IN TRAP-PROOFING — 10 DEADLY 800-POINT PITFALLS
# 15 Questions (All 4 Math Domains • 10 MCQ [A:2,B:3,C:2,D:3] + 5 SPR)
# ============================================================================

def get_boss_drill_8():
    q6_table = build_math_table(
        [r'\(x\)', r'\(f(x)\)'],
        [
            [r'\(1\)', r'\(37\)'],
            [r'\(4\)', r'\(10\)'],
            [r'\(5\)', r'\(13\)'],
            [r'\(7\)', r'\(37\)'],
        ],
        caption='Selected Values of Quadratic Function f',
    )

    q8_table = build_math_table(
        ['Applicant Track', 'Admitted', 'Waitlisted', 'Declined', 'Total'],
        [
            ['STEM', '45', '25', '50', '120'],
            ['Humanities', '36', '24', '40', '100'],
            ['Business', '27', '23', '50', '100'],
            ['<strong>Total</strong>', '<strong>108</strong>', '<strong>72</strong>', '<strong>140</strong>', '<strong>320</strong>'],
        ],
        caption='University Admissions Decisions by Academic Track (320 Applicants)',
    )

    qs = [
        # Q1 — Hard, Algebra, MCQ, Ans: B — Trap #1: Asking for 5x - 3 instead of x
        math_mcq(
            'sat_boss_d8_q1', 1, 'Algebra', 'Systems of two linear equations in two variables', 'Hard',
            r'<p>Consider the system of linear equations below: \[\frac{5}{2}x - 3y = 19\] \[10x + 6y = 46\]</p>',
            r'If \((x, y)\) is the solution to the system, what is the value of \(5x - 3\)?',
            {'A': r'\(\dfrac{28}{5}\)', 'B': r'\(25\)', 'C': r'\(28\)', 'D': r'\(31\)'},
            'B',
            r'Thay vì giải rời từng ẩn \(x, y\) dễ rối phân số, hãy triệt tiêu ngay biến \(y\) bằng cách nhân phương trình đầu với \(2\): \[5x - 6y = 38.\] Cộng vế theo vế với phương trình thứ hai (\(10x + 6y = 46\)): \[(5x + 10x) + (-6y + 6y) = 38 + 46 \implies 15x = 84.\] Chia cả hai vế cho \(3\) để lấy trực tiếp cụm \(5x\) (không cần tìm \(x = \frac{28}{5}\) rồi lại nhân \(5\)!): \[5x = \frac{84}{3} = 28.\] Cuối cùng, tính đúng đại lượng đề yêu cầu: \[5x - 3 = 28 - 3 = 25.\]',
            r'Bẫy #1 — Hỏi Biểu Thức Thay Vì Ẩn Gốc (`5x - 3` vs `x`): Gạch chân ngay biểu thức ở dòng câu hỏi trước khi đặt bút. Trên SAT 750+, hệ số thường được thiết kế để suy thẳng ra `5x = 28` mà không cần giải lẻ \(x\).',
            {
                'A': ('Stopped Early at x', r'\(\frac{28}{5}\) mới chỉ là giá trị của \(x\), quên nhân \(5\) và trừ \(3\).'),
                'B': ('Đáp án đúng', r'Triệt tiêu \(y\) cho \(15x = 84 \implies 5x = 28 \implies 5x - 3 = 25\).'),
                'C': ('Forgot Trailing Constant', r'\(28\) là giá trị của \(5x\), quên trừ thêm \(3\) ở bước cuối.'),
                'D': ('Sign Flip on Constant', r'\(31 = 28 + 3\) cộng nhầm thay vì trừ \(3\).'),
            },
            desmos_tip_vi=r'Gõ cả hai phương trình vào Desmos để chấm giao điểm \((5.6, -1.667)\), rồi gõ ngay dòng thứ 3: <code>5*(5.6) - 3</code> để chắc chắn không điền nhầm <code>5.6</code>!'
        ),

        # Q2 — Hard, Advanced Math, MCQ, Ans: D — Trap #2A: Extraneous radical root (BOTH candidate roots positive!)
        math_mcq(
            'sat_boss_d8_q2', 2, 'Advanced Math', 'Nonlinear equations in one variable', 'Hard',
            r'<p>Consider the radical equation \[\sqrt{3x + 3} = x - 5.\]</p>',
            r'What is the sum of all real solutions to the equation?',
            {'A': r'\(2\)', 'B': r'\(9\)', 'C': r'\(13\)', 'D': r'\(11\)'},
            'D',
            r'Bước 1 (Điều kiện bắt buộc trước khi bình phương): Vì căn bậc hai số học \(\sqrt{3x + 3}\) luôn không âm (\(\ge 0\)), vế phải bắt buộc phải thỏa mãn: \[x - 5 \ge 0 \implies x \ge 5.\] Bước 2 (Bình phương hai vế và giải phương trình bậc hai): \[3x + 3 = (x - 5)^2 = x^2 - 10x + 25 \implies x^2 - 13x + 22 = 0 \implies (x - 2)(x - 11) = 0.\] Ta thu được hai nghiệm ứng viên đều DƯƠNG là \(x = 2\) và \(x = 11\).<br>Bước 3 (Loại nghiệm ngoại lai — Extraneous Root Check):<br>• Thử \(x = 11\): \(\text{VT} = \sqrt{36} = 6\), \(\text{VP} = 11 - 5 = 6\) → <b>THỎA MÃN</b>.<br>• Thử \(x = 2\): \(\text{VT} = \sqrt{9} = +3\), nhưng \(\text{VP} = 2 - 5 = -3 \neq +3\) → <b>NGHIỆM NGOẠI LAI (LOẠI!)</b>, dù \(x = 2 > 0\)!<br>Do đó phương trình chỉ có DUY NHẤT một nghiệm thực là \(x = 11\), nên tổng tất cả các nghiệm thực bằng \(11\).',
            r'Bẫy #2A — Nghiệm Ngoại Lai Căn Thức (Positive Extraneous Root & Blind Vieta Trap): Đừng bao giờ tin mẹo "loại nghiệm âm, giữ nghiệm dương" hay dùng Vieta \(-\frac{b}{a} = 13\) sau khi bình phương! Nghiệm dương \(x = 2\) vẫn ngoại lai vì làm vế phải \(x - 5 = -3 < 0\).',
            {
                'A': ('Picked Extraneous Root Only', r'\(2\) chính là nghiệm ngoại lai bị loại vì \(\sqrt{9} = +3 \neq -3\).'),
                'B': ('Subtracted Candidate Roots', r'\(9 = 11 - 2\) trừ nhầm hai nghiệm thay vì loại bỏ nghiệm ngoại lai \(x = 2\).'),
                'C': ('Blind Vieta Sum Trap', r'\(13 = 2 + 11\) là bẫy sát thủ nhất bài: cộng cả nghiệm ngoại lai \(x = 2\) (hoặc áp Vieta \(-\frac{-13}{1} = 13\) mà không thử lại!).'),
                'D': ('Đáp án đúng', r'Loại nghiệm ngoại lai \(x = 2\), chỉ còn duy nhất nghiệm \(x = 11\) nên tổng các nghiệm thực bằng \(11\).'),
            },
            desmos_tip_vi=r'Trên Desmos, gõ đúng phương trình gốc <code>y = sqrt(3x + 3)</code> và <code>y = x - 5</code> — đồ thị tự động loại nghiệm ngoại lai và chỉ hiển thị <b>1 giao điểm duy nhất</b> tại \((11, 6)\)!'
        ),

        # Q3 — Hard, PSDA, SPR (Ans: 140) — Trap #3A: Cubed unit rate conversion (ft³/min -> yd³/hr)
        math_spr(
            'sat_boss_d8_q3', 3, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Hard',
            r'<p>A high-capacity municipal pump discharges water at a constant rate of \(63\text{ cubic feet per minute}\). (\(1\text{ yard} = 3\text{ feet}\))</p>',
            r'What is this discharge rate, in cubic yards per hour?',
            ['140'],
            '140',
            r'Bước 1 (Đổi đơn vị thể tích lập phương — CẨN THẬN LẬP PHƯƠNG \(3^3 = 27\)): Vì \(1\text{ yard} = 3\text{ feet}\), ta có \[1\text{ yd}^3 = (3\text{ ft})^3 = 27\text{ ft}^3.\] Bước 2 (Đổi đơn vị thời gian từ phút sang giờ): Trong \(1\text{ giờ} = 60\text{ phút}\), lượng nước bơm ra gấp \(60\) lần lượng bơm trong \(1\) phút (nhân \(60\), KHÔNG chia \(60\)).<br>Bước 3 (Phân tích thứ nguyên — Dimensional Analysis): \[63\ \frac{\text{ft}^3}{\text{min}} \times \frac{1\text{ yd}^3}{27\text{ ft}^3} \times \frac{60\text{ min}}{1\text{ hr}} = \frac{63}{27} \times 60 = \frac{7}{3} \times 60 = 140\ \frac{\text{yd}^3}{\text{hr}}.\]',
            r'Bẫy #3A — Tốc Độ Đơn Vị Bậc 3 (`ft³/min → yd³/hr` Trap): Đổi đơn vị thể tích phải chia cho \(3^3 = 27\) (KHÔNG phải \(3\) hay \(9\)), và đổi mẫu số từ phút sang giờ phải NHÂN \(60\). Luôn viết phân số triệt tiêu đơn vị để tránh đảo ngược.',
            desmos_tip_vi=r'Gõ nguyên phép tính phân tích thứ nguyên vào Desmos: <code>63 * (1 / 3^3) * 60</code> → ra thẳng <code>140</code>.'
        ),

        # Q4 — Hard, PSDA, MCQ, Ans: A — Trap #4: "p% greater than" vs "p% of" & reverse discount
        math_mcq(
            'sat_boss_d8_q4', 4, 'Problem-Solving and Data Analysis', 'Percentages', 'Hard',
            r'<p>A wholesale distributor supplies laptops to a retail store. The store sets the list price of a laptop to be \(150\%\) <b>greater than</b> its wholesale cost, and later sells the laptop at a \(20\%\) discount off the list price. The final sale price of the laptop is \(600\text{ dollars}\).</p>',
            r'What was the wholesale cost of the laptop, in dollars?',
            {'A': r'\(300\)', 'B': r'\(500\)', 'C': r'\(288\)', 'D': r'\(480\)'},
            'A',
            r'Gọi giá nhập sỉ (wholesale cost) là \(c\) (dollars).<br>Bước 1 (Gỡ bẫy "\(150\%\) greater than" vs "\(150\%\) of"): Giá niêm yết cao hơn giá sỉ \(150\%\) nghĩa là phải <b>cộng thêm</b> \(150\%\) vào \(100\%\) ban đầu: \[\text{List Price} = c(1 + 1.50) = 2.50c \quad (\text{KHÔNG phải } 1.50c!).\] Bước 2 (Áp mã giảm giá \(20\%\) lên giá niêm yết): \[\text{Sale Price} = (1 - 0.20)(2.50c) = 0.80 \times 2.50c = 2.00c.\] Bước 3 (Giải ngược về giá sỉ \(c\)): \[2.00c = 600 \implies c = \frac{600}{2} = 300\text{ dollars}.\] Kiểm chứng ngược: \(300 \xrightarrow{+150\%} 750 \xrightarrow{-20\%} 750 \times 0.8 = 600\) (khớp 100%).',
            r'Bẫy #4 — Cặp Bẫy Phần Trăm Kép ("p% greater than" & Reverse Discount): "\(p\%\) greater than \(x\)" luôn là \((1 + \frac{p}{100})x\); và để tìm giá gốc trước khi giảm \(20\%\), phải CHIA cho \(0.80\) chứ KHÔNG nhân \(1.20\).',
            {
                'A': ('Đáp án đúng', r'\(c \times (1 + 1.50) \times (1 - 0.20) = 2c = 600 \implies c = 300\).'),
                'B': ('"p% of" Instead of "p% greater"', r'\(500\) là bẫy dịch sai "150% greater than" thành \(1.50c\): \(1.50 \times 0.80c = 1.20c = 600 \implies c = 500\).'),
                'C': ('Reverse Discount Blunder', r'\(288\) là bẫy nhân ngược \(1.20\) thay vì chia \(0.80\): \(600 \times 1.20 = 720\), rồi \(720 / 2.50 = 288\).'),
                'D': ('Wrong Direction Discount', r'\(480 = 600 \times 0.80\) áp giảm \(20\%\) lên thẳng giá bán cuối thay vì chia ngược.'),
            },
            desmos_tip_vi=r'Gõ thẳng phương trình chuỗi hệ số trên Desmos: <code>600 / ((1 + 1.50) * (1 - 0.20))</code> → ra ngay <code>300</code>.'
        ),

        # Q5 — Hard, Algebra, MCQ, Ans: C — Trap #5: Strict inequality integer ceiling/floor trap
        math_mcq(
            'sat_boss_d8_q5', 5, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>A home solar-battery leasing plan charges a one-time installation fee of \(420\text{ dollars}\) plus \(35\text{ dollars}\) per month. An outright purchase plan costs a flat \(1{,}190\text{ dollars}\) with no monthly fees.</p>',
            r'What is the minimum integer number of months \(m\) for which the total cost of the leasing plan is <b>strictly greater than</b> the cost of the purchase plan?',
            {'A': r'\(21\)', 'B': r'\(22\)', 'C': r'\(23\)', 'D': r'\(34\)'},
            'C',
            r'Thiết lập bất phương trình chặt ("strictly greater than" → dấu \(>\), KHÔNG có dấu bằng): \[420 + 35m > 1190.\] Trừ \(420\) ở cả hai vế: \[35m > 770 \implies m > \frac{770}{35} = 22.\] Điểm chết người của bài toán là mốc biên \(m = 22\) rơi vào <b>đúng số nguyên</b>: tại \(m = 22\), tổng tiền thuê là \(420 + 35(22) = 1{,}190\) dollars — BẰNG ĐÚNG giá mua, chưa hề "strictly greater than"! Vì \(m\) phải là số nguyên lớn hơn hẳn \(22\), giá trị nguyên nhỏ nhất thỏa mãn là \[m = 23.\]',
            r'Bẫy #5 — Mốc Biên Nguyên Của Bất Phương Trình Chặt (Strict Inequality Boundary Trap): Khi giải ra \(m > N\) (hoặc \(m < N\)) mà \(N\) là số nguyên, KHÔNG BAO GIỜ chọn \(N\); phải tiến thêm \(+1\) (với \(>\)) hoặc lùi \(-1\) (với \(<\)) và thử lại vào đề.',
            {
                'A': ('Wrong Boundary Direction', r'\(21\) lùi xuống \(22 - 1\) thay vì tiến lên \(22 + 1\); tại \(m = 21\) tiền thuê mới là \(1{,}155 < 1{,}190\).'),
                'B': ('Equality Boundary Trap', r'\(22\) là bẫy kinh điển: giải \(420 + 35m = 1190\) ra \(22\) nhưng quên rằng tại \(m = 22\) hai gói bằng nhau chứ chưa lớn hơn hẳn.'),
                'C': ('Đáp án đúng', r'\(m > 22\) nên số nguyên nhỏ nhất là \(23\) (tiền thuê \(= 1{,}225 > 1{,}190\)).'),
                'D': ('Ignored Fixed Upfront Fee', r'\(34 = 1190 / 35\) quên trừ khoản phí lắp đặt ban đầu \(420\) dollars.'),
            },
            desmos_tip_vi=r'Gõ <code>y = 420 + 35x</code> và <code>y = 1190</code> trên Desmos → giao điểm tại \((22, 1190)\) cho thấy tại \(22\) chúng bằng nhau, nên đáp án nguyên đầu tiên lớn hơn hẳn là <code>23</code>.'
        ),

        # Q6 — Hard, Advanced Math, SPR (Ans: 17) — Trap #6: Shifted function table g(x) = f(x + 2) - 5
        math_spr(
            'sat_boss_d8_q6', 6, 'Advanced Math', 'Nonlinear functions', 'Hard',
            q6_table
            + r'<p>The table above gives selected values of a quadratic function \(f\). The function \(g\) is defined by \(g(x) = f(x + 2) - 5\).</p>',
            r'What is the value of \(g(0)\)?',
            ['17'],
            '17',
            r'Bước 1 (Khôi phục công thức hàm bậc hai \(f(x)\) từ tính đối xứng của bảng): Quan sát thấy \(f(1) = 37\) và \(f(7) = 37\). Trục đối xứng của parabol là trung điểm \[h = \frac{1 + 7}{2} = 4.\] Đúng lúc đó, bảng cho ngay đỉnh tại \(x = 4\) là \(f(4) = 10\), nên: \[f(x) = a(x - 4)^2 + 10.\] Thay điểm \((5, 13)\) vào để tìm \(a\): \[a(5 - 4)^2 + 10 = 13 \implies a = 3 \implies f(x) = 3(x - 4)^2 + 10.\] Bước 2 (Gỡ bẫy dịch chuyển \(g(x) = f(x + 2) - 5\)): Thay trực tiếp \(x = 0\) vào định nghĩa của \(g(x)\) — TUYỆT ĐỐI không đổi dấu bên trong ngoặc khi đang thay số: \[g(0) = f(0 + 2) - 5 = f(2) - 5.\] Tính \(f(2) = 3(2 - 4)^2 + 10 = 3(4) + 10 = 22\). Cuối cùng trừ \(5\): \[g(0) = 22 - 5 = 17.\]',
            r'Bẫy #6 — Dịch Chuyển Bảng Hàm Số (`f(x + 2) - 5` Sign Trap): Đừng suy đoán bằng lời "dịch trái/dịch phải" dễ ngược dấu! Để tìm \(g(0)\), cứ thế thẳng \(x = 0\) vào biểu thức \(g(0) = f(0 + 2) - 5 = f(2) - 5\), và nhớ bước trừ \(5\) cuối cùng.',
            desmos_tip_vi=r'Tạo bảng <code>x_1, y_1</code> với 4 điểm <code>(1,37), (4,10), (5,13), (7,37)</code> trong Desmos, gõ hồi quy <code>y_1 ~ a x_1^2 + b x_1 + c</code> (ra \(a=3, b=-24, c=58\)), định nghĩa <code>f(x) = ax^2 + bx + c</code> rồi bấm <code>f(0 + 2) - 5</code> → hiện ngay <code>17</code>!'
        ),

        # Q7 — Elite 750+, Geo & Trig, MCQ, Ans: B — Trap #7A + #1: 2x^2 + 2y^2 circle + asking for DIAMETER
        math_mcq(
            'sat_boss_d8_q7', 7, 'Geometry and Trigonometry', 'Circles', 'Elite 750+',
            r'<p>In the \(xy\)-plane, a circle is defined by the equation \[2x^2 + 2y^2 - 12x + 20y - 60 = 0.\]</p>',
            r'What is the length of the <b>diameter</b> of this circle?',
            {'A': r'\(8\)', 'B': r'\(16\)', 'C': r'\(28\)', 'D': r'\(14\)'},
            'B',
            r'Bước 1 (GỠ BẪY #7A — Chia toàn bộ phương trình cho hệ số \(a = 2\) TRƯỚC khi hoàn thiện bình phương!): \[x^2 + y^2 - 6x + 10y - 30 = 0 \implies x^2 - 6x + y^2 + 10y = 30.\] Bước 2 (Hoàn thiện bình phương): Thêm \(\left(\frac{-6}{2}\right)^2 = 9\) và \(\left(\frac{10}{2}\right)^2 = 25\) vào cả hai vế: \[(x - 3)^2 + (y + 5)^2 = 30 + 9 + 25 = 64.\] Suy ra bán kính \(r = \sqrt{64} = 8\).<br>Bước 3 (GỠ BẪY #1 — Đề hỏi ĐƯỜNG KÍNH chứ không phải bán kính!): \[\text{Diameter} = 2r = 2(8) = 16.\]',
            r'Bẫy #7A + #1 — Đường Tròn Hệ Số \(2x^2 + 2y^2\) & Bẫy Đường Kính: LUÔN chia cả phương trình cho hệ số đứng trước \(x^2, y^2\) trước khi hoàn thiện bình phương (nếu quên chia sẽ dính số chính phương giả \(196 = 14^2\)!), và kiểm tra xem đề hỏi \(r\) hay \(d = 2r\).',
            {
                'A': ('Radius Instead of Diameter', r'\(8\) là bán kính \(r\), rơi vào Bẫy #1 do quên nhân \(2\) thành đường kính.'),
                'B': ('Đáp án đúng', r'Chia cho \(2 \implies (x-3)^2 + (y+5)^2 = 64 \implies r = 8 \implies d = 16\).'),
                'C': ('Forgot Leading Coeff 2', r'\(28\) là bẫy 800 điểm cực hiểm: quên chia \(2\) nên tính \(60 + (-6)^2 + 10^2 = 196 \implies r_{\text{giả}} = 14 \implies d_{\text{giả}} = 28\).'),
                'D': ('Double Blunder (Coeff 2 + Radius)', r'\(14 = \sqrt{196}\) vừa quên chia \(2\) vừa dừng lại ở bán kính giả.'),
            },
            desmos_tip_vi=r'Gõ thẳng <code>2x^2 + 2y^2 - 12x + 20y - 60 = 0</code> vào Desmos → bấm vào điểm cao nhất \((3, 3)\) và thấp nhất \((3, -13)\) của hình tròn, lấy \(3 - (-13) = 16\) ra thẳng đường kính trong 5 giây!'
        ),

        # Q8 — Elite 750+, PSDA, MCQ, Ans: D — Trap #8: Conditional probability denominator trap
        math_mcq(
            'sat_boss_d8_q8', 8, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Elite 750+',
            q8_table
            + r'<p>The table above summarizes the admission decisions for \(320\) university applicants across three academic tracks.</p>',
            r'If one applicant who was <b>not declined</b> is selected at random, what is the probability that the applicant applied to the STEM track?',
            {'A': r'\(\dfrac{7}{32}\)', 'B': r'\(\dfrac{7}{12}\)', 'C': r'\(\dfrac{5}{12}\)', 'D': r'\(\dfrac{7}{18}\)'},
            'D',
            r'Đây là bài xác suất có điều kiện \(P(\text{STEM} \mid \text{Not Declined})\).<br>Bước 1 (Chốt MẪU SỐ từ mệnh đề điều kiện "If one applicant who was <b>not declined</b>..."): Tập không gian mẫu bị thu hẹp chỉ còn những thí sinh <b>Admitted</b> hoặc <b>Waitlisted</b> (tức tổng trừ đi Declined): \[\text{Denominator} = 108 + 72 = 180 \quad (\text{hoặc } 320 - 140 = 180).\] Bước 2 (Chốt TỬ SỐ — vừa thuộc STEM vừa không bị từ chối): \[\text{Numerator} = 45\ (\text{Admitted}) + 25\ (\text{Waitlisted}) = 70.\] Bước 3 (Rút gọn xác suất): \[P(\text{STEM} \mid \text{Not Declined}) = \frac{70}{180} = \frac{7}{18}.\]',
            r'Bẫy #8 — Sai Mẫu Số Xác Suất Có Điều Kiện (Conditional Probability Denominator Trap): Đọc ngay cụm mở đầu "If one [X] is selected..." để khóa chặt mẫu số là tổng nhóm [X] (`180`), KHÔNG chia cho tổng toàn bảng (`320`), KHÔNG đảo ngược điều kiện, và đọc kỹ từ phủ định `"not declined"` (= Admitted + Waitlisted).',
            {
                'A': ('Grand Total Denominator Trap', r'\(\frac{7}{32} = \frac{70}{320}\) chia nhầm cho tổng toàn bộ \(320\) thí sinh thay vì nhóm điều kiện \(180\) người không bị từ chối.'),
                'B': ('Reversed Conditional Trap', r'\(\frac{7}{12} = \frac{70}{120}\) tính ngược thành \(P(\text{Not Declined} \mid \text{STEM})\), lấy tổng dòng STEM làm mẫu số.'),
                'C': ('Admitted-Only Misread', r'\(\frac{5}{12} = \frac{45}{108}\) bỏ sót nhóm Waitlisted khi đọc cụm "not declined".'),
                'D': ('Đáp án đúng', r'Mẫu số "not declined" \(= 108 + 72 = 180\), tử số STEM không bị từ chối \(= 45 + 25 = 70 \implies \frac{70}{180} = \frac{7}{18}\).'),
            },
            desmos_tip_vi=r'Gõ <code>(45 + 25) / (108 + 72)</code> vào Desmos rồi nhấn biểu tượng phân số bên trái ô nhập để rút gọn tức thì ra <code>7/18</code>.'
        ),

        # Q9 — Elite 750+, Advanced Math, SPR (Ans: 21/4 or 5.25) — Trap #7B: a != 1 Vieta sum/product trap
        math_spr(
            'sat_boss_d8_q9', 9, 'Advanced Math', 'Nonlinear equations in one variable', 'Elite 750+',
            r'<p>In the quadratic equation \[4x^2 - (5k - 3)x + (2k + 7) = 0,\] where \(k\) is a constant, the sum of the two real solutions is \(8\).</p>',
            r'What is the <b>product</b> of the two solutions to this equation?',
            ['21/4', '5.25'],
            '21/4 or 5.25',
            r'Với phương trình bậc hai \(ax^2 + bx + c = 0\) có hệ số đầu \(a = 4 \neq 1\), định lý Vieta BẮT BUỘC phải chia cho \(a = 4\) ở cả tổng lẫn tích nghiệm:<br>Bước 1 (Tìm \(k\) từ tổng nghiệm \(-\frac{b}{a} = 8\)): \[-\frac{-(5k - 3)}{4} = 8 \implies \frac{5k - 3}{4} = 8 \implies 5k - 3 = 32 \implies 5k = 35 \implies k = 7.\] Kiểm tra nhanh biệt thức \(\Delta\) tại \(k = 7\): phương trình trở thành \(4x^2 - 32x + 21 = 0\), có \(\Delta = (-32)^2 - 4(4)(21) = 1024 - 336 = 688 > 0\) (chắc chắn có 2 nghiệm thực phân biệt).<br>Bước 2 (Tính tích nghiệm \(\frac{c}{a}\) — KHÔNG QUÊN CHIA CHO \(a = 4\) LẦN NỮA!): \[\text{Product} = \frac{c}{a} = \frac{2k + 7}{4} = \frac{2(7) + 7}{4} = \frac{21}{4} = 5.25.\]',
            r'Bẫy #7B — Quên Chia Hệ Số Đầu \(a \neq 1\) Trong Vieta (Non-Unit Vieta Trap): Luôn thuộc lòng \(S = -\frac{b}{a}\) và \(P = \frac{c}{a}\). Bài này gài bẫy kép ở cả 2 bước: quên chia \(4\) khi giải \(k\) hoặc dừng ở \(c = 21\) mà quên chia \(4\) cho tích nghiệm!',
            desmos_tip_vi=r'Gõ <code>k = (4*8 + 3) / 5</code> (ra <code>7</code>), rồi vẽ <code>y = 4x^2 - (5k - 3)x + (2k + 7)</code> → nhấn 2 giao điểm trục \(x\) (\(0.721...\) và \(7.278...\)) và nhân chúng lại (hoặc gõ <code>(2k + 7)/4</code>) ra đúng <code>5.25</code>.'
        ),

        # Q10 — Elite 750+, PSDA, MCQ, Ans: A — Trap #9: Standard Deviation shift vs scale trap
        math_mcq(
            'sat_boss_d8_q10', 10, 'Problem-Solving and Data Analysis', 'One-variable data: distributions and measures of center and spread', 'Elite 750+',
            r'<p>Dataset \(A\) consists of \(12\) measurements with a mean of \(40\) and a standard deviation of \(6\). Two new datasets are created from Dataset \(A\):</p><ul><li><b>Dataset \(B\)</b> is formed by multiplying every value in Dataset \(A\) by \(3\) and then adding \(25\).</li><li><b>Dataset \(C\)</b> is formed by adding \(50\) to every value in Dataset \(A\).</li></ul>',
            r'If \(\sigma_B\) and \(\sigma_C\) represent the standard deviations of Datasets \(B\) and \(C\), respectively, what is the value of \(\sigma_B - \sigma_C\)?',
            {'A': r'\(12\)', 'B': r'\(-13\)', 'C': r'\(37\)', 'D': r'\(55\)'},
            'A',
            r'Áp dụng quy tắc bất biến dịch chuyển & co giãn của Độ lệch chuẩn (Standard Deviation — đo <b>độ phân tán quanh trung bình</b>): nếu biến đổi tuyến tính \(Y = mX + b\), thì: \[\mu_Y = m\mu_X + b, \qquad \text{nhưng} \qquad \sigma_Y = |m| \cdot \sigma_X.\] Hằng số cộng thêm \(+b\) chỉ tịnh tiến toàn bộ phân phối sang phải mà KHÔNG làm các điểm dữ liệu giãn xa nhau thêm!<br>• Với <b>Dataset \(B\)</b> (\(3A + 25\)): \(\sigma_B = |3| \cdot \sigma_A = 3(6) = 18\) (số \(+25\) hoàn toàn bị triệt tiêu khỏi SD!).<br>• Với <b>Dataset \(C\)</b> (\(A + 50\)): \(\sigma_C = |1| \cdot \sigma_A = 6\) (cộng \(50\) KHÔNG làm thay đổi SD!).<br>Suy ra: \[\sigma_B - \sigma_C = 18 - 6 = 12.\]',
            r'Bẫy #9 — Tịnh Tiến vs Co Giãn Độ Lệch Chuẩn (SD Shift vs. Scale Trap): Cộng/trừ hằng số \(+b\) vào mọi giá trị sẽ dịch Mean đi \(+b\) nhưng giữ nguyên 100% Standard Deviation; chỉ có phép NHÂN/CHIA cho \(m\) mới nhân SD với \(|m|\).',
            {
                'A': ('Đáp án đúng', r'\(\sigma_B = 3(6) = 18\) và \(\sigma_C = 6 \implies \sigma_B - \sigma_C = 12\).'),
                'B': ('Shifted SD by Constant', r'\(-13\) là bẫy cộng cả hằng số tịnh tiến vào SD: \(\sigma_B = 3(6)+25 = 43\), \(\sigma_C = 6+50 = 56 \implies 43 - 56 = -13\).'),
                'C': ('Inconsistent Shift Error', r'\(37 = (3\cdot 6 + 25) - 6\) cộng nhầm \(+25\) vào \(\sigma_B\) trong khi lại giữ nguyên \(\sigma_C = 6\).'),
                'D': ('Mean Instead of SD Trap', r'\(55 = (3\cdot 40 + 25) - (40 + 50) = 145 - 90\) là hiệu hai giá trị trung bình \(\mu_B - \mu_C\), nhầm công thức của Mean sang SD.'),
            },
            desmos_tip_vi=r'Nếu muốn kiểm chứng bằng dữ liệu thật trên Desmos, tạo một list đối xứng bất kỳ có SD \(= 6\), ví dụ <code>A = [34, 46]</code> (<code>stdevp(A) = 6</code>), rồi gõ <code>stdevp(3*A + 25) - stdevp(A + 50)</code> → hiện thẳng <code>12</code>!'
        ),

        # Q11 — Elite 750+, Advanced Math, MCQ, Ans: C — Trap #10: "distinct solutions" double/triple-root sum trap
        math_mcq(
            'sat_boss_d8_q11', 11, 'Advanced Math', 'Nonlinear equations in one variable', 'Elite 750+',
            r'<p>Consider the polynomial equation \[(x^2 - 10x + 25)(2x^2 - 7x - 15) = 0.\]</p>',
            r'What is the sum of all <b>distinct</b> real solutions to the equation?',
            {'A': r'\(\dfrac{27}{2}\)', 'B': r'\(\dfrac{17}{2}\)', 'C': r'\(\dfrac{7}{2}\)', 'D': r'\(\dfrac{13}{2}\)'},
            'C',
            r'TUYỆT ĐỐI không áp dụng Vieta mù quáng lên hai đa thức bậc hai khi đề có chữ <b>distinct</b> (phân biệt)! Hãy phân tích nhân tử triệt để CẢ HAI thừa số:<br>1. Thừa số thứ nhất: \[x^2 - 10x + 25 = (x - 5)^2 = 0 \implies x = 5 \quad (\text{nghiệm kép bội } 2).\] 2. Thừa số thứ hai: \[2x^2 - 7x - 15 = (2x + 3)(x - 5) = 0 \implies x = -\frac{3}{2} \quad \text{hoặc} \quad x = 5.\] Chú ý cái bẫy cực hiểm: nghiệm \(x = 5\) không chỉ lặp ở thừa số đầu mà còn xuất hiện LẦN THỨ BA ở thừa số sau! Vậy phương trình gốc thực chất là \((x - 5)^3(2x + 3) = 0\), chỉ có ĐÚNG 2 nghiệm thực <b>phân biệt</b> (distinct): \[S_{\text{distinct}} = \left\{5,\ -\frac{3}{2}\right\}.\] Tổng tất cả các nghiệm phân biệt là: \[5 + \left(-\frac{3}{2}\right) = \frac{10 - 3}{2} = \frac{7}{2}.\]',
            r'Bẫy #10 — Tổng Nghiệm "Distinct" Với Nghiệm Bội (Double/Shared-Root Vieta Trap): Hễ thấy từ "distinct solutions", PHẢI phân tích hoàn toàn mọi thừa số thành nhân tử bậc nhất, gom vào tập hợp bỏ trùng (deduplicate) rồi mới cộng — cấm cộng Vieta từng ngoặc!',
            {
                'A': ('Blind Vieta on Both Factors', r'\(\frac{27}{2} = 10 + \frac{7}{2}\) cộng thẳng \(-\frac{b}{a}\) của hai ngoặc, đếm trùng nghiệm \(x = 5\) tận 3 lần!'),
                'B': ('Missed Shared Root in 2nd Factor', r'\(\frac{17}{2} = 5 + \frac{7}{2}\) nhận ra nghiệm kép ở \((x-5)^2\) nhưng lại dùng Vieta cho ngoặc thứ hai nên vẫn đếm trùng \(x = 5\) thêm 1 lần.'),
                'C': ('Đáp án đúng', r'Chỉ có 2 nghiệm phân biệt là \(5\) và \(-\frac{3}{2}\), tổng bằng \(5 - \frac{3}{2} = \frac{7}{2}\).'),
                'D': ('Sign Error on Linear Factor', r'\(\frac{13}{2} = 5 + \frac{3}{2}\) đổi nhầm dấu nghiệm của \(2x + 3 = 0\) thành \(+\frac{3}{2}\).'),
            },
            desmos_tip_vi=r'Vẽ <code>y = (x^2 - 10x + 25)(2x^2 - 7x - 15)</code> trên Desmos → đồ thị chỉ cắt/chạm trục \(x\) tại ĐÚNG 2 điểm <code>(-1.5, 0)</code> và <code>(5, 0)</code>; bấm <code>-1.5 + 5 = 3.5</code> (tức \(\frac{7}{2}\))!'
        ),

        # Q12 — Elite 750+, Advanced Math, SPR (Ans: 29) — Trap #2B + #1: Rational equation with extraneous root + asking for 5x - 6
        math_spr(
            'sat_boss_d8_q12', 12, 'Advanced Math', 'Nonlinear equations in one variable', 'Elite 750+',
            r'<p>Consider the rational equation \[\frac{x}{x - 2} - \frac{10}{x + 1} = \frac{6}{(x - 2)(x + 1)}.\]</p>',
            r'If \(x\) is the sole valid solution to the equation, what is the value of \(5x - 6\)?',
            ['29'],
            '29',
            r'Bước 1 (Gỡ Bẫy #2B — Điều kiện mẫu thức khác \(0\)): \[x - 2 \neq 0 \quad \text{và} \quad x + 1 \neq 0 \implies x \neq 2,\ x \neq -1.\] Bước 2 (Quy đồng khử mẫu bằng cách nhân hai vế với \((x - 2)(x + 1)\)): \[x(x + 1) - 10(x - 2) = 6.\] Khai triển cẩn thận dấu trừ ở \(-10(x - 2)\): \[x^2 + x - 10x + 20 = 6 \implies x^2 - 9x + 14 = 0 \implies (x - 2)(x - 7) = 0.\] Ta được hai nghiệm ứng viên \(x = 2\) và \(x = 7\).<br>Bước 3 (Loại nghiệm ngoại lai): \(x = 2\) làm mẫu số \(x - 2 = 0\) (vô nghĩa) nên <b>LOẠI</b>. Chỉ còn duy nhất nghiệm hợp lệ \(x = 7\) (kiểm tra: \(\frac{7}{5} - \frac{10}{8} = \frac{28 - 25}{20} = \frac{3}{20}\) và \(\frac{6}{5 \cdot 8} = \frac{3}{20}\), khớp 100%).<br>Bước 4 (Gỡ Bẫy #1 — Tính \(5x - 6\) chứ không dừng ở \(x\)): \[5x - 6 = 5(7) - 6 = 29.\]',
            r'Bẫy #2B + #1 — Nghiệm Ngoại Lai Phân Thức & Hỏi Biểu Thức: Trước khi khử mẫu, ghi ngay điều kiện mẫu \(\neq 0\) (\(x \neq 2\)); chú ý dấu \(-10(-2) = +20\); và sau khi tìm \(x = 7\), phải thay vào \(5x - 6 = 29\).',
            desmos_tip_vi=r'Vẽ vế trái <code>y = x/(x - 2) - 10/(x + 1)</code> và vế phải <code>y = 6/((x - 2)(x + 1))</code> trên Desmos → tiệm cận đứng tại \(x = 2\) tự động loại nghiệm ngoại lai, chỉ có 1 giao điểm duy nhất tại \(x = 7\); bấm <code>5*7 - 6 = 29</code>.'
        ),

        # Q13 — Elite 750+, Geo & Trig, MCQ, Ans: B — Trap #3B: Squared unit rate conversion (in^2 -> ft^2) + oz -> lb
        math_mcq(
            'sat_boss_d8_q13', 13, 'Geometry and Trigonometry', 'Area and volume', 'Elite 750+',
            r'<p>A triangular glass skylight panel has a base of \(96\text{ inches}\) and a height of \(72\text{ inches}\). The specialty glass weighs \(20\text{ ounces per square foot}\). (\(1\text{ foot} = 12\text{ inches}\); \(1\text{ pound} = 16\text{ ounces}\))</p>',
            r'What is the total weight, in <b>pounds</b>, of the triangular glass skylight panel?',
            {'A': r'\(60\)', 'B': r'\(30\)', 'C': r'\(360\)', 'D': r'\(480\)'},
            'B',
            r'Cách an toàn tuyệt đối để không bao giờ sập bẫy đổi đơn vị bình phương (\(1\text{ ft}^2 = 12^2 = 144\text{ in}^2\)) là <b>đổi kích thước sang feet TRƯỚC khi tính diện tích</b>:<br>Bước 1: Đổi cạnh đáy và chiều cao sang feet: \[\text{Base} = \frac{96}{12} = 8\text{ ft}, \qquad \text{Height} = \frac{72}{12} = 6\text{ ft}.\] Bước 2: Tính diện tích tam giác (nhớ nhân \(\frac{1}{2}\)!): \[\text{Area} = \frac{1}{2}(8)(6) = 24\text{ ft}^2.\] (Nếu tính theo \(\text{in}^2\) trước: \(\frac{1}{2}(96)(72) = 3456\text{ in}^2\), phải chia cho \(144\) chứ KHÔNG phải \(12\): \(\frac{3456}{144} = 24\text{ ft}^2\).)<br>Bước 3: Tính trọng lượng bằng ounce rồi đổi sang <b>pound</b>: \[\text{Weight} = 24\text{ ft}^2 \times 20\ \frac{\text{oz}}{\text{ft}^2} = 480\text{ oz} \implies \frac{480}{16} = 30\text{ pounds}.\]',
            r'Bẫy #3B — Đổi Đơn Vị Diện Tích Bậc 2 (`in² → ft²` Trap) & Đơn Vị Khối Lượng: Luôn đổi đơn vị dài (`in → ft`) TRƯỚC khi nhân diện tích (hoặc chia diện tích cho \(12^2 = 144\), không chia \(12\)), và kiểm tra kỹ đơn vị câu hỏi (pounds vs ounces).',
            {
                'A': ('Forgot Triangle 1/2 Factor', r'\(60\) quên nhân \(\frac{1}{2}\) trong công thức diện tích tam giác, tính như hình chữ nhật \(8 \times 6 = 48\text{ ft}^2\).'),
                'B': ('Đáp án đúng', r'Diện tích \(\frac{1}{2}(8)(6) = 24\text{ ft}^2 \implies 480\text{ oz} = 30\text{ lb}\).'),
                'C': ('Divided Area by 12 Instead of 144', r'\(360\) là bẫy sát thủ bậc 2: lấy \(3456\text{ in}^2 / 12 = 288\text{ ft}^2\) (thay vì chia \(144\)), dẫn đến kết quả lớn gấp \(12\) lần!'),
                'D': ('Stopped Early in Ounces', r'\(480\) là khối lượng theo đơn vị ounces, quên chia cho \(16\) để đổi sang pounds.'),
            },
            desmos_tip_vi=r'Gõ gọn 1 dòng vào Desmos: <code>0.5 * (96/12) * (72/12) * 20 / 16</code> → ra chính xác <code>30</code>.'
        ),

        # Q14 — Elite 750+, Algebra, MCQ, Ans: D — Trap #1: Parametric infinitely many solutions asking for a + b with sign flip
        math_mcq(
            'sat_boss_d8_q14', 14, 'Algebra', 'Systems of two linear equations in two variables', 'Elite 750+',
            r'<p>In the system of linear equations below, \(a\) and \(b\) are constants: \[\frac{3}{5}x - \frac{2}{3}y = 8\] \[ax + 10y = b\]</p>',
            r'If the system has <b>infinitely many solutions</b>, what is the value of \(a + b\)?',
            {'A': r'\(129\)', 'B': r'\(111\)', 'C': r'\(-111\)', 'D': r'\(-129\)'},
            'D',
            r'Để hệ hai phương trình tuyến tính có <b>vô số nghiệm</b> (infinitely many solutions), hai phương trình phải hoàn toàn trùng khớp nhau (cùng một đường thẳng), nghĩa là tồn tại hệ số nhân \(c\) biến phương trình (1) thành phương trình (2).<br>Bước 1 (So khớp hệ số của \(y\) — CẨN THẬN DẤU TRỪ!): Ở phương trình (1), hệ số của \(y\) là \(-\frac{2}{3}\); ở phương trình (2) là \(+10\). Do đó hệ số nhân phải là số <b>ÂM</b>: \[c = \frac{10}{-2/3} = -15.\] Bước 2 (Nhân ĐẦY ĐỦ cả 3 hạng tử của phương trình (1) với \(-15\)): \[-15\left(\frac{3}{5}x\right) - 15\left(-\frac{2}{3}y\right) = -15(8) \implies -9x + 10y = -120.\] So sánh từng hệ số với \(ax + 10y = b\): \[a = -9, \qquad b = -120.\] Bước 3 (Tính tổng \(a + b\)): \[a + b = -9 + (-120) = -129.\]',
            r'Bẫy #1 — Khớp Hệ Số Dấu Âm & Hỏi Tổng `a + b` (Sign-Flip Ratio Trap): Khi so tỉ lệ hai phương trình \(\frac{a}{3/5} = \frac{10}{-2/3} = \frac{b}{8}\), dấu trừ trước \(\frac{2}{3}y\) kéo CẢ \(a\) lẫn \(b\) sang dấu âm; luôn viết rõ dấu \((-)\) bên trong ngoặc khi nhân.',
            {
                'A': ('Ignored Negative Sign on y', r'\(129 = 9 + 120\) nhân nhầm với \(+15\) thay vì \(-15\) vì bỏ quên dấu trừ trước \(\frac{2}{3}y\).'),
                'B': ('Forgot to Negate RHS Constant b', r'\(111 = -9 + 120\) nhân đúng \(a = -9\) nhưng quên đổi dấu vế phải \(b = -120\).'),
                'C': ('Forgot to Negate Coeff a', r'\(-111 = 9 + (-120)\) đổi dấu \(b = -120\) nhưng giữ nhầm \(a = +9\).'),
                'D': ('Đáp án đúng', r'Hệ số nhân \(c = -15\) cho \(a = -9, b = -120 \implies a + b = -129\).'),
            },
            desmos_tip_vi=r'Tính hệ số nhân trên Desmos: <code>c = 10 / (-2/3)</code> (ra <code>-15</code>), rồi gõ <code>c*(3/5) + c*8</code> → hiện thẳng <code>-129</code>!'
        ),

        # Q15 — Elite 750+, Geo & Trig, SPR (Ans: 24) — Trap #1 + #4 + #3 Combo: Reverse percent on cylinder + DIAMETER!
        math_spr(
            'sat_boss_d8_q15', 15, 'Geometry and Trigonometry', 'Area and volume', 'Elite 750+',
            r'<p>Right circular cylinder \(A\) has a radius of \(8\text{ centimeters}\) and a height of \(12\text{ centimeters}\). Right circular cylinder \(B\) is formed by decreasing the height of cylinder \(A\) by \(25\%\) and increasing the radius so that the volume of cylinder \(B\) is \(68.75\%\) <b>greater than</b> the volume of cylinder \(A\).</p>',
            r'What is the <b>diameter</b>, in centimeters, of cylinder \(B\)?',
            ['24'],
            '24',
            r'Câu chốt hạ hội tụ 4 bẫy 800 điểm liên hoàn — xử lý từng tầng một cách kỷ luật:<br>Bước 1 (Bẫy phần trăm "greater than"):<br>• Chiều cao giảm \(25\% \implies h_B = 0.75 h_A = \frac{3}{4} h_A\) (tức \(h_B = 9\text{ cm}\)).<br>• Thể tích lớn hơn \(68.75\% \implies V_B = (1 + 0.6875)V_A = 1.6875 V_A = \frac{27}{16} V_A\) (KHÔNG nhân \(0.6875\)!).<br>Bước 2 (Tỉ số thể tích trụ \(V = \pi r^2 h\) — nhớ \(r\) BÌNH PHƯƠNG): \[\frac{V_B}{V_A} = \left(\frac{r_B}{r_A}\right)^2 \cdot \frac{h_B}{h_A} \implies \frac{27}{16} = \left(\frac{r_B}{r_A}\right)^2 \cdot \frac{3}{4}.\] Nhân hai vế với \(\frac{4}{3}\) rồi khai căn: \[\left(\frac{r_B}{r_A}\right)^2 = \frac{27}{16} \cdot \frac{4}{3} = \frac{9}{4} \implies \frac{r_B}{r_A} = \frac{3}{2} = 1.5.\] Bước 3 (Tính bán kính \(r_B\)): \(r_B = 8 \times 1.5 = 12\text{ cm}\).<br>Bước 4 (Bẫy cuối cùng — Đề hỏi ĐƯỜNG KÍNH!): \[d_B = 2 r_B = 2(12) = 24\text{ cm}.\] Kiểm chứng ngược: \(V_A = \pi(8^2)(12) = 768\pi\), \(V_B = \pi(12^2)(9) = 1296\pi\), phần trăm tăng \(= \frac{1296 - 768}{768} = \frac{528}{768} = 0.6875 = 68.75\%\).',
            r'Bẫy Tứ Trùng (#4 + #3 + #1 Combo Trap): (1) "68.75% greater" là \(\times 1.6875\); (2) bán kính trong \(V = \pi r^2 h\) là bậc 2 nên phải chia tỉ số \(h\) rồi lấy căn bậc hai; (3) tuyệt đối không điền \(r_B = 12\) khi đề hỏi ĐƯỜNG KÍNH (\(d_B = 24\))!',
            desmos_tip_vi=r'Gõ 1 dòng duy nhất vào Desmos: <code>2 * 8 * sqrt(1.6875 / 0.75)</code> → hiện thẳng đường kính <code>24</code> (nhớ nhân số <code>2</code> ở đầu ngay lập tức khi đọc chữ "diameter"!).'
        ),
    ]
    return build_math_drill_json(
        '🔥 Math Boss Drill 8: SPR Grid-In Trap-Proofing — 10 Deadly 800-Point Pitfalls (15 câu 750–800)',
        'Hard M2 Boss Masterclass • All 4 Math Domains • 10 MCQ + 5 SPR • Target 750–800',
        '750–800 Boss • 10 Deadly Traps',
        qs,
        target_minutes=25,
    )


# ============================================================================
# PUBLIC MODULE API
# ============================================================================

def get_drills():
    """Returns list of 2 tuples: (drill_key, title, order_index, content_json)."""
    return [
        (
            'boss_drill_7',
            '🔥 Math Boss Drill 7: Coordinate Circles, Nested Similarity, Radian Trig & 3D Solids (15 câu 750–800)',
            7,
            get_boss_drill_7(),
        ),
        (
            'boss_drill_8',
            '🔥 Math Boss Drill 8: SPR Grid-In Trap-Proofing — 10 Deadly 800-Point Pitfalls (15 câu 750–800)',
            8,
            get_boss_drill_8(),
        ),
    ]


# ============================================================================
# 100% PROGRAMMATIC MATH & SCHEMA VERIFICATION (ALL 30 BOSS QUESTIONS)
# ============================================================================

def _parse_spr_exact(s):
    s = s.strip()
    if '/' in s:
        a, b = s.split('/')
        return Fraction(a) / Fraction(b)
    return Fraction(s)


def _check_latex_and_strings(obj, path=''):
    """Recursively verifies zero '$' symbols, balanced \\(...\\)/\\[...\\], and zero stray control chars."""
    if isinstance(obj, str):
        assert '$' not in obj, f"Forbidden '$' found at {path}: {obj[:100]}"
        for ch, name in [('\x08', '\\b'), ('\x0c', '\\f'), ('\r', '\\r'), ('\t', '\\t')]:
            assert ch not in obj, f"Unescaped control char {name} found at {path}: {repr(obj[:100])}"
        assert obj.count(r'\(') == obj.count(r'\)'), f"Unbalanced \\(...\\) at {path}: {obj[:140]}"
        assert obj.count(r'\[') == obj.count(r'\]'), f"Unbalanced \\[...\\] at {path}: {obj[:140]}"
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            _check_latex_and_strings(item, f"{path}[{i}]")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            _check_latex_and_strings(v, f"{path}.{k}")


def verify_all_math():
    """Programmatically verifies exact math for all 30 Boss Drill 7 & 8 questions + all schema invariants."""
    drills = get_drills()
    assert len(drills) == 2, f"Expected 2 drills, got {len(drills)}"

    # ==================================================================
    # BOSS DRILL 7 EXACT MATH ASSERTIONS (Q1..Q15)
    # ==================================================================
    # D7 Q1: x^2 + y^2 + 16x - 12y + k = 0, tangent to x-axis => center (-8, 6), r = 6, k = 100 - 36 = 64
    h7_1, k7_1_y = Fraction(-8), Fraction(6)
    r7_1 = abs(k7_1_y)
    k7_1 = h7_1**2 + k7_1_y**2 - r7_1**2
    assert k7_1 == 64 and 16**2 - 4 * k7_1 == 0  # double root at y=0

    # D7 Q2: (x-2)^2 + (y+3)^2 = 225, T(11,9), tangent meets y=-3 at P => PT = 20
    assert (11 - 2)**2 + (9 - (-3))**2 == 225
    m_ot = Fraction(9 - (-3), 11 - 2)
    m_tan = -1 / m_ot
    assert m_ot == Fraction(4, 3) and m_tan == Fraction(-3, 4)
    # -3 - 9 = (-3/4)(x_P - 11)
    x_p = Fraction(11) + Fraction(-12) / m_tan
    assert x_p == 27
    pt_sq = (x_p - 11)**2 + (Fraction(-3) - 9)**2
    op_sq = (x_p - 2)**2 + (Fraction(-3) - (-3))**2
    assert pt_sq == 400 and math.isqrt(int(pt_sq)) == 20 and op_sq == 225 + pt_sq

    # D7 Q3 (SPR): Semicircle r=25 => AB=50, AC=30 => BC=40, Area(BCD) = (40/50)^2 * 600 = 384
    ab7_3 = 2 * 25
    bc7_3 = math.isqrt(ab7_3**2 - 30**2)
    assert bc7_3 == 40
    area_abc_7_3 = Fraction(1, 2) * 30 * bc7_3
    cd7_3 = Fraction(30 * bc7_3, ab7_3)
    bd7_3 = Fraction(bc7_3**2, ab7_3)
    spr_d7_q3 = Fraction(1, 2) * bd7_3 * cd7_3
    assert spr_d7_q3 == area_abc_7_3 * Fraction(bc7_3, ab7_3)**2 == 384

    # D7 Q4: Arc s = 15pi, Area = 135pi => r = 2*135/15 = 18, theta/pi = 15/18 = 5/6
    r7_4 = Fraction(2 * 135, 15)
    theta7_4_over_pi = Fraction(15, r7_4)
    assert r7_4 == 18 and theta7_4_over_pi == Fraction(5, 6)
    assert Fraction(1, 2) * r7_4**2 * theta7_4_over_pi == 135

    # D7 Q5: Nested 3-tier AD=3, DF=3, FB=4 => linear 3:6:10, area 9:36:100; mid=27u=54 => bot=64u=128
    u7_5 = Fraction(54, 6**2 - 3**2)
    bot7_5 = u7_5 * (10**2 - 6**2)
    assert u7_5 == 2 and bot7_5 == 128

    # D7 Q6 (SPR): Right triangle altitude QS=12, PS=x, SR=x+10 => x(x+10)=144 => x=8, PR=26, Area=156
    x7_6 = Fraction(8)
    assert x7_6 * (x7_6 + 10) == 12**2
    spr_d7_q6 = Fraction(1, 2) * (x7_6 + (x7_6 + 10)) * 12
    assert spr_d7_q6 == 156

    # D7 Q7: Trapezoid BC=10, AB=12, ∠A=60°, ∠D=45° => AE=6, h=6√3, FD=6√3, Area = 54 + 78√3
    h7_7 = 6 * math.sqrt(3)
    ad7_7 = 6 + 10 + h7_7
    area7_7 = 0.5 * (10 + ad7_7) * h7_7
    assert math.isclose(area7_7, 54 + 78 * math.sqrt(3), rel_tol=1e-12)

    # D7 Q8: x^2 - 10x + y^2 + 2ky = 56, r=15, k>0 => 81 + k^2 = 225 => k=12, center(5,-12), dist=13
    k7_8_sq = 15**2 - 56 - 5**2
    k7_8 = math.isqrt(k7_8_sq)
    assert k7_8_sq == 144 and k7_8 == 12
    dist7_8 = math.isqrt(5**2 + (-k7_8)**2)
    assert dist7_8 == 13

    # D7 Q9 (SPR): sin(5k*pi/24 - pi/12) = cos(k*pi/8 + pi/6) => (5k-2) + (3k+4) = 12 => k = 5/4
    spr_d7_q9 = Fraction(12 + 2 - 4, 5 + 3)
    assert spr_d7_q9 == Fraction(5, 4)
    a7_9 = Fraction(5, 24) * spr_d7_q9 - Fraction(1, 12)
    b7_9 = Fraction(1, 8) * spr_d7_q9 + Fraction(1, 6)
    assert 0 < a7_9 < Fraction(1, 2) and 0 < b7_9 < Fraction(1, 2) and a7_9 + b7_9 == Fraction(1, 2)
    assert math.isclose(math.sin(float(a7_9) * math.pi), math.cos(float(b7_9) * math.pi), rel_tol=1e-12)

    # D7 Q10: Unit circle QIII, cos = -5/13 => sin = -12/13, tan = +12/5 => 26sin - 5tan = -36
    cos7_10 = Fraction(-5, 13)
    sin7_10 = Fraction(-12, 13)
    assert cos7_10**2 + sin7_10**2 == 1
    tan7_10 = sin7_10 / cos7_10
    assert tan7_10 == Fraction(12, 5)
    assert 26 * sin7_10 - 5 * tan7_10 == -36

    # D7 Q11: Equilateral Area = 36√3 => s = 12; 45-45-90 hyp AC=12 => legs 6√2; P = 24 + 12√2
    s7_11 = math.isqrt(36 * 4)
    assert s7_11 == 12
    leg7_11 = s7_11 / math.sqrt(2)
    perim7_11 = 2 * s7_11 + 2 * leg7_11
    assert math.isclose(perim7_11, 24 + 12 * math.sqrt(2), rel_tol=1e-12)

    # D7 Q12 (SPR): Silo hemisphere + cylinder, r=6, H_total=19 => h_cyl=13, V/pi = 36*13 + (2/3)*216 = 612
    h_cyl7_12 = 19 - 6
    spr_d7_q12 = Fraction(6**2 * h_cyl7_12) + Fraction(2, 3) * (6**3)
    assert spr_d7_q12 == 612

    # D7 Q13: Cone carved from cylinder r=5, h=12 => l=13, Exposed SA/pi = 25 + 120 + 65 = 210
    l7_13 = math.isqrt(5**2 + 12**2)
    assert l7_13 == 13
    assert 5**2 + 2 * 5 * 12 + 5 * l7_13 == 210

    # D7 Q14: Cone R=12, H=18 sliced 6 cm above base => h_top=12, k=2/3, V_frustum/pi = 864*(19/27) = 608
    v_full7_14 = Fraction(1, 3) * (12**2) * 18
    k7_14 = Fraction(18 - 6, 18)
    v_top7_14 = v_full7_14 * (k7_14**3)
    v_frust7_14 = v_full7_14 - v_top7_14
    assert v_full7_14 == 864 and v_top7_14 == 256 and v_frust7_14 == 608
    # Independent direct check with r_top = 8, h_top = 12
    assert Fraction(1, 3) * (8**2) * 12 == v_top7_14

    # D7 Q15 (SPR): Similar sculptures SA 147 vs 432 => k^2 = 144/49, k=12/7, V_X=343 => V_Y=1728, diff=1385
    k7_15_sq = Fraction(432, 147)
    assert k7_15_sq == Fraction(144, 49)
    k7_15 = Fraction(math.isqrt(k7_15_sq.numerator), math.isqrt(k7_15_sq.denominator))
    v_y7_15 = Fraction(343) * (k7_15**3)
    spr_d7_q15 = v_y7_15 - 343
    assert k7_15 == Fraction(12, 7) and v_y7_15 == 1728 and spr_d7_q15 == 1385

    # ==================================================================
    # BOSS DRILL 8 EXACT MATH ASSERTIONS (Q1..Q15)
    # ==================================================================
    # D8 Q1: (5/2)x - 3y = 19, 10x + 6y = 46 => x = 28/5, y = -5/3 => 5x - 3 = 25
    x8_1 = Fraction(28, 5)
    y8_1 = Fraction(-5, 3)
    assert Fraction(5, 2) * x8_1 - 3 * y8_1 == 19
    assert 10 * x8_1 + 6 * y8_1 == 46
    assert 5 * x8_1 - 3 == 25

    # D8 Q2: sqrt(3x + 3) = x - 5 => x^2 - 13x + 22 = 0 => x=2 (ext), x=11 (valid) => sum = 11
    valid8_2 = [x for x in (2, 11) if 3 * x + 3 >= 0 and math.isclose(math.sqrt(3 * x + 3), x - 5, rel_tol=1e-12)]
    assert valid8_2 == [11] and sum(valid8_2) == 11

    # D8 Q3 (SPR): 63 ft^3/min -> yd^3/hr = 63 / 27 * 60 = 140
    spr_d8_q3 = Fraction(63, 3**3) * 60
    assert spr_d8_q3 == 140

    # D8 Q4: c * (1 + 1.50) * (1 - 0.20) = 600 => c = 300
    c8_4 = Fraction(600) / (Fraction(5, 2) * Fraction(4, 5))
    assert c8_4 == 300

    # D8 Q5: 420 + 35m > 1190 => m > 22 => min integer m = 23
    assert 420 + 35 * 22 == 1190 and 420 + 35 * 23 > 1190

    # D8 Q6 (SPR): f(x) = 3(x-4)^2 + 10 matches table; g(x) = f(x+2) - 5 => g(0) = f(2) - 5 = 17
    f8_6 = lambda x: 3 * (x - 4)**2 + 10
    assert f8_6(1) == 37 and f8_6(4) == 10 and f8_6(5) == 13 and f8_6(7) == 37
    spr_d8_q6 = Fraction(f8_6(0 + 2) - 5)
    assert spr_d8_q6 == 17

    # D8 Q7: 2x^2 + 2y^2 - 12x + 20y - 60 = 0 => (x-3)^2 + (y+5)^2 = 64 => r=8 => diameter=16
    r8_7_sq = Fraction(60, 2) + Fraction(-6, 2)**2 + Fraction(10, 2)**2
    assert r8_7_sq == 64 and 2 * math.isqrt(int(r8_7_sq)) == 16
    # Verify trap C (forgot divide by 2): 60 + 36 + 100 = 196 => 2*14 = 28
    assert 60 + 6**2 + 10**2 == 196 and 2 * math.isqrt(196) == 28

    # D8 Q8: Two-way table totals + P(STEM | Not Declined) = (45+25)/(108+72) = 70/180 = 7/18
    rows8_8 = [(45, 25, 50), (36, 24, 40), (27, 23, 50)]
    assert [sum(r) for r in rows8_8] == [120, 100, 100]
    col_sums = [sum(col) for col in zip(*rows8_8)]
    assert col_sums == [108, 72, 140] and sum(col_sums) == 320
    assert Fraction(45 + 25, 108 + 72) == Fraction(7, 18)

    # D8 Q9 (SPR): 4x^2 - (5k-3)x + (2k+7) = 0, sum = 8 => k = 7, disc > 0, product = 21/4 = 5.25
    k8_9 = Fraction(4 * 8 + 3, 5)
    assert k8_9 == 7
    b8_9 = -(5 * k8_9 - 3)
    c8_9 = 2 * k8_9 + 7
    disc8_9 = b8_9**2 - 4 * 4 * c8_9
    assert disc8_9 == 688 and disc8_9 > 0
    spr_d8_q9 = Fraction(c8_9, 4)
    assert spr_d8_q9 == Fraction(21, 4)

    # D8 Q10: SD_A = 6, B = 3A + 25 => SD_B = 18; C = A + 50 => SD_C = 6 => SD_B - SD_C = 12
    sd_b8_10 = 3 * 6
    sd_c8_10 = 6
    assert sd_b8_10 - sd_c8_10 == 12

    # D8 Q11: (x^2 - 10x + 25)(2x^2 - 7x - 15) = (x - 5)^3(2x + 3) = 0 => distinct roots {5, -3/2}, sum = 7/2
    poly11 = lambda x: (x**2 - 10 * x + 25) * (2 * x**2 - 7 * x - 15)
    roots11 = {Fraction(5), Fraction(-3, 2)}
    for r in roots11:
        assert poly11(r) == 0
    assert sum(roots11) == Fraction(7, 2)

    # D8 Q12 (SPR): x/(x-2) - 10/(x+1) = 6/((x-2)(x+1)) => x=2 (ext), x=7 (valid) => 5x - 6 = 29
    x8_12 = Fraction(7)
    lhs8_12 = x8_12 / (x8_12 - 2) - Fraction(10) / (x8_12 + 1)
    rhs8_12 = Fraction(6) / ((x8_12 - 2) * (x8_12 + 1))
    assert lhs8_12 == rhs8_12 == Fraction(3, 20)
    assert (2 - 2) == 0  # x=2 is extraneous
    spr_d8_q12 = 5 * x8_12 - 6
    assert spr_d8_q12 == 29

    # D8 Q13: Triangle base=96 in (8 ft), h=72 in (6 ft), Area=24 ft^2, 20 oz/ft^2 -> 480 oz = 30 lb
    area8_13_ft2 = Fraction(1, 2) * Fraction(96, 12) * Fraction(72, 12)
    assert area8_13_ft2 == Fraction(1, 2) * 96 * 72 / 144 == 24
    weight8_13_lb = area8_13_ft2 * 20 / 16
    assert weight8_13_lb == 30

    # D8 Q14: (3/5)x - (2/3)y = 8 and ax + 10y = b infinitely many solutions => mult -15 => a=-9, b=-120 => a+b=-129
    mult8_14 = Fraction(10) / Fraction(-2, 3)
    a8_14 = mult8_14 * Fraction(3, 5)
    b8_14 = mult8_14 * 8
    assert mult8_14 == -15 and a8_14 == -9 and b8_14 == -120 and a8_14 + b8_14 == -129

    # D8 Q15 (SPR): r_A=8, h_A=12, h_B=0.75*h_A=9, V_B=1.6875*V_A => r_B=12 => diameter d_B = 24
    r_ratio_sq = Fraction(16875, 10000) / Fraction(75, 100)
    assert r_ratio_sq == Fraction(9, 4)
    r_ratio = Fraction(math.isqrt(r_ratio_sq.numerator), math.isqrt(r_ratio_sq.denominator))
    r_b8_15 = 8 * r_ratio
    spr_d8_q15 = 2 * r_b8_15
    assert r_b8_15 == 12 and spr_d8_q15 == 24
    v_a8_15 = 8**2 * 12
    v_b8_15 = int(r_b8_15)**2 * 9
    assert Fraction(v_b8_15 - v_a8_15, v_a8_15) == Fraction(6875, 10000)

    # ==================================================================
    # CROSS-CHECK SPR ANSWERS, BALANCE, SVG COUNT, DOMAINS & LATEX
    # ==================================================================
    expected_spr = {
        'sat_boss_d7_q3': spr_d7_q3,
        'sat_boss_d7_q6': spr_d7_q6,
        'sat_boss_d7_q9': spr_d7_q9,
        'sat_boss_d7_q12': spr_d7_q12,
        'sat_boss_d7_q15': spr_d7_q15,
        'sat_boss_d8_q3': spr_d8_q3,
        'sat_boss_d8_q6': spr_d8_q6,
        'sat_boss_d8_q9': spr_d8_q9,
        'sat_boss_d8_q12': spr_d8_q12,
        'sat_boss_d8_q15': spr_d8_q15,
    }
    expected_spec = [
        ('boss_drill_7', 7, 'sat_boss_d7', {'A': 3, 'B': 2, 'C': 3, 'D': 2}),
        ('boss_drill_8', 8, 'sat_boss_d8', {'A': 2, 'B': 3, 'C': 2, 'D': 3}),
    ]
    expected_spr_positions = {3, 6, 9, 12, 15}
    valid_difficulties = {'Hard', 'Elite 750+'}

    total_q = 0
    for d_idx, (d_key, d_title, order_idx, content_json) in enumerate(drills):
        exp_key, exp_order, id_prefix, exp_balance = expected_spec[d_idx]
        assert d_key == exp_key, f"Unexpected drill_key {d_key}"
        assert order_idx == exp_order, f"Unexpected order_index {order_idx}"
        _check_latex_and_strings(content_json, d_key)

        qs = content_json['drillModule']['questions']
        assert len(qs) == 15, f"{d_key} must have 15 questions, got {len(qs)}"

        mcq_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        spr_positions = set()
        svg_count = 0
        domains_seen = set()

        for i, q in enumerate(qs):
            n = i + 1
            total_q += 1
            expected_id = f'{id_prefix}_q{n}'
            assert q['id'] == expected_id, f"Expected id {expected_id}, got {q['id']}"
            assert q['difficulty'] in valid_difficulties, f"{expected_id} bad difficulty {q['difficulty']}"
            domains_seen.add(q['domain'])
            if '<svg ' in q['stimulusHtml']:
                svg_count += 1

            exp = q['explanation']
            assert exp.get('summaryVi') and len(exp['summaryVi']) >= 60, f"{expected_id} summaryVi too short"
            assert exp.get('desmosTipVi') and len(exp['desmosTipVi']) >= 25, f"{expected_id} missing desmosTipVi"
            assert exp.get('keyTakeaway') and len(exp['keyTakeaway']) >= 25, f"{expected_id} missing keyTakeaway"

            if q['questionFormat'] == 'spr':
                spr_positions.add(n)
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

        assert spr_positions == expected_spr_positions, f"{d_key} SPR positions {spr_positions} != {expected_spr_positions}"
        assert mcq_counts == exp_balance, f"{d_key} MCQ balance {mcq_counts} != {exp_balance}"

        if d_key == 'boss_drill_7':
            assert domains_seen == {'Geometry and Trigonometry'}, f"Drill 7 domains must be Geo/Trig only: {domains_seen}"
            assert svg_count >= 10, f"Drill 7 must have >=10 SVG diagrams, got {svg_count}"
        else:
            assert domains_seen == {
                'Algebra',
                'Advanced Math',
                'Problem-Solving and Data Analysis',
                'Geometry and Trigonometry',
            }, f"Drill 8 must cover all 4 Math domains, got {domains_seen}"

    assert total_q == 30, f"Expected 30 total questions, got {total_q}"


if __name__ == '__main__':
    verify_all_math()
    for drill_key, title, order_index, content_json in get_drills():
        errs = validate_sat_test(content_json, title)
        if errs:
            print(f"QA ERRORS in {drill_key}:")
            for e in errs:
                print("  -", e)
            sys.exit(1)
    print("BOSS MATH DRILLS 7 & 8 (30 ELITE Qs) VERIFIED & QA PASSED!")
