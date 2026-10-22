import React, { useState, useMemo, useEffect } from 'react';
import { supabase } from './supabase';
import { BoardTheme, DEFAULT_BOARD_THEME, BoardThemeModal, createCustomTheme, loadTheme, saveTheme } from './ThemeModal';
import { parseLectureFromItem, getDisplayDescription } from './lectureTaskUtils';

interface Assignment {
  id: string;
  user_id: string;
  due_date: string;
  title: string;
  description: string;
  task_type: 'manual' | 'test';
  test_id: string | null;
  student_completed: boolean;
  admin_approved: boolean;
  is_completed: boolean;
  card_title?: string;
  created_at: string;
}

interface Props {
  assignments: Assignment[];
  completedTestIds: Set<string>;
  topActions?: React.ReactNode;
  rightActions?: React.ReactNode;
  courseTitle?: string;
  lectures?: any[];
  onOpenLecture?: (courseId?: string, lectureId?: string) => void;
  onRefresh: () => void;
  onStartTest?: (testId: string) => void;
  userId?: string;
}

const WEEKDAYS = ['CN', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7'];

const formatDateVN = (dateStr?: string | null) => {
  if (!dateStr) return '';
  const clean = dateStr.split('T')[0];
  const parts = clean.split('-');
  if (parts.length === 3) {
    const [y, m, d] = parts;
    return `${d.padStart(2, '0')}/${m.padStart(2, '0')}/${y}`;
  }
  return dateStr;
};

export default function AssignmentCalendar({ 
  assignments, 
  completedTestIds, 
  topActions, 
  rightActions, 
  courseTitle, 
  lectures,
  onOpenLecture,
  onRefresh, 
  onStartTest, 
  userId: propUserId 
}: Props) {
  const userId = propUserId || (assignments.length > 0 ? assignments[0].user_id : 'default');
  const [internalLectures, setInternalLectures] = useState<any[]>([]);
  useEffect(() => {
    if (!lectures || lectures.length === 0) {
      supabase.from('lectures').select('id, title, course_id, task_list').then(({ data }) => {
        if (data) setInternalLectures(data);
      });
    }
  }, [lectures]);
  const effectiveLectures = (lectures && lectures.length > 0) ? lectures : internalLectures;

  const [currentMonth, setCurrentMonth] = useState(new Date());
  const [selectedDate, setSelectedDate] = useState<string | null>(new Date().toISOString().split('T')[0]);
  const [calendarMode, setCalendarMode] = useState<'day' | 'month' | 'all'>('day');
  const [isUpdating, setIsUpdating] = useState<string | null>(null);
  const [latestTestScores, setLatestTestScores] = useState<Map<string, { score: number; total_score: number; percent: number; isPassed: boolean; completedAt: string | null }>>(new Map());

  const [isThemeModalOpen, setIsThemeModalOpen] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [calendarTheme, setCalendarTheme] = useState<BoardTheme>(() => loadTheme(`tony_calendar_theme_${userId}`, 'tony_calendar_theme'));

  useEffect(() => {
    if (userId && userId !== 'default') {
      setCalendarTheme(loadTheme(`tony_calendar_theme_${userId}`, 'tony_calendar_theme'));
    }
  }, [userId]);

  // Tải điểm thi thực tế từ test_results
  useEffect(() => {
    const fetchScores = async () => {
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) return;
      const { data } = await supabase.from('test_results')
        .select('id, test_id, test_title, score, total_score, created_at, details')
        .eq('user_id', user.id)
        .order('created_at', { ascending: false });

      const scoreMap = new Map<string, { score: number; total_score: number; percent: number; isPassed: boolean; completedAt: string | null }>();
      (data || []).forEach((r: any) => {
        let d = r.details;
        if (typeof d === 'string') {
          try { d = JSON.parse(d); } catch (e) {}
        }
        const testId = d?.test_id ? String(d.test_id) : (r.test_id ? String(r.test_id) : null);
        const testTitle = r.test_title ? r.test_title.trim().toLowerCase() : null;

        const score = parseFloat(r.score != null ? r.score : 0);
        const total = parseFloat(r.total_score != null ? r.total_score : 0);
        const percent = total > 0 ? Math.round((score / total) * 100) : (score >= 5 ? 100 : Math.round(score * 10));

        let isPassed = false;
        if (d?.bandScore != null && !isNaN(parseFloat(d.bandScore))) {
          isPassed = parseFloat(d.bandScore) >= 4.0;
        } else if (total > 0) {
          isPassed = (score / total) >= 0.5;
        } else {
          isPassed = score >= 5.0;
        }

        const completedAt = r.created_at ? r.created_at.split('T')[0] : null;
        const scoreObj = { score, total_score: total, percent, isPassed, completedAt };
        const registerScore = (key: string) => {
          const existing = scoreMap.get(key);
          if (!existing) {
            scoreMap.set(key, scoreObj);
          } else if (!existing.isPassed && isPassed) {
            scoreMap.set(key, scoreObj);
          } else if (isPassed && existing.isPassed) {
            // Lưu lại ngày hoàn thành sớm nhất đạt yêu cầu
            if (completedAt && existing.completedAt && completedAt < existing.completedAt) {
              scoreMap.set(key, { ...existing, completedAt });
            }
          } else if (percent > existing.percent) {
            scoreMap.set(key, scoreObj);
          }
        };

        if (testId) registerScore(testId);
        if (testTitle) registerScore(testTitle);
      });
      setLatestTestScores(scoreMap);
    };

    fetchScores();
    const handleRefresh = () => fetchScores();
    window.addEventListener('tony-refresh-lecture-progress', handleRefresh);
    return () => {
      window.removeEventListener('tony-refresh-lecture-progress', handleRefresh);
    };
  }, [assignments]);

  // ============================================
  // CALENDAR LOGIC
  // ============================================
  const calendarDays = useMemo(() => {
    const year = currentMonth.getFullYear();
    const month = currentMonth.getMonth();
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const startPad = firstDay.getDay(); // 0=Sun
    const days: { date: string; day: number; isCurrentMonth: boolean; isToday: boolean }[] = [];

    // Padding trước
    const prevMonth = new Date(year, month, 0);
    for (let i = startPad - 1; i >= 0; i--) {
      const d = prevMonth.getDate() - i;
      const dateStr = `${year}-${String(month).padStart(2, '0')}-${String(d).padStart(2, '0')}`;
      days.push({ date: dateStr, day: d, isCurrentMonth: false, isToday: false });
    }

    // Ngày trong tháng
    const today = new Date().toISOString().split('T')[0];
    for (let d = 1; d <= lastDay.getDate(); d++) {
      const dateStr = `${year}-${String(month + 1).padStart(2, '0')}-${String(d).padStart(2, '0')}`;
      days.push({ date: dateStr, day: d, isCurrentMonth: true, isToday: dateStr === today });
    }

    // Padding sau
    const remaining = 42 - days.length;
    for (let d = 1; d <= remaining; d++) {
      const nextM = month + 2;
      const dateStr = `${nextM > 12 ? year + 1 : year}-${String(nextM > 12 ? 1 : nextM).padStart(2, '0')}-${String(d).padStart(2, '0')}`;
      days.push({ date: dateStr, day: d, isCurrentMonth: false, isToday: false });
    }

    return days;
  }, [currentMonth]);

  // ============================================
  // QUY TẮC XÁC ĐỊNH NGÀY GIAO BÀI (EFFECTIVE DUE DATE):
  // "Nếu ngày hoàn thành trước ngày giao bài thì lấy ngày hoàn thành làm ngày giao bài."
  // ============================================
  const getEffectiveDueDate = useMemo(() => {
    return (a: Assignment): string | null => {
      const originalDue = a.due_date ? a.due_date.trim() : null;
      if (!originalDue) return null;

      let completionDate: string | null = null;
      if (a.task_type === 'test') {
        const testKey = a.test_id ? String(a.test_id) : null;
        const titleKey = a.title ? a.title.trim().toLowerCase() : null;
        const scoreInfo = (testKey && latestTestScores.get(testKey)) || 
                          (titleKey && latestTestScores.get(titleKey));
        const isDone = a.is_completed || (testKey && completedTestIds.has(testKey)) || !!scoreInfo?.isPassed;
        if (isDone) {
          if (scoreInfo?.completedAt) {
            completionDate = scoreInfo.completedAt;
          } else if (a.updated_at) {
            completionDate = a.updated_at.split('T')[0];
          } else if (a.created_at) {
            completionDate = a.created_at.split('T')[0];
          }
        }
      } else {
        const isDone = a.is_completed || a.student_completed;
        if (isDone) {
          if (a.updated_at) {
            completionDate = a.updated_at.split('T')[0];
          } else if (a.created_at) {
            completionDate = a.created_at.split('T')[0];
          }
        }
      }

      if (completionDate && completionDate < originalDue) {
        return completionDate;
      }
      return originalDue;
    };
  }, [latestTestScores, completedTestIds]);

  // Đồng bộ ngày giao bài vào Database nếu hoàn thành trước hạn
  useEffect(() => {
    if (latestTestScores.size === 0 || assignments.length === 0) return;
    assignments.forEach(async (a) => {
      if (!a.due_date) return;
      const eff = getEffectiveDueDate(a);
      if (eff && eff < a.due_date) {
        await supabase.from('assignments').update({
          due_date: eff,
          updated_at: new Date().toISOString()
        }).eq('id', a.id);
      }
    });
  }, [assignments, latestTestScores, getEffectiveDueDate]);

  // ============================================
  // TRẠNG THÁI TỪNG NGÀY
  // ============================================
  const dateStatusMap = useMemo(() => {
    const map: Record<string, 'blue' | 'green' | 'red'> = {};
    const today = new Date().toISOString().split('T')[0];

    // Group assignments by effective date
    const byDate: Record<string, Assignment[]> = {};
    assignments.forEach(a => {
      const effDate = getEffectiveDueDate(a);
      if (!effDate) return;
      if (!byDate[effDate]) byDate[effDate] = [];
      byDate[effDate].push(a);
    });

    Object.entries(byDate).forEach(([date, tasks]) => {
      const allCompleted = tasks.every(t => {
        if (t.task_type === 'test') {
          const testKey = t.test_id ? String(t.test_id) : null;
          const titleKey = t.title ? t.title.trim().toLowerCase() : null;
          const scoreInfo = (testKey && latestTestScores.get(testKey)) || 
                            (titleKey && latestTestScores.get(titleKey));
          return t.is_completed || (testKey && completedTestIds.has(testKey)) || !!scoreInfo?.isPassed;
        }
        return t.is_completed || t.student_completed;
      });

      if (allCompleted) {
        map[date] = 'green';
      } else if (date < today) {
        map[date] = 'red';
      } else {
        map[date] = 'blue';
      }
    });

    return map;
  }, [assignments, completedTestIds, latestTestScores, getEffectiveDueDate]);

  // ============================================
  // TASKS CHO KHOẢNG THỜI GIAN ĐANG CHỌN (day/month/all)
  // ============================================
  const selectedTasks = useMemo(() => {
    // Chỉ lấy assignment CÓ NGÀY GIAO (due_date) - bỏ qua task từ bảng công việc không có ngày
    const withDate = assignments
      .filter(a => a.due_date && a.due_date.trim() !== '')
      .map(a => {
        const effDate = getEffectiveDueDate(a);
        let isDone = false;
        if (a.task_type === 'test') {
          const testKey = a.test_id ? String(a.test_id) : null;
          const titleKey = a.title ? a.title.trim().toLowerCase() : null;
          const scoreInfo = (testKey && latestTestScores.get(testKey)) || 
                            (titleKey && latestTestScores.get(titleKey));
          isDone = a.is_completed || (testKey && completedTestIds.has(testKey)) || !!scoreInfo?.isPassed;
        } else {
          isDone = a.is_completed || a.student_completed;
        }
        return {
          ...a,
          _effectiveDueDate: effDate,
          _effectiveCompleted: isDone
        };
      });

    let filtered: typeof withDate;

    if (calendarMode === 'day') {
      if (!selectedDate) return [];
      filtered = withDate.filter(a => a._effectiveDueDate === selectedDate);
    } else if (calendarMode === 'month') {
      const year = currentMonth.getFullYear();
      const month = currentMonth.getMonth() + 1;
      const prefix = `${year}-${String(month).padStart(2, '0')}`;
      filtered = withDate.filter(a => a._effectiveDueDate?.startsWith(prefix));
    } else {
      // 'all' mode: tất cả assignment CÓ NGÀY GIAO
      filtered = withDate;
    }

    return filtered.sort((a, b) => (a._effectiveDueDate || '').localeCompare(b._effectiveDueDate || ''));
  }, [selectedDate, calendarMode, currentMonth, assignments, completedTestIds, latestTestScores, getEffectiveDueDate]);

  // Tách thành 2 mảng riêng biệt: Danh sách Công việc (Manual) và Danh sách Bài tập (Test)
  const selectedManualTasks = useMemo(() => {
    return selectedTasks.filter(t => t.task_type === 'manual');
  }, [selectedTasks]);

  const selectedTestTasks = useMemo(() => {
    return selectedTasks.filter(t => t.task_type === 'test');
  }, [selectedTasks]);

  const completedManualCount = selectedManualTasks.filter(t => t._effectiveCompleted).length;
  const completedTestCount = selectedTestTasks.filter(t => t._effectiveCompleted).length;
  const completedTotalCount = selectedTasks.filter(t => t._effectiveCompleted).length;

  // ============================================
  // HANDLERS
  // ============================================
  const handleToggleComplete = async (task: Assignment) => {
    if (task.task_type !== 'manual') return;
    if (task.is_completed) return;

    setIsUpdating(task.id);
    const newVal = !task.student_completed;
    const today = new Date().toISOString().split('T')[0];
    
    // Nếu hoàn thành sớm hơn ngày giao thì lấy ngày hoàn thành làm ngày giao
    let targetDueDate = task.due_date;
    if (newVal && task.due_date && today < task.due_date) {
      targetDueDate = today;
    }
    
    // Update this specific task
    await supabase.from('assignments').update({
      student_completed: newVal,
      due_date: targetDueDate,
      updated_at: new Date().toISOString()
    }).eq('id', task.id);
    
    // Also sync all matching assignments
    const syncPayload: any = { student_completed: newVal, due_date: targetDueDate, updated_at: new Date().toISOString() };
    if (!newVal) syncPayload.admin_approved = false;
    let syncQuery = supabase.from('assignments').update(syncPayload)
      .eq('user_id', task.user_id)
      .eq('title', task.title)
      .eq('task_type', 'manual');
    if (task.card_title) {
      syncQuery = syncQuery.eq('card_title', task.card_title);
    }
    await syncQuery;

    setIsUpdating(null);
    onRefresh();
  };

  const prevMonth = () => setCurrentMonth(new Date(currentMonth.getFullYear(), currentMonth.getMonth() - 1));
  const nextMonth = () => setCurrentMonth(new Date(currentMonth.getFullYear(), currentMonth.getMonth() + 1));
  const goToday = () => { setCalendarMode('day'); setCurrentMonth(new Date()); setSelectedDate(new Date().toISOString().split('T')[0]); };

  const handleSelectCalendarTheme = (theme: BoardTheme) => {
    setCalendarTheme(theme);
    saveTheme(`tony_calendar_theme_${userId}`, theme, 'tony_calendar_theme');
  };

  const handleApplyCustomCalendarColor = (hex: string) => {
    handleSelectCalendarTheme(createCustomTheme(hex));
  };

  const monthLabel = currentMonth.toLocaleDateString('vi-VN', { month: 'long', year: 'numeric' });

  // Helper: get cell background based on status
  const getCellBg = (status: 'blue' | 'green' | 'red' | undefined, isSelected: boolean) => {
    if (isSelected) return 'bg-[#0a5482] text-white shadow-md scale-105 ring-2 ring-[#2ab4e8]/50 font-black';
    if (!status) return '';
    if (status === 'green') return 'bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold';
    if (status === 'red') return 'bg-rose-50 text-rose-700 border border-rose-200 font-bold';
    return 'bg-sky-50 text-[#0a5482] border border-sky-200 font-bold';
  };

  const headerActions = topActions || rightActions;

  const selectedDateFormatted = selectedDate 
    ? new Date(selectedDate + 'T00:00:00').toLocaleDateString('vi-VN', { day: 'numeric', month: 'long' })
    : null;

  const rangeLabel = calendarMode === 'day' 
    ? (selectedDateFormatted ? `Ngày ${selectedDateFormatted}` : 'Chưa chọn ngày')
    : calendarMode === 'month'
      ? monthLabel
      : 'Toàn bộ thời gian';

  const progressPercent = selectedTasks.length > 0 
    ? Math.round((completedTotalCount / selectedTasks.length) * 100) 
    : 0;

  const isCustomBg = calendarTheme.id !== 'tony-classic';

  return (
    <div 
      className={`w-full min-h-[500px] text-slate-800 relative transition-colors duration-300 ${
        isCustomBg ? 'p-3 sm:p-4 md:p-5 rounded-3xl' : 'p-0'
      }`}
      style={isCustomBg ? { backgroundColor: calendarTheme.boardBg } : undefined}
    >
      <div className="w-full space-y-5">
        {/* TONYENGLISH.VN SYNCHRONIZED HERO BANNER */}
        <div 
          className="rounded-2xl sm:rounded-3xl p-5 sm:p-6 md:p-7 shadow-md text-white flex flex-col gap-4 relative z-30 border border-slate-800/20"
          style={{ background: calendarTheme.titleBg }}
        >
          {/* Decorative Ambient Glow */}
          <div className="absolute inset-0 overflow-hidden rounded-2xl sm:rounded-3xl pointer-events-none">
            <div className="absolute -top-24 -right-24 w-80 h-80 bg-[#2ab4e8]/15 blur-3xl rounded-full"></div>
            <div className="absolute -bottom-24 -left-24 w-64 h-64 bg-sky-400/10 blur-3xl rounded-full"></div>
          </div>

          <div className="relative z-20 flex flex-col lg:flex-row justify-between items-start lg:items-center gap-4">
            <div className="flex items-start justify-between w-full lg:w-auto gap-3">
              <div>
                <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-xs border border-white/15 px-3 py-1 rounded-full text-[10px] sm:text-[11px] font-extrabold tracking-widest uppercase text-[#2ab4e8] mb-2.5">
                  <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                  TonyEnglish Study Schedule • Lịch Báo Bài
                </div>
                <h1 className="text-xl sm:text-2xl md:text-[26px] font-black tracking-tight text-white leading-tight">
                  Lịch Báo Bài{courseTitle ? ` — ${courseTitle}` : ''}
                </h1>
                <p className="text-slate-200/85 text-xs sm:text-sm mt-1 font-medium">
                  Chọn ngày trên lịch để theo dõi tiến độ tự học và hoàn thành bài tập đúng hạn.
                </p>
              </div>

              {/* Mobile More Button in Top Header */}
              <div className="sm:hidden relative shrink-0">
                <button
                  type="button"
                  onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
                  className="w-9 h-9 rounded-xl bg-white/15 hover:bg-white/25 border border-white/20 active:scale-95 text-white flex items-center justify-center font-bold text-base transition-all shadow-xs cursor-pointer"
                  title="Tùy chọn khác"
                >
                  ⋯
                </button>

                {isMobileMenuOpen && (
                  <>
                    <div className="fixed inset-0 z-40" onClick={() => setIsMobileMenuOpen(false)}></div>
                    <div className="absolute right-0 top-full mt-2 w-56 bg-white rounded-2xl shadow-2xl border border-slate-200 py-1.5 z-50 animate-in fade-in zoom-in-95 duration-150 text-slate-800">
                      <button
                        type="button"
                        onClick={() => { setIsThemeModalOpen(true); setIsMobileMenuOpen(false); }}
                        className="w-full px-4 py-2.5 text-left text-xs font-bold hover:bg-slate-50 flex items-center gap-2.5 transition-colors cursor-pointer"
                      >
                        <span className="text-base">🎨</span> Đổi giao diện màu nền
                      </button>
                      {onOpenLecture && (
                        <button
                          type="button"
                          onClick={() => { onOpenLecture(); setIsMobileMenuOpen(false); }}
                          className="w-full px-4 py-2.5 text-left text-xs font-bold hover:bg-emerald-50 text-emerald-700 flex items-center gap-2.5 transition-colors border-t border-slate-100 cursor-pointer"
                        >
                          <span className="text-base">📖</span> Bài giảng lý thuyết
                        </button>
                      )}
                      {onStartTest && (
                        <button
                          type="button"
                          onClick={() => { onStartTest(''); setIsMobileMenuOpen(false); }}
                          className="w-full px-4 py-2.5 text-left text-xs font-bold hover:bg-sky-50 text-[#0a5482] flex items-center gap-2.5 transition-colors border-t border-slate-100 cursor-pointer"
                        >
                          <span className="text-base">📚</span> Mở kho đề
                        </button>
                      )}
                    </div>
                  </>
                )}
              </div>
            </div>

            <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 w-full lg:w-auto justify-between lg:justify-end">
              {selectedTasks.length > 0 ? (
                <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-xl px-3.5 py-2 flex flex-col justify-center min-w-[200px]">
                  <div className="flex items-center justify-between text-xs text-white/95 font-bold mb-1.5 gap-3">
                    <span className="truncate">{rangeLabel}</span>
                    <span className="text-[#2ab4e8] font-black shrink-0">{completedTotalCount}/{selectedTasks.length} ({progressPercent}%)</span>
                  </div>
                  <div className="w-full h-1.5 bg-white/20 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-gradient-to-r from-[#2ab4e8] to-emerald-400 rounded-full transition-all duration-500"
                      style={{ width: `${progressPercent}%` }}
                    />
                  </div>
                </div>
              ) : (
                <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-xl px-3.5 py-2 text-xs text-slate-200 font-semibold self-start sm:self-auto">
                  {calendarMode === 'day' && !selectedDate 
                    ? '👈 Chọn một ngày trên lịch để xem công việc'
                    : `${rangeLabel}: Chưa có nhiệm vụ được giao`
                  }
                </div>
              )}

              <div className="flex items-center justify-between sm:justify-end gap-2 shrink-0">
                {/* MODE FILTER */}
                <div className="flex bg-white/10 backdrop-blur-xs border border-white/15 rounded-xl p-1 gap-0.5">
                  {([
                    { key: 'day' as const, label: 'Ngày' },
                    { key: 'month' as const, label: 'Tháng' },
                    { key: 'all' as const, label: 'Tất cả' },
                  ]).map(m => (
                    <button
                      key={m.key}
                      onClick={() => setCalendarMode(m.key)}
                      className={`text-[12px] font-extrabold px-3 py-1.5 rounded-lg transition-all cursor-pointer ${
                        calendarMode === m.key
                          ? 'bg-white text-[#0a5482] shadow-xs'
                          : 'text-white/80 hover:bg-white/10 hover:text-white'
                      }`}
                    >
                      {m.label}
                    </button>
                  ))}
                </div>

                {/* NÚT HÔM NAY */}
                <button 
                  onClick={goToday} 
                  className="bg-[#2ab4e8] hover:bg-[#1fa0d4] active:scale-95 text-white text-xs sm:text-[13px] font-extrabold px-3.5 sm:px-4 py-2 rounded-xl transition-all shadow-sm flex items-center gap-1.5 cursor-pointer shrink-0"
                  title="Xem công việc hôm nay"
                >
                  <span>🎯</span> <span>Hôm nay</span>
                </button>
                
                {/* NÚT ĐỔI MÀU NỀN (desktop only, mobile hides it into ⋯) */}
                <button 
                  onClick={() => setIsThemeModalOpen(true)} 
                  className="hidden sm:flex bg-white/12 hover:bg-white/20 border border-white/20 active:scale-95 text-white text-xs sm:text-[13px] font-bold px-3.5 py-2 rounded-xl transition-all shadow-xs items-center gap-1.5 cursor-pointer shrink-0"
                  title="Đổi giao diện màu nền"
                >
                  <span>🎨</span> <span className="hidden xl:inline">Giao diện</span>
                </button>
              </div>
            </div>
          </div>

          {headerActions && (
            <div className="relative z-30 pt-3 border-t border-white/15 flex flex-wrap items-center justify-between gap-2">
              <span className="text-[11px] font-bold uppercase tracking-wider text-sky-200/80 hidden sm:inline">
                Lối tắt học tập &amp; Bộ lọc khóa học:
              </span>
              <div className="w-full sm:w-auto flex justify-end">
                {headerActions}
              </div>
            </div>
          )}
        </div>

        {/* 3-COLUMN CONTENT: CALENDAR (LEFT) & 2 COLUMNS (RIGHT: CỘT CÔNG VIỆC + CỘT BÀI TẬP) */}
        <div className="flex flex-col xl:flex-row gap-5 items-start w-full">
          
          {/* ========== LEFT: CALENDAR ========== */}
          <div className="w-full xl:w-[380px] 2xl:w-[400px] shrink-0">
            <div className="bg-white rounded-2xl sm:rounded-3xl shadow-xs border border-slate-200/90 overflow-hidden">
              {/* MONTH NAV */}
              <div className="flex items-center justify-between px-5 py-4 border-b border-slate-200/80 bg-slate-50/70">
                <button onClick={prevMonth} className="w-8 h-8 rounded-xl bg-white hover:bg-sky-50 border border-slate-200/90 hover:border-[#2ab4e8] flex items-center justify-center text-[#0a5482] transition-all shadow-2xs cursor-pointer">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" /></svg>
                </button>
                <div className="flex items-center gap-2">
                  <span className="w-1.5 h-5 bg-[#0a5482] rounded-full"></span>
                  <h3 className="font-black text-slate-900 text-[15.5px] capitalize tracking-tight">
                    {monthLabel}
                  </h3>
                </div>
                <button onClick={nextMonth} className="w-8 h-8 rounded-xl bg-white hover:bg-sky-50 border border-slate-200/90 hover:border-[#2ab4e8] flex items-center justify-center text-[#0a5482] transition-all shadow-2xs cursor-pointer">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" /></svg>
                </button>
              </div>

              {/* WEEKDAY HEADERS */}
              <div className="grid grid-cols-7 px-3.5 pt-3.5 pb-1.5">
                {WEEKDAYS.map(d => (
                  <div key={d} className="text-center text-[11px] font-extrabold text-slate-400 uppercase tracking-wider">{d}</div>
                ))}
              </div>

              {/* CALENDAR GRID */}
              <div className="grid grid-cols-7 px-3.5 pb-3.5 gap-1.5">
                {calendarDays.map((day, i) => {
                  const status = dateStatusMap[day.date];
                  const hasTask = !!status;
                  const isSelected = selectedDate === day.date;
                  const cellBg = getCellBg(status, isSelected);

                  return (
                    <button
                      key={i}
                      onClick={() => (hasTask || day.isCurrentMonth) ? setSelectedDate(isSelected ? null : day.date) : undefined}
                      className={`
                        aspect-square rounded-xl flex items-center justify-center text-[13px] font-bold transition-all
                        ${!day.isCurrentMonth ? 'text-slate-300' : 'text-slate-700'}
                        ${day.isToday && !isSelected ? 'ring-2 ring-[#2ab4e8] ring-offset-1 text-[#0a5482] font-black' : ''}
                        ${cellBg}
                        ${day.isCurrentMonth && !isSelected ? 'hover:bg-sky-50 hover:text-[#0a5482] cursor-pointer' : ''}
                        ${!day.isCurrentMonth ? 'cursor-default' : ''}
                      `}
                    >
                      {day.day}
                    </button>
                  );
                })}
              </div>

              {/* LEGEND */}
              <div className="flex items-center justify-center gap-4 px-4 py-3.5 bg-slate-50/80 border-t border-slate-200/80 text-[11px] text-slate-600 font-bold">
                <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded-md bg-sky-100 border border-sky-300"></span> Đang giao</span>
                <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded-md bg-emerald-100 border border-emerald-300"></span> Hoàn thành</span>
                <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded-md bg-rose-100 border border-rose-300"></span> Quá hạn</span>
              </div>
            </div>
          </div>

          {/* ========== RIGHT: 2 COLUMNS (DANH SÁCH CÔNG VIỆC & DANH SÁCH BÀI TẬP) ========== */}
          <div className="flex-1 min-w-0 w-full grid grid-cols-1 md:grid-cols-2 gap-5 items-start">
            
            {/* ========== CỘT 1: CỘT CÔNG VIỆC (MANUAL TASKS) ========== */}
            <div className="bg-white rounded-2xl sm:rounded-3xl shadow-xs border border-slate-200/90 overflow-hidden flex flex-col h-[575px]">
              {/* Header Cột Công việc */}
              <div className="px-5 py-4 border-b border-slate-200/80 bg-slate-50/70 flex items-center justify-between shrink-0">
                <div className="flex items-center gap-3 min-w-0">
                  <span className="w-1.5 h-6 bg-[#0a5482] rounded-full shrink-0"></span>
                  <div className="w-9 h-9 rounded-xl bg-sky-50 border border-sky-200/80 text-[#0a5482] flex items-center justify-center text-base shadow-2xs shrink-0">
                    📋
                  </div>
                  <div className="min-w-0">
                    <h3 className="font-black text-slate-900 text-[15px] leading-tight truncate">
                      Danh sách Công Việc
                    </h3>
                    <p className="text-[11.5px] text-slate-500 font-medium mt-0.5 truncate">
                      Nhiệm vụ tự học, chép bài &amp; tài liệu
                    </p>
                  </div>
                </div>
                <span className="text-[11px] font-extrabold px-2.5 py-1 rounded-full bg-sky-50 text-[#0a5482] border border-sky-200/80 shrink-0">
                  {completedManualCount}/{selectedManualTasks.length} xong
                </span>
              </div>

              {/* Nội dung danh sách công việc */}
              <div className="flex-1 overflow-y-auto custom-scrollbar p-3.5 sm:p-4 space-y-3 bg-slate-50/40">
                {calendarMode === 'day' && !selectedDate ? (
                  <div className="h-full flex flex-col items-center justify-center text-center p-6 text-slate-400">
                    <span className="text-3xl mb-2">👈</span>
                    <p className="text-xs font-semibold">Chọn một ngày trên lịch để xem công việc</p>
                  </div>
                ) : selectedManualTasks.length === 0 ? (
                  <div className="h-full flex flex-col items-center justify-center text-center p-6 text-slate-400">
                    <span className="text-3xl mb-2">📭</span>
                    <p className="text-xs font-bold text-slate-600 mb-0.5">Không có công việc nào</p>
                    <p className="text-[11px] text-slate-400">{rangeLabel} không có nhiệm vụ tự học nào</p>
                  </div>
                ) : (
                  selectedManualTasks.map(task => (
                    <div 
                      key={task.id} 
                      className={`p-4 rounded-2xl border transition-all duration-200 ${
                        task._effectiveCompleted 
                          ? 'bg-emerald-50/40 border-emerald-200/90 shadow-2xs' 
                          : 'bg-white border-slate-200/90 hover:border-[#2ab4e8] hover:shadow-md shadow-2xs'
                      }`}
                    >
                      <div className="flex items-start gap-3">
                        <button
                          onClick={() => handleToggleComplete(task)}
                          disabled={task.is_completed || isUpdating === task.id}
                          className={`mt-0.5 w-5 h-5 rounded-full border-2 flex items-center justify-center transition-all shrink-0 cursor-pointer ${
                            task.is_completed 
                              ? 'bg-emerald-500 border-emerald-500 text-white' 
                              : task.student_completed 
                                ? 'bg-amber-100 border-amber-400 text-amber-600' 
                                : 'border-slate-300 hover:border-[#0a5482] bg-white text-transparent'
                          } ${isUpdating === task.id ? 'animate-pulse' : ''}`}
                          title={task.is_completed ? "Đã được giáo viên duyệt" : task.student_completed ? "Bấm để bỏ đánh dấu hoàn thành" : "Bấm để đánh dấu đã hoàn thành"}
                        >
                          {task.is_completed ? '✓' : task.student_completed ? '⏳' : ''}
                        </button>

                        <div className="flex-1 min-w-0">
                          <p className={`text-[14px] font-bold leading-snug ${
                            task._effectiveCompleted ? 'text-slate-400 line-through' : 'text-slate-800'
                          }`}>
                            {task.title}
                          </p>
                          {(() => {
                            const displayDesc = getDisplayDescription(task.description);
                            return displayDesc ? (
                              <p className="text-[12px] text-slate-500 mt-1 leading-relaxed">
                                {displayDesc}
                              </p>
                            ) : null;
                          })()}

                          {/* Thông tin ngày giao bài */}
                          {task._effectiveDueDate && (
                            <div className="flex items-center gap-1.5 text-[11px] text-slate-500 font-medium mt-1.5">
                              <span className="text-slate-400">📅 Ngày giao:</span>
                              <span className="font-bold text-slate-700">
                                {formatDateVN(task._effectiveDueDate)}
                              </span>
                              {task._effectiveDueDate !== task.due_date && (
                                <span className="text-[10px] font-bold text-emerald-700 bg-emerald-100 px-1.5 py-0.5 rounded">
                                  Đã hoàn thành sớm
                                </span>
                              )}
                            </div>
                          )}

                          {(() => {
                            const lecMeta = parseLectureFromItem(task, task.card_title, effectiveLectures);
                            return (
                              <div className="mt-3 flex items-center justify-between gap-2 flex-wrap">
                                <div className="flex items-center gap-2 flex-wrap">
                                  {task.is_completed && (
                                    <span className="text-[10px] font-extrabold bg-emerald-100 text-emerald-700 px-2.5 py-0.5 rounded-full">
                                      ✅ Đã duyệt
                                    </span>
                                  )}
                                  {task.student_completed && !task.is_completed && (
                                    <span className="text-[10px] font-extrabold bg-amber-100 text-amber-700 px-2.5 py-0.5 rounded-full">
                                      ⏳ Chờ giáo viên duyệt
                                    </span>
                                  )}
                                  {!task.student_completed && !task.is_completed && (
                                    <span className="text-[10px] font-bold bg-slate-100 text-slate-500 px-2.5 py-0.5 rounded-full">
                                      Chưa hoàn thành
                                    </span>
                                  )}
                                </div>
                                {lecMeta.isLecture && (
                                  <button
                                    type="button"
                                    onClick={(e) => {
                                      e.stopPropagation();
                                      onOpenLecture?.(lecMeta.courseId || undefined, lecMeta.lectureId || undefined);
                                    }}
                                    className="text-[11px] font-extrabold px-3 py-1.5 rounded-xl bg-sky-50 text-[#0a5482] hover:bg-[#0a5482] hover:text-white border border-sky-200/90 transition-all flex items-center gap-1.5 shrink-0 cursor-pointer shadow-2xs active:scale-95 ml-auto"
                                    title="Đi tới bài giảng này"
                                  >
                                    <span>📖</span>
                                    <span>Đến bài giảng →</span>
                                  </button>
                                )}
                              </div>
                            );
                          })()}
                        </div>
                      </div>
                    </div>
                  ))
                )}
              </div>
            </div>

            {/* ========== CỘT 2: CỘT BÀI TẬP (TEST / EXERCISE TASKS) ========== */}
            <div className="bg-white rounded-2xl sm:rounded-3xl shadow-xs border border-slate-200/90 overflow-hidden flex flex-col h-[575px]">
              {/* Header Cột Bài tập */}
              <div className="px-5 py-4 border-b border-slate-200/80 bg-slate-50/70 flex items-center justify-between shrink-0">
                <div className="flex items-center gap-3 min-w-0">
                  <span className="w-1.5 h-6 bg-[#2ab4e8] rounded-full shrink-0"></span>
                  <div className="w-9 h-9 rounded-xl bg-sky-50 border border-sky-200/80 text-[#0a5482] flex items-center justify-center text-base shadow-2xs shrink-0">
                    📚
                  </div>
                  <div className="min-w-0">
                    <h3 className="font-black text-slate-900 text-[15px] leading-tight truncate">
                      Danh sách Bài Tập
                    </h3>
                    <p className="text-[11.5px] text-slate-500 font-medium mt-0.5 truncate">
                      Bài tập trong kho đề (Cần đạt ≥ 50%)
                    </p>
                  </div>
                </div>
                <span className="text-[11px] font-extrabold px-2.5 py-1 rounded-full bg-sky-50 text-[#0a5482] border border-sky-200/80 shrink-0">
                  {completedTestCount}/{selectedTestTasks.length} xong
                </span>
              </div>

              {/* Nội dung danh sách bài tập */}
              <div className="flex-1 overflow-y-auto custom-scrollbar p-3.5 sm:p-4 space-y-3 bg-slate-50/40">
                {calendarMode === 'day' && !selectedDate ? (
                  <div className="h-full flex flex-col items-center justify-center text-center p-6 text-slate-400">
                    <span className="text-3xl mb-2">👈</span>
                    <p className="text-xs font-semibold">Chọn một ngày trên lịch để xem bài tập</p>
                  </div>
                ) : selectedTestTasks.length === 0 ? (
                  <div className="h-full flex flex-col items-center justify-center text-center p-6 text-slate-400">
                    <span className="text-3xl mb-2">📭</span>
                    <p className="text-xs font-bold text-slate-600 mb-0.5">Không có bài tập nào</p>
                    <p className="text-[11px] text-slate-400">{rangeLabel} không có bài tập trong kho</p>
                  </div>
                ) : (
                  selectedTestTasks.map(task => {
                    const testKey = task.test_id ? String(task.test_id) : null;
                    const titleKey = task.title ? task.title.trim().toLowerCase() : null;
                    const testScore = (testKey && latestTestScores.get(testKey)) || 
                                      (titleKey && latestTestScores.get(titleKey));
                    const isDone = task._effectiveCompleted;

                    return (
                      <div 
                        key={task.id} 
                        className={`p-4 rounded-2xl border transition-all duration-200 ${
                          isDone 
                            ? 'bg-emerald-50/40 border-emerald-200/90 shadow-2xs' 
                            : 'bg-white border-slate-200/90 hover:border-[#2ab4e8] hover:shadow-md shadow-2xs'
                        }`}
                      >
                        <div className="flex items-start gap-3">
                          {/* Đèn trạng thái cho bài tập trong kho */}
                          <div 
                            className={`mt-0.5 w-5 h-5 rounded-full border-2 flex items-center justify-center shrink-0 select-none text-[11px] ${
                              isDone 
                                ? 'bg-emerald-500 border-emerald-500 text-white' 
                                : 'bg-slate-50 border-slate-300 text-slate-400'
                            }`}
                            title={isDone ? "Bài tập đã nộp và đạt điểm yêu cầu (≥ 50%)" : "Cần nộp bài đạt từ 50% điểm trở lên"}
                          >
                            {isDone ? '✓' : '📝'}
                          </div>

                          <div className="flex-1 min-w-0">
                            <p className={`text-[14px] font-bold leading-snug ${
                              isDone ? 'text-slate-400 line-through' : 'text-slate-800'
                            }`}>
                              {task.title}
                            </p>
                            {task.description && (
                              <p className="text-[12px] text-slate-500 mt-1 leading-relaxed">
                                {task.description}
                              </p>
                            )}

                            {/* Thông tin ngày giao bài */}
                            {task._effectiveDueDate && (
                              <div className="flex items-center gap-1.5 text-[11px] text-slate-500 font-medium mt-1.5">
                                <span className="text-slate-400">📅 Ngày giao:</span>
                                <span className="font-bold text-slate-700">
                                  {formatDateVN(task._effectiveDueDate)}
                                </span>
                                {task._effectiveDueDate !== task.due_date && (
                                  <span className="text-[10px] font-bold text-emerald-700 bg-emerald-100 px-1.5 py-0.5 rounded">
                                    Đã hoàn thành sớm
                                  </span>
                                )}
                              </div>
                            )}

                            {/* Badge điểm thi & Nút hành động */}
                            <div className="mt-3 flex items-center justify-between gap-2 flex-wrap">
                              <div>
                                {isDone ? (
                                  <div className="flex items-center gap-1.5 flex-wrap">
                                    <span className="inline-flex items-center text-[10px] px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-extrabold">
                                      ✓ Đã đạt
                                    </span>
                                    {testScore && (
                                      <span 
                                        className="inline-flex items-center gap-1 text-[10.5px] px-2.5 py-0.5 rounded-full bg-sky-50 text-[#0a5482] font-black border border-sky-200/90 shadow-2xs"
                                        title={`Điểm làm gần đây: ${testScore.score}/${testScore.total_score} (${testScore.percent}%)`}
                                      >
                                        🎯 {testScore.total_score > 0 ? `${testScore.score}/${testScore.total_score}` : testScore.score}
                                        <span className="text-[9.5px] font-bold text-[#2ab4e8]">({testScore.percent}%)</span>
                                      </span>
                                    )}
                                  </div>
                                ) : testScore ? (
                                  <span className="inline-flex items-center gap-1 text-[10px] px-2.5 py-0.5 rounded-full bg-rose-100 text-rose-700 font-bold border border-rose-200">
                                    ⚠️ Chưa đạt: {testScore.total_score > 0 ? `${testScore.score}/${testScore.total_score}` : testScore.score} ({testScore.percent}%) • Cần ≥ 50%
                                  </span>
                                ) : (
                                  <span className="inline-flex items-center text-[10px] px-2.5 py-0.5 rounded-full bg-slate-100 text-slate-500 font-semibold">
                                    Chưa làm (Cần đạt ≥ 50%)
                                  </span>
                                )}
                              </div>

                              {/* Nút hành động */}
                              {isDone ? (
                                <button 
                                  onClick={() => task.test_id && onStartTest?.(task.test_id)}
                                  className="text-[11px] font-extrabold px-3 py-1.5 rounded-xl bg-emerald-50 hover:bg-emerald-600 text-emerald-700 hover:text-white border border-emerald-200 transition-colors flex items-center gap-1 shrink-0 cursor-pointer shadow-2xs"
                                  title="Làm lại bài thi này"
                                >
                                  <span>🔄</span> Làm lại
                                </button>
                              ) : testScore ? (
                                <button 
                                  onClick={() => task.test_id && onStartTest?.(task.test_id)}
                                  className="text-[11px] font-extrabold px-3.5 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-600 text-white transition-colors flex items-center gap-1 shrink-0 cursor-pointer shadow-xs"
                                  title="Làm lại để đạt điểm yêu cầu (≥ 50%)"
                                >
                                  Làm lại để đạt điểm →
                                </button>
                              ) : (
                                <button 
                                  onClick={() => task.test_id && onStartTest?.(task.test_id)}
                                  className="text-[11px] font-extrabold px-3.5 py-1.5 rounded-xl bg-[#0a5482] hover:bg-[#084266] text-white transition-colors flex items-center gap-1 shrink-0 cursor-pointer shadow-xs"
                                  title="Bắt đầu làm bài"
                                >
                                  Bắt đầu làm bài →
                                </button>
                              )}
                            </div>
                          </div>
                        </div>
                      </div>
                    );
                  })
                )}
              </div>
            </div>

          </div>
        </div>
      </div>
      
      <BoardThemeModal
        isOpen={isThemeModalOpen}
        currentTheme={calendarTheme}
        onSelectTheme={handleSelectCalendarTheme}
        onApplyCustomColor={handleApplyCustomCalendarColor}
        onClose={() => setIsThemeModalOpen(false)}
      />
    </div>
  );
}
