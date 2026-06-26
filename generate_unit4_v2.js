const fs = require('fs');

// ============================================================
// UNIT 4: OH, TEMPTATION
// ============================================================

const wordsList1 = [
    { word: "temptation", pos: "n.", pronunciation: "[tempˈteɪʃn]", eng: "a desire to do something, especially something wrong or unwise.", eng_vie: "(sự cám dỗ, sự quyến rũ)", ex: "He felt the temptation to eat the whole cake.", ex_vie: "(Anh ấy cảm thấy sự cám dỗ muốn ăn hết cả cái bánh.)" },
    { word: "if only", pos: "phrase", pronunciation: "[ɪf ˈoʊnli]", eng: "used to express a wish.", eng_vie: "(giá mà)", ex: "If only fast food were truly addictive.", ex_vie: "(Giá như thức ăn nhanh thực sự gây nghiện.)" },
    { word: "fast food", pos: "n.", pronunciation: "[fæst fuːd]", eng: "food that can be prepared quickly and easily.", eng_vie: "(thức ăn nhanh)", ex: "She eats too much fast food.", ex_vie: "(Cô ấy ăn quá nhiều thức ăn nhanh.)" },
    { word: "addictive", pos: "adj.", pronunciation: "[əˈdɪktɪv]", eng: "causing or likely to cause an addiction.", eng_vie: "(nghiện, hấp dẫn)", ex: "Nicotine is a highly addictive substance.", ex_vie: "(Nicotine là một chất gây nghiện rất cao.)" },
    { word: "file", pos: "v.", pronunciation: "[faɪl]", eng: "to submit (a legal document, application, or charge) to be placed on record.", eng_vie: "(nộp, đưa (đơn))", ex: "He filed a lawsuit against the company.", ex_vie: "(Anh ta đã đệ đơn kiện công ty.)" },
    { word: "class-action", pos: "n.", pronunciation: "[klæs ˈækʃn]", eng: "a lawsuit filed or defended by an individual acting on behalf of a group.", eng_vie: "(tập thể)", ex: "They filed a class-action lawsuit.", ex_vie: "(Họ đã đệ đơn kiện tập thể.)" },
    { word: "lawsuit", pos: "n.", pronunciation: "[ˈlɔːsuːt]", eng: "a claim or dispute brought to a court of law.", eng_vie: "(việc kiện cáo, việc tố tụng)", ex: "The absurd lawsuit may have been inevitable.", ex_vie: "(Vụ kiện vô lý có thể là không thể tránh khỏi.)" },
    { word: "claim", pos: "n.", pronunciation: "[kleɪm]", eng: "a demand or request for something considered one's due.", eng_vie: "(sự đòi, sự yêu sách)", ex: "His claim was that they were responsible.", ex_vie: "(Yêu sách của anh ta là họ phải chịu trách nhiệm.)" },
    { word: "obesity", pos: "n.", pronunciation: "[oʊˈbiːsəti]", eng: "the condition of being grossly fat or overweight.", eng_vie: "(sự béo phì)", ex: "Obesity is a major health problem.", ex_vie: "(Béo phì là một vấn đề sức khỏe lớn.)" },
    { word: "craving", pos: "n.", pronunciation: "[ˈkreɪvɪŋ]", eng: "a powerful desire for something.", eng_vie: "(sự thèm muốn, lòng khao khát)", ex: "Fast food had created a craving in his client.", ex_vie: "(Thức ăn nhanh đã tạo ra một sự thèm muốn ở thân chủ của ông ấy.)" },
    { word: "hapless", pos: "adj.", pronunciation: "[ˈhæpləs]", eng: "unfortunate.", eng_vie: "(rủi ro, không may)", ex: "The hapless victim was completely unaware.", ex_vie: "(Nạn nhân kém may mắn hoàn toàn không biết gì.)" },
    { word: "client", pos: "n.", pronunciation: "[ˈklaɪənt]", eng: "a person using the services of a professional person or organization.", eng_vie: "(khách hàng, thân chủ)", ex: "The lawyer represented his client well.", ex_vie: "(Luật sư đã đại diện tốt cho thân chủ của mình.)" },
    { word: "blissfully", pos: "adv.", pronunciation: "[ˈblɪsfəli]", eng: "in a manner characterized by extreme happiness or joy.", eng_vie: "(hạnh phúc, sung sướng)", ex: "He was blissfully unaware of the danger.", ex_vie: "(Anh ta sung sướng không hề biết về mối nguy hiểm.)" },
    { word: "unaware", pos: "adj.", pronunciation: "[ˌʌnəˈwer]", eng: "having no knowledge of a situation or fact.", eng_vie: "(không biết, không hay)", ex: "She was completely unaware of the changes.", ex_vie: "(Cô ấy hoàn toàn không hay biết về những thay đổi.)" },
    { word: "consume", pos: "v.", pronunciation: "[kənˈsuːm]", eng: "to eat, drink, or ingest.", eng_vie: "(dùng, tiêu thụ)", ex: "Consuming huge piles of burgers is not healthy.", ex_vie: "(Tiêu thụ một đống lớn bánh mì kẹp thịt thì không tốt cho sức khỏe.)" },
    { word: "absurd", pos: "adj.", pronunciation: "[əbˈsɜːrd]", eng: "wildly unreasonable, illogical, or inappropriate.", eng_vie: "(vô lý, lố bịch)", ex: "It was an absurd lawsuit.", ex_vie: "(Đó là một vụ kiện lố bịch.)" },
    { word: "inevitable", pos: "adj.", pronunciation: "[ɪnˈevɪtəbl]", eng: "certain to happen; unavoidable.", eng_vie: "(tất yếu, không thể tránh được)", ex: "The accident was inevitable.", ex_vie: "(Vụ tai nạn là không thể tránh khỏi.)" },
    { word: "settlement", pos: "n.", pronunciation: "[ˈsetlmənt]", eng: "an official agreement intended to resolve a dispute or conflict.", eng_vie: "(sự dàn xếp, sự hòa giải)", ex: "They reached a settlement out of court.", ex_vie: "(Họ đã đạt được một thỏa thuận hòa giải ngoài tòa án.)" },
    { word: "catch", pos: "n.", pronunciation: "[kætʃ]", eng: "a hidden problem or disadvantage in an apparently ideal situation.", eng_vie: "(điều bất lợi)", ex: "There is a catch: fast food is not addictive.", ex_vie: "(Có một điều bất lợi: thức ăn nhanh không gây nghiện.)" },
    { word: "as a matter of fact", pos: "phrase", pronunciation: "[əz ə ˈmætər əv fækt]", eng: "in reality; actually.", eng_vie: "(vì vậy, thực tế là)", ex: "As a matter of fact, I do know him.", ex_vie: "(Thực tế là tôi có biết anh ta.)" },
    { word: "contain", pos: "v.", pronunciation: "[kənˈteɪn]", eng: "to have or hold within.", eng_vie: "(chứa, đựng)", ex: "The box contains some old books.", ex_vie: "(Chiếc hộp chứa một vài cuốn sách cũ.)" },
    { word: "substance", pos: "n.", pronunciation: "[ˈsʌbstəns]", eng: "a particular kind of matter with uniform properties.", eng_vie: "(chất)", ex: "It contains no addictive substance.", ex_vie: "(Nó không chứa bất kỳ chất gây nghiện nào.)" },
    { word: "induce", pos: "v.", pronunciation: "[ɪnˈduːs]", eng: "to succeed in persuading or influencing someone to do something.", eng_vie: "(gây ra, đem lại)", ex: "Nothing could induce me to change my mind.", ex_vie: "(Không gì có thể thuyết phục tôi thay đổi ý định.)" },
    { word: "plight", pos: "n.", pronunciation: "[plaɪt]", eng: "a dangerous, difficult, or otherwise unfortunate situation.", eng_vie: "(hoàn cảnh, cảnh ngộ)", ex: "Consider the plight of the poor plaintiffs.", ex_vie: "(Hãy xem xét hoàn cảnh của những nguyên đơn nghèo khổ.)" },
    { word: "plaintiff", pos: "n.", pronunciation: "[ˈpleɪntɪf]", eng: "a person who brings a case against another in a court of law.", eng_vie: "(nguyên đơn, người đứng đơn kiện)", ex: "The plaintiff won the lawsuit.", ex_vie: "(Nguyên đơn đã thắng kiện.)" },
    { word: "compel", pos: "v.", pronunciation: "[kəmˈpel]", eng: "to force or oblige someone to do something.", eng_vie: "(buộc phải, bắt buộc)", ex: "They were physiologically compelled to consume fast food.", ex_vie: "(Họ bị ép buộc về mặt sinh lý phải tiêu thụ đồ ăn nhanh.)" },
    { word: "common sense", pos: "n.", pronunciation: "[ˌkɑːmən ˈsens]", eng: "good sense and sound judgment in practical matters.", eng_vie: "(lẽ thường)", ex: "Use your common sense.", ex_vie: "(Hãy sử dụng lẽ thường của bạn.)" },
    { word: "indulge in", pos: "phrasal v.", pronunciation: "[ɪnˈdʌldʒ ɪn]", eng: "to allow oneself to enjoy the pleasure of.", eng_vie: "(ham mê, say mê)", ex: "Millions more indulge in the stuff.", ex_vie: "(Hàng triệu người khác say mê thứ đó.)" },
    { word: "suborn", pos: "v.", pronunciation: "[səˈbɔːrn]", eng: "to bribe or otherwise induce someone to commit an unlawful act.", eng_vie: "(hối lộ, mua chuộc)", ex: "They knew they had been suborned into doing so.", ex_vie: "(Họ biết rằng mình đã bị mua chuộc để làm như vậy.)" },
];

