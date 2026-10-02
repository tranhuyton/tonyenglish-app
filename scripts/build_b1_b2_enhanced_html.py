import re
import sys
import json
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==========================================
# B1 HTML BUILDER
# ==========================================
b1_html = """<div style="font-family: 'Segoe UI', Arial, sans-serif; width: 100%; color: #334155; line-height: 1.65; box-sizing: border-box;">

  <!-- TOPIC INTRO HEADER CARD -->
  <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(15,23,42,0.15); border: 1.5px solid #334155; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 20px; font-size: 12px; font-weight: 600; color: #93c5fd; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #3b82f6; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B1 • Core Biology</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Characteristics of Living Organisms</h1>
    <p style="margin: 0; color: #94a3b8; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • The Seven Fundamental Life Processes</p>
  </div>

  <!-- SECTION 1: MRS GREN (CONTAINER CARD) -->
  <div id="sec-mrsgren" class="lecture-interactive-card" data-lecture-section="sec_mrsgren" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 1</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 12px; padding-right: 170px;">
        <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
        <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">1. The Seven Characteristics of Living Things (MRS GREN)</h2>
    </div>
    <p style="font-size: 15px; color: #475569; margin-bottom: 22px;">All living organisms share seven fundamental life processes. You can easily remember them using the mnemonic <strong style="color: #2563eb;">MRS GREN</strong>. Nhấn vào từng mục nhỏ bên dưới để nghe bài giảng chi tiết:</p>

    <!-- SUB-CARDS GRID (7 LIFE PROCESSES) -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 10px;">
      
      <!-- SUB-CARD 1: MOVEMENT -->
      <div id="sec-movement" class="lecture-interactive-card" data-lecture-section="sec_movement" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-left: 6px solid #3b82f6; border-radius: 10px; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 12px; font-size: 11px; font-weight: 600; color: #2563eb; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; padding-right: 100px;">
          <h3 style="margin: 0; font-size: 17px; color: #1e40af;">🏃 Movement (M)</h3>
          <span style="font-size: 11px; background: #eff6ff; color: #3b82f6; font-weight: 700; padding: 2px 6px; border-radius: 4px;">Syllabus B1.1(a)</span>
        </div>
        <p style="margin: 0 0 8px 0; font-size: 14px; color: #0f172a; font-weight: 600;">"An action by an organism or part of an organism causing a change of position or place."</p>
        <p style="margin: 0; font-size: 13px; color: #64748b;">• <em>Animals:</em> Move entire bodies using locomotion (walking, swimming, flying).<br/>• <em>Plants:</em> Move parts slowly in response to stimuli (tropisms, e.g. shoots bending toward light).</p>
      </div>

      <!-- SUB-CARD 2: RESPIRATION -->
      <div id="sec-respiration" class="lecture-interactive-card" data-lecture-section="sec_respiration" style="background: #ffffff; border: 1.5px solid #fecaca; border-left: 6px solid #ef4444; border-radius: 10px; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #fef2f2; border: 1px solid #fecaca; border-radius: 12px; font-size: 11px; font-weight: 600; color: #dc2626; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; padding-right: 100px;">
          <h3 style="margin: 0; font-size: 17px; color: #b91c1c;">💨 Respiration (R)</h3>
          <span style="font-size: 11px; background: #fef2f2; color: #ef4444; font-weight: 700; padding: 2px 6px; border-radius: 4px;">Syllabus B1.1(b)</span>
        </div>
        <p style="margin: 0 0 8px 0; font-size: 14px; color: #0f172a; font-weight: 600;">"The chemical reactions in cells that break down nutrient molecules and release energy for metabolism."</p>
        <p style="margin: 0; font-size: 13px; color: #64748b;">• <em>Key Note:</em> Respiration is a cellular chemical process, NOT the same as breathing/ventilation. Occurs in both plants and animals 24/7.</p>
      </div>

      <!-- SUB-CARD 3: SENSITIVITY -->
      <div id="sec-sensitivity" class="lecture-interactive-card" data-lecture-section="sec_sensitivity" style="background: #ffffff; border: 1.5px solid #fed7aa; border-left: 6px solid #f59e0b; border-radius: 10px; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #fffbeb; border: 1px solid #fed7aa; border-radius: 12px; font-size: 11px; font-weight: 600; color: #d97706; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; padding-right: 100px;">
          <h3 style="margin: 0; font-size: 17px; color: #b45309;">👀 Sensitivity (S)</h3>
          <span style="font-size: 11px; background: #fffbeb; color: #f59e0b; font-weight: 700; padding: 2px 6px; border-radius: 4px;">Syllabus B1.1(c)</span>
        </div>
        <p style="margin: 0 0 8px 0; font-size: 14px; color: #0f172a; font-weight: 600;">"The ability to detect and respond to changes in the internal or external environment."</p>
        <p style="margin: 0; font-size: 13px; color: #64748b;">• <em>Receptors:</em> Sense organs detect stimuli (light, sound, chemicals, touch). Effectors (muscles, glands) carry out responses.</p>
      </div>

      <!-- SUB-CARD 4: GROWTH -->
      <div id="sec-growth" class="lecture-interactive-card" data-lecture-section="sec_growth" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 6px solid #10b981; border-radius: 10px; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 12px; font-size: 11px; font-weight: 600; color: #059669; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; padding-right: 100px;">
          <h3 style="margin: 0; font-size: 17px; color: #047857;">🌱 Growth (G)</h3>
          <span style="font-size: 11px; background: #ecfdf5; color: #10b981; font-weight: 700; padding: 2px 6px; border-radius: 4px;">Syllabus B1.1(d)</span>
        </div>
        <p style="margin: 0 0 8px 0; font-size: 14px; color: #0f172a; font-weight: 600;">"A permanent increase in size and dry mass."</p>
        <p style="margin: 0; font-size: 13px; color: #64748b;">• <em>Mechanism:</em> Accomplished through cell division (mitosis) and cell enlargement. "Dry mass" refers to mass after removing all water.</p>
      </div>

      <!-- SUB-CARD 5: REPRODUCTION -->
      <div id="sec-reproduction" class="lecture-interactive-card" data-lecture-section="sec_reproduction" style="background: #ffffff; border: 1.5px solid #ddd6fe; border-left: 6px solid #8b5cf6; border-radius: 10px; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 12px; font-size: 11px; font-weight: 600; color: #7c3aed; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; padding-right: 100px;">
          <h3 style="margin: 0; font-size: 17px; color: #6d28d9;">👶 Reproduction (R)</h3>
          <span style="font-size: 11px; background: #f5f3ff; color: #8b5cf6; font-weight: 700; padding: 2px 6px; border-radius: 4px;">Syllabus B1.1(e)</span>
        </div>
        <p style="margin: 0 0 8px 0; font-size: 14px; color: #0f172a; font-weight: 600;">"The processes that make more of the same kind of organism."</p>
        <p style="margin: 0; font-size: 13px; color: #64748b;">• <em>Asexual:</em> 1 parent, clones (identical).<br/>• <em>Sexual:</em> 2 parents, fusion of haploid gamete nuclei to create genetic variation.</p>
      </div>

      <!-- SUB-CARD 6: EXCRETION -->
      <div id="sec-excretion" class="lecture-interactive-card" data-lecture-section="sec_excretion" style="background: #ffffff; border: 1.5px solid #fbcfe8; border-left: 6px solid #ec4899; border-radius: 10px; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 12px; font-size: 11px; font-weight: 600; color: #db2777; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; padding-right: 100px;">
          <h3 style="margin: 0; font-size: 17px; color: #be185d;">🚽 Excretion (E)</h3>
          <span style="font-size: 11px; background: #fdf2f8; color: #ec4899; font-weight: 700; padding: 2px 6px; border-radius: 4px;">Syllabus B1.1(f)</span>
        </div>
        <p style="margin: 0 0 8px 0; font-size: 14px; color: #0f172a; font-weight: 600;">"The removal of the waste products of metabolism and substances in excess of requirements."</p>
        <p style="margin: 0; font-size: 13px; color: #64748b;">• <em>Examples:</em> Carbon dioxide from lungs, urea and excess salts from kidneys.</p>
      </div>

      <!-- SUB-CARD 7: NUTRITION -->
      <div id="sec-nutrition" class="lecture-interactive-card" data-lecture-section="sec_nutrition" style="background: #ffffff; border: 1.5px solid #a5f3fc; border-left: 6px solid #06b6d4; border-radius: 10px; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #ecfeff; border: 1px solid #a5f3fc; border-radius: 12px; font-size: 11px; font-weight: 600; color: #0891b2; pointer-events: none;">🎧 Nghe mục này</div>
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; padding-right: 100px;">
          <h3 style="margin: 0; font-size: 17px; color: #0e7490;">🍽️ Nutrition (N)</h3>
          <span style="font-size: 11px; background: #ecfeff; color: #06b6d4; font-weight: 700; padding: 2px 6px; border-radius: 4px;">Syllabus B1.1(g)</span>
        </div>
        <p style="margin: 0 0 8px 0; font-size: 14px; color: #0f172a; font-weight: 600;">"The taking in of materials for energy, growth and development."</p>
        <p style="margin: 0; font-size: 13px; color: #64748b;">• <em>Autotrophic (Plants):</em> Synthesise organic compounds via photosynthesis using light, CO₂, and water.<br/>• <em>Heterotrophic (Animals):</em> Ingest organic compounds by eating other organisms.</p>
      </div>

    </div>
  </div>

  <!-- SECTION: EXCRETION VS EGESTION WARNING -->
  <div id="sec-excretion-warning" class="lecture-interactive-card" data-lecture-section="sec_excretion_warning" style="background: #fffbeb; border: 1.5px solid #fde68a; border-left: 6px solid #f59e0b; border-radius: 14px; padding: 22px 26px; margin-bottom: 32px; box-shadow: 0 4px 10px rgba(245,158,11,0.05); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fef3c7; border: 1px solid #fde68a; border-radius: 20px; font-size: 12px; font-weight: 600; color: #b45309; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <h3 style="margin: 0 0 10px 0; color: #92400e; font-size: 18px; padding-right: 140px;">⚠️ Cambridge Exam Warning: Excretion vs. Egestion</h3>
    <p style="margin: 0 0 14px 0; font-size: 14px; color: #78350f;">Students frequently confuse <strong>excretion</strong> with <strong>egestion</strong>. This is one of the most tested distinctions in Paper 2 and Paper 4:</p>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
      <div style="background: #ffffff; padding: 14px 18px; border-radius: 8px; border: 1px solid #fcd34d;">
        <strong style="color: #b45309; font-size: 14.5px;">Excretion (Bài tiết):</strong>
        <p style="margin: 6px 0 0 0; font-size: 13px; color: #451a03; line-height: 1.6;">Removal of <strong>metabolic waste products</strong> produced <em>inside body cells</em> through biochemical reactions (e.g., urea in urine, CO₂ from cellular respiration).</p>
      </div>
      <div style="background: #ffffff; padding: 14px 18px; border-radius: 8px; border: 1px solid #fcd34d;">
        <strong style="color: #b45309; font-size: 14.5px;">Egestion (Tống phân):</strong>
        <p style="margin: 6px 0 0 0; font-size: 13px; color: #451a03; line-height: 1.6;">Passing out of <strong>undigested food as faeces</strong> through the anus. This material was <em>never absorbed into body cells</em> and was never part of cellular metabolism.</p>
      </div>
    </div>
  </div>

  <!-- SECTION 2: 5 KINGDOMS CLASSIFICATION -->
  <div id="sec-five-kingdoms" class="lecture-interactive-card" data-lecture-section="sec_five_kingdoms" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 12px; padding-right: 140px;">
        <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
        <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">2. Classification of Living Organisms: The Five Kingdoms</h2>
    </div>
    <div style="overflow-x: auto;">
      <table style="width: 100%; border-collapse: collapse; font-size: 13.5px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px;">
        <thead>
          <tr style="background: #f8fafc; border-bottom: 2px solid #cbd5e1; color: #0f172a;">
            <th style="padding: 10px 14px; text-align: left;">Kingdom</th>
            <th style="padding: 10px 14px; text-align: left;">Cell Type</th>
            <th style="padding: 10px 14px; text-align: left;">Cell Wall</th>
            <th style="padding: 10px 14px; text-align: left;">Chloroplasts</th>
            <th style="padding: 10px 14px; text-align: left;">Feeding Method</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid #f1f5f9;">
            <td style="padding: 10px 14px; font-weight: 700; color: #1e40af;">Animals</td>
            <td style="padding: 10px 14px;">Multicellular eukaryote</td>
            <td style="padding: 10px 14px; color: #dc2626;">Absent</td>
            <td style="padding: 10px 14px; color: #dc2626;">Absent</td>
            <td style="padding: 10px 14px;">Heterotrophic (ingestion)</td>
          </tr>
          <tr style="border-bottom: 1px solid #f1f5f9; background: #fafafa;">
            <td style="padding: 10px 14px; font-weight: 700; color: #15803d;">Plants</td>
            <td style="padding: 10px 14px;">Multicellular eukaryote</td>
            <td style="padding: 10px 14px; color: #15803d;">Present (Cellulose)</td>
            <td style="padding: 10px 14px; color: #15803d;">Present</td>
            <td style="padding: 10px 14px;">Autotrophic (Photosynthesis)</td>
          </tr>
          <tr style="border-bottom: 1px solid #f1f5f9;">
            <td style="padding: 10px 14px; font-weight: 700; color: #d97706;">Fungi</td>
            <td style="padding: 10px 14px;">Mostly multicellular (except yeast)</td>
            <td style="padding: 10px 14px; color: #15803d;">Present (Chitin)</td>
            <td style="padding: 10px 14px; color: #dc2626;">Absent</td>
            <td style="padding: 10px 14px;">Saprotrophic / Heterotrophic</td>
          </tr>
          <tr style="border-bottom: 1px solid #f1f5f9; background: #fafafa;">
            <td style="padding: 10px 14px; font-weight: 700; color: #7c3aed;">Protoctists</td>
            <td style="padding: 10px 14px;">Mostly unicellular eukaryotes</td>
            <td style="padding: 10px 14px;">Variable</td>
            <td style="padding: 10px 14px;">Some present (e.g. Chlorella)</td>
            <td style="padding: 10px 14px;">Autotrophic or Heterotrophic</td>
          </tr>
          <tr>
            <td style="padding: 10px 14px; font-weight: 700; color: #0284c7;">Prokaryotes (Bacteria)</td>
            <td style="padding: 10px 14px;">Unicellular, no true nucleus</td>
            <td style="padding: 10px 14px; color: #15803d;">Present (Peptidoglycan)</td>
            <td style="padding: 10px 14px; color: #dc2626;">Absent</td>
            <td style="padding: 10px 14px;">Diverse (Saprotrophic/Autotrophic)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

</div>"""

