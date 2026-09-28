import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = '4_3'
LECTURE_ID = '1f909afc-865f-46d0-bb20-2e6d474fa87b'
COURSE_TITLE = 'IGCSE Geography (0460)'
LECTURE_TITLE = '4.3 The Impact of Tectonic Hazards'

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 4.3: Tác động của các Hiểm họa Địa chất",
        "selector": "#sec-header",
        "en": "Lesson 4.3: The Impact of Tectonic Hazards. In this lesson, we analyze physical and human vulnerability factors, primary versus secondary hazard effects, measurement scales, and case study contrasts between HICs and LICs.",
        "vi": "Bài bốn chấm ba: Tác động của các Hiểm họa Địa chất. Trong bài học này, chúng ta sẽ phân tích các yếu tố tổn thương về tự nhiên và con người, tác động sơ cấp so với thứ cấp, các thang đo lường và so sánh điển cứu giữa các nước phát triển và đang phát triển."
    },
    {
        "id": "sec_vulnerability_factors",
        "title": "1. Các yếu tố ảnh hưởng đến mức độ thiệt hại (Tự nhiên vs Con người)",
        "selector": "#sec-vulnerability-factors",
        "en": "Section 1: Factors Influencing Hazard Impact. A hazard only becomes a disaster when it strikes a vulnerable population. Impacts are determined by physical magnitude and focal depth interacting with economic wealth, population density, and building regulations.",
        "vi": "Phần một: Các yếu tố ảnh hưởng đến mức độ thiệt hại. Một hiểm họa chỉ trở thành thảm họa khi nó tấn công một cộng đồng dễ bị tổn thương. Mức độ thiệt hại được quyết định bởi cường độ và độ sâu chấn tiêu tương tác với tiềm lực kinh tế, mật độ dân số và quy chuẩn xây dựng."
    },
    {
        "id": "fact_physical",
        "title": "Các yếu tố tự nhiên (Physical Factors: Magnitude, Depth, Geology)",
        "selector": "#card-fact-physical",
        "en": "Physical Vulnerability Factors. High earthquake magnitude and shallow focal depth release devastating seismic energy. Saturated sandy soils suffer liquefaction, while offshore seabed displacement triggers destructive tsunamis.",
        "vi": "Các yếu tố tự nhiên. Cường độ chấn động lớn và độ sâu chấn tiêu nông giải phóng năng lượng địa chấn có sức tàn phá dữ dội. Nền đất cát bão hòa nước dễ bị hóa lỏng, trong khi sự dịch chuyển đáy biển ngoài khơi sẽ kích hoạt sóng thần hủy diệt."
    },
    {
        "id": "fact_human",
        "title": "Các yếu tố con người & Năng lực ứng phó (Human Resilience & HIC vs LIC)",
        "selector": "#card-fact-human",
        "en": "Human Vulnerability and Economic Development. High-income countries enforce strict seismic building codes and early warning networks. In low-income countries, poor governance, corrupt construction practices, and dense unreinforced masonry cause catastrophic pancake collapse.",
        "vi": "Yếu tố con người và Mức độ phát triển kinh tế. Các quốc gia phát triển thực thi nghiêm ngặt quy chuẩn xây dựng kháng chấn và hệ thống cảnh báo sớm. Tại các nước thu nhập thấp, quản lý yếu kém và nhà cửa bê tông giòn không cốt thép dẫn đến sự sụp đổ tầng lớp như bánh kếp."
    },
    {
        "id": "sec_primary_secondary",
        "title": "2. Tác động sơ cấp vs Tác động thứ cấp (Primary vs Secondary)",
        "selector": "#sec-primary-secondary",
        "en": "Section 2: Primary versus Secondary Impacts. Primary impacts occur instantaneously from ground shaking or eruption. Secondary impacts emerge hours, days, or weeks later as fires spread, water supplies fail, and epidemics take hold.",
        "vi": "Phần hai: Tác động sơ cấp và Tác động thứ cấp. Tác động sơ cấp xảy ra tức thì do rung lắc mặt đất hoặc núi lửa phun. Tác động thứ cấp phát sinh sau vài giờ, vài ngày hoặc vài tuần do hỏa hoạn lan rộng, mất nước sạch và dịch bệnh bùng phát."
    },
    {
        "id": "impact_earthquakes",
        "title": "Tác động của Động đất: Đổ sập công trình, Hỏa hoạn & Sóng thần",
        "selector": "#card-impact-earthquakes",
        "en": "Earthquake Impacts. Primary shaking collapses bridges and buildings, severing pipelines. Secondary consequences include catastrophic tsunamis, uncontrollable gas fires, landslides, and cholera outbreaks in displaced camps.",
        "vi": "Tác động của động đất. Rung lắc sơ cấp làm sập cầu cống và nhà cửa, đứt gãy đường ống dẫn. Hậu quả thứ cấp bao gồm sóng thần thảm khốc, cháy nổ đường ống dẫn khí không thể dập tắt, sạt lở đất và dịch tả trong các trại tị nạn."
    },
    {
        "id": "impact_volcanoes",
        "title": "Tác động của Núi lửa: Dòng mạt vụn, Tro bụi & Dòng bùn Lahar",
        "selector": "#card-impact-volcanoes",
        "en": "Volcanic Impacts. Primary hazards incinerate landscapes with pyroclastic surges and blanket towns in suffocating ash. Secondary hazards trigger roaring mudflows called lahars, roof collapse, global atmospheric cooling, and airspace shutdown.",
        "vi": "Tác động của núi lửa. Hiểm họa sơ cấp thiêu rụi cảnh quan bằng các luồng mạt vụn và phủ kín các thị trấn trong tro bụi độc hại. Hiểm họa thứ cấp gây ra lũ bùn núi lửa lahar kinh hoàng, sập mái nhà, hạ nhiệt độ khí hậu toàn cầu và tê liệt hàng không."
    },
    {
        "id": "sec_severity_scales",
        "title": "3. Đo lường cường độ và sức phá hủy (Magnitude, Mercalli & VEI)",
        "selector": "#sec-severity-scales",
        "en": "Section 3: Measuring Hazard Magnitude and Intensity. Geographers contrast logarithmic physical energy release against observed surface destruction and volcanic ejecta volumes.",
        "vi": "Phần ba: Đo lường cường độ và sức phá hủy. Các nhà địa lý phân biệt giữa năng lượng vật lý giải phóng theo thang logarit với mức độ tàn phá quan sát được trên bề mặt và thể tích vật liệu núi lửa phun ra."
    },
    {
        "id": "scale_moment_magnitude",
        "title": "Thang độ lớn Mômen (Moment Magnitude Scale - Mw)",
        "selector": "#scale-moment-magnitude",
        "en": "Moment Magnitude Scale. A logarithmic physical scale measuring total seismic energy release based on fault slip area and rock rigidity. Each whole integer increase represents approximately 31.6 times more energy.",
        "vi": "Thang độ lớn Mômen. Thang đo vật lý theo hàm logarit đo lường tổng năng lượng địa chấn giải phóng dựa trên diện tích đứt gãy và độ cứng của đá. Mỗi một bậc tăng biểu thị năng lượng giải phóng gấp khoảng ba mươi mốt phẩy sáu lần."
    },
    {
        "id": "scale_mercalli",
        "title": "Thang đo cường độ chấn động Mercalli (MMI: I - XII)",
        "selector": "#scale-mercalli",
        "en": "Modified Mercalli Intensity Scale. An observational twelve-point scale rating witnessed human sensations and structural damage, varying inversely with distance from the epicentre.",
        "vi": "Thang đo cường độ chấn động Mercalli. Thang đánh giá mười hai cấp dựa trên cảm nhận của con người và mức độ hư hại công trình quan sát được trên thực địa, giảm dần khi càng ra xa tâm chấn."
    },
    {
        "id": "scale_vei",
        "title": "Chỉ số bùng nổ núi lửa (VEI: 0 - 8)",
        "selector": "#scale-vei",
        "en": "Volcanic Explosivity Index. A logarithmic scale from zero to eight measuring eruption volume of tephra and eruptive column height, from gentle Hawaiian fountains to catastrophic supervolcano calderas.",
        "vi": "Chỉ số bùng nổ núi lửa. Thang logarit từ không đến tám đo lường thể tích mạt vụn tro núi lửa và độ cao của cột khói phun trào, từ các vòi dung nham êm dịu ở Ha-oai đến các vụ nổ siêu núi lửa kinh hoàng."
    },
    {
        "id": "sec_case_studies",
        "title": "4. So sánh các Nghiên cứu Điển hình: HIC vs LIC (Nhật Bản, Haiti, Pinatubo)",
        "selector": "#sec-case-studies",
        "en": "Section 4: Comparative Case Studies: High-Income versus Low-Income Countries. Contrasting Tohoku, Haiti, and Mount Pinatubo proves that human vulnerability and economic resources dictate disaster survival.",
        "vi": "Phần bốn: So sánh các Nghiên cứu Điển hình giữa các nước giàu và nước nghèo. So sánh giữa Tohoku Nhật Bản, Haiti và núi lửa Pinatubo chứng minh rõ ràng rằng tính dễ tổn thương và tiềm lực kinh tế quyết định tỷ lệ sống sót trước thảm họa."
    },
    {
        "id": "case_japan_2011",
        "title": "🇯🇵 Điển cứu HIC: Động đất & Sóng thần Tohoku, Nhật Bản (2011)",
        "selector": "#case-japan-2011",
        "en": "Case Study 1: Tohoku, Japan 2011 (HIC). An Mw 9.0 megathrust earthquake caused minimal structural shaking collapse due to strict building codes. However, a forty-metre tsunami overtopped seawalls, causing eighteen thousand deaths and a nuclear meltdown, costing 235 billion dollars.",
        "vi": "Nghiên cứu điển hình một: Tohoku Nhật Bản năm hai nghìn không trăm mười một. Trận siêu động đất chín phẩy không độ Mw hầu như không làm sập nhà cửa nhờ quy chuẩn xây dựng nghiêm ngặt. Tuy nhiên sóng thần cao bốn mươi mét đã vượt qua đê biển làm mười tám nghìn người chết và gây sự cố hạt nhân, thiệt hại hai trăm ba mươi lăm tỷ đô-la."
    },
    {
        "id": "case_haiti_2010",
        "title": "🇭🇹 Điển cứu LIC: Động đất tàn phá Port-au-Prince, Haiti (2010)",
        "selector": "#case-haiti-2010",
        "en": "Case Study 2: Port-au-Prince, Haiti 2010 (LIC). An Mw 7.0 shallow earthquake destroyed over 250,000 unreinforced concrete homes. Weak governance and poverty caused over 220,000 fatalities, followed by a secondary cholera epidemic that killed thousands more.",
        "vi": "Nghiên cứu điển hình hai: Port-au-Prince Haiti năm hai nghìn không trăm mười. Trận động đất nông bảy phẩy không độ Mw đã làm sụp đổ hoàn toàn hơn hai trăm năm mươi nghìn ngôi nhà bê tông không cốt thép. Quản lý yếu kém và đói nghèo dẫn tới hơn hai trăm hai mươi nghìn người thiệt mạng, cùng dịch tả sau đó cướp đi thêm hàng nghìn sinh mạng."
    },
    {
        "id": "case_pinatubo_1991",
        "title": "🇵🇭 Điển cứu Núi lửa MIC: Núi Pinatubo, Philippines (1991)",
        "selector": "#case-pinatubo-1991",
        "en": "Case Study 3: Mount Pinatubo, Philippines 1991 (MIC). A colossal VEI 6 eruption combined with Typhoon Yunya triggered catastrophic lahars. Timely seismic forecasting and coordinated evacuation saved over seventy-five thousand lives, demonstrating the power of early warning.",
        "vi": "Nghiên cứu điển hình ba: Núi lửa Pinatubo Phi-líp-pin năm một nghìn chín trăm chín mươi mốt. Vụ nổ núi lửa khổng lồ cấp sáu kết hợp với bão nhiệt đới gây ra các dòng bùn lahar quét sạch các thung lũng sông. Công tác dự báo địa chấn kịp thời và sơ tán có tổ chức đã cứu sống hơn bảy mươi lăm nghìn người."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 3},
    "sec_vulnerability_factors": {"start": 1, "end": 3},
    "sec_primary_secondary": {"start": 4, "end": 6},
    "sec_severity_scales": {"start": 7, "end": 10},
    "sec_case_studies": {"start": 11, "end": 14}
}

