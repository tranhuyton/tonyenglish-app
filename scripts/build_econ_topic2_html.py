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
    m = re.search(r'<div style="max-width:\s*900px;\s*margin:\s*0 auto;\s*padding:\s*20px;\s*font-family:[^>]*>', html)
    if m:
        pos = m.end()
        return html[:pos] + "\n\n    " + banner + "\n" + html[pos:]
    return banner + "\n" + html

# =====================================================================
# LECTURE 5 HTML BUILDER
# =====================================================================
def build_c5_html():
    with open('scripts/raw_econ/lec_5_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = strip_study_resources(html)
    banner = make_banner(2, "The Allocation Of Resources", "5. Microeconomics and Macroeconomics", "Differences, Main Decision-Makers &amp; Their Economic Aims")
    html = insert_banner(html, banner)

    # Sec 1: Micro vs Macro
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*1\.\s*MICROECONOMICS',
        '''<div id="sec-micro-macro" class="lecture-interactive-card" data-lecture-section="sec_micro_macro" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 1. MICROECONOMICS &amp; MACROECONOMICS</h2>''',
        html, count=1
    )

    # Sub-card: Micro
    html = re.sub(
        r'<div style="flex:\s*1;\s*min-width:\s*320px;\s*background:\s*#eff6ff;\s*border:\s*1px solid #bfdbfe;[^>]*>',
        '''<div id="card-micro" class="lecture-interactive-card" data-lecture-section="card_micro" style="flex: 1; min-width: 320px; background: #eff6ff; border: 1.5px solid #3b82f6; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #ffffff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # Sub-card: Macro
    html = re.sub(
        r'<div style="flex:\s*1;\s*min-width:\s*320px;\s*background:\s*#fdf4ff;\s*border:\s*1px solid #f5d0fe;[^>]*>',
        '''<div id="card-macro" class="lecture-interactive-card" data-lecture-section="card_macro" style="flex: 1; min-width: 320px; background: #fdf4ff; border: 1.5px solid #a855f7; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #7e22ce; background: #faf5ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #f5d0fe; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # Sub-card: Comparison Table
    html = re.sub(
        r'<div style="overflow-x:\s*auto;\s*background:\s*#ffffff;\s*border-radius:\s*12px;\s*border:\s*1px solid #e2e8f0;[^>]*>',
        '''<div id="card-criteria-table" class="lecture-interactive-card" data-lecture-section="card_criteria_table" style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1.5px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease; padding-top: 10px;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #475569; background: #f1f5f9; padding: 2px 8px; border-radius: 8px; border: 1px solid #cbd5e1; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # Sec 2: Decision makers
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*2\.\s*ECONOMIC DECISION-MAKERS',
        '''<div id="sec-decision-makers" class="lecture-interactive-card" data-lecture-section="sec_decision_makers" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">👥 2. ECONOMIC DECISION-MAKERS &amp; THEIR AIMS</h2>''',
        html, count=1
    )

    # Sub-cards: Households, Firms, Government
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #cbd5e1; border-top: 4px solid #3b82f6; border-radius: 10px; padding: 22px;">\s*<div style="font-size: 28px; margin-bottom: 8px;">🛒</div>\s*<h4 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px;">Households / Consumers</h4>',
        '''<div id="card-households" class="lecture-interactive-card" data-lecture-section="card_households" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-top: 4px solid #3b82f6; border-radius: 10px; padding: 22px; cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
                <div style="font-size: 28px; margin-bottom: 8px;">🛒</div>
                <h4 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px;">Households / Consumers</h4>''',
        html
    )

    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #cbd5e1; border-top: 4px solid #f59e0b; border-radius: 10px; padding: 22px;">\s*<div style="font-size: 28px; margin-bottom: 8px;">🏭</div>\s*<h4 style="margin: 0 0 8px 0; color: #92400e; font-size: 18px;">Firms / Producers</h4>',
        '''<div id="card-firms" class="lecture-interactive-card" data-lecture-section="card_firms" style="background: #ffffff; border: 1.5px solid #fde68a; border-top: 4px solid #f59e0b; border-radius: 10px; padding: 22px; cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #b45309; background: #fffbeb; padding: 2px 6px; border-radius: 8px; border: 1px solid #fde68a; pointer-events: none;">🎧 Nghe mục này</div>
                <div style="font-size: 28px; margin-bottom: 8px;">🏭</div>
                <h4 style="margin: 0 0 8px 0; color: #92400e; font-size: 18px;">Firms / Producers</h4>''',
        html
    )

    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #cbd5e1; border-top: 4px solid #ef4444; border-radius: 10px; padding: 22px;">\s*<div style="font-size: 28px; margin-bottom: 8px;">🏛️</div>\s*<h4 style="margin: 0 0 8px 0; color: #991b1b; font-size: 18px;">Government</h4>',
        '''<div id="card-government" class="lecture-interactive-card" data-lecture-section="card_government" style="background: #ffffff; border: 1.5px solid #fca5a5; border-top: 4px solid #ef4444; border-radius: 10px; padding: 22px; cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #b91c1c; background: #fef2f2; padding: 2px 6px; border-radius: 8px; border: 1px solid #fca5a5; pointer-events: none;">🎧 Nghe mục này</div>
                <div style="font-size: 28px; margin-bottom: 8px;">🏛️</div>
                <h4 style="margin: 0 0 8px 0; color: #991b1b; font-size: 18px;">Government</h4>''',
        html
    )

    return html

