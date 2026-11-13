// Data & Invariant Templates for IELTS Writing Task 2 — Idea Pillars Studio & 60s Reflex Game

export type Wt2Category = 'discussion' | 'argument' | 'opinion' | 'mixed' | 'twopart';
export type Wt2TemplateId =
  | 'discussion'
  | 'argument'
  | 'opinion_v1'
  | 'opinion_v2'
  | 'mixed_ps'
  | 'mixed_ce'
  | 'twopart';

export type PillarSlotType = 'pillar' | 'cause' | 'effect' | 'example';

export interface PillarBranch {
  label: string;
  viLabel: string;
  /** Fits after "... is related to / due to / is ..." */
  pillarSlot: string;
  /** Fits after "This is/may be because of the fact that ..." (no leading 'This is because') */
  causeSlot: string;
  /** Fits after "As a result, / Consequently, ..." (no leading 'As a result,') */
  effectSlot: string;
  /** Fits after "For instance, / For example, ..." (no leading 'For instance,') */
  exampleSlot: string;
  /** 4 short memory-anchor keywords: [Pillar Hook, Cause Hook, Effect Hook, Example Source] */
  anchors: [string, string, string, string];
}

export interface Wt2Pillar {
  id: number;
  tier: 1 | 2 | 3;
  code: string;
  name: string;
  viName: string;
  icon: string;
  positive: PillarBranch;
  negative: PillarBranch;
}

