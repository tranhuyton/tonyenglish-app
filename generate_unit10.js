const generateUnit = require('./generate_all');

const u = {
  unit: 10,
  title: 'Unit 10: Ruth Handler',
  words: [
    { word: 'Barbie doll', pos: '', defVi: 'búp bê Barbie' },
    { word: 'cruelly', pos: 'ad.', defVi: 'cực kỳ' },
    { word: 'cabbage', pos: 'n.', defVi: 'cải bắp, mẩu vải thừa' },
    { word: 'patch', pos: 'n.', defVi: 'miếng vá' },
    { word: 'thunderbird', pos: 'n.', defVi: 'chim sấm (hình tượng thần thoại)' },
    { word: 'discard', pos: 'v.', defVi: 'loại bỏ, vứt bỏ' },
    { word: 'cupboard', pos: 'n.', defVi: 'tủ chén' },
    { word: 'outlive', pos: 'v.', defVi: 'sống lâu hơn' },
    { word: 'longevity', pos: 'n.', defVi: 'sự trường thọ, tuổi thọ' },
    { word: 'toyland', pos: 'n.', defVi: 'thế giới đồ chơi' },
    { word: 'as much... as', pos: '', defVi: 'nhiều bằng' },
    { word: 'press', pos: 'v.', defVi: 'thúc giục, nài ép' },
    { word: 'flop', pos: 'n.', defVi: 'sự thất bại' },
    { word: 'celebrate', pos: 'v.', defVi: 'tổ chức lễ kỷ niệm' },
    { word: 'fame', pos: 'n.', defVi: 'danh tiếng' },
    { word: 'icon', pos: 'n.', defVi: 'biểu trưng, hình tượng' },
    { word: 'applaud', pos: 'v.', defVi: 'khen ngợi, tán thưởng' },
    { word: 'at one time', pos: '', defVi: 'có thời' },
    { word: 'switch on', pos: '', defVi: 'bật' },
    { word: 'albeit', pos: 'conj.', defVi: 'mặc dù, dù' },
    { word: 'fantastic', pos: 'a.', defVi: 'tuyệt vời' },
    { word: 'time capsule', pos: '', defVi: 'hộp chứa một số vật thể tiêu biểu của một thời điểm nào đó để con người trong tương lai hiểu được cuộc sống như thế nào vào thời điểm đó' },
    { word: 'representative', pos: 'n.', defVi: 'vật / người đại diện' },
    { word: 'archetypal', pos: 'a.', defVi: 'thuộc nguyên mẫu' },
    { word: 'feminist', pos: 'n.', defVi: 'người theo thuyết nam nữ bình quyền' },
    { word: 'bimbo', pos: 'n.', defVi: 'người phụ nữ lẳng lơ, người phụ nữ hấp dẫn nhưng kém thông minh' },
    { word: 'retort', pos: 'v.', defVi: 'cãi lại, đáp lại' },
    { word: 'academe', pos: 'n.', defVi: 'trường đại học' },
    { word: 'bend one\\\'s mind to sth.', pos: '', defVi: 'hướng ý nghĩ vào cái gì' },
    { word: 'phenomenon', pos: 'n.', defVi: 'hiện tượng' },
    { word: 'sociology', pos: 'n.', defVi: 'xã hội học' },
    { word: 'set', pos: 'v.', defVi: 'nêu, giao, đặt' },
    { word: 'role model', pos: '', defVi: 'thần tượng' },
    { word: 'be sensitive to', pos: '', defVi: 'nhạy cảm với' },
    { word: 'line', pos: 'n.', defVi: 'phương pháp, quy tắc, cách' },
    { word: 'line of reasoning', pos: '', defVi: 'cách lý luận' },
    { word: 'reflect', pos: 'v.', defVi: 'phản ánh' },
    { word: 'honour', pos: 'v.', defVi: 'tôn kính, kính trọng' },
    { word: 'steerage', pos: 'n.', defVi: 'khoang hạng chót' },
    { word: 'accommodation', pos: 'n.', defVi: 'phòng ở' },
    { word: 'conscript', pos: 'v.', defVi: 'bắt đi lính' },
    { word: 'exhaust', pos: 'v.', defVi: 'làm kiệt quệ' },
    { word: 'have a way of', pos: '', defVi: 'có cách (làm gì)' },
    { word: 'head for', pos: '', defVi: 'hướng đến' },
    { word: 'make it', pos: '', defVi: 'thực hiện thành công, làm được' },
    { word: 'add to', pos: '', defVi: 'bổ sung thêm' },
    { word: 'lore', pos: 'n.', defVi: 'truyền thuyết' },
    { word: 'picture frame', pos: '', defVi: 'khung hình' },
    { word: 'reasonably', pos: 'ad.', defVi: 'khá' },
    { word: 'come across', pos: '', defVi: 'tình cờ gặp, bắt gặp' },
    { word: 'improbable', pos: 'a.', defVi: 'không chắc có thực, khá kỳ lạ' },
    { word: 'proportions', pos: 'n.', defVi: 'quy mô, kích thước' },
    { word: 'skimpy', pos: 'a.', defVi: 'thiếu, không đủ, hở hang' },
    { word: 'presumably', pos: 'ad.', defVi: 'có lẽ' },
    { word: 'ambition', pos: 'n.', defVi: 'tham vọng' },
    { word: 'suppress', pos: 'v.', defVi: 'kiềm chế, nén' },
    { word: 'blush', pos: 'n.', defVi: 'sự đỏ mặt (vì hổ thẹn)' },
    { word: 'inspire', pos: 'v.', defVi: 'truyền cảm hứng' },
    { word: 'respectable', pos: 'a.', defVi: 'đáng trọng, đáng kính, đứng đắn' },
    { word: 'non-provocative', pos: 'a.', defVi: 'không khêu gợi' },
    { word: 'debut', pos: 'n.', defVi: 'sự xuất hiện lần đầu tiên trước công chúng' },
    { word: 'more than', pos: '', defVi: 'hơn' },
    { word: 'in good condition', pos: '', defVi: 'ở điều kiện tốt' },
    { word: 'sustain', pos: 'v.', defVi: 'giữ vững được, kéo dài' },
    { word: 'guise', pos: 'n.', defVi: 'lốt, vỏ, dáng vẻ' },
    { word: 'shameless', pos: 'a.', defVi: 'vô liêm sỉ, trơ tráo, trơ trẽn' },
    { word: 'retain', pos: 'v.', defVi: 'giữ lại' },
    { word: 'knowing', pos: 'a.', defVi: 'hiểu biết, tinh khôn' },
    { word: 'belly button', pos: '', defVi: 'rốn' },
    { word: 'reproduction', pos: 'n.', defVi: 'sự sinh sản' },
    { word: 'career woman', pos: '', defVi: 'người phụ nữ chuyên tâm vào sự nghiệp vì vậy không muốn lập gia đình và có con cái' },
    { word: 'empty headed', pos: '', defVi: 'đầu óc trống rỗng' },
    { word: 'prospect', pos: 'n.', defVi: 'triển vọng, viễn cảnh' },
    { word: 'innocent', pos: 'a.', defVi: 'ngây thơ, vô tội' },
    { word: 'mores', pos: 'n.', defVi: 'tập tục' },
    { word: 'changeable', pos: 'a.', defVi: 'dễ thay đổi, hay thay đổi' },
    { word: 'cope with', pos: '', defVi: 'đối phó, đương đầu' }
  ],
  story: `<h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Ruth Handler</h1>
  <p style="margin-bottom: 1rem;">Ruth Handler, creator of the Barbie doll, died on April 27th, aged 85.</p>
  <p style="margin-bottom: 1rem;">The Barbie doll is 43 this year, a great age for a toy. Most toys have cruelly short lives. Who now remembers the Cabbage Patch Kids, Tiny Tears, Thunderbirds? They lie discarded in the toy cupboards of the rich world. Barbie has outlived them all. No one has been able to say why, not even Ruth Handler, Barbie's creator. Longevity in toyland is as much a mystery as it is in real life. When pressed by reporters why Barbie had done so well Mrs Handler said, smilingly, "I was a marketing genius." Perhaps she was. But no other products by Mattel, the firm she helped to found, did as well, and some were flops.</p>
  <p style="margin-bottom: 1rem;">Still, America is happy to celebrate success, whatever its mystery, and Barbie gained fame not simply as a product but as an icon. Andy Warhol produced an image of Barbie, to be applauded alongside that of Marilyn Monroe. At one time you could hardly switch on the radio in America without hearing the song "Barbie Girl", albeit by a Danish group, Aqua: "Life in plastic/It's fantastic." A Barbie doll was buried in an American government time capsule as representative of life in the 20th century. Barbie was said to be "the archetypal woman", a modern Mona Lisa. On television feminists said Barbie was a bimbo and bad for children. Mrs Handler retorted that Barbie offered children choices of what to be when they grew up. Academe bent its mind to the Barbie phenomenon. Students on a sociology course were set the following exercise: "What criticisms have been made of Barbie as a role model? Do you agree with this criticism? In your opinion, should the manufacturers be sensitive to this criticism? There are no 'right' answer to these questions, but you should develop a line of reasoning that reflects your values."</p>
  <p style="margin-bottom: 1rem;"><strong>A garage in California</strong></p>
  <p style="margin-bottom: 1rem;">Ruth Handler was herself a success story in an honoured American tradition. Her parents had arrived in the United States in a steamship, travelling steerage, the cheapest accommodation, and settled in Denver. Her father was a blacksmith who had brought his family from Poland so that he would not be conscripted into the Russian army. Mother never felt very well, exhausted after bearing ten children. But big families have a way of looking after themselves, and Ruth, the youngest, says she was well cared for.</p>
  <p style="margin-bottom: 1rem;">At the age of 19 she headed for Hollywood. She did not make it into the film business. She took a course in industrial design, met a boy on the same course and married him. Mattel was started in a garage, adding to another bit of American industrial lore. Ruth Handler and her husband at first made picture frames, then furniture for dolls' houses, then toys, including a child's guitar that found a market. The firm seems to have done reasonably well and in the 1950s Mrs Handler had a holiday in Europe. In Switzerland she came across a German-made doll about 11 in tall called Blonde Lilli, of improbable proportions, dressed in skimpy clothes, and presumably designed to raise the ambitions of young men.</p>
  <p style="margin-bottom: 1rem;">Suppressing her American blushes, Mrs Handler bought three and took them back to America. She said she had been thinking for some time of producing a "grown-up" doll for children, but the men in her firm said there would be no demand for one: what children liked was dolls that looked like babies. Inspired by Lilli, Mrs Handler designed a respectable American doll called Barbie (her daughter's name) with breasts but without nipples and wearing clothes that were pretty but non-provocative. The first dolls were made in Japan and in 1959 "Barbie the teenage model" made its debut at the American Toy Fair in New York. It was the success of the show, selling 350,000 Barbies in the first year. Since then more than a billion Barbies have been sold worldwide.</p>
  <p style="margin-bottom: 1rem;">According to Mattel, an American girl aged up to 11 is likely to own ten Barbie dolls. French children are said to own five. But several million grown-up women are also said to own Barbies. "She is more than a doll to them, whatever their age," Mrs Handler said. "She has become part of them." There are Barbie collectors of both sexes: a 1959 Barbie that sold for $3 is now said to be worth $5,000 in good condition.</p>
  <p style="margin-bottom: 1rem;">What apparently sustains demand for the doll is that Barbies come in all guises, as a dancer, a police officer, an astronaut, a physician, a talking Barbie that says, "What to go shopping?" There is a Chinese Barbie, an American Indian Barbie, a black Barbie, just about every sort of Barbie except its shameless forebear Lilli. Barbie retains an almost sexless body that can puzzle knowing children who wonder how Barbie was born without a belly button and has no obvious means of reproduction. "Hey, Momma...?" "That's enough, dear, or I'll take Barbie away."</p>
  <p style="margin-bottom: 1rem;">In defending Barbie against the feminists Mrs Handler said her creation is a career woman and not at all empty headed. But Barbie has had so many careers, and at 43 marriage seems to be a declining prospect. There is a boyfriend called Ken, named after another of Mrs Handler's children. Barbie and Ken have been together for years. What are Ken's intentions? Barbie was born in the innocent 1950s, and may find the mores of these changeable times hard to cope with. Barbie's friends of all ages are concerned.</p>`
};

generateUnit(u);
