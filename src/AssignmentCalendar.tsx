import React, { useState, useMemo, useEffect } from 'react';
import { supabase } from './supabase';

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
  onRefresh: () => void;
  onStartTest?: (testId: string) => void;
}

const WEEKDAYS = ['CN', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7'];

export default function AssignmentCalendar({ assignments, completedTestIds, topActions, rightActions, courseTitle, onRefresh, onStartTest }: Props) {
  const [currentMonth, setCurrentMonth] = useState(new Date());
  const [selectedDate, setSelectedDate] = useState<string | null>(new Date().toISOString().split('T')[0]);
  const [isUpdating, setIsUpdating] = useState<string | null>(null);
  const [latestTestScores, setLatestTestScores] = useState<Map<string, { score: number; total_score: number; percent: number; isPassed: boolean }>>(new Map());

  // Tải điểm thi thực tế từ test_results
  useEffect(() => {
    const fetchScores = async () => {
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) return;
      const { data } = await supabase.from('test_results')
        .select('id, test_title, score, total_score, created_at, details')
        .eq('user_id', user.id)
        .order('created_at', { ascending: false });

      const scoreMap = new Map<string, { score: number; total_score: number; percent: number; isPassed: boolean }>();
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

        const scoreObj = { score, total_score: total, percent, isPassed };
        const registerScore = (key: string) => {
          const existing = scoreMap.get(key);
          if (!existing) {
            scoreMap.set(key, scoreObj);
          } else if (!existing.isPassed && isPassed) {
            scoreMap.set(key, scoreObj);
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
    window.addEventListener('focus', handleRefresh);
    return () => {
      window.removeEventListener('tony-refresh-lecture-progress', handleRefresh);
      window.removeEventListener('focus', handleRefresh);
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
  // TRẠNG THÁI TỪNG NGÀY
  // ============================================
  const dateStatusMap = useMemo(() => {
    const map: Record<string, 'blue' | 'green' | 'red'> = {};
    const today = new Date().toISOString().split('T')[0];

    // Group assignments by date
    const byDate: Record<string, Assignment[]> = {};
    assignments.forEach(a => {
      if (!byDate[a.due_date]) byDate[a.due_date] = [];
      byDate[a.due_date].push(a);
    });

    Object.entries(byDate).forEach(([date, tasks]) => {
      const allCompleted = tasks.every(t => {
        if (t.task_type === 'test') {
          const testKey = t.test_id ? String(t.test_id) : null;
          const scoreInfo = testKey ? latestTestScores.get(testKey) : null;
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
  }, [assignments, completedTestIds, latestTestScores]);

  // ============================================
  // TASKS CHO NGÀY ĐANG CHỌN
  // ============================================
  const selectedTasks = useMemo(() => {
    if (!selectedDate) return [];
    return assignments
      .filter(a => a.due_date === selectedDate)
      .map(a => {
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
          _effectiveCompleted: isDone
        };
      });
  }, [selectedDate, assignments, completedTestIds, latestTestScores]);

  // Tách thành 2 mảng riêng biệt: Cột Công việc (Manual) và Cột Bài tập (Test)
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
    
    // Update this specific task
    await supabase.from('assignments').update({
      student_completed: newVal,
      updated_at: new Date().toISOString()
    }).eq('id', task.id);
    
    // Also sync all matching assignments
    const syncPayload: any = { student_completed: newVal, updated_at: new Date().toISOString() };
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
  const goToday = () => { setCurrentMonth(new Date()); setSelectedDate(new Date().toISOString().split('T')[0]); };

  const monthLabel = currentMonth.toLocaleDateString('vi-VN', { month: 'long', year: 'numeric' });

  // Helper: get cell background based on status
  const getCellBg = (status: 'blue' | 'green' | 'red' | undefined, isSelected: boolean) => {
    if (isSelected) return 'bg-[#0ea5e9] text-white shadow-md scale-105';
    if (!status) return '';
    if (status === 'green') return 'bg-emerald-100 text-emerald-800 font-bold';
    if (status === 'red') return 'bg-rose-100 text-rose-700 font-bold';
    return 'bg-sky-100 text-sky-800 font-bold';
  };

  const headerActions = topActions || rightActions;

  const selectedDateFormatted = selectedDate 
    ? new Date(selectedDate + 'T00:00:00').toLocaleDateString('vi-VN', { day: 'numeric', month: 'long' })
    : null;

  const dayProgressPercent = selectedTasks.length > 0 
    ? Math.round((completedTotalCount / selectedTasks.length) * 100) 
    : 0;

  return (
    <div className="w-full min-h-[500px] bg-gradient-to-b from-[#e0f2fe] to-[#f0f9ff] p-3 sm:p-4 md:p-5 text-slate-800 rounded-3xl relative">
      <div className="w-full space-y-4">
        {headerActions && (
          <div className="flex justify-end relative z-40 mb-2">
            {headerActions}
          </div>
        )}

        {/* UNIFIED BLUE HEADER BANNER */}
        <div className="bg-gradient-to-r from-[#0ea5e9] to-[#38bdf8] rounded-2xl p-4 md:p-5 shadow-sm text-white flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="flex items-center gap-3">
            <span className="text-3xl">📅</span>
            <div>
              <h1 className="text-xl md:text-2xl font-bold tracking-tight">
                Lịch Báo Bài{courseTitle ? ` - ${courseTitle}` : ''}
              </h1>
              <p className="text-white/80 text-xs md:text-sm mt-0.5">
                Bấm vào ngày để xem và cập nhật tiến độ công việc
              </p>
            </div>
          </div>

          <div className="flex flex-col sm:flex-row items-center sm:items-end gap-3 sm:gap-4 w-full md:w-auto justify-between md:justify-end">
            {selectedDate && selectedTasks.length > 0 ? (
              <div className="flex flex-col items-center sm:items-end">
                <div className="text-sm text-white/90 font-medium mb-1">
                  Tiến độ ngày {selectedDateFormatted}: {completedTotalCount}/{selectedTasks.length} ({dayProgressPercent}%)
                </div>
                <div className="w-48 h-2 bg-white/20 rounded-full overflow-hidden">
                  <div 
                    className="h-full bg-white rounded-full transition-all duration-500"
                    style={{ width: `${dayProgressPercent}%` }}
                  />
                </div>
              </div>
            ) : selectedDate ? (
              <div className="text-xs text-white/80 font-medium">
                Ngày {selectedDateFormatted}: Không có công việc & bài tập
              </div>
            ) : (
              <div className="text-xs text-white/80 font-medium">
                Bấm vào một ngày trên lịch để xem công việc
              </div>
            )}

            <button 
              onClick={goToday} 
              className="bg-white/20 hover:bg-white/30 active:scale-95 text-white text-[13px] font-bold px-4 py-2 rounded-xl transition-all shadow-sm flex items-center gap-1.5 cursor-pointer shrink-0"
              title="Xem công việc hôm nay"
            >
              <span>🎯</span> <span>Hôm nay</span>
            </button>
          </div>
        </div>

        {/* 3-COLUMN CONTENT: CALENDAR (LEFT) & 2 COLUMNS (RIGHT: CỘT CÔNG VIỆC + CỘT BÀI TẬP) */}
        <div className="flex flex-col xl:flex-row gap-4 items-start w-full">
          
          {/* ========== LEFT: CALENDAR ========== */}
          <div className="w-full xl:w-[380px] 2xl:w-[410px] shrink-0">
            <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
              {/* MONTH NAV */}
              <div className="flex items-center justify-between px-5 py-3.5 border-b border-slate-100 bg-slate-50/70">
                <button onClick={prevMonth} className="w-8 h-8 rounded-full hover:bg-white border border-transparent hover:border-slate-200 flex items-center justify-center text-slate-500 transition-all shadow-sm cursor-pointer">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" /></svg>
                </button>
                <h3 className="font-black text-slate-800 text-[15px] capitalize tracking-tight flex items-center gap-1.5">
                  <span>🗓️</span> {monthLabel}
                </h3>
                <button onClick={nextMonth} className="w-8 h-8 rounded-full hover:bg-white border border-transparent hover:border-slate-200 flex items-center justify-center text-slate-500 transition-all shadow-sm cursor-pointer">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" /></svg>
                </button>
              </div>

              {/* WEEKDAY HEADERS */}
              <div className="grid grid-cols-7 px-3 pt-3 pb-1">
                {WEEKDAYS.map(d => (
                  <div key={d} className="text-center text-[11px] font-bold text-slate-400 uppercase">{d}</div>
                ))}
              </div>

              {/* CALENDAR GRID */}
              <div className="grid grid-cols-7 px-3 pb-3 gap-1">
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
                        aspect-square rounded-xl flex items-center justify-center text-[13px] font-semibold transition-all
                        ${!day.isCurrentMonth ? 'text-slate-300' : 'text-slate-700'}
                        ${day.isToday && !isSelected ? 'ring-2 ring-[#0ea5e9] ring-offset-1' : ''}
                        ${cellBg}
                        ${day.isCurrentMonth && !isSelected ? 'hover:bg-slate-100 cursor-pointer' : ''}
                        ${!day.isCurrentMonth ? 'cursor-default' : ''}
                      `}
                    >
                      {day.day}
                    </button>
                  );
                })}
              </div>

              {/* LEGEND */}
              <div className="flex items-center justify-center gap-4 px-4 py-3 bg-slate-50/50 border-t border-slate-100 text-[10px] text-slate-500 font-medium">
                <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-sky-100 border border-sky-300"></span> Chưa xong</span>
                <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-emerald-100 border border-emerald-300"></span> Hoàn thành</span>
                <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-rose-100 border border-rose-300"></span> Quá hạn</span>
              </div>
            </div>
          </div>

          {/* ========== RIGHT: 2 COLUMNS (CỘT CÔNG VIỆC & CỘT BÀI TẬP) ========== */}
          <div className="flex-1 min-w-0 w-full grid grid-cols-1 md:grid-cols-2 gap-4 items-start">
            
            {/* ========== CỘT 1: CỘT CÔNG VIỆC (MANUAL TASKS) ========== */}
            <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden flex flex-col h-[560px]">
              {/* Header Cột Công việc */}
              <div className="px-4 py-3.5 border-b border-slate-100 bg-gradient-to-r from-blue-50/70 to-sky-50/50 flex items-center justify-between shrink-0">
                <div className="flex items-center gap-2.5 min-w-0">
                  <div className="w-8 h-8 rounded-xl bg-sky-500 text-white flex items-center justify-center text-sm shadow-xs shrink-0">
                    📋
                  </div>
                  <div className="min-w-0">
                    <h3 className="font-black text-slate-800 text-[14.5px] leading-tight truncate">
                      Cột Công Việc
                    </h3>
                    <p className="text-[11px] text-slate-500 font-medium mt-0.5 truncate">
                      Nhiệm vụ tự học, chép bài, tài liệu
                    </p>
                  </div>
                </div>
                <span className="text-[11px] font-bold px-2.5 py-1 rounded-full bg-sky-100 text-sky-800 shrink-0">
                  {completedManualCount}/{selectedManualTasks.length} xong
                </span>
              </div>

              {/* Nội dung danh sách công việc (Scrollable giống Trello) */}
              <div className="flex-1 overflow-y-auto custom-scrollbar p-3 sm:p-4 space-y-2.5 bg-slate-50/40">
                {!selectedDate ? (
                  <div className="h-full flex flex-col items-center justify-center text-center p-6 text-slate-400">
                    <span className="text-3xl mb-2">👈</span>
                    <p className="text-xs font-semibold">Chọn một ngày trên lịch để xem công việc</p>
                  </div>
                ) : selectedManualTasks.length === 0 ? (
                  <div className="h-full flex flex-col items-center justify-center text-center p-6 text-slate-400">
                    <span className="text-3xl mb-2">📭</span>
                    <p className="text-xs font-bold text-slate-600 mb-0.5">Không có công việc nào</p>
                    <p className="text-[11px] text-slate-400">Ngày {selectedDateFormatted} không có nhiệm vụ chép bài nào</p>
                  </div>
                ) : (
                  selectedManualTasks.map(task => (
                    <div 
                      key={task.id} 
                      className={`p-3.5 rounded-xl border transition-all ${
                        task._effectiveCompleted 
                          ? 'bg-emerald-50/50 border-emerald-200 shadow-xs' 
                          : 'bg-white border-slate-200 hover:border-sky-300 shadow-xs'
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
                                : 'border-slate-300 hover:border-[#0ea5e9] bg-white text-transparent'
                          } ${isUpdating === task.id ? 'animate-pulse' : ''}`}
                          title={task.is_completed ? "Đã được giáo viên duyệt" : task.student_completed ? "Bấm để bỏ đánh dấu hoàn thành" : "Bấm để đánh dấu đã hoàn thành"}
                        >
                          {task.is_completed ? '✓' : task.student_completed ? '⏳' : ''}
                        </button>

                        <div className="flex-1 min-w-0">
                          <p className={`text-[13.5px] font-bold leading-snug ${
                            task._effectiveCompleted ? 'text-slate-400 line-through' : 'text-slate-800'
                          }`}>
                            {task.title}
                          </p>
                          {task.description && (
                            <p className="text-[11.5px] text-slate-500 mt-1 leading-relaxed">
                              {task.description}
                            </p>
                          )}
                          <div className="mt-2.5 flex items-center gap-2 flex-wrap">
                            {task.is_completed && (
                              <span className="text-[10px] font-bold bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-full">
                                ✅ Đã duyệt
                              </span>
                            )}
                            {task.student_completed && !task.is_completed && (
                              <span className="text-[10px] font-bold bg-amber-100 text-amber-700 px-2 py-0.5 rounded-full">
                                ⏳ Chờ giáo viên duyệt
                              </span>
                            )}
                            {!task.student_completed && !task.is_completed && (
                              <span className="text-[10px] font-bold bg-slate-100 text-slate-500 px-2 py-0.5 rounded-full">
                                Chưa hoàn thành
                              </span>
                            )}
                          </div>
                        </div>
                      </div>
                    </div>
                  ))
                )}
              </div>
            </div>

            {/* ========== CỘT 2: CỘT BÀI TẬP (TEST / EXERCISE TASKS) ========== */}
            <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden flex flex-col h-[560px]">
              {/* Header Cột Bài tập */}
              <div className="px-4 py-3.5 border-b border-slate-100 bg-gradient-to-r from-teal-50/70 to-emerald-50/50 flex items-center justify-between shrink-0">
                <div className="flex items-center gap-2.5 min-w-0">
                  <div className="w-8 h-8 rounded-xl bg-teal-600 text-white flex items-center justify-center text-sm shadow-xs shrink-0">
                    📚
                  </div>
                  <div className="min-w-0">
                    <h3 className="font-black text-slate-800 text-[14.5px] leading-tight truncate">
                      Cột Bài Tập
                    </h3>
                    <p className="text-[11px] text-slate-500 font-medium mt-0.5 truncate">
                      Bài tập trong kho (Cần đạt ≥ 50%)
                    </p>
                  </div>
                </div>
                <span className="text-[11px] font-bold px-2.5 py-1 rounded-full bg-teal-100 text-teal-800 shrink-0">
                  {completedTestCount}/{selectedTestTasks.length} xong
                </span>
              </div>

              {/* Nội dung danh sách bài tập (Scrollable giống Trello) */}
              <div className="flex-1 overflow-y-auto custom-scrollbar p-3 sm:p-4 space-y-2.5 bg-slate-50/40">
                {!selectedDate ? (
                  <div className="h-full flex flex-col items-center justify-center text-center p-6 text-slate-400">
                    <span className="text-3xl mb-2">👈</span>
                    <p className="text-xs font-semibold">Chọn một ngày trên lịch để xem bài tập</p>
                  </div>
                ) : selectedTestTasks.length === 0 ? (
                  <div className="h-full flex flex-col items-center justify-center text-center p-6 text-slate-400">
                    <span className="text-3xl mb-2">📭</span>
                    <p className="text-xs font-bold text-slate-600 mb-0.5">Không có bài tập nào</p>
                    <p className="text-[11px] text-slate-400">Ngày {selectedDateFormatted} không có bài tập trong kho</p>
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
                        className={`p-3.5 rounded-xl border transition-all ${
                          isDone 
                            ? 'bg-emerald-50/50 border-emerald-200 shadow-xs' 
                            : 'bg-white border-slate-200 hover:border-teal-300 shadow-xs'
                        }`}
                      >
                        <div className="flex items-start gap-3">
                          {/* Đèn trạng thái cho bài tập trong kho (Không cho tick thủ công) */}
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
                            <p className={`text-[13.5px] font-bold leading-snug ${
                              isDone ? 'text-slate-400 line-through' : 'text-slate-800'
                            }`}>
                              {task.title}
                            </p>
                            {task.description && (
                              <p className="text-[11.5px] text-slate-500 mt-1 leading-relaxed">
                                {task.description}
                              </p>
                            )}

                            {/* Badge điểm thi & Nút hành động */}
                            <div className="mt-2.5 flex items-center justify-between gap-2 flex-wrap">
                              <div>
                                {isDone ? (
                                  <div className="flex items-center gap-1.5 flex-wrap">
                                    <span className="inline-flex items-center text-[10px] px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-bold">
                                      ✓ Đã đạt
                                    </span>
                                    {testScore && (
                                      <span 
                                        className="inline-flex items-center gap-1 text-[10.5px] px-2 py-0.5 rounded-full bg-sky-100 text-sky-700 font-black border border-sky-200 shadow-xs"
                                        title={`Điểm làm gần đây: ${testScore.score}/${testScore.total_score} (${testScore.percent}%)`}
                                      >
                                        🎯 {testScore.total_score > 0 ? `${testScore.score}/${testScore.total_score}` : testScore.score}
                                        <span className="text-[9.5px] font-bold text-sky-600">({testScore.percent}%)</span>
                                      </span>
                                    )}
                                  </div>
                                ) : testScore ? (
                                  <span className="inline-flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-rose-100 text-rose-700 font-bold border border-rose-200">
                                    ⚠️ Chưa đạt: {testScore.total_score > 0 ? `${testScore.score}/${testScore.total_score}` : testScore.score} ({testScore.percent}%) • Cần ≥ 50%
                                  </span>
                                ) : (
                                  <span className="inline-flex items-center text-[10px] px-2 py-0.5 rounded-full bg-slate-100 text-slate-500 font-medium">
                                    Chưa làm (Cần đạt ≥ 50%)
                                  </span>
                                )}
                              </div>

                              {/* Nút hành động */}
                              {isDone ? (
                                <button 
                                  onClick={() => task.test_id && onStartTest?.(task.test_id)}
                                  className="text-[11px] font-bold px-3 py-1 rounded-lg bg-emerald-100 hover:bg-emerald-200 text-emerald-800 transition-colors flex items-center gap-1 shrink-0 cursor-pointer shadow-xs"
                                  title="Làm lại bài thi này"
                                >
                                  <span>🔄</span> Làm lại
                                </button>
                              ) : testScore ? (
                                <button 
                                  onClick={() => task.test_id && onStartTest?.(task.test_id)}
                                  className="text-[11px] font-bold px-3 py-1 rounded-lg bg-amber-500 hover:bg-amber-600 text-white transition-colors flex items-center gap-1 shrink-0 cursor-pointer shadow-xs"
                                  title="Làm lại để đạt điểm yêu cầu (≥ 50%)"
                                >
                                  Làm lại để đạt điểm ➜
                                </button>
                              ) : (
                                <button 
                                  onClick={() => task.test_id && onStartTest?.(task.test_id)}
                                  className="text-[11px] font-bold px-3 py-1 rounded-lg bg-[#0ea5e9] hover:bg-[#0284c7] text-white transition-colors flex items-center gap-1 shrink-0 cursor-pointer shadow-xs"
                                  title="Bắt đầu làm bài"
                                >
                                  Bắt đầu làm bài ➜
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
    </div>
  );
}
