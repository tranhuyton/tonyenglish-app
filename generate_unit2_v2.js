const fs = require('fs');

// ============================================================
// UNIT 2: SIESTA TIME - Generate JSON in Unit 1 format
// ============================================================

// --- Word List 1 words ---
const wordsList1 = [
    { word: "siesta", pos: "n.", pronunciation: "[siˈestə]", eng: "an afternoon rest or nap.", eng_vie: "(giấc ngủ trưa)", ex: "Everyone takes a siesta after lunch.", ex_vie: "(Mọi người đều ngủ trưa sau bữa trưa.)" },
    { word: "work wonders", pos: "phrase", pronunciation: "[wɜːrk ˈwʌndərz]", eng: "to have a very beneficial effect.", eng_vie: "(rất có hiệu quả, đem lại những kết quả tích cực)", ex: "A good night's sleep can work wonders for your health.", ex_vie: "(Một giấc ngủ ngon có thể mang lại hiệu quả kỳ diệu cho sức khỏe.)" },
    { word: "vindication", pos: "n.", pronunciation: "[ˌvɪndɪˈkeɪʃn]", eng: "proof that someone or something is right or justified.", eng_vie: "(sự chứng minh, sự bào chữa)", ex: "The new evidence provided vindication for the scientist's theory.", ex_vie: "(Bằng chứng mới đã chứng minh cho lý thuyết của nhà khoa học.)" },
    { word: "power", pos: "n.", pronunciation: "[ˈpaʊər]", eng: "ability to do or act.", eng_vie: "(năng lực, khả năng)", ex: "She has the power to change things.", ex_vie: "(Cô ấy có khả năng thay đổi mọi thứ.)" },
    { word: "napper", pos: "n.", pronunciation: "[ˈnæpər]", eng: "a person who takes short sleeps during the day.", eng_vie: "(người ngủ trưa)", ex: "He is a frequent napper on weekends.", ex_vie: "(Anh ấy thường xuyên ngủ trưa vào cuối tuần.)" },
    { word: "far from", pos: "phrase", pronunciation: "[fɑːr frəm]", eng: "not at all.", eng_vie: "(chẳng những không, không hề)", ex: "The situation is far from simple.", ex_vie: "(Tình hình chẳng hề đơn giản chút nào.)" },
    { word: "lout", pos: "n.", pronunciation: "[laʊt]", eng: "an uncouth and aggressive man or boy.", eng_vie: "(người vụng về, người cục mịch)", ex: "He behaves like a lout when he is drunk.", ex_vie: "(Anh ta cư xử như một kẻ cục mịch khi say rượu.)" },
    { word: "siesta-taker", pos: "n.", pronunciation: "[siˈestə ˈteɪkər]", eng: "a person who takes a siesta.", eng_vie: "(người ngủ trưa)", ex: "The office allowed siesta-takers a quiet room.", ex_vie: "(Văn phòng đã sắp xếp một phòng yên tĩnh cho những người ngủ trưa.)" },
    { word: "do one's bit", pos: "phrase", pronunciation: "[duː wʌnz bɪt]", eng: "to make a useful contribution to an effort.", eng_vie: "(làm công việc được giao của mình, có đóng góp đáng kể)", ex: "Everyone must do their bit to keep the park clean.", ex_vie: "(Mọi người phải làm tròn phần việc của mình để giữ công viên sạch sẽ.)" },
    { word: "colleague", pos: "n.", pronunciation: "[ˈkɑːliːɡ]", eng: "a person with whom one works.", eng_vie: "(đồng nghiệp)", ex: "I discussed the project with my colleagues.", ex_vie: "(Tôi đã thảo luận dự án với các đồng nghiệp.)" },
    { word: "shut-eye", pos: "n.", pronunciation: "[ˈʃʌt aɪ]", eng: "sleep.", eng_vie: "(chợp mắt)", ex: "I need to get some shut-eye before the trip.", ex_vie: "(Tôi cần chợp mắt một chút trước chuyến đi.)" },
    { word: "perform", pos: "v.", pronunciation: "[pərˈfɔːrm]", eng: "to carry out, accomplish, or fulfill.", eng_vie: "(làm việc, thi hành)", ex: "The surgeon performed the operation successfully.", ex_vie: "(Bác sĩ phẫu thuật đã thực hiện ca phẫu thuật thành công.)" },
    { word: "fresh daisy", pos: "phrase", pronunciation: "[freʃ ˈdeɪzi]", eng: "healthy, energetic, and full of life.", eng_vie: "(hoa cúc tươi, (nghĩa bóng) tươi tắn)", ex: "After a nap, she felt like a fresh daisy.", ex_vie: "(Sau giấc ngủ trưa, cô ấy cảm thấy tươi tắn như hoa cúc.)" },
    { word: "bona fide", pos: "adj.", pronunciation: "[ˌboʊnə ˈfaɪdi]", eng: "genuine; real.", eng_vie: "(thật sự)", ex: "Make sure you are dealing with a bona fide company.", ex_vie: "(Hãy chắc chắn rằng bạn đang làm việc với một công ty thực sự.)" },
    { word: "mere", pos: "adj.", pronunciation: "[mɪr]", eng: "used to emphasize how small or insignificant someone or something is.", eng_vie: "(chỉ là)", ex: "It costs a mere twenty dollars.", ex_vie: "(Nó chỉ tốn hai mươi đô la.)" },
    { word: "publish", pos: "v.", pronunciation: "[ˈpʌblɪʃ]", eng: "to prepare and issue for public sale.", eng_vie: "(xuất bản)", ex: "The author published his first book last year.", ex_vie: "(Tác giả đã xuất bản cuốn sách đầu tiên vào năm ngoái.)" },
    { word: "visual", pos: "adj.", pronunciation: "[ˈvɪʒuəl]", eng: "relating to seeing or sight.", eng_vie: "(thuộc thị giác)", ex: "The film has stunning visual effects.", ex_vie: "(Bộ phim có hiệu ứng hình ảnh tuyệt đẹp.)" },
    { word: "perception", pos: "n.", pronunciation: "[pərˈsepʃn]", eng: "the ability to see, hear, or become aware of something.", eng_vie: "(sự nhận thức)", ex: "Drugs can alter your perception of reality.", ex_vie: "(Ma túy có thể làm thay đổi nhận thức của bạn về thực tại.)" },
];

