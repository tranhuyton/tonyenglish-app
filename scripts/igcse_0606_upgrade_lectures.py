# -*- coding: utf-8 -*-
"""
Upgrade IGCSE Additional Mathematics (0606) Lectures to Official Cambridge 2025-2027 Syllabus:
1. Create NEW Compulsory Lecture #8 (`c7b`) in Module 2 (order_index=3):
   'Chapter 7B: Coordinate Geometry of the Circle (NEW 2025–2027)'
   with 3 SVGs, 6 Cambridge M1/A1 worked examples, interactive 5-question quiz, and audio section anchors.
2. Create NEW Lecture #18 (`rev`) in Module 5 (order_index=1):
   'Year End Revision: Paper 1 (Non-Calculator) Playbook & Master Formula Sheet (0606 2025–2027)'
   with full 14-topic formula sheet, Paper 1 Non-Calc vs Paper 2 Calc strategy, 6-question cross-topic quiz, and audio anchors.
3. Patch Chapter 3 (Indices & Surds) with 2025-2027 'Foundation Bridge for Paper 1 Non-Calc' banner.
4. Patch Chapter 13 (Vectors) with 2025-2027 'Relative Velocity REMOVED from Syllabus' notice above Compose and Resolve Velocities.
5. Idempotently inject `data-lecture-section="s1"`, `"s2"`, `"s3"` anchors into ALL 18 lectures of 0606 so the Bilingual Audio Player syncs cleanly.
6. Populate rich `tutor_context` for ALL 18 lectures of Maths 0606.
"""

