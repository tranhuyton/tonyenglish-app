import { supabase } from './supabase';
import { formatLectureTaskDescription } from './lectureTaskUtils';
import { assignCourseBoardToAllEnrolledUsers } from './boardLectureSync';

interface BoardItemSpec {
  task_type: 'manual' | 'test';
  title: string;
  description: string;
  test_id: string | null;
}

interface BoardCardSpec {
  title: string;
  items: BoardItemSpec[];
}

interface BoardColumnSpec {
  title: string;
  cards: BoardCardSpec[];
}

export interface AutoGenerateBoardsSummary {
  createdBoards: number;
  createdBoardTitles: string[];
  totalCols: number;
  totalCards: number;
  totalItems: number;
  coursesAssignedCount: number;
  usersUpdated: number;
  addedAssignments: number;
}

async function fetchAllRows<T = any>(
  buildQuery: (from: number, to: number) => PromiseLike<{ data: T[] | null; error: any }>
): Promise<T[]> {
  const rows: T[] = [];
  const pageSize = 1000;
  let from = 0;
  while (true) {
    const { data, error } = await buildQuery(from, from + pageSize - 1);
    if (error || !data || data.length === 0) break;
    rows.push(...data);
    if (data.length < pageSize) break;
    from += pageSize;
  }
  return rows;
}

function naturalCompare(a: string, b: string): number {
  return (a || '').localeCompare(b || '', undefined, { numeric: true, sensitivity: 'base' });
}

function stripColorTag(title: string): string {
  return (title || '').replace(/\s*\[color:[^\]]+\]\s*$/i, '').trim();
}

function cleanTestTitle(raw: string): string {
  return (raw || '').replace(/^Làm\s+(?:bài\s+tập|Bluebook\s+Drill)\s*:\s*/i, '').trim();
}

function chunkArray<T>(arr: T[], size: number): T[][] {
  const out: T[][] = [];
  for (let i = 0; i < arr.length; i += size) out.push(arr.slice(i, i + size));
  return out;
}

function extractLectureItems(
  lec: any,
  courseId: string,
  testsById: Map<string, any>,
  defaultManualTasks?: string[]
): { items: BoardItemSpec[]; usedTestIds: Set<string> } {
  const items: BoardItemSpec[] = [];
  const usedTestIds = new Set<string>();
  const tList = Array.isArray(lec.task_list) ? lec.task_list : [];

  const manualTasks = tList.filter((t: any) => t && (t.type || 'manual') === 'manual' && (t.text || t.title));
  const exTasks = tList.filter((t: any) => t && (t.type === 'exercise' || t.type === 'test' || t.test_id) && t.test_id);

  if (manualTasks.length > 0) {
    for (const mt of manualTasks) {
      const text = String(mt.text || mt.title || '').trim();
      items.push({
        task_type: 'manual',
        title: text,
        description: formatLectureTaskDescription({
          lectureId: lec.id,
          lectureTitle: lec.title,
          courseId,
          taskId: mt.id || null,
        }),
        test_id: null,
      });
    }
  } else if (defaultManualTasks && defaultManualTasks.length > 0) {
    for (const text of defaultManualTasks) {
      items.push({
        task_type: 'manual',
        title: text,
        description: formatLectureTaskDescription({
          lectureId: lec.id,
          lectureTitle: lec.title,
          courseId,
          taskId: null,
        }),
        test_id: null,
      });
    }
  }

  const sortedEx = [...exTasks].sort((a, b) => {
    const tA = testsById.get(String(a.test_id))?.title || a.text || '';
    const tB = testsById.get(String(b.test_id))?.title || b.text || '';
    return naturalCompare(tA, tB);
  });

  for (const ex of sortedEx) {
    const tid = String(ex.test_id);
    if (usedTestIds.has(tid)) continue;
    usedTestIds.add(tid);
    const dbTest = testsById.get(tid);
    const title = cleanTestTitle(dbTest?.title || ex.text || 'Bài tập');
    items.push({
      task_type: 'test',
      title,
      description: '',
      test_id: tid,
    });
  }

  return { items, usedTestIds };
}

