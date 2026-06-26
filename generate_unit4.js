const fs = require('fs');

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
    { word: "burger", pos: "n.", pronunciation: "[ˈbɜːrɡər]", eng: "a hamburger.", eng_vie: "(bánh mì kẹp thịt)", ex: "I'd like a cheeseburger and fries.", ex_vie: "(Tôi muốn một cái bánh mì kẹp phô mai và khoai tây chiên.)" },
    { word: "fry", pos: "n.", pronunciation: "[fraɪ]", eng: "a French fry.", eng_vie: "(thứ rán)", ex: "He ate a large order of fries.", ex_vie: "(Anh ấy đã ăn một phần khoai tây chiên lớn.)" },
    { word: "milkshake", pos: "n.", pronunciation: "[ˈmɪlkʃeɪk]", eng: "a cold drink made of milk, a sweet flavoring, and typically ice cream.", eng_vie: "(sữa lắc)", ex: "She ordered a strawberry milkshake.", ex_vie: "(Cô ấy gọi một ly sữa lắc dâu tây.)" },
    { word: "absurd", pos: "adj.", pronunciation: "[əbˈsɜːrd]", eng: "wildly unreasonable, illogical, or inappropriate.", eng_vie: "(vô lý, lố bịch)", ex: "It was an absurd lawsuit.", ex_vie: "(Đó là một vụ kiện lố bịch.)" },
    { word: "inevitable", pos: "adj.", pronunciation: "[ɪnˈevɪtəbl]", eng: "certain to happen; unavoidable.", eng_vie: "(tất yếu, không thể tránh được)", ex: "The accident was inevitable.", ex_vie: "(Vụ tai nạn là không thể tránh khỏi.)" },
    { word: "settlement", pos: "n.", pronunciation: "[ˈsetlmənt]", eng: "an official agreement intended to resolve a dispute or conflict.", eng_vie: "(sự dàn xếp, sự hòa giải)", ex: "They reached a settlement out of court.", ex_vie: "(Họ đã đạt được một thỏa thuận hòa giải ngoài tòa án.)" },
    { word: "burn a hole in one's pocket", pos: "idiom", pronunciation: "[bɜːrn ə hoʊl ɪn wʌnz ˈpɑːkɪt]", eng: "money that someone wants to spend quickly.", eng_vie: "(đốt cháy túi ai đó)", ex: "The money was burning a hole in his pocket.", ex_vie: "(Số tiền đó như đang đốt cháy túi anh ta.)" },
    { word: "trial lawyer", pos: "n.", pronunciation: "[ˈtraɪəl ˈlɔɪər]", eng: "a lawyer who represents clients in a trial.", eng_vie: "(luật sư)", ex: "The trial lawyer won the case.", ex_vie: "(Luật sư bào chữa đã thắng kiện.)" },
    { word: "catch", pos: "n.", pronunciation: "[kætʃ]", eng: "a hidden problem or disadvantage in an apparently ideal situation.", eng_vie: "(điều bất lợi)", ex: "There is a catch: fast food is not addictive.", ex_vie: "(Có một điều bất lợi: thức ăn nhanh không gây nghiện.)" },
    { word: "as a matter of fact", pos: "phrase", pronunciation: "[əz ə ˈmætər əv fækt]", eng: "in reality; actually.", eng_vie: "(vì vậy, thực tế là)", ex: "As a matter of fact, I do know him.", ex_vie: "(Thực tế là tôi có biết anh ta.)" },
    { word: "contain", pos: "v.", pronunciation: "[kənˈteɪn]", eng: "to have or hold within.", eng_vie: "(chứa, đựng)", ex: "The box contains some old books.", ex_vie: "(Chiếc hộp chứa một vài cuốn sách cũ.)" },
    { word: "substance", pos: "n.", pronunciation: "[ˈsʌbstəns]", eng: "a particular kind of matter with uniform properties.", eng_vie: "(chất)", ex: "It contains no addictive substance.", ex_vie: "(Nó không chứa bất kỳ chất gây nghiện nào.)" },
    { word: "induce", pos: "v.", pronunciation: "[ɪnˈduːs]", eng: "to succeed in persuading or influencing someone to do something.", eng_vie: "(gây ra, đem lại)", ex: "Nothing could induce me to change my mind.", ex_vie: "(Không gì có thể thuyết phục tôi thay đổi ý định.)" },
    { word: "The Economist", pos: "n.", pronunciation: "[ði ɪˈkɑːnəmɪst]", eng: "a well-known newspaper.", eng_vie: "(tờ báo Economist)", ex: "The Economist suggests this should change.", ex_vie: "(Tờ báo Economist gợi ý rằng điều này nên thay đổi.)" },
    { word: "plight", pos: "n.", pronunciation: "[plaɪt]", eng: "a dangerous, difficult, or otherwise unfortunate situation.", eng_vie: "(hoàn cảnh, cảnh ngộ)", ex: "Consider the plight of the poor plaintiffs.", ex_vie: "(Hãy xem xét hoàn cảnh của những nguyên đơn nghèo khổ.)" },
    { word: "plaintiff", pos: "n.", pronunciation: "[ˈpleɪntɪf]", eng: "a person who brings a case against another in a court of law.", eng_vie: "(nguyên đơn, người đứng đơn kiện)", ex: "The plaintiff won the lawsuit.", ex_vie: "(Nguyên đơn đã thắng kiện.)" },
    { word: "compel", pos: "v.", pronunciation: "[kəmˈpel]", eng: "to force or oblige someone to do something.", eng_vie: "(buộc phải, bắt buộc)", ex: "They were physiologically compelled to consume fast food.", ex_vie: "(Họ bị ép buộc về mặt sinh lý phải tiêu thụ đồ ăn nhanh.)" },
    { word: "against", pos: "prep.", pronunciation: "[əˈɡenst]", eng: "in opposition to.", eng_vie: "(chống lại, ngược lại)", ex: "He swam against the current.", ex_vie: "(Anh ấy bơi ngược dòng.)" },
    { word: "weight", pos: "n.", pronunciation: "[weɪt]", eng: "importance, influence, or the physical mass of an object.", eng_vie: "(trọng lượng, sức nặng)", ex: "Against the weight of scientific evidence.", ex_vie: "(Ngược lại với sức nặng của các bằng chứng khoa học.)" },
    { word: "dictate", pos: "n.", pronunciation: "[ˈdɪkteɪt]", eng: "a principle that prescribes behavior.", eng_vie: "(tiếng gọi, mệnh lệnh)", ex: "The dictates of common sense.", ex_vie: "(Tiếng gọi của lẽ thường.)" },
    { word: "common sense", pos: "n.", pronunciation: "[ˌkɑːmən ˈsens]", eng: "good sense and sound judgment in practical matters.", eng_vie: "(lẽ thường)", ex: "Use your common sense.", ex_vie: "(Hãy sử dụng lẽ thường của bạn.)" },
    { word: "indulge in", pos: "phrasal v.", pronunciation: "[ɪnˈdʌldʒ ɪn]", eng: "to allow oneself to enjoy the pleasure of.", eng_vie: "(ham mê, say mê)", ex: "Millions more indulge in the stuff.", ex_vie: "(Hàng triệu người khác say mê thứ đó.)" },
    { word: "stuff", pos: "n.", pronunciation: "[stʌf]", eng: "matter, material, articles, or activities of a specified or indeterminate kind.", eng_vie: "(thứ, món)", ex: "He left his stuff on the table.", ex_vie: "(Anh ấy để lại đồ đạc của mình trên bàn.)" },
    { word: "suborn", pos: "v.", pronunciation: "[səˈbɔːrn]", eng: "to bribe or otherwise induce someone to commit an unlawful act.", eng_vie: "(hối lộ, mua chuộc)", ex: "They knew they had been suborned into doing so.", ex_vie: "(Họ biết rằng mình đã bị mua chuộc để làm như vậy.)" }
];