// --- Word List 2 words ---
const wordsList2 = [
    { word: "volunteer", pos: "n.", pronunciation: "[ˌvɑːlənˈtɪr]", eng: "a person who freely offers to take part in an enterprise.", eng_vie: "(người tình nguyện)", ex: "She is a volunteer at the local hospital.", ex_vie: "(Cô ấy là tình nguyện viên tại bệnh viện địa phương.)" },
    { word: "pick out", pos: "phrasal v.", pronunciation: "[pɪk aʊt]", eng: "to choose or select.", eng_vie: "(chọn ra)", ex: "Can you pick out your luggage from the pile?", ex_vie: "(Bạn có thể nhận ra hành lý của mình trong đống này không?)" },
    { word: "vertical", pos: "adj.", pronunciation: "[ˈvɜːrtɪkl]", eng: "at right angles to a horizontal plane.", eng_vie: "(thẳng đứng)", ex: "The building has vertical stripes on its facade.", ex_vie: "(Tòa nhà có các sọc thẳng đứng trên mặt tiền.)" },
    { word: "horizontal", pos: "adj.", pronunciation: "[ˌhɔːrɪˈzɑːntl]", eng: "parallel to the plane of the horizon.", eng_vie: "(nằm ngang)", ex: "Draw a horizontal line across the page.", ex_vie: "(Hãy vẽ một đường nằm ngang qua trang giấy.)" },
    { word: "bar", pos: "n.", pronunciation: "[bɑːr]", eng: "a long rigid piece of wood, metal, or similar material.", eng_vie: "(thanh, vạch ngang, vạch đường kẻ)", ex: "There are iron bars on the windows.", ex_vie: "(Có những thanh sắt trên cửa sổ.)" },
    { word: "striped", pos: "adj.", pronunciation: "[straɪpt]", eng: "marked with or having stripes.", eng_vie: "(có sọc)", ex: "He wore a blue and white striped shirt.", ex_vie: "(Anh ta mặc một chiếc áo sơ mi sọc xanh trắng.)" },
    { word: "background", pos: "n.", pronunciation: "[ˈbækɡraʊnd]", eng: "the area or scenery behind the main object.", eng_vie: "(nền)", ex: "The picture has a dark background.", ex_vie: "(Bức tranh có nền màu tối.)" },
    { word: "established", pos: "adj.", pronunciation: "[ɪˈstæblɪʃt]", eng: "having existed or done something for a long time.", eng_vie: "(đã có từ lâu nay, có uy tín)", ex: "It is an established scientific fact.", ex_vie: "(Đó là một sự thật khoa học đã được công nhận.)" },
    { word: "perceptiveness", pos: "n.", pronunciation: "[pərˈseptɪvnəs]", eng: "the ability to notice and understand things that are not obvious.", eng_vie: "(khả năng nhận thức)", ex: "Her perceptiveness helped her solve the mystery.", ex_vie: "(Khả năng nhận thức nhạy bén đã giúp cô giải quyết bí ẩn.)" },
    { word: "acute", pos: "adj.", pronunciation: "[əˈkjuːt]", eng: "having or showing a perceptive understanding or insight.", eng_vie: "(sắc sảo, nhạy)", ex: "Dogs have an acute sense of hearing.", ex_vie: "(Chó có thính giác rất nhạy.)" },
    { word: "warn off", pos: "phrasal v.", pronunciation: "[wɔːrn ɔːf]", eng: "to tell someone to stay away.", eng_vie: "(cảnh cáo không được)", ex: "The sign warned off trespassers.", ex_vie: "(Biển báo cảnh cáo những kẻ xâm nhập.)" },
    { word: "alcohol", pos: "n.", pronunciation: "[ˈælkəhɔːl]", eng: "a colorless volatile flammable liquid.", eng_vie: "(rượu)", ex: "He does not drink alcohol.", ex_vie: "(Anh ấy không uống rượu.)" },
    { word: "nicotine", pos: "n.", pronunciation: "[ˈnɪkətiːn]", eng: "a toxic colorless or yellowish oily liquid.", eng_vie: "(nicôtin)", ex: "Cigarettes contain high levels of nicotine.", ex_vie: "(Thuốc lá chứa nồng độ nicotin cao.)" },
    { word: "addict", pos: "n.", pronunciation: "[ˈædɪkt]", eng: "a person who is addicted to a particular substance.", eng_vie: "(người nghiện)", ex: "He is a recovering drug addict.", ex_vie: "(Anh ấy là một người đang cai nghiện ma túy.)" },
    { word: "indulge", pos: "v.", pronunciation: "[ɪnˈdʌldʒ]", eng: "to allow oneself to enjoy the pleasure of.", eng_vie: "(nuông chiều, chiều theo)", ex: "We decided to indulge in a little ice cream.", ex_vie: "(Chúng tôi quyết định nuông chiều bản thân với một chút kem.)" },
    { word: "uncaffeinated", pos: "adj.", pronunciation: "[ʌnˈkæfəneɪtɪd]", eng: "not containing caffeine.", eng_vie: "(không có chất ca-phê-in)", ex: "I prefer uncaffeinated drinks in the evening.", ex_vie: "(Tôi thích đồ uống không chứa caffeine vào buổi tối.)" },
    { word: "cosset", pos: "v.", pronunciation: "[ˈkɑːsɪt]", eng: "to care for and protect in an overindulgent way.", eng_vie: "(nâng niu, nuông chiều)", ex: "She cossets her pet dog.", ex_vie: "(Cô ấy cưng nựng chú chó cưng của mình.)" },
    { word: "performance", pos: "n.", pronunciation: "[pərˈfɔːrməns]", eng: "the action or process of carrying out or accomplishing an action.", eng_vie: "(hiệu suất)", ex: "Her performance in the exam was excellent.", ex_vie: "(Thành tích của cô ấy trong kỳ thi rất xuất sắc.)" },
    { word: "deteriorate", pos: "v.", pronunciation: "[dɪˈtɪriəreɪt]", eng: "to become progressively worse.", eng_vie: "(giảm giá trị, giảm chất lượng)", ex: "His health began to deteriorate rapidly.", ex_vie: "(Sức khỏe của anh ấy bắt đầu suy giảm nhanh chóng.)" },
    { word: "downhill", pos: "adv.", pronunciation: "[ˌdaʊnˈhɪl]", eng: "towards the bottom of a hill; deteriorating.", eng_vie: "(xuống dốc)", ex: "After the mistake, the project went downhill.", ex_vie: "(Sau sai lầm đó, dự án bắt đầu tuột dốc.)" },
    { word: "session", pos: "n.", pronunciation: "[ˈseʃn]", eng: "a period of time devoted to a particular activity.", eng_vie: "(buổi, phiên)", ex: "The afternoon session will start at 2 PM.", ex_vie: "(Phiên họp buổi chiều sẽ bắt đầu lúc 2 giờ.)" },
    { word: "on average", pos: "phrase", pronunciation: "[ɑːn ˈævərɪdʒ]", eng: "usually, normally.", eng_vie: "(tính trung bình)", ex: "On average, she works eight hours a day.", ex_vie: "(Trung bình, cô ấy làm việc tám giờ một ngày.)" },
    { word: "identify", pos: "v.", pronunciation: "[aɪˈdentɪfaɪ]", eng: "to establish or indicate who or what.", eng_vie: "(nhận biết)", ex: "He could not identify the suspect.", ex_vie: "(Anh ta không thể nhận diện được nghi phạm.)" },
    { word: "orientation", pos: "n.", pronunciation: "[ˌɔːriənˈteɪʃn]", eng: "the relative physical position or direction.", eng_vie: "(sự định hướng)", ex: "The building has a north-south orientation.", ex_vie: "(Tòa nhà có hướng bắc-nam.)" },
    { word: "opportunity", pos: "n.", pronunciation: "[ˌɑːpərˈtuːnəti]", eng: "a set of circumstances that makes it possible to do something.", eng_vie: "(cơ hội)", ex: "This is a great opportunity for advancement.", ex_vie: "(Đây là một cơ hội tuyệt vời để thăng tiến.)" },
    { word: "nap", pos: "v.", pronunciation: "[næp]", eng: "to sleep lightly or briefly, especially during the day.", eng_vie: "(ngủ chợp mắt, ngủ trưa)", ex: "I usually nap for 20 minutes after lunch.", ex_vie: "(Tôi thường ngủ trưa 20 phút sau bữa trưa.)" },
    { word: "snooze", pos: "n.", pronunciation: "[snuːz]", eng: "a short, light sleep.", eng_vie: "(giấc ngủ ngắn (ban ngày))", ex: "He had a quick snooze on the sofa.", ex_vie: "(Anh ấy đã chợp mắt một lát trên ghế sofa.)" },
    { word: "do the trick", pos: "idiom", pronunciation: "[duː ðə trɪk]", eng: "to accomplish the required task.", eng_vie: "(có hiệu quả)", ex: "A little oil should do the trick.", ex_vie: "(Một chút dầu sẽ có hiệu quả.)" },
    { word: "to no avail", pos: "idiom", pronunciation: "[tə noʊ əˈveɪl]", eng: "without success.", eng_vie: "(không có hiệu quả)", ex: "They tried to save the house, but to no avail.", ex_vie: "(Họ đã cố gắng cứu ngôi nhà, nhưng vô ích.)" },
    { word: "decline", pos: "v.", pronunciation: "[dɪˈklaɪn]", eng: "to become smaller, fewer, or less.", eng_vie: "(giảm xuống)", ex: "The company's profits declined last year.", ex_vie: "(Lợi nhuận của công ty đã giảm vào năm ngoái.)" },
    { word: "motivation", pos: "n.", pronunciation: "[ˌmoʊtɪˈveɪʃn]", eng: "the reason or reasons one has for acting or behaving.", eng_vie: "(động cơ thúc đẩy)", ex: "His motivation for studying hard is to get a good job.", ex_vie: "(Động lực học tập chăm chỉ của anh ấy là để có được một công việc tốt.)" },
    { word: "upshot", pos: "n.", pronunciation: "[ˈʌpʃɑːt]", eng: "the final or eventual outcome.", eng_vie: "(kết luận, kết quả)", ex: "The upshot of the meeting was a new policy.", ex_vie: "(Kết quả của cuộc họp là một chính sách mới.)" },
    { word: "evidence", pos: "n.", pronunciation: "[ˈevɪdəns]", eng: "the available body of facts indicating whether a belief is valid.", eng_vie: "(chứng cớ)", ex: "There is no evidence to support his claim.", ex_vie: "(Không có bằng chứng nào hỗ trợ cho tuyên bố của anh ta.)" },
    { word: "mammal", pos: "n.", pronunciation: "[ˈmæml]", eng: "a warm-blooded vertebrate animal.", eng_vie: "(động vật có vú)", ex: "Whales and dolphins are mammals.", ex_vie: "(Cá voi và cá heo là động vật có vú.)" },
    { word: "evolve", pos: "v.", pronunciation: "[ɪˈvɑːlv]", eng: "to develop gradually.", eng_vie: "(tiến hóa)", ex: "The company has evolved into a global brand.", ex_vie: "(Công ty đã phát triển thành một thương hiệu toàn cầu.)" },
    { word: "tropical", pos: "adj.", pronunciation: "[ˈtrɑːpɪkl]", eng: "typical of the tropics.", eng_vie: "(thuộc nhiệt đới)", ex: "We enjoy the tropical climate in Hawaii.", ex_vie: "(Chúng tôi tận hưởng khí hậu nhiệt đới ở Hawaii.)" },
    { word: "adapt", pos: "v.", pronunciation: "[əˈdæpt]", eng: "to make suitable for a new use or purpose.", eng_vie: "(làm thích nghi, điều chỉnh cho phù hợp)", ex: "It took time to adapt to the new school.", ex_vie: "(Mất một thời gian để thích nghi với ngôi trường mới.)" },
    { word: "crepuscular", pos: "adj.", pronunciation: "[krɪˈpʌskjələr]", eng: "appearing or active in twilight.", eng_vie: "(hoạt động vào lúc hoàng hôn)", ex: "Bats and owls are crepuscular animals.", ex_vie: "(Dơi và cú là những loài động vật hoạt động vào lúc hoàng hôn.)" },
    { word: "counterproductive", pos: "adj.", pronunciation: "[ˌkaʊntərprəˈdʌktɪv]", eng: "having the opposite of the desired effect.", eng_vie: "(phản tác dụng)", ex: "Yelling at the child was counterproductive.", ex_vie: "(La mắng đứa trẻ lại gây phản tác dụng.)" },
];

