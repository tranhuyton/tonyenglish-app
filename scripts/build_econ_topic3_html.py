import os
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def strip_study_resources(html):
    pattern = r'<!--\s*(?:Thanh Tài liệu học tập|Study Resources Bar)[^>]*-->\s*<div[^>]*>.*?</div>\s*'
    html = re.sub(pattern, '', html, flags=re.DOTALL)
    html = re.sub(r'<div[^>]*id=[\'"]study-resources-bar[\'"][^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)
    html = re.sub(r'<div[^>]*class=[\'"][^\'"]*study-resources[^\'"]*[\'"][^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)
    return html

def make_banner(topic_num, topic_title, lec_title, lec_desc):
    return f'''<!-- Lecture Top Banner & Controls -->
    <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); border-radius: 16px; padding: 30px; margin-bottom: 35px; color: white; box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.4); position: relative; border: 1.5px solid #60a5fa; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: rgba(255,255,255,0.2); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.35); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
            <span style="background: rgba(255, 255, 255, 0.2); padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 600; letter-spacing: 0.5px; text-transform: uppercase;">Topic {topic_num}: {topic_title}</span>
            <span style="background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.4); padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600;">Cambridge IGCSE</span>
        </div>
        <h1 style="font-size: 32px; font-weight: 800; margin: 0 0 10px 0; line-height: 1.25; color: #ffffff;">{lec_title}</h1>
        <p style="font-size: 16px; opacity: 0.9; margin: 0; line-height: 1.5; color: #e0f2fe; max-width: 850px;">{lec_desc}</p>
    </div>'''

def insert_banner(html, banner):
    m = re.search(r'<div style="[^"]*(?:font-family|max-width)[^"]*>', html)
    if m:
        pos = m.end()
        return html[:pos] + "\n\n    " + banner + "\n" + html[pos:]
    return banner + "\n" + html

# =====================================================================
# LECTURE 16 HTML BUILDER
# =====================================================================
def build_c16_html():
    with open('scripts/raw_econ/lec_16_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(3, "Microeconomic Decision Makers", "16. Money and Banking", "Evolution of Money, Four Functions, Characteristics &amp; Banking Roles")
    html = insert_banner(html, banner)

    # 1. Evolution
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*1\.\s*THE EVOLUTION\s*(?:&amp;|&)\s*FORMS OF MONEY',
        '''<div id="sec-evolution" class="lecture-interactive-card" data-lecture-section="sec_evolution" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">💸 1. THE EVOLUTION &amp; FORMS OF MONEY</h2>''',
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
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*2\.\s*FUNCTIONS\s*(?:&amp;|&)\s*CHARACTERISTICS OF MONEY',
        '''<div id="sec-functions" class="lecture-interactive-card" data-lecture-section="sec_functions" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🔍 2. FUNCTIONS &amp; CHARACTERISTICS OF MONEY</h2>''',
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
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*3\.\s*THE BANKING SYSTEM',
        '''<div id="sec-banking" class="lecture-interactive-card" data-lecture-section="sec_banking" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🏦 3. THE BANKING SYSTEM: CENTRAL BANK VS COMMERCIAL BANKS</h2>''',
        html, count=1
    )

    # card-central-bank
    html = re.sub(
        r'<!-- Central Bank -->\s*<div style="background: #ffffff; border: 2px solid #fed7aa; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);[^"]*">',
        '''<!-- Central Bank -->
        <div id="card-central-bank" class="lecture-interactive-card" data-lecture-section="card_central_bank" style="background: #ffffff; border: 2px solid #fed7aa; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #c2410c; background: #fff7ed; padding: 2px 8px; border-radius: 8px; border: 1px solid #fed7aa; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # card-commercial-bank
    html = re.sub(
        r'<!-- Commercial Bank -->\s*<div style="background: #ffffff; border: 2px solid #bfdbfe; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);[^"]*">',
        '''<!-- Commercial Bank -->
        <div id="card-commercial-bank" class="lecture-interactive-card" data-lecture-section="card_commercial_bank" style="background: #ffffff; border: 2px solid #bfdbfe; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # 4. Exam Focus
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*4\.\s*EXAM FOCUS',
        '''<div id="sec-borrowing" class="lecture-interactive-card" data-lecture-section="sec_borrowing" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🔥 4. EXAM FOCUS: WHY FIRMS STRUGGLE TO BORROW</h2>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 17 HTML BUILDER
# =====================================================================
def build_c17_html():
    with open('scripts/raw_econ/lec_17_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(3, "Microeconomic Decision Makers", "17. Households: Income, Saving, Borrowing &amp; Spending", "Determinants of Consumption, Motives for Saving &amp; Borrowing Factors")
    html = insert_banner(html, banner)

    # 1. Spending
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*1\.\s*HOUSEHOLD SPENDING',
        '''<div id="sec-spending" class="lecture-interactive-card" data-lecture-section="sec_spending" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🛒 1. HOUSEHOLD SPENDING (CONSUMPTION)</h2>''',
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
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*2\.\s*HOUSEHOLD SAVING',
        '''<div id="sec-saving" class="lecture-interactive-card" data-lecture-section="sec_saving" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">💰 2. HOUSEHOLD SAVING</h2>''',
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
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*3\.\s*HOUSEHOLD BORROWING',
        '''<div id="sec-borrowing" class="lecture-interactive-card" data-lecture-section="sec_borrowing" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #ffedd5; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">💳 3. HOUSEHOLD BORROWING</h2>''',
        html, count=1
    )

    # 4. Wealth Exam Focus
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*4\.\s*EXAM FOCUS',
        '''<div id="sec-wealth" class="lecture-interactive-card" data-lecture-section="sec_wealth" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🔥 4. EXAM FOCUS: SPENDING, SAVING &amp; WEALTH</h2>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 18 HTML BUILDER
# =====================================================================
def build_c18_html():
    with open('scripts/raw_econ/lec_18_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(3, "Microeconomic Decision Makers", "18. Workers: Wage Determination &amp; Mobility", "Occupational Choice, Labour Demand &amp; Supply, Minimum Wage &amp; Wage Differentials")
    html = insert_banner(html, banner)

    # 1. Occupation
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*1\.\s*CHOOSING AN OCCUPATION',
        '''<div id="sec-occupation" class="lecture-interactive-card" data-lecture-section="sec_occupation" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">💼 1. CHOOSING AN OCCUPATION</h2>''',
        html, count=1
    )

    # card-wage-factors
    html = re.sub(
        r'<!-- Wage Factors -->\s*<div style="background: #ffffff; border: 1px solid #bfdbfe; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);[^"]*">',
        '''<!-- Wage Factors -->
        <div id="card-wage-factors" class="lecture-interactive-card" data-lecture-section="card_wage_factors" style="background: #ffffff; border: 1.5px solid #3b82f6; border-radius: 12px; padding: 25px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # card-non-wage-factors
    html = re.sub(
        r'<!-- Non-wage Factors -->\s*<div style="background: #ffffff; border: 1px solid #bbf7d0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);[^"]*">',
        '''<!-- Non-wage Factors -->
        <div id="card-non-wage-factors" class="lecture-interactive-card" data-lecture-section="card_non_wage_factors" style="background: #ffffff; border: 1.5px solid #10b981; border-radius: 12px; padding: 25px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 8px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # 2. Wage determination
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*2\.\s*WAGE DETERMINATION',
        '''<div id="sec-wage-determination" class="lecture-interactive-card" data-lecture-section="sec_wage_determination" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 2. WAGE DETERMINATION IN THE LABOUR MARKET</h2>''',
        html, count=1
    )

    # 3. Minimum wage
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*3\.\s*NATIONAL MINIMUM WAGE',
        '''<div id="sec-nmw" class="lecture-interactive-card" data-lecture-section="sec_nmw" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🛑 3. NATIONAL MINIMUM WAGE (NMW)</h2>''',
        html, count=1
    )

    # 4. Differentials
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*4\.\s*DIFFERENCES IN EARNINGS',
        '''<div id="sec-wage-differentials" class="lecture-interactive-card" data-lecture-section="sec_wage_differentials" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📊 4. DIFFERENCES IN EARNINGS (WAGE DIFFERENTIALS)</h2>''',
        html, count=1
    )

    # 5. Mobility & Division
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*5\.\s*LABOUR MOBILITY',
        '''<div id="sec-mobility-division" class="lecture-interactive-card" data-lecture-section="sec_mobility_division" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfeff; border: 1px solid #a5f3fc; border-radius: 20px; font-size: 12px; font-weight: 600; color: #0891b2; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #06b6d4; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🔄 5. LABOUR MOBILITY &amp; DIVISION OF LABOUR</h2>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 19 HTML BUILDER
# =====================================================================
def build_c19_html():
    with open('scripts/raw_econ/lec_19_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(3, "Microeconomic Decision Makers", "19. Trade Unions", "Definition, Types, Industrial Action, Bargaining Power &amp; Economic Evaluation")
    html = insert_banner(html, banner)

    # 1. Union Intro
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*1\.\s*WHAT IS A TRADE UNION',
        '''<div id="sec-union-intro" class="lecture-interactive-card" data-lecture-section="sec_union_intro" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🤝 1. WHAT IS A TRADE UNION?</h2>''',
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
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*2\.\s*FORMS OF INDUSTRIAL ACTION',
        '''<div id="sec-industrial-action" class="lecture-interactive-card" data-lecture-section="sec_industrial_action" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #ffedd5; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚠️ 2. FORMS OF INDUSTRIAL ACTION</h2>''',
        html, count=1
    )

    # 3. Bargaining Power
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*3\.\s*BARGAINING POWER',
        '''<div id="sec-bargaining-power" class="lecture-interactive-card" data-lecture-section="sec_bargaining_power" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📈 3. BARGAINING POWER &amp; LABOUR MARKET IMPACT</h2>''',
        html, count=1
    )

    # 4. Evaluation
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*4\.\s*EVALUATION',
        '''<div id="sec-evaluation" class="lecture-interactive-card" data-lecture-section="sec_evaluation" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 4. EVALUATION: COSTS &amp; BENEFITS OF TRADE UNIONS</h2>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 20 HTML BUILDER
# =====================================================================
def build_c20_html():
    with open('scripts/raw_econ/lec_20_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(3, "Microeconomic Decision Makers", "20. Firms: Size, Growth &amp; Integration", "Sector Classification, Small vs Large Firms, Mergers &amp; Economies of Scale")
    html = insert_banner(html, banner)

    # 1. Classification
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*1\.\s*CLASSIFICATION &amp; TYPES OF FIRMS',
        '''<div id="sec-classification" class="lecture-interactive-card" data-lecture-section="sec_classification" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🏢 1. CLASSIFICATION &amp; TYPES OF FIRMS</h2>''',
        html, count=1
    )

    # 2. Firm Size
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*2\.\s*SIZES OF FIRMS',
        '''<div id="sec-firm-size" class="lecture-interactive-card" data-lecture-section="sec_firm_size" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📏 2. SIZES OF FIRMS: SMALL VS LARGE FIRMS</h2>''',
        html, count=1
    )

    # card-small-vs-large
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(320px,\s*1fr\)\); gap: 25px; margin-bottom:\s*(?:30px|35px);">\s*<!-- Small Firms -->',
        '''<div id="card-small-vs-large" class="lecture-interactive-card" data-lecture-section="card_small_vs_large" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px; margin-bottom: 30px; border: 1.5px solid #cbd5e1; border-radius: 14px; padding: 18px; background: #f8fafc; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #475569; background: #ffffff; padding: 2px 8px; border-radius: 8px; border: 1px solid #cbd5e1; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>
            <!-- Small Firms -->''',
        html, count=1
    )

    # 3. Mergers & Integration
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*3\.\s*MERGERS &amp; INTEGRATION',
        '''<div id="sec-integration" class="lecture-interactive-card" data-lecture-section="sec_integration" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🤝 3. MERGERS &amp; INTEGRATION (SYLLABUS 3.4.2)</h2>''',
        html, count=1
    )

    # 4. Economies of Scale
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*4\.\s*ECONOMIES &amp; DISECONOMIES OF SCALE',
        '''<div id="sec-economies-scale" class="lecture-interactive-card" data-lecture-section="sec_economies_scale" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📉 4. ECONOMIES &amp; DISECONOMIES OF SCALE (SYLLABUS 3.4.3)</h2>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 21 HTML BUILDER
