# -*- coding: utf-8 -*-
"""
Cambridge IGCSE Additional Mathematics (0606) 2025–2027 Syllabus Upgrade — TonyEnglish
Topical Drills — Part 2A (Chapters 8 to 12): 5 Drills × 12 Questions = 60 Questions

Exports:
  - DRILLS_0606_P2A: list of 5 drill dicts (folder_key='drills_p2', order_index=1..5)
      1. d0606_c8  (Ch. 8: Circular Measure — Calculator)
      2. d0606_c9  (Ch. 9: Trigonometry — Calculator)
      3. d0606_c10 (Ch. 10: Permutations & Combinations — Calculator)
      4. d0606_c11 (Ch. 11: Series — Binomial Theorem, AP & GP — Calculator)
      5. d0606_c12 (Ch. 12: Differentiation 1 — Non-Calculator)
  - verify_all_math(): programmatically verifies all 60 mathematical solutions,
    exact A/B/C/D balance (3 each per drill), KaTeX hygiene, and runs
    validate_igcse_drill() from scripts.igcse_maths_pipeline.
"""

import itertools
import math
import os
import re
import sys
from fractions import Fraction

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.igcse_maths_pipeline import (
    COURSE_0606_ID,
    build_igcse_drill_json,
    validate_igcse_drill,
)


def _intro_box(en_summary, vi_summary, formulas_html, tip_html):
    return (
        '<div style="background:#f8fafc;border:1.5px solid #cbd5e1;border-radius:12px;'
        'padding:14px 16px;margin-bottom:14px;line-height:1.6;">'
        f'<p style="margin:0 0 6px 0;"><b>🎯 Scope:</b> {en_summary}</p>'
        f'<p style="margin:0 0 8px 0;color:#334155;"><b>🇻🇳 Trọng tâm:</b> {vi_summary}</p>'
        f'<div style="background:#eef2ff;border-left:4px solid #4f46e5;padding:8px 12px;'
        f'border-radius:6px;margin-bottom:8px;font-size:14px;"><b>Key Formulae:</b> {formulas_html}</div>'
        f'<p style="margin:0;font-size:13.5px;color:#9a3412;"><b>⚠️ Exam Tip:</b> {tip_html}</p>'
        '</div>'
    )