# =====================================================================
# LECTURE 6 HTML BUILDER
# =====================================================================
def build_c6_html():
    with open('scripts/raw_econ/lec_6_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = strip_study_resources(html)
    banner = make_banner(2, "The Allocation Of Resources", "6. The Role of Market in Allocating Resources", "Market Types, Price Mechanism Functions &amp; Economic Systems Spectrum")
    html = insert_banner(html, banner)

    # Sec 1: Market work
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*1\.\s*WHAT IS A MARKET',
        '''<div id="sec-market-work" class="lecture-interactive-card" data-lecture-section="sec_market_work" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 30px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🛒 1. WHAT IS A MARKET &amp; HOW MARKETS WORK</h2>''',
        html, count=1
    )

    # card-market-types
    html = re.sub(
        r'<!-- Market Types Grid -->\s*<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(280px,\s*1fr\)\);[^>]*>',
        '''<!-- Market Types Grid -->
        <div id="card-market-types" class="lecture-interactive-card" data-lecture-section="card_market_types" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 30px; border: 1.5px solid #bfdbfe; border-radius: 14px; padding: 18px; background: #f8fafc; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # card-participants
    html = re.sub(
        r'<!-- Roles of Buyers and Sellers -->\s*<div style="background:\s*#f8fafc;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*10px;\s*padding:\s*20px;\">',
        '''<!-- Roles of Buyers and Sellers -->
        <div id="card-participants" class="lecture-interactive-card" data-lecture-section="card_participants" style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 20px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #475569; background: #ffffff; padding: 2px 8px; border-radius: 8px; border: 1px solid #cbd5e1; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # Sec 2: Allocation decisions
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*2\.\s*THE THREE FUNDAMENTAL RESOURCE ALLOCATION DECISIONS',
        '''<div id="sec-allocation-decisions" class="lecture-interactive-card" data-lecture-section="sec_allocation_decisions" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 30px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">❓ 2. THE THREE FUNDAMENTAL RESOURCE ALLOCATION DECISIONS</h2>''',
        html, count=1
    )

    # card-how-to-produce
    html = re.sub(
        r'<div style="background:\s*#f8fafc;\s*border:\s*1px solid #cbd5e1;\s*border-radius:\s*10px;\s*padding:\s*25px;">\s*<h3[^>]*>[^<]*Resolving "How to Produce"',
        '''<div id="card-how-to-produce" class="lecture-interactive-card" data-lecture-section="card_how_to_produce" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 12px; padding: 25px; cursor: pointer; position: relative; transition: all 0.2s ease; margin-bottom: 25px;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 8px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 15px;">🔧 Resolving "How to Produce": Capital vs. Labour Intensity</h3>''',
        html, count=1
    )

    # Sec 3: Price mechanism
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*3\.\s*THE PRICE MECHANISM &amp; RESOURCE ALLOCATION',
        '''<div id="sec-price-mechanism" class="lecture-interactive-card" data-lecture-section="sec_price_mechanism" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 30px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7c3aed; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📈 3. THE PRICE MECHANISM &amp; RESOURCE ALLOCATION</h2>''',
        html, count=1
    )

    # card-price-functions
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(280px,\s*1fr\)\); gap: 20px; margin-bottom: 30px;">',
        '''<div id="card-price-functions" class="lecture-interactive-card" data-lecture-section="card_price_functions" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 30px; border: 1.5px solid #d8b4fe; border-radius: 14px; padding: 18px; background: #faf5ff; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #f5f3ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #ddd6fe; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # card-price-in-action
    html = re.sub(
        r'<div style="background:\s*#f8fafc;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*10px;\s*padding:\s*25px;">\s*<h3[^>]*>[^<]*The Price Mechanism in Action',
        '''<div id="card-price-in-action" class="lecture-interactive-card" data-lecture-section="card_price_in_action" style="background: #ffffff; border: 1.5px solid #86efac; border-radius: 12px; padding: 25px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #15803d; background: #ffffff; padding: 2px 8px; border-radius: 8px; border: 1px solid #86efac; pointer-events: none;">🎧 Nghe mục này</div>
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 15px;">🔍 The Price Mechanism in Action: Shift Analysis</h3>''',
        html, count=1
    )

    # Sec 4: Economic systems
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*4\.\s*THE SPECTRUM OF ECONOMIC SYSTEMS',
        '''<div id="sec-economic-systems" class="lecture-interactive-card" data-lecture-section="sec_economic_systems" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 4. THE SPECTRUM OF ECONOMIC SYSTEMS</h2>''',
        html, count=1
    )

    # card-economic-spectrum
    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*2px solid #e2e8f0;[^>]*>\s*<h3[^>]*>Interactive Economic Systems Spectrum',
        '''<div id="card-economic-spectrum" class="lecture-interactive-card" data-lecture-section="card_economic_spectrum" style="background: #ffffff; border: 2px solid #f472b6; border-radius: 12px; padding: 25px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #be185d; background: #fdf2f8; padding: 2px 8px; border-radius: 10px; border: 1px solid #fbcfe8; pointer-events: none;">🎧 Nghe mục này</div>
            <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 20px; margin-bottom: 10px;">Interactive Economic Systems Spectrum</h3>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 7 HTML BUILDER
# =====================================================================
def build_c7_html():
    with open('scripts/raw_econ/lec_7_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = strip_study_resources(html)
    banner = make_banner(2, "The Allocation Of Resources", "7. Demand", "Definition, Law of Demand, Movements vs Shifts &amp; Non-Price Determinants")
    html = insert_banner(html, banner)

    # Sec 1: What is demand?
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*1\.\s*WHAT IS DEMAND',
        '''<div id="sec-demand-intro" class="lecture-interactive-card" data-lecture-section="sec_demand_intro" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 30px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🛒 1. WHAT IS DEMAND?</h2>''',
        html, count=1
    )

    # card-law-of-demand
    html = re.sub(
        r'<!-- Two Columns: Law of Demand & Individual vs Market -->\s*<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(320px,\s*1fr\)\); gap: 25px; margin-bottom: 30px;">',
        '''<!-- Two Columns: Law of Demand & Individual vs Market -->
        <div id="card-law-of-demand" class="lecture-interactive-card" data-lecture-section="card_law_of_demand" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px; margin-bottom: 30px; border: 1.5px solid #bfdbfe; border-radius: 14px; padding: 18px; background: #f8fafc; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # Sec 2: Movements
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*2\.\s*MOVEMENTS ALONG A DEMAND CURVE',
        '''<div id="sec-movements" class="lecture-interactive-card" data-lecture-section="sec_movements" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 30px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📉 2. MOVEMENTS ALONG A DEMAND CURVE</h2>''',
        html, count=1
    )

    # card-movements
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(320px,\s*1fr\)\); gap: 25px; align-items: center; margin-bottom: 25px;">',
        '''<div id="card-movements" class="lecture-interactive-card" data-lecture-section="card_movements" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px; align-items: center; margin-bottom: 25px; border: 1.5px solid #fed7aa; border-radius: 14px; padding: 18px; background: #fffaf5; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #c2410c; background: #fff7ed; padding: 2px 8px; border-radius: 8px; border: 1px solid #fed7aa; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # Sec 3: Shifts
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*3\.\s*SHIFTS IN THE DEMAND CURVE',
        '''<div id="sec-shifts" class="lecture-interactive-card" data-lecture-section="sec_shifts" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 30px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🚀 3. SHIFTS IN THE DEMAND CURVE</h2>''',
        html, count=1
    )

    # Sec 4: Determinants
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*4\.\s*DETERMINANTS OF DEMAND',
        '''<div id="sec-determinants" class="lecture-interactive-card" data-lecture-section="sec_determinants" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🧠 4. DETERMINANTS OF DEMAND (NON-PRICE FACTORS)</h2>''',
        html, count=1
    )

    # card-determinants (Table)
    html = re.sub(
        r'<!-- Table of PASIFIC Determinants -->\s*<div style="overflow-x:\s*auto;">',
        '''<!-- Table of PASIFIC Determinants -->
        <div id="card-determinants" class="lecture-interactive-card" data-lecture-section="card_determinants" style="overflow-x: auto; border: 1.5px solid #fbcfe8; border-radius: 14px; padding: 18px; background: #fff5f8; cursor: pointer; position: relative; transition: all 0.2s ease; margin-bottom: 30px;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #be185d; background: #fdf2f8; padding: 2px 8px; border-radius: 8px; border: 1px solid #fbcfe8; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 8 HTML BUILDER
