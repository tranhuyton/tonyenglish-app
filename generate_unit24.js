const fs = require('fs');

const u = {
  unit: 24,
  title: 'Unit 24: Head Cases',
  words: [
    { word: 'traditional', pos: 'a.', defVi: 'thuộc truyền thống' },
    { word: 'migraine', pos: 'n.', defVi: 'chứng đau nửa đầu' },
    { word: 'significant', pos: 'a.', defVi: 'đầy ý nghĩa, đáng kể' },
    { word: 'consequence', pos: 'n.', defVi: 'hậu quả' },
    { word: 'sufferer', pos: 'n.', defVi: 'người bị bệnh' },
    { word: 'some', pos: 'ad.', defVi: 'khoảng' },
    { word: 'at a cost', pos: '', defVi: 'với chi phí' },
    { word: 'reckon', pos: 'v.', defVi: 'tính, đếm' },
    { word: 'pop', pos: 'v.', defVi: 'uống (thuốc)' },
    { word: 'pill', pos: 'n.', defVi: 'viên thuốc' },
    { word: 'alleviate', pos: 'v.', defVi: 'làm nhẹ bớt, làm giảm bớt' },
    { word: 'symptom', pos: 'n.', defVi: 'triệu chứng' },
    { word: 'specialised', pos: 'a.', defVi: 'chuyên dùng' },
    { word: 'designed to', pos: '', defVi: 'được thiết kế để' },
    { word: 'keep... at bay', pos: '', defVi: 'cách ly' },
    { word: 'in part', pos: '', defVi: 'một phần, phần nào' },
    { word: 'be due to', pos: '', defVi: 'vì, do bởi' },
    { word: 'fundamental', pos: 'a.', defVi: 'cơ bản, cơ sở' },
    { word: 'colleague', pos: 'n.', defVi: 'đồng nghiệp' },
    { word: 'neurology', pos: 'n.', defVi: 'khoa thần kinh, thần kinh học' },
    { word: 'among others', pos: '', defVi: 'trong số những thứ/điều/người khác' },
    { word: 'round', pos: 'ad.', defVi: 'quanh, xung quanh' },
    { word: 'therapy', pos: 'n.', defVi: 'trị liệu, liệu pháp' },
    { word: 'initial', pos: 'a.', defVi: 'ban đầu, đầu' },
    { word: 'artery', pos: 'n.', defVi: 'động mạch' },
    { word: 'lead to', pos: '', defVi: 'dẫn đến' },
    { word: 'constrict', pos: 'v.', defVi: 'thắt lại, bóp lại, co lại' },
    { word: 'in response to', pos: '', defVi: 'để phản ứng lại với' },
    { word: 'unspecified', pos: 'a.', defVi: 'không chỉ rõ, không nói rõ' },
    { word: 'external', pos: 'a.', defVi: 'bên ngoài' },
    { word: 'trigger', pos: 'n.', defVi: 'nguyên nhân khởi phát một hành động nào đó' },
    { word: 'afflict', pos: 'v.', defVi: 'làm đau' },
    { word: 'function', pos: 'v.', defVi: 'hoạt động' },
    { word: 'abnormally', pos: 'ad.', defVi: '(một cách) bất thường' },
    { word: 'malfunction', pos: 'n.', defVi: 'sự trục trặc, sự cố' },
    { word: 'supposedly', pos: 'ad.', defVi: 'cho là, giả sử là' },
    { word: 'so-called', pos: 'a.', defVi: 'cái gọi là' },
    { word: 'aura', pos: 'n.', defVi: 'tinh hoa phát tiết ra' },
    { word: 'classical', pos: 'a.', defVi: 'kinh điển, cổ điển' },
    { word: 'flashing', pos: 'a.', defVi: '(đèn) pin, (đèn) chớp sáng' },
    { word: 'visual', pos: 'a.', defVi: 'thuộc thị giác' },
    { word: 'pins and needles', pos: '', defVi: 'cảm giác rần rần như kiến bò' },
    { word: 'limb', pos: 'n.', defVi: 'chân, tay' },
    { word: 'torment', pos: 'v.', defVi: 'làm đau khổ, giày vò, day dứt' },
    { word: 'by contrast', pos: '', defVi: 'trái lại' },
    { word: 'be blamed on', pos: '', defVi: 'được đổ lỗi cho, được quy cho' },
    { word: 'dilate', pos: 'v.', defVi: 'giãn ra, mở rộng ra' },
    { word: 'reflex reaction', pos: '', defVi: 'phản xạ' },
    { word: 'constriction', pos: 'n.', defVi: 'sự co, sự thắt' },
    { word: 'pressure', pos: 'n.', defVi: 'áp lực, sức ép' },
    { word: 'curb', pos: 'v.', defVi: 'kiềm chế, hạn chế' },
    { word: 'aim at', pos: '', defVi: 'nhằm để' },
    { word: 'brain-imaging', pos: 'n.', defVi: 'ảnh hóa não bộ' },
    { word: 'neurological', pos: 'a.', defVi: 'thuộc thần kinh, thuộc hệ thần kinh' },
    { word: 'disorder', pos: 'n.', defVi: 'sự rối loạn' },
    { word: 'rather than', pos: '', defVi: 'chứ không phải là' },
    { word: 'circulatory', pos: 'a.', defVi: 'thuộc tuần hoàn máu' },
    { word: 'cortex', pos: 'n.', defVi: 'vỏ não' },
    { word: 'fire off', pos: '', defVi: 'phát ra, nổ ra, bị kích thích' },
    { word: 'wildly', pos: 'ad.', defVi: '(một cách) dữ dội, (một cách) điên cuồng' },
    { word: 'quiescent', pos: 'a.', defVi: 'im lìm, yên lặng' },
    { word: 'phenomena', pos: 'n.', defVi: '(số nhiều của phenomenon) hiện tượng' },
    { word: 'diameter', pos: 'n.', defVi: 'đường kính' },
    { word: 'observe', pos: 'v.', defVi: 'quan sát' },
    { word: 'dilatation', pos: 'n.', defVi: 'sự giãn, sự nở' },
    { word: 'feature', pos: 'n.', defVi: 'đặc điểm' },
    { word: 'associated with', pos: '', defVi: 'liên kết với' },
    { word: 'misinterpretation', pos: 'n.', defVi: 'sự hiểu sai, sự giải thích sai' },
    { word: 'signal', pos: 'n.', defVi: 'dấu hiệu' },
    { word: 'dilation', pos: 'n.', defVi: 'sự giãn, sự nở' },
    { word: 'rather', pos: 'ad.', defVi: 'đúng hơn, hơn là' },
    { word: 'process', pos: 'v.', defVi: 'xử lý' },
    { word: 'stimuli', pos: 'n.', defVi: '(số nhiều của stimulus) sự kích thích, tác nhân kích thích' },
    { word: 'amplify', pos: 'v.', defVi: 'phóng đại, khuếch đại' },
    { word: 'back up', pos: '', defVi: 'hỗ trợ' },
    { word: 'scan', pos: 'n.', defVi: 'sự xem xét, sự quét' },
    { word: 'brain stem', pos: '', defVi: 'thân não' },
    { word: 'filter', pos: 'n.', defVi: 'bộ lọc' },
    { word: 'edit out', pos: '', defVi: 'cắt xén, chọn lọc' },
    { word: 'distract', pos: 'v.', defVi: 'làm sao nhãng' },
    { word: 'go awry', pos: '', defVi: 'bị hỏng' },
    { word: 'overload', pos: 'n.', defVi: 'sự quá tải' },
    { word: 'hypothesis', pos: 'n.', defVi: 'giả thuyết' },
    { word: 'endorse', pos: 'v.', defVi: 'xác nhận, tán thành' },
    { word: 'benefit from', pos: '', defVi: 'hưởng lợi từ' },
    { word: 'imaginative', pos: 'a.', defVi: 'tưởng tượng' },
    { word: 'prescription', pos: 'n.', defVi: 'sự kê toa thuốc' },
    { word: 'anti-convulsant', pos: 'a.', defVi: 'chống co giật' },
    { word: 'epileptic', pos: 'a.', defVi: 'thuộc động kinh' },
    { word: 'seizure', pos: 'n.', defVi: 'cơn tai biến' },
    { word: 'around', pos: 'ad.', defVi: 'khoảng' },
    { word: 'valproate', pos: 'n.', defVi: 'valproate (tên một loại thuốc chống co giật)' },
    { word: 'act on', pos: '', defVi: 'tác động lên' },
    { word: 'rely on', pos: '', defVi: 'phụ thuộc vào' },
    { word: 'calcium', pos: 'n.', defVi: 'canxi' },
    { word: 'communication', pos: 'n.', defVi: 'sự giao tiếp' },
    { word: 'blunt', pos: 'a.', defVi: '(về phương pháp, phương thuốc) gây ra nhiều tác dụng phụ có hại' },
    { word: 'a range of', pos: '', defVi: 'một loạt' },
    { word: 'side-effect', pos: 'n.', defVi: 'tác dụng phụ' },
    { word: 'fatigue', pos: 'n.', defVi: 'sự mệt mỏi, sự mệt nhọc' },
    { word: 'hence', pos: 'ad.', defVi: 'do đó, vì thế' },
    { word: 'precise', pos: 'a.', defVi: 'chính xác' },
    { word: 'ideally', pos: 'ad.', defVi: '(một cách) lý tưởng' },
    { word: 'embark on', pos: '', defVi: 'bắt đầu' },
    { word: 'trial', pos: 'n.', defVi: 'sự thử nghiệm' },
    { word: 'block', pos: 'v.', defVi: 'ngăn chặn' },
    { word: 'instruction', pos: 'n.', defVi: 'chỉ thị' },
    { word: 'neurotransmitter', pos: 'n.', defVi: 'chất dẫn truyền thần kinh' },
    { word: 'adenosine', pos: 'n.', defVi: 'hợp chất adenosine' },
    { word: 'glutamate', pos: 'n.', defVi: 'glutamate' },
    { word: 'crucially', pos: 'ad.', defVi: 'quan trọng, chủ yếu' },
    { word: 'unpalatable', pos: 'a.', defVi: 'có mùi khó chịu, không thể chấp nhận được' },
    { word: 'in sight', pos: '', defVi: 'xuất hiện, trở thành sự thật' }
  ],
  story: `\n<h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Head Cases</h1>\n<p style="margin-bottom: 1rem;">The traditional explanation for migraines may have things backwards—with significant consequences for sufferers.</p>\n<p style="margin-bottom: 1rem;">Migraines are a big headache. One woman in five and one man in 15 suffers from them. In Britain alone, some 90,000 people are absent from work every day as a result of migraines, at a cost to the economy reckoned by some to be £750m ($1.1 billion) a year. Popping a pill or two can help to alleviate the symptoms, but safe, specialised drugs designed to keep migraines at bay do not exist.</p>\n<p style="margin-bottom: 1rem;">That may, in part, be due to a fundamental misunderstanding of how migraines happen. Work by Peter Goadsby and his colleagues at the Institute of Neurology in London, among others, suggests that a widely accepted explanation of migraines is actually the wrong way round—and that the focus of existing therapies is therefore wrong, too.</p>\n<p style="margin-bottom: 1rem;">This accepted explanation is that the initial cause of migraines lies in the blood vessels of the head, rather than the nerve cells of the brain. Arteries leading to the brain constrict in response to an unspecified external trigger. That leads to reduced blood flow, causing nerve cells in the afflicted area to function abnormally.</p>\n<p style="margin-bottom: 1rem;">It is this malfunction, supposedly, that creates the so-called "aura" of a classical migraine: the flashing lights, areas of visual loss and even pins and needles in the face or limbs that torment some sufferers. The pain, by contrast, is blamed on the blood vessels themselves. These, it is supposed, dilate as a reflex reaction to the initial constriction, and the pressure thus produced triggers pain. Drugs designed to curb migraine pain have therefore aimed at stopping blood vessels dilating.</p>\n<p style="margin-bottom: 1rem;">Brain-imaging studies suggest, however, that migraines are neurological disorders, rather than circulatory ones. Again, there is an external trigger, but in this case it causes nerve cells in such areas as the visual cortex to fire off wildly and then become quiescent. That creates the phenomena of the migraine aura. Increases in blood-vessel diameter are, indeed, observed in some patients. But Dr Goadsby has shown that types of head pain other than migraine lead to dilatation of the blood vessels, so it does not appear to be a special feature of the condition.</p>\n<p style="margin-bottom: 1rem;">Dr Goadsby believes that the pain associated with migraine is actually due to the brain's misinterpretation of signals from elsewhere, and is nothing to do with this dilation. Rather, it is because those suffering migraines have a problem processing normal stimuli such as light, sound and probably pain signals, too. Such normal signals become, as it were, painfully amplified. This theory is backed up by brain scans which show that another part of the brain, its stem, is also a centre of abnormal activity during a migraine attack. The brain stem is the area which controls the reflexes of hunger and breathing. It also acts as a filter, allowing people to edit out distracting or unwanted signals such as background noise. When it goes awry, signals crowd in, causing a system overload.</p>\n<p style="margin-bottom: 1rem;">This hypothesis allows patients with doctors who endorse it to benefit from imaginative prescription. In particular, the anti-convulsant drugs used by epileptic patients to prevent seizures seem to be good at turning down the nerve cells which cause the trouble in migraines. According to Dr Goadsby, around 70% of patients with severe migraine can benefit from taking such medicines.</p>\n<p style="margin-bottom: 1rem;">Why this should be is unknown, though the fact that the drugs, which include valproate and gabapentin, act on nerve cells that rely on calcium for part of their communication with each other may be significant. Anti-convulsants, however, are a blunt instrument: they can cause a range of side-effects, including fatigue, hair loss and anxiety.</p>\n<p style="margin-bottom: 1rem;">Hence the search for a more precise weapon ideally one that finds its targets only in the brain stem. Researchers at Eli-Lilly and GlaxoSmithKline are embarking on trials of drugs aimed at blocking the actions of nerve cells that receive their instructions from "neurotransmitter" molecules called adenosine and glutamate. Crucially, these drugs do not also act on blood vessels, something that has made old-style drugs unpalatable to anybody with heart disease or blood-pressure problems. The end of migraine pain may therefore soon be in sight.</p>`
};

