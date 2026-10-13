import os
import sys
import re
import json
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

def make_banner_vi(topic_num, topic_name, lec_title, subtitle):
    return f"""<!-- Lecture Top Banner & Controls -->
<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%); padding: 28px 32px; border-radius: 14px; color: #ffffff; margin-bottom: 25px; box-shadow: 0 10px 25px -5px rgba(30,58,138,0.25); cursor: pointer; transition: all 0.2s ease; position: relative;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
    <span style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #93c5fd;">Cambridge IGCSE Economics (0455) • Topic {topic_num}: {topic_name}</span>
    <span style="background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.4); padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 600;">Bản Tiếng Việt</span>
  </div>
  <h1 style="margin: 0; font-size: 30px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px; padding-right: 140px;">{lec_title}</h1>
  <p style="margin: 8px 0 0 0; font-size: 15.5px; color: #e0f2fe; opacity: 0.95; line-height: 1.5;">{subtitle}</p>
</div>"""

def strip_study_resources(html):
    pattern = r'<!--\s*(?:Thanh Tài liệu học tập|Study Resources Bar)[^>]*-->\s*<div[^>]*>.*?</div>\s*'
    return re.sub(pattern, '', html, flags=re.DOTALL)

def insert_banner(html, banner):
    m = re.search(r'<div style="[^"]*(?:font-family|max-width)[^"]*>', html)
    if m:
        pos = m.end()
        return html[:pos] + "\n\n    " + banner + "\n" + html[pos:]
    return banner + "\n" + html

