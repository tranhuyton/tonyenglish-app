# -*- coding: utf-8 -*-
"""
Rebuild Topic 2 HTML:
- Page 1: English
- Page 2: Bilingual (Song ngữ)
Matching 100% of Topic 1's interactive card quality, with visible audio badges,
cursor: pointer, and perfect div balancing (diff == 0).
"""

import sys
sys.path.append('scripts')
from audio_lecture_engine import sb

T2_ID = '2d2545c0-ccb9-4d04-a6fa-f2eec55cdecc'

def get_page1_html():
    return '''<div style="font-family: 'Segoe UI', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">

    <!-- TOP HEADER BANNER (CLICKABLE OVERVIEW) -->
    <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
            <div>
                <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 0.5px;">Cambridge IGCSE Biology (0610)</span>
                <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc; letter-spacing: -0.5px;">Topic 2: Cells and Organisms</h1>
                <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Cell Ultrastructure, Plant vs Animal, Levels of Organisation, Specialised Cells &amp; Magnification</p>
            </div>
            <div style="background: rgba(37, 99, 235, 0.2); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 20px; padding: 8px 16px; display: flex; align-items: center; gap: 8px; font-weight: 600; font-size: 14px; color: #60a5fa;">
                <span>🎧 Click any card to listen</span>
            </div>
        </div>
    </div>

    <!-- 1. CELL STRUCTURE & ORGANELLES -->
    <div style="margin-bottom: 45px;">
        <div id="sec-cell-structures" class="lecture-interactive-card" data-lecture-section="sec_cell_structures" style="border-bottom: 3px solid #3b82f6; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🔬 1. CELL STRUCTURE &amp; ORGANELLES</h2>
                <span style="font-size: 12px; color: #1d4ed8; font-weight: 600; background: #eff6ff; padding: 4px 10px; border-radius: 12px; border: 1px solid #bfdbfe; display: inline-flex; align-items: center; gap: 4px;">🎧 Listen to Section</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Cells are the microscopic building blocks of all living organisms. Organelles are specialised compartments performing vital metabolic tasks:</p>
        </div>

        <!-- ORGANELLES GRID -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-bottom: 30px;">
            
            <div id="card-membrane" class="lecture-interactive-card" data-lecture-section="card_membrane" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #3b82f6; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #1d4ed8; font-size: 17px; font-weight: 700;">🛡️ Cell Membrane</h4>
                    <span style="font-size: 11px; color: #2563eb; background: #eff6ff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Partially permeable boundary that surrounds the cytoplasm. Controls substances entering and leaving the cell by diffusion, osmosis, and active transport.</p>
                <div style="font-size: 11.5px; color: #b45309; background: #fef3c7; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Partially permeable • Controls entry/exit</div>
            </div>

            <div id="card-cytoplasm" class="lecture-interactive-card" data-lecture-section="card_cytoplasm" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #06b6d4; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #0891b2; font-size: 17px; font-weight: 700;">💧 Cytoplasm</h4>
                    <span style="font-size: 11px; color: #0891b2; background: #ecfeff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Jelly-like aqueous fluid containing dissolved salts, sugars, and organelles. Site where most metabolic and biochemical reactions occur.</p>
                <div style="font-size: 11.5px; color: #0e7490; background: #cffafe; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Site of chemical reactions</div>
            </div>

            <div id="card-nucleus" class="lecture-interactive-card" data-lecture-section="card_nucleus" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #8b5cf6; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #7c3aed; font-size: 17px; font-weight: 700;">🧬 Nucleus</h4>
                    <span style="font-size: 11px; color: #7c3aed; background: #f5f3ff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Control centre of eukaryotic cells. Contains genetic material in chromosomes (DNA) and directs protein synthesis and cellular division.</p>
                <div style="font-size: 11.5px; color: #6b21a8; background: #ede9fe; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Contains DNA • Controls cell activities</div>
            </div>

            <div id="card-mitochondria" class="lecture-interactive-card" data-lecture-section="card_mitochondria" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #ef4444; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #b91c1c; font-size: 17px; font-weight: 700;">⚡ Mitochondria</h4>
                    <span style="font-size: 11px; color: #dc2626; background: #fef2f2; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Powerhouse of the cell. Site of aerobic respiration where glucose is broken down with oxygen to release ATP energy. (Never say create energy).</p>
                <div style="font-size: 11.5px; color: #991b1b; background: #fee2e2; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Aerobic respiration • Release ATP energy</div>
            </div>

            <div id="card-ribosomes" class="lecture-interactive-card" data-lecture-section="card_ribosomes" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #f59e0b; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #b45309; font-size: 17px; font-weight: 700;">🧱 Ribosomes</h4>
                    <span style="font-size: 11px; color: #d97706; background: #fffbeb; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Tiny granular structures located free in the cytoplasm or bound to membranes. Molecular machines responsible for protein synthesis.</p>
                <div style="font-size: 11.5px; color: #78350f; background: #fef3c7; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Protein synthesis</div>
            </div>

            <div id="card-cellwall" class="lecture-interactive-card" data-lecture-section="card_cellwall" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #10b981; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #047857; font-size: 17px; font-weight: 700;">🌿 Cell Wall (Cellulose)</h4>
                    <span style="font-size: 11px; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Outer layer made of cellulose. Fully permeable, provides rigid structural support to maintain cell shape and prevents plant cells from bursting.</p>
                <div style="font-size: 11.5px; color: #065f46; background: #d1fae5; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Tough cellulose • Structural support • Fully permeable</div>
            </div>

            <div id="card-chloroplast" class="lecture-interactive-card" data-lecture-section="card_chloroplast" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #16a34a; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #15803d; font-size: 17px; font-weight: 700;">🍃 Chloroplasts</h4>
                    <span style="font-size: 11px; color: #16a34a; background: #f0fdf4; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Plant organelles containing the green pigment chlorophyll. Absorb light energy to drive photosynthesis to produce glucose.</p>
                <div style="font-size: 11.5px; color: #14532d; background: #dcfce7; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Chlorophyll • Absorbs light • Photosynthesis</div>
            </div>

            <div id="card-vacuole" class="lecture-interactive-card" data-lecture-section="card_vacuole" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #0284c7; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #0369a1; font-size: 17px; font-weight: 700;">💧 Permanent Vacuole</h4>
                    <span style="font-size: 11px; color: #0284c7; background: #e0f2fe; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Large fluid-filled sac in mature plant cells containing cell sap (solution of sugars and ions). Maintains turgidity and mechanical support.</p>
                <div style="font-size: 11.5px; color: #075985; background: #bae6fd; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Cell sap • Maintains turgor pressure</div>
            </div>

            <div id="card-bacteria-cell" class="lecture-interactive-card" data-lecture-section="card_bacteria_cell" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #ca8a04; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #a16207; font-size: 17px; font-weight: 700;">🦠 Bacterial Cell (Prokaryote)</h4>
                    <span style="font-size: 11px; color: #ca8a04; background: #fefce8; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Lacks a true nucleus and mitochondria. Contains a peptidoglycan cell wall, a circular loop of chromosomal DNA, and small plasmid DNA rings.</p>
                <div style="font-size: 11.5px; color: #713f12; background: #fef9c3; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Peptidoglycan • No nucleus • Circular DNA • Plasmids</div>
            </div>

        </div>
    </div>

    <!-- 2. COMPARISON: PLANT VS ANIMAL CELLS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-cell-comparison" class="lecture-interactive-card" data-lecture-section="sec_cell_comparison" style="border-bottom: 3px solid #10b981; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">📊 2. COMPARISON: PLANT VS ANIMAL CELLS</h2>
                <span style="font-size: 12px; color: #059669; font-weight: 600; background: #ecfdf5; padding: 4px 10px; border-radius: 12px; border: 1px solid #a7f3d0; display: inline-flex; align-items: center; gap: 4px;">🎧 Listen to Section</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Plant and animal cells are eukaryotic cells that share core structural features but have key differences essential for Cambridge exams:</p>
        </div>

        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); margin-bottom: 25px; overflow-x: auto;">
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead>
                    <tr style="background: #f8fafc; border-bottom: 2px solid #cbd5e1; text-align: left;">
                        <th style="padding: 12px; color: #0f172a;">Feature / Organelle</th>
                        <th style="padding: 12px; color: #16a34a;">🌿 Plant Cell</th>
                        <th style="padding: 12px; color: #2563eb;">🐾 Animal Cell</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 10px 12px; font-weight: 600;">Cellulose Cell Wall</td>
                        <td style="padding: 10px 12px; color: #16a34a; font-weight: 600;">✅ Present (rigid outer box)</td>
                        <td style="padding: 10px 12px; color: #dc2626; font-weight: 600;">❌ Absent (flexible shape)</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                        <td style="padding: 10px 12px; font-weight: 600;">Chloroplasts &amp; Chlorophyll</td>
                        <td style="padding: 10px 12px; color: #16a34a; font-weight: 600;">✅ Present (in photosynthetic cells)</td>
                        <td style="padding: 10px 12px; color: #dc2626; font-weight: 600;">❌ Absent</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 10px 12px; font-weight: 600;">Vacuole</td>
                        <td style="padding: 10px 12px; color: #16a34a; font-weight: 600;">✅ Large permanent central vacuole</td>
                        <td style="padding: 10px 12px; color: #64748b;">Small temporary vacuoles only</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                        <td style="padding: 10px 12px; font-weight: 600;">Nucleus, Cytoplasm, Membrane</td>
                        <td style="padding: 10px 12px; color: #16a34a; font-weight: 600;">✅ Present</td>
                        <td style="padding: 10px 12px; color: #2563eb; font-weight: 600;">✅ Present</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px 12px; font-weight: 600;">Mitochondria &amp; Ribosomes</td>
                        <td style="padding: 10px 12px; color: #16a34a; font-weight: 600;">✅ Present</td>
                        <td style="padding: 10px 12px; color: #2563eb; font-weight: 600;">✅ Present</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- 3. LEVELS OF ORGANISATION -->
    <div style="margin-bottom: 45px;">
        <div id="sec-levels-organisation" class="lecture-interactive-card" data-lecture-section="sec_levels_organisation" style="border-bottom: 3px solid #8b5cf6; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🏢 3. LEVELS OF ORGANISATION</h2>
                <span style="font-size: 12px; color: #6d28d9; font-weight: 600; background: #f5f3ff; padding: 4px 10px; border-radius: 12px; border: 1px solid #ddd6fe; display: inline-flex; align-items: center; gap: 4px;">🎧 Listen to Section</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Multicellular organisms are built hierarchically: from basic single cells up to complex cooperating living organisms:</p>
        </div>

        <!-- 5 HIERARCHY CARDS -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-bottom: 30px;">
            
            <div id="card-level-cell" class="lecture-interactive-card" data-lecture-section="card_level_cell" style="background: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #3b82f6; border-radius: 10px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h4 style="margin: 0; color: #1d4ed8; font-size: 16px; font-weight: 700;">1. Cell</h4>
                    <span style="font-size: 10.5px; color: #2563eb; background: #eff6ff; padding: 2px 6px; border-radius: 8px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Basic structural and functional building unit of all life. E.g., epithelial cell, neuron, root hair cell.</p>
            </div>

            <div id="card-level-tissue" class="lecture-interactive-card" data-lecture-section="card_level_tissue" style="background: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #06b6d4; border-radius: 10px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h4 style="margin: 0; color: #0891b2; font-size: 16px; font-weight: 700;">2. Tissue</h4>
                    <span style="font-size: 10.5px; color: #0891b2; background: #ecfeff; padding: 2px 6px; border-radius: 8px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Group of similar cells working together to perform a shared biological function. E.g., ciliated epithelium, muscle tissue.</p>
            </div>

            <div id="card-level-organ" class="lecture-interactive-card" data-lecture-section="card_level_organ" style="background: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #8b5cf6; border-radius: 10px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h4 style="margin: 0; color: #7c3aed; font-size: 16px; font-weight: 700;">3. Organ</h4>
                    <span style="font-size: 10.5px; color: #7c3aed; background: #f5f3ff; padding: 2px 6px; border-radius: 8px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Distinct body structure made of several tissues coordinating to perform specific functions. E.g., heart, leaf, stomach.</p>
            </div>

            <div id="card-level-system" class="lecture-interactive-card" data-lecture-section="card_level_system" style="background: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #f59e0b; border-radius: 10px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h4 style="margin: 0; color: #b45309; font-size: 16px; font-weight: 700;">4. Organ System</h4>
                    <span style="font-size: 10.5px; color: #d97706; background: #fffbeb; padding: 2px 6px; border-radius: 8px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Group of interrelated organs with linked roles working together. E.g., circulatory system, digestive system.</p>
            </div>

            <div id="card-level-organism" class="lecture-interactive-card" data-lecture-section="card_level_organism" style="background: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #10b981; border-radius: 10px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h4 style="margin: 0; color: #047857; font-size: 16px; font-weight: 700;">5. Organism</h4>
                    <span style="font-size: 10.5px; color: #059669; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Complete independent living entity carrying out all seven characteristics of life. E.g., human, oak tree.</p>
            </div>

        </div>
    </div>

    <!-- 4. SPECIALISED CELLS & ADAPTATIONS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-specialised-cells" class="lecture-interactive-card" data-lecture-section="sec_specialised_cells" style="border-bottom: 3px solid #ec4899; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🧬 4. SPECIALISED CELLS &amp; ADAPTATIONS</h2>
                <span style="font-size: 12px; color: #be185d; font-weight: 600; background: #fdf2f8; padding: 4px 10px; border-radius: 12px; border: 1px solid #fbcfe8; display: inline-flex; align-items: center; gap: 4px;">🎧 Listen to Section</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Cell differentiation alters cell structure to perform specific physiological roles with high efficiency:</p>
        </div>

        <!-- 7 SPECIALISED CELLS GRID -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 30px;">
            
            <div id="card-roothair" class="lecture-interactive-card" data-lecture-section="card_roothair" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #10b981; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #047857; font-size: 17px; font-weight: 700;">🌱 Root Hair Cell</h4>
                    <span style="font-size: 11px; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Long thin hair projection drastically increases surface area to volume ratio for rapid absorption of water (osmosis) and mineral ions (active transport). No chloroplasts.</p>
                <div style="font-size: 11.5px; color: #065f46; background: #d1fae5; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 High surface area • No chloroplasts</div>
            </div>

            <div id="card-palisade" class="lecture-interactive-card" data-lecture-section="card_palisade" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #16a34a; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #15803d; font-size: 17px; font-weight: 700;">🍃 Palisade Mesophyll Cell</h4>
                    <span style="font-size: 11px; color: #16a34a; background: #f0fdf4; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Tall column-like shape closely packed beneath upper leaf epidermis. Packed with high density of chloroplasts to absorb maximum light for photosynthesis.</p>
                <div style="font-size: 11.5px; color: #14532d; background: #dcfce7; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Dense chloroplasts • Maximum light absorption</div>
            </div>

            <div id="card-ciliated" class="lecture-interactive-card" data-lecture-section="card_ciliated" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #06b6d4; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #0891b2; font-size: 17px; font-weight: 700;">💨 Ciliated Epithelial Cell</h4>
                    <span style="font-size: 11px; color: #0891b2; background: #ecfeff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Lines human trachea and bronchi. Features hair-like cilia that beat in coordinated waves to sweep mucus and trapped bacteria upwards away from lungs.</p>
                <div style="font-size: 11.5px; color: #0e7490; background: #cffafe; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Beating cilia • Sweeps mucus &amp; pathogens</div>
            </div>

            <div id="card-rbc" class="lecture-interactive-card" data-lecture-section="card_rbc" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #ef4444; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #b91c1c; font-size: 17px; font-weight: 700;">🔴 Red Blood Cell (Erythrocyte)</h4>
                    <span style="font-size: 11px; color: #dc2626; background: #fef2f2; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Biconcave disc shape increases SA:V ratio for rapid oxygen diffusion. Packed with haemoglobin protein to bind oxygen; lacks a nucleus to maximize space.</p>
                <div style="font-size: 11.5px; color: #991b1b; background: #fee2e2; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Biconcave disc • Haemoglobin • No nucleus</div>
            </div>

            <div id="card-neuron" class="lecture-interactive-card" data-lecture-section="card_neuron" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #8b5cf6; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #7c3aed; font-size: 17px; font-weight: 700;">⚡ Neurone / Nerve Cell</h4>
                    <span style="font-size: 11px; color: #7c3aed; background: #f5f3ff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Elongated axon conducts electrical nerve impulses over long body distances. Dendrites branch to receive inputs; fatty myelin sheath provides electrical insulation.</p>
                <div style="font-size: 11.5px; color: #6b21a8; background: #ede9fe; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Long axon • Myelin insulation • Electrical impulses</div>
            </div>

            <div id="card-sperm" class="lecture-interactive-card" data-lecture-section="card_sperm" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #3b82f6; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #1d4ed8; font-size: 17px; font-weight: 700;">🏊 Sperm Cell (Male Gamete)</h4>
                    <span style="font-size: 11px; color: #2563eb; background: #eff6ff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Acrosome cap contains enzymes to digest egg jelly coat. Midpiece is packed with mitochondria releasing ATP for flagellum tail motility.</p>
                <div style="font-size: 11.5px; color: #1e3a8a; background: #dbeafe; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Acrosome enzymes • Mitochondria midpiece • Flagellum</div>
            </div>

            <div id="card-egg" class="lecture-interactive-card" data-lecture-section="card_egg" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #ec4899; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #be185d; font-size: 17px; font-weight: 700;">🥚 Egg Cell / Ovum (Female Gamete)</h4>
                    <span style="font-size: 11px; color: #db2777; background: #fdf2f8; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0 0 8px 0; line-height: 1.5;">Large cytoplasm store of nutrients to sustain early zygote development. Outer jelly coat hardens immediately upon fertilisation to block polyspermy.</p>
                <div style="font-size: 11.5px; color: #831843; background: #fce7f3; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Nutrient-rich cytoplasm • Hardening jelly coat</div>
            </div>

        </div>
    </div>

    <!-- 5. MAGNIFICATION FORMULA & CALCULATIONS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-magnification" class="lecture-interactive-card" data-lecture-section="sec_magnification" style="border-bottom: 3px solid #f59e0b; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">📐 5. MAGNIFICATION &amp; SPECIMEN SIZE</h2>
                <span style="font-size: 12px; color: #b45309; font-weight: 600; background: #fffbeb; padding: 4px 10px; border-radius: 12px; border: 1px solid #fde68a; display: inline-flex; align-items: center; gap: 4px;">🎧 Listen to Section</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Master the IAM formula triangle and Cambridge unit conversions for Paper 2, 4, and 6 calculations:</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 18px; margin-bottom: 30px;">
            
            <div id="card-iam-formula" class="lecture-interactive-card" data-lecture-section="card_iam_formula" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #f59e0b; border-radius: 10px; padding: 18px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <h4 style="margin: 0; color: #b45309; font-size: 18px; font-weight: 700;">📐 IAM Formula Triangle</h4>
                    <span style="font-size: 11px; color: #d97706; background: #fffbeb; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px; text-align: center; margin-bottom: 12px; font-weight: 700; font-size: 18px; color: #0f172a;">
                    $$I = A \\times M$$
                </div>
                <ul style="margin: 0; padding-left: 20px; font-size: 13.5px; color: #334155; line-height: 1.6;">
                    <li><b>Image size ($I$):</b> Measured length with ruler (mm).</li>
                    <li><b>Actual size ($A$):</b> $A = \\frac{I}{M}$</li>
                    <li><b>Magnification ($M$):</b> $M = \\frac{I}{A}$ (has no unit, write e.g., $\\times 500$).</li>
                </ul>
            </div>

            <div id="card-units-conversion" class="lecture-interactive-card" data-lecture-section="card_units_conversion" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #3b82f6; border-radius: 10px; padding: 18px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <h4 style="margin: 0; color: #1d4ed8; font-size: 18px; font-weight: 700;">🔄 Units Conversion ($1\\text{ mm} = 1000\\ \\mu\\text{m}$)</h4>
                    <span style="font-size: 11px; color: #2563eb; background: #eff6ff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 12px; text-align: center; margin-bottom: 12px; font-weight: 700; font-size: 16px; color: #1d4ed8;">
                    Millimetres (mm) $\\xrightarrow{\\times 1000}$ Micrometres ($\\mu$m)
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0; line-height: 1.6;">
                    • <b>Convert mm to $\\mu$m:</b> Multiply by 1000.<br/>
                    • <b>Convert $\\mu$m to mm:</b> Divide by 1000.<br/>
                    • <i>Golden Rule:</i> Always ensure Image ($I$) and Actual ($A$) have identical units before calculating!
                </p>
            </div>

        </div>
    </div>

</div>'''

