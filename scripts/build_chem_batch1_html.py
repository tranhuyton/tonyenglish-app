import os
import sys
import re
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# =====================================================================
# C1 HTML TRANSFORMER
# =====================================================================
def build_c1_html():
    raw_path = "scripts/raw_science_chem_phys/c1_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # 2. Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%\);[^>]*>(.*?)</div>\s*<div style="margin-bottom: 35px;'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%); padding: 28px 32px; border-radius: 14px; color: #ffffff; margin-bottom: 25px; box-shadow: 0 10px 25px -5px rgba(30,58,138,0.25); cursor: pointer; transition: all 0.2s ease; position: relative;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #93c5fd; margin-bottom: 6px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Chemistry</div>
  <h1 style="margin: 0; font-size: 30px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px; padding-right: 140px;">C1: States of Matter</h1>
  <p style="margin: 8px 0 0 0; font-size: 15.5px; color: #e0f2fe; opacity: 0.95; line-height: 1.5;">Kinetic Particle Theory, Changes of State, Heating Curves, Gas Laws &amp; Molecular Diffusion</p>
</div>

<div style="margin-bottom: 35px;"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # 3. Section 1 Header Badge
    html = html.replace(
        '<div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>',
        '<div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        1
    )

    # Sub-cards in Section 1: Solid, Liquid, Gas
    # Solid
    html = re.sub(
        r'<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-top: 4px solid #3b82f6; border-radius: 10px; padding: 20px;">\s*<h3 style="margin: 0 0 12px 0; color: #1d4ed8; font-size: 19px;">🧊 Solid</h3>',
        """<div id="sec-solid" class="lecture-interactive-card" data-lecture-section="sec_solid" style="background: #f8fafc; border: 1.5px solid #bfdbfe; border-top: 4px solid #3b82f6; border-radius: 10px; padding: 20px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; color: #1d4ed8; font-size: 19px; padding-right: 80px;">🧊 Solid</h3>""",
        html
    )

    # Liquid
    html = re.sub(
        r'<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-top: 4px solid #10b981; border-radius: 10px; padding: 20px;">\s*<h3 style="margin: 0 0 12px 0; color: #047857; font-size: 19px;">💧 Liquid</h3>',
        """<div id="sec-liquid" class="lecture-interactive-card" data-lecture-section="sec_liquid" style="background: #f8fafc; border: 1.5px solid #a7f3d0; border-top: 4px solid #10b981; border-radius: 10px; padding: 20px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; color: #047857; font-size: 19px; padding-right: 80px;">💧 Liquid</h3>""",
        html
    )

    # Gas
    html = re.sub(
        r'<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-top: 4px solid #ef4444; border-radius: 10px; padding: 20px;">\s*<h3 style="margin: 0 0 12px 0; color: #b91c1c; font-size: 19px;">💨 Gas</h3>',
        """<div id="sec-gas" class="lecture-interactive-card" data-lecture-section="sec_gas" style="background: #f8fafc; border: 1.5px solid #fecaca; border-top: 4px solid #ef4444; border-radius: 10px; padding: 20px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #b91c1c; background: #fef2f2; padding: 2px 6px; border-radius: 8px; border: 1px solid #fecaca; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; color: #b91c1c; font-size: 19px; padding-right: 80px;">💨 Gas</h3>""",
        html
    )

    # 4. Section 2 Header Badge & Sub-cards
    sec2_badge = '<div id="sec-heating-curves"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>'
    def replace_sec2_badge(m):
        return m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 2")
    html = re.sub(sec2_badge, replace_sec2_badge, html, flags=re.DOTALL)

    # Boiling vs Evaporation card
    html = re.sub(
        r'<div style="background: #fff7ed; border-left: 4px solid #f97316; padding: 16px 20px; border-radius: 8px; margin-bottom: 20px;">',
        """<div id="sec-boiling-evap" class="lecture-interactive-card" data-lecture-section="sec_boiling_evap" style="background: #fff7ed; border: 1.5px solid #fed7aa; border-left: 5px solid #f97316; padding: 18px 20px; border-radius: 10px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #c2410c; background: #fff7ed; padding: 2px 6px; border-radius: 8px; border: 1px solid #fed7aa; pointer-events: none;">🎧 Nghe mục này</div>""",
        html
    )

    # Heating curve plateau card
    html = re.sub(
        r'<h3 style="color: #0f172a; font-size: 17px; margin: 20px 0 10px 0;">Heating Curves &amp; Temperature Plateaus</h3>\s*<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; text-align: center; margin-bottom: 14px;">(.*?)<div style="background: #f0fdf4; border-left: 4px solid #16a34a; padding: 12px 18px; border-radius: 6px; font-size: 14px; color: #166534;">(.*?)</div>\s*</div>',
        """<div id="sec-heating-plateau" class="lecture-interactive-card" data-lecture-section="sec_heating_plateau" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-left: 5px solid #3b82f6; border-radius: 10px; padding: 20px; margin-bottom: 14px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="color: #0f172a; font-size: 17px; margin: 0 0 12px 0; padding-right: 90px;">Heating Curves &amp; Temperature Plateaus</h3>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; text-align: center; margin-bottom: 14px;">\\1</div>
        <div style="background: #f0fdf4; border-left: 4px solid #16a34a; padding: 12px 18px; border-radius: 6px; font-size: 14px; color: #166534;">\\2</div>
      </div>""",
        html,
        flags=re.DOTALL
    )

    # 5. Section 3 Header Badge & Sub-cards
    sec3_badge = '<div id="sec-gas-behavior"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>'
    def replace_sec3_badge(m):
        return m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 3")
    html = re.sub(sec3_badge, replace_sec3_badge, html, flags=re.DOTALL)

    # Gas Temp
    html = re.sub(
        r'<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 18px;">\s*<h3 style="margin: 0 0 10px 0; color: #b45309; font-size: 17px;">🌡️ Effect of Temperature</h3>',
        """<div id="sec-gas-temp" class="lecture-interactive-card" data-lecture-section="sec_gas_temp" style="background: #fffbeb; border: 1.5px solid #fde68a; border-left: 5px solid #f59e0b; border-radius: 10px; padding: 18px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #b45309; background: #fef3c7; padding: 2px 6px; border-radius: 8px; border: 1px solid #fde68a; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 10px 0; color: #b45309; font-size: 17px; padding-right: 80px;">🌡️ Effect of Temperature</h3>""",
        html
    )

    # Gas Pressure
    html = re.sub(
        r'<div style="background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 10px; padding: 18px;">\s*<h3 style="margin: 0 0 10px 0; color: #0284c7; font-size: 17px;">🗜️ Effect of Pressure</h3>',
        """<div id="sec-gas-pressure" class="lecture-interactive-card" data-lecture-section="sec_gas_pressure" style="background: #f0f9ff; border: 1.5px solid #bae6fd; border-left: 5px solid #0284c7; border-radius: 10px; padding: 18px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #0284c7; background: #e0f2fe; padding: 2px 6px; border-radius: 8px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 10px 0; color: #0284c7; font-size: 17px; padding-right: 80px;">🗜️ Effect of Pressure</h3>""",
        html
    )

    # 6. Section 4 Header Badge & Sub-cards
    sec4_badge = '<div id="sec-diffusion-mass"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>'
    def replace_sec4_badge(m):
        return m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 4")
    html = re.sub(sec4_badge, replace_sec4_badge, html, flags=re.DOTALL)

    # Diffusion Factors
    html = re.sub(
        r'<div style="background: #faf5ff; border-left: 5px solid #8b5cf6; padding: 16px 20px; border-radius: 0 10px 10px 0; margin-bottom: 20px;">\s*<p style="margin: 0; font-size: 15px; color: #3b0764; line-height: 1.6;">(.*?)</div>\s*<h3 style="margin: 0 0 10px 0; color: #0f172a; font-size: 17px;">Factors Affecting Diffusion Rate:</h3>\s*<ul style="margin: 0 0 20px 0; padding-left: 20px; font-size: 14px; color: #334155; line-height: 1.7;">(.*?)</ul>',
        """<div id="sec-diff-factors" class="lecture-interactive-card" data-lecture-section="sec_diff_factors" style="background: #faf5ff; border: 1.5px solid #ddd6fe; border-left: 5px solid #8b5cf6; padding: 18px 20px; border-radius: 10px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #f5f3ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #ddd6fe; pointer-events: none;">🎧 Nghe mục này</div>
        <p style="margin: 0 0 12px 0; font-size: 15px; color: #3b0764; line-height: 1.6; padding-right: 90px;">\\1</p>
        <h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 16px;">Factors Affecting Diffusion Rate:</h4>
        <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #334155; line-height: 1.7;">\\2</ul>
      </div>""",
        html,
        flags=re.DOTALL
    )

    # Tube Experiment (NH3 vs HCl)
    html = re.sub(
        r'<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; padding: 20px;">\s*<h3 style="margin: 0 0 12px 0; color: #1e293b; font-size: 17px; text-align: center;">\s*🔬 Investigation: Ammonia',
        """<div id="sec-diff-mr" class="lecture-interactive-card" data-lecture-section="sec_diff_mr" style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-left: 5px solid #475569; border-radius: 10px; padding: 20px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #334155; background: #f1f5f9; padding: 2px 6px; border-radius: 8px; border: 1px solid #cbd5e1; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; color: #1e293b; font-size: 17px; text-align: center; padding-right: 80px;">🔬 Investigation: Ammonia""",
        html
    )

    return html