# =====================================================================
# LECTURE 16
# =====================================================================
def build_c16_p2_html():
    with open('scripts/raw_econ/lec_16_p2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner_vi(3, "Các chủ thể ra quyết định vi mô", "16. Tiền tệ và Hệ thống Ngân hàng", "Sự tiến hóa của Tiền, Bốn Chức năng, Đặc tính &amp; Vai trò của Hệ thống Ngân hàng")
    html = insert_banner(html, banner)

    # 1. Evolution
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*1\.[^<]*</h2>)',
        r'''<div id="sec-evolution" class="lecture-interactive-card" data-lecture-section="sec_evolution" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # card-forms
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(280px,\s*1fr\)\); gap: 20px; margin-bottom:\s*(?:30px|25px);">',
        '''<div id="card-forms" class="lecture-interactive-card" data-lecture-section="card_forms" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 25px; border: 1.5px solid #bfdbfe; border-radius: 14px; padding: 18px; background: #f8fafc; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # 2. Functions & Characteristics
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*2\.[^<]*</h2>)',
        r'''<div id="sec-functions" class="lecture-interactive-card" data-lecture-section="sec_functions" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # card-four-functions
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(280px,\s*1fr\)\); gap: 20px; margin-bottom:\s*(?:30px|35px);">',
        '''<div id="card-four-functions" class="lecture-interactive-card" data-lecture-section="card_four_functions" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 35px; border: 1.5px solid #ddd6fe; border-radius: 14px; padding: 18px; background: #faf5ff; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #7e22ce; background: #f5f3ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #ddd6fe; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # card-characteristics
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(200px,\s*1fr\)\); gap: 15px; margin-bottom:\s*(?:30px|35px);">',
        '''<div id="card-characteristics" class="lecture-interactive-card" data-lecture-section="card_characteristics" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 35px; border: 1.5px solid #cbd5e1; border-radius: 14px; padding: 18px; background: #f8fafc; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #475569; background: #f1f5f9; padding: 2px 8px; border-radius: 8px; border: 1px solid #cbd5e1; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # 3. Banking
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*3\.[^<]*</h2>)',
        r'''<div id="sec-banking" class="lecture-interactive-card" data-lecture-section="sec_banking" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # card-central-bank
    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*2px solid #fed7aa;[^>]*>',
        '''<div id="card-central-bank" class="lecture-interactive-card" data-lecture-section="card_central_bank" style="background: #ffffff; border: 2px solid #fed7aa; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #c2410c; background: #fff7ed; padding: 2px 8px; border-radius: 8px; border: 1px solid #fed7aa; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # card-commercial-bank
    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*2px solid #bfdbfe;[^>]*>',
        '''<div id="card-commercial-bank" class="lecture-interactive-card" data-lecture-section="card_commercial_bank" style="background: #ffffff; border: 2px solid #bfdbfe; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # 4. Exam Focus
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*4\.[^<]*</h2>)',
        r'''<div id="sec-borrowing" class="lecture-interactive-card" data-lecture-section="sec_borrowing" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 17
# =====================================================================
def build_c17_p2_html():
    with open('scripts/raw_econ/lec_17_p2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner_vi(3, "Các chủ thể ra quyết định vi mô", "17. Hộ gia đình: Chi tiêu, Tiết kiệm và Vay nợ", "Các yếu tố quyết định Tiêu dùng, Động cơ Tiết kiệm &amp; Vay nợ")
    html = insert_banner(html, banner)

    # 1. Spending
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*1\.[^<]*</h2>)',
        r'''<div id="sec-spending" class="lecture-interactive-card" data-lecture-section="sec_spending" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # card-spending-factors
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(280px,\s*1fr\)\); gap: 20px; margin-bottom:\s*(?:30px|35px);">',
        '''<div id="card-spending-factors" class="lecture-interactive-card" data-lecture-section="card_spending_factors" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 35px; border: 1.5px solid #bfdbfe; border-radius: 14px; padding: 18px; background: #f8fafc; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # 2. Saving
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*2\.[^<]*</h2>)',
        r'''<div id="sec-saving" class="lecture-interactive-card" data-lecture-section="sec_saving" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # card-saving-motives
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(280px,\s*1fr\)\); gap: 20px; margin-bottom: 30px;">',
        '''<div id="card-saving-motives" class="lecture-interactive-card" data-lecture-section="card_saving_motives" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 30px; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 18px; background: #f0fdf4; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 8px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # 3. Borrowing
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*3\.[^<]*</h2>)',
        r'''<div id="sec-borrowing" class="lecture-interactive-card" data-lecture-section="sec_borrowing" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #ffedd5; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 4. Wealth Exam Focus
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*4\.[^<]*</h2>)',
        r'''<div id="sec-wealth" class="lecture-interactive-card" data-lecture-section="sec_wealth" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 18
# =====================================================================
def build_c18_p2_html():
    with open('scripts/raw_econ/lec_18_p2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner_vi(3, "Các chủ thể ra quyết định vi mô", "18. Người lao động: Tiền lương và Tính di động", "Lựa chọn nghề nghiệp, Cung - Cầu lao động, Lương tối thiểu &amp; Chênh lệch tiền lương")
    html = insert_banner(html, banner)

    # 1. Occupation
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*1\.[^<]*</h2>)',
        r'''<div id="sec-occupation" class="lecture-interactive-card" data-lecture-section="sec_occupation" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # card-wage-factors
    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*1px solid #bfdbfe;[^>]*>',
        '''<div id="card-wage-factors" class="lecture-interactive-card" data-lecture-section="card_wage_factors" style="background: #ffffff; border: 1.5px solid #3b82f6; border-radius: 12px; padding: 25px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # card-non-wage-factors
    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*1px solid #bbf7d0;[^>]*>',
        '''<div id="card-non-wage-factors" class="lecture-interactive-card" data-lecture-section="card_non_wage_factors" style="background: #ffffff; border: 1.5px solid #10b981; border-radius: 12px; padding: 25px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 8px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # 2. Wage determination
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*2\.[^<]*</h2>)',
        r'''<div id="sec-wage-determination" class="lecture-interactive-card" data-lecture-section="sec_wage_determination" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 3. Minimum wage
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*3\.[^<]*</h2>)',
        r'''<div id="sec-nmw" class="lecture-interactive-card" data-lecture-section="sec_nmw" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 4. Differentials
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*4\.[^<]*</h2>)',
        r'''<div id="sec-wage-differentials" class="lecture-interactive-card" data-lecture-section="sec_wage_differentials" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 5. Mobility & Division
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*5\.[^<]*</h2>)',
        r'''<div id="sec-mobility-division" class="lecture-interactive-card" data-lecture-section="sec_mobility_division" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfeff; border: 1px solid #a5f3fc; border-radius: 20px; font-size: 12px; font-weight: 600; color: #0891b2; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 19
