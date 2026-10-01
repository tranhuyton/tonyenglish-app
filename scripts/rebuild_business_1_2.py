import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 1.2 ID
LID = '7027f2e2-0ac5-4ee6-8913-7d93c7857733'
CODE = '1_2'
TITLE = '1.2 Classification of businesses'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 11 AUDIO SEGMENTS FOR LESSON 1.2
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 1.2: Phân loại Doanh nghiệp",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 1.2: Classification of Businesses. In this lesson, we examine how economies are structured into primary, secondary, and tertiary stages of production, explore the structural shift known as de-industrialisation, and compare private versus public sector ownership in mixed economies.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 1.2: Phân loại Doanh nghiệp. Trong bài học này, chúng ta sẽ tìm hiểu cơ cấu nền kinh tế qua ba khu vực sản xuất: sơ cấp, thứ cấp và tam cấp, hiện tượng phi công nghiệp hóa trong các nền kinh tế phát triển, và so sánh vai trò giữa khu vực tư nhân và khu vực nhà nước trong nền kinh tế hỗn hợp."
    },
    {
        "id": "sec_sectors",
        "title": "1. Ba Khu vực Kinh tế (Three Sectors of Industry)",
        "selector": "#sec-sectors",
        "en": "Section 1 classifies all commercial and economic activities into three sequential stages of production: the primary sector, the secondary sector, and the tertiary sector. Each sector plays an indispensable role in transforming raw natural gifts into final goods and services for consumers.",
        "vi": "Mục 1 phân loại toàn bộ hoạt động kinh tế thành ba giai đoạn sản xuất tuần tự: khu vực sơ cấp, khu vực thứ cấp và khu vực tam cấp. Mỗi khu vực đảm nhiệm một vai trò thiết yếu trong việc biến đổi tài nguyên thiên nhiên thô sơ thành các sản phẩm và dịch vụ hoàn thiện phục vụ đời sống con người."
    },
    {
        "id": "card_sector_primary",
        "title": "🌾 Khu vực Sơ cấp (Primary Sector)",
        "selector": "#card-sector-primary",
        "en": "The primary sector involves the direct extraction and harvesting of natural resources from the earth and sea. Typical industries include agriculture, forestry, commercial fishing, oil and gas extraction, and mineral mining. In early stages of economic development, the primary sector typically employs the majority of the national workforce.",
        "vi": "Khu vực sơ cấp (Primary Sector) bao gồm các hoạt động trực tiếp khai thác và thu hoạch tài nguyên tự nhiên từ lòng đất, rừng và biển cả. Các ngành nghề điển hình gồm nông nghiệp trồng trọt, lâm nghiệp khai thác gỗ, đánh bắt thủy sản, khai thác dầu khí và khai mỏ khoáng sản. Ở các giai đoạn đầu của sự phát triển kinh tế, khu vực sơ cấp thường thu hút đại đa số lực lượng lao động của quốc gia."
    },
    {
        "id": "card_sector_secondary",
        "title": "🏗️ Khu vực Thứ cấp (Secondary Sector)",
        "selector": "#card-sector-secondary",
        "en": "The secondary sector involves manufacturing, processing, and constructing physical products using raw materials provided by the primary sector. Examples include automobile assembly, steel smelting, chemical processing, textile manufacturing, electronic fabrication, and building construction. This sector adds significant value to raw materials.",
        "vi": "Khu vực thứ cấp (Secondary Sector) bao gồm các hoạt động chế tạo, gia công và xây dựng các sản phẩm vật chất từ các nguyên liệu thô do khu vực sơ cấp cung cấp. Ví dụ như lắp ráp ô tô, luyện kim cán thép, hóa chất, may mặc dệt may, sản xuất linh kiện điện tử và thi công xây dựng công trình. Khu vực này đóng vai trò quan trọng trong việc gia tăng giá trị cho các nguồn tài nguyên thô."
    },
    {
        "id": "card_sector_tertiary",
        "title": "🛎️ Khu vực Tam cấp (Tertiary Sector)",
        "selector": "#card-sector-tertiary",
        "en": "The tertiary sector provides commercial and personal services to consumers and other enterprises. Rather than producing tangible goods, it delivers intangible utility. Prominent examples include commercial banking, insurance, transportation, warehousing, hotels, tourism, telecommunications, retail stores, healthcare, and education.",
        "vi": "Khu vực tam cấp (Tertiary Sector) chuyên cung ứng các dịch vụ thương mại và dịch vụ cá nhân cho người tiêu dùng và các doanh nghiệp khác. Thay vì sản xuất hàng hóa vật chất hữu hình, khu vực này tạo ra các tiện ích vô hình. Các ví dụ nổi bật bao gồm ngân hàng thương mại, bảo hiểm, vận tải logistics, lưu kho, khách sạn, du lịch, viễn thông, bán lẻ, y tế và giáo dục."
    },
    {
        "id": "card_sector_basis",
        "title": "📊 Cơ sở Đo lường Quy mô Khu vực Kinh tế",
        "selector": "#card-sector-basis",
        "en": "Economists measure the relative economic importance of the three sectors using two primary criteria: first, the percentage of the country's total workforce employed in each sector; and second, the monetary value of output each sector adds to Gross Domestic Product (GDP). Crucially, the three sectors are interdependent—a disruption in primary extraction directly impacts factory manufacturing and retail distribution.",
        "vi": "Các nhà kinh tế đo lường tầm quan trọng tương đối của ba khu vực kinh tế dựa trên hai tiêu chí cơ bản: thứ nhất là tỷ lệ phần trăm lực lượng lao động cả nước làm việc trong từng khu vực; và thứ hai là giá trị sản lượng tiền tệ mà mỗi khu vực đóng góp vào Tổng sản phẩm quốc nội (GDP). Cần lưu ý rằng cả ba khu vực có mối quan hệ phụ thuộc lẫn nhau mật thiết—bất kỳ sự đình trệ nào ở khâu khai thác sơ cấp cũng sẽ ảnh hưởng ngay đến sản xuất nhà máy và chuỗi bán lẻ."
    },
    {
        "id": "card_deindustrialisation",
        "title": "🌍 Công nghiệp hóa & Phi công nghiệp hóa (De-industrialisation)",
        "selector": "#card-deindustrialisation",
        "en": "As national economies develop, the relative balance between sectors shifts dramatically. In developing countries, industrialisation occurs as workers transition from farming to factory jobs. In advanced developed nations, de-industrialisation takes place as manufacturing employment and output decline while the service sector expands to exceed 70% of GDP. This occurs due to rising disposable consumer incomes spent on leisure, travel, and finance, exhaustion of domestic raw materials, and intense competition from low-wage overseas manufacturing economies.",
        "vi": "Khi nền kinh tế quốc gia phát triển, cán cân tỷ trọng giữa các khu vực có sự dịch chuyển sâu sắc. Ở các nước đang phát triển, quá trình công nghiệp hóa diễn ra mạnh mẽ khi lao động chuyển từ làm nông sang làm việc tại các nhà máy. Ngược lại ở các quốc gia phát triển, quá trình phi công nghiệp hóa (de-industrialisation) xuất hiện khi việc làm và sản lượng trong ngành sản xuất chế tạo suy giảm, nhường chỗ cho ngành dịch vụ bùng nổ chiếm trên 70% GDP. Hiện tượng này phát sinh do thu nhập của người dân tăng cao thúc đẩy chi tiêu vào du lịch, giải trí và tài chính, cùng với sự cạn kiệt tài nguyên trong nước và sự cạnh tranh gay gắt từ các nước sản xuất có chi phí nhân công thấp."
    },
    {
        "id": "sec_mixed_economy",
        "title": "2. Nền Kinh tế Hỗn hợp (Mixed Economy)",
        "selector": "#sec-mixed-economy",
        "en": "Section 2 explores how resources and businesses are owned in a mixed economy. Unlike a pure free-market economy where all resources are privately owned, or a command economy where the state controls everything, a mixed economy features the coexistence of both a private sector and a public sector.",
        "vi": "Mục 2 tìm hiểu cách thức sở hữu nguồn lực và doanh nghiệp trong nền kinh tế hỗn hợp. Khác với nền kinh tế thị trường tự do thuần túy nơi mọi nguồn lực đều thuộc tư nhân, hay nền kinh tế chỉ huy do nhà nước bao cấp toàn bộ, nền kinh tế hỗn hợp có sự song hành cùng tồn tại của cả khu vực tư nhân và khu vực nhà nước."
    },
    {
        "id": "card_private_sector",
        "title": "💼 Khu vực Tư nhân (Private Sector)",
        "selector": "#card-private-sector",
        "en": "The private sector comprises businesses owned and financed by private individuals, partners, or shareholders. Its primary objective is profit maximization and business expansion. Private enterprises are driven by consumer demand and market price mechanisms, with all investment risks borne by private owners. Familiar examples include Apple, Nike, and local family restaurants.",
        "vi": "Khu vực tư nhân (Private Sector) bao gồm các doanh nghiệp do các cá nhân, các thành viên hợp danh hoặc các cổ đông tư nhân bỏ vốn thành lập và quản lý. Mục tiêu hàng đầu của khu vực này là tối đa hóa lợi nhuận và mở rộng quy mô. Doanh nghiệp tư nhân vận hành dựa trên cơ chế thị trường và thị hiếu người tiêu dùng, với mọi rủi ro tài chính do chủ sở hữu tự chịu trách nhiệm. Các ví dụ quen thuộc gồm có Apple, Nike hay các nhà hàng gia đình tại địa phương."
    },
    {
        "id": "card_public_sector",
        "title": "🏛️ Khu vực Nhà nước (Public Sector)",
        "selector": "#card-public-sector",
        "en": "The public sector consists of enterprises and corporations owned, financed, and directed by the national or local government. Its overriding aim is to provide essential public goods and services to enhance citizen welfare, guarantee universal accessibility, and prevent natural monopolies from exploiting consumers. Funding is provided via taxpayer revenue and state budgets. Examples include state public hospitals, national police, public schools, and public transport systems.",
        "vi": "Khu vực nhà nước (Public Sector) bao gồm các cơ quan, đơn vị sự nghiệp và tổng công ty do chính phủ trung ương hoặc chính quyền địa phương sở hữu và quản lý. Mục tiêu cốt lõi của khu vực này là cung ứng các dịch vụ công cộng thiết yếu nhằm nâng cao phúc lợi xã hội, đảm bảo mọi người dân đều tiếp cận được dịch vụ bình đẳng, và ngăn chặn tình trạng độc quyền tự nhiên lạm quyền thao túng giá. Nguồn vốn vận hành được cấp từ ngân sách nhà nước và tiền thuế của dân. Ví dụ như bệnh viện công lập, lực lượng cảnh sát, trường học công lập và hệ thống giao thông công cộng."
    },
    {
        "id": "card_privatisation",
        "title": "🔄 Tư nhân hóa (Privatisation)",
        "selector": "#card-privatisation",
        "en": "Privatisation is the sale of state-owned public corporations to private sector investors. Proponents argue privatisation improves operational efficiency, introduces market competition, eliminates political interference, and raises capital for government budgets. However, critics point out that privatised monopolies may raise consumer prices, cut unprofitable rural services, and cause widespread job redundancies.",
        "vi": "Tư nhân hóa (Privatisation) là quá trình chính phủ bán lại các tổng công ty hoặc doanh nghiệp nhà nước cho các nhà đầu tư tư nhân. Những người ủng hộ cho rằng tư nhân hóa giúp nâng cao hiệu quả vận hành, gia tăng tính cạnh tranh thị trường, chấm dứt sự can thiệp hành chính và bổ sung nguồn thu lớn cho ngân sách nhà nước. Tuy nhiên, mặt trái là các doanh nghiệp sau tư nhân hóa có thể tăng giá cước dịch vụ, cắt giảm các tuyến phục vụ vùng sâu vùng xa không sinh lời và cắt giảm ồ ạt nhân sự."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_sectors": {"start": 1, "end": 6},
    "sec_mixed_economy": {"start": 7, "end": 10}
}

