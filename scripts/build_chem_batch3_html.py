import os
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

RAW_DIR = os.path.join(os.path.dirname(__file__), "raw_science_chem_phys")

def build_c9_html():
    raw_path = os.path.join(RAW_DIR, "c9_p1.html")
    with open(raw_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Replace the top study resources div with standard top gradient banner
    # In raw C9, line 2 has #sec-header wrapping Tài liệu học tập
    pattern_study = r'<div id="sec-header"[^>]*>.*?📚 Tài liệu học tập:.*?</div>'
    banner_c9 = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; padding: 25px 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin-bottom: 25px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255, 255, 255, 0.15); border: 1px solid rgba(255, 255, 255, 0.25); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <span style="background: #f97316; color: #ffffff; font-size: 12px; font-weight: 800; padding: 4px 12px; border-radius: 20px; text-transform: uppercase; letter-spacing: 1px;">Cambridge IGCSE Chemistry 0654</span>
  <h1 style="font-size: 26px; font-weight: 800; margin: 10px 0 6px 0; color: #ffffff;">C9: Metals &amp; Reactivity Series</h1>
  <p style="font-size: 14px; color: #cbd5e1; margin: 0; line-height: 1.6;">
    Comprehensive lecture notes covering properties of metals, alloy structures, the reactivity series, displacement reactions, blast furnace iron extraction, and essential uses of metals.
  </p>