function buildSatBoardSpec(
  course: any,
  mods: any[],
  lecs: any[],
  folders: any[],
  tests: any[]
): { title: string; columns: BoardColumnSpec[] } {
  const cid = String(course.id);
  const testsById = new Map<string, any>(tests.map(t => [String(t.id), t]));
  const columns: BoardColumnSpec[] = [];
  const usedTestIds = new Set<string>();

  for (const m of [...mods].sort((a, b) => (a.order_index || 999) - (b.order_index || 999))) {
    const mLecs = lecs
      .filter(l => l.module_id === m.id)
      .sort((a, b) => (a.order_index || 999) - (b.order_index || 999));
    const cards: BoardCardSpec[] = [];
    for (const l of mLecs) {
      const { items, usedTestIds: tids } = extractLectureItems(l, cid, testsById);
      tids.forEach(id => usedTestIds.add(id));
      cards.push({ title: l.title, items });
    }
    columns.push({ title: m.title, cards });
  }

  const folderById = new Map<string, any>(folders.map(f => [String(f.id), f]));
  const rwVocabGames: any[] = [];
  const mathGames: any[] = [];
  const rwMocks: any[] = [];
  const mathMocks: any[] = [];

  for (const t of tests) {
    if (usedTestIds.has(String(t.id))) continue;
    const ftitle = String(folderById.get(String(t.folder_id || ''))?.title || '').toLowerCase();
    const ttitle = String(t.title || '').toLowerCase();
    if (ftitle.includes('vocab') || ttitle.includes('vocab')) rwVocabGames.push(t);
    else if (ftitle.includes('formula') || ftitle.includes('desmos') || ftitle.includes('game')) mathGames.push(t);
    else if (ftitle.includes('math') || ttitle.includes('math')) mathMocks.push(t);
    else rwMocks.push(t);
  }

  rwVocabGames.sort((a, b) => naturalCompare(a.title, b.title));
  mathGames.sort((a, b) => naturalCompare(a.title, b.title));
  rwMocks.sort((a, b) => naturalCompare(a.title, b.title));
  mathMocks.sort((a, b) => naturalCompare(a.title, b.title));

  const gameCards: BoardCardSpec[] = [];
  if (rwVocabGames.length > 0) {
    gameCards.push({
      title: '1. Elite SAT Vocabulary Games (Set 1–5: 250 từ)',
      items: rwVocabGames.slice(0, 5).map(t => ({ task_type: 'test', title: t.title, description: '', test_id: String(t.id) })),
    });
    if (rwVocabGames.length > 5) {
      gameCards.push({
        title: '2. Elite SAT Vocabulary Games (Set 6–10: 250 từ)',
        items: rwVocabGames.slice(5).map(t => ({ task_type: 'test', title: t.title, description: '', test_id: String(t.id) })),
      });
    }
  }
  if (mathGames.length > 0) {
    gameCards.push({
      title: '3. Math Formula & Desmos 800 Games (100 thẻ)',
      items: mathGames.map(t => ({ task_type: 'test', title: t.title, description: '', test_id: String(t.id) })),
    });
  }
  if (gameCards.length > 0) {
    columns.push({
      title: '⚡ Speed Games (500 Từ vựng & 100 Công thức) [color:#f3e8ff,#6b21a8]',
      cards: gameCards,
    });
  }

  const mockCards: BoardCardSpec[] = [];
  if (rwMocks.length > 0) {
    mockCards.push({
      title: '1. R&W Adaptive Mock Tests #1–#4 (Đợt 1)',
      items: rwMocks.slice(0, 4).map(t => ({ task_type: 'test', title: t.title, description: '', test_id: String(t.id) })),
    });
    if (rwMocks.length > 4) {
      mockCards.push({
        title: '2. R&W Adaptive Mock Tests #5–#8 (Đợt 2)',
        items: rwMocks.slice(4).map(t => ({ task_type: 'test', title: t.title, description: '', test_id: String(t.id) })),
      });
    }
  }
  if (mathMocks.length > 0) {
    mockCards.push({
      title: '3. Math Adaptive Mock Tests #1–#4 (Đợt 1)',
      items: mathMocks.slice(0, 4).map(t => ({ task_type: 'test', title: t.title, description: '', test_id: String(t.id) })),
    });
    if (mathMocks.length > 4) {
      mockCards.push({
        title: '4. Math Adaptive Mock Tests #5–#8 (Đợt 2)',
        items: mathMocks.slice(4).map(t => ({ task_type: 'test', title: t.title, description: '', test_id: String(t.id) })),
      });
    }
  }
  if (mockCards.length > 0) {
    columns.push({
      title: '🎯 Full-Length Adaptive Mock Tests (Bluebook) [color:#e0f2fe,#0369a1]',
      cards: mockCards,
    });
  }

  return { title: 'Bảng công việc Digital SAT 1500+', columns };
}