export const WT2_PILLARS: Wt2Pillar[] = [
  // ==================== TIER 1: BASIC (1 - 9) ====================
  {
    id: 1,
    tier: 1,
    code: '#1',
    name: 'Freedom',
    viName: 'Sự tự do / Thiếu tự do cá nhân',
    icon: '🕊️',
    positive: {
      label: 'Freedom (Có quyền tự do lựa chọn)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'greater personal freedom',
      causeSlot:
        'by [V-ing theo đề], [S] would be free to choose, study, or do whatever they desire',
      effectSlot:
        'this would have positive effects on their mental well-being and attitude towards their work, study as well as their lives, which would in turn encourage them to work and study more efficiently and effectively',
      exampleSlot:
        "according to the Saigon Social Science Institution's survey, 83% of [S] state that their work and study performance has improved greatly in terms of efficiency and effectiveness when they have freedom in [chủ đề]",
      anchors: [
        'personal freedom',
        'free to choose / do whatever they desire',
        'positive effects on mental well-being & attitude → work efficiently',
        "Saigon Social Science Institution's survey (83%)"
      ]
    },
    negative: {
      label: 'Lack of freedom (Bị gò bó / tước đoạt tự do)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'a severe lack of freedom',
      causeSlot:
        'by [V-ing theo đề], [S] would not be free to choose, study, or do whatever they desire',
      effectSlot:
        'this would have negative effects on their mental well-being and attitude towards their work, study as well as their lives, discouraging them from performing efficiently and effectively',
      exampleSlot:
        "according to the Saigon Social Science Institution's survey, 83% of [S] report that their performance has decreased greatly in terms of efficiency and effectiveness when they do not have freedom",
      anchors: [
        'lack of freedom',
        'not be free to do whatever they desire',
        'negative effects on mental well-being & attitude',
        "Saigon Social Science Institution's survey (83% decreased)"
      ]
    }
  },
  {
    id: 2,
    tier: 1,
    code: '#2',
    name: 'Pollution',
    viName: 'Ô nhiễm không khí & tiếng ồn',
    icon: '🏭',
    positive: {
      label: 'Decreasing pollution (Giảm ô nhiễm môi trường)',
      viLabel: 'Tích cực (+)',
      pillarSlot:
        'decreasing air pollution levels, which is the most prominent and dangerous form of pollution',
      causeSlot:
        'by [V-ing theo đề], [S] would curb the excessive burning of fuel and contribute to a substantial reduction in chemical substances released into the air every day',
      effectSlot:
        'this would prevent environmental degradation, protect human health as well as mitigate global warming',
      exampleSlot:
        'WHO has recently reported a declining number of patients suffering from respiratory problems including asthma or lung cancer in cities where air quality has improved',
      anchors: [
        'decreasing air pollution levels',
        'curb excessive burning of fuel & chemical substances',
        'prevent environmental degradation & global warming',
        'WHO report — respiratory problems (asthma / lung cancer)'
      ]
    },
    negative: {
      label: 'Increasing pollution (Gia tăng ô nhiễm nghiêm trọng)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot:
        'increasing air pollution levels, which is the most prominent and dangerous form of pollution',
      causeSlot:
        'the excessive burning of fuel, which is a necessity for [driving / industrial activities theo đề], releases a huge amount of chemical substances in the air every day, polluting the atmosphere',
      effectSlot:
        'this would lead to environmental degradation, negatively affect human health as well as exacerbate global warming',
      exampleSlot:
        'WHO has recently reported a shocking number of patients in Vietnam suffering from several respiratory problems including asthma or lung cancer due to the deterioration in air quality',
      anchors: [
        'increasing air pollution levels',
        'excessive burning of fuel → chemical substances in the air',
        'environmental degradation + exacerbate global warming',
        'WHO — shocking number of patients (asthma / lung cancer)'
      ]
    }
  },
  {
    id: 3,
    tier: 1,
    code: '#3',
    name: 'Time',
    viName: 'Tiết kiệm thời gian / Lãng phí thời gian',
    icon: '⏱️',
    positive: {
      label: 'Time saving (Tiết kiệm thời gian)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'its remarkable time-saving benefit',
      causeSlot:
        '[S] would be able to travel, communicate, and manage their work much more efficiently and effectively through [chủ đề]',
      effectSlot:
        'they would have more time for their other personal interests such as spending time with their families or relaxing on vacation',
      exampleSlot:
        "according to the Hanoi Social Study's research, about 79% of [S] save at least 8 hours per week on [hoạt động theo đề]",
      anchors: [
        'time saving',
        'travel / manage work much more efficiently and effectively',
        'more time for personal interests, family & vacation',
        "Hanoi Social Study's research — 79% save 8 hours/week"
      ]
    },
    negative: {
      label: 'Time wasting / Time-consuming (Tốn kém thời gian)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'massive time wasting in daily life',
      causeSlot:
        '[S] would manage their work and daily schedules much less efficiently and effectively when [tình huống theo đề]',
      effectSlot:
        'they would have far less time for their other personal interests such as spending time with their families or relaxing on vacation',
      exampleSlot:
        "according to the Hanoi Social Study's research, about 79% of [S] waste at least 8 hours per week on [hoạt động gây tốn giờ]",
      anchors: [
        'time wasting / time-consuming',
        'manage work much less efficiently',
        'less time for family & relaxing on vacation',
        "Hanoi Social Study's research — 79% spend 8 hours/week"
      ]
    }
  },
  {
    id: 4,
    tier: 1,
    code: '#4',
    name: 'Cost',
    viName: 'Tiết kiệm chi phí / Đắt đỏ tốn kém',
    icon: '💰',
    positive: {
      label: 'Cost saving / Cheap price (Tiết kiệm chi phí)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'cost-saving affordability',
      causeSlot:
        'it would be highly economical for [S] to buy or use [chủ đề] at an affordable price',
      effectSlot:
        'they would be able to afford to buy other necessary items or save up more money for their future plans',
      exampleSlot:
        'Vietnam Economic Times has shown that an average person can save up at least 30% of his or her income by choosing [chủ đề]',
      anchors: [
        'cost saving / cheap price',
        'highly economical for S to buy / travel / run',
        'afford other necessary items & save up for future plans',
        'Vietnam Economic Times — save up at least 30% of income'
      ]
    },
    negative: {
      label: 'High cost / Expensive price (Chi phí đắt đỏ)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'excessively high costs',
      causeSlot:
        'it would be highly uneconomical for [S] to pay for or maintain [chủ đề] on a regular basis',
      effectSlot:
        'they would struggle to afford other necessary items or save up money for their future plans',
      exampleSlot:
        'Vietnam Economic Times has shown that an average person wastes at least 30% of his or her income by spending heavily on [chủ đề]',
      anchors: [
        'high cost / expensive price',
        'highly uneconomical for S',
        'struggle to save up money for future plans',
        'Vietnam Economic Times — waste 30% of income'
      ]
    }
  },
  {
    id: 5,
    tier: 1,
    code: '#5',
    name: 'Convenience',
    viName: 'Sự tiện lợi / Sự bất tiện',
    icon: '⚡',
    positive: {
      label: 'Convenience (Tiện lợi mọi lúc mọi nơi)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'unmatched daily convenience',
      causeSlot:
        '[chủ đề] would allow [S] to access services, shop, or travel more frequently on a regular basis without geographical barriers',
      effectSlot:
        'it encourages them to utilize [chủ đề] more often, which significantly promotes the efficiency of their work, study, and business',
      exampleSlot:
        'a recent Vietnamnet interview has reported that people feel much more satisfied when they can access [chủ đề] at any time they desire',
      anchors: [
        'convenience',
        'allow S to buy / travel / access on a regular basis',
        'promote the efficiency of work / study / business',
        'Vietnamnet interview — access at any time they desire'
      ]
    },
    negative: {
      label: 'Inconvenience (Bất tiện, cản trở sinh hoạt)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'considerable daily inconvenience',
      causeSlot:
        '[tình huống đề bài] would prevent [S] from traveling, shopping, or working smoothly on a regular basis',
      effectSlot:
        'this disrupts their daily routines and reduces the overall efficiency of their work, study, and business',
      exampleSlot:
        'a recent Vietnamnet interview has reported that citizens feel dissatisfied when they cannot access essential services at the time they desire',
      anchors: [
        'inconvenience',
        'prevent S from doing ... on a regular basis',
        'reduce efficiency of work / study / business',
        'Vietnamnet interview — dissatisfied with restricted access'
      ]
    }
  },
  {
    id: 6,
    tier: 1,
    code: '#6',
    name: 'Information & Knowledge',
    viName: 'Mở mang tri thức / Tin giả sai lệch',
    icon: '📚',
    positive: {
      label: 'Informative & Broadening horizons (Giàu tri thức)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'providing valuable information and knowledge',
      causeSlot:
        'by engaging with [chủ đề], [S] would be able to access a vast amount of valuable knowledge',
      effectSlot:
        'this would greatly broaden their horizons and deepen their understanding of the world',
      exampleSlot:
        'a recent sociological report indicates that [chủ đề] has helped students and citizens learn much more effectively',
      anchors: [
        'extremely informative / valuable knowledge',
        'access a vast amount of valuable knowledge',
        'greatly broaden their horizons',
        'sociological report — helped students learn more effectively'
      ]
    },
    negative: {
      label: 'Misleading / Fake information (Thông tin sai lệch)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'spreading misleading information',
      causeSlot:
        'by relying heavily on [chủ đề], [S] would easily be exposed to unverified news and fake content',
      effectSlot:
        'this would distort their perception of reality and cause unnecessary public panic',
      exampleSlot:
        'a recent sociological report indicates that [chủ đề] has caused significant anxiety among the youth due to false information',
      anchors: [
        'misleading information',
        'exposed to unverified news and fake content',
        'distort perception of reality & cause public panic',
        'sociological report — anxiety among youth from false info'
      ]
    }
  },
  {
    id: 7,
    tier: 1,
    code: '#7',
    name: 'Job',
    viName: 'Tạo cơ hội việc làm / Gây thất nghiệp',
    icon: '💼',
    positive: {
      label: 'Creates job opportunities (Tạo nhiều việc làm)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'creating abundant job opportunities',
      causeSlot:
        'this development would attract more investments and open up new markets for [ngành/đối tượng theo đề]',
      effectSlot:
        'this would lead to a lower unemployment rate and improve the living standards of many households',
      exampleSlot:
        'recent statistics from VietnamWorks have reported that this trend has successfully created thousands of jobs for [S]',
      anchors: [
        'creates job opportunities',
        'attract more investments & open up new markets',
        'lower unemployment rate & improve household living standards',
        'VietnamWorks statistics — created thousands of jobs'
      ]
    },
    negative: {
      label: 'Limits job opportunities (Thu hẹp việc làm / Thất nghiệp)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'limiting local job opportunities',
      causeSlot:
        'this shift would replace traditional human labor and shrink domestic markets for [ngành/đối tượng theo đề]',
      effectSlot:
        'this would lead to a higher unemployment rate and threaten the living standards of many households',
      exampleSlot:
        'recent statistics from VietnamWorks have reported that automation and market shifts have displaced thousands of jobs among [S]',
      anchors: [
        'limits job opportunities',
        'shrink traditional labor demand',
        'higher unemployment rate & lower living standards',
        'VietnamWorks statistics — displaced thousands of jobs'
      ]
    }
  },
  {
    id: 8,
    tier: 1,
    code: '#8',
    name: 'Unethical Issues & Morality',
    viName: 'Vấn đề vi phạm đạo đức & chuẩn mực xã hội',
    icon: '⚖️',
    positive: {
      label: 'Protecting moral standards (Bảo vệ chuẩn mực đạo đức)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'upholding ethical standards and protecting vulnerable groups',
      causeSlot:
        'strictly regulating [chủ đề] prevents the exploitation of vulnerable groups such as children and safeguards fundamental rights',
      effectSlot:
        'societal values and public trust are preserved across the community',
      exampleSlot:
        'global ethical committees have widely praised nations that enforce strict regulations on [chủ đề] to protect citizens',
      anchors: [
        'upholding ethical standards',
        'prevent exploitation of vulnerable groups & fundamental rights',
        'protect societal values & public trust',
        'global ethical committees praise strict regulations'
      ]
    },
    negative: {
      label: 'Unethical & Moral concerns (Trái đạo đức, cần cấm)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'raising serious unethical issues and moral concerns',
      causeSlot:
        'the practice of [chủ đề] often violates fundamental rights, invades personal privacy, or exploits vulnerable groups such as children',
      effectSlot:
        'many believe that this is fundamentally wrong and should be strictly prohibited or heavily regulated by the authorities to protect societal values',
      exampleSlot:
        'a clear example of this is when commercial organizations use [chủ đề] to manipulate or exploit others for profit, which has been widely condemned by global ethical committees',
      anchors: [
        'unethical issues and moral concerns',
        'violates fundamental rights / exploits vulnerable groups',
        'fundamentally wrong → strictly prohibited by authorities',
        'widely condemned by global ethical committees'
      ]
    }
  },
  {
    id: 9,
    tier: 1,
    code: '#9',
    name: 'Bond & Social Interaction',
    viName: 'Gắn kết tình cảm / Cô lập xã hội',
    icon: '🤝',
    positive: {
      label: 'Strengthens social bonds (Tăng gắn kết cộng đồng)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'strengthening social bonds',
      causeSlot:
        'participating in [hoạt động theo đề] increases face-to-face interactions among [S]',
      effectSlot:
        'the bond between them would be strengthened, potentially leading to a strong sense of community',
      exampleSlot:
        'a psychological report has shown that [S] often feel much more connected to their peers when they engage in [hoạt động theo đề]',
      anchors: [
        'strengthens social bonds',
        'participating in ... increases face-to-face interactions',
        'bond strengthened → sense of community',
        'psychological report — feel more connected to peers'
      ]
    },
    negative: {
      label: 'Weakens social bonds (Làm phai nhạt tình cảm, cô lập)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'weakening social bonds',
      causeSlot:
        'relying heavily on [chủ đề] drastically reduces face-to-face interactions among [S]',
      effectSlot:
        'the bond between them would be severely weakened, potentially leading to a pervasive sense of isolation',
      exampleSlot:
        'a psychological report has shown that [S] often feel disconnected from their peers when they spend excessive time on [chủ đề]',
      anchors: [
        'weakens social bonds',
        'relying heavily on ... reduces face-to-face interactions',
        'bond severely weakened → sense of isolation',
        'psychological report — feel disconnected from peers'
      ]
    }
  },

  // ==================== TIER 2: ADVANCED (10 - 13) ====================
  {
    id: 10,
    tier: 2,
    code: '#10',
    name: 'Health',
    viName: 'Cải thiện / Suy giảm sức khỏe thể chất & tinh thần',
    icon: '🩺',
    positive: {
      label: 'Improving physical & mental health (Nâng cao sức khỏe)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'improving physical and mental health',
      causeSlot:
        'by [V-ing theo đề], [S] would not be exposed to a sedentary lifestyle or high levels of daily stress',
      effectSlot:
        'this would have positive effects on their overall well-being and prevent serious health problems such as obesity, heart disease, or depression',
      exampleSlot:
        "according to the Ministry of Health's report, there has been a significant decrease in the number of patients suffering from lifestyle illnesses due to [chủ đề]",
      anchors: [
        'improving physical and mental health',
        'avoid sedentary lifestyle & high levels of stress',
        'prevent obesity, heart disease, or depression',
        "Ministry of Health's report — decrease in patients"
      ]
    },
    negative: {
      label: 'Deteriorating physical & mental health (Suy giảm sức khỏe)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'deteriorating physical and mental health',
      causeSlot:
        'when [V-ing / tình huống theo đề], [S] would be exposed to a sedentary lifestyle and high levels of stress',
      effectSlot:
        'this would have negative effects on their overall well-being and could lead to serious health problems such as obesity, heart disease, or depression',
      exampleSlot:
        "according to the Ministry of Health's report, there has been a significant increase in the number of patients suffering from obesity and chronic stress due to [chủ đề]",
      anchors: [
        'deteriorating physical and mental health',
        'exposed to sedentary lifestyle / high levels of stress',
        'lead to obesity, heart disease, or depression',
        "Ministry of Health's report — increase in patients"
      ]
    }
  },
  {
    id: 11,
    tier: 2,
    code: '#11',
    name: 'Culture & Tradition',
    viName: 'Bảo tồn văn hóa / Đánh mất bản sắc dân tộc',
    icon: '🏛️',
    positive: {
      label: 'Preserving culture & Enriching understanding (Bảo tồn văn hóa)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'preserving cultural identities and traditional values',
      causeSlot:
        '[S] would have more opportunities to be exposed to traditional customs and cultural heritage through [chủ đề]',
      effectSlot:
        'this would help to enrich their cultural understanding, which is essential for the younger generation',
      exampleSlot:
        'a recent survey by the Ministry of Culture has shown that about 75% of young people feel more connected to their roots when they experience [chủ đề]',
      anchors: [
        'preserving cultural identities & traditional values',
        'more opportunities to be exposed to traditional customs',
        'enrich cultural understanding (essential for youth)',
        'Ministry of Culture survey — 75% feel connected to roots'
      ]
    },
    negative: {
      label: 'Losing cultural identities (Xói mòn bản sắc truyền thống)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'losing cultural identities and traditional values',
      causeSlot:
        '[S] would have fewer opportunities to engage with traditional customs because of [chủ đề]',
      effectSlot:
        'this would gradually erode their national identity, which is harmful for the younger generation',
      exampleSlot:
        'a recent survey by the Ministry of Culture has shown that about 75% of young people feel disconnected from their roots when [tình huống theo đề]',
      anchors: [
        'losing cultural identities & traditional values',
        'fewer opportunities for traditional customs',
        'erode national identity (harmful for youth)',
        'Ministry of Culture survey — 75% disconnected from roots'
      ]
    }
  },
  {
    id: 12,
    tier: 2,
    code: '#12',
    name: 'Crime & Social Order',
    viName: 'Giảm tỷ lệ tội phạm / Gây bất ổn xã hội',
    icon: '🚨',
    positive: {
      label: 'Reducing crime rates (Giữ gìn trật tự & an toàn xã hội)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'reducing crime rates and maintaining social order',
      causeSlot:
        '[S] would receive proper education, financial support, or strict supervision when [giải pháp/chủ đề]',
      effectSlot:
        'this would deter illegal behaviors and create a safer and more stable society',
      exampleSlot:
        'criminology reports consistently show that areas with high levels of [giáo dục/giám sát theo đề] often experience a dramatic drop in juvenile delinquency',
      anchors: [
        'reducing crime rates',
        'receive proper education, financial support, or strict supervision',
        'create a safer and more stable society',
        'criminology reports — dramatic drop in juvenile delinquency'
      ]
    },
    negative: {
      label: 'Breeding social unrest & crime (Gia tăng tội phạm)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'breeding social unrest and criminal activities',
      causeSlot:
        '[S] would not receive proper education, financial support, or strict supervision when [tình huống theo đề]',
      effectSlot:
        'this would drive individuals towards illegal behaviors such as theft or vandalism to fulfill their needs',
      exampleSlot:
        'criminology reports consistently show that areas with high levels of [vấn đề theo đề] often experience a dramatic surge in juvenile delinquency',
      anchors: [
        'breeding social unrest & criminal activities',
        'not receive proper education / strict supervision',
        'drive individuals towards theft or vandalism',
        'criminology reports — dramatic surge in juvenile delinquency'
      ]
    }
  },
  {
    id: 13,
    tier: 2,
    code: '#13',
    name: 'Resource',
    viName: 'Phát triển bền vững / Cạn kiệt tài nguyên thiên nhiên',
    icon: '🌱',
    positive: {
      label: 'Promoting sustainable development (Bảo tồn tài nguyên)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'promoting sustainable development',
      causeSlot:
        'by [V-ing theo đề], there would be a massive reduction in the consumption of natural resources such as fossil fuels, clean water, and forests',
      effectSlot:
        'this would relieve pressure on the ecosystem and ensure a greener future for the next generations',
      exampleSlot:
        'the UN Environment Programme has emphasized that transitioning to [giải pháp xanh theo đề] is vital to avoid an irreversible environmental crisis by 2050',
      anchors: [
        'promoting sustainable development',
        'massive reduction in fossil fuels, clean water & forests use',
        'ensure a greener future for next generations',
        'UN Environment Programme — avoid crisis by 2050'
      ]
    },
    negative: {
      label: 'Accelerating resource depletion (Cạn kiệt tài nguyên)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'accelerating resource depletion',
      causeSlot:
        'when [tình huống theo đề], there would be an excessive consumption of natural resources such as fossil fuels, clean water, and forests',
      effectSlot:
        "this would put enormous pressure on the Earth's ecosystem, leading to severe shortages",
      exampleSlot:
        'the UN Environment Programme has warned that if we continue to rely on [chủ đề gây hại], we will face an irreversible environmental crisis by 2050',
      anchors: [
        'accelerating resource depletion',
        'excessive consumption of fossil fuels, clean water & forests',
        "enormous pressure on Earth's ecosystem → severe shortages",
        'UN Environment Programme — irreversible crisis by 2050'
      ]
    }
  },

  // ==================== TIER 3: PRO MASTER (14 - 19) ====================
  {
    id: 14,
    tier: 3,
    code: '#14',
    name: 'Motivation & Independence',
    viName: 'Rèn tính tự lập / Làm con người ỷ lại thụ động',
    icon: '🚀',
    positive: {
      label: 'Fostering independence (Thúc đẩy tính tự lập & bản lĩnh)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'fostering independence and self-reliance',
      causeSlot:
        'when [S] are encouraged to overcome challenges by themselves through [chủ đề], they would step out of their comfort zones',
      effectSlot:
        'this would cultivate a strong sense of responsibility and problem-solving skills',
      exampleSlot:
        'educational psychologists emphasize that young adults who are accustomed to [chủ đề] often demonstrate higher resilience when facing real-life difficulties',
      anchors: [
        'fostering independence',
        'overcome challenges by themselves → step out of comfort zones',
        'cultivate responsibility & problem-solving skills',
        'educational psychologists — higher resilience in real life'
      ]
    },
    negative: {
      label: 'Demotivating & Passive dependence (Gây ỷ lại, thụ động)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'demotivating individuals and breeding over-dependence',
      causeSlot:
        'when [S] are heavily reliant on [chủ đề], they would not step out of their comfort zones',
      effectSlot:
        'this would make them become passive and highly dependent on others in daily life',
      exampleSlot:
        'educational psychologists emphasize that young adults who are overly reliant on [chủ đề] often demonstrate lower resilience when facing real-life difficulties',
      anchors: [
        'demotivating individuals',
        'heavily reliant on ... → not step out of comfort zones',
        'become passive and highly dependent on others',
        'educational psychologists — lower resilience in real life'
      ]
    }
  },
  {
    id: 15,
    tier: 3,
    code: '#15',
    name: 'Creativity & Innovation',
    viName: 'Kích thích sáng tạo / Kìm hãm tư duy đổi mới',
    icon: '🎨',
    positive: {
      label: 'Fostering creativity & innovation (Khơi dậy sáng tạo)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'fostering creativity and innovation',
      causeSlot:
        '[S] would be encouraged to think outside the box and explore new ideas when engaging in [chủ đề]',
      effectSlot:
        'this would stimulate their imagination and cognitive development, which is vital for their future success',
      exampleSlot:
        'educational research in Finland highlights that students who frequently engage in [chủ đề] are much more likely to develop innovative solutions to complex problems',
      anchors: [
        'fostering creativity and innovation',
        'think outside the box & explore new ideas',
        'stimulate imagination (vital for future success)',
        'educational research in Finland — innovative solutions'
      ]
    },
    negative: {
      label: 'Stifling creativity & innovation (Bóp nghẹt sự sáng tạo)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'stifling creativity and innovation',
      causeSlot:
        '[S] would not be encouraged to think outside the box and explore new ideas when restricted by [chủ đề]',
      effectSlot:
        'this would limit their cognitive development and imagination, hindering their future success',
      exampleSlot:
        'educational research in Finland highlights that students confined to rigid routines without [chủ đề] struggle to develop innovative solutions to complex problems',
      anchors: [
        'stifling creativity and innovation',
        'not encouraged to think outside the box',
        'limit cognitive development & imagination',
        'educational research in Finland — struggle with complex problems'
      ]
    }
  },
  {
    id: 16,
    tier: 3,
    code: '#16',
    name: 'Practical Skills',
    viName: 'Trang bị kỹ năng thực tiễn / Thiếu kỹ năng sống',
    icon: '🛠️',
    positive: {
      label: 'Equipping practical life skills (Trang bị kỹ năng thực tế)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'equipping [S] with practical life skills',
      causeSlot:
        'by participating in [chủ đề], [S] would have the chance to practice essential skills such as teamwork, problem-solving, and time management',
      effectSlot:
        'this would thoroughly prepare them for the real-world challenges in their independent lives',
      exampleSlot:
        'an HR survey by VietnamWorks revealed that over 80% of employers prefer candidates who have gained hands-on experience through [chủ đề]',
      anchors: [
        'equipping practical life skills',
        'practice teamwork, problem-solving & time management',
        'thoroughly prepare for real-world challenges',
        'HR survey by VietnamWorks — over 80% of employers prefer hands-on experience'
      ]
    },
    negative: {
      label: 'Failing to equip practical skills (Thiếu hụt kỹ năng thực tế)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'failing to equip [S] with practical life skills',
      causeSlot:
        'by relying too much on theoretical study or [chủ đề], [S] would not have the chance to practice essential skills such as teamwork, problem-solving, and time management',
      effectSlot:
        'this would make them struggle with the real-world challenges in their independent lives',
      exampleSlot:
        'an HR survey by VietnamWorks revealed that over 80% of employers reject candidates who lack hands-on experience beyond [chủ đề]',
      anchors: [
        'failing to equip practical life skills',
        'no chance to practice teamwork, problem-solving & time management',
        'struggle with real-world challenges',
        'HR survey by VietnamWorks — over 80% of employers'
      ]
    }
  },
  {
    id: 17,
    tier: 3,
    code: '#17',
    name: 'Economic Impact',
    viName: 'Thúc đẩy kinh tế / Gánh nặng thâm hụt ngân sách',
    icon: '📈',
    positive: {
      label: 'Boosting the economy (Thúc đẩy tăng trưởng kinh tế)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'boosting the national and local economy',
      causeSlot:
        '[chủ đề] would attract more foreign investments and generate enormous tax revenues for the state',
      effectSlot:
        'this would greatly contribute to national prosperity and public welfare',
      exampleSlot:
        "the Ministry of Finance's recent data indicates that investing in [chủ đề] has successfully boosted the local economy",
      anchors: [
        'boosting the economy',
        'attract foreign investments & generate enormous tax revenues',
        'greatly contribute to national prosperity',
        "Ministry of Finance's data — boosted local economy"
      ]
    },
    negative: {
      label: 'Financial burden on government (Thâm hụt ngân sách nhà nước)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'causing a heavy financial burden on the government',
      causeSlot:
        '[chủ đề] would require massive funding from the national budget to maintain and operate',
      effectSlot:
        'this would lead to budget deficits, leaving less money for other crucial sectors like healthcare or education',
      exampleSlot:
        "the Ministry of Finance's recent data indicates that investing in [chủ đề] has cost the government billions of dollars annually without practical returns",
      anchors: [
        'financial burden on the government',
        'require massive funding from national budget to maintain',
        'lead to budget deficits → less money for healthcare or education',
        "Ministry of Finance's data — cost billions annually"
      ]
    }
  },
  {
    id: 18,
    tier: 3,
    code: '#18',
    name: 'Security & Privacy',
    viName: 'Tăng cường an ninh / Xâm phạm quyền riêng tư',
    icon: '🔒',
    positive: {
      label: 'Enhancing security (Tăng cường an ninh & bảo mật)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'enhancing public security and data protection',
      causeSlot:
        'public spaces and sensitive records would be closely protected by authorities through [chủ đề]',
      effectSlot:
        'it helps to deter crimes, safeguard sensitive information, and maintain public order',
      exampleSlot:
        'the Global Security Council has reported that crime rates have dropped by 30% since the implementation of [chủ đề]',
      anchors: [
        'enhancing security',
        'closely monitored / protected by authorities',
        'deter crimes & maintain public order',
        'Global Security Council — crime rates dropped by 30%'
      ]
    },
    negative: {
      label: 'Invading personal privacy (Đe dọa quyền riêng tư & dữ liệu)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'invading personal privacy and data security',
      causeSlot:
        "personal data would be closely monitored or widely shared on the internet when using [chủ đề]",
      effectSlot:
        "this poses a severe threat to individuals' private lives and sensitive information",
      exampleSlot:
        'the Global Security Council has reported that cybercrimes have risen by 30% since the widespread use of [chủ đề]',
      anchors: [
        'invading personal privacy',
        'widely shared on the internet / closely monitored',
        "severe threat to private lives & sensitive information",
        'Global Security Council — cybercrimes risen by 30%'
      ]
    }
  },
  {
    id: 19,
    tier: 3,
    code: '#19',
    name: 'Equality / Disparity',
    viName: 'Thúc đẩy bình đẳng xã hội / Nới rộng khoảng cách giàu nghèo',
    icon: '⚖️',
    positive: {
      label: 'Promoting social equality (Thúc đẩy công bằng xã hội)',
      viLabel: 'Tích cực (+)',
      pillarSlot: 'promoting social equality across society',
      causeSlot:
        '[chủ đề] would provide equal access to essential resources such as education, healthcare, and technology for all citizens',
      effectSlot:
        'this would bridge the social divide, creating a fairer and more stable society',
      exampleSlot:
        'recent statistics from the World Bank indicate that countries investing heavily in [chủ đề] have successfully reduced poverty rates',
      anchors: [
        'promoting equality',
        'provide equal access to education, healthcare & technology',
        'bridge the social divide → creating a fairer society',
        'World Bank statistics — reduced poverty rates'
      ]
    },
    negative: {
      label: 'Widening rich-poor gap (Nới rộng bất bình đẳng giàu nghèo)',
      viLabel: 'Tiêu cực (-)',
      pillarSlot: 'widening the gap between the rich and the poor',
      causeSlot:
        '[chủ đề] would limit the availability of essential resources such as education, healthcare, and technology for low-income groups',
      effectSlot:
        'this would exacerbate social inequality, creating a more polarized society',
      exampleSlot:
        'recent statistics from the World Bank indicate that countries neglecting [chủ đề] have seen a sharp increase in wealth disparity',
      anchors: [
        'widening the gap between the rich and the poor',
        'limit availability of education, healthcare & technology',
        'exacerbate social inequality → polarized society',
        'World Bank statistics — sharp increase in wealth disparity'
      ]
    }
  }
];

