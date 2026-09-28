import sys
import re
import json

sys.path.append('scripts')
from audio_lecture_engine import sb

sys.stdout.reconfigure(encoding='utf-8')

LECTURES = [
    ("10_1", "362104be-aedc-4cbe-87b2-29034e93cc9c", {
        "bg1": "#f0fdf4", "bg2": "#dcfce7", "border": "#86efac", "accent": "#16a34a", "accent_dark": "#166534", "text": "#14532d",
        "title": "Cambridge IGCSE Exam Strategy: 7-Mark Agricultural Questions",
        "text_content": "In exam 7-mark case study questions on agricultural systems, always classify the farm precisely along all three axes (Arable vs Pastoral, Commercial vs Subsistence, Intensive vs Extensive), categorize inputs into physical versus human, describe specific farming processes, and identify both commercial outputs and environmental byproducts."
    }),
    ("10_2", "76dcafbf-e6b8-47f1-8618-be1b14e975ed", {
        "bg1": "#f0f9ff", "bg2": "#e0f2fe", "border": "#7dd3fc", "accent": "#0284c7", "accent_dark": "#075985", "text": "#0c4a6e",
        "title": "Cambridge IGCSE Exam Strategy: Food Supply & Demand Disparities",
        "text_content": "In exam questions on food supply disparities, synthesize physical factors like monsoonal droughts with economic drivers like global trade barriers, commodity market speculation, and the diversion of edible corn crops into biofuel ethanol."
    }),
    ("10_3", "96d7f427-3b6d-43e3-84dc-f8f052f20033", {
        "bg1": "#fff7ed", "bg2": "#ffedd5", "border": "#fdba74", "accent": "#ea580c", "accent_dark": "#9a3412", "text": "#7c2d12",
        "title": "Cambridge IGCSE Exam Strategy: Food Shortages & Long-Term Solutions",
        "text_content": "For 7-mark case study questions on food shortages, always balance physical causes like drought and locust swarms with human triggers like armed conflict and food hoarding, and evaluate both emergency food aid versus long-term soil conservation schemes."
    }),
    ("10_4", "199a26cd-1226-4ff7-b063-f7df7fa7b5ba", {
        "bg1": "#fefce8", "bg2": "#fef08a", "border": "#fde047", "accent": "#ca8a04", "accent_dark": "#854d0e", "text": "#713f12",
        "title": "Cambridge IGCSE Exam Strategy: Energy Systems & Fuelwood Crisis",
        "text_content": "In exam questions on energy supply, always provide precise technical classifications: clearly separate non-renewable exhaustible fossil fuels like coal from infinite renewable flows like geothermal, and explain the physical-geographical conditions required to site hydroelectric dams or offshore wind arrays."
    }),
    ("10_5", "a3a8d904-d277-4eef-b8ff-52a913ebc5f6", {
        "bg1": "#f0fdfa", "bg2": "#ccfbf1", "border": "#5eead4", "accent": "#0d9488", "accent_dark": "#115e59", "text": "#134e4a",
        "title": "Cambridge IGCSE Exam Strategy: Global Fuel Mix & Energy Security",
        "text_content": "In exam answers assessing energy security risks, always cite specific geopolitical case studies: evaluate how oil-importing economies insulate themselves by establishing strategic petroleum reserves, constructing liquefied natural gas regasification terminals, and aggressively expanding domestic renewable wind and nuclear capacity."
    }),
    ("10_6", "fb30c141-db3a-49e8-aa55-028c913640d4", {
        "bg1": "#f0fdf4", "bg2": "#dcfce7", "border": "#86efac", "accent": "#059669", "accent_dark": "#065f46", "text": "#064e3b",
        "title": "Cambridge IGCSE Exam Strategy: 7-Mark Energy Trade-offs & Decarbonisation",
        "text_content": "In exam 7-mark case study questions on energy impacts, never depict any energy source as flawless: critically balance economic feasibility against environmental degradation, discuss NIMBYism and aesthetic opposition, and cite quantitative national data like Sweden's 98 percent fossil-free electricity generation."
    })
]

def make_exam_card(cfg):
    return f'''
    <!-- CAMBRIDGE IGCSE EXAM STRATEGY CARD -->
    <div id="card-exam-strategy" class="lecture-interactive-card" data-lecture-section="exam_strategy" style="background: linear-gradient(135deg, {cfg['bg1']} 0%, {cfg['bg2']} 100%); border: 1px solid {cfg['border']}; border-left: 6px solid {cfg['accent']}; border-radius: 12px; padding: 22px; margin: 32px 0 24px 0; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
        <div style="font-weight: 700; color: {cfg['accent_dark']}; font-size: 16px; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 20px;">🎓</span> {cfg['title']}
        </div>
        <div style="font-size: 14.5px; color: {cfg['text']}; line-height: 1.65;">
            {cfg['text_content']}
        </div>
    </div>
'''

