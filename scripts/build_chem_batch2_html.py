import os
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# =====================================================================
# C5 HTML TRANSFORMER
# =====================================================================
def build_c5_html():
    raw_path = "scripts/raw_science_chem_phys/c5_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Top banner
    banner_code = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%); padding: 28px 32px; border-radius: 14px; color: #ffffff; margin-bottom: 25px; box-shadow: 0 10px 25px -5px rgba(30,58,138,0.25); cursor: pointer; transition: all 0.2s ease; position: relative;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #93c5fd; margin-bottom: 6px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Chemistry</div>
  <h1 style="margin: 0; font-size: 30px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px; padding-right: 140px;">C5: Chemical Energetics</h1>
  <p style="margin: 8px 0 0 0; font-size: 15.5px; color: #e0f2fe; opacity: 0.95; line-height: 1.5;">Exothermic &amp; Endothermic Reactions, Energy Level Diagrams, Activation Energy &amp; Bond Calculations</p>
</div>"""

    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', banner_code + '\n', html, flags=re.DOTALL)

    # 2. Section 1 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-exo-endo"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 1"),
        html,
        flags=re.DOTALL
    )

    # Exothermic card
    html = re.sub(
        r'<div style="flex: 1; min-width: 280px; background: #ffffff; border: 2px solid #fecaca; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; color: #b91c1c; font-size: 22px;">🔥 Exothermic</h3>',
        """<div id="sec-exothermic" class="lecture-interactive-card" data-lecture-section="sec_exothermic" style="flex: 1; min-width: 280px; background: #ffffff; border: 1.5px solid #fecaca; border-top: 4px solid #ef4444; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #b91c1c; background: #fef2f2; padding: 2px 6px; border-radius: 8px; border: 1px solid #fecaca; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #b91c1c; font-size: 22px; padding-right: 80px;">🔥 Exothermic</h3>""",
        html
    )

    # Endothermic card
    html = re.sub(
        r'<div style="flex: 1; min-width: 280px; background: #ffffff; border: 2px solid #bfdbfe; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; color: #1d4ed8; font-size: 22px;">❄️ Endothermic</h3>',
        """<div id="sec-endothermic" class="lecture-interactive-card" data-lecture-section="sec_endothermic" style="flex: 1; min-width: 280px; background: #ffffff; border: 1.5px solid #bfdbfe; border-top: 4px solid #3b82f6; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #1d4ed8; font-size: 22px; padding-right: 80px;">❄️ Endothermic</h3>""",
        html
    )

    # 3. Section 2 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-reaction-profiles"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 2"),
        html,
        flags=re.DOTALL
    )

    # Energy profiles card
    html = re.sub(
        r'<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba\(0,0,0,0.05\); margin-bottom: 40px;">\s*<h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive Energy Diagrams</h3>',
        """<div id="sec-energy-profiles" class="lecture-interactive-card" data-lecture-section="sec_energy_profiles" style="background: #ffffff; border: 1.5px solid #fed7aa; border-left: 5px solid #f97316; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #c2410c; background: #fff7ed; padding: 2px 6px; border-radius: 8px; border: 1px solid #fed7aa; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px; padding-right: 80px;">Interactive Energy Diagrams</h3>""",
        html
    )

    # 4. Section 3 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-bond-energies"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 3"),
        html,
        flags=re.DOTALL
    )

    # MEX-BENDO card
    html = re.sub(
        r'<div style="background: #fefce8; border: 2px solid #fef08a; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\); margin-bottom: 30px;">\s*<h3 style="margin: 0 0 15px 0; color: #a16207; font-size: 20px;">🧠 IGCSE Mnemonic: "MEX - BENDO"</h3>',
        """<div id="sec-mex-bendo" class="lecture-interactive-card" data-lecture-section="sec_mex_bendo" style="background: #fefce8; border: 1.5px solid #fef08a; border-left: 5px solid #f59e0b; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 30px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #a16207; background: #fffbeb; padding: 2px 6px; border-radius: 8px; border: 1px solid #fef08a; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #a16207; font-size: 20px; padding-right: 80px;">🧠 IGCSE Mnemonic: "MEX - BENDO"</h3>""",
        html
    )

    # Calculating Enthalpy card
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; color: #0f172a; font-size: 20px;">🧮 Calculating Overall Enthalpy Change \(ΔH\)</h3>',
        """<div id="sec-calc-enthalpy" class="lecture-interactive-card" data-lecture-section="sec_calc_enthalpy" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 5px solid #10b981; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #0f172a; font-size: 20px; padding-right: 80px;">🧮 Calculating Overall Enthalpy Change (ΔH)</h3>""",
        html
    )

    # Fix the missing formula in calculating delta H
    html = html.replace(
        '<p style="margin: 0; font-family: monospace; font-size: 20px; font-weight: bold; color: #047857; text-align: center;">ΔH = -</p>',
        '<p style="margin: 0; font-family: monospace; font-size: 19px; font-weight: bold; color: #047857; text-align: center;">ΔH = Σ(Bonds Broken) − Σ(Bonds Formed)</p>'
    )

    return html


