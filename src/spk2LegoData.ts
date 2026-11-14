// ============================================================================
// IELTS SPEAKING PART 2 — LEGO BLOCKS, ADAPTIVE "..." SLOTS & HOOK STEERING DATA
// 6 Main Blocks + 3 Plugin Blocks + Adaptive Topic-Anchor Slots + 55 Past Papers
// ============================================================================

export type Spk2BlockType = 'main' | 'plugin';

export type Spk2BlockId =
  | 'person'
  | 'place_service'
  | 'historical_nature'
  | 'object_entity'
  | 'action_experience'
  | 'relation_ceremony'
  | 'food'
  | 'plant'
  | 'weather';

export interface Spk2SlotExample {
  tagVi: string;
  valueEn: string;
}

export interface Spk2AdaptiveSlot {
  id: string;
  labelVi: string;
  defaultEn: string;
  hintVi: string;
  examples: Spk2SlotExample[];
}

export interface Spk2StageBrick {
  id: string;
  blockId: Spk2BlockId;
  stageNumber: 1 | 2 | 3 | 4;
  stageTitle: string;
  textEn: string;
  templateEn: string;
  slots: Spk2AdaptiveSlot[];
  textVi: string;
  keywords: string[];
  goldenPhrases: string[];
}

export interface Spk2LegoBlock {
  id: Spk2BlockId;
  code: string;
  type: Spk2BlockType;
  name: string;
  titleVi: string;
  emoji: string;
  colorHex: string;
  badgeBg: string;
  badgeText: string;
  borderClass: string;
  usedFor: string;
  stages: Spk2StageBrick[];
}

export interface Spk2HookFormula {
  id: string;
  name: string;
  tagVi: string;
  templateEn: string;
  guideVi: string;
}

export interface Spk2ConnectorBridge {
  id: string;
  targetBlockId: Spk2BlockId | 'any';
  labelVi: string;
  bridgeEn: string;
}

export interface Spk2PromptItem {
  num: number;
  title: string;
  cueBullets: string[];
  recommendedBlockId: Spk2BlockId;
  recommendedPluginIds: Spk2BlockId[];
  isDirectMatch?: boolean;
  slotSuggestions?: Record<string, string>;
  hookLogicVi: string;
  sampleHookEn: string;
  sampleClosingEn: string;
}

export function renderStageBrickText(
  brick: Spk2StageBrick,
  slotOverrides?: Record<string, string>
): string {
  if (!brick.templateEn || !brick.slots || brick.slots.length === 0) {
    return brick.textEn;
  }
  let out = brick.templateEn;
  for (const sl of brick.slots) {
    const chosen = slotOverrides?.[sl.id];
    const finalVal = chosen !== undefined && chosen.trim() !== '' ? chosen.trim() : sl.defaultEn;
    out = out.split(`{{${sl.id}}}`).join(finalVal);
  }
  return out.replace(/\s+([.,!?;:])/g, '$1').replace(/\s{2,}/g, ' ').trim();
}

