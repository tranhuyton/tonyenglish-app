# -*- coding: utf-8 -*-
"""
Upgrade IGCSE Mathematics (0580) Lectures to Official Cambridge 2025-2027 Syllabus:
1. Patch Topic 2 (Algebra and graphs): add Domain & Range + Fractional Power Graphs y = x^(1/2), y = x^(-1/2) + SVG + Worked Examples.
2. Patch Topic 9 (Statistics): add prominent 2025-2027 Syllabus Notice that Box-and-Whisker Plots are REMOVED.
3. Create NEW Flagship Lecture #11 in Module 4:
   'Paper 2 (Non-Calculator) vs Paper 4 (Calculator) — 2025–2027 Strategy & New Syllabus Masterclass'
   with interactive mini-quiz, exact trig SVG triangles, Topic 1–9 Non-Calc vs Calc matrix, and Casio fx-991EX/CW workflow.
4. Populate rich `tutor_context` for ALL 11 lectures of Maths 0580 (with explicit Paper 2 Non-Calc vs Paper 4 Calc guidance).
Idempotent: uses HTML comment markers so re-running never duplicates content.
"""

import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.igcse_maths_pipeline import (
    COURSE_0580_ID,
    load_ids,
    save_ids,
    sb_get,
    sb_patch,
    upsert_lecture_with_page,
)


def replace_or_insert_marker(html, start_marker, end_marker, block_html, anchor_pattern, insert_before=True):
    pattern = re.compile(re.escape(start_marker) + r'[\s\S]*?' + re.escape(end_marker))
    wrapped = f'{start_marker}\n{block_html}\n{end_marker}'
    if pattern.search(html):
        return pattern.sub(lambda _m: wrapped, html, count=1)
    m = re.search(anchor_pattern, html)
    if m:
        pos = m.start() if insert_before else m.end()
        return html[:pos] + '\n' + wrapped + '\n' + html[pos:]
    return html + '\n' + wrapped


