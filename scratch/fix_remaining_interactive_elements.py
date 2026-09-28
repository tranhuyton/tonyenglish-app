import sys
import re
sys.path.append('scripts')
from audio_lecture_engine import sb

def check_balance(html):
    o = len(re.findall(r'<div\b', html, re.I))
    c = len(re.findall(r'</div>', html, re.I))
    return o - c

def fix_10_1():
    lid = '362104be-aedc-4cbe-87b2-29034e93cc9c'
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    farms = [
        ('fbtn-prairies', 'farm_prairies', 'prairies'),
        ('fbtn-ganges', 'farm_ganges', 'ganges'),
        ('fbtn-sahel', 'farm_sahel', 'sahel'),
        ('fbtn-vertical', 'farm_vertical', 'vertical'),
    ]
    for bid, sec_key, fkey in farms:
        target = f'<button onclick="selectFarm(\'{fkey}\')" id="{bid}"'
        repl = f'<button id="{bid}" class="lecture-interactive-card" data-lecture-section="{sec_key}" onclick="selectFarm(\'{fkey}\')"'
        if target in html:
            html = html.replace(target, repl)
            print(f"10.1: Added lecture-interactive-card to #{bid}")
        else:
            print(f"10.1: Target not found for #{bid}")
            
    diff = check_balance(html)
    assert diff == 0, f"10.1 Div mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("10.1: Updated in DB.")

def fix_9_1():
    lid = '6c14f92b-774a-45d1-a68d-2e9fe5e0b85d'
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    points = [
        ('Mali', 'pin-emp-mali', 'emp_mali'),
        ('Vietnam', 'pin-emp-vietnam', 'emp_vietnam'),
        ('USA', 'pin-emp-usa', 'emp_usa'),
        ('UK', 'pin-emp-uk', 'emp_uk'),
    ]
    for country, pid, sec_key in points:
        pat = rf'<circle(\s+[^>]*class="map-point"[^>]*data-country="{country}"[^>]*)>'
        repl = rf'<circle id="{pid}" data-lecture-section="{sec_key}"\1>'
        # Also ensure 'lecture-interactive-card' is in class
        html = re.sub(
            rf'<circle(\s+cx="[^"]*"\s+cy="[^"]*"\s+r="[^"]*"\s+fill="[^"]*"\s+)class="map-point"(\s+data-country="{country}"[^>]*)>',
            rf'<circle id="{pid}" \1class="map-point lecture-interactive-card" data-lecture-section="{sec_key}"\2>',
            html
        )
        print(f"9.1: Tagged #{pid}")
        
    diff = check_balance(html)
    assert diff == 0, f"9.1 Div mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("9.1: Updated in DB.")

def fix_9_2():
    lid = '5b7da7e1-3da1-4bf4-9700-6e11d7a7ef6b'
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    target_hq = '''            <!-- HQ (Oregon, USA) -->
            <circle cx="150" cy="140" r="12" fill="#0f766e" />
            <text x="150" y="120" font-size="12" text-anchor="middle" font-weight="bold" fill="#0f766e">HQ (Oregon, USA)</text>
            <text x="150" y="170" font-size="10" text-anchor="middle" fill="#475569">Design & Marketing</text>'''
            
    repl_hq = '''            <g id="node-nike-hq" class="lecture-interactive-card" data-lecture-section="nike_hq" style="cursor:pointer;">
            <!-- HQ (Oregon, USA) -->
            <circle cx="150" cy="140" r="12" fill="#0f766e" />
            <text x="150" y="120" font-size="12" text-anchor="middle" font-weight="bold" fill="#0f766e">HQ (Oregon, USA)</text>
            <text x="150" y="170" font-size="10" text-anchor="middle" fill="#475569">Design & Marketing</text>
            </g>'''
            
    if target_hq in html:
        html = html.replace(target_hq, repl_hq)
        print("9.2: Successfully wrapped #node-nike-hq")
    else:
        print("9.2: Target HQ not matched exactly!")
        
    diff = check_balance(html)
    assert diff == 0, f"9.2 Div mismatch: {diff}"
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print("9.2: Updated in DB.")

if __name__ == '__main__':
    fix_10_1()
    fix_9_1()
    fix_9_2()
