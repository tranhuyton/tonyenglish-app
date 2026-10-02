import os
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# =====================================================================
# B7 HTML TRANSFORMER
# =====================================================================
def build_b7_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b7_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #1e3a8a 0%, #1e40af 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1: BALANCED DIET -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(30,58,138,0.15); border: 1.5px solid #1e40af; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #3b82f6; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B7 • Human Biology</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Human Nutrition & Digestive System</h1>
    <p style="margin: 0; color: #bfdbfe; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Diet, Alimentary Canal, Digestion & Enzymes</p>
  </div>

  <!-- SECTION 1: BALANCED DIET -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-balanced-diet"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-cards in Section 1:
    # Nutrients & Deficiencies
    subcards_s1 = """
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin-top: 20px;">
      <div id="sec-diet-nutrients" class="lecture-interactive-card" data-lecture-section="sec_diet_nutrients" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-left: 6px solid #2563eb; border-radius: 10px; padding: 18px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #2563eb; background: #eff6ff; padding: 2px 8px; border-radius: 12px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 10px 0; font-size: 17px; color: #1e40af; padding-right: 90px;">🥗 7 Essential Food Groups</h3>
        <p style="margin: 0; font-size: 13.5px; color: #475569; line-height: 1.6;">Carbohydrates & Fats (energy), Proteins (growth & repair), Vitamins & Minerals, Fibre (peristalsis) & Water (solvent).</p>
      </div>

      <div id="sec-diet-deficiencies" class="lecture-interactive-card" data-lecture-section="sec_diet_deficiencies" style="background: #ffffff; border: 1.5px solid #fecaca; border-left: 6px solid #dc2626; border-radius: 10px; padding: 18px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #dc2626; background: #fef2f2; padding: 2px 8px; border-radius: 12px; border: 1px solid #fecaca; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 10px 0; font-size: 17px; color: #b91c1c; padding-right: 90px;">⚠️ Key Deficiency Diseases</h3>
        <p style="margin: 0; font-size: 13.5px; color: #475569; line-height: 1.6;"><strong>Scurvy:</strong> Lack of Vit C.<br><strong>Rickets:</strong> Lack of Vit D or Calcium.<br><strong>Anaemia:</strong> Lack of Iron (low haemoglobin).<br><strong>Kwashiorkor:</strong> Protein deficiency.</p>
      </div>
    </div>
"""
    # Insert subcards_s1 before `</div>\s*<!-- SECTION 2: 5 STAGES OF FOOD PROCESSING -->`
    html = re.sub(
        r'(</div>\s*<!-- SECTION 2: 5 STAGES OF FOOD PROCESSING -->)',
        subcards_s1 + r'\1',
        html
    )

    # Enhance Section 2 Header badge
    html = re.sub(
        r'(<div id="sec-food-processing"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Enhance Section 3 Header badge
    html = re.sub(
        r'(<div id="sec-digestive-system"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Section 3: Add interactive sub-cards for digestive organs below SVG
    digestive_subcards = """
    <!-- DIGESTIVE ORGANS SUB-CARDS -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-top: 25px;">
      <div id="sec-organ-mouth" class="lecture-interactive-card" data-lecture-section="sec_organ_mouth" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 5px solid #16a34a; border-radius: 10px; padding: 14px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 10px; font-weight: 600; color: #16a34a; background: #dcfce7; padding: 2px 6px; border-radius: 8px;">🎧 Nghe</div>
        <h4 style="margin: 0 0 4px 0; color: #15803d; font-size: 15px;">👄 Mouth & Oesophagus</h4>
        <p style="margin: 0; font-size: 12.5px; color: #475569;">Mechanical chewing + Salivary amylase; peristalsis pushes bolus down.</p>
      </div>

      <div id="sec-organ-stomach" class="lecture-interactive-card" data-lecture-section="sec_organ_stomach" style="background: #fffbeb; border: 1.5px solid #fde68a; border-left: 5px solid #d97706; border-radius: 10px; padding: 14px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 10px; font-weight: 600; color: #d97706; background: #fef3c7; padding: 2px 6px; border-radius: 8px;">🎧 Nghe</div>
        <h4 style="margin: 0 0 4px 0; color: #b45309; font-size: 15px;">🍲 Stomach</h4>
        <p style="margin: 0; font-size: 12.5px; color: #475569;">Churning + Pepsin protease + Hydrochloric acid (pH 2 kills bacteria).</p>
      </div>

      <div id="sec-organ-liver-pancreas" class="lecture-interactive-card" data-lecture-section="sec_organ_liver_pancreas" style="background: #fdf4ff; border: 1.5px solid #fbcfe8; border-left: 5px solid #db2777; border-radius: 10px; padding: 14px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 10px; font-weight: 600; color: #db2777; background: #fdf2f8; padding: 2px 6px; border-radius: 8px;">🎧 Nghe</div>
        <h4 style="margin: 0 0 4px 0; color: #be185d; font-size: 15px;">🥑 Liver, Bile & Pancreas</h4>
        <p style="margin: 0; font-size: 12.5px; color: #475569;">Liver makes bile; Pancreas secretes amylase, trypsin, lipase into duodenum.</p>
      </div>

      <div id="sec-organ-intestines" class="lecture-interactive-card" data-lecture-section="sec_organ_intestines" style="background: #eff6ff; border: 1.5px solid #bfdbfe; border-left: 5px solid #2563eb; border-radius: 10px; padding: 14px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 10px; font-weight: 600; color: #2563eb; background: #dbeafe; padding: 2px 6px; border-radius: 8px;">🎧 Nghe</div>
        <h4 style="margin: 0 0 4px 0; color: #1e40af; font-size: 15px;">🌾 Small & Large Intestine</h4>
        <p style="margin: 0; font-size: 12.5px; color: #475569;">Villi absorb nutrients in ileum; colon reabsorbs water; rectum stores faeces.</p>
      </div>
    </div>
"""
    # Insert digestive_subcards before `</div>\s*<!-- SECTION 4: CHEMICAL DIGESTION -->`
    html = re.sub(
        r'(</div>\s*<div style="display: none;">\s*<div id="d-mouth-en">)',
        digestive_subcards + r'\1',
        html
    )

    # Enhance Section 4 Header badge
    html = re.sub(
        r'(<div id="sec-chemical-digestion"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>🎧 Audio Card</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 4</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-cards in Section 4:
    # 1. Enzyme Actions (Table)
    html = re.sub(
        r'<div style="overflow-x: auto; margin-bottom: 25px;">\s*<table style="width: 100%; border-collapse: collapse;',
        """<div id="sec-enzymes-action" class="lecture-interactive-card" data-lecture-section="sec_enzymes_action" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-left: 6px solid #2563eb; border-radius: 10px; padding: 18px; margin-bottom: 25px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #2563eb; background: #eff6ff; padding: 2px 8px; border-radius: 12px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; font-size: 17px; color: #1e40af; padding-right: 90px;">🧪 Complete Summary of Digestive Enzymes</h3>
        <div style="overflow-x: auto; margin-bottom: 10px;">
        <table style="width: 100%; border-collapse: collapse;""",
        html
    )
    # Close the added outer div for enzymes-action
    html = re.sub(
        r'(</table>\s*</div>)(\s*<div style="background: #fefce8; border: 1px solid #fef08a;)',
        r'\1</div>\2',
        html
    )

    # 2. Bile Role
    html = re.sub(
        r'<div style="background: #fefce8; border: 1px solid #fef08a; border-left: 5px solid #eab308; border-radius: 8px; padding: 18px; margin-bottom: 20px;">\s*<h4 style="margin: 0 0 8px 0; color: #a16207; font-size: 16px;">🥑 Essential Roles of Bile',
        """<div id="sec-bile-role" class="lecture-interactive-card" data-lecture-section="sec_bile_role" style="background: #fefce8; border: 1.5px solid #fef08a; border-left: 6px solid #eab308; border-radius: 10px; padding: 18px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #a16207; background: #fef9c3; padding: 2px 8px; border-radius: 12px; border: 1px solid #fef08a; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 8px 0; color: #a16207; font-size: 16px; padding-right: 90px;">🥑 Essential Roles of Bile""",
        html
    )

    # 3. Villi Absorption Adaptations
    html = re.sub(
        r'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px;">\s*<h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 15px;">🔬 Structural Adaptations of the Small Intestine for Absorption',
        """<div id="sec-villi-absorption" class="lecture-interactive-card" data-lecture-section="sec_villi_absorption" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 6px solid #10b981; border-radius: 10px; padding: 18px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 12px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 8px 0; color: #047857; font-size: 16px; padding-right: 90px;">🔬 Structural Adaptations of the Small Intestine for Absorption""",
        html
    )

    return html

# =====================================================================
# B8 HTML TRANSFORMER
# =====================================================================
def build_b8_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b8_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Add Top Banner intro card
    top_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(2,132,199,0.15); border: 1.5px solid #0369a1; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #38bdf8; color: #082f49; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B8 • Plant Transport</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Transport in Plants</h1>
    <p style="margin: 0; color: #e0f2fe; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Xylem, Phloem, Transpiration & Translocation</p>
  </div>"""
    
    html = re.sub(
        r'(<div style="font-family: [^"]*box-sizing: border-box;">\s*)',
        r'\1' + top_banner + '\n\n',
        html
    )

    # Section 1: Replace bare h2 and wrap section 1 in container card
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-xylem-phloem"[^>]*>.*?</h2>',
        """<div id="sec-xylem-phloem" class="lecture-interactive-card" data-lecture-section="sec_xylem_phloem" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">💧 1. XYLEM AND PHLOEM (VASCULAR TISSUES)</h2>
    </div>""",
        html
    )

    # Section 1 Sub-cards: Xylem & Phloem
    html = re.sub(
        r'<div style="flex: 1; min-width: 320px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin-top: 0; color: #1d4ed8; font-size: 22px; border-bottom: 1px dashed #93c5fd; padding-bottom: 10px;">💧 Xylem Tissue</h3>',
        """<div id="sec-xylem-tissue" class="lecture-interactive-card" data-lecture-section="sec_xylem_tissue" style="flex: 1; min-width: 320px; background: #eff6ff; border: 2px solid #3b82f6; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #1d4ed8; background: #dbeafe; padding: 2px 8px; border-radius: 12px; border: 1px solid #93c5fd; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin-top: 0; color: #1d4ed8; font-size: 22px; border-bottom: 1px dashed #93c5fd; padding-bottom: 10px; padding-right: 90px;">💧 Xylem Tissue</h3>""",
        html
    )

    html = re.sub(
        r'<div style="flex: 1; min-width: 320px; background: #fffbeb; border: 2px solid #fde68a; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba\(0,0,0,0.02\);">\s*<h3 style="margin-top: 0; color: #d97706; font-size: 22px; border-bottom: 1px dashed #fcd34d; padding-bottom: 10px;">🍯 Phloem Tissue</h3>',
        """<div id="sec-phloem-tissue" class="lecture-interactive-card" data-lecture-section="sec_phloem_tissue" style="flex: 1; min-width: 320px; background: #fffbeb; border: 2px solid #f59e0b; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #d97706; background: #fef3c7; padding: 2px 8px; border-radius: 12px; border: 1px solid #fde68a; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin-top: 0; color: #d97706; font-size: 22px; border-bottom: 1px dashed #fcd34d; padding-bottom: 10px; padding-right: 90px;">🍯 Phloem Tissue</h3>""",
        html
    )

    # Section 2: Wrap into container card
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-vascular-position"[^>]*>.*?</h2>',
        """<div id="sec-vascular-position" class="lecture-interactive-card" data-lecture-section="sec_vascular_position" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">🗺️ 2. POSITION IN DICOTYLEDONOUS PLANTS</h2>
    </div>""",
        html
    )

    # Section 2 Sub-cards: Roots, Stems, Leaves
    html = re.sub(
        r'<div style="flex: 1; min-width: 280px; background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba\(0,0,0,0.05\);">\s*<h3 style="margin: 0 0 15px 0; color: #15803d; font-size: 20px;">🌱 In Roots</h3>',
        """<div id="sec-pos-roots" class="lecture-interactive-card" data-lecture-section="sec_pos_roots" style="flex: 1; min-width: 280px; background: #ffffff; border: 2px solid #10b981; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 12px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe</div>
        <h3 style="margin: 0 0 15px 0; color: #15803d; font-size: 20px;">🌱 In Roots</h3>""",
        html
    )

    html = re.sub(
        r'<div style="flex: 1; min-width: 280px; background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba\(0,0,0,0.05\);">\s*<h3 style="margin: 0 0 15px 0; color: #15803d; font-size: 20px;">🎋 In Stems</h3>',
        """<div id="sec-pos-stems" class="lecture-interactive-card" data-lecture-section="sec_pos_stems" style="flex: 1; min-width: 280px; background: #ffffff; border: 2px solid #10b981; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 12px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe</div>
        <h3 style="margin: 0 0 15px 0; color: #15803d; font-size: 20px;">🎋 In Stems</h3>""",
        html
    )

    html = re.sub(
        r'<div style="flex: 1; min-width: 280px; background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba\(0,0,0,0.05\);">\s*<h3 style="margin: 0 0 15px 0; color: #15803d; font-size: 20px;">🍃 In Leaves \(Midrib &amp; Veins\)</h3>',
        """<div id="sec-pos-leaves" class="lecture-interactive-card" data-lecture-section="sec_pos_leaves" style="flex: 1; min-width: 280px; background: #ffffff; border: 2px solid #10b981; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 12px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe</div>
        <h3 style="margin: 0 0 15px 0; color: #15803d; font-size: 20px;">🍃 In Leaves (Midrib &amp; Veins)</h3>""",
        html
    )

    # Section 3: Wrap into container card
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-transpiration"[^>]*>.*?</h2>',
        """<div id="sec-transpiration" class="lecture-interactive-card" data-lecture-section="sec_transpiration" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">🌬️ 3. WATER UPTAKE & TRANSPIRATION</h2>
    </div>""",
        html
    )

    # Section 4: Wrap into container card
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-translocation"[^>]*>.*?</h2>',
        """<div id="sec-translocation" class="lecture-interactive-card" data-lecture-section="sec_translocation" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 4</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">🍯 4. TRANSLOCATION (PHLOEM TRANSPORT)</h2>
    </div>""",
        html
    )

    return html

# =====================================================================
# B9 HTML TRANSFORMER
# =====================================================================
def build_b9_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b9_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Add Top Banner intro card
    top_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #991b1b 0%, #b91c1c 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(185,28,28,0.15); border: 1.5px solid #b91c1c; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #ef4444; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B9 • Animal Transport</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Transport in Animals & Blood Circulation</h1>
    <p style="margin: 0; color: #fecaca; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Heart Anatomy, Blood Vessels & Blood Composition</p>
  </div>"""
    
    html = re.sub(
        r'(<div style="font-family: [^"]*box-sizing: border-box;">\s*)',
        r'\1' + top_banner + '\n\n',
        html
    )

    # Section 1: Wrap into container card
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-circulation-system"[^>]*>.*?</h2>',
        """<div id="sec-circulation-system" class="lecture-interactive-card" data-lecture-section="sec_circulation_system" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">🩸 1. CIRCULATORY SYSTEMS (PUMP, VESSELS & VALVES)</h2>
    </div>""",
        html
    )

    # Section 2: Wrap into container card
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-heart-anatomy"[^>]*>.*?</h2>',
        """<div id="sec-heart-anatomy" class="lecture-interactive-card" data-lecture-section="sec_heart_anatomy" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">❤️ 2. MAMMALIAN HEART STRUCTURE & FUNCTION</h2>
    </div>""",
        html
    )

    # Section 3: CHD
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-chd"[^>]*>.*?</h2>',
        """<div id="sec-chd" class="lecture-interactive-card" data-lecture-section="sec_chd" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">🍔 3. CORONARY HEART DISEASE (CHD)</h2>
    </div>""",
        html
    )

    # Section 4: Blood Vessels
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-vessels-blood"[^>]*>.*?</h2>',
        """<div id="sec-vessels-blood" class="lecture-interactive-card" data-lecture-section="sec_vessels_blood" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 4</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">🧪 4. BLOOD VESSELS (ARTERIES, VEINS, CAPILLARIES)</h2>
    </div>""",
        html
    )

    # Section 5: Blood Composition
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-blood-composition"[^>]*>.*?</h2>',
        """<div id="sec-blood-composition" class="lecture-interactive-card" data-lecture-section="sec_blood_components" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 5</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">🩸 5. BLOOD COMPOSITION & CLOTTING MECHANISM</h2>
    </div>""",
        html
    )

    return html