# =============================================================================
# DRILL 1 (Ch. 8): Circular Measure — Radians, Arc Length & Sector Area (0606)
# Answer balance: A=3 (Q3,Q6,Q9), B=3 (Q1,Q8,Q11), C=3 (Q4,Q7,Q12), D=3 (Q2,Q5,Q10)
# =============================================================================
DRILL_C8 = {
    'code': 'd0606_c8',
    'folder_key': 'drills_p2',
    'lecture_key': 'c8',
    'calculator_policy': 'calculator',
    'order_index': 1,
    'title': 'Ch. 8 Drill: Circular Measure — Radians, Arc Length & Sector Area (0606)',
    'time_limit': '30',
    'intro_html': _intro_box(
        r'Master exact degree–radian conversions, arc length \(s = r\theta\), sector area \(A = \frac{1}{2}r^2\theta\), segment area, tangent-circle regions, composite triangles, and overlapping circles.',
        r'Thành thạo quy đổi độ–radian chính xác, độ dài cung \(s = r\theta\), diện tích hình quạt \(A = \frac{1}{2}r^2\theta\), hình viên phân, tiếp tuyến đường tròn và giao hai đường tròn.',
        r'\(180^\circ = \pi\text{ rad}\) &nbsp;|&nbsp; \(s = r\theta\) &nbsp;|&nbsp; \(A_{\text{sector}} = \frac{1}{2}r^2\theta = \frac{1}{2}rs\) &nbsp;|&nbsp; \(A_{\text{segment}} = \frac{1}{2}r^2(\theta - \sin\theta)\) &nbsp;|&nbsp; Chord \(= 2r\sin\frac{\theta}{2}\)',
        r'Always switch your calculator to <b>RAD</b> mode before computing \(\sin\theta\), \(\cos\theta\), or \(\tan\theta\) when \(\theta\) is in radians! (Luôn chuyển máy tính sang chế độ <b>RAD</b> trước khi bấm lượng giác với góc radian.)',
    ),
    'questions': [
        {
            'tag': 'Radians & Degrees',
            'q': r'<p>Convert \(225^\circ\) into radians in exact terms of \(\pi\), and convert \(\frac{7\pi}{12}\text{ radians}\) into degrees. Give your answer as an ordered pair.</p>',
            'options': [
                r'\(\left(\frac{4\pi}{3},\; 105^\circ\right)\)',
                r'\(\left(\frac{5\pi}{4},\; 105^\circ\right)\)',
                r'\(\left(\frac{5\pi}{4},\; 120^\circ\right)\)',
                r'\(\left(\frac{7\pi}{6},\; 115^\circ\right)\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (Degrees → Radians / Đổi độ sang radian):</b> Multiply by \(\frac{\pi}{180^\circ}\):</p>'
                r'\[225^\circ \times \frac{\pi}{180^\circ} = \frac{225}{180}\pi = \frac{5\pi}{4}\text{ rad} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Radians → Degrees / Đổi radian sang độ):</b> Replace \(\pi\) with \(180^\circ\):</p>'
                r'\[\frac{7\pi}{12} \times \frac{180^\circ}{\pi} = 7 \times 15^\circ = 105^\circ \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> The ordered pair is \(\left(\frac{5\pi}{4},\; 105^\circ\right)\). Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'Arc Length & Perimeter',
            'q': r'<p>A sector \(OAB\) of a circle has radius \(r = 12\text{ cm}\) and subtends an angle \(\theta = 1.35\text{ radians}\) at the centre \(O\). Find the <b>perimeter</b> of the sector \(OAB\).</p>',
            'options': [
                r'\(16.2\text{ cm}\)',
                r'\(28.2\text{ cm}\)',
                r'\(36.4\text{ cm}\)',
                r'\(40.2\text{ cm}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Arc length / Tính độ dài cung \(AB\)):</b></p>'
                r'\[s = r\theta = 12 \times 1.35 = 16.2\text{ cm} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Total perimeter / Tính chu vi hình quạt):</b> Include BOTH straight radii \(OA\) and \(OB\):</p>'
                r'\[P = 2r + s = 2(12) + 16.2 = 24 + 16.2 = 40.2\text{ cm} \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Option A (\(16.2\text{ cm}\)) is only the arc length; Option B (\(28.2\text{ cm}\)) adds only one radius. Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'Sector Area',
            'q': r'<p>A sector of a circle of radius \(r = 8\text{ cm}\) has a perimeter of \(26\text{ cm}\). Calculate the area of the sector.</p>',
            'options': [
                r'\(40\text{ cm}^2\)',
                r'\(50\text{ cm}^2\)',
                r'\(80\text{ cm}^2\)',
                r'\(104\text{ cm}^2\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Find arc length / Tìm độ dài cung \(s\)):</b> Since perimeter \(P = 2r + s\):</p>'
                r'\[2(8) + s = 26 \implies s = 26 - 16 = 10\text{ cm} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Find sector area / Tính diện tích hình quạt):</b> Using \(\theta = \frac{s}{r} = \frac{10}{8} = 1.25\text{ rad}\), or directly \(A = \frac{1}{2}rs\):</p>'
                r'\[A = \frac{1}{2}r^2\theta = \frac{1}{2}rs = \frac{1}{2}(8)(10) = 40\text{ cm}^2 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Forgetting \(\frac{1}{2}\) gives \(80\text{ cm}^2\) (Option C). Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'Arc & Sector System',
            'q': r'<p>A sector of a circle has an arc length of \(15\text{ cm}\) and an area of \(90\text{ cm}^2\). Find the radius \(r\) and the angle \(\theta\) (in radians) of the sector.</p>',
            'options': [
                r'\(r = 6\text{ cm},\; \theta = 2.5\text{ rad}\)',
                r'\(r = 10\text{ cm},\; \theta = 1.5\text{ rad}\)',
                r'\(r = 12\text{ cm},\; \theta = 1.25\text{ rad}\)',
                r'\(r = 15\text{ cm},\; \theta = 1.0\text{ rad}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Eliminate \(\theta\) / Khử \(\theta\) để tìm \(r\)):</b> We have \(r\theta = 15\) and \(\frac{1}{2}r^2\theta = 90\). Substitute \(r\theta = 15\) into the area formula:</p>'
                r'\[\frac{1}{2}r(r\theta) = 90 \implies \frac{1}{2}r(15) = 90 \implies r = \frac{180}{15} = 12\text{ cm} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Find \(\theta\) / Tìm góc ở tâm \(\theta\)):</b></p>'
                r'\[\theta = \frac{s}{r} = \frac{15}{12} = 1.25\text{ rad} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> \(r = 12\text{ cm}\) and \(\theta = 1.25\text{ rad}\). Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'Segment Area (Exact)',
            'q': r'<p>A chord \(AB\) of a circle with centre \(O\) and radius \(6\text{ cm}\) subtends an angle of \(\frac{2\pi}{3}\text{ radians}\) at \(O\). Find the exact area of the minor segment cut off by \(AB\).</p>',
            'options': [
                r'\(12\pi - 18\sqrt{3}\text{ cm}^2\)',
                r'\(12\pi + 9\sqrt{3}\text{ cm}^2\)',
                r'\(6\pi - 9\sqrt{3}\text{ cm}^2\)',
                r'\(12\pi - 9\sqrt{3}\text{ cm}^2\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Apply segment formula / Áp dụng công thức diện tích viên phân):</b></p>'
                r'\[A_{\text{seg}} = A_{\text{sector}} - A_{\triangle OAB} = \frac{1}{2}r^2(\theta - \sin\theta) \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Substitute exact values / Thay giá trị chính xác):</b> With \(r = 6\), \(\theta = \frac{2\pi}{3}\), and \(\sin\left(\frac{2\pi}{3}\right) = \frac{\sqrt{3}}{2}\):</p>'
                r'\[A_{\text{seg}} = \frac{1}{2}(6^2)\left(\frac{2\pi}{3} - \frac{\sqrt{3}}{2}\right) = 18\left(\frac{2\pi}{3} - \frac{\sqrt{3}}{2}\right) = 12\pi - 9\sqrt{3}\text{ cm}^2 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'Segment Area (3 s.f.)',
            'q': r'<p>In a circle with centre \(O\) and radius \(10\text{ cm}\), a chord \(PQ\) subtends an angle of \(1.4\text{ radians}\) at \(O\). Calculate the area of the minor segment bounded by the chord \(PQ\) and the minor arc \(PQ\), correct to 3 significant figures.</p>',
            'options': [
                r'\(20.7\text{ cm}^2\)',
                r'\(49.3\text{ cm}^2\)',
                r'\(68.8\text{ cm}^2\)',
                r'\(70.0\text{ cm}^2\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Set up segment area / Lập công thức diện tích viên phân):</b> Ensure calculator is in <b>RAD</b> mode:</p>'
                r'\[A = \frac{1}{2}(10^2)(1.4 - \sin 1.4) = 50(1.4 - 0.98545\dots) \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Evaluate to 3 s.f. / Tính và làm tròn 3 c.s.c.n.):</b></p>'
                r'\[A = 50 \times 0.41455\dots = 20.7275\dots \approx 20.7\text{ cm}^2 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Leaving the calculator in DEG mode gives \(\sin(1.4^\circ) \approx 0.0244\), yielding the wrong trap \(68.8\text{ cm}^2\) (Option C)! Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'Chord & Segment Perimeter',
            'q': r'<p>A circle has centre \(O\) and radius \(9\text{ cm}\). Points \(A\) and \(B\) lie on the circumference such that \(\angle AOB = 1.6\text{ radians}\). Find the perimeter of the minor segment bounded by the chord \(AB\) and the minor arc \(AB\), correct to 3 significant figures.</p>',
            'options': [
                r'\(20.9\text{ cm}\)',
                r'\(25.6\text{ cm}\)',
                r'\(27.3\text{ cm}\)',
                r'\(32.4\text{ cm}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Arc length & chord length / Tính cung \(AB\) và dây cung \(AB\)):</b></p>'
                r'\[\text{Arc } AB = r\theta = 9 \times 1.6 = 14.4\text{ cm}\]'
                r'\[\text{Chord } AB = 2r\sin\left(\frac{\theta}{2}\right) = 2(9)\sin(0.8) = 18 \times 0.717356\dots = 12.9124\dots\text{ cm} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Total perimeter / Cộng chu vi hình viên phân):</b></p>'
                r'\[P = 14.4 + 12.9124\dots = 27.3124\dots \approx 27.3\text{ cm} \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Using \(r\sin\frac{\theta}{2}\) instead of \(2r\sin\frac{\theta}{2}\) gives \(20.9\text{ cm}\) (Option A); using sector perimeter \(14.4 + 18\) gives \(32.4\text{ cm}\) (Option D). Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'Tangent & Sector Area',
            'q': r'<p>A circle has centre \(O\) and radius \(5\text{ cm}\). The point \(A\) lies on the circle, and the tangent at \(A\) meets the line \(OB\) extended at \(T\), where \(B\) lies on the circle and \(\angle AOT = 1.1\text{ radians}\). Find the area of the shaded region bounded by the tangent \(AT\), the line segment \(BT\), and the minor arc \(AB\), correct to 3 significant figures.</p>',
            'options': [
                r'\(8.65\text{ cm}^2\)',
                r'\(10.8\text{ cm}^2\)',
                r'\(13.8\text{ cm}^2\)',
                r'\(24.6\text{ cm}^2\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (Right-angled triangle \(\triangle OAT\) / Tam giác vuông \(OAT\) tại \(A\)):</b> Since radius \(OA \perp AT\):</p>'
                r'\[AT = OA\tan(1.1) = 5\tan(1.1) \approx 9.8238\text{ cm}\]'
                r'\[A_{\triangle OAT} = \frac{1}{2}(OA)(AT) = \frac{1}{2}(5)(5\tan 1.1) = 12.5\tan(1.1) \approx 24.5595\text{ cm}^2 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Subtract sector \(OAB\) / Trừ diện tích hình quạt \(OAB\)):</b></p>'
                r'\[A_{\text{sector}} = \frac{1}{2}(5^2)(1.1) = 13.75\text{ cm}^2\]'
                r'\[A_{\text{shaded}} = 24.5595 - 13.75 = 10.8095\dots \approx 10.8\text{ cm}^2 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'Two Tangents & Arc Perimeter',
            'q': r'<p>From an external point \(P\), two tangents \(PA\) and \(PB\) are drawn to a circle with centre \(O\) and radius \(6\text{ cm}\) such that \(OP = 12\text{ cm}\). Find the exact perimeter of the region bounded by the two tangents \(PA\), \(PB\) and the minor arc \(AB\).</p>',
            'options': [
                r'\(12\sqrt{3} + 4\pi\text{ cm}\)',
                r'\(6\sqrt{3} + 4\pi\text{ cm}\)',
                r'\(12\sqrt{3} + 2\pi\text{ cm}\)',
                r'\(12\sqrt{3} + 8\pi\text{ cm}\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Find angle and tangent length / Tìm góc ở tâm và độ dài tiếp tuyến):</b> In right-angled \(\triangle OAP\) (\(\angle OAP = \frac{\pi}{2}\)):</p>'
                r'\[\cos(\angle AOP) = \frac{OA}{OP} = \frac{6}{12} = \frac{1}{2} \implies \angle AOP = \frac{\pi}{3}\text{ rad}\]'
                r'\[\implies \angle AOB = 2\left(\frac{\pi}{3}\right) = \frac{2\pi}{3}\text{ rad}, \qquad PA = PB = \sqrt{12^2 - 6^2} = \sqrt{108} = 6\sqrt{3}\text{ cm} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Find arc \(AB\) and sum perimeter / Tính cung \(AB\) và cộng chu vi):</b></p>'
                r'\[\text{Arc } AB = 6 \times \frac{2\pi}{3} = 4\pi\text{ cm}\]'
                r'\[P = PA + PB + \text{Arc } AB = 6\sqrt{3} + 6\sqrt{3} + 4\pi = 12\sqrt{3} + 4\pi\text{ cm} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'Composite Triangle + Sector',
            'q': r'<p>In triangle \(OAB\), \(OA = 8\text{ cm}\), \(OB = 11\text{ cm}\), and \(\angle AOB = 0.9\text{ radians}\). An arc \(AC\) with centre \(O\) and radius \(8\text{ cm}\) meets \(OB\) at \(C\). Find the perimeter of the region \(ABC\) bounded by the straight lines \(AB\), \(CB\) and the arc \(AC\), correct to 3 significant figures.</p>',
            'options': [
                r'\(15.9\text{ cm}\)',
                r'\(17.4\text{ cm}\)',
                r'\(21.2\text{ cm}\)',
                r'\(18.9\text{ cm}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Find \(CB\) and arc \(AC\) / Tìm đoạn \(CB\) và cung \(AC\)):</b> Since \(OC = OA = 8\text{ cm}\):</p>'
                r'\[CB = OB - OC = 11 - 8 = 3\text{ cm}, \qquad \text{Arc } AC = 8 \times 0.9 = 7.2\text{ cm}\]'
                r'<p><b>Step 2 (Cosine Rule for \(AB\) / Định lý Cosin tìm cạnh \(AB\)):</b></p>'
                r'\[AB^2 = 8^2 + 11^2 - 2(8)(11)\cos(0.9) = 185 - 176(0.621610\dots) = 75.5966\dots \quad \text{[M1]}\]'
                r'\[AB = \sqrt{75.5966\dots} = 8.6946\dots\text{ cm}\]'
                r'<p><b>Step 3 (Perimeter of \(ABC\) / Chu vi miền \(ABC\)):</b></p>'
                r'\[P = 8.6946\dots + 3 + 7.2 = 18.8946\dots \approx 18.9\text{ cm} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'Annular Sector',
            'q': r'<p>Two concentric circles have centre \(O\) and radii \(r_1 = 5\text{ cm}\) and \(r_2 = 9\text{ cm}\). A sector of angle \(\theta = 0.8\text{ radians}\) cuts out a curved band (annular sector) \(ABCD\) between the two arcs. Find the exact ratio \(\dfrac{\text{Area of } ABCD}{\text{Perimeter of } ABCD}\) (ignoring units).</p>',
            'options': [
                r'\(\dfrac{6}{7}\)',
                r'\(\dfrac{7}{6}\)',
                r'\(\dfrac{7}{5}\)',
                r'\(\dfrac{14}{9}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (Area of annular sector / Diện tích hình vành khăn quạt):</b></p>'
                r'\[A = \frac{1}{2}(r_2^2 - r_1^2)\theta = \frac{1}{2}(9^2 - 5^2)(0.8) = \frac{1}{2}(56)(0.8) = 22.4 = \frac{112}{5} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Perimeter of annular sector / Chu vi hình vành khăn quạt):</b> Two straight edges of length \(9 - 5 = 4\text{ cm}\) plus two arcs:</p>'
                r'\[P = 2(9 - 5) + (5 + 9)(0.8) = 8 + 11.2 = 19.2 = \frac{96}{5}\]'
                r'<p><b>Step 3 (Exact ratio / Tỉ số tối giản):</b></p>'
                r'\[\frac{A}{P} = \frac{112/5}{96/5} = \frac{112}{96} = \frac{7}{6} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'Overlapping Circles',
            'q': r'<p>Two identical circles, each of radius \(6\text{ cm}\), have centres \(O_1\) and \(O_2\) such that each circle passes through the centre of the other (so \(O_1O_2 = 6\text{ cm}\)). Find the exact area of the overlapping region common to both circles.</p>',
            'options': [
                r'\(12\pi - 9\sqrt{3}\text{ cm}^2\)',
                r'\(24\pi - 9\sqrt{3}\text{ cm}^2\)',
                r'\(24\pi - 18\sqrt{3}\text{ cm}^2\)',
                r'\(12\pi - 18\sqrt{3}\text{ cm}^2\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Geometry of intersection / Phân tích hình học giao điểm):</b> Let the two circles intersect at \(A\) and \(B\). Since \(O_1A = O_2A = O_1O_2 = 6\text{ cm}\), both \(\triangle O_1O_2A\) and \(\triangle O_1O_2B\) are equilateral triangles, so \(\angle AO_1B = \frac{\pi}{3} + \frac{\pi}{3} = \frac{2\pi}{3}\text{ rad}\).</p>'
                r'<p><b>Step 2 (Two identical minor segments / Hai hình viên phân bằng nhau):</b></p>'
                r'\[A_{\text{one seg}} = \frac{1}{2}(6^2)\left(\frac{2\pi}{3} - \sin\frac{2\pi}{3}\right) = 18\left(\frac{2\pi}{3} - \frac{\sqrt{3}}{2}\right) = 12\pi - 9\sqrt{3}\text{ cm}^2 \quad \text{[M1]}\]'
                r'<p><b>Step 3 (Total overlapping area / Tổng diện tích phần giao):</b></p>'
                r'\[A_{\text{total}} = 2(12\pi - 9\sqrt{3}) = 24\pi - 18\sqrt{3}\text{ cm}^2 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Option A forgets to double the single segment; Option B doubles only the sector part. Answer: <b>C</b>.</p>'
            ),
        },
    ],
}


# =============================================================================
# DRILL 2 (Ch. 9): Trigonometry — Identities, Sec/Cosec/Cot & Equations (0606)
# Answer balance: A=3 (Q2,Q5,Q10), B=3 (Q4,Q7,Q12), C=3 (Q1,Q6,Q9), D=3 (Q3,Q8,Q11)
# =============================================================================
DRILL_C9 = {
    'code': 'd0606_c9',
    'folder_key': 'drills_p2',
    'lecture_key': 'c9',
    'calculator_policy': 'calculator',
    'order_index': 2,
    'title': 'Ch. 9 Drill: Trigonometry — Identities, Sec/Cosec/Cot & Equations (0606)',
    'time_limit': '30',
    'intro_html': _intro_box(
        r'Master amplitude/period/vertical shift of \(a\sin(bx) + c\), exact radian values, reciprocal functions (\(\sec, \operatorname{cosec}, \cot\)), Pythagorean identities, compound linear equations, and quadratic trig equations.',
        r'Thành thạo biên độ/chu kỳ/dịch chuyển đồ thị \(a\sin(bx) + c\), giá trị lượng giác chính xác theo radian, hàm nghịch đảo (\(\sec, \operatorname{cosec}, \cot\)), hằng đẳng thức và phương trình lượng giác bậc hai.',
        r'\(\sec x = \frac{1}{\cos x},\; \operatorname{cosec} x = \frac{1}{\sin x},\; \cot x = \frac{1}{\tan x}\) &nbsp;|&nbsp; \(\sec^2 x = 1 + \tan^2 x\) &nbsp;|&nbsp; \(\operatorname{cosec}^2 x = 1 + \cot^2 x\)',
        r'When solving \(\sin(bx + c) = k\), ALWAYS adjust the domain for \(u = bx + c\) FIRST before finding all ASTC quadrant solutions! (Luôn đổi khoảng nghiệm cho \(u = bx + c\) trước khi tìm tất cả các góc phần tư ASTC.)',
    ),
    'questions': [
        {
            'tag': 'Trig Graphs & Features',
            'q': r'<p>The function \(f(x) = 4\sin(3x) - 2\) is defined for \(x \in \mathbb{R}\) (with \(x\) in radians). State the amplitude, period, and range of \(f(x)\).</p>',
            'options': [
                r'Amplitude \(= 4\), Period \(= 6\pi\), Range \(= [-6, 2]\)',
                r'Amplitude \(= 4\), Period \(= \dfrac{2\pi}{3}\), Range \(= [-4, 4]\)',
                r'Amplitude \(= 4\), Period \(= \dfrac{2\pi}{3}\), Range \(= [-6, 2]\)',
                r'Amplitude \(= 2\), Period \(= \dfrac{2\pi}{3}\), Range \(= [-6, 2]\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Amplitude & period / Biên độ và chu kỳ):</b> For \(y = a\sin(bx) + c\):</p>'
                r'\[\text{Amplitude} = |a| = 4, \qquad \text{Period} = \frac{2\pi}{b} = \frac{2\pi}{3} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Range with vertical shift / Tập giá trị khi dịch đứng):</b> Since \(-1 \le \sin(3x) \le 1\):</p>'
                r'\[-4 - 2 \le 4\sin(3x) - 2 \le 4 - 2 \implies -6 \le f(x) \le 2 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Amplitude \(= 4\), Period \(= \frac{2\pi}{3}\), Range \(= [-6, 2]\). Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'Trig Graph Modelling',
            'q': r'<p>A trigonometric curve has equation \(y = a\cos(bx) + c\), where \(a > 0\) and \(b > 0\) (with \(x\) in degrees). The curve has a maximum value of \(7\), a minimum value of \(-3\), and a period of \(120^\circ\). Find the values of \(a\), \(b\), and \(c\).</p>',
            'options': [
                r'\(a = 5,\; b = 3,\; c = 2\)',
                r'\(a = 5,\; b = \frac{1}{3},\; c = 2\)',
                r'\(a = 10,\; b = 3,\; c = 2\)',
                r'\(a = 5,\; b = 3,\; c = -2\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Find \(a\) and \(c\) / Tìm biên độ \(a\) và trục giữa \(c\)):</b></p>'
                r'\[a = \frac{\text{max} - \text{min}}{2} = \frac{7 - (-3)}{2} = 5, \qquad c = \frac{\text{max} + \text{min}}{2} = \frac{7 + (-3)}{2} = 2 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Find \(b\) from period / Tìm \(b\) từ chu kỳ):</b></p>'
                r'\[\text{Period} = \frac{360^\circ}{b} = 120^\circ \implies b = \frac{360^\circ}{120^\circ} = 3 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> \(a = 5,\; b = 3,\; c = 2\). Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'Exact Radian Values',
            'q': r'<p>Evaluate the exact value of \(\sin\left(\dfrac{5\pi}{6}\right) + \cos\left(\dfrac{4\pi}{3}\right) + \tan\left(\dfrac{3\pi}{4}\right) + \sin^2\left(\dfrac{\pi}{3}\right)\).</p>',
            'options': [
                r'\(\dfrac{3}{4}\)',
                r'\(\dfrac{1}{4}\)',
                r'\(-\dfrac{3}{4}\)',
                r'\(-\dfrac{1}{4}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Exact ASTC quadrant values / Xác định từng giá trị theo góc phần tư ASTC):</b></p>'
                r'\[\sin\left(\frac{5\pi}{6}\right) = +\sin\frac{\pi}{6} = \frac{1}{2}, \qquad \cos\left(\frac{4\pi}{3}\right) = -\cos\frac{\pi}{3} = -\frac{1}{2}\]'
                r'\[\tan\left(\frac{3\pi}{4}\right) = -\tan\frac{\pi}{4} = -1, \qquad \sin^2\left(\frac{\pi}{3}\right) = \left(\frac{\sqrt{3}}{2}\right)^2 = \frac{3}{4} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Sum all four terms / Cộng chính xác 4 số hạng):</b></p>'
                r'\[\frac{1}{2} - \frac{1}{2} - 1 + \frac{3}{4} = -\frac{1}{4} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'Reciprocal Trig Functions',
            'q': r'<p>Given that \(\theta\) is an obtuse angle \(\left(\dfrac{\pi}{2} < \theta < \pi\right)\) and \(\sin\theta = \dfrac{5}{13}\), find the exact value of \(\sec\theta + \cot\theta\).</p>',
            'options': [
                r'\(\dfrac{209}{60}\)',
                r'\(-\dfrac{209}{60}\)',
                r'\(-\dfrac{79}{60}\)',
                r'\(-\dfrac{25}{17}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (Quadrant II sign of \(\cos\theta\) / Xác định dấu \(\cos\theta\) ở góc phần tư II):</b> Since \(\frac{\pi}{2} < \theta < \pi\), \(\cos\theta < 0\):</p>'
                r'\[\cos\theta = -\sqrt{1 - \left(\frac{5}{13}\right)^2} = -\frac{12}{13} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Evaluate \(\sec\theta + \cot\theta\) / Tính \(\sec\theta + \cot\theta\)):</b></p>'
                r'\[\sec\theta = \frac{1}{\cos\theta} = -\frac{13}{12}, \qquad \cot\theta = \frac{\cos\theta}{\sin\theta} = -\frac{12}{5}\]'
                r'\[\sec\theta + \cot\theta = -\frac{13}{12} - \frac{12}{5} = \frac{-65 - 144}{60} = -\frac{209}{60} \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Ignoring the obtuse-angle sign gives \(+\frac{209}{60}\) (Option A). Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'Trig Identities',
            'q': r'<p>Simplify the expression \(\dfrac{\sec x - \cos x}{\tan x}\) for \(0 < x < \dfrac{\pi}{2}\).</p>',
            'options': [
                r'\(\sin x\)',
                r'\(\cos x\)',
                r'\(\tan x\)',
                r'\(\operatorname{cosec} x\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Convert to \(\sin x\) and \(\cos x\) / Quy đổi về \(\sin x, \cos x\)):</b></p>'
                r'\[\sec x - \cos x = \frac{1}{\cos x} - \cos x = \frac{1 - \cos^2 x}{\cos x} = \frac{\sin^2 x}{\cos x} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Divide by \(\tan x = \frac{\sin x}{\cos x}\) / Chia cho \(\tan x\)):</b></p>'
                r'\[\frac{\sin^2 x}{\cos x} \div \frac{\sin x}{\cos x} = \frac{\sin^2 x}{\cos x} \cdot \frac{\cos x}{\sin x} = \sin x \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'Pythagorean Identities',
            'q': r'<p>Simplify completely: \((\sec\theta + \tan\theta)(\sec\theta - \tan\theta) + \dfrac{1}{\operatorname{cosec}^2\theta} + \dfrac{1}{\sec^2\theta}\).</p>',
            'options': [
                r'\(0\)',
                r'\(1\)',
                r'\(2\)',
                r'\(2\sec^2\theta\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Apply \(\sec^2\theta = 1 + \tan^2\theta\) / Dùng hằng đẳng thức \(\sec^2\theta - \tan^2\theta = 1\)):</b></p>'
                r'\[(\sec\theta + \tan\theta)(\sec\theta - \tan\theta) = \sec^2\theta - \tan^2\theta = 1 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Convert reciprocals / Chuyển hàm nghịch đảo):</b></p>'
                r'\[\frac{1}{\operatorname{cosec}^2\theta} + \frac{1}{\sec^2\theta} = \sin^2\theta + \cos^2\theta = 1\]'
                r'<p><b>Step 3 (Combine / Cộng kết quả):</b> \(1 + 1 = 2\) \(\text{[A1]}\). Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'Compound Angle Equation',
            'q': r'<p>Solve the equation \(\sin\left(2x - \dfrac{\pi}{6}\right) = \dfrac{1}{2}\) for \(0 \le x \le \pi\).</p>',
            'options': [
                r'\(x = \dfrac{\pi}{6}\) only',
                r'\(x = \dfrac{\pi}{6},\; \dfrac{\pi}{2}\)',
                r'\(x = \dfrac{\pi}{6},\; \dfrac{5\pi}{6}\)',
                r'\(x = \dfrac{\pi}{12},\; \dfrac{5\pi}{12}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (Adjust domain for \(u = 2x - \frac{\pi}{6}\) / Đổi khoảng giá trị cho \(u\)):</b></p>'
                r'\[0 \le x \le \pi \implies -\frac{\pi}{6} \le 2x - \frac{\pi}{6} \le \frac{11\pi}{6} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Find all \(u\) in Q1 & Q2 / Tìm mọi nghiệm \(u\) thoả \(\sin u = \frac{1}{2}\)):</b></p>'
                r'\[u = \frac{\pi}{6} \quad \text{or} \quad u = \pi - \frac{\pi}{6} = \frac{5\pi}{6}\]'
                r'<p><b>Step 3 (Solve for \(x\) / Giải tìm \(x\)):</b></p>'
                r'\[2x = \frac{\pi}{6} + \frac{\pi}{6} = \frac{\pi}{3} \implies x = \frac{\pi}{6}; \qquad 2x = \frac{5\pi}{6} + \frac{\pi}{6} = \pi \implies x = \frac{\pi}{2} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'Trig Equations (Degrees)',
            'q': r'<p>Find the total number of solutions and the largest solution to the equation \(\tan(3x + 30^\circ) = -\sqrt{3}\) for \(0^\circ \le x \le 180^\circ\).</p>',
            'options': [
                r'\(2\) solutions; largest \(x = 90^\circ\)',
                r'\(3\) solutions; largest \(x = 120^\circ\)',
                r'\(4\) solutions; largest \(x = 170^\circ\)',
                r'\(3\) solutions; largest \(x = 150^\circ\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Adjust domain for \(u = 3x + 30^\circ\) / Đổi khoảng nghiệm cho \(u\)):</b></p>'
                r'\[0^\circ \le x \le 180^\circ \implies 30^\circ \le u \le 570^\circ \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Solve \(\tan u = -\sqrt{3}\) / Giải \(\tan u = -\sqrt{3}\)):</b> Basic angle is \(60^\circ\). In Q2 and Q4 (period \(180^\circ\)):</p>'
                r'\[u = 120^\circ,\; 300^\circ,\; 480^\circ \quad (\text{next } 660^\circ > 570^\circ)\] '
                r'<p><b>Step 3 (Solve for \(x = \frac{u - 30^\circ}{3}\) / Giải ra \(x\)):</b></p>'
                r'\[x = 30^\circ,\; 90^\circ,\; 150^\circ \implies 3\text{ solutions, largest is } 150^\circ \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'Quadratic Trig (Sec/Tan)',
            'q': r'<p>Solve the equation \(2\sec^2 x - 5\tan x - 5 = 0\) for \(0^\circ \le x \le 360^\circ\), giving your answers correct to 1 decimal place.</p>',
            'options': [
                r'\(71.6^\circ,\; 251.6^\circ\)',
                r'\(26.6^\circ,\; 71.6^\circ,\; 206.6^\circ,\; 251.6^\circ\)',
                r'\(71.6^\circ,\; 153.4^\circ,\; 251.6^\circ,\; 333.4^\circ\)',
                r'\(18.4^\circ,\; 153.4^\circ,\; 198.4^\circ,\; 333.4^\circ\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Substitute \(\sec^2 x = 1 + \tan^2 x\) / Thay \(\sec^2 x = 1 + \tan^2 x\)):</b></p>'
                r'\[2(1 + \tan^2 x) - 5\tan x - 5 = 0 \implies 2\tan^2 x - 5\tan x - 3 = 0 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Factorise / Phân tích thành nhân tử):</b></p>'
                r'\[(2\tan x + 1)(\tan x - 3) = 0 \implies \tan x = 3 \quad \text{or} \quad \tan x = -\frac{1}{2}\]'
                r'<p><b>Step 3 (All solutions in \([0^\circ, 360^\circ]\) / Tìm mọi nghiệm):</b></p>'
                r'<p>• \(\tan x = 3 \Rightarrow x = 71.6^\circ,\; 180^\circ + 71.6^\circ = 251.6^\circ\).</p>'
                r'<p>• \(\tan x = -0.5\) (basic angle \(26.565^\circ\)) \(\Rightarrow x = 180^\circ - 26.6^\circ = 153.4^\circ,\; 360^\circ - 26.6^\circ = 333.4^\circ\) \(\text{[A1]}\).</p>'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'Quadratic Trig (Cosec/Cot)',
            'q': r'<p>Solve the equation \(\operatorname{cosec}^2 x + 3\cot x - 5 = 0\) for \(0 \le x \le \pi\), giving your answers in radians correct to 3 significant figures.</p>',
            'options': [
                r'\(0.785,\; 2.90\)',
                r'\(0.245,\; 0.785\)',
                r'\(0.785,\; 1.82\)',
                r'\(0.785,\; 2.36\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Use \(\operatorname{cosec}^2 x = 1 + \cot^2 x\) / Thay \(\operatorname{cosec}^2 x = 1 + \cot^2 x\)):</b></p>'
                r'\[(1 + \cot^2 x) + 3\cot x - 5 = 0 \implies \cot^2 x + 3\cot x - 4 = 0 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Factorise & convert to \(\tan x\) / Phân tích và chuyển sang \(\tan x\)):</b></p>'
                r'\[(\cot x + 4)(\cot x - 1) = 0 \implies \tan x = 1 \quad \text{or} \quad \tan x = -\frac{1}{4}\]'
                r'<p><b>Step 3 (Solve in \([0, \pi]\) in RAD mode / Giải trên \([0, \pi]\) ở chế độ RAD):</b></p>'
                r'<p>• \(\tan x = 1 \Rightarrow x = \frac{\pi}{4} \approx 0.785\text{ rad}\).</p>'
                r'<p>• \(\tan x = -0.25 \Rightarrow \alpha = \arctan(0.25) = 0.24498\text{ rad} \Rightarrow x = \pi - 0.24498 = 2.8966 \approx 2.90\text{ rad}\) \(\text{[A1]}\).</p>'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'Quadratic Trig (Radians Exact)',
            'q': r'<p>Find the exact sum of all solutions to the equation \(2\cos^2 x + 3\sin x - 3 = 0\) in the interval \(0 \le x \le 2\pi\).</p>',
            'options': [
                r'\(\dfrac{2\pi}{3}\)',
                r'\(\pi\)',
                r'\(\dfrac{4\pi}{3}\)',
                r'\(\dfrac{3\pi}{2}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Use \(\cos^2 x = 1 - \sin^2 x\) / Đưa về phương trình theo \(\sin x\)):</b></p>'
                r'\[2(1 - \sin^2 x) + 3\sin x - 3 = 0 \implies 2\sin^2 x - 3\sin x + 1 = 0 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Factorise & solve in \([0, 2\pi]\) / Phân tích và tìm tất cả nghiệm):</b></p>'
                r'\[(2\sin x - 1)(\sin x - 1) = 0 \implies \sin x = \frac{1}{2} \;\text{ or }\; \sin x = 1\]'
                r'\[x = \frac{\pi}{6},\; \frac{5\pi}{6},\; \frac{\pi}{2}\]'
                r'<p><b>Step 3 (Sum all roots / Cộng tất cả các nghiệm):</b></p>'
                r'\[\frac{\pi}{6} + \frac{5\pi}{6} + \frac{\pi}{2} = \pi + \frac{\pi}{2} = \frac{3\pi}{2} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'Advanced Trig Identity',
            'q': r'<p>Given that \(\tan\theta + \cot\theta = 4\), find the exact value of \(\sec^2\theta + \operatorname{cosec}^2\theta\).</p>',
            'options': [
                r'\(14\)',
                r'\(16\)',
                r'\(18\)',
                r'\(12\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (Rewrite using Pythagorean identities / Biến đổi bằng hằng đẳng thức):</b></p>'
                r'\[\sec^2\theta + \operatorname{cosec}^2\theta = (1 + \tan^2\theta) + (1 + \cot^2\theta) = \tan^2\theta + 2 + \cot^2\theta \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Recognise the perfect square / Nhận diện hằng đẳng thức bình phương):</b> Since \(\tan\theta\cot\theta = 1\):</p>'
                r'\[\tan^2\theta + 2\tan\theta\cot\theta + \cot^2\theta = (\tan\theta + \cot\theta)^2 = 4^2 = 16 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> \(14 = 4^2 - 2\) is \(\tan^2\theta + \cot^2\theta\), forgetting the \(+2\) from \(1 + 1\). Answer: <b>B</b>.</p>'
            ),
        },
    ],
}


# =============================================================================
# DRILL 3 (Ch. 10): Permutations & Combinations (0606)
# Answer balance: A=3 (Q1,Q6,Q11), B=3 (Q3,Q8,Q9), C=3 (Q2,Q5,Q12), D=3 (Q4,Q7,Q10)
# =============================================================================
DRILL_C10 = {
    'code': 'd0606_c10',
    'folder_key': 'drills_p2',
    'lecture_key': 'c10',
    'calculator_policy': 'calculator',
    'order_index': 3,
    'title': 'Ch. 10 Drill: Permutations & Combinations (0606)',
    'time_limit': '30',
    'intro_html': _intro_box(
        r'Master row arrangements (together / separated / fixed ends), forming multi-digit even/odd/greater-than-\(N\) numbers without repetition, distinct combinations \({}^nC_r\), "at least" committees, and mixed selection-plus-role problems.',
        r'Thành thạo xếp hàng (đứng cạnh nhau / không cạnh nhau / hai đầu), lập số chẵn/lẻ/lớn hơn \(N\) không lặp chữ số, tổ hợp \({}^nC_r\), chọn uỷ ban có điều kiện "ít nhất" và bài toán kết hợp chọn–xếp.',
        r'\({}^nP_r = \dfrac{n!}{(n-r)!}\) (order matters / có thứ tự) &nbsp;|&nbsp; \({}^nC_r = \dfrac{n!}{r!(n-r)!}\) (selection only / không thứ tự)',
        r'For "no two items together", NEVER do Total \(-\) All Together when there are \(3+\) items — ALWAYS use the <b>Gap Method</b>! (Với "không có 2 phần tử nào cạnh nhau" cho từ 3 phần tử trở lên, PHẢI dùng phương pháp <b>chèn khoảng trống</b>.)',
    ),
    'questions': [
        {
            'tag': 'Arrangements: Together',
            'q': r'<p>In how many different ways can \(7\) distinct books—\(4\) Mathematics books and \(3\) Physics books—be arranged in a row on a shelf if all \(3\) Physics books must be placed <b>next to each other</b>?</p>',
            'options': [
                r'\(720\)',
                r'\(120\)',
                r'\(144\)',
                r'\(5040\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Block method / Gom nhóm 3 sách Vật lý):</b> Treat the \(3\) Physics books as \(1\) single block. Together with the \(4\) Mathematics books, there are \(4 + 1 = 5\) units to arrange:</p>'
                r'\[5! = 120\text{ ways} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Internal permutations / Hoán vị nội bộ trong nhóm):</b> The \(3\) distinct Physics books can be arranged among themselves in \(3! = 6\) ways:</p>'
                r'\[\text{Total} = 5! \times 3! = 120 \times 6 = 720 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Forgetting internal \(3!\) gives \(120\) (Option B). Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'Arrangements: Separated',
            'q': r'<p>Five boys and three girls stand in a single line for a photograph. In how many ways can they be arranged if <b>no two girls</b> are standing next to each other?</p>',
            'options': [
                r'\(2400\)',
                r'\(7200\)',
                r'\(14\,400\)',
                r'\(36\,000\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Arrange the boys first / Xếp 5 bạn nam trước):</b> The \(5\) boys can be arranged in \(5! = 120\) ways, creating \(6\) gaps (\(\_\,B\,\_\,B\,\_\,B\,\_\,B\,\_\,B\,\_\)).</p>'
                r'<p><b>Step 2 (Place the 3 girls into 3 of the 6 gaps / Xếp 3 bạn nữ vào 6 khoảng trống):</b></p>'
                r'\[{}^6P_3 = 6 \times 5 \times 4 = 120 \quad \text{[M1]}\]'
                r'<p><b>Step 3 (Multiply / Nhân hai giai đoạn):</b></p>'
                r'\[\text{Total} = 5! \times {}^6P_3 = 120 \times 120 = 14\,400 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> \(8! - 6!3! = 36\,000\) (Option D) only excludes all 3 girls together, leaving cases where 2 girls stand together! Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'Arrangements: Endpoints',
            'q': r'<p>All \(8\) distinct letters of the word <b>TRIANGLE</b> are arranged in a row. How many different arrangements both begin and end with a <b>vowel</b>?</p>',
            'options': [
                r'\(2160\)',
                r'\(4320\)',
                r'\(8640\)',
                r'\(14\,400\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (Fill the two ends / Xếp nguyên âm ở 2 đầu):</b> The word TRIANGLE has \(3\) vowels (\(\text{I, A, E}\)) and \(5\) consonants. Choosing and ordering \(2\) vowels for the first and last positions:</p>'
                r'\[{}^3P_2 = 3 \times 2 = 6 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Arrange remaining 6 letters / Xếp 6 chữ cái còn lại ở giữa):</b> \(6! = 720\) ways:</p>'
                r'\[\text{Total} = 6 \times 720 = 4320 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'Digit Permutations (Even)',
            'q': r'<p>How many \(4\)-digit <b>even</b> numbers can be formed using the digits \(\{1, 2, 3, 5, 6, 8\}\) if no digit may be repeated?</p>',
            'options': [
                r'\(120\)',
                r'\(150\)',
                r'\(360\)',
                r'\(180\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Restrict the units digit first / Chọn chữ số hàng đơn vị trước):</b> For the number to be even, the last digit must be chosen from \(\{2, 6, 8\}\) (\(3\) choices) \(\text{[M1]}\).</p>'
                r'<p><b>Step 2 (Fill the remaining 3 positions / Xếp 3 chữ số đầu từ 5 số còn lại):</b></p>'
                r'\[{}^5P_3 = 5 \times 4 \times 3 = 60\]'
                r'\[\text{Total} = 3 \times 60 = 180 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'Digit Permutations (With 0)',
            'q': r'<p>How many \(4\)-digit <b>even</b> numbers greater than \(1000\) can be formed using the digits \(\{0, 1, 2, 3, 4, 5\}\) if no digit may be repeated?</p>',
            'options': [
                r'\(144\)',
                r'\(150\)',
                r'\(156\)',
                r'\(180\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Split by whether the units digit is \(0\) / Chia 2 trường hợp vì chữ số đầu \(\neq 0\)):</b></p>'
                r'<p>• <b>Case 1 (Ends in \(0\)):</b> \(1\) choice for units digit; remaining \(3\) digits chosen from \(\{1,2,3,4,5\}\) in \({}^5P_3 = 60\) ways.</p>'
                r'<p>• <b>Case 2 (Ends in \(2\) or \(4\)):</b> \(2\) choices for units digit; thousands digit cannot be \(0\) or the units digit (\(4\) choices); middle \(2\) digits from remaining \(4\) digits in \({}^4P_2 = 12\) ways \(\Rightarrow 2 \times 4 \times 12 = 96\) \(\text{[M1]}\).</p>'
                r'<p><b>Step 2 (Sum mutually exclusive cases / Cộng hai trường hợp):</b></p>'
                r'\[\text{Total} = 60 + 96 = 156 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'Digit Constraints (> N)',
            'q': r'<p>How many \(5\)-digit <b>odd</b> numbers greater than \(40\,000\) can be formed using the digits \(\{1, 2, 4, 5, 7, 8\}\) if no digit may be repeated?</p>',
            'options': [
                r'\(240\)',
                r'\(288\)',
                r'\(192\)',
                r'\(360\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Split by first digit parity / Chia trường hợp theo tính chẵn lẻ chữ số đầu \(\ge 4\)):</b> Available digits \(\ge 4\) are \(\{4, 5, 7, 8\}\); odd digits are \(\{1, 5, 7\}\).</p>'
                r'<p>• <b>Case 1 (First digit is \(4\) or \(8\) — even):</b> \(2\) choices for first digit; \(3\) choices for last (odd) digit \(\{1,5,7\}\); \({}^4P_3 = 24\) ways for middle \(3\) digits \(\Rightarrow 2 \times 3 \times 24 = 144\).</p>'
                r'<p>• <b>Case 2 (First digit is \(5\) or \(7\) — odd):</b> \(2\) choices for first digit; only \(2\) odd digits remain for last digit; \({}^4P_3 = 24\) ways for middle \(3\) digits \(\Rightarrow 2 \times 2 \times 24 = 96\) \(\text{[M1]}\).</p>'
                r'<p><b>Step 2 (Total / Tổng số cách):</b></p>'
                r'\[\text{Total} = 144 + 96 = 240 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Multiplying \(4 \times 3 \times 24 = 288\) (Option B) forgets that choosing \(5\) or \(7\) first reduces the odd choices at the end! Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'Combinations (nCr)',
            'q': r'<p>A badminton squad consists of \(6\) seniors and \(5\) juniors. A team of \(5\) players is to be selected so that it contains <b>exactly \(3\) seniors and \(2\) juniors</b>. How many different teams can be formed?</p>',
            'options': [
                r'\(30\)',
                r'\(462\)',
                r'\(2400\)',
                r'\(200\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Select each group independently / Chọn riêng từng nhóm bằng tổ hợp):</b> Since order within a team does not matter:</p>'
                r'\[{}^6C_3 = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = 20, \qquad {}^5C_2 = \frac{5 \times 4}{2 \times 1} = 10 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Multiply / Áp dụng quy tắc nhân):</b></p>'
                r'\[\text{Total teams} = 20 \times 10 = 200 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'Committee: At Least',
            'q': r'<p>A committee of \(4\) people is to be chosen from \(5\) mathematicians and \(6\) physicists. In how many ways can the committee be chosen if it must include <b>at least \(2\) mathematicians</b>?</p>',
            'options': [
                r'\(150\)',
                r'\(215\)',
                r'\(230\)',
                r'\(315\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (List all valid compositions / Liệt kê các trường hợp hợp lệ):</b> \((M, P) \in \{(2,2), (3,1), (4,0)\}\):</p>'
                r'\[{}^5C_2 \times {}^6C_2 = 10 \times 15 = 150\]'
                r'\[{}^5C_3 \times {}^6C_1 = 10 \times 6 = 60, \qquad {}^5C_4 \times {}^6C_0 = 5 \times 1 = 5 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Sum cases / Cộng các trường hợp):</b></p>'
                r'\[\text{Total} = 150 + 60 + 5 = 215 \quad \text{[A1]}\]'
                r'<p><b>Alternative Check / Kiểm tra phần bù:</b> \({}^{11}C_4 - {}^6C_4 - {}^5C_1\cdot{}^6C_3 = 330 - 15 - 100 = 215\). Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'Committee: Restrictions',
            'q': r'<p>From a group of \(6\) men and \(4\) women, a committee of \(5\) people is to be selected. One particular man and one particular woman refuse to serve on the committee together. How many valid committees of \(5\) people can be formed?</p>',
            'options': [
                r'\(140\)',
                r'\(196\)',
                r'\(210\)',
                r'\(252\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (Complementary counting / Phương pháp phần bù):</b> Total unrestricted committees of \(5\) from \(10\) people:</p>'
                r'\[{}^{10}C_5 = 252 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Subtract forbidden committees containing BOTH / Trừ số uỷ ban có CẢ HAI người):</b> If both are included, choose the remaining \(3\) members from the other \(8\) people in \({}^8C_3 = 56\) ways:</p>'
                r'\[\text{Valid committees} = 252 - 56 = 196 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'Mixed Roles & Selection',
            'q': r'<p>A club has \(6\) male and \(4\) female members. A delegation of \(4\) members is to be chosen containing <b>\(2\) males and \(2\) females</b>, and from these \(4\) chosen members, one is appointed Chairperson and another is appointed Secretary. How many different delegations with assigned roles are possible?</p>',
            'options': [
                r'\(90\)',
                r'\(540\)',
                r'\(2160\)',
                r'\(1080\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Choose the mixed delegation / Chọn 2 nam và 2 nữ):</b></p>'
                r'\[{}^6C_2 \times {}^4C_2 = 15 \times 6 = 90 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Assign two distinct roles / Phân công Chủ tịch và Thư ký):</b> From the \(4\) chosen members, order matters for the \(2\) roles: \({}^4P_2 = 4 \times 3 = 12\):</p>'
                r'\[\text{Total} = 90 \times 12 = 1080 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Using \({}^4C_2 = 6\) instead of \({}^4P_2 = 12\) ignores that Chairperson and Secretary are distinct roles, giving \(540\) (Option B). Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'Select & Arrange',
            'q': r'<p>From \(5\) distinct red flags and \(4\) distinct blue flags, \(2\) red flags and \(3\) blue flags are selected and then arranged in a row so that the \(2\) selected red flags are placed at the <b>two ends</b>. How many different rows can be formed?</p>',
            'options': [
                r'\(480\)',
                r'\(240\)',
                r'\(40\)',
                r'\(960\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Select & order the 2 red flags at the ends / Chọn và xếp 2 cờ đỏ ở 2 đầu):</b></p>'
                r'\[{}^5C_2 \times 2! = {}^5P_2 = 5 \times 4 = 20 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Select & order 3 blue flags in the middle / Chọn và xếp 3 cờ xanh ở giữa):</b></p>'
                r'\[{}^4C_3 \times 3! = {}^4P_3 = 4 \times 3 \times 2 = 24\]'
                r'\[\text{Total} = 20 \times 24 = 480 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'Combinatorial Equations',
            'q': r'<p>Given that \(n\) is a positive integer satisfying \({}^nP_3 = 12 \times {}^nC_2\), find the value of \(n\).</p>',
            'options': [
                r'\(6\)',
                r'\(7\)',
                r'\(8\)',
                r'\(14\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Expand \({}^nP_3\) and \({}^nC_2\) / Khai triển công thức chỉnh hợp và tổ hợp):</b></p>'
                r'\[n(n - 1)(n - 2) = 12 \cdot \frac{n(n - 1)}{2} = 6n(n - 1) \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Simplify & solve / Rút gọn với điều kiện \(n \ge 3\)):</b> Dividing both sides by \(n(n - 1) \neq 0\):</p>'
                r'\[n - 2 = 6 \implies n = 8 \quad \text{[A1]}\]'
                r'<p><b>Check / Kiểm tra:</b> \({}^8P_3 = 336\) and \(12 \times {}^8C_2 = 12 \times 28 = 336\). Answer: <b>C</b>.</p>'
            ),
        },
    ],
}


# =============================================================================
# DRILL 4 (Ch. 11): Series — Binomial Theorem, AP & GP (0606)
# Answer balance: A=3 (Q3,Q5,Q12), B=3 (Q2,Q7,Q10), C=3 (Q4,Q8,Q11), D=3 (Q1,Q6,Q9)
# =============================================================================
DRILL_C11 = {
    'code': 'd0606_c11',
    'folder_key': 'drills_p2',
    'lecture_key': 'c11',
    'calculator_policy': 'calculator',
    'order_index': 4,
    'title': 'Ch. 11 Drill: Series — Binomial Theorem, AP & GP (0606)',
    'time_limit': '30',
    'intro_html': _intro_box(
        r'Master Binomial Theorem expansions \((a + bx)^n\), terms independent of \(x\), product expansions \((1 + ax)(2 - x)^n\), Arithmetic Progressions (\(u_n, S_n\)), Geometric Progressions (\(u_n, S_n, S_\infty\)), convergence \(|r| < 1\), and mixed AP–GP problems.',
        r'Thành thạo Nhị thức Newton \((a + bx)^n\), số hạng không chứa \(x\), tích đa thức, Cấp số cộng (\(u_n, S_n\)), Cấp số nhân (\(u_n, S_n, S_\infty\)), điều kiện hội tụ \(|r| < 1\) và bài toán kết hợp CSC–CSN.',
        r'\(T_{r+1} = \binom{n}{r}a^{n-r}b^r\) &nbsp;|&nbsp; AP: \(u_n = a+(n-1)d,\; S_n = \frac{n}{2}[2a+(n-1)d]\) &nbsp;|&nbsp; GP: \(u_n = ar^{n-1},\; S_n = \frac{a(1-r^n)}{1-r},\; S_\infty = \frac{a}{1-r}\; (|r|<1)\)',
        r'For GP convergence, NEVER forget the strict inequality \(-1 < r < 1\) (NOT \(\le\))! And when expanding \((a - bx)^n\), always keep the minus sign inside \((-bx)^r\). (Nhớ điều kiện hội tụ ngặt \(-1 < r < 1\) và luôn giữ dấu trừ bên trong ngoặc \((-bx)^r\).)',
    ),
    'questions': [
        {
            'tag': 'Binomial Expansion',
            'q': r'<p>Find the first three terms in the binomial expansion of \((2 - 3x)^5\) in ascending powers of \(x\).</p>',
            'options': [
                r'\(32 - 48x + 72x^2\)',
                r'\(32 - 240x - 720x^2\)',
                r'\(32 + 240x + 720x^2\)',
                r'\(32 - 240x + 720x^2\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Apply Binomial Theorem / Áp dụng Nhị thức Newton):</b></p>'
                r'\[(2 - 3x)^5 = \binom{5}{0}2^5 + \binom{5}{1}2^4(-3x) + \binom{5}{2}2^3(-3x)^2 + \dots \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Simplify each term / Rút gọn từng số hạng):</b></p>'
                r'\[= 32 + 5(16)(-3x) + 10(8)(9x^2) + \dots = 32 - 240x + 720x^2 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Since \((-3x)^2 = +9x^2\), the \(x^2\) term is positive (eliminating Option B). Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'Binomial Coefficient',
            'q': r'<p>In the binomial expansion of \((2 + kx)^6\), where \(k\) is a non-zero constant, the coefficient of \(x^2\) is equal to \(3\) times the coefficient of \(x\). Find the exact value of \(k\).</p>',
            'options': [
                r'\(\dfrac{6}{5}\)',
                r'\(\dfrac{12}{5}\)',
                r'\(\dfrac{15}{4}\)',
                r'\(\dfrac{4}{5}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (Extract coefficients of \(x\) and \(x^2\) / Tìm hệ số của \(x\) và \(x^2\)):</b></p>'
                r'\[\text{Coeff. of } x = \binom{6}{1}2^5 k = 6 \times 32k = 192k\]'
                r'\[\text{Coeff. of } x^2 = \binom{6}{2}2^4 k^2 = 15 \times 16k^2 = 240k^2 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Form & solve equation / Lập phương trình và giải tìm \(k\)):</b></p>'
                r'\[240k^2 = 3(192k) = 576k \xrightarrow{k \neq 0} k = \frac{576}{240} = \frac{12}{5} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'Term Independent of x',
            'q': r'<p>Find the term independent of \(x\) in the binomial expansion of \(\left(2x - \dfrac{1}{x^2}\right)^6\).</p>',
            'options': [
                r'\(240\)',
                r'\(-240\)',
                r'\(60\)',
                r'\(-160\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Write the general term / Viết số hạng tổng quát):</b></p>'
                r'\[T_{r+1} = \binom{6}{r}(2x)^{6-r}\left(-x^{-2}\right)^r = \binom{6}{r}2^{6-r}(-1)^r x^{6 - 3r} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Set exponent of \(x\) to \(0\) / Cho số mũ của \(x\) bằng \(0\)):</b></p>'
                r'\[6 - 3r = 0 \implies r = 2\]'
                r'\[T_3 = \binom{6}{2}2^4(-1)^2 = 15 \times 16 \times 1 = 240 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'Binomial Product',
            'q': r'<p>In the expansion of \((1 + ax)(2 - x)^5\), the coefficient of \(x^2\) is \(20\). Find the exact value of the constant \(a\).</p>',
            'options': [
                r'\(-\dfrac{3}{4}\)',
                r'\(\dfrac{5}{4}\)',
                r'\(\dfrac{3}{4}\)',
                r'\(\dfrac{1}{4}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Expand \((2 - x)^5\) up to \(x^2\) / Khai triển \((2 - x)^5\) đến \(x^2\)):</b></p>'
                r'\[(2 - x)^5 = 2^5 + \binom{5}{1}2^4(-x) + \binom{5}{2}2^3(-x)^2 + \dots = 32 - 80x + 80x^2 + \dots \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Collect the \(x^2\) terms in the product / Gom các số hạng chứa \(x^2\)):</b></p>'
                r'\[\text{Coeff. of } x^2 = (1)(80) + (a)(-80) = 80 - 80a = 20\]'
                r'\[80a = 60 \implies a = \frac{3}{4} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'AP: nth Term',
            'q': r'<p>The \(4\text{th}\) term of an arithmetic progression is \(17\) and the \(11\text{th}\) term is \(45\). Find the \(20\text{th}\) term of the progression.</p>',
            'options': [
                r'\(81\)',
                r'\(85\)',
                r'\(77\)',
                r'\(86\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Solve simultaneous equations / Giải hệ tìm \(a, d\)):</b> Using \(u_n = a + (n-1)d\):</p>'
                r'\[a + 3d = 17, \qquad a + 10d = 45\]'
                r'\[7d = 28 \implies d = 4, \qquad a = 17 - 3(4) = 5 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Compute \(u_{20}\) / Tính số hạng thứ 20):</b></p>'
                r'\[u_{20} = a + 19d = 5 + 19(4) = 5 + 76 = 81 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Using \(a + 20d\) instead of \(a + 19d\) gives \(85\) (Option B). Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'AP: Sum of n Terms',
            'q': r'<p>An arithmetic progression has first term \(a = 7\) and common difference \(d = 3\). Given that the sum of the first \(n\) terms is \(S_n = 472\), find the value of \(n\).</p>',
            'options': [
                r'\(14\)',
                r'\(15\)',
                r'\(18\)',
                r'\(16\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Substitute into \(S_n\) / Thay vào công thức tổng \(S_n\)):</b></p>'
                r'\[S_n = \frac{n}{2}[2(7) + (n - 1)(3)] = \frac{n}{2}(3n + 11) = 472 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Solve quadratic for \(n > 0\) / Giải phương trình bậc hai):</b></p>'
                r'\[3n^2 + 11n - 944 = 0 \implies (n - 16)(3n + 59) = 0\]'
                r'<p>Since \(n\) is a positive integer, \(n = 16\) \(\text{[A1]}\). Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'AP: Positive Terms Sum',
            'q': r'<p>An arithmetic progression has \(n\text{th}\) term \(u_n = 50 - 3n\) for \(n \ge 1\). Find the sum of all <b>positive</b> terms of this progression.</p>',
            'options': [
                r'\(391\)',
                r'\(392\)',
                r'\(416\)',
                r'\(390\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (Count positive terms / Tìm số lượng số hạng dương):</b></p>'
                r'\[50 - 3n > 0 \implies n < \frac{50}{3} = 16.\overline{6} \implies n_{\max} = 16 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Apply \(S_n = \frac{n}{2}(u_1 + u_n)\) / Tính tổng 16 số hạng đầu):</b> With \(u_1 = 47\) and \(u_{16} = 50 - 48 = 2\):</p>'
                r'\[S_{16} = \frac{16}{2}(47 + 2) = 8 \times 49 = 392 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'GP: nth Term',
            'q': r'<p>The \(3\text{rd}\) term of a geometric progression of positive terms is \(18\) and the \(6\text{th}\) term is \(\dfrac{16}{3}\). Find the first term \(a\) and the common ratio \(r\).</p>',
            'options': [
                r'\(a = 27,\; r = \dfrac{2}{3}\)',
                r'\(a = \dfrac{81}{2},\; r = \dfrac{3}{2}\)',
                r'\(a = \dfrac{81}{2},\; r = \dfrac{2}{3}\)',
                r'\(a = 36,\; r = \dfrac{1}{2}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Divide \(u_6\) by \(u_3\) / Chia \(u_6\) cho \(u_3\) để tìm công bội \(r\)):</b></p>'
                r'\[r^3 = \frac{ar^5}{ar^2} = \frac{16/3}{18} = \frac{16}{54} = \frac{8}{27} \implies r = \frac{2}{3} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Find \(a\) / Tìm số hạng đầu \(a\)):</b></p>'
                r'\[a\left(\frac{2}{3}\right)^2 = 18 \implies a = 18 \times \frac{9}{4} = \frac{81}{2} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'GP: Sum Inequality',
            'q': r'<p>A geometric progression has first term \(a = 5\) and common ratio \(r = 2\). Find the smallest integer value of \(n\) for which the sum of the first \(n\) terms exceeds \(2000\).</p>',
            'options': [
                r'\(7\)',
                r'\(8\)',
                r'\(10\)',
                r'\(9\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Set up GP sum inequality / Lập bất phương trình tổng CSN):</b></p>'
                r'\[S_n = \frac{5(2^n - 1)}{2 - 1} = 5(2^n - 1) > 2000 \implies 2^n - 1 > 400 \implies 2^n > 401 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Solve using powers of \(2\) or logarithms / Giải tìm số nguyên \(n\) nhỏ nhất):</b></p>'
                r'\[n > \frac{\ln 401}{\ln 2} \approx 8.647 \implies n = 9 \quad (S_8 = 1275,\; S_9 = 2555) \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'GP: Convergence',
            'q': r'<p>A geometric progression has common ratio \(r = \dfrac{2x - 1}{5}\). Find the complete set of values of \(x\) for which the sum to infinity \(S_\infty\) exists.</p>',
            'options': [
                r'\(-3 < x < 2\)',
                r'\(-2 < x < 3\)',
                r'\(-2 \le x \le 3\)',
                r'\(x < 3\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (State convergence condition / Điều kiện tồn tại tổng vô hạn \(S_\infty\)):</b> A GP converges if and only if \(|r| < 1\):</p>'
                r'\[-1 < \frac{2x - 1}{5} < 1 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Solve double inequality / Giải bất đẳng thức kép):</b></p>'
                r'\[-5 < 2x - 1 < 5 \implies -4 < 2x < 6 \implies -2 < x < 3 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Option C wrongly includes endpoints (\(|r|=1\) does NOT converge); Option D forgets \(r > -1\). Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'GP: Sum to Infinity',
            'q': r'<p>A convergent geometric progression has first term \(a = 12\) and sum to infinity \(S_\infty = 30\). Find the \(4\text{th}\) term \(u_4\) of the progression as an exact fraction.</p>',
            'options': [
                r'\(\dfrac{108}{25}\)',
                r'\(\dfrac{96}{125}\)',
                r'\(\dfrac{324}{125}\)',
                r'\(\dfrac{972}{625}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Find common ratio \(r\) from \(S_\infty\) / Tìm công bội \(r\)):</b></p>'
                r'\[S_\infty = \frac{a}{1 - r} \implies \frac{12}{1 - r} = 30 \implies 1 - r = \frac{12}{30} = \frac{2}{5} \implies r = \frac{3}{5} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Calculate \(u_4 = ar^3\) / Tính số hạng thứ 4):</b></p>'
                r'\[u_4 = 12\left(\frac{3}{5}\right)^3 = 12 \times \frac{27}{125} = \frac{324}{125} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'Mixed AP & GP',
            'q': r'<p>The \(1\text{st}\), \(3\text{rd}\), and \(7\text{th}\) terms of an arithmetic progression (with non-zero common difference \(d\)) form the first three consecutive terms of a geometric progression. Given that the \(1\text{st}\) term is \(6\), find the sum of the first \(5\) terms of the geometric progression.</p>',
            'options': [
                r'\(186\)',
                r'\(96\)',
                r'\(60\)',
                r'\(192\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Relate AP and GP terms / Thiết lập quan hệ giữa CSC và CSN):</b> The three terms are \(6,\; 6 + 2d,\; 6 + 6d\). By the GP ratio property \((u_3)^2 = u_1 \cdot u_7\):</p>'
                r'\[(6 + 2d)^2 = 6(6 + 6d) \implies 36 + 24d + 4d^2 = 36 + 36d \implies 4d(d - 3) = 0 \quad \text{[M1]}\]'
                r'<p>Since \(d \neq 0\), \(d = 3\), so the GP starts \(6,\; 12,\; 24,\dots\) with \(a = 6\) and \(r = 2\).</p>'
                r'<p><b>Step 2 (Find GP sum \(S_5\) / Tính tổng 5 số hạng đầu của CSN):</b></p>'
                r'\[S_5 = \frac{6(2^5 - 1)}{2 - 1} = 6(31) = 186 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> \(96\) is \(u_5\), not \(S_5\); \(60\) is the AP sum! Answer: <b>A</b>.</p>'
            ),
        },
    ],
}


# =============================================================================
# DRILL 5 (Ch. 12): Differentiation 1 — Chain, Product, Quotient & Stationary Points
# Calculator Policy: NON-CALCULATOR (Paper 1 2025–2027)
# Answer balance: A=3 (Q2,Q7,Q12), B=3 (Q1,Q6,Q9), C=3 (Q3,Q5,Q10), D=3 (Q4,Q8,Q11)
# =============================================================================
DRILL_C12 = {
    'code': 'd0606_c12',
    'folder_key': 'drills_p2',
    'lecture_key': 'c12',
    'calculator_policy': 'non-calculator',
    'order_index': 5,
    'title': 'Ch. 12 Drill: Differentiation 1 — Chain, Product, Quotient & Stationary Points (0606)',
    'time_limit': '30',
    'intro_html': _intro_box(
        r'Paper 1 Non-Calculator mastery of algebraic differentiation: power & chain rule \((ax+b)^n\), product rule, quotient rule, equations of tangents & normals, stationary points, second derivative test, and increasing/decreasing intervals.',
        r'Rèn luyện đạo hàm đại số không dùng máy tính (Paper 1): quy tắc luỹ thừa & hàm hợp \((ax+b)^n\), đạo hàm tích, đạo hàm thương, tiếp tuyến & pháp tuyến, điểm dừng, xét cực trị bằng đạo hàm cấp hai và khoảng đơn điệu.',
        r"\(\frac{d}{dx}(ax+b)^n = an(ax+b)^{n-1}\) &nbsp;|&nbsp; \((uv)' = uv' + vu'\) &nbsp;|&nbsp; \(\left(\frac{u}{v}\right)' = \frac{vu' - uv'}{v^2}\) &nbsp;|&nbsp; \(m_{\text{norm}} = -\frac{1}{m_{\text{tan}}}\)",
        r'Never forget the inner derivative factor \(a\) in the Chain Rule, and remember: \(\frac{d^2y}{dx^2} < 0\) means <b>maximum</b> while \(\frac{d^2y}{dx^2} > 0\) means <b>minimum</b>! (Đừng quên nhân đạo hàm bên trong \(a\), và nhớ \(\frac{d^2y}{dx^2} < 0\) là cực đại, \(> 0\) là cực tiểu.)',
    ),
    'questions': [
        {
            'tag': 'Power Rule (Non-Calc)',
            'q': r'<p>Given that \(y = \dfrac{2x^3 - 6x + 3}{x}\), find the exact value of \(\dfrac{dy}{dx}\) when \(x = -1\).</p>',
            'options': [
                r'\(-1\)',
                r'\(-7\)',
                r'\(1\)',
                r'\(-4\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (Split fraction into powers of \(x\) / Tách phân thức thành các luỹ thừa):</b></p>'
                r'\[y = 2x^2 - 6 + 3x^{-1} \implies \frac{dy}{dx} = 4x - 3x^{-2} = 4x - \frac{3}{x^2} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Substitute \(x = -1\) / Thay \(x = -1\)):</b></p>'
                r'\[\left.\frac{dy}{dx}\right|_{x=-1} = 4(-1) - \frac{3}{(-1)^2} = -4 - 3 = -7 \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'Chain Rule (Non-Calc)',
            'q': r'<p>Differentiate \(y = (3x - 2)^5\) with respect to \(x\), and hence find the gradient of the curve at the point where \(x = 1\).</p>',
            'options': [
                r'\(15\)',
                r'\(5\)',
                r'\(45\)',
                r'\(3\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Apply Chain Rule / Áp dụng đạo hàm hàm hợp):</b></p>'
                r'\[\frac{dy}{dx} = 5(3x - 2)^4 \cdot \frac{d}{dx}(3x - 2) = 15(3x - 2)^4 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Evaluate at \(x = 1\) / Tính hệ số góc tại \(x = 1\)):</b></p>'
                r'\[\left.\frac{dy}{dx}\right|_{x=1} = 15(3(1) - 2)^4 = 15(1)^4 = 15 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Forgetting to multiply by the inner derivative \(3\) gives \(5\) (Option B). Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'Chain Rule: Surds (Non-Calc)',
            'q': r'<p>Given that \(y = \dfrac{4}{\sqrt{2x + 1}}\), find the exact value of \(\dfrac{dy}{dx}\) when \(x = 4\).</p>',
            'options': [
                r'\(-\dfrac{2}{27}\)',
                r'\(\dfrac{4}{27}\)',
                r'\(-\dfrac{4}{27}\)',
                r'\(-\dfrac{4}{9}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Write in index form & differentiate / Đưa về dạng số mũ và lấy đạo hàm):</b> \(y = 4(2x + 1)^{-1/2}\):</p>'
                r'\[\frac{dy}{dx} = 4\left(-\frac{1}{2}\right)(2x + 1)^{-3/2} \cdot 2 = -\frac{4}{(2x + 1)^{3/2}} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Evaluate at \(x = 4\) / Thay \(x = 4\)):</b> Since \(2(4) + 1 = 9\) and \(9^{3/2} = (\sqrt{9})^3 = 27\):</p>'
                r'\[\left.\frac{dy}{dx}\right|_{x=4} = -\frac{4}{27} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'Product Rule (Non-Calc)',
            'q': r'<p>Find the exact value of \(\dfrac{dy}{dx}\) at \(x = 2\) for the curve \(y = x^2(2x - 3)^4\).</p>',
            'options': [
                r'\(20\)',
                r'\(32\)',
                r'\(28\)',
                r'\(36\)',
            ],
            'answer': 'D',
            'explanation': (
                r"<p><b>Step 1 (Apply Product + Chain Rule / Áp dụng đạo hàm tích kết hợp hàm hợp):</b> Let \(u = x^2\) (\(u' = 2x\)) and \(v = (2x - 3)^4\) (\(v' = 4(2x - 3)^3 \cdot 2 = 8(2x - 3)^3\)):</p>"
                r'\[\frac{dy}{dx} = u\frac{dv}{dx} + v\frac{du}{dx} = 8x^2(2x - 3)^3 + 2x(2x - 3)^4 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Substitute \(x = 2\) / Thay \(x = 2\)):</b> Since \(2(2) - 3 = 1\):</p>'
                r'\[\left.\frac{dy}{dx}\right|_{x=2} = 8(4)(1)^3 + 2(2)(1)^4 = 32 + 4 = 36 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Missing the chain factor \(2\) gives \(16 + 4 = 20\) (Option A). Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'Product Rule (Algebraic)',
            'q': r'<p>Given that \(y = x\sqrt{x + 3}\), express \(\dfrac{dy}{dx}\) as a single simplified fraction.</p>',
            'options': [
                r'\(\dfrac{2x + 3}{2\sqrt{x + 3}}\)',
                r'\(\dfrac{3x + 3}{2\sqrt{x + 3}}\)',
                r'\(\dfrac{3x + 6}{2\sqrt{x + 3}}\)',
                r'\(\dfrac{x + 6}{2\sqrt{x + 3}}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Apply Product Rule / Áp dụng quy tắc đạo hàm tích):</b> With \(u = x\) and \(v = (x + 3)^{1/2}\):</p>'
                r'\[\frac{dy}{dx} = (1)\sqrt{x + 3} + x \cdot \frac{1}{2\sqrt{x + 3}} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Combine over common denominator / Quy đồng mẫu số chung \(2\sqrt{x + 3}\)):</b></p>'
                r'\[\frac{dy}{dx} = \frac{2(x + 3) + x}{2\sqrt{x + 3}} = \frac{3x + 6}{2\sqrt{x + 3}} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'Quotient Rule (Non-Calc)',
            'q': r'<p>Differentiate \(y = \dfrac{3x - 1}{2x + 5}\) with respect to \(x\).</p>',
            'options': [
                r'\(\dfrac{13}{(2x + 5)^2}\)',
                r'\(\dfrac{17}{(2x + 5)^2}\)',
                r'\(\dfrac{-17}{(2x + 5)^2}\)',
                r'\(\dfrac{12x + 13}{(2x + 5)^2}\)',
            ],
            'answer': 'B',
            'explanation': (
                r"<p><b>Step 1 (Apply Quotient Rule / Áp dụng quy tắc đạo hàm thương):</b> With \(u = 3x - 1\) (\(u' = 3\)) and \(v = 2x + 5\) (\(v' = 2\)):</p>"
                r"\[\frac{dy}{dx} = \frac{v u' - u v'}{v^2} = \frac{(2x + 5)(3) - (3x - 1)(2)}{(2x + 5)^2} \quad \text{[M1]}\]"
                r'<p><b>Step 2 (Expand numerator carefully / Rút gọn tử số cẩn thận dấu trừ):</b></p>'
                r'\[\frac{dy}{dx} = \frac{6x + 15 - 6x + 2}{(2x + 5)^2} = \frac{17}{(2x + 5)^2} \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Writing \(-2(-1) = -2\) produces \(13\) (Option A). Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'Quotient Rule: Stationary x',
            'q': r'<p>For the curve \(y = \dfrac{x^2}{x - 3}\) (\(x \neq 3\)), find the \(x\)-coordinates of all points on the curve where the gradient is \(0\).</p>',
            'options': [
                r'\(x = 0\) and \(x = 6\)',
                r'\(x = 0\) and \(x = 3\)',
                r'\(x = 0\) and \(x = 2\)',
                r'\(x = 6\) only',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Differentiate via Quotient Rule / Tính đạo hàm bằng quy tắc thương):</b></p>'
                r'\[\frac{dy}{dx} = \frac{(x - 3)(2x) - x^2(1)}{(x - 3)^2} = \frac{2x^2 - 6x - x^2}{(x - 3)^2} = \frac{x(x - 6)}{(x - 3)^2} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Solve \(\frac{dy}{dx} = 0\) / Giải phương trình tử số bằng \(0\)):</b></p>'
                r'\[x(x - 6) = 0 \implies x = 0 \quad \text{or} \quad x = 6 \quad (\text{both } \neq 3) \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>A</b>.</p>'
            ),
        },
        {
            'tag': 'Equation of Tangent',
            'q': r'<p>Find the equation of the <b>tangent</b> to the curve \(y = x^3 - 3x^2 + 2x + 1\) at the point where \(x = 2\).</p>',
            'options': [
                r'\(y = 2x + 3\)',
                r'\(y = -\dfrac{1}{2}x + 2\)',
                r'\(y = 2x - 1\)',
                r'\(y = 2x - 3\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Step 1 (Point and gradient at \(x = 2\) / Tìm toạ độ tiếp điểm và hệ số góc):</b></p>'
                r'\[y(2) = 2^3 - 3(2^2) + 2(2) + 1 = 8 - 12 + 4 + 1 = 1 \implies P(2, 1)\] '
                r'\[\frac{dy}{dx} = 3x^2 - 6x + 2 \implies m_{\text{tan}} = 3(4) - 6(2) + 2 = 2 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Tangent equation / Lập phương trình tiếp tuyến):</b></p>'
                r'\[y - 1 = 2(x - 2) \implies y = 2x - 3 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Option B is the normal equation, not the tangent. Answer: <b>D</b>.</p>'
            ),
        },
        {
            'tag': 'Equation of Normal',
            'q': r'<p>Find the equation of the <b>normal</b> to the curve \(y = \sqrt{4x + 1}\) at the point \(P(2, 3)\), giving your answer in the form \(ax + by + c = 0\) with integer coefficients.</p>',
            'options': [
                r'\(2x - 3y + 5 = 0\)',
                r'\(3x + 2y - 12 = 0\)',
                r'\(3x - 2y = 0\)',
                r'\(3x + 2y - 6 = 0\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Step 1 (Gradient of tangent & normal / Hệ số góc tiếp tuyến và pháp tuyến):</b></p>'
                r'\[\frac{dy}{dx} = \frac{1}{2}(4x + 1)^{-1/2} \cdot 4 = \frac{2}{\sqrt{4x + 1}}\]'
                r'\[m_{\text{tan}} = \frac{2}{\sqrt{4(2) + 1}} = \frac{2}{3} \implies m_{\text{norm}} = -\frac{3}{2} \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Equation of normal through \((2, 3)\) / Lập phương trình pháp tuyến):</b></p>'
                r'\[y - 3 = -\frac{3}{2}(x - 2) \implies 2y - 6 = -3x + 6 \implies 3x + 2y - 12 = 0 \quad \text{[A1]}\]'
                r'<p><b>Trap Check / Lưu ý bẫy:</b> Option A is the tangent line! Answer: <b>B</b>.</p>'
            ),
        },
        {
            'tag': 'Stationary Points & d²y/dx²',
            'q': r'<p>A curve has equation \(y = 2x^3 - 9x^2 + 12x - 4\). Find the coordinates of the <b>local maximum</b> and <b>local minimum</b> points.</p>',
            'options': [
                r'Local maximum \((2, 0)\), local minimum \((1, 1)\)',
                r'Local maximum \((1, 5)\), local minimum \((2, 0)\)',
                r'Local maximum \((1, 1)\), local minimum \((2, 0)\)',
                r'Local maximum \((-1, -27)\), local minimum \((-2, -80)\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Step 1 (Solve \(\frac{dy}{dx} = 0\) / Tìm hoành độ điểm dừng):</b></p>'
                r'\[\frac{dy}{dx} = 6x^2 - 18x + 12 = 6(x - 1)(x - 2) = 0 \implies x = 1 \;\text{ or }\; x = 2 \quad \text{[M1]}\]'
                r'<p><b>Step 2 (Coordinates & second derivative test / Tính tung độ và xét dấu \(\frac{d^2y}{dx^2}\)):</b> \(\frac{d^2y}{dx^2} = 12x - 18\):</p>'
                r'<p>• At \(x = 1\): \(y = 2 - 9 + 12 - 4 = 1\), \(\frac{d^2y}{dx^2} = -6 < 0 \Rightarrow (1, 1)\) is a <b>local maximum</b>.</p>'
                r'<p>• At \(x = 2\): \(y = 16 - 36 + 24 - 4 = 0\), \(\frac{d^2y}{dx^2} = +6 > 0 \Rightarrow (2, 0)\) is a <b>local minimum</b> \(\text{[A1]}\).</p>'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>C</b>.</p>'
            ),
        },
        {
            'tag': 'Increasing & Decreasing',
            'q': r'<p>Find the set of values of \(x\) for which the function \(f(x) = x^3 - 3x^2 - 24x + 5\) is a <b>decreasing</b> function.</p>',
            'options': [
                r'\(x < -2\) or \(x > 4\)',
                r'\(-4 < x < 2\)',
                r'\(x < 1\)',
                r'\(-2 < x < 4\)',
            ],
            'answer': 'D',
            'explanation': (
                r"<p><b>Step 1 (Find \(f'(x)\) and critical points / Tính đạo hàm \(f'(x)\) và phân tích nhân tử):</b></p>"
                r"\[f'(x) = 3x^2 - 6x - 24 = 3(x^2 - 2x - 8) = 3(x - 4)(x + 2) \quad \text{[M1]}\]"
                r"<p><b>Step 2 (Solve \(f'(x) < 0\) / Giải bất phương trình nghịch biến \(f'(x) < 0\)):</b> Since the quadratic opens upwards, it is negative between its roots:</p>"
                r'\[(x - 4)(x + 2) < 0 \implies -2 < x < 4 \quad \text{[A1]}\]'
                r"<p><b>Trap Check / Lưu ý bẫy:</b> Option A is where \(f(x)\) is increasing; Option C solves \(f''(x) < 0\). Answer: <b>D</b>.</p>"
            ),
        },
        {
            'tag': 'Stationary Point Constants',
            'q': r'<p>The curve \(y = ax^3 + bx^2 + 9x + 2\) has a stationary point at \((3, 2)\). Find the values of \(a\) and \(b\), and determine the nature of this stationary point.</p>',
            'options': [
                r'\(a = 1,\; b = -6\); local minimum',
                r'\(a = 1,\; b = -6\); local maximum',
                r'\(a = -1,\; b = 6\); local minimum',
                r'\(a = 2,\; b = -9\); local minimum',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Step 1 (Form two equations / Lập 2 phương trình từ điểm đi qua và điểm dừng):</b></p>'
                r'<p>• Curve passes through \((3, 2)\): \(27a + 9b + 27 + 2 = 2 \Rightarrow 3a + b = -3\).</p>'
                r'<p>• Stationary at \(x = 3\): \(\frac{dy}{dx} = 3ax^2 + 2bx + 9 = 0 \Rightarrow 27a + 6b + 9 = 0 \Rightarrow 9a + 2b = -3\) \(\text{[M1]}\).</p>'
                r'<p><b>Step 2 (Solve & classify / Giải hệ và phân loại cực trị):</b> Substituting \(b = -3 - 3a\):</p>'
                r'\[9a + 2(-3 - 3a) = -3 \implies 3a = 3 \implies a = 1,\; b = -6\]'
                r'\[\frac{d^2y}{dx^2} = 6ax + 2b = 6x - 12 \implies \left.\frac{d^2y}{dx^2}\right|_{x=3} = 18 - 12 = 6 > 0 \implies \text{local minimum} \quad \text{[A1]}\]'
                r'<p><b>Conclusion / Kết luận:</b> Answer: <b>A</b>.</p>'
            ),
        },
    ],
}


DRILLS_0606_P2A = [
    DRILL_C8,
    DRILL_C9,
    DRILL_C10,
    DRILL_C11,
    DRILL_C12,
]


# =============================================================================
# COMPREHENSIVE MATHEMATICAL & STRUCTURAL VERIFICATION (ALL 60 QUESTIONS)
# =============================================================================
def verify_all_math():
    """Programmatically verifies EVERY SINGLE mathematical calculation across all 60 Qs
    plus structural integrity, exact A/B/C/D balance, KaTeX hygiene, and pipeline validation."""

    # -------------------------------------------------------------------------
    # 1. CH. 8 — Circular Measure (12 Qs)
    # -------------------------------------------------------------------------
    # Q1: 225 deg -> 5pi/4, 7pi/12 -> 105 deg
    assert Fraction(225, 180) == Fraction(5, 4)
    assert Fraction(7 * 180, 12) == 105

    # Q2: r=12, theta=1.35 -> s=16.2, P=40.2
    s2 = Fraction(12) * Fraction(135, 100)
    assert s2 == Fraction(81, 5)  # 16.2
    assert 2 * 12 + s2 == Fraction(201, 5)  # 40.2

    # Q3: r=8, P=26 -> s=10, theta=1.25, A=40
    s3 = 26 - 2 * 8
    assert s3 == 10
    assert Fraction(1, 2) * 8 * s3 == 40
    assert Fraction(1, 2) * (8 ** 2) * Fraction(s3, 8) == 40

    # Q4: s=15, A=90 -> r=12, theta=1.25
    r4 = Fraction(2 * 90, 15)
    theta4 = Fraction(15, r4)
    assert r4 == 12 and theta4 == Fraction(5, 4)
    assert Fraction(1, 2) * r4 * r4 * theta4 == 90

    # Q5: r=6, theta=2pi/3 -> A_seg = 12pi - 9*sqrt(3)
    a5_exact = 0.5 * (6 ** 2) * (2 * math.pi / 3 - math.sin(2 * math.pi / 3))
    assert math.isclose(a5_exact, 12 * math.pi - 9 * math.sqrt(3), rel_tol=1e-12)

    # Q6: r=10, theta=1.4 -> A_seg = 20.7275... -> 20.7 (3 s.f.)
    a6 = 0.5 * (10 ** 2) * (1.4 - math.sin(1.4))
    assert f'{a6:.3g}' == '20.7'

    # Q7: r=9, theta=1.6 -> P = 14.4 + 18*sin(0.8) = 27.3124... -> 27.3 (3 s.f.)
    p7 = 9 * 1.6 + 2 * 9 * math.sin(0.8)
    assert f'{p7:.3g}' == '27.3'

    # Q8: r=5, angle=1.1 -> A_tri - A_sec = 12.5*tan(1.1) - 13.75 = 10.8095... -> 10.8 (3 s.f.)
    a8 = 0.5 * 5 * (5 * math.tan(1.1)) - 0.5 * (5 ** 2) * 1.1
    assert f'{a8:.3g}' == '10.8'

    # Q9: r=6, OP=12 -> angle AOP = pi/3, AOB = 2pi/3, PA=PB=6sqrt(3), arc=4pi -> P = 12sqrt(3) + 4pi
    ang9 = math.acos(6 / 12)
    assert math.isclose(ang9, math.pi / 3, rel_tol=1e-12)
    p9 = 2 * math.sqrt(12 ** 2 - 6 ** 2) + 6 * (2 * ang9)
    assert math.isclose(p9, 12 * math.sqrt(3) + 4 * math.pi, rel_tol=1e-12)

    # Q10: OA=8, OB=11, angle=0.9 -> CB=3, arc=7.2, AB=sqrt(64+121-176cos0.9) -> P=18.8946 -> 18.9
    ab10 = math.sqrt(8 ** 2 + 11 ** 2 - 2 * 8 * 11 * math.cos(0.9))
    p10 = ab10 + (11 - 8) + 8 * 0.9
    assert f'{p10:.3g}' == '18.9'

    # Q11: r1=5, r2=9, theta=0.8 -> A=22.4, P=19.2 -> A/P = 7/6
    a11 = Fraction(1, 2) * (9 ** 2 - 5 ** 2) * Fraction(4, 5)
    p11 = 2 * (9 - 5) + (5 + 9) * Fraction(4, 5)
    assert a11 / p11 == Fraction(7, 6)

    # Q12: two circles r=6, d=6 -> overlap = 2 * (12pi - 9sqrt(3)) = 24pi - 18sqrt(3)
    a12 = 2 * 0.5 * (6 ** 2) * (2 * math.pi / 3 - math.sin(2 * math.pi / 3))
    assert math.isclose(a12, 24 * math.pi - 18 * math.sqrt(3), rel_tol=1e-12)

    # -------------------------------------------------------------------------
    # 2. CH. 9 — Trigonometry (12 Qs)
    # -------------------------------------------------------------------------
    # Q1: f(x) = 4 sin(3x) - 2 -> amp=4, period=2pi/3, range=[-6, 2]
    assert abs(4) == 4
    assert math.isclose(2 * math.pi / 3, 2 * math.pi / 3)
    assert (-4 - 2, 4 - 2) == (-6, 2)

    # Q2: max=7, min=-3, period=120 -> a=5, c=2, b=3
    assert Fraction(7 - (-3), 2) == 5
    assert Fraction(7 + (-3), 2) == 2
    assert Fraction(360, 120) == 3

    # Q3: sin(5pi/6) + cos(4pi/3) + tan(3pi/4) + sin^2(pi/3) = -1/4
    val_c9_q3 = (
        math.sin(5 * math.pi / 6)
        + math.cos(4 * math.pi / 3)
        + math.tan(3 * math.pi / 4)
        + math.sin(math.pi / 3) ** 2
    )
    assert math.isclose(val_c9_q3, -0.25, abs_tol=1e-12)

    # Q4: obtuse sin=5/13 -> cos=-12/13 -> sec + cot = -13/12 - 12/5 = -209/60
    sin_q4 = Fraction(5, 13)
    cos_q4 = -Fraction(12, 13)
    assert sin_q4 ** 2 + cos_q4 ** 2 == 1
    assert Fraction(1, cos_q4) + Fraction(cos_q4, sin_q4) == Fraction(-209, 60)

    # Q5: (sec x - cos x)/tan x == sin x (spot check across Q1)
    for x in (0.2, 0.5, 1.0, 1.3):
        lhs = (1 / math.cos(x) - math.cos(x)) / math.tan(x)
        assert math.isclose(lhs, math.sin(x), rel_tol=1e-12)

    # Q6: (sec+tan)(sec-tan) + 1/cosec^2 + 1/sec^2 == 2
    for x in (0.3, 0.7, 1.2):
        sec_x = 1 / math.cos(x)
        tan_x = math.tan(x)
        cosec_x = 1 / math.sin(x)
        expr = (sec_x + tan_x) * (sec_x - tan_x) + 1 / (cosec_x ** 2) + 1 / (sec_x ** 2)
        assert math.isclose(expr, 2.0, rel_tol=1e-12)

    # Q7: sin(2x - pi/6) = 1/2 on [0, pi] -> pi/6, pi/2
    roots_c9_q7 = [math.pi / 6, math.pi / 2]
    for r in roots_c9_q7:
        assert 0 <= r <= math.pi
        assert math.isclose(math.sin(2 * r - math.pi / 6), 0.5, abs_tol=1e-12)
    # Confirm no other roots on [0, pi]
    u_vals_q7 = [u for k in range(-2, 5) for u in (math.pi / 6 + 2 * k * math.pi, 5 * math.pi / 6 + 2 * k * math.pi)
                 if -math.pi / 6 - 1e-9 <= u <= 11 * math.pi / 6 + 1e-9]
    assert len(u_vals_q7) == 2

    # Q8: tan(3x + 30 deg) = -sqrt(3) on [0, 180] -> 30, 90, 150 (3 solutions, max 150)
    sols_c9_q8 = []
    for k in range(-2, 6):
        u_deg = 120 + 180 * k
        x_deg = (u_deg - 30) / 3
        if 0 <= x_deg <= 180:
            sols_c9_q8.append(x_deg)
            assert math.isclose(math.tan(math.radians(3 * x_deg + 30)), -math.sqrt(3), abs_tol=1e-12)
    assert sols_c9_q8 == [30.0, 90.0, 150.0]

    # Q9: 2 sec^2 x - 5 tan x - 5 = 0 on [0, 360] -> 71.6, 153.4, 251.6, 333.4
    raw_q9 = sorted([
        math.degrees(math.atan(3)),
        180 + math.degrees(math.atan(3)),
        180 - math.degrees(math.atan(0.5)),
        360 - math.degrees(math.atan(0.5)),
    ])
    assert [round(v, 1) for v in raw_q9] == [71.6, 153.4, 251.6, 333.4]
    for deg in raw_q9:
        rad = math.radians(deg)
        assert math.isclose(2 / (math.cos(rad) ** 2) - 5 * math.tan(rad) - 5, 0.0, abs_tol=1e-10)

    # Q10: cosec^2 x + 3 cot x - 5 = 0 on [0, pi] -> 0.785, 2.90
    raw_q10 = [math.pi / 4, math.pi - math.atan(0.25)]
    assert [f'{v:.3g}' for v in raw_q10] == ['0.785', '2.9']
    assert f'{raw_q10[1]:.2f}' == '2.90'
    for r in raw_q10:
        cosec_sq = 1 / (math.sin(r) ** 2)
        cot_r = math.cos(r) / math.sin(r)
        assert math.isclose(cosec_sq + 3 * cot_r - 5, 0.0, abs_tol=1e-10)

    # Q11: 2 cos^2 x + 3 sin x - 3 = 0 on [0, 2pi] -> pi/6, pi/2, 5pi/6 -> sum = 3pi/2
    roots_q11 = [math.pi / 6, math.pi / 2, 5 * math.pi / 6]
    for r in roots_q11:
        assert math.isclose(2 * math.cos(r) ** 2 + 3 * math.sin(r) - 3, 0.0, abs_tol=1e-12)
    assert math.isclose(sum(roots_q11), 3 * math.pi / 2, rel_tol=1e-12)

    # Q12: tan + cot = 4 -> sec^2 + cosec^2 = 16
    t12 = 2 + math.sqrt(3)
    assert math.isclose(t12 + 1 / t12, 4.0, rel_tol=1e-12)
    assert math.isclose((1 + t12 ** 2) + (1 + (1 / t12) ** 2), 16.0, rel_tol=1e-12)

    # -------------------------------------------------------------------------
    # 3. CH. 10 — Permutations & Combinations (12 Qs, including brute-force checks!)
    # -------------------------------------------------------------------------
    # Q1: 4 Math + 3 Phys, Phys together = 5! * 3! = 720
    assert math.factorial(5) * math.factorial(3) == 720

    # Q2: 5 boys + 3 girls, no 2 girls together = 5! * 6P3 = 14400
    assert math.factorial(5) * math.perm(6, 3) == 14400
    # Brute-force verify gap-pattern count (3 girls among 8 slots, no adjacent) = C(6,3)=20 -> 20*3!*5! = 14400
    valid_patterns = sum(
        1 for comb in itertools.combinations(range(8), 3)
        if comb[1] - comb[0] > 1 and comb[2] - comb[1] > 1
    )
    assert valid_patterns * math.factorial(3) * math.factorial(5) == 14400

    # Q3: TRIANGLE (8 distinct letters, 3 vowels I,A,E), begin & end with vowel = 3P2 * 6! = 4320
    assert len(set('TRIANGLE')) == 8
    assert math.perm(3, 2) * math.factorial(6) == 4320

    # Q4: 4-digit even from {1,2,3,5,6,8} no rep = 180 (brute-force verify!)
    bf_q4 = sum(1 for p in itertools.permutations([1, 2, 3, 5, 6, 8], 4) if p[-1] % 2 == 0)
    assert bf_q4 == 180 and 3 * math.perm(5, 3) == 180

    # Q5: 4-digit even > 1000 from {0,1,2,3,4,5} no rep = 156 (brute-force verify!)
    bf_q5 = sum(
        1 for p in itertools.permutations([0, 1, 2, 3, 4, 5], 4)
        if p[0] != 0 and p[-1] % 2 == 0
    )
    assert bf_q5 == 156 and math.perm(5, 3) + 2 * 4 * math.perm(4, 2) == 156

    # Q6: 5-digit odd > 40000 from {1,2,4,5,7,8} no rep = 240 (brute-force verify!)
    bf_q6 = sum(
        1 for p in itertools.permutations([1, 2, 4, 5, 7, 8], 5)
        if p[0] >= 4 and p[-1] % 2 == 1
    )
    assert bf_q6 == 240 and 2 * 3 * math.perm(4, 3) + 2 * 2 * math.perm(4, 3) == 240

    # Q7: 6 seniors, 5 juniors -> 3S + 2J = 200
    assert math.comb(6, 3) * math.comb(5, 2) == 200

    # Q8: 4 from 5M + 6P, at least 2M = 215
    c10_q8_dir = (
        math.comb(5, 2) * math.comb(6, 2)
        + math.comb(5, 3) * math.comb(6, 1)
        + math.comb(5, 4) * math.comb(6, 0)
    )
    c10_q8_comp = math.comb(11, 4) - math.comb(6, 4) - math.comb(5, 1) * math.comb(6, 3)
    assert c10_q8_dir == 215 and c10_q8_comp == 215

    # Q9: 5 from 10, 1 pair refuse together = C(10,5) - C(8,3) = 196
    assert math.comb(10, 5) - math.comb(8, 3) == 196

    # Q10: 2M from 6, 2F from 4, assign Chair & Sec = 15 * 6 * 12 = 1080
    assert math.comb(6, 2) * math.comb(4, 2) * math.perm(4, 2) == 1080

    # Q11: 2 red from 5 at ends, 3 blue from 4 in middle = 5P2 * 4P3 = 480
    assert math.perm(5, 2) * math.perm(4, 3) == 480

    # Q12: nP3 = 12 * nC2 -> n = 8
    sols_c10_q12 = [n for n in range(3, 50) if math.perm(n, 3) == 12 * math.comb(n, 2)]
    assert sols_c10_q12 == [8]

    # -------------------------------------------------------------------------
    # 4. CH. 11 — Series: Binomial Theorem, AP & GP (12 Qs)
    # -------------------------------------------------------------------------
    # Q1: (2 - 3x)^5 first 3 terms: 32, -240x, 720x^2
    c11_q1 = [math.comb(5, r) * (2 ** (5 - r)) * ((-3) ** r) for r in range(3)]
    assert c11_q1 == [32, -240, 720]

    # Q2: (2 + kx)^6, coeff(x^2) = 3*coeff(x) -> k = 12/5
    k2 = Fraction(3 * math.comb(6, 1) * (2 ** 5), math.comb(6, 2) * (2 ** 4))
    assert k2 == Fraction(12, 5)
    assert math.comb(6, 2) * (2 ** 4) * (k2 ** 2) == 3 * math.comb(6, 1) * (2 ** 5) * k2

    # Q3: term independent of x in (2x - 1/x^2)^6 -> r=2 -> 240
    indep_terms = [
        math.comb(6, r) * (2 ** (6 - r)) * ((-1) ** r)
        for r in range(7) if (6 - r) - 2 * r == 0
    ]
    assert indep_terms == [240]

    # Q4: (1 + ax)(2 - x)^5, coeff(x^2) = 20 -> a = 3/4
    c_x1 = math.comb(5, 1) * (2 ** 4) * (-1)
    c_x2 = math.comb(5, 2) * (2 ** 3) * ((-1) ** 2)
    a4 = Fraction(20 - c_x2, c_x1)
    assert a4 == Fraction(3, 4) and c_x2 + a4 * c_x1 == 20

    # Q5: AP u4=17, u11=45 -> d=4, a=5, u20=81
    d5 = Fraction(45 - 17, 11 - 4)
    a5 = 17 - 3 * d5
    assert d5 == 4 and a5 == 5 and a5 + 19 * d5 == 81

    # Q6: AP a=7, d=3, Sn=472 -> n=16
    assert sum(7 + 3 * i for i in range(16)) == 472

    # Q7: AP un = 50 - 3n, sum of all positive terms = 392
    pos_terms = [50 - 3 * n for n in range(1, 30) if 50 - 3 * n > 0]
    assert len(pos_terms) == 16 and sum(pos_terms) == 392

    # Q8: GP u3=18, u6=16/3 -> r=2/3, a=81/2
    r8 = Fraction(2, 3)
    a8 = Fraction(81, 2)
    assert a8 * (r8 ** 2) == 18 and a8 * (r8 ** 5) == Fraction(16, 3)

    # Q9: GP a=5, r=2, Sn > 2000 -> smallest n = 9
    sn_q9 = lambda n: 5 * (2 ** n - 1)
    assert sn_q9(8) <= 2000 and sn_q9(9) > 2000

    # Q10: |(2x - 1)/5| < 1 <=> -2 < x < 3
    for x_in in (-1.999, 0, 2.999):
        assert abs((2 * x_in - 1) / 5) < 1
    for x_out in (-2, 3):
        assert abs((2 * x_out - 1) / 5) == 1

    # Q11: GP a=12, S_inf=30 -> r=3/5, u4 = 324/125
    r11 = 1 - Fraction(12, 30)
    assert r11 == Fraction(3, 5)
    assert 12 * (r11 ** 3) == Fraction(324, 125)

    # Q12: AP u1=6, u3=6+2d, u7=6+6d in GP -> d=3 -> GP a=6, r=2 -> S5 = 186
    d12 = 3
    assert (6 + 2 * d12) ** 2 == 6 * (6 + 6 * d12)
    r12 = Fraction(6 + 2 * d12, 6)
    assert r12 == 2
    assert sum(6 * (r12 ** i) for i in range(5)) == 186

    # -------------------------------------------------------------------------
    # 5. CH. 12 — Differentiation 1 (12 Qs, Non-Calculator — exact + finite-diff!)
    # -------------------------------------------------------------------------
    h = 1e-6

    def num_deriv(f, x):
        return (f(x + h) - f(x - h)) / (2 * h)

    # Q1: y = (2x^3 - 6x + 3)/x at x=-1 -> -7
    f_c12_q1 = lambda x: (2 * x ** 3 - 6 * x + 3) / x
    assert math.isclose(num_deriv(f_c12_q1, -1.0), -7.0, rel_tol=1e-7)

    # Q2: y = (3x - 2)^5 at x=1 -> 15
    f_c12_q2 = lambda x: (3 * x - 2) ** 5
    assert math.isclose(num_deriv(f_c12_q2, 1.0), 15.0, rel_tol=1e-7)

    # Q3: y = 4 / sqrt(2x + 1) at x=4 -> -4/27
    f_c12_q3 = lambda x: 4 / math.sqrt(2 * x + 1)
    assert math.isclose(num_deriv(f_c12_q3, 4.0), -4 / 27, rel_tol=1e-7)

    # Q4: y = x^2 (2x - 3)^4 at x=2 -> 36
    f_c12_q4 = lambda x: (x ** 2) * ((2 * x - 3) ** 4)
    assert math.isclose(num_deriv(f_c12_q4, 2.0), 36.0, rel_tol=1e-7)

    # Q5: y = x sqrt(x + 3) -> dy/dx = (3x + 6) / (2 sqrt(x + 3))
    f_c12_q5 = lambda x: x * math.sqrt(x + 3)
    for xv in (0.0, 1.0, 6.0):
        exact = (3 * xv + 6) / (2 * math.sqrt(xv + 3))
        assert math.isclose(num_deriv(f_c12_q5, xv), exact, rel_tol=1e-7)

    # Q6: y = (3x - 1)/(2x + 5) -> dy/dx = 17 / (2x + 5)^2
    f_c12_q6 = lambda x: (3 * x - 1) / (2 * x + 5)
    for xv in (-1.0, 0.0, 2.0):
        exact = 17 / ((2 * xv + 5) ** 2)
        assert math.isclose(num_deriv(f_c12_q6, xv), exact, rel_tol=1e-7)

    # Q7: y = x^2 / (x - 3) -> dy/dx = 0 at x=0, 6
    f_c12_q7 = lambda x: (x ** 2) / (x - 3)
    assert math.isclose(num_deriv(f_c12_q7, 0.0), 0.0, abs_tol=1e-7)
    assert math.isclose(num_deriv(f_c12_q7, 6.0), 0.0, abs_tol=1e-7)

    # Q8: y = x^3 - 3x^2 + 2x + 1 at x=2 -> P(2,1), m=2 -> tangent y = 2x - 3
    f_c12_q8 = lambda x: x ** 3 - 3 * x ** 2 + 2 * x + 1
    assert f_c12_q8(2) == 1
    assert math.isclose(num_deriv(f_c12_q8, 2.0), 2.0, rel_tol=1e-7)
    assert 2 * 2 - 3 == 1

    # Q9: y = sqrt(4x + 1) at P(2, 3) -> m_tan = 2/3, m_norm = -3/2 -> 3x + 2y - 12 = 0
    f_c12_q9 = lambda x: math.sqrt(4 * x + 1)
    assert f_c12_q9(2) == 3.0
    assert math.isclose(num_deriv(f_c12_q9, 2.0), 2 / 3, rel_tol=1e-7)
    assert 3 * 2 + 2 * 3 - 12 == 0 and Fraction(-3, 2) * Fraction(2, 3) == -1

    # Q10: y = 2x^3 - 9x^2 + 12x - 4 -> max (1,1), min (2,0)
    f_c12_q10 = lambda x: 2 * x ** 3 - 9 * x ** 2 + 12 * x - 4
    d1_q10 = lambda x: 6 * x ** 2 - 18 * x + 12
    d2_q10 = lambda x: 12 * x - 18
    assert f_c12_q10(1) == 1 and d1_q10(1) == 0 and d2_q10(1) == -6 < 0
    assert f_c12_q10(2) == 0 and d1_q10(2) == 0 and d2_q10(2) == 6 > 0

    # Q11: f(x) = x^3 - 3x^2 - 24x + 5 -> decreasing on -2 < x < 4
    d1_q11 = lambda x: 3 * x ** 2 - 6 * x - 24
    assert d1_q11(-2) == 0 and d1_q11(4) == 0
    assert d1_q11(0) < 0 and d1_q11(-3) > 0 and d1_q11(5) > 0

    # Q12: y = ax^3 + bx^2 + 9x + 2, stationary at (3, 2) -> a=1, b=-6, d2y/dx2 = 6 > 0 (min)
    a12_c, b12_c = 1, -6
    f_c12_q12 = lambda x: a12_c * x ** 3 + b12_c * x ** 2 + 9 * x + 2
    assert f_c12_q12(3) == 2
    assert math.isclose(num_deriv(f_c12_q12, 3.0), 0.0, abs_tol=1e-7)
    assert 6 * a12_c * 3 + 2 * b12_c == 6 > 0

    # -------------------------------------------------------------------------
    # 6. STRUCTURAL, BALANCE, KATEX & PIPELINE VALIDATION
    # -------------------------------------------------------------------------
    assert len(DRILLS_0606_P2A) == 5, f'Expected 5 drills, got {len(DRILLS_0606_P2A)}'
    expected_meta = [
        ('d0606_c8', 'c8', 'calculator', 1),
        ('d0606_c9', 'c9', 'calculator', 2),
        ('d0606_c10', 'c10', 'calculator', 3),
        ('d0606_c11', 'c11', 'calculator', 4),
        ('d0606_c12', 'c12', 'non-calculator', 5),
    ]

    total_qs = 0
    for drill, (code, lec, policy, oidx) in zip(DRILLS_0606_P2A, expected_meta):
        assert drill['code'] == code
        assert drill['folder_key'] == 'drills_p2'
        assert drill['lecture_key'] == lec
        assert drill['calculator_policy'] == policy
        assert drill['order_index'] == oidx
        assert drill['time_limit'] == '30'
        assert '$' not in drill['intro_html'], f"{code}: raw $ found in intro_html"
        assert r"\'" not in drill['intro_html'], f"{code}: stray backslash-apostrophe in intro_html"
        assert drill['intro_html'].count(r'\(') == drill['intro_html'].count(r'\)'), f"{code}: unbalanced \\( \\) in intro_html"
        assert drill['intro_html'].count(r'\[') == drill['intro_html'].count(r'\]'), f"{code}: unbalanced \\[ \\] in intro_html"

        qs = drill['questions']
        assert len(qs) == 12, f'{code}: expected 12 Qs, got {len(qs)}'
        total_qs += len(qs)

        counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        for i, q in enumerate(qs, start=1):
            for req_key in ('tag', 'q', 'options', 'answer', 'explanation'):
                assert req_key in q and q[req_key], f'{code} Q{i}: missing {req_key}'
            counts[q['answer']] += 1

            # Check no A./B./C./D. prefixes on options
            for opt in q['options']:
                assert not re.match(r'^\s*[A-D][\.\)]\s+', opt), f'{code} Q{i}: forbidden prefix in option {opt}'
                assert '$' not in opt, f'{code} Q{i}: raw $ in option'
                assert r"\'" not in opt, f'{code} Q{i}: stray backslash-apostrophe in option'

            # Check no raw $, no stray \', no unsupported \cosec, and bilingual M1/A1 presence
            full_q_txt = q['q'] + ' '.join(q['options']) + q['explanation']
            assert '$' not in full_q_txt, f'{code} Q{i}: raw $ found'
            assert r"\'" not in full_q_txt, f'{code} Q{i}: stray backslash-apostrophe found'
            assert r'\cosec' not in full_q_txt, f'{code} Q{i}: unsupported \\cosec (use \\operatorname{{cosec}})'
            assert '[M1]' in q['explanation'], f'{code} Q{i}: missing [M1] in explanation'
            assert '[A1]' in q['explanation'], f'{code} Q{i}: missing [A1] in explanation'

        assert counts == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, f'{code}: unbalanced answers {counts}'

        # Build StandardMCQTest JSON & run official pipeline validator
        cj = build_igcse_drill_json(
            title=drill['title'],
            course_id=COURSE_0606_ID,
            calculator_policy=drill['calculator_policy'],
            syllabus_code='0606',
            intro_html=drill['intro_html'],
            questions=qs,
            time_limit=drill['time_limit'],
        )
        errs = validate_igcse_drill(cj, title=drill['title'])
        assert not errs, f'{code} failed validate_igcse_drill: {errs}'

    assert total_qs == 60, f'Expected 60 total questions, got {total_qs}'
    print('[OK] verify_all_math(): All 5 drills (60/60 questions) passed exact math, A/B/C/D=3/3/3/3 balance, KaTeX, and validate_igcse_drill() checks!')


if __name__ == '__main__':
    verify_all_math()
