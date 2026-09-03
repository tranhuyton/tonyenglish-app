import { useState, useEffect } from 'react';
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

export default function TaskBoard({ userId, filterCourseId = 'all', onStartTest }: { userId: string; filterCourseId?: string; onStartTest?: (testId: string) => void }) {
  const [assignments, setAssignments] = useState<Assignment[]>([]);
  const [boardTemplates, setBoardTemplates] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [expandedCards, setExpandedCards] = useState<Set<string>>(new Set());
  const [filterBoard, setFilterBoard] = useState<string>('');
  const [boardOptions, setBoardOptions] = useState<string[]>([]);

  useEffect(() => {
    fetchAssignments();
  }, [userId]);

  const fetchAssignments = async () => {
    try {
      setLoading(true);
      
      const { data: bData } = await supabase.from('board_templates').select('id, title, course_id');
      setBoardTemplates(bData || []);

      const { data, error } = await supabase
        .from('assignments')
        .select('*')
        .eq('user_id', userId)
        .not('category', 'is', null);

      if (error) throw error;
      setAssignments(data || []);
      
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

      setAssignments(prev => prev.map(a => 
        (a.title === task.title && a.task_type === 'manual') ? { ...a, student_completed: newStatus } : a
      ));
    } catch (error) {
      console.error('Error updating task:', error);
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
          const sortedItems = [...items].sort((a, b) => (a.card_order || 0) - (b.card_order || 0));
          const completedCount = sortedItems.filter(i => 
            i.task_type === 'test' ? i.is_completed : i.student_completed
          ).length;
          totalItems += sortedItems.length;
          totalCompleted += completedCount;
          return { title: cardTitle, order: sortedItems[0]?.card_order || 0, items: sortedItems, completedCount, totalCount: sortedItems.length };
        }).sort((a, b) => a.order - b.order);
        return { name: category, cards };
      });

      const overallProgress = totalItems > 0 ? Math.round((totalCompleted / totalItems) * 100) : 0;
      
      return { title: boardTitle, overallProgress, totalCompleted, totalItems, columns };
    });
  }, [assignments, filterCourseId, boardTemplates]);

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-b from-[#e0f2fe] to-[#f0f9ff] flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-4 border-[#0ea5e9] border-t-transparent"></div>
      </div>
    );
  }

  if (boardsData.length === 0) {
    return (
      <div className="min-h-screen bg-gradient-to-b from-[#e0f2fe] to-[#f0f9ff] p-4 md:p-6 flex items-start justify-center">
        <div className="p-12 text-center bg-white/80 backdrop-blur rounded-2xl shadow-sm border border-slate-200 m-6 mt-12 w-full max-w-lg">
          <span className="text-5xl block mb-4">📋</span>
          <h3 className="text-xl font-medium text-slate-700 mb-2">Chưa có bảng công việc nào</h3>
          <p className="text-slate-500">Hãy chọn một khóa học khác hoặc liên hệ giáo viên để được giao bảng công việc.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-[500px] bg-gradient-to-b from-[#e0f2fe] to-[#f0f9ff] p-4 md:p-6 text-slate-800 rounded-3xl">
      <div className="max-w-[1600px] mx-auto space-y-12">
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
            <div className="flex flex-col md:flex-row gap-6 overflow-x-auto pb-8 snap-x">
              {board.columns.map(col => (
                <div 
                  key={col.name} 
                  className="flex-none w-full md:w-80 lg:w-[340px] bg-white/80 backdrop-blur rounded-2xl shadow-sm border border-slate-200 p-4 snap-start flex flex-col h-fit max-h-[calc(100vh-200px)]"
                >
                  <div className="flex justify-between items-center mb-4 px-2">
                    <h2 className="font-bold text-lg text-slate-700">{col.name}</h2>
                    <span className="bg-slate-100 text-slate-600 text-xs font-medium px-2.5 py-1 rounded-full">
                      {col.cards.length} thẻ
                    </span>
                  </div>
              
              <div className="flex flex-col gap-3 overflow-y-auto pr-2 custom-scrollbar">
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
                          <span className="text-xs font-medium text-slate-500 min-w-[32px] text-right">
                            {card.completedCount}/{card.totalCount}
                          </span>
                        </div>
                      </div>

                      {isExpanded && (
                        <div className="px-4 pb-4 border-t border-slate-50 bg-slate-50/50">
                          <div className="mt-3 flex flex-col gap-2">
                            {card.items.map(item => {
                              const isItemDone = item.task_type === 'test' ? item.is_completed : item.student_completed;
                              
                              return (
                                <div 
                                  key={item.id} 
                                  className={`flex items-start gap-2.5 p-2 rounded-lg transition-colors ${
                                    item.task_type === 'manual' ? 'hover:bg-slate-100 cursor-pointer' : ''
                                  } ${isItemDone ? 'opacity-60' : ''}`}
                                  onClick={() => item.task_type === 'manual' && toggleTask(item)}
                                >
                                  <div className="mt-0.5 shrink-0">
                                    {item.task_type === 'manual' ? (
                                      isItemDone ? (
                                        <span className="text-emerald-500">✅</span>
                                      ) : (
                                        <span className="text-slate-300 text-sm">⭕</span>
                                      )
                                    ) : (
                                      isItemDone ? (
                                        <span className="text-emerald-500">✅</span>
                                      ) : (
                                        <button 
                                          onClick={(e) => {
                                            e.stopPropagation();
                                            if (item.test_id && onStartTest) onStartTest(item.test_id);
                                          }}
                                          className="p-1 -m-1 rounded-md hover:bg-[#e0f2fe] text-[#0ea5e9] transition-colors"
                                          title="Làm bài kiểm tra"
                                        >
                                          <span className="text-xs">📝</span>
                                        </button>
                                      )
                                    )}
                                  </div>
                                  <div className="flex flex-col gap-0.5 w-full">
                                    <div>
                                      <span className={`text-sm leading-tight pt-0.5 ${
                                        isItemDone ? 'line-through text-slate-400' : 'text-slate-700'
                                      }`}>
                                        {item.title}
                                      </span>
                                      {item.due_date && (
                                        <span className="text-[10px] text-slate-400 ml-2 whitespace-nowrap">
                                          {new Date(item.due_date + 'T00:00:00').toLocaleDateString('vi-VN', {day:'numeric', month:'short'})}
                                        </span>
                                      )}
                                    </div>
                                    <div className="mt-0.5 flex flex-wrap gap-1">
                                      {isItemDone && (item.task_type === 'test' || item.admin_approved) && (
                                        <span className="text-[10px] px-1.5 py-0.5 rounded bg-emerald-100 text-emerald-700 font-bold">✅ Đã hoàn thành</span>
                                      )}
                                      {isItemDone && !item.admin_approved && item.task_type === 'manual' && (
                                        <span className="text-[10px] px-1.5 py-0.5 rounded bg-amber-100 text-amber-700 font-bold">⏳ Chờ giáo viên phê duyệt</span>
                                      )}
                                      {item.due_date && !isItemDone && new Date() > new Date(item.due_date + 'T23:59:59') && (
                                        <span className="text-[10px] px-1.5 py-0.5 rounded bg-red-100 text-red-600 font-bold">⚠️ Quá hạn</span>
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