# =====================================================================
# C2 HTML TRANSFORMER
# =====================================================================
def build_c2_html():
    raw_path = "scripts/raw_science_chem_phys/c2_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove Study Resources and replace with standard top banner
    banner_code = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%); padding: 28px 32px; border-radius: 14px; color: #ffffff; margin-bottom: 25px; box-shadow: 0 10px 25px -5px rgba(30,58,138,0.25); cursor: pointer; transition: all 0.2s ease; position: relative;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #93c5fd; margin-bottom: 6px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Chemistry</div>
  <h1 style="margin: 0; font-size: 30px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px; padding-right: 140px;">C2: Atoms, Elements &amp; Compounds</h1>
  <p style="margin: 8px 0 0 0; font-size: 15.5px; color: #e0f2fe; opacity: 0.95; line-height: 1.5;">Atomic Structure, Isotopes, Periodic Table Trends, Ionic &amp; Covalent Bonding, Giant Lattices &amp; Macromolecules</p>
</div>"""
    
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', banner_code + '\n', html, flags=re.DOTALL)

    # 2. Wrap Periodic Table in interactive card
    html = html.replace(
        '<div style="margin-bottom: 60px;">\n<h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 10px; margin-bottom: 20px; display: inline-block; font-size: 26px;">🌐 IGCSE INTERACTIVE PERIODIC TABLE</h2>',
        """<div id="sec-periodic-table" class="lecture-interactive-card" data-lecture-section="sec_periodic_table" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 26px 28px; margin-bottom: 40px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 10px; margin-bottom: 20px; display: inline-block; font-size: 26px; padding-right: 140px;">🌐 IGCSE INTERACTIVE PERIODIC TABLE</h2>"""
    )

    # 3. Section 1 Badge & Sub-cards
    html = html.replace(
        '<h2 style="margin-top: 0; color: #0f172a; border-bottom: 3px solid #fed7aa; padding-bottom: 10px; margin-bottom: 25px; font-size: 24px; font-weight: 700; padding-right: 140px;">⚛️ 1. ATOMIC STRUCTURE &amp; ISOTOPES</h2>',
        '<h2 style="margin-top: 0; color: #0f172a; border-bottom: 3px solid #fed7aa; padding-bottom: 10px; margin-bottom: 25px; font-size: 24px; font-weight: 700; padding-right: 140px;">⚛️ 1. ATOMIC STRUCTURE &amp; ISOTOPES</h2>'
    )
    html = re.sub(
        r'<div id="sec-atomic-structure"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 1"),
        html,
        flags=re.DOTALL
    )

    # Sub-item 1: Subatomic particles
    html = re.sub(
        r'<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 4px 10px rgba\(0,0,0,0.05\); margin-bottom: 40px;">\s*<h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive Atom Model</h3>',
        """<div id="sec-subatomic-particles" class="lecture-interactive-card" data-lecture-section="sec_subatomic_particles" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-left: 5px solid #3b82f6; border-radius: 12px; padding: 30px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 40px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px; padding-right: 70px;">Interactive Atom Model</h3>""",
        html
    )

    # Sub-item 2: Calculating particles
    html = re.sub(
        r'<div style="flex: 1; min-width: 300px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 12px; padding: 25px;">\s*<h3 style="margin: 0 0 15px 0; color: #b45309; font-size: 20px;">🧮 Calculating Particles</h3>',
        """<div id="sec-calculating-particles" class="lecture-interactive-card" data-lecture-section="sec_calculating_particles" style="flex: 1; min-width: 300px; background: #fffbeb; border: 1.5px solid #fde68a; border-left: 5px solid #f59e0b; border-radius: 12px; padding: 25px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #b45309; background: #fef3c7; padding: 2px 6px; border-radius: 8px; border: 1px solid #fde68a; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #b45309; font-size: 20px; padding-right: 80px;">🧮 Calculating Particles</h3>""",
        html
    )

    # Sub-item 3: Isotopes
    html = re.sub(
        r'<div style="flex: 1; min-width: 300px; background: #fdf4ff; border: 1px solid #fbcfe8; border-radius: 12px; padding: 25px;">\s*<h3 style="margin: 0 0 15px 0; color: #be185d; font-size: 20px;">⚖️ Isotopes</h3>',
        """<div id="sec-isotopes" class="lecture-interactive-card" data-lecture-section="sec_isotopes" style="flex: 1; min-width: 300px; background: #fdf4ff; border: 1.5px solid #fbcfe8; border-left: 5px solid #db2777; border-radius: 12px; padding: 25px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #be185d; background: #fff1f2; padding: 2px 6px; border-radius: 8px; border: 1px solid #fbcfe8; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #be185d; font-size: 20px; padding-right: 80px;">⚖️ Isotopes</h3>""",
        html
    )

    # 4. Section 2 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-elements-compounds"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 2"),
        html,
        flags=re.DOTALL
    )

    # Elements, compounds, mixtures cards container
    html = re.sub(
        r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(280px, 1fr\)\); gap: 20px; margin-bottom: 40px;">',
        """<div id="sec-elem-comp-mix" class="lecture-interactive-card" data-lecture-section="sec_elem_comp_mix" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-left: 5px solid #3b82f6; border-radius: 12px; padding: 20px; margin-bottom: 40px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #eff6ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 15px;">""",
        html
    )
    # close the extra div for sec-elem-comp-mix before Types of Bonding
    html = re.sub(
        r'(\s*</div>\s*)(<h3 style="color: #0f172a; font-size: 22px; margin-bottom: 20px;">⚖️ Types of Bonding: Ionic vs Covalent</h3>)',
        r'\1</div>\n\2',
        html
    )

    # Ionic Bonding in Table
    html = re.sub(
        r'<div style="padding: 15px 15px 15px 25px; color: #1d4ed8; font-weight: bold;">⚡ Ionic Bonding</div>',
        """<div id="sec-ionic-bonding" class="lecture-interactive-card" data-lecture-section="sec_ionic_bonding" style="padding: 15px 15px 15px 25px; color: #1d4ed8; font-weight: bold; cursor: pointer; position: relative; border-radius: 6px;">⚡ Ionic Bonding <span style="font-size: 11px; background: #dbeafe; padding: 2px 6px; border-radius: 6px; margin-left: 6px;">🎧</span></div>""",
        html
    )

    # Covalent Bonding in Table
    html = re.sub(
        r'<div style="padding: 15px 15px 15px 25px; color: #b45309; font-weight: bold;">🤝 Covalent Bonding</div>',
        """<div id="sec-covalent-bonding" class="lecture-interactive-card" data-lecture-section="sec_covalent_bonding" style="padding: 15px 15px 15px 25px; color: #b45309; font-weight: bold; cursor: pointer; position: relative; border-radius: 6px;">🤝 Covalent Bonding <span style="font-size: 11px; background: #fef3c7; padding: 2px 6px; border-radius: 6px; margin-left: 6px;">🎧</span></div>""",
        html
    )

    # 5. Section 3 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-lattices-macromolecules"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 3"),
        html,
        flags=re.DOTALL
    )

    # Metallic Bonding
    html = re.sub(
        r'<div style="flex: 1; min-width: 320px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 25px;">\s*<h3 style="margin: 0 0 15px 0; color: #334155; font-size: 20px;">🛡️ Metallic Bonding</h3>',
        """<div id="sec-metallic-bonding" class="lecture-interactive-card" data-lecture-section="sec_metallic_bonding" style="flex: 1; min-width: 320px; background: #f8fafc; border: 1.5px solid #fed7aa; border-left: 5px solid #f97316; border-radius: 12px; padding: 25px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #c2410c; background: #fff7ed; padding: 2px 6px; border-radius: 8px; border: 1px solid #fed7aa; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #334155; font-size: 20px; padding-right: 80px;">🛡️ Metallic Bonding</h3>""",
        html
    )

    # Giant Covalent
    html = re.sub(
        r'<div style="flex: 1; min-width: 320px;">\s*<h3 style="margin: 0 0 15px 0; color: #0f172a; font-size: 20px;">🧊 Giant Covalent Structures</h3>',
        """<div id="sec-giant-covalent" class="lecture-interactive-card" data-lecture-section="sec_giant_covalent" style="flex: 1; min-width: 320px; background: #ffffff; border: 1.5px solid #cbd5e1; border-left: 5px solid #0284c7; border-radius: 12px; padding: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #0284c7; background: #f0f9ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #0f172a; font-size: 20px; padding-right: 80px;">🧊 Giant Covalent Structures</h3>""",
        html
    )

    return html