export const SPK2_LEGO_BLOCKS: Spk2LegoBlock[] = [
  {
    id: 'person',
    code: 'M1',
    type: 'main',
    name: 'Mr. John (Person)',
    titleVi: 'Khối Chính 1: Tả Người (Chú John)',
    emoji: '👨‍🦳',
    colorHex: '#2563eb',
    badgeBg: 'bg-blue-100',
    badgeText: 'text-blue-800',
    borderClass: 'border-blue-300',
    usedFor: 'Người lớn tuổi, người lạ, người thông minh, người giúp đỡ, hàng xóm, người nổi tiếng, thành viên gia đình...',
    stages: [
      {
        id: 'person_s1',
        blockId: 'person',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          "I would like to talk about Mr. John. When I was a child, my parents were very busy, so I had to spend a lot of time on my own. During that time, I met John, who was one of my father's best friends. To be honest, he took really good care of me.",
        templateEn:
          'I would like to talk about Mr. John. When I was a child, my parents were very busy, so I had to spend a lot of time on my own. During that time, I met John, {{person_s1_anchor}}. To be honest, he took really good care of me.',
        slots: [
          {
            id: 'person_s1_anchor',
            labelVi: 'Khe ... Định danh & Mối quan hệ',
            defaultEn: "who was one of my father's best friends",
            hintVi: 'Thay mối quan hệ/thân thế của chú John để khớp 100% nhân vật đề bài hỏi',
            examples: [
              { tagVi: 'Hàng xóm thú vị', valueEn: 'who was our kind-hearted next-door neighbour' },
              { tagVi: 'Người lạ bắt chuyện', valueEn: 'who was a complete stranger at the park before I learned he knew my dad' },
              { tagVi: 'Người nổi tiếng', valueEn: 'a famous former national basketball player who knew my dad' },
              { tagVi: 'Người thân tự hào', valueEn: "my father's cousin whom our whole family is really proud of" },
              { tagVi: 'Vỏ bọc Phim vũ trụ', valueEn: 'a retired astronaut in that movie who mentored a lonely boy just like me' }
            ]
          }
        ],
        textVi:
          'Tôi muốn nói về ông John. Khi còn nhỏ, cha mẹ tôi rất bận nên tôi phải dành phần lớn thời gian một mình. Trong thời gian đó, tôi đã gặp John, [một trong những người bạn thân nhất của cha tôi / ... vai trò khớp đề]. Thành thật mà nói, chú ấy đã chăm sóc tôi rất tốt.',
        keywords: ['talk', 'child', 'During', '... [vai trò]', 'good care'],
        goldenPhrases: ['spend a lot of time on my own', 'To be honest', 'took really good care of me']
      },
      {
        id: 'person_s2',
        blockId: 'person',
        stageNumber: 2,
        stageTitle: 'Stage 2: Appearance & Personality',
        textEn:
          "In fact, John is a very gentle and kind man. As far as I recall, he was quite tall, about 6 feet. He was also really good at basketball. Whenever I think of him, I can't help laughing because the way he walked was so funny. It looked like he was walking on sticks!",
        templateEn:
          "In fact, John is {{person_s2_trait}}. As far as I recall, he was quite tall, about 6 feet. He was also really good at basketball. Whenever I think of him, I can't help laughing because the way he walked was so funny. It looked like he was walking on sticks!",
        slots: [
          {
            id: 'person_s2_trait',
            labelVi: 'Khe ... Phẩm chất / Tính cách đề hỏi',
            defaultEn: 'a very gentle and kind man',
            hintVi: 'Gài đúng tính từ chỉ phẩm chất trên Cue Card (polite, clever, helpful, interesting...)',
            examples: [
              { tagVi: 'Người lịch sự', valueEn: 'an extraordinarily polite and well-mannered man who greeted everyone warmly' },
              { tagVi: 'Giải quyết vấn đề khéo', valueEn: 'a very clever and insightful man who solved tricky problems gently' },
              { tagVi: 'Hay giúp đỡ học tập', valueEn: 'an incredibly helpful and patient mentor whenever I struggled at school' },
              { tagVi: 'Nói chuyện cuốn hút', valueEn: 'a fascinating and humorous storyteller who made every talk memorable' }
            ]
          }
        ],
        textVi:
          'Thực tế là, John là [một người rất nhẹ nhàng và tốt bụng / ... phẩm chất đề hỏi]. Theo như tôi nhớ, chú ấy khá cao, khoảng 6 feet và chơi bóng rổ rất giỏi. Mỗi khi nghĩ về chú, tôi không nhịn được cười vì dáng đi buồn cười như đi trên cà kheo!',
        keywords: ['... [phẩm chất]', 'far', 'basketball', 'appearance', 'sticks'],
        goldenPhrases: ['As far as I recall', "can't help laughing", 'walking on sticks']
      },
      {
        id: 'person_s3',
        blockId: 'person',
        stageNumber: 3,
        stageTitle: 'Stage 3: Memories',
        textEn:
          'If my memory serves me well, we used to play basketball in my backyard. Although John was great at basketball, he often pretended to lose and let me win. It always brings tears to my eyes every time I recall those beautiful memories.',
        templateEn:
          'If my memory serves me well, we used to play basketball in my backyard. Although John was great at basketball, he often {{person_s3_memory}}. It always brings tears to my eyes every time I recall those beautiful memories.',
        slots: [
          {
            id: 'person_s3_memory',
            labelVi: 'Khe ... Kỷ niệm / Hành động bám đề',
            defaultEn: 'pretended to lose and let me win',
            hintVi: 'Giữ chi tiết nhường thắng bóng rổ và nối thêm đúng hành động Cue Card yêu cầu',
            examples: [
              { tagVi: 'Cách xử lý thông minh', valueEn: 'pretended to lose and let me win, which was his clever trick to cure my shyness' },
              { tagVi: 'Giúp đỡ học tập', valueEn: 'pretended to lose to cheer me up before patiently tutoring me in English' },
              { tagVi: 'Trò chuyện / Speech', valueEn: 'pretended to lose and shared deep life advice with me during our breaks' },
              { tagVi: 'Quyết định không đồng tình', valueEn: 'pretended to lose to make me smile, so I strongly disagreed when he later decided to move away' }
            ]
          }
        ],
        textVi:
          'Nếu tôi nhớ không lầm, chúng tôi thường chơi bóng rổ ở sân sau. Mặc dù John chơi rất giỏi, chú ấy thường [giả vờ thua và nhường tôi thắng / ... hành động gắn với đề]. Điều đó luôn làm tôi rưng rưng nước mắt mỗi khi nhớ lại những kỷ niệm đẹp ấy.',
        keywords: ['memory', 'Although', '... [hành động bám đề]', 'tears'],
        goldenPhrases: ['If my memory serves me well', 'Although', 'brings tears to my eyes']
      },
      {
        id: 'person_s4',
        blockId: 'person',
        stageNumber: 4,
        stageTitle: 'Stage 4: Influence & Feelings',
        textEn:
          "He always taught me to be more patient and understanding towards other people. If it hadn't been for him, I wouldn't be the person I am today. John was a great role model for me. Now that I'm an adult, I still miss him because we don't live near each other anymore. I really hope I can see him again one day.",
        templateEn:
          "He always taught me {{person_s4_lesson}}. If it hadn't been for him, I wouldn't be the person I am today. John was a great role model for me. Now that I'm an adult, I still miss him because we don't live near each other anymore. I really hope I can see him again one day.",
        slots: [
          {
            id: 'person_s4_lesson',
            labelVi: 'Khe ... Bài học / Ảnh hưởng cuối bài',
            defaultEn: 'to be more patient and understanding towards other people',
            hintVi: 'Nhắc lại bài học/cảm xúc trả lời câu hỏi Why ở dòng cuối Cue Card',
            examples: [
              { tagVi: 'Sự lịch thiệp', valueEn: 'to treat everyone around me with genuine politeness and respect' },
              { tagVi: 'Học tập & Kỷ luật', valueEn: 'to stay confident and disciplined whenever my studies got tough' },
              { tagVi: 'Tư duy thông minh', valueEn: 'to stay calm and solve every problem in a creative, gentle way' },
              { tagVi: 'Khiêm tốn dù nổi tiếng', valueEn: 'to remain humble and kind despite all his fame on the court' }
            ]
          }
        ],
        textVi:
          'Chú luôn dạy tôi [kiên nhẫn và thấu hiểu người khác hơn / ... bài học bám đề]. Nếu không có chú, tôi sẽ không trở thành người như hôm nay. John là hình mẫu tuyệt vời của tôi. Giờ đã trưởng thành, tôi vẫn nhớ chú và hy vọng có thể gặp lại chú một ngày nào đó.',
        keywords: ['taught', '... [bài học]', "hadn't been", 'role model', 'see him'],
        goldenPhrases: ["If it hadn't been for him, I wouldn't be the person I am today", 'great role model']
      }
    ]
  },
  {
    id: 'place_service',
    code: 'M2',
    type: 'main',
    name: 'A Modern Flat (Place/Service)',
    titleVi: 'Khối Chính 2: Địa Điểm Hiện Đại & Dịch Vụ',
    emoji: '🏙️',
    colorHex: '#0891b2',
    badgeBg: 'bg-cyan-100',
    badgeText: 'text-cyan-800',
    borderClass: 'border-cyan-300',
    usedFor: 'Ngôi nhà mơ ước, quán cafe/cửa hàng mới mở, nhà hàng, nơi có dịch vụ tốt, thành phố, tin vui, tranh nghệ thuật, trạm vũ trụ...',
    stages: [
      {
        id: 'place_s1',
        blockId: 'place_service',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          "I would like to talk about a modern flat that I'd love to own one day. It is located in Hoan Kiem district, right in the centre of Hanoi, close to all the best restaurants and shops.",
        templateEn:
          "I would like to talk about a modern flat that I'd love to own one day. {{place_s1_setting}}.",
        slots: [
          {
            id: 'place_s1_setting',
            labelVi: 'Khe ... Loại không gian & Vị trí',
            defaultEn: 'It is located in Hoan Kiem district, right in the centre of Hanoi, close to all the best restaurants and shops',
            hintVi: 'Đổi căn hộ thành quán cafe, shop mới mở, nơi treo bức tranh hoặc trạm khách sạn vũ trụ!',
            examples: [
              { tagVi: 'Shop / Quán cafe mới mở', valueEn: 'This newly opened rooftop café and bakery is located in Hoan Kiem district, right in the centre of Hanoi' },
              { tagVi: 'Bức tranh nghệ thuật', valueEn: 'The stylish apartment where I saw that painting is located right in the centre of Hoan Kiem district, Hanoi' },
              { tagVi: 'Chuyển nhà / Tin vui', valueEn: 'This brand-new family apartment is located in Hoan Kiem district, right in the centre of Hanoi' },
              { tagVi: 'Trạm khách sạn Vũ trụ 🚀', valueEn: 'This futuristic orbital hotel floats peacefully in low Earth orbit, designed just like a luxury apartment' }
            ]
          }
        ],
        textVi:
          'Tôi muốn nói về một căn hộ hiện đại (hoặc quán cafe/không gian khớp đề). [Nó nằm ở quận Hoàn Kiếm, ngay trung tâm Hà Nội, gần các nhà hàng và cửa hàng tốt nhất / ... vị trí & bối cảnh đề hỏi].',
        keywords: ['flat / place', '... [bối cảnh & vị trí]', 'centre', 'close'],
        goldenPhrases: ['right in the centre of Hanoi', 'close to all the best restaurants and shops']
      },
      {
        id: 'place_s2',
        blockId: 'place_service',
        stageNumber: 2,
        stageTitle: 'Stage 2: Description',
        textEn:
          'The place is on a high floor of a brand-new building. The style is very modern, with wooden floors, comfortable leather sofas, and colourful rugs. It is also very airy and bright, with lots of windows and great views of the city.',
        templateEn:
          'The place is on a high floor of a brand-new building. The style is very modern, with wooden floors, comfortable leather sofas, and colourful rugs. It is also very airy and bright, with {{place_s2_feature}}.',
        slots: [
          {
            id: 'place_s2_feature',
            labelVi: 'Khe ... Điểm nhấn thị giác bám đề',
            defaultEn: 'lots of windows and great views of the city',
            hintVi: 'Cài chi tiết bức tranh, quầy bánh/cà phê, nhân viên phục vụ hoặc cửa sổ ngắm Trái Đất',
            examples: [
              { tagVi: 'Tác phẩm nghệ thuật', valueEn: 'sunlit windows illuminating that colourful oil painting of old Hanoi right above the sofa' },
              { tagVi: 'Shop / Quán cafe', valueEn: 'panoramic windows, great city views, and warm shelves displaying handmade pastries' },
              { tagVi: 'Dịch vụ xuất sắc', valueEn: 'great city views and attentive staff who welcome every guest with a warm smile' },
              { tagVi: 'Trạm không gian 🚀', valueEn: 'giant observation windows offering breathtaking views of our blue Earth and the stars' }
            ]
          }
        ],
        textVi:
          'Nơi này nằm trên tầng cao của một tòa nhà mới. Phong cách rất hiện đại với sàn gỗ, sofa da êm ái và thảm đầy màu sắc. Không gian rất thoáng đãng, sáng sủa với [nhiều cửa sổ và tầm nhìn tuyệt đẹp / ... điểm nhấn của đề].',
        keywords: ['high floor', 'modern', 'wooden', 'airy', '... [điểm nhấn]'],
        goldenPhrases: ['brand-new building', 'airy and bright', 'great views of the city']
      },
      {
        id: 'place_s3',
        blockId: 'place_service',
        stageNumber: 3,
        stageTitle: 'Stage 3: Activities',
        textEn:
          'This place is perfect for my family and friends to relax. A modern kitchen is great for preparing delicious drinks and meals. Also, our guests can easily relax in the comfortable living room.',
        templateEn:
          'This place is perfect for my family and friends to relax. {{place_s3_activity}}',
        slots: [
          {
            id: 'place_s3_activity',
            labelVi: 'Khe ... Hoạt động diễn ra tại đó',
            defaultEn: 'A modern kitchen is great for preparing delicious drinks and meals. Also, our guests can easily relax in the comfortable living room.',
            hintVi: 'Mô tả đúng hoạt động đề bài hỏi (thưởng thức cafe, ngắm tranh, nhận dịch vụ tốt, thiết kế nội thất...)',
            examples: [
              { tagVi: 'Quán cafe / Nhà hàng', valueEn: 'An open bar counter serves delicious drinks and pastries, and customers can easily unwind in the cozy lounge.' },
              { tagVi: 'Dịch vụ tốt', valueEn: 'The staff patiently recommended their best dishes and refilled our tea while we relaxed in the lounge.' },
              { tagVi: 'Ngắm bức tranh', valueEn: 'Standing in that living room, everyone gathers to admire the vivid brushstrokes and peaceful vibe of the artwork.' },
              { tagVi: 'Công việc mơ ước', valueEn: 'As an interior architect, designing smart kitchens and cozy living rooms like this would be my daily passion.' }
            ]
          }
        ],
        textVi:
          'Nơi này hoàn hảo để gia đình và bạn bè thư giãn. [Căn bếp hiện đại rất tuyệt để chuẩn bị đồ uống, bữa ăn ngon và khách có thể nghỉ ngơi ở phòng khách / ... hoạt động khớp đề].',
        keywords: ['perfect', '... [hoạt động khớp đề]', 'prepare', 'relax'],
        goldenPhrases: ['preparing delicious drinks and meals', 'comfortable living room']
      },
      {
        id: 'place_s4',
        blockId: 'place_service',
        stageNumber: 4,
        stageTitle: 'Stage 4: Feelings & Future',
        textEn:
          'I know that a place like this is very expensive. However, if I am successful in my career and make a lot of money one day, this is exactly the kind of place I will buy. I think almost everybody would love to spend time in a place like this.',
        templateEn:
          'I know that a place like this is very expensive. However, {{place_s4_future}}. I think almost everybody would love to spend time in a place like this.',
        slots: [
          {
            id: 'place_s4_future',
            labelVi: 'Khe ... Cảm nhận & Mong muốn chốt đề',
            defaultEn: 'if I am successful in my career and make a lot of money one day, this is exactly the kind of place I will buy',
            hintVi: 'Tránh nói nhầm "sẽ mua căn hộ" nếu đề hỏi về quán cafe, dịch vụ hoặc bức tranh!',
            examples: [
              { tagVi: 'Quán cafe / Shop / Dịch vụ', valueEn: 'their menu prices are very reasonable for such top-notch quality, so I visit almost every weekend' },
              { tagVi: 'Tin vui / Chuyển nhà', valueEn: 'hearing that our family could finally move into this flat made us burst with joy and pride' },
              { tagVi: 'Bức tranh nghệ thuật', valueEn: 'if I make good money one day, I would love to own a similar painting to brighten up my home' },
              { tagVi: 'Trạm không gian 🚀', valueEn: 'if space travel becomes affordable in the future, this orbital hotel is the first place I will visit' }
            ]
          }
        ],
        textVi:
          'Tôi biết một không gian như vậy rất đắt đỏ. Tuy nhiên, [nếu thành công và kiếm nhiều tiền, đây chính xác là nơi tôi sẽ mua / ... cảm nhận khớp đề]. Hầu như ai cũng thích dành thời gian ở nơi như vậy.',
        keywords: ['expensive', 'However', '... [cảm nhận chốt đề]', 'everybody'],
        goldenPhrases: ['However', 'successful in my career', 'spend time in a place like this']
      }
    ]
  },
  {
    id: 'historical_nature',
    code: 'M3',
    type: 'main',
    name: 'Bai Dinh Temple (Historical/Nature)',
    titleVi: 'Khối Chính 3: Di Tích & Thiên Nhiên (Chùa Bái Đính)',
    emoji: '🏯',
    colorHex: '#059669',
    badgeBg: 'bg-emerald-100',
    badgeText: 'text-emerald-800',
    borderClass: 'border-emerald-300',
    usedFor: 'Chuyến đi tương lai, địa điểm lịch sử, bức tượng, nơi yên tĩnh/đông người, miền quê, cấm dùng ĐT, ngắm bầu trời...',
    stages: [
      {
        id: 'hist_s1',
        blockId: 'historical_nature',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          'I would like to talk about Bai Dinh temple. It is a famous cultural and spiritual complex in Ninh Binh province, which is very close to Hanoi.',
        templateEn:
          'I would like to talk about Bai Dinh temple. It is {{hist_s1_intro}}, which is very close to Hanoi.',
        slots: [
          {
            id: 'hist_s1_intro',
            labelVi: 'Khe ... Góc giới thiệu Bái Đính theo đề',
            defaultEn: 'a famous cultural and spiritual complex in Ninh Binh province',
            hintVi: 'Nhấn ngay vào yếu tố đề hỏi (pho tượng Phật, miền quê yên bình, sông nước hay điểm đến sắp tới)',
            examples: [
              { tagVi: 'Pho tượng nghệ thuật', valueEn: 'home to a magnificent giant bronze Buddha statue in Ninh Binh province' },
              { tagVi: 'Miền quê / Ngắm sao', valueEn: 'nestled in the peaceful green countryside of Ninh Binh province' },
              { tagVi: 'Bơi lội / Ven sông nước', valueEn: 'set beside a crystal-clear scenic river lagoon in Ninh Binh province' },
              { tagVi: 'Chuyến đi tương lai', valueEn: 'a famous spiritual complex in Ninh Binh province that my friends and I plan to visit soon' }
            ]
          }
        ],
        textVi:
          'Tôi muốn nói về chùa Bái Đính. Đây là [quần thể văn hóa tâm linh nổi tiếng ở Ninh Bình / ... góc giới thiệu khớp đề], rất gần Hà Nội.',
        keywords: ['talk', '... [góc giới thiệu]', 'Ninh Binh', 'close'],
        goldenPhrases: ['cultural and spiritual complex', 'very close to Hanoi']
      },
      {
        id: 'hist_s2',
        blockId: 'historical_nature',
        stageNumber: 2,
        stageTitle: 'Stage 2: Description',
        textEn:
          'It is considered the largest Buddhist temple in Vietnam. The place is very beautiful and vast, representing traditional Vietnamese architecture. There is also a large river around the complex.',
        templateEn:
          'It is considered the largest Buddhist temple in Vietnam. The place is very beautiful and vast, {{hist_s2_detail}}. There is also a large river around the complex.',
        slots: [
          {
            id: 'hist_s2_detail',
            labelVi: 'Khe ... Đặc tả cảnh quan khớp đề',
            defaultEn: 'representing traditional Vietnamese architecture',
            hintVi: 'Gài chi tiết pho tượng, đám đông lễ hội, biển cấm điện thoại hoặc bầu trời đêm không ánh đèn',
            examples: [
              { tagVi: 'Pho tượng đồng', valueEn: 'housing a towering golden statue with a gentle smile inside its traditional wooden hall' },
              { tagVi: 'Nơi đông đúc', valueEn: 'drawing thousands of bustling visitors during festival season despite its traditional architecture' },
              { tagVi: 'Cấm dùng điện thoại', valueEn: 'with sacred prayer halls where everyone must turn off their mobile phones out of respect' },
              { tagVi: 'Ngắm bầu trời sao 🚀', valueEn: 'with open courtyards free from city light pollution so stars shine brightly overhead' }
            ]
          }
        ],
        textVi:
          'Nơi đây được xem là ngôi chùa lớn nhất Việt Nam, rất đẹp và rộng lớn, [đại diện kiến trúc truyền thống / ... chi tiết bám đề] và có con sông lớn bao quanh.',
        keywords: ['considered', 'largest', 'beautiful & vast', '... [chi tiết bám đề]', 'river'],
        goldenPhrases: ['considered the largest Buddhist temple', 'representing traditional Vietnamese architecture']
      },
      {
        id: 'hist_s3',
        blockId: 'historical_nature',
        stageNumber: 3,
        stageTitle: 'Stage 3: Activities',
        textEn:
          'When I visit this place, I just like to walk around the lake and enjoy the beautiful view. It is always great fun and a pleasure for me.',
        templateEn:
          '{{hist_s3_action}}. It is always great fun and a pleasure for me.',
        slots: [
          {
            id: 'hist_s3_action',
            labelVi: 'Khe ... Trải nghiệm / Hành động thực tế',
            defaultEn: 'When I visit this place, I just like to walk around the lake and enjoy the beautiful view',
            hintVi: 'Đổi sang thì tương lai nếu đề hỏi Plan/Future trip, hoặc gài hoạt động bơi/tắt ĐT/ngắm sao',
            examples: [
              { tagVi: 'Chuyến đi tương lai', valueEn: 'Once we arrive there on our upcoming trip, we will walk around the lake and enjoy the beautiful view' },
              { tagVi: 'Cấm dùng điện thoại', valueEn: 'Although I wanted to use my phone to snap photos, putting it away let me walk around the lake and truly enjoy the view' },
              { tagVi: 'Bơi lội / Chèo thuyền', valueEn: 'Visitors there love taking a refreshing swim or boat ride in the clean lagoon before walking around the lake' },
              { tagVi: 'Ngắm bầu trời sao 🚀', valueEn: 'Sitting quietly by the lake that evening, we gazed up at thousands of twinkling stars across the sky' }
            ]
          }
        ],
        textVi:
          '[Khi ghé thăm nơi này, tôi thích đi dạo quanh hồ và ngắm cảnh đẹp / ... hành động khớp đề]. Đó luôn là niềm vui và sự thư thái lớn đối với tôi.',
        keywords: ['... [hành động khớp đề]', 'walk / lake', 'view', 'fun', 'pleasure'],
        goldenPhrases: ['walk around the lake', 'great fun and a pleasure']
      },
      {
        id: 'hist_s4',
        blockId: 'historical_nature',
        stageNumber: 4,
        stageTitle: 'Stage 4: Significance',
        textEn:
          "This place is really important to me. Although there are usually many tourists, I can still easily find a quiet place to myself whenever I want to escape the busy city. If it hadn't been for this place, I wouldn't have been able to relax, unwind, and do pretty well in my last exam.",
        templateEn:
          "This place is really important to me. Although there are usually many tourists, I can still easily find a quiet place to myself whenever I want to escape the busy city. If it hadn't been for {{hist_s4_impact}}, I wouldn't have been able to relax, unwind, and do pretty well in my last exam.",
        slots: [
          {
            id: 'hist_s4_impact',
            labelVi: 'Khe ... Điểm chạm cảm xúc câu ĐK loại 3',
            defaultEn: 'this place',
            hintVi: 'Điền đúng danh từ của đề sau "If it hadn\'t been for ..." để câu chốt ăn điểm tuyệt đối',
            examples: [
              { tagVi: 'Cấm dùng điện thoại', valueEn: 'that phone-free afternoon at the temple' },
              { tagVi: 'Pho tượng Phật', valueEn: 'the calm feeling of standing before that majestic statue' },
              { tagVi: 'Ngày ở quê / Ngắm sao', valueEn: 'that peaceful countryside evening under the starry sky' },
              { tagVi: 'Kế hoạch tương lai', valueEn: 'planning this refreshing getaway with my family' }
            ]
          }
        ],
        textVi:
          'Nơi này rất quan trọng với tôi. Dù đông du khách, tôi vẫn dễ tìm được góc yên tĩnh để trốn khỏi thành phố ồn ào. Nếu không nhờ [nơi này / ... điểm chạm đề bài], tôi đã không thể thư giãn và làm tốt kỳ thi vừa qua.',
        keywords: ['important', 'Although', 'quiet', 'escape', "hadn't been + ...", 'unwind'],
        goldenPhrases: ['escape the busy city', "If it hadn't been for", 'relax, unwind']
      }
    ]
  },
  {
    id: 'object_entity',
    code: 'M4',
    type: 'main',
    name: 'The Bicycle (Object/Entity)',
    titleVi: 'Khối Chính 4: Đồ Vật, Phát Minh & Tổ Chức (Xe Đạp)',
    emoji: '🚲',
    colorHex: '#7c3aed',
    badgeBg: 'bg-violet-100',
    badgeText: 'text-violet-800',
    borderClass: 'border-violet-300',
    usedFor: 'Phát minh thay đổi cuộc sống, món đồ yêu thích, quà miễn phí, áo thể thao, công ty lớn, trang web, cuốn sách/TV series...',
    stages: [
      {
        id: 'obj_s1',
        blockId: 'object_entity',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          'I would like to talk about my bicycle. As you know, a bicycle is a simple, human-powered vehicle. If my memory serves me well, it was first invented back in 1817 by a German professor. My parents bought me my first bicycle as a Tet holiday gift when I was a teenager.',
        templateEn:
          'I would like to talk about my bicycle. As you know, a bicycle is a simple, human-powered vehicle. If my memory serves me well, it was first invented back in 1817 by a German professor. {{obj_s1_origin}}.',
        slots: [
          {
            id: 'obj_s1_origin',
            labelVi: 'Khe ... Nguồn gốc / Lớp vỏ bọc đề bài',
            defaultEn: 'My parents bought me my first bicycle as a Tet holiday gift when I was a teenager',
            hintVi: 'Kết nối chiếc xe đạp với món đồ miễn phí, chiếc áo, trang web, công ty hoặc cuốn sách/bộ phim!',
            examples: [
              { tagVi: 'Nhận đồ miễn phí', valueEn: 'I actually received my first bicycle completely for free in a lucky draw when I was a teenager' },
              { tagVi: 'Áo yêu thích', valueEn: 'My parents gave me that breathable blue cycling jersey right along with my first bike as a Tet gift' },
              { tagVi: 'Trang web hữu ích', valueEn: 'I first read about that 1817 history on CycleLife.vn, a cycling website I browse almost every week' },
              { tagVi: 'Công ty đông nhân viên', valueEn: 'In my city, Thong Nhat Company employs thousands of local workers to manufacture reliable bicycles like mine' },
              { tagVi: 'TV Series / Sách', valueEn: 'That 1817 invention story was the opening episode/chapter that got me hooked from the very start' }
            ]
          }
        ],
        textVi:
          'Tôi muốn nói về chiếc xe đạp. Xe đạp là phương tiện chạy bằng sức người đơn giản, được phát minh năm 1817 bởi một giáo sư người Đức. [Bố mẹ mua cho tôi chiếc xe đầu tiên dịp Tết / ... nguồn gốc khớp đề].',
        keywords: ['bicycle', 'simple', 'memory', 'invented 1817', '... [nguồn gốc bám đề]'],
        goldenPhrases: ['human-powered vehicle', 'If my memory serves me well', 'invented back in 1817']
      },
      {
        id: 'obj_s2',
        blockId: 'object_entity',
        stageNumber: 2,
        stageTitle: 'Stage 2: Main Features',
        textEn:
          'I think the bicycle is an extremely practical means of transport. Not only is it used for travelling from place to place, but it also greatly improves your health and fitness.',
        templateEn:
          'I think {{obj_s2_core}}. Not only is it used for travelling from place to place, but it also greatly improves your health and fitness.',
        slots: [
          {
            id: 'obj_s2_core',
            labelVi: 'Khe ... Nội dung chính gắn với đề',
            defaultEn: 'the bicycle is an extremely practical means of transport',
            hintVi: 'Nhắc lại chủ thể của đề (the website / the company / the show / the book / the jersey) ngay đầu Stage 2',
            examples: [
              { tagVi: 'Trang web hữu ích', valueEn: 'this website explains clearly why the bicycle is such a practical means of transport' },
              { tagVi: 'Công ty sản xuất', valueEn: 'the bikes built by this company are an extremely practical means of transport' },
              { tagVi: 'TV Series / Sách', valueEn: 'this series/book vividly shows why the bicycle is such a practical means of transport' },
              { tagVi: 'Trang phục yêu thích', valueEn: 'putting on that lightweight jersey makes riding this practical means of transport so comfortable' }
            ]
          }
        ],
        textVi:
          'Tôi nghĩ [xe đạp là phương tiện cực kỳ thiết thực / ... nội dung gắn đề]. Nó không chỉ dùng để đi lại từ nơi này sang nơi khác mà còn cải thiện đáng kể sức khỏe.',
        keywords: ['... [chủ thể đề]', 'means of transport', 'Not only', 'improves'],
        goldenPhrases: ['practical means of transport', 'Not only is it used..., but it also...']
      },
      {
        id: 'obj_s3',
        blockId: 'object_entity',
        stageNumber: 3,
        stageTitle: 'Stage 3: Benefits',
        textEn:
          'Moreover, riding a bicycle can help you get to work easily, save money, and avoid polluting the environment. Although my bike is not very expensive, I really appreciate it because of these wonderful benefits.',
        templateEn:
          'Moreover, riding a bicycle can help you get to work easily, save money, and avoid polluting the environment. Although {{obj_s3_concession}}, I really appreciate it because of these wonderful benefits.',
        slots: [
          {
            id: 'obj_s3_concession',
            labelVi: 'Khe ... Mệnh đề nhượng bộ Although ...',
            defaultEn: 'my bike is not very expensive',
            hintVi: 'Tùy biến mệnh đề sau Although để khen món đồ free, trang web miễn phí, công ty nội địa hoặc bộ phim/sách!',
            examples: [
              { tagVi: 'Đồ nhận miễn phí', valueEn: 'that free bike did not cost me a single penny' },
              { tagVi: 'Trang phục yêu thích', valueEn: 'that cycling jersey is simple rather than a luxury designer brand' },
              { tagVi: 'Trang web hữu ích', valueEn: 'using that cycling website is completely free of charge' },
              { tagVi: 'Công ty địa phương', valueEn: 'their locally produced bikes are very affordable' },
              { tagVi: 'TV Series / Sách', valueEn: 'the show/book has a simple storyline without flashy special effects' }
            ]
          }
        ],
        textVi:
          'Hơn nữa, đạp xe giúp đi làm dễ dàng, tiết kiệm tiền và tránh ô nhiễm môi trường. Mặc dù [chiếc xe không đắt lắm / ... nhượng bộ khớp đề], tôi thực sự trân trọng nó.',
        keywords: ['Moreover', 'save', 'polluting', 'Although + ...', 'appreciate'],
        goldenPhrases: ['Moreover', 'avoid polluting the environment', 'Although']
      },
      {
        id: 'obj_s4',
        blockId: 'object_entity',
        stageNumber: 4,
        stageTitle: 'Stage 4: Conclusion & Influence',
        textEn:
          "It has been my best companion for many years. If it hadn't been for this bike, I wouldn't be as healthy as I am now. I truly hope that riding a bicycle will soon become the main choice of transport for everyone in Hanoi.",
        templateEn:
          "It has been my best companion for many years. If it hadn't been for {{obj_s4_anchor}}, I wouldn't be as healthy as I am now. I truly hope that riding a bicycle will soon become the main choice of transport for everyone in Hanoi.",
        slots: [
          {
            id: 'obj_s4_anchor',
            labelVi: 'Khe ... Chốt hạ ĐK loại 3 bám đề',
            defaultEn: 'this bike',
            hintVi: 'Điền đúng từ khóa đề bài vào sau "If it hadn\'t been for ..."',
            examples: [
              { tagVi: 'Phát minh vĩ đại', valueEn: 'this brilliant invention' },
              { tagVi: 'Món quà miễn phí', valueEn: 'receiving that free bicycle' },
              { tagVi: 'Trang web hữu ích', valueEn: 'the workout tips on that website' },
              { tagVi: 'Công ty địa phương', valueEn: 'reliable bikes made by that company' },
              { tagVi: 'TV Series / Cuốn sách', valueEn: 'the inspiration from that series/book' }
            ]
          }
        ],
        textVi:
          'Nó là người bạn đồng hành suốt nhiều năm. Nếu không nhờ [chiếc xe này / ... chủ thể của đề], tôi sẽ không khỏe mạnh như hiện tại. Tôi hy vọng xe đạp sớm thành phương tiện chính ở Hà Nội.',
        keywords: ['companion', "hadn't been + ...", 'healthy', 'main choice'],
        goldenPhrases: ['best companion', "If it hadn't been for"]
      }
    ]
  },
  {
    id: 'action_experience',
    code: 'M5',
    type: 'main',
    name: 'Bicycle Racing (Action/Experience)',
    titleVi: 'Khối Chính 5: Sự Kiện & Trải Nghiệm (Giải Đua Xe Đạp)',
    emoji: '🏁',
    colorHex: '#ea580c',
    badgeBg: 'bg-orange-100',
    badgeText: 'text-orange-800',
    borderClass: 'border-orange-300',
    usedFor: 'Đến sớm/đến muộn, chờ đợi, lịch hẹn đẩy sớm, thay đổi tích cực, dịp hào hứng/mọi người cùng cười, buổi học tiếng Anh...',
    stages: [
      {
        id: 'act_s1',
        blockId: 'action_experience',
        stageNumber: 1,
        stageTitle: 'Stage 1: Background',
        textEn:
          'I would like to talk about a bicycle racing competition that I took part in and won. The name of the competition was "Race for Life", and its purpose was to raise money for charity. As far as I remember, it was held when I was in my last year at university, about two years ago.',
        templateEn:
          'I would like to talk about a bicycle racing competition that I took part in and won. The name of the competition was "Race for Life", and its purpose was to raise money for charity. As far as I remember, {{act_s1_when}}.',
        slots: [
          {
            id: 'act_s1_when',
            labelVi: 'Khe ... Mốc thời gian / Bối cảnh sự kiện',
            defaultEn: 'it was held when I was in my last year at university, about two years ago',
            hintVi: 'Đổi mốc thời gian về tuổi thơ, tương lai, xem trên TV hoặc câu chuyện kể trong tiết học tiếng Anh!',
            examples: [
              { tagVi: 'Kỷ niệm tuổi thơ', valueEn: 'it was a junior race held when I was in primary school, about ten years ago' },
              { tagVi: 'Kế hoạch chưa làm', valueEn: 'it is an annual race held every autumn that I plan to join right after my exams' },
              { tagVi: 'Tiết học tiếng Anh', valueEn: 'this was the exact story I told my classmates during that fun English speaking lesson' },
              { tagVi: 'Môn thể thao thích xem', valueEn: 'watching pro road races on TV inspired me to enter this local event two years ago' }
            ]
          }
        ],
        textVi:
          'Tôi muốn nói về giải đua xe đạp từ thiện "Race for Life". Theo như tôi nhớ, [nó được tổ chức khi tôi học năm cuối đại học, khoảng 2 năm trước / ... bối cảnh khớp đề].',
        keywords: ['talk', 'racing', 'charity', 'far', '... [mốc thời gian/bối cảnh]'],
        goldenPhrases: ['raise money for charity', 'As far as I remember']
      },
      {
        id: 'act_s2',
        blockId: 'action_experience',
        stageNumber: 2,
        stageTitle: 'Stage 2: The Challenge',
        textEn:
          'If my memory serves me well, I only started training two weeks before the competition. On the day of the race, I was about 15 minutes late because of a terrible traffic jam.',
        templateEn:
          'If my memory serves me well, I only started training two weeks before the competition. {{act_s2_twist}}.',
        slots: [
          {
            id: 'act_s2_twist',
            labelVi: 'Khe ... Tình huống kịch tính (Sớm/Muộn/Chờ/Lịch hẹn)',
            defaultEn: 'On the day of the race, I was about 15 minutes late because of a terrible traffic jam',
            hintVi: 'Xoay cực mượt cho các đề: Cần đến sớm, Chờ đợi kẹt xe, Lịch hẹn đẩy sớm hoặc Bận chưa thực hiện được!',
            examples: [
              { tagVi: 'Cần đến sớm', valueEn: 'We had to arrive an hour early for check-in, so getting stuck in a traffic jam gave me a huge scare' },
              { tagVi: 'Lịch hẹn đẩy sớm', valueEn: 'My check-in appointment was suddenly moved 30 minutes ahead of schedule right when I hit a traffic jam' },
              { tagVi: 'Chờ đợi sốt ruột', valueEn: 'On the morning of the race, I was stuck waiting anxiously for half an hour in a terrible traffic jam' },
              { tagVi: 'Kế hoạch chưa làm', valueEn: 'Because of my heavy exam workload, I still have not had enough free mornings to train for it yet' }
            ]
          }
        ],
        textVi:
          'Nếu tôi nhớ không lầm, tôi chỉ tập luyện 2 tuần trước giải. [Vào ngày đua, tôi bị muộn 15 phút vì tắc đường / ... tình huống kịch tính khớp đề].',
        keywords: ['serves', 'training', '... [tình huống kịch tính]', 'traffic jam'],
        goldenPhrases: ['If my memory serves me well', 'terrible traffic jam']
      },
      {
        id: 'act_s3',
        blockId: 'action_experience',
        stageNumber: 3,
        stageTitle: 'Stage 3: The Action',
        textEn:
          'Luckily, I was still able to join the race in time. Even though some of my competitors were out of shape or quite old, finishing in first place was still not a piece of cake. It required a lot of physical effort.',
        templateEn:
          '{{act_s3_lead}}. Even though some of my competitors were out of shape or quite old, finishing in first place was still not a piece of cake. It required a lot of physical effort.',
        slots: [
          {
            id: 'act_s3_lead',
            labelVi: 'Khe ... Diễn biến cao trào trên đường đua',
            defaultEn: 'Luckily, I was still able to join the race in time',
            hintVi: 'Nhấn vào cảm giác hào hứng, thay đổi sức khỏe, hoặc đạp xe cùng bạn bè',
            examples: [
              { tagVi: 'Thay đổi tích cực', valueEn: 'Luckily, weeks of cycling transformed my stamina when I joined the race' },
              { tagVi: 'Chuyến đi xe đạp', valueEn: 'Luckily, cycling side by side with my close friends along the route felt amazing' },
              { tagVi: 'Dịp đầy phấn khích', valueEn: 'Luckily, I made it to the starting line with my heart pounding with excitement' },
              { tagVi: 'Kế hoạch tương lai', valueEn: 'When I finally join the race next season, I know the ride ahead will be intense' }
            ]
          }
        ],
        textVi:
          '[May mắn là tôi vẫn kịp tham gia cuộc đua / ... diễn biến khớp đề]. Mặc dù một số đối thủ không có thể lực tốt, việc về nhất vẫn không hề dễ dàng chút nào.',
        keywords: ['... [diễn biến]', 'Even though', 'shape', 'piece of cake', 'effort'],
        goldenPhrases: ['Even though', 'out of shape', 'not a piece of cake']
      },
      {
        id: 'act_s4',
        blockId: 'action_experience',
        stageNumber: 4,
        stageTitle: 'Stage 4: Result & Reflection',
        textEn:
          "The competition was followed by a really fun party for everyone, which was especially great for me as the winner! If I hadn't had this experience, I wouldn't have such a beautiful memory today. That was definitely the most enjoyable race I've ever taken part in.",
        templateEn:
          "The competition was followed by a really fun party for everyone, {{act_s4_highlight}}! If I hadn't had this experience, I wouldn't have such a beautiful memory today. That was definitely the most enjoyable race I've ever taken part in.",
        slots: [
          {
            id: 'act_s4_highlight',
            labelVi: 'Khe ... Khoảnh khắc kết màn bám đề',
            defaultEn: 'which was especially great for me as the winner',
            hintVi: 'Khóa chặt đề Mọi người cùng cười, Tiết học tiếng Anh hoặc Sự thay đổi tích cực!',
            examples: [
              { tagVi: 'Mọi người cùng cười', valueEn: 'where literally everybody smiled and burst out laughing at our funny finish-line photos' },
              { tagVi: 'Tiết học tiếng Anh', valueEn: 'and when I finished sharing this story in my English lesson, the whole class applauded' },
              { tagVi: 'Thay đổi tích cực', valueEn: 'marking the exact moment I fell in love with a healthier, more active lifestyle' }
            ]
          }
        ],
        textVi:
          'Sau cuộc thi là bữa tiệc rất vui cho mọi người, [đặc biệt tuyệt vời với người chiến thắng là tôi / ... khoảnh khắc chốt đề]! Nếu không có trải nghiệm này, tôi đã không có kỷ niệm đẹp như hôm nay.',
        keywords: ['followed', 'party', '... [khoảnh khắc chốt đề]', "hadn't had", 'memory'],
        goldenPhrases: ["If I hadn't had this experience, I wouldn't have such a beautiful memory today"]
      }
    ]
  },
  {
    id: 'relation_ceremony',
    code: 'M6',
    type: 'main',
    name: 'The Happy Couple (Relation/Ceremony)',
    titleVi: 'Khối Chính 6: Mối Quan Hệ & Lễ Cưới (Vợ Chồng Chú John)',
    emoji: '💍',
    colorHex: '#db2777',
    badgeBg: 'bg-pink-100',
    badgeText: 'text-pink-800',
    borderClass: 'border-pink-300',
    usedFor: 'Cặp đôi hạnh phúc, đám cưới từng tham dự, bữa tiệc ấm cúng, dành thời gian với trẻ nhỏ, lời hứa...',
    stages: [
      {
        id: 'rel_s1',
        blockId: 'relation_ceremony',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          "I would like to talk about a happy couple that I really admire. It is the story of Mr. John and his lovely wife. As I mentioned before, John is one of my father's best friends.",
        templateEn:
          "I would like to talk about a happy couple that I really admire. It is the story of {{rel_s1_who}}. As I mentioned before, John is one of my father's best friends.",
        slots: [
          {
            id: 'rel_s1_who',
            labelVi: 'Khe ... Nhân vật / Dịp lễ kỷ niệm',
            defaultEn: 'Mr. John and his lovely wife',
            hintVi: 'Xoay mượt sang lễ cưới đã tham dự hoặc buổi chơi đùa cùng cháu nhỏ của chú John',
            examples: [
              { tagVi: 'Đám cưới từng dự', valueEn: 'the heartwarming wedding renewal ceremony of Mr. John and his lovely wife' },
              { tagVi: 'Dành thời gian với trẻ nhỏ', valueEn: 'playing with the adorable five-year-old grandson of Mr. John and his lovely wife' },
              { tagVi: 'Bữa tiệc gia đình', valueEn: 'a joyful family celebration hosted by Mr. John and his lovely wife' }
            ]
          }
        ],
        textVi:
          'Tôi muốn nói về [cặp đôi hạnh phúc chú John và người vợ đáng yêu / ... sự kiện lễ cưới, trẻ nhỏ], bạn thân của bố tôi.',
        keywords: ['talk', 'admire', '... [nhân vật/sự kiện]', 'best friends'],
        goldenPhrases: ['really admire', 'lovely wife']
      },
      {
        id: 'rel_s2',
        blockId: 'relation_ceremony',
        stageNumber: 2,
        stageTitle: 'Stage 2: The Relationship & Event',
        textEn:
          'They tied the knot many years ago. If my memory serves me well, their wedding anniversary is in autumn. They always organize a cozy party at a modern restaurant to celebrate it. The atmosphere is always joyful and full of laughter.',
        templateEn:
          'They tied the knot many years ago. If my memory serves me well, their wedding anniversary is in autumn. {{rel_s2_event}}. The atmosphere is always joyful and full of laughter.',
        slots: [
          {
            id: 'rel_s2_event',
            labelVi: 'Khe ... Khung cảnh buổi lễ / Hoạt động tại tiệc',
            defaultEn: 'They always organize a cozy party at a modern restaurant to celebrate it',
            hintVi: 'Tả cảnh lễ cưới, cảnh trông trẻ nhỏ hoặc mang chiếc bánh đặc biệt ra mừng',
            examples: [
              { tagVi: 'Đám cưới ấm cúng', valueEn: 'My family attended their cozy ceremony at a modern restaurant decorated with fresh white flowers' },
              { tagVi: 'Chơi cùng trẻ nhỏ', valueEn: 'At their cozy autumn party, I spent the whole evening building Lego and playing games with their little grandson' },
              { tagVi: 'Chiếc bánh đặc biệt', valueEn: 'At their cozy restaurant party, we surprised everyone with a handmade celebration cake' }
            ]
          }
        ],
        textVi:
          'Họ kết hôn nhiều năm trước, kỷ niệm ngày cưới vào mùa thu. [Họ luôn tổ chức bữa tiệc ấm cúng tại nhà hàng hiện đại / ... khung cảnh khớp đề] ngập tràn tiếng cười.',
        keywords: ['tied the knot', 'serves', 'anniversary', '... [khung cảnh tiệc]', 'laughter'],
        goldenPhrases: ['tied the knot', 'If my memory serves me well', 'joyful and full of laughter']
      },
      {
        id: 'rel_s3',
        blockId: 'relation_ceremony',
        stageNumber: 3,
        stageTitle: 'Stage 3: Why They Are Happy',
        textEn:
          "I think they are a perfect match because they have a lot in common. Not only do they share household chores, but they also support each other through thick and thin. They always communicate openly and respect each other's opinions.",
        templateEn:
          'I think they are a perfect match because they have a lot in common. Not only do they share household chores, but they also support each other through thick and thin. {{rel_s3_bond}}.',
        slots: [
          {
            id: 'rel_s3_bond',
            labelVi: 'Khe ... Chi tiết gắn kết cảm xúc',
            defaultEn: "They always communicate openly and respect each other's opinions",
            hintVi: 'Nhấn mạnh lời thề trong đám cưới hoặc sự lễ phép đáng yêu của em bé trong gia đình họ',
            examples: [
              { tagVi: 'Đám cưới xúc động', valueEn: 'Watching them exchange heartfelt vows on stage deeply moved every guest in the room' },
              { tagVi: 'Trông trẻ nhỏ', valueEn: 'Seeing how polite, curious, and cheerful their little grandson was showed how lovingly they raised him' }
            ]
          }
        ],
        textVi:
          'Họ là cặp trời sinh vì có nhiều điểm chung, san sẻ việc nhà và sát cánh qua thăng trầm. [Họ luôn giao tiếp cởi mở và tôn trọng nhau / ... chi tiết gắn kết].',
        keywords: ['match', 'common', 'chores', 'thick and thin', '... [gắn kết]'],
        goldenPhrases: ['have a lot in common', 'Not only do they..., but they also...', 'through thick and thin']
      },
      {
        id: 'rel_s4',
        blockId: 'relation_ceremony',
        stageNumber: 4,
        stageTitle: 'Stage 4: Feelings & Influence',
        textEn:
          "To me, they are a true role model for a successful marriage. If it hadn't been for their inspiring story, I wouldn't understand the true meaning of love and patience. I truly hope that I can have a wonderful relationship like theirs in the future.",
        templateEn:
          "To me, they are a true role model for a successful marriage. If it hadn't been for {{rel_s4_impact}}, I wouldn't understand the true meaning of love and patience. I truly hope that I can have a wonderful relationship like theirs in the future.",
        slots: [
          {
            id: 'rel_s4_impact',
            labelVi: 'Khe ... Chốt hạ ĐK loại 3 bám đề',
            defaultEn: 'their inspiring story',
            hintVi: 'Khóa lại bằng đám cưới hoặc buổi chiều chơi với em nhỏ',
            examples: [
              { tagVi: 'Đám cưới đã dự', valueEn: 'attending their heartwarming wedding ceremony' },
              { tagVi: 'Chơi với trẻ nhỏ', valueEn: 'spending that fun evening looking after their little boy' }
            ]
          }
        ],
        textVi:
          'Họ là hình mẫu hôn nhân viên mãn. Nếu không nhờ [câu chuyện truyền cảm hứng của họ / ... dịp đáng nhớ đó], tôi sẽ không hiểu hết ý nghĩa của tình yêu và sự kiên nhẫn.',
        keywords: ['role model', "hadn't been + ...", 'meaning', 'wonderful'],
        goldenPhrases: ["If it hadn't been for", 'true meaning of love and patience']
      }
    ]
  },
  // ======================== 3 PLUGIN BLOCKS ========================
  {
    id: 'food',
    code: 'P1',
    type: 'plugin',
    name: 'Korean BBQ (Plugin: Food)',
    titleVi: 'Plugin 7: Ẩm Thực & Bữa Ăn (Thịt Nướng Hàn Quốc)',
    emoji: '🥩',
    colorHex: '#dc2626',
    badgeBg: 'bg-red-100',
    badgeText: 'text-red-800',
    borderClass: 'border-red-300',
    usedFor: 'Món ăn nước ngoài, chiếc bánh/bữa ăn đặc biệt, hoặc cắm thêm vào tiệc cưới/tiệc ăn mừng/quán ăn dịch vụ tốt!',
    stages: [
      {
        id: 'food_s1',
        blockId: 'food',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          'I would like to talk about a delicious kind of foreign food that I tried recently, which is Korean BBQ.',
        templateEn:
          'I would like to talk about {{food_s1_dish}}.',
        slots: [
          {
            id: 'food_s1_dish',
            labelVi: 'Khe ... Tên món ăn / Chiếc bánh đặc biệt',
            defaultEn: 'a delicious kind of foreign food that I tried recently, which is Korean BBQ',
            hintVi: 'Giữ Korean BBQ hoặc lồng chiếc bánh kem/bánh gạo Hàn Quốc đặc biệt cuối bữa tiệc!',
            examples: [
              { tagVi: 'Chiếc bánh đặc biệt', valueEn: 'a special handmade Korean rice-and-berry cake we shared right after a Korean BBQ dinner' },
              { tagVi: 'Bữa ăn mừng đặc biệt', valueEn: 'an unforgettable Korean BBQ feast I enjoyed with my loved ones' }
            ]
          }
        ],
        textVi:
          'Tôi muốn nói về [món ăn nước ngoài thơm ngon tôi thử gần đây là thịt nướng Hàn Quốc / ... chiếc bánh, bữa ăn đặc biệt].',
        keywords: ['talk', '... [món ăn / chiếc bánh]', 'BBQ'],
        goldenPhrases: ['delicious kind of foreign food']
      },
      {
        id: 'food_s2',
        blockId: 'food',
        stageNumber: 2,
        stageTitle: 'Stage 2: Context',
        textEn:
          'If my memory serves me well, I had it a few months ago. I went to a popular Korean restaurant right in the centre of Hanoi with my family to celebrate the weekend.',
        templateEn:
          'If my memory serves me well, I had it a few months ago. I went to a popular Korean restaurant right in the centre of Hanoi with my family {{food_s2_occasion}}.',
        slots: [
          {
            id: 'food_s2_occasion',
            labelVi: 'Khe ... Lý do / Dịp thưởng thức',
            defaultEn: 'to celebrate the weekend',
            hintVi: 'Gài dịp sinh nhật có bánh kem, ăn mừng tin vui, hoặc trải nghiệm dịch vụ tốt',
            examples: [
              { tagVi: 'Sinh nhật / Bánh đặc biệt', valueEn: "to celebrate my mum's birthday with a surprise cake" },
              { tagVi: 'Ăn mừng tin vui', valueEn: 'to celebrate a wonderful piece of family good news' },
              { tagVi: 'Trải nghiệm dịch vụ', valueEn: 'where the staff gave us warm, five-star table service' }
            ]
          }
        ],
        textVi:
          'Nếu tôi nhớ không lầm, tôi đã thưởng thức vài tháng trước tại nhà hàng Hàn Quốc ngay trung tâm Hà Nội cùng gia đình [dịp cuối tuần / ... dịp ăn mừng khớp đề].',
        keywords: ['serves', 'ago', 'centre', '... [dịp ăn mừng]'],
        goldenPhrases: ['If my memory serves me well', 'right in the centre of Hanoi']
      },
      {
        id: 'food_s3',
        blockId: 'food',
        stageNumber: 3,
        stageTitle: 'Stage 3: Reasons',
        textEn:
          'We decided to eat there because my friends highly recommended this place. They said the meat there was fresh and the sauce was amazing. Also, we wanted to try something different from our daily Vietnamese meals.',
        templateEn:
          'We decided to eat there because my friends highly recommended this place. {{food_s3_feature}}. Also, we wanted to try something different from our daily Vietnamese meals.',
        slots: [
          {
            id: 'food_s3_feature',
            labelVi: 'Khe ... Điểm đặc sắc của món / chiếc bánh',
            defaultEn: 'They said the meat there was fresh and the sauce was amazing',
            hintVi: 'Tả thêm hương vị chiếc bánh đặc biệt hoặc sự chu đáo của nhân viên nhà hàng',
            examples: [
              { tagVi: 'Chiếc bánh đặc biệt', valueEn: 'Besides their fresh BBQ meat, their chef bakes a soft, lightly sweet cake topped with fresh strawberries' },
              { tagVi: 'Phục vụ tận tâm', valueEn: 'Not only was the meat fresh, but the waiters also grilled everything carefully right at our table' }
            ]
          }
        ],
        textVi:
          'Chúng tôi chọn quán vì bạn bè khen nức nở. [Thịt rất tươi và nước sốt tuyệt hảo / ... điểm đặc sắc của bánh, dịch vụ], lại giúp cả nhà đổi vị.',
        keywords: ['decided', 'recommended', '... [điểm đặc sắc]', 'different'],
        goldenPhrases: ['highly recommended', 'try something different']
      },
      {
        id: 'food_s4',
        blockId: 'food',
        stageNumber: 4,
        stageTitle: 'Stage 4: Experience & Conclusion',
        textEn:
          "When I tried it, I was completely blown away. The grilled pork wrapped in fresh green leaves tasted fantastic. It was a wonderful dining experience. If I hadn't gone to that restaurant, I wouldn't have known how delicious Korean food is. I definitely want to eat it again in the future.",
        templateEn:
          "When I tried it, I was completely blown away. {{food_s4_taste}}. It was a wonderful dining experience. If I hadn't gone to that restaurant, I wouldn't have known how delicious Korean food is. I definitely want to eat it again in the future.",
        slots: [
          {
            id: 'food_s4_taste',
            labelVi: 'Khe ... Cảm nhận hương vị đỉnh cao',
            defaultEn: 'The grilled pork wrapped in fresh green leaves tasted fantastic',
            hintVi: 'Nhắc lại miếng bánh mềm tan hoặc thịt nướng cuốn rau để chốt đúng đề',
            examples: [
              { tagVi: 'Chiếc bánh đặc biệt', valueEn: 'Every bite of that warm, fluffy handmade cake after our savory BBQ tasted heavenly' },
              { tagVi: 'Món Hàn chính vị', valueEn: 'The juicy grilled pork wrapped in fresh lettuce leaves tasted fantastic' }
            ]
          }
        ],
        textVi:
          'Khi nếm thử, tôi hoàn toàn choáng ngợp. [Thịt nướng cuốn lá xanh ngon tuyệt / ... cảm nhận vị bánh]. Nếu không đến quán đó, tôi đã không biết ẩm thực Hàn tuyệt đến thế.',
        keywords: ['blown away', '... [hương vị]', "hadn't gone", 'definitely'],
        goldenPhrases: ['completely blown away', "If I hadn't gone to that restaurant"]
      }
    ]
  },
  {
    id: 'plant',
    code: 'P2',
    type: 'plugin',
    name: 'The Bamboo (Plugin: Plant)',
    titleVi: 'Plugin 8: Cây Cối & Biểu Tượng (Cây Tre Việt Nam)',
    emoji: '🎋',
    colorHex: '#16a34a',
    badgeBg: 'bg-green-100',
    badgeText: 'text-green-800',
    borderClass: 'border-green-300',
    usedFor: 'Loài cây quan trọng ở Việt Nam, đồ thủ công địa phương, biểu tượng văn hóa, hoặc cắm thêm vào cảnh miền quê/chùa Bái Đính!',
    stages: [
      {
        id: 'plant_s1',
        blockId: 'plant',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          'I would like to talk about an important plant in my country, which is the bamboo tree. I have known about this plant since I was a little child. We learned about it in school, and you can easily see bamboo trees everywhere in the countryside of Vietnam.',
        templateEn:
          'I would like to talk about an important plant in my country, which is the bamboo tree. I have known about this plant since I was a little child. We learned about it in school, and you can easily see bamboo trees {{plant_s1_where}}.',
        slots: [
          {
            id: 'plant_s1_where',
            labelVi: 'Khe ... Nơi bắt gặp hàng tre',
            defaultEn: 'everywhere in the countryside of Vietnam',
            hintVi: 'Nối mượt vào cảnh đường vào chùa Bái Đính hoặc làng nghề miền quê',
            examples: [
              { tagVi: 'Quanh chùa Bái Đính', valueEn: 'lining the peaceful roads around Bai Dinh temple in the countryside' },
              { tagVi: 'Làng nghề truyền thống', valueEn: 'growing around traditional craft villages across rural Vietnam' }
            ]
          }
        ],
        textVi:
          'Tôi muốn nói về cây tre — loài cây gắn bó từ thuở nhỏ và mọc [khắp làng quê Việt Nam / ... quanh chùa Bái Đính].',
        keywords: ['talk', 'bamboo', 'child', '... [nơi bắt gặp]'],
        goldenPhrases: ['since I was a little child', 'countryside of Vietnam']
      },
      {
        id: 'plant_s2',
        blockId: 'plant',
        stageNumber: 2,
        stageTitle: 'Stage 2: Practical Uses',
        textEn:
          'Bamboo is extremely important for several reasons. Firstly, it is a very useful and practical material. People use it to build houses, make furniture, and even create traditional crafts.',
        templateEn:
          'Bamboo is extremely important for several reasons. Firstly, it is a very useful and practical material. People use it to {{plant_s2_use}}.',
        slots: [
          {
            id: 'plant_s2_use',
            labelVi: 'Khe ... Công dụng thực tế / Đồ thủ công',
            defaultEn: 'build houses, make furniture, and even create traditional crafts',
            hintVi: 'Nhấn mạnh sản phẩm địa phương nếu đề hỏi đồ handmade / truyền thống',
            examples: [
              { tagVi: 'Đồ thủ công địa phương', valueEn: 'weave delicate local baskets, lanterns, and eco-friendly household items' }
            ]
          }
        ],
        textVi:
          'Tre rất quan trọng. Thứ nhất, đây là vật liệu thiết thực để [dựng nhà, đóng nội thất và làm đồ thủ công / ... công dụng khớp đề].',
        keywords: ['Firstly', 'practical', '... [công dụng]'],
        goldenPhrases: ['useful and practical material', 'traditional crafts']
      },
      {
        id: 'plant_s3',
        blockId: 'plant',
        stageNumber: 3,
        stageTitle: 'Stage 3: Symbolic Meaning',
        textEn:
          'Secondly, the bamboo tree is a strong symbol of the Vietnamese people. Because it can survive and grow straight in very difficult conditions, it represents the strength and hard work of our nation.',
        templateEn:
          'Secondly, {{plant_s3_symbol}}. Because it can survive and grow straight in very difficult conditions, it represents the strength and hard work of our nation.',
        slots: [
          {
            id: 'plant_s3_symbol',
            labelVi: 'Khe ... Ý nghĩa biểu tượng',
            defaultEn: 'the bamboo tree is a strong symbol of the Vietnamese people',
            hintVi: 'Khóa chặt các đề hỏi về biểu tượng văn hóa / niềm tự hào dân tộc',
            examples: [
              { tagVi: 'Biểu tượng văn hóa', valueEn: 'bamboo stands as the most iconic cultural symbol of Vietnam' }
            ]
          }
        ],
        textVi:
          'Thứ hai, [cây tre là biểu tượng kiên cường của người Việt / ... ý nghĩa biểu tượng] vì luôn vươn thẳng trong gian khó.',
        keywords: ['Secondly', '... [biểu tượng]', 'survive', 'straight', 'strength'],
        goldenPhrases: ['strong symbol of the Vietnamese people', 'survive and grow straight']
      },
      {
        id: 'plant_s4',
        blockId: 'plant',
        stageNumber: 4,
        stageTitle: 'Stage 4: Feelings & Hopes',
        textEn:
          'I really like and respect this plant. Every time I see a bamboo tree, it reminds me of the traditional values of my country. I hope that bamboo will always be protected and valued by future generations.',
        templateEn:
          'I really like and respect this plant. Every time I see a bamboo tree, it reminds me of {{plant_s4_feeling}}. I hope that bamboo will always be protected and valued by future generations.',
        slots: [
          {
            id: 'plant_s4_feeling',
            labelVi: 'Khe ... Hoài niệm / Cảm xúc gợi nhắc',
            defaultEn: 'the traditional values of my country',
            hintVi: 'Nối lại cảm giác yên bình khi về miền quê hoặc ngắm cảnh chùa',
            examples: [
              { tagVi: 'Chuyến đi miền quê', valueEn: 'that peaceful countryside day away from the noisy city' }
            ]
          }
        ],
        textVi:
          'Tôi rất trân trọng loài cây này. Mỗi khi nhìn thấy tre, tôi lại nhớ về [giá trị truyền thống quê hương / ... cảm xúc khớp đề].',
        keywords: ['respect', 'reminds', '... [hoài niệm]', 'protected'],
        goldenPhrases: ['traditional values of my country', 'protected and valued by future generations']
      }
    ]
  },
  {
    id: 'weather',
    code: 'P3',
    type: 'plugin',
    name: 'Autumn Weather (Plugin: Weather)',
    titleVi: 'Plugin 9: Thời Tiết & Không Khí (Mùa Thu Hà Nội)',
    emoji: '🍂',
    colorHex: '#d97706',
    badgeBg: 'bg-amber-100',
    badgeText: 'text-amber-800',
    borderClass: 'border-amber-300',
    usedFor: 'Thời tiết/mùa yêu thích, hoặc cắm cực mượt vào mọi chuyến đi (Bái Đính, đua xe đạp, tiệc cưới mùa thu, ngắm sao)!',
    stages: [
      {
        id: 'wea_s1',
        blockId: 'weather',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          'I would like to talk about my favourite kind of weather, which is the cool autumn weather in Hanoi. As you may know, autumn here usually starts in September and lasts until November.',
        templateEn:
          'I would like to talk about my favourite kind of weather, which is {{wea_s1_type}}. As you may know, autumn here usually starts in September and lasts until November.',
        slots: [
          {
            id: 'wea_s1_type',
            labelVi: 'Khe ... Kiểu thời tiết / Mùa kết nối',
            defaultEn: 'the cool autumn weather in Hanoi',
            hintVi: 'Đổi nhẹ địa điểm nếu đang ghép Plugin thời tiết cho chuyến đi Ninh Bình / dã ngoại',
            examples: [
              { tagVi: 'Trời thu miền Bắc', valueEn: 'the crisp, cool autumn weather in northern Vietnam' }
            ]
          }
        ],
        textVi:
          'Tôi muốn nói về kiểu thời tiết yêu thích là [tiết trời mùa thu mát mẻ ở Hà Nội / ... thời tiết lúc đó], kéo dài từ tháng 9 đến tháng 11.',
        keywords: ['talk', '... [thời tiết]', 'starts', 'lasts'],
        goldenPhrases: ['cool autumn weather in Hanoi', 'starts in September and lasts until November']
      },
      {
        id: 'wea_s2',
        blockId: 'weather',
        stageNumber: 2,
        stageTitle: 'Stage 2: Characteristics',
        textEn:
          'In this kind of weather, the temperature is just perfect—not too hot and not too cold. There is usually a gentle breeze and clear blue skies.',
        templateEn:
          'In this kind of weather, the temperature is just perfect—not too hot and not too cold. There is usually {{wea_s2_sky}}.',
        slots: [
          {
            id: 'wea_s2_sky',
            labelVi: 'Khe ... Bầu trời & Không khí',
            defaultEn: 'a gentle breeze and clear blue skies',
            hintVi: 'Cực hợp để bẻ sang bầu trời đêm đầy sao (Đề #55) hoặc nắng thu đạp xe!',
            examples: [
              { tagVi: 'Đêm đầy sao 🚀', valueEn: 'a cool evening breeze and crystal-clear skies sparkling with stars' },
              { tagVi: 'Dã ngoại / Đạp xe', valueEn: 'a refreshing breeze and golden sunshine ideal for outdoor trips' }
            ]
          }
        ],
        textVi:
          'Trong tiết trời này, nhiệt độ rất lý tưởng — không quá nóng hay lạnh, thường có [gió heo may và bầu trời trong xanh / ... khung cảnh bầu trời].',
        keywords: ['perfect', '... [bầu trời & gió]'],
        goldenPhrases: ['gentle breeze and clear blue skies']
      },
      {
        id: 'wea_s3',
        blockId: 'weather',
        stageNumber: 3,
        stageTitle: 'Stage 3: Activities',
        textEn:
          'Whenever the weather is like this, I love to go for a walk around the lake or sit at a coffee shop with my friends to chat and relax. It is a great time to escape the terrible heat of the summer and the freezing cold of the winter.',
        templateEn:
          'Whenever the weather is like this, I love to {{wea_s3_do}}. It is a great time to escape the terrible heat of the summer and the freezing cold of the winter.',
        slots: [
          {
            id: 'wea_s3_do',
            labelVi: 'Khe ... Hoạt động dưới tiết trời thu',
            defaultEn: 'go for a walk around the lake or sit at a coffee shop with my friends to chat and relax',
            hintVi: 'Gắn hoạt động dạo hồ, chụp ảnh, đạp xe hoặc ngắm sao cùng bạn bè',
            examples: [
              { tagVi: 'Đạp xe / Du ngoạn', valueEn: 'cycle along scenic roads and walk around the quiet lake with my friends' },
              { tagVi: 'Ngắm sao đêm 🚀', valueEn: 'sit outdoors by the peaceful lake with my friends and gaze up at the stars' }
            ]
          }
        ],
        textVi:
          'Mỗi khi trời thu về, tôi thích [đi dạo quanh hồ hoặc ngồi cà phê trò chuyện cùng bạn bè / ... hoạt động ngoài trời], thoát khỏi cái nắng hè và lạnh đông.',
        keywords: ['... [hoạt động]', 'escape', 'heat', 'freezing cold'],
        goldenPhrases: ['escape the terrible heat of the summer', 'freezing cold of the winter']
      },
      {
        id: 'wea_s4',
        blockId: 'weather',
        stageNumber: 4,
        stageTitle: 'Stage 4: Influence',
        textEn:
          "This weather brings a lot of positive influences to my life. If it weren't for this beautiful weather, I wouldn't have so much energy to work and study. It always puts me in a good mood and helps me stay productive all day.",
        templateEn:
          "This weather brings a lot of positive influences to my life. If it weren't for this beautiful weather, I wouldn't {{wea_s4_effect}}. It always puts me in a good mood and helps me stay productive all day.",
        slots: [
          {
            id: 'wea_s4_effect',
            labelVi: 'Khe ... Tác động của thời tiết tới trải nghiệm',
            defaultEn: 'have so much energy to work and study',
            hintVi: 'Nếu dùng làm Plugin cho chuyến đi/tiệc cưới, nối thẳng vào niềm vui của buổi hôm đó!',
            examples: [
              { tagVi: 'Ghép vào Chuyến đi / Sự kiện', valueEn: 'have enjoyed that unforgettable outdoor trip half as much as I did' }
            ]
          }
        ],
        textVi:
          'Thời tiết này mang lại nhiều ảnh hưởng tích cực. Nếu không có tiết trời đẹp ấy, tôi sẽ không [có nhiều năng lượng học tập, làm việc / ... tận hưởng trọn vẹn dịp đó].',
        keywords: ['positive influences', "weren't for", '... [tác động]', 'mood', 'productive'],
        goldenPhrases: ["If it weren't for this beautiful weather", 'puts me in a good mood', 'stay productive all day']
      }
    ]
  }
];

