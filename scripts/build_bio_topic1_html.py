# -*- coding: utf-8 -*-
"""
Script to build merged HTML for Topic 1:
- Page 1: English (Merging original Page 1 + Page 3 + Other Kingdoms)
- Page 2: Vietnamese / Song ngữ (Merging original Page 2 + Page 4)
With strict div balancing and interactive badges.
"""

import os
import re

def build_page_1_html():
    """Builds comprehensive English HTML for Page 1 (1 + 3)"""
    html = '''<div style="font-family: 'Segoe UI', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">

    <!-- TOP HEADER BANNER (CLICKABLE OVERVIEW) -->
    <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
            <div>
                <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 0.5px;">Cambridge IGCSE Biology (0610)</span>
                <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc; letter-spacing: -0.5px;">Topic 1: Characteristics &amp; Classification of Living Organisms</h1>
                <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Complete Master Lecture • MRS GREN, Classification Systems, 5 Kingdoms, Animals &amp; Plants</p>
            </div>
            <div style="background: rgba(37, 99, 235, 0.2); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 20px; padding: 8px 16px; display: flex; align-items: center; gap: 8px; font-weight: 600; font-size: 14px; color: #60a5fa;">
                <span>🎧 Click any card to listen</span>
            </div>
        </div>
    </div>

    <!-- 1. CHARACTERISTICS OF LIVING ORGANISMS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-characteristics" class="lecture-interactive-card" data-lecture-section="sec_characteristics" style="border-bottom: 3px solid #10b981; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🌱 1. CHARACTERISTICS OF LIVING ORGANISMS</h2>
                <span style="font-size: 12px; color: #059669; font-weight: 600; background: #ecfdf5; padding: 4px 10px; border-radius: 12px; border: 1px solid #a7f3d0;">🎧 Listen to Section</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">All living organisms share seven fundamental characteristics. Remember them using the mnemonic <b>MRS GREN</b>:</p>
        </div>

        <!-- 7 MRS GREN CARDS -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; margin-bottom: 30px;">
            <div id="card-movement" class="lecture-interactive-card" data-lecture-section="card_movement" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #3b82f6; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #1d4ed8; font-size: 17px;">🏃 Movement</h4>
                    <span style="font-size: 11px; color: #2563eb; background: #eff6ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">An action by an organism or part of an organism causing a change of position or place.</p>
            </div>

            <div id="card-respiration" class="lecture-interactive-card" data-lecture-section="card_respiration" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #ef4444; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #b91c1c; font-size: 17px;">💨 Respiration</h4>
                    <span style="font-size: 11px; color: #dc2626; background: #fef2f2; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Chemical reactions in cells that break down nutrient molecules and <b>release energy</b> for metabolism.</p>
            </div>

            <div id="card-sensitivity" class="lecture-interactive-card" data-lecture-section="card_sensitivity" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #f59e0b; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #b45309; font-size: 17px;">👀 Sensitivity</h4>
                    <span style="font-size: 11px; color: #d97706; background: #fffbeb; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">The ability to detect and respond to changes in the internal or external environment (stimuli).</p>
            </div>

            <div id="card-growth" class="lecture-interactive-card" data-lecture-section="card_growth" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #10b981; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #047857; font-size: 17px;">📈 Growth</h4>
                    <span style="font-size: 11px; color: #059669; background: #ecfdf5; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">A permanent increase in size and <b>dry mass</b>.</p>
            </div>

            <div id="card-reproduction" class="lecture-interactive-card" data-lecture-section="card_reproduction" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #ec4899; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #be185d; font-size: 17px;">👶 Reproduction</h4>
                    <span style="font-size: 11px; color: #db2777; background: #fdf2f8; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">The biological processes that make more of the same kind of organism.</p>
            </div>

            <div id="card-excretion" class="lecture-interactive-card" data-lecture-section="card_excretion" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #8b5cf6; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #6b21a8; font-size: 17px;">🚽 Excretion</h4>
                    <span style="font-size: 11px; color: #7c3aed; background: #f5f3ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Removal of waste products of metabolism and substances in excess of requirements.</p>
            </div>

            <div id="card-nutrition" class="lecture-interactive-card" data-lecture-section="card_nutrition" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #06b6d4; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #0e7490; font-size: 17px;">🍎 Nutrition</h4>
                    <span style="font-size: 11px; color: #0891b2; background: #ecfeff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Taking in of materials for energy, growth and development.</p>
            </div>
        </div>

        <!-- 3D INTERACTIVE FLIPCARDS -->
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <h3 style="margin: 0; color: #0f172a; font-size: 20px;">🧬 1.2. Interactive Flashcards (MRS GREN)</h3>
                <span style="font-size: 13px; color: #64748b; font-style: italic;">Hover or tap each card to flip</span>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 15px; justify-content: center;">
                <!-- M -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #e0f2fe; background: linear-gradient(135deg, #f0f9ff, #e0f2fe); color: #0284c7;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">M</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Movement</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #0ea5e9; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #0284c7;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Change of position or place.</div>
                        </div>
                    </div>
                </div>
                <!-- R -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #fee2e2; background: linear-gradient(135deg, #fef2f2, #fee2e2); color: #dc2626;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">R</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Respiration</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #ef4444; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #dc2626;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Reactions releasing energy for metabolism.</div>
                        </div>
                    </div>
                </div>
                <!-- S -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #fef3c7; background: linear-gradient(135deg, #fffbeb, #fef3c7); color: #d97706;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">S</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Sensitivity</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #f59e0b; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #d97706;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Detect and respond to internal/external stimuli.</div>
                        </div>
                    </div>
                </div>
                <!-- G -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #dcfce7; background: linear-gradient(135deg, #f0fdf4, #dcfce7); color: #16a34a;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">G</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Growth</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #10b981; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #16a34a;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Permanent increase in size and dry mass.</div>
                        </div>
                    </div>
                </div>
                <!-- R2 -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #fce7f3; background: linear-gradient(135deg, #fdf2f8, #fce7f3); color: #db2777;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">R</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Reproduction</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #ec4899; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #db2777;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Processes making more of the same kind.</div>
                        </div>
                    </div>
                </div>
                <!-- E -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #ede9fe; background: linear-gradient(135deg, #f5f3ff, #ede9fe); color: #7c3aed;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">E</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Excretion</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #8b5cf6; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #7c3aed;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Removal of toxic metabolic waste products.</div>
                        </div>
                    </div>
                </div>
                <!-- N -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #cffafe; background: linear-gradient(135deg, #ecfeff, #cffafe); color: #0891b2;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">N</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Nutrition</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #06b6d4; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #0891b2;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Taking in nutrients for energy &amp; growth.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- EXCRETION ORGANS & EXAM TRAPS -->
        <div style="margin-bottom: 30px;">
            <div id="sec-excretion-organs" class="lecture-interactive-card" data-lecture-section="sec_excretion_organs" style="border-bottom: 2px solid #0284c7; padding-bottom: 8px; margin-bottom: 20px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="margin: 0; color: #0369a1; font-size: 20px;">💧 Major Organs of Excretion in Humans</h3>
                    <span style="font-size: 12px; color: #0284c7; font-weight: 600; background: #e0f2fe; padding: 3px 8px; border-radius: 10px;">🎧 Listen Section</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px; margin-bottom: 25px;">
                <div id="card-skin" class="lecture-interactive-card" data-lecture-section="card_skin" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #0284c7; font-size: 16px;">✋ Skin</h4>
                        <span style="font-size: 11px; color: #0284c7; background: #e0f2fe; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 14px; color: #475569;">Excretes <b>sweat</b>, which contains excess water, mineral salts, and trace urea for thermoregulation.</p>
                </div>
                <div id="card-kidneys" class="lecture-interactive-card" data-lecture-section="card_kidneys" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #0284c7; font-size: 16px;">🫘 Kidneys</h4>
                        <span style="font-size: 11px; color: #0284c7; background: #e0f2fe; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 14px; color: #475569;">Excrete <b>urine</b>, filtering out urea produced from deamination, excess mineral ions, and water.</p>
                </div>
                <div id="card-lungs" class="lecture-interactive-card" data-lecture-section="card_lungs" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #0284c7; font-size: 16px;">🫁 Lungs</h4>
                        <span style="font-size: 11px; color: #0284c7; background: #e0f2fe; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 14px; color: #475569;">Excrete <b>carbon dioxide (CO₂)</b> and water vapour produced continuously by cellular respiration.</p>
                </div>
            </div>

            <div id="sec-key-terms" class="lecture-interactive-card" data-lecture-section="sec_key_terms" style="border-bottom: 2px solid #ea580c; padding-bottom: 8px; margin-bottom: 20px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="margin: 0; color: #c2410c; font-size: 20px;">📌 Key Terms: Ingestion vs Egestion</h3>
                    <span style="font-size: 12px; color: #c2410c; font-weight: 600; background: #ffedd5; padding: 3px 8px; border-radius: 10px;">🎧 Listen Section</span>
                </div>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 15px;">
                <div style="flex: 1; min-width: 260px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 8px; padding: 15px;">
                    <h4 style="margin: 0 0 5px 0; color: #c2410c;">Ingestion</h4>
                    <p style="margin: 0; font-size: 14px; color: #7c2d12;">Taking of substances (food and drink) into the body through the mouth.</p>
                </div>
                <div style="flex: 1; min-width: 260px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 8px; padding: 15px;">
                    <h4 style="margin: 0 0 5px 0; color: #c2410c;">Egestion</h4>
                    <p style="margin: 0; font-size: 14px; color: #7c2d12;">Passing out of food that has not been digested or absorbed, as faeces through the anus.</p>
                </div>
            </div>
            <div id="card-trap-egestion" class="lecture-interactive-card" data-lecture-section="card_trap_egestion" style="background: #fef2f2; border-left: 5px solid #ef4444; padding: 18px; border-radius: 8px; cursor: pointer; box-shadow: 0 2px 4px rgba(239,68,68,0.06);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h4 style="margin: 0; color: #b91c1c; font-size: 16px;">⚠️ Common Exam Trap: Egestion is NOT Excretion</h4>
                    <span style="font-size: 11px; color: #b91c1c; background: #fee2e2; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Exam Trap Audio</span>
                </div>
                <p style="margin: 0; color: #991b1b; font-size: 14px; line-height: 1.6;">
                    • <b>Excretion</b> is removing metabolic waste made <i>inside cells</i> (e.g. urea, CO₂).<br>
                    • <b>Egestion</b> is passing out undigested food that just passed <i>through the gut</i> without ever entering cells or metabolic reactions.
                </p>
            </div>
        </div>
    </div>

    <!-- 2.1. CLASSIFICATION SYSTEMS & IDENTIFICATION -->
    <div style="margin-bottom: 50px;">
        <div id="sec-classification" class="lecture-interactive-card" data-lecture-section="sec_classification" style="border-bottom: 3px solid #3b82f6; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🏷️ 2.1. CLASSIFICATION SYSTEMS &amp; IDENTIFICATION</h2>
                <span style="font-size: 12px; color: #1d4ed8; font-weight: 600; background: #eff6ff; padding: 4px 10px; border-radius: 12px; border: 1px solid #bfdbfe;">🎧 Listen to Section</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Classification reflects evolutionary relationships. Organisms sharing a recent common ancestor share closely matching DNA sequences.</p>
        </div>

        <!-- SPECIES & BINOMIAL SYSTEM -->
        <div style="display: flex; flex-direction: column; gap: 20px; margin-bottom: 30px;">
            <div id="sec-species" class="lecture-interactive-card" data-lecture-section="sec_species" style="background: #e0f2fe; border: 1px solid #bae6fd; border-left: 5px solid #0ea5e9; border-radius: 8px; padding: 18px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h3 style="margin: 0; color: #0284c7; font-size: 18px;">🔑 Key Definition: Species</h3>
                    <span style="font-size: 11px; color: #0284c7; background: #bae6fd; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="margin: 0; font-size: 15px; color: #0f172a;">A <b>species</b> is defined as a group of organisms that can reproduce to produce <b>fertile offspring</b>.</p>
            </div>

            <div id="sec-binomial" class="lecture-interactive-card" data-lecture-section="sec_binomial" style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 12px; padding: 20px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h3 style="margin: 0; color: #1e40af; font-size: 18px;">The Binomial System of Naming Organisms</h3>
                    <span style="font-size: 11px; color: #1d4ed8; background: #dbeafe; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 14px; color: #475569; margin-bottom: 15px;">A two-part Latin naming system: the first name is the <b>Genus</b> (capitalized), and the second is the <b>species</b> (lowercase).</p>
                <div style="background: #ffffff; padding: 15px; border-radius: 8px; border: 2px dashed #93c5fd; text-align: center;">
                    <span style="font-size: 26px; font-weight: bold; font-style: italic; color: #1d4ed8;">Panthera leo</span>
                    <div style="display: flex; justify-content: center; gap: 40px; margin-top: 10px; font-size: 13px; font-weight: bold;">
                        <span style="color: #2563eb;">Genus (Capital letter)</span>
                        <span style="color: #059669;">species (lowercase)</span>
                    </div>
                </div>
            </div>

            <!-- EXAM RULES -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px;">
                <div id="card-rule-typography" class="lecture-interactive-card" data-lecture-section="card_rule_typography" style="background: #fef2f2; border-left: 4px solid #ef4444; padding: 15px; border-radius: 8px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <h4 style="margin: 0; color: #991b1b; font-size: 15px;">🚨 EXAM RULE 1: Typography Rules</h4>
                        <span style="font-size: 11px; color: #991b1b; background: #fee2e2; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #7f1d1d; line-height: 1.6;">
                        • When printed: Must be in <em>italics</em>.<br>
                        • When handwritten in exams: Must be <u>underlined</u> separately (e.g. <u>Panthera</u> <u>leo</u>).<br>
                        • Genus MUST start with a Capital letter; species MUST be in lowercase.
                    </p>
                </div>

                <div id="card-rule-viruses" class="lecture-interactive-card" data-lecture-section="card_rule_viruses" style="background: #fffbeb; border-left: 4px solid #f59e0b; padding: 15px; border-radius: 8px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <h4 style="margin: 0; color: #92400e; font-size: 15px;">🚨 EXAM RULE 2: What about Viruses?</h4>
                        <span style="font-size: 11px; color: #92400e; background: #fef3c7; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #78350f; line-height: 1.6;">
                        • Viruses are <strong>NOT cells</strong> and are <strong>NOT included in the 5 Kingdoms</strong>.<br>
                        • Structure: Genetic material (DNA or RNA) enclosed inside a <strong>protein coat</strong> (capsid).<br>
                        • They only replicate inside living host cells.
                    </p>
                </div>
            </div>
        </div>

        <!-- THE FIVE KINGDOMS -->
        <div id="sec-five-kingdoms" class="lecture-interactive-card" data-lecture-section="sec_five_kingdoms" style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 12px; padding: 25px; margin-bottom: 30px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <h3 style="margin: 0; color: #166534; font-size: 20px;">🌍 The Five Kingdoms of Living Organisms</h3>
                <span style="font-size: 11px; color: #15803d; background: #dcfce7; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Listen Kingdom Audio</span>
            </div>
            <p style="font-size: 14px; color: #14532d; margin-bottom: 20px;">All cellular organisms are classified into Five Kingdoms based on cell structure and nutrition:</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 15px;">
                <div style="background: #ffffff; border: 1px solid #86efac; border-radius: 8px; padding: 15px;">
                    <div style="font-size: 28px; margin-bottom: 5px;">🦁</div>
                    <strong style="color: #15803d; font-size: 15px;">Animals</strong>
                    <p style="font-size: 12px; color: #475569; margin: 5px 0 0 0;">Multicellular, no cell wall, ingestive heterotrophs.</p>
                </div>
                <div style="background: #ffffff; border: 1px solid #86efac; border-radius: 8px; padding: 15px;">
                    <div style="font-size: 28px; margin-bottom: 5px;">🌿</div>
                    <strong style="color: #15803d; font-size: 15px;">Plants</strong>
                    <p style="font-size: 12px; color: #475569; margin: 5px 0 0 0;">Multicellular, cellulose cell walls, chloroplasts, autotrophs.</p>
                </div>
                <div style="background: #ffffff; border: 1px solid #86efac; border-radius: 8px; padding: 15px;">
                    <div style="font-size: 28px; margin-bottom: 5px;">🍄</div>
                    <strong style="color: #15803d; font-size: 15px;">Fungi</strong>
                    <p style="font-size: 12px; color: #475569; margin: 5px 0 0 0;">Chitin cell walls, hyphae mycelium, saprotrophic nutrition.</p>
                </div>
                <div style="background: #ffffff; border: 1px solid #86efac; border-radius: 8px; padding: 15px;">
                    <div style="font-size: 28px; margin-bottom: 5px;">🦠</div>
                    <strong style="color: #15803d; font-size: 15px;">Prokaryotes</strong>
                    <p style="font-size: 12px; color: #475569; margin: 5px 0 0 0;">Unicellular, no true nucleus, circular DNA loop, plasmids.</p>
                </div>
                <div style="background: #ffffff; border: 1px solid #86efac; border-radius: 8px; padding: 15px;">
                    <div style="font-size: 28px; margin-bottom: 5px;">🔬</div>
                    <strong style="color: #15803d; font-size: 15px;">Protoctists</strong>
                    <p style="font-size: 12px; color: #475569; margin: 5px 0 0 0;">Eukaryotes, mostly unicellular, diverse (Amoeba, algae).</p>
                </div>
            </div>
            <div style="margin-top: 15px; background: #ecfdf5; border-radius: 6px; padding: 12px; font-size: 13px; color: #065f46;">
                <strong>🧬 Modern Classification (Supplement):</strong> Organisms sharing more recent common ancestors have base sequences in DNA that are more similar than those of organisms sharing more distant ancestors.
            </div>
        </div>

        <!-- DICHOTOMOUS KEYS -->
        <div id="sec-dichotomous" class="lecture-interactive-card" data-lecture-section="sec_dichotomous" style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <h3 style="margin: 0; color: #0f172a; font-size: 20px;">🔍 Dichotomous Keys</h3>
                <span style="font-size: 11px; color: #0284c7; background: #e0f2fe; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
            </div>
            <p style="font-size: 14px; color: #475569; margin-bottom: 15px;">A dichotomous key is a diagnostic identification tool using pairs of contrasting physical characteristics.</p>
            <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px; font-family: monospace; font-size: 13px; color: #334155; line-height: 1.8;">
                1 a) Has wings .................................................... go to 2<br>
                &nbsp;&nbsp;b) Does not have wings ................................. go to 3<br>
                2 a) 1 pair of wings ............................................. Fly<br>
                &nbsp;&nbsp;b) 2 pairs of wings ........................................... Butterfly
            </div>
        </div>
    </div>

    <!-- 2.2. THE ANIMAL KINGDOM -->
    <div style="margin-bottom: 50px;">
        <div id="sec-animal-kingdom" class="lecture-interactive-card" data-lecture-section="sec_animal_kingdom" style="border-bottom: 3px solid #e11d48; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🦁 2.2. THE ANIMAL KINGDOM</h2>
                <span style="font-size: 12px; color: #e11d48; font-weight: 600; background: #ffe4e6; padding: 4px 10px; border-radius: 12px; border: 1px solid #fecdd3;">🎧 Listen to Section</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Animals are divided into Vertebrates (with backbones) and Invertebrates (including Arthropods).</p>
        </div>
        
        <!-- VERTEBRATES -->
        <div style="margin-bottom: 35px;">
            <div id="sec-vertebrates" class="lecture-interactive-card" data-lecture-section="sec_vertebrates" style="border-left: 4px solid #be123c; padding-left: 10px; margin-bottom: 15px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="color: #be123c; font-size: 19px; margin: 0;">🦴 Vertebrates (5 Classes)</h3>
                    <span style="font-size: 11px; color: #be123c; background: #ffe4e6; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Overview Audio</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
                <div id="card-fish" class="lecture-interactive-card" data-lecture-section="card_fish" style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #9f1239; font-size: 16px;">🐟 Fish</h4>
                        <span style="font-size: 11px; color: #9f1239; background: #ffe4e6; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #881337; line-height: 1.5;">Wet slimy scales, gills for breathing, fins for balance, jelly-covered eggs in water.</p>
                </div>
                <div id="card-amphibians" class="lecture-interactive-card" data-lecture-section="card_amphibians" style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #9f1239; font-size: 16px;">🐸 Amphibians</h4>
                        <span style="font-size: 11px; color: #9f1239; background: #ffe4e6; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #881337; line-height: 1.5;">Moist scaleless permeable skin, larvae have gills in water, adults have lungs on land.</p>
                </div>
                <div id="card-reptiles" class="lecture-interactive-card" data-lecture-section="card_reptiles" style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #9f1239; font-size: 16px;">🦎 Reptiles</h4>
                        <span style="font-size: 11px; color: #9f1239; background: #ffe4e6; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #881337; line-height: 1.5;">Dry waterproof scaly skin, breathe with lungs, rubbery shelled eggs laid on land.</p>
                </div>
                <div id="card-birds" class="lecture-interactive-card" data-lecture-section="card_birds" style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #9f1239; font-size: 16px;">🦅 Birds</h4>
                        <span style="font-size: 11px; color: #9f1239; background: #ffe4e6; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #881337; line-height: 1.5;">Feathers, wings, beak without teeth, endothermic, hard calcium-shelled eggs.</p>
                </div>
                <div id="card-mammals" class="lecture-interactive-card" data-lecture-section="card_mammals" style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #9f1239; font-size: 16px;">🐆 Mammals</h4>
                        <span style="font-size: 11px; color: #9f1239; background: #ffe4e6; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #881337; line-height: 1.5;">Fur or hair, mammary glands producing milk, pinnae (external ears), live young.</p>
                </div>
            </div>
        </div>

        <!-- ARTHROPODS -->
        <div>
            <div id="sec-arthropods" class="lecture-interactive-card" data-lecture-section="sec_arthropods" style="border-left: 4px solid #c026d3; padding-left: 10px; margin-bottom: 15px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="color: #c026d3; font-size: 19px; margin: 0;">🦑 Arthropods (Invertebrates with Jointed Legs)</h3>
                    <span style="font-size: 11px; color: #c026d3; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Overview Audio</span>
                </div>
            </div>
            <p style="font-size: 14px; color: #475569; margin-bottom: 15px;">All arthropods have a waterproof <strong>chitinous exoskeleton</strong>, a segmented body, and jointed legs.</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px;">
                <div id="card-insects" class="lecture-interactive-card" data-lecture-section="card_insects" style="background: #fdf4ff; border: 1px solid #f0abfc; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #a21caf; font-size: 16px;">🐜 Insects</h4>
                        <span style="font-size: 11px; color: #a21caf; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #701a75; line-height: 1.6;">• 3 body parts (head, thorax, abdomen)<br>• 3 pairs of jointed legs on thorax<br>• 1 pair of antennae, usually 2 pairs of wings</p>
                </div>
                <div id="card-arachnids" class="lecture-interactive-card" data-lecture-section="card_arachnids" style="background: #fdf4ff; border: 1px solid #f0abfc; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #a21caf; font-size: 16px;">🕷️ Arachnids</h4>
                        <span style="font-size: 11px; color: #a21caf; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #701a75; line-height: 1.6;">• 2 body parts (cephalothorax, abdomen)<br>• 4 pairs of jointed legs<br>• No antennae, no wings, chelicerae</p>
                </div>
                <div id="card-crustaceans" class="lecture-interactive-card" data-lecture-section="card_crustaceans" style="background: #fdf4ff; border: 1px solid #f0abfc; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #a21caf; font-size: 16px;">🦀 Crustaceans</h4>
                        <span style="font-size: 11px; color: #a21caf; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #701a75; line-height: 1.6;">• 5 or more pairs of jointed legs<br>• 2 pairs of antennae, breathe with gills<br>• Mostly aquatic (crabs, prawns)</p>
                </div>
                <div id="card-myriapods" class="lecture-interactive-card" data-lecture-section="card_myriapods" style="background: #fdf4ff; border: 1px solid #f0abfc; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #a21caf; font-size: 16px;">🐛 Myriapods</h4>
                        <span style="font-size: 11px; color: #a21caf; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #701a75; line-height: 1.6;">• Many body segments<br>• 1 pair of legs per segment (centipedes)<br>• 2 pairs of legs per segment (millipedes)</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 2.3. THE PLANT KINGDOM & OTHER KINGDOMS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-plant-kingdom" class="lecture-interactive-card" data-lecture-section="sec_plant_kingdom" style="border-bottom: 3px solid #16a34a; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🌿 2.3. THE PLANT KINGDOM: MONOCOTS VS DICOTS</h2>
                <span style="font-size: 12px; color: #15803d; font-weight: 600; background: #ecfdf5; padding: 4px 10px; border-radius: 12px; border: 1px solid #a7f3d0;">🎧 Listen to Section</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Flowering plants are divided into Monocotyledons (Monocots) and Dicotyledons (Dicots).</p>
        </div>

        <div style="display: flex; flex-wrap: wrap; gap: 25px; align-items: stretch; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 35px;">
            <!-- SVG DIAGRAM -->
            <div style="flex: 1; min-width: 280px; max-width: 400px; text-align: center; display: flex; flex-direction: column; justify-content: center;">
                <h4 style="margin: 0 0 10px 0; color: #15803d; font-size: 16px;">Interactive: Monocots vs Dicots</h4>
                <p style="font-size: 13px; color: #64748b; margin-bottom: 15px;">Hover over the plant types to switch view:</p>
                <svg viewBox="0 0 300 200" width="100%" height="auto" style="display: block; margin: 0 auto;">
                    <g style="cursor: pointer; transition: 0.2s;" onmouseover="document.getElementById('card-monocots').style.display='block'; document.getElementById('card-dicots').style.display='none';">
                        <rect x="20" y="20" width="120" height="160" rx="8" fill="#f0fdf4" stroke="#4ade80" stroke-width="2"></rect>
                        <path d="M 80 40 Q 50 100 80 160 Q 110 100 80 40 Z" fill="#bbf7d0"></path>
                        <path d="M 70 50 L 70 150 M 80 45 L 80 155 M 90 50 L 90 150" stroke="#16a34a" stroke-width="2"></path>
                        <text x="80" y="150" font-family="Arial" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">Monocot</text>
                    </g>
                    <g style="cursor: pointer; transition: 0.2s;" onmouseover="document.getElementById('card-monocots').style.display='none'; document.getElementById('card-dicots').style.display='block';">
                        <rect x="160" y="20" width="120" height="160" rx="8" fill="#fdf4ff" stroke="#e879f9" stroke-width="2"></rect>
                        <circle cx="220" cy="80" r="35" fill="#f5d0fe"></circle>
                        <path d="M 220 50 L 220 110 M 195 80 L 245 80" stroke="#c026d3" stroke-width="2"></path>
                        <text x="220" y="150" font-family="Arial" font-size="12" font-weight="bold" fill="#a21caf" text-anchor="middle">Dicot</text>
                    </g>
                </svg>
            </div>

            <!-- MONOCOTS & DICOTS DETAILS (BOTH CLICKABLE) -->
            <div style="flex: 1.5; min-width: 320px; display: flex; flex-direction: column; gap: 15px;">
                <div id="card-monocots" class="lecture-interactive-card" data-lecture-section="card_monocots" style="background: #f0fdf4; border-left: 5px solid #22c55e; border-radius: 8px; padding: 20px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h4 style="margin: 0; color: #15803d; font-size: 18px;">🌱 Monocotyledons (Monocots)</h4>
                        <span style="font-size: 11px; color: #15803d; background: #dcfce7; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #14532d; line-height: 1.8;">
                        <li><strong>Seeds:</strong> One cotyledon (seed leaf).</li>
                        <li><strong>Leaves:</strong> Long, narrow leaves with <strong>parallel veins</strong>.</li>
                        <li><strong>Roots:</strong> Branching, fibrous root system.</li>
                        <li><strong>Flowers:</strong> Floral parts in multiples of 3.</li>
                        <li><strong>Examples:</strong> Grasses, maize, wheat, orchids.</li>
                    </ul>
                </div>

                <div id="card-dicots" class="lecture-interactive-card" data-lecture-section="card_dicots" style="background: #fdf4ff; border-left: 5px solid #d946ef; border-radius: 8px; padding: 20px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h4 style="margin: 0; color: #a21caf; font-size: 18px;">🌳 Dicotyledons (Dicots)</h4>
                        <span style="font-size: 11px; color: #a21caf; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #701a75; line-height: 1.8;">
                        <li><strong>Seeds:</strong> Two cotyledons (seed leaves).</li>
                        <li><strong>Leaves:</strong> Broad leaves with a <strong>branching (reticulate) network of veins</strong>.</li>
                        <li><strong>Roots:</strong> Main taproot system with smaller lateral roots.</li>
                        <li><strong>Flowers:</strong> Floral parts in multiples of 4 or 5.</li>
                        <li><strong>Examples:</strong> Oak trees, roses, sunflowers, beans.</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- 2.4. OTHER KINGDOMS -->
        <div>
            <h3 style="color: #0f172a; margin: 0 0 15px 0; font-size: 20px;">🦠 Other Kingdoms: Fungi, Prokaryotes &amp; Protoctists</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 15px;">
                <div id="card-fungi" class="lecture-interactive-card" data-lecture-section="card_fungi" style="flex: 1; min-width: 260px; background: #fffbeb; border: 2px solid #fcd34d; border-radius: 10px; padding: 20px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h4 style="margin: 0; color: #b45309; font-size: 16px;">🍄 Fungi</h4>
                        <span style="font-size: 11px; color: #b45309; background: #fef3c7; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <ul style="margin: 0; padding-left: 18px; font-size: 13px; color: #78350f; line-height: 1.7;">
                        <li>Eukaryotes (multicellular moulds/mushrooms or unicellular yeast).</li>
                        <li>Cell walls made of <strong>chitin</strong> (not cellulose).</li>
                        <li>No chloroplasts; saprotrophic or parasitic feeding via hyphae.</li>
                    </ul>
                </div>

                <div id="card-prokaryotes" class="lecture-interactive-card" data-lecture-section="card_prokaryotes" style="flex: 1; min-width: 260px; background: #fdf4ff; border: 2px solid #f0abfc; border-radius: 10px; padding: 20px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h4 style="margin: 0; color: #a21caf; font-size: 16px;">Prokaryotes (Bacteria)</h4>
                        <span style="font-size: 11px; color: #a21caf; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <ul style="margin: 0; padding-left: 18px; font-size: 13px; color: #4a044e; line-height: 1.7;">
                        <li>Unicellular; <strong>no true nucleus</strong>.</li>
                        <li>Circular DNA loop free in cytoplasm, plus plasmids.</li>
                        <li>Cell wall made of peptidoglycan, no mitochondria.</li>
                    </ul>
                </div>

                <div id="card-protoctists" class="lecture-interactive-card" data-lecture-section="card_protoctists" style="flex: 1; min-width: 260px; background: #ecfdf5; border: 2px solid #6ee7b7; border-radius: 10px; padding: 20px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h4 style="margin: 0; color: #047857; font-size: 16px;">Protoctists</h4>
                        <span style="font-size: 11px; color: #047857; background: #dcfce7; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <ul style="margin: 0; padding-left: 18px; font-size: 13px; color: #064e3b; line-height: 1.7;">
                        <li>Eukaryotes with true nucleus; mostly unicellular.</li>
                        <li>Highly diverse: some animal-like (<em>Amoeba</em>), some plant-like with chloroplasts (<em>Chlorella</em>).</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

</div>'''
    return html


