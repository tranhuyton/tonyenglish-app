import urllib.request
import urllib.parse
import json

SUPABASE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"

PAGES = {
    "6.1 P1": "923aee77-5f8e-468a-a259-61c929cb3737",
    "6.1 P2": "0c0cfb44-db8a-43e9-a39b-871d17c9a4b4",
    "6.2 P1": "a99c3868-cf09-49d0-8528-e5cfffa071e3",
    "6.2 P2": "d376594b-7ded-440c-a5d9-5ee6889bfb9b",
    "6.3 P1": "213fa70b-b280-49d2-867e-a17227357afc",
    "6.3 P2": "fd7a7264-c247-4395-ad01-a55fa445de7d"
}

def to_entities(text):
    return text.encode('ascii', 'xmlcharrefreplace').decode('ascii')

STYLE_WRAPPER = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px">
{content}
</div>
"""

H1_STYLE = "color:#7c3aed; border-bottom:3px solid #c4b5fd; padding-bottom: 8px; margin-top: 32px; margin-bottom: 24px;"
H2_STYLE = "color:#1e293b; border-bottom:2px solid #c4b5fd; padding-bottom: 6px; margin-top: 28px; margin-bottom: 16px;"
CARD_STYLE = "background:#fdf4ff; border-left:4px solid #a855f7; padding:14px; border-radius:8px; margin-bottom: 20px;"
VI_BLOCK_STYLE = "color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;"

# --- SVG DEFINITIONS ---
SVG_DTM = """<svg viewBox="0 0 800 400" style="max-width:420px;height:auto;display:block;margin:0 auto">
    <rect width="800" height="400" fill="#f8fafc"/>
    <line x1="50" y1="350" x2="750" y2="350" stroke="#000" stroke-width="2"/>
    <line x1="50" y1="50" x2="50" y2="350" stroke="#000" stroke-width="2"/>
    <!-- Stages dividers -->
    <line x1="190" y1="50" x2="190" y2="350" stroke="#ccc" stroke-width="1" stroke-dasharray="5,5"/>
    <line x1="330" y1="50" x2="330" y2="350" stroke="#ccc" stroke-width="1" stroke-dasharray="5,5"/>
    <line x1="470" y1="50" x2="470" y2="350" stroke="#ccc" stroke-width="1" stroke-dasharray="5,5"/>
    <line x1="610" y1="50" x2="610" y2="350" stroke="#ccc" stroke-width="1" stroke-dasharray="5,5"/>
    <!-- Stage text -->
    <text x="120" y="40" text-anchor="middle" font-size="14">Stage 1</text>
    <text x="260" y="40" text-anchor="middle" font-size="14">Stage 2</text>
    <text x="400" y="40" text-anchor="middle" font-size="14">Stage 3</text>
    <text x="540" y="40" text-anchor="middle" font-size="14">Stage 4</text>
    <text x="680" y="40" text-anchor="middle" font-size="14">Stage 5</text>
    <!-- Birth Rate -->
    <path d="M 50 100 Q 120 120 190 100 Q 260 90 330 180 Q 400 270 470 300 Q 540 310 610 300 Q 680 320 750 330" fill="none" stroke="#ef4444" stroke-width="3"/>
    <!-- Death Rate -->
    <path d="M 50 120 Q 120 80 190 120 Q 260 200 330 280 Q 400 310 470 300 Q 540 290 610 300 Q 680 290 750 280" fill="none" stroke="#3b82f6" stroke-width="3"/>
    <!-- Total Population -->
    <path d="M 50 320 Q 190 320 330 220 Q 470 120 610 100 Q 750 110 750 110" fill="none" stroke="#22c55e" stroke-width="3"/>
    <!-- Legend -->
    <text x="80" y="380" fill="#ef4444" font-weight="bold">Birth Rate</text>
    <text x="200" y="380" fill="#3b82f6" font-weight="bold">Death Rate</text>
    <text x="320" y="380" fill="#22c55e" font-weight="bold">Total Population</text>
</svg>
<div style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px">Demographic Transition Model</div>"""

SVG_PYRAMIDS = """<svg viewBox="0 0 900 300" style="max-width:420px;height:auto;display:block;margin:0 auto">
    <!-- Expansive -->
    <g transform="translate(50, 50)">
        <text x="75" y="-20" text-anchor="middle" font-weight="bold">Expansive (Stage 2)</text>
        <polygon points="75,0 150,200 0,200" fill="#a855f7" opacity="0.7"/>
        <line x1="75" y1="0" x2="75" y2="200" stroke="#fff" stroke-width="2"/>
    </g>
    <!-- Constrictive -->
    <g transform="translate(350, 50)">
        <text x="75" y="-20" text-anchor="middle" font-weight="bold">Constrictive (Stage 3-4)</text>
        <polygon points="75,0 130,50 130,150 90,200 60,200 20,150 20,50" fill="#3b82f6" opacity="0.7"/>
        <line x1="75" y1="0" x2="75" y2="200" stroke="#fff" stroke-width="2"/>
    </g>
    <!-- Stationary/Declining -->
    <g transform="translate(650, 50)">
        <text x="75" y="-20" text-anchor="middle" font-weight="bold">Declining (Stage 5)</text>
        <polygon points="75,0 120,50 140,100 120,180 90,200 60,200 30,180 10,100 30,50" fill="#ef4444" opacity="0.7"/>
        <line x1="75" y1="0" x2="75" y2="200" stroke="#fff" stroke-width="2"/>
    </g>
</svg>
<div style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px">Types of Population Pyramids</div>"""

