const fs = require('fs');

const wordsList1 = [
    { word: "ABC", pos: "n.", pronunciation: "[ˌeɪ biː ˈsiː]", eng: "the basic facts or principles of a subject.", eng_vie: "(khái niệm cơ sở, cơ sở)", ex: "The ABCs of living a happy life.", ex_vie: "(Những cơ sở của việc sống một cuộc sống hạnh phúc.)" },
    { word: "browse", pos: "v.", pronunciation: "[braʊz]", eng: "to look at or read parts of a book, magazine, etc., casually.", eng_vie: "(đọc lướt qua, xem lướt qua)", ex: "I was browsing around a bookshop.", ex_vie: "(Tôi đang đi dạo xem lướt qua một hiệu sách.)" },
    { word: "entitle", pos: "v.", pronunciation: "[ɪnˈtaɪtl]", eng: "to give a title to (a book, play, etc.).", eng_vie: "(đặt tên (cuốn sách, vở kịch, v.v.))", ex: "A small, interesting book entitled 'The ABCs of loving yourself'.", ex_vie: "(Một cuốn sách nhỏ, thú vị có tựa đề 'Những nguyên tắc cơ bản để yêu bản thân'.)" },
    { word: "alphabet", pos: "n.", pronunciation: "[ˈælfəbet]", eng: "a set of letters or symbols in a fixed order.", eng_vie: "(bảng chữ cái)", ex: "Each letter of the alphabet stands for something.", ex_vie: "(Mỗi chữ cái trong bảng chữ cái tượng trưng cho một điều gì đó.)" },
    { word: "stand for", pos: "phrase", pronunciation: "[stænd fɔːr]", eng: "to represent or mean.", eng_vie: "(là chữ viết tắt của, tượng trưng cho)", ex: "What does this abbreviation stand for?", ex_vie: "(Từ viết tắt này có nghĩa là gì?)" },
    { word: "motivational", pos: "adj.", pronunciation: "[ˌmoʊtɪˈveɪʃənl]", eng: "designed to promote the desire or willingness to do or achieve something.", eng_vie: "(thúc đẩy)", ex: "A motivational word.", ex_vie: "(Một từ ngữ mang tính khích lệ, thúc đẩy.)" },
    { word: "guide", pos: "v.", pronunciation: "[ɡaɪd]", eng: "to show or indicate the way to (someone).", eng_vie: "(hướng dẫn)", ex: "Useful to guide our life.", ex_vie: "(Hữu ích để hướng dẫn cuộc sống của chúng ta.)" },
    { word: "leeway", pos: "n.", pronunciation: "[ˈliːweɪ]", eng: "the amount of freedom to move or act that is available.", eng_vie: "(quyền tự do để ai di chuyển, thay đổi)", ex: "Allowing myself some leeway to adapt.", ex_vie: "(Cho phép bản thân một chút tự do để thích nghi.)" },
    { word: "adapt", pos: "v.", pronunciation: "[əˈdæpt]", eng: "to make (something) suitable for a new use or purpose; modify.", eng_vie: "(thích nghi)", ex: "Adapt the guidelines.", ex_vie: "(Sửa đổi các hướng dẫn cho phù hợp.)" },
    { word: "guideline", pos: "n.", pronunciation: "[ˈɡaɪdlaɪn]", eng: "a general rule, principle, or piece of advice.", eng_vie: "(hướng dẫn)", ex: "Adapt the guidelines.", ex_vie: "(Sửa đổi các hướng dẫn cho phù hợp.)" },
    { word: "go through", pos: "phrasal v.", pronunciation: "[ɡoʊ θruː]", eng: "to examine or search something very carefully.", eng_vie: "(đi hết, hoàn tất)", ex: "Let me go through the alphabet of life.", ex_vie: "(Hãy để tôi đi qua toàn bộ bảng chữ cái của cuộc sống.)" },
    { word: "acknowledge", pos: "v.", pronunciation: "[əkˈnɑːlɪdʒ]", eng: "to accept or admit the existence or truth of.", eng_vie: "(công nhận)", ex: "Acknowledging or appreciating your value.", ex_vie: "(Công nhận hoặc trân trọng giá trị của bạn.)" },
    { word: "appreciate", pos: "v.", pronunciation: "[əˈpriːʃieɪt]", eng: "to recognize the full worth of.", eng_vie: "(hiểu với sự thông cảm, đánh giá cao)", ex: "Appreciating your value as a person.", ex_vie: "(Trân trọng giá trị của bạn như một con người.)" },
    { word: "gifted with", pos: "phrase", pronunciation: "[ˈɡɪftɪd wɪθ]", eng: "having exceptional talent or natural ability.", eng_vie: "(được ban cho)", ex: "Gifted with endowments.", ex_vie: "(Được ban cho những tài năng thiên bẩm.)" },
    { word: "endowments", pos: "n.", pronunciation: "[ɪnˈdaʊmənts]", eng: "a quality or ability possessed or inherited by someone.", eng_vie: "(tài năng thiên bẩm)", ex: "Gifted with endowments of self-awareness.", ex_vie: "(Được ban tặng những thiên bẩm về sự tự nhận thức.)" }
];

