# -*- coding: utf-8 -*-
"""
Cambridge IGCSE Additional Mathematics (0606) 2025–2027 Syllabus Drills (Part 2B):
  - 4 Topical Drills (Chapters 13–16, folder_key='drills_p2', order_index=6..9, 12 Qs each = 48 Qs)
  - 2 Paper 1 Non-Calculator Specialist Drills (folder_key='non_calc', order_index=1..2, 15 Qs each = 30 Qs)
Total: 6 Drills, 78 Questions.

Exports:
  - DRILLS_0606_P2B
  - verify_all_math()

Self-test:
  python scripts/igcse_0606_drills_p2b.py
"""

from collections import Counter
from fractions import Fraction
import math
import os
import re
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.igcse_maths_pipeline import (
    COURSE_0606_ID,
    build_igcse_drill_json,
    validate_igcse_drill,
)


# =============================================================================
# DRILL 1: Ch. 13 — Vectors (Non-Calculator, 12 Qs, ZERO Relative Velocity!)
# Answer balance: A=3, B=3, C=3, D=3 -> B, A, D, C, A, D, B, C, D, A, C, B
# =============================================================================
DRILL_C13 = {
    'code': 'd0606_c13',
    'folder_key': 'drills_p2',
    'lecture_key': 'c13',
    'calculator_policy': 'non-calculator',
    'order_index': 6,
    'title': 'Ch. 13 Drill: Vectors — Position, Magnitude, Unit & Collinearity (2025–2027) (0606)',
    'time_limit': '30',
    'intro_html': (
        '<p>Luyện tập chuyên sâu <b>Chapter 13: Vectors in Two Dimensions</b> theo đúng đề cương '
        '<b>Cambridge 0606 (2025–2027)</b>: tính độ lớn vectơ \\(|\\mathbf{a}|\\), vectơ đơn vị (unit vector), '
        'vectơ vị trí \\(\\overrightarrow{AB} = \\mathbf{b} - \\mathbf{a}\\), chia đoạn thẳng theo tỉ số '
        '\\(AP:PB = m:n\\), chứng minh thẳng hàng (collinearity) và đồng nhất hệ số '
        '\\(\\lambda\\mathbf{a} + \\mu\\mathbf{b} = p\\mathbf{a} + q\\mathbf{b}\\). '
        '<i>Lưu ý: Phần Relative Velocity đã được loại bỏ khỏi đề cương 2025–2027.</i></p>'
    ),
    'questions': [
        {
            'tag': 'Magnitude & Column Vectors (0606)',
            'q': r'<p>Given \(\mathbf{p} = \begin{pmatrix} 4 \\ -5 \end{pmatrix}\) and \(\mathbf{q} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}\), find the exact value of \(|2\mathbf{p} - \mathbf{q}|\).</p>',
            'options': [
                r'\(7\)',
                r'\(13\)',
                r'\(17\)',
                r'\(\sqrt{119}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Compute column vector):</b> '
                r'\(2\mathbf{p} - \mathbf{q} = 2\begin{pmatrix} 4 \\ -5 \end{pmatrix} - \begin{pmatrix} 3 \\ 2 \end{pmatrix} = \begin{pmatrix} 8 - 3 \\ -10 - 2 \end{pmatrix} = \begin{pmatrix} 5 \\ -12 \end{pmatrix}\). [M1]</p>'
                r'<p><b>Bước 2 (Find magnitude):</b> '
                r'\(|2\mathbf{p} - \mathbf{q}| = \sqrt{5^2 + (-12)^2} = \sqrt{25 + 144} = \sqrt{169} = 13\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b> (Cẩn thận bẫy cộng độ dài thành phần \(5 + 12 = 17\).)</p>'
            ),
        },
        {
            'tag': 'Unit Vector (0606)',
            'q': r'<p>Find the unit vector in the same direction as \(\mathbf{v} = 8\mathbf{i} - 15\mathbf{j}\).</p>',
            'options': [
                r'\(\frac{1}{17}(8\mathbf{i} - 15\mathbf{j})\)',
                r'\(\frac{1}{23}(8\mathbf{i} - 15\mathbf{j})\)',
                r'\(\frac{1}{17}(8\mathbf{i} + 15\mathbf{j})\)',
                r'\(\frac{1}{289}(8\mathbf{i} - 15\mathbf{j})\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Find magnitude \(|\mathbf{v}|\)):</b> '
                r'\(|\mathbf{v}| = \sqrt{8^2 + (-15)^2} = \sqrt{64 + 225} = \sqrt{289} = 17\). [M1]</p>'
                r'<p><b>Bước 2 (Divide by magnitude):</b> '
                r'Vectơ đơn vị cùng chiều với \(\mathbf{v}\) là \(\hat{\mathbf{v}} = \frac{\mathbf{v}}{|\mathbf{v}|} = \frac{1}{17}(8\mathbf{i} - 15\mathbf{j})\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Vector of Given Magnitude (0606)',
            'q': r'<p>Find the vector \(\mathbf{w}\) that has magnitude \(50\) and is in the <b>opposite</b> direction to \(\mathbf{a} = \begin{pmatrix} 7 \\ -24 \end{pmatrix}\).</p>',
            'options': [
                r'\(\begin{pmatrix} 14 \\ -48 \end{pmatrix}\)',
                r'\(\begin{pmatrix} -14 \\ -48 \end{pmatrix}\)',
                r'\(\begin{pmatrix} -7 \\ 24 \end{pmatrix}\)',
                r'\(\begin{pmatrix} -14 \\ 48 \end{pmatrix}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Find unit vector of \(\mathbf{a}\)):</b> '
                r'\(|\mathbf{a}| = \sqrt{7^2 + (-24)^2} = \sqrt{49 + 576} = \sqrt{625} = 25\). '
                r'Do đó \(\hat{\mathbf{a}} = \frac{1}{25}\begin{pmatrix} 7 \\ -24 \end{pmatrix}\). [M1]</p>'
                r'<p><b>Bước 2 (Scale and reverse direction):</b> '
                r'Vì \(\mathbf{w}\) ngược chiều với \(\mathbf{a}\) và có độ lớn \(50\), ta nhân với \(-50\): '
                r'\(\mathbf{w} = -50 \cdot \frac{1}{25}\begin{pmatrix} 7 \\ -24 \end{pmatrix} = -2\begin{pmatrix} 7 \\ -24 \end{pmatrix} = \begin{pmatrix} -14 \\ 48 \end{pmatrix}\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Parallel Vectors (0606)',
            'q': r'<p>The vectors \(\mathbf{u} = \begin{pmatrix} k + 3 \\ 6 \end{pmatrix}\) and \(\mathbf{v} = \begin{pmatrix} 5 \\ k - 4 \end{pmatrix}\) are parallel, where \(k > 0\). Find the value of \(k\).</p>',
            'options': [
                r'\(k = 5\)',
                r'\(k = 6\)',
                r'\(k = 7\)',
                r'\(k = 9\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Condition for parallel vectors):</b> '
                r'Hai vectơ song song khi tỉ số các thành phần tương ứng bằng nhau: '
                r'\(\frac{k + 3}{5} = \frac{6}{k - 4} \implies (k + 3)(k - 4) = 30\). [M1]</p>'
                r'<p><b>Bước 2 (Solve quadratic):</b> '
                r'\(k^2 - k - 12 = 30 \implies k^2 - k - 42 = 0 \implies (k - 7)(k + 6) = 0\). '
                r'Vì \(k > 0\), ta nhận \(k = 7\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Position Vectors — Parallelogram (0606)',
            'q': r'<p>Relative to an origin \(O\), points \(A\), \(B\) and \(C\) have position vectors \(\overrightarrow{OA} = \begin{pmatrix} 2 \\ -5 \end{pmatrix}\), \(\overrightarrow{OB} = \begin{pmatrix} 7 \\ 3 \end{pmatrix}\) and \(\overrightarrow{OC} = \begin{pmatrix} 1 \\ 9 \end{pmatrix}\). Point \(D\) is such that \(ABCD\) is a parallelogram (vertices in order \(A, B, C, D\)). Find \(\overrightarrow{OD}\).</p>',
            'options': [
                r'\(\begin{pmatrix} -4 \\ 1 \end{pmatrix}\)',
                r'\(\begin{pmatrix} 8 \\ -11 \end{pmatrix}\)',
                r'\(\begin{pmatrix} 6 \\ 17 \end{pmatrix}\)',
                r'\(\begin{pmatrix} 4 \\ -1 \end{pmatrix}\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Use opposite equal sides of parallelogram):</b> '
                r'Trong hình bình hành \(ABCD\), ta có \(\overrightarrow{AD} = \overrightarrow{BC}\), suy ra '
                r'\(\overrightarrow{OD} - \overrightarrow{OA} = \overrightarrow{OC} - \overrightarrow{OB} \implies \overrightarrow{OD} = \overrightarrow{OA} + \overrightarrow{OC} - \overrightarrow{OB}\). [M1]</p>'
                r'<p><b>Bước 2 (Evaluate):</b> '
                r'\(\overrightarrow{OD} = \begin{pmatrix} 2 + 1 - 7 \\ -5 + 9 - 3 \end{pmatrix} = \begin{pmatrix} -4 \\ 1 \end{pmatrix}\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Ratio Division — Numerical (0606)',
            'q': r'<p>Relative to an origin \(O\), points \(A\) and \(B\) have position vectors \(\mathbf{a} = \begin{pmatrix} 2 \\ 11 \end{pmatrix}\) and \(\mathbf{b} = \begin{pmatrix} 17 \\ -4 \end{pmatrix}\). Point \(P\) lies on the line segment \(AB\) such that \(AP : PB = 2 : 3\). Find \(\overrightarrow{OP}\).</p>',
            'options': [
                r'\(\begin{pmatrix} 11 \\ 2 \end{pmatrix}\)',
                r'\(\begin{pmatrix} 6 \\ -6 \end{pmatrix}\)',
                r'\(\begin{pmatrix} 9.5 \\ 3.5 \end{pmatrix}\)',
                r'\(\begin{pmatrix} 8 \\ 5 \end{pmatrix}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Apply Ratio Theorem):</b> '
                r'Vì \(AP : PB = 2 : 3\), nên \(\overrightarrow{OP} = \mathbf{a} + \frac{2}{5}(\mathbf{b} - \mathbf{a}) = \frac{3\mathbf{a} + 2\mathbf{b}}{5}\). [M1]</p>'
                r'<p><b>Bước 2 (Compute components):</b> '
                r'\(3\mathbf{a} + 2\mathbf{b} = \begin{pmatrix} 6 + 34 \\ 33 - 8 \end{pmatrix} = \begin{pmatrix} 40 \\ 25 \end{pmatrix} \implies \overrightarrow{OP} = \frac{1}{5}\begin{pmatrix} 40 \\ 25 \end{pmatrix} = \begin{pmatrix} 8 \\ 5 \end{pmatrix}\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b> (Chú ý không đảo nhầm trọng số thành \(\frac{2\mathbf{a}+3\mathbf{b}}{5}\).)</p>'
            ),
        },
        {
            'tag': 'Ratio Division — Algebraic (0606)',
            'q': r'<p>In \(\triangle OAB\), \(\overrightarrow{OA} = \mathbf{a}\) and \(\overrightarrow{OB} = \mathbf{b}\). Point \(M\) is the midpoint of \(OA\), and point \(N\) lies on \(AB\) such that \(AN : NB = 1 : 3\). Express \(\overrightarrow{MN}\) in terms of \(\mathbf{a}\) and \(\mathbf{b}\).</p>',
            'options': [
                r'\(\frac{1}{4}\mathbf{a} - \frac{1}{4}\mathbf{b}\)',
                r'\(\frac{1}{4}\mathbf{a} + \frac{1}{4}\mathbf{b}\)',
                r'\(\frac{3}{4}\mathbf{a} + \frac{1}{4}\mathbf{b}\)',
                r'\(-\frac{1}{4}\mathbf{a} + \frac{3}{4}\mathbf{b}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Find \(\overrightarrow{OM}\) and \(\overrightarrow{ON}\)):</b> '
                r'\(\overrightarrow{OM} = \frac{1}{2}\mathbf{a}\) và \(\overrightarrow{AB} = \mathbf{b} - \mathbf{a}\). '
                r'Vì \(AN = \frac{1}{4}AB\), nên \(\overrightarrow{ON} = \mathbf{a} + \frac{1}{4}(\mathbf{b} - \mathbf{a}) = \frac{3}{4}\mathbf{a} + \frac{1}{4}\mathbf{b}\). [M1]</p>'
                r'<p><b>Bước 2 (Compute \(\overrightarrow{MN} = \overrightarrow{ON} - \overrightarrow{OM}\)):</b> '
                r'\(\overrightarrow{MN} = \left(\frac{3}{4} - \frac{1}{2}\right)\mathbf{a} + \frac{1}{4}\mathbf{b} = \frac{1}{4}\mathbf{a} + \frac{1}{4}\mathbf{b}\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Collinearity Parameter (0606)',
            'q': r'<p>Relative to an origin \(O\), points \(P\), \(Q\) and \(R\) have position vectors \(\overrightarrow{OP} = \mathbf{a} + 2\mathbf{b}\), \(\overrightarrow{OQ} = 4\mathbf{a} - \mathbf{b}\) and \(\overrightarrow{OR} = k\mathbf{a} - 7\mathbf{b}\), where \(\mathbf{a}\) and \(\mathbf{b}\) are non-parallel vectors. Given that \(P\), \(Q\) and \(R\) are collinear, find the value of \(k\).</p>',
            'options': [
                r'\(k = 7\)',
                r'\(k = 9\)',
                r'\(k = 10\)',
                r'\(k = 13\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Find \(\overrightarrow{PQ}\) and \(\overrightarrow{PR}\)):</b> '
                r'\(\overrightarrow{PQ} = \overrightarrow{OQ} - \overrightarrow{OP} = 3\mathbf{a} - 3\mathbf{b}\). '
                r'\(\overrightarrow{PR} = \overrightarrow{OR} - \overrightarrow{OP} = (k - 1)\mathbf{a} - 9\mathbf{b}\). [M1]</p>'
                r'<p><b>Bước 2 (Use \(\overrightarrow{PR} = \lambda\overrightarrow{PQ}\)):</b> '
                r'So sánh hệ số của \(\mathbf{b}\): \(-9 = -3\lambda \implies \lambda = 3\). '
                r'So sánh hệ số của \(\mathbf{a}\): \(k - 1 = 3\lambda = 9 \implies k = 10\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Proving Collinearity & Ratio (0606)',
            'q': r'<p>Relative to an origin \(O\), \(\overrightarrow{OA} = 2\mathbf{p} + 3\mathbf{q}\), \(\overrightarrow{OB} = 5\mathbf{p} + \mathbf{q}\) and \(\overrightarrow{OC} = 11\mathbf{p} - 3\mathbf{q}\), where \(\mathbf{p}\) and \(\mathbf{q}\) are non-parallel vectors. Which statement about \(A\), \(B\) and \(C\) is correct?</p>',
            'options': [
                r'\(A, B, C\) are not collinear because \(\overrightarrow{AB}\) and \(\overrightarrow{OC}\) are not parallel.',
                r'\(A, B, C\) are collinear with \(AB : BC = 1 : 3\).',
                r'\(A, B, C\) are collinear with \(AB : BC = 2 : 1\).',
                r'\(A, B, C\) are collinear with \(AB : BC = 1 : 2\).',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Compute \(\overrightarrow{AB}\) and \(\overrightarrow{BC}\)):</b> '
                r'\(\overrightarrow{AB} = (5 - 2)\mathbf{p} + (1 - 3)\mathbf{q} = 3\mathbf{p} - 2\mathbf{q}\). '
                r'\(\overrightarrow{BC} = (11 - 5)\mathbf{p} + (-3 - 1)\mathbf{q} = 6\mathbf{p} - 4\mathbf{q} = 2(3\mathbf{p} - 2\mathbf{q})\). [M1]</p>'
                r'<p><b>Bước 2 (Conclude collinearity and ratio):</b> '
                r'Vì \(\overrightarrow{BC} = 2\overrightarrow{AB}\) và có chung điểm \(B\), ba điểm \(A, B, C\) thẳng hàng với \(AB : BC = 1 : 2\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Equating Vector Coefficients (0606)',
            'q': r'<p>Given that \(\mathbf{a}\) and \(\mathbf{b}\) are non-zero, non-parallel vectors and \[(2\lambda + \mu)\mathbf{a} + (\lambda - 3\mu)\mathbf{b} = 7\mathbf{a} - 7\mathbf{b},\] find the values of \(\lambda\) and \(\mu\).</p>',
            'options': [
                r'\(\lambda = 2,\ \mu = 3\)',
                r'\(\lambda = 3,\ \mu = 1\)',
                r'\(\lambda = 2,\ \mu = -3\)',
                r'\(\lambda = 4,\ \mu = -1\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Equate coefficients of \(\mathbf{a}\) and \(\mathbf{b}\)):</b> '
                r'Vì \(\mathbf{a}\) và \(\mathbf{b}\) không song song, ta được hệ phương trình: '
                r'\(2\lambda + \mu = 7\) và \(\lambda - 3\mu = -7\). [M1]</p>'
                r'<p><b>Bước 2 (Solve simultaneous equations):</b> '
                r'Từ phương trình đầu \(\mu = 7 - 2\lambda\). Thế vào phương trình hai: '
                r'\(\lambda - 3(7 - 2\lambda) = -7 \implies 7\lambda = 14 \implies \lambda = 2\), suy ra \(\mu = 7 - 4 = 3\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Intersecting Lines in Triangle (0606)',
            'q': r'<p>In \(\triangle OAB\), \(\overrightarrow{OA} = \mathbf{a}\) and \(\overrightarrow{OB} = \mathbf{b}\). Point \(C\) lies on \(OA\) with \(\overrightarrow{OC} = \frac{1}{3}\mathbf{a}\), and \(D\) is the midpoint of \(OB\). The line segments \(AD\) and \(BC\) intersect at \(X\), where \(\overrightarrow{OX} = \overrightarrow{OA} + \lambda\overrightarrow{AD}\) and \(\overrightarrow{OX} = \overrightarrow{OB} + \mu\overrightarrow{BC}\). Find \(\lambda\) and \(\mu\).</p>',
            'options': [
                r'\(\lambda = \frac{3}{5},\ \mu = \frac{4}{5}\)',
                r'\(\lambda = \frac{2}{5},\ \mu = \frac{3}{5}\)',
                r'\(\lambda = \frac{4}{5},\ \mu = \frac{3}{5}\)',
                r'\(\lambda = \frac{4}{5},\ \mu = \frac{2}{5}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Express \(\overrightarrow{OX}\) in two ways):</b> '
                r'\(\overrightarrow{AD} = \frac{1}{2}\mathbf{b} - \mathbf{a} \implies \overrightarrow{OX} = (1 - \lambda)\mathbf{a} + \frac{1}{2}\lambda\mathbf{b}\). '
                r'\(\overrightarrow{BC} = \frac{1}{3}\mathbf{a} - \mathbf{b} \implies \overrightarrow{OX} = \frac{1}{3}\mu\mathbf{a} + (1 - \mu)\mathbf{b}\). [M1]</p>'
                r'<p><b>Bước 2 (Equate coefficients):</b> '
                r'\(1 - \lambda = \frac{1}{3}\mu \implies \mu = 3 - 3\lambda\), và \(\frac{1}{2}\lambda = 1 - \mu = 3\lambda - 2\). '
                r'Nhân 2 hai vế: \(\lambda = 6\lambda - 4 \implies 5\lambda = 4 \implies \lambda = \frac{4}{5}\), suy ra \(\mu = 3\left(1 - \frac{4}{5}\right) = \frac{3}{5}\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Ratio via Equating Coefficients (0606)',
            'q': r'<p>In \(\triangle OPQ\), \(\overrightarrow{OP} = \mathbf{p}\) and \(\overrightarrow{OQ} = \mathbf{q}\). Point \(M\) lies on \(OQ\) such that \(OM : MQ = 2 : 1\), and point \(R\) lies on \(OP\) produced such that \(\overrightarrow{OR} = \frac{3}{2}\mathbf{p}\). The line \(RM\) intersects \(PQ\) at \(T\), where \(\overrightarrow{PT} = k\overrightarrow{PQ}\). Find the exact value of \(k\).</p>',
            'options': [
                r'\(k = \frac{1}{3}\)',
                r'\(k = \frac{2}{5}\)',
                r'\(k = \frac{3}{5}\)',
                r'\(k = \frac{2}{3}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Express \(\overrightarrow{OT}\) along \(PQ\) and along \(RM\)):</b> '
                r'Dọc theo \(PQ\): \(\overrightarrow{OT} = \mathbf{p} + k(\mathbf{q} - \mathbf{p}) = (1 - k)\mathbf{p} + k\mathbf{q}\). '
                r'Dọc theo \(RM\) với \(\overrightarrow{OM} = \frac{2}{3}\mathbf{q}\): '
                r'\(\overrightarrow{OT} = \frac{3}{2}\mathbf{p} + \mu\left(\frac{2}{3}\mathbf{q} - \frac{3}{2}\mathbf{p}\right) = \frac{3}{2}(1 - \mu)\mathbf{p} + \frac{2}{3}\mu\mathbf{q}\). [M1]</p>'
                r'<p><b>Bước 2 (Equate coefficients and solve for \(k\)):</b> '
                r'Hệ số của \(\mathbf{q}\): \(k = \frac{2}{3}\mu \implies \mu = \frac{3}{2}k\). '
                r'Hệ số của \(\mathbf{p}\): \(1 - k = \frac{3}{2}\left(1 - \frac{3}{2}k\right) = \frac{3}{2} - \frac{9}{4}k \implies \frac{5}{4}k = \frac{1}{2} \implies k = \frac{2}{5}\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
    ],
}


# =============================================================================
# DRILL 2: Ch. 14 — Differentiation 2 (Calculator Allowed, 12 Qs)
# Answer balance: A=3, B=3, C=3, D=3 -> C, A, D, B, A, C, D, B, C, D, A, B
# =============================================================================
DRILL_C14 = {
    'code': 'd0606_c14',
    'folder_key': 'drills_p2',
    'lecture_key': 'c14',
    'calculator_policy': 'calculator',
    'order_index': 7,
    'title': 'Ch. 14 Drill: Differentiation 2 — Trig, Exp, Ln, Connected Rates & Small Changes (0606)',
    'time_limit': '30',
    'intro_html': (
        '<p>Chinh phục <b>Chapter 14: Differentiation 2</b> của <b>Cambridge 0606</b>: đạo hàm các hàm lượng giác '
        '\\(\\sin(ax), \\cos(ax), \\tan(ax)\\) (theo <b>radian</b>), hàm mũ \\(e^{ax+b}\\), hàm logarit tự nhiên '
        '\\(\\ln(ax+b)\\), quy tắc tích/thương (Product & Quotient Rules), tốc độ biến thiên liên kết '
        '(Connected Rates of Change \\(\\frac{dV}{dt} = \\frac{dV}{dr}\\cdot\\frac{dr}{dt}\\)), xấp xỉ biến thiên nhỏ '
        '(\\(\\delta y \\approx \\frac{dy}{dx}\\delta x\\)) và bài toán tối ưu hoá (Optimisation).</p>'
    ),
    'questions': [
        {
            'tag': 'Trig Derivatives (0606)',
            'q': r'<p>Differentiate \(y = 4\sin(3x) - 2\cos(5x)\) with respect to \(x\).</p>',
            'options': [
                r'\(12\cos(3x) - 10\sin(5x)\)',
                r'\(4\cos(3x) + 2\sin(5x)\)',
                r'\(12\cos(3x) + 10\sin(5x)\)',
                r'\(-12\cos(3x) + 10\sin(5x)\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Apply trig chain rule):</b> '
                r'\(\frac{d}{dx}[\sin(ax)] = a\cos(ax)\) và \(\frac{d}{dx}[\cos(ax)] = -a\sin(ax)\). [M1]</p>'
                r'<p><b>Bước 2 (Differentiate term by term):</b> '
                r'\(\frac{dy}{dx} = 4(3\cos 3x) - 2(-5\sin 5x) = 12\cos(3x) + 10\sin(5x)\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Derivative of tan(ax+b) (0606)',
            'q': r'<p>Find the exact gradient of the curve \(y = 3\tan\left(2x - \frac{\pi}{6}\right)\) at the point where \(x = \frac{\pi}{4}\).</p>',
            'options': [
                r'\(24\)',
                r'\(12\)',
                r'\(8\)',
                r'\(18\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Differentiate using \(\frac{d}{dx}[\tan(ax+b)] = a\sec^2(ax+b)\)):</b> '
                r'\(\frac{dy}{dx} = 3 \cdot 2\sec^2\left(2x - \frac{\pi}{6}\right) = 6\sec^2\left(2x - \frac{\pi}{6}\right)\). [M1]</p>'
                r'<p><b>Bước 2 (Substitute \(x = \frac{\pi}{4}\)):</b> '
                r'\(2\left(\frac{\pi}{4}\right) - \frac{\pi}{6} = \frac{\pi}{3}\). Vì \(\cos\left(\frac{\pi}{3}\right) = \frac{1}{2}\), nên \(\sec^2\left(\frac{\pi}{3}\right) = 4\), '
                r'suy ra \(\frac{dy}{dx} = 6 \times 4 = 24\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Exponential Chain Rule (0606)',
            'q': r'<p>Differentiate \(y = e^{3x^2 - 5x}\) with respect to \(x\).</p>',
            'options': [
                r'\((3x^2 - 5x)e^{3x^2 - 5x - 1}\)',
                r'\(6x e^{3x^2 - 5x}\)',
                r'\((6x - 5)e^{6x - 5}\)',
                r'\((6x - 5)e^{3x^2 - 5x}\)',
            ],
            'answer': 'D',
            'explanation': (
                r"<p><b>Bước 1 (Recall \(\frac{d}{dx}[e^{f(x)}] = f'(x)e^{f(x)}\)):</b> "
                r"Đặt \(f(x) = 3x^2 - 5x \implies f'(x) = 6x - 5\). [M1]</p>"
                r'<p><b>Bước 2 (Combine):</b> '
                r'\(\frac{dy}{dx} = (6x - 5)e^{3x^2 - 5x}\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Logarithmic Differentiation (0606)',
            'q': r'<p>Given \(y = \ln\left(\frac{(2x + 1)^3}{\sqrt{4x - 1}}\right)\) for \(x > \frac{1}{4}\), find the exact value of \(\frac{dy}{dx}\) when \(x = 1\).</p>',
            'options': [
                r'\(\frac{2}{3}\)',
                r'\(\frac{4}{3}\)',
                r'\(\frac{8}{3}\)',
                r'\(\frac{5}{6}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Expand using log laws before differentiating):</b> '
                r'\(y = 3\ln(2x + 1) - \frac{1}{2}\ln(4x - 1)\). '
                r'Suy ra \(\frac{dy}{dx} = 3\cdot\frac{2}{2x + 1} - \frac{1}{2}\cdot\frac{4}{4x - 1} = \frac{6}{2x + 1} - \frac{2}{4x - 1}\). [M1]</p>'
                r'<p><b>Bước 2 (Evaluate at \(x = 1\)):</b> '
                r'\(\frac{dy}{dx}\Big|_{x=1} = \frac{6}{3} - \frac{2}{3} = \frac{4}{3}\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Product Rule with e^x (0606)',
            'q': r'<p>Find the \(x\)-coordinate of the stationary point of the curve \(y = (2x - 3)e^{4x}\).</p>',
            'options': [
                r'\(x = \frac{5}{4}\)',
                r'\(x = \frac{3}{2}\)',
                r'\(x = \frac{7}{4}\)',
                r'\(x = \frac{1}{2}\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Apply Product Rule):</b> '
                r'\(\frac{dy}{dx} = 2\cdot e^{4x} + (2x - 3)\cdot 4e^{4x} = (2 + 8x - 12)e^{4x} = (8x - 10)e^{4x}\). [M1]</p>'
                r'<p><b>Bước 2 (Solve \(\frac{dy}{dx} = 0\)):</b> '
                r'Vì \(e^{4x} > 0\) với mọi \(x\), nên \(8x - 10 = 0 \implies x = \frac{10}{8} = \frac{5}{4}\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Quotient Rule with ln x (0606)',
            'q': r'<p>Find the exact coordinates of the stationary point of the curve \(y = \frac{\ln x}{x^2}\) for \(x > 0\).</p>',
            'options': [
                r'\(\left(e,\ \frac{1}{e^2}\right)\)',
                r'\(\left(\sqrt{e},\ \frac{1}{e}\right)\)',
                r'\(\left(\sqrt{e},\ \frac{1}{2e}\right)\)',
                r'\(\left(e^2,\ \frac{2}{e^4}\right)\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Apply Quotient Rule):</b> '
                r'\(\frac{dy}{dx} = \frac{x^2\left(\frac{1}{x}\right) - (\ln x)(2x)}{x^4} = \frac{x(1 - 2\ln x)}{x^4} = \frac{1 - 2\ln x}{x^3}\). [M1]</p>'
                r'<p><b>Bước 2 (Set \(\frac{dy}{dx} = 0\) and find \(y\)):</b> '
                r'\(1 - 2\ln x = 0 \implies \ln x = \frac{1}{2} \implies x = e^{1/2} = \sqrt{e}\). '
                r'Khi đó \(y = \frac{\frac{1}{2}}{(\sqrt{e})^2} = \frac{1}{2e}\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Normal to Exp-Trig Curve (0606)',
            'q': r'<p>A curve has equation \(y = e^{2x}\cos x\). Find the exact gradient of the <b>normal</b> to the curve at the point where \(x = 0\).</p>',
            'options': [
                r'\(2\)',
                r'\(-2\)',
                r'\(\frac{1}{2}\)',
                r'\(-\frac{1}{2}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Differentiate with Product Rule):</b> '
                r'\(\frac{dy}{dx} = 2e^{2x}\cos x + e^{2x}(-\sin x) = e^{2x}(2\cos x - \sin x)\). [M1]</p>'
                r'<p><b>Bước 2 (Evaluate tangent & normal gradients at \(x = 0\)):</b> '
                r'Tại \(x = 0\): \(m_t = e^0(2\cos 0 - \sin 0) = 2\). '
                r'Hệ số góc pháp tuyến (normal) là \(m_n = -\frac{1}{m_t} = -\frac{1}{2}\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Connected Rates — Sphere (0606)',
            'q': r'<p>Air is pumped into a spherical balloon at a constant rate of \(40\text{ cm}^3/\text{s}\). Given that the volume of a sphere is \(V = \frac{4}{3}\pi r^3\), find the rate of increase of the radius \(r\) when \(r = 5\text{ cm}\), correct to \(3\) significant figures.</p>',
            'options': [
                r'\(0.0637\text{ cm/s}\)',
                r'\(0.127\text{ cm/s}\)',
                r'\(0.382\text{ cm/s}\)',
                r'\(1.26\text{ cm/s}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Relate rates via Chain Rule):</b> '
                r'\(\frac{dV}{dr} = 4\pi r^2\). Tại \(r = 5\): \(\frac{dV}{dr} = 4\pi(25) = 100\pi\). '
                r'Áp dụng \(\frac{dV}{dt} = \frac{dV}{dr}\cdot\frac{dr}{dt}\). [M1]</p>'
                r'<p><b>Bước 2 (Solve for \(\frac{dr}{dt}\)):</b> '
                r'\(\frac{dr}{dt} = \frac{40}{100\pi} = \frac{2}{5\pi} \approx 0.12732\dots \approx 0.127\text{ cm/s}\) (3 s.f.). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Connected Rates — Curve (0606)',
            'q': r'<p>A point \(P(x, y)\) moves along the curve \(y = \sqrt{3x^2 + 4}\) such that its \(x\)-coordinate increases at a constant rate of \(0.5\text{ units/s}\). Find the rate of change of \(y\) when \(x = 2\).</p>',
            'options': [
                r'\(0.375\text{ units/s}\)',
                r'\(1.5\text{ units/s}\)',
                r'\(0.75\text{ units/s}\)',
                r'\(3.0\text{ units/s}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Find \(\frac{dy}{dx}\)):</b> '
                r'\(y = (3x^2 + 4)^{1/2} \implies \frac{dy}{dx} = \frac{1}{2}(3x^2 + 4)^{-1/2}(6x) = \frac{3x}{\sqrt{3x^2 + 4}}\). '
                r'Tại \(x = 2\): \(\frac{dy}{dx} = \frac{6}{\sqrt{16}} = \frac{3}{2}\). [M1]</p>'
                r'<p><b>Bước 2 (Apply Connected Rates):</b> '
                r'\(\frac{dy}{dt} = \frac{dy}{dx}\cdot\frac{dx}{dt} = \frac{3}{2} \times 0.5 = 0.75\text{ units/s}\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Small Changes — Algebraic (0606)',
            'q': r'<p>Given \(y = \frac{24}{x^2} + 3x\), use calculus to find the approximate change in \(y\) when \(x\) increases from \(2\) to \(2 + p\), where \(p\) is small.</p>',
            'options': [
                r'\(3p\)',
                r'\(-6p\)',
                r'\(9p\)',
                r'\(-3p\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Differentiate and evaluate at \(x = 2\)):</b> '
                r'\(y = 24x^{-2} + 3x \implies \frac{dy}{dx} = -48x^{-3} + 3 = -\frac{48}{x^3} + 3\). '
                r'Tại \(x = 2\): \(\frac{dy}{dx} = -\frac{48}{8} + 3 = -6 + 3 = -3\). [M1]</p>'
                r'<p><b>Bước 2 (Use \(\delta y \approx \frac{dy}{dx}\delta x\)):</b> '
                r'Với \(\delta x = p\), ta có \(\delta y \approx -3p\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Small Changes — Trig (0606)',
            'q': r'<p>A curve has equation \(y = 5\sin(2x)\), where \(x\) is in radians. Use calculus to find the approximate change in \(y\) when \(x\) increases from \(\frac{\pi}{6}\) to \(\frac{\pi}{6} + 0.02\).</p>',
            'options': [
                r'\(0.1\)',
                r'\(0.05\)',
                r'\(0.173\)',
                r'\(0.2\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Differentiate \(y = 5\sin(2x)\)):</b> '
                r'\(\frac{dy}{dx} = 10\cos(2x)\). Tại \(x = \frac{\pi}{6}\): \(\frac{dy}{dx} = 10\cos\left(\frac{\pi}{3}\right) = 10 \times \frac{1}{2} = 5\). [M1]</p>'
                r'<p><b>Bước 2 (Compute \(\delta y\)):</b> '
                r'\(\delta y \approx \frac{dy}{dx}\delta x = 5 \times 0.02 = 0.1\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Optimisation Problem (0606)',
            'q': r'<p>An open-top rectangular box has a square base of side \(x\text{ cm}\) and height \(h\text{ cm}\). Its total external surface area is \(192\text{ cm}^2\). Find the <b>maximum</b> possible volume of the box.</p>',
            'options': [
                r'\(192\text{ cm}^3\)',
                r'\(256\text{ cm}^3\)',
                r'\(384\text{ cm}^3\)',
                r'\(512\text{ cm}^3\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Express volume \(V\) in terms of \(x\) only):</b> '
                r'Diện tích toàn phần không nắp: \(x^2 + 4xh = 192 \implies h = \frac{192 - x^2}{4x}\). '
                r'Thể tích: \(V = x^2 h = 48x - \frac{1}{4}x^3\). [M1]</p>'
                r'<p><b>Bước 2 (Differentiate, verify maximum, evaluate \(V_{\max}\)):</b> '
                r'\(\frac{dV}{dx} = 48 - \frac{3}{4}x^2 = 0 \implies x^2 = 64 \implies x = 8\text{ cm}\) (vì \(x > 0\)). '
                r'Kiểm tra đạo hàm cấp 2: \(\frac{d^2V}{dx^2} = -\frac{3}{2}x = -12 < 0\) (cực đại). '
                r'Do đó \(V_{\max} = 48(8) - \frac{1}{4}(8^3) = 384 - 128 = 256\text{ cm}^3\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
    ],
}


# =============================================================================
# DRILL 3: Ch. 15 — Integration (Calculator Allowed, 12 Qs)
# Answer balance: A=3, B=3, C=3, D=3 -> D, B, A, C, B, D, A, C, A, D, B, C
# =============================================================================
DRILL_C15 = {
    'code': 'd0606_c15',
    'folder_key': 'drills_p2',
    'lecture_key': 'c15',
    'calculator_policy': 'calculator',
    'order_index': 8,
    'title': 'Ch. 15 Drill: Integration — Definite Integrals, Reverse Chain & Area (0606)',
    'time_limit': '30',
    'intro_html': (
        '<p>Luyện tập trọng tâm <b>Chapter 15: Integration</b> của <b>Cambridge 0606</b>: nguyên hàm đảo ngược quy tắc dây chuyền '
        '\\((ax+b)^n\\), \\(e^{ax+b}\\), \\(\\frac{1}{ax+b}\\), \\(\\sin(ax+b)\\), \\(\\cos(ax+b)\\), \\(\\sec^2(ax+b)\\), '
        'tìm hằng số \\(+ c\\) từ điểm cho trước, dạng bài kinh điển <i>"Hence find..."</i> (tích phân ngược đạo hàm), '
        'tích phân xác định (Definite Integrals) và tính diện tích hình phẳng dưới đường cong / giữa hai đường cong.</p>'
    ),
    'questions': [
        {
            'tag': 'Reverse Chain Rule (ax+b)^n (0606)',
            'q': r'<p>Find \(\displaystyle \int (3x - 2)^5\,dx\).</p>',
            'options': [
                r'\(\frac{1}{6}(3x - 2)^6 + c\)',
                r'\(\frac{1}{15}(3x - 2)^6 + c\)',
                r'\(15(3x - 2)^4 + c\)',
                r'\(\frac{1}{18}(3x - 2)^6 + c\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Apply reverse chain rule):</b> '
                r'\(\int (ax + b)^n\,dx = \frac{(ax + b)^{n+1}}{a(n + 1)} + c\) với \(a = 3, n = 5\). [M1]</p>'
                r'<p><b>Bước 2 (Simplify):</b> '
                r'\(\int (3x - 2)^5\,dx = \frac{(3x - 2)^6}{3 \times 6} + c = \frac{1}{18}(3x - 2)^6 + c\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Integrating e^(ax+b) & 1/(ax+b) (0606)',
            'q': r'<p>Find \(\displaystyle \int \left(6e^{2x - 1} + \frac{10}{5x + 3}\right)dx\) for \(x > -\frac{3}{5}\).</p>',
            'options': [
                r'\(12e^{2x - 1} + 50\ln(5x + 3) + c\)',
                r'\(3e^{2x - 1} + 2\ln(5x + 3) + c\)',
                r'\(3e^{2x - 1} + 10\ln(5x + 3) + c\)',
                r'\(6e^{2x - 1} + 2\ln(5x + 3) + c\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Apply exponential and reciprocal rules):</b> '
                r'\(\int e^{ax+b}\,dx = \frac{1}{a}e^{ax+b} + c\) và \(\int \frac{1}{ax+b}\,dx = \frac{1}{a}\ln(ax+b) + c\). [M1]</p>'
                r'<p><b>Bước 2 (Divide each term by its linear coefficient):</b> '
                r'\(\frac{6}{2}e^{2x - 1} + \frac{10}{5}\ln(5x + 3) + c = 3e^{2x - 1} + 2\ln(5x + 3) + c\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Trig Integrals — sin & sec² (0606)',
            'q': r'<p>Find \(\displaystyle \int \left(4\sin(2x) + 6\sec^2(3x)\right)dx\).</p>',
            'options': [
                r'\(-2\cos(2x) + 2\tan(3x) + c\)',
                r'\(2\cos(2x) + 2\tan(3x) + c\)',
                r'\(-2\cos(2x) + 18\tan(3x) + c\)',
                r'\(-8\cos(2x) + 2\tan(3x) + c\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Recall standard trig integrals):</b> '
                r'\(\int \sin(ax)\,dx = -\frac{1}{a}\cos(ax) + c\) và \(\int \sec^2(ax)\,dx = \frac{1}{a}\tan(ax) + c\). [M1]</p>'
                r'<p><b>Bước 2 (Evaluate):</b> '
                r'\(4\left(-\frac{1}{2}\cos 2x\right) + 6\left(\frac{1}{3}\tan 3x\right) + c = -2\cos(2x) + 2\tan(3x) + c\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Finding +c from a Point (0606)',
            'q': r'<p>A curve is such that \(\frac{dy}{dx} = \frac{12}{\sqrt{4x + 1}}\) and passes through the point \((2, 15)\). Find the equation of the curve.</p>',
            'options': [
                r'\(y = 24\sqrt{4x + 1} - 57\)',
                r'\(y = 6\sqrt{4x + 1} + 3\)',
                r'\(y = 6\sqrt{4x + 1} - 3\)',
                r'\(y = 3\sqrt{4x + 1} + 6\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Integrate \(\frac{dy}{dx}\)):</b> '
                r'\(y = \int 12(4x + 1)^{-1/2}\,dx = 12 \cdot \frac{(4x + 1)^{1/2}}{\frac{1}{2}\cdot 4} + c = 6\sqrt{4x + 1} + c\). [M1]</p>'
                r'<p><b>Bước 2 (Substitute \((2, 15)\) to find \(c\)):</b> '
                r'\(15 = 6\sqrt{4(2) + 1} + c = 6(3) + c = 18 + c \implies c = -3\). '
                r'Vậy \(y = 6\sqrt{4x + 1} - 3\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': '"Hence Find" Reverse Diff (Exp) (0606)',
            'q': r'<p>Given that \(\frac{d}{dx}\left(x e^{3x}\right) = (1 + 3x)e^{3x}\), hence find \(\displaystyle \int 6x e^{3x}\,dx\).</p>',
            'options': [
                r'\(2x e^{3x} - 2e^{3x} + c\)',
                r'\(2x e^{3x} - \frac{2}{3}e^{3x} + c\)',
                r'\(2x e^{3x} + \frac{2}{3}e^{3x} + c\)',
                r'\(6x e^{3x} - 2e^{3x} + c\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Rearrange the derivative identity):</b> '
                r'Từ \(\frac{d}{dx}(xe^{3x}) = e^{3x} + 3xe^{3x} \implies 3xe^{3x} = \frac{d}{dx}(xe^{3x}) - e^{3x}\). '
                r'Nhân hai vế với \(2\): \(6xe^{3x} = 2\frac{d}{dx}(xe^{3x}) - 2e^{3x}\). [M1]</p>'
                r'<p><b>Bước 2 (Integrate both sides):</b> '
                r'\(\int 6xe^{3x}\,dx = 2xe^{3x} - \int 2e^{3x}\,dx = 2xe^{3x} - \frac{2}{3}e^{3x} + c\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': '"Hence Find" Reverse Diff (Ln) (0606)',
            'q': r'<p>Given that \(\frac{d}{dx}\left(x^2 \ln x\right) = 2x\ln x + x\), hence find the exact value of \(\displaystyle \int_1^e 4x\ln x\,dx\).</p>',
            'options': [
                r'\(e^2 - 1\)',
                r'\(2e^2 - 1\)',
                r'\(2e^2 + 1\)',
                r'\(e^2 + 1\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Rewrite integrand using the given derivative):</b> '
                r'\(4x\ln x = 2\frac{d}{dx}(x^2\ln x) - 2x\), nên '
                r'\(\int_1^e 4x\ln x\,dx = \left[2x^2\ln x - x^2\right]_1^e\). [M1]</p>'
                r'<p><b>Bước 2 (Substitute limits \(e\) and \(1\)):</b> '
                r'\(\left(2e^2\ln e - e^2\right) - \left(2(1)^2\ln 1 - 1^2\right) = (2e^2 - e^2) - (0 - 1) = e^2 + 1\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Definite Integral — Logarithm (0606)',
            'q': r'<p>Evaluate \(\displaystyle \int_1^4 \frac{6}{2x + 1}\,dx\), giving your answer in simplest exact logarithmic form.</p>',
            'options': [
                r'\(3\ln 3\)',
                r'\(6\ln 3\)',
                r'\(3\ln 6\)',
                r'\(3\ln 9\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Find antiderivative):</b> '
                r'\(\int_1^4 \frac{6}{2x + 1}\,dx = \left[\frac{6}{2}\ln(2x + 1)\right]_1^4 = \left[3\ln(2x + 1)\right]_1^4\). [M1]</p>'
                r'<p><b>Bước 2 (Evaluate and simplify using log law):</b> '
                r'\(3\ln 9 - 3\ln 3 = 3\ln\left(\frac{9}{3}\right) = 3\ln 3\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Definite Integral — Trig Radians (0606)',
            'q': r'<p>Find the exact value of \(\displaystyle \int_0^{\pi/6} \left(4\cos(2x) + 3\sin(3x)\right)dx\).</p>',
            'options': [
                r'\(\sqrt{3} - 1\)',
                r'\(\sqrt{3}\)',
                r'\(\sqrt{3} + 1\)',
                r'\(2\sqrt{3} + 1\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Integrate term by term):</b> '
                r'\(\int_0^{\pi/6} (4\cos 2x + 3\sin 3x)\,dx = \left[2\sin(2x) - \cos(3x)\right]_0^{\pi/6}\). [M1]</p>'
                r'<p><b>Bước 2 (Substitute limits carefully — note \(\cos 0 = 1\)):</b> '
                r'\(\left(2\sin\frac{\pi}{3} - \cos\frac{\pi}{2}\right) - \left(2\sin 0 - \cos 0\right) = \left(2\cdot\frac{\sqrt{3}}{2} - 0\right) - (0 - 1) = \sqrt{3} + 1\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b> (Bẫy phổ biến là quên cận dưới \(\cos 0 = 1\)!)</p>'
            ),
        },
        {
            'tag': 'Definite Integral — Unknown Limit (0606)',
            'q': r'<p>Given that \(\displaystyle \int_0^k e^{2x}\,dx = 12\), find the exact value of \(k\).</p>',
            'options': [
                r'\(\ln 5\)',
                r'\(\frac{1}{2}\ln 24\)',
                r'\(\ln 25\)',
                r'\(\frac{1}{2}\ln 7\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Evaluate definite integral in terms of \(k\)):</b> '
                r'\(\left[\frac{1}{2}e^{2x}\right]_0^k = \frac{1}{2}\left(e^{2k} - e^0\right) = \frac{1}{2}(e^{2k} - 1) = 12\). [M1]</p>'
                r'<p><b>Bước 2 (Solve for \(k\)):</b> '
                r'\(e^{2k} - 1 = 24 \implies e^{2k} = 25 \implies 2k = \ln 25 = 2\ln 5 \implies k = \ln 5\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Area Under Curve — Below x-axis (0606)',
            'q': r'<p>Find the <b>total area</b> enclosed between the curve \(y = x^2 - 4\), the \(x\)-axis, and the lines \(x = 0\) and \(x = 3\).</p>',
            'options': [
                r'\(3\)',
                r'\(\frac{16}{3}\)',
                r'\(\frac{19}{3}\)',
                r'\(\frac{23}{3}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Split integral at the \(x\)-intercept \(x = 2\)):</b> '
                r'Trên \([0, 2]\), \(y \le 0\): \(\int_0^2 (x^2 - 4)\,dx = \left[\frac{x^3}{3} - 4x\right]_0^2 = \frac{8}{3} - 8 = -\frac{16}{3} \implies A_1 = \frac{16}{3}\). [M1]</p>'
                r'<p><b>Bước 2 (Evaluate \([2, 3]\) and add positive areas):</b> '
                r'Trên \([2, 3]\), \(y \ge 0\): \(A_2 = \left[\frac{x^3}{3} - 4x\right]_2^3 = (9 - 12) - \left(-\frac{16}{3}\right) = \frac{7}{3}\). '
                r'Tổng diện tích \(= \frac{16}{3} + \frac{7}{3} = \frac{23}{3}\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b> (Không lấy tích phân trực tiếp từ \(0\) đến \(3\) vì hai phần âm/dương triệt tiêu nhau!)</p>'
            ),
        },
        {
            'tag': 'Area Between Curve & Line (0606)',
            'q': r'<p>Find the exact area of the finite region bounded by the curve \(y = 6x - x^2\) and the straight line \(y = 2x\).</p>',
            'options': [
                r'\(\frac{16}{3}\)',
                r'\(\frac{32}{3}\)',
                r'\(16\)',
                r'\(\frac{64}{3}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Find intersection points):</b> '
                r'\(6x - x^2 = 2x \implies x^2 - 4x = 0 \implies x = 0\) hoặc \(x = 4\). [M1]</p>'
                r'<p><b>Bước 2 (Integrate top minus bottom):</b> '
                r'Trên \([0, 4]\), đường cong nằm trên đường thẳng: '
                r'\(A = \int_0^4 [(6x - x^2) - 2x]\,dx = \int_0^4 (4x - x^2)\,dx = \left[2x^2 - \frac{x^3}{3}\right]_0^4 = 32 - \frac{64}{3} = \frac{32}{3}\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Area Between Two Curves (0606)',
            'q': r'<p>Find the exact area of the finite region enclosed between the curves \(y = 8 - x^2\) and \(y = x^2\).</p>',
            'options': [
                r'\(\frac{32}{3}\)',
                r'\(16\)',
                r'\(\frac{64}{3}\)',
                r'\(\frac{128}{3}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Find intersection points):</b> '
                r'\(8 - x^2 = x^2 \implies 2x^2 = 8 \implies x = -2\) và \(x = 2\). [M1]</p>'
                r'<p><b>Bước 2 (Integrate \((y_{\text{upper}} - y_{\text{lower}})\) from \(-2\) to \(2\)):</b> '
                r'\(A = \int_{-2}^2 (8 - 2x^2)\,dx = 2\left[8x - \frac{2}{3}x^3\right]_0^2 = 2\left(16 - \frac{16}{3}\right) = \frac{64}{3}\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
    ],
}


# =============================================================================
# DRILL 4: Ch. 16 — Kinematics (Calculator Allowed, 12 Qs)
# Answer balance: A=3, B=3, C=3, D=3 -> A, D, B, C, D, A, C, B, B, A, D, C
# =============================================================================
DRILL_C16 = {
    'code': 'd0606_c16',
    'folder_key': 'drills_p2',
    'lecture_key': 'c16',
    'calculator_policy': 'calculator',
    'order_index': 9,
    'title': 'Ch. 16 Drill: Kinematics — Calculus of s(t), v(t), a(t) & Total Distance (0606)',
    'time_limit': '30',
    'intro_html': (
        '<p>Chinh phục <b>Chapter 16: Kinematics</b> của <b>Cambridge 0606</b>: vận dụng đạo hàm và tích phân giữa '
        'độ dịch chuyển \\(s(t)\\), vận tốc \\(v = \\frac{ds}{dt}\\) và gia tốc \\(a = \\frac{dv}{dt}\\); xác định thời điểm '
        'dừng tức thời (instantaneous rest \\(v = 0\\)), vận tốc cực đại/cực tiểu (\\(a = 0\\)), tính <b>tổng quãng đường '
        'đi được (Total Distance)</b> khi chất điểm đổi chiều chuyển động, và động học chứa hàm mũ/lượng giác/logarit.</p>'
    ),
    'questions': [
        {
            'tag': 'Displacement to Acceleration (0606)',
            'q': r'<p>A particle moves in a straight line such that its displacement \(s\text{ m}\) from a fixed point \(O\) at time \(t\text{ s}\) is \(s = t^3 - 6t^2 + 9t + 4\). Find its acceleration when \(t = 3\text{ s}\).</p>',
            'options': [
                r'\(6\text{ m/s}^2\)',
                r'\(0\text{ m/s}^2\)',
                r'\(4\text{ m/s}^2\)',
                r'\(18\text{ m/s}^2\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Differentiate twice to get \(v\) and \(a\)):</b> '
                r'\(v = \frac{ds}{dt} = 3t^2 - 12t + 9\), và \(a = \frac{dv}{dt} = 6t - 12\). [M1]</p>'
                r'<p><b>Bước 2 (Substitute \(t = 3\)):</b> '
                r'\(a(3) = 6(3) - 12 = 6\text{ m/s}^2\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b> (Lưu ý \(v(3) = 0\) là vận tốc chứ không phải gia tốc!)</p>'
            ),
        },
        {
            'tag': 'Instantaneous Rest (v = 0) (0606)',
            'q': r'<p>A particle moves in a straight line with displacement \(s = 2t^3 - 15t^2 + 36t\text{ m}\) at time \(t\text{ s}\) (\(t \ge 0\)). Find the distance between the two points where the particle is instantaneously at rest.</p>',
            'options': [
                r'\(5\text{ m}\)',
                r'\(27\text{ m}\)',
                r'\(28\text{ m}\)',
                r'\(1\text{ m}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Solve \(v = \frac{ds}{dt} = 0\)):</b> '
                r'\(v = 6t^2 - 30t + 36 = 6(t - 2)(t - 3) = 0 \implies t = 2\text{ s}\) và \(t = 3\text{ s}\). [M1]</p>'
                r'<p><b>Bước 2 (Find positions and distance between them):</b> '
                r'\(s(2) = 16 - 60 + 72 = 28\text{ m}\); \(s(3) = 54 - 135 + 108 = 27\text{ m}\). '
                r'Khoảng cách giữa hai điểm dừng \(= |27 - 28| = 1\text{ m}\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Maximum Velocity (a = 0) (0606)',
            'q': r'<p>A particle travels along a straight line with velocity \(v = 12t - 3t^2\text{ m/s}\) for \(t \ge 0\). Find the maximum velocity of the particle.</p>',
            'options': [
                r'\(2\text{ m/s}\)',
                r'\(12\text{ m/s}\)',
                r'\(16\text{ m/s}\)',
                r'\(24\text{ m/s}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Set acceleration \(a = \frac{dv}{dt} = 0\)):</b> '
                r'\(a = 12 - 6t = 0 \implies t = 2\text{ s}\). Vì \(\frac{da}{dt} = -6 < 0\), đây là vận tốc cực đại. [M1]</p>'
                r'<p><b>Bước 2 (Substitute \(t = 2\) into \(v\)):</b> '
                r'\(v_{\max} = 12(2) - 3(2^2) = 24 - 12 = 12\text{ m/s}\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Integrating a(t) to v(t) (0606)',
            'q': r'<p>A particle starts from rest at \(t = 0\) and moves in a straight line with acceleration \(a = 6t - 8\text{ m/s}^2\). Find the non-zero value of \(t\) when the particle is next instantaneously at rest.</p>',
            'options': [
                r'\(t = \frac{4}{3}\text{ s}\)',
                r'\(t = 2\text{ s}\)',
                r'\(t = \frac{8}{3}\text{ s}\)',
                r'\(t = \frac{16}{3}\text{ s}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Integrate \(a(t)\) with initial condition \(v(0) = 0\)):</b> '
                r'\(v = \int (6t - 8)\,dt = 3t^2 - 8t + c\). Vì \(v(0) = 0 \implies c = 0\), nên \(v = t(3t - 8)\). [M1]</p>'
                r'<p><b>Bước 2 (Solve \(v = 0\) for \(t > 0\)):</b> '
                r'\(3t - 8 = 0 \implies t = \frac{8}{3}\text{ s}\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Integrating a(t) Twice to s(t) (0606)',
            'q': r'<p>A particle moves in a straight line with acceleration \(a = 12t - 4\text{ m/s}^2\). At \(t = 1\text{ s}\), its velocity is \(5\text{ m/s}\) and its displacement from \(O\) is \(3\text{ m}\). Find its displacement from \(O\) when \(t = 2\text{ s}\).</p>',
            'options': [
                r'\(8\text{ m}\)',
                r'\(11\text{ m}\)',
                r'\(17\text{ m}\)',
                r'\(14\text{ m}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Find \(v(t)\) using \(v(1) = 5\)):</b> '
                r'\(v = 6t^2 - 4t + c_1\). Tại \(t = 1\): \(6 - 4 + c_1 = 5 \implies c_1 = 3 \implies v = 6t^2 - 4t + 3\). [M1]</p>'
                r'<p><b>Bước 2 (Find \(s(t)\) using \(s(1) = 3\), then evaluate \(s(2)\)):</b> '
                r'\(s = 2t^3 - 2t^2 + 3t + c_2\). Tại \(t = 1\): \(2 - 2 + 3 + c_2 = 3 \implies c_2 = 0\). '
                r'Do đó \(s(2) = 2(8) - 2(4) + 3(2) = 16 - 8 + 6 = 14\text{ m}\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Total Distance — Direction Reversal (0606)',
            'q': r'<p>A particle moves in a straight line with velocity \(v = 3t^2 - 12\text{ m/s}\) for \(t \ge 0\). Find the <b>total distance travelled</b> by the particle in the first \(3\) seconds (from \(t = 0\) to \(t = 3\)).</p>',
            'options': [
                r'\(23\text{ m}\)',
                r'\(9\text{ m}\)',
                r'\(16\text{ m}\)',
                r'\(25\text{ m}\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Check when \(v = 0\) inside \([0, 3]\)):</b> '
                r'\(3t^2 - 12 = 0 \implies t = 2\text{ s}\) (chất điểm đổi chiều tại \(t = 2\)). '
                r'Nguyên hàm \(s(t) = t^3 - 12t\) (chọn \(s(0) = 0\)). [M1]</p>'
                r'<p><b>Bước 2 (Sum magnitudes of displacement on \([0, 2]\) and \([2, 3]\)):</b> '
                r'\(s(0) = 0\), \(s(2) = 8 - 24 = -16\), \(s(3) = 27 - 36 = -9\). '
                r'Tổng quãng đường \(= |-16 - 0| + |-9 - (-16)| = 16 + 7 = 23\text{ m}\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b> (Cẩn thận bẫy lấy độ dịch chuyển ròng \(|-9| = 9\text{ m}\)!)</p>'
            ),
        },
        {
            'tag': 'Total Distance — Quadratic v(t) (0606)',
            'q': r'<p>A particle leaves a fixed point \(O\) at \(t = 0\) with velocity \(v = t^2 - 5t + 4\text{ m/s}\). Find the <b>total distance travelled</b> between \(t = 0\) and \(t = 4\text{ s}\).</p>',
            'options': [
                r'\(\frac{8}{3}\text{ m}\)',
                r'\(\frac{9}{2}\text{ m}\)',
                r'\(\frac{19}{3}\text{ m}\)',
                r'\(7\text{ m}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Find turning time in \((0, 4)\)):</b> '
                r'\(v = (t - 1)(t - 4) = 0 \implies\) chất điểm đổi chiều tại \(t = 1\text{ s}\). '
                r'\(s(t) = \frac{1}{3}t^3 - \frac{5}{2}t^2 + 4t\) với \(s(0) = 0\). [M1]</p>'
                r'<p><b>Bước 2 (Compute distance on \([0, 1]\) and \([1, 4]\)):</b> '
                r'\(s(1) = \frac{1}{3} - \frac{5}{2} + 4 = \frac{11}{6}\text{ m}\); \(s(4) = \frac{64}{3} - 40 + 16 = -\frac{8}{3}\text{ m}\). '
                r'Tổng quãng đường \(= \left|\frac{11}{6} - 0\right| + \left|-\frac{8}{3} - \frac{11}{6}\right| = \frac{11}{6} + \frac{27}{6} = \frac{38}{6} = \frac{19}{3}\text{ m}\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Exponential Kinematics — Rest (0606)',
            'q': r'<p>A particle moves in a straight line so that its displacement \(s\text{ m}\) from \(O\) at time \(t\text{ s}\) is given by \(s = 4e^{0.5t} - 6t - 4\). Find the value of \(t\), correct to \(3\) significant figures, when the particle is instantaneously at rest.</p>',
            'options': [
                r'\(1.10\text{ s}\)',
                r'\(2.20\text{ s}\)',
                r'\(0.811\text{ s}\)',
                r'\(2.77\text{ s}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Differentiate \(s(t)\) to find \(v(t)\)):</b> '
                r'\(v = \frac{ds}{dt} = 4(0.5)e^{0.5t} - 6 = 2e^{0.5t} - 6\). [M1]</p>'
                r'<p><b>Bước 2 (Solve \(v = 0\)):</b> '
                r'\(2e^{0.5t} = 6 \implies e^{0.5t} = 3 \implies 0.5t = \ln 3 \implies t = 2\ln 3 \approx 2.1972\dots \approx 2.20\text{ s}\) (3 s.f.). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Exponential Kinematics — Integration (0606)',
            'q': r'<p>A particle passes through \(O\) at \(t = 0\) and moves in a straight line with velocity \(v = 12 - 12e^{-0.5t}\text{ m/s}\). Find its displacement from \(O\) when \(t = 4\text{ s}\), correct to \(3\) significant figures.</p>',
            'options': [
                r'\(20.8\text{ m}\)',
                r'\(27.2\text{ m}\)',
                r'\(42.8\text{ m}\)',
                r'\(51.2\text{ m}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Integrate \(v(t)\) and find \(c\) from \(s(0) = 0\)):</b> '
                r'\(s = \int (12 - 12e^{-0.5t})\,dt = 12t + 24e^{-0.5t} + c\). '
                r'Tại \(t = 0\), \(s = 0 \implies 24e^0 + c = 0 \implies c = -24\). [M1]</p>'
                r'<p><b>Bước 2 (Evaluate at \(t = 4\)):</b> '
                r'\(s(4) = 12(4) + 24e^{-2} - 24 = 24 + 24e^{-2} \approx 24 + 3.248 = 27.2\text{ m}\) (3 s.f.). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Trig Kinematics — Acceleration (0606)',
            'q': r'<p>A particle oscillates along a straight line with displacement \(s = 5\sin(2t)\text{ m}\), where \(t\) is in seconds and angles are in radians. Find its acceleration when \(t = \frac{\pi}{12}\text{ s}\).</p>',
            'options': [
                r'\(-10\text{ m/s}^2\)',
                r'\(10\text{ m/s}^2\)',
                r'\(-5\text{ m/s}^2\)',
                r'\(-17.3\text{ m/s}^2\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Differentiate twice in radians):</b> '
                r'\(v = 10\cos(2t)\), và \(a = \frac{dv}{dt} = -20\sin(2t)\). [M1]</p>'
                r'<p><b>Bước 2 (Substitute \(t = \frac{\pi}{12}\)):</b> '
                r'\(a = -20\sin\left(\frac{\pi}{6}\right) = -20 \times \frac{1}{2} = -10\text{ m/s}^2\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Trig Kinematics — Total Distance (0606)',
            'q': r'<p>A particle starts at \(O\) when \(t = 0\) and moves with velocity \(v = 8\cos(2t)\text{ m/s}\) (\(t\) in seconds, angles in radians). Find the <b>total distance travelled</b> by the particle from \(t = 0\) to \(t = \frac{\pi}{2}\text{ s}\).</p>',
            'options': [
                r'\(0\text{ m}\)',
                r'\(4\text{ m}\)',
                r'\(16\text{ m}\)',
                r'\(8\text{ m}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Find where \(v = 0\) and integrate to \(s(t)\)):</b> '
                r'\(\cos(2t) = 0 \implies 2t = \frac{\pi}{2} \implies t = \frac{\pi}{4}\) (đổi chiều giữa khoảng \([0, \frac{\pi}{2}]\)). '
                r'\(s(t) = \int 8\cos(2t)\,dt = 4\sin(2t)\) (do \(s(0) = 0\)). [M1]</p>'
                r'<p><b>Bước 2 (Sum both segments):</b> '
                r'\(s(0) = 0\), \(s\left(\frac{\pi}{4}\right) = 4\sin\left(\frac{\pi}{2}\right) = 4\), \(s\left(\frac{\pi}{2}\right) = 4\sin(\pi) = 0\). '
                r'Tổng quãng đường \(= |4 - 0| + |0 - 4| = 8\text{ m}\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b> (Chú ý: độ dịch chuyển ròng bằng \(0\text{ m}\), nhưng tổng quãng đường là \(8\text{ m}\)!)</p>'
            ),
        },
        {
            'tag': 'Reciprocal/Ln Kinematics (0606)',
            'q': r'<p>A particle moves along a straight line with velocity \(v = \frac{12}{2t + 1} - 3\text{ m/s}\) for \(t \ge 0\). Given that \(s = 0\) when \(t = 0\), find the exact displacement \(s\) when the particle comes to instantaneous rest.</p>',
            'options': [
                r'\(6\ln 2 - \frac{9}{2}\text{ m}\)',
                r'\(12\ln 4 - \frac{9}{2}\text{ m}\)',
                r'\(12\ln 2 - \frac{9}{2}\text{ m}\)',
                r'\(12\ln 2 - 3\text{ m}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Find rest time \(v = 0\) and integrate \(v(t)\)):</b> '
                r'\(\frac{12}{2t + 1} = 3 \implies 2t + 1 = 4 \implies t = \frac{3}{2}\text{ s}\). '
                r'\(s = \int \left(\frac{12}{2t + 1} - 3\right)dt = 6\ln(2t + 1) - 3t + c\). Vì \(s(0) = 0 \implies c = 0\). [M1]</p>'
                r'<p><b>Bước 2 (Substitute \(t = \frac{3}{2}\) and simplify):</b> '
                r'\(s = 6\ln(4) - 3\left(\frac{3}{2}\right) = 6(2\ln 2) - \frac{9}{2} = 12\ln 2 - \frac{9}{2}\text{ m}\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
    ],
}


# =============================================================================
# DRILL 5: Paper 1 Non-Calc Specialist 1 (15 Qs, Non-Calculator)
# Topics: Surds, Indices, Logs, Circle (2025+), Polynomials, Modulus, Discriminant, Functions
# Answer balance: A=4, B=4, C=4, D=3 -> B, D, A, C, B, A, C, D, A, B, C, D, A, C, B
# =============================================================================
DRILL_NC1 = {
    'code': 'd0606_nc1',
    'folder_key': 'non_calc',
    'lecture_key': 'rev',
    'calculator_policy': 'non-calculator',
    'order_index': 1,
    'title': '🚫 0606 Paper 1 Non-Calc Specialist 1: Surds, Logs, Polynomials & Circle (2025–2027)',
    'time_limit': '35',
    'intro_html': (
        '<p>Bộ đề chuyên biệt <b>Paper 1 Non-Calculator (2025–2027) — Phần 1</b> (15 câu chuẩn đề thi Cambridge 0606/1x): '
        'rèn kỹ năng tính toán chính xác <b>100% không dùng máy tính</b> xuyên suốt các chuyên đề đại số & hình học giải tích: '
        'trục căn thức (Surds), phương trình mũ & logarit, <b>phương trình đường tròn & tiếp tuyến (chuyên đề mới 2025+)</b>, '
        'định lý dư & nhân tử bậc ba (Factor/Remainder Theorem), trị tuyệt đối (Modulus), biệt thức tiếp xúc (Discriminant) '
        'và miền xác định / miền giá trị / hàm ngược.</p>'
    ),
    'questions': [
        {
            'tag': 'Surds Rationalisation (Paper 1)',
            'q': r'<p>Without using a calculator, express \(\frac{11 + 3\sqrt{5}}{3 - \sqrt{5}}\) in the form \(a + b\sqrt{5}\), where \(a\) and \(b\) are integers.</p>',
            'options': [
                r'\(12 - 5\sqrt{5}\)',
                r'\(12 + 5\sqrt{5}\)',
                r'\(9 + 5\sqrt{5}\)',
                r'\(12 + 4\sqrt{5}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Multiply numerator and denominator by conjugate \(3 + \sqrt{5}\)):</b> '
                r'\(\frac{(11 + 3\sqrt{5})(3 + \sqrt{5})}{(3 - \sqrt{5})(3 + \sqrt{5})} = \frac{33 + 11\sqrt{5} + 9\sqrt{5} + 15}{9 - 5}\). [M1]</p>'
                r'<p><b>Bước 2 (Simplify):</b> '
                r'\(\frac{48 + 20\sqrt{5}}{4} = 12 + 5\sqrt{5}\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Surd Geometry (Paper 1)',
            'q': r'<p>A right-angled triangle has base \((4 + \sqrt{3})\text{ cm}\) and area \((15 + 7\sqrt{3})\text{ cm}^2\). Find the exact height of the triangle in the form \(p + q\sqrt{3}\), where \(p\) and \(q\) are integers.</p>',
            'options': [
                r'\(3 + \sqrt{3}\text{ cm}\)',
                r'\(6 - 2\sqrt{3}\text{ cm}\)',
                r'\(8 + 2\sqrt{3}\text{ cm}\)',
                r'\(6 + 2\sqrt{3}\text{ cm}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Use \(\text{Area} = \frac{1}{2}bh\) and rationalise):</b> '
                r'\(h = \frac{2(15 + 7\sqrt{3})}{4 + \sqrt{3}} = \frac{(30 + 14\sqrt{3})(4 - \sqrt{3})}{16 - 3}\). [M1]</p>'
                r'<p><b>Bước 2 (Expand and divide by \(13\)):</b> '
                r'\(h = \frac{120 - 30\sqrt{3} + 56\sqrt{3} - 42}{13} = \frac{78 + 26\sqrt{3}}{13} = 6 + 2\sqrt{3}\text{ cm}\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b> (Bẫy hay gặp: quên nhân \(2\) từ công thức \(\frac{1}{2}bh\).)</p>'
            ),
        },
        {
            'tag': 'Indices Equation (Paper 1)',
            'q': r'<p>Solve the exact equation \(2^{2x + 1} - 9(2^x) + 4 = 0\).</p>',
            'options': [
                r'\(x = -1\) or \(x = 2\)',
                r'\(x = \frac{1}{2}\) or \(x = 4\)',
                r'\(x = 1\) or \(x = 2\)',
                r'\(x = -2\) or \(x = 1\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Substitute \(u = 2^x\)):</b> '
                r'\(2(2^x)^2 - 9(2^x) + 4 = 0 \implies 2u^2 - 9u + 4 = 0 \implies (2u - 1)(u - 4) = 0\). [M1]</p>'
                r'<p><b>Bước 2 (Convert back to \(x\)):</b> '
                r'\(2^x = \frac{1}{2} = 2^{-1} \implies x = -1\); hoặc \(2^x = 4 = 2^2 \implies x = 2\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Exact Log Equation (Paper 1)',
            'q': r'<p>Solve the exact equation \(\log_2(x) + \log_2(x - 2) = 3\).</p>',
            'options': [
                r'\(x = -2\) or \(x = 4\)',
                r'\(x = 5\)',
                r'\(x = 4\) only',
                r'\(x = 3\) only',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Combine logs and convert to exponential form):</b> '
                r'Điều kiện xác định: \(x > 2\). '
                r'\(\log_2[x(x - 2)] = 3 \implies x(x - 2) = 2^3 = 8 \implies x^2 - 2x - 8 = 0\). [M1]</p>'
                r'<p><b>Bước 2 (Factorise and reject invalid root):</b> '
                r'\((x - 4)(x + 2) = 0 \implies x = 4\) hoặc \(x = -2\). Vì \(x > 2\), loại \(x = -2\), nhận duy nhất \(x = 4\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Log Change of Base (Paper 1)',
            'q': r'<p>Solve the exact equation \(\log_9(x) + \log_3(x) = 6\).</p>',
            'options': [
                r'\(x = 27\)',
                r'\(x = 81\)',
                r'\(x = 9\)',
                r'\(x = 243\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Change base from \(9\) to \(3\)):</b> '
                r'\(\log_9 x = \frac{\log_3 x}{\log_3 9} = \frac{1}{2}\log_3 x\). '
                r'Phương trình trở thành \(\frac{3}{2}\log_3 x = 6\). [M1]</p>'
                r'<p><b>Bước 2 (Solve for \(x\)):</b> '
                r'\(\log_3 x = 4 \implies x = 3^4 = 81\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Circle Centre & Radius — 2025+ (Paper 1)',
            'q': r'<p>A circle has equation \(x^2 + y^2 - 8x + 6y - 11 = 0\). Find its centre and exact radius.</p>',
            'options': [
                r'Centre \((4, -3)\), radius \(6\)',
                r'Centre \((-4, 3)\), radius \(6\)',
                r'Centre \((4, -3)\), radius \(36\)',
                r'Centre \((4, -3)\), radius \(\sqrt{14}\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Complete the square in \(x\) and \(y\)):</b> '
                r'\((x - 4)^2 - 16 + (y + 3)^2 - 9 - 11 = 0 \implies (x - 4)^2 + (y + 3)^2 = 36\). [M1]</p>'
                r'<p><b>Bước 2 (Read centre and radius):</b> '
                r'Tâm đường tròn là \((4, -3)\) và bán kính \(r = \sqrt{36} = 6\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Circle Tangent Equation — 2025+ (Paper 1)',
            'q': r'<p>A circle with centre \(C(2, -1)\) passes through the point \(P(5, 3)\). Find the equation of the tangent to the circle at \(P\).</p>',
            'options': [
                r'\(4x - 3y = 11\)',
                r'\(3x + 4y = 2\)',
                r'\(3x + 4y = 27\)',
                r'\(3x - 4y = 3\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Find radius gradient & perpendicular tangent gradient):</b> '
                r'\(m_{CP} = \frac{3 - (-1)}{5 - 2} = \frac{4}{3}\). Vì tiếp tuyến vuông góc với bán kính \(CP\), nên \(m_t = -\frac{3}{4}\). [M1]</p>'
                r'<p><b>Bước 2 (Write equation through \(P(5, 3)\)):</b> '
                r'\(y - 3 = -\frac{3}{4}(x - 5) \implies 4y - 12 = -3x + 15 \implies 3x + 4y = 27\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Circle & Line Tangency — 2025+ (Paper 1)',
            'q': r'<p>The straight line \(y = 2x + k\) is tangent to the circle \((x - 1)^2 + (y + 2)^2 = 20\). Find the exact values of \(k\).</p>',
            'options': [
                r'\(k = 4\) or \(k = -12\)',
                r'\(k = 10\) or \(k = -10\)',
                r'\(k = 14\) or \(k = -6\)',
                r'\(k = 6\) or \(k = -14\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Substitute \(y = 2x + k\) into circle and set \(c = k + 2\)):</b> '
                r'\((x - 1)^2 + (2x + c)^2 = 20 \implies 5x^2 + (4c - 2)x + (c^2 - 19) = 0\). '
                r'Điều kiện tiếp xúc \(\Delta = 0\): \((4c - 2)^2 - 20(c^2 - 19) = 0\). [M1]</p>'
                r'<p><b>Bước 2 (Solve quadratic for \(c\) and \(k\)):</b> '
                r'\(-4c^2 - 16c + 384 = 0 \implies c^2 + 4c - 96 = 0 \implies (c + 12)(c - 8) = 0\). '
                r'Suy ra \(c = 8 \implies k = 6\), hoặc \(c = -12 \implies k = -14\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Factor & Remainder Theorem (Paper 1)',
            'q': r'<p>The polynomial \(p(x) = 2x^3 + ax^2 + bx - 6\) has \((x - 2)\) as a factor, and leaves a remainder of \(-12\) when divided by \((x + 1)\). Find the values of \(a\) and \(b\).</p>',
            'options': [
                r'\(a = -3,\ b = 1\)',
                r'\(a = 3,\ b = -11\)',
                r'\(a = -3,\ b = -1\)',
                r'\(a = -1,\ b = -3\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Apply Factor and Remainder Theorems):</b> '
                r'\(p(2) = 0 \implies 16 + 4a + 2b - 6 = 0 \implies 2a + b = -5\). '
                r'\(p(-1) = -12 \implies -2 + a - b - 6 = -12 \implies a - b = -4\). [M1]</p>'
                r'<p><b>Bước 2 (Solve simultaneous equations):</b> '
                r'Cộng hai phương trình: \(3a = -9 \implies a = -3\), suy ra \(b = a + 4 = 1\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Solving Cubic Equation (Paper 1)',
            'q': r'<p>Given that \((x + 2)\) is a factor of \(f(x) = 2x^3 - 3x^2 - 11x + 6\), find all three real roots of \(f(x) = 0\).</p>',
            'options': [
                r'\(x = -2,\ -\frac{1}{2},\ 3\)',
                r'\(x = -2,\ \frac{1}{2},\ 3\)',
                r'\(x = -2,\ \frac{1}{2},\ -3\)',
                r'\(x = 2,\ -\frac{1}{2},\ -3\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Divide \(f(x)\) by \((x + 2)\)):</b> '
                r'\(2x^3 - 3x^2 - 11x + 6 = (x + 2)(2x^2 - 7x + 3)\). [M1]</p>'
                r'<p><b>Bước 2 (Factorise the quadratic factor):</b> '
                r'\(2x^2 - 7x + 3 = (2x - 1)(x - 3)\), nên \(f(x) = (x + 2)(2x - 1)(x - 3) = 0\). '
                r'Ba nghiệm thực là \(x = -2,\ \frac{1}{2},\ 3\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Modulus Equation (Paper 1)',
            'q': r'<p>Solve the exact modulus equation \(|2x - 5| = |x + 4|\).</p>',
            'options': [
                r'\(x = 9\) only',
                r'\(x = -9\) or \(x = \frac{1}{3}\)',
                r'\(x = \frac{1}{3}\) or \(x = 9\)',
                r'\(x = -\frac{1}{3}\) or \(x = 9\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Split into two linear cases):</b> '
                r'\(2x - 5 = x + 4\) hoặc \(2x - 5 = -(x + 4)\). [M1]</p>'
                r'<p><b>Bước 2 (Solve each case):</b> '
                r'Trường hợp 1: \(x = 9\). Trường hợp 2: \(3x = 1 \implies x = \frac{1}{3}\). '
                r'Cả hai nghiệm đều thoả mãn phương trình gốc. [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Modulus Inequality (Paper 1)',
            'q': r'<p>Find the exact set of values of \(x\) satisfying \(|3x - 2| < x + 4\).</p>',
            'options': [
                r'\(x < -\frac{1}{2}\) or \(x > 3\)',
                r'\(-3 < x < \frac{1}{2}\)',
                r'\(-\frac{3}{2} < x < 3\)',
                r'\(-\frac{1}{2} < x < 3\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Rewrite \(|A| < B\) as \(-B < A < B\)):</b> '
                r'\(-(x + 4) < 3x - 2 < x + 4\) (với \(x + 4 > 0\)). [M1]</p>'
                r'<p><b>Bước 2 (Solve both inequalities):</b> '
                r'Bên trái: \(-x - 4 < 3x - 2 \implies 4x > -2 \implies x > -\frac{1}{2}\). '
                r'Bên phải: \(3x - 2 < x + 4 \implies 2x < 6 \implies x < 3\). '
                r'Kết hợp: \(-\frac{1}{2} < x < 3\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Discriminant & Non-Intersection (Paper 1)',
            'q': r'<p>Find the set of values of \(m\) for which the straight line \(y = mx - 4\) does <b>not</b> intersect the curve \(y = x^2 + 2x + 5\).</p>',
            'options': [
                r'\(-4 < m < 8\)',
                r'\(m < -4\) or \(m > 8\)',
                r'\(-8 < m < 4\)',
                r'\(-4 \le m \le 8\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Eliminate \(y\) and require discriminant \(\Delta < 0\)):</b> '
                r'\(x^2 + 2x + 5 = mx - 4 \implies x^2 + (2 - m)x + 9 = 0\). '
                r'Không có giao điểm thực \(\iff (2 - m)^2 - 4(1)(9) < 0\). [M1]</p>'
                r'<p><b>Bước 2 (Solve quadratic inequality):</b> '
                r'\((m - 2)^2 < 36 \implies -6 < m - 2 < 6 \implies -4 < m < 8\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Inverse Function & Domain (Paper 1)',
            'q': r'<p>The function \(f\) is defined by \(f(x) = x^2 - 6x + 11\) for \(x \ge 3\). Find \(f^{-1}(x)\) and state its domain.</p>',
            'options': [
                r'\(f^{-1}(x) = 3 - \sqrt{x - 2},\ x \ge 2\)',
                r'\(f^{-1}(x) = 3 + \sqrt{x - 2},\ x \ge 3\)',
                r'\(f^{-1}(x) = 3 + \sqrt{x - 2},\ x \ge 2\)',
                r'\(f^{-1}(x) = 3 + \sqrt{x + 2},\ x \ge -2\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Complete the square & find range of \(f\)):</b> '
                r'\(f(x) = (x - 3)^2 + 2\). Với \(x \ge 3\), miền giá trị của \(f\) là \(f(x) \ge 2\), nên miền xác định của \(f^{-1}\) là \(x \ge 2\). [M1]</p>'
                r'<p><b>Bước 2 (Rearrange for \(x\) using \(x \ge 3\)):</b> '
                r'\(y = (x - 3)^2 + 2 \implies x = 3 + \sqrt{y - 2}\) (chọn dấu \(+\) vì \(x \ge 3\)). '
                r'Suy ra \(f^{-1}(x) = 3 + \sqrt{x - 2}\) với \(x \ge 2\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Composite & Range of Functions (Paper 1)',
            'q': r'<p>The functions \(f\) and \(g\) are defined by \(f(x) = e^{2x} + 3\) for \(x \in \mathbb{R}\), and \(g(x) = \frac{1}{2}\ln(x - 1)\) for \(x > 1\). Find the exact value of \(fg(5)\) and the range of \(f\).</p>',
            'options': [
                r'\(fg(5) = 7\), range \(f(x) \ge 3\)',
                r'\(fg(5) = 7\), range \(f(x) > 3\)',
                r'\(fg(5) = 5\), range \(f(x) > 3\)',
                r'\(fg(5) = 19\), range \(f(x) > 3\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Evaluate \(g(5)\) then \(f(g(5))\)):</b> '
                r'\(g(5) = \frac{1}{2}\ln 4 = \ln 2\). '
                r'Do đó \(fg(5) = e^{2\ln 2} + 3 = e^{\ln 4} + 3 = 4 + 3 = 7\). [M1]</p>'
                r'<p><b>Bước 2 (State strict range of exponential function):</b> '
                r'Vì \(e^{2x} > 0\) với mọi \(x \in \mathbb{R}\), nên miền giá trị của \(f\) là \(f(x) > 3\) (dấu lớn hơn nghiêm ngặt). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
    ],
}


# =============================================================================
# DRILL 6: Paper 1 Non-Calc Specialist 2 (15 Qs, Non-Calculator)
# Topics: Exact Radian Trig, Circular Measure, Binomial, AP/GP S_inf, P&C,
#         Exact Diff/Tangents/Stationary, Exact Integrals/Areas, Exact Kinematics & Vectors
# Answer balance: A=4, B=3, C=4, D=4 -> C, A, D, B, A, C, D, A, B, C, D, A, C, B, D
# =============================================================================
DRILL_NC2 = {
    'code': 'd0606_nc2',
    'folder_key': 'non_calc',
    'lecture_key': 'rev',
    'calculator_policy': 'non-calculator',
    'order_index': 2,
    'title': '🚫 0606 Paper 1 Non-Calc Specialist 2: Exact Radian Trig, Series & Calculus (2025–2027)',
    'time_limit': '35',
    'intro_html': (
        '<p>Bộ đề chuyên biệt <b>Paper 1 Non-Calculator (2025–2027) — Phần 2</b> (15 câu chuẩn đề thi Cambridge 0606/1x): '
        'luyện tập giá trị chính xác <b>100% không máy tính</b> cho nửa sau chương trình: phương trình lượng giác theo radian '
        'trên \\([0, 2\\pi]\\), diện tích & chu vi viên phân (Segment) theo \\(\\pi\\) và \\(\\sqrt{3}\\), nhị thức Newton '
        '(Binomial Theorem), cấp số cộng/nhân & tổng vô hạn \\(S_\\infty\\), tổ hợp, đạo hàm/tiếp tuyến/pháp tuyến & tích phân '
        'chính xác chứa \\(e, \\ln, \\pi\\), động học và vectơ đơn vị (không Relative Velocity).</p>'
    ),
    'questions': [
        {
            'tag': 'Exact Radian Trig Equation (Paper 1)',
            'q': r'<p>Solve the equation \(2\sin^2 x - \sin x - 1 = 0\) for \(0 \le x \le 2\pi\), giving exact answers in terms of \(\pi\).</p>',
            'options': [
                r'\(x = \frac{\pi}{6},\ \frac{5\pi}{6},\ \frac{3\pi}{2}\)',
                r'\(x = \frac{\pi}{2},\ \frac{4\pi}{3},\ \frac{5\pi}{3}\)',
                r'\(x = \frac{\pi}{2},\ \frac{7\pi}{6},\ \frac{11\pi}{6}\)',
                r'\(x = \frac{\pi}{2},\ \frac{7\pi}{6}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Factorise quadratic in \(\sin x\)):</b> '
                r'\((2\sin x + 1)(\sin x - 1) = 0 \implies \sin x = 1\) hoặc \(\sin x = -\frac{1}{2}\). [M1]</p>'
                r'<p><b>Bước 2 (Find all exact solutions in \([0, 2\pi]\)):</b> '
                r'\(\sin x = 1 \implies x = \frac{\pi}{2}\). '
                r'\(\sin x = -\frac{1}{2}\) (góc phần tư III và IV, góc cơ bản \(\frac{\pi}{6}\)) \(\implies x = \pi + \frac{\pi}{6} = \frac{7\pi}{6}\) và \(x = 2\pi - \frac{\pi}{6} = \frac{11\pi}{6}\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Exact Compound-Angle Tan Eq (Paper 1)',
            'q': r'<p>Solve \(\sqrt{3}\tan\left(2x - \frac{\pi}{3}\right) = 1\) for \(0 \le x \le \pi\), giving exact answers in terms of \(\pi\).</p>',
            'options': [
                r'\(x = \frac{\pi}{4},\ \frac{3\pi}{4}\)',
                r'\(x = \frac{\pi}{3},\ \frac{5\pi}{6}\)',
                r'\(x = \frac{\pi}{4}\) only',
                r'\(x = \frac{\pi}{12},\ \frac{7\pi}{12}\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Transform the domain for \(u = 2x - \frac{\pi}{3}\)):</b> '
                r'\(\tan u = \frac{1}{\sqrt{3}}\) với \(-\frac{\pi}{3} \le u \le \frac{5\pi}{3}\). '
                r'Các nghiệm của \(u\) trong miền này là \(u = \frac{\pi}{6}\) và \(u = \frac{\pi}{6} + \pi = \frac{7\pi}{6}\). [M1]</p>'
                r'<p><b>Bước 2 (Solve back for \(x\)):</b> '
                r'\(2x = \frac{\pi}{6} + \frac{\pi}{3} = \frac{\pi}{2} \implies x = \frac{\pi}{4}\); '
                r'\(2x = \frac{7\pi}{6} + \frac{\pi}{3} = \frac{3\pi}{2} \implies x = \frac{3\pi}{4}\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Exact Segment Area — π/3 (Paper 1)',
            'q': r'<p>A circle has radius \(6\text{ cm}\) and a sector \(OAB\) subtends an angle of \(\frac{\pi}{3}\) radians at the centre \(O\). Find the exact area of the minor segment cut off by the chord \(AB\).</p>',
            'options': [
                r'\(6\pi - 18\sqrt{3}\text{ cm}^2\)',
                r'\(12\pi - 9\sqrt{3}\text{ cm}^2\)',
                r'\(6\pi - 9\text{ cm}^2\)',
                r'\(6\pi - 9\sqrt{3}\text{ cm}^2\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Compute exact sector area and triangle area):</b> '
                r'Diện tích hình quạt: \(A_{\text{sector}} = \frac{1}{2}r^2\theta = \frac{1}{2}(36)\left(\frac{\pi}{3}\right) = 6\pi\text{ cm}^2\). '
                r'Diện tích \(\triangle OAB\): \(A_{\triangle} = \frac{1}{2}r^2\sin\theta = \frac{1}{2}(36)\left(\frac{\sqrt{3}}{2}\right) = 9\sqrt{3}\text{ cm}^2\). [M1]</p>'
                r'<p><b>Bước 2 (Subtract to get segment area):</b> '
                r'\(A_{\text{segment}} = 6\pi - 9\sqrt{3}\text{ cm}^2\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Exact Segment Perimeter (Paper 1)',
            'q': r'<p>In a circle of radius \(8\text{ cm}\), chord \(PQ\) subtends an angle of \(\frac{2\pi}{3}\) radians at the centre \(O\). Find the exact perimeter of the minor segment bounded by chord \(PQ\) and minor arc \(PQ\).</p>',
            'options': [
                r'\(\frac{16\pi}{3} + 8\text{ cm}\)',
                r'\(\frac{16\pi}{3} + 8\sqrt{3}\text{ cm}\)',
                r'\(\frac{8\pi}{3} + 8\sqrt{3}\text{ cm}\)',
                r'\(\frac{16\pi}{3} + 16\sqrt{3}\text{ cm}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Find minor arc length and chord length):</b> '
                r'Độ dài cung \(PQ = r\theta = 8\cdot\frac{2\pi}{3} = \frac{16\pi}{3}\text{ cm}\). '
                r'Độ dài dây cung \(PQ = 2r\sin\left(\frac{\theta}{2}\right) = 16\sin\left(\frac{\pi}{3}\right) = 8\sqrt{3}\text{ cm}\). [M1]</p>'
                r'<p><b>Bước 2 (Add arc and chord):</b> '
                r'Chu vi viên phân \(= \frac{16\pi}{3} + 8\sqrt{3}\text{ cm}\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Binomial — Term Independent of x (Paper 1)',
            'q': r'<p>Find the term independent of \(x\) in the binomial expansion of \(\left(2x - \frac{1}{x^2}\right)^6\).</p>',
            'options': [
                r'\(240\)',
                r'\(-240\)',
                r'\(160\)',
                r'\(60\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Write general term and set power of \(x\) to \(0\)):</b> '
                r'\(T_{r+1} = \binom{6}{r}(2x)^{6-r}(-x^{-2})^r = \binom{6}{r}2^{6-r}(-1)^r x^{6 - 3r}\). '
                r'Số hạng không chứa \(x \iff 6 - 3r = 0 \implies r = 2\). [M1]</p>'
                r'<p><b>Bước 2 (Evaluate coefficient at \(r = 2\)):</b> '
                r'\(\binom{6}{2}\cdot 2^4 \cdot (-1)^2 = 15 \times 16 \times 1 = 240\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Binomial Product Coefficient (Paper 1)',
            'q': r'<p>Find the exact coefficient of \(x^2\) in the expansion of \((1 - 3x)(2 + x)^5\).</p>',
            'options': [
                r'\(80\)',
                r'\(-320\)',
                r'\(-160\)',
                r'\(320\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Expand \((2 + x)^5\) up to \(x^2\)):</b> '
                r'\((2 + x)^5 = 2^5 + \binom{5}{1}2^4 x + \binom{5}{2}2^3 x^2 + \dots = 32 + 80x + 80x^2 + \dots\) [M1]</p>'
                r'<p><b>Bước 2 (Collect \(x^2\) terms in \((1 - 3x)(32 + 80x + 80x^2)\)):</b> '
                r'Hệ số của \(x^2\) là \(1(80) + (-3)(80) = 80 - 240 = -160\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Arithmetic Progression Sum (Paper 1)',
            'q': r'<p>In an arithmetic progression, the \(4\text{th}\) term is \(17\) and the \(10\text{th}\) term is \(41\). Find the exact sum of the first \(20\) terms.</p>',
            'options': [
                r'\(810\)',
                r'\(900\)',
                r'\(780\)',
                r'\(860\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Find \(a\) and \(d\)):</b> '
                r'\(a + 3d = 17\) và \(a + 9d = 41\). Trừ hai phương trình: \(6d = 24 \implies d = 4\), suy ra \(a = 17 - 12 = 5\). [M1]</p>'
                r'<p><b>Bước 2 (Apply \(S_n = \frac{n}{2}[2a + (n - 1)d]\)):</b> '
                r'\(S_{20} = \frac{20}{2}[2(5) + 19(4)] = 10(10 + 76) = 860\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Geometric Progression — Exact S_∞ (Paper 1)',
            'q': r'<p>A convergent geometric progression has first term \(18\) and second term \(-12\). Find the exact sum to infinity \(S_\infty\).</p>',
            'options': [
                r'\(\frac{54}{5}\)',
                r'\(54\)',
                r'\(-\frac{54}{5}\)',
                r'\(\frac{36}{5}\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Find common ratio \(r\) and check \(|r| < 1\)):</b> '
                r'\(r = \frac{-12}{18} = -\frac{2}{3}\). Vì \(|r| = \frac{2}{3} < 1\), cấp số nhân hội tụ. [M1]</p>'
                r'<p><b>Bước 2 (Evaluate \(S_\infty = \frac{a}{1 - r}\)):</b> '
                r'\(S_\infty = \frac{18}{1 - \left(-\frac{2}{3}\right)} = \frac{18}{\frac{5}{3}} = \frac{54}{5}\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b> (Cẩn thận bẫy dấu trừ kép \(1 - (-\frac{2}{3}) = \frac{5}{3}\)!)</p>'
            ),
        },
        {
            'tag': 'Combinations with Restriction (Paper 1)',
            'q': r'<p>A committee of \(4\) students is to be selected from \(5\) boys and \(4\) girls. How many different committees can be formed if the committee must contain <b>at least \(3\) girls</b>?</p>',
            'options': [
                r'\(20\)',
                r'\(21\)',
                r'\(24\)',
                r'\(40\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Split into mutually exclusive cases):</b> '
                r'Trường hợp 1 (3 nữ, 1 nam): \(\binom{4}{3}\times\binom{5}{1} = 4 \times 5 = 20\). '
                r'Trường hợp 2 (4 nữ, 0 nam): \(\binom{4}{4}\times\binom{5}{0} = 1 \times 1 = 1\). [M1]</p>'
                r'<p><b>Bước 2 (Sum both cases):</b> '
                r'Tổng số cách chọn \(= 20 + 1 = 21\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Exact Normal with e^x (Paper 1)',
            'q': r'<p>Find the exact equation of the <b>normal</b> to the curve \(y = 2e^{3x} - 4x\) at the point where \(x = 0\).</p>',
            'options': [
                r'\(y = 2x + 2\)',
                r'\(y = -\frac{1}{2}x\)',
                r'\(y = -\frac{1}{2}x + 2\)',
                r'\(y = \frac{1}{2}x + 2\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Find point and tangent gradient at \(x = 0\)):</b> '
                r'Tại \(x = 0\): \(y = 2e^0 - 0 = 2 \implies\) điểm \((0, 2)\). '
                r'\(\frac{dy}{dx} = 6e^{3x} - 4 \implies m_t = 6(1) - 4 = 2\). [M1]</p>'
                r'<p><b>Bước 2 (Write equation of normal):</b> '
                r'\(m_n = -\frac{1}{2}\), đi qua tung độ gốc \((0, 2)\) nên \(y = -\frac{1}{2}x + 2\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Exact Stationary Point with ln x (Paper 1)',
            'q': r'<p>Find the exact coordinates and nature of the stationary point on the curve \(y = 2x - 6\ln x\) for \(x > 0\).</p>',
            'options': [
                r'\((3,\ 6 - 6\ln 3)\), maximum',
                r'\(\left(\frac{1}{3},\ \frac{2}{3} + 6\ln 3\right)\), minimum',
                r'\((3,\ 6 - \ln 3)\), minimum',
                r'\((3,\ 6 - 6\ln 3)\), minimum',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Differentiate and solve \(\frac{dy}{dx} = 0\)):</b> '
                r'\(\frac{dy}{dx} = 2 - \frac{6}{x} = 0 \implies x = 3\). Khi đó \(y = 2(3) - 6\ln 3 = 6 - 6\ln 3\). [M1]</p>'
                r'<p><b>Bước 2 (Classify nature via second derivative):</b> '
                r'\(\frac{d^2y}{dx^2} = \frac{6}{x^2}\). Tại \(x = 3\), \(\frac{d^2y}{dx^2} = \frac{2}{3} > 0 \implies\) điểm cực tiểu (minimum). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
        {
            'tag': 'Exact Definite Integral with e (Paper 1)',
            'q': r'<p>Find the exact value of \(\displaystyle \int_0^{\ln 2} \left(4e^{2x} - 3e^x\right)dx\).</p>',
            'options': [
                r'\(3\)',
                r'\(2\)',
                r'\(1\)',
                r'\(9\)',
            ],
            'answer': 'A',
            'explanation': (
                r'<p><b>Bước 1 (Integrate and apply limits):</b> '
                r'\(\int_0^{\ln 2} (4e^{2x} - 3e^x)\,dx = \left[2e^{2x} - 3e^x\right]_0^{\ln 2}\). [M1]</p>'
                r'<p><b>Bước 2 (Use \(e^{\ln 2} = 2\) and \(e^{2\ln 2} = 4\)):</b> '
                r'\(\left(2(4) - 3(2)\right) - \left(2(1) - 3(1)\right) = (8 - 6) - (2 - 3) = 2 - (-1) = 3\). [A1]</p>'
                r'<p><b>Đáp án đúng: A.</b></p>'
            ),
        },
        {
            'tag': 'Exact Area with sec² & sin (Paper 1)',
            'q': r'<p>Find the exact area bounded by the curve \(y = \sec^2 x + 2\sin x\), the \(x\)-axis, and the lines \(x = 0\) and \(x = \frac{\pi}{4}\).</p>',
            'options': [
                r'\(1 - \sqrt{2}\)',
                r'\(3 + \sqrt{2}\)',
                r'\(3 - \sqrt{2}\)',
                r'\(1 + \sqrt{2}\)',
            ],
            'answer': 'C',
            'explanation': (
                r'<p><b>Bước 1 (Set up definite integral on \([0, \frac{\pi}{4}]\)):</b> '
                r'Vì \(y > 0\) trên \([0, \frac{\pi}{4}]\): \(A = \int_0^{\pi/4} (\sec^2 x + 2\sin x)\,dx = \left[\tan x - 2\cos x\right]_0^{\pi/4}\). [M1]</p>'
                r'<p><b>Bước 2 (Evaluate exact trig values):</b> '
                r'\(\left(\tan\frac{\pi}{4} - 2\cos\frac{\pi}{4}\right) - (\tan 0 - 2\cos 0) = \left(1 - 2\cdot\frac{\sqrt{2}}{2}\right) - (0 - 2) = 3 - \sqrt{2}\). [A1]</p>'
                r'<p><b>Đáp án đúng: C.</b></p>'
            ),
        },
        {
            'tag': 'Exact Trig Kinematics (Paper 1)',
            'q': r'<p>A particle starts from \(O\) at \(t = 0\) and moves in a straight line with velocity \(v = 6\sin(3t)\text{ m/s}\) (\(t\) in seconds, angles in radians). Find its exact displacement from \(O\) when it first comes to instantaneous rest for \(t > 0\).</p>',
            'options': [
                r'\(2\text{ m}\)',
                r'\(4\text{ m}\)',
                r'\(0\text{ m}\)',
                r'\(12\text{ m}\)',
            ],
            'answer': 'B',
            'explanation': (
                r'<p><b>Bước 1 (Find first rest time \(t > 0\) and integrate \(v\)):</b> '
                r'\(6\sin(3t) = 0 \implies 3t = \pi \implies t = \frac{\pi}{3}\text{ s}\). '
                r'\(s = \int_0^{\pi/3} 6\sin(3t)\,dt = \left[-2\cos(3t)\right]_0^{\pi/3}\). [M1]</p>'
                r'<p><b>Bước 2 (Evaluate):</b> '
                r'\((-2\cos\pi) - (-2\cos 0) = 2 - (-2) = 4\text{ m}\). [A1]</p>'
                r'<p><b>Đáp án đúng: B.</b></p>'
            ),
        },
        {
            'tag': 'Exact Unit Vector — Non-Calc (Paper 1)',
            'q': r'<p>Relative to an origin \(O\), points \(A\) and \(B\) have position vectors \(\overrightarrow{OA} = 3\mathbf{i} - 5\mathbf{j}\) and \(\overrightarrow{OB} = 11\mathbf{i} + \mathbf{j}\). Find the exact unit vector in the direction of \(\overrightarrow{AB}\).</p>',
            'options': [
                r'\(\frac{4}{5}\mathbf{i} - \frac{3}{5}\mathbf{j}\)',
                r'\(-\frac{4}{5}\mathbf{i} - \frac{3}{5}\mathbf{j}\)',
                r'\(\frac{7}{5}\mathbf{i} - \frac{2}{5}\mathbf{j}\)',
                r'\(\frac{4}{5}\mathbf{i} + \frac{3}{5}\mathbf{j}\)',
            ],
            'answer': 'D',
            'explanation': (
                r'<p><b>Bước 1 (Compute \(\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA}\) and its magnitude):</b> '
                r'\(\overrightarrow{AB} = (11 - 3)\mathbf{i} + (1 - (-5))\mathbf{j} = 8\mathbf{i} + 6\mathbf{j}\). '
                r'\(|\overrightarrow{AB}| = \sqrt{8^2 + 6^2} = \sqrt{100} = 10\). [M1]</p>'
                r'<p><b>Bước 2 (Divide by magnitude and simplify):</b> '
                r'Vectơ đơn vị \(= \frac{1}{10}(8\mathbf{i} + 6\mathbf{j}) = \frac{4}{5}\mathbf{i} + \frac{3}{5}\mathbf{j}\). [A1]</p>'
                r'<p><b>Đáp án đúng: D.</b></p>'
            ),
        },
    ],
}


DRILLS_0606_P2B = [
    DRILL_C13,
    DRILL_C14,
    DRILL_C15,
    DRILL_C16,
    DRILL_NC1,
    DRILL_NC2,
]


# =============================================================================
# MATHEMATICAL & STRUCTURAL SELF-VERIFICATION (ALL 78 QUESTIONS)
# =============================================================================
def _simpson(f, a, b, n=1000):
    """Composite Simpson's rule for high-precision numerical integral verification."""
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 == 1 else 2) * f(a + i * h)
    return s * h / 3.0


def _num_deriv(f, x, h=1e-6):
    """Central difference numerical derivative."""
    return (f(x + h) - f(x - h)) / (2.0 * h)


def _opt(drill, q_num):
    """Returns the selected option text for 1-indexed q_num."""
    q = drill['questions'][q_num - 1]
    idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[q['answer']]
    return q['options'][idx]


def verify_all_math():
    """
    Independently verifies EVERY mathematical calculation across all 78 questions
    AND validates every drill using `validate_igcse_drill` from `scripts.igcse_maths_pipeline`.
    """
    # -------------------------------------------------------------------------
    # 1. Structural, Metadata, KaTeX, Balance & Syllabus-Rule Verification
    # -------------------------------------------------------------------------
    assert len(DRILLS_0606_P2B) == 6, f'Expected 6 drills, got {len(DRILLS_0606_P2B)}'
    expected_meta = [
        ('d0606_c13', 'drills_p2', 'c13', 'non-calculator', 6, 12),
        ('d0606_c14', 'drills_p2', 'c14', 'calculator', 7, 12),
        ('d0606_c15', 'drills_p2', 'c15', 'calculator', 8, 12),
        ('d0606_c16', 'drills_p2', 'c16', 'calculator', 9, 12),
        ('d0606_nc1', 'non_calc', 'rev', 'non-calculator', 1, 15),
        ('d0606_nc2', 'non_calc', 'rev', 'non-calculator', 2, 15),
    ]
    total_qs = 0
    required_keys = {
        'code', 'folder_key', 'lecture_key', 'calculator_policy',
        'order_index', 'title', 'time_limit', 'intro_html', 'questions',
    }
    ctrl_re = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f\t\r]')
    opt_prefix_re = re.compile(r'^\s*[A-D][\.\)\:]\s*')

    for drill, (code, fkey, lkey, policy, oidx, n_qs) in zip(DRILLS_0606_P2B, expected_meta):
        assert required_keys.issubset(drill.keys()), f'{code}: missing keys {required_keys - set(drill.keys())}'
        assert drill['code'] == code
        assert drill['folder_key'] == fkey
        assert drill['lecture_key'] == lkey
        assert drill['calculator_policy'] == policy
        assert drill['order_index'] == oidx
        assert drill['time_limit'] in ('30', '35')
        assert len(drill['questions']) == n_qs, f'{code}: expected {n_qs} Qs, got {len(drill["questions"])}'
        total_qs += n_qs

        # Check answer balance strictly
        counts = Counter(q['answer'] for q in drill['questions'])
        if n_qs == 12:
            assert all(counts[k] == 3 for k in 'ABCD'), f'{code}: 12-Q drill must be 3-3-3-3, got {dict(counts)}'
        else:
            assert all(counts[k] in (3, 4) for k in 'ABCD'), f'{code}: 15-Q drill must be 3-4 each, got {dict(counts)}'

        # Check zero Relative Velocity in Ch. 13 vectors drill (2025-2027 rule)
        if code == 'd0606_c13':
            for idx, q in enumerate(drill['questions'], 1):
                blob = (q['tag'] + ' ' + q['q'] + ' ' + ' '.join(q['options']) + ' ' + q['explanation']).lower()
                for forbidden in ('relative velocity', 'river', 'current', 'wind', 'bearing', 'speed', 'boat', 'aircraft'):
                    assert forbidden not in blob, f'd0606_c13 Q{idx} contains forbidden term "{forbidden}"'

        # Per-question formatting, KaTeX, control-char, option prefix, and marking scheme checks
        for idx, q in enumerate(drill['questions'], 1):
            assert set(q.keys()) == {'tag', 'q', 'options', 'answer', 'explanation'}
            assert '[M1]' in q['explanation'] and '[A1]' in q['explanation'], f'{code} Q{idx}: missing [M1]/[A1]'
            for o in q['options']:
                assert not opt_prefix_re.match(o), f'{code} Q{idx}: option has A./B./C./D. prefix: {o}'
            all_text = drill['intro_html'] + q['tag'] + q['q'] + ' '.join(q['options']) + q['explanation']
            assert '$' not in all_text, f'{code} Q{idx}: raw $ detected'
            assert not ctrl_re.search(all_text), f'{code} Q{idx}: ASCII control char detected (escaped LaTeX?)'
            assert "\\'" not in all_text and '\\"' not in all_text, f'{code} Q{idx}: literal escaped quote in KaTeX'
            assert drill['intro_html'].count('\\(') == drill['intro_html'].count('\\)'), f'{code}: unbalanced intro \\( \\)'

        # Build StandardMCQTest JSON and validate with official pipeline validator
        cj = build_igcse_drill_json(
            title=drill['title'],
            course_id=COURSE_0606_ID,
            calculator_policy=drill['calculator_policy'],
            syllabus_code='0606',
            intro_html=drill['intro_html'],
            questions=drill['questions'],
            time_limit=drill['time_limit'],
        )
        errs = validate_igcse_drill(cj, title=code)
        assert not errs, f'validate_igcse_drill failed for {code}: {errs}'

    assert total_qs == 78, f'Expected 78 total questions, got {total_qs}'

    # -------------------------------------------------------------------------
    # 2. Independent Math Verification: DRILL_C13 (12 Qs)
    # -------------------------------------------------------------------------
    # Q1: |2(4,-5) - (3,2)| = |(5,-12)| = 13
    v1 = (2 * 4 - 3, 2 * (-5) - 2)
    assert v1 == (5, -12) and math.isqrt(v1[0] ** 2 + v1[1] ** 2) == 13 and '13' in _opt(DRILL_C13, 1)

    # Q2: unit vector of (8, -15) -> 1/17 (8i - 15j)
    mag2 = math.isqrt(8 ** 2 + (-15) ** 2)
    assert mag2 == 17 and r'\frac{1}{17}(8\mathbf{i} - 15\mathbf{j})' in _opt(DRILL_C13, 2)

    # Q3: magnitude 50 opposite to (7, -24)
    mag3 = math.isqrt(7 ** 2 + (-24) ** 2)
    w3 = (-50 * 7 // mag3, -50 * (-24) // mag3)
    assert mag3 == 25 and w3 == (-14, 48) and '-14' in _opt(DRILL_C13, 3) and '48' in _opt(DRILL_C13, 3)

    # Q4: (k+3, 6) parallel to (5, k-4), k > 0 -> k = 7
    sols4 = [k for k in range(-20, 20) if (k + 3) * (k - 4) == 30 and k > 0]
    assert sols4 == [7] and 'k = 7' in _opt(DRILL_C13, 4)

    # Q5: parallelogram ABCD -> OD = OA + OC - OB = (2+1-7, -5+9-3) = (-4, 1)
    od5 = (2 + 1 - 7, -5 + 9 - 3)
    assert od5 == (-4, 1) and '-4' in _opt(DRILL_C13, 5) and r'\\ 1' in _opt(DRILL_C13, 5)

    # Q6: AP:PB = 2:3 with A(2,11), B(17,-4) -> (3a + 2b)/5 = (8, 5)
    op6 = (Fraction(3 * 2 + 2 * 17, 5), Fraction(3 * 11 + 2 * (-4), 5))
    assert op6 == (8, 5) and '8' in _opt(DRILL_C13, 6) and '5' in _opt(DRILL_C13, 6)

    # Q7: OM = 1/2 a, ON = 3/4 a + 1/4 b -> MN = 1/4 a + 1/4 b
    mn7 = (Fraction(3, 4) - Fraction(1, 2), Fraction(1, 4))
    assert mn7 == (Fraction(1, 4), Fraction(1, 4)) and r'\frac{1}{4}\mathbf{a} + \frac{1}{4}\mathbf{b}' in _opt(DRILL_C13, 7)

    # Q8: OP = a+2b, OQ = 4a-b, OR = ka-7b collinear -> k = 10
    lam8 = Fraction(-7 - 2, -1 - 2)
    k8 = 1 + lam8 * (4 - 1)
    assert lam8 == 3 and k8 == 10 and 'k = 10' in _opt(DRILL_C13, 8)

    # Q9: OA = 2p+3q, OB = 5p+q, OC = 11p-3q -> AB = (3,-2), BC = (6,-4) = 2 AB -> AB:BC = 1:2
    ab9 = (5 - 2, 1 - 3)
    bc9 = (11 - 5, -3 - 1)
    assert bc9 == (2 * ab9[0], 2 * ab9[1]) and '1 : 2' in _opt(DRILL_C13, 9)

    # Q10: 2*lam + mu = 7, lam - 3*mu = -7 -> lam = 2, mu = 3
    lam10 = Fraction(7 * 3 + (-7), 2 * 3 + 1)
    mu10 = 7 - 2 * lam10
    assert (lam10, mu10) == (2, 3) and r'\lambda = 2,\ \mu = 3' in _opt(DRILL_C13, 10)

    # Q11: OX = (1-lam)a + (lam/2)b = (mu/3)a + (1-mu)b -> lam = 4/5, mu = 3/5
    lam11 = Fraction(4, 5)
    mu11 = Fraction(3, 5)
    assert 1 - lam11 == mu11 / 3 and lam11 / 2 == 1 - mu11
    assert r'\lambda = \frac{4}{5},\ \mu = \frac{3}{5}' in _opt(DRILL_C13, 11)

    # Q12: OT = (1-k)p + kq = (3/2)(1-mu)p + (2/3)mu q -> k = 2/5, mu = 3/5
    k12 = Fraction(2, 5)
    mu12 = Fraction(3, 5)
    assert 1 - k12 == Fraction(3, 2) * (1 - mu12) and k12 == Fraction(2, 3) * mu12
    assert r'k = \frac{2}{5}' in _opt(DRILL_C13, 12)

    # -------------------------------------------------------------------------
    # 3. Independent Math Verification: DRILL_C14 (12 Qs)
    # -------------------------------------------------------------------------
    # Q1: d/dx(4 sin 3x - 2 cos 5x) = 12 cos 3x + 10 sin 5x
    f14_1 = lambda x: 4 * math.sin(3 * x) - 2 * math.cos(5 * x)
    df14_1 = lambda x: 12 * math.cos(3 * x) + 10 * math.sin(5 * x)
    assert abs(_num_deriv(f14_1, 0.7) - df14_1(0.7)) < 1e-6 and '12\\cos(3x) + 10\\sin(5x)' in _opt(DRILL_C14, 1)

    # Q2: y = 3 tan(2x - pi/6) at x = pi/4 -> dy/dx = 24
    f14_2 = lambda x: 3 * math.tan(2 * x - math.pi / 6)
    assert abs(_num_deriv(f14_2, math.pi / 4) - 24.0) < 1e-5 and '24' in _opt(DRILL_C14, 2)

    # Q3: d/dx(e^(3x^2 - 5x)) = (6x - 5) e^(3x^2 - 5x)
    f14_3 = lambda x: math.exp(3 * x ** 2 - 5 * x)
    df14_3 = lambda x: (6 * x - 5) * math.exp(3 * x ** 2 - 5 * x)
    assert abs(_num_deriv(f14_3, 1.2) - df14_3(1.2)) < 1e-5 and '(6x - 5)e^{3x^2 - 5x}' in _opt(DRILL_C14, 3)

    # Q4: y = ln((2x+1)^3 / sqrt(4x-1)) at x = 1 -> 4/3
    f14_4 = lambda x: math.log(((2 * x + 1) ** 3) / math.sqrt(4 * x - 1))
    assert abs(_num_deriv(f14_4, 1.0) - float(Fraction(4, 3))) < 1e-6 and r'\frac{4}{3}' in _opt(DRILL_C14, 4)

    # Q5: stationary point of y = (2x - 3) e^(4x) -> x = 5/4
    f14_5 = lambda x: (2 * x - 3) * math.exp(4 * x)
    assert abs(_num_deriv(f14_5, 5 / 4)) < 1e-5 and r'x = \frac{5}{4}' in _opt(DRILL_C14, 5)

    # Q6: stationary point of y = ln(x)/x^2 -> (sqrt(e), 1/(2e))
    f14_6 = lambda x: math.log(x) / (x ** 2)
    x6 = math.sqrt(math.e)
    assert abs(_num_deriv(f14_6, x6)) < 1e-6 and abs(f14_6(x6) - 1 / (2 * math.e)) < 1e-12
    assert r'\sqrt{e}' in _opt(DRILL_C14, 6) and r'\frac{1}{2e}' in _opt(DRILL_C14, 6)

    # Q7: normal gradient of y = e^(2x) cos(x) at x = 0 -> -1/2
    f14_7 = lambda x: math.exp(2 * x) * math.cos(x)
    mt7 = _num_deriv(f14_7, 0.0)
    assert abs(-1.0 / mt7 - (-0.5)) < 1e-6 and r'-\frac{1}{2}' in _opt(DRILL_C14, 7)

    # Q8: sphere dV/dt = 40, r = 5 -> dr/dt = 40 / (100 pi) = 0.12732... -> 0.127
    drdt8 = 40.0 / (4.0 * math.pi * 25.0)
    assert f'{drdt8:.3g}' == '0.127' and '0.127' in _opt(DRILL_C14, 8)

    # Q9: y = sqrt(3x^2 + 4), dx/dt = 0.5 at x = 2 -> dy/dt = 0.75
    f14_9 = lambda x: math.sqrt(3 * x ** 2 + 4)
    dydt9 = _num_deriv(f14_9, 2.0) * 0.5
    assert abs(dydt9 - 0.75) < 1e-6 and '0.75' in _opt(DRILL_C14, 9)

    # Q10: y = 24/x^2 + 3x at x = 2 -> dy/dx = -3 -> delta y approx -3p
    f14_10 = lambda x: 24.0 / (x ** 2) + 3.0 * x
    assert abs(_num_deriv(f14_10, 2.0) - (-3.0)) < 1e-6 and '-3p' in _opt(DRILL_C14, 10)

    # Q11: y = 5 sin(2x) at x = pi/6, delta x = 0.02 -> delta y approx 0.1
    f14_11 = lambda x: 5.0 * math.sin(2.0 * x)
    assert abs(_num_deriv(f14_11, math.pi / 6) * 0.02 - 0.1) < 1e-6 and '0.1' in _opt(DRILL_C14, 11)

    # Q12: open-top square box SA = 192 -> V = 48x - x^3/4, max at x = 8 -> V_max = 256
    V12 = lambda x: 48 * x - 0.25 * (x ** 3)
    assert abs(_num_deriv(V12, 8.0)) < 1e-6 and V12(8.0) == 256.0 and V12(7.9) < 256.0 and V12(8.1) < 256.0
    assert '256' in _opt(DRILL_C14, 12)

    # -------------------------------------------------------------------------
    # 4. Independent Math Verification: DRILL_C15 (12 Qs)
    # -------------------------------------------------------------------------
    # Q1: int (3x-2)^5 dx = (1/18)(3x-2)^6 + c
    F15_1 = lambda x: ((3 * x - 2) ** 6) / 18.0
    assert abs(_num_deriv(F15_1, 1.5) - (3 * 1.5 - 2) ** 5) < 1e-5 and r'\frac{1}{18}(3x - 2)^6 + c' in _opt(DRILL_C15, 1)

    # Q2: int (6e^(2x-1) + 10/(5x+3)) dx = 3e^(2x-1) + 2 ln(5x+3) + c
    F15_2 = lambda x: 3 * math.exp(2 * x - 1) + 2 * math.log(5 * x + 3)
    assert abs(_num_deriv(F15_2, 1.1) - (6 * math.exp(2 * 1.1 - 1) + 10 / (5 * 1.1 + 3))) < 1e-5
    assert r'3e^{2x - 1} + 2\ln(5x + 3) + c' in _opt(DRILL_C15, 2)

    # Q3: int (4 sin 2x + 6 sec^2 3x) dx = -2 cos 2x + 2 tan 3x + c
    F15_3 = lambda x: -2 * math.cos(2 * x) + 2 * math.tan(3 * x)
    assert abs(_num_deriv(F15_3, 0.3) - (4 * math.sin(0.6) + 6 / (math.cos(0.9) ** 2))) < 1e-5
    assert r'-2\cos(2x) + 2\tan(3x) + c' in _opt(DRILL_C15, 3)

    # Q4: dy/dx = 12/sqrt(4x+1), (2, 15) -> y = 6 sqrt(4x+1) - 3
    F15_4 = lambda x: 6 * math.sqrt(4 * x + 1) - 3
    assert abs(F15_4(2.0) - 15.0) < 1e-12 and abs(_num_deriv(F15_4, 2.0) - 12.0 / 3.0) < 1e-6
    assert r'y = 6\sqrt{4x + 1} - 3' in _opt(DRILL_C15, 4)

    # Q5: int 6x e^(3x) dx = 2x e^(3x) - (2/3) e^(3x) + c
    F15_5 = lambda x: 2 * x * math.exp(3 * x) - (2.0 / 3.0) * math.exp(3 * x)
    assert abs(_num_deriv(F15_5, 0.8) - 6 * 0.8 * math.exp(2.4)) < 1e-5
    assert r'2x e^{3x} - \frac{2}{3}e^{3x} + c' in _opt(DRILL_C15, 5)

    # Q6: int_1^e 4x ln x dx = e^2 + 1
    num15_6 = _simpson(lambda x: 4 * x * math.log(x), 1.0, math.e)
    assert abs(num15_6 - (math.e ** 2 + 1.0)) < 1e-8 and 'e^2 + 1' in _opt(DRILL_C15, 6)

    # Q7: int_1^4 6/(2x+1) dx = 3 ln 3
    num15_7 = _simpson(lambda x: 6.0 / (2 * x + 1), 1.0, 4.0)
    assert abs(num15_7 - 3 * math.log(3)) < 1e-8 and r'3\ln 3' in _opt(DRILL_C15, 7)

    # Q8: int_0^(pi/6) (4 cos 2x + 3 sin 3x) dx = sqrt(3) + 1
    num15_8 = _simpson(lambda x: 4 * math.cos(2 * x) + 3 * math.sin(3 * x), 0.0, math.pi / 6)
    assert abs(num15_8 - (math.sqrt(3) + 1.0)) < 1e-8 and r'\sqrt{3} + 1' in _opt(DRILL_C15, 8)

    # Q9: int_0^k e^(2x) dx = 12 -> k = ln 5
    k15_9 = math.log(5)
    assert abs(_simpson(lambda x: math.exp(2 * x), 0.0, k15_9) - 12.0) < 1e-8 and r'\ln 5' in _opt(DRILL_C15, 9)

    # Q10: total area between y = x^2 - 4 and x-axis on [0, 3] = 16/3 + 7/3 = 23/3
    a15_10 = abs(Fraction(8, 3) - 8) + abs((9 - 12) - (Fraction(8, 3) - 8))
    assert a15_10 == Fraction(23, 3) and r'\frac{23}{3}' in _opt(DRILL_C15, 10)

    # Q11: area between y = 6x - x^2 and y = 2x -> 32/3
    a15_11 = Fraction(2 * 16) - Fraction(64, 3)
    assert a15_11 == Fraction(32, 3) and abs(_simpson(lambda x: (6 * x - x ** 2) - 2 * x, 0.0, 4.0) - float(a15_11)) < 1e-8
    assert r'\frac{32}{3}' in _opt(DRILL_C15, 11)

    # Q12: area between y = 8 - x^2 and y = x^2 -> 64/3
    a15_12 = 2 * (16 - Fraction(16, 3))
    assert a15_12 == Fraction(64, 3) and abs(_simpson(lambda x: 8 - 2 * x ** 2, -2.0, 2.0) - float(a15_12)) < 1e-8
    assert r'\frac{64}{3}' in _opt(DRILL_C15, 12)

    # -------------------------------------------------------------------------
    # 5. Independent Math Verification: DRILL_C16 (12 Qs)
    # -------------------------------------------------------------------------
    # Q1: s = t^3 - 6t^2 + 9t + 4 -> a(3) = 6
    a16_1 = 6 * 3 - 12
    assert a16_1 == 6 and r'6\text{ m/s}^2' in _opt(DRILL_C16, 1)

    # Q2: s = 2t^3 - 15t^2 + 36t -> v = 6(t-2)(t-3) -> |s(3) - s(2)| = |27 - 28| = 1
    s16_2 = lambda t: 2 * t ** 3 - 15 * t ** 2 + 36 * t
    assert abs(s16_2(3) - s16_2(2)) == 1 and r'1\text{ m}' in _opt(DRILL_C16, 2)

    # Q3: v = 12t - 3t^2 -> max at t = 2 -> v_max = 12
    v16_3 = lambda t: 12 * t - 3 * t ** 2
    assert v16_3(2) == 12 and v16_3(1.9) < 12 and v16_3(2.1) < 12 and r'12\text{ m/s}' in _opt(DRILL_C16, 3)

    # Q4: a = 6t - 8, v(0) = 0 -> v = 3t^2 - 8t = 0 -> t = 8/3
    t16_4 = Fraction(8, 3)
    assert 3 * t16_4 ** 2 - 8 * t16_4 == 0 and r'\frac{8}{3}' in _opt(DRILL_C16, 4)

    # Q5: a = 12t - 4, v(1) = 5, s(1) = 3 -> v = 6t^2 - 4t + 3, s = 2t^3 - 2t^2 + 3t -> s(2) = 14
    v16_5 = lambda t: 6 * t ** 2 - 4 * t + 3
    s16_5 = lambda t: 2 * t ** 3 - 2 * t ** 2 + 3 * t
    assert v16_5(1) == 5 and s16_5(1) == 3 and s16_5(2) == 14 and r'14\text{ m}' in _opt(DRILL_C16, 5)

    # Q6: v = 3t^2 - 12 on [0, 3], turns at t = 2 -> total dist = 16 + 7 = 23
    s16_6 = lambda t: t ** 3 - 12 * t
    d16_6 = abs(s16_6(2) - s16_6(0)) + abs(s16_6(3) - s16_6(2))
    assert d16_6 == 23 and r'23\text{ m}' in _opt(DRILL_C16, 6)

    # Q7: v = t^2 - 5t + 4 on [0, 4], turns at t = 1 -> total dist = 11/6 + 27/6 = 19/3
    s16_7 = lambda t: Fraction(1, 3) * t ** 3 - Fraction(5, 2) * t ** 2 + 4 * t
    d16_7 = abs(s16_7(1) - s16_7(0)) + abs(s16_7(4) - s16_7(1))
    assert d16_7 == Fraction(19, 3) and r'\frac{19}{3}' in _opt(DRILL_C16, 7)

    # Q8: s = 4 e^(0.5t) - 6t - 4 -> v = 2 e^(0.5t) - 6 = 0 -> t = 2 ln 3 = 2.1972 -> 2.20
    t16_8 = 2 * math.log(3)
    assert f'{t16_8:.2f}' == '2.20' and '2.20' in _opt(DRILL_C16, 8)

    # Q9: v = 12 - 12 e^(-0.5t), s(0) = 0 -> s(4) = 24 + 24 e^(-2) = 27.248 -> 27.2
    s16_9 = _simpson(lambda t: 12.0 - 12.0 * math.exp(-0.5 * t), 0.0, 4.0)
    assert abs(s16_9 - (24.0 + 24.0 * math.exp(-2.0))) < 1e-8 and f'{s16_9:.3g}' == '27.2'
    assert '27.2' in _opt(DRILL_C16, 9)

    # Q10: s = 5 sin(2t) -> a = -20 sin(2t) at t = pi/12 -> -10
    a16_10 = -20.0 * math.sin(2.0 * (math.pi / 12.0))
    assert abs(a16_10 - (-10.0)) < 1e-12 and '-10' in _opt(DRILL_C16, 10)

    # Q11: v = 8 cos(2t) on [0, pi/2], turns at t = pi/4 -> total dist = 4 + 4 = 8
    d16_11 = abs(_simpson(lambda t: 8 * math.cos(2 * t), 0.0, math.pi / 4)) + abs(
        _simpson(lambda t: 8 * math.cos(2 * t), math.pi / 4, math.pi / 2)
    )
    assert abs(d16_11 - 8.0) < 1e-8 and r'8\text{ m}' in _opt(DRILL_C16, 11)

    # Q12: v = 12/(2t+1) - 3 = 0 -> t = 3/2, s(3/2) = 12 ln 2 - 9/2
    s16_12 = _simpson(lambda t: 12.0 / (2 * t + 1) - 3.0, 0.0, 1.5)
    assert abs(s16_12 - (12.0 * math.log(2) - 4.5)) < 1e-8 and r'12\ln 2 - \frac{9}{2}' in _opt(DRILL_C16, 12)

    # -------------------------------------------------------------------------
    # 6. Independent Math Verification: DRILL_NC1 (15 Qs)
    # -------------------------------------------------------------------------
    # Q1: (11 + 3 sqrt(5)) / (3 - sqrt(5)) = 12 + 5 sqrt(5)
    assert abs((11 + 3 * math.sqrt(5)) / (3 - math.sqrt(5)) - (12 + 5 * math.sqrt(5))) < 1e-12
    assert r'12 + 5\sqrt{5}' in _opt(DRILL_NC1, 1)

    # Q2: 0.5 * (4 + sqrt(3)) * (6 + 2 sqrt(3)) = 15 + 7 sqrt(3)
    assert abs(0.5 * (4 + math.sqrt(3)) * (6 + 2 * math.sqrt(3)) - (15 + 7 * math.sqrt(3))) < 1e-12
    assert r'6 + 2\sqrt{3}' in _opt(DRILL_NC1, 2)

    # Q3: 2^(2x+1) - 9(2^x) + 4 = 0 -> x = -1, 2
    for x in (-1, 2):
        assert abs(2 ** (2 * x + 1) - 9 * (2 ** x) + 4) < 1e-12
    assert 'x = -1' in _opt(DRILL_NC1, 3) and 'x = 2' in _opt(DRILL_NC1, 3)

    # Q4: log_2(x) + log_2(x-2) = 3 -> x = 4 only
    assert math.log2(4) + math.log2(4 - 2) == 3.0 and 'x = 4' in _opt(DRILL_NC1, 4) and 'only' in _opt(DRILL_NC1, 4)

    # Q5: log_9(x) + log_3(x) = 6 -> x = 81
    assert abs(math.log(81, 9) + math.log(81, 3) - 6.0) < 1e-12 and 'x = 81' in _opt(DRILL_NC1, 5)

    # Q6: x^2 + y^2 - 8x + 6y - 11 = 0 -> (x-4)^2 + (y+3)^2 = 36 -> centre (4, -3), r = 6
    assert 4 ** 2 + (-3) ** 2 + 11 == 36 and '(4, -3)' in _opt(DRILL_NC1, 6) and r'radius \(6\)' in _opt(DRILL_NC1, 6)

    # Q7: centre C(2,-1), P(5,3) -> m_CP = 4/3 -> m_t = -3/4 -> 3x + 4y = 27
    m_cp7 = Fraction(3 - (-1), 5 - 2)
    m_t7 = -1 / m_cp7
    assert m_t7 == Fraction(-3, 4) and 3 * 5 + 4 * 3 == 27 and '3x + 4y = 27' in _opt(DRILL_NC1, 7)

    # Q8: y = 2x + k tangent to (x-1)^2 + (y+2)^2 = 20 -> |2(1) - (-2) + k| / sqrt(5) = sqrt(20) -> |k+4| = 10 -> k = 6, -14
    for k in (6, -14):
        assert abs(2 * 1 - (-2) + k) == 10
    assert 'k = 6' in _opt(DRILL_NC1, 8) and 'k = -14' in _opt(DRILL_NC1, 8)

    # Q9: p(x) = 2x^3 + ax^2 + bx - 6, p(2)=0, p(-1)=-12 -> a = -3, b = 1
    p9 = lambda x: 2 * x ** 3 - 3 * x ** 2 + 1 * x - 6
    assert p9(2) == 0 and p9(-1) == -12 and 'a = -3' in _opt(DRILL_NC1, 9) and 'b = 1' in _opt(DRILL_NC1, 9)

    # Q10: f(x) = 2x^3 - 3x^2 - 11x + 6 -> roots -2, 1/2, 3
    f10 = lambda x: 2 * x ** 3 - 3 * x ** 2 - 11 * x + 6
    for r in (Fraction(-2), Fraction(1, 2), Fraction(3)):
        assert f10(r) == 0
    assert r'-2,\ \frac{1}{2},\ 3' in _opt(DRILL_NC1, 10)

    # Q11: |2x - 5| = |x + 4| -> x = 1/3, 9
    for r in (Fraction(1, 3), Fraction(9)):
        assert abs(2 * r - 5) == abs(r + 4)
    assert r'\frac{1}{3}' in _opt(DRILL_NC1, 11) and 'x = 9' in _opt(DRILL_NC1, 11)

    # Q12: |3x - 2| < x + 4 -> -1/2 < x < 3
    assert abs(3 * Fraction(-1, 2) - 2) == Fraction(-1, 2) + 4
    assert abs(3 * 3 - 2) == 3 + 4
    assert abs(3 * 0 - 2) < 0 + 4 and not (abs(3 * (-1) - 2) < -1 + 4) and not (abs(3 * 4 - 2) < 4 + 4)
    assert r'-\frac{1}{2} < x < 3' in _opt(DRILL_NC1, 12)

    # Q13: y = mx - 4 does not intersect y = x^2 + 2x + 5 -> (2-m)^2 - 36 < 0 -> -4 < m < 8
    assert (2 - (-4)) ** 2 - 36 == 0 and (2 - 8) ** 2 - 36 == 0 and (2 - 0) ** 2 - 36 < 0
    assert '-4 < m < 8' in _opt(DRILL_NC1, 13)

    # Q14: f(x) = x^2 - 6x + 11 (x >= 3) -> f^(-1)(x) = 3 + sqrt(x - 2), x >= 2
    f14 = lambda x: x ** 2 - 6 * x + 11
    finv14 = lambda x: 3 + math.sqrt(x - 2)
    assert f14(3) == 2 and abs(finv14(f14(5.5)) - 5.5) < 1e-12
    assert r'3 + \sqrt{x - 2},\ x \ge 2' in _opt(DRILL_NC1, 14)

    # Q15: f(x) = e^(2x) + 3, g(x) = 0.5 ln(x - 1) -> fg(5) = 7, range f(x) > 3
    fg5 = math.exp(2 * 0.5 * math.log(5 - 1)) + 3
    assert abs(fg5 - 7.0) < 1e-12 and 'fg(5) = 7' in _opt(DRILL_NC1, 15) and 'f(x) > 3' in _opt(DRILL_NC1, 15)

    # -------------------------------------------------------------------------
    # 7. Independent Math Verification: DRILL_NC2 (15 Qs)
    # -------------------------------------------------------------------------
    # Q1: 2 sin^2 x - sin x - 1 = 0 on [0, 2pi] -> pi/2, 7pi/6, 11pi/6
    for ang in (math.pi / 2, 7 * math.pi / 6, 11 * math.pi / 6):
        assert abs(2 * math.sin(ang) ** 2 - math.sin(ang) - 1) < 1e-12
    assert r'\frac{\pi}{2},\ \frac{7\pi}{6},\ \frac{11\pi}{6}' in _opt(DRILL_NC2, 1)

    # Q2: sqrt(3) tan(2x - pi/3) = 1 on [0, pi] -> pi/4, 3pi/4
    for ang in (math.pi / 4, 3 * math.pi / 4):
        assert abs(math.sqrt(3) * math.tan(2 * ang - math.pi / 3) - 1.0) < 1e-12
    assert r'\frac{\pi}{4},\ \frac{3\pi}{4}' in _opt(DRILL_NC2, 2)

    # Q3: segment area r=6, theta=pi/3 -> 6pi - 9 sqrt(3)
    seg3 = 0.5 * 36 * (math.pi / 3 - math.sin(math.pi / 3))
    assert abs(seg3 - (6 * math.pi - 9 * math.sqrt(3))) < 1e-12 and r'6\pi - 9\sqrt{3}' in _opt(DRILL_NC2, 3)

    # Q4: segment perimeter r=8, theta=2pi/3 -> 16pi/3 + 8 sqrt(3)
    per4 = 8 * (2 * math.pi / 3) + 2 * 8 * math.sin(math.pi / 3)
    assert abs(per4 - (16 * math.pi / 3 + 8 * math.sqrt(3))) < 1e-12 and r'\frac{16\pi}{3} + 8\sqrt{3}' in _opt(DRILL_NC2, 4)

    # Q5: term independent of x in (2x - 1/x^2)^6 -> C(6,2) * 2^4 * (-1)^2 = 240
    t5 = math.comb(6, 2) * (2 ** 4) * ((-1) ** 2)
    assert t5 == 240 and '240' in _opt(DRILL_NC2, 5) and '-' not in _opt(DRILL_NC2, 5)

    # Q6: coeff of x^2 in (1 - 3x)(2 + x)^5 -> 1*C(5,2)*2^3 - 3*C(5,1)*2^4 = 80 - 240 = -160
    c6 = 1 * math.comb(5, 2) * (2 ** 3) - 3 * math.comb(5, 1) * (2 ** 4)
    assert c6 == -160 and '-160' in _opt(DRILL_NC2, 6)

    # Q7: AP u_4 = 17, u_10 = 41 -> d = 4, a = 5 -> S_20 = 860
    d7 = Fraction(41 - 17, 10 - 4)
    a7 = 17 - 3 * d7
    s20_7 = 10 * (2 * a7 + 19 * d7)
    assert s20_7 == 860 and '860' in _opt(DRILL_NC2, 7)

    # Q8: GP a = 18, u_2 = -12 -> r = -2/3 -> S_inf = 18 / (5/3) = 54/5
    r8 = Fraction(-12, 18)
    sinf8 = Fraction(18) / (1 - r8)
    assert sinf8 == Fraction(54, 5) and r'\frac{54}{5}' in _opt(DRILL_NC2, 8)

    # Q9: committee of 4 from 5 boys, 4 girls with >= 3 girls -> C(4,3)*C(5,1) + C(4,4)*C(5,0) = 21
    ways9 = math.comb(4, 3) * math.comb(5, 1) + math.comb(4, 4) * math.comb(5, 0)
    assert ways9 == 21 and '21' in _opt(DRILL_NC2, 9)

    # Q10: normal to y = 2e^(3x) - 4x at x = 0 -> y = -(1/2)x + 2
    f2_10 = lambda x: 2 * math.exp(3 * x) - 4 * x
    assert abs(f2_10(0.0) - 2.0) < 1e-12 and abs(-1.0 / _num_deriv(f2_10, 0.0) - (-0.5)) < 1e-6
    assert r'y = -\frac{1}{2}x + 2' in _opt(DRILL_NC2, 10)

    # Q11: stationary point of y = 2x - 6 ln x -> x = 3, y = 6 - 6 ln 3, minimum
    f2_11 = lambda x: 2 * x - 6 * math.log(x)
    assert abs(_num_deriv(f2_11, 3.0)) < 1e-6 and f2_11(2.9) > f2_11(3.0) and f2_11(3.1) > f2_11(3.0)
    assert r'(3,\ 6 - 6\ln 3)' in _opt(DRILL_NC2, 11) and 'minimum' in _opt(DRILL_NC2, 11)

    # Q12: int_0^(ln 2) (4e^(2x) - 3e^x) dx = 3
    num2_12 = _simpson(lambda x: 4 * math.exp(2 * x) - 3 * math.exp(x), 0.0, math.log(2))
    assert abs(num2_12 - 3.0) < 1e-8 and r'\(3\)' == _opt(DRILL_NC2, 12)

    # Q13: int_0^(pi/4) (sec^2 x + 2 sin x) dx = 3 - sqrt(2)
    num2_13 = _simpson(lambda x: 1.0 / (math.cos(x) ** 2) + 2 * math.sin(x), 0.0, math.pi / 4)
    assert abs(num2_13 - (3.0 - math.sqrt(2))) < 1e-8 and r'3 - \sqrt{2}' in _opt(DRILL_NC2, 13)

    # Q14: v = 6 sin(3t), first rest t = pi/3 -> s = int_0^(pi/3) 6 sin(3t) dt = 4
    num2_14 = _simpson(lambda t: 6 * math.sin(3 * t), 0.0, math.pi / 3)
    assert abs(num2_14 - 4.0) < 1e-8 and r'4\text{ m}' in _opt(DRILL_NC2, 14)

    # Q15: OA = (3,-5), OB = (11,1) -> AB = (8,6), |AB| = 10 -> unit = (4/5)i + (3/5)j
    ab15 = (11 - 3, 1 - (-5))
    mag15 = math.isqrt(ab15[0] ** 2 + ab15[1] ** 2)
    unit15 = (Fraction(ab15[0], mag15), Fraction(ab15[1], mag15))
    assert unit15 == (Fraction(4, 5), Fraction(3, 5))
    assert r'\frac{4}{5}\mathbf{i} + \frac{3}{5}\mathbf{j}' in _opt(DRILL_NC2, 15)

    return True


if __name__ == '__main__':
    verify_all_math()
    print('=== IGCSE 0606 DRILLS P2B SELF-TEST PASSED ===')
    for d in DRILLS_0606_P2B:
        cnt = dict(sorted(Counter(q['answer'] for q in d['questions']).items()))
        print(
            f"  [OK] {d['code']:10s} | folder={d['folder_key']:9s} | order={d['order_index']} "
            f"| {d['calculator_policy']:14s} | {len(d['questions']):2d} Qs | ans={cnt}"
        )
    print(f'Total: {len(DRILLS_0606_P2B)} drills, {sum(len(d["questions"]) for d in DRILLS_0606_P2B)} questions — ALL VERIFIED!')
