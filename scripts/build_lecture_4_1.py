import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = '4_1'
LECTURE_ID = 'e5fde4e7-a1e6-4b3c-aeb2-756155f06ff5'
COURSE_TITLE = 'IGCSE Geography (0460)'
LECTURE_TITLE = '4.1 The Structure of the Earth and the Distribution of Earthquakes and Volcanoes'

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 4.1: Cấu trúc Trái Đất & Phân bố Động đất Núi lửa",
        "selector": "#sec-header",
        "en": "Lesson 4.1: The Structure of the Earth and the Distribution of Earthquakes and Volcanoes. In this lesson, we study the concentric layers of the Earth, the triad of tectonic driving forces, plate boundary types, and global hazard belts.",
        "vi": "Bài bốn chấm một: Cấu trúc của Trái Đất và Sự phân bố của Động đất và Núi lửa. Trong bài học này, chúng ta sẽ nghiên cứu các tầng cấu tạo đồng tâm của Trái Đất, bộ ba động lực dịch chuyển mảng kiến tạo, các loại ranh giới mảng và các vành đai hiểm họa toàn cầu."
    },
    {
        "id": "sec_earth_structure",
        "title": "1. Cấu trúc bên trong của Trái Đất (Concentric Layers)",
        "selector": "#sec-earth-structure",
        "en": "Section 1: The Internal Structure of the Earth. Earth is organized into concentric spherical layers: the solid brittle crust, the semi-molten convective mantle, the liquid outer core, and the solid metallic inner core.",
        "vi": "Phần một: Cấu trúc bên trong của Trái Đất. Trái Đất được cấu tạo thành các tầng đồng tâm: lớp vỏ cứng giòn ngoài cùng, lớp manti đối lưu bán nóng chảy, lớp lõi ngoài dạng lỏng và lớp lõi trong kim loại rắn đặc."
    },
    {
        "id": "layer_crust",
        "title": "Lớp vỏ Trái Đất: Vỏ đại dương & Vỏ lục địa (Crust)",
        "selector": "#layer-crust",
        "en": "The Crust and Lithosphere. Oceanic crust is thin, dense, and basaltic, averaging five to ten kilometres. Continental crust is thick, buoyant, and granitic, averaging thirty-five kilometres and unable to subduct into the mantle.",
        "vi": "Lớp vỏ Trái Đất và Thạch quyển. Vỏ đại dương mỏng, nặng và chứa nhiều bazan, dày trung bình từ năm đến mười ki-lô-mét. Vỏ lục địa dày, nhẹ và chứa nhiều granit, dày trung bình ba mươi lăm ki-lô-mét và không thể bị chìm vào lớp manti."
    },
    {
        "id": "layer_mantle",
        "title": "Lớp Manti & Dòng đối lưu nhiệt (Mantle Convection)",
        "selector": "#layer-mantle",
        "en": "The Mantle and Asthenosphere. Extending to 2,900 kilometres, comprising eighty-four percent of Earth's volume. Heat from radioactive decay drives sluggish thermal convection cells that drag overlying tectonic plates.",
        "vi": "Lớp Manti và Tầng mềm quyển. Sâu tới hai nghìn chín trăm ki-lô-mét, chiếm tám mươi tư phần trăm thể tích Trái Đất. Nhiệt sinh ra từ phân rã phóng xạ kích hoạt các ô đối lưu nhiệt chậm chạp, kéo trôi các mảng kiến tạo bên trên."
    },
    {
        "id": "layer_outer_core",
        "title": "Lõi ngoài dạng lỏng & Từ trường Trái Đất (Outer Core)",
        "selector": "#layer-outer-core",
        "en": "The Liquid Outer Core. Composed of molten iron and nickel between 2,900 and 5,100 kilometres depth. Churning metallic convection currents act as a planetary dynamo, generating Earth's protective geomagnetic shield.",
        "vi": "Lớp Lõi ngoài dạng lỏng. Cấu tạo từ sắt và niken nóng chảy ở độ sâu từ hai nghìn chín trăm đến năm nghìn một trăm ki-lô-mét. Dòng kim loại lỏng đối lưu mạnh mẽ đóng vai trò như một máy phát điện hành tinh, tạo ra từ trường bảo vệ Trái Đất."
    },
    {
        "id": "layer_inner_core",
        "title": "Lõi trong rắn đặc & Áp suất cực đại (Inner Core)",
        "selector": "#layer-inner-core",
        "en": "The Solid Inner Core. A dense sphere of iron-nickel alloy reaching 6,000 degrees Celsius. Incomprehensible gravitational pressure exceeding 3.6 million atmospheres forces atoms into an immoveable solid crystalline lattice.",
        "vi": "Lớp Lõi trong rắn đặc. Một khối cầu hợp kim sắt niken đặc quánh đạt tới sáu nghìn độ C. Áp suất trọng lực khủng khiếp vượt quá ba phẩy sáu triệu át-mốt-phe ép chặt các nguyên tử thành một mạng tinh thể rắn bất động."
    },
    {
        "id": "sec_driving_mechanisms",
        "title": "2. Thuyết kiến tạo mảng & Bộ ba động lực chuyển động",
        "selector": "#sec-driving-mechanisms",
        "en": "Section 2: Plate Tectonics and Driving Mechanisms. Earth's lithosphere is fractured into major tectonic plates moving at two to ten centimetres annually, driven by three interrelated physical forces.",
        "vi": "Phần hai: Kiến tạo mảng và Cơ chế vận động. Thạch quyển bị phân cắt thành các mảng kiến tạo lớn dịch chuyển từ hai đến mười xăng-ti-mét mỗi năm, được thúc đẩy bởi ba lực vật lý tương tác lẫn nhau."
    },
    {
        "id": "driver_slab_pull",
        "title": "Lực kéo mảng chìm (Slab Pull: Động lực chủ đạo)",
        "selector": "#card-slab-pull",
        "en": "Slab Pull, the Primary Driving Force. As cold, dense oceanic lithosphere plunges into a deep oceanic trench at subduction zones, gravity pulls the entire trailing plate downward into the mantle behind it.",
        "vi": "Lực kéo mảng chìm, động lực chủ đạo. Khi mảng vỏ đại dương lạnh và đặc chìm sâu vào rãnh hút chìm, trọng lực sẽ kéo toàn bộ phần thân mảng phía sau trôi tuột xuống lớp manti theo sau nó."
    },
    {
        "id": "driver_ridge_push",
        "title": "Lực đẩy sống núi & Trôi trượt trọng lực (Ridge Push)",
        "selector": "#card-ridge-push",
        "en": "Ridge Push and Gravitational Sliding. Magma upwelling creates buoyant, elevated mid-ocean ridges two to three kilometres above ocean basins. Gravity forces the elevated crust to slide downslope away from the ridge crest.",
        "vi": "Lực đẩy sống núi và Trôi trượt trọng lực. Magma trồi lên tạo thành các sống núi ngầm nhô cao hai đến ba ki-lô-mét so với đáy biển. Trọng lực khiến lớp vỏ trên cao trượt dốc ra xa khỏi đỉnh sống núi."
    },
    {
        "id": "sec_boundary_types",
        "title": "3. Bốn loại ranh giới mảng kiến tạo (Plate Boundaries)",
        "selector": "#sec-boundary-types",
        "en": "Section 3: Types of Plate Boundaries. Active geological hazards occur where plates interact. The syllabus examines four boundaries: constructive, destructive, collision, and conservative margins.",
        "vi": "Phần ba: Bốn loại ranh giới mảng kiến tạo. Các hiểm họa địa chất xuất hiện tập trung tại nơi các mảng tương tác với nhau. Chương trình học phân loại thành bốn ranh giới: tách giãn, hút chìm, va chạm và chuyển dạng."
    },
    {
        "id": "bnd_constructive",
        "title": "Ranh giới Tách giãn / Kiến tạo (Constructive / Divergent)",
        "selector": "#card-bnd-constructive",
        "en": "Constructive Plate Boundaries. Plates pull apart, allowing basaltic magma to erupt as gentle effusive shield volcanoes and fissure vents, forming mid-ocean ridges like the Mid-Atlantic Ridge and rift valleys in East Africa.",
        "vi": "Ranh giới Tách giãn hay Kiến tạo. Các mảng kéo xa nhau, tạo điều kiện cho magma bazan phun trào tạo thành các núi lửa hình khiên êm đềm và khe nứt ngầm, hình thành sống núi giữa Đại Tây Dương và thung lũng tách giãn Đông Phi."
    },
    {
        "id": "bnd_destructive",
        "title": "Ranh giới Hút chìm / Phá hủy (Destructive / Subduction)",
        "selector": "#card-bnd-destructive",
        "en": "Destructive Subduction Boundaries. Dense oceanic plates plunge beneath lighter continental plates, melting to form violent composite stratovolcanoes, deep ocean trenches, and high-magnitude earthquakes along the Benioff zone.",
        "vi": "Ranh giới Hút chìm hay Phá hủy. Mảng đại dương nặng chìm xuống dưới mảng lục địa nhẹ, bị nóng chảy sinh ra các núi lửa tầng phun nổ dữ dội, các rãnh đại dương sâu thẳm và các trận động đất mạnh dọc đới Bê-ni-ốp."
    },
    {
        "id": "bnd_collision",
        "title": "Ranh giới Va chạm lục địa (Collision: Himalayas)",
        "selector": "#card-bnd-collision",
        "en": "Continental Collision Boundaries. Two buoyant continental plates collide head-on. Neither can sink; the crust buckles upward into immense fold mountains like the Himalayas, producing severe earthquakes with zero volcanism.",
        "vi": "Ranh giới Va chạm lục địa. Hai mảng lục địa nhẹ đâm trực diện vào nhau. Không mảng nào có thể chìm xuống; vỏ đất đá bị dồn nén uốn nếp vồng lên thành các dãy núi khổng lồ như Hi-ma-lay-a, gây ra động đất dữ dội nhưng hoàn toàn không có núi lửa."
    },
    {
        "id": "bnd_conservative",
        "title": "Ranh giới Chuyển dạng / Bảo toàn (Conservative / Transform)",
        "selector": "#card-bnd-conservative",
        "en": "Conservative Transform Boundaries. Plates grind past each other horizontally along transform faults like the San Andreas Fault. Friction locks plates until sudden slips trigger catastrophic shallow-focus earthquakes without volcanic activity.",
        "vi": "Ranh giới Chuyển dạng hay Bảo toàn. Các mảng trượt ngang qua nhau dọc theo các đứt gãy biến đổi như San An-đrê-át. Ma sát khóa chặt các mảng cho đến khi giải phóng đột ngột gây ra các trận động đất nông thảm khốc mà không có núi lửa."
    },
    {
        "id": "sec_hazard_belts",
        "title": "4. Phân bố toàn cầu của Động đất và Núi lửa",
        "selector": "#sec-hazard-belts",
        "en": "Section 4: Global Distribution of Earthquakes and Volcanoes. Seismicity and volcanism form distinct planetary belts corresponding closely to plate margins, most famously the Pacific Ring of Fire.",
        "vi": "Phần bốn: Phân bố toàn cầu của Động đất và Núi lửa. Động đất và núi lửa phân bố thành các vành đai hành tinh rõ rệt trùng khớp với ranh giới mảng, nổi tiếng nhất là Vành đai lửa Thái Bình Dương."
    },
    {
        "id": "belt_ring_of_fire",
        "title": "Vành đai lửa Thái Bình Dương (Pacific Ring of Fire: 75% núi lửa)",
        "selector": "#belt-ring-of-fire",
        "en": "The Pacific Ring of Fire. A forty-thousand-kilometre horseshoe encircling the Pacific Basin where subduction zones trigger seventy-five percent of the world's active volcanoes and ninety percent of all earthquakes.",
        "vi": "Vành đai lửa Thái Bình Dương. Một vòng cung hình móng ngựa dài bốn mươi nghìn ki-lô-mét bao quanh lòng chảo Thái Bình Dương, nơi các đới hút chìm gây ra bảy mươi lăm phần trăm số núi lửa hoạt động và chín mươi phần trăm các trận động đất trên toàn cầu."
    },
    {
        "id": "belt_mid_atlantic",
        "title": "Sống núi giữa Đại Tây Dương (Mid-Atlantic Ridge)",
        "selector": "#belt-mid-atlantic",
        "en": "The Mid-Atlantic Ridge. A continuous underwater mountain range stretching over sixteen thousand kilometres, where sea-floor spreading drives steady volcanic eruptions and submarine hydrothermal vents.",
        "vi": "Sống núi giữa Đại Tây Dương. Dãy núi ngầm liên tục trải dài hơn mười sáu nghìn ki-lô-mét dưới lòng biển, nơi sự tách giãn đáy đại dương tạo ra các vụ phun trào núi lửa êm đềm và các miệng thủy nhiệt dưới đáy biển."
    },
    {
        "id": "belt_himalayas",
        "title": "Đới đứt gãy Alp-Himalaya (Alpine-Himalayan Belt)",
        "selector": "#belt-himalayas",
        "en": "The Alpine-Himalayan Orogenic Belt. Formed by collision between the African, Arabian, and Indian plates with Eurasia, generating devastating shallow-focus earthquakes across Southern Europe, the Middle East, and Nepal.",
        "vi": "Vành đai kiến tạo An-pơ Hi-ma-lay-a. Hình thành do sự va chạm giữa mảng châu Phi, Ả Rập và Ấn Độ với mảng Á-Âu, tạo ra các trận động đất chấn tiêu nông có sức tàn phá khủng khiếp qua Nam Âu, Trung Đông và Nê-pan."
    },
    {
        "id": "belt_hotspots",
        "title": "Điểm nóng nội mảng: Hawaii & Yellowstone (Intraplate Hotspots)",
        "selector": "#belt-hotspots",
        "en": "Intraplate Volcanic Hotspots. Anomalously hot stationary mantle plumes breach through tectonic plates far from boundaries, forming the Hawaiian volcanic chain and the Yellowstone supervolcano caldera.",
        "vi": "Các điểm nóng núi lửa nội mảng. Các luồng manti nhiệt đứng yên dị thường khoét thủng lớp vỏ mảng kiến tạo từ bên dưới dù ở xa ranh giới mảng, tạo thành chuỗi đảo núi lửa Ha-oai và siêu núi lửa Y-eo-lâu-xtôn."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 5},
    "sec_earth_structure": {"start": 1, "end": 5},
    "sec_driving_mechanisms": {"start": 6, "end": 8},
    "sec_boundary_types": {"start": 9, "end": 13},
    "sec_hazard_belts": {"start": 14, "end": 18}
}