T2_NEW_2025_BLOCK = """
<section class="m-section" style="border:2px solid #9333ea;background:linear-gradient(180deg,#faf5ff 0%,#ffffff 100%);border-radius:18px;padding:24px;margin:28px 0;">
  <div style="display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-bottom:14px;">
    <span style="background:#991b1b;color:#fff;font-size:11px;font-weight:900;padding:4px 10px;border-radius:999px;letter-spacing:.4px;">🆕 NEW 2025–2027 SYLLABUS</span>
    <span style="background:#fff1f2;color:#be123c;border:1px solid #fda4af;font-size:11px;font-weight:900;padding:4px 10px;border-radius:999px;">🚫 PAPER 2 NON-CALCULATOR HOTSPOT</span>
  </div>
  <h2 style="font-size:24px;font-weight:900;color:#581c87;margin-bottom:8px;">2.14 Domain &amp; Range + Graphs of Fractional Powers (y = x<sup>1/2</sup> &amp; y = x<sup>−1/2</sup>)</h2>
  <p style="font-size:15px;color:#475569;margin-bottom:16px;">Đây là <b>2 chuyên đề MỚI BẮT BUỘC</b> được Cambridge đưa vào đề thi 0580 Extended từ năm 2025–2027 (rất hay rơi vào <b>Paper 2 Non-Calculator</b> vì hoàn toàn tính chính xác bằng tay!).</p>

  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-bottom:18px;">
    <div style="background:#ffffff;border:1.5px solid #e9d5ff;border-radius:14px;padding:16px;">
      <h3 style="font-size:17px;font-weight:800;color:#6b21a8;margin-bottom:8px;">1. Domain (Tập xác định) &amp; Range (Tập giá trị)</h3>
      <ul style="padding-left:18px;font-size:14.5px;color:#334155;line-height:1.7;">
        <li><b>Domain (Tập đầu vào <i>x</i>):</b> Tập hợp tất cả giá trị <i>x</i> hợp lệ để hàm số <i>f(x)</i> xác định.
          <br/>• Phân thức <code>1 / (x − a)</code> ⇒ <b><i>x ≠ a</i></b> (mẫu số khác 0).
          <br/>• Căn bậc hai <code>√(x − a)</code> ⇒ <b><i>x ≥ a</i></b> (biểu thức trong căn không âm).</li>
        <li><b>Range (Tập đầu ra <i>f(x)</i> hay <i>y</i>):</b> Tập hợp tất cả giá trị <i>f(x)</i> tạo ra từ Domain.
          <br/>• Với parabol <code>f(x) = (x − h)² + k</code> (<i>x ∈ ℝ</i>) ⇒ <b><i>f(x) ≥ k</i></b>.</li>
        <li><b>Quy tắc hoán đổi hàm ngược <i>f<sup>−1</sup></i>:</b><br/>
          <b>Domain(<i>f<sup>−1</sup></i>) = Range(<i>f</i>)</b> &nbsp;và&nbsp; <b>Range(<i>f<sup>−1</sup></i>) = Domain(<i>f</i>)</b>.</li>
      </ul>
    </div>

    <div style="background:#ffffff;border:1.5px solid #e9d5ff;border-radius:14px;padding:16px;">
      <h3 style="font-size:17px;font-weight:800;color:#6b21a8;margin-bottom:8px;">2. Đồ thị lũy thừa phân số <i>y = ax<sup>1/2</sup></i> &amp; <i>y = ax<sup>−1/2</sup></i></h3>
      <ul style="padding-left:18px;font-size:14.5px;color:#334155;line-height:1.7;">
        <li><b><code>y = x<sup>1/2</sup> = √x</code>:</b> Chỉ xác định với <b><i>x ≥ 0</i></b>, đi qua gốc <b>(0, 0)</b>, tăng chậm dần sang phải. Chọn các số chính phương khi vẽ không máy tính: <code>(0,0), (1,1), (4,2), (9,3), (16,4)</code>.</li>
        <li><b><code>y = x<sup>−1/2</sup> = 1/√x</code>:</b> Chỉ xác định với <b><i>x &gt; 0</i></b> (không chạm trục <i>y</i> và trục <i>x</i> — cả hai trục đều là <b>tiệm cận / asymptotes</b>!). Bảng giá trị nhẩm nhanh Paper 2: <code>(1/4, 2), (1, 1), (4, 1/2), (9, 1/3)</code>.</li>
      </ul>
    </div>
  </div>

  <div style="background:#0f172a;border-radius:14px;padding:14px 16px;margin-bottom:18px;">
    <div style="font-size:12px;font-weight:800;color:#38bdf8;letter-spacing:.5px;margin-bottom:8px;">📈 VISUAL COMPARISON — GRAPHS OF y = x¹/² (BLUE) vs y = x⁻¹/² (CORAL)</div>
    <svg viewBox="0 0 680 230" width="100%" style="display:block;max-height:240px;background:#0b1324;border-radius:10px;">
      <!-- Grid -->
      <g stroke="#1e293b" stroke-width="1">
        <line x1="60" y1="20" x2="60" y2="195"/><line x1="120" y1="20" x2="120" y2="195"/><line x1="180" y1="20" x2="180" y2="195"/>
        <line x1="240" y1="20" x2="240" y2="195"/><line x1="300" y1="20" x2="300" y2="195"/><line x1="360" y1="20" x2="360" y2="195"/>
        <line x1="60" y1="55" x2="410" y2="55"/><line x1="60" y1="90" x2="410" y2="90"/><line x1="60" y1="125" x2="410" y2="125"/><line x1="60" y1="160" x2="410" y2="160"/>
      </g>
      <!-- Axes -->
      <line x1="60" y1="195" x2="420" y2="195" stroke="#94a3b8" stroke-width="2"/>
      <line x1="60" y1="15" x2="60" y2="195" stroke="#94a3b8" stroke-width="2"/>
      <text x="424" y="199" fill="#cbd5e1" font-size="12" font-weight="700">x</text>
      <text x="54" y="13" fill="#cbd5e1" font-size="12" font-weight="700">y</text>
      <!-- Ticks: x=1->96, x=4->204, x=9->384 (scale 36px/unit); y=1->155, y=2->115, y=3->75 (scale 40px/unit) -->
      <text x="52" y="210" fill="#94a3b8" font-size="11">0</text>
      <text x="92" y="210" fill="#94a3b8" font-size="11">1</text>
      <text x="200" y="210" fill="#94a3b8" font-size="11">4</text>
      <text x="380" y="210" fill="#94a3b8" font-size="11">9</text>
      <text x="44" y="159" fill="#94a3b8" font-size="11">1</text>
      <text x="44" y="119" fill="#94a3b8" font-size="11">2</text>
      <text x="44" y="79" fill="#94a3b8" font-size="11">3</text>
      <!-- y = x^(1/2): (0,0)->(60,195), (1,1)->(96,155), (2,1.41)->(132,138.4), (4,2)->(204,115), (6,2.45)->(276,97), (9,3)->(384,75) -->
      <path d="M 60 195 Q 72 168, 96 155 T 204 115 T 384 75" fill="none" stroke="#38bdf8" stroke-width="3.2"/>
      <circle cx="60" cy="195" r="4" fill="#38bdf8"/><circle cx="96" cy="155" r="4.5" fill="#fbbf24"/>
      <circle cx="204" cy="115" r="4" fill="#38bdf8"/><circle cx="384" cy="75" r="4" fill="#38bdf8"/>
      <!-- y = x^(-1/2): (0.25,2)->(69,115), (0.5,1.41)->(78,138), (1,1)->(96,155), (4,0.5)->(204,175), (9,0.33)->(384,181.7) -->
      <path d="M 65 45 C 67 98, 72 135, 96 155 C 125 170, 165 173, 204 175 L 384 182" fill="none" stroke="#fb7185" stroke-width="3"/>
      <circle cx="69" cy="115" r="4" fill="#fb7185"/><circle cx="204" cy="175" r="4" fill="#fb7185"/><circle cx="384" cy="182" r="4" fill="#fb7185"/>
      <!-- Legend Panel -->
      <rect x="445" y="20" width="220" height="185" rx="10" fill="#131f38" stroke="#334155"/>
      <text x="460" y="45" fill="#38bdf8" font-size="13" font-weight="800">● y = x¹/² = √x</text>
      <text x="460" y="64" fill="#cbd5e1" font-size="11.5">Domain: x ≥ 0 | Range: y ≥ 0</text>
      <text x="460" y="81" fill="#94a3b8" font-size="11">Points: (0,0), (1,1), (4,2), (9,3)</text>
      <line x1="460" y1="96" x2="650" y2="96" stroke="#334155"/>
      <text x="460" y="118" fill="#fb7185" font-size="13" font-weight="800">● y = x⁻¹/² = 1/√x</text>
      <text x="460" y="137" fill="#cbd5e1" font-size="11.5">Domain: x &gt; 0 | Range: y &gt; 0</text>
      <text x="460" y="154" fill="#94a3b8" font-size="11">Asymptotes: x = 0 and y = 0</text>
      <line x1="460" y1="168" x2="650" y2="168" stroke="#334155"/>
      <text x="460" y="190" fill="#fbbf24" font-size="11.5" font-weight="800">★ Cắt nhau tại đúng điểm (1, 1)!</text>
    </svg>
  </div>

  <div style="background:#ffffff;border:1.5px solid #cbd5e1;border-left:5px solid #7e22ce;border-radius:12px;padding:16px;">
    <div style="font-size:13px;font-weight:900;color:#7e22ce;margin-bottom:6px;">✍️ WORKED EXAMPLE (PAPER 2 NON-CALCULATOR STYLE • [4 marks])</div>
    <p style="font-size:14.5px;color:#0f172a;margin-bottom:8px;"><b>Question:</b> The function <i>f</i> is defined by <i>f(x) = 3x² − 12x + 7</i> for <i>x ∈ ℝ</i>, and <i>g(x) = 4 / (2x − 5)</i>.<br/>
    (a) Find the range of <i>f(x)</i>. [2] &nbsp;&nbsp;(b) State the value of <i>x</i> that must be excluded from the domain of <i>g(x)</i>. [1] &nbsp;&nbsp;(c) Evaluate <i>h(9)</i> where <i>h(x) = 6x<sup>−1/2</sup> + x<sup>1/2</sup></i>. [1]</p>
    <div style="background:#f8fafc;border-radius:8px;padding:12px;font-size:14px;color:#1e293b;line-height:1.7;">
      <b>(a)</b> Hoàn chỉnh bình phương: <i>f(x) = 3(x² − 4x) + 7 = 3[(x − 2)² − 4] + 7 = 3(x − 2)² − 5</i> <b>[M1]</b>.<br/>
      Vì <i>3(x − 2)² ≥ 0</i> nên giá trị nhỏ nhất là −5 ⇒ <b>Range: <i>f(x) ≥ −5</i></b> <b>[A1]</b>.<br/>
      <b>(b)</b> Mẫu số bằng 0 khi <i>2x − 5 = 0</i> ⇒ <b><i>x = 2.5</i></b> (hoặc 5/2) phải loại khỏi Domain <b>[B1]</b>.<br/>
      <b>(c)</b> <i>h(9) = 6 × (1/√9) + √9 = 6 × (1/3) + 3 = 2 + 3 =</i> <b>5</b> <b>[B1]</b>.
    </div>
  </div>
</section>
"""