const wordParts = [];
const mid = Math.ceil(u.words.length / 2);
wordParts.push(u.words.slice(0, mid));
wordParts.push(u.words.slice(mid));

let wordListHtml1 = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;">
<p style="display: none;">Word List 1</p>
<div style="display: flex; flex-direction: column; gap: 16px;">
<img src="/unit${u.unit}_ielts_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" />
</div>
<div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;">
<h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3>
<div style="display: flex; flex-direction: column; gap: 24px;">`;

wordParts[0].forEach(w => {
  wordListHtml1 += `<div style="display: flex; gap: 16px; align-items: flex-start;">
<div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">dY~Z</div>
<div style="display: flex; flex-direction: column; gap: 6px;">
<div style="display: flex; align-items: baseline; gap: 8px;">
<span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span>
<span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron || ''}</span>
<span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.pos || ''}</span>
</div>
<div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def || ''} <span style="color: #0ea5e9;">${w.defVi || ''}</span></div>
<div style="color: #64748b; font-size: 0.95rem; font-style: italic;">"${w.ex || ''}" <span style="color: #0ea5e9;">${w.exVi || ''}</span></div>
</div></div>`;
});
wordListHtml1 += `</div></div></div>`;

let wordListHtml2 = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;">
<p style="display: none;">Word List 2</p>
<div style="display: flex; flex-direction: column; gap: 16px;">
<img src="/unit${u.unit}_ielts_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" />
</div>
<div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;">
<h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3>
<div style="display: flex; flex-direction: column; gap: 24px;">`;