export interface SubjectGroup {
  id: string;
  title: string;
  subtitle: string;
  chips: { en: string; vi: string }[];
}

export const WT2_SUBJECT_GROUPS: SubjectGroup[] = [
  {
    id: 'age',
    title: 'Nhóm 1: Độ tuổi & Gia đình',
    subtitle: 'Thay thế cho children / students',
    chips: [
      { en: 'offspring', vi: 'con cái (gia đình)' },
      { en: 'youngsters', vi: 'giới trẻ / thiếu niên' },
      { en: 'adolescents', vi: 'thanh thiếu niên' },
      { en: 'young adults', vi: 'thanh niên trưởng thành' },
      { en: 'undergraduates', vi: 'sinh viên đại học' },
      { en: 'senior citizens', vi: 'người cao tuổi' }
    ]
  },
  {
    id: 'econ',
    title: 'Nhóm 2: Kinh tế & Giao thông',
    subtitle: 'Ghép cực ăn với Job, Cost, Time, Pollution',
    chips: [
      { en: 'the workforce', vi: 'lực lượng lao động' },
      { en: 'employees', vi: 'người đi làm' },
      { en: 'daily commuters', vi: 'người đi làm hằng ngày' },
      { en: 'passengers', vi: 'hành khách' },
      { en: 'consumers', vi: 'người tiêu dùng' },
      { en: 'viewers and audiences', vi: 'khán giả truyền thông' }
    ]
  },
  {
    id: 'macro',
    title: 'Nhóm 3: Tổ chức & Vĩ mô',
    subtitle: 'Chính phủ, Trường học, Doanh nghiệp',
    chips: [
      { en: 'policymakers', vi: 'nhà hoạch định chính sách' },
      { en: 'authorities', vi: 'các nhà chức trách' },
      { en: 'the government', vi: 'chính phủ' },
      { en: 'educational institutions', vi: 'các cơ sở giáo dục' },
      { en: 'corporations', vi: 'các tập đoàn lớn' },
      { en: 'local communities', vi: 'cộng đồng địa phương' }
    ]
  },
  {
    id: 'people',
    title: 'Nhóm 4: Thay chữ "People"',
    subtitle: 'Tránh lặp từ people / individuals',
    chips: [
      { en: 'citizens', vi: 'công dân' },
      { en: 'members of society', vi: 'các thành viên xã hội' },
      { en: 'urban dwellers', vi: 'cư dân thành thị' },
      { en: 'households', vi: 'các hộ gia đình' },
      { en: 'the younger generation', vi: 'thế hệ trẻ' }
    ]
  }
];