T9_NEW_2025_BLOCK = """
<div style="background:linear-gradient(135deg,#fffbeb 0%,#fef3c7 100%);border:2px solid #f59e0b;border-radius:16px;padding:18px 22px;margin:18px 0 24px 0;box-shadow:0 6px 16px rgba(245,158,11,0.12);">
  <div style="display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-bottom:8px;">
    <span style="background:#b45309;color:#ffffff;font-size:11px;font-weight:900;padding:4px 10px;border-radius:999px;">📢 CAMBRIDGE 0580 SYLLABUS UPDATE (2025–2027)</span>
    <span style="background:#ecfdf5;color:#065f46;border:1px solid #6ee7b7;font-size:11px;font-weight:900;padding:4px 10px;border-radius:999px;">🧮 CHỦ YẾU THI Ở PAPER 4 (CALCULATOR)</span>
  </div>
  <p style="font-size:15px;color:#78350f;line-height:1.65;margin:0;">
    <b>Lưu ý cực quan trọng cho học sinh thi 2025–2027:</b> Biểu đồ hộp <b>Box-and-Whisker Plots</b> đã chính thức được <b>LOẠI BỎ</b> khỏi chương trình thi Cambridge IGCSE Maths 0580 từ năm 2025. Hãy tập trung tối đa điểm số vào 4 dạng bài trọng tâm của <b>Paper 4 (Calculator)</b>: <b>(1) Histograms</b> (Frequency Density = Frequency ÷ Class Width), <b>(2) Cumulative Frequency</b> (Median, LQ, UQ, IQR, Percentiles), <b>(3) Estimated Mean</b> của bảng ghép nhóm (dùng Midpoint), và <b>(4) Scatter Diagrams &amp; Line of Best Fit</b>!
  </p>
</div>
"""

