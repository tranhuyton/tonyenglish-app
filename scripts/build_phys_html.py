import os
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

RAW_DIR = os.path.join(os.path.dirname(__file__), "raw_science_chem_phys")

def replace_top_study_with_header(html):
    # Pattern matching the top study resources div
    pattern_study = r'<div id="sec-header"[^>]*>.*?📚 Tài liệu học tập:.*?</div>'
    html = re.sub(pattern_study, '', html, flags=re.DOTALL)
    
    # Replace the top banner div with interactive card #sec-header
    old_banner_tag = '<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: #ffffff; padding: 25px 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin-bottom: 25px;">'
    new_banner_tag = """<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: #ffffff; padding: 25px 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin-bottom: 25px; position: relative; cursor: pointer;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255, 255, 255, 0.15); border: 1px solid rgba(255, 255, 255, 0.25); border-radius: 20px; font-size: 12px; font-weight: 600; color: #ffffff; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>"""
    
    assert old_banner_tag in html, "Could not find old_banner_tag in physics HTML"
    html = html.replace(old_banner_tag, new_banner_tag, 1)
    return html


def build_p1_html():
    raw_path = os.path.join(RAW_DIR, "p1_p1.html")
    with open(raw_path, "r", encoding="utf-8") as f:
        html = f.read()

    html = replace_top_study_with_header(html)

    # Sub-card 1 in Section 1: Measuring Instruments
    old_meas = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 20px;">'
    new_meas = """<div id="sec-measuring-instruments" class="lecture-interactive-card" data-lecture-section="sec_measuring_instruments" style="background: #f8fafc; border: 2px solid #bfdbfe; border-left: 6px solid #0284c7; border-radius: 12px; padding: 20px; margin-bottom: 20px; position: relative; cursor: pointer;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #0284c7; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 15px;">"""
    assert old_meas in html, "Could not find old_meas in P1"
    target_pos = html.find(old_meas)
    next_pos = html.find('<!-- Scalars vs Vectors Table -->', target_pos)
    sub_slice = html[target_pos:next_pos]
    last_div = sub_slice.rfind('</div>')
    sub_slice_new = sub_slice[:last_div] + '</div></div>'
    sub_slice_new = sub_slice_new.replace(old_meas, new_meas, 1)
    html = html[:target_pos] + sub_slice_new + html[next_pos:]

    # Sub-card 2 in Section 1: Scalars vs Vectors
    old_scal = '<div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 18px;">'
    new_scal = """<div id="sec-scalars-vectors" class="lecture-interactive-card" data-lecture-section="sec_scalars_vectors" style="background: #f0fdf4; border: 2px solid #bbf7d0; border-left: 6px solid #16a34a; border-radius: 12px; padding: 18px; position: relative; cursor: pointer;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #dcfce7; border: 1px solid #bbf7d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #15803d; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_scal in html, "Could not find old_scal in P1"
    html = html.replace(old_scal, new_scal, 1)

    # Sub-card 3 in Section 2: Kinematics Graphs Analyzer
    old_graphs = '<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 25px;">'
    new_graphs = """<div id="sec-kinematics-graphs" class="lecture-interactive-card" data-lecture-section="sec_kinematics_graphs" style="background: #ffffff; border: 2px solid #bfdbfe; border-left: 6px solid #2563eb; border-radius: 12px; padding: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 25px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_graphs in html, "Could not find old_graphs in P1"
    html = html.replace(old_graphs, new_graphs, 1)

    # Sub-card 4 in Section 2: Free Fall & Terminal Velocity
    # In P1 section 2, let's see where terminal velocity or free fall is:
    # Let's check if there is a box for free fall or summary table
    old_tbl = '<h3 style="color: #0f172a; font-size: 16px; margin-bottom: 10px; font-weight: 700;">Graph Interpretation Summary Table</h3>'
    new_tbl = """<div id="sec-free-fall" class="lecture-interactive-card" data-lecture-section="sec_free_fall" style="background: #f8fafc; border: 2px solid #cbd5e1; border-left: 6px solid #475569; border-radius: 12px; padding: 20px; margin-top: 15px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 20px; font-size: 12px; font-weight: 600; color: #334155; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>
  <h3 style="color: #0f172a; font-size: 16px; margin-bottom: 10px; font-weight: 700;">Graph Interpretation Summary Table</h3>"""
    assert old_tbl in html, "Could not find old_tbl in P1"
    # End of section 2 is before <!-- SECTION 3: MASS, WEIGHT & DENSITY
    target_pos = html.find(old_tbl)
    next_pos = html.find('<!-- SECTION 3: MASS, WEIGHT & DENSITY', target_pos)
    sub_slice = html[target_pos:next_pos]
    last_div = sub_slice.rfind('</div>')
    sub_slice_new = sub_slice[:last_div] + '</div></div>'
    sub_slice_new = sub_slice_new.replace(old_tbl, new_tbl, 1)
    html = html[:target_pos] + sub_slice_new + html[next_pos:]

    # Sub-card in Section 3: Density & Weight calculation
    old_den = '<div style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 25px;">'
    new_den = """<div id="sec-density-calc" class="lecture-interactive-card" data-lecture-section="sec_density_calc" style="background: #f8fafc; border: 2px solid #a7f3d0; border-left: 6px solid #059669; border-radius: 12px; padding: 20px; margin-bottom: 25px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #047857; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>
  <div style="display: flex; flex-wrap: wrap; gap: 20px; margin-top: 15px;">"""
    assert old_den in html, "Could not find old_den in P1"
    target_pos = html.find(old_den)
    next_pos = html.find('<!-- Mass vs Weight Comparison Table -->', target_pos)
    sub_slice = html[target_pos:next_pos]
    last_div = sub_slice.rfind('</div>')
    sub_slice_new = sub_slice[:last_div] + '</div></div>'
    sub_slice_new = sub_slice_new.replace(old_den, new_den, 1)
    html = html[:target_pos] + sub_slice_new + html[next_pos:]

    # Sub-card in Section 4: Turning Forces & Pressure Grid
    target_pos = html.find('id="sec-forces"')
    old_turn = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">'
    new_turn = """<div id="sec-moments-pressure" class="lecture-interactive-card" data-lecture-section="sec_moments_pressure" style="background: #f8fafc; border: 2px solid #cbd5e1; border-left: 6px solid #475569; border-radius: 12px; padding: 20px; margin-top: 15px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 20px; font-size: 12px; font-weight: 600; color: #334155; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 15px;">"""
    box_pos = html.find(old_turn, target_pos)
    assert box_pos != -1, "Could not find old_turn in P1 section 4"
    next_pos = html.find('<!-- SECTION 5: ENERGY STORES', box_pos)
    sub_slice = html[box_pos:next_pos]
    last_div = sub_slice.rfind('</div>')
    sub_slice_new = sub_slice[:last_div] + '</div></div>'
    sub_slice_new = sub_slice_new.replace(old_turn, new_turn, 1)
    html = html[:box_pos] + sub_slice_new + html[next_pos:]

    return html