function buildModuleLectureBoardSpec(
  course: any,
  boardTitle: string,
  mods: any[],
  lecs: any[],
  tests: any[],
  defaultManualTasks?: string[],
  emptyLecTaskFn?: (lec: any) => string
): { title: string; columns: BoardColumnSpec[] } {
  const cid = String(course.id);
  const testsById = new Map<string, any>(tests.map(t => [String(t.id), t]));
  const columns: BoardColumnSpec[] = [];

  for (const m of [...mods].sort((a, b) => (a.order_index || 999) - (b.order_index || 999))) {
    const mLecs = lecs
      .filter(l => l.module_id === m.id)
      .sort((a, b) => (a.order_index || 999) - (b.order_index || 999));
    if (mLecs.length === 0) continue;
    const cards: BoardCardSpec[] = mLecs.map(l => {
      const fallback = defaultManualTasks || (emptyLecTaskFn ? [emptyLecTaskFn(l)] : undefined);
      const { items } = extractLectureItems(l, cid, testsById, fallback);
      return { title: l.title, items };
    });
    columns.push({ title: m.title, cards });
  }

  return { title: boardTitle, columns };
}

function buildMaths0580BoardSpec(course: any, lecs: any[], tests: any[]): { title: string; columns: BoardColumnSpec[] } {
  const cid = String(course.id);
  const testsById = new Map<string, any>(tests.map(t => [String(t.id), t]));
  const sortedLecs = [...lecs].sort((a, b) => (a.order_index || 999) - (b.order_index || 999));
  const part1: BoardCardSpec[] = [];
  const part2: BoardCardSpec[] = [];
  const rev: BoardCardSpec[] = [];

  for (const l of sortedLecs) {
    const { items } = extractLectureItems(l, cid, testsById);
    const card: BoardCardSpec = { title: l.title, items };
    const m = String(l.title || '').match(/topic\s*(\d+)/i);
    if (m) {
      if (parseInt(m[1], 10) <= 5) part1.push(card);
      else part2.push(card);
    } else {
      rev.push(card);
    }
  }

  return {
    title: 'Bảng công việc IGCSE Maths 0580',
    columns: [
      { title: 'Part 1: Number, Algebra & Geometry (Topic 1–5) [color:#dcfce7,#15803d]', cards: part1 },
      { title: 'Part 2: Trig, Vectors, Probability & Stats (Topic 6–9) [color:#fef9c3,#713f12]', cards: part2 },
      { title: 'Past Papers & Year End Revision [color:#e0f2fe,#0369a1]', cards: rev },
    ].filter(c => c.cards.length > 0),
  };
}