P2_VS_P4_LECTURE_HTML = """<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  .course-wrapper {
    --th-dark: #7f1d1d;
    --th-main: #b91c1c;
    --th-mid: #dc2626;
    font-family: 'Nunito', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: #ffffff;
    color: #1e293b;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 0 40px 0;
    width: 100%;
    line-height: 1.65;
  }
  .m-lecture-container { width: 100%; max-width: 1000px; padding: 0 14px; }
  .m-hero-banner {
    background: linear-gradient(135deg, #0f172a 0%, #991b1b 55%, #065f46 100%);
    color: #fff; border-radius: 20px; padding: 30px 32px; margin: 16px 0 26px 0;
    box-shadow: 0 16px 34px -8px rgba(15,23,42,.28);
  }
  .m-hero-badges { display:flex; flex-wrap:wrap; gap:8px; margin-bottom:12px; }
  .m-hero-tag { background:rgba(255,255,255,.16); border:1px solid rgba(255,255,255,.3); color:#fff; font-size:11.5px; font-weight:800; padding:4px 11px; border-radius:999px; }
  .m-hero-title { font-size:29px; font-weight:900; line-height:1.25; margin-bottom:8px; color:#fff; }
  .m-hero-vi { font-size:16.5px; font-weight:700; color:rgba(255,255,255,.92); }
  .sec-card { background:#ffffff; border:1.5px solid #e2e8f0; border-radius:18px; padding:24px; margin-bottom:24px; box-shadow:0 4px 14px rgba(15,23,42,.04); }
  .sec-title { font-size:22px; font-weight:900; color:#0f172a; margin-bottom:14px; display:flex; align-items:center; gap:10px; border-bottom:2px solid #f1f5f9; padding-bottom:10px; }
  .grid-2 { display:grid; grid-template-columns:1fr 1fr; gap:18px; }
  .pill-nc { display:inline-block; background:#fff1f2; color:#be123c; border:1px solid #fda4af; font-size:11.5px; font-weight:900; padding:3px 9px; border-radius:999px; }
  .pill-c { display:inline-block; background:#ecfdf5; color:#047857; border:1px solid #6ee7b7; font-size:11.5px; font-weight:900; padding:3px 9px; border-radius:999px; }
  .cmp-table { width:100%; border-collapse:collapse; font-size:14px; margin-top:10px; }
  .cmp-table th { background:#0f172a; color:#fff; padding:11px 12px; text-align:left; font-weight:800; }
  .cmp-table td { padding:10px 12px; border-bottom:1px solid #e2e8f0; vertical-align:top; }
  .cmp-table tr:nth-child(even) { background:#f8fafc; }
  .nc-box { background:#fff1f2; border:1.5px solid #fda4af; border-radius:14px; padding:18px; }
  .c-box { background:#ecfdf5; border:1.5px solid #6ee7b7; border-radius:14px; padding:18px; }
  .trig-table { width:100%; border-collapse:collapse; font-size:14px; text-align:center; margin-top:10px; background:#fff; border-radius:10px; overflow:hidden; }
  .trig-table th { background:#991b1b; color:#fff; padding:9px; font-weight:800; }
  .trig-table td { padding:9px; border:1px solid #fecdd3; font-weight:700; color:#0f172a; }
  .quiz-card { background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:14px; padding:18px; margin-bottom:16px; }
  .quiz-opts { display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:12px 0; }
  .q-opt { display:flex; align-items:center; gap:10px; padding:10px 14px; border-radius:10px; border:1.5px solid #cbd5e1; background:#fff; cursor:pointer; font-size:14px; font-weight:700; text-align:left; transition:.15s; font-family:inherit; }
  .q-opt:hover { border-color:#3b82f6; background:#eff6ff; }
  .q-opt.is-ok { background:#dcfce7 !important; border-color:#16a34a !important; color:#14532d; }
  .q-opt.is-bad { background:#fee2e2 !important; border-color:#dc2626 !important; color:#7f1d1d; }
  .q-fb { display:none; margin-top:10px; padding:12px 14px; border-radius:10px; font-size:13.5px; line-height:1.6; }
  @media (max-width:768px) { .grid-2, .quiz-opts { grid-template-columns:1fr; } .m-hero-title { font-size:23px; } }
</style>

<div class="course-wrapper">
  <div class="m-lecture-container">
    <div class="m-hero-banner">
      <div class="m-hero-badges">
        <span class="m-hero-tag">CAMBRIDGE IGCSE 0580 EXTENDED</span>
        <span class="m-hero-tag">NEW 2025–2027 SYLLABUS</span>
        <span class="m-hero-tag">🚫 PAPER 2 (50%) vs 🧮 PAPER 4 (50%)</span>
      </div>
      <div class="m-hero-title">Paper 2 (Non-Calculator) vs Paper 4 (Calculator) — Chiến lược Săn A* 2025–2027</div>
      <div class="m-hero-vi">Bản đồ phân tách tuyệt đối kỹ năng Không Máy Tính &amp; Có Máy Tính, Bảng Lượng giác chính xác, Casio fx-991EX/CW Workflow &amp; Official Formula Sheet.</div>
    </div>

    <!-- SECTION 1: EXAM BLUEPRINT -->
    <div class="sec-card">
      <div class="sec-title">⚖️ 1. Cấu trúc Đề thi Cambridge 0580 Extended (Từ 2025 trở đi)</div>
      <p style="font-size:15px;color:#475569;margin-bottom:14px;">Thay đổi lớn nhất của lịch sử IGCSE Maths 0580 kể từ năm 2025 là: <b>Paper 2 chính thức CẤM máy tính cầm tay (Non-Calculator)</b> và tỷ trọng tăng từ 35% lên <b>50% tổng điểm (100 điểm / 2 giờ)</b> — ngang bằng hoàn toàn với Paper 4!</p>
      <div class="grid-2">
        <div class="nc-box">
          <div style="font-size:18px;font-weight:900;color:#9f1239;margin-bottom:8px;">🚫 PAPER 2: NON-CALCULATOR</div>
          <ul style="padding-left:18px;font-size:14.5px;color:#4c0519;line-height:1.75;">
            <li><b>Thời gian &amp; Điểm:</b> <b>2 giờ (120 phút)</b> — <b>100 marks</b> (<b>50%</b> tổng điểm).</li>
            <li><b>Quy tắc tuyệt đối:</b> KHÔNG dùng bất kỳ máy tính nào.</li>
            <li><b>Đáp án chuẩn:</b> Giữ dạng <b>chính xác (exact form)</b>: phân số tối giản, căn thức đã trục căn (<code>3√2</code>), số <code>π</code> (<code>12π</code>), số mũ / dạng chuẩn (<code>3.2 × 10⁵</code>).</li>
            <li><b>Vũ khí mới 2025+:</b> Surds &amp; Rationalising, Exact Trig (<code>0°–90°</code>), Domain &amp; Range, đồ thị <code>x<sup>1/2</sup></code> &amp; <code>x<sup>−1/2</sup></code>.</li>
          </ul>
        </div>
        <div class="c-box">
          <div style="font-size:18px;font-weight:900;color:#065f46;margin-bottom:8px;">🧮 PAPER 4: CALCULATOR ALLOWED</div>
          <ul style="padding-left:18px;font-size:14.5px;color:#064e3b;line-height:1.75;">
            <li><b>Thời gian &amp; Điểm:</b> <b>2 giờ (120 phút)</b> — <b>100 marks</b> (<b>50%</b> tổng điểm).</li>
            <li><b>Quy tắc máy tính:</b> Được dùng Casio fx-991EX / fx-991CW / fx-82MS.</li>
            <li><b>Đáp án chuẩn:</b> Làm tròn <b>3 chữ số có nghĩa (3 s.f.)</b>; góc theo độ làm tròn <b>1 chữ số thập phân (1 d.p.)</b>; tiền tệ làm tròn <b>2 d.p.</b></li>
            <li><b>Vũ khí trọng tâm:</b> Lãi kép &amp; tăng trưởng mũ, Định lý Sin/Cos &amp; Hình học 3D, Frustum/Nón/Cầu, Histogram &amp; Cumulative Frequency.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- SECTION 2: TOPIC 1-9 SPLIT MATRIX -->
    <div class="sec-card">
      <div class="sec-title">🗺️ 2. Ma trận Phân tách 9 Chuyên đề: Paper 2 (Non-Calc) vs Paper 4 (Calc)</div>
      <table class="cmp-table">
        <thead>
          <tr>
            <th style="width:18%;">Topic (0580)</th>
            <th style="width:41%;">🚫 Paper 2: Non-Calculator Focus</th>
            <th style="width:41%;">🧮 Paper 4: Calculator Focus</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>1. Number</b></td>
            <td>Surds &amp; Rationalising (<b>NEW</b>), Exact Indices (<code>27<sup>−2/3</sup></code>), Recurring decimals → fraction, Standard Form nhẩm tay, HCF/LCM, Bounds chính xác.</td>
            <td>Compound Interest, Exponential Growth/Decay, Reverse %, Exchange rates + commission, Bounds với số thập phân phức tạp (3 s.f.).</td>
          </tr>
          <tr>
            <td><b>2. Algebra &amp; Graphs</b></td>
            <td><b>Domain &amp; Range (NEW)</b>, đồ thị <b><code>x<sup>1/2</sup>, x<sup>−1/2</sup></code> (NEW)</b>, Completing the square, Algebraic fractions, Composite/Inverse <code>fg(x), f⁻¹(x)</code>, Differentiation đa thức.</td>
            <td>Quadratic Formula (2 d.p.), giải đồ thị tìm giao điểm bằng Table Mode, Kinematics (diện tích hình thang Speed-Time), Variation tỉ lệ nghịch <code>y ∝ 1/√x</code>.</td>
          </tr>
          <tr>
            <td><b>3. Coordinate Geometry</b></td>
            <td>Gradient, Midpoint, Perpendicular bisector (dạng phân số chính xác), độ dài AB để dạng căn thức <code>√52 = 2√13</code>.</td>
            <td>Bài toán kết hợp giao điểm đường thẳng với đường cong, độ dài &amp; diện tích tam giác tọa độ làm tròn 3 s.f.</td>
          </tr>
          <tr>
            <td><b>4. Geometry</b></td>
            <td>Circle Theorems (tìm góc nguyên, chứng minh góc), Polygons nội/ngoại tiếp, Similarity tỷ số cạnh nguyên, Constructions.</td>
            <td>Bài toán kết hợp lượng giác + đa giác + góc phương vị (Bearings) nhiều bước.</td>
          </tr>
          <tr>
            <td><b>5. Mensuration</b></td>
            <td>Diện tích hình quạt (Sector), độ dài cung (Arc), thể tích trụ/nón/cầu để <b>dạng chính xác theo <code>π</code></b> (VD: <code>36π cm³</code>).</td>
            <td>Khối ghép 3D (Nón + Bán cầu), Hình nón cụt (Frustum), Similar Solids (<code>V₁/V₂ = k³</code>), tính bán kính ngược bằng căn bậc ba.</td>
          </tr>
          <tr>
            <td><b>6. Trigonometry</b></td>
            <td><b>Exact Trig Values (NEW):</b> <code>sin/cos/tan</code> của <code>0°, 30°, 45°, 60°, 90°</code> &amp; góc tù <code>120°, 135°, 150°</code>; tam giác đặc biệt; phương trình <code>2 sin x = √3</code>.</td>
            <td>Sine Rule (gồm cả trường hợp góc tù), Cosine Rule tìm cạnh &amp; góc, Bearings đa chặng, <b>3D Trigonometry</b> (góc giữa đường chéo và mặt đáy).</td>
          </tr>
          <tr>
            <td><b>7. Vectors &amp; Transform.</b></td>
            <td>Cộng trừ nhân vectơ cột, tỉ số vectơ hình học, mô tả 4 phép biến hình (Translation, Reflection, Rotation, Enlargement).</td>
            <td>Tính độ dài vectơ <code>|v| = √(x² + y²)</code> làm tròn 3 s.f., góc hướng vectơ.</td>
          </tr>
          <tr>
            <td><b>8. Probability</b></td>
            <td>Sơ đồ cây &amp; Venn với phân số nhỏ (có &amp; không hoàn lại), xác suất điều kiện dạng phân số tối giản.</td>
            <td>Xác suất không hoàn lại lập phương trình bậc hai (VD: tổng số bi <i>n</i>), Conditional Probability nhiều nhánh với xác suất thập phân.</td>
          </tr>
          <tr>
            <td><b>9. Statistics</b></td>
            <td>Mean/Median/Mode/Range tập nhỏ, Stem-and-Leaf, đọc Scatter Diagram. <i>(Box-and-Whisker đã BỎ từ 2025!)</i></td>
            <td><b>Histograms</b> (Frequency Density), <b>Cumulative Frequency</b> (Median, IQR, Percentiles), Estimated Mean từ bảng ghép nhóm.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- SECTION 3: EXACT TRIGONOMETRY SURVIVAL KIT (PAPER 2 NON-CALC) -->
    <div class="sec-card" style="border-color:#fda4af;">
      <div class="sec-title" style="color:#9f1239;">🚫 3. Bộ Công cụ Sinh tồn Paper 2 Non-Calculator (Bắt buộc thuộc lòng!)</div>
      <div class="grid-2" style="align-items:center;">
        <div>
          <p style="font-size:14.5px;color:#334155;margin-bottom:8px;"><b>Quy tắc "Đếm Căn Chia 2" cho bảng sin:</b> viết <code>√0/2, √1/2, √2/2, √3/2, √4/2</code> cho <code>0°, 30°, 45°, 60°, 90°</code> — <code>cos</code> viết ngược lại, còn <code>tan = sin/cos</code>!</p>
          <table class="trig-table">
            <thead>
              <tr><th>θ</th><th>0°</th><th>30°</th><th>45°</th><th>60°</th><th>90°</th></tr>
            </thead>
            <tbody>
              <tr><td><b>sin θ</b></td><td>0</td><td>1/2</td><td>√2 / 2</td><td>√3 / 2</td><td>1</td></tr>
              <tr><td><b>cos θ</b></td><td>1</td><td>√3 / 2</td><td>√2 / 2</td><td>1/2</td><td>0</td></tr>
              <tr><td><b>tan θ</b></td><td>0</td><td>√3 / 3</td><td>1</td><td>√3</td><td>Undefined</td></tr>
            </tbody>
          </table>
          <div style="background:#fff1f2;border-radius:10px;padding:10px 12px;margin-top:10px;font-size:13.5px;color:#881337;">
            <b>Mẹo góc tù (90° &lt; θ &lt; 180°):</b><br/>
            • <code>sin(180° − θ) = +sin θ</code> (VD: <code>sin 120° = √3/2</code>)<br/>
            • <code>cos(180° − θ) = −cos θ</code> (VD: <code>cos 120° = −1/2</code>)<br/>
            • <code>tan(180° − θ) = −tan θ</code> (VD: <code>tan 135° = −1</code>)
          </div>
        </div>
        <div style="background:#0f172a;border-radius:14px;padding:14px;">
          <div style="font-size:11.5px;font-weight:800;color:#fbbf24;margin-bottom:6px;">📐 2 SPECIAL TRIANGLES — NEVER FORGET AN EXACT VALUE!</div>
          <svg viewBox="0 0 420 195" width="100%" style="display:block;background:#0b1324;border-radius:10px;">
            <!-- 30-60-90 triangle (half of equilateral side 2) -->
            <polygon points="35,165 135,165 35,35" fill="rgba(56,189,248,0.12)" stroke="#38bdf8" stroke-width="2.5"/>
            <rect x="35" y="153" width="12" height="12" fill="none" stroke="#38bdf8" stroke-width="1.6"/>
            <text x="80" y="182" fill="#f8fafc" font-size="13" font-weight="800">1</text>
            <text x="12" y="105" fill="#38bdf8" font-size="13" font-weight="800">√3</text>
            <text x="96" y="94" fill="#fbbf24" font-size="13" font-weight="800">2</text>
            <text x="44" y="66" fill="#cbd5e1" font-size="11.5" font-weight="700">30°</text>
            <text x="103" y="158" fill="#cbd5e1" font-size="11.5" font-weight="700">60°</text>
            <text x="35" y="22" fill="#38bdf8" font-size="11.5" font-weight="800">30°–60°–90° Triangle</text>
            <!-- 45-45-90 triangle -->
            <polygon points="240,165 360,165 240,45" fill="rgba(52,211,153,0.12)" stroke="#34d399" stroke-width="2.5"/>
            <rect x="240" y="153" width="12" height="12" fill="none" stroke="#34d399" stroke-width="1.6"/>
            <text x="295" y="182" fill="#f8fafc" font-size="13" font-weight="800">1</text>
            <text x="222" y="110" fill="#f8fafc" font-size="13" font-weight="800">1</text>
            <text x="308" y="98" fill="#fbbf24" font-size="13" font-weight="800">√2</text>
            <text x="249" y="75" fill="#cbd5e1" font-size="11.5" font-weight="700">45°</text>
            <text x="323" y="158" fill="#cbd5e1" font-size="11.5" font-weight="700">45°</text>
            <text x="240" y="22" fill="#34d399" font-size="11.5" font-weight="800">45°–45°–90° Triangle</text>
          </svg>
        </div>
      </div>
    </div>

    <!-- SECTION 4: PAPER 4 CALCULATOR WORKFLOW & OFFICIAL FORMULA SHEET -->
    <div class="sec-card" style="border-color:#6ee7b7;">
      <div class="sec-title" style="color:#065f46;">🧮 4. Quy trình Bấm máy Paper 4 (Casio fx-991EX/CW) &amp; Official Formula List</div>
      <div class="grid-2">
        <div style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:12px;padding:16px;">
          <h3 style="font-size:16px;font-weight:800;color:#065f46;margin-bottom:8px;">⚡ 5 Quy tắc Sống còn trên Paper 4</h3>
          <ol style="padding-left:18px;font-size:14px;color:#334155;line-height:1.75;">
            <li><b>Kiểm tra chữ <code>D</code> (Degree)</b> ở góc trên màn hình trước khi bấm <code>sin/cos/tan</code> — nếu là <code>R</code> sẽ sai sạch toàn bộ bài hình!</li>
            <li><b>KHÔNG bao giờ làm tròn bước trung gian:</b> Dùng phím <code>Ans</code> hoặc lưu biến <code>STO A</code>; giữ tối thiểu 5 s.f. khi ghi nháp rồi chỉ làm tròn <b>3 s.f.</b> (hoặc góc <b>1 d.p.</b>) ở dòng cuối cùng!</li>
            <li><b>Kiểm tra nghiệm phương trình bậc 2/hệ 2 ẩn:</b> Dùng chế độ <code>Equation / Polynomial</code> để kiểm tra lại kết quả viết tay (vẫn phải viết rõ công thức bậc hai để ăn điểm <b>[M1]</b>!).</li>
            <li><b>Vẽ đồ thị chính xác tuyệt đối:</b> Dùng <code>Table Mode</code> nhập <code>f(x)</code>, đặt Start/End/Step để chép bảng tọa độ không sai dấu âm.</li>
            <li><b>Dấu hiệu bài 3D &amp; Frustum:</b> Vẽ tách tam giác vuông 2D ra bên lề, đánh dấu góc vuông rồi mới áp dụng Pythagoras / SOHCAHTOA / Cosine Rule.</li>
          </ol>
        </div>
        <div style="background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:16px;">
          <h3 style="font-size:16px;font-weight:800;color:#1e3a8a;margin-bottom:8px;">📐 Formula Sheet 2025–2027 (In sẵn trang 2 đề thi!)</h3>
          <p style="font-size:13.5px;color:#1e40af;margin-bottom:8px;"><b>✅ ĐƯỢC IN SẴN TRÊN ĐỀ (0580 Extended):</b></p>
          <ul style="padding-left:18px;font-size:13.5px;color:#1e293b;line-height:1.65;margin-bottom:10px;">
            <li>Area of Trapezium: <code>½(a + b)h</code></li>
            <li>Cone CSA = <code>πrl</code> &nbsp;|&nbsp; Cone Vol = <code>⅓πr²h</code> &nbsp;|&nbsp; Pyramid Vol = <code>⅓Ah</code></li>
            <li>Sphere SA = <code>4πr²</code> &nbsp;|&nbsp; Sphere Vol = <code>⁴⁄₃πr³</code></li>
            <li>Quadratic Formula, Sine Rule, Cosine Rule, Area <code>½ab sin C</code>.</li>
          </ul>
          <p style="font-size:13.5px;color:#be123c;margin-bottom:4px;"><b>❌ KHÔNG IN SẴN — PHẢI THUỘC:</b></p>
          <p style="font-size:13.5px;color:#475569;">Circle Area/Circumference (<code>πr², 2πr</code>), Sector/Arc (<code>θ/360</code>), Pythagoras, Gradient/Midpoint/Distance, Compound Interest <code>P(1 + r/100)ⁿ</code>, Frequency Density = <code>Freq / Class Width</code>, Exact Trig Table!</p>
        </div>
      </div>
    </div>

    <!-- SECTION 5: INTERACTIVE MINI-QUIZ (3 NON-CALC + 3 CALC) -->
    <div class="sec-card" id="p2p4_quiz">
      <div class="sec-title">🎯 5. Kiểm tra nhanh: 3 Câu Paper 2 Non-Calc + 3 Câu Paper 4 Calc</div>

      <div class="quiz-card">
        <div style="margin-bottom:6px;"><span class="pill-nc">🚫 PAPER 2 NON-CALC</span> <b>Câu 1:</b> Simplify <code>12 / (√5 − 1)</code> in exact form.</div>
        <div class="quiz-opts">
          <button type="button" class="q-opt" data-ok="0">A. 3√5 − 3</button>
          <button type="button" class="q-opt" data-ok="1">B. 3√5 + 3</button>
          <button type="button" class="q-opt" data-ok="0">C. 4√5 + 4</button>
          <button type="button" class="q-opt" data-ok="0">D. 6√5 + 6</button>
        </div>
        <div class="q-fb"><b>[M1]</b> Nhân cả tử và mẫu với biểu thức liên hợp <code>(√5 + 1)</code>: mẫu số = <code>(√5)² − 1² = 5 − 1 = 4</code>. <b>[A1]</b> <code>12(√5 + 1)/4 = 3(√5 + 1) = 3√5 + 3</code>.</div>
      </div>

      <div class="quiz-card">
        <div style="margin-bottom:6px;"><span class="pill-nc">🚫 PAPER 2 NON-CALC</span> <b>Câu 2:</b> Find the exact value of <code>4 sin 60° × cos 30° − tan 45°</code>.</div>
        <div class="quiz-opts">
          <button type="button" class="q-opt" data-ok="0">A. 1</button>
          <button type="button" class="q-opt" data-ok="0">B. 3/2</button>
          <button type="button" class="q-opt" data-ok="1">C. 2</button>
          <button type="button" class="q-opt" data-ok="0">D. 3</button>
        </div>
        <div class="q-fb"><b>[M1]</b> Thay <code>sin 60° = √3/2</code>, <code>cos 30° = √3/2</code>, <code>tan 45° = 1</code>: <code>4 × (√3/2) × (√3/2) − 1 = 4 × (3/4) − 1</code>. <b>[A1]</b> <code>3 − 1 = 2</code>.</div>
      </div>

      <div class="quiz-card">
        <div style="margin-bottom:6px;"><span class="pill-nc">🚫 PAPER 2 NON-CALC • NEW 2025</span> <b>Câu 3:</b> Given <code>f(x) = 8x<sup>−1/2</sup></code> for <code>x &gt; 0</code>, find the exact value of <code>f(16)</code> and state the range of <code>f</code>.</div>
        <div class="quiz-opts">
          <button type="button" class="q-opt" data-ok="1">A. f(16) = 2; Range: f(x) &gt; 0</button>
          <button type="button" class="q-opt" data-ok="0">B. f(16) = 32; Range: f(x) ≥ 0</button>
          <button type="button" class="q-opt" data-ok="0">C. f(16) = 1/2; Range: f(x) &gt; 0</button>
          <button type="button" class="q-opt" data-ok="0">D. f(16) = 2; Range: f(x) ≥ 0</button>
        </div>
        <div class="q-fb"><b>[B1]</b> <code>f(16) = 8 / √16 = 8 / 4 = 2</code>. <b>[B1]</b> Vì <code>x &gt; 0</code> nên <code>8/√x</code> luôn dương ngặt (tiệm cận <code>y = 0</code> không bao giờ chạm 0) ⇒ <b>Range: <code>f(x) &gt; 0</code></b>!</div>
      </div>

      <div class="quiz-card">
        <div style="margin-bottom:6px;"><span class="pill-c">🧮 PAPER 4 CALC</span> <b>Câu 4:</b> £2400 is invested at 3.5% per year compound interest. Find the value after 6 years to the nearest pound.</div>
        <div class="quiz-opts">
          <button type="button" class="q-opt" data-ok="0">A. £2904</button>
          <button type="button" class="q-opt" data-ok="1">B. £2950</button>
          <button type="button" class="q-opt" data-ok="0">C. £2985</button>
          <button type="button" class="q-opt" data-ok="0">D. £3012</button>
        </div>
        <div class="q-fb"><b>[M1]</b> <code>A = 2400 × (1.035)⁶ = 2400 × 1.229255... = 2950.21...</code>. <b>[A1]</b> Làm tròn đến bảng gần nhất: <b>£2950</b>.</div>
      </div>

      <div class="quiz-card">
        <div style="margin-bottom:6px;"><span class="pill-c">🧮 PAPER 4 CALC</span> <b>Câu 5:</b> Two mathematically similar cones have volumes <code>54 cm³</code> and <code>250 cm³</code>. If the smaller cone has surface area <code>72 cm²</code>, find the surface area of the larger cone.</div>
        <div class="quiz-opts">
          <button type="button" class="q-opt" data-ok="0">A. 120 cm²</button>
          <button type="button" class="q-opt" data-ok="0">B. 180 cm²</button>
          <button type="button" class="q-opt" data-ok="1">C. 200 cm²</button>
          <button type="button" class="q-opt" data-ok="0">D. 333 cm²</button>
        </div>
        <div class="q-fb"><b>[M1]</b> Tỉ số thể tích <code>k³ = 250/54 = 125/27</code> ⇒ tỉ số cạnh <code>k = ∛(125/27) = 5/3</code>. <b>[M1 A1]</b> Tỉ số diện tích <code>k² = 25/9</code> ⇒ <code>SA = 72 × (25/9) = 8 × 25 = 200 cm²</code>.</div>
      </div>

      <div class="quiz-card">
        <div style="margin-bottom:6px;"><span class="pill-c">🧮 PAPER 4 CALC</span> <b>Câu 6:</b> In a histogram, the class <code>20 ≤ t &lt; 35</code> has a frequency density of <code>2.4</code>. What is the frequency of this class?</div>
        <div class="quiz-opts">
          <button type="button" class="q-opt" data-ok="0">A. 18</button>
          <button type="button" class="q-opt" data-ok="0">B. 24</button>
          <button type="button" class="q-opt" data-ok="0">C. 30</button>
          <button type="button" class="q-opt" data-ok="1">D. 36</button>
        </div>
        <div class="q-fb"><b>[M1]</b> Class Width = <code>35 − 20 = 15</code>. Công thức: <code>Frequency = Frequency Density × Class Width = 2.4 × 15</code>. <b>[A1]</b> <b>36</b>.</div>
      </div>
    </div>
  </div>
</div>

<script>
(function(){
  document.querySelectorAll('#p2p4_quiz .quiz-card').forEach(function(card){
    var fb = card.querySelector('.q-fb');
    card.querySelectorAll('.q-opt').forEach(function(btn){
      btn.addEventListener('click', function(){
        card.querySelectorAll('.q-opt').forEach(function(b){ b.classList.remove('is-ok','is-bad'); });
        var ok = btn.getAttribute('data-ok') === '1';
        btn.classList.add(ok ? 'is-ok' : 'is-bad');
        if (fb) {
          fb.style.display = 'block';
          fb.style.background = ok ? '#f0fdf4' : '#fff1f2';
          fb.style.border = ok ? '1px solid #86efac' : '1px solid #fda4af';
          fb.style.color = ok ? '#14532d' : '#881337';
        }
      });
    });
  });
})();
</script>
"""