const wordsList2 = [
    { word: "minute", pos: "adj.", pronunciation: "[maɪˈnuːt]", eng: "extremely small.", eng_vie: "(rất nhỏ)", ex: "Minute amounts of cocaine.", ex_vie: "(Một lượng rất nhỏ cocaine.)" },
    { word: "cocaine", pos: "n.", pronunciation: "[koʊˈkeɪn]", eng: "a strong stimulant mostly used as a recreational drug.", eng_vie: "(côcain)", ex: "The introduction of cocaine into their wares.", ex_vie: "(Sự ra đời của cocaine vào trong các sản phẩm của họ.)" },
    { word: "lot", pos: "n.", pronunciation: "[lɑːt]", eng: "a particular group, collection, or set of people or things.", eng_vie: "(tất cả, số phận)", ex: "Improve the lot of such folk.", ex_vie: "(Cải thiện số phận của những người như vậy.)" },
    { word: "benefit", pos: "n.", pronunciation: "[ˈbenɪfɪt]", eng: "an advantage or profit gained from something.", eng_vie: "(ích lợi)", ex: "The benefits would not stop there.", ex_vie: "(Lợi ích sẽ không dừng lại ở đó.)" },
    { word: "keen", pos: "adj.", pronunciation: "[kiːn]", eng: "having or showing eagerness or enthusiasm.", eng_vie: "(ham mê, say mê)", ex: "Nobody should be keener for fast food to be made addictive.", ex_vie: "(Không ai nên ham mê việc làm cho thức ăn nhanh trở nên gây nghiện hơn thế.)" },
    { word: "genuine", pos: "adj.", pronunciation: "[ˈdʒenjuɪn]", eng: "truly what something is said to be; authentic.", eng_vie: "(thật, chính xác, thành thật)", ex: "Once fast food became a genuine compulsion.", ex_vie: "(Một khi thức ăn nhanh trở thành một sự ép buộc thực sự.)" },
    { word: "compulsion", pos: "n.", pronunciation: "[kəmˈpʌlʃn]", eng: "an irresistible urge to behave in a certain way.", eng_vie: "(sự ép buộc, sự cưỡng bức)", ex: "Eating disorder is a compulsion.", ex_vie: "(Rối loạn ăn uống là một sự cưỡng bức.)" },
    { word: "objection", pos: "n.", pronunciation: "[əbˈdʒekʃn]", eng: "an expression or feeling of disapproval or opposition.", eng_vie: "(sự phản đối, sự chống đối)", ex: "There could be no economic or moral objection.", ex_vie: "(Không thể có sự phản đối nào về mặt kinh tế hay đạo đức.)" },
    { word: "regulate", pos: "v.", pronunciation: "[ˈreɡjuleɪt]", eng: "to control or maintain the rate or speed of (a machine or process).", eng_vie: "(quy định)", ex: "Alcohol and tobacco are regulated.", ex_vie: "(Rượu và thuốc lá đều bị quy định chặt chẽ.)" },
    { word: "consumption", pos: "n.", pronunciation: "[kənˈsʌmpʃn]", eng: "the using up of a resource.", eng_vie: "(sự tiêu thụ)", ex: "Regulating its consumption.", ex_vie: "(Quy định việc tiêu thụ nó.)" },
    { word: "tax", pos: "v.", pronunciation: "[tæks]", eng: "to impose a tax on.", eng_vie: "(đánh thuế)", ex: "And to taxing it.", ex_vie: "(Và đánh thuế nó.)" },
    { word: "revenue", pos: "n.", pronunciation: "[ˈrevənuː]", eng: "income, especially when of a company or organization.", eng_vie: "(thu nhập)", ex: "The revenue from this tax could be used.", ex_vie: "(Doanh thu từ khoản thuế này có thể được sử dụng.)" },
    { word: "sin tax", pos: "n.", pronunciation: "[sɪn tæks]", eng: "a tax on items considered undesirable or harmful, such as alcohol or tobacco.", eng_vie: "(thuế đánh vào những sản phẩm có thể gây hại như rượu bia, thuốc lá)", ex: "A sin tax on fast food.", ex_vie: "(Thuế tội lỗi đối với thức ăn nhanh.)" },
    { word: "pretend", pos: "adj.", pronunciation: "[prɪˈtend]", eng: "not really what it is represented to be; mock.", eng_vie: "(giả, vờ vịt, ngụy tạo)", ex: "Used in a pretend effort.", ex_vie: "(Được sử dụng trong một nỗ lực giả tạo.)" },
    { word: "wean off", pos: "phrasal v.", pronunciation: "[wiːn ɔːf]", eng: "to make someone gradually stop doing or using something.", eng_vie: "(bỏ, cai)", ex: "To wean people off bad food.", ex_vie: "(Để cai nghiện thức ăn không lành mạnh cho mọi người.)" },
    { word: "balance", pos: "v.", pronunciation: "[ˈbæləns]", eng: "to keep or put (something) in a steady position.", eng_vie: "(cân đối)", ex: "On balancing budgets.", ex_vie: "(Trong việc cân đối ngân sách.)" },
    { word: "budget", pos: "n.", pronunciation: "[ˈbʌdʒɪt]", eng: "an estimate of income and expenditure for a set period of time.", eng_vie: "(ngân sách)", ex: "The school has a strict budget.", ex_vie: "(Trường có một ngân sách nghiêm ngặt.)" },
    { word: "supposedly", pos: "adv.", pronunciation: "[səˈpoʊzɪdli]", eng: "according to what is generally assumed or believed.", eng_vie: "(giả sử, cho là)", ex: "Supposedly, people felt less urge.", ex_vie: "(Người ta cho rằng mọi người cảm thấy ít khao khát hơn.)" },
    { word: "fiscally", pos: "adv.", pronunciation: "[ˈfɪskəli]", eng: "in a way that relates to government revenue, especially taxes.", eng_vie: "(xét về tài chính)", ex: "People in fiscally prudent places.", ex_vie: "(Những người ở những nơi thận trọng về tài chính.)" },
    { word: "prudent", pos: "adj.", pronunciation: "[ˈpruːdnt]", eng: "acting with or showing care and thought for the future.", eng_vie: "(thận trọng, khôn ngoan)", ex: "It is prudent to save money.", ex_vie: "(Việc tiết kiệm tiền là rất khôn ngoan.)" },
    { word: "literate", pos: "adj.", pronunciation: "[ˈlɪtərət]", eng: "able to read and write.", eng_vie: "(có học)", ex: "A highly literate population.", ex_vie: "(Một dân số có học thức cao.)" },
    { word: "urge", pos: "n.", pronunciation: "[ɜːrdʒ]", eng: "a strong desire or impulse.", eng_vie: "(sự thúc giục, sự thôi thúc)", ex: "Felt less urge to light up.", ex_vie: "(Cảm thấy ít sự thôi thúc phải châm thuốc hơn.)" },
    { word: "light up", pos: "phrasal v.", pronunciation: "[laɪt ʌp]", eng: "to ignite a cigarette, cigar, or pipe.", eng_vie: "(châm thuốc lá hút)", ex: "He lit up a cigarette.", ex_vie: "(Anh ấy đã châm một điếu thuốc.)" },
    { word: "subsequently", pos: "adv.", pronunciation: "[ˈsʌbsɪkwəntli]", eng: "after a particular thing has happened; afterward.", eng_vie: "(rồi thì, rồi sau đó)", ex: "Subsequently bureaucrats could prepare carefully.", ex_vie: "(Sau đó các quan liêu có thể chuẩn bị cẩn thận.)" },
    { word: "bureaucrat", pos: "n.", pronunciation: "[ˈbjʊrəkræt]", eng: "an official in a government department.", eng_vie: "(viên chức, người quan liêu)", ex: "The bureaucrats are slow to act.", ex_vie: "(Các viên chức chính phủ hành động rất chậm chạp.)" },
    { word: "pension", pos: "n.", pronunciation: "[ˈpenʃn]", eng: "a regular payment made during a person's retirement.", eng_vie: "(tiền lương hưu)", ex: "Their pensions happily financed by such taxes.", ex_vie: "(Lương hưu của họ được tài trợ vui vẻ bằng những khoản thuế đó.)" },
    { word: "finance", pos: "v.", pronunciation: "[ˈfaɪnæns]", eng: "to provide funding for (a person or enterprise).", eng_vie: "(tài trợ, cung cấp tiền)", ex: "The project is heavily financed by the government.", ex_vie: "(Dự án này được chính phủ tài trợ rất nhiều.)" },
    { word: "grade", pos: "v.", pronunciation: "[ɡreɪd]", eng: "to arrange in or allocate to grades; class or sort.", eng_vie: "(xếp loại, phân loại)", ex: "Carefully graded rationing schemes.", ex_vie: "(Kế hoạch chia khẩu phần được phân loại cẩn thận.)" },
    { word: "ration", pos: "v.", pronunciation: "[ˈræʃn]", eng: "to allow each person to have only a fixed amount of.", eng_vie: "(hạn chế (số lượng), chia khẩu phần)", ex: "Food was rationed during the war.", ex_vie: "(Thực phẩm đã bị hạn chế khẩu phần trong suốt thời kỳ chiến tranh.)" },
    { word: "scheme", pos: "n.", pronunciation: "[skiːm]", eng: "a large-scale systematic plan or arrangement.", eng_vie: "(sự sắp xếp theo hệ thống, kế hoạch)", ex: "A rationing scheme.", ex_vie: "(Một kế hoạch phân phối khẩu phần.)" },
    { word: "defendant", pos: "n.", pronunciation: "[dɪˈfendənt]", eng: "an individual, company, or institution sued or accused in a court of law.", eng_vie: "(bị cáo)", ex: "Making fast food addictive could help the defendants as well.", ex_vie: "(Làm cho thức ăn nhanh gây nghiện cũng có thể giúp ích cho các bị cáo.)" },
    { word: "follow", pos: "v.", pronunciation: "[ˈfɑːloʊ]", eng: "to go or come after.", eng_vie: "(theo, theo đuổi)", ex: "They might follow the tobacco firms.", ex_vie: "(Họ có thể đi theo các hãng thuốc lá.)" },
    { word: "living proof", pos: "n.", pronunciation: "[ˈlɪvɪŋ pruːf]", eng: "a person who provides an example of something.", eng_vie: "(bằng chứng sống)", ex: "Tobacco firms are living proof of this.", ex_vie: "(Các hãng thuốc lá là một bằng chứng sống cho điều này.)" },
    { word: "murderous", pos: "adj.", pronunciation: "[ˈmɜːrdərəs]", eng: "capable of or intending to murder; dangerously violent.", eng_vie: "(giết người, tàn sát)", ex: "Even after murderous litigation.", ex_vie: "(Ngay cả sau vụ kiện tàn sát.)" },
    { word: "litigation", pos: "n.", pronunciation: "[ˌlɪtɪˈɡeɪʃn]", eng: "the process of taking legal action.", eng_vie: "(sự kiện tụng, sự tranh chấp)", ex: "The company faces costly litigation.", ex_vie: "(Công ty phải đối mặt với vụ kiện tốn kém.)" },
    { word: "universally", pos: "adv.", pronunciation: "[ˌjuːnɪˈvɜːrsəli]", eng: "by everyone; in every case.", eng_vie: "(khắp nơi, phổ biến)", ex: "You can be universally reviled and still successful.", ex_vie: "(Bạn có thể bị cả thế giới chửi rủa mà vẫn thành công.)" },
    { word: "revile", pos: "v.", pronunciation: "[rɪˈvaɪl]", eng: "to criticize in an abusive or angrily insulting manner.", eng_vie: "(chửi mắng, xỉ vả)", ex: "The politician was reviled by the press.", ex_vie: "(Chính trị gia đó đã bị báo chí xỉ vả.)" },
    { word: "nigh", pos: "adj.", pronunciation: "[naɪ]", eng: "near.", eng_vie: "(sớm (xảy ra))", ex: "Some thought the end of the industry was nigh.", ex_vie: "(Một số người nghĩ rằng ngày tàn của ngành công nghiệp này sắp đến.)" },
    { word: "far from", pos: "phrase", pronunciation: "[fɑːr frəm]", eng: "not at all.", eng_vie: "(không hề, hầu như là trái lại)", ex: "Far from it.", ex_vie: "(Hoàn toàn không phải vậy.)" },
    { word: "obey", pos: "v.", pronunciation: "[oʊˈbeɪ]", eng: "to comply with the command, direction, or request of.", eng_vie: "(tuân theo)", ex: "They may have to obey fiddly rules.", ex_vie: "(Họ có thể phải tuân thủ các quy tắc vớ vẩn.)" },
    { word: "fiddly", pos: "adj.", pronunciation: "[ˈfɪdli]", eng: "complicated or detailed and awkward to do or use.", eng_vie: "(vớ vẩn, vô nghĩa)", ex: "Fiddly rules about not marketing to small children.", ex_vie: "(Những quy định vớ vẩn về việc không tiếp thị cho trẻ nhỏ.)" },
    { word: "market", pos: "v.", pronunciation: "[ˈmɑːrkɪt]", eng: "to advertise or promote.", eng_vie: "(bán ở thị trường, tiếp thị)", ex: "They are not allowed to market to children.", ex_vie: "(Họ không được phép tiếp thị cho trẻ em.)" },
    { word: "firm", pos: "n.", pronunciation: "[fɜːrm]", eng: "a business or company.", eng_vie: "(hãng sản xuất)", ex: "Cigarette firms can still earn money.", ex_vie: "(Các hãng thuốc lá vẫn có thể kiếm được tiền.)" },
    { word: "stockmarket", pos: "n.", pronunciation: "[ˈstɑːkmɑːrkɪt]", eng: "a stock exchange.", eng_vie: "(thị trường chứng khoán)", ex: "Theirs was the best-performing industry in the stockmarket.", ex_vie: "(Của họ là ngành hoạt động tốt nhất trên thị trường chứng khoán.)" },
    { word: "follow suit", pos: "idiom", pronunciation: "[ˈfɑːloʊ suːt]", eng: "to conform to another's actions.", eng_vie: "(làm theo như vậy)", ex: "Fast-food companies could follow suit.", ex_vie: "(Các công ty thức ăn nhanh có thể sẽ làm theo như vậy.)" },
    { word: "reap", pos: "v.", pronunciation: "[riːp]", eng: "to receive (a reward or benefit) as a consequence of one's own or other people's actions.", eng_vie: "(gặt hái, thu hoạch, hưởng)", ex: "They reap both public-relations and financial victories.", ex_vie: "(Họ gặt hái cả chiến thắng về mặt quan hệ công chúng lẫn tài chính.)" },
    { word: "financial", pos: "adj.", pronunciation: "[faɪˈnænʃl]", eng: "relating to finance or finances.", eng_vie: "(thuộc tài chính)", ex: "Financial victories.", ex_vie: "(Chiến thắng về tài chính.)" }
];