function buildMaths0606BoardSpec(course: any, lecs: any[], tests: any[]): { title: string; columns: BoardColumnSpec[] } {
  const cid = String(course.id);
  const testsById = new Map<string, any>(tests.map(t => [String(t.id), t]));
  const sortedLecs = [...lecs].sort((a, b) => (a.order_index || 999) - (b.order_index || 999));
  const defaultTasks = [
    'Học kỹ lý thuyết & ghi chép công thức trọng tâm',
    'Luyện giải ví dụ mẫu & tự tổng kết dạng bài',
  ];
  const buckets: BoardCardSpec[][] = [[], [], [], []];

  sortedLecs.forEach((l, idx) => {
    const { items } = extractLectureItems(l, cid, testsById, defaultTasks);
    const card: BoardCardSpec = { title: l.title, items };
    if (idx < 5) buckets[0].push(card);
    else if (idx < 9) buckets[1].push(card);
    else if (idx < 13) buckets[2].push(card);
    else buckets[3].push(card);
  });

  if (tests.length > 0) {
    buckets[3].push({
      title: 'Past Papers (Đề thi thật Cambridge 0606)',
      items: [...tests]
        .sort((a, b) => naturalCompare(a.title, b.title))
        .map(t => ({ task_type: 'test', title: t.title, description: '', test_id: String(t.id) })),
    });
  }

  return {
    title: 'Bảng công việc IGCSE Maths 0606',
    columns: [
      { title: 'Part 1: Functions, Quadratics & Polynomials (Ch. 1–5) [color:#e0e7ff,#3730a3]', cards: buckets[0] },
      { title: 'Part 2: Logs, Coordinate & Circular Measure (Ch. 6–9) [color:#ccfbf1,#0f766e]', cards: buckets[1] },
      { title: 'Part 3: Combinatorics, Series & Vectors (Ch. 10–13) [color:#fef3c7,#b45309]', cards: buckets[2] },
      { title: 'Part 4: Calculus, Kinematics & Past Papers (Ch. 14–16) [color:#ffe4e6,#be123c]', cards: buckets[3] },
    ].filter(c => c.cards.length > 0),
  };
}

function buildEsl0510BoardSpec(
  course: any,
  mods: any[],
  lecs: any[],
  folders: any[],
  tests: any[]
): { title: string; columns: BoardColumnSpec[] } {
  const cid = String(course.id);
  const testsById = new Map<string, any>(tests.map(t => [String(t.id), t]));
  const columns: BoardColumnSpec[] = [];
  const linkedTids = new Set<string>();

  for (const m of [...mods].sort((a, b) => (a.order_index || 999) - (b.order_index || 999))) {
    const mLecs = lecs
      .filter(l => l.module_id === m.id)
      .sort((a, b) => (a.order_index || 999) - (b.order_index || 999));
    const cards: BoardCardSpec[] = mLecs.map(l => {
      const { items, usedTestIds } = extractLectureItems(l, cid, testsById, ['Học kỹ bài giảng & ghi chú chiến thuật làm bài']);
      usedTestIds.forEach(id => linkedTids.add(id));
      return { title: l.title, items };
    });
    if (cards.length > 0) columns.push({ title: m.title, cards });
  }

  const yearColors: Record<string, string> = {
    '2024': '[color:#dcfce7,#15803d]',
    '2025': '[color:#fef3c7,#b45309]',
    '2026': '[color:#f3e8ff,#7e22ce]',
  };
  for (const year of ['2024', '2025', '2026']) {
    const yearFolder = folders.find(f => String(f.title || '').trim() === year);
    if (!yearFolder) continue;
    const sessionFolders = folders
      .filter(f => f.parent_id === yearFolder.id)
      .sort((a, b) => ((a.display_order || 999) - (b.display_order || 999)) || naturalCompare(a.title, b.title));
    const cards: BoardCardSpec[] = [];
    for (const sf of sessionFolders) {
      const sfTests = tests
        .filter(t => t.folder_id === sf.id && !linkedTids.has(String(t.id)))
        .sort((a, b) => naturalCompare(a.title, b.title));
      if (sfTests.length > 0) {
        cards.push({
          title: sf.title,
          items: sfTests.map(t => ({ task_type: 'test', title: t.title, description: '', test_id: String(t.id) })),
        });
      }
    }
    if (cards.length > 0) {
      columns.push({ title: `Past Papers ${year} ${yearColors[year]}`, cards });
    }
  }

  return { title: 'Bảng công việc IGCSE ESL 0510', columns };
}

