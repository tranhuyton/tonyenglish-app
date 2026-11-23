# -*- coding: utf-8 -*-
"""
Capstone Hard M2 Boss Masterclass (750–800 Sprint) — R&W Boss Drills 1 & 2 (30 Elite Qs):
- Boss Drill 1 (boss_drill_1): Dense Science Logic & Multi-Variable Mapping (15 Qs)
- Boss Drill 2 (boss_drill_2): 50/50 Trap Elimination — 1-Millimeter Rule (15 Qs)

100% original, copyright-clean, zero overlap with Mocks #1–#8 or Drills 1.1–5.5.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from sat_drills_1_1_and_2_1 import q_item
from sat_drills_5_4_to_5_5 import svg_bar_chart, html_table
from sat_qa_validator import validate_sat_test

BOSS_DRILL_1_TITLE = '🔥 R&W Boss Drill 1: Dense Science Logic & Multi-Variable Mapping (15 câu 750–800)'
BOSS_DRILL_2_TITLE = '🔥 R&W Boss Drill 2: 50/50 Trap Elimination — 1-Millimeter Rule (15 câu 750–800)'


# ============================================================================
# BOSS DRILL 1: DENSE SCIENCE LOGIC & MULTI-VARIABLE MAPPING (15 Qs)
# Answer key balance: A=4 (Q3,Q6,Q10,Q15), B=4 (Q1,Q5,Q9,Q13), C=4 (Q4,Q8,Q11,Q14), D=3 (Q2,Q7,Q12)
# ============================================================================

def get_boss_drill_1():
    D_II = 'Information and Ideas'
    S_TXT = 'Command of Evidence (Textual)'
    S_QNT = 'Command of Evidence (Quantitative)'
    S_INF = 'Inferences'

    questions = [
        # Q1 — Epigenetics (CoE Textual — Weaken via Postnatal Confounder) [Key: B]
        q_item(
            'sat_boss_d1_q1', 1, D_II, S_TXT, 'Hard',
            '<p>Epigeneticist Dr. Haruto Fujimoto exposed pregnant mice (F0) to a mild metabolic stressor and observed that both their offspring (F1) and grand-offspring (F2) exhibited elevated baseline cortisol levels and reduced DNA methylation at the <i>Nr3c1</i> stress-receptor gene, even though the F2 generation was housed in stress-free cages. Fujimoto concluded that the maternal stressor permanently reprogrammed germline DNA methylation marks and transmitted them across generations independently of postnatal maternal care.</p>',
            'Which finding, if true, would most directly weaken Fujimoto’s conclusion?',
            [
                'The stressed F0 mothers experienced temporary post-weaning weight loss and altered sleep cycles that returned to baseline levels within two weeks of separating from their litters.',
                'Cross-fostering newborn F1 and F2 pups from stressed lineages to unstressed lactating mothers at birth completely eliminated both elevated cortisol and reduced <i>Nr3c1</i> methylation.',
                'When F2 embryos from stressed grandmothers were gestated in and nursed exclusively by unstressed surrogate mothers in stress-free cages, the resulting adults still displayed elevated cortisol and reduced <i>Nr3c1</i> methylation.',
                'Exposing adult male rats to an unrelated nutritional stressor altered DNA methylation across hepatic metabolic genes without producing detectable changes at the <i>Nr3c1</i> stress-receptor locus.'
            ],
            'B',
            'Bản đồ biến số: Giả thuyết Fujimoto khẳng định dấu ấn methyl hóa di truyền qua tế bào mầm (germline) ĐỘC LẬP với chăm sóc sau sinh (postnatal care). Để BÁC BỎ trực tiếp, ta cần thí nghiệm giữ nguyên phơi nhiễm trước sinh/germline nhưng loại bỏ biến nhiễu chăm sóc sau sinh (cross-fostering ngay lúc mới sinh) → hiệu ứng biến mất hoàn toàn ở cả F1 và F2 (B)! Cẩn thận bẫy đảo chiều cực độc ở C: hiệu ứng VẪN TỒN TẠI dù đã thay mẹ nuôi là bằng chứng CỦNG CỐ (strengthen), không phải làm yếu!',
            'Trong câu hỏi Weaken thí nghiệm sinh học, luôn tìm biến nhiễu (confounding variable: ở đây là postnatal maternal care) và chọn đáp án tách riêng biến đó làm biến mất hoàn toàn kết quả mục tiêu.',
            [
                ('Irrelevant Side Effect', 'Biến động cân nặng và giấc ngủ tạm thời của chuột mẹ F0 sau cai sữa không hề bác bỏ cơ chế di truyền biểu sinh sang F1–F2.'),
                ('Đáp án đúng', 'Tách triệt để biến nhiễu chăm sóc sau sinh ngay lúc lọt lòng (sau khi phơi nhiễm germline đã xảy ra) khiến kiểu hình stress & methyl hóa biến mất hoàn toàn → bác bỏ trực tiếp kết luận "independently of postnatal care".'),
                ('Inverted Logic (Strengthens!)', 'Bẫy đảo chiều kinh điển của Hard M2: nếu thay mẹ nuôi mà F2 VẪN giảm methyl hóa và tăng cortisol thì đó là bằng chứng CỦNG CỐ giả thuyết di truyền germline của Fujimoto!'),
                ('Wrong Species & Locus', 'Thí nghiệm trên chuột cống đực với tác nhân khác và gen khác không liên quan đến kết luận trên chuột nhắt của Fujimoto.'),
            ]
        ),

        # Q2 — Paleomagnetism (CoE Quantitative [html_table] — Thermal Overprinting Confounder) [Key: D]
        q_item(
            'sat_boss_d1_q2', 2, D_II, S_QNT, 'Elite 750+',
            html_table(
                'Table 1. Paleomagnetic Readings and Thermal History of Archean Zircon-Bearing Rocks',
                ['Rock Sample', 'Crystallization Age (Ga)', 'Peak Metamorphic Temp (°C)', 'Measured Paleointensity (µT)', 'Adjacent Unheated Vein Alignment'],
                [
                    ['Isua-14', '3.85', '640°C', '28.4', 'Uniformly aligned (2.7 Ga field)'],
                    ['Acasta-09', '3.78', '615°C', '25.1', 'Uniformly aligned (2.7 Ga field)'],
                    ['JackHills-22', '3.62', '310°C', '21.6', 'Randomly oriented (unreset)'],
                    ['Barberton-03', '3.46', '290°C', '19.2', 'Randomly oriented (unreset)'],
                ]
            ) + '<p>Geophysicists seeking evidence that Earth possessed an active geomagnetic dynamo earlier than 3.7 billion years ago (Ga) must rule out thermal remagnetization: if an ancient rock is subsequently heated above magnetite’s Curie temperature of 580°C, its original magnetic signature is erased and overwritten by whatever younger field prevails during cooling—a heating event that also forces adjacent mineral veins into uniform regional alignment. A rival team contends that the strong magnetic signals recorded in the pre-3.7 Ga samples in Table 1 do not constitute reliable evidence of a pre-3.7 Ga geodynamo.</p>',
            'Which choice best describes data from the table that support the rival team’s contention?',
            [
                'JackHills-22 (3.62 Ga) and Barberton-03 (3.46 Ga) remained well below magnetite’s 580°C Curie threshold and retained randomly oriented adjacent veins, confirming their paleointensity values of 21.6 and 19.2 µT.',
                'Isua-14 (28.4 µT) and Acasta-09 (25.1 µT) yielded higher paleointensity readings than JackHills-22 (21.6 µT) and Barberton-03 (19.2 µT), indicating that Earth’s magnetic field weakened steadily after 3.7 Ga.',
                'All four Archean rock samples crystallized between 3.85 Ga and 3.46 Ga and exhibited measured paleointensities exceeding 19 µT despite experiencing peak temperatures ranging from 290°C to 640°C.',
                'Although both pre-3.7 Ga samples—Isua-14 (3.85 Ga) and Acasta-09 (3.78 Ga)—yielded strong paleointensity values, both exceeded 580°C (640°C and 615°C) and have adjacent veins uniformly aligned with a younger 2.7 Ga field.'
            ],
            'D',
            'Lập bản đồ 3 cột đồng thời: Điều kiện mục tiêu là mẫu ĐÁ CỔ HƠN 3.7 Ga (Isua-14: 3.85 Ga; Acasta-09: 3.78 Ga). Ngưỡng nhiễu nhiệt (Curie temperature) là >580°C + mạch đá lân cận bị xếp thẳng hàng theo từ trường trẻ hơn. Đối chiếu bảng: CẢ HAI mẫu >3.7 Ga đều bị nung vượt 580°C (640°C và 615°C) VÀ mạch lân cận đều bị định hướng lại theo từ trường trẻ 2.7 Ga → tín hiệu 28.4 & 25.1 µT chỉ là dấu ấn ghi đè (overwritten)! Chọn D!',
            'Trong bảng khoa học đa biến Hard M2, luôn khóa "ngưỡng loại trừ" định nghĩa trong văn bản (Curie > 580°C + mạch lân cận xếp thẳng hàng) rồi chiếu chéo lên đúng tập mẫu mục tiêu (> 3.7 Ga).',
            [
                ('Wrong Sample Subset (True Data)', 'Số liệu đúng nhưng nói về 2 mẫu TRẺ HƠN 3.7 Ga (3.62 và 3.46 Ga) — không hề ủng hộ lập luận về 2 mẫu >3.7 Ga.'),
                ('Confounder Blindness', 'Chấp nhận số liệu 28.4 và 25.1 µT như tín hiệu gốc của thời kỳ >3.7 Ga, phớt lờ hoàn toàn việc mẫu đã bị nung xóa từ tính ở >600°C.'),
                ('Surface Summary Only', 'Chỉ tóm tắt gộp cả 4 mẫu, bỏ qua điểm quyết định rằng đúng hai mẫu >3.7 Ga đã vượt ngưỡng 580°C và có mạch đá bị đặt lại.'),
                ('Đáp án đúng', 'Kết nối gọn và đủ 3 biến (2 mẫu >3.7 Ga + nhiệt độ 640°C/615°C vượt 580°C + mạch đá bị đặt lại theo từ trường 2.7 Ga) chứng minh tín hiệu đã bị ghi đè nhiệt.'),
            ]
        ),

        # Q3 — Microbial Consortia (Inferences — Syntrophic Inhibitory-Product Removal) [Key: A]
        q_item(
            'sat_boss_d1_q3', 3, D_II, S_INF, 'Elite 750+',
            '<p>In anaerobic bioreactor trials, microbiologist Dr. Naledi Dlamini isolated a slow-growing bacterium (<i>Syntrophomonas</i> strain K4) that ferments butyrate into acetate and hydrogen gas. In pure culture, strain K4 halts cell division within hours because accumulating dissolved hydrogen renders butyrate fermentation thermodynamically impossible once hydrogen pressure exceeds 10 pascals. Yet when strain K4 is co-cultured with an archaeon (<i>Methanospirillum</i> strain M9)—which cannot metabolize butyrate at all but rapidly consumes hydrogen gas to generate methane—both microbes proliferate steadily for weeks, unless researchers add a selective inhibitor that blocks methane synthesis without directly harming strain K4, whereupon strain K4 promptly stops dividing. Taken together, these results indicate that ______</p>',
            'Which choice most logically completes the text?',
            [
                'strain K4’s growth in co-culture relies on strain M9 continuously clearing inhibitory hydrogen gas rather than breaking down butyrate directly.',
                'strain M9 enzymatically converts butyrate into acetate on behalf of strain K4 whenever dissolved hydrogen pressure in the bioreactor rises above 10 pascals.',
                'the selective methane-synthesis inhibitor directly deactivates strain K4’s butyrate-fermentation enzymes even when dissolved hydrogen pressure remains safely below 10 pascals.',
                'strain K4 can sustain rapid cell division indefinitely in pure anaerobic culture provided that dissolved acetate is continuously removed from the bioreactor medium.'
            ],
            'A',
            'Chuỗi suy luận đa bước: (1) Đơn nuôi: K4 phân giải butyrate tạo H₂ → H₂ > 10 Pa tự khóa chặt phản ứng làm K4 ngừng phân chia. (2) Đồng nuôi với M9: M9 KHÔNG dùng được butyrate nhưng ăn sạch H₂ thành methane → cả hai sống khỏe. (3) Thêm chất ức chế tạo methane (không hại trực tiếp K4) → M9 ngừng ăn H₂ → K4 ngừng phân chia ngay lập tức! Suy luận chuẩn 1mm: K4 sống bền khi đồng nuôi là nhờ M9 liên tục dọn sạch khí H₂ ức chế, không phải do M9 tự phân giải butyrate (A)!',
            'Với chuỗi thí nghiệm có chất ức chế chọn lọc (selective inhibitor), hãy lần ngược chuỗi nhân quả A → B → C: khóa phản ứng của B mà không đụng trực tiếp đến A nhưng A vẫn dừng chứng tỏ A lệ thuộc vào hoạt động xử lý sản phẩm phụ của B.',
            [
                ('Đáp án đúng', 'Khớp trọn vẹn cả 3 dữ kiện: loại trừ vai trò phân giải butyrate của M9 và chốt đúng cơ chế giải phóng nút thắt nhiệt động nhờ dọn khí H₂.'),
                ('Direct Contradiction', 'Đoạn văn khẳng định rõ M9 "cannot metabolize butyrate at all".'),
                ('Direct Contradiction', 'Đoạn văn nêu rõ chất ức chế "blocks methane synthesis without directly harming strain K4".'),
                ('Wrong Bottleneck Variable', 'Nút thắt ức chế được nêu trong bài là khí hydrogen (>10 Pa), không phải acetate.'),
            ]
        ),

        # Q4 — Atmospheric Aerosols (CoE Textual — Support Coupled Radiative-Chemical Trade-Off) [Key: C]
        q_item(
            'sat_boss_d1_q4', 4, D_II, S_TXT, 'Hard',
            '<p>Atmospheric physicist Dr. Matteo Ferretti evaluates stratospheric sulfate aerosol injection—dispersing reflective sulfuric acid droplets 20 kilometers aloft—as an emergency planetary cooling method. Although sulfate droplets scatter sunlight and lower surface temperatures, Ferretti argues that they create a hazardous radiative-chemical trade-off: their acidic liquid surfaces catalyze heterogeneous reactions that convert inert chlorine reservoirs into active ozone-destroying radicals. He further contends that substituting solid calcium carbonate (calcite) particles for sulfate aerosols would markedly reduce this stratospheric ozone loss without sacrificing solar reflectivity.</p>',
            'Which finding from a laboratory and modeling study, if true, would most directly support Ferretti’s contention regarding calcium carbonate?',
            [
                'Industrial-grade calcium carbonate is substantially cheaper to mine, pulverize, and deliver to high-altitude aircraft than comparable tonnages of liquid sulfuric acid precursors.',
                'Under simulated conditions at 20 kilometers altitude, solid calcite particles coagulated twice as rapidly as sulfate droplets, settling out within weeks and reflecting significantly less incoming solar radiation.',
                'In stratospheric chamber tests with chlorine reservoirs, calcite particles matched sulfate’s solar reflectivity while neutralizing chlorine intermediates instead of generating ozone-destroying radicals.',
                'Multi-year satellite measurements collected after the 1991 Mount Pinatubo volcanic eruption confirmed that massive stratospheric sulfate plumes caused measurable temporary ozone depletion across mid-latitude skies.'
            ],
            'C',
            'Khóa ĐÚNG mục tiêu câu hỏi: "Ferretti’s contention **regarding calcium carbonate**" gồm 2 vế bắt buộc phải được chứng minh đồng thời: [1] giảm đáng kể phá hủy tầng ozone (không chuyển clo trơ thành gốc phá ozone) VÀ [2] không đánh mất độ phản xạ ánh sáng mặt trời (without sacrificing solar reflectivity). Duy nhất C xác nhận trọn vẹn cả 2 vế! Đừng sập bẫy D: dữ liệu núi lửa Pinatubo rất thật và đúng về sulfate, nhưng hoàn toàn không kiểm chứng luận điểm về calcium carbonate!',
            'Luôn gạch chân phần đối tượng cụ thể cuối câu hỏi ("regarding calcium carbonate") — bẫy 1400 hay trích bằng chứng ủng hộ nửa ĐẦU đoạn văn (sulfate) thay vì luận điểm mục tiêu ở cuối đoạn!',
            [
                ('Irrelevant Variable (Cost)', 'Chi phí khai thác/vận chuyển hoàn toàn nằm ngoài hai tiêu chí vật lý-hóa học của luận điểm (bảo vệ ozone + giữ độ phản xạ).'),
                ('Opposite / Weakens Contention', 'Hạt calcite vón cục, lắng nhanh và phản xạ KÉM HƠN hẳn → trực tiếp bác bỏ vế "without sacrificing solar reflectivity".'),
                ('Đáp án đúng', 'Xác nhận gọn đủ cả 2 vế bằng chứng cho calcite: độ phản xạ ánh sáng ngang bằng sulfate VÀ trung hòa thay vì kích hoạt gốc clo phá ozone.'),
                ('Wrong Target (First-Half Trap)', 'Chỉ chứng minh tác hại của sulfate sau vụ phun trào 1991, không nói gì về hiệu quả thay thế của calcium carbonate.'),
            ]
        ),

        # Q5 — Neuroplasticity (CoE Quantitative [svg_bar_chart] — Sham & Baseline Controls) [Key: B]
        q_item(
            'sat_boss_d1_q5', 5, D_II, S_QNT, 'Hard',
            svg_bar_chart(
                'Mean Tactile Discrimination Gain (%) After 6 Weeks by Trial Arm',
                ['0%', '10%', '20%', '30%', '40%'],
                [('No Training', 2, '+2%'), ('Training Only', 26, '+26%'), ('Train+Sham', 28, '+28%'), ('Train+tDCS', 30, '+30%')],
                40
            ) + '<p>Commercial brain-stimulation clinics promote transcranial direct-current stimulation (tDCS) as a major booster of adult sensory neuroplasticity, citing studies in which volunteers receiving tactile practice plus tDCS outperformed untrained controls. Neuroscientist Dr. Chidi Nwosu, however, conducted a four-arm randomized trial—in which group differences of 5 percentage points or fewer were not statistically significant—to determine whether genuine gains arise from electrical stimulation itself rather than from behavioral training and the placebo expectation of wearing stimulation headgear.</p>',
            'Which choice best describes data from the graph that support the conclusion that tDCS provides no statistically meaningful benefit beyond tactile training and placebo effects?',
            [
                'Participants assigned to the Train+tDCS arm achieved a +30% gain in tactile discrimination after six weeks, fifteen times larger than the +2% gain recorded by the No Training control arm.',
                'The Train+tDCS gain (+30%) exceeded Train+Sham (+28%) by just 2 percentage points and Training Only (+26%) by 4 percentage points—both within the nonsignificant threshold.',
                'Participants in the Train+Sham headgear arm recorded a +26% tactile discrimination improvement after six weeks, performing slightly below the Training Only arm at +28%.',
                'All three randomized arms that completed six weeks of structured tactile practice achieved mean improvements exceeding 25%, whereas the No Training arm improved by only 2%.'
            ],
            'B',
            'Nhận diện bẫy đối chứng giả (Missing Active Control): Phòng khám thương mại chỉ so `Train+tDCS (+30%)` với `No Training (+2%)` — bỏ qua hoàn toàn hiệu ứng tập luyện (`Training Only: +26%`) và hiệu ứng giả dược đội mũ kích điện (`Train+Sham: +28%`). Văn bản cho ngưỡng có ý nghĩa thống kê là >5 điểm phần trăm. So sánh chuẩn: 30% − 28% = 2 điểm % và 30% − 26% = 4 điểm % (cả hai đều ≤5 điểm %, không có ý nghĩa thống kê) ⇒ tDCS không cộng thêm lợi ích thực chất nào ngoài tập luyện và giả dược (B)!',
            'Khi đề bài có nhóm đối chứng giả dược (Sham control) và ngưỡng thống kê (significance threshold), đáp án đúng PHẢI so sánh trực tiếp nhóm điều trị với nhóm Sham/Training Only chứ không bao giờ dừng ở nhóm No Training!',
            [
                ('Naive Baseline Fallacy', 'Bẫy y hệt cách quảng cáo sai lệch của phòng khám: so Train+tDCS với No Training mà bỏ qua hai nhóm đối chứng thực chất là Training Only và Train+Sham.'),
                ('Đáp án đúng', 'Đối chiếu chính xác Train+tDCS (+30%) với cả Train+Sham (+28%, lệch 2%) và Training Only (+26%, lệch 4%), chứng minh chênh lệch nằm gọn dưới ngưỡng ý nghĩa thống kê 5%.'),
                ('Swapped Bar Values', 'Đọc ngược số liệu hai cột giữa: Train+Sham là +28% còn Training Only là +26%.'),
                ('Incomplete / Wrong Claim', 'Số liệu đúng nhưng chỉ chứng minh việc tập luyện xúc giác có ích, không so sánh riêng giá trị gia tăng của tDCS so với Sham.'),
            ]
        ),

        # Q6 — Historical Metallurgy (Inferences — Dual Necessary Conditions Deduction) [Key: A]
        q_item(
            'sat_boss_d1_q6', 6, D_II, S_INF, 'Elite 750+',
            '<p>Metallurgists long struggled to reproduce the undulating light-and-dark bands characteristic of historic Damascus blades forged from South Indian wootz steel ingots. High-resolution electron microscopy of surviving blades revealed that the pale bands consist of microscopic iron-carbide sheets nucleated around trace impurities of vanadium and molybdenum present at roughly 0.005% by weight in specific ancient ore veins. Crucially, these carbide bands precipitate only when a smith subjects vanadium-bearing ingots to repeated forging and annealing cycles kept strictly below 850°C; heating the ingot above 1,100°C permanently dissolves the vanadium-carbide nuclei into a uniform matrix. When nineteenth-century European smelters relied on purer regional iron ores and hotter industrial blast furnaces, they could not replicate authentic Damascus banding. Taken together, these findings imply that ______</p>',
            'Which choice most logically completes the text?',
            [
                'authentic Damascus banding depended on both trace-element ore chemistry and bounded thermal cycling, so altering either factor prevented banding.',
                'nineteenth-century European smelters could have reproduced authentic Damascus carbide banding from their purer regional ores simply by holding forging temperatures below 850°C.',
                'heating South Indian wootz steel ingots above 1,100°C inside industrial blast furnaces accelerated the precipitation of iron-carbide sheets around trace vanadium impurities.',
                'historic Damascus blades achieved superior mechanical tensile strength relative to modern alloy steels exclusively because European regional iron ores lacked trace molybdenum.'
            ],
            'A',
            'Lập sơ đồ điều kiện CẦN ĐỒNG THỜI (Joint Necessary Conditions): Để hình thành vân carbide Damascus cần ĐỒNG THỜI [Điều kiện 1: quặng có tạp chất vi lượng vanadium/molybdenum ~0.005% làm nhân kết tinh] VÀ [Điều kiện 2: chu trình rèn/ủ giữ chặt dưới 850°C, không vượt 1,100°C]. Thiếu BẤT KỲ điều kiện nào cũng thất bại! Bẫy 1400 cực hay ở B: tách rời 1 biến, cho rằng chỉ cần giữ nhiệt <850°C với quặng tinh khiết hơn của châu Âu là tạo được vân — sai vì quặng tinh khiết thiếu nhân vanadium!',
            'Gặp cấu trúc "only when X is combined with Y" trong bài khoa học vật liệu, luôn cảnh giác bẫy Single-Cause Reductionism (chỉ giữ X hoặc chỉ giữ Y là đủ).',
            [
                ('Đáp án đúng', 'Tổng hợp gọn và chính xác cấu trúc điều kiện kép (hóa học vi lượng của quặng + giới hạn chu trình nhiệt <850°C) mà văn bản thiết lập.'),
                ('Single-Cause Trap', 'Bỏ quên điều kiện quặng phải có vi lượng vanadium/molybdenum; giữ nhiệt <850°C trên quặng tinh khiết vẫn không có nhân kết tinh.'),
                ('Reversed Temperature Logic', 'Ngược hoàn toàn văn bản: nung vượt 1,100°C làm HÒA TAN VĨNH VIỄN (dissolves) các nhân carbide chứ không thúc đẩy kết tụ.'),
                ('Out of Scope Comparison', 'Đoạn văn không hề so sánh độ bền kéo với thép hợp kim hiện đại.'),
            ]
        ),

        # Q7 — Evolutionary Developmental Biology (CoE Textual — Cis-Regulatory vs. Coding Swap) [Key: D]
        q_item(
            'sat_boss_d1_q7', 7, D_II, S_TXT, 'Elite 750+',
            '<p>Closely related cave-dwelling and surface-dwelling populations of a characin fish share nearly identical amino-acid sequences for <i>Pitx1</i>, a master developmental transcription factor required for both lower-jaw formation and pelvic-fin outgrowth. Yet cave fish completely lack pelvic fins while developing normal jaws. Evolutionary developmental biologist Dr. Sonia Álvarez hypothesizes that pelvic-fin loss evolved not through a disabling mutation in the <i>Pitx1</i> protein-coding region—which would fatally deform the jaw—but through the deletion of a tissue-specific regulatory enhancer that switches <i>Pitx1</i> on exclusively in the developing pelvic bud.</p>',
            'Which experimental finding, if true, would most directly support Álvarez’s hypothesis?',
            [
                'Deleting the entire <i>Pitx1</i> protein-coding sequence in surface-fish embryos yields healthy adult fish that develop normal lower jaws while lacking pelvic fins.',
                'Surface-dwelling characin populations inhabit sunlit lowland rivers containing substantially larger vertebrate predators than those present in subterranean limestone caves.',
                'Replacing the surface fish’s <i>Pitx1</i> protein-coding sequence with the cave fish’s <i>Pitx1</i> protein-coding sequence causes surface-fish embryos to lose both their lower jaws and their pelvic fins.',
                'Pairing the cave fish’s <i>Pitx1</i> coding gene with the surface fish’s pelvic enhancer in cave-fish embryos restores pelvic-fin outgrowth without disrupting jaw formation.'
            ],
            'D',
            'Tư duy thí nghiệm hoán đổi gen chuẩn Evo-Devo (Rescue Experiment): Giả thuyết của Álvarez gồm 2 vế: (1) Vùng mã hóa protein <i>Pitx1</i> của cá hang VẪN HOẠT ĐỘNG BÌNH THƯỜNG; (2) Thứ bị mất là đoạn enhancer đặc hiệu cho vây bụng. Trong D, việc ghép CHÍNH gen mã hóa của cá hang với đoạn enhancer vây bụng của cá mặt nước đã khôi phục vây bụng bình thường (chứng minh protein cá hang không hề hỏng và đúng là thiếu enhancer vây bụng!) mà không làm hỏng hàm! Bẫy đảo chiều ở C sẽ CHỨNG MINH NGƯỢC LẠI (nếu thay vùng mã hóa cá hang làm mất hàm & vây thì vùng mã hóa cá hang bị hỏng!).',
            'Với câu hỏi tách bạch 2 cơ chế di truyền (coding region vs. regulatory enhancer), bằng chứng mạnh nhất luôn là thí nghiệm ghép chéo (chimeric rescue): giữ nguyên thành phần được cho là "vẫn tốt" + bù đúng thành phần được cho là "bị mất".',
            [
                ('Contradicts Premise', 'Bác bỏ giả định cốt lõi của bài rằng vô hiệu hóa vùng mã hóa <i>Pitx1</i> sẽ gây dị tật hàm chí tử.'),
                ('Irrelevant Ecological Context', 'Sự khác biệt về động vật ăn thịt giữa sông và hang không phân biệt được cơ chế đột biến vùng mã hóa hay vùng điều hòa.'),
                ('Inverted Mechanism (Weakens!)', 'Nếu vùng mã hóa của cá hang làm cá mặt nước mất cả hàm lẫn vây thì chứng tỏ chính protein của cá hang bị lỗi — bác bỏ trực tiếp Álvarez!'),
                ('Đáp án đúng', 'Thí nghiệm giải cứu ghép chéo hoàn hảo: dùng chính gen mã hóa của cá hang (chứng minh protein tốt) + bổ sung enhancer vây bụng của cá mặt nước → phục hồi vây mà giữ nguyên hàm.'),
            ]
        ),

        # Q8 — Cryospheric Geophysics / Permafrost Methane (CoE Quantitative [html_table] — Water-Table Confounder) [Key: C]
        q_item(
            'sat_boss_d1_q8', 8, D_II, S_QNT, 'Elite 750+',
            html_table(
                'Table 2. Summer Thaw Depth, Water-Table Position, and Methane Flux at Four Boreal Permafrost Sites',
                ['Site', 'Active-Layer Thaw Depth (cm)', 'Water Table vs. Surface (cm)', 'Subsurface CH₄ Production (mg/m²/day)', 'Net Surface CH₄ Emission (mg/m²/day)'],
                [
                    ['Alpha', '92', '−28 (dry upper soil)', '145', '12'],
                    ['Beta', '88', '−24 (dry upper soil)', '138', '15'],
                    ['Gamma', '64', '+4 (waterlogged)', '112', '104'],
                    ['Delta', '59', '+6 (waterlogged)', '105', '98'],
                ]
            ) + '<p>A simplified Arctic carbon model assumes that net atmospheric methane emission from thawing boreal permafrost increases steadily with active-layer thaw depth—the deeper the permafrost thaws each summer, the more methane escapes into the air. Biogeochemist Dr. Mikkel Nygaard challenges this model, contending that whenever the water table lies far beneath the ground surface, oxygen infiltrates the dry upper soil and sustains methane-oxidizing microbes that consume most subsurface methane before it can reach the atmosphere.</p>',
            'Which choice best describes data from the table that both refute the simplified model and support Nygaard’s explanation?',
            [
                'Sites Alpha and Beta thawed considerably deeper (92 and 88 cm) and generated substantially higher subsurface methane production (145 and 138 mg/m²/day) than waterlogged Sites Gamma and Delta (112 and 105 mg/m²/day).',
                'Between the two waterlogged boreal permafrost sites, Site Gamma thawed slightly deeper (64 cm vs. 59 cm) and emitted more net surface methane (104 vs. 98 mg/m²/day) than Site Delta did over the same summer.',
                'Despite thawing deeper (92 and 88 cm) and producing more subsurface CH₄ (145 and 138 mg/m²/day), dry-surfaced Sites Alpha and Beta (−28 and −24 cm water tables) emitted far less net CH₄ (12 and 15) than shallower waterlogged Sites Gamma and Delta (104 and 98).',
                'Sites Gamma and Delta maintained deeper subsurface water tables (+4 and +6 cm) than Sites Alpha and Beta (−28 and −24 cm), allowing oxygen to penetrate the upper soil layer and oxidize most subsurface methane.'
            ],
            'C',
            'Bẫy 2 cột na ná nhau cực hiểm: `Subsurface CH₄ Production` (sản sinh dưới sâu) vs. `Net Surface CH₄ Emission` (phát thải thực ra khí quyển)! Nếu nhìn nhầm sang cột Subsurface Production (như bẫy A), ta thấy tan càng sâu sản sinh càng nhiều (145/138 > 112/105) → tưởng mô hình đơn giản đúng! Nhưng cột mục tiêu là Net Surface Emission: Alpha & Beta tan sâu nhất (92, 88 cm) và sinh nhiều methane ngầm nhất, nhưng vì mực nước ngầm sâu (−28, −24 cm tạo lớp đất mặt khô giàu oxy cho vi khuẩn ăn methane) nên phát thải thực ra khí quyển chỉ còn 12 & 15 mg/m²/day — thấp hơn hẳn vùng ngập nước Gamma & Delta (104 & 98) dù tan nông hơn (64, 59 cm)! Chọn C!',
            'Trong bảng khoa học có 2 cột kết quả dễ nhầm (Production vs. Net Emission), luôn kiểm tra xem biến nhiễu (water table) có đang bẻ gãy mối quan hệ giữa biến đầu vào (thaw depth) và cột đầu ra cuối cùng hay không.',
            [
                ('Wrong Column Trap', 'Nhìn nhầm vào cột "Subsurface Production" thay vì "Net Surface Emission" — vô tình củng cố thay vì bác bỏ mô hình đơn giản!'),
                ('Cherry-Picked Subgroup', 'Chỉ so hai điểm ngập nước Gamma vs. Delta với nhau, nơi mực nước ngầm giống nhau nên tan sâu hơn vẫn phát thải nhiều hơn (không bác bỏ được mô hình).'),
                ('Đáp án đúng', 'Chốt đủ cả hai yêu cầu: bác bỏ quan hệ đồng biến độ sâu tan ↔ phát thải bề mặt, đồng thời chứng minh vai trò lọc methane của tầng đất mặt khô (mực nước −28/−24 cm).'),
                ('Reversed Sign / Misread Table', 'Đọc ngược hoàn toàn dấu âm/dương của mực nước ngầm: +4/+6 cm là ngập úng (waterlogged), không phải mực nước ngầm sâu giàu oxy.'),
            ]
        ),

        # Q9 — Chronobiology (Inferences with Polarity Flip "it is unlikely that ______") [Key: B]
        q_item(
            'sat_boss_d1_q9', 9, D_II, S_INF, 'Elite 750+',
            '<p>In mammalian retinas, non-visual entrainment of the central circadian clock relies primarily on intrinsically photosensitive retinal ganglion cells (ipRGCs) containing the photopigment melanopsin, which absorbs light strongly near 480 nanometers (blue-cyan) and shows negligible sensitivity above 620 nanometers (deep red). In a controlled sleep-laboratory trial, chronobiologist Dr. Ananya Raghavan exposed volunteers for two hours before midnight to 640-nanometer deep-red illumination bright enough to support full cone-mediated color vision, yet recorded neither melatonin suppression nor any shift in core-body-temperature rhythms relative to complete darkness. Because deep-red light activates visual cones robustly while bypassing melanopsin-expressing ipRGCs, Raghavan’s findings imply that it is unlikely that ______</p>',
            'Which choice most logically completes the text?',
            [
                'melanopsin-expressing retinal ganglion cells exhibit high photopigment sensitivity when human volunteers are exposed to short-wavelength blue-cyan light near 480 nanometers.',
                'cone-mediated visual activation alone suffices to shift human circadian melatonin and core-temperature rhythms without melanopsin stimulation.',
                'volunteers exposed to two hours of 640-nanometer deep-red illumination before midnight retained normal visual color perception without experiencing measurable melatonin suppression.',
                'visual cone photoreceptors in mammalian retinas are physiologically incapable of responding to any light wavelengths shorter than 620 nanometers during nighttime exposure.'
            ],
            'B',
            'CẢNH BÁO ĐẢO CỰC PHỦ ĐỊNH: Đọc thật chặt cụm **"imply that it is unlikely that ______"** (ngụ ý rằng KHÓ CÓ KHẢ NĂNG RẰNG...)! Chuỗi thí nghiệm: Ánh sáng đỏ sâu 640 nm kích hoạt ĐẦY ĐỦ tế bào nón thị giác (cones) nhưng bỏ qua melanopsin → kết quả là KHÔNG ức chế melatonin và KHÔNG dịch pha thân nhiệt (giống hệt bóng tối hoàn toàn). Do đó, điều KHÓ CÓ KHẢ NĂNG xảy ra là: chỉ riêng hoạt hóa tế bào nón thị giác đã đủ làm dịch chuyển đồng hồ sinh học khi thiếu kích thích melanopsin (B)! Cả A và C đều là bẫy Polarity Flip (nêu lại sự thật ĐÚNG của bài, ghép vào sau "it is unlikely that" thành tự phủ nhận chính thí nghiệm!).',
            'Gặp khung "it is unlikely that ______" hoặc "do not support the claim that ______", BẮT BUỘC ghép nguyên câu hoàn chỉnh đọc lại 1 lượt để loại bỏ tức thì mọi đáp án bị lộn dấu khẳng định/phủ định!',
            [
                ('Polarity Flip Trap!', 'Dữ kiện trong bài khẳng định ipRGCs hấp thụ mạnh ánh sáng 480 nm — ghép vào sau "it is unlikely that" sẽ trái ngược hoàn toàn với bài.'),
                ('Đáp án đúng', 'Khớp chính xác chiều phủ định: khi tế bào nón hoạt động đủ mà đồng hồ sinh học không dịch chuyển, khó có khả năng riêng tế bào nón đủ sức điều chỉnh nhịp sinh học nếu thiếu melanopsin.'),
                ('Polarity Flip Trap!', 'Đây chính là kết quả quan sát trực tiếp trong thí nghiệm của Raghavan — không thể nói nó "unlikely".'),
                ('Out of Scope / Unwarranted Claim', 'Đoạn văn chỉ nói melanopsin không nhạy trên 620 nm, không hề nói tế bào nón không hấp thụ được bước sóng ngắn hơn 620 nm.'),
            ]
        ),

        # Q10 — Solid-State Electrochemistry (CoE Textual — Stack-Pressure Confounder Control) [Key: A]
        q_item(
            'sat_boss_d1_q10', 10, D_II, S_TXT, 'Elite 750+',
            '<p>Solid-state lithium-metal batteries frequently fail when metallic lithium filaments (dendrites) pierce the ceramic electrolyte and cause an internal short circuit. Materials chemist Dr. Agnieszka Zielinski found that applying a nanometer-thin zinc-oxide coating to a garnet ceramic electrolyte doubled the critical current density before short-circuiting, which she attributed to a lithium-zinc alloy interlayer lowering interfacial electrical resistance. A peer reviewer noted, however, that Zielinski’s coated test cells were clamped at 5 megapascals (MPa) of mechanical stack pressure, whereas her uncoated control cells were clamped at only 0.5 MPa—raising the possibility that mechanical compression, rather than zinc-oxide chemistry, suppressed dendrite penetration.</p>',
            'Which follow-up experimental result, if obtained, would most effectively refute the peer reviewer’s alternative explanation and confirm Zielinski’s chemical mechanism?',
            [
                'When both coated and uncoated garnet cells are clamped at matched stack pressures—tested independently at both 0.5 MPa and 5 MPa—zinc-oxide-coated cells still double critical current density and exhibit substantially lower interfacial resistance than uncoated controls.',
                'Uncoated garnet ceramic electrolytes clamped at 5 MPa withstand significantly higher critical current densities before internal short-circuiting than identical uncoated garnet electrolytes clamped at only 0.5 MPa.',
                'Replacing the rigid garnet ceramic electrolyte with a flexible polymer-gel electrolyte eliminates metallic lithium dendrite short-circuiting at 0.5 MPa even in the complete absence of a zinc-oxide coating.',
                'Raising the mechanical clamping pressure on zinc-oxide-coated garnet ceramic cells from 5 MPa to 12 MPa fractures the ceramic separator mechanically before electrochemical cycling can even begin.'
            ],
            'A',
            'Bản đồ thiết kế thí nghiệm loại bỏ biến nhiễu (Confounder Isolation): Thí nghiệm ban đầu bị dính hai biến cùng lúc — lớp phủ ZnO VÀ áp suất kẹp (5 MPa vs. 0.5 MPa). Để vừa BÁC BỎ giả thuyết thay thế của phản biện (do áp suất kẹp) vừa XÁC NHẬN cơ chế hóa học của Zielinski (hợp kim giảm trở kháng bề mặt), thí nghiệm tiếp theo PHẢI cố định áp suất kẹp ngang bằng nhau giữa nhóm có phủ và không phủ (tại cả 0.5 MPa lẫn 5 MPa) và cho thấy lớp phủ ZnO vẫn tăng gấp đôi mật độ dòng tới hạn đồng thời giảm rõ rệt trở kháng bề mặt (A)!',
            'Khi thí nghiệm gốc bị trộn lẫn 2 biến độc lập (treatment + confounder), đáp án chuẩn 800 luôn giữ cố định confounder (matched controls) và kiểm tra xem treatment + cơ chế trung gian có còn duy trì hiệu ứng hay không.',
            [
                ('Đáp án đúng', 'Khóa chặt biến nhiễu áp suất kẹp (so cặp có phủ vs. không phủ ở cùng mức 0.5 MPa và cùng mức 5 MPa) và xác nhận đồng thời cả hiệu quả (gấp đôi dòng tới hạn) lẫn cơ chế (giảm trở kháng bề mặt).'),
                ('Supports Rival Explanation!', 'Nếu tăng áp suất kẹp từ 0.5 lên 5 MPa trên mẫu không phủ cũng tăng mạnh dòng tới hạn thì điều đó lại CỦNG CỐ nghi ngờ của người phản biện!'),
                ('Wrong Material System', 'Đổi sang chất điện phân polymer-gel hoàn toàn không kiểm chứng được cơ chế của lớp phủ ZnO trên gốm garnet.'),
                ('Irrelevant Upper Limit', 'Việc 12 MPa làm nứt gốm không giúp tách bạch ảnh hưởng của lớp phủ ZnO so với chênh lệch 5 MPa vs. 0.5 MPa.'),
            ]
        ),

        # Q11 — Marine Biogeochemistry (CoE Quantitative [svg_bar_chart] — Silicate/Plankton Confounder) [Key: C]
        q_item(
            'sat_boss_d1_q11', 11, D_II, S_QNT, 'Elite 750+',
            svg_bar_chart(
                'Share of Surface Bloom Carbon Reaching 1,000 m Depth (%) by Regime',
                ['0%', '10%', '20%', '30%', '40%'],
                [('Unfert. Ctrl', 14, '14%'), ('Fe+Flagell.', 6, '6%'), ('Fe+Thin Diat', 11, '11%'), ('Fe+Heavy Diat', 34, '34%')],
                40
            ) + '<p>Advocates of ocean iron fertilization contend that seeding iron-deficient Southern Ocean waters reliably locks atmospheric carbon in the deep ocean for centuries, citing satellite data showing that iron additions consistently triple surface phytoplankton chlorophyll across diverse sites. Oceanographer Dr. Miriam Al-Rashid counters that surface chlorophyll is an unreliable proxy for deep sequestration: unless dissolved silicate is also abundant enough to support heavily silicified diatoms whose dense shells sink rapidly, smaller flagellates and thinly silicified diatoms are grazed and respired in shallow water, causing a smaller proportion of bloom carbon to reach 1,000 meters than in unfertilized control waters.</p>',
            'Which choice best describes data from the graph that support Al-Rashid’s counterargument?',
            [
                'Iron-fertilized Southern Ocean patches dominated by heavily silicified diatoms exported 34% of surface bloom carbon to 1,000 meters, more than five times the 6% exported by flagellate-dominated patches.',
                'Unfertilized control waters exported the lowest percentage of surface bloom carbon to 1,000 meters (14%) among all four Southern Ocean plankton regimes plotted in the study.',
                'Only Fe+Heavy Diat patches (34%) exceeded the unfertilized control’s 1,000-meter carbon export (14%), whereas Fe+Flagell. (6%) and Fe+Thin Diat (11%) exported smaller shares than the control.',
                'Iron-fertilized patches dominated by tiny flagellates generated only 6% as much satellite-measured surface phytoplankton chlorophyll as patches dominated by heavily silicified diatoms.'
            ],
            'C',
            'Khóa 2 nhánh trong phản biện của Al-Rashid: [Nhánh 1] CHỈ khi đủ silicate cho tảo cát vỏ dày (`Fe+Heavy Diat`) thì tỉ lệ carbon chìm xuống 1.000 m mới cao hơn đối chứng không bón sắt (34% > 14%); [Nhánh 2] Nếu thiếu silicate để tảo roi (`Fe+Flagell.`: 6%) hoặc tảo cát vỏ mỏng (`Fe+Thin Diat`: 11%) chiếm ưu thế, tỉ lệ xuất carbon còn THẤP HƠN cả đối chứng không bón sắt (14%)! Duy nhất C đối chiếu đầy đủ cả 3 nhóm bón sắt với mốc đối chứng `Unfert. Ctrl (14%)`!',
            'Trong biểu đồ có cột Control, đáp án đúng cho luận điểm điều kiện ("unless X, performs worse than control") bắt buộc phải nêu rõ cả trường hợp vượt Control lẫn các trường hợp tụt dưới Control.',
            [
                ('Incomplete / Omits Control', 'Số liệu đúng nhưng chỉ so hai nhóm bón sắt (34% vs. 6%), bỏ qua mốc đối chứng 14% và nhóm tảo cát vỏ mỏng 11% nên chưa chứng minh luận điểm so với vùng không bón sắt.'),
                ('False Reading', 'Đọc sai biểu đồ: 14% của nhóm đối chứng CAO HƠN cả 6% và 11%, không phải thấp nhất.'),
                ('Đáp án đúng', 'Khớp hoàn toàn 2 nhánh của phản biện: chỉ Fe+Heavy Diat (34%) vượt Unfert. Ctrl (14%), còn Fe+Flagell. (6%) và Fe+Thin Diat (11%) đều tụt dưới mức đối chứng.'),
                ('Wrong Axis Variable', 'Biểu đồ đo % carbon chìm xuống độ sâu 1.000 m, KHÔNG đo lượng diệp lục bề mặt (surface chlorophyll — thứ mà bài nói tăng gấp ba ở mọi điểm bón sắt).'),
            ]
        ),

        # Q12 — Paleobotany (Inferences — Multi-Step Inverse-Sign Proxy Bias) [Key: D]
        q_item(
            'sat_boss_d1_q12', 12, D_II, S_INF, 'Elite 750+',
            '<p>Paleobotanists frequently estimate ancient atmospheric CO<sub>2</sub> concentrations from fossilized leaves by calculating the stomatal index—the ratio of gas-exchange pores (stomata) to total epidermal cells—because many woody plants decrease stomatal density as ambient CO<sub>2</sub> rises. However, controlled greenhouse trials with living relatives of Eocene laurel trees show that sunlit upper-canopy leaves develop roughly 35% higher stomatal indices than shaded understory leaves on the same tree grown under identical CO<sub>2</sub> levels. Moreover, storms preferentially shear off and carry tough, waxy upper-canopy sun leaves into river channels, where they enter the fossil record far more frequently than fragile shaded leaves. Consequently, paleobotanists who apply a calibration curve derived from mixed sun-and-shade modern foliage directly to riverbed fossil assemblages risk ______</p>',
            'Which choice most logically completes the text?',
            [
                'systematically overestimating ancient atmospheric CO<sub>2</sub> concentrations, because tough upper-canopy sun leaves exhibit stomatal indices roughly 35% higher than those of shaded understory leaves.',
                'reconstructing ancient atmospheric conditions from riverbed fossil assemblages dominated by fragile shaded understory leaves that push measured stomatal indices artificially downward.',
                'concluding erroneously that living relatives of Eocene laurel trees modify their epidermal stomatal indices exclusively in response to ambient CO<sub>2</sub> rather than canopy light exposure.',
                'systematically underestimating ancient CO<sub>2</sub> concentrations, because sun-leaf overrepresentation inflates fossil stomatal indices in a direction that mimics lower CO<sub>2</sub>.'
            ],
            'D',
            'BÀI TOÁN ĐẢO DẤU HAI TẦNG (Kẻ hủy diệt điểm 740→800!): Hãy viết sơ đồ mũi tên rõ ràng để tuyệt đối không lộn dấu: (1) Quy luật nghịch biến: `CO₂ ↑  ⇒  Stomatal Index ↓` (suy ngược lại: `Stomatal Index ↑  ⇒  mô hình suy ra CO₂ ↓`). (2) Thiên lệch bảo tồn: hóa thạch lòng sông chủ yếu là lá nắng trên tán (`sun leaves`), mà lá nắng có Stomatal Index CAO HƠN ~35% so với lá bóng râm. (3) Đưa mẫu hóa thạch có Stomatal Index bị ĐẨY CAO GIẢ TẠO vào đường chuẩn hỗn hợp ⇒ đường chuẩn sẽ đọc nhầm thành nồng độ CO₂ THẤP HƠN thực tế = **systematically underestimating** CO₂ (D)! Đáp án A là bẫy đảo dấu kinh điển nhất của bài!',
            'Mỗi khi gặp quan hệ tỷ lệ nghịch (A tăng → B giảm) kèm thiên lệch mẫu (preservation bias), BẮT BUỘC vẽ nháp 3 mũi tên (Bias → Metric ↑/↓ → Estimated Target ↓/↑) để khóa chặt chiều underestimate vs. overestimate!',
            [
                ('Sign-Flip Killer Trap!', 'Bẫy đảo chiều kinh điển: thấy lá nắng có stomatal index CAO HƠN 35% nên đoán nhầm thành "overestimating CO₂" — quên mất quan hệ NGƯỢC chiều (nhiều khí khổng tương ứng với CO₂ THẤP!).'),
                ('Reversed Preservation Bias', 'Ngược dữ kiện bài: bão cuốn và hóa thạch hóa ưu tiên lá nắng dai phủ sáp, không phải lá bóng râm mỏng manh.'),
                ('Direct Contradiction', 'Thí nghiệm nhà kính vừa chứng minh ánh sáng thay đổi stomatal index tới 35% dưới cùng mức CO₂.'),
                ('Đáp án đúng', 'Khớp tuyệt đối chuỗi mũi tên ngược chiều: thiên lệch lá nắng → chỉ số khí khổng bị đẩy cao giả tạo → mô hình hiểu nhầm là môi trường ít CO₂ → ước tính thấp hơn thực tế (underestimating).'),
            ]
        ),

        # Q13 — Virology / Evolutionary Medicine (CoE Textual — Weaken Evolutionary Trap) [Key: B]
        q_item(
            'sat_boss_d1_q13', 13, D_II, S_TXT, 'Hard',
            '<p>Multidrug-resistant strains of the bacterium <i>Pseudomonas aeruginosa</i> survive conventional antibiotics by overexpressing MexAB-OprM efflux pumps—membrane channels that actively expel drug molecules out of the cell. Evolutionary microbiologist Dr. Bassam Darwish isolated a bacteriophage (OMKO1) that binds specifically to the MexAB-OprM pump as its entry receptor to infect and lyse the bacterium. Darwish hypothesizes that combining OMKO1 with a standard antibiotic springs an evolutionary trade-off trap: bacterial mutants that delete or disable the efflux pump to evade viral infection inevitably forfeit their primary antibiotic-pumping defense, restoring drug susceptibility.</p>',
            'Which finding from a laboratory co-evolution assay, if true, would most directly weaken Darwish’s evolutionary-trap hypothesis?',
            [
                'Bacterial mutants that delete the <i>oprM</i> efflux-pump gene survive exposure to phage OMKO1 but are eliminated by antibiotic concentrations ten times lower than those required to inhibit the parent strain.',
                'Under dual treatment, <i>P. aeruginosa</i> rapidly evolves exterior binding-loop mutations on MexAB-OprM that block OMKO1 attachment while preserving full antibiotic-expelling capacity.',
                'Phage OMKO1 fails to infect or lyse unrelated Gram-positive bacteria such as <i>Staphylococcus aureus</i> whose outer membranes do not synthesize MexAB-OprM efflux pump channels.',
                'Exposing multidrug-resistant <i>P. aeruginosa</i> populations to the standard antibiotic alone, without phage OMKO1, consistently selects for surviving colonies exhibiting even higher MexAB-OprM expression.'
            ],
            'B',
            'Giải phẫu cơ chế bẫy tiến hóa (Evolutionary Trade-Off): Giả thuyết của Darwish dựa trên giả định ngầm rằng *cách duy nhất để vi khuẩn tránh được virus bám vào bơm là xóa hoặc phá hỏng chức năng bơm thuốc*. Để BÁC BỎ trực tiếp giả thuyết này, chỉ cần chỉ ra vi khuẩn có thể TÁCH RỜI hai chức năng đó: đột biến điểm trên vòng gắn bề mặt ngoài để chặn virus OMKO1 bám vào NHƯNG vẫn giữ nguyên 100% năng lực bơm đẩy kháng sinh (B)! Lúc đó bẫy đánh đổi bị vô hiệu hóa hoàn toàn!',
            'Trong câu hỏi Weaken giả thuyết "bắt buộc đánh đổi" (inevitable trade-off), đáp án đúng luôn chỉ ra một con đường tiến hóa/cơ chế giúp đối tượng đạt lợi ích A MÀ KHÔNG PHẢI hy sinh B.',
            [
                ('Inverted Logic (Strengthens!)', 'Xóa gen <i>oprM</i> giúp thoát virus nhưng nhạy cảm gấp 10 lần với kháng sinh → xác nhận 100% giả thuyết bẫy tiến hóa của Darwish!'),
                ('Đáp án đúng', 'Đột biến cục bộ ở vị trí bám bên ngoài chặn được virus mà giữ nguyên kênh đẩy kháng sinh → phá vỡ hoàn toàn thế đánh đổi bắt buộc.'),
                ('Expected Specificity (Irrelevant)', 'Virus đặc hiệu cho bơm MexAB-OprM không nhiễm được loài khác không có bơm này là điều hiển nhiên, không làm yếu giả thuyết trên <i>P. aeruginosa</i>.'),
                ('Single-Treatment Baseline Only', 'Thử nghiệm chỉ dùng kháng sinh đơn lẻ không hề kiểm chứng tương tác kép phage + kháng sinh.'),
            ]
        ),

        # Q14 — Immunology (CoE Quantitative [html_table] — Baseline-Titer Stratification Confounder) [Key: C]
        q_item(
            'sat_boss_d1_q14', 14, D_II, S_QNT, 'Elite 750+',
            html_table(
                'Table 3. Day-28 Influenza Vaccine Antibody Response by Baseline Immunity and Antibiotic Pretreatment',
                ['Volunteer Cohort', 'Pre-Vaccine Baseline Titer', 'Pretreatment Regimen', 'Day-28 Neutralizing Antibody Fold-Increase'],
                [
                    ['Cohort 1', 'High (≥1:160)', 'Placebo (No Abx)', '1.9×'],
                    ['Cohort 2', 'High (≥1:160)', '5-Day Broad-Spectrum Abx', '1.8×'],
                    ['Cohort 3', 'Low (<1:20)', 'Placebo (No Abx)', '11.4×'],
                    ['Cohort 4', 'Low (<1:20)', '5-Day Broad-Spectrum Abx', '2.3×'],
                ]
            ) + '<p>To test whether gut microbes serve as a natural immune adjuvant during seasonal influenza vaccination, researchers gave half of study volunteers a five-day course of broad-spectrum antibiotics (Abx) before immunization. Reviewing only Cohorts 1 and 2, a commentator concluded that depleting gut bacteria has virtually no effect on vaccine-induced antibody responses. Immunologist Dr. Mei-Fen Cheng argues that this sweeping conclusion overlooks a decisive interaction with pre-existing immunity: individuals with high baseline memory antibodies mount recall responses that bypass microbiome-dependent signaling, whereas low-baseline individuals depend heavily on intact gut microbes to generate a strong antibody surge.</p>',
            'Which choice best describes data from the table that directly support Cheng’s argument?',
            [
                'Both Cohort 1 (1.9×) and Cohort 2 (1.8×) started with high pre-vaccine baseline antibody titers of at least 1:160 and displayed modest Day-28 antibody fold-increases below 2.0×.',
                'Low-baseline volunteers pretreated with broad-spectrum antibiotics (Cohort 4, 2.3×) achieved a larger fold-increase than high-baseline placebo volunteers (Cohort 1, 1.9×), indicating that antibiotics enhanced immunity.',
                'Whereas antibiotic pretreatment barely changed Day-28 antibody fold-increase among high-baseline volunteers (1.8× vs. 1.9× with placebo), among low-baseline volunteers it slashed the fold-increase from 11.4× with placebo down to just 2.3×.',
                'Among immunologically naive low-baseline volunteers, those pretreated with five days of broad-spectrum antibiotics achieved an 11.4× antibody surge compared with only 2.3× in the matched placebo cohort.'
            ],
            'C',
            'Bản đồ tương tác 2×2 (Interaction Effect): Luận điểm của Cheng có 2 nhánh đối chiếu theo tầng miễn dịch nền (`High Baseline` vs. `Low Baseline`): [1] Nhóm nền CAO (Cohort 1 vs. 2): dùng kháng sinh gần như không đổi (1.8× vs. 1.9×); [2] Nhóm nền THẤP (Cohort 3 vs. 4): dùng kháng sinh đánh sập mức tăng kháng thể từ 11.4× xuống chỉ còn 2.3×! Chọn C! Chú ý bẫy so chéo tầng cực độc ở B: so Cohort 4 (2.3×, nền thấp + Abx) với Cohort 1 (1.9×, nền cao + placebo) rồi kết luận kháng sinh "tăng miễn dịch" — vi phạm nguyên tắc chỉ so trong cùng tầng baseline!',
            'Trong bảng thí nghiệm phân tầng 2×2, tuyệt đối KHÔNG so chéo hai nhóm khác tầng nền (cross-stratum comparison) — luôn so Treatment vs. Matched Placebo trong TỪNG tầng rồi đối chiếu mức chênh lệch giữa hai tầng!',
            [
                ('Incomplete / Repeats Commentator', 'Chỉ lặp lại số liệu của nhóm nền cao (Cohort 1 & 2) mà bỏ qua hoàn toàn cú sụt giảm 11.4× → 2.3× ở nhóm nền thấp.'),
                ('Cross-Stratum Confounder Trap!', 'Lỗi so chéo tầng nền cực hiểm: so nhóm nền thấp dùng kháng sinh (2.3×) với nhóm nền cao dùng giả dược (1.9×) thay vì so với đối chứng nền thấp (11.4×)!'),
                ('Đáp án đúng', 'Trình bày gọn và chính xác hiệu ứng tương tác ở cả hai tầng: gần như bất biến ở nền cao (1.8× vs. 1.9×) nhưng sụt giảm mạnh ở nền thấp (11.4× → 2.3×).'),
                ('Swapped Rows', 'Đảo ngược số liệu giữa Cohort 3 (Placebo = 11.4×) và Cohort 4 (Abx = 2.3×).'),
            ]
        ),

        # Q15 — Exoplanetary Geochemistry (Inferences — Observational Masking Bias & Negative Frame) [Key: A]
        q_item(
            'sat_boss_d1_q15', 15, D_II, S_INF, 'Elite 750+',
            '<p>Using transmission spectroscopy—which detects atmospheric gases by measuring faint dips in starlight filtered through an exoplanet’s upper atmosphere during transit—astronomers recorded unexpectedly flat, featureless water-vapor spectra on roughly half of surveyed warm sub-Neptune planets (equilibrium temperatures of 500–800 K). Early formation models interpreted these muted spectra as evidence that half of warm sub-Neptunes assembled inside dry, water-poor zones of their protoplanetary disks. Subsequent laboratory photochemistry experiments, however, revealed that methane-bearing gas mixtures irradiated by ultraviolet starlight at 500–800 K readily polymerize into opaque, high-altitude hydrocarbon hazes that prevent starlight from probing deeper atmospheric layers where water vapor resides. Therefore, flat transmission spectra alone do not establish that ______</p>',
            'Which choice most logically completes the text?',
            [
                'the surveyed warm sub-Neptunes with muted water-vapor signals genuinely lack water vapor or formed in dry disk zones.',
                'ultraviolet irradiation of methane-rich atmospheres at 500–800 K can generate opaque high-altitude hydrocarbon hazes capable of obstructing deeper starlight transmission.',
                'transmission spectroscopy relies on analyzing faint dips in starlight filtered through an exoplanet’s upper atmosphere as the planet transits its host star.',
                'warm sub-Neptune exoplanets across all orbital temperatures contain identical proportions of atmospheric methane and water vapor throughout their interiors.'
            ],
            'A',
            'Khóa khung phủ định: `"Therefore, flat transmission spectra alone do not establish that ______"` (Vì vậy, chỉ riêng quang phổ truyền qua phẳng KHÔNG chứng minh được rằng...). Cơ chế nhiễu quan sát (observational masking): Phổ phẳng có thể không phải do hành tinh thiếu nước mà chỉ vì lớp sương mù hydrocarbon quang hóa trên cao che khuất tia sáng sao không cho xuyên xuống tầng chứa hơi nước bên dưới! Do đó, phổ phẳng đơn lẻ không đủ để kết luận các hành tinh này thực sự thiếu nước hay hình thành ở vùng khô của đĩa tiền hành tinh (A)!',
            'Khi thí nghiệm mới đưa ra một cơ chế che khuất tín hiệu đo (masking/confounding mechanism), kết luận sau "alone do not establish that ______" luôn nhắm thẳng vào giả thuyết cũ từng diễn giải tín hiệu trống là sự vắng mặt thực sự (absence of evidence ≠ evidence of absence).',
            [
                ('Đáp án đúng', 'Khớp chính xác chiều phủ định "do not establish that": tín hiệu hơi nước phẳng có thể do sương mù che khuất nên không chứng minh được các hành tinh đó thực sự khô hay thiếu nước.'),
                ('Polarity Flip Trap!', 'Thí nghiệm quang hóa ĐÃ chứng minh cơ chế tạo sương mù che sáng này — ghép vào sau "do not establish that" thành phủ nhận ngược sự thật của bài!'),
                ('Polarity Flip / Definition Trap', 'Đó chính là định nghĩa kỹ thuật của quang phổ truyền qua ngay đầu đoạn văn.'),
                ('Extreme / Unstated Claim', 'Đoạn văn không hề đề cập hay đòi hỏi mọi hành tinh ở mọi nhiệt độ đều có tỷ lệ methane/nước giống hệt nhau.'),
            ]
        ),
    ]

    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': BOSS_DRILL_1_TITLE,
            'subtitle': '15 câu thuần Hard M2 (Q11–Q15, trình độ 750–800): lập bản đồ đa biến khoa học, nhận diện biến nhiễu (confounders), đối chứng giả dược/phân tầng và suy luận thí nghiệm đảo dấu.',
            'difficultyBadge': 'Hard M2 Boss • 750–800',
            'targetTimeMinutes': 22,
        },
        'drillModule': {
            'id': 'boss_drill_1_mod',
            'title': 'Boss Drill 1: Dense Science Logic & Multi-Variable Mapping',
            'timeLimitMinutes': 22,
            'questions': questions,
        },
    }


# ============================================================================
# BOSS DRILL 2: 50/50 TRAP ELIMINATION — 1-MILLIMETER RULE (15 Qs)
# Answer key balance: A=4 (Q2,Q6,Q9,Q13), B=4 (Q4,Q7,Q11,Q15), C=4 (Q1,Q5,Q10,Q14), D=3 (Q3,Q8,Q12)
# ============================================================================

def get_boss_drill_2():
    D_CS = 'Craft and Structure'
    D_II = 'Information and Ideas'
    S_WIC = 'Words in Context'
    S_TSP = 'Text Structure and Purpose'
    S_CID = 'Central Ideas and Details'
    S_INF = 'Inferences'

    questions = [
        # Q1 — Words in Context: arrest vs. restrain (Collocation Mismatch) [Key: C]
        q_item(
            'sat_boss_d2_q1', 1, D_CS, S_WIC, 'Elite 750+',
            '<p>Conservators treating waterlogged seventeenth-century oak timbers salvaged from a Baltic shipwreck must intervene swiftly once the wood meets open air: as trapped water evaporates, weakened cellulose cell walls begin to collapse irreversibly within days. By impregnating the beams with polyethylene glycol wax prior to controlled freeze-drying, specialists can ______ this structural collapse, preserving the hull’s original curvature for museum display.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            [
                'remedy',
                'restrain',
                'arrest',
                'exacerbate'
            ],
            'C',
            'Cặp 50/50 sinh tử: **arrest (C)** vs. **restrain (B)** (và **remedy (A)**). Học sinh 1400 thường bỏ qua `arrest` vì chỉ nhớ nghĩa phổ thông "bắt giữ tội phạm", rồi chọn nhầm `restrain` hoặc `remedy`. Tuy nhiên trong văn học thuật chuẩn SAT, **arrest** mang nghĩa thứ cấp cực kỳ chính xác là *chặn đứng / làm ngưng hẳn một tiến trình suy thoái vật lý hay sinh học* ("arrest structural collapse", "arrest decay"). `restrain` sập bẫy **1mm Collocation Mismatch** (chỉ đi với con người, cảm xúc, tốc độ tăng chi tiêu — không dùng "restrain collapse"), còn `remedy` sai thời điểm vì sự sụp đổ là *irreversible* (không thể sửa sau khi đã xảy ra).',
            'Quy tắc 1mm cho Words in Context 750+: luôn nhớ nghĩa học thuật thứ cấp của động từ quen thuộc (`arrest` = halt a process) và kiểm tra chặt collocation với danh từ mục tiêu ("arrest collapse", KHÔNG dùng "restrain collapse").',
            [
                ('Temporal / Logic Mismatch', 'remedy = khắc phục/chữa lành hậu quả đã xảy ra; nhưng bài nói rõ sự sụp đổ tế bào gỗ là "irreversible" (không thể đảo ngược) nên phải chặn đứng trước khi hoàn tất, không phải chữa sau đó.'),
                ('50/50 Trap (1mm): Collocation Mismatch', 'Bẫy 50/50 cực gắt! "restrain" (kiềm chế/giữ lại) mang hướng nghĩa gần đúng nhưng sai sắc thái kết hợp từ (collocation) — trong tiếng Anh học thuật không dùng "restrain structural collapse".'),
                ('Đáp án đúng', 'Nghĩa học thuật thứ cấp chuẩn xác: arrest = chặn đứng hoàn toàn một tiến trình suy thoái vật lý ("arrest structural collapse"), khớp tuyệt đối ngữ cảnh bảo tồn.'),
                ('Opposite Meaning', 'exacerbate = làm trầm trọng thêm — ngược hoàn toàn với mục đích "preserving the hull’s original curvature".'),
            ]
        ),

        # Q2 — Central Ideas and Details: Ottoman Guilds (50/50 Trap: Unstated Comparison) [Key: A]
        q_item(
            'sat_boss_d2_q2', 2, D_II, S_CID, 'Hard',
            '<p>Economic historian Dr. Defne Demirci examined seventeenth-century Ottoman court registers from Bursa documenting official price ceilings (<i>narh</i>) negotiated between municipal judges and silk-weaving guilds. Rather than reflecting unilateral edicts imposed from above by imperial bureaucrats, the registers record protracted hearings in which guild masters submitted raw-silk invoices, dye costs, and loom-maintenance ledgers to justify seasonal price revisions. Judges frequently adjusted official ceilings upward when supply bottlenecks raised input costs, reserving fines primarily for merchants who secretly adulterated thread weight while charging the regulated rate.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Seventeenth-century court registers from Bursa indicate that Ottoman municipal silk price ceilings were established through evidence-based negotiations between guild masters and judges rather than rigid unilateral edicts.',
                'Seventeenth-century Ottoman municipal judges in Bursa regulated seasonal silk prices far more flexibly and equitably than did judicial authorities in contemporary European guild cities.',
                'Bursa’s silk-weaving guilds exercised total unilateral authority over municipal courts and were never fined by Ottoman judges for violating local commercial regulations.',
                'The primary reason Ottoman authorities preserved seventeenth-century court registers in Bursa was to prosecute merchants who secretly adulterated the weight of regulated silk thread.'
            ],
            'A',
            'Cặp 50/50: **A** vs. **B**. Đáp án B nghe vô cùng mượt mà và mang sắc thái tích cực y hệt đoạn văn, nhưng sập bẫy **1mm Unstated Comparison**: đoạn văn KHÔNG HỀ nhắc tới "contemporary European guild cities" nên mọi phép so sánh hơn ("far more flexibly and equitably than...") đều sai lập tức! Đáp án A bám chặt trục đối lập trung tâm ("Rather than reflecting unilateral edicts... record protracted hearings in which guild masters submitted... ledgers").',
            'Quy tắc 1mm cho phép so sánh: thấy `more ... than`, `less ... than`, `superior to` trong đáp án → dừng lại kiểm tra xem đối tượng thứ hai có thực sự được so sánh trong đoạn văn hay không!',
            [
                ('Đáp án đúng', 'Tóm gọn chính xác ý chính: trần giá tơ lụa ở Bursa được ấn định qua thương lượng dựa trên hóa đơn/sổ sách giữa phường hội và thẩm phán chứ không phải sắc lệnh đơn phương áp đặt từ trên xuống.'),
                ('50/50 Trap (1mm): Unstated Comparison', 'Bẫy 50/50 chết người! Đúng tinh thần linh hoạt của thẩm phán Ottoman nhưng tự bịa ra phép so sánh với "contemporary European guild cities" — đối tượng không hề xuất hiện trong bài!'),
                ('1-Word Extremity', 'Từ cực đoan "total unilateral authority" và "never fined" mâu thuẫn trực tiếp với câu cuối ("reserving fines primarily for merchants who secretly adulterated thread weight").'),
                ('Scope Creep / Minor Detail', 'Nâng chi tiết xử phạt ở cuối bài thành "mục đích chính" khiến chính quyền Ottoman lưu giữ sổ tòa án.'),
            ]
        ),

        # Q3 — Text Structure and Purpose: Kora Polyrhythm (50/50 Trap: Wrong Rhetorical Function) [Key: D]
        q_item(
            'sat_boss_d2_q3', 3, D_CS, S_TSP, 'Elite 750+',
            '<p>Ethnomusicologists analyzing the 21-string West African <i>kora</i> note that master players routinely sustain two seemingly independent rhythms simultaneously—a steady four-beat bass ostinato in the thumbs interlocked with a three-against-two treble melody in the index fingers. <u>This rhythmic divergence does not mean that players conceptualize the two parts as separate, competing time signatures; rather, musicians report perceiving a single unified composite pattern in which each pluck locks into a shared pulse grid.</u> Cognitive studies using motion-capture sensors corroborate these accounts, showing that a player’s thumbs and index fingers adjust timing in tight mutual synchrony whenever tempo shifts.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It argues that motion-capture sensor recordings provide a far more reliable account of <i>kora</i> rhythmic timing than master musicians’ own descriptions do.',
                'It explains the physical hand anatomy that enables master <i>kora</i> players to shift tempo independently between their thumbs and their index fingers.',
                'It concedes a methodological flaw in ethnomusicologists’ opening characterization of <i>kora</i> rhythm before introducing motion-capture data to settle the dispute.',
                'It clarifies how <i>kora</i> players mentally unify the instrument’s layered rhythms, preempting a misinterpretation of the opening sentence.'
            ],
            'D',
            'Cặp 50/50: **D** vs. **C**. Học sinh hay nhìn thấy cụm "does not mean... rather..." rồi vội dán nhãn là "concedes a methodological flaw / dispute" (như bẫy C). Soi sát 1mm ở câu mở đầu: câu đầu đã dùng từ rào đón cực chuẩn **"seemingly independent rhythms"** (có vẻ độc lập), tức là các nhà dân tộc nhạc học KHÔNG hề mắc lỗi hay tranh cãi! Câu gạch chân đóng vai trò làm rõ mô hình nhận thức bên trong đầu nghệ sĩ (một mạng nhịp hợp nhất) để NGĂN NGỪA hiểu nhầm từ chữ "seemingly independent" (D)!',
            'Phân biệt sắc thái tu từ 1mm: `preempts a misinterpretation` (rào trước tránh hiểu sai một mô tả cẩn trọng như "seemingly") ≠ `concedes a flaw / settles a dispute` (thừa nhận sai sót hoặc tranh chấp giữa hai phe).',
            [
                ('Reversed Relationship', 'Câu cuối nói cảm biến chuyển động CỦNG CỐ (corroborate) lời kể của nghệ sĩ, không hề đặt cảm biến ở thế đáng tin cậy hơn lời kể.'),
                ('Direct Contradiction', 'Ngón cái và ngón trỏ điều chỉnh trong sự đồng bộ chặt chẽ (tight mutual synchrony), không dịch chuyển nhịp độc lập.'),
                ('50/50 Trap (1mm): Wrong Rhetorical Function', 'Bẫy 50/50 rất dễ dính! Câu đầu đã cẩn thận dùng từ "seemingly independent", nên câu gạch chân KHÔNG thừa nhận lỗi phương pháp hay giải quyết tranh chấp nào của nhà nghiên cứu — nó chỉ giải thích để người đọc không hiểu nhầm.'),
                ('Đáp án đúng', 'Xác định chuẩn xác vai trò tu từ: làm rõ cách nghệ sĩ kora hình dung nhịp điệu như một khung thống nhất, rào trước hiểu nhầm tiềm ẩn từ câu mở đầu.'),
            ]
        ),

        # Q4 — Words in Context: qualify vs. repudiate (50/50 Trap: 1-Word Extremity) [Key: B]
        q_item(
            'sat_boss_d2_q4', 4, D_CS, S_WIC, 'Elite 750+',
            '<p>In her influential 1984 monograph, sociologist Dr. Judith Caldwell argued that rising suburban homeownership inevitably erodes civic participation across metropolitan regions. Two decades later, after analyzing county-level volunteerism records from Phoenix and Minneapolis, Caldwell did not abandon her overarching thesis, but she did ______ it—acknowledging that neighborhoods built around shared transit hubs and walkable plazas sustained robust civic engagement even at high homeownership rates.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            [
                'repudiate',
                'qualify',
                'substantiate',
                'obscure'
            ],
            'B',
            'Cặp 50/50: **qualify (B)** vs. **repudiate (A)**. Học sinh 1400 thường loại ngay `qualify` vì chỉ nghĩ đến nghĩa "đủ tư cách/đạt chuẩn", rồi nhảy vào `repudiate` vì thấy từ chuyển hướng "but". Nhưng soi 1mm ngay trước chỗ trống: **"Caldwell did not abandon her overarching thesis, but she did ______ it"**! `repudiate` = *bác bỏ hoàn toàn / phủ nhận sạch trơn*, mâu thuẫn 100% với "did not abandon" (bẫy **1-Word Extremity**)! Trong tiếng Anh học thuật, **qualify** mang nghĩa thứ cấp cực đắt là *giới hạn lại / điều chỉnh sắc thái bớt cực đoan cho một luận điểm* — khớp tuyệt đối với việc vẫn giữ luận điểm chính nhưng thừa nhận ngoại lệ cụ thể!',
            'Khóa cặp từ vựng sát thủ 750+: khi tác giả "không từ bỏ hoàn toàn luận điểm nhưng thêm điều kiện/ngoại lệ", động từ đúng luôn là `qualify` / `temper` / `nuance` — TUYỆT ĐỐI loại các động từ xóa sổ 100% như `repudiate` / `refute` / `renounce`!',
            [
                ('50/50 Trap (1mm): 1-Word Extremity', 'Bẫy 50/50 cực mạnh! "repudiate" = phủ nhận hoàn toàn, đi quá đà so với rào chắn "did not abandon her overarching thesis".'),
                ('Đáp án đúng', 'Nghĩa học thuật thứ cấp: qualify = đặt điều kiện giới hạn / làm mềm bớt tính tuyệt đối ("inevitably") của luận điểm ban đầu mà không bác bỏ toàn bộ nó.'),
                ('Opposite Meaning', 'substantiate = chứng minh/củng cố thêm — ngược hướng với từ nối "but" và bằng chứng ngoại lệ ở Phoenix & Minneapolis.'),
                ('Wrong Meaning', 'obscure = làm mờ mịt/che giấu — trong khi Caldwell làm rõ phạm vi áp dụng của luận điểm.'),
            ]
        ),

        # Q5 — Inferences: Protected Manufacturing Zones (50/50 Trap: Reverse Causality) [Key: C]
        q_item(
            'sat_boss_d2_q5', 5, D_II, S_INF, 'Elite 750+',
            '<p>To protect blue-collar industrial jobs, several North American municipalities created "protected manufacturing zones" that bar landlords from converting historic brick warehouses into residential apartments while still allowing light assembly, food processing, and artisan workshops. Yet urban geographer Dr. Efua Quartey found that within a decade of designation, small metalworking and fabrication firms in protected zones still declined by nearly 40%—not because residential developers outbid them, but because warehouse owners raised rents steeply to attract boutique creative studios, design showrooms, and specialty coffee roasters that legally qualified under broad "light-production" zoning definitions. These findings suggest that ______</p>',
            'Which choice most logically completes the text?',
            [
                'the departure of nearly 40% of small metalworking and fabrication firms forced warehouse owners to reduce industrial rents and lobby cities to reclassify creative agencies as light producers.',
                'protected manufacturing zones failed to retain small fabricators primarily because municipal zoning inspectors neglected to enforce legal prohibitions against converting brick warehouses into apartments.',
                'prohibiting residential conversions alone is insufficient to preserve affordable industrial rents for traditional small manufacturers when broad zoning categories allow higher-paying commercial tenants to compete for the same warehouses.',
                'boutique creative studios, design showrooms, and specialty coffee roasters generate substantially greater municipal tax revenue per square meter than residential apartment conversions do.'
            ],
            'C',
            'Cặp 50/50: **C** vs. **A**. Sơ đồ nhân quả gốc: [Định nghĩa quy hoạch "light-production" quá rộng] → [Chủ kho tăng giá thuê hút studio thiết kế & rang xay cà phê trả giá cao] → [Xưởng gia công nhỏ bị đẩy ra ngoài giảm 40%]. Đáp án A dùng chính xác toàn bộ từ khóa của bài nhưng sập bẫy **1mm Reverse Causality** (đảo ngược nguyên nhân–kết quả: nói xưởng nhỏ rời đi *ép* chủ kho hạ giá thuê và vận động đổi luật)! Chỉ C giữ đúng chiều nhân quả và tóm gọn kết luận chính sách chuẩn 1mm.',
            'Khi gặp hai đáp án chứa cùng bộ từ khóa (40%, landlords, rents, creative studios), hãy vẽ mũi tên `Nguyên nhân → Hệ quả` ngay trên hai đáp án để bắt gọn bẫy Reverse Causality trong 5 giây!',
            [
                ('50/50 Trap (1mm): Reverse Causality', 'Bẫy 50/50 đảo chiều nhân quả! Chủ kho TĂNG giá thuê cho nhóm khách thương mại cao cấp khiến xưởng nhỏ rời đi — KHÔNG phải xưởng nhỏ rời đi ép chủ kho hạ giá thuê.'),
                ('Explicitly Negated Cause', 'Đoạn văn loại trừ trực tiếp nguyên nhân này: "not because residential developers outbid them".'),
                ('Đáp án đúng', 'Khớp nguyên vẹn chuỗi nhân quả: chỉ cấm chuyển đổi sang nhà ở là chưa đủ khi kẽ hở định nghĩa quy hoạch vẫn cho phép khách thương mại trả giá cao tranh thuê cùng mặt bằng.'),
                ('Unstated Comparison', 'Bài hoàn toàn không so sánh doanh thu thuế thành phố giữa studio/quán rang xay và chung cư.'),
            ]
        ),

        # Q6 — Text Structure and Purpose: Botanical Lithography (50/50 Trap: Scope Creep) [Key: A]
        q_item(
            'sat_boss_d2_q6', 6, D_CS, S_TSP, 'Hard',
            '<p>Before chromolithography became widely affordable in the 1850s, European botanical atlases relied on hand-colored copperplate engravings whose petal hues varied subtly from copy to copy, frustrating field naturalists who needed exact coloration to separate closely related alpine species. When German botanical draftsman Ernst Gmelin began printing standardized mineral-pigment swatch tables alongside his lithographic plates, publishers initially balked at the extra paper cost. Within a decade, however, herbaria from Vienna to Edinburgh had adopted Gmelin’s color-reference grids as a diagnostic benchmark, turning printed botanical plates from inconsistent luxury artworks into reproducible scientific instruments.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To explain how a printing innovation turned botanical illustrations into reliable tools for scientific identification.',
                'To analyze the chemical composition of the mineral pigments Ernst Gmelin formulated for nineteenth-century color swatch tables.',
                'To show why nineteenth-century herbaria in Vienna and Edinburgh initially rejected chromolithography because of its elevated paper costs.',
                'To trace the commercial rivalry between German chromolithography workshops and traditional copperplate engraving guilds across nineteenth-century Europe.'
            ],
            'A',
            'Cặp 50/50: **A** vs. **D**. Đáp án D nghe rất "sử học" và chứa hàng loạt từ khóa có mặt trong bài ("German", "chromolithography", "copperplate", "Europe"), nhưng sập bẫy **1mm Scope Creep / Wrong Focus**: bài KHÔNG hề kể về cuộc cạnh tranh thương mại giữa các xưởng in đá và phường hội khắc đồng (chỉ có 1 chi tiết nhỏ là nhà xuất bản ban đầu ngại tốn thêm giấy). Mục đích bao trùm từ câu đầu đến câu kết là giải thích cách sáng kiến bảng màu chuẩn hóa của Gmelin biến tranh thực vật thành công cụ khoa học tái lập được (A)!',
            'Kiểm tra Main Purpose bằng bài test Câu Đầu + Câu Kết: câu đầu nêu vấn đề (tranh khắc đồng lệch màu gây khó cho định danh loài), câu kết nêu chuyển hóa (trở thành công cụ khoa học tái lập) ⇒ Main Purpose phải phủ đúng trục Vấn đề → Chuyển hóa này!',
            [
                ('Đáp án đúng', 'Bao quát hoàn hảo cung logic toàn bài: từ bất cập lệch màu ở bản khắc đồng → sáng kiến bảng đối chiếu màu in kèm bản in đá → biến tranh thành công cụ định danh khoa học chuẩn xác.'),
                ('Out of Scope Detail', 'Bài chỉ nhắc tên "mineral-pigment swatch tables", hoàn toàn không mô tả thành phần hóa học của sắc tố.'),
                ('Swapped Actor (Misread)', 'Chính các nhà xuất bản (publishers) ban đầu ngại chi phí giấy, còn các bảo tàng mẫu thực vật (herbaria) ở Vienna và Edinburgh lại ĐÓN NHẬN nó làm chuẩn mực.'),
                ('50/50 Trap (1mm): Scope Creep', 'Bẫy 50/50 mở rộng lệch trọng tâm! Bài không hề bàn về "commercial rivalry" giữa các xưởng in và phường hội khắc đồng; trọng tâm là giá trị khoa học của sáng kiến bảng màu.'),
            ]
        ),

        # Q7 — Central Ideas and Details: Retired Surveyor Fiction (50/50 Trap: 1-Word Extremity) [Key: B]
        q_item(
            'sat_boss_d2_q7', 7, D_II, S_CID, 'Hard',
            '<p><i>The following text is adapted from an original fictional novel set in 1911. Arthur, a retired municipal surveyor, is examining a newly printed street map of the harbor district he had charted forty years earlier.</i><br/>Arthur traced the crisp ink lines along the eastern wharves, where his own chain-and-transit benchmarks still governed the curve of the breakwater. Yet just inland, rows of timber cooperages he had measured with such scrupulous patience had vanished beneath a broad railway viaduct stamped in bold black type. He folded the map neatly along its linen creases—not resentful of the engineers who had superseded his streets, only struck by how effortlessly steel and masonry erased the labor of men who had once sworn their boundaries permanent.</p>',
            'Which choice best describes Arthur’s reaction while examining the new harbor map?',
            [
                'He feels bitter resentment toward the younger railway engineers for demolishing the historic timber cooperages he had spent years measuring so carefully.',
                'He recognizes enduring traces of his past surveying work along the breakwater while quietly reflecting on the impermanence of the urban landscape he once charted.',
                'He identifies several technical surveying inaccuracies in the newly printed map’s depiction of the eastern breakwater and adjacent harbor wharves.',
                'He resolves to return to municipal service in order to update the district’s older boundary records and preserve the remaining timber wharves.'
            ],
            'B',
            'Cặp 50/50: **B** vs. **A**. Trong văn học SAT, những từ như *vanished*, *erased*, *superseded* dễ đánh lừa học sinh 1400 chọn cảm xúc mạnh như "bitter resentment" (A). Nhưng soi kỹ 1mm sau dấu gạch ngang: **"—not resentful of the engineers who had superseded his streets, only struck by..."**! Tác giả phủ định thẳng thừng sự oán giận, thay bằng tâm trạng trầm lắng nhận ra vừa có dấu ấn còn lưu lại (đê chắn sóng vẫn theo mốc đo của ông) vừa có sự vô thường của công trình đô thị (B)!',
            'Trong đoạn văn tiểu thuyết, cảm xúc nhân vật trên Hard M2 gần như luôn mang sắc thái tinh tế, phức hợp (ambivalent / reflective) — đặc biệt cảnh giác những cụm phủ định nằm gọn sau dấu gạch ngang như "not resentful... only struck by..."!',
            [
                ('50/50 Trap (1mm): 1-Word Extremity', 'Bẫy 50/50 cực gắt! Văn bản phủ định trực diện thái độ này bằng cụm "not resentful of the engineers", biến "bitter resentment" thành sai 100%.'),
                ('Đáp án đúng', 'Bắt trọn hai lớp cảm xúc đan xen: nhận ra dấu ấn bền bỉ của mình ("benchmarks still governed the curve") và chiêm nghiệm lặng lẽ về sự hữu hạn ("effortlessly... erased").'),
                ('Reversed Detail', 'Không hề có lỗi đo đạc nào ở đê chắn sóng phía đông — đường nét đó vẫn tuân theo chính mốc chuẩn của Arthur.'),
                ('Out of Scope / Unstated Action', 'Ông chỉ gấp gọn tấm bản đồ lại, không có ý định quay lại làm việc hay bảo tồn bến gỗ.'),
            ]
        ),

        # Q8 — Words in Context: discount vs. refute (50/50 Trap: 1-Word Extremity / Proof vs. Dismissal) [Key: D]
        q_item(
            'sat_boss_d2_q8', 8, D_CS, S_WIC, 'Elite 750+',
            '<p>For decades, many maritime archaeologists tended to ______ oral navigational traditions preserved by Polynesian wayfinders, assuming that unwritten star-compass itineraries could not transmit accurate multi-century sailing routes. Yet computer drift simulations combined with experimental voyages aboard the double-hulled canoe <i>Hōkūleʻa</i> eventually demonstrated that those memorized swell and star bearings reliably guided open-ocean landfalls across thousands of kilometers.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            [
                'refute',
                'codify',
                'corroborate',
                'discount'
            ],
            'D',
            'Cặp 50/50 kinh điển nhất mức 750→800: **discount (D)** vs. **refute (A)**! Cả hai đều mang thái độ bác bỏ/không tin, nhưng cách nhau đúng 1 milimét chí mạng về logic: **refute** đòi hỏi *chứng minh bằng chứng xác thực rằng một điều là SAI* — trong khi các nhà khảo cổ chỉ *giả định* ("assuming") chứ chưa hề chứng minh nó sai (thậm chí sau này còn được chứng minh là ĐÚNG, nên họ chưa bao giờ "refute" được nó!). Ngược lại, nghĩa thứ cấp học thuật của **discount** là *coi nhẹ / gạt bỏ không thèm tính đến* — khớp 100% với "assuming that... could not"!',
            'Khắc cốt ghi tâm cặp 1mm `discount` vs. `refute`: bạn chỉ có thể `refute` điều SAI bằng bằng chứng thực tế; còn nếu chỉ nghi ngờ, xem nhẹ hoặc gạt sang một bên một điều thực ra đúng thì PHẢI dùng `discount` / `dismiss`!',
            [
                ('50/50 Trap (1mm): 1-Word Extremity', 'Bẫy 50/50 đỉnh cao! "refute" = chứng minh là sai bằng bằng chứng; nhưng các nhà khảo cổ chỉ võ đoán ("assuming") và thực tế các hải trình truyền khẩu ấy hoàn toàn CHÍNH XÁC nên không thể bị "refute"!'),
                ('Wrong Meaning', 'codify = hệ thống hóa thành bộ luật/văn bản — không hợp ngữ cảnh xem nhẹ truyền thống truyền khẩu.'),
                ('Opposite Meaning', 'corroborate = xác nhận bằng bằng chứng — đây là điều tàu Hōkūleʻa làm về sau, ngược với thái độ hoài nghi ban đầu.'),
                ('Đáp án đúng', 'Nghĩa học thuật thứ cấp: discount = xem nhẹ / gạt bỏ không coi trọng độ tin cậy, khớp chính xác với mệnh đề "assuming that unwritten star-compass itineraries could not...".'),
            ]
        ),

        # Q9 — Central Ideas and Details: Choice Overload (50/50 Trap: Reverse Causality) [Key: A]
        q_item(
            'sat_boss_d2_q9', 9, D_II, S_CID, 'Hard',
            '<p>In an analysis of employer-sponsored retirement plans across 647 companies, behavioral economists uncovered a striking inverse relationship: for every ten additional mutual-fund options added to a workplace menu, employee participation rates fell by nearly two percentage points. Rather than reflecting contentment with outside personal savings accounts, exit surveys revealed that employees confronted with fifty or more overlapping funds frequently postponed enrollment altogether because they feared selecting an inferior portfolio and lacked an intuitive benchmark for comparing fee structures.</p>',
            'According to the text, why did expanding the number of mutual-fund options lower employee participation in workplace retirement plans?',
            [
                'Facing dozens of overlapping funds without an easy way to compare fees led many workers to delay enrolling out of fear of choosing poorly.',
                'Workers offered expanded retirement menus already held adequate savings in outside personal accounts and therefore saw little practical reason to enroll.',
                'Persistently low employee participation prompted companies across the study to expand fund menus with dozens of overlapping choices in hopes of simplifying fee comparisons.',
                'Workplace retirement plans containing fewer than ten mutual-fund options are legally prohibited from including funds that carry complex fee structures.'
            ],
            'A',
            'Cặp 50/50: **A** vs. **C**. Đoạn văn xác lập rõ chiều nguyên nhân–kết quả: thêm lựa chọn quỹ (Nguyên nhân) → nhân viên choáng ngợp trước 50+ quỹ trùng lặp, sợ chọn nhầm và khó so sánh phí → trì hoãn đăng ký (Hệ quả, đáp án A). Bẫy C mắc lỗi **1mm Reverse Causality**: đảo ngược thành "tỷ lệ tham gia thấp khiến công ty thêm hàng chục quỹ để đơn giản hóa so sánh phí" — vừa ngược chiều nhân quả vừa vô lý về cơ chế!',
            'Với câu hỏi "According to the text, why did X cause Y?", luôn kiểm tra chiều mũi tên trong đáp án (X gây ra Y, không phải Y thúc đẩy X) và loại ngay các nguyên nhân bị phủ định bởi cụm "Rather than...".',
            [
                ('Đáp án đúng', 'Diễn giải trung thành tuyệt đối câu cuối: đối mặt quá nhiều quỹ chồng chéo mà thiếu mốc so sánh phí khiến nhân viên lo chọn sai và trì hoãn tham gia.'),
                ('Explicitly Negated Trap', 'Đoạn văn loại trừ trực tiếp bằng cụm "Rather than reflecting contentment with outside personal savings accounts".'),
                ('50/50 Trap (1mm): Reverse Causality', 'Bẫy 50/50 đảo ngược nhân quả! Việc mở rộng danh mục quỹ làm giảm tỷ lệ tham gia — KHÔNG phải tỷ lệ tham gia thấp khiến chủ lao động thêm quỹ.'),
                ('Out of Scope / Fabricated Rule', 'Văn bản không hề nhắc đến quy định pháp luật nào cấm quỹ có cấu trúc phí phức tạp.'),
            ]
        ),

        # Q10 — Text Structure and Purpose: Icelandic Sagas (50/50 Trap: 1-Word Extremity) [Key: C]
        q_item(
            'sat_boss_d2_q10', 10, D_CS, S_TSP, 'Elite 750+',
            '<p>Literary historians long divided medieval Icelandic sagas into two mutually exclusive camps: "bookprose" scholars insisted the narratives were original written inventions by thirteenth-century authors, whereas "freeprose" scholars contended that scribes merely transcribed fixed oral stories preserved verbatim from the Viking Age. <u>Recent stylistic comparisons of manuscript variants, however, show that medieval scribes actively reshaped dialogue and compressed genealogies even while drawing on shared oral episodes, blurring any sharp boundary between solitary authorship and collective oral tradition.</u> Consequently, contemporary medievalists increasingly interpret the sagas as hybrid creations shaped by continual interplay between spoken performance and textual revision.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It introduces a rare manuscript exception that undercuts the hybrid scholarly consensus summarized in the closing sentence.',
                'It supplies decisive stylistic evidence that the bookprose camp was entirely correct and that medieval Icelandic sagas derived nothing from Viking Age oral storytelling.',
                'It offers manuscript evidence that undermines the rigid opening dichotomy and leads into the hybrid view in the conclusion.',
                'It faults nineteenth- and twentieth-century literary historians for overlooking surviving Viking Age genealogical lists in Icelandic archives.'
            ],
            'C',
            'Cặp 50/50: **C** vs. **B**. Bẫy B cực hiểm vì mượn ngay vế đầu của câu gạch chân ("scribes actively reshaped dialogue and compressed genealogies") rồi đẩy sang cực đoan **1mm 1-Word Extremity** ("bookprose camp was *entirely correct*... derived *nothing* from oral storytelling") — phớt lờ hoàn toàn cụm khóa phía sau: *"even while drawing on shared oral episodes, blurring any sharp boundary"*! Chính sự "làm mờ ranh giới" giữa 2 phe ở câu đầu mở đường cho quan điểm dung hợp (hybrid) ở câu kết (C)!',
            'Trong câu hỏi Function of Underlined Sentence có cấu trúc 3 câu (Phe A vs. Phe B → `however` làm mờ ranh giới → `Consequently` dung hợp), TUYỆT ĐỐI tránh đáp án tuyên bố một phe "thắng tuyệt đối"!',
            [
                ('Reversed Function', 'Câu gạch chân là cơ sở DẪN TỚI đồng thuận dung hợp (Consequently...) ở câu cuối, không phải ngoại lệ phản bác nó.'),
                ('50/50 Trap (1mm): 1-Word Extremity', 'Bẫy 50/50 lấy một nửa câu gạch chân rồi đẩy sang cực đoan ("entirely correct", "derived nothing"), trái ngược với cụm "even while drawing on shared oral episodes, blurring any sharp boundary".'),
                ('Đáp án đúng', 'Bắt trọn hai chức năng nối cầu: phá vỡ thế lưỡng phân cứng nhắc ở câu 1 và mở đường cho góc nhìn lai ghép ở câu 3.'),
                ('Out of Scope Criticism', 'Văn bản không hề chỉ trích các sử gia văn học vì bỏ sót danh sách gia phả thời Viking.'),
            ]
        ),

        # Q11 — Inferences: Tree-Frog Toe Pads (50/50 Trap: Unstated Comparison) [Key: B]
        q_item(
            'sat_boss_d2_q11', 11, D_II, S_INF, 'Elite 750+',
            '<p>Tree frogs cling securely to rain-slicked leaves because their toe pads feature hexagonal epithelial cells separated by microscopic drainage channels that squeeze away trapped water films, restoring direct solid-to-solid friction. By contrast, smooth synthetic elastomer pads lose nearly all grip on wet glass because an unbroken film of water lubricates the contact interface. When biomechanics engineers molded synthetic silicone pads with frog-inspired hexagonal micro-channels, the patterned pads retained nearly 85% of their dry-surface friction on wet glass, although they peeled away easily under dry, dusty conditions where fine grit clogged the channels. These results suggest that ______</p>',
            'Which choice most logically completes the text?',
            [
                'molding hexagonal micro-channels onto synthetic elastomer pads enables them to retain full dry-surface adhesion across both wet glass and dry dusty environments.',
                'replicating the tree frog’s hexagonal micro-channel geometry substantially improves synthetic wet-surface adhesion by draining lubricating water films, though the design introduces vulnerability to particulate clogging in dry, dusty settings.',
                'smooth synthetic elastomer pads slip on wet glass primarily because fine airborne dust particles clog their microscopic surface drainage channels.',
                'patterned synthetic silicone pads generate substantially stronger friction on wet glass than living tree-frog toe pads do, while remaining far more susceptible to dust clogging than biological tissue.'
            ],
            'B',
            'Cặp 50/50: **B** vs. **D**. Đáp án D nghe cực kỳ "khoa học sinh học mô phỏng", nhưng sập bẫy **1mm Unstated Comparison**: đoạn văn KHÔNG HỀ đo hay so sánh lực bám của miếng silicone tạo rãnh *so với bàn chân ếch sống*, cũng không hề so sánh độ chống bụi giữa silicone và mô biểu bì ếch (bài chỉ so sánh silicone có rãnh vs. silicone trơn, và độ bám ướt của silicone có rãnh = ~85% độ bám khô của chính nó)! Đáp án B trung thành 100% với cả hai mặt: lợi ích tăng bám ướt nhờ thoát màng nước + đánh đổi dễ tắc rãnh khi khô bụi.',
            'Cẩn thận bẫy "So sánh bắc cầu lậu" (Unstated Comparison) trong bài mô phỏng sinh học (biomimicry): vật liệu nhân tạo mô phỏng sinh vật X KHÔNG đồng nghĩa văn bản đã so sánh xem vật liệu nhân tạo mạnh hơn hay yếu hơn sinh vật X!',
            [
                ('1-Word Extremity / Contradiction', 'Nói sai cả hai vế: độ bám ướt chỉ đạt "nearly 85%" (không phải "full") và rơi rụng dễ dàng ở môi trường khô bụi.'),
                ('Đáp án đúng', 'Gom trọn gọn cả ưu điểm thực chứng (tăng bám ướt nhờ thoát màng nước bôi trơn) lẫn hạn chế đánh đổi (dễ bị bụi làm tắc rãnh ở môi trường khô).'),
                ('Swapped Mechanism', 'Miếng elastomer trơn (smooth) không có rãnh để bị bụi làm tắc; chúng trượt trên kính ướt vì màng nước nguyên vẹn đóng vai trò chất bôi trơn.'),
                ('50/50 Trap (1mm): Unstated Comparison', 'Bẫy 50/50 rất tinh vi! Bài không hề so sánh trực tiếp lực bám ướt hay khả năng chống bụi giữa miếng silicone nhân tạo với bàn chân ếch cây thật.'),
            ]
        ),

        # Q12 — Words in Context: sanctioned vs. mandated (50/50 Trap: 1-Word Extremity) [Key: D]
        q_item(
            'sat_boss_d2_q12', 12, D_CS, S_WIC, 'Elite 750+',
            '<p>Contrary to the assumption that early modern European monarchs eradicated all local legal autonomy, a 1614 royal maritime charter in Normandy explicitly ______ informal merchant arbitration panels—formally permitting guild elders to settle minor cargo-loss claims whenever royal admiralty judges were unavailable, while leaving merchants free to appeal to the crown if they preferred.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            [
                'mandated',
                'curtailed',
                'adjudicated',
                'sanctioned'
            ],
            'D',
            'Cặp 50/50 kinh điển bậc 800: **sanctioned (D)** vs. **mandated (A)**! Phần lớn thí sinh 1400 loại thẳng tay `sanctioned` vì tưởng chữ này chỉ có nghĩa "trừng phạt / cấm vận kinh tế", rồi nhảy sang `mandated` (bắt buộc). Nhưng hãy áp dụng Quy tắc 1mm vào cụm giải thích ngay sau dấu gạch ngang: **"formally permitting... while leaving merchants free to appeal to the crown if they preferred"**! Cho phép + để thương nhân tự do lựa chọn = **cho phép/phê chuẩn chính thức**, KHÔNG phải cưỡng ép bắt buộc (`mandated` = bẫy **1-Word Extremity**)! Trong tiếng Anh học thuật, **sanction** là từ hai nghĩa đối lập nổi tiếng (contranym) với nghĩa cực hay thi trên SAT là *chính thức phê duyệt / cho phép*!',
            'Nạp ngay từ hai mặt (contranym) siêu hot của Hard M2: `sanction` = (1) trừng phạt, (2) CHÍNH THỨC PHÊ CHUẨN/CHO PHÉP! Luôn kiểm tra ranh giới 1mm giữa `authorized/sanctioned` (cho phép) vs. `mandated/compelled` (bắt buộc).',
            [
                ('50/50 Trap (1mm): 1-Word Extremity', 'Bẫy 50/50 siêu gắt! "mandated" = bắt buộc thi hành, mâu thuẫn 1mm với "formally permitting" và "leaving merchants free to appeal to the crown if they preferred".'),
                ('Opposite Meaning', 'curtailed = cắt giảm/hạn chế — ngược hướng với mở đầu "Contrary to the assumption that... monarchs eradicated all local legal autonomy".'),
                ('Collocation Mismatch', 'adjudicated = xét xử/phân xử một vụ tranh chấp — hiến chương hoàng gia không "xét xử các hội đồng trọng tài", mà chính hội đồng mới xét xử tranh chấp.'),
                ('Đáp án đúng', 'Nghĩa học thuật chuẩn xác: sanctioned = chính thức phê chuẩn/cho phép tồn tại và hoạt động, khớp tuyệt đối với "formally permitting".'),
            ]
        ),

        # Q13 — Central Ideas and Details: Tropical Brutalism (50/50 Trap: Scope Creep) [Key: A]
        q_item(
            'sat_boss_d2_q13', 13, D_II, S_CID, 'Elite 750+',
            '<p>Architectural critics frequently fault mid-twentieth-century civic buildings constructed of exposed raw concrete (<i>béton brut</i>) as austere monuments indifferent to human comfort. Yet architectural historian Dr. Paloma Herrera documents that in humid tropical capitals, designers such as Balkrishna Doshi and Affonso Eduardo Reidy intentionally paired thick concrete sun-breakers (<i>brise-soleil</i>) with elevated shaded breezeways to exploit thermal mass and cross-ventilation—passively lowering interior temperatures by several degrees without mechanical air-conditioning. Viewed in their climatic context, Herrera contends, these raw-concrete structures were pragmatic environmental adaptations rather than purely stylistic gestures.</p>',
            'Which choice best states the central idea of the text?',
            [
                'Though raw-concrete civic halls are often dismissed as austere, Herrera argues that tropical modernist designs used concrete pragmatically for passive cooling.',
                'Balkrishna Doshi and Affonso Eduardo Reidy avoided building with exposed raw concrete in humid tropical capitals because thick slabs trapped excessive heat indoors.',
                'Herrera demonstrates that mid-twentieth-century raw-concrete civic buildings across all climate zones outperform modern air-conditioned buildings in both energy efficiency and visual appeal.',
                'Architectural critics have historically admired mid-century raw-concrete civic buildings in temperate European cities while unfairly dismissing structurally identical designs in tropical capitals.'
            ],
            'A',
            'Cặp 50/50: **A** vs. **C**. Bẫy C rất dễ ăn điểm với người đọc lướt vì giữ đúng thái độ bênh vực kiến trúc bê tông thô của Herrera, nhưng mắc liền hai lỗi **1mm Scope Creep**: (1) thổi phồng phạm vi địa lý từ "in humid tropical capitals" thành *"across all climate zones"*, và (2) tự bịa ra phép so sánh vượt trội *"outperform modern air-conditioned buildings in... visual appeal"*! Chỉ A khóa đúng phạm vi khí hậu nhiệt đới và mục tiêu làm mát thụ động thực dụng của Herrera.',
            'Quy tắc 1mm chống Scope Creep: luôn kiểm tra phạm vi giới hạn (qualifier) về không gian và đối tượng trong bài ("in humid tropical capitals", "these... structures") — bất kỳ đáp án nào phình thành "across all climate zones" hay "all" đều chết ngay lập tức!',
            [
                ('Đáp án đúng', 'Khớp trọn vẹn khung đối lập của bài (bị chê khắc nghiệt ↔ thực tế ở vùng nhiệt đới là giải pháp thích nghi khí hậu làm mát thụ động thực dụng).'),
                ('Reversed Detail', 'Ngược hoàn toàn văn bản: Doshi và Reidy CHỦ ĐÍCH sử dụng bê tông thô kết hợp lam chắn nắng và hành lang thông gió để hạ nhiệt độ bên trong.'),
                ('50/50 Trap (1mm): Scope Creep', 'Bẫy 50/50 thổi phồng phạm vi! Herrera chỉ phân tích công trình ở thủ đô nhiệt đới ẩm — không hề nói về "all climate zones" hay so sánh thẩm mỹ hơn hẳn tòa nhà hiện đại.'),
                ('Unstated Comparison', 'Bài hoàn toàn không nhắc đến các thành phố ôn đới châu Âu để tạo phép so sánh thiên vị.'),
            ]
        ),

        # Q14 — Text Structure and Purpose: Kintsugi vs. Invisible Restoration (50/50 Trap: Unstated Value Judgment) [Key: C]
        q_item(
            'sat_boss_d2_q14', 14, D_CS, S_TSP, 'Elite 750+',
            '<p>In traditional Japanese <i>kintsugi</i> ceramic repair, artisans join shattered stoneware fragments with natural tree-sap lacquer dusted in powdered gold, deliberately accentuating the fracture network as a visible chapter of the vessel’s history. By contrast, twentieth-century Western museum conservation manuals generally prioritized "invisible restoration," filling losses with color-matched resins designed to return an object as closely as possible to its unbroken state. Art philosopher Dr. Takeshi Morimoto emphasizes that these two practices reflect distinct cultural conceptions of authenticity: one locates integrity in the candid record of wear and repair, whereas the other locates it in approximating the maker’s original intact design.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To argue that traditional Japanese <i>kintsugi</i> embodies a deeper and more historically honest philosophy of preservation than Western invisible restoration does.',
                'To evaluate the structural durability of natural tree-sap lacquer compared with synthetic color-matched resins in museum ceramic conservation.',
                'To contrast two ceramic-restoration traditions and link their visual practices to distinct conceptions of artistic authenticity.',
                'To trace how Western museum conservators gradually replaced invisible restoration with <i>kintsugi</i> techniques over the course of the twentieth century.'
            ],
            'C',
            'Cặp 50/50: **C** vs. **A**. Đây là chiếc bẫy 50/50 kinh điển nhất của thể loại phê bình nghệ thuật trên Digital SAT! Vì câu về *kintsugi* dùng chữ đẹp như "visible chapter", "candid record", thí sinh dễ cảm tính chọn A ("argues that *kintsugi* embodies a deeper and more historically honest philosophy... than Western..."). Nhưng soi 1mm vào giọng văn của Morimoto: ông hoàn toàn TRUNG LẬP phân tích ("reflect **distinct** cultural conceptions of authenticity: one locates... whereas the other locates...") — tuyệt đối không xếp hạng truyền thống nào sâu sắc hay trung thực hơn (bẫy **Unstated Comparison / Tone Drift**)! Chọn C!',
            'Trong đoạn văn so sánh hai trường phái nghệ thuật/triết học, kiểm tra ngay xem tác giả có thực sự chấm điểm bên nào "tốt hơn / sâu sắc hơn" không — nếu tác giả giữ giọng trung lập phân tích, mọi đáp án mang từ phán xét (`deeper`, `superior`, `more honest`) đều là bẫy 1mm!',
            [
                ('50/50 Trap (1mm): Unstated Comparison', 'Bẫy 50/50 gài phán xét giá trị! Morimoto phân tích trung lập hai quan niệm khác nhau về tính nguyên bản ("distinct cultural conceptions"), tuyệt đối KHÔNG khẳng định kintsugi sâu sắc hay trung thực hơn phục chế tàng hình.'),
                ('Out of Scope Focus', 'Văn bản không hề đánh giá hay so sánh độ bền cơ học giữa sơn mài nhựa cây và nhựa tổng hợp.'),
                ('Đáp án đúng', 'Giữ đúng giọng trung lập và cấu trúc 2 phần của bài: đối chiếu hai phương pháp phục chế gốm và liên hệ chúng với hai quan niệm khác biệt về tính nguyên bản nghệ thuật.'),
                ('Fabricated Timeline', 'Văn bản không hề nói các bảo tàng phương Tây đã từ bỏ phục chế tàng hình để chuyển sang kintsugi.'),
            ]
        ),

        # Q15 — Inferences: Publication Bias in Preclinical Trials (50/50 Trap: 1-Word Extremity) [Key: B]
        q_item(
            'sat_boss_d2_q15', 15, D_II, S_INF, 'Elite 750+',
            '<p>When pharmacologist Dr. Hannah Lindstrom audited 180 preclinical animal trials for candidate Alzheimer’s compounds conducted between 2005 and 2020, she documented a stark publication asymmetry: trials reporting statistically positive memory gains appeared in peer-reviewed journals 86% of the time, whereas equally rigorous trials finding no measurable benefit were published only 19% of the time, most often remaining locked inside unpublished laboratory archives. Because systematic meta-analyses that decide which drug candidates advance to expensive human clinical trials rely almost exclusively on published journal articles, Lindstrom cautions that ______</p>',
            'Which choice most logically completes the text?',
            [
                'peer-reviewed pharmacology journals between 2005 and 2020 published a substantially greater share of null-result preclinical animal trials than positive-result trials.',
                'systematic meta-analyses drawn from the published literature are likely to overestimate the average efficacy of candidate compounds, increasing the risk of advancing unpromising drugs into costly human trials.',
                'the unpublished null-result animal trials stored inside internal laboratory archives were rejected by peer-reviewed journals primarily because their study designs lacked rigor.',
                'none of the candidate Alzheimer’s compounds evaluated in preclinical animal trials between 2005 and 2020 actually produced genuine memory improvements in laboratory animals.'
            ],
            'B',
            'Cặp 50/50: **B** vs. **D**. Đáp án D sập bẫy **1mm 1-Word Extremity** cực tinh vi! Khi 86% nghiên cứu dương tính được đăng còn chỉ 19% nghiên cứu âm tính được đăng, tập dữ liệu công bố bị thiên lệch mạnh về phía kết quả tốt → các phân tích gộp (meta-analyses) chỉ đọc bài đã đăng sẽ **ước lượng quá cao hiệu quả trung bình** của các ứng viên thuốc và tăng nguy cơ đưa thuốc kém triển vọng vào thử nghiệm trên người (B). Điều đó KHÔNG có nghĩa là *không một hợp chất nào ("none")* tạo ra cải thiện thực sự trong thí nghiệm động vật (D đi quá xa bằng chứng 1mm)!',
            'Trong các bài suy luận về thiên lệch xuất bản (publication bias) hoặc thiên lệch mẫu (selection bias), kết luận chuẩn 1mm luôn là "làm sai lệch / thổi phồng ước tính trung bình" (`overestimate average efficacy`), KHÔNG BAO GIỜ là phủ nhận sạch trơn toàn bộ hiện tượng (`none of... actually...`)!',
            [
                ('Reversed Data', 'Đảo ngược số liệu bài: kết quả dương tính được đăng 86% còn kết quả âm tính (null-result) chỉ được đăng 19%.'),
                ('Đáp án đúng', 'Suy luận chuẩn 1mm từ thiên lệch chọn mẫu: khi kết quả âm tính bị giấu trong kho lưu trữ, meta-analysis chỉ dùng bài đã đăng sẽ phóng đại hiệu quả trung bình và làm tăng rủi ro đưa thuốc kém triển vọng vào thử nghiệm người.'),
                ('Direct Contradiction', 'Đoạn văn khẳng định rõ các thử nghiệm âm tính có chất lượng chặt chẽ ngang bằng ("equally rigorous trials").'),
                ('50/50 Trap (1mm): 1-Word Extremity', 'Bẫy 50/50 cực đoan hóa! Thiên lệch xuất bản làm méo ước lượng trung bình, nhưng KHÔNG chứng minh rằng *không một hợp chất nào* ("none") thực sự có hiệu quả trên động vật.'),
            ]
        ),
    ]

    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': BOSS_DRILL_2_TITLE,
            'subtitle': '15 câu thuần Hard M2 (750–800) luyện Quy tắc 1 Milimét loại bẫy 50/50: nghĩa học thuật thứ cấp, Collocation Mismatch, 1-Word Extremity, Reverse Causality, Unstated Comparison & Scope Creep.',
            'difficultyBadge': 'Hard M2 Boss • 750–800',
            'targetTimeMinutes': 22,
        },
        'drillModule': {
            'id': 'boss_drill_2_mod',
            'title': 'Boss Drill 2: 50/50 Trap Elimination — 1-Millimeter Rule',
            'timeLimitMinutes': 22,
            'questions': questions,
        },
    }


def get_drills():
    return [
        ('boss_drill_1', BOSS_DRILL_1_TITLE, 1, get_boss_drill_1()),
        ('boss_drill_2', BOSS_DRILL_2_TITLE, 2, get_boss_drill_2()),
    ]


if __name__ == '__main__':
    drills = get_drills()
    assert len(drills) == 2, f'Expected 2 drills, got {len(drills)}'

    seen_ids = set()
    all_errors = []

    for drill_key, title, order_idx, content_json in drills:
        assert content_json['schemaVersion'] == 1
        assert content_json['mode'] == 'drill'
        assert content_json['section'] == 'Reading and Writing'
        assert content_json['basicInfo']['difficultyBadge'] == 'Hard M2 Boss • 750–800'
        assert content_json['basicInfo']['targetTimeMinutes'] == 22
        assert content_json['drillModule']['timeLimitMinutes'] == 22

        errs = validate_sat_test(content_json, title)
        all_errors.extend(errs)

        qs = content_json['drillModule']['questions']
        assert len(qs) == 15, f'{drill_key}: expected 15 questions, got {len(qs)}'

        prefix = 'sat_boss_d1_q' if drill_key == 'boss_drill_1' else 'sat_boss_d2_q'
        dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        prev_ans = None
        streak = 0

        for idx, q in enumerate(qs, start=1):
            expected_id = f'{prefix}{idx}'
            assert q['id'] == expected_id, f'ID mismatch: {q["id"]} != {expected_id}'
            assert q['id'] not in seen_ids, f'Duplicate global ID: {q["id"]}'
            seen_ids.add(q['id'])
            assert q['difficulty'] in ('Elite 750+', 'Hard'), f'Invalid difficulty {q["difficulty"]} in {q["id"]}'
            assert q['explanation'].get('keyTakeaway') and len(q['explanation']['keyTakeaway'].strip()) >= 20

            ans = q['correctAnswer']
            dist[ans] += 1
            if ans == prev_ans:
                streak += 1
                assert streak < 2, f'{drill_key}: 3+ consecutive identical keys at {q["id"]}'
            else:
                streak = 0
                prev_ans = ans

        assert sorted(dist.values()) == [3, 4, 4, 4], f'{drill_key}: answer keys not 4/4/4/3 balanced: {dist}'
        print(f'  [PASS] {drill_key} (order={order_idx}): 15 Qs | keys={dist} | errors={len(errs)}')

    assert not all_errors, f'QA validation failed with {len(all_errors)} errors:\n' + '\n'.join(all_errors)
    print('\nBOSS R&W DRILLS 1 & 2 (30 ELITE Qs) QA PASSED!')