const wordsList2 = [
    { word: "genuine", pos: "adj.", pronunciation: "[ˈdʒenjuɪn]", eng: "truly what something is said to be; authentic.", eng_vie: "(thật, chính xác, thành thật)", ex: "Once fast food became a genuine compulsion.", ex_vie: "(Một khi thức ăn nhanh trở thành một sự ép buộc thực sự.)" },
    { word: "compulsion", pos: "n.", pronunciation: "[kəmˈpʌlʃn]", eng: "an irresistible urge to behave in a certain way.", eng_vie: "(sự ép buộc, sự cưỡng bức)", ex: "Eating disorder is a compulsion.", ex_vie: "(Rối loạn ăn uống là một sự cưỡng bức.)" },
    { word: "objection", pos: "n.", pronunciation: "[əbˈdʒekʃn]", eng: "an expression or feeling of disapproval or opposition.", eng_vie: "(sự phản đối, sự chống đối)", ex: "There could be no economic or moral objection.", ex_vie: "(Không thể có sự phản đối nào về mặt kinh tế hay đạo đức.)" },
    { word: "regulate", pos: "v.", pronunciation: "[ˈreɡjuleɪt]", eng: "to control or maintain the rate or speed of (a machine or process).", eng_vie: "(quy định)", ex: "Alcohol and tobacco are regulated.", ex_vie: "(Rượu và thuốc lá đều bị quy định chặt chẽ.)" },
    { word: "consumption", pos: "n.", pronunciation: "[kənˈsʌmpʃn]", eng: "the using up of a resource.", eng_vie: "(sự tiêu thụ)", ex: "Regulating its consumption.", ex_vie: "(Quy định việc tiêu thụ nó.)" },
    { word: "revenue", pos: "n.", pronunciation: "[ˈrevənuː]", eng: "income, especially when of a company or organization.", eng_vie: "(thu nhập)", ex: "The revenue from this tax could be used.", ex_vie: "(Doanh thu từ khoản thuế này có thể được sử dụng.)" },
    { word: "sin tax", pos: "n.", pronunciation: "[sɪn tæks]", eng: "a tax on items considered undesirable or harmful, such as alcohol or tobacco.", eng_vie: "(thuế đánh vào những sản phẩm có thể gây hại như rượu bia, thuốc lá)", ex: "A sin tax on fast food.", ex_vie: "(Thuế tội lỗi đối với thức ăn nhanh.)" },
    { word: "wean off", pos: "phrasal v.", pronunciation: "[wiːn ɔːf]", eng: "to make someone gradually stop doing or using something.", eng_vie: "(bỏ, cai)", ex: "To wean people off bad food.", ex_vie: "(Để cai nghiện thức ăn không lành mạnh cho mọi người.)" },
    { word: "balance", pos: "v.", pronunciation: "[ˈbæləns]", eng: "to keep or put (something) in a steady position.", eng_vie: "(cân đối)", ex: "On balancing budgets.", ex_vie: "(Trong việc cân đối ngân sách.)" },
    { word: "budget", pos: "n.", pronunciation: "[ˈbʌdʒɪt]", eng: "an estimate of income and expenditure for a set period of time.", eng_vie: "(ngân sách)", ex: "The school has a strict budget.", ex_vie: "(Trường có một ngân sách nghiêm ngặt.)" },
    { word: "prudent", pos: "adj.", pronunciation: "[ˈpruːdnt]", eng: "acting with or showing care and thought for the future.", eng_vie: "(thận trọng, khôn ngoan)", ex: "It is prudent to save money.", ex_vie: "(Việc tiết kiệm tiền là rất khôn ngoan.)" },
    { word: "defendant", pos: "n.", pronunciation: "[dɪˈfendənt]", eng: "an individual, company, or institution sued or accused in a court of law.", eng_vie: "(bị cáo)", ex: "Making fast food addictive could help the defendants as well.", ex_vie: "(Làm cho thức ăn nhanh gây nghiện cũng có thể giúp ích cho các bị cáo.)" },
    { word: "living proof", pos: "n.", pronunciation: "[ˈlɪvɪŋ pruːf]", eng: "a person who provides an example of something.", eng_vie: "(bằng chứng sống)", ex: "Tobacco firms are living proof of this.", ex_vie: "(Các hãng thuốc lá là một bằng chứng sống cho điều này.)" },
    { word: "murderous", pos: "adj.", pronunciation: "[ˈmɜːrdərəs]", eng: "capable of or intending to murder; dangerously violent.", eng_vie: "(giết người, tàn sát)", ex: "Even after murderous litigation.", ex_vie: "(Ngay cả sau vụ kiện tàn sát.)" },
    { word: "litigation", pos: "n.", pronunciation: "[ˌlɪtɪˈɡeɪʃn]", eng: "the process of taking legal action.", eng_vie: "(sự kiện tụng, sự tranh chấp)", ex: "The company faces costly litigation.", ex_vie: "(Công ty phải đối mặt với vụ kiện tốn kém.)" },
    { word: "universally", pos: "adv.", pronunciation: "[ˌjuːnɪˈvɜːrsəli]", eng: "by everyone; in every case.", eng_vie: "(khắp nơi, phổ biến)", ex: "You can be universally reviled and still successful.", ex_vie: "(Bạn có thể bị cả thế giới chửi rủa mà vẫn thành công.)" },
    { word: "revile", pos: "v.", pronunciation: "[rɪˈvaɪl]", eng: "to criticize in an abusive or angrily insulting manner.", eng_vie: "(chửi mắng, xỉ vả)", ex: "The politician was reviled by the press.", ex_vie: "(Chính trị gia đó đã bị báo chí xỉ vả.)" },
    { word: "nigh", pos: "adj.", pronunciation: "[naɪ]", eng: "near.", eng_vie: "(sớm (xảy ra))", ex: "Some thought the end of the industry was nigh.", ex_vie: "(Một số người nghĩ rằng ngày tàn của ngành công nghiệp này sắp đến.)" },
    { word: "far from", pos: "phrase", pronunciation: "[fɑːr frəm]", eng: "not at all.", eng_vie: "(không hề, hầu như là trái lại)", ex: "Far from it.", ex_vie: "(Hoàn toàn không phải vậy.)" },
    { word: "fiddly", pos: "adj.", pronunciation: "[ˈfɪdli]", eng: "complicated or detailed and awkward to do or use.", eng_vie: "(vớ vẩn, vô nghĩa)", ex: "Fiddly rules about not marketing to small children.", ex_vie: "(Những quy định vớ vẩn về việc không tiếp thị cho trẻ nhỏ.)" },
    { word: "firm", pos: "n.", pronunciation: "[fɜːrm]", eng: "a business or company.", eng_vie: "(hãng sản xuất)", ex: "Cigarette firms can still earn money.", ex_vie: "(Các hãng thuốc lá vẫn có thể kiếm được tiền.)" },
    { word: "follow suit", pos: "idiom", pronunciation: "[ˈfɑːloʊ suːt]", eng: "to conform to another's actions.", eng_vie: "(làm theo như vậy)", ex: "Fast-food companies could follow suit.", ex_vie: "(Các công ty thức ăn nhanh có thể sẽ làm theo như vậy.)" },
    { word: "reap", pos: "v.", pronunciation: "[riːp]", eng: "to receive (a reward or benefit) as a consequence of one's own or other people's actions.", eng_vie: "(gặt hái, thu hoạch, hưởng)", ex: "They reap both public-relations and financial victories.", ex_vie: "(Họ gặt hái cả chiến thắng về mặt quan hệ công chúng lẫn tài chính.)" },
    { word: "financial", pos: "adj.", pronunciation: "[faɪˈnænʃl]", eng: "relating to finance or finances.", eng_vie: "(thuộc tài chính)", ex: "Financial victories.", ex_vie: "(Chiến thắng về tài chính.)" },
    { word: "stockmarket", pos: "n.", pronunciation: "[ˈstɑːkmɑːrkɪt]", eng: "a stock exchange.", eng_vie: "(thị trường chứng khoán)", ex: "Theirs was the best-performing industry in the stockmarket.", ex_vie: "(Của họ là ngành hoạt động tốt nhất trên thị trường chứng khoán.)" },
];