function buildGrammarVocabBoardSpec(
  course: any,
  mods: any[],
  lecs: any[],
  folders: any[],
  tests: any[]
): { title: string; columns: BoardColumnSpec[] } {
  const cid = String(course.id);
  const testsById = new Map<string, any>(tests.map(t => [String(t.id), t]));
  const columns: BoardColumnSpec[] = [];

  for (const m of [...mods].sort((a, b) => (a.order_index || 999) - (b.order_index || 999))) {
    const mLecs = lecs
      .filter(l => l.module_id === m.id)
      .sort((a, b) => (a.order_index || 999) - (b.order_index || 999));
    const cards: BoardCardSpec[] = mLecs.map(l => {
      const { items } = extractLectureItems(l, cid, testsById, ['Học lý thuyết bài giảng & ghi chép cấu trúc ví dụ']);
      return { title: l.title, items };
    });
    if (cards.length > 0) columns.push({ title: m.title, cards });
  }

  const folderStyles: Record<string, { title: string; chunk?: number }> = {
    grammar: { title: 'Bài tập Ngữ pháp (Grammar) [color:#dcfce7,#15803d]' },
    'vocabulary organiser': { title: 'Vocabulary Organiser [color:#ffedd5,#c2410c]' },
    '4000 english words': { title: '4000 English Words [color:#e0e7ff,#4338ca]' },
    'expand vocabulary through reading': { title: 'Expand Vocabulary Through Reading [color:#fce7f3,#be185d]', chunk: 8 },
  };

  const topFolders = folders
    .filter(f => !f.parent_id)
    .sort((a, b) => (a.display_order || 999) - (b.display_order || 999));

  for (const tf of topFolders) {
    const style = folderStyles[String(tf.title || '').trim().toLowerCase()] || { title: `${tf.title} [color:#e0f2fe,#0369a1]`, chunk: 10 };
    const subFolders = folders
      .filter(f => f.parent_id === tf.id)
      .sort((a, b) => ((a.display_order || 999) - (b.display_order || 999)) || naturalCompare(a.title, b.title));
    const cards: BoardCardSpec[] = [];
    if (subFolders.length > 0) {
      for (const sf of subFolders) {
        const sfTests = tests
          .filter(t => t.folder_id === sf.id)
          .sort((a, b) => ((a.order_index || 999) - (b.order_index || 999)) || naturalCompare(a.title, b.title));
        if (sfTests.length > 0) {
          cards.push({
            title: sf.title,
            items: sfTests.map(t => ({ task_type: 'test', title: t.title, description: '', test_id: String(t.id) })),
          });
        }
      }
    } else {
      const directTests = tests
        .filter(t => t.folder_id === tf.id)
        .sort((a, b) => ((a.order_index || 999) - (b.order_index || 999)) || naturalCompare(a.title, b.title));
      const sz = style.chunk || 10;
      chunkArray(directTests, sz).forEach((grp, gIdx) => {
        const startN = gIdx * sz + 1;
        const endN = startN + grp.length - 1;
        cards.push({
          title: `${gIdx + 1}. Reading Pack ${startN}–${endN}`,
          items: grp.map(t => ({ task_type: 'test', title: t.title, description: '', test_id: String(t.id) })),
        });
      });
    }
    if (cards.length > 0) columns.push({ title: style.title, cards });
  }

  return { title: 'Bảng công việc Grammar and Vocabulary', columns };
}