def transform_html(raw_html):
    html = raw_html
    
    # 1. Header
    html = re.sub(
        r'(<div style="background:linear-gradient\(135deg, #b91c1c, #dc2626, #ea580c\);[^"]*">[\s\S]*?</div>)',
        r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; border-radius:12px; margin-bottom:24px; transition:all 0.2s ease;">\1</div>',
        html, count=1
    )
    
    # 2. Section 1: Internal Structure
    html = re.sub(
        r'(<h2 style="color:#b91c1c;[^"]*">\s*1\. The Internal Structure of the Earth\s*</h2>)',
        r'<div id="sec-earth-structure" class="lecture-interactive-card" data-lecture-section="sec_earth_structure" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 2
    html = re.sub(
        r'(\s*)(<h2 style="color:#b91c1c;[^"]*">\s*2\. Plate Tectonics)',
        r'</div>\1\2',
        html, count=1
    )
    
    # SVG 1 layers
    html = html.replace('<text x="745" y="35" fill="#0f172a" font-size="13" font-weight="bold">1. Crust (0–70 km)</text>', '<g id="layer-crust" data-lecture-section="layer_crust" style="cursor:pointer;"><text x="745" y="35" fill="#0f172a" font-size="13" font-weight="bold">1. Crust (0–70 km)</text>')
    html = html.replace('<text x="635" y="25" fill="#c2410c" font-size="13" font-weight="bold">2. Mantle (70–2900 km)</text>', '</g><g id="layer-mantle" data-lecture-section="layer_mantle" style="cursor:pointer;"><text x="635" y="25" fill="#c2410c" font-size="13" font-weight="bold">2. Mantle (70–2900 km)</text>')
    html = html.replace('<text x="350" y="55" fill="#b45309" font-size="13" font-weight="bold">3. Outer Core (2900–5100 km)</text>', '</g><g id="layer-outer-core" data-lecture-section="layer_outer_core" style="cursor:pointer;"><text x="350" y="55" fill="#b45309" font-size="13" font-weight="bold">3. Outer Core (2900–5100 km)</text>')
    html = html.replace('<text x="80" y="85" fill="#a16207" font-size="13" font-weight="bold">4. Inner Core (5100–6371 km)</text>', '</g><g id="layer-inner-core" data-lecture-section="layer_inner_core" style="cursor:pointer;"><text x="80" y="85" fill="#a16207" font-size="13" font-weight="bold">4. Inner Core (5100–6371 km)</text>')
    # close inner core g
    html = html.replace('• Temp: ~5500°C (Extreme Pressure)</text>', '• Temp: ~5500°C (Extreme Pressure)</text></g>')
    
    # 3. Section 2: Plate Tectonics
    html = re.sub(
        r'(<h2 style="color:#b91c1c;[^"]*">\s*2\. Plate Tectonics and Driving Mechanisms\s*</h2>)',
        r'<div id="sec-driving-mechanisms" class="lecture-interactive-card" data-lecture-section="sec_driving_mechanisms" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 3
    html = re.sub(
        r'(\s*)(<h2 style="color:#b91c1c;[^"]*">\s*3\. Types of Plate Boundaries)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Driving mechanisms cards
    html = html.replace(
        '<li style="margin-bottom:10px;"><strong>Slab Pull (Primary Driving Force):</strong>',
        '<div id="card-slab-pull" class="lecture-interactive-card" data-lecture-section="driver_slab_pull" style="cursor:pointer; padding:6px; border-radius:6px;"><li style="margin-bottom:10px;"><strong>Slab Pull (Primary Driving Force):</strong>'
    )
    html = html.replace(
        '<li><strong>Ridge Push (Gravitational Sliding):</strong>',
        '</div><div id="card-ridge-push" class="lecture-interactive-card" data-lecture-section="driver_ridge_push" style="cursor:pointer; padding:6px; border-radius:6px;"><li><strong>Ridge Push (Gravitational Sliding):</strong>'
    )
    html = html.replace('exerting a lateral pushing force upon the plate.</li>\n      </ol>', 'exerting a lateral pushing force upon the plate.</li></div>\n      </ol>')
    
    # 4. Section 3: Boundary Types
    html = re.sub(
        r'(<h2 style="color:#b91c1c;[^"]*">\s*3\. Types of Plate Boundaries\s*</h2>)',
        r'<div id="sec-boundary-types" class="lecture-interactive-card" data-lecture-section="sec_boundary_types" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 4
    html = re.sub(
        r'(\s*)(<h2 style="color:#b91c1c;[^"]*">\s*4\. Global Distribution of Earthquakes)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Boundary rows in Table
    html = html.replace('<tr>\n            <td style="padding:10px 14px; border:1px solid #e2e8f0; font-weight:bold; color:#0369a1;">Constructive (Divergent)</td>', '<tr id="card-bnd-constructive" class="lecture-interactive-card" data-lecture-section="bnd_constructive" style="cursor:pointer;">\n            <td style="padding:10px 14px; border:1px solid #e2e8f0; font-weight:bold; color:#0369a1;">Constructive (Divergent)</td>')
    html = html.replace('<tr style="background:#f8fafc;">\n            <td style="padding:10px 14px; border:1px solid #e2e8f0; font-weight:bold; color:#dc2626;">Destructive (Subduction)</td>', '<tr id="card-bnd-destructive" class="lecture-interactive-card" data-lecture-section="bnd_destructive" style="background:#f8fafc; cursor:pointer;">\n            <td style="padding:10px 14px; border:1px solid #e2e8f0; font-weight:bold; color:#dc2626;">Destructive (Subduction)</td>')
    html = html.replace('<tr>\n            <td style="padding:10px 14px; border:1px solid #e2e8f0; font-weight:bold; color:#d97706;">Collision (Continental)</td>', '<tr id="card-bnd-collision" class="lecture-interactive-card" data-lecture-section="bnd_collision" style="cursor:pointer;">\n            <td style="padding:10px 14px; border:1px solid #e2e8f0; font-weight:bold; color:#d97706;">Collision (Continental)</td>')
    html = html.replace('<tr style="background:#f8fafc;">\n            <td style="padding:10px 14px; border:1px solid #e2e8f0; font-weight:bold; color:#475569;">Conservative (Transform)</td>', '<tr id="card-bnd-conservative" class="lecture-interactive-card" data-lecture-section="bnd_conservative" style="background:#f8fafc; cursor:pointer;">\n            <td style="padding:10px 14px; border:1px solid #e2e8f0; font-weight:bold; color:#475569;">Conservative (Transform)</td>')
    
    # 5. Section 4: Hazard Belts
    html = re.sub(
        r'(<h2 style="color:#b91c1c;[^"]*">\s*4\. Global Distribution of Earthquakes and Volcanoes\s*</h2>)',
        r'<div id="sec-hazard-belts" class="lecture-interactive-card" data-lecture-section="sec_hazard_belts" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    
    # Belts in SVG 2
    html = html.replace('<path d="M 170 120 Q 215 200 210 290 Q 150 370 140 430" fill="none" stroke="#ef4444" stroke-width="4" filter="url(#glow1)"/>', '<g id="belt-ring-of-fire" data-lecture-section="belt_ring_of_fire" style="cursor:pointer;"><path d="M 170 120 Q 215 200 210 290 Q 150 370 140 430" fill="none" stroke="#ef4444" stroke-width="4" filter="url(#glow1)"/><path d="M 770 110 Q 740 210 740 310 Q 755 390 770 430" fill="none" stroke="#ef4444" stroke-width="4" filter="url(#glow1)"/><path d="M 230 130 L 320 210 L 330 420" fill="none" stroke="#ef4444" stroke-width="3.5" filter="url(#glow1)"/></g>')
    # remove duplicate paths replaced above
    html = html.replace('<path d="M 770 110 Q 740 210 740 310 Q 755 390 770 430" fill="none" stroke="#ef4444" stroke-width="4" filter="url(#glow1)"/>\n    <path d="M 230 130 L 320 210 L 330 420" fill="none" stroke="#ef4444" stroke-width="3.5" filter="url(#glow1)"/>', '')
    
    # Mid-Atlantic
    html = html.replace('<path d="M 460 60 Q 470 140 450 200 Q 470 300 460 440" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4"/>', '<g id="belt-mid-atlantic" data-lecture-section="belt_mid_atlantic" style="cursor:pointer;"><path d="M 460 60 Q 470 140 450 200 Q 470 300 460 440" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4"/></g>')
    
    # Himalayas
    html = html.replace('<path d="M 620 205 L 680 215" fill="none" stroke="#ef4444" stroke-width="5"/>', '<g id="belt-himalayas" data-lecture-section="belt_himalayas" style="cursor:pointer;"><path d="M 620 205 L 680 215" fill="none" stroke="#ef4444" stroke-width="5"/>')
    html = html.replace('<text x="650" y="195" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">Himalayas (Collision)</text>', '<text x="650" y="195" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">Himalayas (Collision)</text></g>')
    
    # Hotspots Hawaii & Yellowstone
    html = html.replace('<g class="hotspot-item">', '<g id="belt-hotspots" class="hotspot-item" data-lecture-section="belt_hotspots" style="cursor:pointer;">', 1)
    
    # Close section 4 at end
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
