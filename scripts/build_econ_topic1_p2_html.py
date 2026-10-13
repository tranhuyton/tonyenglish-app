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
# LECTURE 1 (Page 2)
# =====================================================================
def build_c1_p2_html():
    with open('scripts/raw_econ/lec_1_p2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner_vi(1, "The Basic Economic Problem", "1. Vấn đề Kinh tế Cơ bản", "Nguồn lực Hữu hạn vs Nhu cầu Vô hạn, Các Quyết định Kinh tế Cốt lõi &amp; Phân loại Hàng hóa")
    html = insert_banner(html, banner)

    # Sec 1
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*1\.[^<]*</h2>)',
        '''<div id="sec-nature" class="lecture-interactive-card" data-lecture-section="sec_nature" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # Card concept map
    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*2px solid #e2e8f0;\s*border-radius:\s*12px;\s*padding:\s*30px;\s*box-shadow:\s*0 10px 15px -3px rgba\(0,0,0,0.05\);\s*margin-top:\s*25px;\s*margin-bottom:\s*30px;">\s*(<h3[^>]*>[^<]*</h3>)',
        '''<div id="card-concept-map" class="lecture-interactive-card" data-lecture-section="card_concept_map" style="background: #ffffff; border: 2px solid #93c5fd; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-top: 25px; margin-bottom: 30px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 10px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
            \\1''',
        html, count=1
    )

    # Sec 2
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*2\.[^<]*</h2>)',
        '''<div id="sec-contexts" class="lecture-interactive-card" data-lecture-section="sec_contexts" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eef2ff; border: 1px solid #c7d2fe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #4338ca; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # 4 sub-cards
    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*1px solid #cbd5e1;\s*border-top:\s*4px solid #3b82f6;\s*border-radius:\s*10px;\s*padding:\s*20px;\s*box-shadow:\s*0 4px 6px rgba\(0,0,0,0.02\);[^"]*">\s*<div style="font-size: 28px; margin-bottom: 8px;">🛒</div>\s*(<h4[^>]*>[^<]*</h4>)',
        '''<div id="card-consumers" class="lecture-interactive-card" data-lecture-section="card_consumers" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-top: 4px solid #3b82f6; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
                <div style="font-size: 28px; margin-bottom: 8px;">🛒</div>
                \\1''',
        html, count=1
    )

    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*1px solid #cbd5e1;\s*border-top:\s*4px solid #10b981;\s*border-radius:\s*10px;\s*padding:\s*20px;\s*box-shadow:\s*0 4px 6px rgba\(0,0,0,0.02\);[^"]*">\s*<div style="font-size: 28px; margin-bottom: 8px;">👷</div>\s*(<h4[^>]*>[^<]*</h4>)',
        '''<div id="card-workers" class="lecture-interactive-card" data-lecture-section="card_workers" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-top: 4px solid #10b981; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
                <div style="font-size: 28px; margin-bottom: 8px;">👷</div>
                \\1''',
        html, count=1
    )

    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*1px solid #cbd5e1;\s*border-top:\s*4px solid #f59e0b;\s*border-radius:\s*10px;\s*padding:\s*20px;\s*box-shadow:\s*0 4px 6px rgba\(0,0,0,0.02\);[^"]*">\s*<div style="font-size: 28px; margin-bottom: 8px;">🏭</div>\s*(<h4[^>]*>[^<]*</h4>)',
        '''<div id="card-producers" class="lecture-interactive-card" data-lecture-section="card_producers" style="background: #ffffff; border: 1.5px solid #fde68a; border-top: 4px solid #f59e0b; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #b45309; background: #fffbeb; padding: 2px 6px; border-radius: 8px; border: 1px solid #fde68a; pointer-events: none;">🎧 Nghe mục này</div>
                <div style="font-size: 28px; margin-bottom: 8px;">🏭</div>
                \\1''',
        html, count=1
    )

    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*1px solid #cbd5e1;\s*border-top:\s*4px solid #ef4444;\s*border-radius:\s*10px;\s*padding:\s*20px;\s*box-shadow:\s*0 4px 6px rgba\(0,0,0,0.02\);[^"]*">\s*<div style="font-size: 28px; margin-bottom: 8px;">🏛️</div>\s*(<h4[^>]*>[^<]*</h4>)',
        '''<div id="card-governments" class="lecture-interactive-card" data-lecture-section="card_governments" style="background: #ffffff; border: 1.5px solid #fca5a5; border-top: 4px solid #ef4444; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #b91c1c; background: #fef2f2; padding: 2px 6px; border-radius: 8px; border: 1px solid #fca5a5; pointer-events: none;">🎧 Nghe mục này</div>
                <div style="font-size: 28px; margin-bottom: 8px;">🏛️</div>
                \\1''',
        html, count=1
    )

    # Sec 3
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*3\.[^<]*</h2>)',
        '''<div id="sec-questions" class="lecture-interactive-card" data-lecture-section="sec_questions" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfeff; border: 1px solid #a5f3fc; border-radius: 20px; font-size: 12px; font-weight: 600; color: #0891b2; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # card-three-questions
    html = re.sub(
        r'<div style="display:\s*flex;\s*flex-direction:\s*column;\s*gap:\s*15px;">\s*<div style="background:\s*#f8fafc;\s*border-left:\s*5px solid #0284c7;\s*padding:\s*18px 22px;\s*border-radius:\s*0 10px 10px 0;">',
        '''<div id="card-three-questions" class="lecture-interactive-card" data-lecture-section="card_three_questions" style="display: flex; flex-direction: column; gap: 15px; border: 1.5px solid #bae6fd; border-radius: 12px; padding: 16px; background: #f0f9ff; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #0369a1; background: #e0f2fe; padding: 2px 8px; border-radius: 8px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>
            <div style="background: #ffffff; border-left: 5px solid #0284c7; padding: 18px 22px; border-radius: 0 10px 10px 0; border: 1px solid #e2e8f0; border-left-width: 5px;">''',
        html, count=1
    )

    # Sec 4
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*4\.[^<]*</h2>)',
        '''<div id="sec-distinctions" class="lecture-interactive-card" data-lecture-section="sec_distinctions" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # card-needs-wants
    html = re.sub(
        r'<div style="display:\s*flex;\s*flex-wrap:\s*wrap;\s*gap:\s*20px;\s*margin-bottom:\s*30px;">\s*<div style="flex:\s*1;\s*min-width:\s*300px;\s*background:\s*#fef2f2;\s*border:\s*1px solid #fca5a5;\s*border-radius:\s*12px;\s*padding:\s*20px;">',
        '''<div id="card-needs-wants" class="lecture-interactive-card" data-lecture-section="card_needs_wants" style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 30px; border: 1.5px solid #fbcfe8; border-radius: 14px; padding: 15px; background: #fff5f8; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #be185d; background: #fdf2f8; padding: 2px 8px; border-radius: 8px; border: 1px solid #fbcfe8; pointer-events: none;">🎧 Nghe mục này</div>
            <div style="flex: 1; min-width: 300px; background: #fef2f2; border: 1px solid #fca5a5; border-radius: 12px; padding: 20px;">''',
        html, count=1
    )

    # card-sectors
    html = re.sub(
        r'(?:<!--[^-]*-->\s*)?<div style="overflow-x:\s*auto;\s*background:\s*#ffffff;\s*border-radius:\s*12px;\s*border:\s*1px solid #e2e8f0;\s*box-shadow:\s*0 4px 6px rgba\(0,0,0,0.02\);[^"]*">',
        '''<div id="card-sectors" class="lecture-interactive-card" data-lecture-section="card_sectors" style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1.5px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease; padding-top: 10px;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #475569; background: #f1f5f9; padding: 2px 8px; border-radius: 8px; border: 1px solid #cbd5e1; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # Sec 5
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*5\.[^<]*</h2>)',
        '''<div id="sec-goods" class="lecture-interactive-card" data-lecture-section="sec_goods" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7c3aed; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # card-goods-comparison
    html = re.sub(
        r'<div style="display:\s*flex;\s*flex-wrap:\s*wrap;\s*gap:\s*20px;\s*margin-bottom:\s*25px;">\s*<div style="flex:\s*1;\s*min-width:\s*320px;\s*background:\s*#fdf4ff;\s*border:\s*1px solid #fbcfe8;\s*border-radius:\s*12px;\s*padding:\s*25px;">',
        '''<div id="card-goods-comparison" class="lecture-interactive-card" data-lecture-section="card_goods_comparison" style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 25px; border: 1.5px solid #e9d5ff; border-radius: 14px; padding: 15px; background: #faf5ff; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #f5f3ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #ddd6fe; pointer-events: none;">🎧 Nghe mục này</div>
            <div style="flex: 1; min-width: 320px; background: #fdf4ff; border: 1px solid #fbcfe8; border-radius: 12px; padding: 25px;">''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 2 (Page 2)
# =====================================================================
def build_p2_c2_html():
    with open('scripts/raw_econ/lec_2_p2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner_vi(1, "The Basic Economic Problem", "2. Các Yếu tố Sản xuất", "Đất đai, Lao động, Vốn, Doanh nhân, Tính Cơ động của Nguồn lực &amp; Năng lực Sản xuất")
    html = insert_banner(html, banner)

    # Sec 1
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*1\.[^<]*</h2>)',
        '''<div id="sec-factors" class="lecture-interactive-card" data-lecture-section="sec_factors" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # Sub-card: Interactive Factor Map
    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*2px solid #e2e8f0;\s*border-radius:\s*12px;\s*padding:\s*30px;\s*box-shadow:\s*0 10px 15px -3px rgba\(0,0,0,0.05\);\s*margin-bottom:\s*40px;">\s*(<h3[^>]*>[^<]*</h3>)',
        '''<div id="card-factors-grid" class="lecture-interactive-card" data-lecture-section="card_factors_grid" style="background: #ffffff; border: 2px solid #6ee7b7; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 8px; border-radius: 10px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
            \\1''',
        html, count=1
    )

    # Sub-card: Capital vs Money
    html = re.sub(
        r'(?:<!--[^-]*-->\s*)?<div style="background:\s*#eff6ff;\s*border-left:\s*4px solid #3b82f6;\s*padding:\s*18px 22px;\s*border-radius:\s*0 10px 10px 0;\s*margin-top:\s*25px;">',
        '''<div id="card-capital-distinction" class="lecture-interactive-card" data-lecture-section="card_capital_distinction" style="background: #eff6ff; border: 1.5px solid #bfdbfe; border-left: 5px solid #3b82f6; padding: 18px 22px; border-radius: 10px; margin-top: 25px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #ffffff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # Sec 2: Mobility
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*2\.[^<]*</h2>)',
        '''<div id="sec-mobility" class="lecture-interactive-card" data-lecture-section="sec_mobility" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # Sub-card: Factor mobility grid
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(280px,\s*1fr\)\);\s*gap:\s*20px;">\s*<div style="background:\s*#ffffff;\s*border:\s*1px solid #cbd5e1;\s*border-radius:\s*10px;\s*padding:\s*20px;\s*box-shadow:\s*0 4px 6px rgba\(0,0,0,0.02\);[^"]*">',
        '''<div id="card-mobility-types" class="lecture-interactive-card" data-lecture-section="card_mobility_types" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; border: 1.5px solid #fed7aa; border-radius: 14px; padding: 18px; background: #fffaf5; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #c2410c; background: #fff7ed; padding: 2px 8px; border-radius: 8px; border: 1px solid #fed7aa; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>
            <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">''',
        html, count=1
    )

    # Sec 3: Quantity & Quality
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*3\.[^<]*</h2>)',
        '''<div id="sec-quant-qual" class="lecture-interactive-card" data-lecture-section="sec_quant_qual" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # Sub-card: Table
    html = re.sub(
        r'<div style="overflow-x:\s*auto;\s*background:\s*#ffffff;\s*border-radius:\s*12px;\s*border:\s*1px solid #e2e8f0;\s*box-shadow:\s*0 4px 6px rgba\(0,0,0,0.02\);[^"]*">',
        '''<div id="card-quant-qual-table" class="lecture-interactive-card" data-lecture-section="card_quant_qual_table" style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1.5px solid #fbcfe8; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease; padding-top: 10px;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #be185d; background: #fdf2f8; padding: 2px 8px; border-radius: 8px; border: 1px solid #fbcfe8; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 3 (Page 2)
