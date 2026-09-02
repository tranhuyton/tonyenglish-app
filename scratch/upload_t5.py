import urllib.request
import json
import urllib.error

def encode_html(text):
    return text.encode('ascii', 'xmlcharrefreplace').decode('ascii')

# ==========================================
# 5.1 P1
# ==========================================
p5_1_1 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6; font-size: 16px;">
    <h1 style="color:#0891b2; border-bottom:3px solid #67e8f9; padding-bottom: 8px; margin-top: 0;">5.1 Natural & Human Causes of Climate Change</h1>
    
    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 24px; padding-bottom: 4px;">1. What is Climate Change?</h2>
    <p>To understand climate change, it is essential to distinguish between weather and climate:</p>
    <ul style="margin-bottom: 16px;">
        <li><strong>Weather</strong> refers to the short-term atmospheric conditions at a specific place and time (e.g., raining today, sunny tomorrow).</li>
        <li><strong>Climate</strong> is the average of these weather patterns over a long period, typically 30 years or more, at a specific location.</li>
        <li><strong>Climate change</strong> denotes a long-term, significant change in global or regional climate patterns.</li>
    </ul>
    
    <div style="background:#ecfeff; border-left:4px solid #22d3ee; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <h3 style="margin-top:0; color:#0891b2;">Evidence of Climate Change</h3>
        <p>Scientific data confirms that our planet is warming at an unprecedented rate:</p>
        <ul>
            <li><strong>Global Temperature Records:</strong> Data from NASA and NOAA show a +1.2°C increase in global temperatures since 1880, with most of this warming occurring since 1975.</li>
            <li><strong>Ice Cores:</strong> Deep ice cores extracted from Greenland and Antarctica contain bubbles of ancient air. These bubbles reveal a direct correlation between carbon dioxide (CO₂) levels and temperature going back 800,000 years.</li>
            <li><strong>Glacier Retreat and Ice Loss:</strong> The Himalayan and Alpine glaciers are retreating rapidly. The Greenland ice sheet is losing approximately 280 billion tonnes of ice per year.</li>
            <li><strong>Arctic Sea Ice:</strong> The extent of Arctic sea ice is declining by 13% per decade.</li>
            <li><strong>Coral Bleaching:</strong> There has been an increase in mass coral bleaching events globally, driven by warmer ocean temperatures.</li>
        </ul>
    </div>

    <!-- Temperature Trend Graph SVG -->
    <svg viewBox="0 0 420 250" style="max-width:420px;height:auto;display:block;margin:20px auto;background:#fff;">
        <rect width="420" height="250" fill="#f8fafc"/>
        <text x="210" y="25" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0891b2">Global Temperature Anomaly (1880-2020)</text>
        <line x1="40" y1="200" x2="380" y2="200" stroke="#94a3b8" stroke-width="2"/>
        <line x1="40" y1="40" x2="40" y2="200" stroke="#94a3b8" stroke-width="2"/>
        <text x="35" y="200" text-anchor="end" font-size="10" fill="#64748b">0.0°C</text>
        <text x="35" y="120" text-anchor="end" font-size="10" fill="#64748b">+0.6°C</text>
        <text x="35" y="40" text-anchor="end" font-size="10" fill="#64748b">+1.2°C</text>
        <text x="40" y="215" font-size="10" fill="#64748b">1880</text>
        <text x="210" y="215" text-anchor="middle" font-size="10" fill="#64748b">1950</text>
        <text x="380" y="215" text-anchor="end" font-size="10" fill="#64748b">2020</text>
        <path d="M40,195 Q90,190 140,185 T240,160 T320,100 T380,45" fill="none" stroke="#ef4444" stroke-width="3"/>
        <circle cx="380" cy="45" r="4" fill="#ef4444"/>
    </svg>

    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 32px; padding-bottom: 4px;">2. Natural Causes of Climate Change</h2>
    <p>Before the Industrial Revolution, the Earth's climate changed due to natural factors. These are still active today but cannot explain the rapid warming we see now.</p>
    
    <div style="background:#ecfeff; border-left:4px solid #22d3ee; padding:14px; border-radius:8px; margin-bottom: 16px;">
        <h3 style="margin-top:0; color:#0891b2;">Milankovitch Cycles</h3>
        <p>These are long-term changes in the Earth's orbit and tilt that affect the amount of solar energy the Earth receives. They are responsible for historical ice ages (glacials) and warm periods (interglacials).</p>
        <ol>
            <li><strong>Eccentricity (100,000-year cycle):</strong> The shape of Earth's orbit around the sun slowly changes from near-circular to more elliptical.</li>
            <li><strong>Axial Tilt (41,000-year cycle):</strong> The Earth's tilt varies between 22.1° and 24.5°, affecting the severity of seasons.</li>
            <li><strong>Precession (26,000-year cycle):</strong> The 'wobble' of the Earth's axis, like a spinning top.</li>
        </ol>
    </div>

    <p><strong>Volcanic Activity:</strong> Large volcanic eruptions can inject sulfur dioxide (SO₂) high into the stratosphere. This creates sulfate aerosols that reflect incoming sunlight, causing temporary global cooling. For example, the eruption of Mt. Pinatubo in 1991 cooled the Earth by about 0.5°C for two years. The 1815 Mt. Tambora eruption caused the infamous "Year Without a Summer" in 1816. While volcanoes also release CO₂, human emissions are currently over 100 times greater than volcanic emissions.</p>

    <p><strong>Solar Output Variations:</strong> The sun's energy output varies in an 11-year sunspot cycle. More sunspots mean slightly more solar energy. Historically, the <em>Maunder Minimum</em> (1645-1715) was a period with very few sunspots, contributing to the "Little Ice Age" when the Thames River in London froze. However, solar output has been relatively flat or slightly decreasing since 1980, while global temperatures have spiked, ruling out the sun as the cause of current warming.</p>

    <p><strong>Oceanic Circulation:</strong> Short-term climate variations are influenced by ocean currents, such as the Atlantic Meridional Overturning Circulation (AMOC) and the El Niño/La Niña cycle in the Pacific.</p>

    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 32px; padding-bottom: 4px;">3. Human Causes (The Enhanced Greenhouse Effect)</h2>
    
    <p>The <strong>natural greenhouse effect</strong> is essential for life. The Earth's atmosphere acts like the glass of a greenhouse. Short-wave solar radiation passes through the atmosphere and warms the Earth's surface. The Earth then re-emits this energy as long-wave infrared radiation. Greenhouse gases in the atmosphere absorb this long-wave radiation and re-emit it in all directions, trapping heat. Without this natural effect, Earth's average temperature would be a freezing -18°C instead of the comfortable +15°C we experience.</p>
    
    <p>The <strong>enhanced greenhouse effect</strong> occurs when human activities increase the concentration of these gases beyond natural levels, trapping too much heat and causing global warming.</p>

    <!-- Greenhouse Effect Diagram SVG -->
    <svg viewBox="0 0 420 280" style="max-width:420px;height:auto;display:block;margin:20px auto;background:#fff;">
        <rect width="420" height="280" fill="#f0f9ff"/>
        <!-- Sun -->
        <circle cx="50" cy="50" r="30" fill="#fbbf24"/>
        <!-- Earth Surface -->
        <path d="M0,230 Q210,210 420,230 L420,280 L0,280 Z" fill="#22c55e"/>
        <!-- Atmosphere Layer -->
        <path d="M0,120 Q210,100 420,120" fill="none" stroke="#60a5fa" stroke-width="20" stroke-opacity="0.3"/>
        <text x="210" y="125" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1d4ed8">Atmosphere (Greenhouse Gases)</text>
        
        <!-- Short wave from sun -->
        <path d="M70,70 L200,220" fill="none" stroke="#f59e0b" stroke-width="3" stroke-dasharray="5,5"/>
        <polygon points="200,220 190,212 198,206" fill="#f59e0b" transform="rotate(50 200 220)"/>
        
        <!-- Long wave emitted from earth -->
        <path d="M250,220 L300,130" fill="none" stroke="#ef4444" stroke-width="3"/>
        <polygon points="300,130 292,138 298,144" fill="#ef4444" transform="rotate(-60 300 130)"/>
        
        <!-- Trapped heat -->
        <path d="M300,130 L350,210" fill="none" stroke="#ef4444" stroke-width="3"/>
        <polygon points="350,210 342,202 348,196" fill="#ef4444" transform="rotate(130 350 210)"/>
        
        <!-- Escaping heat -->
        <path d="M300,130 L320,50" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4"/>
        
        <text x="60" y="160" font-family="sans-serif" font-size="10" fill="#b45309">Short-wave<br/>solar radiation</text>
        <text x="360" y="170" font-family="sans-serif" font-size="10" fill="#991b1b">Long-wave<br/>infrared trapped</text>
    </svg>

    <div style="background:#ecfeff; border-left:4px solid #22d3ee; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <h3 style="margin-top:0; color:#0891b2;">Key Greenhouse Gases (GHGs)</h3>
        <ul>
            <li><strong>Carbon Dioxide (CO₂):</strong> Currently at 420 ppm (up from 280 ppm pre-industrial), the highest level in 3 million years. It stays in the atmosphere for hundreds of years. Sources include burning fossil fuels (78%), deforestation (12%), and cement production (4%).</li>
            <li><strong>Methane (CH₄):</strong> 30 times more powerful at trapping heat than CO₂ over a 100-year period, though it only stays in the atmosphere for about 12 years. Sources include livestock (enteric fermentation—cows and sheep burping/farting accounts for 14% of total GHG), rice paddies, landfill decomposition, oil/gas drilling ('fugitive emissions'), and thawing permafrost.</li>
            <li><strong>Nitrous Oxide (N₂O):</strong> 265 times more powerful than CO₂. Sources include synthetic agricultural fertilisers and vehicle exhausts.</li>
            <li><strong>Chlorofluorocarbons (CFCs):</strong> Up to 10,000 times more powerful than CO₂. Historically used in fridges and aerosols, they are now being phased out under the Montreal Protocol.</li>
        </ul>
    </div>

    <p><strong>Primary Human Activities Driving Emissions:</strong></p>
    <ul>
        <li><strong>Fossil Fuels:</strong> Burning coal, oil, and gas for electricity, heat, and transport accounts for roughly 64% of global emissions.</li>
        <li><strong>Deforestation:</strong> Cutting down forests not only releases stored carbon into the air but also destroys vital 'carbon sinks' that absorb CO₂.</li>
        <li><strong>Agriculture:</strong> Intensive farming, excessive fertiliser use, and massive cattle ranches produce vast amounts of methane and nitrous oxide.</li>
    </ul>

    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 32px; padding-bottom: 4px;">4. Evidence and Attribution</h2>
    <p>How do we know humans are responsible? </p>
    <ul>
        <li><strong>Climate Models (GCMs):</strong> When scientists run General Circulation Models using <em>only</em> natural factors (volcanoes, sun), they fail to simulate modern warming. The models only match the observed rapid temperature rise perfectly when human GHG emissions are included. There is a 97%+ scientific consensus that human activity is the primary driver.</li>
        <li><strong>Carbon Fingerprinting:</strong> Isotopic analysis of atmospheric CO₂ shows an increasing proportion of lighter carbon-12. This specific isotope profile indicates the carbon comes from burning ancient plants (fossil fuels), not from natural volcanic sources.</li>
    </ul>
