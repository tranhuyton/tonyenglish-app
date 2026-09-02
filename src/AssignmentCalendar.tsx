import React, { useState, useMemo } from 'react';
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
  created_at: string;
}

interface Props {
  assignments: Assignment[];
  completedTestIds: Set<string>;
  onRefresh: () => void;
  onStartTest?: (testId: string) => void;
}

const WEEKDAYS = ['CN', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7'];

export default function AssignmentCalendar({ assignments, completedTestIds, onRefresh, onStartTest }: Props) {
  const [currentMonth, setCurrentMonth] = useState(new Date());
  const [selectedDate, setSelectedDate] = useState<string | null>(new Date().toISOString().split('T')[0]);
  const [isUpdating, setIsUpdating] = useState<string | null>(null);

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
        if (t.task_type === 'test' && t.test_id) {
          return t.is_completed || completedTestIds.has(t.test_id);
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
  }, [assignments, completedTestIds]);

  // ============================================
  // TASKS CHO NGÀY ĐANG CHỌN
  // ============================================
  const selectedTasks = useMemo(() => {
    if (!selectedDate) return [];
    return assignments
      .filter(a => a.due_date === selectedDate)
      .map(a => ({
        ...a,
        _effectiveCompleted: a.task_type === 'test' && a.test_id
          ? (a.is_completed || completedTestIds.has(a.test_id))
          : (a.is_completed || a.student_completed)
      }));
  }, [selectedDate, assignments, completedTestIds]);

  const completedCount = selectedTasks.filter(t => t._effectiveCompleted).length;

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
    
    // Also sync all matching assignments (same title, same user, same task_type)
    const syncPayload: any = { student_completed: newVal, updated_at: new Date().toISOString() };
    if (!newVal) syncPayload.admin_approved = false; // Reset approval when un-completing
    await supabase.from('assignments').update(syncPayload)
      .eq('user_id', task.user_id)
      .eq('title', task.title)
      .eq('task_type', 'manual');

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
    if (status === 'green') return 'bg-emerald-100 text-emerald-800';
    if (status === 'red') return 'bg-red-100 text-red-700';
    return 'bg-sky-100 text-sky-800';
  };

  // ============================================
  // RENDER
  // ============================================
  return (
    <div className="flex gap-6 items-start max-w-5xl mx-auto">
      {/* ========== LEFT: CALENDAR ========== */}
      <div className="w-[420px] shrink-0">
        <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
          <div className="bg-gradient-to-r from-[#0ea5e9] to-[#0284c7] px-5 py-4 flex items-center justify-between">
            <div>
              <h2 className="text-white font-black text-lg">📅 Lịch Báo Bài</h2>
              <p className="text-white/70 text-[11px] mt-0.5">Bấm vào ngày để xem công việc</p>
            </div>
            <button onClick={goToday} className="bg-white/20 hover:bg-white/30 text-white text-[11px] font-bold px-3 py-1.5 rounded-full transition-all">
              Hôm nay
            </button>
          </div>

          {/* MONTH NAV */}
          <div className="flex items-center justify-between px-5 py-3 border-b border-slate-100">
            <button onClick={prevMonth} className="w-8 h-8 rounded-full hover:bg-slate-100 flex items-center justify-center text-slate-500 transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" /></svg>
            </button>
            <h3 className="font-black text-slate-800 text-[15px] capitalize">{monthLabel}</h3>
            <button onClick={nextMonth} className="w-8 h-8 rounded-full hover:bg-slate-100 flex items-center justify-center text-slate-500 transition-colors">
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
          <div className="flex items-center justify-center gap-5 px-4 pb-3 text-[10px] text-slate-400">
            <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-sky-100 border border-sky-300"></span> Chưa xong</span>
            <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-emerald-100 border border-emerald-300"></span> Hoàn thành</span>
            <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-red-100 border border-red-300"></span> Quá hạn</span>
          </div>
        </div>
      </div>

      {/* ========== RIGHT: TASKS PANEL ========== */}
      <div className="flex-1 min-w-0">
        {selectedDate && selectedTasks.length > 0 ? (
          <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
            <div className="px-5 py-4 border-b border-slate-100">
              <h3 className="font-black text-slate-800 text-[15px]">
                📋 Công việc ngày {new Date(selectedDate + 'T00:00:00').toLocaleDateString('vi-VN', { day: 'numeric', month: 'long' })}
              </h3>
              <p className="text-[12px] text-slate-400 mt-0.5">
                Hoàn thành: <span className={`font-bold ${completedCount === selectedTasks.length ? 'text-emerald-600' : 'text-[#0ea5e9]'}`}>{completedCount}/{selectedTasks.length}</span>
              </p>
            </div>

            <div className="divide-y divide-slate-100 max-h-[500px] overflow-y-auto">
              {selectedTasks.map(task => (
                <div key={task.id} className={`px-5 py-4 flex items-start gap-3 transition-colors ${task._effectiveCompleted ? 'bg-emerald-50/50' : ''}`}>
                  {/* CHECKBOX / STATUS */}
                  <div className="pt-0.5 shrink-0">
                    {task.task_type === 'manual' ? (
                      <button
                        onClick={() => handleToggleComplete(task)}
                        disabled={task.is_completed || isUpdating === task.id}
                        className={`w-6 h-6 rounded-lg border-2 flex items-center justify-center transition-all ${
                          task.is_completed ? 'bg-emerald-500 border-emerald-500 text-white' :
                          task.student_completed ? 'bg-amber-100 border-amber-400 text-amber-600' :
                          'border-slate-300 hover:border-[#0ea5e9] text-transparent hover:text-slate-300'
                        } ${isUpdating === task.id ? 'animate-pulse' : ''}`}
                      >
                        {task.is_completed ? '✓' : task.student_completed ? '⏳' : '✓'}
                      </button>
                    ) : (
                      <div className={`w-6 h-6 rounded-lg flex items-center justify-center text-[12px] ${
                        task._effectiveCompleted ? 'bg-emerald-500 text-white' : 'bg-slate-100 text-slate-400'
                      }`}>
                        {task._effectiveCompleted ? '✓' : '📝'}
                      </div>
                    )}
                  </div>

                  {/* CONTENT */}
                  <div className="flex-1 min-w-0">
                    <p className={`text-[14px] font-bold ${task._effectiveCompleted ? 'text-slate-400 line-through' : 'text-slate-800'}`}>
                      {task.title}
                    </p>
                    {task.description && (
                      <p className="text-[12px] text-slate-400 mt-0.5">{task.description}</p>
                    )}
                    {/* Status badge */}
                    <div className="mt-2 flex items-center gap-2">
                      {task.task_type === 'manual' && (
                        <>
                          {task.is_completed && (
                            <span className="text-[10px] font-bold bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-full">✅ Đã duyệt</span>
                          )}
                          {task.student_completed && !task.is_completed && (
                            <span className="text-[10px] font-bold bg-amber-100 text-amber-700 px-2 py-0.5 rounded-full">⏳ Chờ giáo viên duyệt</span>
                          )}
                          {!task.student_completed && !task.is_completed && (
                            <span className="text-[10px] font-bold bg-slate-100 text-slate-500 px-2 py-0.5 rounded-full">Chưa hoàn thành</span>
                          )}
                        </>
                      )}
                      {task.task_type === 'test' && (
                        <>
                          {task._effectiveCompleted ? (
                            <span className="text-[10px] font-bold bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-full">✅ Đã nộp bài</span>
                          ) : (
                            <button 
                              onClick={() => task.test_id && onStartTest?.(task.test_id)}
                              className="text-[10px] font-bold bg-[#0ea5e9]/10 text-[#0ea5e9] px-3 py-1 rounded-full hover:bg-[#0ea5e9]/20 transition-colors"
                            >
                              📝 Vào làm bài →
                            </button>
                          )}
                        </>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        ) : selectedDate ? (
          <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 text-center">
            <span className="text-4xl block mb-3">📭</span>
            <h3 className="font-bold text-slate-500 text-[14px] mb-1">Không có công việc</h3>
            <p className="text-[12px] text-slate-400">
              Ngày {new Date(selectedDate + 'T00:00:00').toLocaleDateString('vi-VN', { day: 'numeric', month: 'long' })} chưa có bài tập nào
            </p>
          </div>
        ) : (
          <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 text-center">
            <span className="text-4xl block mb-3">👈</span>
            <h3 className="font-bold text-slate-500 text-[14px]">Chọn ngày trên lịch để xem công việc</h3>
          </div>
        )}

        {/* EMPTY STATE - no assignments at all */}
        {assignments.length === 0 && (
          <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 text-center">
            <span className="text-4xl block mb-3">📭</span>
            <h3 className="font-bold text-slate-600 text-[15px] mb-1">Chưa có bài tập nào được giao</h3>
            <p className="text-[12px] text-slate-400">Giáo viên sẽ giao bài cho bạn trên lịch này. Hãy kiểm tra thường xuyên nhé!</p>
          </div>
        )}
      </div>
    </div>
  );
}