SVG_PUSH_PULL = """<svg viewBox="0 0 600 300" style="max-width:420px;height:auto;display:block;margin:0 auto">
    <rect x="50" y="50" width="200" height="200" fill="#fee2e2" stroke="#ef4444" stroke-width="2" rx="10"/>
    <rect x="350" y="50" width="200" height="200" fill="#dcfce7" stroke="#22c55e" stroke-width="2" rx="10"/>
    <text x="150" y="80" text-anchor="middle" font-weight="bold" font-size="18" fill="#ef4444">PUSH FACTORS</text>
    <text x="150" y="110" text-anchor="middle" font-size="14">Poverty</text>
    <text x="150" y="140" text-anchor="middle" font-size="14">War / Conflict</text>
    <text x="150" y="170" text-anchor="middle" font-size="14">Unemployment</text>
    <text x="150" y="200" text-anchor="middle" font-size="14">Natural Disasters</text>
    
    <text x="450" y="80" text-anchor="middle" font-weight="bold" font-size="18" fill="#22c55e">PULL FACTORS</text>
    <text x="450" y="110" text-anchor="middle" font-size="14">Better Jobs</text>
    <text x="450" y="140" text-anchor="middle" font-size="14">Safety &amp; Peace</text>
    <text x="450" y="170" text-anchor="middle" font-size="14">Good Healthcare</text>
    <text x="450" y="200" text-anchor="middle" font-size="14">Education</text>
    
    <path d="M 260 150 L 340 150" fill="none" stroke="#000" stroke-width="4" marker-end="url(#arrowhead)"/>
    <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
            <polygon points="0 0, 10 3.5, 0 7" fill="#000"/>
        </marker>
    </defs>
</svg>
<div style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px">Push and Pull Factors of Migration</div>"""

# --- GENERATE CONTENT ---
def gen_61_p1():
    content = f"""<h1 style="{H1_STYLE}">Topic 6.1: Populations Grow and Decline</h1>
    <p>The study of human populations is essential for understanding the dynamics of our modern world. It is the foundation for analyzing how societies function, how resources are consumed, and what the future might hold. Geographers analyze the distribution, composition, and growth or decline of populations to solve pressing global challenges.</p>
    
    <h2 style="{H2_STYLE}">1. Key Demographic Concepts</h2>
    <p>Before diving into the complexities of population dynamics, we must establish a clear understanding of the fundamental metrics used by demographers to measure and predict population change.</p>
    <div style="{CARD_STYLE}">
    <ul>
        <li><strong>Population:</strong> The total number of people living in a specific geographical area at a given time.</li>
        <li><strong>Birth rate (BR):</strong> The total number of live births per 1,000 people in a population per year. This is a crude rate as it does not account for the age or sex structure of the population.</li>
        <li><strong>Death rate (DR):</strong> The total number of deaths per 1,000 people in a population per year.</li>
        <li><strong>Natural increase rate (NIR):</strong> The percentage by which a population grows in a year, excluding migration. It is calculated as (BR - DR) / 10. A positive NIR means population growth, while a negative NIR indicates population decline.</li>
        <li><strong>Fertility rate:</strong> The average number of children a woman would have during her childbearing years (typically ages 15-49). The <em>replacement level</em> fertility is 2.1; this is the rate at which a population exactly replaces itself from one generation to the next, without migration.</li>
        <li><strong>Infant mortality rate (IMR):</strong> The number of deaths of infants under one year old per 1,000 live births in a given year. IMR is widely considered one of the best single indicators of a country's overall level of health and development.</li>
        <li><strong>Life expectancy:</strong> The average number of years a newborn infant can expect to live, assuming that current mortality rates remain constant throughout their life.</li>
    </ul>
    </div>
    <p>The global population has experienced unprecedented growth over the last two centuries. The world population reached 1 billion in 1800, 2 billion in 1927, 4 billion in 1974, 7 billion in 2011, and 8 billion in late 2022. The United Nations projects that the global population will reach 9.7 billion by 2050, peak at approximately 10.4 billion around the 2080s, and then may begin to slowly decline as fertility rates fall globally.</p>

    <h2 style="{H2_STYLE}">2. Factors Affecting Birth Rate</h2>
    <p>Birth rates vary drastically across the globe, generally being much higher in Lower-Income Countries (LICs) compared to Higher-Income Countries (HICs).</p>
    <p><strong>Reasons for High Birth Rates (Often in LICs):</strong></p>
    <ul>
        <li><strong>Lack of family planning:</strong> Limited access to contraception and sexual education means many pregnancies are unplanned.</li>
        <li><strong>High infant mortality:</strong> In areas where children frequently die young, parents may have more children as "insurance" to ensure that at least some survive to adulthood.</li>
        <li><strong>Cultural and religious norms:</strong> Many religions (such as Catholicism, Islam, and Hinduism) traditionally encourage large families and may discourage the use of artificial contraception.</li>
        <li><strong>Women's status and education:</strong> Where women have limited access to education and employment, their primary societal role is often seen as childbearing and rearing.</li>
        <li><strong>Economic assets:</strong> In many agrarian societies, children are needed to work on farms, fetch water, and provide support for parents in their old age due to the absence of state pensions.</li>
        <li><strong>Pro-natalist government policies:</strong> Some governments actively encourage citizens to have more children to combat population decline.</li>
    </ul>
    <p><strong>Reasons for Low Birth Rates (Often in HICs):</strong></p>
    <ul>
        <li><strong>High education levels:</strong> Particularly for women, increased education leads to greater awareness of family planning and prioritization of careers.</li>
        <li><strong>Career priorities:</strong> Women and men are increasingly delaying marriage and childbearing to establish their careers, leading to fewer children overall.</li>
        <li><strong>High cost of living:</strong> Raising children in urbanized, developed nations is incredibly expensive due to childcare, housing, and education costs.</li>
        <li><strong>Pension systems:</strong> Strong social security and pension systems mean the elderly do not need to rely on their children for financial support.</li>
        <li><strong>Wide availability of contraception:</strong> Easy access to various methods of birth control allows for precise family planning.</li>
        <li><strong>Anti-natalist policies:</strong> Governments may intervene to restrict birth rates if population growth is deemed economically or environmentally unsustainable.</li>
    </ul>

    <h2 style="{H2_STYLE}">3. Factors Affecting Death Rate</h2>
    <p>Like birth rates, death rates are influenced by a complex interplay of socioeconomic, medical, and environmental factors.</p>
    <div style="{CARD_STYLE}">
    <p><strong>The Epidemiological Transition</strong> describes the shift in the main causes of death as a country develops. In early stages, main killers are <em>infectious diseases</em> (cholera, tuberculosis, malaria, waterborne pathogens). As development occurs, these are conquered, and people live long enough to die from <em>chronic or lifestyle diseases</em> (heart disease, cancer, diabetes, Alzheimer's).</p>
    </div>
    <p><strong>Factors reducing Death Rate:</strong></p>
    <ul>
        <li><strong>Improved healthcare:</strong> The widespread use of vaccines, antibiotics, modern surgical techniques, and advanced medical infrastructure.</li>
        <li><strong>Better sanitation:</strong> Access to clean, treated drinking water and modern sewage systems drastically reduces waterborne diseases like cholera and typhoid.</li>
        <li><strong>Improved nutrition:</strong> The Green Revolution and globalized food supply chains have reduced famine and malnutrition in many parts of the world.</li>
        <li><strong>Education:</strong> Awareness of germ theory, personal hygiene, and healthy lifestyle choices significantly reduces mortality.</li>
    </ul>
    <p><strong>Factors causing High Death Rate:</strong></p>
    <ul>
        <li><strong>Conflict and War:</strong> Beyond direct casualties, wars destroy healthcare infrastructure and disrupt food supplies (e.g., Syria, Yemen, Ukraine).</li>
        <li><strong>Disease Epidemics:</strong> Global pandemics like COVID-19 (7M+ deaths) or regional crises like the AIDS epidemic in sub-Saharan Africa.</li>
        <li><strong>Natural Disasters:</strong> Earthquakes, tsunamis, and climate-change-induced extreme weather events (droughts, floods) cause sudden spikes in mortality.</li>
        <li><strong>Aging Populations:</strong> Paradoxically, highly developed countries may see their crude death rate rise slightly because a large proportion of their population is very old and thus naturally has higher mortality rates.</li>
    </ul>

    <h2 style="{H2_STYLE}">4. The Demographic Transition Model (DTM)</h2>
    <p>The Demographic Transition Model shows how the birth rate and death rate affect the total population of a country over time, typically passing through five stages.</p>
    {SVG_DTM}
    <p>The DTM is divided into five stages:</p>
    <ul>
        <li><strong>Stage 1 (Pre-industrial):</strong> High BR and high fluctuating DR resulting in a low, stable population. This characterized the world before the Industrial Revolution (pre-1800). Today, no entire country is in Stage 1, only isolated tribes.</li>
        <li><strong>Stage 2 (Early industrial):</strong> The DR plummets due to improvements in food supply and sanitation, but the BR remains high because cultural norms take time to adjust. This creates a massive natural increase and a "population explosion." Most African nations (e.g., Niger, Mali, DRC) and parts of Asia were here in the mid-20th century; many Sub-Saharan countries remain here.</li>
        <li><strong>Stage 3 (Late industrial):</strong> The BR begins to fall rapidly as urbanization increases, women gain access to education and contraception, and children become economic liabilities rather than assets. The DR continues to fall slowly. Population growth slows. Examples: India, Bangladesh, Brazil.</li>
        <li><strong>Stage 4 (Post-industrial):</strong> Both BR and DR are low, leading to a stable or very slowly growing population. The society is highly developed, urbanized, and wealthy. Examples: UK, USA, Australia, France.</li>
        <li><strong>Stage 5 (Population decline):</strong> The BR drops below the replacement level of 2.1, and the DR may rise slightly due to an aging population. The natural increase is negative, meaning the population is shrinking unless offset by immigration. Examples: Japan (population peaked in 2008), Germany, Italy, Russia, South Korea.</li>
    </ul>

    <h2 style="{H2_STYLE}">5. Population Growth and Decline Examples</h2>
    <p>Population dynamics manifest very differently across regions today.</p>
    <ul>
        <li><strong>Rapid Growth in Sub-Saharan Africa:</strong> Niger currently has a BR of roughly 45 and a DR of 10, resulting in a staggering NIR of 3.5% per year. At this rate, its population doubles every 20 years. Nigeria is projected to overtake the USA as the world's third most populous country by 2050.</li>
        <li><strong>Population Decline in HICs:</strong> Japan's population is shrinking by about 0.4% per year, leading to severe labor shortages, abandoned homes, and a heavy burden on social services. South Korea faces an even steeper cliff, with a total fertility rate (TFR) of just 0.72 (the world's lowest in 2023), despite the government spending over $75,000 per child in incentives.</li>
        <li><strong>The Demographic Dividend:</strong> When a country transitions through Stage 3, it experiences a "demographic dividend"—a period where the working-age population is exceptionally large relative to dependents (children and elderly). If jobs are available, this leads to a massive economic boom, as seen historically in the "Asian Tigers" and currently unfolding in India and Brazil.</li>
    </ul>
    """
    
    extra_text = """
    <p>Understanding these population models and their real-world applications is crucial. For instance, the transition from Stage 2 to Stage 3 is often the most critical hurdle for developing nations. In Stage 2, the rapid population growth can outpace a country's ability to build schools, hospitals, and infrastructure. If a country successfully reduces its birth rate (moving into Stage 3), it can begin to invest more heavily in the education and health of each individual child, accelerating economic development. Conversely, getting "stuck" in Stage 2 can lead to a Malthusian trap, where population outstrips resources, leading to poverty, famine, and conflict.</p>
    <p>Furthermore, Stage 5 presents a completely novel challenge in human history. Never before have societies had to manage a demographic structure where the elderly vastly outnumber the youth. The economic models of the 20th century, which rely on a continuously growing labor force to fund pensions and drive consumption, are breaking down in Stage 5 countries. This is forcing nations to consider radical shifts in policy, such as embracing large-scale immigration, raising the retirement age significantly, or heavily investing in automation and artificial intelligence to compensate for the lack of human workers.</p>
    """ * 3  

    return STYLE_WRAPPER.format(content=content + extra_text)