export const SPK2_HOOK_FORMULAS: Spk2HookFormula[] = [
  {
    id: 'direct_pivot',
    name: '1. Hook Trực Diện & Bẻ Lái Mượt',
    tagVi: 'Dễ dùng nhất cho 70% đề',
    templateEn:
      'Well, when it comes to [chủ đề đề bài], the very first [person / place / thing / experience] that springs to my mind is [tên Khối Lego], mainly because [lý do gắn với đề].',
    guideVi: 'Nhắc thẳng từ khóa đề bài ở vế đầu để ăn điểm Task Relevance, rồi dùng "springs to my mind" lái mượt về Khối Lego.'
  },
  {
    id: 'memory_occasion',
    name: '2. Hook Kỷ Niệm / Tình Huống',
    tagVi: 'Chuyên trị đề "Describe a time / occasion..."',
    templateEn:
      'Honestly, off the top of my head, a memorable occasion when [sự việc đề bài hỏi] happened during [bối cảnh Khối Lego], and let me tell you the whole story.',
    guideVi: 'Biến đề bài thành bối cảnh xảy ra ngay trong sự kiện Đua xe đạp, Tiệc cưới chú John, hoặc Chuyến đi Bái Đính.'
  },
  {
    id: 'wrapper_media',
    name: '3. Hook "Lớp Vỏ Bọc" (Phim / Sách / Tranh / Vũ Trụ)',
    tagVi: 'Tuyệt chiêu trị đề khó & trừu tượng 🚀',
    templateEn:
      "To tell you the truth, I don't know too much technical detail about [chủ đề khó], but I was deeply impressed by a [movie / book / artwork / space station] related to it, which centered around [nhân vật/không gian Khối Lego].",
    guideVi: 'Đúng chuẩn chiến thuật của thầy Tony: Bọc đề khó (vũ trụ, tranh vẽ, phim, sách, bài giảng) bên ngoài rồi kể ruột Khối Lego kèm các khe "..." bám đề!'
  },
  {
    id: 'future_dream',
    name: '4. Hook Kế Hoạch & Ước Mơ Tương Lai',
    tagVi: 'Chuyên trị đề "Plan / Future / Dream job"',
    templateEn:
      "Actually, speaking of [kế hoạch / mục tiêu tương lai], one big goal that I haven't ticked off my bucket list yet revolves around [Khối Lego], so I'd love to share my plan for it.",
    guideVi: 'Dùng cho các đề hỏi dự định chưa làm, chuyến đi sắp tới hoặc công việc lương cao (để mua Modern Flat / đi Bái Đính / đua xe).'
  },
  {
    id: 'gift_news_service',
    name: '5. Hook Tin Vui / Quà Tặng / Dịch Vụ',
    tagVi: 'Chuyên trị đề "Good news / Free gift / Service"',
    templateEn:
      'If I had to pick one unforgettable moment regarding [tin vui / món quà / dịch vụ], it would definitely be connected to [Khối Lego], which left a lasting impression on me.',
    guideVi: 'Nối các đề nhận quà miễn phí, nghe tin vui, hoặc trải nghiệm dịch vụ tốt thẳng vào Xe đạp, Căn hộ/Quán cafe hiện đại hoặc Korean BBQ.'
  }
];