# =====================================================================
# C6 HTML TRANSFORMER
# =====================================================================
def build_c6_html():
    raw_path = "scripts/raw_science_chem_phys/c6_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Top banner
    banner_code = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%); padding: 28px 32px; border-radius: 14px; color: #ffffff; margin-bottom: 25px; box-shadow: 0 10px 25px -5px rgba(30,58,138,0.25); cursor: pointer; transition: all 0.2s ease; position: relative;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #93c5fd; margin-bottom: 6px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Chemistry</div>
  <h1 style="margin: 0; font-size: 30px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px; padding-right: 140px;">C6: Chemical Reactions</h1>
  <p style="margin: 8px 0 0 0; font-size: 15.5px; color: #e0f2fe; opacity: 0.95; line-height: 1.5;">Physical vs. Chemical Changes, Collision Theory, Rate Factors, Dynamic Equilibrium &amp; Redox</p>
</div>"""

    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', banner_code + '\n', html, flags=re.DOTALL)

    # 2. Section 1 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-physical-chemical"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 1"),
        html,
        flags=re.DOTALL
    )

    # Physical vs Chemical differences card
    html = re.sub(
        r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(320px, 1fr\)\); gap: 24px; margin-bottom: 35px;">',
        """<div id="sec-phys-chem-diff" class="lecture-interactive-card" data-lecture-section="sec_phys_chem_diff" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-left: 5px solid #3b82f6; border-radius: 12px; padding: 20px; margin-bottom: 35px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; margin-top: 15px;">""",
        html
    )
    # close the extra wrapper div before the 4 observations
    html = re.sub(
        r'(\s*</div>\s*)(<h3 style="color: #0f172a; font-size: 22px; margin-bottom: 20px;">🔍 4 Key Observations Showing a Chemical Reaction</h3>)',
        r'\1</div>\n\2',
        html
    )

    # 4 Observations card
    html = re.sub(
        r'<h3 style="color: #0f172a; font-size: 22px; margin-bottom: 20px;">🔍 4 Key Observations Showing a Chemical Reaction</h3>\s*<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(240px, 1fr\)\); gap: 18px; margin-bottom: 35px;">',
        """<div id="sec-chem-observations" class="lecture-interactive-card" data-lecture-section="sec_chem_observations" style="background: #ffffff; border: 1.5px solid #fed7aa; border-left: 5px solid #f97316; border-radius: 12px; padding: 24px; margin-bottom: 35px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 16px; right: 16px; font-size: 11px; font-weight: 600; color: #c2410c; background: #fff7ed; padding: 2px 6px; border-radius: 8px; border: 1px solid #fed7aa; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="color: #0f172a; font-size: 22px; margin: 0 0 20px 0; padding-right: 90px;">🔍 4 Key Observations Showing a Chemical Reaction</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 18px;">""",
        html
    )
    # close extra div before Interactive Particle-Level Model
    html = re.sub(
        r'(\s*</div>\s*)(<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba\(0,0,0,0.05\); margin-bottom: 35px;">\s*<h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive Particle-Level Model)',
        r'\1</div>\n\2',
        html
    )

    # 3. Section 2 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-rate-of-reaction"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 2"),
        html,
        flags=re.DOTALL
    )

    # Collision Theory card
    html = re.sub(
        r'<div style="background: #eff6ff; border-left: 5px solid #3b82f6; padding: 25px; border-radius: 0 12px 12px 0; margin-bottom: 30px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 10px 0; color: #1e3a8a; font-size: 20px;">💥 Collision Theory \(Thuyết va chạm\)</h3>',
        """<div id="sec-collision-theory" class="lecture-interactive-card" data-lecture-section="sec_collision_theory" style="background: #eff6ff; border: 1.5px solid #bfdbfe; border-left: 5px solid #2563eb; border-radius: 12px; padding: 25px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #dbeafe; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 10px 0; color: #1e3a8a; font-size: 20px; padding-right: 80px;">💥 Collision Theory (Thuyết va chạm)</h3>""",
        html
    )

    # Rate Factors card
    html = re.sub(
        r'<h3 style="color: #0f172a; font-size: 22px; margin-bottom: 20px;">🚀 4 Factors Affecting Rate of Reaction</h3>\s*<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(280px, 1fr\)\); gap: 20px; margin-bottom: 30px;">',
        """<div id="sec-rate-factors" class="lecture-interactive-card" data-lecture-section="sec_rate_factors" style="background: #ffffff; border: 1.5px solid #bbf7d0; border-left: 5px solid #10b981; border-radius: 12px; padding: 24px; margin-bottom: 30px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 16px; right: 16px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="color: #0f172a; font-size: 22px; margin: 0 0 20px 0; padding-right: 90px;">🚀 4 Factors Affecting Rate of Reaction</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">""",
        html
    )
    # close the extra wrapper div before the warning box
    html = re.sub(
        r'(\s*</div>\s*)(<div style="background: #fefce8; border: 2px solid #fef08a;)',
        r'\1</div>\n\2',
        html,
        count=1
    )

    # 4. Section 3 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-reversible-equilibrium"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 3"),
        html,
        flags=re.DOTALL
    )

    # Dynamic equilibrium card
    html = re.sub(
        r'<div style="background: #ecfdf5; border-left: 5px solid #10b981; padding: 25px; border-radius: 0 12px 12px 0; margin-bottom: 30px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 10px 0; color: #047857; font-size: 20px;">Phản ứng Thuận nghịch \(⇌\)</h3>',
        """<div id="sec-dynamic-equilibrium" class="lecture-interactive-card" data-lecture-section="sec_dynamic_equilibrium" style="background: #ecfdf5; border: 1.5px solid #a7f3d0; border-left: 5px solid #059669; border-radius: 12px; padding: 25px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 10px 0; color: #047857; font-size: 20px; padding-right: 80px;">Phản ứng Thuận nghịch (⇌)</h3>""",
        html
    )

    # Haber Process card
    html = re.sub(
        r'<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 10px 0; color: #0f172a; font-size: 20px;">🏭 Ứng dụng: The Haber Process',
        """<div id="sec-haber-process" class="lecture-interactive-card" data-lecture-section="sec_haber_process" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-left: 5px solid #0284c7; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #0284c7; background: #f0f9ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 10px 0; color: #0f172a; font-size: 20px; padding-right: 80px;">🏭 Ứng dụng: The Haber Process""",
        html
    )

    # 5. Section 4 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-redox-reactions"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 4"),
        html,
        flags=re.DOTALL
    )

    # Redox definitions (OIL RIG) card
    html = re.sub(
        r'<div style="background: #fdf2f8; border: 2px solid #fbcfe8; border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 30px;">\s*<h4 style="margin: 0 0 5px 0; color: #be185d; font-size: 22px;">🧠 Essential Mnemonic: "OIL RIG"</h4>',
        """<div id="sec-redox-definitions" class="lecture-interactive-card" data-lecture-section="sec_redox_definitions" style="background: #fdf2f8; border: 1.5px solid #fbcfe8; border-left: 5px solid #db2777; border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 30px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #be185d; background: #fff1f2; padding: 2px 6px; border-radius: 8px; border: 1px solid #fbcfe8; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 5px 0; color: #be185d; font-size: 22px; padding-right: 70px;">🧠 Essential Mnemonic: "OIL RIG"</h4>""",
        html
    )

    # Chemical tests for redox card
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 25px; margin-bottom: 25px; box-shadow: 0 4px 6px -1px rgba\(0,0,0,0.03\);">\s*<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">\s*<span style="background: #fef3c7; color: #b45309; border: 1px solid #fde68a; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 13px;">Cambridge Practical</span>\s*<h4 style="margin: 0; color: #1e293b; font-size: 18px;">🧪 Chemical Tests for Redox Agents</h4>',
        """<div id="sec-redox-tests" class="lecture-interactive-card" data-lecture-section="sec_redox_tests" style="background: #ffffff; border: 1.5px solid #ddd6fe; border-left: 5px solid #8b5cf6; border-radius: 14px; padding: 25px; margin-bottom: 25px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 16px; right: 16px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #f5f3ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #ddd6fe; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px; padding-right: 90px;">
          <span style="background: #fef3c7; color: #b45309; border: 1px solid #fde68a; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 13px;">Cambridge Practical</span>
          <h4 style="margin: 0; color: #1e293b; font-size: 18px;">🧪 Chemical Tests for Redox Agents</h4>""",
        html
    )

    return html