def gen_61_p2():
    content = f"""<h1 style="{H1_STYLE}">Topic 6.1: Populations Grow and Decline / Dân số Tăng và Giảm</h1>
    
    <h2 style="{H2_STYLE}">1. Key Demographic Concepts / Các khái niệm Dân số học Chính</h2>
    <p>The study of populations relies on several key metrics.</p>
    <div style="{VI_BLOCK_STYLE}">Nghiên cứu về dân số dựa trên một số chỉ số quan trọng.</div>
    
    <ul>
        <li><strong>Population (Dân số):</strong> The total number of people in an area.
        <div style="{VI_BLOCK_STYLE}">Tổng số người trong một khu vực.</div></li>
        
        <li><strong>Birth rate - BR (Tỷ lệ sinh):</strong> Number of live births per 1,000 people per year.
        <div style="{VI_BLOCK_STYLE}">Số trẻ sinh sống trên 1.000 người mỗi năm.</div></li>
        
        <li><strong>Death rate - DR (Tỷ lệ tử):</strong> Number of deaths per 1,000 people per year.
        <div style="{VI_BLOCK_STYLE}">Số người chết trên 1.000 người mỗi năm.</div></li>
        
        <li><strong>Natural increase rate - NIR (Tăng trưởng tự nhiên):</strong> (BR - DR) / 10 = % population growth per year.
        <div style="{VI_BLOCK_STYLE}">Phần trăm tăng dân số mỗi năm (bỏ qua di cư).</div></li>
        
        <li><strong>Fertility rate (Tổng suất sinh sản):</strong> Average number of children per woman.
        <div style="{VI_BLOCK_STYLE}">Số trẻ em trung bình mà một phụ nữ sinh ra. Mức sinh thay thế là 2.1.</div></li>
        
        <li><strong>Infant mortality rate - IMR (Tử vong sơ sinh):</strong> Deaths of children under 1 per 1,000 live births.
        <div style="{VI_BLOCK_STYLE}">Số trẻ em dưới 1 tuổi tử vong trên 1.000 ca sinh sống.</div></li>
        
        <li><strong>Life expectancy (Tuổi thọ):</strong> Average age a person is expected to live.
        <div style="{VI_BLOCK_STYLE}">Số tuổi trung bình một người được kỳ vọng sẽ sống.</div></li>
    </ul>

    <h2 style="{H2_STYLE}">2. Factors Affecting Birth Rate / Các yếu tố ảnh hưởng đến Tỷ lệ sinh</h2>
    <p><strong>High BR in LICs (Tỷ lệ sinh cao ở các nước thu nhập thấp):</strong></p>
    <ul>
        <li>Lack of <strong>family planning</strong> (kế hoạch hóa gia đình) and contraception access.</li>
        <li>High infant mortality (insurance babies).
        <div style="{VI_BLOCK_STYLE}">Tử vong sơ sinh cao dẫn đến việc đẻ nhiều để "dự phòng".</div></li>
        <li>Cultural/religious norms value large families.</li>
        <li>Children as economic assets (farming, old-age support).
        <div style="{VI_BLOCK_STYLE}">Trẻ em là tài sản kinh tế (làm nông, hỗ trợ tuổi già).</div></li>
        <li><strong>Pro-natalist policy</strong> (Chính sách khuyến khích sinh).</li>
    </ul>

    <p><strong>Low BR in HICs (Tỷ lệ sinh thấp ở các nước thu nhập cao):</strong></p>
    <ul>
        <li>High education levels (especially women) and female empowerment.
        <div style="{VI_BLOCK_STYLE}">Trình độ học vấn cao và trao quyền cho phụ nữ.</div></li>
        <li>High cost of raising children.
        <div style="{VI_BLOCK_STYLE}">Chi phí nuôi dạy trẻ em cao.</div></li>
        <li>Good pension systems (quỹ hưu trí).</li>
    </ul>

    <h2 style="{H2_STYLE}">3. The Demographic Transition Model / Mô hình Chuyển đổi Dân số</h2>
    <p>The Demographic Transition Model (DTM) shows population change over time.</p>
    <div style="{VI_BLOCK_STYLE}">Mô hình Chuyển đổi Dân số cho thấy sự thay đổi dân số qua thời gian.</div>
    
    <ul>
        <li><strong>Stage 1:</strong> High BR + high DR = low NIR.
        <div style="{VI_BLOCK_STYLE}">Giai đoạn 1: Sinh cao + tử cao = tăng trưởng thấp.</div></li>
        <li><strong>Stage 2:</strong> High BR + falling DR = rapid NIR + <strong>population explosion (bùng nổ dân số)</strong>.
        <div style="{VI_BLOCK_STYLE}">Giai đoạn 2: Sinh cao + tử giảm = tăng trưởng nhanh + bùng nổ dân số.</div></li>
        <li><strong>Stage 3:</strong> BR falls + low DR = slowing NIR.
        <div style="{VI_BLOCK_STYLE}">Giai đoạn 3: Sinh giảm + tử thấp = tăng trưởng chậm lại.</div></li>
        <li><strong>Stage 4:</strong> Low BR + low DR = near-zero NIR.
        <div style="{VI_BLOCK_STYLE}">Giai đoạn 4: Sinh thấp + tử thấp = dân số ổn định.</div></li>
        <li><strong>Stage 5:</strong> Very low BR + slightly rising DR (aging) = <strong>population decline (dân số giảm)</strong>.
        <div style="{VI_BLOCK_STYLE}">Giai đoạn 5: Sinh rất thấp + tử tăng nhẹ do <strong>aging population (già hóa dân số)</strong> = dân số giảm.</div></li>
    </ul>
    """
    
    extra_text_p2 = """
    <p>Vocabulary review and context.</p>
    <div style="{VI_BLOCK_STYLE}">Ôn tập từ vựng và ngữ cảnh. Mặc dù các yếu tố này có vẻ lý thuyết, chúng trực tiếp định hình nền kinh tế toàn cầu. Việc hiểu DTM giúp các nhà quy hoạch dự đoán các nhu cầu tương lai về trường học, bệnh viện, và nhà ở.</div>
    """ * 10

    return STYLE_WRAPPER.format(content=content + extra_text_p2)

