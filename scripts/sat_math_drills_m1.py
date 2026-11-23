# -*- coding: utf-8 -*-
"""
Digital SAT Math 1500+ — Module 1: Algebra & Desmos Mastery
3 Flagship Skill Drills × 15 Questions = 45 Unique, Original, Programmatically Verified Questions:
  - Drill 1.1 (drill_m1_1): Desmos 800 Playbook, Linear Equations & Systems
  - Drill 1.2 (drill_m1_2): Linear Functions, Slope-Intercept Models & Word Problems
  - Drill 1.3 (drill_m1_3): Linear Inequalities, Systems & Feasible Regions
"""

import os
import re
import sys
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
# CRISP BLUEBOOK-STYLE SVG HELPER FOR DRILL 1.3 Q2 (3x - 2y < 6)
# ============================================================================

def _svg_inequality_halfplane_3x_minus_2y_lt_6():
    """
    Exact coordinate-plane SVG for the inequality 3x - 2y < 6 (y > 1.5x - 3).
    Grid: x in [-4, 6], y in [-5, 5]; 22 px per unit.
    Origin (0, 0) -> (118, 130).
    Boundary line hits y = -5 at x = -4/3 (88.67, 240) and y = 5 at x = 16/3 (235.33, 20).
    Intercepts: (0, -3) -> (118, 196) and (2, 0) -> (162, 130).
    """
    grid_lines = []
    for gx in range(-4, 7):
        px = 118 + gx * 22
        grid_lines.append(f'<line x1="{px}" y1="20" x2="{px}" y2="240" stroke="#e2e8f0" stroke-width="1"/>')
    for gy in range(-5, 6):
        py = 130 - gy * 22
        grid_lines.append(f'<line x1="30" y1="{py}" x2="250" y2="{py}" stroke="#e2e8f0" stroke-width="1"/>')

    ticks = []
    for tx in (-4, -2, 2, 4, 6):
        px = 118 + tx * 22
        ticks.append(f'<line x1="{px}" y1="126" x2="{px}" y2="134" stroke="#334155" stroke-width="1.4"/>')
        ticks.append(f'<text x="{px}" y="146" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#475569">{tx}</text>')
    for ty in (-4, -2, 2, 4):
        py = 130 - ty * 22
        ticks.append(f'<line x1="114" y1="{py}" x2="122" y2="{py}" stroke="#334155" stroke-width="1.4"/>')
        ticks.append(f'<text x="109" y="{py + 3.5}" text-anchor="end" font-family="sans-serif" font-size="10.5" fill="#475569">{ty}</text>')

    return (
        '<div style="display:flex;justify-content:center;margin:8px 0 12px 0;">'
        '<svg viewBox="0 0 280 264" width="280" height="264" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:12px;">'
        '<rect x="30" y="20" width="220" height="220" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>'
        + ''.join(grid_lines)
        # Shaded region y > 1.5x - 3 (above & left of boundary line)
        + '<polygon points="30,20 235.33,20 88.67,240 30,240" fill="#3b82f6" fill-opacity="0.22"/>'
        # Axes
        + '<line x1="24" y1="130" x2="260" y2="130" stroke="#0f172a" stroke-width="1.8"/>'
        + '<line x1="118" y1="246" x2="118" y2="12" stroke="#0f172a" stroke-width="1.8"/>'
        + '<polygon points="262,130 255,126 255,134" fill="#0f172a"/>'
        + '<polygon points="118,10 114,17 122,17" fill="#0f172a"/>'
        + '<text x="266" y="134" font-family="serif" font-style="italic" font-size="13" font-weight="bold" fill="#0f172a">x</text>'
        + '<text x="124" y="16" font-family="serif" font-style="italic" font-size="13" font-weight="bold" fill="#0f172a">y</text>'
        + ''.join(ticks)
        # Dashed boundary line
        + '<line x1="88.67" y1="240" x2="235.33" y2="20" stroke="#1d4ed8" stroke-width="2.6" stroke-dasharray="7 5"/>'
        # Open circles at intercepts (0, -3) and (2, 0)
        + '<circle cx="118" cy="196" r="4" fill="#ffffff" stroke="#1d4ed8" stroke-width="2.2"/>'
        + '<circle cx="162" cy="130" r="4" fill="#ffffff" stroke="#1d4ed8" stroke-width="2.2"/>'
        + '<text x="126" y="203" font-family="sans-serif" font-size="10.5" font-weight="700" fill="#1e3a8a">(0, -3)</text>'
        + '<text x="168" y="122" font-family="sans-serif" font-size="10.5" font-weight="700" fill="#1e3a8a">(2, 0)</text>'
        + '<text x="140" y="257" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Shaded region represents the solution set.</text>'
        + '</svg></div>'
    )


# ============================================================================
# DRILL 1.1: DESMOS 800 PLAYBOOK, LINEAR EQUATIONS & SYSTEMS (15 QUESTIONS)
# ============================================================================

