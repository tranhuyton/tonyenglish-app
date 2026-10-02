import os
import sys
import re
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# =====================================================================
# B3 HTML TRANSFORMER
# =====================================================================
def build_b3_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b3_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #0284c7 0%, #0369a1 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1: DIFFUSION -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(2,132,199,0.15); border: 1.5px solid #0284c7; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #38bdf8; color: #082f49; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B3 • Cell Transport</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Movement Into and Out of Cells</h1>
    <p style="margin: 0; color: #e0f2fe; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Diffusion, Osmosis & Active Transport</p>
  </div>

  <!-- SECTION 1: DIFFUSION -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = html.replace(
        '<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669; padding: 3px 8px; border-radius: 4px; border: 1px solid #a7f3d0;">🎧 Audio Card</span>',
        '<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>'
    )

    # Sub-cards for Section 1 factors:
    # 1. Temperature
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba\(0,0,0,0.02\);"[^>]*>\s*<h4 style="margin: 0 0 6px 0; color: #0369a1; font-size: 15px;">🌡️ Temperature</h4>',
        """<div id="sec-diff-temp" class="lecture-interactive-card" data-lecture-section="sec_diff_temp" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-left: 5px solid #0284c7; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #0284c7; background: #f0f9ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #0369a1; font-size: 15px; padding-right: 80px;">🌡️ Temperature</h4>""",
        html
    )

    # 2. Surface Area
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba\(0,0,0,0.02\);"[^>]*>\s*<h4 style="margin: 0 0 6px 0; color: #0369a1; font-size: 15px;">📐 Surface Area</h4>',
        """<div id="sec-diff-sa" class="lecture-interactive-card" data-lecture-section="sec_diff_sa" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 5px solid #10b981; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #047857; font-size: 15px; padding-right: 80px;">📐 Surface Area</h4>""",
        html
    )

    # 3. Concentration Gradient
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba\(0,0,0,0.02\);"[^>]*>\s*<h4 style="margin: 0 0 6px 0; color: #0369a1; font-size: 15px;">⚡ Concentration Gradient</h4>',
        """<div id="sec-diff-gradient" class="lecture-interactive-card" data-lecture-section="sec_diff_gradient" style="background: #ffffff; border: 1.5px solid #fed7aa; border-left: 5px solid #f59e0b; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #d97706; background: #fffbeb; padding: 2px 6px; border-radius: 8px; border: 1px solid #fed7aa; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #b45309; font-size: 15px; padding-right: 80px;">⚡ Concentration Gradient</h4>""",
        html
    )

    # 4. Diffusion Distance
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba\(0,0,0,0.02\);"[^>]*>\s*<h4 style="margin: 0 0 6px 0; color: #0369a1; font-size: 15px;">📏 Diffusion Distance</h4>',
        """<div id="sec-diff-dist" class="lecture-interactive-card" data-lecture-section="sec_diff_dist" style="background: #ffffff; border: 1.5px solid #ddd6fe; border-left: 5px solid #8b5cf6; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #f5f3ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #ddd6fe; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #6d28d9; font-size: 15px; padding-right: 80px;">📏 Diffusion Distance</h4>""",
        html
    )

    # 5. Biological Importance of Diffusion
    old_imp = r'<div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 10px; padding: 20px; margin-top: 20px; margin-bottom: 25px;">'
    new_imp = """<div id="sec-diff-importance" class="lecture-interactive-card" data-lecture-section="sec_diff_importance" style="background: #f0fdf4; border: 1.5px solid #86efac; border-left: 6px solid #16a34a; border-radius: 10px; padding: 20px; margin-top: 20px; margin-bottom: 25px; cursor: pointer; transition: all 0.2s ease; position: relative;">
      <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #ecfdf5; border: 1px solid #86efac; border-radius: 12px; font-size: 11px; font-weight: 600; color: #059669; pointer-events: none;">🎧 Nghe mục này</div>"""
    html = html.replace(old_imp, new_imp)

    # Section 2: Osmosis Header Badge
    html = re.sub(
        r'(<div id="sec-osmosis"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Section 2 Osmosis Buttons: Pure, Equal, Salt
    html = re.sub(
        r'<button onmouseout="[^"]*pure[^"]*" onmouseover="[^"]*data-os-pure-en[^"]*" style="([^"]*)"',
        r'<button id="sec-os-pure" class="lecture-interactive-card" data-lecture-section="sec_os_pure" onmouseout="this.style.background=\'#e0f2fe\'; this.style.transform=\'translateY(0)\';" onmouseover="document.getElementById(\'os-panel-display-en\').innerHTML = document.getElementById(\'data-os-pure-en\').innerHTML; this.style.background=\'#bae6fd\'; this.style.transform=\'translateY(-2px)\';" style="\1 position: relative;"',
        html
    )

    html = re.sub(
        r'<button onmouseout="[^"]*equal[^"]*" onmouseover="[^"]*data-os-equal-en[^"]*" style="([^"]*)"',
        r'<button id="sec-os-equal" class="lecture-interactive-card" data-lecture-section="sec_os_equal" onmouseout="this.style.background=\'#f1f5f9\'; this.style.transform=\'translateY(0)\';" onmouseover="document.getElementById(\'os-panel-display-en\').innerHTML = document.getElementById(\'data-os-equal-en\').innerHTML; this.style.background=\'#e2e8f0\'; this.style.transform=\'translateY(-2px)\';" style="\1 position: relative;"',
        html
    )

    html = re.sub(
        r'<button onmouseout="[^"]*salt[^"]*" onmouseover="[^"]*data-os-salt-en[^"]*" style="([^"]*)"',
        r'<button id="sec-os-salt" class="lecture-interactive-card" data-lecture-section="sec_os_salt" onmouseout="this.style.background=\'#fee2e2\'; this.style.transform=\'translateY(0)\';" onmouseover="document.getElementById(\'os-panel-display-en\').innerHTML = document.getElementById(\'data-os-salt-en\').innerHTML; this.style.background=\'#fecaca\'; this.style.transform=\'translateY(-2px)\';" style="\1 position: relative;"',
        html
    )

    # Section 3: Active Transport Header Badge
    html = re.sub(
        r'(<div id="sec-active-transport"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-cards in Active Transport:
    # Carrier Proteins mechanism
    html = re.sub(
        r'<div style="background: #fdf4ff; border: 1px solid #f0abfc; border-left: 5px solid #c026d3; border-radius: 8px; padding: 18px; margin-bottom: 20px;">',
        """<div id="sec-active-carrier" class="lecture-interactive-card" data-lecture-section="sec_active_carrier" style="background: #fdf4ff; border: 1.5px solid #f0abfc; border-left: 6px solid #c026d3; border-radius: 10px; padding: 18px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #c026d3; background: #fae8ff; padding: 2px 8px; border-radius: 12px; border: 1px solid #f0abfc; pointer-events: none;">🎧 Nghe mục này</div>""",
        html
    )

    # Biological Importance in Section 3
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin-top: 15px;">\s*<h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 15px;">🌱 Biological Importance of Active Transport</h4>',
        """<div id="sec-active-importance" class="lecture-interactive-card" data-lecture-section="sec_active_importance" style="background: #f0fdf4; border: 1.5px solid #86efac; border-left: 6px solid #16a34a; border-radius: 10px; padding: 18px; margin-top: 15px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 12px; border: 1px solid #86efac; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 8px 0; color: #166534; font-size: 16px; padding-right: 90px;">🌱 Biological Importance of Active Transport</h4>""",
        html
    )

    return html

# =====================================================================
# B4 HTML TRANSFORMER
# =====================================================================
def build_b4_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b4_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #7c2d12 0%, #9a3412 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1: MOLECULAR COMPOSITION -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #7c2d12 0%, #9a3412 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(124,45,18,0.15); border: 1.5px solid #9a3412; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #ea580c; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B4 • Biochemistry</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Biological Molecules</h1>
    <p style="margin: 0; color: #ffedd5; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Carbohydrates, Lipids, Proteins, DNA & Food Tests</p>
  </div>

  <!-- SECTION 1: MOLECULAR COMPOSITION -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-biomolecules"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-cards in Section 1:
    # 1. Carbohydrates
    html = re.sub(
        r'<div style="flex: 1; min-width: 280px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba\(0,0,0,0.05\);">\s*<h3 style="margin-top: 0; color: #1d4ed8; font-size: 22px;">🍞 Carbohydrates</h3>',
        """<div id="sec-carbohydrates" class="lecture-interactive-card" data-lecture-section="sec_carbohydrates" style="flex: 1; min-width: 280px; background: #eff6ff; border: 2px solid #3b82f6; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #dbeafe; padding: 2px 8px; border-radius: 12px; border: 1px solid #93c5fd; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin-top: 0; color: #1d4ed8; font-size: 22px;">🍞 Carbohydrates</h3>""",
        html
    )

    # 2. Fats & Oils (Lipids)
    html = re.sub(
        r'<div style="flex: 1; min-width: 280px; background: #fffbeb; border: 2px solid #fde68a; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba\(0,0,0,0.05\);">\s*<h3 style="margin-top: 0; color: #d97706; font-size: 22px;">🥑 Fats &amp; Oils \(Lipids\)</h3>',
        """<div id="sec-lipids" class="lecture-interactive-card" data-lecture-section="sec_lipids" style="flex: 1; min-width: 280px; background: #fffbeb; border: 2px solid #f59e0b; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #d97706; background: #fef3c7; padding: 2px 8px; border-radius: 12px; border: 1px solid #fde68a; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin-top: 0; color: #d97706; font-size: 22px;">🥑 Fats &amp; Oils (Lipids)</h3>""",
        html
    )

    # 3. Proteins
    html = re.sub(
        r'<div style="flex: 1; min-width: 280px; background: #fdf4ff; border: 2px solid #fbcfe8; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba\(0,0,0,0.05\);">\s*<h3 style="margin-top: 0; color: #be185d; font-size: 22px;">🥩 Proteins</h3>',
        """<div id="sec-proteins" class="lecture-interactive-card" data-lecture-section="sec_proteins" style="flex: 1; min-width: 280px; background: #fdf4ff; border: 2px solid #ec4899; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #be185d; background: #fce7f3; padding: 2px 8px; border-radius: 12px; border: 1px solid #fbcfe8; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin-top: 0; color: #be185d; font-size: 22px;">🥩 Proteins</h3>""",
        html
    )

    # 4. DNA Structure
    html = re.sub(
        r'<div style="flex: 2; min-width: 320px; background: #faf5ff; border: 2px solid #e9d5ff; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; color: #7e22ce; font-size: 22px; display: flex; align-items: center; gap: 10px;">🧬 DNA Structure',
        """<div id="sec-dna" class="lecture-interactive-card" data-lecture-section="sec_dna" style="flex: 2; min-width: 320px; background: #faf5ff; border: 2px solid #8b5cf6; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 16px; right: 16px; font-size: 11px; font-weight: 600; color: #7e22ce; background: #f3e8ff; padding: 2px 8px; border-radius: 12px; border: 1px solid #d8b4fe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #7e22ce; font-size: 22px; display: flex; align-items: center; gap: 10px; padding-right: 90px;">🧬 DNA Structure""",
        html
    )

    # 5. Role of Water
    html = re.sub(
        r'<div style="flex: 1; min-width: 250px; background: #f0f9ff; border: 2px solid #bae6fd; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; color: #0369a1; font-size: 22px; display: flex; align-items: center; gap: 10px;">💧 Role of Water',
        """<div id="sec-water" class="lecture-interactive-card" data-lecture-section="sec_water" style="flex: 1; min-width: 250px; background: #f0f9ff; border: 2px solid #0284c7; border-radius: 12px; padding: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 16px; right: 16px; font-size: 11px; font-weight: 600; color: #0369a1; background: #e0f2fe; padding: 2px 8px; border-radius: 12px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; color: #0369a1; font-size: 22px; display: flex; align-items: center; gap: 10px; padding-right: 90px;">💧 Role of Water""",
        html
    )

    # Section 2: Qualitative Food Tests Header Badge
    html = re.sub(
        r'(<div id="sec-food-tests"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # 5 Food test buttons: Starch, Sugar, Protein, Lipid, VitC
    html = re.sub(
        r'<button onmouseout="[^"]*334155[^"]*" onmouseover="[^"]*test-starch-en[^"]*" style="([^"]*)"[^>]*>🍞 1\. Test for Starch</button>',
        r'<button id="sec-test-starch" class="lecture-interactive-card" data-lecture-section="sec_test_starch" onmouseout="this.style.background=\'#334155\'; this.style.borderColor=\'#475569\';" onmouseover="document.getElementById(\'virtual-lab-display-en\').innerHTML = document.getElementById(\'test-starch-en\').innerHTML; this.style.background=\'#475569\'; this.style.borderColor=\'#f59e0b\';" style="\1 position: relative;">🍞 1. Test for Starch</button>',
        html
    )

    html = re.sub(
        r'<button onmouseout="[^"]*334155[^"]*" onmouseover="[^"]*test-sugar-en[^"]*" style="([^"]*)"[^>]*>🍬 2\. Test for Reducing Sugars</button>',
        r'<button id="sec-test-sugar" class="lecture-interactive-card" data-lecture-section="sec_test_sugar" onmouseout="this.style.background=\'#334155\'; this.style.borderColor=\'#475569\';" onmouseover="document.getElementById(\'virtual-lab-display-en\').innerHTML = document.getElementById(\'test-sugar-en\').innerHTML; this.style.background=\'#475569\'; this.style.borderColor=\'#ef4444\';" style="\1 position: relative;">🍬 2. Test for Reducing Sugars</button>',
        html
    )

    html = re.sub(
        r'<button onmouseout="[^"]*334155[^"]*" onmouseover="[^"]*test-protein-en[^"]*" style="([^"]*)"[^>]*>🥩 3\. Test for Proteins</button>',
        r'<button id="sec-test-protein" class="lecture-interactive-card" data-lecture-section="sec_test_protein" onmouseout="this.style.background=\'#334155\'; this.style.borderColor=\'#475569\';" onmouseover="document.getElementById(\'virtual-lab-display-en\').innerHTML = document.getElementById(\'test-protein-en\').innerHTML; this.style.background=\'#475569\'; this.style.borderColor=\'#a855f7\';" style="\1 position: relative;">🥩 3. Test for Proteins</button>',
        html
    )

    html = re.sub(
        r'<button onmouseout="[^"]*334155[^"]*" onmouseover="[^"]*test-lipid-en[^"]*" style="([^"]*)"[^>]*>🥑 4\. Test for Lipids \(Fats\)</button>',
        r'<button id="sec-test-lipid" class="lecture-interactive-card" data-lecture-section="sec_test_lipid" onmouseout="this.style.background=\'#334155\'; this.style.borderColor=\'#475569\';" onmouseover="document.getElementById(\'virtual-lab-display-en\').innerHTML = document.getElementById(\'test-lipid-en\').innerHTML; this.style.background=\'#475569\'; this.style.borderColor=\'#fcd34d\';" style="\1 position: relative;">🥑 4. Test for Lipids (Fats)</button>',
        html
    )

    html = re.sub(
        r'<button onmouseout="[^"]*334155[^"]*" onmouseover="[^"]*test-vitc-en[^"]*" style="([^"]*)"[^>]*>🍋 5\. Test for Vitamin C</button>',
        r'<button id="sec-test-vitc" class="lecture-interactive-card" data-lecture-section="sec_test_vitc" onmouseout="this.style.background=\'#334155\'; this.style.borderColor=\'#475569\';" onmouseover="document.getElementById(\'virtual-lab-display-en\').innerHTML = document.getElementById(\'test-vitc-en\').innerHTML; this.style.background=\'#475569\'; this.style.borderColor=\'#38bdf8\';" style="\1 position: relative;">🍋 5. Test for Vitamin C</button>',
        html
    )

    return html

# =====================================================================
# B5 HTML TRANSFORMER
# =====================================================================
def build_b5_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b5_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #4c1d95 0%, #6d28d9 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1: DEFINITION -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #4c1d95 0%, #6d28d9 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(76,29,149,0.15); border: 1.5px solid #6d28d9; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #8b5cf6; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B5 • Enzymology</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Enzymes: Biological Catalysts</h1>
    <p style="margin: 0; color: #ddd6fe; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Lock and Key Model, Temperature, pH & Denaturation</p>
  </div>

  <!-- SECTION 1: DEFINITION -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-enzyme-nature"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Add Sub-card for Key Properties of Enzymes in Section 1
    old_sec1_content = r'(<p style="margin: 0; font-size: 16px; font-weight: 700; color: #14532d;">\s*"Enzymes are proteins that are involved in all metabolic reactions, where they function as biological catalysts."\s*</p>\s*</div>)'
    new_sec1_content = r"""\1
    <div id="sec-enzyme-properties" class="lecture-interactive-card" data-lecture-section="sec_enzyme_properties" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-left: 6px solid #2563eb; border-radius: 10px; padding: 18px; margin-top: 15px; cursor: pointer; transition: all 0.2s ease; position: relative;">
      <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #2563eb; background: #eff6ff; padding: 2px 8px; border-radius: 12px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
      <h3 style="margin: 0 0 10px 0; color: #1e40af; font-size: 17px; padding-right: 90px;">⭐ Core Enzyme Properties to Memorise</h3>
      <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #334155; line-height: 1.7;">
        <li><strong>Proteins:</strong> All enzymes are proteins synthesised by ribosomes.</li>
        <li><strong>Biological Catalysts:</strong> Speed up cellular metabolic reactions without being used up.</li>
        <li><strong>Specificity:</strong> Each enzyme has an active site fitting only one specific substrate.</li>
        <li><strong>Reusable:</strong> Enzymes remain completely unchanged at the end of the reaction.</li>
      </ul>
    </div>"""
    html = re.sub(old_sec1_content, new_sec1_content, html, flags=re.DOTALL)

    # Enhance Section 2 Header badge
    html = re.sub(
        r'(<div id="sec-lock-and-key"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Make Section 2 Explorer panel interactive card
    html = re.sub(
        r'<div id="enz-info-panel-en" style="([^"]*)">',
        r'<div id="sec-lock-key-mechanism" class="lecture-interactive-card" data-lecture-section="sec_lock_key_mechanism" style="\1 cursor: pointer; position: relative;"><div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #c026d3; background: #fae8ff; padding: 2px 8px; border-radius: 12px; border: 1px solid #f0abfc; pointer-events: none;">🎧 Nghe mục này</div>',
        html
    )

    # Enhance Section 3 Header badge
    html = re.sub(
        r'(<div id="sec-temp-ph"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Make Temperature Explorer panel interactive card
    html = re.sub(
        r'<div id="temp-info-panel-en" style="([^"]*)">',
        r'<div id="sec-temp-effect" class="lecture-interactive-card" data-lecture-section="sec_temp_effect" style="\1 cursor: pointer; position: relative;"><div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #c026d3; background: #fae8ff; padding: 2px 8px; border-radius: 12px; border: 1px solid #f0abfc; pointer-events: none;">🎧 Nghe mục này</div>',
        html
    )

    # Make pH Table interactive card
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; margin-top: 20px;">\s*<h3 style="margin: 0 0 10px 0; font-size: 16px; color: #0f172a;">🧪 Optimum pH in the Human Body</h3>',
        """<div id="sec-ph-effect" class="lecture-interactive-card" data-lecture-section="sec_ph_effect" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 6px solid #059669; border-radius: 10px; padding: 20px; margin-top: 20px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 14px; right: 14px; font-size: 11px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 12px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 10px 0; font-size: 17px; color: #047857; padding-right: 90px;">🧪 Optimum pH in the Human Body</h3>""",
        html
    )

    return html

# =====================================================================
# B6 HTML TRANSFORMER
# =====================================================================
def build_b6_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b6_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #065f46 0%, #047857 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1: PHOTOSYNTHESIS EQUATIONS & ENERGY -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #065f46 0%, #047857 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(6,95,70,0.15); border: 1.5px solid #047857; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #10b981; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B6 • Plant Biology</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Plant Nutrition & Photosynthesis</h1>
    <p style="margin: 0; color: #a7f3d0; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Autotrophic Synthesis, Leaf Anatomy & Factors</p>
  </div>

  <!-- SECTION 1: PHOTOSYNTHESIS EQUATIONS & ENERGY -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-photosynthesis"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Enhance Section 2 Header badge
    html = re.sub(
        r'(<div id="sec-glucose-minerals"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-cards in Section 2:
    # 1. Carbohydrate Storage & Transport (Fate of Glucose)
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; box-shadow: 0 2px 6px rgba\(0,0,0,0.03\);">\s*<h3 style="margin: 0 0 12px 0; font-size: 16px; color: #15803d;">🍬 Carbohydrate Storage &amp; Transport</h3>',
        """<div id="sec-glucose-uses" class="lecture-interactive-card" data-lecture-section="sec_glucose_uses" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 6px solid #10b981; border-radius: 10px; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 12px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; font-size: 17px; color: #047857; padding-right: 90px;">🍬 Carbohydrate Storage &amp; Transport</h3>""",
        html
    )

    # 2. Essential Mineral Ions
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; box-shadow: 0 2px 6px rgba\(0,0,0,0.03\);">\s*<h3 style="margin: 0 0 12px 0; font-size: 16px; color: #b45309;">🌾 Essential Mineral Ions</h3>',
        """<div id="sec-minerals" class="lecture-interactive-card" data-lecture-section="sec_minerals" style="background: #ffffff; border: 1.5px solid #fed7aa; border-left: 6px solid #f59e0b; border-radius: 10px; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #d97706; background: #fffbeb; padding: 2px 8px; border-radius: 12px; border: 1px solid #fed7aa; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; font-size: 17px; color: #b45309; padding-right: 90px;">🌾 Essential Mineral Ions</h3>""",
        html
    )

    # Enhance Section 3 Header badge
    html = re.sub(
        r'(<div id="sec-leaf-anatomy"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Section 3: Add interactive explorer sub-cards below SVG
    leaf_subcards = """
    <!-- LEAF TISSUE SUB-CARDS -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-top: 25px;">
      <div id="sec-leaf-cuticle" class="lecture-interactive-card" data-lecture-section="sec_leaf_cuticle" style="background: #f0f9ff; border: 1.5px solid #bae6fd; border-left: 5px solid #0284c7; border-radius: 10px; padding: 14px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 10px; font-weight: 600; color: #0284c7; background: #e0f2fe; padding: 2px 6px; border-radius: 8px;">🎧 Nghe</div>
        <h4 style="margin: 0 0 4px 0; color: #0369a1; font-size: 15px;">💧 Cuticle & Epidermis</h4>
        <p style="margin: 0; font-size: 12.5px; color: #475569;">Waterproof waxy layer prevents water loss; transparent epidermis lets light enter.</p>
      </div>

      <div id="sec-leaf-palisade" class="lecture-interactive-card" data-lecture-section="sec_leaf_palisade" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 5px solid #16a34a; border-radius: 10px; padding: 14px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 10px; font-weight: 600; color: #16a34a; background: #dcfce7; padding: 2px 6px; border-radius: 8px;">🎧 Nghe</div>
        <h4 style="margin: 0 0 4px 0; color: #15803d; font-size: 15px;">☀️ Palisade Mesophyll</h4>
        <p style="margin: 0; font-size: 12.5px; color: #475569;">Columnar cells tightly packed with chloroplasts; primary site of photosynthesis.</p>
      </div>

      <div id="sec-leaf-spongy" class="lecture-interactive-card" data-lecture-section="sec_leaf_spongy" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 5px solid #059669; border-radius: 10px; padding: 14px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 10px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 6px; border-radius: 8px;">🎧 Nghe</div>
        <h4 style="margin: 0 0 4px 0; color: #047857; font-size: 15px;">💨 Spongy Mesophyll</h4>
        <p style="margin: 0; font-size: 12.5px; color: #475569;">Loose rounded cells with air spaces for rapid CO₂ and O₂ diffusion.</p>
      </div>

      <div id="sec-leaf-vein" class="lecture-interactive-card" data-lecture-section="sec_leaf_vein" style="background: #fffbeb; border: 1.5px solid #fde68a; border-left: 5px solid #d97706; border-radius: 10px; padding: 14px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 10px; font-weight: 600; color: #d97706; background: #fef3c7; padding: 2px 6px; border-radius: 8px;">🎧 Nghe</div>
        <h4 style="margin: 0 0 4px 0; color: #b45309; font-size: 15px;">🌿 Vascular Bundle</h4>
        <p style="margin: 0; font-size: 12.5px; color: #475569;">Xylem delivers water/minerals; Phloem translocates sucrose and amino acids.</p>
      </div>

      <div id="sec-leaf-stomata" class="lecture-interactive-card" data-lecture-section="sec_leaf_stomata" style="background: #faf5ff; border: 1.5px solid #e9d5ff; border-left: 5px solid #9333ea; border-radius: 10px; padding: 14px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 10px; font-weight: 600; color: #9333ea; background: #f3e8ff; padding: 2px 6px; border-radius: 8px;">🎧 Nghe</div>
        <h4 style="margin: 0 0 4px 0; color: #7e22ce; font-size: 15px;">🚪 Stomata & Guard Cells</h4>
        <p style="margin: 0; font-size: 12.5px; color: #475569;">Pores on lower surface open for gas exchange and close to limit water loss.</p>
      </div>
    </div>
"""
    # Insert leaf_subcards right before `</div>\s*</div>\s*<!-- SECTION 4: FACTORS & GAS EXCHANGE -->`
    html = re.sub(
        r'(</div>\s*<div style="display: none;">\s*<div id="l-cuticle-en">)',
        leaf_subcards + r'\1',
        html
    )

    # Enhance Section 4 Header badge
    html = re.sub(
        r'(<div id="sec-limiting-factors"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 4</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-cards in Section 4:
    # 1. Limiting Factors
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba\(0,0,0,0.02\);">\s*<h4 style="margin: 0 0 8px 0; font-size: 15px; color: #0f172a;">☀️ Limiting Factors</h4>',
        """<div id="sec-limiting-detail" class="lecture-interactive-card" data-lecture-section="sec_limiting_detail" style="background: #ffffff; border: 1.5px solid #fed7aa; border-left: 5px solid #f59e0b; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #d97706; background: #fffbeb; padding: 2px 6px; border-radius: 8px; border: 1px solid #fed7aa; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 8px 0; font-size: 15px; color: #b45309; padding-right: 80px;">☀️ Limiting Factors</h4>""",
        html
    )

    # 2. Hydrogencarbonate Indicator
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba\(0,0,0,0.02\);">\s*<h4 style="margin: 0 0 8px 0; font-size: 15px; color: #0f172a;">🧪 Hydrogencarbonate Indicator</h4>',
        """<div id="sec-hydrogencarbonate" class="lecture-interactive-card" data-lecture-section="sec_hydrogencarbonate" style="background: #ffffff; border: 1.5px solid #ddd6fe; border-left: 5px solid #8b5cf6; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #f5f3ff; padding: 2px 6px; border-radius: 8px; border: 1px solid #ddd6fe; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 8px 0; font-size: 15px; color: #6d28d9; padding-right: 80px;">🧪 Hydrogencarbonate Indicator</h4>""",
        html
    )

    return html

def verify_and_save(code, html):
    opens = len(re.findall(r'<div\b[^>]*>', html, flags=re.IGNORECASE))
    closes = len(re.findall(r'</div>', html, flags=re.IGNORECASE))
    diff = opens - closes
    print(f"[{code.upper()}] Opens: {opens} | Closes: {closes} | Diff: {diff}")
    if diff != 0:
        raise ValueError(f"Div balance failed for {code.upper()} with diff={diff}")
    
    out_path = f"scripts/raw_science_bio_b3_b19/{code}_p1_transformed.html"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"[{code.upper()}] Saved transformed HTML to {out_path} ({len(html)} chars)")

if __name__ == "__main__":
    print("=== BUILDING BATCH 1 ENHANCED HTML (B3, B4, B5, B6) ===")
    b3 = build_b3_html()
    verify_and_save('b3', b3)
    
    b4 = build_b4_html()
    verify_and_save('b4', b4)
    
    b5 = build_b5_html()
    verify_and_save('b5', b5)
    
    b6 = build_b6_html()
    verify_and_save('b6', b6)
    print("🎉 BATCH 1 HTML TRANSFORMATION SUCCESSFUL!")