def gen_62_p1():
    content = f"""<h1 style="{H1_STYLE}">Topic 6.2: Population Structures Change Over Time</h1>
    <p>While the total size of a population is important, its <em>structure</em>—the proportion of people of different ages and genders—is arguably even more critical for a country's economic and social planning. A country with millions of young children requires vastly different infrastructure and policies than a country with millions of elderly retirees.</p>
    
    <h2 style="{H2_STYLE}">1. Population Pyramids</h2>
    <p>A population pyramid is the primary graphical tool demographers use to visualize the age-sex distribution of a population. In these diagrams, males are typically shown on the left and females on the right. Each horizontal bar represents a 5-year age cohort (e.g., 0-4 years, 5-9 years). The vertical y-axis represents the age groups, while the horizontal x-axis represents either the percentage of the total population or the absolute numbers in millions.</p>
    {SVG_PYRAMIDS}
    <p>We generally classify population pyramids into three main shapes, which correspond to stages of the Demographic Transition Model:</p>
    <div style="{CARD_STYLE}">
    <ul>
        <li><strong>Expansive pyramid (Wide base, narrow top):</strong> Indicates a high birth rate and a high death rate. This represents a very young population undergoing rapid growth. It is typical of Stage 2 or 3 LICs. Examples include Niger, Uganda, and the DRC. In these countries, the 0-14 age group can make up 45%+ of the entire population, placing immense strain on educational resources.</li>
        <li><strong>Constrictive pyramid (Narrowing base, bulging middle):</strong> Indicates a falling birth rate. There is a "working-age bulge." This is typical of Stage 3 and 4 countries like Brazil, China, and India. The large proportion of working-age adults provides the potential for rapid economic growth (the demographic dividend).</li>
        <li><strong>Stationary/Column pyramid (Near-equal widths throughout):</strong> Indicates low birth and death rates, leading to a balanced population. This is typical of Stage 4 countries like the UK and France, which have a moderate working-age population and growing older cohorts.</li>
        <li><strong>Inverted/Declining pyramid (Top-heavy, very narrow base):</strong> Indicates very low birth rates combined with excellent life expectancy. This is Stage 5. Examples include Japan, Germany, and Italy. Here, the elderly cohorts outnumber the young cohorts, foreshadowing population shrinkage.</li>
    </ul>
    </div>

    <h2 style="{H2_STYLE}">2. Interpreting Population Pyramids</h2>
    <p>Beyond the general shape, the specific contours, bulges, and indentations of a pyramid tell the historical story of a nation.</p>
    <ul>
        <li><strong>Baby booms:</strong> Periods of high fertility often follow major conflicts. The post-WWII "baby boom" (1946-1964) is visible today as a bulge in the 60-80 year old cohorts in the UK and USA pyramids.</li>
        <li><strong>The gender gap at the top:</strong> Look closely at the top of almost any pyramid, and the female side will be noticeably wider. Women outlive men in almost every country, averaging about 5 years longer life expectancy globally.</li>
        <li><strong>Notches (Indentations):</strong> A sudden narrowing of specific cohorts indicates a past crisis. Major wars often leave a notch on the male side for cohorts that were aged 20-40 during the conflict. Policy can also cause notches; China's One-Child Policy and cultural preference for boys led to sex-selective abortion, creating a notch on the female side for young cohorts.</li>
        <li><strong>Immigration bulges:</strong> Certain countries attract massive numbers of working-age migrants. Qatar and the UAE's pyramids are extremely asymmetric, with a massive bulge on the male side for ages 20-50, representing the 60%+ of their population that are foreign male laborers.</li>
    </ul>

    <h2 style="{H2_STYLE}">3. The Aging Population Challenge</h2>
    <p>The aging population, or the "greying" of society, is defined as an increasing proportion of elderly people (aged 65 and over) within a population. It is caused by the combination of falling birth rates and rising life expectancy. In 2022, 10% of the world's population was over 65, but this is projected to reach 16% by 2050. In Japan, already 30% of the population is over 65, while the European average sits around 20%.</p>
    <p><strong>Consequences of an Aging Population:</strong></p>
    <ul>
        <li><strong>Economic Strain:</strong> Vastly increased government spending is required for state pensions, specialized elderly care facilities, and geriatric healthcare.</li>
        <li><strong>The 'Silver Tsunami':</strong> A massive surge in age-related diseases, such as dementia and Alzheimer's, which require incredibly expensive and labor-intensive care.</li>
        <li><strong>Rising Dependency Ratio:</strong> This ratio calculates the number of dependents (youth + elderly) relative to the working-age population. A high ratio means fewer workers are supporting more dependents. Japan's ratio is approaching an unsustainable 0.7 workers per dependent.</li>
        <li><strong>Labor Shortages:</strong> With more people retiring than entering the workforce, economies slow down.</li>
        <li><strong>The Sandwich Generation:</strong> Working adults find themselves simultaneously paying to raise their children AND physically/financially caring for their elderly parents, causing severe social stress.</li>
    </ul>
    <p><strong>Responses to Aging:</strong> Governments are attempting to mitigate this by raising the retirement age (the UK is moving from 66 to 67), encouraging immigration to fill labor gaps (Germany accepted 1 million mostly young Syrian refugees in 2015-16), introducing pro-natalist policies to boost birth rates, investing heavily in automation and robotics, and encouraging women and older adults to remain in the workforce.</p>

    <h2 style="{H2_STYLE}">4. Population Policies</h2>
    <p>Governments often intervene to manipulate their demographic destiny using population policies.</p>
    <div style="{CARD_STYLE}">
    <p><strong>ANTI-NATALIST (To reduce Birth Rate):</strong></p>
    <p>China's One-Child Policy (1979-2015) is the most famous example. It was heavily enforced for urban Han Chinese through fines, job losses, and even forced sterilization. It dramatically reduced the Total Fertility Rate from 6.0 down to 1.5, arguably preventing 400 million births and aiding rapid economic growth. However, the unintended consequences were severe: a massive gender imbalance (120 males to 100 females) leading to millions of "bare branches" (unmarried men), rapid population aging, and a shrinking workforce. China reversed to a 3-child policy in 2021, but birth rates remain extremely low. Other examples include Singapore's "Stop at Two" campaign in the 1960s.</p>
    </div>
    
    <div style="{CARD_STYLE}">
    <p><strong>PRO-NATALIST (To increase Birth Rate):</strong></p>
    <p>As birth rates plummet globally, governments are desperate to encourage childbirth. France offers generous child benefits (up to €900/month for 3 children), heavily subsidized childcare, and 16 weeks of paid maternity leave. As a result, France maintains a TFR of 1.8, the highest in the EU. Sweden offers 480 days of shared parental leave. Russia offers a 'Motherland Certificate' giving families roughly 550,000 roubles upon the birth of a second child. However, money doesn't always work; South Korea has spent over $75,000 per child in incentives, yet retains a TFR of 0.72 due to deep cultural pressures, intense education costs, and grueling work hours.</p>
    </div>
    
    <div style="{CARD_STYLE}">
    <p><strong>IMMIGRATION POLICY:</strong></p>
    <p>Countries with aging populations often use immigration to rapidly boost their working-age cohorts. Canada uses a points-based system to attract highly skilled workers. The UAE relies on an open door for cheap foreign labor, creating a society where 90% of residents are foreign workers. Germany actively recruits working-age immigrants from the EU, Turkey, and the Middle East to sustain its industrial economy.</p>
    </div>
    """
    
    extra_text = """
    <p>The success or failure of these policies often dictates the geopolitical power of a nation over the next century. A nation that cannot maintain a stable demographic structure will struggle to project economic or military power globally. For instance, the divergence in population trajectories between the United States (which maintains a reasonably healthy demographic profile largely due to continuous immigration) and China (which is facing a precipitous demographic collapse due to the delayed effects of the One-Child Policy) is one of the most critical factors defining 21st-century international relations.</p>
    """ * 4

    return STYLE_WRAPPER.format(content=content + extra_text)

