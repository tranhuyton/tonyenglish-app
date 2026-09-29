import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# TOPIC C5: Chemical energetics
# ==============================================================================
async def build_c5():
    lid = '71545c83-4d45-4201-978c-aa58d01b57e5'
    code = 'c5'
    title = 'C5: Chemical energetics'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-exo-endo" class="lecture-interactive-card" data-lecture-section="sec_exo_endo" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-reaction-profiles" class="lecture-interactive-card" data-lecture-section="sec_reaction_profiles" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-bond-energies" class="lecture-interactive-card" data-lecture-section="sec_bond_energies" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic C5 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề C5: Nhiệt Hóa học & Năng lượng Liên kết",
            "selector": "#sec-header",
            "en": "Welcome to Topic C5: Chemical energetics. Every chemical transformation involves energetic exchanges with surroundings. In this lesson, we contrast exothermic and endothermic reactions, interpret reaction pathway energy profiles and activation energy, and compute net enthalpy changes using bond energies.",
            "vi": "Chào mừng các bạn đến với Chuyên đề C5: Nhiệt Hóa học và Năng lượng Liên kết. Mọi biến đổi hóa học đều đi kèm với sự trao đổi năng lượng với môi trường. Trong bài học này, chúng ta sẽ so sánh phản ứng tỏa nhiệt và thu nhiệt, đọc giản đồ năng lượng phản ứng, và tính biến thiên enthalpy dựa vào năng lượng liên kết."
        },
        {
            "id": "sec_exo_endo",
            "title": "1. Phản ứng Tỏa nhiệt & Thu nhiệt (Exothermic vs Endothermic)",
            "selector": "#sec-exo-endo",
            "en": "Section 1 contrasts reaction energetics: An Exothermic reaction transfers thermal energy to the surroundings, leading to an increase in the temperature of the surroundings, giving a negative enthalpy change (Delta H < 0), such as combustion and neutralization. An Endothermic reaction takes in thermal energy from the surroundings, leading to a decrease in temperature, giving a positive enthalpy change (Delta H > 0), such as thermal decomposition of calcium carbonate and photosynthesis.",
            "vi": "Mục một so sánh bản chất năng lượng của phản ứng: Phản ứng Tỏa nhiệt (Exothermic) truyền nhiệt lượng ra môi trường xung quanh, làm nhiệt độ môi trường tăng lên, có biến thiên enthalpy âm (Delta H < 0), ví dụ như phản ứng cháy và phản ứng trung hòa axit-bazơ. Phản ứng Thu nhiệt (Endothermic) hấp thu nhiệt năng từ môi trường, làm nhiệt độ môi trường hạ xuống, có biến thiên enthalpy dương (Delta H > 0), ví dụ như phản ứng nhiệt phân đá vôi CaCO3 và quang hợp."
        },
        {
            "id": "sec_reaction_profiles",
            "title": "2. Giản đồ Năng lượng Phản ứng & Năng lượng Hoạt hóa (Ea)",
            "selector": "#sec-reaction-profiles",
            "en": "Section 2 interprets reaction pathway profiles: In exothermic profiles, reactants start at higher potential energy than products, with an arrow pointing downward representing negative Delta H. In endothermic profiles, products sit at higher energy than reactants, with Delta H pointing upward. Activation Energy (E_a) is the minimum energy that colliding particles must possess to react, represented on profiles by the energy difference between reactants and the peak of the transition state.",
            "vi": "Mục hai giải mã giản đồ năng lượng: Trong giản đồ phản ứng tỏa nhiệt, chất phản ứng ở mức thế năng cao hơn sản phẩm, mũi tên Delta H chỉ xuống dưới mang giá trị âm. Trong giản đồ phản ứng thu nhiệt, sản phẩm nằm ở mức năng lượng cao hơn chất phản ứng, mũi tên Delta H hướng lên trên mang giá trị dương. Năng lượng Hoạt hóa (Activation Energy - Ea) là mức năng lượng tối thiểu mà các hạt va chạm phải sở hữu để phản ứng diễn ra, biểu diễn bằng khoảng cách năng lượng từ chất phản ứng lên đến đỉnh của trạng thái chuyển tiếp."
        },
        {
            "id": "sec_bond_energies",
            "title": "3. Tính toán Năng lượng Liên kết (Bond Energies)",
            "selector": "#sec-bond-energies",
            "en": "Section 3 calculates enthalpy changes via bond energies: Bond breaking is always endothermic, absorbing energy to overcome chemical attractions. Bond forming is always exothermic, releasing energy as stable bonds form. Net enthalpy change Delta H equals Total energy absorbed to break bonds in reactants minus Total energy released when forming bonds in products. If bond forming exceeds bond breaking, the overall reaction is exothermic.",
            "vi": "Mục ba hướng dẫn tính toán biến thiên enthalpy qua năng lượng liên kết: Bẻ gãy liên kết luôn là quá trình Thu nhiệt (cần cung cấp năng lượng để tách rời các nguyên tử). Hình thành liên kết mới luôn là quá trình Tỏa nhiệt (giải phóng năng lượng khi liên kết bền vững được thiết lập). Biến thiên enthalpy Delta H bằng Tổng năng lượng bẻ gãy các liên kết ở chất phản ứng trừ đi Tổng năng lượng giải phóng khi tạo thành liên kết ở sản phẩm. Nếu nhiệt tỏa ra khi tạo liên kết lớn hơn nhiệt hấp thu khi phá vỡ liên kết, phản ứng tổng thể là phản ứng tỏa nhiệt."
        }
    ]

    major_sections = [
        {"id": "sec_exo_endo", "title": "1. Phản ứng Tỏa nhiệt & Thu nhiệt"},
        {"id": "sec_reaction_profiles", "title": "2. Giản đồ Năng lượng & Năng lượng Hoạt hóa (Ea)"},
        {"id": "sec_bond_energies", "title": "3. Tính toán Năng lượng Liên kết (Bond Energies)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic C5 successfully built!")


# ==============================================================================
# TOPIC C6: Chemical reactions
# ==============================================================================
async def build_c6():
    lid = '7f2b44b2-ba70-4cfc-85b3-3a0709058b46'
    code = 'c6'
    title = 'C6: Chemical reactions'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-physical-chemical" class="lecture-interactive-card" data-lecture-section="sec_physical_chemical" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-rate-of-reaction" class="lecture-interactive-card" data-lecture-section="sec_rate_of_reaction" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-reversible-equilibrium" class="lecture-interactive-card" data-lecture-section="sec_reversible_equilibrium" style="cursor: pointer; ')
    
    t_h2_4 = h2s[4]
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-redox-reactions" class="lecture-interactive-card" data-lecture-section="sec_redox_reactions" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic C6 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề C6: Tốc độ Phản ứng, Cân bằng & Oxy hóa Khử",
            "selector": "#sec-header",
            "en": "Welcome to Topic C6: Chemical reactions. Chemical dynamics governs how quickly and in which direction transformations occur. In this lesson, we contrast physical and chemical changes, analyze collision theory and reaction rates, explore reversible reactions and Le Chatelier's dynamic equilibrium, and decode redox electron transfer.",
            "vi": "Chào mừng các bạn đến với Chuyên đề C6: Tốc độ Phản ứng, Cân bằng Hóa học và Phản ứng Oxy hóa Khử. Động hóa học điều khiển tốc độ và chiều hướng biến đổi của phản ứng. Trong bài học này, chúng ta sẽ phân biệt biến đổi vật lý và hóa học, thuyết va chạm và tốc độ phản ứng, phản ứng thuận nghịch và cân bằng động Le Chatelier, cùng bản chất phản ứng oxy hóa khử."
        },
        {
            "id": "sec_physical_chemical",
            "title": "1. Biến đổi Vật lý vs Biến đổi Hóa học",
            "selector": "#sec-physical-chemical",
            "en": "Section 1 distinguishes physical and chemical changes: A Physical change alters state or appearance without producing new chemical substances, requiring relatively little energy and being readily reversible, like ice melting. A Chemical change breaks and forms bonds to produce one or more entirely new substances with different properties, often accompanied by noticeable energy changes like temperature rise, colour change, gas effervescence, or precipitate formation, and is difficult to reverse.",
            "vi": "Mục một phân biệt hiện tượng vật lý và hóa học: Biến đổi Vật lý chỉ thay đổi trạng thái hoặc hình dạng mà không tạo ra chất mới, tiêu tốn ít năng lượng và dễ dàng đảo ngược, như nước đá tan thành nước lỏng. Biến đổi Hóa học phá vỡ và thiết lập các liên kết mới để tạo ra các chất hoàn toàn mới với tính chất khác biệt, thường đi kèm các dấu hiệu tỏa nhiệt, đổi màu, sủi bọt khí hoặc xuất hiện kết tủa, và rất khó đảo ngược."
        },
        {
            "id": "sec_rate_of_reaction",
            "title": "2. Tốc độ Phản ứng & Thuyết Va chạm (Collision Theory)",
            "selector": "#sec-rate-of-reaction",
            "en": "Section 2 investigates Reaction Rates: Rate of reaction measures the change in concentration, volume of gas evolved, or mass loss of reactant per unit time. Under Collision Theory, reacting particles must collide with sufficient activation energy and correct orientation. Four factors accelerate rate: Increasing concentration or gas pressure packs particles closer, increasing collision frequency. Increasing temperature gives particles higher kinetic energy so more collisions exceed activation energy. Increasing solid surface area exposes more reactive sites. Adding a catalyst lowers activation energy by providing an alternative pathway.",
            "vi": "Mục hai nghiên cứu Tốc độ Phản ứng: là đại lượng đo sự biến thiên nồng độ, thể tích khí thoát ra hoặc độ giảm khối lượng chất phản ứng trong một đơn vị thời gian. Theo Thuyết Va chạm, các hạt phản ứng phải va chạm với năng lượng lớn hơn hoặc bằng năng lượng hoạt hóa và đúng hướng không gian. Bốn yếu tố làm tăng tốc độ phản ứng: Tăng nồng độ hoặc áp suất khí làm tăng mật độ hạt dẫn đến tần suất va chạm dày đặc hơn; Tăng nhiệt độ làm hạt chuyển động nhanh hơn và tỷ lệ va chạm vượt qua rào cản năng lượng hoạt hóa tăng vọt; Tăng diện tích tiếp xúc bề mặt chất rắn; và Thêm chất xúc tác giúp hạ thấp năng lượng hoạt hóa bằng cách mở ra con đường phản ứng mới."
        },
        {
            "id": "sec_reversible_equilibrium",
            "title": "3. Phản ứng Thuận nghịch & Cân bằng Hóa học (Le Chatelier)",
            "selector": "#sec-reversible-equilibrium",
            "en": "Section 3 examines Reversible Reactions: indicated by double equilibrium arrows, where products can react back to reform original reactants, like the thermal decomposition of hydrated copper(II) sulfate. In a closed system, a Reversible reaction reaches Dynamic Equilibrium when forward and reverse reaction rates become equal, and concentrations of reactants and products remain constant. Under Le Chatelier's Principle, if a closed system at equilibrium is disturbed, the equilibrium shifts to counteract the change.",
            "vi": "Mục ba phân tích Phản ứng Thuận nghịch: được ký hiệu bằng mũi tên hai chiều, trong đó sản phẩm sinh ra có thể phản ứng ngược lại để tái tạo chất ban đầu, ví dụ phản ứng nhiệt phân tinh thể đồng(II) sunfat ngậm nước. Trong hệ kín, phản ứng thuận nghịch đạt Cân bằng Động (Dynamic Equilibrium) khi tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch, và nồng độ các chất trong hệ giữ nguyên không đổi. Theo Nguyên lý chuyển dịch cân bằng Le Chatelier: Khi một hệ cân bằng bị thay đổi các yếu tố nồng độ, nhiệt độ, áp suất, cân bằng sẽ tự động chuyển dịch theo chiều chống lại sự thay đổi đó."
        },
        {
            "id": "sec_redox_reactions",
            "title": "4. Bản chất Phản ứng Oxy hóa - Khử (Redox Reactions)",
            "selector": "#sec-redox-reactions",
            "en": "Section 4 defines Redox reactions: Oxidation is the gain of oxygen, loss of hydrogen, or loss of electrons. Reduction is the loss of oxygen, gain of hydrogen, or gain of electrons. Remember OIL RIG: Oxidation Is Loss, Reduction Is Gain of electrons. An Oxidizing agent oxidizes another substance while itself being reduced. A Reducing agent reduces another substance while itself being oxidized. Acidified aqueous potassium manganate(VII) acts as an oxidizing agent, changing from purple to colorless upon reduction; potassium iodide acts as a reducing agent, turning colorless to yellow-brown.",
            "vi": "Mục bốn định nghĩa Phản ứng Oxy hóa - Khử: Sự Oxy hóa là quá trình kết hợp với oxy, mất hydro, hoặc nhường electron. Sự Khử là quá trình mất oxy, kết hợp với hydro, hoặc nhận electron. Quy tắc cốt lõi: Khử cho - O nhận (Chất khử nhường electron, chất oxy hóa nhận electron). Thuốc thử nhận biết chất khử là dung dịch thuốc tím KMnO4 trong môi trường axit, chuyển từ màu tím sang không màu; thuốc thử nhận biết chất oxy hóa là dung dịch kali iotua KI không màu hóa màu nâu vàng do tạo ra iot đơn chất."
        }
    ]

    major_sections = [
        {"id": "sec_physical_chemical", "title": "1. Biến đổi Vật lý vs Biến đổi Hóa học"},
        {"id": "sec_rate_of_reaction", "title": "2. Tốc độ Phản ứng & Thuyết Va chạm"},
        {"id": "sec_reversible_equilibrium", "title": "3. Phản ứng Thuận nghịch & Cân bằng Động"},
        {"id": "sec_redox_reactions", "title": "4. Bản chất Phản ứng Oxy hóa - Khử (Redox)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic C6 successfully built!")


# ==============================================================================
# TOPIC C7: Acids bases and salts
# ==============================================================================
async def build_c7():
    lid = '2c83104c-9413-4ee1-bdf3-2c0da8fd96a6'
    code = 'c7'
    title = 'C7: Acids bases and salts'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-acids-bases" class="lecture-interactive-card" data-lecture-section="sec_acids_bases" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-acid-reactions" class="lecture-interactive-card" data-lecture-section="sec_acid_reactions" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-salt-preparation" class="lecture-interactive-card" data-lecture-section="sec_salt_preparation" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic C7 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề C7: Axit, Bazơ & Phương pháp Điều chế Muối",
            "selector": "#sec-header",
            "en": "Welcome to Topic C7: Acids, bases and salts. Acid-base chemistry underpins ionic solution behavior. In this lesson, we define proton donor acids and acceptor bases, test pH scales with indicators, examine the three characteristic acid reactions, and master laboratory preparations of soluble and insoluble salts.",
            "vi": "Chào mừng các bạn đến với Chuyên đề C7: Axit, Bazơ và Phương pháp Điều chế Muối. Hóa học axit-bazơ là nền tảng của các phản ứng trong dung dịch nước. Trong bài học này, chúng ta sẽ định nghĩa axit và bazơ theo thuyết proton, thang đo pH và chất chỉ thị, 3 phản ứng đặc trưng của axit, cùng quy trình phòng thí nghiệm điều chế muối tan và muối không tan."
        },
        {
            "id": "sec_acids_bases",
            "title": "1. Khái niệm Axit, Bazơ, Kiềm & Thang đo pH",
            "selector": "#sec-acids-bases",
            "en": "Section 1 defines acids and bases: An Acid is a proton donor, dissociating in water to produce aqueous hydrogen ions (H+). A Base is a proton acceptor, neutralizing acids to produce salt and water. An Alkali is a soluble base that dissociates in aqueous solution to produce hydroxide ions (OH-). The pH scale quantifies acidity: pH 0 to 6 indicates acidic solutions, pH 7 is neutral, and pH 8 to 14 indicates alkaline solutions. Universal indicator displays red in strong acid, green at neutrality, and purple in strong alkali; litmus turns red in acid and blue in alkali.",
            "vi": "Mục một định nghĩa axit, bazơ và thang đo pH: Axit là chất nhường proton (H+), khi hòa tan trong nước phân ly giải phóng ion H+. Bazơ là chất nhận proton, trung hòa axit tạo thành muối và nước. Kiềm (Alkali) là bazơ tan trong nước, khi hòa tan phân ly giải phóng ion OH-. Thang đo pH đo lường độ axit: pH từ 0 đến 6 biểu thị môi trường axit, pH 7 là trung tính, và pH từ 8 đến 14 biểu thị môi trường kiềm. Chất chỉ thị vạn năng chuyển sang màu đỏ trong axit mạnh, màu xanh lá cây ở môi trường trung tính và màu tím trong kiềm mạnh; quỳ tím hóa đỏ trong axit và hóa xanh trong kiềm."
        },
        {
            "id": "sec_acid_reactions",
            "title": "2. Ba Phản ứng Đặc trưng của Axit",
            "selector": "#sec-acid-reactions",
            "en": "Section 2 investigates the three classic acid reactions: First, Acid reacts with Metal above hydrogen in the reactivity series to produce a Salt and Hydrogen gas, tested by a squeaky pop with a lit splint. Second, Acid reacts with Metal Oxide or Hydroxide base in neutralization to produce a Salt and Water. Third, Acid reacts with Metal Carbonate to produce a Salt, Water, and Carbon Dioxide gas, which effervesces and turns limewater cloudy milk white.",
            "vi": "Mục hai nghiên cứu 3 phản ứng đặc trưng của axit: Thứ nhất, Axit phản ứng với Kim loại đứng trước hydro trong dãy hoạt động hóa học tạo thành Muối và giải phóng khí Hydro H2 (thử bằng que đóm đang cháy phát ra tiếng nổ 'bốp' nhỏ). Thứ hai, Axit phản ứng với Oxit kim loại hoặc Hiđroxit bazơ trong phản ứng trung hòa tạo thành Muối và Nước. Thứ ba, Axit phản ứng với Muối Cacbonat tạo thành Muối, Nước và sủi bọt khí CO2 (làm đục nước vôi trong)."
        },
        {
            "id": "sec_salt_preparation",
            "title": "3. Kỹ thuật Điều chế Muối trong Phòng Thí nghiệm",
            "selector": "#sec-salt-preparation",
            "en": "Section 3 details salt preparation methods based on solubility: To prepare a Soluble salt from an Insoluble base or carbonate: add excess solid to warm acid until no more dissolves, filter off unreacted excess solid, heat filtrate to crystallisation point, and cool to form pure crystals. To prepare a Soluble salt from an Alkali: perform acid-base titration using indicator to find exact neutralization endpoint, repeat without indicator, and crystallize. To prepare an Insoluble salt: mix two soluble solutions in Precipitation, filter precipitate, wash thoroughly with distilled water, and dry.",
            "vi": "Mục ba hướng dẫn quy trình điều chế muối trong phòng thí nghiệm dựa vào độ tan: Để điều chế Muối Tan từ oxit/bazơ không tan: cho từ từ chất rắn dư vào axit đun nóng nhẹ cho đến khi chất rắn không tan thêm, lọc bỏ bã rắn dư, đun bay hơi dung dịch lọc đến điểm kết tinh rồi để nguội cho tinh thể muối kết tinh. Để điều chế Muối Tan từ dung dịch kiềm: chuẩn độ thể tích bằng chất chỉ thị màu để xác định điểm tương đương chính xác, lặp lại thí nghiệm không dùng chất chỉ thị rồi kết tinh. Để điều chế Muối Không Tan: trộn hai dung dịch muối tan trong phản ứng kết tủa (Precipitation), lọc lấy kết tủa trên phễu, rửa sạch nhiều lần bằng nước cất và sấy khô."
        }
    ]

    major_sections = [
        {"id": "sec_acids_bases", "title": "1. Khái niệm Axit, Bazơ & Thang đo pH"},
        {"id": "sec_acid_reactions", "title": "2. Ba Phản ứng Đặc trưng của Axit"},
        {"id": "sec_salt_preparation", "title": "3. Phương pháp Điều chế Muối"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic C7 successfully built!")


# ==============================================================================
# TOPIC C8: Periodic table
# ==============================================================================
async def build_c8():
    lid = '856f20da-80e8-4c6a-9cd1-dbe8a1f40828'
    code = 'c8'
    title = 'C8: Periodic table'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-arrangement-elements" class="lecture-interactive-card" data-lecture-section="sec_arrangement_elements" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-group-trends" class="lecture-interactive-card" data-lecture-section="sec_group_trends" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-transition-noblegases" class="lecture-interactive-card" data-lecture-section="sec_transition_noblegases" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic C8 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề C8: Bảng Tuần hoàn các Nguyên tố Hóa học",
            "selector": "#sec-header",
            "en": "Welcome to Topic C8: Periodic table. The Periodic Table is the foundational map organizing all known chemical elements. In this chapter, we explore periodic trends across groups and periods, contrast Group I Alkali metals with Group VII Halogens, and analyze the unique properties of transition elements and noble gases.",
            "vi": "Chào mừng các bạn đến với Chuyên đề C8: Bảng Tuần hoàn các Nguyên tố Hóa học. Bảng tuần hoàn là bản đồ phân loại trật tự của toàn bộ nguyên tố hóa học. Trong bài học này, chúng ta sẽ khảo sát quy luật biến đổi tuần hoàn theo chu kỳ và nhóm, so sánh Nhóm I kim loại kiềm và Nhóm VII halogen, cùng đặc tính của kim loại chuyển tiếp và khí hiếm."
        },
        {
            "id": "sec_arrangement_elements",
            "title": "1. Cấu trúc Bảng Tuần hoàn: Chu kỳ & Phân nhóm",
            "selector": "#sec-arrangement-elements",
            "en": "Section 1 explains Periodic Table architecture: Elements are arranged in order of increasing atomic number or proton number. Vertical columns are Groups: elements in the same group possess the same number of outer-shell valence electrons, resulting in similar chemical properties. Horizontal rows are Periods: the period number corresponds to the number of occupied electron shells. Across a period from left to right, metallic character decreases while non-metallic character increases.",
            "vi": "Mục một giải thích cấu trúc Bảng tuần hoàn: Các nguyên tố được sắp xếp theo chiều tăng dần của số hiệu nguyên tử (số proton). Các cột thẳng đứng là các Nhóm (Groups): các nguyên tố cùng nhóm có cùng số electron lớp ngoài cùng nên có tính chất hóa học tương tự nhau. Các hàng ngang là các Chu kỳ (Periods): số thứ tự chu kỳ tương ứng với số lớp electron trong nguyên tử. Đi từ trái sang phải qua một chu kỳ, tính kim loại giảm dần và tính phi kim tăng dần."
        },
        {
            "id": "sec_group_trends",
            "title": "2. Kim loại Kiềm Nhóm I vs Halogen Nhóm VII",
            "selector": "#sec-group-trends",
            "en": "Section 2 contrasts Group I and Group VII: Group I Alkali metals are soft, low-density metals with one valence electron that react vigorously with water to form alkaline metal hydroxide solutions and hydrogen gas; reactivity increases down the group as the valence electron is further from the nucleus and more easily lost. Group VII Halogens are diatomic non-metals with seven valence electrons; reactivity decreases down the group from fluorine to iodine because incoming electrons feel less nuclear attraction. A more reactive halogen will displace a less reactive halide ion from aqueous solution.",
            "vi": "Mục hai so sánh Nhóm I và Nhóm VII: Kim loại kiềm Nhóm I (Alkali metals) là các kim loại mềm, khối lượng riêng thấp, có 1 electron lớp ngoài cùng, phản ứng mãnh liệt với nước tạo dung dịch kiềm hiđroxit và giải phóng khí H2; độ hoạt động hóa học tăng dần từ trên xuống dưới do bán kính nguyên tử tăng làm lực giữ electron ngoài cùng yếu đi. Halogen Nhóm VII là các phi kim hai nguyên tử có 7 electron ngoài cùng; độ hoạt động hóa học giảm dần từ trên xuống dưới từ flo đến iot do hạt nhân hút electron nhận vào ngày càng yếu. Một halogen hoạt động mạnh hơn sẽ đẩy halogen yếu hơn ra khỏi dung dịch muối của nó."
        },
        {
            "id": "sec_transition_noblegases",
            "title": "3. Kim loại Chuyển tiếp & Khí hiếm Nhóm VIII (Noble Gases)",
            "selector": "#sec-transition-noblegases",
            "en": "Section 3 investigates transition metals and noble gases: Transition elements form the central block of the table, characterized by high melting points, high densities, variable oxidation states, ability to form brightly coloured compounds, and extensive utility as industrial catalysts. Group VIII or Group zero Noble Gases are unreactive monatomic gases with full, stable outer electron shells, rendering them chemically inert, used in incandescent lamps and advertising signs.",
            "vi": "Mục ba nghiên cứu kim loại chuyển tiếp và khí hiếm: Kim loại chuyển tiếp (Transition elements) nằm ở khối giữa của bảng tuần hoàn, có nhiệt độ nóng chảy cao, khối lượng riêng lớn, có nhiều trạng thái oxy hóa khác nhau, tạo nên các hợp chất có màu sắc rực rỡ và được ứng dụng rộng rãi làm chất xúc tác công nghiệp. Khí hiếm Nhóm VIII gồm các đơn nguyên tử khí không màu có lớp electron ngoài cùng bão hòa bền vững tuyệt đối, hoàn toàn trơ về mặt hóa học, được ứng dụng trong bóng đèn dây tóc và đèn quảng cáo neon."
        }
    ]

    major_sections = [
        {"id": "sec_arrangement_elements", "title": "1. Cấu trúc Bảng Tuần hoàn: Chu kỳ & Nhóm"},
        {"id": "sec_group_trends", "title": "2. Kim loại Kiềm Nhóm I vs Halogen Nhóm VII"},
        {"id": "sec_transition_noblegases", "title": "3. Kim loại Chuyển tiếp & Khí hiếm Nhóm VIII"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic C8 successfully built!")


# ==============================================================================
# MAIN BATCH 6 RUNNER (TOPICS C5 -> C8)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING CO-ORDINATED SCIENCE BATCH 6: TOPICS C5 -> C8")
    print("*******************************************************\n")
    
    await build_c5()
    await asyncio.sleep(2)
    
    await build_c6()
    await asyncio.sleep(2)
    
    await build_c7()
    await asyncio.sleep(2)
    
    await build_c8()
    
    print("\n*******************************************************")
    print("BATCH 6 COMPLETE: TOPICS C5 -> C8 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
