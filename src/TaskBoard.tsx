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

export interface BoardTheme {
  id: string;
  name: string;
  boardBg: string;
  titleBg: string;
  titleText?: string;
  isDark?: boolean;
}

export const DEFAULT_BOARD_THEME: BoardTheme = {
  id: 'light-blue',
  name: 'Xanh nhạt (Mặc định)',
  boardBg: '#e0f2fe',
  titleBg: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
  titleText: '#ffffff'
};

export const BOARD_THEMES: BoardTheme[] = [
  {
    id: 'light-blue',
    name: 'Xanh nhạt (Mặc định)',
    boardBg: '#e0f2fe',
    titleBg: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'sky-soft',
    name: 'Xanh lam êm dịu',
    boardBg: '#dbeafe',
    titleBg: 'linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'trello-ocean',
    name: 'Xanh Trello kinh điển',
    boardBg: '#0079bf',
    titleBg: 'linear-gradient(135deg, #005a9c 0%, #004377 100%)',
    titleText: '#ffffff',
    isDark: true
  },
  {
    id: 'teal-mint',
    name: 'Xanh ngọc / Bạc hà',
    boardBg: '#ccfbf1',
    titleBg: 'linear-gradient(135deg, #0f766e 0%, #115e59 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'purple-lavender',
    name: 'Tím Lavender',
    boardBg: '#ede9fe',
    titleBg: 'linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'sunset-orange',
    name: 'Cam hoàng hôn',
    boardBg: '#ffedd5',
    titleBg: 'linear-gradient(135deg, #ea580c 0%, #c2410c 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'rose-pastel',
    name: 'Hồng phấn Pastel',
    boardBg: '#ffe4e6',
    titleBg: 'linear-gradient(135deg, #e11d48 0%, #be123c 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'emerald-leaf',
    name: 'Xanh lá tươi mát',
    boardBg: '#dcfce7',
    titleBg: 'linear-gradient(135deg, #16a34a 0%, #15803d 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'slate-modern',
    name: 'Xám hiện đại',
    boardBg: '#e2e8f0',
    titleBg: 'linear-gradient(135deg, #334155 0%, #1e293b 100%)',
    titleText: '#ffffff'
  },
  {
    id: 'midnight-dark',
    name: 'Đêm đen huyền bí',
    boardBg: '#0f172a',
    titleBg: 'linear-gradient(135deg, #1e293b 0%, #0f172a 100%)',
    titleText: '#ffffff',
    isDark: true
  }
];

function getDarkerShade(hex: string, percent = 30): string {
  let c = hex.replace('#', '');
  if (c.length === 3) c = c.split('').map(x => x + x).join('');
  const num = parseInt(c, 16);
  if (isNaN(num)) return '#0284c7';
  let r = (num >> 16);
  let g = ((num >> 8) & 0x00FF);
  let b = (num & 0x0000FF);
  r = Math.max(0, Math.min(255, Math.floor(r * (1 - percent / 100))));
  g = Math.max(0, Math.min(255, Math.floor(g * (1 - percent / 100))));
  b = Math.max(0, Math.min(255, Math.floor(b * (1 - percent / 100))));
  return `#${((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1)}`;
}