# =====================================================================
def build_p2_c3_html():
    with open('scripts/raw_econ/lec_3_p2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner_vi(1, "The Basic Economic Problem", "3. Chi phí Cơ hội", "Định nghĩa, Sự Đánh đổi trong Ra Quyết định &amp; Các Nguyên tắc Cốt lõi")
    html = insert_banner(html, banner)

    # Sec 1
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*1\.[^<]*</h2>)',
        '''<div id="sec-definition" class="lecture-interactive-card" data-lecture-section="sec_definition" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7c3aed; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # Sub-card: Definition box
    html = re.sub(
        r'<div style="background:\s*#f3e8ff;\s*border-left:\s*5px solid #9333ea;\s*padding:\s*25px;\s*border-radius:\s*0 12px 12px 0;\s*margin-bottom:\s*30px;\s*box-shadow:\s*0 4px 6px rgba\(0,0,0,0.02\);[^"]*">',
        '''<div id="card-definition" class="lecture-interactive-card" data-lecture-section="card_definition" style="background: #f3e8ff; border: 1.5px solid #d8b4fe; border-left: 6px solid #9333ea; padding: 25px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #ffffff; padding: 2px 8px; border-radius: 8px; border: 1px solid #d8b4fe; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # Sec 2
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*2\.[^<]*</h2>)',
        '''<div id="sec-decision-making" class="lecture-interactive-card" data-lecture-section="sec_decision_making" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # Sub-card: Interactive Decision Map
    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*2px solid #e2e8f0;\s*border-radius:\s*12px;\s*padding:\s*30px;\s*box-shadow:\s*0 10px 15px -3px rgba\(0,0,0,0.05\);\s*margin-bottom:\s*30px;">\s*(<h3[^>]*>[^<]*</h3>)',
        '''<div id="card-agent-tradeoffs" class="lecture-interactive-card" data-lecture-section="card_agent_tradeoffs" style="background: #ffffff; border: 2px solid #93c5fd; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 30px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 10px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
            \\1''',
        html, count=1
    )

    # Sec 3
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*3\.[^<]*</h2>)',
        '''<div id="sec-pitfalls" class="lecture-interactive-card" data-lecture-section="sec_pitfalls" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 4 (Page 2)