</div>
"""

p5_1_2 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6; font-size: 16px;">
    <h1 style="color:#0891b2; border-bottom:3px solid #67e8f9; padding-bottom: 8px; margin-top: 0;">5.1 Review & Bilingual Notes</h1>
    
    <p>In the previous section, we explored the mechanisms of the climate system, the historical natural causes of climate change, and the overwhelming evidence pointing to the human-driven enhanced greenhouse effect. Below is a bilingual review of the core concepts and vocabulary essential for your IGCSE Geography exam.</p>

    <div style="background:#ecfeff; border-left:4px solid #22d3ee; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <h3 style="margin-top:0; color:#0891b2;">Summary of Key Concepts</h3>
        <ul>
            <li><strong>Natural vs. Enhanced:</strong> The natural greenhouse effect keeps Earth habitable (+15°C). The <em>enhanced</em> greenhouse effect is the artificial amplification of this process by human-released gases.</li>
            <li><strong>Major Gases:</strong> CO₂ (most abundant human GHG, lasts centuries), CH₄ (very potent, from agriculture/waste), N₂O (from fertilisers).</li>
            <li><strong>Fossil Fuels:</strong> The primary culprit. Coal, oil, and gas account for the vast majority of new CO₂ entering the atmosphere.</li>
            <li><strong>Natural Drivers:</strong> Milankovitch cycles, solar variations, and volcanic eruptions occur over timescales or magnitudes that cannot explain the rapid warming seen since 1975.</li>
        </ul>
    </div>

    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 32px; padding-bottom: 4px;">Bilingual Vocabulary Guide (English - Vietnamese)</h2>
    
    <p><strong>Climate change</strong> — Biến đổi khí hậu</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Sự thay đổi dài hạn về nhiệt độ và các kiểu thời tiết điển hình ở một khu vực hoặc trên toàn cầu.</div>

    <p><strong>Weather</strong> — Thời tiết</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Trạng thái khí quyển tại một địa điểm và thời điểm cụ thể (ngắn hạn).</div>

    <p><strong>Climate</strong> — Khí hậu</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Kiểu thời tiết trung bình trong một thời gian dài (thường là 30 năm trở lên).</div>

    <p><strong>Greenhouse effect</strong> — Hiệu ứng nhà kính</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Hiện tượng các khí trong bầu khí quyển giữ lại bức xạ nhiệt từ Trái Đất, làm ấm hành tinh.</div>

    <p><strong>Greenhouse gas</strong> — Khí nhà kính</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Các loại khí như CO₂, CH₄, N₂O có khả năng hấp thụ và phát xạ lại tia hồng ngoại.</div>

    <p><strong>Carbon dioxide (CO₂)</strong> — Khí carbon dioxide (CO₂)</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Khí nhà kính phổ biến nhất do con người tạo ra, chủ yếu từ việc đốt nhiên liệu hóa thạch.</div>

    <p><strong>Methane (CH₄)</strong> — Khí methane (CH₄)</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Khí nhà kính mạnh hơn CO₂ nhiều lần, sinh ra từ chăn nuôi, nông nghiệp và phân hủy rác.</div>

    <p><strong>Fossil fuel</strong> — Nhiên liệu hóa thạch</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Than đá, dầu mỏ và khí đốt tự nhiên được hình thành từ xác sinh vật hàng triệu năm trước.</div>

    <p><strong>Deforestation</strong> — Phá rừng</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Việc chặt phá rừng trên diện rộng, làm mất đi 'lá phổi' hấp thụ CO₂ của Trái Đất.</div>

    <p><strong>Carbon sink</strong> — Bể hấp thụ carbon</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Các hệ sinh thái như rừng, đại dương và đất có khả năng hấp thụ nhiều carbon hơn lượng chúng thải ra.</div>

    <p><strong>Ice core</strong> — Cốt lõi băng (Lõi băng)</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Mẫu băng hình trụ được khoan từ các sông băng sâu, chứa các bọt khí cổ đại dùng để nghiên cứu khí hậu trong quá khứ.</div>

    <p><strong>Evidence</strong> — Chứng cứ (Bằng chứng)</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Dữ liệu khoa học thực tế chứng minh sự nóng lên toàn cầu (ví dụ: mực nước biển dâng, băng tan).</div>

    <p><strong>Global warming</strong> — Nhiệt độ toàn cầu tăng (Sự nóng lên toàn cầu)</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Sự gia tăng nhiệt độ trung bình của bầu khí quyển và đại dương Trái Đất.</div>

    <p><strong>Milankovitch cycles</strong> — Chu kỳ Milankovitch</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Sự thay đổi tự nhiên về quỹ đạo và độ nghiêng của Trái Đất, gây ra các kỷ băng hà trong quá khứ xa xôi.</div>

    <p><strong>Stratosphere</strong> — Tầng bình lưu (Tầng ạp cao)</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Tầng khí quyển nằm phía trên tầng đối lưu, nơi bụi núi lửa có thể lưu lại và che chắn ánh sáng mặt trời.</div>
</div>
"""