const generateHtml = (words) => {
    let html = `<div style="display:flex;flex-direction:column;gap:24px;padding-top:24px;border-top:1px dashed #cbd5e1;"><h3 style="font-size:1.125rem;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:0.05em;margin:0;">Detailed Meanings</h3><div style="display:flex;flex-direction:column;gap:24px;">`;
    words.forEach(w => {
        html += `<div style="display:flex;gap:16px;align-items:flex-start;"><div style="width:32px;height:32px;flex-shrink:0;background-color:#f8fafc;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 3px rgba(0,0,0,0.1);border:1px solid #e2e8f0;font-size:16px;">😎</div><div style="display:flex;flex-direction:column;gap:6px;"><div style="display:flex;align-items:baseline;gap:8px;"><span style="font-size:1.25rem;font-weight:800;color:#65a30d;">${w.word}</span><span style="font-size:0.875rem;color:#94a3b8;font-family:monospace;">${w.pronunciation}</span><span style="font-size:0.875rem;color:#94a3b8;font-style:italic;">${w.pos}</span></div><div style="color:#475569;font-size:0.95rem;line-height:1.5;">${w.eng} <span style="color:#0ea5e9;">${w.eng_vie}</span></div><div style="color:#64748b;font-size:0.95rem;font-style:italic;">→ ${w.ex} <span style="color:#0ea5e9;">${w.ex_vie}</span></div></div></div>`;
    });
    html += `</div></div>`;
    return html;
};

