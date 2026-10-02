import os
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# =====================================================================
# B11 HTML TRANSFORMER
# =====================================================================
def build_b11_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b11_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #0284c7 0%, #0369a1 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1 -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(2,132,199,0.15); border: 1.5px solid #0369a1; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #38bdf8; color: #082f49; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B11 • Respiratory Biology</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Gas Exchange in Humans</h1>
    <p style="margin: 0; color: #e0f2fe; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Alveolar Adaptations, Respiratory Anatomy & Ventilation Mechanics</p>
  </div>

  <!-- SECTION 1 -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-gas-exchange-surfaces"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Wrap the 5 Adaptations Grid into interactive sub-card
    html = re.sub(
        r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(260px, 1fr\)\); gap: 14px; margin-bottom: 24px;">',
        """<div id="sec-gas-adaptations" class="lecture-interactive-card" data-lecture-section="sec_gas_adaptations" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 6px solid #10b981; border-radius: 12px; padding: 20px; margin-bottom: 24px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 12px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; color: #047857; font-size: 17px; padding-right: 90px;">🫁 Five Essential Features of Gas Exchange Surfaces</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px;">""",
        html
    )
    # Close the added outer wrapper for gas-adaptations
    html = re.sub(
        r'(<h4 style="margin: 0 0 6px 0; color: #0284c7; font-size: 15px;">5\. Moist Internal Lining</h4>\s*<p[^>]*>.*?</p>\s*</div>\s*</div>)(\s*</div>\s*<!-- SECTION 2 -->)',
        r'\1</div>\2',
        html,
        flags=re.DOTALL
    )

    # Enhance Section 2 Header badge
    html = re.sub(
        r'(<div id="sec-respiratory-system"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-cards in Section 2:
    # 1. Trachea & Cartilage
    html = re.sub(
        r'<div id="resp-panel"[^>]*>',
        """<div id="sec-resp-trachea-cartilage" class="lecture-interactive-card" data-lecture-section="sec_resp_trachea_cartilage" style="flex: 1.5; min-width: 320px; background: #fdf4ff; border-left: 6px solid #0ea5e9; border-radius: 8px; padding: 30px; min-height: 250px; display: flex; flex-direction: column; justify-content: center; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); cursor: pointer; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #0284c7; background: #e0f2fe; padding: 2px 8px; border-radius: 12px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>""",
        html
    )

    # 2. Defense of the Airways: Goblet Cells & Cilia
    html = re.sub(
        r'<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-top: 25px;">\s*<h3 style="margin: 0 0 12px 0; color: #0f172a; font-size: 16px;">🛡️ Defense of the Airways: Goblet Cells &amp; Ciliated Cells</h3>',
        """<div id="sec-resp-goblet-cilia" class="lecture-interactive-card" data-lecture-section="sec_resp_goblet_cilia" style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-left: 6px solid #64748b; border-radius: 10px; padding: 20px; margin-top: 25px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 14px; right: 14px; font-size: 11px; font-weight: 600; color: #475569; background: #f1f5f9; padding: 2px 8px; border-radius: 12px; border: 1px solid #cbd5e1; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; color: #0f172a; font-size: 17px; padding-right: 90px;">🛡️ Defense of the Airways: Goblet Cells &amp; Ciliated Cells</h3>""",
        html
    )

    # Enhance Section 3 Header badge
    html = re.sub(
        r'(<div id="sec-ventilation-mechanics"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-cards in Section 3:
    # 1. Inhalation & Exhalation Mechanics
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-bottom: 25px; box-shadow: 0 2px 4px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; font-size: 17px; color: #0f172a;">⚖️ Cơ chế Hít vào &amp; Thở ra</h3>',
        """<div id="sec-inhalation-exhalation" class="lecture-interactive-card" data-lecture-section="sec_inhalation_exhalation" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-left: 6px solid #2563eb; border-radius: 10px; padding: 20px; margin-bottom: 25px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 14px; right: 14px; font-size: 11px; font-weight: 600; color: #2563eb; background: #eff6ff; padding: 2px 8px; border-radius: 12px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; font-size: 17px; color: #1e40af; padding-right: 90px;">⚖️ Mechanics of Breathing: Inhalation & Exhalation</h3>""",
        html
    )

    # 2. Composition of Inspired vs Expired Air & Exercise
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba\(0,0,0,0.02\);">\s*<h3 style="margin: 0 0 15px 0; font-size: 17px; color: #0f172a;">📊 Composition of Inspired vs Expired Air</h3>',
        """<div id="sec-inspired-expired" class="lecture-interactive-card" data-lecture-section="sec_inspired_expired" style="background: #ffffff; border: 1.5px solid #fed7aa; border-left: 6px solid #f59e0b; border-radius: 10px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 14px; right: 14px; font-size: 11px; font-weight: 600; color: #d97706; background: #fffbeb; padding: 2px 8px; border-radius: 12px; border: 1px solid #fed7aa; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; font-size: 17px; color: #b45309; padding-right: 90px;">📊 Composition of Inspired vs Expired Air & Exercise</h3>""",
        html
    )

    return html