const wordsList2 = [
    { word: "self-awareness", pos: "n.", pronunciation: "[ˌself əˈwernəs]", eng: "conscious knowledge of one's own character, feelings, motives, and desires.", eng_vie: "(sự tự ý thức)", ex: "Endowments of self-awareness.", ex_vie: "(Những tài năng thiên bẩm về sự tự nhận thức.)" },
    { word: "creative", pos: "adj.", pronunciation: "[kriˈeɪtɪv]", eng: "relating to or involving the imagination or original ideas.", eng_vie: "(sáng tạo)", ex: "Creative imagination.", ex_vie: "(Trí tưởng tượng sáng tạo.)" },
    { word: "imagination", pos: "n.", pronunciation: "[ɪˌmædʒɪˈneɪʃn]", eng: "the faculty or action of forming new ideas, or images or concepts of external objects not present to the senses.", eng_vie: "(sự tưởng tượng)", ex: "Creative imagination.", ex_vie: "(Trí tưởng tượng sáng tạo.)" },
    { word: "conscience", pos: "n.", pronunciation: "[ˈkɑːnʃəns]", eng: "an inner feeling or voice viewed as acting as a guide to the rightness or wrongness of one's behavior.", eng_vie: "(lương tâm)", ex: "Conscience, independence, will.", ex_vie: "(Lương tâm, sự độc lập, ý chí.)" },
    { word: "will", pos: "n.", pronunciation: "[wɪl]", eng: "the faculty by which a person decides on and initiates action.", eng_vie: "(ý chí)", ex: "Conscience, independence, will.", ex_vie: "(Lương tâm, sự độc lập, ý chí.)" },
    { word: "multiple", pos: "adj.", pronunciation: "[ˈmʌltɪpl]", eng: "having or involving several parts, elements, or members.", eng_vie: "(nhiều, phức tạp)", ex: "Multiple intelligence.", ex_vie: "(Trí thông minh đa dạng.)" },
    { word: "intelligence", pos: "n.", pronunciation: "[ɪnˈtelɪdʒəns]", eng: "the ability to acquire and apply knowledge and skills.", eng_vie: "(trí thông minh)", ex: "Multiple intelligence.", ex_vie: "(Trí thông minh đa dạng.)" },
    { word: "tap into", pos: "phrasal v.", pronunciation: "[tæp ˈɪntuː]", eng: "to manage to use something in a way that brings good results.", eng_vie: "(khai thác)", ex: "The ability to tap into your endowments.", ex_vie: "(Khả năng khai thác những tài năng thiên bẩm của bạn.)" },
    { word: "lead", pos: "v.", pronunciation: "[liːd]", eng: "to have or experience (a particular way of life).", eng_vie: "(sống (một cuộc sống))", ex: "To lead an effective, meaningful life.", ex_vie: "(Để sống một cuộc sống hiệu quả và có ý nghĩa.)" },
    { word: "meaningful", pos: "adj.", pronunciation: "[ˈmiːnɪŋfl]", eng: "having a serious, important, or useful quality or purpose.", eng_vie: "(có ý nghĩa)", ex: "An effective, meaningful life.", ex_vie: "(Một cuộc sống hiệu quả, đầy ý nghĩa.)" },
    { word: "care about", pos: "phrase", pronunciation: "[ker əˈbaʊt]", eng: "to feel concern or interest for.", eng_vie: "(quan tâm đến)", ex: "Caring about yourself and people.", ex_vie: "(Quan tâm đến bản thân và mọi người.)" },
    { word: "legacy", pos: "n.", pronunciation: "[ˈleɡəsi]", eng: "an amount of money or property left to someone in a will.", eng_vie: "(di sản)", ex: "Leave a legacy.", ex_vie: "(Để lại một di sản.)" },
    { word: "care for", pos: "phrase", pronunciation: "[ker fɔːr]", eng: "to look after and provide for the needs of.", eng_vie: "(quan tâm đến)", ex: "Caring for similar needs of other people.", ex_vie: "(Quan tâm đến những nhu cầu tương tự của người khác.)" },
    { word: "wild", pos: "adj.", pronunciation: "[waɪld]", eng: "lacking discipline or restraint.", eng_vie: "(ngông cuồng)", ex: "Search for the wildest wishes.", ex_vie: "(Tìm kiếm những mong ước điên rồ nhất.)" },
    { word: "point", pos: "v.", pronunciation: "[pɔɪnt]", eng: "to direct someone's attention to.", eng_vie: "(chỉ, trỏ)", ex: "Begin to point you in certain directions.", ex_vie: "(Bắt đầu hướng bạn đi theo những hướng nhất định.)" },
    { word: "empathize", pos: "v.", pronunciation: "[ˈempəθaɪz]", eng: "to understand and share the feelings of another.", eng_vie: "(thông cảm, đồng cảm)", ex: "Empathizing with people.", ex_vie: "(Đồng cảm với mọi người.)" },
    { word: "generously", pos: "adv.", pronunciation: "[ˈdʒenərəsli]", eng: "in a way that shows a readiness to give more of something, as money or time, than is strictly necessary or expected.", eng_vie: "(một cách hào phóng)", ex: "Giving generously your time.", ex_vie: "(Hào phóng dành thời gian của bạn.)" },
    { word: "positive", pos: "adj.", pronunciation: "[ˈpɑːzətɪv]", eng: "consisting in or characterized by the presence rather than the absence of distinguishing features.", eng_vie: "(tích cực)", ex: "Your positive thoughts.", ex_vie: "(Những suy nghĩ tích cực của bạn.)" },
    { word: "solution", pos: "n.", pronunciation: "[səˈluːʃn]", eng: "a means of solving a problem or dealing with a difficult situation.", eng_vie: "(giải pháp)", ex: "Search for dreams and solutions.", ex_vie: "(Tìm kiếm những giấc mơ và giải pháp.)" },
    { word: "goal", pos: "n.", pronunciation: "[ɡoʊl]", eng: "the object of a person's ambition or effort; an aim or desired result.", eng_vie: "(mục tiêu)", ex: "Solutions to achieve your goals.", ex_vie: "(Giải pháp để đạt được mục tiêu của bạn.)" },
    { word: "betterment", pos: "n.", pronunciation: "[ˈbetərmənt]", eng: "the improvement of something.", eng_vie: "(sự làm cho tốt hơn, sự cải thiện)", ex: "For the betterment of life and society.", ex_vie: "(Vì sự cải thiện của cuộc sống và xã hội.)" },
    { word: "unconditionally", pos: "adv.", pronunciation: "[ˌʌnkənˈdɪʃənəli]", eng: "without conditions or limits.", eng_vie: "((một cách) dứt khoát, (một cách) vô điều kiện)", ex: "Loving unconditionally.", ex_vie: "(Yêu thương vô điều kiện.)" },
    { word: "emotionally", pos: "adv.", pronunciation: "[ɪˈmoʊʃənəli]", eng: "in a way that relates to a person's emotions.", eng_vie: "(về mặt tình cảm)", ex: "Not only emotionally or physically but spiritually.", ex_vie: "(Không chỉ về mặt cảm xúc hay thể chất mà còn về mặt tinh thần.)" },
    { word: "physically", pos: "adv.", pronunciation: "[ˈfɪzɪkli]", eng: "in a manner relating to the body as opposed to the mind.", eng_vie: "(về mặt thể chất)", ex: "Not only emotionally or physically but spiritually.", ex_vie: "(Không chỉ về mặt cảm xúc hay thể chất mà còn về mặt tinh thần.)" },
    { word: "spiritually", pos: "adv.", pronunciation: "[ˈspɪrɪtʃuəli]", eng: "in a way that relates to the spirit or soul.", eng_vie: "(về mặt tinh thần)", ex: "Not only emotionally or physically but spiritually.", ex_vie: "(Không chỉ về mặt cảm xúc hay thể chất mà còn về mặt tinh thần.)" },
    { word: "motivation", pos: "n.", pronunciation: "[ˌmoʊtɪˈveɪʃn]", eng: "the reason or reasons one has for acting or behaving in a particular way.", eng_vie: "(động cơ thúc đẩy)", ex: "M is for motivation.", ex_vie: "(M là viết tắt của động lực.)" },
    { word: "self-discipline", pos: "n.", pronunciation: "[ˌself ˈdɪsəplɪn]", eng: "the ability to control one's feelings and overcome one's weaknesses.", eng_vie: "(kỷ luật tự giác)", ex: "Self-discipline and spurring yourself on.", ex_vie: "(Kỷ luật bản thân và không ngừng thúc đẩy chính mình.)" },
    { word: "spur on", pos: "phrasal v.", pronunciation: "[spɜːr ɑːn]", eng: "to encourage someone.", eng_vie: "(khuyến khích, động viên)", ex: "Spurring yourself on as well as motivating people.", ex_vie: "(Thúc đẩy bản thân cũng như tạo động lực cho mọi người.)" },
    { word: "motivate", pos: "v.", pronunciation: "[ˈmoʊtɪveɪt]", eng: "to provide (someone) with a motive for doing something.", eng_vie: "(thúc đẩy)", ex: "Motivating people to excel.", ex_vie: "(Thúc đẩy mọi người vượt trội.)" },
    { word: "excel", pos: "v.", pronunciation: "[ɪkˈsel]", eng: "to be exceptionally good at or proficient in an activity or subject.", eng_vie: "(xuất sắc, trội hơn)", ex: "Motivating people to excel.", ex_vie: "(Thúc đẩy mọi người trở nên xuất sắc.)" },
    { word: "amiable", pos: "adj.", pronunciation: "[ˈeɪmiəbl]", eng: "having or displaying a friendly and pleasant manner.", eng_vie: "(nhã nhặn, hòa nhã)", ex: "Being nice, amiable and friendly.", ex_vie: "(Trở nên tốt bụng, nhã nhặn và thân thiện.)" },
    { word: "open", pos: "adj.", pronunciation: "[ˈoʊpən]", eng: "allowing access, passage, or a view through an empty space.", eng_vie: "(cởi mở)", ex: "Being open to people.", ex_vie: "(Cởi mở với mọi người.)" },
    { word: "absurd", pos: "adj.", pronunciation: "[əbˈsɜːrd]", eng: "wildly unreasonable, illogical, or inappropriate.", eng_vie: "(vô lý, ngớ ngẩn)", ex: "Absurd but intriguing ideas.", ex_vie: "(Những ý tưởng phi lý nhưng hấp dẫn.)" },
    { word: "intriguing", pos: "adj.", pronunciation: "[ɪnˈtriːɡɪŋ]", eng: "arousing one's curiosity or interest; fascinating.", eng_vie: "(hấp dẫn, thú vị)", ex: "Absurd but intriguing ideas.", ex_vie: "(Những ý tưởng ngớ ngẩn nhưng thú vị.)" },
    { word: "patience", pos: "n.", pronunciation: "[ˈpeɪʃns]", eng: "the capacity to accept or tolerate delay, trouble, or suffering without getting angry or upset.", eng_vie: "(sự kiên nhẫn)", ex: "P is for patience.", ex_vie: "(P là viết tắt của sự kiên nhẫn.)" },
    { word: "pace", pos: "v.", pronunciation: "[peɪs]", eng: "to do something at a slow and steady rate.", eng_vie: "(đi từng bước)", ex: "To pace oneself.", ex_vie: "(Đi từng bước theo nhịp độ của riêng mình.)" },
    { word: "spot", pos: "n.", pronunciation: "[spɑːt]", eng: "a particular place or point.", eng_vie: "(nơi, chốn)", ex: "Find a quiet spot to review.", ex_vie: "(Tìm một nơi yên tĩnh để xem xét lại.)" },
    { word: "review", pos: "v.", pronunciation: "[rɪˈvjuː]", eng: "to examine or assess (something) formally.", eng_vie: "(xem lại)", ex: "To review, reflect and rejuvenate yourself.", ex_vie: "(Để nhìn nhận, suy ngẫm và làm mới lại bản thân.)" },
    { word: "reflect", pos: "v.", pronunciation: "[rɪˈflekt]", eng: "to think deeply or carefully about.", eng_vie: "(phản ánh, ngẫm nghĩ)", ex: "To review, reflect and rejuvenate yourself.", ex_vie: "(Để nhìn nhận, suy ngẫm và làm mới lại bản thân.)" },
    { word: "rejuvenate", pos: "v.", pronunciation: "[rɪˈdʒuːvəneɪt]", eng: "to make (someone or something) look or feel younger, fresher, or more lively.", eng_vie: "(làm trẻ lại)", ex: "To review, reflect and rejuvenate yourself.", ex_vie: "(Để nhìn nhận, suy ngẫm và làm tươi mới lại bản thân.)" },
    { word: "respect", pos: "n.", pronunciation: "[rɪˈspekt]", eng: "a feeling of deep admiration for someone or something elicited by their abilities, qualities, or achievements.", eng_vie: "(sự tôn trọng)", ex: "R is for respect.", ex_vie: "(R là sự tôn trọng.)" },
    { word: "value", pos: "v.", pronunciation: "[ˈvæljuː]", eng: "to consider (someone or something) to be important or beneficial.", eng_vie: "(định giá, coi trọng)", ex: "To value diversity.", ex_vie: "(Coi trọng sự đa dạng.)" },
    { word: "diversity", pos: "n.", pronunciation: "[daɪˈvɜːrsəti]", eng: "the state of being diverse; variety.", eng_vie: "(tính đa dạng)", ex: "Diversity of races.", ex_vie: "(Sự đa dạng về chủng tộc.)" },
    { word: "religion", pos: "n.", pronunciation: "[rɪˈlɪdʒən]", eng: "the belief in and worship of a superhuman controlling power.", eng_vie: "(tôn giáo)", ex: "Diversity of races, religions.", ex_vie: "(Sự đa dạng về chủng tộc, tôn giáo.)" },
    { word: "culture", pos: "n.", pronunciation: "[ˈkʌltʃər]", eng: "the arts and other manifestations of human intellectual achievement regarded collectively.", eng_vie: "(văn hóa)", ex: "Religions, cultures, beliefs.", ex_vie: "(Tôn giáo, nền văn hóa, tín ngưỡng.)" },
    { word: "despair", pos: "n.", pronunciation: "[dɪˈsper]", eng: "the complete loss or absence of hope.", eng_vie: "(sự thất vọng, nỗi tuyệt vọng)", ex: "Even in moments of despair.", ex_vie: "(Ngay cả trong những lúc tuyệt vọng nhất.)" },
    { word: "unity", pos: "n.", pronunciation: "[ˈjuːnəti]", eng: "the state of being united or joined as a whole.", eng_vie: "(sự đoàn kết, sự hòa hợp)", ex: "U is for unity.", ex_vie: "(U là sự đoàn kết.)" },
    { word: "input", pos: "n.", pronunciation: "[ˈɪnpʊt]", eng: "what is put in, taken in, or operated on by any process or system.", eng_vie: "(đầu vào, nguồn vào)", ex: "Valuing the input of a unified team.", ex_vie: "(Coi trọng đóng góp của một tập thể thống nhất.)" },
    { word: "unified", pos: "adj.", pronunciation: "[ˈjuːnɪfaɪd]", eng: "made uniform or whole.", eng_vie: "(thống nhất)", ex: "A unified team.", ex_vie: "(Một đội ngũ thống nhất.)" },
    { word: "colleague", pos: "n.", pronunciation: "[ˈkɑːliːɡ]", eng: "a person with whom one works.", eng_vie: "(đồng nghiệp)", ex: "Family, friends and colleagues.", ex_vie: "(Gia đình, bạn bè và đồng nghiệp.)" },
    { word: "wonder", pos: "n.", pronunciation: "[ˈwʌndər]", eng: "a feeling of surprise mingled with admiration.", eng_vie: "(sự ngạc nhiên, sự kinh ngạc, sự thắc mắc)", ex: "W is for wonder.", ex_vie: "(W là viết tắt của sự kinh ngạc.)" },
    { word: "factor", pos: "n.", pronunciation: "[ˈfæktər]", eng: "a circumstance, fact, or influence that contributes to a result or outcome.", eng_vie: "(nhân tố)", ex: "The 'X' factor.", ex_vie: "(Nhân tố 'X'.)" },
    { word: "seek", pos: "v.", pronunciation: "[siːk]", eng: "to attempt to find (something).", eng_vie: "(tìm kiếm)", ex: "Seeking the extra dimension.", ex_vie: "(Tìm kiếm một khía cạnh vượt trội.)" },
    { word: "extra", pos: "adj.", pronunciation: "[ˈekstrə]", eng: "added to an existing or usual amount or number.", eng_vie: "(thượng hạng, đặc biệt)", ex: "Seeking the extra dimension.", ex_vie: "(Tìm kiếm khía cạnh đặc biệt.)" },
    { word: "dimension", pos: "n.", pronunciation: "[dɪˈmenʃn]", eng: "a measurable extent of some kind, such as length, breadth, depth, or height.", eng_vie: "(khía cạnh)", ex: "Seeking the extra dimension.", ex_vie: "(Tìm kiếm khía cạnh đặc biệt.)" },
    { word: "winning", pos: "adj.", pronunciation: "[ˈwɪnɪŋ]", eng: "attractive; endearing.", eng_vie: "(thắng cuộc, quyến rũ, hấp dẫn)", ex: "Finding the winning trait.", ex_vie: "(Tìm ra nét hấp dẫn.)" },
    { word: "trait", pos: "n.", pronunciation: "[treɪt]", eng: "a distinguishing quality or characteristic.", eng_vie: "(nét, đặc điểm)", ex: "The winning trait in each person.", ex_vie: "(Đặc điểm nổi bật trong mỗi người.)" },
    { word: "challenge", pos: "n.", pronunciation: "[ˈtʃælɪndʒ]", eng: "a call to take part in a contest or competition.", eng_vie: "(sự thách thức)", ex: "Positive challenges.", ex_vie: "(Những thử thách mang tính tích cực.)" },
    { word: "adventure", pos: "n.", pronunciation: "[ədˈventʃər]", eng: "an unusual and exciting, typically hazardous, experience or activity.", eng_vie: "(cuộc phiêu lưu)", ex: "Positive challenges and adventures.", ex_vie: "(Những thử thách và cuộc phiêu lưu mang tính tích cực.)" },
    { word: "zest", pos: "n.", pronunciation: "[zest]", eng: "great enthusiasm and energy.", eng_vie: "(sự say mê, sự thích thú)", ex: "Z is for zest in life.", ex_vie: "(Z là sự say mê trong cuộc sống.)" },
    { word: "set out", pos: "phrasal v.", pronunciation: "[set aʊt]", eng: "to begin a journey.", eng_vie: "(bắt tay (vào một công việc gì))", ex: "Whatever you set out to do.", ex_vie: "(Bất cứ điều gì bạn bắt tay vào làm.)" },
    { word: "substitute", pos: "v.", pronunciation: "[ˈsʌbstɪtuːt]", eng: "to use or add in place of.", eng_vie: "(thay thế)", ex: "Substitute your own words.", ex_vie: "(Thay thế bằng từ ngữ của riêng bạn.)" }
];