# =====================================================================
def build_c19_p2_html():
    with open('scripts/raw_econ/lec_19_p2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner_vi(3, "Các chủ thể ra quyết định vi mô", "19. Công đoàn (Trade Unions)", "Định nghĩa, Phân loại, Tranh đấu công nghiệp, Sức mạnh đàm phán &amp; Đánh giá kinh tế")
    html = insert_banner(html, banner)

    # 1. Union Intro
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*1\.[^<]*</h2>)',
        r'''<div id="sec-union-intro" class="lecture-interactive-card" data-lecture-section="sec_union_intro" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # card-union-types
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(280px,\s*1fr\)\); gap: 20px; margin-bottom:\s*(?:30px|35px);">',
        '''<div id="card-union-types" class="lecture-interactive-card" data-lecture-section="card_union_types" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 35px; border: 1.5px solid #bfdbfe; border-radius: 14px; padding: 18px; background: #f8fafc; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # 2. Industrial Action
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*2\.[^<]*</h2>)',
        r'''<div id="sec-industrial-action" class="lecture-interactive-card" data-lecture-section="sec_industrial_action" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #ffedd5; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 3. Bargaining Power
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*3\.[^<]*</h2>)',
        r'''<div id="sec-bargaining-power" class="lecture-interactive-card" data-lecture-section="sec_bargaining_power" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 4. Evaluation
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*4\.[^<]*</h2>)',
        r'''<div id="sec-evaluation" class="lecture-interactive-card" data-lecture-section="sec_evaluation" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 20
# =====================================================================
def build_c20_p2_html():
    with open('scripts/raw_econ/lec_20_p2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner_vi(3, "Các chủ thể ra quyết định vi mô", "20. Doanh nghiệp: Quy mô, Tăng trưởng &amp; Sáp nhập", "Phân loại khu vực kinh tế, Doanh nghiệp Nhỏ vs Lớn, Sáp nhập &amp; Tính kinh tế theo quy mô")
    html = insert_banner(html, banner)

    # 1. Classification
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*1\.[^<]*</h2>)',
        r'''<div id="sec-classification" class="lecture-interactive-card" data-lecture-section="sec_classification" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 2. Firm Size
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*2\.[^<]*</h2>)',
        r'''<div id="sec-firm-size" class="lecture-interactive-card" data-lecture-section="sec_firm_size" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # card-small-vs-large
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(320px,\s*1fr\)\); gap: 25px; margin-bottom:\s*(?:30px|35px);">',
        '''<div id="card-small-vs-large" class="lecture-interactive-card" data-lecture-section="card_small_vs_large" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px; margin-bottom: 30px; border: 1.5px solid #cbd5e1; border-radius: 14px; padding: 18px; background: #f8fafc; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #475569; background: #ffffff; padding: 2px 8px; border-radius: 8px; border: 1px solid #cbd5e1; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # 3. Mergers & Integration
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*3\.[^<]*</h2>)',
        r'''<div id="sec-integration" class="lecture-interactive-card" data-lecture-section="sec_integration" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 4. Economies of Scale
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*4\.[^<]*</h2>)',
        r'''<div id="sec-economies-scale" class="lecture-interactive-card" data-lecture-section="sec_economies_scale" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 21
# =====================================================================
def build_c21_p2_html():
    with open('scripts/raw_econ/lec_21_p2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner_vi(3, "Các chủ thể ra quyết định vi mô", "21. Doanh nghiệp và Sản xuất: Cầu yếu tố sản xuất &amp; Chi phí", "Cầu dẫn xuất, Mức độ thâm dụng vốn/lao động, Sản lượng vs Năng suất &amp; Chi phí")
    html = insert_banner(html, banner)

    # 1. Factor Demand
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*1\.[^<]*</h2>)',
        r'''<div id="sec-factor-demand" class="lecture-interactive-card" data-lecture-section="sec_factor_demand" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 2. Intensity
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*2\.[^<]*</h2>)',
        r'''<div id="sec-intensity" class="lecture-interactive-card" data-lecture-section="sec_intensity" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 3. Productivity
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*3\.[^<]*</h2>)',
        r'''<div id="sec-productivity" class="lecture-interactive-card" data-lecture-section="sec_productivity" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 4. Short-Run Costs
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*4\.[^<]*</h2>)',
        r'''<div id="sec-short-run-costs" class="lecture-interactive-card" data-lecture-section="sec_short_run_costs" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 22