# =====================================================================
def build_c21_html():
    with open('scripts/raw_econ/lec_21_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(3, "Microeconomic Decision Makers", "21. Firms and Production: Factor Demand &amp; Costs", "Derived Factor Demand, Production Intensity, Output vs Productivity &amp; Costs")
    html = insert_banner(html, banner)

    # 1. Factor Demand
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*1\.\s*DEMAND FOR FACTORS OF PRODUCTION',
        '''<div id="sec-factor-demand" class="lecture-interactive-card" data-lecture-section="sec_factor_demand" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚙️ 1. DEMAND FOR FACTORS OF PRODUCTION (SYLLABUS 3.5.1)</h2>''',
        html, count=1
    )

    # 2. Intensity
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*2\.\s*LABOUR-INTENSIVE VS CAPITAL-INTENSIVE',
        '''<div id="sec-intensity" class="lecture-interactive-card" data-lecture-section="sec_intensity" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🏭 2. LABOUR-INTENSIVE VS CAPITAL-INTENSIVE PRODUCTION</h2>''',
        html, count=1
    )

    # 3. Productivity
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*3\.\s*PRODUCTION VS PRODUCTIVITY',
        '''<div id="sec-productivity" class="lecture-interactive-card" data-lecture-section="sec_productivity" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚡ 3. PRODUCTION VS PRODUCTIVITY (SYLLABUS 3.5.3)</h2>''',
        html, count=1
    )

    # 4. Short-Run Costs
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*4\.\s*SHORT-RUN COSTS OF PRODUCTION',
        '''<div id="sec-short-run-costs" class="lecture-interactive-card" data-lecture-section="sec_short_run_costs" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">💰 4. SHORT-RUN COSTS OF PRODUCTION</h2>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 22 HTML BUILDER
# =====================================================================
def build_c22_html():
    with open('scripts/raw_econ/lec_22_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(3, "Microeconomic Decision Makers", "22. Firms' Objectives, Costs, Revenue &amp; Break-even", "Business Goals, Cost Formulas, Calculation Tables &amp; Break-even Analysis")
    html = insert_banner(html, banner)

    # 1. Objectives
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*1\.\s*OBJECTIVES OF FIRMS',
        '''<div id="sec-objectives" class="lecture-interactive-card" data-lecture-section="sec_objectives" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🎯 1. OBJECTIVES OF FIRMS (SYLLABUS 3.6.5)</h2>''',
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
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*2\.\s*COSTS OF PRODUCTION',
        '''<div id="sec-formulas" class="lecture-interactive-card" data-lecture-section="sec_formulas" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🧮 2. COSTS OF PRODUCTION: DEFINITIONS &amp; FORMULAS</h2>''',
        html, count=1
    )

    # 3. Revenue & Break-even
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*3\.\s*REVENUE,\s*PROFIT &amp; BREAK-EVEN',
        '''<div id="sec-revenue-breakeven" class="lecture-interactive-card" data-lecture-section="sec_revenue_breakeven" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📊 3. REVENUE, PROFIT &amp; BREAK-EVEN ANALYSIS</h2>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 23 HTML BUILDER