export default function TaskBoard({ 
  userId, 
  filterCourseId = 'all', 
  topActions,
  bottomActions,
  courseTitle,
  filterElement, 
  onStartTest 
}: { 
  userId: string; 
  filterCourseId?: string; 
  topActions?: React.ReactNode;
  bottomActions?: React.ReactNode;
  courseTitle?: string;
  filterElement?: React.ReactNode; 
  onStartTest?: (testId: string) => void 
}) {
  const headerActions = topActions || filterElement;
  const [assignments, setAssignments] = useState<Assignment[]>([]);
  const [boardTemplates, setBoardTemplates] = useState<any[]>([]);
  const [boardColumns, setBoardColumns] = useState<any[]>([]);
  const [completedTestIds, setCompletedTestIds] = useState<Set<string>>(new Set());
  const [latestTestScores, setLatestTestScores] = useState<Map<string, { score: number; total_score: number; percent: number; isPassed: boolean }>>(new Map());
  const [inProgressTestIds, setInProgressTestIds] = useState<Set<string>>(new Set());
  const [loading, setLoading] = useState(true);
  const [activeModalCard, setActiveModalCard] = useState<ActiveModalCard | null>(null);
  const [isThemeModalOpen, setIsThemeModalOpen] = useState(false);
  const [boardTheme, setBoardTheme] = useState<BoardTheme>(() => {
    try {
      const saved = localStorage.getItem(`tony_taskboard_theme_${userId}`);
      if (saved) return JSON.parse(saved);
    } catch (e) {}
    return DEFAULT_BOARD_THEME;
  });

  const handleSelectTheme = (theme: BoardTheme) => {
    setBoardTheme(theme);
    try {
      localStorage.setItem(`tony_taskboard_theme_${userId}`, JSON.stringify(theme));
    } catch (e) {
      console.error('[TaskBoard] Error saving theme:', e);
    }
  };

  const handleApplyCustomColor = (hex: string) => {
    const darker = getDarkerShade(hex, 28);
    const darker2 = getDarkerShade(darker, 15);
    const newTheme: BoardTheme = {
      id: 'custom',
      name: 'Màu tùy chọn',
      boardBg: hex,
      titleBg: `linear-gradient(135deg, ${darker} 0%, ${darker2} 100%)`,
      titleText: '#ffffff'
    };
    handleSelectTheme(newTheme);
  };
  const [activeBoardIndex, setActiveBoardIndex] = useState(0);
  const [draggedColName, setDraggedColName] = useState<string | null>(null);
  const [dragOverColName, setDragOverColName] = useState<string | null>(null);
  const [customColOrders, setCustomColOrders] = useState<Record<string, string[]>>(() => {
    try {
      const saved = localStorage.getItem(`tony_taskboard_col_orders_${userId}`);
      return saved ? JSON.parse(saved) : {};
    } catch (e) {
      return {};
    }
  });

  const handleReorderColumns = (boardTitle: string, sourceColName: string, targetColName: string) => {
    if (!sourceColName || !targetColName || sourceColName === targetColName) return;

    setCustomColOrders(prev => {
      const board = boardsData.find(b => b.title === boardTitle);
      const currentCols = board ? board.columns.map(c => c.name) : (prev[boardTitle] || []);
      const fromIdx = currentCols.indexOf(sourceColName);
      const toIdx = currentCols.indexOf(targetColName);
      if (fromIdx === -1 || toIdx === -1) return prev;

      const newOrder = [...currentCols];
      const [moved] = newOrder.splice(fromIdx, 1);
      newOrder.splice(toIdx, 0, moved);

      const next = { ...prev, [boardTitle]: newOrder };
      try {
        localStorage.setItem(`tony_taskboard_col_orders_${userId}`, JSON.stringify(next));
      } catch (e) {
        console.error('[TaskBoard] Error saving column order:', e);
      }
      return next;
    });
  };

  const handleResetColumnOrder = (boardTitle: string) => {
    setCustomColOrders(prev => {
      const next = { ...prev };
      delete next[boardTitle];
      try {
        localStorage.setItem(`tony_taskboard_col_orders_${userId}`, JSON.stringify(next));
      } catch (e) {}
      return next;
    });
  };

  useEffect(() => {
    fetchAssignments();
    const handleRefresh = () => fetchAssignments();
    window.addEventListener('tony-refresh-lecture-progress', handleRefresh);
    return () => {
      window.removeEventListener('tony-refresh-lecture-progress', handleRefresh);
    };
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
      const scoreMap = new Map<string, { score: number; total_score: number; percent: number; isPassed: boolean }>();
      (trRes.data || []).forEach((r: any) => {
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
          isPassed = (score / total) >= 0.5; // Cần đạt từ 50% trở lên
        } else {
          isPassed = score >= 5.0;
        }

        if (testId && isPassed) cSet.add(testId);

        const scoreObj = {
          score,
          total_score: total,
          percent,
          isPassed
        };

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

      // Sort columns: Topic 1 -> 21 strictly, then Exam practice & Past papers ALWAYS at the very end
      const getColumnWeight = (catName: string) => {
        const norm = parseModuleTheme(catName).cleanTitle.trim().toLowerCase();
        // Exam practice & Past papers ALWAYS at the very end
        if (norm.includes('exam practice') || norm.includes('past paper') || norm.includes('đề thi')) {
          return 999999;
        }
        // Matching board_columns order_index first
        const bc = boardColumns.find(c => parseModuleTheme(c.title).cleanTitle.trim().toLowerCase() === norm);
        if (bc && bc.order_index != null) {
          return bc.order_index;
        }
        // Topic / Section 1 to 21 in numeric order
        const match = norm.match(/(?:topic|section)\s*(\d+)/i);
        if (match) {
          return parseInt(match[1], 10);
        }
        return 50000;
      };

      const customOrder = customColOrders[boardTitle];
      const isCustomOrderValid = customOrder && Array.isArray(customOrder) &&
        customOrder.length === columns.length &&
        columns.every(col => customOrder.includes(col.name));

      if (isCustomOrderValid) {
        columns.sort((a, b) => {
          const idxA = customOrder.indexOf(a.name);
          const idxB = customOrder.indexOf(b.name);
          return idxA - idxB;
        });
      } else {
        columns.sort((a, b) => getColumnWeight(a.name) - getColumnWeight(b.name));
      }

      const overallProgress = totalItems > 0 ? Math.round((totalCompleted / totalItems) * 100) : 0;
      
      return { title: boardTitle, overallProgress, totalCompleted, totalItems, columns };
    });
  }, [assignments, filterCourseId, boardTemplates, boardColumns, completedTestIds, customColOrders]);

  if (loading) {
    return (
      <div 
        className="w-full flex-1 min-h-0 h-full flex items-center justify-center transition-colors duration-300"
        style={{ backgroundColor: boardTheme.boardBg }}
      >
        <div className="animate-spin rounded-full h-12 w-12 border-4 border-[#0ea5e9] border-t-transparent"></div>
      </div>
    );
  }

  if (boardsData.length === 0) {
    return (
      <div 
        className="w-full flex-1 min-h-0 h-full flex flex-col p-4 transition-colors duration-300"
        style={{ backgroundColor: boardTheme.boardBg }}
      >
        {headerActions && (
          <div className="flex justify-end relative z-40 mb-3 shrink-0">
            {headerActions}
          </div>
        )}
        <div className="flex-1 flex flex-col items-center justify-center">
          <div className="p-10 text-center bg-white rounded-[2rem] shadow-sm border border-slate-200 max-w-md">
            <span className="text-5xl block mb-4 opacity-40 grayscale">📋</span>
            <h3 className="text-xl font-black text-slate-800 mb-2 tracking-tight">Chưa có bảng công việc nào</h3>
            <p className="text-[14px] text-slate-500 font-medium">Hãy chọn một khóa học khác hoặc liên hệ giáo viên để được giao bảng công việc.</p>
          </div>
        </div>
      </div>
    );
  }

  const currentBoard = boardsData[activeBoardIndex] || boardsData[0];

  return (
    <div 
      className="w-full flex-1 min-h-0 h-full flex flex-col relative transition-colors duration-300"
      style={{ backgroundColor: boardTheme.boardBg }}
    >
      {/* Top Actions Row */}
      {headerActions && (
        <div className="flex justify-end relative z-40 mb-2 px-3 pt-2 shrink-0">
          {headerActions}
        </div>
      )}

      {/* UNIFIED HEADER BANNER - DARKER BLUE OR THEME TITLE BG */}
      <div className="px-3 pt-2.5 pb-2 shrink-0">
        <div 
          className="rounded-2xl p-3 sm:p-4 shadow-sm text-white flex flex-col md:flex-row justify-between items-center gap-3 transition-all duration-300"
          style={{ background: boardTheme.titleBg }}
        >
          <div className="flex items-center gap-3">
            <span className="text-2xl sm:text-3xl">📋</span>
            <div>
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold tracking-tight text-white">
                Bảng Công Việc{courseTitle ? ` - ${courseTitle}` : (currentBoard?.title ? ` - ${currentBoard.title}` : '')}
              </h1>
              <p className="text-white/85 text-xs md:text-sm mt-0.5">
                Theo dõi tiến độ bài học và làm bài tập theo từng chuyên đề
              </p>
            </div>
          </div>

          <div className="flex flex-wrap items-center gap-2 sm:gap-3 w-full md:w-auto justify-between md:justify-end">
            {/* Switch tabs if multiple boards exist */}
            {boardsData.length > 1 && (
              <div className="flex items-center gap-1 bg-white/20 backdrop-blur-sm p-1 rounded-xl">
                {boardsData.map((b, idx) => (
                  <button
                    key={b.title}
                    onClick={() => setActiveBoardIndex(idx)}
                    className={`px-3 py-1.5 rounded-lg font-bold text-xs transition-all whitespace-nowrap cursor-pointer ${activeBoardIndex === idx ? 'bg-white text-slate-800 shadow-sm' : 'text-white/80 hover:text-white hover:bg-white/10'}`}
                  >
                    {b.title}
                  </button>
                ))}
              </div>
            )}

            {/* Progress bar */}
            {currentBoard && currentBoard.totalItems > 0 && (
              <div className="flex flex-col items-center sm:items-end">
                <div className="text-xs sm:text-sm text-white/90 font-medium mb-1">
                  Tiến độ: {currentBoard.totalCompleted}/{currentBoard.totalItems} ({currentBoard.overallProgress}%)
                </div>
                <div className="w-32 sm:w-40 h-2 bg-white/25 rounded-full overflow-hidden">
                  <div 
                    className="h-full bg-white rounded-full transition-all duration-500"
                    style={{ width: `${currentBoard.overallProgress}%` }}
                  />
                </div>
              </div>
            )}

            {/* Reset column order button */}
            {currentBoard && customColOrders[currentBoard.title]?.length > 0 && (
              <button
                type="button"
                onClick={() => handleResetColumnOrder(currentBoard.title)}
                className="bg-white/20 hover:bg-white/30 active:scale-95 text-white text-xs sm:text-[13px] font-bold px-3 py-1.5 rounded-xl transition-all shadow-sm flex items-center gap-1.5 cursor-pointer shrink-0"
                title="Khôi phục thứ tự các cột ban đầu"
              >
                <span>↺</span> <span>Đặt lại thứ tự cột</span>
              </button>
            )}

            {/* Đổi màu nền bảng làm việc */}
            <button
              type="button"
              onClick={() => setIsThemeModalOpen(true)}
              className="bg-white/20 hover:bg-white/30 active:scale-95 text-white text-xs sm:text-[13px] font-bold px-3 py-1.5 rounded-xl transition-all shadow-sm flex items-center gap-1.5 cursor-pointer shrink-0"
              title="Đổi màu nền bảng làm việc giống Trello"
            >
              <span>🎨</span> <span>Đổi màu nền</span>
            </button>
          </div>
        </div>
      </div>

      {(() => {
        const board = boardsData[activeBoardIndex] || boardsData[0];
        if (!board) return null;

        return (
          <div key={board.title} className="w-full flex-1 min-h-0 h-full flex flex-col relative overflow-hidden">
            {/* Board - Horizontal Scroll like Trello */}
            <div 
              className={`flex-1 min-h-0 h-full flex flex-row gap-3 overflow-x-auto overflow-y-hidden pb-16 pt-0.5 board-horizontal-scrollbar items-stretch w-full px-3 ${
                boardTheme.isDark ? 'dark-theme' : ''
              }`}
            >
              {board.columns.map(col => {
                const isDragging = draggedColName === col.name;
                const isDragOver = dragOverColName === col.name && draggedColName !== col.name;

                return (
                  <div 
                    key={col.name} 
                    draggable={true}
                    onDragStart={(e) => {
                      const target = e.target as HTMLElement;
                      if (target.closest('button, input, textarea, .task-card-item')) {
                        e.preventDefault();
                        return;
                      }
                      setDraggedColName(col.name);
                      e.dataTransfer.setData('text/plain', col.name);
                      e.dataTransfer.effectAllowed = 'move';
                    }}
                    onDragOver={(e) => {
                      e.preventDefault();
                      e.dataTransfer.dropEffect = 'move';
                      if (draggedColName && draggedColName !== col.name && dragOverColName !== col.name) {
                        setDragOverColName(col.name);
                      }
                    }}
                    onDragLeave={(e) => {
                      if (e.currentTarget.contains(e.relatedTarget as Node)) return;
                      if (dragOverColName === col.name) {
                        setDragOverColName(null);
                      }
                    }}
                    onDrop={(e) => {
                      e.preventDefault();
                      const sourceColName = e.dataTransfer.getData('text/plain') || draggedColName;
                      if (sourceColName && sourceColName !== col.name) {
                        handleReorderColumns(board.title, sourceColName, col.name);
                      }
                      setDraggedColName(null);
                      setDragOverColName(null);
                    }}
                    onDragEnd={() => {
                      setDraggedColName(null);
                      setDragOverColName(null);
                    }}
                    className={`flex-none w-[275px] sm:w-[280px] rounded-[1.25rem] border p-2.5 sm:p-3 flex flex-col h-full max-h-full transition-all duration-200 shadow-sm ${
                      isDragging 
                        ? 'opacity-30 scale-95 border-dashed border-2 border-sky-400 bg-sky-50/50' 
                        : isDragOver
                          ? 'ring-4 ring-sky-400/50 scale-[1.01] border-sky-400 shadow-xl'
                          : 'hover:shadow-md'
                    }`}
                    style={{
                      backgroundColor: 'rgba(255, 255, 255, 0.90)',
                      borderColor: '#cbd5e1'
                    }}
                  >
                    {/* Column Header */}
                    <div 
                      className="column-drag-handle flex justify-between items-center p-2.5 rounded-xl mb-2.5 bg-slate-100/90 border border-slate-200/80 shadow-xs transition-colors shrink-0 cursor-grab active:cursor-grabbing select-none"
                      title="Nhấp và kéo để đổi vị trí cột"
                    >
                      <div className="flex items-center gap-1.5 min-w-0 flex-1">
                        <span className="text-slate-400 hover:text-slate-600 transition-opacity shrink-0 text-sm leading-none select-none cursor-grab" title="Kéo thả cột">
                          ⠿
                        </span>
                        <h2 className="font-bold text-[14px] truncate tracking-tight text-slate-800" title={col.name}>
                          {col.name}
                        </h2>
                      </div>
                      <div className="flex items-center gap-1.5 shrink-0">
                        <span className="text-[11px] font-bold px-2 py-0.5 rounded-lg bg-white border border-slate-200 text-slate-600 shadow-xs">
                          {col.cards.length} thẻ
                        </span>
                        <button
                          type="button"
                          onClick={(e) => {
                            e.stopPropagation();
                            setIsThemeModalOpen(true);
                          }}
                          className="w-6 h-6 rounded-lg bg-white hover:bg-slate-50 border border-slate-200 flex items-center justify-center text-xs transition-all cursor-pointer shadow-xs hover:scale-105"
                          title="Đổi màu nền bảng"
                        >
                          🎨
                        </button>
                      </div>
                    </div>
                
                    {/* Cards List inside column with vertical scroll */}
                    <div className="flex-1 overflow-y-auto column-cards-scrollbar pr-1 flex flex-col gap-2.5 min-h-0 pt-0.5">
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
                            className={`task-card-item bg-white rounded-xl border shadow-xs hover:shadow-md hover:-translate-y-0.5 transition-all duration-200 p-3 cursor-pointer select-none group ${
                              isCardAllDone 
                                ? 'border-emerald-300 bg-gradient-to-br from-white to-emerald-50/40' 
                                : 'border-slate-200/90 hover:border-sky-300'
                            }`}
                          >
                            <div className="flex justify-between items-start gap-2 mb-2">
                              <h3 className="font-bold text-slate-800 text-[13px] leading-snug group-hover:text-sky-600 transition-colors tracking-tight">
                                {card.title}
                              </h3>
                              <span className="text-slate-300 group-hover:text-sky-500 text-xs transition-colors shrink-0 mt-0.5">
                                ➜
                              </span>
                            </div>
                            
                            {/* Progress bar */}
                            <div className="flex items-center gap-2 mb-2.5">
                              <div className="flex-1 h-1.5 bg-slate-100 rounded-full overflow-hidden">
                                <div 
                                  className={`h-full rounded-full transition-all duration-500 ${isCardAllDone ? 'bg-gradient-to-r from-emerald-400 to-emerald-500' : 'bg-gradient-to-r from-sky-400 to-sky-600'}`}
                                  style={{ width: `${progressPct}%` }}
                                />
                              </div>
                              <div className="flex items-center gap-1 shrink-0">
                                <span className={`text-[12px] font-bold ${isCardAllDone ? 'text-emerald-600' : 'text-sky-600'}`}>
                                  {progressPct}%
                                </span>
                                <span className="text-[10px] font-medium text-slate-400">
                                  ({card.completedCount}/{card.totalCount})
                                </span>
                              </div>
                            </div>

                            {/* Card badges */}
                            <div className="flex items-center gap-1 flex-wrap">
                              {testCount > 0 && (
                                <span className="text-[10px] font-bold px-2 py-0.5 rounded-lg bg-sky-50 text-sky-700 border border-sky-100">
                                  📝 {testCount} đề thi
                                </span>
                              )}
                              {manualCount > 0 && (
                                <span className="text-[10px] font-bold px-2 py-0.5 rounded-lg bg-emerald-50 text-emerald-700 border border-emerald-100">
                                  ✓ {manualCount} việc
                                </span>
                              )}
                              {isCardAllDone && (
                                <span className="text-[10px] font-bold px-2 py-0.5 rounded-lg bg-emerald-100 text-emerald-800 border border-emerald-200">
                                  ✓ Xong
                                </span>
                              )}
                              {hasOverdue && (
                                <span className="text-[10px] font-bold px-2 py-0.5 rounded-lg bg-rose-50 text-rose-600 border border-rose-200">
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

            {/* Floating Bottom Controls centered above scrollbar */}
            {bottomActions && (
              <div className="absolute bottom-5 left-1/2 -translate-x-1/2 z-30 pointer-events-none">
                <div className="pointer-events-auto">
                  {bottomActions}
                </div>
              </div>
            )}
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
            className="fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-md flex items-center justify-center p-3 sm:p-6 animate-in fade-in duration-200"
            onClick={() => setActiveModalCard(null)}
          >
            <div 
              className="relative w-full max-w-2xl bg-white rounded-[2rem] shadow-2xl border border-slate-200 flex flex-col max-h-[88vh] overflow-hidden animate-in zoom-in-95 duration-200"
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
                    <span className="text-xs text-slate-500 font-semibold">• {activeModalCard.boardTitle}</span>
                  </div>
                  <h2 className="text-xl sm:text-2xl font-black text-slate-900 leading-tight tracking-tight">
                    {currentCard.title}
                  </h2>
                  
                  {/* Progress bar in header */}
                  <div className="mt-3 flex items-center gap-3">
                    <div className="flex-1 h-2.5 bg-black/10 rounded-full overflow-hidden">
                      <div 
                        className={`h-full rounded-full transition-all duration-500 ${isCardAllDone ? 'bg-gradient-to-r from-emerald-400 to-emerald-500' : 'bg-gradient-to-r from-sky-400 to-[#0ea5e9]'}`}
                        style={{ width: `${progressPct}%` }}
                      />
                    </div>
                    <span className="text-[13px] font-black shrink-0" style={{ color: modalTheme.hasColor ? modalTheme.text : '#0f172a' }}>
                      {progressPct}% ({currentCard.completedCount}/{currentCard.totalCount} hoàn thành)
                    </span>
                  </div>
                </div>

                <button
                  type="button"
                  onClick={() => setActiveModalCard(null)}
                  className="w-9 h-9 rounded-full bg-white/90 hover:bg-white text-slate-500 hover:text-slate-800 flex items-center justify-center transition-all shadow-sm shrink-0 border border-slate-200/80 cursor-pointer hover:scale-105"
                  title="Đóng (ESC)"
                >
                  ✕
                </button>
              </div>

              {/* Modal Body - Scrollable Items */}
              <div className="flex-1 overflow-y-auto custom-scrollbar p-5 sm:p-6 space-y-3 bg-slate-50/50">
                <div className="flex items-center justify-between mb-2">
                  <span className="text-[11px] font-black text-slate-400 uppercase tracking-widest">
                    Danh sách bài tập ({currentCard.items.length} mục)
                  </span>
                  <span className="text-[11px] font-semibold text-slate-400">
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
                                ) : testScore ? (
                                  <span className="inline-flex items-center gap-1 text-[10px] px-2.5 py-0.5 rounded-full bg-rose-100 text-rose-700 font-bold border border-rose-200">
                                    ⚠️ Chưa đạt: {testScore.total_score > 0 ? `${testScore.score}/${testScore.total_score}` : testScore.score} ({testScore.percent}%) • Cần ≥ 50%
                                  </span>
                                ) : (
                                  <span className="inline-flex items-center text-[10px] px-2.5 py-0.5 rounded-full bg-slate-100 text-slate-500 font-medium">
                                    Chưa làm (Cần đạt ≥ 50%)
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
                              ) : testScore ? (
                                <button 
                                  onClick={() => {
                                    if (item.test_id && onStartTest) {
                                      onStartTest(item.test_id);
                                      setActiveModalCard(null);
                                    }
                                  }}
                                  className="text-xs font-bold px-3.5 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-600 text-white shadow-xs transition-all flex items-center gap-1.5 shrink-0 cursor-pointer"
                                  title="Làm lại để đạt điểm yêu cầu (≥ 50%)"
                                >
                                  Làm lại để đạt điểm ➜
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
                <div className="text-[13px] text-slate-400 font-medium">
                  {isCardAllDone ? '🎉 Bạn đã hoàn thành toàn bộ công việc trong thẻ này!' : '💡 Nhấp vào bài để bắt đầu làm hoặc tick chọn việc đã làm'}
                </div>
                <button
                  type="button"
                  onClick={() => setActiveModalCard(null)}
                  className="px-5 py-2.5 rounded-2xl text-[13px] font-black bg-slate-100 hover:bg-slate-200 text-slate-700 transition-all cursor-pointer hover:shadow-sm"
                >
                  Đóng
                </button>
              </div>
            </div>
          </div>
        );
      })()}

      {/* ================= BOARD BACKGROUND THEME MODAL (TRELLO STYLE) ================= */}
      <BoardThemeModal
        isOpen={isThemeModalOpen}
        currentTheme={boardTheme}
        onSelectTheme={handleSelectTheme}
        onApplyCustomColor={handleApplyCustomColor}
        onClose={() => setIsThemeModalOpen(false)}
      />

      <style>{`
        /* Horizontal scrollbar for the board at bottom - 14px thick, easy to grab like Trello */
        .board-horizontal-scrollbar {
          scrollbar-width: auto;
          scrollbar-color: rgba(0, 0, 0, 0.35) rgba(0, 0, 0, 0.08);
        }
        .board-horizontal-scrollbar::-webkit-scrollbar {
          height: 14px;
        }
        .board-horizontal-scrollbar::-webkit-scrollbar-track {
          background: rgba(0, 0, 0, 0.08);
          border-radius: 9999px;
          margin: 0 16px 2px 16px;
        }
        .board-horizontal-scrollbar::-webkit-scrollbar-thumb {
          background-color: rgba(0, 0, 0, 0.32);
          border-radius: 9999px;
          border: 2px solid transparent;
          background-clip: padding-box;
          cursor: grab;
        }
        .board-horizontal-scrollbar::-webkit-scrollbar-thumb:hover {
          background-color: rgba(0, 0, 0, 0.55);
        }
        .board-horizontal-scrollbar::-webkit-scrollbar-thumb:active {
          background-color: rgba(0, 0, 0, 0.75);
          cursor: grabbing;
        }

        /* Dark theme scrollbar */
        .board-horizontal-scrollbar.dark-theme {
          scrollbar-color: rgba(255, 255, 255, 0.45) rgba(255, 255, 255, 0.12);
        }
        .board-horizontal-scrollbar.dark-theme::-webkit-scrollbar-track {
          background: rgba(255, 255, 255, 0.12);
        }
        .board-horizontal-scrollbar.dark-theme::-webkit-scrollbar-thumb {
          background-color: rgba(255, 255, 255, 0.45);
        }
        .board-horizontal-scrollbar.dark-theme::-webkit-scrollbar-thumb:hover {
          background-color: rgba(255, 255, 255, 0.75);
        }

        /* Column cards vertical scrollbar */
        .column-cards-scrollbar::-webkit-scrollbar {
          width: 5px;
        }
        .column-cards-scrollbar::-webkit-scrollbar-track {
          background: transparent;
        }
        .column-cards-scrollbar::-webkit-scrollbar-thumb {
          background-color: #cbd5e1;
          border-radius: 9999px;
        }
        .column-cards-scrollbar::-webkit-scrollbar-thumb:hover {
          background-color: #94a3b8;
        }

        .custom-scrollbar::-webkit-scrollbar {
          width: 5px;
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

function BoardThemeModal({
  isOpen,
  currentTheme,
  onSelectTheme,
  onApplyCustomColor,
  onClose
}: {
  isOpen: boolean;
  currentTheme: BoardTheme;
  onSelectTheme: (theme: BoardTheme) => void;
  onApplyCustomColor: (hex: string) => void;
  onClose: () => void;
}) {
  const [customHex, setCustomHex] = useState(currentTheme.boardBg.startsWith('#') ? currentTheme.boardBg : '#e0f2fe');

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/45 backdrop-blur-xs p-4 animate-in fade-in duration-200">
      <div 
        className="fixed inset-0" 
        onClick={onClose}
      />
      <div className="relative bg-white rounded-3xl shadow-2xl border border-slate-200 w-full max-w-lg overflow-hidden flex flex-col z-10 animate-in zoom-in-95 duration-200">
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-100 flex items-center justify-between bg-slate-50/70">
          <div className="flex items-center gap-2.5">
            <span className="text-2xl">🎨</span>
            <div>
              <h3 className="font-bold text-slate-800 text-base">Đổi màu nền bảng (Trello Style)</h3>
              <p className="text-slate-400 text-xs mt-0.5">Chọn màu nền yêu thích cho toàn bộ không gian làm việc</p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-white hover:bg-slate-100 border border-slate-200 text-slate-500 flex items-center justify-center font-bold text-sm transition-all cursor-pointer shadow-xs"
          >
            ✕
          </button>
        </div>

        {/* Body */}
        <div className="p-6 space-y-5 max-h-[70vh] overflow-y-auto custom-scrollbar">
          {/* Preset Palettes */}
          <div>
            <label className="text-xs font-bold text-slate-500 uppercase tracking-wider block mb-3">
              Bảng màu gợi ý
            </label>
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
              {BOARD_THEMES.map((theme) => {
                const isSelected = currentTheme.id === theme.id || currentTheme.boardBg === theme.boardBg;
                return (
                  <button
                    key={theme.id}
                    type="button"
                    onClick={() => {
                      onSelectTheme(theme);
                      onClose();
                    }}
                    className={`rounded-2xl p-2.5 border text-left transition-all cursor-pointer flex flex-col gap-2 group hover:scale-[1.02] hover:shadow-md ${
                      isSelected 
                        ? 'border-sky-500 ring-2 ring-sky-400/40 shadow-sm bg-sky-50/20' 
                        : 'border-slate-200 hover:border-slate-300 bg-white'
                    }`}
                  >
                    {/* Mini board preview */}
                    <div 
                      className="w-full h-14 rounded-xl border border-black/5 p-1.5 flex flex-col justify-between shadow-inner"
                      style={{ background: theme.boardBg }}
                    >
                      {/* Mini Title bar */}
                      <div 
                        className="h-2.5 w-full rounded-md shadow-2xs"
                        style={{ background: theme.titleBg }}
                      />
                      {/* Mini Columns */}
                      <div className="flex gap-1 h-6">
                        <div className="w-1/3 bg-white/90 rounded-sm shadow-2xs" />
                        <div className="w-1/3 bg-white/90 rounded-sm shadow-2xs" />
                        <div className="w-1/3 bg-white/90 rounded-sm shadow-2xs" />
                      </div>
                    </div>

                    <div className="flex items-center justify-between px-0.5">
                      <span className="font-bold text-xs text-slate-700 truncate group-hover:text-sky-600">
                        {theme.name}
                      </span>
                      {isSelected && (
                        <span className="text-[11px] font-black text-sky-600 shrink-0">✓</span>
                      )}
                    </div>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Custom Color Picker */}
          <div className="pt-4 border-t border-slate-100">
            <label className="text-xs font-bold text-slate-500 uppercase tracking-wider block mb-2.5">
              Hoặc chọn mã màu tùy thích
            </label>
            <div className="flex items-center gap-3">
              <input
                type="color"
                value={customHex}
                onChange={(e) => setCustomHex(e.target.value)}
                className="w-11 h-10 rounded-xl cursor-pointer border border-slate-200 p-0.5 bg-white shadow-xs shrink-0"
              />
              <input
                type="text"
                value={customHex}
                onChange={(e) => setCustomHex(e.target.value)}
                placeholder="#e0f2fe"
                className="flex-1 px-3.5 py-2 text-xs font-mono font-bold rounded-xl border border-slate-200 bg-slate-50 focus:bg-white focus:border-sky-500 outline-none uppercase"
              />
              <button
                type="button"
                onClick={() => {
                  onApplyCustomColor(customHex);
                  onClose();
                }}
                className="px-4 py-2 rounded-xl text-xs font-bold text-white bg-sky-600 hover:bg-sky-700 transition-all cursor-pointer shadow-xs active:scale-95 shrink-0"
              >
                Áp dụng
              </button>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-3.5 border-t border-slate-100 bg-slate-50/70 flex items-center justify-between">
          <button
            type="button"
            onClick={() => {
              onSelectTheme(DEFAULT_BOARD_THEME);
              onClose();
            }}
            className="text-xs font-bold text-slate-500 hover:text-sky-600 transition-colors cursor-pointer"
          >
            ↺ Khôi phục mặc định (Xanh nhạt)
          </button>
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-1.5 rounded-xl text-xs font-bold bg-white border border-slate-200 hover:bg-slate-100 text-slate-700 transition-all cursor-pointer shadow-xs"
          >
            Đóng
          </button>
        </div>
      </div>
    </div>
  );
}