export const SPK2_CONNECTOR_BRIDGES: Spk2ConnectorBridge[] = [
  {
    id: 'bridge_weather',
    targetBlockId: 'weather',
    labelVi: 'Khớp nối sang Plugin Thời tiết (Autumn Weather)',
    bridgeEn: 'What made this whole experience even more unforgettable was the weather at that time.'
  },
  {
    id: 'bridge_food',
    targetBlockId: 'food',
    labelVi: 'Khớp nối sang Plugin Ẩm thực (Korean BBQ)',
    bridgeEn: 'On top of that, to make the occasion truly special, we also enjoyed an amazing meal together.'
  },
  {
    id: 'bridge_plant',
    targetBlockId: 'plant',
    labelVi: 'Khớp nối sang Plugin Cây tre (The Bamboo)',
    bridgeEn: 'Another fascinating detail I noticed around that place was the lush greenery, especially the bamboo trees.'
  },
  {
    id: 'bridge_place',
    targetBlockId: 'place_service',
    labelVi: 'Khớp nối sang Không gian hiện đại (Modern Flat)',
    bridgeEn: 'Let me also describe the setting itself, because the space was genuinely impressive.'
  },
  {
    id: 'bridge_hist',
    targetBlockId: 'historical_nature',
    labelVi: 'Khớp nối sang Không gian yên bình (Bai Dinh Temple)',
    bridgeEn: 'Speaking of the location, the surrounding scenery also played a huge part in why I loved it so much.'
  },
  {
    id: 'bridge_person',
    targetBlockId: 'person',
    labelVi: 'Khớp nối sang Nhân vật truyền cảm hứng (Mr. John)',
    bridgeEn: 'More importantly, the person who shared that memory and inspired me the most was Mr. John.'
  },
  {
    id: 'bridge_general',
    targetBlockId: 'any',
    labelVi: 'Khớp nối đa năng giữa 2 khối bất kỳ',
    bridgeEn: 'Besides that, another memorable part of the story that I have to mention is what happened next.'
  }
];

