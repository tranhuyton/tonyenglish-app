import { supabase } from './supabase';

export interface TutorActionItem {
  type: 'OPEN_LECTURE' | 'OPEN_FOLDER' | 'OPEN_LIBRARY' | 'OPEN_AI_ROOM' | 'OPEN_TAB';
  target: string;
  label: string;
}

export interface GlobalStudentSnapshot {
  userId: string;
  studentName: string;
  courseId: string;
  courseTitle: string;
  isIelts: boolean;
  isIgcse0654: boolean;
  lastLecture: {
    id?: string;
    title: string;
    timeLabel: string;
  } | null;
  recentTests: Array<{
    title: string;
    scoreLabel: string;
    percent: number;
    isLow: boolean;
    dateLabel: string;
    skill: string;
  }>;
  taskProgress: {
    completedTasks: number;
    totalTasks: number;
    percent: number;
    completedLecturesCount: number;
    totalLecturesCount: number;
    inProgressLectures: Array<{
      id: string;
      title: string;
      done: number;
      total: number;
      moduleName: string;
    }>;
    nextUpLectures: Array<{
      id: string;
      title: string;
      total: number;
      moduleName: string;
    }>;
    recentlyDoneLectures: Array<{
      id: string;
      title: string;
    }>;
  };
  libraryProgress: {
    camReadingCount: number;
    camListeningCount: number;
    recentLibraryTitles: string[];
  };
  skillSummary: Record<string, { count: number; avgLabel: string }>;
  promptContext: string;
  fetchedAt: number;
}

const cleanTitle = (raw: string) =>
  (raw || '')
    .replace(/\s*\[color:[^\]]*\]/gi, '')
    .replace(/\s*\[bg:[^\]]*\]/gi, '')
    .trim();

export const extractStudentFirstName = (rawName?: string | null): string => {
  const cleaned = (rawName || '').trim();
  if (!cleaned || cleaned.toLowerCase() === 'học viên' || cleaned.toLowerCase() === 'em') {
    return 'em';
  }
  const parts = cleaned.split(/\s+/).filter(Boolean);
  return parts[parts.length - 1] || cleaned;
};

const formatShortDate = (iso?: string) => {
  if (!iso) return '';
  try {
    const d = new Date(iso);
    return `${String(d.getDate()).padStart(2, '0')}/${String(d.getMonth() + 1).padStart(2, '0')}`;
  } catch {
    return '';
  }
};

const snapshotMemoryCache = new Map<string, GlobalStudentSnapshot>();

export function clearGlobalTutorCache() {
  snapshotMemoryCache.clear();
}