# =====================================================================
# C7 HTML TRANSFORMER
# =====================================================================
def build_c7_html():
    raw_path = "scripts/raw_science_chem_phys/c7_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Top banner
    banner_code = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%); padding: 28px 32px; border-radius: 14px; color: #ffffff; margin-bottom: 25px; box-shadow: 0 10px 25px -5px rgba(30,58,138,0.25); cursor: pointer; transition: all 0.2s ease; position: relative;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #93c5fd; margin-bottom: 6px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Chemistry</div>
  <h1 style="margin: 0; font-size: 30px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px; padding-right: 140px;">C7: Acids, Bases &amp; Salts</h1>
  <p style="margin: 8px 0 0 0; font-size: 15.5px; color: #e0f2fe; opacity: 0.95; line-height: 1.5;">Proton Donors &amp; Acceptors, pH Scale, Characteristic Acid Reactions &amp; Salt Synthesis</p>
</div>"""

    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', banner_code + '\n', html, flags=re.DOTALL)

    # 2. Section 1 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-acids-bases"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 1"),
        html,
        flags=re.DOTALL
    )

    # Acids vs Bases vs Alkalis card
    html = re.sub(
        r'<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin-bottom: 30px;">\s*<div style="flex: 1; min-width: 280px; background: #fef2f2;',
        """<div id="sec-acids-bases-def" class="lecture-interactive-card" data-lecture-section="sec_acids_bases_def" style="background: #ffffff; border: 1.5px solid #fecaca; border-left: 5px solid #ef4444; border-radius: 12px; padding: 20px; margin-bottom: 30px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #b91c1c; background: #fef2f2; padding: 2px 6px; border-radius: 8px; border: 1px solid #fecaca; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin-top: 15px;">
        <div style="flex: 1; min-width: 280px; background: #fef2f2;""",
        html
    )
    # close the extra wrapper div before the EXAM TRAP WARNING
    html = re.sub(
        r'(\s*</div>\s*</div>\s*)(<div style="background: #fefce8; border: 2px solid #fef08a; border-radius: 12px; padding: 20px; margin-bottom: 40px;">\s*<h3 style="margin: 0 0 10px 0; color: #a16207; font-size: 18px;">🚨 EXAM TRAP WARNING)',
        r'\1</div>\n\2',
        html
    )

    # Interactive pH Scale card
    html = re.sub(
        r'<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba\(0,0,0,0.05\);">\s*<h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive pH Scale &amp; Universal Indicator</h3>',
        """<div id="sec-ph-scale" class="lecture-interactive-card" data-lecture-section="sec_ph_scale" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 5px solid #10b981; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px; padding-right: 80px;">Interactive pH Scale &amp; Universal Indicator</h3>""",
        html
    )

    # 3. Section 2 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-acid-reactions"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 2"),
        html,
        flags=re.DOTALL
    )

    # 3 Acid reactions card
    html = re.sub(
        r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(300px, 1fr\)\); gap: 20px; margin-bottom: 30px;">',
        """<div id="sec-three-acid-reactions" class="lecture-interactive-card" data-lecture-section="sec_three_acid_reactions" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-left: 5px solid #3b82f6; border-radius: 12px; padding: 20px; margin-bottom: 30px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 15px;">""",
        html
    )
    # close the extra wrapper div before the EXAM TRAP WARNING
    html = re.sub(
        r'(\s*</div>\s*)(<div style="background: #fefce8; border: 2px solid #fef08a; border-radius: 12px; padding: 20px; display: flex; gap: 20px; align-items: center;">\s*<div style="font-size: 30px;">🚨</div>\s*<div>\s*<h3 style="margin: 0 0 5px 0; color: #a16207; font-size: 18px;">CẢNH BÁO BẪY ĐỀ THI: Phản ứng với Đồng</h3>)',
        r'\1</div>\n\2',
        html
    )

    # 4. Section 3 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-salt-preparation"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 3"),
        html,
        flags=re.DOTALL
    )

    # SNAP solubility card
    html = re.sub(
        r'<div style="background: #f3e8ff; border-left: 5px solid #8b5cf6; padding: 25px; border-radius: 0 12px 12px 0; margin-bottom: 30px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 10px 0; color: #6b21a8; font-size: 20px;">🧠 IGCSE Memory Tip: "SNAP" Rule for Soluble Salts</h3>',
        """<div id="sec-solubility-rules" class="lecture-interactive-card" data-lecture-section="sec_solubility_rules" style="background: #f3e8ff; border: 1.5px solid #d8b4fe; border-left: 5px solid #8b5cf6; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 30px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #7e22ce; background: #faf5ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #d8b4fe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 10px 0; color: #6b21a8; font-size: 20px; padding-right: 80px;">🧠 IGCSE Memory Tip: "SNAP" Rule for Soluble Salts</h3>""",
        html
    )

    # 3 Salt methods card
    html = re.sub(
        r'<h3 style="color: #0f172a; font-size: 22px; margin-bottom: 20px;">⚙️ The 3 Methods of Salt Preparation \(The 3 Methods\)</h3>\s*<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(250px, 1fr\)\); gap: 20px;">',
        """<div id="sec-salt-methods" class="lecture-interactive-card" data-lecture-section="sec_salt_methods" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-left: 5px solid #0284c7; border-radius: 12px; padding: 24px; margin-bottom: 30px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 16px; right: 16px; font-size: 11px; font-weight: 600; color: #0284c7; background: #f0f9ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="color: #0f172a; font-size: 22px; margin: 0 0 20px 0; padding-right: 90px;">⚙️ The 3 Methods of Salt Preparation (The 3 Methods)</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">""",
        html
    )
    # close the extra wrapper div at the end of Section 3
    html = re.sub(
        r'(\s*</div>\s*</div>\s*</div>\s*</div>\s*)$',
        r'</div>\n\1',
        html
    )

    return html