# =====================================================================
def build_c8_html():
    with open('scripts/raw_econ/lec_8_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = strip_study_resources(html)
    banner = make_banner(2, "The Allocation Of Resources", "8. Supply", "Definition, Law of Supply, Movements along Curve &amp; Non-Price Determinants")
    html = insert_banner(html, banner)

    # Sec 1
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*1\.\s*WHAT IS SUPPLY',
        '''<div id="sec-supply-intro" class="lecture-interactive-card" data-lecture-section="sec_supply_intro" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📦 1. WHAT IS SUPPLY?</h2>''',
        html, count=1
    )

    # card-law-of-supply
    html = re.sub(
        r'<div style="flex:\s*1;\s*min-width:\s*320px;\s*background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*12px;\s*padding:\s*25px;\s*box-shadow:\s*0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3[^>]*>[^<]*The Law of Supply</h3>',
        '''<div id="card-law-of-supply" class="lecture-interactive-card" data-lecture-section="card_law_of_supply" style="flex: 1; min-width: 320px; background: #ffffff; border: 2px solid #3b82f6; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
                <h3 style="margin: 0 0 15px 0; color: #1d4ed8; font-size: 20px;">⚖️ The Law of Supply</h3>''',
        html, count=1
    )

    # Sec 2: Movements
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*2\.\s*MOVEMENTS ALONG THE SUPPLY CURVE',
        '''<div id="sec-movements" class="lecture-interactive-card" data-lecture-section="sec_movements" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📈 2. MOVEMENTS ALONG THE SUPPLY CURVE</h2>''',
        html, count=1
    )

    # card-movements
    html = re.sub(
        r'<div style="background:\s*#ffffff;\s*border:\s*2px solid #e2e8f0;\s*border-radius:\s*12px;\s*padding:\s*30px;\s*box-shadow:\s*0 10px 15px -3px rgba\(0,0,0,0.05\);\s*margin-bottom:\s*40px;">\s*<h3[^>]*>Interactive Supply Dynamics</h3>',
        '''<div id="card-movements" class="lecture-interactive-card" data-lecture-section="card_movements" style="background: #ffffff; border: 1.5px solid #10b981; border-radius: 12px; padding: 30px; cursor: pointer; position: relative; transition: all 0.2s ease; margin-bottom: 40px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
            <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 8px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
            <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive Supply Dynamics</h3>''',
        html, count=1
    )

    # Sec 3: Shifts
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*3\.\s*SHIFTS IN THE SUPPLY CURVE',
        '''<div id="sec-shifts" class="lecture-interactive-card" data-lecture-section="sec_shifts" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🚀 3. SHIFTS IN THE SUPPLY CURVE</h2>''',
        html, count=1
    )

    # Sec 4: Determinants
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*4\.\s*DETERMINANTS OF SUPPLY',
        '''<div id="sec-determinants" class="lecture-interactive-card" data-lecture-section="sec_determinants" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🧠 4. DETERMINANTS OF SUPPLY (NON-PRICE FACTORS)</h2>''',
        html, count=1
    )

    # card-determinants
    html = re.sub(
        r'<div style="overflow-x:\s*auto;\s*background:\s*#ffffff;\s*border-radius:\s*12px;\s*border:\s*1px solid #e2e8f0;\s*box-shadow:\s*0 4px 6px rgba\(0,0,0,0.02\);">',
        '''<div id="card-determinants" class="lecture-interactive-card" data-lecture-section="card_determinants" style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1.5px solid #fbcfe8; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease; padding-top: 10px; margin-bottom: 30px;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #be185d; background: #fdf2f8; padding: 2px 8px; border-radius: 8px; border: 1px solid #fbcfe8; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 9 HTML BUILDER
# =====================================================================
def build_c9_html():
    with open('scripts/raw_econ/lec_9_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = strip_study_resources(html)
    banner = make_banner(2, "The Allocation Of Resources", "9. Price Determination", "Market Equilibrium, Market Clearing Price &amp; Disequilibrium Adjustments")
    html = insert_banner(html, banner)

    # Sec 1
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*1\.\s*THE PRICE MECHANISM',
        '''<div id="sec-price-mechanism" class="lecture-interactive-card" data-lecture-section="sec_price_mechanism" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚙️ 1. THE PRICE MECHANISM</h2>''',
        html, count=1
    )

    # Sec 2
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*2\.\s*MARKET EQUILIBRIUM',
        '''<div id="sec-equilibrium" class="lecture-interactive-card" data-lecture-section="sec_equilibrium" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 2. MARKET EQUILIBRIUM</h2>''',
        html, count=1
    )

    # card-equilibrium
    html = re.sub(
        r'<div style="flex:\s*1;\s*min-width:\s*320px;\s*background:\s*#eff6ff;\s*border:\s*1px solid #bfdbfe;\s*border-radius:\s*12px;\s*padding:\s*25px;">\s*<h3[^>]*>[^<]*Equilibrium Price',
        '''<div id="card-equilibrium" class="lecture-interactive-card" data-lecture-section="card_equilibrium" style="flex: 1; min-width: 320px; background: #eff6ff; border: 1.5px solid #3b82f6; border-radius: 12px; padding: 25px; cursor: pointer; position: relative; transition: all 0.2s ease; margin-bottom: 20px;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #ffffff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
            <h3 style="margin: 0 0 10px 0; color: #1d4ed8; font-size: 20px;">✅ Equilibrium Price &amp; Quantity</h3>''',
        html, count=1
    )

    # Sec 3
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*3\.\s*MARKET DISEQUILIBRIUM',
        '''<div id="sec-disequilibrium" class="lecture-interactive-card" data-lecture-section="sec_disequilibrium" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚠️ 3. MARKET DISEQUILIBRIUM</h2>''',
        html, count=1
    )

    # card-excess-supply
    html = re.sub(
        r'<!-- Excess Supply -->\s*<div style="flex:\s*1;\s*min-width:\s*320px;\s*background:\s*#f0fdf4;\s*border:\s*1px solid #bbf7d0;\s*border-radius:\s*12px;\s*padding:\s*25px;[^>]*>',
        '''<!-- Excess Supply -->
        <div id="card-excess-supply" class="lecture-interactive-card" data-lecture-section="card_excess_supply" style="flex: 1; min-width: 320px; background: #f0fdf4; border: 1.5px solid #22c55e; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #15803d; background: #dcfce7; padding: 2px 8px; border-radius: 8px; border: 1px solid #86efac; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # card-excess-demand
    html = re.sub(
        r'<!-- Excess Demand -->\s*<div style="flex:\s*1;\s*min-width:\s*320px;\s*background:\s*#fef2f2;\s*border:\s*1px solid #fecaca;\s*border-radius:\s*12px;\s*padding:\s*25px;[^>]*>',
        '''<!-- Excess Demand -->
        <div id="card-excess-demand" class="lecture-interactive-card" data-lecture-section="card_excess_demand" style="flex: 1; min-width: 320px; background: #fef2f2; border: 1.5px solid #ef4444; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #b91c1c; background: #fee2e2; padding: 2px 8px; border-radius: 8px; border: 1px solid #fca5a5; pointer-events: none;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 10 HTML BUILDER
# =====================================================================
def build_c10_html():
    with open('scripts/raw_econ/lec_10_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(2, "The Allocation Of Resources", "10. Price Changes", "Shifts in Demand and Supply, Impact on Market Equilibrium &amp; Elasticity")
    html = insert_banner(html, banner)

    # Sec 1
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*1\.\s*CAUSES OF PRICE CHANGES',
        '''<div id="sec-causes" class="lecture-interactive-card" data-lecture-section="sec_causes" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📈 1. CAUSES OF PRICE CHANGES</h2>''',
        html, count=1
    )

    # Sec 2
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*2\.\s*CONSEQUENCES ON MARKET EQUILIBRIUM',
        '''<div id="sec-consequences" class="lecture-interactive-card" data-lecture-section="sec_consequences" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 2. CONSEQUENCES ON MARKET EQUILIBRIUM</h2>''',
        html, count=1
    )

    # card-four-scenarios
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(320px,\s*1fr\)\);\s*gap:\s*30px;">',
        '''<div id="card-four-scenarios" class="lecture-interactive-card" data-lecture-section="card_four_scenarios" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 18px; background: #f0fdf4; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 8px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 11 HTML BUILDER
# =====================================================================
def build_c11_html():
    with open('scripts/raw_econ/lec_11_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(2, "The Allocation Of Resources", "11. Price Elasticity of Demand (PED)", "Calculation, Determinants, Range of Values &amp; Revenue Link")
    html = insert_banner(html, banner)

    # 1. PED Definition
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*1\.\s*WHAT IS PRICE ELASTICITY OF DEMAND',
        '''<div id="sec-ped-intro" class="lecture-interactive-card" data-lecture-section="sec_ped_intro" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📉 1. WHAT IS PRICE ELASTICITY OF DEMAND (P.E.D)?</h2>''',
        html, count=1
    )

    # 2. Elastic vs Inelastic
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*2\.\s*ELASTIC VS INELASTIC DEMAND',
        '''<div id="sec-elastic-inelastic" class="lecture-interactive-card" data-lecture-section="sec_elastic_inelastic" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 2. ELASTIC VS INELASTIC DEMAND</h2>''',
        html, count=1
    )

    # 3. Special Cases
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*3\.\s*THREE SPECIAL CASES OF P\.E\.D',
        '''<div id="sec-special-cases" class="lecture-interactive-card" data-lecture-section="sec_special_cases" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🎯 3. THREE SPECIAL CASES OF P.E.D</h2>''',
        html, count=1
    )

    # 4. Determinants
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*4\.\s*DETERMINANTS OF P\.E\.D',
        '''<div id="sec-determinants" class="lecture-interactive-card" data-lecture-section="sec_determinants" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🔍 4. DETERMINANTS OF P.E.D</h2>''',
        html, count=1
    )

    # 5. Total Revenue
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*5\.\s*P\.E\.D',
        '''<div id="sec-revenue" class="lecture-interactive-card" data-lecture-section="sec_revenue" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #166534; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #16a34a; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">💰 5. P.E.D, CONSUMER EXPENDITURE &amp; TOTAL REVENUE</h2>''',
        html, count=1
    )

    # 6. Significance
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*6\.\s*SIGNIFICANCE OF P\.E\.D',
        '''<div id="sec-significance" class="lecture-interactive-card" data-lecture-section="sec_significance" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #9333ea; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🌟 6. SIGNIFICANCE OF P.E.D IN DECISION-MAKING</h2>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 12 HTML BUILDER
# =====================================================================
def build_c12_html():
    with open('scripts/raw_econ/lec_12_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(2, "The Allocation Of Resources", "12. Price Elasticity of Supply (PES)", "Calculation, Determinants, Range of Values &amp; Implications")
    html = insert_banner(html, banner)

    # 1. PES Definition
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*1\.\s*WHAT IS PRICE ELASTICITY OF SUPPLY',
        '''<div id="sec-pes-intro" class="lecture-interactive-card" data-lecture-section="sec_pes_intro" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📈 1. WHAT IS PRICE ELASTICITY OF SUPPLY (P.E.S)?</h2>''',
        html, count=1
    )

    # 2. Elastic vs Inelastic
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*2\.\s*ELASTIC VS INELASTIC SUPPLY',
        '''<div id="sec-elastic-inelastic" class="lecture-interactive-card" data-lecture-section="sec_elastic_inelastic" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 2. ELASTIC VS INELASTIC SUPPLY</h2>''',
        html, count=1
    )

    # 3. Special Cases
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*3\.\s*THREE SPECIAL CASES OF P\.E\.S',
        '''<div id="sec-special-cases" class="lecture-interactive-card" data-lecture-section="sec_special_cases" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🎯 3. THREE SPECIAL CASES OF P.E.S</h2>''',
        html, count=1
    )

    # 4. Determinants
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*4\.\s*DETERMINANTS OF P\.E\.S',
        '''<div id="sec-determinants" class="lecture-interactive-card" data-lecture-section="sec_determinants" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🔍 4. DETERMINANTS OF P.E.S</h2>''',
        html, count=1
    )

    # 5. Significance
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*5\.\s*SIGNIFICANCE OF P\.E\.S',
        '''<div id="sec-significance" class="lecture-interactive-card" data-lecture-section="sec_significance" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #9333ea; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🌟 5. SIGNIFICANCE OF P.E.S</h2>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 13 HTML BUILDER