# ==========================================
# B2 HTML BUILDER
# ==========================================
b2_html = """<div style="font-family: 'Segoe UI', Arial, sans-serif; width: 100%; color: #334155; line-height: 1.65; box-sizing: border-box;">

  <!-- TOPIC INTRO HEADER CARD -->
  <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #1e3a8a 0%, #0284c7 100%); color: #f8fafc; padding: 25px 30px; border-radius: 14px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(30,58,138,0.15); border: 1.5px solid #0369a1; cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.25); border-radius: 20px; font-size: 12px; font-weight: 600; color: #bae6fd; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: inline-block; background: #38bdf8; color: #082f49; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Topic B2 • Cell Biology</div>
    <h1 style="margin: 0 0 8px 0; font-size: 26px; font-weight: 800; color: #ffffff; padding-right: 140px;">Cells and Organisms</h1>
    <p style="margin: 0; color: #e0f2fe; font-size: 15px;">Cambridge IGCSE Co-ordinated Sciences (0654) • Ultrastructure, Specialized Cells & Magnification</p>
  </div>

  <!-- SECTION 1: CELL COMPARISON TABLE -->
  <div id="sec-cell-comparison" class="lecture-interactive-card" data-lecture-section="sec_cell_comparison" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 12px; padding-right: 140px;">
        <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
        <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">1. Comparison of Plant, Animal and Bacterial Cells</h2>
    </div>
    <div style="overflow-x: auto;">
      <table style="width: 100%; border-collapse: collapse; font-size: 13.5px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px;">
        <thead>
          <tr style="background: #f8fafc; border-bottom: 2px solid #cbd5e1; color: #0f172a;">
            <th style="padding: 10px 14px; text-align: left;">Cell Structure</th>
            <th style="padding: 10px 14px; text-align: left;">Animal Cell</th>
            <th style="padding: 10px 14px; text-align: left;">Plant Cell</th>
            <th style="padding: 10px 14px; text-align: left;">Bacterial Cell</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid #f1f5f9;">
            <td style="padding: 10px 14px; font-weight: 700; color: #1e40af;">Cell Membrane</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present</td>
          </tr>
          <tr style="border-bottom: 1px solid #f1f5f9; background: #fafafa;">
            <td style="padding: 10px 14px; font-weight: 700; color: #1e40af;">Cytoplasm & Ribosomes</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present</td>
          </tr>
          <tr style="border-bottom: 1px solid #f1f5f9;">
            <td style="padding: 10px 14px; font-weight: 700; color: #1e40af;">True Nucleus & DNA</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present (linear DNA)</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present (linear DNA)</td>
            <td style="padding: 10px 14px; color: #dc2626;">✖ Absent (Circular DNA loop + Plasmids)</td>
          </tr>
          <tr style="border-bottom: 1px solid #f1f5f9; background: #fafafa;">
            <td style="padding: 10px 14px; font-weight: 700; color: #1e40af;">Cell Wall</td>
            <td style="padding: 10px 14px; color: #dc2626;">✖ Absent</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present (Cellulose)</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present (Peptidoglycan)</td>
          </tr>
          <tr style="border-bottom: 1px solid #f1f5f9;">
            <td style="padding: 10px 14px; font-weight: 700; color: #1e40af;">Chloroplasts</td>
            <td style="padding: 10px 14px; color: #dc2626;">✖ Absent</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present in photosynthetic cells</td>
            <td style="padding: 10px 14px; color: #dc2626;">✖ Absent</td>
          </tr>
          <tr style="border-bottom: 1px solid #f1f5f9; background: #fafafa;">
            <td style="padding: 10px 14px; font-weight: 700; color: #1e40af;">Mitochondria</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Present</td>
            <td style="padding: 10px 14px; color: #dc2626;">✖ Absent</td>
          </tr>
          <tr>
            <td style="padding: 10px 14px; font-weight: 700; color: #1e40af;">Vacuoles</td>
            <td style="padding: 10px 14px; color: #64748b;">Small, temporary vesicles</td>
            <td style="padding: 10px 14px; color: #15803d;">✔ Large permanent central vacuole</td>
            <td style="padding: 10px 14px; color: #dc2626;">✖ Absent</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- SECTION 2: INTERACTIVE CELL MAP & ORGANELLE FUNCTIONS -->
  <div id="sec-organelles" class="lecture-interactive-card" data-lecture-section="sec_organelles" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 2</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 12px; padding-right: 170px;">
        <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
        <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">2. Interactive Cell Map & Organelle Functions</h2>
    </div>

    <!-- SVG CELL DIAGRAM WRAPPER -->
    <div style="background-color: #f8fafc; border-radius: 12px; padding: 24px; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); border: 1.5px solid #e2e8f0; margin-bottom: 25px;">
      <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 20px;">Interactive Cell Ultrastructure</h3>
      <p style="text-align: center; color: #64748b; font-style: italic; margin-bottom: 24px; font-size: 15px;">Hover over or tap any organelle in the diagrams to inspect its definition and play its lecture</p>
      
      <div style="display: flex; flex-wrap: wrap; gap: 24px; justify-content: center;">
        
        <!-- ANIMAL CELL SVG -->
        <div style="flex: 1; min-width: 280px; text-align: center; background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #e2e8f0;">
          <h4 style="margin-top: 0; margin-bottom: 16px; color: #334155; font-size: 18px;">🐾 Animal Cell</h4>
          <svg height="auto" style="max-width: 220px; display: block; margin: 0 auto;" viewbox="0 0 300 300" width="100%">
            <!-- Cytoplasm -->
            <circle cx="150" cy="150" r="120" fill="#e0f2fe" stroke="#bae6fd" stroke-width="2" data-lecture-section="sec_cytoplasm" onmouseout="this.style.stroke='#bae6fd'; this.style.strokeWidth='2px';" onmouseover="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-cytoplasm').innerHTML; this.style.stroke='#f59e0b'; this.style.strokeWidth='5px';" style="cursor: pointer; transition: 0.2s;"></circle>
            <!-- Cell Membrane -->
            <circle cx="150" cy="150" r="120" fill="none" stroke="#38bdf8" stroke-width="6" data-lecture-section="sec_membrane" onmouseout="this.style.stroke='#38bdf8'; this.style.strokeWidth='6px';" onmouseover="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-membrane').innerHTML; this.style.stroke='#f59e0b'; this.style.strokeWidth='9px';" style="cursor: pointer; transition: 0.2s;"></circle>
            <!-- Nucleus -->
            <circle cx="150" cy="110" r="35" fill="#818cf8" data-lecture-section="sec_nucleus" onmouseout="this.style.stroke='none';" onmouseover="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-nucleus').innerHTML; this.style.stroke='#f59e0b'; this.style.strokeWidth='4px';" style="cursor: pointer; transition: 0.2s;"></circle>
            <circle cx="150" cy="110" r="12" fill="#4f46e5" pointer-events="none"></circle>
            <!-- Mitochondria -->
            <g data-lecture-section="sec_mitochondria" onmouseout="this.removeAttribute('stroke'); this.removeAttribute('stroke-width');" onmouseover="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-mitochondria').innerHTML; this.setAttribute('stroke', '#f59e0b'); this.setAttribute('stroke-width', '3');" style="cursor: pointer; transition: 0.2s;">
              <ellipse cx="100" cy="200" fill="#f87171" rx="20" ry="10" transform="rotate(-30 100 200)"></ellipse>
              <path d="M 85 200 Q 100 190 115 200" fill="none" stroke="#b91c1c" stroke-width="2" transform="rotate(-30 100 200)"></path>
              <ellipse cx="200" cy="180" fill="#f87171" rx="20" ry="10" transform="rotate(45 200 180)"></ellipse>
              <path d="M 185 180 Q 200 170 215 180" fill="none" stroke="#b91c1c" stroke-width="2" transform="rotate(45 200 180)"></path>
            </g>
          </svg>
        </div>

        <!-- PLANT CELL SVG -->
        <div style="flex: 1; min-width: 280px; text-align: center; background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #e2e8f0;">
          <h4 style="margin-top: 0; margin-bottom: 16px; color: #334155; font-size: 18px;">🌿 Plant Cell</h4>
          <svg height="auto" style="max-width: 220px; display: block; margin: 0 auto;" viewbox="0 0 300 300" width="100%">
            <!-- Cell Wall -->
            <rect x="30" y="20" width="240" height="260" rx="20" fill="#86efac" stroke="#22c55e" stroke-width="12" data-lecture-section="sec_cellwall" onmouseout="this.style.stroke='#22c55e'; this.style.strokeWidth='12px';" onmouseover="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-cellwall').innerHTML; this.style.stroke='#f59e0b'; this.style.strokeWidth='14px';" style="cursor: pointer; transition: 0.2s;"></rect>
            <!-- Cell Membrane -->
            <rect x="36" y="26" width="228" height="248" rx="15" fill="none" stroke="#facc15" stroke-width="4" data-lecture-section="sec_membrane" onmouseout="this.style.stroke='#facc15'; this.style.strokeWidth='4px';" onmouseover="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-membrane').innerHTML; this.style.stroke='#f59e0b'; this.style.strokeWidth='8px';" style="cursor: pointer; transition: 0.2s;"></rect>
            <!-- Cytoplasm -->
            <rect x="38" y="28" width="224" height="244" rx="14" fill="#dcfce7" data-lecture-section="sec_cytoplasm" onmouseout="this.style.fill='#dcfce7';" onmouseover="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-cytoplasm').innerHTML; this.style.fill='#bbf7d0';" style="cursor: pointer; transition: 0.2s;"></rect>
            <!-- Permanent Vacuole -->
            <rect x="70" y="60" width="160" height="120" rx="30" fill="#bfdbfe" stroke="#60a5fa" stroke-width="3" data-lecture-section="sec_vacuole" onmouseout="this.style.stroke='#60a5fa'; this.style.strokeWidth='3px';" onmouseover="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-vacuole').innerHTML; this.style.stroke='#f59e0b'; this.style.strokeWidth='6px';" style="cursor: pointer; transition: 0.2s;"></rect>
            <!-- Nucleus -->
            <circle cx="210" cy="220" r="30" fill="#818cf8" data-lecture-section="sec_nucleus" onmouseout="this.style.stroke='none';" onmouseover="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-nucleus').innerHTML; this.style.stroke='#f59e0b'; this.style.strokeWidth='4px';" style="cursor: pointer; transition: 0.2s;"></circle>
            <!-- Chloroplasts -->
            <g data-lecture-section="sec_chloroplast" onmouseout="this.removeAttribute('stroke'); this.removeAttribute('stroke-width');" onmouseover="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-chloroplast').innerHTML; this.setAttribute('stroke', '#f59e0b'); this.setAttribute('stroke-width', '4');" style="cursor: pointer; transition: 0.2s;">
              <ellipse cx="60" cy="190" rx="15" ry="25" fill="#22c55e"></ellipse>
              <ellipse cx="130" cy="240" rx="25" ry="15" fill="#22c55e"></ellipse>
            </g>
            <!-- Mitochondria -->
            <g data-lecture-section="sec_mitochondria" onmouseout="this.removeAttribute('stroke'); this.removeAttribute('stroke-width');" onmouseover="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-mitochondria').innerHTML; this.setAttribute('stroke', '#f59e0b'); this.setAttribute('stroke-width', '3');" style="cursor: pointer; transition: 0.2s;">
              <ellipse cx="80" cy="40" rx="15" ry="8" fill="#f87171"></ellipse>
            </g>
          </svg>
        </div>

      </div>

      <!-- MAIN INFO PANEL (DISPLAYS ACTIVE ORGANELLE DETAILS) -->
      <div id="te-main-info-panel" style="margin-top: 24px; padding: 20px 24px; background-color: #eff6ff; border-left: 6px solid #3b82f6; border-radius: 8px; min-height: 120px; box-sizing: border-box; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <h4 style="color: #1d4ed8; margin: 0 0 8px 0; font-size: 18px;">Interactive Organelle Explorer 👆</h4>
        <p style="margin: 0; color: #334155; line-height: 1.6; font-size: 15px;">Rê chuột hoặc nhấn vào bất kỳ bào quan nào trên hình hoặc danh sách thẻ bên dưới để xem chi tiết định nghĩa và nghe bài giảng.</p>
      </div>
    </div>

    <!-- ORGANELLE DETAILED SUB-CARDS GRID (BOUNDED CARDS) -->
    <h3 style="color: #0f172a; margin: 25px 0 14px 0; font-size: 18px; font-weight: 700;">Danh mục bài giảng chi tiết từng bào quan:</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-bottom: 10px;">
      
      <!-- SUB-CARD: NUCLEUS -->
      <div id="sec-nucleus" class="lecture-interactive-card" data-lecture-section="sec_nucleus" onclick="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-nucleus').innerHTML;" style="background: #ffffff; border: 1.5px solid #c7d2fe; border-left: 6px solid #6366f1; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #eef2ff; border: 1px solid #c7d2fe; border-radius: 12px; font-size: 11px; font-weight: 600; color: #4f46e5; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #3730a3; font-size: 16px; padding-right: 95px;">🧬 Nucleus (Nhân tế bào)</h4>
        <p style="margin: 0 0 8px 0; font-size: 13.5px; color: #334155; line-height: 1.5;">Contains genetic material (DNA) in chromosomes; controls cell growth, division and protein synthesis.</p>
        <div style="background: #fef3c7; color: #b45309; font-size: 11.5px; font-weight: 700; padding: 4px 8px; border-radius: 4px; display: inline-block;">🔑 Keywords: Contains DNA, controls cell</div>
      </div>

      <!-- SUB-CARD: CELL MEMBRANE -->
      <div id="sec-membrane" class="lecture-interactive-card" data-lecture-section="sec_membrane" onclick="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-membrane').innerHTML;" style="background: #ffffff; border: 1.5px solid #bae6fd; border-left: 6px solid #0284c7; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 12px; font-size: 11px; font-weight: 600; color: #0284c7; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #0369a1; font-size: 16px; padding-right: 95px;">🛡️ Cell Membrane (Màng tế bào)</h4>
        <p style="margin: 0 0 8px 0; font-size: 13.5px; color: #334155; line-height: 1.5;">Partially permeable barrier regulating which substances enter and leave by diffusion, osmosis, active transport.</p>
        <div style="background: #fef3c7; color: #b45309; font-size: 11.5px; font-weight: 700; padding: 4px 8px; border-radius: 4px; display: inline-block;">🔑 Keywords: Partially permeable, controls entry/exit</div>
      </div>

      <!-- SUB-CARD: CYTOPLASM -->
      <div id="sec-cytoplasm" class="lecture-interactive-card" data-lecture-section="sec_cytoplasm" onclick="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-cytoplasm').innerHTML;" style="background: #ffffff; border: 1.5px solid #a5f3fc; border-left: 6px solid #06b6d4; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #ecfeff; border: 1px solid #a5f3fc; border-radius: 12px; font-size: 11px; font-weight: 600; color: #0891b2; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #0e7490; font-size: 16px; padding-right: 95px;">💧 Cytoplasm (Tế bào chất)</h4>
        <p style="margin: 0 0 8px 0; font-size: 13.5px; color: #334155; line-height: 1.5;">Jelly-like fluid containing dissolved substances; the primary site of biochemical reactions and cellular metabolism.</p>
        <div style="background: #fef3c7; color: #b45309; font-size: 11.5px; font-weight: 700; padding: 4px 8px; border-radius: 4px; display: inline-block;">🔑 Keywords: Site of chemical reactions</div>
      </div>

      <!-- SUB-CARD: MITOCHONDRIA -->
      <div id="sec-mitochondria" class="lecture-interactive-card" data-lecture-section="sec_mitochondria" onclick="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-mitochondria').innerHTML;" style="background: #ffffff; border: 1.5px solid #fecaca; border-left: 6px solid #ef4444; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #fef2f2; border: 1px solid #fecaca; border-radius: 12px; font-size: 11px; font-weight: 600; color: #dc2626; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #b91c1c; font-size: 16px; padding-right: 95px;">⚡ Mitochondria (Ti thể)</h4>
        <p style="margin: 0 0 8px 0; font-size: 13.5px; color: #334155; line-height: 1.5;">Powerhouses of the cell; the site of aerobic cellular respiration where energy (ATP) is released.</p>
        <div style="background: #fef3c7; color: #b45309; font-size: 11.5px; font-weight: 700; padding: 4px 8px; border-radius: 4px; display: inline-block;">🔑 Keywords: Aerobic respiration, releases energy</div>
      </div>

      <!-- SUB-CARD: RIBOSOMES -->
      <div id="sec-ribosomes" class="lecture-interactive-card" data-lecture-section="sec_ribosomes" onclick="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-ribosomes').innerHTML;" style="background: #ffffff; border: 1.5px solid #fed7aa; border-left: 6px solid #f97316; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 12px; font-size: 11px; font-weight: 600; color: #ea580c; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #c2410c; font-size: 16px; padding-right: 95px;">🔬 Ribosomes (Ribosome)</h4>
        <p style="margin: 0 0 8px 0; font-size: 13.5px; color: #334155; line-height: 1.5;">Tiny structures in cytoplasm synthesizing polypeptides and proteins by linking amino acids together.</p>
        <div style="background: #fef3c7; color: #b45309; font-size: 11.5px; font-weight: 700; padding: 4px 8px; border-radius: 4px; display: inline-block;">🔑 Keywords: Protein synthesis from amino acids</div>
      </div>

      <!-- SUB-CARD: CELL WALL -->
      <div id="sec-cellwall" class="lecture-interactive-card" data-lecture-section="sec_cellwall" onclick="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-cellwall').innerHTML;" style="background: #ffffff; border: 1.5px solid #bbf7d0; border-left: 6px solid #22c55e; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 12px; font-size: 11px; font-weight: 600; color: #16a34a; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #15803d; font-size: 16px; padding-right: 95px;">🧱 Cell Wall (Thành tế bào)</h4>
        <p style="margin: 0 0 8px 0; font-size: 13.5px; color: #334155; line-height: 1.5;">Rigid outer layer composed of cellulose; provides mechanical strength and prevents osmotic bursting.</p>
        <div style="background: #fef3c7; color: #b45309; font-size: 11.5px; font-weight: 700; padding: 4px 8px; border-radius: 4px; display: inline-block;">🔑 Keywords: Cellulose, support, prevents bursting</div>
      </div>

      <!-- SUB-CARD: CHLOROPLAST -->
      <div id="sec-chloroplast" class="lecture-interactive-card" data-lecture-section="sec_chloroplast" onclick="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-chloroplast').innerHTML;" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 6px solid #10b981; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 12px; font-size: 11px; font-weight: 600; color: #059669; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #047857; font-size: 16px; padding-right: 95px;">🍃 Chloroplast (Lục lạp)</h4>
        <p style="margin: 0 0 8px 0; font-size: 13.5px; color: #334155; line-height: 1.5;">Organelle containing chlorophyll pigments; absorbs light energy to drive glucose synthesis in photosynthesis.</p>
        <div style="background: #fef3c7; color: #b45309; font-size: 11.5px; font-weight: 700; padding: 4px 8px; border-radius: 4px; display: inline-block;">🔑 Keywords: Chlorophyll, absorbs light, photosynthesis</div>
      </div>

      <!-- SUB-CARD: VACUOLE -->
      <div id="sec-vacuole" class="lecture-interactive-card" data-lecture-section="sec_vacuole" onclick="document.getElementById('te-main-info-panel').innerHTML = document.getElementById('data-vacuole').innerHTML;" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-left: 6px solid #3b82f6; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 12px; font-size: 11px; font-weight: 600; color: #2563eb; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #1e40af; font-size: 16px; padding-right: 95px;">💧 Permanent Vacuole (Không bào)</h4>
        <p style="margin: 0 0 8px 0; font-size: 13.5px; color: #334155; line-height: 1.5;">Large central plant cavity filled with cell sap; exerts pressure against cell wall to maintain turgidity.</p>
        <div style="background: #fef3c7; color: #b45309; font-size: 11.5px; font-weight: 700; padding: 4px 8px; border-radius: 4px; display: inline-block;">🔑 Keywords: Cell sap, maintains turgor pressure</div>
      </div>

    </div>

    <!-- HIDDEN ORGANELLE TEMPLATES FOR PANEL UPDATES -->
    <div style="display: none;">
      <div id="data-cytoplasm">
        <h4 style="color: #1d4ed8; margin: 0 0 8px 0; font-size: 18px;">💧 Cytoplasm (Tế bào chất)</h4>
        <p style="margin: 0 0 8px 0; color: #334155; line-height: 1.6; font-size: 14.5px;">Jelly-like fluid containing cell organelles and dissolved substances. It is the site of almost all chemical reactions and cellular metabolism.</p>
        <div style="background-color: #fef3c7; padding: 6px 12px; border-radius: 6px; display: inline-block;"><span style="color: #b45309; font-weight: 700; font-size: 12.5px;">🔑 Keywords: Site of chemical reactions, holds organelles</span></div>
      </div>
      <div id="data-membrane">
        <h4 style="color: #1d4ed8; margin: 0 0 8px 0; font-size: 18px;">🛡️ Cell Membrane (Màng tế bào)</h4>
        <p style="margin: 0 0 8px 0; color: #334155; line-height: 1.6; font-size: 14.5px;">Partially permeable outer barrier that surrounds the cytoplasm. Controls which substances enter and leave the cell by diffusion, osmosis, and active transport.</p>
        <div style="background-color: #fef3c7; padding: 6px 12px; border-radius: 6px; display: inline-block;"><span style="color: #b45309; font-weight: 700; font-size: 12.5px;">🔑 Keywords: Controls entry and exit, partially permeable</span></div>
      </div>
      <div id="data-nucleus">
        <h4 style="color: #1d4ed8; margin: 0 0 8px 0; font-size: 18px;">🧬 Nucleus (Nhân tế bào)</h4>
        <p style="margin: 0 0 8px 0; color: #334155; line-height: 1.6; font-size: 14.5px;">Contains genetic material (DNA) organized into chromosomes. Regulates cell growth, protein synthesis, and cell division.</p>
        <div style="background-color: #fef3c7; padding: 6px 12px; border-radius: 6px; display: inline-block;"><span style="color: #b45309; font-weight: 700; font-size: 12.5px;">🔑 Keywords: Contains genetic material (DNA), controls cell activities</span></div>
      </div>
      <div id="data-mitochondria">
        <h4 style="color: #1d4ed8; margin: 0 0 8px 0; font-size: 18px;">⚡ Mitochondria (Ti thể)</h4>
        <p style="margin: 0 0 8px 0; color: #334155; line-height: 1.6; font-size: 14.5px;">Powerhouses of the cell. The primary site of aerobic respiration where glucose and oxygen are broken down to release energy (ATP).</p>
        <div style="background-color: #fef3c7; padding: 6px 12px; border-radius: 6px; display: inline-block;"><span style="color: #b45309; font-weight: 700; font-size: 12.5px;">🔑 Keywords: Aerobic respiration, releases energy (never say 'creates energy')</span></div>
      </div>
      <div id="data-ribosomes">
        <h4 style="color: #1d4ed8; margin: 0 0 8px 0; font-size: 18px;">🔬 Ribosomes (Ribosome)</h4>
        <p style="margin: 0 0 8px 0; color: #334155; line-height: 1.6; font-size: 14.5px;">Microscopic structures in cytoplasm that carry out protein synthesis, translating genetic instructions to assemble amino acids into polypeptides.</p>
        <div style="background-color: #fef3c7; padding: 6px 12px; border-radius: 6px; display: inline-block;"><span style="color: #b45309; font-weight: 700; font-size: 12.5px;">🔑 Keywords: Protein synthesis from amino acids</span></div>
      </div>
      <div id="data-cellwall">
        <h4 style="color: #1d4ed8; margin: 0 0 8px 0; font-size: 18px;">🧱 Cell Wall (Thành tế bào - Plants Only)</h4>
        <p style="margin: 0 0 8px 0; color: #334155; line-height: 1.6; font-size: 14.5px;">Rigid layer surrounding plant cells, composed of tough cellulose fibres. Provides structural support and prevents osmotic bursting when water enters.</p>
        <div style="background-color: #fef3c7; padding: 6px 12px; border-radius: 6px; display: inline-block;"><span style="color: #b45309; font-weight: 700; font-size: 12.5px;">🔑 Keywords: Cellulose, structural support, prevents bursting</span></div>
      </div>
      <div id="data-chloroplast">
        <h4 style="color: #1d4ed8; margin: 0 0 8px 0; font-size: 18px;">🍃 Chloroplast (Lục lạp - Plants Only)</h4>
        <p style="margin: 0 0 8px 0; color: #334155; line-height: 1.6; font-size: 14.5px;">Organelle containing green chlorophyll pigments. Absorbs light energy and converts it into chemical energy to drive photosynthesis.</p>
        <div style="background-color: #fef3c7; padding: 6px 12px; border-radius: 6px; display: inline-block;"><span style="color: #b45309; font-weight: 700; font-size: 12.5px;">🔑 Keywords: Chlorophyll, absorbs light energy, site of photosynthesis</span></div>
      </div>
      <div id="data-vacuole">
        <h4 style="color: #1d4ed8; margin: 0 0 8px 0; font-size: 18px;">💧 Permanent Vacuole (Không bào trung tâm - Plants Only)</h4>
        <p style="margin: 0 0 8px 0; color: #334155; line-height: 1.6; font-size: 14.5px;">Large central cavity filled with cell sap (solution of water, sugars, and mineral salts). Pushes outward against cytoplasm and cell wall to maintain turgidity.</p>
        <div style="background-color: #fef3c7; padding: 6px 12px; border-radius: 6px; display: inline-block;"><span style="color: #b45309; font-weight: 700; font-size: 12.5px;">🔑 Keywords: Cell sap, maintains turgidity and firmness</span></div>
      </div>
    </div>
  </div>

  <!-- SECTION 3: SPECIALIZED CELLS -->
  <div id="sec-specialised-cells" class="lecture-interactive-card" data-lecture-section="sec_specialised_cells" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe toàn bộ mục 3</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 12px; padding-right: 170px;">
        <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
        <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">3. Specialised Cells & Their Adaptations</h2>
    </div>
    <p style="font-size: 15px; color: #475569; margin-bottom: 20px;">Tế bào biệt hóa cấu trúc để thực hiện chức năng chuyên biệt. Nhấn vào từng loại tế bào để nghe bài giảng chi tiết:</p>

    <!-- SUB-CARDS GRID (6 SPECIALISED CELLS) -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
      
      <!-- SUB-CARD: CILIATED CELL -->
      <div id="sec-cell-ciliated" class="lecture-interactive-card" data-lecture-section="sec_cell_ciliated" style="background: #ffffff; border: 1.5px solid #bae6fd; border-left: 5px solid #0284c7; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 12px; font-size: 11px; font-weight: 600; color: #0284c7; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #0369a1; font-size: 16px; padding-right: 95px;">🍃 Ciliated Cell</h4>
        <p style="margin: 0 0 6px 0; font-size: 13px; color: #64748b;"><strong>Location:</strong> Trachea & bronchi.</p>
        <p style="margin: 0; font-size: 13px; color: #334155;"><strong>Adaptation:</strong> Covered with microscopic hair-like cilia that beat rhythmically to sweep mucus containing trapped dust and microbes away from the lungs.</p>
      </div>

      <!-- SUB-CARD: ROOT HAIR CELL -->
      <div id="sec-cell-roothair" class="lecture-interactive-card" data-lecture-section="sec_cell_roothair" style="background: #ffffff; border: 1.5px solid #bbf7d0; border-left: 5px solid #16a34a; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 12px; font-size: 11px; font-weight: 600; color: #16a34a; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #15803d; font-size: 16px; padding-right: 95px;">🌱 Root Hair Cell</h4>
        <p style="margin: 0 0 6px 0; font-size: 13px; color: #64748b;"><strong>Location:</strong> Root epidermis.</p>
        <p style="margin: 0; font-size: 13px; color: #334155;"><strong>Adaptation:</strong> Long slender extension provides a huge surface-area-to-volume ratio for rapid absorption of water (osmosis) and mineral ions (active transport).</p>
      </div>

      <!-- SUB-CARD: XYLEM VESSEL -->
      <div id="sec-cell-xylem" class="lecture-interactive-card" data-lecture-section="sec_cell_xylem" style="background: #ffffff; border: 1.5px solid #fed7aa; border-left: 5px solid #d97706; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #fffbeb; border: 1px solid #fed7aa; border-radius: 12px; font-size: 11px; font-weight: 600; color: #d97706; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #b45309; font-size: 16px; padding-right: 95px;">🪵 Xylem Vessel</h4>
        <p style="margin: 0 0 6px 0; font-size: 13px; color: #64748b;"><strong>Location:</strong> Stems, roots, leaves.</p>
        <p style="margin: 0; font-size: 13px; color: #334155;"><strong>Adaptation:</strong> Dead hollow tubes with no end walls, reinforced with waterproof lignin; transports water/ions under tension and provides mechanical support.</p>
      </div>

      <!-- SUB-CARD: PALISADE MESOPHYLL -->
      <div id="sec-cell-palisade" class="lecture-interactive-card" data-lecture-section="sec_cell_palisade" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-left: 5px solid #10b981; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 12px; font-size: 11px; font-weight: 600; color: #059669; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #047857; font-size: 16px; padding-right: 95px;">☀️ Palisade Mesophyll Cell</h4>
        <p style="margin: 0 0 6px 0; font-size: 13px; color: #64748b;"><strong>Location:</strong> Upper layer of leaves.</p>
        <p style="margin: 0; font-size: 13px; color: #334155;"><strong>Adaptation:</strong> Columnar, vertically packed with abundant chloroplasts to capture maximum sunlight for photosynthesis.</p>
      </div>

      <!-- SUB-CARD: RED BLOOD CELL -->
      <div id="sec-cell-rbc" class="lecture-interactive-card" data-lecture-section="sec_cell_rbc" style="background: #ffffff; border: 1.5px solid #fecaca; border-left: 5px solid #ef4444; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #fef2f2; border: 1px solid #fecaca; border-radius: 12px; font-size: 11px; font-weight: 600; color: #dc2626; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #b91c1c; font-size: 16px; padding-right: 95px;">🩸 Red Blood Cell (Erythrocyte)</h4>
        <p style="margin: 0 0 6px 0; font-size: 13px; color: #64748b;"><strong>Location:</strong> Bloodstream.</p>
        <p style="margin: 0; font-size: 13px; color: #334155;"><strong>Adaptation:</strong> Biconcave disc shape increases surface area; contains haemoglobin; lacks a nucleus to maximize oxygen storage space.</p>
      </div>

      <!-- SUB-CARD: NEURONE -->
      <div id="sec-cell-neurone" class="lecture-interactive-card" data-lecture-section="sec_cell_neurone" style="background: #ffffff; border: 1.5px solid #ddd6fe; border-left: 5px solid #8b5cf6; border-radius: 10px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
        <div style="position: absolute; top: 12px; right: 12px; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 12px; font-size: 11px; font-weight: 600; color: #7c3aed; pointer-events: none;">🎧 Nghe mục này</div>
        <h4 style="margin: 0 0 6px 0; color: #6d28d9; font-size: 16px; padding-right: 95px;">⚡ Neurone (Nerve Cell)</h4>
        <p style="margin: 0 0 6px 0; font-size: 13px; color: #64748b;"><strong>Location:</strong> Nervous system.</p>
        <p style="margin: 0; font-size: 13px; color: #334155;"><strong>Adaptation:</strong> Long axon carries electrical impulses over long distances; myelin sheath provides electrical insulation and speeds transmission.</p>
      </div>

    </div>
  </div>

  <!-- SECTION 4: MAGNIFICATION FORMULA -->
  <div id="sec-magnification" class="lecture-interactive-card" data-lecture-section="sec_magnification" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">
    <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 20px; font-size: 12px; font-weight: 600; color: #059669; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #a7f3d0; padding-bottom: 12px; padding-right: 140px;">
        <span style="background: #dbeafe; color: #1e40af; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟦 CORE</span>
        <span style="background: #dcfce7; color: #166534; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🟩 SUPPLEMENT</span>
        <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">4. Specimen Calculations: The Magnification Formula (I = A × M)</h2>
    </div>

    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 22px; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; align-items: center;">
        
        <div style="background: #ffffff; border: 2px solid #3b82f6; border-radius: 10px; padding: 20px; text-align: center;">
          <div style="font-size: 28px; font-weight: 800; color: #1e40af; margin-bottom: 8px; letter-spacing: 1px;">
            <i>I</i> = <i>A</i> × <i>M</i>
          </div>
          <div style="font-size: 14px; color: #475569; line-height: 1.6;">
            Magnification = Image size ÷ Actual size<br/>
            Actual size = Image size ÷ Magnification
          </div>
        </div>

        <div>
          <h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 15px;">Golden Rules for Cambridge Calculations:</h4>
          <ul style="margin: 0; padding-left: 18px; font-size: 13.5px; color: #334155; line-height: 1.75;">
            <li>Always measure the image size (<i>I</i>) in <strong>millimetres (mm)</strong> using a ruler.</li>
            <li><strong style="color: #166534;">Unit Conversion (Supplement):</strong> 1 mm = 1000 µm.
              <br/>• To convert mm → µm: <strong>Multiply by 1000</strong>.
              <br/>• To convert µm → mm: <strong>Divide by 1000</strong>.
            </li>
            <li>Ensure <i>I</i> and <i>A</i> have the same units before calculating <i>M</i>. Magnification has <strong>no units</strong> (e.g. × 400).</li>
          </ul>
        </div>

      </div>
    </div>
  </div>

</div>"""

