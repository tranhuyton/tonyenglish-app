import { supabase } from './supabase';
import { parseModuleTheme } from './moduleTheme';
import { formatLectureTaskDescription } from './lectureTaskUtils';

export interface SyncBoardResult {
  addedBoardItems: number;
  updatedBoardItems: number;
  addedDayPlanTasks: number;
  updatedDayPlanTasks: number;
  syncedUsersCount: number;
  addedUserAssignments: number;
  updatedUserAssignments: number;
}

async function fetchAllPaginated<T = any>(
  buildQuery: (from: number, to: number) => PromiseLike<{ data: T[] | null; error: any }>
): Promise<{ data: T[]; error: any }> {
  const allRows: T[] = [];
  const pageSize = 1000;
  let from = 0;
  while (true) {
    const { data, error } = await buildQuery(from, from + pageSize - 1);
    if (error) return { data: allRows, error };
    if (!data || data.length === 0) break;
    allRows.push(...data);
    if (data.length < pageSize) break;
    from += pageSize;
  }
  return { data: allRows, error: null };
}

/**
 * Resolves the primary active `board_templates` record for a given course.
 */
export async function resolveActiveBoardTemplateForCourse(
  courseId: string,
  explicitBoardTemplateId?: string
): Promise<{ id: string; title: string; course_id: string; is_active?: boolean } | null> {
  if (!courseId && !explicitBoardTemplateId) return null;
  let query = supabase.from('board_templates').select('id, title, course_id, is_active, created_at');
  if (explicitBoardTemplateId) {
    query = query.eq('id', explicitBoardTemplateId);
  } else {
    query = query.eq('course_id', courseId).order('is_active', { ascending: false }).order('created_at', { ascending: true });
  }
  const { data } = await query.limit(1);
  return data && data.length > 0 ? data[0] : null;
}

function extractLeadingNumber(text: string): number | null {
  const clean = parseModuleTheme(text || '').cleanTitle.trim();
  const secMatch = clean.match(/^(?:section|topic|unit|chapter|module)\s*(\d+)\b/i);
  if (secMatch) return parseInt(secMatch[1], 10);
  const numMatch = clean.match(/^(\d+)(?:\.\d+)?\b/);
  if (numMatch) return parseInt(numMatch[1], 10);
  return null;
}

function sortLectureExerciseTasks(exTasks: any[], testsById: Map<string, any>): any[] {
  return [...exTasks].sort((a, b) => {
    const titleA = (testsById.get(String(a.test_id))?.title || a.text || '').replace(/^Làm bài tập:\s*/i, '').trim();
    const titleB = (testsById.get(String(b.test_id))?.title || b.text || '').replace(/^Làm bài tập:\s*/i, '').trim();
    const numA = parseInt((titleA.match(/^(\d+)(?:\.(\d+))?/) || [])[1] || '9999', 10);
    const subA = parseInt((titleA.match(/^(\d+)(?:\.(\d+))?/) || [])[2] || '0', 10);
    const numB = parseInt((titleB.match(/^(\d+)(?:\.(\d+))?/) || [])[1] || '9999', 10);
    const subB = parseInt((titleB.match(/^(\d+)(?:\.(\d+))?/) || [])[2] || '0', 10);
    if (numA !== numB) return numA - numB;
    if (subA !== subB) return subA - subB;
    const isQuizA = /\bquiz(?:zes)?\b/i.test(titleA) ? 1 : 0;
    const isQuizB = /\bquiz(?:zes)?\b/i.test(titleB) ? 1 : 0;
    return isQuizA - isQuizB;
  });
}

/**
 * Non-destructively syncs a board template's current columns/cards/items to a single user's `assignments`
 * without wiping existing `student_completed`, `is_completed`, `admin_approved`, or `due_date`.
 */