# =====================================================================
# B12 HTML TRANSFORMER
# =====================================================================
def build_b12_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b12_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #10b981 0%, #047857 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1 -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #10b981 0%, #047857 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(16,185,129,0.15); border: 1.5px solid #047857; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #34d399; color: #064e3b; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B12 • Cellular Bioenergetics</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Respiration & Bioenergetics</h1>
    <p style="margin: 0; color: #d1fae5; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Aerobic & Anaerobic Respiration, Yeast Fermentation, and Oxygen Debt</p>
  </div>

  <!-- SECTION 1 -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-bioenergetics"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Wrap the 7 Vital Uses into sub-card
    html = re.sub(
        r'<h3 style="color: #047857; font-size: 16px; margin: 20px 0 12px 0;">🔋 Seven Vital Uses of Released Energy in Humans:</h3>\s*<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(200px, 1fr\)\); gap: 12px;">',
        """<div id="sec-respiration-def" class="lecture-interactive-card" data-lecture-section="sec_respiration_def" style="background: #f0fdf4; border: 1.5px solid #86efac; border-left: 6px solid #16a34a; border-radius: 12px; padding: 20px; margin-top: 20px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #16a34a; background: #dcfce7; padding: 2px 8px; border-radius: 12px; border: 1px solid #86efac; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="color: #047857; font-size: 17px; margin: 0 0 12px 0; padding-right: 90px;">🔋 Seven Vital Uses of Released Energy in Humans</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">""",
        html
    )
    # Close the added outer wrapper
    html = re.sub(
        r'(<b style="color: #047857; font-size: 14px;">7\. Constant Body Temp:</b>\s*<p[^>]*>.*?</p>\s*</div>\s*</div>)(\s*</div>\s*<!-- SECTION 2 -->)',
        r'\1</div>\2',
        html,
        flags=re.DOTALL
    )

    # Enhance Section 2 Header badge
    html = re.sub(
        r'(<div id="sec-aerobic-respiration"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Enhance Section 3 Header badge
    html = re.sub(
        r'(<div id="sec-anaerobic-respiration"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-cards in Section 3:
    # 1. In Muscles
    html = re.sub(
        r'<div style="background: #fff1f2; border: 1px solid #fecdd3; border-left: 4px solid #e11d48; padding: 18px; border-radius: 8px;">\s*<h3 style="margin: 0 0 10px 0; color: #9f1239; font-size: 16px;">A\. In Human Muscle Cells \(During Vigorous Exercise\)</h3>',
        """<div id="sec-anaerobic-muscles" class="lecture-interactive-card" data-lecture-section="sec_anaerobic_muscles" style="background: #fff1f2; border: 1.5px solid #fecdd3; border-left: 6px solid #e11d48; padding: 18px; border-radius: 10px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #e11d48; background: #ffe4e6; padding: 2px 8px; border-radius: 12px; border: 1px solid #fecdd3; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 10px 0; color: #9f1239; font-size: 16px; padding-right: 90px;">A. In Human Muscle Cells (During Vigorous Exercise)</h3>""",
        html
    )

    # 2. In Yeast (Fermentation)
    html = re.sub(
        r'<div style="background: #fefce8; border: 1px solid #fef08a; border-left: 4px solid #ca8a04; padding: 18px; border-radius: 8px;">\s*<h3 style="margin: 0 0 10px 0; color: #854d0e; font-size: 16px;">B\. In Yeast \(Fermentation\)</h3>',
        """<div id="sec-anaerobic-yeast" class="lecture-interactive-card" data-lecture-section="sec_anaerobic_yeast" style="background: #fefce8; border: 1.5px solid #fef08a; border-left: 6px solid #ca8a04; padding: 18px; border-radius: 10px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #a16207; background: #fef9c3; padding: 2px 8px; border-radius: 12px; border: 1px solid #fef08a; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 10px 0; color: #854d0e; font-size: 16px; padding-right: 90px;">B. In Yeast (Fermentation)</h3>""",
        html
    )

    # 3. Oxygen Debt
    html = re.sub(
        r'<div style="background: #fff7ed; border: 1px solid #fed7aa; border-left: 4px solid #ea580c; padding: 18px; border-radius: 8px;">\s*<h3 style="margin: 0 0 8px 0; color: #9a3412; font-size: 16px;">🩸 Oxygen Debt \(Repaying the Debt\)</h3>',
        """<div id="sec-oxygen-debt" class="lecture-interactive-card" data-lecture-section="sec_oxygen_debt" style="background: #fff7ed; border: 1.5px solid #fed7aa; border-left: 6px solid #ea580c; padding: 18px; border-radius: 10px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #c2410c; background: #ffedd5; padding: 2px 8px; border-radius: 12px; border: 1px solid #fed7aa; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 8px 0; color: #9a3412; font-size: 16px; padding-right: 90px;">🩸 Oxygen Debt (Repaying the Debt)</h3>""",
        html
    )

    return html

# =====================================================================
# B13 HTML TRANSFORMER
# =====================================================================
def build_b13_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b13_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #7c3aed 0%, #5b21b6 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1 -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #7c3aed 0%, #5b21b6 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(124,58,237,0.15); border: 1.5px solid #5b21b6; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #a78bfa; color: #2e1065; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B13 • Animal Physiology</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Coordination & Response</h1>
    <p style="margin: 0; color: #ede9fe; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Reflex Arc, Endocrine Hormones, and Homeostatic Thermoregulation</p>
  </div>

  <!-- SECTION 1 -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-nervous-reflex"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card: Reflex Arc Panel
    html = re.sub(
        r'<div id="reflex-panel"[^>]*>',
        """<div id="sec-reflex-arc-path" class="lecture-interactive-card" data-lecture-section="sec_reflex_arc_path" style="flex: 1.5; min-width: 320px; background: #fdf4ff; border-left: 6px solid #a855f7; border-radius: 8px; padding: 30px; min-height: 220px; display: flex; flex-direction: column; justify-content: center; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); cursor: pointer; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #7c3aed; background: #f5f3ff; padding: 2px 8px; border-radius: 12px; border: 1px solid #ddd6fe; pointer-events: none;">🎧 Nghe mục này</div>""",
        html
    )

    # Enhance Section 2 Header badge
    html = re.sub(
        r'(<div id="sec-endocrine-system"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card: Glands Panel
    html = re.sub(
        r'<div id="endo-panel"[^>]*>',
        """<div id="sec-endocrine-glands" class="lecture-interactive-card" data-lecture-section="sec_endocrine_glands" style="flex: 1.5; min-width: 320px; background: #fdf4ff; border-left: 6px solid #e11d48; border-radius: 8px; padding: 30px; min-height: 200px; display: flex; flex-direction: column; justify-content: center; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); cursor: pointer; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #be185d; background: #fdf2f8; padding: 2px 8px; border-radius: 12px; border: 1px solid #fbcfe8; pointer-events: none;">🎧 Nghe mục này</div>""",
        html
    )

    # Enhance Section 3 Header badge
    html = re.sub(
        r'(<div id="sec-homeostasis"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card: Skin Thermoregulation Panel
    html = re.sub(
        r'<div id="skin-panel"[^>]*>',
        """<div id="sec-skin-thermo" class="lecture-interactive-card" data-lecture-section="sec_skin_thermo" style="flex: 1.5; min-width: 320px; background: #fdf4ff; border-left: 6px solid #0284c7; border-radius: 8px; padding: 30px; min-height: 220px; display: flex; flex-direction: column; justify-content: center; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); cursor: pointer; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #0284c7; background: #e0f2fe; padding: 2px 8px; border-radius: 12px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>""",
        html
    )

    return html

# =====================================================================
# B14 HTML TRANSFORMER
# =====================================================================
def build_b14_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b14_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #e11d48 0%, #be123c 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1 -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #e11d48 0%, #be123c 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(225,29,72,0.15); border: 1.5px solid #be123c; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #fb7185; color: #881337; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B14 • Pharmacology & Microbiology</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Drugs & Antibiotics</h1>
    <p style="margin: 0; color: #ffe4e6; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Definition of Drugs, Antibiotics vs Viruses, and MRSA Superbug</p>
  </div>

  <!-- SECTION 1 -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-what-is-drug"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Enhance Section 2 Header badge
    html = re.sub(
        r'(<div id="sec-antibiotics"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card: Antibiotics vs Viruses Panel
    html = re.sub(
        r'<div id="anti-panel"[^>]*>',
        """<div id="sec-antibiotics-target" class="lecture-interactive-card" data-lecture-section="sec_antibiotics_target" style="flex: 1.5; min-width: 300px; background: #f8fafc; border-left: 6px solid #64748b; border-radius: 8px; padding: 25px; min-height: 180px; display: flex; flex-direction: column; justify-content: center; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); cursor: pointer; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #475569; background: #f1f5f9; padding: 2px 8px; border-radius: 12px; border: 1px solid #cbd5e1; pointer-events: none;">🎧 Nghe mục này</div>""",
        html
    )

    # Enhance Section 3 Header badge
    html = re.sub(
        r'(<div id="sec-mrsa-crisis"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card: Natural Selection of Resistance
    html = re.sub(
        r'<div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-bottom: 25px;">\s*<h3 style="margin: 0 0 15px 0; font-size: 16px; color: #0f172a;">Step-by-Step Mechanism of Resistance by Natural Selection</h3>',
        """<div id="sec-resistance-selection" class="lecture-interactive-card" data-lecture-section="sec_resistance_selection" style="background: white; border: 1.5px solid #bfdbfe; border-left: 6px solid #2563eb; border-radius: 10px; padding: 20px; margin-bottom: 25px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 14px; right: 14px; font-size: 11px; font-weight: 600; color: #2563eb; background: #eff6ff; padding: 2px 8px; border-radius: 12px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 15px 0; font-size: 17px; color: #1e40af; padding-right: 90px;">Step-by-Step Mechanism of Resistance by Natural Selection</h3>""",
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
    print("=== BUILDING BATCH 3 ENHANCED HTML (B11, B12, B13, B14) ===")
    b11 = build_b11_html()
    verify_and_save('b11', b11)
    
    b12 = build_b12_html()
    verify_and_save('b12', b12)
    
    b13 = build_b13_html()
    verify_and_save('b13', b13)
    
    b14 = build_b14_html()
    verify_and_save('b14', b14)
    print("🎉 BATCH 3 HTML TRANSFORMATION SUCCESSFUL!")
