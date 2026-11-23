import React, { useEffect, useState } from 'react';
import { BookOpen, ChevronLeft, ChevronRight, FileText, Monitor, X, ZoomIn } from 'lucide-react';

export interface CourseShowcaseItem {
  src: string;
  category: 'theory' | 'practice';
  badgeVi?: string;
  badgeEn?: string;
  titleVi: string;
  titleEn: string;
  descVi: string;
  descEn: string;
}

export interface CourseShowcaseConfig {
  headingVi: string;
  headingEn: string;
  subheadingVi: string;
  subheadingEn: string;
  items: CourseShowcaseItem[];
}

const GALLERY_BY_COURSE_ID: Record<number, CourseShowcaseConfig> = {
  // 111: Giao tiếp Căn bản (parent)
  111: {
    headingVi: 'Hình ảnh thực tế hệ thống học tập Giao tiếp Căn bản',
    headingEn: 'Real LMS Previews: Basic Communication Program',
    subheadingVi:
      'Kết hợp trọn bộ Bài giảng Phát âm 44 âm IPA, 90 mẫu câu Luyện phản xạ, Hội thoại tình huống thực tế và Kho 102 đề luyện nghe chấm điểm tự động.',
    subheadingEn:
      'Combining 44 IPA Pronunciation lessons, 90 reflex sentence patterns, real-life dialogues, and 102 auto-graded listening drills.',
    items: [
      {
        src: '/images/course-showcases/pa_01_phonemic_chart.webp',
        category: 'theory',
        badgeVi: '📘 Lý thuyết Phát âm',
        badgeEn: '📘 Pronunciation Theory',
        titleVi: 'Bảng phiên âm quốc tế 44 âm IPA tương tác',
        titleEn: 'Interactive 44-Sound IPA Phonemic Chart',
        descVi: 'Bấm nghe phát âm chuẩn Anh-Anh từng nguyên âm, phụ âm kết hợp sơ đồ khẩu hình trực quan.',
        descEn: 'Click-to-listen British English audio for every vowel and consonant with mouth-position guides.',
      },
      {
        src: '/images/course-showcases/px_01_sentence_pattern.webp',
        category: 'theory',
        badgeVi: '📘 Lý thuyết Phản xạ',
        badgeEn: '📘 Reflex Theory',
        titleVi: 'Hệ thống 90 mẫu câu phản xạ giao tiếp cốt lõi',
        titleEn: '90 Core Communication Sentence Patterns',
        descVi: 'Mỗi mẫu câu đi kèm ví dụ song ngữ, file nghe bản xứ và hướng dẫn lắp ghép nói tự nhiên.',
        descEn: 'Each pattern includes bilingual examples, native audio, and natural speech drills.',
      },
      {
        src: '/images/course-showcases/th_02_birthday_planning.webp',
        category: 'theory',
        badgeVi: '📘 Hội thoại Tình huống',
        badgeEn: '📘 Dialogue Practice',
        titleVi: 'Hội thoại đời sống song ngữ có audio từng lượt thoại',
        titleEn: 'Bilingual Real-Life Dialogues with Turn Audio',
        descVi: 'Luyện nghe-nói qua các tình huống gần gũi hàng ngày kèm tra từ điển tức thì khi click đúp.',
        descEn: 'Practice everyday scenarios with turn-by-turn audio and instant double-click dictionary lookup.',
      },
      {
        src: '/images/course-showcases/px_03_basic_listening_test.webp',
        category: 'practice',
        badgeVi: '📝 Kho đề Luyện nghe',
        badgeEn: '📝 Listening Test Bank',
        titleVi: 'Kho 102 bài test luyện nghe phản xạ (Basic → Advanced)',
        titleEn: '102 Auto-Graded Listening Tests (Basic to Advanced)',
        descVi: 'Trình phát audio mượt mà, chấm điểm ngay sau khi nộp kèm transcript và giải thích chi tiết từng câu.',
        descEn: 'Smooth audio player with instant scoring, full transcript, and per-question explanations.',
      },
    ],
  },

  // 114: Phát âm
  114: {
    headingVi: 'Hình ảnh thực tế khóa học Phát âm chuẩn Anh – Anh',
    headingEn: 'Real LMS Previews: British Pronunciation Course',
    subheadingVi:
      '32 bài giảng trực quan từ Bảng phiên âm 44 âm IPA, Vị trí cấu âm, Nguyên âm – Phụ âm, Cặp âm dễ nhầm lẫn đến Trọng âm và Ngữ điệu câu.',
    subheadingEn:
      '32 visual lessons covering the 44-sound IPA chart, articulation diagrams, minimal pairs, word stress, and intonation.',
    items: [
      {
        src: '/images/course-showcases/pa_01_phonemic_chart.webp',
        category: 'theory',
        badgeVi: '📘 Bài giảng Lý thuyết',
        badgeEn: '📘 Theory Lecture',
        titleVi: 'Bảng phiên âm quốc tế (The Phonemic Chart)',
        titleEn: 'The IPA Phonemic Chart',
        descVi: 'Học chuẩn toàn bộ hệ thống nguyên âm đơn, nguyên âm đôi và phụ âm với âm thanh mẫu chuẩn Anh-Anh.',
        descEn: 'Master every monophthong, diphthong, and consonant with authentic British English audio.',
      },
      {
        src: '/images/course-showcases/pa_02_vowel_monophthongs.webp',
        category: 'theory',
        badgeVi: '📘 Bài giảng Lý thuyết',
        badgeEn: '📘 Theory Lecture',
        titleVi: 'Hướng dẫn khẩu hình Nguyên âm đơn (Vowel Monophthongs)',
        titleEn: 'Vowel Monophthongs & Articulation Guide',
        descVi: 'Minh họa vị trí lưỡi, độ mở hàm và độ dài âm giúp học viên sửa triệt để lỗi phát âm kiểu Việt.',
        descEn: 'Visual tongue-position and jaw-opening guides to fix common pronunciation habits.',
      },
      {
        src: '/images/course-showcases/pa_03_minimal_pair_drill.webp',
        category: 'practice',
        badgeVi: '🎧 Thực hành Phân biệt âm',
        badgeEn: '🎧 Minimal-Pair Drill',
        titleVi: 'Luyện cặp âm tối thiểu — Unit 1: /ɪ/ vs /iː/',
        titleEn: 'Minimal-Pair Practice — Unit 1: /ɪ/ vs /iː/',
        descVi: 'So sánh trực tiếp các cặp từ dễ nhầm lẫn kèm audio bản xứ và bài luyện đọc câu ứng dụng.',
        descEn: 'Direct contrast of confusing sound pairs with native audio and sentence drills.',
      },
      {
        src: '/images/course-showcases/pa_04_word_stress.webp',
        category: 'practice',
        badgeVi: '🎧 Giai điệu & Trọng âm',
        badgeEn: '🎧 Stress & Rhythm',
        titleVi: 'Trọng âm từ & Ngữ điệu tự nhiên (Word Stress)',
        titleEn: 'Word Stress & Natural Rhythm',
        descVi: 'Hệ thống quy tắc đánh trọng âm, âm cuối (ending sounds) và nối âm để nói tiếng Anh có nhạc điệu.',
        descEn: 'Systematic stress rules, ending sounds, and connected speech for natural fluency.',
      },
    ],
  },

  // 115: Luyện phản xạ
  115: {
    headingVi: 'Hình ảnh thực tế Bài giảng & Kho bài tập Luyện phản xạ',
    headingEn: 'Real LMS Previews: Speaking Reflex Lectures & Tests',
    subheadingVi:
      'Xây dựng phản xạ nói nhanh không cần dịch ngầm với 90 cấu trúc câu thông dụng nhất, bài luyện phản xạ theo cụm và 102 đề luyện nghe từ cơ bản đến nâng cao.',
    subheadingEn:
      'Build instant speaking reflexes with 90 essential sentence patterns, timed recall drills, and 102 graded listening tests.',
    items: [
      {
        src: '/images/course-showcases/px_01_sentence_pattern.webp',
        category: 'theory',
        badgeVi: '📘 Bài giảng Lý thuyết',
        badgeEn: '📘 Theory Lecture',
        titleVi: 'Bài giảng mẫu câu cốt lõi — 90 cấu trúc phản xạ',
        titleEn: 'Core Sentence Patterns — 90 Reflex Structures',
        descVi: 'Trình bày mạch lạc cấu trúc, ngữ cảnh dùng tự nhiên, câu ví dụ song ngữ và file nghe chuẩn.',
        descEn: 'Clear structure breakdown, natural usage contexts, bilingual examples, and native audio.',
      },
      {
        src: '/images/course-showcases/px_02_practice_30_sentences.webp',
        category: 'practice',
        badgeVi: '🎧 Luyện Phản xạ',
        badgeEn: '🎧 Reflex Drill',
        titleVi: 'Bài tổng ôn phản xạ 30 – 90 câu nói liên hoàn',
        titleEn: '30-to-90 Sentence Rapid Reflex Review',
        descVi: 'Rèn tốc độ bật câu Việt → Anh dưới áp lực thời gian theo phương pháp ghi nhớ 3 bước.',
        descEn: 'Train rapid Vietnamese-to-English recall using our 3-step retention method.',
      },
      {
        src: '/images/course-showcases/px_03_basic_listening_test.webp',
        category: 'practice',
        badgeVi: '📝 Kho đề Cơ bản',
        badgeEn: '📝 Basic Test Bank',
        titleVi: 'Kho đề Basic Listening Test — Chấm điểm & Giải thích',
        titleEn: 'Basic Listening Test Bank — Auto-Graded',
        descVi: 'Luyện tai nghe phản xạ ngay trên trình duyệt với thanh phát audio và bảng điều hướng câu hỏi.',
        descEn: 'Practice listening reflexes in-browser with integrated audio controls and question palette.',
      },
      {
        src: '/images/course-showcases/px_04_intermediate_listening_test.webp',
        category: 'practice',
        badgeVi: '📝 Kho đề Trung cấp',
        badgeEn: '📝 Intermediate Test Bank',
        titleVi: 'Kho đề Intermediate Listening Test — Nâng tốc độ nghe hiểu',
        titleEn: 'Intermediate Listening Tests — Speed & Comprehension',
        descVi: 'Tăng dần tốc độ nói tự nhiên kèm transcript bôi đậm người nói và lời giải chi tiết sau khi nộp.',
        descEn: 'Progressive native speech speed with speaker-formatted transcripts and explanations.',
      },
    ],
  },

  // 116: Tình huống Giao tiếp
  116: {
    headingVi: 'Hình ảnh thực tế Bài giảng Tình huống Giao tiếp & Kho đề Nghe',
    headingEn: 'Real LMS Previews: Real-Life Dialogues & Listening Bank',
    subheadingVi:
      'Làm chủ 12 chiến thuật giao tiếp tự nhiên cùng hàng loạt hội thoại đời sống thực tế (đặt bàn, gọi điện, tiệc tùng, du lịch…) và đề nghe ứng dụng.',
    subheadingEn:
      'Master 12 conversation strategies alongside real-life dialogues (phone calls, dining, travel, social events) and applied listening tests.',
    items: [
      {
        src: '/images/course-showcases/th_01_communication_strategy.webp',
        category: 'theory',
        badgeVi: '📘 Lý thuyết Chiến thuật',
        badgeEn: '📘 Strategy Lecture',
        titleVi: 'Chiến thuật chào hỏi, bắt chuyện & duy trì hội thoại',
        titleEn: 'Greeting, Small Talk & Conversation Strategies',
        descVi: 'Hệ thống 12 chuyên đề chiến thuật giúp mở đầu tự nhiên và kéo dài câu chuyện với người bản xứ.',
        descEn: '12 structured communication tactics to open and sustain natural conversations.',
      },
      {
        src: '/images/course-showcases/th_02_birthday_planning.webp',
        category: 'theory',
        badgeVi: '📘 Hội thoại Thực tế',
        badgeEn: '📘 Real-Life Dialogue',
        titleVi: 'Tình huống đời sống — Birthday Party Planning',
        titleEn: 'Everyday Scenario — Birthday Party Planning',
        descVi: 'Hội thoại song ngữ phân vai rõ ràng, hỗ trợ phát audio từng câu và giải thích cụm từ bản xứ.',
        descEn: 'Role-based bilingual dialogues with line-by-line audio and idiomatic notes.',
      },
      {
        src: '/images/course-showcases/th_03_on_the_phone.webp',
        category: 'theory',
        badgeVi: '📘 Hội thoại Ứng dụng',
        badgeEn: '📘 Applied Scenario',
        titleVi: 'Tình huống gọi điện & hẹn lịch — On the Phone',
        titleEn: 'Phone Calls & Scheduling — On the Phone',
        descVi: 'Luyện phản xạ trao đổi qua điện thoại, đề xuất kế hoạch và xử lý tình huống giao tiếp thực tế.',
        descEn: 'Practice phone etiquette, proposals, and spontaneous real-world responses.',
      },
      {
        src: '/images/course-showcases/th_04_advanced_listening_test.webp',
        category: 'practice',
        badgeVi: '📝 Kho đề Thực chiến',
        badgeEn: '📝 Listening Test Bank',
        titleVi: 'Kho đề Advanced Listening — Thử thách hội thoại tốc độ thật',
        titleEn: 'Advanced Listening Tests — Natural-Speed Dialogues',
        descVi: 'Kiểm tra khả năng nghe hiểu hội thoại đời thực với chấm điểm tự động và AI Tutor giải thích.',
        descEn: 'Test real-world listening comprehension with instant grading and AI Tutor support.',
      },
    ],
  },

  // 129: Giao tiếp Nâng cao (parent — showcases all 4 child courses: Văn phòng, Thành ngữ, Email, Phỏng vấn)
  129: {
    headingVi: 'Hình ảnh thực tế hệ thống học tập Giao tiếp Nâng cao & Công sở (4 Học phần)',
    headingEn: 'Real LMS Previews: Advanced & Business English (4 Modules)',
    subheadingVi:
      'Trọn bộ 4 học phần Giao tiếp Nâng cao trên nền tảng LMS: Tiếng Anh Văn phòng (52 bài), 150 Thành ngữ thông dụng (15 bài), Học viết Email (60 mẫu Email), và Luyện Phỏng vấn Xin việc (24 tình huống STAR + Mock Interview AI).',
    subheadingEn:
      'Four complete Advanced Communication tracks on our LMS: Office English (52 lessons), 150 Idioms & Phrases, Business Email Writing (60 models), and Job Interview English (24 STAR lessons + AI Mock Interviews).',
    items: [
      {
        src: '/images/course-showcases/vp_01_office_intro.webp',
        category: 'theory',
        badgeVi: '📘 Tiếng Anh Văn phòng',
        badgeEn: '📘 Office English',
        titleVi: '13 Chuyên đề Tiếng Anh Văn phòng — Business Collocations',
        titleEn: '13 Corporate Modules — Business Collocations',
        descVi: 'Hệ thống hóa cụm từ kết hợp chuyên nghiệp trong doanh nghiệp kèm audio chuẩn, đối chiếu song ngữ và Learn by Heart.',
        descEn: 'Structured corporate collocations with native audio, bilingual views, and active recall.',
      },
      {
        src: '/images/course-showcases/id_01_cards.webp',
        category: 'theory',
        badgeVi: '📘 Thành ngữ Thông dụng',
        badgeEn: '📘 Idioms & Phrases',
        titleVi: '150 Thành ngữ bản xứ kèm Audio Anh – Anh & IELTS Band 8+',
        titleEn: '150 Native Idioms with British Audio & IELTS Band 8+',
        descVi: '15 chủ đề thành ngữ thực chiến phân chia 3 trang tương tác: Thẻ nghĩa & Audio, Hội thoại ứng dụng và Active Recall.',
        descEn: '15 themed idiom lessons across 3 interactive tabs: Audio Cards, Real Dialogues, and Active Recall.',
      },
      {
        src: '/images/course-showcases/em_04_writing_ai.webp',
        category: 'practice',
        badgeVi: '✍️ Thực hành Viết Email AI',
        badgeEn: '✍️ AI Email Writing Lab',
        titleVi: '60 Mẫu Email Thương mại & Phòng luyện viết Email chấm AI',
        titleEn: '60 Business Email Models & AI-Graded Writing Practice',
        descVi: 'Rèn văn phong chuẩn quốc tế qua 5 cấp độ từ cơ bản đến đàm phán, kèm thực hành viết trực tiếp có AI góp ý chi tiết.',
        descEn: 'Master international email etiquette across 5 levels with hands-on split-screen AI writing feedback.',
      },
      {
        src: '/images/course-showcases/iv_01_star_models.webp',
        category: 'theory',
        badgeVi: '🎤 Luyện Phỏng vấn STAR',
        badgeEn: '🎤 STAR Interview Mastery',
        titleVi: '24 Tình huống Phỏng vấn Xin việc (Fresher & Senior + Mock AI)',
        titleEn: '24 Job Interview Scenarios (Fresher & Senior + AI Mock)',
        descVi: 'Phân tích ý đồ nhà tuyển dụng, bài mẫu 2 cấp độ kèm Audio, né bẫy Red Flag và luyện Phỏng vấn Thử chấm chữa AI.',
        descEn: 'Recruiter-intent insights, Fresher & Senior audio models, Red-Flag traps, and AI Mock Interviews.',
      },
    ],
  },

  // 128: Thành ngữ thông dụng
  128: {
    headingVi: 'Hình ảnh thực tế Bài giảng & Kho đề Thành ngữ Thông dụng (150 Idioms)',
    headingEn: 'Real LMS Previews: 150 Essential Idioms & Phrases',
    subheadingVi:
      '15 chủ đề tinh tuyển gồm 150 thành ngữ thông dụng nhất trong công sở, đời sống và IELTS Speaking Band 8.0+ — tích hợp Audio Anh – Anh, hội thoại mẫu, luyện nhớ Active Recall và 150 câu trắc nghiệm.',
    subheadingEn:
      '15 curated themes covering 150 essential workplace, daily & IELTS Band 8.0+ idioms — with British English audio, natural dialogues, Active Recall drills, and 150 MCQ questions.',
    items: [
      {
        src: '/images/course-showcases/id_01_cards.webp',
        category: 'theory',
        badgeVi: '📘 10 Thành ngữ & Audio',
        badgeEn: '📘 Idiom Cards & Audio',
        titleVi: 'Trang 1: Thẻ 10 Thành ngữ kèm Audio Anh – Anh & Sắc thái dùng',
        titleEn: 'Page 1: 10 Idiom Cards with British Audio & Register Tags',
        descVi: 'Trình phát audio chỉnh tốc độ 0.8x/1.0x/1.2x kèm giải nghĩa tiếng Anh – Việt, ví dụ thực tế và ghi chú bối cảnh chuẩn xác.',
        descEn: 'Speed-controlled native audio player with clear definitions, authentic examples, and usage notes.',
      },
      {
        src: '/images/course-showcases/id_02_dialogue_ielts.webp',
        category: 'theory',
        badgeVi: '💬 Hội thoại & IELTS 8+',
        badgeEn: '💬 Dialogue & IELTS 8+',
        titleVi: 'Trang 2: Hội thoại bản xứ Song ngữ & Bài mẫu IELTS Speaking',
        titleEn: 'Page 2: Bilingual Workplace Dialogue & IELTS Band 8+ Model',
        descVi: 'Hiểu ngay cách lồng ghép tự nhiên nhiều thành ngữ trong cùng một cuộc trò chuyện và bài nói IELTS đạt điểm Lexical Resource cao.',
        descEn: 'See idioms woven naturally into real conversations and high-scoring IELTS Speaking answers.',
      },
      {
        src: '/images/course-showcases/id_03_active_recall.webp',
        category: 'practice',
        badgeVi: '🧠 Active Recall',
        badgeEn: '🧠 Active Recall Drill',
        titleVi: 'Trang 3: Phản xạ Active Recall — Tự bật thành ngữ từ gợi ý Việt',
        titleEn: 'Page 3: Active Recall — Instant Vietnamese-to-Idiom Recall',
        descVi: 'Chế độ ẩn/hiện đáp án màu cam tương tác giúp học viên tự kiểm tra trí nhớ và biến thành ngữ thành phản xạ nói thật.',
        descEn: 'Interactive hide/reveal orange cues turn passive recognition into active speaking fluency.',
      },
      {
        src: '/images/course-showcases/id_04_mcq_test.webp',
        category: 'practice',
        badgeVi: '📝 Kho đề 150 câu MCQ',
        badgeEn: '📝 150-Question Test Bank',
        titleVi: 'Kho 15 đề Trắc nghiệm ứng dụng ngữ cảnh chấm điểm tức thì',
        titleEn: '15 Contextual MCQ Tests with Instant Explanations',
        descVi: 'Mỗi chủ đề đi kèm đề test 10 câu hỏi tình huống thực tế, chấm điểm tự động và giải thích chi tiết từng đáp án.',
        descEn: 'Each theme pairs with a 10-question contextual test featuring auto-grading and Vietnamese explanations.',
      },
    ],
  },

  // 124: Học viết Email
  124: {
    headingVi: 'Hình ảnh thực tế Bài giảng & Thực hành Viết Email Chuyên nghiệp',
    headingEn: 'Real LMS Previews: Business Email Writing (5 Levels · 60 Models)',
    subheadingVi:
      '20 bài giảng chia làm 5 cấp độ gồm 60 mẫu Email thương mại chuẩn quốc tế kèm Audio Anh – Anh, bảng sửa lỗi Vietlish → Pro, biểu mẫu Copy-Ready, 100 câu trắc nghiệm và 15 đề thực hành viết Email chấm AI.',
    subheadingEn:
      '20 lessons across 5 levels featuring 60 workplace email models with British audio, Vietlish-to-Pro upgrades, copy-ready templates, 100 MCQs, and 15 AI-graded email writing tasks.',
    items: [
      {
        src: '/images/course-showcases/em_01_models.webp',
        category: 'theory',
        badgeVi: '✉️ 60 Mẫu Email chuẩn',
        badgeEn: '✉️ 60 Email Models',
        titleVi: 'Trang 1: Cụm từ đắt giá & 3 Mẫu Email thực tế kèm Audio đọc mẫu',
        titleEn: 'Page 1: Power Email Phrases & 3 Realistic Models with Audio',
        descVi: 'Nắm trọn Subject Line sắc nét, sắc thái trang trọng (Register & Tone) và cấu trúc email súc tích cho từng tình huống công sở.',
        descEn: 'Master sharp subject lines, tone calibration, and crisp international email structure.',
      },
      {
        src: '/images/course-showcases/em_02_upgrades_bilingual.webp',
        category: 'theory',
        badgeVi: '🔄 Sửa lỗi & Song ngữ',
        badgeEn: '🔄 Upgrades & Bilingual',
        titleVi: 'Trang 2: Nâng cấp câu Vietlish thô → Chuẩn quốc tế & Đối chiếu Song ngữ',
        titleEn: 'Page 2: Awkward vs Professional Upgrades & Bilingual Parallel',
        descVi: 'Chỉ rõ vì sao cách diễn đạt dịch từng chữ dễ gây hiểu lầm, đồng thời đối chiếu song ngữ 2 cột đầy đủ cả 3 bức email.',
        descEn: 'Side-by-side comparison fixing blunt phrasing plus full English-Vietnamese bilingual columns.',
      },
      {
        src: '/images/course-showcases/em_03_template_recall.webp',
        category: 'practice',
        badgeVi: '📋 Biểu mẫu & Recall',
        badgeEn: '📋 Templates & Recall',
        titleVi: 'Trang 3: Khung Email Copy-Ready & Luyện phản xạ Active Recall',
        titleEn: 'Page 3: Copy-Ready Email Templates & Active Recall',
        descVi: 'Kho khung mẫu tham chiếu nhanh dùng ngay trong công việc kết hợp bài tự kiểm tra viết lại câu chuyên nghiệp.',
        descEn: 'Quick-reference templates ready for daily work paired with interactive phrasing recall drills.',
      },
      {
        src: '/images/course-showcases/em_04_writing_ai.webp',
        category: 'practice',
        badgeVi: '🤖 Viết Email AI Chấm',
        badgeEn: '🤖 AI Email Writing Lab',
        titleVi: 'Phòng thực hành chia đôi màn hình — Viết Email & AI chấm chữa 24/7',
        titleEn: 'Split-Screen Writing Lab — Draft Emails with 24/7 AI Coaching',
        descVi: 'Đề bài tình huống doanh nghiệp bên trái, khung soạn thảo bên phải — nộp bài xong nhận bài mẫu chuẩn và AI góp ý chi tiết.',
        descEn: 'Realistic business briefs on the left, drafting editor on the right, with model answers and AI feedback.',
      },
    ],
  },

  // 142: Luyện Phỏng vấn Xin việc
  142: {
    headingVi: 'Hình ảnh thực tế khóa học Luyện Phỏng vấn Xin việc (Job Interview English)',
    headingEn: 'Real LMS Previews: Job Interview English (24 STAR Lessons)',
    subheadingVi:
      '24 tình huống phỏng vấn cốt lõi chia làm 6 chuyên đề với bài mẫu song song 2 cấp độ (Fresher & Senior), Audio bản xứ Anh – Anh, nhận diện bẫy Red Flag, 60 câu trắc nghiệm và 24 đề Mock Interview chấm AI.',
    subheadingEn:
      '24 core interview scenarios across 6 modules with parallel Fresher & Senior British-audio models, Red-Flag trap guides, 60 strategy MCQs, and 24 AI-coached Mock Interviews.',
    items: [
      {
        src: '/images/course-showcases/iv_01_star_models.webp',
        category: 'theory',
        badgeVi: '🎤 Chiến lược & Bài mẫu',
        badgeEn: '🎤 STAR Strategy & Models',
        titleVi: 'Trang 1: Ý đồ Nhà tuyển dụng, Công thức STAR & 2 Bài Mẫu Fresher/Senior',
        titleEn: 'Page 1: Recruiter Intent, STAR Formula & Fresher/Senior Models',
        descVi: 'Phân tích góc nhìn thật của Hiring Manager kèm Audio Anh – Anh và 2 phiên bản trả lời riêng cho sinh viên mới ra trường & quản lý.',
        descEn: 'Decode recruiter intent with native British audio and tailored Fresher & Senior answers.',
      },
      {
        src: '/images/course-showcases/iv_02_traps_bilingual.webp',
        category: 'theory',
        badgeVi: '🚨 Né Bẫy & Song ngữ',
        badgeEn: '🚨 Traps & Bilingual',
        titleVi: 'Trang 2: 3 Bẫy Trả lời Mất điểm (Red Flags) & Đối chiếu Song ngữ 2 cột',
        titleEn: 'Page 2: 3 Red-Flag Traps vs Winning Reframes & Bilingual View',
        descVi: 'Giúp ứng viên tránh tuyệt đối các câu trả lời sáo rỗng, đổ lỗi hay tự hạ giá trị, kèm bản dịch đối chiếu từng ý chi tiết.',
        descEn: 'Eliminate cliché or risky answers with concrete reframes and side-by-side bilingual scripts.',
      },
      {
        src: '/images/course-showcases/iv_03_mcq_strategy.webp',
        category: 'practice',
        badgeVi: '📝 Trắc nghiệm Chiến lược',
        badgeEn: '📝 Strategy MCQ Bank',
        titleVi: 'Kho 60 câu Trắc nghiệm Phản xạ Né Bẫy & Chọn Câu Trả Lời Ghi Điểm',
        titleEn: '60-Question Interview Strategy & Trap-Avoidance Tests',
        descVi: 'Luyện tư duy chọn phản hồi khéo léo nhất trước các câu hỏi hóc búa về điểm yếu, xung đột, khoảng trống CV và mức lương.',
        descEn: 'Sharpen judgment across tricky questions on weaknesses, conflict, CV gaps, and salary.',
      },
      {
        src: '/images/course-showcases/iv_04_mock_interview_ai.webp',
        category: 'practice',
        badgeVi: '🤖 Mock Interview AI',
        badgeEn: '🤖 AI Mock Interview',
        titleVi: 'Phòng Phỏng vấn Thử Thực chiến (24 câu hỏi) — AI đóng vai Hiring Manager',
        titleEn: '24-Prompt Mock Interview Simulator — AI Hiring Manager Feedback',
        descVi: 'Thực hành trả lời trực tiếp theo khung STAR với đề bài và gợi ý ở khung trái, nộp bài nhận nhận xét chuyên sâu ngay lập tức.',
        descEn: 'Practice full STAR responses in a split-screen simulator with instant structured coaching.',
      },
    ],
  },

  // 123: Tiếng Anh văn phòng
  123: {
    headingVi: 'Hình ảnh thực tế Bài giảng & Thực hành Tiếng Anh Văn phòng',
    headingEn: 'Real LMS Previews: Business & Office English',
    subheadingVi:
      '52 bài học thuộc 13 chủ đề doanh nghiệp cốt lõi — mỗi chủ đề gồm 4 phần bài bản: Introduction (Từ vựng & Collocations), Conversation (Hội thoại), Short Talk 1 & Short Talk 2.',
    subheadingEn:
      '52 lessons across 13 core corporate topics — each structured into Introduction, Workplace Conversation, Short Talk 1, and Short Talk 2.',
    items: [
      {
        src: '/images/course-showcases/vp_01_office_intro.webp',
        category: 'theory',
        badgeVi: '📘 Bài giảng Từ vựng',
        badgeEn: '📘 Vocabulary Lecture',
        titleVi: '1.1 Introduction — Từ vựng & Cụm từ công sở (Offices)',
        titleEn: '1.1 Introduction — Office Vocabulary & Collocations',
        descVi: 'Trình bày sắc nét bộ cụm từ công sở thông dụng kèm ngữ cảnh sử dụng thực tế trong doanh nghiệp.',
        descEn: 'High-frequency workplace collocations presented in practical corporate contexts.',
      },
      {
        src: '/images/course-showcases/vp_02_office_conversation.webp',
        category: 'practice',
        badgeVi: '🎧 Hội thoại Thực chiến',
        badgeEn: '🎧 Dialogue Drill',
        titleVi: '1.2 Conversation — Hội thoại văn phòng thực tế',
        titleEn: '1.2 Conversation — Real Workplace Dialogues',
        descVi: 'Nghe hội thoại chuẩn thương mại, luyện nhập vai giao tiếp đồng nghiệp & đối tác quốc tế.',
        descEn: 'Listen to realistic workplace dialogues and practice professional responses.',
      },
      {
        src: '/images/course-showcases/vp_03_finance_budgeting.webp',
        category: 'theory',
        badgeVi: '📘 Đối chiếu Song ngữ',
        badgeEn: '📘 Bilingual Parallel',
        titleVi: '9.1 Finance & Budgeting — Đọc đối chiếu Song ngữ 2 cột',
        titleEn: '9.1 Finance & Budgeting — Side-by-Side Bilingual Reading',
        descVi: 'Trang bị vốn từ chuyên môn sâu cho Tài chính, Kế toán, Nhân sự, Sản xuất kèm đối chiếu Anh–Việt trực quan.',
        descEn: 'Specialized vocabulary for Finance, Accounting, HR & Manufacturing with parallel translations.',
      },
      {
        src: '/images/course-showcases/vp_04_short_talk_practice.webp',
        category: 'practice',
        badgeVi: '🎧 Learn by Heart',
        badgeEn: '🎧 Active Recall',
        titleVi: '1.3 Short Talk 1 — Luyện trí nhớ Active Recall (Learn by Heart)',
        titleEn: '1.3 Short Talk 1 — Active Recall (Learn by Heart)',
        descVi: 'Tự dịch ngược cụm từ màu cam từ tiếng Việt sang Business Collocations chuẩn ngay sau khi nghe bài nói ngắn.',
        descEn: 'Convert orange Vietnamese prompts into authentic business collocations after listening.',
      },
    ],
  },

  // 127: Luyện thi IELTS cấp tốc
  127: {
    headingVi: 'Hình ảnh thực tế Bài giảng Chiến thuật & Phòng thi IELTS chuẩn IDP/BC',
    headingEn: 'Real LMS Previews: IELTS Strategy Lectures & IDP/BC Exam Lab',
    subheadingVi:
      '79 bài giảng chiến thuật chuyên sâu 4 kỹ năng kết hợp kho 621 đề thi Cambridge IELTS 1–20 giả lập 100% phòng thi máy tính IDP/BC và AI chấm chữa Writing/Speaking.',
    subheadingEn:
      '79 four-skill strategy lectures paired with 621 Cambridge IELTS 1–20 tests on a realistic IDP/BC computer-based exam simulator and AI grader.',
    items: [
      {
        src: '/images/course-showcases/ielts_01_lecture_reading.webp',
        category: 'theory',
        badgeVi: '📘 Lý thuyết Reading',
        badgeEn: '📘 Reading Theory',
        titleVi: 'Bài giảng Chiến thuật Reading — Keyword Table & Đọc 3 Bước',
        titleEn: 'IELTS Reading Strategy — Keyword Table & 3-Step Method',
        descVi: 'Phân tích bản chất từng dạng bài, bẫy paraphrase và phương pháp tối ưu tốc độ đạt Band 7.5–8.5+.',
        descEn: 'Breakdown of question types, paraphrase traps, and speed techniques for Band 7.5–8.5+.',
      },
      {
        src: '/images/course-showcases/ielts_02_lecture_writing.webp',
        category: 'theory',
        badgeVi: '📘 Lý thuyết Writing',
        badgeEn: '📘 Writing Theory',
        titleVi: 'Bài giảng Writing Task 1 & Task 2 — Tư duy lập luận Band 8.0',
        titleEn: 'IELTS Writing Task 1 & Task 2 — Band 8.0 Frameworks',
        descVi: 'Hướng dẫn chọn lọc số liệu, lập dàn ý logic mạch lạc kèm bài mẫu phân tích từ vựng ăn điểm.',
        descEn: 'Data selection, coherent essay planning, and annotated Band 8.0 model essays.',
      },
      {
        src: '/images/course-showcases/ielts_03_test_reading_idp.webp',
        category: 'practice',
        badgeVi: '📝 Phòng thi IDP/BC',
        badgeEn: '📝 IDP/BC Exam Lab',
        titleVi: 'Phòng thi máy tính IELTS Cambridge Reading (chuẩn 100% IDP/BC)',
        titleEn: 'Computer-Based IELTS Reading Simulator (IDP/BC Format)',
        descVi: 'Chia đôi màn hình bài đọc – câu hỏi, hỗ trợ bôi vàng highlight text, đồng hồ đếm ngược và tự chấm.',
        descEn: 'Split-screen passage and questions with text highlighting, countdown timer, and auto-scoring.',
      },
      {
        src: '/images/course-showcases/ielts_04_test_writing_ai.webp',
        category: 'practice',
        badgeVi: '📝 Phòng luyện Writing AI',
        badgeEn: '📝 AI Writing Lab',
        titleVi: 'Phòng luyện IELTS Writing Cambridge — Đếm từ & AI Chấm Band',
        titleEn: 'IELTS Writing Lab — Word Counter & AI Band Grader',
        descVi: 'Soạn bài trực tiếp theo đề Cambridge thật, tự động đếm từ và nhận chấm chữa chi tiết 4 tiêu chí.',
        descEn: 'Write directly on authentic Cambridge prompts with live word count and 4-criteria AI feedback.',
      },
    ],
  },

  // 132: Luyện thi IGCSE / A-Level cấp tốc
  132: {
    headingVi: 'Hình ảnh thực tế Bài giảng Song ngữ & Kho đề Cambridge IGCSE',
    headingEn: 'Real LMS Previews: Bilingual IGCSE Lectures & Past Papers Lab',
    subheadingVi:
      'Hơn 200 bài giảng song ngữ Anh–Việt tích hợp audio giảng bài, video & mô phỏng cùng kho 990+ đề Past Papers (Paper 2 MCQ, Paper 4/6 Tự luận, Case Study) chấm AI sát Marking Scheme.',
    subheadingEn:
      '200+ bilingual English–Vietnamese lectures with audio walkthroughs and 990+ Past Papers (Paper 2 MCQ, Paper 4/6 Structured, Case Studies) graded against Cambridge Marking Schemes.',
    items: [
      {
        src: '/images/course-showcases/igcse_01_lecture_econ.webp',
        category: 'theory',
        badgeVi: '📘 Bài giảng Song ngữ',
        badgeEn: '📘 Bilingual Lecture',
        titleVi: 'Bài giảng IGCSE Economics 0455 — Song ngữ & Audio giảng bài',
        titleEn: 'IGCSE Economics 0455 — Bilingual Notes & Audio Walkthrough',
        descVi: 'Chuyển đổi linh hoạt Bản Tiếng Anh / Bản Song ngữ Anh-Việt kèm đồ thị trực quan và audio phân tích.',
        descEn: 'Switch seamlessly between English and Bilingual tabs with interactive diagrams and audio.',
      },
      {
        src: '/images/course-showcases/igcse_02_lecture_physics.webp',
        category: 'theory',
        badgeVi: '📘 Bài giảng Khoa học',
        badgeEn: '📘 Science Lecture',
        titleVi: 'Bài giảng IGCSE Physics 0625 — Chuẩn Syllabus Cambridge',
        titleEn: 'IGCSE Physics 0625 — Cambridge Syllabus Lectures',
        descVi: 'Hệ thống đầy đủ các môn Sciences (0654/0610/0620/0625), Maths, Economics, Business, Geography, ESL.',
        descEn: 'Full coverage of Sciences (0654/0610/0620/0625), Maths, Economics, Business, Geography & ESL.',
      },
      {
        src: '/images/course-showcases/igcse_03_test_mcq_physics.webp',
        category: 'practice',
        badgeVi: '📝 Kho đề Paper 2 MCQ',
        badgeEn: '📝 Paper 2 MCQ Bank',
        titleVi: 'Kho đề Topical Paper 2 (Physics / Chemistry / Biology / Econ)',
        titleEn: 'Topical Paper 2 MCQ Practice with Diagrams',
        descVi: 'Hình vẽ sắc nét từ đề thi gốc Cambridge, tự động chấm điểm và có lời giải thích tiếng Việt từng câu.',
        descEn: 'Crisp Cambridge exam diagrams with instant scoring and Vietnamese step-by-step explanations.',
      },
      {
        src: '/images/course-showcases/igcse_04_test_paper4_ai.webp',
        category: 'practice',
        badgeVi: '📝 Tự luận Paper 4 & AI',
        badgeEn: '📝 Paper 4 AI Grader',
        titleVi: 'Đề thi tự luận Paper 4 (Extended) — Xem PDF gốc & AI chấm điểm',
        titleEn: 'Paper 4 Structured Exam — Original PDF & AI Marking Scheme',
        descVi: 'Chia đôi màn hình xem đề PDF gốc Cambridge bên trái, nhập đáp án từng ý nhỏ bên phải và chấm theo Marking Scheme.',
        descEn: 'Split-screen original Cambridge PDF alongside structured answer inputs graded via Marking Scheme.',
      },
      {
        src: '/images/course-showcases/igcse_05_test_business_case.webp',
        category: 'practice',
        badgeVi: '📝 Case Study 0450',
        badgeEn: '📝 Business Case Study',
        titleVi: 'Kho đề Case Study Business 0450 & Geography 0460',
        titleEn: 'IGCSE Business 0450 & Geography 0460 Case Studies',
        descVi: 'Đọc trực tiếp Insert PDF tình huống doanh nghiệp và trả lời tự luận chấm theo chuẩn AO1–AO4.',
        descEn: 'Read authentic business Case Study inserts and get AO1–AO4 rubric-based AI grading.',
      },
      {
        src: '/images/course-showcases/igcse_06_test_maths_direct.webp',
        category: 'practice',
        badgeVi: '📝 Kho đề Toán 0580',
        badgeEn: '📝 IGCSE Maths 0580',
        titleVi: 'Đề thi Toán IGCSE 0580 Paper 2 & Paper 4 — Công thức KaTeX',
        titleEn: 'IGCSE Maths 0580 Papers 2 & 4 — KaTeX Rendering',
        descVi: 'Hiển thị công thức toán học sắc nét, hỗ trợ gõ lời giải từng bước và chấm chữa theo phương pháp chuẩn.',
        descEn: 'Crisp KaTeX mathematical notation with step-by-step working inputs and detailed feedback.',
      },
    ],
  },

  // 133: Luyện thi SAT cấp tốc
  133: {
    headingVi: 'Hình ảnh thực tế Bài giảng Digital SAT 1500+ & Phòng thi Bluebook',
    headingEn: 'Real LMS Previews: Digital SAT 1500+ Lectures & Bluebook Simulator',
    subheadingVi:
      '36 bài giảng chiến thuật 1500+ (Reading & Writing + Math Desmos 800 + Hard Module 2 Boss) cùng 64 đề Drill & Adaptive Mock trên giao diện mô phỏng chuẩn Bluebook College Board.',
    subheadingEn:
      '36 targeted 1500+ lectures (R&W, Math Desmos 800, Hard Module 2 Boss) plus 64 drills and adaptive mocks on a true-to-life Bluebook exam interface.',
    items: [
      {
        src: '/images/course-showcases/sat_01_lecture_rw.webp',
        category: 'theory',
        badgeVi: '📘 Lý thuyết R&W 1500+',
        badgeEn: '📘 SAT R&W Theory',
        titleVi: 'Bài giảng Digital SAT Reading & Writing — Chiến thuật loại bẫy',
        titleEn: 'Digital SAT Reading & Writing — Trap-Elimination Playbook',
        descVi: 'Phân tích chuyên sâu Words in Context, Transitions, Boundaries và tư duy loại nhiễu 50/50 chuẩn 750–800.',
        descEn: 'Deep strategies for Words in Context, Transitions, Boundaries, and 750–800 trap elimination.',
      },
      {
        src: '/images/course-showcases/sat_02_lecture_math.webp',
        category: 'theory',
        badgeVi: '📘 Lý thuyết Math Desmos',
        badgeEn: '📘 SAT Math & Desmos',
        titleVi: 'Bài giảng SAT Math — Desmos 800 Speed Playbook',
        titleEn: 'SAT Math — Desmos 800 Speed Playbook',
        descVi: 'Làm chủ kỹ thuật giải siêu tốc hệ phương trình, tham số, hồi quy bằng Desmos & 100 thẻ công thức.',
        descEn: 'Master ultra-fast graphing, regression, and parameter solving with Desmos.',
      },
      {
        src: '/images/course-showcases/sat_03_bluebook_rw.webp',
        category: 'practice',
        badgeVi: '📝 Phòng thi Bluebook R&W',
        badgeEn: '📝 Bluebook R&W Lab',
        titleVi: 'Phòng thi giả lập Bluebook Digital SAT — Reading & Writing',
        titleEn: 'Bluebook Digital SAT Simulator — Reading & Writing',
        descVi: 'Giả lập trọn vẹn giao diện thi thật College Board: chia đôi màn hình, gạch chéo loại đáp án, đánh dấu cờ & đếm giờ.',
        descEn: 'Authentic College Board Bluebook experience with split screen, answer eliminator, flagging, and timer.',
      },
      {
        src: '/images/course-showcases/sat_04_bluebook_math.webp',
        category: 'practice',
        badgeVi: '📝 Bluebook Math + Desmos',
        badgeEn: '📝 Bluebook Math + Desmos',
        titleVi: 'Phòng thi Bluebook SAT Math — Tích hợp máy tính đồ thị Desmos',
        titleEn: 'Bluebook SAT Math — Built-In Desmos Graphing Calculator',
        descVi: 'Bấm mở máy tính Desmos và bảng công thức Reference Sheet trực tiếp trong phòng thi, hỗ trợ câu SPR điền số.',
        descEn: 'Built-in Desmos Graphing Calculator, Reference Sheet, KaTeX math, and Student-Produced Response (SPR).',
      },
    ],
  },
};