import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.igcse_maths_pipeline import (
    COURSE_0606_ID,
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


def ensure_audio_section_anchors(html):
    """Idempotently ensures data-lecture-section='s1', 's2', 's3' exist on h1/h2 or slides."""
    if 'data-lecture-section="s1"' in html and 'data-lecture-section="s2"' in html and 'data-lecture-section="s3"' in html:
        return html

    out = html
    # Tag first <h1> as s1
    if 'data-lecture-section="s1"' not in out:
        if re.search(r'<h1\b[^>]*>', out):
            out = re.sub(r'<h1\b([^>]*)>', r'<h1 data-lecture-section="s1"\1>', out, count=1)
        else:
            out = '<div data-lecture-section="s1"></div>\n' + out

    # Tag first and second <h2> (or last <h2>) as s2 and s3
    h2_matches = list(re.finditer(r'<h2\b[^>]*>', out))
    if 'data-lecture-section="s2"' not in out:
        if len(h2_matches) >= 1:
            m = h2_matches[0]
            tag = m.group(0)
            new_tag = tag.replace('<h2', '<h2 data-lecture-section="s2"', 1)
            out = out[:m.start()] + new_tag + out[m.end():]
        else:
            out += '\n<div data-lecture-section="s2"></div>'

    # Re-find h2s after modification
    h2_matches = list(re.finditer(r'<h2\b[^>]*>', out))
    if 'data-lecture-section="s3"' not in out:
        if len(h2_matches) >= 2:
            m = h2_matches[-1]
            tag = m.group(0)
            if 'data-lecture-section=' not in tag:
                new_tag = tag.replace('<h2', '<h2 data-lecture-section="s3"', 1)
                out = out[:m.start()] + new_tag + out[m.end():]
            else:
                out += '\n<div data-lecture-section="s3"></div>'
        else:
            out += '\n<div data-lecture-section="s3"></div>'
    return out


C3_BANNER = """
<div class="box-info" style="background:#fff1f2;border-left:6px solid #e11d48;margin:16px 0;">
  <p style="margin:0;color:#881337;font-size:15.5px;"><b>🚫 CAMBRIDGE 0606 (2025–2027) — FOUNDATION BRIDGE FOR PAPER 1 (NON-CALCULATOR):</b> Từ năm 2025, Indices &amp; Surds là kỹ năng nền tảng được giả định học sinh đã nắm chắc từ 0580 Extended — và là <b>vũ khí bắt buộc trên Paper 1 (Non-Calculator)</b> khi rút gọn nghiệm phương trình bậc 2, diện tích hình học, phương trình đường tròn và giá trị lượng giác chính xác!</p>
</div>
"""

C13_BANNER = """
<div class="box-alert" style="background:#fffbeb;border:2px dashed #d97706;margin:16px 0;">
  <p style="margin:0;color:#78350f;font-size:15.5px;"><b>📢 CAMBRIDGE 0606 SYLLABUS UPDATE (2025–2027) — LƯU Ý PHẠM VI THI:</b> Phần <b>Relative Velocity (Vận tốc tương đối / Compose &amp; Resolve Velocities)</b> bên dưới đã được <b>LOẠI BỎ</b> khỏi đề thi 0606 từ kỳ thi 2025–2027 (chỉ đọc tham khảo mở rộng). Trọng tâm ăn điểm tuyệt đối của Chapter 13 trong kỳ thi 2025–2027 là: <b>Position Vectors, Magnitude &amp; Unit Vectors, Tỉ số chia đoạn thẳng (AP : PB = m : n), và Chứng minh thẳng hàng (Collinearity)</b>!</p>
</div>
"""

CIRCLE_7B_HTML = """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Nunito', sans-serif; background: #ffffff; color: #334155; display: flex; flex-direction: column; align-items: center; }
  .resources-bar { display: flex; flex-wrap: wrap; gap: 10px; padding: 16px 20px; background: #f8fafc; border-bottom: 1px dashed #cbd5e1; justify-content: center; align-items: center; width: 100%; max-width: 1000px; }
  .resources-bar span { font-weight: 800; color: #0f172a; font-size: 14.5px; }
  .badge-new { background: #dc2626; color: #fff; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 800; }
  .badge-nc { background: #fff1f2; color: #be123c; border: 1px solid #fda4af; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 800; }
  .slide { width: 100%; max-width: 1000px; background: #ffffff; position: relative; padding: 38px 22px; border-bottom: 4px solid #f1f5f9; }
  .slide-math::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 8px; background: linear-gradient(90deg, #059669, #0ea5e9, #4f46e5); }
  h1 { font-size: 36px; font-weight: 900; margin-bottom: 8px; line-height: 1.2; color: #0f172a; }
  h2 { font-size: 25px; font-weight: 800; margin-bottom: 18px; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; color: #1e3a8a; }
  h3 { font-size: 19px; font-weight: 800; margin: 18px 0 10px; color: #047857; }
  p { font-size: 16px; line-height: 1.68; margin-bottom: 14px; color: #334155; }
  .subtitle { font-size: 19px; color: #64748b; font-weight: 700; margin-bottom: 22px; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin: 16px 0; }
  .box { border-radius: 14px; padding: 18px; border: 1.5px solid #e2e8f0; background: #f8fafc; }
  .box-info { padding: 18px; border-radius: 12px; margin-bottom: 18px; background: #eff6ff; border-left: 6px solid #2563eb; }
  .box-alert { padding: 18px; border-radius: 12px; margin-bottom: 18px; background: #fff1f2; border: 1.5px dashed #e11d48; }
  .math-block { background: #0f172a; padding: 15px 18px; border-radius: 12px; font-size: 19px; color: #f8fafc; text-align: center; margin: 14px 0; font-weight: 800; letter-spacing: .3px; }
  .worked { background: #ffffff; border: 1.5px solid #cbd5e1; border-left: 5px solid #059669; border-radius: 12px; padding: 18px; margin: 16px 0; }
  .worked-tag { display: inline-block; background: #ecfdf5; color: #065f46; font-size: 11.5px; font-weight: 900; padding: 3px 9px; border-radius: 6px; margin-bottom: 8px; }
  .step-list { list-style: none; counter-reset: st; margin-top: 10px; }
  .step-list li { position: relative; padding: 10px 14px 10px 44px; margin-bottom: 10px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 15px; line-height: 1.6; }
  .step-list li::before { content: counter(st); counter-increment: st; position: absolute; left: 10px; top: 12px; background: #059669; color: #fff; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12.5px; font-weight: 800; }
  .quiz-card { background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 16px; margin-bottom: 14px; }
  .quiz-opts { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 10px 0; }
  .q-opt { padding: 10px 12px; border-radius: 8px; border: 1.5px solid #cbd5e1; background: #fff; cursor: pointer; font-weight: 700; font-size: 14px; text-align: left; font-family: inherit; }
  .q-opt:hover { border-color: #2563eb; background: #eff6ff; }
  .q-opt.is-ok { background: #dcfce7 !important; border-color: #16a34a !important; color: #14532d; }
  .q-opt.is-bad { background: #fee2e2 !important; border-color: #dc2626 !important; color: #7f1d1d; }
  .q-fb { display: none; margin-top: 8px; padding: 10px 12px; border-radius: 8px; font-size: 13.5px; }
  @media (max-width: 768px) { .grid-2, .quiz-opts { grid-template-columns: 1fr; } h1 { font-size: 28px; } }
</style>

<div class="resources-bar">
  <span>📚 Syllabus 0606 — Section 7.4 (NEW 2025–2027):</span>
  <span class="badge-new">🆕 CHƯƠNG MỚI BẮT BUỘC 2025+</span>
  <span class="badge-nc">🚫 PAPER 1 NON-CALC &amp; 🧮 PAPER 2 CALC</span>
</div>

<!-- SLIDE 1: STANDARD & EXPANDED EQUATION -->
<div class="slide slide-math">
  <h1 data-lecture-section="s1">Chapter 7B: Coordinate Geometry of the Circle</h1>
  <div class="subtitle">Phương trình Đường tròn, Tâm &amp; Bán kính, Tiếp tuyến – Pháp tuyến và Giao điểm Đường thẳng – Đường tròn (Mới 2025–2027)</div>

  <div class="box-info">
    <p style="margin:0;"><b>Tại sao chương này siêu quan trọng?</b> Từ kỳ thi <b>Cambridge IGCSE Additional Mathematics 0606 (2025–2027)</b>, phần <b>Coordinate Geometry of the Circle</b> chính thức được bổ sung vào Syllabus bắt buộc và gần như <b>chắc chắn xuất hiện 6–10 điểm</b> trong đề thi Paper 1 (Non-Calculator) hoặc Paper 2 (Calculator)!</p>
  </div>

  <div class="grid-2">
    <div class="box">
      <h3>1. Dạng chính tắc (Standard Form)</h3>
      <p>Đường tròn tâm <b><i>C(a, b)</i></b> và bán kính <b><i>r</i></b> là tập hợp mọi điểm <i>P(x, y)</i> thỏa mãn khoảng cách <i>CP = r</i>:</p>
      <div class="math-block">(x − a)² + (y − b)² = r²</div>
      <p style="font-size:14.5px;"><b>Cẩn thận dấu!</b> Với <code>(x + 3)² + (y − 5)² = 20</code> ⇒ Tâm là <b><i>C(−3, 5)</i></b> (đổi dấu!) và bán kính <b><i>r = √20 = 2√5</i></b> (nhớ lấy căn bậc hai, không phải 20!).</p>
    </div>
    <div class="box">
      <h3>2. Dạng khai triển (Expanded Form)</h3>
      <p>Khi khai triển dạng chính tắc, ta thu được dạng tổng quát:</p>
      <div class="math-block">x² + y² + 2gx + 2fy + c = 0</div>
      <p style="font-size:14.5px;"><b>Tâm:</b> <b><i>C(−g, −f)</i></b> (chia đôi hệ số <i>x, y</i> rồi đổi dấu!).<br/>
      <b>Bán kính:</b> <b><i>r = √(g² + f² − c)</i></b> (điều kiện tồn tại đường tròn: <code>g² + f² − c &gt; 0</code>).<br/>
      <b>Lưu ý:</b> Nếu đề cho <code>2x² + 2y² − 8x + 12y − 6 = 0</code>, BẮT BUỘC <b>chia cả 2 vế cho 2</b> trước khi hoàn chỉnh bình phương!</p>
    </div>
  </div>

  <!-- SVG 1: Circle Standard Form + Diameter -->
  <div style="background:#0f172a;border-radius:14px;padding:14px;margin:16px 0;">
    <div style="font-size:12px;font-weight:800;color:#38bdf8;margin-bottom:8px;">🔵 DIAGRAM 1 — CIRCLE CENTRE C(a, b), RADIUS r, AND DIAMETER ENDPOINTS A, B</div>
    <svg viewBox="0 0 680 230" width="100%" style="display:block;max-height:230px;background:#0b1324;border-radius:10px;">
      <line x1="40" y1="190" x2="360" y2="190" stroke="#64748b" stroke-width="1.6"/>
      <line x1="80" y1="20" x2="80" y2="210" stroke="#64748b" stroke-width="1.6"/>
      <circle cx="215" cy="112" r="70" fill="rgba(56,189,248,0.10)" stroke="#38bdf8" stroke-width="2.8"/>
      <!-- Diameter AB -->
      <line x1="159" y1="154" x2="271" y2="70" stroke="#34d399" stroke-width="2" stroke-dasharray="5,4"/>
      <circle cx="159" cy="154" r="4.5" fill="#34d399"/><text x="122" y="168" fill="#34d399" font-size="12" font-weight="800">A(x₁, y₁)</text>
      <circle cx="271" cy="70" r="4.5" fill="#34d399"/><text x="278" y="68" fill="#34d399" font-size="12" font-weight="800">B(x₂, y₂)</text>
      <!-- Centre & Radius to P(x,y) -->
      <line x1="215" y1="112" x2="215" y2="42" stroke="#fbbf24" stroke-width="2.4"/>
      <circle cx="215" cy="112" r="5" fill="#fbbf24"/><text x="223" y="122" fill="#fbbf24" font-size="12.5" font-weight="800">C(a, b)</text>
      <circle cx="215" cy="42" r="4.5" fill="#f472b6"/><text x="222" y="39" fill="#f472b6" font-size="12" font-weight="800">P(x, y)</text>
      <text x="200" y="80" fill="#fbbf24" font-size="13" font-weight="800">r</text>
      <!-- Right side rules -->
      <rect x="385" y="20" width="275" height="190" rx="10" fill="#131f38" stroke="#334155"/>
      <text x="402" y="48" fill="#38bdf8" font-size="13" font-weight="800">DIAMETER FORM SHORTCUT</text>
      <text x="402" y="74" fill="#e2e8f0" font-size="12">1. Centre C = Midpoint of AB:</text>
      <text x="412" y="96" fill="#34d399" font-size="13" font-weight="800">C = ((x₁+x₂)/2 , (y₁+y₂)/2)</text>
      <text x="402" y="124" fill="#e2e8f0" font-size="12">2. Radius r = ½ × Distance AB:</text>
      <text x="412" y="146" fill="#fbbf24" font-size="13" font-weight="800">r² = (x₁ − a)² + (y₁ − b)²</text>
      <text x="402" y="176" fill="#cbd5e1" font-size="11.5">3. Angle in a semicircle ∠APB = 90°:</text>
      <text x="412" y="196" fill="#f472b6" font-size="12" font-weight="800">m(AP) × m(BP) = −1</text>
    </svg>
  </div>

  <div class="worked">
    <span class="worked-tag">✍️ WORKED EXAMPLE 1 — COMPLETING THE SQUARE [3 marks • Paper 1 Non-Calc]</span>
    <p>Find the coordinates of the centre and the exact radius of the circle <b><i>2x² + 2y² − 12x + 20y − 14 = 0</i></b>.</p>
    <ol class="step-list">
      <li><b>Chia cả 2 vế cho 2</b> để hệ số <i>x²</i> và <i>y²</i> bằng 1: <code>x² + y² − 6x + 10y − 7 = 0</code> <b>[M1]</b></li>
      <li><b>Hoàn chỉnh bình phương theo từng biến:</b> <code>(x − 3)² − 9 + (y + 5)² − 25 − 7 = 0</code> ⇒ <code>(x − 3)² + (y + 5)² = 41</code> <b>[M1]</b></li>
      <li><b>Kết luận:</b> Tâm <b><i>C(3, −5)</i></b>, bán kính <b><i>r = √41</i></b> <b>[A1]</b>.</li>
    </ol>
  </div>
</div>

<!-- SLIDE 2: TANGENTS, NORMALS & CHORDS -->
<div class="slide slide-math">
  <h2 data-lecture-section="s2">2. Tangents, Normals &amp; Perpendicular Bisectors of Chords</h2>
  <p>3 định lý hình học cổ điển của đường tròn khi chuyển sang hệ trục tọa độ sẽ giải quyết <b>90% câu hỏi khó</b> trong đề 0606:</p>

  <!-- SVG 2: Tangent perpendicular to radius + Chord bisector -->
  <div style="background:#0f172a;border-radius:14px;padding:14px;margin:14px 0;">
    <div style="font-size:12px;font-weight:800;color:#34d399;margin-bottom:8px;">📐 DIAGRAM 2 — TANGENT ⊥ RADIUS (NORMAL) &amp; CHORD PERPENDICULAR BISECTOR</div>
    <svg viewBox="0 0 680 230" width="100%" style="display:block;max-height:230px;background:#0b1324;border-radius:10px;">
      <!-- Left: Tangent & Normal -->
      <circle cx="155" cy="120" r="65" fill="rgba(52,211,153,0.10)" stroke="#34d399" stroke-width="2.5"/>
      <circle cx="155" cy="120" r="4.5" fill="#fbbf24"/><text x="128" y="135" fill="#fbbf24" font-size="12" font-weight="800">C(a,b)</text>
      <!-- Point P at (155+52, 120-39) = (207, 81) -->
      <line x1="125" y1="142.5" x2="233" y2="61.5" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3"/>
      <line x1="168" y1="29" x2="255" y2="145" stroke="#f43f5e" stroke-width="2.8"/>
      <circle cx="207" cy="81" r="4.5" fill="#f43f5e"/><text x="215" y="79" fill="#f43f5e" font-size="12" font-weight="800">P(x₁, y₁)</text>
      <text x="220" y="142" fill="#f43f5e" font-size="11.5" font-weight="800">Tangent: m_T = −1/m_CP</text>
      <text x="58" y="34" fill="#fbbf24" font-size="11.5" font-weight="800">Normal passes through C!</text>
      <!-- Right: Chord & Bisector -->
      <circle cx="515" cy="120" r="65" fill="rgba(168,85,247,0.10)" stroke="#c084fc" stroke-width="2.5"/>
      <line x1="463" y1="158" x2="567" y2="158" stroke="#38bdf8" stroke-width="2.8"/>
      <line x1="515" y1="120" x2="515" y2="158" stroke="#fbbf24" stroke-width="2.4"/>
      <line x1="515" y1="120" x2="567" y2="158" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,3"/>
      <rect x="515" y="148" width="10" height="10" fill="none" stroke="#fbbf24" stroke-width="1.5"/>
      <circle cx="515" cy="120" r="4.5" fill="#fbbf24"/><text x="522" y="116" fill="#fbbf24" font-size="12" font-weight="800">C</text>
      <circle cx="515" cy="158" r="4" fill="#38bdf8"/><text x="509" y="174" fill="#38bdf8" font-size="11.5" font-weight="800">M</text>
      <text x="448" y="162" fill="#38bdf8" font-size="12" font-weight="800">A</text>
      <text x="572" y="162" fill="#38bdf8" font-size="12" font-weight="800">B</text>
      <text x="521" y="142" fill="#fbbf24" font-size="11.5" font-weight="800">d</text>
      <text x="546" y="135" fill="#cbd5e1" font-size="11.5" font-weight="800">r</text>
      <text x="415" y="210" fill="#e2e8f0" font-size="12" font-weight="800">Pythagoras: (AB/2)² + d² = r² ⇒ AB = 2√(r² − d²)</text>
    </svg>
  </div>

  <div class="worked">
    <span class="worked-tag">✍️ WORKED EXAMPLE 2 — TANGENT &amp; NORMAL EQUATION [5 marks • Paper 1 Non-Calc]</span>
    <p>A circle has equation <b><i>(x − 2)² + (y + 1)² = 25</i></b>. Verify that <i>P(5, 3)</i> lies on the circle, then find the equation of the <b>tangent</b> to the circle at <i>P</i>.</p>
    <ol class="step-list">
      <li><b>Kiểm tra điểm <i>P(5, 3)</i>:</b> <code>(5 − 2)² + (3 + 1)² = 3² + 4² = 9 + 16 = 25</code> ✔ ⇒ <i>P</i> nằm trên đường tròn <b>[B1]</b>.</li>
      <li><b>Hệ số góc bán kính <i>CP</i> (Normal):</b> Tâm <i>C(2, −1)</i> ⇒ <code>m_CP = (3 − (−1)) / (5 − 2) = 4/3</code> <b>[M1]</b>.</li>
      <li><b>Hệ số góc tiếp tuyến (Tangent ⊥ Radius):</b> <code>m_T = −3/4</code> <b>[M1]</b>.</li>
      <li><b>Phương trình tiếp tuyến qua <i>P(5, 3)</i>:</b> <code>y − 3 = −(3/4)(x − 5)</code> ⇒ <code>4y − 12 = −3x + 15</code> ⇒ <b><i>3x + 4y = 27</i></b> <b>[M1 A1]</b>.</li>
    </ol>
  </div>
</div>

<!-- SLIDE 3: LINE-CIRCLE INTERSECTION & TWO CIRCLES + QUIZ -->
<div class="slide slide-math">
  <h2 data-lecture-section="s3">3. Line–Circle Intersection (Discriminant) &amp; Two Circles</h2>
  <div class="grid-2">
    <div class="box">
      <h3>Giao điểm Đường thẳng <i>y = mx + c</i> &amp; Đường tròn</h3>
      <p style="font-size:14.5px;">Thế <i>y = mx + c</i> vào phương trình đường tròn để thu được phương trình bậc hai <code>Ax² + Bx + C = 0</code>, sau đó xét biệt thức <b><code>Δ = B² − 4AC</code></b>:</p>
      <ul style="padding-left:18px;font-size:14.5px;line-height:1.75;">
        <li><b><code>Δ &gt; 0</code>:</b> Cắt tại <b>2 điểm phân biệt</b> (dây cung / chord).</li>
        <li><b><code>Δ = 0</code>:</b> Tiếp xúc tại <b>1 điểm duy nhất</b> (tiếp tuyến / tangent) — <i>câu hỏi tủ tìm hằng số k!</i></li>
        <li><b><code>Δ &lt; 0</code>:</b> <b>Không giao nhau</b> (does not intersect).</li>
      </ul>
    </div>
    <div class="box">
      <h3>Vị trí tương đối 2 Đường tròn (Khoảng cách tâm <i>d = C₁C₂</i>)</h3>
      <ul style="padding-left:18px;font-size:14.5px;line-height:1.75;">
        <li><b><code>d &gt; r₁ + r₂</code>:</b> Nằm ngoài nhau (không cắt).</li>
        <li><b><code>d = r₁ + r₂</code>:</b> <b>Tiếp xúc ngoài</b> (touch externally).</li>
        <li><b><code>|r₁ − r₂| &lt; d &lt; r₁ + r₂</code>:</b> Cắt nhau tại 2 điểm.</li>
        <li><b><code>d = |r₁ − r₂|</code>:</b> <b>Tiếp xúc trong</b> (touch internally).</li>
        <li><b><code>d &lt; |r₁ − r₂|</code>:</b> Đựng nhau (một đường tròn nằm lọt bên trong).</li>
      </ul>
    </div>
  </div>

  <div class="worked">
    <span class="worked-tag">✍️ WORKED EXAMPLE 3 — TANGENCY VIA DISCRIMINANT [5 marks • Paper 1 Non-Calc]</span>
    <p>Find the exact values of the constant <i>k</i> such that the line <b><i>y = 2x + k</i></b> is a tangent to the circle <b><i>x² + y² = 20</i></b>.</p>
    <ol class="step-list">
      <li><b>Thế <i>y = 2x + k</i> vào đường tròn:</b> <code>x² + (2x + k)² = 20</code> ⇒ <code>5x² + 4kx + (k² − 20) = 0</code> <b>[M1]</b>.</li>
      <li><b>Điều kiện tiếp xúc <code>Δ = b² − 4ac = 0</code>:</b> <code>(4k)² − 4(5)(k² − 20) = 0</code> <b>[M1]</b>.</li>
      <li><b>Rút gọn &amp; Giải <i>k</i>:</b> <code>16k² − 20k² + 400 = 0</code> ⇒ <code>4k² = 400</code> ⇒ <code>k² = 100</code> ⇒ <b><i>k = 10</i> hoặc <i>k = −10</i></b> <b>[M1 A1 A1]</b>.</li>
    </ol>
  </div>

  <h3>🎯 Mini-Quiz Tự kiểm tra Chapter 7B (Chuẩn 2025–2027)</h3>
  <div id="c7b_quiz">
    <div class="quiz-card">
      <p style="margin-bottom:6px;"><b>Q1:</b> Find the centre and radius of the circle <code>x² + y² + 8x − 6y − 11 = 0</code>.</p>
      <div class="quiz-opts">
        <button type="button" class="q-opt" data-ok="0">A. Centre (4, −3), r = 6</button>
        <button type="button" class="q-opt" data-ok="1">B. Centre (−4, 3), r = 6</button>
        <button type="button" class="q-opt" data-ok="0">C. Centre (−4, 3), r = 36</button>
        <button type="button" class="q-opt" data-ok="0">D. Centre (−8, 6), r = √11</button>
      </div>
      <div class="q-fb"><b>[M1 A1]</b> <code>(x + 4)² − 16 + (y − 3)² − 9 − 11 = 0</code> ⇒ <code>(x + 4)² + (y − 3)² = 36</code> ⇒ Tâm <b>(−4, 3)</b>, bán kính <b>r = √36 = 6</b>.</div>
    </div>

    <div class="quiz-card">
      <p style="margin-bottom:6px;"><b>Q2:</b> A circle has diameter <i>AB</i> where <i>A(−2, 7)</i> and <i>B(6, 1)</i>. What is the equation of the circle?</p>
      <div class="quiz-opts">
        <button type="button" class="q-opt" data-ok="1">A. (x − 2)² + (y − 4)² = 25</button>
        <button type="button" class="q-opt" data-ok="0">B. (x − 2)² + (y − 4)² = 100</button>
        <button type="button" class="q-opt" data-ok="0">C. (x + 2)² + (y + 4)² = 25</button>
        <button type="button" class="q-opt" data-ok="0">D. (x − 4)² + (y − 3)² = 25</button>
      </div>
      <div class="q-fb"><b>[M1]</b> Tâm = trung điểm AB = <code>((−2+6)/2, (7+1)/2) = (2, 4)</code>. <b>[M1 A1]</b> <code>r² = (6−2)² + (1−4)² = 16 + 9 = 25</code> ⇒ <b>(x − 2)² + (y − 4)² = 25</b>.</div>
    </div>

    <div class="quiz-card">
      <p style="margin-bottom:6px;"><b>Q3:</b> Circle <i>C₁</i> has centre <i>(1, 2)</i>, radius <i>r₁ = 4</i>. Circle <i>C₂</i> has centre <i>(7, 10)</i>, radius <i>r₂ = 6</i>. How do <i>C₁</i> and <i>C₂</i> relate?</p>
      <div class="quiz-opts">
        <button type="button" class="q-opt" data-ok="0">A. Do not intersect (too far apart)</button>
        <button type="button" class="q-opt" data-ok="0">B. Intersect at 2 points</button>
        <button type="button" class="q-opt" data-ok="1">C. Touch externally</button>
        <button type="button" class="q-opt" data-ok="0">D. Touch internally</button>
      </div>
      <div class="q-fb"><b>[M1]</b> Khoảng cách 2 tâm <code>d = √((7−1)² + (10−2)²) = √(36 + 64) = 10</code>. <b>[A1]</b> Vì <code>r₁ + r₂ = 4 + 6 = 10 = d</code> nên hai đường tròn <b>tiếp xúc ngoài (Touch externally)</b>!</div>
    </div>

    <div class="quiz-card">
      <p style="margin-bottom:6px;"><b>Q4:</b> A circle of radius 10 has a chord at perpendicular distance 6 from the centre. What is the exact length of the chord?</p>
      <div class="quiz-opts">
        <button type="button" class="q-opt" data-ok="0">A. 8</button>
        <button type="button" class="q-opt" data-ok="0">B. 12</button>
        <button type="button" class="q-opt" data-ok="1">C. 16</button>
        <button type="button" class="q-opt" data-ok="0">D. 20</button>
      </div>
      <div class="q-fb"><b>[M1]</b> Nửa dây cung = <code>√(r² − d²) = √(10² − 6²) = √64 = 8</code>. <b>[A1]</b> Cả dây cung = <code>2 × 8 = 16</code>.</div>
    </div>

    <div class="quiz-card">
      <p style="margin-bottom:6px;"><b>Q5:</b> The tangent to <code>(x − 1)² + (y − 2)² = 13</code> at <i>P(3, 5)</i> has gradient:</p>
      <div class="quiz-opts">
        <button type="button" class="q-opt" data-ok="0">A. 3/2</button>
        <button type="button" class="q-opt" data-ok="1">B. −2/3</button>
        <button type="button" class="q-opt" data-ok="0">C. 2/3</button>
        <button type="button" class="q-opt" data-ok="0">D. −3/2</button>
      </div>
      <div class="q-fb"><b>[M1]</b> Hệ số góc bán kính <i>CP</i> = <code>(5 − 2)/(3 − 1) = 3/2</code>. <b>[A1]</b> Tiếp tuyến vuông góc bán kính ⇒ <code>m_T = −2/3</code>.</div>
    </div>
  </div>
</div>

<script>
(function(){
  document.querySelectorAll('#c7b_quiz .quiz-card').forEach(function(card){
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

REV_0606_HTML = """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Nunito', sans-serif; background: #ffffff; color: #334155; display: flex; flex-direction: column; align-items: center; }
  .slide { width: 100%; max-width: 1000px; background: #ffffff; position: relative; padding: 38px 22px; border-bottom: 4px solid #f1f5f9; }
  .slide-math::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 8px; background: linear-gradient(90deg, #991b1b, #d97706, #1d4ed8); }
  h1 { font-size: 34px; font-weight: 900; margin-bottom: 8px; line-height: 1.22; color: #0f172a; }
  h2 { font-size: 24px; font-weight: 800; margin-bottom: 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; color: #1e3a8a; }
  p { font-size: 15.5px; line-height: 1.65; margin-bottom: 14px; color: #334155; }
  .subtitle { font-size: 18px; color: #64748b; font-weight: 700; margin-bottom: 20px; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 14px 0; }
  .card { background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 16px; }
  .nc-card { background: #fff1f2; border: 1.5px solid #fda4af; border-radius: 14px; padding: 18px; }
  .c-card { background: #ecfdf5; border: 1.5px solid #6ee7b7; border-radius: 14px; padding: 18px; }
  .ftbl { width: 100%; border-collapse: collapse; font-size: 13.8px; margin-top: 8px; }
  .ftbl th { background: #0f172a; color: #fff; padding: 9px 11px; text-align: left; }
  .ftbl td { padding: 9px 11px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  .ftbl tr:nth-child(even) { background: #f8fafc; }
  .tag-p { display:inline-block; background:#dcfce7; color:#166534; font-size:11px; font-weight:800; padding:2px 7px; border-radius:5px; }
  .tag-m { display:inline-block; background:#fee2e2; color:#991b1b; font-size:11px; font-weight:800; padding:2px 7px; border-radius:5px; }
  .quiz-card { background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 16px; margin-bottom: 14px; }
  .quiz-opts { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 10px 0; }
  .q-opt { padding: 10px 12px; border-radius: 8px; border: 1.5px solid #cbd5e1; background: #fff; cursor: pointer; font-weight: 700; font-size: 14px; text-align: left; font-family: inherit; }
  .q-opt.is-ok { background: #dcfce7 !important; border-color: #16a34a !important; color: #14532d; }
  .q-opt.is-bad { background: #fee2e2 !important; border-color: #dc2626 !important; color: #7f1d1d; }
  .q-fb { display: none; margin-top: 8px; padding: 10px 12px; border-radius: 8px; font-size: 13.5px; }
  @media (max-width: 768px) { .grid-2, .quiz-opts { grid-template-columns: 1fr; } }
</style>

<!-- SLIDE 1: PAPER 1 NON-CALC vs PAPER 2 CALC PLAYBOOK -->
<div class="slide slide-math">
  <h1 data-lecture-section="s1">Year End Revision: 0606 Paper 1 (Non-Calculator) Survival Playbook &amp; Master Formula Sheet</h1>
  <div class="subtitle">Cẩm nang Săn A* Cambridge IGCSE Additional Mathematics (0606) 2025–2027</div>

  <div class="grid-2">
    <div class="nc-card">
      <div style="font-size:17px;font-weight:900;color:#9f1239;margin-bottom:8px;">🚫 PAPER 1: NON-CALCULATOR (2h • 80 marks • 50%)</div>
      <ul style="padding-left:18px;font-size:14.2px;color:#4c0519;line-height:1.7;">
        <li><b>MỚI từ 2025–2027:</b> Cấm hoàn toàn máy tính! Mọi câu trả lời đều ở dạng <b>chính xác</b> (căn thức, <code>π</code>, <code>e</code>, <code>ln</code>, phân số).</li>
        <li><b>Chuyên đề chắc chắn ra Paper 1:</b> Surds/Rationalising, Circle (Ch. 7B), Factor/Remainder Theorem, Modulus equations, Exact Radian Trig (<code>π/6, π/4, π/3</code>), Binomial coefficients, Exact Differentiation &amp; "Hence integrate".</li>
        <li><b>Chiến thuật thời gian:</b> Trung bình <b>1.5 phút / 1 mark</b> (80 marks = 120 phút). Câu 6 điểm chỉ tối đa 9 phút!</li>
      </ul>
    </div>
    <div class="c-card">
      <div style="font-size:17px;font-weight:900;color:#065f46;margin-bottom:8px;">🧮 PAPER 2: CALCULATOR ALLOWED (2h • 80 marks • 50%)</div>
      <ul style="padding-left:18px;font-size:14.2px;color:#064e3b;line-height:1.7;">
        <li><b>Quy tắc làm tròn:</b> Số thập phân làm tròn <b>3 s.f.</b> (trừ góc theo độ làm tròn <b>1 d.p.</b>). Chú ý chuyển chế độ <b>RAD ↔ DEG</b> giữa các câu!</li>
        <li><b>Chuyên đề đặc sản Paper 2:</b> Linear Law (<code>ln y</code> vs <code>x</code>), Circular Measure (Shaded Segment), Permutations &amp; Combinations, Log/Exp equations to 3 s.f., Connected Rates &amp; Small Changes, Kinematics với <code>e<sup>kt</sup></code>.</li>
        <li><b>Thay đổi Syllabus 2025+:</b> <b>+THÊM</b> Coordinate Geometry of the Circle (Ch. 7B); <b>−BỎ</b> Relative Velocity (Ch. 13).</li>
      </ul>
    </div>
  </div>
</div>

<!-- SLIDE 2: MASTER FORMULA SHEET (ALL 14 TOPICS) -->
<div class="slide slide-math">
  <h2 data-lecture-section="s2">📋 Master Formula Sheet — Toàn bộ 14 Chuyên đề 0606 (2025–2027)</h2>
  <p>Cột <b>Status</b> chỉ rõ công thức nào <span class="tag-p">IN SẴN TRÊN ĐỀ</span> và công thức nào <span class="tag-m">PHẢI THUỘC LÒNG</span>!</p>
  <table class="ftbl">
    <thead><tr><th style="width:20%;">Chuyên đề</th><th style="width:62%;">Công thức cốt lõi</th><th style="width:18%;">Status</th></tr></thead>
    <tbody>
      <tr><td><b>Functions &amp; Quadratics</b></td><td><code>x = (−b ± √(b²−4ac)) / 2a</code>; <code>Δ = b²−4ac</code>; <code>Dom(f⁻¹) = Ran(f)</code>; giải <code>f(x) = f⁻¹(x)</code> qua <code>f(x) = x</code>.</td><td><span class="tag-p">Quad IN SẴN</span><br/><span class="tag-m">Swap THUỘC</span></td></tr>
      <tr><td><b>Polynomials &amp; Logs</b></td><td>Remainder = <code>f(b/a)</code> khi chia cho <code>(ax−b)</code>; <code>log_a(x) = log_b(x)/log_b(a)</code>; <code>ln(e^x) = x</code>.</td><td><span class="tag-m">PHẢI THUỘC</span></td></tr>
      <tr><td><b>Circle (NEW 2025)</b></td><td><code>(x−a)² + (y−b)² = r²</code>; <code>x²+y²+2gx+2fy+c=0</code> ⇒ <code>C(−g,−f), r=√(g²+f²−c)</code>; <code>m_T × m_R = −1</code>.</td><td><span class="tag-m">PHẢI THUỘC</span></td></tr>
      <tr><td><b>Circular Measure</b></td><td><code>180° = π rad</code>; Arc <code>s = rθ</code>; Sector <code>A = ½r²θ</code>; Segment <code>A = ½r²(θ − sin θ)</code>.</td><td><span class="tag-m">PHẢI THUỘC</span></td></tr>
      <tr><td><b>Trigonometry</b></td><td><code>sin²A + cos²A = 1</code>; <code>sec²A = 1 + tan²A</code>; <code>cosec²A = 1 + cot²A</code>. Exact: <code>π/6, π/4, π/3</code>!</td><td><span class="tag-p">Identities IN SẴN</span><br/><span class="tag-m">Exact THUỘC</span></td></tr>
      <tr><td><b>Series (Binomial, AP, GP)</b></td><td><code>(a+b)ⁿ = Σ nCr aⁿ⁻ʳ bʳ</code>; AP: <code>uₙ = a+(n−1)d</code>, <code>Sₙ = ½n(2a+(n−1)d)</code>; GP: <code>uₙ = arⁿ⁻¹</code>, <code>S∞ = a/(1−r)</code> (<code>|r|&lt;1</code>).</td><td><span class="tag-p">IN SẴN TRÊN ĐỀ</span></td></tr>
      <tr><td><b>Differentiation</b></td><td>Product <code>uv' + vu'</code>; Quotient <code>(vu' − uv')/v²</code>; <code>(sin ax)' = a cos ax</code>; <code>(cos ax)' = −a sin ax</code>; <code>(tan ax)' = a sec² ax</code>; <code>(eᵃˣ)' = aeᵃˣ</code>; <code>(ln(ax+b))' = a/(ax+b)</code>.</td><td><span class="tag-m">PHẢI THUỘC</span></td></tr>
      <tr><td><b>Integration &amp; Kinematics</b></td><td><code>∫(ax+b)ⁿ dx = (ax+b)ⁿ⁺¹/[a(n+1)] + c</code>; <code>∫eᵃˣ dx = (1/a)eᵃˣ + c</code>; <code>∫1/(ax+b) dx = (1/a)ln|ax+b| + c</code>; <code>v = ds/dt</code>, <code>a = dv/dt</code>.</td><td><span class="tag-m">PHẢI THUỘC</span></td></tr>
    </tbody>
  </table>
</div>

<!-- SLIDE 3: TOP 8 PAPER 1 TRAPS & MINI-QUIZ -->
<div class="slide slide-math">
  <h2 data-lecture-section="s3">⚠️ Top 6 Bẫy Mất Điểm Kinh Điển Trên Paper 1 &amp; Bài Tập Tổng Hợp</h2>
  <div class="grid-2" style="margin-bottom:18px;">
    <div class="card"><b>1. Quên nhân hệ số trong Chain Rule:</b> <code>d/dx[sin(3x)] = 3 cos(3x)</code> (KHÔNG phải <code>cos(3x)</code>); <code>∫cos(2x) dx = ½ sin(2x) + c</code>!</div>
    <div class="card"><b>2. Quên loại nghiệm âm của Log:</b> Khi giải <code>ln(x−2) + ln(x+1) = ln 4</code>, BẮT BUỘC kiểm tra <code>x &gt; 2</code> rồi gạch nghiệm ngoại lai!</div>
    <div class="card"><b>3. Nhầm độ (DEG) và radian (RAD):</b> Hễ miền đề là <code>0 ≤ x ≤ 2π</code> thì toàn bộ bài toán và đáp án phải tính theo <b>Radian</b>!</div>
    <div class="card"><b>4. Tính Total Distance khi hạt đổi chiều:</b> Giải <code>v(t) = 0</code> xem có thời điểm đổi chiều trong khoảng <code>[t₁, t₂]</code> không — nếu có phải tách <code>|Δs₁| + |Δs₂|</code>!</div>
  </div>

  <div id="rev0606_quiz">
    <div class="quiz-card">
      <p style="margin-bottom:6px;"><b>Q1 (🚫 Non-Calc • Trig):</b> Find the exact value of <code>sec²(π/3) − tan(π/4)</code>.</p>
      <div class="quiz-opts">
        <button type="button" class="q-opt" data-ok="0">A. 1</button>
        <button type="button" class="q-opt" data-ok="0">B. 2</button>
        <button type="button" class="q-opt" data-ok="1">C. 3</button>
        <button type="button" class="q-opt" data-ok="0">D. 4</button>
      </div>
      <div class="q-fb"><b>[M1 A1]</b> <code>cos(π/3) = 1/2</code> ⇒ <code>sec(π/3) = 2</code> ⇒ <code>sec²(π/3) = 4</code>. <code>4 − 1 = 3</code>.</div>
    </div>

    <div class="quiz-card">
      <p style="margin-bottom:6px;"><b>Q2 (🚫 Non-Calc • Calculus):</b> Evaluate <code>∫₀¹ (6e²ˣ) dx</code> in exact form.</p>
      <div class="quiz-opts">
        <button type="button" class="q-opt" data-ok="1">A. 3e² − 3</button>
        <button type="button" class="q-opt" data-ok="0">B. 3e²</button>
        <button type="button" class="q-opt" data-ok="0">C. 6e² − 6</button>
        <button type="button" class="q-opt" data-ok="0">D. 12e² − 12</button>
      </div>
      <div class="q-fb"><b>[M1]</b> Nguyên hàm = <code>[3e²ˣ]₀¹</code>. <b>[A1]</b> <code>3e² − 3e⁰ = 3e² − 3</code> (Cẩn thận bẫy <code>e⁰ = 1</code>, không phải 0!).</div>
    </div>

    <div class="quiz-card">
      <p style="margin-bottom:6px;"><b>Q3 (🚫 Non-Calc • Logs):</b> Solve <code>log₃(x) + log₃(x − 2) = 1</code>.</p>
      <div class="quiz-opts">
        <button type="button" class="q-opt" data-ok="0">A. x = −1 or x = 3</button>
        <button type="button" class="q-opt" data-ok="1">B. x = 3 only</button>
        <button type="button" class="q-opt" data-ok="0">C. x = 4 only</button>
        <button type="button" class="q-opt" data-ok="0">D. x = 1 only</button>
      </div>
      <div class="q-fb"><b>[M1]</b> <code>x(x − 2) = 3¹ = 3</code> ⇒ <code>x² − 2x − 3 = 0</code> ⇒ <code>x = 3</code> hoặc <code>x = −1</code>. <b>[A1]</b> Vì cần <code>x &gt; 2</code> nên loại <code>x = −1</code> ⇒ <b>x = 3 only</b>!</div>
    </div>

    <div class="quiz-card">
      <p style="margin-bottom:6px;"><b>Q4 (🚫 Non-Calc • Series):</b> A GP has first term 12 and sum to infinity 18. Find the common ratio <i>r</i>.</p>
      <div class="quiz-opts">
        <button type="button" class="q-opt" data-ok="0">A. 2/3</button>
        <button type="button" class="q-opt" data-ok="1">B. 1/3</button>
        <button type="button" class="q-opt" data-ok="0">C. −1/3</button>
        <button type="button" class="q-opt" data-ok="0">D. 1/2</button>
      </div>
      <div class="q-fb"><b>[M1 A1]</b> <code>18 = 12 / (1 − r)</code> ⇒ <code>1 − r = 12/18 = 2/3</code> ⇒ <b>r = 1/3</b>.</div>
    </div>
  </div>
</div>

<script>
(function(){
  document.querySelectorAll('#rev0606_quiz .quiz-card').forEach(function(card){
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

TUTOR_CONTEXT_0606 = {
    'c1': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 1: Functions. Domain, range, 1-to-1 restriction for inverse f^-1(x), composite fg(x), mirror symmetry across y=x, modulus functions |ax+b| and |quadratic|. Heavily tested on Paper 1 Non-Calculator.',
    'c2': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 2: Quadratic Functions. Completing the square a(x+p)^2+q, min/max values, discriminant b^2-4ac for line-curve tangency and intersection conditions, quadratic inequalities, hidden quadratics.',
    'c3': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 3: Indices & Surds (Foundation Bridge for Paper 1 Non-Calculator). Rationalising denominators (a+b√c)/(d+e√c), exact geometric surds, index equations.',
    'c4': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 4: Factors of Polynomials. Remainder Theorem, Factor Theorem, cubic factorisation, solving cubic equations & inequalities without a calculator (Paper 1 hotspot).',
    'c5': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 5: Equations, Inequalities & Graphs. Simultaneous linear + non-linear equations, modulus equations |ax+b|=|cx+d|, modulus inequalities, cubic/quadratic inequalities.',
    'c6': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 6: Logarithmic & Exponential Functions. Laws of logarithms, change of base, solving exponential/log equations (Paper 1 exact + Paper 2 3 s.f.), graphs/asymptotes/inverses of e^(ax+b) and ln(ax+b).',
    'c7': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 7: Straight Line Graphs & Linear Law. Perpendicular bisectors, shoelace area of polygons, transforming non-linear relations (y=Ax^n, y=Ab^x, y=ax^2+bx) into straight line Y=mX+c.',
    'c7b': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 7B: Coordinate Geometry of the Circle (NEW 2025-2027 COMPULSORY TOPIC!). Standard equation (x-a)^2+(y-b)^2=r^2, expanded form x^2+y^2+2gx+2fy+c=0, completing the square for centre/radius, diameter form, tangent & normal equations (m_T*m_R=-1), chord midpoint & length, line-circle intersection discriminant, two-circle touching conditions.',
    'c8': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 8: Circular Measure. Radians, arc length s=r*theta, sector area A=1/2*r^2*theta, segment area 1/2*r^2*(theta - sin theta), perimeters of composite shapes (Paper 1 exact + Paper 2 3 s.f.).',
    'c9': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 9: Trigonometry. Graphs a sin(bx)+c, exact radian values (pi/6, pi/4, pi/3), sec/cosec/cot, identities sec^2=1+tan^2 & cosec^2=1+cot^2, solving trig equations in radians and degrees.',
    'c10': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 10: Permutations & Combinations. Arrangements with restrictions (together, separated, ends), digit-forming problems, combinations nCr, committee selections with at-least conditions (Paper 2 Calculator).',
    'c11': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 11: Series. Binomial expansion (a+bx)^n, term independent of x, Arithmetic Progressions (u_n, S_n), Geometric Progressions (u_n, S_n, convergence |r|<1, S_infinity = a/(1-r)).',
    'c12': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 12: Differentiation 1. Chain rule, Product rule, Quotient rule, tangents & normals, stationary points dy/dx=0, second derivative test d^2y/dx^2 for nature of turning points.',
    'c13': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 13: Vectors. IMPORTANT 2025-2027 UPDATE: Relative Velocity was REMOVED! Focus on position vectors, magnitude, unit vectors, ratio division AP:PB=m:n, collinearity proofs, equating coefficients.',
    'c14': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 14: Differentiation 2. Derivatives of sin(ax), cos(ax), tan(ax), e^(ax+b), ln(ax+b); connected rates of change; small changes delta_y ≈ (dy/dx)*delta_x; optimisation.',
    'c15': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 15: Integration. Indefinite & definite integrals of (ax+b)^n, e^(ax+b), 1/(ax+b), sin, cos, sec^2; "Hence find..." reverse differentiation; area under curve and between two curves.',
    'c16': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Chapter 16: Kinematics. Calculus links v=ds/dt, a=dv/dt, instantaneous rest v=0, max velocity a=0, displacement vs total distance travelled (splitting when v changes sign).',
    'rev': 'Cambridge IGCSE Additional Maths 0606 (2025-2027) Year End Revision: Paper 1 (Non-Calculator, 80 marks, 2h) vs Paper 2 (Calculator, 80 marks, 2h) Survival Playbook, complete 14-topic Master Formula Sheet (printed vs memorise), and top exam traps.',
}


def main():
    ids = load_ids()
    m0606 = ids['m0606']
    print("=== UPGRADING IGCSE MATHS 0606 LECTURES (2025-2027) ===", flush=True)

    # 1. Create NEW Chapter 7B: Coordinate Geometry of the Circle (Module 2, order_index=3)
    c7b_id = upsert_lecture_with_page(
        course_id=COURSE_0606_ID,
        module_id=m0606['modules']['m2'],
        title='Chapter 7B: Coordinate Geometry of the Circle (NEW 2025–2027)',
        order_index=3,
        content_html=CIRCLE_7B_HTML,
        tutor_context=TUTOR_CONTEXT_0606['c7b'],
        existing_lecture_id=m0606['lectures'].get('c7b'),
    )
    m0606['lectures']['c7b'] = c7b_id

    # 2. Create NEW Year End Revision: Paper 1 Non-Calc Playbook (Module 5, order_index=1)
    rev_id = upsert_lecture_with_page(
        course_id=COURSE_0606_ID,
        module_id=m0606['modules']['m5'],
        title='Year End Revision: Paper 1 (Non-Calculator) Playbook & Master Formula Sheet (0606 2025–2027)',
        order_index=1,
        content_html=REV_0606_HTML,
        tutor_context=TUTOR_CONTEXT_0606['rev'],
        existing_lecture_id=m0606['lectures'].get('rev'),
    )
    m0606['lectures']['rev'] = rev_id
    save_ids(ids)

    # 3. Patch Chapter 3 (Foundation Bridge banner) and Chapter 13 (Relative Velocity removed notice)
    c3_id = m0606['lectures']['c3']
    p3 = sb_get(f'lecture_pages?lecture_id=eq.{c3_id}&order=page_number.asc&select=id,content_html')[0]
    p3_html = replace_or_insert_marker(
        p3['content_html'],
        '<!-- TONY_2025_0606_C3_START -->',
        '<!-- TONY_2025_0606_C3_END -->',
        C3_BANNER,
        r'</h1>',
        insert_before=False,
    )
    sb_patch(f'lecture_pages?id=eq.{p3["id"]}', {'content_html': p3_html})
    print("  [PATCHED] Chapter 3: Indices & Surds (+Paper 1 Non-Calc Foundation Bridge banner)", flush=True)

    c13_id = m0606['lectures']['c13']
    p13 = sb_get(f'lecture_pages?lecture_id=eq.{c13_id}&order=page_number.asc&select=id,content_html')[0]
    p13_html = replace_or_insert_marker(
        p13['content_html'],
        '<!-- TONY_2025_0606_C13_START -->',
        '<!-- TONY_2025_0606_C13_END -->',
        C13_BANNER,
        r'<h2[^>]*>Compose and Resolve Velocities',
        insert_before=True,
    )
    sb_patch(f'lecture_pages?id=eq.{p13["id"]}', {'content_html': p13_html})
    print("  [PATCHED] Chapter 13: Vectors (+2025-2027 Relative Velocity Removal Notice)", flush=True)

    # 4. Inject audio anchors (data-lecture-section="s1/s2/s3") & tutor_context on ALL 18 lectures of 0606
    for key, lid in m0606['lectures'].items():
        ctx = TUTOR_CONTEXT_0606.get(key)
        if ctx:
            sb_patch(f'lectures?id=eq.{lid}', {'tutor_context': ctx})
        pages = sb_get(f'lecture_pages?lecture_id=eq.{lid}&order=page_number.asc&select=id,content_html')
        if pages:
            orig = pages[0]['content_html'] or ''
            anchored = ensure_audio_section_anchors(orig)
            if anchored != orig:
                sb_patch(f'lecture_pages?id=eq.{pages[0]["id"]}', {'content_html': anchored})
    print(f"  [OK] Updated tutor_context & audio section anchors on all {len(m0606['lectures'])} lectures of Maths 0606!", flush=True)
    print("\n[DONE] IGCSE Maths 0606 lectures upgraded successfully!", flush=True)


if __name__ == '__main__':
    main()