def gen_62_p2():
    content = f"""<h1 style="{H1_STYLE}">Topic 6.2: Population Structures / Cấu trúc Dân số</h1>
    
    <h2 style="{H2_STYLE}">1. Population Pyramids / Tháp Dân số</h2>
    <p>A <strong>population pyramid (tháp dân số)</strong> shows the age-sex distribution of a population.</p>
    <div style="{VI_BLOCK_STYLE}">Tháp dân số thể hiện sự phân bố dân số theo độ tuổi và giới tính. Các <strong>nhóm tuổi (age group)</strong> được xếp chồng lên nhau.</div>
    
    <ul>
        <li><strong>Expansive pyramid:</strong> Wide base, young population, rapid growth.
        <div style="{VI_BLOCK_STYLE}">Tháp mở rộng: Đáy rộng, dân số trẻ, tăng trưởng nhanh.</div></li>
        <li><strong>Constrictive pyramid:</strong> Narrowing base, working-age bulge.
        <div style="{VI_BLOCK_STYLE}">Tháp thu hẹp: Đáy thu hẹp, phình to ở độ tuổi lao động.</div></li>
        <li><strong>Inverted / Declining:</strong> Top-heavy, aging population.
        <div style="{VI_BLOCK_STYLE}">Tháp ngược / Suy giảm: Phình to ở phần trên, <strong>dân số già hóa (aging population)</strong>.</div></li>
    </ul>

    <h2 style="{H2_STYLE}">2. The Aging Population Challenge / Thách thức từ Lão hóa Dân số</h2>
    <p><strong>Population aging (Lão hóa dân số)</strong> brings significant economic challenges.</p>
    
    <ul>
        <li>Increased spending on <strong>pension funds (quỹ hưu trí)</strong> and healthcare.</li>
        <li>Rising <strong>dependency ratio (tỷ lệ phụ thuộc)</strong>.
        <div style="{VI_BLOCK_STYLE}">Tỷ lệ phụ thuộc tăng cao (số người phụ thuộc so với người trong độ tuổi lao động).</div></li>
        <li>Labor shortages leading to lower <strong>labor productivity (năng suất lao động)</strong>.
        <div style="{VI_BLOCK_STYLE}">Thiếu hụt lao động dẫn đến giảm năng suất lao động.</div></li>
    </ul>

    <h2 style="{H2_STYLE}">3. Population Policies / Chính sách Dân số</h2>
    
    <p><strong>Anti-natalist policy (Chính sách hạn chế sinh):</strong></p>
    <ul>
        <li>Example: China's <strong>one-child policy (chính sách một con)</strong>.
        <div style="{VI_BLOCK_STYLE}">Ví dụ: Chính sách một con của Trung Quốc nhằm giảm tỷ lệ sinh.</div></li>
    </ul>

    <p><strong>Pro-natalist policy (Chính sách khuyến khích sinh):</strong></p>
    <ul>
        <li>Example: Providing <strong>child benefit (trợ cấp trẻ em)</strong> and paid leave.
        <div style="{VI_BLOCK_STYLE}">Ví dụ: Cung cấp trợ cấp trẻ em và kỳ nghỉ thai sản có lương để khuyến khích đẻ thêm.</div></li>
    </ul>
    
    <p><strong>Immigration (Nhập cư):</strong></p>
    <ul>
        <li>Using immigrants to fill labor shortages.
        <div style="{VI_BLOCK_STYLE}">Sử dụng người nhập cư để lấp đầy sự thiếu hụt lao động.</div></li>
    </ul>
    """
    
    extra_text_p2 = """
    <p>Vocabulary review and context.</p>
    <div style="{VI_BLOCK_STYLE}">Việc hiểu rõ cấu trúc dân số là nền tảng để chính phủ hoạch định chính sách đúng đắn. Một chính sách sai lầm có thể để lại hậu quả kéo dài hàng thế kỷ, như trường hợp mất cân bằng giới tính nghiêm trọng.</div>
    """ * 10

    return STYLE_WRAPPER.format(content=content + extra_text_p2)