export async function syncBoardTemplateToSingleUser(
  boardTemplateId: string,
  userId: string
): Promise<{ added: number; updated: number; total: number; error?: string | null }> {
  const { data: tpl } = await supabase
    .from('board_templates')
    .select('id, title, course_id')
    .eq('id', boardTemplateId)
    .maybeSingle();
  if (!tpl) return { added: 0, updated: 0, total: 0, error: null };

  const { data: cols } = await supabase
    .from('board_columns')
    .select('*')
    .eq('board_template_id', boardTemplateId)
    .order('order_index');
  const colList = cols || [];
  if (colList.length === 0) return { added: 0, updated: 0, total: 0, error: null };

  const colIds = colList.map(c => c.id);
  const { data: cardList } = await fetchAllPaginated((from, to) =>
    supabase.from('board_cards').select('*').in('column_id', colIds).order('order_index').order('id').range(from, to)
  );
  const cardIds = cardList.map(c => c.id);
  const { data: itemList } = cardIds.length > 0
    ? await fetchAllPaginated((from, to) =>
        supabase.from('board_card_items').select('*').in('card_id', cardIds).order('order_index').order('id').range(from, to)
      )
    : { data: [] };

  const { data: existingRows } = await fetchAllPaginated((from, to) =>
    supabase.from('assignments').select('*').eq('user_id', userId).order('id').range(from, to)
  );

  const boardExisting = (existingRows || []).filter(
    r => r.board_template_id === boardTemplateId || r.board_template_title === tpl.title
  );

  const usedAssignmentIds = new Set<string>();
  const toInsert: any[] = [];
  const toUpdate: { id: string; payload: any }[] = [];

  for (const col of colList) {
    const colCards = cardList.filter(c => c.column_id === col.id);
    for (const card of colCards) {
      const cardItems = itemList.filter(i => i.card_id === card.id);
      for (const item of cardItems) {
        const match = boardExisting.find(ex => {
          if (usedAssignmentIds.has(ex.id)) return false;
          if (item.task_type === 'test' && item.test_id) {
            return String(ex.test_id || '') === String(item.test_id) &&
              (ex.card_title === card.title || !ex.card_title);
          }
          return (
            ex.task_type === item.task_type &&
            ex.card_title === card.title &&
            (ex.title || '').trim() === (item.title || '').trim()
          );
        });

        const desiredDesc = item.description || '';
        const desiredOrder = item.order_index || 0;
        const desiredCardOrder = card.order_index || 0;

        if (match) {
          usedAssignmentIds.add(match.id);
          const needsUpdate =
            (match.order_index || 0) !== desiredOrder ||
            (match.card_order || 0) !== desiredCardOrder ||
            (match.category || '') !== col.title ||
            (match.card_title || '') !== card.title ||
            (match.description || '') !== desiredDesc ||
            match.board_template_id !== boardTemplateId ||
            match.board_template_title !== tpl.title;

          if (needsUpdate) {
            toUpdate.push({
              id: match.id,
              payload: {
                category: col.title,
                card_title: card.title,
                card_order: desiredCardOrder,
                order_index: desiredOrder,
                description: desiredDesc,
                board_template_id: boardTemplateId,
                board_template_title: tpl.title
              }
            });
          }
        } else {
          toInsert.push({
            user_id: userId,
            title: item.title,
            description: desiredDesc,
            task_type: item.task_type,
            test_id: item.test_id || null,
            category: col.title,
            card_title: card.title,
            card_order: desiredCardOrder,
            order_index: desiredOrder,
            due_date: null,
            board_template_id: boardTemplateId,
            board_template_title: tpl.title
          });
        }
      }
    }
  }

  let firstError: string | null = null;
  let updatedOk = 0;
  for (const upd of toUpdate) {
    const { error } = await supabase.from('assignments').update(upd.payload).eq('id', upd.id);
    if (error) {
      if (!firstError) firstError = error.message;
    } else {
      updatedOk++;
    }
  }

  let addedOk = 0;
  const chunkSize = 100;
  for (let i = 0; i < toInsert.length; i += chunkSize) {
    const slice = toInsert.slice(i, i + chunkSize);
    const { error } = await supabase.from('assignments').insert(slice);
    if (error) {
      if (!firstError) firstError = error.message;
      break;
    }
    addedOk += slice.length;
  }

  return {
    added: addedOk,
    updated: updatedOk,
    total: itemList.length,
    error: firstError
  };
}

