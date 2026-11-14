// ============================================================================
// IELTS WRITING TASK 1 — BẢNG TỪ VỰNG XU HƯỚNG & CẤP ĐỘ + 8 KHUNG BẤT BIẾN
// ============================================================================

export type Wt1FrameworkId =
  | 'dynamic'
  | 'static'
  | 'mixed'
  | 'process'
  | 'outdoor_map'
  | 'indoor_map'
  | 'evolution_diagram'
  | 'bio_diagram';

export type Wt1VocabGroupKey =
  | 'up'
  | 'down'
  | 'stable'
  | 'fluctuate'
  | 'peak_low'
  | 'future'
  | 'static_share'
  | 'approx_fraction'
  | 'map_outdoor'
  | 'map_indoor'
  | 'process_seq';

export interface Wt1TrendItem {
  id: string;
  group: 'up' | 'down' | 'stable' | 'fluctuate' | 'peak_low' | 'future';
  verbPast: string;
  verbPresent: string;
  verbBase: string;
  nounForm?: string;
  vi: string;
  isExtreme?: boolean; // e.g., surged/soared/plummeted -> DO NOT pair with dramatically/sharply
  sampleCollocation: string;
}

export interface Wt1DegreeModifier {
  id: string;
  intensity: 'rapid_huge' | 'moderate_steady' | 'slight_small';
  adjective: string;
  adverb: string;
  article: 'a' | 'an';
  vi: string;
  exampleVerbAdv: string;
  exampleAdjNoun: string;
}

export interface Wt1PhraseChip {
  phrase: string;
  vi: string;
  note?: string;
}

export interface Wt1Token {
  type: 'text' | 'vocab_slot' | 'data_slot';
  text?: string;
  slotKey?: string;
  label?: string;
  placeholder?: string;
  vocabPresetGroup?:
    | 'trend_up_phrase'
    | 'trend_down_phrase'
    | 'trend_any_phrase'
    | 'trend_overview_dir'
    | 'static_rank_verb'
    | 'static_share_verb'
    | 'process_type'
    | 'process_intro_verb'
    | 'map_change_verb'
    | 'map_compass'
    | 'map_indoor_pos'
    | 'diagram_adj';
  quickChips?: string[];
}

export interface Wt1ParagraphTemplate {
  key: 'intro' | 'overview' | 'body1' | 'body2';
  title: string;
  viHint: string;
  accentColor: string;
  tokens: Wt1Token[];
}

export interface Wt1FrameworkDef {
  id: Wt1FrameworkId;
  shortBadge: string;
  name: string;
  viSubtitle: string;
  signalCue: string;
  tenseRule: string;
  goldenTips: string[];
  recommendedVocabTab: 'trends' | 'degrees' | 'static' | 'process_map';
  paragraphs: Wt1ParagraphTemplate[];
}

// ============================================================================
// 1. BẢNG ĐỘNG TỪ & DANH TỪ CHỈ XU HƯỚNG (ĐI LÊN / ĐI XUỐNG / GIỮ NGUYÊN / DAO ĐỘNG)
// ============================================================================
export const WT1_TREND_ITEMS: Wt1TrendItem[] = [
  // --- ĐI LÊN (UPWARD) ---
  {
    id: 'up_climb',
    group: 'up',
    verbPast: 'climbed up',
    verbPresent: 'climbs up',
    verbBase: 'climb up',
    nounForm: 'climb',
    vi: 'leo lên / tăng lên',
    sampleCollocation: 'climbed up steadily to 75%'
  },
  {
    id: 'up_rise',
    group: 'up',
    verbPast: 'rose',
    verbPresent: 'rises',
    verbBase: 'rise',
    nounForm: 'rise',
    vi: 'tăng lên',
    sampleCollocation: 'rose dramatically from 20 to 65 million'
  },
  {
    id: 'up_increase',
    group: 'up',
    verbPast: 'increased',
    verbPresent: 'increases',
    verbBase: 'increase',
    nounForm: 'increase',
    vi: 'gia tăng (phổ biến, học thuật)',
    sampleCollocation: 'experienced a significant increase to 120 units'
  },
  {
    id: 'up_grow',
    group: 'up',
    verbPast: 'grew',
    verbPresent: 'grows',
    verbBase: 'grow',
    nounForm: 'growth',
    vi: 'tăng trưởng',
    sampleCollocation: 'witnessed a steady growth over the decade'
  },
  {
    id: 'up_goup',
    group: 'up',
    verbPast: 'went up',
    verbPresent: 'goes up',
    verbBase: 'go up',
    nounForm: 'upward trend',
    vi: 'đi lên / xu hướng tăng',
    sampleCollocation: 'went up moderately by 15%'
  },
  {
    id: 'up_surge',
    group: 'up',
    verbPast: 'surged',
    verbPresent: 'surges',
    verbBase: 'surge',
    nounForm: 'surge',
    vi: 'tăng vọt mạnh mẽ (KHÔNG thêm dramatically)',
    isExtreme: true,
    sampleCollocation: 'surged to a peak of 95 billion minutes'
  },
  {
    id: 'up_soar',
    group: 'up',
    verbPast: 'soared',
    verbPresent: 'soars',
    verbBase: 'soar',
    nounForm: 'jump',
    vi: 'tăng vút / nhảy vọt (KHÔNG thêm sharply)',
    isExtreme: true,
    sampleCollocation: 'soared from 12% to nearly 60%'
  },
  {
    id: 'up_rocket',
    group: 'up',
    verbPast: 'rocketed',
    verbPresent: 'rockets',
    verbBase: 'rocket',
    vi: 'tăng phi mã (KHÔNG thêm trạng từ mạnh)',
    isExtreme: true,
    sampleCollocation: 'rocketed to 500,000 users in 2020'
  },

  // --- ĐI XUỐNG (DOWNWARD) ---
  {
    id: 'down_fall',
    group: 'down',
    verbPast: 'fell',
    verbPresent: 'falls',
    verbBase: 'fall',
    nounForm: 'fall',
    vi: 'giảm xuống / rơi xuống',
    sampleCollocation: 'fell sharply to just 10%'
  },
  {
    id: 'down_drop',
    group: 'down',
    verbPast: 'dropped',
    verbPresent: 'drops',
    verbBase: 'drop',
    nounForm: 'drop',
    vi: 'sụt giảm',
    sampleCollocation: 'experienced a dramatic drop to 18 tonnes'
  },
  {
    id: 'down_decline',
    group: 'down',
    verbPast: 'declined',
    verbPresent: 'declines',
    verbBase: 'decline',
    nounForm: 'decline',
    vi: 'suy giảm (rất học thuật)',
    sampleCollocation: 'declined gradually throughout the period'
  },
  {
    id: 'down_decrease',
    group: 'down',
    verbPast: 'decreased',
    verbPresent: 'decreases',
    verbBase: 'decrease',
    nounForm: 'decrease',
    vi: 'giảm bớt',
    sampleCollocation: 'saw a slight decrease from 45% to 41%'
  },
  {
    id: 'down_dip',
    group: 'down',
    verbPast: 'dipped',
    verbPresent: 'dips',
    verbBase: 'dip',
    nounForm: 'dip',
    vi: 'hạ nhẹ tạm thời (rồi thường tăng lại)',
    sampleCollocation: 'dipped slightly to 30% in 2005 before recovering'
  },
  {
    id: 'down_plunge',
    group: 'down',
    verbPast: 'plunged',
    verbPresent: 'plunges',
    verbBase: 'plunge',
    nounForm: 'plunge',
    vi: 'lao dốc mạnh (KHÔNG thêm dramatically)',
    isExtreme: true,
    sampleCollocation: 'plunged to a record low of 4%'
  },
  {
    id: 'down_plummet',
    group: 'down',
    verbPast: 'plummeted',
    verbPresent: 'plummets',
    verbBase: 'plummet',
    nounForm: 'slump',
    vi: 'rơi thẳng đứng / sụt thê thảm (KHÔNG thêm sharply)',
    isExtreme: true,
    sampleCollocation: 'plummeted from 80,000 to under 15,000'
  },

  // --- GIỮ NGUYÊN / ỔN ĐỊNH (STABILITY) ---
  {
    id: 'stable_remain',
    group: 'stable',
    verbPast: 'remained stable at',
    verbPresent: 'remains stable at',
    verbBase: 'remain stable at',
    nounForm: 'stability',
    vi: 'giữ ổn định ở mức',
    sampleCollocation: 'remained relatively stable at around 25%'
  },
  {
    id: 'stable_unchanged',
    group: 'stable',
    verbPast: 'remained unchanged at',
    verbPresent: 'remains unchanged at',
    verbBase: 'remain unchanged at',
    nounForm: 'no significant change',
    vi: 'giữ nguyên không đổi ở mức',
    sampleCollocation: 'remained unchanged at 50 million tonnes'
  },
  {
    id: 'stable_constant',
    group: 'stable',
    verbPast: 'stayed constant at',
    verbPresent: 'stays constant at',
    verbBase: 'stay constant at',
    vi: 'duy trì cố định ở mức',
    sampleCollocation: 'stayed constant at 12% over the next five years'
  },
  {
    id: 'stable_level',
    group: 'stable',
    verbPast: 'leveled off at',
    verbPresent: 'levels off at',
    verbBase: 'level off at',
    vi: 'chững lại / đi ngang ở mức (sau khi tăng hoặc giảm)',
    sampleCollocation: 'leveled off at approximately 40% until 2010'
  },
  {
    id: 'stable_plateau',
    group: 'stable',
    verbPast: 'reached a plateau of',
    verbPresent: 'reaches a plateau of',
    verbBase: 'reach a plateau of',
    nounForm: 'plateau',
    vi: 'đi ngang trên vùng đỉnh ở mức',
    sampleCollocation: 'reached a plateau of 90% in the final decade'
  },

  // --- DAO ĐỘNG (FLUCTUATION) ---
  {
    id: 'fluc_around',
    group: 'fluctuate',
    verbPast: 'fluctuated around',
    verbPresent: 'fluctuates around',
    verbBase: 'fluctuate around',
    nounForm: 'fluctuation',
    vi: 'dao động lên xuống quanh mốc',
    sampleCollocation: 'fluctuated mildly around 35% throughout the period'
  },
  {
    id: 'fluc_between',
    group: 'fluctuate',
    verbPast: 'fluctuated between',
    verbPresent: 'fluctuates between',
    verbBase: 'fluctuate between',
    vi: 'dao động trong khoảng [X] and [Y]',
    sampleCollocation: 'fluctuated wildly between 15% and 28%'
  },
  {
    id: 'fluc_hover',
    group: 'fluctuate',
    verbPast: 'hovered around',
    verbPresent: 'hovers around',
    verbBase: 'hover around',
    vi: 'quanh quẩn ở mức xấp xỉ',
    sampleCollocation: 'hovered around the 50-mark for a decade'
  },

  // --- CHẠM ĐỈNH & CHẠM ĐÁY (PEAKS & LOWS) ---
  {
    id: 'peak_at',
    group: 'peak_low',
    verbPast: 'peaked at',
    verbPresent: 'peaks at',
    verbBase: 'peak at',
    nounForm: 'peak',
    vi: 'đạt đỉnh cao nhất tại',
    sampleCollocation: 'peaked at 110 billion minutes in 1999'
  },
  {
    id: 'peak_reach',
    group: 'peak_low',
    verbPast: 'reached a peak of',
    verbPresent: 'reaches a peak of',
    verbBase: 'reach a peak of',
    vi: 'chạm mức đỉnh là',
    sampleCollocation: 'reached a peak of 84% before falling back'
  },
  {
    id: 'low_hit',
    group: 'peak_low',
    verbPast: 'hit a low of',
    verbPresent: 'hits a low of',
    verbBase: 'hit a low of',
    nounForm: 'low',
    vi: 'chạm mức thấp nhất là',
    sampleCollocation: 'hit a low of 8% in 2002'
  },
  {
    id: 'low_bottom',
    group: 'peak_low',
    verbPast: 'bottomed out at',
    verbPresent: 'bottoms out at',
    verbBase: 'bottom out at',
    vi: 'chạm đáy tại (trước khi phục hồi)',
    sampleCollocation: 'bottomed out at $120 in March'
  },

  // --- DỰ BÁO TƯƠNG LAI (FUTURE PROJECTIONS) ---
  {
    id: 'fut_projected',
    group: 'future',
    verbPast: 'is projected to',
    verbPresent: 'is projected to',
    verbBase: 'be projected to',
    vi: 'được dự phóng sẽ (+ V nguyên thể)',
    sampleCollocation: 'is projected to climb up steadily to 45 quadrillion units by 2030'
  },
  {
    id: 'fut_expected',
    group: 'future',
    verbPast: 'is expected to',
    verbPresent: 'is expected to',
    verbBase: 'be expected to',
    vi: 'được kỳ vọng / dự kiến sẽ (+ V nguyên thể)',
    sampleCollocation: 'is expected to experience a slight decline to 12%'
  },
  {
    id: 'fut_predicted',
    group: 'future',
    verbPast: 'is predicted to',
    verbPresent: 'is predicted to',
    verbBase: 'be predicted to',
    vi: 'được dự đoán sẽ (+ V nguyên thể)',
    sampleCollocation: 'is predicted to remain unchanged at 20%'
  },
  {
    id: 'fut_forecast',
    group: 'future',
    verbPast: 'is forecast to',
    verbPresent: 'is forecast to',
    verbBase: 'be forecast to',
    vi: 'được dự báo sẽ (forecast giữ nguyên V3)',
    sampleCollocation: 'is forecast to reach 10 million by 2040'
  }
];