</div>"""
    html = re.sub(pattern_study, banner_c9, html, flags=re.DOTALL)

    # 2. Sub-card for Alloys Hardness in Section 1 (#sec-properties-alloys)
    # The interactive model is in <div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; ...">
    old_alloy_box = '<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px;">'
    new_alloy_box = """<div id="sec-alloys-hardness" class="lecture-interactive-card" data-lecture-section="sec_alloys_hardness" style="background: #ffffff; border: 2px solid #fed7aa; border-left: 6px solid #f97316; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_alloy_box in html, "Could not find old_alloy_box in C9"
    html = html.replace(old_alloy_box, new_alloy_box, 1)

    # 3. Sub-cards in Section 2 (#sec-reactivity-series)
    # Sub-card 1: Mnemonic
    old_mnem = '<div style="background: #fffbeb; border: 2px solid #fde68a; border-radius: 12px; padding: 25px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">'
    new_mnem = """<div id="sec-reactivity-mnemonic" class="lecture-interactive-card" data-lecture-section="sec_reactivity_mnemonic" style="background: #fffbeb; border: 2px solid #fde68a; border-left: 6px solid #d97706; border-radius: 12px; padding: 25px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fef3c7; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_mnem in html, "Could not find old_mnem in C9"
    html = html.replace(old_mnem, new_mnem, 1)

    # Sub-card 2: Displacement reactions
    old_disp = '<div style="background: #fef2f2; border-left: 5px solid #ef4444; padding: 25px; border-radius: 0 12px 12px 0; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">'
    new_disp = """<div id="sec-displacement-reactions" class="lecture-interactive-card" data-lecture-section="sec_displacement_reactions" style="background: #fef2f2; border: 2px solid #fecaca; border-left: 6px solid #ef4444; padding: 25px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fee2e2; border: 1px solid #fca5a5; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b91c1c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_disp in html, "Could not find old_disp in C9"
    html = html.replace(old_disp, new_disp, 1)

    # 4. Sub-card in Section 3 (#sec-extraction-metals): Blast furnace
    old_blast = '<div style="background: #ffffff; border: 2px solid #fca5a5; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">'
    new_blast = """<div id="sec-blast-furnace" class="lecture-interactive-card" data-lecture-section="sec_blast_furnace" style="background: #ffffff; border: 2px solid #fca5a5; border-left: 6px solid #dc2626; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fee2e2; border: 1px solid #fca5a5; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b91c1c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_blast in html, "Could not find old_blast in C9"
    html = html.replace(old_blast, new_blast, 1)

    # 5. Sub-card in Section 4 (#sec-uses-metals): Specific uses grid
    old_uses = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">'
    new_uses = """<div id="sec-metal-uses-cases" class="lecture-interactive-card" data-lecture-section="sec_metal_uses_cases" style="background: #f8fafc; border: 2px solid #fed7aa; border-left: 6px solid #f97316; border-radius: 12px; padding: 25px; margin-top: 15px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 20px;">"""
    # Note: Because new_uses adds a wrapper div, we must close it before the section ends
    assert old_uses in html, "Could not find old_uses in C9"
    html = html.replace(old_uses, new_uses, 1)
    # The grid ends right before </div></div> at the end of the file
    # Let's close the new wrapper:
    html = html[:html.rfind('</div>\n</div>')] + '</div>\n</div>\n</div>'

    return html


def build_c10_html():
    raw_path = os.path.join(RAW_DIR, "c10_p1.html")
    with open(raw_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Top banner
    pattern_study = r'<div id="sec-header"[^>]*>.*?📚 Tài liệu học tập:.*?</div>'
    banner_c10 = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; padding: 25px 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin-bottom: 25px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255, 255, 255, 0.15); border: 1px solid rgba(255, 255, 255, 0.25); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <span style="background: #f97316; color: #ffffff; font-size: 12px; font-weight: 800; padding: 4px 12px; border-radius: 20px; text-transform: uppercase; letter-spacing: 1px;">Cambridge IGCSE Chemistry 0654</span>
  <h1 style="font-size: 26px; font-weight: 800; margin: 10px 0 6px 0; color: #ffffff;">C10: Chemistry of the Environment</h1>
  <p style="font-size: 14px; color: #cbd5e1; margin: 0; line-height: 1.6;">
    Comprehensive lecture notes covering water treatment and testing, atmospheric air composition, air pollutants and catalytic converters, rust prevention methods, and synthetic NPK fertilizers.
  </p>
</div>"""
    html = re.sub(pattern_study, banner_c10, html, flags=re.DOTALL)

    # 2. Section 1: Sub-card Water Treatment & Tests
    old_water = '<div style="background: #fefce8; border: 2px solid #fef08a; border-radius: 12px; padding: 25px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">'
    new_water = """<div id="sec-water-treatment" class="lecture-interactive-card" data-lecture-section="sec_water_treatment" style="background: #fefce8; border: 2px solid #fde047; border-left: 6px solid #eab308; border-radius: 12px; padding: 25px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fef9c3; border: 1px solid #fde047; border-radius: 20px; font-size: 12px; font-weight: 600; color: #a16207; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_water in html, "Could not find old_water in C10"
    html = html.replace(old_water, new_water, 1)

    # 3. Section 2: Sub-card Clean Air Composition
    old_air = '<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 40px;">'
    new_air = """<div id="sec-clean-air-composition" class="lecture-interactive-card" data-lecture-section="sec_clean_air_composition" style="background: #ffffff; border: 2px solid #bfdbfe; border-left: 6px solid #3b82f6; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 40px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_air in html, "Could not find old_air in C10"
    html = html.replace(old_air, new_air, 1)

    # 4. Section 2: Sub-card Catalytic Converters & Pollutants
    old_cat = '<div style="background: #ffffff; border: 2px solid #a5b4fc; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">'
    new_cat = """<div id="sec-pollutants-catalytic" class="lecture-interactive-card" data-lecture-section="sec_pollutants_catalytic" style="background: #ffffff; border: 2px solid #a5b4fc; border-left: 6px solid #6366f1; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #e0e7ff; border: 1px solid #c7d2fe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #4338ca; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_cat in html, "Could not find old_cat in C10"
    html = html.replace(old_cat, new_cat, 1)

    # 5. Section 3: Sub-card Rusting & Prevention
    old_rust = '<div style="background: #fffbeb; border-left: 5px solid #f59e0b; padding: 25px; border-radius: 0 12px 12px 0; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">'
    new_rust = """<div id="sec-rust-prevention" class="lecture-interactive-card" data-lecture-section="sec_rust_prevention" style="background: #fffbeb; border: 2px solid #fde68a; border-left: 6px solid #f59e0b; padding: 25px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fef3c7; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_rust in html, "Could not find old_rust in C10"
    html = html.replace(old_rust, new_rust, 1)

    # 6. Section 3: Sub-card NPK Fertilizers
    old_npk = '<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">'
    new_npk = """<div id="sec-npk-fertilizers" class="lecture-interactive-card" data-lecture-section="sec_npk_fertilizers" style="background: #f0fdf4; border: 2px solid #bbf7d0; border-left: 6px solid #22c55e; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #dcfce7; border: 1px solid #bbf7d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #15803d; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_npk in html, "Could not find old_npk in C10"
    html = html.replace(old_npk, new_npk, 1)

    return html


def build_c11_html():
    raw_path = os.path.join(RAW_DIR, "c11_p1.html")
    with open(raw_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Top banner
    pattern_study = r'<div id="sec-header"[^>]*>.*?📚 Tài liệu học tập:.*?</div>'
    banner_c11 = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; padding: 25px 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin-bottom: 25px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255, 255, 255, 0.15); border: 1px solid rgba(255, 255, 255, 0.25); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <span style="background: #f97316; color: #ffffff; font-size: 12px; font-weight: 800; padding: 4px 12px; border-radius: 20px; text-transform: uppercase; letter-spacing: 1px;">Cambridge IGCSE Chemistry 0654</span>
  <h1 style="font-size: 26px; font-weight: 800; margin: 10px 0 6px 0; color: #ffffff;">C11: Organic Chemistry &amp; Polymers</h1>
  <p style="font-size: 14px; color: #cbd5e1; margin: 0; line-height: 1.6;">
    Comprehensive lecture notes covering homologous series, IUPAC naming prefixes, saturated alkanes vs unsaturated alkenes, catalytic cracking, bromine water test, and addition polymerisation.
  </p>
</div>"""
    html = re.sub(pattern_study, banner_c11, html, flags=re.DOTALL)

    # 2. Section 1: Sub-card Prefix Naming
    old_prefix = '<div style="background: #f8fafc; border-left: 5px solid #64748b; padding: 20px; border-radius: 0 8px 8px 0; margin-bottom: 30px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">'
    new_prefix = """<div id="sec-naming-prefixes" class="lecture-interactive-card" data-lecture-section="sec_naming_prefixes" style="background: #f8fafc; border: 2px solid #cbd5e1; border-left: 6px solid #64748b; padding: 20px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 20px; font-size: 12px; font-weight: 600; color: #334155; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_prefix in html, "Could not find old_prefix in C11"
    html = html.replace(old_prefix, new_prefix, 1)

    # 3. Section 2: Sub-card Saturated vs Unsaturated Alkanes & Alkenes
    old_sat = '<div style="flex: 1; min-width: 300px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">'
    new_sat = """<div id="sec-alkanes-alkenes-diff" class="lecture-interactive-card" data-lecture-section="sec_alkanes_alkenes_diff" style="flex: 1; min-width: 300px; background: #ffffff; border: 2px solid #bfdbfe; border-left: 6px solid #3b82f6; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_sat in html, "Could not find old_sat in C11"
    html = html.replace(old_sat, new_sat, 1)

    # 4. Section 2: Sub-card Cracking & Bromine test
    # In C11, cracking is in a box and exam trap is in another box.
    # We can wrap both or put the card on Cracking. Let's make cracking the card container:
    old_crack = '<div style="flex: 1; min-width: 300px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">'
    new_crack = """<div id="sec-cracking-bromine" class="lecture-interactive-card" data-lecture-section="sec_cracking_bromine" style="flex: 1; min-width: 300px; background: #fffbeb; border: 2px solid #fde68a; border-left: 6px solid #f59e0b; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fef3c7; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_crack in html, "Could not find old_crack in C11"
    html = html.replace(old_crack, new_crack, 1)

    # 5. Section 3: Sub-card Addition Polymerisation
    old_poly = '<div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">'
    new_poly = """<div id="sec-addition-polymers" class="lecture-interactive-card" data-lecture-section="sec_addition_polymers" style="background: #f0fdf4; border: 2px solid #bbf7d0; border-left: 6px solid #22c55e; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #dcfce7; border: 1px solid #bbf7d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #15803d; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_poly in html, "Could not find old_poly in C11"
    html = html.replace(old_poly, new_poly, 1)

    return html