const word1Html = `<p style="display: none;">Word List</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="https://gxxalzhxpsqahgnyxwhb.supabase.co/storage/v1/object/public/images/unit4_wordlist1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div>${generateHtml(wordsList1)}</div>`;
const word2Html = `<p style="display: none;">Word List</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="https://gxxalzhxpsqahgnyxwhb.supabase.co/storage/v1/object/public/images/unit4_wordlist2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div>${generateHtml(wordsList2)}</div>`;

const readingPassageHTML = `<div style="display: flex; flex-direction: column; gap: 16px; margin-bottom: 24px;"><img src="https://gxxalzhxpsqahgnyxwhb.supabase.co/storage/v1/object/public/images/unit4_story.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="color: #334155; font-size: 1rem; line-height: 1.8; text-align: justify;"><p style="margin-bottom: 1rem;"><b>If only fast food</b> were truly <b>addictive</b>.</p><p style="margin-bottom: 1rem;">Last week, Caesar Barber of New York <b>filed</b> a <b>class-action lawsuit</b> against McDonald's, Kentucky Fried Chicken, Burger King and Wendy's, four of the world's biggest fast-food chains. His <b>claim</b> was that they were responsible for his <b>obesity</b> and poor health. According to his lawyer, fast food had created a “<b>craving</b>” in his <b>hapless client</b>, who was <b>blissfully unaware</b>, until his doctor told him, that <b>consuming huge piles of burgers</b>, <b>fries</b> and <b>milkshakes</b> was not actually good for his health.</p><p style="margin-bottom: 1rem;">Such an <b>absurd</b> lawsuit may have been <b>inevitable</b> as soon as the big tobacco <b>settlements began burning a hole in trial lawyers' pockets</b>. But there is a <b>catch</b>: fast food is not addictive. It does not, <b>as a matter of fact</b>, create a real physical craving, because it <b>contains no substance</b> that could <b>induce</b> one.</p><p style="margin-bottom: 1rem;"><b>The Economist</b> suggests that this should now change. Consider the <b>plight</b> of the poor <b>plaintiffs</b>. They must prove that they were physiologically <b>compelled</b> to consume fast food, <b>against</b> the <b>weight</b> of scientific evidence and the <b>dictates</b> of <b>common sense</b>. Then there are the millions more who <b>indulge in</b> the <b>stuff</b>, but who would feel much better about themselves if they knew they had been <b>suborned</b> into doing so. Through the simple introduction of <b>minute amounts of cocaine</b> or nicotine into their wares, fast-food companies could improve the <b>lot</b> of such folk in future.</p><p style="margin-bottom: 1rem;">The <b>benefits</b> would not stop there. Nobody should be <b>keener</b> for fast food to be made <b>addictive</b> than governments. Once fast food became a <b>genuine compulsion</b>, there could be no economic or moral <b>objection</b> to <b>regulating</b> its <b>consumption</b>, as alcohol and tobacco are regulated, and to <b>taxing</b> it. The <b>revenue</b> from this “<b>sin tax</b>” could be used in a <b>pretend</b> effort to <b>wean</b> people <b>off</b> bad food. Many states spent their millions from tobacco settlements on <b>balancing budgets</b>, improving roads or paying teachers more. <b>Supposedly</b>, people in <b>fiscally prudent</b>, <b>literate</b> and well-paved places felt less <b>urge</b> to <b>light up</b>. Taxes on fast-food sales could be used in similar ways. <b>Subsequently bureaucrats</b>, their <b>pensions</b> happily <b>financed</b> by such taxes, could prepare carefully <b>graded rationing schemes</b>.</p><p style="margin-bottom: 1rem;">Making fast food addictive could help the <b>defendants</b> as well. They might <b>follow</b> the tobacco <b>firms</b>, who are <b>living proof</b> that even after <b>murderous litigation</b> you can be both <b>universally reviled</b> and still successful. When the big tobacco lawsuits finished, some thought the end of the industry was <b>nigh</b>. <b>Far from</b> it: they may have to <b>obey fiddly</b> rules about not <b>marketing</b> to small children in North America, but cigarette firms can still earn money in the rest of the world. Last year, theirs was the best-performing industry in the <b>stockmarket</b>. Fast-food companies could <b>follow suit</b> and <b>reap</b> both public-relations and <b>financial</b> victories.</p></div>`;