export async function fetchGlobalStudentSnapshot(
  courseIdInput?: string | null,
  courseTitleInput?: string | null,
  forceRefresh = false
): Promise<GlobalStudentSnapshot | null> {
  try {
    const { data: authData } = await supabase.auth.getUser();
    const user = authData?.user;
    if (!user) return null;

    const resolvedCourseId =
      courseIdInput ||
      sessionStorage.getItem('lms_active_course_id') ||
      sessionStorage.getItem('portal_selected_course_id') ||
      localStorage.getItem('portal_filter_course') ||
      '239a64f0-c106-40e5-a6e2-4e685a0d70fb';

    const cacheKey = `${user.id}_${resolvedCourseId}`;
    const cached = snapshotMemoryCache.get(cacheKey);
    if (!forceRefresh && cached && Date.now() - cached.fetchedAt < 120_000) {
      return cached;
    }

    // Fetch student profile, course info, modules, lectures, folders, test results, assignments, lecture_progress, activity_logs in parallel
    const [
      profileRes,
      courseRes,
      modulesRes,
      lecturesRes,
      foldersRes,
      courseTestsRes,
      testResultsRes,
      assignmentsRes,
      lectureProgRes,
      activityLogsRes,
    ] = await Promise.all([
      supabase.from('profiles').select('full_name, email').eq('id', user.id).maybeSingle(),
      resolvedCourseId && resolvedCourseId !== 'all'
        ? supabase.from('courses').select('id, title, type').eq('id', resolvedCourseId).maybeSingle()
        : Promise.resolve({ data: null }),
      resolvedCourseId && resolvedCourseId !== 'all'
        ? supabase
            .from('lecture_modules')
            .select('id, title, order_index')
            .eq('course_id', resolvedCourseId)
            .order('order_index')
        : Promise.resolve({ data: [] }),
      resolvedCourseId && resolvedCourseId !== 'all'
        ? supabase
            .from('lectures')
            .select('id, title, module_id, order_index, task_list')
            .eq('course_id', resolvedCourseId)
            .eq('is_published', true)
            .order('order_index')
        : Promise.resolve({ data: [] }),
      resolvedCourseId && resolvedCourseId !== 'all'
        ? supabase
            .from('folders')
            .select('id, title, parent_id')
            .eq('course_id', resolvedCourseId)
        : Promise.resolve({ data: [] }),
      resolvedCourseId && resolvedCourseId !== 'all'
        ? supabase
            .from('tests')
            .select('id, title, folder_id, course_id')
        : Promise.resolve({ data: [] }),
      supabase
        .from('test_results')
        .select('id, test_title, score, total_score, details, created_at')
        .eq('user_id', user.id)
        .order('created_at', { ascending: false })
        .limit(80),
      supabase
        .from('assignments')
        .select('id, title, card_title, student_completed, is_completed, task_type, test_id')
        .eq('user_id', user.id),
      supabase
        .from('lecture_progress')
        .select('lecture_id, completed_tasks, is_completed')
        .eq('user_id', user.id),
      supabase
        .from('activity_logs')
        .select('action_type, details, created_at')
        .eq('user_id', user.id)
        .order('created_at', { ascending: false })
        .limit(120),
    ]);

    const rawFullName =
      profileRes.data?.full_name ||
      user.user_metadata?.full_name ||
      user.email?.split('@')[0] ||
      'Học viên';
    const studentName = extractStudentFirstName(rawFullName);

    const courseTitle = cleanTitle(
      courseTitleInput || courseRes.data?.title || 'IELTS Premium'
    );
    const lowerCourseTitle = courseTitle.toLowerCase();
    const isIelts =
      resolvedCourseId === '239a64f0-c106-40e5-a6e2-4e685a0d70fb' ||
      lowerCourseTitle.includes('ielts');
    const isIgcse0654 =
      resolvedCourseId === 'a2a949c7-c23e-45a7-82fa-cdeda5cc32a7' ||
      lowerCourseTitle.includes('co-ordinated') ||
      lowerCourseTitle.includes('0654');

    const modules = (modulesRes.data || []) as any[];
    const moduleMap = new Map<string, string>();
    modules.forEach((m) => moduleMap.set(String(m.id), cleanTitle(m.title || 'Học phần')));

    const lectures = (lecturesRes.data || []) as any[];
    const folders = (foldersRes.data || []) as any[];
    const rootFolders = folders.filter((f) => !f.parent_id);
    const folderMap = new Map<string, { id: string; title: string; parent_id: string | null }>();
    folders.forEach((f) =>
      folderMap.set(String(f.id), {
        id: String(f.id),
        title: cleanTitle(f.title || ''),
        parent_id: f.parent_id ? String(f.parent_id) : null,
      })
    );

    const isFolderInsideCambridge = (folderId?: string | null): boolean => {
      let curId = folderId ? String(folderId) : null;
      let depth = 0;
      while (curId && depth < 15) {
        depth++;
        const f = folderMap.get(curId);
        if (!f) break;
        if (f.title.toLowerCase().includes('cambridge')) return true;
        curId = f.parent_id;
      }
      return false;
    };

    const allTestsMeta = (courseTestsRes.data || []) as any[];
    const courseTests = allTestsMeta.filter(
      (t) =>
        String(t.course_id) === String(resolvedCourseId) ||
        (t.folder_id && folderMap.has(String(t.folder_id)))
    );
    const courseTestIds = new Set<string>(courseTests.map((t) => String(t.id)));
    const courseTestTitles = new Set<string>(
      courseTests.map((t) => cleanTitle(t.title || '').toLowerCase()).filter(Boolean)
    );
    const testFolderById = new Map<string, string>();
    const testFolderByTitle = new Map<string, string>();
    courseTests.forEach((t) => {
      const tid = String(t.id);
      const tTitle = cleanTitle(t.title || '').toLowerCase();
      if (t.folder_id) {
        testFolderById.set(tid, String(t.folder_id));
        if (tTitle) testFolderByTitle.set(tTitle, String(t.folder_id));
      }
    });

    // 1. Parse Test Results & Build Score Map for Lecture Exercise Reconciliation
    const rawTestResults = (testResultsRes.data || []) as any[];
    const passedTestKeys = new Set<string>();
    const recentTests: GlobalStudentSnapshot['recentTests'] = [];
    const skillBuckets: Record<string, { bands: number[]; percents: number[] }> = {
      Listening: { bands: [], percents: [] },
      Reading: { bands: [], percents: [] },
      Writing: { bands: [], percents: [] },
      Speaking: { bands: [], percents: [] },
    };

    rawTestResults.forEach((r) => {
      let d = r.details;
      if (typeof d === 'string') {
        try {
          d = JSON.parse(d);
        } catch {}
      }
      const testId = d?.test_id ? String(d.test_id) : '';
      const rawTitle = cleanTitle(r.test_title || d?.test_title || 'Bài kiểm tra');
      const lowerTitle = rawTitle.toLowerCase();
      const score = parseFloat(r.score != null ? r.score : 0);
      const total = parseFloat(r.total_score != null ? r.total_score : 0);
      const bandScore = d?.bandScore != null ? parseFloat(d.bandScore) : null;

      // Determine whether this test is inside the "Cambridge Test" folder tree (only Cambridge Test uses Band score; Crash Course, Cram Course, Strategies, Unit tests use %)
      const matchedFolderId =
        (testId && testFolderById.get(testId)) ||
        (lowerTitle && testFolderByTitle.get(lowerTitle)) ||
        null;
      const isCambridgeTest =
        isFolderInsideCambridge(matchedFolderId) || lowerTitle.includes('cambridge');

      let percent = 0;
      let isPassed = false;
      let scoreLabel = '';
      let isLow = false;

      if (isIelts && isCambridgeTest && bandScore != null && !isNaN(bandScore) && bandScore > 0) {
        scoreLabel = total > 0 ? `${score}/${total} (Band ${bandScore.toFixed(1)})` : `Band ${bandScore.toFixed(1)}`;
        percent = total > 0 ? Math.round((score / total) * 100) : Math.round((bandScore / 9) * 100);
        isPassed = bandScore >= 4.0;
        isLow = bandScore < 6.0;
      } else if (total > 0) {
        percent = Math.round((score / total) * 100);
        scoreLabel = `${score}/${total} (${percent}%)`;
        isPassed = percent >= 50;
        isLow = percent < 65;
      } else if (bandScore != null && !isNaN(bandScore) && bandScore > 0 && isCambridgeTest) {
        scoreLabel = `Band ${bandScore.toFixed(1)}`;
        percent = Math.round((bandScore / 9) * 100);
        isPassed = bandScore >= 4.0;
        isLow = bandScore < 6.0;
      } else {
        percent = score <= 10 ? Math.round(score * 10) : Math.round(score);
        scoreLabel = `${percent}%`;
        isPassed = percent >= 50;
        isLow = percent < 65;
      }

      if (isPassed) {
        if (testId) passedTestKeys.add(testId);
        if (lowerTitle) passedTestKeys.add(lowerTitle);
      }

      // Check if this test belongs to the active course (and is not an abandoned 0-score click)
      const isNonZeroSubmission = score > 0 || (bandScore != null && !isNaN(bandScore) && bandScore > 0);
      if (!isNonZeroSubmission) return;

      const matchesCourseByIdOrTitle =
        (testId && courseTestIds.has(testId)) || (lowerTitle && courseTestTitles.has(lowerTitle));
      const courseKeywords = lowerCourseTitle
        .replace(/[^a-z0-9\u00C0-\u1EF9\s]/gi, ' ')
        .split(/\s+/)
        .filter((w) => w.length >= 4 && !['igcse', 'course', 'khóa', 'luyện', 'tiếng'].includes(w));
      const matchesCourseByKeyword = isIelts
        ? lowerTitle.includes('ielts') ||
          lowerTitle.includes('cambridge') ||
          lowerTitle.includes('listening') ||
          lowerTitle.includes('reading') ||
          lowerTitle.includes('writing') ||
          lowerTitle.includes('speaking') ||
          bandScore != null
        : isIgcse0654
        ? lowerTitle.includes('0654') ||
          lowerTitle.includes('science') ||
          lowerTitle.includes('biology') ||
          lowerTitle.includes('chemistry') ||
          lowerTitle.includes('physics') ||
          /^([bcp]\d+)\b/i.test(rawTitle)
        : courseTestIds.size === 0 && courseKeywords.some((kw) => lowerTitle.includes(kw));

      if (!matchesCourseByIdOrTitle && !matchesCourseByKeyword) return;

      // Detect skill
      let skill = 'Tổng hợp';
      if (lowerTitle.includes('listen') || lowerTitle.includes('nghe') || d?.skill === 'listening') {
        skill = 'Listening';
      } else if (
        lowerTitle.includes('read') ||
        lowerTitle.includes('đọc') ||
        lowerTitle.includes('passage') ||
        lowerTitle.includes('crash') ||
        lowerTitle.includes('cram')
      ) {
        skill = 'Reading';
      } else if (lowerTitle.includes('writ') || lowerTitle.includes('task 1') || lowerTitle.includes('task 2')) {
        skill = 'Writing';
      } else if (lowerTitle.includes('speak') || lowerTitle.includes('nói')) {
        skill = 'Speaking';
      }

      if (skillBuckets[skill]) {
        if (isIelts && isCambridgeTest && bandScore != null && !isNaN(bandScore) && bandScore > 0) {
          skillBuckets[skill].bands.push(bandScore);
        } else {
          skillBuckets[skill].percents.push(percent);
        }
      }

      if (recentTests.length < 8) {
        recentTests.push({
          title: rawTitle,
          scoreLabel,
          percent,
          isLow,
          dateLabel: formatShortDate(r.created_at),
          skill,
        });
      }
    });

    const skillSummary: Record<string, { count: number; avgLabel: string }> = {};
    Object.entries(skillBuckets).forEach(([sk, bucket]) => {
      const totalCount = bucket.bands.length + bucket.percents.length;
      if (totalCount > 0) {
        const parts: string[] = [];
        if (bucket.bands.length > 0) {
          const avgBand = bucket.bands.reduce((a, b) => a + b, 0) / bucket.bands.length;
          parts.push(`Cambridge Band ~${avgBand.toFixed(1)}`);
        }
        if (bucket.percents.length > 0) {
          const avgPct = Math.round(
            bucket.percents.reduce((a, b) => a + b, 0) / bucket.percents.length
          );
          parts.push(`Bài tập ${avgPct}%`);
        }
        skillSummary[sk] = {
          count: totalCount,
          avgLabel: parts.join(', '),
        };
      }
    });

    // 2. Reconcile Lecture Progress & Assignments
    const assignments = (assignmentsRes.data || []) as any[];
    const progMap = new Map<string, Set<string>>();
    (lectureProgRes.data || []).forEach((p: any) => {
      progMap.set(String(p.lecture_id), new Set(Array.isArray(p.completed_tasks) ? p.completed_tasks : []));
    });

    let completedTasksCount = 0;
    let totalTasksCount = 0;
    let completedLecturesCount = 0;
    const inProgressLectures: GlobalStudentSnapshot['taskProgress']['inProgressLectures'] = [];
    const nextUpLectures: GlobalStudentSnapshot['taskProgress']['nextUpLectures'] = [];
    const recentlyDoneLectures: GlobalStudentSnapshot['taskProgress']['recentlyDoneLectures'] = [];

    // Sort lectures by module order then lecture order_index
    const modOrderMap = new Map<string, number>();
    modules.forEach((m, idx) => modOrderMap.set(String(m.id), m.order_index ?? idx));
    const sortedLectures = [...lectures].sort((a, b) => {
      const ma = modOrderMap.get(String(a.module_id)) ?? 999;
      const mb = modOrderMap.get(String(b.module_id)) ?? 999;
      if (ma !== mb) return ma - mb;
      return (a.order_index ?? 0) - (b.order_index ?? 0);
    });

    const nextUpPerModuleCount = new Map<string, number>();

    sortedLectures.forEach((lec) => {
      const lecId = String(lec.id);
      const lecTitle = cleanTitle(lec.title || 'Bài giảng');
      const modName = moduleMap.get(String(lec.module_id)) || 'Chuyên đề';
      const taskList = Array.isArray(lec.task_list) ? lec.task_list : [];
      const total = taskList.length;

      const doneSet = new Set<string>(progMap.get(lecId) || []);
      taskList.forEach((t: any) => {
        if (t.type === 'manual') {
          const syncTitle = `${lec.title || ''} : ${t.text}`;
          const matched = assignments.some(
            (a) =>
              a.student_completed &&
              a.card_title === lec.title &&
              (a.title === syncTitle || a.title === t.text || a.title === `[Bài giảng] ${t.text}`)
          );
          if (matched) doneSet.add(t.id);
        } else if (t.type === 'exercise') {
          const tId = t.test_id ? String(t.test_id) : '';
          const tTitle = t.text ? t.text.trim().toLowerCase() : '';
          if ((tId && passedTestKeys.has(tId)) || (tTitle && passedTestKeys.has(tTitle))) {
            doneSet.add(t.id);
          }
        }
      });

      const done = Math.min(doneSet.size, total);
      totalTasksCount += total;
      completedTasksCount += done;

      if (total > 0 && done === total) {
        completedLecturesCount++;
        if (recentlyDoneLectures.length < 5) {
          recentlyDoneLectures.push({ id: lecId, title: lecTitle });
        }
      } else if (done > 0 && done < total) {
        inProgressLectures.push({
          id: lecId,
          title: lecTitle,
          done,
          total,
          moduleName: modName,
        });
      } else {
        const modKey = String(lec.module_id || 'default');
        const curModCount = nextUpPerModuleCount.get(modKey) || 0;
        if (curModCount < 2 && nextUpLectures.length < 10) {
          nextUpPerModuleCount.set(modKey, curModCount + 1);
          nextUpLectures.push({
            id: lecId,
            title: lecTitle,
            total: total || 1,
            moduleName: modName,
          });
        }
      }
    });

    // 3. Parse Activity Logs (Last Lecture Viewed & Library Reading Progress)
    const logs = (activityLogsRes.data || []) as any[];
    let lastLecture: GlobalStudentSnapshot['lastLecture'] = null;
    const camReadingSet = new Set<string>();
    const camListeningSet = new Set<string>();
    const recentLibraryTitles: string[] = [];

    logs.forEach((log) => {
      let d = log.details;
      if (typeof d === 'string') {
        try {
          d = JSON.parse(d);
        } catch {}
      }
      if (!lastLecture && (log.action_type === 'view_lecture' || log.action_type === 'finish_lecture')) {
        const lTitle = cleanTitle(d?.lecture_title || '');
        if (lTitle) {
          const matchedLec = sortedLectures.find(
            (l) => cleanTitle(l.title || '').toLowerCase() === lTitle.toLowerCase()
          );
          if (matchedLec) {
            lastLecture = {
              id: matchedLec.id,
              title: lTitle,
              timeLabel: formatShortDate(log.created_at),
            };
          }
        }
      }

      if (log.action_type === 'read_library') {
        const key = String(d?.news_id || d?.article_slug || d?.article_title || '');
        const title = cleanTitle(d?.article_title || '');
        const libType = String(d?.library_type || '');
        const parentCatId = Number(d?.parent_category_id || d?.category_id || 0);

        if (key) {
          if (libType === 'cambridge_reading_translation' || parentCatId === 38) {
            camReadingSet.add(key);
          } else if (libType === 'cambridge_listening_translation' || parentCatId === 87) {
            camListeningSet.add(key);
          }
        }
        if (title && recentLibraryTitles.length < 5 && !recentLibraryTitles.includes(title)) {
          recentLibraryTitles.push(title);
        }
      }
    });

    const taskPercent =
      totalTasksCount > 0 ? Math.round((completedTasksCount / totalTasksCount) * 100) : 0;

    // 4. Build Compact Prompt Context (~1,000 tokens) for Gemini AI
    const courseLecturesCatalog = sortedLectures
      .slice(0, 45)
      .map((l) => {
        const modName = moduleMap.get(String(l.module_id)) || '';
        return `- [${modName}] "${cleanTitle(l.title)}" -> ID: ${l.id}`;
      })
      .join('\n');

    const rootFoldersCatalog = rootFolders
      .slice(0, 20)
      .map((f) => `- Thư mục đề "${cleanTitle(f.title)}" -> FOLDER_ID: ${f.id}`)
      .join('\n');

    const recentTestsText =
      recentTests.length > 0
        ? recentTests
            .map(
              (t) =>
                `- [${t.dateLabel}] ${t.title} (${t.skill}): đạt ${t.scoreLabel}${
                  t.isLow ? ' (⚠️ Điểm còn thấp, cần củng cố)' : ' (✅ Tốt)'
                }`
            )
            .join('\n')
        : '- Chưa có bài kiểm tra nào gần đây.';

    const inProgressText =
      inProgressLectures.length > 0
        ? inProgressLectures
            .slice(0, 6)
            .map((l) => `- [${l.moduleName}] "${l.title}" (Đang làm dở: ${l.done}/${l.total} việc) -> ID: ${l.id}`)
            .join('\n')
        : '- Không có bài giảng nào đang bỏ dở.';

    const nextUpText =
      nextUpLectures.length > 0
        ? nextUpLectures
            .slice(0, 8)
            .map((l) => `- [${l.moduleName}] "${l.title}" (Chưa học: 0/${l.total} việc) -> ID: ${l.id}`)
            .join('\n')
        : '- Đã hoàn thành toàn bộ các bài giảng.';

    const skillSummaryText =
      Object.keys(skillSummary).length > 0
        ? Object.entries(skillSummary)
            .map(([k, v]) => `${k}: TB ${v.avgLabel} (${v.count} bài)`)
            .join(' | ')
        : 'Chưa đủ dữ liệu phân tích kỹ năng';

    const moduleNamesList = modules.map((m) => cleanTitle(m.title)).filter(Boolean).join(', ');
    const folderNamesList = rootFolders.map((f) => cleanTitle(f.title)).filter(Boolean).join(', ');

    const pedagogyRules = isIelts
      ? `[TRIẾT LÝ & QUY TẮC DẠY HỌC CỦA THẦY TONY - KHÓA IELTS PREMIUM]:
1. Thầy Tony luôn nhìn vào DỮ LIỆU THỰC TẾ của học sinh (bài đang làm dở trên Bảng công việc, điểm bài thi gần nhất, tiến độ đọc Bài dịch Cambridge trong Thư viện) để giao việc cụ thể ngay lập tức. Chỉ gọi học sinh bằng tên gọi ngắn ("${studentName}") hoặc "em", không lặp lại cả họ và tên đệm.
2. QUY TẮC TÍNH ĐIỂM BẮT BUỘC: Trong khóa IELTS Premium, CHỈ DUY NHẤT các đề thi trong thư mục "Cambridge Test" mới được chấm theo thang điểm Band (VD: Band 6.5). Tất cả các thư mục khác (Crash Course, Cram Course, Reading Strategies, Listening Strategies, bài tập theo Unit...) đều chỉ chấm theo tỷ lệ phần trăm số câu đúng (%), TUYỆT ĐỐI KHÔNG gọi điểm của các bài luyện tập đó là Band.
3. Nếu học sinh có bài giảng đang làm dở (VD: 1/5 việc, 2/7 việc) hoặc vừa mới hoàn thành 1 bài (VD: xong "1. Main Block: Person"), hãy khen ngợi và chỉ định học tiếp bài kế tiếp ngay sau đó (VD: "2. Main Block: Place/Service" hoặc bài tiếp theo trong Task 1/Task 2).
4. Với Kỹ năng Nghe (Listening) & Đọc (Reading):
   - Nếu điểm test thấp (< Band 6.0 đối với đề Cambridge, hoặc < 65% đối với các bài tập khác): Yêu cầu học lại bài giảng chiến thuật, luyện bộ đề Strategies (Listening Strategies / Reading Strategies / Crash Course), và BẮT BUỘC mở Thư viện đọc "Bài dịch đọc Cambridge IELTS" (/news/category/cambridge-ielts-reading-translation) hoặc "Bài dịch nghe Cambridge IELTS" (/news/category/cambridge-ielts-listening-translation).
   - Nhắc học sinh chỉ tiêu bắt buộc của khóa IELTS Premium: Đọc hiểu 252 bài dịch đọc Cambridge và 336 bài dịch nghe Cambridge trong Thư viện.
5. Với Kỹ năng Nói (Speaking): Học công thức Lego Blocks (6 Main Blocks + 3 Plugin Blocks) trong Bài giảng -> sau đó BẮT BUỘC vào Phòng luyện IELTS Speaking AI để ghi âm thực hành.
6. Với Kỹ năng Viết (Writing): Học công thức phân tích biểu đồ (Task 1) hoặc 5 dạng luận + 24 chủ đề từ vựng (Task 2) -> sau đó vào Phòng chấm IELTS Writing AI để nộp bài.`
      : isIgcse0654
      ? `[TRIẾT LÝ & QUY TẮC DẠY HỌC CỦA THẦY TONY - KHÓA IGCSE CO-ORDINATED SCIENCES 0654]:
1. Thầy Tony luôn kiểm tra xem học sinh đang học tới chương nào trong Biology (B1–B19), Chemistry (C1–C12), hay Physics (P1–P6) và điểm các bài Test/Past Paper gần nhất ra sao. Chỉ gọi học sinh bằng tên gọi ngắn ("${studentName}") hoặc "em".
2. Quy trình chuẩn cho mỗi chuyên đề:
   - Bước 1: Mở Bài giảng lý thuyết của chương đó (nghe Audio song ngữ Anh-Việt của Thầy AI + xem Video bài giảng).
   - Bước 2: Hoàn thành các bài tập trắc nghiệm & tự luận ngắn ở cuối bài giảng để đạt 100% tiến độ chương.
   - Bước 3: Luyện đề Past Paper trong Kho đề (Paper 2 Multiple Choice, Paper 4 Extended Theory, Paper 6 Alternative to Practical).`
      : `[TRIẾT LÝ & QUY TẮC DẠY HỌC CỦA THẦY TONY - KHÓA ${courseTitle.toUpperCase()}]:
1. Thầy Tony luôn kiểm tra sát sao tiến độ thực tế của học sinh trong khóa "${courseTitle}" (các học phần: ${moduleNamesList || 'theo giáo trình'}, các bài giảng đang làm dở trên Bảng công việc, bài giảng kế tiếp và kết quả các bài kiểm tra gần nhất trong Kho đề: ${folderNamesList || 'Kho đề luyện tập'}). Chỉ gọi học sinh bằng tên gọi ngắn ("${studentName}") hoặc "em", không lặp lại cả họ và tên đệm.
2. Tất cả các bài tập và đề kiểm tra trong khóa này đều được chấm theo tỷ lệ phần trăm (%). Nếu điểm bài kiểm tra gần nhất dưới 65%, hãy chỉ rõ chuyên đề cần củng cố và yêu cầu học sinh xem lại bài giảng lý thuyết tương ứng.
3. Quy trình học chuẩn cho mỗi bài / chuyên đề trong khóa "${courseTitle}":
   - Bước 1: Mở Bài giảng lý thuyết (OPEN_LECTURE) của bài đang làm dở hoặc bài kế tiếp để nghe giảng (Audio song ngữ / Video bài giảng) và nắm chắc kiến thức trọng tâm.
   - Bước 2: Hoàn thành đầy đủ các đầu việc & bài tập thực hành gắn liền với bài giảng đó trên Bảng công việc (OPEN_TAB:board) để đạt 100% tiến độ bài học.
   - Bước 3: Vào Thư mục Kho đề luyện tập (OPEN_FOLDER) tương ứng với chuyên đề vừa học để làm bài kiểm tra / Past Papers củng cố điểm số.`;

    const promptContext = `
====================================================================
HỒ SƠ HỌC TẬP TỔNG THỂ CỦA HỌC VIÊN (REAL-TIME STUDENT SNAPSHOT)
====================================================================
- Tên học viên: ${studentName}
- Khóa học đang mở: ${courseTitle}
- Tiến độ Bảng công việc toàn khóa: Hoàn thành ${completedTasksCount}/${totalTasksCount} đầu việc (${taskPercent}%), xong trọn vẹn ${completedLecturesCount}/${sortedLectures.length} bài giảng.
- Bài giảng vừa mở gần nhất trong khóa này: ${lastLecture ? `"${lastLecture.title}" (ngày ${lastLecture.timeLabel})` : 'Chưa ghi nhận'}
- Điểm trung bình theo kỹ năng: ${skillSummaryText}
${
  isIelts
    ? `- Tiến độ Thư viện Cambridge IELTS (Bắt buộc):
  + Bài dịch ĐỌC Cambridge IELTS đã đọc: ${camReadingSet.size} / 252 bài
  + Bài dịch NGHE Cambridge IELTS đã đọc: ${camListeningSet.size} / 336 bài
  + Tài liệu Thư viện vừa đọc gần đây: ${recentLibraryTitles.length > 0 ? recentLibraryTitles.join('; ') : 'Chưa đọc bài nào'}`
    : ''
}

[KẾT QUẢ CÁC BÀI TEST GẦN NHẤT]:
${recentTestsText}

[CÁC BÀI GIẢNG ĐANG LÀM DỞ TRÊN BẢNG CÔNG VIỆC (ƯU TIÊN HOÀN THÀNH)]:
${inProgressText}

[CÁC BÀI GIẢNG TIẾP THEO CẦN HỌC TRONG TỪNG CHUYÊN ĐỀ]:
${nextUpText}

${pedagogyRules}

====================================================================
BẢN ĐỒ TỔNG THỂ CÁC HỌC LIỆU & CÔNG CỤ TRÊN WEBSITE (DÙNG ĐỂ TẠO NÚT BẤM)
====================================================================
Khi tư vấn cho học sinh, BẮT BUỘC chèn trực tiếp các mã nút bấm hành động theo đúng cú pháp sau vào cuối mỗi bước hoặc cuối câu trả lời để học sinh bấm 1 click là nhảy thẳng tới nơi cần làm:

1. Mở trực tiếp 1 Bài giảng lý thuyết:
   Cú pháp: [[ACTION:OPEN_LECTURE:<ID_BÀI_GIẢNG>|📖 Mở bài: <Tên bài giảng>]]
   Danh sách ID bài giảng trong khóa:
${courseLecturesCatalog || '- Chưa có danh sách bài giảng'}

2. Mở trực tiếp 1 Thư mục Kho đề luyện tập:
   Cú pháp: [[ACTION:OPEN_FOLDER:<FOLDER_ID>|📂 Luyện đề: <Tên thư mục>]]
   Danh sách FOLDER_ID kho đề:
${rootFoldersCatalog || '- Chưa có thư mục kho đề'}
${
  isIelts
    ? `
3. Mở trực tiếp Thư viện Bài dịch & Bài mẫu:
   - Bài dịch đọc Cambridge IELTS (01-21): [[ACTION:OPEN_LIBRARY:/news/category/cambridge-ielts-reading-translation|📚 Mở Thư viện: Bài dịch đọc Cambridge]]
   - Bài dịch nghe Cambridge IELTS (01-21): [[ACTION:OPEN_LIBRARY:/news/category/cambridge-ielts-listening-translation|🎧 Mở Thư viện: Bài dịch nghe Cambridge]]
   - Bài mẫu IELTS Writing: [[ACTION:OPEN_LIBRARY:/news/category/ielts-writting-samples|✍️ Xem Thư viện Bài mẫu Writing]]
   - Bài mẫu IELTS Speaking: [[ACTION:OPEN_LIBRARY:/news/category/speaking-ielts-sample|🎙️ Xem Thư viện Bài mẫu Speaking]]

4. Mở Phòng Luyện & Chấm Điểm AI Thực Chiến:
   - Phòng luyện Speaking với Giám khảo AI: [[ACTION:OPEN_AI_ROOM:speaking|🎙️ Vào Phòng Luyện IELTS Speaking AI]]
   - Phòng chấm Writing Task 1 AI: [[ACTION:OPEN_AI_ROOM:task1|📊 Vào Phòng Chấm Writing Task 1 AI]]
   - Phòng chấm Writing Task 2 AI: [[ACTION:OPEN_AI_ROOM:task2|✍️ Vào Phòng Chấm Writing Task 2 AI]]`
    : ''
}

5. Mở Bảng công việc hoặc Báo cáo Tiến độ học:
   - Bảng công việc: [[ACTION:OPEN_TAB:board|📋 Mở Bảng Công Việc]]
   - Báo cáo Tiến độ học: [[ACTION:OPEN_TAB:analytics|📈 Xem Báo Cáo Tiến Độ Học]]
====================================================================
`.trim();

    const snapshot: GlobalStudentSnapshot = {
      userId: user.id,
      studentName,
      courseId: resolvedCourseId,
      courseTitle,
      isIelts,
      isIgcse0654,
      lastLecture,
      recentTests,
      taskProgress: {
        completedTasks: completedTasksCount,
        totalTasks: totalTasksCount,
        percent: taskPercent,
        completedLecturesCount,
        totalLecturesCount: sortedLectures.length,
        inProgressLectures,
        nextUpLectures,
        recentlyDoneLectures,
      },
      libraryProgress: {
        camReadingCount: camReadingSet.size,
        camListeningCount: camListeningSet.size,
        recentLibraryTitles,
      },
      skillSummary,
      promptContext,
      fetchedAt: Date.now(),
    };

    snapshotMemoryCache.set(cacheKey, snapshot);
    return snapshot;
  } catch (err) {
    console.error('[GlobalTutorContext] Error building student snapshot:', err);
    return null;
  }
}

