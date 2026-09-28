import sys
import os
import re
from bs4 import BeautifulSoup

sys.path.append('scripts')
from audio_lecture_engine import sb

def check_balance(html):
    o = len(re.findall(r'<div\b', html, re.I))
    c = len(re.findall(r'</div>', html, re.I))
    return o - c

def fix_6_1():
    lid = 'c6fccfc5-088b-4145-9a23-9cbb2df1cce9'
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    # In 6.1, the second card-fertility-factors should be card-dtm-evaluation
    # Find the second occurrence of card-fertility-factors
    pattern = r'(id="card-fertility-factors"\s+class="[^"]*"\s+data-lecture-section="fertility_factors")'
    matches = list(re.finditer(pattern, html))
    if len(matches) >= 2:
        m2 = matches[1]
        replacement = 'id="card-dtm-evaluation" class="lecture-interactive-card" data-lecture-section="dtm_evaluation"'
        html = html[:m2.start()] + replacement + html[m2.end():]
        print("6.1: Successfully replaced duplicate card-fertility-factors with card-dtm-evaluation")
    else:
        print("6.1: Warning - could not find 2 occurrences of card-fertility-factors")
        
    diff = check_balance(html)
    assert diff == 0, f"6.1 Div balance mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("6.1: Updated in DB.")

def fix_7_2():
    lid = '30bae547-a9b0-4c09-8850-ce22b96cfea2'
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    # 1. Hero header
    hero_pattern = r'(<!-- HERO HEADER -->\s*<div style="background:\s*linear-gradient\(135deg,\s*#0f766e[^"]*"\s*>)'
    if re.search(hero_pattern, html):
        html = re.sub(
            hero_pattern,
            r'<!-- HERO HEADER -->\n  <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f766e 0%, #0d9488 60%, #14b8a6 100%); color:#ffffff; padding:32px 28px; border-radius:16px; margin-bottom:32px; box-shadow:0 10px 25px -5px rgba(13, 148, 136, 0.25); cursor:pointer;">',
            html
        )
        print("7.2: Tagged #sec-header")
    else:
        # direct string replacement
        old_hero = '<div style="background: linear-gradient(135deg, #0f766e 0%, #0d9488 60%, #14b8a6 100%); color:#ffffff; padding:32px 28px; border-radius:16px; margin-bottom:32px; box-shadow:0 10px 25px -5px rgba(13, 148, 136, 0.25);">'
        new_hero = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f766e 0%, #0d9488 60%, #14b8a6 100%); color:#ffffff; padding:32px 28px; border-radius:16px; margin-bottom:32px; box-shadow:0 10px 25px -5px rgba(13, 148, 136, 0.25); cursor:pointer;">'
        if old_hero in html:
            html = html.replace(old_hero, new_hero)
            print("7.2: Tagged #sec-header (exact)")

    # 2. Economic drivers & social benefits
    old_econ = '<div style="background:#f0fdfa; border-left:4px solid #0d9488; padding:18px; border-radius:8px;">\n      <div style="font-weight:700; color:#115e59;'
    new_econ = '<div id="card-economic-drivers" class="lecture-interactive-card" data-lecture-section="economic_drivers" style="background:#f0fdfa; border-left:4px solid #0d9488; padding:18px; border-radius:8px; cursor:pointer;">\n      <div style="font-weight:700; color:#115e59;'
    if old_econ in html:
        html = html.replace(old_econ, new_econ)
        print("7.2: Tagged #card-economic-drivers")
        
    old_soc = '<div style="background:#eff6ff; border-left:4px solid #3b82f6; padding:18px; border-radius:8px;">\n      <div style="font-weight:700; color:#1d4ed8;'
    new_soc = '<div id="card-social-benefits" class="lecture-interactive-card" data-lecture-section="social_benefits" style="background:#eff6ff; border-left:4px solid #3b82f6; padding:18px; border-radius:8px; cursor:pointer;">\n      <div style="font-weight:700; color:#1d4ed8;'
    if old_soc in html:
        html = html.replace(old_soc, new_soc)
        print("7.2: Tagged #card-social-benefits")
        
    # 3. Land use models container
    old_lum = '<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05);">'
    new_lum = '<div id="card-land-use-models" class="lecture-interactive-card" data-lecture-section="land_use_models" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); cursor:pointer;">'
    if old_lum in html:
        html = html.replace(old_lum, new_lum, 1) # first occurrence is the land use models SVG box
        print("7.2: Tagged #card-land-use-models")
        
    diff = check_balance(html)
    assert diff == 0, f"7.2 Div balance mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("7.2: Updated in DB.")