export interface StructurePartToken {
  type: 'text' | 'topic_input' | 'pillar_slot';
  text?: string;
  /** Used in Level 2 Memory Mode to blank out key template connectors */
  memoryHint?: string;
  slotKey?: string;
  placeholder?: string;
  bodyIndex?: 1 | 2;
  pillarCol?: PillarSlotType;
}

export interface Wt2StructureDef {
  id: Wt2TemplateId;
  category: Wt2Category;
  name: string;
  viSubtitle: string;
  supportsStance?: boolean;
  /** Whether Body 2 uses Pillar cards (true for 6 templates; for mixed_ps Body 2 uses Solutions + Pillar 2 Effect) */
  body2UsesFullPillar: boolean;
  buildParagraphs: (stance: 'agree' | 'disagree') => {
    sectionTitle: string;
    borderColor: string;
    tokens: StructurePartToken[];
  }[];
}

export const WT2_STRUCTURES: Record<Wt2TemplateId, Wt2StructureDef> = {
  discussion: {
    id: 'discussion',
    category: 'discussion',
    name: 'Discussion: Discuss Both Views',
    viSubtitle: 'Thảo luận 2 luồng ý kiến (Body 1: Ý không ủng hộ → Body 2: Ý ủng hộ)',
    body2UsesFullPillar: true,
    buildParagraphs: () => [
      {
        sectionTitle: '📝 Introduction',
        borderColor: '#0ea5e9',
        tokens: [
          { type: 'text', text: 'Over the last few decades, the world has seen that ', memoryHint: 'Over the last few decades, ...' },
          { type: 'topic_input', slotKey: 'intro_v1', placeholder: 'Quan điểm 1 của đề (mệnh đề S + V)' },
          { type: 'text', text: '. However, others see that ', memoryHint: '. However, others ...' },
          { type: 'topic_input', slotKey: 'intro_v2', placeholder: 'Quan điểm 2 của đề (mệnh đề S + V)' },
          { type: 'text', text: '. This essay will discuss both points of view and argue that ', memoryHint: '. This essay will discuss ...' },
          { type: 'topic_input', slotKey: 'intro_thesis', placeholder: 'Quan điểm cá nhân em ủng hộ (thường là Quan điểm 2)' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '💡 Body Paragraph 1 (Bàn về Quan điểm 1 — Ý không ủng hộ)',
        borderColor: '#8b5cf6',
        tokens: [
          { type: 'text', text: 'The main reason some people believe ', memoryHint: 'The main reason some people ...' },
          { type: 'topic_input', slotKey: 'b1_view', placeholder: 'Tóm tắt Quan điểm 1 (S + V)' },
          { type: 'text', text: ' is related to ' },
          { type: 'pillar_slot', slotKey: 'b1_pillar', bodyIndex: 1, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 1]' },
          { type: 'text', text: '. This may be because of the fact that ', memoryHint: '. This may be because ...' },
          { type: 'pillar_slot', slotKey: 'b1_cause', bodyIndex: 1, pillarCol: 'cause', placeholder: 'Thả [Cause 1 - Nguyên nhân]' },
          { type: 'text', text: '. As a result, ' },
          { type: 'pillar_slot', slotKey: 'b1_effect', bodyIndex: 1, pillarCol: 'effect', placeholder: 'Thả [Effect 1 - Kết quả]' },
          { type: 'text', text: '. For instance, ' },
          { type: 'pillar_slot', slotKey: 'b1_example', bodyIndex: 1, pillarCol: 'example', placeholder: 'Thả [Example 1 - Ví dụ số liệu]' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '💡 Body Paragraph 2 (Bàn về Quan điểm 2 — Ý em ủng hộ)',
        borderColor: '#f59e0b',
        tokens: [
          { type: 'text', text: 'However, I would argue that ', memoryHint: 'However, I would argue ...' },
          { type: 'topic_input', slotKey: 'b2_view', placeholder: 'Cụm V-ing / Danh từ chỉ Quan điểm 2' },
          { type: 'text', text: ' is a much stronger argument due to ', memoryHint: ' is a much stronger argument due to ' },
          { type: 'pillar_slot', slotKey: 'b2_pillar', bodyIndex: 2, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 2]' },
          { type: 'text', text: '. This is because of the fact that ' },
          { type: 'pillar_slot', slotKey: 'b2_cause', bodyIndex: 2, pillarCol: 'cause', placeholder: 'Thả [Cause 2 - Nguyên nhân]' },
          { type: 'text', text: '. Consequently, ' },
          { type: 'pillar_slot', slotKey: 'b2_effect', bodyIndex: 2, pillarCol: 'effect', placeholder: 'Thả [Effect 2 - Kết quả]' },
          { type: 'text', text: '. For example, ' },
          { type: 'pillar_slot', slotKey: 'b2_example', bodyIndex: 2, pillarCol: 'example', placeholder: 'Thả [Example 2 - Ví dụ số liệu]' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '✅ Conclusion',
        borderColor: '#10b981',
        tokens: [
          { type: 'text', text: 'To sum up, although some people argue that ', memoryHint: 'To sum up, although ...' },
          { type: 'topic_input', slotKey: 'conc_v1', placeholder: 'Tóm tắt lại Quan điểm 1' },
          { type: 'text', text: ', I would argue there is sufficient evidence to demonstrate that ', memoryHint: ', I would argue there is sufficient evidence ...' },
          { type: 'topic_input', slotKey: 'conc_v2', placeholder: 'Khẳng định lại Quan điểm 2 em ủng hộ' },
          { type: 'text', text: ', and therefore ' },
          { type: 'topic_input', slotKey: 'conc_final', placeholder: 'Lời khuyên / Chốt lại vấn đề' },
          { type: 'text', text: '.' }
        ]
      }
    ]
  },

  argument: {
    id: 'argument',
    category: 'argument',
    name: 'Argument: Advantages & Disadvantages (Outweigh)',
    viSubtitle: 'Phân tích mặt Lợi ở Body 1 (Advantage) và mặt Hại ở Body 2 (Disadvantage)',
    body2UsesFullPillar: true,
    buildParagraphs: () => [
      {
        sectionTitle: '📝 Introduction',
        borderColor: '#0ea5e9',
        tokens: [
          { type: 'text', text: 'Over the last few decades, the world has seen that ' },
          { type: 'topic_input', slotKey: 'intro_topic', placeholder: 'Xu hướng / Chủ đề đề bài nêu (S + V)' },
          { type: 'text', text: '. However, others see that this is not entirely positive. This essay will firstly discuss ' },
          { type: 'pillar_slot', slotKey: 'b1_pillar', bodyIndex: 1, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 1 - Lợi ích]' },
          { type: 'text', text: ' as one of the main advantages of this development and then outline ' },
          { type: 'pillar_slot', slotKey: 'b2_pillar', bodyIndex: 2, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 2 - Bất lợi]' },
          { type: 'text', text: ' as one of the main disadvantages of it.' }
        ]
      },
      {
        sectionTitle: '💡 Body Paragraph 1 (Advantage — Mặt tích cực)',
        borderColor: '#8b5cf6',
        tokens: [
          { type: 'text', text: 'One of the principal advantages of ' },
          { type: 'topic_input', slotKey: 'b1_topic_np', placeholder: 'Cụm danh từ / V-ing chủ đề' },
          { type: 'text', text: ' is ' },
          { type: 'pillar_slot', slotKey: 'b1_pillar', bodyIndex: 1, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 1]' },
          { type: 'text', text: '. This is because of the fact that ' },
          { type: 'pillar_slot', slotKey: 'b1_cause', bodyIndex: 1, pillarCol: 'cause', placeholder: 'Thả [Cause 1]' },
          { type: 'text', text: '. As a result, ' },
          { type: 'pillar_slot', slotKey: 'b1_effect', bodyIndex: 1, pillarCol: 'effect', placeholder: 'Thả [Effect 1]' },
          { type: 'text', text: '. For instance, ' },
          { type: 'pillar_slot', slotKey: 'b1_example', bodyIndex: 1, pillarCol: 'example', placeholder: 'Thả [Example 1]' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '💡 Body Paragraph 2 (Disadvantage — Mặt bất lợi)',
        borderColor: '#f59e0b',
        tokens: [
          { type: 'text', text: 'The main disadvantage associated with ' },
          { type: 'topic_input', slotKey: 'b2_topic_np', placeholder: 'Cụm danh từ / V-ing chủ đề (paraphrase)' },
          { type: 'text', text: ' is ' },
          { type: 'pillar_slot', slotKey: 'b2_pillar', bodyIndex: 2, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 2]' },
          { type: 'text', text: '. This is because of the fact that ' },
          { type: 'pillar_slot', slotKey: 'b2_cause', bodyIndex: 2, pillarCol: 'cause', placeholder: 'Thả [Cause 2]' },
          { type: 'text', text: '. Consequently, ' },
          { type: 'pillar_slot', slotKey: 'b2_effect', bodyIndex: 2, pillarCol: 'effect', placeholder: 'Thả [Effect 2]' },
          { type: 'text', text: '. For example, ' },
          { type: 'pillar_slot', slotKey: 'b2_example', bodyIndex: 2, pillarCol: 'example', placeholder: 'Thả [Example 2]' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '✅ Conclusion',
        borderColor: '#10b981',
        tokens: [
          { type: 'text', text: 'To sum up, although there are some advantages in ' },
          { type: 'topic_input', slotKey: 'conc_topic', placeholder: 'Cụm danh từ chủ đề' },
          { type: 'text', text: ', such as ' },
          { type: 'topic_input', slotKey: 'conc_adv', placeholder: 'Tóm tắt ngắn Lợi ích 1' },
          { type: 'text', text: ', these are perhaps outweighed by the significant disadvantages like ' },
          { type: 'topic_input', slotKey: 'conc_disadv', placeholder: 'Tóm tắt ngắn Bất lợi 2' },
          { type: 'text', text: '.' }
        ]
      }
    ]
  },

  opinion_v1: {
    id: 'opinion_v1',
    category: 'opinion',
    name: 'Opinion Version 1: One-sided (100% Agree / Disagree)',
    viSubtitle: 'Bảo vệ hoàn toàn 1 phía bằng 2 Trụ ý song song',
    supportsStance: true,
    body2UsesFullPillar: true,
    buildParagraphs: (stance) => {
      const verb = stance === 'agree' ? 'agree' : 'disagree';
      const noun = stance === 'agree' ? 'agreement' : 'disagreement';
      return [
        {
          sectionTitle: `📝 Introduction (100% ${verb.toUpperCase()})`,
          borderColor: '#0ea5e9',
          tokens: [
            { type: 'text', text: 'Over the last few decades, the world has seen that ' },
            { type: 'topic_input', slotKey: 'intro_ctx', placeholder: 'Bối cảnh / Sự việc đề bài nêu (S + V)' },
            { type: 'text', text: `. I completely ${verb} with the argument that ` },
            { type: 'topic_input', slotKey: 'intro_claim', placeholder: 'Quan điểm / Đề xuất của đề bài' },
            { type: 'text', text: '. This essay will firstly discuss ' },
            { type: 'pillar_slot', slotKey: 'b1_pillar', bodyIndex: 1, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 1]' },
            { type: 'text', text: ` as one of the main reasons for my ${noun}, and then outline ` },
            { type: 'pillar_slot', slotKey: 'b2_pillar', bodyIndex: 2, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 2]' },
            { type: 'text', text: ' as another prominent factor.' }
          ]
        },
        {
          sectionTitle: '💡 Body Paragraph 1 (Lý do thứ nhất)',
          borderColor: '#8b5cf6',
          tokens: [
            { type: 'text', text: `One of the principal reasons why I ${verb} with ` },
            { type: 'topic_input', slotKey: 'b1_topic', placeholder: 'Cụm V-ing / Danh từ chủ đề đang bàn' },
            { type: 'text', text: ' is ' },
            { type: 'pillar_slot', slotKey: 'b1_pillar', bodyIndex: 1, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 1]' },
            { type: 'text', text: '. This is because of the fact that ' },
            { type: 'pillar_slot', slotKey: 'b1_cause', bodyIndex: 1, pillarCol: 'cause', placeholder: 'Thả [Cause 1]' },
            { type: 'text', text: '. As a result, ' },
            { type: 'pillar_slot', slotKey: 'b1_effect', bodyIndex: 1, pillarCol: 'effect', placeholder: 'Thả [Effect 1]' },
            { type: 'text', text: '. For instance, ' },
            { type: 'pillar_slot', slotKey: 'b1_example', bodyIndex: 1, pillarCol: 'example', placeholder: 'Thả [Example 1]' },
            { type: 'text', text: '.' }
          ]
        },
        {
          sectionTitle: '💡 Body Paragraph 2 (Lý do thứ hai)',
          borderColor: '#f59e0b',
          tokens: [
            { type: 'text', text: `Another main reason to support my ${noun} is ` },
            { type: 'pillar_slot', slotKey: 'b2_pillar', bodyIndex: 2, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 2]' },
            { type: 'text', text: '. This is due to the fact that ' },
            { type: 'pillar_slot', slotKey: 'b2_cause', bodyIndex: 2, pillarCol: 'cause', placeholder: 'Thả [Cause 2]' },
            { type: 'text', text: '. Consequently, ' },
            { type: 'pillar_slot', slotKey: 'b2_effect', bodyIndex: 2, pillarCol: 'effect', placeholder: 'Thả [Effect 2]' },
            { type: 'text', text: '. For example, ' },
            { type: 'pillar_slot', slotKey: 'b2_example', bodyIndex: 2, pillarCol: 'example', placeholder: 'Thả [Example 2]' },
            { type: 'text', text: '.' }
          ]
        },
        {
          sectionTitle: '✅ Conclusion',
          borderColor: '#10b981',
          tokens: [
            { type: 'text', text: `To sum up, I completely ${verb} that ` },
            { type: 'topic_input', slotKey: 'conc_claim', placeholder: 'Nhắc lại quan điểm / Đề xuất' },
            { type: 'text', text: ', mainly because of ' },
            { type: 'topic_input', slotKey: 'conc_p1', placeholder: 'Tóm tắt Trụ ý 1' },
            { type: 'text', text: ' and ' },
            { type: 'topic_input', slotKey: 'conc_p2', placeholder: 'Tóm tắt Trụ ý 2' },
            { type: 'text', text: '.' }
          ]
        }
      ];
    }
  },

  opinion_v2: {
    id: 'opinion_v2',
    category: 'opinion',
    name: 'Opinion Version 2: Concession (Nhượng bộ & Phản biện)',
    viSubtitle: 'Body 1 nhượng bộ 1 ý hợp lý → Body 2 bảo vệ quan điểm chính (cực hợp đề có từ all / best / only)',
    supportsStance: true,
    body2UsesFullPillar: true,
    buildParagraphs: (stance) => {
      const verb = stance === 'agree' ? 'agree' : 'disagree';
      const noun = stance === 'agree' ? 'agreement' : 'disagreement';
      return [
        {
          sectionTitle: `📝 Introduction (Concession — Strongly ${verb})`,
          borderColor: '#0ea5e9',
          tokens: [
            { type: 'text', text: 'Over the last few decades, the world has seen that ' },
            { type: 'topic_input', slotKey: 'intro_ctx', placeholder: 'Bối cảnh chung của đề bài (S + V)' },
            { type: 'text', text: '. Some people argue that ' },
            { type: 'topic_input', slotKey: 'intro_prompt_view', placeholder: 'Quan điểm đề bài đưa ra' },
            { type: 'text', text: '. Although I accept that ' },
            { type: 'topic_input', slotKey: 'intro_concede', placeholder: 'Ý nhượng bộ (mặt hợp lý nhỏ)' },
            { type: 'text', text: `, I strongly ${verb} with the argument that ` },
            { type: 'topic_input', slotKey: 'intro_main_view', placeholder: 'Quan điểm chính em bảo vệ/phản bác' },
            { type: 'text', text: '. This essay will firstly discuss ' },
            { type: 'pillar_slot', slotKey: 'b1_pillar', bodyIndex: 1, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 1 - Nhượng bộ]' },
            { type: 'text', text: ' as a valid point, and then outline ' },
            { type: 'pillar_slot', slotKey: 'b2_pillar', bodyIndex: 2, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 2 - Bảo vệ chính]' },
            { type: 'text', text: ' as the main reason for my overall view.' }
          ]
        },
        {
          sectionTitle: '💡 Body Paragraph 1 (Nhượng bộ — Công nhận 1 khía cạnh)',
          borderColor: '#8b5cf6',
          tokens: [
            { type: 'text', text: 'One of the principal reasons why some people support ' },
            { type: 'topic_input', slotKey: 'b1_concede_np', placeholder: 'Cụm V-ing / Danh từ ý nhượng bộ' },
            { type: 'text', text: ' is ' },
            { type: 'pillar_slot', slotKey: 'b1_pillar', bodyIndex: 1, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 1]' },
            { type: 'text', text: '. This is because of the fact that ' },
            { type: 'pillar_slot', slotKey: 'b1_cause', bodyIndex: 1, pillarCol: 'cause', placeholder: 'Thả [Cause 1]' },
            { type: 'text', text: '. As a result, ' },
            { type: 'pillar_slot', slotKey: 'b1_effect', bodyIndex: 1, pillarCol: 'effect', placeholder: 'Thả [Effect 1]' },
            { type: 'text', text: '. For instance, ' },
            { type: 'pillar_slot', slotKey: 'b1_example', bodyIndex: 1, pillarCol: 'example', placeholder: 'Thả [Example 1]' },
            { type: 'text', text: '.' }
          ]
        },
        {
          sectionTitle: '💡 Body Paragraph 2 (Bảo vệ quan điểm chính của em)',
          borderColor: '#f59e0b',
          tokens: [
            { type: 'text', text: `However, the main reason to support my ${noun} is ` },
            { type: 'pillar_slot', slotKey: 'b2_pillar', bodyIndex: 2, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 2]' },
            { type: 'text', text: '. This is due to the fact that ' },
            { type: 'pillar_slot', slotKey: 'b2_cause', bodyIndex: 2, pillarCol: 'cause', placeholder: 'Thả [Cause 2]' },
            { type: 'text', text: '. Consequently, ' },
            { type: 'pillar_slot', slotKey: 'b2_effect', bodyIndex: 2, pillarCol: 'effect', placeholder: 'Thả [Effect 2]' },
            { type: 'text', text: '. For example, ' },
            { type: 'pillar_slot', slotKey: 'b2_example', bodyIndex: 2, pillarCol: 'example', placeholder: 'Thả [Example 2]' },
            { type: 'text', text: '.' }
          ]
        },
        {
          sectionTitle: '✅ Conclusion',
          borderColor: '#10b981',
          tokens: [
            { type: 'text', text: 'To sum up, although there are some arguments for ' },
            { type: 'topic_input', slotKey: 'conc_concede', placeholder: 'Cụm danh từ ý nhượng bộ' },
            { type: 'text', text: ' mainly because of ' },
            { type: 'topic_input', slotKey: 'conc_p1', placeholder: 'Tóm tắt Trụ ý 1' },
            { type: 'text', text: `, I completely ${verb} that ` },
            { type: 'topic_input', slotKey: 'conc_main', placeholder: 'Nhắc lại quan điểm chính' },
            { type: 'text', text: ' due to ' },
            { type: 'topic_input', slotKey: 'conc_p2', placeholder: 'Tóm tắt Trụ ý 2' },
            { type: 'text', text: '.' }
          ]
        }
      ];
    }
  },

  mixed_ps: {
    id: 'mixed_ps',
    category: 'mixed',
    name: 'Mixed (Trang 1): Problems / Causes & Solutions',
    viSubtitle: 'Body 1 nêu Vấn đề/Nguyên nhân (lắp Pillar 1) → Body 2 nêu 2 Giải pháp + Kết quả kỳ vọng (Pillar 2)',
    body2UsesFullPillar: false,
    buildParagraphs: () => [
      {
        sectionTitle: '📝 Introduction',
        borderColor: '#0ea5e9',
        tokens: [
          { type: 'text', text: 'Over the last few decades, the world has seen that ' },
          { type: 'topic_input', slotKey: 'intro_issue', placeholder: 'Cụm danh từ / V-ing chỉ hiện tượng đề nêu' },
          { type: 'text', text: ' has become a major issue. This essay will firstly discuss ' },
          { type: 'pillar_slot', slotKey: 'b1_pillar', bodyIndex: 1, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý Vấn đề/Nguyên nhân]' },
          { type: 'text', text: ' as the main problem caused by this, and then provide some possible solutions, namely ' },
          { type: 'topic_input', slotKey: 'intro_sol1', placeholder: 'Tóm tắt Giải pháp 1 (V-ing)' },
          { type: 'text', text: ' and ' },
          { type: 'topic_input', slotKey: 'intro_sol2', placeholder: 'Tóm tắt Giải pháp 2 (V-ing)' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '💡 Body Paragraph 1 (Problem / Cause)',
        borderColor: '#8b5cf6',
        tokens: [
          { type: 'text', text: 'The main problem related to ' },
          { type: 'topic_input', slotKey: 'b1_topic', placeholder: 'Cụm danh từ chủ đề' },
          { type: 'text', text: ' is ' },
          { type: 'pillar_slot', slotKey: 'b1_pillar', bodyIndex: 1, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 1]' },
          { type: 'text', text: '. This may be because of the fact that ' },
          { type: 'pillar_slot', slotKey: 'b1_cause', bodyIndex: 1, pillarCol: 'cause', placeholder: 'Thả [Cause 1]' },
          { type: 'text', text: '. As a result, ' },
          { type: 'pillar_slot', slotKey: 'b1_effect', bodyIndex: 1, pillarCol: 'effect', placeholder: 'Thả [Effect 1]' },
          { type: 'text', text: '. For example, ' },
          { type: 'pillar_slot', slotKey: 'b1_example', bodyIndex: 1, pillarCol: 'example', placeholder: 'Thả [Example 1]' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '💡 Body Paragraph 2 (Solutions — Giải pháp & Kết quả kỳ vọng)',
        borderColor: '#f59e0b',
        tokens: [
          { type: 'text', text: 'However, there are ways to tackle such problems. Firstly, one of the most effective solutions is to ' },
          { type: 'topic_input', slotKey: 'b2_sol1', placeholder: 'Giải pháp 1 (V nguyên thể + chi tiết cụ thể)' },
          { type: 'text', text: '. Furthermore, the government and individuals should ' },
          { type: 'topic_input', slotKey: 'b2_sol2', placeholder: 'Giải pháp 2 (V nguyên thể + chi tiết cụ thể)' },
          { type: 'text', text: '. By doing so, ' },
          { type: 'pillar_slot', slotKey: 'b2_effect', bodyIndex: 2, pillarCol: 'effect', placeholder: 'Thả thẻ [Effect tích cực của Trụ ý 2] làm kết quả giải pháp' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '✅ Conclusion',
        borderColor: '#10b981',
        tokens: [
          { type: 'text', text: 'To sum up, it is evident that ' },
          { type: 'topic_input', slotKey: 'conc_topic', placeholder: 'Chủ đề đề bài' },
          { type: 'text', text: ' causes several problems related to ' },
          { type: 'topic_input', slotKey: 'conc_prob', placeholder: 'Nhắc lại Vấn đề chính' },
          { type: 'text', text: ', but measures such as ' },
          { type: 'topic_input', slotKey: 'conc_sols', placeholder: 'Tóm tắt 2 Giải pháp' },
          { type: 'text', text: ' are available to tackle this issue effectively.' }
        ]
      }
    ]
  },

  mixed_ce: {
    id: 'mixed_ce',
    category: 'mixed',
    name: 'Mixed (Trang 3): Causes & Effects',
    viSubtitle: 'Body 1 phân tích Nguyên nhân (Causes) → Body 2 phân tích Hậu quả nghiêm trọng (Effects)',
    body2UsesFullPillar: true,
    buildParagraphs: () => [
      {
        sectionTitle: '📝 Introduction',
        borderColor: '#0ea5e9',
        tokens: [
          { type: 'text', text: 'Over the last few decades, the world has seen that ' },
          { type: 'topic_input', slotKey: 'intro_event', placeholder: 'Sự việc / Xu hướng đề bài nêu (S + V)' },
          { type: 'text', text: '. This essay will firstly discuss the reasons for this, primarily ' },
          { type: 'pillar_slot', slotKey: 'b1_pillar', bodyIndex: 1, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý Nguyên nhân]' },
          { type: 'text', text: ', and then examine the consequences, specifically ' },
          { type: 'pillar_slot', slotKey: 'b2_pillar', bodyIndex: 2, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý Hậu quả]' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '💡 Body Paragraph 1 (Causes — Nguyên nhân)',
        borderColor: '#8b5cf6',
        tokens: [
          { type: 'text', text: 'The main reason for ' },
          { type: 'topic_input', slotKey: 'b1_topic', placeholder: 'Cụm danh từ chỉ hiện tượng' },
          { type: 'text', text: ' is related to ' },
          { type: 'pillar_slot', slotKey: 'b1_pillar', bodyIndex: 1, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 1]' },
          { type: 'text', text: '. This is because of the fact that ' },
          { type: 'pillar_slot', slotKey: 'b1_cause', bodyIndex: 1, pillarCol: 'cause', placeholder: 'Thả [Cause 1]' },
          { type: 'text', text: '. As a result, ' },
          { type: 'pillar_slot', slotKey: 'b1_effect', bodyIndex: 1, pillarCol: 'effect', placeholder: 'Thả [Effect 1]' },
          { type: 'text', text: '. For instance, ' },
          { type: 'pillar_slot', slotKey: 'b1_example', bodyIndex: 1, pillarCol: 'example', placeholder: 'Thả [Example 1]' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '💡 Body Paragraph 2 (Effects — Hậu quả)',
        borderColor: '#f59e0b',
        tokens: [
          { type: 'text', text: 'The effects of this have been and will continue to be very serious. Firstly, it leads to ' },
          { type: 'pillar_slot', slotKey: 'b2_pillar', bodyIndex: 2, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 2]' },
          { type: 'text', text: '. This stems from the fact that ' },
          { type: 'pillar_slot', slotKey: 'b2_cause', bodyIndex: 2, pillarCol: 'cause', placeholder: 'Thả [Cause 2]' },
          { type: 'text', text: '. Consequently, ' },
          { type: 'pillar_slot', slotKey: 'b2_effect', bodyIndex: 2, pillarCol: 'effect', placeholder: 'Thả [Effect 2]' },
          { type: 'text', text: '. For example, ' },
          { type: 'pillar_slot', slotKey: 'b2_example', bodyIndex: 2, pillarCol: 'example', placeholder: 'Thả [Example 2]' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '✅ Conclusion',
        borderColor: '#10b981',
        tokens: [
          { type: 'text', text: 'To sum up, it is evident that factors like ' },
          { type: 'topic_input', slotKey: 'conc_cause', placeholder: 'Tóm tắt Nguyên nhân' },
          { type: 'text', text: ' have led to ' },
          { type: 'topic_input', slotKey: 'conc_topic', placeholder: 'Chủ đề đề bài' },
          { type: 'text', text: ', resulting in a variety of negative effects such as ' },
          { type: 'topic_input', slotKey: 'conc_effect', placeholder: 'Tóm tắt Hậu quả' },
          { type: 'text', text: '.' }
        ]
      }
    ]
  },

  twopart: {
    id: 'twopart',
    category: 'twopart',
    name: 'Two-part Questions (Trả lời 2 câu hỏi trực tiếp)',
    viSubtitle: 'Body 1 trả lời Câu hỏi 1 (Regarding the first question...) → Body 2 trả lời Câu hỏi 2 (With regards to the second question...)',
    body2UsesFullPillar: true,
    buildParagraphs: () => [
      {
        sectionTitle: '📝 Introduction',
        borderColor: '#0ea5e9',
        tokens: [
          { type: 'text', text: 'Over the last few decades, the world has seen that ' },
          { type: 'topic_input', slotKey: 'intro_ctx', placeholder: 'Bối cảnh chung đề bài đưa ra (S + V)' },
          { type: 'text', text: '. This essay will firstly discuss ' },
          { type: 'topic_input', slotKey: 'intro_q1', placeholder: 'Trả lời tóm tắt cho Câu hỏi 1' },
          { type: 'text', text: ' and it will then address the question of ' },
          { type: 'topic_input', slotKey: 'intro_q2', placeholder: 'Trả lời tóm tắt cho Câu hỏi 2' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '💡 Body Paragraph 1 (Answer to Question 1)',
        borderColor: '#8b5cf6',
        tokens: [
          { type: 'text', text: 'Regarding the first question, ' },
          { type: 'topic_input', slotKey: 'b1_lead', placeholder: 'Câu dẫn trả lời Câu 1 (VD: the main purpose of ... is)' },
          { type: 'text', text: ' ' },
          { type: 'pillar_slot', slotKey: 'b1_pillar', bodyIndex: 1, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 1]' },
          { type: 'text', text: '. This is because of the fact that ' },
          { type: 'pillar_slot', slotKey: 'b1_cause', bodyIndex: 1, pillarCol: 'cause', placeholder: 'Thả [Cause 1]' },
          { type: 'text', text: '. As a result, ' },
          { type: 'pillar_slot', slotKey: 'b1_effect', bodyIndex: 1, pillarCol: 'effect', placeholder: 'Thả [Effect 1]' },
          { type: 'text', text: '. For example, ' },
          { type: 'pillar_slot', slotKey: 'b1_example', bodyIndex: 1, pillarCol: 'example', placeholder: 'Thả [Example 1]' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '💡 Body Paragraph 2 (Answer to Question 2)',
        borderColor: '#f59e0b',
        tokens: [
          { type: 'text', text: 'With regards to the second question, ' },
          { type: 'topic_input', slotKey: 'b2_lead', placeholder: 'Câu dẫn trả lời Câu 2 (VD: another vital factor is)' },
          { type: 'text', text: ' ' },
          { type: 'pillar_slot', slotKey: 'b2_pillar', bodyIndex: 2, pillarCol: 'pillar', placeholder: 'Thả [Tên Trụ ý 2]' },
          { type: 'text', text: '. This is due to the fact that ' },
          { type: 'pillar_slot', slotKey: 'b2_cause', bodyIndex: 2, pillarCol: 'cause', placeholder: 'Thả [Cause 2]' },
          { type: 'text', text: '. Consequently, ' },
          { type: 'pillar_slot', slotKey: 'b2_effect', bodyIndex: 2, pillarCol: 'effect', placeholder: 'Thả [Effect 2]' },
          { type: 'text', text: '. For instance, ' },
          { type: 'pillar_slot', slotKey: 'b2_example', bodyIndex: 2, pillarCol: 'example', placeholder: 'Thả [Example 2]' },
          { type: 'text', text: '.' }
        ]
      },
      {
        sectionTitle: '✅ Conclusion',
        borderColor: '#10b981',
        tokens: [
          { type: 'text', text: 'To sum up, ' },
          { type: 'topic_input', slotKey: 'conc_q1', placeholder: 'Tóm tắt câu trả lời cho Câu hỏi 1' },
          { type: 'text', text: ', and ' },
          { type: 'topic_input', slotKey: 'conc_q2', placeholder: 'Tóm tắt câu trả lời cho Câu hỏi 2' },
          { type: 'text', text: '.' }
        ]
      }
    ]
  }
};

export interface ReflexQuestion {
  id: string;
  prompt: string;
  correctCategory: Wt2Category;
  subTypeLabel: string;
  triggerWords: string;
  bestPillars: number[];
  primaryPair: [number, number];
  explanation: string;
}

export const WT2_REFLEX_QUESTIONS: ReflexQuestion[] = [
  {
    id: 'rf_1',
    prompt:
      'Many people think that cheap air travel should be encouraged because it gives ordinary people freedom to travel further. However, others think this leads to environmental problems, so air travel should be more expensive. Discuss both views and give your own opinion.',
    correctCategory: 'discussion',
    subTypeLabel: 'Discussion (Discuss both views)',
    triggerWords: 'Discuss both views and give your own opinion | freedom | environmental problems',
    bestPillars: [1, 2, 13, 4],
    primaryPair: [1, 2],
    explanation:
      'Đề có câu lệnh "Discuss both views..." → Dạng Discussion. Ngay trong đề đã lộ sẵn 2 từ khóa vàng: "freedom" (→ #1 Freedom cho Body 1) và "environmental problems" (→ #2 Pollution hoặc #13 Resource cho Body 2)!'
  },
  {
    id: 'rf_2',
    prompt:
      'Some people say that the government should not put money on building theatres and sports stadiums. Others argue that they should spend more money on medical care and education. Discuss both views and give your opinion.',
    correctCategory: 'discussion',
    subTypeLabel: 'Discussion (Discuss both views)',
    triggerWords: 'Discuss both views | government put money | medical care and education',
    bestPillars: [17, 19, 4, 10, 9],
    primaryPair: [17, 19],
    explanation:
      'Đề hỏi "Discuss both views" → Discussion. Quan điểm 1 (không rót ngân sách xây sân vận động) khớp hoàn hảo với #17 Economic Impact (nhánh gây thâm hụt ngân sách); Quan điểm 2 (chi cho y tế & giáo dục) khớp nguyên văn #19 Equality/Disparity (equal access to education & healthcare)!'
  },
  {
    id: 'rf_3',
    prompt:
      'Some people think that parents should teach children how to be good members of society. Others, however, believe that school is the place to learn this. Discuss both views and give your own opinion.',
    correctCategory: 'discussion',
    subTypeLabel: 'Discussion (Discuss both views)',
    triggerWords: 'Others, however, believe... Discuss both views',
    bestPillars: [14, 16, 9, 12],
    primaryPair: [14, 16],
    explanation:
      'Dạng Discussion: Body 1 (Cha mẹ rèn con tự giác ở nhà) ghép cực mượt #14 Motivation & Independence; Body 2 (Trường học rèn làm việc nhóm, kỹ năng sống) ghép #16 Practical Skills (hoặc #9 Bond).'
  },
  {
    id: 'rf_4',
    prompt:
      'Films and computer games containing violence are popular. Some people say they have negative impacts on society and should be banned, while others say they are just harmless relaxation. Discuss both sides and give your own opinion.',
    correctCategory: 'discussion',
    subTypeLabel: 'Discussion (Discuss both sides)',
    triggerWords: 'Discuss both sides | violence / negative impacts | harmless relaxation',
    bestPillars: [1, 12, 8, 10],
    primaryPair: [1, 12],
    explanation:
      'Dạng Discussion: Ý "harmless relaxation" (không ủng hộ → đẩy lên Body 1) ghép #1 Freedom (tự do giải trí xả stress); Ý "negative impacts & banned" (ủng hộ → Body 2) ghép #12 Crime & Social Order (surge in juvenile delinquency)!'
  },
  {
    id: 'rf_5',
    prompt:
      'Do you agree that the advantages cars bring outweigh the disadvantages?',
    correctCategory: 'argument',
    subTypeLabel: 'Argument (Advantages outweigh Disadvantages)',
    triggerWords: 'advantages ... outweigh the disadvantages',
    bestPillars: [3, 5, 2, 13],
    primaryPair: [3, 2],
    explanation:
      'Có cụm "advantages ... outweigh the disadvantages" → Dạng Argument! Body 1 (Lợi ích xe hơi) ghép #3 Time (tiết kiệm thời gian đi lại) hoặc #5 Convenience; Body 2 (Tác hại) ghép #2 Pollution (excessive burning of fuel).'
  },
  {
    id: 'rf_6',
    prompt:
      'People can live and work anywhere they want to choose because of improved communication technology and transport. Do the advantages of this development outweigh the disadvantages?',
    correctCategory: 'argument',
    subTypeLabel: 'Argument (Outweigh)',
    triggerWords: 'Do the advantages of this development outweigh the disadvantages?',
    bestPillars: [3, 1, 5, 9, 10],
    primaryPair: [3, 9],
    explanation:
      'Dạng Argument: Làm việc từ xa giúp tiết kiệm giờ đi lại (#3 Time / #1 Freedom ở Body 1), nhưng giao tiếp qua màn hình làm giảm tương tác trực tiếp, gây cô lập (#9 Bond & Social Interaction ở Body 2).'
  },
  {
    id: 'rf_7',
    prompt:
      'Food can be produced much more cheaply today because of improved fertilizers and better machinery. However, some of the methods used to do this may be dangerous to human health. What are the advantages and disadvantages?',
    correctCategory: 'argument',
    subTypeLabel: 'Argument (Advantages & Disadvantages)',
    triggerWords: 'What are the advantages and disadvantages? | cheaply | human health',
    bestPillars: [4, 10, 2],
    primaryPair: [4, 10],
    explanation:
      'Đề hỏi thẳng "What are the advantages and disadvantages?" → Argument. Chữ "cheaply" chỉ thẳng tới #4 Cost (Body 1), chữ "dangerous to human health" chỉ thẳng tới #10 Health (Body 2)!'
  },
  {
    id: 'rf_8',
    prompt:
      'The spread of English as a “global language” is an issue nowadays. To what extent do you think the advantages outweigh the disadvantages?',
    correctCategory: 'argument',
    subTypeLabel: 'Argument (Outweigh)',
    triggerWords: 'advantages outweigh the disadvantages | global language',
    bestPillars: [7, 6, 11],
    primaryPair: [7, 11],
    explanation:
      'Cẩn thận bẫy "To what extent" nhưng phía sau là "advantages outweigh the disadvantages" → thuộc dạng Argument! Lợi ích tiếng Anh toàn cầu: mở rộng việc làm & đầu tư (#7 Job); Bất lợi: mai một ngôn ngữ & bản sắc (#11 Culture & Tradition).'
  },
  {
    id: 'rf_9',
    prompt:
      'Too much money has been spent on looking after and repairing old buildings. Therefore, we should knock down old buildings and build modern ones instead. To what extent do you agree or disagree?',
    correctCategory: 'opinion',
    subTypeLabel: 'Opinion Version 1 (100% Disagree)',
    triggerWords: 'To what extent do you agree or disagree? | old buildings',
    bestPillars: [11, 17, 4],
    primaryPair: [11, 17],
    explanation:
      'Câu hỏi "To what extent do you agree or disagree?" (chỉ có 1 ý kiến) → Opinion! Chọn 100% Disagree (Version 1): Giữ công trình cổ giúp bảo tồn di sản (#11 Culture & Tradition) và thu hút du lịch tạo doanh thu thuế (#17 Economic Impact).'
  },
  {
    id: 'rf_10',
    prompt:
      'Overeating is just as harmful as smoking. Thus, the advertising of all food products should be banned in the same way as cigarette advertising. To what extent do you agree or disagree?',
    correctCategory: 'opinion',
    subTypeLabel: 'Opinion Version 2 (Concession — Phản biện chữ "all")',
    triggerWords: 'To what extent do you agree or disagree? | ALL food products should be banned',
    bestPillars: [10, 6, 17, 1],
    primaryPair: [10, 6],
    explanation:
      'Đề Opinion có từ cực đoan "ALL food products" → Dùng Version 2 (Concession): Body 1 nhượng bộ rằng hạn chế quảng cáo đồ ăn nhanh giúp ngừa béo phì (#10 Health), Body 2 phản bác việc cấm TẤT CẢ vì quảng cáo thực phẩm sạch cung cấp thông tin dinh dưỡng (#6 Information & Knowledge).'
  },
  {
    id: 'rf_11',
    prompt:
      'Creative subjects such as arts, music, drama and creative writing are more beneficial to children and therefore they need more of these subjects in the school timetable. To what extent do you agree or disagree?',
    correctCategory: 'opinion',
    subTypeLabel: 'Opinion Version 2 (Concession)',
    triggerWords: 'more beneficial ... To what extent do you agree or disagree?',
    bestPillars: [15, 16, 7],
    primaryPair: [15, 16],
    explanation:
      'Đề Opinion so sánh môn nghệ thuật vs môn cốt lõi: Body 1 nhượng bộ môn nghệ thuật kích thích tư duy sáng tạo (#15 Creativity & Innovation); Body 2 bảo vệ các môn cốt lõi trang bị kỹ năng giải quyết vấn đề thực tế (#16 Practical Skills).'
  },
  {
    id: 'rf_12',
    prompt:
      'Some people argue that the best way to understand another culture is to work in a multinational organization. To what extent do you agree or disagree?',
    correctCategory: 'opinion',
    subTypeLabel: 'Opinion Version 2 (Concession — Phản biện "the best way")',
    triggerWords: 'the best way ... To what extent do you agree or disagree?',
    bestPillars: [9, 11, 6],
    primaryPair: [9, 11],
    explanation:
      'Đề Opinion chứa so sánh nhất "the best way" → Version 2 (Concession): Body 1 nhượng bộ làm công ty đa quốc gia tăng tương tác đồng nghiệp quốc tế (#9 Bond); Body 2 phản biện đi trải nghiệm thực tế mới thấu hiểu sâu văn hóa bản địa (#11 Culture & Tradition).'
  },
  {
    id: 'rf_13',
    prompt:
      'In some countries, the rate of crimes committed by teenagers is increasing. What are the reasons and what can be done to relieve the problem?',
    correctCategory: 'mixed',
    subTypeLabel: 'Mixed Trang 1 (Causes & Solutions)',
    triggerWords: 'What are the reasons and what can be done...',
    bestPillars: [12, 16, 8],
    primaryPair: [12, 16],
    explanation:
      'Đề hỏi "reasons + what can be done" → Mixed (Causes & Solutions)! Body 1 lắp nguyên nhánh tiêu cực của #12 Crime & Social Order (thiếu giáo dục & giám sát → juvenile delinquency); Body 2 đưa giải pháp nhà trường (#16 Practical Skills) + gia đình/pháp luật (#12 tích cực).'
  },
  {
    id: 'rf_14',
    prompt:
      'Nowadays, children spend too much time on technological devices such as smartphones and tablets. What are the problems associated with this, and what solutions can be suggested?',
    correctCategory: 'mixed',
    subTypeLabel: 'Mixed Trang 1 (Problems & Solutions)',
    triggerWords: 'What are the problems ... and what solutions...',
    bestPillars: [10, 9, 14, 16],
    primaryPair: [10, 9],
    explanation:
      'Đề hỏi "problems + solutions" → Mixed (Trang 1)! Trẻ nghiện thiết bị điện tử dẫn tới lối sống tĩnh tại béo phì (#10 Health) và giảm giao tiếp mặt đối mặt gây cô lập (#9 Bond & Social Interaction).'
  },
  {
    id: 'rf_15',
    prompt:
      'Traffic congestion is becoming a major problem in many cities around the world. What are the problems caused by this, and what solutions can be suggested?',
    correctCategory: 'mixed',
    subTypeLabel: 'Mixed Trang 1 (Problems & Solutions)',
    triggerWords: 'Traffic congestion | problems ... and solutions',
    bestPillars: [2, 3, 4, 5],
    primaryPair: [2, 3],
    explanation:
      'Đề kẹt xe dạng Mixed (Problems & Solutions): Vấn đề lớn nhất là khí thải ô nhiễm không khí (#2 Pollution) và lãng phí hàng giờ di chuyển (#3 Time); Giải pháp nâng cấp xe công cộng (#5 Convenience) và thu phí xe cá nhân (#4 Cost).'
  },
  {
    id: 'rf_16',
    prompt:
      'The speeding up of life in many areas such as travel and communication has negative effects on society at all levels—individual, national and global. Evaluate the causes and effects.',
    correctCategory: 'mixed',
    subTypeLabel: 'Mixed Trang 3 (Causes & Effects)',
    triggerWords: 'causes and effects | speeding up of life',
    bestPillars: [3, 5, 10, 2],
    primaryPair: [3, 10],
    explanation:
      'Đề hỏi Nguyên nhân & Hậu quả (không hỏi giải pháp) → Mixed Trang 3 (Causes & Effects)! Nguyên nhân do áp lực tiết kiệm thời gian & tiện lợi tức thời (#3 Time / #5 Convenience); Hậu quả gây stress cá nhân (#10 Health) và ô nhiễm toàn cầu (#2 Pollution).'
  },
  {
    id: 'rf_17',
    prompt:
      'Some people believe they should keep all the money they have earned and should not pay tax to the state. What is the purpose of taxes? Why do some people refuse to pay taxes and explain the effects on society?',
    correctCategory: 'twopart',
    subTypeLabel: 'Two-part Questions',
    triggerWords: '2 câu hỏi riêng biệt: What is the purpose...? Why do some people refuse...?',
    bestPillars: [19, 17, 4],
    primaryPair: [19, 17],
    explanation:
      'Đề đặt 2 câu hỏi cụ thể xoay quanh thuế → Two-part! Câu 1 (Mục đích thuế): cung cấp bình đẳng y tế, giáo dục (#19 Equality); Câu 2 (Tại sao trốn thuế & tác hại): áp lực chi phí (#4 Cost) dẫn tới thâm hụt ngân sách nhà nước (#17 Economic Impact).'
  },
  {
    id: 'rf_18',
    prompt:
      'Many people say that we have developed into a “throw-away” culture, because we are filling up our environment with so many plastic bags and rubbish. To what extent do you agree with this opinion and what measures can you recommend?',
    correctCategory: 'twopart',
    subTypeLabel: 'Two-part Questions (Đề lai Opinion + Measures)',
    triggerWords: 'To what extent do you agree ... AND what measures can you recommend?',
    bestPillars: [13, 2, 4, 6],
    primaryPair: [13, 4],
    explanation:
      'Đề ghép 2 câu hỏi khác loại (Agree/Disagree + Measures) → Dùng khung Two-part ("Regarding the first question... / With regards to the second question...") là gọn nhất! Body 1 lắp #13 Resource (cạn kiệt tài nguyên & rác thải); Body 2 đánh thuế túi nhựa (#4 Cost) + tuyên truyền (#6 Knowledge).'
  },
  {
    id: 'rf_19',
    prompt:
      'With the increase in the use of mobile phones and computers, fewer people are writing letters. Some people think that the traditional skill of writing letters will disappear completely. To what extent do you agree or disagree? How important do you think is letter-writing?',
    correctCategory: 'twopart',
    subTypeLabel: 'Two-part Questions',
    triggerWords: '2 câu hỏi cuối đề: To what extent...? + How important...?',
    bestPillars: [18, 9, 11],
    primaryPair: [18, 9],
    explanation:
      'Có 2 dấu chấm hỏi tách biệt → Two-part! Câu 1 (Có biến mất hoàn toàn không?): Không, vì thư/văn bản giấy giữ tính bảo mật pháp lý (#18 Security & Privacy); Câu 2 (Tầm quan trọng): Thư tay gắn kết tình cảm chân thành (#9 Bond & Social Interaction).'
  },
  {
    id: 'rf_20',
    prompt:
      'Increasing surveillance cameras in public places helps prevent crime, while others worry about privacy. Do the advantages of public CCTV cameras outweigh the disadvantages?',
    correctCategory: 'argument',
    subTypeLabel: 'Argument (Outweigh)',
    triggerWords: 'Do the advantages ... outweigh the disadvantages? | prevent crime | privacy',
    bestPillars: [18, 12, 1],
    primaryPair: [12, 18],
    explanation:
      'Đề hỏi "advantages outweigh disadvantages" → Argument! Body 1 (Lợi ích camera): giảm tội phạm (#12 Crime hoặc #18 Security nhánh +); Body 2 (Bất lợi): xâm phạm đời tư cá nhân (#18 Security & Privacy nhánh -).'
  }
];

export interface Wt2QuestionGuide {
  recommendedCategory: Wt2Category;
  recommendedTemplate: Wt2TemplateId;
  acceptedCategories: Wt2Category[];
  signalHint: string;
  suggestedPillar1: { id: number; polarity: 'positive' | 'negative' };
  suggestedPillar2: { id: number; polarity: 'positive' | 'negative' };
}

export function detectWt2QuestionGuide(topic: string): Wt2QuestionGuide {
  const q = (topic || '').trim();
  const ql = q.toLowerCase();

  let recommendedCategory: Wt2Category = 'opinion';
  let recommendedTemplate: Wt2TemplateId = 'opinion_v2';
  let acceptedCategories: Wt2Category[] = ['opinion'];
  let signalHint =
    'Đề hỏi quan điểm cá nhân ("agree or disagree / what is your opinion") → Khung chuẩn: 3. Opinion (Version 1 hoặc Version 2)';

  if (
    [
      'discuss both',
      'discuss these views',
      'discuss the two views',
      'reason in support of and opposing',
      'which viewpoint do you agree with'
    ].some((p) => ql.includes(p))
  ) {
    recommendedCategory = 'discussion';
    recommendedTemplate = 'discussion';
    acceptedCategories = ql.includes('which viewpoint do you agree with')
      ? ['discussion', 'opinion']
      : ['discussion'];
    signalHint =
      'Đề nêu 2 luồng quan điểm đối lập ("Discuss both views / sides...") → Khung chuẩn: 1. Discussion';
  } else if (
    [
      'advantages and disadvantages',
      'outweigh',
      'problems international travelers cause greater than the advantages',
      'positive or negative',
      'positive effects or negative effects'
    ].some((p) => ql.includes(p))
  ) {
    recommendedCategory = 'argument';
    recommendedTemplate = 'argument';
    acceptedCategories =
      ql.includes('positive or negative') || ql.includes('positive effects or negative effects')
        ? ['argument', 'opinion']
        : ql.includes('what forms do they take')
        ? ['argument', 'twopart']
        : ql.includes('both approaches')
        ? ['argument', 'discussion']
        : ['argument'];
    signalHint =
      'Đề yêu cầu cân nhắc mặt Lợi & Hại ("advantages and disadvantages / outweigh / positive or negative") → Khung chuẩn: 2. Argument';
  } else if (
    [
      'causes and effects',
      'cause and effects',
      'reasons for this and the effects',
      'causes of this problem and what can be done',
      'cause and possible solutions',
      'causes of water shortages',
      'motivated to learn',
      'what do you think the effects this may be',
      'what problems do big cities have',
      'why do you think that is? what are some of the possible problems'
    ].some((p) => ql.includes(p))
  ) {
    const hasSolution = ['solve', 'solution', 'measures', 'can be done', 'motivated'].some((w) =>
      ql.includes(w)
    );
    recommendedCategory = 'mixed';
    recommendedTemplate = hasSolution ? 'mixed_ps' : 'mixed_ce';
    acceptedCategories = ['mixed', 'twopart'];
    signalHint = hasSolution
      ? 'Đề hỏi Nguyên nhân/Vấn đề kèm Giải pháp ("causes/problems + solutions/measures") → Khung chuẩn: 4. Mixed (Problems/Causes & Solutions)'
      : 'Đề hỏi Nguyên nhân & Hệ quả ("causes/reasons + effects/problems") → Khung chuẩn: 4. Mixed (Causes & Effects)';
  } else {
    const qMarks = (q.match(/\?/g) || []).length;
    if (
      qMarks >= 2 ||
      [
        'what criteria should be used',
        'what other measures do you think',
        'do you think this tendency should be changed',
        'what measures can be taken to protect them',
        'what can the arts tell us'
      ].some((p) => ql.includes(p))
    ) {
      recommendedCategory = 'twopart';
      recommendedTemplate = 'twopart';
      acceptedCategories = ['twopart', 'mixed'];
      signalHint =
        'Đề đặt câu hỏi mở trực tiếp / gồm 2 câu hỏi riêng biệt → Khung chuẩn: 5. Two-part';
    } else if (ql.includes('critics say')) {
      acceptedCategories = ['opinion', 'discussion'];
    }
  }

  // Pick 2 highly relevant Pillars based on topic keywords
  const candidateIds: number[] = [];
  const pushUnique = (id: number) => {
    if (!candidateIds.includes(id)) candidateIds.push(id);
  };

  if (/(air travel|petrol|fuel|car|traffic|environment|pollution|global warming|species|consumer goods|disposable|water shortage)/.test(ql)) {
    pushUnique(2); // Pollution
    pushUnique(13); // Resource
    pushUnique(4); // Cost
  }
  if (/(crime|criminal|prison|community service|ban|restrict|dangerous)/.test(ql)) {
    pushUnique(12); // Crime & Social Order
    pushUnique(1); // Freedom
    pushUnique(16); // Practical Skills
  }
  if (/(animal|laboratory|scientific experimenting|zoo)/.test(ql)) {
    pushUnique(8); // Unethical Issues & Morality
    pushUnique(10); // Health
  }
  if (/(online|computer|internet|mobile phone|television|communication technology)/.test(ql)) {
    pushUnique(5); // Convenience
    pushUnique(9); // Bond & Social Interaction
    pushUnique(6); // Information & Knowledge
  }
  if (/(school|university|college|education|student|subject|learn|language|book|librar|museum)/.test(ql)) {
    pushUnique(6); // Information & Knowledge
    pushUnique(16); // Practical Skills
    pushUnique(14); // Motivation & Independence
    pushUnique(1); // Freedom
  }
  if (/(health|medical|medicine|doctor|diet|eat|older|aged 60|elderly)/.test(ql)) {
    pushUnique(10); // Health
    pushUnique(17); // Economic Impact
    pushUnique(9); // Bond & Social Interaction
  }
  if (/(money|tax|fund|billions|financial|salary|paid|wealthy|rich|poor|shopping|advertis)/.test(ql)) {
    pushUnique(4); // Cost
    pushUnique(17); // Economic Impact
    pushUnique(19); // Equality / Disparity
  }
  if (/(job|work|career|employ|graduate)/.test(ql)) {
    pushUnique(7); // Job
    pushUnique(16); // Practical Skills
    pushUnique(9); // Bond & Social Interaction
  }
  if (/(culture|tradition|art|foreign|travel|passport)/.test(ql)) {
    pushUnique(11); // Culture & Tradition
    pushUnique(15); // Creativity & Innovation
    pushUnique(6); // Information & Knowledge
  }
  if (/(family|parent|mother|live alone|friend)/.test(ql)) {
    pushUnique(9); // Bond & Social Interaction
    pushUnique(14); // Motivation & Independence
    pushUnique(4); // Cost
  }

  pushUnique(6);
  pushUnique(4);

  const p1Id = candidateIds[0] || 1;
  const p2Id = candidateIds[1] || 2;

  let pol1: 'positive' | 'negative' = 'positive';
  let pol2: 'positive' | 'negative' = 'positive';
  if (recommendedCategory === 'argument') {
    pol1 = 'positive';
    pol2 = 'negative';
  } else if (recommendedCategory === 'mixed') {
    pol1 = 'negative';
    pol2 = recommendedTemplate === 'mixed_ps' ? 'positive' : 'negative';
  }

  return {
    recommendedCategory,
    recommendedTemplate,
    acceptedCategories,
    signalHint,
    suggestedPillar1: { id: p1Id, polarity: pol1 },
    suggestedPillar2: { id: p2Id, polarity: pol2 }
  };
}
