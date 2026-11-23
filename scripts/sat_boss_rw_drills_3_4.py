# -*- coding: utf-8 -*-
"""
Hard M2 Boss Masterclass (750–800 Sprint) — R&W Boss Drills 3 & 4 (30 Elite Qs):
- Boss Drill 3: Archaic Literature, 19th-Century Poetry & Dual-Text Nuance (15 Qs)
- Boss Drill 4: Nested Hard Grammar Combos, Transitions & Synthesis (15 Qs)

100% original, copyright-clean Digital SAT 750–800 content.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sat_drills_1_1_and_2_1 import q_item


def get_boss_drill_3():
    title = '🔥 R&W Boss Drill 3: Archaic Literature, 19th-Century Poetry & Dual-Text Nuance (15 câu 750–800)'
    questions = [
        # Q1 — Central Ideas and Details (Archaic 18th-c essay prose, inverted syntax, extended metaphor) -> B
        q_item(
            'sat_boss_d3_q1', 1, 'Information and Ideas', 'Central Ideas and Details', 'Elite 750+',
            '<p><i>The following text is adapted from an original 1784 philosophical essay on reputation and craft.</i><br/>Seldom does the edifice raised amid clamor outlast the first winter tempest that its hurried architects scorned to anticipate, nor is the applause of a restless multitude any reliable surety against decay. Far more quietly labors the unheralded mason who, indifferent to the passing crowd’s impatience, dresses rough granite in obscurity; and though no herald proclaims his cornice upon completion, it is his stone that the seasons reluctantly weather rather than topple.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Public criticism of hurried architecture encourages stone masons to abandon decorative cornices in favor of plain granite.',
                'Work produced carefully without concern for immediate acclaim tends to prove far more durable than showy achievements celebrated upon arrival.',
                'Even the most painstakingly constructed stone buildings eventually collapse more rapidly than observers expect when exposed to winter storms.',
                'Craftsmen who work in obscurity rarely receive fair compensation because restless audiences cannot recognize skillful masonry.'
            ],
            'B',
            'Đoạn văn cổ thế kỷ 18 dùng cú pháp đảo ngữ ("Seldom does...", "nor is...", "Far more quietly labors...") kết hợp ẩn dụ kiến trúc để đối chiếu hai kiểu thành quả: công trình dựng vội giữa tiếng reo hò (clamor / applause) nhanh sụp đổ trước bão tố, còn người thợ đá âm thầm gọt giũa đá hoa cương chẳng màng sự sốt ruột của đám đông lại tạo ra công trình chỉ bị năm tháng bào mòn miễn cưỡng chứ không đổ sụp ("reluctantly weather rather than topple"). Ý chính là thành quả làm cẩn trọng không chạy theo danh tiếng nhất thời sẽ bền vững hơn nhiều → Chọn B.',
            'Gặp văn cổ đảo ngữ ("Seldom does...", "Far more quietly labors..."), hãy đảo lại trật tự S-V bình thường và giải mã ẩn dụ mở rộng (edifice/mason = thành quả/tác phẩm bền vững vs. phù phiếm).',
            [
                ('Literal / Out of Scope', 'Hiểu sai ẩn dụ thành câu chuyện thực tế về việc bỏ gờ mái (cornice) do bị chỉ trích.'),
                ('Đáp án đúng', 'Tóm gọn chính xác phép đối chiếu trung tâm: lao động cẩn trọng không màng hư danh nhất thời → độ bền vượt trội so với sự phô trương chóng tàn.'),
                ('Contradiction', 'Đảo ngược cụm "reluctantly weather rather than topple" (không hề sụp đổ nhanh hơn dự kiến).'),
                ('Out of Scope', 'Bài không hề bàn đến chuyện tiền công (fair compensation) của người thợ.'),
            ]
        ),

        # Q2 — Central Ideas and Details (19th-c metrical poem, nautical metaphor for memory) -> D
        q_item(
            'sat_boss_d3_q2', 2, 'Information and Ideas', 'Central Ideas and Details', 'Elite 750+',
            '<p><i>The following text is from an original 1876 poem in which a speaker examines an old coastal map once owned by a late companion.</i><br/>'
            'No longer may this yellowing chart command<br/>'
            'A vessel’s helm across the shifting bay;<br/>'
            'New shoals have crept where fathoms deep once lay,<br/>'
            'And winter gales have pared the headland’s sand.<br/>'
            'Yet fold it not among discarded things,<br/>'
            'Nor fault the ink that Time has rendered wrong:<br/>'
            'Its erring lines preserve, where memories throng,<br/>'
            'The bygone coast of his sure harborings.</p>',
            'Based on the text, why does the speaker refuse to discard the outdated chart?',
            [
                'The speaker believes that the bay’s depth and sandbars have remained stable enough for careful winter navigation.',
                'The speaker hopes to correct the faded ink markings so that future sailors can still steer safely into harbor.',
                'The speaker views the chart’s geographical errors as evidence that the companion deliberately exaggerated the coastline.',
                'The speaker cherishes the obsolete markings because they preserve the coastline as it appeared when the companion drew it.'
            ],
            'D',
            'Bốn dòng đầu thừa nhận tấm hải đồ cũ không còn dùng để lái tàu được nữa vì bãi cạn mới đã hình thành và bão đông đã gọt mòn mũi đất. Bốn dòng sau mở bằng "Yet" (bước ngoặt tư tưởng): đừng vứt đi hay chê nét mực bị Thời gian làm sai lệch ("Nor fault the ink that Time has rendered wrong"), vì chính những đường nét nay đã sai đó ("Its erring lines") lưu giữ nguyên vẹn bờ biển thời đôi tay vững chãi của người bạn quá cố vẽ nên nó → Chọn D.',
            'Trong thơ thế kỷ 19, luôn khoanh tròn bước ngoặt "Yet / But / Though" ở nửa sau: lý do thực sự của nhân vật trữ tình gần như luôn nằm sau bước ngoặt này!',
            [
                ('Contradiction', 'Dòng 1–4 khẳng định ngược lại: "New shoals have crept", "No longer may this yellowing chart command a vessel’s helm".'),
                ('Out of Scope', 'Nhân vật trữ tình không hề có ý định sửa nét mực để dùng cho thủy thủ tương lai.'),
                ('Misread Archaic Diction', 'Hiểu nhầm "erring lines" là lỗi cố ý phóng đại; câu trước ghi rõ "that Time has rendered wrong" (do thời gian làm cảnh vật đổi thay).'),
                ('Đáp án đúng', 'Bắt trọn nghịch lý trữ tình ở 4 dòng cuối: chính những nét vẽ lỗi thời lại bảo tồn ký ức về bờ biển lúc người bạn còn sống.'),
            ]
        ),

        # Q3 — Central Ideas and Details (1830s ironic social satire, Austen-style dry understatement) -> A
        q_item(
            'sat_boss_d3_q3', 3, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p><i>The following text is adapted from an original 1834 novel. Mr. Aldridge is a provincial magistrate hosting a dinner party.</i><br/>Mr. Aldridge prided himself above all on what he termed his "impartial candor," a virtue his neighbors observed with a mixture of bewilderment and caution. Were a guest to commend the new turnpike road, Mr. Aldridge would swiftly enumerate its ruinous toll rates and crooked ditches; yet should that same visitor, out of politeness, concede the point and lament the highway’s defects, Mr. Aldridge would discover, with admirable promptness, unforeseen commercial blessings in the very gravel he had moments earlier condemned.</p>',
            'Based on the text, what does the narrator imply about Mr. Aldridge’s "impartial candor"?',
            [
                'It reflects a reflexive habit of contradicting whoever is speaking rather than adherence to any consistent principle.',
                'It stems from his meticulous legal training, which obliges him to weigh the merits of municipal roads fairly.',
                'It succeeds in persuading his neighbors to examine both sides of public controversies with equal enthusiasm.',
                'It conceals his private financial investment in the construction of the new provincial turnpike.'
            ],
            'A',
            'Đoạn văn dùng giọng châm biếm kín đáo (ironic understatement): Ông Aldridge tự hào về "sự thẳng thắn công tâm" (impartial candor), nhưng hễ khách khen con đường mới thì ông chê tơi tả; đến khi vị khách lịch sự nhượng bộ hùa theo lời chê, ông lập tức quay xe khen ngợi chính lớp sỏi mình vừa lên án! Điều này ngầm vạch trần rằng ông chẳng hề có lập trường nhất quán mà chỉ có thói quen phản biện ngược lại bất kỳ ai đang nói → Chọn A.',
            'Cẩn thận bẫy "Literal Reading" ở văn châm biếm thế kỷ 19: dấu ngoặc kép quanh đức tính tự nhận ("impartial candor") và chi tiết "with admirable promptness" là tín hiệu mỉa mai 100%!',
            [
                ('Đáp án đúng', 'Giải mã chính xác hàm ý châm biếm: hành vi đổi phe ngay khi khách đồng thuận chứng tỏ động cơ duy nhất là thích cãi ngược.'),
                ('Literal / Missed Irony', 'Tin nguyên văn lời tự khoe "impartial candor" và suy diễn thêm về đào tạo luật học không có trong bài.'),
                ('Contradiction', 'Hàng xóm nhìn ông với "bewilderment and caution" (bối rối và dè chừng), không phải hào hứng bị thuyết phục.'),
                ('Out of Scope', 'Không hề có chi tiết nào về lợi ích tài chính bí mật trong dự án đường thu phí.'),
            ]
        ),

        # Q4 — Central Ideas and Details (19th-c Romantic nature verse, inverted syntax & paradox) -> C
        q_item(
            'sat_boss_d3_q4', 4, 'Information and Ideas', 'Central Ideas and Details', 'Elite 750+',
            '<p><i>The following text is from an original 1859 poem describing an apple orchard after an ice storm.</i><br/>'
            'To hasty eyes, this glazed and brittle grove<br/>'
            'Stands sealed within a monument of glass,<br/>'
            'Each bough bowed low as though no breath could pass<br/>'
            'Nor green return where February strove.<br/>'
            'Yet deep within the dark, unyielding rind,<br/>'
            'A patient vigor hoards its summer fire—<br/>'
            'For blooms must borrow winter’s stern attire<br/>'
            'Before a single petal dares unwind.</p>',
            'Which choice best states the central idea of the text?',
            [
                'Severe February ice storms permanently weaken orchard branches even when the trees appear undamaged from a distance.',
                'The visual splendor of ice-coated boughs surpasses the brief beauty of apple blossoms in late spring.',
                'Conditions that appear to imprison and extinguish life in the orchard are in fact essential precursors to its seasonal renewal.',
                'Orchard caretakers must patiently wait until summer temperatures arrive before pruning frost-damaged bark.'
            ],
            'C',
            'Nửa đầu bài thơ nói với "hasty eyes" (đôi mắt vội vã), vườn cây đóng băng trông như bị phong ấn chết cứng trong lăng mộ thủy tinh. Bước ngoặt "Yet" ở dòng 5 đảo ngược góc nhìn: sâu dưới lớp vỏ cây, nhựa sống kiên nhẫn tích trữ sức nóng mùa hạ ("hoards its summer fire"), bởi hoa phải mượn chiếc áo khắc nghiệt của mùa đông trước khi cánh hoa dám bung nở ("For blooms must borrow winter’s stern attire / Before a single petal dares unwind"). Đây là nghịch lý sinh học/thơ ca: cái lạnh tưởng như giam cầm hủy diệt lại chính là điều kiện tiên quyết cho sự tái sinh → Chọn C.',
            'Khóa cụm tương phản "To hasty eyes... Yet..." và liên từ giải thích "For" ở hai dòng cuối: mọi câu đáp án đi ngược bước ngoặt "Yet" đều là bẫy nửa đầu!',
            [
                ('Half-Passage Trap / Contradiction', 'Chỉ đọc bề mặt 4 dòng đầu và hiểu sai rằng băng giá làm suy yếu cây vĩnh viễn.'),
                ('Out of Scope', 'Bài thơ không hề so sánh vẻ đẹp của băng giá đẹp hơn hoa mùa xuân.'),
                ('Đáp án đúng', 'Bắt trọn nghịch lý cốt lõi của cả bài: sự giam cầm giá lạnh bề ngoài thực chất là điều kiện cần để vườn cây đơm hoa tái sinh.'),
                ('Out of Scope', 'Không hề nhắc đến người chăm vườn hay việc cắt tỉa vỏ cây.'),
            ]
        ),

        # Q5 — Command of Evidence (Literary Quotation: Original 19th-c novel) -> B
        q_item(
            'sat_boss_d3_q5', 5, 'Information and Ideas', 'Command of Evidence', 'Elite 750+',
            '<p><i>The Glassblower’s Apprentice</i> is an original 1868 novel by Clara Merrick. In the novel, young Henrik works under his stern uncle, Master Lind. A literary critic claims that although Henrik initially resents his uncle’s refusal to praise his finished vessels, Henrik eventually recognizes that this austere silence was a form of respect rather than indifference.</p>',
            'Which quotation from <i>The Glassblower’s Apprentice</i> most effectively illustrates the critic’s claim?',
            [
                '"Evening after evening Henrik set his cooled decanters along the oak shelf, and evening after evening Master Lind passed them without a syllable, until the boy’s pride hardened into a quiet, smoldering bitterness."',
                '"Only years later, watching his uncle lavish effortless compliments upon a merchant’s clumsy curiosities, did Henrik understand that the old man reserved his unsparing silence solely for craft serious enough to merit scrutiny."',
                '"On the morning of the guild exhibition, Master Lind lifted Henrik’s cobalt pitcher into the sunlit doorway and declared aloud before three aldermen that no steadier hand worked along the river."',
                '"Henrik learned at last to judge the annealing oven by the faint cherry glow behind its iron grate, knowing that a hasty draft would fracture even the purest lead crystal before dawn."'
            ],
            'B',
            'Luận điểm của nhà phê bình có 2 vế, trong đó trọng tâm cần chứng minh là vế kết: Henrik cuối cùng NHẬN RA sự im lặng khắc nghiệt của chú mình là biểu hiện của SỰ TÔN TRỌNG chứ không phải thờ ơ. A chỉ chứng minh nỗi oán giận ban đầu (thiếu sự nhận ra sau này); C làm ngược luận điểm (người chú lại khen lớn tiếng); D chỉ nói kỹ thuật nung thủy tinh. Duy nhất B cho thấy bước ngoặt nhận thức ("Only years later... did Henrik understand"): ông chú chỉ khen xã giao đồ vụng về, còn sự im lặng nghiêm khắc dành riêng cho tay nghề đáng được soi xét nghiêm túc → Chọn B.',
            'Với Command of Evidence (Literary Quotation), tách Claim thành checklist từng mảnh nhỏ rồi gạch ngay mọi trích dẫn chỉ thỏa mãn 1 nửa (như A) hoặc phá vỡ điều kiện cốt lõi (như C)!',
            [
                ('Half-Claim Trap', 'Chỉ minh họa sự oán giận ban đầu của Henrik, thiếu hoàn toàn sự nhận thức về lòng tôn trọng về sau.'),
                ('Đáp án đúng', 'Minh họa trọn vẹn bước ngoặt nhận thức: sự im lặng khắc nghiệt là đặc quyền tôn trọng dành cho tay nghề nghiêm túc, trái ngược lời khen hời hợt dành cho đồ vụng về.'),
                ('Contradiction', 'Miêu tả người chú khen ngợi công khai, trái ngược luận điểm nói về việc hiểu ý nghĩa của "austere silence".'),
                ('Irrelevant Detail', 'Chỉ mô tả kỹ năng kiểm soát lò ủ thủy tinh, không liên quan đến thái độ im lặng của người chú.'),
            ]
        ),

        # Q6 — Command of Evidence (Literary Quotation: Original 1884 poem) -> A
        q_item(
            'sat_boss_d3_q6', 6, 'Information and Ideas', 'Command of Evidence', 'Hard',
            '<p>"The Loom at Dusk" is an original 1884 poem by Thomas Halstead. In a study of nineteenth-century industrial verse, a scholar argues that the poem portrays mechanized textile looms not merely as sources of physical exhaustion, but as forces that displace the weavers’ perception of natural time, imposing an unchanging mechanical rhythm in place of seasonal cycles.</p>',
            'Which quotation from "The Loom at Dusk" most effectively illustrates the scholar’s claim?',
            [
                '"Outside the soot-dimmed pane the harvest moon / Gives way to frost, yet iron shuttles keep / One shrill, unvarying noon that knows no spring, / No solstice turning, nor autumnal sleep."',
                '"With lint-choked breath and knuckles raw from thread, / The weavers lean above the trembling frame / Till aching shoulders bow beneath the dusk / And cramped hands scarcely grip the wooden beam."',
                '"From raw gray flax the steady rollers draw / Crisp bolts of linen pale as winter snow, / Packed tight in crates for clippers bound downstream / Toward distant quays the weavers never know."',
                '"Along the meadow path the hedgerows bloom / With hawthorn white beside the swollen brook, / Where sparrows chorus through the lengthening light / Unmindful of the town’s dark chimney-smoke."'
            ],
            'A',
            'Luận điểm học giả nhấn mạnh: không chỉ là kiệt sức thể chất, mà khung cửi cơ khí CHIẾM ĐOẠT cảm nhận về thời gian tự nhiên, thay thế vòng tuần hoàn mùa vụ bằng nhịp điệu cơ giới bất biến ("displace natural time... unchanging mechanical rhythm in place of seasonal cycles"). Đáp án A khớp tuyệt đối từng hình ảnh: ngoài cửa sổ trăng thu chuyển sang sương giá, nhưng thoi sắt duy trì "một buổi trưa chói tai bất biến chẳng biết mùa xuân, chí tuyến hay giấc ngủ mùa thu"! B là bẫy cực mạnh vì chỉ tả sự kiệt sức thể chất ("not merely physical exhaustion")!',
            'Trong các Claim có cấu trúc "not merely X, but Y", đáp án đúng PHẢI chứng minh Y — bất kỳ trích dẫn nào chỉ chứng minh X (như B) đều là bẫy kinh điển của Hard Module 2!',
            [
                ('Đáp án đúng', 'Đối chiếu trực diện chu kỳ mùa tự nhiên (harvest moon, frost, spring, solstice) bị thay thế bởi nhịp máy đơn điệu bất biến ("one shrill, unvarying noon").'),
                ('Not-Merely-X Trap', 'Chỉ minh họa sự kiệt sức thể chất (lint-choked breath, aching shoulders) mà không hề đề cập đến sự biến dạng của thời gian tự nhiên/mùa vụ.'),
                ('Off-Topic Detail', 'Tập trung vào thành phẩm vải lanh và thương mại vận tải, không nói về nhận thức thời gian.'),
                ('Off-Topic Detail', 'Chỉ tả cảnh đồng cỏ mùa xuân tách biệt khỏi nhịp điệu bên trong xưởng dệt.'),
            ]
        ),

        # Q7 — Command of Evidence (Literary Quotation: Original 1862 Victorian novel) -> D
        q_item(
            'sat_boss_d3_q7', 7, 'Information and Ideas', 'Command of Evidence', 'Elite 750+',
            '<p><i>Harbor of Ash</i> is an original 1862 novel by Harriet Pendelton. A critic contends that the narrator uses details of Lady Verney’s drawing-room furnishings not to celebrate aristocratic opulence, but to expose a fragile performance of prestige meant to hide impending financial ruin.</p>',
            'Which quotation from <i>Harbor of Ash</i> most effectively illustrates the critic’s claim?',
            [
                '"Tall Venetian mirrors flanked the marble hearth, catching the glow of three silver chandeliers that turned the crimson damask curtains into folds of burnished fire."',
                '"Setting her ledger firmly beside the inkstand, Lady Verney informed her solicitor without a tremor that the manor and its timberlands would be auctioned at Michaelmas."',
                '"Her late husband’s study remained untouched since his death—a bare oak desk, two leather folios of navigation law, and a single brass globe dulled by coastal salt."',
                '"The gilded sconce was angled cunningly to double the flame of one thriftily stubbed candle, yet pale rectangles on the silk wall still betrayed where four ancestral portraits had quietly gone to satisfy creditors."'
            ],
            'D',
            'Kiểm tra checklist của Claim: (1) dùng chi tiết NỘI THẤT PHÒNG KHÁCH (drawing-room furnishings), (2) phơi bày màn TRÌNH DIỄN ĐỊA VỊ MONG MANH (fragile performance of prestige), (3) nhằm CHE GIẤU sự phá sản cận kề (hide impending financial ruin). A chỉ tả sự xa hoa thật sự; B cho thấy bà Verney thừa nhận thẳng thắn chuyện bán đấu giá (không phải che giấu qua đồ nội thất); C tả phòng làm việc giản dị của người chồng quá cố. Duy nhất D hội đủ 100%: đèn treo mạ vàng đặt góc khéo léo để nhân đôi ánh sáng từ một mẩu nến tiết kiệm, còn những ô chữ nhật nhạt màu trên tường lụa lại tố cáo chỗ 4 bức chân dung gia tộc đã bị bán lén để trả nợ → Chọn D.',
            'Đối chiếu sắc thái từ vựng trong trích dẫn: "angled cunningly" + "thriftily stubbed" + "betrayed" + "satisfy creditors" chính là bản dịch văn học hoàn hảo của "fragile performance... hide financial ruin"!',
            [
                ('Opposite Impression', 'Chỉ khắc họa sự xa hoa lộng lẫy thuần túy, không có dấu hiệu mong manh hay che giấu nợ nần.'),
                ('Contradiction', 'Bà Verney thẳng thắn thông báo bán tài sản với luật sư — trái ngược ý che giấu phá sản qua dàn dựng phòng khách.'),
                ('Wrong Setting / Off-Topic', 'Mô tả phòng làm việc mộc mạc của người chồng quá cố, không liên quan đến màn phô trương địa vị hay nợ nần.'),
                ('Đáp án đúng', 'Mọi chi tiết nội thất (đèn mạ vàng nhân đôi ngọn nến ngắn, mảng tường trống mất tranh tổ tiên để trả chủ nợ) đều khớp 100% luận điểm.'),
            ]
        ),

        # Q8 — Text Structure and Purpose (1819 aesthetic treatise, underlined anticipated objection) -> C
        q_item(
            'sat_boss_d3_q8', 8, 'Craft and Structure', 'Text Structure and Purpose', 'Elite 750+',
            '<p><i>The following text is adapted from an original 1819 essay criticizing the fashionable practice of rebuilding ruined medieval abbeys.</i><br/>Nothing so thoroughly misunderstands the dignity of an ancient cloister as the zeal to restore its shattered arches to crisp geometric completion. <u>No doubt the orderly antiquary will protest that a ragged wall offends symmetry and that fresh mortar secures the outline for posterity.</u> Yet to scrape six centuries of lichen from weathered limestone and cap every broken vault with obedient plaster is not to preserve antiquity, but to evict a genuine witness of time in favor of a polite theatrical counterfeit.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It endorses the pragmatic methods of nineteenth-century antiquaries who prioritize structural safety over decorative authenticity.',
                'It provides historical evidence showing that medieval builders themselves routinely patched weathered limestone with fresh plaster.',
                'It anticipates a likely objection rooted in order and preservation in order to prepare for the author’s sharper counterargument in the next sentence.',
                'It shifts the essay’s focus from architectural aesthetics to the financial costs of maintaining medieval cloisters.'
            ],
            'C',
            'Cấu trúc tu từ kinh điển của văn nghị luận thế kỷ 18–19: Câu 1 đưa luận điểm phê phán trào lưu phục dựng tu viện cổ cho "mới tinh". Câu gạch chân mở bằng "No doubt the orderly antiquary will protest that..." → dự đoán trước lập luận phản biện (anticipates a likely objection) nhân danh tính cân đối và bảo tồn cho hậu thế, để ngay câu sau dùng "Yet..." tung đòn bác bỏ sắc bén (gọi đó là "polite theatrical counterfeit" — hàng giả sân khấu lịch sự) → Chọn C.',
            'Nhìn thấy cụm "No doubt [nhóm X] will protest / object / contend that..." theo sau là "Yet / Still / But..." → 100% là kỹ thuật **Anticipate an objection / Concede a counterargument to refute it**!',
            [
                ('Reversed Tone', 'Tác giả KHÔNG hề tán thành nhà khảo cổ chuộng trật tự; câu sau bác bỏ gay gắt quan điểm này.'),
                ('Out of Scope', 'Không hề nhắc thợ xây thời Trung cổ từng tự trát vữa lên đá vôi.'),
                ('Đáp án đúng', 'Nêu chính xác cả nội dung (phản biện dựa trên trật tự & bảo tồn) lẫn vai trò cấu trúc (làm bàn đạp cho đòn phản bác ở câu tiếp theo).'),
                ('Out of Scope', 'Hoàn toàn không đề cập đến chi phí tài chính.'),
            ]
        ),

        # Q9 — Text Structure and Purpose (1891 lyric poem with sharp volta) -> A
        q_item(
            'sat_boss_d3_q9', 9, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p><i>The following text is from an original 1891 lyric poem.</i><br/>'
            'Behold the conqueror’s column, brass and proud,<br/>'
            'Whose chiseled boasts command the passing crowd;<br/>'
            'Tall chariots rear in bronze above the square,<br/>'
            'And gilded letters shout a monarch’s prayer<br/>'
            'That centuries may tremble at his name.<br/>'
            'Yet pause three paces west, where none proclaim<br/>'
            'A lineage or triumph: on the stone<br/>'
            'Rim of the village well, by ropes unknown<br/>'
            'Worn silky deep through unrecorded years,<br/>'
            'A quieter dominion perseveres.</p>',
            'Which choice best describes the overall structure of the text?',
            [
                'It describes ostentatious monuments erected to enforce lasting fame, then pivots to an unmarked everyday fixture whose worn endurance subtly undercuts that grandeur.',
                'It narrates a military victory commemorated by bronze chariots, then laments that local villagers have neglected the square’s historic statues.',
                'It contrasts the superior craftsmanship of bronze sculpture with the crude masonry of rural stone wells.',
                'It urges readers to study royal inscriptions closely before arguing that anonymous labor rarely leaves any physical trace.'
            ],
            'A',
            'Cấu trúc 2 chặng rạch ròi với bước ngoặt (volta) "Yet pause three paces west" ở dòng 6: Chặng 1 (dòng 1–5) miêu tả những tượng đài phô trương (cột đồng kiêu hãnh, lời khoe khoang chạm khắc, chữ mạ vàng gào thét cầu danh bất tử). Chặng 2 (dòng 6–10) xoay sang miệng giếng đá làng không khắc tên ai nhưng dây gầu vô danh kéo qua bao năm tháng đã mài nhẵn bóng — "a quieter dominion perseveres" (một quyền uy lặng lẽ hơn vẫn bền bỉ tồn tại), ngầm hạ bệ sự ồn ào kiêu căng của tượng đài → Chọn A.',
            'Với câu hỏi Overall Structure cho thơ có volta ("Yet..."), luôn kiểm tra đủ 2 vế: [Chặng trước volta] + [Chặng sau volta và thái độ của nó đối với chặng trước]!',
            [
                ('Đáp án đúng', 'Bắt trọn cả hai nửa bài thơ và mối tương quan tu từ: tượng đài phô trương đòi danh tiếng → ngoặt sang giếng đá bình dị bền bỉ làm lu mờ sự ồn ào kia.'),
                ('Out of Scope / Contradiction', 'Không hề kể chi tiết trận chiến hay than phiền dân làng bỏ bê tượng đài.'),
                ('Misplaced Focus', 'Bài thơ không so sánh tay nghề điêu khắc đồng tốt hơn thợ xây giếng đá.'),
                ('Contradiction', 'Dòng 8–9 khẳng định điều ngược lại: lao động vô danh ĐỂ LẠI dấu ấn vật lý sâu sắc trên thành giếng ("worn silky deep").'),
            ]
        ),

        # Q10 — Text Structure and Purpose (1850s narrative prose, extended metaphor function) -> B
        q_item(
            'sat_boss_d3_q10', 10, 'Craft and Structure', 'Text Structure and Purpose', 'Elite 750+',
            '<p><i>The following text is adapted from an original 1854 novel. Two estranged sisters, Beatrice and Nora, are meeting for tea after a decade apart.</i><br/>For twenty minutes the sisters traded impeccably civil observations concerning the spring rains, the vicar’s rheumatism, and the price of Darjeeling leaf. <u>Beneath their immaculate politeness, however, lay the precarious quiet of river ice in late March—glossy enough to mirror a tranquil sky, yet scored with hair-thin fractures waiting only for a single careless footstep to loose the dark current below.</u> When Nora at last set down her spoon and remarked how curiously their father’s estate had been apportioned, Beatrice’s porcelain saucer gave a sharp, unmistakable clatter.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It explains why the two sisters chose to postpone their reunion until the harsh winter weather had subsided.',
                'It uses an extended natural metaphor to expose the volatile, unspoken animosity concealed beneath the sisters’ courteous conversation.',
                'It suggests that Beatrice regrets her earlier refusal to discuss parish affairs with Nora.',
                'It foreshadows Nora’s sudden decision to abandon her legal claim to their father’s estate.'
            ],
            'B',
            'Câu 1 tả cuộc trò chuyện cực kỳ lịch thiệp xã giao về mưa xuân, giá trà. Câu gạch chân dùng ẩn dụ mở rộng về "lớp băng sông cuối tháng Ba" (mặt ngoài bóng loáng phản chiếu trời êm, bên dưới đầy vết nứt mảnh chỉ chờ một bước chân bất cẩn là dòng nước đen trào vỡ) để bóc trần sự thù địch ngầm đầy nguy hiểm dưới vỏ bọc lễ độ — dẫn thẳng đến câu 3 khi Nora chạm vào chủ đề di chúc của cha và đĩa sứ của Beatrice kêu lách cách → Chọn B.',
            'Khi câu gạch chân trong truyện xuất hiện ẩn dụ thiên nhiên (river ice, dark current) giữa hai câu đối thoại tâm lý, đừng bao giờ đọc nghĩa đen thành thời tiết thật (như A)!',
            [
                ('Literal Reading Trap', 'Đọc "late March" và "river ice" thành thời tiết thật khiến họ hoãn gặp — sai hoàn toàn chức năng ẩn dụ.'),
                ('Đáp án đúng', 'Xác định chuẩn xác cả thủ pháp (extended natural metaphor) lẫn ý nghĩa tâm lý (bộc lộ thù địch dễ bùng nổ ẩn sau sự lịch thiệp bề ngoài).'),
                ('Out of Scope', 'Không hề có chi tiết nào cho thấy Beatrice hối hận vì không bàn chuyện giáo xứ.'),
                ('Out of Scope', 'Câu cuối chỉ cho thấy Nora khơi chuyện chia tài sản chứ không từ bỏ quyền thừa kế.'),
            ]
        ),

        # Q11 — Cross-Text Connections #1 (Qualified concession + core disagreement) -> C
        q_item(
            'sat_boss_d3_q11', 11, 'Craft and Structure', 'Cross-Text Connections', 'Elite 750+',
            '<p><b>Text 1</b><br/>Literary historian Arthur Delacroix argues that nineteenth-century monthly magazine serialization degraded the formal discipline of the novel. Bound to fill rigid installment page quotas and fearful that subscribers would forget earlier plotlines during four-week intervals, authors routinely padded their narratives with redundant recaps and sprawling secondary casts—commercial compromises that diluted artistic unity.</p>'
            '<p><b>Text 2</b><br/>Media scholar Mei-Ling Zhou acknowledges that monthly publication contracts undeniably shaped chapter length and pacing in Victorian fiction. Yet she contends that dismissing recurring summaries and intricate subplots as mere mercenary padding misreads how nineteenth-century audiences actually consumed literature: because households read installments aloud and debated outcomes between issues, novelists deliberately wove expansive parallel threads to reward communal speculation across months.</p>',
            'Based on the texts, how would Mei-Ling Zhou (Text 2) most likely respond to Arthur Delacroix’s characterization of serialized novels (Text 1)?',
            [
                'By arguing that monthly publication schedules exerted no measurable influence on the length or pacing of Victorian chapters.',
                'By agreeing that redundant recaps weakened artistic unity, while insisting that publishers rather than authors deserved the blame.',
                'By conceding that contractual publication formats affected structural pacing, while rejecting the view that dense subplots and recaps were purely commercial filler.',
                'By demonstrating that nineteenth-century subscribers rarely discussed serialized novels with other members of their households.'
            ],
            'C',
            'Phân tích cấu trúc Text 2 khi đáp lại Text 1: (1) Nhượng bộ có điều kiện (Qualified Concession): "acknowledges that monthly publication contracts undeniably shaped chapter length and pacing"; (2) Phản bác trọng tâm: "Yet... dismissing recurring summaries and intricate subplots as mere mercenary padding misreads..." vì các tuyến phụ được dệt có chủ đích thẩm mỹ để phục vụ việc đọc và suy đoán cộng đồng → Chọn C.',
            'Ở câu Cross-Text bậc 750+, đáp án đúng thường có cấu trúc 2 vế song hành y hệt Text 2: `[Concede X] + [while rejecting/qualifying Y]`. Cẩn thận loại ngay đáp án cực đoan phủ nhận luôn cả phần Text 2 đã thừa nhận (như A)!',
            [
                ('Too Extreme / Contradiction', 'Text 2 thừa nhận rõ ràng hợp đồng xuất bản hàng tháng CÓ định hình độ dài và nhịp độ chương ("undeniably shaped"), không hề phủ nhận.'),
                ('Misattributed Agreement', 'Zhou KHÔNG đồng ý rằng các đoạn tóm tắt làm suy yếu tính thống nhất nghệ thuật; bà bảo vệ giá trị thẩm mỹ cộng đồng của chúng.'),
                ('Đáp án đúng', 'Phản chiếu hoàn hảo cả hai vế lập luận của Zhou: thừa nhận ảnh hưởng của lịch xuất bản lên nhịp độ, nhưng bác bỏ cách quy chụp các tuyến phụ là "hàng độn thương mại".'),
                ('Contradiction', 'Đảo ngược hoàn toàn bằng chứng của Text 2 ("households read installments aloud and debated outcomes").'),
            ]
        ),

        # Q12 — Cross-Text Connections #2 (Subtle point of agreement between opposing experts!) -> A
        q_item(
            'sat_boss_d3_q12', 12, 'Craft and Structure', 'Cross-Text Connections', 'Elite 750+',
            '<p><b>Text 1</b><br/>Paintings conservator Elena Marchetti advocates using calibrated organic solvents to strip yellowed nineteenth-century resin varnishes from seventeenth-century canvases. Although museumgoers have grown accustomed to a warm amber "old-master glow," Marchetti argues that darkened varnish severely distorts the cool azure skies and crisp tonal contrasts the original painters intended.</p>'
            '<p><b>Text 2</b><br/>Art historian David Okafor urges restraint in solvent cleaning of seventeenth-century oil paintings. Because aged varnish frequently bonds at a microscopic level with delicate upper paint glazes, aggressive stripping risks permanently abrading subtle shadow transitions. Even though retained amber varnish undeniably shifts an artist’s original color balance, Okafor maintains that tolerating chromatic alteration is ethically preferable to risking irreversible physical loss.</p>',
            'Based on the texts, both Elena Marchetti (Text 1) and David Okafor (Text 2) would most likely agree with which statement?',
            [
                'Aged resin varnish perceptibly alters the original color balance created by seventeenth-century painters.',
                'Calibrated organic solvents can reliably remove yellowed varnish without disturbing delicate upper paint glazes.',
                'Museum visitors generally prefer cool tonal contrasts over the warm amber appearance of uncleaned canvases.',
                'Art historians should prohibit all physical intervention on seventeenth-century canvases regardless of surface condition.'
            ],
            'A',
            'Bẫy siêu tinh vi dạng "Both would agree" giữa hai tác giả ĐỐI LẬP nhau về giải pháp! Marchetti ủng hộ tẩy lớp vecni cũ; Okafor cảnh báo hạn chế tẩy. Nhưng tìm điểm đồng thuận ẩn trong mệnh đề nhượng bộ của Text 2: "Even though retained amber varnish undeniably shifts an artist’s original color balance" — khớp hoàn toàn với Text 1 ("darkened varnish severely distorts the cool azure skies and crisp tonal contrasts the original painters intended")! Cả hai đều đồng ý rằng lớp vecni lâu năm làm thay đổi rõ rệt cân bằng màu gốc → Chọn A.',
            'Khi hai tác giả tranh luận gay gắt mà đề hỏi "both would agree", hãy nhảy thẳng vào các cụm nhượng bộ ("Although...", "Even though...", "Admittedly...") — điểm giao chung luôn ẩn ở đó!',
            [
                ('Đáp án đúng', 'Khớp cả hai văn bản: Text 1 nói vecni sẫm màu "severely distorts" và Text 2 thừa nhận nó "undeniably shifts an artist’s original color balance".'),
                ('Text 1 Only / Contradicted by Text 2', 'Okafor cảnh báo ngược lại rằng dung môi có nguy cơ mài mòn vĩnh viễn lớp men sơn trên cùng.'),
                ('Contradicted by Text 1', 'Text 1 nói khách bảo tàng đã quen thuộc với ánh hổ phách ấm ("grown accustomed to"), không nói họ chuộng tông lạnh hơn.'),
                ('Too Extreme', 'Okafor chỉ khuyên "urges restraint in solvent cleaning", không hề đòi cấm tuyệt đối mọi can thiệp vật lý.'),
            ]
        ),

        # Q13 — Cross-Text Connections #3 (Different causal mechanism for agreed empirical trend) -> D
        q_item(
            'sat_boss_d3_q13', 13, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Over a forty-year acoustic survey of European cities, bioacoustician Lukas Lindholm documented a steady rise in the minimum pitch of urban blackbird songs. Because low-frequency engine rumble from arterial roads overlaps with traditional blackbird notes, Lindholm concludes that city birds rely on real-time vocal flexibility—deliberately shifting their calls upward whenever street traffic intensifies.</p>'
            '<p><b>Text 2</b><br/>Evolutionary biologist Nadia Al-Mansoor notes that Lindholm’s field recordings accurately capture a widespread upward frequency shift across urban blackbird populations. In controlled aviary experiments, however, she raised urban-born and rural-born chicks inside identical soundproof chambers completely free of traffic noise; upon reaching maturity, the urban-lineage birds still sang at markedly higher baseline pitches than their rural counterparts, pointing toward multi-generational genetic selection.</p>',
            'Based on the texts, how would Nadia Al-Mansoor (Text 2) most likely view Lukas Lindholm’s conclusion (Text 1)?',
            [
                'She would question the accuracy of his forty-year field recordings on the grounds that urban blackbirds have not actually raised their minimum pitch.',
                'She would argue that arterial road traffic primarily produces high-frequency noise rather than low-frequency rumble.',
                'She would contend that rural-born blackbirds raised in soundproof chambers quickly learn to mimic the higher pitches of urban birds.',
                'She would view it as incomplete because heritable population differences appear to drive higher baseline pitch even in the absence of live traffic noise.'
            ],
            'D',
            'Text 2 KHÔNG bác bỏ dữ liệu thực địa của Lindholm ("accurately capture a widespread upward frequency shift"), nhưng thí nghiệm trong phòng cách âm cho thấy chim dòng dõi thành thị nuôi không có tiếng xe vẫn hót ở cao độ nền cao hơn chim nông thôn → chứng tỏ giải thích của Lindholm (chỉ do linh hoạt điều chỉnh tức thời khi gặp tiếng xe) là chưa đầy đủ vì còn có chọn lọc di truyền qua nhiều thế hệ → Chọn D.',
            'Phân biệt sắc bén "bác bỏ dữ liệu" (dispute the findings) với "bổ sung/thách thức cơ chế giải thích" (challenge the causal explanation): Al-Mansoor chấp nhận dữ liệu của Lindholm, chỉ thách thức nguyên nhân!',
            [
                ('Contradiction', 'Text 2 khẳng định rõ bản ghi âm của Lindholm "accurately capture" xu hướng tăng cao độ.'),
                ('Out of Scope / Reversed Fact', 'Text 2 không hề bác bỏ dải tần số thấp của tiếng động cơ xe.'),
                ('Contradiction', 'Chim dòng dõi nông thôn vẫn hót thấp hơn chim dòng dõi thành thị trong phòng cách âm.'),
                ('Đáp án đúng', 'Khớp hoàn hảo logic phòng cách âm: không có tiếng xe mà chênh lệch cao độ vẫn duy trì → giả thuyết linh hoạt tức thời của Lindholm bỏ sót yếu tố di truyền.'),
            ]
        ),

        # Q14 — Cross-Text Connections #4 (Theory vs. inconsistent practice contradiction) -> B
        q_item(
            'sat_boss_d3_q14', 14, 'Craft and Structure', 'Cross-Text Connections', 'Elite 750+',
            '<p><b>Text 1</b><br/><i>Adapted from an original 1815 preface on literary translation by Edmund Carew.</i><br/>A scrupulous translator of classical verse must resist the vanity of smoothing ancient idioms into familiar parlor English. Better that the modern reader feel the rugged strangeness of foreign syntax—and bend our tongue toward antiquity—than drag Homer or Theocritus down into the polite chatter of a contemporary drawing room.</p>'
            '<p><b>Text 2</b><br/>Modern scholars frequently praise Edmund Carew’s 1815 preface as an early manifesto for culturally faithful, "foreignizing" translation. Yet critic Priya Subramanian’s side-by-side collation of Carew’s own 1818 translations of Greek pastoral odes reveals a revealing double standard: while Carew preserved archaic inversions for heroic invocations, whenever a classical line referenced earthy farm labor or bodily coarseness, he quietly substituted genteel Regency euphemisms acceptable to elite salons.</p>',
            'Based on the texts, what is the primary relationship between Text 2 and Text 1?',
            [
                'Text 2 confirms that Carew’s 1818 translations faithfully implemented every stylistic principle advocated in Text 1.',
                'Text 2 complicates the theoretical position stated in Text 1 by citing textual evidence that its author applied that principle selectively in practice.',
                'Text 2 argues that classical Greek pastoral odes contain no archaic syntax worth preserving in English translation.',
                'Text 2 refutes the claim in Text 1 by showing that nineteenth-century salon readers actually preferred blunt references to farm labor.'
            ],
            'B',
            'Text 1 là tuyên ngôn lý thuyết năm 1815 của Edmund Carew: dịch giả phải giữ nguyên vẻ thô ráp ngoại lai của cổ văn chứ không được mài nhẵn theo lối nói lịch sự phòng khách. Text 2 đối chiếu ngay bản dịch năm 1818 của CHÍNH Carew và phát hiện "tiêu chuẩn kép" (double standard): ông chỉ giữ cú pháp cổ ở những lời cầu khẩn trang trọng, còn hễ gặp chi tiết lao động đồng áng dân dã hay thô mộc thì ông lại lén thay bằng uyển ngữ quý tộc thời Regency! Tức là Text 2 làm phức tạp hóa lập trường lý thuyết của Text 1 bằng bằng chứng cho thấy tác giả áp dụng chọn lọc/không nhất quán trong thực hành → Chọn B.',
            'Nhớ động từ tu từ 750+ cực phổ biến trên SAT: "complicates [a claim/position]" = không bác bỏ hoàn toàn từ A-Z mà chỉ ra mâu thuẫn, giới hạn hoặc tính không nhất quán đằng sau nó!',
            [
                ('Contradiction', 'Text 2 chứng minh điều ngược lại: bản dịch 1818 bộc lộ tiêu chuẩn kép chứ không trung thành trọn vẹn.'),
                ('Đáp án đúng', 'Tóm gọn chính xác mối quan hệ: đối chiếu bản dịch thực tế để chỉ ra sự áp dụng chọn lọc (inconsistent/selective practice) so với tuyên ngôn lý thuyết ở Text 1.'),
                ('Out of Scope', 'Text 2 không hề nói thơ mục đồng Hy Lạp không có cú pháp cổ đáng giữ.'),
                ('Reversed Logic', 'Carew phải thay bằng uyển ngữ quý tộc CHÍNH VÌ giới phòng khách không chuộng lối nói thô mộc.'),
            ]
        ),

        # Q15 — Cross-Text Connections #5 (Methodological proxy critique without disputing raw tallies) -> C
        q_item(
            'sat_boss_d3_q15', 15, 'Craft and Structure', 'Cross-Text Connections', 'Elite 750+',
            '<p><b>Text 1</b><br/>Examining parish marriage registers across three English port towns between 1740 and 1790, economic historian Marta Kowalski found that the share of shipwrights signing their full names—rather than marking an "X"—climbed from 41 percent to 68 percent. She concludes that formal reading and writing proficiency expanded broadly among maritime artisans during that fifty-year span.</p>'
            '<p><b>Text 2</b><br/>Social historian Samuel Mensah accepts the statistical reliability of Kowalski’s signature counts across the three ports, yet warns that eighteenth-century parish schools taught reading and writing sequentially rather than simultaneously, reserving penmanship lessons for pupils who could afford extra years of attendance. Because many artisans learned to read fluently without ever being taught to write—while others merely memorized the mechanical strokes of their own names—signature tallies offer a noisy gauge of overall literacy.</p>',
            'Based on the texts, how would Samuel Mensah (Text 2) most likely respond to Marta Kowalski’s conclusion (Text 1)?',
            [
                'By challenging the numerical accuracy of her 41-to-68-percent tally on the grounds that parish registers omitted maritime artisans.',
                'By noting that because parish schools taught writing before reading, full signatures reliably prove fluent reading ability.',
                'By acknowledging her signature figures while cautioning that signing one’s name is an imprecise measure that can both overlook readers who could not write and overstate broader writing fluency.',
                'By arguing that shipwrights who marked an "X" in marriage registers intentionally concealed their formal education from parish clerks.'
            ],
            'C',
            'Theo dõi lập luận phương pháp luận sắc bén của Samuel Mensah ở Text 2: (1) Thừa nhận số liệu thô đáng tin ("accepts the statistical reliability of Kowalski’s signature counts"); (2) Chỉ ra hai chiều sai số của thước đo chữ ký (noisy gauge / imprecise proxy): vì trường học dạy đọc trước, viết sau → nhiều người đọc thông thạo nhưng không biết viết (bị bỏ sót), trong khi người khác chỉ học thuộc máy móc nét chữ ký tên mình (làm thổi phồng năng lực viết thực tế) → Chọn C.',
            'Khi Text 2 đánh vào THƯỚC ĐO ĐẠI DIỆN (proxy measurement — ở đây là dùng chữ ký để suy ra năng lực đọc & viết), hãy kiểm tra đủ hai chiều sai lệch (underestimate/overlook vs. overestimate/overstate)!',
            [
                ('Contradiction', 'Mensah công khai chấp nhận độ tin cậy thống kê của số liệu chữ ký ("accepts the statistical reliability").'),
                ('Reversed Sequence', 'Text 2 nói nhiều người biết đọc nhưng chưa từng học viết — tức dạy đọc TRƯỚC viết, không phải viết trước đọc.'),
                ('Đáp án đúng', 'Bắt trọn cả sự công nhận số liệu lẫn phân tích sai số hai chiều của thước đo chữ ký.'),
                ('Out of Scope', 'Không hề có chi tiết nào cho rằng thợ đóng tàu cố tình giấu học vấn bằng cách ký dấu "X".'),
            ]
        ),
    ]

    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': title,
            'subtitle': '15 câu văn cổ thế kỷ 18–19, thơ đảo ngữ ẩn dụ, Literary Quotations và 5 bài Dual-Text 750–800 chuyên trị bẫy nhượng bộ tinh vi & điểm đồng thuận ẩn.',
            'difficultyBadge': 'Hard M2 Boss • 750–800',
            'targetTimeMinutes': 22,
        },
        'drillModule': {
            'id': 'sat_boss_drill_3_mod',
            'title': 'R&W Boss Drill 3: Archaic Literature, 19th-Century Poetry & Dual-Text Nuance',
            'timeLimitMinutes': 22,
            'questions': questions,
        },
    }


def get_boss_drill_4():
    title = '🔥 R&W Boss Drill 4: Nested Hard Grammar Combos, Transitions & Synthesis (15 câu 750–800)'
    sec_stem = 'Which choice completes the text so that it conforms to the conventions of Standard English?'
    trans_stem = 'Which choice completes the text with the most logical transition?'

    questions = [
        # Q1 — Boundaries (Stacked non-essential appositives) -> C
        q_item(
            'sat_boss_d4_q1', 1, 'Standard English Conventions', 'Boundaries', 'Elite 750+',
            '<p>Completed in 1883, the Brooklyn Bridge, an engineering triumph overseen in its final decade by Emily Warren Roebling, the chief engineer’s ______ spanned the East River with unprecedented steel-wire suspension cables.</p>',
            sec_stem,
            [
                'wife and principal field deputy',
                'wife and principal field deputy;',
                'wife and principal field deputy,',
                'wife, and principal field deputy,'
            ],
            'C',
            'Cấu trúc đồng vị ngữ lồng nhau (Stacked Non-Essential Appositives): Chủ ngữ chính là "the Brooklyn Bridge", động từ chính là "spanned". Giữa chúng có cụm đồng vị thứ nhất (", an engineering triumph overseen... by Emily Warren Roebling") và cụm đồng vị thứ hai lồng bên trong bổ nghĩa cho bà Roebling (", the chief engineer’s wife and principal field deputy,"). Ta BẮT BUỘC phải đóng cả hai cụm bổ ngữ không thiết yếu này bằng 1 dấu phẩy ngay trước động từ chính "spanned" → Chọn C. A thiếu dấu phẩy đóng; B dùng chấm phẩy chặt đứt chủ ngữ khỏi động từ; D đặt dấu phẩy thừa chia cắt cụm danh từ song song "wife and principal field deputy".',
            'Gặp đồng vị ngữ lồng nhau nằm giữa S và V, áp dụng bài test cắt bỏ (Delete Test): bỏ toàn bộ từ dấu phẩy đầu sau S đến dấu phẩy đóng trước V → "Completed in 1883, the Brooklyn Bridge spanned..." phải liền mạch không gãy!',
            [
                ('Missing Closing Comma', 'Thiếu dấu phẩy đóng cụm đồng vị không thiết yếu, khiến cụm bổ ngữ dính liền vào động từ chính "spanned".'),
                ('Semicolon Split Trap', 'Dấu chấm phẩy tách rời chủ ngữ "the Brooklyn Bridge" khỏi động từ chính "spanned" → tạo 2 mảnh Fragment.'),
                ('Đáp án đúng', 'Đóng trọn vẹn cụm đồng vị lồng nhau bằng dấu phẩy đơn chuẩn xác trước động từ chính "spanned".'),
                ('Compound Phrase Split', 'Không đặt dấu phẩy trước "and" khi chỉ nối hai danh từ song song ("wife and principal field deputy") chứ không phải 2 mệnh đề độc lập.'),
            ]
        ),

        # Q2 — Boundaries (Semicolon-list super-commas) -> A
        q_item(
            'sat_boss_d4_q2', 2, 'Standard English Conventions', 'Boundaries', 'Elite 750+',
            '<p>For her comparative archive of endangered musical instruments, ethnomusicologist Dr. Miriam Al-Khatib cataloged three rare chordophones: the <i>kora</i>, a twenty-one-string bridge-harp crafted from calabash gourds in West ______ the <i>nyckelharpa</i>, a keyed fiddle originating in medieval Sweden; and the <i>morin khuur</i>, a horsehead-carved spike fiddle native to Mongolia.</p>',
            sec_stem,
            [
                'Africa;',
                'Africa,',
                'Africa:',
                'Africa'
            ],
            'A',
            'Bài kiểm tra Super-Semicolon (dấu chấm phẩy ngăn cách danh sách phức tạp): Sau dấu hai chấm ở "chordophones:" là danh sách 3 nhạc cụ mà MỖI MỤC đều chứa dấu phẩy nội bộ cho cụm đồng vị ngữ. Nhìn dấu hiệu khóa ở mục 2→3: `medieval Sweden; and the morin khuur` đã dùng dấu chấm phẩy `;`! Do đó ranh giới mục 1→2 sau "West Africa" PHẢI đồng bộ dùng dấu chấm phẩy (`Africa;`) → Chọn A.',
            'Khi thấy danh sách có ít nhất 1 dấu `;` ngăn cách (đặc biệt trước `and` ở cuối), hãy kiểm tra tính đối xứng: mọi ranh giới cấp cao giữa các mục trong danh sách đó đều PHẢI dùng `;`!',
            [
                ('Đáp án đúng', 'Dùng Super-Semicolon (`Africa;`) đồng bộ với `; and the morin khuur`, phân tách rõ ràng mục 1 khỏi mục 2 dù bên trong có nhiều dấu phẩy.'),
                ('Comma Ambiguity Trap', 'Dùng dấu phẩy làm mờ ranh giới mục 1–2 và phá vỡ tính nhất quán với dấu `;` ở mục 2–3.'),
                ('Nested Colon Trap', 'Đã có dấu hai chấm mở danh sách ở "chordophones:", không được lồng thêm dấu hai chấm thứ hai giữa các mục liệt kê.'),
                ('Fused Items', 'Không có dấu câu khiến "West Africa" dính liền vào mục thứ hai "the nyckelharpa".'),
            ]
        ),

        # Q3 — Boundaries (Colon before explanation NP vs. false semicolon/period) -> D
        q_item(
            'sat_boss_d4_q3', 3, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Paleobotanists excavating Eocene coal seams on Axel Heiberg Island in the Canadian High Arctic uncovered something that initially baffled climate ______ fossilized dawn redwood stumps still retaining unmineralized cellular wood, proving that lush temperate rainforests once thrived above the Arctic Circle.</p>',
            sec_stem,
            [
                'modelers;',
                'modelers.',
                'modelers; in fact,',
                'modelers:'
            ],
            'D',
            'Phân tích hai vế quanh chỗ trống: Vế trái là 1 mệnh đề độc lập hoàn chỉnh (IC: "Paleobotanists... uncovered something that initially baffled climate modelers"). Vế phải ("fossilized dawn redwood stumps still retaining..., proving that...") tuy dài tới 20 từ nhưng KHÔNG có động từ chính chia thì (retaining & proving đều là phân từ V-ing) → chỉ là một cụm danh từ (NP) giải thích cho chữ "something"! Vì vế phải KHÔNG phải IC, loại ngay `;` (A), `.` (B) và `; in fact,` (C). Chỉ có dấu hai chấm (`:`) đứng sau IC mới dẫn nhập chính xác cụm danh từ giải thích → Chọn D.',
            'Đừng bị đánh lừa bởi độ dài vế sau! Trước khi chọn dấu chấm (.) hay chấm phẩy (;), LUÔN kiểm tra xem vế sau có động từ chính (finite verb) để tạo thành IC thực sự hay chỉ là NP + cụm V-ing!',
            [
                ('Semicolon Before Fragment', 'Dấu chấm phẩy bắt buộc hai bên đều là IC; vế sau chỉ là cụm danh từ ("stumps retaining..., proving...") không có động từ chính.'),
                ('Period Creating Fragment', 'Ngắt câu bằng dấu chấm biến toàn bộ cụm danh từ phía sau thành câu cụt (Fragment).'),
                ('Semicolon + Transition Fragment Trap', 'Bẫy kinh điển 750+: `; in fact,` vẫn cần một IC đầy đủ phía sau, nhưng cụm "fossilized... stumps..." thiếu động từ chính.'),
                ('Đáp án đúng', 'Dấu hai chấm (`:`) sau IC hoàn chỉnh dẫn nhập chuẩn xác lời giải thích cụ thể cho từ "something".'),
            ]
        ),

        # Q4 — Boundaries (False colon trap after preposition/participle "including") -> B
        q_item(
            'sat_boss_d4_q4', 4, 'Standard English Conventions', 'Boundaries', 'Elite 750+',
            '<p>During her botanical fieldwork across remote Andean cloud forests, collector Camila Morales gathered thousands of herbarium specimens that yielded previously undocumented flora, ______ a purple-flowered shrub in the nightshade family, a high-altitude wax palm, and a resinous medicinal fern.</p>',
            sec_stem,
            [
                'including:',
                'including',
                'including,',
                'including;'
            ],
            'B',
            'Bẫy False Colon kinh điển! Thí sinh thấy danh sách 3 loài thực vật phía sau nên theo phản xạ chọn ngay `including:`. Nhưng trên Digital SAT, dấu hai chấm CHỈ ĐƯỢC đặt sau một mệnh đề độc lập (IC) trọn vẹn — TUYỆT ĐỐI CẤM đặt dấu hai chấm, dấu phẩy, hay chấm phẩy ngay sau giới từ/từ dẫn nhập liệt kê như `including`, `such as`, `like`, hoặc động từ `are / consist of`! Dấu phẩy tách cụm bổ ngữ đã nằm SẴN trước `including`, nên sau `including` phải là KHÔNG DẤU CÂU → Chọn B.',
            'Quy tắc thép cho False Colon: Không bao giờ đặt `:`, `,`, hay `;` ngay sau `including`, `such as`, `between`, `consists of`, hoặc `are` trước danh sách!',
            [
                ('False Colon After Preposition', 'Đặt dấu hai chấm ngay sau "including" phá vỡ cấu trúc giới từ – tân ngữ và vi phạm quy tắc IC trước dấu hai chấm.'),
                ('Đáp án đúng', 'Nối liền mạch "including" với danh sách tân ngữ phía sau mà không chen dấu câu thừa.'),
                ('Unnecessary Comma', 'Dấu phẩy sau "including" cắt ngang vô lý giữa từ dẫn nhập và phần tử đầu tiên của danh sách.'),
                ('False Semicolon', 'Dấu chấm phẩy sau "including" tạo ra Fragment ở cả cụm phía sau.'),
            ]
        ),

        # Q5 — Boundaries (Dash-parenthetical closure + finite verb double combo) -> A
        q_item(
            'sat_boss_d4_q5', 5, 'Standard English Conventions', 'Boundaries', 'Elite 750+',
            '<p>Intrinsically disordered proteins found in tardigrades—molecules that, lacking a rigid three-dimensional fold in hydrated cells, rapidly harden into a protective glasslike ______ delicate cellular membranes from collapsing during extreme desiccation.</p>',
            sec_stem,
            [
                'matrix—prevent',
                'matrix, prevent',
                'matrix—preventing',
                'matrix; prevent'
            ],
            'A',
            'Đòn combo 2 tầng cực hiểm (Dash Closure + Main Finite Verb): Mở đầu bằng chủ ngữ số nhiều "Intrinsically disordered proteins found in tardigrades", theo sau là dấu gạch ngang `—` mở cụm đồng vị giải thích dài ("—molecules that, lacking..., rapidly harden into a protective glasslike matrix—"). Do bên trong có cặp dấu phẩy lồng, thí sinh dễ quên dấu `—` ở đầu mà đóng nhầm bằng `,` (B) hoặc `;` (D)! Sau khi đóng đúng bằng `—`, câu VẪN CẦN động từ chính chia thì số nhiều cho "proteins" → phải là `prevent` (A), loại bẫy phân từ cụt `preventing` (C)!',
            'Luôn khớp đôi dấu câu ngăn cách (`—` mở → `—` đóng, cấm trộn `—` với `,`) rồi kiểm tra ngay sau dấu đóng xem câu đã có ĐỘNG TỪ CHÍNH (finite verb) cho chủ ngữ đầu câu chưa!',
            [
                ('Đáp án đúng', 'Đóng chuẩn dấu gạch ngang đôi (`—...—`) và cung cấp động từ chính số nhiều "prevent" khớp chủ ngữ "proteins".'),
                ('Mismatched Pair Trap', 'Mở bằng dấu gạch ngang (`—`) nhưng đóng bằng dấu phẩy (`,`) — lỗi lệch cặp dấu câu kinh điển.'),
                ('Non-Finite Fragment Trap', 'Đóng đúng dấu gạch ngang nhưng dùng phân từ "preventing", khiến cả câu không có động từ chính (Fragment).'),
                ('Semicolon Split Trap', 'Không đóng được cụm gạch ngang và dùng dấu chấm phẩy cắt rời chủ ngữ khỏi động từ chính.'),
            ]
        ),

        # Q6 — Boundaries (Mid-clause parenthetical ", however," inside a single IC with long gerund subject) -> C
        q_item(
            'sat_boss_d4_q6', 6, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Acoustic archaeologists have reconstructed the resonant chambers of several Bronze Age stone tombs with remarkable precision. Determining whether ancient builders deliberately tuned those cavities to amplify ritual ______ remains far more speculative.</p>',
            sec_stem,
            [
                'chanting; however,',
                'chanting, however;',
                'chanting, however,',
                'chanting however,'
            ],
            'C',
            'Bẫy "Phản xạ `; however,` mù quáng" của học sinh mục tiêu 750+! Đọc kỹ câu thứ hai: Chủ ngữ là MỘT cụm danh động từ dài ("Determining whether ancient builders deliberately tuned those cavities to amplify ritual chanting"), và động từ chính của nó là "remains far more speculative". Toàn bộ câu 2 chỉ có DUY NHẤT 1 mệnh đề độc lập (1 IC)! Từ nối `however` đứng xen giữa chủ ngữ và động từ nên PHẢI được bọc bởi cặp dấu phẩy hai bên (`, however,`) → Chọn C! Nếu dùng `; however,` (A) hay `, however;` (B) sẽ chặt đôi chủ ngữ khỏi động từ thành 2 Fragment!',
            'Đừng bao giờ mặc định cứ thấy `however` là chọn `; however,`! Kiểm tra vế trái và vế phải: 2 IC → `; however,`; chỉ 1 IC (xen giữa S và V) → `, however,`!',
            [
                ('False Semicolon Trap', 'Vế trái chỉ là cụm chủ ngữ V-ing ("Determining whether...") chưa hề có động từ chính; đặt dấu `;` tạo ngay 2 Fragment.'),
                ('False Semicolon Trap', 'Vế phải ("remains far more speculative") thiếu chủ ngữ nên không thể đứng sau dấu chấm phẩy.'),
                ('Đáp án đúng', 'Dùng cặp dấu phẩy (`, however,`) kẹp từ nối xen giữa trong cùng một mệnh đề độc lập duy nhất.'),
                ('Missing Opening Comma', 'Thiếu dấu phẩy mở trước "however", biến dấu phẩy sau thành một dấu phẩy đơn chặn giữa chủ ngữ và động từ.'),
            ]
        ),

        # Q7 — Form, Structure, and Sense (Ultra-long subject-verb distance with inverted clause) -> B
        q_item(
            'sat_boss_d4_q7', 7, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite 750+',
            '<p>Tucked behind the vaulted archives of the city’s maritime museum, amid stacks of frayed navigation charts and uncataloged ships’ manifests, ______ an annotated eighteenth-century logbook that documents an otherwise unrecorded Pacific voyage.</p>',
            sec_stem,
            [
                'rest',
                'rests',
                'have rested',
                'were resting'
            ],
            'B',
            'Cấu trúc ĐẢO NGỮ với khoảng cách chủ-vị cực dài (Inverted Clause SVA): Toàn bộ phần trước chỗ trống ("Tucked behind..., amid stacks of... charts and... manifests") chỉ là chuỗi cụm phân từ và giới từ chỉ địa điểm chứa đầy danh từ số nhiều gây nhiễu (`archives`, `stacks`, `charts`, `manifests`). Chủ ngữ THỰC SỰ nằm SAU chỗ trống: `an annotated eighteenth-century logbook` (SỐ ÍT)! Kết hợp dấu hiệu thì hiện tại đơn ở mệnh đề quan hệ ("that documents"), động từ bắt buộc chia số ít hiện tại → `rests` (B).',
            'Gặp câu mở đầu bằng cụm giới từ/phân từ chỉ vị trí ("Tucked behind...", "Buried beneath...", "Among..."), chủ ngữ thật nằm NGAY SAU động từ — đừng bao giờ chia theo các danh từ số nhiều đứng trước chỗ trống!',
            [
                ('Decoy Plural Trap', 'Động từ số nhiều "rest" bị bẫy bởi các danh từ số nhiều gần chỗ trống (charts, manifests) thay vì chủ ngữ thật "logbook".'),
                ('Đáp án đúng', 'Động từ số ít hiện tại đơn "rests" khớp cả số ít của chủ ngữ đảo ngữ "an annotated... logbook" lẫn thì hiện tại của "documents".'),
                ('Wrong Number (Plural)', '"have rested" là động từ số nhiều, sai với chủ ngữ số ít "logbook".'),
                ('Wrong Number + Tense Shift', '"were resting" vừa sai số nhiều vừa lệch thì quá khứ so với hiện tại đơn "documents".'),
            ]
        ),

        # Q8 — Form, Structure, and Sense (Dangling participial modifier + possessive trap) -> D
        q_item(
            'sat_boss_d4_q8', 8, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite 750+',
            '<p>Having spent four winters calibrating acoustic buoys beneath the Ross Ice Shelf, ______</p>',
            sec_stem,
            [
                'glaciologist Dr. Amara Osei’s resulting dataset revealed unexpected subglacial meltwater channels pulsing every twelve days.',
                'unexpected subglacial meltwater channels pulsing every twelve days were detected by glaciologist Dr. Amara Osei.',
                'the acoustic measurements compiled by glaciologist Dr. Amara Osei pointed to subglacial meltwater channels pulsing every twelve days.',
                'glaciologist Dr. Amara Osei compiled a dataset revealing unexpected subglacial meltwater channels that pulse every twelve days.'
            ],
            'D',
            'Bẫy Dangling Modifier kết hợp Possessive Subject Trap: Cụm phân từ mở đầu ("Having spent four winters calibrating acoustic buoys...") đặt ra câu hỏi: AI đã dành 4 mùa đông hiệu chỉnh phao âm học? Câu trả lời phải là nhà băng hà học `glaciologist Dr. Amara Osei` — và CHÍNH bà phải đứng làm chủ ngữ ngữ pháp ngay sau dấu phẩy! Cảnh giác cực độ với bẫy A: `Dr. Amara Osei’s resulting dataset` có chủ ngữ ngữ pháp là `dataset` (tập dữ liệu không thể đi hiệu chỉnh phao!). B biến `channels` thành chủ ngữ; C biến `measurements` thành chủ ngữ. Chỉ có D đặt trực tiếp `glaciologist Dr. Amara Osei` làm chủ ngữ → Chọn D.',
            'Cảnh giác bẫy Sở Hữu Cách (Possessive Trap): `Person’s + Noun` thì chủ ngữ thật là `Noun`, KHÔNG phải `Person`! Luôn kiểm tra danh từ làm chủ ngữ thật ngay sau dấu phẩy có thực hiện được hành động V-ing ở đầu câu không!',
            [
                ('Possessive Subject Trap', 'Chủ ngữ ngữ pháp là "resulting dataset" (sở hữu của Dr. Osei) — một tập dữ liệu không thể trải qua 4 mùa đông hiệu chỉnh phao!'),
                ('Passive Dangling Modifier', 'Đưa "unexpected subglacial meltwater channels" làm chủ ngữ khiến câu mang nghĩa các dòng nước tan đã đi hiệu chỉnh phao.'),
                ('Inanimate Subject Trap', 'Chủ ngữ là "the acoustic measurements" — số đo không thể tự hiệu chỉnh phao suốt 4 mùa đông.'),
                ('Đáp án đúng', 'Đặt trực tiếp "glaciologist Dr. Amara Osei" làm chủ ngữ của mệnh đề chính, khớp hoàn hảo chủ thể của hành động "Having spent...".'),
            ]
        ),

        # Q9 — Form, Structure, and Sense (Possessive plural/singular + apostrophe two-noun trap) -> A
        q_item(
            'sat_boss_d4_q9', 9, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>In her monograph on Renaissance textile workshops, historian Isabel Vasquez demonstrates that the two rival ______ frequently overlapped along shared riverfront dyeing districts despite strict municipal zoning charters.</p>',
            sec_stem,
            [
                'guilds’ supply networks',
                'guild’s supply networks',
                'guilds’ supply network’s',
                'guilds supply networks’'
            ],
            'A',
            'Kiểm tra quy tắc dấu nháy đơn (Apostrophe) trên cặp 2 danh từ: (1) Danh từ thứ nhất đi sau "the two rival" (HAI phường hội đối địch → SỐ NHIỀU) và làm chủ sở hữu của "supply networks" → bắt buộc là sở hữu cách số nhiều `guilds’` (nháy đơn sau chữ `s`). (2) Danh từ thứ hai `networks` đứng ngay trước động từ chính `overlapped` (không sở hữu thứ gì phía sau) → chỉ là danh từ số nhiều thường `networks` (KHÔNG dấu nháy đơn) → Chọn A.',
            'Quy tắc kiểm tra cặp danh từ có dấu nháy đơn: (1) Đếm số lượng sở hữu (two → plural `s’`), (2) Kiểm tra danh từ ngay trước động từ chính: nó là chủ ngữ chứ không sở hữu động từ, nên CẤM có dấu nháy đơn!',
            [
                ('Đáp án đúng', 'Sở hữu cách số nhiều "guilds’" khớp cụm "the two rival", đi kèm danh từ số nhiều không dấu nháy "supply networks" làm chủ ngữ cho "overlapped".'),
                ('Singular vs. Plural Possessive', '"guild’s" là sở hữu cách số ít, mâu thuẫn trực tiếp với số đếm "the two rival".'),
                ('Phantom Apostrophe Trap', 'Đặt thừa dấu nháy ở "network’s" dù ngay sau đó là động từ "overlapped" chứ không có danh từ bị sở hữu.'),
                ('Inverted Apostrophe Trap', 'Thiếu dấu sở hữu ở "guilds" nhưng lại gắn nhầm dấu sở hữu vào "networks’" trước động từ.'),
            ]
        ),

        # Q10 — Form, Structure, and Sense (Finite vs. non-finite verb + distant head subject + dash closure) -> C
        q_item(
            'sat_boss_d4_q10', 10, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite 750+',
            '<p>A suite of newly decoded limestone ostraca unearthed near the ancient copper mines of Timna—inscriptions that itemize weekly grain rations, bronze chisel repairs, and shift rotations for seasonal ______ a remarkably bureaucratic labor organization operating more than three thousand years ago.</p>',
            sec_stem,
            [
                'workers—documenting',
                'workers—to document',
                'workers—documents',
                'workers—document'
            ],
            'C',
            'Siêu combo 3 trong 1 (Dash Closure + Finite Verb + Distant SVA): Cả 4 đáp án đều có dấu gạch ngang đóng `workers—`, nhưng câu cần một ĐỘNG TỪ CHÍNH CHIA THÌ (Finite Verb) ngay sau dấu đóng để hoàn thành câu → loại ngay dạng không chia thì `documenting` (A) và `to document` (B) vì tạo thành Fragment! Giữa `documents` (C) và `document` (D), truy ngược 28 từ về chủ ngữ lõi (head noun) trước giới từ `of`: `A suite` (SỐ ÍT — đừng bị bẫy bởi các danh từ số nhiều `ostraca`, `mines`, `inscriptions`, `workers`!) → Chọn `workers—documents` (C)!',
            'Áp dụng 2 bước thần tốc cho câu siêu dài: (1) Gạch toàn bộ cụm `of...` và `—...—` để tìm CHỦ NGỮ LÕI (`A suite` = số ít); (2) Đảm bảo điền ĐỘNG TỪ CHIA THÌ (không phải V-ing / to-V) khớp số của chủ ngữ lõi!',
            [
                ('Non-Finite Fragment Trap', 'V-ing ("documenting") không thể làm động từ chính cho chủ ngữ "A suite" → cả câu thành Fragment.'),
                ('Infinitive Fragment Trap', 'To-V ("to document") không phải động từ chia thì → câu thiếu động từ chính.'),
                ('Đáp án đúng', 'Đóng dấu gạch ngang và cung cấp động từ chia thì số ít "documents" khớp tuyệt đối với chủ ngữ lõi số ít "A suite".'),
                ('Decoy Plural SVA Trap', 'Động từ số nhiều "document" chia nhầm theo các danh từ gây nhiễu (ostraca, inscriptions, workers) thay vì chủ ngữ lõi "A suite".'),
            ]
        ),

        # Q11 — Transitions (Elite nuance: In fact vs. Indeed — contradicting assumption vs. confirming!) -> D
        q_item(
            'sat_boss_d4_q11', 11, 'Expression of Ideas', 'Transitions', 'Elite 750+',
            '<p>Early mid-twentieth-century bathymetric cartographers hypothesized that the submerged Lomonosov Ridge beneath the central Arctic Ocean had formed entirely from volcanic lava erupting along a mid-ocean rift. ______ deep-sea sediment cores recovered in 2004 revealed ancient continental granite and freshwater microfossils, proving that the ridge is a sliver of Eurasia torn away by plate tectonics.</p>',
            trans_stem,
            [
                'Indeed,',
                'Consequently,',
                'Similarly,',
                'In fact,'
            ],
            'D',
            'Cặp bẫy sắc thái bậc 750+: **`In fact,`** vs. **`Indeed,`**. Câu 1 nêu một giả thuyết SAI LẦM cũ ("hypothesized that... formed entirely from volcanic lava"). Câu 2 đưa bằng chứng bác bỏ giả thuyết đó bằng sự thật ngược lại ("a sliver of Eurasia" — đá hoa cương lục địa chứ không phải dung nham núi lửa!). Khi dùng để ĐÍNH CHÍNH / PHỦ NHẬN một nhận định sai ở câu trước (mang nghĩa "trên thực tế thì..."), chỉ **`In fact,`** chuẩn xác; còn **`Indeed,`** chỉ dùng để XÁC NHẬN hoặc NHẤN MẠNH THÊM tính đúng đắn của câu trước — dùng ở đây sẽ gây mâu thuẫn logic trực diện → Chọn D.',
            'Phân biệt cặp vàng 750+: `Indeed` = khẳng định/củng cố ý đúng của câu trước; `In fact` = có thể dùng để lật ngược/đính chính một giả thuyết sai ở câu trước ("trên thực tế thì ngược lại")!',
            [
                ('Nuance Trap (Confirm vs. Correct)', '"Indeed" xác nhận/tăng cường câu liền trước — sai hoàn toàn vì câu 2 bác bỏ giả thuyết dung nham ở câu 1.'),
                ('False Cause-Effect', 'Việc lõi trầm tích chứa đá hoa cương lục địa không phải là kết quả sinh ra từ giả thuyết sai của giới bản đồ học đáy biển.'),
                ('False Similarity', 'Câu 2 lật ngược chứ không nêu hiện tượng tương đồng với câu 1.'),
                ('Đáp án đúng', '"In fact" dẫn nhập chuẩn xác thực tế đính chính lại giả thuyết sai lầm ("hypothesized that...") ở câu trước.'),
            ]
        ),

        # Q12 — Transitions (Elite nuance: Nevertheless vs. Granted — rebuttal after concession!) -> B
        q_item(
            'sat_boss_d4_q12', 12, 'Expression of Ideas', 'Transitions', 'Elite 750+',
            '<p>Admittedly, retrofitting historic masonry warehouses with vacuum-insulated glazing requires custom mullion fabrication and entails considerably higher upfront costs than installing conventional storm windows. ______ building-envelope simulations indicate that the ultra-thin glass panels cut annual heating losses by nearly 60 percent without altering a facade’s protected architectural profile.</p>',
            trans_stem,
            [
                'Granted,',
                'Nevertheless,',
                'Specifically,',
                'Likewise,'
            ],
            'B',
            'Cặp bẫy sắc thái bậc 750+: **`Nevertheless,`** vs. **`Granted,`**. Đọc kỹ từ khóa đầu câu 1: **`Admittedly,`** đã thực hiện bước NHƯỢNG BỘ nhược điểm (chế tạo khung riêng, chi phí ban đầu cao hơn hẳn). Do đó câu 2 chuyển sang vế PHẢN BÁC / BÙ ĐẮP CHÍNH (dù tốn kém ban đầu nhưng giảm gần 60% thất thoát nhiệt mà vẫn giữ nguyên mặt tiền di sản). Ta cần từ nối chuyển hướng vượt qua sự nhượng bộ → **`Nevertheless,`** (B)! Bẫy cực hiểm là **`Granted,`** (A): `Granted` đồng nghĩa với `Admittedly` (mở ra một sự nhượng bộ mới), nên đặt vào câu 2 sẽ làm đảo lộn chiều lập luận!',
            'Nhớ cặp cộng sinh bất di bất dịch: Câu 1 có `Admittedly / Granted / To be sure` (Nhượng bộ nhược điểm) → Câu 2 PHẢI là `Nevertheless / Nonetheless / Still / Even so` (Đảo chiều khẳng định lợi ích chính)!',
            [
                ('Reversed Concession Trap', '"Granted" dùng để NHƯỢNG BỘ (cùng chức năng với "Admittedly" ở câu 1), không dùng để đảo chiều sang luận điểm chính ở câu 2.'),
                ('Đáp án đúng', '"Nevertheless" (tuy nhiên / bất chấp điều đó) tạo nhịp chuyển chuẩn xác từ nhược điểm đã thừa nhận sang lợi thế vượt trội ở câu 2.'),
                ('False Specification', 'Câu 2 không nêu ví dụ cụ thể về chi phí cao hay việc chế tạo khung ở câu 1.'),
                ('False Addition', 'Câu 2 đối lập (ưu điểm vs. nhược điểm) chứ không bổ sung thêm một nhược điểm tương tự.'),
            ]
        ),

        # Q13 — Transitions (Elite nuance: Specifically vs. Consequently — specification vs. cause-effect!) -> A
        q_item(
            'sat_boss_d4_q13', 13, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>In her archival audit of seventeenth-century Venetian shipping syndicates, economic historian Dr. Giulia Conti uncovered a subtle bookkeeping device that shielded merchants from sudden investor panic after coastal storms. ______ partnerships logged hull repairs as long-term vessel upgrades on separate capital ledgers rather than expensing them immediately against a single voyage’s net return.</p>',
            trans_stem,
            [
                'Specifically,',
                'Consequently,',
                'By contrast,',
                'Meanwhile,'
            ],
            'A',
            'Cặp bẫy sắc thái bậc 750+: **`Specifically,`** vs. **`Consequently,`**. Câu 1 giới thiệu khái quát "a subtle bookkeeping device" (một thủ thuật sổ sách tinh vi). Câu 2 mô tả CHÍNH THỦ THUẬT ĐÓ vận hành ra sao (ghi chi phí sửa thân tàu thành nâng cấp dài hạn vào sổ vốn riêng thay vì trừ thẳng vào lãi chuyến đi). Đây là quan hệ **Khái quát → Chi tiết hóa** (General → Specific), hoàn toàn KHÔNG phải nhân–quả (việc ghi sổ đó KHÔNG xảy ra do hệ quả từ nghiên cứu của Dr. Conti!) → Chọn **`Specifically,`** (A).',
            'Kiểm tra mũi tên thời gian để tách `Specifically` khỏi `Consequently`: nếu câu 2 chỉ GIẢI THÍCH / MỔ XẺ một danh từ khái quát ở câu 1 ("a device", "a strategy", "a mechanism"), chọn `Specifically`!',
            [
                ('Đáp án đúng', '"Specifically" báo hiệu chính xác câu 2 đang cụ thể hóa thủ thuật sổ sách ("bookkeeping device") vừa được nhắc khái quát ở câu 1.'),
                ('False Cause-Effect Trap', 'Việc các hội thương nhân thế kỷ 17 ghi sổ như vậy KHÔNG phải hệ quả của việc Dr. Conti phát hiện ra nó hay của việc tránh hoảng loạn — chính nó LÀ thủ thuật đó.'),
                ('False Contrast', 'Không hề có sự đối lập giữa câu 1 và câu 2.'),
                ('False Simultaneity', 'Câu 2 đi sâu giải thích cơ chế của câu 1 chứ không kể một sự việc song song diễn ra cùng lúc.'),
            ]
        ),

        # Q14 — Rhetorical Synthesis #1 (Multi-constraint: 3 factually true distractors failing 1 exact constraint) -> C
        q_item(
            'sat_boss_d4_q14', 14, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite 750+',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Both the glacier lanternfish (<i>Benthosema glaciale</i>) and the Pacific blackdragon (<i>Idiacanthus antrostomus</i>) generate bioluminescence through luciferin-luciferase reactions in specialized photophores.</li>
              <li>The glacier lanternfish typically inhabits ocean depths of 300 to 800 meters.</li>
              <li>It emits downward light along its underside to match dim surface sunlight, camouflaging its silhouette from predators below (a defense called counter-illumination).</li>
              <li>The Pacific blackdragon typically inhabits depths of 500 to 2,000 meters.</li>
              <li>It dangles a glowing chin barbel to lure smaller crustaceans and fish within striking range.</li>
              <li>Adult glacier lanternfish rarely exceed 10 centimeters in length, whereas female Pacific blackdragons can grow up to 48 centimeters long.</li>
            </ul>''',
            'The student wants to contrast the ecological functions of bioluminescence in the glacier lanternfish and the Pacific blackdragon while specifying the typical ocean depth range of each species. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Whereas the glacier lanternfish uses downward bioluminescence at depths of 300 to 800 meters to camouflage its silhouette from predators below, the Pacific blackdragon employs a glowing chin barbel to lure prey within striking range.',
                'Although both species produce bioluminescence via luciferin-luciferase reactions, the glacier lanternfish inhabits depths of 300 to 800 meters and rarely exceeds 10 centimeters, whereas the Pacific blackdragon occupies depths of 500 to 2,000 meters and can reach 48 centimeters.',
                'Found at depths of 300 to 800 meters, the glacier lanternfish uses ventral bioluminescence to camouflage its silhouette from predators below; by contrast, the Pacific blackdragon, which inhabits depths of 500 to 2,000 meters, uses a glowing chin barbel to lure prey.',
                'Both the glacier lanternfish, which typically lives between 300 and 800 meters deep, and the Pacific blackdragon rely on chemical reactions in specialized photophores to generate bioluminescent light.'
            ],
            'C',
            'Cả 4 đáp án đều ĐÚNG SỰ THẬT 100%, nên phải dùng bảng kiểm 3 ràng buộc của đề: [1] Đối chiếu chức năng sinh thái của phát quang ở CẢ HAI loài (ngụy trang tránh kẻ thù vs. nhử mồi), [2] Nêu độ sâu đặc trưng của loài 1 (300–800 m), [3] Nêu độ sâu đặc trưng của loài 2 (500–2,000 m). A đạt [1]+[2] nhưng THIẾU độ sâu của Pacific blackdragon! B đạt [2]+[3] nhưng lại đối chiếu chiều dài cơ thể (10 cm vs. 48 cm) thay vì chức năng sinh thái của phát quang! D chỉ nêu cơ chế hóa học chung và thiếu cả chức năng lẫn độ sâu loài 2. Duy nhất C hoàn thành 3/3 ràng buộc → Chọn C.',
            'Với Rhetorical Synthesis bậc 750+, đừng chọn vội ngay khi thấy câu "đúng notes & có từ contrast"! Hãy tách đề thành checklist đánh số [1], [2], [3] và gạch từng lựa chọn thiếu dù chỉ 1 mảnh nhỏ!',
            [
                ('Missing 1 Constraint (Depth #2)', 'Đúng sự thật và đối chiếu được 2 chức năng, nhưng bỏ sót dải độ sâu 500–2,000 m của loài Pacific blackdragon.'),
                ('Wrong Contrast Dimension', 'Đúng sự thật và đủ độ sâu cả hai loài, nhưng đối chiếu kích thước cơ thể (10 cm vs. 48 cm) thay vì chức năng sinh thái của phát quang.'),
                ('Đáp án đúng', 'Hoàn thành trọn vẹn cả 3 yêu cầu: đối chiếu chức năng (ngụy trang vs. nhử mồi) và nêu chính xác dải độ sâu của cả hai loài.'),
                ('Similarity Instead of Contrast', 'Nhấn mạnh điểm giống nhau về phản ứng hóa học luciferin-luciferase thay vì đối chiếu chức năng sinh thái và thiếu độ sâu loài 2.'),
            ]
        ),

        # Q15 — Rhetorical Synthesis #2 (Multi-constraint with BOTH positive AND negative constraints!) -> D
        q_item(
            'sat_boss_d4_q15', 15, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite 750+',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Traditional tree-ring dating (dendrochronology) infers past volcanic eruptions by identifying unusually narrow annual growth rings caused by cold summers.</li>
              <li>Because severe localized droughts can also produce narrow rings, ring width alone cannot reliably separate regional dry spells from global volcanic winters.</li>
              <li>In 2024, paleoclimatologist Dr. Tomas Novak studied microscopic unlignified wood cells—called "blue rings"—in ancient subalpine pines from the Carpathian Mountains.</li>
              <li>Blue rings develop only when abrupt late-summer frosts halt cell-wall hardening, a thermal shock strongly tied to stratospheric volcanic ash rather than moisture deficits.</li>
              <li>Using blue-ring analysis, Novak corroborated a previously disputed volcanic cooling episode in 1453 CE.</li>
            </ul>''',
            'The student wants to explain how Dr. Tomas Novak’s 2024 technique overcomes a limitation of traditional tree-ring dating, without naming any mountain range or the specific historical eruption year that Novak corroborated. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Because narrow tree rings can stem from either localized droughts or volcanic cooling, Dr. Tomas Novak’s 2024 analysis of ancient pines in the Carpathian Mountains instead tracks unlignified "blue rings," which form specifically during abrupt frost shocks caused by volcanic ash.',
                'In 2024, paleoclimatologist Dr. Tomas Novak analyzed microscopic unlignified wood cells called "blue rings," which develop when sudden late-summer frosts interrupt cell-wall hardening during volcanic ash events.',
                'Overcoming the inability of traditional narrow-ring measurements to distinguish localized droughts from volcanic winters, Dr. Tomas Novak’s 2024 frost-sensitive "blue ring" technique corroborated a disputed volcanic cooling episode in 1453 CE.',
                'Because traditional narrow-ring dating cannot reliably separate regional droughts from volcanic winters, Dr. Tomas Novak’s 2024 technique instead examines microscopic "blue rings"—unlignified cells triggered specifically by abrupt frost shocks linked to stratospheric volcanic ash.'
            ],
            'D',
            'Đề kết hợp CẢ ràng buộc khẳng định LẪN ràng buộc phủ định (Positive + Negative Constraints): [1] Nêu hạn chế của phương pháp vòng năm truyền thống (không tách được hạn hán cục bộ khỏi mùa đông núi lửa), [2] Giải thích kỹ thuật năm 2024 của Dr. Novak khắc phục bằng "blue rings" ra sao, [3] CẤM nhắc tên dãy núi cụ thể ("Carpathian Mountains"), [4] CẤM nhắc năm lịch sử cụ thể ("1453 CE"). Cả 4 đáp án đều đúng sự thật 100%, nhưng: A dính tên dãy núi "Carpathian Mountains" (vi phạm [3]); B bỏ quên hoàn toàn hạn chế của vòng năm truyền thống (vi phạm [1]); C dính năm lịch sử "1453 CE" (vi phạm [4]). Duy nhất D vượt qua toàn bộ 4 cổng kiểm duyệt → Chọn D.',
            'Khi đề Rhetorical Synthesis có cụm "without referencing / without focusing on...", hãy quét mắt gạch NGAY các từ cấm trong 4 đáp án chỉ trong 3 giây trước khi xét chi tiết ràng buộc khẳng định!',
            [
                ('Violates Negative Constraint (Mountain)', 'Giải thích đúng cơ chế khắc phục nhưng nhắc trực tiếp "the Carpathian Mountains" — vi phạm lệnh cấm nhắc tên dãy núi.'),
                ('Missing Positive Constraint (Limitation)', 'Tránh được từ cấm nhưng không hề giải thích hạn chế của phương pháp đo độ rộng vòng năm truyền thống (nhầm lẫn với hạn hán).'),
                ('Violates Negative Constraint (Year)', 'Trình bày tốt hạn chế và giải pháp nhưng nhắc cụ thể năm lịch sử "1453 CE" — vi phạm lệnh cấm.'),
                ('Đáp án đúng', 'Đáp ứng trọn vẹn cả 2 vế khẳng định (hạn chế vòng hẹp + cơ chế khắc phục bằng "blue rings") lẫn 2 lệnh cấm (không nhắc dãy núi hay năm lịch sử).'),
            ]
        ),
    ]

    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': title,
            'subtitle': '15 câu Boss Grammar & Expression of Ideas 750–800: đồng vị ngữ lồng nhau, Super-Semicolon, bẫy False Colon, đảo ngữ SVA siêu dài, cặp Transitions sát nghĩa và Synthesis đa ràng buộc.',
            'difficultyBadge': 'Hard M2 Boss • 750–800',
            'targetTimeMinutes': 22,
        },
        'drillModule': {
            'id': 'sat_boss_drill_4_mod',
            'title': 'R&W Boss Drill 4: Nested Hard Grammar Combos, Transitions & Synthesis',
            'timeLimitMinutes': 22,
            'questions': questions,
        },
    }


def get_drills():
    d3 = get_boss_drill_3()
    d4 = get_boss_drill_4()
    return [
        ('boss_drill_3', d3['basicInfo']['title'], 3, d3),
        ('boss_drill_4', d4['basicInfo']['title'], 4, d4),
    ]


if __name__ == '__main__':
    from sat_qa_validator import validate_sat_test

    drills = get_drills()
    all_errors = []
    for key, title, order_idx, cj in drills:
        errs = validate_sat_test(cj, key)
        qs = cj['drillModule']['questions']
        if len(qs) != 15:
            errs.append(f"[{key}] Expected 15 questions, got {len(qs)}")
        counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        expected_prefix = 'sat_boss_d3_q' if key == 'boss_drill_3' else 'sat_boss_d4_q'
        for idx, q in enumerate(qs, 1):
            if q['id'] != f'{expected_prefix}{idx}':
                errs.append(f"[{key}] Bad ID at Q{idx}: {q['id']}")
            if q['difficulty'] not in ('Hard', 'Elite 750+'):
                errs.append(f"[{key}] Bad difficulty at Q{idx}: {q['difficulty']}")
            counts[q['correctAnswer']] += 1
        if sorted(counts.values()) != [3, 4, 4, 4]:
            errs.append(f"[{key}] Answer keys not strictly (4,4,4,3): {counts}")
        print(f"Checked {key} (order={order_idx}, Qs={len(qs)}, keys={counts}): {len(errs)} errors")
        all_errors.extend(errs)

    if all_errors:
        for e in all_errors:
            print("ERROR:", e)
        sys.exit(1)

    print("BOSS R&W DRILLS 3 & 4 (30 ELITE Qs) QA PASSED!")