# =====================================================================
def build_c22_p2_html():
    with open('scripts/raw_econ/lec_22_p2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner_vi(3, "Các chủ thể ra quyết định vi mô", "22. Mục tiêu doanh nghiệp, Chi phí, Doanh thu &amp; Điểm hòa vốn", "Mục tiêu kinh doanh, Công thức chi phí, Bảng tính toán &amp; Phân tích điểm hòa vốn")
    html = insert_banner(html, banner)

    # 1. Objectives
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*1\.[^<]*</h2>)',
        r'''<div id="sec-objectives" class="lecture-interactive-card" data-lecture-section="sec_objectives" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # card-objectives-grid
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(280px,\s*1fr\)\); gap: 20px; margin-bottom:\s*(?:30px|35px);">',
        '''<div id="card-objectives-grid" class="lecture-interactive-card" data-lecture-section="card_objectives_grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 35px; border: 1.5px solid #bfdbfe; border-radius: 14px; padding: 18px; background: #f8fafc; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # 2. Formulas
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*2\.[^<]*</h2>)',
        r'''<div id="sec-formulas" class="lecture-interactive-card" data-lecture-section="sec_formulas" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 3. Revenue & Break-even
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*3\.[^<]*</h2>)',
        r'''<div id="sec-revenue-breakeven" class="lecture-interactive-card" data-lecture-section="sec_revenue_breakeven" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 23
# =====================================================================
def build_c23_p2_html():
    with open('scripts/raw_econ/lec_23_p2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner_vi(3, "Các chủ thể ra quyết định vi mô", "23. Cấu trúc thị trường: Cạnh tranh hoàn hảo vs Độc quyền", "Thị trường cạnh tranh vs Độc quyền thuần túy, Quyền định giá &amp; Phúc lợi người tiêu dùng")
    html = insert_banner(html, banner)

    # 1. Competition vs Monopoly
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*1\.[^<]*</h2>)',
        r'''<div id="sec-competition-vs-monopoly" class="lecture-interactive-card" data-lecture-section="sec_competition_vs_monopoly" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # card-comparison-table (Section 2)
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*2\.[^<]*</h2>)',
        r'''<div id="card-comparison-table" class="lecture-interactive-card" data-lecture-section="card_comparison_table" style="background: white; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 20px; font-size: 12px; font-weight: 600; color: #475569; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 3. Impact on Price & Output
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*3\.[^<]*</h2>)',
        r'''<div id="sec-impact-price-output" class="lecture-interactive-card" data-lecture-section="sec_impact_price_output" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    # 4. Evaluating Monopoly
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*(<h2[^>]*>[^<]*4\.[^<]*</h2>)',
        r'''<div id="sec-evaluating-monopoly" class="lecture-interactive-card" data-lecture-section="sec_evaluating_monopoly" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \1''',
        html, count=1
    )

    return html

def verify_build(lec_num, html):
    manifest_path = f'public/audio/lectures/economics/{lec_num}/manifest.json'
    if not os.path.exists(manifest_path):
        print(f"Skipping {lec_num}: No manifest")
        return False
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    soup = BeautifulSoup(html, 'html.parser')
    missing = []
    for s in manifest.get('segments', []):
        sel = s.get('selector', '')
        if sel.startswith('#'):
            el_id = sel[1:]
            if not soup.find(id=el_id):
                missing.append(sel)
        elif sel.startswith('.'):
            cl = sel[1:]
            if not soup.find(class_=cl):
                missing.append(sel)

    # Div balance
    open_divs = len(re.findall(r'<div\b', html))
    close_divs = len(re.findall(r'</div\b', html))
    diff = open_divs - close_divs

    if not missing and diff == 0:
        print(f"✅ Lec {lec_num}: 100% MATCH ({len(manifest['segments'])} segments, diff={diff})")
        return True
    else:
        print(f"❌ Lec {lec_num}: Missing {len(missing)}: {missing}, diff={diff}")
        return False

if __name__ == '__main__':
    builders = [
        (16, build_c16_p2_html),
        (17, build_c17_p2_html),
        (18, build_c18_p2_html),
        (19, build_c19_p2_html),
        (20, build_c20_p2_html),
        (21, build_c21_p2_html),
        (22, build_c22_p2_html),
        (23, build_c23_p2_html),
    ]

    for num, b in builders:
        html = b()
        verify_build(num, html)