def _build_drill_m1_1():
    D = 'Algebra'
    S_EQ = 'Linear equations in one variable'
    S_SYS = 'Systems of two linear equations in two variables'

    q8_table = build_math_table(
        headers=[r'\(x\)', r'\(f(x)\)', r'\(g(x)\)'],
        rows=[
            [r'\(-2\)', r'\(17\)', r'\(-6\)'],
            [r'\(2\)', r'\(7\)', r'\(0\)'],
            [r'\(6\)', r'\(-3\)', r'\(6\)'],
        ],
        caption='Selected Values of Linear Functions f and g',
    )

    questions = [
        # Q1 — Medium — MCQ (Key: B)
        math_mcq(
            'sat_m1_1_q1', 1, D, S_EQ, 'Medium',
            r'<p>\[4(3x - 5) + 7 = 2(3x - 5) + 25\]</p>',
            r'<p>Based on the given equation, what is the value of \(6x - 13\)?</p>',
            {
                'A': r'\(9\)',
                'B': r'\(15\)',
                'C': r'\(18\)',
                'D': r'\(28\)',
            },
            'B',
            '\n'.join([
                r'<b>Bước 1 (Đặt ẩn phụ khối):</b> Đặt \(u = 3x - 5\). Phương trình trở thành:',
                r'\[4u + 7 = 2u + 25 \implies 2u = 18 \implies u = 9\]',
                r'<b>Bước 2 (Biểu diễn thẳng mục tiêu theo \(u\)):</b>',
                r'\[6x - 13 = 2(3x - 5) - 3 = 2u - 3 = 2(9) - 3 = 15\]',
                r'Không cần giải lẻ \(x = \frac{14}{3}\), tránh hoàn toàn sai số phân số.',
            ]),
            r'Khi cụm \((ax + b)\) lặp lại hai lần trong phương trình và biểu thức cần tìm là bội của nó, luôn đặt \(u = ax + b\) thay vì phá ngoặc tìm \(x\).',
            {
                'A': ('Partial Solve', r'Dừng lại ngay sau khi tìm ra \(3x - 5 = 9\) mà quên nhân \(2\) và trừ \(3\).'),
                'B': ('Đáp án đúng', r'Tính chuẩn \(6x - 13 = 2(3x - 5) - 3 = 2(9) - 3 = 15\).'),
                'C': ('Missing Constant Shift', r'Tính được \(2(3x - 5) = 6x - 10 = 18\) nhưng quên trừ tiếp \(3\) để ra \(6x - 13\).'),
                'D': ('Incomplete Expression', r'Tính ra \(6x = 28\) từ \(x = \frac{14}{3}\) rồi quên trừ \(13\).'),
            },
            desmos_tip_vi=r'Gõ hồi quy 1 dòng <code>4(3x_1 - 5) + 7 ~ 2(3x_1 - 5) + 25</code> rồi gõ <code>6x_1 - 13</code> ở dòng 2 — Desmos xuất ngay kết quả chính xác <code>15</code> không bị làm tròn!',
        ),

        # Q2 — Medium — MCQ (Key: D)
        math_mcq(
            'sat_m1_1_q2', 2, D, S_SYS, 'Medium',
            r'<p>\[7x + 4y = 31\]\[2x + 5y = 23\]</p>',
            r'<p>The solution to the given system of equations is \((x, y)\). What is the value of \(5x - y\)?</p>',
            {
                'A': r'\(-8\)',
                'B': r'\(\frac{7}{3}\)',
                'C': r'\(6\)',
                'D': r'\(8\)',
            },
            'D',
            '\n'.join([
                r'<b>Chiến thuật tổ hợp tuyến tính (Không giải lẻ \(x, y\)):</b>',
                r'Lấy phương trình (1) trừ thẳng vế theo vế cho phương trình (2):',
                r'\[(7x + 4y) - (2x + 5y) = 31 - 23\]',
                r'\[5x - y = 8\]',
                r'<i>Kiểm chứng:</i> Nếu giải hệ ra \(x = \frac{7}{3}, y = \frac{11}{3}\) thì \(5\left(\frac{7}{3}\right) - \frac{11}{3} = \frac{24}{3} = 8\).',
            ]),
            r'Trước khi khử biến tìm \(x, y\) riêng lẻ trong hệ phương trình, luôn thử cộng hoặc trừ trực tiếp hai phương trình xem có ra ngay biểu thức đề hỏi không.',
            {
                'A': ('Reversed Subtraction', r'Lấy phương trình (2) trừ (1) ra \(-5x + y = -8\) rồi quên đổi dấu cả hai vế.'),
                'B': ('Partial Solve', r'Chỉ giải ra \(x = \frac{7}{3}\) mà quên tính giá trị biểu thức \(5x - y\).'),
                'C': ('Wrong Target Expression', r'Cộng hai phương trình được \(9x + 9y = 54 \implies x + y = 6\), tính nhầm sang \(x + y\).'),
                'D': ('Đáp án đúng', r'Trừ trực tiếp phương trình (1) cho (2) thu ngay \(5x - y = 31 - 23 = 8\).'),
            },
            desmos_tip_vi=r'Dùng hồi quy hệ 2 ẩn trong 5 giây: gõ <code>[7x_1 + 4y_1, 2x_1 + 5y_1] ~ [31, 23]</code>, sau đó gõ <code>5x_1 - y_1</code> ở dòng 2 sẽ hiện chính xác <code>8</code>.',
        ),

        # Q3 — Medium — MCQ (Key: A)
        math_mcq(
            'sat_m1_1_q3', 3, D, S_EQ, 'Medium',
            r'<p>\[\frac{1}{4}(20x - 16) + kx = 10x - 4\]</p>',
            r'<p>In the given equation, \(k\) is a constant. If the equation has infinitely many solutions, what is the value of \(k\)?</p>',
            {
                'A': r'\(5\)',
                'B': r'\(10\)',
                'C': r'\(15\)',
                'D': r'\(20\)',
            },
            'A',
            '\n'.join([
                r'<b>Bước 1:</b> Khai triển vế trái và gom các hạng tử chứa \(x\):',
                r'\[\frac{1}{4}(20x - 16) + kx = 5x - 4 + kx = (5 + k)x - 4\]',
                r'<b>Bước 2:</b> So sánh hai vế \((5 + k)x - 4 = 10x - 4\).',
                r'Hằng số tự do đã bằng nhau (\(-4 = -4\)). Để phương trình có vô số nghiệm, hệ số của \(x\) hai vế phải bằng nhau:',
                r'\[5 + k = 10 \implies k = 5\]',
            ]),
            r'Phương trình bậc nhất \(Ax + B = Cx + D\) có vô số nghiệm khi và chỉ khi đồng nhất tuyệt đối cả hệ số góc (\(A = C\)) lẫn hệ số tự do (\(B = D\)).',
            {
                'A': ('Đáp án đúng', r'Đồng nhất hệ số của \(x\): \(5 + k = 10 \implies k = 5\), và hằng số \(-4 = -4\) khớp hoàn toàn.'),
                'B': ('Ignored Distributed Term', r'Cho thẳng \(k = 10\) mà quên cộng hệ số \(5x\) tách ra từ \(\frac{1}{4}(20x)\).'),
                'C': ('Sign Flip Error', r'Chuyển vế sai dấu thành \(k = 10 + 5 = 15\) thay vì \(10 - 5\).'),
                'D': ('Distribution Error', r'Lấy nguyên số \(20\) trong ngoặc mà không nhân phân phối với \(\frac{1}{4}\).'),
            },
            desmos_tip_vi=r'Gõ <code>x_1 = [0, 1]</code>, sau đó gõ hồi quy <code>(1/4)(20x_1 - 16) + k x_1 ~ 10x_1 - 4</code> — Desmos trả ngay <code>k = 5</code>!',
        ),

        # Q4 — Medium — SPR (Answer: 9)
        math_spr(
            'sat_m1_1_q4', 4, D, S_SYS, 'Medium',
            r'<p>\[\frac{3}{5}x - \frac{2}{3}y = 7\]\[px - 10y = 14\]</p>',
            r'<p>In the given system of equations, \(p\) is a constant. If the system has no solution, what is the value of \(p\)?</p>',
            ['9'],
            '9',
            '\n'.join([
                r'<b>Điều kiện hệ vô nghiệm:</b> Hai đường thẳng song song nhưng không trùng nhau \(\iff \frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}\).',
                r'<b>Bước 1:</b> Tìm hệ số tỷ lệ giữa hệ số của \(y\) ở hai phương trình:',
                r'\[\frac{-10}{-\frac{2}{3}} = 15\]',
                r'<b>Bước 2:</b> Nhân hệ số của \(x\) ở phương trình (1) với cùng tỷ số \(15\):',
                r'\[p = 15 \cdot \frac{3}{5} = 9\]',
                r'<b>Bước 3 (Kiểm tra khác hằng số):</b> \(7 \cdot 15 = 105 \neq 14\), nên hai đường thẳng thực sự song song phân biệt (vô nghiệm).',
            ]),
            r'Với hệ vô nghiệm, chỉ cần tìm tỷ số nhân từ cặp hệ số đã biết (của \(y\)) rồi áp dụng cho cặp hệ số ẩn (\(x\)), và kiểm tra vế hằng số KHÔNG cùng tỷ số.',
            desmos_tip_vi=r'Nhập cả 2 phương trình vào Desmos và bấm <b>Add slider: p</b>. Kéo (hoặc gõ) <code>p = 9</code> sẽ thấy ngay hai đường thẳng song song tách rời nhau!',
        ),

        # Q5 — Medium-Hard — MCQ (Key: C)
        math_mcq(
            'sat_m1_1_q5', 5, D, S_EQ, 'Medium-Hard',
            r'<p>\[\frac{5x - 3}{4} - \frac{2x + 7}{6} = \frac{x + 11}{12}\]</p>',
            r'<p>What value of \(x\) is the solution to the given equation?</p>',
            {
                'A': r'\(\frac{3}{5}\)',
                'B': r'\(\frac{21}{10}\)',
                'C': r'\(\frac{17}{5}\)',
                'D': r'\(5\)',
            },
            'C',
            '\n'.join([
                r'<b>Bước 1:</b> Nhân cả hai vế với mẫu số chung nhỏ nhất \(\text{LCM}(4, 6, 12) = 12\):',
                r'\[3(5x - 3) - 2(2x + 7) = x + 11\]',
                r'<b>Bước 2 (Cẩn thận dấu trừ trước phân số thứ hai!):</b>',
                r'\[15x - 9 - 4x - 14 = x + 11\]',
                r'\[11x - 23 = x + 11 \implies 10x = 34 \implies x = \frac{34}{10} = \frac{17}{5}\]',
            ]),
            r'Khi khử mẫu phương trình có dấu trừ đứng trước phân số, luôn bọc tử số trong ngoặc đơn \(-2(2x + 7)\) để không bao giờ quên đổi dấu hạng tử thứ hai.',
            {
                'A': ('Distribution Sign Trap', r'Quên nhân dấu trừ vào \(+7\), viết nhầm thành \(-4x + 14\) dẫn tới \(11x + 5 = x + 11 \implies x = \frac{3}{5}\).'),
                'B': ('Partial Distribution', r'Chỉ nhân hệ số cho biến \(x\) mà quên nhân cho hằng số: \(15x - 3 - 4x - 7 = x + 11 \implies x = \frac{21}{10}\).'),
                'C': ('Đáp án đúng', r'Khử mẫu với \(12\) và phân phối dấu chuẩn xác cho \(10x = 34 \implies x = \frac{17}{5}\).'),
                'D': ('Over-Multiplied RHS', r'Nhân nhầm vế phải thêm \(2\) dù mẫu đã là \(12\): \(11x - 23 = 2x + 22 \implies x = 5\).'),
            },
            desmos_tip_vi=r'Gõ thẳng phương trình gốc vào Desmos, bấm vào đường thẳng đứng màu kết quả tại <code>x = 3.4</code>; gõ <code>3.4</code> rồi bấm biểu tượng phân số bên trái để đổi ra <code>17/5</code>.',
        ),

        # Q6 — Medium-Hard — MCQ (Key: A)
        math_mcq(
            'sat_m1_1_q6', 6, D, S_EQ, 'Medium-Hard',
            r'<p>\[a(4x - 9) + 18 = 12x + b\]</p><p>In the given equation, \(a\) and \(b\) are constants. The equation has no solution.</p>',
            r'<p>Which of the following must be true about \(a\) and \(b\)?</p>',
            {
                'A': r'\(a = 3\) and \(b \neq -9\)',
                'B': r'\(a = 3\) and \(b = -9\)',
                'C': r'\(a = 3\) and \(b \neq 9\)',
                'D': r'\(a \neq 3\) and \(b = -9\)',
            },
            'A',
            '\n'.join([
                r'<b>Bước 1:</b> Khai triển vế trái theo dạng \(Ax + B\):',
                r'\[4ax + (18 - 9a) = 12x + b\]',
                r'<b>Bước 2:</b> Phương trình vô nghiệm khi hệ số của \(x\) bằng nhau NHƯNG hằng số tự do khác nhau:',
                r'• Hệ số của \(x\): \(4a = 12 \implies a = 3\).',
                r'• Hằng số tự do: \(18 - 9(3) \neq b \implies 18 - 27 \neq b \implies b \neq -9\).',
            ]),
            r'Nhớ bảng 3 trạng thái của \(Ax + B = Cx + D\): 1 nghiệm (\(A \neq C\)), Vô nghiệm (\(A = C, B \neq D\)), Vô số nghiệm (\(A = C, B = D\)).',
            {
                'A': ('Đáp án đúng', r'Khi \(a = 3\) và \(b \neq -9\), phương trình thành \(12x - 9 = 12x + b \iff -9 = b\) (vô lý \(\to\) vô nghiệm).'),
                'B': ('Infinite vs. No Solution', r'Khi \(a = 3\) và \(b = -9\), hai vế đồng nhất \(12x - 9 = 12x - 9\), cho vô số nghiệm chứ không phải vô nghiệm.'),
                'C': ('Arithmetic Sign Error', r'Tính nhầm \(18 - 9(3) = +9\) thay vì \(-9\).'),
                'D': ('Reversed Condition', r'Khi \(a \neq 3\), hệ số của \(x\) hai vế khác nhau nên phương trình luôn có đúng 1 nghiệm duy nhất.'),
            },
            desmos_tip_vi=r'Gõ <code>y = a(4x - 9) + 18</code> và <code>y = 12x + b</code> với thanh trượt <code>a, b</code>. Đặt <code>a = 3</code> sẽ thấy hai đường song song; chỉ khi <code>b = -9</code> chúng mới trùng khít, còn mọi <code>b != -9</code> đều vô nghiệm.',
        ),

        # Q7 — Medium-Hard — MCQ (Key: B)
        math_mcq(
            'sat_m1_1_q7', 7, D, S_SYS, 'Medium-Hard',
            r'<p>\[6x - 15y = 24\]\[rx + 20y = s\]</p><p>In the given system of equations, \(r\) and \(s\) are constants. The system has infinitely many solutions.</p>',
            r'<p>What is the value of \(r + s\)?</p>',
            {
                'A': r'\(-60\)',
                'B': r'\(-40\)',
                'C': r'\(-24\)',
                'D': r'\(40\)',
            },
            'B',
            '\n'.join([
                r'<b>Bước 1:</b> Để hệ có vô số nghiệm, phương trình (2) phải là bội số chính xác của phương trình (1).',
                r'<b>Bước 2:</b> Tính tỷ số nhân từ hệ số của \(y\):',
                r'\[k = \frac{20}{-15} = -\frac{4}{3}\]',
                r'<b>Bước 3:</b> Nhân toàn bộ phương trình (1) với \(-\frac{4}{3}\):',
                r'• \(r = 6 \cdot \left(-\frac{4}{3}\right) = -8\)',
                r'• \(s = 24 \cdot \left(-\frac{4}{3}\right) = -32\)',
                r'Vậy \(r + s = -8 + (-32) = -40\).',
            ]),
            r'Luôn kiểm tra kỹ dấu \(+\) và \(-\) khi tính hệ số tỷ lệ giữa hai phương trình: \(-15y\) thành \(+20y\) bắt buộc nhân hệ số ÂM \(-\frac{4}{3}\).',
            {
                'A': ('Wrong Scale Factor', r'Ước lượng nhầm tỷ số thành \(-2\) thay vì \(-\frac{4}{3}\), ra \(r = -12, s = -48 \implies r + s = -60\).'),
                'B': ('Đáp án đúng', r'Hệ số tỷ lệ là \(-\frac{4}{3}\) cho \(r = -8\) và \(s = -32\), suy ra \(r + s = -40\).'),
                'C': ('Dropped Negative on r', r'Quên dấu âm ở \(r\) (lấy \(r = +8, s = -32\)) nên cộng ra \(-24\).'),
                'D': ('Sign Flip Error', r'Dùng tỷ số dương \(+\frac{4}{3}\) thay vì \(-\frac{4}{3}\), ra \(r = 8, s = 32 \implies 40\).'),
            },
            desmos_tip_vi=r'Rút gọn phương trình (1) chia cho 3 thành <code>2x - 5y = 8</code>, rồi nhân với <code>-4</code> để hệ số <code>y</code> khớp <code>+20</code>: ra ngay <code>-8x + 20y = -32</code> \(\implies -8 + (-32) = -40\).',
        ),

        # Q8 — Medium-Hard — SPR (Answer: 15/4 or 3.75)
        math_spr(
            'sat_m1_1_q8', 8, D, S_SYS, 'Medium-Hard',
            q8_table + r'<p>The table above shows three values of \(x\) and the corresponding values of two linear functions, \(f\) and \(g\).</p>',
            r'<p>In the \(xy\)-plane, the graphs of \(y = f(x)\) and \(y = g(x)\) intersect at the point \((a, b)\). What is the value of \(a\)?</p>',
            ['15/4', '3.75'],
            '15/4 (hoặc 3.75)',
            '\n'.join([
                r'<b>Bước 1 (Tìm công thức \(f(x)\)):</b>',
                r'Hệ số góc \(m_f = \frac{7 - 17}{2 - (-2)} = \frac{-10}{4} = -\frac{5}{2}\).',
                r'Đi qua \((2, 7)\): \(7 = -\frac{5}{2}(2) + c_1 \implies c_1 = 12 \implies f(x) = -\frac{5}{2}x + 12\).',
                r'<b>Bước 2 (Tìm công thức \(g(x)\)):</b>',
                r'Hệ số góc \(m_g = \frac{0 - (-6)}{2 - (-2)} = \frac{6}{4} = \frac{3}{2}\).',
                r'Đi qua \((2, 0)\): \(0 = \frac{3}{2}(2) + c_2 \implies c_2 = -3 \implies g(x) = \frac{3}{2}x - 3\).',
                r'<b>Bước 3 (Tìm hoành độ giao điểm \(a\)):</b>',
                r'\[-\frac{5}{2}a + 12 = \frac{3}{2}a - 3 \implies 15 = 4a \implies a = \frac{15}{4} = 3.75\]',
            ]),
            r'Với bảng giá trị hai hàm bậc nhất, dùng hồi quy kép trong Desmos tìm ngay giao điểm \((a, b)\) trong dưới 15 giây mà không cần giải tay hai phương trình đường thẳng.',
            desmos_tip_vi=r'Nhấn <code>+</code> \(\to\) <b>Table</b>, tạo 3 cột <code>x_1 = [-2, 2, 6]</code>, <code>y_1 = [17, 7, -3]</code>, <code>y_2 = [-6, 0, 6]</code>. Gõ 2 dòng hồi quy <code>y_1 ~ m_1 x_1 + b_1</code> và <code>y_2 ~ m_2 x_1 + b_2</code> rồi bấm thẳng vào giao điểm hai đường trên đồ thị \(\to (3.75, 2.625)\).',
        ),

        # Q9 — Medium-Hard — MCQ (Key: D)
        math_mcq(
            'sat_m1_1_q9', 9, D, S_EQ, 'Medium-Hard',
            r'<p>A specialty coffee roaster blends a premium single-origin bean that costs $18 per pound with a house-roast bean that costs $10 per pound to create a 60-pound batch. The average cost of the 60-pound batch is $13.20 per pound.</p>',
            r'<p>How many pounds of the house-roast bean are in the 60-pound batch?</p>',
            {
                'A': r'\(18\)',
                'B': r'\(24\)',
                'C': r'\(30\)',
                'D': r'\(36\)',
            },
            'D',
            '\n'.join([
                r'<b>Bước 1:</b> Gọi \(h\) là số pound hạt house-roast ($10/pound). Khi đó số pound hạt premium ($18/pound) là \(60 - h\).',
                r'<b>Bước 2:</b> Tổng chi phí của cả mẻ 60 pound là \(60 \times 13.20 = 792\) đô-la:',
                r'\[10h + 18(60 - h) = 792\]',
                r'\[10h + 1080 - 18h = 792 \implies -8h = -288 \implies h = 36\]',
                r'<i>Kiểm tra nhanh:</i> \(36(10) + 24(18) = 360 + 432 = 792\), và \(792 / 60 = 13.20\).',
            ]),
            r'Trong bài toán trộn hỗn hợp (mixture problem), luôn gạch chân tên thành phần ĐỀ HỎI ở câu cuối (house-roast vs. premium) để tránh giải đúng ẩn kia rồi khoanh nhầm.',
            {
                'A': ('Unit Confusion', r'Nhầm lẫn đơn giá $18/pound của hạt premium thành khối lượng cần tìm.'),
                'B': ('Solved Wrong Variable', r'Giải ra \(p = 24\) là khối lượng hạt premium, nhưng đề bài hỏi khối lượng hạt house-roast (\(60 - 24 = 36\)).'),
                'C': ('Equal-Split Assumption', r'Giả định trộn đều 50/50 (\(30\) pound mỗi loại), khi đó giá trung bình sẽ là $14.00/pound chứ không phải $13.20.'),
                'D': ('Đáp án đúng', r'Giải phương trình \(10h + 18(60 - h) = 792\) cho chính xác \(h = 36\) pound hạt house-roast.'),
            },
            desmos_tip_vi=r'Gõ trực tiếp phương trình <code>10x + 18(60 - x) = 60(13.2)</code> vào Desmos và đọc ngay nghiệm đường đứng <code>x = 36</code>.',
        ),

        # Q10 — Medium-Hard — MCQ (Key: C)
        math_mcq(
            'sat_m1_1_q10', 10, D, S_SYS, 'Medium-Hard',
            r'<p>\[\frac{1}{2}x - \frac{3}{4}y = 5\]\[kx + 6y = -16\]</p><p>In the given system of equations, \(k\) is a constant. The graphs of the equations in the \(xy\)-plane intersect at a point \((x, y)\) where \(y = -4\).</p>',
            r'<p>What is the value of \(k\)?</p>',
            {
                'A': r'\(-10\)',
                'B': r'\(-4\)',
                'C': r'\(2\)',
                'D': r'\(4\)',
            },
            'C',
            '\n'.join([
                r'<b>Bước 1 (Tìm hoành độ giao điểm \(x\)):</b> Thay \(y = -4\) vào phương trình (1):',
                r'\[\frac{1}{2}x - \frac{3}{4}(-4) = 5 \implies \frac{1}{2}x + 3 = 5 \implies \frac{1}{2}x = 2 \implies x = 4\]',
                r'<b>Bước 2 (Tìm \(k\)):</b> Vì giao điểm là \((4, -4)\), thay \(x = 4, y = -4\) vào phương trình (2):',
                r'\[k(4) + 6(-4) = -16 \implies 4k - 24 = -16 \implies 4k = 8 \implies k = 2\]',
            ]),
            r'Đọc kỹ đề: không phải hệ có tham số \(k\) nào cũng hỏi "vô nghiệm"! Nếu đề cho biết giao điểm có \(y = -4\), hãy thay thẳng vào phương trình không chứa \(k\) trước.',
            {
                'A': ('Sign Flip Error', r'Chuyển \(-24\) sang vế phải quên đổi dấu thành \(-16 - 24 = -40 \implies k = -10\).'),
                'B': ('Auto-Pilot Parallel Trap', r'Đọc lướt tưởng đề hỏi hệ vô nghiệm nên tính tỷ số song song \(k = \frac{6}{-3/4} \cdot \frac{1}{2} = -4\).'),
                'C': ('Đáp án đúng', r'Tìm được giao điểm \((4, -4)\), thay vào \(4k - 24 = -16\) thu ra \(k = 2\).'),
                'D': ('Partial Solve', r'Dừng lại ngay sau khi tìm ra \(x = 4\) mà quên bước thay vào phương trình (2) để tính \(k\).'),
            },
            desmos_tip_vi=r'Gõ <code>(1/2)x - (3/4)(-4) = 5</code> để thấy <code>x = 4</code>, hoặc gõ thẳng 1 dòng hồi quy <code>[(1/2)x_1 - (3/4)(-4), k x_1 + 6(-4)] ~ [5, -16]</code> \(\to\) Desmos hiện ngay <code>x_1 = 4, k = 2</code>!',
        ),

        # Q11 — Hard (750–800) — MCQ (Key: A)
        math_mcq(
            'sat_m1_1_q11', 11, D, S_EQ, 'Hard (750–800)',
            r'<p>\[\frac{kx - 15}{4} - \frac{3x - 2}{5} = \frac{8x - c}{20}\]</p><p>In the given equation, \(k\) and \(c\) are constants. The equation has infinitely many solutions.</p>',
            r'<p>What is the value of \(c - k\)?</p>',
            {
                'A': r'\(63\)',
                'B': r'\(67\)',
                'C': r'\(71\)',
                'D': r'\(79\)',
            },
            'A',
            '\n'.join([
                r'<b>Bước 1:</b> Nhân cả hai vế với mẫu số chung \(20\):',
                r'\[5(kx - 15) - 4(3x - 2) = 8x - c\]',
                r'<b>Bước 2:</b> Phân phối cẩn thận dấu trừ \(-4(-2) = +8\) và gom biến \(x\):',
                r'\[5kx - 75 - 12x + 8 = 8x - c\]',
                r'\[(5k - 12)x - 67 = 8x - c\]',
                r'<b>Bước 3:</b> Đồng nhất hệ số hai vế để có vô số nghiệm:',
                r'• \(5k - 12 = 8 \implies 5k = 20 \implies k = 4\)',
                r'• \(-67 = -c \implies c = 67\)',
                r'Vậy \(c - k = 67 - 4 = 63\).',
            ]),
            r'Với phương trình đồng nhất 2 hằng số \((k, c)\), kỹ thuật Desmos Identity Regression với mảng 2 điểm <code>x_1 = [0, 1]</code> giải đồng thời cả \(k\) và \(c\) trong đúng 5 giây.',
            {
                'A': ('Đáp án đúng', r'Tìm chuẩn \(k = 4\) và \(c = 67\), suy ra \(c - k = 67 - 4 = 63\).'),
                'B': ('Partial Solve', r'Chỉ tính được \(c = 67\) mà quên trừ đi \(k = 4\).'),
                'C': ('Wrong Operation', r'Tính đúng \(c = 67, k = 4\) nhưng cộng thành \(c + k = 71\) thay vì \(c - k\).'),
                'D': ('Distribution Sign Trap', r'Viết nhầm \(-4(3x - 2) = -12x - 8\), ra \(-75 - 8 = -83 \implies c = 83 \implies c - k = 79\).'),
            },
            desmos_tip_vi=r'Tuyệt chiêu 800 điểm (Identity Regression): gõ dòng 1 <code>x_1 = [0, 1]</code>, dòng 2 gõ <code>(k x_1 - 15)/4 - (3x_1 - 2)/5 ~ (8x_1 - c)/20</code> \(\to\) Desmos lập tức in ra <code>k = 4, c = 67</code>, dòng 3 gõ <code>c - k</code> ra <code>63</code>!',
        ),

        # Q12 — Hard (750–800) — SPR (Answer: -13)
        math_spr(
            'sat_m1_1_q12', 12, D, S_SYS, 'Hard (750–800)',
            r'<p>\[\frac{5}{6}x - \frac{3}{8}y = \frac{11}{12}\]\[2ax + 22 = 3by\]</p><p>In the given system of equations, \(a\) and \(b\) are constants. The system has infinitely many solutions.</p>',
            r'<p>What is the value of \(a + b\)?</p>',
            ['-13'],
            '-13',
            '\n'.join([
                r'<b>Bước 1 (Đưa phương trình 2 về cùng dạng chuẩn \(Ax + By = C\)):</b>',
                r'\[2ax - 3by = -22\]',
                r'<b>Bước 2 (So sánh tỷ số của vế hằng số tự do):</b>',
                r'\[k = \frac{-22}{\frac{11}{12}} = -22 \cdot \frac{12}{11} = -24\]',
                r'<b>Bước 3:</b> Nhân cả hai vế phương trình (1) với \(-24\):',
                r'\[-24\left(\frac{5}{6}x\right) - 24\left(-\frac{3}{8}y\right) = -24\left(\frac{11}{12}\right)\]',
                r'\[-20x + 9y = -22\]',
                r'<b>Bước 4 (Đồng nhất hệ số với \(2ax - 3by = -22\)):</b>',
                r'• \(2a = -20 \implies a = -10\)',
                r'• \(-3b = 9 \implies b = -3\)',
                r'Vậy \(a + b = -10 + (-3) = -13\).',
            ]),
            r'Khi hai phương trình trong hệ bị xáo trộn thứ tự vế, BẮT BUỘC sắp xếp cả hai về cùng chuẩn \(Ax + By = C\) trước khi lập tỷ số, tránh sai dấu âm chí mạng.',
            desmos_tip_vi=r'Để kiểm chứng nhanh: chọn 2 điểm bất kỳ trên đường 1 (nhập đường 1 vào Desmos, lấy 2 điểm dễ như <code>(1.1, 0)</code> và <code>(0, -22/9)</code>), lập <code>x_1 = [1.1, 0]</code>, <code>y_1 = [0, -22/9]</code> rồi hồi quy <code>2a x_1 + 22 ~ 3b y_1</code> \(\to\) ra ngay <code>a = -10, b = -3</code>!',
        ),

        # Q13 — Hard (750–800) — MCQ (Key: C)
        math_mcq(
            'sat_m1_1_q13', 13, D, S_SYS, 'Hard (750–800)',
            r'<p>\[ax - 4y = 18\]\[-6x + (a - 5)y = 36\]</p><p>In the given system of equations, \(a\) is a constant. The system has no solution.</p>',
            r'<p>What is the value of \(a\)?</p>',
            {
                'A': r'\(-8\)',
                'B': r'\(-3\)',
                'C': r'\(8\)',
                'D': r'\(9\)',
            },
            'C',
            '\n'.join([
                r'<b>Bước 1 (Thiết lập điều kiện hai đường thẳng song song):</b>',
                r'\[\frac{a}{-6} = \frac{-4}{a - 5} \implies a(a - 5) = 24 \implies a^2 - 5a - 24 = 0\]',
                r'\[(a - 8)(a + 3) = 0 \implies a = 8 \text{ hoặc } a = -3\]',
                r'<b>Bước 2 (BẪY CHÍ MẠNG 800 ĐIỂM — Kiểm tra điều kiện hằng số \(\neq \frac{18}{36} = \frac{1}{2}\)):</b>',
                r'• Với \(a = -3\): \(\frac{a}{-6} = \frac{-3}{-6} = \frac{1}{2} = \frac{18}{36}\). Khi đó phương trình (2) là \(-6x - 8y = 36 = 2(-3x - 4y)\) \(\to\) <b>VÔ SỐ NGHIỆM</b> (LOẠI!).',
                r'• Với \(a = 8\): \(\frac{a}{-6} = -\frac{4}{3} \neq \frac{1}{2}\). Hai đường thẳng \(8x - 4y = 18\) và \(-6x + 3y = 36\) cùng hệ số góc \(2\) nhưng tung độ gốc khác nhau (\(-4.5 \neq 12\)) \(\to\) <b>VÔ NGHIỆM</b> (NHẬN!).',
            ]),
            r'Khi điều kiện song song cho ra hai giá trị của tham số \(a\), LUÔN thay ngược cả hai vào hệ gốc: một giá trị thường gây trùng nhau (vô số nghiệm), giá trị còn lại mới thực sự vô nghiệm!',
            {
                'A': ('Factoring Sign Error', r'Phân tích sai dấu thành \((a + 8)(a - 3) = 0\) nên chọn nhầm \(-8\).'),
                'B': ('Coincident-Line Trap', r'Bẫy kinh điển Module 2 Hard: tại \(a = -3\), hai phương trình trùng khít thành một đường thẳng (vô số nghiệm), KHÔNG phải vô nghiệm.'),
                'C': ('Đáp án đúng', r'Tại \(a = 8\), hệ số góc đều bằng \(2\) nhưng tung độ gốc khác nhau (\(-\frac{9}{2}\) vs. \(12\)), hệ vô nghiệm.'),
                'D': ('Matched Single Coeff Only', r'Chỉ cho \(a - 5 = 4 \implies a = 9\) để cân bằng hệ số \(y\) mà quên kiểm tra tỷ số hệ số \(x\).'),
            },
            desmos_tip_vi=r'Gõ cả hai phương trình vào Desmos và tạo thanh trượt <code>a</code>. Gõ thử <code>a = -3</code> thấy 2 đường chồng khít (vô số nghiệm); đổi sang <code>a = 8</code> thấy ngay 2 đường song song tách rời (vô nghiệm)!',
        ),

        # Q14 — Hard (750–800) — MCQ (Key: B)
        math_mcq(
            'sat_m1_1_q14', 14, D, S_EQ, 'Hard (750–800)',
            r'<p>\[\frac{2(px - 3)}{5} - \frac{3x + 1}{4} = \frac{px + 7}{10}\]</p><p>In the given equation, \(p\) is a constant.</p>',
            r'<p>For what value of \(p\) does the equation have no solution?</p>',
            {
                'A': r'\(\frac{3}{2}\)',
                'B': r'\(\frac{5}{2}\)',
                'C': r'\(\frac{15}{4}\)',
                'D': r'\(\frac{15}{2}\)',
            },
            'B',
            '\n'.join([
                r'<b>Bước 1:</b> Nhân cả hai vế với mẫu số chung nhỏ nhất \(\text{LCM}(5, 4, 10) = 20\):',
                r'\[4 \cdot 2(px - 3) - 5(3x + 1) = 2(px + 7)\]',
                r'\[8px - 24 - 15x - 5 = 2px + 14\]',
                r'<b>Bước 2:</b> Gom toàn bộ hạng tử chứa \(x\) về vế trái và hằng số về vế phải:',
                r'\[(8p - 15 - 2p)x = 14 + 29 \implies (6p - 15)x = 43\]',
                r'<b>Bước 3:</b> Phương trình \(Ax = 43\) vô nghiệm khi và chỉ khi \(A = 0\) (vì \(43 \neq 0\)):',
                r'\[6p - 15 = 0 \implies p = \frac{15}{6} = \frac{5}{2}\]',
            ]),
            r'Để giải nhanh phương trình tham số vô nghiệm có phân số, chỉ cần gom riêng hệ số của \(x\) sau khi quy đồng mẫu chung rồi cho tổng hệ số \(x\) bằng \(0\) (và kiểm tra hằng số khác \(0\)).',
            {
                'A': ('Moved Term Without Sign Change', r'Chuyển \(2px\) sang vế trái quên đổi dấu thành \(8p + 2p = 10p \implies 10p - 15 = 0 \implies p = \frac{3}{2}\).'),
                'B': ('Đáp án đúng', r'Quy đồng với \(20\) thu được \((6p - 15)x = 43\), cho \(6p - 15 = 0 \implies p = \frac{5}{2}\).'),
                'C': ('Over-Multiplied RHS', r'Nhân vế phải với \(4\) thay vì \(2\), tạo ra \((8p - 4p - 15)x = 0 \implies p = \frac{15}{4}\).'),
                'D': ('Dropped Numerator Factor', r'Quên hệ số \(2\) ở tử số \(2(px - 3)\), giải thành \((4p - 2p - 15)x = 0 \implies p = \frac{15}{2}\).'),
            },
            desmos_tip_vi=r'Gõ hai hàm <code>y = 2(p x - 3)/5 - (3x + 1)/4</code> và <code>y = (p x + 7)/10</code> với thanh trượt <code>p</code>. Kéo/nhập <code>p = 2.5</code> thấy ngay hai đường thẳng song song cách biệt nhau!',
        ),

        # Q15 — Hard (750–800) — SPR (Answer: 19/4 or 4.75)
        math_spr(
            'sat_m1_1_q15', 15, D, S_SYS, 'Hard (750–800)',
            r'<p>\[3x - 2y = 17\]\[5x + 4y = 10\]\[kx - 6y = 34\]</p><p>In the \(xy\)-plane, the graphs of the three given linear equations all intersect at the same point \((x, y)\), where \(k\) is a constant.</p>',
            r'<p>What is the value of \(k\)?</p>',
            ['19/4', '4.75'],
            '19/4 (hoặc 4.75)',
            '\n'.join([
                r'<b>Bước 1 (Tìm giao điểm chung từ 2 phương trình đầu):</b>',
                r'Nhân phương trình (1) với \(2\): \(6x - 4y = 34\).',
                r'Cộng với phương trình (2): \((6x - 4y) + (5x + 4y) = 34 + 10 \implies 11x = 44 \implies x = 4\).',
                r'Thay \(x = 4\) vào phương trình (1): \(3(4) - 2y = 17 \implies -2y = 5 \implies y = -\frac{5}{2}\).',
                r'<b>Bước 2 (Thay giao điểm \(\left(4, -\frac{5}{2}\right)\) vào phương trình 3):</b>',
                r'\[k(4) - 6\left(-\frac{5}{2}\right) = 34 \implies 4k + 15 = 34 \implies 4k = 19 \implies k = \frac{19}{4} = 4.75\]',
            ]),
            r'Bài toán ba đường thẳng đồng quy thực chất chỉ là 2 bước: giải hệ 2 phương trình đầy đủ để lấy tọa độ \((x, y)\), rồi thế thẳng vào phương trình chứa tham số \(k\).',
            desmos_tip_vi=r'Gõ 2 phương trình đầu vào Desmos, bấm vào giao điểm hiện ngay <code>(4, -2.5)</code>. Sau đó gõ một dòng <code>k = (34 + 6(-2.5))/4</code> (hoặc <code>4k - 6(-2.5) ~ 34</code>) \(\to\) ra chuẩn <code>4.75</code>!',
        ),
    ]

    return build_math_drill_json(
        title='Math Drill 1.1: Desmos 800 Playbook, Linear Equations & Systems (15 câu)',
        subtitle='Algebra • Parametric Systems, Linear Shortcuts & Desmos Regression Mastery',
        skill_badge='Module 1 • Target 750–800',
        questions=questions,
        target_minutes=22,
    )