// ============================================================================
// 2. BẢNG TRẠNG TỪ & TÍNH TỪ CHỈ CẤP ĐỘ / TỐC ĐỘ (DEGREE & SPEED MODIFIERS)
// ============================================================================
export const WT1_DEGREE_MODIFIERS: Wt1DegreeModifier[] = [
  // --- CẤP ĐỘ 1: MẠNH / ĐỘT NGỘT / RÕ RỆT (RAPID / HUGE) ---
  {
    id: 'deg_dramatic',
    intensity: 'rapid_huge',
    adjective: 'dramatic',
    adverb: 'dramatically',
    article: 'a',
    vi: 'đột ngột, mạnh mẽ, ấn tượng',
    exampleVerbAdv: 'climbed up dramatically to 90%',
    exampleAdjNoun: 'experienced a dramatic increase to 90%'
  },
  {
    id: 'deg_sharp',
    intensity: 'rapid_huge',
    adjective: 'sharp',
    adverb: 'sharply',
    article: 'a',
    vi: 'nhanh và dốc đứng',
    exampleVerbAdv: 'fell sharply from 60% to 15%',
    exampleAdjNoun: 'witnessed a sharp drop to 15%'
  },
  {
    id: 'deg_significant',
    intensity: 'rapid_huge',
    adjective: 'significant',
    adverb: 'significantly',
    article: 'a',
    vi: 'đáng kể, có ý nghĩa lớn (rất an toàn & chuẩn mực)',
    exampleVerbAdv: 'rose significantly over the 10-year period',
    exampleAdjNoun: 'saw a significant rise over the 10-year period'
  },
  {
    id: 'deg_substantial',
    intensity: 'rapid_huge',
    adjective: 'substantial',
    adverb: 'substantially',
    article: 'a',
    vi: 'đáng kể, khối lượng lớn',
    exampleVerbAdv: 'grew substantially to 250 tonnes',
    exampleAdjNoun: 'recorded a substantial growth to 250 tonnes'
  },
  {
    id: 'deg_considerable',
    intensity: 'rapid_huge',
    adjective: 'considerable',
    adverb: 'considerably',
    article: 'a',
    vi: 'đáng kể, nhiều',
    exampleVerbAdv: 'declined considerably by 30%',
    exampleAdjNoun: 'experienced a considerable decline of 30%'
  },
  {
    id: 'deg_rapid',
    intensity: 'rapid_huge',
    adjective: 'rapid',
    adverb: 'rapidly',
    article: 'a',
    vi: 'nhanh chóng (nhấn mạnh tốc độ thời gian)',
    exampleVerbAdv: 'increased rapidly between 2005 and 2008',
    exampleAdjNoun: 'witnessed a rapid increase between 2005 and 2008'
  },
  {
    id: 'deg_steep',
    intensity: 'rapid_huge',
    adjective: 'steep',
    adverb: 'steeply',
    article: 'a',
    vi: 'dốc đứng (hợp với Line Graph)',
    exampleVerbAdv: 'dropped steeply in the final year',
    exampleAdjNoun: 'saw a steep fall in the final year'
  },
  {
    id: 'deg_marked',
    intensity: 'rapid_huge',
    adjective: 'marked',
    adverb: 'markedly',
    article: 'a',
    vi: 'rõ rệt, dễ nhận thấy (Band 7.5+)',
    exampleVerbAdv: 'improved markedly to 78%',
    exampleAdjNoun: 'showed a marked upward trend'
  },

  // --- CẤP ĐỘ 2: ĐỀU ĐẶN / TỪ TỪ / VỪA PHẢI (MODERATE / STEADY) ---
  {
    id: 'deg_steady',
    intensity: 'moderate_steady',
    adjective: 'steady',
    adverb: 'steadily',
    article: 'a',
    vi: 'đều đặn, ổn định theo một hướng',
    exampleVerbAdv: 'climbed up steadily from 20% to 45%',
    exampleAdjNoun: 'experienced a steady rise to 45%'
  },
  {
    id: 'deg_gradual',
    intensity: 'moderate_steady',
    adjective: 'gradual',
    adverb: 'gradually',
    article: 'a',
    vi: 'từ từ, dần dần qua nhiều năm',
    exampleVerbAdv: 'decreased gradually over the two decades',
    exampleAdjNoun: 'saw a gradual decline over the two decades'
  },
  {
    id: 'deg_moderate',
    intensity: 'moderate_steady',
    adjective: 'moderate',
    adverb: 'moderately',
    article: 'a',
    vi: 'ở mức độ vừa phải',
    exampleVerbAdv: 'grew moderately to reach 52%',
    exampleAdjNoun: 'recorded a moderate growth to 52%'
  },
  {
    id: 'deg_consistent',
    intensity: 'moderate_steady',
    adjective: 'consistent',
    adverb: 'consistently',
    article: 'a',
    vi: 'nhất quán, liên tục suốt giai đoạn',
    exampleVerbAdv: 'consistently recorded the highest figures',
    exampleAdjNoun: 'maintained a consistent upward trend'
  },
  {
    id: 'deg_progressive',
    intensity: 'moderate_steady',
    adjective: 'progressive',
    adverb: 'progressively',
    article: 'a',
    vi: 'tiến triển từng bước (Band 7.5+)',
    exampleVerbAdv: 'increased progressively each year',
    exampleAdjNoun: 'witnessed a progressive increase'
  },

  // --- CẤP ĐỘ 3: NHẸ / CHẬM / KHÔNG ĐÁNG KỂ (SLIGHT / SMALL) ---
  {
    id: 'deg_slight',
    intensity: 'slight_small',
    adjective: 'slight',
    adverb: 'slightly',
    article: 'a',
    vi: 'nhẹ, một chút ít',
    exampleVerbAdv: 'rose slightly by 2%',
    exampleAdjNoun: 'saw a slight rise of 2%'
  },
  {
    id: 'deg_marginal',
    intensity: 'slight_small',
    adjective: 'marginal',
    adverb: 'marginally',
    article: 'a',
    vi: 'rất nhẹ, xê xích không đáng kể (Band 7.5+)',
    exampleVerbAdv: 'fell marginally from 31% to 29.5%',
    exampleAdjNoun: 'experienced a marginal drop to 29.5%'
  },
  {
    id: 'deg_minimal',
    intensity: 'slight_small',
    adjective: 'minimal',
    adverb: 'minimally',
    article: 'a',
    vi: 'tối thiểu, rất nhỏ',
    exampleVerbAdv: 'changed minimally during the 1990s',
    exampleAdjNoun: 'recorded a minimal increase of just 1%'
  },
  {
    id: 'deg_modest',
    intensity: 'slight_small',
    adjective: 'modest',
    adverb: 'modestly',
    article: 'a',
    vi: 'khiêm tốn, vừa phải nhỏ',
    exampleVerbAdv: 'grew modestly to 18 million',
    exampleAdjNoun: 'witnessed a modest climb to 18 million'
  },
  {
    id: 'deg_fractional',
    intensity: 'slight_small',
    adjective: 'fractional',
    adverb: 'fractionally',
    article: 'a',
    vi: 'chỉ nhích một phần cực nhỏ (Band 8.0)',
    exampleVerbAdv: 'dipped fractionally to 9.8%',
    exampleAdjNoun: 'saw a fractional decrease to 9.8%'
  }
];

// ============================================================================
// 3. TỪ VỰNG SO SÁNH TĨNH, PHÂN SỐ/XẤP XỈ, PROCESS & MAPS
// ============================================================================
export const WT1_STATIC_SHARE_CHIPS: Wt1PhraseChip[] = [
  { phrase: 'accounted for', vi: 'chiếm (tỷ trọng %)', note: 'Chuẩn nhất cho Pie / Table %' },
  { phrase: 'made up', vi: 'tạo nên / chiếm', note: 'Tự nhiên, tránh lặp accounted for' },
  { phrase: 'constituted', vi: 'cấu thành / chiếm (Band 7.5+)', note: 'Rất học thuật' },
  { phrase: 'comprised', vi: 'bao gồm / chiếm (LƯU Ý: KHÔNG viết comprised of ở chủ động)', note: 'Band 7.5+' },
  { phrase: 'represented', vi: 'đại diện cho / chiếm', note: 'Đa năng cho cả % và con số' },
  { phrase: 'stood at', vi: 'đứng ở mức (dùng trước số liệu cụ thể)', note: 'Dùng tốt cho cả Dynamic & Static' },
  { phrase: 'ranked first, standing at', vi: 'xếp thứ nhất, đứng ở mức', note: 'Mở đầu Body 1 cực mượt' },
  { phrase: 'topped the chart at', vi: 'dẫn đầu bảng/biểu đồ ở mức', note: 'Band 7.5+' },
  { phrase: 'was almost double / triple that of', vi: 'gấp gần đôi / gấp ba số liệu của', note: 'Ăn điểm so sánh gấp bội' },
  { phrase: 'lagged far behind at only', vi: 'tụt lại khá xa phía sau chỉ với', note: 'Tả nhóm thấp nhất rất hay' }
];

