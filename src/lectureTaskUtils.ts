export interface LectureTaskMeta {
  isLecture: boolean;
  lectureId: string | null;
  lectureTitle: string;
  courseId: string | null;
  taskId: string | null;
}

/**
 * Parses lecture metadata from an assignment or board_card_item.
 * Checks item.description JSON first, then falls back to matching card title or item title against lectures.
 */
export function parseLectureFromItem(item: any, cardTitle?: string, lectures?: any[]): LectureTaskMeta {
  if (!item) {
    return { isLecture: false, lectureId: null, lectureTitle: '', courseId: null, taskId: null };
  }

  // 1. Check description JSON
  if (item.description) {
    try {
      const parsed = typeof item.description === 'string' ? JSON.parse(item.description) : item.description;
      if (parsed && (parsed.lecture_id || parsed.source === 'lecture')) {
        return {
          isLecture: true,
          lectureId: parsed.lecture_id || null,
          lectureTitle: parsed.lecture_title || '',
          courseId: parsed.course_id || null,
          taskId: parsed.task_id || null
        };
      }
    } catch (e) {
      // Not JSON, continue to fallback checks
    }
  }

  // 2. Fallback check with lectures list
  if (Array.isArray(lectures) && lectures.length > 0) {
    const effectiveCardTitle = (cardTitle || item.card_title || '').trim().toLowerCase();
    const itemTitle = (item.title || '').trim().toLowerCase();

    // 2a. Match by card title
    if (effectiveCardTitle) {
      const matchedLec = lectures.find(l => (l.title || '').trim().toLowerCase() === effectiveCardTitle);
      if (matchedLec && Array.isArray(matchedLec.task_list)) {
        const hasTask = matchedLec.task_list.some((t: any) => {
          const tText = (t.text || t.title || '').trim().toLowerCase();
          return tText && (
            tText === itemTitle ||
            `${(matchedLec.title || '').toLowerCase()} : ${tText}` === itemTitle ||
            itemTitle.endsWith(tText)
          );
        });
        if (hasTask) {
          return {
            isLecture: true,
            lectureId: matchedLec.id,
            lectureTitle: matchedLec.title || '',
            courseId: matchedLec.course_id || null,
            taskId: null
          };
        }
      }
    }

    // 2b. Match by task text in any lecture's task_list
    if (itemTitle) {
      const anyLecWithTask = lectures.find(l => 
        Array.isArray(l.task_list) && l.task_list.some((t: any) => {
          const tText = (t.text || t.title || '').trim().toLowerCase();
          return tText && (
            tText === itemTitle ||
            `${(l.title || '').toLowerCase()} : ${tText}` === itemTitle
          );
        })
      );
      if (anyLecWithTask) {
        return {
          isLecture: true,
          lectureId: anyLecWithTask.id,
          lectureTitle: anyLecWithTask.title || '',
          courseId: anyLecWithTask.course_id || null,
          taskId: null
        };
      }
    }
  }

  return { isLecture: false, lectureId: null, lectureTitle: '', courseId: null, taskId: null };
}

/**
 * Returns a human-friendly display description, filtering out raw internal JSON strings.
 */
export function getDisplayDescription(desc?: string | null): string | null {
  if (!desc || typeof desc !== 'string') return null;
  const trimmed = desc.trim();
  if (trimmed.startsWith('{') && (trimmed.includes('lecture_id') || trimmed.includes('source'))) {
    try {
      const parsed = JSON.parse(trimmed);
      if (parsed.source === 'lecture' || parsed.lecture_id) {
        return null; // Don't show raw JSON, UI shows explicit lecture badge/button
      }
    } catch (e) {}
  }
  return trimmed;
}

/**
 * Formats lecture metadata into a description JSON string for storing in DB.
 */
export function formatLectureTaskDescription(meta: {
  lectureId: string;
  lectureTitle: string;
  courseId?: string | null;
  taskId?: string | null;
}): string {
  return JSON.stringify({
    source: 'lecture',
    lecture_id: meta.lectureId,
    lecture_title: meta.lectureTitle,
    course_id: meta.courseId || null,
    task_id: meta.taskId || null
  });
}