/**
 * Ensures a student has the active board template of `courseId` assigned in `assignments`.
 * Safe & idempotent: never duplicates items or overwrites completion status.
 */
export async function ensureCourseBoardAssignedToUser(
  courseId: string,
  userId: string,
  options?: { forceSync?: boolean; explicitBoardTemplateId?: string }
): Promise<{
  boardTemplateId: string | null;
  boardTitle: string | null;
  added: number;
  updated: number;
  alreadyAssigned: boolean;
  error?: string | null;
}> {
  if (!courseId || !userId) {
    return { boardTemplateId: null, boardTitle: null, added: 0, updated: 0, alreadyAssigned: false, error: null };
  }
  const tpl = await resolveActiveBoardTemplateForCourse(courseId, options?.explicitBoardTemplateId);
  if (!tpl) {
    return { boardTemplateId: null, boardTitle: null, added: 0, updated: 0, alreadyAssigned: false, error: null };
  }

  if (!options?.forceSync) {
    const { data: existingOne } = await supabase
      .from('assignments')
      .select('id')
      .eq('user_id', userId)
      .eq('board_template_id', tpl.id)
      .not('category', 'is', null)
      .limit(1);
    if (existingOne && existingOne.length > 0) {
      return {
        boardTemplateId: tpl.id,
        boardTitle: tpl.title,
        added: 0,
        updated: 0,
        alreadyAssigned: true,
        error: null
      };
    }
  }

  const syncRes = await syncBoardTemplateToSingleUser(tpl.id, userId);
  return {
    boardTemplateId: tpl.id,
    boardTitle: tpl.title,
    added: syncRes.added,
    updated: syncRes.updated,
    alreadyAssigned: false,
    error: syncRes.error || null
  };
}

/**
 * Ensures ALL enrolled courses with an active board template are assigned to `userId`.
 * Used automatically when students log in / open their course or TaskBoard.
 */
export async function ensureCourseBoardsAssignedForUser(
  userId: string,
  courseIds: string[]
): Promise<{
  assignedBoards: number;
  addedItems: number;
  missingTemplateIds: string[];
  blockedByRls: boolean;
}> {
  const uniqueCourseIds = Array.from(new Set((courseIds || []).map(String).filter(Boolean)));
  if (!userId || userId === 'default' || uniqueCourseIds.length === 0) {
    return { assignedBoards: 0, addedItems: 0, missingTemplateIds: [], blockedByRls: false };
  }

  const { data: tpls } = await supabase
    .from('board_templates')
    .select('id, title, course_id, is_active, created_at')
    .in('course_id', uniqueCourseIds)
    .order('is_active', { ascending: false })
    .order('created_at', { ascending: true });

  if (!tpls || tpls.length === 0) {
    return { assignedBoards: 0, addedItems: 0, missingTemplateIds: [], blockedByRls: false };
  }

  // Pick 1 primary template per course
  const primaryByCourse = new Map<string, any>();
  for (const t of tpls) {
    const cid = String(t.course_id);
    if (!primaryByCourse.has(cid)) primaryByCourse.set(cid, t);
  }

  const { data: existingAssigns } = await fetchAllPaginated((from, to) =>
    supabase
      .from('assignments')
      .select('board_template_id, board_template_title')
      .eq('user_id', userId)
      .not('category', 'is', null)
      .order('id')
      .range(from, to)
  );

  const existingIds = new Set(existingAssigns.map(a => String(a.board_template_id || '')).filter(Boolean));
  const existingTitles = new Set(existingAssigns.map(a => String(a.board_template_title || '')).filter(Boolean));

  const missingTpls = Array.from(primaryByCourse.values()).filter(
    t => !existingIds.has(String(t.id)) && !existingTitles.has(String(t.title))
  );

  if (missingTpls.length === 0) {
    return { assignedBoards: 0, addedItems: 0, missingTemplateIds: [], blockedByRls: false };
  }

  let assignedBoards = 0;
  let addedItems = 0;
  let blockedByRls = false;
  const stillMissingIds: string[] = [];

  for (const tpl of missingTpls) {
    const res = await syncBoardTemplateToSingleUser(tpl.id, userId);
    if (res.error) {
      blockedByRls = true;
      stillMissingIds.push(tpl.id);
      // Stop attempting further inserts if RLS blocks student self-insert
      const remaining = missingTpls.slice(missingTpls.indexOf(tpl) + 1).map(t => t.id);
      stillMissingIds.push(...remaining);
      break;
    }
    if (res.added > 0) {
      assignedBoards++;
      addedItems += res.added;
    } else if (res.total === 0) {
      // Empty template, nothing to assign
    }
  }

  return {
    assignedBoards,
    addedItems,
    missingTemplateIds: Array.from(new Set(stillMissingIds)),
    blockedByRls
  };
}