export const WT1_APPROX_FRACTION_CHIPS: Wt1PhraseChip[] = [
  { phrase: 'approximately / roughly / around', vi: 'xấp xỉ / khoảng chừng (VD: ~31%)', note: 'Đặt ngay trước con số' },
  { phrase: 'just over / slightly above', vi: 'nhỉnh hơn một chút (VD: 51% → just over half)', note: 'Band 7.5+ paraphrase số' },
  { phrase: 'just under / nearly / almost', vi: 'gần chạm mức / xấp xỉ dưới (VD: 49% → nearly half)', note: 'Rất tự nhiên' },
  { phrase: 'exactly a quarter (25%) / a third (33%)', vi: 'đúng 1/4 (25%) / 1/3 (33%)', note: 'Đổi % sang phân số ăn điểm LR' },
  { phrase: 'two-fifths (40%) / three-quarters (75%)', vi: '2/5 (40%) / 3/4 (75%)', note: 'Nhớ có gạch nối khi tử số ≥ 2' },
  { phrase: 'the vast majority (around 75%–85%)', vi: 'đại đa số', note: 'Dùng cho nhóm áp đảo' },
  { phrase: 'a mere / a tiny fraction of (under 5%)', vi: 'chỉ một phần nhỏ vỏn vẹn', note: 'Dùng cho nhóm 1%–4%' }
];

export const WT1_PROCESS_MAP_CHIPS: Record<'process' | 'outdoor_map' | 'indoor_map', Wt1PhraseChip[]> = {
  process: [
    { phrase: 'At the initial stage, ... is collected / extracted', vi: 'Ở bước đầu tiên, ... được thu gom / khai thác' },
    { phrase: 'Following this, / Subsequently,', vi: 'Tiếp theo đó, / Sau đó,' },
    { phrase: 'Once this step is completed,', vi: 'Ngay khi bước này hoàn tất,' },
    { phrase: 'undergoes a transformation into', vi: 'trải qua sự biến đổi thành (cụm tủ Band 7.5+)' },
    { phrase: 'is filtered / crushed / heated / compressed', vi: 'được lọc / nghiền / đun nóng / nén (Bị động nhân tạo)' },
    { phrase: 'absorbs / releases / grows into', vi: 'hấp thụ / giải phóng / phát triển thành (Chủ động tự nhiên)' },
    { phrase: 'Finally, the process concludes when', vi: 'Cuối cùng, quy trình khép lại khi' }
  ],
  outdoor_map: [
    { phrase: 'in the north / south / east / west of the area', vi: 'ở phía Bắc / Nam / Đông / Tây khu vực' },
    { phrase: 'in the north-west / south-east corner', vi: 'ở góc Tây Bắc / Đông Nam' },
    { phrase: 'was knocked down / demolished to make way for', vi: 'bị phá dỡ để nhường chỗ cho' },
    { phrase: 'trees were chopped down / cleared', vi: 'cây cối bị đốn hạ / giải phóng mặt bằng' },
    { phrase: 'a new ... was constructed / erected / built', vi: 'một ... mới được xây dựng' },
    { phrase: 'was expanded / extended northward', vi: 'được mở rộng / kéo dài về phía Bắc' },
    { phrase: 'was converted / transformed into', vi: 'được chuyển đổi công năng thành' },
    { phrase: 'remained unchanged throughout the period', vi: 'giữ nguyên không thay đổi suốt giai đoạn' }
  ],
  indoor_map: [
    { phrase: 'upon entering the building / room', vi: 'ngay khi bước vào tòa nhà / căn phòng (KHÔNG dùng Đông/Tây/Nam/Bắc)' },
    { phrase: 'on the left-hand / right-hand side of the entrance', vi: 'ở phía tay trái / tay phải lối vào' },
    { phrase: 'in the central area / in the middle of the layout', vi: 'ở khu vực trung tâm mặt bằng' },
    { phrase: 'in the top-right / bottom-left corner', vi: 'ở góc trên bên phải / dưới bên trái' },
    { phrase: 'along the back wall / opposite the reception', vi: 'dọc bức tường phía sau / đối diện quầy lễ tân' },
    { phrase: 'was replaced by / is planned to be replaced by', vi: 'được thay thế bởi (Quá khứ) / dự kiến thay bởi (Tương lai)' },
    { phrase: 'was relocated to / will be moved to', vi: 'được dời sang / sẽ được chuyển tới' }
  ]
};