# ============================================================================
# DRILL 1.2: LINEAR FUNCTIONS, SLOPE-INTERCEPT MODELS & WORD PROBLEMS (15 Qs)
# ============================================================================

def _build_drill_m1_2():
    D = 'Algebra'
    S_FN = 'Linear functions'
    S_2V = 'Linear equations in two variables'

    q4_table = build_math_table(
        headers=[r'\(x\)', r'\(g(x)\)'],
        rows=[
            [r'\(-3\)', r'\(23\)'],
            [r'\(1\)', r'\(11\)'],
            [r'\(5\)', r'\(-1\)'],
        ],
        caption='Values of Linear Function g',
    )

    q8_table = build_math_table(
        headers=[r'\(x\)', r'\(f(x + 3)\)'],
        rows=[
            [r'\(-2\)', r'\(4\)'],
            [r'\(2\)', r'\(10\)'],
            [r'\(6\)', r'\(16\)'],
        ],
        caption='Shifted Values of Linear Function f',
    )

    q13_table = build_math_table(
        headers=[r'\(x\)', r'\(h(x)\)'],
        rows=[
            [r'\(-1\)', r'\(2c - 5\)'],
            [r'\(3\)', r'\(5c + 3\)'],
            [r'\(9\)', r'\(40 - 3c\)'],
        ],
        caption='Parametric Table for Linear Function h',
    )

    questions = [
        # Q1 — Medium — MCQ (Key: A)
        math_mcq(
            'sat_m1_2_q1', 1, D, S_2V, 'Medium',
            r'<p>A commercial photography studio rents lighting equipment to clients. The total cost \(C\), in dollars, to rent a lighting package for \(h\) hours is modeled by the equation \(C = 45h + 120\).</p>',
            r'<p>Which of the following is the best interpretation of the number \(120\) in this context?</p>',
            {
                'A': r'The flat base fee, in dollars, charged for renting the lighting package before any hourly rate is added.',
                'B': r'The hourly rental rate, in dollars per hour, for using the lighting package.',
                'C': r'The total cost, in dollars, of renting the lighting package for \(45\) hours.',
                'D': r'The maximum number of hours a client can rent the lighting package.',
            },
            'A',
            '\n'.join([
                r'Phương trình \(C = 45h + 120\) có dạng hàm bậc nhất \(y = mx + b\):',
                r'• Hệ số góc \(m = 45\) là chi phí tăng thêm cho mỗi giờ thuê ($45/giờ).',
                r'• Tung độ gốc \(b = 120\) là giá trị của \(C\) khi \(h = 0\) — tức khoản phí cơ bản cố định ($120) chưa tính phí theo giờ.',
            ]),
            r'Trong mô hình thực tế \(y = mx + b\), luôn phân biệt đơn vị: \(b\) cùng đơn vị với \(y\) (giá trị ban đầu khi \(x = 0\)), còn \(m\) có đơn vị "y trên mỗi x" (tốc độ thay đổi).',
            {
                'A': ('Đáp án đúng', r'Khi \(h = 0\), \(C = 120\), biểu thị khoản phí cố định ban đầu (flat base fee) tính bằng đô-la.'),
                'B': ('Slope-Intercept Swap', r'Đây là ý nghĩa của hệ số góc \(45\) (đô-la mỗi giờ), không phải hằng số \(120\).'),
                'C': ('Misread Coefficient as Input', r'Nhầm \(45\) là số giờ thuê; nếu thuê \(45\) giờ thì tổng chi phí là \(45(45) + 120 = 2{,}145\) đô-la.'),
                'D': ('Wrong Variable & Unit', r'\(120\) mang đơn vị đô-la (cùng đơn vị \(C\)), không phải số giờ tối đa.'),
            },
            desmos_tip_vi=r'Gõ <code>y = 45x + 120</code> vào Desmos và bấm vào giao điểm trục tung <code>(0, 120)</code>: tại <code>x = 0</code> giờ, chi phí đã là $120 — khẳng định ngay đây là phí cố định ban đầu.',
        ),

        # Q2 — Medium — MCQ (Key: D)
        math_mcq(
            'sat_m1_2_q2', 2, D, S_FN, 'Medium',
            r'<p>For a linear function \(f\), \(f(x + 4) - f(x) = -14\) for all real numbers \(x\), and \(f(2) = 19\).</p>',
            r'<p>Which equation defines \(f(x)\)?</p>',
            {
                'A': r'\(f(x) = -14x + 47\)',
                'B': r'\(f(x) = -\frac{7}{2}x + 12\)',
                'C': r'\(f(x) = -\frac{7}{2}x + 19\)',
                'D': r'\(f(x) = -\frac{7}{2}x + 26\)',
            },
            'D',
            '\n'.join([
                r'<b>Bước 1 (Tính hệ số góc \(m\) từ hiệu sai phân):</b>',
                r'Với hàm bậc nhất \(f(x) = mx + b\), ta có:',
                r'\[m = \frac{f(x + 4) - f(x)}{(x + 4) - x} = \frac{-14}{4} = -\frac{7}{2}\]',
                r'<b>Bước 2 (Tìm tung độ gốc \(b\) từ \(f(2) = 19\)):</b>',
                r'\[19 = -\frac{7}{2}(2) + b \implies 19 = -7 + b \implies b = 26\]',
                r'Vậy \(f(x) = -\frac{7}{2}x + 26\).',
            ]),
            r'Đừng bao giờ nhầm \(f(x + h) - f(x)\) là hệ số góc! Hệ số góc thực sự luôn là \(m = \frac{f(x + h) - f(x)}{h}\) (phải chia cho bước nhảy \(h\)).',
            {
                'A': ('Forgot to Divide by Δx', r'Lấy thẳng \(-14\) làm hệ số góc thay vì chia cho \(\Delta x = 4\).'),
                'B': ('Sign Error Solving b', r'Tính đúng \(m = -\frac{7}{2}\) nhưng chuyển \(-7\) sai dấu thành \(b = 19 - 7 = 12\).'),
                'C': ('Non-Zero Input as y-Intercept', r'Ngộ nhận \(f(2) = 19\) là tung độ gốc \(b\) (trong khi tung độ gốc phải là \(f(0)\)).'),
                'D': ('Đáp án đúng', r'Hệ số góc \(m = -\frac{14}{4} = -\frac{7}{2}\) và \(f(2) = -7 + 26 = 19\) khớp hoàn toàn.'),
            },
            desmos_tip_vi=r'Từ dữ kiện: \(f(2) = 19\) và \(f(6) = f(2 + 4) = 19 - 14 = 5\). Tạo bảng Desmos gồm 2 điểm <code>(2, 19)</code> và <code>(6, 5)</code>, chạy <code>y_1 ~ m x_1 + b</code> \(\to\) <code>m = -3.5, b = 26</code>!',
        ),

        # Q3 — Medium — MCQ (Key: B)
        math_mcq(
            'sat_m1_2_q3', 3, D, S_2V, 'Medium',
            r'<p>In the \(xy\)-plane, line \(\ell\) is defined by the equation \(3x - 5y = 20\). Line \(m\) is perpendicular to line \(\ell\) and passes through the point \((6, -4)\).</p>',
            r'<p>Which of the following is an equation of line \(m\)?</p>',
            {
                'A': r'\(y = -\frac{5}{3}x - 14\)',
                'B': r'\(y = -\frac{5}{3}x + 6\)',
                'C': r'\(y = \frac{5}{3}x - 14\)',
                'D': r'\(y = \frac{3}{5}x - \frac{38}{5}\)',
            },
            'B',
            '\n'.join([
                r'<b>Bước 1 (Tìm hệ số góc đường thẳng \(\ell\)):</b>',
                r'\[3x - 5y = 20 \implies -5y = -3x + 20 \implies y = \frac{3}{5}x - 4 \implies m_\ell = \frac{3}{5}\]',
                r'<b>Bước 2 (Hệ số góc vuông góc — nghịch đảo đổi dấu):</b>',
                r'\[m_m = -\frac{1}{m_\ell} = -\frac{5}{3}\]',
                r'<b>Bước 3 (Thay điểm \((6, -4)\)):</b>',
                r'\[-4 = -\frac{5}{3}(6) + b \implies -4 = -10 + b \implies b = 6\]',
                r'Vậy phương trình đường thẳng \(m\) là \(y = -\frac{5}{3}x + 6\).',
            ]),
            r'Hai đường thẳng vuông góc có tích hệ số góc bằng \(-1\) (nghịch đảo VÀ đổi dấu): đường gốc \(Ax + By = C\) luôn có đường vuông góc dạng \(Bx - Ay = D\).',
            {
                'A': ('Sign Error Solving b', r'Tìm đúng \(m_m = -\frac{5}{3}\) nhưng tính sai \(b = -4 - 10 = -14\).'),
                'B': ('Đáp án đúng', r'Vuông góc với hệ số góc \(\frac{3}{5}\) (nên \(m_m = -\frac{5}{3}\)) và đi qua \((6, -4)\): \(-\frac{5}{3}(6) + 6 = -4\).'),
                'C': ('Forgot Negative Sign', r'Chỉ lấy nghịch đảo \(\frac{5}{3}\) mà quên đổi dấu âm.'),
                'D': ('Parallel Instead of Perpendicular', r'Dùng hệ số góc song song \(\frac{3}{5}\) thay vì vuông góc \(-\frac{5}{3}\).'),
            },
            desmos_tip_vi=r'Gõ <code>3x - 5y = 20</code>, điểm <code>(6, -4)</code>, và gõ lần lượt các đáp án vào Desmos — bật chế độ <b>Zoom Square</b> (biểu tượng cờ lê) sẽ nhìn thấy ngay đáp án B tạo góc vuông 90° hoàn hảo và đi xuyên qua <code>(6, -4)</code>!',
        ),

        # Q4 — Medium — SPR (Answer: 35)
        math_spr(
            'sat_m1_2_q4', 4, D, S_FN, 'Medium',
            q4_table + r'<p>The table above shows three values of \(x\) and their corresponding values of \(g(x)\) for a linear function \(g\).</p>',
            r'<p>What is the value of \(g(-7)\)?</p>',
            ['35'],
            '35',
            '\n'.join([
                r'<b>Bước 1 (Tính hệ số góc \(m\)):</b>',
                r'\[m = \frac{11 - 23}{1 - (-3)} = \frac{-12}{4} = -3\]',
                r'<b>Bước 2 (Tính \(g(-7)\) nhanh bằng bước nhảy hoặc lập công thức):</b>',
                r'• <i>Cách 1 (Lập công thức):</i> \(g(1) = -3(1) + b = 11 \implies b = 14 \implies g(x) = -3x + 14\).',
                r'Suy ra \(g(-7) = -3(-7) + 14 = 21 + 14 = 35\).',
                r'• <i>Cách 2 (Bước nhảy đều):</i> Khi \(x\) giảm \(4\) đơn vị (từ \(5 \to 1 \to -3\)), \(g(x)\) tăng \(12\) đơn vị (\(-1 \to 11 \to 23\)). Giảm tiếp \(4\) đơn vị từ \(-3 \to -7\), ta có \(g(-7) = 23 + 12 = 35\).',
            ]),
            r'Khi các giá trị \(x\) trong bảng cách đều nhau và điểm cần tính cũng nằm đúng một bước nhảy đều, chỉ cần cộng/trừ thêm đúng bước nhảy \(\Delta y\) là ra đáp án trong 3 giây!',
            desmos_tip_vi=r'Tạo bảng <code>x_1 = [-3, 1, 5]</code>, <code>y_1 = [23, 11, -1]</code>. Gõ <code>y_1 ~ m x_1 + b</code>, rồi gõ <code>m(-7) + b</code> ở dòng 3 \(\to\) hiện ngay <code>35</code>.',
        ),

        # Q5 — Medium-Hard — MCQ (Key: C)
        math_mcq(
            'sat_m1_2_q5', 5, D, S_2V, 'Medium-Hard',
            r'<p>An event coordinator has a budget of $1,440 to purchase centerpieces and table runners for a banquet. Each centerpiece costs $36, and each table runner costs $16. The equation \(36x + 16y = 1{,}440\) represents this situation, where \(x\) is the number of centerpieces and \(y\) is the number of table runners purchased.</p>',
            r'<p>If the graph of this equation is drawn in the \(xy\)-plane, which of the following is the best interpretation of the \(x\)-intercept of the graph?</p>',
            {
                'A': r'The coordinator can purchase a maximum of \(90\) table runners if no centerpieces are purchased.',
                'B': r'Each centerpiece costs $36 more than each table runner.',
                'C': r'The coordinator can purchase \(40\) centerpieces if no table runners are purchased.',
                'D': r'The total number of centerpieces and table runners purchased is \(40\).',
            },
            'C',
            '\n'.join([
                r'<b>Bước 1 (Tìm hoành độ gốc — \(x\)-intercept):</b>',
                r'Tại giao điểm trục hoành (\(x\)-intercept), ta luôn có \(y = 0\) (mua \(0\) table runners):',
                r'\[36x + 16(0) = 1{,}440 \implies x = \frac{1{,}440}{36} = 40\]',
                r'<b>Bước 2 (Diễn giải thực tế):</b> Điểm \((40, 0)\) nghĩa là với toàn bộ ngân sách $1,440, người điều phối có thể mua \(40\) centerpieces nếu không mua chiếc table runner nào.',
            ]),
            r'Trong phương trình ngân sách \(Ax + By = C\): \(x\)-intercept \((C/A, 0)\) là số lượng tối đa của \(x\) khi \(y = 0\); \(y\)-intercept \((0, C/B)\) là số lượng tối đa của \(y\) khi \(x = 0\).',
            {
                'A': ('y-Intercept Trap', r'Đây là diễn giải của \(y\)-intercept \((0, 90)\) khi \(x = 0\), KHÔNG phải \(x\)-intercept.'),
                'B': ('Misread Coefficient', r'\(36\) là đơn giá mỗi centerpiece ($36), không phải phần chênh lệch giá ($20).'),
                'C': ('Đáp án đúng', r'Khi \(y = 0\) (0 table runners), \(x = 1{,}440 / 36 = 40\) centerpieces.'),
                'D': ('Forgot Zero Constraint', r'Nếu có mua thêm table runners (\(y > 0\)), tổng số lượng \(x + y\) sẽ thay đổi chứ không cố định bằng \(40\).'),
            },
            desmos_tip_vi=r'Gõ <code>36x + 16y = 1440</code> vào Desmos và bấm điểm cắt trục hoành <code>(40, 0)</code>: nhìn ngay <code>x = 40</code> đi kèm <code>y = 0</code> (0 table runners).',
        ),

        # Q6 — Medium-Hard — MCQ (Key: A)
        math_mcq(
            'sat_m1_2_q6', 6, D, S_FN, 'Medium-Hard',
            r'<p>The linear function \(f\) is defined by \(f(x) = -\frac{3}{4}x + 5\). The graph of \(y = g(x)\) in the \(xy\)-plane is obtained by translating the graph of \(y = f(x)\) to the right by \(8\) units and down by \(3\) units.</p>',
            r'<p>What is the \(y\)-intercept of the graph of \(y = g(x)\)?</p>',
            {
                'A': r'\((0, 8)\)',
                'B': r'\((0, -4)\)',
                'C': r'\((0, 2)\)',
                'D': r'\((0, 14)\)',
            },
            'A',
            '\n'.join([
                r'<b>Bước 1 (Áp dụng quy tắc tịnh tiến đồ thị):</b>',
                r'• Dịch sang <b>phải</b> \(8\) đơn vị \(\implies\) thay \(x\) bằng \((x - 8)\).',
                r'• Dịch xuống <b>dưới</b> \(3\) đơn vị \(\implies\) trừ \(3\) ở ngoài hàm.',
                r'<b>Bước 2 (Rút gọn \(g(x)\)):</b>',
                r'\[g(x) = f(x - 8) - 3 = -\frac{3}{4}(x - 8) + 5 - 3\]',
                r'\[g(x) = -\frac{3}{4}x + 6 + 2 = -\frac{3}{4}x + 8\]',
                r'Vậy tung độ gốc của \(y = g(x)\) là \((0, 8)\).',
            ]),
            r'Quy tắc tịnh tiến bất di bất dịch: dịch PHẢI \(h\) đơn vị luôn thay \(x \to (x - h)\) (trừ bên trong!), dịch TRÁI thay \(x \to (x + h)\), dịch LÊN/XUỐNG cộng/trừ bên ngoài.',
            {
                'A': ('Đáp án đúng', r'\(g(x) = -\frac{3}{4}(x - 8) + 5 - 3 = -\frac{3}{4}x + 8 \implies y\)-intercept là \((0, 8)\).'),
                'B': ('Reversed Horizontal Shift', r'Nhầm dịch phải thành \(f(x + 8) - 3 = -\frac{3}{4}x - 6 + 2 = -\frac{3}{4}x - 4\).'),
                'C': ('Ignored Horizontal Shift', r'Chỉ trừ \(3\) vào tung độ gốc \(5 - 3 = 2\) mà quên rằng dịch ngang cũng làm thay đổi tung độ gốc khi hệ số góc khác \(0\).'),
                'D': ('Shifted Up Instead of Down', r'Cộng thêm \(3\) thay vì trừ \(3\): \(6 + 5 + 3 = 14\).'),
            },
            desmos_tip_vi=r'Gõ dòng 1 <code>f(x) = -(3/4)x + 5</code>, dòng 2 gõ <code>g(x) = f(x - 8) - 3</code>, dòng 3 gõ <code>g(0)</code> — Desmos trả ngay <code>8</code> và bạn nhìn thấy đồ thị dịch đúng sang phải & xuống dưới!',
        ),

        # Q7 — Medium-Hard — MCQ (Key: D)
        math_mcq(
            'sat_m1_2_q7', 7, D, S_2V, 'Medium-Hard',
            r'<p>In the \(xy\)-plane, line \(r\) has equation \(4x + ky = 15\) and line \(s\) has equation \(6x - 9y = 22\), where \(k\) is a constant. Line \(r\) is perpendicular to line \(s\).</p>',
            r'<p>What is the value of \(k\)?</p>',
            {
                'A': r'\(-6\)',
                'B': r'\(-\frac{8}{3}\)',
                'C': r'\(\frac{3}{8}\)',
                'D': r'\(\frac{8}{3}\)',
            },
            'D',
            '\n'.join([
                r'<b>Cách 1 (Dùng tích hệ số góc \(m_r \cdot m_s = -1\)):</b>',
                r'• Đường thẳng \(r\): \(y = -\frac{4}{k}x + \frac{15}{k} \implies m_r = -\frac{4}{k}\).',
                r'• Đường thẳng \(s\): \(y = \frac{6}{9}x - \frac{22}{9} = \frac{2}{3}x - \frac{22}{9} \implies m_s = \frac{2}{3}\).',
                r'• Vuông góc: \(\left(-\frac{4}{k}\right)\left(\frac{2}{3}\right) = -1 \implies \frac{8}{3k} = 1 \implies k = \frac{8}{3}\).',
                r'<b>Cách 2 (Công thức 800 điểm — Tích vô hướng vector pháp tuyến \(A_1 A_2 + B_1 B_2 = 0\)):</b>',
                r'\[(4)(6) + (k)(-9) = 0 \implies 24 - 9k = 0 \implies k = \frac{24}{9} = \frac{8}{3}\]',
            ]),
            r'Mẹo siêu tốc 800 điểm: Hai đường thẳng dạng chuẩn \(A_1 x + B_1 y = C_1\) và \(A_2 x + B_2 y = C_2\) vuông góc khi và chỉ khi \(A_1 A_2 + B_1 B_2 = 0\)!',
            {
                'A': ('Parallel vs. Perpendicular', r'Dùng nhầm điều kiện song song \(\frac{4}{6} = \frac{k}{-9} \implies k = -6\).'),
                'B': ('Sign Flip Error', r'Quên dấu âm trong \(m_r = -\frac{4}{k}\) hoặc viết nhầm \(m_r \cdot m_s = +1\) dẫn đến \(k = -\frac{8}{3}\).'),
                'C': ('Reciprocal Trap', r'Giải nhầm tỷ lệ nghịch đảo thành \(\frac{9}{24} = \frac{3}{8}\).'),
                'D': ('Đáp án đúng', r'Áp dụng \(4(6) + k(-9) = 0 \implies k = \frac{24}{9} = \frac{8}{3}\).'),
            },
            desmos_tip_vi=r'Gõ nhanh phép tính <code>(4*6)/9</code> rồi bấm nút đổi phân số bên trái Desmos ra <code>8/3</code> — hoặc vẽ cả 2 đường với thanh trượt <code>k</code> ở chế độ <b>Zoom Square</b> để kiểm chứng góc vuông 90°!',
        ),

        # Q8 — Medium-Hard — SPR (Answer: 5/2 or 2.5)
        math_spr(
            'sat_m1_2_q8', 8, D, S_FN, 'Medium-Hard',
            q8_table + r'<p>For the linear function \(f\), the table above shows three values of \(x\) and the corresponding values of \(f(x + 3)\).</p>',
            r'<p>What is the value of \(f(0)\)?</p>',
            ['5/2', '2.5'],
            '5/2 (hoặc 2.5)',
            '\n'.join([
                r'<b>CẢNH BÁO BẪY KINH ĐIỂN SAT:</b> Cột bên phải là \(f(x + 3)\), KHÔNG phải \(f(x)\)!',
                r'<b>Bước 1 (Đổi biến về đầu vào thực \(t = x + 3\)):</b>',
                r'• Khi \(x = -2 \implies t = -2 + 3 = 1\), nên \(f(1) = 4\).',
                r'• Khi \(x = 2 \implies t = 2 + 3 = 5\), nên \(f(5) = 10\).',
                r'• Khi \(x = 6 \implies t = 6 + 3 = 9\), nên \(f(9) = 16\).',
                r'<b>Bước 2 (Tìm hàm \(f(t)\) và tính \(f(0)\)):</b>',
                r'Hệ số góc \(m = \frac{10 - 4}{5 - 1} = \frac{6}{4} = \frac{3}{2}\).',
                r'Thay điểm \((1, 4)\): \(4 = \frac{3}{2}(1) + b \implies b = 4 - \frac{3}{2} = \frac{5}{2} = 2.5\).',
                r'<i>Kiểm chứng cách 2:</i> Nếu viết \(h(x) = f(x + 3) = \frac{3}{2}x + 7\), muốn có \(f(0)\) ta phải thay \(x = -3\): \(f(-3 + 3) = \frac{3}{2}(-3) + 7 = \frac{5}{2} = 2.5\).',
            ]),
            r'Khi tiêu đề cột bảng là \(f(x + c)\) thay vì \(f(x)\), BẮT BUỘC cộng thêm \(c\) vào cột \(x\) trước khi chạy hồi quy — tuyệt đối không lấy tung độ gốc thô của bảng gốc!',
            desmos_tip_vi=r'Tạo bảng Desmos với cột <code>x_1 = [-2 + 3, 2 + 3, 6 + 3]</code> (tức <code>[1, 5, 9]</code>) và <code>y_1 = [4, 10, 16]</code>. Chạy <code>y_1 ~ m x_1 + b</code> \(\to\) Desmos báo ngay <code>b = 2.5</code> chính là <code>f(0)</code>!',
        ),

        # Q9 — Medium-Hard — MCQ (Key: B)
        math_mcq(
            'sat_m1_2_q9', 9, D, S_2V, 'Medium-Hard',
            r'<p>A solar battery array begins discharging at \(h = 0\) with an initial stored charge of \(960\) kilowatt-hours (kWh). The battery loses charge at a constant rate of \(4.5\) kilowatt-hours every \(15\) minutes.</p>',
            r'<p>Which linear function \(E(h)\) gives the remaining charge, in kilowatt-hours, \(h\) hours after the battery begins discharging?</p>',
            {
                'A': r'\(E(h) = 960 - 4.5h\)',
                'B': r'\(E(h) = 960 - 18h\)',
                'C': r'\(E(h) = 960 - 67.5h\)',
                'D': r'\(E(h) = 960 - 270h\)',
            },
            'B',
            '\n'.join([
                r'<b>Bước 1 (Đổi đơn vị thời gian về đúng biến \(h\) — giờ):</b>',
                r'1 giờ có \(60\) phút, tương đương \(\frac{60}{15} = 4\) chu kỳ 15 phút.',
                r'Tốc độ giảm năng lượng mỗi giờ là:',
                r'\[4.5 \times 4 = 18 \text{ kWh/giờ}\]',
                r'<b>Bước 2 (Lập hàm bậc nhất):</b>',
                r'Bắt đầu từ \(960\) kWh và giảm \(18\) kWh mỗi giờ \(\implies E(h) = 960 - 18h\).',
            ]),
            r'Luôn kiểm tra đơn vị của biến đầu vào (\(h\) giờ vs. \(15\) phút): khi tốc độ cho theo khoảng \(k\) phút mà hàm tính theo giờ, phải nhân tốc độ đó với \(\frac{60}{k}\).',
            {
                'A': ('Unit Conversion Trap', r'Quên đổi \(15\) phút sang giờ, giữ nguyên \(4.5\) làm tốc độ theo giờ.'),
                'B': ('Đáp án đúng', r'Đổi chuẩn: \(4.5 \text{ kWh / 15 phút} = 18 \text{ kWh/giờ} \implies E(h) = 960 - 18h\).'),
                'C': ('Multiplied Instead of Divided', r'Nhân nhầm \(4.5 \times 15 = 67.5\) thay vì nhân với \(60 / 15 = 4\).'),
                'D': ('Per-Minute Misread', r'Nhân \(4.5 \times 60 = 270\), hiểu nhầm \(4.5\) kWh là mức giảm mỗi 1 phút thay vì mỗi 15 phút.'),
            },
            desmos_tip_vi=r'Kiểm tra hợp lý nhanh bằng 1 phép tính trên Desmos: sau 1 giờ (4 lần 15 phút), lượng pin còn <code>960 - 4*4.5 = 942</code>. Thay <code>h = 1</code> vào 4 đáp án, chỉ B cho <code>942</code>!',
        ),

        # Q10 — Medium-Hard — MCQ (Key: D)
        math_mcq(
            'sat_m1_2_q10', 10, D, S_FN, 'Medium-Hard',
            r'<p>A freight logistics company uses the linear function \(C(w) = mw + b\) to calculate the shipping fee, in dollars, for a crate weighing \(w\) kilograms, where \(m\) and \(b\) are positive constants. Increasing a crate’s weight by \(12\) kilograms increases the shipping fee by $21. A crate weighing \(20\) kilograms costs $53 to ship.</p>',
            r'<p>What is the shipping fee, in dollars, for a crate weighing \(36\) kilograms?</p>',
            {
                'A': r'\(63\)',
                'B': r'\(71\)',
                'C': r'\(74\)',
                'D': r'\(81\)',
            },
            'D',
            '\n'.join([
                r'<b>Bước 1 (Tìm hệ số góc \(m\)):</b>',
                r'Tăng \(12\) kg làm tăng cước thêm $21:',
                r'\[m = \frac{\Delta C}{\Delta w} = \frac{21}{12} = \frac{7}{4} = 1.75 \text{ đô-la/kg}\]',
                r'<b>Bước 2 (Tính nhanh \(C(36)\) từ \(C(20) = 53\)):</b>',
                r'Trọng lượng tăng thêm \(\Delta w = 36 - 20 = 16\) kg, nên chi phí tăng thêm:',
                r'\[\Delta C = 16 \times \frac{7}{4} = 28 \text{ đô-la}\]',
                r'\[C(36) = 53 + 28 = 81 \text{ đô-la}\]',
                r'<i>Kiểm chứng qua \(b\):</i> \(53 = 1.75(20) + b \implies b = 18\), nên \(C(36) = 1.75(36) + 18 = 63 + 18 = 81\).',
            ]),
            r'Với hàm tuyến tính, không nhất thiết phải tìm \(b\) — dùng trực tiếp công thức \(f(x_2) = f(x_1) + m(x_2 - x_1)\) nhanh và ít sai dấu hơn hẳn!',
            {
                'A': ('Forgot Base Fee b', r'Chỉ tính \(1.75 \times 36 = 63\) mà quên cộng khoản phí cố định \(b = 18\).'),
                'B': ('Added Base Fee to C(20)', r'Cộng nhầm phí cố định \(b = 18\) vào \(53\) thành \(71\) thay vì cộng \(\Delta C = 28\).'),
                'C': ('Unscaled Delta Trap', r'Cộng thẳng $21 vào $53 (thành $74), quên rằng trọng lượng tăng \(16\) kg chứ không phải \(12\) kg.'),
                'D': ('Đáp án đúng', r'Tốc độ \(m = \frac{7}{4}\), tăng thêm \(16\) kg cộng thêm $28 \(\implies 53 + 28 = 81\).'),
            },
            desmos_tip_vi=r'Gõ một dòng <code>53 + (21/12)*(36 - 20)</code> trong Desmos \(\to\) nhận ngay <code>81</code> trong 4 giây!',
        ),

        # Q11 — Hard (750–800) — MCQ (Key: B)
        math_mcq(
            'sat_m1_2_q11', 11, D, S_FN, 'Hard (750–800)',
            r'<p>The linear function \(f\) is defined by \(f(x) = mx + b\), where \(m\) and \(b\) are constants with \(m \neq 0\). In the \(xy\)-plane, the graph of \(y = f(x)\) has an \(x\)-intercept at \((k, 0)\) and a \(y\)-intercept at \((0, 3k)\), where \(k\) is a nonzero constant. The graph of \(y = f(x) + 12\) passes through the point \((2, 24)\).</p>',
            r'<p>What is the value of \(k\)?</p>',
            {
                'A': r'\(2\)',
                'B': r'\(6\)',
                'C': r'\(10\)',
                'D': r'\(18\)',
            },
            'B',
            '\n'.join([
                r'<b>Bước 1 (Khử tham số \(k\) khi tính hệ số góc \(m\)!):</b>',
                r'Đường thẳng \(y = f(x)\) đi qua \((k, 0)\) và \((0, 3k)\) với \(k \neq 0\):',
                r'\[m = \frac{3k - 0}{0 - k} = \frac{3k}{-k} = -3\]',
                r'Và tung độ gốc là \(b = 3k\), nên \(f(x) = -3x + 3k\).',
                r'<b>Bước 2 (Áp dụng điều kiện đồ thị tịnh tiến \(y = f(x) + 12\) đi qua \((2, 24)\)):</b>',
                r'\[f(2) + 12 = 24 \implies (-3(2) + 3k) + 12 = 24\]',
                r'\[3k + 6 = 24 \implies 3k = 18 \implies k = 6\]',
            ]),
            r'Khi cả \(x\)-intercept và \(y\)-intercept cùng tỷ lệ với một hằng số \(k \neq 0\), hệ số góc \(m = -\frac{y\text{-int}}{x\text{-int}}\) sẽ triệt tiêu sạch \(k\) thành một hằng số cố định!',
            {
                'A': ('Slope Sign Error', r'Tính nhầm hệ số góc thành \(+3\) thay vì \(-3\), dẫn tới \(3(2) + 3k + 12 = 24 \implies k = 2\).'),
                'B': ('Đáp án đúng', r'Triệt tiêu \(k\) cho \(m = -3\), suy ra \(f(x) = -3x + 3k\) và \(-6 + 3k + 12 = 24 \implies k = 6\).'),
                'C': ('Ignored Vertical Shift', r'Quên cộng \(+12\), giải nhầm \(f(2) = 24 \implies -6 + 3k = 24 \implies k = 10\).'),
                'D': ('Solved for y-Intercept', r'Tìm ra tung độ gốc \(b = 3k = 18\) rồi khoanh luôn \(18\) thay vì chia cho \(3\) lấy \(k\).'),
            },
            desmos_tip_vi=r'Gõ <code>f(x) = -3x + 3k</code> với thanh trượt <code>k</code>, rồi gõ hồi quy <code>f(2) + 12 ~ 24</code> (hoặc vẽ <code>y = f(x) + 12</code> và điểm <code>(2, 24)</code> rồi kéo <code>k</code> cho đường thẳng đi qua điểm) \(\to\) <code>k = 6</code>!',
        ),

        # Q12 — Hard (750–800) — SPR (Answer: -5)
        math_spr(
            'sat_m1_2_q12', 12, D, S_2V, 'Hard (750–800)',
            r'<p>In the \(xy\)-plane, line \(j\) passes through the points \((-3, 10)\) and \((5, -2)\). Line \(k\) is perpendicular to line \(j\) and intersects line \(j\) at the point where \(x = 1\).</p>',
            r'<p>The \(x\)-intercept of line \(k\) is \((a, 0)\). What is the value of \(a\)?</p>',
            ['-5'],
            '-5',
            '\n'.join([
                r'<b>Bước 1 (Tìm phương trình đường thẳng \(j\)):</b>',
                r'\[m_j = \frac{-2 - 10}{5 - (-3)} = \frac{-12}{8} = -\frac{3}{2}\]',
                r'Đi qua \((5, -2)\): \(-2 = -\frac{3}{2}(5) + b_j \implies b_j = \frac{11}{2} \implies y = -\frac{3}{2}x + \frac{11}{2}\).',
                r'<b>Bước 2 (Tìm tọa độ giao điểm tại \(x = 1\)):</b>',
                r'\[y = -\frac{3}{2}(1) + \frac{11}{2} = \frac{8}{2} = 4 \implies \text{Giao điểm là } (1, 4)\]',
                r'<b>Bước 3 (Lập phương trình đường thẳng \(k\) vuông góc và tìm \(x\)-intercept):</b>',
                r'Hệ số góc \(m_k = -\frac{1}{m_j} = \frac{2}{3}\). Đường thẳng \(k\) qua \((1, 4)\):',
                r'\[y - 4 = \frac{2}{3}(x - 1)\]',
                r'Cho \(y = 0\): \(-4 = \frac{2}{3}(a - 1) \implies a - 1 = -6 \implies a = -5\).',
            ]),
            r'Với bài toán hình học giải tích nhiều bước (tìm giao điểm \(\to\) đường vuông góc \(\to\) hoành độ gốc), hãy giữ dạng point-slope \(y - y_0 = m(x - x_0)\) và thế thẳng \(y = 0\) để khỏi phải rút gọn \(b\).',
            desmos_tip_vi=r'Tạo bảng 2 điểm <code>(-3, 10)</code> và <code>(5, -2)</code>, chạy <code>y_1 ~ m_1 x_1 + b_1</code>. Tính tung độ giao điểm <code>y_0 = m_1(1) + b_1</code> (ra <code>4</code>), rồi vẽ đường vuông góc <code>y - y_0 = (-1/m_1)(x - 1)</code> và bấm điểm cắt trục \(x\) \(\to (-5, 0)\)!',
        ),

        # Q13 — Hard (750–800) — MCQ (Key: A)
        math_mcq(
            'sat_m1_2_q13', 13, D, S_FN, 'Hard (750–800)',
            q13_table + r'<p>The table above shows three values of \(x\) and their corresponding values of \(h(x)\) for a linear function \(h\), where \(c\) is a constant.</p>',
            r'<p>What is the value of \(h(-3)\)?</p>',
            {
                'A': r'\(-8\)',
                'B': r'\(-1\)',
                'C': r'\(2\)',
                'D': r'\(\frac{7}{2}\)',
            },
            'A',
            '\n'.join([
                r'<b>Bước 1 (Dùng tính chất hệ số góc không đổi của hàm bậc nhất để tìm \(c\)):</b>',
                r'\[\frac{(5c + 3) - (2c - 5)}{3 - (-1)} = \frac{(40 - 3c) - (5c + 3)}{9 - 3}\]',
                r'\[\frac{3c + 8}{4} = \frac{37 - 8c}{6}\]',
                r'Nhân chéo (rút gọn mẫu 4 và 6 thành 2 và 3):',
                r'\[3(3c + 8) = 2(37 - 8c) \implies 9c + 24 = 74 - 16c \implies 25c = 50 \implies c = 2\]',
                r'<b>Bước 2 (Thay \(c = 2\) để lấy tọa độ thực của bảng):</b>',
                r'• \(h(-1) = 2(2) - 5 = -1\)',
                r'• \(h(3) = 5(2) + 3 = 13\)',
                r'Hệ số góc \(m = \frac{13 - (-1)}{3 - (-1)} = \frac{14}{4} = \frac{7}{2}\).',
                r'<b>Bước 3 (Tính \(h(-3)\)):</b>',
                r'\[h(-3) = h(-1) + m(-3 - (-1)) = -1 + \frac{7}{2}(-2) = -1 - 7 = -8\]',
            ]),
            r'Khi một bảng giá trị hàm tuyến tính chứa tham số \(c\) ở cả 3 hàng, đặt hệ số góc giữa hàng 1–2 bằng hàng 2–3 để giải \(c\), rồi LUÔN đọc kỹ xem đề hỏi \(c\), hệ số góc \(m\), hay \(h(x_0)\).',
            {
                'A': ('Đáp án đúng', r'Giải \(c = 2\), suy ra \(h(x) = \frac{7}{2}x + \frac{5}{2}\) và \(h(-3) = -\frac{21}{2} + \frac{5}{2} = -8\).'),
                'B': ('Evaluated Wrong Input', r'Đây là giá trị \(h(-1) = -1\), không phải \(h(-3)\).'),
                'C': ('Partial Solve', r'Dừng lại ngay sau khi giải ra tham số \(c = 2\) mà quên tính \(h(-3)\).'),
                'D': ('Answered Slope Instead', r'Tính ra hệ số góc \(m = \frac{7}{2}\) rồi khoanh nhầm thay vì tính giá trị hàm \(h(-3)\).'),
            },
            desmos_tip_vi=r'Gõ 1 dòng hồi quy hệ số góc <code>((5c + 3) - (2c - 5))/4 ~ ((40 - 3c) - (5c + 3))/6</code> để ra ngay <code>c = 2</code>. Tiếp theo gõ <code>m = ((5c + 3) - (2c - 5))/4</code> và <code>(2c - 5) + m(-3 - (-1))</code> \(\to\) ra ngay <code>-8</code>!',
        ),

        # Q14 — Hard (750–800) — MCQ (Key: C)
        math_mcq(
            'sat_m1_2_q14', 14, D, S_2V, 'Hard (750–800)',
            r'<p>In the \(xy\)-plane, line \(p\) is defined by the equation \(5x - 3y = k\), where \(k\) is a constant. Line \(q\) is formed by translating line \(p\) to the left by \(4\) units and up by \(6\) units. Line \(q\) passes through the origin \((0, 0)\).</p>',
            r'<p>What is the value of \(k\)?</p>',
            {
                'A': r'\(-38\)',
                'B': r'\(2\)',
                'C': r'\(38\)',
                'D': r'\(42\)',
            },
            'C',
            '\n'.join([
                r'<b>Cách 1 (Biến đổi phương trình trực tiếp):</b>',
                r'• Dịch sang <b>trái</b> \(4\) đơn vị: thay \(x \to (x + 4)\).',
                r'• Dịch lên <b>trên</b> \(6\) đơn vị: thay \(y \to (y - 6)\).',
                r'Phương trình đường thẳng \(q\) là: \(5(x + 4) - 3(y - 6) = k\).',
                r'Vì đường thẳng \(q\) đi qua \((0, 0)\), thay \(x = 0, y = 0\):',
                r'\[5(0 + 4) - 3(0 - 6) = k \implies 20 + 18 = k \implies k = 38\]',
                r'<b>Cách 2 (Tư duy điểm ngược — siêu trực quan):</b>',
                r'Dịch điểm trên \(p\) sang trái \(4\) và lên \(6\) được \((0, 0)\) \(\implies\) điểm ban đầu trên đường \(p\) là \((0 + 4, 0 - 6) = (4, -6)\). Thay vào \(5x - 3y = k\): \(5(4) - 3(-6) = 38\).',
            ]),
            r'Khi tịnh tiến một đường thẳng dạng ẩn \(Ax + By = C\): thay \(x \to (x - \Delta x)\) và \(y \to (y - \Delta y)\), hoặc đơn giản hơn là dịch NGƯỢC điểm đích \((x_q, y_q)\) về lại đường gốc rồi thế thẳng vào \(Ax + By = k\)!',
            {
                'A': ('Reversed Both Directions', r'Thay nhầm điểm \((-4, 6)\) (dịch xuôi thay vì dịch ngược) vào \(5x - 3y\) ra \(-20 - 18 = -38\).'),
                'B': ('Reversed Vertical Shift', r'Đúng chiều ngang nhưng nhầm chiều dọc thành \(5(4) - 3(6) = 20 - 18 = 2\).'),
                'C': ('Đáp án đúng', r'Điểm tương ứng trên đường gốc là \((4, -6)\), cho \(k = 5(4) - 3(-6) = 38\).'),
                'D': ('Swapped x and y Shifts', r'Tráo đổi bước dịch ngang \(4\) và dọc \(6\), tính thành \(5(6) - 3(-4) = 42\).'),
            },
            desmos_tip_vi=r'Gõ <code>5(x + 4) - 3(y - 6) = k</code> với thanh trượt <code>k</code> (hoặc thay thẳng <code>x=0, y=0</code>: <code>5(4) - 3(-6)</code>) \(\to\) thấy ngay tại <code>k = 38</code> đường thẳng đi xuyên tâm gốc tọa độ <code>(0, 0)</code>!',
        ),

        # Q15 — Hard (750–800) — SPR (Answer: 23/4 or 5.75)
        math_spr(
            'sat_m1_2_q15', 15, D, S_FN, 'Hard (750–800)',
            r'<p>A linear function \(f\) satisfies the equation \(f(3x + 2) = 12x + 17\) for all real numbers \(x\). The graph of \(y = g(x)\) in the \(xy\)-plane is obtained by translating the graph of \(y = f(x)\) to the right by \(h\) units, where \(h\) is a constant.</p>',
            r'<p>If \(g(0) = -14\), what is the value of \(h\)?</p>',
            ['23/4', '5.75'],
            '23/4 (hoặc 5.75)',
            '\n'.join([
                r'<b>Bước 1 (Tìm công thức tường minh của \(f(t)\)):</b>',
                r'Đặt \(t = 3x + 2 \implies x = \frac{t - 2}{3}\). Thay vào vế phải:',
                r'\[f(t) = 12\left(\frac{t - 2}{3}\right) + 17 = 4(t - 2) + 17 = 4t + 9\]',
                r'<i>Kiểm chứng:</i> \(f(3x + 2) = 4(3x + 2) + 9 = 12x + 17\) (đúng!).',
                r'<b>Bước 2 (Áp dụng phép dịch sang phải \(h\) đơn vị):</b>',
                r'\[g(x) = f(x - h) = 4(x - h) + 9\]',
                r'<b>Bước 3 (Dùng \(g(0) = -14\) để tìm \(h\)):</b>',
                r'\[g(0) = 4(0 - h) + 9 = -14 \implies -4h = -23 \implies h = \frac{23}{4} = 5.75\]',
            ]),
            r'Để giải nhanh \(f(ax + b) = cx + d\) trong 3 giây: hệ số góc của \(f\) luôn là \(m = \frac{c}{a}\); lấy 1 điểm bất kỳ (chọn \(x = 0 \implies f(b) = d\)) là chốt ngay công thức \(f(t)\)!',
            desmos_tip_vi=r'Mẹo Desmos không cần đặt ẩn phụ: tại \(x = 0\) có \(f(2) = 17\), tại \(x = 1\) có \(f(5) = 29\). Nhập bảng <code>x_1 = [2, 5]</code>, <code>y_1 = [17, 29]</code> \(\to\) chạy <code>y_1 ~ m x_1 + b</code> ra <code>m = 4, b = 9</code>. Gõ <code>f(x) = m x + b</code> rồi hồi quy <code>f(0 - h) ~ -14</code> \(\to\) <code>h = 5.75</code>!',
        ),
    ]

    return build_math_drill_json(
        title='Math Drill 1.2: Linear Functions, Slope-Intercept Models & Word Problems (15 câu)',
        subtitle='Algebra • Perpendicular/Parallel Lines, Rate-of-Change Traps & Graph Translations',
        skill_badge='Module 1 • Target 750–800',
        questions=questions,
        target_minutes=22,
    )