const generateHtml = (words) => {
    let html = `<div style="display:flex;flex-direction:column;gap:24px;padding-top:24px;border-top:1px dashed #cbd5e1;"><h3 style="font-size:1.125rem;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:0.05em;margin:0;">Detailed Meanings</h3><div style="display:flex;flex-direction:column;gap:24px;">`;
    words.forEach(w => {
        html += `<div style="display:flex;gap:16px;align-items:flex-start;"><div style="width:32px;height:32px;flex-shrink:0;background-color:#f8fafc;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 3px rgba(0,0,0,0.1);border:1px solid #e2e8f0;font-size:16px;">😎</div><div style="display:flex;flex-direction:column;gap:6px;"><div style="display:flex;align-items:baseline;gap:8px;"><span style="font-size:1.25rem;font-weight:800;color:#65a30d;">${w.word}</span><span style="font-size:0.875rem;color:#94a3b8;font-family:monospace;">${w.pronunciation}</span><span style="font-size:0.875rem;color:#94a3b8;font-style:italic;">${w.pos}</span></div><div style="color:#475569;font-size:0.95rem;line-height:1.5;">${w.eng} <span style="color:#0ea5e9;">${w.eng_vie}</span></div><div style="color:#64748b;font-size:0.95rem;font-style:italic;">→ ${w.ex} <span style="color:#0ea5e9;">${w.ex_vie}</span></div></div></div>`;
    });
    html += `</div></div>`;
    return html;
};