function wordHtml(w) {
    return `<div style="display:flex;gap:16px;align-items:flex-start;"><div style="width:32px;height:32px;flex-shrink:0;background-color:#f8fafc;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 3px rgba(0,0,0,0.1);border:1px solid #e2e8f0;font-size:16px;">😎</div><div style="display:flex;flex-direction:column;gap:6px;"><div style="display:flex;align-items:baseline;gap:8px;"><span style="font-size:1.25rem;font-weight:800;color:#65a30d;">${w.word}</span><span style="font-size:0.875rem;color:#94a3b8;font-family:monospace;">${w.pronunciation}</span><span style="font-size:0.875rem;color:#94a3b8;font-style:italic;">${w.pos}</span></div><div style="color:#475569;font-size:0.95rem;line-height:1.5;">${w.eng} <span style="color:#0ea5e9;">${w.eng_vie}</span></div><div style="color:#64748b;font-size:0.95rem;font-style:italic;">→ ${w.ex} <span style="color:#0ea5e9;">${w.ex_vie}</span></div></div></div>`;
}
function generateDetailedMeanings(words) {
    return `<div style="display:flex;flex-direction:column;gap:24px;padding-top:24px;border-top:1px dashed #cbd5e1;"><h3 style="font-size:1.125rem;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:0.05em;margin:0;">Detailed Meanings</h3><div style="display:flex;flex-direction:column;gap:24px;">${words.map(w => wordHtml(w)).join('')}</div></div>`;
}