def build_page_2_html():
    """Builds comprehensive Vietnamese/Bilingual HTML for Page 2 (2 + 4)"""
    html = '''<div style="font-family: 'Segoe UI', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">

    <!-- TOP HEADER BANNER (CLICKABLE OVERVIEW) -->
    <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
            <div>
                <span style="display: inline-block; background: #10b981; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 0.5px;">Cambridge IGCSE Biology (0610) • Song ngữ</span>
                <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc; letter-spacing: -0.5px;">Chuyên đề 1: Đặc điểm &amp; Phân loại Sinh vật sống</h1>
                <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Bài giảng Song ngữ Toàn diện • MRS GREN, Hệ thống phân loại, Năm Giới, Động vật &amp; Thực vật</p>
            </div>
            <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; display: flex; align-items: center; gap: 8px; font-weight: 600; font-size: 14px; color: #34d399;">
                <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
            </div>
        </div>
    </div>

    <!-- 1. CHARACTERISTICS OF LIVING THINGS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-characteristics" class="lecture-interactive-card" data-lecture-section="sec_characteristics" style="border-bottom: 3px solid #10b981; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🌱 1. BẢY ĐẶC TÍNH CỦA SỰ SỐNG (MRS GREN)</h2>
                <span style="font-size: 12px; color: #059669; font-weight: 600; background: #ecfdf5; padding: 4px 10px; border-radius: 12px; border: 1px solid #a7f3d0;">🎧 Nghe giảng phần này</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Tất cả các sinh vật sống đều có chung 7 đặc điểm thiết yếu. Hãy ghi nhớ bằng quy tắc <b>MRS GREN</b>:</p>
        </div>

        <!-- 7 MRS GREN CARDS -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; margin-bottom: 30px;">
            <div id="card-movement" class="lecture-interactive-card" data-lecture-section="card_movement" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #3b82f6; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #1d4ed8; font-size: 17px;">🏃 Movement (Vận động)</h4>
                    <span style="font-size: 11px; color: #2563eb; background: #eff6ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Sự di chuyển. Hành động của cơ thể hoặc bộ phận cơ thể gây ra sự thay đổi vị trí hoặc chỗ ở.</p>
            </div>

            <div id="card-respiration" class="lecture-interactive-card" data-lecture-section="card_respiration" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #ef4444; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #b91c1c; font-size: 17px;">💨 Respiration (Hô hấp)</h4>
                    <span style="font-size: 11px; color: #dc2626; background: #fef2f2; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Phản ứng hóa học trong tế bào giúp phân giải chất dinh dưỡng và <b>giải phóng năng lượng</b> cho trao đổi chất.</p>
            </div>

            <div id="card-sensitivity" class="lecture-interactive-card" data-lecture-section="card_sensitivity" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #f59e0b; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #b45309; font-size: 17px;">👀 Sensitivity (Cảm ứng)</h4>
                    <span style="font-size: 11px; color: #d97706; background: #fffbeb; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Khả năng phát hiện và phản ứng lại với các kích thích thay đổi từ môi trường trong hoặc môi trường ngoài.</p>
            </div>

            <div id="card-growth" class="lecture-interactive-card" data-lecture-section="card_growth" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #10b981; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #047857; font-size: 17px;">📈 Growth (Sinh trưởng)</h4>
                    <span style="font-size: 11px; color: #059669; background: #ecfdf5; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Sự gia tăng vĩnh viễn về kích thước và <b>khối lượng khô (dry mass)</b>.</p>
            </div>

            <div id="card-reproduction" class="lecture-interactive-card" data-lecture-section="card_reproduction" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #ec4899; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #be185d; font-size: 17px;">👶 Reproduction (Sinh sản)</h4>
                    <span style="font-size: 11px; color: #db2777; background: #fdf2f8; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Quá trình tạo ra thế hệ con cháu mới cùng loài (vô tính hoặc hữu tính).</p>
            </div>

            <div id="card-excretion" class="lecture-interactive-card" data-lecture-section="card_excretion" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #8b5cf6; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #6b21a8; font-size: 17px;">🚽 Excretion (Bài tiết)</h4>
                    <span style="font-size: 11px; color: #7c3aed; background: #f5f3ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Loại bỏ các <b>chất thải chuyển hóa (metabolic waste)</b> và các chất dư thừa so với nhu cầu cơ thể.</p>
            </div>

            <div id="card-nutrition" class="lecture-interactive-card" data-lecture-section="card_nutrition" style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 4px solid #14b8a6; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0 0 5px 0; color: #0f766e; font-size: 17px;">🍎 Nutrition (Dinh dưỡng)</h4>
                    <span style="font-size: 11px; color: #0f766e; background: #f0fdfa; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 13px; color: #475569; margin: 0;">Lấy các chất vật chất để cung cấp năng lượng, phục vụ cho sự sinh trưởng và phát triển cơ thể.</p>
            </div>
        </div>

        <!-- 3D INTERACTIVE FLIPCARDS -->
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 35px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <h3 style="margin: 0; color: #0f172a; font-size: 20px;">🧬 1.2. Thẻ ghi nhớ Flashcards (MRS GREN)</h3>
                <span style="font-size: 13px; color: #64748b; font-style: italic;">Di chuột hoặc chạm vào thẻ để lật mặt sau</span>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 15px; justify-content: center;">
                <!-- M -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #e0f2fe; background: linear-gradient(135deg, #f0f9ff, #e0f2fe); color: #0284c7;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">M</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Movement</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #0ea5e9; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #0284c7;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Thay đổi vị trí hoặc chỗ ở của cơ thể.</div>
                        </div>
                    </div>
                </div>
                <!-- R -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #fee2e2; background: linear-gradient(135deg, #fef2f2, #fee2e2); color: #dc2626;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">R</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Respiration</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #ef4444; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #dc2626;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Phản ứng giải phóng năng lượng trao đổi chất.</div>
                        </div>
                    </div>
                </div>
                <!-- S -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #fef3c7; background: linear-gradient(135deg, #fffbeb, #fef3c7); color: #d97706;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">S</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Sensitivity</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #f59e0b; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #d97706;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Nhận biết và phản ứng với kích thích môi trường.</div>
                        </div>
                    </div>
                </div>
                <!-- G -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #dcfce7; background: linear-gradient(135deg, #f0fdf4, #dcfce7); color: #16a34a;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">G</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Growth</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #10b981; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #16a34a;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Gia tăng vĩnh viễn kích thước và khối lượng khô.</div>
                        </div>
                    </div>
                </div>
                <!-- R2 -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #fce7f3; background: linear-gradient(135deg, #fdf2f8, #fce7f3); color: #db2777;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">R</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Reproduction</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #ec4899; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #db2777;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Quá trình sinh sản tạo ra cá thể cùng loài.</div>
                        </div>
                    </div>
                </div>
                <!-- E -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #ede9fe; background: linear-gradient(135deg, #f5f3ff, #ede9fe); color: #7c3aed;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">E</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Excretion</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #8b5cf6; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #7c3aed;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Đào thải các chất độc sinh ra từ chuyển hóa.</div>
                        </div>
                    </div>
                </div>
                <!-- N -->
                <div style="background-color: transparent; width: 150px; height: 160px; perspective: 1000px;" onmouseenter="this.firstElementChild.style.transform='rotateY(180deg)'" onmouseleave="this.firstElementChild.style.transform='rotateY(0deg)'">
                    <div style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; cursor: pointer;">
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 2px solid #cffafe; background: linear-gradient(135deg, #ecfeff, #cffafe); color: #0891b2;">
                            <h2 style="font-size: 2.8rem; margin: 0; line-height: 1;">N</h2>
                            <p style="font-size: 0.95rem; margin: 8px 0 0 0; font-weight: bold; text-transform: uppercase;">Nutrition</p>
                        </div>
                        <div style="position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 12px; padding: 12px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #06b6d4; color: #ffffff; transform: rotateY(180deg); text-align: left; border: 2px solid #0891b2;">
                            <div style="font-size: 0.8rem; font-weight: 600; line-height: 1.3;">Thu nhận dinh dưỡng cho năng lượng và lớn lên.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- EXCRETION ORGANS & EXAM TRAPS -->
        <div style="margin-bottom: 30px;">
            <div id="sec-excretion-organs" class="lecture-interactive-card" data-lecture-section="sec_excretion_organs" style="border-bottom: 2px solid #0284c7; padding-bottom: 8px; margin-bottom: 20px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="margin: 0; color: #0369a1; font-size: 20px;">💧 Cơ quan bài tiết chính ở người</h3>
                    <span style="font-size: 12px; color: #0284c7; font-weight: 600; background: #e0f2fe; padding: 3px 8px; border-radius: 10px;">🎧 Nghe giảng phần này</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px; margin-bottom: 25px;">
                <div id="card-skin" class="lecture-interactive-card" data-lecture-section="card_skin" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #0284c7; font-size: 16px;">✋ Skin (Da)</h4>
                        <span style="font-size: 11px; color: #0284c7; background: #e0f2fe; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 14px; color: #475569;">Bài tiết <b>mồ hôi</b>, chứa nước dư thừa, muối khoáng và một lượng nhỏ urê; tham gia điều hòa thân nhiệt.</p>
                </div>
                <div id="card-kidneys" class="lecture-interactive-card" data-lecture-section="card_kidneys" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #0284c7; font-size: 16px;">🫘 Kidneys (Thận)</h4>
                        <span style="font-size: 11px; color: #0284c7; background: #e0f2fe; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 14px; color: #475569;">Bài tiết <b>nước tiểu</b>, lọc urê từ gan, các ion muối khoáng dư thừa và nước khỏi máu.</p>
                </div>
                <div id="card-lungs" class="lecture-interactive-card" data-lecture-section="card_lungs" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #0284c7; font-size: 16px;">🫁 Lungs (Phổi)</h4>
                        <span style="font-size: 11px; color: #0284c7; background: #e0f2fe; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 14px; color: #475569;">Bài tiết <b>carbon dioxide (CO₂)</b> và hơi nước sinh ra từ quá trình hô hấp hiếu khí của tế bào.</p>
                </div>
            </div>

            <div id="sec-key-terms" class="lecture-interactive-card" data-lecture-section="sec_key_terms" style="border-bottom: 2px solid #ea580c; padding-bottom: 8px; margin-bottom: 20px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="margin: 0; color: #c2410c; font-size: 20px;">📌 Thuật ngữ cốt lõi: Ingestion vs Egestion</h3>
                    <span style="font-size: 12px; color: #c2410c; font-weight: 600; background: #ffedd5; padding: 3px 8px; border-radius: 10px;">🎧 Nghe giảng phần này</span>
                </div>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 15px;">
                <div style="flex: 1; min-width: 260px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 8px; padding: 15px;">
                    <h4 style="margin: 0 0 5px 0; color: #c2410c;">Ingestion (Sự ăn/nuốt)</h4>
                    <p style="margin: 0; font-size: 14px; color: #7c2d12;">Hành động đưa thức ăn và nước uống vào trong cơ thể qua miệng.</p>
                </div>
                <div style="flex: 1; min-width: 260px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 8px; padding: 15px;">
                    <h4 style="margin: 0 0 5px 0; color: #c2410c;">Egestion (Sự thải bã / Tống phân)</h4>
                    <p style="margin: 0; font-size: 14px; color: #7c2d12;">Đào thải các chất cặn bã không được tiêu hóa hoặc hấp thu ra khỏi cơ thể qua hậu môn dưới dạng phân.</p>
                </div>
            </div>
            <div id="card-trap-egestion" class="lecture-interactive-card" data-lecture-section="card_trap_egestion" style="background: #fef2f2; border-left: 5px solid #ef4444; padding: 18px; border-radius: 8px; cursor: pointer; box-shadow: 0 2px 4px rgba(239,68,68,0.06);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h4 style="margin: 0; color: #b91c1c; font-size: 16px;">⚠️ Cảnh báo Bẫy đề thi: Egestion KHÔNG PHẢI là Excretion!</h4>
                    <span style="font-size: 11px; color: #b91c1c; background: #fee2e2; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio Bẫy thi</span>
                </div>
                <p style="margin: 0; color: #991b1b; font-size: 14px; line-height: 1.6;">
                    • <b>Excretion (Bài tiết)</b> là quá trình loại bỏ các chất thải chuyển hóa sinh ra <i>bên trong tế bào</i> (ví dụ: urê, CO₂).<br>
                    • <b>Egestion (Tống phân)</b> chỉ là việc tống khứ các chất thải đi <i>xuyên qua ống tiêu hóa</i> mà chưa từng đi vào tế bào hay tham gia bất kỳ phản ứng sinh hóa nào.
                </p>
            </div>
        </div>
    </div>

    <!-- 2.1. CLASSIFICATION SYSTEMS & IDENTIFICATION -->
    <div style="margin-bottom: 50px;">
        <div id="sec-classification" class="lecture-interactive-card" data-lecture-section="sec_classification" style="border-bottom: 3px solid #3b82f6; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🏷️ 2.1. HỆ THỐNG PHÂN LOẠI &amp; NHẬN DIỆN SINH VẬT</h2>
                <span style="font-size: 12px; color: #1d4ed8; font-weight: 600; background: #eff6ff; padding: 4px 10px; border-radius: 12px; border: 1px solid #bfdbfe;">🎧 Nghe giảng phần này</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Phân loại học phản ánh mối quan hệ họ hàng tiến hóa. Các loài có họ hàng gần gũi sẽ có trình tự nucleotide trên DNA giống nhau hơn.</p>
        </div>

        <!-- SPECIES & BINOMIAL SYSTEM -->
        <div style="display: flex; flex-direction: column; gap: 20px; margin-bottom: 30px;">
            <div id="sec-species" class="lecture-interactive-card" data-lecture-section="sec_species" style="background: #e0f2fe; border: 1px solid #bae6fd; border-left: 5px solid #0ea5e9; border-radius: 8px; padding: 18px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h3 style="margin: 0; color: #0284c7; font-size: 18px;">🔑 Định nghĩa chuẩn Cambridge: Species (Loài)</h3>
                    <span style="font-size: 11px; color: #0284c7; background: #bae6fd; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="margin: 0; font-size: 15px; color: #0f172a;">A <strong>species</strong> is a group of organisms that can reproduce to produce <strong>fertile offspring</strong>.</p>
                <p style="margin: 5px 0 0 0; font-size: 14px; color: #475569;"><em>(Loài là một nhóm các sinh vật có khả năng giao phối sinh sản với nhau để tạo ra con non có khả năng sinh sản).</em></p>
            </div>

            <div id="sec-binomial" class="lecture-interactive-card" data-lecture-section="sec_binomial" style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 12px; padding: 20px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h3 style="margin: 0; color: #1e40af; font-size: 18px;">Hệ thống danh pháp Nhị phân (Binomial System)</h3>
                    <span style="font-size: 11px; color: #1d4ed8; background: #dbeafe; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                </div>
                <p style="font-size: 15px; color: #475569; margin-bottom: 15px;">Hệ thống quốc tế đặt tên cho các loài bằng hai từ la-tinh: từ thứ nhất là tên <b>Genus (Chi)</b>, từ thứ hai là tên <b>species (Loài)</b>.</p>
                <div style="background: #ffffff; padding: 15px; border-radius: 8px; border: 2px dashed #93c5fd; text-align: center;">
                    <p style="margin: 0 0 5px 0; font-size: 14px; color: #1e3a8a;">Ví dụ: Tên khoa học của Sư tử là</p>
                    <p style="margin: 0; font-size: 26px; font-weight: bold; font-style: italic; color: #1d4ed8;">Panthera leo</p>
                    <div style="display: flex; justify-content: center; gap: 40px; margin-top: 10px; font-size: 13px; font-weight: bold;">
                        <span style="color: #2563eb;">Chi / Giống: Panthera</span>
                        <span style="color: #059669;">Loài: leo</span>
                    </div>
                </div>
            </div>

            <!-- EXAM RULES -->
            <div style="display: flex; flex-wrap: wrap; gap: 20px;">
                <div id="card-rule-typography" class="lecture-interactive-card" data-lecture-section="card_rule_typography" style="flex: 1; min-width: 280px; background: #fefce8; border: 2px solid #fde047; border-radius: 8px; padding: 18px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <h4 style="margin: 0; color: #a16207; font-size: 17px;">🚨 BẪY ĐỀ THI 1: Quy tắc Viết tên</h4>
                        <span style="font-size: 11px; color: #a16207; background: #fef08a; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #713f12; line-height: 1.8;">
                        <li>Tên Genus (Chi) luôn bắt đầu bằng chữ <strong>IN HOA</strong> (vd: <em>Panthera</em>).</li>
                        <li>Tên species (Loài) luôn bắt đầu bằng chữ <strong>viết thường</strong> (vd: <em>leo</em>).</li>
                        <li>Khi gõ máy phải <em>in nghiêng (italics)</em>, khi viết tay phải <span style="text-decoration: underline;">gạch chân riêng biệt</span> từng từ (vd: <u>Panthera</u> <u>leo</u>).</li>
                    </ul>
                </div>

                <div id="card-rule-viruses" class="lecture-interactive-card" data-lecture-section="card_rule_viruses" style="flex: 1; min-width: 280px; background: #fef2f2; border: 2px solid #fecaca; border-radius: 8px; padding: 18px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <h4 style="margin: 0; color: #b91c1c; font-size: 17px;">🚨 BẪY ĐỀ THI 2: Virus nằm ở đâu?</h4>
                        <span style="font-size: 11px; color: #b91c1c; background: #fee2e2; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="font-size: 14px; color: #7f1d1d; margin-bottom: 10px;">Giám khảo hỏi: <em>"Tại sao Virus không được xếp vào bất kỳ Giới nào trong 5 Giới?"</em></p>
                    <p style="font-size: 14px; color: #991b1b; margin: 0; font-weight: bold;">➔ Trả lời chuẩn: Vì Virus không có cấu tạo tế bào (Not cellular). Chúng chỉ gồm vỏ protein bao bọc phân tử DNA/RNA và chỉ nhân lên trong tế bào chủ sống.</p>
                </div>
            </div>
        </div>

        <!-- THE FIVE KINGDOMS TABLE -->
        <div id="sec-five-kingdoms" class="lecture-interactive-card" data-lecture-section="sec_five_kingdoms" style="background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 5px solid #22c55e; border-radius: 12px; padding: 25px; margin-bottom: 30px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <h3 style="margin: 0; color: #15803d; font-size: 20px;">🌍 Hệ thống 5 Giới (The Five Kingdoms)</h3>
                <span style="font-size: 11px; color: #15803d; background: #dcfce7; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Nghe giảng 5 Giới</span>
            </div>
            <p style="margin: 0 0 15px 0; font-size: 15px; color: #166534;">Dựa trên cấu tạo tế bào và phương thức dinh dưỡng, tất cả sinh vật nhân thực và nhân sơ được phân loại vào 5 giới:</p>
            <div style="overflow-x: auto; background: #ffffff; border-radius: 8px; border: 1px solid #dcfce7;">
                <table style="width: 100%; border-collapse: collapse; min-width: 650px; text-align: left; font-size: 14px;">
                    <thead>
                        <tr style="background-color: #dcfce7; border-bottom: 2px solid #bbf7d0;">
                            <th style="padding: 10px; color: #14532d; font-weight: bold;">Kingdom (Giới)</th>
                            <th style="padding: 10px; color: #14532d; font-weight: bold;">Cấu tạo tế bào</th>
                            <th style="padding: 10px; color: #14532d; font-weight: bold;">Màng nhân</th>
                            <th style="padding: 10px; color: #14532d; font-weight: bold;">Thành tế bào</th>
                            <th style="padding: 10px; color: #14532d; font-weight: bold;">Phương thức dinh dưỡng</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px; font-weight: bold; color: #0284c7;">1. Animals (Động vật)</td>
                            <td style="padding: 10px; color: #475569;">Đa bào</td>
                            <td style="padding: 10px; color: #475569;">Có nhân thực</td>
                            <td style="padding: 10px; color: #475569;">Không có</td>
                            <td style="padding: 10px; color: #475569;">Dị dưỡng (tiêu thụ sinh vật khác). Không có lục lạp.</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; background-color: #f8fafc;">
                            <td style="padding: 10px; font-weight: bold; color: #16a34a;">2. Plants (Thực vật)</td>
                            <td style="padding: 10px; color: #475569;">Đa bào</td>
                            <td style="padding: 10px; color: #475569;">Có nhân thực</td>
                            <td style="padding: 10px; color: #475569;">Cellulose</td>
                            <td style="padding: 10px; color: #475569;">Tự dưỡng (quang hợp nhờ lục lạp).</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px; font-weight: bold; color: #d97706;">3. Fungi (Nấm)</td>
                            <td style="padding: 10px; color: #475569;">Đa bào hoặc đơn bào</td>
                            <td style="padding: 10px; color: #475569;">Có nhân thực</td>
                            <td style="padding: 10px; color: #475569;">Chitin</td>
                            <td style="padding: 10px; color: #475569;">Hoại sinh qua sợi nấm (hyphae). Không có lục lạp.</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; background-color: #f8fafc;">
                            <td style="padding: 10px; font-weight: bold; color: #8b5cf6;">4. Prokaryotes (Khởi sinh)</td>
                            <td style="padding: 10px; color: #475569;">Đơn bào</td>
                            <td style="padding: 10px; color: #475569;">Không có nhân thực</td>
                            <td style="padding: 10px; color: #475569;">Peptidoglycan</td>
                            <td style="padding: 10px; color: #475569;">DNA vòng trần, plasmid, không có bào quan màng.</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px; font-weight: bold; color: #06b6d4;">5. Protoctists (Nguyên sinh)</td>
                            <td style="padding: 10px; color: #475569;">Đa số đơn bào</td>
                            <td style="padding: 10px; color: #475569;">Có nhân thực</td>
                            <td style="padding: 10px; color: #475569;">Tùy loài</td>
                            <td style="padding: 10px; color: #475569;">Rất đa dạng (giống động vật như Amoeba hoặc giống tảo).</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div style="margin-top: 15px; background: #ecfdf5; border-radius: 6px; padding: 12px; font-size: 13px; color: #065f46;">
                <strong>🧬 Phân loại học hiện đại (Kiến thức Nâng cao):</strong> Việc phân loại chính xác dựa vào so sánh <b>trình tự base trên DNA</b> hoặc trình tự axit amin trên protein. Các loài có trình tự giống nhau hơn chứng tỏ có tổ tiên chung gần hơn.
            </div>
        </div>

        <!-- DICHOTOMOUS KEYS -->
        <div id="sec-dichotomous" class="lecture-interactive-card" data-lecture-section="sec_dichotomous" style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <h3 style="margin: 0; color: #0f172a; font-size: 20px;">🔍 Dichotomous keys (Khóa lưỡng phân)</h3>
                <span style="font-size: 11px; color: #0284c7; background: #e0f2fe; padding: 2px 8px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin-bottom: 15px;">Khóa lưỡng phân là công cụ dùng để nhận diện sinh vật chưa biết qua một chuỗi các cặp đặc điểm hình thái đối lập nhau (Có hoặc Không).</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px;">
                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px; font-size: 13px; line-height: 1.8;">
                    <strong>📝 Dạng 1: Danh sách câu hỏi từng bước</strong><br>
                    1 a) Có cánh ........................................... Đi tiếp bước 2<br>
                    &nbsp;&nbsp;&nbsp;b) Không có cánh ............................ Đi tiếp bước 3<br>
                    2 a) Chỉ có 1 cặp cánh (2 cánh) ..... Con Ruồi (Fly)<br>
                    &nbsp;&nbsp;&nbsp;b) Có 2 cặp cánh (4 cánh) ........... Con Bướm (Butterfly)
                </div>
                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px; font-size: 13px; line-height: 1.8;">
                    <strong>🔀 Dạng 2: Sơ đồ nhánh nhận diện</strong><br>
                    • Ở mỗi điểm rẽ nhánh, người quan sát chỉ trả lời Đúng hoặc Sai theo đặc điểm hình thái.<br>
                    • Đi theo mũi tên đến khi tìm ra tên khoa học của loài sinh vật.
                </div>
            </div>
        </div>
    </div>

    <!-- 2.2. THE ANIMAL KINGDOM -->
    <div style="margin-bottom: 50px;">
        <div id="sec-animal-kingdom" class="lecture-interactive-card" data-lecture-section="sec_animal_kingdom" style="border-bottom: 3px solid #e11d48; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🦁 2.2. GIỚI ĐỘNG VẬT (THE ANIMAL KINGDOM)</h2>
                <span style="font-size: 12px; color: #e11d48; font-weight: 600; background: #ffe4e6; padding: 4px 10px; border-radius: 12px; border: 1px solid #fecdd3;">🎧 Nghe giảng phần này</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Giới Động vật gồm Động vật có xương sống (Vertebrates) và Động vật không xương sống (Invertebrates - trọng tâm là Arthropods).</p>
        </div>

        <!-- VERTEBRATES -->
        <div style="margin-bottom: 35px;">
            <div id="sec-vertebrates" class="lecture-interactive-card" data-lecture-section="sec_vertebrates" style="border-left: 4px solid #be123c; padding-left: 10px; margin-bottom: 15px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="color: #be123c; font-size: 19px; margin: 0;">🦴 Động vật có xương sống (Vertebrates - 5 Lớp)</h3>
                    <span style="font-size: 11px; color: #be123c; background: #ffe4e6; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio Tổng quan</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
                <div id="card-fish" class="lecture-interactive-card" data-lecture-section="card_fish" style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #9f1239; font-size: 16px;">🐟 Fish (Cá)</h4>
                        <span style="font-size: 11px; color: #9f1239; background: #ffe4e6; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #881337; line-height: 1.5;">Vảy nhớt ẩm ướt, hô hấp bằng mang, vây bơi, đẻ trứng có màng nhầy trong nước.</p>
                </div>
                <div id="card-amphibians" class="lecture-interactive-card" data-lecture-section="card_amphibians" style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #9f1239; font-size: 16px;">🐸 Amphibians (Lưỡng cư)</h4>
                        <span style="font-size: 11px; color: #9f1239; background: #ffe4e6; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #881337; line-height: 1.5;">Da ẩm không vảy, trao đổi khí qua da; ấu trùng thở bằng mang, con trưởng thành thở bằng phổi.</p>
                </div>
                <div id="card-reptiles" class="lecture-interactive-card" data-lecture-section="card_reptiles" style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #9f1239; font-size: 16px;">🦎 Reptiles (Bò sát)</h4>
                        <span style="font-size: 11px; color: #9f1239; background: #ffe4e6; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #881337; line-height: 1.5;">Da khô phủ vảy sừng chống mất nước, thở bằng phổi, đẻ trứng có vỏ dai trên cạn.</p>
                </div>
                <div id="card-birds" class="lecture-interactive-card" data-lecture-section="card_birds" style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #9f1239; font-size: 16px;">🦅 Birds (Chim)</h4>
                        <span style="font-size: 11px; color: #9f1239; background: #ffe4e6; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #881337; line-height: 1.5;">Lông vũ bao phủ, có cánh, mỏ sừng không răng, hằng nhiệt, đẻ trứng vỏ vôi cứng.</p>
                </div>
                <div id="card-mammals" class="lecture-interactive-card" data-lecture-section="card_mammals" style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #9f1239; font-size: 16px;">🐆 Mammals (Thú)</h4>
                        <span style="font-size: 11px; color: #9f1239; background: #ffe4e6; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #881337; line-height: 1.5;">Lông mao, có tuyến sữa nuôi con, vành tai ngoài (pinna), răng phân hóa, sinh con non.</p>
                </div>
            </div>
        </div>

        <!-- ARTHROPODS -->
        <div>
            <div id="sec-arthropods" class="lecture-interactive-card" data-lecture-section="sec_arthropods" style="border-left: 4px solid #c026d3; padding-left: 10px; margin-bottom: 15px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="color: #c026d3; font-size: 19px; margin: 0;">🦑 Động vật chân khớp (Arthropods)</h3>
                    <span style="font-size: 11px; color: #c026d3; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio Tổng quan</span>
                </div>
            </div>
            <p style="font-size: 14px; color: #475569; margin-bottom: 15px;">Tất cả chân khớp đều có bộ xương ngoài bằng chất <strong>chitin</strong> chống thấm nước, cơ thể phân đốt và các cặp chân có khớp nối.</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px;">
                <div id="card-insects" class="lecture-interactive-card" data-lecture-section="card_insects" style="background: #fdf4ff; border: 1px solid #f0abfc; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #a21caf; font-size: 16px;">🐜 Insects (Côn trùng)</h4>
                        <span style="font-size: 11px; color: #a21caf; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #701a75; line-height: 1.6;">• Cơ thể 3 phần (đầu, ngực, bụng)<br>• 3 cặp chân gắn ở ngực (6 chân)<br>• 1 cặp râu, thường có 2 cặp cánh</p>
                </div>
                <div id="card-arachnids" class="lecture-interactive-card" data-lecture-section="card_arachnids" style="background: #fdf4ff; border: 1px solid #f0abfc; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #a21caf; font-size: 16px;">🕷️ Arachnids (Lớp Nhện)</h4>
                        <span style="font-size: 11px; color: #a21caf; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #701a75; line-height: 1.6;">• Cơ thể 2 phần (đầu ngực liền và bụng)<br>• 4 cặp chân bò (8 chân)<br>• Không râu, không cánh, có kìm chelicerae</p>
                </div>
                <div id="card-crustaceans" class="lecture-interactive-card" data-lecture-section="card_crustaceans" style="background: #fdf4ff; border: 1px solid #f0abfc; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #a21caf; font-size: 16px;">🦀 Crustaceans (Giáp xác)</h4>
                        <span style="font-size: 11px; color: #a21caf; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #701a75; line-height: 1.6;">• Từ 5 cặp chân trở lên (thường có càng)<br>• 2 cặp râu, thở bằng mang<br>• Đa số sống dưới nước (tôm, cua)</p>
                </div>
                <div id="card-myriapods" class="lecture-interactive-card" data-lecture-section="card_myriapods" style="background: #fdf4ff; border: 1px solid #f0abfc; border-radius: 8px; padding: 15px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0 0 5px 0; color: #a21caf; font-size: 16px;">🐛 Myriapods (Đa túc)</h4>
                        <span style="font-size: 11px; color: #a21caf; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #701a75; line-height: 1.6;">• Cơ thể gồm nhiều đốt giống nhau<br>• Rết: 1 cặp chân/đốt (ăn thịt nhanh)<br>• Cuốn chiếu: 2 cặp chân/đốt (ăn thực vật)</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 2.3. THE PLANT KINGDOM & OTHER KINGDOMS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-plant-kingdom" class="lecture-interactive-card" data-lecture-section="sec_plant_kingdom" style="border-bottom: 3px solid #16a34a; padding-bottom: 10px; margin-bottom: 25px; cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <h2 style="color: #0f172a; margin: 0; font-size: 24px;">🌿 2.3. GIỚI THỰC VẬT: CÂY MỘT LÁ MẦM VS HAI LÁ MẦM</h2>
                <span style="font-size: 12px; color: #15803d; font-weight: 600; background: #ecfdf5; padding: 4px 10px; border-radius: 12px; border: 1px solid #a7f3d0;">🎧 Nghe giảng phần này</span>
            </div>
            <p style="font-size: 15px; color: #475569; margin: 8px 0 0 0;">Thực vật có hoa được chia thành hai nhóm chính: Monocotyledons (Một lá mầm) và Dicotyledons (Hai lá mầm).</p>
        </div>

        <div style="display: flex; flex-wrap: wrap; gap: 25px; align-items: stretch; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 35px;">
            <!-- SVG DIAGRAM -->
            <div style="flex: 1; min-width: 280px; max-width: 400px; text-align: center; display: flex; flex-direction: column; justify-content: center;">
                <h4 style="margin: 0 0 10px 0; color: #15803d; font-size: 16px;">Sơ đồ tương tác Monocots vs Dicots</h4>
                <p style="font-size: 13px; color: #64748b; margin-bottom: 15px;">Di chuột vào hình để đổi góc nhìn:</p>
                <svg viewBox="0 0 300 200" width="100%" height="auto" style="display: block; margin: 0 auto;">
                    <g style="cursor: pointer; transition: 0.2s;" onmouseover="document.getElementById('card-monocots').style.display='block'; document.getElementById('card-dicots').style.display='none';">
                        <rect x="20" y="20" width="120" height="160" rx="8" fill="#f0fdf4" stroke="#4ade80" stroke-width="2"></rect>
                        <path d="M 80 40 Q 50 100 80 160 Q 110 100 80 40 Z" fill="#bbf7d0"></path>
                        <path d="M 70 50 L 70 150 M 80 45 L 80 155 M 90 50 L 90 150" stroke="#16a34a" stroke-width="2"></path>
                        <text x="80" y="150" font-family="Arial" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">Một lá mầm</text>
                    </g>
                    <g style="cursor: pointer; transition: 0.2s;" onmouseover="document.getElementById('card-monocots').style.display='none'; document.getElementById('card-dicots').style.display='block';">
                        <rect x="160" y="20" width="120" height="160" rx="8" fill="#fdf4ff" stroke="#e879f9" stroke-width="2"></rect>
                        <circle cx="220" cy="80" r="35" fill="#f5d0fe"></circle>
                        <path d="M 220 50 L 220 110 M 195 80 L 245 80" stroke="#c026d3" stroke-width="2"></path>
                        <text x="220" y="150" font-family="Arial" font-size="12" font-weight="bold" fill="#a21caf" text-anchor="middle">Hai lá mầm</text>
                    </g>
                </svg>
            </div>

            <!-- MONOCOTS & DICOTS DETAILS (BOTH CLICKABLE) -->
            <div style="flex: 1.5; min-width: 320px; display: flex; flex-direction: column; gap: 15px;">
                <div id="card-monocots" class="lecture-interactive-card" data-lecture-section="card_monocots" style="background: #f0fdf4; border-left: 5px solid #22c55e; border-radius: 8px; padding: 20px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h4 style="margin: 0; color: #15803d; font-size: 18px;">🌱 Monocotyledons (Cây một lá mầm)</h4>
                        <span style="font-size: 11px; color: #15803d; background: #dcfce7; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #14532d; line-height: 1.8;">
                        <li><strong>Hạt:</strong> Chỉ chứa 1 lá mầm (1 cotyledon) bên trong. <em>(Vd: Lúa, ngô, cỏ).</em></li>
                        <li><strong>Lá:</strong> Dài, hẹp với hệ <strong>gân lá song song (parallel veins)</strong>.</li>
                        <li><strong>Rễ:</strong> Hệ rễ chùm (fibrous root system).</li>
                        <li><strong>Hoa:</strong> Các bộ phận của hoa (cánh hoa) thường là <strong>bội số của 3</strong> (3, 6, 9 cánh).</li>
                    </ul>
                </div>

                <div id="card-dicots" class="lecture-interactive-card" data-lecture-section="card_dicots" style="background: #fdf4ff; border-left: 5px solid #d946ef; border-radius: 8px; padding: 20px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h4 style="margin: 0; color: #a21caf; font-size: 18px;">🌳 Dicotyledons (Cây hai lá mầm)</h4>
                        <span style="font-size: 11px; color: #a21caf; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #701a75; line-height: 1.8;">
                        <li><strong>Hạt:</strong> Chứa 2 lá mầm (2 cotyledons) bên trong. <em>(Vd: Đậu, lạc, hoa hồng, sồi).</em></li>
                        <li><strong>Lá:</strong> Bản rộng với hệ <strong>gân lá phân nhánh mạng lưới (branching/net-like veins)</strong>.</li>
                        <li><strong>Rễ:</strong> Hệ rễ cọc chính (taproot) với các rễ bên nhỏ hơn.</li>
                        <li><strong>Hoa:</strong> Các bộ phận của hoa thường là <strong>bội số của 4 hoặc 5</strong> (4, 5, 8, 10 cánh).</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- 2.4. OTHER KINGDOMS -->
        <div>
            <h3 style="color: #0f172a; margin: 0 0 15px 0; font-size: 20px;">🦠 Các Giới khác: Nấm, Khởi sinh &amp; Nguyên sinh</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 15px;">
                <div id="card-fungi" class="lecture-interactive-card" data-lecture-section="card_fungi" style="flex: 1; min-width: 260px; background: #fffbeb; border: 2px solid #fcd34d; border-radius: 10px; padding: 20px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h4 style="margin: 0; color: #b45309; font-size: 16px;">🍄 Fungi (Giới Nấm)</h4>
                        <span style="font-size: 11px; color: #b45309; background: #fef3c7; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <ul style="margin: 0; padding-left: 18px; font-size: 13px; color: #78350f; line-height: 1.7;">
                        <li>Đa bào (nấm mốc, nấm rơm) hoặc đơn bào (nấm men Yeast); có nhân thực.</li>
                        <li>Thành tế bào cấu tạo từ <strong>chitin</strong> (không phải cellulose).</li>
                        <li>Không có lục lạp; dinh dưỡng hoại sinh qua hệ sợi nấm (hyphae).</li>
                    </ul>
                </div>

                <div id="card-prokaryotes" class="lecture-interactive-card" data-lecture-section="card_prokaryotes" style="flex: 1; min-width: 260px; background: #fdf4ff; border: 2px solid #f0abfc; border-radius: 10px; padding: 20px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h4 style="margin: 0; color: #a21caf; font-size: 16px;">Prokaryotes (Khởi sinh / Vi khuẩn)</h4>
                        <span style="font-size: 11px; color: #a21caf; background: #fae8ff; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <ul style="margin: 0; padding-left: 18px; font-size: 13px; color: #4a044e; line-height: 1.7;">
                        <li>Cơ thể đơn bào; <strong>không có màng nhân thật</strong>.</li>
                        <li>DNA vòng trần nằm tự do trong tế bào chất cùng plasmid.</li>
                        <li>Thành tế bào bằng peptidoglycan; không có ti thể/lục lạp.</li>
                    </ul>
                </div>

                <div id="card-protoctists" class="lecture-interactive-card" data-lecture-section="card_protoctists" style="flex: 1; min-width: 260px; background: #ecfdf5; border: 2px solid #6ee7b7; border-radius: 10px; padding: 20px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h4 style="margin: 0; color: #047857; font-size: 16px;">Protoctists (Nguyên sinh vật)</h4>
                        <span style="font-size: 11px; color: #047857; background: #dcfce7; padding: 2px 6px; border-radius: 10px; font-weight: 600;">🎧 Audio</span>
                    </div>
                    <ul style="margin: 0; padding-left: 18px; font-size: 13px; color: #064e3b; line-height: 1.7;">
                        <li>Có nhân thực; đa số đơn bào (một số như rong biển là đa bào).</li>
                        <li>Rất đa dạng: một số dị dưỡng giống động vật (<em>Amoeba</em>), một số quang hợp có lục lạp (<em>Chlorella</em>).</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

</div>'''
    return html

def verify_div_balance(name, html):
    open_count = html.count('<div')
    close_count = html.count('</div>')
    diff = open_count - close_count
    print(f"[{name}] <div: {open_count}, </div: {close_count} -> Diff: {diff}")
    assert diff == 0, f"Div mismatch in {name}!"

if __name__ == '__main__':
    p1 = build_page_1_html()
    p2 = build_page_2_html()
    verify_div_balance("Page 1 (English)", p1)
    verify_div_balance("Page 2 (Bilingual)", p2)

    os.makedirs('scripts/output_bio', exist_ok=True)
    with open('scripts/output_bio/merged_page_1.html', 'w', encoding='utf-8') as f:
        f.write(p1)
    with open('scripts/output_bio/merged_page_2.html', 'w', encoding='utf-8') as f:
        f.write(p2)
    print("Files successfully generated in scripts/output_bio/!")