# =====================================================================
# C8 HTML TRANSFORMER
# =====================================================================
def build_c8_html():
    raw_path = "scripts/raw_science_chem_phys/c8_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Top banner
    banner_code = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%); padding: 28px 32px; border-radius: 14px; color: #ffffff; margin-bottom: 25px; box-shadow: 0 10px 25px -5px rgba(30,58,138,0.25); cursor: pointer; transition: all 0.2s ease; position: relative;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #93c5fd; margin-bottom: 6px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Chemistry</div>
  <h1 style="margin: 0; font-size: 30px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px; padding-right: 140px;">C8: The Periodic Table</h1>
  <p style="margin: 8px 0 0 0; font-size: 15.5px; color: #e0f2fe; opacity: 0.95; line-height: 1.5;">Periods, Groups, Group I Alkali Metals vs. Group VII Halogens, Transition Metals &amp; Noble Gases</p>
</div>"""

    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', banner_code + '\n', html, flags=re.DOTALL)

    # 2. Section 1 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-arrangement-elements"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 1"),
        html,
        flags=re.DOTALL
    )

    # Periods & Groups card
    html = re.sub(
        r'<div style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 30px;">\s*<div style="flex: 1; min-width: 280px; background: #eff6ff;',
        """<div id="sec-periods-groups" class="lecture-interactive-card" data-lecture-section="sec_periods_groups" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-left: 5px solid #3b82f6; border-radius: 12px; padding: 20px; margin-bottom: 30px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: flex; flex-wrap: wrap; gap: 20px; margin-top: 15px;">
        <div style="flex: 1; min-width: 280px; background: #eff6ff;""",
        html
    )
    # close the extra wrapper div
    html = re.sub(
        r'(\s*</div>\s*</div>\s*)(</div>\s*<div id="sec-group-trends")',
        r'\1</div>\n\2',
        html
    )

    # 3. Section 2 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-group-trends"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 2"),
        html,
        flags=re.DOTALL
    )

    # Group 1 Alkali Metals card
    html = re.sub(
        r'<div style="flex: 1; min-width: 320px; background: #ffffff; border: 2px solid #93c5fd; border-radius: 12px; padding: 30px; box-shadow: 0 4px 10px rgba\(0,0,0,0.05\);">\s*<h3 style="margin: 0 0 5px 0; color: #1d4ed8; font-size: 22px;">🔵 Group I: Alkali Metals</h3>',
        """<div id="sec-group1-metals" class="lecture-interactive-card" data-lecture-section="sec_group1_metals" style="flex: 1; min-width: 320px; background: #ffffff; border: 1.5px solid #93c5fd; border-top: 4px solid #2563eb; border-radius: 12px; padding: 30px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 5px 0; color: #1d4ed8; font-size: 22px; padding-right: 80px;">🔵 Group I: Alkali Metals</h3>""",
        html
    )

    # Group 7 Halogens card
    html = re.sub(
        r'<div style="flex: 1; min-width: 320px; background: #ffffff; border: 2px solid #f9a8d4; border-radius: 12px; padding: 30px; box-shadow: 0 4px 10px rgba\(0,0,0,0.05\);">\s*<h3 style="margin: 0 0 5px 0; color: #be185d; font-size: 22px;">🟣 Group VII: Halogens</h3>',
        """<div id="sec-group7-halogens" class="lecture-interactive-card" data-lecture-section="sec_group7_halogens" style="flex: 1; min-width: 320px; background: #ffffff; border: 1.5px solid #f9a8d4; border-top: 4px solid #db2777; border-radius: 12px; padding: 30px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #be185d; background: #fdf2f8; padding: 2px 6px; border-radius: 8px; border: 1px solid #fbcfe8; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 5px 0; color: #be185d; font-size: 22px; padding-right: 80px;">🟣 Group VII: Halogens</h3>""",
        html
    )

    # 4. Section 3 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-transition-noblegases"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 3"),
        html,
        flags=re.DOTALL
    )

    # Transition elements card
    html = re.sub(
        r'<div style="flex: 1; min-width: 300px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; color: #047857; font-size: 20px;">🛡️ Transition Elements</h3>',
        """<div id="sec-transition-elements" class="lecture-interactive-card" data-lecture-section="sec_transition_elements" style="flex: 1; min-width: 300px; background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 5px solid #10b981; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #047857; font-size: 20px; padding-right: 80px;">🛡️ Transition Elements</h3>""",
        html
    )

    # Noble gases card
    html = re.sub(
        r'<div style="flex: 1; min-width: 300px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; color: #8b5cf6; font-size: 20px;">🎈 Group VIII / 0: Noble Gases</h3>',
        """<div id="sec-noble-gases" class="lecture-interactive-card" data-lecture-section="sec_noble_gases" style="flex: 1; min-width: 300px; background: #ffffff; border: 1.5px solid #ddd6fe; border-left: 5px solid #8b5cf6; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #f5f3ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #ddd6fe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #8b5cf6; font-size: 20px; padding-right: 80px;">🎈 Group VIII / 0: Noble Gases</h3>""",
        html
    )

    return html