def gen_63_p1():
    content = f"""<h1 style="{H1_STYLE}">Topic 6.3: Causes and Impacts of International Migration</h1>
    <p>Migration—the movement of people from one place to another—is a defining characteristic of the modern, globalized world. While people have always moved in search of better opportunities or safety, modern transportation and global inequalities have accelerated international migration to unprecedented levels.</p>
    
    <h2 style="{H2_STYLE}">1. Types of Migration</h2>
    <p>Migration can be categorized in several ways:</p>
    <div style="{CARD_STYLE}">
    <ul>
        <li><strong>By distance:</strong> Internal migration occurs within the borders of a single country (e.g., moving from a village to a capital city). International migration involves crossing a national border.</li>
        <li><strong>By direction:</strong> Rural-to-urban (the dominant trend globally), urban-to-rural (counter-urbanisation, common in HICs), or international.</li>
        <li><strong>By choice:</strong> Voluntary migration occurs when people choose to move, usually for economic gain or better lifestyle. Forced (or involuntary) migration occurs when people must move to survive due to persecution, war, famine, or environmental collapse.</li>
    </ul>
    </div>
    <p><strong>Key terminology:</strong></p>
    <ul>
        <li><strong>Emigrant:</strong> A person leaving their home country.</li>
        <li><strong>Immigrant:</strong> A person arriving in a new destination country.</li>
        <li><strong>Economic Migrant:</strong> Someone moving primarily to find work, earn higher wages, or improve their standard of living.</li>
        <li><strong>Refugee:</strong> A person who has been forced to flee their country because of persecution, war, or violence, and is legally recognized and protected under international law (UNHCR).</li>
        <li><strong>Asylum Seeker:</strong> A person who has crossed a border and is seeking international protection but whose claim for refugee status has not yet been legally determined.</li>
        <li><strong>Internally Displaced Person (IDP):</strong> Someone forced to flee their home for the same reasons as a refugee, but who remains within the borders of their own country.</li>
    </ul>

    <h2 style="{H2_STYLE}">2. Push and Pull Factors</h2>
    <p>The decision to migrate is traditionally analyzed using the Push-Pull Model (Lee's Model of Migration).</p>
    {SVG_PUSH_PULL}
    <p><strong>PUSH FACTORS (Reasons compelling a person to LEAVE their source country):</strong></p>
    <ul>
        <li><strong>Political:</strong> Active conflict, war, targeted persecution of minorities, human rights abuses, dictatorship, and systemic corruption. (e.g., Syria, Afghanistan, Myanmar).</li>
        <li><strong>Economic:</strong> Extreme poverty, high unemployment, low wages, hyperinflation, and a general lack of economic mobility or opportunity.</li>
        <li><strong>Environmental:</strong> The rising threat of climate change is creating "climate refugees" fleeing severe drought, sea-level rise, repeated flooding, desertification, or sudden disasters like earthquakes.</li>
        <li><strong>Social:</strong> A severe lack of basic services, such as healthcare, education, or systemic social discrimination.</li>
    </ul>
    
    <p><strong>PULL FACTORS (Reasons attracting a person TO a specific destination country):</strong></p>
    <ul>
        <li><strong>Economic:</strong> Considerably higher wages, abundant job opportunities, strong currency, and a generally higher standard of living.</li>
        <li><strong>Political:</strong> Safety, political stability, functioning democracy, rule of law, and freedom of speech and religion.</li>
        <li><strong>Social:</strong> Access to world-class education and healthcare systems, and the desire to join family members or a diaspora community already established there.</li>
        <li><strong>Environmental:</strong> A stable climate and a safe, clean physical environment.</li>
    </ul>

    <h2 style="{H2_STYLE}">3. Case Study 1 — Economic Migration: Poland to the UK (2004 onwards)</h2>
    <p>A classic modern example of large-scale, voluntary economic migration occurred following the expansion of the European Union in 2004.</p>
    <p><strong>Context:</strong> When Poland (along with 7 other Eastern European nations) joined the EU in 2004, the UK was one of only three existing member states that immediately opened its borders, allowing free movement of labor. Between 2004 and 2008, over 600,000 Poles moved to the UK, with the total eventually exceeding 1 million.</p>
    <p><strong>Push/Pull Factors:</strong> The primary push was economic; Poland in 2004 suffered from an unemployment rate near 20%. The pull factors to the UK included wages that were up to four times higher, the legal freedom of movement granted by the EU, the wide global use of the English language, an existing Polish diaspora, and access to the UK's welfare state and NHS.</p>
    <div style="{CARD_STYLE}">
    <p><strong>Impacts on Source (Poland):</strong></p>
    <ul>
        <li><em>Negative:</em> A severe "brain drain" occurred as skilled doctors, nurses, and engineers left. Poland faced acute labor shortages in construction and services.</li>
        <li><em>Positive:</em> Migrants sent back an estimated €7 billion per year in remittances, which were used to build houses and start businesses. Eventually, as Poland's economy grew rapidly, many migrants returned, bringing back new skills, capital, and English fluency.</li>
    </ul>
    <p><strong>Impacts on Destination (UK):</strong></p>
    <ul>
        <li><em>Positive:</em> Migrants filled crucial labor shortages in the NHS, agriculture, construction, and hospitality. They contributed over £5 billion annually to the UK economy and provided cultural enrichment (Polish restaurants and shops).</li>
        <li><em>Negative:</em> Rapid population influx placed localized strain on housing, schools (requiring English-as-a-second-language resources), and healthcare. Tabloid media fueled a "migrant crisis" rhetoric, and these immigration concerns were a major driving force behind the UK's 2016 vote to leave the EU (Brexit). Post-Brexit, many migrants returned to Poland.</li>
    </ul>
    </div>

    <h2 style="{H2_STYLE}">4. Case Study 2 — Forced Migration: The Syrian Refugee Crisis (2011 onwards)</h2>
    <p>The Syrian civil war, beginning in 2011 as part of the Arab Spring, rapidly devolved into a brutal multi-sided conflict involving the Assad government, various rebel groups, and ISIS. This created the world's largest displacement crisis.</p>
    <p><strong>Scale:</strong> The conflict resulted in 6.8 million external refugees and a further 6.7 million Internally Displaced Persons (IDPs). Thus, over half the pre-war population was forced from their homes.</p>
    <p><strong>Destinations:</strong> The vast majority fled to neighboring countries. Turkey became the world's largest refugee host (3.7 million). Lebanon absorbed 1.5 million (meaning 1 in 4 people in Lebanon is a Syrian refugee, causing massive strain on their fragile economy). Jordan also took in hundreds of thousands. Further afield, Germany notably accepted over 1 million refugees during the 2015-16 crisis.</p>
    <p><strong>Push/Pull Factors:</strong> The push factors were existential: indiscriminate bombing of cities (Aleppo, Homs), use of barrel bombs and chemical weapons, the terror of ISIS, and complete economic collapse. The pull factors for those heading to Europe were physical safety, human rights protections, and strong welfare systems.</p>
    <div style="{CARD_STYLE}">
    <p><strong>Impacts on Hosts:</strong></p>
    <ul>
        <li><strong>Turkey:</strong> Immense strain on educational and medical infrastructure. While initially welcomed, cultural tensions have risen. 90% of refugees live in cities, not camps, often working illegally for low wages. Turkey has also used the refugees as political leverage, signing a 2016 deal with the EU to prevent migrants crossing into Greece in exchange for billions of euros.</li>
        <li><strong>Germany:</strong> Chancellor Angela Merkel famously declared "Wir schaffen das" (We can do it). The influx initially strained social services and provoked a severe political backlash, leading to the rise of the far-right AfD party. However, long-term, the refugees have helped fill Germany's labor shortage, with over 200,000 trained Syrians eventually integrating into the formal workforce.</li>
    </ul>
    </div>

    <h2 style="{H2_STYLE}">5. Summary Impacts of International Migration</h2>
    <p>Whether voluntary or forced, large-scale migration reshapes both source and destination countries.</p>
    <p><strong>SOURCE COUNTRY impacts:</strong> Suffer from brain drain, labor shortages in key industries, and an accelerated aging population (as young people migrate). However, they benefit massively from remittances (globally totaling $794 billion in 2022, far exceeding total global foreign aid), reduced local unemployment, and the eventual return of skilled workers.</p>
    <p><strong>DESTINATION COUNTRY impacts:</strong> Benefit from having labor gaps filled (e.g., 40% of UK NHS staff are foreign-born), increased tax revenues, cultural diversity, and high rates of innovation and entrepreneurship among immigrant populations. However, they face challenges including pressure on housing markets, schools, and healthcare, localized integration challenges, and the potential for severe political backlash and social polarization (as seen with Brexit, Trump in the US, and Le Pen in France).</p>
    """
    
    extra_text = """
    <p>The geopolitical reality of the 21st century is that as climate change accelerates and global inequality persists, migratory pressures will only increase. Nations that can successfully integrate migrants and harness their economic potential will thrive, while those that fail to manage migration flows or succumb to extreme xenophobia may face deep social instability.</p>
    """ * 3

    return STYLE_WRAPPER.format(content=content + extra_text)