# =====================================================================
def build_c13_html():
    with open('scripts/raw_econ/lec_13_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(2, "The Allocation Of Resources", "13. Market Economic System", "Key Characteristics, Advantages, Disadvantages &amp; Efficiency")
    html = insert_banner(html, banner)

    # Sec 1
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*1\.\s*THE MARKET ECONOMIC SYSTEM',
        '''<div id="sec-market-system" class="lecture-interactive-card" data-lecture-section="sec_market_system" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 1. THE MARKET ECONOMIC SYSTEM</h2>''',
        html, count=1
    )

    # card-features
    html = re.sub(
        r'<div style="display:\s*grid;\s*grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(280px,\s*1fr\)\);\s*gap:\s*20px;">',
        '''<div id="card-features" class="lecture-interactive-card" data-lecture-section="card_features" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; border: 1.5px solid #bfdbfe; border-radius: 14px; padding: 18px; background: #f8fafc; cursor: pointer; position: relative; transition: all 0.2s ease; margin-bottom: 30px;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        html, count=1
    )

    # Sec 2
    html = re.sub(
        r'<div style="margin-bottom:\s*50px;">\s*<h2[^>]*>[^<]*2\.\s*MERITS &amp; DEMERITS',
        '''<div id="sec-merits-demerits" class="lecture-interactive-card" data-lecture-section="sec_merits_demerits" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📊 2. MERITS &amp; DEMERITS (ARGUMENTS FOR AND AGAINST)</h2>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 14 HTML BUILDER
# =====================================================================
def build_c14_html():
    with open('scripts/raw_econ/lec_14_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(2, "The Allocation Of Resources", "14. Market Failure", "Definition, Causes, Externalities &amp; Inefficient Resource Allocation")
    html = insert_banner(html, banner)

    # 1. Market Failure
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*1\.\s*WHAT IS MARKET FAILURE',
        '''<div id="sec-market-failure-intro" class="lecture-interactive-card" data-lecture-section="sec_market_failure_intro" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📉 1. WHAT IS MARKET FAILURE?</h2>''',
        html, count=1
    )

    # 2. Causes
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*2\.\s*SIX CORE CAUSES OF MARKET FAILURE',
        '''<div id="sec-causes" class="lecture-interactive-card" data-lecture-section="sec_causes" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🚨 2. SIX CORE CAUSES OF MARKET FAILURE</h2>''',
        html, count=1
    )

    # 3. Externalities
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*3\.\s*EXTERNALITIES',
        '''<div id="sec-externalities" class="lecture-interactive-card" data-lecture-section="sec_externalities" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🌍 3. EXTERNALITIES (SPILLOVER EFFECTS)</h2>''',
        html, count=1
    )

    # 4. Consequences
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*4\.\s*EXAM FOCUS:\s*CONSEQUENCES OF MARKET FAILURE',
        '''<div id="sec-consequences" class="lecture-interactive-card" data-lecture-section="sec_consequences" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🔥 4. EXAM FOCUS: CONSEQUENCES OF MARKET FAILURE</h2>''',
        html, count=1
    )

    return html