/**
 * Assigns/syncs a course's active board template to ALL students enrolled in that course.
 */
export async function assignCourseBoardToAllEnrolledUsers(
  courseId: string,
  explicitBoardTemplateId?: string
): Promise<{
  boardTitle: string;
  usersTotal: number;
  usersUpdated: number;
  addedItems: number;
  updatedItems: number;
}> {
  const tpl = await resolveActiveBoardTemplateForCourse(courseId, explicitBoardTemplateId);
  if (!tpl) {
    return { boardTitle: '', usersTotal: 0, usersUpdated: 0, addedItems: 0, updatedItems: 0 };
  }

  const { data: enrollRows } = await fetchAllPaginated((from, to) =>
    supabase.from('enrollments').select('user_id').eq('course_id', courseId).order('id').range(from, to)
  );
  const uniqueUserIds = Array.from(new Set((enrollRows || []).map(r => r.user_id).filter(Boolean)));

  let usersUpdated = 0;
  let addedItems = 0;
  let updatedItems = 0;

  for (const uid of uniqueUserIds) {
    const res = await syncBoardTemplateToSingleUser(tpl.id, uid);
    if (res.added > 0 || res.updated > 0) {
      usersUpdated++;
      addedItems += res.added;
      updatedItems += res.updated;
    }
  }

  return {
    boardTitle: tpl.title,
    usersTotal: uniqueUserIds.length,
    usersUpdated,
    addedItems,
    updatedItems
  };
}

/**
 * Syncs all lecture tasks (manual tasks + exercises/quizzes) of a course into:
 * 1) Active `board_templates` (`board_card_items` + `order_index` + lecture `description` JSON)
 * 2) `course_day_plans` (`day_plan_tasks`)
 * 3) All users currently assigned that board in `assignments` (non-destructively).
 */