def verify_html(code, html, manifest_path):
    print(f"\n=== VERIFYING {code} HTML ===")
    
    # 1. Div balance
    opens = len(re.findall(r'<div\b[^>]*>', html, flags=re.IGNORECASE))
    closes = len(re.findall(r'</div>', html, flags=re.IGNORECASE))
    diff = opens - closes
    print(f"Div balance: opens={opens}, closes={closes}, diff={diff}")
    assert diff == 0, f"Error: div diff is {diff}!"
    
    # 2. Check no study resources
    has_sr = 'Tài liệu học tập' in html or 'Study Resource' in html or 'Paper 2' in html and 'Textbook' in html
    print(f"Has study resources: {has_sr} (expected False)")
    assert not has_sr, "Error: study resources still present!"
    
    # 3. Check against manifest
    with open(manifest_path, 'r', encoding='utf-8') as f:
        mf = json.load(f)
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Check no h2 cards
    h2_cards = [h for h in soup.find_all('h2') if 'lecture-interactive-card' in h.get('class', [])]
    print(f"H2 cards: {len(h2_cards)} (expected 0)")
    assert len(h2_cards) == 0, "Error: found H2 elements with lecture-interactive-card!"
    
    # Check each segment selector
    missing = []
    for seg in mf['segments']:
        sel = seg['selector']
        elems = soup.select(sel)
        if not elems:
            missing.append((seg['id'], sel))
        else:
            # check that at least one matching element has lecture-interactive-card
            has_card = any('lecture-interactive-card' in el.get('class', []) for el in elems)
            if not has_card:
                print(f"  Warning: selector {sel} for {seg['id']} matched {len(elems)} elements, but none have class 'lecture-interactive-card'")
                
    if missing:
        print(f"❌ Missing selectors: {missing}")
        assert False, f"Missing selectors: {missing}"
    else:
        print(f"✅ All {len(mf['segments'])} segment selectors exist in HTML and match perfectly!")
        
    # Write to file
    out_file = f"scripts/raw_science_bio/{code.lower()}_p1_transformed.html"
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved to {out_file}")

verify_html("B1", b1_html, "public/audio/lectures/science/b1/manifest.json")
verify_html("B2", b2_html, "public/audio/lectures/science/b2/manifest.json")

print("\n🎉 ALL HTML FILES VERIFIED 100% PERFECT!")