# =====================================================================
def build_c23_html():
    with open('scripts/raw_econ/lec_23_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(3, "Microeconomic Decision Makers", "23. Market Structure: Competition vs Monopoly", "Competitive Markets vs Pure Monopoly, Pricing Power &amp; Welfare Evaluation")
    html = insert_banner(html, banner)

    # 1. Competition vs Monopoly
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*1\.\s*COMPETITIVE MARKETS VS MONOPOLY',
        '''<div id="sec-competition-vs-monopoly" class="lecture-interactive-card" data-lecture-section="sec_competition_vs_monopoly" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 1. COMPETITIVE MARKETS VS MONOPOLY (SYLLABUS 3.7)</h2>''',
        html, count=1
    )

    # card-comparison-table (Section 2 is the comparison table)
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*2\.\s*THE FOUR KEY DIMENSIONS',
        '''<div id="card-comparison-table" class="lecture-interactive-card" data-lecture-section="card_comparison_table" style="background: white; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 20px; font-size: 12px; font-weight: 600; color: #475569; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📊 2. THE FOUR KEY DIMENSIONS: COMPARISON TABLE</h2>''',
        html, count=1
    )

    # 3. Impact on Price & Output
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*3\.\s*HOW COMPETITION IMPACTS PRICE &amp; OUTPUT',
        '''<div id="sec-impact-price-output" class="lecture-interactive-card" data-lecture-section="sec_impact_price_output" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📉 3. HOW COMPETITION IMPACTS PRICE &amp; OUTPUT</h2>''',
        html, count=1
    )

    # 4. Evaluating Monopoly
    html = re.sub(
        r'<div style="margin-bottom:\s*(?:50px|40px);">\s*<h2[^>]*>[^<]*4\.\s*EVALUATING MONOPOLY',
        '''<div id="sec-evaluating-monopoly" class="lecture-interactive-card" data-lecture-section="sec_evaluating_monopoly" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🔥 4. EVALUATING MONOPOLY: ARE THEY ALWAYS BAD FOR CONSUMERS?</h2>''',
        html, count=1
    )

    return html