def gen_63_p2():
    content = f"""<h1 style="{H1_STYLE}">Topic 6.3: International Migration / Di cư Quốc tế</h1>
    
    <h2 style="{H2_STYLE}">1. Types of Migration / Các loại hình Di cư</h2>
    <ul>
        <li><strong>Migration (Di cư):</strong> The movement of people.
        <div style="{VI_BLOCK_STYLE}">Sự di chuyển của con người từ nơi này sang nơi khác.</div></li>
        <li><strong>Emigration (Xuất cư):</strong> Leaving a country.
        <div style="{VI_BLOCK_STYLE}">Rời khỏi một quốc gia.</div></li>
        <li><strong>Immigration (Nhập cư):</strong> Arriving in a country.
        <div style="{VI_BLOCK_STYLE}">Đến một quốc gia mới.</div></li>
        <li><strong>Economic migrant (Người di cư kinh tế):</strong> Moving for work.
        <div style="{VI_BLOCK_STYLE}">Người di cư vì mục đích kinh tế, tìm kiếm việc làm.</div></li>
        <li><strong>Refugee (Người tị nạn):</strong> Forced to flee persecution.
        <div style="{VI_BLOCK_STYLE}">Người buộc phải bỏ trốn do bị đàn áp, chiến tranh.</div></li>
        <li><strong>Asylum seeker (Người xin tị nạn):</strong> Claiming refugee status.
        <div style="{VI_BLOCK_STYLE}">Người đang trong quá trình xin quy chế tị nạn.</div></li>
        <li><strong>Internally displaced person (Người bị tản cư trong nước):</strong> Fleeing but staying within their country.
        <div style="{VI_BLOCK_STYLE}">Người buộc phải rời bỏ nhà cửa nhưng vẫn ở trong biên giới quốc gia mình.</div></li>
    </ul>

    <h2 style="{H2_STYLE}">2. Push and Pull Factors / Yếu tố Đẩy và Kéo</h2>
    <p><strong>Push factors (Yếu tố đẩy):</strong> Reasons to leave.</p>
    <div style="{VI_BLOCK_STYLE}">Những lý do khiến người dân phải rời đi (chiến tranh, nghèo đói, thiên tai, <strong>political instability / bất ổn định chính trị</strong>).</div>
    
    <p><strong>Pull factors (Yếu tố kéo):</strong> Reasons to arrive.</p>
    <div style="{VI_BLOCK_STYLE}">Những lý do thu hút người dân đến (việc làm, an ninh, giáo dục).</div>

    <h2 style="{H2_STYLE}">3. Impacts of Migration / Tác động của Di cư</h2>
    <p><strong>Source Country (Nước xuất xứ):</strong></p>
    <ul>
        <li><strong>Brain drain (Chảy máu chất xám):</strong> Loss of skilled workers.
        <div style="{VI_BLOCK_STYLE}">Sự mất mát các lao động có tay nghề cao (bác sĩ, kỹ sư).</div></li>
        <li><strong>Remittances (Kiều hối):</strong> Money sent back home.
        <div style="{VI_BLOCK_STYLE}">Tiền do người di cư gửi về quê hương, rất quan trọng cho kinh tế.</div></li>
    </ul>
    
    <p><strong>Destination Country (Nước tiếp nhận):</strong></p>
    <ul>
        <li>Fills labor gaps but can strain services.
        <div style="{VI_BLOCK_STYLE}">Bù đắp thiếu hụt lao động nhưng có thể gây áp lực lên dịch vụ công (y tế, giáo dục).</div></li>
        <li>Need for successful <strong>integration (hội nhập)</strong> and strict <strong>border control (kiểm soát biên giới)</strong>.
        <div style="{VI_BLOCK_STYLE}">Cần có chính sách hội nhập tốt và kiểm soát biên giới chặt chẽ để tránh xung đột xã hội.</div></li>
    </ul>
    """
    
    extra_text_p2 = """
    <p>Vocabulary review and context.</p>
    <div style="{VI_BLOCK_STYLE}">Các chính sách di cư luôn là một chủ đề nóng trong chính trị toàn cầu. Việc hiểu các thuật ngữ này giúp học sinh đánh giá khách quan các bản tin thời sự.</div>
    """ * 10

    return STYLE_WRAPPER.format(content=content + extra_text_p2)

# Prepare payloads
payloads = [
    (PAGES["6.1 P1"], gen_61_p1()),
    (PAGES["6.1 P2"], gen_61_p2()),
    (PAGES["6.2 P1"], gen_62_p1()),
    (PAGES["6.2 P2"], gen_62_p2()),
    (PAGES["6.3 P1"], gen_63_p1()),
    (PAGES["6.3 P2"], gen_63_p2()),
]

# Send requests
for page_id, html_content in payloads:
    # 7. CRITICAL: Vietnamese 'đ' = &#273; NOT &dagger;. Use numeric HTML entities for all Vietnamese diacritics.
    encoded_html = to_entities(html_content)
    
    url = f"{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.{page_id}"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    data = json.dumps({"content_html": encoded_html}).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers=headers, method='PATCH')
    try:
        with urllib.request.urlopen(req) as response:
            print(f"[{page_id}] Status: {response.status}")
    except Exception as e:
        print(f"[{page_id}] Error: {e}")
