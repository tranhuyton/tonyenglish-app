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
): Promise<{ added: number; updated: number; total: number }> {
  const { data: tpl } = await supabase
    .from('board_templates')
    .select('id, title, course_id')
    .eq('id', boardTemplateId)
    .maybeSingle();
  if (!tpl) return { added: 0, updated: 0, total: 0 };

  const { data: cols } = await supabase
    .from('board_columns')
    .select('*')
    .eq('board_template_id', boardTemplateId)
    .order('order_index');
  const colList = cols || [];
  if (colList.length === 0) return { added: 0, updated: 0, total: 0 };

  const colIds = colList.map(c => c.id);
  const { data: cards } = await supabase
    .from('board_cards')
    .select('*')
    .in('column_id', colIds)
    .order('order_index');
  const cardList = cards || [];
  const cardIds = cardList.map(c => c.id);
  const { data: items } = cardIds.length > 0
    ? await supabase.from('board_card_items').select('*').in('card_id', cardIds).order('order_index')
    : { data: [] };
  const itemList = items || [];

  const { data: existingRows } = await supabase
    .from('assignments')
    .select('*')
    .eq('user_id', userId);

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

  for (const upd of toUpdate) {
    await supabase.from('assignments').update(upd.payload).eq('id', upd.id);
  }

  const chunkSize = 100;
  for (let i = 0; i < toInsert.length; i += chunkSize) {
    await supabase.from('assignments').insert(toInsert.slice(i, i + chunkSize));
  }

  return {
    added: toInsert.length,
    updated: toUpdate.length,
    total: itemList.length
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