wordParts[1].forEach(w => {
  wordListHtml2 += `<div style="display: flex; gap: 16px; align-items: flex-start;">
<div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">dY~Z</div>
<div style="display: flex; flex-direction: column; gap: 6px;">
<div style="display: flex; align-items: baseline; gap: 8px;">
<span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span>
<span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron || ''}</span>
<span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.pos || ''}</span>
</div>
<div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def || ''} <span style="color: #0ea5e9;">${w.defVi || ''}</span></div>
<div style="color: #64748b; font-size: 0.95rem; font-style: italic;">"${w.ex || ''}" <span style="color: #0ea5e9;">${w.exVi || ''}</span></div>
</div></div>`;
});
wordListHtml2 += `</div></div></div>`;

let readingHtml = `<div style="display: flex; flex-direction: column; gap: 16px; margin-bottom: 20px;">
<p style="display: none;">Comprehensive Reading</p>
<img src="/unit${u.unit}_ielts_story.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" />
<div style="font-family: Arial, sans-serif; ">${u.story}</div></div>`;

const finalJson = {
  parts: [
    { title: "Word List 1", content: wordListHtml1, sections: [] },
    { title: "Word List 2", content: wordListHtml2, sections: [] },
    { title: "Comprehensive Reading", content: readingHtml, sections: [] }
  ],
  basicInfo: {
    skill: "MCQ (Standard)",
    title: u.title,
    category: "exercise",
    courseId: "239a64f0-c106-40e5-a6e2-4e685a0d70fb",
    timeLimit: 40
  }
};

fs.writeFileSync(`public/unit${u.unit}_ielts.json`, JSON.stringify(finalJson, null, 2));
console.log(`Unit ${u.unit} generated successfully.`);