# ==========================================
# 5.2 P1
# ==========================================
p5_2_1 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6; font-size: 16px;">
    <h1 style="color:#0891b2; border-bottom:3px solid #67e8f9; padding-bottom: 8px; margin-top: 0;">5.2 Impacts of Climate Change at Multiple Scales</h1>
    
    <p>Climate change is not a future theoretical problem; its impacts are already being felt globally, regionally, and locally across various sectors of human life and natural ecosystems.</p>

    <!-- Impacts Mind Map SVG -->
    <svg viewBox="0 0 420 280" style="max-width:420px;height:auto;display:block;margin:20px auto;background:#fff;">
        <rect width="420" height="280" fill="#f8fafc"/>
        <circle cx="210" cy="140" r="45" fill="#0891b2"/>
        <text x="210" y="140" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ffffff">CLIMATE</text>
        <text x="210" y="152" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ffffff">CHANGE</text>
        
        <!-- Lines -->
        <line x1="210" y1="95" x2="100" y2="50" stroke="#94a3b8" stroke-width="2"/>
        <line x1="210" y1="95" x2="320" y2="50" stroke="#94a3b8" stroke-width="2"/>
        <line x1="165" y1="140" x2="70" y2="140" stroke="#94a3b8" stroke-width="2"/>
        <line x1="255" y1="140" x2="350" y2="140" stroke="#94a3b8" stroke-width="2"/>
        <line x1="210" y1="185" x2="100" y2="230" stroke="#94a3b8" stroke-width="2"/>
        <line x1="210" y1="185" x2="320" y2="230" stroke="#94a3b8" stroke-width="2"/>

        <!-- Nodes -->
        <rect x="50" y="30" width="100" height="40" rx="20" fill="#bae6fd"/>
        <text x="100" y="54" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#0369a1">Sea Level Rise</text>

        <rect x="270" y="30" width="100" height="40" rx="20" fill="#bae6fd"/>
        <text x="320" y="54" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#0369a1">Extreme Weather</text>

        <rect x="10" y="120" width="100" height="40" rx="20" fill="#bae6fd"/>
        <text x="60" y="144" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#0369a1">Ocean Acidification</text>

        <rect x="310" y="120" width="100" height="40" rx="20" fill="#bae6fd"/>
        <text x="360" y="144" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#0369a1">Biodiversity Loss</text>

        <rect x="50" y="210" width="100" height="40" rx="20" fill="#bae6fd"/>
        <text x="100" y="234" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#0369a1">Food Security</text>

        <rect x="270" y="210" width="100" height="40" rx="20" fill="#bae6fd"/>
        <text x="320" y="234" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#0369a1">Human Health</text>
    </svg>

    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 32px; padding-bottom: 4px;">1. Global Impacts</h2>
    
    <div style="background:#ecfeff; border-left:4px solid #22d3ee; padding:14px; border-radius:8px; margin-bottom: 16px;">
        <h3 style="margin-top:0; color:#0891b2;">Temperature & Sea Levels</h3>
        <p>The IPCC AR6 (2021) projects a 1.5°C warming is likely by the 2030s, and potentially 4°C by 2100 under high-emission scenarios. Every additional 0.5°C drastically increases the intensity of extreme events.</p>
        <p><strong>Sea Level Rise (SLR):</strong> Currently rising at 3.7mm/year due to two factors: thermal expansion (warmer water takes up more space) and melting land ice (glaciers and ice sheets). By 2100, sea levels could rise between 0.3m and 1.0m (or up to 2m if ice sheets collapse). This threatens over 1 billion coastal residents across 570 cities globally.</p>
    </div>

    <p><strong>Extreme Weather:</strong> A warmer atmosphere holds more moisture and energy. This leads to more intense hurricanes/cyclones, more frequent and deadly heatwaves (e.g., Russia 2010: 55,000 deaths; Europe 2003: 70,000 deaths), intense flooding, and prolonged droughts in regions like sub-Saharan Africa and the Mediterranean.</p>
    
    <p><strong>Ocean Acidification:</strong> The oceans absorb about 25% of human CO₂ emissions. This forms carbonic acid, lowering the ocean's pH from 8.2 to 8.1 (a 30% increase in acidity since the industrial revolution). This dissolves the calcium carbonate shells of marine life like oysters and corals, leading to mass coral bleaching (e.g., the Great Barrier Reef lost 50% of its coral between 2016-2020).</p>

    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 32px; padding-bottom: 4px;">2. Interactive Regional Impacts</h2>
    <p>Click on the regions below to see how climate change is affecting them specifically.</p>

    <details style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; margin-bottom:8px; padding:10px;">
        <summary style="font-weight:bold; cursor:pointer; color:#0369a1;">Arctic & Greenland</summary>
        <div style="margin-top:10px; font-size:15px;">Warming 4x faster than the global average. Arctic sea ice is losing 13% of its extent per decade. Thawing permafrost is releasing trapped methane, creating a dangerous positive feedback loop. Polar bear habitats are shrinking rapidly, while ice-free shipping routes (like the Northwest Passage) are opening up.</div>
    </details>

    <details style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; margin-bottom:8px; padding:10px;">
        <summary style="font-weight:bold; cursor:pointer; color:#0369a1;">Sub-Saharan Africa</summary>
        <div style="margin-top:10px; font-size:15px;">Facing severe desertification as the Sahara expands southward into the Sahel. Crop failures could reduce yields by 30-40% by 2050. Severe water scarcity (e.g., Lake Chad has shrunk 90% since 1960) could create up to 200 million climate refugees by 2050.</div>
    </details>

    <details style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; margin-bottom:8px; padding:10px;">
        <summary style="font-weight:bold; cursor:pointer; color:#0369a1;">Asia</summary>
        <div style="margin-top:10px; font-size:15px;">Glaciers in the Himalayas (the 'water towers' of Asia) feed rivers like the Ganges and Mekong for 2 billion people. Glacial retreat threatens dry-season river flows and causes dangerous Glacial Lake Outburst Floods (GLOFs). In Bangladesh, a 1m sea level rise would put 20% of the country underwater, displacing 17 million people.</div>
    </details>

    <details style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; margin-bottom:8px; padding:10px;">
        <summary style="font-weight:bold; cursor:pointer; color:#0369a1;">Small Island Developing States (SIDS)</summary>
        <div style="margin-top:10px; font-size:15px;">Islands like the Maldives, Kiribati, and Tuvalu face an existential threat from sea level rise. Impacts include increased storm surges, saltwater intrusion destroying freshwater supplies, and coral bleaching ruining fisheries. Some nations are already buying land elsewhere as a contingency plan.</div>
    </details>

    <details style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; margin-bottom:24px; padding:10px;">
        <summary style="font-weight:bold; cursor:pointer; color:#0369a1;">USA & Europe</summary>
        <div style="margin-top:10px; font-size:15px;">USA: More intense hurricanes (Katrina, Harvey), massive wildfires in California, and severe western droughts (Lake Mead at record lows). Europe: Wildfires in the Mediterranean, water stress in the south, declining Alpine ski industries, and extreme heatwaves.</div>
    </details>

    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 32px; padding-bottom: 4px;">3. Case Studies & Systemic Impacts</h2>
    
    <div style="background:#ecfeff; border-left:4px solid #22d3ee; padding:14px; border-radius:8px; margin-bottom: 16px;">
        <h3 style="margin-top:0; color:#0891b2;">Local Case Studies</h3>
        <ul>
            <li><strong>Maldives:</strong> 99% of land is under 5m altitude. A 1m sea level rise makes 80% of the country uninhabitable. The capital, Male, is surrounded by a sea wall.</li>
            <li><strong>Bangladesh:</strong> Highly vulnerable due to low altitude (60% under 6m). Facing intensifying cyclones, declining crop yields, and massive rural-to-urban climate migration swamping Dhaka. The world's largest mangrove forest (Sundarbans) is being lost to the sea.</li>
            <li><strong>UK:</strong> Experiencing warmer, wetter winters and drier summers. Increased flooding (York, Somerset) and unprecedented extreme heat (40°C recorded for the first time in July 2022). Coastal erosion threatens regions like Norfolk.</li>
        </ul>
    </div>

    <p><strong>Systemic Impacts on Human Society:</strong></p>
    <ul>
        <li><strong>Food Security:</strong> Disrupted rainfall patterns and heat stress are reducing tropical wheat yields, just as the world needs 50% more food by 2050.</li>
        <li><strong>Biodiversity:</strong> 30-40% of species face extinction at 2°C warming. "Phenological mismatch" occurs when natural cycles fall out of sync (e.g., flowers blooming before their pollinating insects emerge).</li>
        <li><strong>Human Health:</strong> Tropical diseases like malaria and dengue are expanding into higher latitudes. Heat stress causes direct mortality. Wildfire smoke degrades air quality.</li>
        <li><strong>Economy:</strong> The IPCC estimates a 10-23% loss in global GDP by 2100 under a 4°C scenario due to infrastructure damage, rising insurance costs, and agricultural collapse.</li>
    </ul>