function buildGiaoTiepBoardSpec(
  course: any,
  mods: any[],
  lecs: any[],
  folders: any[],
  tests: any[]
): { title: string; columns: BoardColumnSpec[] } {
  const cid = String(course.id);
  const sortedMods = [...mods].sort((a, b) => (a.order_index || 999) - (b.order_index || 999));

  const buildStageCards = (modSlice: any[]): BoardCardSpec[] =>
    modSlice.map((m, idx) => {
      const mLecs = lecs
        .filter(l => l.module_id === m.id)
        .sort((a, b) => (a.order_index || 999) - (b.order_index || 999));
      return {
        title: `${idx + 1}. ${stripColorTag(m.title)}`,
        items: mLecs.map(l => ({
          task_type: 'manual' as const,
          title: `Luyện phản xạ: ${l.title}`,
          description: formatLectureTaskDescription({ lectureId: l.id, lectureTitle: l.title, courseId: cid, taskId: null }),
          test_id: null,
        })),
      };
    });

  const columns: BoardColumnSpec[] = [
    { title: 'Giai đoạn 1: Mẫu câu 01–30 & Ôn tập [color:#ccfbf1,#0f766e]', cards: buildStageCards(sortedMods.slice(0, 4)) },
    { title: 'Giai đoạn 2: Mẫu câu 31–60 & Ôn tập [color:#e0f2fe,#0369a1]', cards: buildStageCards(sortedMods.slice(4, 8)) },
    { title: 'Giai đoạn 3: Mẫu câu 61–90 & Ôn tập [color:#f3e8ff,#7e22ce]', cards: buildStageCards(sortedMods.slice(8, 12)) },
  ].filter(c => c.cards.length > 0);

  if (sortedMods.length >= 13) {
    const m13 = sortedMods[12];
    const m13Lecs = lecs
      .filter(l => l.module_id === m13.id)
      .sort((a, b) => (a.order_index || 999) - (b.order_index || 999));
    columns.push({
      title: m13.title,
      cards: m13Lecs.map((l, idx) => ({
        title: `${idx + 1}. ${l.title}`,
        items: [
          {
            task_type: 'manual',
            title: 'Học bài giảng & luyện phản xạ tình huống',
            description: formatLectureTaskDescription({ lectureId: l.id, lectureTitle: l.title, courseId: cid, taskId: null }),
            test_id: null,
          },
        ],
      })),
    });
  }

  const topFolders = folders
    .filter(f => !f.parent_id)
    .sort((a, b) => (a.display_order || 999) - (b.display_order || 999));
  const listenColors = ['[color:#dcfce7,#15803d]', '[color:#ffedd5,#c2410c]', '[color:#ffe4e6,#be123c]'];
  topFolders.forEach((tf, fIdx) => {
    const fTests = tests
      .filter(t => t.folder_id === tf.id)
      .sort((a, b) => ((a.order_index || 999) - (b.order_index || 999)) || naturalCompare(a.title, b.title));
    const cards: BoardCardSpec[] = chunkArray(fTests, 12).map((grp, gIdx) => {
      const sN = gIdx * 12 + 1;
      const eN = sN + grp.length - 1;
      return {
        title: `${gIdx + 1}. Listening Pack ${sN}–${eN}`,
        items: grp.map(t => ({ task_type: 'test', title: t.title, description: '', test_id: String(t.id) })),
      };
    });
    if (cards.length > 0) {
      columns.push({ title: `${tf.title} ${listenColors[fIdx % listenColors.length]}`, cards });
    }
  });

  return { title: 'Bảng công việc Giao tiếp và phản xạ', columns };
}

function buildVanPhongBoardSpec(course: any, mods: any[], lecs: any[]): { title: string; columns: BoardColumnSpec[] } {
  const cid = String(course.id);
  const sortedMods = [...mods].sort((a, b) => (a.order_index || 999) - (b.order_index || 999));

  const buildTopicCards = (modSlice: any[]): BoardCardSpec[] =>
    modSlice.map(m => {
      const mLecs = lecs
        .filter(l => l.module_id === m.id)
        .sort((a, b) => (a.order_index || 999) - (b.order_index || 999));
      return {
        title: stripColorTag(m.title),
        items: mLecs.map(l => ({
          task_type: 'manual' as const,
          title: `Hoàn thành bài giảng: ${l.title}`,
          description: formatLectureTaskDescription({ lectureId: l.id, lectureTitle: l.title, courseId: cid, taskId: null }),
          test_id: null,
        })),
      };
    });

  return {
    title: 'Bảng công việc Tiếng Anh văn phòng',
    columns: [
      { title: 'Phần 1: Văn phòng, Thương mại & Công tác (1–4) [color:#ccfbf1,#0f766e]', cards: buildTopicCards(sortedMods.slice(0, 4)) },
      { title: 'Phần 2: Tiếp khách, Mua sắm & Ẩm thực (5–7) [color:#fce7f3,#be185d]', cards: buildTopicCards(sortedMods.slice(4, 7)) },
      { title: 'Phần 3: Nhân sự, Tài chính & Phát triển SP (8–10) [color:#ffedd5,#c2410c]', cards: buildTopicCards(sortedMods.slice(7, 10)) },
      { title: 'Phần 4: Sản xuất, Tài sản & Y tế (11–13) [color:#e0f2fe,#0369a1]', cards: buildTopicCards(sortedMods.slice(10, 13)) },
    ].filter(c => c.cards.length > 0),
  };
}