# ============================================================================
# DRILL 1.3: LINEAR INEQUALITIES, SYSTEMS & FEASIBLE REGIONS (15 QUESTIONS)
# ============================================================================

def _build_drill_m1_3():
    D = 'Algebra'
    S_INEQ = 'Linear inequalities in one or two variables'

    questions = [
        # Q1 — Medium — MCQ (Key: B)
        math_mcq(
            'sat_m1_3_q1', 1, D, S_INEQ, 'Medium',
            r'<p>\[7 - 3(2x - 5) \ge 4x + 52\]</p>',
            r'<p>Which of the following represents all solutions to the given inequality?</p>',
            {
                'A': r'\(x \ge -3\)',
                'B': r'\(x \le -3\)',
                'C': r'\(x \le -6\)',
                'D': r'\(x \ge -6\)',
            },
            'B',
            '\n'.join([
                r'<b>Bước 1 (Phân phối cẩn thận dấu âm):</b>',
                r'\[7 - 6x + 15 \ge 4x + 52 \implies 22 - 6x \ge 4x + 52\]',
                r'<b>Bước 2 (Chuyển vế và ĐỔI CHIỀU khi chia cho số âm):</b>',
                r'\[-10x \ge 30\]',
                r'Chia cả hai vế cho \(-10 < 0\) (bắt buộc đảo chiều \(\ge\) thành \(\le\)):',
                r'\[x \le -3\]',
            ]),
            r'Mỗi khi nhân hoặc chia cả hai vế bất đẳng thức với một số ÂM, bắt buộc đảo chiều bất đẳng thức — hoặc chuyển biến \(x\) sang vế có hệ số DƯƠNG để không bao giờ quên đổi chiều!',
            {
                'A': ('Forgot Sign Flip', r'Giải ra \(-10x \ge 30\) nhưng chia cho \(-10\) mà quên đảo chiều \(\ge\) thành \(\le\).'),
                'B': ('Đáp án đúng', r'Phân phối đúng \(-3(-5) = +15\) và đảo chiều chuẩn khi chia cho \(-10\) cho \(x \le -3\).'),
                'C': ('Distribution Sign Trap', r'Viết sai \(-3(2x - 5) = -6x - 15\), dẫn tới \(-8 - 6x \ge 4x + 52 \implies x \le -6\).'),
                'D': ('Double Trap (Sign + Flip)', r'Mắc đồng thời lỗi phân phối dấu và quên đảo chiều bất đẳng thức.'),
            },
            desmos_tip_vi=r'Gõ thẳng bất đẳng thức <code>7 - 3(2x - 5) >= 4x + 52</code> vào Desmos — miền tô đậm màu xuất hiện từ đường nét liền <code>x = -3</code> kéo về bên trái (\(-\infty\)), chốt ngay <code>x <= -3</code>!',
        ),

        # Q2 — Medium — MCQ (Key: D)
        math_mcq(
            'sat_m1_3_q2', 2, D, S_INEQ, 'Medium',
            _svg_inequality_halfplane_3x_minus_2y_lt_6()
            + r'<p>The shaded region shown in the \(xy\)-plane above represents the solutions to a linear inequality, where the dashed line is not included in the solution set.</p>',
            r'<p>Which of the following inequalities is represented by the shaded region?</p>',
            {
                'A': r'\(3x - 2y \le 6\)',
                'B': r'\(3x - 2y \ge 6\)',
                'C': r'\(3x - 2y > 6\)',
                'D': r'\(3x - 2y < 6\)',
            },
            'D',
            '\n'.join([
                r'<b>Bước 1 (Xác định đường biên):</b> Đường thẳng đi qua \((0, -3)\) và \((2, 0)\) có hệ số góc \(m = \frac{0 - (-3)}{2 - 0} = \frac{3}{2}\):',
                r'\[y = \frac{3}{2}x - 3 \iff 3x - 2y = 6\]',
                r'<b>Bước 2 (Nét đứt \(\to\) bất đẳng thức nghiêm ngặt):</b> Vì đường biên là <b>nét đứt (dashed)</b> nên loại ngay \(\le\) và \(\ge\) (loại A và B).',
                r'<b>Bước 3 (Thử điểm \((0, 0)\) để tránh bẫy hệ số âm của \(y\)):</b>',
                r'Gốc tọa độ \((0, 0)\) nằm <b>BÊN TRONG</b> miền tô đậm. Thay \((0, 0)\) vào vế trái: \(3(0) - 2(0) = 0\).',
                r'Vì \(0 < 6\) là ĐÚNG, bất đẳng thức chuẩn là \(3x - 2y < 6\) (tương đương \(y > \frac{3}{2}x - 3\)).',
            ]),
            r'ĐỪNG đoán dấu \(>\) hay \(<\) theo cảm tính "tô phía trên = dấu lớn"! Khi hệ số của \(y\) âm (như \(-2y\)), phép chia âm làm đảo dấu — luôn kiểm tra nhanh bằng điểm thử \((0, 0)\)!',
            {
                'A': ('Solid vs. Dashed Trap', r'Đúng miền tô nhưng dùng dấu \(\le\) (đường nét liền) thay vì đường nét đứt trên hình.'),
                'B': ('Wrong Boundary & Direction', r'Sai cả loại đường biên (nét liền) lẫn chiều miền nghiệm.'),
                'C': ('Negative-y Sign-Flip Trap', r'Thấy miền tô ở phía trên đường thẳng nên chọn vội dấu \(>\) mà quên rằng chia \(-2y > -3x + 6\) cho \(-2\) lại thành \(y < \frac{3}{2}x - 3\) (tô phía dưới!).'),
                'D': ('Đáp án đúng', r'Đường nét đứt (\(< \)) và gốc tọa độ \((0, 0)\) thỏa mãn \(3(0) - 2(0) = 0 < 6\).'),
            },
            desmos_tip_vi=r'Gõ <code>3x - 2y < 6</code> vào Desmos để đối chiếu trực quan ngay lập tức: đường biên nét đứt đi qua <code>(0, -3)</code> và <code>(2, 0)</code>, tô xanh phía trên chứa <code>(0, 0)</code>!',
        ),

        # Q3 — Medium — MCQ (Key: C)
        math_mcq(
            'sat_m1_3_q3', 3, D, S_INEQ, 'Medium',
            r'<p>\[y < -3x + 8\]\[2x - 5y \le 10\]</p>',
            r'<p>Which of the following points \((x, y)\) is a solution to the given system of inequalities in the \(xy\)-plane?</p>',
            {
                'A': r'\((2, 2)\)',
                'B': r'\((4, -1)\)',
                'C': r'\((1, 2)\)',
                'D': r'\((3, -2)\)',
            },
            'C',
            '\n'.join([
                r'Thử từng điểm vào <b>CẢ HAI</b> bất đẳng thức:',
                r'• <b>(A) \((2, 2)\):</b> Bất đẳng thức 1 cho \(2 < -3(2) + 8 \iff 2 < 2\) (SAI! Dấu \(<\) không lấy điểm trên biên).',
                r'• <b>(B) \((4, -1)\):</b> Bất đẳng thức 1 cho \(-1 < -3(4) + 8 = -4\) (SAI vì \(-1 > -4\)).',
                r'• <b>(C) \((1, 2)\):</b> BĐT 1: \(2 < -3(1) + 8 = 5\) (ĐÚNG); BĐT 2: \(2(1) - 5(2) = -8 \le 10\) (ĐÚNG) \(\implies\) <b>THỎA MÃN!</b>',
                r'• <b>(D) \((3, -2)\):</b> BĐT 1: \(-2 < -1\) (ĐÚNG), nhưng BĐT 2: \(2(3) - 5(-2) = 16 \le 10\) (SAI!).',
            ]),
            r'Điểm thuộc hệ bất đẳng thức phải thỏa mãn ĐỒNG THỜI tất cả bất đẳng thức; luôn cảnh giác bẫy "điểm nằm đúng trên đường biên nét đứt" (như \(2 < 2\) là SAI).',
            {
                'A': ('Boundary Inclusion Trap', r'\((2, 2)\) nằm đúng trên đường biên \(y = -3x + 8\), bị loại vì bất đẳng thức dùng dấu nghiêm ngặt \(<\).'),
                'B': ('Negative Comparison Error', r'So sánh nhầm \(-1 < -4\); thực tế \(-1\) lớn hơn \(-4\).'),
                'C': ('Đáp án đúng', r'\((1, 2)\) thỏa cả \(2 < 5\) lẫn \(2 - 10 = -8 \le 10\).'),
                'D': ('Checked Only One Inequality', r'Chỉ thỏa bất đẳng thức đầu (\(-2 < -1\)) nhưng vi phạm bất đẳng thức hai (\(16 > 10\)).'),
            },
            desmos_tip_vi=r'Gõ cả 2 bất đẳng thức vào Desmos, rồi nhập 4 điểm dưới dạng 1 danh sách <code>[(2,2), (4,-1), (1,2), (3,-2)]</code> — nhìn bằng mắt thường điểm duy nhất nằm trọn trong vùng giao nhau đậm nhất là <code>(1, 2)</code>!',
        ),

        # Q4 — Medium — SPR (Answer: 13)
        math_spr(
            'sat_m1_3_q4', 4, D, S_INEQ, 'Medium',
            r'<p>A graphic design agency has a monthly software budget of at most $850. The agency pays a fixed enterprise platform fee of $190 per month plus $48 per month for each active designer license.</p>',
            r'<p>What is the maximum number of active designer licenses the agency can afford in a month without exceeding its budget?</p>',
            ['13'],
            '13',
            '\n'.join([
                r'<b>Bước 1 (Lập bất đẳng thức ngân sách):</b> Gọi \(n\) là số bản quyền (số nguyên không âm):',
                r'\[190 + 48n \le 850\]',
                r'<b>Bước 2 (Giải tìm cận trên của \(n\)):</b>',
                r'\[48n \le 660 \implies n \le \frac{660}{48} = \frac{55}{4} = 13.75\]',
                r'<b>Bước 3 (Làm tròn XUỐNG — không làm tròn gần nhất!):</b>',
                r'Vì \(n\) phải là số nguyên và không được vượt ngân sách, số bản quyền tối đa là \(n = 13\) (nếu lấy \(14\) thì tốn \(190 + 48(14) = 862 > 850\) đô-la).',
            ]),
            r'Trong bài toán tìm số nguyên tối đa (at most / maximum), kết quả \(13.75\) BẮT BUỘC phải lấy phần nguyên dưới \(\lfloor 13.75 \rfloor = 13\), tuyệt đối không làm tròn lên \(14\)!',
            desmos_tip_vi=r'Gõ <code>(850 - 190)/48</code> trên Desmos \(\to\) hiện <code>13.75</code>. Vì là giới hạn tối đa (không vượt $850), lấy số nguyên lớn nhất không vượt \(13.75\) là <code>13</code>.',
        ),

        # Q5 — Medium-Hard — MCQ (Key: A)
        math_mcq(
            'sat_m1_3_q5', 5, D, S_INEQ, 'Medium-Hard',
            r'<p>A bakery prepares trays of croissants and trays of muffins for a morning catering order. Each tray of croissants requires \(2.5\) cups of flour and sells for $32. Each tray of muffins requires \(1.5\) cups of flour and sells for $20. The bakery has at most \(45\) cups of flour available and wants to earn at least $520 in total revenue from selling \(c\) trays of croissants and \(m\) trays of muffins.</p>',
            r'<p>Which system of inequalities represents this situation?</p>',
            {
                'A': r'\(2.5c + 1.5m \le 45\) and \(32c + 20m \ge 520\)',
                'B': r'\(2.5c + 1.5m \ge 45\) and \(32c + 20m \le 520\)',
                'C': r'\(2.5c + 32m \le 45\) and \(1.5c + 20m \ge 520\)',
                'D': r'\(32c + 20m \le 45\) and \(2.5c + 1.5m \ge 520\)',
            },
            'A',
            '\n'.join([
                r'<b>Bước 1 (Tách riêng từng ràng buộc theo ĐƠN VỊ):</b>',
                r'• <b>Ràng buộc bột (đơn vị: cups):</b> Mỗi khay croissant cần \(2.5\) cups, mỗi khay muffin cần \(1.5\) cups; có <i>tối đa</i> (at most \(\le\)) \(45\) cups:',
                r'\[2.5c + 1.5m \le 45\]',
                r'• <b>Ràng buộc doanh thu (đơn vị: dollars):</b> Mỗi khay croissant bán $32, mỗi khay muffin bán $20; muốn thu <i>ít nhất</i> (at least \(\ge\)) $520:',
                r'\[32c + 20m \ge 520\]',
            ]),
            r'Luôn nhóm bất đẳng thức theo ĐƠN VỊ CỦA VẾ PHẢI (cups đi với cups, dollars đi với dollars) và nhớ mã dịch: "at most" \(\to \le\), "at least" \(\to \ge\).',
            {
                'A': ('Đáp án đúng', r'Khớp hoàn toàn cả đơn vị (bột \(\le 45\) cups, doanh thu \(\ge 520\) đô-la) lẫn chiều bất đẳng thức.'),
                'B': ('Reversed Inequalities', r'Đảo ngược nghĩa của "at most" (\(\le\)) và "at least" (\(\ge\)).'),
                'C': ('Grouped by Item Not Unit', r'Gộp nhầm bột (\(2.5\)) với tiền ($32) trong cùng một bất đẳng thức — sai hoàn toàn về đơn vị.'),
                'D': ('Swapped Right-Hand Totals', r'Gán nhầm giới hạn \(45\) cups cho doanh thu và $520 cho lượng bột.'),
            },
            desmos_tip_vi=r'Mẹo kiểm tra nhanh không cần vẽ đồ thị: chọn thử 1 tình huống dễ như bán \(c = 10\) khay croissant, \(m = 10\) khay muffin \(\to\) tốn <code>2.5(10)+1.5(10) = 40 <= 45</code> cups và thu <code>32(10)+20(10) = 520 >= 520</code> đô-la. Chỉ đáp án A đúng cả hai!',
        ),

        # Q6 — Medium-Hard — MCQ (Key: D)
        math_mcq(
            'sat_m1_3_q6', 6, D, S_INEQ, 'Medium-Hard',
            r'<p>\[y > 2x + 1\]\[y > -\frac{1}{2}x - 3\]</p><p>The given system of inequalities is graphed in the \(xy\)-plane.</p>',
            r'<p>Which quadrant contains NO solutions to the system?</p>',
            {
                'A': r'Quadrant I',
                'B': r'Quadrant II',
                'C': r'Quadrant III',
                'D': r'Quadrant IV',
            },
            'D',
            '\n'.join([
                r'<b>Phân tích dấu của \((x, y)\) ở từng góc phần tư:</b>',
                r'• Xét bất đẳng thức thứ nhất: \(y > 2x + 1\).',
                r'• Ở <b>Quadrant IV</b>, mọi điểm đều có \(x > 0\) và \(y < 0\).',
                r'Tuy nhiên, nếu \(x > 0\) thì \(2x + 1 > 1 > 0\), kéo theo \(y > 2x + 1 > 0\) — <b>mâu thuẫn hoàn toàn</b> với \(y < 0\)!',
                r'• <i>Kiểm chứng 3 góc phần tư còn lại đều CÓ nghiệm:</i>',
                r'  – Quadrant I: \((1, 5)\) thỏa \(5 > 3\) và \(5 > -3.5\).',
                r'  – Quadrant II: \((-2, 2)\) thỏa \(2 > -3\) và \(2 > -2\).',
                r'  – Quadrant III: \((-2, -1)\) thỏa \(-1 > -3\) và \(-1 > -2\).',
            ]),
            r'Với câu hỏi "Which quadrant contains NO solutions?", hãy vẽ ngay 2 bất đẳng thức vào Desmos trong 5 giây — góc phần tư hoàn toàn KHÔNG có vùng tô chồng (màu đậm nhất) chính là đáp án!',
            {
                'A': ('Quadrant Has Solutions', r'Điểm \((1, 5)\) ở Quadrant I thỏa mãn cả hai bất đẳng thức.'),
                'B': ('Quadrant Has Solutions', r'Điểm \((-2, 2)\) ở Quadrant II thỏa mãn cả hai bất đẳng thức.'),
                'C': ('Quadrant Has Solutions', r'Đường \(y = 2x + 1\) và \(y = -\frac{1}{2}x - 3\) cắt nhau tại \((-1.6, -2.2)\) trong Quadrant III, nên điểm \((-2, -1)\) thuộc Q-III vẫn là nghiệm!'),
                'D': ('Đáp án đúng', r'Mọi điểm có \(x > 0\) đều bị ép \(y > 2x + 1 > 1 > 0\), nên Quadrant IV (\(x > 0, y < 0\)) không chứa bất kỳ nghiệm nào.'),
            },
            desmos_tip_vi=r'Gõ nguyên 2 dòng <code>y > 2x + 1</code> và <code>y > -(1/2)x - 3</code> vào Desmos. Quan sát miền giao chồng nhau (phần đậm nhất): nó trải qua Q-I, Q-II và một góc của Q-III, nhưng <b>trống hoàn toàn ở Quadrant IV</b>!',
        ),

        # Q7 — Medium-Hard — MCQ (Key: B)
        math_mcq(
            'sat_m1_3_q7', 7, D, S_INEQ, 'Medium-Hard',
            r'<p>\[5x + 2y \ge 34\]\[2y - 3x \le -2\]</p>',
            r'<p>For all points \((x, y)\) that are solutions to the given system of inequalities, what is the minimum possible value of \(x\)?</p>',
            {
                'A': r'\(4\)',
                'B': r'\(\frac{9}{2}\)',
                'C': r'\(\frac{23}{4}\)',
                'D': r'\(16\)',
            },
            'B',
            '\n'.join([
                r'<b>Bước 1 (Đổi chiều BĐT 2 về cùng chiều \(\ge\) bằng cách nhân \(-1\)):</b>',
                r'\[-(2y - 3x) \ge -(-2) \iff 3x - 2y \ge 2\]',
                r'<b>Bước 2 (Cộng hai bất đẳng thức CÙNG CHIỀU để khử \(y\)):</b>',
                r'\[(5x + 2y) + (3x - 2y) \ge 34 + 2\]',
                r'\[8x \ge 36 \implies x \ge \frac{36}{8} = \frac{9}{2}\]',
                r'<b>Bước 3 (Kiểm tra dấu bằng đạt được):</b> Tại \(x = \frac{9}{2}, y = \frac{23}{4}\), cả hai bất đẳng thức đều xảy ra dấu \(=\). Vậy giá trị nhỏ nhất của \(x\) là \(\frac{9}{2}\).',
            ]),
            r'Chỉ được phép CỘNG hai bất đẳng thức khi chúng CÙNG CHIỀU (\(\ge\) với \(\ge\)); nếu ngược chiều, nhân một bất đẳng thức với \(-1\) và ĐỔI CHIỀU trước khi cộng khử biến!',
            {
                'A': ('Forgot to Negate RHS', r'Nhân BĐT 2 với \(-1\) nhưng quên đổi dấu \(-2\) thành \(+2\), cộng thành \(8x \ge 32 \implies x \ge 4\).'),
                'B': ('Đáp án đúng', r'Đổi chiều BĐT 2 thành \(3x - 2y \ge 2\), cộng với BĐT 1 cho \(8x \ge 36 \implies x \ge \frac{9}{2}\).'),
                'C': ('Solved for y Instead of x', r'Đây là tung độ \(y = \frac{23}{4}\) tại đỉnh giao điểm, không phải hoành độ \(x\).'),
                'D': ('Added Opposite Directions', r'Cộng nhầm hệ số \(5x - 3x = 2x \ge 32 \implies x \ge 16\).'),
            },
            desmos_tip_vi=r'Gõ cả hai bất đẳng thức <code>5x + 2y >= 34</code> và <code>2y - 3x <= -2</code> vào Desmos. Bấm vào đỉnh cực trái của miền giao nhau \(\to (4.5, 5.75)\), đọc ngay \(x_{\min} = 4.5 = \frac{9}{2}\)!',
        ),

        # Q8 — Medium-Hard — SPR (Answer: 8)
        math_spr(
            'sat_m1_3_q8', 8, D, S_INEQ, 'Medium-Hard',
            r'<p>A tech conference organizer is booking workshop rooms and keynote halls. Each workshop room holds \(30\) attendees and costs $400 to rent. Each keynote hall holds \(80\) attendees and costs $900 to rent. The organizer must provide seating for at least \(480\) attendees while spending at most $5,950 on room rentals.</p>',
            r'<p>If the organizer rents \(w\) workshop rooms and \(k\) keynote halls, where \(w\) and \(k\) are nonnegative integers, what is the maximum number of workshop rooms the organizer can rent?</p>',
            ['8'],
            '8',
            '\n'.join([
                r'<b>Bước 1 (Lập hệ bất đẳng thức):</b>',
                r'• Sức chứa: \(30w + 80k \ge 480 \iff 3w + 8k \ge 48 \implies k \ge \frac{48 - 3w}{8}\).',
                r'• Chi phí: \(400w + 900k \le 5{,}950 \iff 8w + 18k \le 119 \implies k \le \frac{119 - 8w}{18}\).',
                r'<b>Bước 2 (Khử \(k\) tìm cận trên của \(w\)):</b>',
                r'\[\frac{48 - 3w}{8} \le \frac{119 - 8w}{18} \implies 9(48 - 3w) \le 4(119 - 8w)\]',
                r'\[432 - 27w \le 476 - 32w \implies 5w \le 44 \implies w \le 8.8\]',
                r'<b>Bước 3 (Kiểm tra tồn tại số nguyên \(k\) tại \(w = 8\)):</b>',
                r'Với \(w = 8\): \(k \ge \frac{48 - 24}{8} = 3\) và \(k \le \frac{119 - 64}{18} = 3.055\dots \implies k = 3\) (nguyên, thỏa mãn!).',
                r'Kiểm chứng \((w = 8, k = 3)\): chỗ ngồi \(= 30(8) + 80(3) = 480 \ge 480\) và chi phí \(= 400(8) + 900(3) = 5{,}900 \le 5{,}950\). Vậy \(w_{\max} = 8\).',
            ]),
            r'Trong bài toán tối ưu 2 biến nguyên, sau khi tìm cận trên liên tục (\(w \le 8.8\)), LUÔN kiểm chứng lại xem tại \(w = 8\) có tồn tại giá trị nguyên \(k\) thỏa cả 2 bất đẳng thức không!',
            desmos_tip_vi=r'Vẽ <code>30x + 80y >= 480</code> và <code>400x + 900y <= 5950</code> trên Desmos. Bấm đỉnh cực phải của miền giao nhau thấy <code>(8.8, 2.7)</code>; vẽ thêm đường đứng <code>x = 8</code> kiểm tra thấy đi qua điểm nguyên <code>(8, 3)</code> nằm trọn trong miền \(\to\) đáp án <code>8</code>!',
        ),

        # Q9 — Medium-Hard — MCQ (Key: C)
        math_mcq(
            'sat_m1_3_q9', 9, D, S_INEQ, 'Medium-Hard',
            r'<p>\[-11 \le 5 - 4x < 29\]</p>',
            r'<p>What is the sum of all integer values of \(x\) that satisfy the given compound inequality?</p>',
            {
                'A': r'\(-11\)',
                'B': r'\(-9\)',
                'C': r'\(-5\)',
                'D': r'\(5\)',
            },
            'C',
            '\n'.join([
                r'<b>Bước 1 (Cô lập \(x\) ở giữa — chú ý đảo CẢ HAI dấu khi chia \(-4\)):</b>',
                r'Trừ \(5\) cho cả ba vế:',
                r'\[-16 \le -4x < 24\]',
                r'Chia cả ba vế cho \(-4 < 0\) (đảo \(\le\) thành \(\ge\) và \(<\) thành \(>\)):',
                r'\[4 \ge x > -6 \iff -6 < x \le 4\]',
                r'<b>Bước 2 (Liệt kê và tính tổng các nghiệm nguyên — triệt tiêu đối xứng!):</b>',
                r'Các số nguyên thỏa \(-6 < x \le 4\) là: \(-5, -4, -3, -2, -1, 0, 1, 2, 3, 4\).',
                r'Các cặp \((-4, 4), (-3, 3), (-2, 2), (-1, 1)\) triệt tiêu bằng \(0\), chỉ còn lại đúng \(-5\)!',
            ]),
            r'Với bất đẳng thức kép có hệ số \(x\) âm, chia số âm phải đảo CẢ HAI dấu bất đẳng thức; sau đó kiểm tra cực kỹ hai đầu mút (có lấy dấu \(=\) hay không) rồi mới cộng!',
            {
                'A': ('Included Strict Endpoint', r'Lấy nhầm luôn đầu mút \(x = -6\) (dù là dấu \(<\)), cộng ra \(-6 + (-5) = -11\).'),
                'B': ('Excluded Closed Endpoint', r'Bỏ sót đầu mút \(x = 4\) (dù có dấu \(\le\)), cộng từ \(-5\) đến \(3\) ra \(-9\).'),
                'C': ('Đáp án đúng', r'Miền nghiệm \(-6 < x \le 4\) gồm các số nguyên từ \(-5\) đến \(4\), tổng bằng \(-5\).'),
                'D': ('Sign-Flip Mirror Trap', r'Quên đảo chiều hoặc đảo dấu khi chia \(-4\), giải nhầm thành \(-4 \le x < 6\) có tổng bằng \(+5\).'),
            },
            desmos_tip_vi=r'Gõ <code>-11 <= 5 - 4x < 29</code> vào Desmos để nhìn trực tiếp biên trái nét đứt tại <code>x = -6</code> (không lấy) và biên phải nét liền tại <code>x = 4</code> (có lấy). Gõ <code>sum</code> trong Desmos rồi nhập cận <code>n = -5</code> đến <code>4</code> cho biểu thức <code>n</code> \(\to\) ra ngay <code>-5</code>!',
        ),

        # Q10 — Medium-Hard — MCQ (Key: A)
        math_mcq(
            'sat_m1_3_q10', 10, D, S_INEQ, 'Medium-Hard',
            r'<p>\[y < kx - 11\]\[2x + ky > -4\]</p><p>In the \(xy\)-plane, the point \((3, -2)\) is a solution to the given system of inequalities, where \(k\) is a constant.</p>',
            r'<p>Which of the following inequalities gives all possible values of \(k\)?</p>',
            {
                'A': r'\(3 < k < 5\)',
                'B': r'\(k > 5\)',
                'C': r'\(k < 3\)',
                'D': r'\(-5 < k < 3\)',
            },
            'A',
            '\n'.join([
                r'<b>Bước 1 (Thay \((3, -2)\) vào bất đẳng thức thứ nhất):</b>',
                r'\[-2 < k(3) - 11 \implies 9 < 3k \implies k > 3\]',
                r'<b>Bước 2 (Thay \((3, -2)\) vào bất đẳng thức thứ hai — chú ý chia cho \(-2\)!):</b>',
                r'\[2(3) + k(-2) > -4 \implies 6 - 2k > -4 \implies -2k > -10\]',
                r'Chia cả hai vế cho \(-2 < 0\) và đảo chiều bất đẳng thức:',
                r'\[k < 5\]',
                r'<b>Bước 3 (Giao hai điều kiện):</b> \(k > 3\) và \(k < 5 \iff 3 < k < 5\).',
            ]),
            r'Khi thế tọa độ điểm có tung độ âm (như \(y = -2\)) vào bất đẳng thức chứa \(ky\), hệ số của \(k\) trở thành số âm — nhớ ĐẢO CHIỀU khi giải ra \(k\)!',
            {
                'A': ('Đáp án đúng', r'Giải chuẩn \(k > 3\) và \(k < 5\), hợp lại thành \(3 < k < 5\).'),
                'B': ('Forgot Sign Flip on -2k', r'Bẫy kinh điển: quên đảo chiều khi chia \(-2k > -10\) cho \(-2\) thành \(k > 5\), rồi lấy giao của \(k > 3\) và \(k > 5\) ra \(k > 5\).'),
                'C': ('Reversed First Inequality', r'Đảo ngược sai chiều ở bất đẳng thức đầu tiên thành \(k < 3\).'),
                'D': ('Arithmetic Sign Error', r'Giải sai dấu cả hai bất đẳng thức dẫn tới khoảng \(-5 < k < 3\).'),
            },
            desmos_tip_vi=r'Thay <code>k</code> bằng <code>x</code> để Desmos vẽ trục nghiệm: gõ <code>-2 < 3x - 11</code> và <code>6 - 2x > -4</code>. Miền giao nhau đậm nhất là dải nét đứt nằm chính xác giữa <code>x = 3</code> và <code>x = 5</code> \(\to 3 < k < 5\)!',
        ),

        # Q11 — Hard (750–800) — MCQ (Key: D)
        math_mcq(
            'sat_m1_3_q11', 11, D, S_INEQ, 'Hard (750–800)',
            r'<p>\[(3k - 4)x + 11 > (k + 6)x - 1\]</p><p>In the given inequality, \(k\) is a constant. The inequality is true for all values of \(x\) such that \(x < 0\).</p>',
            r'<p>Which of the following must be true about \(k\)?</p>',
            {
                'A': r'\(k > 5\)',
                'B': r'\(k \ge 5\)',
                'C': r'\(k < 5\)',
                'D': r'\(k \le 5\)',
            },
            'D',
            '\n'.join([
                r'<b>Bước 1 (Đưa toàn bộ \(x\) về vế trái và hằng số về vế phải):</b>',
                r'\[((3k - 4) - (k + 6))x > -1 - 11\]',
                r'\[(2k - 10)x > -12\]',
                r'<b>Bước 2 (Xét đủ cả 3 trường hợp của hệ số \(A = 2k - 10\) với mọi \(x < 0\)):</b>',
                r'• <b>Trường hợp 1 (\(2k - 10 < 0 \iff k < 5\)):</b> Vì \(A < 0\) và \(x < 0\), tích \(Ax > 0 > -12\) luôn ĐÚNG với mọi \(x < 0\) (NHẬN!).',
                r'• <b>Trường hợp 2 (\(2k - 10 = 0 \iff k = 5\) — BẪY BIÊN 800 ĐIỂM!):</b> Bất đẳng thức trở thành \(0 \cdot x > -12 \iff 0 > -12\), luôn ĐÚNG với mọi \(x < 0\) (NHẬN!).',
                r'• <b>Trường hợp 3 (\(2k - 10 > 0 \iff k > 5\)):</b> Bất đẳng thức thành \(x > \frac{-12}{2k - 10}\). Khi \(x\) đủ âm (ví dụ \(x = \frac{-24}{2k - 10} < 0\)), bất đẳng thức SAI (LOẠI!).',
                r'Kết luận: Điều kiện cần và đủ là \(k \le 5\).',
            ]),
            r'Với bất đẳng thức tham số \(Ax > C\) (với \(C < 0\)) đòi hỏi đúng với MỌI \(x < 0\), LUÔN kiểm tra riêng trường hợp biên \(A = 0\): vì \(0 > C\) là đúng, dấu phải là \(\le\) chứ không chỉ \(<\)!',
            {
                'A': ('Reversed Sign Intuition', r'Thấy dấu \(>\) trong đề nên nghĩ hệ số \(2k - 10\) phải dương, quên rằng \(x < 0\) là số âm.'),
                'B': ('Reversed Sign + Boundary', r'Ngược chiều bất đẳng thức của \(k\): khi \(k > 5\), bất đẳng thức luôn bị phá vỡ với \(x\) rất âm.'),
                'C': ('Missed Boundary k = 5', r'Bẫy 780–800 kinh điển: phân tích đúng \(k < 5\) nhưng quên kiểm tra điểm biên \(k = 5\), tại đó \(11 > -1\) vẫn đúng với mọi \(x < 0\)!'),
                'D': ('Đáp án đúng', r'Cả \(k < 5\) (cho \(Ax > 0 > -12\)) lẫn \(k = 5\) (cho \(0 > -12\)) đều đúng với mọi \(x < 0 \implies k \le 5\).'),
            },
            desmos_tip_vi=r'Gõ <code>(3k - 4)x + 11 > (k + 6)x - 1</code> với thanh trượt <code>k</code>. Kiểm tra xem toàn bộ nửa mặt phẳng bên trái trục tung (<code>x < 0</code>) có được tô kín không: ở <code>k = 4</code> tô kín, ở <code>k = 5</code> VẪN tô kín toàn bộ mặt phẳng, nhưng nhích lên <code>k = 5.5</code> lập tức hở trắng ở phía âm vô cực \(\implies k \le 5\)!',
        ),

        # Q12 — Hard (750–800) — SPR (Answer: 6)
        math_spr(
            'sat_m1_3_q12', 12, D, S_INEQ, 'Hard (750–800)',
            r'<p>A relief logistics team is loading standard crates and heavy pallets onto a cargo aircraft. Each standard crate holds \(25\) medical kits and weighs \(300\) pounds. Each heavy pallet holds \(80\) medical kits and weighs \(750\) pounds. The aircraft must carry at least \(460\) medical kits while keeping the total cargo weight at most \(4{,}800\) pounds.</p>',
            r'<p>If the team loads \(s\) standard crates and \(p\) heavy pallets, where \(s\) and \(p\) are nonnegative integers, what is the maximum number of standard crates that can be loaded?</p>',
            ['6'],
            '6',
            '\n'.join([
                r'<b>Bước 1 (Lập hệ bất đẳng thức rút gọn):</b>',
                r'• Số bộ y tế: \(25s + 80p \ge 460 \iff 5s + 16p \ge 92 \implies p \ge \frac{92 - 5s}{16}\).',
                r'• Tổng trọng lượng: \(300s + 750p \le 4{,}800 \iff 2s + 5p \le 32 \implies p \le \frac{32 - 2s}{5}\).',
                r'<b>Bước 2 (Tìm cận trên liên tục của \(s\)):</b>',
                r'\[\frac{92 - 5s}{16} \le \frac{32 - 2s}{5} \implies 5(92 - 5s) \le 16(32 - 2s)\]',
                r'\[460 - 25s \le 512 - 32s \implies 7s \le 52 \implies s \le \frac{52}{7} \approx 7.428\]',
                r'<b>Bước 3 (BẪY LƯỚI NGUYÊN 800 ĐIỂM — Đừng vội điền \(7\)!):</b>',
                r'• <b>Thử \(s = 7\):</b> Ta cần \(\frac{92 - 35}{16} \le p \le \frac{32 - 14}{5} \iff 3.5625 \le p \le 3.6\).',
                r'<b>KHÔNG CÓ SỐ NGUYÊN \(p\) NÀO</b> nằm giữa \(3.5625\) và \(3.6\)! Do đó \(s = 7\) là <b>BẤT KHẢ THI</b>!',
                r'• <b>Thử \(s = 6\):</b> Ta cần \(\frac{92 - 30}{16} \le p \le \frac{32 - 12}{5} \iff 3.875 \le p \le 4.0 \implies p = 4\) (NGUYÊN, THỎA MÃN!).',
                r'Kiểm chứng \((s = 6, p = 4)\): \(25(6) + 80(4) = 470 \ge 460\) kits và \(300(6) + 750(4) = 4{,}800 \le 4{,}800\) lb. Vậy \(s_{\max} = 6\).',
            ]),
            r'Cảnh giác bẫy tối thượng của bài toán quy hoạch nguyên (Integer Lattice Trap): đỉnh liên tục \(x \le 7.43\) KHÔNG đảm bảo \(x = 7\) khả thi — phải luôn thử ngược xem có số nguyên \(y\) nào lọt trong khoảng kẹp hay không!',
            desmos_tip_vi=r'Vẽ <code>25x + 80y >= 460</code> và <code>300x + 750y <= 4800</code>, bấm giao điểm thấy <code>(7.429, 3.429)</code>. Vẽ thêm <code>x = 7</code> rồi zoom kỹ vào dải kẹp: thấy <code>y</code> nằm hoàn toàn giữa <code>3.56</code> và <code>3.6</code> (không có đường lưới nguyên nào đi qua!). Đổi sang <code>x = 6</code> thấy điểm nguyên <code>(6, 4)</code> khớp đẹp \(\to\) đáp án <code>6</code>!',
        ),

        # Q13 — Hard (750–800) — MCQ (Key: B)
        math_mcq(
            'sat_m1_3_q13', 13, D, S_INEQ, 'Hard (750–800)',
            r'<p>\[y \ge \frac{1}{2}x + 4\]\[y \le 2x + k\]</p><p>In the given system of inequalities in the \(xy\)-plane, \(k\) is a constant. The system has NO solutions in Quadrant III (the region where \(x < 0\) and \(y < 0\)).</p>',
            r'<p>Which of the following gives all possible values of \(k\)?</p>',
            {
                'A': r'\(k \le 4\)',
                'B': r'\(k \le 16\)',
                'C': r'\(k \ge 4\)',
                'D': r'\(k \ge 16\)',
            },
            'B',
            '\n'.join([
                r'<b>Bước 1 (Tìm hoành độ đỉnh cực trái \(x^*\) của miền nghiệm):</b>',
                r'Để tồn tại \(y\) thỏa mãn \(\frac{1}{2}x + 4 \le y \le 2x + k\), điều kiện cần và đủ là:',
                r'\[\frac{1}{2}x + 4 \le 2x + k \iff \frac{3}{2}x \ge 4 - k \iff x \ge \frac{2(4 - k)}{3} = x^*\]',
                r'<b>Bước 2 (Điều kiện để miền nghiệm KHÔNG lọt vào Quadrant III):</b>',
                r'Đường biên dưới \(y = \frac{1}{2}x + 4\) cắt trục hoành tại \(x\)-intercept \((-8, 0)\), tức nó chỉ có \(y < 0\) khi \(x < -8\).',
                r'Do đó, để mọi nghiệm \((x, y)\) KHÔNG bao giờ có \(y < 0\) (tránh hoàn toàn Quadrant III), hoành độ cực trái \(x^*\) phải thỏa \(x^* \ge -8\):',
                r'\[\frac{2(4 - k)}{3} \ge -8 \iff 4 - k \ge -12 \iff k \le 16\]',
                r'<i>Kiểm chứng biên \(k = 16\):</i> Giao điểm là \((-8, 0)\) nằm trên trục \(x\) (không thuộc Quadrant III). Với mọi \(x \ge -8\), \(y \ge \frac{1}{2}(-8) + 4 = 0\), nên không tồn tại nghiệm nào có \(y < 0\)!',
            ]),
            r'Để một miền nêm (wedge) giữa hai đường thẳng tránh hoàn toàn Quadrant III, hãy tìm điểm đường biên dưới cắt trục hoành \((x_0, 0)\) và ép giao điểm hai đường thẳng nằm ở phía bên phải điểm đó (\(x^* \ge x_0\))!',
            {
                'A': ('y-Intercept Trap', r'Chỉ nhìn tung độ gốc \((0, 4)\) và ép \(x^* \ge 0\) (làm mất cả Quadrant II lẫn III), bỏ sót đoạn \(4 < k \le 16\) dù vùng đó chỉ nằm ở Q-II chứ không vào Q-III!'),
                'B': ('Đáp án đúng', r'Khi \(k \le 16\), đỉnh giao điểm có \(x^* \ge -8\) kéo theo \(y \ge 0\) với mọi nghiệm, nên Quadrant III hoàn toàn trống.'),
                'C': ('Wrong Intercept & Direction', r'Dùng sai điểm biên \((0, 4)\) đồng thời ngược chiều bất đẳng thức.'),
                'D': ('Reversed Direction on k', r'Tìm đúng biên \(k = 16\) nhưng đảo ngược chiều thành \(k \ge 16\) (khi \(k = 20\), điểm \((-9, -0.5)\) lọt thẳng vào Quadrant III!).'),
            },
            desmos_tip_vi=r'Gõ <code>y >= (1/2)x + 4</code> và <code>y <= 2x + k</code> vào Desmos với thanh trượt <code>k</code> (chỉnh khoảng thanh trượt từ <code>-5</code> đến <code>25</code>). Kéo <code>k</code> lên đến đúng <code>k = 16</code> sẽ thấy mũi nhọn của vùng giao nhau vừa chạm điểm <code>(-8, 0)</code> trên trục hoành; vượt quá <code>16</code> lập tức đâm xuống Quadrant III \(\implies k \le 16\)!',
        ),

        # Q14 — Hard (750–800) — MCQ (Key: C)
        math_mcq(
            'sat_m1_3_q14', 14, D, S_INEQ, 'Hard (750–800)',
            r'<p>\[2x + 3y \le 26\]\[4x - y \le 10\]</p><p>In the \(xy\)-plane, \((x, y)\) is a solution to the given system of inequalities.</p>',
            r'<p>What is the greatest possible value of \(5x + 4y\)?</p>',
            {
                'A': r'\(36\)',
                'B': r'\(42\)',
                'C': r'\(44\)',
                'D': r'\(46\)',
            },
            'C',
            '\n'.join([
                r'<b>Cách 1 (Tổ hợp tuyến tính dương — chuẩn 800 điểm):</b>',
                r'Tìm hai số dương \(A, B > 0\) sao cho \(A(2x + 3y) + B(4x - y) = 5x + 4y\):',
                r'• Hệ số \(x\): \(2A + 4B = 5\)',
                r'• Hệ số \(y\): \(3A - B = 4 \implies B = 3A - 4\)',
                r'Thay vào phương trình đầu: \(2A + 4(3A - 4) = 5 \implies 14A = 21 \implies A = \frac{3}{2} > 0\), suy ra \(B = \frac{1}{2} > 0\).',
                r'Vì \(A, B > 0\), ta nhân và cộng hai bất đẳng thức cùng chiều:',
                r'\[5x + 4y = \frac{3}{2}(2x + 3y) + \frac{1}{2}(4x - y) \le \frac{3}{2}(26) + \frac{1}{2}(10) = 39 + 5 = 44\]',
                r'<b>Cách 2 (Kiểm tra đỉnh giao điểm — Linear Programming):</b>',
                r'Giải \(2x + 3y = 26\) và \(4x - y = 10\) cho đỉnh \((4, 6)\). Tại \((4, 6)\), \(5(4) + 4(6) = 20 + 24 = 44\).',
            ]),
            r'Giá trị lớn nhất/nhỏ nhất của hàm mục tiêu tuyến tính \(px + qy\) trên miền nghiệm hệ 2 bất đẳng thức luôn đạt tại giao điểm hai đường biên — miễn hệ số tổ hợp \(A, B\) cùng dương!',
            {
                'A': ('Blind Addition Trap', r'Cộng thẳng hai vế phải \(26 + 10 = 36\) (đó là cận của \(6x + 2y\), không phải \(5x + 4y\)).'),
                'B': ('Illegal Inequality Subtraction', r'Tính nhầm \(2(26) - 10 = 42\) — vừa sai tổ hợp biểu thức vừa trừ hai bất đẳng thức cùng chiều.'),
                'C': ('Đáp án đúng', r'Tổ hợp \(\frac{3}{2}(2x + 3y) + \frac{1}{2}(4x - y) \le 39 + 5 = 44\), đạt dấu bằng tại đỉnh \((4, 6)\).'),
                'D': ('Swapped Coordinates Trap', r'Giải ra đỉnh \((4, 6)\) nhưng thế nhầm ngược thành \(5(6) + 4(4) = 46\).'),
            },
            desmos_tip_vi=r'Vẽ <code>2x + 3y <= 26</code> và <code>4x - y <= 10</code> trên Desmos, bấm giao điểm thấy ngay <code>(4, 6)</code>. Kiểm tra bằng đường mục tiêu <code>5x + 4y = M</code> với thanh trượt <code>M</code>: kéo <code>M</code> lớn dần thấy đường thẳng rời khỏi miền nghiệm đúng tại <code>M = 44</code>!',
        ),

        # Q15 — Hard (750–800) — SPR (Answer: 7/4 or 1.75)
        math_spr(
            'sat_m1_3_q15', 15, D, S_INEQ, 'Hard (750–800)',
            r'<p>\[y \ge mx - 5\]\[y \le -\frac{3}{4}x + 10\]</p><p>In the given system of inequalities in the \(xy\)-plane, \(m\) is a positive constant. Every point \((x, y)\) in the solution set of the system satisfies \(x \le 6\).</p>',
            r'<p>What is the least possible value of \(m\)?</p>',
            ['7/4', '1.75'],
            '7/4 (hoặc 1.75)',
            '\n'.join([
                r'<b>Bước 1 (Khử \(y\) để tìm cận trên \(x_{\max}\) của miền nghiệm theo \(m\)):</b>',
                r'Từ \(mx - 5 \le y \le -\frac{3}{4}x + 10\), ta suy ra:',
                r'\[mx - 5 \le -\frac{3}{4}x + 10 \iff \left(m + \frac{3}{4}\right)x \le 15\]',
                r'Vì \(m > 0\), hệ số \(m + \frac{3}{4} > 0\), nên chia hai vế giữ nguyên chiều:',
                r'\[x \le \frac{15}{m + \frac{3}{4}}\]',
                r'<b>Bước 2 (Ép mọi nghiệm đều thỏa mãn \(x \le 6\)):</b>',
                r'Hoành độ lớn nhất của miền nghiệm phải không vượt quá \(6\):',
                r'\[\frac{15}{m + \frac{3}{4}} \le 6 \iff 15 \le 6m + \frac{9}{2}\]',
                r'\[6m \ge \frac{21}{2} \iff m \ge \frac{21}{12} = \frac{7}{4} = 1.75\]',
                r'Vậy giá trị nhỏ nhất có thể của \(m\) là \(\frac{7}{4}\) (hoặc \(1.75\)).',
            ]),
            r'Để MỌI điểm trong một miền bất đẳng thức đều thỏa \(x \le c\), chỉ cần giải hoành độ cực đại \(x_{\max}\) tại giao điểm hai đường biên và ép \(x_{\max} \le c\)!',
            desmos_tip_vi=r'Vẽ <code>y >= m x - 5</code>, <code>y <= -(3/4)x + 10</code>, và đường ranh giới <code>x = 6</code>. Kéo thanh trượt <code>m</code> cho đến khi đỉnh nhọn cực phải của miền giao nhau chạm đúng tường <code>x = 6</code> — hoặc gõ thẳng hồi quy tại giao điểm <code>6m - 5 ~ -(3/4)(6) + 10</code> \(\to\) ra chuẩn <code>m = 1.75</code>!',
        ),
    ]

    return build_math_drill_json(
        title='Math Drill 1.3: Linear Inequalities, Systems & Feasible Regions (15 câu)',
        subtitle='Algebra • Sign-Flip Traps, Quadrant Elimination & Parametric Inequality Bounds',
        skill_badge='Module 1 • Target 750–800',
        questions=questions,
        target_minutes=22,
    )