</div>
"""

p5_2_2 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6; font-size: 16px;">
    <h1 style="color:#0891b2; border-bottom:3px solid #67e8f9; padding-bottom: 8px; margin-top: 0;">5.2 Review & Bilingual Notes</h1>
    
    <p>The impacts of climate change cascade through environmental and human systems. Reviewing the terminology in both English and Vietnamese will help you articulate these complex geographical issues clearly in your exams.</p>

    <div style="background:#ecfeff; border-left:4px solid #22d3ee; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <h3 style="margin-top:0; color:#0891b2;">Key Impact Mechanisms</h3>
        <ul>
            <li><strong>Water & Ice:</strong> Warming oceans expand, and melting land ice raises sea levels, threatening low-lying nations (SIDS) and delta regions (Bangladesh).</li>
            <li><strong>Ecosystems:</strong> CO₂ changes ocean chemistry (acidification), destroying coral reefs. Changing seasons disrupt wildlife lifecycles.</li>
            <li><strong>Human Systems:</strong> Extreme weather (droughts, floods, heatwaves) severely impacts food production, creates climate refugees, and damages economies.</li>
        </ul>
    </div>

    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 32px; padding-bottom: 4px;">Bilingual Vocabulary Guide (English - Vietnamese)</h2>
    
    <p><strong>Sea level rise</strong> — Mực nước biển dâng</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Sự gia tăng mực nước trung bình của các đại dương, do nước biển giãn nở vì nhiệt và băng tan.</div>

    <p><strong>Ocean acidification</strong> — Axit hóa đại dương</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Việc nước biển trở nên axit hơn do hấp thụ CO₂ từ khí quyển, gây hại cho san hô và sinh vật biển có vỏ.</div>

    <p><strong>Saltwater intrusion</strong> — Xâm nhập mặn</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Nước mặn từ biển tràn vào các tầng chứa nước ngọt ven bờ hoặc các con sông, phá hủy nguồn nước sinh hoạt và nông nghiệp.</div>

    <p><strong>Drought</strong> — Hạn hán</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Thời kỳ khô hạn kéo dài bất thường do thiếu mưa, gây ra tình trạng thiếu nước nghiêm trọng.</div>

    <p><strong>Flooding</strong> — Lũ lụt</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Tình trạng ngập nước tràn lan trên những vùng đất thường khô ráo, do mưa lớn cục bộ hoặc bão.</div>

    <p><strong>Heat wave</strong> — Sóng nhiệt</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Giai đoạn nhiệt độ tăng cao bất thường kéo dài trong nhiều ngày, nguy hiểm cho sức khỏe con người.</div>

    <p><strong>Tropical cyclone</strong> — Bão nhiệt đới</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Hệ thống bão mạnh, quay tròn trên các đại dương ấm (còn gọi là cuồng phong - hurricane hoặc bão tố - typhoon).</div>

    <p><strong>Permafrost</strong> — Súng rặn nước (Băng vĩnh cửu)</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Lớp đất đóng băng quanh năm ở vùng cực. Khi tan, nó giải phóng lượng lớn khí methane.</div>

    <p><strong>Desertification</strong> — Sa mạc hóa</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Quá trình đất màu mỡ trở thành sa mạc, thường do hạn hán kéo dài và phá rừng.</div>

    <p><strong>Climate refugee</strong> — Di dân cư khí hậu (Tị nạn khí hậu)</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Người phải rời bỏ nhà cửa do những tác động tàn phá của biến đổi khí hậu (như biển dâng, mất mùa).</div>

    <p><strong>Biodiversity</strong> — Đa dạng sinh học</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Sự đa dạng của các loài động thực vật trong một môi trường sống; hiện đang bị đe dọa nghiêm trọng.</div>

    <p><strong>Coral bleaching</strong> — San hô tẩy trắng</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Hiện tượng san hô trục xuất tảo cộng sinh do nước quá ấm, khiến chúng mất màu và dễ chết.</div>

    <p><strong>Water security</strong> — Bảo hòa nước (An ninh nguồn nước)</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Việc đảm bảo đủ lượng nước sạch cho các nhu cầu sinh hoạt, công nghiệp và nông nghiệp.</div>

    <p><strong>Food production</strong> — Sản xuất lương thực</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Việc canh tác và trồng trọt, hiện đang chịu áp lực lớn do năng suất giảm dưới tác động khí hậu.</div>
</div>
"""