interface CourseShowcaseGalleryProps {
  courseId: number | null | undefined;
  lang: 'vi' | 'en';
}

export const CourseShowcaseGallery: React.FC<CourseShowcaseGalleryProps> = ({ courseId, lang }) => {
  const [filter, setFilter] = useState<'all' | 'theory' | 'practice'>('all');
  const [lightboxIndex, setLightboxIndex] = useState<number | null>(null);

  const config = courseId ? GALLERY_BY_COURSE_ID[Number(courseId)] : undefined;

  useEffect(() => {
    setFilter('all');
    setLightboxIndex(null);
  }, [courseId]);

  const items = config?.items || [];
  const theoryCount = items.filter((i) => i.category === 'theory').length;
  const practiceCount = items.filter((i) => i.category === 'practice').length;
  const filteredItems =
    filter === 'all' ? items : items.filter((item) => item.category === filter);

  useEffect(() => {
    if (lightboxIndex === null) return;
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';

    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setLightboxIndex(null);
      } else if (e.key === 'ArrowRight') {
        setLightboxIndex((prev) =>
          prev === null ? null : (prev + 1) % filteredItems.length
        );
      } else if (e.key === 'ArrowLeft') {
        setLightboxIndex((prev) =>
          prev === null ? null : (prev - 1 + filteredItems.length) % filteredItems.length
        );
      }
    };
    window.addEventListener('keydown', onKeyDown);
    return () => {
      document.body.style.overflow = prevOverflow;
      window.removeEventListener('keydown', onKeyDown);
    };
  }, [lightboxIndex, filteredItems.length]);

  if (!config || items.length === 0) return null;

  const activeLightboxItem =
    lightboxIndex !== null && filteredItems[lightboxIndex] ? filteredItems[lightboxIndex] : null;

  return (
    <section className="rounded-2xl border border-slate-200/90 bg-gradient-to-b from-slate-50/80 to-white p-4 sm:p-6 space-y-4 shadow-2xs">
      {/* Header + Filter Pills */}
      <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-3 pb-3 border-b border-slate-200/80">
        <div className="space-y-1">
          <div className="inline-flex items-center gap-1.5 text-[11px] font-extrabold uppercase tracking-wider text-[#0a5482] bg-sky-100/80 border border-sky-200/80 px-2.5 py-0.5 rounded-full">
            <Monitor className="w-3.5 h-3.5" />
            <span>{lang === 'vi' ? 'Ảnh chụp màn hình thực tế trên LMS' : 'Live Platform Screenshots'}</span>
          </div>
          <h3 className="text-base sm:text-lg font-black text-slate-900 leading-snug">
            {lang === 'vi' ? config.headingVi : config.headingEn}
          </h3>
          <p className="text-xs sm:text-[13.5px] text-slate-600 leading-relaxed max-w-3xl">
            {lang === 'vi' ? config.subheadingVi : config.subheadingEn}
          </p>
        </div>

        {theoryCount > 0 && practiceCount > 0 && (
          <div className="flex items-center gap-1.5 shrink-0 flex-wrap">
            <button
              type="button"
              onClick={() => setFilter('all')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition cursor-pointer border ${
                filter === 'all'
                  ? 'bg-[#0a5482] text-white border-[#0a5482] shadow-2xs'
                  : 'bg-white text-slate-600 border-slate-200 hover:border-sky-300 hover:text-[#0a5482]'
              }`}
            >
              {lang === 'vi' ? `Tất cả (${items.length})` : `All (${items.length})`}
            </button>
            <button
              type="button"
              onClick={() => setFilter('theory')}
              className={`inline-flex items-center gap-1 px-3 py-1.5 rounded-xl text-xs font-bold transition cursor-pointer border ${
                filter === 'theory'
                  ? 'bg-[#0a5482] text-white border-[#0a5482] shadow-2xs'
                  : 'bg-white text-slate-600 border-slate-200 hover:border-sky-300 hover:text-[#0a5482]'
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>{lang === 'vi' ? `Lý thuyết (${theoryCount})` : `Theory (${theoryCount})`}</span>
            </button>
            <button
              type="button"
              onClick={() => setFilter('practice')}
              className={`inline-flex items-center gap-1 px-3 py-1.5 rounded-xl text-xs font-bold transition cursor-pointer border ${
                filter === 'practice'
                  ? 'bg-emerald-600 text-white border-emerald-600 shadow-2xs'
                  : 'bg-white text-slate-600 border-slate-200 hover:border-emerald-300 hover:text-emerald-700'
              }`}
            >
              <FileText className="w-3.5 h-3.5" />
              <span>{lang === 'vi' ? `Bài tập & Kho đề (${practiceCount})` : `Practice & Tests (${practiceCount})`}</span>
            </button>
          </div>
        )}
      </div>

      {/* Screenshot Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-5">
        {filteredItems.map((item, idx) => {
          const isTheory = item.category === 'theory';
          const badgeText = lang === 'vi'
            ? item.badgeVi || (isTheory ? '📘 Lý thuyết' : '📝 Bài tập / Kho đề')
            : item.badgeEn || (isTheory ? '📘 Theory' : '📝 Practice / Test');
          const title = lang === 'vi' ? item.titleVi : item.titleEn;
          const desc = lang === 'vi' ? item.descVi : item.descEn;

          return (
            <button
              key={item.src}
              type="button"
              onClick={() => setLightboxIndex(idx)}
              className="group text-left bg-white rounded-2xl border border-slate-200/90 hover:border-[#2ab4e8] shadow-2xs hover:shadow-lg transition-all duration-200 overflow-hidden flex flex-col cursor-pointer focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
            >
              <div className="relative w-full aspect-[16/10] bg-slate-100 overflow-hidden border-b border-slate-200/80">
                <img
                  src={item.src}
                  alt={title}
                  loading="lazy"
                  decoding="async"
                  className="w-full h-full object-cover object-top group-hover:scale-[1.03] transition-transform duration-300"
                />
                {/* Category pill */}
                <span
                  className={`absolute top-2.5 left-2.5 px-2.5 py-1 rounded-lg text-[11px] font-extrabold shadow-sm backdrop-blur-md border ${
                    isTheory
                      ? 'bg-[#0a5482]/90 text-white border-white/20'
                      : 'bg-emerald-700/90 text-white border-white/20'
                  }`}
                >
                  {badgeText}
                </span>
                {/* Hover zoom badge */}
                <span className="absolute bottom-2.5 right-2.5 inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-slate-900/80 text-white text-[11px] font-bold opacity-90 sm:opacity-0 sm:group-hover:opacity-100 transition-opacity shadow-sm backdrop-blur-xs">
                  <ZoomIn className="w-3.5 h-3.5" />
                  <span>{lang === 'vi' ? 'Phóng to' : 'Zoom'}</span>
                </span>
              </div>

              <div className="p-3.5 sm:p-4 space-y-1 flex-1 flex flex-col justify-start">
                <h4 className="font-extrabold text-[13.5px] sm:text-[14.5px] text-slate-900 group-hover:text-[#0a5482] transition-colors leading-snug">
                  {title}
                </h4>
                <p className="text-xs sm:text-[13px] text-slate-600 leading-relaxed">
                  {desc}
                </p>
              </div>
            </button>
          );
        })}
      </div>

      <p className="text-[11.5px] text-slate-500 font-medium text-center pt-0.5">
        {lang === 'vi'
          ? '💡 Bấm vào bất kỳ hình ảnh nào để phóng to xem chi tiết giao diện thực tế.'
          : '💡 Click any screenshot above to view it full-size.'}
      </p>

      {/* Interactive Lightbox Modal */}
      {activeLightboxItem && lightboxIndex !== null && (
        <div
          className="fixed inset-0 z-[70] bg-slate-950/90 backdrop-blur-sm flex items-center justify-center p-3 sm:p-6"
          onClick={() => setLightboxIndex(null)}
        >
          <div
            role="dialog"
            aria-modal="true"
            className="relative max-w-6xl w-full flex flex-col items-center gap-3"
            onClick={(e) => e.stopPropagation()}
          >
            {/* Top bar */}
            <div className="w-full flex items-center justify-between gap-3 text-white px-1">
              <div className="flex items-center gap-2 min-w-0">
                <span className="px-2.5 py-1 rounded-lg bg-white/15 border border-white/20 text-xs font-extrabold shrink-0">
                  {lightboxIndex + 1} / {filteredItems.length}
                </span>
                <span className="font-bold text-sm sm:text-base truncate">
                  {lang === 'vi' ? activeLightboxItem.titleVi : activeLightboxItem.titleEn}
                </span>
              </div>
              <button
                type="button"
                onClick={() => setLightboxIndex(null)}
                className="w-9 h-9 rounded-full bg-white/15 hover:bg-white/25 text-white flex items-center justify-center transition cursor-pointer shrink-0"
                aria-label={lang === 'vi' ? 'Đóng' : 'Close'}
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Image + Prev/Next */}
            <div className="relative w-full flex items-center justify-center">
              {filteredItems.length > 1 && (
                <button
                  type="button"
                  onClick={() =>
                    setLightboxIndex((lightboxIndex - 1 + filteredItems.length) % filteredItems.length)
                  }
                  className="absolute left-2 sm:left-3 z-10 w-10 h-10 sm:w-11 sm:h-11 rounded-full bg-slate-900/75 hover:bg-slate-900 text-white border border-white/20 flex items-center justify-center shadow-lg transition cursor-pointer"
                  aria-label="Previous screenshot"
                >
                  <ChevronLeft className="w-6 h-6" />
                </button>
              )}

              <img
                src={activeLightboxItem.src}
                alt={lang === 'vi' ? activeLightboxItem.titleVi : activeLightboxItem.titleEn}
                className="max-h-[75vh] w-auto max-w-full rounded-xl sm:rounded-2xl border border-white/15 shadow-2xl object-contain bg-white"
              />

              {filteredItems.length > 1 && (
                <button
                  type="button"
                  onClick={() => setLightboxIndex((lightboxIndex + 1) % filteredItems.length)}
                  className="absolute right-2 sm:right-3 z-10 w-10 h-10 sm:w-11 sm:h-11 rounded-full bg-slate-900/75 hover:bg-slate-900 text-white border border-white/20 flex items-center justify-center shadow-lg transition cursor-pointer"
                  aria-label="Next screenshot"
                >
                  <ChevronRight className="w-6 h-6" />
                </button>
              )}
            </div>

            {/* Bottom caption */}
            <div className="w-full max-w-3xl text-center bg-white/10 border border-white/15 rounded-xl px-4 py-2.5 text-xs sm:text-sm text-sky-100 font-medium leading-relaxed">
              {lang === 'vi' ? activeLightboxItem.descVi : activeLightboxItem.descEn}
            </div>
          </div>
        </div>
      )}
    </section>
  );
};
