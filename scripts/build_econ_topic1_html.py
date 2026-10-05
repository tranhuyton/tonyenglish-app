import os
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def make_banner(topic_num, topic_name, lec_title, subtitle):
    return f"""<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%); padding: 28px 32px; border-radius: 14px; color: #ffffff; margin-bottom: 25px; box-shadow: 0 10px 25px -5px rgba(30,58,138,0.25); cursor: pointer; transition: all 0.2s ease; position: relative;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #93c5fd; margin-bottom: 6px;">Cambridge IGCSE Economics (0455) • Topic {topic_num}: {topic_name}</div>
  <h1 style="margin: 0; font-size: 30px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px; padding-right: 140px;">{lec_title}</h1>
  <p style="margin: 8px 0 0 0; font-size: 15.5px; color: #e0f2fe; opacity: 0.95; line-height: 1.5;">{subtitle}</p>
</div>"""

# =====================================================================
# LECTURE 1 HTML BUILDER
# =====================================================================
def build_c1_html():
    with open('scripts/raw_econ/lec_1_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = re.sub(r'<!--\s*Study Resources Bar\s*-->\s*<div[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    banner = make_banner(1, "The Basic Economic Problem", "1. The Basic Economic Problem", "Finite Resources vs Infinite Wants, Core Economic Decisions &amp; Goods Classification")
    top_container_pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; [^>]*>)'
    html = re.sub(top_container_pattern, r'\1\n\n    ' + banner, html, count=1)

    # Sec 1
    html = html.replace(
        '<!-- 1. The Nature of the Basic Economic Problem -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🌍 1. THE NATURE OF THE BASIC ECONOMIC PROBLEM</h2>',
        '''<!-- 1. The Nature of the Basic Economic Problem -->
    <div id="sec-nature" class="lecture-interactive-card" data-lecture-section="sec_nature" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🌍 1. THE NATURE OF THE BASIC ECONOMIC PROBLEM</h2>''',
        1
    )

    # Card concept map
    html = html.replace(
        '<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-top: 25px; margin-bottom: 30px;">\n            <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive Concept Map</h3>',
        '''<div id="card-concept-map" class="lecture-interactive-card" data-lecture-section="card_concept_map" style="background: #ffffff; border: 2px solid #93c5fd; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-top: 25px; margin-bottom: 30px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 10px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
            <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive Concept Map</h3>''',
        1
    )

    # Sec 2
    html = html.replace(
        '<!-- 2. The Basic Economic Problem in 4 Contexts (Syllabus 1.1.1) -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #6366f1; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">👥 2. THE BASIC ECONOMIC PROBLEM IN 4 CONTEXTS</h2>',
        '''<!-- 2. The Basic Economic Problem in 4 Contexts (Syllabus 1.1.1) -->
    <div id="sec-contexts" class="lecture-interactive-card" data-lecture-section="sec_contexts" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eef2ff; border: 1px solid #c7d2fe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #4338ca; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #6366f1; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">👥 2. THE BASIC ECONOMIC PROBLEM IN 4 CONTEXTS</h2>''',
        1
    )

    # 4 sub-cards
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #cbd5e1; border-top: 4px solid #3b82f6; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<div style="font-size: 28px; margin-bottom: 8px;">🛒</div>\s*<h4 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px;">Consumers</h4>',
        '''<div id="card-consumers" class="lecture-interactive-card" data-lecture-section="card_consumers" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-top: 4px solid #3b82f6; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
                <div style="font-size: 28px; margin-bottom: 8px;">🛒</div>
                <h4 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px;">Consumers</h4>''',
        html
    )

    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #cbd5e1; border-top: 4px solid #10b981; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<div style="font-size: 28px; margin-bottom: 8px;">👷</div>\s*<h4 style="margin: 0 0 8px 0; color: #065f46; font-size: 18px;">Workers</h4>',
        '''<div id="card-workers" class="lecture-interactive-card" data-lecture-section="card_workers" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-top: 4px solid #10b981; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
                <div style="font-size: 28px; margin-bottom: 8px;">👷</div>
                <h4 style="margin: 0 0 8px 0; color: #065f46; font-size: 18px;">Workers</h4>''',
        html
    )

    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #cbd5e1; border-top: 4px solid #f59e0b; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<div style="font-size: 28px; margin-bottom: 8px;">🏭</div>\s*<h4 style="margin: 0 0 8px 0; color: #92400e; font-size: 18px;">Producers / Firms</h4>',
        '''<div id="card-producers" class="lecture-interactive-card" data-lecture-section="card_producers" style="background: #ffffff; border: 1.5px solid #fde68a; border-top: 4px solid #f59e0b; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #b45309; background: #fffbeb; padding: 2px 6px; border-radius: 8px; border: 1px solid #fde68a; pointer-events: none;">🎧 Nghe mục này</div>
                <div style="font-size: 28px; margin-bottom: 8px;">🏭</div>
                <h4 style="margin: 0 0 8px 0; color: #92400e; font-size: 18px;">Producers / Firms</h4>''',
        html
    )

    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #cbd5e1; border-top: 4px solid #ef4444; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<div style="font-size: 28px; margin-bottom: 8px;">🏛️</div>\s*<h4 style="margin: 0 0 8px 0; color: #991b1b; font-size: 18px;">Governments</h4>',
        '''<div id="card-governments" class="lecture-interactive-card" data-lecture-section="card_governments" style="background: #ffffff; border: 1.5px solid #fca5a5; border-top: 4px solid #ef4444; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #b91c1c; background: #fef2f2; padding: 2px 6px; border-radius: 8px; border: 1px solid #fca5a5; pointer-events: none;">🎧 Nghe mục này</div>
                <div style="font-size: 28px; margin-bottom: 8px;">🏛️</div>
                <h4 style="margin: 0 0 8px 0; color: #991b1b; font-size: 18px;">Governments</h4>''',
        html
    )

    # Sec 3
    html = html.replace(
        '<!-- 3. Resource Allocation Decisions (Syllabus 1.1.2) -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #06b6d4; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">⚖️ 3. RESOURCE ALLOCATION: THE THREE ECONOMIC QUESTIONS</h2>',
        '''<!-- 3. Resource Allocation Decisions (Syllabus 1.1.2) -->
    <div id="sec-questions" class="lecture-interactive-card" data-lecture-section="sec_questions" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfeff; border: 1px solid #a5f3fc; border-radius: 20px; font-size: 12px; font-weight: 600; color: #0891b2; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #06b6d4; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 3. RESOURCE ALLOCATION: THE THREE ECONOMIC QUESTIONS</h2>''',
        1
    )

    html = html.replace(
        '<div style="display: flex; flex-direction: column; gap: 15px;">\n            <div style="background: #f8fafc; border-left: 5px solid #0284c7; padding: 18px 22px; border-radius: 0 10px 10px 0;">',
        '''<div id="card-three-questions" class="lecture-interactive-card" data-lecture-section="card_three_questions" style="display: flex; flex-direction: column; gap: 15px; border: 1.5px solid #bae6fd; border-radius: 12px; padding: 16px; background: #f0f9ff; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #0369a1; background: #e0f2fe; padding: 2px 8px; border-radius: 8px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>
            <div style="background: #ffffff; border-left: 5px solid #0284c7; padding: 18px 22px; border-radius: 0 10px 10px 0; border: 1px solid #e2e8f0; border-left-width: 5px;">''',
        1
    )

    # Sec 4
    html = html.replace(
        '<!-- 4. Needs vs Wants & Economic Sectors -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🛍️ 4. KEY DISTINCTIONS: NEEDS VS WANTS & SECTORS</h2>',
        '''<!-- 4. Needs vs Wants & Economic Sectors -->
    <div id="sec-distinctions" class="lecture-interactive-card" data-lecture-section="sec_distinctions" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🛍️ 4. KEY DISTINCTIONS: NEEDS VS WANTS & SECTORS</h2>''',
        1
    )

    html = html.replace(
        '<div style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 30px;">\n            <div style="flex: 1; min-width: 300px; background: #fef2f2; border: 1px solid #fca5a5; border-radius: 12px; padding: 20px;">\n                <h4 style="margin: 0 0 8px 0; color: #b91c1c; font-size: 18px;">💧 Needs</h4>',
        '''<div id="card-needs-wants" class="lecture-interactive-card" data-lecture-section="card_needs_wants" style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 30px; border: 1.5px solid #fbcfe8; border-radius: 14px; padding: 15px; background: #fff5f8; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #be185d; background: #fdf2f8; padding: 2px 8px; border-radius: 8px; border: 1px solid #fbcfe8; pointer-events: none;">🎧 Nghe mục này</div>
            <div style="flex: 1; min-width: 300px; background: #fef2f2; border: 1px solid #fca5a5; border-radius: 12px; padding: 20px;">\n                <h4 style="margin: 0 0 8px 0; color: #b91c1c; font-size: 18px;">💧 Needs</h4>''',
        1
    )

    html = html.replace(
        '<!-- Private vs Public Sector -->\n        <div style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">',
        '''<!-- Private vs Public Sector -->
        <div id="card-sectors" class="lecture-interactive-card" data-lecture-section="card_sectors" style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1.5px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease; padding-top: 10px;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #475569; background: #f1f5f9; padding: 2px 8px; border-radius: 8px; border: 1px solid #cbd5e1; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        1
    )

    # Sec 5
    html = html.replace(
        '<!-- 5. Economic Goods vs Free Goods (Syllabus 1.1.3) -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">⚖️ 5. ECONOMIC GOODS VS FREE GOODS</h2>',
        '''<!-- 5. Economic Goods vs Free Goods (Syllabus 1.1.3) -->
    <div id="sec-goods" class="lecture-interactive-card" data-lecture-section="sec_goods" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7c3aed; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 5. ECONOMIC GOODS VS FREE GOODS</h2>''',
        1
    )

    html = html.replace(
        '<div style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 25px;">\n            <div style="flex: 1; min-width: 320px; background: #fdf4ff; border: 1px solid #fbcfe8; border-radius: 12px; padding: 25px;">\n                <h3 style="margin: 0 0 15px 0; color: #be185d; font-size: 20px;">📦 Economic Goods</h3>',
        '''<div id="card-goods-comparison" class="lecture-interactive-card" data-lecture-section="card_goods_comparison" style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 25px; border: 1.5px solid #e9d5ff; border-radius: 14px; padding: 15px; background: #faf5ff; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #f5f3ff; padding: 2px 8px; border-radius: 8px; border: 1px solid #ddd6fe; pointer-events: none;">🎧 Nghe mục này</div>
            <div style="flex: 1; min-width: 320px; background: #fdf4ff; border: 1px solid #fbcfe8; border-radius: 12px; padding: 25px;">\n                <h3 style="margin: 0 0 15px 0; color: #be185d; font-size: 20px;">📦 Economic Goods</h3>''',
        1
    )

    return html

# =====================================================================
# LECTURE 2 HTML BUILDER
# =====================================================================
def build_c2_html():
    with open('scripts/raw_econ/lec_2_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = re.sub(r'<!--\s*Study Resources Bar\s*-->\s*<div[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    banner = make_banner(1, "The Basic Economic Problem", "2. The Factors of Production", "Land, Labour, Capital, Enterprise, Factor Mobility &amp; Productive Capacity")
    top_container_pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; [^>]*>)'
    html = re.sub(top_container_pattern, r'\1\n\n    ' + banner, html, count=1)

    # Sec 1: 4 Factors
    html = html.replace(
        '<!-- 1. The Four Factors of Production & Rewards -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🏭 1. THE FOUR FACTORS OF PRODUCTION & THEIR REWARDS</h2>',
        '''<!-- 1. The Four Factors of Production & Rewards -->
    <div id="sec-factors" class="lecture-interactive-card" data-lecture-section="sec_factors" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🏭 1. THE FOUR FACTORS OF PRODUCTION & THEIR REWARDS</h2>''',
        1
    )

    # Sub-card: Interactive Factor Map
    html = html.replace(
        '<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px;">\n            <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive Factor Map</h3>',
        '''<div id="card-factors-grid" class="lecture-interactive-card" data-lecture-section="card_factors_grid" style="background: #ffffff; border: 2px solid #6ee7b7; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 8px; border-radius: 10px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
            <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive Factor Map</h3>''',
        1
    )

    # Sub-card: Capital vs Money
    html = html.replace(
        '<!-- Key Distinction Box: Capital vs Money -->\n        <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 18px 22px; border-radius: 0 10px 10px 0; margin-top: 25px;">',
        '''<!-- Key Distinction Box: Capital vs Money -->
        <div id="card-capital-distinction" class="lecture-interactive-card" data-lecture-section="card_capital_distinction" style="background: #eff6ff; border: 1.5px solid #bfdbfe; border-left: 5px solid #3b82f6; padding: 18px 22px; border-radius: 10px; margin-top: 25px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #ffffff; padding: 2px 8px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>''',
        1
    )

    # Sec 2: Mobility
    html = html.replace(
        '<!-- 2. Mobility of Factors of Production -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🏃‍♂️ 2. MOBILITY OF FACTORS OF PRODUCTION</h2>',
        '''<!-- 2. Mobility of Factors of Production -->
    <div id="sec-mobility" class="lecture-interactive-card" data-lecture-section="sec_mobility" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🏃‍♂️ 2. MOBILITY OF FACTORS OF PRODUCTION</h2>''',
        1
    )

    # Sub-card: Factor mobility grid
    html = html.replace(
        '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">\n            <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">',
        '''<div id="card-mobility-types" class="lecture-interactive-card" data-lecture-section="card_mobility_types" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; border: 1.5px solid #fed7aa; border-radius: 14px; padding: 18px; background: #fffaf5; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #c2410c; background: #fff7ed; padding: 2px 8px; border-radius: 8px; border: 1px solid #fed7aa; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>
            <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">''',
        1
    )

    # Sec 3: Quantity & Quality
    html = html.replace(
        '<!-- 3. Quantity & Quality of Factors of Production (Syllabus 1.2.2) -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">📈 3. QUANTITY & QUALITY OF FACTORS OF PRODUCTION</h2>',
        '''<!-- 3. Quantity & Quality of Factors of Production (Syllabus 1.2.2) -->
    <div id="sec-quant-qual" class="lecture-interactive-card" data-lecture-section="sec_quant_qual" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📈 3. QUANTITY & QUALITY OF FACTORS OF PRODUCTION</h2>''',
        1
    )

    # Sub-card: Table
    html = html.replace(
        '<div style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">',
        '''<div id="card-quant-qual-table" class="lecture-interactive-card" data-lecture-section="card_quant_qual_table" style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1.5px solid #fbcfe8; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease; padding-top: 10px;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #be185d; background: #fdf2f8; padding: 2px 8px; border-radius: 8px; border: 1px solid #fbcfe8; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>''',
        1
    )

    return html