let qId = 1;

const unit4 = {
  "id": "ielts_unit4",
  "title": "UNIT 4: OH, TEMPTATION",
  "parts": [
    {
      "title": "Word List 1",
      "content": word1Html,
      "sections": [
        {
          "content": "<p class=\"font-bold text-lg text-slate-800 mb-2 mt-4\">Task 1</p><p class=\"font-bold text-[16px] text-slate-800 mb-4\">Listen carefully and fill the missing words from the word list into the blanks to complete the sentence.</p><p>1. I tried to resist the [ 1 ] to laugh.</p><p>2. They [ 2 ] an application to have their case heard early.</p><p>3. A confrontation was [ 3 ] because they disliked each other so much.</p><p>4. The whole country is hoping for the [ 4 ] of this strike.</p><p>5. Heroin is an illegal [ 5 ].</p>",
          "questions": [
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "temptation",
              "explanation": "<b>Temptation</b> (n.): sự cám dỗ. Tôi đã cố gắng cưỡng lại sự cám dỗ muốn cười."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "filed",
              "explanation": "<b>File</b> (v.): đệ đơn. Họ đã nộp đơn yêu cầu xét xử sớm vụ án của mình."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "inevitable",
              "explanation": "<b>Inevitable</b> (adj.): không thể tránh khỏi. Một cuộc đối đầu là không thể tránh khỏi vì họ quá ghét nhau."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "settlement",
              "explanation": "<b>Settlement</b> (n.): sự hòa giải, dàn xếp. Cả nước đang hy vọng vào sự dàn xếp của cuộc đình công này."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "substance",
              "explanation": "<b>Substance</b> (n.): chất. Heroin là một chất bất hợp pháp."
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
          "content": "<p class=\"font-bold text-lg text-slate-800 mb-2 mt-4\">Task 2</p><p class=\"font-bold text-[16px] text-slate-800 mb-4\">Listen carefully and fill the missing words from the word list into the blanks to complete the sentence.</p><p>6. Nothing could [ 1 ] her to be disloyal to him.</p><p>7. We are all moved by the [ 2 ] of these poor homeless children.</p><p>8. Employees are [ 3 ] to join the company's pension plan after a year's service.</p><p>9. I occasionally [ 4 ] in a big fat cigar.</p><p>10. His writing is [ 5 ].</p>",
          "questions": [
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "induce",
              "explanation": "<b>Induce</b> (v.): xui khiến, thuyết phục. Không có gì có thể thuyết phục cô ấy không trung thành với anh ta."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "plight",
              "explanation": "<b>Plight</b> (n.): hoàn cảnh. Tất cả chúng tôi đều cảm động trước hoàn cảnh của những đứa trẻ vô gia cư đáng thương này."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "compelled",
              "explanation": "<b>Compel</b> (v.): buộc phải. Nhân viên bắt buộc phải tham gia chương trình lương hưu của công ty sau một năm làm việc."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "indulge",
              "explanation": "<b>Indulge</b> (v.): ham mê, tự thưởng cho mình. Thỉnh thoảng tôi lại hút một điếu xì gà thật to."
            },
            {
              "id": qId++,
              "questionType": "Điền từ",
              "content": "",
              "options": [],
              "answer": "minute",
              "explanation": "<b>Minute</b> (adj.): rất nhỏ, tỉ mỉ. Chữ viết của anh ấy rất nhỏ."
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
              "content": "Caesar Barber won his class-action lawsuit against fast-food chains.",
              "options": ["True", "False", "Not Given"],
              "answer": "Not Given",
              "explanation": "<b>Not Given</b>. The text says he filed a lawsuit, but does not mention the outcome."
            },
            {
              "id": qId++,
              "questionType": "Droplist",
              "content": "Fast food is scientifically proven to be physically addictive.",
              "options": ["True", "False", "Not Given"],
              "answer": "False",
              "explanation": "<b>False</b>. The text states: 'fast food is not addictive. It does not, as a matter of fact, create a real physical craving, because it contains no substance that could induce one.'"
            },
            {
              "id": qId++,
              "questionType": "Droplist",
              "content": "The author suggests in a satirical way that fast food companies should add cocaine to their food.",
              "options": ["True", "False", "Not Given"],
              "answer": "True",
              "explanation": "<b>True</b>. The text satirically says: 'Through the simple introduction of minute amounts of cocaine or nicotine into their wares, fast-food companies could improve the lot of such folk in future.'"
            }
          ]
        }
      ]
    }
  ]
};

// Ensure all IDs are sequential from 1
finalId = 1;
unit4.parts.forEach(p => {
    p.sections.forEach(s => {
        s.questions.forEach(q => {
            q.id = finalId++;
        });
    });
});

fs.writeFileSync('public/unit4_ielts.json', JSON.stringify(unit4, null, 2));
console.log('Unit 4 generated successfully.');