# =====================================================================
# LECTURE 15 HTML BUILDER
# =====================================================================
def build_c15_html():
    with open('scripts/raw_econ/lec_15_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = strip_study_resources(html)
    banner = make_banner(2, "The Allocation Of Resources", "15. Mixed Economic System", "Government Intervention Methods, Price Controls, Privatisation &amp; Trade-offs")
    html = insert_banner(html, banner)

    # 1. Mixed Economic System
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*1\.\s*THE MIXED ECONOMIC SYSTEM',
        '''<div id="sec-mixed-system" class="lecture-interactive-card" data-lecture-section="sec_mixed_system" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 1. THE MIXED ECONOMIC SYSTEM</h2>''',
        html, count=1
    )

    # 2. Price Controls
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*2\.\s*GOVERNMENT PRICE CONTROLS',
        '''<div id="sec-price-controls" class="lecture-interactive-card" data-lecture-section="sec_price_controls" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🛑 2. GOVERNMENT PRICE CONTROLS</h2>''',
        html, count=1
    )

    # 3. Interventions
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*3\.\s*OTHER INTERVENTION METHODS',
        '''<div id="sec-intervention" class="lecture-interactive-card" data-lecture-section="sec_intervention" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">💸 3. OTHER INTERVENTION METHODS TO ADDRESS MARKET FAILURE</h2>''',
        html, count=1
    )

    # 4. Privatisation
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*4\.\s*PRIVATISATION &amp; NATIONALISATION',
        '''<div id="sec-privatisation" class="lecture-interactive-card" data-lecture-section="sec_privatisation" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7e22ce; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🔄 4. PRIVATISATION &amp; NATIONALISATION</h2>''',
        html, count=1
    )

    # 5. Direct Provision
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*5\.\s*DIRECT PROVISION &amp; QUOTAS',
        '''<div id="sec-direct-provision" class="lecture-interactive-card" data-lecture-section="sec_direct_provision" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🏛️ 5. DIRECT PROVISION &amp; QUOTAS</h2>''',
        html, count=1
    )

    # 6. Merits & Demerits
    html = re.sub(
        r'<div style="background:\s*white;[^>]*>\s*<h2[^>]*>[^<]*6\.\s*MERITS &amp; DEMERITS',
        '''<div id="sec-merits_demerits" class="lecture-interactive-card" data-lecture-section="sec_merits_demerits" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📊 6. MERITS &amp; DEMERITS OF A MIXED ECONOMY</h2>''',
        html, count=1
    )

    return html