# =====================================================================
# LECTURE 3 HTML BUILDER
# =====================================================================
def build_c3_html():
    with open('scripts/raw_econ/lec_3_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = re.sub(r'<!--\s*Study Resources Bar\s*-->\s*<div[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    banner = make_banner(1, "The Basic Economic Problem", "3. Opportunity Cost", "Definition, Decision-Making Trade-offs across Economic Agents &amp; Critical Principles")
    top_container_pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; [^>]*>)'
    html = re.sub(top_container_pattern, r'\1\n\n    ' + banner, html, count=1)

    # Sec 1: Definition
    html = html.replace(
        '<!-- 1. The Core Definition of Opportunity Cost -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">⚖️ 1. THE DEFINITION OF OPPORTUNITY COST</h2>',
        '''<!-- 1. The Core Definition of Opportunity Cost -->
    <div id="sec-definition" class="lecture-interactive-card" data-lecture-section="sec_definition" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #7c3aed; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚖️ 1. THE DEFINITION OF OPPORTUNITY COST</h2>''',
        1
    )

    # Sub-card: Definition box & examples
    html = html.replace(
        '<div style="background: #f3e8ff; border-left: 5px solid #9333ea; padding: 25px; border-radius: 0 12px 12px 0; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">',
        '''<div id="card-definition" class="lecture-interactive-card" data-lecture-section="card_definition" style="background: #f3e8ff; border: 1.5px solid #d8b4fe; border-left: 6px solid #9333ea; padding: 25px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #ffffff; padding: 2px 8px; border-radius: 8px; border: 1px solid #d8b4fe; pointer-events: none;">🎧 Nghe mục này</div>''',
        1
    )

    # Sec 2: Decision making
    html = html.replace(
        '<!-- 2. Interactive Decision Map: 4 Economic Agents -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">👥 2. OPPORTUNITY COST IN DECISION-MAKING (SYLLABUS 1.3.2)</h2>',
        '''<!-- 2. Interactive Decision Map: 4 Economic Agents -->
    <div id="sec-decision-making" class="lecture-interactive-card" data-lecture-section="sec_decision_making" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">👥 2. OPPORTUNITY COST IN DECISION-MAKING (SYLLABUS 1.3.2)</h2>''',
        1
    )

    # Sub-card: interactive decision map
    html = html.replace(
        '<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 30px;">\n            <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive Decision Map</h3>',
        '''<div id="card-agent-tradeoffs" class="lecture-interactive-card" data-lecture-section="card_agent_tradeoffs" style="background: #ffffff; border: 2px solid #93c5fd; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 30px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 8px; border-radius: 10px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
            <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive Decision Map</h3>''',
        1
    )

    # Sec 3: Pitfalls
    html = html.replace(
        '<!-- 3. Key Exam Traps & Principles -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">⚠️ 3. CRITICAL PRINCIPLES & EXAM PITFALLS</h2>',
        '''<!-- 3. Key Exam Traps & Principles -->
    <div id="sec-pitfalls" class="lecture-interactive-card" data-lecture-section="sec_pitfalls" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">⚠️ 3. CRITICAL PRINCIPLES & EXAM PITFALLS</h2>''',
        1
    )

    return html

# =====================================================================
# LECTURE 4 HTML BUILDER
# =====================================================================
def build_c4_html():
    with open('scripts/raw_econ/lec_4_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = re.sub(r'<!--\s*Study Resources Bar\s*-->\s*<div[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    banner = make_banner(1, "The Basic Economic Problem", "4. Production Possibility Curve", "PPC Boundary, Full Employment, Increasing vs Constant Opportunity Cost &amp; Shifts")
    top_container_pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; [^>]*>)'
    html = re.sub(top_container_pattern, r'\1\n\n    ' + banner, html, count=1)

    # Sec 1: PPC Intro
    html = html.replace(
        '<!-- 1. The Production Possibility Curve (PPC) -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #0284c7; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">📈 1. THE PRODUCTION POSSIBILITY CURVE (PPC)</h2>',
        '''<!-- 1. The Production Possibility Curve (PPC) -->
    <div id="sec-ppc-intro" class="lecture-interactive-card" data-lecture-section="sec_ppc_intro" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 20px; font-size: 12px; font-weight: 600; color: #0369a1; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #0284c7; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📈 1. THE PRODUCTION POSSIBILITY CURVE (PPC)</h2>''',
        1
    )

    # Sub-card: Points A, B, C
    html = html.replace(
        '<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px;">\n            <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive PPC Diagram: Points Under, On, and Beyond</h3>',
        '''<div id="card-ppc-points" class="lecture-interactive-card" data-lecture-section="card_ppc_points" style="background: #ffffff; border: 2px solid #7dd3fc; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #0369a1; background: #f0f9ff; padding: 2px 8px; border-radius: 10px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>
            <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive PPC Diagram: Points Under, On, and Beyond</h3>''',
        1
    )

    # Sec 2: Movements
    html = html.replace(
        '<!-- 2. Movements along a PPC & Opportunity Cost -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🔄 2. MOVEMENTS ALONG A PPC (SYLLABUS 1.4.3)</h2>',
        '''<!-- 2. Movements along a PPC & Opportunity Cost -->
    <div id="sec-movements" class="lecture-interactive-card" data-lecture-section="sec_movements" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🔄 2. MOVEMENTS ALONG A PPC (SYLLABUS 1.4.3)</h2>''',
        1
    )

    # Sub-card: Reallocation
    html = html.replace(
        '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 25px;">\n            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; padding: 20px;">',
        '''<div id="card-movements" class="lecture-interactive-card" data-lecture-section="card_movements" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 25px; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 18px; background: #f0fdf4; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 8px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none; z-index: 5;">🎧 Nghe mục này</div>
            <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; padding: 20px;">''',
        1
    )

    # Sec 3: Shape
    html = html.replace(
        '<!-- 3. Shape of the PPC: Bowed-Out vs Straight Line -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">📐 3. SHAPE OF THE PPC: INCREASING VS CONSTANT OPPORTUNITY COST</h2>',
        '''<!-- 3. Shape of the PPC: Bowed-Out vs Straight Line -->
    <div id="sec-shape" class="lecture-interactive-card" data-lecture-section="sec_shape" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #db2777; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">📐 3. SHAPE OF THE PPC: INCREASING VS CONSTANT OPPORTUNITY COST</h2>''',
        1
    )

    # Sec 4: Shifts
    html = html.replace(
        '<!-- 4. Shifts of the PPC (Syllabus 1.4.4) -->\n    <div style="margin-bottom: 50px;">\n        <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🚀 4. SHIFTS OF THE PPC: ECONOMIC GROWTH & RECESSION</h2>',
        '''<!-- 4. Shifts of the PPC (Syllabus 1.4.4) -->
    <div id="sec-shifts" class="lecture-interactive-card" data-lecture-section="sec_shifts" style="background: white; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); position: relative; cursor: pointer; transition: all 0.2s ease;">
        <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
        <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; padding-right: 130px;">🚀 4. SHIFTS OF THE PPC: ECONOMIC GROWTH & RECESSION</h2>''',
        1
    )

    # Sub-card: Growth comparison
    html = html.replace(
        '<!-- Actual vs Potential Growth Box -->\n        <div style="background: #fffbeb; border: 1px solid #fde047; border-radius: 10px; padding: 20px; margin-top: 25px;">',
        '''<!-- Actual vs Potential Growth Box -->
        <div id="card-shifts-comparison" class="lecture-interactive-card" data-lecture-section="card_shifts_comparison" style="background: #fffbeb; border: 1.5px solid #fde047; border-radius: 12px; padding: 20px; margin-top: 25px; cursor: pointer; position: relative; transition: all 0.2s ease;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #92400e; background: #ffffff; padding: 2px 8px; border-radius: 8px; border: 1px solid #fde047; pointer-events: none;">🎧 Nghe mục này</div>''',
        1
    )

    return html

def verify_all():
    builders = [
        ("Lec 1", build_c1_html),
        ("Lec 2", build_c2_html),
        ("Lec 3", build_c3_html),
        ("Lec 4", build_c4_html),
    ]
    for name, b in builders:
        html = b()
        op = len(re.findall(r'<div\b', html))
        cl = len(re.findall(r'</div>', html))
        diff = op - cl
        assert diff == 0, f"{name} diff is {diff} (op={op}, cl={cl})"
        assert "Study Resources" not in html and "Tài liệu học tập" not in html, f"{name} has study resources"
        assert "#sec-header" in html or 'id="sec-header"' in html, f"{name} missing sec-header"
        print(f"✅ {name} verified successfully: opens={op}, closes={cl}, diff={diff}")

if __name__ == '__main__':
    verify_all()