def build_p2_html():
    raw_path = os.path.join(RAW_DIR, "p2_p1.html")
    with open(raw_path, "r", encoding="utf-8") as f:
        html = f.read()

    html = replace_top_study_with_header(html)

    # Sub-card in Section 1: Brownian motion & Gas pressure
    old_bp = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">'
    new_bp = """<div id="sec-brownian-pressure" class="lecture-interactive-card" data-lecture-section="sec_brownian_pressure" style="background: #f8fafc; border: 2px solid #bfdbfe; border-left: 6px solid #0284c7; border-radius: 12px; padding: 20px; margin-top: 15px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #0284c7; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 15px;">"""
    assert old_bp in html, "Could not find old_bp in P2"
    target_pos = html.find(old_bp)
    next_pos = html.find('<!-- SECTION 2: THERMAL PROPERTIES', target_pos)
    sub_slice = html[target_pos:next_pos]
    last_div = sub_slice.rfind('</div>')
    sub_slice_new = sub_slice[:last_div] + '</div></div>'
    sub_slice_new = sub_slice_new.replace(old_bp, new_bp, 1)
    html = html[:target_pos] + sub_slice_new + html[next_pos:]

    # Sub-card in Section 2: Evaporation & Cooling
    old_evap = '<div style="background: #f0fdfa; border-left: 5px solid #14b8a6; padding: 20px; border-radius: 0 10px 10px 0; margin-bottom: 25px;">'
    new_evap = """<div id="sec-evaporation-cooling" class="lecture-interactive-card" data-lecture-section="sec_evaporation_cooling" style="background: #f0fdfa; border: 2px solid #99f6e4; border-left: 6px solid #0d9488; padding: 20px; border-radius: 12px; margin-bottom: 25px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ccfbf1; border: 1px solid #99f6e4; border-radius: 20px; font-size: 12px; font-weight: 600; color: #0f766e; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_evap in html, "Could not find old_evap in P2"
    html = html.replace(old_evap, new_evap, 1)

    # Sub-card in Section 3: Convection & Radiation
    old_conv = '<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 30px;">'
    new_conv = """<div id="sec-convection-radiation" class="lecture-interactive-card" data-lecture-section="sec_convection_radiation" style="background: #ffffff; border: 2px solid #fecaca; border-left: 6px solid #ef4444; border-radius: 12px; padding: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 30px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fee2e2; border: 1px solid #fca5a5; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b91c1c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_conv in html, "Could not find old_conv in P2"
    html = html.replace(old_conv, new_conv, 1)

    return html


