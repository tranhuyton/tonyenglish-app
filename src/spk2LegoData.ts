// ============================================================================
// IELTS SPEAKING PART 2 — LEGO BLOCKS & HOOK STEERING ("BẺ LÁI") DATA
// 6 Main Blocks + 3 Plugin Blocks + Universal Hooks + Bridges + 55 Past Papers
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

export interface Spk2StageBrick {
  id: string;
  blockId: Spk2BlockId;
  stageNumber: 1 | 2 | 3 | 4;
  stageTitle: string;
  textEn: string;
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
  hookLogicVi: string;
  sampleHookEn: string;
  sampleClosingEn: string;
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
        textVi:
          'Tôi muốn nói về ông John. Khi còn nhỏ, cha mẹ tôi rất bận nên tôi phải dành phần lớn thời gian một mình. Trong thời gian đó, tôi đã gặp John, một trong những người bạn thân nhất của cha tôi. Thành thật mà nói, chú ấy đã chăm sóc tôi rất tốt.',
        keywords: ['talk', 'child', 'During', 'good care'],
        goldenPhrases: ['spend a lot of time on my own', 'To be honest', 'took really good care of me']
      },
      {
        id: 'person_s2',
        blockId: 'person',
        stageNumber: 2,
        stageTitle: 'Stage 2: Appearance & Personality',
        textEn:
          "In fact, John is a very gentle and kind man. As far as I recall, he was quite tall, about 6 feet. He was also really good at basketball. Whenever I think of him, I can't help laughing because the way he walked was so funny. It looked like he was walking on sticks!",
        textVi:
          'Thực tế là, John là một người rất nhẹ nhàng và tốt bụng. Theo như tôi nhớ, chú ấy khá cao, khoảng 6 feet và chơi bóng rổ rất giỏi. Mỗi khi nghĩ về chú, tôi không nhịn được cười vì dáng đi buồn cười như đi trên cà kheo!',
        keywords: ['gentle', 'far', 'basketball', 'appearance', 'sticks'],
        goldenPhrases: ['As far as I recall', "can't help laughing", 'walking on sticks']
      },
      {
        id: 'person_s3',
        blockId: 'person',
        stageNumber: 3,
        stageTitle: 'Stage 3: Memories',
        textEn:
          'If my memory serves me well, we used to play basketball in my backyard. Although John was great at basketball, he often pretended to lose and let me win. It always brings tears to my eyes every time I recall those beautiful memories.',
        textVi:
          'Nếu tôi nhớ không lầm, chúng tôi thường chơi bóng rổ ở sân sau. Mặc dù John chơi rất giỏi, chú ấy thường giả vờ thua và nhường tôi thắng. Điều đó luôn làm tôi rưng rưng nước mắt mỗi khi nhớ lại những kỷ niệm đẹp ấy.',
        keywords: ['memory', 'Although', 'tears'],
        goldenPhrases: ['If my memory serves me well', 'Although', 'brings tears to my eyes']
      },
      {
        id: 'person_s4',
        blockId: 'person',
        stageNumber: 4,
        stageTitle: 'Stage 4: Influence & Feelings',
        textEn:
          "He always taught me to be more patient and understanding towards other people. If it hadn't been for him, I wouldn't be the person I am today. John was a great role model for me. Now that I'm an adult, I still miss him because we don't live near each other anymore. I really hope I can see him again one day.",
        textVi:
          'Chú luôn dạy tôi kiên nhẫn và thấu hiểu người khác hơn. Nếu không có chú, tôi sẽ không trở thành người như hôm nay. John là hình mẫu tuyệt vời của tôi. Giờ đã trưởng thành, tôi vẫn nhớ chú và hy vọng có thể gặp lại chú một ngày nào đó.',
        keywords: ['taught', "hadn't been", 'role model', 'adult', 'see him'],
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
    usedFor: 'Ngôi nhà mơ ước, quán cafe/cửa hàng mới mở, nhà hàng, nơi có dịch vụ tốt, thành phố, tin vui, công việc mơ ước...',
    stages: [
      {
        id: 'place_s1',
        blockId: 'place_service',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          "I would like to talk about a modern flat that I'd love to own one day. It is located in Hoan Kiem district, right in the centre of Hanoi, close to all the best restaurants and shops.",
        textVi:
          'Tôi muốn nói về một căn hộ hiện đại mà tôi muốn sở hữu vào một ngày nào đó (hoặc quán cafe mới mở). Nó nằm ở quận Hoàn Kiếm, ngay trung tâm Hà Nội, gần tất cả các nhà hàng và cửa hàng tốt nhất.',
        keywords: ['flat', 'located', 'centre', 'close'],
        goldenPhrases: ['right in the centre of Hanoi', 'close to all the best restaurants and shops']
      },
      {
        id: 'place_s2',
        blockId: 'place_service',
        stageNumber: 2,
        stageTitle: 'Stage 2: Description',
        textEn:
          'The place is on a high floor of a brand-new building. The style is very modern, with wooden floors, comfortable leather sofas, and colourful rugs. It is also very airy and bright, with lots of windows and great views of the city.',
        textVi:
          'Nơi này nằm trên tầng cao của một tòa nhà hoàn toàn mới. Phong cách rất hiện đại với sàn gỗ, sofa da êm ái và thảm đầy màu sắc. Không gian rất thoáng đãng, sáng sủa với nhiều cửa sổ và tầm nhìn tuyệt đẹp ra thành phố.',
        keywords: ['high floor', 'modern', 'wooden', 'airy', 'views'],
        goldenPhrases: ['brand-new building', 'airy and bright', 'great views of the city']
      },
      {
        id: 'place_s3',
        blockId: 'place_service',
        stageNumber: 3,
        stageTitle: 'Stage 3: Activities',
        textEn:
          'This place is perfect for my family and friends to relax. A modern kitchen is great for preparing delicious drinks and meals. Also, our guests can easily relax in the comfortable living room.',
        textVi:
          'Nơi này hoàn hảo để gia đình và bạn bè tôi thư giãn. Căn bếp (hoặc quầy pha chế) hiện đại rất tuyệt để chuẩn bị đồ uống và bữa ăn ngon, và khách có thể thoải mái nghỉ ngơi ở phòng khách.',
        keywords: ['perfect', 'kitchen', 'prepare', 'relax'],
        goldenPhrases: ['preparing delicious drinks and meals', 'comfortable living room']
      },
      {
        id: 'place_s4',
        blockId: 'place_service',
        stageNumber: 4,
        stageTitle: 'Stage 4: Feelings & Future',
        textEn:
          'I know that a place like this is very expensive. However, if I am successful in my career and make a lot of money one day, this is exactly the kind of place I will buy. I think almost everybody would love to spend time in a place like this.',
        textVi:
          'Tôi biết một nơi như thế này rất đắt đỏ. Tuy nhiên, nếu tôi thành công trong sự nghiệp và kiếm được nhiều tiền một ngày nào đó, đây chính xác là nơi tôi sẽ mua (hoặc ghé thăm mỗi ngày). Hầu như ai cũng thích dành thời gian ở nơi như vậy.',
        keywords: ['expensive', 'However', 'successful', 'everybody'],
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
    usedFor: 'Chuyến đi tương lai, địa điểm lịch sử, bức tượng, nơi yên tĩnh/đông người, miền quê, ngắm bầu trời...',
    stages: [
      {
        id: 'hist_s1',
        blockId: 'historical_nature',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          'I would like to talk about Bai Dinh temple. It is a famous cultural and spiritual complex in Ninh Binh province, which is very close to Hanoi.',
        textVi:
          'Tôi muốn nói về chùa Bái Đính. Đây là một quần thể văn hóa và tâm linh nổi tiếng ở tỉnh Ninh Bình, rất gần Hà Nội.',
        keywords: ['talk', 'spiritual', 'Ninh Binh', 'close'],
        goldenPhrases: ['cultural and spiritual complex', 'very close to Hanoi']
      },
      {
        id: 'hist_s2',
        blockId: 'historical_nature',
        stageNumber: 2,
        stageTitle: 'Stage 2: Description',
        textEn:
          'It is considered the largest Buddhist temple in Vietnam. The place is very beautiful and vast, representing traditional Vietnamese architecture. There is also a large river around the complex.',
        textVi:
          'Nơi đây được xem là ngôi chùa Phật giáo lớn nhất Việt Nam, rất đẹp và rộng lớn, đại diện cho kiến trúc truyền thống Việt Nam và có một con sông lớn bao quanh.',
        keywords: ['considered', 'largest', 'beautiful & vast', 'representing', 'river'],
        goldenPhrases: ['considered the largest Buddhist temple', 'representing traditional Vietnamese architecture']
      },
      {
        id: 'hist_s3',
        blockId: 'historical_nature',
        stageNumber: 3,
        stageTitle: 'Stage 3: Activities',
        textEn:
          'When I visit this place, I just like to walk around the lake and enjoy the beautiful view. It is always great fun and a pleasure for me.',
        textVi:
          'Khi ghé thăm nơi này, tôi thích đi dạo quanh hồ và tận hưởng khung cảnh tuyệt đẹp. Đó luôn là niềm vui và sự thư thái lớn đối với tôi.',
        keywords: ['visit', 'walk', 'view', 'fun', 'pleasure'],
        goldenPhrases: ['walk around the lake', 'great fun and a pleasure']
      },
      {
        id: 'hist_s4',
        blockId: 'historical_nature',
        stageNumber: 4,
        stageTitle: 'Stage 4: Significance',
        textEn:
          "This place is really important to me. Although there are usually many tourists, I can still easily find a quiet place to myself whenever I want to escape the busy city. If it hadn't been for this place, I wouldn't have been able to relax, unwind, and do pretty well in my last exam.",
        textVi:
          'Nơi này thực sự quan trọng với tôi. Mặc dù thường đông du khách, tôi vẫn dễ dàng tìm được góc yên tĩnh cho riêng mình để trốn khỏi thành phố ồn ào. Nếu không có nơi này, tôi đã không thể thư giãn, xả hơi và làm tốt kỳ thi vừa qua.',
        keywords: ['important', 'Although', 'quiet', 'escape', "hadn't been", 'unwind'],
        goldenPhrases: ['escape the busy city', "If it hadn't been for this place", 'relax, unwind']
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
    usedFor: 'Phát minh thay đổi cuộc sống, món đồ yêu thích, quà miễn phí, công ty lớn, trang web hữu ích, cuốn sách/phim...',
    stages: [
      {
        id: 'obj_s1',
        blockId: 'object_entity',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          'I would like to talk about my bicycle. As you know, a bicycle is a simple, human-powered vehicle. If my memory serves me well, it was first invented back in 1817 by a German professor. My parents bought me my first bicycle as a Tet holiday gift when I was a teenager.',
        textVi:
          'Tôi muốn nói về chiếc xe đạp của mình. Như bạn biết, xe đạp là phương tiện chạy bằng sức người đơn giản. Nếu tôi nhớ không lầm, nó được phát minh năm 1817 bởi một giáo sư người Đức. Bố mẹ mua cho tôi chiếc xe đầu tiên làm quà Tết khi tôi là thiếu niên.',
        keywords: ['bicycle', 'simple', 'memory', 'invented', 'gift'],
        goldenPhrases: ['human-powered vehicle', 'If my memory serves me well', 'invented back in 1817']
      },
      {
        id: 'obj_s2',
        blockId: 'object_entity',
        stageNumber: 2,
        stageTitle: 'Stage 2: Main Features',
        textEn:
          'I think the bicycle is an extremely practical means of transport. Not only is it used for travelling from place to place, but it also greatly improves your health and fitness.',
        textVi:
          'Tôi nghĩ xe đạp là phương tiện giao thông cực kỳ thiết thực. Nó không chỉ dùng để đi lại từ nơi này sang nơi khác mà còn cải thiện đáng kể sức khỏe và thể lực.',
        keywords: ['practical', 'means of transport', 'Not only', 'improves'],
        goldenPhrases: ['practical means of transport', 'Not only is it used..., but it also...']
      },
      {
        id: 'obj_s3',
        blockId: 'object_entity',
        stageNumber: 3,
        stageTitle: 'Stage 3: Benefits',
        textEn:
          'Moreover, riding a bicycle can help you get to work easily, save money, and avoid polluting the environment. Although my bike is not very expensive, I really appreciate it because of these wonderful benefits.',
        textVi:
          'Hơn nữa, đạp xe giúp bạn đi làm dễ dàng, tiết kiệm tiền và tránh gây ô nhiễm môi trường. Mặc dù chiếc xe không đắt lắm, tôi thực sự trân trọng nó vì những lợi ích tuyệt vời này.',
        keywords: ['Moreover', 'save', 'polluting', 'Although', 'appreciate'],
        goldenPhrases: ['Moreover', 'avoid polluting the environment', 'Although']
      },
      {
        id: 'obj_s4',
        blockId: 'object_entity',
        stageNumber: 4,
        stageTitle: 'Stage 4: Conclusion & Influence',
        textEn:
          "It has been my best companion for many years. If it hadn't been for this bike, I wouldn't be as healthy as I am now. I truly hope that riding a bicycle will soon become the main choice of transport for everyone in Hanoi.",
        textVi:
          'Nó là người bạn đồng hành tốt nhất của tôi suốt nhiều năm. Nếu không có chiếc xe này, tôi sẽ không khỏe mạnh như hiện tại. Tôi hy vọng xe đạp sớm trở thành lựa chọn đi lại chính của mọi người ở Hà Nội.',
        keywords: ['companion', "hadn't been", 'healthy', 'main choice'],
        goldenPhrases: ['best companion', "If it hadn't been for this bike, I wouldn't be as healthy as I am now"]
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
    usedFor: 'Đến sớm/đến muộn, chờ đợi, vượt qua thử thách, thay đổi tích cực, dịp hào hứng/mọi người cùng cười, thể thao...',
    stages: [
      {
        id: 'act_s1',
        blockId: 'action_experience',
        stageNumber: 1,
        stageTitle: 'Stage 1: Background',
        textEn:
          'I would like to talk about a bicycle racing competition that I took part in and won. The name of the competition was "Race for Life", and its purpose was to raise money for charity. As far as I remember, it was held when I was in my last year at university, about two years ago.',
        textVi:
          'Tôi muốn nói về giải đua xe đạp mà tôi tham gia và giành chiến thắng mang tên "Race for Life" nhằm gây quỹ từ thiện. Theo như tôi nhớ, giải được tổ chức khi tôi học năm cuối đại học, khoảng hai năm trước.',
        keywords: ['talk', 'racing', 'purpose', 'charity', 'far', 'university'],
        goldenPhrases: ['raise money for charity', 'As far as I remember']
      },
      {
        id: 'act_s2',
        blockId: 'action_experience',
        stageNumber: 2,
        stageTitle: 'Stage 2: The Challenge',
        textEn:
          'If my memory serves me well, I only started training two weeks before the competition. On the day of the race, I was about 15 minutes late because of a terrible traffic jam.',
        textVi:
          'Nếu tôi nhớ không lầm, tôi chỉ mới bắt đầu tập luyện hai tuần trước giải đấu. Vào ngày đua, tôi bị muộn khoảng 15 phút vì một vụ tắc đường kinh khủng.',
        keywords: ['serves', 'training', 'late', 'traffic jam'],
        goldenPhrases: ['If my memory serves me well', 'terrible traffic jam']
      },
      {
        id: 'act_s3',
        blockId: 'action_experience',
        stageNumber: 3,
        stageTitle: 'Stage 3: The Action',
        textEn:
          'Luckily, I was still able to join the race in time. Even though some of my competitors were out of shape or quite old, finishing in first place was still not a piece of cake. It required a lot of physical effort.',
        textVi:
          'May mắn là tôi vẫn kịp tham gia cuộc đua. Mặc dù một số đối thủ không có thể lực tốt hoặc khá lớn tuổi, việc về nhất vẫn không hề dễ dàng chút nào và đòi hỏi rất nhiều nỗ lực thể chất.',
        keywords: ['Luckily', 'Even though', 'shape', 'piece of cake', 'effort'],
        goldenPhrases: ['Even though', 'out of shape', 'not a piece of cake']
      },
      {
        id: 'act_s4',
        blockId: 'action_experience',
        stageNumber: 4,
        stageTitle: 'Stage 4: Result & Reflection',
        textEn:
          "The competition was followed by a really fun party for everyone, which was especially great for me as the winner! If I hadn't had this experience, I wouldn't have such a beautiful memory today. That was definitely the most enjoyable race I've ever taken part in.",
        textVi:
          'Sau cuộc thi là một bữa tiệc thực sự vui vẻ cho tất cả mọi người, đặc biệt tuyệt vời với người chiến thắng là tôi! Nếu không có trải nghiệm này, tôi đã không có kỷ niệm đẹp như hôm nay.',
        keywords: ['followed', 'party', 'winner', "hadn't had", 'memory', 'enjoyable'],
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
    usedFor: 'Cặp đôi hạnh phúc, đám cưới từng tham dự, bữa tiệc ấm cúng, dành thời gian với trẻ nhỏ...',
    stages: [
      {
        id: 'rel_s1',
        blockId: 'relation_ceremony',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          "I would like to talk about a happy couple that I really admire. It is the story of Mr. John and his lovely wife. As I mentioned before, John is one of my father's best friends.",
        textVi:
          'Tôi muốn nói về một cặp đôi hạnh phúc mà tôi thực sự ngưỡng mộ (hoặc đám cưới tuyệt đẹp tôi đã dự). Đó là câu chuyện của chú John và người vợ đáng yêu của chú, bạn thân của bố tôi.',
        keywords: ['talk', 'admire', 'story', 'mentioned', 'best friends'],
        goldenPhrases: ['really admire', 'lovely wife']
      },
      {
        id: 'rel_s2',
        blockId: 'relation_ceremony',
        stageNumber: 2,
        stageTitle: 'Stage 2: The Relationship & Event',
        textEn:
          'They tied the knot many years ago. If my memory serves me well, their wedding anniversary is in autumn. They always organize a cozy party at a modern restaurant to celebrate it. The atmosphere is always joyful and full of laughter.',
        textVi:
          'Họ kết hôn nhiều năm trước. Nếu tôi nhớ không lầm, kỷ niệm ngày cưới của họ vào mùa thu. Họ luôn tổ chức bữa tiệc ấm cúng tại một nhà hàng hiện đại trong bầu không khí ngập tràn niềm vui và tiếng cười.',
        keywords: ['tied the knot', 'serves', 'anniversary', 'cozy', 'atmosphere', 'laughter'],
        goldenPhrases: ['tied the knot', 'If my memory serves me well', 'joyful and full of laughter']
      },
      {
        id: 'rel_s3',
        blockId: 'relation_ceremony',
        stageNumber: 3,
        stageTitle: 'Stage 3: Why They Are Happy',
        textEn:
          "I think they are a perfect match because they have a lot in common. Not only do they share household chores, but they also support each other through thick and thin. They always communicate openly and respect each other's opinions.",
        textVi:
          'Họ là một cặp trời sinh vì có rất nhiều điểm chung. Không chỉ san sẻ việc nhà, họ còn sát cánh bên nhau qua mọi thăng trầm, luôn trò chuyện cởi mở và tôn trọng ý kiến của nhau.',
        keywords: ['match', 'common', 'chores', 'thick and thin', 'openly'],
        goldenPhrases: ['have a lot in common', 'Not only do they..., but they also...', 'through thick and thin']
      },
      {
        id: 'rel_s4',
        blockId: 'relation_ceremony',
        stageNumber: 4,
        stageTitle: 'Stage 4: Feelings & Influence',
        textEn:
          "To me, they are a true role model for a successful marriage. If it hadn't been for their inspiring story, I wouldn't understand the true meaning of love and patience. I truly hope that I can have a wonderful relationship like theirs in the future.",
        textVi:
          'Với tôi, họ là hình mẫu thực sự cho một cuộc hôn nhân viên mãn. Nếu không nhờ câu chuyện truyền cảm hứng của họ, tôi sẽ không hiểu hết ý nghĩa của tình yêu và sự kiên nhẫn.',
        keywords: ['role model', "hadn't been", 'inspiring', 'meaning', 'wonderful'],
        goldenPhrases: ["If it hadn't been for their inspiring story", 'true meaning of love and patience']
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
    usedFor: 'Món ăn nước ngoài, chiếc bánh/bữa ăn đặc biệt, hoặc cắm thêm vào tiệc cưới/tiệc ăn mừng giải đua/nhà hàng!',
    stages: [
      {
        id: 'food_s1',
        blockId: 'food',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          'I would like to talk about a delicious kind of foreign food that I tried recently, which is Korean BBQ.',
        textVi:
          'Tôi muốn nói về một món ăn nước ngoài thơm ngon mà tôi thử gần đây, đó là thịt nướng Hàn Quốc (Korean BBQ).',
        keywords: ['talk', 'foreign food', 'BBQ'],
        goldenPhrases: ['delicious kind of foreign food']
      },
      {
        id: 'food_s2',
        blockId: 'food',
        stageNumber: 2,
        stageTitle: 'Stage 2: Context',
        textEn:
          'If my memory serves me well, I had it a few months ago. I went to a popular Korean restaurant right in the centre of Hanoi with my family to celebrate the weekend.',
        textVi:
          'Nếu tôi nhớ không lầm, tôi đã thưởng thức món này vài tháng trước tại một nhà hàng Hàn Quốc nổi tiếng ngay trung tâm Hà Nội cùng gia đình dịp cuối tuần.',
        keywords: ['serves', 'ago', 'popular', 'centre', 'celebrate'],
        goldenPhrases: ['If my memory serves me well', 'right in the centre of Hanoi']
      },
      {
        id: 'food_s3',
        blockId: 'food',
        stageNumber: 3,
        stageTitle: 'Stage 3: Reasons',
        textEn:
          'We decided to eat there because my friends highly recommended this place. They said the meat there was fresh and the sauce was amazing. Also, we wanted to try something different from our daily Vietnamese meals.',
        textVi:
          'Chúng tôi chọn ăn ở đó vì bạn bè giới thiệu rất nhiệt tình rằng thịt tươi và nước sốt tuyệt hảo, đồng thời cả nhà cũng muốn đổi vị khác bữa cơm Việt hàng ngày.',
        keywords: ['decided', 'recommended', 'fresh', 'sauce', 'different'],
        goldenPhrases: ['highly recommended', 'try something different']
      },
      {
        id: 'food_s4',
        blockId: 'food',
        stageNumber: 4,
        stageTitle: 'Stage 4: Experience & Conclusion',
        textEn:
          "When I tried it, I was completely blown away. The grilled pork wrapped in fresh green leaves tasted fantastic. It was a wonderful dining experience. If I hadn't gone to that restaurant, I wouldn't have known how delicious Korean food is. I definitely want to eat it again in the future.",
        textVi:
          'Khi nếm thử, tôi hoàn toàn choáng ngợp. Thịt nướng cuốn lá xanh tươi ngon tuyệt cú mèo. Nếu không đến nhà hàng đó, tôi đã không biết đồ Hàn ngon đến thế.',
        keywords: ['blown away', 'grilled', 'wrapped', "hadn't gone", 'definitely'],
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
    usedFor: 'Loài cây quan trọng ở Việt Nam, biểu tượng văn hóa, hoặc cắm thêm vào cảnh miền quê/chùa Bái Đính!',
    stages: [
      {
        id: 'plant_s1',
        blockId: 'plant',
        stageNumber: 1,
        stageTitle: 'Stage 1: Introduction',
        textEn:
          'I would like to talk about an important plant in my country, which is the bamboo tree. I have known about this plant since I was a little child. We learned about it in school, and you can easily see bamboo trees everywhere in the countryside of Vietnam.',
        textVi:
          'Tôi muốn nói về một loài cây quan trọng ở nước tôi là cây tre. Tôi biết cây này từ nhỏ qua bài học ở trường, và bạn có thể dễ dàng bắt gặp tre ở khắp làng quê Việt Nam.',
        keywords: ['talk', 'important plant', 'child', 'learned', 'easily see'],
        goldenPhrases: ['since I was a little child', 'countryside of Vietnam']
      },
      {
        id: 'plant_s2',
        blockId: 'plant',
        stageNumber: 2,
        stageTitle: 'Stage 2: Practical Uses',
        textEn:
          'Bamboo is extremely important for several reasons. Firstly, it is a very useful and practical material. People use it to build houses, make furniture, and even create traditional crafts.',
        textVi:
          'Tre cực kỳ quan trọng vì nhiều lý do. Thứ nhất, đó là vật liệu hữu ích và thiết thực để dựng nhà, đóng nội thất và làm đồ thủ công truyền thống.',
        keywords: ['extremely', 'Firstly', 'practical', 'build', 'furniture', 'crafts'],
        goldenPhrases: ['useful and practical material', 'traditional crafts']
      },
      {
        id: 'plant_s3',
        blockId: 'plant',
        stageNumber: 3,
        stageTitle: 'Stage 3: Symbolic Meaning',
        textEn:
          'Secondly, the bamboo tree is a strong symbol of the Vietnamese people. Because it can survive and grow straight in very difficult conditions, it represents the strength and hard work of our nation.',
        textVi:
          'Thứ hai, cây tre là biểu tượng kiên cường của người Việt. Vì có thể sinh tồn và vươn thẳng trong điều kiện khắc nghiệt, tre đại diện cho sức mạnh và sự cần cù của dân tộc.',
        keywords: ['Secondly', 'symbol', 'survive', 'straight', 'difficult', 'strength'],
        goldenPhrases: ['strong symbol of the Vietnamese people', 'survive and grow straight']
      },
      {
        id: 'plant_s4',
        blockId: 'plant',
        stageNumber: 4,
        stageTitle: 'Stage 4: Feelings & Hopes',
        textEn:
          'I really like and respect this plant. Every time I see a bamboo tree, it reminds me of the traditional values of my country. I hope that bamboo will always be protected and valued by future generations.',
        textVi:
          'Tôi thực sự yêu quý và trân trọng loài cây này. Mỗi lần nhìn thấy tre, tôi lại nhớ về những giá trị truyền thống của đất nước và hy vọng thế hệ sau sẽ luôn gìn giữ loài cây ấy.',
        keywords: ['respect', 'reminds', 'traditional values', 'hope', 'protected'],
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
        textVi:
          'Tôi muốn nói về kiểu thời tiết yêu thích của mình là tiết trời mùa thu mát mẻ ở Hà Nội, thường bắt đầu từ tháng 9 và kéo dài đến tháng 11.',
        keywords: ['talk', 'cool', 'starts', 'lasts'],
        goldenPhrases: ['cool autumn weather in Hanoi', 'starts in September and lasts until November']
      },
      {
        id: 'wea_s2',
        blockId: 'weather',
        stageNumber: 2,
        stageTitle: 'Stage 2: Characteristics',
        textEn:
          'In this kind of weather, the temperature is just perfect—not too hot and not too cold. There is usually a gentle breeze and clear blue skies.',
        textVi:
          'Trong tiết trời này, nhiệt độ vô cùng lý tưởng — không quá nóng cũng không quá lạnh, thường có làn gió heo may nhẹ và bầu trời trong xanh.',
        keywords: ['perfect', 'breeze', 'clear blue'],
        goldenPhrases: ['gentle breeze and clear blue skies']
      },
      {
        id: 'wea_s3',
        blockId: 'weather',
        stageNumber: 3,
        stageTitle: 'Stage 3: Activities',
        textEn:
          'Whenever the weather is like this, I love to go for a walk around the lake or sit at a coffee shop with my friends to chat and relax. It is a great time to escape the terrible heat of the summer and the freezing cold of the winter.',
        textVi:
          'Mỗi khi trời thu về, tôi thích đi dạo quanh hồ hoặc ngồi quán cà phê trò chuyện cùng bạn bè, thoát khỏi cái nắng gay gắt mùa hè và cái lạnh buốt giá mùa đông.',
        keywords: ['walk', 'chat', 'escape', 'heat', 'freezing cold'],
        goldenPhrases: ['escape the terrible heat of the summer', 'freezing cold of the winter']
      },
      {
        id: 'wea_s4',
        blockId: 'weather',
        stageNumber: 4,
        stageTitle: 'Stage 4: Influence',
        textEn:
          "This weather brings a lot of positive influences to my life. If it weren't for this beautiful weather, I wouldn't have so much energy to work and study. It always puts me in a good mood and helps me stay productive all day.",
        textVi:
          'Thời tiết này mang lại nhiều ảnh hưởng tích cực cho tôi. Nếu không có tiết trời tuyệt đẹp ấy, tôi sẽ không có nhiều năng lượng học tập và làm việc hiệu quả cả ngày như vậy.',
        keywords: ['positive influences', "weren't for", 'energy', 'mood', 'productive'],
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
    guideVi: 'Đúng chuẩn chiến thuật của thầy Tony: Bọc đề khó (vũ trụ, tranh vẽ, phim, sách, bài giảng) bên ngoài rồi kể ruột Khối Lego quen thuộc!'
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
    hookLogicVi: 'Dùng vỏ bọc đi ăn sinh nhật/kỷ niệm tại nhà hàng Hàn Quốc (Korean BBQ), sau bữa thịt nướng cả nhà bất ngờ mang ra chiếc bánh gạo/bánh kem kỷ niệm đặc biệt!',
    sampleHookEn: "Honestly, a memorable occasion when I had a truly special cake was during a family celebration at a Korean BBQ restaurant, where we ended our meal with a handmade Korean rice cake.",
    sampleClosingEn: 'Having that special cake right after our wonderful Korean BBQ dinner made the whole evening unforgettable for me.'
  },
  {
    num: 3,
    title: 'Describe a couple you know who have a happy marriage',
    cueBullets: ['Who they are', 'How you knew them', 'What they usually do together', 'And explain how you feel about their marriage'],
    recommendedBlockId: 'relation_ceremony',
    recommendedPluginIds: ['person'],
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
    hookLogicVi: 'Dùng Hook "Lớp Vỏ Bọc": Một series phim tài liệu truyền hình tên "The Power of Two Wheels" kể về lịch sử và hành trình đạp xe xuyên Việt, rồi lái mượt vào The Bicycle + Race for Life!',
    sampleHookEn: 'To be honest, my all-time favourite TV series is an inspiring documentary show called "Two Wheels of Life", which explores how the humble bicycle changed the world and even inspired me to ride.',
    sampleClosingEn: 'Watching every episode of that TV series made me fall in love with cycling and live a much healthier lifestyle.'
  },
  {
    num: 5,
    title: 'Describe a work of art that you saw before',
    cueBullets: ['When you first saw this work of art', 'Where you saw it', 'What it looked like', 'And explain your feelings about it.'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: ['weather'],
    hookLogicVi: 'Bẻ lái từ bức tranh sơn dầu phong cảnh Hà Nội treo nổi bật giữa phòng khách/quán cafe sang trọng trên tầng cao Hoàn Kiếm (A Modern Flat)!',
    sampleHookEn: 'Well, a stunning work of art that left a deep impression on me was a colourful oil painting of Hanoi, which I first saw hanging inside a gorgeous modern apartment in Hoan Kiem district.',
    sampleClosingEn: 'That artwork blended so harmoniously with the modern interior that I still picture it clearly whenever I think of great art.'
  },
  {
    num: 6,
    title: 'Describe a plan you haven’t done yet',
    cueBullets: ['What is about', 'When you plan to do it', 'Why do you want to do it', 'And explain why you haven’t done it'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['object_entity'],
    hookLogicVi: 'Bẻ lái sang kế hoạch đăng ký giải đua xe từ thiện "Race for Life" mùa tới (hoặc sở hữu căn hộ Modern Flat) — chưa làm được vì bận ôn thi đại học/IELTS!',
    sampleHookEn: "Actually, one exciting personal plan I haven't been able to carry out yet because of my busy exam schedule is competing again in a charity cycling tournament called 'Race for Life'.",
    sampleClosingEn: 'As soon as I finish my IELTS exam this year, training properly to fulfil this plan will be at the very top of my list.'
  },
  {
    num: 7,
    title: 'Describe an English lesson you have taken',
    cueBullets: ['When it was', 'What it was about', 'What happened', 'And explain why you liked it'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['person'],
    hookLogicVi: 'Lớp vỏ bọc buổi học Speaking đáng nhớ khi thầy giáo yêu cầu kể lại thử thách đáng tự hào nhất bằng tiếng Anh — và em đã kể câu chuyện thắng giải "Race for Life"!',
    sampleHookEn: 'One of the most memorable English lessons I have ever taken was a lively speaking workshop last semester, where our teacher asked each of us to share a real-life challenge—and I told the class about a cycling race I won.',
    sampleClosingEn: 'Being able to tell that exciting personal story fluently in front of everyone made that English lesson truly unforgettable.'
  },
  {
    num: 8,
    title: 'Describe one of your favorite clothing.',
    cueBullets: ['What is it looks like', 'How did you get it', 'Do you often dress it', 'And explain why it is your favorite clothing'],
    recommendedBlockId: 'object_entity',
    recommendedPluginIds: ['action_experience'],
    hookLogicVi: 'Bẻ lái từ chiếc áo thể thao đạp xe (cycling jersey) bố mẹ tặng kèm chiếc xe đạp dịp Tết — rồi triển khai mượt sang lợi ích đạp xe mỗi ngày của khối The Bicycle!',
    sampleHookEn: 'Well, my absolute favourite piece of clothing is a bright blue breathable cycling jersey, which my parents gave me right along with my very first bicycle.',
    sampleClosingEn: 'Every time I put on that jersey and hop on my bike, I feel energetic, comfortable, and ready for the day.'
  },
  {
    num: 9,
    title: 'Describe a time when you received something free',
    cueBullets: ['What it was', 'When and where you got it', 'Why you got it', 'And explain how you felt about it'],
    recommendedBlockId: 'object_entity',
    recommendedPluginIds: [],
    hookLogicVi: 'Bẻ lái cực khớp vào chiếc xe đạp nhận hoàn toàn miễn phí làm quà thưởng Tết / trúng thưởng bốc thăm may mắn ở trường (The Bicycle)!',
    sampleHookEn: 'Honestly, the best time I ever received something completely free was when I got a brand-new bicycle at no cost at all as a surprise Tet gift.',
    sampleClosingEn: 'Even though I did not have to pay a single penny for it, that free bicycle turned out to be the most valuable item I own.'
  },
  {
    num: 10,
    title: 'Describe a time you need to arrive early',
    cueBullets: ['When it was', 'What time you arrived', 'Why you need to arrive early', 'How you felt'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: [],
    hookLogicVi: 'Khớp trực tiếp với Bicycle Racing: Sáng hôm thi "Race for Life" ban tổ chức yêu cầu có mặt sớm để điểm danh & khởi động, nhưng kẹt xe làm em suýt trễ 15 phút!',
    sampleHookEn: 'Well, an unforgettable occasion when I really needed to arrive early was on the morning of a charity bicycle race called "Race for Life", where participants had to check in before the starting whistle.',
    sampleClosingEn: 'That nerve-racking morning taught me a lifelong lesson to always leave home extra early whenever I have an important event.'
  },
  {
    num: 11,
    title: 'Describe an occasion where everybody smiled/laughed.',
    cueBullets: ['What happened', 'When it happened', 'Who were there', 'And explain why everyone smiled/laughed.'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['relation_ceremony'],
    hookLogicVi: 'Kết hợp cực vui giữa buổi tiệc mừng chiến thắng giải đua "Race for Life" (Stage 4 Bicycle Racing) hoặc bữa tiệc kỷ niệm ngày cưới ngập tiếng cười của vợ chồng chú John!',
    sampleHookEn: 'Off the top of my head, a wonderful occasion where literally everybody was smiling and laughing non-stop was the celebration party right after a charity cycling race I joined.',
    sampleClosingEn: 'Seeing every single participant burst into laughter together at the finish-line party still puts a big smile on my face today.'
  },
  {
    num: 12,
    title: 'Describe a favorite sports you watched / a sport you like to watch.',
    cueBullets: ['What it is', 'When you watched it', 'How you watch it', 'And explain why you like watching it'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['object_entity'],
    hookLogicVi: 'Bẻ lái từ đam mê xem đua xe đạp đường trường trên TV sang kỷ niệm trực tiếp tham gia & cổ vũ giải đua từ thiện "Race for Life"!',
    sampleHookEn: 'Actually, the sport I enjoy watching the most is road bicycle racing, and watching it on TV even inspired me to experience a real race first-hand.',
    sampleClosingEn: 'Whether I am watching professional cyclists on screen or cheering at a local race, cycling never fails to thrill me.'
  },
  {
    num: 13,
    title: 'Describe a place where you feel crowded',
    cueBullets: ['Where it is', 'When do you usually go there', 'What you do there', 'And explain why it is crowded'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather'],
    hookLogicVi: 'Khớp ngay Stage 4 của Bai Dinh Temple ("Although there are usually many tourists..."): Chùa Bái Đính cực đông khách hành hương dịp đầu xuân, nhưng khuôn viên rộng mênh mông bên hồ vẫn rất đẹp!',
    sampleHookEn: 'Well, a place that often gets packed with thousands of visitors—especially during festival season—is Bai Dinh temple, though I still love going there.',
    sampleClosingEn: 'So despite the huge crowds of pilgrims and tourists at the entrance, Bai Dinh remains a place I willingly return to.'
  },
  {
    num: 14,
    title: 'Describe an interesting conversation you had with a stranger',
    cueBullets: ['Who the person is', 'What you talked about', 'What kind of person he/she is', 'Why the conversation was interesting'],
    recommendedBlockId: 'person',
    recommendedPluginIds: ['weather'],
    hookLogicVi: 'Bẻ lái về lần đầu tiên gặp chú John ở sân bóng rổ khi em còn nhỏ — lúc đầu chú hoàn toàn là một người lạ bắt chuyện dạy em ném bóng, sau đó mới biết chú là bạn cũ của bố!',
    sampleHookEn: 'Honestly, the most memorable conversation I ever had with a complete stranger happened when I was a kid playing alone, before I found out that this kind stranger—Mr. John—actually knew my dad.',
    sampleClosingEn: 'That chance conversation with a stranger turned into one of the most meaningful mentorships of my entire childhood.'
  },
  {
    num: 15,
    title: 'Describe a helpful person in work or study',
    cueBullets: ['Who it was', 'What this person did', 'How this person helped', 'And explain how you felt after this person helped you'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    hookLogicVi: 'Khớp trực diện với khối Mr. John: Chú John luôn kiên nhẫn kèm cặp, động viên em học tập và dạy em bài học kiên nhẫn khi bố mẹ đi làm bận.',
    sampleHookEn: 'When it comes to someone who helped me tremendously in my studies and personal growth, I immediately think of Mr. John.',
    sampleClosingEn: 'Thanks to his patient guidance in both my schoolwork and life, I became much more confident and disciplined.'
  },
  {
    num: 16,
    title: 'Describe a piece of good news that you received',
    cueBullets: ['What this news was', 'When and where you heard it', 'How you heard it', 'And explain why you think it was good news'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: ['food'],
    hookLogicVi: 'Dùng Hook Tin vui: Anh trai / bố mẹ gọi điện báo tin vui cả nhà vừa mua được (hoặc được mời đến ở tại) một căn hộ hiện đại ngay trung tâm Hoàn Kiếm (A Modern Flat)!',
    sampleHookEn: 'One wonderful piece of good news that thrilled my whole family recently was hearing from my older brother that he had just bought a brand-new apartment in the heart of Hanoi.',
    sampleClosingEn: 'Hearing that fantastic news gave me huge motivation to work hard so I can achieve a milestone like that myself.'
  },
  {
    num: 17,
    title: 'Describe an important plant in your country.',
    cueBullets: ['What the plant is', 'How you know it', 'Why it is important', 'And explain how much you like the plant.'],
    recommendedBlockId: 'plant',
    recommendedPluginIds: ['historical_nature'],
    hookLogicVi: 'Khớp trực diện 100% với Plugin Block 8: The Bamboo (Cây tre Việt Nam)! Nếu muốn nói đủ 2 phút dư dả, có thể cắm thêm cảnh tre mọc quanh chùa Bái Đính.',
    sampleHookEn: 'I would love to talk about an iconic plant that holds a special place in Vietnamese life and culture, which is the bamboo tree.',
    sampleClosingEn: 'In short, bamboo is far more than just a plant in Vietnam—it is the living spirit of our homeland.'
  },
  {
    num: 18,
    title: 'Describe a city that you have visited.',
    cueBullets: ['Where the city is (and its name)', 'When you went there', 'What you liked / disliked about the city', 'And explain why you visited this city.'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: ['weather', 'food'],
    hookLogicVi: 'Ghép Lego kinh điển: Tả chuyến thăm Hà Nội vào mùa thu (Autumn Weather), nghỉ tại căn hộ/quán cafe view cao quận Hoàn Kiếm (Modern Flat) và thưởng thức đồ nướng!',
    sampleHookEn: 'Well, a vibrant city I visited and fell in love with is Hanoi, especially the central Hoan Kiem area where I stayed in an amazing modern flat.',
    sampleClosingEn: 'Between the modern city vibe, the food, and the autumn breeze, visiting Hanoi was an experience I will never forget.'
  },
  {
    num: 19,
    title: 'Describe a time when you moved to a new house or a new school',
    cueBullets: ['When it happened', 'What kind of home did you moved into', 'Why you moved', 'And explain how you felt about the moving'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: [],
    hookLogicVi: 'Đổi nhẹ câu mở đầu của A Modern Flat từ "muốn sở hữu" sang kỷ niệm gia đình chuyển lên căn hộ tầng cao mới tinh ở quận Hoàn Kiếm!',
    sampleHookEn: 'A major milestone I remember vividlly was the time my family moved into a brand-new modern apartment right in the centre of Hanoi.',
    sampleClosingEn: 'Moving into that bright, modern flat brought our whole family closer together and made daily life so much more convenient.'
  },
  {
    num: 20,
    title: 'Describe a leisure activity near or on the sea',
    cueBullets: ['What it is', 'Who do you play with', 'Why you have to prepare', 'And explain how you feel about it'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather'],
    hookLogicVi: 'Bẻ lái khéo sang hoạt động chèo thuyền / tản bộ thư giãn ven vùng cửa biển - sông nước Ninh Bình quanh quần thể Bái Đính trong tiết trời thu mát mẻ!',
    sampleHookEn: 'Whenever I think of a relaxing leisure activity by the water, I immediately picture sightseeing and boating along the scenic coastal riverway leading to the Bai Dinh complex in Ninh Binh.',
    sampleClosingEn: 'Prepared with just a hat, sunscreen, and a camera, spending a breezy day by the water there always recharges my batteries.'
  },
  {
    num: 21,
    title: 'Describe a positive change in your life',
    cueBullets: ['What the change was', 'When it happened', 'How it happened', 'And explain why it was a positive change'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['object_entity'],
    hookLogicVi: 'Ghép đôi hoàn hảo: Quyết định tập đạp xe (The Bicycle) và đăng ký giải đua từ thiện "Race for Life" (Bicycle Racing) đã biến em từ người lười vận động thành người khỏe mạnh, năng động!',
    sampleHookEn: 'Hands down, one of the biggest positive changes in my life was taking up cycling and pushing myself to compete in a charity bicycle race.',
    sampleClosingEn: 'That single decision transformed both my physical stamina and my mindset in the most positive way imaginable.'
  },
  {
    num: 22,
    title: 'Describe an organization or company where you live and they employs a lot of people.',
    cueBullets: ['What it is', 'How many employees work there', 'What its work', 'And explain what you think about it.'],
    recommendedBlockId: 'object_entity',
    recommendedPluginIds: [],
    hookLogicVi: 'Bẻ lái đúng hướng dẫn bài 4: Công ty Xe đạp Thống Nhất tại Hà Nội tạo việc làm cho hàng nghìn công nhân để sản xuất những chiếc xe đạp bền bỉ, xanh sạch (The Bicycle)!',
    sampleHookEn: 'Well, a well-known local company in my city that employs thousands of workers is Thong Nhat, a long-standing Vietnamese manufacturer famous for producing bicycles.',
    sampleClosingEn: 'By creating stable local jobs while promoting green transport, this bicycle company makes a real contribution to our community.'
  },
  {
    num: 23,
    title: 'Describe a happy event from your childhood that you remember well.',
    cueBullets: ['What the event was', 'When and where it happened', 'What you saw or did', 'And explain why you remember this event so well'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['person'],
    hookLogicVi: 'Đổi mốc thời gian giải đua "Race for Life" về thời niên thiếu/cấp 2 (hoặc ghép với kỷ niệm chú John cổ vũ em ở vạch đích)!',
    sampleHookEn: 'Looking back at my childhood, one joyful event that stands out vividly in my mind is a junior charity bicycle race I entered and won when I was a kid.',
    sampleClosingEn: 'Even after all these years, the thrill of winning that childhood race and celebrating with everyone remains crystal clear.'
  },
  {
    num: 24,
    title: 'Describe a person who solved a problem in a clever way',
    cueBullets: ['Who the person is', 'When you meet the person', 'Where do you', 'And explain why do you think the person is clever'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    hookLogicVi: 'Dùng khối Mr. John: Khi em còn nhỏ nhút nhát dễ nản lòng, chú John đã giải quyết tâm lý đó cực khéo bằng cách rủ chơi bóng rổ và giả vờ thua tinh tế để em tự tin lên!',
    sampleHookEn: 'Someone I deeply admire for solving a tricky problem in a very clever and gentle way is Mr. John, who ingeniously helped me overcome my childhood shyness.',
    sampleClosingEn: 'Instead of lecturing me, his clever basketball trick built up my confidence naturally, showing true wisdom.'
  },
  {
    num: 25,
    title: 'Describe an appointment that was put ahead of schedule.',
    cueBullets: ['What this appointment was', 'When it happened', 'Why it was brought forward', 'And explain how you felt about the result.'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: [],
    hookLogicVi: 'Lịch hẹn kiểm tra thể lực & điểm danh của giải đua "Race for Life" bất ngờ bị đẩy sớm lên 30 phút để tránh mưa/nắng, cộng thêm kẹt xe làm em hú vía suýt trễ!',
    sampleHookEn: 'A nerve-racking time when an important appointment was suddenly moved ahead of schedule happened on the morning of my check-in for a charity cycling competition.',
    sampleClosingEn: 'Even though moving the check-in appointment earlier gave me a huge scare in traffic, everything worked out wonderfully in the end.'
  },
  {
    num: 26,
    title: 'Describe a statue or art.',
    cueBullets: ['What it looks like', 'Where you saw it', 'Did you like it', 'And why you think it is special.'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['plant'],
    hookLogicVi: 'Bẻ lái thẳng về pho tượng Phật bằng đồng khổng lồ uy nghiêm đặt trong khuôn viên chùa Bái Đính (Bai Dinh Temple)!',
    sampleHookEn: 'A magnificent statue that left me in awe when I saw it in person is the giant golden bronze Buddha statue inside Bai Dinh temple.',
    sampleClosingEn: 'Standing before that majestic statue amidst the peaceful temple grounds gave me a deep sense of inner calm.'
  },
  {
    num: 27,
    title: 'Describe a bicycle tour.',
    cueBullets: ['When you had this trip', 'Whom went on with you', 'What did you do during this trip', 'And explain why you like it.'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: ['historical_nature', 'weather'],
    hookLogicVi: 'Trúng tủ 100%! Kết hợp hành trình đạp xe gây quỹ "Race for Life" (Bicycle Racing) hoặc đạp xe về vùng quê Ninh Bình (Bai Dinh Temple) dưới trời thu mát mẻ!',
    sampleHookEn: 'Speaking of a memorable bicycle tour, I would love to tell you about an exciting charity cycling ride called "Race for Life" that I joined with my university friends.',
    sampleClosingEn: 'Pedalling together for a good cause and celebrating afterwards made it the best cycling trip of my life.'
  },
  {
    num: 28,
    title: 'Describe a useful website that you often visited.',
    cueBullets: ['What the contents of this website are', 'How you first found this website', 'How often you go to visited this website', 'And explain how this website helps you.'],
    recommendedBlockId: 'object_entity',
    recommendedPluginIds: [],
    hookLogicVi: 'Đúng gợi ý gốc ở bài 4: Trang web cộng đồng yêu xe đạp "VietCycleHub.com" chia sẻ lịch sử xe đạp 1817, mẹo bảo dưỡng và lộ trình đạp xe rèn sức khỏe (The Bicycle)!',
    sampleHookEn: 'A super practical website that I browse almost every week is an online cycling community called "CycleLife.vn", which shares everything about bicycles and healthy living.',
    sampleClosingEn: 'Thanks to all the tips and inspiration on that website, cycling has become an indispensable part of my daily routine.'
  },
  {
    num: 29,
    title: 'Describe an experience you spend your time with a child.',
    cueBullets: ['When you spent time with this child', 'Who this child was', 'What you did together', 'And explain how you felt about it'],
    recommendedBlockId: 'relation_ceremony',
    recommendedPluginIds: ['person'],
    hookLogicVi: 'Dịp dự tiệc kỷ niệm ngày cưới mùa thu của vợ chồng chú John (The Happy Couple), em đã chơi đùa và trông cậu cháu trai nhỏ đáng yêu của hai cô chú (hoặc nhớ lại lúc chú John chơi bóng rổ với chính em thời bé)!',
    sampleHookEn: 'A heartwarming experience I had spending time with a little kid took place during the autumn wedding anniversary party of Mr. John and his wife, where I looked after their energetic little grandson.',
    sampleClosingEn: 'Playing basketball tricks with that little boy reminded me of my own childhood and made the family gathering even sweeter.'
  },
  {
    num: 30,
    title: 'Describe an enjoyable day spent in the countryside',
    cueBullets: ['When and where you went', 'Who you went with', 'What you did there', 'And explain why you think it was enjoyable'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['plant', 'weather'],
    hookLogicVi: 'Combo 3 khối siêu mượt: Một ngày thu mát mẻ (Autumn Weather) về vùng quê Ninh Bình thăm chùa Bái Đính (Bai Dinh Temple) rợp bóng tre xanh (The Bamboo)!',
    sampleHookEn: 'One of the most refreshing days I have ever spent in the countryside was a weekend trip with my friends to rural Ninh Binh province, home to Bai Dinh temple.',
    sampleClosingEn: 'Breathing in the fresh countryside air away from Hanoi’s noise recharged me completely for the week ahead.'
  },
  {
    num: 31,
    title: 'Describe a decision made by that you disagree with',
    cueBullets: ['Who made this decision', 'What it is', 'How you told him/her', 'And explain why you disagree the decision'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    hookLogicVi: 'Dùng khối Mr. John: Quyết định chuyển nhà đi xa của chú John khiến em lúc đó kịch liệt phản đối và buồn rưng rưng vì không muốn xa người thầy/người chú thân thiết (khớp câu "we don\'t live near each other anymore")!',
    sampleHookEn: 'Honestly, a decision made by someone close to me that I initially disagreed with from the bottom of my heart was when my childhood mentor, Mr. John, decided to relocate to a distant city.',
    sampleClosingEn: 'Although I told him back then how much I disagreed with his move, time taught me to respect his choice while cherishing everything he gave me.'
  },
  {
    num: 32,
    title: 'Describe an occasion waiting for something.',
    cueBullets: ['What the situation is', 'When it happened', 'Why you decided to wait', 'And explain how you felt while you were waiting'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: [],
    hookLogicVi: 'Bẻ lái sang 15 phút đứng chờ nhích từng mét trong cảnh tắc đường kinh hoàng sáng hôm thi "Race for Life" (hoặc hồi hộp chờ công bố kết quả người chiến thắng)!',
    sampleHookEn: 'An intense occasion when every minute of waiting felt like an eternity was when I got stuck waiting in traffic right before the start—and later waiting for the winner announcement—of a charity bike race.',
    sampleClosingEn: 'Looking back, refusing to give up during that stressful wait made winning the race taste twice as sweet.'
  },
  {
    num: 33,
    title: 'Describe an interesting house or an apartment you visited.',
    cueBullets: ['Where it was', 'Whose home it was', 'What it looks like', 'And explain why you think it was interesting?'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: [],
    hookLogicVi: 'Khớp trực diện 100% với khối A Modern Flat (ghé thăm căn hộ tầng cao cực hiện đại của người bạn/chú John ở quận Hoàn Kiếm)!',
    sampleHookEn: 'I would love to tell you about a stunning modern apartment I visited recently in Hoan Kiem district, which belongs to a close family friend.',
    sampleClosingEn: 'Stepping inside that stylish flat inspired me to work hard so I can own an apartment just like it one day.'
  },
  {
    num: 34,
    title: 'Describe a kind of foreign food you tried.',
    cueBullets: ['What it was', 'When and where you had it', 'Why you had it', 'And explain how you felt it.'],
    recommendedBlockId: 'food',
    recommendedPluginIds: ['place_service'],
    hookLogicVi: 'Khớp trực diện 100% với Plugin Block 7: Korean BBQ! Có thể gắn thêm 1 Stage tả không gian nhà hàng hiện đại từ A Modern Flat để tròn 2 phút.',
    sampleHookEn: 'Well, when it comes to a mouth-watering foreign cuisine I have tried, Korean BBQ immediately comes to mind.',
    sampleClosingEn: 'All in all, trying authentic Korean BBQ was an unforgettable culinary treat that I cannot wait to repeat.'
  },
  {
    num: 35,
    title: 'Describe an interesting neighbor',
    cueBullets: ['Who this person is', 'How you know this person', 'What this person like to do', 'And explain why you think this neighbor is interesting'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    hookLogicVi: 'Khớp trực diện với bài 1 Mr. John: Chỉ cần giới thiệu chú John vừa là bạn thân của bố vừa là người hàng xóm sống sát vách nhà em hồi nhỏ!',
    sampleHookEn: 'The most fascinating and kind-hearted neighbour I have ever had was Mr. John, who lived right next door to my family when I was growing up.',
    sampleClosingEn: 'Having an interesting and caring neighbour like Mr. John made my childhood neighbourhood feel warm and unforgettable.'
  },
  {
    num: 36,
    title: 'Describe a shop that just opened in your hometown.',
    cueBullets: ['Where the shop is', 'When it opened', 'What it sells', 'And how you feel about the shop?'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: ['food'],
    hookLogicVi: 'Đúng hướng dẫn gốc của A Modern Flat: Thay chữ "flat" thành "a newly opened coffee & pastry shop" nằm trên tầng cao tòa nhà mới ở Hoàn Kiếm với sàn gỗ, sofa da và view thành phố!',
    sampleHookEn: 'Recently, a trendy lifestyle coffee and bakery shop just opened in Hoan Kiem district, and it has quickly become my favourite hangout spot.',
    sampleClosingEn: 'With its modern design, tasty drinks, and panoramic city view, I am sure this new shop will thrive for years.'
  },
  {
    num: 37,
    title: 'Describe a future plan which is not related to work or study',
    cueBullets: ['What the plan is', 'When you thought of the plan', 'Who is involved in the plan', 'And say how you think you will achieve the plan.'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather'],
    hookLogicVi: 'Kế hoạch cá nhân không liên quan học tập/công việc: Tổ chức chuyến đi nghỉ dưỡng tâm linh cuối tuần cùng gia đình về chùa Bái Đính vào mùa thu tới để nạp lại năng lượng!',
    sampleHookEn: 'Speaking of a personal future plan completely unrelated to work or study, I am planning a relaxing autumn weekend getaway with my family to Bai Dinh temple.',
    sampleClosingEn: 'By saving a little pocket money each month and booking transport early, I am confident we will make this refreshing trip happen soon.'
  },
  {
    num: 38,
    title: 'Describe a well-paid job you would like to do in the future.',
    cueBullets: ['What job it is', 'What qualities are required for this job', 'What you would need to learn to get this job', 'And explain why you would like to do this job.'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: [],
    hookLogicVi: 'Bẻ lái cực thông minh: Muốn trở thành Kiến trúc sư nội thất cao cấp (Interior Architect) — đòi hỏi mắt thẩm mỹ & tiếng Anh — để tự tay thiết kế và đủ tài chính mua căn hộ mơ ước A Modern Flat!',
    sampleHookEn: 'In the future, a well-paid profession I aspire to pursue is becoming a senior interior architect, largely because I dream of designing and owning a modern high-rise apartment.',
    sampleClosingEn: 'Working towards that rewarding career gives me clear motivation to master design skills and afford my dream home.'
  },
  {
    num: 39,
    title: 'Describe a book that you would like to read again.',
    cueBullets: ['What the book was about', 'Why you read it the first place', 'What you learned from this book', 'And explain why you would like to read again.'],
    recommendedBlockId: 'object_entity',
    recommendedPluginIds: ['person'],
    hookLogicVi: 'Dùng Hook "Lớp Vỏ Bọc": Cuốn sách "The Story of Two Wheels" viết về lịch sử phát minh xe đạp 1817 và lối sống xanh (hoặc cuốn hồi ký về người thầy kiểu Mr. John)!',
    sampleHookEn: 'A fascinating book that I would love to read all over again is titled "Miracle on Two Wheels", which tells the inspiring history of the bicycle and how it reshaped modern life.',
    sampleClosingEn: 'Re-reading that book always reminds me to appreciate simple, sustainable things like my trusty bicycle.'
  },
  {
    num: 40,
    title: 'Describe a kind of weather that you like',
    cueBullets: ['What it is', 'What you usually do in this kind of weather', 'How you felt about it', 'And explain what influences it may bring to you'],
    recommendedBlockId: 'weather',
    recommendedPluginIds: ['historical_nature'],
    hookLogicVi: 'Khớp trực diện 100% với Plugin Block 9: Autumn Weather (Thời tiết mùa thu Hà Nội)! Có thể cắm thêm 1 Stage đi dạo hồ chùa Bái Đính để câu chuyện thêm dày dặn.',
    sampleHookEn: 'Without a doubt, the kind of weather I adore the most is the crisp, cool autumn weather in Hanoi.',
    sampleClosingEn: 'Whenever autumn arrives with its gentle breeze, I feel happier, calmer, and more inspired than at any other time of year.'
  },
  {
    num: 41,
    title: 'Describe an interesting talk or speech you heard recently.',
    cueBullets: ['Who was the person you talk to', 'Where and when you talked with this person', 'What you talked about with this person', 'And explain why it was interesting?'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    hookLogicVi: 'Bẻ lái sang buổi trò chuyện/bài chia sẻ truyền cảm hứng về lòng kiên nhẫn và sự thấu cảm mà chú John (Mr. John) kể cho em nghe gần đây!',
    sampleHookEn: 'Recently, I had an unforgettable heart-to-heart talk—almost like a mini life speech—with Mr. John about patience, kindness, and our old childhood memories.',
    sampleClosingEn: 'Every word he shared in that talk stayed with me and reminded me why he has always been my greatest role model.'
  },
  {
    num: 42,
    title: 'Describe a famous person in your country.',
    cueBullets: ['Who this person is', 'How you know this person', 'What this person famous for', 'And explain why you like this person.'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    hookLogicVi: 'Nâng cấp nhẹ thân thế chú John trong câu Hook: Ông là một cựu tuyển thủ bóng rổ nổi tiếng ở Việt Nam nhưng ngoài đời lại vô cùng giản dị và từng chăm sóc em hồi nhỏ!',
    sampleHookEn: 'Well, a famous figure in my country whom I admire deeply—and was lucky enough to know personally through my father—is a former national basketball star named John.',
    sampleClosingEn: 'Despite his fame on the basketball court, his humility and kindness in real life are what make me respect him the most.'
  },
  {
    num: 43,
    title: 'Describe a café or restaurant you enjoy.',
    cueBullets: ['Where it is', 'Where it is like there', 'How often you go there', 'And explain why you enjoy going there.'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: ['food'],
    hookLogicVi: 'Combo đỉnh cao: Tả không gian hiện đại tầng cao Hoàn Kiếm của A Modern Flat + đồ ăn ngon xuất sắc của Korean BBQ!',
    sampleHookEn: 'My absolute favourite place to dine and unwind with friends is a modern rooftop café-restaurant right in Hoan Kiem district.',
    sampleClosingEn: 'With its airy modern vibe, city views, and mouth-watering food, it is easily the place I enjoy visiting most on weekends.'
  },
  {
    num: 44,
    title: 'Describe a polite person you met.',
    cueBullets: ['Who this person was', 'When and where you met this person', 'How you met', 'And explain why you think he or she was polite.'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    hookLogicVi: 'Khớp hoàn hảo với Mr. John ("a very gentle and kind man", luôn nhẫn nại, lịch thiệp và nhường nhịn trẻ nhỏ).',
    sampleHookEn: 'When I think of the most polite and well-mannered person I have ever met, Mr. John immediately comes to mind.',
    sampleClosingEn: 'His gentle manners and genuine respect for everyone—even a little kid like me—taught me what true politeness means.'
  },
  {
    num: 45,
    title: 'Describe a popular place where people go swimming.',
    cueBullets: ['Where it is', 'What it looks like', 'What kind of people usually go there', 'And explain why people like to go there.'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather'],
    hookLogicVi: 'Bẻ lái sang khu hồ bơi sinh thái / bến sông trong vắt nằm ngay cạnh quần thể danh thắng chùa Bái Đính (Ninh Bình) nơi du khách và người dân thích bơi lội, thư giãn!',
    sampleHookEn: 'A popular scenic spot where many families and travellers love to go for a refreshing swim is an eco-lagoon right beside the famous Bai Dinh complex in Ninh Binh.',
    sampleClosingEn: 'Swimming in cool clean water surrounded by peaceful traditional scenery is why people flock there every summer and autumn.'
  },
  {
    num: 46,
    title: 'Describe a trip you plan to take in the near future.',
    cueBullets: ['Where you plan to go', 'Who you plan to go with', 'How you plan to travel', 'And explain what you plan to see and do on this trip'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather', 'food'],
    hookLogicVi: 'Đúng ví dụ số 1 trong bài Bai Dinh Temple ("Sử dụng cho: Chuyến đi tương lai")! Ghép Bai Dinh Temple + Autumn Weather là ra bài nói 2 phút hoàn hảo!',
    sampleHookEn: 'In the near future, right after my upcoming exams, I am planning to take a short road trip with my close friends to Bai Dinh temple in Ninh Binh.',
    sampleClosingEn: 'I am counting down the days until this trip because I know it will be the perfect way for us to unwind.'
  },
  {
    num: 47,
    title: 'Describe a time you were not allowed to use your mobile phone.',
    cueBullets: ['When and where it was', 'Why you were not allowed to use your phone', 'What you wanted to use your phone for', 'And explain how you felt about not being able to use your phone.'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: [],
    hookLogicVi: 'Bẻ lái cực tự nhiên vào Bai Dinh Temple: Khi bước vào chánh điện trang nghiêm của chùa Bái Đính, du khách bắt buộc tắt điện thoại (dù em định mở máy chụp ảnh), nhờ vậy em lại tận hưởng trọn vẹn sự tĩnh lặng!',
    sampleHookEn: 'A memorable time when I was strictly not allowed to use my mobile phone was when I stepped inside the sacred main hall of Bai Dinh temple.',
    sampleClosingEn: 'Surprisingly, putting my phone away turned out to be a blessing because it let me truly soak in the peaceful spiritual atmosphere.'
  },
  {
    num: 48,
    title: 'Describe an occasion that you feel excited.',
    cueBullets: ['What it is', 'Where you can do it', 'How you do it', 'And explain why you feel excited'],
    recommendedBlockId: 'action_experience',
    recommendedPluginIds: [],
    hookLogicVi: 'Khớp trực diện với cảm giác hồi hộp vỡ òa khi bứt tốc về nhất và dự bữa tiệc mừng chiến thắng giải đua xe từ thiện "Race for Life" (Bicycle Racing)!',
    sampleHookEn: 'One of the most thrilling occasions when my heart was pounding with excitement was the day I competed in and won a charity cycling race.',
    sampleClosingEn: 'Even today, recalling the cheers at the finish line brings back that exact rush of pure excitement.'
  },
  {
    num: 49,
    title: 'Describe a quiet place you visited.',
    cueBullets: ['Where it was', 'When you went there', 'What you did there', 'And explain why you think it was quite'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather'],
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
    hookLogicVi: 'Biến nhẹ nhân vật chú John thành "Uncle John — em trai ruột/anh họ của bố" trong gia đình! Vẫn giữ nguyên 100% tính cách ấm áp, cao 6 feet, chơi bóng rổ và hôn nhân hạnh phúc.',
    sampleHookEn: 'A beloved family member whom I am immensely proud of is my Uncle John, my father’s cousin who practically helped raise me.',
    sampleClosingEn: 'Seeing how kind, patient, and respected Uncle John is makes me truly proud to be part of his family.'
  },
  {
    num: 51,
    title: 'A wedding you have been to',
    cueBullets: ['Where it was', 'Who you went with', 'What you saw', 'And how you felt about the wedding?'],
    recommendedBlockId: 'relation_ceremony',
    recommendedPluginIds: ['food', 'weather'],
    hookLogicVi: 'Khớp trực diện với khối 6 The Happy Couple (đám cưới/lễ kỷ niệm cưới vàng của chú John vào mùa thu) + cắm thêm món ăn ngon từ Korean BBQ hoặc không gian từ Modern Flat!',
    sampleHookEn: 'One of the warmest and most joyful weddings—actually a milestone wedding renewal ceremony—I have ever attended was held for Mr. John and his lovely wife.',
    sampleClosingEn: 'Attending that heartwarming celebration left me with unforgettable memories of love, family, and happiness.'
  },
  {
    num: 52,
    title: 'Describe an occasion that you received a good service from a company or shop',
    cueBullets: ['What the service was', 'When and where you received the service', 'Whom you were together with', 'And explain why you think it was a good service'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: ['food'],
    hookLogicVi: 'Kết hợp không gian quán cafe/nhà hàng tầng cao Hoàn Kiếm (A Modern Flat) với dịch vụ chu đáo, đồ ăn xuất sắc (Korean BBQ) khi đi cùng gia đình!',
    sampleHookEn: 'An occasion when I was genuinely impressed by top-notch customer service was during a weekend visit with my family to a newly opened rooftop lounge and restaurant in Hoan Kiem.',
    sampleClosingEn: 'Because the staff were so attentive inside such a comfortable modern space, I have recommended their service to all my friends.'
  },
  {
    num: 53,
    title: 'Describe a place you would like to visit in space 🚀',
    cueBullets: ['Where it is', 'What it looks like', 'What you would do there', 'And explain why you want to visit this place.'],
    recommendedBlockId: 'place_service',
    recommendedPluginIds: [],
    hookLogicVi: 'Tuyệt chiêu "Lớp Vỏ Bọc" đúng chuẩn thầy Tony: Bọc ngoài bằng một Trạm khách sạn không gian xoay quanh Trái Đất, còn bên trong được thiết kế tiện nghi ấm cúng y hệt căn hộ A Modern Flat (sàn gỗ, sofa êm, cửa sổ lớn ngắm Trái Đất thay vì ngắm phố)!',
    sampleHookEn: 'To tell you the truth, if space tourism becomes affordable one day, I would love to visit an orbital space hotel designed just like a cozy, ultra-modern apartment floating above Earth.',
    sampleClosingEn: 'Experiencing zero gravity inside a comfortable modern living space with a view of our blue planet would be a dream come true.'
  },
  {
    num: 54,
    title: 'Describe a movie or documentary about space 🚀',
    cueBullets: ['What it is', 'When you watched it', 'What it is about', 'And explain why you liked it.'],
    recommendedBlockId: 'person',
    recommendedPluginIds: [],
    hookLogicVi: 'Tuyệt chiêu "Lớp Vỏ Bọc": Bộ phim về vũ trụ mang tên "Beyond the Stars" không khô khan kỹ thuật mà kể câu chuyện đầy xúc động về cựu phi hành gia tên Mr. John và cậu bé ông dìuắt — rồi lắp trọn khối Mr. John!',
    sampleHookEn: 'Honestly, I am not a huge sci-fi geek, but I was deeply moved by a space movie called "Beyond the Stars", because at its heart it tells the touching story of a retired astronaut named Mr. John.',
    sampleClosingEn: 'By blending outer-space visuals with such a human story of mentorship, that film became my favourite movie about space.'
  },
  {
    num: 55,
    title: 'Describe a time you looked at the sky or stars 🚀',
    cueBullets: ['When it was', 'Who you were with', 'What you saw', 'And explain how you felt about it.'],
    recommendedBlockId: 'historical_nature',
    recommendedPluginIds: ['weather'],
    hookLogicVi: 'Ghép 2 khối cực thơ mộng: Chuyến đi Bái Đính Ninh Bình (Bai Dinh Temple) vào một tối mùa thu trời trong xanh gió mát (Autumn Weather), ngồi bên hồ ngước nhìn bầu trời đầy sao không bị ánh đèn thành phố che khuất!',
    sampleHookEn: 'An unforgettable evening when I gazed up at a breathtaking starry sky happened during an autumn trip to the peaceful countryside around Bai Dinh temple in Ninh Binh.',
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

export function findSpk2PromptMeta(topicText: string, promptNum?: number): Spk2PromptItem {
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
  if (normTarget) {
    const exact = SPK2_PROMPTS_55.find((p) => normalizeSpkTopic(p.title) === normTarget);
    if (exact) return exact;

    const partial = SPK2_PROMPTS_55.find((p) => {
      const np = normalizeSpkTopic(p.title);
      return np.includes(normTarget) || normTarget.includes(np);
    });
    if (partial) return partial;
  }

  // Fallback for any custom Part 2 prompt
  const lower = normTarget;
  let blockId: Spk2BlockId = 'action_experience';
  if (/\b(person|stranger|neighbor|neighbour|friend|family|teacher|polite|famous)\b/.test(lower)) {
    blockId = 'person';
  } else if (/\b(couple|wedding|marriage|child)\b/.test(lower)) {
    blockId = 'relation_ceremony';
  } else if (/\b(food|meal|cake|dish|dinner)\b/.test(lower)) {
    blockId = 'food';
  } else if (/\b(plant|tree|flower|crop)\b/.test(lower)) {
    blockId = 'plant';
  } else if (/\b(weather|season|climate)\b/.test(lower)) {
    blockId = 'weather';
  } else if (/\b(quiet|temple|historical|countryside|statue|trip|river|sea|sky|star)\b/.test(lower)) {
    blockId = 'historical_nature';
  } else if (/\b(house|flat|apartment|shop|cafe|restaurant|city|service|news|job)\b/.test(lower)) {
    blockId = 'place_service';
  } else if (/\b(invention|object|gift|free|clothing|website|company|book|series)\b/.test(lower)) {
    blockId = 'object_entity';
  }

  const block = getSpk2BlockById(blockId);
  return {
    num: 0,
    title: topicText || 'Describe a memorable topic in IELTS Speaking Part 2',
    cueBullets: ['What/Who it is', 'When and where it happened', 'Key details & story', 'And explain how you felt about it'],
    recommendedBlockId: blockId,
    recommendedPluginIds: ['weather'],
    hookLogicVi: `Đề này có thể bẻ lái tự nhiên về khối ${block.name} bằng 1-2 câu dẫn mở đầu rồi chốt lại đúng từ khóa đề bài ở cuối.`,
    sampleHookEn: `Well, when it comes to ${topicText.replace(/^Describe\s+/i, '').replace(/\.$/, '')}, the very first story that springs to my mind connects directly to ${block.name.split(' (')[0]}.`,
    sampleClosingEn: `All in all, that is why this experience immediately came to my mind when I saw the topic.`
  };
}