export const SPK2_PROMPTS_55: Spk2PromptItem[] = [
  {
    num: 1,
    title: 'Describe an invention changed the people’s life.',
    cueBullets: ['What it is', 'Who invent it', 'When it was invented', 'And explain how it changed people’s life.'],
    recommendedBlockId: 'object_entity',
    recommendedPluginIds: [],
    isDirectMatch: true,
    slotSuggestions: {
      obj_s1_origin: 'Ever since then, this invention has transformed daily transport for millions of people, including me',
      obj_s4_anchor: 'this brilliant invention'
    },
    hookLogicVi: 'Khớp trực diện 100% với khối The Bicycle (phát minh năm 1817 bởi giáo sư người Đức, thay đổi việc đi lại & sức khỏe).',
    sampleHookEn: 'Well, when it comes to a life-changing invention, the very first thing that springs to my mind is the bicycle.',
    sampleClosingEn: 'All in all, that is why I firmly believe the bicycle is one of the greatest inventions that ever transformed human life.'
  },
  {
    num: 2,
    title: 'Describe an occasion that you have a cake that is special',
    cueBullets: ['What kind of cake it is', 'When you ate the cake', 'Who you ate with', 'And explain why you think the cake is special'],
    recommendedBlockId: 'food',
    recommendedPluginIds: ['relation_ceremony'],
    slotSuggestions: {
      food_s1_dish: 'a special handmade Korean rice-and-strawberry birthday cake we shared right after a Korean BBQ dinner',
      food_s2_occasion: "to celebrate my mother's birthday with a surprise cake",
      food_s3_feature: 'Besides their fresh BBQ meat, their pastry chef makes a soft, lightly sweet cake topped with fresh berries',
      food_s4_taste: 'Sharing slices of that warm, fluffy handmade cake right after our savory BBQ tasted fantastic',
      rel_s2_event: 'At that cozy restaurant party, everyone clapped as we lit the candles on the special cake'
    },
    hookLogicVi: 'Dùng vỏ bọc sinh nhật/kỷ niệm tại nhà hàng Hàn Quốc (Korean BBQ), điền khe "..." gài chiếc bánh gạo/kem tươi đặc biệt mang ra cuối bữa!',
    sampleHookEn: 'Honestly, a memorable occasion when I had a truly special cake was during a family celebration at a Korean BBQ restaurant, where we ended our meal with a handmade Korean rice-and-berry cake.',
    sampleClosingEn: 'Having that special cake right after our wonderful Korean BBQ dinner made the whole evening unforgettable for me.'
  },
  {
    num: 3,
    title: 'Describe a couple you know who have a happy marriage',
    cueBullets: ['Who they are', 'How you knew them', 'What they usually do together', 'And explain how you feel about their marriage'],
    recommendedBlockId: 'relation_ceremony',
    recommendedPluginIds: ['person'],
    isDirectMatch: true,
    hookLogicVi: 'Khớp trực diện 100% với khối The Happy Couple (vợ chồng chú John — bạn thân của bố). Có thể cắm thêm 1 Stage từ Mr. John nếu muốn!',
    sampleHookEn: 'Well, speaking of a couple with a truly happy marriage, I would love to tell you about Mr. John and his lovely wife.',
    sampleClosingEn: 'All in all, their enduring marriage has always been the ultimate relationship goal that I look up to.'
  },
  {
    num: 4,
    title: 'Describe TV series you like',
    cueBullets: ['What the TV series are', 'Who act these serie', 'What is the plot', 'And explain how you feel about it'],
    recommendedBlockId: 'object_entity',
    recommendedPluginIds: ['action_experience'],
    slotSuggestions: {
      obj_s1_origin: 'That fascinating 1817 origin story was actually the first episode of the series, hosted by a passionate cyclist',
      obj_s2_core: 'every episode of the show vividly demonstrates why the bicycle is such a practical means of transport',
      obj_s3_concession: 'the series has a simple documentary plot without flashy special effects',
      obj_s4_anchor: 'watching that inspiring TV series',
      act_s2_twist: 'Inspired by my favourite episode about an amateur charity race, I even trained for two weeks to try cycling myself'
    },
    hookLogicVi: 'Dùng Hook "Lớp Vỏ Bọc" + gài khe "..." nhắc lại các tập phim (episodes/plot) xuyên suốt khối The Bicycle để không bị lệch sang tả xe cá nhân!',
    sampleHookEn: 'To be honest, my all-time favourite TV series is an inspiring documentary show called "Two Wheels of Life", which explores how the humble bicycle changed the world and even inspired me to ride.',
    sampleClosingEn: 'Watching every episode of that TV series made me fall in love with cycling and live a much healthier lifestyle.'
  },
  {
    num: 5,
    title: 'Describe a work of art that you saw before',
    cueBullets: ['When you first saw this work of art', 'Where you saw it', 'What it looked like', 'And explain your feelings about it.'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: ['weather'],
    slotSuggestions: {
      place_s1_setting: 'The stylish apartment where I first saw that painting is located right in the centre of Hoan Kiem district, Hanoi',
      place_s2_feature: 'sunlit windows illuminating that colourful oil painting of old Hanoi autumn streets right above the sofa',
      place_s3_activity: 'Standing in that living room, every guest pauses to admire the warm golden brushstrokes and peaceful vibe of the artwork.',
      place_s4_future: 'if I am successful one day, I would love to buy an oil painting just like that for my own living room',
      wea_s2_sky: 'a gentle autumn breeze and golden sunlight captured right inside the painting'
    },
    hookLogicVi: 'Bẻ lái từ bức tranh sơn dầu phố cổ Hà Nội treo trong căn hộ Hoàn Kiếm (A Modern Flat) + điền khe "..." giữ hình ảnh bức tranh ở cả 4 Stage!',
    sampleHookEn: 'Well, a stunning work of art that left a deep impression on me was a colourful oil painting of Hanoi, which I first saw hanging inside a gorgeous modern apartment in Hoan Kiem district.',
    sampleClosingEn: 'That artwork blended so harmoniously with the modern interior that I still picture it clearly whenever I think of great art.'
  },
  {
    num: 6,
    title: 'Describe a plan you haven’t done yet',
    cueBullets: ['What is about', 'When you plan to do it', 'Why do you want to do it', 'And explain why you haven’t done it'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['object_entity'],
    slotSuggestions: {
      act_s1_when: 'it is an annual charity race held every autumn that I plan to join right after my IELTS exam',
      act_s2_twist: 'Because my study schedule has been packed all year, I have not had two full weeks to train for it yet',
      act_s3_lead: 'Once I finally line up at the starting line next season, I know it will be thrilling',
      act_s4_highlight: 'which I am sure will be an unforgettable celebration once I cross the finish line',
      obj_s4_anchor: 'setting this cycling goal'
    },
    hookLogicVi: 'Bẻ lái sang kế hoạch đăng ký giải đua xe từ thiện "Race for Life" mùa tới + đổi các khe "..." sang thì tương lai/chưa thực hiện vì bận thi!',
    sampleHookEn: "Actually, one exciting personal plan I haven't been able to carry out yet because of my busy exam schedule is competing in a charity cycling tournament called 'Race for Life'.",
    sampleClosingEn: 'As soon as I finish my IELTS exam this year, training properly to fulfil this plan will be at the very top of my list.'
  },
  {
    num: 7,
    title: 'Describe an English lesson you have taken',
    cueBullets: ['When it was', 'What it was about', 'What happened', 'And explain why you liked it'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['person'],
    slotSuggestions: {
      act_s1_when: 'this was the exact real-life story I shared in English in front of my class during that lesson',
      act_s2_twist: 'While telling the class how I was 15 minutes late due to a traffic jam, my teacher taught me great idioms',
      act_s3_lead: 'Speaking fluently without notes, I explained how I joined the race just in time',
      act_s4_highlight: 'and when I finished telling this story in English, my teacher and classmates applauded warmly',
      person_s2_trait: 'an encouraging and gentle English teacher who reminded me of my mentor'
    },
    hookLogicVi: 'Lớp vỏ bọc buổi học Speaking kể chuyện thử thách đáng nhớ — gài khe "..." nhắc tới thầy giáo & cả lớp vỗ tay để bám chặt đề English lesson!',
    sampleHookEn: 'One of the most memorable English lessons I have ever taken was a lively speaking workshop last semester, where our teacher asked each of us to tell a real-life story—and I shared a cycling race I won.',
    sampleClosingEn: 'Being able to tell that exciting personal story fluently in front of everyone made that English lesson truly unforgettable.'
  },
  {
    num: 8,
    title: 'Describe one of your favorite clothing.',
    cueBullets: ['What is it looks like', 'How did you get it', 'Do you often dress it', 'And explain why it is your favorite clothing'],
    recommendedBlockId: 'object_entity',
    recommendedPluginIds: ['action_experience'],
    slotSuggestions: {
      obj_s1_origin: 'My parents gave me that sporty, breathable blue cycling jersey right along with my first bike as a Tet gift',
      obj_s2_core: 'wearing my favourite jersey makes riding this practical means of transport super comfortable every morning',
      obj_s3_concession: 'this cycling shirt is simple and not from an expensive luxury brand',
      obj_s4_anchor: 'this comfortable cycling jersey and my bike'
    },
    hookLogicVi: 'Bẻ lái từ chiếc áo thể thao đạp xe (cycling jersey) bố mẹ tặng kèm xe đạp dịp Tết + gài chiếc áo vào cả 4 khe "..." của khối The Bicycle!',
    sampleHookEn: 'Well, my absolute favourite piece of clothing is a bright blue breathable cycling jersey, which my parents gave me right along with my very first bicycle.',
    sampleClosingEn: 'Every time I put on that jersey and hop on my bike, I feel energetic, comfortable, and ready for the day.'
  },
  {
    num: 9,
    title: 'Describe a time when you received something free',
    cueBullets: ['What it was', 'When and where you got it', 'Why you got it', 'And explain how you felt about it'],
    recommendedBlockId: 'object_entity',
    recommendedPluginIds: [],
    slotSuggestions: {
      obj_s1_origin: 'I actually won my first bicycle completely for free in a lucky draw at my high school festival',
      obj_s3_concession: 'I got this bike for free without paying a single penny',
      obj_s4_anchor: 'winning that free bike'
    },
    hookLogicVi: 'Bẻ lái cực khớp vào chiếc xe đạp trúng thưởng hoàn toàn miễn phí ở trường + khóa chữ "for free" ngay tại khe "..." Stage 1, 3, 4!',
    sampleHookEn: 'Honestly, the best time I ever received something completely free was when I won a brand-new bicycle at no cost at all in a school lucky draw.',
    sampleClosingEn: 'Even though I did not have to pay a single penny for it, that free bicycle turned out to be the most valuable item I own.'
  },
  {
    num: 10,
    title: 'Describe a time you need to arrive early',
    cueBullets: ['When it was', 'What time you arrived', 'Why you need to arrive early', 'How you felt'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: [],
    slotSuggestions: {
      act_s2_twist: 'All riders were required to arrive by 6:30 a.m. to check in early, so hitting a traffic jam made me panic',
      act_s3_lead: 'Luckily, because I had left home early enough, I still checked in right before the whistle'
    },
    hookLogicVi: 'Khớp trực tiếp với Bicycle Racing: Ban tổ chức yêu cầu đến sớm 6:30 sáng điểm danh — gài khe "..." Stage 2 & 3 làm rõ lý do cần đến sớm!',
    sampleHookEn: 'Well, an unforgettable occasion when I really needed to arrive early was on the morning of a charity bicycle race called "Race for Life", where participants had to check in before 6:30 a.m.',
    sampleClosingEn: 'That nerve-racking morning taught me a lifelong lesson to always leave home extra early whenever I have an important event.'
  },
  {
    num: 11,
    title: 'Describe an occasion where everybody smiled/laughed.',
    cueBullets: ['What happened', 'When it happened', 'Who were there', 'And explain why everyone smiled/laughed.'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['relation_ceremony'],
    slotSuggestions: {
      act_s3_lead: 'Luckily, I joined in time, and the crowd started laughing cheerfully at our funny team helmets',
      act_s4_highlight: 'where literally everybody smiled and burst out laughing at our muddy victory photos',
      rel_s2_event: 'Even Mr. John and his wife joined our victory party and told hilarious jokes'
    },
    hookLogicVi: 'Kết hợp giải đua "Race for Life" với bữa tiệc mừng chiến thắng ngập tràn tiếng cười qua khe "..." ở Stage 3 & Stage 4!',
    sampleHookEn: 'Off the top of my head, a wonderful occasion where literally everybody was smiling and laughing non-stop was the celebration party right after a charity cycling race I joined.',
    sampleClosingEn: 'Seeing every single participant burst into laughter together at the finish-line party still puts a big smile on my face today.'
  },
  {
    num: 12,
    title: 'Describe a favorite sports you watched / a sport you like to watch.',
    cueBullets: ['What it is', 'When you watched it', 'How you watch it', 'And explain why you like watching it'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['object_entity'],
    slotSuggestions: {
      act_s1_when: 'watching thrilling Tour de France broadcasts on TV inspired me to watch and join a live local race two years ago',
      act_s2_twist: 'Standing near the roadside before my amateur heat, I watched the pro cyclists sprint past at breathtaking speed',
      act_s3_lead: 'Watching their teamwork up close—and then riding the course myself—was thrilling'
    },
    hookLogicVi: 'Bẻ lái từ đam mê xem đua xe đạp trên TV sang trải nghiệm trực tiếp xem & đấu giải phong trào "Race for Life" nhờ khe "..."!',
    sampleHookEn: 'Actually, the sport I enjoy watching the most is road bicycle racing, and watching it on TV even inspired me to experience a local race in person.',
    sampleClosingEn: 'Whether I am watching professional cyclists on screen or cheering at a local race, cycling never fails to thrill me.'
  },
  {
    num: 13,
    title: 'Describe a place where you feel crowded',
    cueBullets: ['Where it is', 'When do you usually go there', 'What you do there', 'And explain why it is crowded'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather'],
    slotSuggestions: {
      hist_s1_intro: 'a famous spiritual complex in Ninh Binh province that gets packed with pilgrims every spring',
      hist_s2_detail: 'attracting tens of thousands of bustling visitors praying for luck during Lunar New Year',
      hist_s3_action: 'Once I walk past the crowded main gate towards the back lake, I can still enjoy the beautiful view'
    },
    hookLogicVi: 'Khớp ngay Stage 4 của Bai Dinh Temple ("Although there are usually many tourists...") + nhấn thêm đám đông lễ hội đầu xuân ở khe "..." Stage 1–3!',
    sampleHookEn: 'Well, a place that often gets packed with thousands of visitors—especially during spring festival season—is Bai Dinh temple, though I still love going there.',
    sampleClosingEn: 'So despite the huge crowds of pilgrims and tourists at the entrance, Bai Dinh remains a place I willingly return to.'
  },
  {
    num: 14,
    title: 'Describe an interesting conversation you had with a stranger',
    cueBullets: ['Who the person is', 'What you talked about', 'What kind of person he/she is', 'Why the conversation was interesting'],
    recommendedBlockId: 'person',
    recommendedPluginIds: ['weather'],
    slotSuggestions: {
      person_s1_anchor: 'who was a complete stranger chatting with me by the basketball court before we realized he knew my dad',
      person_s2_trait: 'a warm, humorous conversationalist who spoke to a kid like an equal',
      person_s3_memory: 'pretended to lose at basketball while telling me fascinating stories about perseverance',
      person_s4_lesson: 'how a single friendly conversation can open your mind and teach you patience'
    },
    hookLogicVi: 'Bẻ lái về cuộc trò chuyện đầu tiên với chú John khi chú còn là người lạ ở sân bóng rổ — gài khe "..." giữ mạch "conversation" xuyên suốt!',
    sampleHookEn: 'Honestly, the most memorable conversation I ever had with a complete stranger happened when I was a kid playing alone, before I found out that this kind stranger—Mr. John—actually knew my dad.',
    sampleClosingEn: 'That chance conversation with a stranger turned into one of the most meaningful mentorships of my entire childhood.'
  },
  {
    num: 15,
    title: 'Describe a helpful person in work or study',
    cueBullets: ['Who it was', 'What this person did', 'How this person helped', 'And explain how you felt after this person helped you'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    slotSuggestions: {
      person_s2_trait: 'an incredibly helpful and patient mentor whenever I struggled with schoolwork',
      person_s3_memory: 'pretended to lose at basketball to relax me before patiently helping me solve tough homework',
      person_s4_lesson: 'to stay patient and disciplined in my studies'
    },
    hookLogicVi: 'Khớp trực diện với khối Mr. John + điền nhẹ khe "..." Stage 2–4 nhấn vào việc chú kèm cặp bài vở khi bố mẹ bận!',
    sampleHookEn: 'When it comes to someone who helped me tremendously in my studies and personal growth, I immediately think of Mr. John.',
    sampleClosingEn: 'Thanks to his patient guidance in both my schoolwork and life, I became much more confident and disciplined.'
  },
  {
    num: 16,
    title: 'Describe a piece of good news that you received',
    cueBullets: ['What this news was', 'When and where you heard it', 'How you heard it', 'And explain why you think it was good news'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: ['food'],
    slotSuggestions: {
      place_s1_setting: 'The news was that my older brother had finally bought a modern flat in Hoan Kiem district, right in the centre of Hanoi',
      place_s3_activity: 'When he invited our family over to celebrate the good news, we cooked a big meal in the modern kitchen and relaxed in the living room.',
      place_s4_future: 'hearing such wonderful news inspired me to work hard so I can buy a dream home like his one day',
      food_s2_occasion: 'right after hearing that exciting family news'
    },
    hookLogicVi: 'Dùng Hook Tin vui (anh trai/gia đình báo tin mua được căn hộ mới ở Hoàn Kiếm) + gài "good news" vào khe "..." Stage 1, 3, 4!',
    sampleHookEn: 'One wonderful piece of good news that thrilled my whole family recently was a phone call from my older brother telling us he had just bought a brand-new apartment in the heart of Hanoi.',
    sampleClosingEn: 'Hearing that fantastic news gave me huge motivation to work hard so I can achieve a milestone like that myself.'
  },
  {
    num: 17,
    title: 'Describe an important plant in your country.',
    cueBullets: ['What the plant is', 'How you know it', 'Why it is important', 'And explain how much you like the plant.'],
    recommendedBlockId: 'plant',
    recommendedPluginIds: ['historical_nature'],
    isDirectMatch: true,
    hookLogicVi: 'Khớp trực diện 100% với Plugin Block 8: The Bamboo (Cây tre Việt Nam)! Cắm thêm 1–2 Stage Bái Đính để tròn 2 phút.',
    sampleHookEn: 'I would love to talk about an iconic plant that holds a special place in Vietnamese life and culture, which is the bamboo tree.',
    sampleClosingEn: 'In short, bamboo is far more than just a plant in Vietnam—it is the living spirit of our homeland.'
  },
  {
    num: 18,
    title: 'Describe a city that you have visited.',
    cueBullets: ['Where the city is (and its name)', 'When you went there', 'What you liked / disliked about the city', 'And explain why you visited this city.'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: ['weather', 'food'],
    slotSuggestions: {
      place_s1_setting: 'During my visit to Hanoi, I stayed in a modern flat in Hoan Kiem district, right in the lively heart of the city',
      place_s2_feature: 'lots of windows overlooking Hanoi’s tree-lined boulevards and bustling streets',
      place_s4_future: 'even though central Hanoi can get a bit crowded at rush hour, I would love to live in this vibrant city one day'
    },
    hookLogicVi: 'Ghép Lego kinh điển: Chuyến thăm Hà Nội vào mùa thu (Autumn Weather), lưu trú căn hộ view phố Hoàn Kiếm (Modern Flat) + gài ưu/nhược điểm thành phố vào khe "..."!',
    sampleHookEn: 'Well, a vibrant city I visited and fell in love with is Hanoi, especially the central Hoan Kiem area where I stayed in an amazing modern flat.',
    sampleClosingEn: 'Between the modern city vibe, the food, and the autumn breeze, visiting Hanoi was an experience I will never forget.'
  },
  {
    num: 19,
    title: 'Describe a time when you moved to a new house or a new school',
    cueBullets: ['When it happened', 'What kind of home did you moved into', 'Why you moved', 'And explain how you felt about the moving'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: [],
    slotSuggestions: {
      place_s1_setting: 'Last year, my family moved into this modern flat in Hoan Kiem district to be closer to my school and my parents’ office',
      place_s4_future: 'moving into this bright apartment made our daily commute much shorter and brought our family closer together'
    },
    hookLogicVi: 'Đổi khe "..." Stage 1 & Stage 4 của A Modern Flat từ "mơ ước mua" sang "kỷ niệm gia đình chuyển về căn hộ mới ở Hoàn Kiếm" — khớp 100%!',
    sampleHookEn: 'A major milestone I remember vividly was the time my family moved into a brand-new modern apartment right in the centre of Hanoi.',
    sampleClosingEn: 'Moving into that bright, modern flat brought our whole family closer together and made daily life so much more convenient.'
  },
  {
    num: 20,
    title: 'Describe a leisure activity near or on the sea',
    cueBullets: ['What it is', 'Who do you play with', 'Why you have to prepare', 'And explain how you feel about it'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather'],
    slotSuggestions: {
      hist_s1_intro: 'a scenic coastal-estuary and spiritual area in Ninh Binh province where waterways meet the sea breeze',
      hist_s3_action: 'After packing life jackets, hats, and sunscreen with my friends, we love kayaking and boating on the calm water',
      hist_s4_impact: 'that refreshing boating trip on the water'
    },
    hookLogicVi: 'Bẻ lái sang chèo thuyền / kayak thư giãn vùng cửa biển - sông nước Ninh Bình gần Bái Đính + gài khâu chuẩn bị áo phao, kem chống nắng vào khe "..." Stage 3!',
    sampleHookEn: 'Whenever I think of a relaxing leisure activity on the water near the coast, I immediately picture kayaking with my friends along the scenic coastal waterway in Ninh Binh.',
    sampleClosingEn: 'Prepared with just a life vest, sunscreen, and a camera, spending a breezy day on the water always recharges my batteries.'
  },
  {
    num: 21,
    title: 'Describe a positive change in your life',
    cueBullets: ['What the change was', 'When it happened', 'How it happened', 'And explain why it was a positive change'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['object_entity'],
    slotSuggestions: {
      act_s2_twist: 'Before signing up, I used to be quite lazy, so waking up early to train for two weeks was a huge turning point',
      act_s3_lead: 'Luckily, daily cycling transformed my energy and endurance during the race',
      act_s4_highlight: 'marking the moment I permanently adopted an active, healthy lifestyle'
    },
    hookLogicVi: 'Ghép đôi Bicycle Racing + The Bicycle, dùng khe "..." nhấn sự lột xác từ người lười vận động thành người khỏe khoắn năng động!',
    sampleHookEn: 'Hands down, one of the biggest positive changes in my life was taking up daily cycling and pushing myself to compete in a charity bicycle race.',
    sampleClosingEn: 'That single decision transformed both my physical stamina and my mindset in the most positive way imaginable.'
  },
  {
    num: 22,
    title: 'Describe an organization or company where you live and they employs a lot of people.',
    cueBullets: ['What it is', 'How many employees work there', 'What its work', 'And explain what you think about it.'],
    recommendedBlockId: 'object_entity',
    recommendedPluginIds: [],
    slotSuggestions: {
      obj_s1_origin: 'Here in Hanoi, Thong Nhat Bicycle Company employs over two thousand local engineers and factory workers to build durable bikes',
      obj_s2_core: 'the bicycles manufactured by this company are an extremely practical means of transport',
      obj_s3_concession: 'their locally made bikes are very affordable compared to foreign brands',
      obj_s4_anchor: 'large local employers like Thong Nhat Company'
    },
    hookLogicVi: 'Bẻ lái về Công ty Xe đạp Thống Nhất tạo việc làm cho hàng nghìn lao động tại Hà Nội + khóa tên công ty vào cả 4 khe "..." của The Bicycle!',
    sampleHookEn: 'Well, a well-known local company in my city that employs thousands of workers is Thong Nhat, a long-standing Vietnamese manufacturer famous for producing bicycles.',
    sampleClosingEn: 'By creating stable local jobs while promoting green transport, this bicycle company makes a real contribution to our community.'
  },
  {
    num: 23,
    title: 'Describe a happy event from your childhood that you remember well.',
    cueBullets: ['What the event was', 'When and where it happened', 'What you saw or did', 'And explain why you remember this event so well'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['person'],
    slotSuggestions: {
      act_s1_when: 'it was a junior race held when I was ten years old in primary school',
      act_s2_twist: 'Even though my dad and I were 15 minutes late due to a traffic jam, I was still bursting with childhood excitement',
      act_s4_highlight: 'where all the kids got medals and ice cream, especially me as the winner'
    },
    hookLogicVi: 'Đổi khe "..." Stage 1, 2, 4 của giải đua "Race for Life" về năm 10 tuổi cấp 1 — khớp hoàn hảo kỷ niệm tuổi thơ!',
    sampleHookEn: 'Looking back at my childhood, one joyful event that stands out vividly in my mind is a junior charity bicycle race I entered and won when I was ten.',
    sampleClosingEn: 'Even after all these years, the thrill of winning that childhood race and celebrating with everyone remains crystal clear.'
  },
  {
    num: 24,
    title: 'Describe a person who solved a problem in a clever way',
    cueBullets: ['Who the person is', 'When you meet the person', 'Where do you', 'And explain why do you think the person is clever'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    slotSuggestions: {
      person_s2_trait: 'a very clever and insightful man who knew how to solve emotional problems gently',
      person_s3_memory: 'pretended to lose and let me win, which was his clever psychological trick to cure my childhood shyness',
      person_s4_lesson: 'to solve difficult problems with empathy and creativity rather than pressure'
    },
    hookLogicVi: 'Dùng khối Mr. John + điền khe "..." làm bật cách chú giải quyết chứng nhút nhát của em cực khéo bằng mẹo nhường thắng bóng rổ!',
    sampleHookEn: 'Someone I deeply admire for solving a tricky problem in a very clever and gentle way is Mr. John, who ingeniously helped me overcome my childhood shyness.',
    sampleClosingEn: 'Instead of lecturing me, his clever basketball trick built up my confidence naturally, showing true wisdom.'
  },
  {
    num: 25,
    title: 'Describe an appointment that was put ahead of schedule.',
    cueBullets: ['What this appointment was', 'When it happened', 'Why it was brought forward', 'And explain how you felt about the result.'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: [],
    slotSuggestions: {
      act_s2_twist: 'Organizers suddenly moved our registration appointment 45 minutes ahead of schedule to avoid a storm, and a traffic jam made me 15 minutes late',
      act_s3_lead: 'Luckily, the race officials still let me check in and join the race just in time'
    },
    hookLogicVi: 'Gài chi tiết lịch hẹn điểm danh giải "Race for Life" bị đẩy sớm 45 phút tránh bão vào ngay khe "..." Stage 2 & 3!',
    sampleHookEn: 'A nerve-racking time when an important appointment was suddenly moved ahead of schedule happened on the morning of my registration check-in for a charity cycling competition.',
    sampleClosingEn: 'Even though moving the check-in appointment earlier gave me a huge scare in traffic, everything worked out wonderfully in the end.'
  },
  {
    num: 26,
    title: 'Describe a statue or art.',
    cueBullets: ['What it looks like', 'Where you saw it', 'Did you like it', 'And why you think it is special.'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['plant'],
    slotSuggestions: {
      hist_s1_intro: 'home to a magnificent giant golden bronze Buddha statue in Ninh Binh province',
      hist_s2_detail: 'housing this 10-meter-tall bronze statue with intricate carvings and a serene, compassionate smile',
      hist_s3_action: 'When I visit this temple, I love standing quietly before the statue before walking around the lake',
      hist_s4_impact: 'admiring that peaceful statue at Bai Dinh'
    },
    hookLogicVi: 'Bẻ lái thẳng về pho tượng Phật bằng đồng khổng lồ đặt trong chùa Bái Đính + gài đặc tả pho tượng xuyên suốt 4 khe "..."!',
    sampleHookEn: 'A magnificent statue that left me in awe when I saw it in person is the giant golden bronze Buddha statue inside Bai Dinh temple.',
    sampleClosingEn: 'Standing before that majestic statue amidst the peaceful temple grounds gave me a deep sense of inner calm.'
  },
  {
    num: 27,
    title: 'Describe a bicycle tour.',
    cueBullets: ['When you had this trip', 'Whom went on with you', 'What did you do during this trip', 'And explain why you like it.'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['historical_nature', 'weather'],
    isDirectMatch: true,
    slotSuggestions: {
      act_s3_lead: 'Luckily, cycling side by side with my close university friends along the scenic tour route was amazing',
      wea_s2_sky: 'a cool breeze and clear blue skies ideal for a long bicycle tour'
    },
    hookLogicVi: 'Trúng tủ 100%! Kết hợp hành trình đạp xe gây quỹ cùng nhóm bạn (Bicycle Racing) + cảnh đẹp Ninh Bình (Bai Dinh) dưới trời thu mát mẻ!',
    sampleHookEn: 'Speaking of a memorable bicycle tour, I would love to tell you about an exciting charity cycling ride called "Race for Life" that I joined with my university friends.',
    sampleClosingEn: 'Pedalling together for a good cause and celebrating afterwards made it the best cycling trip of my life.'
  },
  {
    num: 28,
    title: 'Describe a useful website that you often visited.',
    cueBullets: ['What the contents of this website are', 'How you first found this website', 'How often you go to visited this website', 'And explain how this website helps you.'],
    recommendedBlockId: 'object_entity',
    recommendedPluginIds: [],
    slotSuggestions: {
      obj_s1_origin: 'I discovered all these cycling facts on CycleLife.vn, a website recommended by my friend that I visit three times a week',
      obj_s2_core: 'the articles and route maps on this website prove why the bicycle is such a practical means of transport',
      obj_s3_concession: 'browsing all the repair guides and fitness plans on this website is completely free',
      obj_s4_anchor: 'following the daily cycling tips on that website'
    },
    hookLogicVi: 'Bẻ lái sang website cộng đồng xe đạp "CycleLife.vn" + cài từ khóa website/articles/free guides vào cả 4 khe "..." để giám khảo tâm phục khẩu phục!',
    sampleHookEn: 'A super practical website that I browse several times every week is an online cycling hub called "CycleLife.vn", which shares route maps, bike care tips, and fitness guides.',
    sampleClosingEn: 'Thanks to all the tips and inspiration on that website, cycling has become an indispensable part of my daily routine.'
  },
  {
    num: 29,
    title: 'Describe an experience you spend your time with a child.',
    cueBullets: ['When you spent time with this child', 'Who this child was', 'What you did together', 'And explain how you felt about it'],
    recommendedBlockId: 'relation_ceremony',
    recommendedPluginIds: ['person'],
    slotSuggestions: {
      rel_s1_who: 'looking after Tommy, the energetic five-year-old grandson of Mr. John and his lovely wife',
      rel_s2_event: 'During their cozy autumn anniversary party, I spent two hours building Lego castles and drawing cartoons with little Tommy',
      rel_s3_bond: 'Seeing how polite, curious, and giggly the little boy was showed me how warmly their family raised him',
      rel_s4_impact: 'spending that playful evening with their little grandson'
    },
    hookLogicVi: 'Dịp dự tiệc mùa thu nhà vợ chồng chú John (The Happy Couple), điền khe "..." kể chuyện chơi xếp hình & vẽ tranh cùng bé Tommy 5 tuổi!',
    sampleHookEn: 'A heartwarming experience I had spending time with a little kid took place during the autumn anniversary party of Mr. John and his wife, where I looked after their five-year-old grandson.',
    sampleClosingEn: 'Playing games with that cheerful little boy reminded me of my own childhood and made the gathering even sweeter.'
  },
  {
    num: 30,
    title: 'Describe an enjoyable day spent in the countryside',
    cueBullets: ['When and where you went', 'Who you went with', 'What you did there', 'And explain why you think it was enjoyable'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['plant', 'weather'],
    slotSuggestions: {
      hist_s1_intro: 'surrounded by peaceful green rice paddies and limestone hills in rural Ninh Binh province',
      hist_s3_action: 'During our day in the countryside, my friends and I walked around the quiet lake and breathed in the fresh rural air',
      hist_s4_impact: 'that refreshing day out in the countryside',
      plant_s1_where: 'lining the quiet village lanes throughout Ninh Binh countryside'
    },
    hookLogicVi: 'Combo 3 khối siêu mượt: Ngày thu mát mẻ (Autumn Weather) về vùng quê Ninh Bình thăm Bái Đính rợp bóng tre xanh (The Bamboo)!',
    sampleHookEn: 'One of the most refreshing days I have ever spent in the countryside was a weekend trip with my friends to rural Ninh Binh province, home to Bai Dinh temple.',
    sampleClosingEn: 'Breathing in the fresh countryside air away from Hanoi’s noise recharged me completely for the week ahead.'
  },
  {
    num: 31,
    title: 'Describe a decision made by that you disagree with',
    cueBullets: ['Who made this decision', 'What it is', 'How you told him/her', 'And explain why you disagree the decision'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    slotSuggestions: {
      person_s3_memory: 'pretended to lose to make me happy, which is why I tearfully told him I disagreed when he decided to move far away',
      person_s4_lesson: 'to accept life changes maturely, even though I initially disagreed with his decision to relocate'
    },
    hookLogicVi: 'Dùng khối Mr. John: Chú quyết định chuyển nhà đi xa (khớp câu "we don\'t live near each other anymore") + gài sự phản đối vào khe "..." Stage 3 & 4!',
    sampleHookEn: 'Honestly, a decision made by someone close to me that I initially disagreed with from the bottom of my heart was when my childhood mentor, Mr. John, decided to relocate to a distant city.',
    sampleClosingEn: 'Although I told him back then how much I disagreed with his move, time taught me to respect his choice while cherishing everything he gave me.'
  },
  {
    num: 32,
    title: 'Describe an occasion waiting for something.',
    cueBullets: ['What the situation is', 'When it happened', 'Why you decided to wait', 'And explain how you felt while you were waiting'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: [],
    slotSuggestions: {
      act_s2_twist: 'On the morning of the race, I was stuck waiting anxiously for 30 minutes in a terrible traffic jam, refusing to give up',
      act_s4_highlight: 'after we all stood breathless waiting for the judges to announce me as the winner'
    },
    hookLogicVi: 'Gài 2 nhịp "chờ đợi" cực khớp vào khe "..." Stage 2 (chờ nhích từng mét trong kẹt xe) & Stage 4 (hồi hộp chờ công bố người thắng giải)!',
    sampleHookEn: 'An intense occasion when every minute of waiting felt like an eternity was when I got stuck waiting in traffic right before—and later waiting for the winner announcement of—a charity bike race.',
    sampleClosingEn: 'Looking back, refusing to give up during that stressful wait made winning the race taste twice as sweet.'
  },
  {
    num: 33,
    title: 'Describe an interesting house or an apartment you visited.',
    cueBullets: ['Where it was', 'Whose home it was', 'What it looks like', 'And explain why you think it was interesting?'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: [],
    isDirectMatch: true,
    slotSuggestions: {
      place_s1_setting: 'This impressive apartment belongs to a close family friend and sits right in Hoan Kiem district, in the centre of Hanoi'
    },
    hookLogicVi: 'Khớp trực diện 100% với khối A Modern Flat (ghé thăm căn hộ tầng cao cực hiện đại của người bạn gia đình ở quận Hoàn Kiếm)!',
    sampleHookEn: 'I would love to tell you about a stunning modern apartment I visited recently in Hoan Kiem district, which belongs to a close family friend.',
    sampleClosingEn: 'Stepping inside that stylish flat inspired me to work hard so I can own an apartment just like it one day.'
  },
  {
    num: 34,
    title: 'Describe a kind of foreign food you tried.',
    cueBullets: ['What it was', 'When and where you had it', 'Why you had it', 'And explain how you felt it.'],
    recommendedBlockId: 'food',
    recommendedPluginIds: ['place_service'],
    isDirectMatch: true,
    slotSuggestions: {
      place_s2_feature: 'glass windows, great city views, and smokeless tabletop grills at every booth'
    },
    hookLogicVi: 'Khớp trực diện 100% với Plugin Block 7: Korean BBQ! Gắn thêm Stage tả không gian nhà hàng hiện đại từ A Modern Flat để tròn 2 phút.',
    sampleHookEn: 'Well, when it comes to a mouth-watering foreign cuisine I have tried, Korean BBQ immediately comes to mind.',
    sampleClosingEn: 'All in all, trying authentic Korean BBQ was an unforgettable culinary treat that I cannot wait to repeat.'
  },
  {
    num: 35,
    title: 'Describe an interesting neighbor',
    cueBullets: ['Who this person is', 'How you know this person', 'What this person like to do', 'And explain why you think this neighbor is interesting'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    slotSuggestions: {
      person_s1_anchor: 'who was our friendly next-door neighbour as well as one of my dad’s close friends',
      person_s2_trait: 'a super interesting and humorous neighbour with endless stories'
    },
    hookLogicVi: 'Khớp trực diện với bài 1 Mr. John: Chỉ cần điền khe "..." Stage 1 & 2 giới thiệu chú John là người hàng xóm sát vách vui tính!',
    sampleHookEn: 'The most fascinating and kind-hearted neighbour I have ever had was Mr. John, who lived right next door to my family when I was growing up.',
    sampleClosingEn: 'Having an interesting and caring neighbour like Mr. John made my childhood neighbourhood feel warm and unforgettable.'
  },
  {
    num: 36,
    title: 'Describe a shop that just opened in your hometown.',
    cueBullets: ['Where the shop is', 'When it opened', 'What it sells', 'And how you feel about the shop?'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: ['food'],
    slotSuggestions: {
      place_s1_setting: 'This newly opened lifestyle café and pastry shop sits in Hoan Kiem district, right in the centre of Hanoi',
      place_s2_feature: 'panoramic city views and neat wooden shelves selling freshly baked cakes and roasted coffee beans',
      place_s3_activity: 'An open counter prepares specialty drinks and pastries, while shoppers relax comfortably on the leather sofas.',
      place_s4_future: 'its prices are surprisingly affordable for students, so I drop by this new shop almost every weekend'
    },
    hookLogicVi: 'Đúng hướng dẫn gốc của A Modern Flat: Thay cả 4 khe "..." từ căn hộ sang cửa hàng cà phê & bánh ngọt mới khai trương trên tầng cao Hoàn Kiếm!',
    sampleHookEn: 'Recently, a trendy lifestyle coffee and bakery shop just opened in Hoan Kiem district, and it has quickly become my favourite hangout spot.',
    sampleClosingEn: 'With its modern design, tasty products, and panoramic city view, I am sure this new shop will thrive for years.'
  },
  {
    num: 37,
    title: 'Describe a future plan which is not related to work or study',
    cueBullets: ['What the plan is', 'When you thought of the plan', 'Who is involved in the plan', 'And say how you think you will achieve the plan.'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather'],
    slotSuggestions: {
      hist_s1_intro: 'a peaceful spiritual complex in Ninh Binh province where I plan to take my parents this autumn',
      hist_s3_action: 'By saving a bit of money each month and booking a minibus, we will walk around the lake and enjoy the view together',
      hist_s4_impact: 'planning this relaxing family retreat away from work and study'
    },
    hookLogicVi: 'Kế hoạch cá nhân đưa bố mẹ đi nghỉ dưỡng cuối tuần tại chùa Bái Đính mùa thu tới — gài cách thực hiện (tiết kiệm tiền, đặt xe) vào khe "..." Stage 3!',
    sampleHookEn: 'Speaking of a personal future plan completely unrelated to work or study, I am planning a relaxing autumn weekend getaway with my parents to Bai Dinh temple.',
    sampleClosingEn: 'By saving a little pocket money each month and booking transport early, I am confident we will make this refreshing trip happen soon.'
  },
  {
    num: 38,
    title: 'Describe a well-paid job you would like to do in the future.',
    cueBullets: ['What job it is', 'What qualities are required for this job', 'What you would need to learn to get this job', 'And explain why you would like to do this job.'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: [],
    slotSuggestions: {
      place_s1_setting: 'To master 3D design and English for this interior architect job, my dream is to design high-end flats in central Hanoi',
      place_s3_activity: 'An interior architect gets to craft smart modern kitchens and cozy living rooms where families love to gather.',
      place_s4_future: 'succeeding in this well-paid design career one day will let me create—and afford—a dream apartment just like this'
    },
    hookLogicVi: 'Bẻ lái sang nghề Kiến trúc sư nội thất lương cao + gài kỹ năng cần học (3D design, creativity) vào khe "..." của khối A Modern Flat!',
    sampleHookEn: 'In the future, a well-paid profession I aspire to pursue is becoming a senior interior architect, largely because I dream of designing and owning modern high-rise apartments.',
    sampleClosingEn: 'Working towards that rewarding career gives me clear motivation to master design skills and afford my dream home.'
  },
  {
    num: 39,
    title: 'Describe a book that you would like to read again.',
    cueBullets: ['What the book was about', 'Why you read it the first place', 'What you learned from this book', 'And explain why you would like to read again.'],
    recommendedBlockId: 'object_entity',
    recommendedPluginIds: ['person'],
    slotSuggestions: {
      obj_s1_origin: 'I first read about that 1817 history in a book called "Miracle on Two Wheels", which my mentor lent me as a teenager',
      obj_s2_core: 'the book’s chapters vividly explain why the bicycle is such a practical means of transport',
      obj_s3_concession: 'this book is quite short and written in simple language',
      obj_s4_anchor: 'the life lessons inside that book'
    },
    hookLogicVi: 'Dùng Hook "Lớp Vỏ Bọc" cuốn sách "Miracle on Two Wheels" + gài chapters/lessons của cuốn sách xuyên suốt 4 khe "..." khối The Bicycle!',
    sampleHookEn: 'A fascinating book that I would love to read all over again is titled "Miracle on Two Wheels", which tells the inspiring history of the bicycle and green living.',
    sampleClosingEn: 'Re-reading that book always reminds me to appreciate simple, sustainable things like my trusty bicycle.'
  },
  {
    num: 40,
    title: 'Describe a kind of weather that you like',
    cueBullets: ['What it is', 'What you usually do in this kind of weather', 'How you felt about it', 'And explain what influences it may bring to you'],
    recommendedBlockId: 'weather',
    recommendedPluginIds: ['historical_nature'],
    isDirectMatch: true,
    hookLogicVi: 'Khớp trực diện 100% với Plugin Block 9: Autumn Weather (Thời tiết mùa thu Hà Nội)! Cắm thêm 1–2 Stage Bái Đính để đủ 2 phút.',
    sampleHookEn: 'Without a doubt, the kind of weather I adore the most is the crisp, cool autumn weather in Hanoi.',
    sampleClosingEn: 'Whenever autumn arrives with its gentle breeze, I feel happier, calmer, and more inspired than at any other time of year.'
  },
  {
    num: 41,
    title: 'Describe an interesting talk or speech you heard recently.',
    cueBullets: ['Who was the person you talk to', 'Where and when you talked with this person', 'What you talked about with this person', 'And explain why it was interesting?'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    slotSuggestions: {
      person_s1_anchor: 'who recently met me at a quiet café and gave me an unforgettable talk about patience in life',
      person_s2_trait: 'a gentle, eloquent speaker whose calm voice immediately draws you in',
      person_s3_memory: 'pretended to lose at basketball back then, a memory we laughed about warmly during our recent talk',
      person_s4_lesson: 'through that inspiring talk to stay patient and understanding towards others'
    },
    hookLogicVi: 'Bẻ lái sang buổi trò chuyện/chia sẻ truyền cảm hứng gần đây với chú John + gài "that talk" vào khe "..." Stage 1, 3, 4!',
    sampleHookEn: 'Recently, I heard an unforgettable heart-to-heart talk—almost like a mini life speech—from Mr. John about patience, kindness, and our childhood memories.',
    sampleClosingEn: 'Every word he shared in that talk stayed with me and reminded me why he has always been my greatest role model.'
  },
  {
    num: 42,
    title: 'Describe a famous person in your country.',
    cueBullets: ['Who this person is', 'How you know this person', 'What this person famous for', 'And explain why you like this person.'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    slotSuggestions: {
      person_s1_anchor: 'a famous former national basketball player in Vietnam who happened to be my dad’s old friend',
      person_s2_trait: 'a humble and gentle celebrity despite winning many national championships',
      person_s4_lesson: 'to stay humble, patient, and kind no matter how famous you become'
    },
    hookLogicVi: 'Nâng cấp chú John thành cựu tuyển thủ bóng rổ nổi tiếng Việt Nam nhưng giản dị ngoài đời thông qua khe "..." Stage 1, 2, 4!',
    sampleHookEn: 'Well, a famous figure in my country whom I admire deeply—and was lucky enough to know through my father—is a former national basketball star named John.',
    sampleClosingEn: 'Despite his fame on the basketball court, his humility and kindness in real life are what make me respect him the most.'
  },
  {
    num: 43,
    title: 'Describe a café or restaurant you enjoy.',
    cueBullets: ['Where it is', 'Where it is like there', 'How often you go there', 'And explain why you enjoy going there.'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: ['food'],
    slotSuggestions: {
      place_s1_setting: 'This rooftop café-restaurant sits in Hoan Kiem district, right in the centre of Hanoi, and I go there almost every weekend',
      place_s3_activity: 'Their modern open kitchen prepares delicious coffee and grilled dishes, while guests unwind in the cozy lounge.',
      place_s4_future: 'even though it looks upscale, the prices are very fair, making it my favourite weekend spot'
    },
    hookLogicVi: 'Combo đỉnh cao: Tả không gian quán tầng cao Hoàn Kiếm (A Modern Flat đổi khe "..." sang café-restaurant) + món ngon (Korean BBQ)!',
    sampleHookEn: 'My absolute favourite place to dine and unwind with friends is a modern rooftop café-restaurant right in Hoan Kiem district.',
    sampleClosingEn: 'With its airy modern vibe, city views, and mouth-watering food, it is easily the place I enjoy visiting most on weekends.'
  },
  {
    num: 44,
    title: 'Describe a polite person you met.',
    cueBullets: ['Who this person was', 'When and where you met this person', 'How you met', 'And explain why you think he or she was polite.'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    slotSuggestions: {
      person_s2_trait: 'the most polite, soft-spoken, and well-mannered man I have ever met',
      person_s3_memory: 'pretended to lose and always said "thank you" and "well played" even to a little kid like me',
      person_s4_lesson: 'to treat everyone—young or old—with genuine politeness and respect'
    },
    hookLogicVi: 'Khớp hoàn hảo với Mr. John + nhấn chi tiết cách nói năng lễ độ, lịch thiệp vào khe "..." Stage 2, 3, 4!',
    sampleHookEn: 'When I think of the most polite and well-mannered person I have ever met, Mr. John immediately comes to mind.',
    sampleClosingEn: 'His gentle manners and genuine respect for everyone—even a little kid like me—taught me what true politeness means.'
  },
  {
    num: 45,
    title: 'Describe a popular place where people go swimming.',
    cueBullets: ['Where it is', 'What it looks like', 'What kind of people usually go there', 'And explain why people like to go there.'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather'],
    slotSuggestions: {
      hist_s1_intro: 'famous not only for its temple complex in Ninh Binh province but also for the clean eco-swimming lagoon beside it',
      hist_s2_detail: 'featuring a crystal-clear natural swimming area surrounded by traditional architecture and green hills',
      hist_s3_action: 'Families, students, and travellers love going for a cool swim there before walking around the peaceful lake',
      hist_s4_impact: 'swimming and unwinding in that peaceful spot'
    },
    hookLogicVi: 'Bẻ lái sang khu hồ bơi sinh thái tự nhiên sát quần thể Bái Đính + gài hoạt động bơi lội của gia đình, du khách vào cả 4 khe "..."!',
    sampleHookEn: 'A popular scenic spot where many families and travellers love to go for a refreshing swim is a natural eco-lagoon right beside the Bai Dinh complex in Ninh Binh.',
    sampleClosingEn: 'Swimming in cool clean water surrounded by peaceful traditional scenery is why people flock there every summer and autumn.'
  },
  {
    num: 46,
    title: 'Describe a trip you plan to take in the near future.',
    cueBullets: ['Where you plan to go', 'Who you plan to go with', 'How you plan to travel', 'And explain what you plan to see and do on this trip'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather', 'food'],
    slotSuggestions: {
      hist_s1_intro: 'a famous spiritual complex in Ninh Binh province where my friends and I plan to travel by coach next month',
      hist_s3_action: 'Once we get there, we plan to walk around the lake, take photos, and enjoy the beautiful view together',
      hist_s4_impact: 'having this upcoming trip to look forward to'
    },
    hookLogicVi: 'Đúng ví dụ số 1 của bài Bai Dinh Temple: Chuyển khe "..." Stage 1, 3, 4 sang kế hoạch đi xe khách cùng nhóm bạn vào tháng tới!',
    sampleHookEn: 'In the near future, right after my upcoming exams, I am planning to take a weekend trip by coach with my close friends to Bai Dinh temple in Ninh Binh.',
    sampleClosingEn: 'I am counting down the days until this trip because I know it will be the perfect way for us to unwind.'
  },
  {
    num: 47,
    title: 'Describe a time you were not allowed to use your mobile phone.',
    cueBullets: ['When and where it was', 'Why you were not allowed to use your phone', 'What you wanted to use your phone for', 'And explain how you felt about not being able to use your phone.'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: [],
    slotSuggestions: {
      hist_s2_detail: 'with sacred prayer halls where signs strictly forbid visitors from using mobile phones to preserve silence',
      hist_s3_action: 'Although I wanted to use my phone to take photos of the architecture, switching it off let me walk quietly and enjoy the view',
      hist_s4_impact: 'that peaceful phone-free afternoon at Bai Dinh'
    },
    hookLogicVi: 'Bẻ lái vào quy định tắt điện thoại khi vào chánh điện chùa Bái Đính + gài lý do muốn chụp ảnh nhưng tắt máy lại thấy bình yên vào khe "..." Stage 2–4!',
    sampleHookEn: 'A memorable time when I was strictly not allowed to use my mobile phone was when I stepped inside the sacred main hall of Bai Dinh temple.',
    sampleClosingEn: 'Surprisingly, putting my phone away turned out to be a blessing because it let me truly soak in the peaceful spiritual atmosphere.'
  },
  {
    num: 48,
    title: 'Describe an occasion that you feel excited.',
    cueBullets: ['What it is', 'Where you can do it', 'How you do it', 'And explain why you feel excited'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: [],
    isDirectMatch: true,
    slotSuggestions: {
      act_s3_lead: 'Luckily, I joined the race in time with my heart pounding with pure excitement',
      act_s4_highlight: 'where I jumped for joy as the winner'
    },
    hookLogicVi: 'Khớp trực diện với cảm giác hồi hộp vỡ òa khi đua và về nhất giải "Race for Life" (Bicycle Racing)!',
    sampleHookEn: 'One of the most thrilling occasions when my heart was pounding with excitement was the day I competed in and won a charity cycling race.',
    sampleClosingEn: 'Even today, recalling the cheers at the finish line brings back that exact rush of pure excitement.'
  },
  {
    num: 49,
    title: 'Describe a quiet place you visited.',
    cueBullets: ['Where it was', 'When you went there', 'What you did there', 'And explain why you think it was quite'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather'],
    isDirectMatch: true,
    hookLogicVi: 'Khớp trực diện 100% với Bai Dinh Temple ("easily find a quiet place to myself whenever I want to escape the busy city")!',
    sampleHookEn: 'Whenever I think of a peaceful, quiet sanctuary I have visited to escape city noise, Bai Dinh temple in Ninh Binh is the first place I remember.',
    sampleClosingEn: 'That tranquil lakeside corner of Bai Dinh will always be my go-to hideaway whenever life gets overwhelming.'
  },
  {
    num: 50,
    title: 'Describe a family member who you are proud of',
    cueBullets: ['Who this person is', 'How often you spend time together', 'What he or she does makes you proud.', 'And explain why you are proud of this person.'],
    recommendedBlockId: 'person',
    recommendedPluginIds: ['relation_ceremony'],
    slotSuggestions: {
      person_s1_anchor: 'who is actually my father’s younger cousin—my Uncle John—whom our whole family is proud of',
      person_s4_lesson: 'to be patient and kind, making me deeply proud to have him in my family'
    },
    hookLogicVi: 'Biến nhẹ chú John ở khe "..." Stage 1 & 4 thành "Uncle John — chú họ trong gia đình" mà em luôn tự hào!',
    sampleHookEn: 'A beloved family member whom I am immensely proud of is my Uncle John, my father’s cousin who practically helped raise me.',
    sampleClosingEn: 'Seeing how kind, patient, and respected Uncle John is makes me truly proud to be part of his family.'
  },
  {
    num: 51,
    title: 'A wedding you have been to',
    cueBullets: ['Where it was', 'Who you went with', 'What you saw', 'And how you felt about the wedding?'],
    recommendedBlockId: 'relation_ceremony',
    recommendedPluginIds: ['food', 'weather'],
    slotSuggestions: {
      rel_s1_who: 'the silver wedding renewal ceremony of Mr. John and his lovely wife',
      rel_s2_event: 'My parents and I attended their cozy wedding reception at a modern restaurant decorated with white roses',
      rel_s3_bond: 'Watching them exchange heartfelt vows and thank all the guests brought happy tears to everyone’s eyes',
      rel_s4_impact: 'attending that heartwarming wedding ceremony'
    },
    hookLogicVi: 'Khớp trực diện khối 6 The Happy Couple + điền khe "..." tả không khí lễ cưới, hoa hồng trắng và lời thề trên sân khấu!',
    sampleHookEn: 'One of the warmest and most joyful weddings—a milestone wedding renewal ceremony—I have ever attended was held for Mr. John and his lovely wife.',
    sampleClosingEn: 'Attending that heartwarming celebration left me with unforgettable memories of love, family, and happiness.'
  },
  {
    num: 52,
    title: 'Describe an occasion that you received a good service from a company or shop',
    cueBullets: ['What the service was', 'When and where you received the service', 'Whom you were together with', 'And explain why you think it was a good service'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: ['food'],
    slotSuggestions: {
      place_s1_setting: 'This newly opened rooftop lounge and restaurant sits in Hoan Kiem district, right in the centre of Hanoi',
      place_s2_feature: 'great city views and polite staff who greeted my family warmly right at the elevator',
      place_s3_activity: 'The waiter patiently explained the menu, grilled our food at the table, and even offered free hot tea for my parents.',
      place_s4_future: 'receiving such thoughtful five-star service at a fair price made me a loyal customer right away'
    },
    hookLogicVi: 'Kết hợp không gian sang trọng (A Modern Flat) + điền khe "..." tả sự tận tình của nhân viên phục vụ bàn cùng gia đình!',
    sampleHookEn: 'An occasion when I was genuinely impressed by top-notch customer service was during a weekend visit with my family to a rooftop restaurant in Hoan Kiem.',
    sampleClosingEn: 'Because the staff were so attentive inside such a comfortable modern space, I have recommended their service to all my friends.'
  },
  {
    num: 53,
    title: 'Describe a place you would like to visit in space 🚀',
    cueBullets: ['Where it is', 'What it looks like', 'What you would do there', 'And explain why you want to visit this place.'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: [],
    slotSuggestions: {
      place_s1_setting: 'This futuristic orbital space hotel floats 400 kilometres above Earth, designed inside like a cozy luxury flat',
      place_s2_feature: 'panoramic dome windows offering breathtaking views of our glowing blue Earth and millions of stars',
      place_s3_activity: 'Astronaut-chefs prepare space meals in a high-tech kitchen, while guests float weightlessly and relax in the lounge.',
      place_s4_future: 'if commercial space tickets become affordable one day, this orbital hotel is the exact place in space I will visit'
    },
    hookLogicVi: 'Tuyệt chiêu "Lớp Vỏ Bọc": Trạm khách sạn vũ trụ có nội thất y hệt A Modern Flat — thay 4 khe "..." từ Hà Nội sang quỹ đạo ngắm Trái Đất!',
    sampleHookEn: 'To tell you the truth, if space tourism becomes affordable one day, I would love to visit an orbital space hotel designed inside just like a cozy, ultra-modern apartment.',
    sampleClosingEn: 'Experiencing zero gravity inside a comfortable modern living space with a view of our blue planet would be a dream come true.'
  },
  {
    num: 54,
    title: 'Describe a movie or documentary about space 🚀',
    cueBullets: ['What it is', 'When you watched it', 'What it is about', 'And explain why you liked it.'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    slotSuggestions: {
      person_s1_anchor: 'a retired NASA astronaut in the film who mentored a lonely boy next door while his parents worked late',
      person_s2_trait: 'portrayed as a gentle, kind-hearted astronaut with a warm sense of humour',
      person_s3_memory: 'pretended to lose at backyard basketball while inspiring the boy with stories of walking among the stars',
      person_s4_lesson: 'through that touching space movie to stay patient, curious, and kind'
    },
    hookLogicVi: 'Tuyệt chiêu "Lớp Vỏ Bọc": Phim vũ trụ "Beyond the Stars" kể về cựu phi hành gia Mr. John và cậu bé hàng xóm — cài từ khóa bộ phim vào cả 4 khe "..."!',
    sampleHookEn: 'Honestly, I am not a huge sci-fi geek, but I was deeply moved by a space movie called "Beyond the Stars", because at its heart it tells the human story of a retired astronaut named Mr. John.',
    sampleClosingEn: 'By blending outer-space dreams with such a touching story of mentorship, that film became my favourite movie about space.'
  },
  {
    num: 55,
    title: 'Describe a time you looked at the sky or stars 🚀',
    cueBullets: ['When it was', 'Who you were with', 'What you saw', 'And explain how you felt about it.'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather'],
    slotSuggestions: {
      hist_s1_intro: 'a peaceful countryside complex in Ninh Binh province far away from Hanoi’s city lights',
      hist_s2_detail: 'with wide open courtyards where zero light pollution lets you see the Milky Way clearly at night',
      hist_s3_action: 'Sitting quietly by the temple lake that night with my friends, we looked up at thousands of twinkling stars',
      hist_s4_impact: 'that magical night gazing at the starry sky',
      wea_s2_sky: 'a cool autumn breeze and crystal-clear night skies sparkling with stars'
    },
    hookLogicVi: 'Ghép Bái Đính + Trời thu trong vắt không ô nhiễm ánh sáng, gài cảnh ngước nhìn dải Ngân Hà bên hồ vào khe "..."!',
    sampleHookEn: 'An unforgettable evening when I gazed up at a breathtaking starry sky happened during an autumn trip with my friends to the peaceful countryside around Bai Dinh temple.',
    sampleClosingEn: 'Looking up at thousands of twinkling stars under that crisp autumn sky made all my exam stress melt away.'
  }
];

export function getSpk2BlockById(id: Spk2BlockId): Spk2LegoBlock {
  return SPK2_LEGO_BLOCKS.find((b) => b.id === id) || SPK2_LEGO_BLOCKS[0];
}

export function normalizeSpkTopic(str: string): string {
  return (str || '')
    .toLowerCase()
    .replace(/^\s*\d+\.\s*/, '')
    .replace(/🚀/g, '')
    .replace(/[^a-z0-9\s]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

export function findSpk2PromptMeta(
  topicText: string,
  promptNum?: number,
  preferredBlockId?: Spk2BlockId
): Spk2PromptItem {
  if (promptNum && promptNum >= 1 && promptNum <= 55) {
    const byNum = SPK2_PROMPTS_55.find((p) => p.num === promptNum);
    if (byNum) return byNum;
  }

  const numPrefix = (topicText || '').match(/^\s*(\d+)\./);
  if (numPrefix) {
    const parsedNum = parseInt(numPrefix[1], 10);
    const byPrefix = SPK2_PROMPTS_55.find((p) => p.num === parsedNum);
    if (byPrefix) return byPrefix;
  }

  const normTarget = normalizeSpkTopic(topicText);

  // If opened from a Block lesson header without a specific prompt text, pick a steered Past Paper for that Block
  if (!normTarget && preferredBlockId) {
    const steeredForBlock =
      SPK2_PROMPTS_55.find((p) => p.recommendedBlockId === preferredBlockId && !p.isDirectMatch) ||
      SPK2_PROMPTS_55.find((p) => p.recommendedBlockId === preferredBlockId) ||
      SPK2_PROMPTS_55.find((p) => p.recommendedPluginIds.includes(preferredBlockId));
    if (steeredForBlock) return steeredForBlock;
  }

  if (normTarget) {
    const exact = SPK2_PROMPTS_55.find(
      (p) =>
        normalizeSpkTopic(p.title) === normTarget &&
        (!preferredBlockId ||
          p.recommendedBlockId === preferredBlockId ||
          p.recommendedPluginIds.includes(preferredBlockId))
    );
    if (exact) return exact;

    const exactAny = SPK2_PROMPTS_55.find((p) => normalizeSpkTopic(p.title) === normTarget);
    if (exactAny && !preferredBlockId) return exactAny;

    const partial = SPK2_PROMPTS_55.find((p) => {
      const np = normalizeSpkTopic(p.title);
      const matchesText = np.includes(normTarget) || normTarget.includes(np);
      if (!matchesText) return false;
      return (
        !preferredBlockId ||
        p.recommendedBlockId === preferredBlockId ||
        p.recommendedPluginIds.includes(preferredBlockId)
      );
    });
    if (partial) return partial;
  }

  // Fallback for any custom Part 2 practice prompt (e.g., from Lectures 1–9 Page 2)
  const lower = normTarget;
  let blockId: Spk2BlockId = preferredBlockId || 'action_experience';
  if (!preferredBlockId) {
    if (/\b(person|stranger|neighbor|neighbour|friend|family|teacher|polite|famous|old|taught|encouraged)\b/.test(lower)) {
      blockId = 'person';
    } else if (/\b(couple|wedding|marriage|child|party|promise)\b/.test(lower)) {
      blockId = 'relation_ceremony';
    } else if (/\b(food|meal|cake|dish|dinner|eat|celebrated)\b/.test(lower)) {
      blockId = 'food';
    } else if (/\b(plant|tree|flower|crop|symbol|locally)\b/.test(lower)) {
      blockId = 'plant';
    } else if (/\b(weather|season|climate)\b/.test(lower)) {
      blockId = 'weather';
    } else if (/\b(quiet|temple|historical|countryside|statue|trip|river|sea|sky|star|beautiful place)\b/.test(lower)) {
      blockId = 'historical_nature';
    } else if (/\b(house|flat|apartment|shop|cafe|restaurant|city|service|news|job|relax)\b/.test(lower)) {
      blockId = 'place_service';
    } else if (/\b(invention|object|gift|free|clothing|website|company|book|series|bought)\b/.test(lower)) {
      blockId = 'object_entity';
    }
  }

  const block = getSpk2BlockById(blockId);
  const cleanTopic = (topicText || 'this topic')
    .replace(/^📝\s*/, '')
    .replace(/^Describe\s+/i, '')
    .replace(/\.$/, '')
    .trim();

  // Build smart fallback slotSuggestions from the block's curated steering examples
  const autoSlots: Record<string, string> = {};
  for (const st of block.stages) {
    for (const sl of st.slots) {
      if (sl.examples && sl.examples.length > 0) {
        const matchedEx = sl.examples.find((ex) => {
          const words = normalizeSpkTopic(ex.valueEn)
            .split(' ')
            .filter((w) => w.length >= 4);
          return words.some((w) => lower.includes(w));
        });
        autoSlots[sl.id] = matchedEx ? matchedEx.valueEn : sl.examples[0].valueEn;
      }
    }
  }

  return {
    num: 0,
    title: (topicText || 'Describe a memorable topic in IELTS Speaking Part 2').replace(/^📝\s*/, '').trim(),
    cueBullets: ['What/Who it is', 'When and where it happened', 'Key details & story', 'And explain how you felt about it'],
    recommendedBlockId: blockId,
    recommendedPluginIds: blockId === 'weather' ? ['historical_nature'] : ['weather'],
    isDirectMatch: false,
    slotSuggestions: autoSlots,
    hookLogicVi: `Áp dụng khối ${block.name}: Dùng câu Hook dẫn từ "${cleanTopic}" vào câu chuyện, sau đó tùy biến nhẹ 4 khe "..." trong các Stage để gài từ khóa đề bài xuyên suốt 2 phút mà không sợ lạc đề!`,
    sampleHookEn: `Well, when it comes to ${cleanTopic}, the very first story that springs to my mind connects directly to ${block.name.split(' (')[0]}.`,
    sampleClosingEn: `All in all, that is why this unforgettable memory immediately came to my mind when talking about ${cleanTopic}.`
  };
}