# =====================================================================
# C3 HTML TRANSFORMER
# =====================================================================
def build_c3_html():
    raw_path = "scripts/raw_science_chem_phys/c3_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove Study Resources and add top banner
    banner_code = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%); padding: 28px 32px; border-radius: 14px; color: #ffffff; margin-bottom: 25px; box-shadow: 0 10px 25px -5px rgba(30,58,138,0.25); cursor: pointer; transition: all 0.2s ease; position: relative;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #93c5fd; margin-bottom: 6px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Chemistry</div>
  <h1 style="margin: 0; font-size: 30px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px; padding-right: 140px;">C3: Stoichiometry</h1>
  <p style="margin: 8px 0 0 0; font-size: 15.5px; color: #e0f2fe; opacity: 0.95; line-height: 1.5;">Formulas, State Symbols, Mole Concept, Gas Volumes, Solution Concentrations, Empirical Formulas &amp; Yield</p>
</div>"""

    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', banner_code + '\n', html, flags=re.DOTALL)

    # 2. Section 1 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-formulas-equations"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 1"),
        html,
        flags=re.DOTALL
    )

    # Atomic mass card
    html = re.sub(
        r'<div style="flex: 1; min-width: 300px; background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; color: #6b21a8; font-size: 20px;">📌 Atomic &amp; Molecular Masses</h3>',
        """<div id="sec-atomic-mass" class="lecture-interactive-card" data-lecture-section="sec_atomic_mass" style="flex: 1; min-width: 300px; background: #ffffff; border: 1.5px solid #ddd6fe; border-left: 5px solid #8b5cf6; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #f5f3ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #ddd6fe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #6b21a8; font-size: 20px; padding-right: 80px;">📌 Atomic &amp; Molecular Masses</h3>""",
        html
    )

    # State symbols card
    html = re.sub(
        r'<div style="flex: 1; min-width: 300px; background: #fdf4ff; border: 1px solid #fbcfe8; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; color: #be185d; font-size: 20px;">📌 State Symbols</h3>',
        """<div id="sec-state-symbols" class="lecture-interactive-card" data-lecture-section="sec_state_symbols" style="flex: 1; min-width: 300px; background: #fdf4ff; border: 1.5px solid #fbcfe8; border-left: 5px solid #db2777; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #be185d; background: #fff1f2; padding: 2px 6px; border-radius: 8px; border: 1px solid #fbcfe8; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #be185d; font-size: 20px; padding-right: 80px;">📌 State Symbols</h3>""",
        html
    )

    # 3. Section 2 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-mole-concept"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 2"),
        html,
        flags=re.DOTALL
    )

    # Mole-Mass
    html = re.sub(
        r'<div style="background: #eff6ff; border: 2px solid #93c5fd; border-radius: 12px; padding: 15px; text-align: center;">\s*<h4 style="margin: 0 0 10px 0; color: #1d4ed8; font-size: 16px;">Molar Mass</h4>',
        """<div id="sec-mole-mass" class="lecture-interactive-card" data-lecture-section="sec_mole_mass" style="background: #eff6ff; border: 1.5px solid #93c5fd; border-radius: 12px; padding: 15px; text-align: center; position: relative; cursor: pointer;">
        <div style="position: absolute; top: 8px; right: 8px; font-size: 10px; font-weight: 600; color: #1d4ed8; background: #dbeafe; padding: 2px 5px; border-radius: 6px; border: 1px solid #93c5fd; pointer-events: none;">🎧 Nghe</div>
        <h4 style="margin: 0 0 10px 0; color: #1d4ed8; font-size: 16px;">Molar Mass</h4>""",
        html
    )

    # Mole-Gas
    html = re.sub(
        r'<div style="background: #ecfdf5; border: 2px solid #6ee7b7; border-radius: 12px; padding: 15px; text-align: center;">\s*<h4 style="margin: 0 0 10px 0; color: #047857; font-size: 16px;">Gas Volume \(rtp\)</h4>',
        """<div id="sec-mole-gas" class="lecture-interactive-card" data-lecture-section="sec_mole_gas" style="background: #ecfdf5; border: 1.5px solid #6ee7b7; border-radius: 12px; padding: 15px; text-align: center; position: relative; cursor: pointer;">
        <div style="position: absolute; top: 8px; right: 8px; font-size: 10px; font-weight: 600; color: #047857; background: #d1fae5; padding: 2px 5px; border-radius: 6px; border: 1px solid #6ee7b7; pointer-events: none;">🎧 Nghe</div>
        <h4 style="margin: 0 0 10px 0; color: #047857; font-size: 16px;">Gas Volume (rtp)</h4>""",
        html
    )

    # Mole-Conc
    html = re.sub(
        r'<div style="background: #fef2f2; border: 2px solid #fca5a5; border-radius: 12px; padding: 15px; text-align: center;">\s*<h4 style="margin: 0 0 10px 0; color: #b91c1c; font-size: 16px;">Concentration</h4>',
        """<div id="sec-mole-conc" class="lecture-interactive-card" data-lecture-section="sec_mole_conc" style="background: #fef2f2; border: 1.5px solid #fca5a5; border-radius: 12px; padding: 15px; text-align: center; position: relative; cursor: pointer;">
        <div style="position: absolute; top: 8px; right: 8px; font-size: 10px; font-weight: 600; color: #b91c1c; background: #fee2e2; padding: 2px 5px; border-radius: 6px; border: 1px solid #fca5a5; pointer-events: none;">🎧 Nghe</div>
        <h4 style="margin: 0 0 10px 0; color: #b91c1c; font-size: 16px;">Concentration</h4>""",
        html
    )

    # 4. Section 3 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-empirical-yield"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 3"),
        html,
        flags=re.DOTALL
    )

    # Empirical Formula
    html = re.sub(
        r'<div style="flex: 1; min-width: 320px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; color: #047857; font-size: 20px;">Empirical Formula</h3>',
        """<div id="sec-empirical-formula" class="lecture-interactive-card" data-lecture-section="sec_empirical_formula" style="flex: 1; min-width: 320px; background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 5px solid #059669; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #047857; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #047857; font-size: 20px; padding-right: 80px;">Empirical Formula</h3>""",
        html
    )

    # Yield and Purity column
    html = re.sub(
        r'<div style="flex: 1; min-width: 320px; display: flex; flex-direction: column; gap: 20px;">',
        """<div id="sec-yield-purity" class="lecture-interactive-card" data-lecture-section="sec_yield_purity" style="flex: 1; min-width: 320px; display: flex; flex-direction: column; gap: 20px; background: #ffffff; border: 1.5px solid #fbcfe8; border-left: 5px solid #db2777; border-radius: 12px; padding: 15px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #be185d; background: #fff1f2; padding: 2px 6px; border-radius: 8px; border: 1px solid #fbcfe8; pointer-events: none; z-index: 10;">🎧 Nghe mục này</div>""",
        html
    )

    return html


# =====================================================================
# C4 HTML TRANSFORMER
# =====================================================================
def build_c4_html():
    raw_path = "scripts/raw_science_chem_phys/c4_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove Study Resources and add top banner
    banner_code = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%); padding: 28px 32px; border-radius: 14px; color: #ffffff; margin-bottom: 25px; box-shadow: 0 10px 25px -5px rgba(30,58,138,0.25); cursor: pointer; transition: all 0.2s ease; position: relative;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
  <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #93c5fd; margin-bottom: 6px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Chemistry</div>
  <h1 style="margin: 0; font-size: 30px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px; padding-right: 140px;">C4: Electrochemistry</h1>
  <p style="margin: 8px 0 0 0; font-size: 15.5px; color: #e0f2fe; opacity: 0.95; line-height: 1.5;">Electrolysis Fundamentals, Molten vs Aqueous Electrolysis, Discharge Rules, Electroplating &amp; Fuel Cells</p>
</div>"""

    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', banner_code + '\n', html, flags=re.DOTALL)

    # 2. Section 1 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-electrolysis-basics"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 1"),
        html,
        flags=re.DOTALL
    )

    # Cell components card
    html = re.sub(
        r'<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba\(0,0,0,0.05\); margin-bottom: 40px;">\s*<h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive Electrolysis Cell</h3>',
        """<div id="sec-cell-components" class="lecture-interactive-card" data-lecture-section="sec_cell_components" style="background: #ffffff; border: 1.5px solid #ddd6fe; border-left: 5px solid #8b5cf6; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #f5f3ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #ddd6fe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px; padding-right: 80px;">Interactive Electrolysis Cell</h3>""",
        html
    )

    # OIL RIG card
    html = re.sub(
        r'<div style="background: #fefce8; border: 2px solid #fef08a; border-radius: 12px; padding: 20px; text-align: center;">\s*<h4 style="margin: 0 0 5px 0; color: #a16207; font-size: 18px;">🧠 Mẹo nhớ IGCSE: OIL RIG</h4>',
        """<div id="sec-oil-rig" class="lecture-interactive-card" data-lecture-section="sec_oil_rig" style="background: #fefce8; border: 1.5px solid #fef08a; border-left: 5px solid #f59e0b; border-radius: 12px; padding: 20px; text-align: center; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #a16207; background: #fffbeb; padding: 2px 6px; border-radius: 8px; border: 1px solid #fef08a; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 5px 0; color: #a16207; font-size: 18px; padding-right: 70px;">🧠 Mẹo nhớ IGCSE: OIL RIG</h4>""",
        html
    )

    # 3. Section 2 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-molten-aqueous"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 2"),
        html,
        flags=re.DOTALL
    )

    # Molten vs aqueous table card
    html = re.sub(
        r'<div style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\); margin-bottom: 40px;">',
        """<div id="sec-molten-lead-bromide" class="lecture-interactive-card" data-lecture-section="sec_molten_lead_bromide" style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1.5px solid #fed7aa; border-left: 5px solid #f97316; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 40px; padding: 15px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #c2410c; background: #fff7ed; padding: 2px 6px; border-radius: 8px; border: 1px solid #fed7aa; pointer-events: none; z-index: 10;">🎧 Nghe mục này</div>""",
        html
    )

    # Aqueous discharge card
    html = re.sub(
        r'<h3 style="color: #0f172a; font-size: 20px; margin-bottom: 15px;">📜 Discharge Rules for Aqueous Solutions</h3>\s*<div style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 30px;">',
        """<div id="sec-aqueous-discharge" class="lecture-interactive-card" data-lecture-section="sec_aqueous_discharge" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-left: 5px solid #0284c7; border-radius: 12px; padding: 24px; margin-bottom: 30px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 16px; right: 16px; font-size: 11px; font-weight: 600; color: #0284c7; background: #f0f9ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="color: #0f172a; font-size: 20px; margin: 0 0 15px 0; padding-right: 90px;">📜 Discharge Rules for Aqueous Solutions</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 20px;">""",
        html
    )
    # close the extra wrapper div before Section 3
    html = re.sub(
        r'(\s*</div>\s*</div>\s*)(<div id="sec-electroplating-cells")',
        r'\1</div>\n\2',
        html
    )

    # 4. Section 3 Badge & Sub-cards
    html = re.sub(
        r'<div id="sec-electroplating-cells"[^>]*>.*?<div style="position: absolute; top: 16px; right: 16px;[^>]*><span[^>]*>🎧</span> Nghe phần này</div>',
        lambda m: m.group(0).replace("Nghe phần này", "Nghe toàn bộ mục 3"),
        html,
        flags=re.DOTALL
    )

    # Electroplating card
    html = re.sub(
        r'<div style="flex: 1; min-width: 320px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; color: #db2777; font-size: 20px;">🛡️ Electroplating</h3>',
        """<div id="sec-electroplating" class="lecture-interactive-card" data-lecture-section="sec_electroplating" style="flex: 1; min-width: 320px; background: #ffffff; border: 1.5px solid #fbcfe8; border-left: 5px solid #db2777; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #db2777; background: #fdf2f8; padding: 2px 6px; border-radius: 8px; border: 1px solid #fbcfe8; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #db2777; font-size: 20px; padding-right: 80px;">🛡️ Electroplating</h3>""",
        html
    )

    # Fuel Cells card
    html = re.sub(
        r'<div style="flex: 1; min-width: 320px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; color: #059669; font-size: 20px;">💧 Hydrogen-Oxygen Fuel Cell</h3>',
        """<div id="sec-fuel-cells" class="lecture-interactive-card" data-lecture-section="sec_fuel_cells" style="flex: 1; min-width: 320px; background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 5px solid #059669; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #059669; font-size: 20px; padding-right: 80px;">💧 Hydrogen-Oxygen Fuel Cell</h3>""",
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
    print("Testing C1-C4 HTML Transformations & Div Balance...")
    c1 = build_c1_html()
    verify_div_balance("C1", c1)
    with open("scripts/raw_science_chem_phys/c1_p1_transformed.html", "w", encoding="utf-8") as f:
        f.write(c1)

    c2 = build_c2_html()
    verify_div_balance("C2", c2)
    with open("scripts/raw_science_chem_phys/c2_p1_transformed.html", "w", encoding="utf-8") as f:
        f.write(c2)

    c3 = build_c3_html()
    verify_div_balance("C3", c3)
    with open("scripts/raw_science_chem_phys/c3_p1_transformed.html", "w", encoding="utf-8") as f:
        f.write(c3)

    c4 = build_c4_html()
    verify_div_balance("C4", c4)
    with open("scripts/raw_science_chem_phys/c4_p1_transformed.html", "w", encoding="utf-8") as f:
        f.write(c4)

    print("🎉 ALL C1-C4 HTML TRANSFORMED AND PASSED DIV BALANCE VERIFICATION!")