export async function syncCourseBoardWithLectures(
  courseId: string,
  explicitBoardTemplateId?: string
): Promise<SyncBoardResult> {
  const result: SyncBoardResult = {
    addedBoardItems: 0,
    updatedBoardItems: 0,
    addedDayPlanTasks: 0,
    updatedDayPlanTasks: 0,
    syncedUsersCount: 0,
    addedUserAssignments: 0,
    updatedUserAssignments: 0
  };

  // 1. Resolve target board template
  let tplQuery = supabase.from('board_templates').select('*').eq('course_id', courseId);
  if (explicitBoardTemplateId) {
    tplQuery = tplQuery.eq('id', explicitBoardTemplateId);
  } else {
    tplQuery = tplQuery.order('is_active', { ascending: false }).order('created_at', { ascending: true });
  }
  const { data: tpls } = await tplQuery;
  const tpl = tpls?.[0];
  if (!tpl) return result;

  // 2. Fetch board structure, lectures, modules, tests, and day plans
  const [colsRes, modsRes, lecsRes, testsRes, plansRes] = await Promise.all([
    supabase.from('board_columns').select('*').eq('board_template_id', tpl.id).order('order_index'),
    supabase.from('lecture_modules').select('*').eq('course_id', courseId).order('order_index'),
    supabase.from('lectures').select('id, title, module_id, course_id, order_index, task_list').eq('course_id', courseId).order('order_index'),
    supabase.from('tests').select('id, title, test_type').eq('course_id', courseId),
    supabase.from('course_day_plans').select('*').eq('course_id', courseId).order('day_number')
  ]);

  const cols = colsRes.data || [];
  const mods = modsRes.data || [];
  const lecs = lecsRes.data || [];
  const testsById = new Map<string, any>((testsRes.data || []).map(t => [String(t.id), t]));
  const dayPlans = plansRes.data || [];

  if (cols.length === 0 || lecs.length === 0) return result;

  const colIds = cols.map(c => c.id);
  const { data: cardsData } = await supabase
    .from('board_cards')
    .select('*')
    .in('column_id', colIds)
    .order('order_index');
  const cards = cardsData || [];
  const cardIds = cards.map(c => c.id);
  const { data: itemsData } = cardIds.length > 0
    ? await supabase.from('board_card_items').select('*').in('card_id', cardIds).order('order_index')
    : { data: [] };
  const allItems = itemsData || [];

  // 3. Sync each column / card
  for (const col of cols) {
    const colCards = cards.filter(c => c.column_id === col.id);
    const cvCard = colCards.find(c => /^công việc\b/i.test((c.title || '').trim()));
    const btCard = colCards.find(c => /^bài tập\b/i.test((c.title || '').trim()));

    if (cvCard && btCard) {
      // Section/Topic layout (e.g., Business Studies, Geography)
      const colNum = extractLeadingNumber(col.title);
      const matchedMod = mods.find(m => {
        const modNum = extractLeadingNumber(m.title);
        if (colNum != null && modNum != null) return colNum === modNum;
        return m.order_index === col.order_index;
      });
      if (!matchedMod) continue;

      const modLecs = lecs
        .filter(l => l.module_id === matchedMod.id)
        .sort((a, b) => (a.order_index || 0) - (b.order_index || 0));

      // 3a. Sync Manual Tasks in `Công việc` card
      const cvItems = allItems
        .filter(i => i.card_id === cvCard.id)
        .sort((a, b) => (a.order_index || 0) - (b.order_index || 0));

      let nextManualOrder = 1;
      for (const lec of modLecs) {
        const manualTasks = (Array.isArray(lec.task_list) ? lec.task_list : []).filter(
          (t: any) => (t.type || 'manual') === 'manual' && (t.text || t.title)
        );
        for (const mTask of manualTasks) {
          const rawText = (mTask.text || mTask.title || '').trim();
          const fullTitle = `${lec.title} : ${rawText}`;
          const descJson = formatLectureTaskDescription({
            lectureId: lec.id,
            lectureTitle: lec.title,
            courseId,
            taskId: mTask.id || null
          });

          const existingItem = cvItems.find(
            i =>
              i.task_type === 'manual' &&
              ((i.title || '').trim() === fullTitle || (i.title || '').trim() === rawText)
          );

          if (existingItem) {
            if (existingItem.description !== descJson || existingItem.order_index !== nextManualOrder) {
              const { error } = await supabase
                .from('board_card_items')
                .update({ description: descJson, order_index: nextManualOrder })
                .eq('id', existingItem.id);
              if (!error) result.updatedBoardItems++;
            }
          } else {
            const { error } = await supabase.from('board_card_items').insert({
              card_id: cvCard.id,
              task_type: 'manual',
              title: fullTitle,
              description: descJson,
              test_id: null,
              order_index: nextManualOrder
            });
            if (!error) result.addedBoardItems++;
          }
          nextManualOrder++;
        }
      }

      // 3b. Sync Exercise/Quiz Tasks in `Bài tập` card (interleaved in chapter order, keeping End-of-section items at bottom)
      const btItems = allItems
        .filter(i => i.card_id === btCard.id)
        .sort((a, b) => (a.order_index || 0) - (b.order_index || 0));

      const desiredTests: { testId: string; title: string; lectureId: string; lectureTitle: string; taskId: string | null }[] = [];
      const seenTestIds = new Set<string>();

      for (const lec of modLecs) {
        const rawEx = (Array.isArray(lec.task_list) ? lec.task_list : []).filter(
          (t: any) => (t.type === 'exercise' || t.type === 'test' || t.test_id) && t.test_id
        );
        const sortedEx = sortLectureExerciseTasks(rawEx, testsById);
        for (const ex of sortedEx) {
          const tid = String(ex.test_id);
          if (seenTestIds.has(tid)) continue;
          seenTestIds.add(tid);
          const dbTest = testsById.get(tid);
          const cleanTitle = (dbTest?.title || ex.text || '').replace(/^Làm bài tập:\s*/i, '').trim();
          desiredTests.push({
            testId: tid,
            title: cleanTitle,
            lectureId: lec.id,
            lectureTitle: lec.title,
            taskId: ex.id || null
          });
        }
      }

      // Preserve any non-lecture tests already in `btCard` (such as "End of section case study" or practice papers) at the end
      const trailingItems = btItems.filter(i => !i.test_id || !seenTestIds.has(String(i.test_id)));

      let orderCursor = 1;
      for (const dt of desiredTests) {
        const existingBt = btItems.find(i => String(i.test_id || '') === dt.testId);
        if (existingBt) {
          if (existingBt.order_index !== orderCursor) {
            const { error } = await supabase
              .from('board_card_items')
              .update({ order_index: orderCursor })
              .eq('id', existingBt.id);
            if (!error) result.updatedBoardItems++;
          }
        } else {
          const { error } = await supabase.from('board_card_items').insert({
            card_id: btCard.id,
            task_type: 'test',
            title: dt.title,
            description: '',
            test_id: dt.testId,
            order_index: orderCursor
          });
          if (!error) result.addedBoardItems++;
        }
        orderCursor++;
      }

      for (const tr of trailingItems) {
        if (tr.order_index !== orderCursor) {
          const { error } = await supabase
            .from('board_card_items')
            .update({ order_index: orderCursor })
            .eq('id', tr.id);
          if (!error) result.updatedBoardItems++;
        }
        orderCursor++;
      }

      // 3c. Sync matching `course_day_plans` (`day_plan_tasks`) if present
      const cvPlan = dayPlans.find(p => (p.title || '').includes(cvCard.title));
      if (cvPlan) {
        const { data: refreshedCvItems } = await supabase
          .from('board_card_items')
          .select('*')
          .eq('card_id', cvCard.id)
          .order('order_index');
        const { data: existingPlanTasks } = await supabase
          .from('day_plan_tasks')
          .select('*')
          .eq('day_plan_id', cvPlan.id)
          .order('order_index');
        const pTasks = existingPlanTasks || [];
        for (const bItem of refreshedCvItems || []) {
          const matchPt = pTasks.find(pt => pt.task_type === 'manual' && (pt.title || '').trim() === (bItem.title || '').trim());
          if (matchPt) {
            if (matchPt.order_index !== bItem.order_index || (matchPt.description || '') !== (bItem.description || '')) {
              const { error } = await supabase
                .from('day_plan_tasks')
                .update({ order_index: bItem.order_index, description: bItem.description || '' })
                .eq('id', matchPt.id);
              if (!error) result.updatedDayPlanTasks++;
            }
          } else {
            const { error } = await supabase.from('day_plan_tasks').insert({
              day_plan_id: cvPlan.id,
              task_type: 'manual',
              title: bItem.title,
              description: bItem.description || '',
              test_id: null,
              order_index: bItem.order_index
            });
            if (!error) result.addedDayPlanTasks++;
          }
        }
      }

      const btPlan = dayPlans.find(p => (p.title || '').includes(btCard.title));
      if (btPlan) {
        const { data: refreshedBtItems } = await supabase
          .from('board_card_items')
          .select('*')
          .eq('card_id', btCard.id)
          .order('order_index');
        const { data: existingPlanTasks } = await supabase
          .from('day_plan_tasks')
          .select('*')
          .eq('day_plan_id', btPlan.id)
          .order('order_index');
        const pTasks = existingPlanTasks || [];
        for (const bItem of refreshedBtItems || []) {
          const matchPt = pTasks.find(pt => String(pt.test_id || '') === String(bItem.test_id || '') && bItem.test_id);
          if (matchPt) {
            if (matchPt.order_index !== bItem.order_index) {
              const { error } = await supabase
                .from('day_plan_tasks')
                .update({ order_index: bItem.order_index })
                .eq('id', matchPt.id);
              if (!error) result.updatedDayPlanTasks++;
            }
          } else {
            const { error } = await supabase.from('day_plan_tasks').insert({
              day_plan_id: btPlan.id,
              task_type: 'test',
              title: bItem.title,
              description: '',
              test_id: bItem.test_id,
              order_index: bItem.order_index
            });
            if (!error) result.addedDayPlanTasks++;
          }
        }
      }
    } else {
      // Lecture-per-card layout (e.g., Co-ordinated Science, Economics, Biology)
      for (const card of colCards) {
        const matchedLec = lecs.find(
          l => (l.title || '').trim().toLowerCase() === (card.title || '').trim().toLowerCase()
        );
        if (!matchedLec) continue;

        const cItems = allItems
          .filter(i => i.card_id === card.id)
          .sort((a, b) => (a.order_index || 0) - (b.order_index || 0));

        let orderCursor = 1;
        const tList = Array.isArray(matchedLec.task_list) ? matchedLec.task_list : [];
        const manualTasks = tList.filter((t: any) => (t.type || 'manual') === 'manual' && (t.text || t.title));
        const exTasks = sortLectureExerciseTasks(
          tList.filter((t: any) => (t.type === 'exercise' || t.type === 'test' || t.test_id) && t.test_id),
          testsById
        );

        for (const mTask of manualTasks) {
          const rawText = (mTask.text || mTask.title || '').trim();
          const descJson = formatLectureTaskDescription({
            lectureId: matchedLec.id,
            lectureTitle: matchedLec.title,
            courseId,
            taskId: mTask.id || null
          });
          const existingM = cItems.find(
            i =>
              i.task_type === 'manual' &&
              ((i.title || '').trim() === rawText || (i.title || '').trim() === `${matchedLec.title} : ${rawText}`)
          );
          if (existingM) {
            if (existingM.order_index !== orderCursor || existingM.description !== descJson) {
              const { error } = await supabase
                .from('board_card_items')
                .update({ order_index: orderCursor, description: descJson })
                .eq('id', existingM.id);
              if (!error) result.updatedBoardItems++;
            }
          } else {
            const { error } = await supabase.from('board_card_items').insert({
              card_id: card.id,
              task_type: 'manual',
              title: rawText,
              description: descJson,
              test_id: null,
              order_index: orderCursor
            });
            if (!error) result.addedBoardItems++;
          }
          orderCursor++;
        }

        const seenTids = new Set<string>();
        for (const ex of exTasks) {
          const tid = String(ex.test_id);
          if (seenTids.has(tid)) continue;
          seenTids.add(tid);
          const dbTest = testsById.get(tid);
          const cleanTitle = (dbTest?.title || ex.text || '').replace(/^Làm bài tập:\s*/i, '').trim();
          const existingT = cItems.find(i => String(i.test_id || '') === tid);
          if (existingT) {
            if (existingT.order_index !== orderCursor) {
              const { error } = await supabase
                .from('board_card_items')
                .update({ order_index: orderCursor })
                .eq('id', existingT.id);
              if (!error) result.updatedBoardItems++;
            }
          } else {
            const { error } = await supabase.from('board_card_items').insert({
              card_id: card.id,
              task_type: 'test',
              title: cleanTitle,
              description: '',
              test_id: tid,
              order_index: orderCursor
            });
            if (!error) result.addedBoardItems++;
          }
          orderCursor++;
        }
      }
    }
  }

  // 4. Sync all users who already have this board assigned
  const { data: assignedRows } = await supabase
    .from('assignments')
    .select('user_id')
    .or(`board_template_id.eq.${tpl.id},board_template_title.eq."${tpl.title.replace(/"/g, '\\"')}"`);

  const uniqueUserIds = Array.from(new Set((assignedRows || []).map(r => r.user_id).filter(Boolean)));
  for (const uid of uniqueUserIds) {
    const userRes = await syncBoardTemplateToSingleUser(tpl.id, uid);
    result.syncedUsersCount++;
    result.addedUserAssignments += userRes.added;
    result.updatedUserAssignments += userRes.updated;
  }

  return result;
}