# ==========================================
# 5.3 P1
# ==========================================
p5_3_1 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6; font-size: 16px;">
    <h1 style="color:#0891b2; border-bottom:3px solid #67e8f9; padding-bottom: 8px; margin-top: 0;">5.3 Responses to Climate Change</h1>
    
    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 24px; padding-bottom: 4px;">1. The Golden Rule: Mitigation vs Adaptation</h2>
    <p>Humanity's response to the climate crisis is divided into two distinct but complementary approaches. You must understand the difference:</p>
    <ul>
        <li><strong>Mitigation:</strong> Reducing the <em>causes</em> of climate change. This means reducing greenhouse gas emissions into the atmosphere or enhancing 'carbon sinks' to remove existing gases. It is dealing with the root problem.</li>
        <li><strong>Adaptation:</strong> Adjusting to the <em>effects</em> of climate change that are already happening or are inevitable. It is coping with the consequences to protect people and ecosystems.</li>
    </ul>
    <p>Both are necessary. Without mitigation, the climate will eventually change so drastically that adaptation becomes impossible. But because historical emissions have already 'locked in' some warming, adaptation is required right now.</p>

    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 32px; padding-bottom: 4px;">2. Interactive Mitigation Strategies</h2>
    <p>Click on the strategies below to learn how we are tackling the root cause of global warming.</p>

    <details style="background:#ecfeff; border-left:4px solid #22d3ee; border-radius:6px; margin-bottom:8px; padding:10px;">
        <summary style="font-weight:bold; cursor:pointer; color:#0369a1;">Renewable Energy Transition</summary>
        <div style="margin-top:10px; font-size:15px;">Shifting away from fossil fuels to clean sources. Solar PV panel costs have plummeted 90% since 2010. China now holds 35% of the world's solar capacity. Wind power (onshore and offshore) is scaling massively (e.g., Denmark gets 53% of its electricity from wind). The overarching goal is to "electrify everything and make electricity clean."</div>
    </details>

    <details style="background:#ecfeff; border-left:4px solid #22d3ee; border-radius:6px; margin-bottom:8px; padding:10px;">
        <summary style="font-weight:bold; cursor:pointer; color:#0369a1;">Energy Efficiency</summary>
        <div style="margin-top:10px; font-size:15px;">Using less energy to achieve the same result. This includes better home insulation (triple glazing, cavity walls), switching to LED lighting (75% more efficient), transitioning to Electric Vehicles (EVs now make up 10% of global new car sales), and upgrading to smart grids.</div>
    </details>

    <details style="background:#ecfeff; border-left:4px solid #22d3ee; border-radius:6px; margin-bottom:8px; padding:10px;">
        <summary style="font-weight:bold; cursor:pointer; color:#0369a1;">Carbon Capture and Storage (CCS)</summary>
        <div style="margin-top:10px; font-size:15px;">Technological solutions to capture CO₂ directly at the source (like a power plant exhaust), compress it into a liquid, and store it deep underground in geological formations. Direct Air Capture (DAC) goes further by chemically removing ambient CO₂ directly from the air, though it remains expensive and small-scale.</div>
    </details>

    <details style="background:#ecfeff; border-left:4px solid #22d3ee; border-radius:6px; margin-bottom:8px; padding:10px;">
        <summary style="font-weight:bold; cursor:pointer; color:#0369a1;">Forestry (Reforestation & Afforestation)</summary>
        <div style="margin-top:10px; font-size:15px;">Enhancing natural carbon sinks. Trees naturally absorb CO₂. Global initiatives like the Bonn Challenge aim to restore 350 million hectares of degraded land by 2030. REDD+ schemes financially reward developing nations for protecting their existing forests.</div>
    </details>

    <details style="background:#ecfeff; border-left:4px solid #22d3ee; border-radius:6px; margin-bottom:8px; padding:10px;">
        <summary style="font-weight:bold; cursor:pointer; color:#0369a1;">Reducing Methane Emissions</summary>
        <div style="margin-top:10px; font-size:15px;">Addressing agriculture and waste. This involves shifting diets (eating less beef, which has a huge methane footprint), using precision agriculture to minimize fertiliser waste, and capturing methane off-gassing from landfill sites to burn as energy.</div>
    </details>

    <details style="background:#ecfeff; border-left:4px solid #22d3ee; border-radius:6px; margin-bottom:24px; padding:10px;">
        <summary style="font-weight:bold; cursor:pointer; color:#0369a1;">International Agreements</summary>
        <div style="margin-top:10px; font-size:15px;">Global problems require global governance. The 1997 Kyoto Protocol set binding targets but failed when the USA withdrew. The 2015 Paris Agreement is the current framework: 196 countries pledged "Nationally Determined Contributions" (NDCs) to limit warming to 1.5°C above pre-industrial levels. At COP28 in Dubai (2023), nations agreed for the first time to explicitly "transition away" from fossil fuels.</div>
    </details>

    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 32px; padding-bottom: 4px;">3. Adaptation Strategies by Sector</h2>
    <p>Adapting to the new climate reality requires transforming how we live and build:</p>
    <ul>
        <li><strong>Coastal Protection:</strong> Building hard engineering structures like sea walls, or using 'managed retreat' (moving populations inland). Soft engineering includes beach nourishment and restoring mangrove forests as natural storm buffers. The Netherlands is pioneering floating homes.</li>
        <li><strong>Agriculture:</strong> Utilizing drought-resistant crop varieties developed by research centers. Farmers are shifting cultivation zones northward and employing high-efficiency micro-irrigation to conserve water.</li>
        <li><strong>Water Management:</strong> Building new reservoirs, investing in desalination plants (removing salt from seawater), capturing rainwater, and artificially recharging depleted underground aquifers.</li>
        <li><strong>Infrastructure & Building:</strong> Raising critical infrastructure (roads/railways) above new flood plains. Designing cities to combat the 'urban heat island' effect using cool roofs, urban tree planting, and passive cooling natural ventilation. Implementing early warning systems for extreme weather events.</li>
    </ul>

    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 32px; padding-bottom: 4px;">4. Technology & Individual Action</h2>
    
    <div style="background:#ecfeff; border-left:4px solid #22d3ee; padding:14px; border-radius:8px; margin-bottom: 16px;">
        <h3 style="margin-top:0; color:#0891b2;">Emerging Technologies</h3>
        <p><strong>Carbon Markets:</strong> Systems like the EU Emissions Trading Scheme (ETS) use a 'cap-and-trade' mechanism, putting a financial price on carbon pollution to incentivize companies to reduce emissions.</p>
        <p><strong>Geoengineering:</strong> Highly controversial proposals to hack the climate system. Ideas include Stratospheric Aerosol Injection (spraying reflective particles into the sky to mimic a volcano) or marine cloud brightening. These carry massive risks of unintended global side effects.</p>
        <p><strong>Green Hydrogen:</strong> Using renewable energy to split water into hydrogen fuel via electrolysis. This offers a clean fuel alternative for hard-to-decarbonize sectors like heavy shipping, steel production, and aviation.</p>
    </div>

    <p><strong>Individual Actions (What can you do?):</strong></p>
    <ul>
        <li><strong>Diet:</strong> Reduce meat consumption, especially beef (beef generates ~60kg CO₂e per kg of protein, compared to just 6kg for chicken).</li>
        <li><strong>Transport:</strong> Fly less, switch to an electric vehicle, or use public transport and active travel (cycling).</li>
        <li><strong>Consumer Habits:</strong> Buy less, repair more, and reject fast fashion and planned obsolescence.</li>
        <li><strong>Energy:</strong> Switch your home energy supplier to a 100% renewable tariff and improve home insulation.</li>
        <li><strong>Civic Action:</strong> Vote for politicians and policies that prioritize aggressive climate action.</li>
    </ul>