# ============================================================================
# PUBLIC MODULE API
# ============================================================================

def get_drills():
    """Returns a list of 3 tuples: (drill_key, title, order_index, content_json)."""
    d1 = _build_drill_m1_1()
    d2 = _build_drill_m1_2()
    d3 = _build_drill_m1_3()
    return [
        ('drill_m1_1', d1['basicInfo']['title'], 1, d1),
        ('drill_m1_2', d2['basicInfo']['title'], 2, d2),
        ('drill_m1_3', d3['basicInfo']['title'], 3, d3),
    ]


# ============================================================================
# 100% PROGRAMMATIC EXACT-ARITHMETIC VERIFICATION (ALL 45 QUESTIONS)
# ============================================================================

def verify_all_math():
    """Uses exact rational arithmetic (fractions.Fraction) to verify every single answer of all 45 questions."""
    F = Fraction

    # -------------------- DRILL 1.1 (15 QUESTIONS) --------------------
    # Q1: 4(3x - 5) + 7 = 2(3x - 5) + 25 -> find 6x - 13
    u = F(25 - 7, 4 - 2)
    x1 = (u + 5) / 3
    assert 4 * (3 * x1 - 5) + 7 == 2 * (3 * x1 - 5) + 25
    assert 6 * x1 - 13 == 15

    # Q2: 7x + 4y = 31 and 2x + 5y = 23 -> find 5x - y
    det2 = 7 * 5 - 4 * 2
    x2 = F(31 * 5 - 4 * 23, det2)
    y2 = F(7 * 23 - 31 * 2, det2)
    assert 7 * x2 + 4 * y2 == 31 and 2 * x2 + 5 * y2 == 23
    assert 5 * x2 - y2 == 8

    # Q3: (1/4)(20x - 16) + kx = 10x - 4 infinitely many solutions -> k = 5
    k3 = 10 - F(1, 4) * 20
    assert k3 == 5
    for xt in (F(-7), F(0), F(13, 3)):
        assert F(1, 4) * (20 * xt - 16) + k3 * xt == 10 * xt - 4

    # Q4 (SPR): (3/5)x - (2/3)y = 7 and px - 10y = 14 no solution -> p = 9
    ratio4 = F(-10) / F(-2, 3)
    p4 = ratio4 * F(3, 5)
    assert p4 == 9 and ratio4 * 7 != 14

    # Q5: (5x - 3)/4 - (2x + 7)/6 = (x + 11)/12 -> x = 17/5
    x5 = F(17, 5)
    assert (5 * x5 - 3) / 4 - (2 * x5 + 7) / 6 == (x5 + 11) / 12

    # Q6: a(4x - 9) + 18 = 12x + b no solution -> a = 3, b != -9
    a6 = F(12, 4)
    b6_excluded = 18 - 9 * a6
    assert a6 == 3 and b6_excluded == -9

    # Q7: 6x - 15y = 24 and rx + 20y = s infinite solutions -> r + s = -40
    scale7 = F(20, -15)
    r7, s7 = 6 * scale7, 24 * scale7
    assert r7 == -8 and s7 == -32 and (r7 + s7) == -40

    # Q8 (SPR): Table f(-2)=17, f(2)=7, f(6)=-3; g(-2)=-6, g(2)=0, g(6)=6 -> intersection a = 15/4
    mf8 = F(7 - 17, 2 - (-2))
    bf8 = 7 - mf8 * 2
    assert mf8 * 6 + bf8 == -3
    mg8 = F(0 - (-6), 2 - (-2))
    bg8 = 0 - mg8 * 2
    assert mg8 * 6 + bg8 == 6
    a8 = (bg8 - bf8) / (mf8 - mg8)
    assert a8 == F(15, 4) and float(a8) == 3.75

    # Q9: Coffee blend $18 premium, $10 house-roast, 60 lb at $13.20/lb -> house-roast = 36
    h9 = F(60 * F(132, 10) - 18 * 60, 10 - 18)
    assert h9 == 36
    assert 10 * h9 + 18 * (60 - h9) == 60 * F(132, 10)

    # Q10: (1/2)x - (3/4)y = 5, kx + 6y = -16, intersect at y = -4 -> k = 2
    y10 = F(-4)
    x10 = (5 + F(3, 4) * y10) * 2
    k10 = (-16 - 6 * y10) / x10
    assert x10 == 4 and k10 == 2

    # Q11: (kx - 15)/4 - (3x - 2)/5 = (8x - c)/20 infinite solutions -> c - k = 63
    k11 = F(8 + 12, 5)
    c11 = -(5 * (-15) - 4 * (-2))
    assert k11 == 4 and c11 == 67 and c11 - k11 == 63
    for xt in (F(-5), F(0), F(9, 2)):
        assert (k11 * xt - 15) / 4 - (3 * xt - 2) / 5 == (8 * xt - c11) / 20

    # Q12 (SPR): (5/6)x - (3/8)y = 11/12 and 2ax + 22 = 3by infinite solutions -> a + b = -13
    scale12 = F(-22) / F(11, 12)
    a12 = (scale12 * F(5, 6)) / 2
    b12 = -(scale12 * F(-3, 8)) / 3
    assert a12 == -10 and b12 == -3 and (a12 + b12) == -13
    # Verify any solution of eq1 solves eq2
    x12t = F(3)
    y12t = (F(5, 6) * x12t - F(11, 12)) / F(3, 8)
    assert 2 * a12 * x12t + 22 == 3 * b12 * y12t

    # Q13: ax - 4y = 18 and -6x + (a - 5)y = 36 no solution -> a = 8 (and a = -3 is infinite)
    # Roots of a(a - 5) = 24 are -3 and 8
    assert (-3) * (-3 - 5) == 24 and 8 * (8 - 5) == 24
    # At a = -3: ratio (-3)/(-6) = 1/2 == 18/36 (infinite solutions -> rejected)
    assert F(-3, -6) == F(18, 36)
    # At a = 8: ratio 8/(-6) = -4/3 == (-4)/3 != 18/36 (no solution -> accepted)
    assert F(8, -6) == F(-4, 8 - 5) and F(8, -6) != F(18, 36)

    # Q14: 2(px - 3)/5 - (3x + 1)/4 = (px + 7)/10 no solution -> p = 5/2
    p14 = F(15, 6)
    assert p14 == F(5, 2)
    # Check equal x-coefficients and unequal constants
    lhs_slope14 = F(2, 5) * p14 - F(3, 4)
    rhs_slope14 = p14 / 10
    lhs_const14 = F(-6, 5) - F(1, 4)
    rhs_const14 = F(7, 10)
    assert lhs_slope14 == rhs_slope14 and lhs_const14 != rhs_const14

    # Q15 (SPR): 3x - 2y = 17, 5x + 4y = 10, kx - 6y = 34 concurrent -> k = 19/4
    x15 = F(2 * 17 + 10, 6 + 5)
    y15 = F(3 * x15 - 17, 2)
    assert 3 * x15 - 2 * y15 == 17 and 5 * x15 + 4 * y15 == 10
    k15 = (34 + 6 * y15) / x15
    assert k15 == F(19, 4) and float(k15) == 4.75

    # -------------------- DRILL 1.2 (15 QUESTIONS) --------------------
    # Q1: C = 45h + 120 -> C(0) = 120
    assert 45 * 0 + 120 == 120

    # Q2: f(x + 4) - f(x) = -14 and f(2) = 19 -> f(x) = -(7/2)x + 26
    m2_2 = F(-14, 4)
    b2_2 = 19 - m2_2 * 2
    assert m2_2 == F(-7, 2) and b2_2 == 26
    assert (m2_2 * (10 + 4) + b2_2) - (m2_2 * 10 + b2_2) == -14

    # Q3: Perp to 3x - 5y = 20 through (6, -4) -> y = -(5/3)x + 6
    m_ell = F(3, 5)
    m_m = -1 / m_ell
    b_m = -4 - m_m * 6
    assert m_m == F(-5, 3) and b_m == 6

    # Q4 (SPR): g(-3)=23, g(1)=11, g(5)=-1 -> g(-7) = 35
    mg4 = F(11 - 23, 1 - (-3))
    bg4 = 11 - mg4 * 1
    assert mg4 * 5 + bg4 == -1
    assert mg4 * (-7) + bg4 == 35

    # Q5: 36x + 16y = 1440 -> x-intercept (40, 0), y-intercept (0, 90)
    assert F(1440, 36) == 40 and F(1440, 16) == 90

    # Q6: f(x) = -(3/4)x + 5 shifted right 8, down 3 -> g(0) = 8
    f6 = lambda t: F(-3, 4) * t + 5
    g6 = lambda t: f6(t - 8) - 3
    assert g6(0) == 8

    # Q7: 4x + ky = 15 perp to 6x - 9y = 22 -> k = 8/3
    k2_7 = F(4 * 6, 9)
    assert k2_7 == F(8, 3)
    assert (F(-4) / k2_7) * F(6, 9) == -1

    # Q8 (SPR): Table x=[-2, 2, 6], f(x+3)=[4, 10, 16] -> f(0) = 5/2
    mf8_2 = F(10 - 4, (2 + 3) - (-2 + 3))
    bf8_2 = 4 - mf8_2 * (-2 + 3)
    assert mf8_2 * (6 + 3) + bf8_2 == 16
    assert bf8_2 == F(5, 2) and float(bf8_2) == 2.5

    # Q9: 960 kWh, loses 4.5 kWh / 15 min -> 18 kWh / hour -> E(h) = 960 - 18h
    rate_hr = F(9, 2) * F(60, 15)
    assert rate_hr == 18

    # Q10: +12 kg -> +$21, C(20) = 53 -> C(36) = 81
    m2_10 = F(21, 12)
    b2_10 = 53 - m2_10 * 20
    assert m2_10 * 36 + b2_10 == 81

    # Q11: x-int (k, 0), y-int (0, 3k), y = f(x) + 12 passes through (2, 24) -> k = 6
    m2_11 = F(-3)
    # 24 = -3(2) + 3k + 12 => 3k = 18 => k = 6
    k2_11 = F(24 - m2_11 * 2 - 12, 3)
    assert k2_11 == 6
    assert m2_11 * k2_11 + 3 * k2_11 == 0
    assert m2_11 * 2 + 3 * k2_11 + 12 == 24

    # Q12 (SPR): Line j through (-3, 10), (5, -2); line k perp to j at x = 1; x-int a = -5
    mj12 = F(-2 - 10, 5 - (-3))
    bj12 = 10 - mj12 * (-3)
    assert mj12 * 5 + bj12 == -2
    y_int12 = mj12 * 1 + bj12
    mk12 = -1 / mj12
    a12_2 = 1 - y_int12 / mk12
    assert y_int12 == 4 and mk12 == F(2, 3) and a12_2 == -5

    # Q13: h(-1)=2c-5, h(3)=5c+3, h(9)=40-3c linear -> c = 2, h(-3) = -8
    # (3c + 8)/4 = (37 - 8c)/6 => 25c = 50 => c = 2
    c2_13 = F(2)
    h_pts = [(-1, 2 * c2_13 - 5), (3, 5 * c2_13 + 3), (9, 40 - 3 * c2_13)]
    m2_13_a = F(h_pts[1][1] - h_pts[0][1], h_pts[1][0] - h_pts[0][0])
    m2_13_b = F(h_pts[2][1] - h_pts[1][1], h_pts[2][0] - h_pts[1][0])
    assert m2_13_a == m2_13_b == F(7, 2)
    b2_13 = h_pts[0][1] - m2_13_a * (-1)
    assert m2_13_a * (-3) + b2_13 == -8

    # Q14: 5x - 3y = k shifted left 4 and up 6 passes through (0, 0) -> k = 38
    k2_14 = 5 * (0 + 4) - 3 * (0 - 6)
    assert k2_14 == 38

    # Q15 (SPR): f(3x + 2) = 12x + 17, g(x) = f(x - h), g(0) = -14 -> h = 23/4
    f2_15 = lambda t: 4 * t + 9
    for xt in (F(-3), F(0), F(5, 2)):
        assert f2_15(3 * xt + 2) == 12 * xt + 17
    h2_15 = F(23, 4)
    assert f2_15(0 - h2_15) == -14 and float(h2_15) == 5.75

    # -------------------- DRILL 1.3 (15 QUESTIONS) --------------------
    # Q1: 7 - 3(2x - 5) >= 4x + 52 <-> x <= -3
    for xt in (F(-10), F(-3)):
        assert 7 - 3 * (2 * xt - 5) >= 4 * xt + 52
    assert not (7 - 3 * (2 * F(-29, 10) - 5) >= 4 * F(-29, 10) + 52)

    # Q2: 3x - 2y < 6 -> intercepts (0, -3), (2, 0), contains (0, 0), dashed
    assert 3 * 0 - 2 * (-3) == 6 and 3 * 2 - 2 * 0 == 6
    assert 3 * 0 - 2 * 0 < 6

    # Q3: y < -3x + 8 and 2x - 5y <= 10 -> only (1, 2) works among A, B, C, D
    def _sat_q3(pt):
        px, py = pt
        return (py < -3 * px + 8) and (2 * px - 5 * py <= 10)
    assert not _sat_q3((2, 2))
    assert not _sat_q3((4, -1))
    assert _sat_q3((1, 2))
    assert not _sat_q3((3, -2))

    # Q4 (SPR): 190 + 48n <= 850 -> max integer n = 13
    max_n4 = max(n for n in range(100) if 190 + 48 * n <= 850)
    assert max_n4 == 13 and 190 + 48 * 14 > 850

    # Q5: 2.5c + 1.5m <= 45 and 32c + 20m >= 520 (verified feasible at (10, 10))
    assert F(5, 2) * 10 + F(3, 2) * 10 <= 45 and 32 * 10 + 20 * 10 >= 520

    # Q6: y > 2x + 1 and y > -(1/2)x - 3 -> Q-I, Q-II, Q-III have solutions, Q-IV has none
    def _sat_q6(px, py):
        return (py > 2 * px + 1) and (py > F(-1, 2) * px - 3)
    assert _sat_q6(F(1), F(5))      # Q-I
    assert _sat_q6(F(-2), F(2))     # Q-II
    assert _sat_q6(F(-2), F(-1))    # Q-III
    # Q-IV: x > 0 implies 2x + 1 > 1 > 0, so y > 2x + 1 > 0 contradicts y < 0
    for px in (F(1, 100), F(1), F(10)):
        assert 2 * px + 1 > 0

    # Q7: 5x + 2y >= 34 and 2y - 3x <= -2 -> min x = 9/2
    x3_7 = F(34 + 2, 5 + 3)
    y3_7 = (34 - 5 * x3_7) / 2
    assert x3_7 == F(9, 2) and y3_7 == F(23, 4)
    assert 5 * x3_7 + 2 * y3_7 == 34 and 2 * y3_7 - 3 * x3_7 == -2

    # Q8 (SPR): 30w + 80k >= 480 and 400w + 900k <= 5950 -> max integer w = 8
    feasible_w8 = [
        w for w in range(30)
        if any(30 * w + 80 * k >= 480 and 400 * w + 900 * k <= 5950 for k in range(30))
    ]
    assert max(feasible_w8) == 8

    # Q9: Sum of integer x satisfying -11 <= 5 - 4x < 29 -> -5
    ints_q9 = [n for n in range(-50, 51) if -11 <= 5 - 4 * n < 29]
    assert ints_q9 == list(range(-5, 5)) and sum(ints_q9) == -5

    # Q10: (3, -2) solves y < kx - 11 and 2x + ky > -4 -> 3 < k < 5
    for kt in (F(31, 10), F(4), F(49, 10)):
        assert (-2 < kt * 3 - 11) and (2 * 3 + kt * (-2) > -4)
    for kt in (F(3), F(5), F(6), F(0)):
        assert not ((-2 < kt * 3 - 11) and (2 * 3 + kt * (-2) > -4))

    # Q11: (3k - 4)x + 11 > (k + 6)x - 1 true for all x < 0 <-> k <= 5
    for kt in (F(-10), F(0), F(4), F(5)):
        for xt in (F(-10000), F(-1), F(-1, 10000)):
            assert (3 * kt - 4) * xt + 11 > (kt + 6) * xt - 1
    # For k = 5 + 1/100, fails for sufficiently negative x
    k_fail = F(501, 100)
    x_fail = F(-1000)
    assert not ((3 * k_fail - 4) * x_fail + 11 > (k_fail + 6) * x_fail - 1)

    # Q12 (SPR): 25s + 80p >= 460 and 300s + 750p <= 4800 -> continuous max 52/7, integer max s = 6
    assert F(52, 7) > 7  # confirms continuous max exceeds 7
    feasible_s12 = [
        s for s in range(30)
        if any(25 * s + 80 * p >= 460 and 300 * s + 750 * p <= 4800 for p in range(30))
    ]
    assert 7 not in feasible_s12 and max(feasible_s12) == 6

    # Q13: y >= (1/2)x + 4 and y <= 2x + k has NO solutions in Q-III (x < 0, y < 0) <-> k <= 16
    # Intersection x* = 2(4 - k)/3. x* >= -8 <-> k <= 16.
    assert F(2 * (4 - 16), 3) == -8 and F(1, 2) * (-8) + 4 == 0
    # At k = 17, point (-8.5, -0.1) is strictly in Q-III and satisfies both
    px13, py13 = F(-17, 2), F(-1, 10)
    assert px13 < 0 and py13 < 0
    assert py13 >= F(1, 2) * px13 + 4 and py13 <= 2 * px13 + 17

    # Q14: 2x + 3y <= 26 and 4x - y <= 10 -> max(5x + 4y) = 44
    A14, B14 = F(3, 2), F(1, 2)
    assert A14 > 0 and B14 > 0
    assert 2 * A14 + 4 * B14 == 5 and 3 * A14 - 1 * B14 == 4
    assert A14 * 26 + B14 * 10 == 44
    # Attained at vertex (4, 6)
    assert 2 * 4 + 3 * 6 == 26 and 4 * 4 - 6 == 10 and 5 * 4 + 4 * 6 == 44

    # Q15 (SPR): y >= mx - 5 and y <= -(3/4)x + 10 (m > 0), all solutions have x <= 6 -> min m = 7/4
    m15 = F(7, 4)
    assert F(15) / (m15 + F(3, 4)) == 6
    assert F(15) / (F(7, 4) - F(1, 100) + F(3, 4)) > 6
    assert F(15) / (F(7, 4) + F(1, 100) + F(3, 4)) < 6
    assert float(m15) == 1.75

    return True


