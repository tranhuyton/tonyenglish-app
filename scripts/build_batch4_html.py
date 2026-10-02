import os
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# =====================================================================
# B15 HTML TRANSFORMER
# =====================================================================
def build_b15_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b15_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #db2777 0%, #be185d 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1 -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #db2777 0%, #be185d 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(219,39,119,0.15); border: 1.5px solid #be185d; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #f472b6; color: #831843; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B15 • Reproductive Biology</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Reproduction</h1>
    <p style="margin: 0; color: #fce7f3; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Asexual vs sexual reproduction, floral anatomy, insect vs wind pollination, human reproductive anatomy, menstrual cycle, and STIs.</p>
  </div>

  <!-- SECTION 1 -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-reproduction-modes"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Wrap Asexual Reproduction div into interactive sub-card
    html = re.sub(
        r'<div style="background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 8px; padding: 16px;">\s*<h3 style="margin: 0 0 8px 0; color: #be185d; font-size: 16px;">Asexual Reproduction</h3>',
        """<div id="sec-asexual-repro" class="lecture-interactive-card" data-lecture-section="sec_asexual_repro" style="background: #fdf2f8; border: 1.5px solid #fbcfe8; border-left: 6px solid #db2777; border-radius: 10px; padding: 16px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #be185d; background: #fce7f3; padding: 2px 8px; border-radius: 12px; border: 1px solid #fbcfe8; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 8px 0; color: #be185d; font-size: 16px; padding-right: 90px;">🌱 Asexual Reproduction</h3>""",
        html
    )

    # Wrap Sexual Reproduction div into interactive sub-card
    html = re.sub(
        r'<div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 16px;">\s*<h3 style="margin: 0 0 8px 0; color: #15803d; font-size: 16px;">Sexual Reproduction</h3>',
        """<div id="sec-sexual-repro" class="lecture-interactive-card" data-lecture-section="sec_sexual_repro" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 6px solid #16a34a; border-radius: 10px; padding: 16px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #16a34a; background: #dcfce7; padding: 2px 8px; border-radius: 12px; border: 1px solid #bbf7d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 8px 0; color: #15803d; font-size: 16px; padding-right: 90px;">👶 Sexual Reproduction</h3>""",
        html
    )

    # Enhance Section 2 Header badge
    html = re.sub(
        r'(<div id="sec-flowering-plants"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Wrap Pollination modes table into sub-card
    html = re.sub(
        r'<!-- Wind vs Insect table -->\s*<h3 style="color: #be185d; margin: 24px 0 12px 0; font-size: 17px;">📊 Comparison: Insect-Pollinated vs Wind-Pollinated Flowers</h3>\s*<table style="width: 100%; border-collapse: collapse; background: white; font-size: 13.5px; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba\(0,0,0,0.05\); margin-bottom: 24px;">(.*?)</table>',
        """<div id="sec-pollination-modes" class="lecture-interactive-card" data-lecture-section="sec_pollination_modes" style="background: #ffffff; border: 1.5px solid #fbcfe8; border-left: 6px solid #be185d; border-radius: 12px; padding: 20px; margin-bottom: 24px; cursor: pointer; transition: all 0.2s ease; position: relative;">
      <div style="position: absolute; top: 14px; right: 14px; font-size: 11px; font-weight: 600; color: #be185d; background: #fdf2f8; padding: 2px 8px; border-radius: 12px; border: 1px solid #fbcfe8; pointer-events: none;">🎧 Nghe mục này</div>
      <h3 style="color: #be185d; margin: 0 0 14px 0; font-size: 17px; padding-right: 90px;">🐝 Comparison: Insect-Pollinated vs Wind-Pollinated Flowers</h3>
      <table style="width: 100%; border-collapse: collapse; background: white; font-size: 13.5px; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.05); margin-bottom: 0;">\\1</table>
    </div>""",
        html,
        flags=re.DOTALL
    )

    # Enhance Section 3 Header badge
    html = re.sub(
        r'(<div id="sec-human-reproduction"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Wrap Menstrual Cycle Interactive into sub-card
    html = re.sub(
        r'<!-- Menstrual cycle interactive -->\s*<h3 style="color: #be185d; margin: 30px 0 12px 0; font-size: 17px;">📅 The Menstrual Cycle: 28-Day Hormone Sequence</h3>\s*<p style="font-size: 13.5px; color: #475569; margin-bottom: 12px;"><i>Click each phase of the cycle to explore hormonal changes and uterine lining thickness:</i></p>\s*<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba\(0,0,0,0.05\); margin-bottom: 40px;">',
        """<div id="sec-menstrual-cycle" class="lecture-interactive-card" data-lecture-section="sec_menstrual_cycle" style="background: #ffffff; border: 1.5px solid #fde68a; border-left: 6px solid #f59e0b; border-radius: 12px; padding: 25px; margin-top: 30px; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
      <div style="position: absolute; top: 16px; right: 16px; font-size: 11px; font-weight: 600; color: #b45309; background: #fef3c7; padding: 2px 8px; border-radius: 12px; border: 1px solid #fde68a; pointer-events: none;">🎧 Nghe mục này</div>
      <h3 style="color: #b45309; margin: 0 0 8px 0; font-size: 18px; padding-right: 90px;">📅 The Menstrual Cycle: 28-Day Hormone Sequence</h3>
      <p style="font-size: 13.5px; color: #475569; margin-bottom: 20px;"><i>Click each phase of the cycle to explore hormonal changes and uterine lining thickness:</i></p>
      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">""",
        html
    )
    # Close the added outer wrapper for menstrual cycle
    html = re.sub(
        r'(<div id="cycle-panel"[^>]*>.*?</div>\s*</div>\s*</div>)(\s*</div>\s*<!-- SECTION 4 -->)',
        r'\1</div>\2',
        html,
        flags=re.DOTALL
    )

    # Enhance Section 4 Header badge
    html = re.sub(
        r'(<div id="sec-stis-hiv"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 4</div>',
        html,
        flags=re.DOTALL
    )

    out_path = "scripts/raw_science_bio_b3_b19/b15_p1_transformed.html"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("B15 HTML built successfully.")
    return html

# =====================================================================
# B16 HTML TRANSFORMER
# =====================================================================
def build_b16_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b16_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #0ea5e9 0%, #0284c7 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1 -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(14,165,233,0.15); border: 1.5px solid #0284c7; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #7dd3fc; color: #0c4a6e; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B16 • Genetics</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Inheritance</h1>
    <p style="margin: 0; color: #e0f2fe; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Chromosomes, genes, monohybrid crosses, Punnett squares, pedigree charts, and sex determination.</p>
  </div>

  <!-- SECTION 1 -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-genetic-code"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card in Section 1: Mitosis vs Meiosis
    html = re.sub(
        r'<!-- Haploid vs Diploid & Cell Division -->\s*<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin-bottom: 20px;">\s*<h4 style="margin: 0 0 8px 0; color: #0284c7; font-size: 15px;">➗ Cell Division &amp; Chromosome Numbers:</h4>',
        """<div id="sec-mitosis-meiosis" class="lecture-interactive-card" data-lecture-section="sec_mitosis_meiosis" style="background: #f8fafc; border: 1.5px solid #bae6fd; border-left: 6px solid #0284c7; border-radius: 10px; padding: 16px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #0284c7; background: #e0f2fe; padding: 2px 8px; border-radius: 12px; border: 1px solid #bae6fd; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 8px 0; color: #0369a1; font-size: 16px; padding-right: 90px;">➗ Cell Division &amp; Chromosome Numbers:</h4>""",
        html
    )

    # Enhance Section 2 Header badge
    html = re.sub(
        r'(<div id="sec-monohybrid-inheritance"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card in Section 2: Punnett Summary
    html = re.sub(
        r'<div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 14px; margin-top: 16px;">\s*<b style="color: #15803d; font-size: 14px;">Summary of <i>Tt</i> × <i>Tt</i> Cross Results:</b>',
        """<div id="sec-punnett-summary" class="lecture-interactive-card" data-lecture-section="sec_punnett_summary" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 6px solid #16a34a; border-radius: 10px; padding: 16px; margin-top: 16px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #16a34a; background: #dcfce7; padding: 2px 8px; border-radius: 12px; border: 1px solid #bbf7d0; pointer-events: none;">🎧 Nghe mục này</div>
        <b style="color: #15803d; font-size: 15px; display: block; margin-bottom: 6px; padding-right: 90px;">Summary of <i>Tt</i> × <i>Tt</i> Cross Results:</b>""",
        html
    )

    # Enhance Section 3 Header badge
    html = re.sub(
        r'(<div id="sec-pedigree-sex"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card in Section 3: Sex Determination
    html = re.sub(
        r'<!-- Sex determination -->\s*<div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 16px; margin-top: 24px;">\s*<h3 style="margin: 0 0 8px 0; color: #1d4ed8; font-size: 16px;">👦👧 Sex Determination in Humans \(50% Probability\)</h3>',
        """<div id="sec-sex-determination" class="lecture-interactive-card" data-lecture-section="sec_sex_determination" style="background: #eff6ff; border: 1.5px solid #bfdbfe; border-left: 6px solid #2563eb; border-radius: 10px; padding: 18px; margin-top: 24px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 14px; right: 14px; font-size: 11px; font-weight: 600; color: #2563eb; background: #dbeafe; padding: 2px 8px; border-radius: 12px; border: 1px solid #bfdbfe; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 8px 0; color: #1d4ed8; font-size: 16px; padding-right: 90px;">👦👧 Sex Determination in Humans (50% Probability)</h3>""",
        html
    )

    out_path = "scripts/raw_science_bio_b3_b19/b16_p1_transformed.html"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("B16 HTML built successfully.")
    return html

# =====================================================================
# B17 HTML TRANSFORMER
# =====================================================================
def build_b17_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b17_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #059669 0%, #047857 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1 -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #059669 0%, #047857 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(5,150,105,0.15); border: 1.5px solid #047857; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #6ee7b7; color: #064e3b; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B17 • Evolutionary Biology</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Variation &amp; Selection</h1>
    <p style="margin: 0; color: #d1fae5; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Continuous vs discontinuous variation, mutations, plant adaptations (xerophytes and hydrophytes), and natural vs artificial selection.</p>
  </div>

  <!-- SECTION 1 -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-variation-mutation"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card in Section 1: Continuous vs Discontinuous Variation
    html = re.sub(
        r'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px;">',
        """<div id="sec-continuous-discontinuous" class="lecture-interactive-card" data-lecture-section="sec_continuous_discontinuous" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 6px solid #10b981; border-radius: 12px; padding: 18px; margin-bottom: 24px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 12px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; color: #047857; font-size: 16px; padding-right: 90px;">📊 Continuous vs Discontinuous Variation</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">""",
        html
    )
    # Close added wrapper
    html = re.sub(
        r'(<!-- Mutation box -->)',
        r'</div>\n    \1',
        html
    )

    # Enhance Section 2 Header badge
    html = re.sub(
        r'(<div id="sec-adaptive-features"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card in Section 2: Xerophytes & Hydrophytes
    html = re.sub(
        r'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">\s*<div style="background: #fffbeb;',
        """<div id="sec-xerophytes-hydrophytes" class="lecture-interactive-card" data-lecture-section="sec_xerophytes_hydrophytes" style="background: #ffffff; border: 1.5px solid #fde68a; border-left: 6px solid #d97706; border-radius: 12px; padding: 18px; margin-top: 14px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #b45309; background: #fef3c7; padding: 2px 8px; border-radius: 12px; border: 1px solid #fde68a; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; color: #b45309; font-size: 16px; padding-right: 90px;">🌵 Xerophytes vs Hydrophytes Adaptations</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
        <div style="background: #fffbeb;""",
        html
    )
    # Close added wrapper
    html = re.sub(
        r'(</ul>\s*</div>\s*</div>)(\s*</div>\s*<!-- SECTION 3 -->)',
        r'\1</div>\2',
        html
    )

    # Enhance Section 3 Header badge
    html = re.sub(
        r'(<div id="sec-natural-selection"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card in Section 3: 5 Stages of Natural Selection
    html = re.sub(
        r'<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px; margin-bottom: 24px;">\s*<h3 style="margin: 0 0 10px 0; color: #047857; font-size: 16px;">The 5 Stages of Natural Selection \(Evolution\):</h3>',
        """<div id="sec-natural-selection-stages" class="lecture-interactive-card" data-lecture-section="sec_natural_selection_stages" style="background: #f8fafc; border: 1.5px solid #a7f3d0; border-left: 6px solid #059669; border-radius: 10px; padding: 20px; margin-bottom: 24px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 14px; right: 14px; font-size: 11px; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 12px; border: 1px solid #a7f3d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 10px 0; color: #047857; font-size: 16px; padding-right: 90px;">🌿 The 5 Stages of Natural Selection (Evolution):</h3>""",
        html
    )

    out_path = "scripts/raw_science_bio_b3_b19/b17_p1_transformed.html"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("B17 HTML built successfully.")
    return html

# =====================================================================
# B18 HTML TRANSFORMER
# =====================================================================
def build_b18_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b18_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #15803d 0%, #166534 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1 -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #15803d 0%, #166534 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(21,128,61,0.15); border: 1.5px solid #166534; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #86efac; color: #14532d; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B18 • Ecology</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Organisms &amp; Their Environment</h1>
    <p style="margin: 0; color: #dcfce7; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Ecological terminology, food chains, trophic levels, 10% energy loss rule, and the global carbon cycle.</p>
  </div>

  <!-- SECTION 1 -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-ecological-definitions"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Enhance Section 2 Header badge
    html = re.sub(
        r'(<div id="sec-food-chains-energy"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card in Section 2: 10% Rule Box
    html = re.sub(
        r'<!-- 10% Rule Box -->\s*<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 18px; margin-bottom: 24px;">\s*<h3 style="margin: 0 0 8px 0; color: #b45309; font-size: 16px;">📉 Why Food Chains Are Rarely Longer Than 4 or 5 Levels \(The 10% Rule\):</h3>',
        """<div id="sec-energy-loss-rule" class="lecture-interactive-card" data-lecture-section="sec_energy_loss_rule" style="background: #fffbeb; border: 1.5px solid #fde68a; border-left: 6px solid #d97706; border-radius: 10px; padding: 18px; margin-bottom: 24px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #b45309; background: #fef3c7; padding: 2px 8px; border-radius: 12px; border: 1px solid #fde68a; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 8px 0; color: #b45309; font-size: 16px; padding-right: 90px;">📉 The 10% Energy Loss Rule in Food Chains</h3>""",
        html
    )

    # Enhance Section 3 Header badge
    html = re.sub(
        r'(<div id="sec-carbon-cycle"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card in Section 3: 4 Carbon processes
    html = re.sub(
        r'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">\s*<div style="background: #f0fdf4;',
        """<div id="sec-carbon-processes" class="lecture-interactive-card" data-lecture-section="sec_carbon_processes" style="background: #ffffff; border: 1.5px solid #bbf7d0; border-left: 6px solid #16a34a; border-radius: 12px; padding: 18px; margin-top: 14px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #16a34a; background: #dcfce7; padding: 2px 8px; border-radius: 12px; border: 1px solid #bbf7d0; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; color: #15803d; font-size: 16px; padding-right: 90px;">♻️ Four Major Processes in the Carbon Cycle</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
        <div style="background: #f0fdf4;""",
        html
    )
    # Close wrapper
    html = re.sub(
        r'(<h4 style="margin: 0 0 6px 0; color: #1d4ed8; font-size: 15px;">4\. Combustion \(Releases CO₂\):</h4>\s*<p[^>]*>.*?</p>\s*</div>\s*</div>)(\s*</div>\s*</div>\s*$)',
        r'\1</div>\2',
        html,
        flags=re.DOTALL
    )

    out_path = "scripts/raw_science_bio_b3_b19/b18_p1_transformed.html"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("B18 HTML built successfully.")
    return html

# =====================================================================
# B19 HTML TRANSFORMER
# =====================================================================
def build_b19_html():
    raw_path = "scripts/raw_science_bio_b3_b19/b19_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Study Resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

    # Transform Top Banner into intro card
    old_banner_pattern = r'<div style="background: linear-gradient\(135deg, #0d9488 0%, #0f766e 100%\);[^>]*>(.*?)</div>\s*<!-- SECTION 1 -->'
    new_banner = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0d9488 0%, #0f766e 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(13,148,136,0.15); border: 1.5px solid #0f766e; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #5eead4; color: #134e4a; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B19 • Conservation & Environment</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Human Influences on Ecosystems</h1>
    <p style="margin: 0; color: #ccfbf1; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Agriculture and food supply, deforestation consequences, eutrophication in aquatic ecosystems, and biodiversity conservation.</p>
  </div>

  <!-- SECTION 1 -->"""
    html = re.sub(old_banner_pattern, new_banner, html, flags=re.DOTALL)

    # Enhance Section 1 Header badge
    html = re.sub(
        r'(<div id="sec-agriculture"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card in Section 1: Monoculture & Livestock
    html = re.sub(
        r'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 20px;">',
        """<div id="sec-monoculture-livestock" class="lecture-interactive-card" data-lecture-section="sec_monoculture_livestock" style="background: #ffffff; border: 1.5px solid #99f6e4; border-left: 6px solid #0d9488; border-radius: 12px; padding: 18px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; font-size: 11px; font-weight: 600; color: #0d9488; background: #f0fdfa; padding: 2px 8px; border-radius: 12px; border: 1px solid #99f6e4; pointer-events: none;">🎧 Nghe mục này</div>
        <h3 style="margin: 0 0 12px 0; color: #0f766e; font-size: 16px; padding-right: 90px;">🌾 Monocultures &amp; Intensive Livestock Farming</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">""",
        html
    )
    # Close wrapper
    html = re.sub(
        r'(</ul>\s*</div>\s*</div>)(\s*</div>\s*<!-- SECTION 2 -->)',
        r'\1</div>\2',
        html
    )

    # Enhance Section 2 Header badge
    html = re.sub(
        r'(<div id="sec-deforestation"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>',
        html,
        flags=re.DOTALL
    )

    # Sub-card in Section 2: Deforestation map
    html = re.sub(
        r'<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba\(0,0,0,0.05\); margin-bottom: 40px;">\s*<h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 22px; margin-bottom: 10px;">Interactive Effects of Deforestation</h3>',
        """<div id="sec-deforestation-effects" class="lecture-interactive-card" data-lecture-section="sec_deforestation_effects" style="background: #ffffff; border: 1.5px solid #fed7aa; border-left: 6px solid #ea580c; border-radius: 12px; padding: 25px; margin-bottom: 40px; box-shadow: 0 6px 16px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease; position: relative;">
      <div style="position: absolute; top: 16px; right: 16px; font-size: 11px; font-weight: 600; color: #c2410c; background: #fff7ed; padding: 2px 8px; border-radius: 12px; border: 1px solid #fed7aa; pointer-events: none;">🎧 Nghe mục này</div>
      <h3 style="text-align: center; color: #9a3412; margin-top: 0; font-size: 22px; margin-bottom: 10px;">🚜 Interactive Effects of Deforestation</h3>""",
        html
    )

    # Enhance Section 3 Header badge
    html = re.sub(
        r'(<div id="sec-eutrophication"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>',
        html,
        flags=re.DOTALL
    )

    # Enhance Section 4 Header badge
    html = re.sub(
        r'(<div id="sec-conservation"[^>]*>.*?)(<span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669;[^>]*>Nghe phần này</span>)',
        r'\1<div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 4</div>',
        html,
        flags=re.DOTALL
    )

    out_path = "scripts/raw_science_bio_b3_b19/b19_p1_transformed.html"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("B19 HTML built successfully.")
    return html

def check_div_balance(filename, html_content):
    opens = len(re.findall(r'<div\b[^>]*>', html_content, re.IGNORECASE))
    closes = len(re.findall(r'</div>', html_content, re.IGNORECASE))
    diff = opens - closes
    print(f"{filename}: <div> opens={opens}, closes={closes}, diff={diff}")
    return diff == 0

def main():
    print("=== BUILDING & VALIDATING BATCH 4 HTML (B15, B16, B17, B18, B19) ===")
    h15 = build_b15_html()
    h16 = build_b16_html()
    h17 = build_b17_html()
    h18 = build_b18_html()
    h19 = build_b19_html()

    all_balanced = True
    for name, content in [('b15', h15), ('b16', h16), ('b17', h17), ('b18', h18), ('b19', h19)]:
        if not check_div_balance(name, content):
            all_balanced = False

    if all_balanced:
        print("\n🎉 ALL BATCH 4 HTML FILES ARE 100% BALANCED (DIFF = 0)!")
    else:
        print("\n❌ SOME FILES HAVE DIV IMBALANCES. PLEASE FIX!")

if __name__ == "__main__":
    main()