def build_c12_html():
    raw_path = os.path.join(RAW_DIR, "c12_p1.html")
    with open(raw_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Top banner
    pattern_study = r'<div id="sec-header"[^>]*>.*?📚 Tài liệu học tập:.*?</div>'
    banner_c12 = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; padding: 25px 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin-bottom: 25px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255, 255, 255, 0.15); border: 1px solid rgba(255, 255, 255, 0.25); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <span style="background: #f97316; color: #ffffff; font-size: 12px; font-weight: 800; padding: 4px 12px; border-radius: 20px; text-transform: uppercase; letter-spacing: 1px;">Cambridge IGCSE Chemistry 0654</span>
  <h1 style="font-size: 26px; font-weight: 800; margin: 10px 0 6px 0; color: #ffffff;">C12: Experimental Techniques &amp; Chemical Analysis</h1>
  <p style="font-size: 14px; color: #cbd5e1; margin: 0; line-height: 1.6;">
    Comprehensive lecture notes covering laboratory separation techniques, paper chromatography and Rf values, qualitative testing for common gases, and identification tests for cations and anions.
  </p>
</div>"""
    html = re.sub(pattern_study, banner_c12, html, flags=re.DOTALL)

    # 2. Section 1: Sub-card Filtration & Distillation Grid
    old_sep_grid = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 40px;">'
    new_sep_grid = """<div id="sec-filtration-crystallisation" class="lecture-interactive-card" data-lecture-section="sec_filtration_crystallisation" style="background: #f8fafc; border: 2px solid #fed7aa; border-left: 6px solid #f97316; border-radius: 12px; padding: 25px; margin-bottom: 40px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 15px;">"""
    assert old_sep_grid in html, "Could not find old_sep_grid in C12"
    # Replace and close the wrapper
    # In C12, old_sep_grid ends right before <div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px;">
    target_pos = html.find(old_sep_grid)
    next_pos = html.find('<div style="background: #ffffff; border: 2px solid #e2e8f0;', target_pos)
    # The grid ends right before next_pos with </div>
    # So we replace </div> before next_pos with </div></div>
    sub_slice = html[target_pos:next_pos]
    last_div = sub_slice.rfind('</div>')
    sub_slice_new = sub_slice[:last_div] + '</div></div>'
    sub_slice_new = sub_slice_new.replace(old_sep_grid, new_sep_grid, 1)
    html = html[:target_pos] + sub_slice_new + html[next_pos:]

    # 3. Section 1: Sub-card Paper Chromatography
    old_chroma = '<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px;">'
    new_chroma = """<div id="sec-chromatography-rf" class="lecture-interactive-card" data-lecture-section="sec_chromatography_rf" style="background: #ffffff; border: 2px solid #bfdbfe; border-left: 6px solid #3b82f6; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_chroma in html, "Could not find old_chroma in C12"
    html = html.replace(old_chroma, new_chroma, 1)

    # 4. Section 2: Sub-card Gas Tests Grid
    old_gas_grid = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">'
    new_gas_grid = """<div id="sec-gas-tests" class="lecture-interactive-card" data-lecture-section="sec_gas_tests" style="background: #f8fafc; border: 2px solid #fed7aa; border-left: 6px solid #f97316; border-radius: 12px; padding: 25px; margin-top: 15px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 15px; margin-top: 15px;">"""
    assert old_gas_grid in html, "Could not find old_gas_grid in C12"
    # Next section is #sec-ion-identification
    target_pos = html.find(old_gas_grid)
    next_pos = html.find('<div id="sec-ion-identification"', target_pos)
    # The grid ends right before next_pos with </div></div> (section ends)
    sub_slice = html[target_pos:next_pos]
    last_div = sub_slice.rfind('</div>')
    # replace that </div> with </div></div>
    sub_slice_new = sub_slice[:last_div] + '</div></div>'
    sub_slice_new = sub_slice_new.replace(old_gas_grid, new_gas_grid, 1)
    html = html[:target_pos] + sub_slice_new + html[next_pos:]

    # 5. Section 3: Sub-card Testing for Anions
    # In Section 3: table for Anions and exam warning box
    # Let's wrap the Anions table in a sub-card
    old_anion_tbl = '<div style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 40px;">'
    new_anion_tbl = """<div id="sec-anion-tests" class="lecture-interactive-card" data-lecture-section="sec_anion_tests" style="background: #ffffff; border: 2px solid #fecaca; border-left: 6px solid #ef4444; border-radius: 12px; padding: 25px; margin-bottom: 40px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fee2e2; border: 1px solid #fca5a5; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b91c1c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>
  <div style="overflow-x: auto; background: #ffffff; border-radius: 8px; border: 1px solid #e2e8f0; margin-top: 15px;">"""
    assert old_anion_tbl in html, "Could not find old_anion_tbl in C12"
    target_pos = html.find(old_anion_tbl)
    next_pos = html.find('<div style="background: #fefce8;', target_pos)
    sub_slice = html[target_pos:next_pos]
    last_div = sub_slice.rfind('</div>')
    sub_slice_new = sub_slice[:last_div] + '</div></div>'
    sub_slice_new = sub_slice_new.replace(old_anion_tbl, new_anion_tbl, 1)
    html = html[:target_pos] + sub_slice_new + html[next_pos:]

    # 6. Section 3: Sub-card Testing for Cations
    old_cat_grid = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px;">'
    new_cat_grid = """<div id="sec-cation-tests" class="lecture-interactive-card" data-lecture-section="sec_cation_tests" style="background: #f8fafc; border: 2px solid #bfdbfe; border-left: 6px solid #3b82f6; border-radius: 12px; padding: 25px; margin-top: 15px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 15px; margin-top: 15px;">"""
    assert old_cat_grid in html, "Could not find old_cat_grid in C12"
    # The grid ends right before </div></div> at the very end of the file
    html = html[:html.rfind('</div>\n</div>')] + '</div>\n</div>\n</div>'
    html = html.replace(old_cat_grid, new_cat_grid, 1)

    return html


def verify_and_save():
    builders = [
        ("c9", build_c9_html),
        ("c10", build_c10_html),
        ("c11", build_c11_html),
        ("c12", build_c12_html),
    ]
    
    for code, builder in builders:
        html = builder()
        opens = len(re.findall(r'<div\b[^>]*>', html))
        closes = len(re.findall(r'</div>', html))
        diff = opens - closes
        has_tl = "Tài liệu học tập" in html or "Study Resources" in html
        print(f"[{code.upper()}] opens={opens}, closes={closes}, diff={diff}, has_study_resources={has_tl}")
        assert diff == 0, f"Div mismatch for {code}: diff={diff}"
        assert not has_tl, f"Study resources found in {code}"
        
        out_path = os.path.join(RAW_DIR, f"{code}_p1_transformed.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  -> Saved {out_path}")

if __name__ == '__main__':
    verify_and_save()