function buildSpecForCourse(course: any, mods: any[], lecs: any[], folders: any[], tests: any[]) {
  const titleLow = String(course.title || '').toLowerCase();
  if (titleLow.includes('sat') || course.type === 'SAT') {
    return buildSatBoardSpec(course, mods, lecs, folders, tests);
  }
  if (titleLow.includes('physics-0625')) {
    return buildModuleLectureBoardSpec(
      course,
      'Bảng công việc IGCSE Physics 0625',
      mods,
      lecs,
      tests,
      undefined,
      l => `Nghe trọn ${l.title} & ghi chú kiến thức trọng tâm`
    );
  }
  if (titleLow.includes('chemistry-0620')) {
    return buildModuleLectureBoardSpec(
      course,
      'Bảng công việc IGCSE Chemistry 0620',
      mods,
      lecs,
      tests,
      undefined,
      l => `Nghe trọn ${l.title} & ghi chú kiến thức trọng tâm`
    );
  }
  if (titleLow.includes('maths-0580')) {
    return buildMaths0580BoardSpec(course, lecs, tests);
  }
  if (titleLow.includes('maths-0606')) {
    return buildMaths0606BoardSpec(course, lecs, tests);
  }
  if (titleLow.includes('esl-0510')) {
    return buildEsl0510BoardSpec(course, mods, lecs, folders, tests);
  }
  if (titleLow.includes('grammar and vocabulary')) {
    return buildGrammarVocabBoardSpec(course, mods, lecs, folders, tests);
  }
  if (titleLow.includes('phát âm')) {
    return buildModuleLectureBoardSpec(course, 'Bảng công việc Phát Âm', mods, lecs, tests, [
      'Xem bài giảng & ghi nhớ khẩu hình / quy tắc phát âm',
      'Luyện đọc to theo audio mẫu & tự ghi âm kiểm tra',
    ]);
  }
  if (titleLow.includes('giao tiếp')) {
    return buildGiaoTiepBoardSpec(course, mods, lecs, folders, tests);
  }
  if (titleLow.includes('văn phòng')) {
    return buildVanPhongBoardSpec(course, mods, lecs);
  }
  return buildModuleLectureBoardSpec(course, `Bảng công việc ${course.title}`, mods, lecs, tests, [
    'Học bài giảng & ghi chú kiến thức trọng tâm',
  ]);
}

/**
 * Generates Task Boards for EVERY course that does not yet have a populated board
 * (reusing any empty stub `board_templates` row cleanly) and then assigns every
 * course's active board to ALL students enrolled in that course (16/16 coverage).
 * Runs under the currently authenticated Admin session.
 */