const word1Content = `<p style="display: none;">Word List 1</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="/unit4_ielts_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" />${generateDetailedMeanings(wordsList1)}</div>`;
const word2Content = `<p style="display: none;">Word List 2</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="/unit4_ielts_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" />${generateDetailedMeanings(wordsList2)}</div>`;

const readingContent = `<p style="display: none;">Comprehensive Reading</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="/unit4_ielts_story.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Oh, Temptation</h1><p style="margin-bottom: 1rem;"><b>If only fast food</b> were truly <b>addictive</b>.</p><p style="margin-bottom: 1rem;">Last week, Caesar Barber of New York <b>filed</b> a <b>class-action lawsuit</b> against McDonald's, Kentucky Fried Chicken, Burger King and Wendy's, four of the world's biggest fast-food chains. His <b>claim</b> was that they were responsible for his <b>obesity</b> and poor health. According to his lawyer, fast food had created a "<b>craving</b>" in his <b>hapless client</b>, who was <b>blissfully unaware</b>, until his doctor told him, that <b>consuming</b> huge piles of burgers, fries and milkshakes was not actually good for his health.</p><p style="margin-bottom: 1rem;">Such an <b>absurd</b> lawsuit may have been <b>inevitable</b> as soon as the big tobacco <b>settlements</b> began burning a hole in trial lawyers' pockets. But there is a <b>catch</b>: fast food is not addictive. It does not, <b>as a matter of fact</b>, create a real physical craving, because it <b>contains</b> no <b>substance</b> that could <b>induce</b> one.</p><p style="margin-bottom: 1rem;">The Economist suggests that this should now change. Consider the <b>plight</b> of the poor <b>plaintiffs</b>. They must prove that they were physiologically <b>compelled</b> to consume fast food, against the weight of scientific evidence and the dictates of <b>common sense</b>. Then there are the millions more who <b>indulge in</b> the stuff, but who would feel much better about themselves if they knew they had been <b>suborned</b> into doing so. Through the simple introduction of minute amounts of cocaine or nicotine into their wares, fast-food companies could improve the lot of such folk in future.</p><p style="margin-bottom: 1rem;">The benefits would not stop there. Nobody should be keener for fast food to be made addictive than governments. Once fast food became a <b>genuine compulsion</b>, there could be no economic or moral <b>objection</b> to <b>regulating</b> its <b>consumption</b>, as alcohol and tobacco are regulated, and to taxing it. The <b>revenue</b> from this "<b>sin tax</b>" could be used in a pretend effort to <b>wean</b> people <b>off</b> bad food. Many states spent their millions from tobacco settlements on <b>balancing budgets</b>, improving roads or paying teachers more. Supposedly, people in fiscally <b>prudent</b>, literate and well-paved places felt less urge to light up.</p><p style="margin-bottom: 1rem;">Making fast food addictive could help the <b>defendants</b> as well. They might follow the tobacco <b>firms</b>, who are <b>living proof</b> that even after <b>murderous litigation</b> you can be both <b>universally reviled</b> and still successful. When the big tobacco lawsuits finished, some thought the end of the industry was <b>nigh</b>. <b>Far from</b> it: they may have to obey <b>fiddly</b> rules about not marketing to small children in North America, but cigarette firms can still earn money in the rest of the world. Last year, theirs was the best-performing industry in the <b>stockmarket</b>. Fast-food companies could <b>follow suit</b> and <b>reap</b> both public-relations and <b>financial</b> victories.</p></div></div>`;

