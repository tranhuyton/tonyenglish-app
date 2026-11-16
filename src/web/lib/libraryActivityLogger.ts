import { supabase, isTonyEnglishAuthUser } from '../../supabase';

export interface LibraryExerciseQuestionResult {
  qNum: number;
  question: string;
  picked: string;
  correct: string;
  isRight: boolean;
}

export interface LibraryReadLogInput {
  activity_kind: 'read_article' | 'read_ebook' | 'watch_video';
  news_id?: number;
  video_id?: number;
  article_title: string;
  article_slug?: string;
  url_path?: string;
  category_id?: number;
  parent_category_id?: number;
  category_name: string;
  sub_category_name?: string;
  library_type: string;
  course_id?: string;
  has_quiz?: boolean;
  quiz_question_count?: number;
  has_legacy_qa?: boolean;
  is_ebook?: boolean;
  has_podcast?: boolean;
  ebook_page?: number;
  ebook_max_page?: number;
  ebook_total_pages?: number | null;
  pages_turned?: number;
  duration_sec?: number;
}

export interface LibraryExerciseLogInput {
  exercise_kind: 'article_quiz' | 'video_quiz' | 'qa_practice' | 'speaking_podcast';
  news_id?: number;
  video_id?: number;
  item_title: string;
  article_slug?: string;
  url_path?: string;
  category_id?: number;
  parent_category_id?: number;
  category_name: string;
  sub_category_name?: string;
  library_type: string;
  course_id?: string;
  score?: number;
  total_questions?: number;
  percent?: number;
  answered_count?: number;
  time_spent_sec?: number;
  practice_mode?: 'shadowing' | 'reflex' | 'orange_drill' | string;
  practiced_count?: number;
  question_results?: LibraryExerciseQuestionResult[];
}

export async function getActiveTonyStudentUserId(): Promise<string | null> {
  try {
    const {
      data: { session },
    } = await supabase.auth.getSession();
    if (!session?.user?.id) return null;
    if (!isTonyEnglishAuthUser(session.user)) return null;
    return session.user.id;
  } catch {
    return null;
  }
}

export async function insertLibraryReadLog(
  details: LibraryReadLogInput,
  explicitUserId?: string | null
): Promise<string | null> {
  const uid = explicitUserId || (await getActiveTonyStudentUserId());
  if (!uid) return null;

  try {
    const { data, error } = await supabase
      .from('activity_logs')
      .insert([
        {
          user_id: uid,
          action_type: 'read_library',
          details,
        },
      ])
      .select('id')
      .maybeSingle();

    if (error) {
      // Fallback without .select('id') in case SELECT policy differs
      await supabase.from('activity_logs').insert([
        {
          user_id: uid,
          action_type: 'read_library',
          details,
        },
      ]);
      return null;
    }
    return data?.id ? String(data.id) : null;
  } catch {
    return null;
  }
}

export async function updateLibraryReadDuration(
  logId: string | null,
  baseDetails: LibraryReadLogInput,
  durationSec: number
): Promise<void> {
  if (!logId || durationSec < 10) return;
  try {
    await supabase
      .from('activity_logs')
      .update({
        details: {
          ...baseDetails,
          duration_sec: Math.round(durationSec),
        },
      })
      .eq('id', logId);
  } catch {
    // Best-effort duration enrichment; ignore if RLS disallows update
  }
}

export async function insertLibraryExerciseLog(
  input: LibraryExerciseLogInput,
  explicitUserId?: string | null
): Promise<void> {
  const uid = explicitUserId || (await getActiveTonyStudentUserId());
  if (!uid) return;

  try {
    await supabase.from('activity_logs').insert([
      {
        user_id: uid,
        action_type: 'library_exercise',
        details: {
          ...input,
          article_title: input.item_title,
        },
      },
    ]);
  } catch {
    // ignore network failure gracefully
  }
}
