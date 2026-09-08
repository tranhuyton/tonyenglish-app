import { useState, useEffect, useMemo } from 'react';
import { supabase } from './supabase';

interface Assignment {
  id: string;
  category: string;
  card_title: string;
  card_order: number;
  title: string;
  student_completed: boolean;
  is_completed: boolean;
  task_type: 'manual' | 'test';
  test_id?: string;
  user_id: string;
  board_template_id?: string;
  board_template_title?: string;
  admin_approved?: boolean;
  due_date?: string;
}

interface CardData {
  title: string;
  order: number;
  items: Assignment[];
  completedCount: number;
  totalCount: number;
}

interface ColumnData {
  name: string;
  cards: CardData[];
}

export default function TaskBoard({ userId, filterCourseId = 'all', filterElement, onStartTest }: { userId: string; filterCourseId?: string; filterElement?: React.ReactNode; onStartTest?: (testId: string) => void }) {
  const [assignments, setAssignments] = useState<Assignment[]>([]);
  const [boardTemplates, setBoardTemplates] = useState<any[]>([]);
  const [boardColumns, setBoardColumns] = useState<any[]>([]);
  const [completedTestIds, setCompletedTestIds] = useState<Set<string>>(new Set());
  const [inProgressTestIds, setInProgressTestIds] = useState<Set<string>>(new Set());
  const [loading, setLoading] = useState(true);
  const [expandedCards, setExpandedCards] = useState<Set<string>>(new Set());

  useEffect(() => {
    fetchAssignments();
  }, [userId]);

  const fetchAssignments = async () => {
    try {
      setLoading(true);
      
      const [bRes, colRes, assignRes, trRes] = await Promise.all([
        supabase.from('board_templates').select('id, title, course_id'),
        supabase.from('board_columns').select('*').order('order_index', { ascending: true }),
        supabase.from('assignments').select('*').eq('user_id', userId).not('category', 'is', null),
        supabase.from('test_results').select('test_id, details').eq('user_id', userId)
      ]);

      setBoardTemplates(bRes.data || []);
      setBoardColumns(colRes.data || []);

      const cSet = new Set<string>();
      (trRes.data || []).forEach((r: any) => {
        if (r.test_id) cSet.add(String(r.test_id));
        let d = r.details;
        if (typeof d === 'string') {
          try { d = JSON.parse(d); } catch (e) {}
        }
        if (d?.test_id) cSet.add(String(d.test_id));
      });
      setCompletedTestIds(cSet);

      const inProg = new Set<string>();
      try {
        for (let i = 0; i < localStorage.length; i++) {
          const key = localStorage.key(i);
          if (!key) continue;
          let match = key.match(/^(?:ielts_ans_|ielts_paper_ans_|std_ans_|case_study_ans_|igcse_ans_)(.+)$/);
          if (match) {
            const data = localStorage.getItem(key);
            if (data && Object.keys(JSON.parse(data)).length > 0) inProg.add(match[1]);
          } else {
            match = key.match(/^(?:ielts_endtime_|standard_endtime_|case_study_endtime_|ielts_paper_endtime_|igcse_endtime_)(.+)$/);
            if (match) {
              const endTime = parseInt(localStorage.getItem(key) || '0');
              if (endTime > Date.now()) inProg.add(match[1]);
            }
          }
        }
      } catch (e) {}
      setInProgressTestIds(inProg);

      setAssignments(assignRes.data || []);
      
    } catch (error) {
      console.error('[TaskBoard] Error fetching assignments:', error);
    } finally {
      setLoading(false);
    }
  };


  const toggleTask = async (task: Assignment) => {
    if (task.task_type !== 'manual') return;

    try {
      const newStatus = !task.student_completed;
      
      // Update this specific task
      const { error } = await supabase
        .from('assignments')
        .update({ student_completed: newStatus })
        .eq('id', task.id);

      if (error) throw error;

      // Also sync all matching assignments (same title, same user, same task_type)
      const updatePayload: any = { student_completed: newStatus };
      if (!newStatus) updatePayload.admin_approved = false; // Reset approval when un-completing
      await supabase
        .from('assignments')
        .update(updatePayload)
        .eq('user_id', userId)
        .eq('title', task.title)
        .eq('task_type', 'manual');

      // Update local state
      setAssignments(prev => prev.map(a => 
        (a.title === task.title && a.task_type === 'manual') ? { ...a, student_completed: newStatus } : a
      ));
    } catch (error) {
      console.error('Error toggling task:', error);
      alert('Không thể cập nhật trạng thái công việc. Vui lòng thử lại.');
    }
  };

  const toggleCardExpand = (cardId: string) => {
    setExpandedCards(prev => {
      const next = new Set(prev);
      if (next.has(cardId)) {
        next.delete(cardId);
      } else {
        next.add(cardId);
      }
      return next;
    });
  };

  const boardsData = useMemo(() => {
    const boardTitles = [...new Set(assignments.map(a => a.board_template_title).filter(Boolean))] as string[];
    
    const filteredTitles = boardTitles.filter(bt => {
      if (!filterCourseId || filterCourseId === 'all') return true;
      const tpl = boardTemplates.find(t => t.title === bt);
      return tpl && String(tpl.course_id) === String(filterCourseId);
    });

    return filteredTitles.map(boardTitle => {
      const boardAssignments = assignments.filter(a => a.board_template_title === boardTitle);
      
      const columnsMap = new Map<string, Map<string, Assignment[]>>();
      boardAssignments.forEach(task => {
        if (!columnsMap.has(task.category)) columnsMap.set(task.category, new Map());
        const categoryMap = columnsMap.get(task.category)!;
        if (!categoryMap.has(task.card_title)) categoryMap.set(task.card_title, []);
        categoryMap.get(task.card_title)!.push(task);
      });

      let totalItems = 0;
      let totalCompleted = 0;

      const columns: ColumnData[] = Array.from(columnsMap.entries()).map(([category, cardsMap]) => {
        const cards: CardData[] = Array.from(cardsMap.entries()).map(([cardTitle, items]) => {
          const sortedItems = [...items].sort((a, b) => (a.order_index || 0) - (b.order_index || 0));
          const cardOrder = (items[0]?.card_order != null && items[0]?.card_order !== 0) 
            ? items[0].card_order 
            : (cardTitle.toLowerCase().startsWith('công việc') ? 1 : cardTitle.toLowerCase().startsWith('bài tập') ? 2 : 3);
          const completedCount = sortedItems.filter(i => {
            if (i.task_type === 'test') {
              return i.is_completed || (i.test_id && completedTestIds.has(String(i.test_id)));
            }
            return i.student_completed;
          }).length;
          totalItems += sortedItems.length;
          totalCompleted += completedCount;
          return { title: cardTitle, order: cardOrder, items: sortedItems, completedCount, totalCount: sortedItems.length };
        }).sort((a, b) => a.order - b.order);
        return { name: category, cards };
      });

      // Sort columns: Topic 1 -> 10 strictly, then Exam practice ALWAYS at the very end
      const getColumnWeight = (catName: string) => {
        const norm = catName.trim().toLowerCase();
        // Exam practice & Past papers ALWAYS at the very end
        if (norm.includes('exam practice') || norm.includes('past paper') || norm.includes('đề thi')) {
          return 999999;
        }
        // Topic 1 to 10 in numeric order
        const match = norm.match(/topic\s*(\d+)/i);
        if (match) {
          return parseInt(match[1], 10);
        }
        // Matching board_columns order_index
        const bc = boardColumns.find(c => c.title && c.title.trim().toLowerCase() === norm);
        if (bc && bc.order_index != null) {
          return 1000 + bc.order_index;
        }
        return 50000;
      };

      columns.sort((a, b) => getColumnWeight(a.name) - getColumnWeight(b.name));

      const overallProgress = totalItems > 0 ? Math.round((totalCompleted / totalItems) * 100) : 0;
      
      return { title: boardTitle, overallProgress, totalCompleted, totalItems, columns };
    });
  }, [assignments, filterCourseId, boardTemplates, boardColumns, completedTestIds]);

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-b from-[#e0f2fe] to-[#f0f9ff] flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-4 border-[#0ea5e9] border-t-transparent"></div>
      </div>
    );
  }

  if (boardsData.length === 0) {
    return (
      <div className="min-h-screen bg-gradient-to-b from-[#e0f2fe] to-[#f0f9ff] p-4 md:p-6 flex flex-col items-start justify-start rounded-3xl">
        <div className="w-full max-w-[1600px] mx-auto flex justify-end mb-4 relative z-40">
          {filterElement}
        </div>
        <div className="p-12 mx-auto text-center bg-white/80 backdrop-blur rounded-2xl shadow-sm border border-slate-200 m-6 mt-12 w-full max-w-lg relative z-10">
          <span className="text-5xl block mb-4">📋</span>
          <h3 className="text-xl font-medium text-slate-700 mb-2">Chưa có bảng công việc nào</h3>
          <p className="text-slate-500">Hãy chọn một khóa học khác hoặc liên hệ giáo viên để được giao bảng công việc.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-[500px] bg-gradient-to-b from-[#e0f2fe] to-[#f0f9ff] p-4 md:p-6 text-slate-800 rounded-3xl relative">
      <div className="max-w-[1600px] mx-auto space-y-12">
        {filterElement && (
          <div className="flex justify-end mb-[-1.5rem] relative z-40">
            {filterElement}
          </div>
        )}
        {boardsData.map(board => (
          <div key={board.title}>
            {/* Header */}
            <div className="bg-gradient-to-r from-[#0ea5e9] to-[#38bdf8] rounded-2xl p-4 md:p-6 mb-6 shadow-sm text-white flex flex-col md:flex-row justify-between items-center gap-4">
              <div className="flex items-center gap-3">
                <span className="text-2xl">📋</span>
                <h1 className="text-xl font-bold tracking-tight">Bảng Công Việc - {board.title}</h1>
              </div>
              <div className="flex flex-col items-end">
                <div className="text-sm text-white/90 font-medium mb-1">
                  Tổng tiến độ: {board.overallProgress}%
                </div>
                <div className="w-48 h-2 bg-white/20 rounded-full overflow-hidden">
                  <div 
                    className="h-full bg-white rounded-full transition-all duration-500"
                    style={{ width: `${board.overallProgress}%` }}
                  />
                </div>
                <div className="text-xs text-white/70 mt-1">
                  Đã hoàn thành {board.totalCompleted}/{board.totalItems}
                </div>
              </div>
            </div>

            {/* Board */}
            <div className="flex flex-col md:flex-row gap-6 overflow-x-auto pb-8 snap-x items-start">
              {board.columns.map(col => (
                <div 
                  key={col.name} 
                  className="flex-none w-full md:w-80 lg:w-[350px] bg-white/80 backdrop-blur rounded-2xl shadow-sm border border-slate-200 p-4 snap-start flex flex-col h-fit"
                >
                  <div className="flex justify-between items-center mb-4 px-2">
                    <h2 className="font-bold text-lg text-slate-700">{col.name}</h2>
                    <span className="bg-slate-100 text-slate-600 text-xs font-medium px-2.5 py-1 rounded-full">
                      {col.cards.length} thẻ
                    </span>
                  </div>
              
              <div className="flex flex-col gap-3">
                {col.cards.map(card => {
                  const cardId = `${col.name}-${card.title}`;
                  const isExpanded = expandedCards.has(cardId);
                  const progressPct = card.totalCount > 0 ? Math.round((card.completedCount / card.totalCount) * 100) : 0;

                  return (
                    <div key={card.title} className="bg-white rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow overflow-hidden">
                      <div 
                        className="p-4 cursor-pointer select-none group"
                        onClick={() => toggleCardExpand(cardId)}
                      >
                        <div className="flex justify-between items-start mb-2">
                          <h3 className="font-semibold text-slate-800 text-sm leading-tight group-hover:text-[#0ea5e9] transition-colors">{card.title}</h3>
                          {isExpanded ? (
                            <span className="text-slate-400 text-xs">▲</span>
                          ) : (
                            <span className="text-slate-400 text-xs">▼</span>
                          )}
                        </div>
                        
                        <div className="flex items-center gap-2">
                          <div className="flex-1 h-1.5 bg-slate-100 rounded-full overflow-hidden">
                            <div 
                              className="h-full bg-emerald-500 rounded-full transition-all duration-300"
                              style={{ width: `${progressPct}%` }}
                            />
                          </div>
                          <div className="flex items-center gap-1 shrink-0">
                            <span className="text-xs font-bold text-emerald-600">
                              {progressPct}%
                            </span>
                            <span className="text-[11px] font-medium text-slate-400">
                              ({card.completedCount}/{card.totalCount})
                            </span>
                          </div>
                        </div>
                      </div>

                      {isExpanded && (
                        <div className="px-4 pb-4 border-t border-slate-50 bg-slate-50/50">
                          <div className="mt-3 flex flex-col gap-2">
                            {card.items.map(item => {
                              const isTest = item.task_type === 'test';
                              const isItemDone = isTest 
                                ? (item.is_completed || (item.test_id && completedTestIds.has(String(item.test_id))))
                                : item.student_completed;
                              const isItemInProgress = isTest && !isItemDone && item.test_id && inProgressTestIds.has(String(item.test_id));

                              if (isTest) {
                                return (
                                  <div 
                                    key={item.id} 
                                    className={`p-3 rounded-xl border transition-all cursor-pointer select-none ${
                                      isItemDone 
                                        ? 'bg-emerald-50/50 border-emerald-200 hover:border-emerald-300' 
                                        : isItemInProgress 
                                          ? 'bg-amber-50/50 border-amber-200 hover:border-amber-300 shadow-sm' 
                                          : 'bg-white border-slate-200 hover:border-sky-300 hover:bg-sky-50/20 shadow-sm'
                                    }`}
                                    onClick={() => {
                                      if (item.test_id && onStartTest) onStartTest(item.test_id);
                                    }}
                                  >
                                    <div className="flex items-start gap-2.5">
                                      <div className="mt-0.5 shrink-0 text-base">
                                        {isItemDone ? (
                                          <span className="text-emerald-500 font-bold">✅</span>
                                        ) : isItemInProgress ? (
                                          <span className="text-amber-500">⏳</span>
                                        ) : (
                                          <span className="text-sky-500">📝</span>
                                        )}
                                      </div>
                                      <div className="flex-1 min-w-0">
                                        <div className="flex items-baseline justify-between gap-1">
                                          <p className={`text-xs font-bold leading-snug ${
                                            isItemDone ? 'text-slate-600' : 'text-slate-800'
                                          }`}>
                                            {item.title}
                                          </p>
                                          {item.due_date && (
                                            <span className="text-[10px] text-slate-400 shrink-0 ml-2">
                                              {new Date(item.due_date + 'T00:00:00').toLocaleDateString('vi-VN', {day:'numeric', month:'short'})}
                                            </span>
                                          )}
                                        </div>

                                        <div className="mt-2.5 flex items-center justify-between gap-2 flex-wrap">
                                          <div>
                                            {isItemDone ? (
                                              <span className="inline-flex items-center text-[10px] px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-bold">
                                                ✓ Hoàn thành
                                              </span>
                                            ) : isItemInProgress ? (
                                              <span className="inline-flex items-center text-[10px] px-2 py-0.5 rounded-full bg-amber-100 text-amber-700 font-bold">
                                                ⏳ Đang làm dở
                                              </span>
                                            ) : (
                                              <span className="inline-flex items-center text-[10px] px-2 py-0.5 rounded-full bg-slate-100 text-slate-500 font-medium">
                                                Chưa làm
                                              </span>
                                            )}
                                          </div>

                                          {isItemDone ? (
                                            <button 
                                              onClick={(e) => {
                                                e.stopPropagation();
                                                if (item.test_id && onStartTest) onStartTest(item.test_id);
                                              }}
                                              className="text-[11px] font-bold px-3 py-1 rounded-lg bg-emerald-100 hover:bg-emerald-200 text-emerald-800 transition-colors flex items-center gap-1 shrink-0 shadow-sm"
                                              title="Làm lại bài thi này"
                                            >
                                              <span>🔄</span> Làm lại
                                            </button>
                                          ) : isItemInProgress ? (
                                            <button 
                                              onClick={(e) => {
                                                e.stopPropagation();
                                                if (item.test_id && onStartTest) onStartTest(item.test_id);
                                              }}
                                              className="text-[11px] font-bold px-3 py-1 rounded-lg bg-amber-500 hover:bg-amber-600 text-white shadow-sm transition-all flex items-center gap-1 shrink-0"
                                              title="Làm tiếp bài đang làm dở"
                                            >
                                              Làm tiếp ➜
                                            </button>
                                          ) : (
                                            <button 
                                              onClick={(e) => {
                                                e.stopPropagation();
                                                if (item.test_id && onStartTest) onStartTest(item.test_id);
                                              }}
                                              className="text-[11px] font-bold px-3 py-1 rounded-lg bg-[#0ea5e9] hover:bg-[#0284c7] text-white shadow-sm transition-all flex items-center gap-1 shrink-0"
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
                              }

                              return (
                                <div 
                                  key={item.id} 
                                  className={`flex items-start gap-3 p-2.5 rounded-xl border transition-all cursor-pointer select-none ${
                                    isItemDone 
                                      ? 'bg-slate-50/70 border-slate-200/80 opacity-75' 
                                      : 'bg-white border-slate-200 hover:border-sky-300 hover:bg-sky-50/20 shadow-sm'
                                  }`}
                                  onClick={() => toggleTask(item)}
                                >
                                  <div className="mt-0.5 shrink-0">
                                    {isItemDone ? (
                                      <div className="w-5 h-5 rounded-md bg-emerald-500 text-white flex items-center justify-center text-xs font-black shadow-sm">
                                        ✓
                                      </div>
                                    ) : (
                                      <div className="w-5 h-5 rounded-md border-2 border-slate-300 bg-white hover:border-[#0ea5e9] hover:bg-sky-50 transition-all flex items-center justify-center shadow-sm">
                                      </div>
                                    )}
                                  </div>
                                  <div className="flex flex-col gap-0.5 w-full min-w-0">
                                    <div className="flex items-baseline justify-between gap-1">
                                      <span className={`text-xs font-semibold leading-snug ${
                                        isItemDone ? 'line-through text-slate-400' : 'text-slate-700'
                                      }`}>
                                        {item.title}
                                      </span>
                                      {item.due_date && (
                                        <span className="text-[10px] text-slate-400 shrink-0 whitespace-nowrap">
                                          {new Date(item.due_date + 'T00:00:00').toLocaleDateString('vi-VN', {day:'numeric', month:'short'})}
                                        </span>
                                      )}
                                    </div>
                                    <div className="mt-1 flex flex-wrap gap-1">
                                      {isItemDone && item.admin_approved && (
                                        <span className="text-[10px] px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-bold">✅ Đã hoàn thành</span>
                                      )}
                                      {isItemDone && !item.admin_approved && (
                                        <span className="text-[10px] px-2 py-0.5 rounded-full bg-amber-100 text-amber-700 font-bold">⏳ Chờ giáo viên phê duyệt</span>
                                      )}
                                      {item.due_date && !isItemDone && new Date() > new Date(item.due_date + 'T23:59:59') && (
                                        <span className="text-[10px] px-2 py-0.5 rounded-full bg-red-100 text-red-600 font-bold">⚠️ Quá hạn</span>
                                      )}
                                    </div>
                                  </div>
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>
          ))}
            </div>
          </div>
        ))}
      </div>
      <style>{`
        .custom-scrollbar::-webkit-scrollbar {
          width: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background-color: #cbd5e1;
          border-radius: 20px;
        }
      `}</style>
    </div>
  );
}