# =====================================================================
# B10 HTML TRANSFORMER
# =====================================================================
def build_b10_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b10_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Add Top Banner intro card
    top_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #581c87 0%, #6b21a8 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(107,33,168,0.15); border: 1.5px solid #6b21a8; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #a855f7; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B10 • Pathology & Immunology</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Diseases and Immunity</h1>
    <p style="margin: 0; color: #e9d5ff; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Pathogens, Defences, Immunity & Cholera</p>
  </div>"""
    
    html = re.sub(
        r'(<div style="font-family: [^"]*box-sizing: border-box;">\s*)',
        r'\1' + top_banner + '\n\n',
        html
    )

    # Section 1: Wrap into container card
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-pathogens"[^>]*>.*?</h2>',
        """<div id="sec-pathogens" class="lecture-interactive-card" data-lecture-section="sec_pathogens" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">🦠 1. PATHOGENS AND TRANSMISSIBLE DISEASES</h2>
    </div>""",
        html
    )

    # Section 2: Defences
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-immune-response"[^>]*>.*?</h2>',
        """<div id="sec-defences" class="lecture-interactive-card" data-lecture-section="sec_defences" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">🛡️ 2. BODY'S DEFENCE MECHANISMS</h2>
    </div>""",
        html
    )

    # Section 3: Active and Passive Immunity
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-vaccination"[^>]*>.*?</h2>',
        """<div id="sec-immune-response" class="lecture-interactive-card" data-lecture-section="sec_immune_response" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">💉 3. ACTIVE AND PASSIVE IMMUNITY</h2>
    </div>""",
        html
    )

    # Section 4: Controlling the spread of disease
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-control-disease-en"[^>]*>.*?</h2>',
        """<div id="sec-disease-control" class="lecture-interactive-card" data-lecture-section="sec_disease_control" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 4</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">🌍 4. CONTROLLING THE SPREAD OF DISEASE</h2>
    </div>""",
        html
    )

    # Section 5: Cholera Mechanism
    html = re.sub(
        r'<div style="margin-bottom: 50px;">\s*<h2 id="sec-cholera-en"[^>]*>.*?</h2>',
        """<div id="sec-cholera" class="lecture-interactive-card" data-lecture-section="sec_cholera" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 5</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; padding-right: 180px;">
      <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
      <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">⚠️ 5. CHOLERA MECHANISM & ORT SUPPLEMENT</h2>
    </div>""",
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
    print("=== BUILDING BATCH 2 ENHANCED HTML (B7, B8, B9, B10) ===")
    b7 = build_b7_html()
    verify_and_save('b7', b7)
    
    b8 = build_b8_html()
    verify_and_save('b8', b8)
    
    b9 = build_b9_html()
    verify_and_save('b9', b9)
    
    b10 = build_b10_html()
    verify_and_save('b10', b10)
    print("🎉 BATCH 2 HTML TRANSFORMATION SUCCESSFUL!")