# ==============================================================================
# 2. GENERATE NEW HTML FOR PAGE 1
# ==============================================================================
def build_page_1_html():
    html = """<div style="font-family: 'Segoe UI', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">

    <!-- TOP HEADER BANNER (NO STUDY RESOURCES) -->
    <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="margin-bottom: 35px; padding: 22px 26px; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-radius: 14px; border: 1px solid #e2e8f0; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
            <div>
                <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Unit 1</span>
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">1.2 Classification of Businesses (Phân loại Doanh nghiệp)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. PRIMARY, SECONDARY AND TERTIARY SECTOR -->
    <div style="margin-bottom: 50px;">
        <div id="sec-sectors" class="lecture-interactive-card" data-lecture-section="sec_sectors" style="margin-bottom: 22px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🏭 1. PRIMARY, SECONDARY AND TERTIARY SECTOR</h2>
            <p style="font-size: 15.5px; color: #475569; margin: 0; line-height: 1.6;">All economic activities in a country are classified into three sequential sectors of industry. Bấm vào từng khu vực bên dưới để nghe giảng chi tiết:</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 25px;">
            <div id="card-sector-primary" class="lecture-interactive-card" data-lecture-section="card_sector_primary" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-top: 4px solid #16a34a; border-radius: 12px; padding: 22px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #16a34a; font-size: 19px; margin: 0 0 10px 0; border-bottom: 1.5px dashed #86efac; padding-bottom: 6px; display: flex; align-items: center; justify-content: space-between;">
                    <span>🌾 Primary Sector</span>
                    <span style="font-size: 11px; background: #dcfce7; padding: 2px 7px; border-radius: 10px; font-weight: 700;">Extraction</span>
                </h4>
                <p style="margin: 0 0 10px 0; color: #475569; font-size: 14.5px; line-height: 1.6;">This involves the <b>extraction and harvesting of natural resources</b> from the earth.</p>
                <div style="background: #f0fdf4; padding: 10px 12px; border-radius: 6px; font-size: 13.5px; color: #166534; line-height: 1.5;">
                    <i>Examples: farming/agriculture, mining, fishing, forestry/wood-cutting, oil and gas drilling.</i>
                </div>
            </div>

            <div id="card-sector-secondary" class="lecture-interactive-card" data-lecture-section="card_sector_secondary" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-top: 4px solid #2563eb; border-radius: 12px; padding: 22px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #2563eb; font-size: 19px; margin: 0 0 10px 0; border-bottom: 1.5px dashed #93c5fd; padding-bottom: 6px; display: flex; align-items: center; justify-content: space-between;">
                    <span>🏗️ Secondary Sector</span>
                    <span style="font-size: 11px; background: #dbeafe; padding: 2px 7px; border-radius: 10px; font-weight: 700;">Manufacturing</span>
                </h4>
                <p style="margin: 0 0 10px 0; color: #475569; font-size: 14.5px; line-height: 1.6;">This involves <b>manufacturing, processing, and constructing goods</b> using raw materials from the primary sector.</p>
                <div style="background: #eff6ff; padding: 10px 12px; border-radius: 6px; font-size: 13.5px; color: #1e40af; line-height: 1.5;">
                    <i>Examples: automobile manufacturing, food processing, steel production, textiles, construction.</i>
                </div>
            </div>

            <div id="card-sector-tertiary" class="lecture-interactive-card" data-lecture-section="card_sector_tertiary" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-top: 4px solid #9333ea; border-radius: 12px; padding: 22px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #9333ea; font-size: 19px; margin: 0 0 10px 0; border-bottom: 1.5px dashed #d8b4fe; padding-bottom: 6px; display: flex; align-items: center; justify-content: space-between;">
                    <span>🛎️ Tertiary Sector</span>
                    <span style="font-size: 11px; background: #f3e8ff; padding: 2px 7px; border-radius: 10px; font-weight: 700;">Services</span>
                </h4>
                <p style="margin: 0 0 10px 0; color: #475569; font-size: 14.5px; line-height: 1.6;">This involves providing commercial and personal <b>services</b> to final consumers and other businesses.</p>
                <div style="background: #faf5ff; padding: 10px 12px; border-radius: 6px; font-size: 13.5px; color: #6b21a8; line-height: 1.5;">
                    <i>Examples: banking, insurance, hotels, transport/logistics, hair salons, retail stores, healthcare.</i>
                </div>
            </div>
        </div>

        <!-- Basis of Classification Callout -->
        <div id="card-sector-basis" class="lecture-interactive-card" data-lecture-section="card_sector_basis" style="background: #eff6ff; border-left: 5px solid #3b82f6; border-radius: 10px; padding: 20px 24px; margin-bottom: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h4 style="color: #1e40af; margin: 0 0 10px 0; font-size: 17px; display: flex; align-items: center; gap: 8px;">
                <span>📊</span> Basis of Business Classification &amp; Economic Interdependence
            </h4>
            <p style="margin: 0 0 12px 0; color: #334155; font-size: 15px; line-height: 1.6;">
                How do economists measure the relative importance or size of each sector in an economy?
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px;">
                <div style="background: #ffffff; padding: 12px 16px; border-radius: 8px; border: 1px solid #bfdbfe; font-size: 14px;">
                    <b style="color: #1d4ed8;">1. Workforce Employment:</b> Percentage of the total national workforce employed in each sector.
                </div>
                <div style="background: #ffffff; padding: 12px 16px; border-radius: 8px; border: 1px solid #bfdbfe; font-size: 14px;">
                    <b style="color: #1d4ed8;">2. Output Value:</b> Proportion of total output value contributing to Gross Domestic Product (GDP).
                </div>
            </div>
        </div>

        <!-- Industrialization & De-industrialization in Developed vs Developing -->
        <div id="card-deindustrialisation" class="lecture-interactive-card" data-lecture-section="card_deindustrialisation" style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-left: 5px solid #64748b; padding: 22px 24px; border-radius: 12px; font-size: 15px; color: #475569; line-height: 1.6; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h4 style="color: #0f172a; margin: 0 0 12px 0; font-size: 17px; display: flex; align-items: center; gap: 8px;">
                <span>🌍</span> Reasons for the Changing Importance of Sectors
            </h4>
            <p style="margin: 0 0 14px 0;">
                <b>1. Developing Economies &amp; Industrialisation:</b> Historically, primary extraction was the largest employer. As developing countries modernise, farming becomes mechanised and workers migrate to urban factories. This rapid shift is called <b>industrialisation</b>.
            </p>
            <p style="margin: 0 0 14px 0;">
                <b>2. Developed Economies &amp; De-industrialisation:</b> In advanced countries (e.g. UK, USA, Singapore), the tertiary sector accounts for over 75% of employment and GDP, while manufacturing shrinks. This decline is called <b>de-industrialisation</b>.
            </p>
            <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px 18px; font-size: 14px;">
                <b style="color: #0f172a;">Why does de-industrialisation happen in developed countries?</b>
                <ul style="margin: 8px 0 0 0; padding-left: 20px; line-height: 1.6;">
                    <li><b>Higher disposable incomes:</b> Wealthier consumers spend heavily on services (tourism, restaurants, private healthcare).</li>
                    <li><b>Global competition:</b> Manufacturing moves overseas to emerging economies with lower labour costs.</li>
                    <li><b>Depletion of raw materials:</b> Domestic mineral and natural resources run out or become uneconomic to extract.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 2. PRIVATE AND PUBLIC SECTOR -->
    <div style="margin-bottom: 50px;">
        <div id="sec-mixed-economy" class="lecture-interactive-card" data-lecture-section="sec_mixed_economy" style="margin-bottom: 22px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🤝 2. PRIVATE AND PUBLIC SECTOR IN A MIXED ECONOMY</h2>
            <p style="font-size: 15.5px; color: #475569; margin: 0; line-height: 1.6;">In a <b>Mixed Economy</b>, both the private sector and the public sector coexist to balance market efficiency with social equity and citizen welfare. Bấm vào từng thẻ bên dưới để nghe giảng chi tiết:</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 22px;">
            <div id="card-private-sector" class="lecture-interactive-card" data-lecture-section="card_private_sector" style="background: #fff7ed; border: 1.5px solid #fed7aa; border-left: 5px solid #ea580c; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <h4 style="color: #c2410c; font-size: 19px; margin: 0 0 12px 0; display: flex; align-items: center; justify-content: space-between;">
                    <span>💼 Private Sector</span>
                    <span style="font-size: 11px; background: #ffedd5; padding: 2px 7px; border-radius: 10px; font-weight: 700; color: #c2410c;">For Profit</span>
                </h4>
                <p style="margin: 0 0 10px 0; color: #475569; font-size: 14.5px; line-height: 1.6;">Businesses owned and managed by <b>private individuals and shareholders</b>.</p>
                <ul style="margin: 0; padding-left: 20px; color: #475569; font-size: 14px; line-height: 1.6;">
                    <li><b>Primary Aim:</b> Profit maximization and return on shareholder investment.</li>
                    <li><b>Finance &amp; Risk:</b> Financed by private capital; risks borne completely by owners.</li>
                    <li><b>Resource Allocation:</b> Governed by market forces (consumer demand and price mechanism).</li>
                    <li><b>Examples:</b> Apple, Nike, local cafes and private retail stores.</li>
                </ul>
            </div>

            <div id="card-public-sector" class="lecture-interactive-card" data-lecture-section="card_public_sector" style="background: #f0fdfa; border: 1.5px solid #99f6e4; border-left: 5px solid #0d9488; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <h4 style="color: #0f766e; font-size: 19px; margin: 0 0 12px 0; display: flex; align-items: center; justify-content: space-between;">
                    <span>🏛️ Public Sector</span>
                    <span style="font-size: 11px; background: #ccfbf1; padding: 2px 7px; border-radius: 10px; font-weight: 700; color: #0f766e;">Public Welfare</span>
                </h4>
                <p style="margin: 0 0 10px 0; color: #475569; font-size: 14.5px; line-height: 1.6;">Enterprises and corporations owned and operated by the <b>government</b>.</p>
                <ul style="margin: 0; padding-left: 20px; color: #475569; font-size: 14px; line-height: 1.6;">
                    <li><b>Primary Aim:</b> Providing essential public services and maximizing citizen welfare (not profit).</li>
                    <li><b>Finance:</b> Funded by state budget and taxpayer revenues.</li>
                    <li><b>Resource Allocation:</b> Planned and directed by government priorities and policy.</li>
                    <li><b>Examples:</b> Public hospitals, state schools, police, national postal service.</li>
                </ul>
            </div>
        </div>

        <div id="card-privatisation" class="lecture-interactive-card" data-lecture-section="card_privatisation" style="background: #eef2ff; border: 1.5px solid #c7d2fe; border-left: 5px solid #6366f1; padding: 20px 24px; border-radius: 12px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h4 style="margin: 0 0 8px 0; font-size: 17px; color: #4338ca; font-weight: bold;">
                🔄 Privatisation (Tư nhân hóa Doanh nghiệp Nhà nước)
            </h4>
            <p style="margin: 0 0 10px 0; font-size: 14.5px; color: #334155; line-height: 1.6;">
                <b>Privatisation</b> refers to the sale of public sector businesses to the private sector.
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px; font-size: 13.5px;">
                <div style="background: #ffffff; padding: 10px 14px; border-radius: 8px; border: 1px solid #c7d2fe;">
                    <b style="color: #16a34a;">✅ Arguments For:</b> Higher efficiency driven by profit motive, competition lowers prices, reduces burden on taxpayers.
                </div>
                <div style="background: #ffffff; padding: 10px 14px; border-radius: 8px; border: 1px solid #c7d2fe;">
                    <b style="color: #b91c1c;">❌ Arguments Against:</b> Private monopolies may exploit consumers, job cuts to lower costs, social services ignored.
                </div>
            </div>
        </div>
    </div>

</div>"""
    return html

