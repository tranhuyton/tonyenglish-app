import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# TOPIC B11: Gas exchange and respiration
# ==============================================================================
async def build_b11():
    lid = '39003a2f-708e-47fe-b8ad-7aae073273a3'
    code = 'b11'
    title = 'B11: Gas exchange and respiration'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 50px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 50px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-gas-exchange-surfaces" class="lecture-interactive-card" data-lecture-section="sec_gas_exchange_surfaces" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-respiratory-system" class="lecture-interactive-card" data-lecture-section="sec_respiratory_system" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-ventilation-mechanics" class="lecture-interactive-card" data-lecture-section="sec_ventilation_mechanics" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B11 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B11: Hệ Hô hấp & Trao đổi Khí ở Người",
            "selector": "#sec-header",
            "en": "Welcome to Topic B11: Gas exchange and respiration. Aerobic organisms require rapid gas exchange to deliver oxygen to metabolizing cells. In this lesson, we study the essential structural adaptations of gas exchange surfaces, map respiratory anatomy from trachea to alveoli, and analyze ventilation biomechanics.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B11: Hệ Hô hấp và Trao đổi Khí ở Người. Các sinh vật hiếu khí đòi hỏi bề mặt trao đổi khí hiệu quả để cung cấp oxy liên tục cho tế bào. Trong bài học này, chúng ta sẽ khảo sát các đặc điểm thích nghi của bề mặt trao đổi khí, giải phẫu đường dẫn khí và phế nang, cùng cơ chế thông khí phổi."
        },
        {
            "id": "sec_gas_exchange_surfaces",
            "title": "1. Đặc điểm Thích nghi của Bề mặt Trao đổi Khí",
            "selector": "#sec-gas-exchange-surfaces",
            "en": "Section 1 details alveolar adaptations: Gas exchange surfaces must maximize diffusion rate by satisfying Fick's law: A large surface area provided by hundreds of millions of alveoli; extremely thin walls only one epithelial cell thick to minimize diffusion distance; a thin film of moisture lining alveolar walls so oxygen dissolves before diffusing; and a dense surrounding capillary network coupled with continuous ventilation to maintain steep concentration gradients for oxygen and carbon dioxide.",
            "vi": "Mục một chi tiết hóa các đặc tính thích nghi của phế nang: Bề mặt trao đổi khí tối đa hóa tốc độ khuếch tán theo định luật Fick: Diện tích tiếp xúc khổng lồ từ hàng trăm triệu phế nang; vách phế nang và thành mao mạch cực mỏng chỉ dày một lớp tế bào biểu mô giúp tối thiểu hóa khoảng cách khuếch tán; lớp màng ẩm mỏng lót mặt trong phế nang giúp khí oxy hòa tan trước khi khuếch tán; và mạng lưới mao mạch máu dày đặc bao quanh kết hợp với sự thông khí liên tục để duy trì độ dốc gradient nồng độ cao cho O2 và CO2."
        },
        {
            "id": "sec_respiratory_system",
            "title": "2. Cấu trúc Giải phẫu Hệ Hô hấp Người",
            "selector": "#sec-respiratory-system",
            "en": "Section 2 maps human respiratory anatomy: Air enters via the nasal cavity, passes through the larynx into the trachea, which is reinforced by C-shaped rings of cartilage that prevent airway collapse during pressure drops. The trachea bifurcates into two bronchi, branching into narrower bronchioles that terminate in clusters of microscopic alveoli. Goblet cells secrete sticky mucus to trap inhaled dirt and microbes, while ciliated epithelial cells beat rhythmically to propel mucus upward toward the throat.",
            "vi": "Mục hai khảo sát giải phẫu hệ hô hấp: Không khí đi qua khoang mũi, qua thanh quản vào khí quản được gia cố bởi các vòng sụn hình chữ C giúp đường dẫn khí không bị xẹp khi áp suất lồng ngực giảm. Khí quản chia thành hai phế quản chính dẫn vào hai lá phổi, phân nhánh thành các tiểu phế quản nhỏ và tận cùng bằng các chùm phế nang vi thể. Các tế bào hình đài tiết chất nhầy dính bẫy giữ bụi bẩn và vi sinh vật, trong khi các tế bào biểu mô có lông rung quét liên tục đẩy dịch nhầy lên hầu họng để nuốt hoặc khạc ra ngoài."
        },
        {
            "id": "sec_ventilation_mechanics",
            "title": "3. Cơ chế Thông khí: Hít vào & Thở ra (Ventilation Mechanics)",
            "selector": "#sec-ventilation-mechanics",
            "en": "Section 3 investigates ventilation mechanics: During Inhalation, external intercostal muscles contract pulling the ribcage upwards and outwards, while the diaphragm contracts and flattens downwards; thoracic volume expands, decreasing internal pulmonary pressure below atmospheric, drawing air inward. During Exhalation, external intercostals relax and internal intercostals contract, dropping ribs downwards and inwards, while the diaphragm relaxes into a dome shape; thoracic volume decreases, increasing pressure and expelling air. Inspired air contains 21% oxygen and 0.04% carbon dioxide; Expired air contains roughly 16% oxygen and 4% carbon dioxide, which turns limewater cloudy milk white.",
            "vi": "Mục ba nghiên cứu cơ chế thông khí phổi: Khi Hít vào, cơ liên sườn ngoài co nâng lồng ngực lên trên và ra ngoài, đồng thời cơ hoành co phẳng xuống dưới; thể tích khoang ngực tăng lên làm áp suất trong phổi giảm thấp hơn áp suất khí quyển, hút không khí tràn vào phổi. Khi Thở ra, cơ liên sườn ngoài giãn, xương sườn hạ xuống, cơ hoành giãn cong lồi lên hình vòm; thể tích lồng ngực thu nhỏ làm tăng áp suất tống khí ra ngoài. Khí hít vào chứa 21% oxy và 0.04% CO2; khí thở ra chứa khoảng 16% oxy và 4% CO2, làm đục nước vôi trong nhanh chóng."
        }
    ]

    major_sections = [
        {"id": "sec_gas_exchange_surfaces", "title": "1. Đặc điểm Bề mặt Trao đổi Khí"},
        {"id": "sec_respiratory_system", "title": "2. Cấu trúc Giải phẫu Hệ Hô hấp"},
        {"id": "sec_ventilation_mechanics", "title": "3. Cơ chế Thông khí Hít vào & Thở ra"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B11 successfully built!")


# ==============================================================================
# TOPIC B12: Respiration
# ==============================================================================
async def build_b12():
    lid = '58e65add-a67a-4b90-8b84-52de1a2840be'
    code = 'b12'
    title = 'B12: Respiration'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 50px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 50px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-bioenergetics" class="lecture-interactive-card" data-lecture-section="sec_bioenergetics" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-aerobic-respiration" class="lecture-interactive-card" data-lecture-section="sec_aerobic_respiration" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-anaerobic-respiration" class="lecture-interactive-card" data-lecture-section="sec_anaerobic_respiration" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B12 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B12: Năng lượng Sinh học & Hô hấp Tế bào",
            "selector": "#sec-header",
            "en": "Welcome to Topic B12: Respiration. Cellular respiration is the master biochemical energy engine of all living organisms. In this lesson, we define bioenergetic ATP usage, contrast aerobic and anaerobic pathways, examine lactic acid production and oxygen debt in human muscles, and explore industrial yeast fermentation.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B12: Năng lượng Sinh học và Hô hấp Tế bào. Hô hấp tế bào là động cơ hóa sinh cung cấp năng lượng cho mọi hoạt động sống. Trong bài học này, chúng ta sẽ khảo sát vai trò của đồng tiền năng lượng ATP, so sánh hô hấp hiếu khí và kỵ khí, cơ chế tích tụ axit lactic và nợ oxy ở cơ bắp, cùng ứng dụng lên men của nấm men."
        },
        {
            "id": "sec_bioenergetics",
            "title": "1. Khái niệm Hô hấp Tế bào & Đồng tiền Năng lượng ATP",
            "selector": "#sec-bioenergetics",
            "en": "Section 1 defines Respiration: the chemical reactions in cells that break down nutrient molecules and release energy for metabolism. Unlike ventilation which is physical breathing, respiration is an intracellular enzymatic chemical reaction. Living organisms utilize the released ATP energy for muscle contraction, active transport across membranes, protein synthesis, cell division, nerve impulse conduction, and homeostatic thermoregulation.",
            "vi": "Mục một định nghĩa Hô hấp Tế bào: là chuỗi phản ứng sinh hóa diễn ra bên trong tế bào bẻ gãy các phân tử dinh dưỡng để giải phóng năng lượng cho các hoạt động chuyển hóa. Khác với sự thông khí phổi chỉ là động tác cơ học, hô hấp là phản ứng enzym nội bào. Năng lượng ATP giải phóng được tế bào sử dụng cho sự co cơ, vận chuyển chủ động qua màng, tổng hợp protein, phân chia tế bào, dẫn truyền xung thần kinh và duy trì thân nhiệt ổn định."
        },
        {
            "id": "sec_aerobic_respiration",
            "title": "2. Hô hấp Hiếu khí (Aerobic Respiration)",
            "selector": "#sec-aerobic-respiration",
            "en": "Section 2 explores Aerobic Respiration: the chemical reactions in cells that use oxygen to break down nutrient molecules to release energy. The balanced chemical equation is: one molecule of glucose reacts with six molecules of oxygen to produce six molecules of carbon dioxide and six molecules of water, liberating a high yield of approximately thirty-two ATP molecules per glucose inside mitochondria.",
            "vi": "Mục hai nghiên cứu Hô hấp Hiếu khí (Aerobic Respiration): là các phản ứng hóa sinh trong tế bào sử dụng khí oxy để oxy hóa hoàn toàn phân tử dinh dưỡng giải phóng năng lượng. Phương trình hóa học cân bằng: 1 phân tử glucose kết hợp với 6 phân tử oxy tạo ra 6 phân tử carbon dioxide và 6 phân tử nước, giải phóng lượng năng lượng rất lớn khoảng 32 phân tử ATP cho mỗi phân tử glucose diễn ra trong ty thể."
        },
        {
            "id": "sec_anaerobic_respiration",
            "title": "3. Hô hấp Kỵ khí, Axit Lactic & Nợ Oxy (Oxygen Debt)",
            "selector": "#sec-anaerobic-respiration",
            "en": "Section 3 investigates Anaerobic Respiration: releasing energy from glucose without using oxygen, yielding far less energy per glucose due to incomplete breakdown. In vigorously exercising human muscle cells when oxygen cannot reach tissues fast enough, glucose breaks down into toxic Lactic Acid, which causes muscle fatigue and cramps. The volume of oxygen required to break down accumulated lactic acid in the liver during recovery is termed the Oxygen Debt. In yeast cells, anaerobic respiration produces Ethanol and Carbon Dioxide, harnessed globally in brewing and breadmaking.",
            "vi": "Mục ba phân tích Hô hấp Kỵ khí (Anaerobic Respiration): là quá trình giải phóng năng lượng từ glucose mà không dùng oxy, tạo ra ít năng lượng hơn do phân tử bị bẻ gãy không hoàn toàn. Ở tế bào cơ người khi vận động cường độ cao mà máu không cung cấp đủ oxy, glucose chuyển hóa thành Axit Lactic gây mỏi cơ và chuột rút. Lượng oxy cần thiết sau vận động để oxy hóa sạch axit lactic tại gan được gọi là Hiện tượng Nợ Oxy (Oxygen Debt). Ở tế bào nấm men, hô hấp kỵ khí tạo ra Cồn Ethanol và khí CO2, được ứng dụng rộng rãi trong nấu bia và làm bánh mì nở xốp."
        }
    ]

    major_sections = [
        {"id": "sec_bioenergetics", "title": "1. Khái niệm Hô hấp Tế bào & ATP"},
        {"id": "sec_aerobic_respiration", "title": "2. Hô hấp Hiếu khí (Aerobic Respiration)"},
        {"id": "sec_anaerobic_respiration", "title": "3. Hô hấp Kỵ khí & Nợ Oxy (Oxygen Debt)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B12 successfully built!")


# ==============================================================================
# TOPIC B13: Coordination and response
# ==============================================================================
async def build_b13():
    lid = '2637d6ee-fd5f-48fc-aa7a-fc794fb3e561'
    code = 'b13'
    title = 'B13: Coordination and response'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 50px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 50px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-nervous-reflex" class="lecture-interactive-card" data-lecture-section="sec_nervous_reflex" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-endocrine-system" class="lecture-interactive-card" data-lecture-section="sec_endocrine_system" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-homeostasis" class="lecture-interactive-card" data-lecture-section="sec_homeostasis" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B13 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B13: Điều hòa, Phản xạ & Cân bằng Nội môi",
            "selector": "#sec-header",
            "en": "Welcome to Topic B13: Coordination and response. Survival hinges on rapid detection and adaptive responses to stimuli. In this topic, we examine the nervous system and the five-component reflex arc, compare electrical and hormonal communication, and master homeostatic thermoregulation via negative feedback.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B13: Điều hòa, Phản xạ và Cân bằng Nội môi. Sự sinh tồn của sinh vật dựa vào khả năng phát hiện và đáp ứng thích nghi trước các kích thích. Trong bài học này, chúng ta sẽ khảo sát hệ thần kinh và cung phản xạ 5 khâu, so sánh dẫn truyền xung thần kinh và hormone, cùng cơ chế điều hòa thân nhiệt qua phản hồi âm tính."
        },
        {
            "id": "sec_nervous_reflex",
            "title": "1. Hệ Thần kinh & Cung Phản xạ Tủy sống (Reflex Arc)",
            "selector": "#sec-nervous-reflex",
            "en": "Section 1 outlines the nervous system: The Central Nervous System comprises the brain and spinal cord, connected to receptors and effectors by peripheral nerves. A Reflex action is an automatic, rapid, and protective response to a stimulus without conscious cerebral thought. The reflex arc consists of five components: Receptor detects stimulus; Sensory neurone conducts impulses to CNS; Relay neurone in spinal cord gray matter integrates signal across synaptic gaps using neurotransmitter chemicals; Motor neurone transmits impulses outward; Effector muscle or gland executes the response.",
            "vi": "Mục một khái quát hệ thần kinh: Hệ thần kinh trung ương gồm não bộ và tủy sống, liên lạc với các cơ quan thụ cảm và đáp ứng qua các dây thần kinh ngoại biên. Phản xạ (Reflex action) là phản ứng nhanh chóng, tự động và mang tính bảo vệ cơ thể trước kích thích mà không cần suy nghĩ ý thức từ vỏ não. Cung phản xạ gồm 5 khâu tuần tự: Thụ quan tiếp nhận kích thích; Nơron cảm giác dẫn truyền xung thần kinh vào tủy sống; Nơron trung gian trong chất xám tích hợp tín hiệu qua khe synapse bằng chất dẫn truyền hóa học; Nơron vận động truyền xung ra ngoài; Cơ quan đáp ứng (cơ hoặc tuyến) thực hiện co cơ hoặc tiết dịch."
        },
        {
            "id": "sec_endocrine_system",
            "title": "2. Tuyến Nội tiết, Hormone & Phản ứng Sinh tồn (Adrenaline)",
            "selector": "#sec-endocrine-system",
            "en": "Section 2 investigates the endocrine system: A Hormone is a chemical substance produced by an endocrine gland, carried by blood plasma, which alters the activity of specific target organs. Compared to nervous impulses which are rapid and short-lived, hormonal control is slower but longer-lasting. Adrenaline, secreted by adrenal glands during fear or stress, triggers fight-or-flight responses: increasing heart rate, dilating bronchioles and pupils, and stimulating liver glycogen breakdown into glucose to supply fuel for emergency muscle exertion.",
            "vi": "Mục hai nghiên cứu hệ nội tiết: Hormone là chất hóa học do tuyến nội tiết tiết trực tiếp vào huyết tương, làm biến đổi hoạt động sinh lý của các cơ quan đích đặc hiệu. So với xung thần kinh truyền điện thế nhanh và thoáng qua, hormone tác động chậm hơn nhưng duy trì hiệu ứng kéo dài. Adrenaline do tủy tuyến thượng thận tiết ra khi sợ hãi hoặc căng thẳng, kích hoạt phản ứng chiến-hay-chạy (fight-or-flight): tăng nhịp tim và huyết áp, giãn phế quản và đồng tử, kích thích gan phân giải glycogen thành glucose cung cấp nhiên liệu khẩn cấp cho cơ bắp."
        },
        {
            "id": "sec_homeostasis",
            "title": "3. Cân bằng Nội môi & Điều hòa Thân nhiệt (Homeostasis)",
            "selector": "#sec-homeostasis",
            "en": "Section 3 details Homeostasis: the maintenance of a constant internal environment within tight physiological parameters using negative feedback. Thermoregulation stabilizes core temperature around 37 degrees Celsius. When body temperature rises, arterioles near the skin surface undergo Vasodilation, increasing cutaneous blood flow to radiate heat away, while sweat glands secrete perspiration whose evaporation cools the skin. When body temperature drops, arterioles undergo Vasoconstriction to minimize heat loss, shivering skeletal muscles generate metabolic heat, and arrector pili muscles contract to erect hairs.",
            "vi": "Mục ba phân tích Cân bằng Nội môi (Homeostasis): là sự duy trì ổn định môi trường bên trong cơ thể xung quanh các giá trị sinh lý tối ưu nhờ cơ chế điều hòa ngược âm tính (negative feedback). Điều hòa thân nhiệt giữ nhiệt độ cơ thể ổn định khoảng 37 độ C. Khi thân nhiệt tăng, tiểu động mạch dưới da Giãn mạch (Vasodilation) tăng lưu lượng máu đến da để tỏa nhiệt ra ngoài, tuyến mồ hôi tiết mồ hôi bay hơi làm mát cơ thể. Khi trời lạnh, tiểu động mạch Co mạch (Vasoconstriction) hạn chế mất nhiệt, cơ xương run rẩy sinh nhiệt và cơ dựng lông co lại để giữ lớp khí cách nhiệt."
        }
    ]

    major_sections = [
        {"id": "sec_nervous_reflex", "title": "1. Hệ Thần kinh & Cung Phản xạ (Reflex Arc)"},
        {"id": "sec_endocrine_system", "title": "2. Tuyến Nội tiết & Hormone Adrenaline"},
        {"id": "sec_homeostasis", "title": "3. Cân bằng Nội môi & Điều hòa Thân nhiệt"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B13 successfully built!")


# ==============================================================================
# TOPIC B14: Drugs
# ==============================================================================
async def build_b14():
    lid = '7ed510d0-acd2-4d0a-9079-1f1e4e4fc463'
    code = 'b14'
    title = 'B14: Drugs'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-what-is-drug" class="lecture-interactive-card" data-lecture-section="sec_what_is_drug" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-antibiotics" class="lecture-interactive-card" data-lecture-section="sec_antibiotics" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-mrsa-crisis" class="lecture-interactive-card" data-lecture-section="sec_mrsa_crisis" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B14 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B14: Dược lý học, Kháng sinh & Kháng thuốc",
            "selector": "#sec-header",
            "en": "Welcome to Topic B14: Drugs. Pharmacology examines chemical substances that modify human physiology. In this lesson, we define drugs, contrast medicinal and non-medicinal substances, investigate how antibiotics selectively target bacterial pathogens without affecting human cells or viruses, and analyze the emergence of antibiotic resistance.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B14: Thuốc, Kháng sinh và Khủng hoảng Kháng thuốc. Dược lý học nghiên cứu các chất hóa học làm thay đổi phản ứng sinh lý cơ thể. Trong bài học này, chúng ta sẽ định nghĩa thuốc, cơ chế kháng sinh tiêu diệt vi khuẩn mà vô hiệu trước virus, cùng quá trình tiến hóa kháng thuốc nguy hiểm của vi khuẩn."
        },
        {
            "id": "sec_what_is_drug",
            "title": "1. Khái niệm Thuốc & Phân loại Dược chất (What is a Drug?)",
            "selector": "#sec-what-is-drug",
            "en": "Section 1 defines a Drug: any substance taken into the body that modifies or affects chemical reactions in the body. Medicinal drugs, like analgesics and antibiotics, relieve symptoms and eradicate infections under clinical supervision. Misused drugs like alcohol and tobacco depress nervous transmission or damage respiratory mucosa, leading to chemical dependency, tolerance, and organ damage.",
            "vi": "Mục một định nghĩa Thuốc (Drug): là bất kỳ chất nào đưa vào cơ thể làm thay đổi hoặc ảnh hưởng đến các phản ứng hóa sinh trong cơ thể. Thuốc chữa bệnh (Medicinal drugs) như thuốc giảm đau và kháng sinh giúp xoa dịu triệu chứng và tiêu diệt mầm bệnh theo chỉ dẫn y khoa. Các chất gây nghiện bị lạm dụng như rượu bia và thuốc lá ức chế dẫn truyền thần kinh hoặc phá hủy niêm mạc phổi, dẫn đến tình trạng lệnh thuộc thuốc, lờn thuốc và suy đa tạng."
        },
        {
            "id": "sec_antibiotics",
            "title": "2. Kháng sinh & Vì sao Kháng sinh Vô hiệu trước Virus?",
            "selector": "#sec-antibiotics",
            "en": "Section 2 investigates Antibiotics: chemical substances produced by microorganisms that kill or inhibit the growth of bacteria. Penicillin disrupts peptidoglycan cell wall cross-linking, causing bacterial cells to burst by osmotic lysis. Critically, antibiotics are completely ineffective against viruses: viruses possess no cellular structures, no cell walls, and no independent metabolic machinery of their own, reproducing solely inside host cells by hijacking host biochemical mechanisms.",
            "vi": "Mục hai nghiên cứu Thuốc Kháng sinh (Antibiotics): là các chất hóa học do vi sinh vật sản sinh có khả năng tiêu diệt hoặc ức chế sự sinh trưởng của vi khuẩn. Ví dụ kháng sinh Penicillin ngăn chặn sự liên kết ngang của thành tế bào peptidoglycan, khiến vi khuẩn trương vỡ dưới áp suất thẩm thấu. Điểm nhấn cốt lõi: Kháng sinh hoàn toàn bất lực trước virus vì virus không có cấu trúc tế bào, không có thành tế bào và không có bộ máy chuyển hóa riêng mà ký sinh bắt buộc bên trong tế bào chủ."
        },
        {
            "id": "sec_mrsa_crisis",
            "title": "3. Kháng thuốc Kháng sinh & Khủng hoảng MRSA",
            "selector": "#sec-mrsa-crisis",
            "en": "Section 3 examines Antibiotic Resistance: In any large bacterial population, random genetic mutations occasionally produce individual bacteria with resistance to specific antibiotics. When exposed to antibiotics, non-resistant bacteria perish while resistant mutants survive, reproduce rapidly via binary fission, and pass resistance genes to progeny. Overuse of antibiotics in livestock and patients who fail to complete their prescribed course accelerates this selection pressure, yielding superbugs like Methicillin-Resistant Staphylococcus aureus, or MRSA.",
            "vi": "Mục ba phân tích Kháng thuốc Kháng sinh: Trong một quần thể vi khuẩn đông đúc, các đột biến gen ngẫu nhiên tạo ra các cá thể có khả năng kháng lại một loại kháng sinh nhất định. Khi dùng kháng sinh, vi khuẩn nhạy cảm bị tiêu diệt trong khi vi khuẩn đột biến kháng thuốc sống sót, phân chia nhân đôi nhanh chóng và truyền gen kháng thuốc cho thế hệ sau. Việc lạm dụng kháng sinh trong chăn nuôi và việc bệnh nhân tự ý ngừng thuốc khi chưa hết liệu trình đã tạo áp lực chọn lọc gay gắt, sinh ra các siêu vi khuẩn đa kháng thuốc như tụ cầu vàng kháng methicillin (MRSA)."
        }
    ]

    major_sections = [
        {"id": "sec_what_is_drug", "title": "1. Khái niệm Thuốc (What is a Drug?)"},
        {"id": "sec_antibiotics", "title": "2. Cơ chế Kháng sinh & Tính Vô hiệu với Virus"},
        {"id": "sec_mrsa_crisis", "title": "3. Tiến hóa Kháng thuốc & Khủng hoảng MRSA"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B14 successfully built!")


# ==============================================================================
# TOPIC B15: Reproduction
# ==============================================================================
async def build_b15():
    lid = 'deb8222d-2b75-42a3-b454-9601fbfa1bd2'
    code = 'b15'
    title = 'B15: Reproduction'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-reproduction-modes" class="lecture-interactive-card" data-lecture-section="sec_reproduction_modes" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-flowering-plants" class="lecture-interactive-card" data-lecture-section="sec_flowering_plants" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-human-reproduction" class="lecture-interactive-card" data-lecture-section="sec_human_reproduction" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-stis-hiv" class="lecture-interactive-card" data-lecture-section="sec_stis_hiv" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B15 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B15: Sinh sản ở Thực vật & Người",
            "selector": "#sec-header",
            "en": "Welcome to Topic B15: Reproduction. Reproduction ensures the perpetuation of genetic lineages. In this comprehensive lesson, we contrast asexual and sexual modes, examine floral adaptations and pollination in flowering plants, trace human reproductive physiology and hormonal cycles, and study sexually transmitted infections.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B15: Sinh sản ở Thực vật và Người. Sinh sản bảo đảm sự trường tồn của các dòng giống di truyền. Trong bài học này, chúng ta sẽ so sánh sinh sản vô tính và hữu tính, cấu tạo hoa và sự thụ phấn ở thực vật có hoa, sinh lý sinh sản người và chu kỳ hormone, cùng các bệnh lây truyền qua đường tình dục."
        },
        {
            "id": "sec_reproduction_modes",
            "title": "1. So sánh Sinh sản Vô tính & Hữu tính",
            "selector": "#sec-reproduction-modes",
            "en": "Section 1 contrasts reproductive strategies: Asexual reproduction involves a single parent, producing genetically identical offspring called clones via mitotic division without fusion of gametes, allowing rapid colonization of favorable environments. Sexual reproduction involves the fusion of two haploid gamete nuclei during fertilization to produce a diploid zygote, creating genetic variation that enables populations to adapt to changing environments.",
            "vi": "Mục một so sánh hai chiến lược sinh sản: Sinh sản vô tính chỉ có một cơ thể mẹ, tạo ra các thế hệ con giống hệt nhau về di truyền (dòng vô tính) qua nguyên phân mà không có sự dung hợp giao tử, giúp nhân nhanh số lượng cá thể trong môi trường thuận lợi. Sinh sản hữu tính là sự kết hợp giữa nhân của hai giao tử đơn bội qua thụ tinh tạo thành hợp tử lưỡng bội, tạo ra sự đa dạng biến dị di truyền giúp quần thể thích nghi với môi trường biến động."
        },
        {
            "id": "sec_flowering_plants",
            "title": "2. Sinh sản Hữu tính ở Thực vật có hoa: Thụ phấn & Nảy mầm",
            "selector": "#sec-flowering-plants",
            "en": "Section 2 investigates angiosperm reproduction: Insect-pollinated flowers have large colourful petals, sweet nectar, and sticky pollen grains to attach to visiting insects, with stigmas located inside the flower. Wind-pollinated flowers have small green petals, long dangling anthers outside the flower exposing lightweight pollen to air currents, and feathery stigmas to trap passing pollen. Pollination transfers pollen from anther to stigma; a pollen tube grows down the style into the ovary micropyle, where fertilization occurs.",
            "vi": "Mục hai khảo sát sinh sản ở thực vật hạt kín: Hoa thụ phấn nhờ côn trùng có cánh hoa sặc sỡ, tuyến mật ngọt và hạt phấn có gai nham nhở dễ dính vào côn trùng, đầu nhụy nằm sâu bên trong hoa. Hoa thụ phấn nhờ gió có cánh hoa tiêu giảm màu xanh nhạt, bao phấn đung đưa lơ lửng ngoài hoa giải phóng hạt phấn nhẹ bay theo gió và đầu nhụy dạng lông chim đón phấn. Thụ phấn là quá trình chuyển hạt phấn từ bao phấn sang đầu nhụy; hạt phấn nảy mầm mọc ống phấn đâm xuyên qua vòi nhụy vào noãn để thực hiện thụ tinh tạo hạt và quả."
        },
        {
            "id": "sec_human_reproduction",
            "title": "3. Sinh lý Sinh sản Người & Chu kỳ Kinh nguyệt",
            "selector": "#sec-human-reproduction",
            "en": "Section 3 details human reproduction: Testes produce sperm and testosterone; ovaries release mature ova and estrogen. Fertilization occurs in the oviduct. The zygote divides into an embryo, which implants into the vascularized uterine lining. The placenta connects mother and fetus via the umbilical cord, facilitating diffusion of oxygen, glucose, and antibodies to the fetus while removing urea and carbon dioxide, without mixing maternal and fetal blood. The menstrual cycle is coordinated by hormones: pituitary FSH stimulates follicle maturation; estrogen thickens uterine lining; LH surge triggers ovulation on day 14; progesterone maintains the lining for implantation.",
            "vi": "Mục ba chi tiết hóa sinh lý sinh sản người: Tinh hoàn sản sinh tinh trùng và testosterone; buồng trứng rụng trứng chín và tiết estrogen. Sự thụ tinh diễn ra ở 1/3 trên ống dẫn trứng (vòi fallop). Hợp tử phân chia thành phôi nang rồi làm tổ vào lớp niêm mạc tử cung giàu mạch máu. Nhau thai liên kết mẹ và thai nhi qua dây rốn, thực hiện khuếch tán oxy, glucose và kháng thể cho thai nhi đồng thời đào thải urê và CO2 mà không hòa trộn dòng máu mẹ và con. Chu kỳ kinh nguyệt được điều hòa nhịp nhàng: FSH kích thích nang trứng chín; estrogen làm dày niêm mạc tử cung; đỉnh LH kích hoạt rụng trứng vào ngày thứ 14; progesterone duy trì niêm mạc sẵn sàng cho phôi làm tổ."
        },
        {
            "id": "sec_stis_hiv",
            "title": "4. Bệnh Lây truyền qua Đường Tình dục (STIs) & Virus HIV",
            "selector": "#sec-stis-hiv",
            "en": "Section 4 covers Sexually Transmitted Infections: An STI is an infection transmitted via sexual contact. Human Immunodeficiency Virus, or HIV, infects and progressively destroys lymphocytes, crippling antibody production and cellular immunity, leading to Acquired Immune Deficiency Syndrome, or AIDS. HIV is transmitted through unprotected sexual intercourse, sharing contaminated hypodermic needles, and mother-to-child during birth or breastfeeding. Transmission is prevented by using barrier contraception like condoms and screening donor blood.",
            "vi": "Mục bốn phân tích các bệnh lây truyền qua đường tình dục (STIs): HIV là virus gây suy giảm miễn dịch ở người, xâm nhập và phá hủy các tế bào bạch cầu lympho T, làm tê liệt khả năng sản xuất kháng thể và đáp ứng miễn dịch, dẫn đến hội chứng AIDS. HIV lây truyền qua quan hệ tình dục không an toàn, dùng chung kim tiêm nhiễm máu và truyền từ mẹ sang con trong khi sinh hoặc cho con bú. Phòng ngừa lây nhiễm bằng cách sử dụng biện pháp rào cản như bao cao su và sàng lọc kỹ lưỡng máu hiến tặng."
        }
    ]

    major_sections = [
        {"id": "sec_reproduction_modes", "title": "1. Sinh sản Vô tính vs Hữu tính"},
        {"id": "sec_flowering_plants", "title": "2. Sinh sản Hữu tính ở Thực vật"},
        {"id": "sec_human_reproduction", "title": "3. Sinh sản Người & Chu kỳ Kinh nguyệt"},
        {"id": "sec_stis_hiv", "title": "4. Bệnh Lây qua Đường Tình dục (STIs) & HIV"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B15 successfully built!")


# ==============================================================================
# MAIN BATCH 3 RUNNER (TOPICS B11 -> B15)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING CO-ORDINATED SCIENCE BATCH 3: TOPICS B11 -> B15")
    print("*******************************************************\n")
    
    await build_b11()
    await asyncio.sleep(2)
    
    await build_b12()
    await asyncio.sleep(2)
    
    await build_b13()
    await asyncio.sleep(2)
    
    await build_b14()
    await asyncio.sleep(2)
    
    await build_b15()
    
    print("\n*******************************************************")
    print("BATCH 3 COMPLETE: TOPICS B11 -> B15 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
