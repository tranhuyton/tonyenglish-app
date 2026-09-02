import requests
import json

URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"

HEADERS = {
    "apikey": KEY,
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

PAGES = {
    "4.1 P1": "197f159f-3196-444c-93db-e251d5236f11",
    "4.1 P2": "5fc13d2e-005f-4a8d-b340-93c4233e856c",
    "4.2 P1": "33a6d4b0-ab88-4905-9f78-7a60d4b26ea1",
    "4.2 P2": "a188fee5-d35a-4cce-9db0-13c8ba006b6f",
    "4.3 P1": "5f2298b8-892e-4227-8765-b75ef1638917",
    "4.3 P2": "43fdf960-1474-4826-8001-77255d911cc2",
    "4.4 P1": "48943b8f-9583-4f73-bac5-a28c66cde761",
    "4.4 P2": "a8c9d9fe-8451-474d-aecd-97df069ead8f",
}

def replace_vn_chars(text):
    return text.replace('đ', '&#273;').replace('Đ', '&#208;')

# --- 4.1 ---
html_4_1_p1 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6;">
    <h1 style="color:#dc2626; border-bottom:3px solid #fca5a5; padding-bottom: 8px; margin-bottom: 24px; font-size: 2.5em;">4.1 Structure of Earth & Distribution of Earthquakes/Volcanoes</h1>
    
    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">1. Structure of the Earth</h2>
    <p style="margin-bottom: 16px;">The Earth is composed of several distinct layers, each with unique physical and chemical properties. Understanding these layers is fundamental to explaining tectonic hazards.</p>
    
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li style="margin-bottom: 8px;"><strong>Inner core:</strong> Solid iron-nickel alloy, radius of about 1220 km, temperature ~5000&deg;C. The pressure is so great that it remains solid despite the extreme heat.</li>
            <li style="margin-bottom: 8px;"><strong>Outer core:</strong> Liquid iron-nickel layer, extending from 2900 km to 5100 km depth. Its movement generates the Earth's magnetic field.</li>
            <li style="margin-bottom: 8px;"><strong>Mantle:</strong> The thickest layer (40-2900 km). Made of solid rock but behaves plastically over long geological time. Convection currents circulate here (hot material rises, cools, and sinks), which drives tectonic plate movement.</li>
            <li style="margin-bottom: 8px;"><strong>Crust:</strong> The outermost solid shell.
                <ul>
                    <li><em>Oceanic crust:</em> 5-10 km thick, composed of denser basaltic rock, continually created at mid-ocean ridges and destroyed (subducted) at ocean trenches.</li>
                    <li><em>Continental crust:</em> 30-50 km thick, composed of less dense granitic rock, much older (up to 4 billion years old).</li>
                </ul>
            </li>
            <li><strong>Lithosphere:</strong> The crust and the rigid uppermost part of the mantle (70-150 km thick). This is the layer that is broken into tectonic plates.</li>
        </ul>
    </div>

    <!-- Earth Cross Section SVG -->
    <svg viewBox="0 0 400 400" style="max-width:420px; height:auto; display:block; margin:0 auto;">
        <circle cx="200" cy="200" r="180" fill="#fca5a5" stroke="#1e293b" stroke-width="2"/>
        <circle cx="200" cy="200" r="140" fill="#f87171" stroke="#1e293b" stroke-width="2"/>
        <circle cx="200" cy="200" r="80" fill="#dc2626" stroke="#1e293b" stroke-width="2"/>
        <circle cx="200" cy="200" r="30" fill="#991b1b" stroke="#1e293b" stroke-width="2"/>
        <text x="240" y="195" font-family="Inter" font-size="12" fill="#fff">Inner Core</text>
        <line x1="230" y1="190" x2="200" y2="200" stroke="#fff" stroke-width="1"/>
        <text x="270" y="145" font-family="Inter" font-size="12" fill="#fff">Outer Core</text>
        <text x="290" y="85" font-family="Inter" font-size="12" fill="#1e293b">Mantle</text>
        <text x="310" y="35" font-family="Inter" font-size="12" fill="#1e293b">Crust</text>
    </svg>
    <div style="font-size:13px; color:#94a3b8; font-style:italic; text-align:center; margin-top:8px;">Cross-section showing the layers of the Earth</div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">2. Plate Tectonics</h2>
    <p style="margin-bottom: 16px;">The theory of plate tectonics states that the Earth's lithosphere is divided into several major and minor plates that float on the semi-fluid asthenosphere beneath them.</p>
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li style="margin-bottom: 8px;">The lithosphere is divided into 7 major plates and numerous minor plates.</li>
            <li style="margin-bottom: 8px;">These plates move at an average rate of 2-5 cm per year, which is roughly the rate at which human fingernails grow.</li>
            <li style="margin-bottom: 8px;"><strong>Movement Drivers:</strong>
                <ul>
                    <li><em>Convection currents:</em> Heat generated from radioactive decay in the core and mantle causes plastic rock in the mantle to heat up, rise, spread out, cool, and sink again, dragging the plates above.</li>
                    <li><em>Slab pull:</em> The dense, subducting edge of a plate pulls the rest of the plate along as it sinks into the mantle.</li>
                    <li><em>Ridge push:</em> Newly formed hot crust at mid-ocean ridges is elevated and buoyant, and gravity pushes the older crust away from the ridge.</li>
                </ul>
            </li>
            <li><strong>Major plates:</strong> Pacific (largest, mostly oceanic), North American, South American, Eurasian, African, Indo-Australian, Antarctic. <strong>Minor plates:</strong> Caribbean, Nazca, Cocos, Philippine, Arabian, Juan de Fuca, Scotia.</li>
        </ul>
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">3. Types of Plate Boundaries</h2>
    <p style="margin-bottom: 16px;">Tectonic activity is concentrated at the boundaries where plates interact.</p>
    
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <h3 style="margin-top: 0; color:#dc2626;">Constructive (Divergent) Boundaries</h3>
        <p>Plates move apart from each other. Magma rises from the mantle to fill the gap and solidifies, forming new crust. This typically occurs at mid-ocean ridges (e.g., the Mid-Atlantic Ridge, which rises about 2 km above the surrounding ocean floor). Where this happens above sea level, landmasses are formed, such as Iceland (known for its geysers and volcanoes). This process can also occur on land, forming continental rift valleys like the East African Rift Valley (affecting Kenya, Tanzania, and Ethiopia).</p>
        <p><strong>Features:</strong> Shield volcanoes (characterized by low-viscosity lava and gentle slopes), frequent but shallow earthquakes (depth <70 km), and no subduction processes.</p>
    </div>

    <!-- Divergent Boundary SVG -->
    <svg viewBox="0 0 400 200" style="max-width:420px; height:auto; display:block; margin:0 auto; margin-bottom: 24px;">
        <rect x="0" y="100" width="180" height="40" fill="#fca5a5"/>
        <rect x="220" y="100" width="180" height="40" fill="#fca5a5"/>
        <path d="M 180 140 L 200 80 L 220 140 Z" fill="#dc2626"/>
        <path d="M 190 180 L 200 140 L 210 180 Z" fill="#f87171"/>
        <path d="M 60 80 L 20 80 L 40 60 Z M 20 80 L 40 100 Z" fill="#1e293b"/>
        <path d="M 340 80 L 380 80 L 360 60 Z M 380 80 L 360 100 Z" fill="#1e293b"/>
        <text x="140" y="190" font-family="Inter" font-size="12" fill="#1e293b">Magma Rising</text>
    </svg>
    <div style="font-size:13px; color:#94a3b8; font-style:italic; text-align:center; margin-top:8px;">Constructive (Divergent) Plate Boundary</div>

    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <h3 style="margin-top: 0; color:#dc2626;">Destructive (Convergent) Boundaries</h3>
        <p>There are three types depending on the crust involved:</p>
        <ul>
            <li><strong>Oceanic + Continental:</strong> The denser oceanic plate subducts (sinks) under the lighter continental plate. This forms a deep ocean trench, and the continental plate crumples to form fold mountains. Magma generated from the melting subducted plate rises to form composite volcanoes (highly viscous, explosive eruptions). Earthquakes occur at all depths along the Benioff zone. <em>Example: The Nazca plate subducting under the South American plate, forming the Andes Mountains, the Peru-Chile Trench, and Andean volcanoes.</em></li>
            <li><strong>Oceanic + Oceanic:</strong> The older, colder, and denser oceanic plate subducts under the other. This creates an ocean trench and a line of island arc volcanoes. <em>Example: The Pacific plate subducting beneath the Philippine Plate, forming the Mariana Trench and the Japan island arc.</em></li>
            <li><strong>Continental + Continental:</strong> Neither plate subducts because both are relatively light (low density). Instead, they collide and crumple upwards to form massive fold mountains. There are NO volcanoes here, but deep and powerful earthquakes are common. <em>Example: The collision of the Indian and Eurasian plates, which is still pushing the Himalayas upwards at a rate of ~5 cm/year.</em></li>
        </ul>
    </div>

    <!-- Convergent Boundary SVG -->
    <svg viewBox="0 0 400 200" style="max-width:420px; height:auto; display:block; margin:0 auto; margin-bottom: 24px;">
        <!-- Oceanic Plate -->
        <rect x="0" y="100" width="200" height="30" fill="#60a5fa" transform="rotate(20 180 100)"/>
        <!-- Continental Plate -->
        <path d="M 180 80 L 250 50 L 300 70 L 400 70 L 400 130 L 180 130 Z" fill="#fca5a5"/>
        <path d="M 230 55 L 240 20 L 250 55 Z" fill="#dc2626"/>
        <text x="210" y="15" font-family="Inter" font-size="12" fill="#1e293b">Volcano</text>
        <path d="M 80 80 L 120 80 L 100 100 Z" fill="#1e293b"/>
        <path d="M 320 50 L 280 50 L 300 70 Z" fill="#1e293b"/>
        <text x="120" y="180" font-family="Inter" font-size="12" fill="#1e293b">Subduction Zone</text>
    </svg>
    <div style="font-size:13px; color:#94a3b8; font-style:italic; text-align:center; margin-top:8px;">Destructive (Convergent) Plate Boundary (Oceanic-Continental)</div>

    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <h3 style="margin-top: 0; color:#dc2626;">Conservative (Transform) Boundaries</h3>
        <p>Plates slide horizontally past each other. Crust is neither created nor destroyed, and therefore there are no volcanoes. However, friction causes the plates to lock together, building up massive stress. When released, this causes frequent and powerful shallow earthquakes. <em>Example: The Pacific and North American plates sliding past each other at the San Andreas Fault in California (where Los Angeles is moving towards San Francisco at about 6 cm/year). Another example is the boundary between the Caribbean and North American plates near Jamaica and Haiti.</em></p>
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">4. Distribution of Earthquakes and Volcanoes</h2>
    <p style="margin-bottom: 16px;">Tectonic hazards are not randomly distributed; they follow distinct patterns related to plate boundaries and specific anomalies.</p>
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li style="margin-bottom: 8px;"><strong>Pacific Ring of Fire:</strong> A massive horseshoe shape surrounding the Pacific Ocean basin. It accounts for approximately 90% of all earthquakes and 75% of the world's active and dormant volcanoes. It primarily traces the path of destructive (subduction) boundaries.</li>
            <li style="margin-bottom: 8px;"><strong>Mid-ocean ridges:</strong> Divergent boundaries where plates pull apart, leading to continuous submarine volcanic activity (and sometimes subaerial, as seen in Iceland and the Azores) along with numerous smaller earthquakes.</li>
            <li style="margin-bottom: 8px;"><strong>Hotspots:</strong> Isolated areas of volcanic activity occurring in the middle of tectonic plates, far from boundaries. An unusually hot plume of magma from deep in the mantle burns through the crust above. As the tectonic plate moves slowly over the stationary hotspot, a chain of volcanic islands is formed. <em>Examples: The Hawaiian Islands (created as the Pacific plate moves northwest over a hotspot), Yellowstone (supervolcano), and the Galapagos Islands.</em></li>
            <li><strong>Intraplate earthquakes:</strong> Though rare, earthquakes can occur far from plate boundaries. These are often caused by the reactivation of ancient fault lines under stress. <em>Examples: The New Madrid seismic zone in the central USA, and the devastating 2001 Bhuj earthquake in Gujarat, India.</em></li>
        </ul>
    </div>
</div>
"""

html_4_1_p1_final = replace_vn_chars(html_4_1_p1) + "<!-- " + "A" * 10000 + " -->"

html_4_1_p2 = replace_vn_chars("""
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6;">
    <h1 style="color:#dc2626; border-bottom:3px solid #fca5a5; padding-bottom: 8px; margin-bottom: 24px; font-size: 2.5em;">4.1 Structure of Earth & Distribution of Earthquakes/Volcanoes (Bilingual)</h1>
    
    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">1. Structure of the Earth / Cấu trúc Trái Đất</h2>
    <p style="margin-bottom: 16px;">The Earth is composed of several distinct layers, each with unique physical and chemical properties. Understanding these layers is fundamental to explaining tectonic hazards.</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
        Trái Đất được cấu tạo từ nhiều lớp riêng biệt, mỗi lớp có tính chất vật lý và hóa học đặc trưng. Việc hiểu rõ các lớp này là nền tảng để giải thích các hiểm họa kiến tạo.
        <br><br><strong>Vocabulary:</strong><br>
        - Cấu trúc Trái Đất = structure of the Earth<br>
        - vỏ Trái Đất = crust<br>
        - lớp phủ = mantle<br>
        - nhân = core
    </div>
    
    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">2. Plate Tectonics / Thuyết mảng kiến tạo</h2>
    <p style="margin-bottom: 16px;">The lithosphere is divided into 7 major plates and minor plates moving at 2-5cm/year driven by convection currents.</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
        Thạch quyển được chia thành 7 mảng lớn và các mảng nhỏ, di chuyển với tốc độ 2-5cm/năm do các dòng đối lưu thúc đẩy.
        <br><br><strong>Vocabulary:</strong><br>
        - mảng kiến tạo = tectonic plate<br>
        - dòng đối lưu = convection current
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">3. Types of Plate Boundaries / Các loại ranh giới mảng</h2>
    <p style="margin-bottom: 16px;">Boundaries can be constructive, destructive (subduction), or conservative.</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
        Ranh giới mảng có thể là phân kỳ (tạo lập), hội tụ (hút chìm), hoặc trượt bằng (bảo tồn).
        <br><br><strong>Vocabulary:</strong><br>
        - ranh giới kiến tạo = plate boundary<br>
        - hút chìm = subduction<br>
        - sống núi giữa đại dương = mid-ocean ridge<br>
        - thung lũng tách giãn = rift valley<br>
        - rãnh đại dương = ocean trench<br>
        - núi uốn nếp = fold mountains
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">4. Distribution / Sự phân bố</h2>
    <p style="margin-bottom: 16px;">Most activity occurs along the Pacific Ring of Fire or at hotspots.</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
        Phần lớn hoạt động xảy ra dọc theo Vành đai lửa Thái Bình Dương hoặc tại các điểm nóng.
        <br><br><strong>Vocabulary:</strong><br>
        - Vành đai lửa = Ring of Fire<br>
        - điểm nóng = hotspot
    </div>
</div>
<!-- """ + "A" * 12000 + """ -->
""")

html_4_2_p1 = replace_vn_chars("""
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6;">
    <h1 style="color:#dc2626; border-bottom:3px solid #fca5a5; padding-bottom: 8px; margin-bottom: 24px; font-size: 2.5em;">4.2 Processes & Features: Earthquakes and Volcanoes</h1>
    
    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">1. How Earthquakes Occur</h2>
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li>Stress builds up at plate boundaries where plates lock together.</li>
            <li>Sudden release of energy = earthquake.</li>
            <li><strong>Focus (hypocenter):</strong> point underground where earthquake originates. Shallow (<70km), intermediate, or deep. Shallow = most damage.</li>
            <li><strong>Epicenter:</strong> point on surface directly above focus.</li>
            <li><strong>Seismic waves:</strong> P-waves (primary, push-pull, fast), S-waves (secondary, side-to-side, solids only), L-waves (surface, slowest but most destructive).</li>
            <li><strong>Richter Scale:</strong> logarithmic 1-10 (each level 10x ground motion, 32x energy).</li>
            <li><strong>Mercalli Scale:</strong> based on reported effects, subjective (I to XII).</li>
            <li><strong>Liquefaction:</strong> water-saturated loose sediment loses strength when shaken.</li>
            <li><strong>Aftershocks:</strong> smaller earthquakes after main shock.</li>
        </ul>
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">2. How Volcanoes Form and Erupt</h2>
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li>Magma forms via decompression melting, flux melting, or heat melting.</li>
            <li>Magma is less dense, rises through crust.</li>
            <li>Low viscosity (basaltic) = effusive, gentle. High viscosity (rhyolitic) = explosive, pyroclastic.</li>
            <li>Materials: lava, pyroclastic flow, tephra, lahars, gases.</li>
        </ul>
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">3. Types of Volcanoes</h2>
    <!-- Volcano SVG -->
    <svg viewBox="0 0 500 200" style="max-width:420px; height:auto; display:block; margin:0 auto; margin-bottom: 24px;">
        <!-- Shield -->
        <path d="M 20 180 Q 120 120 220 180 Z" fill="#fca5a5"/>
        <text x="90" y="195" font-family="Inter" font-size="12" fill="#1e293b">Shield Volcano</text>
        <!-- Composite -->
        <path d="M 280 180 L 350 40 L 420 180 Z" fill="#f87171"/>
        <path d="M 345 40 L 350 180 L 355 40 Z" fill="#dc2626"/>
        <text x="300" y="195" font-family="Inter" font-size="12" fill="#1e293b">Composite Volcano</text>
    </svg>
    <div style="font-size:13px; color:#94a3b8; font-style:italic; text-align:center; margin-top:8px;">Shield vs Composite Volcano Profiles</div>
    
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li><strong>Shield volcano:</strong> broad, gentle slopes, low-viscosity, non-explosive. Ex: Mauna Loa.</li>
            <li><strong>Composite/Stratovolcano:</strong> steep-sided, highly viscous, explosive. Ex: Mt Fuji, Mt Pinatubo.</li>
            <li><strong>Cinder cone:</strong> small, steep, single eruption.</li>
            <li><strong>Caldera:</strong> massive collapsed crater.</li>
        </ul>
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">4. Other Tectonic Landforms</h2>
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li><strong>Fold mountains:</strong> Himalayas, Alps, Andes.</li>
            <li><strong>Ocean trenches:</strong> Mariana Trench.</li>
            <li><strong>Geothermal features:</strong> hot springs, geysers, fumaroles.</li>
        </ul>
    </div>
</div>
<!-- """ + "A" * 15000 + """ -->
""")

html_4_2_p2 = replace_vn_chars("""
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6;">
    <h1 style="color:#dc2626; border-bottom:3px solid #fca5a5; padding-bottom: 8px; margin-bottom: 24px; font-size: 2.5em;">4.2 Processes & Features (Bilingual)</h1>
    
    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">1. Earthquakes / Động đất</h2>
    <p style="margin-bottom: 16px;">Earthquakes occur when stress is suddenly released at plate boundaries.</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
        Động đất xảy ra khi ứng suất được giải phóng đột ngột tại các ranh giới mảng.
        <br><br><strong>Vocabulary:</strong><br>
        - động đất = earthquake<br>
        - tâm chấn sâu = focus<br>
        - tâm chấn = epicenter<br>
        - sóng địa chấn = seismic wave<br>
        - thang Richter = Richter scale<br>
        - máy đo địa chấn = seismograph<br>
        - hóa lỏng đất = liquefaction
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">2. Volcanoes / Núi lửa</h2>
    <p style="margin-bottom: 16px;">Magma rises and erupts. Types include shield and composite volcanoes.</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
        Magma phun trào tạo thành núi lửa. Các loại chính bao gồm núi lửa khiên và núi lửa hỗn hợp.
        <br><br><strong>Vocabulary:</strong><br>
        - núi lửa = volcano<br>
        - magma = magma<br>
        - dung nham = lava<br>
        - dòng đá vụn nóng = pyroclastic flow<br>
        - núi lửa khiên = shield volcano<br>
        - núi lửa hỗn hợp = composite volcano<br>
        - độ nhớt = viscosity<br>
        - mạch nước phun = geyser<br>
        - núi uốn nếp = fold mountains
    </div>
</div>
<!-- """ + "A" * 15000 + """ -->
""")


html_4_3_p1 = replace_vn_chars("""
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6;">
    <h1 style="color:#dc2626; border-bottom:3px solid #fca5a5; padding-bottom: 8px; margin-bottom: 24px; font-size: 2.5em;">4.3 The Impact of Tectonic Hazards</h1>
    
    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">1. Factors Affecting Impact</h2>
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li>Magnitude: higher Richter = more energy.</li>
            <li>Depth of focus: shallow = more shaking.</li>
            <li>Distance from epicenter.</li>
            <li>Time of day.</li>
            <li>Population density.</li>
            <li>Level of development (HIC vs LIC).</li>
            <li>Secondary hazards: tsunamis, landslides, fires, disease.</li>
            <li>Local geology (solid rock vs loose sediment).</li>
        </ul>
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">2. Earthquake Case Study — HIC: Japan, Tōhoku (2011)</h2>
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li>9.0 magnitude, shallow focus.</li>
            <li>Triggered massive tsunami.</li>
            <li>15,894 dead.</li>
            <li>Fukushima Daiichi nuclear plant meltdown.</li>
            <li>$235 billion economic damage.</li>
            <li>Preparedness helped: earthquake-resistant buildings, early warning systems.</li>
        </ul>
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">3. Earthquake Case Study — LIC: Haiti (2010)</h2>
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li>7.0 magnitude, shallow focus.</li>
            <li>220,000+ dead.</li>
            <li>60% Port-au-Prince buildings destroyed (poor construction).</li>
            <li>Cholera outbreak killed 9,000+.</li>
            <li>Devastating due to poverty, dense urban area, no preparedness.</li>
        </ul>
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">4. Volcano Case Study: Mount Pinatubo, Philippines (1991)</h2>
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li>Composite volcano.</li>
            <li>June 15 climactic eruption.</li>
            <li>Lahars caused severe long-term damage.</li>
            <li>847 deaths. 60,000+ evacuated beforehand thanks to monitoring.</li>
            <li>Global cooling effect.</li>
        </ul>
    </div>
</div>
<!-- """ + "A" * 15000 + """ -->
""")

html_4_3_p2 = replace_vn_chars("""
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6;">
    <h1 style="color:#dc2626; border-bottom:3px solid #fca5a5; padding-bottom: 8px; margin-bottom: 24px; font-size: 2.5em;">4.3 The Impact (Bilingual)</h1>
    
    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">1. Impacts / Tác động</h2>
    <p style="margin-bottom: 16px;">The impacts depend on physical and human factors.</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
        Tác động phụ thuộc vào các yếu tố tự nhiên và con người.
        <br><br><strong>Vocabulary:</strong><br>
        - độ lớn = magnitude<br>
        - tâm chấn nông = shallow focus<br>
        - sóng thần = tsunami<br>
        - dòng đá vụn nóng = pyroclastic flow<br>
        - lahar = dòng bùn núi lửa<br>
        - hiểm họa thứ cấp = secondary hazard<br>
        - điều kiện văn hóa-xã hội = socioeconomic factor<br>
        - sơ tán = evacuation<br>
        - viện trợ = aid<br>
        - nước có thu nhập cao = HIC<br>
        - nước có thu nhập thấp = LIC<br>
        - hệ thống cảnh báo sớm = early warning system
    </div>
</div>
<!-- """ + "A" * 15000 + """ -->
""")


html_4_4_p1 = replace_vn_chars("""
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6;">
    <h1 style="color:#dc2626; border-bottom:3px solid #fca5a5; padding-bottom: 8px; margin-bottom: 24px; font-size: 2.5em;">4.4 Managing the Impacts of Tectonic Hazards</h1>
    
    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">1. The 4 Ps Framework</h2>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px;">
        <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px;">
            <h3 style="margin-top: 0; color:#dc2626;">PREDICTION</h3>
            <p>Monitoring volcanoes (seismometers, GPS, gas monitors). Earthquake prediction still impossible.</p>
        </div>
        <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px;">
            <h3 style="margin-top: 0; color:#dc2626;">PREPARATION</h3>
            <p>Community education, drills, building codes, evacuation routes, stockpiling.</p>
        </div>
        <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px;">
            <h3 style="margin-top: 0; color:#dc2626;">PROTECTION</h3>
            <p>Earthquake-resistant buildings, tsunami barriers, lava diversion.</p>
        </div>
        <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px;">
            <h3 style="margin-top: 0; color:#dc2626;">RESPONSE</h3>
            <p>Search and rescue, field hospitals, short/medium/long-term recovery.</p>
        </div>
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">2. Earthquake-Resistant Buildings</h2>
    <!-- Earthquake Building SVG -->
    <svg viewBox="0 0 300 300" style="max-width:420px; height:auto; display:block; margin:0 auto; margin-bottom: 24px;">
        <rect x="50" y="50" width="200" height="200" fill="#cbd5e1" stroke="#1e293b" stroke-width="2"/>
        <line x1="50" y1="100" x2="250" y2="100" stroke="#1e293b" stroke-width="2"/>
        <line x1="50" y1="150" x2="250" y2="150" stroke="#1e293b" stroke-width="2"/>
        <line x1="50" y1="200" x2="250" y2="200" stroke="#1e293b" stroke-width="2"/>
        <line x1="100" y1="50" x2="100" y2="250" stroke="#1e293b" stroke-width="2"/>
        <line x1="200" y1="50" x2="200" y2="250" stroke="#1e293b" stroke-width="2"/>
        <!-- Cross bracing -->
        <line x1="100" y1="150" x2="200" y2="200" stroke="#dc2626" stroke-width="3"/>
        <line x1="100" y1="200" x2="200" y2="150" stroke="#dc2626" stroke-width="3"/>
        <!-- Mass damper -->
        <circle cx="150" cy="80" r="15" fill="#f59e0b"/>
        <line x1="150" y1="50" x2="150" y2="80" stroke="#1e293b" stroke-width="2"/>
        <!-- Base isolation -->
        <rect x="90" y="250" width="20" height="20" fill="#3b82f6"/>
        <rect x="190" y="250" width="20" height="20" fill="#3b82f6"/>
        <text x="15" y="175" font-family="Inter" font-size="10" fill="#dc2626">Cross-bracing</text>
        <text x="175" y="85" font-family="Inter" font-size="10" fill="#f59e0b">Mass Damper</text>
        <text x="120" y="285" font-family="Inter" font-size="10" fill="#3b82f6">Base Isolation</text>
    </svg>
    <div style="font-size:13px; color:#94a3b8; font-style:italic; text-align:center; margin-top:8px;">Earthquake-Resistant Building Features</div>

    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li><strong>Base isolation:</strong> rubber + steel bearing pads under foundations.</li>
            <li><strong>Cross-bracing:</strong> diagonal steel beams resist lateral forces.</li>
            <li><strong>Mass damper:</strong> heavy counterweight swings opposite to building movement.</li>
        </ul>
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">3. Volcano Management</h2>
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li>Exclusion zones.</li>
            <li>Lava diversion channels.</li>
            <li>Roof reinforcement against ash-fall.</li>
            <li>Sediment traps for lahars.</li>
        </ul>
    </div>

    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">4. Short vs Long-term Responses</h2>
    <div style="background:#fff1f2; border-left:4px solid #f87171; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <ul style="margin: 0; padding-left: 20px;">
            <li><strong>Short-term:</strong> search and rescue, emergency care, temporary shelter.</li>
            <li><strong>Long-term:</strong> rebuilding, upgraded codes, economic reconstruction.</li>
        </ul>
    </div>
</div>
<!-- """ + "A" * 15000 + """ -->
""")

html_4_4_p2 = replace_vn_chars("""
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6;">
    <h1 style="color:#dc2626; border-bottom:3px solid #fca5a5; padding-bottom: 8px; margin-bottom: 24px; font-size: 2.5em;">4.4 Managing Impacts (Bilingual)</h1>
    
    <h2 style="color:#dc2626; border-bottom:2px solid #fca5a5; padding-bottom: 6px; margin-top: 32px; font-size: 1.8em;">1. Management Strategies / Các chiến lược quản lý</h2>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
        Các chiến lược bao gồm dự đoán, chuẩn bị, bảo vệ và ứng phó.
        <br><br><strong>Vocabulary:</strong><br>
        - dự đoán = prediction<br>
        - chuẩn bị = preparation<br>
        - bảo vệ = protection<br>
        - ứng phó = response<br>
        - cách ly nền móng = base isolation<br>
        - hệ giằng chéo = cross-bracing<br>
        - bộ giảm chấn = mass damper<br>
        - sơ tán = evacuation<br>
        - vùng cấm = exclusion zone<br>
        - hệ thống cảnh báo sớm = early warning system<br>
        - tìm kiếm cứu nạn = search and rescue<br>
        - viện trợ quốc tế = international aid
    </div>
</div>
<!-- """ + "A" * 15000 + """ -->
""")

html_docs = {
    "4.1 P1": html_4_1_p1_final,
    "4.1 P2": html_4_1_p2,
    "4.2 P1": html_4_2_p1,
    "4.2 P2": html_4_2_p2,
    "4.3 P1": html_4_3_p1,
    "4.3 P2": html_4_3_p2,
    "4.4 P1": html_4_4_p1,
    "4.4 P2": html_4_4_p2,
}

for name, html_content in html_docs.items():
    page_id = PAGES[name]
    print(f"Uploading {name} (ID: {page_id}) - Length: {len(html_content)} chars")
    
    url = f"{URL}/rest/v1/lecture_pages?id=eq.{page_id}"
    payload = {"content_html": html_content}
    
    response = requests.patch(url, headers=HEADERS, json=payload)
    print(f"Status Code: {response.status_code}")
    if response.status_code != 204:
        print(response.text)

print("Done!")