const unit4 = {
  "title": "Unit 4: Oh, Temptation",
  "parts": [
    {
      "title": "Word List 1",
      "content": word1Content,
      "sections": [
        {
          "title": "Exercise 1: Choose the correct word to fill in the blank.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            { "id": 1, "content": "I tried to resist the ________ to laugh.", "options": ["temptation", "craving", "settlement", "claim"], "correctAnswer": "A", "explanation": "Temptation means a desire to do something, especially something wrong or unwise." },
            { "id": 2, "content": "They ________ an application to have their case heard early.", "options": ["consumed", "compelled", "filed", "induced"], "correctAnswer": "C", "explanation": "File means to submit a legal document to be placed on record." },
            { "id": 3, "content": "A confrontation was ________ because they disliked each other so much.", "options": ["absurd", "inevitable", "hapless", "addictive"], "correctAnswer": "B", "explanation": "Inevitable means certain to happen; unavoidable." },
            { "id": 4, "content": "Heroin is an illegal ________.", "options": ["claim", "substance", "settlement", "plight"], "correctAnswer": "B", "explanation": "Substance means a particular kind of matter with uniform properties." },
            { "id": 5, "content": "________, I do know him.", "options": ["If only", "Far from", "As a matter of fact", "To no avail"], "correctAnswer": "C", "explanation": "As a matter of fact means in reality; actually." }
          ]
        },
        {
          "title": "Exercise 2: Choose the word that best matches the definition.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            { "id": 6, "content": "The condition of being grossly fat or overweight", "options": ["Craving", "Obesity", "Temptation", "Plight"], "correctAnswer": "B", "explanation": "Obesity is the condition of being grossly fat or overweight." },
            { "id": 7, "content": "A person who brings a case against another in a court of law", "options": ["Client", "Defendant", "Plaintiff", "Hapless"], "correctAnswer": "C", "explanation": "A plaintiff is a person who brings a case against another in a court of law." },
            { "id": 8, "content": "To force or oblige someone to do something", "options": ["Induce", "Compel", "Consume", "Suborn"], "correctAnswer": "B", "explanation": "Compel means to force or oblige someone to do something." }
          ]
        },
        {
          "title": "Exercise 3: Mark each statement T for true or F for false.",
          "content": "<p class=\"font-bold text-[16px] text-slate-800 mb-4\">True / False</p>",
          "questionType": "TFNG",
          "questions": [
            { "id": 9, "content": "A 'class-action' lawsuit is filed by one person on behalf of a group.", "options": ["True", "False"], "correctAnswer": "True", "explanation": "True. A class-action lawsuit is filed or defended by an individual acting on behalf of a group." },
            { "id": 10, "content": "If someone is 'blissfully unaware', they know exactly what is happening.", "options": ["True", "False"], "correctAnswer": "False", "explanation": "False. Blissfully unaware means having no knowledge of a situation, while feeling happy." },
            { "id": 11, "content": "To 'indulge in' something means to allow oneself to enjoy the pleasure of it.", "options": ["True", "False"], "correctAnswer": "True", "explanation": "True. Indulge in means to allow oneself to enjoy the pleasure of something." }
          ]
        }
      ]
    },
    {
      "title": "Word List 2",
      "content": word2Content,
      "sections": [
        {
          "title": "Exercise 1: Choose the correct word to fill in the blank.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            { "id": 12, "content": "Alcohol and tobacco are ________ by the government.", "options": ["regulated", "reviled", "reaped", "balanced"], "correctAnswer": "A", "explanation": "Regulate means to control or maintain the rate or speed of a process." },
            { "id": 13, "content": "The company faces costly ________.", "options": ["revenue", "litigation", "compulsion", "stockmarket"], "correctAnswer": "B", "explanation": "Litigation is the process of taking legal action." },
            { "id": 14, "content": "It is ________ to save money for the future.", "options": ["fiddly", "nigh", "prudent", "murderous"], "correctAnswer": "C", "explanation": "Prudent means acting with care and thought for the future." },
            { "id": 15, "content": "Fast-food companies could ________ and reap financial victories.", "options": ["follow suit", "wean off", "far from", "living proof"], "correctAnswer": "A", "explanation": "Follow suit means to conform to another's actions." }
          ]
        },
        {
          "title": "Exercise 2: Write C if the italicized word is used correctly. Write I if the word is used incorrectly.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            { "id": 16, "content": "The <i>revenue</i> from taxes can be used to improve public services.", "options": ["C", "I"], "correctAnswer": "A", "explanation": "Correct. Revenue means income, especially when of a company or organization." },
            { "id": 17, "content": "The <i>defendant</i> is the person who brings a case to court.", "options": ["C", "I"], "correctAnswer": "B", "explanation": "Incorrect. A defendant is the person who is sued or accused, not the one who brings the case." },
            { "id": 18, "content": "The politician was <i>universally reviled</i>, meaning everyone praised him.", "options": ["C", "I"], "correctAnswer": "B", "explanation": "Incorrect. Universally reviled means criticized by everyone, not praised." }
          ]
        },
        {
          "title": "Exercise 3: Choose the word that best matches the definition.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            { "id": 19, "content": "An irresistible urge to behave in a certain way", "options": ["Objection", "Compulsion", "Revenue", "Litigation"], "correctAnswer": "B", "explanation": "Compulsion is an irresistible urge to behave in a certain way." },
            { "id": 20, "content": "To receive a reward or benefit as a consequence of actions", "options": ["Regulate", "Revile", "Reap", "Balance"], "correctAnswer": "C", "explanation": "Reap means to receive a reward or benefit as a consequence of actions." },
            { "id": 21, "content": "Truly what something is said to be; authentic", "options": ["Prudent", "Genuine", "Fiddly", "Nigh"], "correctAnswer": "B", "explanation": "Genuine means truly what something is said to be; authentic." }
          ]
        }
      ]
    },
    {
      "title": "Comprehensive Reading",
      "content": readingContent,
      "explanation": "Transcript and Reading Passage Explanation",
      "sections": [
        {
          "title": "Exercise 1: Fill in each blank with the appropriate word",
          "content": "<p class=\"font-bold text-[16px] text-slate-800 mb-4\">Drag and drop the correct words into the blanks.</p>",
          "questionType": "Kéo thả",
          "questions": (() => {
            const blanks = [
              { answer: "addictive" },
              { answer: "class-action" },
              { answer: "obesity" },
              { answer: "craving" },
              { answer: "inevitable" },
              { answer: "substance" },
              { answer: "plaintiffs" },
              { answer: "compelled" },
              { answer: "genuine" },
              { answer: "regulating" },
              { answer: "follow suit" }
            ];
            const allOptions = blanks.map(b => b.answer);
            const contentText = `1. If only fast food were truly [ 1 ].<br/><br/>2. Caesar Barber filed a [ 2 ] lawsuit against fast-food chains.<br/><br/>3. His claim was that they were responsible for his [ 3 ].<br/><br/>4. Fast food had created a "[ 4 ]" in his hapless client.<br/><br/>5. Such an absurd lawsuit may have been [ 5 ].<br/><br/>6. It contains no [ 6 ] that could induce a craving.<br/><br/>7. Consider the plight of the poor [ 7 ].<br/><br/>8. They must prove that they were physiologically [ 8 ] to consume fast food.<br/><br/>9. Once fast food became a [ 9 ] compulsion...<br/><br/>10. There could be no objection to [ 10 ] its consumption.<br/><br/>11. Fast-food companies could [ 11 ] and reap financial victories.`;
            return blanks.map((b, i) => ({
              "id": 22 + i,
              "content": i === 0 ? contentText : "",
              "options": allOptions,
              "correctAnswer": b.answer
            }));
          })()
        },
        {
          "title": "Exercise 2: Reading Comprehension",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            { "id": 33, "content": "What was Caesar Barber's main claim in the lawsuit?", "options": ["Fast-food chains used illegal substances in their food.", "Fast-food chains were responsible for his obesity and poor health.", "Fast-food chains refused to serve him.", "Fast-food chains discriminated against him."], "correctAnswer": "B", "explanation": "The text states: 'His claim was that they were responsible for his obesity and poor health.'" },
            { "id": 34, "content": "According to the passage, why is the lawsuit considered 'absurd'?", "options": ["Because the plaintiff was not really obese.", "Because fast food is not actually addictive and contains no addictive substance.", "Because the fast-food chains had already settled.", "Because the judge dismissed the case immediately."], "correctAnswer": "B", "explanation": "The text says: 'fast food is not addictive. It does not, as a matter of fact, create a real physical craving, because it contains no substance that could induce one.'" },
            { "id": 35, "content": "What satirical suggestion does The Economist make?", "options": ["Fast-food companies should lower their prices.", "Fast-food companies should add addictive substances to their food.", "Fast-food companies should close their restaurants.", "Fast-food companies should only serve healthy food."], "correctAnswer": "B", "explanation": "The text satirically suggests: 'Through the simple introduction of minute amounts of cocaine or nicotine into their wares, fast-food companies could improve the lot of such folk.'" },
            { "id": 36, "content": "What does the passage say about tobacco companies after major lawsuits?", "options": ["They went bankrupt.", "They became universally praised.", "They were universally reviled but still successful.", "They stopped selling tobacco products."], "correctAnswer": "C", "explanation": "The text states: tobacco firms 'are living proof that even after murderous litigation you can be both universally reviled and still successful.'" }
          ]
        }
      ]
    }
  ],
  "basicInfo": {
    "skill": "MCQ (Standard)",
    "title": "Unit 4: Oh, Temptation",
    "category": "exercise",
    "courseId": "239a64f0-c106-40e5-a6e2-4e685a0d70fb",
    "timeLimit": 40
  }
};

fs.writeFileSync('public/unit4_ielts.json', JSON.stringify(unit4, null, 2));
console.log('Unit 4 JSON generated successfully! (Unit 1 format)');