def transform_html(raw_html):
    html = raw_html
    
    # 1. Header
    html = re.sub(
        r'(<div style="background:linear-gradient\(135deg, #b91c1c, #dc2626, #ea580c\);[^"]*">[\s\S]*?</div>)',
        r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; border-radius:12px; margin-bottom:24px; transition:all 0.2s ease;">\1</div>',
        html, count=1
    )
    
    # 2. Section 1: Factors Influencing Hazard Impact
    html = re.sub(
        r'(<h2 style="color:#b91c1c;[^"]*">\s*1\. Factors Influencing Hazard Impact\s*\(Physical vs\. Human\)\s*</h2>)',
        r'<div id="sec-vulnerability-factors" class="lecture-interactive-card" data-lecture-section="sec_vulnerability_factors" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 2
    html = re.sub(
        r'(\s*)(<h2 style="color:#b91c1c;[^"]*">\s*2\. Primary vs\. Secondary Impacts)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Physical vs Human cards
    html = html.replace(
        '<div style="background:#fff1f2; border:1px solid #fecaca; border-radius:8px; padding:18px;">\n        <h4 style="margin:0 0 10px 0; color:#991b1b; font-size:16px; font-weight:bold;">🌍 Physical Factors</h4>',
        '<div id="card-fact-physical" class="lecture-interactive-card" data-lecture-section="fact_physical" style="background:#fff1f2; border:1px solid #fecaca; border-radius:8px; padding:18px; cursor:pointer;">\n        <h4 style="margin:0 0 10px 0; color:#991b1b; font-size:16px; font-weight:bold;">🌍 Physical Factors</h4>'
    )
    html = html.replace(
        '<div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px; padding:18px;">\n        <h4 style="margin:0 0 10px 0; color:#1e40af; font-size:16px; font-weight:bold;">👥 Human Factors &amp; Vulnerability</h4>',
        '<div id="card-fact-human" class="lecture-interactive-card" data-lecture-section="fact_human" style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px; padding:18px; cursor:pointer;">\n        <h4 style="margin:0 0 10px 0; color:#1e40af; font-size:16px; font-weight:bold;">👥 Human Factors &amp; Vulnerability</h4>'
    )
    
    # 3. Section 2: Primary vs Secondary
    html = re.sub(
        r'(<h2 style="color:#b91c1c;[^"]*">\s*2\. Primary vs\. Secondary Impacts\s*</h2>)',
        r'<div id="sec-primary-secondary" class="lecture-interactive-card" data-lecture-section="sec_primary_secondary" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 3
    html = re.sub(
        r'(\s*)(<h2 style="color:#b91c1c;[^"]*">\s*3\. Measuring Hazard Magnitude)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Table rows in Primary vs Secondary
    html = html.replace('<tr>\n            <td style="padding:12px 14px; border:1px solid #e2e8f0; font-weight:bold; color:#dc2626;">Earthquakes</td>', '<tr id="card-impact-earthquakes" class="lecture-interactive-card" data-lecture-section="impact_earthquakes" style="cursor:pointer;">\n            <td style="padding:12px 14px; border:1px solid #e2e8f0; font-weight:bold; color:#dc2626;">Earthquakes</td>')
    html = html.replace('<tr style="background:#f8fafc;">\n            <td style="padding:12px 14px; border:1px solid #e2e8f0; font-weight:bold; color:#ea580c;">Volcanoes</td>', '<tr id="card-impact-volcanoes" class="lecture-interactive-card" data-lecture-section="impact_volcanoes" style="background:#f8fafc; cursor:pointer;">\n            <td style="padding:12px 14px; border:1px solid #e2e8f0; font-weight:bold; color:#ea580c;">Volcanoes</td>')
    
    # 4. Section 3: Severity Scales
    html = re.sub(
        r'(<h2 style="color:#b91c1c;[^"]*">\s*3\. Measuring Hazard Magnitude and Intensity\s*</h2>)',
        r'<div id="sec-severity-scales" class="lecture-interactive-card" data-lecture-section="sec_severity_scales" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 4
    html = re.sub(
        r'(\s*)(<h2 style="color:#b91c1c;[^"]*">\s*4\. Comparative Case Studies)',
        r'</div>\1\2',
        html, count=1
    )
    
    # SVG 1 Columns
    html = html.replace('<rect x="20" y="20" width="265" height="300" rx="8" fill="#1e3a5f" stroke="#38bdf8" stroke-width="1.5"/>', '<g id="scale-moment-magnitude" data-lecture-section="scale_moment_magnitude" style="cursor:pointer;"><rect x="20" y="20" width="265" height="300" rx="8" fill="#1e3a5f" stroke="#38bdf8" stroke-width="1.5"/>')
    html = html.replace('<text x="152" y="305" fill="#bae6fd" font-size="9.5" text-anchor="middle">💡 Each +1.0 = 31.6× more energy released</text>', '<text x="152" y="305" fill="#bae6fd" font-size="9.5" text-anchor="middle">💡 Each +1.0 = 31.6× more energy released</text></g>')
    
    html = html.replace('<rect x="305" y="20" width="270" height="300" rx="8" fill="#312e81" stroke="#818cf8" stroke-width="1.5"/>', '<g id="scale-mercalli" data-lecture-section="scale_mercalli" style="cursor:pointer;"><rect x="305" y="20" width="270" height="300" rx="8" fill="#312e81" stroke="#818cf8" stroke-width="1.5"/>')
    html = html.replace('<text x="440" y="305" fill="#c7d2fe" font-size="9.5" text-anchor="middle">💡 Subjective scale; decreases with distance</text>', '<text x="440" y="305" fill="#c7d2fe" font-size="9.5" text-anchor="middle">💡 Subjective scale; decreases with distance</text></g>')
    
    html = html.replace('<rect x="595" y="20" width="265" height="300" rx="8" fill="#4c0519" stroke="#f43f5e" stroke-width="1.5"/>', '<g id="scale-vei" data-lecture-section="scale_vei" style="cursor:pointer;"><rect x="595" y="20" width="265" height="300" rx="8" fill="#4c0519" stroke="#f43f5e" stroke-width="1.5"/>')
    html = html.replace('<text x="727" y="305" fill="#fecdd3" font-size="9.5" text-anchor="middle">💡 Logarithmic scale for tephra ejecta (&gt;1 km³)</text>', '<text x="727" y="305" fill="#fecdd3" font-size="9.5" text-anchor="middle">💡 Logarithmic scale for tephra ejecta (&gt;1 km³)</text></g>')
    
    # 5. Section 4: Case Studies
    html = re.sub(
        r'(<h2 style="color:#b91c1c;[^"]*">\s*4\. Comparative Case Studies: HIC vs\. LIC Impacts\s*</h2>)',
        r'<div id="sec-case-studies" class="lecture-interactive-card" data-lecture-section="sec_case_studies" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    
    # Case study cards
    html = html.replace(
        '<div style="background:#f0f9ff; border:1px solid #bae6fd; border-left:5px solid #0284c7; border-radius:8px; padding:20px;">\n        <h4 style="margin:0 0 10px 0; color:#0369a1; font-size:17px; font-weight:bold;">🇯🇵 Case Study 1: Earthquake &amp; Tsunami in an HIC — Tohoku, Japan (2011)</h4>',
        '<div id="case-japan-2011" class="lecture-interactive-card" data-lecture-section="case_japan_2011" style="background:#f0f9ff; border:1px solid #bae6fd; border-left:5px solid #0284c7; border-radius:8px; padding:20px; cursor:pointer;">\n        <h4 style="margin:0 0 10px 0; color:#0369a1; font-size:17px; font-weight:bold;">🇯🇵 Case Study 1: Earthquake &amp; Tsunami in an HIC — Tohoku, Japan (2011)</h4>'
    )
    html = html.replace(
        '<div style="background:#fef2f2; border:1px solid #fecaca; border-left:5px solid #dc2626; border-radius:8px; padding:20px;">\n        <h4 style="margin:0 0 10px 0; color:#991b1b; font-size:17px; font-weight:bold;">🇭🇹 Case Study 2: Earthquake in an LIC — Port-au-Prince, Haiti (2010)</h4>',
        '<div id="case-haiti-2010" class="lecture-interactive-card" data-lecture-section="case_haiti_2010" style="background:#fef2f2; border:1px solid #fecaca; border-left:5px solid #dc2626; border-radius:8px; padding:20px; cursor:pointer;">\n        <h4 style="margin:0 0 10px 0; color:#991b1b; font-size:17px; font-weight:bold;">🇭🇹 Case Study 2: Earthquake in an LIC — Port-au-Prince, Haiti (2010)</h4>'
    )
    html = html.replace(
        '<div style="background:#fff7ed; border:1px solid #fed7aa; border-left:5px solid #ea580c; border-radius:8px; padding:20px;">\n        <h4 style="margin:0 0 10px 0; color:#c2410c; font-size:17px; font-weight:bold;">🇵🇭 Case Study 3: Volcanic Eruption in an MIC — Mount Pinatubo, Philippines (1991)</h4>',
        '<div id="case-pinatubo-1991" class="lecture-interactive-card" data-lecture-section="case_pinatubo_1991" style="background:#fff7ed; border:1px solid #fed7aa; border-left:5px solid #ea580c; border-radius:8px; padding:20px; cursor:pointer;">\n        <h4 style="margin:0 0 10px 0; color:#c2410c; font-size:17px; font-weight:bold;">🇵🇭 Case Study 3: Volcanic Eruption in an MIC — Mount Pinatubo, Philippines (1991)</h4>'
    )
    
    html += '</div>'
    return html

async def main():
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )
    
    raw_path = f"scratch/lectures/{LECTURE_CODE}_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        raw_html = f.read()
    
    new_html = transform_html(raw_html)
    
    interactive_path = f"scratch/lectures/{LECTURE_CODE}_p1_interactive.html"
    with open(interactive_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Transformed HTML saved to {interactive_path}")
    
    update_supabase_page(LECTURE_ID, new_html)
    print(f"Lecture {LECTURE_CODE} fully processed and uploaded!")

if __name__ == '__main__':
    asyncio.run(main())
