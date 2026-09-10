import { useState, useEffect, useMemo } from 'react';
import { supabase } from './supabase';
import { parseModuleTheme, formatModuleTitleWithColor, ModuleColorModal } from './moduleTheme';

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

interface ActiveModalCard {
  card: CardData;
  colName: string;
  boardTitle: string;
}

export default function TaskBoard({ userId, filterCourseId = 'all', filterElement, onStartTest }: { userId: string; filterCourseId?: string; filterElement?: React.ReactNode; onStartTest?: (testId: string) => void }) {
  const [assignments, setAssignments] = useState<Assignment[]>([]);
  const [boardTemplates, setBoardTemplates] = useState<any[]>([]);
  const [boardColumns, setBoardColumns] = useState<any[]>([]);
  const [completedTestIds, setCompletedTestIds] = useState<Set<string>>(new Set());
  const [latestTestScores, setLatestTestScores] = useState<Map<string, { score: number; total_score: number; percent: number }>>(new Map());
  const [inProgressTestIds, setInProgressTestIds] = useState<Set<string>>(new Set());
  const [loading, setLoading] = useState(true);
  const [activeModalCard, setActiveModalCard] = useState<ActiveModalCard | null>(null);
  const [colorPickerTarget, setColorPickerTarget] = useState<{ colId?: string; colTitle: string } | null>(null);
  const [activeBoardIndex, setActiveBoardIndex] = useState(0);

  useEffect(() => {
    fetchAssignments();
  }, [userId]);

  useEffect(() => {
    if (!activeModalCard) return;
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setActiveModalCard(null);
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [activeModalCard]);

  const fetchAssignments = async () => {
    try {
      setLoading(true);
      
      const [bRes, colRes, assignRes, trRes] = await Promise.all([
        supabase.from('board_templates').select('id, title, course_id'),
        supabase.from('board_columns').select('*').order('order_index', { ascending: true }),
        supabase.from('assignments').select('*').eq('user_id', userId).not('category', 'is', null),
        supabase.from('test_results').select('id, test_title, score, total_score, created_at, details').eq('user_id', userId).order('created_at', { ascending: false })
      ]);

      setBoardTemplates(bRes.data || []);
      setBoardColumns(colRes.data || []);

      const cSet = new Set<string>();
      const scoreMap = new Map<string, { score: number; total_score: number; percent: number }>();
      (trRes.data || []).forEach((r: any) => {
        let d = r.details;
        if (typeof d === 'string') {
          try { d = JSON.parse(d); } catch (e) {}
        }
        const testId = d?.test_id ? String(d.test_id) : (r.test_id ? String(r.test_id) : null);
        const testTitle = r.test_title ? r.test_title.trim().toLowerCase() : null;

        if (testId) cSet.add(testId);

        const scoreObj = {
          score: r.score != null ? r.score : 0,
          total_score: r.total_score != null ? r.total_score : 0,
          percent: (r.total_score && r.total_score > 0) ? Math.round((r.score / r.total_score) * 100) : (r.score || 0)
        };

        if (testId && !scoreMap.has(testId)) {
          scoreMap.set(testId, scoreObj);
        }
        if (testTitle && !scoreMap.has(testTitle)) {
          scoreMap.set(testTitle, scoreObj);
        }
      });
      setCompletedTestIds(cSet);
      setLatestTestScores(scoreMap);

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

      // Also sync all matching assignments (same title, same user, same task_type, scoped to card)
      const updatePayload: any = { student_completed: newStatus };
      if (!newStatus) updatePayload.admin_approved = false; // Reset approval when un-completing
      let query = supabase
        .from('assignments')
        .update(updatePayload)
        .eq('user_id', userId)
        .eq('title', task.title)
        .eq('task_type', 'manual');
      if (task.card_title) {
        query = query.eq('card_title', task.card_title);
      }
      await query;

      // Update local state
      setAssignments(prev => prev.map(a => 
        (a.title === task.title && a.task_type === 'manual' && (!task.card_title || a.card_title === task.card_title)) ? { ...a, student_completed: newStatus } : a
      ));

      // Also sync activeModalCard if currently open
      setActiveModalCard(prev => {
        if (!prev) return null;
        const updatedItems = prev.card.items.map(a => 
          (a.title === task.title && a.task_type === 'manual' && (!task.card_title || a.card_title === task.card_title)) ? { ...a, student_completed: newStatus } : a
        );
        const compCount = updatedItems.filter(i => {
          if (i.task_type === 'test') {
            return i.is_completed || (i.test_id && completedTestIds.has(String(i.test_id)));
          }
          return i.student_completed;
        }).length;
        return {
          ...prev,
          card: {
            ...prev.card,
            items: updatedItems,
            completedCount: compCount
          }
        };
      });
    } catch (error) {
      console.error('Error toggling task:', error);
      alert('Không thể cập nhật trạng thái công việc. Vui lòng thử lại.');
    }
  };

  const handleSaveColumnColor = async (bg: string, text: string) => {
    if (!colorPickerTarget) return;
    const clean = parseModuleTheme(colorPickerTarget.colTitle).cleanTitle;
    const newTitle = formatModuleTitleWithColor(clean, bg, text);

    try {
      if (colorPickerTarget.colId) {
        await supabase.from('board_columns').update({ title: newTitle }).eq('id', colorPickerTarget.colId);
        setBoardColumns(prev => prev.map(c => c.id === colorPickerTarget.colId ? { ...c, title: newTitle } : c));
      }

      await supabase.from('assignments').update({ category: newTitle }).eq('category', colorPickerTarget.colTitle);
      setAssignments(prev => prev.map(a => a.category === colorPickerTarget.colTitle ? { ...a, category: newTitle } : a));
    } catch (e) {
      console.error('Error updating column color:', e);
    } finally {
      setColorPickerTarget(null);
    }
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
        const norm = parseModuleTheme(catName).cleanTitle.trim().toLowerCase();
        // Exam practice & Past papers ALWAYS at the very end
        if (norm.includes('exam practice') || norm.includes('past paper') || norm.includes('đề thi')) {
          return 999999;
        }
        // Topic / Section 1 to 10 in numeric order
        const match = norm.match(/(?:topic|section)\s*(\d+)/i);
        if (match) {
          return parseInt(match[1], 10);
        }
        // Matching board_columns order_index
        const bc = boardColumns.find(c => parseModuleTheme(c.title).cleanTitle.trim().toLowerCase() === norm);
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
      <div className="w-full flex-1 min-h-0 h-full flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-4 border-[#0ea5e9] border-t-transparent"></div>
      </div>
    );
  }

  if (boardsData.length === 0) {
    return (
      <div className="w-full flex-1 min-h-0 h-full flex flex-col items-center justify-center p-6 bg-white/60 backdrop-blur rounded-2xl border border-dashed border-slate-200">
        <div className="p-8 text-center bg-white rounded-2xl shadow-sm border border-slate-200 max-w-md">
          <span className="text-4xl block mb-3">📋</span>
          <h3 className="text-lg font-bold text-slate-800 mb-1">Chưa có bảng công việc nào</h3>
          <p className="text-sm text-slate-500">Hãy chọn một khóa học khác hoặc liên hệ giáo viên để được giao bảng công việc.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="w-full flex-1 min-h-0 h-full flex flex-col relative">
      {/* If multiple boards exist, show switch tabs */}
      {boardsData.length > 1 && (
        <div className="flex items-center gap-2 mb-2.5 shrink-0 overflow-x-auto custom-scrollbar pb-1">
          {boardsData.map((b, idx) => (
            <button
              key={b.title}
              onClick={() => setActiveBoardIndex(idx)}
              className={`px-3 py-1.5 rounded-xl font-bold text-xs transition-all whitespace-nowrap cursor-pointer ${activeBoardIndex === idx ? 'bg-[#0ea5e9] text-white shadow-sm' : 'bg-white/80 hover:bg-white text-slate-600 border border-slate-200'}`}
            >
              📋 {b.title}
            </button>
          ))}
        </div>
      )}

      {(() => {
        const board = boardsData[activeBoardIndex] || boardsData[0];
        if (!board) return null;

        return (
          <div key={board.title} className="w-full flex-1 min-h-0 h-full flex flex-col">
            {/* Board - Horizontal Scroll like Trello */}
            <div className="flex-1 min-h-0 h-full flex flex-row gap-4 overflow-x-auto overflow-y-hidden pb-1 pt-0.5 custom-scrollbar items-stretch w-full">
              {board.columns.map(col => {
                const matchingCol = boardColumns.find(bc => {
                  const t1 = parseModuleTheme(bc.title).cleanTitle.trim().toLowerCase();
                  const t2 = parseModuleTheme(col.name).cleanTitle.trim().toLowerCase();
                  return t1 === t2 || (bc.id && col.name === bc.id);
                });
                const colTheme = matchingCol ? parseModuleTheme(matchingCol.title) : parseModuleTheme(col.name);

                return (
                  <div 
                    key={col.name} 
                    className="flex-none w-[340px] md:w-[360px] rounded-2xl shadow-sm border p-3 flex flex-col h-full max-h-full transition-all"
                    style={{
                      backgroundColor: colTheme.hasColor ? `${colTheme.bg}40` : 'rgba(255, 255, 255, 0.85)',
                      borderColor: colTheme.hasColor ? colTheme.border : '#e2e8f0'
                    }}
                  >
                    {/* Column Header */}
                    <div 
                      className="flex justify-between items-center p-2.5 rounded-xl mb-2.5 border shadow-xs transition-colors shrink-0"
                      style={{
                        backgroundColor: colTheme.hasColor ? colTheme.bg : '#ffffff',
                        borderColor: colTheme.hasColor ? colTheme.border : '#e2e8f0',
                        color: colTheme.hasColor ? colTheme.text : '#1e293b'
                      }}
                    >
                      <div className="flex items-center gap-2 min-w-0">
                        <h2 className="font-extrabold text-[15px] truncate" title={colTheme.cleanTitle}>
                          {colTheme.cleanTitle}
                        </h2>
                      </div>
                      <div className="flex items-center gap-1.5 shrink-0">
                        <span 
                          className="text-xs font-bold px-2 py-0.5 rounded-full border"
                          style={{
                            backgroundColor: 'white',
                            borderColor: colTheme.hasColor ? colTheme.border : '#e2e8f0',
                            color: colTheme.hasColor ? colTheme.text : '#64748b'
                          }}
                        >
                          {col.cards.length} thẻ
                        </span>
                        <button
                          type="button"
                          onClick={() => setColorPickerTarget({ colId: matchingCol?.id, colTitle: matchingCol?.title || col.name })}
                          className="w-7 h-7 rounded-lg bg-white/80 hover:bg-white border border-black/10 hover:border-black/20 flex items-center justify-center text-xs transition cursor-pointer shadow-xs"
                          title="Chọn màu cột này"
                        >
                          🎨
                        </button>
                      </div>
                    </div>
                
                    {/* Cards List inside column with vertical scroll */}
                    <div className="flex-1 overflow-y-auto custom-scrollbar pr-1 flex flex-col gap-3 min-h-0 pt-0.5">
                      {col.cards.map(card => {
                        const progressPct = card.totalCount > 0 ? Math.round((card.completedCount / card.totalCount) * 100) : 0;
                        const testCount = card.items.filter(i => i.task_type === 'test').length;
                        const manualCount = card.items.filter(i => i.task_type === 'manual').length;
                        const isCardAllDone = card.totalCount > 0 && card.completedCount === card.totalCount;
                        const hasOverdue = card.items.some(i => {
                          const isItemDone = i.task_type === 'test' 
                            ? (i.is_completed || (i.test_id && completedTestIds.has(String(i.test_id))))
                            : i.student_completed;
                          return i.due_date && !isItemDone && new Date() > new Date(i.due_date + 'T23:59:59');
                        });

                        return (
                          <div 
                            key={card.title} 
                            onClick={() => setActiveModalCard({ card, colName: col.name, boardTitle: board.title })}
                            className="bg-white rounded-xl border border-slate-200/90 shadow-xs hover:shadow-md hover:border-sky-300 hover:-translate-y-0.5 transition-all p-3.5 cursor-pointer select-none group"
                          >
                            <div className="flex justify-between items-start gap-2 mb-2">
                              <h3 className="font-bold text-slate-800 text-sm leading-snug group-hover:text-[#0ea5e9] transition-colors">
                                {card.title}
                              </h3>
                              <span className="text-slate-300 group-hover:text-[#0ea5e9] text-xs transition-colors shrink-0">
                                ➜
                              </span>
                            </div>
                            
                            {/* Progress bar */}
                            <div className="flex items-center gap-2 mb-2.5">
                              <div className="flex-1 h-1.5 bg-slate-100 rounded-full overflow-hidden">
                                <div 
                                  className={`h-full rounded-full transition-all duration-300 ${isCardAllDone ? 'bg-emerald-500' : 'bg-[#0ea5e9]'}`}
                                  style={{ width: `${progressPct}%` }}
                                />
                              </div>
                              <div className="flex items-center gap-1 shrink-0">
                                <span className={`text-xs font-bold ${isCardAllDone ? 'text-emerald-600' : 'text-[#0284c7]'}`}>
                                  {progressPct}%
                                </span>
                                <span className="text-[11px] font-medium text-slate-400">
                                  ({card.completedCount}/{card.totalCount})
                                </span>
                              </div>
                            </div>

                            {/* Card badges */}
                            <div className="flex items-center gap-1.5 flex-wrap">
                              {testCount > 0 && (
                                <span className="text-[10px] font-semibold px-2 py-0.5 rounded-md bg-sky-50 text-sky-700 border border-sky-100">
                                  📝 {testCount} đề thi
                                </span>
                              )}
                              {manualCount > 0 && (
                                <span className="text-[10px] font-semibold px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-700 border border-emerald-100">
                                  ✓ {manualCount} việc
                                </span>
                              )}
                              {isCardAllDone && (
                                <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-emerald-100 text-emerald-700">
                                  ✓ Xong
                                </span>
                              )}
                              {hasOverdue && (
                                <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-red-100 text-red-600">
                                  ⚠️ Quá hạn
                                </span>
                              )}
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        );
      })()}

      {/* ================= CARD DETAIL POPUP MODAL ================= */}
      {activeModalCard && (() => {
        const matchingCol = boardColumns.find(bc => {
          const t1 = parseModuleTheme(bc.title).cleanTitle.trim().toLowerCase();
          const t2 = parseModuleTheme(activeModalCard.colName).cleanTitle.trim().toLowerCase();
          return t1 === t2 || (bc.id && activeModalCard.colName === bc.id);
        });
        const modalTheme = matchingCol ? parseModuleTheme(matchingCol.title) : parseModuleTheme(activeModalCard.colName);
        const currentCard = activeModalCard.card;
        const progressPct = currentCard.totalCount > 0 ? Math.round((currentCard.completedCount / currentCard.totalCount) * 100) : 0;
        const isCardAllDone = currentCard.totalCount > 0 && currentCard.completedCount === currentCard.totalCount;

        return (
          <div 
            className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-3 sm:p-6 animate-in fade-in duration-200"
            onClick={() => setActiveModalCard(null)}
          >
            <div 
              className="relative w-full max-w-2xl bg-white rounded-3xl shadow-2xl border border-slate-200 flex flex-col max-h-[88vh] overflow-hidden animate-in zoom-in-95 duration-150"
              onClick={e => e.stopPropagation()}
            >
              {/* Modal Header */}
              <div 
                className="px-6 py-5 border-b flex items-start justify-between gap-4 transition-colors shrink-0"
                style={{
                  backgroundColor: modalTheme.hasColor ? modalTheme.bg : '#f8fafc',
                  borderColor: modalTheme.hasColor ? modalTheme.border : '#e2e8f0'
                }}
              >
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 flex-wrap mb-1.5">
                    <span 
                      className="text-[11px] font-black uppercase tracking-wider px-2.5 py-0.5 rounded-lg border shadow-xs"
                      style={{
                        backgroundColor: 'white',
                        color: modalTheme.hasColor ? modalTheme.text : '#0284c7',
                        borderColor: modalTheme.hasColor ? modalTheme.border : '#bae6fd'
                      }}
                    >
                      {modalTheme.cleanTitle}
                    </span>
                    <span className="text-xs text-slate-500 font-medium">• {activeModalCard.boardTitle}</span>
                  </div>
                  <h2 className="text-xl sm:text-2xl font-black text-slate-900 leading-tight">
                    {currentCard.title}
                  </h2>
                  
                  {/* Progress bar in header */}
                  <div className="mt-3 flex items-center gap-3">
                    <div className="flex-1 h-2 bg-black/10 rounded-full overflow-hidden">
                      <div 
                        className={`h-full rounded-full transition-all duration-300 ${isCardAllDone ? 'bg-emerald-500' : 'bg-[#0ea5e9]'}`}
                        style={{ width: `${progressPct}%` }}
                      />
                    </div>
                    <span className="text-xs font-bold shrink-0" style={{ color: modalTheme.hasColor ? modalTheme.text : '#0f172a' }}>
                      {progressPct}% ({currentCard.completedCount}/{currentCard.totalCount} hoàn thành)
                    </span>
                  </div>
                </div>

                <button
                  type="button"
                  onClick={() => setActiveModalCard(null)}
                  className="w-9 h-9 rounded-full bg-white/90 hover:bg-white text-slate-500 hover:text-slate-800 flex items-center justify-center transition-all shadow-xs shrink-0 border border-slate-200/80 cursor-pointer"
                  title="Đóng (ESC)"
                >
                  ✕
                </button>
              </div>

              {/* Modal Body - Scrollable Items */}
              <div className="flex-1 overflow-y-auto custom-scrollbar p-5 sm:p-6 space-y-3 bg-slate-50/50">
                <div className="flex items-center justify-between mb-1">
                  <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">
                    Danh sách bài tập ({currentCard.items.length} mục)
                  </span>
                  <span className="text-xs font-medium text-slate-400">
                    {currentCard.completedCount}/{currentCard.totalCount} đã xong
                  </span>
                </div>

                {currentCard.items.map(item => {
                  const isTest = item.task_type === 'test';
                  const isItemDone = isTest 
                    ? (item.is_completed || (item.test_id && completedTestIds.has(String(item.test_id))))
                    : item.student_completed;
                  const isItemInProgress = isTest && !isItemDone && item.test_id && inProgressTestIds.has(String(item.test_id));
                  const testScore = isTest ? (item.test_id ? latestTestScores.get(String(item.test_id)) : (item.title ? latestTestScores.get(item.title.trim().toLowerCase()) : null)) : null;

                  if (isTest) {
                    return (
                      <div 
                        key={item.id} 
                        className={`p-3.5 rounded-2xl border transition-all select-none ${
                          isItemDone 
                            ? 'bg-emerald-50/50 border-emerald-200' 
                            : isItemInProgress 
                              ? 'bg-amber-50/50 border-amber-200 shadow-xs' 
                              : 'bg-white border-slate-200 hover:border-sky-300 shadow-xs'
                        }`}
                      >
                        <div className="flex items-start gap-3">
                          <div className="mt-0.5 shrink-0 text-lg">
                            {isItemDone ? (
                              <span className="text-emerald-500 font-bold">✅</span>
                            ) : isItemInProgress ? (
                              <span className="text-amber-500">⏳</span>
                            ) : (
                              <span className="text-sky-500">📝</span>
                            )}
                          </div>
                          <div className="flex-1 min-w-0">
                            <div className="flex items-baseline justify-between gap-2">
                              <p className={`text-sm font-bold leading-snug ${
                                isItemDone ? 'text-slate-600' : 'text-slate-800'
                              }`}>
                                {item.title}
                              </p>
                              {item.due_date && (
                                <span className="text-[11px] text-slate-400 shrink-0 ml-2">
                                  Hạn: {new Date(item.due_date + 'T00:00:00').toLocaleDateString('vi-VN', {day:'numeric', month:'short'})}
                                </span>
                              )}
                            </div>

                            <div className="mt-2.5 flex items-center justify-between gap-2 flex-wrap">
                              <div>
                                {isItemDone ? (
                                  <div className="flex items-center gap-1.5 flex-wrap">
                                    <span className="inline-flex items-center text-[10px] px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-bold">
                                      ✓ Hoàn thành
                                    </span>
                                    {testScore && (
                                      <span 
                                        className="inline-flex items-center gap-1 text-[11px] px-2.5 py-0.5 rounded-full bg-sky-100 text-[#0284c7] font-black border border-sky-200 shadow-xs"
                                        title={`Điểm làm gần đây nhất: ${testScore.score}/${testScore.total_score} (${testScore.percent}%)`}
                                      >
                                        🎯 {testScore.total_score > 0 ? `${testScore.score}/${testScore.total_score}` : testScore.score}
                                        <span className="text-[10px] font-bold text-sky-600">({testScore.percent}%)</span>
                                      </span>
                                    )}
                                  </div>
                                ) : isItemInProgress ? (
                                  <span className="inline-flex items-center text-[10px] px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-700 font-bold">
                                    ⏳ Đang làm dở
                                  </span>
                                ) : (
                                  <span className="inline-flex items-center text-[10px] px-2.5 py-0.5 rounded-full bg-slate-100 text-slate-500 font-medium">
                                    Chưa làm
                                  </span>
                                )}
                              </div>

                              {isItemDone ? (
                                <button 
                                  onClick={() => {
                                    if (item.test_id && onStartTest) {
                                      onStartTest(item.test_id);
                                      setActiveModalCard(null);
                                    }
                                  }}
                                  className="text-xs font-bold px-3.5 py-1.5 rounded-xl bg-emerald-100 hover:bg-emerald-200 text-emerald-800 transition-colors flex items-center gap-1.5 shrink-0 shadow-xs cursor-pointer"
                                  title="Làm lại bài thi này"
                                >
                                  <span>🔄</span> Làm lại
                                </button>
                              ) : isItemInProgress ? (
                                <button 
                                  onClick={() => {
                                    if (item.test_id && onStartTest) {
                                      onStartTest(item.test_id);
                                      setActiveModalCard(null);
                                    }
                                  }}
                                  className="text-xs font-bold px-3.5 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-600 text-white shadow-xs transition-all flex items-center gap-1.5 shrink-0 cursor-pointer"
                                  title="Làm tiếp bài đang làm dở"
                                >
                                  Làm tiếp ➜
                                </button>
                              ) : (
                                <button 
                                  onClick={() => {
                                    if (item.test_id && onStartTest) {
                                      onStartTest(item.test_id);
                                      setActiveModalCard(null);
                                    }
                                  }}
                                  className="text-xs font-bold px-3.5 py-1.5 rounded-xl bg-[#0ea5e9] hover:bg-[#0284c7] text-white shadow-xs transition-all flex items-center gap-1.5 shrink-0 cursor-pointer"
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
                      className={`flex items-start gap-3 p-3.5 rounded-2xl border transition-all cursor-pointer select-none ${
                        isItemDone 
                          ? 'bg-slate-50/80 border-slate-200/80 opacity-80' 
                          : 'bg-white border-slate-200 hover:border-sky-300 shadow-xs'
                      }`}
                      onClick={() => toggleTask(item)}
                    >
                      <div className="mt-0.5 shrink-0">
                        {isItemDone ? (
                          <div className="w-5 h-5 rounded-md bg-emerald-500 text-white flex items-center justify-center text-xs font-black shadow-xs">
                            ✓
                          </div>
                        ) : (
                          <div className="w-5 h-5 rounded-md border-2 border-slate-300 bg-white hover:border-[#0ea5e9] hover:bg-sky-50 transition-all flex items-center justify-center shadow-xs">
                          </div>
                        )}
                      </div>
                      <div className="flex flex-col gap-1 w-full min-w-0">
                        <div className="flex items-baseline justify-between gap-2">
                          <span className={`text-sm font-semibold leading-snug ${
                            isItemDone ? 'line-through text-slate-400' : 'text-slate-800'
                          }`}>
                            {item.title}
                          </span>
                          {item.due_date && (
                            <span className="text-[11px] text-slate-400 shrink-0 whitespace-nowrap">
                              Hạn: {new Date(item.due_date + 'T00:00:00').toLocaleDateString('vi-VN', {day:'numeric', month:'short'})}
                            </span>
                          )}
                        </div>
                        <div className="flex flex-wrap gap-1.5">
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

              {/* Modal Footer */}
              <div className="px-6 py-4 border-t border-slate-100 bg-white flex items-center justify-between shrink-0">
                <div className="text-xs text-slate-400">
                  {isCardAllDone ? '🎉 Bạn đã hoàn thành toàn bộ công việc trong thẻ này!' : '💡 Nhấp vào bài để bắt đầu làm hoặc tick chọn việc đã làm'}
                </div>
                <button
                  type="button"
                  onClick={() => setActiveModalCard(null)}
                  className="px-5 py-2 rounded-xl text-xs font-bold bg-slate-100 hover:bg-slate-200 text-slate-700 transition cursor-pointer"
                >
                  Đóng
                </button>
              </div>
            </div>
          </div>
        );
      })()}

      {/* ================= COLUMN COLOR PICKER MODAL ================= */}
      {colorPickerTarget && (() => {
        const theme = parseModuleTheme(colorPickerTarget.colTitle);
        return (
          <ModuleColorModal
            isOpen={true}
            title={theme.cleanTitle}
            initialBg={theme.bg}
            initialText={theme.text}
            onSave={handleSaveColumnColor}
            onClose={() => setColorPickerTarget(null)}
          />
        );
      })()}
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