// --- Helper: Generate word entry HTML ---
function wordHtml(w) {
    return `<div style="display:flex;gap:16px;align-items:flex-start;"><div style="width:32px;height:32px;flex-shrink:0;background-color:#f8fafc;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 3px rgba(0,0,0,0.1);border:1px solid #e2e8f0;font-size:16px;">😎</div><div style="display:flex;flex-direction:column;gap:6px;"><div style="display:flex;align-items:baseline;gap:8px;"><span style="font-size:1.25rem;font-weight:800;color:#65a30d;">${w.word}</span><span style="font-size:0.875rem;color:#94a3b8;font-family:monospace;">${w.pronunciation}</span><span style="font-size:0.875rem;color:#94a3b8;font-style:italic;">${w.pos}</span></div><div style="color:#475569;font-size:0.95rem;line-height:1.5;">${w.eng} <span style="color:#0ea5e9;">${w.eng_vie}</span></div><div style="color:#64748b;font-size:0.95rem;font-style:italic;">→ ${w.ex} <span style="color:#0ea5e9;">${w.ex_vie}</span></div></div></div>`;
}

function generateDetailedMeanings(words) {
    return `<div style="display:flex;flex-direction:column;gap:24px;padding-top:24px;border-top:1px dashed #cbd5e1;"><h3 style="font-size:1.125rem;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:0.05em;margin:0;">Detailed Meanings</h3><div style="display:flex;flex-direction:column;gap:24px;">${words.map(w => wordHtml(w)).join('')}</div></div>`;
}