const word1Html = `<p style="display: none;">Word List</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="https://gxxalzhxpsqahgnyxwhb.supabase.co/storage/v1/object/public/images/unit5_wordlist1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div>${generateHtml(wordsList1)}</div>`;
const word2Html = `<p style="display: none;">Word List</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="https://gxxalzhxpsqahgnyxwhb.supabase.co/storage/v1/object/public/images/unit5_wordlist2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div>${generateHtml(wordsList2)}</div>`;

const readingPassageHTML = `<div style="display: flex; flex-direction: column; gap: 16px; margin-bottom: 24px;"><img src="https://gxxalzhxpsqahgnyxwhb.supabase.co/storage/v1/object/public/images/unit5_story.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="color: #334155; font-size: 1rem; line-height: 1.8; text-align: justify;"><p style="margin-bottom: 1rem;">I was <b>browsing</b> around a bookshop, a habit of mine, when I saw a small, interesting book <b>entitled</b> "The ABCs of loving yourself."</p><p style="margin-bottom: 1rem;">Each letter of the <b>alphabet stands for</b> an encouraging and <b>motivational</b> word, useful to <b>guide</b> our life.</p><p style="margin-bottom: 1rem;">Working from memory and allowing myself some <b>leeway</b> to <b>adapt</b> the <b>guidelines</b>, let me <b>go through</b> the alphabet of life.</p><p style="margin-bottom: 1rem;">"A" is for <b>acknowledging</b> or <b>appreciating</b> your value as a person, <b>gifted with endowments</b> of <b>self-awareness</b>, <b>creative imagination</b>, <b>conscience</b>, independence, <b>will</b> and <b>multiple intelligence</b>.</p><p style="margin-bottom: 1rem;">"B" is for believing in yourself, that you have the ability to <b>tap into</b> your <b>endowments</b> to <b>lead</b> an effective, <b>meaningful</b> life.</p><p style="margin-bottom: 1rem;">"C" is for <b>caring about</b> yourself and people, taking care of your basic needs to live, learn, love and leave a <b>legacy</b> while <b>caring for</b> similar needs of other people around you.</p><p style="margin-bottom: 1rem;">"D" is for dreaming big dreams, to search for the <b>wildest</b> wishes that may seem impossible, but that begin to <b>point</b> you in certain directions.</p><p style="margin-bottom: 1rem;">"E" is for <b>empathizing</b> with people, understanding their feelings and their thinking.</p><p style="margin-bottom: 1rem;">"F" is for fun, allowing yourself to enjoy life, what you do and how you do things.</p><p style="margin-bottom: 1rem;">"G" is for giving <b>generously</b> your time, your <b>positive</b> thoughts, your kindness and whatever you can afford to bring to others.</p><p style="margin-bottom: 1rem;">"H" is for happiness, being happy with who you are and what you do in life.</p><p style="margin-bottom: 1rem;">"I" is for imagination, stretching your mind to search for dreams and <b>solutions</b> to achieve your <b>goals</b>.</p><p style="margin-bottom: 1rem;">"J" is for joy, bringing joy to people you meet, live with or work with.</p><p style="margin-bottom: 1rem;">"K" is for knowledge; always learning and using what you know for the <b>betterment</b> of life and society.</p><p style="margin-bottom: 1rem;">"L" is for love, loving <b>unconditionally</b>, not only <b>emotionally</b> or <b>physically</b> but <b>spiritually</b>.</p><p style="margin-bottom: 1rem;">"M" is for <b>motivation</b>, <b>self-discipline</b> and <b>spurring</b> yourself <b>on</b> as well as <b>motivating</b> people to <b>excel</b>.</p><p style="margin-bottom: 1rem;">"N" is for being nice, <b>amiable</b> and friendly even to strangers.</p><p style="margin-bottom: 1rem;">"O" is for openness, being <b>open</b> to people, new ideas and <b>absurd</b> but <b>intriguing</b> ideas.</p><p style="margin-bottom: 1rem;">"P" is for <b>patience</b>, to control oneself, to <b>pace</b> oneself and to follow certain steps in nature.</p><p style="margin-bottom: 1rem;">"Q" is for quiet, to find moments of quiet within yourself, to find a quiet <b>spot</b> to <b>review</b>, <b>reflect</b> and <b>rejuvenate</b> yourself.</p><p style="margin-bottom: 1rem;">"R" is for <b>respect</b>, to <b>value diversity</b> of races, <b>religions</b>, <b>cultures</b>, beliefs and values.</p><p style="margin-bottom: 1rem;">"S" is for smiling, the ability to smile freely even in moments of <b>despair</b>.</p><p style="margin-bottom: 1rem;">"T" is for trust, trusting yourself, your relatives, your friends and people.</p><p style="margin-bottom: 1rem;">"U" is for <b>unity</b>, in living peacefully with people and in valuing the <b>input</b> of a <b>unified</b> team of family, friends and <b>colleagues</b>.</p><p style="margin-bottom: 1rem;">"V" is for victory, recognizing and celebrating even the smallest victory in whatever you do.</p><p style="margin-bottom: 1rem;">"W" is for <b>wonder</b>, wondering about mankind, men and women, yourself and nature.</p><p style="margin-bottom: 1rem;">"X" is for the "X" <b>factor</b>, <b>seeking</b> the <b>extra dimension</b> in yourself and in people, finding the <b>winning trait</b> in each person.</p><p style="margin-bottom: 1rem;">"Y" is for saying "yes" to positive <b>challenges</b> and <b>adventures</b>.</p><p style="margin-bottom: 1rem;">"Z" is for <b>zest</b> in life, in whatever you <b>set out</b> to do.</p><p style="margin-bottom: 1rem;">May you be guided by these ABCs of life. Perhaps you can <b>substitute</b> your own words to make them more meaningful for you.</p></div>`;