def fix_7_3():
    lid = '0b658b3f-bf70-4991-95d5-d65616b7ec1a'
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    old_hero = '<div style="background: linear-gradient(135deg, #0f766e 0%, #0d9488 60%, #14b8a6 100%); color:#ffffff; padding:32px 28px; border-radius:16px; margin-bottom:32px; box-shadow:0 10px 25px -5px rgba(13, 148, 136, 0.25);">'
    new_hero = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f766e 0%, #0d9488 60%, #14b8a6 100%); color:#ffffff; padding:32px 28px; border-radius:16px; margin-bottom:32px; box-shadow:0 10px 25px -5px rgba(13, 148, 136, 0.25); cursor:pointer;">'
    if old_hero in html:
        html = html.replace(old_hero, new_hero)
        print("7.3: Tagged #sec-header")
        
    diff = check_balance(html)
    assert diff == 0, f"7.3 Div balance mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("7.3: Updated in DB.")

def fix_8_1():
    lid = '5ff5f837-df39-4488-bbd2-5138f4faed1e'
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    # 1. Hero header
    old_banner = '  <!-- Hero Banner -->\n  <div style="background: linear-gradient(135deg, #78350f 0%, #b45309 60%, #d97706 100%);'
    new_banner = '  <!-- Hero Banner -->\n  <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; background: linear-gradient(135deg, #78350f 0%, #b45309 60%, #d97706 100%);'
    if old_banner in html:
        html = html.replace(old_banner, new_banner)
        print("8.1: Tagged #sec-header")
        
    diff = check_balance(html)
    assert diff == 0, f"8.1 Div balance mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("8.1: Updated in DB.")

def fix_8_2():
    lid = '9cf90212-43f4-4b28-8014-fd6c130db8ef'
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    # 1. Hero header
    old_banner = '  <!-- Hero Banner -->\n  <div style="background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 60%, #3b82f6 100%);'
    new_banner = '  <!-- Hero Banner -->\n  <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 60%, #3b82f6 100%);'
    if old_banner in html:
        html = html.replace(old_banner, new_banner)
        print("8.2: Tagged #sec-header")
        
    diff = check_balance(html)
    assert diff == 0, f"8.2 Div balance mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("8.2: Updated in DB.")

def fix_8_3():
    lid = '7da208d1-559d-4e60-a6a3-ebfb8c2d232f'
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    # 1. Hero header
    old_banner = '  <!-- Hero Banner -->\n  <div style="background: linear-gradient(135deg, #064e3b 0%, #047857 60%, #10b981 100%);'
    new_banner = '  <!-- Hero Banner -->\n  <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; background: linear-gradient(135deg, #064e3b 0%, #047857 60%, #10b981 100%);'
    if old_banner in html:
        html = html.replace(old_banner, new_banner)
        print("8.3: Tagged #sec-header")
        
    diff = check_balance(html)
    assert diff == 0, f"8.3 Div balance mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("8.3: Updated in DB.")
        
    diff = check_balance(html)
    assert diff == 0, f"8.3 Div balance mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("8.3: Updated in DB.")