export async function generateMissingBoardsAndAssignEnrolledStudents(
  onProgress?: (msg: string) => void
): Promise<AutoGenerateBoardsSummary> {
  onProgress?.('Đang quét danh sách khóa học & bảng công việc hiện có...');

  const [courses, boards, existingCols, mods, lecs, folders, tests] = await Promise.all([
    fetchAllRows((from, to) => supabase.from('courses').select('id, title, type, order_index').order('order_index').order('id').range(from, to)),
    fetchAllRows((from, to) => supabase.from('board_templates').select('*').order('id').range(from, to)),
    fetchAllRows((from, to) => supabase.from('board_columns').select('id, board_template_id, course_id').order('id').range(from, to)),
    fetchAllRows((from, to) => supabase.from('lecture_modules').select('*').order('order_index').order('id').range(from, to)),
    fetchAllRows((from, to) => supabase.from('lectures').select('id, course_id, module_id, title, order_index, task_list').order('order_index').order('id').range(from, to)),
    fetchAllRows((from, to) => supabase.from('folders').select('*').order('display_order').order('id').range(from, to)),
    fetchAllRows((from, to) => supabase.from('tests').select('id, course_id, folder_id, title, test_type, order_index').order('order_index').order('id').range(from, to)),
  ]);

  const summary: AutoGenerateBoardsSummary = {
    createdBoards: 0,
    createdBoardTitles: [],
    totalCols: 0,
    totalCards: 0,
    totalItems: 0,
    coursesAssignedCount: 0,
    usersUpdated: 0,
    addedAssignments: 0,
  };

  const colCountByBoard = new Map<string, number>();
  for (const col of existingCols) {
    const btid = String(col.board_template_id || '');
    if (btid) colCountByBoard.set(btid, (colCountByBoard.get(btid) || 0) + 1);
  }

  for (const course of courses) {
    const cid = String(course.id);
    const cBoards = boards.filter(b => String(b.course_id) === cid);
    const populatedBoard = cBoards.find(b => (colCountByBoard.get(String(b.id)) || 0) > 0);
    if (populatedBoard) continue;

    onProgress?.(`Đang khởi tạo Bảng Công Việc: ${course.title}...`);

    const cMods = mods.filter(m => String(m.course_id) === cid);
    const cLecs = lecs.filter(l => String(l.course_id) === cid);
    const cFolders = folders.filter(f => String(f.course_id) === cid);
    const cTests = tests.filter(t => String(t.course_id) === cid);

    const spec = buildSpecForCourse(course, cMods, cLecs, cFolders, cTests);
    if (spec.columns.length === 0) continue;

    let tplId: string | null = cBoards[0]?.id || null;
    if (tplId) {
      await supabase.from('board_templates').update({ title: spec.title, is_active: true }).eq('id', tplId);
    } else {
      const { data: createdTpl, error: tplErr } = await supabase
        .from('board_templates')
        .insert({ course_id: cid, title: spec.title, is_active: true })
        .select('id')
        .single();
      if (tplErr || !createdTpl) throw new Error(`Không thể tạo board_templates cho ${course.title}: ${tplErr?.message}`);
      tplId = createdTpl.id;
    }

    const colPayloads = spec.columns.map((col, idx) => ({
      course_id: cid,
      board_template_id: tplId,
      title: col.title,
      order_index: idx + 1,
    }));
    const { data: insertedCols, error: colErr } = await supabase
      .from('board_columns')
      .insert(colPayloads)
      .select('id, order_index');
    if (colErr || !insertedCols) throw new Error(`Không thể tạo board_columns cho ${course.title}: ${colErr?.message}`);

    const colIdByOrder = new Map<number, string>(insertedCols.map((c: any) => [c.order_index, c.id]));

    const cardPayloads: any[] = [];
    const cardItemsPlan: BoardItemSpec[][] = [];
    spec.columns.forEach((col, colIdx) => {
      const colId = colIdByOrder.get(colIdx + 1);
      if (!colId) return;
      let cardOrder = 0;
      for (const card of col.cards) {
        if (!card.items || card.items.length === 0) continue;
        cardOrder++;
        cardPayloads.push({
          column_id: colId,
          title: card.title,
          order_index: cardOrder,
        });
        cardItemsPlan.push(card.items);
      }
    });

    const insertedCards: any[] = [];
    for (const chunk of chunkArray(cardPayloads, 100)) {
      const { data: cData, error: cErr } = await supabase.from('board_cards').insert(chunk).select('id');
      if (cErr || !cData) throw new Error(`Không thể tạo board_cards cho ${course.title}: ${cErr?.message}`);
      insertedCards.push(...cData);
    }

    const itemPayloads: any[] = [];
    insertedCards.forEach((cardRow, idx) => {
      const items = cardItemsPlan[idx] || [];
      items.forEach((it, itemIdx) => {
        itemPayloads.push({
          card_id: cardRow.id,
          task_type: it.task_type,
          title: it.title,
          description: it.description || '',
          test_id: it.test_id || null,
          order_index: itemIdx + 1,
        });
      });
    });

    for (const chunk of chunkArray(itemPayloads, 100)) {
      const { error: iErr } = await supabase.from('board_card_items').insert(chunk);
      if (iErr) throw new Error(`Không thể tạo board_card_items cho ${course.title}: ${iErr.message}`);
    }

    summary.createdBoards++;
    summary.createdBoardTitles.push(spec.title);
    summary.totalCols += insertedCols.length;
    summary.totalCards += insertedCards.length;
    summary.totalItems += itemPayloads.length;
  }

  // Assign active course boards to ALL enrolled students across ALL courses
  for (const course of courses) {
    onProgress?.(`Đang gán Bảng Công Việc cho học viên khóa: ${course.title}...`);
    const assignRes = await assignCourseBoardToAllEnrolledUsers(String(course.id));
    if (assignRes.usersTotal > 0) {
      summary.coursesAssignedCount++;
      summary.usersUpdated += assignRes.usersUpdated;
      summary.addedAssignments += assignRes.addedItems;
    }
  }

  return summary;
}