def verify_div_balance(name, html):
    opens = len(re.findall(r'<div\b[^>]*>', html))
    closes = len(re.findall(r'</div>', html))
    diff = opens - closes
    print(f"  {name}: opens={opens}, closes={closes}, diff={diff}")
    assert diff == 0, f"Div balance mismatch in {name}: diff={diff}"

if __name__ == '__main__':
    print("Testing C5-C8 HTML Transformations & Div Balance...")
    c5 = build_c5_html()
    verify_div_balance("C5", c5)
    with open("scripts/raw_science_chem_phys/c5_p1_transformed.html", "w", encoding="utf-8") as f:
        f.write(c5)

    c6 = build_c6_html()
    verify_div_balance("C6", c6)
    with open("scripts/raw_science_chem_phys/c6_p1_transformed.html", "w", encoding="utf-8") as f:
        f.write(c6)

    c7 = build_c7_html()
    verify_div_balance("C7", c7)
    with open("scripts/raw_science_chem_phys/c7_p1_transformed.html", "w", encoding="utf-8") as f:
        f.write(c7)

    c8 = build_c8_html()
    verify_div_balance("C8", c8)
    with open("scripts/raw_science_chem_phys/c8_p1_transformed.html", "w", encoding="utf-8") as f:
        f.write(c8)

    print("🎉 ALL C5-C8 HTML TRANSFORMED AND PASSED DIV BALANCE VERIFICATION!")