def build_p3_html():
    raw_path = os.path.join(RAW_DIR, "p3_p1.html")
    with open(raw_path, "r", encoding="utf-8") as f:
        html = f.read()

    html = replace_top_study_with_header(html)

    # Sub-card in Section 1: Transverse vs Longitudinal Wave Visualizer
    old_wave = '<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 25px;">'
    new_wave = """<div id="sec-transverse-longitudinal" class="lecture-interactive-card" data-lecture-section="sec_transverse_longitudinal" style="background: #ffffff; border: 2px solid #bfdbfe; border-left: 6px solid #0284c7; border-radius: 12px; padding: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 25px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #0284c7; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_wave in html, "Could not find old_wave in P3"
    html = html.replace(old_wave, new_wave, 1)

    # Sub-card in Section 2: Reflection, Refraction, Diffraction
    old_beh = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 15px;">'
    new_beh = """<div id="sec-reflection-refraction" class="lecture-interactive-card" data-lecture-section="sec_reflection_refraction" style="background: #f8fafc; border: 2px solid #bfdbfe; border-left: 6px solid #2563eb; border-radius: 12px; padding: 20px; margin-bottom: 25px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 15px; margin-top: 15px;">"""
    assert old_beh in html, "Could not find old_beh in P3"
    target_pos = html.find(old_beh)
    next_pos = html.find('<!-- SECTION 3: LIGHT', target_pos)
    sub_slice = html[target_pos:next_pos]
    last_div = sub_slice.rfind('</div>')
    sub_slice_new = sub_slice[:last_div] + '</div></div>'
    sub_slice_new = sub_slice_new.replace(old_beh, new_beh, 1)
    html = html[:target_pos] + sub_slice_new + html[next_pos:]

    return html


def build_p4_html():
    raw_path = os.path.join(RAW_DIR, "p4_p1.html")
    with open(raw_path, "r", encoding="utf-8") as f:
        html = f.read()

    html = replace_top_study_with_header(html)

    # Sub-card in Section 1: Resistance & Formula Triangles
    old_tri = '<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 25px;">'
    new_tri = """<div id="sec-resistance-factors" class="lecture-interactive-card" data-lecture-section="sec_resistance_factors" style="background: #ffffff; border: 2px solid #bfdbfe; border-left: 6px solid #2563eb; border-radius: 12px; padding: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 25px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #1d4ed8; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    assert old_tri in html, "Could not find old_tri in P4"
    html = html.replace(old_tri, new_tri, 1)

    # Sub-card in Section 2: Potential Dividers & Sensors
    target_pos = html.find('id="sec-electric-circuits"')
    old_box = '<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 25px;">'
    box_pos = html.find(old_box, target_pos)
    assert box_pos != -1, "Could not find potential divider box in P4 section 2"
    new_pot = """<div id="sec-potential-dividers" class="lecture-interactive-card" data-lecture-section="sec_potential_dividers" style="background: #ffffff; border: 2px solid #fbcfe8; border-left: 6px solid #db2777; border-radius: 12px; padding: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 25px; position: relative; cursor: pointer;">
  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fce7f3; border: 1px solid #fbcfe8; border-radius: 20px; font-size: 12px; font-weight: 600; color: #9d174d; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe mục này</div>"""
    html = html[:box_pos] + new_pot + html[box_pos + len(old_box):]

    return html


def build_p5_html():
    raw_path = os.path.join(RAW_DIR, "p5_p1.html")
    with open(raw_path, "r", encoding="utf-8") as f:
        html = f.read()

    html = replace_top_study_with_header(html)
    return html


def build_p6_html():
    raw_path = os.path.join(RAW_DIR, "p6_p1.html")
    with open(raw_path, "r", encoding="utf-8") as f:
        html = f.read()

    html = replace_top_study_with_header(html)
    return html


def verify_and_save():
    builders = [
        ("p1", build_p1_html),
        ("p2", build_p2_html),
        ("p3", build_p3_html),
        ("p4", build_p4_html),
        ("p5", build_p5_html),
        ("p6", build_p6_html),
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