</div>
"""

p5_3_2 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height: 1.6; font-size: 16px;">
    <h1 style="color:#0891b2; border-bottom:3px solid #67e8f9; padding-bottom: 8px; margin-top: 0;">5.3 Review & Bilingual Notes</h1>
    
    <p>Responding to climate change is the greatest challenge of the 21st century. It requires a combined approach of cutting emissions (mitigation) and preparing for the unavoidable impacts (adaptation). Mastering this terminology is key for discussing solutions.</p>

    <div style="background:#ecfeff; border-left:4px solid #22d3ee; padding:14px; border-radius:8px; margin-bottom: 24px;">
        <h3 style="margin-top:0; color:#0891b2;">Key Solutions Summary</h3>
        <ul>
            <li><strong>Mitigation:</strong> Renewable energy (solar, wind), efficiency (EVs, LEDs), planting trees (carbon sinks), and international treaties (Paris Agreement).</li>
            <li><strong>Adaptation:</strong> Sea walls against floods, drought-resistant crops for agriculture, and early warning systems for storms.</li>
            <li><strong>Technology:</strong> Carbon capture, green hydrogen, and potentially geoengineering are tools for the future.</li>
        </ul>
    </div>

    <h2 style="color:#0891b2; border-bottom:2px solid #67e8f9; margin-top: 32px; padding-bottom: 4px;">Bilingual Vocabulary Guide (English - Vietnamese)</h2>
    
    <p><strong>Mitigation</strong> — Giảm thiểu</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Các nỗ lực nhằm giảm bớt hoặc ngăn chặn việc phát thải khí nhà kính (giải quyết nguyên nhân).</div>

    <p><strong>Adaptation</strong> — Thích ứng</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Sự điều chỉnh tự nhiên hoặc của con người để đối phó với những tác động hiện tại hoặc tương lai của biến đổi khí hậu (giải quyết hậu quả).</div>

    <p><strong>Renewable energy</strong> — Năng lượng tái tạo</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Nguồn năng lượng sạch, tự nhiên không bao giờ cạn kiệt.</div>

    <p><strong>Solar energy</strong> — Năng lượng mặt trời</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Năng lượng thu được từ ánh sáng mặt trời qua các tấm pin quang điện (PV).</div>

    <p><strong>Wind energy</strong> — Năng lượng gió</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Năng lượng thu được từ tua-bin gió trên đất liền hoặc ngoài khơi.</div>

    <p><strong>Energy efficiency</strong> — Hiệu suất năng lượng</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Sử dụng công nghệ (như đèn LED, xe điện) để thực hiện cùng một công việc nhưng tốn ít năng lượng hơn.</div>

    <p><strong>Carbon Capture and Storage (CCS)</strong> — Thu giữ và lưu trữ carbon (CCS)</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Công nghệ thu khí CO₂ từ các nhà máy và bơm sâu xuống lòng đất để cách ly khỏi khí quyển.</div>

    <p><strong>Reforestation</strong> — Trồng rừng (Tái trồng rừng)</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Việc trồng lại rừng ở những nơi đã bị chặt phá để tăng cường khả năng hấp thụ carbon của Trái Đất.</div>

    <p><strong>Paris Agreement</strong> — Hiệp định Paris</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Hiệp ước quốc tế (2015) mang tính lịch sử, cam kết giới hạn sự nóng lên toàn cầu ở mức 1.5°C.</div>

    <p><strong>Emissions</strong> — Khí thải</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Lượng khí nhà kính xả vào bầu khí quyển từ các hoạt động của con người.</div>

    <p><strong>Sea wall</strong> — Tường biển (Đê biển)</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Công trình phòng thủ kiên cố ven bờ để ngăn chặn nước biển dâng và sóng bão.</div>

    <p><strong>Managed retreat</strong> — Rút lui có quản lý</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Chiến lược thích ứng chủ động di dời các cộng đồng ven biển vào đất liền khi khu vực đó không thể bảo vệ được nữa.</div>

    <p><strong>Drought-resistant crops</strong> — Giống cây chịu hạn</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Các loại cây trồng biến đổi gen hoặc lai tạo để có thể sinh trưởng tốt ngay cả khi thiếu nước trầm trọng.</div>

    <p><strong>Carbon market</strong> — Thị trường carbon</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Hệ thống mua bán quyền phát thải, tạo động lực tài chính cho các công ty giảm lượng khí thải của họ.</div>

    <p><strong>Geoengineering</strong> — Địa kỹ thuật</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Sự can thiệp có chủ ý và quy mô lớn vào hệ thống khí hậu Trái Đất để chống lại hiện tượng nóng lên toàn cầu (còn nhiều rủi ro).</div>

    <p><strong>Green hydrogen</strong> — Hydro xanh</p>
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Nhiên liệu khí hydro được sản xuất bằng năng lượng tái tạo, không tạo ra khí thải carbon khi đốt cháy.</div>
</div>
"""

pages = [
    ("8c30875a-3c75-4707-8653-2c39c4059c3e", p5_1_1),
    ("9dc048ea-33eb-4ee1-9d0f-0de825f6dfb9", p5_1_2),
    ("81b16ff1-0bb6-46a4-b8b1-ea16b69e29b5", p5_2_1),
    ("ca6e2803-6b90-4d44-8d64-4ff5ec33ccd6", p5_2_2),
    ("1c838513-574b-4f76-8de2-e2a28db5078d", p5_3_1),
    ("13f580c7-6961-43fe-a0e6-0592bccf4d4e", p5_3_2),
]

SUPABASE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"

success_count = 0

for page_id, html_content in pages:
    safe_html = encode_html(html_content)
    url = f"{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.{page_id}"
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    data = json.dumps({"content_html": safe_html}).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers=headers, method="PATCH")
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 204:
                print(f"Success updating page {page_id}")
                success_count += 1
            else:
                print(f"Failed updating page {page_id} - status {response.status}")
    except urllib.error.URLError as e:
        print(f"Error updating page {page_id}: {e}")

print(f"Done. Successfully updated {success_count}/6 pages.")