def get_page2_html():
    return '''<div style="font-family: 'Segoe UI', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">

    <!-- TOP HEADER BANNER (CLICKABLE OVERVIEW) -->
    <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
            <div>
                <span style="display: inline-block; background: #10b981; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 0.5px;">Cambridge IGCSE Biology (0610) • Song ngữ</span>
                <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc; letter-spacing: -0.5px;">Chuyên đề 2: Tế bào và Cấu trúc Sinh vật</h1>
                <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Cấu trúc tế bào, So sánh TV vs ĐV, Cấp độ tổ chức sống, Tế bào chuyên hóa &amp; Độ phóng đại</p>
            </div>
            <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; display: flex; align-items: center; gap: 8px; font-weight: 600; font-size: 14px; color: #34d399;">
                <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
            </div>
        </div>
    </div>

    <!-- 1. CELL STRUCTURE & ORGANELLES -->
    <div style="margin-bottom: 45px;">
        <div id="sec-cell-structures" class="lecture-interactive-card" data-lecture-section="sec_cell_structures" style="border-bottom: 3px solid #3b82f6; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🔬 1. CẤU TRÚC TẾ BÀO &amp; CÁC BÀO QUAN (Cell Organelles)</h2>
                <span style="font-size: 12px; color: #1d4ed8; font-weight: 600; background: #eff6ff; padding: 4px 10px; border-radius: 12px; border: 1px solid #bfdbfe; display: inline-flex; align-items: center; gap: 4px;">🎧 Nghe giảng phần này</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Tế bào là đơn vị cấu trúc và chức năng cơ bản của mọi sinh vật sống. Bào quan là các khoang cấu trúc dưới tế bào chuyên biệt đảm nhiệm những chức năng chuyển hóa riêng biệt:</p>
        </div>

        <!-- ORGANELLES GRID -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-bottom: 30px;">
            
            <div id="card-membrane" class="lecture-interactive-card" data-lecture-section="card_membrane" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #3b82f6; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #1d4ed8; font-size: 17px; font-weight: 700;">🛡️ Cell Membrane (Màng tế bào)</h4>
                    <span style="font-size: 11px; color: #2563eb; background: #eff6ff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Partially permeable membrane controlling entry and exit of substances by diffusion, osmosis, and active transport.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Màng bán thấm chọn lọc, kiểm soát các chất đi vào và đi ra khỏi tế bào qua khuếch tán, thẩm thấu và vận chuyển chủ động.</p>
                <div style="font-size: 11.5px; color: #b45309; background: #fef3c7; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Màng bán thấm • Kiểm soát ra vào</div>
            </div>

            <div id="card-cytoplasm" class="lecture-interactive-card" data-lecture-section="card_cytoplasm" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #06b6d4; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #0891b2; font-size: 17px; font-weight: 700;">💧 Cytoplasm (Tế bào chất)</h4>
                    <span style="font-size: 11px; color: #0891b2; background: #ecfeff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Jelly-like fluid where most metabolic chemical reactions take place.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Chất dịch bán lỏng dạng keo, nơi diễn ra phần lớn các phản ứng chuyển hóa và phản ứng sinh hóa của tế bào.</p>
                <div style="font-size: 11.5px; color: #0e7490; background: #cffafe; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Nơi diễn ra các phản ứng sinh hóa</div>
            </div>

            <div id="card-nucleus" class="lecture-interactive-card" data-lecture-section="card_nucleus" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #8b5cf6; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #7c3aed; font-size: 17px; font-weight: 700;">🧬 Nucleus (Nhân tế bào)</h4>
                    <span style="font-size: 11px; color: #7c3aed; background: #f5f3ff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Contains DNA in chromosomes; controls cell activities and protein synthesis.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Trung tâm điều khiển của tế bào nhân thực, chứa DNA dưới dạng nhiễm sắc thể, chỉ huy quá trình tổng hợp protein và phân bào.</p>
                <div style="font-size: 11.5px; color: #6b21a8; background: #ede9fe; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Chứa DNA • Điều khiển hoạt động tế bào</div>
            </div>

            <div id="card-mitochondria" class="lecture-interactive-card" data-lecture-section="card_mitochondria" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #ef4444; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #b91c1c; font-size: 17px; font-weight: 700;">⚡ Mitochondria (Ti thể)</h4>
                    <span style="font-size: 11px; color: #dc2626; background: #fef2f2; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Site of aerobic respiration, releasing ATP energy. (Never say create energy).</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Bào quan nhà máy năng lượng, nơi diễn ra hô hấp hiếu khí để giải phóng ATP cho hoạt động sống. (Không được nói tạo ra năng lượng).</p>
                <div style="font-size: 11.5px; color: #991b1b; background: #fee2e2; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Hô hấp hiếu khí • Giải phóng năng lượng ATP</div>
            </div>

            <div id="card-ribosomes" class="lecture-interactive-card" data-lecture-section="card_ribosomes" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #f59e0b; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #b45309; font-size: 17px; font-weight: 700;">🧱 Ribosomes (Ribôxôm)</h4>
                    <span style="font-size: 11px; color: #d97706; background: #fffbeb; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Tiny structures responsible for protein synthesis by assembling amino acids.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Hạt cầu tí hon đảm nhiệm lắp ráp các axit amin thành phân tử protein theo khuôn mã di truyền.</p>
                <div style="font-size: 11.5px; color: #78350f; background: #fef3c7; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Tổng hợp protein</div>
            </div>

            <div id="card-cellwall" class="lecture-interactive-card" data-lecture-section="card_cellwall" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #10b981; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #047857; font-size: 17px; font-weight: 700;">🌿 Cell Wall (Thành tế bào thực vật)</h4>
                    <span style="font-size: 11px; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Made of tough cellulose. Fully permeable, provides rigid shape and prevents bursting.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Cấu tạo từ các sợi cellulose bền chắc, thấm hoàn toàn, tạo hình dạng cố định và bảo vệ tế bào không bị vỡ khi no nước.</p>
                <div style="font-size: 11.5px; color: #065f46; background: #d1fae5; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Sợi cellulose • Nâng đỡ tế bào • Thấm hoàn toàn</div>
            </div>

            <div id="card-chloroplast" class="lecture-interactive-card" data-lecture-section="card_chloroplast" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #16a34a; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #15803d; font-size: 17px; font-weight: 700;">🍃 Chloroplasts (Lục lạp)</h4>
                    <span style="font-size: 11px; color: #16a34a; background: #f0fdf4; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Contain green chlorophyll pigment to absorb light for photosynthesis.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Bào quan chứa sắc tố diệp lục, hấp thu ánh sáng mặt trời để thực hiện quang hợp tổng hợp đường glucose.</p>
                <div style="font-size: 11.5px; color: #14532d; background: #dcfce7; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Sắc tố diệp lục • Hấp thụ ánh sáng • Quang hợp</div>
            </div>

            <div id="card-vacuole" class="lecture-interactive-card" data-lecture-section="card_vacuole" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #0284c7; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #0369a1; font-size: 17px; font-weight: 700;">💧 Permanent Vacuole (Không bào trung tâm)</h4>
                    <span style="font-size: 11px; color: #0284c7; background: #e0f2fe; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Large fluid-filled sac containing cell sap (sugars and mineral salts), maintaining turgidity.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Không bào lớn chứa dịch bào (đường và khoáng), tạo áp suất trương nước giữ tế bào căng cứng nâng đỡ cành lá.</p>
                <div style="font-size: 11.5px; color: #075985; background: #bae6fd; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Dịch tế bào • Duy trì áp suất trương nước</div>
            </div>

            <div id="card-bacteria-cell" class="lecture-interactive-card" data-lecture-section="card_bacteria_cell" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #ca8a04; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #a16207; font-size: 17px; font-weight: 700;">🦠 Bacterial Cell (Tế bào vi khuẩn)</h4>
                    <span style="font-size: 11px; color: #ca8a04; background: #fefce8; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Prokaryote with peptidoglycan wall, no nucleus, circular DNA chromosome and plasmids.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Tế bào nhân sơ, thành peptidoglycan, không có màng nhân và ti thể, chứa phân tử DNA trần dạng vòng và plasmid.</p>
                <div style="font-size: 11.5px; color: #713f12; background: #fef9c3; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Thành peptidoglycan • Không nhân • DNA vòng • Plasmid</div>
            </div>

        </div>
    </div>

    <!-- 2. COMPARISON: PLANT VS ANIMAL CELLS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-cell-comparison" class="lecture-interactive-card" data-lecture-section="sec_cell_comparison" style="border-bottom: 3px solid #10b981; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">📊 2. SO SÁNH TẾ BÀO THỰC VẬT &amp; ĐỘNG VẬT (Comparison)</h2>
                <span style="font-size: 12px; color: #059669; font-weight: 600; background: #ecfdf5; padding: 4px 10px; border-radius: 12px; border: 1px solid #a7f3d0; display: inline-flex; align-items: center; gap: 4px;">🎧 Nghe giảng phần này</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Cả tế bào thực vật và động vật đều là tế bào nhân thực, sở hữu những đặc tính chung nhưng có các khác biệt đặc trưng cực kỳ trọng tâm trong đề thi:</p>
        </div>

        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); margin-bottom: 25px; overflow-x: auto;">
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead>
                    <tr style="background: #f8fafc; border-bottom: 2px solid #cbd5e1; text-align: left;">
                        <th style="padding: 12px; color: #0f172a;">Đặc điểm / Bào quan</th>
                        <th style="padding: 12px; color: #16a34a;">🌿 Tế bào Thực vật</th>
                        <th style="padding: 12px; color: #2563eb;">🐾 Tế bào Động vật</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 10px 12px; font-weight: 600;">Thành tế bào Cellulose</td>
                        <td style="padding: 10px 12px; color: #16a34a; font-weight: 600;">✅ Có (tạo khung định hình cố định)</td>
                        <td style="padding: 10px 12px; color: #dc2626; font-weight: 600;">❌ Không có (hình dạng linh hoạt)</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                        <td style="padding: 10px 12px; font-weight: 600;">Lục lạp &amp; Diệp lục</td>
                        <td style="padding: 10px 12px; color: #16a34a; font-weight: 600;">✅ Có (ở các tế bào quang hợp như lá)</td>
                        <td style="padding: 10px 12px; color: #dc2626; font-weight: 600;">❌ Không có</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 10px 12px; font-weight: 600;">Không bào</td>
                        <td style="padding: 10px 12px; color: #16a34a; font-weight: 600;">✅ Không bào lớn trung tâm chứa dịch bào</td>
                        <td style="padding: 10px 12px; color: #64748b;">Chỉ có các không bào nhỏ tạm thời</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                        <td style="padding: 10px 12px; font-weight: 600;">Nhân, Tế bào chất, Màng tế bào</td>
                        <td style="padding: 10px 12px; color: #16a34a; font-weight: 600;">✅ Đều có</td>
                        <td style="padding: 10px 12px; color: #2563eb; font-weight: 600;">✅ Đều có</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px 12px; font-weight: 600;">Ti thể &amp; Ribosome</td>
                        <td style="padding: 10px 12px; color: #16a34a; font-weight: 600;">✅ Đều có</td>
                        <td style="padding: 10px 12px; color: #2563eb; font-weight: 600;">✅ Đều có</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- 3. LEVELS OF ORGANISATION -->
    <div style="margin-bottom: 45px;">
        <div id="sec-levels-organisation" class="lecture-interactive-card" data-lecture-section="sec_levels_organisation" style="border-bottom: 3px solid #8b5cf6; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🏢 3. CÁC CẤP ĐỘ TỔ CHỨC SỐNG (Levels of Organisation)</h2>
                <span style="font-size: 12px; color: #6d28d9; font-weight: 600; background: #f5f3ff; padding: 4px 10px; border-radius: 12px; border: 1px solid #ddd6fe; display: inline-flex; align-items: center; gap: 4px;">🎧 Nghe giảng phần này</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Sinh vật đa bào được tổ chức theo thứ bậc chặt chẽ: từ tế bào chuyên hóa đơn lẻ cho đến cơ thể sinh vật hoàn chỉnh:</p>
        </div>

        <!-- 5 HIERARCHY CARDS -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-bottom: 30px;">
            
            <div id="card-level-cell" class="lecture-interactive-card" data-lecture-section="card_level_cell" style="background: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #3b82f6; border-radius: 10px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h4 style="margin: 0; color: #1d4ed8; font-size: 16px; font-weight: 700;">1. Cell (Tế bào)</h4>
                    <span style="font-size: 10.5px; color: #2563eb; background: #eff6ff; padding: 2px 6px; border-radius: 8px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #1e293b; margin: 0 0 4px 0;">Basic unit of life.</p>
                <p style="font-size: 12.5px; color: #0284c7; margin: 0; font-style: italic;">Đơn vị cấu trúc và chức năng cơ bản nhất của sự sống (VD: nơron, hồng cầu, lông hút).</p>
            </div>

            <div id="card-level-tissue" class="lecture-interactive-card" data-lecture-section="card_level_tissue" style="background: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #06b6d4; border-radius: 10px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h4 style="margin: 0; color: #0891b2; font-size: 16px; font-weight: 700;">2. Tissue (Mô)</h4>
                    <span style="font-size: 10.5px; color: #0891b2; background: #ecfeff; padding: 2px 6px; border-radius: 8px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #1e293b; margin: 0 0 4px 0;">Group of similar cells.</p>
                <p style="font-size: 12.5px; color: #0284c7; margin: 0; font-style: italic;">Tập hợp các tế bào có cấu trúc tương tự nhau cùng làm một chức năng chung (VD: mô giậu, mô cơ).</p>
            </div>

            <div id="card-level-organ" class="lecture-interactive-card" data-lecture-section="card_level_organ" style="background: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #8b5cf6; border-radius: 10px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h4 style="margin: 0; color: #7c3aed; font-size: 16px; font-weight: 700;">3. Organ (Cơ quan)</h4>
                    <span style="font-size: 10.5px; color: #7c3aed; background: #f5f3ff; padding: 2px 6px; border-radius: 8px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #1e293b; margin: 0 0 4px 0;">Several coordinating tissues.</p>
                <p style="font-size: 12.5px; color: #0284c7; margin: 0; font-style: italic;">Cấu trúc cơ thể riêng biệt gồm nhiều mô khác nhau cùng phối hợp (VD: tim, dạ dày, lá cây).</p>
            </div>

            <div id="card-level-system" class="lecture-interactive-card" data-lecture-section="card_level_system" style="background: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #f59e0b; border-radius: 10px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h4 style="margin: 0; color: #b45309; font-size: 16px; font-weight: 700;">4. Organ System (Hệ cơ quan)</h4>
                    <span style="font-size: 10.5px; color: #d97706; background: #fffbeb; padding: 2px 6px; border-radius: 8px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #1e293b; margin: 0 0 4px 0;">Group of linked organs.</p>
                <p style="font-size: 12.5px; color: #0284c7; margin: 0; font-style: italic;">Tập hợp các cơ quan có chức năng liên hệ mật thiết cùng hoạt động (VD: hệ tuần hoàn, tiêu hóa).</p>
            </div>

            <div id="card-level-organism" class="lecture-interactive-card" data-lecture-section="card_level_organism" style="background: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #10b981; border-radius: 10px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h4 style="margin: 0; color: #047857; font-size: 16px; font-weight: 700;">5. Organism (Cơ thể)</h4>
                    <span style="font-size: 10.5px; color: #059669; background: #ecfdf5; padding: 2px 6px; border-radius: 8px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #1e293b; margin: 0 0 4px 0;">Complete living entity.</p>
                <p style="font-size: 12.5px; color: #0284c7; margin: 0; font-style: italic;">Một thực thể sống hoàn chỉnh có khả năng thực hiện độc lập 7 đặc tính sống (VD: con người, cây sồi).</p>
            </div>

        </div>
    </div>

    <!-- 4. SPECIALISED CELLS & ADAPTATIONS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-specialised-cells" class="lecture-interactive-card" data-lecture-section="sec_specialised_cells" style="border-bottom: 3px solid #ec4899; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🧬 4. CÁC TẾ BÀO CHUYÊN HÓA (Specialised Cells)</h2>
                <span style="font-size: 12px; color: #be185d; font-weight: 600; background: #fdf2f8; padding: 4px 10px; border-radius: 12px; border: 1px solid #fbcfe8; display: inline-flex; align-items: center; gap: 4px;">🎧 Nghe giảng phần này</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Quá trình biệt hóa tế bào làm thay đổi cấu trúc để mỗi loại tế bào thích nghi hoàn hảo với một chức năng sinh lý chuyên biệt:</p>
        </div>

        <!-- 7 SPECIALISED CELLS GRID -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 30px;">
            
            <div id="card-roothair" class="lecture-interactive-card" data-lecture-section="card_roothair" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #10b981; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #047857; font-size: 17px; font-weight: 700;">🌱 Root Hair Cell (Tế bào lông hút)</h4>
                    <span style="font-size: 11px; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Long thin hair projection increases surface area for water and ion absorption. No chloroplasts.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Lông dài tăng diện tích bề mặt để hút nước (thẩm thấu) và ion khoáng (vận chuyển chủ động). Không có lục lạp do ở dưới đất.</p>
                <div style="font-size: 11.5px; color: #065f46; background: #d1fae5; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Diện tích bề mặt lớn • Không có lục lạp</div>
            </div>

            <div id="card-palisade" class="lecture-interactive-card" data-lecture-section="card_palisade" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #16a34a; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #15803d; font-size: 17px; font-weight: 700;">🍃 Palisade Mesophyll Cell (Tế bào mô giậu)</h4>
                    <span style="font-size: 11px; color: #16a34a; background: #f0fdf4; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Column shape packed closely under upper epidermis with massive chloroplast density.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Hình trụ thon dài xếp khít nhau ngay dưới lớp biểu bì trên của lá, chứa mật độ lục lạp cực cao để hấp thụ ánh sáng tối đa cho quang hợp.</p>
                <div style="font-size: 11.5px; color: #14532d; background: #dcfce7; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Mật độ lục lạp dày đặc • Hấp thụ ánh sáng tối đa</div>
            </div>

            <div id="card-ciliated" class="lecture-interactive-card" data-lecture-section="card_ciliated" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #06b6d4; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #0891b2; font-size: 17px; font-weight: 700;">💨 Ciliated Epithelial Cell (Biểu mô lông rung)</h4>
                    <span style="font-size: 11px; color: #0891b2; background: #ecfeff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Hair-like cilia sweep mucus and trapped bacteria upwards away from lungs.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Lông rung chuyển động nhịp nhàng quét sạch chất nhầy, bụi bẩn và vi khuẩn ngược lên họng tránh đi vào phổi.</p>
                <div style="font-size: 11.5px; color: #0e7490; background: #cffafe; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Lông rung nhịp nhàng • Quét sạch chất nhầy &amp; vi khuẩn</div>
            </div>

            <div id="card-rbc" class="lecture-interactive-card" data-lecture-section="card_rbc" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #ef4444; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #b91c1c; font-size: 17px; font-weight: 700;">🔴 Red Blood Cell (Hồng cầu)</h4>
                    <span style="font-size: 11px; color: #dc2626; background: #fef2f2; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Biconcave disc, packed with haemoglobin, no nucleus to maximize oxygen space.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Hình đĩa lõm hai mặt tăng diện tích khuếch tán oxy, chứa đầy sắc tố haemoglobin và không có nhân để chứa tối đa oxy.</p>
                <div style="font-size: 11.5px; color: #991b1b; background: #fee2e2; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Đĩa lõm 2 mặt • Chứa haemoglobin • Không nhân</div>
            </div>

            <div id="card-neuron" class="lecture-interactive-card" data-lecture-section="card_neuron" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #8b5cf6; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #7c3aed; font-size: 17px; font-weight: 700;">⚡ Neurone / Nerve Cell (Tế bào thần kinh)</h4>
                    <span style="font-size: 11px; color: #7c3aed; background: #f5f3ff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Long axon conducts electrical impulses over distance. Myelin sheath insulates.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Sợi trục dài dẫn truyền xung điện thần kinh đi xa, các sợi nhánh tiếp nhận tín hiệu và bao myelin cách điện giúp dẫn truyền cực nhanh.</p>
                <div style="font-size: 11.5px; color: #6b21a8; background: #ede9fe; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Sợi trục dài • Bao myelin cách điện • Xung thần kinh</div>
            </div>

            <div id="card-sperm" class="lecture-interactive-card" data-lecture-section="card_sperm" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #3b82f6; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #1d4ed8; font-size: 17px; font-weight: 700;">🏊 Sperm Cell (Tinh trùng)</h4>
                    <span style="font-size: 11px; color: #2563eb; background: #eff6ff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Acrosome enzymes penetrate egg. Midpiece has mitochondria for flagellum tail motility.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Đầu có thể đỉnh acrosome tiết enzym phân giải màng trứng, phần giữa chứa đầy ti thể giải phóng năng lượng cho đuôi roi bơi nhanh.</p>
                <div style="font-size: 11.5px; color: #1e3a8a; background: #dbeafe; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Thể đỉnh acrosome • Ti thể giải phóng ATP • Đuôi roi</div>
            </div>

            <div id="card-egg" class="lecture-interactive-card" data-lecture-section="card_egg" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #ec4899; border-radius: 10px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="margin: 0; color: #be185d; font-size: 17px; font-weight: 700;">🥚 Egg Cell / Ovum (Trứng)</h4>
                    <span style="font-size: 11px; color: #db2777; background: #fdf2f8; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <p style="font-size: 13.5px; color: #1e293b; margin: 0 0 4px 0; line-height: 1.5;">Nutrient-rich cytoplasm nourishes embryo. Jelly coat hardens upon fertilisation to block polyspermy.</p>
                <p style="font-size: 13px; color: #0284c7; margin: 0 0 8px 0; font-style: italic;">Lượng tế bào chất khổng lồ giàu dinh dưỡng nuôi dưỡng phôi; lớp màng nhầy bên ngoài cứng lại ngay khi 1 tinh trùng vào để chống đa tinh trùng.</p>
                <div style="font-size: 11.5px; color: #831843; background: #fce7f3; padding: 4px 8px; border-radius: 6px; font-weight: 600; display: inline-block;">🔑 Tế bào chất giàu dinh dưỡng • Màng nhầy cứng lại</div>
            </div>

        </div>
    </div>

    <!-- 5. MAGNIFICATION FORMULA & CALCULATIONS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-magnification" class="lecture-interactive-card" data-lecture-section="sec_magnification" style="border-bottom: 3px solid #f59e0b; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">📐 5. TÍNH ĐỘ PHÓNG ĐẠI &amp; KÍCH THƯỚC MẪU VẬT (Magnification)</h2>
                <span style="font-size: 12px; color: #b45309; font-weight: 600; background: #fffbeb; padding: 4px 10px; border-radius: 12px; border: 1px solid #fde68a; display: inline-flex; align-items: center; gap: 4px;">🎧 Nghe giảng phần này</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Nắm vững tam giác công thức IAM và quy tắc đổi đơn vị đo lường cực kỳ quan trọng cho các bài thi Paper 2, 4 và Paper 6:</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 18px; margin-bottom: 30px;">
            
            <div id="card-iam-formula" class="lecture-interactive-card" data-lecture-section="card_iam_formula" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #f59e0b; border-radius: 10px; padding: 18px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <h4 style="margin: 0; color: #b45309; font-size: 18px; font-weight: 700;">📐 Tam giác Công thức IAM</h4>
                    <span style="font-size: 11px; color: #d97706; background: #fffbeb; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px; text-align: center; margin-bottom: 12px; font-weight: 700; font-size: 18px; color: #0f172a;">
                    $$I = A \\times M$$
                </div>
                <ul style="margin: 0; padding-left: 20px; font-size: 13.5px; color: #334155; line-height: 1.6;">
                    <li><b>Kích thước ảnh ($I$):</b> Đo bằng thước kẻ trên giấy thi (mm).</li>
                    <li><b>Kích thước thực tế ($A$):</b> $A = \\frac{I}{M}$</li>
                    <li><b>Độ phóng đại ($M$):</b> $M = \\frac{I}{A}$ (không có đơn vị, viết kèm dấu $\\times$, VD: $\\times 500$).</li>
                </ul>
            </div>

            <div id="card-units-conversion" class="lecture-interactive-card" data-lecture-section="card_units_conversion" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #3b82f6; border-radius: 10px; padding: 18px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <h4 style="margin: 0; color: #1d4ed8; font-size: 18px; font-weight: 700;">🔄 Quy tắc Đổi Đơn vị ($1\\text{ mm} = 1000\\ \\mu\\text{m}$)</h4>
                    <span style="font-size: 11px; color: #2563eb; background: #eff6ff; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng</span>
                </div>
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 12px; text-align: center; margin-bottom: 12px; font-weight: 700; font-size: 16px; color: #1d4ed8;">
                    Milimét (mm) $\\xrightarrow{\\times 1000}$ Micromét ($\\mu$m)
                </div>
                <p style="font-size: 13.5px; color: #334155; margin: 0; line-height: 1.6;">
                    • <b>Đổi từ mm sang $\\mu$m:</b> Nhân với 1000.<br/>
                    • <b>Đổi từ $\\mu$m sang mm:</b> Chia cho 1000.<br/>
                    • <i>Quy tắc vàng:</i> Luôn đưa $I$ và $A$ về cùng một đơn vị (thường là $\\mu$m) trước khi thực hiện phép chia!
                </p>
            </div>

        </div>
    </div>

</div>'''

def main():
    p1 = get_page1_html()
    p2 = get_page2_html()

    d1 = p1.count('<div') - p1.count('</div>')
    d2 = p2.count('<div') - p2.count('</div>')
    print(f"Div balance check: P1={d1}, P2={d2}")
    assert d1 == 0 and d2 == 0, f"Divs unbalanced: P1={d1}, P2={d2}"

    # Update Supabase
    print("Updating Topic 2 in Supabase...")
    sb.table('lecture_pages').update({'content_html': p1}).eq('lecture_id', T2_ID).eq('page_number', 1).execute()
    sb.table('lecture_pages').update({'content_html': p2}).eq('lecture_id', T2_ID).eq('page_number', 2).execute()
    print("Successfully updated Topic 2 Page 1 and Page 2 in Supabase!")

if __name__ == '__main__':
    main()