# ==============================================================================
# 3. GENERATE NEW HTML FOR PAGE 2 (BILINGUAL)
# ==============================================================================
def build_page_2_html(original_p2):
    pattern = r'<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">[\s\S]*?</div>'
    header_banner = """<div style="margin-bottom: 35px; padding: 22px 26px; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-radius: 14px; border: 1px solid #e2e8f0; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
        <div>
            <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Song Ngữ Anh - Việt</span>
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">1.2 Classification of Businesses (Phân loại Doanh nghiệp)</h1>
        </div>
    </div>"""
    new_p2 = re.sub(pattern, header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 1.2 Audio and HTML ===")
    
    # 0. Clean stale audio files so that all 11 segments match perfectly
    audio_dir = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'business', CODE)
    os.makedirs(audio_dir, exist_ok=True)
    valid_ids = {s['id'] for s in segments}
    for fname in os.listdir(audio_dir):
        if fname.endswith('.mp3'):
            base_id = fname[:-4]
            if base_id not in valid_ids or base_id in {'sec_sectors', 'sec_mixed_economy', 'card_private_public_sector'}:
                try:
                    os.remove(os.path.join(audio_dir, fname))
                    print(f"  [CLEAN] Removed outdated audio: {fname}")
                except Exception as e:
                    print(f"  [WARN] Could not remove {fname}: {e}")

    # 1. Generate audio files and write manifest.json
    print(f"\nGenerating {len(segments)} audio segments...")
    manifest = await process_lecture_audio(CODE, LID, COURSE_TITLE, TITLE, segments, major_sections, subject='business')
    
    # 2. Build Page 1 HTML
    p1_html = build_page_1_html()
    diff1 = len(p1_html.split('<div')) - len(p1_html.split('</div>'))
    print(f"\nPage 1 HTML div diff: {diff1}")
    if diff1 != 0:
        raise ValueError(f"Page 1 has div balance error: {diff1}")
        
    # 3. Build Page 2 HTML
    with open('scripts/bs_1_2_page_2.html', 'r', encoding='utf-8') as f:
        orig_p2 = f.read()
    p2_html = build_page_2_html(orig_p2)
    diff2 = len(p2_html.split('<div')) - len(p2_html.split('</div>'))
    print(f"Page 2 HTML div diff: {diff2}")
    if diff2 != 0:
        raise ValueError(f"Page 2 has div balance error: {diff2}")
        
    # 4. Update Supabase
    print("\nUpdating Supabase page 1...")
    res1 = sb.table('lecture_pages').update({'content_html': p1_html}).eq('lecture_id', LID).eq('page_number', 1).execute()
    print(f"Page 1 updated: {len(res1.data)} rows.")
    
    print("Updating Supabase page 2...")
    res2 = sb.table('lecture_pages').update({'content_html': p2_html}).eq('lecture_id', LID).eq('page_number', 2).execute()
    print(f"Page 2 updated: {len(res2.data)} rows.")
    
    print("\n✅ REBUILD 1.2 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