def fix_9_1():
    lid = '6c14f92b-774a-45d1-a68d-2e9fe5e0b85d'
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    # 1. Header
    old_h1 = '<h1>9.1 Changing employment structures</h1>'
    new_h1 = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; margin-bottom:20px;">\n        <h1 style="margin-top:0;">9.1 Changing employment structures</h1>\n    </div>'
    if old_h1 in html:
        html = html.replace(old_h1, new_h1)
        print("9.1: Tagged #sec-header")
        
    # 2. Triangular graph
    old_tri = '<div class="img-box" style="margin:24px 0; text-align:center;">\n    <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_11.png?v=3"'
    new_tri = '<div id="card-triangular-graph" class="img-box lecture-interactive-card" data-lecture-section="triangular_graph" style="margin:24px 0; text-align:center; cursor:pointer;">\n    <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_11.png?v=3"'
    if old_tri in html:
        html = html.replace(old_tri, new_tri)
        print("9.1: Tagged #card-triangular-graph")
        
    diff = check_balance(html)
    assert diff == 0, f"9.1 Div balance mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("9.1: Updated in DB.")

def fix_9_2():
    lid = '5b7da7e1-3da1-4bf4-9700-6e11d7a7ef6b'
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    # 1. Header
    old_h1 = '<h1>9.2 The impact of globalisation and the role of transnational corporations</h1>'
    new_h1 = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; margin-bottom:20px;">\n        <h1 style="margin-top:0;">9.2 The impact of globalisation and the role of transnational corporations</h1>\n    </div>'
    if old_h1 in html:
        html = html.replace(old_h1, new_h1)
        print("9.2: Tagged #sec-header")
        
    # 2. Globalisation factors
    old_glob = '<div class="img-box" style="margin:24px 0; text-align:center;">\n    <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_22.png?v=3"'
    new_glob = '<div id="card-globalisation-factors" class="img-box lecture-interactive-card" data-lecture-section="globalisation_factors" style="margin:24px 0; text-align:center; cursor:pointer;">\n    <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_22.png?v=3"'
    if old_glob in html:
        html = html.replace(old_glob, new_glob)
        print("9.2: Tagged #card-globalisation-factors")
        
    diff = check_balance(html)
    assert diff == 0, f"9.2 Div balance mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("9.2: Updated in DB.")

def fix_9_3():
    lid = '53517557-9eb4-450d-a8dd-18b73c71938a'
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    # 1. Header
    old_h1 = '<h1>9.3 Tourism is a growing industry</h1>'
    new_h1 = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; margin-bottom:20px;">\n        <h1 style="margin-top:0;">9.3 Tourism is a growing industry</h1>\n    </div>'
    if old_h1 in html:
        html = html.replace(old_h1, new_h1)
        print("9.3: Tagged #sec-header")
        
    # 2. Butler Model
    old_butler = '<div class="img-box" style="margin:24px 0; text-align:center;">\n    <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_37.png?v=3"'
    new_butler = '<div id="card-butler-model" class="img-box lecture-interactive-card" data-lecture-section="butler_model" style="margin:24px 0; text-align:center; cursor:pointer;">\n    <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_37.png?v=3"'
    if old_butler in html:
        html = html.replace(old_butler, new_butler)
        print("9.3: Tagged #card-butler-model")
        
    # 3. Jamaica Case Study
    old_jam = '<div class="img-box" style="margin:24px 0; text-align:center;">\n    <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_47.png?v=3"'
    new_jam = '<div id="card-jamaica-case-study" class="img-box lecture-interactive-card" data-lecture-section="jamaica_case_study" style="margin:24px 0; text-align:center; cursor:pointer;">\n    <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_47.png?v=3"'
    if old_jam in html:
        html = html.replace(old_jam, new_jam)
        print("9.3: Tagged #card-jamaica-case-study")
        
    diff = check_balance(html)
    assert diff == 0, f"9.3 Div balance mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("9.3: Updated in DB.")

if __name__ == '__main__':
    fix_6_1()
    fix_7_2()
    fix_7_3()
    fix_8_1()
    fix_8_2()
    fix_8_3()
    fix_9_1()
    fix_9_2()
    fix_9_3()