let qId = 1;

const unit5 = {
  "id": "ielts_unit5",
  "title": "UNIT 5: THE ABCs OF LIVING A HAPPY LIFE",
  "parts": [
    {
      "title": "Word List 1",
      "content": word1Html,
      "sections": [
        {
          "content": "<p class=\"font-bold text-lg text-slate-800 mb-2 mt-4\">Task 1</p><p class=\"font-bold text-[16px] text-slate-800 mb-4\">Listen carefully and fill the missing words from the word list into the blanks to complete the sentence.</p><p>1. I spent hours [ 1 ] in the bookshop.</p><p>2. I'm afraid he can't [ 2 ] to the idea of having a woman as his boss.</p><p>3. When the results of the vote were announced, the prime minister [ 3 ] defeat.</p><p>4. She doesn't [ 4 ] good wine.</p><p>5. His natural [ 5 ] are somewhat limited, and scarcely fit him for this post.</p>",
          "questions": [
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "browsing",
              "explanation": "<b>Browse</b> (v.): xem lướt qua, đi dạo xem. Tôi đã dành hàng giờ để dạo quanh xem sách trong hiệu sách."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "adapt",
              "explanation": "<b>Adapt</b> (v.): thích nghi. Tôi e rằng anh ấy không thể thích nghi với ý tưởng có sếp là phụ nữ."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "acknowledged",
              "explanation": "<b>Acknowledge</b> (v.): thừa nhận. Khi kết quả bỏ phiếu được công bố, thủ tướng đã thừa nhận thất bại."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "appreciate",
              "explanation": "<b>Appreciate</b> (v.): đánh giá cao, biết thưởng thức. Cô ấy không biết thưởng thức loại rượu vang ngon."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "endowments",
              "explanation": "<b>Endowment</b> (n.): năng lực bẩm sinh. Những năng khiếu tự nhiên của anh ấy có phần hạn chế, và hầu như không phù hợp với vị trí này."
            }
          ]
        }
      ]
    },
    {
      "title": "Word List 2",
      "content": word2Html,
      "sections": [
        {
          "content": "<p class=\"font-bold text-lg text-slate-800 mb-2 mt-4\">Task 2</p><p class=\"font-bold text-[16px] text-slate-800 mb-4\">Listen carefully and fill the missing words from the word list into the blanks to complete the sentence.</p><p>6. I haven't done anything wrong—I've got a clear [ 1 ].</p><p>7. The driver of the crashed car received [ 2 ] injuries.</p><p>8. I got a nice little [ 3 ] from my aunt.</p><p>9. The rich men [ 4 ] with those in distress.</p><p>10. This policy aims at [ 5 ] the lot of the poorest nations.</p>",
          "questions": [
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "conscience",
              "explanation": "<b>Conscience</b> (n.): lương tâm. Tôi chưa làm gì sai trái cả—tôi có một lương tâm trong sạch."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "multiple",
              "explanation": "<b>Multiple</b> (adj.): nhiều, nhiều phần. Người lái xe của chiếc ô tô bị tai nạn đã bị đa chấn thương."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "legacy",
              "explanation": "<b>Legacy</b> (n.): di sản, tiền thừa kế. Tôi đã nhận được một khoản tiền thừa kế nhỏ xinh từ dì của tôi."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "empathize",
              "explanation": "<b>Empathize</b> (v.): đồng cảm. Những người giàu có đồng cảm với những người đang gặp khó khăn."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "betterment",
              "explanation": "<b>Betterment</b> (n.): sự cải thiện. Chính sách này nhằm mục đích cải thiện số phận của những quốc gia nghèo nhất."
            }
          ]
        }
      ]
    },
    {
      "title": "Comprehensive Reading",
      "content": readingPassageHTML,
      "sections": [
        {
          "content": "<p class=\"font-bold text-lg text-slate-800 mb-2 mt-4\">Exercise 1: True / False</p><p>Determine if the following statements are True or False according to the text.</p>",
          "questions": [
            {
              "id": qId++,
              "questionType": "Droplist",
              "content": "The author found a book titled 'The ABCs of loving yourself' while browsing in a library.",
              "options": ["True", "False", "Not Given"],
              "answer": "False",
              "explanation": "<b>False</b>. The text states: 'I was browsing around a bookshop...' not a library."
            },
            {
              "id": qId++,
              "questionType": "Droplist",
              "content": "The letter 'E' stands for enjoying life and having fun.",
              "options": ["True", "False", "Not Given"],
              "answer": "False",
              "explanation": "<b>False</b>. The text states: '\"E\" is for empathizing with people...' and '\"F\" is for fun, allowing yourself to enjoy life...'."
            },
            {
              "id": qId++,
              "questionType": "Droplist",
              "content": "According to the text, 'L' encourages people to love conditionally, only when they are treated well.",
              "options": ["True", "False", "Not Given"],
              "answer": "False",
              "explanation": "<b>False</b>. The text states: '\"L\" is for love, loving unconditionally...'."
            },
            {
              "id": qId++,
              "questionType": "Droplist",
              "content": "The author suggests that readers can change the words for each letter to make them more personally meaningful.",
              "options": ["True", "False", "Not Given"],
              "answer": "True",
              "explanation": "<b>True</b>. The text concludes with: 'Perhaps you can substitute your own words to make them more meaningful for you.'"
            }
          ]
        }
      ]
    }
  ],
  "basicInfo": {
    "skill": "MCQ (Standard)",
    "title": "Unit 5: The ABCs of Living a Happy Life",
    "category": "exercise",
    "courseId": "239a64f0-c106-40e5-a6e2-4e685a0d70fb",
    "timeLimit": 40
  }
};

// Ensure all IDs are sequential from 1
finalId = 1;
unit5.parts.forEach(p => {
    p.sections.forEach(s => {
        s.questions.forEach(q => {
            q.id = finalId++;
        });
    });
});

fs.writeFileSync('public/unit5_ielts.json', JSON.stringify(unit5, null, 2));
console.log('Unit 5 generated successfully.');