TUTOR_CONTEXT_0580 = {
    't1': 'Cambridge IGCSE Maths 0580 (2025-2027) Topic 1: Number. PAPER 2 NON-CALCULATOR focus: Surds & rationalising denominators (NEW 2025), exact fractional/negative indices, recurring decimals to fractions, standard form arithmetic by hand, prime factorisation HCF/LCM, exact upper/lower bounds. PAPER 4 CALCULATOR focus: compound interest, exponential growth/decay, reverse percentages, currency exchange & commission, 3 s.f. bounds.',
    't2': 'Cambridge IGCSE Maths 0580 (2025-2027) Topic 2: Algebra and graphs. Includes NEW 2025 syllabus topics: Domain & Range of functions and graphs of fractional powers y = x^(1/2) & y = x^(-1/2) (heavily tested on Paper 2 Non-Calculator!). Also covers completing the square, algebraic fractions, composite/inverse functions, differentiation (dy/dx, stationary points), quadratic formula (Paper 4), kinematics speed-time graphs, direct/inverse proportion.',
    't3': 'Cambridge IGCSE Maths 0580 (2025-2027) Topic 3: Coordinate geometry. Paper 2 Non-Calc: exact gradient, midpoint, perpendicular bisector equations, exact surd distance AB. Paper 4 Calc: intersections, geometric polygons on axes to 3 s.f.',
    't4': 'Cambridge IGCSE Maths 0580 (2025-2027) Topic 4: Geometry. Circle theorems with exact geometric reasoning (Paper 2 Non-Calc), polygon interior/exterior angles, parallel lines, congruence & similarity, constructions & scale drawings.',
    't5': 'Cambridge IGCSE Maths 0580 (2025-2027) Topic 5: Mensuration. Paper 2 Non-Calc: exact sector area, arc length, cylinder/cone/sphere volumes in terms of pi. Paper 4 Calc: composite 3D solids (cone+hemisphere), frustums, similar solids (A1/A2 = k^2, V1/V2 = k^3). Note: Cone/Sphere/Pyramid/Trapezium formulas are printed on page 2 of the 2025-2027 exam paper.',
    't6': 'Cambridge IGCSE Maths 0580 (2025-2027) Topic 6: Trigonometry. CRITICAL 2025 SPLIT — Paper 2 Non-Calc: EXACT trig values of 0°, 30°, 45°, 60°, 90° and obtuse angles 120°, 135°, 150°, special triangles, exact trig equations. Paper 4 Calc: Sine Rule (incl. ambiguous case), Cosine Rule, area 1/2 ab sin C, bearings, 3D trigonometry (line-to-plane angle, always check Casio is in Degree mode D!).',
    't7': 'Cambridge IGCSE Maths 0580 (2025-2027) Topic 7: Vectors and transformations. Column vectors, vector magnitude, geometric vector proofs & ratios, and full description of 4 transformations (Translation vector, Reflection mirror line, Rotation centre/angle/direction, Enlargement centre/scale factor incl. negative & fractional).',
    't8': 'Cambridge IGCSE Maths 0580 (2025-2027) Topic 8: Probability. Combined events, tree diagrams with & without replacement, Venn diagrams & set notation, conditional probability P(A|B). Paper 2 uses exact simplified fractions; Paper 4 includes algebraic quadratic probability equations.',
    't9': 'Cambridge IGCSE Maths 0580 (2025-2027) Topic 9: Statistics. IMPORTANT 2025-2027 UPDATE: Box-and-Whisker Plots were REMOVED from the 2025 syllabus! Paper 4 Calculator focus: Histograms (Frequency Density = Freq / Class Width), Cumulative Frequency curves (Median, LQ, UQ, IQR, percentiles), Estimated Mean of grouped data, Scatter Diagrams & correlation.',
    'rev': 'Cambridge IGCSE Maths 0580 (2025-2027) Year End Revision. Full bilingual synthesis of all 9 Extended topics, exam technique, official 2025-2027 formula sheet, Paper 2 Non-Calculator (50%, 100 marks) vs Paper 4 Calculator (50%, 100 marks) mastery.',
    'p2p4': 'Cambridge IGCSE Maths 0580 (2025-2027) Flagship Strategy Masterclass: Paper 2 (Non-Calculator, 2h, 100 marks, 50%) vs Paper 4 (Calculator, 2h, 100 marks, 50%). Covers exact Topic 1-9 Non-Calc vs Calc separation, exact trig table & special triangles, surds/rationalising, Domain & Range, x^(±1/2) graphs, Casio fx-991EX/CW Paper 4 workflow, and official 2025-2027 formula sheet.',
}