export function parseTutorResponseWithActions(rawText: string): {
  cleanedText: string;
  actions: TutorActionItem[];
} {
  if (!rawText) return { cleanedText: '', actions: [] };

  const actions: TutorActionItem[] = [];
  const seenKeys = new Set<string>();

  const regex = /\[\[ACTION:(OPEN_LECTURE|OPEN_FOLDER|OPEN_LIBRARY|OPEN_AI_ROOM|OPEN_TAB):([^|\]]+)\|([^\]]+)\]\]/g;

  const cleanedText = rawText
    .replace(regex, (_match, typeRaw, targetRaw, labelRaw) => {
      const type = String(typeRaw).trim() as TutorActionItem['type'];
      const target = String(targetRaw).trim();
      const label = String(labelRaw).trim();
      const key = `${type}:${target}`;
      if (!seenKeys.has(key) && target && label) {
        seenKeys.add(key);
        actions.push({ type, target, label });
      }
      return '';
    })
    .replace(/\n{3,}/g, '\n\n')
    .trim();

  return { cleanedText, actions };
}

export function executeTutorAction(
  action: TutorActionItem,
  courseId?: string,
  callbacks?: {
    onOpenLecture?: (courseId: string, lectureId?: string) => void;
    onSelectFolder?: (folderId: string) => void;
    onNavigate?: (view: string) => void;
  }
) {
  const activeCourseId =
    courseId ||
    sessionStorage.getItem('lms_active_course_id') ||
    sessionStorage.getItem('portal_selected_course_id') ||
    '239a64f0-c106-40e5-a6e2-4e685a0d70fb';

  if (action.type === 'OPEN_LECTURE') {
    try {
      sessionStorage.setItem('lms_active_course_id', activeCourseId);
      sessionStorage.setItem('tony_target_lecture_id', action.target);
      sessionStorage.setItem(`tony_last_lec_${activeCourseId}`, action.target);
    } catch {}

    if (callbacks?.onOpenLecture) {
      callbacks.onOpenLecture(activeCourseId, action.target);
      return;
    }

    window.dispatchEvent(
      new CustomEvent('tony-select-lecture', {
        detail: { courseId: activeCourseId, lectureId: action.target },
      })
    );
    window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'lecture' }));
    return;
  }

  if (action.type === 'OPEN_FOLDER') {
    try {
      sessionStorage.setItem('portal_selected_course_id', activeCourseId);
      sessionStorage.setItem('portal_active_view', 'course');
      sessionStorage.setItem('portal_current_folder_id', action.target);
      sessionStorage.setItem('lms_portal_tab', 'library');
    } catch {}

    if (callbacks?.onSelectFolder) {
      callbacks.onSelectFolder(action.target);
      return;
    }

    window.dispatchEvent(
      new CustomEvent('tony-portal-open-folder', {
        detail: { courseId: activeCourseId, folderId: action.target },
      })
    );
    window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'portal' }));
    return;
  }

  if (action.type === 'OPEN_LIBRARY') {
    const path = action.target.startsWith('/') ? action.target : `/${action.target}`;
    window.history.pushState(null, '', path);
    if (callbacks?.onNavigate) {
      callbacks.onNavigate('home');
    } else {
      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'home' }));
    }
    return;
  }

  if (action.type === 'OPEN_AI_ROOM') {
    const room = action.target.toLowerCase();
    if (room === 'speaking') {
      if (callbacks?.onNavigate) callbacks.onNavigate('ielts-speaking');
      else window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'ielts-speaking' }));
    } else {
      try {
        sessionStorage.setItem('tony_writing_initial_tab', room === 'task1' ? '1' : '2');
      } catch {}
      if (callbacks?.onNavigate) callbacks.onNavigate('ielts-writing');
      else window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'ielts-writing' }));
    }
    return;
  }

  if (action.type === 'OPEN_TAB') {
    const tab = action.target.toLowerCase();
    try {
      sessionStorage.setItem('lms_portal_tab', tab);
    } catch {}
    window.dispatchEvent(new CustomEvent('tony-portal-switch-tab', { detail: tab }));
    if (callbacks?.onNavigate) {
      callbacks.onNavigate('portal');
    } else {
      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'portal' }));
    }
  }
}