for code, lid, cfg in LECTURES:
    with open(f'scratch/lectures/{code}_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    with open(f'public/audio/lectures/geography/{code}/manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 1. Transform Header Banner
    html = re.sub(
        r'<div style="background:\s*linear-gradient\(135deg[^>]+>',
        lambda m: m.group(0).replace('<div style="', '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; '),
        html,
        count=1
    )

    # 2. Specific per lecture transformations
    if code == "10_1":
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Classification of Farming Types & Operational Scales</h2>',
            '<h2 id="sec-farming-classification" class="lecture-interactive-card" data-lecture-section="sec_farming_classification" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Classification of Farming Types & Operational Scales</h2>'
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">The Agricultural System: Input-Process-Output (IPO) Framework</h2>',
            '<h2 id="sec-agricultural-ipo" class="lecture-interactive-card" data-lecture-section="sec_agricultural_ipo" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">The Agricultural System: Input-Process-Output (IPO) Framework</h2>'
        )
        html = re.sub(
            r'(<div style="margin: 22px 0; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px; text-align: center;">\s*<img src="[^"]*t10_fig_10_8\.png)',
            r'<div id="card-ipo-framework" class="lecture-interactive-card" data-lecture-section="ipo_framework" style="margin: 22px 0; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px; text-align: center; cursor:pointer;">\n            <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t10_fig_10_8.png?v=2',
            html
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Interactive Agricultural System Explorer: Case Studies & IPO Mechanics</h2>',
            '<h2 id="sec-ipo-explorer" class="lecture-interactive-card" data-lecture-section="sec_ipo_explorer" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Interactive Agricultural System Explorer: Case Studies & IPO Mechanics</h2>'
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">High-Tech Frontiers: Hydroponics, Aeroponics & Vertical Farming</h2>',
            '<h2 id="sec-hightech-farming" class="lecture-interactive-card" data-lecture-section="sec_hightech_farming" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">High-Tech Frontiers: Hydroponics, Aeroponics & Vertical Farming</h2>'
        )

    elif code == "10_2":
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Global Calorie Supply Patterns & The Nutrition Transition</h2>',
            '<h2 id="sec-calorie-patterns" class="lecture-interactive-card" data-lecture-section="sec_calorie_patterns" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Global Calorie Supply Patterns & The Nutrition Transition</h2>'
        )
        html = html.replace(
            '<div style="background: #f0fdfa; border-left: 4px solid #0d9488; border-radius: 8px; padding: 16px 20px; margin: 20px 0;">',
            '<div id="card-nutrition-transition" class="lecture-interactive-card" data-lecture-section="nutrition_transition" style="background: #f0fdfa; border-left: 4px solid #0d9488; border-radius: 8px; padding: 16px 20px; margin: 20px 0; cursor:pointer;">'
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Interactive Map: Global Food System Dynamics & Hotspots</h2>',
            '<h2 id="sec-food-map" class="lecture-interactive-card" data-lecture-section="sec_food_map" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Interactive Map: Global Food System Dynamics & Hotspots</h2>'
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Agro-Industrialisation & Environmental Costs of Meat Demand</h2>',
            '<h2 id="sec-meat-demand" class="lecture-interactive-card" data-lecture-section="sec_meat_demand" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Agro-Industrialisation & Environmental Costs of Meat Demand</h2>'
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Food Waste Geography & Multinational Agribusiness Corporations</h2>',
            '<h2 id="sec-food-waste" class="lecture-interactive-card" data-lecture-section="sec_food_waste" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Food Waste Geography & Multinational Agribusiness Corporations</h2>'
        )

    elif code == "10_3":
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Defining Food Security & Measuring Global Hunger</h2>',
            '<h2 id="sec-food-security" class="lecture-interactive-card" data-lecture-section="sec_food_security" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Defining Food Security & Measuring Global Hunger</h2>'
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Interactive Food Insecurity Hotspots & Theoretical Models</h2>',
            '<h2 id="sec-insecurity-hotspots" class="lecture-interactive-card" data-lecture-section="sec_insecurity_hotspots" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Interactive Food Insecurity Hotspots & Theoretical Models</h2>'
        )
        html = html.replace(
            '<h3 style="color: #0f172a; margin: 24px 0 12px 0; font-size: 18px; font-weight: 700;">Theoretical Debate: Thomas Malthus vs Ester Boserup</h3>',
            '<h3 id="card-malthus-boserup" class="lecture-interactive-card" data-lecture-section="malthus_boserup" style="color: #0f172a; margin: 24px 0 12px 0; font-size: 18px; font-weight: 700; cursor:pointer;">Theoretical Debate: Thomas Malthus vs Ester Boserup</h3>'
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Detailed Specific Example: The Food Crisis in Nigeria</h2>',
            '<h2 id="sec-nigeria-crisis" class="lecture-interactive-card" data-lecture-section="sec_nigeria_crisis" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Detailed Specific Example: The Food Crisis in Nigeria</h2>'
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Sustainable Strategies: Soil Conservation & Advanced Irrigation</h2>',
            '<h2 id="sec-sustainable-food" class="lecture-interactive-card" data-lecture-section="sec_sustainable_food" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Sustainable Strategies: Soil Conservation & Advanced Irrigation</h2>'
        )

    elif code == "10_4":
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Foundational Energy Taxonomy: Primary vs Secondary Energy</h2>',
            '<h2 id="sec-energy-taxonomy" class="lecture-interactive-card" data-lecture-section="sec_energy_taxonomy" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Foundational Energy Taxonomy: Primary vs Secondary Energy</h2>'
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">The Fuelwood Crisis: Energy Poverty in Low-Income Nations</h2>',
            '<h2 id="sec-fuelwood-crisis" class="lecture-interactive-card" data-lecture-section="sec_fuelwood_crisis" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">The Fuelwood Crisis: Energy Poverty in Low-Income Nations</h2>'
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Interactive Energy Ladder & Decarbonisation Transition</h2>',
            '<h2 id="sec-energy-ladder" class="lecture-interactive-card" data-lecture-section="sec_energy_ladder" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Interactive Energy Ladder & Decarbonisation Transition</h2>'
        )

    elif code == "10_5":
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Global Consumption Surges & Evolving Primary Fuel Shares</h2>',
            '<h2 id="sec-consumption-surges" class="lecture-interactive-card" data-lecture-section="sec_consumption_surges" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Global Consumption Surges & Evolving Primary Fuel Shares</h2>'
        )
        html = re.sub(
            r'<h2([^>]*)>(Interactive Map: Regional Fuel Mix Profiles[^<]*)</h2>',
            r'<h2\1 id="sec-fuel-mix-map" class="lecture-interactive-card" data-lecture-section="sec_fuel_mix_map" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">\2</h2>',
            html
        )
        html = re.sub(
            r'<h2([^>]*)>(Energy Security & The 3-Stage Interruption Sequence[^<]*)</h2>',
            r'<h2\1 id="sec-energy-security" class="lecture-interactive-card" data-lecture-section="sec_energy_security" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">\2</h2>',
            html
        )

    elif code == "10_6":
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Environmental &amp; Health Impacts of Fossil Fuels</h2>',
            '<h2 id="sec-fossil-impacts" class="lecture-interactive-card" data-lecture-section="sec_fossil_impacts" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Environmental &amp; Health Impacts of Fossil Fuels</h2>'
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Nuclear Power: Low-Carbon Baseload vs Radiological Risks</h2>',
            '<h2 id="sec-nuclear-power" class="lecture-interactive-card" data-lecture-section="sec_nuclear_power" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Nuclear Power: Low-Carbon Baseload vs Radiological Risks</h2>'
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">Renewable Energy: Green Credentials vs Environmental Trade-offs</h2>',
            '<h2 id="sec-renewable-tradeoffs" class="lecture-interactive-card" data-lecture-section="sec_renewable_tradeoffs" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">Renewable Energy: Green Credentials vs Environmental Trade-offs</h2>'
        )
        html = re.sub(
            r'<h2([^>]*)>(Global Energy Consumption Trends[^<]*)</h2>',
            r'<h2\1 id="sec-global-trends" class="lecture-interactive-card" data-lecture-section="sec_global_trends" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">\2</h2>',
            html
        )
        html = html.replace(
            '<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">IGCSE Case Study: Sweden\'s Sustainable Decarbonisation</h2>',
            '<h2 id="sec-sweden-casestudy" class="lecture-interactive-card" data-lecture-section="sec_sweden_casestudy" style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700; cursor:pointer;">IGCSE Case Study: Sweden\'s Sustainable Decarbonisation</h2>'
        )

    # 3. Insert Exam Strategy Card
    card_html = make_exam_card(cfg)
    if '<script' in html:
        html = html.replace('<script', card_html + '\n<script', 1)
    else:
        last_div_idx = html.rfind('</div>')
        html = html[:last_div_idx] + card_html + html[last_div_idx:]

    # Check div balance
    open_divs = len(re.findall(r'<div\b', html, re.I))
    close_divs = len(re.findall(r'</div\b', html, re.I))
    diff = open_divs - close_divs
    assert diff == 0, f"Diff mismatch for {code}: {diff}"

    # Check all manifest selectors
    missing_selectors = []
    for s in manifest['segments']:
        sel = s['selector']
        raw_id = sel.lstrip('#')
        if f'id="{raw_id}"' not in html:
            missing_selectors.append(sel)
    assert not missing_selectors, f"Missing selectors in {code}: {missing_selectors}"

    # Save interactive HTML
    interactive_path = f"scratch/lectures/{code}_p1_interactive.html"
    with open(interactive_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Update Supabase
    print(f"Updating Supabase for {code} ({lid})...")
    res = sb.table('lecture_pages').update({
        'content_html': html
    }).eq('lecture_id', lid).eq('page_number', 1).execute()
    print(f"✅ {code} updated in Supabase successfully ({len(res.data)} page).")

print("\n🎉 ALL TOPIC 10 LECTURES SUCCESSFULLY UPDATED IN SUPABASE WITH DIFF=0!")