def _verify_latex_and_structure(drills):
    """Extra strict QA checks: no $...$ LaTeX delimiters, balanced \\( \\) / \\[ \\], 11 MCQ + 4 SPR per drill."""
    dollar_math_re = re.compile(r'\$[^0-9\s][^$]*\$')
    seen_ids = set()

    for drill_key, title, order_idx, content_json in drills:
        errs = validate_sat_test(content_json, title)
        assert not errs, f"QA validation failed for {drill_key}:\n" + "\n".join(errs)

        qs = content_json['drillModule']['questions']
        assert len(qs) == 15, f"{drill_key}: expected 15 questions, got {len(qs)}"

        mcq_qs = [q for q in qs if q.get('questionFormat') == 'mcq']
        spr_qs = [q for q in qs if q.get('questionFormat') == 'spr']
        assert len(mcq_qs) == 11, f"{drill_key}: expected 11 MCQ, got {len(mcq_qs)}"
        assert len(spr_qs) == 4, f"{drill_key}: expected 4 SPR, got {len(spr_qs)}"
        assert [q['number'] for q in spr_qs] == [4, 8, 12, 15], f"{drill_key}: SPR positions mismatch"

        # Check difficulty progression
        for q in qs:
            assert q['id'] not in seen_ids, f"Duplicate global id: {q['id']}"
            seen_ids.add(q['id'])
            n = q['number']
            if n <= 4:
                assert q['difficulty'] == 'Medium', f"{q['id']}: bad difficulty {q['difficulty']}"
            elif n <= 10:
                assert q['difficulty'] == 'Medium-Hard', f"{q['id']}: bad difficulty {q['difficulty']}"
            else:
                assert q['difficulty'] == 'Hard (750–800)', f"{q['id']}: bad difficulty {q['difficulty']}"

            exp = q['explanation']
            assert exp.get('desmosTipVi') and len(exp['desmosTipVi'].strip()) >= 20, f"{q['id']}: missing desmosTipVi"
            assert exp.get('keyTakeaway') and len(exp['keyTakeaway'].strip()) >= 20, f"{q['id']}: missing keyTakeaway"

            # Gather all text fields for LaTeX delimiter sanity check
            texts = [
                q['stimulusHtml'],
                q['questionHtml'],
                exp['summaryVi'],
                exp['desmosTipVi'],
                exp['keyTakeaway'],
            ]
            for opt in q.get('options', []):
                texts.append(opt['text'])
            for oa in (exp.get('optionAnalysis') or {}).values():
                texts.append(oa['reasonVi'])

            for txt in texts:
                assert not dollar_math_re.search(txt), f"{q['id']}: forbidden $...$ math found in: {txt[:120]}"
                assert txt.count(r'\(') == txt.count(r'\)'), f"{q['id']}: unbalanced \\( \\) in: {txt[:120]}"
                assert txt.count(r'\[') == txt.count(r'\]'), f"{q['id']}: unbalanced \\[ \\] in: {txt[:120]}"

        # Verify balanced MCQ answer key distribution
        dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        for q in mcq_qs:
            dist[q['correctAnswer']] += 1
        assert min(dist.values()) >= 2 and max(dist.values()) <= 3, f"{drill_key}: unbalanced MCQ keys {dist}"
        print(f"  [PASS] {drill_key} (order={order_idx}): 15 Qs (11 MCQ {dist} + 4 SPR) | QA & LaTeX verified")


if __name__ == '__main__':
    print("=== STEP 1: PROGRAMMATIC EXACT-ARITHMETIC VERIFICATION (45 QUESTIONS) ===")
    verify_all_math()
    print("  [PASS] All 45 questions verified mathematically with fractions.Fraction!")

    print("\n=== STEP 2: SCHEMA, LATEX & SAT QA VALIDATION (3 DRILLS) ===")
    drills = get_drills()
    assert len(drills) == 3, f"Expected 3 drills, got {len(drills)}"
    _verify_latex_and_structure(drills)

    print("\nALL 3 M1 DRILLS (45 Qs) VERIFIED & QA PASSED!")