// --- Build Word List content HTML (matches Unit 1 exactly) ---
const word1Content = `<p style="display: none;">Word List 1</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="/unit2_ielts_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" />${generateDetailedMeanings(wordsList1)}</div>`;

const word2Content = `<p style="display: none;">Word List 2</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="/unit2_ielts_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" />${generateDetailedMeanings(wordsList2)}</div>`;

// --- Build Reading Passage content HTML ---
const readingContent = `<p style="display: none;">Comprehensive Reading</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="/unit2_ielts_story.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Siesta Time</h1><p style="margin-bottom: 1rem;">An hour's sleep in the middle of the day can <b>work wonders</b>.</p><p style="margin-bottom: 1rem;">Finally, <b>vindication</b> for <b>power</b> nappers. <b>Far from</b> being lazy <b>louts</b>, <b>siesta</b>-takers are actually doing their bit for the firm. According to Sara Mednick and her <b>colleagues</b> at Harvard, just 60 minutes of <b>shut-eye</b> in the middle of the day can make you <b>perform</b> like the <b>fresh daisy</b> in the morning. But it has to be <b>bona fide</b> sleep; a <b>mere</b> rest, they found, has no effect.</p><p style="margin-bottom: 1rem;">Dr. Mednick, whose results have just been <b>published</b> in Nature Neuroscience, wanted to know what effect power napping would have on people's <b>visual perception</b>. She asked 30 student <b>volunteers</b> to come into her laboratory. Four times on the same day, at 9 am, noon, 4 pm and 7 pm, they were required to stare at a computer screen for an hour. Their task was to <b>pick out</b> a <b>vertical</b> or <b>horizontal bar</b> from a <b>striped background</b>—an <b>established</b> test of visual <b>perceptiveness</b>. The more quickly they picked out the bar, the more <b>acute</b> their perception.</p><p style="margin-bottom: 1rem;">All the volunteers had slept well in the days before the test, and had been <b>warned off alcohol</b>. During the test day, <b>nicotine addicts</b> were allowed to <b>indulge</b> their habits, but everyone had to remain <b>uncaffeinated</b>. Despite this <b>cosseting</b>, the <b>performance</b> of the ten volunteers who went straight through the day without a <b>nap deteriorated</b> rapidly. Their best scores were first thing in the morning, and it was <b>downhill</b> from there on. By the last <b>session</b>, they were taking 52% longer, <b>on average</b>, to <b>identify</b> the <b>orientation</b> of the bar than they had in the first.</p><p style="margin-bottom: 1rem;">However, another ten of the volunteers were given the <b>opportunity</b> to nap at 2 pm for 30 minutes, while the remaining ten were allowed a 60-minute <b>snooze</b>. The short nappers did not get any worse in their afternoon test sessions. The long nappers actually got better—they performed just as well as they had first thing.</p><p style="margin-bottom: 1rem;">To test whether a rest, rather than a nap, would <b>do the trick</b>, nine more volunteers were asked in. But <b>to no avail</b>: their abilities <b>declined</b> with each session. Nor did <b>motivation</b> seem to be a factor. Yet another set of volunteers, after a poor showing in the second session, was told they had not done very well, but that they could earn a further $25 if they could do as well in the afternoon as they had that morning. The poor students' eyes lit up, according to Dr Mednick, but not one, alas, was able to stop the decay.</p><p style="margin-bottom: 1rem;">The <b>upshot</b> is another piece of <b>evidence</b> that humans, like many <b>mammals</b> which have <b>evolved</b> in <b>tropical</b> climes, are <b>adapted</b> not to go out in the mid-day sun. They are, rather, <b>crepuscular</b>—that is, they are most active in the morning and the evening. The protestant work ethic that drives those now living in colder climates to work throughout the day may actually be <b>counterproductive</b>. At least, that is what you should tell your boss when asking for a couch to be installed in the office.</p></div></div>`;