def main():
    ids = load_ids()
    m0580 = ids['m0580']
    print("=== UPGRADING IGCSE MATHS 0580 LECTURES (2025-2027) ===", flush=True)

    # 1. Patch Topic 2 (Algebra and graphs)
    t2_id = m0580['lectures']['t2']
    pages_t2 = sb_get(f'lecture_pages?lecture_id=eq.{t2_id}&order=page_number.asc&select=id,content_html')
    t2_html = pages_t2[0]['content_html']
    t2_new = replace_or_insert_marker(
        t2_html,
        '<!-- TONY_2025_0580_T2_START -->',
        '<!-- TONY_2025_0580_T2_END -->',
        T2_NEW_2025_BLOCK,
        r'<section[^>]*class="[^"]*m-practice-zone',
        insert_before=True,
    )
    sb_patch(f'lecture_pages?id=eq.{pages_t2[0]["id"]}', {'content_html': t2_new})
    print(f"  [PATCHED] Topic 2: Algebra and graphs (+Domain/Range + x^(±1/2) SVG, {len(t2_new)} chars)", flush=True)

    # 2. Patch Topic 9 (Statistics)
    t9_id = m0580['lectures']['t9']
    pages_t9 = sb_get(f'lecture_pages?lecture_id=eq.{t9_id}&order=page_number.asc&select=id,content_html')
    t9_html = pages_t9[0]['content_html']
    t9_new = replace_or_insert_marker(
        t9_html,
        '<!-- TONY_2025_0580_T9_START -->',
        '<!-- TONY_2025_0580_T9_END -->',
        T9_NEW_2025_BLOCK,
        r'class="m-hero-banner"[\s\S]*?</div>\s*</div>',
        insert_before=False,
    )
    sb_patch(f'lecture_pages?id=eq.{pages_t9[0]["id"]}', {'content_html': t9_new})
    print(f"  [PATCHED] Topic 9: Statistics (+2025-2027 Box-and-Whisker Removal Notice, {len(t9_new)} chars)", flush=True)

    # 3. Create NEW Flagship Lecture #11 in Module 4
    p2p4_id = upsert_lecture_with_page(
        course_id=COURSE_0580_ID,
        module_id=m0580['modules']['m4'],
        title='Paper 2 (Non-Calculator) vs Paper 4 (Calculator) — 2025–2027 Strategy & New Syllabus Masterclass',
        order_index=2,
        content_html=P2_VS_P4_LECTURE_HTML,
        tutor_context=TUTOR_CONTEXT_0580['p2p4'],
        existing_lecture_id=m0580['lectures'].get('p2p4'),
    )
    m0580['lectures']['p2p4'] = p2p4_id
    save_ids(ids)

    # 4. Populate tutor_context across ALL 11 lectures of 0580
    for key, lid in m0580['lectures'].items():
        ctx = TUTOR_CONTEXT_0580.get(key)
        if ctx:
            sb_patch(f'lectures?id=eq.{lid}', {'tutor_context': ctx})
    print(f"  [OK] Updated tutor_context on all {len(m0580['lectures'])} lectures of Maths 0580!", flush=True)
    print("\n[DONE] IGCSE Maths 0580 lectures upgraded successfully!", flush=True)


if __name__ == '__main__':
    main()