# =====================================================================
def build_p2_c4_html():
    with open('scripts/raw_econ/lec_4_p2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner_vi(1, "The Basic Economic Problem", "4. Đường Giới hạn Khả năng Sản xuất (PPC)", "Đường biên PPC, Toàn dụng Nguồn lực, Chi phí Cơ hội Tăng dần vs Không đổi &amp; Sự Dịch chuyển")
    html = insert_banner(html, banner)

    # Sec 1
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*1\.[^<]*</h2>)',
        '''<div id="sec-ppc-intro" class="lecture-interactive-card" data-lecture-section="sec_ppc_intro" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 20px; font-size: 12px; font-weight: 600; color: #0369a1; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # Sub-card: Points A, B, C
    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*2px solid #e2e8f0;\s*border-radius:\s*12px;\s*padding:\s*30px;\s*box-shadow:\s*0 10px 15px -3px rgba\(0,0,0,0.05\);\s*margin-bottom:\s*40px;">\s*(<h3[^>]*>[^<]*</h3>)',
        '''<div id="card-ppc-points" class="lecture-interactive-card" data-lecture-section="card_ppc_points" style="background: #ffffff; border: 2px solid #7dd3fc; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #0369a1; background: #f0f9ff; padding: 2px 8px; border-radius: 10px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>
            \\1''',
        html, count=1
    )

    # Sec 2
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*2\.[^<]*</h2>)',
        '''<div id="sec-movements" class="lecture-interactive-card" data-lecture-section="sec_movements" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # Sub-card: Reallocation
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(280px,\s*1fr\)\);\s*gap:\s*20px;\s*margin-bottom:\s*25px;">\s*<div style="background:\s*#f8fafc;\s*border:\s*1px solid #cbd5e1;\s*border-radius:\s*10px;\s*padding:\s*20px;">',
        '''<div id="card-movements" class="lecture-interactive-card" data-lecture-section="card_movements" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 25px; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 18px; background: #f0fdf4; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 8px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>
            <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; padding: 20px;">''',
        html, count=1
    )

    # Sec 3: Shape
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*3\.[^<]*</h2>)',
        '''<div id="sec-shape" class="lecture-interactive-card" data-lecture-section="sec_shape" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # Sec 4: Shifts
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*(<h2[^>]*>[^<]*4\.[^<]*</h2>)',
        '''<div id="sec-shifts" class="lecture-interactive-card" data-lecture-section="sec_shifts" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        \\1''',
        html, count=1
    )

    # Sub-card: Growth comparison
    html = re.sub(
        r'(?:<!--[^-]*-->\s*)?<div style="background:\s*#fffbeb;\s*border:\s*1px solid #fde047;\s*border-radius:\s*10px;\s*padding:\s*20px;\s*margin-top:\s*25px;">',
        '''<div id="card-shifts-comparison" class="lecture-interactive-card" data-lecture-section="card_shifts_comparison" style="background: #fffbeb; border: 1.5px solid #fde047; border-radius: 12px; padding: 20px; margin-top: 25px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #92400e; background: #ffffff; padding: 2px 8px; border-radius: 8px; border: 1px solid #fde047; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    return html

build_c2_p2_html = build_p2_c2_html
build_c3_p2_html = build_p2_c3_html
build_c4_p2_html = build_p2_c4_html


def verify_all_topic1_p2():
    builders = [
        (1, build_c1_p2_html),
        (2, build_p2_c2_html),
        (3, build_p2_c3_html),
        (4, build_p2_c4_html),
    ]
    all_ok = True
    for lec_num, builder in builders:
        html = builder()
        diff = html.count('<div') - html.count('</div')
        with open(f'public/audio/lectures/economics/{lec_num}/manifest.json', 'r', encoding='utf-8') as f:
            mf = json.load(f)
        soup = BeautifulSoup(html, 'html.parser')
        missing = []
        for s in mf['segments']:
            el = soup.select_one(s['selector'])
            if not el:
                missing.append(s['id'])
        if missing or diff != 0:
            all_ok = False
            print(f"❌ Lec {lec_num}: diff={diff}, missing={missing}")
        else:
            print(f"✅ Lec {lec_num}: 100% MATCH ({len(mf['segments'])} segments, diff=0)")
    return all_ok

if __name__ == '__main__':
    verify_all_topic1_p2()