// --- Build the JSON ---
const unit2 = {
  "title": "Unit 2: Siesta Time",
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
            {
              "id": 1,
              "content": "An hour's sleep in the middle of the day can ________ for your health.",
              "options": ["work wonders", "do the trick", "far from", "shut-eye"],
              "correctAnswer": "A",
              "explanation": "Work wonders means to have a very beneficial effect."
            },
            {
              "id": 2,
              "content": "The surgeon ________ the operation successfully.",
              "options": ["published", "performed", "adapted", "evolved"],
              "correctAnswer": "B",
              "explanation": "Perform means to carry out, accomplish, or fulfill."
            },
            {
              "id": 3,
              "content": "It costs a ________ twenty dollars.",
              "options": ["bona fide", "mere", "acute", "visual"],
              "correctAnswer": "B",
              "explanation": "Mere is used to emphasize how small or insignificant something is."
            },
            {
              "id": 4,
              "content": "The situation is ________ simple.",
              "options": ["far from", "bona fide", "fresh daisy", "mere"],
              "correctAnswer": "A",
              "explanation": "Far from means not at all."
            },
            {
              "id": 5,
              "content": "I need to get some ________ before the trip.",
              "options": ["siesta", "shut-eye", "vindication", "perception"],
              "correctAnswer": "B",
              "explanation": "Shut-eye means sleep."
            }
          ]
        },
        {
          "title": "Exercise 2: Choose the word that best matches the definition.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": 6,
              "content": "Proof that someone or something is right or justified",
              "options": ["Perception", "Vindication", "Power", "Colleague"],
              "correctAnswer": "B",
              "explanation": "Vindication is proof that someone or something is right or justified."
            },
            {
              "id": 7,
              "content": "A person with whom one works",
              "options": ["Napper", "Lout", "Colleague", "Siesta-taker"],
              "correctAnswer": "C",
              "explanation": "A colleague is a person with whom one works."
            },
            {
              "id": 8,
              "content": "Genuine; real",
              "options": ["Mere", "Visual", "Bona fide", "Fresh daisy"],
              "correctAnswer": "C",
              "explanation": "Bona fide means genuine or real."
            }
          ]
        },
        {
          "title": "Exercise 3: Mark each statement T for true or F for false.",
          "content": "<p class=\"font-bold text-[16px] text-slate-800 mb-4\">True / False</p>",
          "questionType": "TFNG",
          "questions": [
            {
              "id": 9,
              "content": "A 'siesta' is a morning exercise routine.",
              "options": ["True", "False"],
              "correctAnswer": "False",
              "explanation": "False. A siesta is an afternoon rest or nap."
            },
            {
              "id": 10,
              "content": "If something 'works wonders', it has a very beneficial effect.",
              "options": ["True", "False"],
              "correctAnswer": "True",
              "explanation": "True. Work wonders means to have a very beneficial effect."
            },
            {
              "id": 11,
              "content": "The word 'publish' means to prepare and issue for public sale.",
              "options": ["True", "False"],
              "correctAnswer": "True",
              "explanation": "True. Publish means to prepare and issue for public sale."
            }
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
            {
              "id": 12,
              "content": "Dogs have an ________ sense of hearing.",
              "options": ["established", "acute", "horizontal", "striped"],
              "correctAnswer": "B",
              "explanation": "Acute means having or showing a perceptive understanding or insight."
            },
            {
              "id": 13,
              "content": "His health began to ________ rapidly.",
              "options": ["adapt", "evolve", "deteriorate", "decline"],
              "correctAnswer": "C",
              "explanation": "Deteriorate means to become progressively worse."
            },
            {
              "id": 14,
              "content": "This is a great ________ for advancement.",
              "options": ["session", "motivation", "opportunity", "orientation"],
              "correctAnswer": "C",
              "explanation": "Opportunity means a set of circumstances that makes it possible to do something."
            },
            {
              "id": 15,
              "content": "________, she works eight hours a day.",
              "options": ["To no avail", "On average", "Far from", "Downhill"],
              "correctAnswer": "B",
              "explanation": "On average means usually, normally."
            }
          ]
        },
        {
          "title": "Exercise 2: Write C if the italicized word is used correctly. Write I if the word is used incorrectly.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": 16,
              "content": "The <i>volunteers</i> were paid for their mandatory service at the hospital.",
              "options": ["C", "I"],
              "correctAnswer": "B",
              "explanation": "Incorrect. A volunteer is a person who freely offers to take part, not someone who is paid for mandatory service."
            },
            {
              "id": 17,
              "content": "It is an <i>established</i> scientific fact that the Earth orbits the Sun.",
              "options": ["C", "I"],
              "correctAnswer": "A",
              "explanation": "Correct. Established means having existed or been accepted for a long time."
            },
            {
              "id": 18,
              "content": "The <i>crepuscular</i> animals are most active at noon.",
              "options": ["C", "I"],
              "correctAnswer": "B",
              "explanation": "Incorrect. Crepuscular means appearing or active in twilight, not at noon."
            }
          ]
        },
        {
          "title": "Exercise 3: Choose the word that best matches the definition.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": 19,
              "content": "The final or eventual outcome",
              "options": ["Evidence", "Upshot", "Motivation", "Session"],
              "correctAnswer": "B",
              "explanation": "Upshot means the final or eventual outcome."
            },
            {
              "id": 20,
              "content": "To develop gradually",
              "options": ["Adapt", "Evolve", "Decline", "Identify"],
              "correctAnswer": "B",
              "explanation": "Evolve means to develop gradually."
            },
            {
              "id": 21,
              "content": "Having the opposite of the desired effect",
              "options": ["Counterproductive", "Established", "Tropical", "Acute"],
              "correctAnswer": "A",
              "explanation": "Counterproductive means having the opposite of the desired effect."
            }
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
              { answer: "vindication" },
              { answer: "siesta" },
              { answer: "perform" },
              { answer: "bona fide" },
              { answer: "volunteers" },
              { answer: "pick out" },
              { answer: "acute" },
              { answer: "deteriorated" },
              { answer: "opportunity" },
              { answer: "upshot" },
              { answer: "counterproductive" }
            ];
            const allOptions = blanks.map(b => b.answer);
            const contentText = `1. Finally, [ 1 ] for power nappers.<br/><br/>2. [ 2 ]-takers are actually doing their bit for the firm.<br/><br/>3. Just 60 minutes of shut-eye can make you [ 3 ] like a fresh daisy.<br/><br/>4. It has to be [ 4 ] sleep; a mere rest has no effect.<br/><br/>5. She asked 30 student [ 5 ] to come into her laboratory.<br/><br/>6. Their task was to [ 6 ] a vertical or horizontal bar.<br/><br/>7. The more quickly they picked out the bar, the more [ 7 ] their perception.<br/><br/>8. The performance of ten volunteers [ 8 ] rapidly.<br/><br/>9. Another ten were given the [ 9 ] to nap at 2 pm.<br/><br/>10. The [ 10 ] is another piece of evidence.<br/><br/>11. The protestant work ethic may actually be [ 11 ].`;
            
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
            {
              "id": 33,
              "content": "What is the main conclusion of Dr. Mednick's study?",
              "options": [
                "Napping is counterproductive for humans.",
                "A mid-day nap can maintain or improve visual perception.",
                "Resting without sleeping is just as effective as napping.",
                "People should sleep for at least 3 hours during the day."
              ],
              "correctAnswer": "B",
              "explanation": "The study tested visual perceptiveness, and showed that napping maintained or improved abilities while those who didn't nap deteriorated."
            },
            {
              "id": 34,
              "content": "According to the passage, what happened to volunteers who did not nap?",
              "options": [
                "They performed better throughout the day.",
                "Their performance stayed the same.",
                "Their performance deteriorated rapidly.",
                "They fell asleep during the test."
              ],
              "correctAnswer": "C",
              "explanation": "The text states: 'the performance of the ten volunteers who went straight through the day without a nap deteriorated rapidly.'"
            },
            {
              "id": 35,
              "content": "Why does the author mention 'crepuscular' animals?",
              "options": [
                "To show that humans should only sleep at night.",
                "To suggest humans are adapted to be most active in morning and evening.",
                "To prove that all mammals need long naps.",
                "To explain why cold climates are better for working."
              ],
              "correctAnswer": "B",
              "explanation": "The text states: 'They are, rather, crepuscular—that is, they are most active in the morning and the evening.'"
            },
            {
              "id": 36,
              "content": "What does the passage say about the effect of financial motivation on performance?",
              "options": [
                "It significantly improved afternoon performance.",
                "It had no effect—no one could stop the decay.",
                "It helped some volunteers but not others.",
                "It was not tested in the study."
              ],
              "correctAnswer": "B",
              "explanation": "The text mentions they were offered $25, but 'not one, alas, was able to stop the decay.'"
            }
          ]
        }
      ]
    }
  ],
  "basicInfo": {
    "skill": "MCQ (Standard)",
    "title": "Unit 2: Siesta Time",
    "category": "exercise",
    "courseId": "239a64f0-c106-40e5-a6e2-4e685a0d70fb",
    "timeLimit": 40
  }
};

fs.writeFileSync('public/unit2_ielts.json', JSON.stringify(unit2, null, 2));
console.log('Unit 2 JSON generated successfully! (Unit 1 format)');
