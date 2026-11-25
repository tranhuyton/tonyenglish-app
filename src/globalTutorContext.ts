import { supabase } from './supabase';
import { AppLang, getLmsLang, getLocalizedCourseTitle } from './utils/lmsI18n';

export interface TutorActionItem {
  type: 'OPEN_LECTURE' | 'OPEN_FOLDER' | 'OPEN_LIBRARY' | 'OPEN_AI_ROOM' | 'OPEN_TAB';
  target: string;
  label: string;
}

export interface DeadlineItem {
  id: string;
  title: string;
  dueDate: string;
  dueLabel: string;
  taskType: string;
  testId?: string | null;
  isCurrentCourse: boolean;
}

export type CourseFamily =
  | 'ielts'
  | 'sat'
  | 'igcse_0654'
  | 'igcse_subject'
  | 'comm_advanced'
  | 'comm_basic'
  | 'general';

export interface GlobalStudentSnapshot {
  userId: string;
  studentName: string;
  courseId: string;
  courseTitle: string;
  courseFamily: CourseFamily;
  isIelts: boolean;
  isSat: boolean;
  isIgcse0654: boolean;
  isIgcseSubject: boolean;
  isComm: boolean;
  lastLecture: {
    id?: string;
    title: string;
    timeLabel: string;
  } | null;
  deadlines: {
    overdue: DeadlineItem[];
    dueToday: DeadlineItem[];
    upcomingSoon: DeadlineItem[];
  };
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

export const extractStudentFirstName = (rawName?: string | null, lang?: AppLang): string => {
  const isEn = (lang || getLmsLang()) === 'en';
  const cleaned = (rawName || '').trim();
  if (!cleaned || cleaned.toLowerCase() === 'học viên' || cleaned.toLowerCase() === 'em' || cleaned.toLowerCase() === 'student') {
    return isEn ? 'there' : 'em';
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
const lectureCourseMap = new Map<string, string>();
const folderCourseMap = new Map<string, string>();

export const GRAMMAR_VOCAB_COURSE_ID = '8c3bea0e-458c-4c18-ab60-44b432e71170';

export function clearGlobalTutorCache() {
  snapshotMemoryCache.clear();
}

export async function fetchGlobalStudentSnapshot(
  courseIdInput?: string | null,
  courseTitleInput?: string | null,
  forceRefresh = false,
  langOverride?: AppLang
): Promise<GlobalStudentSnapshot | null> {
  try {
    const lang: AppLang = langOverride || getLmsLang();
    const isEn = lang === 'en';
    const { data: authData } = await supabase.auth.getUser();
    const user = authData?.user;
    if (!user) return null;

    const resolvedCourseId =
      courseIdInput ||
      sessionStorage.getItem('lms_active_course_id') ||
      sessionStorage.getItem('portal_selected_course_id') ||
      localStorage.getItem('portal_filter_course') ||
      '239a64f0-c106-40e5-a6e2-4e685a0d70fb';

    const cacheKey = `${user.id}_${resolvedCourseId}_${lang}`;
    const cached = snapshotMemoryCache.get(cacheKey);
    if (!forceRefresh && cached && Date.now() - cached.fetchedAt < 120_000) {
      return cached;
    }

    const targetCourseIds =
      resolvedCourseId && resolvedCourseId !== 'all'
        ? Array.from(new Set([resolvedCourseId, GRAMMAR_VOCAB_COURSE_ID]))
        : [];

    // Fetch student profile, course info, modules, lectures, folders, test results, assignments (with due_date), lecture_progress, activity_logs in parallel
    const [
      profileRes,
      courseRes,
      modulesRes,
      lecturesRes,
      foldersRes,
      testResultsRes,
      assignmentsRes,
      lectureProgRes,
      activityLogsRes,
    ] = await Promise.all([
      supabase.from('profiles').select('full_name, email').eq('id', user.id).maybeSingle(),
      resolvedCourseId && resolvedCourseId !== 'all'
        ? supabase.from('courses').select('id, title, type').eq('id', resolvedCourseId).maybeSingle()
        : Promise.resolve({ data: null }),
      targetCourseIds.length > 0
        ? supabase
            .from('lecture_modules')
            .select('id, title, order_index, course_id')
            .in('course_id', targetCourseIds)
            .order('order_index')
        : Promise.resolve({ data: [] }),
      targetCourseIds.length > 0
        ? supabase
            .from('lectures')
            .select('id, title, module_id, order_index, task_list, course_id')
            .in('course_id', targetCourseIds)
            .eq('is_published', true)
            .order('order_index')
        : Promise.resolve({ data: [] }),
      targetCourseIds.length > 0
        ? supabase
            .from('folders')
            .select('id, title, parent_id, course_id')
            .in('course_id', targetCourseIds)
        : Promise.resolve({ data: [] }),
      supabase
        .from('test_results')
        .select('id, test_title, score, total_score, details, created_at')
        .eq('user_id', user.id)
        .order('created_at', { ascending: false })
        .limit(80),
      supabase
        .from('assignments')
        .select('id, title, card_title, due_date, student_completed, is_completed, task_type, test_id')
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
      (isEn ? 'Student' : 'Học viên');
    const studentName = extractStudentFirstName(rawFullName, lang);

    const rawCourseTitle = cleanTitle(
      courseTitleInput || courseRes.data?.title || 'IELTS Premium'
    );
    const courseTitle = getLocalizedCourseTitle(rawCourseTitle, lang);
    const lowerCourseTitle = `${rawCourseTitle} ${courseRes.data?.type || ''}`.toLowerCase();
    const isIelts =
      resolvedCourseId === '239a64f0-c106-40e5-a6e2-4e685a0d70fb' ||
      lowerCourseTitle.includes('ielts');
    const isSat = !isIelts && lowerCourseTitle.includes('sat');
    const isIgcse0654 =
      resolvedCourseId === 'a2a949c7-c23e-45a7-82fa-cdeda5cc32a7' ||
      lowerCourseTitle.includes('co-ordinated') ||
      lowerCourseTitle.includes('0654');
    const isIgcseSubject =
      !isIelts &&
      !isSat &&
      !isIgcse0654 &&
      (lowerCourseTitle.includes('igcse') ||
        lowerCourseTitle.includes('a-level') ||
        lowerCourseTitle.includes('biology') ||
        lowerCourseTitle.includes('chemistry') ||
        lowerCourseTitle.includes('physics') ||
        lowerCourseTitle.includes('geography') ||
        lowerCourseTitle.includes('science') ||
        lowerCourseTitle.includes('0580') ||
        lowerCourseTitle.includes('0606') ||
        lowerCourseTitle.includes('math') ||
        lowerCourseTitle.includes('econ') ||
        lowerCourseTitle.includes('business'));
    const isCommAdvanced =
      !isIelts &&
      !isSat &&
      !isIgcse0654 &&
      !isIgcseSubject &&
      (lowerCourseTitle.includes('văn phòng') ||
        lowerCourseTitle.includes('thành ngữ') ||
        lowerCourseTitle.includes('idiom') ||
        lowerCourseTitle.includes('email') ||
        lowerCourseTitle.includes('phỏng vấn') ||
        lowerCourseTitle.includes('interview') ||
        lowerCourseTitle.includes('office'));
    const isCommBasic =
      !isIelts &&
      !isSat &&
      !isIgcse0654 &&
      !isIgcseSubject &&
      !isCommAdvanced &&
      (lowerCourseTitle.includes('pronunciation') ||
        lowerCourseTitle.includes('phát âm') ||
        lowerCourseTitle.includes('reflex') ||
        lowerCourseTitle.includes('phản ứng') ||
        lowerCourseTitle.includes('phản xạ') ||
        lowerCourseTitle.includes('tình huống') ||
        lowerCourseTitle.includes('communication') ||
        lowerCourseTitle.includes('giao tiếp'));
    const isComm = isCommAdvanced || isCommBasic;
    const courseFamily: CourseFamily = isIelts
      ? 'ielts'
      : isSat
      ? 'sat'
      : isIgcse0654
      ? 'igcse_0654'
      : isIgcseSubject
      ? 'igcse_subject'
      : isCommAdvanced
      ? 'comm_advanced'
      : isCommBasic
      ? 'comm_basic'
      : 'general';

    const allFetchedModules = (modulesRes.data || []) as any[];
    const allFetchedLectures = (lecturesRes.data || []) as any[];
    const allFetchedFolders = (foldersRes.data || []) as any[];

    // Targeted tests query (only tests belonging to active course + companion folders, instead of full table scan)
    const fetchedFolderIds = allFetchedFolders.map((f) => String(f.id)).filter(Boolean);
    const [testsByCourseRes, testsByFolderRes] = await Promise.all([
      targetCourseIds.length > 0
        ? supabase.from('tests').select('id, title, folder_id, course_id').in('course_id', targetCourseIds)
        : Promise.resolve({ data: [] }),
      fetchedFolderIds.length > 0
        ? supabase.from('tests').select('id, title, folder_id, course_id').in('folder_id', fetchedFolderIds.slice(0, 180))
        : Promise.resolve({ data: [] }),
    ]);
    const testsDedupMap = new Map<string, any>();
    [...(testsByCourseRes.data || []), ...(testsByFolderRes.data || [])].forEach((t: any) => {
      if (t?.id) testsDedupMap.set(String(t.id), t);
    });
    const courseTestsRes = { data: Array.from(testsDedupMap.values()) };

    allFetchedLectures.forEach((l) => {
      if (l.id && l.course_id) lectureCourseMap.set(String(l.id), String(l.course_id));
    });
    allFetchedFolders.forEach((f) => {
      if (f.id && f.course_id) folderCourseMap.set(String(f.id), String(f.course_id));
    });

    const modules = allFetchedModules.filter((m) => String(m.course_id) === String(resolvedCourseId));
    const moduleMap = new Map<string, string>();
    allFetchedModules.forEach((m) => moduleMap.set(String(m.id), cleanTitle(m.title || 'Học phần')));

    const lectures = allFetchedLectures.filter((l) => String(l.course_id) === String(resolvedCourseId));
    const folders = allFetchedFolders.filter((f) => String(f.course_id) === String(resolvedCourseId));
    const rootFolders = folders.filter((f) => !f.parent_id);
    const folderMap = new Map<string, { id: string; title: string; parent_id: string | null }>();
    folders.forEach((f) =>
      folderMap.set(String(f.id), {
        id: String(f.id),
        title: cleanTitle(f.title || ''),
        parent_id: f.parent_id ? String(f.parent_id) : null,
      })
    );

    // Companion "Grammar and Vocabulary" course data for IELTS Premium students
    const gvModules = allFetchedModules.filter((m) => String(m.course_id) === GRAMMAR_VOCAB_COURSE_ID);
    const gvLectures = allFetchedLectures.filter((l) => String(l.course_id) === GRAMMAR_VOCAB_COURSE_ID);
    const gvFolders = allFetchedFolders.filter((f) => String(f.course_id) === GRAMMAR_VOCAB_COURSE_ID);
    const gvFolderMap = new Map<string, { id: string; title: string; parent_id: string | null }>();
    gvFolders.forEach((f) =>
      gvFolderMap.set(String(f.id), {
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
      let skill = isEn ? 'General' : 'Tổng hợp';
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
          parts.push(isEn ? `Practice ${avgPct}%` : `Bài tập ${avgPct}%`);
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

    // 2b. Parse Study Calendar Deadlines (overdue / dueToday / upcomingSoon within 3 days)
    const nowLocal = new Date();
    const toLocalYMD = (dt: Date) =>
      `${dt.getFullYear()}-${String(dt.getMonth() + 1).padStart(2, '0')}-${String(dt.getDate()).padStart(2, '0')}`;
    const todayStr = toLocalYMD(nowLocal);
    const soonDate = new Date(nowLocal);
    soonDate.setDate(soonDate.getDate() + 3);
    const soonStr = toLocalYMD(soonDate);

    const activeLectureTitlesLower = new Set<string>(
      sortedLectures.map((l) => cleanTitle(l.title || '').toLowerCase()).filter(Boolean)
    );

    const overdueDeadlines: DeadlineItem[] = [];
    const dueTodayDeadlines: DeadlineItem[] = [];
    const upcomingSoonDeadlines: DeadlineItem[] = [];

    assignments
      .filter((a) => a.due_date && String(a.due_date).trim() !== '')
      .sort((a, b) => String(a.due_date).localeCompare(String(b.due_date)))
      .forEach((a) => {
        const dueClean = String(a.due_date).trim().split('T')[0];
        if (!/^\d{4}-\d{2}-\d{2}$/.test(dueClean)) return;

        const testKey = a.test_id ? String(a.test_id) : '';
        const titleLower = cleanTitle(a.title || '').toLowerCase();
        const cardLower = cleanTitle(a.card_title || '').toLowerCase();
        const isDone =
          a.task_type === 'test'
            ? Boolean(a.is_completed || (testKey && passedTestKeys.has(testKey)) || (titleLower && passedTestKeys.has(titleLower)))
            : Boolean(a.is_completed || a.student_completed);
        if (isDone) return;

        const isCurrentCourse =
          (testKey && courseTestIds.has(testKey)) ||
          (titleLower && courseTestTitles.has(titleLower)) ||
          (cardLower && activeLectureTitlesLower.has(cardLower)) ||
          (titleLower && activeLectureTitlesLower.has(titleLower));

        const parts = dueClean.split('-');
        const dueLabel = parts.length === 3 ? `${parts[2]}/${parts[1]}` : dueClean;
        const item: DeadlineItem = {
          id: String(a.id),
          title: cleanTitle(a.title || a.card_title || (isEn ? 'Study Task' : 'Nhiệm vụ học tập')),
          dueDate: dueClean,
          dueLabel,
          taskType: a.task_type || 'manual',
          testId: a.test_id || null,
          isCurrentCourse: Boolean(isCurrentCourse),
        };

        if (dueClean < todayStr) {
          overdueDeadlines.push(item);
        } else if (dueClean === todayStr) {
          dueTodayDeadlines.push(item);
        } else if (dueClean <= soonStr) {
          upcomingSoonDeadlines.push(item);
        }
      });

    // Prioritize current-course deadlines first while keeping urgent cross-course overdue items visible
    const sortDeadlinePriority = (arr: DeadlineItem[]) =>
      [...arr].sort((a, b) => {
        if (a.isCurrentCourse !== b.isCurrentCourse) return a.isCurrentCourse ? -1 : 1;
        return a.dueDate.localeCompare(b.dueDate);
      });

    const deadlines = {
      overdue: sortDeadlinePriority(overdueDeadlines).slice(0, 6),
      dueToday: sortDeadlinePriority(dueTodayDeadlines).slice(0, 6),
      upcomingSoon: sortDeadlinePriority(upcomingSoonDeadlines).slice(0, 6),
    };

    // 3b. Build Companion "Grammar and Vocabulary" Progress & Catalog for IELTS Premium
    let gvSummarySection = '';
    let gvCatalogSection = '';
    if (isIelts) {
      const gvModOrderMap = new Map<string, number>();
      gvModules.forEach((m, idx) => gvModOrderMap.set(String(m.id), m.order_index ?? idx));
      const gvSortedLectures = [...gvLectures].sort((a, b) => {
        const ma = gvModOrderMap.get(String(a.module_id)) ?? 999;
        const mb = gvModOrderMap.get(String(b.module_id)) ?? 999;
        if (ma !== mb) return ma - mb;
        return (a.order_index ?? 0) - (b.order_index ?? 0);
      });

      let gvDoneLectures = 0;
      const gvInProgOrNext: string[] = [];
      gvSortedLectures.forEach((lec) => {
        const lecId = String(lec.id);
        const lecTitle = cleanTitle(lec.title || 'Bài giảng');
        const modName = moduleMap.get(String(lec.module_id)) || 'Ngữ pháp';
        const taskList = Array.isArray(lec.task_list) ? lec.task_list : [];
        const total = taskList.length;
        const doneSet = progMap.get(lecId) || new Set<string>();
        const done = Math.min(doneSet.size, total);
        if (total > 0 && done >= total) {
          gvDoneLectures++;
        } else if (gvInProgOrNext.length < 6) {
          gvInProgOrNext.push(
            `- [${modName}] "${lecTitle}" (${done > 0 ? `Đang học dở ${done}/${total}` : 'Chưa học'}) -> ID: ${lecId}`
          );
        }
      });

      const gvTests = allTestsMeta.filter(
        (t) =>
          String(t.course_id) === GRAMMAR_VOCAB_COURSE_ID ||
          (t.folder_id && gvFolderMap.has(String(t.folder_id)))
      );
      const gvTestIds = new Set<string>(gvTests.map((t) => String(t.id)));
      const gvTestTitles = new Set<string>(
        gvTests.map((t) => cleanTitle(t.title || '').toLowerCase()).filter(Boolean)
      );
      const gvRecentTestLines: string[] = [];
      rawTestResults.forEach((r) => {
        if (gvRecentTestLines.length >= 4) return;
        let d = r.details;
        if (typeof d === 'string') {
          try {
            d = JSON.parse(d);
          } catch {}
        }
        const tId = d?.test_id ? String(d.test_id) : '';
        const tTitle = cleanTitle(r.test_title || d?.test_title || '');
        const lowerT = tTitle.toLowerCase();
        const score = parseFloat(r.score != null ? r.score : 0);
        const total = parseFloat(r.total_score != null ? r.total_score : 0);
        if (score <= 0) return;
        if ((tId && gvTestIds.has(tId)) || (lowerT && gvTestTitles.has(lowerT))) {
          const pct = total > 0 ? Math.round((score / total) * 100) : Math.round(score);
          gvRecentTestLines.push(
            `- [${formatShortDate(r.created_at)}] ${tTitle}: ${
              total > 0 ? `${score}/${total} (${pct}%)` : `${pct}%`
            }`
          );
        }
      });

      gvSummarySection = isEn
        ? `
[COMPANION FOUNDATION COURSE: GRAMMAR AND VOCABULARY]:
- Grammar lectures completed: ${gvDoneLectures}/${gvSortedLectures.length} lectures.
- Recommended next / in-progress grammar lectures:
${gvInProgOrNext.length > 0 ? gvInProgOrNext.join('\n') : '- Core grammar lectures completed.'}
- Recent Grammar & Vocabulary practice tests:
${gvRecentTestLines.length > 0 ? gvRecentTestLines.join('\n') : '- No recent exercises in Grammar and Vocabulary yet (proactively assign practice!).'}`
        : `
[KHÓA HỌC BỔ TRỢ NỀN TẢNG ĐI KÈM: GRAMMAR AND VOCABULARY]:
- Tiến độ bài giảng Ngữ pháp nền tảng: Hoàn thành ${gvDoneLectures}/${gvSortedLectures.length} bài giảng.
- Các bài giảng Ngữ pháp đang học dở / kế tiếp nên giao thêm:
${gvInProgOrNext.length > 0 ? gvInProgOrNext.join('\n') : '- Đã học xong các bài giảng ngữ pháp chính.'}
- Bài tập Từ vựng & Ngữ pháp vừa làm gần đây:
${gvRecentTestLines.length > 0 ? gvRecentTestLines.join('\n') : '- Chưa làm bài tập nào trong khóa Grammar and Vocabulary gần đây (Thầy cần chủ động sai học sinh vào làm thêm!).'}`;

      const gvFoldersCatalog = gvFolders
        .slice(0, 28)
        .map((f) => {
          const pTitle = f.parent_id ? gvFolderMap.get(String(f.parent_id))?.title : '';
          const label = pTitle ? `${pTitle} > ${cleanTitle(f.title)}` : cleanTitle(f.title);
          return `- ${isEn ? 'Grammar & Vocabulary Folder' : 'Thư mục Grammar & Vocabulary'} "${label}" -> FOLDER_ID: ${f.id}`;
        })
        .join('\n');

      const gvLecturesCatalog = gvSortedLectures
        .slice(0, 20)
        .map((l) => {
          const modName = moduleMap.get(String(l.module_id)) || 'Grammar';
          return `- [Grammar & Vocab - ${modName}] "${cleanTitle(l.title)}" -> ID: ${l.id}`;
        })
        .join('\n');

      gvCatalogSection = isEn
        ? `
2b. Open exercises & lectures in companion course "Grammar and Vocabulary" (to strengthen vocabulary & grammar):
   - Folder action syntax: [[ACTION:OPEN_FOLDER:<FOLDER_ID>|📂 Grammar & Vocab: <Folder Name>]]
${gvFoldersCatalog}
   - Lecture action syntax: [[ACTION:OPEN_LECTURE:<LECTURE_ID>|📖 Study Grammar: <Lecture Title>]]
${gvLecturesCatalog}`
        : `
2b. Mở trực tiếp Bài tập & Bài giảng trong khóa bổ trợ "Grammar and Vocabulary" (Dùng để sai học sinh IELTS Premium cày thêm Từ vựng & Ngữ pháp):
   - Khi giao bài tập Từ vựng / Ngữ pháp, dùng cú pháp: [[ACTION:OPEN_FOLDER:<FOLDER_ID>|📂 Bổ trợ Từ vựng/Ngữ pháp: <Tên thư mục>]]
${gvFoldersCatalog}
   - Khi giao bài giảng Ngữ pháp nền tảng, dùng cú pháp: [[ACTION:OPEN_LECTURE:<ID_BÀI_GIẢNG>|📖 Học Ngữ pháp: <Tên bài giảng>]]
${gvLecturesCatalog}`;
    }

    // 4. Build Prioritized Compact Prompt Context for Gemini AI (never truncating in-progress/next lectures on long courses!)
    const prioritizedLecturesMap = new Map<string, any>();
    const lectureById = new Map<string, any>();
    sortedLectures.forEach((l) => lectureById.set(String(l.id), l));

    inProgressLectures.forEach((ip) => {
      const l = lectureById.get(ip.id);
      if (l) prioritizedLecturesMap.set(ip.id, l);
    });
    nextUpLectures.forEach((nu) => {
      const l = lectureById.get(nu.id);
      if (l) prioritizedLecturesMap.set(nu.id, l);
    });
    sortedLectures.forEach((l) => {
      if (prioritizedLecturesMap.size < 60 && !prioritizedLecturesMap.has(String(l.id))) {
        prioritizedLecturesMap.set(String(l.id), l);
      }
    });

    const courseLecturesCatalog = Array.from(prioritizedLecturesMap.values())
      .map((l) => {
        const modName = moduleMap.get(String(l.module_id)) || '';
        return `- [${modName}] "${cleanTitle(l.title)}" -> ID: ${l.id}`;
      })
      .join('\n');

    // Include root folders AND key subfolders (Parent > Child) up to 32 entries so SAT/IGCSE specific papers are directly linkable
    const orderedFoldersForCatalog = [
      ...rootFolders,
      ...folders.filter((f) => Boolean(f.parent_id)),
    ].slice(0, 32);
    const rootFoldersCatalog = orderedFoldersForCatalog
      .map((f) => {
        const pTitle = f.parent_id ? folderMap.get(String(f.parent_id))?.title : '';
        const label = pTitle ? `${pTitle} > ${cleanTitle(f.title)}` : cleanTitle(f.title);
        return `- ${isEn ? 'Practice Folder' : 'Thư mục đề'} "${label}" -> FOLDER_ID: ${f.id}`;
      })
      .join('\n');

    const formatDeadlineLine = (d: DeadlineItem, tagVi: string, tagEn: string) =>
      `- [${isEn ? tagEn : tagVi} ${d.dueLabel}]${!d.isCurrentCourse ? (isEn ? ' [Other course]' : ' [Khóa khác]') : ''} ${d.title}`;

    const deadlinesLinesEn = [
      ...deadlines.overdue.map((d) => formatDeadlineLine(d, 'QUÁ HẠN', 'OVERDUE')),
      ...deadlines.dueToday.map((d) => formatDeadlineLine(d, 'HẠN HÔM NAY', 'DUE TODAY')),
      ...deadlines.upcomingSoon.map((d) => formatDeadlineLine(d, 'SẮP ĐẾN HẠN', 'UPCOMING')),
    ];
    const deadlinesSectionEn =
      deadlinesLinesEn.length > 0
        ? `\n[STUDY CALENDAR & URGENT DEADLINES (HIGHEST PRIORITY)]:\n${deadlinesLinesEn.join('\n')}`
        : '\n[STUDY CALENDAR & URGENT DEADLINES]:\n- No overdue or urgent deadlines in the next 3 days.';

    const deadlinesSectionVi =
      deadlinesLinesEn.length > 0
        ? `\n[LỊCH BÁO BÀI & DEADLINE CẦN ƯU TIÊN HÀNG ĐẦU]:\n${deadlinesLinesEn.join('\n')}`
        : '\n[LỊCH BÁO BÀI & DEADLINE]:\n- Không có bài quá hạn hay gấp trong 3 ngày tới.';

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
1. Thầy Tony luôn nhìn vào DỮ LIỆU THỰC TẾ của học sinh (bài QUÁ HẠN / ĐẾN HẠN trên Lịch báo bài, bài đang làm dở trên Bảng công việc, điểm bài thi gần nhất, tiến độ đọc Bài dịch Cambridge trong Thư viện) để giao việc cụ thể ngay lập tức. Nếu có bài quá hạn hoặc hạn hôm nay, BẮT BUỘC nhắc xử lý trước và đính kèm nút [[ACTION:OPEN_TAB:calendar|📅 Mở Lịch Báo Bài]]. Chỉ gọi học sinh bằng tên gọi ngắn ("${studentName}") hoặc "em", không lặp lại cả họ và tên đệm.
2. QUY TẮC TÍNH ĐIỂM BẮT BUỘC: Trong khóa IELTS Premium, CHỈ DUY NHẤT các đề thi trong thư mục "Cambridge Test" mới được chấm theo thang điểm Band (VD: Band 6.5). Tất cả các thư mục khác (Crash Course, Cram Course, Reading Strategies, Listening Strategies, bài tập theo Unit...) đều chỉ chấm theo tỷ lệ phần trăm số câu đúng (%), TUYỆT ĐỐI KHÔNG gọi điểm của các bài luyện tập đó là Band.
3. Nếu học sinh có bài giảng đang làm dở (VD: 1/5 việc, 2/7 việc) hoặc vừa mới hoàn thành 1 bài (VD: xong "1. Main Block: Person"), hãy khen ngợi và chỉ định học tiếp bài kế tiếp ngay sau đó (VD: "2. Main Block: Place/Service" hoặc bài tiếp theo trong Task 1/Task 2).
4. Với Kỹ năng Nghe (Listening) & Đọc (Reading):
   - Nếu điểm test thấp (< Band 6.0 đối với đề Cambridge, hoặc < 65% đối với các bài tập khác): Yêu cầu học lại bài giảng chiến thuật, luyện bộ đề Strategies (Listening Strategies / Reading Strategies / Crash Course), và BẮT BUỘC mở Thư viện đọc "Bài dịch đọc Cambridge IELTS" (/news/category/cambridge-ielts-reading-translation) hoặc "Bài dịch nghe Cambridge IELTS" (/news/category/cambridge-ielts-listening-translation).
   - Nhắc học sinh chỉ tiêu bắt buộc của khóa IELTS Premium: Đọc hiểu 252 bài dịch đọc Cambridge và 336 bài dịch nghe Cambridge trong Thư viện.
5. Với Kỹ năng Nói (Speaking): Học công thức Lego Blocks (6 Main Blocks + 3 Plugin Blocks) trong Bài giảng -> sau đó BẮT BUỘC vào Phòng luyện IELTS Speaking AI để ghi âm thực hành.
6. Với Kỹ năng Viết (Writing): Học công thức phân tích biểu đồ (Task 1) hoặc 5 dạng luận + 24 chủ đề từ vựng (Task 2) -> sau đó vào Phòng chấm IELTS Writing AI để nộp bài.
7. ĐẶC QUYỀN KHÓA IELTS PREMIUM — GIAO THÊM BÀI TẬP TRONG KHÓA "GRAMMAR AND VOCABULARY": Học sinh học khóa IELTS Premium luôn được Thầy Tony xếp học kèm khóa "Grammar and Vocabulary" để bồi đắp vốn từ vựng và nền tảng ngữ pháp. Vì vậy, khi tư vấn lộ trình học hôm nay hoặc khi thấy điểm Reading/Listening/Writing/Speaking của học sinh còn yếu, Thầy Tony AI BẮT BUỘC phải sai học sinh làm thêm bài tập trong khóa "Grammar and Vocabulary" (ví dụ: cày từ vựng trong "4000 English Words", "Vocabulary Organiser", "Expand Vocabulary Through Reading", hoặc làm bài tập ngữ pháp trong "Grammar" -> "I. Basic English Grammar exercises" / "II. English Tenses exercises" / "III. Advanced English Grammar exercises", hoặc học bài giảng Ngữ pháp tương ứng) và chèn sẵn nút bấm [[ACTION:OPEN_FOLDER:...]] hoặc [[ACTION:OPEN_LECTURE:...]] để học sinh bấm vào làm ngay!`
      : isSat
      ? `[TRIẾT LÝ & QUY TẮC DẠY HỌC CỦA THẦY TONY - KHÓA DIGITAL SAT 1500+]:
1. Thầy Tony huấn luyện học sinh theo đúng cấu trúc đề thi Digital SAT Bluebook thích ứng (Adaptive): gồm 2 phần **Reading & Writing (R&W — 71 giây/câu)** và **Math (1500+ — 95 giây/câu)**, với mục tiêu vượt qua Module 1 sạch lỗi để mở khóa Hard Module 2 chinh phục 750–800 điểm mỗi phần. Nếu có bài quá hạn / hạn hôm nay trên Lịch báo bài, nhắc hoàn thành ngay trước tiên.
2. Phân tích rõ từng mảng chuyên sâu:
   - **Reading & Writing:** Craft & Structure (Words in Context, Cross-Text), Information & Ideas (Inference, Command of Evidence), Standard English Conventions (Boundaries, Form/Structure/Sense), Expression of Ideas (Transitions, Rhetorical Synthesis).
   - **Math 1500+:** Algebra, Advanced Math, Problem-Solving & Data Analysis, Geometry & Trig — luôn gợi ý mẹo giải nhanh bằng máy tính **Desmos** cho các câu hệ phương trình, hàm bậc hai, hồi quy.
   - **Chốt điểm cao:** Khi nền tảng vững (>80% ở bài luyện theo chuyên đề), giao ngay bộ **Hard M2 Boss Drills (120 Câu Trùm Cuối 750–800)** và **Real Past Exams (2024–2025)** trong Kho đề (kèm nút [[ACTION:OPEN_FOLDER:...]]).`
      : isIgcse0654
      ? `[TRIẾT LÝ & QUY TẮC DẠY HỌC CỦA THẦY TONY - KHÓA IGCSE CO-ORDINATED SCIENCES 0654]:
1. Thầy Tony luôn kiểm tra bài quá hạn/hạn hôm nay trên Lịch báo bài, xem học sinh đang học tới chương nào trong Biology (B1–B19), Chemistry (C1–C12), hay Physics (P1–P6) và điểm các bài Test/Past Paper gần nhất ra sao. Chỉ gọi học sinh bằng tên gọi ngắn ("${studentName}") hoặc "em".
2. Quy trình chuẩn chuẩn Cambridge Marking Scheme cho mỗi chuyên đề:
   - Bước 1: Mở Bài giảng lý thuyết của chương đó (nghe Audio song ngữ Anh-Việt của Thầy AI + nắm chắc từ khóa ăn điểm theo Command Words: State, Describe, Explain, Calculate).
   - Bước 2: Hoàn thành các bài tập trắc nghiệm & tự luận ngắn ở cuối bài giảng để đạt 100% tiến độ chương.
   - Bước 3: Luyện đề Past Paper trong Kho đề (Paper 2 Multiple Choice, Paper 4 Extended Theory, Paper 6 Alternative to Practical).`
      : isIgcseSubject
      ? `[TRIẾT LÝ & QUY TẮC DẠY HỌC CỦA THẦY TONY - KHÓA CAMBRIDGE ${courseTitle.toUpperCase()}]:
1. Thầy Tony bám sát đề cương Cambridge IGCSE/A-Level chính thức của môn "${courseTitle}" (các học phần: ${moduleNamesList || 'theo Syllabus'}, Kho đề: ${folderNamesList || 'Topical & Past Papers'}). Nếu có bài quá hạn / hạn hôm nay trên Lịch báo bài, ưu tiên nhắc xử lý trước.
2. Nhấn mạnh chiến thuật đạt điểm **A / A*** theo Marking Scheme thực tế: học kỹ Command Words (**State / Define / Describe / Explain / Analyse / Evaluate / Calculate**), trình bày đủ ý theo số điểm (VD: câu 4 marks cần đủ 4 ý ăn điểm / câu tính toán phải ghi công thức + đơn vị).
3. Quy trình 3 bước chuẩn: (1) Học bài giảng song ngữ (OPEN_LECTURE) -> (2) Làm sạch checklist & mini-quiz trên Bảng công việc -> (3) Luyện bộ đề Topical / Past Papers (Paper 1/2 MCQ, Paper 4 Extended / Structured / Case Study, Paper 6 ATP nếu có) qua nút OPEN_FOLDER.`
      : isComm
      ? `[TRIẾT LÝ & QUY TẮC DẠY HỌC CỦA THẦY TONY - KHÓA ${courseTitle.toUpperCase()}]:
1. Với khóa học thực chiến "${courseTitle}" (các chuyên đề: ${moduleNamesList || 'giao tiếp thực tế'}), Thầy Tony ưu tiên tính **ứng dụng ngay lập tức** vào công việc & đời sống thay vì học vẹt lý thuyết. Nếu có bài quá hạn / hạn hôm nay trên Lịch báo bài, nhắc hoàn thành trước.
2. Sau khi giao bài giảng (OPEN_LECTURE) và bài thực hành trong Kho đề (OPEN_FOLDER), Thầy chủ động khuyến khích học viên **thực hành đóng vai (roleplay) / viết nháp Email / trả lời câu hỏi phỏng vấn theo cấu trúc STAR / đặt câu với Thành ngữ** ngay trong khung chat này để Thầy sửa câu tự nhiên như người bản xứ (British/International Business English).`
      : `[TRIẾT LÝ & QUY TẮC DẠY HỌC CỦA THẦY TONY - KHÓA ${courseTitle.toUpperCase()}]:
1. Thầy Tony luôn kiểm tra sát sao tiến độ thực tế của học sinh trong khóa "${courseTitle}" (bài quá hạn/hạn hôm nay trên Lịch báo bài, các học phần: ${moduleNamesList || 'theo giáo trình'}, các bài giảng đang làm dở trên Bảng công việc, bài giảng kế tiếp và kết quả các bài kiểm tra gần nhất trong Kho đề: ${folderNamesList || 'Kho đề luyện tập'}). Chỉ gọi học sinh bằng tên gọi ngắn ("${studentName}") hoặc "em", không lặp lại cả họ và tên đệm.
2. Tất cả các bài tập và đề kiểm tra trong khóa này đều được chấm theo tỷ lệ phần trăm (%). Nếu điểm bài kiểm tra gần nhất dưới 65%, hãy chỉ rõ chuyên đề cần củng cố và yêu cầu học sinh xem lại bài giảng lý thuyết tương ứng.
3. Quy trình học chuẩn cho mỗi bài / chuyên đề trong khóa "${courseTitle}":
   - Bước 1: Mở Bài giảng lý thuyết (OPEN_LECTURE) của bài đang làm dở hoặc bài kế tiếp để nghe giảng (Audio song ngữ / Video bài giảng) và nắm chắc kiến thức trọng tâm.
   - Bước 2: Hoàn thành đầy đủ các đầu việc & bài tập thực hành gắn liền với bài giảng đó trên Bảng công việc (OPEN_TAB:board) để đạt 100% tiến độ bài học.
   - Bước 3: Vào Thư mục Kho đề luyện tập (OPEN_FOLDER) tương ứng với chuyên đề vừa học để làm bài kiểm tra củng cố điểm số.`;

    const promptContext = isEn
      ? `
====================================================================
[STRICT LANGUAGE RULE]: The student is using the ENGLISH interface.
You MUST write your ENTIRE response, greeting, analysis, coaching advice, AND ALL [[ACTION:...|Button Label]] labels in natural, warm, encouraging ENGLISH (unless the student explicitly requests Vietnamese).
Address yourself as "Teacher Tony" / "I" and address the student by first name ("${studentName}") or "you".
====================================================================
REAL-TIME STUDENT LEARNING SNAPSHOT
====================================================================
- Student Name: ${studentName}
- Active Course: ${courseTitle}
- Overall Task Board Progress: ${completedTasksCount}/${totalTasksCount} tasks completed (${taskPercent}%), ${completedLecturesCount}/${sortedLectures.length} lectures fully completed.
- Most Recently Viewed Lecture: ${lastLecture ? `"${lastLecture.title}" (${lastLecture.timeLabel})` : 'None recorded yet'}
- Skill Performance Summary: ${skillSummaryText}
${
  isIelts
    ? `- Cambridge IELTS Library Progress (Mandatory):
  + Cambridge Reading Translations read: ${camReadingSet.size} / 252 passages
  + Cambridge Listening Translations read: ${camListeningSet.size} / 336 sections
  + Recently read Library items: ${recentLibraryTitles.length > 0 ? recentLibraryTitles.join('; ') : 'None yet'}`
    : ''
}

${deadlinesSectionEn}

[RECENT TEST RESULTS]:
${
  recentTests.length > 0
    ? recentTests
        .map(
          (t) =>
            `- [${t.dateLabel}] ${t.title} (${t.skill}): ${t.scoreLabel}${
              t.isLow ? ' (⚠️ Needs reinforcement)' : ' (✅ Good)'
            }`
        )
        .join('\n')
    : '- No recent test attempts yet.'
}

[IN-PROGRESS LECTURES ON TASK BOARD (PRIORITY TO FINISH)]:
${
  inProgressLectures.length > 0
    ? inProgressLectures
        .slice(0, 6)
        .map((l) => `- [${l.moduleName}] "${l.title}" (In progress: ${l.done}/${l.total} tasks) -> ID: ${l.id}`)
        .join('\n')
    : '- No unfinished in-progress lectures.'
}

[NEXT UP LECTURES BY MODULE]:
${
  nextUpLectures.length > 0
    ? nextUpLectures
        .slice(0, 8)
        .map((l) => `- [${l.moduleName}] "${l.title}" (Not started: 0/${l.total} tasks) -> ID: ${l.id}`)
        .join('\n')
    : '- All course lectures completed!'
}
${gvSummarySection}

[TEACHER TONY'S COACHING RULES FOR ${courseTitle.toUpperCase()}]:
${
  isIelts
    ? `1. Base every recommendation directly on ${studentName}'s real data above (overdue/today Study Calendar deadlines first, unfinished lectures, recent test scores, Cambridge Library progress, and companion "Grammar and Vocabulary" course). If overdue or due-today tasks exist, highlight them first with [[ACTION:OPEN_TAB:calendar|📅 Open Study Calendar]].
2. SCORING RULE: Only tests inside the "Cambridge Test" folder are graded on the IELTS Band scale (e.g., Band 6.5). All other practice folders (Crash Course, Cram Course, Strategies, Unit exercises) are graded by percentage (%) — NEVER call those scores a Band score.
3. For Listening & Reading: if scores are low (< Band 6.0 on Cambridge or < 65% on drills), assign strategy lectures, strategy drills, and Cambridge Library reading/listening translations.
4. For Speaking: follow the Lego Blocks method in Lectures -> then practice in the IELTS Speaking AI Room.
5. For Writing: review Task 1 chart analysis / Task 2 5 essay types & 24 topic packs -> then submit in the IELTS Writing AI Grader.
6. COMPANION COURSE ("Grammar and Vocabulary"): IELTS Premium students also study "Grammar and Vocabulary" to strengthen vocabulary & grammar. Proactively assign matching folders/lectures from Grammar and Vocabulary with clickable [[ACTION:...]] buttons.`
    : isSat
    ? `1. Coach ${studentName} for the adaptive Digital SAT Bluebook format (Reading & Writing ~71s/question; Math 1500+ ~95s/question) aiming to clear Module 1 cleanly and unlock Hard Module 2 for 750–800 scores. Prioritize any overdue/today deadlines first.
2. Reading & Writing focus: Craft & Structure, Information & Ideas, Standard English Conventions, Expression of Ideas. Math focus: Algebra, Advanced Math, Problem-Solving & Data Analysis, Geometry & Trig (recommend Desmos graphing shortcuts where helpful).
3. Once core drills exceed 80%, assign Hard M2 Boss Drills and Real Past Exams (2024–2025) with direct [[ACTION:OPEN_FOLDER:...]] buttons.`
    : isIgcse0654
    ? `1. Check urgent Study Calendar deadlines first, then see which Biology (B1–B19), Chemistry (C1–C12), or Physics (P1–P6) topics ${studentName} is working on and review recent test/past-paper results.
2. Standard Cambridge Marking Scheme workflow per topic: (1) Study theory lecture & command-word keywords -> (2) Complete lecture checklist tasks -> (3) Practice Past Papers (Paper 2 MCQ, Paper 4 Extended Theory, Paper 6 Alternative to Practical).`
    : isIgcseSubject
    ? `1. Check urgent Study Calendar deadlines first, then align with the official Cambridge syllabus for "${courseTitle}" (modules: ${moduleNamesList || 'curriculum'}; test folders: ${folderNamesList || 'Past Papers'}).
2. Coach for A / A* marks using official Cambridge command words (State, Define, Describe, Explain, Analyse, Evaluate, Calculate) and full marking-scheme points.
3. Standard workflow: (1) Theory lecture (OPEN_LECTURE) -> (2) Task Board checklist -> (3) Topical & Past Paper practice (OPEN_FOLDER).`
    : isComm
    ? `1. Check any urgent deadlines first, then focus on practical, immediate real-world communication in "${courseTitle}" (modules: ${moduleNamesList || 'communication topics'}).
2. After assigning the next lecture (OPEN_LECTURE) and practice folder (OPEN_FOLDER), actively invite ${studentName} to practice live right in this chat (roleplay dialogue, mock STAR interview Q&A, business email critique, or natural idiom sentences) so you can polish their English like a native coach.`
    : `1. Check urgent Study Calendar deadlines first, then review ${studentName}'s real progress in "${courseTitle}" (modules: ${moduleNamesList || 'curriculum'}, in-progress/next lectures, and recent practice test folders: ${folderNamesList || 'Test Bank'}).
2. All quizzes/tests in this course are graded by percentage (%). If a recent test is below 65%, point out the weak topic and recommend reviewing the matching theory lecture.
3. Standard workflow: (1) Study the theory lecture (OPEN_LECTURE) -> (2) Complete all checklist items on the Task Board (OPEN_TAB:board) -> (3) Practice in the matching Test Bank folder (OPEN_FOLDER).`
}

====================================================================
COURSE CATALOG & CLICKABLE ACTION BUTTONS (USE ENGLISH LABELS!)
====================================================================
Always append 1–4 clickable action tags using this exact syntax (with English button labels):

1. Open a Theory Lecture directly:
   Syntax: [[ACTION:OPEN_LECTURE:<LECTURE_ID>|📖 Open Lesson: <Lecture Title>]]
   Course Lecture IDs:
${courseLecturesCatalog || '- No lecture list available'}

2. Open a Test Bank Folder directly:
   Syntax: [[ACTION:OPEN_FOLDER:<FOLDER_ID>|📂 Practice: <Folder Name>]]
   Course Folder IDs:
${rootFoldersCatalog || '- No test folders available'}
${gvCatalogSection}
${
  isIelts
    ? `
3. Open Library Resources directly:
   - Cambridge IELTS Reading Translations (01-21): [[ACTION:OPEN_LIBRARY:/news/category/cambridge-ielts-reading-translation|📚 Open Library: Cambridge Reading]]
   - Cambridge IELTS Listening Translations (01-21): [[ACTION:OPEN_LIBRARY:/news/category/cambridge-ielts-listening-translation|🎧 Open Library: Cambridge Listening]]
   - IELTS Writing Samples: [[ACTION:OPEN_LIBRARY:/news/category/ielts-writting-samples|✍️ View Writing Samples]]
   - IELTS Speaking Samples: [[ACTION:OPEN_LIBRARY:/news/category/speaking-ielts-sample|🎙️ View Speaking Samples]]

4. Open AI Practice & Grading Rooms:
   - IELTS Speaking AI Room: [[ACTION:OPEN_AI_ROOM:speaking|🎙️ Open IELTS Speaking AI Room]]
   - IELTS Writing Task 1 AI Grader: [[ACTION:OPEN_AI_ROOM:task1|📊 Open Writing Task 1 AI Grader]]
   - IELTS Writing Task 2 AI Grader: [[ACTION:OPEN_AI_ROOM:task2|✍️ Open Writing Task 2 AI Grader]]`
    : ''
}

5. Open Study Calendar, Task Board, or Progress Analytics:
   - Study Calendar (Deadlines): [[ACTION:OPEN_TAB:calendar|📅 Open Study Calendar]]
   - Task Board: [[ACTION:OPEN_TAB:board|📋 Open Task Board]]
   - Progress Report: [[ACTION:OPEN_TAB:analytics|📈 View Progress Report]]
====================================================================
`.trim()
      : `
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
${deadlinesSectionVi}

[KẾT QUẢ CÁC BÀI TEST GẦN NHẤT]:
${recentTestsText}

[CÁC BÀI GIẢNG ĐANG LÀM DỞ TRÊN BẢNG CÔNG VIỆC (ƯU TIÊN HOÀN THÀNH)]:
${inProgressText}

[CÁC BÀI GIẢNG TIẾP THEO CẦN HỌC TRONG TỪNG CHUYÊN ĐỀ]:
${nextUpText}
${gvSummarySection}

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
${gvCatalogSection}
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

5. Mở Lịch báo bài, Bảng công việc hoặc Báo cáo Tiến độ học:
   - Lịch báo bài (Deadline): [[ACTION:OPEN_TAB:calendar|📅 Mở Lịch Báo Bài]]
   - Bảng công việc: [[ACTION:OPEN_TAB:board|📋 Mở Bảng Công Việc]]
   - Báo cáo Tiến độ học: [[ACTION:OPEN_TAB:analytics|📈 Xem Báo Cáo Tiến Độ Học]]
====================================================================
`.trim();

    const snapshot: GlobalStudentSnapshot = {
      userId: user.id,
      studentName,
      courseId: resolvedCourseId,
      courseTitle,
      courseFamily,
      isIelts,
      isSat,
      isIgcse0654,
      isIgcseSubject,
      isComm,
      lastLecture,
      deadlines,
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
    onSelectFolder?: (folderId: string, targetCourseId?: string) => void;
    onNavigate?: (view: string) => void;
  }
) {
  const activeCourseId =
    courseId ||
    sessionStorage.getItem('lms_active_course_id') ||
    sessionStorage.getItem('portal_selected_course_id') ||
    '239a64f0-c106-40e5-a6e2-4e685a0d70fb';

  if (action.type === 'OPEN_LECTURE') {
    const resolvedLecCourseId = lectureCourseMap.get(action.target) || activeCourseId;
    try {
      sessionStorage.setItem('lms_active_course_id', resolvedLecCourseId);
      localStorage.setItem('lms_active_course_id', resolvedLecCourseId);
      sessionStorage.setItem('tony_target_lecture_id', action.target);
      sessionStorage.setItem(`tony_last_lec_${resolvedLecCourseId}`, action.target);
    } catch {}

    if (callbacks?.onOpenLecture) {
      callbacks.onOpenLecture(resolvedLecCourseId, action.target);
      return;
    }

    window.dispatchEvent(
      new CustomEvent('tony-select-lecture', {
        detail: { courseId: resolvedLecCourseId, lectureId: action.target },
      })
    );
    window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'lecture' }));
    return;
  }

  if (action.type === 'OPEN_FOLDER') {
    const resolvedFolderCourseId = folderCourseMap.get(action.target) || activeCourseId;
    try {
      sessionStorage.setItem('portal_selected_course_id', resolvedFolderCourseId);
      localStorage.setItem('portal_filter_course', resolvedFolderCourseId);
      sessionStorage.setItem('portal_active_view', 'course');
      sessionStorage.setItem('portal_current_folder_id', action.target);
      sessionStorage.setItem('lms_portal_tab', 'library');
    } catch {}

    if (callbacks?.onSelectFolder) {
      callbacks.onSelectFolder(action.target, resolvedFolderCourseId);
      return;
    }

    window.dispatchEvent(
      new CustomEvent('tony-portal-open-folder', {
        detail: { courseId: resolvedFolderCourseId, folderId: action.target },
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