// ============================================================================
// 4. BỘ 8 KHUNG CẤU TRÚC BẤT BIẾN (ĐÃ RÀ SOÁT & CHUẨN HÓA KẾT NỐI BẢNG TỪ VỰNG)
// ============================================================================
export const WT1_STRUCTURES: Record<Wt1FrameworkId, Wt1FrameworkDef> = {
  dynamic: {
    id: 'dynamic',
    shortBadge: '1. Dynamic (Qua các năm)',
    name: '1. Data Analysis — DYNAMIC (Biến thiên theo thời gian)',
    viSubtitle: 'Có từ 2 mốc năm trở lên (VD: from 1995 to 2002, between 1980 and 2030)',
    signalCue: 'Đề có ≥ 2 mốc thời gian (Line Graph, hoặc Bar / Pie / Table qua nhiều năm).',
    tenseRule:
      'Năm quá khứ → Quá khứ đơn (rose, climbed up, experienced). Có năm tương lai (VD: 2030) → dùng "is projected / expected to + V" cho giai đoạn dự báo.',
    goldenTips: [
      'Luôn ghép ĐỘNG TỪ XU HƯỚNG + TRẠNG TỪ CẤP ĐỘ (VD: climbed up steadily) hoặc EXPERIENCED A + TÍNH TỪ + DANH TỪ (VD: experienced a dramatic surge).',
      'TUYỆT ĐỐI không quên ĐƠN VỊ (%, million, billion minutes, tonnes...) ngay sau số liệu!',
      'Không viết câu kết bài "In conclusion / To sum up" và không đưa ý kiến cá nhân vào Task 1.'
    ],
    recommendedVocabTab: 'trends',
    paragraphs: [
      {
        key: 'intro',
        title: 'Introduction (Mở bài — 1 câu chuẩn xác)',
        viHint: 'Paraphrase tên biểu đồ + chủ đề + khoảng thời gian.',
        accentColor: 'blue',
        tokens: [
          { type: 'text', text: 'The provided ' },
          {
            type: 'data_slot',
            slotKey: 'chart_type',
            label: 'loại biểu đồ',
            placeholder: 'line graph / bar chart / pie charts / table',
            quickChips: ['line graph', 'bar chart', 'pie charts', 'table']
          },
          { type: 'text', text: ' illustrates ' },
          {
            type: 'data_slot',
            slotKey: 'topic_paraphrase',
            label: 'chủ đề đề bài (paraphrase)',
            placeholder: 'VD: how much energy was consumed in the US'
          },
          { type: 'text', text: ' over a ' },
          {
            type: 'data_slot',
            slotKey: 'num_years',
            label: 'số năm',
            placeholder: 'VD: 10'
          },
          { type: 'text', text: '-year period from ' },
          {
            type: 'data_slot',
            slotKey: 'start_year',
            label: 'năm bắt đầu',
            placeholder: 'VD: 2000'
          },
          { type: 'text', text: ' to ' },
          {
            type: 'data_slot',
            slotKey: 'end_year',
            label: 'năm kết thúc',
            placeholder: 'VD: 2010'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'overview',
        title: 'Overview (Tổng quan — 2 câu: Xu hướng chung + Độ lớn cao nhất)',
        viHint: 'KHÔNG nêu số liệu cụ thể ở Overview! Chỉ nêu xu hướng tăng/giảm và đường/nhóm nào cao nhất.',
        accentColor: 'indigo',
        tokens: [
          { type: 'text', text: 'Overall, it is clear that the figures for ' },
          {
            type: 'data_slot',
            slotKey: 'ov_group_up',
            label: 'Nhóm A (hoặc A & B)',
            placeholder: 'VD: cars and buses'
          },
          { type: 'text', text: ' ' },
          {
            type: 'vocab_slot',
            slotKey: 'ov_trend_1',
            label: 'Cụm xu hướng chung 1',
            placeholder: 'witnessed an upward trend',
            vocabPresetGroup: 'trend_overview_dir',
            quickChips: [
              'witnessed an upward trend',
              'experienced a downward trend',
              'increased significantly',
              'remained relatively stable'
            ]
          },
          { type: 'text', text: ', while ' },
          {
            type: 'data_slot',
            slotKey: 'ov_contrast_clause',
            label: 'Nhóm đối lập C',
            placeholder: 'VD: the opposite was true for trains / cycling remained relatively stable',
            quickChips: ['the opposite was true for ', 'the figure for ... remained relatively stable']
          },
          { type: 'text', text: '. In addition, ' },
          {
            type: 'data_slot',
            slotKey: 'ov_highest_item',
            label: 'Đối tượng cao nhất [A]',
            placeholder: 'VD: petrol and oil'
          },
          { type: 'text', text: ' consistently recorded the highest figures throughout the examined period.' }
        ]
      },
      {
        key: 'body1',
        title: 'Body 1 (Nhóm nổi bật / Xu hướng tăng chủ đạo)',
        viHint: 'So sánh điểm xuất phát ở năm đầu, sau đó gắn Cụm [Xu hướng + Cấp độ] + Số liệu kèm Đơn vị.',
        accentColor: 'emerald',
        tokens: [
          { type: 'text', text: 'Looking at the details, in ' },
          {
            type: 'data_slot',
            slotKey: 'b1_start_year',
            label: 'Năm đầu',
            placeholder: 'VD: 2000'
          },
          { type: 'text', text: ', the figure for ' },
          {
            type: 'data_slot',
            slotKey: 'b1_item_a',
            label: 'Đối tượng [A]',
            placeholder: 'VD: local fixed-line calls'
          },
          { type: 'text', text: ' stood at ' },
          {
            type: 'data_slot',
            slotKey: 'b1_data_1',
            label: 'Data 1 + Đơn vị',
            placeholder: 'VD: 72 billion minutes'
          },
          { type: 'text', text: ', which was significantly higher than that of ' },
          {
            type: 'data_slot',
            slotKey: 'b1_item_b',
            label: 'Đối tượng [B]',
            placeholder: 'VD: mobile calls'
          },
          { type: 'text', text: ' at ' },
          {
            type: 'data_slot',
            slotKey: 'b1_data_2',
            label: 'Data 2 + Đơn vị',
            placeholder: 'VD: 38 billion minutes'
          },
          { type: 'text', text: '. Over the following years, the figure for ' },
          {
            type: 'data_slot',
            slotKey: 'b1_item_a_ref',
            label: 'Nhắc lại [A]',
            placeholder: 'VD: local calls'
          },
          { type: 'text', text: ' ' },
          {
            type: 'vocab_slot',
            slotKey: 'b1_trend_a',
            label: 'Xu hướng + Cấp độ (A)',
            placeholder: 'climbed up dramatically to / experienced a rapid surge to',
            vocabPresetGroup: 'trend_up_phrase',
            quickChips: [
              'climbed up dramatically to',
              'experienced a rapid increase to',
              'rose steadily to',
              'surged to a peak of',
              'declined gradually to'
            ]
          },
          { type: 'text', text: ' ' },
          {
            type: 'data_slot',
            slotKey: 'b1_data_3',
            label: 'Data 3 + Đơn vị',
            placeholder: 'VD: 90 billion minutes in 1999'
          },
          { type: 'text', text: '. Similarly, ' },
          {
            type: 'data_slot',
            slotKey: 'b1_item_b_ref',
            label: 'Nhắc lại [B]',
            placeholder: 'VD: mobile calls'
          },
          { type: 'text', text: ' ' },
          {
            type: 'vocab_slot',
            slotKey: 'b1_trend_b',
            label: 'Xu hướng + Cấp độ (B)',
            placeholder: 'saw a slight rise, reaching / grew substantially to',
            vocabPresetGroup: 'trend_any_phrase',
            quickChips: [
              'saw a slight rise, reaching',
              'grew substantially to',
              'increased moderately to',
              'remained stable at',
              'is projected to reach'
            ]
          },
          { type: 'text', text: ' ' },
          {
            type: 'data_slot',
            slotKey: 'b1_data_4',
            label: 'Data 4 + Đơn vị + Năm',
            placeholder: 'VD: 45 billion minutes in 2002'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'body2',
        title: 'Body 2 (Nhóm đối lập / Xu hướng giảm hoặc giữ nguyên)',
        viHint: 'Dùng Turning to the remaining categories + từ vựng giảm / dao động / đi ngang.',
        accentColor: 'amber',
        tokens: [
          { type: 'text', text: 'Turning to the remaining categories, the figure for ' },
          {
            type: 'data_slot',
            slotKey: 'b2_item_c',
            label: 'Đối tượng [C]',
            placeholder: 'VD: rail transport'
          },
          { type: 'text', text: ' started at ' },
          {
            type: 'data_slot',
            slotKey: 'b2_data_5',
            label: 'Data 5 + Đơn vị',
            placeholder: 'VD: 25%'
          },
          { type: 'text', text: ', before it ' },
          {
            type: 'vocab_slot',
            slotKey: 'b2_trend_c',
            label: 'Xu hướng + Cấp độ (C)',
            placeholder: 'dropped sharply to / experienced a steady decline to',
            vocabPresetGroup: 'trend_down_phrase',
            quickChips: [
              'dropped sharply to',
              'experienced a steady decline to',
              'fell dramatically to',
              'fluctuated mildly around',
              'remained unchanged at'
            ]
          },
          { type: 'text', text: ' ' },
          {
            type: 'data_slot',
            slotKey: 'b2_data_6',
            label: 'Data 6 + Đơn vị',
            placeholder: 'VD: 12%'
          },
          { type: 'text', text: ' at the end of the period. Meanwhile, ' },
          {
            type: 'data_slot',
            slotKey: 'b2_items_de',
            label: 'Đối tượng [D] (và [E])',
            placeholder: 'VD: hydropower and solar energy'
          },
          { type: 'text', text: ' ' },
          {
            type: 'vocab_slot',
            slotKey: 'b2_trend_de',
            label: 'Xu hướng / Kết thúc (D & E)',
            placeholder: 'remained relatively stable, ending at / shared a similar pattern, finishing at',
            vocabPresetGroup: 'trend_any_phrase',
            quickChips: [
              'shared a similar pattern, ending at',
              'remained relatively stable at around',
              'dipped marginally to',
              'witnessed mild fluctuations, finishing at'
            ]
          },
          { type: 'text', text: ' ' },
          {
            type: 'data_slot',
            slotKey: 'b2_data_78',
            label: 'Data 7 (& Data 8) + Đơn vị',
            placeholder: 'VD: 5% and 3% respectively'
          },
          { type: 'text', text: '.' }
        ]
      }
    ]
  },

  static: {
    id: 'static',
    shortBadge: '2. Static (1 thời điểm)',
    name: '2. Data Analysis — STATIC (So sánh chéo tại 1 thời điểm)',
    viSubtitle: 'Chỉ có 1 năm duy nhất (VD: in 2006) hoặc không có năm — TUYỆT ĐỐI KHÔNG dùng từ tăng/giảm!',
    signalCue: 'Đề so sánh các quốc gia/nhóm/hoạt động tại 1 thời điểm duy nhất (không có sự biến thiên theo năm).',
    tenseRule:
      'Nếu đề có năm quá khứ (VD: in 2002) → chia Quá khứ đơn (accounted for, ranked, was). Nếu đề KHÔNG nêu năm → chia Hiện tại đơn (accounts for, ranks, is).',
    goldenTips: [
      'CẤM TUYỆT ĐỐI các động từ tăng/giảm (increase, decrease, climb, drop, fluctuate) vì biểu đồ tĩnh không có dòng thời gian!',
      'Thay bằng từ vựng TỶ TRỌNG & XẾP HẠNG: accounted for, made up, constituted, ranked first, stood at, was double that of...',
      'Gộp các mục nhỏ xíu bằng nhau vào chung 1 câu ở cuối Body 2 (VD: 3% each and 1% respectively).'
    ],
    recommendedVocabTab: 'static',
    paragraphs: [
      {
        key: 'intro',
        title: 'Introduction (Mở bài — So sánh theo tiêu chí)',
        viHint: 'Dùng động từ compares ... in terms of ... (+ mốc năm nếu đề có).',
        accentColor: 'emerald',
        tokens: [
          { type: 'text', text: 'The provided ' },
          {
            type: 'data_slot',
            slotKey: 'chart_type',
            label: 'loại biểu đồ',
            placeholder: 'pie chart / bar chart / table',
            quickChips: ['pie chart', 'pie charts', 'bar chart', 'table']
          },
          { type: 'text', text: ' compares ' },
          {
            type: 'data_slot',
            slotKey: 'topic_paraphrase',
            label: 'chủ đề đề bài',
            placeholder: 'VD: consumer spending in five countries'
          },
          { type: 'text', text: ' in terms of ' },
          {
            type: 'data_slot',
            slotKey: 'criteria_and_year',
            label: 'tiêu chí phân loại (+ in Năm nếu có)',
            placeholder: 'VD: three categories of items in 2002'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'overview',
        title: 'Overview (Tổng quan — Cao nhất vs Thấp nhất)',
        viHint: 'Chỉ ra nhóm chiếm tỷ trọng cao nhất [A], thấp nhất [B], và nhóm lớn thứ nhì [C].',
        accentColor: 'indigo',
        tokens: [
          { type: 'text', text: 'Overall, it is clear that ' },
          {
            type: 'data_slot',
            slotKey: 'ov_highest_a',
            label: 'Nhóm cao nhất [A]',
            placeholder: 'VD: food, drinks and tobacco'
          },
          { type: 'text', text: ' ' },
          {
            type: 'vocab_slot',
            slotKey: 'ov_share_verb',
            label: 'Động từ tỷ trọng',
            placeholder: 'accounted for / accounts for',
            vocabPresetGroup: 'static_share_verb',
            quickChips: ['accounted for', 'accounts for', 'recorded', 'records']
          },
          { type: 'text', text: ' the highest proportion/figure, whereas the opposite ' },
          {
            type: 'vocab_slot',
            slotKey: 'ov_be_tense',
            label: 'was / is',
            placeholder: 'was',
            quickChips: ['was', 'is']
          },
          { type: 'text', text: ' true for ' },
          {
            type: 'data_slot',
            slotKey: 'ov_lowest_b',
            label: 'Nhóm thấp nhất [B]',
            placeholder: 'VD: leisure and education'
          },
          { type: 'text', text: '. Furthermore, ' },
          {
            type: 'data_slot',
            slotKey: 'ov_second_c',
            label: 'Nhóm nổi bật thứ nhì [C]',
            placeholder: 'VD: clothing and footwear'
          },
          { type: 'text', text: ' also constituted a notable share of the total.' }
        ]
      },
      {
        key: 'body1',
        title: 'Body 1 (Phân tích Nhóm Nhất & Nhì)',
        viHint: 'Nêu số liệu cụ thể của nhóm dẫn đầu [A] và nhóm theo sau [C].',
        accentColor: 'teal',
        tokens: [
          { type: 'text', text: 'Looking at the details, the figure for ' },
          {
            type: 'data_slot',
            slotKey: 'b1_item_a',
            label: 'Nhóm dẫn đầu [A]',
            placeholder: 'VD: cattle ranches'
          },
          { type: 'text', text: ' ' },
          {
            type: 'vocab_slot',
            slotKey: 'b1_rank_verb',
            label: 'Cụm dẫn đầu',
            placeholder: 'ranked first, standing at',
            vocabPresetGroup: 'static_rank_verb',
            quickChips: [
              'ranked first, standing at',
              'was the highest, standing at',
              'is the highest, standing at',
              'topped the list at'
            ]
          },
          { type: 'text', text: ' ' },
          {
            type: 'data_slot',
            slotKey: 'b1_data_1',
            label: 'Data 1 + Đơn vị',
            placeholder: 'VD: 54%'
          },
          { type: 'text', text: '. This was followed by ' },
          {
            type: 'data_slot',
            slotKey: 'b1_item_c',
            label: 'Nhóm thứ hai [C]',
            placeholder: 'VD: small-scale subsistence agriculture'
          },
          { type: 'text', text: ', which ' },
          {
            type: 'vocab_slot',
            slotKey: 'b1_share_verb2',
            label: 'Động từ tỷ trọng 2',
            placeholder: 'made up / accounted for',
            vocabPresetGroup: 'static_share_verb',
            quickChips: ['made up', 'makes up', 'constituted', 'represented']
          },
          { type: 'text', text: ' ' },
          {
            type: 'data_slot',
            slotKey: 'b1_data_2',
            label: 'Data 2 + Đơn vị',
            placeholder: 'VD: roughly a third (33%)'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'body2',
        title: 'Body 2 (Các nhóm thấp hơn & Nhóm nhỏ nhất)',
        viHint: 'Gom các nhóm trung bình/thấp và chốt lại số liệu thấp nhất [B].',
        accentColor: 'amber',
        tokens: [
          { type: 'text', text: 'Turning to the remaining categories, ' },
          {
            type: 'data_slot',
            slotKey: 'b2_items_de',
            label: 'Nhóm trung bình [D] & [E]',
            placeholder: 'VD: other causes and logging'
          },
          { type: 'text', text: ' ' },
          {
            type: 'vocab_slot',
            slotKey: 'b2_low_verb',
            label: 'Cụm tỷ trọng thấp hơn',
            placeholder: 'recorded much lower figures of',
            vocabPresetGroup: 'static_share_verb',
            quickChips: [
              'recorded much lower figures of',
              'accounted for relatively smaller shares, at',
              'account for relatively smaller shares, at',
              'constituted modest proportions of'
            ]
          },
          { type: 'text', text: ' ' },
          {
            type: 'data_slot',
            slotKey: 'b2_data_34',
            label: 'Data 3 & 4 + Đơn vị',
            placeholder: 'VD: 6% and 3% respectively'
          },
          { type: 'text', text: '. Finally, the lowest figure was seen in ' },
          {
            type: 'data_slot',
            slotKey: 'b2_item_b',
            label: 'Nhóm thấp nhất [B]',
            placeholder: 'VD: large-scale commercial agriculture'
          },
          { type: 'text', text: ', with only ' },
          {
            type: 'data_slot',
            slotKey: 'b2_data_5',
            label: 'Data 5 + Đơn vị',
            placeholder: 'VD: a mere 1%'
          },
          { type: 'text', text: '.' }
        ]
      }
    ]
  },

  mixed: {
    id: 'mixed',
    shortBadge: '3. Mixed Charts',
    name: '3. MIXED CHARTS (Biểu đồ kết hợp 2 loại hình)',
    viSubtitle: 'Chiến thuật "Chia để trị": Body 1 chỉ tả Hình 1 — Body 2 chỉ tả Hình 2',
    signalCue: 'Đề cho 2 loại biểu đồ khác nhau (VD: 1 Pie Chart + 1 Table, hoặc 1 Line Graph + 1 Bar Chart).',
    tenseRule:
      'Xét riêng từng hình! Hình nào có nhiều năm → dùng từ vựng Xu hướng (Dynamic). Hình nào chỉ có 1 thời điểm → dùng từ vựng Tỷ trọng (Static).',
    goldenTips: [
      'TUYỆT ĐỐI không trộn lẫn hay cố cộng/trừ số liệu giữa 2 biểu đồ khác đơn vị.',
      'Overview viết đúng 2 câu: Câu 1 nêu điểm nổi bật nhất của Hình 1; Câu 2 ("In addition,...") nêu điểm nổi bật nhất của Hình 2.',
      'Mỗi Body chỉ chọn lọc 2–3 con số đắt giá nhất (cao nhất, thấp nhất, biến động lớn nhất).'
    ],
    recommendedVocabTab: 'trends',
    paragraphs: [
      {
        key: 'intro',
        title: 'Introduction (Giới thiệu Hình 1 + while + Hình 2)',
        viHint: 'Ghép gọn 2 biểu đồ trong 1 câu phức bằng liên từ "while".',
        accentColor: 'teal',
        tokens: [
          { type: 'text', text: 'The provided ' },
          {
            type: 'data_slot',
            slotKey: 'chart_1_type',
            label: 'loại biểu đồ 1',
            placeholder: 'pie chart / line graph / bar chart',
            quickChips: ['pie chart', 'line graph', 'bar chart', 'table']
          },
          { type: 'text', text: ' illustrates ' },
          {
            type: 'data_slot',
            slotKey: 'chart_1_topic',
            label: 'chủ đề của hình 1',
            placeholder: 'VD: the main reasons why agricultural land becomes less productive'
          },
          { type: 'text', text: ', while the ' },
          {
            type: 'data_slot',
            slotKey: 'chart_2_type',
            label: 'loại biểu đồ 2',
            placeholder: 'table / bar chart / pie chart',
            quickChips: ['table', 'bar chart', 'pie chart', 'line graph']
          },
          { type: 'text', text: ' shows ' },
          {
            type: 'data_slot',
            slotKey: 'chart_2_topic',
            label: 'chủ đề của hình 2',
            placeholder: 'VD: how these causes affected three regions during the 1990s'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'overview',
        title: 'Overview (Câu 1 cho Hình 1 + Câu 2 cho Hình 2)',
        viHint: 'Mỗi hình rút ra 1 kết luận tổng quát nhất (không kèm số liệu chi tiết).',
        accentColor: 'indigo',
        tokens: [
          { type: 'text', text: 'Overall, it is clear that ' },
          {
            type: 'data_slot',
            slotKey: 'ov_chart_1_feature',
            label: 'Đặc điểm nổi bật nhất của Hình 1',
            placeholder: 'VD: over-grazing accounted for the largest share of global land degradation'
          },
          { type: 'text', text: '. In addition, ' },
          {
            type: 'data_slot',
            slotKey: 'ov_chart_2_feature',
            label: 'Đặc điểm nổi bật nhất của Hình 2',
            placeholder: 'VD: Europe suffered the highest percentage of degraded land among the three regions'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'body1',
        title: 'Body 1 (Chỉ phân tích sâu Biểu đồ 1)',
        viHint: 'Áp dụng từ vựng Dynamic (nếu Hình 1 có nhiều năm) hoặc Static (nếu Hình 1 là 1 thời điểm).',
        accentColor: 'emerald',
        tokens: [
          { type: 'text', text: 'Looking at the ' },
          {
            type: 'data_slot',
            slotKey: 'b1_chart_1_ref',
            label: 'loại biểu đồ 1',
            placeholder: 'pie chart / line graph'
          },
          { type: 'text', text: ' in more detail, ' },
          {
            type: 'data_slot',
            slotKey: 'b1_main_detail',
            label: 'Số liệu / xu hướng chính của Hình 1',
            placeholder: 'VD: over-grazing ranked first at 35%, closely followed by deforestation at 30%'
          },
          { type: 'text', text: '. Furthermore, ' },
          {
            type: 'data_slot',
            slotKey: 'b1_sub_detail',
            label: '1–2 chi tiết còn lại của Hình 1',
            placeholder: 'VD: over-cultivation made up 28%, whereas other causes accounted for only 7%'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'body2',
        title: 'Body 2 (Chỉ phân tích sâu Biểu đồ 2)',
        viHint: 'Chuyển mượt sang Hình 2 bằng "Turning to the [loại biểu đồ 2], it can be seen that...".',
        accentColor: 'amber',
        tokens: [
          { type: 'text', text: 'Turning to the ' },
          {
            type: 'data_slot',
            slotKey: 'b2_chart_2_ref',
            label: 'loại biểu đồ 2',
            placeholder: 'table / bar chart'
          },
          { type: 'text', text: ', it can be seen that ' },
          {
            type: 'data_slot',
            slotKey: 'b2_main_detail',
            label: 'Số liệu / xu hướng chính của Hình 2',
            placeholder: 'VD: Europe recorded the highest total land degraded at 23%, largely due to deforestation (9.8%)'
          },
          { type: 'text', text: '. Meanwhile, ' },
          {
            type: 'data_slot',
            slotKey: 'b2_sub_detail',
            label: '1–2 chi tiết đối chiếu của Hình 2',
            placeholder: 'VD: Oceania had 13% of degraded land, while North America was least affected with just 5%'
          },
          { type: 'text', text: '.' }
        ]
      }
    ]
  },

  process: {
    id: 'process',
    shortBadge: '4. Process (Quy trình)',
    name: '4. PROCESS DIAGRAM (Quy trình sản xuất / Tự nhiên / Vòng đời)',
    viSubtitle: 'Đếm tổng số bước + điểm đầu & điểm cuối; chia đôi quy trình vào Body 1 & Body 2',
    signalCue: 'Sơ đồ mũi tên các bước sản xuất/tái chế (Man-made) hoặc hiện tượng tự nhiên/vòng đời (Natural).',
    tenseRule:
      'Luôn dùng HIỆN TẠI ĐƠN (Present Simple)! Quy trình nhân tạo → ưu tiên Bị động (is crushed, is heated). Quy trình tự nhiên/vòng đời → ưu tiên Chủ động (absorbs, hatches, grows into).',
    goldenTips: [
      'Overview bắt buộc nêu: (1) Tổng số bước chính + bản chất man-made hay natural, (2) Bước mở đầu (beginning with) & bước kết thúc (culminating in).',
      'Tận dụng các từ nối chuyển bước sẵn trong khung: Looking at the first stage, Following this, Once this step is completed, In the subsequent stage, Finally.'
    ],
    recommendedVocabTab: 'process_map',
    paragraphs: [
      {
        key: 'intro',
        title: 'Introduction (Giới thiệu Quy trình Nhân tạo hoặc Tự nhiên)',
        viHint: 'Chọn cụm động từ khớp với quy trình sản xuất hay vòng đời/tự nhiên.',
        accentColor: 'indigo',
        tokens: [
          { type: 'text', text: 'The provided diagram illustrates ' },
          {
            type: 'vocab_slot',
            slotKey: 'proc_intro_lead',
            label: 'Cụm mở đầu quy trình',
            placeholder: 'the process of producing',
            vocabPresetGroup: 'process_intro_verb',
            quickChips: [
              'the process of producing',
              'the process of manufacturing',
              'the process of recycling',
              'how',
              'the life cycle of'
            ]
          },
          { type: 'text', text: ' ' },
          {
            type: 'data_slot',
            slotKey: 'proc_topic',
            label: 'chủ đề quy trình',
            placeholder: 'VD: cement and concrete for building purposes / photosynthesis occurs in plants'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'overview',
        title: 'Overview (Tổng số bước + Bản chất + Điểm đầu & Điểm cuối)',
        viHint: 'Cấu trúc ăn điểm tuyệt đối: beginning with ... and culminating in ...',
        accentColor: 'violet',
        tokens: [
          { type: 'text', text: 'Overall, it is clear that there are ' },
          {
            type: 'data_slot',
            slotKey: 'proc_num_stages',
            label: 'Số lượng bước',
            placeholder: 'VD: five / eight / several'
          },
          { type: 'text', text: ' main stages in this entirely ' },
          {
            type: 'vocab_slot',
            slotKey: 'proc_nature',
            label: 'man-made / natural',
            placeholder: 'man-made',
            vocabPresetGroup: 'process_type',
            quickChips: ['man-made', 'natural', 'cyclical natural', 'linear man-made']
          },
          { type: 'text', text: ' process, beginning with ' },
          {
            type: 'data_slot',
            slotKey: 'proc_first_step_noun',
            label: 'Bước đầu tiên (Cụm danh từ / V-ing)',
            placeholder: 'VD: crushing limestone and clay'
          },
          { type: 'text', text: ' and culminating in ' },
          {
            type: 'data_slot',
            slotKey: 'proc_last_step_noun',
            label: 'Bước cuối cùng (Cụm danh từ / V-ing)',
            placeholder: 'VD: packaging the finished cement into bags'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'body1',
        title: 'Body 1 (Nửa đầu quy trình — Bước 1 đến Bước giữa)',
        viHint: 'Dùng Bị động (is + V3) cho máy móc/con người làm, Chủ động cho tự nhiên.',
        accentColor: 'emerald',
        tokens: [
          { type: 'text', text: 'Looking at the first stage of the process, ' },
          {
            type: 'data_slot',
            slotKey: 'proc_step_1',
            label: 'Mệnh đề mô tả Bước 1 (S + V)',
            placeholder: 'VD: limestone and clay are crushed together into a fine powder'
          },
          { type: 'text', text: '. Following this, ' },
          {
            type: 'data_slot',
            slotKey: 'proc_step_2',
            label: 'Mệnh đề mô tả Bước 2 (S + V)',
            placeholder: 'VD: the resulting powder is thoroughly mixed before passing through a rotating heater'
          },
          { type: 'text', text: '. Once this step is completed, the ' },
          {
            type: 'data_slot',
            slotKey: 'proc_mid_input',
            label: 'Nguyên liệu / Sự vật trung gian',
            placeholder: 'VD: heated mixture'
          },
          { type: 'text', text: ' undergoes a transformation into ' },
          {
            type: 'data_slot',
            slotKey: 'proc_mid_output',
            label: 'Sản phẩm / Trạng thái mới',
            placeholder: 'VD: raw cement'
          },
          { type: 'text', text: ' by ' },
          {
            type: 'data_slot',
            slotKey: 'proc_step_3_ving',
            label: 'Hành động V-ing ở Bước 3',
            placeholder: 'VD: being ground in a heavy grinder'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'body2',
        title: 'Body 2 (Nửa sau quy trình — Đến bước hoàn tất)',
        viHint: 'Nối tiếp các bước còn lại đến khi ra thành phẩm cuối cùng.',
        accentColor: 'amber',
        tokens: [
          { type: 'text', text: 'In the subsequent stage, ' },
          {
            type: 'data_slot',
            slotKey: 'proc_step_4',
            label: 'Mệnh đề mô tả Bước 4 (S + V)',
            placeholder: 'VD: the finished cement is packed into large bags ready for construction use'
          },
          { type: 'text', text: '. After that, ' },
          {
            type: 'data_slot',
            slotKey: 'proc_step_5',
            label: 'Mệnh đề mô tả Bước 5 (S + V)',
            placeholder: 'VD: 15% cement is combined with 10% water, 25% sand, and 50% small stones inside a concrete mixer'
          },
          { type: 'text', text: '. Finally, the process concludes when ' },
          {
            type: 'data_slot',
            slotKey: 'proc_step_final',
            label: 'Mệnh đề mô tả Bước cuối (S + V)',
            placeholder: 'VD: the mixer rotates continuously to yield ready-to-use concrete'
          },
          { type: 'text', text: '.' }
        ]
      }
    ]
  },

  outdoor_map: {
    id: 'outdoor_map',
    shortBadge: '5. Outdoor Map (La bàn)',
    name: '5. OUTDOOR MAP (Bản đồ quy hoạch ngoài trời)',
    viSubtitle: 'Thị trấn, hòn đảo, ngôi làng, khu công nghiệp — BẮT BUỘC định vị bằng North / South / East / West',
    signalCue: 'Bản đồ ngoài trời có la bàn (town, village, island, park, road, harbour).',
    tenseRule:
      'Chú ý mốc năm trên 2 bản đồ: (1) Hai năm quá khứ → was V3; (2) Quá khứ đến Now/Today → has been V3; (3) Now và Kế hoạch tương lai (plans/future) → is planned to be V3 / will be V3!',
    goldenTips: [
      'Luôn dùng phương hướng La bàn (in the north, to the south-east of...) thay vì left/right.',
      'Dùng thể Bị động quy hoạch: was demolished / knocked down, was constructed / built, was expanded, to make way for...'
    ],
    recommendedVocabTab: 'process_map',
    paragraphs: [
      {
        key: 'intro',
        title: 'Introduction (Giới thiệu Địa điểm & Mốc thời gian quy hoạch)',
        viHint: 'Chú ý nếu bản đồ 2 là tương lai thì dùng "and proposed plans for its future development".',
        accentColor: 'emerald',
        tokens: [
          { type: 'text', text: 'The provided maps illustrate ' },
          {
            type: 'data_slot',
            slotKey: 'map_intro_focus',
            label: 'sự thay đổi / kế hoạch phát triển tại [Địa điểm + Thời gian]',
            placeholder: 'VD: the changes that took place in the town of Islip between 2000 and 2015 / the town of Islip now and plans for its future development'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'overview',
        title: 'Overview (Sự lột xác tổng thể + 2 thay đổi lớn nhất)',
        viHint: 'Nêu khu vực mở rộng lớn nhất [A] và công trình bị phá dỡ/thay thế nổi bật nhất [B].',
        accentColor: 'indigo',
        tokens: [
          { type: 'text', text: 'Overall, it is clear that the area ' },
          {
            type: 'vocab_slot',
            slotKey: 'map_ov_tense',
            label: 'Thì của sự biến đổi',
            placeholder: 'underwent a significant transformation',
            vocabPresetGroup: 'map_change_verb',
            quickChips: [
              'underwent a significant transformation',
              'has undergone a dramatic transformation',
              'is set to undergo a major redevelopment'
            ]
          },
          { type: 'text', text: ', with the most notable changes being the expansion/addition of ' },
          {
            type: 'data_slot',
            slotKey: 'map_ov_add',
            label: 'Hạng mục mở rộng/mới [A]',
            placeholder: 'VD: new housing and transport infrastructure'
          },
          { type: 'text', text: ' and the removal/conversion of ' },
          {
            type: 'data_slot',
            slotKey: 'map_ov_remove',
            label: 'Khu vực bị phá dỡ/chuyển đổi [B]',
            placeholder: 'VD: the countryside and old shops'
          },
          { type: 'text', text: ' to make way for modern facilities.' }
        ]
      },
      {
        key: 'body1',
        title: 'Body 1 (Khu vực Bắc / Trung tâm — Phá dỡ, Xây mới & Mở rộng)',
        viHint: 'Định vị bằng North / South / East / West + chia đúng Thì bị động theo năm của đề.',
        accentColor: 'teal',
        tokens: [
          { type: 'text', text: 'Looking at the details, in the ' },
          {
            type: 'vocab_slot',
            slotKey: 'map_b1_dir1',
            label: 'Hướng la bàn 1',
            placeholder: 'north',
            vocabPresetGroup: 'map_compass',
            quickChips: ['north', 'south', 'east', 'west', 'central part', 'north-west', 'south-east']
          },
          { type: 'text', text: ' of the map, ' },
          {
            type: 'data_slot',
            slotKey: 'map_b1_old',
            label: 'Công trình cũ',
            placeholder: 'VD: the row of shops / the forest area'
          },
          { type: 'text', text: ' ' },
          {
            type: 'vocab_slot',
            slotKey: 'map_b1_demolish',
            label: 'Động từ phá dỡ (đúng Thì)',
            placeholder: 'was knocked down',
            vocabPresetGroup: 'map_change_verb',
            quickChips: [
              'was knocked down',
              'was demolished',
              'has been cleared',
              'is planned to be demolished',
              'will be replaced'
            ]
          },
          { type: 'text', text: ' to make way for ' },
          {
            type: 'data_slot',
            slotKey: 'map_b1_new',
            label: 'Công trình mới xây',
            placeholder: 'VD: a new bus station and a shopping centre'
          },
          { type: 'text', text: '. Additionally, ' },
          {
            type: 'data_slot',
            slotKey: 'map_b1_second_change',
            label: 'Công trình thứ 2 + thay đổi + hướng',
            placeholder: 'VD: a dual carriageway is planned to be constructed around the town centre'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'body2',
        title: 'Body 2 (Khu vực còn lại — Phần giữ nguyên & Phần chuyển đổi)',
        viHint: 'Chỉ ra hạng mục không đổi (remained unchanged) và khu vực chuyển đổi mục đích sử dụng.',
        accentColor: 'amber',
        tokens: [
          { type: 'text', text: 'Turning to the ' },
          {
            type: 'vocab_slot',
            slotKey: 'map_b2_dir',
            label: 'Hướng còn lại',
            placeholder: 'southern and eastern parts',
            vocabPresetGroup: 'map_compass',
            quickChips: ['southern part', 'eastern side', 'western section', 'other side']
          },
          { type: 'text', text: ' of the area, ' },
          {
            type: 'data_slot',
            slotKey: 'map_b2_unchanged',
            label: 'Công trình giữ nguyên + động từ',
            placeholder: 'VD: the main park remained largely unchanged / the school will remain in its original site'
          },
          { type: 'text', text: '. However, ' },
          {
            type: 'data_slot',
            slotKey: 'map_b2_transformed',
            label: 'Công trình 4 chuyển đổi thành Công trình 5',
            placeholder: 'VD: the farmland in the south-east was transformed into a new residential housing area'
          },
          { type: 'text', text: ', providing more space for ' },
          {
            type: 'data_slot',
            slotKey: 'map_b2_purpose',
            label: 'Mục đích sử dụng',
            placeholder: 'VD: local residents / recreation and leisure'
          },
          { type: 'text', text: '.' }
        ]
      }
    ]
  },

  indoor_map: {
    id: 'indoor_map',
    shortBadge: '6. Indoor Map (Mặt bằng)',
    name: '6. INDOOR MAP (Sơ đồ mặt bằng / Nội thất tòa nhà)',
    viSubtitle: 'Thư viện, bảo tàng, trung tâm nghệ thuật, văn phòng — KHÔNG dùng Đông/Tây/Nam/Bắc nếu không có la bàn',
    signalCue: 'Sơ đồ bố trí phòng ốc (floor plan, layout of a library / office / gallery / airport / centre).',
    tenseRule:
      'Kiểm tra kỹ thời gian đề bài: (1) 2001 → 2009: dùng Quá khứ (was replaced, was converted); (2) Past → Today: dùng Hiện tại hoàn thành (has been replaced); (3) Now → Future/Proposed: dùng is planned to be replaced / will be transformed.',
    goldenTips: [
      'Dùng từ vựng không gian nội thất: upon entering the building, on the left/right-hand side, in the central area, in the top-right corner, along the back wall.',
      'Nếu đề KHÔNG có biểu tượng La bàn thì tuyệt đối không tự bịa North/South/East/West.'
    ],
    recommendedVocabTab: 'process_map',
    paragraphs: [
      {
        key: 'intro',
        title: 'Introduction (Giới thiệu Sơ đồ mặt bằng & Thời gian)',
        viHint: 'Dùng floor plans / diagrams illustrate the modifications / proposed changes to the layout of...',
        accentColor: 'teal',
        tokens: [
          { type: 'text', text: 'The provided floor plans illustrate ' },
          {
            type: 'data_slot',
            slotKey: 'in_intro_desc',
            label: 'sự thay đổi / kế hoạch bố trí lại của [Tên tòa nhà + Thời gian]',
            placeholder: 'VD: the modifications to the layout of a public library between 2001 and 2009 / the current layout of an office building and proposed plans for its future redesign'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'overview',
        title: 'Overview (Tái bố trí không gian: Thêm mới & Dời/Xóa bỏ)',
        viHint: 'Tóm tắt các phòng/khu mới được bổ sung và các khu cũ bị dời hoặc loại bỏ.',
        accentColor: 'indigo',
        tokens: [
          { type: 'text', text: 'Overall, the most significant changes involve the reorganization of the interior space, notably the addition of ' },
          {
            type: 'data_slot',
            slotKey: 'in_ov_added',
            label: 'Khu vực mới thêm vào',
            placeholder: 'VD: a café, computer stations, and a children’s area'
          },
          { type: 'text', text: ' and the relocation/removal of ' },
          {
            type: 'data_slot',
            slotKey: 'in_ov_removed',
            label: 'Khu vực bị dời đi / xóa bỏ',
            placeholder: 'VD: the old reading tables and the history section'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'body1',
        title: 'Body 1 (Khu vực Cửa vào, Hai bên Trái/Phải & Khu Trung tâm)',
        viHint: 'Dẫn giám khảo đi từ cửa chính vào: upon entering the building...',
        accentColor: 'emerald',
        tokens: [
          { type: 'text', text: 'Looking at the details, upon entering the building, the ' },
          {
            type: 'data_slot',
            slotKey: 'in_b1_item_a',
            label: 'Khu vực A + vị trí trái/phải',
            placeholder: 'VD: reception desk on the left-hand side of the entrance'
          },
          { type: 'text', text: ' ' },
          {
            type: 'vocab_slot',
            slotKey: 'in_b1_verb1',
            label: 'Cụm thay thế (đúng Thì)',
            placeholder: 'was replaced by / is planned to be replaced by',
            vocabPresetGroup: 'map_change_verb',
            quickChips: [
              'was replaced by',
              'has been replaced by',
              'is planned to be replaced by',
              'was relocated to make room for'
            ]
          },
          { type: 'text', text: ' ' },
          {
            type: 'data_slot',
            slotKey: 'in_b1_item_b',
            label: 'Khu vực mới B',
            placeholder: 'VD: a larger self-service check-in zone'
          },
          { type: 'text', text: '. Furthermore, the central area, which previously housed ' },
          {
            type: 'data_slot',
            slotKey: 'in_b1_item_c',
            label: 'Khu vực C cũ ở trung tâm',
            placeholder: 'VD: adult fiction shelves and tables'
          },
          { type: 'text', text: ', ' },
          {
            type: 'vocab_slot',
            slotKey: 'in_b1_verb2',
            label: 'Cụm chuyển đổi (đúng Thì)',
            placeholder: 'was transformed into / will be transformed into',
            vocabPresetGroup: 'map_change_verb',
            quickChips: [
              'was transformed into',
              'has been converted into',
              'will be transformed into',
              'was reorganized into'
            ]
          },
          { type: 'text', text: ' ' },
          {
            type: 'data_slot',
            slotKey: 'in_b1_item_d',
            label: 'Khu vực D mới ở trung tâm',
            placeholder: 'VD: an open-plan exhibition space'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'body2',
        title: 'Body 2 (Các góc phòng & Bức tường phía sau)',
        viHint: 'Dùng in the top-right/bottom-left corner và along the back wall.',
        accentColor: 'amber',
        tokens: [
          { type: 'text', text: 'Turning to the rest of the layout, the ' },
          {
            type: 'data_slot',
            slotKey: 'in_b2_item_e',
            label: 'Khu vực E',
            placeholder: 'VD: storage room'
          },
          { type: 'text', text: ' located ' },
          {
            type: 'vocab_slot',
            slotKey: 'in_b2_pos',
            label: 'Vị trí góc / tường',
            placeholder: 'in the top-right corner',
            vocabPresetGroup: 'map_indoor_pos',
            quickChips: [
              'in the top-right corner',
              'in the bottom-left corner',
              'in the top-left corner',
              'on the right-hand side'
            ]
          },
          { type: 'text', text: ' ' },
          {
            type: 'data_slot',
            slotKey: 'in_b2_change_ef',
            label: 'biến đổi thành Khu vực F (đúng Thì)',
            placeholder: 'VD: was converted into a modern lecture room / will be expanded into a café'
          },
          { type: 'text', text: '. Meanwhile, ' },
          {
            type: 'data_slot',
            slotKey: 'in_b2_unchanged_g',
            label: 'Khu vực G giữ nguyên dọc tường sau',
            placeholder: 'VD: the lift and stairs along the back wall remained completely unchanged'
          },
          { type: 'text', text: '.' }
        ]
      }
    ]
  },

  evolution_diagram: {
    id: 'evolution_diagram',
    shortBadge: '7. Evolution Diagram',
    name: '7. OBJECT / EVOLUTION DIAGRAM (Sự tiến hóa của Đồ vật / Sinh vật)',
    viSubtitle: 'So sánh phiên bản sơ khai (Body 1) với phiên bản nâng cấp/tiến hóa (Body 2)',
    signalCue: 'Hình vẽ so sánh công cụ cổ đại qua các thời kỳ (Stone Age tools) hoặc sự tiến hóa của loài vật (Horse evolution).',
    tenseRule: 'Quá khứ đơn (was, consisted of, evolved into) khi mô tả các thời kỳ lịch sử/tiền sử; Hiện tại đơn cho phiên bản hiện đại (modern horse).',
    goldenTips: [
      'Body 1 tả mẫu nguyên bản (kích thước, hình dáng thô sơ); Body 2 dùng tính từ so sánh hơn (larger, sharper, more refined) để nổi bật sự tiến hóa.',
      'Chốt mục đích tiến hóa ở cuối Body 2: making it far more effective for [running / cutting].'
    ],
    recommendedVocabTab: 'process_map',
    paragraphs: [
      {
        key: 'intro',
        title: 'Introduction (Sự tiến hóa từ Thời kỳ cũ đến Thời kỳ mới)',
        viHint: 'Dùng the evolution / development of [Đối tượng] from [Thời kỳ 1] to [Thời kỳ 2].',
        accentColor: 'amber',
        tokens: [
          { type: 'text', text: 'The provided diagrams illustrate the evolution/development of ' },
          {
            type: 'data_slot',
            slotKey: 'evo_subject',
            label: 'Tên đồ vật / Loài vật',
            placeholder: 'VD: Stone Age cutting tools / the horse'
          },
          { type: 'text', text: ' from ' },
          {
            type: 'data_slot',
            slotKey: 'evo_time_1',
            label: 'Thời kỳ mẫu cũ',
            placeholder: 'VD: 1.4 million years ago / 40 million years ago'
          },
          { type: 'text', text: ' to ' },
          {
            type: 'data_slot',
            slotKey: 'evo_time_2',
            label: 'Thời kỳ mẫu mới',
            placeholder: 'VD: 0.8 million years ago / the present day'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'overview',
        title: 'Overview (Các thay đổi hình thái nổi bật nhất)',
        viHint: 'Dùng becoming + 2 tính từ so sánh hơn (larger, sharper, taller, more refined).',
        accentColor: 'indigo',
        tokens: [
          { type: 'text', text: 'Overall, it is clear that the ' },
          {
            type: 'data_slot',
            slotKey: 'evo_ov_subj',
            label: 'Tên đồ vật / Loài vật',
            placeholder: 'VD: cutting tool / horse'
          },
          { type: 'text', text: ' underwent significant physical changes, becoming ' },
          {
            type: 'vocab_slot',
            slotKey: 'evo_adj_1',
            label: 'Tính từ so sánh 1',
            placeholder: 'larger',
            vocabPresetGroup: 'diagram_adj',
            quickChips: ['larger', 'taller', 'sleeker', 'more compact']
          },
          { type: 'text', text: ', ' },
          {
            type: 'vocab_slot',
            slotKey: 'evo_adj_2',
            label: 'Tính từ so sánh 2',
            placeholder: 'sharper and more refined',
            vocabPresetGroup: 'diagram_adj',
            quickChips: ['sharper', 'more symmetrical', 'more solid', 'structurally more refined']
          },
          { type: 'text', text: ', and much more developed over the given period.' }
        ]
      },
      {
        key: 'body1',
        title: 'Body 1 (Miêu tả Mẫu nguyên bản / Tổ tiên)',
        viHint: 'Nêu mốc thời gian cổ xưa, kích thước và đặc điểm hình thái sơ khai.',
        accentColor: 'emerald',
        tokens: [
          { type: 'text', text: 'Looking at the earliest version, ' },
          {
            type: 'data_slot',
            slotKey: 'evo_b1_name',
            label: 'Tên mẫu đầu tiên',
            placeholder: 'VD: Tool A / the Eohippus'
          },
          { type: 'text', text: ' dating back to ' },
          {
            type: 'data_slot',
            slotKey: 'evo_b1_time',
            label: 'Thời gian 1',
            placeholder: 'VD: 1.4 million years ago'
          },
          { type: 'text', text: ' was relatively ' },
          {
            type: 'data_slot',
            slotKey: 'evo_b1_adj',
            label: 'Tính từ sơ khai',
            placeholder: 'VD: rough and rudimentary / small'
          },
          { type: 'text', text: ' in its structure. From the visual representation, its overall size was approximately ' },
          {
            type: 'data_slot',
            slotKey: 'evo_b1_size',
            label: 'Kích thước mẫu 1',
            placeholder: 'VD: 7–8 centimeters in length'
          },
          { type: 'text', text: ', and its main feature consisted of ' },
          {
            type: 'data_slot',
            slotKey: 'evo_b1_feature',
            label: 'Đặc điểm bộ phận ban đầu',
            placeholder: 'VD: an uneven surface and blunt edges / four separate toes'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'body2',
        title: 'Body 2 (Miêu tả Bản nâng cấp / Hậu duệ)',
        viHint: 'Đối chiếu trực tiếp với mẫu cũ bằng "Compared to the previous version...".',
        accentColor: 'orange',
        tokens: [
          { type: 'text', text: 'Turning to the later stage(s), ' },
          {
            type: 'data_slot',
            slotKey: 'evo_b2_name',
            label: 'Tên mẫu sau / hiện đại',
            placeholder: 'VD: Tool B / the modern horse'
          },
          { type: 'text', text: ' showed marked developments. Compared to the previous version, it became significantly ' },
          {
            type: 'data_slot',
            slotKey: 'evo_b2_comp',
            label: 'So sánh kích thước & hình dáng mới',
            placeholder: 'VD: larger and more tear-drop shaped, measuring around 10 centimeters'
          },
          { type: 'text', text: '. Furthermore, its key parts ' },
          {
            type: 'data_slot',
            slotKey: 'evo_b2_parts',
            label: 'Sự cải tiến bộ phận',
            placeholder: 'VD: were finely chipped to form smooth, sharp edges / fused into a single sturdy hoof'
          },
          { type: 'text', text: ', making it far more effective for ' },
          {
            type: 'data_slot',
            slotKey: 'evo_b2_purpose',
            label: 'công năng (V-ing / Noun)',
            placeholder: 'VD: cutting and slicing / running at high speeds'
          },
          { type: 'text', text: '.' }
        ]
      }
    ]
  },

  bio_diagram: {
    id: 'bio_diagram',
    shortBadge: '8. Structure & Function',
    name: '8. BIOLOGICAL / OBJECT DIAGRAM (Cấu tạo & Cơ chế hoạt động)',
    viSubtitle: 'Body 1 chỉ tả Cấu tạo bộ phận tĩnh — Body 2 bấm nút "Play" tả Cơ chế vận hành',
    signalCue: 'Sơ đồ giải phẫu tế bào/máy móc kèm mũi tên cơ chế vận hành (Neuron, Solar panel, Aeroponics, Water filter).',
    tenseRule: 'Dùng HIỆN TẠI ĐƠN (Present Simple) xuyên suốt toàn bài (is composed of, connects, travels through, allows).',
    goldenTips: [
      'Không trộn lẫn vị trí bộ phận và quy trình chạy trong cùng một câu — tách sạch Cấu tạo (Body 1) và Hoạt động (Body 2).',
      'Cụm từ ăn điểm Body 1: is largely composed of, attached to / surrounding this component, connects A to B.'
    ],
    recommendedVocabTab: 'process_map',
    paragraphs: [
      {
        key: 'intro',
        title: 'Introduction (Giới thiệu Cấu tạo + Cách vận hành)',
        viHint: 'illustrates the structure of [Đối tượng] and how it functions/operates.',
        accentColor: 'orange',
        tokens: [
          { type: 'text', text: 'The provided diagram illustrates the structure of ' },
          {
            type: 'data_slot',
            slotKey: 'bio_subject',
            label: 'Tên đối tượng / thiết bị / tế bào',
            placeholder: 'VD: a neural cell (neuron) / a domestic solar heating panel'
          },
          { type: 'text', text: ' and how it functions to ' },
          {
            type: 'data_slot',
            slotKey: 'bio_goal',
            label: 'mục đích hoạt động',
            placeholder: 'VD: transmit electrical signals / heat air or water using solar energy'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'overview',
        title: 'Overview (Số bộ phận cấu thành + Chuỗi vận hành từ Đầu đến Cuối)',
        viHint: 'Câu 1 nêu tổng số bộ phận chính; Câu 2 nêu điểm bắt đầu & kết thúc của cơ chế.',
        accentColor: 'indigo',
        tokens: [
          { type: 'text', text: 'Overall, it is clear that the ' },
          {
            type: 'data_slot',
            slotKey: 'bio_ov_subj',
            label: 'Tên đối tượng',
            placeholder: 'VD: neuron / solar panel'
          },
          { type: 'text', text: ' consists of ' },
          {
            type: 'data_slot',
            slotKey: 'bio_num_parts',
            label: 'Số lượng bộ phận chính',
            placeholder: 'VD: five / three'
          },
          { type: 'text', text: ' main components. Furthermore, its operation relies on a sequential process beginning with ' },
          {
            type: 'data_slot',
            slotKey: 'bio_first_action',
            label: 'Bước/Bộ phận đầu vào',
            placeholder: 'VD: receiving chemical messages via dendrites'
          },
          { type: 'text', text: ' and culminating in ' },
          {
            type: 'data_slot',
            slotKey: 'bio_last_action',
            label: 'Bước/Bộ phận đầu ra',
            placeholder: 'VD: passing electrical impulses to adjacent cells'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'body1',
        title: 'Body 1 (Chỉ tả Cấu tạo hình thể / Các bộ phận)',
        viHint: 'Dùng is largely composed of, attached to, surrounding, connects...',
        accentColor: 'emerald',
        tokens: [
          { type: 'text', text: 'Looking at the physical features, the ' },
          {
            type: 'data_slot',
            slotKey: 'bio_b1_subj',
            label: 'Tên đối tượng',
            placeholder: 'VD: neuron / box'
          },
          { type: 'text', text: ' is largely composed of ' },
          {
            type: 'data_slot',
            slotKey: 'bio_b1_core',
            label: 'Bộ phận trung tâm / chính',
            placeholder: 'VD: a central cell body called the soma'
          },
          { type: 'text', text: '. Attached to/Surrounding this component are ' },
          {
            type: 'data_slot',
            slotKey: 'bio_b1_subparts',
            label: 'Các bộ phận phụ bao quanh',
            placeholder: 'VD: tree-like branches known as dendrites'
          },
          { type: 'text', text: '. Additionally, ' },
          {
            type: 'data_slot',
            slotKey: 'bio_b1_connector',
            label: 'Bộ phận nối & Bộ phận đầu cuối',
            placeholder: 'VD: a long fiber called the axon connects the soma to the terminal buttons at the far end'
          },
          { type: 'text', text: '.' }
        ]
      },
      {
        key: 'body2',
        title: 'Body 2 (Chỉ tả Cơ chế hoạt động / Luân chuyển)',
        viHint: 'Bấm "Play" cho luồng tín hiệu/nước/khí đi từ đầu vào → trung gian → đầu ra.',
        accentColor: 'amber',
        tokens: [
          { type: 'text', text: 'Turning to how it works, the process commences when ' },
          {
            type: 'data_slot',
            slotKey: 'bio_b2_input',
            label: 'Tín hiệu/Vật chất đi vào Bộ phận đầu vào',
            placeholder: 'VD: signals from neighboring cells are received by the dendrites'
          },
          { type: 'text', text: '. Following this, it travels through ' },
          {
            type: 'data_slot',
            slotKey: 'bio_b2_middle',
            label: 'Bộ phận trung gian + tác động phụ',
            placeholder: 'VD: the axon, where the myelin sheath insulates and accelerates the neural impulse'
          },
          { type: 'text', text: '. Finally, the ' },
          {
            type: 'data_slot',
            slotKey: 'bio_b2_output',
            label: 'Tín hiệu/Vật chất chạm đầu ra & phát tán',
            placeholder: 'VD: electrical impulse reaches the terminal buttons, allowing chemical neurotransmitters to be released to the next cell'
          },
          { type: 'text', text: '.' }
        ]
      }
    ]
  }
};

export const WT1_FRAMEWORK_ORDER: Wt1FrameworkId[] = [
  'dynamic',
  'static',
  'mixed',
  'process',
  'outdoor_map',
  'indoor_map',
  'evolution_diagram',
  'bio_diagram'
];

// ============================================================================
// 5. BỘ NHẬN DIỆN DẠNG BÀI THÔNG MINH CHO 63 ĐỀ TRONG "7. TASK 1 : QUESTIONS"
// ============================================================================
export interface Wt1PromptGuide {
  detectedFramework: Wt1FrameworkId;
  detectedConfidenceNote: string;
  detectedTenseTip: string;
  keyCueWords: string[];
}

export function detectWt1PromptGuide(topic: string, pageHint?: string): Wt1PromptGuide {
  const low = (topic || '').toLowerCase();
  const pLow = (pageHint || '').toLowerCase();

  // Extract 4-digit years (e.g. 1980, 2003, 2030)
  const yearMatches = Array.from(new Set(topic.match(/\b(18|19|20)\d{2}\b/g) || []));
  const yearsNum = yearMatches.map((y) => parseInt(y, 10));
  const hasFutureYear = yearsNum.some((y) => y >= 2027) || /\b(future|plan|plans|planned|proposed|projection|projections|next year|redevelopment)\b/i.test(topic);
  const hasMultipleTimePoints =
    yearMatches.length >= 2 ||
    /\b(between\s+\d{4}\s+and\s+\d{4}|from\s+\d{4}\s+to\s+\d{4}|over\s+a\s+period|changes\s+in|two\s+different\s+points|since\s+\d{4}|1994-98)\b/i.test(topic);

  // 1. Check Maps first
  if (pLow.includes('map') || /\b(maps?\s+below|floor\s+plans?|plans?\s+below\s+show\s+the\s+(layout|ground|site|room|centre))\b/i.test(topic)) {
    const isIndoor =
      /\b(floor\s+plan|ground\s+floor|layout\s+of\s+a\s+(building|library|theatre|cinema|museum|centre|center|gallery|office|airport|department|room|hall)|student\s+common\s+room|art\s+gallery|conference\s+centre)\b/i.test(
        topic
      ) && !/\b(town|village|island|city|park|harbour|industrial\s+area)\b/i.test(topic);

    const tenseTip = hasFutureYear
      ? 'Đề có yếu tố TƯƠNG LAI (now & plans / next year) → Dùng Hiện tại đơn cho bản đồ hiện tại + "is planned to be V3 / will be V3" cho bản đồ quy hoạch!'
      : /\b(today|now|present)\b/i.test(topic) && yearMatches.length >= 1
      ? `Đề kéo dài từ ${yearMatches[0]} đến Hiện tại (today/now) → Ưu tiên Hiện tại hoàn thành bị động (has/have been constructed, has been converted)!`
      : 'Đề so sánh 2 mốc trong Quá khứ → Dùng Quá khứ đơn bị động (was demolished, was constructed, was expanded).';

    return {
      detectedFramework: isIndoor ? 'indoor_map' : 'outdoor_map',
      detectedConfidenceNote: isIndoor
        ? 'Đề mô tả mặt bằng bên trong tòa nhà/căn phòng → Khớp chuẩn Khung #6: INDOOR MAP (định vị Trái/Phải/Góc/Cửa vào).'
        : 'Đề mô tả quy hoạch không gian ngoài trời → Khớp chuẩn Khung #5: OUTDOOR MAP (định vị La bàn North/South/East/West).',
      detectedTenseTip: tenseTip,
      keyCueWords: isIndoor ? ['layout / floor plan', 'interior space'] : ['maps', 'development / changes']
    };
  }

  // 2. Check Process / Diagram
  if (
    pLow.includes('process') ||
    /\b(process\s+of|stages\s+and\s+equipment|life\s+cycle|how\s+.*\s+is\s+(produced|made|manufactured|recycled|generated)|diagrams?\s+below\s+show)\b/i.test(
      topic
    )
  ) {
    if (/\b(evolved|evolution|stone\s+age|cutting\s+tools)\b/i.test(topic)) {
      return {
        detectedFramework: 'evolution_diagram',
        detectedConfidenceNote: 'Đề so sánh sự tiến hóa/phát triển hình thái qua các thời kỳ → Khớp Khung #7: OBJECT / EVOLUTION DIAGRAM.',
        detectedTenseTip: 'Dùng Quá khứ đơn cho phiên bản cổ đại và cấu trúc so sánh hơn (larger, sharper, more refined).',
        keyCueWords: ['evolution / development', 'physical changes']
      };
    }
    if (/\b(structure\s+of|components\s+of|how\s+it\s+works|solar\s+panel)\b/i.test(topic) && !/\bstages\b/i.test(topic)) {
      return {
        detectedFramework: 'bio_diagram',
        detectedConfidenceNote: 'Đề mô tả cấu tạo bộ phận kèm cơ chế vận hành → Khớp Khung #8: STRUCTURE & FUNCTION DIAGRAM.',
        detectedTenseTip: 'Dùng Hiện tại đơn toàn bài: Body 1 tả cấu tạo bộ phận, Body 2 tả luồng vận hành.',
        keyCueWords: ['structure / components', 'how it works']
      };
    }
    const isNatural = /\b(life\s+cycle|silkworm|salmon|frog|bee|water\s+cycle|photosynthesis|erosion|headland|fossils)\b/i.test(topic);
    return {
      detectedFramework: 'process',
      detectedConfidenceNote: isNatural
        ? 'Đề mô tả quy trình Tự nhiên / Vòng đời sinh học → Khớp Khung #4: PROCESS DIAGRAM (chọn nhánh Natural Process).'
        : 'Đề mô tả các bước sản xuất / chế tạo nhân tạo → Khớp Khung #4: PROCESS DIAGRAM (chọn nhánh Man-made Process).',
      detectedTenseTip: isNatural
        ? 'Dùng Hiện tại đơn CHỦ ĐỘNG (lays eggs, hatches, grows into, erodes) cho hiện tượng tự nhiên.'
        : 'Dùng Hiện tại đơn BỊ ĐỘNG (is collected, is heated, is mixed, is packaged) cho quy trình nhân tạo.',
      keyCueWords: isNatural ? ['natural process / life cycle'] : ['man-made process', 'stages']
    };
  }

  // 3. Check Mixed Charts (2 distinct chart types or "first chart ... second chart / table")
  const chartTypesMentioned = [
    /\bpie\s+charts?\b/i.test(low),
    /\bbar\s+charts?\b/i.test(low),
    /\b(line\s+)?graphs?\b/i.test(low),
    /\btables?\b/i.test(low)
  ].filter(Boolean).length;

  if (
    pLow.includes('mixed') ||
    chartTypesMentioned >= 2 ||
    /\b(the\s+first\s+chart\s+below\s+shows.*the\s+(second\s+chart|table)\s+shows)\b/i.test(topic)
  ) {
    // Note: If two pie charts show two aspects of one household (like Australian household energy use vs greenhouse gas emissions) with NO years, Mixed Divide & Conquer (Body 1 = Chart 1, Body 2 = Chart 2) is actually the cleanest strategy!
    return {
      detectedFramework: 'mixed',
      detectedConfidenceNote:
        'Đề kết hợp 2 biểu đồ/bảng biểu chứa 2 tập dữ liệu riêng → Khớp Khung #3: MIXED CHARTS (Chia để trị: Body 1 = Hình 1, Body 2 = Hình 2).',
      detectedTenseTip: hasMultipleTimePoints
        ? 'Chú ý kiểm tra riêng từng hình: hình có nhiều năm dùng từ vựng Tăng/Giảm; hình 1 thời điểm dùng từ vựng Tỷ trọng!'
        : 'Dữ liệu tĩnh 1 thời điểm → Dùng từ vựng Tỷ trọng & So sánh (accounted for, made up, highest/lowest) cho từng hình.',
      keyCueWords: ['2 biểu đồ kết hợp', 'Divide & Conquer']
    };
  }

  // 4. Single-type Data Chart (Pie / Bar / Line / Table) -> Dynamic vs Static!
  if (pLow.includes('line') || hasMultipleTimePoints) {
    return {
      detectedFramework: 'dynamic',
      detectedConfidenceNote: `Đề có sự biến thiên qua nhiều mốc thời gian${
        yearMatches.length ? ` (${yearMatches.join(' → ')})` : ''
      } → Khớp Khung #1: DYNAMIC DATA ANALYSIS (Dùng Bảng Từ Vựng Đi lên / Đi xuống + Cấp độ).`,
      detectedTenseTip: hasFutureYear
        ? `Có mốc dự báo tương lai (${yearMatches.filter((y) => parseInt(y, 10) >= 2027).join(', ') || 'future'}) → Quá khứ dùng V2/ed, riêng đoạn tương lai bắt buộc chuyển sang "is projected / expected to + V"!`
        : 'Toàn bộ mốc năm nằm trong quá khứ → Chia Quá khứ đơn (climbed up, rose, fell, stood at) xuyên suốt!',
      keyCueWords: yearMatches.length ? yearMatches : ['time period', 'changes']
    };
  }

  // Otherwise -> Static Data Analysis!
  return {
    detectedFramework: 'static',
    detectedConfidenceNote:
      'Đề chỉ khảo sát tại 1 thời điểm (không có chuỗi năm tăng/giảm) → Khớp Khung #2: STATIC DATA ANALYSIS (Chỉ so sánh Tỷ trọng & Thứ hạng, CẤM dùng từ tăng/giảm!).',
    detectedTenseTip:
      yearMatches.length === 1
        ? `Đề có mốc năm quá khứ (${yearMatches[0]}) → Chia Quá khứ đơn (accounted for, ranked first, was), TUYỆT ĐỐI không dùng rose/fell!`
        : 'Đề không gắn mốc năm quá khứ → Chia Hiện tại đơn (accounts for, makes up, is the highest), TUYỆT ĐỐI không dùng rose/fell!',
    keyCueWords: yearMatches.length === 1 ? [yearMatches[0], '1 thời điểm tĩnh'] : ['Không có năm (Static)']
  };
}
